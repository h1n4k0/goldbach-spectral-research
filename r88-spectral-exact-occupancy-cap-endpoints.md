# Exact mixed-strip occupancy at either real cap endpoint

**Scope.** The [exact occupancy theorem](r87-spectral-exact-band-occupancy-mixed-main.md) excluded the two points where the real autocorrelation cap meets a band endpoint. At either point the hard prime test gives an explicit target-dependent signed boundary factor, not the value assigned to a step function or a universal half-jump. This gives the genuine full and original polynomial-major formulas unconditionally on a density-one family, for all integer occupancies. A fixed positive-density subfamily has nonconstant boundary factor across the physical interval. There is no pointwise assertion at a prescribed target and no assertion about weak S.

Use all exact coefficients, cuts, parities, arcs and tests of the occupancy theorem: $Y\le N\le2Y$ even, $\ell=\log Y$, $v=\log\ell$, $L=\log N$, $D=\sqrt N L^{-B}$, $U_0=B-B_0>0$, $\tau=2B$, $x=N-y$ and $y\in I\subset(N/2,9N/16]$. Let $J=(a,b]$ with $U_0<a<b<1$, and now suppose $\tau=a$ or $\tau=b$. The count $K_Y(m)$ is the number of actual distinct primes $\ell^a<p\le\ell^b$ dividing the true right integer. Write $\rho(u)=\mathbf1_J(u)/u$ and $m_0=\log(b/a)$ as before. For complex $|w|\le1$ put

$$
 g_w=\sum_{k\ge1}\frac{(1-w)^k}{k!}\rho^{*k},
 \qquad h_w=g_w-(1-w)\rho,\qquad
 C_g(t)=\int_{\mathbb R}g(u)g(u+t)\,du .
$$

In particular $h_w$ is continuous and its value at $\tau$ is well-defined, with bilinear conventions as before.

## 1. The exact boundary coefficient

Let $R_{N,j}(u)$ be the unmarked signed reciprocal primitive of the occupancy theorem, zero for $u<0$. Its local parameters are $\alpha_p=0$ for $p\mid N$, $\alpha_p=(p-1)/(p^2-2)$ otherwise; the additional $j$ mask discards the primes dividing $j$. With $\alpha_j=\prod_{p\mid j}\alpha_p$ on squarefree $j$, use the positive mass $M_j=\int_{\mathbb R}R_{N,j}$, the unmarked factor $P_N$ of the [true parity cap](r67-spectral-high-mixed-parity-major.md), and its exact signed weights $c_j=P_N\mu(j)\alpha_j^2M_j^2$. In the notation of the occupancy proof, $P_N=P(1)$. Put $\kappa_j=R_{N,j}/M_j$ on the **raw**, unscaled logarithmic line, and define

$$
 \begin{split}
 F_{N,j}(c)&=\iint_{\mathbb R^2}
       \kappa_j(r)\kappa_j(s)\mathbf1_{s-r<c}\,dr\,ds,\qquad
 F_N(c)=\sum_{j\ {\rm sf}}c_j F_{N,j}(c),\\
 c_{N,x}&=\log(x/N)+\tau(\log L-v),\\
 E_N(c)&=
 \begin{cases}F_N(c),&\tau=a,\\1-F_N(c),&\tau=b.\end{cases}
 \end{split}
 \tag{1}
$$

All integrals are absolutely convergent and the $j$ sum is absolutely convergent. The uniform bounds $\|\kappa_j\|_1+\|\kappa_j\|_\infty\ll1$ follow from the unmarked positive probability convolution in the [first band theorem](r85-spectral-log-power-band-marked-main.md), §2. The exact $\int\kappa_j=1$ and $\sum_jc_j=1$ imply $F_N(c)+F_N(-c)=1$ and $F_N(0)=1/2$, because equality on a line is null in (1). Also $F_N$ is uniformly Lipschitz, since its a.e. derivative is $\sum_j c_j C_{\kappa_j}(c)$ by the change $s=r+c$, and $\sum_j j^{1/2}|c_j|\ll1$. There is no positivity assertion for the individual signed measures in (1).

Define

