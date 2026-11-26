# A fixed primorial suffices for the full-strength pointwise exceptional parity difference

This removes the growing planting threshold from the [full-strength pointwise aligned bound](r99-spectral-pointwise-aligned-parity-difference-logarithmic-primorial.md). It does not change the genuine exceptional conductor alignment, the closeness of its actual zero, or the original finite-denominator margin. It concerns individual targets, not the distinct complete-family signed mean.

Use the parameters, true cuts and test of that theorem. In particular $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, and the even target is $N\in[Y,2Y]$. The genuine primitive real Page character $\chi$ has conductor $r\mid N$ with a simple zero $\beta$ satisfying $(1-\beta)G\le C_*\log G$, for fixed $C_*>0$. Keep $\log(Q_0/r)\ge(\log G)^3$. The nonnegative real bounded-BV weight $\omega$ is on a half-open physical interval $I\subset(N/2,9N/16]$ and satisfies $\int_I\omega\ge c_{\rm test}Y$. Fix the original admissible $B>B_0>0$, set $D=\sqrt N(\log N)^{-B}$, and put $U=(B-B_0)\log\log N$, $T_x=\log(x/D^2)$ for $N-x\in I$. Thus $T_x,U\asymp\log G$.

**Theorem.** There is a sufficiently large fixed $z_*>0$ such that it suffices to have $K_z=\prod_{p\le z}p\mid N$ for any $z_*\le z\le Z$, including the single fixed choice $z=z_*$. Then for all sufficiently large qualifying targets,

$$
 -\chi(-1)\bigl(\mathfrak E_+(N;I,\omega)-\mathfrak E_-(N;I,\omega)\bigr)
 \gg \frac{Y^{2\beta-1}}{G}\,\frac{\Sigma(N)}{(\log r)^4}.
 \tag{1}
$$

Here $\mathfrak E_\pm$ are the original genuine exceptional terms and $\Sigma(N)$ is the true pointwise binary singular factor. The constants and $z_*$ can depend on the fixed parameters. No assertion is made that a qualifying zero exists or that either full parity, the uncorrected mixed sum, or Hypothesis S is controlled. No auxiliary alignment $r\mid K_z$ is needed.

## 1. A summable local envelope for the reciprocal primitive

It suffices to handle $z\le\log G$: otherwise the R99 lower threshold already holds when $Y$ is large. Put $\ell=\log z$, so $\log z_*\le\ell\le\log\log G$ in the remaining range. In particular $U/\ell\gg \log G/\log\log G$. Take $U_*=C\log G$ with fixed large $C$ to include all $U$ and $\ell$. Below, primes above $e^{U_*}$ cannot affect any of the finite primitives at arguments in $[0,U_*]$.

Use the all-minus baseline of R99, namely $b_p=p^{-\beta}/(a_p+2p^{-\beta})$ for $p>z$, with $a_p=(p-2)/(p-1)$. The signed ratio $\nu_-$ has local factors $(1-b_p X)/(1-X/p)$ for $z<p\le e^{U_*}$, where $X^k$ denotes shift $k\log p$. Let $\lambda_z$ be the ordinary positive reciprocal measure on $z$-smooth integers from R99. In addition to its mass $O(\ell)$ we have the tilted bound

$$
      \int e^{v/\ell}\,d\lambda_z(v)
            =\prod_{p\le z}(1-p^{-1+1/\ell})^{-1}\ll\ell .
 \tag{2}
$$

Indeed, comparing the two logarithmic Euler masses costs $O(\sum_{p\le z}(p^{1/\ell}-1)/p)=O(1)$, by $p^{1/\ell}\le e$ and the elementary prime log-harmonic bound. The denominators are bounded away from zero for large enough $\log z_*$.

Write $b=1-\beta$ and $\delta=1/\ell$. At a prime the nonconstant tilted absolute mass of its ratio is at most $p^\delta|b_p-1/p|/(1-p^{-1+\delta})$. The denominator is uniformly bounded below. By $|b_p-p^{-\beta}|\ll p^{-2\beta}+p^{-1-\beta}$, and the elementary prime log-harmonic bound for the change from $p^{-\beta}$ to $1/p$, the sum of these tilted local errors is

