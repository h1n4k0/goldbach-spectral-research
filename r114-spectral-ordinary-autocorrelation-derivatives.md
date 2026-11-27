# One-sided derivatives and infinite variation of the ordinary arithmetic autocorrelation

The fixed-radical ordinary autocorrelation is differentiable precisely where its exact symmetric cusp vanishes. Its two one-sided derivative versions are bounded, regulated, and integrable. Nevertheless, the absolute derivative jumps have infinite sum on every open lag interval. The claim is about the actual arithmetic profile in the ordinary unsigned wall, not its Dickman replacement or a full parity difference.

## 1. Notation and result

Fix an even squarefree integer $R$ and use the same $C_R$ as in the [arithmetic cusp theorem](r113-spectral-ordinary-autocorrelation-arithmetic-cusps.md) and the [true unsigned wall](r112-spectral-odd-disjoint-true-wall-correlation.md). Define $\alpha^\circ(n)$ multiplicatively on squarefree odd integers by $\alpha^\circ(p)=(p-1)/(p^2-2)$ for odd primes, and $\alpha^\circ(1)=1$. Only squarefree integers coprime to $R$ are used below. For squarefree $j$ with $(j,R)=1$, write

$$
 \begin{split}
  v_j&=\mu(j)\alpha^\circ(j)^2,\qquad
  a_j(n)=\mu(n)\alpha^\circ(n)\mathbf1_{(n,Rj)=1}
                     \quad(n\ {\rm squarefree}),\\
  R_j(u)&=\sum_{n\le e^u}a_j(n),\qquad
  C_j(t)=\int_{\mathbb R}R_j(u)R_j(u+t)\,du,\qquad
  C_R(t)=\sum_j v_j C_j(t).
 \end{split}                                                       \tag{1}
$$

For all other $n$ set $a_j(n)=0$. The function $R_j$ is right-continuous and is zero on $u<0$; its jump at zero is included. In particular $|a_j(n)|\le1/n$. Put

$$
  J_R(t)=
  \begin{cases}
  \mu(ab)\alpha^\circ(ab),&
    e^t=a/b,\quad a,b\ge1,\quad (a,b)=1,\quad
    ab\ {\rm squarefree},\quad (ab,R)=1,\\
  0,&\text{otherwise}.
  \end{cases}                                                      \tag{2}
$$

**Theorem.** The right and left derivatives $D_+,D_-$ of $C_R$ exist at every real $t$. Their absolutely and locally uniformly convergent formulas are

$$
 \begin{split}
 D_+(t)&=\sum_j v_j\sum_{n\ge1}a_j(n)R_j((\log n-t)-),\\
 D_-(t)&=\sum_j v_j\sum_{n\ge1}a_j(n)R_j(\log n-t).
 \end{split}                                                       \tag{3}
$$

Here $f(x-)$ denotes the left limit. These versions are regulated, with $D_+$ right-continuous, $D_-$ left-continuous, and the left and right limits of either version at $t$ equal to $D_-(t)$ and $D_+(t)$ respectively. One has $D_-(t)-D_+(t)=J_R(t)$. Thus $C_R$ is differentiable at every real number except the precise admissible log ratios in (2), including differentiability at all irrational $e^t$ and at rational $e^t$ disallowed by the mask or squarefree condition. Both versions are continuous at each such differentiability point. There is a fixed $c>0$ such that

$$
                        |D_\pm(t)|\ll_R e^{-c\sqrt{|t|}}.            \tag{4}
$$

In particular $C_R$ is globally Lipschitz and absolutely continuous. But for every nonempty open lag interval $I$,

$$
                        \sum_{t\in I}|J_R(t)|=\infty .              \tag{5}
$$

Neither version of the derivative has bounded variation on any such interval.

## 2. Direct one-sided increments

Equations (6)–(7) of the [shifted autocorrelation proof](r108-spectral-odd-disjoint-shifted-autocorrelation.md) give, when the fixed deleted-prime mask is $R$, a positive moment $A(j)\ge1$ with

$$
 |R_j(u)|\ll_R A(j)\quad(u\in\mathbb R),\qquad
 |R_j(u)|\ll_R A(j)e^{-c_0\sqrt u}\quad(u\ge1),\qquad
                    \sum_j |v_j| A(j)^2\ll1.                     \tag{6}
$$

The associated $L^1$ and $L^2$ bounds in that proof give absolute convergence in (1). Now for $h>0$, the exact increment in the second argument of $C_j$ is

