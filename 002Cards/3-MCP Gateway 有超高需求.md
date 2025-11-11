
企業一旦開始導入 MCP，
馬上就會發現需要 Gateway 來解決各種問題，
如何管理內部眾多 MCP server 和工具，
特別是安全與授權挑戰。
因此希望能有單一的 MCP server 作為 Gateway 角色，統一入口管理。

- WorkOS 分享從 [localhost](localhost) 到企業級的血淚史。身份驗證只是第一步，更難的是「AI workload 之間的授權傳遞」。還有各家推出 Gateway 方案百花齊放:

- UCL 把 MCP 包成企業級 Gateway

- Pomerium 用零信任架構包裝所有服務

- A16Z 提出 Service Proxy 概念

- Smithery、Fastn、Natoma 都推出託管方案

- MCP Defender 的安全方案: 使用 Proxy 攔截所有流量，用 LLM 來保護 LLM

- ScaleKit 提出 Auth 託管方案

- Anthropic 工程師也分享了他們內部 MCP gateway 的經驗

非常多公司都在做 Gateway 這個題目，顯示這是真實且迫切的需求。