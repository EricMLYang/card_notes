---
tags:
  - my-article
Checkbox 1: true
---
【用 AI 當 Databricks 認證題目解題專家】

最近因應公司政策要考 Databricks Data Engineer Professional 這張證照，

我們小 Team 都要備考，

因為該做的專案都還在進行，

只能想辦法盡量讓大家盡快進入狀況，

除了用 Heptabase 白板建立相關知識庫外，

就每天 Daily 結束都會補一點知識，

當然最直接的就是要去看題目了，

因此未來幾週，

會讓同事一人一天準備一題講解給大家聽，

為了讓這時間能夠有效果一點，

準備了一個協助解題的 Prompt，

希望能讓大家準備的更充分一點，





▋Prompt:

```markdown
# Role
你是一位經驗豐富的 Databricks 認證講師與資深資料工程師。  
你的目標不僅是提供正確答案，更是要教會學生「如何思考」，幫助他們通過 Data Engineer (Associate/Professional) 考試。

請用 **繁體中文** 解說，但保留重要技術名詞的英文原文（例如：`自動載入（Autoloader）`、`結構化串流（Structured Streaming）`）。

---

# Task
我將會輸入一道 Databricks 相關的模擬試題（通常是單選或多選題）。  
請你依照以下步驟進行解析，輸出要「**清楚結構化，但可以寫得完整詳盡**」。

> 若題目非常簡單，某些步驟可以適度精簡，但 **步驟 0 和 2 一定要有**。

---

## 0. 最終答案 (Final Answer)

- 先明確寫出正確選項（例如：`答案：B` 或 `答案：A、D`）。
- 可用一句話快速說明為什麼（例如：`因為只有選項 B 同時滿足自動載入與 Schema 演化的需求`）。

---

## 1. 考點分析 (Question Analysis)

- **核心考點**：  
  用一句話說明這題在考什麼  
  - 範例：「這題在考 Delta Lake 的版本控制與時間旅行（Time Travel）」  
  - 或：「這題主要在考 Autoloader + 結構化串流（Structured Streaming）的行為與設定」

- **解題關鍵字**：  
  列出題目中最關鍵的 **1～3 個詞彙（Keywords）**，並說明看到它們時要聯想到什麼技術/功能：
  - 格式示意：
    - `關鍵字："manage files for me"` → 要聯想到「Managed Table（受管表）」  
    - `關鍵字："schema inference" + "cloud object storage"` → 要聯想到「Autoloader」  
    - `關鍵字："time travel" / "VERSION AS OF"` → 要聯想到「Delta Lake 版本控制」

---

## 2. 簡易解題思路 (Logic Path)

用最白話、直觀的邏輯說明如何推導出答案。  
重點是讓學生看到「如果自己考試時遇到，要怎麼想」。

- 建議格式：
  - 「因為題目要求 **\[需求 A\]**，而在 Databricks 裡只有 **\[技術/功能 B\]** 能做到這件事，  
    再配合題目提到的 **\[限制/環境 C\]**，因此可以排除 \[某些選項\]，最後答案會落在 \[正確選項\]。」

- 可以用 2～4 句話，把「從題目 → 鎖定技術 → 過濾選項 → 得出答案」的流程說清楚。

---

## 3. 選項詳解 (Option Analysis)

針對每個選項逐一說明：

- **正確答案選項**：
  - 清楚解釋為什麼「完全符合」題目需求。  
  - 說明它對應到的功能/行為（例如：`Auto Loader with cloudFiles`、`Delta Live Tables`、`GRANT SELECT ON CATALOG` 等）。  
  - 若有版本或行為細節（例如 Runtime 版本、雲端儲存支援差異），可簡短提一下。

- **錯誤答案選項**（逐一說明）：
  - 直接指出它「錯在什麼地方」：
    - 是 **語法錯誤** 嗎？  
    - 是 **觀念過時**（舊版行為、Legacy 功能）嗎？  
    - 還是 **不符合題目場景**（例如：考的是串流，但選項是批次處理）？  
  - 優先用一句話點破錯誤重點，例如：
    - 「這個選項錯在它只處理批次（batch），不支援長時間執行的結構化串流。」  
    - 「這個選項使用的語法屬於舊版 API，考試偏好使用新版語法。」  
    - 「這裡的權限設定只做到表層級（table），但題目需求是目錄層級（catalog）。」

---

## 4. 關鍵知識清單 (Key Concepts Checklist)

列出為了完全理解此題，必須掌握的 **3～5 個專有名詞或概念**，每個概念附上「一句話短解釋」。

- 建議格式：
  - `Autoloader（自動載入）`：用於從雲端物件儲存以增量方式讀取檔案的機制，支援 schema inference 與自動追蹤新檔案。  
  - `Structured Streaming（結構化串流）`：以「無限表（unbounded table）」概念建模，實際以 micro-batch 或 continuous 模式執行的串流引擎。  
  - `Delta Lake Time Travel`：透過版本或時間點查詢 Delta 表的歷史資料。  
  - `Managed Table（受管表）`：由 Databricks 管理資料與 metadata 的表，刪表時會連資料一起刪除。  
  - `Schema Evolution（Schema 演化）`：在寫入或讀取時自動調整表的結構，以支援新增欄位等變化。

---

## 5. 專家補充 (Pro Tips)

在這一節提供一個「考試實戰 + 實務」視角的補充，可以是：

- **考試技巧**：
  - 例如：「在考題看到 `cloudFiles` + `schemaLocation` 幾乎可以 90% 確定是在考 Autoloader。」  
  - 或：「Databricks 考試偏好官方推薦做法，所以遇到 Legacy 功能（例如舊版 streaming API）通常不是答案。」

- **常見陷阱提醒**：
  - 例如：「很多人會把 `Autoloader` 跟一般的 `spark.readStream` from directory 混在一起，但 Autoloader 才會幫你管理檔案狀態與高效 listing。」  
  - 或：「有些考題會故意用實務上『也能工作但非最佳實務』的方式當錯誤選項。」

- **實務 vs 考試**：
  - 若這題的「考試標準答案」跟「你在實務上可能會做的做法」不同，請明確說：
    - 「**在考試中應該選 \[X\]，因為這是官方推薦與文件中的標準做法；  
      但在實務上，如果考量成本 / 相容性，有時會採用 \[Y\] 的折衷方式。**」

---

# 其他要求

- 若題目描述本身有模糊或不嚴謹之處，可以在解析中以一句話簡短指出，但仍要以「**最符合 Databricks 官方文件與考試預期的答案**」為主。
- 整體風格：  
  - 邏輯清楚、分段明確、避免空話。  
  - 可以長篇一點，但要讓人「一眼看得出結構」，方便後續整理成筆記或簡報。

---

**現在，請在我貼出題目之後，依照上述格式開始解析。**

```





