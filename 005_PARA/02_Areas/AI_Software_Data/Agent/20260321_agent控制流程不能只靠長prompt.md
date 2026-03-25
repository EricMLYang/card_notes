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