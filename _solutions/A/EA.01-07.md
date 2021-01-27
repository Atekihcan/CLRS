---
title:      Exercise A.1-7
clrs:       [A, 1]
published:  2012-12-19 18:30
redirect_from:
  - /EA.01-07/
---

>Evaluate the product $$\prod_{k = 1}^n 2 \cdot 4^k$$.

Let's assume $$P = \prod_{k = 1}^n 2 \cdot 4^k$$

$$\begin {align}
\lg P 
& = \lg \left( \prod_{k = 1}^n 2 \cdot 4^k \right) \\
& = \sum_{k = 1}^n \lg \left(2 \cdot 4^k \right) \\
& = \sum_{k = 1}^n \lg \left(2 \cdot 2^{2k} \right) \\
& = \sum_{k = 1}^n \lg 2^{2k + 1} \\
& = \sum_{k = 1}^n (2k + 1) \\
& = 2\sum_{k = 1}^n k + \sum_{k = 1}^n 1 \\
& = 2 \frac {n(n + 1)} 2 + n \\
& = n(n + 1) + n \\
& = n(n + 2)
\end {align}$$

Hence, $$P = 2^{n(n + 2)}$$.