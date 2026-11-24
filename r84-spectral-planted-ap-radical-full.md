# The true mixed correlation on a planted AP-radical family

**Scope.** A pointwise major law on the exact-radical sequences of the [AP-radical result](r83-spectral-ap-radical-major-law.md) does not by itself evaluate their full prime correlation: the [unconditional original-minor bound](r79-spectral-original-minor-power-exception.md) could miss every member of such a sparse sequence. Planting the same primes by **divisibility**, rather than specifying the entire radical, fixes this counting problem. Almost every target in the resulting, still sparse, family has the same generalized Dickman major coefficients under the historical prime and masked Möbius Dirichlet-GRH inputs. On that family the genuine original minor has an **unconditional** power bound outside a relative power-small subset. Thus the genuine **full** coefficients satisfy the Dickman law outside a relative-density-zero subset, with only the major evaluation conditional. Nothing here proves a full theorem for exact radicals, for every member of the planted family, or for Hypothesis S.

Fix a modulus $q_*$ and a fixed nonempty union $\mathcal P$ of its reduced residue classes, of prime density $d\in(0,1]$. In the dyad $[Y,2Y]$ choose a real threshold $z=z(Y)\to\infty$ with

$$
 z\le 10^{-4}\log Y,\qquad
 \frac{\log z}{\log\log Y}\longrightarrow\vartheta\in(0,1],
 \qquad
 K_z=2\!\!\prod_{\substack{2<p\le z\\p\in\mathcal P}}p,\qquad
 \mathcal N_Y=\{N\in[Y,2Y]\cap\mathbb Z:K_z\mid N\}.
 \tag{1}
$$

For $\vartheta<1$ one can take $z=(\log Y)^\vartheta$; at $\vartheta=1$ take $z=10^{-4}\log Y$. This is not a constraint on exponents or on the other prime divisors of $N$. It does not change either the exact right coefficient or the circle-method integration sets. Put $\ell=\log z$, and keep the notation of the AP-radical and pointwise parity formulas: $L=\log N$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ with fixed admissible $B>B_0>0$, $V=[N/3,2N]$, $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$, and the true squarefree $M_\pm=(1\pm\mu(m))M_>/2$, plus denoting even prime-factor count. The exact half-open left $I\subset(N/2,9N/16\,N]$ and $\omega$ of uniformly bounded supremum and variation are unrestricted. The major $\mathfrak M_N$ is the union of the original arcs of denominators $q\le N^{1/1000}$ and radii $2N^{1/1000}/N$; $\mathfrak m_N$ denotes the complement. Write $P_{I,\omega}(\phi)=\sum_{n\in I}\lambda(n)\omega(n)e^{2\pi i n\phi}$, and use the actual right polynomial $\widehat M_\pm(\phi)=\sum_m M_\pm(m)e^{2\pi i m\phi}$.

Let $\tau=2B/\vartheta$, $\upsilon=(B-B_0)/\vartheta$, and denote by $\mathcal K_{\pm,d}(\tau,\upsilon)$ the two constants in [the generalized Dickman law, (4)](r83-spectral-ap-radical-major-law.md). No finite factor is removed from the actual singular factor $\Sigma(N)$.

**Theorem.** For all large $Y$ there is an unconditional exceptional set $\mathcal E_Y\subset\mathcal N_Y$ of size

$$
 |\mathcal E_Y|
  \ll \frac{Y}{K_z}\exp(-\ell^{1/3})+Y^{1-3/10000},
 \qquad
 \frac{|\mathcal E_Y|}{|\mathcal N_Y|}
  \ll \exp(-\ell^{1/3})+Y^{-7/40000}=o(1).
 \tag{2}
$$

Outside this set, unconditionally and simultaneously for both signs and all the hard/BV tests above,

$$
 \left|\int_{\mathfrak m_N}P_{I,\omega}(\phi)\widehat M_\pm(\phi)
                       e^{-2\pi iN\phi}\,d\phi\right|
        \ll Y^{1-1/40000}.
 \tag{3}
$$

