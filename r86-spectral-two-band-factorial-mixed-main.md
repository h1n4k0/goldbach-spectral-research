# A two-band factorial moment of both actual mixed-strip parities

**Scope.** This computes a genuine ordered **distinct-prime** second moment of the actual above-BV mixed cutoff coefficient. The two bands may coincide or overlap. Besides the product of their logarithmic lengths there is a separate overlap term from the literal finite lower cutoff. The result is unconditional for the true full and original moving polynomial-major integrals on a density-one family. It is not a positive counting measure or an estimate on a prescribed even modulus.

Use the exact setup of the [first log-power band theorem](r85-spectral-log-power-band-marked-main.md), including $Y\le N\le2Y$, $\ell=\log Y$, $v=\log\ell$, $L=\log N$, the usual hard $I$ and bounded-BV left $\omega$, the same physical support $V$, and the exact right squarefree parities $M_\pm=(1\pm\mu(m))M_>/2$. In particular $M_>$ is the genuine above-BV mixed coefficient before external subtraction. Keep fixed admissible $B>B_0>0$, so $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$. Put $U_0=B-B_0$ and $\tau_0=2B$.

Take fixed real intervals $J_i=(a_i,b_i]$ for $i=1,2$ satisfying

$$
             U_0<a_i<b_i<1,\qquad b_1+b_2<\tau_0.
$$

Write $m_i=b_i-a_i$, $m_{12}=|J_1\cap J_2|$ for their ordinary real lengths, and define the actual weights

$$
 \begin{split}
  u_i(p)&=\frac{\log p}{v}\mathbf1_{\log p/v\in J_i},\\
  W_{12}(m)&=\sum_{\substack{p,q\mid m\\p,q\ {\rm prime},\ p\ne q}}
                                   u_1(p)u_2(q).
 \end{split}
$$

The condition $p\ne q$ is literal even in the overlap. When $J_1=J_2$, this is the ordered, log-weighted factorial moment, not the square of the previous mark.

**Theorem.** For every fixed $A>0$, outside $O_A(Y\ell^{-A})$ even targets and simultaneously for either parity and all the usual $I,\omega$, the actual full signed correlation with $W_{12}(m)M_\pm(m)$ is

$$
 \left(2m_1m_2+2B\,m_{12}\right)
              \Sigma(N)\int_I\frac{\omega(y)}{\log(N-y)}\,dy
       +o\!\left(\frac{\Sigma(N)|I|}{L}\right)+O_A(Y\ell^{-A}).
 \tag{1}
$$

The identical statement holds for the actual original polynomial-major integral. The little-oh is uniform on that family. In particular a single band of width $m_1$ has leading signed coefficient $2m_1^2+2B\,m_1$ for its factorial mark, despite the zero leading term of unmarked odd parity.

## 1. Two true tags and the differentiated real bracket

At each actual occupied prime insert $1+t_1u_1(p)+t_2u_2(p)$, with no mixed term at that prime. The coefficient of $t_1t_2$ in the product is exactly $W_{12}$; this proves algebraically that even at an overlapping prime no self-pair is introduced. As in Section 1 of the first band theorem the insertion is before the true signed above/below identity and before the real parity twist. Give the band union independent prime markers first. Its prime product has logarithm $O(\ell^{\max b_i})=o(\ell)$, its reciprocal harmonic prime sum is bounded, and positive marked-part allocations number $Y^{o(1)}$. Thus the coefficient-norm arithmetic, polynomial lower bounds for the rescaled large variables, and exact hard gates of that section apply. The derivative costs a fixed log power because $0\le W_{12}(m)\le(\log m/v)^2=O(\ell^2)$ on the actual support; the signed progression errors still sum by $1/s$ over true marked parts. The fixed common auxiliary arc cap is $Q_0=\ell^K$ with $K$ chosen sufficiently large. Rational completion and slow-radius real extension in coefficient norm follow with arbitrary inverse-log accuracy, using the same mean Ramanujan tail and absolute occupation bound.

In the real parity bracket the exact local quantities are

$$
  d_p(t)=r_p(1+t_1u_1(p)+t_2u_2(p)),\quad
  \alpha_p(t)=\frac{d_p(t)}{p+2d_p(t)},\quad
  P(t)=\prod_p(1-1/p)^2(1+2d_p(t)/p),
 \tag{2}
