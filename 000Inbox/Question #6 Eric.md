## **Question #6 Eric**

The security team is exploring whether or not the **Databricks secrets** module can be leveraged for connecting to an external database. After testing the code with all Python variables being defined with strings, they upload the password to the secrets module and **configure the correct permissions** for the currently active user.

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

- A. The connection to the external table will fail; the string "REDACTED" will be printed.

- B. An interactive input box will appear in the notebook; if the right password is provided, the connection will succeed and the encoded password will be saved to DBFS.

- C. An interactive input box will appear in the notebook; if the right password is provided, the connection will succeed and the password will be printed in plain text.

- D. The connection to the external table will succeed; the string value of password will be printed in plain text.

- E. The connection to the external table will succeed; the string "REDACTED" will be printed.



關於 **Databricks Secrets 安全機制**的考題。

**答案：E**（連線成功；印出 `[REDACTED]`）

**核心解析：**

1. **連線成功**：`dbutils.secrets.get` 會在程式執行時取回正確的密碼，因此 JDBC 連線能順利建立。

2. **輸出遮蔽**：為了安全性，Databricks 會自動攔截來自 Secrets 的變數，若嘗試將其列印（`print`）至標準輸出，系統會強制顯示為 **`[REDACTED]`** 以防外洩。

**技巧**：看到 `dbutils.secrets` 被 `print`，輸出結果一定是 `[REDACTED]`，絕不會是明文。



這是一道關於 Databricks 安全性（Security）與 Secrets Management 的經典考題。

這題看似在考程式碼語法，實際上是在考你對 「機敏資料保護機制（Redaction）」 的理解。

以下是針對這道題目的詳細解析：

---

## 0\. 最終答案 (Final Answer)

- **答案：E**

- **原因**：`dbutils.secrets.get` 會正確取回密碼供程式內部使用（因此連線成功），但 Databricks 為了安全性，會強制將來自 Secrets 的值在標準輸出（Standard Output）中顯示為 `[REDACTED]`。

---



## 1\. 考點分析 (Question Analysis)

- 核心考點：

   這題在考 Databricks Secrets Utility (dbutils.secrets) 的行為特徵，特別是當使用者試圖將機敏資訊列印（print）出來時的自動遮蔽機制。

- **解題關鍵字**：

   - `dbutils.secrets.get`：看到這個，就要想到「從 Secret Scope 讀取機敏資訊」。

   - `print(password)`：看到這個，要馬上聯想到 Databricks 的 **Redaction（遮蔽/編修）** 機制。

   - `configure the correct permissions`：這句話是為了排除「權限不足導致失敗」的可能性，確保程式能讀到值。

---



## 2\. 簡易解題思路 (Logic Path)

1. 程式邏輯判斷：

   題目中使用了 dbutils.secrets.get(scope, key)。因為題目說權限設定正確（correct permissions），所以變數 password 在記憶體中確實存有正確的密碼字串。

2. 連線行為判斷：

   既然 password 變數裡有正確的值，那麼接下來的 [spark.read](spark.read).format("jdbc")... 就能把正確的密碼傳給資料庫驅動程式。因此，連線會成功（Connection Succeeds）。這點讓我們可以先排除說連線會失敗的選項（例如選項 A）。

3. 輸出行為判斷：

   Databricks 有一個內建的安全機制：凡是透過 dbutils.secrets 取出的值，只要試圖在 Notebook 的 Cell Output 中顯示（例如使用 print() 或 show()），系統會自動將其替換為字串 \[REDACTED\]。

4. 結論：

   程式執行成功（因為密碼是對的），但螢幕上你看不到密碼（因為被遮蔽了）。

   $\\rightarrow$ 找一個描述「連線成功」且「印出 REDACTED」的選項 $\\rightarrow$ 選項 E。

---



## 3\. 選項詳解 (Option Analysis)

- **選項 A：連線失敗；印出 "REDACTED"**

   - **錯誤**。雖然它正確預測了會印出 "REDACTED"，但連線**不會失敗**。`dbutils.secrets.get` 回傳的是真實的密碼字串物件，只是在顯示層被遮蔽，程式內部邏輯完全能正常讀取該字串。

