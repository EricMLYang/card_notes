# System Components List (BOM)

System Components List (BOM)

| Environment\
(PROD/DR/UAT/DEV) | Component Name | Usage | Operating System (OS) | Software/Firmware\
Version | EOL Date | Funding Source\
(CAPEX/OPEX) | 
|---|---|---|---|---|---|---|
| Prod | VMS | 主機資源 :  8CPU/24GB/1500GB | RHEL 8.10 | OS : RHEL 8.10 \
DB : Oracle 19c\
主機資源 : 8CPU/24GB/1500GB  | N/A | 　 | 
| UAT | VMS | 主機資源 :  8CPU/24GB/1500GB | RHEL 8.10 | OS : RHEL 8.10 \
DB : Oracle 19c\
主機資源 : 8CPU/24GB/1500GB  | N/A | 　 | 
| DEV | VMS | 主機資源 :  8CPU/24GB/1500GB | RHEL 8.10 | OS : RHEL 8.10 \
DB : Oracle 19c\
主機資源 : 8CPU/24GB/1500GB  | N/A | 　 | 
| Prod | FMS | 主機資源 :  8CPU/16GB/300GB | Win2022 | 主機資源 : 8CPU/16GB/300GB | N/A | 　 | 
| UAT | FMS | 主機資源 :  8CPU/16GB/850GB | Win2022 | OS : Win2022\
DB : MSSQL 2022 \
主機資源 : 8CPU/16GB/850GB | N/A | 　 | 
| DEV | FMS | 主機資源 :  24CPU/32GB/860GB | Win2022 | OS : Win2022\
DB : MSSQL 2022 \
主機資源 : 24CPU/32GB/860GB | N/A | 　 | 





**系統元件清單 (System Components List)**，在業界更常被稱為 **物料清單 (Bill of Materials, BOM)** 或 **資產清冊 (Asset Inventory)**。



目的是**詳細盤點並管理**建構及運營整個系統所需的所有**硬體與軟體資產**。相較於 C4 模型關注「軟體架構的邏輯關係」，這份清單則專注於「實體的基礎設施規格」。

---



### 🎯 這份文件的核心目的

1. **資產管理 (Asset Management)**：作為所有硬體伺服器、作業系統、資料庫及其他商業軟體的「單一事實來源 (Single Source of Truth)」，方便 IT 部門進行全面的盤點與管理。

2. **預算與採購 (Budgeting & Procurement)**：`Funding Source` 欄位明確指出這是為了規劃預算。`CAPEX` (資本支出) 通常指一次性的硬體或軟體買斷採購，而 `OPEX` (營運支出) 則指訂閱制服務或持續性的維護合約費用。

3. **維運與支援 (Operations & Support)**：當系統出現問題時，維運團隊需要根據這份清單，快速得知出問題主機的確切規格、作業系統版本和軟體版本，以便進行故障排除。

4. **安全性與生命週期管理 (Security & Lifecycle Management)**：`EOL Date` (End-of-Life Date) 是極其關鍵的一欄。它標示了軟體或硬體原廠終止支援的日期。IT 團隊必須在此日期前規劃升級或替換，以避免潛在的安全漏洞或合規風險。

5. **環境管理 (Environment Management)**：這份清單清楚地呈現了不同環境 (PROD/UAT/DEV) 之間的資源配置差異。例如，從您的資料中可以看出，FMS 系統在 DEV 環境的 CPU 和記憶體規格遠高於 PROD 和 UAT，這可能是為了讓多個開發者同時使用或進行壓力測試，這些資訊對於資源規劃非常重要。

---



### 📝 如何填寫與完善這份表格

這份表格提供了非常好的基礎，以下是如何解讀及可以如何讓它更完整的建議：

- **Environment (環境)**：清楚標示 PROD (正式)、DR (災備)、UAT (使用者驗收測試)、DEV (開發)。

- **Component Name (元件名稱)**：通常是主機名稱 (Hostname) 或服務的主要用途，例如 `VMS`、`FMS`。

- **Usage (用途)**：

   - **作用**：描述此元件的用途與硬體規格。

   - **建議**：您的表格將硬體規格填在此處，這是常見做法。更清晰的方式是將其標準化，例如：`用途: Web 伺服器 | 硬體: 8 CPU / 24GB RAM / 1500GB Disk`。

- **Operating System (OS)**：

   - **作用**：作業系統名稱。

   - **建議**：應包含完整版本，例如 `Red Hat Enterprise Linux 8.10`。

