# Joint exact prime occupancies in the genuine mixed strip

**Scope.** On one density-one set of even targets this evaluates every joint count in finitely many fixed log-power prime bands, with the actual full and moving polynomial-major Fourier integrals and both true squarefree parities. Overlapping bands count the same actual prime in all the bands containing it. A real cap touching one or several band ends retains a physical arithmetic coefficient. Two examples give opposite signed joint counts on disjoint bands and a two-sided signed contrast at a shared cap end. These are statements about the mixed signed coefficient, not prime counts, prescribed targets, or weak S.

Use the genuine $M_\pm$, admissible fixed $B>B_0>0$, hard $I\subset(N/2,9N/16]$, bounded-BV $\omega$, $x=N-y$, $\Sigma(N)$ and original moving arcs of the [whole mixed theorem](r80-spectral-whole-mixed-parity-density.md). Here $Y\le N\le2Y$ is even, $\ell=\log Y$, $v=\log\ell$, $L=\log N$, $D=\sqrt N L^{-B}$, $U_0=B-B_0$ and $\tau=2B$. Fix $d$ real intervals $J_i=(a_i,b_i]$ with $U_0<a_i<b_i<1$, possibly overlapping or repeating. For a true right integer $m$, set
$K_i(m)=\#\{p\mid m:\log p/v\in J_i\}$.
All these hard prime bands are common throughout the dyad.

For $|w_i|\le1$ write $w_i$ for the $i$th coordinate and define

$$
 \begin{split}
 W(u)&=\prod_{i:u\in J_i}w_i,\qquad
 \lambda(u)=(1-W(u))/u \quad (u>0),\qquad \lambda(u)=0\quad (u\le0),\\
 M&=\int_{\mathbb R}\lambda(u)\,du,\qquad
 g=\sum_{n\ge1}\frac{\lambda^{*n}}{n!},\qquad h=g-\lambda,\qquad
 C_g(s)=\int_{\mathbb R}g(t)g(t+s)\,dt.
 \end{split}
$$

Empty products are one. Dependence on the vector $\mathbf w$ is suppressed; all products of functions and autocorrelations are bilinear. The convolution series converges in $L^1$ and bounded supremum norm uniformly on the closed polydisc, and $h$ is continuous. Let $\lambda_-,\lambda_+$ be the one-sided limits of $\lambda$ at $\tau$.

Define $F_N(c)$ as in the [one-band hard cap theorem](r88-spectral-exact-occupancy-cap-endpoints.md), using the **unmarked** primitive. Explicitly, if $R_{N,j}$ is the genuine unmarked signed reciprocal primitive, $M_j=\int R_{N,j}$, $\kappa_j=R_{N,j}/M_j$ on the raw logarithmic line, and $c_j=P_N\mu(j)\alpha_j^2M_j^2$ are the unmarked signed weights there, then

$$
 F_N(c)=\sum_{j\ {\rm sf}}c_j\iint\kappa_j(r)\kappa_j(s)
                               \mathbf1_{s-r<c}\,dr\,ds,
 \qquad c_{N,x}=\log(x/N)+\tau(\log L-v).
$$

Let $\Lambda_N(x)=\lambda_- (1-F_N(c_{N,x}))+\lambda_+F_N(c_{N,x})$. In particular $\Lambda_N(x)=\lambda(\tau)$ if no band end is at $\tau$. Define

$$
 \begin{split}
 \mathcal U &=1+\tau\int_{U_0}^{\infty}g^2,\qquad
 \mathcal V_N(x)=1+2\int_0^\tau g
       +\int_{-\tau}^{\tau}C_g(s)\,ds
       -\tau\bigl(h(\tau)+\Lambda_N(x)+C_g(\tau)\bigr),\\
 \mathcal B_{\pm,N}(\mathbf w;x)&=\tfrac12 e^{-2M}
                        \bigl(\mathcal U\pm\mathcal V_N(x)\bigr).
 \end{split}                                                    \tag{1}
$$

**Theorem.** For every fixed $A>0$, outside $O_A(Y\ell^{-A})$ even targets, simultaneously for every integer vector $\mathbf k\ge0$, both parities and all usual $I,\omega$, the full signed correlation with $\mathbf1_{\mathbf K(m)=\mathbf k}M_\pm(m)$ is

$$
 \Sigma(N)\int_I\frac{\omega(y)}{\log(N-y)}
                [\mathbf w^{\mathbf k}]\mathcal B_{\pm,N}(\mathbf w;N-y)\,dy
   +o\left(\frac{\Sigma(N)|I|}{L}\right)+O_A(Y\ell^{-A}).            \tag{2}
