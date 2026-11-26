# The two even-conductor channels of the genuine mixed strip

**Scope.** For the genuine above-BV mixed coefficient, the regular completed bracket cancels in two fixed 2-adic signed means to arbitrary inverse-log accuracy. The same channels of the actual full correlation and the original moving-major integral therefore isolate the exceptional correction, without discarding any targets on the sampling progression. Under the hypothetical supported even Page-zero conditions stated below, a quantitative signed lower bound transfers to these **genuine modulated mixed-strip means**. This is not a pointwise result, an unweighted sign or positivity assertion, the full signed shell beyond this mixed coefficient, a prime-pair result, or Weak S. No Page-zero existence, Dirichlet GRH, or external zero-gap assertion is used.

Use the common real scaled tests and genuine sums of [the complete signed mean](r95-spectral-complete-planting-signed-mean.md), with $G=\log Y$, $Z=\sqrt G/\log G$, $Y\le N\le2Y$ even, $J\subset(1/2,9/16]$ real half-open, $I_N=NJ$, $\omega_N(u)=w(u/N)$, and fixed admissible $B>B_0>0$. The left weight $w$ on $J$ and target weight $\eta$ on $[1,2]$ are bounded and of bounded variation, uniformly and common across each dyad. The symbols $S_\pm$ and $S_\pm^{\rm maj}$ are respectively the original full correlation and its actual moving polynomial-major integral, for the genuine mixed-strip right-hand sectors of even and odd squarefree factor count. In particular the integral in $S_\pm^{\rm maj}$ is on the original denominators at most $N^{1/1000}$ and radius $2N^{1/1000}/N$; it is not the common auxiliary major integral. Write $\mathcal B_\pm$ for the exact regular bracket of the [whole mixed parity calculation](r80-spectral-whole-mixed-parity-density.md), equation (2), as used before removing the correction in the [all-scale decomposition](r89-spectral-exceptional-conductor-folded-sampling.md). Write $\mathfrak E_\pm$ for that decomposition's actual exceptional correction, zero if no Page zero exists.

For an even integer $K$ fixed on the dyad put

$$
 \langle F\rangle_K
   =\frac K Y\sum_{\substack{Y\le N\le2Y\\K\mid N}}\eta(N/Y)F(N),
 \qquad f_2(N)=(-1)^{N/2},\qquad f_3(N)=\cos(\pi N/4).
 \tag{1}
$$

**Theorem.** If $v_2(K)=1$, then for $j=2,3$ the regular means satisfy
$\langle f_j\mathcal B_\pm\rangle_K=O(KG^C)$ with a fixed $C$, uniformly in the declared tests. If additionally $K\le e^{2Z}$, then the actual sums satisfy, for every fixed $A>0$,

$$
 \begin{split}
 \langle f_j S_\pm\rangle_K
   &=\langle f_j\mathfrak E_\pm\rangle_K+O_A(YG^{-A}),\\
 \langle f_j S_\pm^{\rm maj}\rangle_K
   &=\langle f_j\mathfrak E_\pm\rangle_K+O_A(YG^{-A}).
 \end{split} \tag{2}
$$

No zero or closeness hypothesis is needed for either comparison in (2).

For the quantitative signed conclusion take the full primorial $K=K_z=\prod_{p\le z}p$, with $2\le z\le Z$, $4K_z\le e^{2Z}$, and fixed nonnegative $w,\eta$ of positive integrals. Suppose the actual primitive real Page character $\chi$ has conductor $r=2^e r_{\rm odd}$ with $e=2$ or $3$ and $r_{\rm odd}\mid K_z$, and its simple zero satisfies $(1-\beta)G\le C_*\log G$ for fixed $C_*$. Put $s_2=1,\ s_3=1/2$. Then for either of the two actual choices $X_\pm=S_\pm$ or $X_\pm=S_\pm^{\rm maj}$,

$$
 -\chi(-1)\left\langle f_e(X_+-X_-)\right\rangle_{K_z}
  \ \gg\
  s_e\left(\int_Jw\right)\left(\int_1^2\eta\right)
      \frac{Y^{2\beta-1}}G\frac{K_z}{\varphi(K_z)(\log r)^4}.
 \tag{3}
$$

