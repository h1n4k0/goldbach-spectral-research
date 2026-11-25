# Exact prime occupancy in a log-power band of the genuine mixed strip

**Scope.** This is an exact integer-count selector, not a factorial or logarithmically weighted moment. It gives the unconditional original full and moving polynomial-major asymptotics for each number of occupied primes in one fixed band, on the same density-one family of even targets. Two narrow-band count classes have opposite signed main terms in **both** actual squarefree parities. There is no claim about positivity of the prime correlation, prescribed even integers, or weak S.

Use the true above-BV mixed coefficient $M_>$ and the two literal parities $M_\pm=(1\pm\mu(m))M_>/2$ of the [whole mixed theorem](r80-spectral-whole-mixed-parity-density.md). Retain its hard $I$, bounded-BV left $\omega$, physical $x=N-y$, original polynomial arcs, and singular series $\Sigma(N)$. Let $Y\le N\le2Y$, $\ell=\log Y$, $v=\log\ell$, $L=\log N$, and retain fixed admissible $B>B_0>0$. Put $U_0=B-B_0$, $\tau=2B$. Fix

$$
                  U_0<a<b<1,\qquad \tau\notin\{a,b\}.
$$

Let $J=(a,b]$ and $\rho(u)=\mathbf1_J(u)/u$, $m_0=\int\rho=\log(b/a)$. The right integer contains exactly
$K_Y(m)=\#\{p\mid m:p\ {\rm prime},\,\ell^a<p\le\ell^b\}$
primes in the band. All quantities specifying this count are common to the dyad. In particular this is not a weighted sum of logarithms in the band.

For a complex variable $w$ define on the real line

$$
 \begin{split}
 g_w &=\sum_{k\ge1}\frac{(1-w)^k}{k!}\rho^{*k},\\
 C_{g_w}(s)&=\int_{\mathbb R}g_w(t)g_w(t+s)\,dt,\\
 \mathcal U(w)&=1+\tau\int_{U_0}^{\infty}g_w(t)^2\,dt,\\
 \mathcal V(w)&=1+2\int_0^\tau g_w(s)\,ds+
       \int_{-\tau}^{\tau}C_{g_w}(s)\,ds-\tau\bigl(g_w(\tau)+C_{g_w}(\tau)\bigr),\\
 \mathcal B_\pm(w)&=\frac12 e^{2(w-1)m_0}\bigl(\mathcal U(w)\pm\mathcal V(w)\bigr).
 \end{split}
 \tag{1}
$$

Convolutions are on the real line, the density is zero on the negative half-line, and products are bilinear, not Hermitian. The series defining $g_w$ is locally uniformly convergent in $L^1$ and in supremum norm, with its sole possible jumps at $a,b$. In particular its value at the positive point $\tau$ is the continuous value and does not depend on how $\rho$ is defined at its endpoints.

**Theorem.** For every fixed $A>0$, outside $O_A(Y\ell^{-A})$ even targets and simultaneously for all integers $k\ge0$, either true parity, and all usual $I,\omega$, the actual full signed correlation with $\mathbf1_{K_Y(m)=k}M_\pm(m)$ is

$$
 [w^k]\mathcal B_\pm(w)\,\Sigma(N)\int_I\frac{\omega(y)}{\log(N-y)}\,dy
       +o\left(\frac{\Sigma(N)|I|}{L}\right)+O_A(Y\ell^{-A}).
 \tag{2}
$$

The identical formula holds on the actual original moving polynomial majors. The little-oh is uniform, including in $k$. If $\tau>a$, $\tau/a$ is not an integer, and $b=a+\delta$ with $\delta>0$ sufficiently small and fixed, then for both signs

$$
 [w]\mathcal B_\pm(w)=m_0(1-\tau/a)+O_{a,\tau}(\delta^2)<0,\qquad
 [w^2]\mathcal B_\pm(w)=\frac{\tau m_0}{2a}+O_{a,\tau}(\delta^2)>0.
 \tag{3}
