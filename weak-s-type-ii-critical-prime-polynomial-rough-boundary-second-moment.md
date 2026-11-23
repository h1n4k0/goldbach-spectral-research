# An unconditional second moment for all polynomially rough critical-boundary divisors

Keep the original hard central prime box $P$ with arbitrary fixed $|E(u,v)|\le1$, its active gate $N/2<uv\le y\le9N/16$, and the three exact signed branches of the [least-prime boundary reduction](weak-s-type-ii-critical-prime-least-prime-boundaries.md). Thus $N$ is even, $X=\sqrt N$, $L=\log N$, and the true complementary summands are

$$
m=dk,\quad d\in I_0=I_d\cap[X,\infty),\quad k>t\ge N^{.49999},
\quad N-y\le m<N/2,\quad (m,N)=1,
$$

with coefficient $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. Nonzero terms have squarefree $m$. For $p=P^-(m)$ the three exact branches are (1) $p\mid d$ and $d/p$ fails the lower end of $I_0$; (2) $p\mid k$ and $pd$ fails the upper end; (3) $p\mid k$, $pd\in I_0$, and $k/p\le t$. These are disjoint. Endpoint inequalities in the original coefficients are not changed.

Fix $0<\kappa<1/2$ and allow $1\le R<N^\kappa$, $2\le W<N^\kappa$. For squarefree $d$ put

$$
r=r_\kappa(d)=\prod_{\substack{\ell\mid d,\ \ell<N^\kappa\\\ell\ {\rm prime}}}\ell.
$$

Let $D_{\kappa,R,W}$ retain precisely the original signed terms of the three branches for which $p\le W$ and $r\le R$. Thus $d/r>1$ has only polynomially large prime factors, but may be prime or composite, with no bin, ratio, or gap restriction on those prime factors. The (unnormalized) coefficient energy satisfies unconditionally

$$
\int_0^1 |D_{\kappa,R,W}(\alpha)|^2\,d\alpha
 \ll_\kappa \frac{N}{L}(1+\log R)^3(1+\log W).
\tag{1}
$$

In particular, the full and double-centered signed pairings with the genuine $P$, on the **entire** critical shell, satisfy

$$
|\mathcal I(P,D_{\kappa,R,W})|+|\mathcal C(P,D_{\kappa,R,W})|
  \ll_\kappa \frac{N}{\sqrt L}(1+\log R)^{3/2}(1+\log W)^{1/2}.
\tag{2}
$$

For example, for any fixed $A>0$ and $0<\theta<1/3$, one may take $W=L^A$ and $R=\exp(L^\theta)$ and obtain $o(N)$ for every sufficiently large even $N$. More generally $R=\exp(L^\theta)$ and $W=\exp(L^\omega)$ work whenever $\theta,\omega>0$ and $3\theta+\omega<1$. The estimate is uniform in the original cuts and fixed $E$. It needs no zero hypothesis and no averaging over targets.

## 1. First representative, second small part

For each integer $m$ let $T_m$ count its retained nonzero summands without sign. For a fixed $r$ there are only $O_\kappa(1)$ possible complementary divisors $d$ giving such a summand: the remaining part $d/r$ is a subset of the at most $1/\kappa$ distinct prime factors of $m$ at least $N^\kappa$, and $k=m/d$ is determined. Set