$$

The same formula holds on the actual original moving polynomial majors. The little-oh is uniform over the asserted family and all joint counts; the bands and $d$ are fixed.

## 1. Literal occupancy multiplier and uniform arithmetic

At a prime actually dividing the squarefree right partner, insert $W(\log p/v)$ once. The product equals $\prod_i w_i^{K_i(m)}$ identically, including weights with a zero coordinate ($0^0=1$). If a prime belongs to several bands, it increases each corresponding count by one; this is not a distinct-prime factorial mark. Insert the product before the [true marginal fold](r66-spectral-above-bv-strip-deletions.md) or the sign twist. All four actual squarefree factors remain pairwise coprime, so the density multiplies by $W_p$ exactly once at an occupied prime no matter which factor contains it, with $W_p=W(\log p/v)$. All actual divisor, interval and unit gates are unchanged.

Use the common polylogarithmic auxiliary arcs of the [one-band occupancy proof](r87-spectral-exact-band-occupancy-mixed-main.md), with an arbitrarily large fixed exponent for the required error. Here the union of the finitely many alphabets has prime product $\exp(O(\ell^{b_*}))=Y^{o(1)}$, $b_*=\max b_i<1$, and bounded reciprocal prime mass. Fixing the actual marked parts on the four right factors works exactly as in that proof, §1: the two-positive-factor errors save a fixed power against $Y^{o(1)}$ allocations, and the polynomial signed-variable progression errors sum harmonically over the actual fixed marked parts. On the closed polydisc, each exact fixed-pattern weight has modulus at most one. Thus neither summation incurs any extra coefficient-norm cost from the markers or the overlap. This uses the same coprime reciprocal sums, hard real completion and summed Ramanujan estimate, not a new distribution assertion for primes in moduli of size $\prod_{p\ {\rm marked}}p$.

The exact local parameters in the [real parity cap](r67-spectral-high-mixed-parity-major.md) become

$$
 d_p=r_p W_p,\qquad \alpha_p(\mathbf w)=\frac{d_p}{p+2d_p},\qquad
 P(\mathbf w)=\prod_p(1-1/p)^2(1+2d_p/p),
 \quad
 r_p=\begin{cases}0,&p\mid N,\\(p-1)/(p-2),&p\nmid N.\end{cases}
$$

The binary left singular series remains $\Sigma(N)$. The denominators of the modified prime factors are nonzero for large $Y$ since all active primes tend to infinity uniformly and $|W_p|\le1$. The clipping argument of the one-band proof also applies: the absolute correcting norm at exponent $1/v$ relative to the ordinary reciprocal primitive increases by at most $\exp(O(\sum_{p\ {\rm marked}}p^{-1+1/v}))=O(1)$. Keep its family $\log\mathcal A(N)\le v^{1/3}$ and its full $O_A(Y\ell^{-A})$ exceptions. The distant artificial clips for $j\le e^{L/20}$ may be removed at the same exponentially small cost, and weighted Euler square tails handle $j>e^{L/20}$. On a nonzero unmarked $j$ weight, $|\alpha_j(\mathbf w)/\alpha_j(\mathbf1)|$ is uniformly bounded: the active factors are each at most $1+O(1/p)$ in absolute value relative to the base, and their reciprocal sum is bounded. It equals one eventually at every fixed $j$; an unmarked zero weight remains zero. Finally prime partial summation, separately on each elementary subinterval cut out by the distinct endpoints, yields $P(\mathbf w)/P(\mathbf1)=e^{-2M}+o(1)$ uniformly on the polydisc. The omitted active primes dividing $N$ have harmonic mass $O(e^{-\min_i a_i\,v/4}\log\mathcal A(N))$, and the local quadratic errors are summable with a vanishing tail.

## 2. Uniform profile and the real contact

Set $f_j(u)=v\kappa_j(vu)$ and $f_{j,\mathbf w}=v R_{N,j,\mathbf w}(vu)/M_j$. Relative to $f_j$ the local correcting measure at an active $p\nmid Nj$ has identity atom and $(\alpha_p(\mathbf1)-\alpha_p(\mathbf w))\sum_{n\ge1}\alpha_p(\mathbf1)^{n-1}\delta_{n\log p/v}$. Its first coefficient is $(1-W_p)/p+O(p^{-2})$ and its higher total variation is $O(p^{-2})$, uniformly. Take its convergent convolution logarithm. The resulting primewise product is $\exp_*(\nu_{v,j}+E_{v,j})$, where