$$

where $t=(t_1,t_2)$, $r_p=0$ at $p\mid N$ and $r_p=(p-1)/(p-2)$ otherwise. This is the literal local occupied-prime rule of the [marked completion](r83-spectral-adaptive-bounded-pattern-main.md); the singular series remains $\Sigma(N)$. The right signed primitive with extra gcd cutoff $j$ is $R_{N,j,t}$ with mark-dependent $\alpha_p(t)$, zero below zero. Distant artificial clips $L/10-\log j$ in the cap calculation can be removed before differentiating: on a fixed complex bidisk $|t_i|\le1/8$, the $1/v$ exponential moment of its log-convolution kernel relative to ordinary reciprocal Möbius is $O(\mathcal A(N)\mathcal A(j))$ as in the first band theorem. Indeed the marked-prime cost is only $\exp(O(\sum_{p:\log p/v\in J_1\cup J_2}p^{-1+1/v}))=O(1)$, and $\alpha_p(t)\ll p^{-1}$ uniformly. Here $\mathcal A$ is the [quarter-power radical factor](r81-spectral-radical-criterion-and-log-exceptions.md). The long tails at argument $\gg L$ are $O(\mathcal A(N)\mathcal A(j)(e^{-c\sqrt L}+e^{-cL/v}))$ and the large $j$ have a convergent weighted Euler square tail; Cauchy's estimate on the bidisk transfers this to the mixed derivative. Restrict henceforth to the same good radical family $\log\mathcal A(N)\le v^{1/3}$, outside $O_A(Y\ell^{-A})$, so these errors are negligible. This justifies using the differentiated exact real bracket, rather than differentiating an uncontrolled infinite arithmetic sum.

## 2. The first and mixed profile derivatives

Let $M_j=\int R_{N,j,0}$ be the **unmarked** positive primitive mass. Use normalized profiles on the real line

$$
 f_j(x)=vR_{N,j,0}(vx)/M_j,\quad
 g_{j,i}(x)=v\partial_iR_{N,j,t}(vx)|_0/M_j,\quad
 h_j(x)=v\partial_1\partial_2R_{N,j,t}(vx)|_0/M_j .
$$

All are supported on the nonnegative half-line. Here the normalization by $M_j$ is held fixed in both derivatives. For every $j$, $\|f_j\|_1\ll1$, $\int f_j=1$, $\|f_j\|_2\ll\sqrt v$, $\|f_j\|_\infty\ll v$ and $\sup_{x>0}|xf_j(x)|\ll1$. These are the unmarked bounds from the first band theorem, which include the uniform position derivative argument of the [AP-radical major law](r83-spectral-ap-radical-major-law.md). For fixed $j$ on our good family, $f_j$ is a signed approximate identity of mass one, with absolute mass concentrated at zero and supremum $o(1)$ at any fixed positive distance from zero.

For each active $p\nmid Nj$, the correcting ratio relative to the unmarked local primitive has constant term the unit atom and derivative log-shift measure

$$
 L_{p,i}=-\partial_i\alpha_p(0)
            \sum_{k\ge1}\alpha_p(0)^{k-1}\delta_{k\log p/v},
 \qquad
 \partial_i\alpha_p(0)
       =u_i(p)\alpha_p(0)(1-2\alpha_p(0)).
 \tag{3}
$$

Put $\Lambda_{j,i}=\sum_pL_{p,i}$, summing only actual active primes. The first band proof gives $g_{j,i}=f_j*\Lambda_{j,i}$ with $\|g_{j,i}\|_1+\|g_{j,i}\|_\infty\ll1$ uniformly in $N,j$, and for fixed $j$,

$$
             g_{j,i}\longrightarrow g_i=-\mathbf1_{J_i}
                 \text{ in }L^1,\qquad
       \sup_{x\ge b_i+\epsilon}|g_{j,i}(x)|\longrightarrow0
                            \quad(\epsilon>0).
 \tag{4}
$$

