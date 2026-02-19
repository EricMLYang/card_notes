## **證照：AWS Certified Cloud Practitioner（CLF-C02, CCP）**

### **1) 證照目的（為什麼考）**

- 驗證你具備 **AWS 雲基礎知識**：雲端價值、共享責任模型、安全與合規、核心服務、成本與計費，以及常見使用情境。適合非技術或轉職入門者作為第一張 AWS 證照。  



### **2) 考試內容概要（考什麼）**

CLF-C02 的四大領域與比重：

- **Domain 1：Cloud Concepts（24%）**

- **Domain 2：Security & Compliance（30%）**

- **Domain 3：Cloud Technology & Services（34%）**

- **Domain 4：Billing, Pricing, & Support（12%）**

- 官方並在考綱附上「在考範圍」服務清單（如 EC2/Lambda、VPC、S3/EBS/EFS、RDS/Aurora、DynamoDB、CloudFront、Route 53、CloudWatch/CloudTrail、KMS、Organizations 等）。



### **3) 考試形式（怎麼考）**

- **題數**：65 題（**50 計分 + 15 測試題**，不標示哪些不計分）

- **題型**：單選或多選

- **時間**：**90 分鐘**

- **費用**：**USD 100**

- **通過標準**：**scaled score 700 / 1000**

- **考試方式**：Pearson VUE 考場或線上遠距監考

- **有效期限**：**3 年**（可依官方選項續證）

- 以上皆以 AWS 官方頁面與考綱為準。  





### **4) 難度與準備方向（要會到什麼程度）**

- **難度**：入門級，重概念與選型邏輯，不考實作細節。官方建議有 **0–6 個月** AWS 接觸經驗更順利。

- **高頻主題地圖**

   - **雲端價值與經濟學**：彈性、可用性、全球基礎設施、**權責/成本型態（固定 vs 可變）**、Rightsizing、Savings/Cost Explorer。

   - **共享責任模型**：客戶 vs AWS 的安全責任、依服務而變（EC2、RDS、Lambda）。

   - **安全與合規**：IAM/IAM Identity Center、最小權限、KMS、CloudTrail、Security Hub、GuardDuty、WAF/Shield、Artifact。

   - **網路與內容傳遞**：VPC、子網/路由/Security Group vs NACL、CloudFront、Route 53。

   - **運算/儲存/資料庫選型**：EC2/Auto Scaling/Lambda、S3 vs EFS vs EBS、RDS/Aurora vs DynamoDB。

   - **帳務與支援**：Cost Explorer、Budgets、Support Plans、Trusted Advisor。







#### **5) 讀書計畫（2–4 週範例）**

- **第 1 週：打底**

   - 讀完 **Exam Guide** 與 **官方 Exam overview**，列出四域重點與關鍵名詞。  

- **第 2 週：核心主題 + 小實作**

   - 做 2 個微型 Lab：

      1. **VPC + EC2 + S3** 基礎網路與存取

      2. **Lambda + API Gateway + DynamoDB**（事件驅動概念）

- **第 3 週：帳務/安全強化 + 題感訓練**

   - 熟悉 **Cost Explorer、Budgets、Support Plans**；做 1–2 回模擬題並精讀解析。

- **第 4 週：模考與查漏補缺**

   - 再做 1 回全真模考（90 分鐘/65 題），回到考綱將錯題歸類回四大領域補洞。

- 可搭配 **AWS Skill Builder 的 CCP 準備路線**。



### **6) 應試技巧（拿分關鍵）**

- **先讀需求→抓關鍵字**：如「最低成本」「零停機」「跨區容錯」「合規」決定答案方向（受管服務、多 AZ、快取/邊緣加速、加密/審計）。

- **偏好受管服務**：無特別限制時，傾向選 **受管**（RDS、Lambda、ECS on Fargate）而非自管 EC2。

- **安全不打折**：最小權限、加密（at rest/in transit）、保護 root、審計（CloudTrail）。

- **成本題心法**：S3 分層 + Lifecycle、資料傳輸路徑（Region/AZ/Internet）常是關鍵。

- **時間管理**：**\~1.4 分/題**；先掃易題，長題標記回頭；不倒扣，**全部作答**。



### **7) 報名與續證**

- 報名費 **USD 100**；可線上或到考場。

- 證照 **3 年有效**，可透過再考、考更高級別，或（目前）**Cloud Quest Recertify CCP** 遊戲式路徑續期（Beta 至 2025/7 月底）。