$$
 \nu_{v,j}=\sum_{\substack{p\ {\rm marked}\\p\nmid Nj}}
          \frac{1-W_p}{p}\delta_{\log p/v},\qquad
 \|E_{v,j}\|_{\rm TV}\ll e^{-\min_i a_i\,v}.
$$

For every $j$ the absolute log-bin mass of $\nu_{v,j}$ is $O(1/v)$ on a scaled bin of width $1/v$. With the unmarked normalized positive convolution and its ordinary reciprocal primitive, the bin bound gives $\|f_j*\nu_{v,j}\|_\infty\ll1$. Also $\|f_j\|_1\ll1$ and $\|f_j\|_\infty\ll v$. Thus $g_{j,\mathbf w}=f_{j,\mathbf w}-f_j$ has bounded $L^1$ and supremum norms for all $j$, and the error $E_{v,j}$ contributes $o(1)$ in both. For fixed $j$ on the good family the omitted marked primes can all be restored when computing the limit of this difference, by the same exponentially small reciprocal bound as in §1.

Partition the union into its finitely many intervals cut by all endpoints; the constant multiplier $1-W_p$ is a bounded polynomial in $\mathbf w$ on each piece. By the one-band smearing proof, §2, the first-power contribution tends strongly in $L^1$ to $\lambda$, uniformly away from neighborhoods of the distinct endpoints. This also follows by linear combination of that proof on the separate pieces, with the same raw prime tests and the same zero extension. For the second convolution the bounded mass of any translated endpoint neighborhood is $O(\epsilon+1/v)$ for the measures, and $O(\epsilon)$ for the limiting density, even for complex coefficients by total variation. Approximate the first-power limit by a bounded continuous compactly supported function outside these neighborhoods. Weak prime partial summation and equicontinuity of its compact translate family give uniform convergence of the second power. Strong $L^1$ follows from tightness of the signed primitive and continuity of translations in $L^1$; subsequent powers have the same argument with a continuous limiting input. Factorial tails are uniformly bounded in both norms by the bounded prime mass and first-power supremum. Hence $g_{j,\mathbf w}\to g$ strongly in $L^1$, and its second-and-higher part tends uniformly to $h$. This applies uniformly on the polydisc for fixed $j$, including repeated endpoints.

In the finite real cap of one-band occupancy, §3, put $T_v=\log(x/D^2)/v$ and $U_j=((B-B_0)\log L-\log j)_+/v$. At fixed $j$, $T_v\to\tau$ and $U_j\to U_0$ uniformly. The unmarked $f_j$ is a signed approximate identity with mass one, uniformly concentrated in absolute $L^1$ at zero, and with vanishing positive-distance supremum. Because each band is above $U_0$, the untwisted part $T_v\int_{U_j}^\infty f_{j,\mathbf w}^2+(\int_0^{U_j} f_{j,\mathbf w})^2$ tends to $\mathcal U$. The integrated twisted autocorrelation tends to $1+2\int_0^\tau g+\int_{-\tau}^\tau C_g$. In the endpoint correlation the unmarked pair and the pair with unmarked primitive in the positively shifted factor vanish by the positive-distance supremum. The purely marked autocorrelation tends uniformly to $C_g$, by strong $L^1$ plus the bounded supremum of $g_{j,\mathbf w}$. The remaining pair, unmarked at the first place and marked at the shifted place, contributes $h(\tau)$ from convolution powers at least two.

For its first power the true computation from the hard cap proof, §§2–3, is linear over the elementary intervals. In raw logs $T=\tau v+c_{N,x}$, the prime argument is $u=T+r-s$, with exact hard elementary interval and zero-extended primitive pair $\kappa_j(r)\kappa_j(s)$. The raw tail beyond $v^{3/4}$ is negligible for fixed $j$ even after a factor $v$ in the supremum, by the same stretched-exponential and radical bound. Thus only a neighborhood $u/v=\tau+O(v^{-1/4})$ matters. In this neighborhood, if an endpoint is present the two neighboring pieces correspond exactly to $s-r<c_{N,x}$ on the **upper** piece and $s-r\ge c_{N,x}$ on the **lower** piece (the elementary intervals are open at left, closed at right). If a side is geometrically unmarked its piece weight is zero. In the prime Stieltjes test the normalized factor $v/u=1/\tau+o(1)$ and the piece weight is its constant $1-W$ on that side; together these are $\lambda_+$ or $\lambda_-$ up to $o(1)$. The bounded-variation uniform ordinary PNT step in hard cap §3 applies unchanged to each piece, with at most two pieces near $\tau$ and uniformly bounded complex coefficients. Equality in the resulting double density is null; it has not been removed from the discrete selection. Consequently the raw first-power term equals $\lambda_- (1-F_{N,j}(c_{N,x}))+\lambda_+F_{N,j}(c_{N,x})+o(1)$ for this fixed $j$, with $F_{N,j}$ the summand before the weight $c_j$. This argument also covers no endpoint since then the two side values coincide.

