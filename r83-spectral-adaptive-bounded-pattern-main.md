# The actual mixed-strip main term under every bounded adaptive small-prime pattern

**Scope.** This is a simultaneous density-one law for the actual above-BV mixed cutoff weights, by true squarefree parity. The right multiplier can be an arbitrary bounded, target-dependent function of the actual small-prime part, not just an exclusion. The leading term samples that function at the empty pattern; every multiplier vanishing there contributes no leading term. This is not a pointwise theorem, a prime-counting interpretation, or weak S.

Use the actual $M_\pm$, physical right gate, real hard left intervals $I$, bounded-BV left weights $\omega$, and original moving polynomial arcs of the [whole mixed parity theorem](r80-spectral-whole-mixed-parity-density.md). In particular $M_>$, before its external subtraction, has the four-factor weight $\mu(b)\mu(c)(1-2\log(ac)/\log m)$ on pairwise coprime squarefree $abcd=m$, the genuine cutoff $abc>H_0$, and $D<\min(ab,ac)<\sqrt m$. Write $M_\pm=(1\pm\mu(m))M_>/2$ on squarefree partners, with $+$ denoting even factor count. For $Y\le N\le2Y$, set $L=\log N$, $\ell=\log Y$, $v=\log\log Y$, and $z=v^2(1+\log(2v))^2$. Define the true pattern $s(m)=\prod_{p\mid m,\ p\le z}p$. Allow an arbitrary function $F_N$ on the squarefree divisors of $\prod_{p\le z}p$, with $|F_N|\le1$, independently at each target. In particular an arbitrary smaller adaptive alphabet or an arbitrary exact subset of small-prime patterns is permitted.

For each fixed $A>0$ there is one exceptional family of $O_A(Y\ell^{-A})$ even $N$ outside which, simultaneously over every such $F_N,I,\omega$, the actual full correlation with $F_N(s(m))M_+(m)$ equals

$$
 F_N(1)\Sigma(N)\int_I\frac{\omega(u)}{\log(N-u)}\,du
 +O_A\left(\frac{\Sigma(N)|I|}{L}e^{-c\sqrt v}+Y\ell^{-A}\right),
 \tag{1}
$$

while the odd correlation has just the stated error. The same statements hold for the actual original major integrals. Here $c>0$ is fixed, depending on the fixed cutoff parameters. For example, one may require the presence of **any** designated small prime, select a nonempty exact pattern or a nonempty collection of patterns, or put independent signed weights on all nonempty patterns, with the same error. This is stronger than separately estimating every avoidance event: separately summing their errors would cost exponentially many terms.

## 1. Track the exact pattern in the auxiliary major

Let $\mathcal P=\{p:5\le p\le z,\ p\ {\rm prime}\}$ and let $R=\prod_{p\in\mathcal P}p$. Use the complex Banach algebra $\mathscr B$ of absolutely summable coefficient arrays in the finitely many variables $X_p$ for $p\in\mathcal P$, with ordinary power series multiplication and norm the sum of the absolute values of the coefficients. This is ordinary multiplication, not reduction modulo any idempotent relation. Monomials have norm one and multiplication is submultiplicative. Let $X(s)=\prod_{p\mid s}X_p$ for $s\mid R$. A polynomial $\sum_{s\mid R}c_s X(s)$ encodes the actual disjoint coefficients at the exact patterns. Bounding its error in $\mathscr B$ bounds all linear combinations with weights of magnitude at most one at once. Operations on the analytic approximants may involve higher powers temporarily; the actual polynomial and the completed arithmetic densities before division are multilinear because the four factors are pairwise coprime.

At first fix $r_0\mid6$ and retain the extra exact gate $(m,r_0)=1$. Put the marker $X((m,R))$ in the right sum. For $p=2,3$ we use only those four exclusion cases, and recover exact occupancy of the two small primes at the end by a finite difference. This avoids the need to invert a formal series with large first coefficient at 3.

