---
tags:
  - container
---
# 〈Linux containers in 500 lines of code〉

是篇很好的文章，運用 Linux 核心提供的 *namespace*, *capability*, *seccomp* 與 *pivot_root*／*chroot* 等機制，從無到有打造可運作的 Linux container。然而該文章充斥大量原始程式碼，讓閱讀門檻偏高。Andrushika 同學閱讀該文章並整理相關背景知識，在期末專題的報告中，重新彙整為下方筆記。

除了整理對應 man page 與 /proc 資訊，Andrushika 同學進行下方實驗：

以 `unshare(2)`／`setns(2)` 理解 Linux namespaces 對行程 ID、網路介面與掛載點的隔離

交替 pivot_root 與 chroot，比對 rootfs 切換對可見路徑的影響

歡迎關注和討論。

**<https://hackmd.io/@sysprog/H18ne9Y-gl>**