# Only four-distinct-prime terms remain in the signed Dirichlet complement

Retain the setup of the [full Dirichlet-width estimate](r35-source-square-root-dirichlet-arcs.md) and the [synthetic-leg removal](r37-source-synthetic-localization-dirichlet-complement.md): fixed $0<\rho<1/2$, $0<\kappa\le1/2000$, sufficiently large even $N$, $L=\log N$, $I_0=[\rho N,(1-\rho)N]$, arbitrary moving hard $I\subseteq I_0$, and

$$
 \mathcal Q=\{q\text{ prime}:N^\kappa\le q\le N^{1/2-\kappa},\ (q,N)=1\},
 \qquad Q_*=\lfloor\sqrt N\rfloor,\quad R=\lfloor Q_*L^{-200}\rfloor.
$$

Write $e(x)=e^{2\pi ix}$. The disjoint union $\mathfrak D$ consists of every reduced rational arc with denominator $1\le r\le R$ and width $B_r=1/(rQ_*)$; its exact complement is $\mathfrak m$. Use the genuine prime transform

$$
 A_J(\alpha)=\sum_{q\in\mathcal Q}(\log q)
   \sum_{\substack{p\ {\rm prime},\ (p,N)=1\\qp\in J}}e(\alpha qp),
 \qquad J\in\{I,I_0\}.
$$

Write $A_{J,q}$ for the subtransform with the small prime $q$ fixed, and $A^{(p)}_J$ for the subtransform with the large prime $p$ fixed. Every occurring large prime satisfies $p\ge\rho N^{1/2+\kappa}>Q_*$ for large $N$, precluding equality with any small prime. Every constituent prime is a unit modulo $N$.

**Theorem.** The signed contribution on the exact $\mathfrak m$ of the sum of products sharing a large prime is $O_{\rho,\kappa}(NL^{-198})$, unconditionally. Assuming global Dirichlet GRH, the signed contribution of the sum of products sharing a small prime is $O_{\rho,\kappa}(NL^{-15})$. Both bounds are uniform in $I$, with either hard endpoint convention. The overlap, where both primes coincide, is $O_{\rho,\kappa}(NL^{-198})$ unconditionally. Consequently, under global Dirichlet GRH,

$$
 \int_{\mathfrak m} A_I(\alpha)A_{I_0}(\alpha)e(-N\alpha)\,d\alpha
  =\int_{\mathfrak m} \mathcal A_I^{(4)}(\alpha)e(-N\alpha)\,d\alpha
         +O_{\rho,\kappa}(NL^{-15}),                            \tag{1}
$$

where $\mathcal A_I^{(4)}$ is the actual expansion of $A_I A_{I_0}$ restricted to four distinct primes. No estimate for the signed four-distinct integral is asserted.

## 1. Large-prime repetitions: unconditional dilation bound

For each fixed occurring $p$ one has $A^{(p)}_J(\alpha)=f_{J,p}(p\alpha)$ with $f_{J,p}(x)=\sum_{q\in\mathcal Q,\;qp\in J}(\log q)e(qx)$. At fixed $x\in[0,1)$, a point of the fiber $\alpha=(x+m)/p$, $0\le m<p$, lies in the arc around a reduced $a/r$ only if some integer $\ell$ satisfies

$$
 |rx-k|\le p/Q_*,
 \qquad k=pa+rp\ell-rm\in\mathbb Z .
$$

At fixed $r$, a qualifying integer $k$ determines $m$ uniquely modulo $p$, since $k\equiv-rm\bmod p$ and $p>r$ is prime. Therefore for this $r$ at most $2p/Q_*+1$ distinct fiber points belong to such arcs, even after summing all reduced numerators. Summing $r\le R$ shows that at every $x$ the fraction of points in $\mathfrak D$ is at most $2R/Q_*+R/p\ll L^{-200}$. In particular

$$
 \int_{\mathfrak D}|A^{(p)}_J(\alpha)|^2\,d\alpha
  \ll L^{-200}\int_{\mathbb T}|A^{(p)}_J(\alpha)|^2\,d\alpha .
$$

By Parseval the sum over $p$ of the latter full-circle energies is $O_\kappa(NL^2)$: each $n\le N$ has at most $1/\kappa$ eligible prime divisors, and each pair contributes at most $L^2$. Cauchy–Schwarz over $p$ and $\alpha$ now gives the claimed $O_{\rho,\kappa}(NL^{-198})$ estimate on $\mathfrak D$. For each $p$ the full-circle signed coefficient is exactly zero: all product indices are divisible by $p$ but $p\nmid N$. Negating the contribution of $\mathfrak D$ therefore gives the same bound on its exact complement.

