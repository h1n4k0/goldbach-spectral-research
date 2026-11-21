# Full Dirichlet widths up to the logarithmic square-root cutoff

Continue the exact centered transform of [R32](r32-source-double-giant-major-arcs.md), with global Dirichlet GRH, fixed $0<\rho<1/2$, $0<\kappa\le1/2000$, all sufficiently large even $N$, $L=\log N$, $S=\mathfrak S(N)$, and $I_0=[\rho N,(1-\rho)N]$. Write $\mathcal Q=\{q\text{ prime}:N^\kappa\le q\le N^{1/2-\kappa},\ (q,N)=1\}$. Put $z=\kappa L/1000$, $W=\prod_{\ell\le z,\,\ell\nmid N}\ell$ over primes, $M=\operatorname{rad}(NW)$, and $K=M/\varphi(M)$. For any hard interval $I\subseteq I_0$ with its original endpoint convention,

$$
 F_I(\alpha)=\sum_{\substack{q\in\mathcal Q,\ p\ge1\\qp\in I,\ (p,N)=1}}
       (\log q)\left({\bf1}_{p\ {\rm prime}}-\frac{K}{\log p}{\bf1}_{(p,W)=1}\right)e(\alpha qp),
 \qquad e(x)=e^{2\pi ix}.
$$

The exact same-target covariance is $\int_{\mathbb T}F_I F_{I_0}e(-N\alpha)$, where the second factor stays fixed independently of $I$.

**Theorem.** Put $Q_*=\lfloor\sqrt N\rfloor$, $R=\lfloor Q_* L^{-200}\rfloor$, and $B_r=1/(rQ_*)$. Uniformly over moving hard $I\subseteq I_0$, the genuine signed integral satisfies

$$
 \left|\int_{\mathfrak D}F_I(\alpha)F_{I_0}(\alpha)e(-N\alpha)\,d\alpha\right|
 \ll_{\rho,\kappa} \frac{SN}{L\log L},
 \qquad
 \mathfrak D=\bigcup_{\substack{1\le r\le R\\a\bmod r,\ (a,r)=1}}
              \{\alpha:\|\alpha-a/r\|\le B_r\}. \tag{1}
$$

The arcs are pairwise disjoint: the sum of the widths times $rs$ is $(r+s)/Q_*\le2L^{-200}<1$. The set contains the exact R32 major arcs and [R33 cores](r33-source-signed-minor-rational-cores.md) for sufficiently large $N$ at fixed $\kappa$ (since $\lfloor N^{1/2-\kappa/4}\rfloor<R$). Their disjoint signed contributions can be subtracted, so (1) also holds on the new part relative to their union. This family and the separate [constant-width arcs](r34-source-wide-rational-cores.md) are not nested: the present family includes smaller denominators, while the constant-width arcs are wider around some of the same reduced fractions. No signed estimate over the union is inferred. By Dirichlet approximation, every $\alpha\notin\mathfrak D$ can only have square-root Dirichlet approximants with denominator $Q_*L^{-200}<r\le Q_*$, in the sense of distance at most $1/(rQ_*)$. The signed contribution of that remaining set is not bounded here. There is no pointwise hypothesis on Goldbach or the full weak-S operator in (1).

## 1. The exact main profile and smoothing loss

The R32 CRT computation is valid on any reduced rational arc here. Set $r_q=r/(r,q)$, $\Delta_N(d)=\mu(d){\bf1}_{d\nmid M}/\varphi(d)$ and

$$
 G_r(t)=\sum_{q\in\mathcal Q}\frac{\log q}{q\log(t/q)}\Delta_N(r_q),
 \qquad M_{I,r}(\beta)=\int_I G_r(t)e(\beta t)\,dt .
$$

