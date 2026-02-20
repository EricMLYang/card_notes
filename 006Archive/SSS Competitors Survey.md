---
tags:
  - smart-space-solution
---
# SSS Competitors Survey

第三屆亞太地區優良智慧綠建築暨系 統產品獎獲得鉑金獎的樺康智雲股份有限公司及獲得金獎的通航國際股 份有限公司進行本次技術彙編撰寫

## Johnson Controls OpenBlue & Azure

- **Azure IoT Hub:** OpenBlue leverages Azure IoT Hub to connect and manage a vast network of IoT devices deployed in buildings. This enables the collection of real-time data from sensors and equipment, facilitating efficient monitoring and control of building systems.

- **[Azure Digital Twins](https://news.microsoft.com/2020/12/08/johnson-controls-and-microsoft-announce-global-collaboration-launch-integration-between-openblue-digital-twin-and-azure-digital-twins/):** This service is likely used to create virtual representations (digital twins) of physical buildings and assets within OpenBlue.expand_more This allows for better visualization, simulation, and optimization of building operations. 





## 數據中台構想參考 - Smart Building 相關供應商

因為我們產品有規劃 IoT，又以 Smart Space 為主體，系統面來看會很類似範圍較小的 Smart Building，搜尋了一下發現，許多 Smart Building 大廠也都有自己的數據管理平台，也有和 Azure 合作的，因此，我們所謂的數據中台，也許也可以用他們的數據管理平台概念出發，每個企業就是一個  Tenant，其他所有 Building, user …等都歸類在這 Tenant 下，以下幾個主要供應商：

備註：Tenant 翻譯成租戶，是 SaaS 系統的名詞，意思是雲端資源(儲存、計算、應用報表…等) 都以租戶為依據設計

- **Johnson Controls**：

   - 江森自控提供全面的智慧建築解決方案，包括智慧辦公室。他們利用 IoT 感測器收集數據，監控和優化照明、暖通空調 (HVAC)、能源使用等，實現節能和提高舒適度。此外，他們還提供空間管理和預訂系統，幫助企業更有效地利用辦公空間。

   - 提供 OpenBlue 數字平台，用於智能建築的數據分析和管理

- **Honeywell**：提供 Honeywell Forge，這是一個企業績效管理 SaaS 平台

   - Honeywell 的智慧建築解決方案包括智慧辦公室，利用 IoT 感測器收集數據，分析空間利用率、空氣品質、照明等，並提供預測性維護建議。他們的 Vector Space Sense 技術可以幫助企業了解員工如何使用辦公空間，進而優化空間佈局。

   - 供 Honeywell Forge，這是一個企業績效管理 SaaS 平台

- 西門子 (Siemens)

   - 西門子提供 Comfy 應用程式和 Desigo CC 平台，結合 IoT 感測器和樓宇自動化系統，實現智能照明、溫度控制和空間利用分析。員工可以透過 Comfy 應用程式回饋對環境的感受，系統會自動調整，提供更舒適的工作環境。

- 施耐德電機 (Schneider Electric)

   - 施耐德電機的 EcoStruxure 平台整合了 IoT 感測器、樓宇管理系統和能源管理系統，實現能源監控、預測性維護和空間優化。他們的智慧辦公室解決方案還可以整合會議室預訂、訪客管理等功能。

- Enlighted

   - Enlighted 專注於智慧照明解決方案，他們的 IoT 感測器可以收集照明數據，並根據自然光和占用情況自動調整燈光亮度，實現節能和提高舒適度。Enlighted 的解決方案還可以整合其他樓宇系統，如 HVAC 和安全系統。



後續我先抓 **Johnson Controls 為主要研究對象，其簡單歷史如下：**

Johnson Controls 是一家歷史悠久的跨國企業，其歷史沿革可追溯至19世紀末，經過多次的併購與轉型，發展至今成為全球領先的智慧建築解決方案供應商

- 1885年: Warren Johnson 教授創立 Johnson Electric Service Company，專注於恆溫控制系統

- 2016年: 與 Tyco International 合併，成為全球最大的樓宇技術和解決方案供應商。expand_more

- 2017年: 剝離汽車電池業務，專注於樓宇和能源解決方案。

- 2020年: 推出 OpenBlue 數位平台，整合樓宇管理系統、能源管理系統和智慧建築解決方案

- 2021年: 收購 FM:Systems，加強職場管理軟體產品組合。





## Johnson Controls 平台 - OpenBlue

其大致可分成 1. 企業數據管理平台    2. 應用程式平台    3. 串接 IoT 數據，將數據轉成 Digital Twin 的軟體架構，我們初期會主要參考其企業數據管理平台

**[OpenBlue Enterprise Manager:](https://azuremarketplace.microsoft.com/en/marketplace/apps/johnsoncontrols.optimization-tool-for-buildings-energy-equipment?tab=Overview)**[ 一個基於雲端的建築能源和設備管理平台](https://azuremarketplace.microsoft.com/en/marketplace/apps/johnsoncontrols.optimization-tool-for-buildings-energy-equipment?tab=Overview)