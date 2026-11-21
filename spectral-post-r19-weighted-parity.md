# Standalone follow-up: a weighted parity export for the actual central block

**Scope.** This is a pointwise quantitative reduction for the true Mangoldt weights, and a conditional localized lower bound. It does not prove that the additional diagonal Möbius progression error or the signed parity primitive is small. It does not close Hypothesis S or R and does not handle exterior or crossing blocks.

The method adapts the divisor split of [Huang–Li, arXiv:2005.03811v2](https://arxiv.org/pdf/2005.03811) to central weights and retains the moving endpoint highlighted in [Moya's correction](https://zenodo.org/records/21939906). The quantitative uniformity below is useful for [Round 18](r18-spectral.md), because it applies to all cumulative positions of that actual block, not only to the unweighted global Goldbach sum.

## 1. A uniform central weighted estimate with an explicit remaining input

Assume **global** Dirichlet GRH. Fix $0<\theta<1/2$, $D=\lfloor N^\theta\rfloor$, $Q=\lfloor N/D\rfloor$, $L=\log N$, and write $S=\mathfrak S(N)$. For unit prefixes define
$$
 A_\mu(y)=\sum_{\substack{n\le y;\ n<N\\(n,N)=1}}\Lambda(n)\mu(N-n),\qquad
 A_{\mu,q}(y)=\sum_{\substack{n\le y;\ n<N\\(n,N)=1;\ n\equiv N\bmod q}}
                       \Lambda(n)\mu(N-n).
$$
The nonnegative error parameter is
$$
 \mathcal E_N^{\flat}(Q)=\sum_{\substack{q\le Q\\(q,N)=1;\ \mu^2(q)=1}}
       \sup_{y<N}\left|A_{\mu,q}(y)-A_\mu(y)/\varphi(q)\right|.
$$
Only the residue $N\bmod q$ and squarefree moduli are used, but the maximum over $y$ is essential. No decay is assumed in the identity below.

For any real bounded piecewise $C^1$ weight $W$ supported in $[7/16,9/16]$, with finitely many jumps, put $\|W\|_{\rm BV}=\|W\|_\infty+\operatorname{Var}(W)$ for the zero extension. Define
$$
 G_W=\frac1N\sum_{\substack{n+m=N\\(nm,N)=1}}\Lambda(n)\Lambda(m)W(n/N),
 \qquad
 P_W=\frac1N\sum_{\substack{n<N\\(n,N)=1}}\Lambda(n)\mu(N-n)W(n/N).
$$
For every fixed $A>0$, uniformly in these weights and even $N$,
$$
 G_W=S\left(\int W-P_W\right)
       +O_{\theta,A}\left(\|W\|_{\rm BV}
                    \left[L^{-A}+ \frac{L\,\mathcal E_N^{\flat}(Q)}{N}\right]\right).
                                                                    \tag{1}
$$
The allowed weights include intervals ending at moving upper endpoints of the central block. The individual assumption $\mathcal E_N^{\flat}(Q)\ll_B NL^{-B}$ for all fixed $B$ would be a **new, unproved diagonal Möbius-twisted distribution condition** at $Q\asymp N^{1-\theta}$, not a consequence claimed from GRH.

## 2. Short divisors, with the squarefree condition included

Put $m=N-n$. Replacing $\Lambda(m)$ by $\mu^2(m)\Lambda(m)$ costs $O(N^{-1/2}L^2\|W\|_\infty)$, since only proper prime powers on that side change. For $d\le D$ use
$\Lambda(m)=-\sum_{d\mid m}\mu(d)\log d$ and expand $\mu^2(m)=\sum_{b^2\mid m}\mu(b)$.
Here $b$ is a divisor index. With $B=L^C$, the tail $b>B$ in the raw sum is
$$
 \ll N L^2\|W\|_\infty
       \sum_{b>B,d\le D}\frac{|\mu(b)\mu(d)|}{[b^2,d]}
 \ll N L^3\|W\|_\infty \frac{\log(2B)}{B}.                          \tag{2}
$$
The first inequality counts positive multiples of $[b^2,d]$ by $N/[b^2,d]$ exactly as an upper bound. For squarefree $b,d$, write $c=(b,d)$, $d=cd'$; the summand is $1/(b^2d')$. Sum $d'$ harmonically and $c\mid b$ trivially, then use $\sum_{b>B}d(b)/b^2\ll\log(2B)/B$.