- **選項 B：出現互動式輸入框；若密碼正確則連線成功並存入 DBFS**

   - **錯誤**。

      1. `dbutils.secrets.get` 是直接從後端 Secret Store 取值，**不會跳出輸入框**（跳出輸入框是 `dbutils.widgets` 的功能）。

      2. Databricks 不會自動把編碼後的密碼存入 DBFS，這完全是憑空捏造的行為。

- **選項 C：出現互動式輸入框；若密碼正確則連線成功並印出明文**

   - **錯誤**。同上，不會有輸入框。且 Databricks 絕不會將 Secret 以明文（Plain Text）印出，這違反了使用 Secret 的初衷。

- **選項 D：連線成功；密碼以明文印出**

   - **錯誤**。這是最危險的選項。如果 Databricks 允許 `print(secret)` 顯示明文，那任何人只要能在 Notebook 寫程式碼，就能輕鬆竊取密碼。Secret API 的核心設計就是防止這種情況。

- **選項 E：連線成功；印出 "REDACTED"**

   - **正確**。

      - **連線成功**：因為 `password` 變數在程式執行期間持有正確的憑證。

      - **印出 REDACTED**：這是 Databricks Notebook 環境對 Secret 物件的標準保護行為。

---



## 4\. 關鍵知識清單 (Key Concepts Checklist)



- dbutils.secrets.get(scope, key)：

   Databricks Utilities 中用於讀取機敏資訊的方法。它需要 Scope（作用域）和 Key（鍵值）。讀取後的值可用於 API 連線或變數賦值。

- Secret Redaction（機敏資訊遮蔽）：

   Databricks 的安全特性。當從 Secret Store 讀取的值被傳送到標準輸出（stdout/stderr）時，系統會攔截並顯示為 \[REDACTED\]，防止密碼在 Notebook logs 中外洩。

- Secret Scope：

   儲存 Secret 的邏輯容器。可以是 Databricks Backed（存在 Databricks 內部）或 Azure Key Vault Backed（整合 Azure Key Vault）。

- JDBC (Java Database Connectivity)：

   Spark 讀取外部關聯式資料庫（如 PostgreSQL, MySQL, SQL Server）的標準介面。需要 URL、Table、User 和 Password。

---





# Databricks Secrets 新手完全指南

以下用最簡單、最實用的方式說明 **Secrets 基本觀念** 與 **底層架構**，讓你考試＋工作都能立即上手。

---

# 一、新手必知的 6 個基本觀念

## **1\. Secret 可以用，但不能印出來**

```
# ✅ 可以這樣用（連線成功）
password = dbutils.secrets.get("my-scope", "db-password")
df = spark.read.jdbc(url, table, properties={"user": "admin", "password": password})

# ❌ 但印出來會被遮蔽
print(password)  # 顯示：[REDACTED]

```

**為什麼？**

- 程式內部是真實密碼（所以可以連 DB）

- 但任何輸出到螢幕、log 的內容，Databricks 會自動遮蔽

- 這叫做 **Secret Redaction**（秘密遮蔽機制）

---

## **2\. 密碼一定要放在 Secret Scope，不能寫在程式碼**

**錯誤做法：**

```
password = "MyPassword123"  # ❌ 危險！

```

**為什麼危險？**

- 程式碼會被 commit 到 Git → 密碼外洩

- Notebook 歷史紀錄會保留 → 刪不掉

- 其他人打開 Notebook 就能看到

**正確做法：**

```
password = dbutils.secrets.get("my-scope", "db-password")  # ✅ 安全

```

---

## **3\. Secret Scope 有兩種類型**

| 類型 | 密碼存放位置 | 適用情境 | 
|---|---|---|
| **Databricks-backed** | Databricks 平台（自動加密） | 開發、測試 | 
| **Key Vault-backed** | Azure Key Vault（你自己管理） | 正式環境 | 

**新手建議**：先用 Databricks-backed 練習，正式環境再換成 Key Vault。

---

## **4\. 你只能看到「有哪些 Key」，看不到「Key 的內容」**

```
# ✅ 可以列出有哪些 scope
dbutils.secrets.listScopes()
# 結果：[SecretScope(name='my-scope')]

# ✅ 可以列出 scope 裡有哪些 key
dbutils.secrets.list("my-scope")
# 結果：[SecretMetadata(key='db-password')]

# ❌ 但看不到 db-password 的實際內容
# 即使你是管理員也一樣！

```

