---
tags:
  - my-article
Checkbox 1: true
---
【AI Agent 開發的 Prompt 管理嘗試】



在大神 **++[安德魯的部落格](https://www.facebook.com/andrew.blog.0928) ++**6月某貼文某段內容引發的想法：

—

過去: source (code) 要進版控, (code) build 的結果 (binary, executable, container image) 要進 AM (artifact management).

---

現在: source (requirement, 通常是 document + prompt) 要進版控, vibe coding + build 的結果 ( code / executable / container image ) 要進 AM ( 可能是同一個 or 另一個部署用的 git repo, 以及真正儲存 binary 的 AM )

就 CI/CD 的觀點來看，其實流程是一樣的，只是通通都往 "左移” 了一階, 未來的 source code, 意義上更像是產出物，而不是手寫的原始碼了。

我都特別寫 “source” code 或是講 “原始” 碼，因為我認為文字上的意義，是強調 “source” 才對，那是人類意圖真正變成對機器有意義的第一個產出。關鍵是 source, 不是 code. AI 的進步，同樣意義的 source 逐漸變成 document, 原本代表 source 的 code 現在變成 AI 的產出物了, 自然會有這樣的平移。

所以，意義上真正需要被版控的，其實是 source 而不是 code. 現在的 Git 是為了 code 的版控而設計的系統，如果未來的 source 從 code 變成 document, 版控會有甚麼改變? 版控的目的，是讓你能夠追蹤 source 因為甚麼原因，做了甚麼改變，讓你能事後還原整個變化的過程跟意圖，也能讓你從實際運作中的系統 ( 通常是來自 AM 部署出去的系統) 往回追蹤這份運行中的 artifacts 是來自哪一版的 source..

所以，未來需要追蹤的，是需求文件及 prompt 的變化。這邊的 prompt 包含產生 code 用的 prompt ( vibe coding )，應該也包含實際在線上運作的 AI APP 內含的 prompt .. 這有點難區分，就像之前在 GenAI 年會講到的，用 AI 開發 AI 產品，兩邊用到的 prompt 其實都需要被管理。

—



今天正式嘗試想在 code base 新增 prompts 資料夾，正式把 prompt 納入管理，



目前我認為Prompt 管理最理想的切入點會是不斷重複的類似開發動作，例如：新頁面、新的 Pipeline、新的一組 API …等，因為他們是，



「有範本可循 (template-based)」但又需要客製化細節的任務，且這些場景的共通點是「**變動點是可預測的**」



Prompt 的作用就是將「不變的部分」固化成最佳實踐，讓 AI 和開發者都專注於「變動的部分」



而 prompt 的內容原本想要放 參考檔案路徑 以及 程式限定範疇，但又想到如果把路徑寫得太死，維護管理又會變得很麻煩，



因此 prompt 應該會放置原則性的界定，並且把相關檔案路徑放到某一個文件統一維護，



\---

version: 1.0.0  # 版本迭進

tags: \["data-pipeline", "anomaly-detection", "architecture"\] # 標籤更具體

status: "draft" # 新增狀態，如 draft, in-review, finalized

author: "Your Name" # 追溯作者

\---

**\## Goal / Epic:** 

Designing a Generic Automated Anomaly Detection Pipeline

**\## Key Concepts & References (Guide to search):**

\* Primary Logic: The existing anomaly detection implementation, likely named \`anomaly\_[detector.py](detector.py)\` inside \`/src/algorithm/\`.

\* Data Models: Search for Pydantic or SQLAlchemy models within \`/src/models/\` to understand current data structures.

\* Service Layer: The main application services are located in \`/src/services/\` and handle business logic orchestration.

**\## The Coding Boundary (Scope):**

\* Allowed to modify: \`/src/services\`, \`/src/algorithm\`, \`/src/utils\`, \`/notebooks\`

\* Allowed to create: New files within the allowed directories.

\* Forbidden to modify: \`/src/core/\`, \`pyproject.toml\` (unless specified in iteration plan)

**\## Main Description**

…

…

**\## 🗺️ Iteration Strategy & Plan of Attack**

This is a complex task. We will break it down into the following iterative steps. The output of one step will be the input for the next.



**\*\*\[ This section should be filled by the output of the first run of this prompt \]\*\***



\* **\*\*Step 1: Architectural Design & Task Breakdown (This Prompt)\*\***

\* **\*\*Goal\*\***: Generate a detailed design for the event table schema and the pluggable detection logic. Produce a list of files to be created/modified and a sequence of implementation tasks.

\* **\*\*Expected Output\*\***: A Markdown document outlining the design and a JSON array of sub-tasks.

\* **\*\*Step 2: Implement Event Table Model\*\***

\* **\*\*Depends on\*\***: Step 1's Event Table Schema.

\* **\*\*Prompt\*\***: \`\[Link to a new, specific prompt for this task\]\`

\* **\*\*Goal\*\***: Create the Python data model for the event table.



\* **\*\*Step 3: Implement Detection Logic Interface\*\***

\* **\*\*Depends on\*\***: Step 1's Logic Design.

\* **\*\*Prompt\*\***: \`\[Link to a new, specific prompt for this task\]\`

\* **\*\*Goal\*\***: Create the abstract base class for all anomaly detectors.



\* **\*\*Step 4: ... (and so on)\*\***

\--- 

**\## 💬 \[Output from Previous Step\]**

(This section will be used in child prompts to provide context from the parent prompt's output)


