import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest
from decimal import Decimal

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/deepseen-ad-report-lite/scripts/diagnose_ads.py'
spec = importlib.util.spec_from_file_location('diagnose_ads', SCRIPT)
ads = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ads)


class AdScopeTests(unittest.TestCase):
    def test_cup_totals_recompute_from_raw_values(self):
        table, sheet = ads.load_table(ROOT / 'skills/deepseen-ad-report-lite/assets/cup-ads.csv')
        report = ads.analyze(table, sheet)
        self.assertEqual(report['groups'][0]['known_totals']['spend'], Decimal(360))
        self.assertEqual(report['groups'][0]['metrics']['roas'], Decimal('1.25'))

    def test_same_currency_different_market_stays_separate(self):
        report = ads.analyze([['市场', '币种', '消耗', '广告归因成交金额'], ['美国', 'USD', '100', '300'], ['新加坡', 'USD', '100', '20']])
        self.assertEqual(len(report['groups']), 2)
        self.assertEqual({g['scope']['market']:g['metrics']['roas'] for g in report['groups']}, {'美国':Decimal(3), '新加坡':Decimal('.2')})

    def test_unknown_store_sales_does_not_become_ad_revenue(self):
        report = ads.analyze([['消耗', '销售额'], ['100', '900']])
        self.assertIsNone(report['groups'][0]['metrics']['roas'])
        self.assertEqual(report['groups'][0]['coverage']['revenue'], 0)

    def test_user_confirmed_attribution_can_enable_generic_revenue(self):
        report = ads.analyze([['消耗', '销售额'], ['100', '900']], revenue_scope='ad-attributed')
        self.assertEqual(report['groups'][0]['metrics']['roas'], Decimal(9))

    def test_missing_revenue_not_zero_and_blocks_group_ratio(self):
        report = ads.analyze([['消耗', '广告归因成交金额'], ['100', '300'], ['100', '']])
        self.assertIsNone(report['groups'][0]['metrics']['roas'])
        self.assertEqual(report['groups'][0]['coverage']['revenue'], 1)

    def test_cli_has_no_site_package_dependency(self):
        result = subprocess.run([sys.executable, '-I', '-S', '-X', 'utf8', str(SCRIPT), str(ROOT/'skills/deepseen-ad-report-lite/assets/cup-ads.csv'), '--demo'], capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