---

## **5\. 沒有權限會直接報錯**

如果你沒有 READ 權限：

```
dbutils.secrets.get("my-scope", "db-password")
# 錯誤：PERMISSION_DENIED: User does not have READ permission

```

程式會直接中斷，連 JDBC 都跑不到。

---

## **6\. Redaction 只保護「輸出」，不保護「檔案」**

```
# ❌ 這樣會把真實密碼寫進檔案（危險！）
password = dbutils.secrets.get("my-scope", "db-password")
with open("/dbfs/temp/log.txt", "w") as f:
    f.write(password)  # 沒有被遮蔽！

```

**記住**：Redaction 只攔截螢幕輸出和 log，不會自動保護你寫入的檔案。

---

# 二、Secrets Scope 底層架構（簡單版）

## **Databricks 不是密碼管理工具，是「密碼索引器」**

Databricks 提供的是一個介面：

```
dbutils.secrets.get(scope, key)

```

真正的密碼存在哪裡？答案取決於你選的 Scope 類型。

---

## **類型 1：Databricks-backed Scope**

### **密碼存在哪裡？**

- 存在 Databricks 控制平面（Control Plane）

- Databricks 幫你自動加密

- 你看不到也碰不到這個儲存空間

### **特性**

✅ 設定簡單（3 分鐘內完成） ✅ Databricks 自動管理加密金鑰 ❌ 無法自訂金鑰輪替（Rotation） ❌ 密碼存在 Databricks，不在你的 Azure 訂閱

### **適合誰用？**

- 開發、測試環境

- 小型專案

- 快速 POC

### **你可以做什麼？**

1. 建立 scope

2. 新增 secret（但看不到內容）

3. 設定權限（READ / WRITE / MANAGE）

---

## **類型 2：Key Vault-backed Scope**

### **密碼存在哪裡？**

- 存在 **你的 Azure Key Vault**

- Databricks 只記住「Key Vault 的位置」

- 每次 `get()` 都即時向 Key Vault 查詢

### **特性**

✅ 安全等級最高（企業級） ✅ 支援自動金鑰輪替 ✅ 可在 Azure Portal 設定稽核日誌 ✅ 你完全掌控密碼（Databricks 不儲存） ❌ 設定較複雜（需要設定 Key Vault 權限）

### **適合誰用？**

- 正式環境（Production）

- 需要符合企業合規要求

- 需要自動金鑰輪替的場景

### **運作流程**

```
使用者執行 dbutils.secrets.get("my-scope", "password")
        ↓
Databricks 查表：這個 scope 對應哪個 Key Vault？
        ↓
向 Azure Key Vault 發送 API 請求
        ↓
Key Vault 回傳密碼
        ↓
Databricks 把密碼暫存在記憶體（這個 session）
        ↓
回傳給使用者

```

---

## **兩種 Scope 的關鍵差異**

| 項目 | Databricks-backed | Key Vault-backed | 
|---|---|---|
| 密碼儲存位置 | Databricks 控制平面 | 你的 Azure Key Vault | 
| 誰管理加密？ | Databricks | 你自己 | 
| 金鑰輪替 | ❌ 不支援 | ✅ 支援 | 
| Key Vault 被刪除？ | 無影響 | 立即失效 | 
| 查看 secret 內容 | ❌ 管理員也看不到 | ✅ 有 Key Vault 權限就能在 Azure Portal 看到 | 
| 設定難度 | ⭐ 簡單 | ⭐⭐⭐ 較複雜 | 

---

# 三、Secret Redaction 底層原理（簡單版）

**Databricks 怎麼做到「自動遮蔽」？**

1. 當你執行 `dbutils.secrets.get()`，Databricks 會記住這個值

2. 把這個值加入「敏感資料黑名單」

3. 任何輸出（print / log / Notebook 畫面）都會經過檢查

4. 如果輸出內容符合黑名單 → 自動替換成 `[REDACTED]`

這個機制在以下地方生效：

- Notebook 輸出

- Job logs

- Cluster logs

- Spark UI

**但不包括**：

- 你自己寫入的檔案

- 傳給外部 API 的內容

---

# 四、權限管理（ACL）

Secret Scope 有三種權限：

