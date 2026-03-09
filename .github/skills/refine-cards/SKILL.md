---
name: refine-cards
description: 將 break-cards 產出的 lite 候選卡精煉成正式卡草稿，先給 user 確認；只有 user 確認後，才進行實際分類、寫入 010_CardNotes/02_Cards/{分類資料夾}/、更新 010_CardNotes/01_Index/ 與原文改名。
---

# Skill: Refine Cards（正式卡精煉 + 分類草稿 + 等待確認）

## 目標
將 lite 候選卡精煉成可正式進入卡片盒的高品質卡片草稿。  
這一步要完成：
- 去重
- 合併
- 淘汰
- 正式卡定稿
- 主分類建議
- 目標檔名建議
- 目標路徑建議

**但在 user 確認前，不落檔。**

## 輸入來源
- 來自 `break-cards` 產出的 lite 候選卡
- 或 user 明確指定要 refine 的候選卡草稿

## 個人化偏好來源
- 讀取檔案：`000_MyContext/break_cards_profile.md`
- 用途：
  - 同級候選卡的優先取捨
  - 知識鉤子的主題方向建議
  - 組裝藍圖優先連向哪些知識板塊
- **絕對限制**：
  - 不得因個人偏好保留低訊號卡
  - 不得因個人偏好淘汰高價值異質節點
  - 若某張卡能擴張或修正既有框架，應優先保留並說明原因

## 核心原則

### 1. 正式卡要能獨立理解
每張卡都必須能單獨閱讀，不依賴原文上下文。

### 2. 正式卡要更利於連結
每張卡不只要有正文，還要有：
- 上游連結
- 下游連結
- 關聯對照

### 3. 一卡只能有一個主張中心
若候選卡混了兩個以上概念：
- 拆開
- 或只保留主軸

### 4. 先草稿，後落檔
refine 完成時，先輸出正式卡草稿與分類建議，等 user 確認後才落檔。

## 高訊號篩選器
優先保留符合以下至少 2 項的卡：
- 非顯而易見
- 有清楚機制
- 有取捨或邊界
- 可用於決策
- 可跨情境遷移
- 可檢驗或可觀測
- 挑戰常見共識
- 具有高連結潛力

若未滿 2 項，但明顯屬於：
- 橋接節點
- 反例節點
- 概念澄清節點
- 值得追蹤的問題節點

也可列為 `WEAK KEEP`

## 保留狀態
每張候選卡最後只能是：
- `KEEP`
- `WEAK KEEP`
- `SKIP`

若 `SKIP`，必須寫一句原因。

## 正式卡寫作規格
每張正式卡必須包含：

```text
序號 N
- 標題：[一句話、具觀點、易索引]
- 狀態：[KEEP / WEAK KEEP]
- 類型：[Principle / Pattern / Heuristic / Warning / Question]

- 核心命題（1–2 句）：
  [最值得被引用的判斷]

- 卡片內容（80–250 字）：
  [卡片正文。寫清楚概念本身、背後機制、成立原因與要修正的誤解。必須可獨立理解。]

- 使用情境（1–3 點）：
  [這張卡在什麼判斷、設計、分析、寫作情境下最有用]

- 邊界 / 失效條件（1–3 點）：
  [何時不適用、何時容易誤用]

- 上游連結：
  [依賴的前提、上位概念、底層原理]

- 下游連結：
  [可支撐的決策、框架、方法、行動]

- 關聯對照：
  [互補、對立、反例、修正]

- 分類建議：
  [選一個主分類前綴，例如 1- / 4- / 8-]

- 目標索引：
  [010_CardNotes/01_Index/ 下的對應索引檔]

- 目標卡片路徑：
  [010_CardNotes/02_Cards/{分類資料夾}/ 下的目標檔名，例如：010_CardNotes/02_Cards/03_ai_applications_and_productization/3-001_AI產品化的核心挑戰.md]
```

## 編號分類對照表

**1- Mental Models（思維模型）**
- 索引：`010_CardNotes/01_Index/01_mental_models.md`
- 資料夾：`01_mental_models/`
- 範疇：最底層、可跨領域重用的思維原則（第一性原理、槓桿、系統思考、決策框架、trade-off）

**2- Knowledge Management（知識管理）**
- 索引：`010_CardNotes/01_Index/02_knowledge_management.md`
- 資料夾：`02_knowledge_management/`
- 範疇：知識系統本身（Zettelkasten、PARA、卡片拆解、索引設計、知識萃取流程）

**3- AI Applications and Productization（AI 應用與產品化）**
- 索引：`010_CardNotes/01_Index/03_ai_applications_and_productization.md`
- 資料夾：`03_ai_applications_and_productization/`
- 範疇：AI 如何進入真實業務、產品、流程並產生價值（AI 功能嵌入產品、企業導入、商業價值）

