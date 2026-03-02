# Solution Review Checklist

Solution Review Checklist

| **Ref** | **Item Description** | **Answer** | **Remarks/Supplement/Justification Details** | 
|---|---|---|---|
| **1** | **Project Overview** | 　 | 　 | 
| **1\.1** | **Project High Level Scope / Requirements** | 　 | 　 | 
| **1\.1.1** | **Enterprise Information System / Infrastructure** |  |  | 
| 1\.1.1.1 | Nature of System \
(Be-spoke / Software Package / IaaS / PaaS / SaaS / etc) | Software Package |  | 
| 1\.1.1.2 | Hosting Type and Hosting Location of System\
(On Premise Hosting - DCH HK Data Center / Cloud Hosting - Hosting Location/Region)\
\- e.g. Cloud Hosting - Hong Kong and Singapore Region | Cloud Hosting -Singapore |  | 
| 1\.1.1.3 | For cloud-based solution, which solution vendors and hosting cloud services provider (CSP) is selected?\
\- Please provide CSP detail in Remarks.\
\- For any CSP other than AWS/Azure (incl. any 3rd parties cloud compnents in the solution) or PaaS/SaaS deployment , please attach the CAIQ Assessment for every cloud component\
<https://dchholdingsltd.sharepoint.com/:f:/r/sites/GIT/Shared%20Documents/10%20-%20Process%20and%20Guidelines/30%20-%20Cyber%20Security/Cloud%20Security%20Requirement?csf=1&web=1&e=YFMMcv> | AWS |  | 
| 1\.1.1.4 | Type of Development Project (New System / Enhancement / Revamp / etc)\
\- For major enhancement/revamp on existing applications, please verify if technology/platform upgrade from obsolete or to be obsolete platform is considered. | New System |  | 
| 1\.1.1.5 | Target Users (User type and number of users)\
\- e.g. GFN users - 50, All HK Users - 4000 , Customer - estimated 20,000 users, etc) | Motor Taiwan users (30) |  | 
| 1\.1.1.6 | Project Type: Meeting two or more of the following criteria?\
i) Major Project (i.e. the estimated expenditure is over $2 million)\
ii) Initatives from Project Blue Ocean or A3 Strategy\
iii) Public facing or users involved VVVIP\
iv) Deviations from the current EA/INFRA/Security standards | 　 |  | 
| **2** | **User Requirement Specification** | 　 | 　 | 
| **2\.1** | **High level Functional Requirements** | 　 | 　 | 
| 2\.1.1 | If it is a new/revamped system, has the business stakeholder endorsed the user requirement specification? | 　 |  | 
| **2\.2** | **Constraints, Assumptions and Dependencies** | 　 | 　 | 
| 2\.2.1 | Has all constraints, assumptions and dependencies been well documented? | 　 |  | 
| 2\.2.2 | If there is hard time limit in batch or maintenance window, has it been well documented as a constraint? | 　 |  | 
| **2\.3** | **Non Functional Requirements**  | 　 | 　 | 
| 2\.3.1 | Have sufficient budget been provisioned for all non functional requirement? For example, Performance & Capacity, Security, Data Retention, Data conversion, Portability, Interface and Training, etc. | 　 |  | 
| **2\.4** | **System Performance** | 　 | 　 | 
| 2\.4.1 | If it has performance commitment to external parties, has it been well documented? | 　 |  | 
| 2\.4.2 | Does system has dynamic workload requirement?\
 -Does the Project budgeted and plan for performance testing on normal workload?\
 -Does the Project budgeted and plan for performance testing on peak workload?\
 -If the solution is based on elastic computing resource, does the Project budgeted and plan for testing on scaling? | 　 |  | 
