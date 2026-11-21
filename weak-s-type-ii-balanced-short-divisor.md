# Short-divisor cancellation in one exactly balanced central Type II box

**Unconditional, pointwise in $N=2^j$.** Put $X=\sqrt N$, $L=\log N$, and let $I_0,J_0,D_0$ be arbitrary subintervals of $[.740X,.745X]$, $[.715X,.720X]$, $[.445X,.450X]$, respectively. Define

$$
 {\cal A}_N(w)=\sum_{\substack{u\in I_0,\ v\in J_0,\ d\in D_0\\
             u,v,d\ {\rm odd},\ uv\equiv N\bmod d}}
       \mu(u)\mu(d)\mu^2(N-uv)\,w(v).
$$

This is the exact genuine balanced central box at $t=X,\ y=9N/16$ from the [occupied-diagonal note](weak-s-type-ii-exactly-balanced-diagonal.md): the product lies between $.5291N$ and $.5364N$, and the quotient $(N-uv)/d$ exceeds $1.03X$. Units modulo $N$ are exactly oddness, and even $d$ cannot divide $N-uv$. The box satisfies $d>N^{.4975}$ for sufficiently large $N$ and is disjoint from both previously removed $u$-ranges $u\le N^{.265}$ and $N^{.5099}\le u\le N^{.5101}$.

Let $Y=N^{.024}$. Uniformly in all the indicated subintervals, all $1\le M_0\le Y$, and all complex coefficients $|c(1)|\le1,\ |c(r)|\le\Lambda(r)$ for $r\ge2$, the following hold for every fixed $A>0$:

$$
 \begin{split}
 \left|{\cal A}_N\!\left(\sum_{r\le M_0,\ r\mid v}c(r)\right)\right|
   &\ll_A NL^{-A},\\
 |{\cal A}_N(\log v)|&\ll_A NL^{-A}.
 \end{split} \tag{1}
$$

In particular, selecting the conjugate sign in each $r$ gives

$$
 \sum_{r\le Y}\Lambda(r)
      |{\cal A}_N({\bf1}_{r\mid v})|\ll_A NL^{-A}.
 \tag{2}
$$

Writing $V=N^{.2499}$, the exact genuine Vaughan weight in this box thus has the reduction

$$
 {\cal A}_N\bigl(b_{\rm II}(v)\bigr)
   =-\sum_{Y<p\le V,\ p\ {\rm prime}}
                  (\log p)\,{\cal A}_N({\bf1}_{p\mid v})
      +O_A(NL^{-A}),\qquad
 b_{\rm II}(v)=\sum_{r\mid v,\ r>V}\Lambda(r). \tag{3}
$$

This is signed cancellation for short-divisor tests on the true balanced residual, not an estimate for the medium-prime sum in (3), the rest of Type II, or weak S. No GRH or averaging in $N$ is used.

## 1. Freeze just the quotient interval; retain exact integer parity

Only odd $r$ can divide $v$. Work over dyads $R\le r<2R$, $1\le R\le Y$, and partition each into relative blocks with left endpoint $R_0$ and ratio at most $1+\eta$, $\eta=L^{-J_0}$, including a possible shorter last block and the exact $r\le M_0$ cutoff. On one block write $v=r\ell$. Replace the condition $\ell\in J_0/r$ by $\ell\in J_0/R_0$. A mismatch can occur only for $v$ within $O(\eta X+1)$ integers of the two endpoints of $J_0$, independent of the block. For each such $v$ and $d$ there is at most one $u\in I_0$ in a solution: if $(d,v)>1$ the residue is impossible since $d$ is odd, and otherwise the interval length is less than $d$. Because $\sum_{r\mid v}|c(r)|\le1+\log v$, the total absolute freezing error, before completing squares, is $O(LX(\eta X+1))$. Choose $J_0$ in terms of $A$. The enlarged $v$-support is still inside a fixed small neighborhood of the original outer box, so $N-uv\asymp N$, $N/2<uv<9N/16$, and $(N-uv)/d>X$ for any new admissible point once $N$ is large. For $r=1$ the interval is exact without a freezing error.

Complete $\mu^2(m)=\sum_{b^2\mid m}\mu(b)$, $m=N-uv>0$, and retain $b\le B=L^{J_1}$. The tail is supported on $O(N/B)$ integers $m$; per such $m$ its total absolute weight is $O(L\tau(N-m)\tau(m)^2)$. The number of choices of $u,v$ is at most $\tau(N-m)$, of $d$ at most $\tau(m)$, and the summed $r$-weight and square tail cost at most $1+\log v$ and $\tau(m)$ respectively. Thus Hölder with exponents $4,4,2$ and fixed divisor moments gives $O(NL^{C}B^{-1/2})$ with absolute $C$, and $J_1$ may be chosen in terms of $A$. The freezing is compared before square completion, so it has not introduced an unaccounted $B$-factor.

