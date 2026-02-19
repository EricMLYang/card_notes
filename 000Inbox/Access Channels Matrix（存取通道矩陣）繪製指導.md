# Access Channels Matrix（存取通道矩陣）繪製指導

## **快速版：用 Excel/Google Sheets 畫表格**

### **表格結構建議**

```
┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
│ Actor    │ Device   │ Channel  │ Protocol │ Auth     │ Encrypt  │ Notes    │
│ (誰)     │ (設備)   │ (通道)   │ (協定)   │ (驗證)   │ (加密)   │ (備註)   │
├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
│          │          │          │ /Port    │ Method   │ Method   │          │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

---

## **完整表格範例：VMS & FMS 系統**

### **欄位說明**

| 欄位 | 說明 | 範例 | 
|---|---|---|
| **Actor (角色)** | 誰在使用系統 | 一般使用者、管理員、外部系統 | 
| **Device (設備)** | 用什麼設備存取 | Web Browser、Mobile App、API Client | 
| **Channel (通道)** | 透過什麼路徑 | Public Internet、VPN、Private Network | 
| **Protocol/Port (協定/埠號)** | 使用的通訊協定 | HTTPS/443、SSH/22、gRPC/50051 | 
| **Authentication (驗證方式)** | 如何驗證身份 | OAuth 2.0、API Key、MFA | 
| **Encryption (加密方式)** | 資料加密方式 | TLS 1.3、AES-256、End-to-End | 
| **Access Level (權限等級)** | 可存取的範圍 | Read-Only、Full Access、Admin | 
| **Notes (備註)** | 其他重要資訊 | 需要 VPN、IP 白名單 | 

---

## **實際填寫範例**

# Access Channels Matrix - VMS & FMS System

## User Access

| Actor | Device | Channel | Access Level | 
|---|---|---|---|
| Sales Team | Web Browser | Private Network | Read-Only (Reports) | 
| Warranty / Maintenance EV PM Team | Web Browser | Private Network | Limited Access | 
| Fleet Customers (FMS) | Web Browser / Mobile App | Public Internet | Limited Access | 

## Admin Access

| Actor | Device | Channel | Access Level | 
|---|---|---|---|
| System Admin | SSH Client | Private Network | Full Admin | 
| Database Admin | PostgreSQL Client | Private Network | DB Admin | 
| DevOps Engineer | GitHub Actions | GitHub | Deployment Access | 
| Data Engineer | Databricks Workspace | Private Network | Workspace Admin | 

## External System Access

| Actor | Device | Channel | Authentication | Access Level | 
|---|---|---|---|---|
| T-Box (Vehicle Telematics) | IoT Device | Public Internet | Device Certificate | Write-Only (Telemetry) | 
| DMS (Dealer Management System) | API Client | Public Internet | API Key + OAuth 2.0 | Write Access | 
| FMS (Fleet Management System) | API Client | Public Internet | API Key + OAuth 2.0 | API Access | 
| CloudWatch Monitoring | AWS Service | AWS Private Network | IAM Role | Logs & Metrics | 
| Grafana Dashboard | Web Browser | Private Network | Username + Password | Read-Only (Monitoring) | 

## Data Pipeline Access

| Actor | Device | Channel | Authentication | Access Level | 
|---|---|---|---|---|
| Databricks Jobs | Compute Cluster | AWS PrivateLink | Service Principal | Data Processing | 
| S3 Data Lake | AWS Service | AWS Private Network | IAM Role | Storage Access | 
| Kinesis Stream | AWS Service | AWS Private Network | IAM Role | Data Streaming | 

---

**Key Security Controls:**

- ✅ All production access requires MFA

- ✅ Admin access via Bastion Host only

- ✅ API rate limiting enabled

- ✅ WAF protection for all public endpoints

- ✅ IP whitelisting for database access

- ✅ All communications use TLS 1.3