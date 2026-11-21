# One signed rectangle criterion for a central Goldbach lower bound

**Scope.** This is a conditional arithmetic sufficiency theorem. The required signed rectangle estimate is not proved. No independent smallness condition on the weighted Möbius primitive is needed for this lower bound. Neither GRH nor an operator identification is needed for the implication below, and the implication is not Hypothesis S.

Write $L=\log N$ and $S=\mathfrak S(N)$ for large even $N$. For $y<N$, use the actual unit prefixes
$$
 A_\mu(y)=\sum_{\substack{n\le y\\(n,N)=1}}\Lambda(n)\mu(N-n),\qquad
 A_{\mu,q}(y)=\sum_{\substack{n\le y;\ n\equiv N\bmod q\\(n,N)=1}}
             \Lambda(n)\mu(N-n).
$$
Define the **signed** rectangle total
$$
 \mathcal B(t,y)=\sum_{\substack{q\le t\\(q,N)=1}}
 \mu(q)\left(A_{\mu,q}(y)-\frac{A_\mu(y)}{\varphi(q)}\right).
$$
In particular only squarefree $q$ contribute. Choose a sufficiently large fixed constant $C$, set $D=\lfloor\sqrt N/L^C\rfloor$, $Q=\lfloor N/D\rfloor$, and let
$$
 \mathcal B_* = \sup_{1\le t\le Q,\ 0\le y\le9N/16}|\mathcal B(t,y)|.
$$
If an even $N$ satisfies $\mathcal B_*\ll N/L^{10}$, with fixed constant in the hypothesis, then for every fixed nonnegative bounded-variation $W$ supported on the strict upper central half $(1/2,9/16]$, with $\int W>0$,
$$
 G_W:=\frac1N\sum_{\substack{n+m=N\\(nm,N)=1}}
       \Lambda(n)\Lambda(m)W(n/N)
       \gg_W \frac{S}{p_0},\qquad p_0=\min\{p\text{ prime}:p\nmid N\}.
 \tag{1}
$$
Here sufficiently large $N$ may depend on the fixed constants and the weight. Consequently there are $\gg_W SN/(p_0L^2)$ prime pairs on this central support. In particular $p_0\ll L$ gives $\gg_W SN/L^3$ uniformly among qualifying $N$. If one fixed prime does not divide $N$, the bound is of predicted order $SN/L^2$ even when $S$ is unbounded.

## 1. Signed critical transfer, with only ordinary prime-distribution inputs

Use the true one-variable weighted primitive
$$
 P_W=\frac1N\sum_{\substack{n<N\\(n,N)=1}}
                 \Lambda(n)\mu(N-n)W(n/N).
$$
The exact divisor decomposition gives
$$
 G_W=S(\int W-P_W)
    +O\!\left(\|W\|_{\rm BV}
       [L^{-3}+L^8\mathcal B_*/N]\right).
 \tag{2}
$$
Here $\|W\|_{\rm BV}$ is the supremum plus variation of the zero extension. For the unconditional ordinary-primes step in (2), the details are as follows.

Insert $\mu^2(m)$ at the cost $O(\|W\|_\infty N^{-1/2}L^2)$, $m=N-n$, and write $\Lambda(m)=-\sum_{d\mid m}\mu(d)\log d$. For $d\le D$, expand $\mu^2(m)=\sum_{b^2\mid m}\mu(b)$ and truncate $b$ at $B=L^{12}$. The real and progression-model tails are $O(\|W\|_{\rm BV}L^3(\log(2B))^2/B)$ after normalization: for squarefree $b,d$, write $d=(b,d)d'$, so the modulus is $[b^2,d]=b^2d'$; count positive multiples by $N/[b^2,d]$, and use a harmonic $d'$ sum and the divisor bound for the $b$-tail. For the model one also uses $1/\varphi([b^2,d])\ll(L+\log(2b))/[b^2,d]$.

For $b\le B$ the moduli $\ell=[b^2,d]$ are at most $D B^2$, all reduced at residue $N$. With $b$ fixed, the same $\ell$ has at most $2^{\omega(b)}\le b$ squarefree preimages $d$ since outside primes dividing $b$ all factors are prescribed. Across $b$ the multiplicity is $O(B^2)$; $|\mu(d)\log d|\le L$. Apply the usual **untwisted**, maximal Bombieri–Vinogradov theorem with prescribed saving $L^{-32}$ to the $\ell$'s (take $C$ larger than $24$ plus its logarithmic cutoff exponent). Abel summation in $n$ costs $O(\|W\|_{\rm BV})$. Thus the total normalized progression error is $O(L^{-7}\|W\|_{\rm BV})$. Deleting $n$ supported on prime powers at primes dividing $N$ costs $O(L^2)$ per progression before multiplying by the coefficients; the sum of those losses is power-saving.

The extended squarefree Euler model has factor
$$
 A_N=\prod_{p\nmid N}(1-1/[p(p-1)]),\qquad
 g(p)=\frac{p-1}{p^2-p-1},
$$
so its $d$ coefficients are $A_N\mu(d)g(d)$ on units. The primewise square-completion factors are $1-1/[p(p-1)]$ when $p\nmid d$ and $1/p$ when $p\mid d$, before factoring out $A_N$. The model derivative at $0$ of $\zeta(1+s)^{-1}H_N(s)$ equals $H_N(0)$; multiplying by $A_N$ gives exactly $S$, since at $p\nmid N$ its product factor is $p(p-2)/(p-1)^2$ and at $p\mid N$ is $(1-1/p)^{-1}$. This yields the short main term $S\int W$.

