---
tags:
  - smart-space-solution
---
# SSS Data Values



## Office Air-Condition Control

- Feature :

   - Outdoor :

      - **Temperature**

      - **Weather Forecast:** Predicted outdoor temperature and humidity

   - Indoor :

      - **Humidity:** Current room humidity.

      - **Temperature:** Current room temperature

      - **Occupancy:** Whether the room is occupied or not.

   - Operation:

      - **Time of Day:** Time in hours.

   - Reference :

      - **Historical Data:** Past temperature and AC usage data.





## 數據綜合分析效益

- 數據累積的價值

- 控溫：一堆特徵

- 控燈：一堆特徵

![image 54.png](./SSS%20Data%20Values-assets/image%2054.png)



## 能源模組

| **可控制項目 (Y)** | **監控數據 (X)**  | **簡易說明** | 
|---|---|---|
| **空調** | 溫度感測器 | 偵測室內溫度，當溫度過高或過低時，自動調整空調溫度。 | 
|  | 濕度感測器 | 偵測室內濕度，當濕度過高或過低時，調整空調除濕或加濕功能。 | 
|  | CO2 感測器 | 偵測室內二氧化碳濃度，當濃度過高時，自動開啟通風系統。 | 
|  | 預設排程 | 根據預先設定的排程，在特定時間自動調整空調運行模式。 | 
|  | 電力負載 | 當電力負載過高時，自動調整空調溫度或減少運行頻率以節約能源。 | 
|  | 室外溫度 | 根據室外溫度變化，自動調整室內空調溫度。 | 
| **燈光** | 光照感測器 | 偵測室內光線強度，根據光線變化自動調整燈光亮度。 | 
|  | 人體感測器 (PIR) | 偵測是否有人員在場，若無人則自動關閉燈光。 | 
|  | 預設排程 | 根據預先設定的排程，在特定時間自動開關燈光。 | 
|  | 能源價格 | 根據實時能源價格，調整燈光運行模式，以降低能源成本。 | 
| **窗簾** | 光照感測器 | 偵測室內光線強度，根據光線變化自動調整窗簾開關。 | 
|  | 預設排程 | 根據日出日落時間，自動調整窗簾開關。 | 
|  | 天氣預報 | 根據天氣預報，提前調整窗簾設定，例如預期降雨時關閉窗戶。 | 
| **通風系統** | CO2 感測器 | 偵測室內二氧化碳濃度，當濃度過高時，自動開啟通風系統以降低CO2濃度。 | 
|  | 空氣質量感測器 | 偵測室內空氣質量，根據空氣質量自動調整通風系統。 | 
|  | 室內污染物感測器 | 偵測室內的有害物質濃度，當濃度過高時，啟動通風系統以改善空氣質量。 | 



## 會議模組

| **可控制項目 (Y)** | **監控數據 (X)**  | **簡易說明** | 
|---|---|---|
| **燈光** | 會議狀態 | 當會議開始時，自動調整燈光亮度至適合會議的設定，會議結束後恢復至節能模式。 | 
|  | 光照感測器 | 偵測室內光線強度，根據光線變化自動調整燈光亮度以提供最佳的會議環境。 | 
|  | 人體感測器 (PIR) | 偵測會議室內人員活動，若會議室無人則自動關閉燈光以節省能源。 | 
| **空調** | 溫度感測器 | 根據會議室內溫度自動調整空調溫度，確保會議期間舒適的環境。 | 
|  | 會議人數 | 根據會議人數調整空調通風量，確保室內空氣流通和溫度適宜。 | 
|  | CO2 感測器 | 偵測二氧化碳濃度，當濃度過高時，自動增加通風以保持空氣清新。 | 
| **窗簾** | 光照感測器 | 偵測室外光線變化，自動調整窗簾開關以防止眩光或提供充足的自然光。 | 
|  | 會議狀態 | 根據會議安排自動開關窗簾，會議開始時拉上窗簾，會議結束後打開窗簾。 | 
| **會議設備** | 會議預約系統 | 根據預約會議自動開啟會議設備，如投影儀、音響系統等，會議結束後自動關閉以節省能源。 | 
|  | 人體感測器 (PIR) | 偵測會議室內人員活動，根據活動情況調整設備狀態，如自動啟動或暫停投影儀。 | 
| **通風系統** | CO2 感測器 | 偵測室內二氧化碳濃度，當濃度過高時，自動開啟通風系統以降低CO2濃度。 | 
|  | 空氣質量感測器 | 偵測室內空氣質量，根據空氣質量自動調整通風系統。 | 
| **音響系統** | 會議狀態 | 根據會議安排自動調整音響系統，提供清晰的會議音效，會議結束後自動關閉音響設備。 | 
|  | 人體感測器 (PIR) | 偵測會議室內人員活動，根據活動情況調整音響系統，如自動啟動或暫停音響系統。 | 



