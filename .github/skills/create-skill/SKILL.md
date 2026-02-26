---
name: create-skill
description: 根據用戶需求建立符合 Claude Agent Skills / GitHub Copilot Agent Skills 規範的新 Skill。適用於用戶說「幫我建立 skill」「新增技能」「create a new skill」「我想做一個自動化流程」時。Use when user asks to create a new agent skill.
---

# Skill: Create Skill（技能建立助理）

## 目標

根據用戶描述的需求，建立符合 Claude Agent Skills / GitHub Copilot Agent Skills 規範的 `SKILL.md`，並在需要時放入可參考的 scripts / 範例檔案。

## Skill 規範

### 目錄結構
```
.github/
└── skills/
    └── [skill-name]/
        ├── SKILL.md      <-- 核心定義檔 (必備)
        └── [輔助資源]    <-- 可選
```

### SKILL.md 必要格式

```markdown
---
name: skill-name
description: 觸發條件描述（中英文皆可）。適用於用戶說「XXX」「YYY」時。Use when user asks to...
---

# Skill: Skill Name（技能名稱）

## 目標
[一句話說明這個 skill 要達成什麼]

## 執行流程
[描述 skill 的工作步驟]

## 輸出格式
[定義輸出的結構]

## 操作指引
**觸發條件**：
- 用戶說「...」
- 用戶說「...」

## 禁止事項
- ❌ [不應該做的事]
```

### 關鍵規則

1. **YAML Frontmatter 必備**
   - `name`: 小寫、用連字號分隔（如 `break-cards`）
   - `description`: 包含中英文觸發條件，讓 Copilot 知道何時啟用

2. **不要用 code fence 包裹整個檔案**
   - ❌ 錯誤：用 ````skill 包住整個內容
   - ✅ 正確：直接以 `---` 開頭

3. **Description 要具體**
   - 列出用戶可能說的關鍵詞
   - 中英文都要有，增加觸發機率

## 執行流程

### Step 1: 收集需求

詢問用戶：

* 這個 skill 要解決什麼問題？
* 用戶會怎麼觸發它？（用戶會說什麼話？）
* 期望的輸出是什麼？
* 是否已有參考檔案／現成 scripts（可選）：放哪裡、用什麼語言、要不要提供 sample input/output？

### Step 2: 設計 Skill 結構

根據需求決定：

* `name`: 簡潔的識別名稱（小寫、用連字號分隔）
* 執行流程的步驟（可落地、可操作）
* 輸出格式（明確、可複製）
* 禁止事項（避免誤用/風險）

### Step 3: 建立檔案與資料夾結構

1. 建立目錄：`.github/skills/[skill-name]/`
2. 建立檔案：`SKILL.md`（放在 skill 根目錄）
3. 若有 scripts / 參考檔案，使用以下結構（必要就好，不要硬塞）：

```
.github/skills/[skill-name]/
  SKILL.md
  scripts/          # 可執行腳本（可選）
  examples/         # 範例輸入/輸出（可選）
  templates/        # 產出模板（可選）
  assets/           # 小型靜態資源（可選）
```

放置規則：

* `scripts/`：用來「被呼叫執行」的腳本（例如 python/js/sh），檔名要自解釋，避免過多相依。
* `examples/`：放 sample input/output、mock data、期望輸出，讓 agent 能對齊格式。
* `templates/`：放要產出的文件模板（md/yaml/json 等）。
* `assets/`：只放小檔案（例如示意圖/小字典），不要放大型檔或機密。

4. 確保 `SKILL.md` 格式正確（無多餘 code fence，直接以 `---` 開頭）。

### Step 4: 驗證

檢查：

* ✅ 檔案開頭是 `---`（不是 code fence）
* ✅ YAML frontmatter 包含 `name` 和 `description`
* ✅ `description` 包含中英文觸發關鍵詞
* ✅ 有清楚的執行流程、輸出格式、與禁止事項
* ✅ 若有 scripts/examples/templates：路徑正確、命名清楚、README 不必需（資訊寫在 SKILL.md 即可）

## 輸出格式

建立完成後回報：

```
✅ Skill 建立完成

📁 位置：.github/skills/[skill-name]/
- SKILL.md
- scripts/ (optional)
- examples/ (optional)
- templates/ (optional)

🏷️ 名稱：[skill-name]
🎯 觸發：「...」「...」

請重新載入 VS Code 或執行 /skills list 確認。
```

## 操作指引

**觸發條件**：
- 用戶說「幫我建立 skill」
- 用戶說「新增一個技能」
- 用戶說「Create a new skill」
- 用戶說「我想做一個自動化流程」

**執行步驟**：

1. 若用戶已提供完整需求 → 直接建立
2. 若需求不明確 → 先詢問澄清問題
3. 若用戶提供 scripts/參考檔案 → 依用途放入 `scripts/`、`examples/`、`templates/`
4. 建立檔案後 → 輸出驗證結果

## Skill 範例模板

### 簡單型（單一任務）

```markdown
---
name: example-simple
description: 簡單描述功能。適用於用戶說「做X」「執行Y」時。Use when user asks to do X.
---

# Skill: Example Simple

## 目標
[一句話目標]

## 執行流程
1. [步驟一]
2. [步驟二]
3. [步驟三]

## 輸出格式
[定義輸出]

## 操作指引
**觸發條件**：
- 用戶說「...」

## 禁止事項
- ❌ [禁止事項]
```

### 複雜型（多步驟流程）

```markdown
---
name: example-complex
description: 複雜功能描述。適用於用戶說「處理A」「分析B」「建立C」時。Use when user asks to process A, analyze B, or create C.
---

# Skill: Example Complex

## 目標
[目標描述]

## 核心原則
### 1. [原則一]
[說明]

### 2. [原則二]
[說明]

## 執行流程

### Step 1: [階段名稱]
[詳細說明]

### Step 2: [階段名稱]
[詳細說明]

### Step 3: [階段名稱]
[詳細說明]

## 輸出格式
[詳細定義]

## 操作指引
**觸發條件**：
- 用戶說「...」
- 用戶說「...」

**執行步驟**：
1. [步驟]
2. [步驟]

## 禁止事項
- ❌ [禁止事項一]
- ❌ [禁止事項二]
```

## 禁止事項

* ❌ 不要用 code fence（如 ````skill）包裹整個 SKILL.md 內容
* ❌ 不要遺漏 YAML frontmatter
* ❌ 不要讓 description 太籠統（要有具體觸發詞）
* ❌ 不要建立與現有 skill 重複的功能
* ❌ 在用戶需求不明確時直接產出（應先詢問澄清）
* ❌ 不要把機密/憑證/大型檔案放進 skills 目錄