| **2\.5** | **Data Conversion or Data Interfacing** | 　 | 　 | 
| 2\.5.1 | Is data conversion required in the proposed solution AND the cost of the conversion provisioned in the project? | 　 |  | 
| 2\.5.2 | Is data conversion or ETL required in the proposed solution AND the necessary compute resources has been provisioned in the project? | 　 |  | 
| 2\.5.3 | Is data interfacing to 3rd party or external systems required in the proposed solution? If "Yes", what is the interfacing/integration method? | 　 |  | 
| **3** | **Bill of Material (BOM)** | 　 | 　 | 
| **3\.1** | **Cost Estimation** | 　 | 　 | 
| 3\.1.1 | Have the BOM documented the funding source of CAPEX and OPEX?\
If it is funded by other divisions/departments, does project cost controller have sufficient budget for the project? | 　 |  | 
| 3\.1.2 | Have any Software / Hardware / Firmware listed in the BOM was already End-of-Life (EOL) or to-be EOL within 12 months. \
If "Yes", please justify in remarks column why use the EOL/to-be EOL product.  | 　 |  | 
| 3\.1.3 | Have any additional recurring cost (including software maintenance, cloud service subscriptions and manpower resources in supporting the service to be delivered) been provisioned for at least three(3) years? If "No", please provide details and rationale in Remarks. | 　 |  | 
| 3\.1.4 | If the solution will replace an existing system, have sufficient budget and action been planned for demise or secure clean up of old data/resources and the retirement of old servers. | 　 |  | 
| **3\.2** | **Resource** | 　 | 　 | 
| 3\.2.1 | If there is Professional Service and Software License, are those items budgeted as separate items? | 　 |  | 
| 3\.2.2 | If there is dependency system that required interfacing, have the implementation (including interface testing) of the interfaces from both ends been budgeted?\
\
If it is budgeted in another project, please supplement in the remarks column. | 　 |  | 
| **4** | **IS/IT Project** | 　 | 　 | 
| **4\.1** | **Proposed Solution** | 　 | 　 | 
| 4\.1.1 | Have the proposed solution been benchmarked with the market?\
\
a) The products and/or solutions that has been evaluated\
b) The CAPEX and OPEX of the products and/or solutions\
c) Highlight any product or solution that is not GIT standard\
d) Reason for leveraging existing hardware and/or software | 　 |  | 
| 4\.1.2 | If it is a packaged or SaaS solution, is there no customisation required.?\
Otherwise, please provide justification in the remarks column. | 　 |  | 
| **5** | **Implementation Approach, Technology Platform and Architecture** | 　 | 　 | 
| **5\.1** | **High Level Architecture** | 　 | 　 | 
| 5\.1.1 | Have the proposed architecture with diagram with the specified hardware/software/subscrption components provided in BOM?\
If cloud service is used or integrate/interfacing with other systems (cloud or on permise systems), please indicate data flow in the diagram. | 　 |  | 
| **5\.2** | **Implementation Approach and Technology Architecture** | 　 | 　 | 
| 5\.2.1 | Is Mainstream standard technology platforms adopted? Please state the detail versions in Remarks if not covered in architecture diagram in 5.1.\
\- Operating System (OS) (latest Windows Server OS, Desktop OS, UNIX/Linux OS, Mobile OS : Android / iOS)\
\- Web/Application Server ( Kubernetes Service, latest IIS with .NET)\
\- Database Server (AWS RDS, DynamoDB, Cosmos DB, latest Microsoft SQL Server)\
\- Reporting Service (Power BI, latest Microsoft SQL Server Reporting Service)\
\- Knowledge Management (latest Microsoft SharePoint)\
\- Job Scheduling (AWS Step Functions, Lambda, Azure Logic App, etc)\
\
\- If Answer = "No", \
  - provide justification for not adopting mainstream technology in Remarks\
  - verify if adequate maintenance cost/service from the vendor to mitigate the support risk provisioned? | 　 |  | 
| 5\.2.2 | If a new technology is targeted to be adopted (especially for enterprise use), has the evaluation results and implementation approach been endorsed? | 　 |  | 
| 5\.2.3 | For web-based application, is the latest Microsoft Edge and Google Chorme targeted to be compatible? | 　 |  | 
| 5\.2.4 | Is the proposed solution considered as a standardized, enterprise-wide solution? \
\- Please provide evidence on scalable/extensible architecture if the proposed solution is intended to be enterprise-wide. | 　 |  | 
| 5\.2.5 | Is third party tools and its related terms of use and license cost (if any) considered and provisioned? | 　 |  | 
| 5\.2.6 | For public facing solution, is all components hosted on the same platform?\
 - Please provide justification and rationale if the answer is "No" | 　 |  | 
| 5\.2.7 | For Advance Data Analytic solution, is it hosted on the corprate Cloud Platform?\
 - Please provide justification and rationale if the answer is "No" | 　 |  | 
| **5\.3** | **Virtualization Services** | 　 | 　 | 
| 5\.3.1 | Virtualized machines are used for all servers? \
\- Please provide justification and rationale if the answer is "No" | 　 |  | 
| 5\.3.2 | Are dedicated servers are used in the proposed solution?\
If "Yes", please state the reason/criteria met for using dedicated servers in the Remarks.\
Following are some of the criteria on using dedicated servers.\
     --- public facing systems; or\
     --- systems with at least one of the following characteristics:\
          --- 24x7 online service window\
          --- High processing power requirement\
          --- Bursty loading\
          --- Processing or store sensitive data\
          --- Application/package requires privilege access\
          --- High dependency on other system software(s)\