## 方法

根據上述表格，這裡列出了一些可能的模型與使用方法，以 AI / 機器學習 / 統計學的眼光來幫助你提升智慧辦公室中的空間使用率與能源效率：

### 模型與使用方法

#### 1\. 用多個輸入調控多個輸出

**用法**: 利用多個感測器輸入（例如人體感測器、光照感測器、CO2 感測器）來調控多個輸出（如燈光、空調、窗簾、通風系統）。\
**模型**: 多變量回歸模型、深度學習模型（如LSTM或CNN）\
**說明**: 建立一個多變量回歸模型來預測和調控多個系統，以達到最佳的能源使用和空間舒適度。

#### 2\. 預測未來使用率，預先調控資源

**用法**: 利用歷史使用數據來預測未來的會議室或辦公空間使用率，提前調整燈光、空調和其他設施。\
**模型**: 時間序列預測模型（如ARIMA、Prophet、LSTM）\
**說明**: 使用時間序列模型來分析過去的使用數據，預測未來的使用情況，並提前調整設備運行模式，以提高使用效率和節省能源。

#### 3\. 在用電總量限制下，調控所有設備

**用法**: 根據即時的電力使用情況和預測的需求，在整體用電限制內調整所有相關設備的運行。\
**模型**: 優化模型（如線性規劃、整數規劃）、強化學習模型\
**說明**: 建立一個優化模型來在電力消耗限制內分配資源，確保各系統在最佳狀態下運行。

#### 4\. 依據使用者行為模式自動調整環境設置

**用法**: 利用使用者的歷史行為數據，學習並預測其偏好，並自動調整燈光、空調等設施。\
**模型**: 行為分析模型（如K-means、HMM）、深度學習模型\
**說明**: 使用聚類算法或隱馬爾可夫模型（HMM）來分析使用者行為，並根據其偏好自動調整環境設置，提高舒適度和使用效率。

#### 5\. 分析會議室和辦公空間的使用模式

**用法**: 分析不同時間段的空間使用率，識別高峰期和低峰期，優化空間配置和預約系統。\
**模型**: 群集分析（如K-means）、頻繁項目集分析（如Apriori）\
**說明**: 使用群集分析來識別使用模式和高峰時段，並根據結果調整預約系統和空間配置。

#### 6\. 當設備故障時的即時調控

**用法**: 當某個設備出現故障時，利用即時數據調整其他設備的運行，以維持系統的正常運行。\
**模型**: 即時反應模型（如Decision Trees, SVM）、異常檢測模型\
**說明**: 建立一個即時反應模型來監測設備運行狀況，並在故障發生時即時調整其他設備，保持系統穩定。

#### 7\. 節能優化模型

**用法**: 根據即時能源價格和消耗模式，動態調整所有設備的運行模式以達到最佳節能效果。\
**模型**: 優化算法（如遺傳算法、模擬退火）、強化學習模型\
**說明**: 使用優化算法來動態調整設備運行模式，以最低的能源成本達到最大的運行效率。

