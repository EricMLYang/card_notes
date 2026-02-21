---
tags:
  - os
---
# Linux 核心系統開發

## https://operating-system-in-1000-lines.vercel.app/en?fbclid=IwZXh0bgNhZW0CMTEAAR1L5-JX_CIABDObH_VjHpfa_9u2jBllxmKuVtsA5WnAiQ1TyFqcGhVA474_aem_IoQZnyvIg2YFWw8-Bh59zw

## Join the development

- 改進 Linux 核心的困難處不只在於找到切入點，而是就算做出貢獻且獲得開發者認可，其後尚有各式整合驗證的工作，可見現代軟體系統規模之龐大和複雜

   - 稍早 [邱冠維](https://www.facebook.com/profile.php?id=100000444220164&\__cft_\_\[0\]=AZWilVY9ckgKxt4uvWq9HN9jMC0QJgyQVjNe1Idi9k_Bbk1mQtpWfawXKw4J37ePJE3nWLa5YcgEr55lBshlIMPCyvxKAjZljVy7BR8VKV4Y9rVoUf9PaM8qShW7G2ln-pfIXjBqBk6M3pIHzHJIOsoS7qZm21Xrbv5tU8jcWwW8wjhP9XjfcjbeNS7Q1RoTKpzsFp23im7x7uPJv-6AhOWqx3c4rYhBpC0BzLBnre6ZZTvHllv20h20AVSMF2t2I8M&\__tn_\_=-\]K-y-R) 針對 Linux 核心的資料排序提出一系列更動，降低排序所需要的資料交換次數，但最近 Linux DRM (Direct Rendering Manager，與硬體加速繪圖有關) 的開發者發現，在 AMD 處理器上無法有效進行電源管理 (power management，簡稱 PM)，這樣就無法真正休眠，從而造成電池續航時間大幅縮短。起初開發者認為是 PM 子系統相關的修改，結果用 git bisect (使用基本二分搜尋演算法來找出有問題的 commit) 才發現，上述問題竟然跟邱同學稍早的 sort 貢獻有關。

   - <https://gitlab.freedesktop.org/drm/amd/-/issues/3436>