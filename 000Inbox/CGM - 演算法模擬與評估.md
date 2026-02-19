---
tags:
  - charging-master
---
# CGM - 演算法模擬與評估

- 目標： 期望模擬變成一個有價值的服務

   - 方便模擬的機制 ( 產生期望案例 input 檔)

   - 自動跑多個演算法

   - 評分機制

![image 130.png](./CGM%20-%20演算法模擬與評估-assets/image%20130.png)

![image 131.png](./CGM%20-%20演算法模擬與評估-assets/image%20131.png)

**核心流程:**

1. **輸入讀取：**

   - 讀取 **Input JSON** 檔案，獲取模擬情境的基礎設定。

      - **關鍵資訊：** 巴士清單、各巴士初始電量 (SoC %)、目標電量 (SoC %)、電池容量 (kWh)、可用充電時段、充電站契約容量上限 (kW 或 kVA)、單一充電樁/巴士功率上下限 (kW) 等。*(建議明確列出所有 Input 包含的關鍵欄位)*

   - 讀取對應的 **Output JSON** 檔案，獲取演算法產出的充電排程。

      - **關鍵資訊：** 針對**每一台**巴士 (`plateNumber`)，提供一系列時間點 (`startPeriod`，單位：秒) 及其對應的建議充電功率 (`limit`，單位：W)。*(需確認 Output 格式是單一檔案包含所有巴士，還是每台巴士一個檔案)*

2. **情境生成 (可選但建議)：**

   - 基於基礎 Input JSON，透過**參數化隨機**的方式，生成多個不同的測試情境 Input 檔案。

   - **可變參數範例：**

      - 初始電量在特定範圍內浮動 (e.g., 20%-40%)。

      - 目標電量變動 (e.g., 固定 95% 或在 90%-100% 之間)。

      - 契約容量調整 (e.g., 降低 10%、20%)。

      - 可用充電時段縮短或變動。

      - 巴士數量增減。

   - **存放位置：** 按照不同客戶或情境類型分類存放 (e.g., `simulation_case/客戶A/隨機情境1.json`, `simulation_case/客戶A/隨機情境2.json`)。

3. **演算法執行 (整合點)：**

   - 針對每一個生成的 Input JSON 檔案，**呼叫**充電排程演算法。*(需要定義如何觸發演算法，是執行檔？API？或其他形式？)*

   - 演算法根據 Input 產生對應的 Output JSON 檔案。

4. **結果評估與分析：**

   - 針對**每一組** (Input JSON, Output JSON) 進行處理。

   - **核心評估指標 (KPIs) - 需要明確定義：**

      - **目標達成率：**

         - 有多少比例的巴士在指定的充電結束時間前達到了目標電量？

         - 未達標的巴士，最終電量與目標電量的差距是多少？

      - **契約容量合規性：**

         - 在任何時間點，所有同時充電巴士的總功率是否超過契約容量上限？

         - 如果超約，超約的頻率、持續時間、最大超約量是多少？

      - **功率限制合規性：**

         - 每台巴士的充電功率是否始終在其功率上下限範圍內？

      - **充電效率/成本 (進階)：**

         - 總耗電量是多少？

         - 若有不同時段電價，總充電成本是多少？

         - 平均充電功率？功率曲線的平滑度？(避免頻繁啟停或劇烈波動)

   - **數據處理：**

      - 計算上述 KPIs 的量化數值。

      - 將時間序列的充電功率數據整理成方便繪圖的格式。

5. **報告產出：**

   - 彙整所有測試情境的評估結果。

   - 產生一份**綜合報告**，包含：

      - **總體摘要：** 所有情境的平均表現、最優/最差情境等。

      - **各情境詳情：** 每個 (Input, Output) 配對的詳細 KPIs 評分。

      - **視覺化圖表：**

         - 總功率隨時間變化圖 (與契約容量對比)。

         - 單一/多巴士電量 (SoC) 隨時間變化圖。

         - (可能) 其他 KPI 的分佈圖或比較圖。







# 巴士充電排程模擬程式使用說明

