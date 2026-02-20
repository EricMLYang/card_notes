---
tags:
  - vms
---
## Domain - Motor & Inverter

- what is Inverter: 

   - EV**Inverter (逆變器）**是關鍵元件之一，負責將電池所儲存的直流電（DC）轉換為驅動電動馬達所需的交流電（AC）。這個轉換過程是電動車能夠運行的核心，因為大多數電動馬達都是交流馬達，如交流感應馬達（AC induction motor）或永磁同步馬達（PMSM）

- Reference

   - Dashboard

      - [馬達狀態管理& 能耗管理 - Tesla](https://grafana.csselectronics.stellarhosted.com/d/yBc5x90nk3/css-playground-tesla?orgId=1&var-devices=3F78A21D&var-parameters=BMS_appCrc&var-parameters=BMS_appGitHash&var-parameters=DI_accelPedalPos&var-parameters=SteeringSpeed129&var-parameters=APP_environmentRainy&var-parameters=APP_environmentSnowy&var-parameters=BMS_acChargerKwhTotal&var-parameters=BMS_activeHeatingWorthwhile)

      - [馬達狀態管理& 能耗管理 -KIA](https://grafana.csselectronics.stellarhosted.com/d/yBc5x90nk2/css-playground-kia-ev6?orgId=1)

   - Diagnostics

      - **[Fault Detection and Diagnosis of the Electric Motor Drive and Battery System of Electric Vehicles](https://www.mdpi.com/2075-1702/11/7/713)**

      - **[Induction Motor Bearing Fault Diagnosis Based on Singular Value Decomposition of the Stator Current](https://www.mdpi.com/1996-1073/16/8/3303#:\~:text=Among%20the%20works%20analyzing%20IM,are%20caused%20by%20bearing%20breakdowns.)**

   - Range

      - **[To what degree does temperature impact EV range?](https://www.geotab.com/blog/ev-range/) **

      - **[Digging deeper into how temperature and speed impact EV range](https://www.geotab.com/blog/ev-range-impact-of-speed-and-temperature/)**

   - Efficient

      - [電動車馬達是什麼？體積小、效率高是永磁馬達被採用的關鍵，概念股一次看](https://www.sinotrade.com.tw/richclub/industry/-640eb372e0730b554092abf9)

      - [電動自行車：續航力與馬達效率 ( I )](https://vocus.cc/article/630eeb2cfd8978000160940c)



## **\[電動車馬達異常數據診斷\]：關鍵指標與全面檢測**

### 馬達安全：

- Motor Temperature: High temperatures can indicate motor overload or potential issues with cooling systems.

- Motor Current: This represents the flow of electrical current through the motor.

- Inverter Temperature: High temperatures can indicate stress or potential failure.

### 電氣數據

- **電壓數據**：監測電壓是否過高/低，確保電壓穩定，避免對馬達性能和效率產生負面影響

- **電流數據**：馬達運行時的電流大小，過高的電流可能表示負載過重或馬達內部故障，過低的電流則可能是控制系統問題

- **電流諧波數據**：分析電流波形的諧波成分，識別馬達或逆變器可能存在的問題，預防效率降低和壽命縮短。

- **絕緣電阻數據**：定期測量馬達繞組與外殼之間的絕緣電阻，及早發現絕緣劣化，防止短路等嚴重故障。

- **逆變器溫度**：監測逆變器的溫度，因為過熱可能直接影響馬達的運行效率和壽命，這也是電氣數據監控的關鍵之一。

### 機械數據

- **馬達轉速**：轉速變化，識別潛在的機械故障或控制系統問題

- **轉矩數據**：轉矩變化，評估馬達負載狀況，及時發現負載過重或馬達內部故障

- **振動數據**：檢測馬達振動水平，識別軸承磨損、對中不良等機械問題

- **軸承溫度**：監測軸承溫度以評估其運行狀況，過高的溫度可能預示磨損或潤滑不足

### 熱數據

- **溫度分布數據**：監測馬達各部位（定子繞組、轉子、軸承等）的溫度分布，發現局部過熱或冷卻問題

- **冷卻系統性能**：若馬達配有冷卻系統，監控冷卻液的流量和溫度，以評估冷卻系統的運行效率並預防過熱情況

### 效率與歷史數據

- **效率數據**：持續監控馬達運行效率，及時發現故障或維護需求。

- **故障記錄與歷史數據**：分析過去的故障記錄和運行數據，結合機器學習等方法，建立馬達健康模型，預測未來故障風險，實現預防性維護。

- **負載歷史**：追蹤馬達的歷史負載情況，有助於了解馬達長期運行壓力，為未來風險預測提供有力數據支持。

### 環境與運行數據

- **環境數據**：考慮環境因素（溫度、濕度、海拔等）對馬達運行的影響，輔助解釋異常並調整診斷策略。

- **車輛運行數據**：結合車輛的行駛速度、加速度、電池狀態等數據，更全面地評估馬達的工作狀態，發現與特定工況相關的異常。

- **路況數據**：考慮道路情況（如坡度、道路類型）對馬達負載的影響，協助分析特定運行工況下的異常。



## \[關鍵指標\]

### **1\. 剩餘續航里程 (Remaining Range)**

- **原因**: 剩餘續航里程是電動車使用者最關心的指標之一，因為它直接影響他們的行駛計劃和充電策略。預測未來的續航里程可以幫助使用者及時規劃充電，降低里程焦慮

- **可用數據**: 能源消耗 (DC_Current_OUT、APC_Current_OUT)、車速 (VehSpd)、電動機扭矩 (Motor_Torque)

### **2\. 電池能耗率 (Energy Consumption Rate)**

- **原因**: 能耗率影響續航里程和運營成本，是車主和車隊管理者關注的焦點

- 每公里能耗（Wh/km）,  每百公里能耗（kWh/100km）,  每公里電量消耗時間（Wh/min/km）

- **可用數據**: 能源消耗 (DC_Current_OUT、APC_Current_OUT)、車速 (VehSpd)、電動機轉速 (Motor_Speed) 等

### **3\. 馬達溫度 (Motor Temperature)**

- **原因**: 馬達溫度過高可能導致性能下降，甚至損壞。預測馬達溫度的變化有助於預防故障，確保馬達穩定運行。這對於車主和車輛維護人員來說非常重要

- **可用數據**: 電動機溫度 (TS4_Motor_Temp)、電動機轉速 (Motor_Speed)、電動機扭矩 (Motor_Torque)、MCU 溫度 (TS4_MCU_Temp)

### **4\.** Rated range

 電動車在理想條件下，單次充滿電後所能行駛的最遠距離。它是根據標準化測試得出的，因此可以作為一個參考指標，但實際行駛里程可能會因各種因素而有所不同, 包括：

- **溫度：** 低溫和高溫都會影響電池性能和輔助系統的能耗，從而降低續航里程。

- **駕駛習慣：** 急加速、急煞車、高速行駛都會增加能耗，縮短續航里程。

- **路況與地形：** 上坡、塞車、崎嶇路面等都會增加能耗，影響續航里程。

- **車輛負載：** 載重越多，能耗越高，續航里程越短。

- **氣候條件：** 使用空調或暖氣會增加能耗，降低續航里程。

- **車輛狀況：** 輪胎胎壓、車輛保養狀況等都會影響能耗和續航里程。

- **電池老化：** 隨著電池使用時間的增加，其容量和性能會逐漸下降，導致續航里程縮短。

### 5\. 馬達效率:  ( 角速度 \* 轉矩 )   /   (V  \*  I )

- **輸入電壓（V）**

   - **範圍：** 200V - 800V（直流電壓，視電動車的電池系統而定）

   - **說明：** 大多數電動車使用高電壓電池系統。普通乘用電動車通常採用約 400V 的系統，而高性能或長續航的電動車則可能採用 800V 系統，以提高充電速度和效率。

- **輸入電流（I）**

   - **範圍：** 50A - 500A（在不同運行狀態下變動）

   - **說明：** 電流的範圍取決於車輛的加速、負載情況和運行條件。在高負載或加速時，電流會較高，反之則較低。大型電動車（如電動卡車或巴士）的電流會更大。

- **轉速（RPM，Revolutions Per Minute）**

   - **範圍：** 0 - 20,000 RPM（通常情況）

   - **說明：** 電動車馬達的轉速範圍很廣，具備快速起步和高速運行的能力。大部分電動車的馬達在最高效率時的轉速約在 5,000 - 10,000 RPM 左右，而在極端運行情況下，某些馬達可達到 20,000 RPM。

- **轉矩（Torque，τ）**

   - **範圍：** 50 Nm - 400 Nm（視馬達類型和車型而定）

   - **說明：** 乘用車的電動馬達轉矩通常在 50 Nm - 300 Nm 之間，電動卡車或巴士等大型車輛的轉矩會更高，甚至可達到 400 Nm 以上。電動車馬達通常在低轉速時能提供最大轉矩，這也是電動車擁有強勁起步加速能力的原因。



## \[ Dashboard Design \]

### **電動車綜合監控儀表板設計**

聚焦於「續航與能效監控」以及「馬達與逆變器診斷」兩大核心模塊。此儀表板旨在即時呈現關鍵數據、預測重要指標，並展示相關特徵的歷史趨勢，幫助客戶全面掌握車輛狀態，優化運營決策。

---

### **儀表板佈局概覽**

1. **頂部橫幅**

   - **標題**: 電動車綜合監控儀表板

   - **日期與時間**: 實時更新，顯示當前數據截取時間

   - **車輛識別**: 車輛ID或名稱

2. **主要分區**

   - **左側區塊**: 續航與能效監控

   - **右側區塊**: 馬達與逆變器診斷

3. **底部區塊**

   - **歷史數據趨勢圖**

   - **預測指標展示**

---

### **1\. 續航與能效監控**

#### **1\.1 能源消耗面板**

- **DC_Current_OUT**

   - **視覺化**: 實時圓形儀表

   - **顏色指示**: 綠色（正常）、黃色（警告）、紅色（異常）

- **APC_Current_OUT**

   - **視覺化**: 條形圖

- **Motor_Torque**

   - **視覺化**: 實時扭矩儀表

#### **1\.2 車速與動力輸出面板**

- **VehSpd（車速）**

   - **視覺化**: 仿真速度計

- **Motor_Speed（電動機轉速）**

   - **視覺化**: 折線圖，顯示過去1小時的轉速變化

#### **1\.3 效率參數**

- **總能耗與動力輸出比率**

   - **視覺化**: 動態指標顯示，附帶歷史趨勢折線圖

   - **顏色編碼**: 綠色（高效）、黃色（中等）、紅色（低效）

#### **1\.4 剩餘續航里程預測**

- **預測範圍**: 根據當前能耗和駕駛模式，預測未來50公里的續航

   - **視覺化**: 圓形儀表，顯示預測里程，並用顏色區分範圍狀態（綠色、高；黃色、中；紅色、低）

---

### **2\. 馬達與逆變器診斷**

#### **2\.1 馬達狀態面板**

- **MCU_Sta（MCU 狀態）**

   - **視覺化**: 指示燈（綠色：正常，黃色：警告，紅色：故障）

- **McuRunmodeSts（MCU 運行模式狀態）**

   - **視覺化**: 圖標或標籤顯示當前運行模式（如運行、待機、故障）

#### **2\.2 馬達轉速與扭矩**

- **Motor_Speed（電動機轉速）**

   - **視覺化**: 與續航面板共享折線圖，保持數據一致性

- **Motor_Torque（電動機扭矩）**

   - **視覺化**: 與能源消耗面板共享實時扭矩儀表

#### **2\.3 溫度監控**

- **TS4_MCU_Temp（MCU 溫度）**

   - **視覺化**: 溫度計圖示，顯示實時溫度

- **TS4_Motor_Temp（電動機溫度）**

   - **視覺化**: 溫度計圖示

   - **顏色指示**: 正常（藍色）、警告（橙色）、危險（紅色）

#### **2\.4 故障診斷面板**

- **MCU_DTC_Code（MCU 故障診斷碼）**

   - **視覺化**: 故障碼列表，包含故障描述和時間戳

- **MCU_ErrLevel（MCU 故障等級）**

   - **視覺化**: 圖標顯示故障嚴重程度（低、中、高）

#### **2\.5 逆變器狀態**

- **IGBT_Enable（IGBT 啟動狀態）**

   - **視覺化**: 切換式指示燈（ON/OFF）

---

### **3\. 歷史數據與預測指標**

#### **3\.1 歷史數據趨勢圖**

- **內容**: 展示過去24小時內的主要指標變化，如車速、能耗、馬達溫度等

- **視覺化**: 多重折線圖，支持用戶選擇查看不同時間範圍

#### **3\.2 預測指標展示**

- **剩餘續航里程預測**

   - **模型**: LSTM

   - **視覺化**: 預測趨勢線與實際數據對比圖

- **電池能耗率預測**

   - **模型**: Seasonal ARIMA

   - **視覺化**: 預測趨勢圖

- **馬達溫度預測**

   - **模型**: Prophet

   - **視覺化**: 預測溫度曲線，顯示未來一小時的溫度變化

---

### **4\. 附加功能**

#### **4\.1 數據過濾與篩選**

- **選項**: 按時間範圍（如過去24小時、過去一週）

- **用途**: 允許用戶查看特定時間段內的數據，進行更詳細的分析

#### **4\.2 警報系統**

- **功能**: 異常數據自動觸發警報，如能耗過高、溫度超標、馬達故障等

- **視覺化**: 顯示在儀表板顯著位置，並以彈窗或通知形式提醒用戶

#### **4\.3 預測模型整合**

- **功能**: 根據歷史數據和當前狀態，實時更新預測指標

- **用途**: 幫助用戶提前採取行動，如安排充電或進行維護

---

### **視覺化設計建議**

- **一致性**: 使用統一的色彩和圖表風格，提升可讀性和專業感

- **互動性**: 支持用戶點擊圖表查看詳細信息，或通過滑鼠懸停顯示數據點

- **響應式設計**: 確保儀表板在不同設備上（如桌面、平板、手機）均能良好顯示

- **色彩編碼**: 使用顏色區分不同狀態，綠色表示正常，黃色表示警告，紅色表示異常

---

### **客戶簡報要點**

1. **儀表板目標**

   - 提供全面的電動車性能監控

   - 即時呈現關鍵數據，支持預測分析

   - 幫助優化車輛運營，提升用戶體驗

2. **主要功能展示**

   - 續航與能效實時監控

   - 馬達與逆變器健康診斷

   - 歷史數據趨勢與預測指標

3. **技術優勢**

   - 採用先進的時間序列模型進行預測

   - 高度互動和可定制的視覺化界面

   - 實時警報系統，保障車輛安全

4. **客戶收益**

   - 降低運營成本，提升能源效率

   - 提前識別並解決車輛潛在問題

   - 增強用戶對車輛性能的掌控感





## \[ Dashboard Code \]

以下是使用 Python 的 Dash 和 Plotly 庫創建的電動車綜合監控儀表板程式碼。該儀表板包含「續航與能效監控」和「馬達與逆變器診斷」兩個主要部分，使用藍色系的科技風配色，並生成了盡量真實的假設數據。

```python
import dash
from dash import dcc, html, dash_table
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 創建假設數據
np.random.seed(42)  # 為了使結果可重複

# 時間序列
time_series = pd.date_range(end=datetime.now(), periods=100, freq='T')

# 生成假設數據
data = pd.DataFrame({
    'Time': time_series,
    'DC_Current_OUT': np.random.normal(loc=100, scale=10, size=100),
    'APC_Current_OUT': np.random.normal(loc=50, scale=5, size=100),
    'Motor_Torque': np.random.normal(loc=200, scale=20, size=100),
    'VehSpd': np.random.normal(loc=60, scale=5, size=100),
    'Motor_Speed': np.random.normal(loc=3000, scale=300, size=100),
    'TS4_MCU_Temp': np.random.normal(loc=75, scale=5, size=100),
    'TS4_Motor_Temp': np.random.normal(loc=80, scale=5, size=100),
    'MCU_DTC_Code': np.random.choice(['0', 'P1234', 'P5678'], size=100, p=[0.9, 0.05, 0.05]),
    'MCU_ErrLevel': np.random.choice(['Low', 'Medium', 'High'], size=100, p=[0.9, 0.05, 0.05]),
    'IGBT_Enable': np.random.choice([True, False], size=100, p=[0.95, 0.05])
})

# 計算效率參數
data['Efficiency_Ratio'] = (data['VehSpd'] * data['Motor_Torque']) / (data['DC_Current_OUT'] + data['APC_Current_OUT'])

# 創建Dash應用
app = dash.Dash(__name__)

# 設定外觀主題
colors = {
    'background': '#0F0F0F',
    'text': '#FFFFFF',
    'grid': '#2A2A2A',
    'blue': '#1E90FF'
}

app.layout = html.Div(style={'backgroundColor': colors['background'], 'color': colors['text'], 'font-family': 'Arial'}, children=[
    html.H1('電動車綜合監控儀表板', style={'textAlign': 'center', 'color': colors['text']}),
    html.Div([
        html.Div([
            # 續航與能效監控
            html.H2('續航與能效監控', style={'color': colors['blue']}),
            html.Div([
                # DC_Current_OUT
                dcc.Graph(
                    id='dc-current-out',
                    figure={
                        'data': [go.Indicator(
                            mode="gauge+number",
                            value=data['DC_Current_OUT'].iloc[-1],
                            title={'text': "DC Current OUT (A)"},
                            gauge={'axis': {'range': [0, 150]},
                                   'bar': {'color': colors['blue']},
                                   'bgcolor': colors['grid'],
                                   'borderwidth': 2,
                                   'bordercolor': colors['grid'],
                                   'steps': [
                                       {'range': [0, 100], 'color': "#3D9970"},
                                       {'range': [100, 125], 'color': "#FF851B"},
                                       {'range': [125, 150], 'color': "#FF4136"},
                                   ]},
                            number={'font': {'color': colors['text']}}
                        )],
                        'layout': go.Layout(
                            paper_bgcolor=colors['background'],
                            font={'color': colors['text']},
                            margin={'t': 50, 'b': 0}
                        )
                    }
                ),
                # APC_Current_OUT
                dcc.Graph(
                    id='apc-current-out',
                    figure={
                        'data': [go.Indicator(
                            mode="gauge+number",
                            value=data['APC_Current_OUT'].iloc[-1],
                            title={'text': "APC Current OUT (A)"},
                            gauge={'axis': {'range': [0, 75]},
                                   'bar': {'color': colors['blue']},
                                   'bgcolor': colors['grid'],
                                   'borderwidth': 2,
                                   'bordercolor': colors['grid'],
                                   'steps': [
                                       {'range': [0, 50], 'color': "#3D9970"},
                                       {'range': [50, 65], 'color': "#FF851B"},
                                       {'range': [65, 75], 'color': "#FF4136"},
                                   ]},
                            number={'font': {'color': colors['text']}}
                        )],
                        'layout': go.Layout(
                            paper_bgcolor=colors['background'],
                            font={'color': colors['text']},
                            margin={'t': 50, 'b': 0}
                        )
                    }
                ),
                # Motor_Torque
                dcc.Graph(
                    id='motor-torque',
                    figure={
                        'data': [go.Indicator(
                            mode="gauge+number",
                            value=data['Motor_Torque'].iloc[-1],
                            title={'text': "Motor Torque (Nm)"},
                            gauge={'axis': {'range': [0, 300]},
                                   'bar': {'color': colors['blue']},
                                   'bgcolor': colors['grid'],
                                   'borderwidth': 2,
                                   'bordercolor': colors['grid'],
                                   'steps': [
                                       {'range': [0, 200], 'color': "#3D9970"},
                                       {'range': [200, 250], 'color': "#FF851B"},
                                       {'range': [250, 300], 'color': "#FF4136"},
                                   ]},
                            number={'font': {'color': colors['text']}}
                        )],
                        'layout': go.Layout(
                            paper_bgcolor=colors['background'],
                            font={'color': colors['text']},
                            margin={'t': 50, 'b': 0}
                        )
                    }
                )
            ], style={'display': 'flex', 'justify-content': 'space-around'}),
            html.Div([
                # Vehicle Speed
                dcc.Graph(
                    id='vehicle-speed',
                    figure={
                        'data': [go.Indicator(
                            mode="gauge+number",
                            value=data['VehSpd'].iloc[-1],
                            title={'text': "Vehicle Speed (km/h)"},
                            gauge={'axis': {'range': [0, 120]},
                                   'bar': {'color': colors['blue']},
                                   'bgcolor': colors['grid'],
                                   'borderwidth': 2,
                                   'bordercolor': colors['grid']},
                            number={'font': {'color': colors['text']}}
                        )],
                        'layout': go.Layout(
                            paper_bgcolor=colors['background'],
                            font={'color': colors['text']},
                            margin={'t': 50, 'b': 0}
                        )
                    }
                ),
                # Motor Speed
                dcc.Graph(
                    id='motor-speed',
                    figure={
                        'data': [go.Scatter(
                            x=data['Time'],
                            y=data['Motor_Speed'],
                            mode='lines',
                            line={'color': colors['blue']},
                            name='Motor Speed (RPM)'
                        )],
                        'layout': go.Layout(
                            title='Motor Speed (RPM)',
                            paper_bgcolor=colors['background'],
                            plot_bgcolor=colors['background'],
                            xaxis={'title': 'Time', 'gridcolor': colors['grid'], 'color': colors['text']},
                            yaxis={'gridcolor': colors['grid'], 'color': colors['text']},
                            font={'color': colors['text']},
                            margin={'t': 50}
                        )
                    }
                )
            ], style={'display': 'flex', 'justify-content': 'space-around'})
        ], className='six columns'),
        html.Div([
            # 馬達與逆變器診斷
            html.H2('馬達與逆變器診斷', style={'color': colors['blue']}),
            html.Div([
                # MCU Status
                html.Div([
                    html.H4('MCU 狀態', style={'color': colors['text']}),
                    html.Div('正常', style={'color': '#3D9970', 'fontSize': 24})  # 假設為正常狀態
                ], style={'textAlign': 'center', 'padding': '20px'}),
                # MCU Run Mode Status
                html.Div([
                    html.H4('MCU 運行模式狀態', style={'color': colors['text']}),
                    html.Div('運行中', style={'color': '#3D9970', 'fontSize': 24})  # 假設為運行中
                ], style={'textAlign': 'center', 'padding': '20px'}),
            ], style={'display': 'flex', 'justify-content': 'space-around'}),
            html.Div([
                # Motor Temperature
                dcc.Graph(
                    id='motor-temp',
                    figure={
                        'data': [go.Scatter(
                            x=data['Time'],
                            y=data['TS4_Motor_Temp'],
                            mode='lines',
                            line={'color': colors['blue']},
                            name='Motor Temperature (°C)'
                        )],
                        'layout': go.Layout(
                            title='Motor Temperature (°C)',
                            paper_bgcolor=colors['background'],
                            plot_bgcolor=colors['background'],
                            xaxis={'title': 'Time', 'gridcolor': colors['grid'], 'color': colors['text']},
                            yaxis={'gridcolor': colors['grid'], 'color': colors['text']},
                            font={'color': colors['text']},
                            margin={'t': 50}
                        )
                    }
                ),
                # MCU Temperature
                dcc.Graph(
                    id='mcu-temp',
                    figure={
                        'data': [go.Scatter(
                            x=data['Time'],
                            y=data['TS4_MCU_Temp'],
                            mode='lines',
                            line={'color': colors['blue']},
                            name='MCU Temperature (°C)'
                        )],
                        'layout': go.Layout(
                            title='MCU Temperature (°C)',
                            paper_bgcolor=colors['background'],
                            plot_bgcolor=colors['background'],
                            xaxis={'title': 'Time', 'gridcolor': colors['grid'], 'color': colors['text']},
                            yaxis={'gridcolor': colors['grid'], 'color': colors['text']},
                            font={'color': colors['text']},
                            margin={'t': 50}
                        )
                    }
                )
            ], style={'display': 'flex', 'justify-content': 'space-around'}),
            html.Div([
                # Fault Diagnosis
                html.H4('故障診斷碼', style={'color': colors['text'], 'textAlign': 'center'}),
                dash_table.DataTable(
                    id='fault-codes',
                    columns=[
                        {'name': 'Time', 'id': 'Time', 'type': 'datetime'},
                        {'name': 'DTC Code', 'id': 'MCU_DTC_Code'},
                        {'name': 'Error Level', 'id': 'MCU_ErrLevel'}
                    ],
                    data=data[data['MCU_DTC_Code'] != '0'][['Time', 'MCU_DTC_Code', 'MCU_ErrLevel']].to_dict('records'),
                    style_table={'maxHeight': '300px', 'overflowY': 'auto'},
                    style_cell={'backgroundColor': colors['background'], 'color': colors['text'], 'textAlign': 'center'},
                    style_header={'backgroundColor': colors['grid'], 'fontWeight': 'bold', 'color': colors['text']}
                )
            ], style={'padding': '20px'})
        ], className='six columns')
    ], className='row'),
    html.Div([
        # 效率參數
        html.H2('效率參數', style={'color': colors['blue'], 'textAlign': 'center'}),
        dcc.Graph(
            id='efficiency-ratio',
            figure={
                'data': [go.Scatter(
                    x=data['Time'],
                    y=data['Efficiency_Ratio'],
                    mode='lines',
                    line={'color': colors['blue']},
                    name='Efficiency Ratio'
                )],
                'layout': go.Layout(
                    title='總能耗與動力輸出比率',
                    paper_bgcolor=colors['background'],
                    plot_bgcolor=colors['background'],
                    xaxis={'title': 'Time', 'gridcolor': colors['grid'], 'color': colors['text']},
                    yaxis={'gridcolor': colors['grid'], 'color': colors['text']},
                    font={'color': colors['text']},
                    margin={'t': 50}
                )
            }
        )
    ], style={'padding': '20px'}),
    html.Div([
        # 剩餘續航里程預測（假設模型）
        html.H2('剩餘續航里程預測', style={'color': colors['blue'], 'textAlign': 'center'}),
        dcc.Graph(
            id='range-prediction',
            figure={
                'data': [go.Indicator(
                    mode="gauge+number",
                    value=250,  # 假設預測剩餘續航里程為250公里
                    title={'text': "預測剩餘續航里程 (km)"},
                    gauge={'axis': {'range': [0, 500]},
                           'bar': {'color': colors['blue']},
                           'bgcolor': colors['grid'],
                           'borderwidth': 2,
                           'bordercolor': colors['grid'],
                           'steps': [
                               {'range': [0, 150], 'color': "#FF4136"},
                               {'range': [150, 300], 'color': "#FF851B"},
                               {'range': [300, 500], 'color': "#3D9970"},
                           ]},
                    number={'font': {'color': colors['text']}}
                )],
                'layout': go.Layout(
                    paper_bgcolor=colors['background'],
                    font={'color': colors['text']},
                    margin={'t': 50}
                )
            }
        )
    ], style={'padding': '20px'})
])

if __name__ == '__main__':
    app.run_server(debug=False)

```



### **說明**

- **假設數據生成**：使用 `numpy` 和 `pandas` 生成假設的電動車運行數據，包括時間序列和各項指標的值。為了增加真實性，使用了實際可能的範圍和分佈。

   - **DC_Current_OUT** 和 **APC_Current_OUT**：模擬電流輸出，分別以 100A 和 50A 為均值。

   - **Motor_Torque**：以 200 Nm 為均值，模擬電動機扭矩。

   - **VehSpd**：以 60 km/h 為均值，模擬車速。

   - **Motor_Speed**：以 3000 RPM 為均值，模擬電動機轉速。

   - **TS4_MCU_Temp** 和 **TS4_Motor_Temp**：模擬溫度，以 75°C 和 80°C 為均值。

   - **MCU_DTC_Code** 和 **MCU_ErrLevel**：模擬故障診斷碼和故障等級，主要為正常狀態，少部分為故障。

   - **IGBT_Enable**：模擬 IGBT 啟動狀態，大部分時間為啟動。