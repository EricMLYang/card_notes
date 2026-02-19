# 一鍵部署 - **CloudFormation**

- **[Best Practices and Guidance for Cloud Engineers to Deploy Databricks on AWS: Part 3](https://www.databricks.com/blog/best-practices-and-guidance-cloud-engineers-deploy-databricks-aws-part-3)**



**「以 CloudFormation 為基礎，整合 CI/CD 流程來部署一個包含 Fargate、AWS 原生服務和 Databricks 的完整方案」**，是一個非常漂亮且完整的 Infrastructure as Code (IaC) 實踐。



Databricks 確實提供了 AWS Quick Start CloudFormation 模板，可以在約 5-15 分鐘內自動部署 Databricks 工作區 [Amazon Web Services](https://aws.amazon.com/partners/success/databricks-quickstart/)[Aws-ia](https://aws-ia.github.io/cfn-ps-databricks-unified-data-analytics-platform/)。這些模板是用 YAML 編寫，並通過 AWS Lambda 支持的自定義資源（用 Python 編寫）進行擴展 [GitHub](https://github.com/aws-quickstart/quickstart-databricks-unified-data-analytics-platform/blob/main/templates/databricks-multi-workspace.template.yaml)[Databricks](https://www.databricks.com/blog/2020/10/29/announcing-databricks-on-aws-quick-starts-to-deploy-in-under-15-minutes.html)。您可以在主 CloudFormation 模板中引用這些官方模板。



### 1\. CloudFormation 作為統一的「部署藍圖」

可以把整個 CloudFormation 模板想像成一個**安裝包的說明書 (Installation Manifest)**。這份說明書會告訴 AWS 如何把你方案需要的所有零件組裝起來：

- **定義 Fargate 服務**：

   - 在 CloudFormation 裡定義 ECS Cluster、Task Definition (任務定義)、Service。

   - 在 Task Definition 中，你會指向存放在 ECR (Amazon Elastic Container Registry) 裡的 **Docker Image**。這個 Image 就是你打包好程式碼的地方。

   - 你還會定義 Fargate 需要的網路設定 (VPC, Subnets)、負載平衡器 (ALB) 和 IAM 權限。

- **定義 AWS 原生雲服務**：

   - 你的方案可能需要 S3 儲存桶、RDS 資料庫、DynamoDB 表、SQS 隊列等等。

   - 所有這些資源以及它們之間的關係（例如：讓 Fargate 可以存取 S3 的權限），全部都可以在同一個 CloudFormation 模板裡被清晰地定義出來。

- **整合 Databricks 服務**：

   - 可以利用 **Nested Stacks (巢狀堆疊)** 的技術，在你的主 CloudFormation 模板中，直接呼叫 Databricks 官方提供的 CloudFormation 模板。

   - 這樣一來，購買你方案的客戶只需要執行你提供的一個主模板，CloudFormation 就會自動先幫他把 Databricks 的底層環境建好，然後再建立你的 Fargate 應用。