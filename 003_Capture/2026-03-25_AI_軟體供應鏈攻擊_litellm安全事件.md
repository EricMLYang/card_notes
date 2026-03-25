# AI 軟體供應鏈攻擊：litellm PyPI 安全事件深度分析

**來源**：Andrej Karpathy（@karpathy）
**連結**：https://x.com/karpathy/status/2036487306585268612
**日期**：2026-03-25
**主題**：AI / 軟體安全 / 供應鏈攻擊
**互動**：45.7M 瀏覽 · 1.1K 留言 · 5.9K 轉發 · 24K 喜歡

---

## 正文

Software horror: litellm PyPI supply chain attack.

Simple `pip install litellm` was enough to exfiltrate SSH keys, AWS/GCP/Azure creds, Kubernetes configs, git credentials, env vars (all your API keys), shell history, crypto wallets, SSL private keys, CI/CD secrets, database passwords.

LiteLLM itself has 97 million downloads per month which is already terrible, but much worse, the contagion spreads to any project that depends on litellm. For example, if you did `pip install dspy` (which depended on litellm>=1.64.0), you'd also be pwnd. Same for any other large project that depended on litellm.

Afaict the poisoned version was up for only less than ~1 hour. The attack had a bug which led to its discovery - Callum McMahon was using an MCP plugin inside Cursor that pulled in litellm as a transitive dependency. When litellm 1.82.8 installed, their machine ran out of RAM and crashed. So if the attacker didn't vibe code this attack it could have been undetected for many days or weeks.

Supply chain attacks like this are basically the scariest thing imaginable in modern software. Every time you install any dependency you could be pulling in a poisoned package anywhere deep inside its entire dependency tree. This is especially risky with large projects that might have lots and lots of dependencies. The credentials that do get stolen in each attack can then be used to take over more accounts and compromise more packages.

Classical software engineering would have you believe that dependencies are good (we're building pyramids from bricks), but imo this has to be re-evaluated, and it's why I've been so growingly averse to them, preferring to use LLMs to "yoink" functionality when it's simple enough and possible.

---

## 背景資訊（引用貼文）

Daniel Hnyk (@hnykda)，Mar 24：

> LiteLLM HAS BEEN COMPROMISED, DO NOT UPDATE. We just discovered that LiteLLM pypi release 1.82.8. It has been compromised, it contains litellm_init.pth with base64 encoded instructions to send all the credentials it can find to remote server + self-replicate. link below

---

## 重點摘要

- **受害規模**：litellm 每月 9700 萬次下載，任何依賴 litellm 的專案（如 dspy）都受影響
- **竊取內容**：SSH keys、雲端憑證（AWS/GCP/Azure）、API keys、shell history、crypto wallets、CI/CD secrets、資料庫密碼
- **發現原因**：攻擊程式有 bug，導致某用戶機器 RAM 耗盡崩潰才被發現
- **持續時間**：惡意版本存在不到 1 小時即被下架
- **Karpathy 觀點**：這讓他更傾向使用 LLM 直接「提取」功能代碼，而非依賴大量第三方套件
