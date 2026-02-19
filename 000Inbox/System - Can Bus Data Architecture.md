---
tags:
  - vms
---
# System - Can Bus Data Architecture

## \[ Basic Concept \]

- Electrical:

   - Deals with the generation, distribution, and use of electric power

   - Focuses on higher power applications and raw electricity

   - In EVs, this includes:

      - High voltage battery systems

      - Power distribution networks

      - Electric motors

      - Charging systems

      - Basic lighting systems

      - Heating elements

      - Power cables and connections

- Electronic:

   - Involves circuits that control and process electrical signals

   - Focuses on information processing and control systems

   - Uses semiconductor components

   - In EVs, this includes:

      - Battery Management Systems (BMS)

      - Motor controllers

      - Sensors and control units

      - Infotainment systems

      - Advanced Driver Assistance Systems (ADAS)

      - Communication networks (CAN bus, LIN, FlexRay)

      - Digital displays and interfaces

   Think of it this way: Electrical systems are like the "muscles" of the vehicle, providing power and doing the heavy work, while electronic systems are like the "brain and nervous system," controlling and coordinating everything.

   

## \[ 網路拓撲 \] 

0. EE Network Topology (Electrical/Electronic Network Topology)

   - The network topology partially represents the physical relationships and partially represents the logical relationships.

1. Network Topology Overview:

   - Uses SAE J1939 protocol and "inter" format

   - Managed by a central gateway

   - Divided into 5 CAN (Controller Area Network) branches

2. CAN Bus be separated by 5 CAN Buses: 

   - 動力 EVCAN: For power/drivetrain systems

   - 車身 BodyCAN: For body control systems

   - 底盤  ChassisCAN: For chassis control

   - 娛樂 INFDCAN \[預留\]: Reserved for infotainment systems

   - 診斷 DiagCAN: For diagnostics

3. Terminal Resistor Configuration: 終端電阻節點：EVCAN500kb在GW和BMS各佈置一個120電阻;BodyCAN，ChassiaCAN,INFDCAN各路250kb均在網關和線束遠端佈置共計兩個電阻120

   - EVCAN (500kb):

      - Two 120Ω resistors

      - Located at Gateway and BMS (Battery Management System)

   - BodyCAN, ChassisCAN, INFDCAN (250kb each):

      - Each branch has two 120Ω resistors

      - Located at the gateway and at the end of the wire harness

## \[ Each CAN Bus \]

### **1\. 動力 EVCAN**

- **整車控制器  VCU (Vehicle Control Unit)**

   - MCU命令

   - DCDC命令

   - 制动踏板电耗信息

   - 油门踏板车速

   - 仪表故障

   - 软件版本号

   - 辅件命令

   - 远程锁车控制

   - VCU发送到BMS的VIN

- **電池管理系統 BMS (Battery Management System)**

   - BMU发送的VIN码请求

   - BMS发送到车载终端的编码信息

   - 电池包基本信息1

   - 电池包基本信息2

   - BMS的单体详细电压

   - BMS的单体详细电压1

   - BMS的电芯详细温度

   - BMS发送GB32960中规定需要上传的故障

   - BMS的故障信息2

   - BMS的状态数据1

   - BMS的状态数据2

   - BMS的状态数据3

   - BMS的状态数据4

   - BMS的状态数据5

   - BMS的状态数据6

   - BMS的状态数据7

   - BMS的电量相关数据

   - BMS的允许充放电电流

   - BMS发送到ACcharger的充电状态

   - 多合一项目BMS请求指令

   - BMS发送到 TMS 的数据

   - 灭火控制器发送的广播报文

   - **快速充電樁 QC (Quick Charger)**

- **高壓配電箱控制模組 PDU (Power Distribution Unit)**

   - 高压继电器状态

   - 高压控制板状态

   - 高压板软硬件版本

   - 绝缘信息

   - **直流轉換器 DCDC (DC-DC Converter)**

      - DC状态信

      - DC故障信息

   - **氣泵 AC DCAC_AP (DC-AC for Air Pump)**

      - 气泵模块状态信息

      - 输出功率

   - **油泵 AC DCAC_SP (DC-AC for Steering Pump)** 

      - 油泵模块状态信息

      - 输出功率

- **變速箱控制器 TCU (Transmission Control Unit)**

   - 换挡指令

   - 输入轴参数

   - 故障信息

   - 电机扭矩转速

   - 电机温度故障

   - 电机电压故障

   - 电机电流故障

   - 转VCU控制指令

   - TCU相关状态

- **馬達控制器  PCU (Power Control Unit) 或 MCU (Motor Control Unit)**

   - 电机扭矩转速

   - 电机温度故障

   - 电机电压故障

   - 电机电流故障

- **車載充電機 OBC (On-Board Charger)**

   - OBC状态

   - ACcharger发送BMS的充电状态

- **遠端監控終端 TBOX (Telematics BOX)**

   - 时间参数

   - 控制参数

   - 远程锁车控制

   - 网络管理