| 權限 | 能做什麼 | 
|---|---|
| **READ** | 使用 `dbutils.secrets.get()` | 
| **WRITE** | 新增/更新 secrets（但仍看不到內容） | 
| **MANAGE** | 管理權限（給別人 READ/WRITE） | 

**重要提醒**：

- WRITE 權限不代表可以讀取 secret

- 即使你能新增密碼，也看不到現有密碼的內容

---

# 五、實務注意事項

## **1\. Secret 大小限制**

- 單一 secret 上限：**128 KB**

- 適合存：密碼、API Token

- 不適合存：大型證書檔案、JSON 設定檔

## **2\. Key Vault-backed Scope 的設定要求**

建立時需要提供：

```
# Databricks CLI 範例
databricks secrets create-scope \
  --scope my-kv-scope \
  --scope-backend-type AZURE_KEYVAULT \
  --resource-id /subscriptions/.../resourceGroups/.../providers/Microsoft.KeyVault/vaults/my-keyvault \
  --dns-name https://my-keyvault.vault.azure.net/

```

並且確保 Databricks workspace 有 Key Vault 的 `Get` 權限。

## **3\. 常見錯誤情境**

**情境 1：Key Vault 被刪除**

- Key Vault-backed scope 會立即失效

- `dbutils.secrets.get()` 會報錯

**情境 2：忘記設定權限**

```
# 錯誤：PERMISSION_DENIED

```

解決：請管理員給你 READ 權限

**情境 3：Scope 名稱打錯**

```
dbutils.secrets.get("my-scop", "password")  # 少一個 e
# 錯誤：Scope does not exist

```

---

# 六、快速參考（Cheat Sheet）

```
# 列出所有 scope
dbutils.secrets.listScopes()

# 列出 scope 中的所有 key
dbutils.secrets.list("my-scope")

# 取得 secret（在程式中可正常使用）
password = dbutils.secrets.get("my-scope", "db-password")

# 使用 secret（正常運作）
df = spark.read.jdbc(url, table, properties={"password": password})

# 印出 secret（會被遮蔽）
print(password)  # [REDACTED]

```

---

