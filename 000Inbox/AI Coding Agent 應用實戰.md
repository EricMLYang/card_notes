---
tags:
  - vibe-code
---
# AI Coding Agent 應用實戰

- Reference

   - **Claude Code: One Month of Practical Experience — A Guide for Software Architects and Developers**

   - **不只是寫程式！Anthropic 內部團隊如何把 Claude Code 發揮到極致？**

   - **[How Anthropic teams use Claude Code](https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf)**



## User Case

- **用截圖就能除錯 Kubernetes？** 沒錯。當 Kubernetes 叢集出問題，團隊成員不再需要花大把時間手動檢查，而是直接把儀表板的**截圖**餵給 Claude Code。Claude 會一步步引導他們在 Google Cloud 的介面中找出問題根源（例如 Pod IP 位址耗盡），甚至直接提供解決問題的指令。過去需要網路專家介入的難題，現在幾分鐘就搞定了。

- **讓非技術人員也能操作複雜數據流：** 財務團隊需要處理數據，但他們不懂程式碼。怎麼辦？很簡單，他們只需要用白話文寫下需求，像是「查詢這個儀表板的資料，然後產生一份 Excel 報告」。Claude Code 就能將這些文字指令轉化為可執行的自動化流程。這徹底打破了部門間的技術壁壘。

- **新人的最佳導航員：** 對於剛加入的資料科學家來說，要馬上弄懂龐大又複雜的程式碼庫（Codebase）簡直是惡夢。現在，他們可以直接把團隊的說明文件（[Claude.md](Claude.md)）丟給 Claude，然後問：「我想做某個任務，需要看哪些檔案？」Claude 能快速解釋數據管線的依賴關係，讓新人以前所未有的速度上手。

- **快速原型打造（非同步模式）：** 當要開發一些實驗性或非核心功能時，工程師會啟用「自動接受模式」(auto-accept mode)。他們會給 Claude一個抽象的任務，然後就放手讓它自主編寫、測試、迭代。工程師只需要在 Claude 完成 80% 的工作後介入，進行最後的微調。他們用這個方法，只花了幾次迭代，就讓 Claude 自主完成了 Vim 模式 70% 的開發工作。

- **核心功能開發（同步模式）：** 但如果是涉及核心商業邏輯的關鍵功能，團隊就會採取更緊密的同步協作。他們會提供非常詳細的指令，即時監控 Claude 產生的程式碼品質，確保一切都符合架構和風格規範。這就像一位資深工程師帶著一位手速極快的實習生，完美結合了人類的經驗與 AI 的效率。

- **事件響應時間從 15 分鐘縮短到 5 分鐘：** 過去，手動追蹤一段程式碼的控制流，平均需要 10-15 分鐘。現在，他們把堆疊追蹤（stack traces）和相關文件丟給 Claude，幾分鐘內就能得到分析結果。

- **更有效率的程式碼審查：** 在審查 Terraform 這種基礎設施即程式碼（IaC）的變更時，他們會直接把計畫貼給 Claude，然後問一個很直接的問題：「這東西會搞砸什麼嗎？我會後悔嗎？」這讓安全審查變得更快速、更直觀。



## Basic Knowledge

- DDD ( Domain Driven Design )

- Clean Code

- Clean Architecture

- TDD ( Test Driven Design )



## Human Value

- can finally focus on what really matters: solving complex business problems

- 價值將從「寫程式」轉向「把技術語言翻譯成商業成果」。溝通、協作與故事化呈現會成為核心能力

- AI 會成為程式設計的必備工具，但仍需人類做「信任但驗證」──安全審計、效能壓測、法規遵循

- 長期維護與演進版本，核心功能，1 - 100

   

   

   

   



## **Shines and  Struggles**

- Strength

   - **Unit tests** are the absolute killer use 

      - generates comprehensive tests that cover edge cases I often don’t think of. 

   - New features on projects with standard architectures are another strength. 

      - If your project follows established patterns, Claude can generate REST endpoints, service layers, and repositories that integrate perfectly with the existing code.

   - **Debugging** with log analysis is surprisingly effective. 



- Limitations 

   - complex or unconventional architectures. 

   - An **event-driven** system with Kafka, CQRS patterns, and microservices communicating via gRPC can confuse even Opus. 

   - **比對 Cursor、Copilot 等**：在上下文處理與技術任務（如資料視覺化、程式碼分析）上更強，但成本也較高。Cursor 在精細控制上更強，一次性付費更划算 ()。

   



## Maximizes ProductivityWork Flow

- Example One:

   - Every feature begins with a **brainstorming** session with Claude where I define requirements.

   - Claude generates the initial code, I review and make modifications. 

   - **Unit tests** are generated automatically — this is probably the use case where Claude excels most.

   - The cycle continues with frequent commits on **feature branches**

   - Claude automatically manages commits following the **commitlint** conventions configured in the project. Manual review remains essential

   - Short, focused sessions work better than coding marathons. After 30–40 minutes, I use **`/clear`** to reset context and maintain optimal performance.



## Agent \*md File

- [CLAUDE.md](CLAUDE.md) file has become my AI assistant’s brain.

- The initial investment in configuration pays off exponentially. Every hour spent perfecting [CLAUDE.md](CLAUDE.md) translates into days saved from manual corrections.

- Project-specific **code conventions** are fundamental. 

- in java use case? Adding this information transformed Claude from a beginner to a junior developer who writes code indistinguishable from mine.

   - use **Lombok** to reduce boilerplate

   - adopt Google’s guidelines for indentation as styles

   - have specific patterns for error handling

   - always work with a DDD (domain driven design) structure in my projects when possible.