Use the fixed auxiliary arcs $q\le Q_0=\ell^K$, $|\beta|\le2Q_0/Y$, with $K$ chosen for the desired log budget. The exact signed identity $M_>+M_\le=-\Xi_D$ remains true after multiplication by the marker and the gate, and also after the total Möbius twist. Use the same large signed sectors and two-positive-variable bulks as in the [adaptive exclusion proof](r82-spectral-adaptive-small-prime-exclusion-main.md) and the [parity formula](r67-spectral-high-mixed-parity-major.md). We check the norm estimates needed to rerun that argument, rather than sum pointwise scalar error bounds over all patterns.

* In a large signed sector, freeze the other three factors of product $h$ and split the true marked part of the signed variable into $s\mid R$. Write that variable $s d$, imposing $(d,hRr_0)=1$ and the exact compatibility $(s,hr_0)=1$. Its sign becomes $\mu(s)\mu(d)$, because $(d,s)=1$. A residue class of $s d\bmod q$ is either impossible or one class for $d\bmod q/(s,q)$, and the upper length scale is $Y/(hs)$. All the original gates in the signed variable are the same hard intervals, simply divided by $s$. On every nonempty sector the scale of $d$ is polynomial, since $s\le R=\exp(O(z))=Y^{o(1)}$ and the signed variable was polynomial. The uniform unconditional masked Möbius estimate of §1 of the [squarefree CRT theorem](r63-spectral-full-squarefree-crt-strip.md) therefore gives an error $O_C(Y/(hs)\ell^{-C})$ for each fixed residue, with the usual bounded/monotone weight and $O(1+Q_0)$ phase variation. Its coprime-mask proof permits $hRr_0\le Y^{O(1)}$: the smoothing convolution has reciprocal mass $O(\log\log Y)$ and its quarter-power moment is $O_\epsilon((hRr_0)^\epsilon)$. The sum of these errors in $\mathscr B$ costs only $\sum_{s\mid R}1/s=\prod_{p\in\mathcal P}(1+1/p)\ll(1+\log(2z))^{O(1)}$, not the number of patterns. Triple reciprocal sums and the $q$ residue classes cost fixed log powers. This also handles the twisted low $M_\le$ where the signed $d$ is at polynomial scale; the argument uses the actual hard $d$ intervals.
* Where both counted variables are positive, the usual squarefree count followed by the harmonic average applies coefficientwise with a power-saving error. In detail, for fixed signed labels, enumerate fixed disjoint marked parts $s_1,s_2\mid R$ of the two positive variables, compatible with those labels, and replace each variable by $s_i$ times a variable prime to $Rr_0$. These remaining variables still lie at polynomial scales, as the original positive variables in the untwisted and twisted strip bulks exceed $N^{.39}$, and both in the untwisted low mixed term exceed $N^{.49}$. The first squarefree progression uses a linear congruence reduced by $(q,s_i)$ if necessary; its floor error is $O(\tau(w)\sqrt X)$ for scale $X$, with the remaining coprime mask $w\le Y^{O(1)}$. In the harmonic average of the second variable, primes of $R$ are now omitted in that variable and the statuses of the fixed factors at those primes are constants. The proof by convolution with $1$ in §2 of the squarefree CRT theorem is unchanged: at excluded primes the harmonic convolution has only $k(p)=-1$, at primes of $q$ any nontrivial factors cost $q^{O(1)}$, and elsewhere the same $3/4$ moment is bounded by $O_\epsilon(q^{O(1)}w^\epsilon)$. Equivalently at a prime of $R$ keep its locally forced factors outside the harmonic average from the outset. The fixed scaled-variable coefficients and conversion factors have at most $Y^{o(1)}$ extra cost from $R$; factors of fixed unmarked coprime labels have the same bounds as in the cited proof. A power saving thus absorbs the at most $3^{|\mathcal P|}=Y^{o(1)}$ allocations in the norm of this error. No such counting factor was used on the signed Siegel--Walfisz errors. The real integrals retain the original interval endpoints in the unscaled variables.

At $p\in\mathcal P$, taking the sum of the actual local cases multiplies a right-occupied term by $X_p$ once. For example, when the two signed labels omit $p$, the two-positive-variable local factors at uncompleted $q$ are $(1-1/p)^2(1+2X_p/p)$ off $q$ and $(1-1/p)^2(-1/(p-1)+2X_p/p)$ on $q$. If one signed label contains $p$, the two positive variables are units and the monomial from that label marks the occupied prime. A right-occupied term has rational residue zero at that prime; when right-unoccupied, the product of the two units has uniform nonzero residue. These facts give the exact local polynomials on the genuine coefficients. At $p\mid r_0$ all occupied cases disappear. On other primes all cases are unchanged.