For context, at $I=I_0$ the sum over $p$ of the integrals on $\mathfrak m$ of the absolute values of the individual same-$p$ products is $\gg_{\rho,\kappa} NL$. Indeed Parseval identifies the full-circle sum with the genuine weighted pair count with squared marker $(\log q)^2$; restricting $q$ to $[N^{1/5},N^{1/4}]$, the ordinary prime number theorem on the fixed-proportion large-prime intervals and prime Mertens give a lower bound $N L^{-1}\sum_q(\log q)^2/q\gg_\rho NL$. Removing the primes dividing $N$ is negligible in these ranges. The preceding dilation estimate removes only an $O(L^{-200})$ fraction of this energy. This is a termwise absolute comparison, not a lower bound for the modulus of the summed products or any signed coefficient.

## 2. Small-prime repetitions: GRH in the direct sum over $q$

For a reduced rational $a/r$ and $d=r/(r,q)$ define the exact uncentered real model

$$
 G_{J,q,r}(\beta)
 =\frac{\mu(d)}{\varphi(d)}
    \int_J\frac{\log q}{q\log(t/q)}e(\beta t)\,dt .
$$

We use the separate squared approximation

$$
 \sum_{q\in\mathcal Q}\sum_{r\le R}\ \sum_{a\bmod r}^{\!*}
       \int_{|\beta|\le B_r}
       |A_{J,q}(a/r+\beta)-G_{J,q,r}(\beta)|^2\,d\beta
  \ll_{\rho,\kappa} NL^{-37}.                                 \tag{2}
$$

Here the star means reduced numerators. To verify (2), smooth the hard interval as in R35 using a $[0,1]$-valued convolution of width $\varepsilon=L^{-40}$ in $t/N$. The sum of the squared torus errors over $q$ is $O_\kappa((\varepsilon N+1)L^2)$ by Parseval and the bounded number of eligible $q\mid n$ on the two edges, including any endpoint atoms. The model edge removal costs $O_\rho(\varepsilon NL^3)$ by full real Plancherel: its weights satisfy

$$
 \sum_{q\in\mathcal Q}\frac1{q^2}
     \sum_{r\le R} \frac{\varphi(r)}{\varphi(r/(r,q))^2}
 \ll L^3.                                                     \tag{3}
$$

For $q\nmid r$ use $\sum_{r\le R}1/\varphi(r)\ll L^2$. For $q\mid r$ write $r=qd$, use $\varphi(qd)/\varphi(d)\le q$ also when $q\mid d$, and then $\sum_{q\le N}1/q\ll L$. The same argument without $\varepsilon$ gives squared model energy $O_\rho(NL^3)$.

Apply the Mellin/real Plancherel bound of R35 to each smoothed $q$ transform separately. More explicitly, put $P=N/q$, choose fixed smooth $V(p/P)$ supported at $p\asymp_\rho P$ and equal to one on the smoothed physical interval, and use $A_\beta(x)=w_J(e^x)e(\beta N e^x)$. With the normalization $\widehat A_\beta(\tau)=\int A_\beta(x)e^{-i\tau x}\,dx$, R35 gives

$$
 \int_{|\beta|\le B_r}\left|\frac1{2\pi}
           \int_{-T_r}^{T_r}\widehat A_\beta(\tau)D(\tau)\,d\tau
      \right|^2 d\beta
 \ll_\rho N^{-1}\int_{-T_r}^{T_r}|D(\tau)|^2d\tau,\qquad
 T_r=100NB_r .
$$

The separated error $D_{q,r,a}(\tau)$ here is the sum of the unit prime weights $(\log q)V(p/P)(p/P)^{i\tau}e(aqp/r)$ minus its indicated principal integral before Mellin inversion. For $|\tau|\le N^3$, the smooth GRH estimate in R35 bounds the prime character error before multiplication by $\log q$ by $O_\rho(\sqrt P L^2)$, uniform in the shift. Its proof uses fixed smooth $V$ and the shifted unit-bin zero count; the finitely many prime divisors of $N$ contribute within this bound. Every prime in this support exceeds $r$, so is in a unit class modulo $d$.

