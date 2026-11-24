# The whole actual mixed-strip minor has a power-small exceptional set

**Scope.** This evaluates neither a major density nor a signed additive correlation at a prescribed modulus. It bounds the **whole actual minor at the original polynomial $Q$** for the true above-BV mixed coefficient, unconditionally outside a power-small exceptional set of even targets. In particular a polynomially separated macroscopic gap is allowed if chosen by a fixed common right selector. The theorem does not imply any result on a prescribed exceptional target, powers of two, pointwise weak S or the exterior. It is distinct from the [small-$Q$ almost-all sharp argument](r63-spectral-full-integer-sharp-product.md); the original major complement below really moves with $N$.

Fix $B>B_0>0$, and $Y\le N\le2Y$ even. Write $L=\log N$, $D_N=\sqrt N L^{-B}$, $H_N=\sqrt N L^{-B_0}$, $V_N=[N/3,2N]$, $Q_N=N^{1/1000}$. For squarefree $m$ let $M_{>,N}(m)$ be the exact mixed coefficient of [the above-BV split](r66-spectral-above-bv-strip-deletions.md), before its minus sign in the decomposition. Thus it is the sum over mutually coprime $a,b,c,d$ with $abcd=m$, $abc>H_N$, $D_N<\min(ab,ac)<\sqrt m$, of $\mu(b)\mu(c)(1-2\log(ac)/\log m)$. It is zero on nonsquarefree partners. Fix any common right selector $|\rho_m|\le1$, independent of $N$ throughout $[Y,2Y]$; this may impose either Möbius parity or arbitrary fixed conditions on the actual largest primes of $m$. Optionally impose the actual largest-prime cofactor band of the [ordered calculation](r75-spectral-separated-ordered-major.md): if $p=P^+(m)$, require $D_NN^{\sigma_1}<m/p\le D_NN^{\sigma_2}$ for fixed $0<\sigma_1<\sigma_2<1/10$. The exceptional set is for a fixed common selector, not a supremum over arbitrary varying right weights.

Let $A_N$ be this actual right coefficient, including its literal physical gate $m\in V_N$, and $\mathfrak m_N$ the complement of the exact arcs

$$
        (a,q)=1,\quad q\le Q_N,\quad
                  |\theta-a/q|\le 2Q_N/N .
$$

For every $Y$ sufficiently large, outside $O(Y^{1-3/10000})$ even targets, simultaneously for all half-open central $I\subset(N/2,9N/16]$ and all weights $\omega$ of uniformly bounded supremum plus variation,

$$
 \left|\int_{\mathfrak m_N}P_{I,\omega}(\theta)\widehat A_N(\theta)
                         e(-N\theta)d\theta\right|
                           \ll Y^{1-1/40000}.
 \tag{1}
$$

Here $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$ and $P_{I,\omega}=\sum_{n\in I}\lambda(n)\omega(n)e(n\theta)$. Neither the theorem nor its proof assumes Dirichlet GRH. The constants may depend on the fixed cutoff constants and left variation bound. A fixed finite choice of the stated selectors or bands can be handled by a union of their exceptional sets.

## 1. Freeze only numerical divisor thresholds

Set $\eta=Y^{-1/10000}$ and partition $[Y,2Y]$ into $O(\eta^{-1})$ fixed target intervals of length at most $\eta Y$. On one such interval use its left endpoint $N_0$ to freeze the two thresholds $D_N,H_N$ and the optional two thresholds $D_NN^{\sigma_i}$. Each differs from its frozen value by at most $O(\eta)$ **relatively** by its logarithmic derivative. None of the weights $1-2\log(ac)/\log m$ or of the upper gate $\min(ab,ac)<\sqrt m$ is changed. Let $A^{(0)}$ be this frozen arithmetic coefficient with the fixed $\rho_m$, supported in the fixed ambient interval $[Y/4,5Y]$; the actual $V_N$ gate is still applied separately as a variable physical interval.

