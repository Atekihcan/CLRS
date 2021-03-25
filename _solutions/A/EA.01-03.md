---
title:      Exercise A.1-3
clrs:       [A, 1]
published:  2012-12-19 18:10
---

>Show that $$\sum_{k = 0}^{\infty} k^2x^k = x(1 + x)/(1 - x)^3$$ for $$0 < \vert x \vert < 1$$.

From chapter text $$\sum_{k = 0}^{\infty} kx^k = \frac x {(1 - x)^2}$$ (Eqn. A.8).

By differentiating this with respect to $$x$$, we get:

$$\begin {align}
\sum_{k = 0}^{\infty} k^2x^{k - 1} 
& =  \frac 1 {(1 - x)^2} + x \cdot \left( -\frac {2x - 2} {(1 - x)^4}\right) \\
& =  \frac 1 {(1 - x)^2} + x \cdot \left( \frac 2 {(1 - x)^3}\right) \\
& =  \frac {(1 - x) + 2x } {(1 - x)^3} \\
& =  \frac {1 + x} {(1 - x)^3}
\end {align}$$

Multiplying both sides by $$x$$, we get:

$$\sum_{k = 0}^{\infty} k^2x^k = \frac {x(1 + x)} {(1 - x)^3}$$