---
tags:
  - business-data-science
---
# NP-Hard

- [輕鬆談演算法的複雜度分界：什麼是P, NP, NP-Complete, NP-Hard問題](https://ycc.idv.tw/algorithm-complexity-theory.html)

- Glossary:

   - deterministic Turing machine (DTM)

   - non-deterministic Turing machine (NTM) 

- P ( polynomial time )

   - 現實面是只有在一個數量級時間以下的問題我們才好應付，這個數量級被稱為 polynomial time（多項式時間），用大ＯＯ表示為Ｏ(N\*\*k)

   - 如果超過 polynomial time 的問題我們稱為 [intractable](https://en.wikipedia.org/wiki/Intractability\_%28complexity%29) problem (難解的問題)

- NP ( non-deterministic polynomial-time )

   - 有一群演算法用NTM來做計算所需時間是 polynomial time

   - 如果用 DTM 來驗證一組解是否正確只需要 polynomial time，那這個問題就是一個NP問題

- NP-Complete

   - 1971年美國 Stephen A. Cook提出了[Cook-Levin理論](https://zh.wikipedia.org/wiki/Cook-Levin%E7%90%86%E8%AB%96)，這個數學理論指出任何一個NP裡面的問題都可以在 polynomial time 內，使用DTM，將之化約成「一個布林方程式是否存在解」的問題，這個被化約的問題又稱為布爾可滿足性問題（SAT），我們稱SAT問題為NP-Complete問題。

   - 只要滿足以下兩個條件的，我們都稱之為[NP-Complete](https://en.wikipedia.org/wiki/NP-completeness)：

      - 「問題」本身是一個NP問題

      - 所有的NP問題都可以用DTM在 polynomial time 內化約成為這個「問題」。

   - 1972年，Richard Karp將這個想法往前推進了一步，他證明了[21個不同但都難解的組合數學與圖論問題為NP-Complete問題](https://zh.wikipedia.org/wiki/%E5%8D%A1%E6%99%AE%E7%9A%84%E4%BA%8C%E5%8D%81%E4%B8%80%E5%80%8BNP-%E5%AE%8C%E5%85%A8%E5%95%8F%E9%A1%8C)，一樣的其中的任何一種只要被證明為P問題，都可以間接證明P=NP，目前已經有更多問題被證明為NP-Complete 問題

- NP-Hard

   - 所有的 NP 問題都可以用 DTM 在 polynomial time 內化約成為一個「問題」