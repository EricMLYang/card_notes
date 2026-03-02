---
tags:
  - vms
---
# Data - CAN Bus Data

## \[ Sub System Name \]

- **整車控制器**  VCU (Vehicle Control Unit)

- **電池管理系統** BMS (Battery Management System)

   - **快速充電樁** QC (Quick Charger)

- **馬達控制器**  PCU (Power Control Unit) 或 MCU (Motor Control Unit)

- **變速箱控制器** TCU (Transmission Control Unit)

- **高壓配電箱控制模組** PDU (Power Distribution Unit)

- **車載充電機** OBC (On-Board Charger)

- **遠端監控終端** TBOX (Telematics BOX)

- **直流轉換器** DCDC (DC-DC Converter)

- **氣泵 AC** DCAC_AP (DC-AC for Air Pump)

- **油泵 AC** DCAC_SP (DC-AC for Steering Pump) 

- **電動空調壓縮機控制器** EC (Electric Compressor)

- **電動儀表** ICM (Instrument Cluster Module)

- **空調面板** AC (Air Conditioning)

- 

- **行人警報裝置** VSP (Vehicle Sound for Pedestrians)

- **車身控制器** BCM (Body Control Module)

- **防夾控制器** APM (Anti-Pinch Module)

- **胎壓監測** TPMS (Tire Pressure Monitoring System)

- **安全氣囊控制器** ABM (Airbag Module)

- **盲區監測** BSD (Blind Spot Detection)

- **娛樂系統** MP5 (Multimedia Player 5)

- 

- **防鎖死煞車系統** ABS (Anti-lock Braking System)

- **緊急煞車系統** AEBS (Autonomous Emergency Braking System)

- **車道偏離系統** LDWS (Lane Departure Warning System)

- **自動駐車系統** EPB (Electronic Parking Brake)

- 

- **煙霧警報器** Fire 

- **輔助動力控制器** APU (Auxiliary Power Unit)

- 





## \[VCU\] (Vehicle Control Unit) : 車輛控制單元

- **VCM_Ready:** 車輛控制模組的準備狀態

- **VehPowerMode:** 車輛電源模式，顯示當前動力狀態

- **St_Charge_Awake:** 充電狀態標記，指示車輛是否處於充電模式或系統是否已喚醒

- **L_Battery_Voltage:** 低壓電池（如12V）的電壓數據，用於車輛輔助系統

- **CoolantTemp:** 冷卻液溫度，監控車輛冷卻系統中冷卻液的當前溫度

- **DriveMode:** 駕駛模式，顯示車輛當前模式（如運動、節能、標準等）

- **VehSpd:** 車速

- **cruiseTargetSpeed:** 巡航控制目標速度

- **cruise_main_lamp:** 巡航控制主燈狀態，指示巡航控制是否激活

- **cruise_active:** 巡航控制啟動狀態，顯示系統是否已經啟動

- **DrivingRange:** 剩餘續航里程，顯示電池狀態下的預估可行駛里程

- **MIC_Rly_Sta:** 主斷路器繼電器狀態，指示主電路是否閉合或開啟

- **PDUTotalNegRly:** 電源分配單元的負繼電器狀態，監控電力系統中的電路狀態

- **TotalPosRlySts:** 正極繼電器狀態，監控電力輸送相關的繼電器工作情況

- **BrakePedalStatus:** 剎車踏板狀態，指示剎車踏板是否被踩下

- **BrakePadelPct:** 剎車踏板百分比，顯示剎車踏板踩下的程度

- **MotPedalPosThrottle:** 加速踏板位置，顯示加速踏板的當前位置（油門開度百分比）

- **HandBrakeSts:** 手剎狀態

