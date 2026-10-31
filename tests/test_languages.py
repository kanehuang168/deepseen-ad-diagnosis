from pathlib import Path
import json,subprocess,sys,tempfile,unittest

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills/deepseen-ad-report-lite'

class LanguageTests(unittest.TestCase):
    def test_english_and_chinese_preserve_arithmetic(self):
        with tempfile.TemporaryDirectory() as tmp:
            outputs=[]
            for lang in ['zh-CN','en']:
                p=Path(tmp)/(lang+'.json')
                r=subprocess.run([sys.executable,'-I','-S','-X','utf8',str(SKILL/'scripts/diagnose_ads.py'),str(SKILL/'assets/cup-ads.en.csv'),'--demo','--lang',lang,'--json-output',str(p)],capture_output=True,encoding='utf-8')
                self.assertEqual(r.returncode,0,r.stderr)
                outputs.append(json.loads(p.read_text(encoding='utf-8')))
                self.assertIn('Fictional sample' if lang=='en' else '虚构示例',r.stdout)
            self.assertEqual(outputs[0]['groups'][0]['metrics'],outputs[1]['groups'][0]['metrics'])
            self.assertEqual(outputs[1]['groups'][0]['metrics']['roas'],1.25)
            self.assertEqual(outputs[0]['groups'][0]['known_totals'],outputs[1]['groups'][0]['known_totals'])

    def test_english_rejects_existing_output_without_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'old.md';p.write_text('keep',encoding='utf-8')
            r=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'scripts/diagnose_ads.py'),str(SKILL/'assets/cup-ads.en.csv'),'--lang','en','--output',str(p)],capture_output=True,encoding='utf-8')
            self.assertEqual(r.returncode,2)
            self.assertIn('already exists',r.stderr)
            self.assertEqual(p.read_text(encoding='utf-8'),'keep')

    def test_invalid_english_target_is_reported_in_english(self):
        r=subprocess.run([sys.executable,'-X','utf8',str(SKILL/'scripts/diagnose_ads.py'),str(SKILL/'assets/cup-ads.en.csv'),'--lang','en','--target-roas','nan'],capture_output=True,encoding='utf-8')
        self.assertEqual(r.returncode,2)
        self.assertIn('finite and greater than zero',r.stderr)

if __name__=='__main__':unittest.main()
