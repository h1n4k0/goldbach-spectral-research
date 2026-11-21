# Wider rational neighborhoods in the signed double-giant covariance

Assume global Dirichlet GRH and retain the exact setup of [R32](r32-source-double-giant-major-arcs.md) and [R33](r33-source-signed-minor-rational-cores.md). In particular $I_0=[\rho N,(1-\rho)N]$, $I\subseteq I_0$ is a moving hard interval, $0<\rho<1/2$, $0<\kappa\le1/2000$ are fixed, $L=\log N$, $S=\mathfrak S(N)$, and $\mathcal Q$ is the prime cofactor set $N^\kappa\le q\le N^{1/2-\kappa}$, $(q,N)=1$. The exact centered transform is

$$
 F_I(\alpha)=\sum_{\substack{q\in\mathcal Q,\ p\ge1\\qp\in I,\ (p,N)=1}}
   \log q\left({\bf1}_{p\ {\rm prime}}-\frac{K}{\log p}{\bf1}_{(p,W)=1}\right)e(\alpha qp),
$$

where $z=\kappa L/1000$, $W$ is the product of primes $\ell\le z$ not dividing $N$, $M=\operatorname{rad}(NW)$, and $K=M/\varphi(M)$. The covariance is the exact fixed-target coefficient of $F_I F_{I_0}$ at $N$.

**Theorem.** Set $R_0=\lfloor N^{1/4}\rfloor$, $R_1=\lfloor N^{1/2-\kappa/4}\rfloor$ and $B=N^{-1+\kappa/3}$. Uniformly over the original moving hard intervals,

$$
 \left|\int_{\mathfrak V}F_I(\alpha)F_{I_0}(\alpha)e(-N\alpha)\,d\alpha\right|
 \ll_{\rho,\kappa}\frac{SN}{L\log L},\qquad
 \mathfrak V=\bigcup_{\substack{R_0<r\le R_1\\a\bmod r,\ (a,r)=1}}
             \{\alpha:\|\alpha-a/r\|\le B\}. \tag{1}
$$

The arcs in $\mathfrak V$ are pairwise disjoint and outside the R32 major arcs. Indeed $2BR_1^2\ll N^{-\kappa/6}$ and $BR_0R_1+R_0R_1/N=o(1)$, comparing with separation of reduced fractions and the R32 widths $R_0/(sN)$ for $s\le R_0$. Their measure is $\asymp BR_1^2\asymp N^{-\kappa/6}$, versus $\asymp N^{-\kappa/2}$ in R33. Subtracting the nested R33 cores gives the same bound on the genuinely new annuli. For $N^{1/2-\kappa/3}\le r\le R_1$ these arcs contain the full width $1/(r\sqrt N)$ of the usual square-root Dirichlet approximation (up to integer endpoint conventions). No coverage of the broad remaining minor arc or signed compensation of other sectors is claimed.

## 1. Moving endpoints are recovered by a small energy error

Choose $\epsilon=L^{-40}$ and let $w_I(u)$ be a $[0,1]$-valued smoothing of the indicator of $I/N$, supported in $[\rho/2,1-\rho/2]$, equal to it off $\epsilon$-neighborhoods of its endpoints, with derivatives of order $j$ bounded by $O_{\rho,j}(\epsilon^{-j})$. Convolution with a fixed scaled nonnegative bump gives these properties, including arbitrarily short intervals; a singleton atom may be deleted at its endpoint. Use $F_w$ for the actual transform with this weight in place of $qp\in I$. The coefficient error is only on $O(\epsilon N+1)$ integers and has magnitude $O_{\rho,\kappa}(L^2)$ at each: $q\ge N^\kappa$ bounds the number of its distinct eligible prime divisors by $O_\kappa(1)$ and $K\ll L^2$. Thus $\|F_I-F_w\|_{L^2(\mathbb T)}^2\ll(\epsilon N+1)L^4$, with no prime-distribution input at the edges.

As in R32, put $r_q=r/(r,q)$, $\Delta_N(d)=\mu(d){\bf1}_{d\nmid M}/\varphi(d)$ and

