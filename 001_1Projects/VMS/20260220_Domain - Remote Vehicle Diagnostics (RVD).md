---
tags:
  - vms
---
# **Domain - Remote Vehicle Diagnostics (RVD)**

## Company

- Softing Automotive

   - Offers cloud-based remote diagnostics and troubleshooting, including over-the-air software updates and remote technical support.

   - <https://automotive.softing.com/fileadmin/sof-files/img/ae/anwendungen/180220_WEB_softing_AC_Flyer.pdf>

   - <https://automotive.softing.com/products/softing-tdx/softing-tdx-next-generation-cloud-based-aftersales-diagnostics.html>

- Samsara

   - Their cloud platform utilizes sensor data to provide predictive maintenance insights, helping fleet managers address issues before they become major problems.

   - **[A Samsara platform dive](https://hhhypergrowth.com/a-samsara-platform-dive/)**

- Bosch Automotive Aftermarket

   - Service: Bosch offers IoT-based remote diagnostics leveraging CAN bus data. Their Bosch Connected Mobility Solutions can connect to vehicles via the CAN bus and provide real-time data for vehicle health monitoring and diagnostics.

   - **[Connected Mobility](https://www.bosch-softwaretechnologies.com/en/industries/mobility/)**

- Geotab

   - Service: Geotab's Fleet Management System offers remote diagnostics using CAN bus data. Through its MyGeotab platform, fleet managers can monitor vehicle performance, detect faults, and run predictive diagnostics.



---



## \[ Our Client Consider Important\]

- [Domain-Battery Management System (BMS).md](./Domain-Battery%20Management%20System%20\(BMS\).md)

   - Battery Life & **Degradation**

   - Range & Fuel efficiency

- [Domain - Motor & Inverter.md](./Domain%20-%20Motor%20&%20Inverter.md)

- Error Codes and Diagnostic Messages







## **\[電動車診斷分析結果主題分類與詳細說明\]**

基於您提供的情境和資訊，以下將電動車的診斷分析結果進行最適當的主題分類。每個主題包含說明及所需的數據，旨在協助您說服客戶採用我們團隊的數據處理、分析、建模能力，並提供優質的儀表板（Dashboard）設計。

---

### 1\. 電池管理系統（BMS）

**說明：**
電池是電動車的核心，直接影響續航里程、安全性和壽命。BMS 負責監控電池的各項狀態，包括電壓、溫度、電流，並管理充放電過程，以確保電池在安全範圍內運行，防止過充、過放及熱失控。

**需要的數據：**

- **電池電壓與電流：**

   - `L_Battery_Voltage`：低壓電池電壓

   - `Battery_HV_Link_PDU`：電池高壓連接狀態

- **電池溫度：**

   - `Temperature_PTC`：PTC 溫度

- **充放電狀態：**

   - `ChrgStatus`：充電狀態

   - `Charge_Cmd`：充電命令

- **電池健康與故障診斷：**

   - `PDU_DTC`：PDU 故障診斷碼

   - `PDU_ErrLevel`：PDU 故障等級

   - `SOH`（需進一步計算）：電池健康狀態

---

### 2\. 續航與能效監控（Range & Fuel Efficiency）

**說明：**
監控車輛的能源消耗和續航里程，有助於優化車輛性能、降低運營成本，並提升用戶體驗。通過分析能耗數據，可以預測車輛的剩餘續航里程，並進行能效優化。

**需要的數據：**

- **能源消耗：**

   - `DC_Current_OUT`：DCDC 輸出電流

   - `APC_Current_OUT`：APC 輸出電流

   - `Motor_Torque`：電動機扭矩

- **車速與動力輸出：**

   - `VehSpd`：車速

   - `Motor_Speed`：電動機轉速

- **效率參數（需進一步計算）：**

   - 車輛總能耗與動力輸出比率

---

### 3\. 馬達與逆變器診斷（Motor & Inverter Diagnostics）

**說明：**
馬達和逆變器是電動車的驅動核心，其性能和可靠性直接影響車輛的動力輸出和能源效率。及時診斷異常狀況可防止動力系統故障，確保車輛穩定運行。

**需要的數據：**

- **馬達狀態：**

   - `MCU_Sta`：MCU 狀態

   - `McuRunmodeSts`：MCU 運行模式狀態

   - `Motor_Speed`：電動機轉速

   - `Motor_Torque`：電動機扭矩

- **溫度監控：**

   - `TS4_MCU_Temp`：MCU 溫度

   - `TS4_Motor_Temp`：電動機溫度

- **故障診斷：**

   - `MCU_DTC_Code`：MCU 故障診斷碼

   - `MCU_ErrLevel`：MCU 故障等級

- **逆變器狀態：**

   - `IGBT_Enable`：IGBT 啟動狀態

---

### 4\. 車輛控制系統（VCU Diagnostics）

**說明：**
車輛控制系統負責協調車輛的各個部分，確保其正常運行和安全性。它監控車速、加速、制動等關鍵參數，並管理車輛的電源模式和運行狀態。

**需要的數據：**

- **車輛狀態：**

   - `VCM_Ready`：車輛控制模組準備狀態

   - `VehPowerMode`：車輛電源模式

   - `VehSpd`：車速

   - `DriveMode`：駕駛模式

- **制動系統：**

   - `BrakePedalStatus`：剎車踏板狀態

   - `BrakePadelPct`：剎車踏板百分比

- **換檔系統：**

   - `ShiftLeverPosition`：排檔桿位置

   - `Gearshift_Cmd`：換檔指令

   - `TS1_CurrentGear`：當前檔位

   - `TS1_Gearshift_error`：換檔錯誤

- **緊急狀態：**

   - `Estop_Valid`：緊急停止狀態

- **故障診斷：**

   - `VCUDTC`：VCU 故障診斷碼

---

### 5\. 熱管理系統（Thermal Management System）

**說明：**
熱管理系統確保電池、馬達和電子設備在最佳溫度範圍內運行，防止過熱或過冷，從而維持性能和安全性。有效的熱管理可延長組件壽命並提升運行效率。

**需要的數據：**

- **冷卻系統：**

   - `CoolantTemp`：冷卻液溫度

- **設備溫度監控：**

   - `TS4_MCU_Temp`：MCU 溫度

   - `TS4_Motor_Temp`：電動機溫度

- **空調系統：**

   - `AC_Work_Mode`：AC 工作模式

   - `AC_Rly_Sta`：AC 繼電器狀態

   - `Temperature_Amb`：環境溫度

   - `ACPress`：AC 壓力

   - `AC_Temperure`：AC 溫度

---

### 6\. 充電系統診斷（Charging System Diagnostics）

**說明：**
充電系統的健康狀況決定了電池的充電效率、壽命和安全性。有效的充電管理可以延長電池壽命並提高用戶體驗，確保充電過程的安全和穩定。

**需要的數據：**

- **充電狀態：**

   - `ChrgMode`：充電模式

   - `ChrgStatus`：充電狀態

   - `DCChrgConnectSt`：DC 充電連接狀態

   - `ACChrgConnectSt`：AC 充電連接狀態

- **充電安全監控：**

   - `ChargeportTemp1`：充電口溫度

   - `ChrgRelayCMD`：充電繼電器命令

- **充電故障診斷：**

   - `ACDTC`：AC 故障診斷碼

---

### 7\. 遠程通訊與診斷系統（Remote Communication & Diagnostics）

**說明：**
CAN Bus 通訊和遠程診斷系統確保車輛內部各模組的協同工作，並支持遠程監控和更新。這對於實時監控車輛狀況、故障排除和軟體更新至關重要。

**需要的數據：**

- **通訊狀態：**

   - `CAN_Bus_Health_Status`（需進一步定義）：CAN Bus 通訊健康狀態

- **遠程診斷：**

   - `VCUDTC`：VCU 故障診斷碼

   - `MCU_DTC_Code`：MCU 故障診斷碼

   - `PDU_DTC`：PDU 故障診斷碼

   - `EHPS_DTC`：EHPS 故障診斷碼

- **軟體更新狀態：**

   - `Software_Update_Status`（需進一步定義）：軟體更新狀態

---

### 8\. 安全與故障管理（Safety & Fault Management）

**說明：**
確保車輛運行的安全性，及時識別和處理各種故障，防止事故發生。包括監控緊急停止狀態、故障等級以及各系統的故障碼。

**需要的數據：**

- **緊急狀態：**

   - `Estop_Valid`：緊急停止狀態

- **故障等級：**

   - `EWV_VehFault_Lvl`：車輛故障等級

   - `MCU_ErrLevel`：MCU 故障等級

   - `PDU_ErrLevel`：PDU 故障等級

- **安全故障診斷碼：**

   - `VCUDTC`：VCU 故障診斷碼

   - `MCU_DTC_Code`：MCU 故障診斷碼

   - `PDU_DTC`：PDU 故障診斷碼

   - `EHPS_DTC`：EHPS 故障診斷碼

   - `ACDTC`：AC 故障診斷碼

---

### 9\. 液壓轉向系統（EHPS）診斷

**說明：**
液壓轉向系統（EHPS）影響車輛的操控性和安全性。監控其運行狀態和參數，可及早發現潛在問題，確保轉向系統的可靠性。

**需要的數據：**

- **轉向系統狀態：**

   - `EHPS_State`：EHPS 狀態

- **電壓與電流：**

   - `EHPS_Voltage_IN`：EHPS 輸入電壓

   - `EHPS_Current_IN`：EHPS 輸入電流

- **溫度監控：**

   - `EHPS_Temperure`：EHPS 溫度

- **轉向扭矩：**

   - `EHPS_MotorTorq`：EHPS 馬達扭矩

---

### 10\. 制動系統診斷（Brake System Diagnostics）

**說明：**
制動系統是車輛安全的關鍵組成部分，除了再生制動，傳統的液壓制動系統需要持續監控以確保行車安全。包括剎車踏板狀態、手剎狀態及制動系統故障碼。

**需要的數據：**

- **剎車踏板狀態：**

   - `BrakePedalStatus`：剎車踏板狀態

   - `BrakePadelPct`：剎車踏板百分比

- **手剎狀態：**

   - `HandBrakeSts`：手剎狀態

- **再生制動狀態：**

   - `regenActive`：再生制動激活狀態

- **制動故障診斷：**

   - `Brake_System_DTC`（需進一步定義）：制動系統故障診斷碼

---

### 11\. 輪胎與懸掛系統（Tire & Suspension Diagnostics）

**說明：**
輪胎和懸掛系統影響車輛的操控性、安全性和能耗。監控胎壓和懸掛狀態，可提升行車安全並優化車輛性能。

**需要的數據：**

- **胎壓監測：**

   - `Tire_Pressure_Status`（需進一步定義）：輪胎胎壓狀態

- **懸掛系統狀態：**

   - `Suspension_Status`（需進一步定義）：懸掛系統狀態

- **轉向系統：**

   - `EHPS_State`：電子液壓轉向系統狀態

   - `EHPS_Voltage_IN`：EHPS 輸入電壓

   - `EHPS_Current_IN`：EHPS 輸入電流

   - `EHPS_Temperure`：EHPS 溫度

---

### 12\. 車內環境與舒適性監控（In-Vehicle Environment & Comfort Monitoring）

**說明：**
車內環境影響駕駛員和乘客的舒適性，進而影響用戶體驗。監控空調系統、環境溫度等參數，可提升車內舒適度並優化能耗。

**需要的數據：**

- **空調系統：**

   - `AC_Work_Mode`：AC 工作模式

   - `AC_Rly_Sta`：AC 繼電器狀態

   - `Blower_Signal_IN`：鼓風機信號輸入

   - `FanPWM_Value`：風扇 PWM 值

- **環境參數：**

   - `Temperature_Amb`：環境溫度

   - `Temperature_PTC`：PTC 溫度

   - `Temperature_evap`：蒸發器溫度

- **用戶請求：**

   - `UserReq`：用戶請求

---

**結論：**

透過上述主題分類，我們可以為客戶提供一個全面且深入的電動車診斷分析方案。我們的團隊具備強大的數據處理、分析和建模能力，能夠有效地處理來自 CAN Bus 的大量數據，並將其轉化為有價值的見解。此外，我們可以設計直觀且功能強大的儀表板（Dashboard），將關鍵資訊以易於理解的方式呈現，協助客戶進行車隊管理和決策。

**儀表板（Dashboard）設計建議：**

- **實時監控視圖：** 顯示關鍵參數的實時數據，如電池電壓、馬達轉速、車速等。

- **故障警報系統：** 即時提示各系統的故障警報，並顯示故障等級及詳細資訊。

- **歷史數據分析：** 提供過去數據的趨勢分析，幫助預測未來的維護需求。

- **能效報告：** 展示車輛的能耗情況和續航里程預估，幫助優化運營策略。

- **預測性維護建議：** 基於數據模型，提供預測性維護建議，降低維護成本並提高車輛運營效率。

**附加說明：**

- **優先關注項目：** 根據客戶的重點關注，我們特別強調電池管理系統（BMS）、續航與能效監控、以及馬達與逆變器的故障診斷。

- **數據整合與可視化：** 我們將整合多來源的 CAN Bus 數據，並通過高效的數據可視化技術，確保資訊的即時性和準確性。

- **彈性擴展：** 系統設計具備高度的彈性，可根據客戶需求進行功能擴展和定制。

希望上述分類和詳細說明能夠全面展示我們團隊在電動車診斷分析方面的專業能力，協助您成功說服客戶採用我們的 VMS 開發方案。



---

##  **\[遠程診斷分析產品功能的重要程度分類\] view by client’s data** 

### **一級重要性（關鍵功能）**

這些功能直接關係到車輛的安全運行和核心性能，需優先關注和實施。

1. **車輛控制單元（VCU）診斷**

   - **VCM_Ready**：車輛控制模組準備狀態

   - **VehPowerMode**：車輛電源模式

   - **CoolantTemp**：冷卻液溫度

   - **L_Battery_Voltage**：低壓電池電壓

   - **BrakePedalStatus**：剎車踏板狀態

   - **BrakePadelPct**：剎車踏板百分比

   - **Estop_Valid**：緊急停止狀態

2. **電動機和變速器（MCU & TCU）診斷**

   - **MCU_Sta**：MCU 狀態

   - **McuRunmodeSts**：MCU 運行模式狀態

   - **Motor_Speed**：電動機轉速

   - **Motor_Torque**：電動機扭矩

   - **TS4_MCU_Temp**：MCU 溫度

   - **TS4_Motor_Temp**：電動機溫度

   - **IGBT_Enable**：IGBT 啟動狀態

   - **TS1_TCU_Mode**：TCU 模式

   - **TS1_CurrentGear**：當前檔位

   - **TS1_Gearshift_error**：換檔錯誤

3. **安全故障模式診斷**

   - **VCUDTC**：VCU 故障診斷碼

   - **MCU_DTC_Code**：MCU 故障診斷碼

   - **PDU_DTC**：PDU 故障診斷碼

   - **EHPS_DTC**：EHPS 故障診斷碼

   - **ACDTC**：AC 故障診斷碼

   - **EWV_VehFault_Lvl**：車輛故障等級

   - **MCU_ErrLevel**：MCU 故障等級

   - **PDU_ErrLevel**：PDU 故障等級

4. **液壓轉向系統（EHPS）診斷**

   - **EHPS_State**：EHPS 狀態

   - **EHPS_Voltage_IN**：EHPS 輸入電壓

   - **EHPS_Current_IN**：EHPS 輸入電流

   - **EHPS_MotorTorq**：EHPS 馬達扭矩

   - **EHPS_Temperure**：EHPS 溫度

---

### **二級重要性（重要功能）**

這些功能對車輛性能和用戶體驗有重要影響，需要重點關注。

1. **電力分配單元（PDU）診斷**

   - **PreCharge_Relay_Sta**：預充電繼電器狀態

   - **Drivers_Relay_PDU**：驅動系統繼電器狀態

   - **Battery_HV_Link_PDU**：電池高壓連接狀態

   - **PTC1_Relay_PDU**：電池加熱器繼電器狀態

2. **充電系統診斷**

   - **ChrgMode**：充電模式

   - **ChrgStatus**：充電狀態

   - **DCChrgConnectSt**：DC 充電連接狀態

   - **ACChrgConnectSt**：AC 充電連接狀態

   - **ChargeportTemp1**：充電口溫度

   - **ChrgRelayCMD**：充電繼電器命令

   - **Charge_Cmd**：充電命令

3. **DCDC 轉換器診斷**

   - **DCDCEnable**：DCDC 啟動

   - **Work_DCDC**：DCDC 工作狀態

   - **DC_Voltage_IN**：DCDC 輸入電壓

   - **DC_Voltage_OUT**：DCDC 輸出電壓

   - **DC_Current_OUT**：DCDC 輸出電流

   - **DC_Temperure**：DCDC 溫度

4. **DCAC 轉換器診斷**

   - **Work_APC**：APC 工作狀態

   - **APC_Voltage_IN**：APC 輸入電壓

   - **APC_Voltage_OUT**：APC 輸出電壓

   - **APC_Current_OUT**：APC 輸出電流

   - **APC_Temperure**：APC 溫度

5. **空調系統（AC）診斷**

   - **AC_Work_Mode**：AC 工作模式

   - **AC_Rly_Sta**：AC 繼電器狀態

   - **Temperature_Amb**：環境溫度

   - **ECTpt**：EC 溫度

   - **ACPress**：AC 壓力

   - **CondFanSts**：冷凝風扇狀態

   - **FanPWM_Value**：風扇 PWM 值

---

### **三級重要性（一般功能）**

這些功能影響車輛的舒適性和輔助性能，可作為附加監控項目。

1. **車輛其他狀態監控**

   - **DriveMode**：駕駛模式

   - **VehSpd**：車速

   - **MotPedalPosThrottle**：加速踏板位置

   - **HandBrakeSts**：手剎狀態

   - **ShiftLeverPosition**：排檔桿位置

   - **Gearshift_Cmd**：換檔指令

2. **再生制動和能量回收**

   - **regenActive**：再生制動激活狀態

   - \*\*HoldEnable(VCU)\*\*：停車保持功能啟動狀態

   - **SlopeState**：坡道狀態

3. **輔助系統診斷**

   - **AuxPreChargeRelaySta**：輔助系統預充電繼電器狀態

   - **AuxDrives_Relay_Sta**：輔助驅動繼電器狀態

4. **環境與舒適性監控**

   - **Temperature_PTC**：PTC 溫度

   - **Blower_Signal_IN**：鼓風機信號輸入

   - **Temperature_evap**：蒸發器溫度

   - **UserReq**：用戶請求


