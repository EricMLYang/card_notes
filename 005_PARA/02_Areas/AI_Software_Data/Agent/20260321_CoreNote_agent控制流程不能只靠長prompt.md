---
process_level: 1  # [1.找重點  2.摘要  3.重新詮釋]
last_review: 2026-03-23
---

## [重點]
hook 能保證的是你有攔到的那些點，不是整個 agent 自動變聰明。
如果風險點沒被你定義成 hook，模型還是可能在別處漂移。這篇文章本身也沒有證明 steering 能解決所有類型的 agent failure。它只是證明在那個特定任務裡很有效。

## [摘要]


## [詮釋]


---
- Prompt engineering：快但會失控、長尾崩。  
  - SOP（自然語言流程文件，RFC2119 MUST/SHOULD/MAY）：更穩但 token 成本高。  
  - Workflow/graph：可預期但犧牲彈性，需求一偏離就卡死，圖越畫越脆。

- **實測結果（作者宣稱）**  
  在 600 次 evaluation 中：**Steering hooks 100% 通過率**；相比之下「簡單 prompt 指令」約 **82.5%**，「graph workflow」約 **80.8%**，且 steering 仍保留模型推理與適應能力。

這篇在推「代理可靠性」不要只靠長 prompt 或硬流程圖，而要用可測的 **攔截/校驗 hooks** 在工具呼叫與輸出階段做即時糾偏，讓行為控制從“文字許願”變成“可驗證規則”。

-- GPT 補充
這篇在講的核心，其實很清楚：

它在主張，**要讓 agent 可靠，不該只把規則塞進 prompt，也不該只靠固定 workflow/graph**。更好的做法，是在 agent 執行過程中的關鍵時點，加上可程式化、可測試的 **steering hooks**，去即時攔截、檢查、糾偏。([Strands Agents SDK][1])

更白話一點，它在對比三種控制方式：

第一種是 **prompt engineering**。
做法最快，原型很好用，但一旦規則變多，prompt 會越來越長，模型也可能忽略深藏的限制，導致長尾情境失控。原文直接把這件事描述成 prompting treadmill。([Strands Agents SDK][1])

第二種是 **SOP**。
也就是用自然語言寫成步驟文件，搭配 RFC 2119 那種 MUST / SHOULD / MAY 的規範字眼。它比一般 prompt 穩，因為程序講得更清楚；但代價是每次都要把整份 SOP 放進上下文，token 成本很高。Strands 與 AWS 相關說明都把 SOP 定位成可靠、但偏重的中間路線。([Strands Agents SDK][1])

第三種是 **workflow / graph**。
它把流程拆成節點與邊，行為比較可預期，但彈性會下降。只要使用者輸入不在預先設計的路徑裡，graph 就容易失敗，而且 edge case 越多，圖就越複雜、越脆。這正是原文拿來批評 graph 的重點。([Strands Agents SDK][1])

這篇真正想推的是第四種：**steering**。
Steering 的做法不是一開始把所有規則都講完，而是在 agent「快要做錯事的那一刻」才介入。原文說它主要有兩個攔截點：
一個是 **tool call 前**，先檢查工具名稱與參數；
另一個是 **model 回答後**，先檢查輸出格式、語氣或其他要求，不合格就丟回去重做。([Strands Agents SDK][1])

所以你摘錄的那句話：「把行為控制從文字許願變成可驗證規則」其實很接近原意。因為它強調 steering handler 可以寫成 **deterministic Python function**，能夠穩定重複執行，也能做 unit test。這代表某些規則不再只是“希望模型記得”，而是“真的在執行點被驗證”。([Strands Agents SDK][1])

你提到的那組數字，我也確認到了。
原文的確宣稱，在一個圖書館續借 agent 的測試裡，每個版本跑 6 個情境、每個情境 100 次，也就是每個 agent 600 次、總共 3,000 次 run。結果是：
Steering 100.0%、Simple instructions 82.5%、Workflow 80.8%、SOP 99.8%。同時，SOP 的平均 input tokens 約 9,879，而 Steering 約 3,346，原文因此主張 steering 在接近 SOP 的可靠性下，token 成本更低。([Strands Agents SDK][1])

不過這裡有一個很重要的補充：
**這些數據目前是作者自己的實驗結果，不是獨立第三方 benchmark。** 原文是 Strands 官方部落格，由 Strands/AWS 生態的人發表，測試案例也是作者自己設計的 library renewal agent。它有參考價值，但還不能把它當成跨框架、跨任務、跨模型都成立的普遍定律。([Strands Agents SDK][1])