$$
 G_r(t)=\sum_{q\in\mathcal Q}\frac{\log q}{q\log(t/q)}\Delta_N(r_q),\qquad
 M_{I,r}(\beta)=\int_I G_r(t)e(\beta t)\,dt .
$$

The smoothed model $M_{w,r}$ inserts $w_I(t/N)$ in place of the interval. The R32 bound $|G_r(t)|\ll_\rho1/\varphi(r)$ holds on the slightly enlarged central region: use $\sum_q\log q/q\ll L$ for $q\nmid r$, and $\varphi(r)/\varphi(r_q)\le q$, $\sum_{q\mid r}\log q\le\log r$ for the rest. Full real Plancherel in $\beta$ and $\sum_{r\le R_1}1/\varphi(r)\ll L^2$ give squared model-edge error $\ll\epsilon N L^2$ over $\mathfrak V$, and $\|M_{I,\cdot}\|_{L^2(\mathfrak V)}^2\ll NL^2$.

## 2. Mellin separation, with an integrated rather than pointwise frequency cost

For a dyad $q\in(U,2U]$ put $P=N/U$. Fix $V\in C_c^\infty(0,\infty)$ depending only on $\rho$, equal to one on all $p/P$ admitted by the smoothed central support, and supported in $[\rho/8,2]$. It can be inserted into both arithmetic and continuous $p$ integrals. Use

$$
 A_\beta(x)=w_I(e^x)e(\beta N e^x),\qquad
 \widehat A_\beta(\tau)=\int_\mathbb R A_\beta(x)e^{-i\tau x}\,dx .
$$

Fourier inversion at $x=\log(qp/N)$ separates the factors $(q/U)^{i\tau}$, $(p/P)^{i\tau}$, since $UP=N$. It applies to the smooth real models as well. Put $T=N^{3\kappa/8}$. For $|\beta|\le B$, repeated integration by parts gives

$$
 |\widehat A_\beta(\tau)|\ll_{\rho,j} L^{40j}(1+N^{\kappa/3})^j(1+|\tau|)^{-j}.
$$

Thus its $|\tau|>T$ integral is $O_{\rho,\kappa,A}(N^{-A})$ for arbitrary fixed $A$; all unintegrated arithmetic and model polynomials here have polynomial-size trivial bounds uniform in $\tau$. Dropping this tail is negligible even after all core sums.

The essential estimate for any scalar error $D(\tau)$ on $[-T,T]$ is

$$
 \int_{|\beta|\le B}\left|\frac1{2\pi}\int_{-T}^T
                \widehat A_\beta(\tau)D(\tau)\,d\tau\right|^2d\beta
 \ll_\rho \frac1N\int_{-T}^T |D(\tau)|^2d\tau. \tag{2}
$$

Indeed, first use full real Plancherel in $\beta$ after writing $\widehat A_\beta(\tau)=\int w_I(u)e(\beta N u)u^{-i\tau}\,du/u$, and then use log-coordinate Plancherel in $\tau$ on the interval $u\asymp_\rho1$. The answer contains $T$, not $T^2$, after bounding the $\tau$ integrand uniformly. The smoothing derivative bounds were used only for the discarded tail, not in the norm in (2).

## 3. Genuine prime discrepancy on the separated factors

For a character $\chi\bmod d$, $d\le R_1$, and $|\tau|\le T$, the separated prime factor obeys

$$
 \sum_{\substack{p\ {\rm prime}\\(p,N)=1}}\chi(p)V(p/P)(p/P)^{i\tau}
 =\delta_\chi\int_0^\infty \frac{V(t/P)(t/P)^{i\tau}}{\log t}\,dt
    +O_{\rho,\kappa}(\sqrt P L^C). \tag{3}
$$