```markdown
# E-Commerce Platform Project Guide
## Project Overview
Multi-tenant e-commerce platform based on microservices architecture with Java 21 and AWS.
## Architecture Style
- **Domain-Driven Design (DDD)** with clear bounded contexts
- **Hexagonal Architecture** for each microservice
- **Event-Driven** communication between services via AWS EventBridge
## Code Conventions
### Java Style
- Google Java Style Guide for indentation (2 spaces)
- Lombok to reduce boilerplate (@Data, @Builder, @RequiredArgsConstructor)
- Avoid @AllArgsConstructor unless strictly necessary
- Prefer Optional<T> to null returns
- Stream API for collections when it improves readability
### Naming Conventions
- Package: com.company.domain.subdomain
- Classes: PascalCase (UserProfile, OrderService)
- Methods/Variables: camelCase
- Constants: UPPER_SNAKE_CASE
- Database fields: snake_case but mapped to camelCase in entities
### Error Handling
- Custom exceptions for domain logic (e.g.: InsufficientStockException)
- GlobalExceptionHandler for REST endpoints
- Problem Details RFC 7807 for error responses
- Log errors with correlation ID for distributed tracing
## Testing Strategy
- Unit tests: Given-When-Then pattern with AssertJ
- Integration tests: @SpringBootTest with Testcontainers
- Mock externals with WireMock
- Minimum coverage: 80% for business logic
## AWS Services Used
- ECS Fargate for deployment
- RDS Aurora PostgreSQL for persistence
- ElastiCache Redis for caching
- S3 for asset storage
- CloudWatch for monitoring
## Dependencies
- Spring Boot 3.4.x
- AWS SDK v2
- MapStruct for DTO mapping
- Resilience4j for circuit breaking
```



## Document

- For complex projects, I’ve discovered that maintaining separate documents for different domains works better than a single monolithic file.

   - A CLAUDE\_[AWS.md](AWS.md) for cloud configurations, a CLAUDE\_[TESTING.md](TESTING.md) for testing strategies, and so on. 

- dynamic context updates during session:

   - The **`/memory`** command allows dynamic context updates during sessions, while the **`#`** operator saves options directly into memory during the session.



# **Prompt Engineering: The New Core Competency**

- Writing effective prompts has become as fundamental a skill as knowing design patterns. The difference between a mediocre prompt and an excellent one can mean hours of saved work.

- After weeks of experimentation, I’ve consolidated a workflow that maximizes productivity. Every feature begins with a **brainstorming** session with Claude where I define requirements. Claude generates the initial code, I review and make modifications. **Unit tests** are generated automatically — this is probably the use case where Claude excels most.





## Other Tips:

- **read the documentation**. It’s an essential step, often underestimated. Claude Code has hidden features you’ll only discover by carefully reading the docs. The difference between using it at 20% or 100% of its potential lies right there.

- **Multi-Model Strategy: Cost Optimization**

- create **custom slash commands**. These commands allow you to automate specific workflows for your project, transforming complex operations into simple shortcuts.

- The configuration of **tools** available during sessions makes a huge difference. 

   - The **settings.json** file allows control over which tools Claude can use. 

   - The best strategy is to be permissive with read-only and navigation tools, which enormously accelerate the workflow without security risks.

```markdown
{
  "allow": [
    "Bash(cat:*)",
    "Bash(ls:*)",
    "Bash(rg:*)",
    "Bash(find:*)",
    "Bash(grep:*)",
    "Bash(head:*)",
    "Bash(tail:*)",
    "Bash(wc:*)",
    "Bash(tree:*)",
    "Bash(git:log,status,diff,branch)",
    "Bash(mvn:clean,compile,test)",
    "Bash(npm:list,outdated)"
  ]
}
```





# **Quantified ROI: Not Just Hype**

- productivity on standard development tasks increased significantly — what previously took an entire day now completes in a few hours. 

- Precisely quantifying this improvement is complex, but in my experience the increase is around **400%** for repetitive and well-defined activities.

- The real value,  My role has evolved. 

   - I spend less time writing boilerplate and more time reasoning about architectures and business requirements.

   - **Code review** has become more strategic — instead of looking for syntactic bugs, I focus on architectural decisions and scalability.

- Required skills are changing.

   - Knowing how to translate business requirements into effective prompts is the new critical competency. It’s like moving from manually assembling components to orchestrating complex systems.





## Take Away 

1. **先計畫，再執行：** 許多團隊都提到，他們會先在對話式的 [Claude.ai](Claude.ai) 介面中進行腦力激盪和規劃，把想法完全梳理清楚後，再請 Claude 產生一個步驟清晰的提示（Prompt），最後才拿到 Claude Code 中執行。

2. **把 AI 當成迭代的夥伴，而非一次性的解決方案：** 不要期望 AI 一次就給出完美答案。學會與它來回溝通、迭代修正，把它當成一個聰明的合作夥伴。

3. **視覺化溝通是王道：** 尤其是非技術團隊，大量使用「截圖」來告訴 Claude 他們想要什麼樣的介面。所見即所得，遠比用文字描述更有效率。

4. **勇敢分享「不完美」的原型：** 法務團隊特別強調，要克服分享「玩具」或未完成專案的恐懼。這些看似粗糙的原型，往往能激發跨部門的創新火花。

5. Anthropic 展示了一個工作新常態：**AI 不再只是特定職位的專屬工具，而是賦能給每一個人的「超能力」。** 無論你身處哪個行業、哪個職位，這份文件都證明了，只要用對方法，AI 就能幫助你打破技能的限制，專注於更具策略性和創造性的工作。