If "No", please state the reason to share server for multiple role/system | 　 |  | 
| **5\.4** | **Authentication/Directory Services** | 　 |  | 
| 5\.4.1 | For on permise solution, is the corporate Microsoft Active Directory (AD) and/or Single Sign-On (SSO) used adopted for account authentication and authorization?\
\- If Answer = "No", please state the reason and rationale in Remarks.\
\- If Answer = "No", please also state the authentication model (e.g. local user database/other LDAP service) will be used\
\- If Answer = "No", please state who will be responsible for the user account management | 　 |  | 
| 5\.4.2 | For cloud-based solution, is the corporate Microsoft Azure Active Directory (AAD) or Microsoft  Active Directory Federation Services (ADFS) being adopted for account authentication and federation identity management?\
\- If Answer = "No", please state the reason and rationale in Remarks.\
\- If Answer = "No", please also state the authentication model (e.g. local user database/other LDAP service) will be used\
\- If Answer = "No", please state who will be responsible for the user account management | 　 |  | 
| 5\.4.3 | For customer and public facing solution, please specify for customer account management? | 　 |  | 
| **5\.5** | **Communication Services (NA if not applicable)** | 　 | 　 | 
| 5\.5.1 | Is the corporate Microsoft O365 platform adopted as the mainstream email platform? \
\- If Answer = "No", please provide nme of the email service provider details and rationale in Remarks. | 　 |  | 
| 5\.5.2 | Is Microsoft Teams adopted as mainstream platform for instant messaging and video conferencing communication?\
\- If Answer = "No", please provide details and rationale in Remarks. | 　 |  | 
| **5\.6** | **Mobile Application (NA it if not applicable)** | 　 | 　 | 
| 5\.6.1 | Is standardized development approach adopted?\
\
\- For Internal Application\
\- is Low Code Development Platform considered first to build Responsive Web App (RWA) , Progressive Web App (PWA) or Mobile Application.\
\
\- For Enterprise Application\
\- is Responsive Web App (RWA) considered first to enable mobility with simpler deployment & maintainability?\
\- For Public Facing application please discuss with Enterprise Architect team for adopting.\
\
\- If Answer = "No", please state the justification and rationale in Remarks. | 　 |  | 
| **5\.7** | **DevOps** | 　 | 　 | 
| 5\.7.1 | Is DevOps been adopted for build and release.  \
 - if "Yes", please ensure sufficient user accounts or licenses are included\
 - if additional build pipeline is required, please state the justification and rationale in Remarks.\
 - if "No", please state the justification and rationale in Remarks. | 　 |  | 
| 5\.7.2 | Is Application Performance Monitoring has been included in the project scope?   | 　 |  | 
| 5\.7.3 | Is auto test has been included in the project scope?  | 　 |  | 
| **6** | **Data Sensitivity and Security** | 　 | 　 | 
| **6\.1** | **Personal Data (NA if not applicable)** | 　 | 　 | 
| 6\.1.1 | If personal data is collected\
\- verify if PICS (Personal Information Collection Statement) requirement in seeking end-user acknowledgement and acceptance on use of personal data is included in the requirement specification.  | 　 |  | 
| 6\.1.2 | If the personal data will be hosted on cloud storage/services outside your BU region, is the following requirements included in the project scope?\
1) Control of unnecessary cross-border data flow activities \
2) User written consent is required if location of cloud services location not in White List\
3) Keep inventory of personal data and require regular audits | 　 |  | 
| **6\.2** | **Data Retention and Housekeeping** | 　 | 　 | 
| 6\.2.1 | What kind of data would be collected, processed and/or stored in your system? | 　 |  | 
| 6\.2.2 | Is data housekeeping requirement included in the requirement specification? | 　 |  | 
| **6\.3** | **Encryption/Masking of Personal/Sensitive/Classified Information** | 　 | 　 | 
| 6\.3.1 | In addition to personal data, if classified information (like financial data, credential…) will be stored, data encryption and tokenization shall be enforced. Are the encryption requirements stated below included in the project scope? \
If "Yes", please specify which encryption technologies were selected.\
If "No", please provide details and rationale in Remarks.\
\
(A1) Data-At-Rest Encryption (Server Side)\
(1) Database Encryption \[TDE (Transparent Data Encryption)\] to encrypt data in database level; and/or\
(2) Database Column Encryption to encrypt data in table column level; and/or\
(3) Hashing  (if decryption is not required like password); and/or\
(4) Tokenization;\
\
(A2) Data-At-Rest Encryption (Applicable to Mobile Front-end Side)\
(1) Although not recommended to store personal data in local storage of mobile apps, if unavoidable, the data shall be encrypted using industrial standard.\
\
(B) Data-In-Transit Encryption\
(1) HTTPS encryption for transmission to encrypt data in transit (TLS should be used)\
\- Shall meet GIT Secure Communications Standard | 　 |  | 
| 6\.3.2 | Is data masking requirements in non-production environments included in the project scope? | 　 |  | 
| **6\.4** | **Mobile Device Security** | 　 | 　 | 
| 6\.4.1 | If Offline Login is required in the proposed internal mobile app, is the following security requirements included in requirement specification? If "No", please provide details and rationale in Remarks.\
\- The password stored in the local storage of the mobile device shall be encrypted with encryption key stored in keychain\
\- Expiration must be enforced for the password stored in the mobile device (for example, 10 days)\
\- The account shall be disabled when the number of consecutive failure Offline Logins is reached (for example, 5 times)\
\- Proper logic shall be built in the mobile app to handle the periodic change of password   | 　 |  | 
| 6\.4.2 | Is the following security requirements for login session included in requirement specification? If "No", please provide details and rationale in Remarks.\
\- For each login session, no matter online or offline, Session Expiry shall  be designed and enforced appropriately to protect information to against any unreasonably prolonged session. | 　 |  | 
| 6\.4.3 | EMM (Enterprise Mobility Management) solution shall be used for protection on personal/COPE (Corporate Owned Personally Enabled) / Corporate Owned mobile devices in a way to access Classified Information via the mobile devices.\
\- Has sufficient EMM license cost and on-going yearly subscription cost has been provisioned for the project?\
\- If EMM will be installed in the corporate owned devices, DEP shall be enabled for all iOS devices. Is the requirement included in the requirement specification? If "No", please provide details and rationale in Remarks.\
  | 　 |  | 
