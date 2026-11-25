# One unconditional scale set for planted AP radicals

**Scope.** The [unconditional planted AP-radical law](r85-spectral-unconditional-planted-ap-good-dyads.md) held on arbitrarily large good dyads for a prescribed planting cap. Here a single analytic scale set works for all fixed AP prime unions and all allowed planting exponents at once. It contains diverging contiguous windows and has **upper density one in $G=\log Y$**. On those scales the actual full and original moving polynomial-major laws hold unconditionally, with errors uniform as the planting threshold moves over a large range. Exceptional target sets are relative to each prescribed divisibility family, not a shared assertion over all targets or all planting thresholds. Neither all-scale validity, lower density one of the scales, exact radicals, individual target control, nor Hypothesis S is claimed.

Put

$$
 G=\log Y,\qquad Z(G)=\frac{\sqrt G}{\log G},\qquad
 Q_{\rm cap}(G)=\exp(16 Z(G)).
 \tag{1}
$$

Choose the small fixed $a_0>0$ from [the good-dyad proof, Section 1](r85-spectral-unconditional-planted-ap-good-dyads.md#1-good-dyads-are-unconditional), and let $\mathcal G$ be the set of sufficiently large real $G$ for which no primitive real character of conductor at most $Q_{\rm cap}(G)$ has a zero $\beta>1-4a_0/\sqrt G$. This definition does not involve an AP union or any of the real divisor cuts. There is a fixed $c>0$ such that, for arbitrarily large $H$,

$$
       [H,\ cH(\log H)^2]\subset\mathcal G.
 \tag{2}
$$

In particular, $\limsup_{R\to\infty}R^{-1}|\mathcal G\cap[1,R]|=1$, where bars in this scale statement denote Lebesgue measure.

Fix any modulus $q_*$ and nonempty union $\mathcal P$ of its reduced prime classes of density $d\in(0,1]$, and fix $0<\epsilon<1/2$. On a dyad with $G\in\mathcal G$ prescribe **any** real $z$ with $G^\epsilon\le z\le Z(G)$, and set

$$
 K_z=2\!\!\prod_{\substack{2<p\le z\\p\in\mathcal P}}p,\qquad
 \mathcal N_{Y,z}=\{N\in[Y,2Y]\cap\mathbb Z:K_z\mid N\},\qquad
 \theta_z=\frac{\log z}{\log G}.
 \tag{3}
$$

Use the genuine $M_\pm$, hard tests $I,\omega$, prime weight $\lambda$, and exact original arcs $\mathfrak M_N,\mathfrak m_N$ of the good-dyad proof. In particular $M_\pm=(1\pm\mu(m))M_>/2$ on its actual squarefree support $m\in[N/3,2N]$, $L=\log N$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ for fixed admissible $B>B_0>0$, and $+$ denotes even squarefree prime-factor count. The original major has denominator cap $N^{1/1000}$ and radius $2N^{1/1000}/N$, not the auxiliary cap (1). Denote by $\mathcal K_{\pm,d}$ the two constants in [the AP-radical law, (4)](r83-spectral-ap-radical-major-law.md).

**Theorem.** On each sufficiently large dyad with $G\in\mathcal G$, for each prescribed $z$ in (3), there is an exceptional set in $\mathcal N_{Y,z}$ of size

$$
 \ll (Y/K_z)\exp\!\bigl(-(\log z)^{1/3}\bigr)+Y^{\,1-3/10000}
 \tag{4}
$$

such that, outside it, the actual **full** signed correlation and the actual original $\mathfrak M_N$ integral both equal

$$
 \Sigma(N)\mathcal K_{\pm,d}\!\left(\frac{2B}{\theta_z},
                              \frac{B-B_0}{\theta_z}\right)
   \int_I\frac{\omega(u)}{\log(N-u)}\,du
 +o\!\left(\frac{\Sigma(N)|I|}{L}\right)+O_{A,B,B_0}(YG^{-A}),
 \tag{5}
$$

for each fixed $A>0$. This is simultaneous for both signs and all genuine $I,\omega$, with the errors uniform in $z$ over (3) for the fixed $q_*,\mathcal P,\epsilon,B,B_0$. The actual original minor is $O(Y^{1-1/40000})$ by the unconditional original-moving-minor theorem. There is no assumption about zeros in the statement: the scale windows (2) are unconditional. A chosen sequence with $\theta_z\to\vartheta\in(0,1/2]$ can thus use the same scale set, and has the fixed leading parameters $2B/\vartheta,(B-B_0)/\vartheta$ in the limit.

## 1. Whole good windows from one exceptional zero

Use [Montgomery–Vaughan, Chapter 11, Corollary 11.10](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF), as in the good-dyad proof: among primitive characters of conductors at most $Q$ there is at most one zero in the real interval $\beta\ge1-c_P/\log(4Q)$, with an absolute $c_P>0$. If all sufficiently large $G$ are good, (2) is immediate. Otherwise take arbitrarily large bad $G_0$, and let the obstructing zero have $b=1-\beta<4a_0/\sqrt{G_0}$. Put $H=(8a_0/b)^2>4G_0$. At every $G\ge H$ this old zero no longer obstructs goodness: $b=8a_0/\sqrt H>4a_0/\sqrt G$. The old conductor is still under the cap, since $Z(G)$ is increasing for large $G$.

For $H\le G\le cH(\log H)^2$, the same old zero remains strictly within the Page interval of the **current** cap, because

$$
 b\log(4Q_{\rm cap}(G))
 \le \frac{8a_0}{\sqrt H}\left(\log4+
                        \frac{16\sqrt{cH}\log H}{\log H}\right)
 =128 a_0\sqrt c+o(1) < c_P
 \tag{6}
$$

for a sufficiently small fixed $c>0$. Any new zero obstructing goodness is different and would also lie within the Page interval, since
$(4a_0/\sqrt G)\log(4Q_{\rm cap}(G))\ll1/\log G$. This contradicts uniqueness. The whole closed window in (2) is good for all sufficiently large $H$ obtained this way, with strict margins in both tests. Taking $R=cH(\log H)^2$ gives the upper-density assertion (the available interval has relative length $1-H/R\to1$). Neither the proof nor the statement bounds the length of earlier bad portions.

## 2. Common analytic inputs and disjoint-error budgets

On this single scale set apply the proof of the [uniform prime and all-residue masked Möbius bounds, (3)–(4)](r85-spectral-unconditional-planted-ap-good-dyads.md#1-good-dyads-are-unconditional) with $Q_0=Q_{\rm cap}(G)$. Those estimates used only $\log Q_0\le\sqrt G/2$, the absence of the stated real zero, and fixed polynomial lower ranges for the progression lengths; these hold uniformly here. In particular for every necessary coprimality mask of polynomial size and every residue, including nonunits, the signed Möbius progression error is length times $\exp(-c_1\sqrt G)$ on the polynomial-length ranges. The left prime progression has its ordinary principal main. No separate hypothesis on the character sums is introduced by changing the planting threshold.

For clarity, use the **same** common auxiliary arcs throughout this dyad, with denominators $q\le Q_0$ and widths $2Q_0/Y$. On the actual large signed sectors, residue sums and slow-phase partial summation multiply the error by at most $Q_0^2G^{O(1)}$; the two positive-variable CRT sectors have a fixed power saving after a fixed power of $Q_0$. The left error has the same phase and residue cost. The arcs have total measure $O(Q_0^3/Y)$, while the genuine polynomials have trivial bound $YG^{O(1)}$. Hence the integrated analytic error is $Y G^{O(1)}Q_0^5 e^{-c_2\sqrt G}$ plus a power-saving error, by [the actual auxiliary-major proof](r85-spectral-unconditional-planted-ap-good-dyads.md#2-unconditional-auxiliary-majors-at-the-planted-scale). It is smaller than $YG^{-A}$ for any fixed $A$, uniformly because $\log Q_0=o(\sqrt G)$. All of these arithmetic estimates are independent of $z$ except for the subsequent rational-tail and profile restrictions; the true $D,H_0,V$ have not been frozen.

We now list the exceptional count separately for each family (3). The AP prime number theorem gives $\log K_z\sim dz$ uniformly as $z\to\infty$, in particular $K_z\le e^{2z}\le e^{2Z(G)}$. The two positive divisor-moment arguments from [the good-dyad proof, (5)](r85-spectral-unconditional-planted-ap-good-dyads.md#2-unconditional-auxiliary-majors-at-the-planted-scale) give, outside
$O((Y/K_z)(e^{-(\log z)^{1/3}}+e^{-z^{1/2}}))$ members of $\mathcal N_{Y,z}$,

$$
     \sum_{\substack{p\mid N\\p\nmid K_z}}\frac{\log p}{p}
                    \le(\log z)^{1/3},
 \qquad
     \sum_{\substack{p\mid N\\p\nmid K_z}}p^{-3/4}\le z^{1/2}.
 \tag{7}
$$

The uniformity follows from the same bounded Euler products (over all primes) in the two moments, using $\#\{N\in\mathcal N_{Y,z}:a\mid N/K_z\}\le2Y/(K_z a)$ for the exact extra divisors with $(a,K_z)=1$. Pointwise on the second condition the rational completion error, normalized by $Y$, is
$G^{O(1)}Q_0^{-1/4}\mathcal A(N)^{C}$ with $\log\mathcal A(N)=O(z^{1/4}+z^{1/2})$, by [the good-dyad proof, (6)](r85-spectral-unconditional-planted-ap-good-dyads.md#2-unconditional-auxiliary-majors-at-the-planted-scale). This is $O(G^{O(1)}e^{-(4+o(1))Z(G)})$ uniformly over the planting thresholds, since $z\le Z(G)$. The slow completion costs $YQ_0^{-1}$ times fixed log powers, also negligible. Thus on (7) the auxiliary integral has the same exact completed parity bracket as in that proof.

The **common complement** uses the fixed-arc Bessel estimate of [the common-complement proof](r85-spectral-unconditional-planted-ap-good-dyads.md#3-the-two-actual-arc-complements), with the original exact hard axes $m,ab,ac,abc$ and no pattern restrictions. It bounds the ambient squared maximal sum by $O(Y^3G^C Q_0^{-1/2})$. Markov at $Y e^{-Z(G)}$ excludes $O(Y G^C e^{-6Z(G)})$ ambient targets. This is a single exceptional set before any planting, so its relative cost for any $z$ is $O(G^C e^{-4Z(G)})$, uniformly. The true original-moving-minor theorem in that same proof gives its two fixed parity exceptions of ambient size $O(Y^{1-3/10000})$, independent of $z$. The exponential auxiliary costs and $e^{-z^{1/2}}$ are absorbed in the first term of (4), because $z\ge G^\epsilon$ and $Z(G)\ge z$. Combining with (7) proves (4), and also proves the relative-density-one assertion since $K_z\le e^{2Z(G)}=Y^{o(1)}$. Keeping distinct exceptional sets for (7) is necessary when claiming uniformity across the different divisibility families.

## 3. Uniform cutoff profile and exact arc conclusions

Use $\ell=\log z$ in [the planted mask transfer](r84-spectral-planted-ap-radical-full.md#2-perturb-the-genuine-radical-in-log-coordinates). For each fixed $j$ the normalized primitive with mask $K_z$ converges in $L^1$ and weighted $v f$ in $L^2$ to $f_d$ as $z\to\infty$, with the same limit for all $z$. The extra mask of $N$ is the exact positive probability convolution with first moment $O(\ell^{-2/3})$ on the first condition of (7); its weighted $L^2$ error term is $O(\ell^{-1/6})$. Thus both convergences are uniform for $G^\epsilon\le z\le Z(G)$ and all the retained targets, for each fixed $j$. This assertion follows directly from the tail definition of convergence as $z\to\infty$, since the lower bound on $z$ tends to infinity; no effective rate for the AP profile is needed.

The actual $U=\log(H_0/D)$ and $T(x)=\log(x/D^2)$ with $x=N-u\in[N/3,2N]$ satisfy
$U/\ell=(B-B_0)/\theta_z+O((G\ell)^{-1})$ and
$T(x)/\ell=2B/\theta_z+O(\ell^{-1})$, uniformly, since $L=G+O(1)$. For each fixed $j$ the actual first terminal endpoint is $(U-\log j)_+/\ell$. As $\epsilon\le\theta_z\le1/2$, the target terminal cutoff and shift vary in compact intervals bounded away from zero. The convergence of the bracket is uniform on those compact intervals. Indeed for the terminal square restrict to a half-line bounded away from zero, using weighted $L^2$; the integrals there are absolutely continuous in the endpoint uniformly for the fixed limit. The cumulative and integrated autocorrelation terms follow uniformly from global $L^1$ and Young's inequality. For the single positive-shift autocorrelation the small $v$ portion is small uniformly by global $L^1$ convergence plus the uniform shifted supremum bound; on $v\ge\epsilon'$ use translation continuity of an $L^2$ profile restricted away from zero and Cauchy–Schwarz, uniformly as the shifts stay in this compact interval. One may send the auxiliary $\epsilon'\downarrow0$ after convergence. This also proves the needed continuity of $\mathcal K_{\pm,d}$ in the two compact positive parameters, even in the cusp case.

As in [the exact parity bracket transfer](r84-spectral-planted-ap-radical-full.md#3-put-back-the-exact-parity-coefficients-and-invert), the mass coefficients at each $N$ have exact signed sum one and a uniform absolute $j^{1/2}$ moment. Split off $j>e^{U/2}$ first, with error $O((1+\ell)e^{-U/4})=o(1)$ uniformly; only on the other part is the terminal cutoff bounded away from zero. That part has a bounded bracket, uniformly by the $v f$ supremum and $L^1$ bounds. Fixed-$j$ convergence then gives the desired limit uniformly through the sum using the moment and the exact mass identity. This reproduces the coefficients in (5) with $\theta_z$ rather than its eventual limit. It uses the literal hard cutoff, not a limit through the origin.

It follows that the auxiliary integral has (5) on (7). Adding its genuine common complement yields the true full correlation by Fourier inversion on the stated good targets. Then subtracting the **actual original** moving minor yields the genuine original major. At no stage are the auxiliary and original major sets identified. The conclusion uses R85's unconditional analytic argument on the common scale set rather than the historical GRH statement of the pointwise parity formula.

## 4. A fixed planting cap below the endpoint

For comparison, fix $0<\rho<1/2$ and replace $Z(G)$ by $\kappa G^\rho$ with fixed sufficiently small $\kappa>0$, defining $\mathcal G_\rho$ by the corresponding conductor cap. The same proof of (6) shows that for some fixed $c_\rho>0$ there are arbitrarily large $H$ such that
$[H,c_\rho H^{1/(2\rho)}]\subset\mathcal G_\rho$: at the upper end, the product of $b=8a_0/\sqrt H$ and the cap logarithm is at most $128a_0\kappa c_\rho^\rho+o(1)$, and a potential new obstructing zero still lies in the Page interval. All analytic, profile and exceptional-set arguments above apply with this common cap and with $0<\epsilon<\rho$, since its logarithm remains $o(\sqrt G)$ and the parameters in the compact profile argument remain positive. In particular this includes the **fixed** planting $z=\kappa G^\rho$ of the original good-dyad theorem. These windows again give upper density one in $G$ and also the quantitative upper logarithmic density bound

$$
 \limsup_{R\to\infty}\frac1{\log R}
           \int_{2}^{R}\mathbf1_{\mathcal G_\rho}(u)\,\frac{du}{u}
      \ge 1-2\rho .
 \tag{8}
$$

Indeed the interval ending at $R=c_\rho H^{1/(2\rho)}$ contributes $\log R-\log H$. This is an upper-density statement along the endpoints of verified windows, not a lower-density claim, and not an estimate on missing dyads.