For each squarefree $q$ the resulting right profile has supremum and variation, in $\mathscr B$ norm, at most $O(\ell^C C_1^{\omega(q)}/q)$, including after extension by zero. Indeed off $q$ the norm of an unoccupied-signed-label local polynomial is at most $(1-1/p)^2(1+2/p)$ with product bounded; on $q$ its norm is $O(1/p)$. If a signed label instead occupies $p\mid q$, the reciprocal sum over that label supplies the same $1/p$, as in the original occupancy proof. These bounds also hold for the low mixed profile, with the same finite Archimedean caps and variation, and for the analogous twisted high profile. Left prime Siegel--Walfisz is unchanged, including elimination of nonsquarefree $q$ in the left main term; the exact right polynomial has norm at most its signed tuple absolute envelope $O(Y\ell^3)$. The two BV bounds give the same slow Fourier completion. For the rational tail the bound on $\mathscr B$ variation applies also to formal $q>Q_0$; average $|c_q(N)|\le 2\tau(q)$ over $[Y,2Y]$ as in the whole mixed theorem. Its normalized mean norm is $O(\ell^C Q_0^{-1/2})$. Thus outside $O_A(Y\ell^{-A})$ targets the actual auxiliary major is the real integral of the full completed $\mathscr B$ densities up to $O_A(Y\ell^{-A})$ in norm, uniformly in $I,\omega$ and the four fixed $r_0$.

## 2. Complete the signed primitive in coefficient norm

Use the underlying unmarked local ratio $r_p=(p-1)/(p-2)$ if $p\nmid N$ and zero otherwise. Write $d_p=0$ at $p\mid r_0$, $d_p=r_p X_p$ for marked $p\in\mathcal P$, and $d_p=r_p$ otherwise. Here when $p=2\mid N$ the ratio is zero by definition. The rationally completed factors are exactly those of the parity formula with

$$
 P=\prod_p(1-1/p)^2(1+2d_p/p),\qquad \alpha_p=\frac{d_p}{p+2d_p}.
 \tag{2}
$$

In fact the ratio of occupied to unoccupied after rational completion is multiplied by the same $X_p$ whether occupancy was in a fixed signed label or one of the two summed positive labels. This is the same calculation with the local unit and nonunit factors in the squarefree CRT theorem. The singular series is still the true $\Sigma(N)$; the left additive numerator is twisted by the actual $N$, not one multiplied by the alphabet. The norm of $P$ is bounded by the unmarked positive product $P_N\ll1$. For marked $p\ge5$ the geometric inverse defining $\alpha_p$ exists in $\mathscr B$, since $2r_p/p<1$, and

$$
 \|\alpha_p\|\le\frac{r_p}{p-2r_p}\ll p^{-1},\qquad \|\alpha_p\|<1.
 \tag{3}
$$

At unmarked primes $\alpha_p$ is its ordinary nonnegative scalar value or zero. Thus $1-\alpha_p$ is invertible at all primes. Extend $\alpha$ multiplicatively on squarefree integers, and set

$$
 R_j(u)=\sum_{\substack{n\le e^u\\(n,j)=1}}\mu(n)\alpha(n)
 \quad(u\ge0),\qquad R_j(u)=0\quad(u<0).
$$

Let $Q,Q_U,J_U,C(t)$ denote the four parity-formula moments, now interpreted in $\mathscr B$, with $U=(B-B_0)\log L$ and $T(x)=\log(x/D^2)$. Here $Q$ is the quadratic coefficient, not an arc cutoff.

For detail on completing these integrals in norm, the transform of $R_j$ is given by convolving the ordinary reciprocal Möbius primitive with the Euler ratio correcting the coefficients. At $p$, write $\alpha'_p=\alpha_p$ if $p\nmid j$ and zero otherwise. The correction series has coefficient $(1/p-\alpha'_p)/p^{a-1}$ at $p^a$, $a\ge1$, as follows by multiplying $1-\alpha'_p t$ by $(1-t/p)^{-1}$. The resulting kernel of discrete logarithmic shifts has weighted total norm, at exponent $1/4$, at most

