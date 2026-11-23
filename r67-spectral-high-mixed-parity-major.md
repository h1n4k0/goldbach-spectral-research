# The high mixed strip major term separates the two genuine squarefree parities

**Scope.** We calculate the pointwise major-arc contribution of the actual above-BV mixed strip after splitting the squarefree partners by total Möbius sign. The new input is an exact major density for its parity twist. On the individual even moduli $N=2^v$ (and more generally any fixed even radical), the even squarefree parity carries a nonzero natural-scale major term and the odd parity has zero leading major term, even after the previously deleted largest-prime portions are removed. This is about actual major coefficients, not a signed minor lower bound, a prime representation result, or Hypothesis S.

Let $N$ be sufficiently large and even, $L=\log N$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, fixed $B>B_0>0$ as in the [below-level calculation](r65-spectral-bv-visible-strip-minor.md), and $V=[N/3,2N]$. Use the exact arcs $\mathfrak M$ of denominator $q\le Q=N^{1/1000}$ and width $2Q/N$ of the [pointwise bridge](r64-spectral-pointwise-major-central-bridge.md), with $e(t)=e^{2\pi it}$. For a real half-open $I\subset(N/2,9/16\,N]$ and left weight $\omega$ of uniformly bounded supremum and variation, let $P_{I,\omega}(\theta)=\sum_{n\in I}\lambda(n)\omega(n)e(n\theta)$, where $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$. For a right sequence $A$ put $\widehat A(\theta)=\sum_m A(m)e(m\theta)$ and

$$
 \mathfrak M_N(A;I,\omega)=
       \int_{\mathfrak M}P_{I,\omega}(\theta)\widehat A(\theta)
                                            e(-N\theta)d\theta.
$$

All right sequences below are zero outside squarefree $m\in V$. Use the [exact mixed remainder](r66-spectral-above-bv-strip-deletions.md): $M_>(m)$ sums over the mutually coprime four factors $abcd=m$, $h=abc>H_0$, $D<\min(ab,ac)<\sqrt m$, with weight $\mu(b)\mu(c)(1-2\log(ac)/\log m)$, before the overall minus in the decomposition. Let $M_\le$ have $h\le H_0$. The exact global prime marginal removes itself, so

$$
                     M_>(m)+M_\le(m)=-\Xi_D(m).
                                                                  \tag{1}
$$

Define the actual parity selectors $M_\pm=\tfrac12(1\pm\mu(m))M_>$ on squarefree partners. This is even prime-factor count for $+$ and odd count for $-$.

Use the notation $\alpha_p,P_N,R_{N,j},Q_N=\mathcal Q_N$ from the [full squarefree CRT model](r63-spectral-full-squarefree-crt-strip.md): $\alpha_p=(p-1)/(p^2-2)$ when $p\nmid N$ and zero otherwise, $P_N\asymp(\varphi(N)/N)^2$, and
$R_{N,j}(u)=\sum_{a\le e^u,\ (a,j)=1}\mu(a)\alpha(a)$ for $u\ge0$, extended by zero for $u<0$. Here $\alpha$ is multiplicative on squarefree integers. Define for real $t$

$$
 C_N(t)=\sum_{j\ {\rm sf}}\mu(j)\alpha(j)^2
              \int_{\mathbb R}R_{N,j}(u)R_{N,j}(u+t)\,du .
                                                                  \tag{2}
$$

This is even and continuous, with $C_N(0)=Q_N$. The convergences needed below follow from the $L^1$ and $L^2$ bounds of that proof, namely $\|R_{N,j}\|_1+\|R_{N,j}\|_2\ll Nj/\varphi(Nj)$, and $\sum_{j}\alpha(j)^2(j/\varphi(j))^2<\infty$. Let $U=\log(H_0/D)=(B-B_0)\log L$ and denote the finite moments of the below-level proof by

$$
 Q_{N,U}=\sum_{j\le e^U}\mu(j)\alpha(j)^2
          \int_0^{U-\log j}R_{N,j}(u)^2du,\qquad
 J_{N,U}=\sum_{j\le e^U}\mu(j)\alpha(j)^2
            \left(\int_0^{U-\log j}R_{N,j}(u)\,du\right)^2 .
$$

Finally $T(x)=2\bigl(\frac12\log x-\log D\bigr)>0$ on $V$.

**Pointwise major formula.** Assume the historical global Dirichlet GRH inputs for primes and masked Möbius on the present polynomial-denominator major arcs, as in the pointwise bridge. The presence of masked Möbius here differs from the prior upper bounds that needed prime AP input alone. Uniformly on every $N$ and every $I,\omega$ above, for either sign,