There is no $(1+|\tau|)$ loss here. For verification take $G(u)=V(u)/\log(Pu)$, and insert $\Lambda(n) G(n/P)(n/P)^{i\tau}$ in the smooth Dirichlet [explicit formula, Kowalski Theorem C.5.6](https://people.math.ethz.ch/~kowalski/probabilistic-number-theory.pdf). Equivalently use Mellin inversion with $-L'/L(s,\chi)$ and $P^s\widetilde G(s+i\tau)$ and shift to $\Re s=-1/2$ for the primitive inducing character. Uniformly in the fixed strip the Mellin transform is bounded by $O_{\rho,j}(L^{-1}(1+|\Im s+\tau|)^{-j})$. By GRH the nontrivial zeros all have real part $1/2$, and the ordinary unit-interval zero count $O(\log(d(2+|v|)))$ bounds their localized sum by $O(\sqrt P L^C)$ because $d,T$ are polynomial in $N$. The pole contributes the displayed integral and the possible trivial zero at 0, together with the shifted line, is smaller. The shifted-line bound follows from the functional equation at $\Re s=-1/2$ and the absolutely convergent logarithmic derivative on the reflected line; horizontal integrals vanish along heights separated from zeros, using rapid Mellin decay. Proper prime powers, extra induced Euler factors and prime divisors of $N$ contribute within the same error. This proves (3) for every separated twist, with the principal case including the Riemann zeta function.

For $q$ a unit mod $r$, write $e(aqp/r)$ by character inversion on the unit group; here all prime $p$ on $V$ exceed $r$. Apply (3) and Parseval in the reduced numerator. As in R33, $|\tau_r(\chi)|\le\sqrt r$ for complete Gauss sums even for induced characters, while the average squared cofactor character sum is at most $L^2 U(1+U/r)$ by ordinary character orthogonality for residues of $q$; inserting the separated twist of modulus one does not affect this upper bound. Therefore at each $\tau$ the sum of squared prime discrepancies over reduced $a$ is $\ll_\rho N(r+U)L^C$. Applying (2), summing denominators, and then the logarithmically many dyads in norm gives $\ll_{\rho,\kappa}T(R_1^2+N^{1/2-\kappa}R_1)L^C$ for their total squared energy.

For $q\mid r$ use $r_q=r/q$ individually. From (3) and character orthogonality the squared class discrepancy for $p\bmod r_q$ is $\ll_\rho (N/q)L^C$ at each $\tau$. Finite additive Parseval summed over all numerators mod $r$ costs $r$, because the lift mod $r_q$ has multiplicity $r/r_q$. There are $O_\kappa(1)$ eligible primes $q$ per $r$, as they are all at least $N^\kappa$. Cauchy–Schwarz over these choices and (2) then cost $\ll_{\rho,\kappa}T R_1^2N^{-\kappa}L^C$. Hence the whole prime error energy is $\ll_{\rho,\kappa}N^{1-\kappa/8}L^C$. The principal real profiles recombine by Fourier inversion exactly; the reduced numerator main coefficients are those in R32.

## 4. Exact synthetic units: short progressions and long-divisor tails

Expand $(p,M)=1$ by $\sum_{h\mid M,\ h\mid p}\mu(h)$, put $H=N^{\kappa/4}$, and first use $h\le H$. For every $q$, the $p$ progression in a class mod $r_q$ is either empty or a single class mod $\ell=[h,r_q]\le H R_1$. For the separated weight $V(p/P)(p/P)^{i\tau}/\log p$, Poisson summation in this progression gives its real integral divided by $\ell$ and negligible error, uniformly for $|\tau|\le T$. In detail, the nonzero Fourier modes are bounded by

$$
 \ll_{\rho,j}(P/\ell)\sum_{k\ne0}
             (1+T)^j(|k|P/\ell)^{-j},
$$

by differentiating the fixed compactly supported weight in the normalized coordinate $p/P$. This is $O_{\rho,\kappa,A}(N^{-A})$ for any fixed $A$, since $(1+T)H R_1/P\ll N^{-5\kappa/8}$ and $P\ge N^{1/2+\kappa}$. Summing these errors over all progression, dyad and core indices is harmless. The main integrals have the exact CRT densities, with no primality or artificial $p$ unit modulo $r_q$ imposed on the synthetic term.

For the **actual** omitted $h>H$ part, at each integer $n=qp$ there are $O_\kappa(1)$ choices of $q$ and at most $\tau(M)$ choices of $h$ for each $q$. Cauchy–Schwarz in these choices bounds the sum of squared coefficients by

$$
 \ll_{\rho,\kappa}K^2\tau(M)
       \sum_{q\in\mathcal Q}\sum_{h\mid M,\,h>H}\frac{N}{qh}
 \ll_{\rho,\kappa}N K^2\tau(M)^2 L/H .
$$

Indeed all coefficients are supported at $n\le N$ divisible by $qh$, and the log ratio is bounded. Parseval on $\mathbb T$ makes this a squared energy bound on any cores. Chebyshev at $z$ gives $W\le N^{\kappa/100}$, so $\tau(M)\le N^{\kappa/100+o(1)}$; with $K\ll L^2$ this costs at most $O_{\rho,\kappa}(N^{1-\kappa/5})$ for fixed $\kappa$.

The omitted **continuous model** need not be small for each $r$, and is checked separately. For a fixed $q$ it has coefficient $K\sum_{h\mid M,\,h>H,\,r_q\mid h}\mu(h)/h$ on the profile with the $\log q/q$ and $\log(t/q)$ markers. This is the CRT Fourier coefficient proved in R32, before extending the $h$ sum. If $q\nmid r$ it is supported only on $r\mid M$; as $r>R_0>H$ the coefficient equals the entire synthetic coefficient $\mu(r)/\varphi(r)$. Its squared energy is $\ll_\rho N\sum_{r\mid M,r>R_0}\varphi(r)^{-1}\ll_\rho N K\tau(M)/R_0$ by full real Plancherel after summing the numerator count.

If $q\mid r$, support requires $r=qd$ with $d\mid M$. Since $q\not\mid M$ (all $q>z$ and $(q,N)=1$), there is at most one such $q$ for each denominator. The real model profile is bounded by $O_\rho(K\tau(M)/(q\max(d,H)))$ after the log markers. Summing numerator counts $\le qd$ and using real Plancherel gives squared energy at most

$$
 \ll_\rho N K^2\tau(M)^2
       \sum_{q\in\mathcal Q}\frac1q\sum_{d\mid M}\frac d{\max(d,H)^2}
 \ll_{\rho,\kappa} N K^2\tau(M)^3 L/H
 \ll_{\rho,\kappa} N^{1-\kappa/5}.
$$

The short synthetic estimates and both long tails therefore compare the exact synthetic transform to its full model without sacrificing the $K$ or the original units.

## 5. Signed summation over numerators

The preceding estimates and §1 imply squared energy $\|F_I-M_{I,\cdot}\|_{L^2(\mathfrak V)}^2\ll_{\rho,\kappa}NL^{-32}+N^{1-\kappa/8}L^C$ (increasing the constant for $N$ large). The same applies to $I_0$. Cauchy–Schwarz with the model energy makes every product term containing at least one error $O_{\rho,\kappa}(NL^{-8})$.

For the remaining main product the $a$-dependence is exactly the fixed coefficient phase $e(-aN/r)$, giving $c_r(N)$ after summing. Nonsquarefree denominators only have a possible signal at $r=q^2d$ with squarefree $d$ coprime to $q\in\mathcal Q$, and then $c_r(N)=0$. Squarefree $r\mid M$ have zero centered signal. For the surviving squarefree $r\nmid M$, the R32 integration-by-parts bound $|M_{I,r}(\beta)|\ll_\rho\min(N,|\beta|^{-1})/\varphi(r)$ works also at these widths, with integral of the product at most $O_\rho(N/\varphi(r)^2)$ by extending the real $\beta$ integral. Thus the remaining absolute signed sum is bounded by $O_\rho(N\sum_{r\text{ squarefree},\,r\nmid M}|c_r(N)|/\varphi(r)^2)=O_{\rho,\kappa}(SN/(L\log L))$, since a retained denominator includes a prime $\ell>z$, $\ell\nmid N$, with a summable $O(\ell^{-2})$ local coefficient and total positive Euler product $O(S)$. This proves (1) for the actual moving intervals.

Holding the second factor fixed preserves additivity in the first interval; Abel summation therefore transfers (1) to the central bounded-variation cumulative probe. This is still only a Fourier subregion of one true arithmetic covariance. The remaining signed coefficient outside the R32 arcs and these extended neighborhoods is not estimated.