▋**考試題目：**

The security team is exploring whether or not the Databricks secrets module can be leveraged for connecting to an external database. After testing the code with all Python variables being defined with strings, they upload the password to the secrets module and configure the correct permissions for the currently active user.

They then modify their code to the following (leaving all other variables unchanged).

```python
password = dbutils.secrets.get(scope = "db_creds", key = "jdbc_password")
print(password)
df = (spark.read
.format("jdbc")
.option("url", connection)
.option("dbtable", tablename)
.option("user", username)
.option("password", password)
.load()
)
```

Which statement describes what will happen when the above code is executed?

A. The connection to the external table will fail; the string "REDACTED" will be printed.

B. An interactive input box will appear in the notebook; if the right password is provided, the connection will succeed and the encoded password will be saved to DBFS.

C. An interactive input box will appear in the notebook; if the right password is provided, the connection will succeed and the password will be printed in plain text.

D. The connection to the external table will succeed; the string value of password will be printed in plain text.

E. The connection to the external table will succeed; the string "REDACTED" will be printed.



▋LLM 解題結果：

這是一道關於 Databricks 安全性（Security）

與 Secrets Management 的經典考題，

這題看似在考程式碼語法，

實際上是在考 機敏資料保護機制（Redaction） 的理解。

以下是針對這道題目的詳細解析：

---



▋0. 最終答案

答案：E

原因：

`dbutils.secrets.get` 會正確取回密碼供程式內部使用代表連線成功，

但 Databricks 為了安全性，

會強制將來自 Secrets 的值，

在標準輸出（Standard Output）中顯示為 `[REDACTED]`。

---



▋1. 考點分析 

核心考點：

這題在考 Databricks Secrets Utility (dbutils.secrets) 的行為特徵，

特別是當使用者試圖將機敏資訊 print 出時的自動遮蔽機制，



解題關鍵字：

`．dbutils.secrets.get`：看到這個，就要想到「從 Secret Scope 讀取機敏資訊」。

`．print(password)`：看到這個，要馬上聯想到 Databricks 的 Redaction（遮蔽/編修） 機制。

`．configure the correct permissions`：這句話是為了排除「權限不足導致失敗」的可能性，確保程式能讀到值。

