---
title:      Exercise A.1-2
clrs:       [A, 1]
published:  2012-12-19 18:05
---

>Show that $$\sum_{k = 1}^n 1/(2k - 1) = \ln(\sqrt n) + O(1)$$ by manipulating the harmonic series.

$$\begin {align}
\sum_{k = 1}^n \frac 1 {(2k - 1)} 
& = 1 + \frac 1 3 + \frac 1 5 + \cdots + \frac 1 {2n - 1} \\
& = \left(1 + \frac 1 2 + \frac 1 3 + \cdots + \frac 1 {2n} \right) -  \frac 1 2 \left(1 + \frac 1 2 + \frac 1 3 + \cdots + \frac 1 n \right)\\
& = \sum_{k = 1}^{2n} \frac 1 k - \frac 1 2 \sum_{k = 1}^n \frac 1 k \\
& = \ln 2n + O(1) - \frac 1 2 \left(\ln n + O(1)\right) \\
& = \ln 2 + \ln n + O(1) - \frac 1 2 \left(\ln n + O(1)\right) \\
& = \ln n - \frac 1 2 \ln n + \ln 2 + O(1) - \frac 1 2 O(1)  \\
& = \frac 1 2 \ln n + O(1) \\
& = \ln \sqrt n + O(1)
\end {align}$$