| 6\.4.4 | For internal (enterprise) mobile apps, authentication using Corporate AD or AAD shall be used. Authorization for right people to access the right information shall be properly implemented for all mobile apps wherever applicable. Is this security requirement included in the requirement specification? If "No", please provide details and rationale in Remarks. | 　 |  | 
| **6\.5** | **Security Testing** | 　 | 　 | 
| 6\.5.1 | For new bespoke system or mobile app development/replacement, is the following mandatory Security Testing requirements included in requirement specification? If "No", please provide details and rationale in Remarks.\
1) SAST (Static Application Security Testing) (for source code)\
\- is used for analyzing source code and/or compiled versions of code to help find security flaws\
\- It is applied when source code development is involved\
2) SCA (Software Composition Analysis) tool that attempts to detect publicly disclosed vulnerabilities contained within a project's dependencies\
\- It is applicable when third party library is utilized in the project development \
3) DAST (Dynamic Application Security Testing) (Black-box Testing) (for backend)\
\- is used for simulating different test cases to hack if there is security vulnerabilities \
\- It is applied when web interface is involved or it is a web application | 　 |  | 
| 6\.5.2 | For enhancement of enterprise IS/mobile apps, please confirm if security testing is required to be included in the project scope?\
\- Project team shall provision the security testing resource and effort requirements in the project scope based on the security testing requirements as stated in table below.\
1) SAST (Static Application Security Testing) (for source code)\
\- is used for analyzing source code and/or compiled versions of code to help find security flaws\
\- It is applied when source code development is involved\
2) SCA (Software Composition Analysis)  tool that attempts to detect publicly disclosed vulnerabilities contained within a project's dependencies\
\- It is applicable when third party library is utilized in the project development \
3) DAST (Dynamic Application Security Testing) (Black-box Testing) (for backend)\
\- is used for simulating different test cases to hack if there is security vulnerabilities \
\- It is applied when web interface is involved or it is a web application | 　 |  | 
| 6\.5.3 | For software package,   \
Is the security test requirement on either the followings included in the project scope? Please provide more details in Remarks\
1) certification/evidence from the vendor that the package has gone through SAST & SCA & DAST process with positive result in detailed report | 　 |  | 
| 6\.5.4 | Do Vendor/Project Team included the cost for conducting Penetration Test with DCH qualified third party vendor with positive result on new system or mobile apps (6.5.1), enhancement of existing system (6.5.2) , software package (6.5.3 ) if the systems are public facing. | 　 |  | 
| **7** | **Infrastructure Design (HA/DR) / Network Considerations** | 　 | 　 | 
| **7\.1** | **High Availability (HA) / Disaster Recovery (DR) Provisioning (applicable for mission-critical / public facing applications)** | 　 | 　 | 
| 7\.1.1 | If the proposed solution is Public Facing and/or mission-critical IS/IT services, High Availability (HA) & Disaster Recovery (DR) Architecture shall be adopted. Is the following HA and DR requirements included in the project scope? If "No", please provide details and rationale in Remarks.\
1) HA & DR Requirements\
\- The Active-Active or Active-Passive configuration, each HA server is capable to support 100% of workload; and\
\- The single DR server is capable to support 100% of workload \
\
2) For Microsoft SQL Server HA Architecture, it is using\
\- AlwaysOn Availability Group (AG)\
\- Sync Commit for Auto Failover\
\- Primary Replica (Server) is read/write\
\- Secondary Replica (Server) is read only (can be used as report server to avoid data contention)\
\
3) For Load Balancing HA Architecture, where\
\- Dedicated/Hardware Load Balancer or other non-Windows NLB software shall be used\
\- Software Load Balancer in Cloud Platform shall configured with sufficient scale-out capacity\
\
4) For cloud storage, including AWS S3, Azure SQL server and Azure Storage\
\- Depends on Recover Time Objective (RTO), please consider enable Geo-Redundant Storage (GRS) or Backup. | 　 |  | 
| 7\.1.2 | For Failover Handling on the HA Architecture in application aspect, is the following requirement included in the project scope? If "No", please provide details and rationale in Remarks.\
(1) Failover mechanism (either one)\
(a) smooth failover with session values being retained from 1 server to another where user operation will not be impacted, \
     -- for .Net web application, please ensure the followings are properly configured,\
             (1) Machine Keys of the load balanced application servers were created and of same values\
             (2) Server session management (session state) is using either SQL Server Database or State Server\
              <https://dotnetcodr.com/2013/07/01/web-farms-in-net-and-iis-part-5-session-state-management/>\
      -- for other applications, please ensure the language specific clustering/failover requirements were properly configured.\
 (b) seamless failover (as described above) is not required, \
      -- the system will reload the web page and \
      -- users have to re-enter the values to the page again\
 (2) Failover test\