These are hypotheses only for the lower bound; its large-scale comparison is ineffective as in the signed exceptional result. The other even channel has both true means $O_A(YG^{-A})$. If there is no Page zero, or if the Page conductor is odd or has unsupported odd part, both channels of both actual sums on this primorial are $O_A(YG^{-A})$ for every fixed $A$. There is no extra lower bound on $z$.

## 1. A uniform time-variation bound for the fixed kernels

Write $R(u)=\sum_{n\le e^u}\mu(n)/n$ for $u\ge0$ and zero for $u<0$. Use the same ordinary unconditional bound $R(u)\ll e^{-c\sqrt u}$ of R80 Section 2. Its total variation on any closed interval of log length at most $2$ is bounded by an absolute constant, since the jumps are bounded in absolute value by $1/n$ and the reciprocal sum between real endpoints of ratio at most $e^2$ is bounded, including the possible jump at zero. In particular $R\in L^1\cap L^2\cap L^\infty$, and $\sum_{k\ge0}\sup_{u\in[k,k+1]}|R(u)|<\infty$.

Its real autocorrelation $C_R(t)=\int_{\mathbb R}R(u)R(u+t)\,du$ is globally Lipschitz. To prove the Lipschitz claim with a constant independent of the translate $t$, take $0<a\le1$, split $u\ge0$ into $[k,k+1)$, and bound the difference in the second factor by the absolute jump measure $|dR|$ on $[u+t,u+t+a]$. After interchanging that positive measure and the integral in $u$, each jump costs length at most $a$ within its block, and all relevant jumps are in $[k+t,k+t+2]$. Thus

$$
  |C_R(t+a)-C_R(t)|
       \le a\sum_{k\ge0}\sup_{u\in[k,k+1]}|R(u)|\,
                                  |dR|([k+t,k+t+2])
       \ll a.
 \tag{4}
$$

This also treats endpoint jumps, and longer or negative increments follow by splitting or reversal.

If $F_i=R*\lambda_i$ for finite log-shift measures $\lambda_i$ on $[0,\infty)$, their sup, $L^1$ and $L^2$ norms are bounded by corresponding fixed norms of $R$ times $\|\lambda_i\|_{\rm TV}$. Their cross-correlation is the double shifted average of $C_R$, by Fubini and the $L^2$ bounds. Its sup and global Lipschitz constant are therefore $O(\|\lambda_1\|_{\rm TV}\|\lambda_2\|_{\rm TV})$; no bound on the sizes of the shifts is needed.

## 2. Expand the actual regular bracket only in odd occupancies

Use the notation with $\alpha_p^\circ=(p-1)/(p^2-2)$ for odd primes, zero for $2$, and $\alpha_N(p)=\alpha_p^\circ\mathbf1_{p\nmid N}$. The two primitives and all kernels below are those of R80 (2) and the definitions in [the parity computation](r67-spectral-high-mixed-parity-major.md). They are used here only for the exact regular bracket, not for any historical Dirichlet GRH assumption in the pointwise original-major calculation. In particular the primitive $R_{N,j}$ has the weights $\mu(n)\alpha_N(n)$ with $(n,j)=1$; for even $N$ every even label has zero weight. Define the positive fixed base shift measure $\nu_0$ by the local ratios $(1-\alpha_p^\circ X)/(1-X/p)$, with $X$ denoting shift $\log p$. At odd $p$ the nonconstant coefficient sum is $(1/p-\alpha_p^\circ)/(1-1/p)=O(p^{-2})$, nonnegative; at $2$ the ratio is the ordinary geometric inverse. Thus the product converges in total variation to a finite positive measure on nonnegative shifts. For odd $p$ put
$\rho_p=\sum_{k\ge1}(\alpha_p^\circ)^k\delta_{k\log p}$ and $b_p=\|\rho_p\|_{\rm TV}\ll1/p$, and take the multiplicative convolution product $\rho_d$ over the primes of an odd squarefree $d$ with norm $b_d$. The $d=1$ conventions are $\delta_0$ and one.