For $b\le B$, the moduli $[b^2,d]\le DB^2$ are coprime to $N$ on the surviving unit terms. The GRH prime number theorem in progressions, followed by summation by parts against $W$, replaces the inner weighted sum by $N\int W/\varphi([b^2,d])$ with total normalized error $O_\theta(DBL^3/\sqrt N\,\|W\|_{\rm BV})$. Removing or restoring prime powers supported at primes dividing $N$ costs $O(L^2)$ per progression and is smaller here. This step uses the GRH for auxiliary conductors, not just those dividing $N$. Extend the resulting Euler model in $b$ to infinity: the same argument as (2) bounds its tail after using $\varphi(q)^{-1}\ll\log(2q)/q$, $[b^2,d]\le b^2D$, and $\sum_{b>B}d(b)\log(2b)/b^2\ll(\log(2B))^2/B$. Choosing $C$ large in terms of $A$ makes these errors $O_{\theta,A}(\|W\|_{\rm BV}L^{-A})$.

For a squarefree $d$ coprime to $N$,
$$
 \sum_{(b,N)=1}\frac{\mu(b)}{\varphi([b^2,d])}
    =A_N\prod_{p\mid d} g(p),\qquad
 A_N=\prod_{p\nmid N}\left(1-\frac1{p(p-1)}\right),\qquad
 g(p)=\frac{p-1}{p^2-p-1}.
$$
In fact the local sum is $1-1/[p(p-1)]$ at $p\nmid d$ and $1/p$ at $p\mid d$. Extend $g$ multiplicatively on squarefree integers. The Dirichlet series $\sum_{(d,N)=1}\mu(d)g(d)d^{-s}$ is $\zeta(1+s)^{-1}H_N(s)$, where the good-prime factors of $H_N$ are $(1-g(p)p^{-s})/(1-p^{-1-s})$ and the bad ones $(1-p^{-1-s})^{-1}$. For fixed $0<\kappa<1/3$, the absolute weighted coefficient sum of $H_N$ at $\Re s=-\kappa$ is $\ll_\kappa\exp(C_\kappa L^\kappa)$. This follows by summing the convergent good-prime differences $g(p)-1/p=O(p^{-3})$, and splitting the bad-prime sum $\sum_{p\mid N}p^{-1+\kappa}$ at $p=L$. The same bound holds for the series with $g(p)=(p-1)^{-1}$, using $O(p^{-2})$ differences instead.

For clarity, these facts imply log-power errors at all fixed positive-power divisor cutoffs, uniformly in $N$. Convolve the absolutely weighted coefficients of $H_N$ with $\mu(m)/m$. On RH,
$\sum_{m>x}\mu(m)/m\ll_\epsilon x^{-1/2+\epsilon}$ and
$\sum_{m>x}\mu(m)\log m/m\ll_\epsilon x^{-1/2+\epsilon}\log(2x)$
by the Mertens bound and partial summation. In the convolution split the $H_N$ index at the cutoff $Y$. The indices $\le Y$ cost $O_\kappa(Y^{-\kappa}\log(2Y)e^{C_\kappa L^\kappa})$ by the weighted sum bound, after choosing $\epsilon$ small so $1/2-\epsilon>\kappa$. The remaining indices cost the same or less: the total sum of $\mu(m)/m$ is zero, and the differentiated total is finite. This checks that the derivative at $s=0$ gives the required truncated $-\mu(d)\log d$ model with $O_A(L^{-A})$ error. Its value is $H_N(0)$. At a good prime,
$\bigl(1-1/[p(p-1)]\bigr)(1-g(p))/(1-1/p)=p(p-2)/(p-1)^2$; at a bad prime the factor is $(1-1/p)^{-1}$. Thus $A_NH_N(0)=S$, and the short contribution in (1) is $S\int W+O_{\theta,A}(\|W\|_{\rm BV}L^{-A})$.

## 3. Long divisors with the exact moving endpoint

For squarefree $m$, set $q=m/d$ on the $d>D$ portion. Then $\mu(d)=\mu(m)\mu(q)$ and **$q<m/D$**. With the zero value of $\mu(m)$ on nonsquarefree inputs, the raw long contribution is exactly
$$
 -\sum_{\substack{q\le Q\\(q,N)=1}}\mu(q)
   \sum_{\substack{n<N-Dq;\ n\equiv N\bmod q\\(n,N)=1}}
        \Lambda(n)\mu(N-n) W(n/N)\log((N-n)/q).                      \tag{3}