$$
 \ll z^{1-2\beta+\delta}+ b U_* e^{(b+\delta)U_*}.
 \tag{3}
$$

For example the exponent in the latter term follows on using $p^\delta(p^{1-\beta}-1)\le b e^{(b+\delta)U_*}\log p$. With $\log z_*\ge 2C$ this second term tends to zero uniformly; the first can be made uniformly small by making $z_*$ larger. In particular $\int e^{v/\ell}\,d|\nu_-|(v)\ll1$ by multiplying the local mass bounds, and $\|\nu_--\delta_0\|_{\rm TV}$ can be made as small as any prescribed constant. The latter does not have to tend to zero with $Y$ when $z$ is fixed.

The ordinary reciprocal Möbius primitive $m(v)=\sum_{n\le e^v}\mu(n)/n$, zero below zero, satisfies $|m(v)|\ll F(v)$ where $F(v)=\mathbf1_{v\ge0}(1+v)^{-2}$, by R99 Section 1. The all-minus primitive $R_-$ is $m*\lambda_z*\nu_-$ on $[0,U_*]$ by the same coefficient identity. Hence an absolute envelope there is a constant times $H=F*\lambda_z*|\nu_-|$. The positive measure $\lambda_z*|\nu_-|$ in this convolution has total mass and tilted mass $O(\ell)$. For any real shift the sum of the translated $F$ suprema on consecutive unit intervals is bounded by an absolute constant. Integrating that observation against the positive measure gives

$$
        \sum_{n\ge0}\sup_{n\le v\le n+1}H(v)\ll\ell .
 \tag{4}
$$

For $v>0$, split the shift variable at $v/2$. The small shifts cost $O(\ell/(1+v)^2)$ and the rest cost $O(\ell e^{-v/(2\ell)})$ by (2)–(3). In particular uniformly for $v\ge U/4$ the envelope is $O(\ell/U)$ in the present range, in fact $O(\ell/U^2+\ell e^{-U/(8\ell)})$. These are real pointwise bounds, even at the jumps.

The ordinary reciprocal rough integrated primitive in R99 is nonnegative, bounded by $O(\ell)$, and bounded below by $c\ell$ for $\ell\le v\le U_*$ with an absolute $c>0$ once $z_*$ is large. Those bounds follow there by keeping the harmonic labels $a\le\sqrt z$ in the positive convolution of the ordinary integrated primitive. The small fixed unweighted variation of $\nu_--\delta_0$ preserves the lower bound and the $O(\ell)$ upper for its perturbed integrated primitive $A_-$ on that interval. On $0\le v\le\ell$ nothing has entered the rough Euler factors, so $A_-(v)=v$. In particular $A_-\ge0$ throughout $[0,U_*]$.

## 2. A local interval estimate for the positive reciprocal shifts

Use the genuine pointwise $\alpha_p$ of the [completed aligned formula](r93-spectral-completed-colored-caps.md), equal to zero at all prime divisors of $N$. On our finite range $R_1=R_-*\nu_+$ and $A=A_-*\nu_+$ are the actual primitive and its integral, with $\nu_+$ from local ratios $(1+\alpha_pX)/(1-b_pX)$ for $z<p\le e^{U_*}$. This measure is positive since $\alpha_p\ge-b_p$, and each factor has atom one at zero. Put $D_+(v)=\nu_+([0,v])$. In particular a true extra prime $p\mid N$, $p>z$, has the positive geometric ratio $(1-b_pX)^{-1}$.

Log-coordinate marking gives the exact measure identity
$s\,d\nu_+(s)=d(\nu_+*\Lambda_+)(s)$, where the coefficient of $\Lambda_+$ at $k\log p$ is

$$
          \bigl((-1)^{k-1}\alpha_p^k+b_p^k\bigr)\log p
                              \qquad (k\ge1).
 \tag{5}
$$

