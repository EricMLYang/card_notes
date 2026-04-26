# Production Agent 失靈是慢性失能而非急性故障

- 狀態：WEAK KEEP
- 類型：Warning
- 分類：10-
- 索引：010_CardNotes/01_Index/10_testing_operations_and_reliability.md
- 來源：005_PARA/02_Areas/AI_Software_Data/AI_Coding/01_inbox/20260401_從HarnessEng看skills的原子性.md（#1）

## 核心命題
Agent 不會「爆炸式」失敗，而是默默失去動力——某工具突然連不上、edge case 一再發生、升級模型反而行為跑掉，最後變成「沒人再提的 agent」。

## 卡片內容
Production agent 的失敗模式是慢性退化——成功率時間序列下滑、token 浪費率上升、user 信任度緩慢侵蝕，但都不會觸發 alarm。這種失靈比單次故障處理更難識別，是建立 agent SLO、可觀測性與生命週期管理的觸發點。對應「Agent 95% 失敗」的時間維度——95% 不是「上線那天爆炸」，是「上線三個月後沒人用了」。需要的監控指標：成功率時間序列、tool 失敗率、user 重試率、token 浪費率、人類接手比例。

## 使用情境
- 設計 production agent 的監控儀表板
- 為 agent 產品建立 SLO 指標體系
- 對外解釋「為什麼 demo 成功不等於上線成功」

## 邊界 / 失效條件
- 低頻使用的 agent 慢性退化偵測難度更高
- 需要長期 trace 才有趨勢資料

## 上游連結
- [[Agent 產品 95% 在 Production 失敗的原因]]

## 下游連結
- [[10-008_Span-Level_Debug是Agent工程的分水嶺]]

## 關聯對照
- [[10-001_Agent速度撞上legacy_backend的DDoS化失敗模式]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