Set $a=ur$ and $\alpha_a=\sum_{ur=a}\mu(u)c(r)$ with the exact odd $u\in I_0$ and current odd $r$-block restrictions. The coefficient bound is $|\alpha_a|\le1+\log a$; the support is at scale $C_0\asymp XR$. The frozen $\ell$-interval has half-integer endpoints $E_0,E_1$ with integer membership unchanged, $E_i=O(X/R)$, $E_1-E_0=O(X/R)$; ignore an interval selecting no integers. Both $b,d$ are odd and squarefree on nonzero coefficients. At fixed $b$, group by $g=(b,d)$ and write $q=[b^2,d]=b^2d/g$. This is injective in $d$ on the group; put $q'=2q$, also at one constant-factor scale $D_1\asymp X b^2/g$. The congruence $a\ell\equiv N\bmod q$ has no solutions unless $(a,q)=1$. On this support, $\ell$ odd and the exact congruence are equivalent to

$$
 \ell\equiv (N+q)\bar a\pmod{q'},\qquad
 \frac{h(N+q)\bar a}{q'}\equiv \frac{hN\bar a}{q'}+\frac h2\pmod1.
 \tag{4}
$$

Indeed $a$ and its inverse modulo $q'$ are odd, and $N$ is even. Thus the parity term is exactly $(-1)^h$, not a moving residue weight in $a,q'$.

## 2. Keep the endpoint difference on low frequencies

Use the exact interval count in the progression (4), with density $(E_1-E_0)/q'$ and the difference of the two sawtooth values. Both half-integer endpoints avoid all jumps. Apply [Vaaler's Theorem 18](https://www.ams.org/journals/bull/1985-12-02/S0273-0979-1985-15349-2/) at degree $H=\lceil R N^\delta\rceil$, $\delta=10^{-3}$. The approximation coefficients $j_h$ are $O(1/|h|)$ for $h\ne0$, and the nonnegative Fejér error majorant has Fourier coefficients $O(1/H)$, including the zero mode. For bounding its endpoint errors use the absolute arithmetic coefficients. The zero Fejér term costs $O(L C_0D_1/H)$, and all dyadic frequency and block multiplicities, as well as $b,g$ multiplicities, are polynomial in $L$. Thus its summed size is $N^{1-\delta+o(1)}$, since $C_0D_1\ll NR B^2$.

For a signed frequency dyad $|h|\asymp K$ (change $h$ to $-h$ when needed), the phase, up to a global sign and the parity factor, is

$$
 e\!\left(hN\bar a/q'-hE/q'\right),
 \qquad E\in[E_0,E_1],\qquad e(z)=e^{2\pi i z}.
$$

Apply [Bettin–Chandee, Theorem 1 and Remark 1](https://arxiv.org/pdf/1502.00769#page=2) to the two separated arithmetic coefficients in $a,q'$ with $(a,q')=1$. The perturbation $f=-hE/q'$ is independent of $a$, with $|\partial_{q'} f|\ll KX/(R(q')^2)\ll KN/(a(q')^2)$; it fits the derivative allowance of Remark 1 with parameter $O(KN)$. The multiplier is therefore $O((1+K/R)^{1/2})$ because $C_0D_1\gg NR$. The arithmetic coefficient norm product is $O(L\sqrt{C_0D_1})$.

For $K\ge R$, one may bound the two approximate sawtooth endpoints separately, with frequency norm $O(K^{-1/2})$. For $K<R$, retain their exact difference **before** applying the trilinear bound:

$$
 j_h\,[e(-hE_1/q')-e(-hE_0/q')]
   =-\frac{2\pi i\,h j_h}{q'}
                \int_{E_0}^{E_1}e(-hE/q')\,dE .
$$

The extra factor $X/q'$ is a bounded coefficient depending only on $q'$, so we may apply the same trilinear estimate uniformly in $E$, then integrate over length $O(X/R)$ using coefficient $h j_h$ with norm $O(\sqrt K)$. This results in the effective frequency norm $O(K^{-1/2}(K/R))$. For each Fejér endpoint the norm $O(\sqrt K/H)$ is likewise at most $O(K^{-1/2}\min(1,K/R))$ since $H\ge R$ and $K\le H$. If a dyad meets $K=R$, split it first. Both types of estimates therefore have the same effective factor $K^{-1/2}\min(1,K/R)$.

The first trilinear term, including the arithmetic and frequency norms, after summing frequency dyads, is bounded up to $N^{o(1)}$ by

$$
 (C_0D_1)^{17/20}(C_0+D_1)^{1/4}
       R^{-3/20}N^{7\delta/20}.
$$

Indeed the remaining frequency maximum is that of $K^{-3/20}\min(1,K/R)(1+K/R)^{1/2}$, bounded by $O(R^{-3/20}N^{7\delta/20})$. The second trilinear term is at most

$$
 (C_0D_1)^{7/8}(C_0+D_1)^{1/8}N^{\delta/2},
$$

since the two $K$ factors from Theorem 1 cancel the $K^{-1/2}$ coefficient factor, leaving $\min(1,K/R)(1+K/R)^{1/2}\ll N^{\delta/2}$. Using $C_0D_1\ll NR B^2,\ C_0+D_1\ll XR B^2,\ R\le N^{.024}$, these are at most $N^{.975+.95(.024)+.35\delta+o(1)}$ and $N^{.9375+.024+\delta/2+o(1)}$, respectively. Both have power savings. Retaining the low-frequency endpoint difference matters numerically; bounding them separately would produce $.975+1.10(.024)>1$ for the first term at small frequency.

## 3. Cancel the signed density, then extract the genuine prime remainder

Discard $a,b$ with $(a,b)>1$, which have no congruence and no density because every $q$ is divisible by $b^2$. For the density at each remaining fixed $a,b$, recombine the $g$-groups. The signed arithmetic factor is

$$
 \sum_{\substack{d\in D_0\\(d,2a)=1}}\frac{\mu(d)}{2[d,b^2]}
   =\frac1{2b^2}
      \sum_{\substack{g\mid b\\(g,2a)=1}}\mu(g)
           \sum_{\substack{e\in D_0/g\\(e,2ab)=1}}\frac{\mu(e)}e .
 \tag{5}
$$

Here $b$ is odd squarefree, and $[b^2,g e]=b^2 e$ on the chosen group with $(e,b)=1$. Use the same unconditional coprime Mertens estimate as in the [earlier left strip, §3](weak-s-type-ii-left-strip.md#3-cancel-the-combined-actual-density): $\sum_{e\le Z,(e,W)=1}\mu(e)/e\ll_D L^{-D}$ uniformly for $Z$ at polynomial scale bounded away from 1 ($\log Z\asymp L$) and $W\le N^{O(1)}$. Briefly, expand the finite inverse Euler product $\prod_{p\mid W}(1-p^{-s})^{-1}$; the weighted coefficient mass at $s=3/4$ is $\exp(O((\log(2W))^{1/4}))$, by splitting prime factors at $\log(2W)$ and bounding all small ones by integers. Convolving with $\mu$, split the Euler coefficient index at $\sqrt Z$: the short part uses classical zero-free-region Mertens on $Z/f\ge\sqrt Z$, and the long part costs $Z^{-1/8}$ times the same coefficient mass and a logarithm. Hence all inverse-logarithmic powers follow. The endpoints of $D_0/g$ remain at scale $X/g$, uniformly $\log(X/g)\asymp L$ for $g\le B$. Thus (5) is $O_D(\tau(b)b^{-2}L^{-D})$. Summing $\alpha_a$ absolutely costs $O(L XR)$, and the density interval has length $O(X/R)$, so the total signed density has any logarithmic saving after choosing $D$ sufficiently large. The result is uniform in subinterval endpoints (differences of two prefixes, with half-integer replacements).

This proves the first estimate in (1), with all square tails and ratio-freezing errors included. Its $r=1$ assertion is uniform when $J_0$ is shortened at any upper endpoint; Abel summation of that prefix against $\log v$ proves the second estimate. The complex coefficient uniformity gives (2) by choosing $c(r)$ aligned with the conjugate sign of each unweighted value. In the identity $b_{\rm II}(v)=\log v-\sum_{r\le V,r\mid v}\Lambda(r)$, remove the two contributions in (1). Remaining proper prime powers $r=p^a>Y,\ a\ge2$ cost only

$$
 O\!\left(N\sum_{\substack{Y<p^a\le V\\a\ge2}}\frac{\log p}{p^a}\right)
 \ll N Y^{-1/2} L^2 .
$$

For each $v,d$ at most one $u$ contributes. The number of $v\le X$ divisible by $p^a$ is at most $X/p^a$, and summing all integers $p\ge Y^{1/a}$ in place of primes gives $O(Y^{-1+1/a})$ for each reciprocal-power sum, with $O(L)$ exponents. Thus the exact signed remainder in (3) contains only medium primes, not prime powers. It has not been bounded here.