**4- AI Coding and Agent Workflows（AI 編碼與 Agent 工作流）**
- 索引：`010_CardNotes/01_Index/04_ai_coding_and_agent_workflows.md`
- 資料夾：`04_ai_coding_and_agent_workflows/`
- 範疇：AI 如何直接參與開發與知識工作（Copilot、agent skills、prompt engineering、agentic workflow）

**5- Data Engineering and Analytics（資料工程與分析）**
- 索引：`010_CardNotes/01_Index/05_data_engineering_and_analytics.md`
- 資料夾：`05_data_engineering_and_analytics/`
- 範疇：資料工程、分析建模、BI 與決策支持（ETL/ELT、數據管線、指標體系、商業分析框架）

**6- Databricks and Lakehouse Platform（Databricks 與湖倉平台）**
- 索引：`010_CardNotes/01_Index/06_databricks_and_lakehouse_platform.md`
- 資料夾：`06_databricks_and_lakehouse_platform/`
- 範疇：Databricks 平台專屬知識（Unity Catalog、Delta Lake、DLT、Mosaic AI、平台操作）

**7- Product Management（產品管理）**
- 索引：`010_CardNotes/01_Index/07_product_management.md`
- 資料夾：`07_product_management/`
- 範疇：產品管理與產品探索（PMF、opportunity solution tree、discovery、roadmap、problem framing）

**8- System Architecture（系統架構）**
- 索引：`010_CardNotes/01_Index/08_system_architecture.md`
- 資料夾：`08_system_architecture/`
- 範疇：系統架構與高層設計（系統邊界、模組劃分、integration pattern、distributed system）

**9- Software Engineering（軟體工程）**
- 索引：`010_CardNotes/01_Index/09_software_engineering.md`
- 資料夾：`09_software_engineering/`
- 範疇：程式開發本身的方法與原則（clean code、refactoring、design principles、工程品質方法）

**10- Testing, Operations and Reliability（測試、維運與可靠性）**
- 索引：`010_CardNotes/01_Index/10_testing_operations_and_reliability.md`
- 資料夾：`10_testing_operations_and_reliability/`
- 範疇：測試、維運、監控、穩定性（testing、observability、monitoring、SRE、incident response）

**11- Finance and Investment（財務與投資）**
- 索引：`010_CardNotes/01_Index/11_finance_and_investment.md`
- 資料夾：`11_finance_and_investment/`
- 範疇：財務、投資、資產配置與房地產

**12- Personal Growth and Execution（個人成長與執行）**
- 索引：`010_CardNotes/01_Index/12_personal_growth_and_execution.md`
- 資料夾：`12_personal_growth_and_execution/`
- 範疇：人的成長、習慣、執行系統（習慣養成、執行力、精力管理、長期成長策略）

**13- Writing, Communication and Expression（寫作、溝通與表達）**
- 索引：`010_CardNotes/01_Index/13_writing_communication_and_expression.md`
- 資料夾：`13_writing_communication_and_expression/`
- 範疇：寫作、表達、簡報、論述設計（文章組織、商業表達、敘事方式、AI 協助寫作）

**14- Domains, Industries and Macro Trends（領域、產業與宏觀趨勢）**
- 索引：`010_CardNotes/01_Index/14_domains_industries_and_macro_trends.md`
- 資料夾：`14_domains_industries_and_macro_trends/`
- 範疇：產業、技術浪潮、宏觀變化、場域知識（AI 趨勢、產業轉型、市場結構變化）

**15- Design and Aesthetics（設計與美感）**
- 索引：`010_CardNotes/01_Index/15_design_and_aesthetics.md`
- 資料夾：`15_design_and_aesthetics/`
- 範疇：設計原則、美感培養、UI/UX、視覺設計、產品設計美學、品味養成

## 分類判斷順序（避免重複分類）
1. **先判斷是否為宏觀趨勢 / 產業結構變化**：是則優先 `14-`
2. **再判斷是否為明確專業域**：Databricks `6-`、架構 `8-`、軟工 `9-`、測維 `10-`
3. **AI 主題再細分**：
   - AI 應用 / 產品化（對業務產生價值）→ `3-`
   - AI Coding / 開發工作流（幫你做工程）→ `4-`
4. **非特定技術域但可跨域重用的思維框架**：歸 `1-`
5. **個人與知識系統**：
   - 知識如何被組織與管理 → `2-`
   - 人如何成長與執行 → `12-`
   - 如何表達與溝通 → `13-`

### 衝突處理
- 同時命中多類時，只選一個主分類
- 原則為：**這張卡最常被拿來做哪種決策**
- 以用途優先於來源

## 執行流程（強制順序）

