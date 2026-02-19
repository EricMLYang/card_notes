【Databricks 認證一天一題：  Databricks Secrets】



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

- A. The connection to the external table will fail; the string "REDACTED" will be printed.

- B. An interactive input box will appear in the notebook; if the right password is provided, the connection will succeed and the encoded password will be saved to DBFS.

- C. An interactive input box will appear in the notebook; if the right password is provided, the connection will succeed and the password will be printed in plain text.

- D. The connection to the external table will succeed; the string value of password will be printed in plain text.

- E. The connection to the external table will succeed; the string "REDACTED" will be printed.



這是一道關於 Databricks Secrets 安全機制的考題。

答案：E（連線成功；印出 `[REDACTED]`）

核心解析：

1. 連線成功：`dbutils.secrets.get` 會在程式執行時取回正確的密碼，因此 JDBC 連線能順利建立。

2. 輸出遮蔽：為了安全性，Databricks 會自動攔截來自 Secrets 的變數，若嘗試將其列印（`print`）至標準輸出，系統會強制顯示為 `[REDACTED]` 以防外洩。

技巧：看到 `dbutils.secrets` 被 `print`，輸出結果一定是 `[REDACTED]`，絕不會是明文。



以下短紀錄：



▋ Secret 可以用但不能印

你用 `dbutils.secrets.get()` 取得的密碼，在程式內部是真實字串。 可以正常連資料庫。

但只要印出來，畫面上就會顯示 `[REDACTED]`。 這是 Databricks 的 Secret Redaction 機制。

記住：連線成功，但 print 永遠被遮蔽。

---

▋ 密碼不能寫在程式碼

很多人會直接寫 `password = "MyPassword123"`。 非常危險。

程式碼會被 commit 到 Git，密碼就外洩了。 Notebook 的歷史紀錄也會保留明文。

唯一安全做法：把密碼放 Secret Scope。 程式碼只寫 `dbutils.secrets.get("my-scope", "db-password")`。

---

▋ 兩種 Secret Scope

第一種叫 Databricks-backed。 密碼存在 Databricks 平台，自動加密。 適合開發測試。

第二種叫 Key Vault-backed。 密碼存在你的 Azure Key Vault。 適合正式環境。

新手先用 Databricks-backed 練習就好。

---

▋ 只能看名稱，看不到內容

你可以列出有哪些 scope、哪些 key。 但永遠看不到 key 的實際內容。

就算你是管理員也一樣。 只能新增、覆蓋，不能讀出。

唯一方法是用 `dbutils.secrets.get()` 在程式中取值。

---

▋ 沒權限會直接報錯

沒有 READ 權限時，執行 `dbutils.secrets.get()` 會拋錯。

錯誤訊息：`PERMISSION_DENIED: User does not have READ permission`。

程式會中斷，連 JDBC 都跑不到。

---

▋ Redaction 不保護檔案

Databricks 會攔截螢幕輸出和 log。

但如果你手動寫進檔案，不會被保護。 比如 `f.write(password)` 會把真實密碼寫進去。

所以不要把 secret 寫入任何檔案。

---

▋ Databricks-backed Scope 怎麼運作

密碼存在 Databricks 控制平面。 Databricks 自動加密，你碰不到儲存空間。

設定很簡單，3 分鐘就能完成。 但無法自訂金鑰輪替。

密碼不在你的 Azure 訂閱，而是在 Databricks 那邊。

---

▋ Key Vault-backed Scope 怎麼運作

密碼存在你的 Azure Key Vault。 Databricks 只記住 Key Vault 的位置。

每次 `get()` 都即時向 Key Vault 查詢。 查到之後暫存在記憶體。

如果 Key Vault 被刪除，`get()` 會立即失效。

---

▋ 兩種 Scope 的關鍵差異

Databricks-backed：密碼在 Databricks，設定簡單，不支援金鑰輪替。 管理員也看不到 secret 內容。

Key Vault-backed：密碼在你的 Key Vault，支援金鑰輪替。 有 Key Vault 權限的人可以在 Azure Portal 看到內容。

正式環境建議用 Key Vault-backed。

---

▋ Redaction 的底層原理

當你執行 `dbutils.secrets.get()`，Databricks 會記住這個值。 把它加入敏感資料黑名單。

任何輸出都會經過檢查。 符合黑名單就自動替換成 `[REDACTED]`。

這機制在 Notebook 輸出、Job logs、Cluster logs 都有效。 但不包括你自己寫入的檔案。

---

▋ 三種權限等級

READ：可以使用 `dbutils.secrets.get()`。 WRITE：可以新增或更新 secrets，但仍看不到內容。 MANAGE：可以管理權限，給別人 READ 或 WRITE。

重點：WRITE 不代表可以讀取 secret。

---

▋ Secret 大小限制

單一 secret 上限 128 KB。

適合存密碼、API Token。 不適合存大型證書檔案或 JSON 設定檔。

---

▋ Key Vault-backed 的設定要求

建立時需要提供 Key Vault 的 Resource ID 和 DNS Name。

還要確保 Databricks workspace 有 Key Vault 的 `Get` 權限。

可以用 Databricks CLI 建立： `databricks secrets create-scope --scope my-kv-scope --scope-backend-type AZURE_KEYVAULT`

---

▋ 常見錯誤情境

Key Vault 被刪除：Key Vault-backed scope 立即失效。

忘記設定權限：會出現 `PERMISSION_DENIED` 錯誤。

Scope 名稱打錯：會出現 `Scope does not exist` 錯誤。

記得仔細檢查名稱和權限。

---

▋ 快速指令參考

列出所有 scope：`dbutils.secrets.listScopes()`

列出 scope 中的 key：`dbutils.secrets.list("my-scope")`

取得 secret：`password = dbutils.secrets.get("my-scope", "db-password")`

使用 secret：`[spark.read](spark.read)``.jdbc(url, table, properties={"password": password})`

---

▋ 新手最重要的 5 件事

第一，secret 可以用但不能印。 第二，密碼不要寫在程式碼。 第三，開發用 Databricks-backed，正式環境用 Key Vault-backed。 第四，沒權限會直接報錯。 第五，Redaction 不保護你寫入的檔案。

記住這些，就不會踩到基本錯誤。

---

完成！

全文已改寫成萬能寫作法架構，每段都遵循：

- 一句話主題（隱藏在段落開頭）

- 內容展開（1-2 句就換行）

- 一句話總結（隱藏在段落結尾）

篇幅大幅縮減，適合新手快速理解。