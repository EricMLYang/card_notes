AWS「軟體合作夥伴（Software Partner Path）」技術審核



核心就是 **FTR（Foundational Technical Review）**。

FTR 會檢視你的解決方案是否符合 AWS 最佳實務，

重點集中在 Well-Architected 的幾大面向，

外加 SaaS（若是多租戶）特有的租戶隔離等要求。

以下是「技術審核會看什麼」的精煉彙整：



# 重點面向與必查項

- **安全（Security）**

   - 身分與存取：最小權限、細粒度 IAM、角色分離、跨帳號/環境邊界控制、金鑰/密碼管控（KMS、Parameter Store/Secrets Manager）。([Amazon Web Services, Inc.](https://aws.amazon.com/partners/foundational-technical-review/?utm_source=chatgpt.com "AWS Foundational Technical Review"))

   - 資料保護：傳輸與靜態加密、金鑰輪替、備援、刪除/保留政策（含 PII 處理）。([Amazon Web Services, Inc.](https://aws.amazon.com/partners/foundational-technical-review/?utm_source=chatgpt.com "AWS Foundational Technical Review"))

   - 弱點與修補：映像與相依性掃描、修補流程、端點與邊界保護、常見攻擊面（S3、IAM、SG/NACL）防護。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

   - 稽核/監控：集中式記錄（CloudTrail、VPC Flow Logs、ALB/WAF）、警示與事件回應 Runbook。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

- **可靠度（Reliability）與災難復原**

   - 多 AZ 部署、故障隔離、備份與還原測試（RPO/RTO）、節流/重試/斷路器等韌性設計。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

- **營運卓越（Operational Excellence）**

   - **基礎設施即程式（IaC）** 與 **CI/CD**：版本化、審核與變更管控（變更紀錄、回滾計畫）。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

   - 監控可觀測性：指標、日誌、追蹤與 SLO/SLI；事故處理與事後檢討流程。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

- **效能效率（Performance Efficiency）** 與 **成本最佳化（Cost Optimization）**

   - 適當的服務與規模化策略（Auto Scaling、快取、併發與限流），容量/負載測試與效能基準。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

   - 成本可見性與治理（標籤、Budgets、Cost Explorer、Reserved/Spot 策略）。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

- **SaaS/多租戶特有（若適用）**

   - **租戶隔離模型**（資料、網路、運算層級隔離），跨租戶存取防護與測試、租戶計量/配額/節流、分層與嘗試策略。這通常對通過 FTR 的 SaaS 方案是關鍵。([AWS Documentation](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-isolation.html?utm_source=chatgpt.com "Tenant Isolation - SaaS Lens"))

# 形式與流程上會要求什麼

- **自我評估 + 自動化帳號驗證 + 提交審查**

   - 先完成 FTR 自我檢核與改善，再由 Partner Central 送審；流程包含 AWS 帳號的自動驗證報告與自評文件。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/new-foundational-technical-review-process-for-partner-hosted-solutions/?utm_source=chatgpt.com "New Foundational Technical Review Process for Partner ..."))

- **以檢核表對齊**

   - 官方提供 **Validation Checklist / Guide**（不同託管型態版本）作為審核依據；你要逐項提供證據（設計說明、架構圖、政策/Runbook、組態截圖等）。([Westcon-Comstor](https://www.westconcomstor.com/content/dam/wcgcom/Global/CorpSite/pdfs/AWS-foundational-technical-review-guide.pdf?utm_source=chatgpt.com "AWS Foundational Technical Review Guide"))

- **與 Well-Architected 對齊**

   - FTR 本質上是 Well-Architected 的「合規子集」；重點集中在安全、可靠、營運三大風險緩解，但也會觸及效能與成本。([Jit](https://www.jit.io/resources/security-standards/aws-ftr-checklist-xls?utm_source=chatgpt.com "AWS FTR (Foundational Technical Review) Checklist [XLS ..."))

- **審後修正期**

   - 若有缺口，通常會給定期限完成補強（一般敘述為可在核可後持續補齊／或需於期限內完成）。([Westcon-Comstor](https://www.westconcomstor.com/content/dam/wcgcom/Global/CorpSite/pdfs/AWS-foundational-technical-review-guide.pdf?utm_source=chatgpt.com "AWS Foundational Technical Review Guide"))

# 你可以準備的「審核包」清單（實務建議）

1. **架構與環境**

   - C4 圖（含多 AZ/跨帳號/網路拓撲）、服務清單與邏輯資料流、租戶隔離設計（SaaS）。([AWS Documentation](https://docs.aws.amazon.com/pdfs/wellarchitected/latest/saas-lens/wellarchitected-saas-lens.pdf?utm_source=chatgpt.com "SaaS Lens - AWS Well-Architected Framework"))

2. **安全基線文件**

   - IAM 最小權限矩陣、密鑰/Secrets 管理、加密策略、WAF/Shield/SG/NACL 策略、S3/KMS 設定證據。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

3. **營運與韌性**

   - IaC（如 Terraform/CloudFormation）與 CI/CD Pipeline 描述、備份/還原與 DR 演練紀錄、監控與警報儀表板截圖、事故回應流程。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

4. **效能與成本**

   - 容量/壓測報告、節流/重試與併發上限設計、成本標籤與預算/警示、資源使用優化策略。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

5. **合規與資料治理（若處理 PII/受規客戶）**

   - 數據分類/保留/刪除政策、稽核軌跡與權限審計計畫。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

# 相關官方/權威來源

- AWS 官方 FTR 頁與流程說明（加入 APN、Software Path、審查步驟）。([Amazon Web Services, Inc.](https://aws.amazon.com/partners/foundational-technical-review/?utm_source=chatgpt.com "AWS Foundational Technical Review"))

- AWS 公告：新版 FTR 流程（自動驗證、自評、提交）。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/new-foundational-technical-review-process-for-partner-hosted-solutions/?utm_source=chatgpt.com "New Foundational Technical Review Process for Partner ..."))

- 2024/11 更新說明：如何在 Partner Central 申請與後續步驟。([Amazon Web Services, Inc.](https://aws.amazon.com/blogs/apn/updates-to-the-aws-foundational-technical-review/?utm_source=chatgpt.com "Updates to the AWS Foundational Technical Review"))

- FTR Guide / 檢核表（樣本與結構）。([Westcon-Comstor](https://www.westconcomstor.com/content/dam/wcgcom/Global/CorpSite/pdfs/AWS-foundational-technical-review-guide.pdf?utm_source=chatgpt.com "AWS Foundational Technical Review Guide"))

- SaaS Lens：租戶隔離與多租戶設計的審查重點。([AWS Documentation](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-isolation.html?utm_source=chatgpt.com "Tenant Isolation - SaaS Lens"))

如果你要，我可以把上述項目變成一份「FTR 自評檢核表（繁中）」Markdown 文件，讓你的團隊逐欄填寫證據與狀態，一次到位對齊 FTR。