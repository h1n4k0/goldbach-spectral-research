# An unmasked zero-numerator base that exceeds the target scale

Use the genuine coefficients of the [critical-prime shell](weak-s-type-ii-critical-prime-least-prime-boundaries.md) with $N=2^j$, $X=\sqrt N$, $L=\log N$, and $e(z)=\exp(2\pi i z)$. Take the unselected prime leg $E=1$ in the two full original hard prime boxes $[.740X,.745X]$ and $[.715X,.720X]$: its coefficient is $P_{uv}=-\log v$ on the true prime pairs and their original gates. Fix $y=9N/16$, $t=N^{.49999}$ and write $J=[7N/16,N/2)$. The endpoint $T$ in $I_d=[X,T]$ is allowed to move in $[X,\sqrt2 X]$. The complementary leg is the complete **unmasked** coefficient

$$
 D_m=\sum_{\substack{dk=m,\ X\le d\le T,\ k>t\\
                     m\in J,\ (dk,N)=1,\ (d,k)=1}}
                   \mu(d)\mu^2(k).
$$

No support selector or auxiliary multiplier is imposed on either leg.

Write $\mathcal Q=[.8X,.9X]\cap\mathbb P$, $\mathcal B=[-1/(10N),1/(10N)]$, and let $P(\alpha)$ and $D(\alpha)$ denote the integer Fourier polynomials of the respective coefficients. Define the signed offset convolution $U(h)=\sum_{n+m=N+h}P_nD_m$ and $A(h)=\operatorname{sinc}(h/(5N))U(h)$, where $\operatorname{sinc}(z)=\sin(\pi z)/(\pi z)$ with value one at zero. Use the exact zero-numerator base and actual hit sum

$$
 Z_N=\frac{|\mathcal Q|}{5N}\sum_{h\in\mathbb Z}A(h)
     =|\mathcal Q|\int_{\mathcal B}P(\beta)D(\beta)e(-N\beta)\,d\beta,
 \qquad
 H_N^{\rm hit}=\frac{1}{5N}\sum_{q\in\mathcal Q}q\sum_{b\in\mathbb Z}A(qb).
$$

These are the two pieces of the full signed shell, whose exact difference is $\mathcal I_N=H_N^{\rm hit}-Z_N$. In particular, $Z_N$ is not a unit-centered residue average.

**Theorem.** Unconditionally, for infinitely many dyadic targets $N=2^j$ there is an admissible $T=T_N\in[X,\sqrt2 X]$ for which

$$
 |Z_N|\gg \frac{N^{5/4}}{L^2},\qquad H_N^{\rm hit}=Z_N+O(N).
 \tag{1}
$$

On this same sequence the raw and literal block-compensated squared methods both fail for actual unselected coefficients:

$$
 \sum_{h\in\mathcal H_N}|U(h)|^2\gg \frac{N^{5/2}}{L^3},
 \qquad
 \sum_{\substack{h\in\mathcal H_N\\h\ {\rm odd}}}
  \left|A(h)-\frac1{q(h)}\sum_{r=0}^{q(h)-1}A(h+r)\right|^2
     \gg \frac{N^{5/2}}{L^3}.
 \tag{2}
$$

Here $\mathcal H_N=\{h\in\mathbb Z:0<|h|<N/20,\ \exists q\in\mathcal Q,\ q\mid h\}$, and $q(h)$ is its unique such divisor. These are not lower bounds for $\mathcal I_N$. The second bound uses odd-start blocks in the literal partition into consecutive integers; it does **not** prove failure for the unmasked parity-aware partition into even offsets.

## 1. A squarefree count uniform under the actual coprimality condition

