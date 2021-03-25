---
title:      Exercise A.2-5
clrs:       [A, 2]
published:  2012-12-19 19:25
---

>Why didn’t we use the integral approximation (A.12) directly on $$\sum_{k = 1}^n 1/k$$ to obtain an upper bound on the $$n$$-th harmonic number?.

To get an upper bound using integral approximation (A.12), we need to integrate the function from $$x = (1 - 1) = 0$$. This makes the function $$\frac 1 x$$ undefined because of division-by-zero. To avoid this, we took out the first term ($$k = 1$$) and carried out the sum from $$k = 2$$ and the integral from $$x = 1$$.