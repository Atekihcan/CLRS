---
title:      Exercise A.2-1
clrs:       [A, 2]
published:  2012-12-19 19:00
---

>Show that $$\sum_{k = 1}^n 1/k^2$$ is bounded above by a constant.

As $$\frac 1 {k^2}$$ is a monotonically decreasing function, we can get an upper bound by using integral as follows:

$$\begin {align}
\sum_{k = 1}^n \frac 1 {k^2}
& = 1 + \sum_{k = 2}^n \frac 1 {k^2} \\
& \le 1 + \int_1^n \frac {dx} {x^2} \\
& = 1 + \left[-\frac 1 x\right]_1^n \\
& = 1 + \left[-\frac 1 n - \left(-\frac 1 1\right)\right] \\
& = 2 - \frac 1 n \\
& \le 2
\end {align}$$

Note that in the second line I took out the first term out of the sum to avoid division by zero while computing the integrals. These manipulations might seem irritating to some of you and they suck big time if you are not a fan of mathematics but mathematics is largely manipulation! ;)