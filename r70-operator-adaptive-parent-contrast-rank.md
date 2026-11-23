# Adaptive parent contrasts reduce the actual exterior mean rank

**Scope.** This proves a full all-alias estimate after projecting the genuine exterior mean directions onto larger, true weighted-zero contrasts. It controls the principal residue-orbit component of these contrasts, with the original continuous benchmark and all three signs. A positive trace lift removes their crossings with every other direction, including the whole Hardy space outside the tested annulus. The new parent means themselves remain unestimated; no prescribed-modulus variance or weak-S result is claimed.

## Statement

Use the setting and exact physical unitary realization of [R60](r60-operator-localized-coarse-contrast-annulus.md). Let $\mathcal A\subset[Q,2Q]$ contain $J\ge1$ distinct even integers, with the original local GRH at each. On a reference dyad starting at $V$ contained in $[H,M]$, with $4\le H<M\le Q^\Gamma$ and fixed $0<\Gamma<1$, take a disjoint partition of its intervals into parents of lengths at most $W_V$, where $1\le W_V\le V/20$. As usual a final interval can be shorter. Transport a parent $I$ by $I_N=(Q/N)I$, and let $R_{N,V}$ be the orthogonal projection onto all vectors supported on these parents with the constraint $\int_{I_N}r_N(u)f(u)\,du=0$ in each, where $r_N$ is the exact weight of R60 (1). Let $R_N=\sum_V R_{N,V}$. Assume auxiliary Dirichlet GRH for each integer $q\le\lceil20\sqrt{Q\max_V W_V}\rceil$, including $q=1$. Write $L=\log(3Q)$.

For two such dyads $V,U$, suppose their parent lengths are bounded by a common $W\le\min(V,U)/20$. Then

$$
\left(\frac1J\sum_{N\in\mathcal A}\|R_{N,V}T_N R_{N,U}\|_{\rm HS}^2\right)^{1/2}
     \ll_{\Gamma,\epsilon} Q^\epsilon\frac{W}{\sqrt{VU}}
                 \left[\sqrt{\frac WJ}(QW)^{1/4}
                                  +\sqrt{\frac WQ}\right],
 \tag{1}
$$

using auxiliary GRH through $\lceil20\sqrt{QW}\rceil$. In particular put $U=V,\ W=W_V$, and denote the right-hand side of (1) by $A_V^{\rm rms}$ (including its implicit constant). The full deletion, not just the compression, satisfies

$$
\left(\frac1J\sum_{N\in\mathcal A}
       \|T_N-(1-R_N)T_N(1-R_N)\|_{\rm HS}^4\right)^{1/4}
 \ll_{\Gamma,\kappa,\epsilon} Q^\epsilon
        \sum_V \left[(A_V^{\rm rms})^{1/2}
                       +(W_V/V)^{1/4}+V^{-\kappa/2}\right],
 \tag{2}
$$

for any fixed $0<\kappa<1/3$. The appearances of $Q^\epsilon$ absorb logarithms and the choice of smaller powers in intermediate estimates.

In the reference example

$$
H=Q^{2/5},\qquad M=Q^{3/5},\qquad D=Q^{8/25},\qquad
 W_V=Q^{23/175} V^{4/7},
 \tag{3}
$$

choose each parent to be a union of consecutive original length-$D$ mesowindows within its dyad. For all large $Q$ these widths are allowed. At $J\gg Q^{99/100}$, each diagonal contrast square in (1) has RMS $O_\epsilon(Q^{-3/200+\epsilon})$, and the full deletion in (2) has fourth-root fourth mean $O_\epsilon(Q^{-3/400+\epsilon})$. The auxiliary range is through $\lceil20Q^{129/175}\rceil$. Without a lower bound on $J$, there are $O_\epsilon(Q^{97/100+\epsilon})$ exceptions among the selected moduli at threshold $Q^{-1/500}$ for the full deletion. On the surviving annular **literal** mean space from the original length-$D$ windows, the operator can therefore be replaced, with that same error, by its compression to $O(Q^{22/175})$ parent mean directions, versus the earlier dimension $O(Q^{7/25})$. This replacement does not shrink the complement outside the annulus.