$$

Thus even exact one-prime occupancy is a negative leading slice of the signed mixed coefficient on this band; its positive logarithmically weighted first moment is not a positivity statement for the count slices.

## 1. Insert the literal count in the rational completion

At each occupied right prime in the band insert $w$, and outside the band insert $1$. Squarefreeness and pairwise coprimality of the four true factors give the exact factor $w^{K_Y(m)}$, with $0^0=1$. Put $w_p=w$ in the band and $1$ otherwise. This insertion precedes the exact above/below signed fold and the real Möbius parity twist. It changes no actual divisor or interval gate.

On the common auxiliary caps $q\le Q_0=\ell^D$ with slow radius $2Q_0/Y$ (use a separate fixed exponent $D$ in this paragraph only), invoke the coefficient-norm arithmetic of [the first band theorem](r85-spectral-log-power-band-marked-main.md), §1, and [the bounded-pattern completion](r83-spectral-adaptive-bounded-pattern-main.md), §1. The same proof gives the marked completed density uniformly on $|w|\le1$. Indeed the actual band alphabet has prime product $\exp(O(\ell^b))=Y^{o(1)}$ and bounded reciprocal prime mass. Fix the true marked part in every variable: scales of unmarked signed variables are still polynomial, their masked Möbius progression errors sum harmonically over that part, and the true two-positive-variable floors save a fixed power against $Y^{o(1)}$ positive allocations. Multiplying a fixed pattern by its $w$-weight has modulus at most one, so no additional error is introduced in either the arithmetic occupation estimate or the coefficient-norm Ramanujan tail. The left primes, hard ends, variation bound and uniform extension of the real integral are unchanged. This is the same argument as for the first band theorem, only with bounded pattern weights instead of a logarithmic-cost derivative.

In the exact real bracket of the [true parity cap](r67-spectral-high-mixed-parity-major.md), the modified local parameters are

$$
 d_p(w)=r_pw_p,\qquad \alpha_p(w)=\frac{d_p(w)}{p+2d_p(w)},\qquad
 P(w)=\prod_p(1-1/p)^2(1+2d_p(w)/p),
 \tag{4}
$$

where $r_p=0$ at $p\mid N$ and $r_p=(p-1)/(p-2)$ otherwise. The binary singular factor remains $\Sigma(N)$; the prime multiplier applies exactly once at actual right occupation. All marked primes tend uniformly to infinity, so the displayed denominators are nonzero on the closed disk $|w|\le1$ for sufficiently large $Y$. The possible complex values cause no problem in identities of real signed primitives: their products remain bilinear. The correcting log-convolution relative to unmodified reciprocal Möbius has weighted variation at exponent $1/v$ bounded by $O(\mathcal A(N)\mathcal A(j))$ uniformly in this disk, with $\mathcal A$ the positive [quarter-power radical factor](r81-spectral-radical-criterion-and-log-exceptions.md): the band costs only $\exp(O(\sum_{p\in J}p^{-1+1/v}))=O(1)$, exactly as in the first-band clipping argument. Here and below a prime in $J$ means $\log p/v\in J$. Consequently the distant $L/10-\log j$ clips may be removed uniformly, first for $j\le e^{L/20}$ with the same $e^{-c\sqrt L}+e^{-cL/v}$ errors, and for the rest by the weighted Euler square tail. This uses only the unmarked radical restriction $\log\mathcal A(N)\le v^{1/3}$ from the first band theorem. Its exceptions are $O_A(Y\ell^{-A})$ for every fixed $A$; the clipping errors are smaller than any required inverse logarithm. The local ratio $|\alpha_j(w)/\alpha_j(1)|$ is uniformly bounded where the denominator is nonzero: for an active marked prime use $|\alpha_p(w)/\alpha_p(1)|\le1+O(p^{-1})$, and sum over the bounded total reciprocal band mass. Zero coefficients stay zero.

## 2. Actual arithmetic profiles converge to the compound kernel