For odd squarefree $j$ define
$\nu_j=\nu_0*\prod_{p\mid j}(\delta_0+\rho_p)$ and $V_j=\prod_{p\mid j}(1-\alpha_p^\circ)^{-1}$. This measure has mass $\|\nu_0\|_{\rm TV}V_j$. Comparing exact Euler coefficients in the primitive, and then expanding the removals at primes of $N$ not in $j$, gives

$$
 R_{N,j}
   =\sum_{\substack{d\mid\operatorname{rad}_{\rm odd}(N)\\(d,j)=1}}
                       R*\nu_j*\rho_d ,
 \tag{5}
$$

where $\operatorname{rad}_{\rm odd}(N)$ is the product of the odd primes of $N$. Formula (5) does not remove a common prime of $N,j$ twice. It holds even if $(N,j)>1$. The scalar weight outside the associated quadratic terms is
$\mu(j)\alpha^\circ(j)^2\mathbf1_{(N,j)=1}$, where $\alpha^\circ(j)=\prod_{p\mid j}\alpha_p^\circ$; expand its indicator by $\sum_{d_0\mid j}\mu(d_0)\mathbf1_{d_0\mid N}$.

The prefactor $\Sigma(N)P_N$ has a similar elementary expansion. By the local formulas of [the squarefree CRT bracket](r63-spectral-full-squarefree-crt-strip.md), at each odd $p$ the ratio between its factor when $p\mid N$ and its factor when $p\nmid N$ is a positive real number $1+O(1/p)$: the ratio in $\Sigma(N)$ is $(p-1)/(p-2)$ and the ratio in $P_N$ is
$(1+2(p-1)/(p(p-2)))^{-1}$. The prime $2$ is fixed for all even $N$. The product of the factors for the initially unoccupied **odd** primes converges absolutely to a positive constant. Therefore $\Sigma(N)P_N=C_0\sum_{k\mid\operatorname{rad}_{\rm odd}(N)}\delta(k)$ with $|\delta(k)|\le \prod_{p\mid k}C_1/p$ for a fixed $C_1$. This uses only one occupancy bit per prime, not the valuation of $N$.

Insert (5) in both primitive slots of each part of the bracket. For fixed $j,k,d_0,d_1,d_2$ the only remaining arithmetic condition at the target is $d\mid N$, with $d=[k,d_0,d_1,d_2]$ **odd** and squarefree; the conditions $(d_1d_2,j)=1$ remain fixed on the labels. The two possible pairs of geometric expressions for the resulting fixed functions
$F_i=R*\nu_j*\rho_{d_i}$ are linear combinations of

$$
  \begin{split}
  &T\int_a^\infty F_1(u)F_2(u)\,du+
                \left(\int_0^a F_1(u)\,du\right)
                \left(\int_0^a F_2(u)\,du\right),\\
  &\int_{-T}^T C_{F_1,F_2}(t)\,dt - T C_{F_1,F_2}(T),\\
  &\hspace{20mm} a=(U-\log j)_+,\qquad
        C_{F_1,F_2}(t)=\int_{\mathbb R} F_1(u)F_2(u+t)\,du .
  \end{split} \tag{6}
$$

The first is the bilinear expression for $T(Q_N-Q_{N,U})+J_{N,U}$: if $j>e^U$, then $a=0$ and both finite terms vanish exactly. The second is the cross-correlation expression for the other color. An individual cross-correlation need not be even; the exact expansion is in ordered pairs and keeps $T C_{F_1,F_2}(T)$ as written. Thus no replacement of a moving finite cap by a limiting one has been made.

In the physical integral use $u=vs$ and $x=v(1-s)$ for real $v\in[Y,2Y]$ and fixed $s\in J$. The actual widths are $T=\log(1-s)+2B\log\log v$ and $U=(B-B_0)\log\log v$, with $T>0$ for large $Y$. They have supremum $O(\log G)$ and variation $O(1/G)$ throughout the dyad, uniformly in $s$. The map $U\mapsto a$ is 1-Lipschitz. The tails $\int_a^\infty F_1F_2$ and the terminal integrals $\int_0^a F_i$ are Lipschitz in $a$ using the sup norms of their integrands, and bounded by the respective full $L^2$ or $L^1$ bounds. The cross-correlation terms obey (4) in their moving argument and are bounded by the corresponding constant. Thus the sup plus variation of (6) as a function of $v$, for fixed $s,j,d_1,d_2$, is at most $G^C V_j^2 b_{d_1}b_{d_2}$. Multiplying by the actual physical factor $v/\log(v(1-s))$, with sup plus variation $O(Y/G)$, and by $\eta(v/Y)$, and integrating the bounded fixed $w(s)$ over $J$, gives sup plus total variation