$$
 \begin{split}
 \mathcal U(w)&=1+\tau\int_{U_0}^\infty g_w(u)^2\,du,\\
 \mathcal V_N(w;x)&=1+2\int_0^\tau g_w(s)\,ds
       +\int_{-\tau}^{\tau}C_{g_w}(s)\,ds\\
 &\hspace{12mm}-\tau\left(h_w(\tau)+C_{g_w}(\tau)
                                 +\frac{1-w}{\tau}E_N(c_{N,x})\right),\\
 \mathcal B_{\pm,N}(w;x)&=\tfrac12 e^{2(w-1)m_0}
                      \bigl(\mathcal U(w)\pm\mathcal V_N(w;x)\bigr).
 \end{split}
 \tag{2}
$$

**Theorem.** For every fixed $A>0$, outside $O_A(Y\ell^{-A})$ even targets, simultaneously for all $k\ge0$, either true parity and all usual hard $I,\omega$, the actual full signed correlation with $\mathbf1_{K_Y(m)=k} M_\pm(m)$, and its actual original moving major integral, are both

$$
 \Sigma(N)\int_I\frac{\omega(y)}{\log(N-y)}
               [w^k]\mathcal B_{\pm,N}(w;N-y)\,dy
    +o\left(\frac{\Sigma(N)|I|}{L}\right)+O_A(Y\ell^{-A}).
 \tag{3}
$$

The little-oh is uniform including in $k$. The factor $E_N$ in (2) is a physical amplitude inside the integral, not an artificial average over a shifted cap.

There is also a fixed positive-density subfamily of even targets on which $F_N(c_{N,x})$ is strictly increasing in $x$ on the physical interval $7N/16\le x<N/2$, and is uniformly bounded away from $1/2$ towards smaller values. More precisely, take any sufficiently large **fixed** $Z$, let $K_Z=\prod_{p\le Z}p$, and impose $K_Z\mid N$ and $\sum_{p\mid N,\ p>Z}(\log p)/p\le1$. Uniformly over those targets, as $Z$ tends to infinity,

$$
 F_N'(c)=\frac{\|f\|_2^2+o(1)}{\log Z}\quad (|c|\le1),
 \tag{4}
$$

where $f$ is the unit-mass Dickman density of the [primorial radical theorem](r82-spectral-primorial-radical-major-law.md), so $\|f\|_2^2>0$. The derivative here is the continuous difference density. Thus on each such family with $Z$ chosen fixed, the departure from $1/2$ on the physical $c_{N,x}$ is of order $1/\log Z$ and is not part of the little-oh of (3). This also rules out treating the physical boundary value as constant in $x$ in that part of the parity bracket.

## 2. The sole hard endpoint in the predecessor proof

The actual marked arithmetic of the occupancy theorem, §1, applies unchanged: the values $w^{K_Y(m)}$ are bounded by one on the closed disk and no condition $\tau\ne a,b$ was used in common-auxiliary occupation, real-line completion, or long $j$ clips. In its normalized profiles put $f_j(u)=v\kappa_j(vu)$ and $f_{j,w}=f_j+g_{j,w}$. The strong $L^1$ and bounded supremum for $g_{j,w}$ apply for our endpoints too. Furthermore the first-power contribution to $g_{j,w}$ at every fixed $j$ is

$$
 (1-w)(f_j*\nu_v),\qquad
 \nu_v=\sum_{\ell^a<p\le\ell^b}p^{-1}\delta_{\log p/v},
 \tag{5}
$$