Failover test for using method (a) or (b) | 　 |  | 
| **7\.2** | **IT Infrastructure Design for Internet Access for Internal Systems** | 　 | 　 | 
| 7\.2.1 | If the proposed solution is an internal IS/IT solution and requires internet access, is the following internet access requirements included in the project scope? If "No", please provide details and rationale in Remarks. \
1) Reverse Proxy / Direct NAT is used to enable user access from the Internet to the proposed internal IS/IT solution\
2) Direct NAT is used for DMZ application\
\
Please note,  any non-reverse proxy internet access architecture for internal server shall only be used upon Exemption sought with justifications | 　 |  | 
| **7\.3** | **Network Requirements** | 　 | 　 | 
| 7\.3.1 | Does the proposed solution use the standards of networking technology? If "No", please provide details of exemption. | 　 |  | 
| 7\.3.2 | Is the network bandwidth requirement of the proposed solution expected to be covered by the current network bandwidth capacity in infrastructure? \
If "Yes, have it reviewed by Infrastructure Architect and Network Architect? Please specify the reviewer name.\
If "No", have it reviewed by Infrastructure Architect and Network Architect to include the cost of topping up the bandwidth?  Please specify the reviewer name and provide details. | 　 |  | 
| **8** | **Performance and Capacity Planning** | 　 | 　 | 
| **8\.1** | **Performance Requirement** | 　 | 　 | 
| 8\.1.1 | Is performance requirements (incl. performance test) included in project scope? If "No", please provide details and rationale in Remarks.\
\- please note existing performance shall be used as benchmark to define expected to-be performance requirement for improvement in the proposed solution where applicable for revamp / technology upgrade / major enhancement projects | 　 |  | 
| 8\.1.2 | Is pre-production site required for performance / stress test and included in the project scope? | 　 |  | 
| **8\.2** | **Capacity Planning and Data Retention** | 　 | 　 | 
| 8\.2.1 | Has capacity planning been made? If "No", please provide details and rationale in Remarks. | 　 |  | 
| 8\.2.2 | Please confirm lower pricing tier of cloud storage service has been considered for long term retention | 　 |  | 





## 檢查表的核心目的

是確保專案在**商業需求、技術架構、成本效益、安全性、可維護性**及**未來擴展性**等各個面向都經過周詳的考慮。

---

## 總覽：檢查表八大分類

我將這份檢查表歸納為以下 **8 大核心類別**，每個類別都對應一個關鍵的專案面向：

1. **專案概覽 (Project Overview)**：定義專案的「身分」。

2. **使用者需求 (User Requirement)**：定義專案要「做什麼」。

3. **物料清單 (Bill of Material - BOM)**：定義專案要「花多少錢」。

4. **解決方案 (IS/IT Project)**：定義「為何選用」此方案。

5. **技術與架構 (Technology & Architecture)**：定義專案要「如何建構」。

6. **資料與安全 (Data & Security)**：定義專 to案如何「保護資產」。

7. **基礎設施 (Infrastructure)**：定義專案的「運行環境」。

8. **效能與容量 (Performance & Capacity)**：定義專案能「承受多大壓力」。

以下針對每個類別進行詳細說明。

---

## 1\. 專案概覽 (Project Overview)

- **\## 範疇**
   此部分是專案的「**基本資料卡**」📄。用來快速理解專案的性質、範疇、目標使用者和部署環境，是整個審查的基礎。

- **\## 填寫者**
   **專案經理 (Project Manager, PM)** 主導，並與 **技術負責人 (Tech Lead)** 協作完成。

- **\## 填寫指南**

   - **1\.1.1.1 (Nature of System):** 根據您的方案類型填寫，例如 `Software Package` (套裝軟體)、`Bespoke` (客製化開發) 或 `SaaS` (軟體即服務)。

   - **1\.1.1.2 (Hosting):** 明確指出託管方式 (地端 `On-Premise` 或雲端 `Cloud`) 與具體地點/區域。

   - **1\.1.1.3 (Cloud Provider):** 若是雲端方案，需寫明是哪家雲端服務商 (如 AWS, Azure, GCP)。若非主流廠商，需按要求提供 CAIQ 安全評估問卷。

   - **1\.1.1.6 (Project Type):** 這是**重要分類題**。根據專案預算、戰略重要性、是否面向公眾等標準，判斷專案的監管級別。若符合兩項或以上，通常代表此專案需要更嚴格的治理與審查。

- **\## 注意事項**

   - 這是建立共識的第一步，內容務必**清晰、準確**。

   - 第 `1.1.1.6` 題的答案會直接影響後續的審查嚴謹度與資源投入。

---

## 2\. 使用者需求規格 (User Requirement Specification)