$$
                   O(YG^C V_j^2 b_{d_1}b_{d_2})
 \tag{7}
$$

for the real profile of each such tuple. In particular this is a bound in the **target variable** $v$, not in its partner variable at a fixed integer target. All literal point values of $\eta$ and the same half-open $J$ remain admissible.

## 3. Sum on the literal progression before taking any limit

At actual targets $N\in[Y,2Y]$, every contributing odd $d\mid N$ is at most $2Y$. We may impose that bound on the expanded labels without an error. It forces $k,d_1,d_2\le 2Y$, whereas $j$ need not be truncated. The scalar sums needed to apply (7) are controlled by

$$
 \sum_{j\ {\rm odd,\ sf}}
       \alpha^\circ(j)^2 V_j^2\tau(j)<\infty,\qquad
 \sum_{\substack{h\le2Y\\ h\ {\rm odd,\ sf}}}
                     (|\delta(h)|+b_h)\ll G^C.
 \tag{8}
$$

The first product has increments $O(p^{-2})$; the second is bounded by products with increments $O(1/p)$ and the usual reciprocal prime bound. The sum over $d_0\mid j$ is included by $\tau(j)$. Absolute convergence justifies the expansion at each $N$ and the finite target averaging, even with the real profiles and signs retained.

For each fixed odd $d$, the conditions $K\mid N$ and $d\mid N$ select the literal multiples of $[K,d]$. Its 2-adic valuation is exactly one. Therefore $f_2$ along that progression has alternating values, and $f_3$ has a four-period with values $1,0,-1,0$ up to a cyclic shift. Both have zero complete-period mean and bounded partial sums on every interval of indices. Discrete partial summation thus bounds the unnormalized sum of the tuple's profile times $f_j$ by an absolute constant times its sup plus total variation in (7), uniformly even when $[K,d]$ exceeds the dyad length. Multiply by $K/Y$ and sum the absolute scalar weights using (8). This gives $O(KG^C)$, as claimed. In particular the proof does not try to pair integers of exactly equal odd radical one by one.

## 4. Transfer the same channels to the genuine correlations

In the deterministic step of the R89 all-scale decomposition the actual common auxiliary major integral at every target equals $\mathcal B_\pm+\mathfrak E_\pm+O_A(YG^{-A})$ before imposing any planting condition. Use the **mean absolute** complement estimates of R95 Section 2 on the full $K$ family: the common auxiliary complement has bound $YG^{O(1)}\sqrt K\,Q_0^{-1/4}$ with $Q_0=e^{16Z}$, and the actual original moving minor has bound $Y^{1-1/40000}+KG^{O(1)}Y^{1-3/10000}$. These estimates bound averages with bounded external factors, so inserting $f_j$ of absolute value at most one costs nothing. They do not assume that the modulated target test itself is slowly varying. For $K\le e^{2Z}$ both bounds and the regular-bracket estimate above are $O_A(YG^{-A})$ for every fixed $A$. Add the common complement for the full sum, and subtract the actual original moving minor for the original major. This proves (2) without identifying the two arc sets or removing any targets.

Now use [the exact exceptional 2-adic channels](r99-spectral-two-adic-exceptional-mean-channels.md) on the complete $K_z$ family. Its fixed $f_2,f_3$ are precisely (1). When $e=2$ or $3$ and $r_{\rm odd}\mid K_z$, the matching exceptional parity difference has sign and size (4) of that result under the stated closeness and nonnegative tests. Its response is $s_e$. Since $Y^{2\beta-1}\ge YG^{-2C_*}$ and $\log r\le16Z$, the available error in (2) is smaller than half that lower bound for a sufficiently large fixed $A$. This gives (3). The other vanishing cases follow from the corresponding exact signed exceptional channel estimates, including zero correction on a dyad without a Page zero. The theorem isolates this signal in actual modulated mixed means, not in a regular-bracket subtraction performed on individual data.