up to $o(1)$ in $L^1$ and supremum norm from omissions at $p\mid Nj$ and the exact local logarithm errors. The remaining part tends uniformly on the full line to $h_w$: the proof of [occupancy §2](r87-spectral-exact-band-occupancy-mixed-main.md#2-actual-arithmetic-profiles-converge-to-the-compound-kernel) gives uniform convergence for each convolution power at least two and a uniform factorial tail. These statements hold on the same good radical family $\log\mathcal A(N)\le v^{1/3}$ and uniformly over $|w|\le1$.

In the predecessor's two finite real bracket components (9), the truncated and terminal parts, the integrated autocorrelations and the continuous quadratic autocorrelation at the positive cap use only strong $L^1$, bounded suprema and a signed approximate identity at zero. They therefore have the identical limits computed there, including the upper terminal starting at $U_0<a$. The unmarked autocorrelation and the cross term with $f_j$ in the positively shifted factor have vanishing value at the positive cap, by the same unmarked supremum at positive distance. The contribution of $h_w$ in the other cross term is $h_w(\tau)+o(1)$ by uniform convergence and continuity. Only the first-power positive-shift term from (5) requires a separate computation. More explicitly, with $T=\log(x/D^2)=\tau v+c_{N,x}$, that term at fixed $j$ before its factor $1-w$ is

$$
 \int_{\mathbb R}\kappa_j(r)
       \sum_{\ell^a<p\le\ell^b}\frac{v}{p}\,
                         \kappa_j(T+r-\log p)\,dr .
 \tag{6}
$$

The domains $r\ge0$ and $T+r-\log p\ge0$ are exact, due to the zero extension. The use of signed primitives is important: one cannot replace (6) by an independent unconditioned probability for a band prime.

## 3. Evaluate the cap contact in raw logarithmic coordinates

For each fixed $j$ set $H=v^{3/4}$. The absolute tail integral of $\kappa_j$ above $H$ and $v$ times its supremum there are $o(1)$, uniformly on the good radical family. Indeed write $R_{N,j}$ as ordinary reciprocal Möbius primitive convolved with its positive correcting kernel from the first band proof. The latter has quarter-power exponential moment $\ll\mathcal A(N)\mathcal A(j)$, $M_j\ge1$, and the ordinary primitive has the stretched exponential bound in the raw argument. Splitting at half that argument bounds the supremum by $O_j(e^{v^{1/3}} e^{-c_0\sqrt H})$ and the absolute integral by the corresponding tail integral times fixed powers of $H$, both tending to zero as required. Thus in (6) first take $0\le r\le H$ using $\|f_j*\nu_v\|_\infty\ll1$, and then take $0\le s=T+r-\log p\le H$ using $v\sup_{s>H}|\kappa_j(s)|=o(1)$ and bounded reciprocal band mass. No rescaling of the hard contact by the much larger $v$ has taken place.

With $r$ fixed on this cut, use the ordinary prime number theorem in the Stieltjes test
$v e^{-u}\kappa_j(T+r-u)/u$ against $d\vartheta(e^u)$, where $u=\log p$. Intersect the real half-open band $(av,bv]$ with the actual $0\le T+r-u\le H$. On this intersection $u=\tau v+O(H+1)$, so $v/u=1/\tau+O(H/v)$, and that replacement will cost $o(1)$ in the continuum main. The prime number theorem error is uniform $o(1)$ on the whole clipped test. To see it directly, on the clipped interval $u\asymp v$, use $\vartheta(e^u)-e^u\ll e^u e^{-c_1\sqrt u}$. The variation of $\kappa_j$ on a raw interval in $[0,H]$, including the zero-extension or cut jumps if present, is $O(1+H)$: the primitive has jumps of absolute size at most $1/n$ at $\log n$, and $M_j\ge1$. In Stieltjes summation with this finite variation and the exponential test weight, the factor $e^u$ cancels $e^{-u}$ at each boundary and in each variation integral; the remaining error is $O((1+H)e^{-c_2\sqrt v})$. Right- or left-hand values at coinciding prime and primitive jumps are allowed here: bound endpoint access using the same one-sided discrepancy (or decompose the bounded-variation test into interval indicators with the same hard values). Thus the clipped prime sum is, uniformly in $r$,

$$
 \frac1\tau\int_0^H \kappa_j(s)
           \mathbf1_{av<T+r-s\le bv}\,ds+o(1).
 \tag{7}
$$

The continuum error from $v/u$ is bounded by $O(H/v)\|\kappa_j\|_1$; no interval length loss is needed. Since $H=o(v)$, if $\tau=a$ the upper prime edge is automatically satisfied on the clipped square and the lower edge is exactly $s-r<c_{N,x}$. If $\tau=b$, the lower edge is automatic and the upper edge is exactly $s-r\ge c_{N,x}$. In either case unclip both variables at $o(1)$ absolute cost. Formula (6) is therefore $F_{N,j}(c_{N,x})/\tau+o(1)$ at $\tau=a$, and $(1-F_{N,j}(c_{N,x}))/\tau+o(1)$ at $\tau=b$. These differences are evaluated on the actual raw variable; even a fixed physical shift is not lost.

For fixed $j$, multiply this coefficient by $1-w$ and restore the $h_w$ term above. The contribution is inside the point-value term multiplied by the moving $-T/v$, which tends to $-\tau$ uniformly. The marked ratios $\alpha_j(w)^2/\alpha_j(1)^2$ are bounded on the disk and are identically one eventually at fixed $j$ on nonzero weights, as before. The finite-cutoff part of the occupancy proof discards $j>e^{(B-B_0)\log L/2}$ by $O(1+v)$ bracket norms and the Euler half-moment, and bounds the remaining brackets uniformly using their positive lower cutoffs. The same bounds hold on the limits in (2) and (7), by the uniform absolute norms of $\kappa_j$. One can thus take any fixed finite set of $j$, use (7) on it, then enlarge it using the same Euler half-moment. This replaces the raw factor by the literal $E_N(c_{N,x})$ in (2), without a claim that a raw fixed-$j$ factor has an $N$-independent limit. The remaining prefactor $P(w)/P(1)$ converges uniformly to $e^{2(w-1)m_0}$ as in the occupancy theorem, proving (2) for the actual common auxiliary majors.

Finally unit-circle extraction has norm one for every $k$, even with the physical integrand varying inside $I$. The actual common complementary hard-cut Bessel and original moving minor arguments of the occupancy theorem, §3, apply to each bounded literal count mask; union over the $O(\ell)$ physically possible counts, with two extra inverse-log powers first. Fourier inversion and subtraction of that true original minor prove (3). Neither the auxiliary nor the original arcs have moved in this step.

## 4. Nontrivial variation at the physical endpoint

For the exact fixed threshold $Z$, the unmarked scaled primitive
$f_{K_Z,1}(u)=(\log Z)\kappa_{K_Z,1}((\log Z)u)$ has the strong global $L^2$ limit $f$ by the primorial radical theorem, §2. This part of that proof depends only on the prime mask and not on a polynomial relation of $K_Z$ to a dyadic position. Passing from that analytic base to the same scaled primitive $f_{N,1}^{(Z)}$ for a target with $K_Z\mid N$ gives the exact positive probability convolution of the [planted radical transfer](r84-spectral-planted-ap-radical-full.md#2-perturb-the-genuine-radical-in-log-coordinates). Its first moment is $O((\log Z)^{-1}\sum_{p\mid N,p>Z}(\log p)/p)=O(1/\log Z)$ on the family here. Translation continuity in $L^2$, splitting at a small shift and using Markov for the probability tail, implies $f_{N,1}^{(Z)}\to f$ in $L^2$, uniformly in such $N$. The exact additional $j$ exclusions also act by positive probability convolution from the same analytic base, so $\|f_{N,j}^{(Z)}\|_2\le\|f_{K_Z,1}\|_2\ll1$ for **all** $j$.

If $c_j\ne0$ and $j>1$, every prime in $j$ is $>Z$. Thus $\sum_{j>1}|c_j|\ll Z^{-1/2}$ by the Euler half-moment, and $c_1=1+O(Z^{-1/2})$. Each scaled autocorrelation at lag $c/\log Z$, $|c|\le1$, is bounded by its squared $L^2$ norm; for $j=1$ it tends uniformly to $\|f\|_2^2$ by the strong convergence and translation continuity. Returning to raw coordinates therefore gives $\sum_j c_j C_{\kappa_j}(c)=(\|f\|_2^2+o(1))/\log Z$ uniformly for $|c|\le1$. This sum is continuous, by the same $L^2$ autocorrelation continuity and uniform summable tail. It proves (4). For large $Y$, $c_{N,x}$ on the actual physical interval lies strictly inside $(-1,0)$ and a fixed distance below zero; (1) and (4) give the asserted strictly varying bias.

For completeness this subfamily has positive proportion among all even targets for each sufficiently large fixed $Z$. For $N\in[Y,2Y]$ divisible by $K_Z$, the actual sum of the extra-prime condition's left side is bounded by $2Y/K_Z$ times $\sum_{p>Z}(\log p)/p^2=o(1)$ as $Z\to\infty$, by counting exact positive multiples of $p$ in the quotient. Markov therefore keeps a fixed positive fraction of the multiples, and for each chosen fixed $Z$ the exceptional $O_A(Y\ell^{-A})$ set in (3) has vanishing relative density there. This does not upgrade the statement to arbitrary individual multiples or characterize the sign of $F_N'$ on all even targets.