- **\## 範疇**
   此部分聚焦在專案的「**商業價值**」與「**功能邊界**」🗺️。確保技術方案是為了解決真實的業務問題而設計，並已考慮所有限制與非功能性需求。

- **\## 填寫者**
   **業務分析師 (Business Analyst, BA)** 或 **PM** 主導，內容需獲得**業務單位/客戶 (Business Stakeholders)** 的認可。

- **\## 填寫指南**

   - **2\.1.1 (Endorsed URS):** 務必回答「是」，並在備註中說明需求規格文件已由哪位業務方簽核確認。這是專案範疇的**最重要依據**。

   - **2\.3.1 (Non Functional Requirements):** 確認除了功能開發外，是否已編列**效能測試、安全、資料轉移、使用者培訓**等預算。

   - **2\.4 (System Performance):** 如果有對外的服務等級協議 (SLA)，必須明確記錄。若系統有尖峰/離峰流量差異，需規劃對應的壓力測試。

   - **2\.5 (Data Interfacing):** 如果需要與第三方系統對接，需明確說明整合方式 (如 API, SFTP, ETL)。

- **\## 注意事項**

   - **需求必須被量化**。例如，效能需求不能只寫「系統反應要快」，應寫「95% 的頁面載入時間需在 3 秒內」。

   - 所有假設 (Assumptions) 和依賴 (Dependencies) 都應清楚記錄，以避免日後爭議。

---

## 3\. 物料清單 (Bill of Material - BOM)

- **\## 範疇**
   此部分是專案的「**財務規劃書**」💰。詳細列出所有硬體、軟體、雲端服務、人力資源的成本，包含一次性的資本支出 (CAPEX) 和持續性的營運支出 (OPEX)。

- **\## 填寫者**
   **PM** 主導，並與**技術架構師 (Architect)**、**採購部門 (Procurement)** 協作。

- **\## 填寫指南**

   - **3\.1.1 (Funding Source):** 清楚標明資金來源。

   - **3\.1.2 (EOL):** 檢查所有採購項目，確保沒有任何即將或已經終止服務 (End-of-Life) 的產品。使用 EOL 產品是**重大風險**，需要極強的理由。

   - **3\.1.3 (Recurring Cost):** 這是常見的疏漏點。務必估算**至少三年**的維護、訂閱和支援費用。

   - **3\.1.4 (Retirement Cost):** 若是系統汰換，舊系統的資料清除、伺服器退役等也需要成本，必須納入預算。

- **\## 注意事項**

   - 成本估算要**考慮到未來**，尤其是雲端服務的費用可能會隨用量增長。

   - 務必將授權、維護、人力等「隱性成本」完全揭露。

---

## 4\. IS/IT 專案 (IS/IT Project)

- **\## 範疇**
   此部分在於「**方案的合理性**」⚖️。說明為何選擇目前的技術方案，是否做過市場評估，以及方案是否符合公司標準。

- **\## 填寫者**
   **技術架構師**或**解決方案架構師 (Solution Architect)**。

- **\## 填寫指南**

   - **4\.1.1 (Benchmarked):** 需提供評估過程，列出其他被考慮過的方案，並從成本、功能、技術符合度等角度，說明最終選擇的原因。

   - **4\.1.2 (Customisation):** 盡量採用標準功能 (Out-of-the-box)。如果需要客製化，必須說明其**必要性與價值**，因為客製化會增加成本與未來升級的複雜性。

- **\## 注意事項**

   - 這部分是向審查者證明團隊已做足功課，所選方案是經過**深思熟慮**的最佳解。

---

## 5\. 實施方法、技術平台與架構 (Implementation, Technology & Architecture)

- **\## 範疇**
   這是整個檢查表的「**技術核心**」🛠️。詳細描述系統的架構藍圖、採用的技術堆疊、身份驗證機制、開發維運模式 (DevOps) 等。

- **\## 填寫者**
   **技術架構師**與**主要開發人員 (Lead Developer)**。

- **\## 填寫指南**

   - **5\.1.1 (Architecture Diagram):** **必須提供**！一張清晰的架構圖勝過千言萬語。圖中需包含主要元件、伺服器、資料庫、以及與其他系統的資料流向。

   - **5\.2.1 (Mainstream Technology):** 盡可能採用公司內部的主流或標準技術，以降低維護與支援的風險。若採用新技術，需有充分理由並評估支援風險。

   - **5\.4 (Authentication):** 身份驗證是資安重點。應優先整合公司的目錄服務 (如 AD/AAD)，避免各自為政建立帳號系統。

   - **5\.6 (Mobile Application):** 若開發手機 App，需說明為何選擇特定的開發方式 (例如，為何不用 RWA 而要用原生 App)。

   - **5\.7 (DevOps):** 說明是否採用自動化建置與部署 (CI/CD)，以及是否規劃應用程式效能監控 (APM) 和自動化測試。

- **\## 注意事項**

   - **架構圖是溝通的關鍵**，務必確保其準確反映 BOM 和技術選型。

   - 任何偏離公司標準技術的選擇，都需要提出**強而有力的 justification**。

