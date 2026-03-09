---
tags:
  - backend
---
# Sytem Token Design

# B2B系統認證機制設計筆記

## 多層次Token認證設計

### 三種Token及其用途

1. **Access Token**

   - 短期有效（1-2小時）

   - 用於所有API操作的授權

   - 每次API請求都需要附加

   - 被盜時風險較小，因為很快過期

2. **Refresh Token**

   - 長期有效（1-7天）

   - 僅用於獲取新的Access Token

   - 儲存在安全的地方（如HTTP-only cookie）

   - 可以撤銷，用於安全控制

3. **ID Token**

   - 包含用戶資訊的JWT格式token

   - 用於前端顯示個人化內容

   - 避免額外的用戶資訊API請求

   - 支援單點登入(SSO)

### 工作流程

1. 用戶登入後獲取三種token

2. 使用Access Token進行API操作

3. Access Token過期時，用Refresh Token獲取新的Access Token

4. 僅當Refresh Token也過期時，才需要重新登入

![image 125.png](./Sytem%20Token%20Design-assets/image%20125.png)

### 安全優勢

- 縮小被盜token的攻擊窗口

- 權限最小化和職責分離

- 更精細的token撤銷控制

- 降低資料庫驗證負載

## B2B數據服務認證機制

### API Key機制

- 專為系統對系統(S2S)通信設計

- 長期有效的憑證

- 每個下游系統擁有唯一Key

- 與特定權限集綁定

- 可以在管理後台統一管理

### 服務帳號(Service Account)

- 代表一個系統而非人類用戶

- 具有明確定義的權限範圍

- 不使用密碼，而是密鑰認證

- 活動被獨立記錄和監控

- 不受密碼過期等人類用戶策略影響

### 設計考量

1. **分層認證機制**

   - 人類用戶：使用三層token機制

   - 系統整合：使用API Key和服務帳號

2. **風險等級分層**

   - 高風險操作：要求重新驗證

   - 一般操作：標準Access Token

   - 系統間調用：API Key機制

3. **安全加強機制**

   - Token和API Key撤銷機制

   - 活躍工作階段監控

   - IP白名單限制

   - 異常活動自動警報

4. **使用者體驗優化**

   - 人類用戶：Refresh Token避免頻繁登入

   - 下游系統：長期API Key簡化整合