另外，這篇其實也不是在說「prompt 完全沒用」或「workflow 完全不行」。
它比較像是在說：

* prompt 適合原型與簡單 agent
* SOP 適合要高可靠、但沒有 steering 能力的環境
* workflow 適合輸入變異小、流程明確的任務
* steering 適合你要保留模型推理彈性，但又有某些規則不能違反的情境 ([Strands Agents SDK][1])

從工程角度看，這篇最值得你注意的地方有三個。

第一，**它把控制點放在 agent loop 裡，而不是全壓在 prompt 前面**。
這和你平常在講的 harness / control loop 觀念很接近：不是單純把 instruction 寫更長，而是把檢查點放到「觀察、計畫、執行」的關鍵節點。這是 agent engineering 很典型的方向。原文也明確說 steering 是 just-in-time guidance。([Strands Agents SDK][1])

第二，**它把規則分層**。
文中提到 agent 內部可以用 steering handler 做流程與輸出糾偏，外部則可搭配 Amazon Bedrock AgentCore Policy Engine，在 gateway 層對工具呼叫做政策式限制。AWS 文件也說得很清楚，AgentCore Gateway 會把工具視為 action，並用 Cedar policy 在每次工具呼叫時做評估。這就是典型的 defense in depth。([Strands Agents SDK][1])

第三，**它在推一種比 graph 更局部、比 prompt 更可驗證的控制手法**。
這種方式的好處是，你不一定要把整個 agent 重寫成大圖，也不需要讓 prompt 越堆越長。你可以只針對高風險點加 rule，例如：

* 某工具必須先於另一工具
* 某參數必須來自前一步查到的真值
* 某種輸出格式一定要符合模板
* 某些語氣、合規、資安要求要過關才准回覆
  這一點和一般「只靠 system prompt 勸模型守規矩」差很多。([Strands Agents SDK][1])

但它也有邊界。

一個邊界是，**hook 能保證的是你有攔到的那些點，不是整個 agent 自動變聰明**。
如果風險點沒被你定義成 hook，模型還是可能在別處漂移。這篇文章本身也沒有證明 steering 能解決所有類型的 agent failure。它只是證明在那個特定任務裡很有效。([Strands Agents SDK][1])

另一個邊界是，**後驗檢查也會增加一些 token 與控制成本**。
原文數據裡 steering 的 input token 比 simple instructions 高，因為 agent 偏離時要收到額外 guidance 再重試。只是作者認為，這個成本比塞超長 SOP 或跑多節點 graph 還划算。([Strands Agents SDK][1])

如果用一句話幫你總結這篇：

**它在推的不是「把 agent 變成硬編排」，而是「在保留模型推理自由的前提下，把關鍵規則改成執行時可攔截、可校驗、可測試的控制點」。** 這也是為什麼它會拿 prompt、SOP、workflow 當對照組。([Strands Agents SDK][1])

如果你要把它帶回你自己的語境，我會這樣翻成你的工程語言：

**Prompt 是全局弱約束，SOP 是高成本全局強約束，workflow 是硬編排；steering hooks 則是 agent loop 內的局部強約束。**
它比較像在 agent 的 O/P/E 節點上放 guardrails，而不是把所有控制都前置成一大段文字。這個方向，跟你最近在想的 harness、context engineering、tool 約束，其實是同一條線。([Strands Agents SDK][1])

# BreadCards

## A. 主脈絡與個人映射
- 論證骨架：四種 agent 控制方式各有適用範圍——Prompt（弱、快、易失控）、SOP（強、貴、token 飽和）、Workflow/Graph（可預期、脆、邊際 case 卡死）、Steering Hooks（局部強、可測、保留推理彈性）。Strands 自家測試 600 trial 顯示 steering 100% / SOP 99.8% / prompt 82.5% / workflow 80.8%，且 token 成本只有 SOP 的 1/3。
- 挑戰的預設：「規則寫多一點 prompt 就會聽」「workflow 越完整越穩定」「multi-agent / graph 是上限解」。指出這些都會在 long-tail 失敗。
- 個人映射：對 D2D Architect / DecisionOps 主軸，這是把「驗證點」明確化的工具——把治理從「全局文字許願」改為「agent loop 內可驗證、可單元測試的程式」，正好對應 Anthropic 的 Policy as Code 與 production checklist。但要同時記住作者邊界：steering 只能保證你攔到的點，沒攔的還是會漂移；數據是作者自己的測試，不是第三方 benchmark。