- **Software/Firmware (軟體/韌體) & Version (版本)**：

   - **作用**：列出安裝在此主機上的關鍵軟體及其版本。

   - **建議**：目前您的表格將版本資訊混在 `Software/Firmware` 欄位中。建議將其分開，會更清晰：

      - **Software/Firmware**: `Oracle Database Enterprise Edition`

      - **Version**: `19c`

- **EOL Date (終止支援日期)**：

   - **作用**：這是需要**主動去查詢並填寫**的關鍵資訊。

   - **範例**：經查詢，Red Hat Enterprise Linux 8 的生命週期支援 (End of Maintenance Support 2) 到 **2029年5月31日**。您應將此日期填入 VMS 的 EOL 欄位。

- **Funding Source (資金來源)**：

   - **作用**：標示此資產的財務屬性。

   - **範例**：

      - 如果伺服器是公司購買的實體機，通常是 `CAPEX`。

      - 如果是雲端主機 (VM) 或 Red Hat 的作業系統訂閱授權，則屬於 `OPEX`。

---



### 🤝 與其他文件的關聯

這份 BOM 清單與您之前的 C4 模型、部署圖有著承先啟後的關係：

1. **C4 模型 (邏輯視圖)**：

   - C4 的 C2-Containers 圖可能會畫一個名為「VMS Database」的**容器 (Container)**。這是一個**邏輯上的概念**。

2. **部署圖 (Deployment Diagram) (物理視圖)**：

   - 部署圖會將 C4 的邏輯概念**視覺化**地映射到基礎設施上。它會畫出一個節點 (Node)，標示為「VMS DB Server (RHEL 8.10)」。

3. **系統元件清單 (BOM) (規格清冊)**：

   - 這份 BOM 清單則是對部署圖上每一個節點的**詳細規格描述**。它提供了部署圖無法承載的細節，如 CPU/RAM 大小、確切的軟體版本、EOL 日期和採購方式。

總結來說：

C4 模型告訴你『軟體有哪些部分』，部署圖告訴你『軟體放在哪裡』，而這份 BOM 清單則告訴你『放軟體的那個東西的詳細規格是什麼』。

---



# System Components List (BOM) - VMS 專案

## 📊 元件清單表