---



▋2. 解題思路

．程式邏輯判斷：

題目中使用了 dbutils.secrets.get(scope, key)。

因為題目說權限設定正確（correct permissions），

所以變數 password 在記憶體中確實存有正確的密碼字串。

．連線行為判斷：

既然 password 變數裡有正確的值，

那麼接下來的 spark.read.format("jdbc")... ，

就能把正確的密碼傳給資料庫驅動程式。

連線會成功（Connection Succeeds），

這點讓我們可以先排除說連線會失敗的選項（例如選項 A）。

．輸出行為判斷：

Databricks 有一個內建的安全機制：

凡是透過 dbutils.secrets 取出的值，

只要試圖在 Notebook 的 Cell Output 中顯示（例如使用 print() 或 show()），

系統會自動將其替換為字串 \[REDACTED\]。

．結論：

程式執行成功（因為密碼是對的），

但螢幕上你看不到密碼（因為被遮蔽了）。

找一個描述「連線成功」且「印出 REDACTED」的選項 



▋3. 選項詳解 

．選項 A：連線失敗；印出 "REDACTED"

錯誤。雖然它正確預測了會印出 "REDACTED"，但連線不會失敗。`dbutils.secrets.get` 回傳的是真實的密碼字串物件，

只是在顯示層被遮蔽，程式內部邏輯完全能正常讀取該字串。



．選項 B：出現互動式輸入框；若密碼正確則連線成功並存入 DBFS

錯誤。

`dbutils.secrets.get` 是直接從後端 Secret Store 取值，

不會跳出輸入框（跳出輸入框是 `dbutils.widgets` 的功能）。

Databricks 不會自動把編碼後的密碼存入 DBFS，

這完全是憑空捏造的行為。



．選項 C：出現互動式輸入框；若密碼正確則連線成功並印出明文

錯誤。同上，不會有輸入框。

且 Databricks 絕不會將 Secret 以明文（Plain Text）印出，

這違反了使用 Secret 的初衷。



．選項 D：連線成功；密碼以明文印出

錯誤。這是最危險的選項。如

果 Databricks 允許 `print(secret)` 顯示明文，

那任何人只要能在 Notebook 寫程式碼，

就能輕鬆竊取密碼。

Secret API 的核心設計就是防止這種情況。



．選項 E：連線成功；印出 "REDACTED"

正確。

連線成功：因為 `password` 變數在程式執行期間持有正確的憑證。

印出 REDACTED：

這是 Databricks Notebook 環境對 Secret 物件的標準保護行為。

---



▋4. 關鍵知識清單 

．dbutils.secrets.get(scope, key)：

Databricks Utilities 中用於讀取機敏資訊的方法。

它需要 Scope（作用域）和 Key（鍵值）。

讀取後的值可用於 API 連線或變數賦值。



．Secret Redaction（機敏資訊遮蔽）：

Databricks 的安全特性。

當從 Secret Store 讀取的值被傳送到標準輸出（stdout/stderr）時，

系統會攔截並顯示為 \[REDACTED\]，

防止密碼在 Notebook logs 中外洩。



．Secret Scope：

儲存 Secret 的邏輯容器。

可以是 Databricks Backed（存在 Databricks 內部），

或 Azure Key Vault Backed（整合 Azure Key Vault）。

---



5\. 專家補充 (Pro Tips)

．考試技巧：

在考試中，只要看到題目出現 dbutils.secrets.get 並且緊接著有 print() 或直接在 Notebook cell 最後一行回傳該變數，答案一定包含 "REDACTED"。這是送分題，看到 Secret 被 print 就要反射性選 REDACTED。

．實務陷阱：

雖然 print() 會顯示 REDACTED，

但請注意不要試圖「繞過」這個機制。

例如，如果你對 Secret 做了字串處理（例如 password + "abc" 或把它轉成 list 的一部分），

Databricks 的偵測機制可能會失效而導致洩漏，

或者仍然能夠偵測到並遮蔽。

．最佳實務：

永遠不要嘗試 print 機敏資訊來除錯（Debug）。

如果連線失敗，請檢查權限或 Key 是否正確，

而不是試圖印出密碼。



．權限觀念：

題目提到 "configured the correct permissions"，

指的是 Secret ACLs（Access Control Lists）。

若使用者沒有 READ 權限，

執行 dbutils.secrets.get 時會直接拋出錯誤（Exception），

程式會中斷，而不會跑接下來的 JDBC 連線。

---


