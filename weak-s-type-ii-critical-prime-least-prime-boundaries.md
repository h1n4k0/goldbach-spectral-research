# The genuine critical-prime covariance reduces to three signed divisor boundary bands

Let $N$ be even and large, $X=\sqrt N$, $L=\log N$, and retain the actual fixed proportional prime boxes of the [critical-prime setup](weak-s-type-ii-critical-prime-double-centered.md). Thus $P(\alpha)$ has prime inputs in arbitrary hard subintervals of $[.740X,.745X]$ and $[.715X,.720X]$, weight $-E(u,v)\log v$ with $|E|\le1$, $N/2<uv\le y\le9N/16$, and $(uv,N)=1$. All cuts and the selector are fixed at each $N$, independently of the rational point. The actual complementary polynomial is

$$
D(\alpha)=\sum_{\substack{d\in I_0,\ k>t\\N-y\le dk<N/2\\(dk,N)=1,\ (d,k)=1}}
 \mu(d)\mu^2(k)e(\alpha dk),\qquad
I_0=I_d\cap[X,\infty),\quad t\ge N^{.49999}.
\tag{1}
$$

Keep the endpoint conventions of $I_d$ and strict $k>t$. Write $A=\inf I_0\ge X$, $U=\sup I_0$ (possibly infinite); if $I_0$ is empty the assertion is immediate. A constant overall sign of the Type II statistic is immaterial here.

Fix $3/4<\theta<1$, put $Z=\exp(L^\theta)$ and $\gamma=(4\theta-3)/2>0$. Split the actual nonzero terms of (1) by $m=dk$. When $P^-(m)>Z$, retain the entire coefficient in a polynomial $D_{\rm rough}$. Otherwise let $p=P^-(m)\le Z$ and retain in a polynomial $D_{\partial}$ precisely these three disjoint types of original terms:
1. $p\mid d$ and $d/p\notin I_0$;
2. $p\mid k$ and $pd\notin I_0$;
3. $p\mid k$, $pd\in I_0$, and $k/p\le t$.

In each type keep the original coefficient, phase, and every mask in (1). These types are supported respectively in $A\le d\le pA$, $U/p\le d\le U$ (type 2 is empty if $U=\infty$), and $t<k\le pt$. All comparisons with the original endpoints are determined by the displayed exact type rules, not by these containing bands. In particular the entire retained nonrough component lies in three boundary bands of multiplicative width at most $\exp(L^\theta)$.

Let $\mathcal Q=\{q\ \text{prime}:.8X\le q\le .9X\}$, $\mathcal B=[-1/(10N),1/(10N)]$. Write $\mathcal I(P,F)$ for the full critical-shell integral of $P(a/q+\beta)F(a/q+\beta)e(-N(a/q+\beta))$ summed over $q\in\mathcal Q$ and $a=1,\ldots,q-1$, then integrated in $\beta\in\mathcal B$. Write $\mathcal C(P,F)$ for the same integral with both numerator arrays centered by subtracting their separate means over $a\ne0$, as in the critical-prime setup. The result is unconditional:

$$
\begin{split}
 D&=D_{\rm rough}+D_{\partial} \quad\text{as integer Fourier polynomials},\\
 |\mathcal C(P,D)-\mathcal C(P,D_{\partial})|
 +|\mathcal I(P,D)-\mathcal I(P,D_{\partial})|
 &\ll_\theta N L^{-\gamma}.
\end{split}
\tag{2}
$$

For example $\theta=7/8$ gives error $O(N/(\log N)^{1/4})$. No selection in the rational numerators, moduli, or aliases is made. The boundary contribution is still the genuine signed covariance and is not claimed small.

## 1. Exact cancellation at common integer coefficients

Every nonzero term in (1) has squarefree $m$, since $\mu(d)\ne0$, $\mu^2(k)=1$, and $(d,k)=1$. In particular its chosen $p$ divides exactly one of $d,k$, and $(m,N)=1$ ensures that $p$ is a unit modulo $N$. Pair divisors of $m$ not divisible by $p$ with their multiples by $p$ at the same $m$.

If $p\mid d$, the mate is $(d/p,pk)$. Its new $k$ is still $>t$; its new $d$ is smaller and stays below the upper endpoint, so the sole possible failure is the lower endpoint of $I_0$, including its actual convention. This gives type 1. If $p\mid k$, the mate is $(pd,k/p)$. Its $d$ is larger and cannot violate the lower endpoint, but it may violate the upper endpoint (type 2); if not, the only possible failure is $k/p\le t$ (type 3). Both mates preserve the original $m$ window, squarefreeness and all unit and gcd constraints. The prime used for the mate is unchanged because it depends only on $m$.