## 1. Exact support and the grand test norm

Write $p=N/Q$ and $z=pu$. The exact two-sided pullback in R60 §1 maps a true test $f$ on $I_N$ to

$$
g(z)=p^{-2}\frac{r_N(z/p)}{r_Q(z)}f(z/p),
 \tag{4}
$$

on $I$, with bounded operator norm on the whole annulus. Here $r_Q$ is the explicit same weight with parameter $Q$, not an arithmetic modulus. The map carries the true constraint to $\int_I r_Qg=0$, since the latter equals $p^{-1}\int_{I_N}r_N f$. It preserves the original raw Volterra profile exactly, including the prefactor, by $p^{-2}/Q=1/(Np)$. Thus it suffices, by the HS ideal property, to estimate the fixed spaces $\mathcal H_I$ of this weighted-zero condition using fixed raw profiles in the two dyads. One can first use arbitrary finite real orthonormal families in each $\mathcal H_I$.

For $f_i$ in such a family the fixed profile is

$$
h_{I,i}(x)=\frac{\sqrt{2\pi x}}Q
             \int_{z\in I,\ z\ge x/Q} r_Q(z)f_i(z)\,dz.
 \tag{5}
$$

It is supported on $QI$, continuous with zero endpoints and absolutely continuous there. Below $QI$ it vanishes by the exact weighted-zero condition. Put $a=QV,\ X=QW$. On these dyads $r_Q(z)\ll_\Gamma V^{-3/2}$. If $X_I=Q|I|\le X$, Bessel shows that the profile vector $h_I(x)=(h_{I,i}(x))_i$ has pointwise norm $O(b_I)$ with $b_I=\sqrt{X_I}/a$. For every unit scalar combination of the $f_i$, the resulting profile also has total variation $O(b_I)$ by Cauchy in (5) after differentiation. Since the $QI$ are disjoint and their total length is $O(a)$,

$$
\sum_I b_I^2\ll a^{-1},\qquad
     \sum_{I,i}|h_{I,i}(x)|^2\ll X/a^2 .
 \tag{6}
$$

All assertions include clipped final windows. For the $U$-dyad use the identical notation with $a'=QU$.

## 2. Grand residue error savings from subtracting local constants

For $q$ in the auxiliary range let $\mathbf F(x)=(\psi(x;q,r)-x/\phi(q))_r$ on units, zero on nonunits, as in R60. Use the finite-height Selberg estimate of [R59](r59-operator-balanced-arcs-cuberoot-prefix.md), namely its residue-vector integral estimate as stated in R60 (7). It implies on a bounded dyadic enlargement of $[a,2a]$

$$
\int\|\mathbf F(x+h)-\mathbf F(x)\|_2^2\,dx
                        \ll_\Gamma a h L^4,\qquad 0<h\le X.
 \tag{7}
$$

For $h\ge1$, cover the enlarged range by a bounded number of dyads. For $h<1$, each slide can see at most one prime-power atom, each atom is seen for length at most $h$, and the squared drift costs $O(ah^2)$. This gives (7) there also. Negative shifts are treated by translation. We only use ranges of $x$ and $x+h$ comparable to $a$, since $X\le a/20$.

For each $QI$ with left endpoint $l_I$ choose $\mathbf m_I=X^{-1}\int_{l_I}^{l_I+X}\mathbf F(y)\,dy$. Jensen applied on $x\in QI$ gives

$$
\sum_I\int_{QI}\|\mathbf F(x)-\mathbf m_I\|_2^2dx
  \ll \frac1X\int_{-X}^X\int_{a-X}^{2a+X}
                   \|\mathbf F(x+h)-\mathbf F(x)\|_2^2dx\,dh
  \ll_\Gamma a X L^4 .
 \tag{8}
$$

For the first inequality $y\in[l_I,l_I+X]$ implies $|y-x|\le X$, and the $x$-intervals $QI$ are disjoint. No bound on overlap of the $y$-intervals is needed.