The prime coefficient in the reduced phase $e(a q p/r)$ is $\mu(r_q)/\varphi(r_q)$; every central true prime $p$ exceeds $r$. The synthetic coefficient is $K\sum_{h\mid M,\ r_q\mid h}\mu(h)/h$, equal to the prime coefficient when $r_q\mid M$ and zero otherwise. Both are independent of the reduced numerator. Also $|G_r|\ll_\rho1/\varphi(r)$ in a fixed enlarged central interval, using $\sum_q\log q/q\ll L$ for nondividing $q$ and $\varphi(r)/\varphi(r_q)\le q$, $\sum_{q\mid r}\log q\le\log r$ for the rest.

Smooth the hard support in $t/N$ within $\epsilon=L^{-40}$ of its two endpoints by a $[0,1]$-valued bump convolution, obtaining $w_I(t/N)$ with derivative bounds $O_{\rho,j}(L^{40j})$ and support in $[\rho/2,1-\rho/2]$. Singleton endpoint atoms are included in the discrepancy. For the corresponding $F_w$ the coefficient change is on at most $O(\epsilon N+1)$ integers; each has at most $O_\kappa(1)$ eligible prime divisors, and each coefficient is $O_{\rho,\kappa}(L^2)$ since $K\ll L^2$. Hence $\|F_I-F_w\|_{L^2(\mathbb T)}^2\ll(\epsilon N+1)L^4$ exactly, without requiring a prime count on the removed edge. Real Plancherel similarly bounds the model edge energy by $\epsilon N\sum_{r\le R}O_\rho(1/\varphi(r))\ll \epsilon N L^2$. Also $\|M_{I,\cdot}\|_{L^2(\mathfrak D)}^2\ll NL^2$.

## 2. An adaptive Mellin cutoff for the prime residual

On each cofactor dyad $q\in(U,2U]$, put $P=N/U$ and fix a smooth $V(p/P)$ supported in $[\rho/8,2]$ and equal to one whenever the smoothed physical weight is nonzero. Use the log transform

$$
 A_\beta(x)=w_I(e^x)e(\beta N e^x),\qquad
 \widehat A_\beta(\tau)=\int A_\beta(x)e^{-i\tau x}\,dx.
$$

Mellin separation of $w_I(qp/N)e(\beta qp)$ gives twists $(q/U)^{i\tau}$, $(p/P)^{i\tau}$ because $UP=N$. For $|\beta|\le B_r$ choose $T_r=100NB_r$. Uniformly for $|\tau|\ge T_r$,

$$
 |\widehat A_\beta(\tau)|\ll_{\rho,j}L^{40j}|\tau|^{-j}.
 \tag{2}
$$

This is not the estimate obtained by differentiating the entire oscillatory exponential as an amplitude. Its phase is $2\pi\beta Ne^x-\tau x$. Its derivative has magnitude $\gg|\tau|$ on the support, and each higher phase derivative is $O_{\rho,j}(|\tau|)$. Repeated integration by parts with the reciprocal phase derivative gains $|\tau|^{-1}$ at each step with only the stated amplitude-derivative losses. In particular $T_r\gg L^{200}$ on all these arcs, so the integral of this tail is $O_\rho(L^{-100})$ with a fixed choice of $j$.

For any separated scalar error $D(\tau)$ on $[-T_r,T_r]$,

$$
 \int_{|\beta|\le B_r}
 \left|\frac1{2\pi}\int_{-T_r}^{T_r}\widehat A_\beta(\tau)D(\tau)\,d\tau\right|^2d\beta
 \ll_\rho N^{-1}\int_{-T_r}^{T_r}|D(\tau)|^2d\tau .
 \tag{3}
$$

To see this, insert $\widehat A_\beta(\tau)=\int w_I(u)e(\beta Nu)u^{-i\tau}\,du/u$, apply full real Plancherel in $\beta$, and then log-coordinate Plancherel in $\tau$ with $u\asymp_\rho1$. Thus an adaptive height costs $T_r$, not $T_r^2$.