---

## 6\. 資料敏感性與安全性 (Data Sensitivity and Security)

- **\## 範疇**
   專案的「**安全防護網**」🛡️。確保系統設計從一開始就將資料保護、隱私法規、加密措施與安全測試納入考量。

- **\## 填寫者**
   **技術架構師**與**資安專家 (Security Specialist)**。

- **\## 填寫指南**

   - **6\.1 (Personal Data):** 若處理個資，必須遵循當地的隱私法規 (如 PDPA, GDPR)。需有使用者同意條款 (PICS)，並注意跨境資料傳輸的合規性。

   - **6\.3 (Encryption):** 這是**必做題**。所有敏感資料在靜止 (Data-at-Rest，如存於資料庫) 和傳輸 (Data-in-Transit，如透過網路) 時都**必須加密**。需說明採用的加密技術 (如 TDE, TLS)。

   - **6\.5 (Security Testing):** 根據專案類型 (全新開發/功能增強/套裝軟體)，規劃對應的安全測試：

      - **SAST (源碼掃描):** 檢查程式碼是否有漏洞。

      - **SCA (相依性掃描):** 檢查使用的第三方套件是否有漏洞。

      - **DAST (動態測試):** 模擬駭客攻擊。

      - **Penetration Test (滲透測試):** 若為**對外服務 (Public Facing)**，此項通常是**強制要求**。

- **\## 注意事項**

   - **安全性是設計的一部分，而不是事後補救**。所有安全相關需求都應在專案初期就納入範疇與預算。

   - 對於安全相關問題，「否」通常不是一個可接受的答案，除非有正式的風險接受程序 (Risk Acceptance)。

---

## 7\. 基礎設施設計 / 網路考量 (Infrastructure Design / Network)

- **\## 範疇**
   專案的「**骨架與血脈**」🏗️。確保系統的部署環境具備高可用性 (HA)、災難備援 (DR) 能力，並且網路頻寬足以支撐。

- **\## 填寫者**
   **基礎設施架構師 (Infrastructure Architect)** 與 **網路架構師 (Network Architect)**。

- **\## 填寫指南**

   - **7\.1 (HA/DR):** 對於關鍵或對外服務的系統，必須設計 HA/DR 架構。需說明是 Active-Active 還是 Active-Passive，並規劃故障轉移 (Failover) 測試。

   - **7\.3.2 (Network Bandwidth):** 估算系統上線後所需的網路流量，並與網路團隊確認現有頻寬是否足夠，不足時需將升級成本納入預算。

- **\## 注意事項**

   - HA/DR 的設計等級應與**業務關鍵性 (Business Criticality)** 成正比。不是所有系統都需要最頂級的災備方案。

---

## 8\. 效能與容量規劃 (Performance and Capacity Planning)

- **\## 範疇**
   確保系統「**跑得動、扛得住**」💪。規劃系統的效能指標、壓力測試，並預估未來的容量需求。

- **\## 填寫者**
   **技術架構師**與**效能工程師 (Performance Engineer)**。

- **\## 填寫指南**

   - **8\.1.1 (Performance Requirement):** 需定義**具體的效能指標** (如每秒交易數 TPS、回應時間)，並規劃效能測試。

   - **8\.1.2 (Pre-production Site):** 效能/壓力測試**不應在正式環境 (Production) 進行**。需規劃一個與正式環境規格相近的預備環境 (Pre-production/Staging)。

   - **8\.2.1 (Capacity Planning):** 需根據預期的使用者增長、資料量增長，規劃未來 3-5 年的擴充能力。

- **\## 注意事項**

   - 效能測試應盡早規劃並納入專案時程與預算。等到上線前才發現效能問題，通常為時已晚。

   - 對於雲端方案，容量規劃應結合彈性擴展 (Auto-scaling) 的策略。





---



# VMS Project Checklist - 快速回覆

我來幫您逐項回答這份檢查清單。根據您提供的專案資訊，我會盡量簡潔地回覆：

## 2\. User Requirement Specification

**2\.1.1** Yes - 建議補充：需確認業務利益相關者已審核並簽署需求規格書

**2\.2.1** Yes - 建議補充：已於架構文件中記載主要假設與依賴關係

**2\.2.2** Yes - 建議補充：Databricks Job 批次作業時間窗口已定義

**2\.3.1** Yes - 建議補充：已包含安全測試、效能測試、監控工具等預算

**2\.4.1** NA - 建議補充：內部系統，無對外效能承諾

**2\.4.2** Yes - 建議補充：AWS Fargate 與 Databricks 均支援彈性擴展，已規劃效能測試

**2\.5.1** Yes - 建議補充：包含 T-Box、DMS 資料轉換成本

**2\.5.2** Yes - 建議補充：Kinesis、S3、Databricks 運算資源已納入

**2\.5.3** Yes - 建議補充：整合方式為 HTTPS API (T-Box)、API (DMS)

## 3\. Bill of Material (BOM)

**3\.1.1** Yes - 建議補充：需確認 CAPEX/OPEX 資金來源與預算控制者

