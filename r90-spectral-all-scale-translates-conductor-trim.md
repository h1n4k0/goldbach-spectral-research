# All-scale planted laws after a choice of translate or a conductor-prime trim

**Scope.** The genuine full and original moving polynomial-major mixed-strip correlations have the prescribed generalized Dickman profile on a selected planted divisibility family on every sufficiently large dyad. Everything here is unconditional: neither Dirichlet GRH nor the separate external real-zero-gap result is used. For any fixed proper AP union, one can select among its translates **without changing its AP density**. For any fixed AP union, including the full prime mask, one can instead delete a small, specified portion of its planting primes and use a divisor of the originally prescribed planting integer, without changing the limiting profile. Neither argument proves the law on the complete originally prescribed planting at all scales, on an exact radical or a specified target, or for Hypothesis S. The arithmetic has real prime weights and the original signed composite coefficients, not a model sum.

## Notation and assertions

Use the actual coefficients, tests, and original arcs of [the all-scale exceptional-left reduction](r87-spectral-all-scale-exceptional-left-reduction.md). Thus $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $Y\le N\le2Y$, $L=\log N$, $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$ for fixed admissible $B>B_0>0$. The two $M_{\pm,N}=\frac12(1\pm\mu(m))M_{>,N}$ select even and odd **squarefree prime-factor count** on the actual right support before the overall subtraction. The left interval $I$ is real and half-open in $(N/2,9N/16]$, and the weight $\omega$ has bounded supremum and variation. Write $S_\pm(N;I,\omega)=\sum_{n\in I}\lambda(n)\omega(n)M_{\pm,N}(N-n)$ with $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Write $S_\pm^{\rm maj}$ for the corresponding actual original moving polynomial-major integral, with cap $N^{1/1000}$ and slow radius $2N^{1/1000}/N$ about reduced fractions. It is not the auxiliary major under $Q_0$.

Fix $0<\epsilon<1/2$, a modulus $q_*$ and a nonempty set $\mathcal P$ of reduced residue classes modulo $q_*$. A prime belongs to a set of classes when its class modulo $q_*$ does. Put $J_*=\varphi(q_*)$, $m_*=|\mathcal P|$, $d=m_*/J_*$, and at any prescribed $G^\epsilon\le z\le Z$ put

$$
 K_z(\mathcal P)=2\prod_{\substack{2<p\le z\\p\in\mathcal P}}p,\quad
 \ell=\log z,\quad \theta_z=\frac{\ell}{\log G},\quad
 \mathcal D_{\pm,d}(N;I,\omega;z)
  =\Sigma(N)\mathcal K_{\pm,d}
       \left(\frac{2B}{\theta_z},\frac{B-B_0}{\theta_z}\right)
        \int_I\frac{\omega(u)}{\log(N-u)}\,du .
 \tag{1}
$$

Here $\Sigma(N)$ is the genuine singular series and $\mathcal K_{\pm,d}$ is exactly [the AP Dickman bracket (4)](r83-spectral-ap-radical-major-law.md). In particular $d$ is not adjusted in the formula after the prime deletion below.

**Theorem.** On every sufficiently large dyad:

1. **Fixed-density translates, $d<1$.** There is a subset of at least $J_*-m_*$ of the group elements $a\in(\mathbb Z/q_*\mathbb Z)^\times$, independent of $z$, such that for each its mask is $K'_z=K_z(a\mathcal P)$ and has the conclusion below. Group elements, not necessarily distinct translates, are counted; the translates all have the same stabilizer size, so in particular at least a proportion $1-d$ of the distinct translates has the conclusion.
2. **A divisor of the prescribed planting, $0<d\le1$.** There is one finite set $\mathcal R_Y$ of odd planting primes at most $Z$, independent of $z$, such that $K'_z=K_z(\mathcal P)/\prod_{p\in\mathcal R_Y,\,p\le z}p$ has the conclusion below. One can take $\mathcal R_Y=\varnothing$ when there is no Page zero of R87. If there is one of conductor $r$, let $H=\log r$ and $W=\min(\sqrt{H\log G},\sqrt{G^\epsilon\log G})$. Then the construction satisfies