As in one-band occupancy, discard $j>e^{(B-B_0)\log L/2}$ by the uniform crude $O(1+v)$ bracket bounds and the Euler half moment $\sum_jj^{1/2}|c_j|\ll1$. For smaller $j$, the lower cut remains positive uniformly, and $\sup_{u>0}|u f_j(u)|\ll1$ and the marked $L^1$/supremum bounds give $O(1)$ brackets (including the positive-shift autocorrelation at $T_v$). The raw limit summands also have $O(1)$ bounds by the uniform $\|\kappa_j\|_1$ and bounded marked norms. Truncate at a large fixed $j$, pass to the fixed-$j$ formulas uniformly in $x$ and $\mathbf w$, and use the same half moment to let the fixed truncation grow. Since $\sum_j c_j=1$, the exact residual endpoint becomes $\Lambda_N(x)$, without any limit of the raw unmarked factor assumed. The prefactor from §1 completes (1).

## 3. Actual full and original moving majors

For every literal count vector use unit-torus coefficient extraction, whose integration test has norm one. This remains valid inside the physical integral with its $N,x$-dependent norm-bounded coefficient. The auxiliary complementary Fourier estimate in whole mixed parity with a fixed mask applies to each exact common indicator $\mathbf1_{\mathbf K(m)=\mathbf k}$, with the original hard cuts, since this is a fixed dyad-wide bounded multiplier on the integer $m$. The number of possible vectors on the actual integer support, uniformly in the dyad, is $O_d(\ell^d)$: each prime divisor consumes at least $\log 2$ in the total logarithm of such an integer. Request $d+2$ extra inverse-log powers first and take this finite union. Outside the actual possible vectors the Fourier polynomial is zero and the auxiliary-major uniform extraction error is already the error for those coefficients. This proves (2) by full Fourier inversion. The [genuine original moving minor](r79-spectral-original-minor-power-exception.md) accepts the same actual fixed masks and either true parity; its power losses absorb the same finite union. Subtract that minor to prove (2) on the original moving polynomial majors. No modulus hypotheses are used.

## 4. Two disjoint narrow bands: opposite joint signs

Take $d=2$ and fix $U_0<a_1<a_2<\min(B,1)$, with $a_2<2a_1$ and with $\tau$ different from all sums of three of the $a_i$, allowing repetition. When $U_0<1$ such choices are possible in a nonempty open interval since $U_0<B$. Take $J_i=(a_i,a_i+\delta]$ with $\delta>0$ sufficiently small and fixed, so they are disjoint and all sums of two points in their union are below $\tau$ and above their own upper endpoints; the threefold sums avoid $\tau$. Write $x_i=1-w_i$, $\rho_i(u)=\mathbf1_{J_i}(u)/u$, $m_i=\int\rho_i$ and $s_i=\int\rho_i^2$. Then $\lambda=x_1\rho_1+x_2\rho_2$ has $\|\lambda\|_1=O(\delta)$ and $\|\lambda\|_\infty=O(1)$. The term of degree $n$ in $g$ has $L^1$ norm $O(C^n\delta^n/n!)$ and supremum $O(C^n\delta^{n-1}/n!)$. In any correlation of total degree at least four these bounds give $O(\delta^3)$ pointwise by one $L^1$ and one supremum norm, and $O(\delta^4)$ in $L^1(ds)$. For degree three in $\int g^2$, the first- and second-power supports are disjoint by the choice $a_2<2a_1$ and small $\delta$. The first-power squares have disjoint bands. It follows that

$$
 \mathcal U=1+\tau(s_1x_1^2+s_2x_2^2)+O(\delta^3).
$$