Uniformly for $|\tau|\le N^3$, prime sums with fixed weight $V(p/P)(p/P)^{i\tau}$ have character discrepancy $O_\rho(\sqrt P L^2)$ after subtracting the principal integral of $V(t/P)(t/P)^{i\tau}/\log t$. Here one uses the smooth [Dirichlet explicit formula (Kowalski, Theorem C.5.6)](https://people.math.ethz.ch/~kowalski/probabilistic-number-theory.pdf): insert $\Lambda(n)V(n/P)(n/P)^{i\tau}/\log n$, with Mellin factor $\widetilde V_{\log}(s+i\tau)$, $V_{\log}(u)=V(u)/\log(Pu)$. It is $O_{\rho,j}(L^{-1}(1+|\Im s+\tau|)^{-j})$ in the strip $-1/2\le\Re s\le2$. Shift the primitive character logarithmic derivative to $-1/2$; its pole gives the indicated integral, the unit-bin zero count $O(\log(d(2+|v|)))$ and GRH bound the shifted zero sum by $O_\rho(\sqrt P L^2)$, and the left contour by the functional equation is smaller. The possible zero at 0, prime powers, inducing Euler factors, and prime divisors of $N$ cost within this error. In particular only the polynomial logarithm of $|\tau|$, not a power of $|\tau|$, is used.

For cofactor units mod $r$, character inversion of $e(aqp/r)$ and numerator Parseval give a squared discrepancy at each separated $\tau$ (summed over reduced $a$) at most $O_\rho(N(r+U)L^8)$. Indeed complete Gauss coefficients are at most $\sqrt r$ also for induced characters, and ordinary character orthogonality bounds the mean squared cofactor character sum by $O(L^2U(1+U/r))$, independent of the twist of modulus one. This is the same character computation as in R33, now with a smooth shifted prime estimate. The shared $q\mid r$ contributions use modulus $r/q$, then additive Parseval lifted to $a\bmod r$; their squared discrepancy is $O_{\rho,\kappa}(rN^{1-\kappa}L^8)$ after the $O_\kappa(1)$ possible choices.

By (3), the prime error on $|\tau|\le T_r$ summed over denominators has per-dyad energy

$$
 \ll_{\rho,\kappa} L^8\sum_{r\le R}T_r(r+U)
       +L^8 N^{-\kappa}\sum_{r\le R}T_r r
 \ll_{\rho,\kappa} L^8\frac N{Q_*}(R+U L+N^{-\kappa}R).
$$

Summing the logarithmically many dyads in norm costs at most another $L^2$. Since $R\ll\sqrt N/L^{200}$ and $U\le N^{1/2-\kappa}$, this is $O_{\rho,\kappa}(NL^{-100})$. On $T_r<|\tau|\le N^3$ apply (2) against the **same uniform GRH norm bounds** just proved. The integral tail weight $O(L^{-100})$, squared and then multiplied by $B_r$, costs at most $O_{\rho,\kappa}(NL^{-100})$ again since $NB_r=T_r/100$. On $|\tau|>N^3$ the polynomial trivial bound independent of $\tau$ is killed by (2) with larger fixed $j$. These estimates preserve the full principal profile by Mellin inversion.

## 3. Synthetic tail estimates now include small denominators

As before expand the exact $(p,M)=1$ by $\sum_{h\mid M,h\mid p}\mu(h)$. Put $H=N^{\kappa/4}$. For $h\le H$ every class of $p\bmod r_q$ together with $h\mid p$ is empty or one progression of spacing $\ell=[h,r_q]$. Use Poisson on the smooth separated synthetic weight $V(p/P)(p/P)^{i\tau}/\log p$ up to $T'_r=N^{\kappa/8}T_r$, not merely $T_r$. Its nonzero modes are bounded by $O_{\rho,j}((P/\ell)(1+T'_r)^j(P/\ell)^{-j})$ after summing $|k|^{-j}$. Uniformly,