$$
 \begin{split}
  \frac{C_j(t+h)-C_j(t)}{h}
     &=\sum_{n\ge1}a_j(n)\frac1h
                  \int_{\log n-t-h}^{\log n-t} R_j(u)\,du,\\
  \frac{C_j(t)-C_j(t-h)}{h}
     &=\sum_{n\ge1}a_j(n)\frac1h
                  \int_{\log n-t}^{\log n-t+h} R_j(u)\,du.
 \end{split}                                                       \tag{7}
$$

For example $R_j(u+t+h)-R_j(u+t)=\sum_n a_j(n)\mathbf1_{[\log n-t-h,\log n-t)}(u)$ at every finite $u$. Before integrating, take $t$ in any compact interval and $0<h\le1$. For all sufficiently large $n$, every sampled $u$ is at least $\tfrac12\log n$ and at least $1$. The absolute integrals divided by $h$, multiplied by $|a_j(n)|$, are therefore bounded by $O_R(A(j)n^{-1}e^{-c_1\sqrt{\log n}})$. The sum over $n$ of this bound is finite, as is seen by grouping in unit logarithmic intervals. For the finitely many small $n$ use $O_R(A(j)/n)$. This majorant works before and after summing against $|v_j|$, since (6) also bounds $\sum_j |v_j|A(j)$. Thus (7) follows by absolute integration and summation, including the atom at $n=1$; no absolute bound for the total jump mass of a primitive is required.

Send $h$ to zero in both directions in (7). The interval averages tend to the values displayed in (3), including when $\log n-t=0$. The same majorant justifies this passage and absolute local uniform convergence of the series in (3). For any fixed finite set of $(j,n)$, each of the two versions is a step function in $t$ with finitely many jumps on a compact interval, because only finitely many $m$ can have $\log m$ in the compact range of $\log n-t$. Their respective endpoint conventions in $t$ are right and left. Hence the uniform series have one-sided limits and the stated continuity conventions. For either finite version the left and right limits use respectively $R_j(\log n-t)$ and $R_j((\log n-t)-)$; the uniform convergence gives the same matching for the full versions.

The difference of the two derivatives is the symmetric numerator from the cusp theorem, divided by $h$ and sent to zero. Its exact coefficient (3) there is $J_R(t)$ as in (2) here; equivalently (3) here directly pairs the jump at $\log n-t$ with the jump at $\log n$, and the signed $j$ Euler sum is the one evaluated in that theorem. This proves the differentiability and continuity classifications. For the global bound, if $t\le-2$, each argument of $R_j$ in (7) is at least $|t|+\log n-1$. Grouping $n$ in $\log n\in[k,k+1)$, where the sum of $1/n$ is $O(1)$ uniformly for integers $k\ge0$, bounds the absolute series in each quotient by

$$
  \ll_R A(j)\sum_{k\ge0} e^{-c_0\sqrt{|t|+k-1}}
                         \ll_R A(j)e^{-c_2\sqrt{|t|}}.              \tag{8}
$$

The second inequality follows by comparison with the integral of $e^{-c_0\sqrt x}$, decreasing $c_2$ if needed. The local bound on quotients covers $|t|\le2$. Evenness of $C_R$ converts a positive-lag difference quotient to a negative-lag quotient with opposite sign and the other endpoint convention. Thus all the real quotients in (7) after summation over $j$, for $0<h\le1$, admit a single constant bound, and the same argument proves (4) for the derivatives. This uniform quotient bound proves the global Lipschitz assertion by subdivision; global absolute continuity follows from that bound, and (4) gives integrability of both derivative versions.

## 3. A positive mass of absolute jumps in each large block

Fix any nonempty open lag interval $I$. Choose fixed closed intervals $[A_1,A_2]\subset(0,\infty)$ and $[B_1,B_2]\subset(1,2)$ of positive length such that the rectangle

$$
          A_1 X\le a\le A_2 X,\qquad B_1 X\le b\le B_2 X             \tag{9}
$$

lies in $\log(a/b)\in I$ for every $X>0$. This is possible by taking a sufficiently small rectangle around any point with the desired ratio and $B_1<b/X<B_2$. We show that for all sufficiently large $X$ there are $\gg_{R,I} X^2$ integer pairs in (9) with $ab$ squarefree, $(ab,R)=1$ and

$$
                  \sum_{\substack{p\mid ab\\p>P}}\frac1p\le1        \tag{10}
$$

