# Complementary Fourier collars for the true exterior difference matrix

**Scope.** This bounds actual Fourier modes outside the [low-denominator rational span](r44-operator-rational-variance-component.md), on the same finite sequence of even moduli. The estimate is for collars around low-denominator rational frequencies, not the entire complement or the full variance.

Use the actual [weighted mean differences](r40-operator-negative-difference-subspace.md) and [common physical grid](r43-operator-signed-modulus-window.md). Write $L=\log Q,\ \ell=\log L$. Fix $K>0,\ C>1,\ 0<\delta'<\delta<1/2$ and positive $\gamma,\xi$ with $\xi+3\gamma/2<\delta'$. Let $\mathcal I\subset[Q,2Q]$ have length $\Delta\ge Q^{1/2+\delta}$, and choose

$$
 H\ge2(K+3)\ell^2/\log\ell,\qquad Y=e^H,\qquad M=e^{CH}\le Q^\gamma,\qquad
 1\le B\le Q^\xi .
$$

Here $B$ is an integer. Take the whole dyads $I_V=[V,2V)\subset[Y,M]$ on the grid $V=2^jY$, and let $E_N$ be the isometry from the fixed dyad-index basis to the true normalized R40 difference tests at $N$. Use original local Dirichlet GRH for every even $N\in\mathcal I$, and auxiliary Dirichlet GRH for all moduli up to $8BM+2$. Global Dirichlet GRH suffices.

Put $\mathcal J=\{n\in\mathbb Z:2n\in\mathcal I\}$ with uniform probability, $J=|\mathcal J|$, and $X(n)=E_{2n}^{*}T_{2n}E_{2n}$. Let $\mathcal F_B=\{a/r\bmod1:1\le r\le B,\ 0\le a<r,\ (a,r)=1\}$, including $0$ at $r=1$, and let $\mathcal R_B$ be the span of its rational phases restricted to $\mathcal J$, as in R44. For any integer $h$ with $B^2\le h\le J/64$, put

$$
 \mathcal U_{B,h}=
 \{j\pmod J:\ \min_{\alpha\in\mathcal F_B}\|j/J-\alpha\|_{\mathbb R/\mathbb Z}\le1/(8h)\},
 \qquad
 \mathcal B_{B,h}=\operatorname{span}\{e^{2\pi i jn/J}:j\in\mathcal U_{B,h}\}.
$$

Then for every fixed $\epsilon>0$ the actual orthogonal projection satisfies

$$
 \|P_{\mathcal B_{B,h}}X\|_{L^2(\mathcal J;\mathrm{HS})}
 \ll_\epsilon BQ^{1/2+\epsilon}M^{3/2}/h+L^{5/2}Y^{-1/5}.
 \tag{1}
$$

The second term is absent for the R43 fixed-endpoint difference tests. Moreover,

$$
 \dim(\mathcal B_{B,h}\cap\mathcal R_B^\perp)\asymp B^2J/h ,
 \tag{2}
$$

