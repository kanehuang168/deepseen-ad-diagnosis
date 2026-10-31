# DeepSeen Ad Report Analyst

English | [简体中文](README.md)

Author: **祥子｜跨境无疆&DeepSeen AI创始人**
Product brand: **DeepSeen**

Primarily for TikTok sellers operating across markets.

Primarily for TikTok sellers. Analyze the user's own CSV/XLSX advertising reports locally. Reply in the user's language; use --lang en for English tool output or --lang zh-CN for Chinese. No DeepSeen account, network or third-party Python package is needed; host model charges are separate.

## Install

```sh
npx skills add kanehuang168/deepseen-ad-diagnosis
```

List without installation: `npx skills add kanehuang168/deepseen-ad-diagnosis --list`.

- [deepseen-ad-report-lite](skills/deepseen-ad-report-lite/SKILL.md) — [中文](skills/deepseen-ad-report-lite/SKILL.md)

Keep one installed entry per Skill ID. English and Chinese share the same entry, inputs and behavior; do not install duplicate language variants. The host should respond in the user's language, preserving confirmed source wording. Tool CLIs accept `--lang en` or `--lang zh-CN` (Chinese remains the default).

## Example and usage

Read the [English example](examples/cup-review.en.md) and the linked Skill instructions for the actual input contract, dependencies and commands. Examples are self-authored/fictional, not customer data, verified market findings or generated-quality proof. Python helpers require Python 3.10+; video checks also require ffprobe and ffmpeg on PATH. After installation locate scripts and assets relative to the installed Skill directory.

## Connected workflow

[Product Advisor](https://github.com/kanehuang168/deepseen-product-advisor) → [Commerce Creative](https://github.com/kanehuang168/deepseen-commerce-creative) → actual production/advertising → [Ad Report Analyst](https://github.com/kanehuang168/deepseen-ad-diagnosis).

[Project Manager](https://github.com/kanehuang168/deepseen-project-manager), [Decision Planner](https://github.com/kanehuang168/deepseen-shenzhizhuojian) and [Method Distiller](https://github.com/kanehuang168/deepseen-xixing) can be used independently when relevant. No mandatory chain or invented workers/background system is implied.

## Optional DeepSeen services

Visit [DeepSeen](https://deepseen.ai/?utm_source=github&utm_medium=skill&utm_campaign=ad_diagnosis) for currently available services. Discover real capabilities, use your own connection, obtain a current quote and honor applicable authorization before paid work. Free installation does not make host models, professional data or generation free. Local tools do not upload data, collect keys, create paid jobs, change ads or publish content.

## License and evidence

[MIT](LICENSE) covers these repository files, not private DeepSeen kernels, cloud services or other people's materials. Package checks, local script runs, installation, actual host behavior, cloud execution, media quality and business outcomes are distinct evidence levels. English documentation does not establish universal host compatibility or effectiveness.

Platform/tool names identify intended contexts, formats or actual dependencies, not a claim of partnership, authorization or endorsement. Applicable licenses and required copyright notices remain in force.