- **ShiftLeverPosition:** 排檔桿位置( 如P、N、D檔）

- **Gearshift_Cmd:** 換檔指令，顯示電子控制的檔位切換命令

- **Estop_Valid:** 緊急停止狀態，顯示是否有有效的緊急停止指令

- **EleCost100km:** 每百公里預估電力消耗



## \[Power Battery\] 動力電池相關數據欄位：

- **MainNegRelaySt:** 主負極繼電器狀態是否閉合或開啟，影響電池系統的電流流動

- **Charge_Awake:** 充電喚醒狀態，顯示電池是否處於充電模式或是否已準備好充電

- **BMS_HVStatus:** 高壓電池狀態，如電壓異常或故障。

- **PackinsideVolt:** 電池組內部總電壓，表示整個電池組的電壓

- **PackCurrent:** 電池組當前電流，顯示瞬時電流流動

- **InpulseDischrgCurr:** 瞬時放電電流，表示電池短時間內釋放的電流

- **FollowDischrgCurr:** 持續放電電流，表示電池長時間內釋放的穩定電流

- **InpulseChrgCurr:** 瞬時充電電流，表示電池短時間內吸收的電流

- **FollowChrgCurr:** 持續充電電流，表示電池長時間內吸收的穩定電流

- **ST2_SOP:** 充電狀態（State of Power），顯示電池的可用功率

- **BalanceStatus:** 電池平衡狀態，指示電池管理系統是否正在進行單元間的電壓平衡

- **BI1_RateCap:** 電池額定容量，安培小時（Ah）

- **BI1_RatePower:** 電池額定功率，表示最大功率輸出, 千瓦（kW）

- **BI1_RateHVolt:** 電池組的額定工作電壓

- **BI1_BattType:** 電池類型，電池的化學成分，如鋰電池、鎳氫電池

- **BI1_CoolType:** 電池冷卻類型，如液冷、風冷或自然冷卻

- **BattManufacture:** 電池製造商

- **ST5_Max_Ucell:** 單個電池單元的最高電壓，監控電池組內部單元的最大電壓

- **ST5_Min_Ucell:** 單個電池單元的最低電壓，監控電池組內部單元的最小電壓

- **ST5_Avg_Ucell:** 單個電池單元的平均電壓，表示所有單元的平均電壓水平

- **ST4_Max_Temp:** 電池組內最高溫度，

- **ST4_Min_Temp:** 電池組內最低溫度

- **Avg_Temp:** 電池組內的平均溫度

- **ST2_SOE:** 能量狀態（State of Energy），顯示電池剩餘的可用能量。

- **ST2_SOH:** 健康狀態（State of Health），顯示電池的健康狀態，反映老化

- **ST2_SOC:** 電池的充電狀態（State of Charge）（百分比）

- **ChargeAH:** 已充電量，安培小時（Ah），當前充電周期內充入的電量

- **DchargeAH:** 已放電量，安培小時（Ah），當前放電周期內釋放的電量

- **TtlChgAH:** 總充電量，安培小時（Ah），電池的累計充電量

- **SingleChgEnergy:** 單次充電周期內存儲的能量

- **TotChgEnergy:** 電池的累計充電能量。

- **TotDischgEnergy:** 電池的累計放電能量。

- **BMS_RemKM:** 根據當前電池狀態估算剩餘可行駛里程

- **ST1_HeatingStatus:** 電池加熱系統狀態，加熱功能是否啟動

- **ST7_Heat_Temp:** 電池加熱溫度，加熱系統的工作溫度

- **ST1_HeatPosRelaySt:** 正極加熱繼電器狀態

- **ST1_HeatNegRelaySt:** 負極加熱繼電器狀態

- **ST1_CoolingStatus:** 電池冷卻系統狀態

- **ST3_InsDetectorSt:** 絕緣檢測器狀態

- **ST3_PosInsRes:** 正極絕緣電阻，

- **ST3_NegInsRes:** 負極絕緣電阻

- **HVBThmlMod:** 高壓電池熱管理模式，如冷卻或加熱。



## \[MCU & TCU\] 電動機和變速器相關數據欄位：

- **MCUEnable(VCU):** MCU（電動機控制單元）啟動狀態，由 VCU（車輛控制單元）授權

- **IGBT_Enable:** 絕緣柵雙極晶體管（IGBT）啟動狀態，MCU 控制電流流動的開關元件

- **McuRunmodeSts:** 顯示 MCU 當前的運行模式。

- **MCU_Sta:** 提供 MCU 的整體狀態信息。

- **MCUMode(VCU):** MCU 模式，可能包括節能、動力等不同運行模式

- **Work_Mode:** 顯示 MCU 當前狀態，如運行、待機或故障

- **MCU_Fast_DisChar:** MCU 快速放電狀態，是否正在快速放電以防止過載

- **Precharge_Allow:** 指示是否允許對 MCU 進行預充電

- **regenActive:** 再生制動狀態，顯示是否進行能量回收

- **HoldEnable(VCU):** 停車保持功能（Hold）狀態

- **SlopeState:** 坡道狀態，顯示坡道輔助功能是否啟動。

- **Motor_Speed:** 顯示電動機當前轉速（RPM）。

- **TorqueCommand:** VCU 發給 MCU 的扭矩需求指令

- **Motor_Torque:** 顯示電動機當前輸出扭矩

- **Positive TorqLimit:** 正扭矩限制，電動機在前進方向的最大扭矩限制

- **NegTorqLimit:** 負扭矩限制，電動機在反向時的最大扭矩限制

- **VCU_Reqpower:**   VCU 對電動機的功率需求

- **TS4_MCU_Temp:**  MCU 的工作溫度

- **TS4_Motor_Temp:** 電動機內部的工作溫度

- **MCU_DCVoltage:** MCU 接收的直流電源電壓

- **Motor_AC_Current:** MCU 控制下電動機使用的交流電流

- **MCU_DCCurrent:** MCU 接收的直流電流

- **TCU1_TrsminSpd:** 變速器輸入速度，輸入軸當前轉速

- **TCU1_TrsmOutSpd:** 變速器輸出速度，輸出軸當前轉速

- **TS1_TCU_Ready:** TCU 變速器控制單元是否已準備好工作

- **TS1_TCU_Mode:** TCU 變速器的當前運行模式，如自動或手動

- **TS1_CurrentGear:** 變速器當前的檔位（如 P 檔、D 檔）。

- **TS1_Gearshift_Req:** 駕駛員或控制單元的換檔指令

- **TS1_Gearshift_State:** 變速器當前的換檔操作狀態

- **TS1_Gearshift_error:** 指示變速器換檔過程中是否發生錯誤或異常

- **HS1_PTO_State:** 動力輸出軸（PTO）狀態，輔助動力輸出裝置是否已啟用



## \[PDU\] 電力分配單元相關數據欄位

- **PreCharge_Relay_Sta:** 預充電繼電器狀態，顯示主系統的預充電繼電器是否閉合，以避免上電時的電流衝擊

- **PreCharge_Relay_PDU:** PDU 中預充電繼電器的狀態，開啟或關閉

- **Drivers_Relay_PDU:** 驅動系統繼電器狀態 (是否工作), 用於電力控制

- **AuxPreChargeRelaySta:** 輔助系統預充電繼電器狀態，輔助系統（如車內電器）的預充電繼電器是否激活

- **AuxPreCharge_Relay:** 輔助系統預充電繼電器狀態，與輔助系統的預充電過程相關，類似主預充電繼電器

- **AuxDrives_Relay_Sta:** 輔助驅動繼電器狀態，顯示輔助驅動系統（如 HVAC）的繼電器工作狀態。

- **ACCharge_AnodeRly:** 交流充電正極繼電器，顯示交流充電模式下的正極繼電器狀態，確保充電安全。

- **Battery_HV_Link_PDU:** 電池高壓連接狀態，顯示電池與 PDU 之間的高壓連接是否正常。

- **PTC1_Relay_PDU:** 電池加熱器（PTC）繼電器狀態，顯示 PDU 控制的加熱器繼電器狀態，用於寒冷環境下的電池加熱。

- **TopInstall_Relay_Sta:** 與頂裝系統或輔助功能相關的繼電器狀態

- **VCU_Offline:** VCU 離線狀態， VCU 是否離線或失去與其他控制單元的連接





# \[Charge Information\] 充電資訊

- **ChrgMode** ：顯示當前充電系統的運行模式，例如快充、慢充等模式。

- **Charge_Req** ：車輛是否向充電站發送充電請求，通常是車輛端發出

- **B2C_S_VoltageSet**：Battery to Charger **設定電壓**，從電池端傳送到充電器的目標電壓設置值

- **ChrgStatus (**：顯示充電過程的狀態，如正在充電、完成充電或充電中止

- **Charge_Cmd**：從車輛發送到充電系統的充電控制命令，指示系統進行或停止充電

- **B2C_S_CurrentSet**：B2C 設定的目標充電電流值，控制充電器應如何調節電流供應給電池

- **DCChrgConnectSt**：DC 直流充電連接狀態，車輛是否已連接到直流充電器

- **ACChrgConnectSt** ：AC 交流充電連接狀態，車輛是否已連接到交流充電器

- **ACCharge_InputVol**：AC 交流充電時的輸入電壓，測量交流充電器向車輛提供的電壓值

- **Gun1DCPosTemp**：直流充電槍正極端子的位置溫度，監控充電槍的溫度變化

- **CHR_Temp**：可能表示充電過程中其他相關設備或電路的溫度

- **ACCharge_InputCur**：AC 交流充電過程中的輸入電流，測量充電器向車輛供應的電流量

- **DCChrgPos1RlySt (直流充電正極繼電器1狀態)**：直流充電正極端第一個繼電器的狀態，指示該繼電器是否處於開啟或關閉狀態。

- **ChargeportTemp1 (充電口溫度1)**：充電接口的溫度監測，確保充電過程中沒有過熱情況。

- **C2B_N_VoltOutput (C2B 輸出電壓)**：C2B（Charger to Battery），表示從充電器到電池的實際輸出電壓。

- **DCChrgNeg1RlySt** ：直流充電負極端第一個繼電器的狀態，其是否閉合以允許電流流動

- **ChrgRelayCMD**：車輛發送的充電繼電器控制命令，決定充電過程中繼電器的開關

- **C2B_N_CurrOutput**：C2B（Charger to Battery）輸出的實際充電電流

- **DCcharge_Cmd**：車輛向直流充電站發送的充電控制命令，指示直流充電開始或停止

- **ChargeControl** ：總體的充電控制信號

- **OBCHwVer**：OBC（On-board Charger）硬件版本號，車載充電器的硬件配置版本

- **DCchrgAlowVCmd**：允許的直流充電目標電壓設定，充電器應提供的最大電壓範圍

- **AC_CC_Sta** ：交流充電的狀態信息，顯示交流充電的運行狀態

- **OBCSwVer**：車載充電器（OBC）的軟件版本號。

- **DCHVOptCur**：指示最佳的直流高壓充電電流，通常根據電池狀況自動調節以優化充電速度與安全

- **AC_CP_Sta** ：交流充電中 CP（Control Pilot）的狀態，用來監控充電的協商和過程

- **Charge_Time**：當前充電過程持續的時間

- **DCHVOptVol**：顯示直流高壓充電的最佳電壓，根據電池需求進行調節

- **Lock_Sta**：充電插座或充電槍的鎖定狀態，確保在充電過程中無法移除充電槍

- **RechrgCycels**：電池已經完成的充電循環次數

- **RqHVPoerOff**：車輛或充電站發出的關閉高壓電源的請求，用於停止充電過程或進行安全處理

- **S2_Sta**：S2 是充電過程中的一個特定信號階段，表示充電協議中的狀態或步驟

- **CP_Dutyfactor**：CP 信號的占空比，指示充電器的最大充電電流，根據 CP 信號的占空比協商車輛和充電站之間的充電電流



## \[DCDC\] 轉換器數據：負責將高壓電源轉換為低壓，供車內電子系統使用

- **DCDCEnable:** DCDC 轉換器啟動狀態，指示是否允許電源轉換開始

- **HW_EN_DCDC:** 硬件啟用 DCDC，表示轉換器是否由物理硬件系統啟動

- **PreCharge_DCDC:** DCDC 預充電，確保在開始工作前電壓逐步升高到安全範圍，防止瞬間大電流損壞系統

- **Work_DCDC:** DCDC 顯示轉換器是否處於運行模式

- **DC_Voltage_IN:** D輸入電壓，通常來自電動車高壓電池的直流電壓

- **DCDCOutVoltCmd:** 輸出電壓命令，設定轉換器的目標輸出電壓以供應低壓系統

- **DC_Voltage_OUT:** 實際輸出電壓，低壓系統（如 12V 電池）接收到的電壓

- **DC_Current_OUT:** 輸出電流，表示低壓系統消耗的實際電流量

- **DCDC_N_OutPower:** 輸出功率，電壓與電流的乘積，反映轉換器的實際電能輸出

- **DC_Temperature:** 監控轉換器內部或相關元件的溫度，確保運行在安全範圍內





## \[DCAC\] 轉換器將直流電（DC）轉換為交流電（AC），用於驅動車中的交流電機和相關設備

- **HW_EN_APC:** 硬件啟用 APC（交流電源轉換器）的信號，APC 是否被硬件層面啟動

- **HW_EN_SPC:** 硬件啟用 SPC（輔助電源轉換器）的信號，SPC 是否被硬件層面啟動

- **PreCharge_APC:** APC 預充電，在 APC 開始工作前提供穩定電壓以避免瞬間過大電流

- **PreChargeSPC:** SPC 預充電，確保 SPC 系統安全穩定啟動

- **Work_APC:** APC 工作狀態，顯示 APC 是否正在運行

- **Work_SPC:** SPC 工作狀態，顯示 SPC 是否正在運行

- **APC_Voltage_IN:** APC 輸入電壓，通常來自電池或 DCDC 轉換器的直流電壓

- **SPC_Voltage_IN:** SPC 輸入電壓，進入 SPC 轉換器的直流電壓

- **APC_Voltage_OUT:** APC 輸出電壓，轉換後提供給車輛中交流設備的電壓

- **SPC_Voltage_OUT:** SPC 輸出電壓，提供給不同電氣系統的交流電壓

- **APC_Current_OUT:** APC 輸出電流，為交流負載設備提供的實際電流

- **SPC_Current_OUT:** SPC 輸出電流

- **APU_AP_OutPower:** APC 輸出功率，為車內交流設備提供的總電功率

- **APU_SP_OutPower:** SPC 輸出功率

- **APU_AP_Frequency:** APC 輸出頻率，通常為 50Hz 或 60Hz。

- **APU_SP_Frequency:** SPC 輸出頻率

- **APC_Temperature:** 監控 APC 的內部溫度，防止過熱

- **SPC_Temperature:** 監控 SPC 的內部溫度

- **AP_PumpTemp:** APC 冷卻泵溫度，確保冷卻系統正常運行

- **SP_PumpTemp:** SPC 冷卻泵溫度





## \[Hydraulic Steering\] 液壓轉向系統數據，特別針對電動液壓轉向系統 (EHPS)

- **EHPS_State:** EHPS 系統的工作狀態，如運行、待機或故障

- **EHPS_Voltage_IN:** EHPS 輸入電壓，來自車輛電源系統，用於驅動馬達和相關設備

- **EHPS_Current_IN:** EHPS 輸入電流，反映馬達的電流消耗

- **EHPS_MotorTorq:** EHPS 馬達扭矩，用於輔助轉向，幫助駕駛者輕鬆轉動方向盤

- **EHPS_MotorSped:** EHPS 馬達轉速，決定液壓泵速率，影響轉向輔助力度

- **EHPS_OutPower:** EHPS 系統的輸出功率，表示馬達和液壓泵產生的總功率

- **EHPS_Temperure:** EHPS 系統或馬達的溫度，用於監控過熱，確保運行安全

- **EHPS_ZeroState:** EHPS 零位狀態，指示方向盤未轉動或系統無需輔助力

- **EHPS_AngleDirection:** EHPS 感測到的方向盤轉動方向，表示向左或向右

- **SteeringWheelAngle:** 方向盤的實際轉動角度，用於監控轉向狀態

- **SteeringWheelAngleSpd:** 方向盤角速度，測量轉動的快慢，幫助 EHPS 快速反應提供適當輔助力





## \[AC\] 空調系統數據，空調運行、風扇控制、溫度調節等參數

- **AC_Rly_Sta:** AC 繼電器狀態，控制空調系統的開關

- **AC_Work_Mode:** AC 工作模式，如制冷、制熱、通風

- **ECSta:** EC（電子控制器）狀態，監控空調系統的主要控制單元

- **CondFanSts:** 冷凝風扇狀態，影響制冷效果

- **Temperature_Amb:** 表示車內或車外的溫度，用於調節空調運行參數

- **ACSpeedWant:** 所需 AC 風速，駕駛者或系統設定的風速

- **EN_ColdFAN_CAN:** 冷卻風扇使能信號

- **TptCmd:** 溫度命令，設定空調目標溫度

- **EC_IptDCVol:** EC 輸入直流電壓，表示電子控制器的供電狀況

- **FanPWM_Value:** 風扇 PWM 值，控制風扇轉速的脈寬調製信號

- **CondFanReq:** 冷凝風扇請求，指示空調系統要求風扇開始運行

- **ECPow:** EC 功率，空調電子控制器的功耗

- **ColdPump_PWM:** 冷卻泵 PWM 信號，用於調節泵速和冷卻效率

- **CabinCoolReq:** 車廂冷卻請求，表示駕駛艙需要降低溫度

- **ECTpt:** EC 溫度，監控電子控制器的運行溫度

- **Pump_PWM_Value:** 泵 PWM 值，控制冷卻液泵的運行速度

- **ACSignalOn:** AC 信號啟動，顯示空調系統是否已打開

- **ECHwVer:** EC 硬件版本，空調電子控制器的硬件版本號

- **AC_Signal_IN:** AC 信號輸入，監控空調系統接收的控制命令

- **ECSwVer:** EC 軟件版本，空調電子控制器的軟件版本號

- **PTC_Signal_IN:** PTC 加熱器控制信號，指示加熱系統的運行狀態

- **ACPowerAllowed:** 允許的 AC 功率，受車輛電源管理系統限制的最大空調功率

- **Temperature_PTC:** PTC 加熱器的溫度，監控加熱器運行狀況

- **Blower_Signal_IN:** 鼓風機信號輸入，控制風機的運行狀態

- **ACPress:** AC 壓力，監控空調系統的冷媒壓力

- **Temperature_evap:** 蒸發器溫度，用於控制空調的制冷效果

- **MI_Signal_IN:** 未知信號輸入，可能與空調操作模式或診斷信息相關

- **PTSenPress:** PT 傳感器壓力值，監控系統內部壓力

- **Temperature_Evp:** 蒸發器溫度（與前面相同）

- **PTC_Rate:** PTC 加熱速率，表示加熱器的加熱速度

- **PTSenTemp:** PT 傳感器溫度值，監控系統內部溫度

- **T2:** 第二溫度傳感器的讀數，可能與冷卻劑或氣流溫度有關

- **UserReq:** 用戶請求，表示對空調系統的操作

- **ACHwVer:** AC 硬件版本號

- **ACSwVer:** AC 軟件版本號





## \[Safe Failure Mode\] 安全故障模式數據，監控車輛不同子系統的故障，協助系統進入安全模式

- **VCUDTC:** VCU 故障診斷碼，顯示車輛控制系統檢測到的問題或故障

- **EWV_VehFault_Lvl:** EWV（電動車警告系統）檢測到的車輛故障等級

- **BMS_FaultCode:** BMS（電池管理系統）故障碼，顯示電池系統的問題

- **B2V_ST2_FaultLevel:** B2V（電池與車輛）ST2 相關故障等級，可能涉及電池與車輛間的通信或電力傳輸問題

- **B2V_Fult2_FaultNum:** B2V 相關的第二故障編號，用於記錄特定故障事件

- **OBC_DTC:** OBC（車載充電器）故障診斷碼，顯示充電系統的問題，如電壓或電流異常

- **MCU_DTC_Code:** MCU（電機控制單元）故障診斷碼

- **MCU_ErrLevel:** MCU 系統故障等級，表示問題的嚴重性

- **PDU_DTC:** PDU（電力分配單元）故障診斷碼

- **PDU_ErrLevel:** PDU 故障等級

- **DCDC_DTC:** DCDC 轉換器故障診斷碼，顯示高壓到低壓轉換中的問題

- **DCDC_ErrLevel:** DCDC 系統故障等級，指示問題的嚴重程度

- **DCAC-AP_DTC:** DCAC 系統中 APC（交流電轉換器）故障診斷碼，顯示直流到交流電轉換中的問題

- **DCAC_AP_ErrLevel:** DCAC APC 故障等級

- **DCAC-SP_DTC:** DCAC 系統中 SPC（輔助電源轉換器）故障診斷碼，顯示轉換器的異常情況

- **DCAC_SP_ErrLevel:** DCAC SPC 故障等級，指示問題的嚴重性

- **EHPS_DTC:** EHPS（電動液壓轉向系統）故障診斷碼，顯示轉向系統問題，如電機故障或液壓異常。

- **EHPS_ErrLevel:** EHPS 系統故障等級，表示轉向系統問題的嚴重性。

- **TCU_DTC:** TCU（遠程信息控制單元）故障診斷碼，顯示遠程信息系統中的通信或硬件問題

- **ACDTC:** 空調系統故障診斷碼，顯示空調系統的問題，如制冷劑壓力過高或傳感器故障

- **TBOXDTC:** TBOX（遠程信息盒）故障碼，顯示車輛與外部通訊設備的故障或連接問題

- **ECDTC:** EC（電子控制器）故障碼，顯示車輛各子系統電子控制單元的問題或異常





## \[ABS\] (Anti-lock Braking System) 數據

- **ASR brake active:** Anti-Slip Regulation（ASR）或牽引力控制系統的狀態，顯示系統是否正在施加制動力以防止車輪打滑

- **ABSactive:** ABS 是否啟動，表示系統是否正在運作以防止車輪鎖死

- **ABSfullyoperational:** ABS 是否完全運行，顯示系統內是否有故障

- **SteerAxleSpeed:** 轉向軸速度，通常為前軸速度，提供車輛運動的反饋，用於 ABS 監控路面狀況

- **SpdSteerAxleLeft:** 轉向軸左輪速度，用於檢測車輪打滑或兩側速度差，對 ABS 和穩定控制至關重要

- **SpdSteerAxleRight:** 轉向軸右輪速度，與左輪速度比較，確保安全制動

- **SpdDriverAxleLeft:** 驅動軸左輪速度，ABS 和牽引力控制用於監控驅動車輪的速度

- **SpdAddAxleLeft:** 額外軸左輪速度，用於多軸車輛（如卡車），監控額外軸的車輪速度

- **SpdDriverAxleRight:** 驅動軸右輪速度，與左輪速度比較，調整車輛動態

- **SpdAddAxleRight:** 額外軸右輪速度，監控多軸車輛中的額外車輪速度





## \[EPB\] (Electronic Parking Brake) 駐車制動狀態、安全功能（如 Auto-Hold）的啟動，以及制動相關開關狀態

- **EPB_ParkBraStatus:** 電子駐車制動狀態，顯示駐車制動器是否已啟動或釋放

- **AH_ParkActive:** Auto-Hold 功能狀態，當車輛停下時自動啟動駐車制動

- **AH_BraStatus:** Auto-Hold 制動系統狀態

- **ChildLockActive:** 兒童安全鎖狀態

- **LowPreRelLimit:** 低壓釋放限制，表示 EPB 系統內的制動釋放機制壓力閾值

- **IdepedtBraOly:** 獨立制動 狀態，顯示是否使用獨立制動系統，例如 EPB 單獨控制車輪

- **PrakBraForcTest:** 駐車制動力測試，診斷或測試信號，用於檢查駐車制動系統施加的力

- **EPB_BraSwitch:** 電子駐車制動開關狀態，顯示駕駛員是否啟動或釋放了駐車制動

- **ParkBtSwitch:** 駐車按鈕開關狀態，用於啟動駐車制動

- **RelsBtSwitch:** 釋放按鈕開關狀態，用於釋放駐車制動

- **AHBtSwitch:** Auto-Hold 按鈕開關，控制 Auto-Hold 制動功能的啟動或停用



## \[TBOX\] (Telematics Box) 遠程控制、狀態監控、充電管理、空調、及安全功能

- **RmtACReq:** 遠程空調請求

- **RmtACReqTpt:** 遠程空調設定溫度

- **UserReqrACEnd:** 用戶請求空調關閉，表示用戶發送停止遠程空調的指令

- **RmtChgReq:** 遠程充電請求，表示用戶通過應用或遠程系統發起的電池充電請求

- **UserReqrChgEnd:** 用戶請求充電結束，表示用戶發送停止充電的指令

- **LVBChgCmd:** 低壓電池充電指令，指示車輛啟動 12V 電池的充電

- **RmtRdVhlDatReq:** 遠程讀取車輛數據請求，發起遠程讀取車輛數據（如電池狀態、位置、診斷信息）的指令

- **TBOXRdSts:** TBOX 讀取狀態，表示 TBOX 當前正在讀取或處理數據的狀態

- **MPPreHeatWupPur:** 主電源預熱模式，設定車輛的預加熱用途（如車廂暖氣、電池熱管理）。

- **MPPreHeatMode:** 主電源預熱模式，顯示車輛的預熱系統當前運行模式。

- **VCUShtDnwCmd:** VCU 關閉指令，遠程關閉車輛控制單元（VCU）以進行安全或系統重置。

- **Lock_Cmd:** 鎖車指令，遠程鎖定車輛車門的指令。

- **TamperStart_Cmd:** 防盜啟動指令，與車輛防盜檢測系統相關，可能在偵測到未授權訪問時觸發。

- **EmerunlocktimeCmd:** 緊急解鎖時間指令，設定緊急解鎖功能的時間。

- **VCU_Lock_Req:** VCU 鎖車請求，車輛控制單元自動發起的鎖車請求。

- **VCU_PassiveLock_Sta:** VCU 被動鎖定狀態，反映 VCU 管理的被動鎖車狀態（無需用戶操作的自動鎖定）。

- **VCU_TamperStart_Req:** VCU 防盜啟動請求，表示 VCU 偵測到潛在的車輛未授權訪問。

- **VCU_Emerunlock_time:** VCU 緊急解鎖時間，顯示緊急解鎖功能的設定時間或倒計時。

- **TBOX_Lock_SN:** TBOX 鎖定序列號，用於追蹤和記錄遠程鎖車操作。

- **VCU_TBOX_SN_Back:** VCU TBOX 序列號回傳，確認命令已接收，確保 VCU 和 TBOX 之間的安全通信。

- **SeverLinkSts:** 服務器連接狀態，顯示 TBOX 與遠程服務器的連接狀態。





## \[Others\] 主要涉及輪胎管理、車輛安全和先進駕駛輔助系統 (ADAS)

**輪胎管理 (Tire Management):**

- **Tire Location:** 輪胎位置，標識每個輪胎在車輛上的位置（如前左、前右）。

- **Tire Pressure:** 輪胎壓力，顯示每個輪胎的當前氣壓，用於安全、燃油效率和延長輪胎壽命。

- **TirePressThreshold:** 輪胎壓力閾值，設定輪胎的壓力下限，低於此值時觸發低壓警告。

- **Tire Temperature:** 輪胎溫度，監測每個輪胎的溫度，以識別過高溫度可能引起的問題。

- **TireTempThreshold:** 輪胎溫度閾值，超過此溫度會觸發警告，防止輪胎損壞。

**盲點檢測 (BSD - Blind Spot Detection):**

- **BSD_VideoType:** 盲點檢測系統使用的視頻或攝像頭類型。

- **BSD_WarnType1 to BSD_WarnType5:** 不同級別的盲點警告，包含視覺、聲音或觸覺警報。

**車道偏離警告 (LDW - Lane Departure Warning):**

- **LDW_EnableCmd:** 車道偏離警告啟用/停用命令，啟用時監控車道標記。

- **Left side deviation:** 左側偏離，測量車輛與左側車道標記的偏離程度。

- **Right side deviation:** 右側偏離，測量車輛與右側車道標記的偏離程度。

- **LDW WorkSt:** 車道偏離警告系統的運行狀態，顯示系統是否正在監控。

- **LDW 29St:** 與 LDW 系統相關的特定狀態信號，可能表示條件或錯誤代碼。

**泵和電源系統 (Pump and Power Systems):**

- **PumpSts:** 泵的狀態，與車輛冷卻系統、制動液泵或液壓系統相關。

- **VPCErr:** 車輛電源控制系統錯誤，用於診斷電源相關問題。

- **Power_Switch_Sts:** 電源開關狀態，顯示車輛處於開啟、關閉或輔助模式。

- **Power_Solenoid_Sts:** 電磁閥狀態，控制電力或液體在車輛系統中的流動。

**制動和安全系統 (Braking and Safety Systems):**

- **VCM_BrakeLampSt:** 制動燈狀態，反映制動燈是否點亮，通常基於制動踏板動作。

- **ABES_CloseCmd:** 自動緊急制動系統 (ABES) 關閉指令，用於啟動或停用緊急制動功能。

- **ABES State:** 自動緊急制動系統的狀態，顯示其是否準備就緒、運行或出現故障。

- **Collision warning level:** 碰撞警告級別，表示車輛系統檢測到的碰撞嚴重程度。

- **AEBS Found_Obj:** 自動緊急制動系統檢測到的物體，表示 AEBS 正在監控車前物體的距離和速度。

**調試和高壓系統 (Debugging and High Voltage Systems):**

- **Debugging -HVprocess:** 與高壓系統過程相關的調試信號，用於診斷 HV 元件的運行狀況。

- **Debugging -HV:** 高壓系統的一般調試信號，顯示 HV 元件的狀態或健康情況。

- **Debugging -HVOFF:** 高壓系統關閉狀態，用於安全維護或診斷。

- **Debugging - e_state:** 反映 "電氣狀態" 的調試信號，可能與動力總成運行模式或電氣系統狀態相關。