In fact additive Parseval on all numerator classes modulo $d$, followed by character Parseval on its units, bounds the reduced-numerator sum of squared errors by $O_\rho(dP L^4)$ before the marker. To see the normalization, write $E_b$ for each residue prime sum minus the principal integral divided by $\varphi(d)$; then $\sum_{j\bmod d}|\sum_b E_b e(jb/d)|^2=d\sum_b|E_b|^2=(d/\varphi(d))\sum_\chi|E_\chi|^2$. The principal additive model for reduced $j$ is exactly $\mu(d)/\varphi(d)$ times the integral. The map $a\bmod r$ reduced to $(q/(r,q))a\bmod d$ is a surjection on the unit classes with multiplicity $\varphi(r)/\varphi(d)\le r/d$. This handles both $q\nmid r$ and $q\mid r$, including $q\mid d$. Consequently

$$
 \sum_{q\in\mathcal Q}\sum_{a\bmod r}^{\!*}|D_{q,r,a}(\tau)|^2
 \ll_\rho r L^4\sum_q P(\log q)^2
 \ll_\rho r N L^7 .
$$

Combine with the Mellin bound and sum $r$: the low-$\tau$ squared error is $O_\rho(L^7\sum_{r\le R} rT_r)=O_\rho(NL^{-193})$. For $T_r<|\tau|\le N^3$, the nonstationary estimate of R35, uniform for $|\beta|\le B_r$, gives $\int_{|\tau|>T_r}|\widehat A_\beta(\tau)|d\tau=O(L^{-100})$ since $T_r\gg L^{200}$. Minkowski against the same uniform separated numerator norm gives squared tail $\ll L^{-200}\sum_{r\le R} B_r r N L^7$, smaller still. For $|\tau|>N^3$ increase the number of integrations by parts to dominate all polynomial trivial bounds. Mellin inversion retains the principal model exactly. With the edge estimates this proves (2) for the original hard intervals.

Use Cauchy–Schwarz on the direct-sum model discrepancy (2) and the model energy $O_\rho(NL^3)$. In the signed $\mathfrak D$ integral of $\sum_q A_{I,q}A_{I_0,q}$, replacement by $\sum_q G_{I,q,r}G_{I_0,q,r}$ therefore costs $O_{\rho,\kappa}(NL^{-17})$. The model is independent of the reduced numerator and the target phase sums to $c_r(N)$. The absolute value of the remaining signed model is at most

$$
 \ll_\rho N\sum_{q\in\mathcal Q}\frac1{q^2}
       \sum_{r\le R}
         \frac{|c_r(N)|\mu(r/(r,q))^2}{\varphi(r/(r,q))^2}
 \ll_\rho \mathfrak S(N)\,N^{1-\kappa}.
$$

The first bound is real Plancherel separately for each pair of hard profiles. For the second, when $q\nmid r$ the inner sum is bounded by the squarefree Ramanujan Euler sum $O(\mathfrak S(N))$ of the [major-arc calculation](r32-source-double-giant-major-arcs.md). When $r=qd$ and $q\nmid d$, use $|c_q(N)|=1$ and $|c_r(N)|=|c_d(N)|$. When $r=qd$ and $q\mid d$, a nonzero $\mu(d)$ forces $r=q^2h$ with $(q,h)=1$ and then $c_r(N)=0$ because $q\nmid N$. This exhausts the model. The full-torus signed coefficient for each fixed $q$ is again identically zero because $q\nmid N$, so the same bound with the opposite sign applies on $\mathfrak m$ after adding the approximation error. This gives $O_{\rho,\kappa}(NL^{-15})$.

## 3. Intersection and exact remaining term

The two repetition classes intersect only at the identical ordered constituent pair $(q,p)$, since the small and large prime ranges do not intersect. Their product transform is

$$
 \sum_{\substack{q,p\ {\rm eligible}\\qp\in I}}(\log q)^2 e(2qp\,\alpha).
$$

Its full-circle coefficient at $N$ is zero since $q\nmid N$. Its absolute value is $O_\kappa(NL^2)$, while $|\mathfrak D|\le2R/Q_*\ll L^{-200}$. Its signed $\mathfrak m$ coefficient consequently costs $O_{\rho,\kappa}(NL^{-198})$ by negation, unconditionally. Subtracting the two repetition classes and adding back this exact intersection proves (1). The moving endpoint convention is preserved, and the second interval remains $I_0$ throughout. Together with R37 this removes the synthetic contributions and repeated-prime terms from the exact signed complementary integral; it neither estimates the remaining four-prime cancellation nor extends the result to a union with R34.