Indeed differentiating a local factor with the operator $(\log p)X\partial_X$ gives the product of that factor and the power series (5); multiplying the finite prime factors proves the coefficient identity. No division by a Fourier value or by a sum with the moving cutoff is needed. For $k=1$ the total variation of the resulting measure on any unit log interval is $O(1)$: $|\alpha_p|+b_p\ll p^{-\beta}\ll p^{-1}$ in the finite prime set, and Chebyshev gives $\sum_{\log p\in[a,a+1]}\log p/p\ll1$ uniformly. The entire contribution of $k\ge2$ even without restricting to a unit interval is $O(\sum_{p>z}(\log p)p^{-2\beta})=O(1)$ by the geometric tails and $\beta\ge .99$. Thus the total variation of $\Lambda_+$ restricted to any interval of length at most one is $O(1)$.

If $J\subset[v,U]$ has length at most one and $v>0$, use positivity on the left of (5), and use that all $\Lambda_+$ shifts are positive on the right. Integrating (5) over $J$ then gives

$$
                       \nu_+(J)\ll D_+(U)/v .
 \tag{6}
$$

The fixed interval can have either endpoint convention. This is a local bound in the genuine discrete positive shift distribution, not just a first-moment estimate.

For $w\in[U/2,U]$ evaluate $R_1(w)$ at its actual weak endpoint. In the convolution, shifts $s\le w/2$ leave $w-s\ge U/4$; the far envelope after (4) gives $O(\ell D_+(U)/U)$. For shifts $s>w/2$, partition according to consecutive unit intervals of $w-s$ with nonnegative arguments. Each shifted interval lies in $[U/4,U]$ and has mass $O(D_+(U)/U)$ by (6), and the sum of the envelope suprema is $O(\ell)$ by (4). Thus

$$
       \sup_{U/2\le w\le U}|R_1(w)|\ll \frac{\ell}{U}D_+(U).
 \tag{7}
$$

The global sup bound on $[0,U]$ remains $O(D_+(U))$, by the ordinary reciprocal rough supremum and the unweighted ratio. The genuine positive convolution also gives $\sup_{0\le u\le U}|A(u)|\ll\ell D_+(U)$ and $A(U)\gg\ell D_+(U)$. To see the lower, use the actual positive mass in shifts at most $U/2$, where $A_-(U-s)\gg\ell$. That mass is $\gg D_+(U)$ by the R99 Markov comparison: keep the factors $p\le e^{U/M_0}$ for one sufficiently large fixed $M_0$, so their normalized mean log shift is $O(U/M_0)$, and the remaining product up to $e^U$ enlarges mass by at most $O_{M_0}(1)$. Here $U/2\ge\ell$ eventually, and nonnegative $A_-$ allows all other terms to be omitted. The argument is valid unchanged for fixed $z$.

## 3. Use the local bound at the true shifted cap

Let $M=\mathcal N_\chi>0$ be the exact pointwise prefactor, and let $\kappa_j$ be the inverse-removal shift measure for each squarefree $j$ with nonzero $\alpha(j)$, with factors $(1+\alpha_pX)^{-1}$ for $p\mid j$. Its absolute mass is at most $V_j=\prod_{p\mid j}(1-|\alpha_p|)^{-1}$. Put $E(U)=\int_U^\infty R_1^2$. The signed square-label formula in [R97 (6)](r97-spectral-pointwise-aligned-parity-difference-all-fixed-cuts.md) includes the actual shifted cutoff $U-\log j$. Its $j=1$ tail equals $E(U)$ on division by $M$. For $j>1$, applying Cauchy–Schwarz in the inverse measure bounds the tail norm by

$$
 V_j^2 E(U)+V_j\int\left(\int_{\max(0,U-\log j-s)}^U
                     R_1(v)^2\,dv\right)d|\kappa_j|(s).
 \tag{8}
$$

This includes $j>e^U$ literally, since the whole norm has been taken there. All functions are zero below zero. The signed contribution is bounded below by subtracting (8) with the absolute weight $|\alpha(j)|^2$.

When the displacement $s+\log j$ is at most $U/2$, the inner integral in (8) is at most its length times the square of (7). Aggregate its length by the log moment from R99 (4), namely
$\sum_{j>1}|\alpha(j)|^2 V_j\int (s+\log j)d|\kappa_j|(s)\ll z^{1-2\beta}$. It follows by the local geometric moments and the elementary prime bound without an extra log factor. For large displacements the integral is at most $O(U D_+(U)^2)$. An exponential moment at $\eta=1/4$ gives the necessary tail bound:

$$
 \sum_j|\alpha(j)|^2 V_j\int e^{\eta(s+\log j)}d|\kappa_j|(s)
 \le \prod_{p>z}
   \left(1+\frac{|\alpha_p|^2p^\eta}
     {(1-|\alpha_p|)(1-|\alpha_p|p^\eta)}\right)\ll1 .
 \tag{9}
$$

This product converges uniformly by $|\alpha_p|\ll p^{-\beta}$ on the full half-line, $\beta\ge.99$, and sufficiently large fixed $z_*$. Let $\Delta_0=\sum_{j>1}|\alpha(j)|^2V_j^2\ll z^{1-2\beta}$. Combining (8)–(9) with the true square-label signs gives

$$
 \frac{C_\chi(0)-Q_\chi(U)}{M}\ge
 (1-\Delta_0)E(U)
 -O\!\left(D_+(U)^2
       \{z^{1-2\beta}(\ell/U)^2+U e^{-\eta U/2}\}\right).
 \tag{10}
$$

The inherited global $L^2$ is only used for this exact identity and nonnegative $E(U)$; no uniform upper bound on that late norm is needed.

For the other cap, use the genuine shifted integrals $(A*\kappa_j)(U-\log j)$ for $j\le e^U$. The total of the absolute $j>1$ contribution to $J_\chi(U)/M$ is at most $\Delta_0\sup_{0\le u\le U}|A(u)|^2$. Thus $J_\chi(U)/M\gg\ell^2 D_+(U)^2$ by Section 2 and a sufficiently large fixed $z_*$. The same choice ensures $1-\Delta_0>0$. Multiplying the loss in (10) by $T_x\asymp U$ gives $o(\ell^2D_+(U)^2)$ uniformly even at fixed $z$. That is the improvement over using the entire initial shelf in the tail comparison. The actual second-color scalar therefore satisfies

$$
 B_1(x)=T_x\{C_\chi(0)-Q_\chi(U)\}+J_\chi(U)
                            \gg M\ell^2D_+(U)^2 .
 \tag{11}
$$

## 4. Recover the pointwise factor without any growing cutoff

Use the exact pointwise normalization R99 (6), or R97 (9). At fixed $z$ its exterior paired product for $p\nmid N$ need no longer tend to one, but its absolute logarithmic sum is $O(\sum_{p>z}(p^{-1-\beta}+p^{-2\beta}))=O(1)$, so it stays bounded below. The $p\mid N,\ p\nmid r$ factors have lower bound $\exp(-2\sum_{p\mid N,\,p\nmid r}p^{-\beta})$. Below $z$ this costs at most a constant times $\ell^2$ in the reciprocal. Retain in $\nu_+$ just the actual geometric factors at $z<p\le e^{U/M_0}$ dividing $N$ but not $r$. Their Euler mass is $\gg\exp(\sum p^{-\beta})$ over precisely these primes and at least half of it lies below $U/2$ by the same normalized mean estimate; unit atoms of the other factors give that lower bound for $D_+(U)$. Primes of $N$ above $e^{U/M_0}\ge G^c$ contribute a bounded reciprocal sum, by splitting at $G$ just as in R99. All bounds are uniform when $z$ is fixed and depend on no growing number of its small factors. The same near-exception derivative bound $|L'(\beta,\chi)|\ll (\log r)^2$ thus gives $M\ell^2D_+(U)^2\gg\Sigma(N)/(\log r)^4$.

Finally use the original physical formula R97 (11): subtraction of the two actual exceptional parities and multiplication by $-\chi(-1)$ leaves the positive weighted integral of (11) times $(N-x)^{\beta-1}x^{\beta-1}/\log x$, plus $O_A(Y^\beta G^{-A})$ under the unchanged finite-denominator margin. The actual weight and intervals give its lower scale $Y^{2\beta-1}/G$ times the factor in (1). The error is absorbed by $A>C_*+4$ as before. This proves the original pointwise exceptional difference for a single sufficiently large fixed primorial, without asserting the existence of the designated zero.