$$
 H_j\ll
 \mathcal A(N)\mathcal A(j)\exp\left(C\sum_{p\le z}p^{-3/4}\right),
 \tag{4}
$$

where $\mathcal A(w)=\prod_{p\mid w,\ p>2}(1-\alpha_p^\circ p^{1/4})^{-1}$ is the [radical criterion](r81-spectral-radical-criterion-and-log-exceptions.md) weight, with $\alpha_p^\circ=(p-1)/(p^2-2)$. To see this, for unchanged scalar primes use the positive ordinary correction ratio from the whole mixed theorem. Scalar deletion at divisors of $Nj$ costs the displayed factors $\mathcal A(N)\mathcal A(j)$ and the primes of $r_0$ cost an absolute constant. At marked primes use (3), giving an extra local bound $1+O(p^{-3/4})$. Splitting shifts at $u_0/2$ and using ordinary reciprocal Mertens decay therefore gives, for $\nu=1,2$,

$$
 \|\,\|R_j\|\mathbf1_{u\ge u_0}\|_{L^\nu(du)}
   \ll H_j e^{-c_0\sqrt{u_0}}\quad(u_0\ge1),\qquad
 \|\,\|R_j\|\,\|_{L^\nu(du)}\ll H_j .
 \tag{5}
$$

Here ordinary reciprocal Mertens is exactly the unconditional input in §2 of the whole mixed theorem; the convolution identity follows coefficientwise and Minkowski is applied to norms. The same split gives a pointwise norm tail bound for $R_j(u_0)$. The series $\sum_j\|\alpha(j)\|^2\mathcal A(j)^2 j^{1/4}$ is uniformly bounded, by (3) at large $p$ and the fixed finitely many small factors.

The real-variable integrations can now be taken in $\mathscr B$: for finite cutoffs the same exact two-variable kernels and finite signed gcd expansion as in the parity formula apply. The cutoffs do not depend on any $X_p$. For the signed cap calculation one first clips and subtracts the terminal mass at $L/10-\log j$; (5) and its pointwise version justify removal of that clipping in coefficient norm, using the sum over $j$ just proved. The same submultiplicativity and Cauchy--Schwarz justify the correlation against the two point masses of the second derivative of the cap. Consequently the completed density for either parity is

$$
 \frac{\Sigma(N)P}{2\log x}
 \left(T(x)(Q-Q_U)+J_U
       \ \pm\left(\int_{-T(x)}^{T(x)}C(t)\,dt-T(x)C(T(x))\right)\right).
 \tag{6}
$$

This is the actual real integral with the original above/below cuts, not a surrogate with independently assigned prime labels.

Write $J_\infty=\sum_{j\ {\rm sf}}\mu(j)\alpha(j)^2(\int_0^\infty R_j(u)\,du)^2$. Submultiplicativity and (5), splitting $j$ at $e^{U/2}$ for the low moments, give the bounds on $Q-Q_U,J_U-J_\infty$ in precisely the norm version of §2 of the whole mixed theorem. For $C(T)$ and the integral of $C$ outside $[-T,T]$, at least one of the two primitive arguments is $\ge T$; apply (5) and Cauchy--Schwarz or the $L^1$ product. The norm errors in the bracket, including its factors $T(x)$, are

$$
 \ll \mathcal A(N)^2\exp\left(C\sum_{p\le z}p^{-3/4}-c_1\sqrt v\right),
 \tag{7}
$$

uniform in the physical $x$, with fixed $c_1>0$. Chebyshev and partial summation give $\sum_{p\le z}p^{-3/4}\ll z^{1/4}/\log(2z)=o(\sqrt v)$. The growing positive Euler moments in the radical criterion allow restriction to $\log\mathcal A(N)\le b\sqrt v$ with any fixed $b>0$ outside $O_A(Y\ell^{-A})$. Take $b$ sufficiently small. Thus (7) is $O(e^{-c\sqrt v})$ on one common good family.

