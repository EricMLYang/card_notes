---
tags:
  - charging-master
---
# CGM-Algorithm: Framework 

- Reference

   - [探索電動車充電的科學之旅：解密電池充電曲線](https://vocus.cc/article/65322129fd89780001b75cf9)

   - 



## GA

- Tips

   - Increase population size for better solution diversity

   - More generations allow better convergence

   - However, there's a tradeoff with computation time

      - Rule of thumb: Start with population = 10x problem dimensions, then adjust based on results

   - Keep mutation rate relatively low (0.1-0.2) to avoid random search

      - If getting stuck in local optima: increase mutation rate

      - If solutions are too random: decrease mutation rate

   - Crossover rate should be higher (0.4-0.8) to combine good solutions

   - 