$$
 \sum_{p\in\mathcal R_Y}\log p\le W+\log Z=o(G^\epsilon),\qquad
 \sum_{p\in\mathcal R_Y}\frac{\log p}{p}
                   \ll \frac{W+\log Z}{H}=o(1).
 \tag{2}
$$

In particular $K'_z\mid K_z(\mathcal P)$ and $\log K'_z/\log K_z(\mathcal P)\to1$ uniformly in $z$. The selection may use the actual conductor; no effectiveness claim is made.

**Conclusion in either case.** For each fixed $A>0$ and each prescribed $z$, outside $O_A((Y/K'_z)G^{-A})$ members of $\{N\in[Y,2Y]\cap\mathbb Z:K'_z\mid N\}$, for both signs and all actual hard/BV tests,

$$
 S_\pm(N;I,\omega),\ S_\pm^{\rm maj}(N;I,\omega)
   =\mathcal D_{\pm,d}(N;I,\omega;z)
     +o\!\left(\frac{\Sigma(N)|I|}{L}\right)+O_A(YG^{-A}).
 \tag{3}
$$

The errors and counts are uniform in $z$ and the retained choices of $a$; constants may depend on the fixed $\epsilon,\mathcal P,B,B_0$ and the bound on the left tests. Exceptional sets are relative to each specified divisor $K'_z$, not a common set valid for all $z$. The original moving minor retains the unconditional $O(Y^{1-1/40000})$ bound on the retained targets, by the original minor input in the folded theorem. Since $K'_z\le e^{2Z}$ and even, these divisibility families have size asymptotic to $Y/K'_z$. The theorem counts even targets automatically. The asymptotic natural-scale error and the separate absolute $YG^{-A}$ error in (3) should not be interchanged on very short intervals.

## 1. A simultaneous outside-conductor factor for every threshold

We use [the exact-bracket consequence of the folded second moment, (8)--(9)](r89-spectral-exceptional-conductor-folded-sampling.md#3-consequences-for-the-genuine-full-and-original-major-sums). For any specified divisor integer $K\le e^{2Z}$ it gives the genuine full and original-major sums equal to the exact completed finite-cut bracket $\mathcal B_\pm(N;I,\omega)$ plus $O_A(YG^{-A})$, with relative exception $O_A(G^{-A})$, provided either the Page zero is absent or

$$
 \log(r/(r,K))+2(1-\beta)G\ \ge\ (C+3A)\log G .
 \tag{4}
$$

The original minor bound there is on the true minor. We will use only the first term on the left in (4), not an assumption on the gap. The classical conductor lower bound in [Section 1 of R87](r87-spectral-all-scale-exceptional-left-reduction.md#1-remove-only-multiples-of-the-exceptional-conductor-in-the-auxiliary-calculation) is $r>G^T$ for every fixed $T$ eventually, uniformly when this Page zero exists. We use it in the form $H/\log G\to\infty$ along those scales. The ordinary prime number theorem gives $K'_z\le e^{2Z}$ for all large $G$, even for the full prime mask. One could also apply the fixed AP prime number theorem here. No condition on the distribution of primes in a growing modulus is needed.

For the first part fix the cutoff at the **common cap $Z$**. Each odd prime at most $Z$ coprime to $q_*$ belongs to exactly $m_*$ of the translates $a\mathcal P$ when all $J_*$ group elements are counted. In fact its class determines $a$ uniquely for each original class in $\mathcal P$. Nonunits and primes above $Z$ belong to none. Thus if $\mathcal A$ is any $m_*+1$ of these elements, each odd prime occurs in at most $m_*$ of the squarefree integers $K_Z(a\mathcal P)$ with $a\in\mathcal A$, and the prime $2$ can appear $m_*+1$ times. Even if $r$ is not squarefree this proves

$$
 \prod_{a\in\mathcal A}(r,K_Z(a\mathcal P))
                \ \le\ 2^{m_*+1}r^{m_*}.
 \tag{5}
$$

If all $m_*+1$ of their quotients $r/(r,K_Z(a\mathcal P))$ were strictly smaller than $\tfrac12 r^{1/(m_*+1)}$, their product of gcds would strictly exceed (5). Consequently at most $m_*$ of the $J_*$ translates fail the quotient test. When there is no zero all translates may be used. For each retained $a$ the quotient at a smaller $z$ can only increase, since $K_z(a\mathcal P)$ divides $K_Z(a\mathcal P)$. Its logarithm exceeds $(C+3A)\log G$ for each fixed $A$ as $G\to\infty$ by the classical bound on $r$. Both the selection and the consequent arithmetic estimate are uniform in $z$. Taking all $J_*$ in the same product also gives at least one quotient at the cap at least $\tfrac12r^{1-d}$, but this stronger single-translate exponent is not required.

For the second part suppose the conductor exists. At the cap put $g=(r,K_Z(\mathcal P))$. If $\log(r/g)\ge W$, choose no deletion. Otherwise $\log g>H-W$. The elementary Chebyshev bound $\sum_{p\le x}\log p\le C_\vartheta x$ for $x\ge2$ allows a fixed $\lambda>0$ so small that $C_\vartheta\lambda<1/4$. Since $g$ is squarefree, the primes dividing $g$ with $p>\lambda H$ have total logarithmic mass at least

$$
          \log g-\sum_{p\le\lambda H}\log p
                          > 3H/4-W .
 \tag{6}
$$

This exceeds $W$ for all sufficiently large $G$ because $W/H\to0$. They are odd for large $G$. If $\lambda H\ge Z$, inequality (6) contradicts this case, so no high-prime selection is necessary there. Otherwise choose such common primes until their sum of logarithms first reaches $W$; the last increment is at most $\log Z$. Call this set $\mathcal R_Y$. The true quotient for $K'_Z$ then has logarithm at least $W$, since removing a prime dividing the squarefree $g$ divides that gcd by the prime. A smaller cutoff yields a divisor of $K'_Z$ with no worse quotient. At the same time $\sum_{\mathcal R_Y}(\log p)/p\le(\lambda H)^{-1}(W+\log Z)$. Here $W/\log G\to\infty$, $W/H\to0$, and $W/G^\epsilon\to0$ by its definition and $H/\log G\to\infty$. These facts prove (2), as well as (4) for every fixed $A$ without using $1-\beta$. The logarithmic ratio follows by $\log K_z(\mathcal P)\sim dz$ from the fixed AP prime number theorem and $z\ge G^\epsilon$. The chosen primes are an arithmetic deletion from the planting integer, not a further selector on $M_{\pm,N}$.

Applying the folded theorem now gives the true two sums at $\mathcal B_\pm$ with the stated absolute error and relative exceptional count on either family in the theorem. The remainder of the proof evaluates the exact bracket on these families and controls its **target** exceptions.

## 2. An extra-mask moment on the actual multiples

For any selected $K'_z$ above, on its actual multiples put

$$
 X_N=\sum_{\substack{p\mid N\\p\nmid K'_z}}\frac{\log p}{p}.
$$

Uniformly for these divisors, outside $O_A((Y/K'_z)G^{-A})$ of their multiples on the dyad, one has

$$
                       X_N\ll\log(2\ell).
 \tag{7}
$$

Here is an elementary strong tail at this threshold. Write $a_p=(\log p)/p$. For real $s\ge2$ expand the positive product for $e^{s X_N}$ over squarefree divisors $h$ composed only of primes outside $K'_z$. The number of these actual multiples for which $h\mid N/K'_z$ is at most $2Y/(K'_z h)$. Therefore

$$
 \frac{K'_z}{Y}\sum_{\substack{Y\le N\le2Y\\K'_z\mid N}} e^{sX_N}
 \ \le\ 2\prod_p\left(1+\frac{e^{sa_p}-1}{p}\right)
 \ \le\ 2\exp\!\big(C_1s\log(2s)\big).
 \tag{8}
$$

Indeed each factor's log is at most $sa_p$ for $p\le s^2$, and $\sum_{p\le s^2}\log p/p\ll\log(2s)$ by Chebyshev and partial summation. For $p>s^2$, $sa_p\le 2\log(s)/s\le1$, and the log factors sum to $\ll s\sum_{n>s^2}\log(n)/n^2\ll1$. The product converges for each $s$. Take $s=\ell$, eventually at least $2$, and discard $X_N>2C_1\log(2\ell)$ (enlarge $C_1$ if needed). The bound is $2(Y/K'_z)e^{-C_1\ell\log(2\ell)}$, smaller than the required count for every fixed $A$ uniformly since $\ell\ge\epsilon\log G$. This uses the actual subfamily of multiples, not a model of independent prime divisibility.

## 3. Transfer the genuine Euler primitives through the omitted primes

Use the signed normalized Euler primitive of [the AP-mask proof, Sections 1--2](r83-spectral-ap-radical-major-law.md). For even $K$ use $\alpha_p^\circ=(p-1)/(p^2-2)$ on odd primes, delete $p\mid K$ and the primes of a squarefree $j$, and write $R_{K,j}(u)$ for the resulting signed reciprocal cumulative as in that proof, zero for $u<0$. Put $M_{K,j}=\int R_{K,j}>0$ and

$$
             f_{K,j}(v)=\frac{\ell R_{K,j}(\ell v)}{M_{K,j}} .
 \tag{9}
$$

The scale $\ell$ here is always the logarithm of the original threshold $z$. For the complete fixed AP mask $K_z(\mathcal P)$, and for any of the finitely many complete translates, that proof gives for each fixed $j$

$$
 f_{K_z,j}\longrightarrow f_d\text{ in }L^1,\qquad
           v f_{K_z,j}(v)\longrightarrow v f_d(v)\text{ in }L^2 ,
 \tag{10}
$$

where $f_d$ is exactly the normalized probability density of (1). This part of the AP-mask proof is unconditional; its GRH assumptions concern evaluation of original arcs on prescribed exact-radical targets, not (10). The convergence is uniform across the allowed $z$ as $G\to\infty$ since $z\ge G^\epsilon$, and across the finite translates. The two elementary bounds $\|f_{K,j}\|_1\ll1$ and $\|f_{K,j}\|_2\ll\sqrt\ell$ from (5) there hold for **any** finite mask $K$: their proof is the ordinary reciprocal Möbius primitive convolved with a normalized positive Euler measure. The pointwise bound $|v f_{K,j}(v)|\ll1$ on $v>0$ from (7) there also holds for any such mask. In its differentiation proof, each local coefficient $p^{-k}-\beta_p^k$ lies between $0$ and $p^{-k}$; hence the prime-in-log-bin upper bounds in that proof never used the AP restriction. These uniform bounds will apply in particular to the exact mask of $N$.

For the trimmed family take $K_z=K_z(\mathcal P)$. For a removed prime $p\le z$ not already masked by $j$, unmasking $p$ multiplies the unnormalized reciprocal primitive by the convolution factor $\delta_0-\alpha_p^\circ\delta_{\log p}$ on the raw log line. This follows by comparing the two signed Euler coefficients on every prefix: an unmasked term supported at $p$ is $-\alpha_p^\circ$ times the prefix of the former sequence shifted by $\log p$, whose support was coprime to $p$. Its total mass is $1-\alpha_p^\circ$. Thus after the normalization and scaling of (9), the exact operation is convolution by the signed finite measure

$$
 \nu_p=\frac{\delta_0-\alpha_p^\circ\delta_{\log p/\ell}}{1-\alpha_p^\circ}.
 \tag{11}
$$

If $p\mid j$ the operation is the identity and that prime is omitted from the product. The convolution $\nu$ of the remaining finitely many $\nu_p$ satisfies

$$
 \begin{split}
 \|\nu-\delta_0\|_{\rm TV}
       &\ll e^{C_2 U_0} U_0,\qquad
   \int_0^\infty t\,d|\nu|(t)\ll e^{C_2 U_0}\,U_1/\ell,\\
 U_0&=\sum_{p\in\mathcal R_Y,\,p\le z}\alpha_p^\circ,\qquad
 U_1=\sum_{p\in\mathcal R_Y,\,p\le z}\alpha_p^\circ\log p=o(1).
 \end{split}
 \tag{12}
$$

For the first use $\|\nu_p\|_{\rm TV}=(1+\alpha_p^\circ)/(1-\alpha_p^\circ)$ and telescope the differences from the unit atom. For the second, convolution of the positive measures $|\nu_p|$ dominates total variation and its first moment is at most the product of the variation masses times $\sum_p(\log p/\ell)\alpha_p^\circ/(1+\alpha_p^\circ)$. The final bound on $U_1$ follows from (2) and $\alpha_p^\circ\le 1/p$. It gives $U_0=o(1)$ also because these primes are odd. All these bounds remain valid independently of the excluded $j$ primes.

We have the exact identity $f_{K'_z,j}=\nu*f_{K_z,j}$. By (10) and (12) this changes the $L^1$ profile by $o(1)$. For the weighted $L^2$ profile, multiplication by log position satisfies $v(\nu*f)=\nu*(vf)+(t\nu)*f$ by writing $v=(v-t)+t$ in the convolution. Its difference therefore costs at most

$$
       \|\nu-\delta_0\|_{\rm TV}\,\|v f_{K_z,j}\|_2+
       \left(\int t\,d|\nu|(t)\right)\|f_{K_z,j}\|_2=o(1).
 \tag{13}
$$

In fact the first norm of $vf_{K_z,j}$ is bounded for every fixed $j$ by (10), and the latter unweighted norm is $O(\sqrt\ell)$, not assumed bounded when $d\le1/2$. Thus the same two convergences (10) hold for $K'_z$. In the translate case there is no deletion and this follows directly from (10). This transfers the density $d$ even for the trimmed full-prime mask $d=1$; replacing it by a $z$-dependent AP density is unnecessary.

Now $N$ may have extra primes outside $K'_z$. At each such odd prime not dividing $j$, adding its mask multiplies the normalized scaled Euler measure by the positive probability $(1-\alpha_p^\circ)\sum_{k\ge0}(\alpha_p^\circ)^k\delta_{k\log p/\ell}$. The total convolution $\pi_{N,j}$ of these measures has mean at most $C X_N/\ell$ by the geometric-series mean and $\alpha_p^\circ\le1/p$. Thus $f_{N,j}=\pi_{N,j}*f_{K'_z,j}$ exactly. On (7), this mean is $O(\log(2\ell)/\ell)=o(1)$ uniformly in $j,N,z$. The convolution preserves (10): in $L^1$, use that $\pi_{N,j}$ is a probability and translations of $f_d$ are continuous in $L^1$, splitting the shifts at a fixed small threshold and bounding the remainder by the first moment. For the weighted norm use the same argument in $L^2$ for $v f_d$, together with $\|(t\pi_{N,j})* f_{K'_z,j}\|_2\ll (X_N/\ell)\sqrt\ell=o(1)$. This uses only the strong *limit* in (10), not an unpublished rate or global square integrability of the limiting profile. We conclude that on the retained actual multiples

$$
  \|f_{N,j}-f_d\|_1+\|v(f_{N,j}-f_d)\|_2=o(1)
 \tag{14}
$$

for every fixed $j$, uniformly in the moving $z$ and the declared choices. For both deletions and additions the identities used the true mask, including repeated prime powers in $N$ affecting it only through divisibility.

## 4. Invert the exact finite-cut bracket

For completeness, the transfer to (3) through the actual thresholds is as follows. Write $x=N-u$, $T(x)=\log(x/D^2)$ and $U=(B-B_0)\log L$ as in the [exact parity formula](r67-spectral-high-mixed-parity-major.md). Let $\tau_x=T(x)/\ell$ and $\upsilon_j=(U-\log j)_+/\ell$. For a real profile $f$ supported on $[0,\infty)$, write $C_f(t)=\int f(v)f(v+t)\,dv$. After scaling, the bracket inside $\Sigma(N)\int_I\omega(u)/\log x\,du$ in $\mathcal B_\pm$ is

$$
 \frac12\sum_{j\ {\rm sf}}c_{N,j}
    \left\{\tau_x\int_{\upsilon_j}^\infty f_{N,j}(v)^2\,dv
            +\left(\int_0^{\upsilon_j} f_{N,j}\right)^2
     \ \pm\left(\int_{-\tau_x}^{\tau_x} C_{f_{N,j}}(t)\,dt
                      -\tau_x C_{f_{N,j}}(\tau_x)\right)\right\},
 \quad c_{N,j}=P_N\mu(j)\alpha_N(j)^2 M_{N,j}^2 .
 \tag{15}
$$

This is an exact rescaling: when $j>e^U$ the terminal cut is at zero and the truncated cumulative term vanishes. The signed coefficients satisfy $\sum_j c_{N,j}=1$ and $\sum_j j^{1/2}|c_{N,j}|\ll1$ by the same Euler identity [R83 (6)](r83-spectral-ap-radical-major-law.md), valid for any fixed actual $N$. For $j>e^{U/2}$ the absolute cost in (15) is $O((1+\ell)e^{-U/4})=o(1)$ by the universal $L^1$ and crude squared $L^2$ bounds. For the other $j$, the terminal cut is bounded below by a positive constant and $\tau_x$ is in a compact positive interval, since $\theta_z\in[\epsilon,1/2]$. Their braces are bounded uniformly using $|v f_{N,j}(v)|\ll1$, $L^1$, and convolution. For every fixed $j$, the real endpoint differences $\tau_x-2B/\theta_z$ and $\upsilon_j-(B-B_0)/\theta_z$ tend to zero uniformly, using $x\asymp Y$ and $L=G+O(1)$.

Specifically, (14) controls the terminal square on a half-line bounded away from zero by weighted $L^2$ and Cauchy--Schwarz, and its endpoint movement by the bounded density there. The cumulative term and the integrated autocorrelation follow by $L^1$ and Young's inequality. For the pointwise autocorrelation at $t$ in a fixed positive compact interval, split its integration variable at a small fixed $v_0>0$. On $[0,v_0]$, $\int |f_{N,j}|\le \int_0^{v_0}f_d+o(1)$ by (14), and the shifted profiles are uniformly bounded by the universal $|vf|$ estimate. On $[v_0,\infty)$ apply Cauchy--Schwarz to the differences using (14) and the lower bounds for both $v$ and $v+t$. The limit $C_{f_d}(t)$ is continuous for $t>0$ by the same split and translation continuity on the part separated from zero. Its shifted supremum bound follows from the [positive Dickman delay identity](r83-spectral-ap-radical-major-law.md#4-what-changes-at-one-half-density), or from the corresponding uniform bound already obtained in (10). This proves convergence uniformly at the moving positive cap even when $f_d\notin L^2$ globally.

Now take a fixed large finite set of $j$ first, use (14) and the endpoint checks there, and then send the size of the set to infinity using the uniform half-moment and the large-$j$ estimate. Since the signed weights sum exactly to one, (15) is $\mathcal K_{\pm,d}(2B/\theta_z,(B-B_0)/\theta_z)+o(1)$ uniformly on the retained targets and real $x$. Integrating against the original hard/BV test gives the natural-scale error in (3). The only additional arithmetic exceptional count used after the exact bracket was (8); it is within the stated $O_A((Y/K'_z)G^{-A})$. This proves the two unconditional genuine sum assertions without changing the original minor arcs or the cutoffs.
