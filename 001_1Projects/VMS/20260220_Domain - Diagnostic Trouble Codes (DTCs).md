---
tags:
  - vms
---
# **Domain - Diagnostic Trouble Codes (DTCs)**

### Reference

- [A Guide to Understanding DTC Codes](https://www.samsara.com/guides/dtc-codes)

## \[ Dashboard \]

- 車輛狀態總覽（Vehicle Overview）

   - 車輛基本信息：Battery SOH、里程數、年分

   - 健康指標儀錶盤：以儀表盤的形式顯示車輛健康狀況的綜合評分，快速反映車輛當前狀態。這個儀表盤可以整合電池、電機、電子控制單元（ECU）等主要系統的狀態，並以顏色（如綠色為正常、黃色為警告、紅色為嚴重故障）來表示。

- 即時故障監控（Live Fault Monitoring）

   - 故障代碼列表：顯示車輛當前活躍的故障代碼，以表格形式呈現，包括以下欄位：

      - 故障代碼（DTC Code）

      - 故障描述（Fault Description）

      - 嚴重程度（Severity Level）：用顏色標示，如紅色（嚴重）、黃色（警告）

      - 觸發時間（Timestamp）

      - 故障指示燈：類似車內儀表盤上的故障燈，儀表板上可以顯示不同系統（如電池、電機、充電系統、制動系統）的狀態燈，顯示該系統是否存在問題。可以直接從故障燈點擊進入詳細信息區域。

- 歷史故障記錄（Historical Faults）

   - 時間軸視圖：採用時間軸的形式，展示該車輛在過去一段時間內出現的故障記錄。這能夠幫助使用者識別反覆出現的問題。

   - 折線圖：顯示歷史故障發生的頻率，區分不同類型的故障（例如，以不同顏色的線條表示不同系統的故障），協助分析長期趨勢。

- 詳細信息區（Detailed Information）

   - 選定故障詳情：當選中某個故障代碼時，Dashboard 應顯示該故障的詳細信息，包括：

      - 故障描述及原因（簡明解釋故障代碼的含義）

      - 故障影響（該問題可能對車輛性能或安全造成的影響）

      - 修復建議（建議的解決方案或維修步驟）

      - 錯誤次數（該故障在特定時間段內發生的次數）

      - 技術數據：若需要進一步分析，提供來自 CANBus、BMS 等系統的技術數據，如電池電壓、電流、溫度等，以幫助診斷。

- 建議行動區（Suggested Actions）

   - 維修建議：根據故障嚴重程度，自動生成維修建議，例如："立即聯絡維修中心" 或 "檢查電池狀態"。

   - 維修預約按鈕：提供快速操作，如一鍵預約維修服務，方便車主立即採取行動。



## \[ Fault Codes - Battery Management System \]

EV battery-related  : 

### 1\. **Voltage-Related Alarms**

- **Single Cell Overvoltage** (Codes 1-3)

   - Trigger: Cell voltage (Umax) ≥ 3.8V, 3.85V, 3.9V (depending on level)

   - Resolution: Limit power to 0%, stop charging.

   - Clear Condition: Umax drops below thresholds (e.g., < 3.65V, 3.7V).

- **Single Cell Undervoltage** (Codes 4-6)

   - Trigger: Cell voltage (Umin) ≤ 2.8V (0℃), 2.5V (<0℃) or lower.

   - Resolution: Power limitation (50% to 0%), request high voltage shutdown.

   - Clear Condition: Umin rises above thresholds (e.g., > 2.8V, 2.4V).

- **Total Voltage Overvoltage** (Codes 8-10)

   - Trigger: Total voltage (Vbat) ≥ 3.65V*N, 3.75V*N, 3.8V\*N (N = number of cells in series).

   - Resolution: Power limitation (50% to 0%), stop charging.

   - Clear Condition: Vbat drops below threshold (e.g., < 3.65V\*N-5).

- **Total Voltage Undervoltage** (Codes 11-13)

   - Trigger: Total voltage (Ubat) ≤ 2.85V*N, 2.6V*N, 2.4V\*N (adjusted based on temperature).

   - Resolution: Power limitation (50% to 0%), request high voltage shutdown.

   - Clear Condition: Ubat rises above threshold (e.g., > 2.85V\*N+5).

### 2\. **Temperature-Related Alarms**

- **Cell High Temperature** (Codes 14-16)

   - Trigger: Tmax ≥ 60℃, 65℃, 67℃ (depending on level).

   - Resolution: Power limitation (50% to 0%), stop charging.

   - Clear Condition: Tmax < specific thresholds (e.g., 58℃).

- **Cell Low Temperature** (Code 17)

   - Trigger: Tmin ≤ -35℃.

   - Resolution: None specified.

   - Clear Condition: Tmin > -30℃.

- **Temperature Difference Too Large** (Codes 18-20)

   - Trigger: ΔT ≥ 25℃, 30℃, 35℃.

   - Resolution: None specified.

   - Clear Condition: ΔT < specified thresholds (e.g., < 23℃).

### 3\. **Current-Related Alarms**

- **Pulse Discharge Current Exceeded** (Codes 22-24)

   - Trigger: I ≥ 105%, 120%, 125% of rated current.

   - Resolution: Power limitation (50%).

   - Clear Condition: I drops below specific thresholds.

- **Pulse Charge Current Exceeded** (Codes 25-27)

   - Trigger: I ≥ 105%, 120%, 125% of rated current.

   - Resolution: Power limitation (50% to 0%).

   - Clear Condition: I drops below specific thresholds.

- **Sustained Discharge Overcurrent** (Codes 105-107)

   - Trigger: I ≥ 105%, 120%, 125% of rated current.

   - Resolution: Power limitation (50%).

   - Clear Condition: I drops below specific thresholds.

### 4\. **Charging and Insulation-Related Alarms**

- **Battery SOC Low** (Codes 32-34)

   - Trigger: SOC ≤ 20%, 12%, 8%.

   - Resolution: Power limitation (50%).

   - Clear Condition: SOC rises above specific thresholds (e.g., > 22%).

- **SOC Too High** (Code 101)

   - Trigger: SOC > 100%.

   - Resolution: None specified.

   - Clear Condition: SOC ≤ 100%.

- **Insulation Resistance Low** (Codes 40-43)

   - Trigger: Resistance (R) ≤ specific values (e.g., 600Ω/V).

   - Resolution: Power limitation (50% to 0%).

   - Clear Condition: R rises above specified values (e.g., > 1100Ω/V).

- **Charging Overcurrent** (Code 74)

   - Trigger: Current exceeds the allowed charging current by certain thresholds.

   - Resolution: Stop charging.

   - Clear Condition: Current drops to normal levels.

### 5\. **Contactors and Internal Communication Alarms**

- **Contactor Failure to Close/Open** (Codes 49-58)

   - Trigger: Voltage difference across contactor is not within the expected range.

   - Resolution: Stop specific charging or request high voltage shutdown.

   - Clear Condition: Voltage difference returns to normal range.

- **Internal Communication Failure** (Code 45)

   - Trigger: Various internal communication faults (e.g., sensor failures).

   - Resolution: Limp mode, limit power to 0%.

   - Clear Condition: Fault conditions cleared internally.

### 6\. **Extreme Conditions and Emergency Alarms**

- **Battery Fire Alarm** (Code 21)

   - Trigger: Fire alarm flag set.

   - Resolution: Limit power to 0%, stop charging, disconnect contactors.

   - Clear Condition: Requires diagnosis tool or low voltage power reset.

- **Battery Self-Protection Fault** (Code 37)

   - Trigger: Extreme overvoltage, overtemperature, or undervoltage.

   - Resolution: Limit power to 0%, request high voltage shutdown.

   - Clear Condition: Requires specific conditions, such as tool reset.

### **General Notes:**

- **Reset Conditions:** Many faults require a specific action for reset (e.g., dropping below a threshold, use of diagnostic tools).

- **Power Limitations:** Actions taken often include limiting the vehicle's power output or stopping the charging process.

- **Communication:** Some codes involve one-way or two-way communication with thresholds for fault detection and recovery.

This structure provides a clear overview of the fault codes and associated actions, focusing on the most important information.