In $\mathcal V_N$, all degree-one and degree-two mass in $g$ lies below $\tau$, and the only degree-two correlation has its entire difference support inside $[-\tau,\tau]$. Thus the integrated terms agree with full integrals up to $O(\delta^3)$ using the $L^1$ norms. The point values of first through third power in $g$ vanish at $\tau$ by the separations; the fourth-and-higher terms are $O(\delta^3)$ in supremum. The point correlation terms of total degree at most three also vanish there: each of their two supports lies below $\tau$ and above zero. Hence $\mathcal V_N=e^{2M}+O(\delta^3)$ since the whole integrated bracket equals $(1+\int g)^2=e^{2M}$ before the point terms. All these bounds are uniform on the polydisc as $\delta\downarrow0$. There is no contact in this example.

In (1), $e^{-2M}\mathcal V_N=1+O(\delta^3)$, so both true parities give the same coefficients through this precision at the nonzero joint indices below. Expanding $e^{-2M}$ with $M=m_1x_1+m_2x_2$ and extracting exact coefficients gives

$$
 \begin{split}
 [w_1w_2]\mathcal B_{\pm,N}
     &=2m_1m_2-2\tau(s_1m_2+s_2m_1)+O(\delta^3)<0,\\
 [w_1^2w_2]\mathcal B_{\pm,N}
     &=\tau s_1m_2+O(\delta^3)>0,\qquad
 [w_1w_2^2]\mathcal B_{\pm,N}
     =\tau s_2m_1+O(\delta^3)>0.
 \end{split}
$$

Indeed $s_i/m_i=1/a_i+O(\delta)$, $m_i\asymp\delta$ and $\tau>a_i$. Terms omitted in the expansion cost $O(\delta^3)$ in coefficient norm at these individual indices by the unit-torus test. These are literal two-band signed slices with $\omega=1$ on physical intervals of any fixed inverse-log fractional length, using (2) with the required power. The sign of the joint $(1,1)$ is not obtained by multiplying signs of its two marginals.

## 5. Abutting bands: a signed two-sided contact contrast

Assume $U_0<\tau<1$ and take $J_1=(\tau-\delta,\tau]$, $J_2=(\tau,\tau+\delta]$, for a sufficiently small fixed $\delta>0$. The two touching one-sided values yield **exactly**

$$
 \tau\Lambda_N(x)=(1-w_1)(1-F_N(c_{N,x}))+(1-w_2)F_N(c_{N,x}).
$$

For these narrow bands, $\|g\|_1=O(\delta)$ and $\|g\|_\infty=O(1)$ by the same factorial bounds, $\|h\|_\infty=O(\delta)$, and $e^{-2M}=1+O(\delta)$. Consequently $\mathcal U=1+O(\delta)$ and $\mathcal V_N=1-\tau\Lambda_N(x)+O(\delta)$ uniformly on the polydisc; $\Lambda_N$ is bounded uniformly by the raw primitive product norms. In particular

$$
 \begin{split}
 [w_1^1w_2^0]\mathcal B_{\pm,N}(\mathbf w;x)
     &=\pm\tfrac12(1-F_N(c_{N,x}))+O(\delta),\\
 [w_1^0w_2^1]\mathcal B_{\pm,N}(\mathbf w;x)
     &=\pm\tfrac12 F_N(c_{N,x})+O(\delta).
 \end{split}
$$

These coefficients compare actual occupation on opposite sides of the same physical contact, not different arbitrary endpoint conventions. The nontrivial variation statement in hard cap §4 gives, for a sufficiently large **fixed** $Z$, a positive-density subfamily with $1-2F_N(c_{N,x})\gg1/\log Z$ uniformly throughout the physical interval. In detail $c_{N,x}$ is a bounded fixed distance below zero there for large $Y$, $F_N(0)=1/2$, and the continuous derivative on $[-1,1]$ is $(\|f\|_2^2+o(1))/\log Z$ as fixed $Z$ is taken large. The absolute implicit $O(\delta)$ above is uniform in $N,x,Z$ for fixed $\tau$. Fix $Z$ first, then take $\delta$ sufficiently small compared to $1/\log Z$. Thus the signed difference $(1,0)$ minus $(0,1)$ has a strictly positive leading amplitude in $+$ and a strictly negative one in $-$, both bounded away from zero on that same subfamily. This gives the same separation for the true full and original major integrals with $\omega=1$ and any fixed inverse-log fractional length of $I$ by (2), removing its negligible exception set. The use of fixed $Z$ does not claim every primorial multiple, and nothing here controls the exterior or weak S.