In the first-band notation, let $M_j=\int R_{N,j,1}$ be the unmarked primitive mass, and put

$$
 f_j(u)=\frac{v}{M_j}R_{N,j,1}(vu),\qquad
 f_{j,w}(u)=\frac{v}{M_j}R_{N,j,w}(vu).
$$

Both vanish below zero. We always normalize by the unmarked mass. The first-band estimates give for all $N,j$: $\|f_j\|_1\ll1$, $\|f_j\|_\infty\ll v$, $\|f_j\|_2^2\ll v$, $\sup_{u>0}|u f_j(u)|\ll1$. For each fixed $j$, uniformly on the good radical family, $f_j$ is a signed approximate identity with total integral one, bounded absolute integral concentrated at zero, and $\sup_{u\ge\epsilon}|f_j(u)|=o(1)$ for fixed $\epsilon>0$.

At $p\nmid Nj$ in the band the exact local correction relative to the unmarked primitive, as a convolution measure in scaled log coordinate, is

$$
 \delta_0+(\alpha_p(1)-\alpha_p(w))
        \sum_{n\ge1}\alpha_p(1)^{n-1}\delta_{n\log p/v}.
 \tag{5}
$$

No correction occurs at any inactive $p$. The $n=1$ coefficient is $(1-w)/p+O(p^{-2})$, uniformly on the disk, and the higher-power total variation is $O(p^{-2})$. Since the nonidentity term has norm $O(1/p)$, take its convolution logarithm by the absolutely convergent power series. Summing shows that the product of (5) over active primes is exactly

$$
 \exp_*\bigl((1-w)\nu_{v,j}+E_{v,j,w}\bigr),\qquad
 \nu_{v,j}=\sum_{\substack{p\in J\\p\nmid Nj}}\frac{\delta_{\log p/v}}p,\qquad
 \|E_{v,j,w}\|_{\rm TV}\ll e^{-a v},
 \tag{6}
$$

where $\exp_*=\sum_{n\ge0}(\cdot)^{*n}/n!$ with zeroth term $\delta_0$. All errors are supported on the nonnegative half-line, and the bounds hold for every $j$. Set $g_{j,w}=f_{j,w}-f_j$. The contribution of $E_{v,j,w}$ to $g_{j,w}$ is $o(1)$ in $L^1$ and supremum norm, by the bounded band mass and $\|f_j\|_\infty\ll v$. The measure $\nu_{v,j}$ has mass $O(1/v)$ per scaled bin of width $1/v$ by the elementary upper bound for primes. The log-bin convolution argument of the first-band theorem therefore gives $\|f_j*\nu_{v,j}\|_\infty\ll1$ (use its positive probability convolution with the ordinary reciprocal primitive), so the entire series in (6) gives

$$
                 \|g_{j,w}\|_1+\|g_{j,w}\|_\infty\ll1
          \quad\text{uniformly in }N,j,|w|\le1.
 \tag{7}
$$

For each fixed $j$, the omission in $\nu_{v,j}$ has norm $O(e^{-a v/4}\log\mathcal A(N))$ from $p\mid N$, and no contribution from $p\mid j$ eventually. Replacing it by $\nu_v=\sum_{p\in J}p^{-1}\delta_{\log p/v}$ thus costs $o(1)$ in the norms of $g_{j,w}$. By prime partial summation $\nu_v$ converges weakly to $\rho(u)\,du$. Also $f_j*\nu_v$ converges strongly to $\rho$ in $L^1$, and uniformly on the complement of fixed neighborhoods of $a,b$. This is the first-band smearing calculation: on scaled interior intervals, the prime Chebyshev Stieltjes test is the same as there multiplied by the smooth factor $v/\log p$ on a compact band away from zero; its main term tends uniformly to $1/u$ and the error still tends uniformly to zero. The hard endpoints are controlled by the log-bin bound; off the band use the primitive tail and split the positive probability convolution at a fixed small shift, whose omitted mass tends to zero. This also gives uniform convergence on the positive-distance unbounded upper tail. Tightness for the $L^1$ assertion follows by the same convolution tail bounds.

