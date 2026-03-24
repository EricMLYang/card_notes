---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-23
---

## [重點]
請貼上你認為的重點

## [摘要]


## [詮釋]


---
- Prompt engineering：快但會失控、長尾崩。  
  - SOP（自然語言流程文件，RFC2119 MUST/SHOULD/MAY）：更穩但 token 成本高。  
  - Workflow/graph：可預期但犧牲彈性，需求一偏離就卡死，圖越畫越脆。

- **實測結果（作者宣稱）**  
  在 600 次 evaluation 中：**Steering hooks 100% 通過率**；相比之下「簡單 prompt 指令」約 **82.5%**，「graph workflow」約 **80.8%**，且 steering 仍保留模型推理與適應能力。

這篇在推「代理可靠性」不要只靠長 prompt 或硬流程圖，而要用可測的 **攔截/校驗 hooks** 在工具呼叫與輸出階段做即時糾偏，讓行為控制從“文字許願”變成“可驗證規則”。