![CleanShot 2025-12-06 at 07.32.00@2x.png](./Question%20#6%20Eric-assets/CleanShot%202025-12-06%20at%2007.32.00@2x.png)

![CleanShot 2025-12-06 at 07.33.08@2x.png](./Question%20#6%20Eric-assets/CleanShot%202025-12-06%20at%2007.33.08@2x.png)

# 七、圖解總結

```
                dbutils.secrets.get(scope, key)
                           │
           ┌───────────────┴───────────────┐
           │                               │
   Databricks-backed              Key Vault-backed
   (密碼存在 Databricks)           (密碼存在 Azure Key Vault)
   - 自動加密                      - 你控制加密金鑰
   - 設定簡單                      - 支援金鑰輪替
   - 適合開發測試                   - 適合正式環境
           │                               │
           └───────────────┬───────────────┘
                           │
                  程式取得真實密碼（可連 DB）
                           │
                  嘗試 print / log
                           │
                  Databricks 自動遮蔽
                           │
                      顯示 [REDACTED]

```

---



---





![CleanShot 2025-12-06 at 07.05.30@2x.png](./Question%20#6%20Eric-assets/CleanShot%202025-12-06%20at%2007.05.30@2x.png)



## 其他題號

![CleanShot 2025-12-06 at 07.45.49@2x.png](./Question%20#6%20Eric-assets/CleanShot%202025-12-06%20at%2007.45.49@2x.png)

---

【Q6、Q124 — Secrets 的保護與遮蔽機制（Redaction）】

Databricks 在執行時會安全處理用 `dbutils.secrets.get()` 取得的密碼。
密碼可正常用於 JDBC 等連線，連線會成功；但若在 Notebook 中 `print(password)`，輸出會自動被遮蔽成 **"REDACTED"，避免外洩。
→ 重點：**可用、可連線，但不可被印出明文。

---

【Q100、Q167 — Secret 的存取控制（Access Control）】

Secret 的權限是設定在 **Secret Scope**（不是個別 key）。
若要給某團隊最低必要權限，應在只放該團隊需要的憑證之 Scope 上授予 **Read** 權限。
Read 只允許讀取使用，不允許修改，是最常見的安全配置。
→ 重點：**Scope 分組管理 + 依團隊給 Read 權限。**

---

【Q46 — Secret Redaction 的已知限制】

遮蔽功能只保護「字面值」的明文。
若使用者透過邏輯運算（例如逐字元印出）操作 secret，就可能洩漏原始內容。
→ 重點：**Redaction 非萬能；程式中操作 secret 仍需謹慎。**

---





下面我用 **最清楚、最實務、Databricks 官方推薦的方式** 告訴你：
**要如何設定 Secret Scope 的權限，才能做到「依團隊分 Scope、給 Read 最低必要權限」**。

---

# ✅ **Databricks Secrets 權限到底怎麼設定？**

Databricks 秘密管理（Secrets）有一個關鍵原則：

> **權限是設定在 Secret Scope 上，而不是設定在 Key 上。**
> （Key 沒有獨立 ACL，ACL 是作用在整個 Scope。）

因此你要做到「不同團隊只能看到他們需要的 secrets」
→ **正確方式是：依團隊建立不同 Secret Scope，再把 Read 權限授給該團隊。**

---

# ✅ **標準做法示範（最常見的企業做法）**

假設你的 Databricks 中有三個團隊：

- Data Engineering Team

- Analytics Team

- Machine Learning Team

那你應該這樣設計：

---

## **Step 1：建立不同的 Secret Scope（依團隊 / 專案分）**

例如：

```
db_creds_data_engineering
db_creds_analytics
db_creds_ml
```

這樣每個 Scope 裡面只放這個團隊需要的 key。
避免「一個大 Scope 裝全部團隊的密碼」造成權限難以管理。

---

## **Step 2：為 Scope 設定 ACL（權限）**

你可以用 UI 或 CLI 設定。
企業多用 CLI 或 Databricks SDK（如你之前貼的 WorkspaceClient）。

---

## ⭐ **方式 A：使用 Databricks UI 設定（最簡單）**

1. 打開 Databricks → **Compute / Workspace** → **Secrets**

2. 找到你的 secret scope

3. 點選 **Permissions**

4. 對需要的群組設定：

- **READ** → 可讀取 key（典型最小授權）

- **WRITE** → 可新增 key

- **MANAGE** → 可管理這個 scope（僅限管理者）

**一般最佳實務：團隊只給 READ，不給 WRITE 和 MANAGE。**

---

## ⭐ **方式 B：使用 Databricks CLI 設定（正式環境常用）**

建立 Scope：

```bash
databricks secrets create-scope --scope db_creds_data_engineering
```

設定權限：

```bash
databricks secrets put-acl \
  --scope db_creds_data_engineering \
  --principal data_engineering_team \
  --permission READ
```

如果有一個 DevOps 角色需要管理：

```bash
databricks secrets put-acl \
  --scope db_creds_data_engineering \
  --principal devops_admin \
  --permission MANAGE
```

---

## ⭐ **方式 C：使用 Python SDK（你貼的 WorkspaceClient）**

你可以這樣做：

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

# 設定 READ 權限
w.secrets.put_secret_acl(
    scope="db_creds_data_engineering",
    principal="data_engineering_team",
    permission="READ"
)
```

這裡：

- `principal` 可以是 user、group、service principal

- `permission` 只能是 `READ`, `WRITE`, `MANAGE`

---

# 🔥 **最終安全配置原則（你主管一定會喜歡）**

| 角色 | 權限 | 說明 | 
|---|---|---|
| 一般開發人員（Data Team） | READ | 讀取密碼即可 | 
| DevOps / 平台管理員 | MANAGE | 可以建立 scope、刪除、修改 ACL | 
| 部分可信工程師（可選） | WRITE | 可新增 key，但不能看其它人的 key | 

---

# 🔑 **結論：你要做的就是三件事**

1. **為每個團隊或專案分開建立 Secret Scope**

2. **在該 Scope 上設定 ACL，給 Read 就好**

3. **不要讓不相關的團隊共用同一個 Scope**

這樣就是 Databricks 正統、考試也考的 **最佳安全實務**。

---

如果你願意，我可以幫你：

✔ 生成完整的「貴公司 Secret Scope 結構建議表」
✔ 用表格方式設計哪些 Scope 給哪些團隊
✔ 幫你寫一段可以直接貼到你專案的 README（教同事如何用 secret）

你需要哪一種？