For $n=2$, $(f_j*\nu_v)*\nu_v$ converges **uniformly on the whole line** to $\rho*\rho$. To see this, approximate $\rho$ by a fixed compactly supported continuous function equal to it outside arbitrarily small neighborhoods of the two jumps, with bounded approximation. The mass of any translated jump neighborhood under $\nu_v$ is $O(\epsilon+1/v)$ by the log-bin bound, and likewise $O(\epsilon)$ under $\rho(u)\,du$. Off the neighborhoods use the uniform approximation of $f_j*\nu_v$. For a fixed continuous approximation, weak convergence gives uniform convergence after convolution: its family of translates on the compact input supports is equicontinuous and has a finite uniform approximation net, and only a compact range of output translations can contribute. Strong $L^1$ convergence again follows from strong first-factor convergence and bounded weak measures by continuity of translations into $L^1$. Iterating with the continuous compactly supported convolution limits gives both strong $L^1$ and uniform convergence for every fixed $n\ge2$. Uniform norm bounds by $C^n$ and the factorial denominators allow the series tails to be removed uniformly for $|w|\le1$. We conclude for fixed $j$

$$
 g_{j,w}\longrightarrow g_w \text{ in }L^1,\qquad
 g_{j,w}\longrightarrow g_w \text{ uniformly away from }a,b,
 \tag{8}
$$

uniformly in $w$ and in the good radical family. In particular it is valid at moving points tending to $\tau$ when $\tau\ne a,b$. No discrete step value at a band boundary has been replaced by a weak limit.

## 3. Evaluate the finite real cap, then select exact occupancies

Let $T_v=\log(x/D^2)/v$ where here $D=\sqrt N L^{-B}$ is the original physical divisor cutoff, and $U_j=((B-B_0)\log L-\log j)_+/v$. For fixed $j$, $T_v\to\tau$ and $U_j\to U_0$ uniformly on the physical $x$. With the common unmarked normalization, the two parts of the parity cap for input $F=f_{j,w}$ are

$$
 T_v\int_{U_j}^\infty F^2+\left(\int_0^{U_j}F\right)^2,\qquad
 \int_{-T_v}^{T_v}C_F(s)\,ds-T_v C_F(T_v).
 \tag{9}
$$

For the first part, $f_j$ contributes one in the truncated integral and vanishes in the terminal square, including its cross term with $g_{j,w}$ by (7) and concentration. The limit $g_w$ is supported above $a>U_0$. Strong $L^1$ and bounded supremum give strong $L^2$ for $g_{j,w}$. The limit is $\mathcal U(w)$.

For the second part, the autocorrelation of $f_j$ puts total mass one inside the positive-width cap and tends to zero at its positive endpoint. The two cross correlations with $g_{j,w}$ converge strongly in $L^1(ds)$ to $g_w(s),g_w(-s)$ by (8) and the signed approximate identity. At the positive endpoint, $\int f_j(u)g_{j,w}(u+T_v)du\to g_w(\tau)$: first restrict the concentrated absolute $f_j$ to a small neighborhood of zero, where (8) and continuity at $\tau$ apply, then decrease its width. The opposite term with $f_j(u+T_v)$ vanishes by the unmarked positive-distance supremum and (7). The quadratic autocorrelations of $g_{j,w}$ converge globally in $L^1(ds)$ by strong $L^1$, and uniformly by (7) and the same strong convergence. They therefore give exactly the continuous correlation and its positive endpoint in (1). This is the $\mathcal V(w)$ limit. In particular keeping $-\tau g_w(\tau)$ is necessary even where $\tau$ lies inside the original band.

