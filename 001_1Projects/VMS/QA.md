# QA

我們一個系統架構正在客戶 IT 審核流程中，客戶提了 3 個問題，請檢查我們回覆，確保我們有回達到客戶問題:

(你用繁體中文回覆)



顧客 Review 完我們架構後提的問題:

1. **Internet Access Security Controls enable**\
   For example, 2FA and data transmission. If T-Box Public, DMS, and FMS have different security controls, please explain them separately.

2. **Driver Behavior Analysis and Driver Performance “駕駛行為分析、司機績效”**\
   Can these be used to identify customer identity? If yes, encryption for data at rest and during processing will be required.

3. **Pre-Production Security Assessment**\
   Has the security assessment been scheduled before go-live?



我們回覆:

---

1. The security controls for each system component are as follows:\
   ***VMS、FMS***: Uses **Azure AAD** for user authentication, subject to your company's specific Azure configuration.\
   \
   ***T-Box Public***: Uses **AWS API Gateway API Keys** to authenticate external identity and access.\
   \
   **DMS**: Authentication is achieved either through a **JWT (JSON Web Token)** or by providing the **VMS** with an AWS **API Gateway API Key**, based on your company's preference. (The VMS will **poll** the DMS periodically to check for and retrieve the latest data updates.)\
   \
   **Data Transmission:**\
   All communication protocols utilize **HTTPS** to ensure data is encrypted during processing (in-transit encryption).

2. Yes, the system will use a **JWT (JSON Web Token)** to store user information. The **hash key** (or **signing secret**) will be stored securely as an **AWS environment variable** for protection at rest. Additionally, all API communication utilizing the JWT is secured via **HTTPS** to ensure data is encrypted during processing.

3. The security scan list is as follows:\
   ***OWASP Dependency Scan (CVE)***: Must pass, except for Common Vulnerabilities and Exposures (CVEs) that have no available fix.\
   \
   ***Trivy Image Scan***: Must pass, except for vulnerabilities that have no available fix.\
   \
   ***Semgrep Code Scan***: Must pass, except for vulnerabilities that have no available fix.\
   \
   ***OWASP ZAP Scan (DAST)***: Must pass, except for vulnerabilities that have no available fix.



# 客戶 IT 審核問題回覆

問題 1: Internet Access Security Controls（網路存取安全控制）

**針對 2FA 和資料傳輸安全的說明**

### 身份驗證機制

- **VMS、FMS**: 

   - 貴司使用 Azure Active Directory (AAD) 進行身份驗證

   - 可支援 Azure AD 的多因素驗證 (MFA/2FA)服務，取決於貴公司的 Azure 租戶配置

   - 如果貴司決定用其他 MFA 服務，需要另外評估

- **T-Box Public**: 使用 AWS API Gateway API Keys 進行外部系統身份驗證

- **DMS**: 支援兩種認證方式 

   - JWT (JSON Web Token) 認證

   - AWS API Gateway API Key（用於 VMS 輪詢）

### 資料傳輸安全

- 所有通訊協定皆使用 HTTPS (TLS 1.2+) 確保傳輸過程加密

- API 端點僅允許安全協定連線

---





問題 2: Driver Behavior Analysis - 個人識別資料處理

**駕駛行為分析是否可識別客戶身份及加密要求**

### 個人識別資料評估

目前可識別 ID 侷限在車子所屬公司行號， ”無”  駕駛 … 等個人資訊，

駕駛行為是以車子 ID 為主體



### 資料加密保護措施

**靜態資料（At Rest）：**

- 資料庫啟用 AWS RDS 加密（AES-256）

- JWT 簽章金鑰存儲於 AWS Secrets Manager

- 所有備份均已加密

**傳輸中資料（In Transit）：**

- 所有 API 通訊使用 HTTPS/TLS 1.2+

- JWT 令牌採用安全演算法簽章（如 HS256）

**處理過程（During Processing）：**

- 實施角色型存取控制（RBAC）限制資料存取

- 所有個人資料存取皆記錄於稽核日誌

- 僅處理必要的個人資料欄位

---





問題 3: Pre-Production Security Assessment（上線前安全評估）

**上線前安全評估排程**

### 評估時程

**是的**，我們已安排基礎上線前安全評估，每次上版 Stage 環境都要過掃:

- 安全掃描：開發期間持續進行，每次發布前執行

- 正式環境部署前：進行最終安全審查

### 安全掃描項目

系統需通過以下自動化安全掃描：

1. **OWASP Dependency Check**：CVE 漏洞掃描

2. **Trivy**：容器映像掃描

3. **Semgrep**：靜態程式碼分析（SAST）

4. **OWASP ZAP**：動態應用程式安全測試（DAST）

**通過標準**：所有掃描必須通過，除非該漏洞無可用修復方案

### 

進階:

如貴司另有特別採購之資安掃描服務，可配合進行