$$
U_R(m)=\sum_{\substack{r'\le R,\ r'\mid m}}\mu^2(r').
$$

Then $T_m\ll_\kappa U_R(m)$ and the squared magnitude of the true coefficient of $m$ is at most $T_m^2\ll_\kappa T_mU_R(m)$. This allows one to count a genuine first representative, imposing also $r'\mid m$, without imposing that $r'$ actually occurs in a second representation. The exact signs are not modified in the statement.

Fix a first $r$, a branch, a possible $p$, and $r'\le R$ squarefree. Write $d=r\mathfrak d$; all prime factors of $\mathfrak d$ are at least $N^\kappa$. There is no $\mathfrak d=1$ because $r<N^\kappa<X\le d$. Since $W,R<N^\kappa$, both $p$ and every prime factor of $r'$ are smaller than all prime factors of $\mathfrak d$. Thus $r'\mid m=r\mathfrak d k$ implies $r'/(r',r)\mid k$. In branch 1, $p=P^-(r)$ is fixed by $r$ and the additional condition $p\mid k$ is absent. In branches 2 and 3, $p\mid k$ and $p\nmid r$ on genuine squarefree support. Write $s=1$ in branch 1 and $s=p$ in branches 2/3. For any fixed $\mathfrak d$, the number of $k$ is at most

$$
\left\lfloor\frac{N}{2 r\mathfrak d [s,r'/(r',r)]}\right\rfloor,
\qquad
r[s,r'/(r',r)]=
\begin{cases}
[r,r'],&s=1,\\
[r,r',p],&s=p,\ p\nmid r.
\end{cases}
\tag{3}
$$

Here brackets denote least common multiple. Unit and other sharp restrictions can be dropped for this upper bound only, after the necessary $p\nmid r$ in branches 2/3 and $r'\mid m$ have been used. There is no added floor error.

## 2. The genuine branch forces one harmonic saving

For each fixed $p$ and branch, $d$ belongs to a positive interval of endpoint ratio $O(p)$, **without** restricting a dyad of any of its factors. In branch 1 use $[a,pa]$ with $a=\inf I_0\ge X$, and in branch 2 use $[b/p,b]$ with $b=\sup I_0$ (no upper failure if $b=+\infty$). In branch 3, $t<k\le pt$ and $7N/16\le m<N/2$ imply $7N/(16pt)\le d<N/(2t)$. Intersect each interval with $[X,N^{.50001}/2)$, which is automatic from $k>t$ and $m<N/2$. Therefore $\mathfrak d=d/r$ ranges over an interval of ratio $O(p)$.

Any dyad $[H,2H]$, $H\ge N^\kappa/2$, contains $O_\kappa(H/L)$ integers $h>1$ all of whose prime factors are at least $N^\kappa$. To see this, split off the largest prime factor and write $h=g b$; for fixed $b$, if $2H/b<N^\kappa$ no $g$ is possible, otherwise Chebyshev gives $O_\kappa(H/(bL))$ such primes up to $2H/b$. The reciprocal sum of the possible $b$, including $1$, is at most $\prod_{N^\kappa\le\ell\le N}(1-1/\ell)^{-1}=O_\kappa(1)$ over primes, by Chebyshev and partial summation. Hence the harmonic sum of $\mathfrak d>1$ in the above interval (and at most $N$) is

$$
\sum_{\substack{\mathfrak d=d/r\ {\rm possible}}}\mathfrak d^{-1}
 \ll_\kappa\frac{1+\log p}{L}.
\tag{4}
$$

It includes all possible numbers of large prime factors, and does not distinguish whether a factor exceeds $X$.

Equations (3)–(4) bound the weighted genuine first-representative count, for fixed $r,r',p$ in one branch, by $O_\kappa(N(1+\log p)/(L[r,r']))$ in branch 1 and $O_\kappa(N(1+\log p)/(L[r,r',p]))$ in branches 2/3. The parameters $r$ and $r'$ are squarefree. Their unrestricted supports lie on primes $\ell\le R$, and

$$
\sum_{r,r'\le R}\frac{\mu^2(r)\mu^2(r')}{[r,r']}
\le \prod_{\substack{\ell\le R\\\ell\ {\rm prime}}}(1+3/\ell)
\ll (1+\log R)^3.
\tag{5}
$$

For a fixed $p$, in the other two branches $p\nmid r$; the local $p$ factor in the sum of $1/[r,r',p]$ is at most $2/p$ (two choices for $p\mid r'$, or one if $p>R$). The other prime factors in (5) are unchanged. Branch 1 has only the single $p=P^-(r)\le W$ per first $r$, so its extra factor $1+\log p$ is at most $1+\log W$. In branches 2/3 sum over $p\le W$, using $\sum_{p\le W}(1+\log p)/p\ll1+\log W$ by Chebyshev and partial summation. These bounds for $\sum_m T_mU_R(m)$ prove (1) by ordinary Parseval.

## 3. Ordinary energy gives the actual all-alias signed estimate

The critical arcs are the disjoint intervals $\alpha=a/q+\beta$, $q\in[.8X,.9X]$ prime, $a\not\equiv0\bmod q$, $|\beta|\le1/(10N)$. Restricting to their union contracts ordinary $L^2$, and subtracting the mean over $a\ne0$ at fixed $q,\beta$ is another orthogonal contraction. This handles all shell primes, including any $q\mid N$, without changing the original $(m,N)=1$ condition. The prime box satisfies $\int_0^1|P|^2\ll N$: its two disjoint proportional prime intervals give unique products, $O(N/L^2)$ pairs, and weight $O(L)$ for any fixed selector. Thus Cauchy–Schwarz on the true phase $e(-N\alpha)$ yields (2) for both full and double-centered pairings. The arithmetic gain is in genuine coefficient energy, not a lower bound or a sign assertion for the covariance.

For actual non-giant and composite support, take fixed $\kappa<1/6$, $W,R\ge3$, and large $N=2^j$, with $y=9N/16$, $I_0=[X,2X]$, and $t=N^{.49999}$. Choose primes $g,a,b$ in $[.80,.81]N^{1/6}$, $[.64,.65]N^{1/6}$ and $[.68,.69]N^{1/6}$, and a prime $k\in[.43,.44]X$. Set $d=3gab$, $m=dk$. The prime number theorem supplies such choices. The endpoints give $X<d<1.091X$, $7N/16<m<N/2$, and all factors are distinct odd primes and $N$-units. We have $r_\kappa(d)=3$, $p=3$, $d/3<X$, and $\mu(d)=+1$. This is a true branch-1 term with no giant at least $X$ and not a mere one-large-factor specialization.

For fixed $\kappa$, no bound here is asserted for the actual $r_\kappa(d)>R$ remainder. The previously studied high-$p$ band is separate. The theorem does not control the full critical shell on general exceptional targets and does not prove weak S.
