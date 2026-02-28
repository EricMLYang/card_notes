# 4-測試套件是 Agentic Engineering 的核心槓桿點

**類型**：Leverage

## 概念

「The single biggest differentiator between agentic engineering and vibe coding is testing.」

**機制**：
- 有完善測試套件 → AI Agent 可在迴圈中迭代直到測試通過 → 你對結果有高信心 → 你能安心委派更多任務。
- 無測試套件 → AI 會愉快地宣告「完成」在 broken code 上 → 你只能手動驗證每個輸出 → 速度優勢消失。

測試不只是品質保證，而是「將不可靠 agent 轉成可靠系統」的機制。它讓 AI 從「產生垃圾需要你判斷」變成「自我迭代直到正確」。

**實務建議**：在引入 AI 之前，先建立測試文化與 CI 流程。AI 不是「讓你可以跳過測試」，而是「讓測試變得更重要」。

## 重要性

讓你知道在 AI 協作中，測試不是成本而是槓桿。一個好的測試套件可以讓你放心將重複性實現工作委派給 AI，自己專注於架構與邊界案例。

## 邊界/反例

測試套件本身的品質至關重要。若你的測試只覆蓋 happy path，AI 會過度自信地通過測試但在 edge case 失敗。若測試寫得太脆弱（過度依賴實現細節），AI 每次重構都會打破測試，反而增加負擔。

## 標籤

#測試 #AgenticEngineering #槓桿 #TDD #CI
