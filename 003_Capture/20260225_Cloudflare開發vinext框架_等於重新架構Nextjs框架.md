Cloudflare 最近搞了個叫 vinext 的框架，等於重新架構Nextjs框架，用 Vite 的引擎來跑 Next.js 的代碼，解決Nextjs最讓人詬病效能差的問題。
.
這兄弟搭了一個最簡單的測試網站，部署在 Cloudflare Workers 上，順手加了性能測試功能，可以即時顯示網頁載入速度和傳輸大小，想看看到底能有多快。

他親自驗證了下，官方沒吹牛逼：同樣一個基礎頁面，原生 Next.js 打包出來 165.2 KB，vinext 只有 71.6 KB。小了57%。用戶打開更快，流量也省了一半。

他還在頁面底部放了個對比表，把自己寫的單頁面跟官方博客的 33 頁中型應用數據放一起比。最右邊那列寫著 Verdict（判決結果）

Repo: https://github.com/h1n054ur/vinext-starter