Under the historical prime and masked Möbius GRH inputs of the [pointwise original-major formula](r67-spectral-high-mixed-parity-major.md), on the same targets uniformly in the same tests, for each fixed $A>0$,

$$
 \sum_{n\in I}\lambda(n)\omega(n)M_\pm(N-n)=
     \Sigma(N)\mathcal K_{\pm,d}(\tau,\upsilon)
             \int_I\frac{\omega(y)}{\log(N-y)}\,dy
      +o\!\left(\frac{\Sigma(N)|I|}{L}\right)
      +O_{A,B,B_0}(YL^{-A}).
 \tag{4}
$$

The actual major integral has the same expression. As in the previous theorem, the additive error need not be smaller than the main scale on extremely short $I$. In particular on central intervals of length at least a fixed inverse-log fraction of $Y$, the positive odd major constants at $d\le1/2$ for sufficiently small fixed $\upsilon$ from the AP-radical law are also positive leading **full** constants on this relative-density-one subset, taking $\omega\equiv1$. This is a signed mixed-composite contribution, not a prime representation count.

## 1. The original minor and the extra primes of the target

The prime number theorem in fixed progressions, as used in the AP-radical law, gives $\log K_z\sim dz$. It follows from (1) that $K_z\le Y^{1/8000}$ for large $Y$, and $|\mathcal N_Y|\sim Y/K_z$. Apply the [unconditional original-minor theorem, (1)](r79-spectral-original-minor-power-exception.md) on the whole dyad to each of the two right selectors $\rho_m=\mathbf1_{\mu(m)=+1}$ and $\rho_m=\mathbf1_{\mu(m)=-1}$, with no cofactor band. These selectors are fixed throughout the dyad. Nonsquarefree partners already have zero coefficient. The two unconditional exceptional sets, intersected with $\mathcal N_Y$, cost $O(Y^{1-3/10000})$ altogether, and outside them the theorem gives exactly (3) with the original moving cutoffs and arcs, not auxiliary arcs. Dividing this cost by $Y/K_z$ gives $O(Y^{-7/40000})$.

Use the extra-prime moment

$$
 X_N=\sum_{\substack{p\mid N\\p\nmid K_z}}\frac{\log p}{p}.
$$

It has uniformly bounded exponential mean on $\mathcal N_Y$. With $g(p)=\exp((\log p)/p)-1\ll(\log p)/p$, expand $\exp(X_N)$ as a squarefree divisor sum over the extra primes. Writing $N=K_z n$, positivity and the upper bound $\lfloor 2Y/(K_z a)\rfloor\le2Y/(K_z a)$ give

$$
 \sum_{N\in\mathcal N_Y}\exp(X_N)
  \le \sum_{n\le 2Y/K_z}\ \sum_{\substack{a\mid n,\ a\ {\rm sf}\\(a,K_z)=1}}
                   \prod_{p\mid a}g(p)
  \le \frac{2Y}{K_z}\prod_p(1+g(p)/p)
  \ll \frac{Y}{K_z}.
 \tag{5}
$$

Absolute convergence follows from $\sum_p(\log p)/p^2<\infty$. In particular, outside $O((Y/K_z)\exp(-\ell^{1/3}))$ targets, one has $X_N\le\ell^{1/3}$. Combine this set with the two original-minor exceptional sets. This proves (2) and (3) and supplies the perturbation bound for the major calculation.

## 2. Perturb the genuine radical in log coordinates

