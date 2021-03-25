---
title:      Exercise A.1-1
clrs:       [A, 1]
published:  2012-12-19 18:00
---

>Find a simple formula for $$\sum_{k = 1}^n (2k - 1)$$.

$$\begin {align}
\sum_{k = 1}^n (2k - 1) 
& = 2\sum_{k = 1}^n k - \sum_{k = 1}^n 1 \\
& = 2 \frac {n(n + 1)} 2 - n \\
& = n(n + 1) - n \\
& = n^2 + n - n \\
& = n^2
\end {align}$$