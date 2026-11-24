# The original mixed-strip major law for fixed AP prime masks

**Scope.** A growing target radical made from a fixed set of prime residue classes need not have the same major coefficient as a growing primorial. The exact original polynomial major of the genuine mixed squarefree strip has a generalized Dickman limit, for every positive density of a fixed union of reduced classes, including density at most one-half. The profile then has a non-square-integrable cusp, but the actual cutoff and positive autocorrelation shift remove that difficulty. This evaluates **only** the original major arcs under the historical prime and masked Möbius Dirichlet-GRH inputs of the [pointwise parity formula](r67-spectral-high-mixed-parity-major.md). It does not evaluate the full coefficient or original minor arcs on these sparse subsequences, or imply weak S or Hypothesis S.

Fix a modulus $q_*\ge1$ and a nonempty union $\mathcal P$ of reduced residue classes modulo $q_*$, interpreted below as a set of primes, and let $d=|\mathcal P_{\rm classes}|/\varphi(q_*)\in(0,1]$. Take even targets $N$ along any sequence with

$$
 \operatorname{rad}(N)=2\!\!\prod_{\substack{2<p\le z\\p\in\mathcal P}}p,
 \quad z\to\infty,\qquad
 \frac{\log z}{\log\log N}\longrightarrow\vartheta\in(0,1].
 \tag{1}
$$

For example the powers $\lfloor z^{1/\vartheta-1}\rfloor$ of the displayed radical suffice, since the logarithm of that radical is asymptotic to $dz$ by the prime number theorem in fixed progressions. Set $L=\log N$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ for fixed admissible $B>B_0>0$, and $V=[N/3,2N]$. Keep the true $M_\pm=(1\pm\mu(m))M_>/2$ on squarefree partners, with $M_>$ the exact above-BV mixed strip before the overall minus. The $+$ sign denotes an even number of distinct prime factors, not even numerical $m$. The exact hard left interval $I\subset(N/2,9N/16\,N]$ is half-open, $\omega$ has uniformly bounded supremum and variation, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$ is the left sequence before weighting. As in the parity formula, $\mathfrak M_N$ integrates the corresponding actual Fourier product over $q\le Q=N^{1/1000}$ and $|\eta|\le2Q/N$ about reduced $a/q$.

Write $f=f_d$ for the generalized Dickman probability density, zero on the negative half-line, with Fourier convention $\widehat f(\xi)=\int_{\mathbb R}f(v)e^{-i\xi v}\,dv$ and

$$
 \widehat f_d(\xi)=\exp\left(d\int_0^1
                            \frac{e^{-i\xi v}-1}{v}\,dv\right).
 \tag{2}
$$