The model tails here can be bounded using the classical zero-free-region Mertens estimate, not RH. For $g(p)$ above or $g(p)=1/(p-1)$, the absolute coefficient sum of $H_N$ at $\Re s=-1/4$ is $\exp(O(L^{1/4}))$, by the good-prime difference $g(p)-1/p=O(p^{-2})$ and by splitting $\sum_{p\mid N}p^{-3/4}$ at $p=L$. In the convolution with $\mu(k)/k$, use $M(x)\ll x\exp(-c\sqrt{\log x})$ and partial summation for the zeroth and logarithmic tails. At a cutoff $X$ of fixed positive-power size in $N$, their tails for coefficient indices $j\le\sqrt X$ are $O(L^{O(1)}e^{-c'\sqrt L})$ against that absolute coefficient sum. The remaining $j>\sqrt X$ are bounded by the power-weighted tail, which stays power-saving even after a $\log j$ factor. Hence both truncated model moments differ from their limits by every fixed inverse log power, uniformly over the cutoffs here.

On the long part $d>D$, switch exactly with $q=m/d$, so the endpoint is $q<m/D$, equivalently $n<N-Dq$, and $\mu(d)=\mu(m)\mu(q)$ on squarefree $m$. After replacing each progression by its $1/\varphi(q)$ unit baseline, the coefficient of $-\Lambda(n)\mu(m)W(n/N)/N$ is
$$
 \sum_{\substack{q<m/D\\(q,N)=1}}
 \frac{\mu(q)}{\varphi(q)}\log(m/q)
       =S+O(L^{-4}).
$$
Indeed the same two Euler moments, now with $g(p)=1/(p-1)$, are zero and $S$ for the zeroth and negative logarithmic sums, and $m/D$ has fixed positive-power size. The strict cutoff at an integer can at worst change one term of size $O(L/\varphi(q))$, which is power-saving here. Thus the baseline gives the $-SP_W$ in (2).

To estimate the remaining signed long discrepancy, split the upper central interval into $K=\lceil L^7\rceil$ equal bins and freeze the moving upper $q$-cut at the left endpoint of each bin. The changed $q$'s are $\asymp Q$ in a range of length $O(Q/K)$, and, for each such $q$, the bin has $O(D/K+1)$ integers in its residue. The baseline counts all integers with multiplier $1/\varphi(q)\ll L/q$, giving at most one extra $L$ in the same bound. Using the trivial bounds $L$ for the Mangoldt factor and kernel log, the total normalized edge cost is
$$
 O\!\left(\|W\|_\infty L^3 (K^{-1}+(Q+D+K)/N)\right)
       = O(\|W\|_\infty L^{-3}).
$$
On each fixed rectangle split $\log(m/q)=\log m-\log q$. Summation by parts in $q$ for the log $q$ and in $n$ for the weight uses $\mathcal B(t,y)$ and costs $O(L\|W\|_{\rm BV}\mathcal B_*)$ per bin; left limits of prefixes keep the strict endpoints. Summing and dividing by $N$ gives the $L^8$ factor in (2). This verifies the critical transfer using classical untwisted prime distribution and no GRH.

## 2. The jump at the least missing prime replaces a separate parity condition

The least missing prime $p_0$ is odd for even $N$, and $p_0\ll L$ by the ordinary Chebyshev lower bound for $\vartheta(x)$: otherwise the product of all primes up to a sufficiently large fixed multiple of $L$ divides $N$. In particular $3\le p_0\le Q$ for large $N$. The difference $\mathcal B(p_0,y)-\mathcal B(p_0-1,y)$ equals **minus**
$$
 A_{\mu,p_0}(y)-A_\mu(y)/\varphi(p_0),
$$
because the added coefficient is $\mu(p_0)=-1$. Therefore this individual discrepancy is bounded by $2\mathcal B_*$ for all the required prefixes. Abel summation against $W$ and the triangle inequality give
$$
 |P_W|\le
 \frac{\varphi(p_0)}{N}
 \sum_{\substack{n\equiv N\bmod p_0\\(n,N)=1}}
     \Lambda(n)\mu^2(N-n)W(n/N)
 +O\!\left(\frac{\varphi(p_0)\|W\|_{\rm BV}\mathcal B_*}{N}\right).
$$
In that progression $\mu^2(N-n)\le1-\mathbf1_{p_0^2\mid(N-n)}$. Both residues $N\bmod p_0$ and $N\bmod p_0^2$ are reduced. The Siegel–Walfisz estimate is uniform in these polylogarithmic moduli and in prefixes (very small endpoints are trivial), and the nonunit powers can again be removed at logarithmic cost. Hence the renormalized main factor above is
$$
 \varphi(p_0)\left[\frac1{\varphi(p_0)}-\frac1{\varphi(p_0^2)}\right]
       =1-\frac1{p_0}.
$$
By requesting sufficient ordinary inverse-log saving, we obtain
$$
 |P_W| \le (1-1/p_0)\int W
       +O\!\left(\|W\|_{\rm BV}[L^{-3}+p_0\mathcal B_*/N]\right).
 \tag{3}
$$
With $\mathcal B_*\ll N/L^{10}$, the error in (2) is $O_W(L^{-2})$, and the error after multiplying (3) by $S$ is $O_W(SL^{-3})$. Both are $o(S/p_0)$, because $S$ is bounded below by an absolute positive constant and $p_0\ll L$; no upper bound on $S$ is needed. Inserting (3) in (2) proves (1). Removing proper prime powers now costs $o(S/p_0)$; each remaining summand has weight at most $\|W\|_\infty L^2$ before normalization. This gives the asserted count.

Thus a genuinely signed rectangle estimate would be enough for central existence without separately showing cancellation of the Möbius primitive. The actual near-square-root pairing results control only specified subsets of that rectangle problem, and do not prove the required $\mathcal B_*$ bound.