$$
Only squarefree $q$ contribute since $\mu(q)$ appears in (3). Thus the endpoint cannot be replaced by $n<N$. The weight $W(n/N)\log((N-n)/q)$, cut at $n<N-Dq$, has supremum plus variation $O(L\|W\|_{\rm BV})$ because $N-n\asymp N$ on its original support. Partial summation using $\mathcal E_N^{\flat}(Q)$ replaces the inner progression by its $1/\varphi(q)$ multiple of the unconditioned unit sum, with normalized error $O(\|W\|_{\rm BV} L\mathcal E_N^{\flat}(Q)/N)$. Now restore the order of summation. The two truncated coefficient sums at $Y=(N-n)/D$ are
$$
 \sum_{\substack{q<Y\\(q,N)=1}}\frac{\mu(q)}{\varphi(q)}=O_A(L^{-A}),\qquad
 -\sum_{\substack{q<Y\\(q,N)=1}}\frac{\mu(q)\log q}{\varphi(q)}
       =S+O_A(L^{-A}).
$$
This is exactly the preceding Euler-product/convolution argument with $g(p)=(p-1)^{-1}$, $Y\asymp N^{1-\theta}$; the strict endpoint costs at most a single term $O(L/\varphi(\lceil Y\rceil))$ if needed. With one extra log power the combined sum weighted by $\log((N-n)/q)$ is $S+O_A(L^{-A})$. Therefore (3) is $-SP_W$ after normalization, up to the error in (1). This proves the weighted identity with the corrected endpoint intact.

## 4. Two quantitative consequences, with different conclusions

For $x\in[1/2,9/16]$, take $W_x(u)=\mathbf1_{(1/2,x]}(u)\sqrt{u(1-u)}$. Its variation is uniformly bounded. The exact central cumulative $F_N(x)$ of Round 18 satisfies
$$
 \sup_x |F_N(x)+SP_{W_x}|
     \ll_{\theta,A} L^{-A}+L\mathcal E_N^{\flat}(Q)/N.                       \tag{4}
$$
In particular the *actual block* in operator norm differs by this same bound from its rank-two parity-primitive model obtained by replacing $F_N$ by $-SP_{W_x}$ in the Round 18 formula. This conclusion is uniform in the sine cutoff, not the $\sqrt K$ loss from bounding individual sine tests separately. If both $\mathcal E_N^{\flat}(Q)$ and the actual parity primitive have the required inverse-log cancellation, (4) certifies a small central block. Neither cancellation is proved here.

For a **fixed nonnegative weight** $W$ of positive integral in the central window, there is a distinct positive lower consequence under diagonal distribution alone. The pointwise inequality $|\mu|\le\mu^2$ and squarefree expansion give
$$
 |P_W|\le \frac1N\sum_{(n,N)=1}\Lambda(n)\mu^2(N-n)W(n/N)
        = A_N\int W +O_A(\|W\|_{\rm BV} L^{-A}).
$$
For the last equality use the same $b$-split as in (2) with no $d$-sum, then the GRH progression estimate; the main constant is $\sum_{(b,N)=1}\mu(b)/\varphi(b^2)=A_N$. The least prime $p_0\nmid N$ is $O(L)$ by Chebyshev's lower bound for $\sum_{p\le y}\log p$, since otherwise all primes up to a sufficiently large multiple of $L$ divide $N$. Thus $1-A_N\ge1/[p_0(p_0-1)]\gg L^{-2}$. If the extra diagonal twisted distribution condition gives $\mathcal E_N^{\flat}(Q)\ll_B NL^{-B}$ for sufficiently large $B$, (1) yields
$$
 G_W\gg_W S L^{-2}.
$$
Removing proper prime powers on either side costs $O_W(N^{-1/2}L^2)$, and each prime-pair summand has weight at most $O_W(L^2)$ before division by $N$. Hence there are $\gg_W SN/L^4$ ordered prime–prime pairs in the support of each such fixed weight for every sufficiently large qualifying even $N$. This is a **localized conditional lower bound**, not the centered estimate $G_W\sim S\int W$ and not a consequence of GRH alone. Endpoint-only diagonal estimates, an untwisted global parity sum, or averages of the Möbius-twisted error cannot be substituted for the uniform moving-cut input in this proof.

**Why squarefree moduli are specified.** If the defining sum for $\mathcal E_N^{\flat}(Q)$ is instead taken over *all* coprime $q\le Q$, call it $\mathcal E_N^{\rm all}(Q)$. For $q=p_0^2\le Q$ with $p_0$ the least prime not dividing $N$, the progression sum $A_{\mu,q}(y)$ vanishes identically since $p_0^2\mid(N-n)$. Consequently $\sup_y|A_\mu(y)|\le\varphi(p_0^2)\mathcal E_N^{\rm all}(Q)\ll L^2\mathcal E_N^{\rm all}(Q)$, and Abel summation also controls $P_W$. This stronger all-moduli hypothesis already supplies the signed parity cancellation if it has sufficient logarithmic saving. Restricting to the squarefree terms suffices for (1) and does not use that shortcut.