This is the normalized convolution-power family in [Hensley's paper](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms/s2-33.3.395). We verify existence and the profile properties needed below. For $v\ge0$ put $F_d(v)=\int_0^v f_d(w)\,dw$, and for $t\ne0$ put $C_d(t)=\int_{\mathbb R}f_d(v)f_d(v+t)\,dv$. The value of $C_d$ at $0$ can be left arbitrary in its shift integral. Let $\tau=2B/\vartheta$, $\upsilon=(B-B_0)/\vartheta$.

**Theorem.** Under the stated historical inputs, uniformly in the true $I,\omega$ and the physical cutoff, the original major on (1) satisfies, for each fixed $A>0$,

$$
 \mathfrak M_N(M_\pm;I,\omega)=
  \Sigma(N)\,\mathcal K_{\pm,d}(\tau,\upsilon)
      \int_I\frac{\omega(y)}{\log(N-y)}\,dy
   +o\!\left(\frac{\Sigma(N)|I|}{L}\right)+O_{A,B,B_0}(NL^{-A}),
 \tag{3}
$$

where $\Sigma(N)$ is the original singular factor and

$$
 \mathcal K_{\pm,d}(\tau,\upsilon)=
 \frac12\left[
   \tau\int_{\upsilon}^\infty f_d(v)^2\,dv+F_d(\upsilon)^2
    \ \pm\left(\int_{-\tau}^{\tau}C_d(t)\,dt-\tau C_d(\tau)\right)\right].
 \tag{4}
$$

The additive error is retained even for very short $I$; for interval length at least a fixed inverse-log fraction of $N$ one may take $A$ large enough. At $d=1$ the formula agrees with the [primorial-radical law](r82-spectral-primorial-radical-major-law.md). When $d\le1/2$, both constants in (4) tend to $+\infty$ as $\upsilon\downarrow0$ at a fixed positive $\tau$, with explicit powers or logarithm in Section 4. That refers to choosing different fixed allowed cuts before the $N$ limit, not an estimate uniform down to an $N$-dependent cutoff.

## 1. Exact marked mask, mass and a bound away from zero

Set $\ell=\log z$. In the [pointwise parity formula](r67-spectral-high-mixed-parity-major.md) let $\alpha_p=0$ on $p\mid N$, and $\alpha_p=(p-1)/(p^2-2)$ otherwise, with $\alpha$ multiplicative on squarefree integers. For squarefree $j$ define $\beta_p=\alpha_p\mathbf1_{p\nmid j}$. The actual signed primitive is $R_{N,j}(u)=\sum_{a\le e^u,(a,j)=1}\mu(a)\alpha(a)$, zero on $u<0$. Write $R(u)=\sum_{a\le e^u}\mu(a)/a$ on $u\ge0$, and zero otherwise. The [ordinary reciprocal Mertens estimate](r70-spectral-signed-shift-euler-slots.md#1-fourier-weight-of-the-rough-reciprocal-primitive) gives $|R(u)|\ll e^{-c\sqrt u}$ and $\int R=1$; the integral follows by taking $s\downarrow0$ in its Laplace transform $1/(s\zeta(1+s))$.

Relative to $R$ the exact positive log-convolution factor at $p$ has Laplace transform $(1-\beta_p p^{-s})/(1-p^{-1-s})$. It is the unit atom at $0$ plus the atoms of mass $(1/p-\beta_p)p^{-(k-1)}$ at $k\log p$ for $k\ge1$. This includes deleted primes $\beta_p=0$. Unmasked, nonexceptional factors have extra mass $O(p^{-2})$, so the convolution exists as a finite positive measure for each $z,j$. Comparing the Euler coefficients on every finite prefix proves the primitive identity. Let $M_{z,j}=\int R_{N,j}>0$, the mass of the convolution kernel. Write $\pi_{z,j}$ for its normalized positive probability after scaling the log positions by $1/\ell$, and put $a_\ell(v)=\ell R(\ell v)$, $f_{z,j}(v)=\ell R_{N,j}(\ell v)/M_{z,j}$. Then exactly

$$
          f_{z,j}=\pi_{z,j}*a_\ell,\qquad
          \|f_{z,j}\|_1\le\|R\|_1,\qquad
          \|f_{z,j}\|_2^2\le\ell\|R\|_2^2 .
 \tag{5}
$$

For the Euler coefficient of $j$ in the rescaled formula write $c_{N,j}=P_N\mu(j)\alpha(j)^2 M_{z,j}^2$. The exact mass and uniform half-power bound are

$$
 \sum_{j\ {\rm sf}}c_{N,j}=1,\qquad
 \sum_{j\ {\rm sf}}j^{1/2}|c_{N,j}|\ll1.
 \tag{6}
$$

Indeed $M_{z,j}/M_{z,1}=\prod_{p\mid j}(1-\alpha_p)^{-1}\le j/\varphi(j)$. As in the primorial proof, $P_N M_{z,1}^2=\prod_p (1-\alpha_p)^2/(1-2\alpha_p)\ll1$, now including the nondeleted primes below $z$ as well. The local formula for $P_N$ used there applies to all masks. The $j$ product for the signed sum in (6) then cancels this factor exactly, since $1-(\alpha_p/(1-\alpha_p))^2=(1-2\alpha_p)/(1-\alpha_p)^2$. The absolute half-power moment is bounded by Euler increments $O(p^{-3/2})$. We do not discard all $j>1$: on an AP-masked radical, fixed nondeleted primes can contribute such $j$.

There is a uniform real-space bound, including all $j$:

$$
                     |v f_{z,j}(v)|\ll1\qquad(v>0).
 \tag{7}
$$

In fact the logarithm of the characteristic transform of $\pi=\pi_{z,j}$ is the absolutely convergent series

$$
  \log\widehat\pi(\xi)=
   \sum_{p,k\ge1}\frac{p^{-k}-\beta_p^k}{k}
                       (e^{-i\xi k\log p/\ell}-1).
 \tag{8}
$$

Here and below the sum ranges over primes $p$ and integers $k\ge1$. For each fixed $z,j$ the measure has a finite first moment. Differentiate (8) and use uniqueness of Fourier transforms of finite measures: multiplying a measure by its position gives $v\pi=\sigma*\pi$, with the positive measure

$$
   \sigma=\frac1\ell
       \sum_{p,k\ge1}(\log p)(p^{-k}-\beta_p^k)
                              \delta_{k\log p/\ell}.
 \tag{9}
$$

Every log-position interval of length $1/\ell$ has $\sigma$ mass $O(1/\ell)$, independently of $j$. For $k=1$ bound by all primes in an unscaled log interval of length $1$, using Chebyshev and partial summation (the endpoint convention adds at most a constant). For $k\ge2$ use the finite full sum $\sum_{p,k\ge2}(\log p)/p^k$. Thus
$\|\sigma*a_\ell\|_\infty\ll\sum_{k\ge0}\sup_{k\le u\le k+1}|R(u)|\ll1$, by dividing the arguments of $R$ into unit intervals. Also $\|v a_\ell\|_\infty=\sup_{u\ge0}u|R(u)|\ll1$. The rule for multiplication by position in a convolution gives $v f_{z,j}=\pi*(v a_\ell)+\pi*(\sigma*a_\ell)$; this proves (7). The identities can also be read as identities of densities almost everywhere, which is all that is required for the integrals.

## 2. Weighted convergence without global square integrability

Fix $j$. We will show

$$
 f_{z,j}\longrightarrow f_d\text{ in }L^1(\mathbb R),\qquad
 v f_{z,j}(v)\longrightarrow v f_d(v)\text{ in }L^2(\mathbb R).
 \tag{10}
$$

For each fixed $\xi$, (8) converges to the logarithm in (2). The leading part is $k=1$ for the primes $\mathcal P$ up to $z$, with the prime $2$ contributing at most one additional fixed term. The fixed-AP prime number theorem gives $\sum_{p\le X,p\in\mathcal P}p^{-1}=d\log\log X+C_{\mathcal P}+o(1)$ by partial summation. Thus by partitions, for any fixed $\epsilon>0$ the reciprocal measure on $z^\epsilon<p\le z$ converges in the log-ratio coordinate to $d\,dv/v$ on $[\epsilon,1]$. The omitted small primes cost $O(|\xi|(\epsilon+\ell^{-1}))$ by $\sum_{p\le X}(\log p)/p\ll1+\log X$. The $k\ge2$ terms tend to zero by dominated convergence, and the remaining $k=1$ terms are dominated for fixed $j$ by the sum of $O(p^{-2})$ replacements and finitely many fixed exceptions. Taking $\epsilon\downarrow0$ yields (2) for the pointwise limit of $\widehat f_{z,j}$ also, since $\widehat a_\ell(\xi)=\widehat R(\xi/\ell)\to1$. Exactly the same argument with $e^{-sk\log p/\ell}$ gives the Laplace limits of $\pi_{z,j}$ for fixed $s\ge0$:

$$
    \mathcal L_d(s)=\exp\left(d\int_0^1\frac{e^{-sv}-1}{v}\,dv\right).
 \tag{11}
$$

We use a weighted Plancherel argument to turn this into convergence on the scale of the cutoff. Let $t=\xi/\ell$. If $j$ is fixed, the logarithmic derivative of (8) is

$$
 \partial_\xi\log\widehat\pi_{z,j}(\xi)=
       -\frac{i}{\ell}\sum_{\substack{p\le z\\p\in\mathcal P}}
                     \frac{\log p}{p}e^{-it\log p}
        +O_j(\ell^{-1}).
 \tag{12}
$$

The remainder is uniform in real $\xi$: the $k\ge2$ weights have finite full sum, and the first powers of the replacement weights outside the true mask cost $\sum_p(\log p)/p^2$ plus finitely many exceptions. The prime $2$ is covered whether included in the AP union or not. A bound for the oscillatory prime sum on $e^a<p\le e^b$ comes from partial summation of the fixed-AP prime number theorem in $\vartheta$ form, namely the fixed-modulus case of [Montgomery–Vaughan, Chapter 11, Corollary 11.19 and its $\vartheta$ consequence](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF). Its main term is $d\int_a^b e^{-itu}\,du$ and its error is
$O_{q_*}((1+|t|)(1+a)e^{-c\sqrt a})$, uniformly in $b\ge a\ge\log 2$, decreasing $c>0$ if necessary. In fact the end terms have exponential decay in the log variable and the integral error is bounded by $(1+|t|)\int_a^\infty e^{-c_0\sqrt u}du$.

For $|t|\le1$ start at $\log 2$, absorbing the endpoint prime. The main integral divided by $\ell$ is $O(\min(1,1/|\xi|))$ and the error is $O_{q_*}(1/\ell)$. Since $|\xi|\le\ell$, (12) is $O_{q_*,j}((1+|\xi|)^{-1})$. For $|t|\ge1$ set $a=C(1+\log(3+|t|))^2$ with $C$ sufficiently large. The part below $e^a$ is $O(1+a)$ by Chebyshev and partial summation. If $a<\ell$, the rest of the sum is $O(1)$ by the oscillatory main integral and the stated error. Thus (12) is $O_{q_*,j}((1+\log(3+|t|))^2/\ell)$. For each fixed $\xi$ the same low-frequency calculation shows that (12) converges to $-id\int_0^1 e^{-i\xi v}dv$.

The ordinary $\widehat R$ and $\widehat R'$ are bounded for $|t|\le1$ by the first moment of $|R|$. For $|t|\ge1$ they are $O((1+\log(3+|t|))^4/|t|)$: for the derivative use integration by parts on $uR(u)$ truncated at $C'(1+\log(3+|t|))^2$, as for $\widehat R$ in the [rough Fourier proof](r70-spectral-signed-shift-euler-slots.md#1-fourier-weight-of-the-rough-reciprocal-primitive). The piecewise variation of $uR(u)$ on $[0,H]$ is $O((1+H)^2)$, by summing the jump sizes at $\log n$ and integrating the bounded continuous slopes. The discarded $L^1$ tail is $O(|t|^{-2})$ for $C'$ large. Using $|\widehat\pi|\le1$ and differentiating $\widehat f_{z,j}=\widehat\pi\,\widehat R(\xi/\ell)$ now gives

$$
    |\partial_\xi\widehat f_{z,j}(\xi)|
         \ll_{q_*,j}\frac{(1+\log(3+|\xi|))^6}{1+|\xi|}.
 \tag{13}
$$

For the high range the factor $\ell^{-1}|t|^{-1}$ is exactly $|\xi|^{-1}$, and for the low range $\ell^{-1}\ll(1+|\xi|)^{-1}$. This estimate does not require a density greater than one-half. The derivatives converge pointwise to the derivative of (2), by (12) and boundedness of $\widehat R'(\xi/\ell)$. The right side of (13) has integrable square. Plancherel and dominated convergence therefore give strong $L^2$ convergence of $v f_{z,j}$. For the use of Plancherel, these functions belong to $L^1\cap L^2$ for each finite $z$ by (5), the finite first moment of $\pi$, and the corresponding norms of $v a_\ell$.

On every bounded interval away from zero this gives strong $L^1$ convergence of $f_{z,j}$. To get global $L^1$, at large $v$ use a first-moment bound: $\int v\,\pi_{z,j}(dv)=O_{q_*,j}(1)$ by (12) at zero, and $\int v|a_\ell(v)|\,dv=O(\ell^{-1})$. Thus the $L^1$ tails of the absolute $f_{z,j}$ beyond $b$ are $O_{q_*,j}(1/b)$. Near zero use support on $[0,\infty)$ to get
$\int_0^\epsilon |f_{z,j}|\le\|R\|_1\pi_{z,j}([0,\epsilon])$. By nonnegativity the latter measure is bounded by $e$ times its Laplace transform at $1/\epsilon$. Formula (11) gives a $\limsup$ bound $O_d(\epsilon^d)$ by splitting the defining integral at $v=\epsilon$. These bounds prove the claimed global $L^1$ convergence, by Cauchy convergence first on compact intervals and then sending their endpoints to $0$ and $\infty$. The limiting density has transform (2) and does not depend on $j$. Its mass is $1$ since $\int f_{z,j}=1$. It is nonnegative: testing $f_{z,j}$ against any nonnegative compactly supported Lipschitz function differs from testing the positive $\pi_{z,j}$ by $O(\ell^{-1})$ times the Lipschitz constant, since $\int R=1$ and $\int u|R(u)|du<\infty$. The weighted $L^2$ limit equals $v f_d$ by agreement locally away from zero, proving (10). The Laplace transform of the limit is (11) by $L^1$ convergence and the original convolution. The bound $|vf_d(v)|\ll1$ holds almost everywhere by (7) and convergence.

## 3. The hard cutoff and the positive shift

Use $U=\log(H_0/D)$ and $T=T(x)=\log(x/D^2)$ for $x=N-y\in V$. For each squarefree $j$ set $\upsilon_{z,j}=(U-\log j)_+/\ell$ and $\tau_z(x)=T/\ell$. The bracket from the [pointwise parity formula, (3)](r67-spectral-high-mixed-parity-major.md), including its $P_N$ factor, is exactly the sum over $j$ of $c_{N,j}$ times

$$
 \tau_z(x)\int_{\upsilon_{z,j}}^\infty f_{z,j}(v)^2\,dv
    +\left(\int_0^{\upsilon_{z,j}} f_{z,j}(v)\,dv\right)^2
  \ \pm\
 \left(\int_{-\tau_z(x)}^{\tau_z(x)} C_{f_{z,j}}(t)\,dt
                          -\tau_z(x)C_{f_{z,j}}(\tau_z(x))\right),
 \tag{14}
$$

where $C_g(t)=\int g(v)g(v+t)\,dv$. This follows directly by rescaling, with $Q_N-Q_{N,U}$ contributing the terminal square after $(U-\log j)_+$. In particular if $j>e^U$ the terminal square starts at zero and the $J_{N,U}$ term is absent, so there is no unjustified positive cutoff for such $j$.

For $j>e^{U/2}$ first use (5) for the square terms and individual autocorrelation and its $L^1$ bound $\|f_{z,j}\|_1^2$ for the integrated autocorrelation. The total of (14) on this range after weighting (6) is $O((1+\ell)e^{-U/4})=o(1)$. For $j\le e^{U/2}$ the effective terminal cutoff is at least $U/(2\ell)$, bounded away from zero. Then (5), (7) bound that square by $O(1)$ through $\int_{\upsilon_{z,j}}^\infty |f|^2\le \sup_{v\ge\upsilon_{z,j}}|f(v)|\,\|f\|_1$. Uniformly on $V$, $\tau_z(x)\to\tau>0$, so (7) and support on the nonnegative half-line also bound $C_{f_{z,j}}(\tau_z(x))$ by $O(1)$ using the uniform supremum of its second factor. The other terms are bounded by (5). Hence (6) allows us to pass first through any finite collection of $j$ and then take the tail beyond that collection, uniformly in $x$.

For fixed $j$, $\upsilon_{z,j}\to\upsilon>0$ and the terminal square converges by (10), which gives $L^2$ convergence on any half-line bounded away from zero, plus absolute continuity of the limiting square integral on that half-line. The cumulative term converges by $L^1$. The autocorrelations converge in $L^1(dt)$ by Young's inequality for convolution with the reflected first factor, and (10). This justifies the shift integral including the moving endpoints. For the single positive shift, split the $v$ integral into $0<v<\epsilon$ and $v\ge\epsilon$. The first part is uniformly small in the limit, by the near-zero $L^1$ bound above and (7) on the shifted factor. On the second part use $L^2$ convergence on a half-line bounded away from zero for both factors and translation continuity in $L^2$ on the same restricted profiles, uniformly for shifts tending to $\tau$. This proves convergence at the moving positive shift, without needing convergence at zero shift. The limit is independent of $j$. The sum of the $c_{N,j}$ is exactly one, so the limit in (14) is the bracket in (4). Inserting it into the conditional pointwise parity formula, with its factor $\Sigma(N)/(2\log x)$ and exact bounded weight, gives (3). Nothing in this limiting calculation discards a term of the genuine Fourier coefficients.

## 4. What changes at one-half density

For $s>0$, differentiating (11) gives $-\mathcal L_d'(s)=d\mathcal L_d(s)(1-e^{-s})/s$. Laplace uniqueness implies
$v f_d(v)=d\int_{\max(0,v-1)}^v f_d(t)\,dt$ almost everywhere. This uses finite first moment, which follows either by monotone convergence as $s\downarrow0$ (the mean is $d$), or the uniform first-moment bound above. Therefore on $0<v<1$, $F_d'=dF_d/v$, so $f_d(v)=b_d v^{d-1}$ for a constant $b_d\ge0$. This constant is strictly positive: splitting the integral in (11) at $v=1/s$ shows that $s^d\mathcal L_d(s)$ tends to a positive finite constant, and the part of the Laplace integral with $v\ge1$ is $O(e^{-s})$. Indeed

$$
 b_d=\frac1{\Gamma(d)}
   \exp\!\left(d\int_0^1\frac{e^{-u}-1}{u}\,du
                +d\int_1^\infty\frac{e^{-u}}{u}\,du\right)>0 .
 \tag{15}
$$

Thus global square integrability fails exactly at the origin for $d\le1/2$, but $f_d$ is square-integrable on any positive terminal half-line by the weighted bounds. For fixed positive $\tau$, the shift terms in (4) are finite and independent of $\upsilon$, and the cumulative term is bounded. Consequently, as one varies fixed cuts to $\upsilon\downarrow0$, the exact leading constants in the original majors satisfy

$$
 \mathcal K_{\pm,d}(\tau,\upsilon)=
 \begin{cases}
 \displaystyle\frac{\tau b_d^2}{2(1-2d)}\upsilon^{\,2d-1}
                   +O_{\tau,d}(1), &0<d<1/2,\\[2mm]
 \displaystyle\frac{\tau b_d^2}{2}\log(1/\upsilon)
                   +O_{\tau,d}(1), &d=1/2 .
 \end{cases}
 \tag{16}
$$

For example a single reduced class modulo $3$ has $d=1/2$, and a single reduced class modulo $5$ has $d=1/4$. One may first choose $B$ within the admissible range, and then choose $B_0<B$ sufficiently close so that the fixed scaled gap $\upsilon=(B-B_0)/\vartheta$ is small. This illustrates why the compact positive cutoff in the original hard formula, rather than replacing it by zero, is necessary in lower-density radical families. It asserts no smallness of the original minor on these targets.