$$
 \frac{(1+T'_r)H r}{P}\ll_\rho N^{-5\kappa/8}.
$$

Indeed $T_r r=100N/Q_*\asymp\sqrt N$, while $P\ge N^{1/2+\kappa}$. Thus the nonzero Poisson modes are negligible to any fixed power. For $|\tau|>T'_r$, (2) directly beats a polynomial trivial bound since $T'_r\gg N^{\kappa/8}L^{200}$. This proves the short synthetic estimate with its exact real CRT principal coefficient and no artificial unit forcing at $r_q$.

The actual omitted long $h$ terms have full-circle squared energy $\ll_{\rho,\kappa}N K^2\tau(M)^2 L/H$, by Cauchy–Schwarz over at most $O_\kappa(\tau(M))$ tuples for each integer $n$, then counting $n\le N$ divisible by $qh$. Here and below $\tau(M)\le N^{\kappa/100+o(1)}$ by Chebyshev at $z=\kappa L/1000$ and $2^{\omega(N)}=N^{o(1)}$. For the omitted real model the coefficient at $r_q=d$ has magnitude at most $K\tau(M)/\max(d,H)$ and is supported on $d\mid M$, since it is $K\sum_{h\mid M,\ h>H,\ d\mid h}\mu(h)/h$.

When $q\nmid r$, one has $d=r$, and after summing the real cofactor profiles their total log-normalized magnitude is $O_\rho(1)$. The full real Plancherel model energy, weighted by numerator count, is at most

$$
 \ll_\rho N K^2\tau(M)^2
         \sum_{r\mid M}\frac r{\max(r,H)^2}
 \ll_\rho N K^2\tau(M)^3/H .
$$

This bound works for $r\le H$ as well; one cannot assert the entire synthetic coefficient is omitted at these small denominators. For $q\mid r$, support requires $r=qd$ with $d\mid M$; since $q\not\mid M$, at most one eligible $q$ occurs for each such $r$. The cofactor profile contributes $O_\rho(1/q)$, and summing numerator counts at most $qd$ gives the same last bound with an extra $\sum_q1/q\ll L$. All synthetic energy errors are consequently $O_{\rho,\kappa}(N^{1-\kappa/5})$ for fixed $\kappa$.

## 4. Signed conclusion

The squared discrepancy between the exact $F_I$ and its full $M_{I,r}$ on $\mathfrak D$ is $\ll_{\rho,\kappa}NL^{-32}$ after the smoothing, prime and synthetic estimates. The same holds for $I_0$. Cauchy–Schwarz against the model energy $O(NL^2)$ gives $O_{\rho,\kappa}(NL^{-8})$ for all integrated product-error terms. The surviving main profiles carry no numerator dependence, so summing $e(-aN/r)$ gives $c_r(N)$ before absolute values. For nonsquarefree $r$ the only possible nonzero main has $r=q^2d$ with squarefree $d$ coprime to $q\in\mathcal Q$, hence $c_r(N)=0$. Squarefree $r\mid M$ give zero centered profile. Integration by parts on the original hard intervals gives $|M_{I,r}(\beta)|\ll_\rho\min(N,|\beta|^{-1})/\varphi(r)$, so the remaining integral is bounded by $O_\rho(N\sum_{r\ {\rm squarefree},\,r\nmid M}|c_r(N)|/\varphi(r)^2)$ after extending the real $\beta$ integration. Every retained denominator has some prime $\ell>z$ with $\ell\nmid N$ and corresponding local coefficient $O(\ell^{-2})$; the full positive Euler product is $O(S)$, whence the R32 signed tail $O_{\rho,\kappa}(SN/(L\log L))$.

This proves (1) for genuine hard intervals and transfers by Abel summation to central bounded-variation cumulative weights, since the second factor is fixed. The only remaining coefficient for this approach to the selected covariance is on the complement of $\mathfrak D$, not a proved bound there.