The corresponding measures $\Lambda_{j,i}$ converge weakly as finite signed measures to $g_i(x)dx$ and have uniformly bounded variation. This last assertion follows directly from (3), or from the replacement by $-\sum_{p:\log p/v\in J_i}(\log p)/(vp)\,\delta_{\log p/v}$ in that proof: omitted actual $p\mid N$ cost $O(e^{-a_i v/4}\log\mathcal A(N))$, fixed $j$ eventually omits no band prime, and the higher powers and first-power coefficient correction have variation $O(e^{-a_i v})$. Prime partial summation gives the ordinary Lebesgue limit of the displayed log-prime measure, including the true weak upper endpoints. The total variation above $b_i+\epsilon$ tends to zero, even uniformly for all $N,j$, since there it comes only from higher powers.

Differentiating the finite product of local correction factors gives the exact mixed kernel $\Lambda_{j,1}*\Lambda_{j,2}+E_j$. At an overlapping prime subtract $L_{p,1}*L_{p,2}$, because this term in the product of the two summed first derivatives would apply both derivatives to independently inserted factors at the **same** prime. Include instead the true local mixed derivative
$-\partial_{12}\alpha_p(0)\sum_{k\ge1}\alpha_p(0)^{k-1}\delta_{k\log p/v}$. There is no contribution at an excluded prime. By (2), $\partial_{12}\alpha_p(0)=O(p^{-2})$ at these marked primes, and each $L_{p,i}$ has norm $O(p^{-1})$. Thus $\|E_j\|_{\rm TV}\ll e^{-\min(a_i)v}$ uniformly, and

$$
       h_j=g_{j,1}*\Lambda_{j,2}+f_j*E_j.
 \tag{5}
$$

The error term is $o(1)$ in $L^1$ and supremum norm, even after the factor $O(v)$ for $\|f_j\|_\infty$. In particular $\|h_j\|_1+\|h_j\|_\infty\ll1$ uniformly.

For each fixed $j$, (4) and weak convergence of the tight bounded measures imply

$$
      h_j\longrightarrow h=g_1*g_2\quad\text{in }L^1,\qquad
       \sup_{x\ge b_1+b_2+\epsilon}|h_j(x)|\longrightarrow0 .
 \tag{6}
$$

To justify the first implication precisely, replace $g_{j,1}$ by its strong $L^1$ limit in (5). The map from the shift parameter to translation of $g_1$ is uniformly continuous into $L^1$ on compact shift intervals. Approximate this map by finitely many fixed translations with continuous coefficients on a finite partition of unity, use weak convergence on those coefficients, and bound tails by the total variation outside compact support. This gives convergence of the convolution in $L^1$. For the supremum statement split the measure in (5) at $b_2+\epsilon/2$, using the upper-distance bound for $g_{j,1}$ on the first part and the exponentially small higher-power mass on the second. All limits for fixed $j$ are uniform on the good radical family. The integral of $h$ is $m_1m_2$.

## 3. The actual finite-cutoff overlap term

For physical $x=N-y$, set $T=\log(x/D^2)$, $U=(B-B_0)\log L$, $T_v=T/v$, $U_j=(U-\log j)_+/v$. The two real bracket components from the [exact parity cap](r67-spectral-high-mixed-parity-major.md), with the unmarked masses held fixed, are

$$
 \mathcal U_j=T_v\int_{U_j}^\infty f_j^2
                +\left(\int_0^{U_j}f_j\right)^2,\qquad
 \mathcal V_j=\int_{-T_v}^{T_v} C_{f_j}(s)\,ds-T_v C_{f_j}(T_v),
 \quad C_f(s)=\int f(u)f(u+s)du .
 \tag{7}
$$

With marking, insert $vR_{N,j,t}(vx)/M_j$ in place of $f_j$, and retain the outer weight $P(t)\mu(j)\alpha_j(t)^2M_j^2$. Thus ordinary differentiation uses $g_{j,i},h_j$ in (7) and also the differentiated outer weight. For fixed $j$, $U_j\to U_0>0$ and $T_v\to\tau_0$ uniformly in $x$. By concentration and (4)–(6) we have

$$
 \begin{array}{c|ccc}
 &\text{unmarked limit}&\partial_i\text{ limit}&\partial_{12}\text{ limit}\\ \hline
  \mathcal U_j&1&0&2\tau_0 m_{12}\\
  \mathcal V_j&1&-2m_i&4m_1m_2 .
 \end{array}
 \tag{8}
$$