## B. 候選卡（Lite）

序號 1
- 候選標題：四種 Agent 控制方式的適用矩陣（Prompt / SOP / Workflow / Steering）
- 分級：Core
- 類型：Pattern
- 核心內容：Prompt 適合原型與簡單 agent；SOP 適合要高可靠但沒有 hook 能力的環境；Workflow 適合輸入變異小、流程明確；Steering 適合要保留推理彈性但有些規則絕不能違反。不是替代而是分流——根據「規則明確度 × 輸入變異度 × 推理彈性需求」三軸選擇。
- 保留理由：給 Agent 控制方式的選型一個結構化判準，可直接寫進架構決策表。
- 待補強處：何時組合使用（如 SOP backbone + Steering hooks 補強）。
- 初步知識鉤子：Policy as Code、Workflow vs Agent、AI 治理分層。

序號 2
- 候選標題：Steering Hooks ＝ 在 agent loop 的兩個節點放可測試的 deterministic 守門人
- 分級：Core
- 類型：Pattern
- 核心內容：兩個攔截點：(1) tool call 前——檢查工具名稱與參數；(2) model 回答後——檢查格式 / 語氣 / 合規。Hook 是 deterministic Python function，能單元測試、能重複執行。把規則從「希望模型記得」變成「執行點被驗證」。是 12-Factor Agents 與 Anthropic Policy as Code 的具體實作。
- 保留理由：是把 Agent 治理「程式化」的最小可行單位。
- 待補強處：當規則需要 LLM 判斷（如「語氣是否合適」）時 hook 內要不要再叫一次 LLM。
- 初步知識鉤子：Pre-tool / Post-output gates、Policy as Code、Defense in Depth。

序號 3
- 候選標題：Steering 的邊界 — Hook 只能擋住你定義的點，沒攔的還是會漂移
- 分級：Core
- 類型：Warning
- 核心內容：作者明確自我設限：「hook 能保證的是你有攔到的那些點，不是整個 agent 自動變聰明。」如果風險點沒被定義成 hook，模型還是會在別處漂移。文章只證明在那個特定任務（圖書館續借 agent）有效，不能當跨框架、跨任務、跨模型的普遍定律。
- 保留理由：避免把 steering 當銀彈；提醒「風險點識別」才是真功夫。
- 待補強處：風險點識別的方法論——通常從哪裡找未被攔截的漂移（trace 分析？failure mode catalog？）。
- 初步知識鉤子：Anthropic eval saturation 警報、Failure-driven design、Threat Modeling for Agents。

序號 4
- 候選標題：作者實驗數據的解讀邊界 — 自家 benchmark 不能當定律
- 分級：Support
- 類型：Warning
- 核心內容：Strands/AWS 自家發表，library renewal agent 自己設計，每版 6 情境 × 100 次 = 600 trial（總 3000 trial）。Steering 100.0% / SOP 99.8% / Prompt 82.5% / Workflow 80.8%；input token Steering 約 3,346 vs SOP 約 9,879。有參考價值但不是第三方 benchmark——這是讀任何「廠商自家 best practice 文章」應有的預設懷疑。
- 保留理由：是「讀產業文章該有的審讀紀律」的範例卡。
- 待補強處：第三方獨立驗證 steering 的研究；跨任務類型的數據。
- 初步知識鉤子：Vendor benchmark bias、A/B with strawman、Reproducibility crisis。

序號 5
- 候選標題：分層治理 — Steering 在 agent 內，Policy Engine 在 gateway 層（Defense in Depth）
- 分級：Support
- 類型：Pattern
- 核心內容：原文同時提到 agent 內部用 steering hook 做流程與輸出糾偏，外部用 Amazon Bedrock AgentCore Policy Engine 在 gateway 層對工具呼叫做 Cedar policy 評估。這是 defense in depth——兩層獨立失敗才會有事故，比把所有規則塞進 prompt 安全得多。
- 保留理由：把治理從「單點防線」升級到「多層防線」的設計藍圖。
- 待補強處：兩層之間如何避免規則重複 / 衝突。
- 初步知識鉤子：Cedar Policy、AWS Shared Responsibility、Production Agent Guardrails。

## C. 建議送 refine 的項目
- 序號 1, 2, 3（最高優先：控制方式選型 + steering 機制 + 邊界警示是同一組三角）
- 序號 4, 5（中優先：補完讀文章紀律與多層防線）

## D. 呼叫 refine-cards
- 將上述 5 張候選卡交由 refine-cards 精煉。