Whenever both terms are admissible, the $d$ factors have opposite Möbius signs, both $\mu^2(k)$ factors equal one, and the two phases agree for every $\alpha$. Such pairs cancel exactly. This proves the polynomial identity in (2) without separately summing at any modulus. The same fixed-coefficient cancellation implies the identity after either additive centering. It is a statement about matched pairs in the original hard window, not a claim that the polynomial formed by imposing an additional interior cutoff would vanish on its own.

## 2. Uniform rough-tail energy

At squarefree $m$ the absolute value of the original coefficient is at most $\tau(m)=2^{\omega(m)}$. Its square is at most $\tau_4(m)=4^{\omega(m)}$, the four-fold divisor function there; the other $m$ give zero. We show

$$
\sum_{\substack{m\le N\\P^-(m)>Z}}\tau_4(m)
\ll_\theta \frac{N L^3}{(\log Z)^4},
\tag{3}
$$

with $1$ allowed as a rough factor. In an ordered tuple $a,b,c,d$ with product $\le N$, take $d$ to be one of the largest factors; counting each choice gives a factor of at most four in an upper bound. Then $abc\le N^{3/4}$, and for the last factor the upper bound $Y=N/(abc)$ is at least $N^{1/4}$. An elementary upper sieve gives uniformly in this range

$$
\#\{d\le Y:P^-(d)>Z\}\ll_\theta Y/\log Z.
$$

In detail, take the one-dimensional Selberg square from the [sparse-alias sieve, equation (3) at modulus one](weak-s-type-ii-critical-prime-sparse-aliases.md) of level $R=\lfloor Z\rfloor$. It majorizes the rough indicator since a rough integer has no divisor in $[2,R]$. Its main density is $1/G_1\ll1/\log Z$ and the floor error is $O(R^2(1+\log R)^2)$ from the divisor bound on the Selberg weights. The latter is $o(Y/\log Z)$ uniformly because $Z=\exp(L^\theta)$ with fixed $\theta<1$. By the prime Mertens bound, the harmonic sum of the remaining rough variables is bounded by

$$
\sum_{\substack{n\le N\\P^-(n)>Z}}\frac1n
 \le\prod_{Z<p\le N}(1-1/p)^{-1}
 \ll L/\log Z.
$$

Combining the largest-factor split, the upper sieve for $d$ and three such harmonic sums proves (3).

Parseval yields $\int_0^1|D_{\rm rough}(\alpha)|^2\,d\alpha\ll_\theta NL^{3-4\theta}$. On the prime side, the two boxes are disjoint, so each allowed integer $uv$ has a unique ordered representation in them. The prime counts are $O(X/L)$ and the coefficient is at most $L$. Hence $\int_0^1|P(\alpha)|^2\,d\alpha\ll N$, for any of the fixed selectors and hard cuts allowed here.

## 3. Full and double-centered bookkeeping

The critical arcs are disjoint since their center spacing is at least $1/(qq')$ and their combined radii are $1/(5N)$. The $L^2$ energy of both arrays sampled and integrated over the shell is therefore bounded by their ordinary Parseval energies. Subtracting the numerator mean is an orthogonal contraction for each $q,\beta$ and so preserves these upper bounds for the centered arrays. In particular no coprimality with the *arc modulus* $q$ is added to $D_{\rm rough}$. If $q\mid m$ then that term is constant in the numerator variable and is removed exactly by centering; it still belongs to the uncentered polynomial and to the same Parseval bound. Cauchy–Schwarz with $D_{\rm rough}$ now bounds each difference in (2) by $O_\theta(NL^{-\gamma})$.

For the original full $D$, the [two critical constant-mode estimates](weak-s-type-ii-critical-prime-double-centered.md), including the [full-$d$ principal bound](weak-s-type-ii-critical-prime-arcs-full-principal.md), give $\mathcal I(P,D)=\mathcal C(P,D)+O(N\log L/L^2)$. Together with (2) this means the original full shell can also be replaced by the double-centered boundary shell at cost $O_\theta(NL^{-\gamma}+N\log L/L^2)$. This does not assume the earlier constant-mode proofs for $D_{\partial}$ alone under its new least-prime masks.

The reduction uses a least-prime toggle, but unlike the earlier medium-factor, weighted first-moment applications it takes place directly in the exact common coefficient of the one complementary Type II leg, with no logarithmic payload and no averaging over targets $N$. It localizes the genuine dense rational-shell question to the three sharp boundary bands. The common signed covariance on those bands, the entire critical shell, and weak S remain unproved.