for some sufficiently large fixed $P$. In particular they are already reduced pairs. The cutoff $P$ is fixed before sending $X$ to infinity.

Take $P\ge2$ at least as large as every prime dividing $R$, and first prescribe local conditions only at $p\le P$. For $p\mid R$ require $p\nmid ab$. For $p\nmid R$ exclude $p^2\mid a$, $p^2\mid b$ and simultaneous $p\mid a,b$. The latter admissible fraction of pairs modulo $p^2$ in both coordinates is at least $1-3/p^2$ by the union bound, and is positive (both coordinates can be units). The product of the local admissible fractions is bounded below by a positive constant depending only on $R$, since $\sum_p p^{-2}<\infty$. For each fixed $P$, the Chinese remainder theorem and integer counts in the two genuine intervals imply that the density in (9) tends to this product as $X\to\infty$. Thus these conditions alone leave at least $c_{R,I}X^2$ pairs, for $c_{R,I}>0$ independent of $P$, once $X$ is sufficiently large depending on $P$.

A square divisor $p^2\mid a$ or $p^2\mid b$ at $p>P$ loses at most $O_I(X^2/P+X^{3/2})$ pairs, by summing $O_I(X(X/p^2+1))$ over $P<p\le O_I(\sqrt X)$. A common divisor $p\mid(a,b)$ at $p>P$ loses at most $O_I(X^2/P+X\log(2X))$ pairs by summing $O_I((X/p+1)^2)$ over $P<p\le O_I(X)$. These upper bounds can sum over integers instead of primes. For (10) the total reciprocal mark over all pairs in (9) is at most

$$
      O_I\!\left(X^2\sum_{m>P}\frac1{m^2}
                         +X\sum_{m\le O_I(X)}\frac1m\right)
                    =O_I(X^2/P+X\log(2X)),                       \tag{11}
$$

since the counts at an individual $p$ in either coordinate are $O_I(X(X/p+1))$. The number excluded by (10) is at most this total mark. Choose $P$ large relative to the uniform positive density lower bound and the rectangle constants, then send $X$ to infinity. This proves the asserted $\gg_{R,I}X^2$ bound on the actual squarefree coprime pairs with (10).

On each remaining pair,

$$
 |J_R(\log(a/b))|=\alpha^\circ(ab)
 \ \ge\ \frac1{ab}\prod_{p\mid ab}(1-1/p)
 \ \gg_{R,I,P} X^{-2}.                                            \tag{12}
$$

The inequality follows at each allowed prime from the exact factor in (1). For the last bound use the product over all $p\le P$ as a fixed positive lower bound for the small-prime factors; the others have $\log(1-1/p)\ge-2/p$ and (10) bounds their total loss. Thus a large block contributes a fixed positive sum of absolute jumps. Using $X=2^k$, $k\to\infty$, the intervals for $b$ are pairwise disjoint. A reduced positive fraction determines both $a$ and $b$ uniquely, so all jumps counted in distinct blocks are distinct. This proves (5).

For a regulated function, the sum of absolute jumps over any finite subset of an open interval is at most its total variation on that interval: choose disjoint subintervals about those points, include their endpoints in a partition, and let them tend to the points to recover each jump. Both versions in (3) have jump size $|J_R(t)|$ by their proved one-sided limits. Thus (5) excludes bounded variation for either. It does not represent the second derivative as a locally finite atomic measure.

## 4. The moving ordinary wall bracket

In the true unsigned wall formula write $d=T-\log p$ for the same wall prime $p$ throughout. Its ordinary bracket, with the original directed integral, is

$$
 W_p(d)=(d+\log p)C_R(d)-2\int_0^d C_R(t)\,dt,\qquad d+\log p>0 .
$$

When varying $d$ in this formula the cap $T=d+\log p$ also varies. Its one-sided derivatives are $(d+\log p)D_\pm(d)-C_R(d)$, so the exact difference of left and right derivatives is $(d+\log p)J_R(d)$. The nondifferentiability set on this domain is precisely the log-ratio set in (2). On a closed subinterval of any nonempty open interval in the domain the cap is bounded below by some positive constant, so (5) and the same jump argument show that the moving bracket's derivative is not of bounded variation on any such open interval. This is a local statement about the ordinary integrand of the actual unsigned wall formula. It does not assign derivative behavior to the physical integral or its error term, or assert a sign or size for the distinct signed pole, a full parity difference, or a full mixed correlation. No existence of an exceptional zero is asserted.
