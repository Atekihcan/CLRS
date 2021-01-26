---
title:      Exercise A.2-4
clrs:       [A, 2]
published:  2012-12-19 19:15
---

>Approximate $$\sum_{k = 1}^n k^3$$ with an integral.

As $$k^3$$ is a monotonically increasing function, we can write:

$$\begin {align}
\int_0^n x^3 & \le \sum_{k = 1}^n k^3 \le \int_1^{n + 1} x^3 \\
\left[\frac {x^4} 4\right]_0^n & \le \sum_{k = 1}^n k^3 \le \left[\frac {x^4} 4\right]_1^{n + 1} \\
\left[\frac {n^4} 4 - 0\right] & \le \sum_{k = 1}^n k^3 \le \left[\frac {(n + 1)^4} 4 - \frac 1 4\right] \\
\frac {n^4} 4 & \le \sum_{k = 1}^n k^3 \le \frac {(n + 1)^4 - 1} 4
\end {align}$$