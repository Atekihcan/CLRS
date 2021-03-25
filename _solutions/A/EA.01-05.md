---
title:      Exercise A.1-5
clrs:       [A, 1]
published:  2012-12-19 18:20
---

>Evaluate the sum $$\sum_{k = 1}^{\infty} (2k + 1)x^{2k}$$.

We have to assume $$\vert x \vert < 1$$, otherwise we can't use the infinite series approximation.

We can calculate $$\sum_{k = 1}^{\infty} x^{2k + 1}$$ as follows:

$$\begin {align}
\sum_{k = 1}^{\infty} x^{2k + 1} 
& = x^3 + x^5 + x^7 + \cdots \\
& = x + x^3 + x^5 + x^7 + \cdots - x \\
& = x(1 + x^2 + x^4 + x^6 + \cdots) - x \\
& = x \cdot \sum_{k = 0}^{\infty} (x^2)^k - x \\
& = x \cdot \frac 1 {1 - x^2} - x \\
& = \frac {x - x(1 - x^2)} {(1 - x^2)} \\
& = \frac {x^3} {(1 - x^2)}
\end {align}$$

Differentiating both sides of the above equation w.r.t $$x$$:

$$\begin {align}
\sum_{k = 1}^{\infty} (2k + 1)x^{2k} 
& = \frac d {dx} \frac {x^3} {(1 - x^2)} \\
& = \frac {3x^2(1 - x^2) - x^3(-2x)} {(1 - x^2)^2} \\
& = \frac {3x^2 - 3x^4 + 2x^4} {(1 - x^2)^2} \\
& = \frac {x^2(3 - x^2)} {(1 - x^2)^2}
\end {align}$$