**3\.1.2** Yes - 建議補充：所有元件均採用主流且非 EOL 版本（AWS、Databricks）

**3\.1.3** Yes - 建議補充：AWS 訂閱、Databricks 授權、維運人力已規劃 3 年

**3\.1.4** NA - 建議補充：為新系統，無舊系統需退役

**3\.2.1** Yes - 建議補充：專業服務與授權已分項列示

**3\.2.2** Yes - 建議補充：DMS、FMS 介面開發與測試成本已納入

## 4\. IS/IT Project

**4\.1.1** Yes - 建議補充：已評估 AWS vs Azure，選用 AWS + Databricks 方案

**4\.1.2** Yes - 建議補充：採用 AWS 標準服務與 Databricks 平台，無客製化

## 5\. Implementation Approach, Technology Platform and Architecture

**5\.1.1** Yes - 建議補充：已提供 C1、C2、部署架構圖及資料流向

**5\.2.1** Yes - 建議補充：[ASP.NET](http://ASP.NET) Core、Vue.js、Python FastAPI、PostgreSQL、Databricks Spark

**5\.2.2** Yes - 建議補充：Databricks + Delta Lake 為數據分析標準架構

**5\.2.3** Yes - 建議補充：前端支援最新 Edge 與 Chrome

**5\.2.4** Yes - 建議補充：可擴展至區域標竿，架構支援水平擴展

**5\.2.5** NA - 建議補充：均使用開源或 AWS/Databricks 內建工具

**5\.2.6** Yes - 建議補充：所有元件均在 AWS 雲端平台

**5\.2.7** Yes - 建議補充：Databricks 託管於 AWS Singapore

**5\.3.1** Yes - 建議補充：AWS Fargate 為 Serverless 容器服務

**5\.3.2** Yes - 建議補充：採用 Fargate，24x7 服務、處理敏感車輛數據

**5\.4.1** NA - 建議補充：雲端解決方案

**5\.4.2** Yes - 建議補充：採用 Azure AD 或 AWS Cognito 整合企業目錄

**5\.4.3** NA - 建議補充：初期為內部使用，未來 FMS 客戶端另行規劃

**5\.5.1** NA

**5\.5.2** NA

**5\.6.1** Yes - 建議補充：採用 RWA 架構（Vue.js）

**5\.7.1** Yes - 建議補充：GitHub Actions CI/CD，已含授權與 Pipeline

**5\.7.2** Yes - 建議補充：AWS CloudWatch + Grafana

**5\.7.3** Yes - 建議補充：已納入自動化測試階段

## 6\. Data Sensitivity and Security

**6\.1.1** NA - 建議補充：初期內部使用，未來 FMS 需補充 PICS

**6\.1.2** NA - 建議補充：資料託管於新加坡，符合地區要求

**6\.2.1** 建議補充：車輛感測數據、CAN Bus 資料、DMS 業務資料、告警記錄、駕駛行為數據

**6\.2.2** Yes - 建議補充：S3 設定歸檔政策，定期清理舊數據

**6\.3.1** Yes - 建議補充：RDS TDE、S3 加密、HTTPS/TLS 1.2+

**6\.3.2** Yes - 建議補充：非正式環境採用資料遮罩

**6\.4.1** NA

**6\.4.2** Yes - 建議補充：Session 逾時機制已設計

**6\.4.3** NA

**6\.4.4** Yes - 建議補充：採用企業 AD/AAD 驗證

**6\.5.1** Yes - 建議補充：Dev to Stage 階段包含 SAST、SCA、DAST

**6\.5.2** Yes - 建議補充：所有變更均需通過安全掃描

**6\.5.3** Yes - 建議補充：AWS、Databricks 均提供安全認證報告

**6\.5.4** Yes - 建議補充：Stage 階段需執行第三方滲透測試

## 7\. Infrastructure Design (HA/DR) / Network Considerations

**7\.1.1** Yes - 建議補充：Multi-AZ 部署、RDS 自動備份、S3 版本控制

**7\.1.2** Yes - 建議補充：Fargate 支援自動 Failover，已規劃測試

**7\.2.1** Yes - 建議補充：API Gateway + WAF 作為反向代理

**7\.3.1** Yes - 建議補充：標準 HTTPS、VPC 網路架構

**7\.3.2** Yes - 建議補充：需由網路架構師 (待指定) 確認頻寬需求

## 8\. Performance and Capacity Planning

**8\.1.1** Yes - 建議補充：Stage 環境包含效能測試，以現有系統為基準

**8\.1.2** Yes - 建議補充：Stage 環境用於效能與壓力測試

**8\.2.1** Yes - 建議補充：已規劃 30 輛車初期容量，可擴展至數千輛

**8\.2.2** Yes - 建議補充：採用 S3 Glacier 進行長期歸檔

---

**建議後續動作：**

1. 補充具體的預算數字與資金來源

2. 指定基礎架構與網路審核人員

3. 準備 PICS 文件供未來 FMS 使用

4. 確認效能測試的具體指標與基準值