and (1) also bounds the orthogonal projection onto this intersection. Taking $h=\lfloor Q^{1/2+\delta'}\rfloor$ gives $o(L^{-K})$ for sufficiently small fixed $\epsilon$, and satisfies the bounds on $h$ for large $Q$. In a full shell one may for example take $M\le Q^{.10}$, $B=\lfloor Q^{.05}\rfloor$, and $h=\lfloor Q^{.75}\rfloor$; the first error in (1) is then $O_\epsilon(Q^{-.05+\epsilon})$ and the dimension in (2) is $\asymp Q^{.35}$. The [spatial log-separation mask](r31-operator-zero-diagonal.md) is one on all supports here, since the spatial log diameter is at most $\log M\le \gamma L$. The benchmark is the exact original continuous model, as in R43–R44.

## 1. A uniform short partial-sum vector

Use the R43 fixed physical endpoints and omit proper prime powers temporarily, leaving the exact model unchanged; call the resulting true arithmetic error matrix sequence $\widetilde X$. Set $R=Q^{1/2+\epsilon}M^{3/2}$, absorbing fixed logarithms by reducing the $\epsilon$ in intermediate estimates. For every consecutive subinterval $\mathcal A\subset\mathcal J$ and every $r\le B$, the [unnormalized class-vector bound](r44-operator-rational-variance-component.md#1-the-arithmetic-class-vector-error) is

$$
 \left(\sum_{j\bmod r}
    \left\|\sum_{\substack{n\in\mathcal A\\n\equiv j\ (r)}}\widetilde X(n)
         \right\|_{\rm HS}^{2}\right)^{1/2}\ll_\epsilon R .
 \tag{3}
$$

No minimum length for $\mathcal A$ is needed in this unnormalized assertion. In fact, in the R44 switch replace the interval indicator by the one for the modulus interval corresponding to $\mathcal A$: its two endpoint jumps have the same total-variation bound, the residue-class vector estimate for the first prime coordinate uses only its raw range and auxiliary GRH, and the model floor discrepancy on a progression is $O(1)$ on every interval. Those are precisely the steps before the class counts are used in R44 §3. Thus the raw error bound $O_\epsilon(Q^{1/2+\epsilon}M^{3/2})$ survives a singleton or an empty intersection. Matrix HS costs at most $O(L)$, included in the $\epsilon$. Both same-residue and reflected arithmetic aliases retain their exact separate continuum densities from R44.

Write $e(s)=e^{2\pi i s}$. Finite Fourier Parseval over the $r$ class sums shows that the sum over $a\bmod r$ of
$\|\sum_{n\in\mathcal A}\widetilde X(n)e(-an/r)\|_{\rm HS}^{2}$
is $r$ times the left side of (3) squared. Retain only the distinct reduced phases and sum over denominators. Since $\sum_{r\le B}r=O(B^2)$, this gives the uniform vector estimate

$$
 \left(\sum_{\alpha\in\mathcal F_B}
       \left\|\sum_{n\in\mathcal A}\widetilde X(n)e(-\alpha n)
       \right\|_{\rm HS}^{2}\right)^{1/2}\ll_\epsilon BR.
 \tag{4}
$$

## 2. From rational centers to nearby actual Fourier modes

For each $\alpha\in\mathcal F_B$, let $b_\alpha/J$ be its nearest frequency on the $J$-point Fourier grid, choosing either in a tie. Choose $\beta_\alpha$ with $|\beta_\alpha|\le1/(2J)$ such that $b_\alpha/J=\alpha+\beta_\alpha$ mod $1$. For a consecutive interval of length at most $h$, (4) gives the same $O_\epsilon(BR)$ bound for the vector with phase $e(-b_\alpha n/J)$ in place of $e(-\alpha n)$. Indeed apply summation by parts in $n$ using the diagonal matrix of factors $e(-\beta_\alpha n)$ acting on the $\ell^2(\mathcal F_B;\mathrm{HS})$ vector. Its terminal factor has norm one; its successive differences have operator norm at most $\pi/J$. The sum of these differences along the interval is $O(h/J)=O(1)$, and (4) bounds all prefix sums. This step is uniform over the differing offsets $\beta_\alpha$.

Identify the consecutive interval $\mathcal J$ with representatives of $\mathbb Z/J\mathbb Z$. For each $\alpha$, demodulate $\widetilde X$ by the grid phase $e(-b_\alpha n/J)$ and take the length-$h$ moving average on this finite cyclic group. A window that wraps past the last representative splits into two ordinary consecutive subintervals of $\mathcal J$; the grid phase is genuinely periodic modulo $J$, and the preceding bound applies to both pieces. Therefore the squared $\ell^2(\mathcal F_B;\mathrm{HS})$ norm of these averages is $O_\epsilon((BR/h)^2)$ at each position, hence also in normalized mean square over the positions.

In the orthonormal $J$-point Fourier basis, this cyclic averaging has multiplier $h^{-1}\sum_{s=0}^{h-1}e(s\theta)$. Its absolute value is at least $1/\sqrt2$ when $\|\theta\|_{\mathbb R/\mathbb Z}\le1/(4h)$: rotate by the midpoint phase and each summand has angle at most $\pi/4$ in absolute value. If a grid mode $j/J$ lies within $1/(8h)$ of $\alpha$, it lies within $1/(4h)$ of $b_\alpha/J$, since $h\le J/64$. By cyclic Parseval, summing the preceding bound over the centers therefore bounds the actual Fourier energy of $\widetilde X$ in the entire union of collars by $O_\epsilon((BR/h)^2)$. Any overlap could only increase the sum used for this upper bound.

Restoring proper powers costs $O(Q^{-1/2}ML^4)$ in full $L^2(\mathrm{HS})$ by the R43 per-entry bound and the $O(L)$ matrix dimension. It is absorbed since $h\le J\ll Q$. The true coarse-cell unions instead of fixed endpoints cost $O(L^{5/2}Y^{-1/5})$ by the R43 operator comparison and at most $O(L^{1/2})$ on passing to HS. Both restorations remain bounded after an orthogonal projection. This proves (1).

Finally, the rational centers are $B^{-2}$-separated on the circle and number $\asymp B^2$ by the elementary coprime-pair count. For the lower count, at most $B^2\sum_{d\ge2}1/d^2<B^2$ ordered pairs in $[1,B]^2$ are noncoprime, and reflection interchanges the two triangles. With $h\ge B^2$ the collars are disjoint. Each contains at least $J/(4h)-1$ and at most $J/(4h)+1$ Fourier grid points; the bounds hold also for a collar crossing zero. The grid phases are orthonormal under normalized counting, so $\dim\mathcal B_{B,h}\asymp B^2J/h$. Imposing orthogonality to $\mathcal R_B$ loses at most $|\mathcal F_B|$ dimensions, which is a fixed fraction at most with $J/h\ge64$. This proves (2); projection onto the intersection has no larger norm than projection onto the full collar space.

The argument controls these extra modes of the actual modulus sequence at the stated polynomial collar width. It does not show the total Fourier energy, the complementary frequencies outside the collars, or an individual-modulus bound is small. The resulting variance component is not a proof of weak S.