這些模型和使用方法可以幫助你有效地管理和優化智慧辦公室中的資源使用，提高空間利用率並降低能源消耗。每個模型的選擇和實施取決於具體的需求和可用的數據。



### 可能的模型與使用方法參考

以下是一些適合用於智慧辦公室的AI和機器學習模型與使用方法的參考資料，幫助提升空間使用率與能源效率：

#### 1\. 用多個輸入調控多個輸出

- **模型**: 多變量回歸模型

- **參考資料**:

   - [Statistical primer: multivariable regression considerations and pitfalls](https://academic.oup.com/ejcts/article/55/2/179/5195284)

#### 2\. 預測未來使用率，預先調控資源

- **模型**: 時間序列預測模型 (如ARIMA、Prophet、LSTM)

- **參考資料**:

   - [Research on short-term and ultra-short-term cooling load prediction](https://www.sciencedirect.com/science/article/pii/S0142061519302762)

#### 3\. 在用電總量限制下，調控所有設備

- **模型**: 優化模型 (如線性規劃、整數規劃)、強化學習模型

- **參考資料**:

   - [An improved office building cooling load prediction model](https://www.sciencedirect.com/science/article/pii/S0360544219303408)

#### 4\. 依據使用者行為模式自動調整環境設置

- **模型**: 行為分析模型 (如K-means、HMM)

- **參考資料**:

   - [Multiple Linear Regression Analysis](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_multivariable/)

#### 5\. 分析會議室和辦公空間的使用模式

- **模型**: 群集分析 (如K-means)、頻繁項目集分析 (如Apriori)

- **參考資料**:

   - [Identification of Multivariable, Linear, Dynamic Models](https://www.sciencedirect.com/science/article/pii/S0142061519302762)

#### 6\. 當設備故障時的即時調控

- **模型**: 即時反應模型 (如Decision Trees, SVM)、異常檢測模型

- **參考資料**:

   - [Multivariable regression analysis to assess energy consumption and CO2 emissions](https://www.sciencedirect.com/science/article/pii/S0306261917310937)

#### 7\. 節能優化模型

- **模型**: 優化算法 (如遺傳算法、模擬退火)、強化學習模型

- **參考資料**:

   - [An online predictive control method with the temperature based](https://link.springer.com/article/10.1007/s12053-020-09825-2)





這些模型和方法能幫助你有效管理和優化智慧辦公室的資源使用，提高空間利用率並降低能源消耗。每個模型的選擇和實施取決於具體需求和可用數據。

以下是一些適合用於智慧辦公室，提升能源效率和使用率的供應商、產品和平台說明：

### 供應商和產品平台

1. **Nest Thermostat by Google Nest**

   - **說明**: Nest Thermostat利用學習算法來優化暖通空調系統的運行，根據用戶行為和環境條件自動調整溫度。這不僅節省了能源，也提高了用戶的舒適度。例如，Nest Thermostat可以根據家庭成員的習慣調整溫度，並在無人時自動降低暖氣或空調的運行頻率，從而節省能源【32†source】。

2. **Deskbird**

   - **說明**: Deskbird提供多種智慧辦公室技術，包括智能顯示屏、智能家具和佔用感測器。這些工具可以優化空間利用率，提高員工的舒適度和生產力。例如，智能顯示屏可以提升視訊會議體驗，智能家具能夠自動調整高度和支撐，佔用感測器則能夠根據實時佔用情況自動調整照明和通風系統【33†source】。

3. **A-Team Global**

   - **說明**: A-Team Global專注於智慧辦公自動化，提供包括Nest Thermostat在內的多種物聯網（IoT）解決方案。這些解決方案能夠通過數據驅動的學習和遠程控制顯著降低能源消耗，並促進能源保存。A-Team Global還提供智慧家具，如具有調整高度和監控姿勢的智能桌椅，這些設施能夠提高員工的舒適度和健康【32†source】【33†source】。

4. **[Businesstechweekly.com](http://Businesstechweekly.com)**

   - **說明**: 提供智能照明系統和智慧溫控系統，這些系統能夠根據自然光、佔用情況和員工偏好自動調整。這些技術不僅節省能源，還能創造舒適且生產力高的工作環境。例如，智能照明系統可以根據光線變化調整亮度，智能溫控系統則可以保持舒適的室內溫度，同時減少碳足跡【31†source】。

這些供應商和產品平台為智慧辦公室的能效管理提供了強大的工具，通過先進的技術和數據驅動的分析來提升能源效率和空間利用率。同時，這些技術還能提高員工的舒適度和工作效率，為企業帶來雙重收益。





### 供應商和產品平台

1. **Nest Thermostat by Google Nest**

   - **說明**: Nest Thermostat利用學習算法來優化暖通空調系統的運行，根據用戶行為和環境條件自動調整溫度。這不僅節省了能源，也提高了用戶的舒適度。例如，Nest Thermostat可以根據家庭成員的習慣調整溫度，並在無人時自動降低暖氣或空調的運行頻率，從而節省能源​ ([A-Team Global](https://a-team.global/blog/revolutionizing-the-workplace-iot-for-smart-office-automation/))​。

2. **Deskbird**

   - **說明**: Deskbird提供多種智慧辦公室技術，包括智能顯示屏、智能家具和佔用感測器。這些工具可以優化空間利用率，提高員工的舒適度和生產力。例如，智能顯示屏可以提升視訊會議體驗，智能家具能夠自動調整高度和支撐，佔用感測器則能夠根據實時佔用情況自動調整照明和通風系統​ ([Deskbird](https://www.deskbird.com/blog/smart-office-technology))​。

3. **A-Team Global**

   - **說明**: A-Team Global專注於智慧辦公自動化，提供包括Nest Thermostat在內的多種物聯網（IoT）解決方案。這些解決方案能夠通過數據驅動的學習和遠程控制顯著降低能源消耗，並促進能源保存。A-Team Global還提供智慧家具，如具有調整高度和監控姿勢的智能桌椅，這些設施能夠提高員工的舒適度和健康​ ([A-Team Global](https://a-team.global/blog/revolutionizing-the-workplace-iot-for-smart-office-automation/))​​ ([Deskbird](https://www.deskbird.com/blog/smart-office-technology))​。

4. **[Businesstechweekly.com](Businesstechweekly.com)**

   - **說明**: 提供智能照明系統和智慧溫控系統，這些系統能夠根據自然光、佔用情況和員工偏好自動調整。這些技術不僅節省能源，還能創造舒適且生產力高的工作環境。例如，智能照明系統可以根據光線變化調整亮度，智能溫控系統則可以保持舒適的室內溫度，同時減少碳足跡​ ([Businesstechweekly.com](Businesstechweekly.com))​。



## 應用-能源管理效率

- **近零耗能建築簡介**

   - 建築能效評估系統——TBERS、R-BERS

   - **[綠建築標章](http://gb.tabc.org.tw/ "財團法人台灣建築中心 - 綠建築標章")**

   - 節能標章

   - 再生能源憑證



## 基礎設施

- 數據化

### 物聯網

- 價值：

   - 監控、自動化、控制，產生的服務

   - 讓物理資訊和其他 OT 資訊結合

- 技術趨勢：

   - 有線變無線，部署跟維護負擔大幅降低

   - 傳感器功能變強，體現在多功能傳輸整合以及不同傳感器整合，有助於部署管理

## Edge Compute & 5G





## Product Cloud Architecture 

Johnson Controls OpenBlue 

Johnson Controls OpenBlue 是一個 SaaS（軟體即服務）平台：旨在將建築生態系統中的 IT 和 OT 數據整合在一起。它利用雲端技術、人工智慧 (AI) 和物聯網 (IoT) 來優化建築性能、提高能源效率、改善空間利用和設備性能，並確保居住者的健康和福祉。

OpenBlue Enterprise Manager: 一個基於雲端的建築能源和設備管理平台

<https://www.johnsoncontrols.com/openblue/enterprise-manager>

the web-based application that allows users to monitor, control, and optimize building performance using the data and insights from the OpenBlue Cloud.

OpenBlue Cloud: The core cloud platform for OpenBlue, providing data storage, processing, and analytics capabilities.

OpenBlue Companion: 一個面向使用者的智慧建築行動應用程式

OpenBlue Connected Chillers: 一個將設備數據連接到雲端的解決方案

OpenBlue Bridge: An IoT connectivity platform that securely connects building systems and devices to the OpenBlue Cloud.

Hybrid architecture design

Protect backend APIs by using Azure API Management and Azure AD B2C

Yes, your described architecture is absolutely possible in Azure. It's a common hybrid cloud scenario where the management system (your SaaS application) resides in the public Azure cloud, while the customer's data is stored in their own private Azure cloud environment (or on-premises infrastructure).

Here's how it typically works, along with relevant articles:

Secure Network Connectivity:

ExpressRoute: This establishes a dedicated private connection between your public Azure environment and the customer's private Azure environment. This is the most secure and reliable option.

Site-to-Site VPN: This is a more cost-effective option that uses encryption to create a secure tunnel over the public internet.

Reference:

ExpressRoute documentation: <https://learn.microsoft.com/en-us/azure/expressroute/>

Site-to-Site VPN documentation: <https://learn.microsoft.com/en-us/azure/vpn-gateway/>

Data Access:

Private Endpoints: This allows your SaaS application to access the customer's private Azure resources (like databases) as if they were within your own virtual network, without exposing them to the public internet.

Service Endpoints: This is similar to private endpoints, but specifically for Azure services like Azure Storage or Azure SQL Database.

Reference:

Private Endpoints documentation: <https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview>

Service Endpoints documentation: <https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview>

Authentication and Authorization:

Azure Active Directory (Azure AD): This can be used to manage user identities and control access to both the SaaS application and the private Azure resources. You can use Azure AD to implement single sign-on (SSO) for a seamless user experience.

Reference:

Azure Active Directory documentation: <https://learn.microsoft.com/en-us/azure/active-directory/>

Data Security:

Encryption: Ensure data is encrypted both at rest (in the database) and in transit (between the SaaS application and the database).

Firewall and Network Security Groups (NSGs): Use these to control network traffic and restrict access to the private Azure resources.

Reference:

Azure Data Encryption documentation: <https://learn.microsoft.com/en-us/azure/security/fundamentals/encryption-overview>

Azure Firewall documentation: <https://learn.microsoft.com/en-us/azure/firewall/>

Network Security Groups documentation: <https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview>

Additional Tips:

Consider using Azure API Management to create a secure and scalable API gateway for your SaaS application to interact with the private Azure resources.

Use Azure Monitor and Azure Security Center to monitor the hybrid environment for security threats and performance issues.

By following these best practices and utilizing Azure's hybrid cloud capabilities, you can create a secure and efficient architecture where your SaaS application in the public cloud can seamlessly access and manage customer data residing in private Azure environments.

pen_spark

Sources

info

[learn.microsoft.com/en-us/answers/questions/1282392/private-link-for-multiple-services](learn.microsoft.com/en-us/answers/questions/1282392/private-link-for-multiple-services)

[stackoverflow.com/questions/58978371/azure-function-or-web-service-with-internal-ip-address](stackoverflow.com/questions/58978371/azure-function-or-web-service-with-internal-ip-address)

[www.examtopics.com/discussions/microsoft/view/111017-exam-az-140-topic-6-question-3-discussion/](www.examtopics.com/discussions/microsoft/view/111017-exam-az-140-topic-6-question-3-discussion/)

[www.examtopics.com/discussions/microsoft/view/51523-exam-az-104-topic-5-question-54-discussion/](www.examtopics.com/discussions/microsoft/view/51523-exam-az-104-topic-5-question-54-discussion/)