$$
 \begin{split}
 \mathfrak M_N(M_\pm;I,\omega)
  ={}&\frac{\Sigma(N)P_N}{2}\int_I\frac{\omega(u)}{\log x}
   \left\{T(x)(Q_N-Q_{N,U})+J_{N,U}\right.\\
  &\left.\hspace{29mm}
        \pm\left(\int_{-T(x)}^{T(x)}C_N(t)\,dt-T(x)C_N(T(x))\right)
   \right\}du +O_{A,B,B_0}(NL^{-A}),
            \qquad x=N-u ,
 \end{split}                                                       \tag{3}
$$

for every fixed $A>0$. There is no average over the target modulus. We first establish the new twisted term, then use the existing untwisted density to complete the comparison.

## 1. The actual twisted arithmetic at polynomial-denominator majors

On the squarefree support, multiplication of the genuine strip coefficient by $\mu(m)$ turns its sign from $\mu(b)\mu(c)$ into $\mu(a)\mu(d)$, exactly. The same is true for its two mixed pieces before subtraction. By symmetry in $b,c$, replace the centered factor by $\log(d/a)/\log m$ in either twisted sum. We compute the density of $\mu(m)\Xi_D(m)$ and show that $\mu(m)M_\le(m)$ has no major main term.

The two disjoint sectors $a>N^{.1}$, and $d>N^{.1}$ with $a\le N^{.1}$, are bounded to a fixed power saving on each right major polynomial. Fix the other three factors and apply the [pointwise masked Möbius GRH input](r64-spectral-pointwise-major-central-bridge.md#1-the-pointwise-transfer) in every residue class of the signed variable. For the original strip the gate is $D<a\max(b,c)<\sqrt{abcd}$; for the low mixed term it is $D<a\min(b,c)<\sqrt{abcd}$ together with $abc\le H_0$. In either case all the conditions are interval constraints on the chosen signed variable when the others are fixed. Its coprimality to the three fixed factors is exact, and the centered weight is bounded and monotone as a function of $a$ or $d$. The phase $e(\eta abcd)$ gives variation $O(Q)$ on $V$. Summing $q$ residue errors and the triple reciprocal sums, as in the bridge, costs $O_\epsilon(N^{1-.05+\epsilon}Q^2L^3)$, with no unproved Möbius estimate on the minor arcs.

In the remaining bulk $a,d\le N^{.1}$, the low mixed term has no support: $h=x/d>N^{.9}/3>H_0$. For the original strip bulk, both positive variables $b,c$ are at least $N^{.39}$ on the actual support, because $a\max(b,c)<\sqrt x$ implies $\min(b,c)>\sqrt x/d$. Hence they can be counted by the two-variable squarefree procedure of the earlier CRT proof, now with $(b,c)$ the positive variables and $(a,d)$ fixed:
* At a fixed positive $b$, the conditions on $c$ are the union of at most two intervals, by splitting which of $b,c$ is larger. The exact squarefree CRT count in any residue has error $\tau(abd)\sqrt{N/(abd)}$ and preserves coprimality to all fixed factors. Fixed log factors and the slow phase put this through bounded variation.
* At fixed real $x=abcd$, the remaining interval conditions on $b$ are again at most two intervals, and $b\ge N^{.39}$. The $b$ harmonic count with the exact local multiplicative factors follows from the convolution $g=1*k$ of the squarefree CRT proof: its moment error at exponent $3/4$ is $O_\epsilon(q^3(ad)^\epsilon)$ and the fixed prefactor is $O(q^2)$. This gives a power saving at $q\le Q$ by partial summation.

These are the identical local factors after renaming the two positive variables. In particular, at a prime dividing $ad$ their uncompleted local density is $(1-1/p)^2$, and otherwise it is $(1-1/p)^2(1+2/p)$ off $q$, or $(1-1/p)^2(-1/(p-1)+2/p)$ on $q$. The left prime factor $\mu(q)c_q(N)/\varphi(q)$ thus completes the positive harmonic factor, including the reciprocal $1/(ad)$ from changing variables, to

$$
                  \Sigma(N)P_N\,\alpha(a)\alpha(d)
                                                                  \tag{4}
$$

when $(a,d)=1$ and both are squarefree. Nonunits on the right were kept, and disappear through the completed factors. To verify that no averaged Ramanujan error is being used, the profiles in $x$ below have supremum and variation $O(1+\log L)$ for each $a,d$. As in the earlier occupancy proof, each prime of squarefree $q$ either forces one of $a,d$ to occupy it, gaining a reciprocal factor $1/p$, or gains $O(1/p)$ in the two positive-variable local factor. Thus the right densities in sup/variation have bound $O(L^3 C^{\omega(q)}/q)$. The same pointwise rational-tail argument works: weighting by $q^{1/4}$ and using $|c_q(N)|\le(q,N)$ bounds the tail by $Q^{-1/4}N^\epsilon$, up to fixed log powers. The Fourier tails after real extension and the two progression error budgets also save a fixed power in the integrated majors, exactly as in the bridge. These checks show that all major densities just described hold on each $N$ and exact hard interval. In particular the twisted low mixed major is $O(N^{1-10^{-4}})$.

It remains to compute the real two-positive-factor integral in the twisted strip. Fix $a,d$, put $x=abcd$, and first use $b\le c$. Then $c\ge\sqrt{x/(ad)}$, $D/a<c<\sqrt x/a$. Its allowed logarithmic width is zero unless $\log(d/a)>0$, and otherwise

$$
 \min\bigl(\tfrac12\log(d/a),\,\tfrac12\log x-\log D\bigr).
$$

The other order of $b,c$ has the same harmonic width and joint local density; the equal line has zero integration measure (and is impossible on the actual coprime bulk). The symmetrized centered weight is constant $\log(d/a)/\log x$. Multiplication by the two widths leaves the profile

$$
     \frac{(\log(d/a))_+\min(T(x),(\log(d/a))_+)}{\log x}.
                                                                  \tag{5}
$$

For fixed $a,d\le N^{.1}$ its size and variation in $x$ have the stated $O(1+\log L)$ bounds, since $T(x)=O(\log L)$, $\log x\asymp L$, and the cap is monotone with at most one transition. Combining (4)–(5) and then averaging the two orders of $a,d$, the actual completed density of the twisted strip is
$\Sigma(N)P_N/(2\log x)$ times the signed finite sum on coprime squarefree $a,d\le N^{.1}$ of the kernel $g_T(\log d-\log a)$, weighted by $\mu(a)\mu(d)\alpha(a)\alpha(d)$, where $g_T(t)=|t|\min(T,|t|)$.

## 2. Convert the signed cap to an autocorrelation

Expand $(a,d)=1$ by $j\mid(a,d)$ and divide both variables by $j$. The sign and weight outside are $\mu(j)\alpha(j)^2$ and the common log shift does not affect the kernel. For fixed $j$ the two signed arrays now have primitive $R_{N,j}$ at upper limit $U_j=L/10-\log j$. For $j\le e^{L/20}$ this limit is at least $L/20$. The [masked reciprocal Mertens bound](r63-spectral-full-squarefree-crt-strip.md) gives uniformly
$|R_{N,j}(U_j)|+\|R_{N,j}\mathbf1_{u>U_j}\|_1+\|R_{N,j}\mathbf1_{u>U_j}\|_2\ll_A L^{-A}$ for every fixed $A$. Indeed its Euler kernel has total mass $O(Nj/\varphi(Nj))$ and a quarter-power moment $O_\epsilon((Nj)^\epsilon)$, and one splits at a log shift $u/2$. The tail $j>e^{L/20}$ in the finite sums is negligible by $\alpha(j)^2\le j^{-2}$ and the trivial reciprocal harmonic and logarithmic weight bounds. It is equally negligible in the completed integrals by the displayed primitive norm bound.

For a finite signed array truncated at $U_j$, subtract its total mass at the endpoint $U_j$. This changes its quadratic kernel sum by at most that mass times a fixed power of $L$: its truncated absolute mass is $O(1+L)$ and $g_T$ is at most a fixed power of $L$ on this range. The new array has total zero and primitive $R_{N,j}(u)\mathbf1_{[0,U_j)}(u)$ almost everywhere. For a compactly supported zero-total signed array $\nu$ with primitive $F$, integration by parts twice gives

$$
 \iint g_T(y-z)\nu(dy)\nu(dz)
       =-\iint F(y)F(z)g_T''(y-z)\,dy\,dz ,
 \qquad
 g_T''(t)=2\mathbf1_{|t|<T}-T(\delta_T+\delta_{-T}).
                                                                  \tag{6}
$$

One can smooth $g_T$ and pass to the limit: the autocorrelation of compactly supported $F\in L^2$ is continuous by continuity of translations, and the second derivative is a finite measure on any bounded interval. The boundary terms vanish by the zero total. The formula for the second derivative follows from the derivative drop from $2T$ to $T$ on the positive cap boundary and its reflected drop on the negative one. The clipped primitive can be replaced by the full $R_{N,j}$ with the required arbitrary log saving by the stated tail estimates and Cauchy. This avoids using any infinite total-variation assumption for the original signed array.

The half from averaging the orders in (5) leaves the twisted strip density

$$
       \frac{\Sigma(N)P_N}{\log x}
          \left(-\int_{-T(x)}^{T(x)} C_N(t)\,dt
                              +T(x) C_N(T(x))\right) .
                                                                  \tag{7}
$$

This sign can also be checked with $g_T(t)=t^2$ on the whole support of a finite array: the expression in parentheses then is minus the square of the integrated primitive. By (1), and the negligible twisted low mixed major, the **negative** of (7) is the twisted high mixed density. The untwisted full mixed is $-\Xi_D$ with density $\Sigma(N)P_N T(x)Q_N/\log x$. The untwisted low mixed has density $\Sigma(N)P_N(T(x)Q_{N,U}-J_{N,U})/\log x$: this is the low union overlap term in the [exact below-level density](r65-spectral-bv-visible-strip-minor.md), excluding its separate prime marginal. Subtract the latter from the former and average with plus or minus the twisted density. This proves (3), including the factor one-half.

## 3. A natural-scale effect on the actual even-parity residual for fixed radical

On $N=2^v$ with $v\to\infty$, or any sequence with fixed even radical $R_0$, the arrays $\alpha,R_{N,j}$ and the constants $Q_N,\Sigma(N),P_N$ depend only on that fixed set of prime divisors. Write them without the $N$ subscript where unambiguous. Then

$$
 J_\infty=\sum_j\mu(j)\alpha(j)^2
                   \left(\int_0^\infty R_j(u)\,du\right)^2>0 .
                                                                  \tag{8}
$$

Indeed the ordinary reciprocal Mertens primitive has integral $1$, by its Laplace transform $1/(s\zeta(1+s))$ at $s\downarrow0$ and its unconditional integrability. The replacement kernel from its coefficients $1/p$ to $\alpha_p$ has total
$m_\alpha=\prod_p(1-\alpha_p)/(1-1/p)>0$, a finite positive number (the inactive set is fixed and all other deviations are $O(p^{-2})$). Excluding a finite $j$ adds the factor $\prod_{p\mid j}(1-\alpha_p)^{-1}$. Thus (8) equals
$m_\alpha^2\prod_{p\nmid N}(1-(\alpha_p/(1-\alpha_p))^2)>0$.
The series and product converge absolutely in the needed weighted sense. In fact $P_N J_\infty=1$ exactly: the local factor of $J_\infty$ is $(1-2\alpha_p)/(1-1/p)^2$, and $(1-2\alpha_p)(1+2r_p/p)=1$ by $\alpha_p=r_p/(p+2r_p)$, including inactive primes.

In this fixed-prime-set family the convergence statements are strong enough even when multiplied by $T(x)\asymp\log L$:
$Q_{N,U}=Q_N+O(e^{-c\sqrt U})$, $J_{N,U}=J_\infty+O(e^{-c\sqrt U})$, and
$\int_{-T}^T C_N(t)dt=J_\infty+O(e^{-c\sqrt T})$, $C_N(T)=O(e^{-c\sqrt T})$.
For the first two, split $j\le e^{U/2}$ and its complement, then apply the reciprocal Mertens tail at $U-\log j\ge U/2$ on the former, now with mask $R_0j$ only, and use the $j^{-2}$ tails on the latter. For the autocorrelation, Cauchy bounds $C_j(T)$ by $\|R_j\|_2\|R_j\mathbf1_{u\ge T}\|_2$; the integral absolute tail is bounded by twice $\|R_j\|_1\|R_j\mathbf1_{u\ge T}\|_1$. Split $j$ at $e^{T/2}$ and apply the same fixed-prime-set tail bound. The total integral of the autocorrelation is the square of the signed integral, giving (8). These checks justify all convergence here without a density-one assertion on the sparse sequence $2^v$.

Consequently the completed major **density** of the even $M_+$ on these moduli is
$(\Sigma(N)/\log x)(1+o(1))$ uniformly on $V$, while the odd $M_-$ has density $o(\Sigma(N)/L)$. These also hold after imposing $P^+(m)\le \sqrt N\exp(-L^\gamma)$ on the even residual for any fixed $\gamma<2/3$, or on the odd residual for any fixed $\gamma<1$. In fact the corresponding complementary largest-prime components have major bounds $o(\Sigma(N)/L)$ in the [actual integrated-energy deletion](r66-spectral-integrated-short-cutoff.md), Sections 2–4, and parity selectors are constant in its extracted prime at fixed cofactor. The exact reflection deletion in the above-BV proof likewise respects both parities and any largest-prime selector, since it leaves $m$ fixed.

For instance, on any original cell of length $N/(16\lceil L^J\rceil)$ for fixed $J$ at weight $1$, the surviving even-parity genuine mixed **major coefficient** is asymptotic to $\Sigma(N)|I|/L$ on $N=2^v$ or fixed even radical, and the odd is $o(\Sigma(N)|I|/L)$. The arbitrary fixed log saving in (3) absorbs the integrated power errors for these cell lengths. Neither sign could be inferred just from the corresponding untwisted total. This locates a natural-scale contribution on major arcs in the actual unresolved parity and largest-prime regime, not on the minor arcs: those could offset the computed baseline or be small, and this proof decides neither.
