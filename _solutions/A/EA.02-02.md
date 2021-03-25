---
title:      Exercise A.2-2
clrs:       [A, 2]
published:  2012-12-19 19:05
---

>Find an asymptotic upper bound on the summation $$\sum_{k = 0}^{\lfloor \lg n\rfloor} \lceil n/2^k\rceil$$.

Remember that $$\lceil x \rceil \le x + 1$$.
So, we can write:

$$\begin {align}
\sum_{k = 0}^{\lfloor \lg n\rfloor} \lceil \frac n {2^k}\rceil
& \le \sum_{k = 0}^{\lfloor \lg n\rfloor} \left( \frac n {2^k} + 1 \right)\\
& = \lg n + 1 + \sum_{k = 0}^{\lfloor \lg n\rfloor} \frac n {2^k} \\
& \le \lg n + 1 + \sum_{k = 0}^{\infty} \frac n {2^k} \\
& = \lg n + 1 + n \cdot \frac 1 {1 - 1/2} \\
& = \lg n + 1 + 2n \\
& = O(n)
\end {align}$$