Every change between the true and frozen arithmetic coefficients is supported on integers $m$ divisible by some integer $d'$ in one of a bounded number of strips around these thresholds. Indeed $ab,ac,abc$ and, if selected, the true largest-prime cofactor $m/P^+(m)$ are actual divisors of $m$. The strips are of length $O(\eta T+1)$ at scales $T\ge Y^{.49}$ for all sufficiently large $Y$. Strict endpoints and equalities are included in these enclosing strips. The true coefficient and its frozen counterpart are bounded by $O(\tau_4(m))$ on squarefree $m$; each term is bounded and the number of ordered four-factor decompositions is $\tau_4(m)$. Therefore their squared difference, summed over the ambient $m$ range, is at most a constant times

$$
  Y(1+\log Y)^{15}
        \sum_{\text{threshold strips}}\sum_{d'\text{ in strip}}
                                 \frac{\tau_{16}(d')}{d'} .
 \tag{2}
$$

Here $\tau_4(m)^2=\tau_{16}(m)$ on squarefree $m$ and, on a multiple $m=d'v$ in this support, $d',v$ are coprime; use multiplicativity and the elementary $\sum_{v\le x}\tau_{16}(v)\ll x(1+\log(2x))^{15}$. Dropping squarefreeness after this positive bound is harmless. The count of tuples for this divisor estimate follows by first summing the reciprocal product of 15 factors.

For completeness, on an arbitrary strip of length $J$ in $[T/2,2T]$ the divisor sum $\sum\tau_{16}$ is

$$
 O\big(J(1+\log(2T))^{15}+T^{15/16}(1+\log(2T))^{14}\big).
$$

Choose the largest factor in an ordered 16-factor decomposition, at most 16 choices. The product of the other factors is at most $(2T)^{15/16}$. For each of their tuples, the largest-factor count is at most $J$ divided by that product plus an absolute constant, even with hard endpoints. Sum its reciprocal and ordinary 15-factor counts. Consequently (2) is $O(Y^{1-1/10000+o(1)})$ uniformly in $N$, and

$$
 \|\,\widehat A_N-\widehat{A^{(0)}\mathbf1_{V_N}}\,\|_2
                  \ll Y^{(1-1/10000)/2+o(1)} .
 \tag{3}
$$

In particular the physical interval has not been frozen. Also $\|\widehat {A^{(0)}}\|_2^2\ll Y(1+\log Y)^{15}$. With $\|P_{I,\omega}\|_2^2\ll Y(1+\log Y)$, (3) changes the actual minor integral by $O(Y^{1-1/20000+o(1)})$ uniformly, by Cauchy on its actual moving set. This argument is purely a divisor norm bound, not a prime distribution statement on the boundary.

## 2. One common minor and the genuine moving rectangle

Let $\mathcal U$ be the complement of the common arcs of denominator $q\le Y^{1/1000}/2$ and radius $Y^{-999/1000}/2$. These arcs are contained in every genuine major set for $[Y,2Y]$, by comparing both denominators and radii. On the common minor,

$$
 \sup_{\theta\in\mathcal U}\ \sup_{J}
       |P_J(\theta)|\ll Y^{1-1/2000}(1+\log Y)^4,
 \qquad P_J(\theta)=\sum_{n\in J}\lambda(n)e(n\theta),
 \tag{4}
$$

where $J$ is any integer interval in $[1,5Y]$. Indeed use Dirichlet approximation with bound $\lceil4Y^{999/1000}\rceil$ on the denominator. If its denominator were $\le Y^{1/1000}/2$, even the largest permitted approximation error is at most $Y^{-999/1000}/4$, contradicting $\theta\in\mathcal U$. The approximant has $|\theta-a/q|\le q^{-2}$ and $Y^{1/1000}/2<q\le 5Y^{999/1000}$. The standard [Vaughan prime exponential sum bound as proved by Montgomery–Vaughan, Theorem 17.1](https://personal.science.psu.edu/rcv4/Vol2/Vol2.pdf#page=79) then bounds all prime prefixes $x\le5Y$ by $(x/\sqrt q+x^{4/5}+\sqrt{xq})(1+\log Y)^4$ up to an absolute constant. If $q>x$ the $\sqrt{xq}$ term already dominates the trivial Chebyshev bound. Removing prime powers costs $O(\sqrt Y(1+\log Y)^2)$ and taking interval differences proves (4).

For the actual moving cut, form an ambient family of disjoint arcs with all reduced numerators for denominators $q\le 2Y^{1/1000}$ and slow coordinate $|\beta|\le3Y^{-999/1000}$. Different reduced centers have distance at least $1/(4Y^{2/1000})$ on the torus, greater than the sum of their radii. Work inside $\mathcal U$. Then the exact actual minor is $\mathcal U$ minus its intersection with the single actual rectangle

$$
            q\le Q_N,\qquad -2Q_N/N\le\beta\le2Q_N/N ,
$$

where each $q$ cell retains all its reduced numerators. The $q$ coordinate is discrete so its cut is exact. Round only the $\beta$ rectangle inward to cells of width at most $Y^{-3}$, using a fixed dyadic grid of polynomially many cells for the whole slow interval. The omitted at most two grid cells per center cost $O(Y^{2/1000}Y^{-3})$ in measure. The trivial bounds $\|P_{I,\omega}\|_\infty\ll Y$ and $\|\widehat {A^{(0)}\mathbf1_{V_N}}\|_\infty\ll Y(1+\log Y)^3$ make their pointwise integral error negligible even relative to (3). Intersecting all rectangles with the same fixed $\mathcal U$ preserves disjointness, and keeps (4) applicable. No old minor is used as a proxy for the genuine one.

## 3. Maximal Bessel on these actual rectangles

For a fixed frozen target block, use four finite dyadic axes: the left integer interval $J$, the right integer interval $K$ (ultimately $V_N$), the discrete $q$ interval and the $\beta$ grid interval. At each fixed set of levels these are disjoint partitions. Treat the term on the common $\mathcal U$ by the same argument with only its two physical axes. A general rectangle decomposes exactly into $O((1+\log Y)^4)$ canonical rectangles. For fixed such cells $J,K,R$, the functions whose Fourier coefficients we need are

$$
              \mathbf1_{\mathcal U\cap R}P_J\widehat {A^{(0)}\mathbf1_K}.
$$

At any fixed choice of levels, by Cauchy--Schwarz across the decomposition, then summing over all canonical choices and using Parseval, their squared Fourier-coefficient sum is controlled by their summed torus energies. On $\mathcal U$, at each fixed left level,

$$
 \sum_J|P_J(\theta)|^2
        \le \big(\sup_J|P_J(\theta)|\big)\sum_J|P_J(\theta)|
        \ll Y^{2-1/2000}(1+\log Y)^4,
$$

since the intervals are disjoint and $\sum_{n\le5Y}\lambda(n)\ll Y$. The right intervals are disjoint in integer support, so $\sum_K\|\widehat {A^{(0)}\mathbf1_K}\|_2^2=\|\widehat {A^{(0)}}\|_2^2$. The arc rectangles at these levels are disjoint on the torus. These three facts make the total energy per level at most $Y^{3-1/2000}(1+\log Y)^{19}$. Summing the finitely many levels and the decomposition cost contributes only fixed further powers of $\log Y$. Thus the sum over all integer Fourier indices $N$ of the supremum of the squared frozen integrals, over the complete moving rectangles and physical intervals, is

$$
                           O(Y^{3-1/2000+o(1)}).
 \tag{5}
$$

The unrounded actual $q$ threshold and the rounded slow interval are among these choices. At fixed $N$, bounded-variation partial summation in the left integer coefficient bounds the weighted integral by the supremum over left hard prefixes times $\|\omega\|_\infty+\operatorname{Var}\omega$. This inserts the actual $\omega$ in (5) with a uniform fixed constant; no arbitrary target-dependent multiplier was used on the right.

The $O(Y^{1/10000})$ target blocks give total squared supremum budget $O(Y^{3-4/10000+o(1)})$ on the retained targets before deterministic errors. Markov at $Y^{1-1/40000}$ excluded at most $O(Y^{1-35/100000+o(1)})$, which is $O(Y^{1-3/10000})$ for large $Y$. Finally (3) and the slow-coordinate rounding errors are uniformly smaller than this threshold. Restoring them proves (1) for the true $D_N,H_N$, the exact physical support including optional actual cofactor eligibility, and the genuine original minor. The bound contains no estimate on the completed major, no small exceptional set within sparse fixed-radical families, and no pointwise weak-S implication.