The infinite constant is exactly one, as a power series, not just when all marks are $0$ or $1$. Since the ordinary reciprocal primitive has integral one, the integrated correction kernel contributes at each prime $(1-\alpha_p)/(1-1/p)$ when $p\nmid j$ and $(1-1/p)^{-1}$ otherwise. Summing the gcd label gives local factor $(1-2\alpha_p)/(1-1/p)^2$ for $J_\infty$. These manipulations converge in coefficient norm, by (4) and the square-summable outer series; only finitely many primes are marked, and the unchanged infinite unmarked factors have the usual convergent tails. The local product with (2) is identically

$$
 (1-2\alpha_p)(1+2d_p/p)=1 .
$$

Therefore (6) equals the constant polynomial $\Sigma(N)/\log x$ for even parity and zero for odd parity, up to $O(\Sigma(N)e^{-c\sqrt v}/L)$ in norm. This step accounts for every exact occupancy pattern, not only scalar substitutions corresponding to avoidance gates.

## 3. The true complements and bounded target-dependent weights

On the complement of the common auxiliary arcs, for each fixed $s\mid R$ impose the exact tests $s\mid m$ and $(m/s,R)=1$, along with $(m,r_0)=1$. These are fixed tests on actual tuples, not moving cutoffs, because the alphabet is common on the scale $Y$. The [true moving cut Bessel proof](r80-spectral-adaptive-divisor-label-minor.md) applies with these fixed tests and the true parity mask. Its fixed arc set version is the one already used for the adaptive exclusion theorem. In particular the summed squared right cell norms for each fixed $s$ are at most $\sum_{m\le5Y,\ s\mid m,\ m\ {\rm sf}}\tau_{16}(m)$, up to fixed dyadic-level factors. Use weighted Cauchy for the sum of absolute values of coefficients of the auxiliary-minor integral, with weights $s^{-1/2}$ and $s^{1/2}$. The two resulting factors cost, respectively, $\prod_{p\le z}(1+p^{-1/2})$ and

$$
 \sum_{m\le5Y,\ m\ {\rm sf}}\tau_{16}(m)
          \sum_{s\mid(m,R)}s^{1/2}
       \ll Y(1+\ell)^{15}\prod_{p\le z}(1+16p^{-1/2}).
$$

For the latter, write $m=sd$ with $(s,d)=1$ and use the elementary summatory bound for $\tau_{16}(d)$. The crucial estimate $\sum_{p\le z}p^{-1/2}\ll\sqrt z/\log(2z)=O(v)$ makes both extra factors fixed powers of $\ell$. Thus increasing the fixed auxiliary exponent $K$ in the genuine prime supremum, exactly as in the exclusion proof, gives $O_A(Y\ell^{-A})$ for this coefficient norm off $O_A(Y\ell^{-A})$ targets. No union bound over the individual patterns is necessary. By Fourier inversion this establishes the genuine full law in the polynomial encoding.

To restore the exact pattern at 2 and 3, let $T_0$ be a chosen set of the primes among $\{2,3\}$ required present and $E_0=\{2,3\}\setminus T_0$. The actual indicator is

$$
 \mathbf1_{(m,\prod_{p\in E_0}p)=1}\prod_{p\in T_0}(1-\mathbf1_{p\nmid m}).
$$

Its four-case finite expansion uses only the already treated exclusions $r_0\mid6$. The constant polynomial main survives precisely when $T_0$ is empty. Summing the norms over the four actual patterns loses at most an absolute constant; consequently arbitrary $F_N$ contracts this exact simultaneously bounded error and the leading value is $F_N(1)$. This proves (1), also for complex $F_N$.

Lastly the [whole adaptive-pattern minor theorem](r81-spectral-adaptive-prime-pattern-minor.md), with no count slots and either fixed true parity multiplier, applies directly to the entire $F_N(s(m))$ in the original moving minor: $z\ll\log Y$, all its label intervals are the actual ones, and the right function is bounded by one. This has power-saving error off a power-small family, simultaneously over every $F_N,I,\omega$. Subtract it from the true full result to obtain the same asymptotic on the actual original majors. The result does not assert a fixed-target estimate, or an independent bound for prescribed sparse radicals.
