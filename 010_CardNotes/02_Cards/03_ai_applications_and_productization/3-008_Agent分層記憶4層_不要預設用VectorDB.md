# Agent 分層記憶 4 層 — 不要預設用 Vector DB

- 狀態：KEEP
- 類型：Pattern
- 分類：3-
- 索引：010_CardNotes/01_Index/03_ai_applications_and_productization.md
- 來源：005_PARA/02_Areas/AI_Software_Data/Agent/20260316_AI_Agent生產架構_工具記憶評估護欄.md（#3）+ 005_PARA/02_Areas/AI_Software_Data/Agent/inbox/20260414_李宏毅2026Agent課高解析摘要.md（#2，吸收）

## 核心命題
Agent 記憶分四層：工作記憶 / 對話摘要 / 任務製品 / 長期偏好；vector DB 只適合特定語意搜尋場景，不該作為記憶基礎。

## 卡片內容
多數團隊一聽到「agent 記憶」就先架 vector DB，這是錯誤預設。實務上分四層：(1) **工作記憶**（短暫狀態、本輪 reducer 用）；(2) **對話摘要**（rolling 有損壓縮，避免 context 爆掉）；(3) **任務製品**（結構化輸出，agent 自己生產的中間產物）；(4) **長期偏好**（user-level、跨 session 的設定與 pattern）。多用結構化儲存（Redis/Delta/KV）+ 摘要管理，比向量檢索更可靠、更便宜、更可觀察。Vector 檢索只在「語意搜尋大量非結構化文件」這個特定場景才有優勢。提醒：李宏毅課程指出 agent 運行時 84% 的 context 被工具觀察結果佔據——記憶設計的核心問題是「壓縮與過濾」，不是「儲存與檢索」。

## 使用情境
- 規劃 agent 記憶層架構選型時
- 反駁「先架 vector DB」的常見預設
- 評估現有 agent 的 context 浪費點

## 邊界 / 失效條件
- RAG-heavy 應用 vector DB 仍是合適選擇
- 多用戶隔離與權限治理需要額外設計
- 摘要壓縮可能丟失關鍵 context

## 上游連結
- [[3-006_Harness六層構成_Agent系統工程的解構]]

## 下游連結
- [[Lakebase 作為 AI Agent 記憶層：sub-10ms 狀態管理 + Database Branching 沙盒]]
- [[Context 是增值型投資：維護的上下文隨 AI 進步而複利成長]]

## 關聯對照
- [[Context Graph 捕獲組織隱性知識]]

## 備註
- 由 `break-cards` → `refine-cards` 流程產出