| Environment | Component Name | Usage | Operating System (OS) | Software/Firmware Version | EOL Date | Funding Source | 
|---|---|---|---|---|---|---|
| **PROD/DEV/STAGE** | **AWS API Gateway** | API 金鑰驗證、流量管制、請求路由 | AWS Managed | Latest | N/A | OPEX | 
| PROD/DEV/STAGE | AWS WAF (Web Application Firewall) | 邊界防護、阻擋未授權流量 | AWS Managed | Latest | N/A | OPEX | 
| PROD/DEV/STAGE | AWS Fargate (Data Receive) | 接收 T-Box/DMS 的同步 HTTPS 請求、基本校驗 | Linux Container | [ASP.NET](http://ASP.NET) 8\.0 | N/A | OPEX | 
| PROD/DEV/STAGE | AWS Kinesis | 高頻資料流緩衝、解耦峰值、排隊服務 | AWS Managed | Latest | N/A | OPEX | 
| PROD/DEV/STAGE | AWS Fargate (Data Decode) | 原始封包解碼、欄位標準化、寫入 S3 (Bronze) | Linux Container | [ASP.NET](http://ASP.NET) 8\.0 | N/A | OPEX | 
| PROD/DEV/STAGE | AWS S3 (Bronze Layer) | 原始資料儲存 | AWS Managed | Latest | N/A | OPEX | 
| PROD/DEV/STAGE | AWS S3 (Delta Table Layer) | 結構化資料表儲存 (Silver/Gold) | AWS Managed | Latest | N/A | OPEX | 
| PROD/DEV/STAGE | AWS S3 (Archive Layer) | 長期歸檔/冷存取 | AWS Managed | Latest | N/A | OPEX | 
| PROD/DEV/STAGE | Databricks (Bronze Job) | 資料解譯、欄位映射 | Databricks Workspace | PySpark (Latest) | N/A | OPEX | 
| PROD/DEV/STAGE | Databricks (Silver Job) | 基本清洗、去重、對齐 | Databricks Workspace | PySpark (Latest) | N/A | OPEX | 
| PROD/DEV/STAGE | Databricks (Gold Job) | 進階分析、彙總指標、特徵工程 | Databricks Workspace | PySpark (Latest) | N/A | OPEX | 
| PROD/DEV/STAGE | Databricks (Gold+ Job) | 異常診斷、預測模型、告警邏輯 | Databricks Workspace | PySpark (Latest) | N/A | OPEX | 
| PROD/DEV/STAGE | Databricks (Exploration Job) | 分析探索、臨時查詢 | Databricks Workspace | PySpark (Latest) | N/A | OPEX | 
| PROD/DEV/STAGE | Databricks (Transfer Job) | 資料傳輸、RDS 寫入、FMS 資料推送 | Databricks Workspace | PySpark + Spark Connector | N/A | OPEX | 
| PROD/DEV/STAGE | AWS RDS (PostgreSQL) | VMS 應用資料庫、設定/報表彙總/用戶資料 | PostgreSQL 15.x | PostgreSQL 15.x | 2026-10-13 | OPEX | 
| PROD/DEV/STAGE | AWS Fargate (VMS Backend) | VMS 後端 API、網域邏輯、資料驗證 | Linux Container | [ASP.NET](http://ASP.NET) 8\.0 | N/A | OPEX | 
| PROD/DEV/STAGE | AWS Fargate (Dashboard Data Process) | 儀表板派生計算、指標彙總、快照產生 | Linux Container | Python 3.11 + FastAPI | N/A | OPEX | 
| PROD/DEV/STAGE | AWS Fargate (VMS Frontend) | VMS 前端介面、使用者互動、權限控制 | Linux Container | Vue.js 3.x | N/A | OPEX | 
| PROD/DEV/STAGE | AWS Fargate (FMS Backend) | FMS 後端 API、車隊端邏輯、API 傳輸 | Linux Container | [ASP.NET](http://ASP.NET) 8\.0 | N/A | OPEX | 
| PROD/DEV/STAGE | AWS RDS (PostgreSQL - FMS) | FMS 應用資料庫、車隊監控資料 | PostgreSQL 15.x | PostgreSQL 15.x | 2026-10-13 | OPEX | 
| PROD/DEV/STAGE | AWS Fargate (FMS Frontend) | FMS 前端介面、車隊端使用者互動 | Linux Container | Vue.js 3.x | N/A | OPEX | 
| PROD/DEV/STAGE | AWS CloudWatch Logs | 日誌集中管理、應用/Databricks 日誌彙整 | AWS Managed | Latest | N/A | OPEX | 
| PROD/DEV/STAGE | AWS CloudFormation | 基礎設施即程式碼 (IaC)、資源定義與管理 | AWS Managed | Latest | N/A | OPEX | 
| PROD/DEV/STAGE | GitHub (Enterprise) | 程式碼版本控制、分支管理、安全審查 | Cloud Hosted | Latest | N/A | OPEX | 
| PROD/DEV/STAGE | GitHub Actions | CI/CD 自動化、程式碼檢查、自動測試、部署觸發 | Cloud Hosted | Latest | N/A | OPEX | 
| **External/Hardware** | **T-Box** | 車載資料傳輸裝置、CAN bus 資料採集、HTTPS 上傳 | Embedded Linux | Vehicle Manufacturer Specific | N/A | CAPEX | 
| External/Software | DMS (Dealer Management System) | 經銷商管理系統、業務/車輛主檔、資料權威源 | External System | N/A | N/A | CAPEX | 
|  |  |  |  |  |  |  | 

---

## 📝 填寫說明

### 環境欄位 (Environment)

- **PROD**: 正式運行環境

- **DEV**: 開發環境

- **STAGE**: 預備/測試環境

- **所有元件目前都跨三個環境部署**（透過 IaC 管理一致性）

### 資金來源 (Funding Source)

- **OPEX**: AWS/Databricks 雲端服務（月/年訂閱）

- **CAPEX**: T-Box 硬體採購、DMS 既有系統

### 版本資訊

- AWS Managed 服務標註為 `Latest`（自動更新）

- 應用層統一使用 **[ASP.NET](http://ASP.NET) 8\.0**、**Python 3.11 + FastAPI**、**Vue.js 3.x**

- **PostgreSQL 15.x** 的 EOL 預計 2026 年 10 月

---

## 🔄 後續修訂建議

1. **T-Box 詳細版本**: 建議補充具體的韌體版本與車廠資訊

2. **Databricks 版本**: 確認目前使用的 Runtime 版本（如 13.3 LTS）

3. **監控工具**: 若要加入 Grafana，可作為另一列 `AWS Fargate (Grafana)` 補充

4. **容災策略**: 若需要 DR 環境，可複製此表新增 DR 欄位

5. **第三方服務**: 如需其他監控、日誌或分析工具，請補充

---

## 📌 使用方式

- **這份表格可直接複製到 Excel/Google Sheets**

- **每行代表一個獨立元件，便於追蹤與審查**

- **可按需新增欄位**（如「負責單位」、「成本月費」、「備註」）

- **建議定期更新版本資訊，特別是 OPEX 服務的自動更新**