Put $\Phi(x)=(\log x)^{3/5}(\log\log x)^{-1/5}$ for all sufficiently large $x$. The effective ordinary Mertens bound $M(x)=\sum_{a\le x}\mu(a)\ll x\exp(-c\Phi(x))$ follows, for example, from [Lee and Leong, Theorem 2.2, (23)](https://arxiv.org/html/2208.06141v5#S2.SS2). First derive a squarefree count from it. In $Q(x)=\sum_{a\le\sqrt x}\mu(a)\lfloor x/a^2\rfloor$ split at $z=\sqrt x\exp(-\eta\Phi(x))$ for a small fixed $\eta>0$. The floors at $a\le z$ cost $O(z)$. The remainder is exactly

$$
 \sum_{b\le x/z^2}\big(M(\sqrt{x/b})-M(z)\big).
$$

The endpoints in each Mertens term are at least $z$ and at most $\sqrt x$, so the exponential saving is uniform, say $\exp(-c_1\Phi(x))$ with $c_1>0$ independent of the chosen sufficiently small fixed $\eta$. Since $\sum_{b\le x/z^2}b^{-1/2}\ll\sqrt x/z$, the remainder costs $O((x/z)\exp(-c_1\Phi(x)))$. By partial summation the continuous tail $x\sum_{a>z}\mu(a)/a^2$ costs the same, using the eventual monotonicity of $\Phi$. Taking $0<\eta<c_1$ gives

$$
 Q(x)=x/\zeta(2)+O(\sqrt x\exp(-c_2\Phi(x))).
 \tag{3}
$$

We will also use $Q(u)=u/\zeta(2)+O(\sqrt u)$ for all real $u>0$. The latter follows by elementary floor removal and extension of the main sum for $u\ge1$, and is immediate for $u<1$.

For a positive integer $M_0\ll X$ and $x\asymp X$, impose $(n,M_0)=1$ in this squarefree count. The exact convolution is $\mu^2(n)\mathbf1_{(n,M_0)=1}=(\mu^2*\vartheta_{M_0})(n)$, where the correcting Euler factor is $(1+p^{-s})^{-1}$ at $p\mid M_0$ and is one otherwise. In particular, for fixed $0<\sigma<1$,

$$
 \sum_{a\ge1}\frac{|\vartheta_{M_0}(a)|}{a^\sigma}
 =\prod_{p\mid M_0}(1-p^{-\sigma})^{-1}
 \le \exp\big(O_\sigma((\log X)^{1-\sigma})\big).
$$

To see the uniform bound, split the primes at $\log X$. Below the split sum $p^{-\sigma}$ over all integers in that range; above it there are $O(\log X/\log\log X)$ divisors which are primes, each contributing at most $(\log X)^{-\sigma}$. The logarithm of the product is bounded by a fixed multiple of this sum.

Apply (3) termwise to $Q(x/a)$ for $a\le\sqrt x$. The factor from the corresponding absolute convolution sum at $\sigma=1/2$ is absorbed by the saving since $(\log X)^{1/2}=o(\Phi(X))$. For $a>\sqrt x$ use the elementary square-root error, including the terms $a>x$ where the count is zero. At any fixed $0<\delta<1/2$ this tail costs

$$
 \sqrt x\sum_{a>\sqrt x}|\vartheta_{M_0}(a)|a^{-1/2}
 \ll_\delta \sqrt x\, x^{-\delta/2}
          \exp\big(O_\delta((\log X)^{1/2+\delta})\big).
$$

It is smaller than the error from the first range. The main sum over all $a$ gives exactly the local Euler density. Thus, uniformly for these $x,M_0$,

$$
 \sum_{\substack{n\le x\\(n,M_0)=1}}\mu^2(n)
       =C(M_0)x+O(\sqrt X\exp(-c_3\Phi(X))),\qquad
 C(M_0)=\frac1{\zeta(2)}\prod_{p\mid M_0}\frac{p}{p+1}.
 \tag{4}
$$

The same endpoint errors apply to sharp differences of prefixes: changing whether an integer endpoint is included costs at most one.

## 2. The exact leading coefficient of the true base

For $X\le d\le T\le\sqrt2 X$ and $dk\in J$, one has $k\ge (7/(16\sqrt2))X>t$ for sufficiently large $N$. So the lower $k$ gate is genuinely inactive on this specific region. Since $N$ is a power of two, the unit and relative coprimality conditions for an odd $d$ reduce precisely to $(k,2d)=1$. The odd $d$ condition is retained.

For each permitted $d$, apply (4) with $M_0=2d$ and the interval $J/d$. Its endpoints are $\asymp X$, uniformly in $d$, and the total variation of $e(\beta dk)$ on it is $O(1)$ for $\beta\in\mathcal B$. Partial summation, with the strict upper endpoint of $J$, gives the corresponding main integral $C(2d)d^{-1}\int_J e(\beta z)\,dz$ plus $O(\sqrt X\exp(-c_3\Phi(X)))$. Define

$$
 f(d)=\mu(d)\mathbf1_{2\nmid d}\prod_{p\mid d}\frac{p}{p+1},
 \qquad S_X(T)=\sum_{X\le d\le T}\frac{f(d)}d,\qquad
 G_N(\beta)=\int_J e(\beta z)\,dz.
$$

Summing over the actual $d$ yields, uniformly in the two sharp endpoints and $\beta\in\mathcal B$,

$$
 D(\beta)=C(2)G_N(\beta)S_X(T)+O\big(X^{3/2}\exp(-c_3\Phi(X))\big).
 \tag{5}
$$

There is no replacement of $D_m$ by a model on the critical arcs. The approximation (5) is used only in the exact central integral defining $Z_N$.

The two prime boxes are disjoint, so each product corresponds to a unique pair. The prime product gate is automatic for these boxes and the chosen $y$; all their primes are odd and thus units. The prime number theorem gives $\sum_n |P_n|\asymp N/L$ and $|\mathcal Q|\asymp X/L$. On inserting (5) into $Z_N$, the exact $\beta$ integral of the main term is

$$
 \frac{|\mathcal Q|C(2)}{5N}\,S_X(T)
       \sum_n P_n\int_J\operatorname{sinc}\big((n+z-N)/(5N)\big)\,dz.
 \tag{6}
$$

The sinc is bounded above and below by positive constants on this physical range, and all nonzero $P_n$ have the same negative sign. Consequently the coefficient of $S_X(T)$ in (6) has magnitude $\asymp N^{3/2}/L^2$. The contribution of the error in (5) to $Z_N$ is $O(N^{5/4}L^{-2}\exp(-c_3\Phi(X)))$: indeed multiply by a bound $O(N/L)$ for $P$, the arc length $1/(5N)$ and $|\mathcal Q|\ll X/L$. It follows that $|S_X(T)|\gg X^{-1/2}$ on a sequence suffices for the first inequality of (1).

## 3. A nonzero pole forces the signed harmonic witness

For $\operatorname{Re}s>1$, the Dirichlet series of the actual $f$ is

$$
 \sum_{d\ge1}\frac{f(d)}{d^s}
  =\frac{H(s)}{\zeta(s)},\qquad
 H(s)=(1-2^{-s})^{-1}
      \prod_{p>2}\left(1+\frac{p^{-s}}{(p+1)(1-p^{-s})}\right).
 \tag{7}
$$

The correction $H$ is holomorphic and nonvanishing on $\operatorname{Re}s>0$. In fact each odd-prime local factor is $(1-(p/(p+1))p^{-s})/(1-p^{-s})$, with nonzero numerator and denominator there, and the differences of the factors from one sum locally absolutely. The factor at $2$ is also holomorphic and nonvanishing there. Therefore the meromorphic series in (7) has a pole of order at least one at a fixed critical-line zero $s_0=1/2+i\gamma$ of $\zeta$; the existence of such a zero is unconditional, for example by [Hardy and Littlewood, §4.1](https://projecteuclid.org/journals/acta-mathematica/volume-41/issue-none/Contributions-to-the-theory-of-the-riemann-zeta-function-and/10.1007/BF02422942.pdf#page=59).

In particular $M_f(x)=\sum_{d\le x}f(d)$ cannot be $o(\sqrt x)$. If it were, the integral $s\int_1^\infty M_f(x)x^{-s-1}\,dx$ would be holomorphic for $\operatorname{Re}s>1/2$ and agree with (7) there by uniqueness of meromorphic continuation. At $s=s_0+\delta$ with $\delta>0$, multiplying this integral by $\delta$ would give a quantity tending to zero: on any fixed initial interval this follows from the factor $\delta$, and beyond an arbitrary sufficiently large initial point one uses $|M_f(x)|\le\epsilon\sqrt x$ and $\delta\int_1^\infty x^{-1-\delta}\,dx=1$. This contradicts the pole at $s_0$, whether simple or multiple.

Now suppose the quantity $\sup_{X\le T\le\sqrt2 X}|S_X(T)|$ were $o(X^{-1/2})$ for $X=2^{j/2}$ as $j\to\infty$. Partial summation on each such dyad would give the uniform $o(\sqrt X)$ bound for $\sum_{X\le d\le T}f(d)$ over its prefixes. These consecutive dyads cover all sufficiently large reals; use half-open intervals at common boundaries, changing the bound by at most one when necessary. Since the square roots of the earlier endpoints form a geometric series, summing the prefix bound and all completed dyadic bounds would yield $M_f(x)=o(\sqrt x)$ for all real $x$. More explicitly, for any $\epsilon>0$ discard finitely many initial dyads and use an $\epsilon\sqrt X$ bound on each remaining dyad; their cumulative bound is $O(\epsilon\sqrt x)$. This is the contradiction just established. Thus on infinitely many $X=2^{j/2}$ there is a genuine $T=T_N\in[X,\sqrt2 X]$ with $|S_X(T_N)|\gg X^{-1/2}$. Equations (5) and (6) prove the asserted lower bound for the base. No endpoint $T/X$ independent of $N$ or assertion for all $j$ is needed.

## 4. What this forces on actual hits and on literal block squares

By finite numerator orthogonality and exact integration on $\mathcal B$, the signed shell equals $H_N^{\rm hit}-Z_N$. Its absolute value is $O(N)$: the reduced arcs at $a/q$ for $a\ne0$ are disjoint modulo one, since distinct centers are separated by $\gg1/N$ with spacing at least $1/(.81N)$ across distinct $q$ and arc lengths $1/(5N)$. Apply Cauchy on their union and use the full circle energies $\int_0^1|P|^2,\int_0^1|D|^2\ll N$. The prime bound follows from unique factorization and the prime counts; the complementary bound is the [uniform hard-interval ordinary energy](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy). This proves the second assertion of (1). In particular the unmasked signed hit sum and base cancel to relative accuracy $O(L^2N^{-1/4})$ on this sequence, but an $o(N)$ absolute bound for their difference is not obtained.

The physical support is $|h|\le .037N$; a nonzero contributing block center is therefore in $|h|<N/20$ for large $N$. Since two distinct primes in $\mathcal Q$ have product at least $.64N$, a nonzero center can belong to only one $q$. The number of possible centers is $|\mathcal H_N|\ll N/L$, just by summing the number of multiples in that range over $q$. The repeated $h=0$ weighted part of $H_N^{\rm hit}$ costs only $O(N/L)$, since $|A(0)|\ll N$ by the two ordinary coefficient energies and $\sum_{q\in\mathcal Q}q\ll N/L$. The remaining hits therefore have sum of magnitude $\gg N^{5/4}/L^2$ along the witness sequence. Cauchy gives

$$
 \left|\frac1{5N}\sum_{h\in\mathcal H_N}q(h)A(h)\right|^2
   \ll L^{-1}\sum_{h\in\mathcal H_N}|A(h)|^2
   \le L^{-1}\sum_{h\in\mathcal H_N}|U(h)|^2 .
$$

This is the first inequality of (2).

For the second inequality, the [signed odd-start identity](weak-s-type-ii-critical-prime-parity-compensation.md#1-exact-compensation-and-a-signed-estimate-on-its-odd-blocks) applies to these true unselected primes and the unmasked $D$. In the literal partition into blocks of $q$ consecutive integers it gives

$$
 \frac1{5N}\sum_{q\in\mathcal Q}q\sum_{b\ {\rm odd}}
       \left(A(qb)-q^{-1}\sum_{r=0}^{q-1}A(qb+r)\right)
 =-\tfrac12 Z_N+O(N/\sqrt L).
$$

All contributing starts here are odd, nonzero and uniquely assigned to their $q(h)$. Their signed sum has magnitude $\gg N^{5/4}/L^2$ by (1). Cauchy with the same count of centers proves the second inequality of (2). Both bounds exceed the sufficient squared scale $o(N^2L)$, without using an artificial product mask. The second lower bound specifically uses the forced parity of the original coefficients: $A(h)=0$ at the odd starts themselves. It cannot be transported to the parity-aware blocks $A(2qb)-q^{-1}\sum_{r=0}^{q-1}A(2qb+2r)$ by equality of their signed totals; those blocks are distinct before squaring. The unmasked even-lattice compensated moment and the signed full shell at the target $o(N)$ scale remain open.
