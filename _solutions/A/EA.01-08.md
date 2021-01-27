---
title:      Exercise A.1-8
clrs:       [A, 1]
published:  2012-12-19 18:35
redirect_from:
  - /EA.01-08/
---

>Evaluate the product $$\prod_{k = 2}^n (1 - 1/k^2)$$.

Note that, $$1 - \frac 1 {k^2} = \frac {k^2 - 1} {k^2} = \frac {(k - 1)(k + 1)} {k \cdot k}$$

$$\require {cancel}\begin {align}
& \prod_{k = 2}^n \left(1 - \frac 1 {k^2}\right) \\
= & \prod_{k = 2}^n \left(\frac {(k - 1)(k + 1)} {k \cdot k}\right) \\
= & \frac {1 \cdot 3} {2 \cdot 2} \cdot \frac {2 \cdot 4} {3 \cdot 3} \cdot \frac {3 \cdot 5} {4 \cdot 4} \cdots \frac {(k - 2) \cdot k} {(k - 1) \cdot (k - 1)} \cdot \frac {(k - 1) \cdot (k + 1)} {k \cdot k} \\
= & \frac {1 \cdot \cancel{3}} {2 \cdot \cancel{2}} \cdot \frac {\cancel{2} \cdot \cancel{4}} {\cancel{3} \cdot \cancel{3}} \cdot \frac {\cancel{3} \cdot \cancel{5}} {\cancel{4} \cdot \cancel{4}} \cdots \frac {\cancel{(k - 2)} \cdot \cancel{k}} {\cancel{(k - 1)} \cdot \cancel{(k - 1)}} \cdot \frac {\cancel{(k - 1)} \cdot (k + 1)} {\cancel{k} \cdot k} \\
= & \frac {k + 1} {2k}
\end {align}$$