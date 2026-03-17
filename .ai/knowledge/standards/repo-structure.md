# Repo Structure Standard (Minimal)

必備結構：
- `.github/skills/_index.yaml`
- `.github/copilot-instructions.md`
- `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`
- `.ai/identity.yaml`
- `.ai/principles.md`
- `.ai/knowledge/glossary.yaml`
- `.ai/interfaces/exports.yaml`, `.ai/interfaces/imports.yaml`
- `.ai/memory/decisions.md`

命名規則：
- `010_CardNotes/01_Index` 需使用 `NN_分類名稱.md`
- `003_Capture`/`015_Write/Draft`/`015_Write/Publish` 依各自日期前綴規範

橋接規則：
- `AGENTS.md` 為核心指令源
- `CLAUDE.md`、`GEMINI.md`、`.github/copilot-instructions.md` 只做橋接與摘要