- **空調面板 AC (Air Conditioning)**

   - 空调状态信息

   - 工作模式故障

   - 电池液冷设置

   - 压缩机控制指令

   - 空调设置

- **電動空調壓縮機控制器 EC (Electric Compressor)**

   - EC状态版本

   - EC故障信息

- **電動儀表 ICM (Instrument Cluster Module)**

   - 网络管理

   - 仪表车速

   - 仪表里程

   - 仪表车身状态

   - 前方车道图像指令

   - AEBS 开关

### 2\. 車身 BodyCAN

- **行人警報裝置 VSP (Vehicle Sound for Pedestrians)**

   - 行人报警装置发送

- **車身控制器 BCM (Body Control Module)**

   - 灯光

   - 开关状态

   - 巡航控制/车辆车速

   - 灯光及转向灯

   - 雨刮

   - 倒挡

   - 车窗控制

   - 防盗报警

   - 握手密钥

   - 握手随机数

   - 认证状态

   - 网络管理

- **防夾控制器 APM (Anti-Pinch Module)**

   - 车控指令

   - 网络管理

- **胎壓監測 TPMS (Tire Pressure Monitoring System)**

   - 胎压信息

- **安全氣囊控制器 ABM (Airbag Module)**

   - 安全气囊状态

- **盲區監測 BSD (Blind Spot Detection)**

   - BSD系统状态

- **娛樂系統 MP5 (Multimedia Player 5)**

   - 时间

   - 导航画面

   - 空调设置

   - 网络管理

- **點火系統 PEPS**

### **3\. 底盤  ChassisCAN**

- 防鎖死煞車系統 ABS (Anti-lock Braking System) + ESC

   - 电控刹车控制器1

   - 电子制动控制器5

   - 车辆动态稳定性控制1

   - 车辆动态稳定性控制2

   - ABS故障诊断

   - 传输协议-数据传送

   - 传输协议-连接管理

   - 扭矩/速度控制

   - 扭矩/速度控制Driveline Retarder

   - Torque/Speed Control to Engine Retarder

   - Torque/Speed Control to Exhaust Retarder

   - 轮速

   - 车轮施加压力高精度信息

   - 高分辨率轮速

- **緊急煞車系統 AEBS (Autonomous Emergency Braking System)**

   - External Brake Request

   - Advanced Emergency Braking System 1

   - AEBS故障诊断1

   - 传输协议-数据传送

   - 传输协议-连接管理

- **車道偏離系統 LDWS (Lane Departure Warning System)**

   - Forward Lane Image urgent msg

   - 车道偏离状态

- **自動駐車系統 EPB (Electronic Parking Brake)**

   - EPB系统状态

   - EPB故障诊断1

   - 传输协议-连接管理

   - 传输协议-数据传送

   - 临停状态

### 4\. 娛樂 INFDCAN \[預留\]: Reserved for infotainment systems

### 5\. 診斷 DiagCAN: For diagnostics



## \[ PCU (動力控制單元)\]

- 核心功能定義： PCU 是電動車的核心控制裝置，主要負責：

   - 將電池的直流電轉換為電動機所需的交流電

   - 調節電動機的運行狀態

   - 管理能量回收系統

   - 協助電池充電過程

工作流程原理：

1. 電能輸入

- 從電池組獲取直流電源（一般在200V至800V之間）

- 透過DC-DC轉換器調整電壓，供應各組件使用

1. 逆變器轉換

- 將直流電轉換為三相交流電來驅動電動機

- 透過調整輸出頻率和電壓來控制電動機的轉速和扭力

1. 電機控制

- 依據行駛需求（加速、減速、巡航）調節電動機運作

- 使用PWM技術精確控制輸出功率

1. 能量回收

- 在煞車或減速時，將機械能轉為電能

- 透過逆變器將回收電能轉為直流電儲存

1. 電池管理

- 與BMS系統協同運作

- 監控電池狀態，最佳化充放電過程

通訊協定：

1. CAN匯流排：

- 用於與MCU、BMS、VCU等進行數據交換

- 傳輸電壓、電流、溫度和故障資訊

1. 乙太網路：

- 用於高速數據傳輸

- 特別適用於處理大量感測器數據

主要組成部分：

1. 逆變器：轉換電流並控制電動機

2. DC-DC轉換器：轉換電壓供電子設備使用

3. 控制單元：管理整體系統運作

4. 冷卻系統：維持安全工作溫度

5. 感測器：監測各項參數

6. 通訊模組：負責數據傳輸

參考技術規格：

- 輸入電壓：200V\~800V DC

- 輸出功率：50kW\~300kW（依車型而異）

- 效率：95%\~98%

- 冷卻方式：液冷或氣冷

- 工作溫度：-40°C\~85°C

- 通訊速率：CAN匯流排1Mbps，乙太網路100Mbps

要我針對哪個部分再詳細說明嗎？



## 