Let $\nu_{I,i,r}=h_{I,i}\,dF_r$ and $e(t)=\exp(2\pi it)$. Fourier partial integration subtracts $\mathbf m_I$ exactly since each $h_{I,i}$ vanishes at endpoints. For the terminal term in the derivative use

$$
h_{I,i}'(x)=\frac{h_{I,i}(x)}{2x}
       -\frac{\sqrt{2\pi x}}{Q^2}\,r_Q(x/Q)f_i(x/Q)
       \qquad (x\in QI).
 \tag{9}
$$

Bessel after $z=x/Q$, then (8), bounds the terminal part's squared norm over all $I,i,r$ by

$$
\ll a^{-2}\sum_I\int_{QI}
                     \|\mathbf F(x)-\mathbf m_I\|_2^2dx
       \ll_\Gamma (X/a)L^4 .
$$

Indeed the Bessel coefficient squared in $dz$ is $O((QV)/Q^2\cdot V^{-3})$, giving $O(a^{-2})$ with $dx$. For the bulk and the derivative of $e(\beta x)$, Cauchy over each $QI$ gives the same bound times $(1+|\beta|X)^2$: the factor is at most $X(X/a^2)(a^{-1}+|\beta|)^2\ll a^{-2}(1+|\beta|X)^2$. Consequently

$$
\sum_{I,i,r}|\widehat\nu_{I,i,r}(\beta)|^2
               \ll_\Gamma (X/a)(1+|\beta|X)^2 L^4.
 \tag{10}
$$

The joint Bessel estimate in (8)–(10) gives $X/a=W/V$ for the entire dyad, not separately for each parent.

For the corresponding grand short-increment estimate take $2\le \ell\le X$. Use

$$
\int_{(s,s+\ell]} h\,dF_r
  =h(s+\ell)[F_r(s+\ell)-F_r(s)]
                  -\int_s^{s+\ell}h'(x)[F_r(x)-F_r(s)]dx.
 \tag{11}
$$

No boundary jumps arise after extending by zero, even when the slide is not contained in $QI$. From (6), (7), the grand squared integral of the first term is $O((X/a)\ell L^4)$. Use Minkowski for the $h/(2x)$ term: its squared size is at most $O((X/a^4)a\ell^3 L^4)$ by integrating the square-root residue lag bound $\sqrt{a u}L^2$ for $u=x-s\in[0,\ell]$ and the envelope in (6). This is at most $O((X/a)\ell L^4)$, since $\ell\le X\le a$. For the terminal derivative term, Bessel in (9) applied with the indicator of $(s,s+\ell]$ gives at each $s$ a bound by $O(a^{-2})$ times the squared residue integral over $\bigcup QI\cap(s,s+\ell]$, with $F_r(x)-F_r(s)$ inside. Integrating in $s$ and using (7) yields $O((\ell^2/a)L^4)$, again at most $O((X/a)\ell L^4)$. We have proved

$$
\int_{\mathbb R}\sum_{I,i,r}|\nu_{I,i,r}((s,s+\ell])|^2ds
             \ll_\Gamma (X/a)\ell L^4 .
 \tag{12}
$$

By convolution with a length-$\ell$ indicator and Plancherel, its Fourier consequence on $|\beta|\le1/(4\ell)$ is $O((X/a)L^4/\ell)$. This estimate for the grand vector does not require an assumption on the number or individual lengths of its parent windows.

## 3. Balanced arcs and all original aliases

Define the grand vectors of prime sums and continuum transforms as $A_V(\alpha)_{I,i}=\sum_n\Lambda(n)h_{I,i}(n)e(n\alpha)$ and $B_V(\beta)_{I,i}=\int h_{I,i}(x)e(\beta x)dx$. From (6), total support length $O(a)$, the trivial $\Lambda$ bound, and the variation bound,

$$
\|A_V\|_{L^2(\mathbb T;\ell^2)}\ll L\sqrt{X/a},\qquad
 \|B_V(\beta)\|_2\ll a^{-1/2}\min(X,|\beta|^{-1}).
 \tag{13}
$$