Here are the cutoff details. For $\mathcal U_j$, the limits of the integrals of $g_{j,i}$ and $h_j$ up to $U_j$ are zero since both bands start strictly above $U_0$, as does their sum support. The terminal terms containing $f_j$ vanish by its absolute concentration and the uniform suprema. The sole surviving mixed derivative in the terminal square is $2T_v\int_{U_j}^\infty g_{j,1}g_{j,2}$; bounded suprema and strong $L^1$ convergence imply strong $L^2$ convergence, so this tends to $2\tau_0 m_{12}$. This term is not a repeated-prime contribution; it comes from the real signed terminal quadratic form.

For $\mathcal V_j$, the mixed derivative of its autocorrelation is the sum of two correlations of $h_j$ with $f_j$ and two of $g_{j,1}$ with $g_{j,2}$. These converge strongly in $L^1$ of the shift by the signed approximate identity and Young's inequality, with limiting terms $h(s),h(-s)$ and the two cross-correlations of $g_1,g_2$. Their total integral is $2m_1m_2+2m_1m_2$. All supports lie within $[-b_1-b_2,b_1+b_2]$, strictly inside the limiting cap. At the single positive shift $T_v$, terms with $f_j$ in the shifted factor vanish by its positive-distance supremum, those with $h_j$ vanish by (6), and those with a shifted $g_{j,i}$ by (4). The support of all real profiles is nonnegative and the unshifted factors have bounded $L^1$ norms. The same argument, replacing $h_j$ by $g_{j,i}$, gives the first derivative and the unmarked entry in (8). No weak limit is evaluated as a point value at a band endpoint.

The signed weights $c_j=P(0)\mu(j)\alpha_j(0)^2M_j^2$ obey $\sum_j c_j=1$ and $\sum_jj^{1/2}|c_j|\ll1$, by the unmarked Euler cancellation. The derivative ratios of $\alpha_j(t)^2$ at $0$ have bounds $O(\log j/v)$ in first order and $O((\log j/v)^2)$ in mixed order, by the local formulas in (2); if the unmarked product is zero it stays zero. At fixed $j$ these ratios tend to zero, and their weighted sums are $o(1)$ using the Euler moment. For $j>e^{U/2}$ use crude $O(1+v)$ bounds for all entries and derivatives of (7) and the moment tail (even after the logarithmic derivative weights). For $j\le e^{U/2}$, $U_j$ and $T_v$ are bounded away from zero. Then $\sup_{x>0}|xf_j(x)|\ll1$ and the uniform $L^1$/supremum bounds of §2 bound every displayed bracket and derivative by $O(1)$; use these to pass through finitely many $j$ and then enlarge that fixed set. This proves that (8) can be summed with the true signed weights.

Finally, prime partial summation and the exponentially small removed marked primes give $P_i(0)/P(0)\to2m_i$, and

$$
       P_{12}(0)/P(0)\longrightarrow4m_1m_2 .
$$

Indeed the mixed log derivative is a sum of $O(p^{-2})$ on the overlap, with no other local term at that order. Thus the mixed derivative of the entire *untwisted* component after its $P(t)$ factor is $4m_1m_2+2\tau_0m_{12}$ in the limit. For the *twisted* component it is
$4m_1m_2+(2m_1)(-2m_2)+(2m_2)(-2m_1)+4m_1m_2=0$.
Taking the true parity half gives precisely (1) on the common auxiliary majors, with the original $\Sigma(N)$. All normalized limits are uniform for $x=N-y$ on the hard physical region.

## 4. The genuine full and original major integrals

The mark $W_{12}$ is fixed throughout the dyad and $O(\ell^2)$ on the whole coefficient support. Divide by this bound and use the fixed-common-multiplier maximal hard-cut Bessel bound on the auxiliary complement from the [whole mixed theorem](r80-spectral-whole-mixed-parity-density.md). It keeps the original squarefree divisor-moment energy, and increasing the fixed log cap absorbs this fixed log loss. Fourier inversion therefore gives the full formula (1) outside the stated common inverse-log family. The exact [original moving minor](r79-spectral-original-minor-power-exception.md) also permits this fixed multiplier and either fixed true parity after the same normalization. Its power exception and error absorb the log loss, so the true full minus that genuine minor gives the identical formula on the original polynomial majors. No historical Dirichlet-GRH input is used for this theorem.