Now sum (9). As in the [two-band factorial theorem](r86-spectral-two-band-factorial-mixed-main.md), the exact unmarked signed weights $c_j=P(1)\mu(j)\alpha_j(1)^2 M_j^2$ obey $\sum_jc_j=1$, $\sum_jj^{1/2}|c_j|\ll1$. The additional factor of the marked $\alpha_j(w)^2/\alpha_j(1)^2$ is uniformly bounded by §1 and is identically one eventually at every fixed $j$. The fixed tail $j>e^{(B-B_0)\log L/2}$ is negligible by the uniform crude $O(1+v)$ bounds from (7) and the norms of $f_j$. For the remaining $j$, both positive cutoffs in (9) stay bounded away from zero, and $\sup_{u>0}|u f_j(u)|\ll1$ with (7) makes (9) uniformly bounded. Thus the fixed-$j$ limits may be summed. Finally the actual local ratio in (4) satisfies, uniformly on $|w|\le1$,

$$
        P(w)/P(1)\longrightarrow \exp\bigl(2(w-1)m_0\bigr)
$$

by log expansion, the exponentially small marked $p^{-2}$ corrections and the same omission of marked $p\mid N$. The two true parity halves give (1) as the genuine auxiliary-major generating coefficient. The convergence is uniform in the full closed unit disk, physical $x$, and good targets. At $w=1$ this recovers $\mathcal B_+(1)=1$ and $\mathcal B_-(1)=0$.

Extract the coefficient $[w^k]$ by the unit-circle integral in $w$. Its test has norm one for every integer $k\ge0$, so the error and little-oh remain uniform; the input coefficient is exactly the count selector even when $k=0$. Fourier inversion on the auxiliary complement uses the actual fixed common right count mask and either true parity, at no multiplier norm loss. The maximal hard-cut Bessel statement of the whole mixed theorem applies to each $k$. There are only $O(\ell)$ possible $k$ on the original $m\in[N/3,2N]$ support, simultaneously throughout the dyad, so union over these masks retaining arbitrary inverse-log exceptions by first requesting two extra powers. Beyond this range the finite actual right polynomial has zero coefficient, and the auxiliary-major uniform error already controls the purported leading term at those $k$. The genuine [original moving minor](r79-spectral-original-minor-power-exception.md) uses the same fixed count mask and parity; its power exception and bound also absorb the union loss. Subtract it from the full formula to obtain (2) on the original moving majors. There is no pointwise claim, and no RH or GRH input in (2).

## 4. Two explicit opposite count signs

For fixed $\tau>a$ with $\tau/a$ not an integer, take $\delta$ small enough that $\tau$ lies outside every $n$-fold sum interval $[na,n(a+\delta)]$, $n\ge1$; only finitely many intervals have $na<\tau$. In particular $g_w(\tau)=0$ and the first band lies wholly below $\tau$. Write $g_w=(1-w)\rho+h_w$. Since $\|\rho\|_1=m_0=O_a(\delta)$ and $\|\rho\|_\infty\le1/a$, the series has $\|h_w\|_1=O_a(\delta^2)$ and $\|h_w\|_\infty=O_a(\delta)$ on the unit disk. With $s_0=\int\rho^2=m_0/a+O_a(\delta^2)$ this gives

$$
 \mathcal U(w)=1+\tau(1-w)^2s_0+O_{a,\tau}(\delta^2),\qquad
 \mathcal V(w)=1+2(1-w)m_0+O_{a,\tau}(\delta^2).
$$

For the first identity all positive support lies beyond $U_0$ and the cross/tail integrals are $O(\delta^2)$. In the second, the integrated autocorrelation is $O(\|g_w\|_1^2)$, its point-value first-first term is zero because the width of $J$ is below $\tau$, and all its terms involving $h_w$ are $O(\delta^2)$ by the given norms. Thus the generating perturbation to **both** unmarked parity values is $-m_0(1-w)+(\tau s_0/2)(1-w)^2+O_{a,\tau}(\delta^2)$ uniformly on $|w|\le1$. Extracting the two coefficients proves (3): each linear term in $\delta$ has the stated strict sign for sufficiently small fixed $\delta$. This sign comparison only concerns the actual signed mixed-strip asymptotics (2), not primes being counted by a positive measure.