On the balanced arcs of R59, $P=\lfloor\sqrt X/10\rfloor$, $\delta_q=2P/(qX)$, use the usual decomposition $A_V=\mu(q)B_V/\phi(q)+E_V+Z_V$ at $c/q+\beta$. The last term is the $q$-nonunit prime-power term. Equation (10), by Cauchy over the residues, gives

$$
\|E_V(c/q+\beta)\|_2
           \ll \sqrt{X/a}\sqrt q\,(1+|\beta|X)L^2.
 \tag{14}
$$

Also $\|Z_V\|_2\ll L^2/\sqrt a$, using bounded total weights of powers supported on primes dividing $q$, and (6). Off the arcs choose a Dirichlet approximation with $P<q\le\lceil20\sqrt X\rceil$, $|\beta|X\le1$. Equations (13)–(14) give a grand minor supremum $O_\epsilon(Q^\epsilon\sqrt{X/a}X^{1/4})$. Using the other leg's first bound of (13), the minor tensor has $L^2(\mathbb T;{\rm HS})$ norm $O_\epsilon(Q^\epsilon X^{1/4}X/\sqrt{aa'})$.

On the majors use $\ell=qX/(8P)$ in (12) and finite additive Parseval in $c$: the integrated square for one error over the $q$-arcs is $O((X/a)L^4 P/X)$. Combine with the other error's square supremum in (14) and $\sum_{q\le P}q(1+P/q)^2\ll P^2\log(2P)$. The double error has the same $L^2({\rm HS})$ norm as the minors, up to $Q^\epsilon$. For the single errors, use additive Parseval, (10), and $(1+|\beta|X)\|B_U(\beta)\|_2\ll X/\sqrt{a'}$. The squared norm on the majors is bounded by