Keep the original arithmetic $\alpha_p^{(N)}$, equal to $0$ on $p\mid N$ and to $(p-1)/(p^2-2)$ otherwise, from the pointwise parity formula. For a squarefree $j$ let $R_{N,j}$ be its signed reciprocal primitive with the actual additional $(a,j)=1$ restriction, zero in negative log coordinates. Define $M_{N,j}=\int R_{N,j}>0$ and $f_{N,j}(v)=\ell R_{N,j}(\ell v)/M_{N,j}$. In this section $M_{N,j}$ is a positive scalar mass, distinct from the right sequence $M_\pm$. Use a base copy $f_{K_z,j}$ obtained by using the mask for the bare radical $K_z$. Its proof of global $L^1$ and weighted $L^2$ convergence, [AP-radical law (10)](r83-spectral-ap-radical-major-law.md#2-weighted-convergence-without-global-square-integrability), is purely in $z,j$ and the log-prime mask, so makes no assumption about an auxiliary dyadic position of $K_z$. For each fixed $j$ it gives

$$
 f_{K_z,j}\longrightarrow f_d\ \text{in }L^1,\qquad
 v f_{K_z,j}\longrightarrow v f_d\ \text{in }L^2,\qquad
 \|f_{K_z,j}\|_2\le\sqrt\ell\,\|R\|_2.
 \tag{6}
$$

Here $R$ is the ordinary primitive from that proof.

Passing from $K_z$ to $N$ *adds* deletion factors at the extra primes, with no change at primes already masked by $j$. At an extra prime $p\nmid j$ the unnormalized log kernel is $\sum_{k\ge0}(\alpha_p^{(K_z)})^k\delta_{k\log p/\ell}$ after scaling. For the normalized functions this gives the exact positive probability convolution

$$
    f_{N,j}=\eta_{N,j}*f_{K_z,j},\qquad
    \int_{[0,\infty)} v\,\eta_{N,j}(dv)
      =\frac1\ell\sum_{\substack{p\mid N,\ p\nmid K_z\\p\nmid j}}
             \frac{\alpha_p^{(K_z)}}{1-\alpha_p^{(K_z)}}\log p
      \ll X_N/\ell.
 \tag{7}
$$

Indeed the Euler factor replacing $1-\alpha_p^{(K_z)}p^{-s}$ by $1$ is its reciprocal, and normalizing a geometric weighted measure divides by its total mass. Since $2\mid K_z$ and $0\le\alpha_p^{(K_z)}\le1/p$, the stated bound is uniform even in $j$. All kernels are supported on the nonnegative half-line.

Positive probability measures with mean bounded by $O(\ell^{-2/3})$ form an approximate identity for fixed $L^p$ functions, uniformly in such measures, for $p=1,2$. To see this, split the translation average at a fixed small $\epsilon>0$. The large displacements have probability $O(\ell^{-2/3}/\epsilon)$ by Markov, and the small displacements cost at most the supremum of the $L^p$ translation modulus up to $\epsilon$. Let $\ell\to\infty$ and then $\epsilon\downarrow0$. Thus (7) and (6) give $f_{N,j}\to f_d$ in $L^1$ for each fixed $j$, uniformly over all targets satisfying $X_N\le\ell^{1/3}$. For the weighted convergence use the exact identity

$$
 v f_{N,j}=\eta_{N,j}*(v f_{K_z,j})+(v\eta_{N,j})* f_{K_z,j}.
$$

The first term tends to $v f_d$ in $L^2$ by (6) and the same translation argument. The second has $L^2$ norm $O(X_N/\sqrt\ell)=O(\ell^{-1/6})$ by (6), (7), and Young's inequality for a finite measure. Consequently the weighted $L^2$ convergence also holds uniformly for fixed $j$. No assertion of unweighted global $L^2$ convergence is needed at $d\le1/2$.

For use before passing through the infinite $j$ sum, the uniform bounds of the AP-radical law on $\|f_{N,j}\|_1$, $\ell^{-1/2}\|f_{N,j}\|_2$, and $\|v f_{N,j}\|_\infty$ remain valid for the enlarged mask. In detail, the local kernel relative to $R$ uses the effective parameter $\beta_p=\alpha_p^{(N)}\mathbf1_{p\nmid j}$ in $(1-\beta_p p^{-s})/(1-p^{-1-s})$, with $0\le\beta_p\le1/p$. Its normalized positive probability gives the first two norm bounds by Young. The derivative measure $\sigma$ of [AP-radical law (9)](r83-spectral-ap-radical-major-law.md) weights $k\log p/\ell$ by $(\log p)(p^{-k}-\beta_p^k)/\ell$. The mass estimate on each sliding bin of width $1/\ell$ only uses $p^{-k}-\beta_p^k\le p^{-k}$, Chebyshev for $k=1$, and the convergent full higher-power sum. It is unchanged by any finite removal, so convolution with the decaying scaled ordinary primitive bounds $\|v f_{N,j}\|_\infty$ uniformly in $N,j$.

## 3. Put back the exact parity coefficients and invert

Let $P_N$ be the local prefactor of the pointwise parity formula, and set $c_{N,j}=P_N\mu(j)(\alpha^{(N)}(j))^2 M_{N,j}^2$. Exactly as in the [AP-radical law, (6)](r83-spectral-ap-radical-major-law.md), for **every** even $N$ one has

$$
             \sum_{j\ {\rm sf}}c_{N,j}=1,\qquad
             \sum_{j\ {\rm sf}}j^{1/2}|c_{N,j}|\ll1.
 \tag{8}
$$

The proof is the direct Euler cancellation of the mass product, and the absolute estimate uses $\alpha_p^{(N)}\le1/p$ and the uniform boundedness of $P_N M_{N,1}^2=\prod_p(1-\alpha_p^{(N)})^2/(1-2\alpha_p^{(N)})$. Thus the extra primes need not be excluded from the true singular factor, nor from this intermediate signed sum. No coefficient $c_{N,j}$ is required to have a limit separately.

Here $U=\log(H_0/D)$ and $T(x)=\log(x/D^2)$ retain the actual cutoffs. The effective terminal endpoints in the rescaled formula are $(U-\log j)_+/\ell$, and the shift is $T(x)/\ell$. Uniformly on $N\in\mathcal N_Y$ one has $U/\ell\to\upsilon>0$ and $T(x)/\ell\to\tau>0$ uniformly for $x\in V$, since $L=\log Y+O(1)$. In the genuine major bracket of [AP-radical law (14)](r83-spectral-ap-radical-major-law.md), now use $f_{N,j}$ and (8). The $j>e^{U/2}$ part, where the terminal endpoint may even be zero, is $O((1+\ell)e^{-U/4})=o(1)$ by the uniform crude bounds and the half-moment in (8). In the other part the terminal starts at least $U/(2\ell)$, uniformly positive. Its square integral and the positive-shift autocorrelation are thus uniformly bounded by $\|v f_{N,j}\|_\infty$ and $\|f_{N,j}\|_1$, and the integrated autocorrelation costs only $\|f_{N,j}\|_1^2$. This bounds the tail uniformly beyond any fixed $j$ threshold.

For each fixed $j$, the terminal square converges on a half-line bounded away from zero by the weighted $L^2$ convergence of Section 2, while the cumulative term and the integrated autocorrelation converge by global $L^1$ convergence and Young. The single positive-shift autocorrelation converges by splitting its integral in $v$ at small fixed $\epsilon$: the lower part is bounded by the near-zero $L^1$ mass times the uniform shifted supremum from Section 2, and on the upper part ordinary $L^2$ translation continuity applies after truncating away from zero. Its convergence is uniform for the shifts $T(x)/\ell\to\tau$. Thus each fixed normalized bracket tends to the same limit, independently of $j$. Use the uniform tail and exact sum $1$ in (8); there is no step of taking limits of the signed Euler coefficients themselves. The limiting bracket is twice $\mathcal K_{\pm,d}(\tau,\upsilon)$ by the actual hard-cut formula (14).

The conditional pointwise original-major formula now gives the major assertion with error $o(\Sigma(N)|I|/L)+O_{A,B,B_0}(YL^{-A})$, uniformly among all targets satisfying $X_N\le\ell^{1/3}$ even before the minor exceptions are removed. The full additive coefficient is its exact major plus minor by Fourier inversion. For the remaining targets (3) is absorbed in the displayed arbitrary fixed log error, which proves (4). Sparsity was used only to compare the original-minor exceptional count with $|\mathcal N_Y|$; no assertion of a minor bound on individual prescribed targets follows.