## 1\. 概述

此程式提供一個完整的流程，用於生成不同巴士充電情境的測試案例，執行充電排程演算法，並將結果與輸入檔案配對以供後續評估。整體流程包括情境生成、演算法執行和結果處理三個主要步驟。

## 2\. 主要組件

- **SimulationCase**: 管理多個相關情境的類別

- **SimulationScenario**: 負責生成和修改單一充電情境的類別

- **情境生成函數**: 各種預設情境的生成器（標準、高需求、有限容量等）

- **run_algorithm**: 執行演算法並處理結果檔案

- **run_all_simulations**: 批量執行多個情境並收集結果

## 3\. 使用流程

### 步驟一：生成模擬情境

1. 載入基礎輸入資料模板

2. 定義不同類型的模擬案例（可依客戶或情境類型分類）

3. 為每個案例生成多個情境

4. 將情境保存為JSON檔案

```python
# 建立模擬案例
standard_case = SimulationCase("大南客運_標準情境")

# 添加情境
standard_case.add_scenario(generate_standard_scenario(base_input_data))
standard_case.add_scenario(generate_high_demand_scenario(base_input_data))

# 生成JSON檔案
standard_case.generate_all_json("simulation_case/大南客運/標準")
```

### 步驟二：執行演算法

1. 針對生成的每個情境執行充電排程演算法

2. 演算法會產生result.json檔案

3. 結果檔案會被重命名並移動到與輸入檔案相同的資料夾

```python
# 執行單一情境
stdout, stderr, exec_time, result_path = run_algorithm(
    "path/to/algorithm.py", 
    "simulation_case/大南客運/標準/大南客運_標準情境_scenario_0.json"
)

# 批量執行所有情境
results = run_all_simulations("path/to/algorithm.py", "simulation_case")
```

### 步驟三：結果處理與評估

1. 結果檔案已重命名並與輸入檔案配對

2. 可依需求進行後續評估和分析

3. 可查看執行摘要統計

## 4\. 預設情境類型

1. **標準情境**: 使用預設設定的基本案例

2. **高需求情境**: 大量巴士（20台）同時需要充電

3. **有限容量情境**: 充電站契約容量有限（400kW）

4. **緊湊排程情境**: 充電時段有限（僅上午8點至中午12點）

5. **混合車隊情境**: 包含不同類型和電池容量的巴士

6. **優先級情境**: 巴士具有不同充電優先級

7. **夜間充電情境**: 僅限夜間充電

8. **隨機情境**: 完全隨機化的設定

## 5\. 檔案組織結構

```
simulation_case/
├── 客戶A/
│   ├── 標準/
│   │   ├── 客戶A_標準情境_scenario_0.json
│   │   ├── 客戶A_標準情境_scenario_1.json
│   │   └── output_客戶A_標準情境_scenario_0.json (結果)
│   ├── 特殊/
│   └── 隨機/
├── 客戶B/
└── 客戶C/
```

## 6\. 注意事項

- 演算法應接受輸入檔案路徑作為參數

- 演算法執行後應在當前目錄產生result.json檔案

- 所有參數（如充電站契約容量、巴士數量等）都可以在情境生成時自定義

- 結果檔案會自動重命名為與輸入檔案關聯的名稱（如output\_情境名稱.json）

## 7\. 快速開始範例

```python
# 從模板生成模擬情境
with open('input_template.json', 'r') as f:
    base_input_data = json.load(f)

# 建立各種情境
case = SimulationCase("測試案例")
case.add_scenario(generate_standard_scenario(base_input_data))
case.add_scenario(generate_high_demand_scenario(base_input_data))
case.generate_all_json("simulation_case/測試")

# 執行所有情境並處理結果
results = run_all_simulations("algorithm.py", "simulation_case")

# 檢視結果摘要
print(f"總共執行情境: {len(results)}")
print(f"成功執行: {sum(1 for r in results if r['success'])}")
```

此流程可以幫助您系統性地評估充電排程演算法在各種情況下的表現，並方便後續進行詳細分析。