$$
\ll L^4(X/a)(X^2/a')\sum_{q\le P}q\phi(q)^{-2}\delta_q
          \ll L^4 \frac{X^2}{aa'} P,
 \tag{15}
$$

since $\sum_q\phi(q)^{-2}<\infty$. This suffices for the same norm bound. The same statements hold with either Fourier argument reversed by the reflection symmetry.

For each entry belonging to parents $I,I'$, and each orientation, the actual alias and the continuum line both vanish unless $s=kN$ lies in the affine sum or difference of $QI,QI'$. This interval has length at most $2X$; the number of retained $k\ge1$ is $O(W)$ per entry, though their positions need not coincide between entries. Cauchy on $k$ **within each entry**, and then divisor multiplicity for positive $s\ll QM$, give for the fixed coefficient tensor

$$
\sum_{N\in\mathcal A}
      \left\|\sum_{\text{entrywise allowed }k}c_{kN}\right\|_{\rm HS}^2
     \ll_\epsilon WQ^\epsilon\sum_s\|c_s\|_{\rm HS}^2 .
 \tag{16}
$$

All Fourier coefficients here are fixed in $N$ by (4). Thus the minor and the three major error products give the first term in (1). This estimates the **sum of all true aliases** inside the contrast matrix, not separately estimating narrow alias bands of a mean matrix.

We record the pointwise errors to match the exact continuum and units. For terms involving $Z_V$ or $Z_U$ on the major arcs, the per-entry sum is bounded by $O(W)$ times its $L^1$ Fourier tensor bound. Take HS and Minkowski over entries, then use $\|Z_V\|_2\ll L^2/\sqrt a$, (13) and the two-leg $Z$ term as in [R66](r66-operator-dense-top-sum-edge.md) §4. This gives $O(L^{O(1)}(W/\sqrt{VU})\sqrt{W/Q})$. For dropping $N$-nonunits from the intermediate prime sum, each nonunit atom on one leg has at most one partner per line. Using the total nonunit prime-power weight $O(L^2)$, the per-parent norm $b_I$, and then (6), the pointwise cost is $O(L^{O(1)}W/(Q\sqrt{VU}))$. This restores exactly the original unit condition without deleting admissible proper powers.

For the pure principal term use the individual decay $O(b_I\min(X,|\beta|^{-1}))$ on each parent. The full continuum coefficient for a parent pair has norm $O(b_Ib_{I'}X)$, and the omitted $\beta$-tail at denominator $q\le P$ has norm $O(b_Ib_{I'}/\delta_q)=O(b_Ib_{I'}qX/P)$. The absolute Ramanujan bounds of R66 (14) extend the integrals and the series at cost $O_\epsilon(Q^\epsilon b_Ib_{I'}X/P)$ per line. Aggregate using $O(W)$ lines per parent pair and (6); the total pointwise cost is $O_\epsilon(Q^\epsilon W^2/(P\sqrt{VU}))$, which is the second term in (1). The full model is the exact signed $\mathfrak S(kN)$ continuum affine integral by Fourier inversion, with the two positive differences and the negative sum, and the equality line excluded. Thus (1) follows, after the exact pullback and passage through finite basis truncations.

## 4. Deleting all mixed legs and coarsening the literal means

For a single dyad the deterministic proof of [R62](r62-operator-full-mixed-contrast-deletion.md) §1 applies with the local scale $V$ and parent maximum width $W_V$. It uses disjointness and the exact weighted-zero constraint, not equal parent widths. In particular

$$
\|(D_N+K_N)R_{N,V}\|_{\rm HS}
       \ll_{\Gamma,\kappa,\epsilon}
              Q^\epsilon\big(\sqrt{W_V/V}+V^{-\kappa}\big)
              =:b_V^{\rm det}.
 \tag{17}
$$

Here $D_N+K_N$ is the true diagonal plus Beta benchmark. This estimate uses local GRH only. The true positive odd-character Gram $P_N=T_N+D_N+K_N$ has full trace $O(L^2)$ under local GRH, as in R62 §2. Its positivity gives the pointwise lift

$$
\|T_NR_{N,V}\|_{\rm HS}
       \ll L\big(\|R_{N,V}T_NR_{N,V}\|_{\rm HS}+b_V^{\rm det}\big)^{1/2}
                  +b_V^{\rm det}.
 \tag{18}
$$

Apply (1) separately to each diagonal block, take fourth means in (18), and sum over the dyads. This does not require any common width in the estimates between different dyads. The identity
$T_N-(1-R_N)T_N(1-R_N)=T_NR_N+R_NT_N(1-R_N)$
and self-adjointness give (2), with all the actual mixed crossings included.

In (3), choose $\lfloor W_V/D\rfloor$ successive original windows per parent, shortening the last parent if needed. A true parent mean direction is $r_N\mathbf1_{I_N}$ normalized; it is the sum of the underlying unnormalized original window means, before normalization. Thus the parent mean space is genuinely nested inside the surviving literal mean space. The projection onto the parent contrasts, restricted to that literal space, is exactly its orthogonal complement of the parent means. Compress the full difference in (2) to the original literal mean space; by this nesting it equals the error of replacing the original mean operator by its parent-mean compression. The latter lies in dimension

$$
\ll \sum_V(1+V/W_V)
      \ll_\Gamma \log Q+Q^{-23/175}M^{3/7}
      \ll Q^{22/175}.
 \tag{19}
$$

In particular no dimension outside the annulus is being counted as deleted.

Finally $Q^{1/4}W_V^{7/4}/V=Q^{12/25}$ in (3), so the sampled RMS in (1) has the stated value at $J\gg Q^{99/100}$. Its non-sampled error is smaller, and $W_V/V\le Q^{-1/25}$. Choose $\kappa=1/4$ in (17); (18) gives the rate in (2). Before dividing by $J$, the sampled square sum on each dyad is $O_\epsilon(Q^{24/25+\epsilon})$ by (16); the deterministic error is pointwise $o(Q^{-1/200})$. Chebyshev and a union over dyads therefore leave $O_\epsilon(Q^{97/100+\epsilon})$ selected exceptions at threshold $Q^{-1/200}$ in the contrast-square HS bounds. At all other $N$, (17)–(18) and the logarithmic number of dyads make the full deletion $O(L^{O(1)}Q^{-1/400})$, below $Q^{-1/500}$ for large $Q$. Nothing in this argument estimates the principal covariance on the remaining parent means.
