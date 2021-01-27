---
title:      Exercise A.1-4
clrs:       [A, 1]
published:  2012-12-19 18:15
redirect_from:
  - /EA.01-04/
---

>Show that $$\sum_{k = 0}^{\infty} (k - 1)/2^k = 0$$.

From chapter text $$\sum_{k = 0}^{\infty} x^k = \frac 1 {(1 - x)}$$ (Eqn. A.6) and $$\sum_{k = 0}^{\infty} kx^k = \frac x {(1 - x)^2}$$ (Eqn. A.8).

So, we can write:

$$\begin {align}
& \sum_{k = 0}^{\infty} kx^k - \sum_{k = 0}^{\infty} x^k \tag {1} \\
= & \frac x {(1 - x)^2} - \frac 1 {(1 - x)} \\
= & \frac {x - (1 - x)} {(1 - x)^2} \\
= & \frac {2x - 1} {(1 - x)^2}
\end {align}$$ 

Now, we can rearrange the expression in question as follows:

$$\begin {align}
\sum_{k = 0}^{\infty} \frac {k - 1} {2^k} 
& =  \sum_{k = 0}^{\infty} \frac k {2^k} - \sum_{k = 0}^{\infty} \frac 1 {2^k} \\
& =  \sum_{k = 0}^{\infty} k \cdot \left(\frac 1 2\right)^k - \sum_{k = 0}^{\infty} \left(\frac 1 2\right)^k
\end {align}$$

Note that this rearranged version is nothing but (1) with $$x = \frac 1 2$$.

$$\therefore \sum_{k = 0}^{\infty} \frac {k - 1} {2^k} = \frac {2 \cdot \frac 1 2 - 1} {\left(1 - \frac 1 2\right)^2} = 0$$