### Step 0: 智能讀取候選卡（優化 TOKEN 使用）
在正式精煉前，先使用 `check_breadcards.py` 檢查並快速讀取候選卡：

```bash
python .github/skills/refine-cards/check_breadcards.py <檔案路徑>
```

**根據返回值決定動作：**
- **Exit Code 0**（已有 BreadCards）：
  - ✓ 檔案已完成 break-cards 處理
  - **直接使用輸出的 BreadCards 內容**
  - 大幅減少 TOKEN 消耗，無需讀取整篇原文

- **Exit Code 2**（未拆解）：
  - ❌ 檔案尚未執行 break-cards
  - **告知 user 並建議先執行 break-cards skill**
  - 不繼續執行 refine

- **Exit Code 1 或 3**（錯誤）：
  - ❌ 檔案不存在或讀取失敗
  - 告知 user 並終止

**直接輸入路徑：**
- 如果 user 直接在對話中提供候選卡內容（非從檔案讀取）
- 則直接使用 user 提供的候選卡進行精煉，跳過 Step 0

### Step 1: 讀取候選卡
理解每張候選卡在整體中的角色。

### Step 2: 去重 / 合併 / 拆分
- 合併過度相近卡
- 淘汰弱卡
- 拆分混合卡

### Step 3: 標記保留狀態
對每張候選卡標記：
- `KEEP`
- `WEAK KEEP`
- `SKIP`

### Step 4: 產出正式卡草稿
只對 `KEEP / WEAK KEEP` 產出正式卡。

### Step 5: 補上分類與路徑
每張正式卡都必須補上：
- `分類建議`
- `目標索引`
- `目標卡片路徑`

### Step 6: 向 user 確認
refine 完成後，必須主動詢問 user 是否要：
1. 正式寫入 `010_CardNotes/02_Cards/{分類資料夾}/`
2. 更新 `010_CardNotes/01_Index/`
3. 將原文改名為 `YYYYMMDD_CoreNote_原本檔名.md`

在 user 確認前：
- ❌ 不寫檔
- ❌ 不更新索引
- ❌ 不改名原文

### Step 7: user 確認後才執行落檔
若 user 明確確認，才執行：

#### 7.1 寫正式卡
- 目錄：`010_CardNotes/02_Cards/{分類資料夾}/`（根據索引對應的分類資料夾，如 `ai_engineering/`、`mental_models/` 等）
- 檔名格式：`{分類前綴}{流水號}_{卡片標題}.md`
- 範例：`010_CardNotes/02_Cards/ai_engineering/3-001_AI產品化的核心挑戰.md`

#### 7.2 更新對應索引
- 目錄：`010_CardNotes/01_Index/`
- 將卡片連結加到對應索引檔

#### 7.3 改名原始來源檔案
- 格式：`YYYYMMDD_CoreNote_原本檔名.md`

## 輸出格式（Refine 草稿）

```markdown
# 正式卡精煉結果（待確認）

## A. 篩選結果總覽
- KEEP：X 張
- WEAK KEEP：Y 張
- SKIP：Z 張

## B. 淘汰與合併說明
- [哪些卡被合併，原因]
- [哪些卡被淘汰，原因]
- [哪些卡被拆開，原因]

## C. 正式卡片草稿

序號 1
- 標題：
- 狀態：
- 類型：

- 核心命題：
- 卡片內容：
- 使用情境：
- 邊界 / 失效條件：
- 上游連結：
- 下游連結：
- 關聯對照：

- 分類建議：
- 目標索引：
- 目標卡片路徑：

...

## D. SKIP 清單
- 序號 X：原因
- 序號 Y：原因

## E. 組裝藍圖
- 內部組裝：[哪些卡可組成更大框架]
- 外部對接：[可連到哪些既有主題、索引或知識板塊]
- 實際用途：[可支撐哪些決策、文章、專案或研究方向]

## F. 請 user 確認
請確認是否要：
1. 寫入正式卡到 `010_CardNotes/02_Cards/{分類資料夾}/`
2. 更新索引到 `010_CardNotes/01_Index/`
3. 將原始來源檔案改名為 `YYYYMMDD_CoreNote_原本檔名.md`
```

## 正式卡檔案內容格式（user 確認後寫入）

```markdown
# {卡片標題}

- 狀態：{KEEP / WEAK KEEP}
- 類型：{Principle / Pattern / Heuristic / Warning / Question}
- 分類：{分類前綴}
- 索引：{目標索引}
- 來源：{原始來源檔案路徑}

## 核心命題
{核心命題}

## 卡片內容
{卡片內容}

## 使用情境
- ...
- ...

## 邊界 / 失效條件
- ...
- ...

## 上游連結
- [[...]]
- [[...]]

## 下游連結
- [[...]]
- [[...]]

## 關聯對照
- [[...]]
- [[...]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
```