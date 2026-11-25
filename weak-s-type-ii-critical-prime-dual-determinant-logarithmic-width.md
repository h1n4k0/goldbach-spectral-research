# Joint dual-determinant completion for the logarithmically wide critical prime shell

Let $N$ be even, $X=\sqrt N$, $L=\log N$ and $L_2=1+\log L$. Keep the exact critical prime shell, genuine prime polynomial $P$ (including its permissible bounded selector and true unit test), and genuine complementary coefficient $D$ from the [logarithmic-width and reciprocal-unit theorem](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md). In particular, $N/2\le y\le9N/16$, $J=[N-y,N/2)$, $d$ lies in a hard interval $I_d$, the actual cofactor interval requires $k>t\ge N^{.49999}$, and

$$
 D_m=\mathbf1_{m\in J}\!
       \sum_{\substack{dk=m,\ d\in I_d,\ k\text{ in its true interval}\\
                      (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k).
$$

For $e(z)=e^{2\pi iz}$ put $D(\alpha)=\sum_mD_m e(m\alpha)$, $\mathcal Q=[.8X,.9X]\cap\mathbb P$, and

$$
 \mathcal E_N(D)
    =\int_{-1/(10N)}^{1/(10N)}
       \sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}|D(a/q+\beta)|^2\,d\beta .
$$

**Theorem.** Fix $C>1$ and any fixed $\gamma\ge0,\ F>0$. Allow all hard $I_d\subset[X,CXL^\gamma]$ and all the original hard cutoffs. For every even $R\mid N$ with $R\le L^F$ and all $\varepsilon>0$, uniformly,

$$
 \mathcal E_N(D)\ll_{C,\gamma,F,\varepsilon}
     N\left(L^{-1/2+\varepsilon}+\mathcal V(N,R)\right),\qquad
 \mathcal V(N,R)=\sum_{\substack{p\mid N\\p\nmid R}}\frac1p .
 \tag{1}
$$

The full signed shell on $(P,D)$, its separately centered numerator covariance, and the exact parity-preserving signed residual with $M=\lceil XL^2\rceil$ are consequently

$$
 O_{C,\gamma,F,\varepsilon}\!\left(
          NL^{-1/4+\varepsilon}+N\sqrt{\mathcal V(N,R)}\right).
 \tag{2}
$$

These are unconditional, also for all the permissible prime selectors. In particular a polylogarithmic full radical can be kept with zero unit loss. For every fixed $\gamma\ge0$ and $A>0$, simultaneously in the cutoffs and selectors, outside $O_{C,\gamma,A}(Y(\log Y)^{-A})$ even $N\in[Y,2Y]$, (1) gives $O_{C,\gamma,A}(N/\log^2(2+\log\log N))$, and (2) gives $O_{C,\gamma,A}(N/\log(2+\log\log N))$. The wider logarithmic box does not worsen this density rate. There is no claim on polynomial $d/X$, on an unrestricted radical pointwise, on other shells, or on Hypothesis S.

## 1. Exact initial transfers

Let $F_m$ be the signed raw coefficient of the preceding theorem, with the same physical and label cuts and without unit or squarefree restrictions. Exactly $D_m=\mu^2(m)\mathbf1_{(m,N)=1}F_m$. The [global reciprocal unit estimate](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md#1-the-true-global-omitted-unit-cost), equation (5), transfers this to the retained $R$-unit coefficient at ordinary squared cost $O_{C,\gamma}(N\mathcal V(N,R)+N^{1-\delta_0})$. This step uses the entire interval and so precedes all dyadic sums. The proof of that estimate holds for any fixed $\gamma$; its small-$g$ Mertens bound has polynomial endpoints and a stretched exponential margin against every fixed power of $L$.

Work on one disjoint half-open divisor dyad $A_0\le d<2A_0$, $A_0=\lambda X$ with $1\le\lambda\ll_C L^\gamma$, $K=X/\lambda$. There are $O_{C,\gamma}(L_2)$ dyads. Smooth the physical and short cofactor boundaries, not the hard long divisor; use $W(m/N)$ and $w(k/K)$ of relative width $\delta=L^{-B}$ supported inside the corresponding gates. We may choose all derivatives of orders $r\ge1$ to have support of measure $O(\delta)$, with sup norm $O_r(\delta^{-r})$. The $W,w$ ranges are fixed compact subsets of $(0,\infty)$, since $dk\in J$ and $d\asymp A_0$; inactive hard cofactor cuts may first be intersected with such a range, without creating any error outside a boundary strip in that range. For intervals shorter than a constant multiple of the smoothing width, the zero weight is allowed. Then truncate the squarefree identity at $l\le T=L^\eta$ with

$$
 D^{[T,R]}_m=\mathbf1_{(m,R)=1}F_m^{\rm sm}
          \sum_{\substack{l\le T\\ l^2\mid m}}\mu(l).
$$

The [true dyadic transfers](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md#2-uniform-exact-transfers-on-one-divisor-dyad) and the start of its §3 give the combined ordinary squared error

$$
 O_{C,\gamma,\rho,B,\eta}
        \big(N\delta L_2+N^{3/4}+NT^{-1+\rho}L_2\big)
 \tag{3}
$$

for fixed $\rho>0$, and $\|D^{[T,R]}\|_{\ell^2}^2\ll_{C,\gamma,\eta}N$. Their dyad proofs apply to the present $\lambda$: the forced square floor threshold is $\lceil\lambda^2\ell^2\rceil$ for a squarefree forcing label $\ell$; the signed short-divisor physical floor term is $K\sqrt{A_0}\le N^{3/4}$; the narrow short-label floor errors have size at most fixed powers of $L$ apart from the terms already $O(N\delta)$ for every fixed $\gamma$. The only upper restriction on $\gamma$ in the preceding theorem's optimized final bound came from its long character completion, which we replace below.

## 2. Dual cutoff and true square expansion

Fix $\beta\in[-1/(10N),1/(10N)]$. Exact logarithmic Fourier inversion uses
$G_\beta(z)=W(e^z)e(\beta N e^z)$ and $\widehat f(\xi)=\int f(z)e(-z\xi)\,dz$. Uniformly in $\beta$,

$$
 |\widehat G_\beta(\tau)|\ll\min(1,|\tau|^{-1},\delta^{-1}|\tau|^{-2}),\qquad
 |\widehat G_\beta(\tau)|\ll_r\delta^{1-r}|\tau|^{-r}\quad(r\ge2,\ \tau\ne0).
 \tag{4}
$$

These follow by integration by parts, since the nonconstant cutoff derivatives are localized, and the remaining phase derivatives cost bounded constants of each order.

Take a fixed term of the exact split $l\le T$ squarefree with $(l,R)=1$, $s=(l,d)\mid l$, and a squarefree inclusion variable $h\mid R$. Write $d=su$, $k=(l^2/s)hv$. This is the true $l^2\mid dk$ constraint on the squarefree signed $d$ support. Its long coefficients, exact short test and scales at frequency $\tau$ are

$$
 \begin{split}
 a_u&=\mu(u)\mathbf1_{su\in I_d\cap[A_0,2A_0)}
       \mathbf1_{(u,lR)=1}\,e\big(\tau\log(su/A_0)\big),
       & A_\tau(\theta)&=\sum_u a_u e(u\theta),\\
 f_\tau(z)&=w(z)e(\tau\log z),\qquad U=A_0/s,
       & V&=Ks/(l^2 h),\qquad x_0=V/X,\quad x_q=V/q .
 \end{split}
 \tag{5}
$$

Thus $u\in[U,2U)$ and $V\le K$, $x_q\asymp x_0\le1$ up to the fixed factor $1/.8$. Because $h\mid R$, $s\ge1$, and $\lambda\ll_C L^\gamma$, $x_q\gg_C L^{-(\gamma+2\eta+F)}$. The remaining multiplicative factors in the exact split are $\mu(l)\mu(s)\mu(h)$ and the character multiplier $\chi(l^2h)$, of modulus one on the prime shell for sufficiently large $N$. The unit of $s$ is automatic because $(l,R)=1$. Inclusion on $h$ imposes the unit condition on the remaining short variable; there is no extra coprimality condition between $u$ and $v$ in this truncated auxiliary, since the genuine one was already encoded by the exact original squarefree identity.

For a nonprincipal character $\chi\bmod q$ let $U_\chi=\sum_u a_u\chi(u)$ and $V_\chi=\sum_v f_\tau(v/V)\chi(v)$. Finite progression Poisson and the primitive Gauss identity give exactly

$$
 V_\chi=\tau_q(\chi)\,x_q\sum_{j\ne0}\overline{\chi(j)}\,\widehat f_\tau(jx_q),
 \qquad |\tau_q(\chi)|=\sqrt q .
 \tag{6}
$$

The convention is $\tau_q(\chi)=\sum_{b\bmod q}\chi(b)e(b/q)$; the missing $j=0$ has character sum zero here. The test is zero on nonpositive real arguments.

We may work with fixed polynomial-logarithmic cutoffs $|\tau|\le L^{J_\tau}$ and $1\le|j|\le L^{J_j}$, with negligible error in the norm defined below. For detail, use the periodization estimate at mesh $x_q\le5/4$ from the [composite-square proof](weak-s-type-ii-critical-prime-composite-square-and-unit-tail.md#3-smooth-completion-at-the-literal-rational-points),
$x_q\sum_j|\widehat f_\tau(jx_q)|\ll\delta^{-1/4}+\sqrt{1+|\tau|}$.
The elementary long character norm is at most $O(\lambda\sqrt{qX})$ from counting residue occupancy. Thus the untruncated $\ell^2(q,\chi\ne\chi_0)$ norm of $U_\chi V_\chi$ is $O_C(N L^{O_{\gamma,B}(1)}(1+\sqrt{|\tau|}))$. For any $J_\tau>B+1$, (4) with sufficiently large $r$ makes its integrated tail $O(NL^{-M_0})$ for any prescribed fixed $M_0>0$. On the retained $\tau$ range, choose fixed $J_j>\gamma+2\eta+F+\max(B,J_\tau)+2$. Since $\|f_\tau^{(r)}\|_1\ll_r(1+\delta^{-1}+|\tau|)^r$ on the fixed positive support, the absolute dual tail in (6) after removing the Gauss factor is at most

$$
 x_q\sum_{|j|>L^{J_j}}|\widehat f_\tau(jx_q)|
 \ll_r (1+\delta^{-1}+|\tau|)^r
          (x_q L^{J_j})^{1-r}.
$$

This is $O(L^{-M_0})$ for every fixed $M_0$ on increasing $r$. Using the same elementary long norm, the two discarded parts stay negligible after multiplying by the fixed-power-logarithmic tuple count and after the actual $\beta$ integration. All retained $j$ are nonzero modulo $q$ for sufficiently large $N$.

On the retained frequencies, remove $|\tau_q(\chi)|$ and algebraically add the principal character to the positive norm (without applying (6) to the actual principal sum). Orthogonality groups the terms by $u/j$ in the nonzero residue group. Adding the square of the zero residue group can only increase the answer. We obtain the following upper bound for the squared norm at fixed tuple and $\tau$, with the dual cutoffs understood:

$$
 \sum_{q\in\mathcal Q} q(q-1)x_q^2
   \sum_{j,j'}\widehat f_\tau(jx_q)\overline{\widehat f_\tau(j'x_q)}
   \sum_{\substack{u,u'\\j'u-ju'\equiv0\bmod q}}a_u\overline{a_{u'}} .
 \tag{7}
$$

This is a nonnegative complete residue norm. It does not remove or replace the actual nonunit additive contribution, which is retained separately below. In particular, the added residues in (7) are an algebraic inequality, not a hypothesis that arbitrary signs or products can be made nonzero.

## 3. Nonzero determinants and the weighted zero determinant

We use the classical unconditional uniform Möbius exponential sum theorem of [Davenport, 1937](https://academic.oup.com/qjmath/article-abstract/os-8/1/313/1564796), stated explicitly in [He and Huang, equation (1.2), PDF p. 1](https://www.impan.pl/shop/en/publication/transaction/download/product/91740?download.pdf=). It gives $\sup_\theta|\sum_{u\le z}\mu(u)e(u\theta)|\ll_H z(\log z)^{-H}$ for each fixed $H>0$; implied constants here need not be effective.

For the masks in (5), this implies

$$
 \sup_\theta |A_\tau(\theta)|\ll_{H,C,\gamma,F,\eta,J_\tau} U L^{-H}
 \qquad(|\tau|\le L^{J_\tau}).
 \tag{8}
$$

To verify this, write the coprime Möbius function as $\mu$ convolved with the indicator of positive integers all of whose prime factors divide $lR$. For the convolution divisor $b\le\sqrt U$ apply Davenport to the rescaled hard endpoints of size $\asymp U/b$, with additive frequency $b\theta$. The summed reciprocal Euler product is $L^{O_{F,\eta}(1)}$ since $lR\le L^{F+\eta}$. For $b>\sqrt U$ count trivially, and use
$\sum_{b>\sqrt U,\ b\ {\rm supported\ on}\ lR}b^{-1}
 \le U^{-1/8}\prod_{p\mid lR}(1-p^{-3/4})^{-1}
 \ll U^{-1/8}L^{O_{F,\eta}(1)}$.
Abel summation on the proportional long interval handles the smooth twist in (5), with cost $O(1+|\tau|)$ and no movement of the hard endpoints. Both losses are absorbed by choosing a stronger fixed Davenport exponent, since $U\gg X/L^\eta$.

For $j'u-ju'\ne0$ write $j'u-ju'=bq$ with $b\ne0$. For fixed $j,j',b$ the contribution to (7) is exactly the integral over $[0,1]$ of

$$
 A_\tau(j'\theta)\overline{A_\tau(j\theta)}
                \sum_{q\in\mathcal Q} w_q e(-bq\theta),\qquad
 w_q=q(q-1)x_q^2\,\widehat f_\tau(jx_q)
                               \overline{\widehat f_\tau(j'x_q)}.
$$

Here $|w_q|\ll X^2$ and the frequencies $bq$ are distinct because $b\ne0$. Plancherel gives norms $O(\sqrt U)$ for the second factor involving $A_\tau$ (nonzero integral dilation) and $O(X^2\sqrt{\#\mathcal Q})$ for the last factor. Bound the first by (8). Since the number of $j,j',b$ is a fixed power of $L$ (in particular $|b|\ll_C L^{J_j+\gamma}$), the resulting absolute bound over all nonzero determinants is $O(N^2 L^{-H})$ for every fixed $H>0$. Indeed $U^{3/2}X^2\sqrt{\#\mathcal Q}\ll_C N^2L^{3\gamma/2}$ before the arbitrarily strong logarithmic saving. This step uses the signs of the same long Möbius coefficient at every $q$, rather than taking separate unsigned character or progression norms.

For the zero determinant, $u,u'>0$ forces $j,j'$ to have the same sign. The solution count in $[U,2U)^2$ is at most $2U\gcd(|j|,|j'|)/\max(|j|,|j'|)$: the larger required positive multiple bounds its multiplier, so no additive $1$ is needed. Put $Y_\tau=1+\delta^{-1/2}+|\tau|$ and $J_0=Y_\tau/x_0$. From $\|f_\tau''\|_1\ll 1+\delta^{-1}+|\tau|^2$ one has, uniformly across $q$,

$$
 |\widehat f_\tau(jx_q)|\ll b_j:=\min(1,(J_0/|j|)^2).
$$

For positive $i\le j$, $\sum_{i\le j}\gcd(i,j)/j\le\tau_{\mathrm d}(j)$, where $\tau_{\mathrm d}$ is the divisor-counting function; expand the gcd by Euler's totient and count multiples. Ordering $i,j$ and allowing the corresponding infinite positive tails therefore bounds the double sum of $b_i b_j\gcd(i,j)/\max(i,j)$ by $O(\sum_j b_j\tau_{\mathrm d}(j))=O(J_0\log(2J_0))$, using the elementary summatory divisor bound. On the retained frequency interval, $\log(2J_0)\ll_{C,\gamma,F,\eta,J_\tau,B}L_2$. Multiplication by $U x_0^2$ reduces this to $O(Y_\tau L_2 U x_0)$, importantly with the *actual* support length $U=A_0/s$. Thus

$$
 Ux_0=\frac{A_0}{s}\frac{Ks}{Xl^2 h}=\frac{X}{l^2 h}.
$$

Together with $\sum_{q\in\mathcal Q}q(q-1)\ll X^3/L$, the zero determinant contributes at most

$$
 O_{C,\gamma,F,\eta,J_\tau,B}
        \left(\frac{N^2Y_\tau L_2}{L\,l^2h}\right).
 \tag{9}
$$

Neither the logarithmic dyad imbalance nor the square-label count survives as a power of $L$ in the main estimate.

## 4. Return to the actual shell

Take the square root of (9) and use Minkowski across the shared logarithmic frequency and the exact split. Equation (4) gives
$\int |\widehat G_\beta(\tau)|\sqrt{Y_\tau}\,d\tau\ll_B\delta^{-1/2}$:
split at $1$ and $\delta^{-1}$, and use
$\sqrt{Y_\tau}\ll\delta^{-1/4}+\sqrt{1+|\tau|}$.
The diagonal tuple sum in norm is bounded by

$$
 \sum_{l\le T}\frac{\tau_{\mathrm d}(l)}l
          \sum_{\substack{h\mid R\\h\ {\rm squarefree}}}\frac1{\sqrt h}
 \ll (1+\log T)^2 L^{o(1)}.
$$

Indeed the first estimate follows by the divisor convolution and harmonic sums, and the second follows already from $2^{\omega(R)}\ll_{\nu,F}L^\nu$ for every fixed $\nu>0$, by the elementary bound $2^{\omega(R)}\ll_\nu R^{\nu/F}$ (with $F$ fixed). The negligible off-diagonal and cutoff errors can instead use the unweighted tuple count, which is still a fixed power of $L$. This bounds the squared nonprincipal norm after $\beta$ integration by $O_{C,\gamma,F,B,\eta,\varepsilon}(N L^{-1+B+\varepsilon})$; the length of the genuine $\beta$ interval is $1/(5N)$.

At nonzero numerators the ordinary finite Gauss expansion multiplies the squared nonprincipal character norm by $q/(q-1)$, a uniformly bounded factor. Restore the actual principal unit character and the $q$-nonunit additive polynomial by the same literal calculation as [the logarithmic-width theorem, §3](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md#3-completion-at-the-longer-residue-scale). For clarity, $k\le X/2<q$ forces $q\mid d$ on the nonunit part. There are $O(\lambda)$ values $d=j q$; summing the truncated square multiplier over the corresponding $k\ll K$ costs at most $O(K\prod_{p\mid jq}(1+1/p))\ll_{C,\gamma,\varepsilon}K L^\varepsilon$ per $d$, by counting the required multiples $l^2/(l,d)$ on the signed squarefree $d$ support. Thus the actual nonunit polynomial is $O(XL^\varepsilon)$ for each $q,\beta$, and its squared energy is $O(NL^{-1+\varepsilon})$. This also covers the possibility $q\mid N$ without altering the original unit restoration. The exact numerator-zero value of the unit portion is the full ordinary value minus that nonunit value; the full ordinary squared norm is $O(N)$ by §1. The factor $\sum_q1/(q-1)\ll1/L$ then bounds the actual principal squared contribution by $O(NL^{-1+\varepsilon})$. The principal term algebraically added in (7) is not identified with this term.

Set $B=\eta=1/2$, and take $\rho$ small in terms of the desired $\varepsilon$. Transfer (3) by ordinary Parseval to the actual disjoint arcs. Sum the divisor dyads in norm, absorbing $L_2$ powers into $\varepsilon$. Finally reinstate the omitted primes by the global, undivided reciprocal unit estimate from §1. This proves (1). The full true hard $D$ and $P$ have ordinary squared norm $O(N)$ as in the logarithmic-width theorem (for $D$ use the true signed short label on squarefree support and the full $O(X^2)$ floor total). Cauchy and contraction under centering give the first two signed estimates. The [exact parity-preserving identity](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md) uses the same physical support, true oddness and ordinary squared norms. Its remainder is $O(N/L+N(X/M)^2)$, so (2) holds also for its signed residual. No bound on individual compensated offset squares is implied.

## 5. Density without losing the preceding rate

Use exactly the reciprocal cutoff family of the logarithmic-width theorem: $v=\log\log N$, $z_N=\kappa v\log(2v)$ for a fixed sufficiently small $\kappa>0$, and $R_N=\prod_{p\mid N,\ p\le z_N}p$. For large $N$ and even targets $R_N$ is even. On $[Y,2Y]$ let $z^*=\max z_N$ there and $v_Y=\log\log Y$. The positive expansion of $R_N^{1/2}$ is dominated by the analogous product over all $p\le z^*$; counting positive multiples gives

$$
 \frac1{2Y}\sum_{Y\le N\le2Y}R_N^{1/2}
 \le \prod_{p\le z^*}\left(1+\frac{\sqrt p-1}{p}\right)
 \le \exp(O(\sqrt{z^*}))=\exp(o(v_Y)).
$$

The last inequality even uses the sum over all integers up to $z^*$. Taking $F>2A+2$ bounds the count where $R_N>(\log N)^F$ by $O_A(Y(\log Y)^{-A})$. Independently the reciprocal-tail Euler estimate in [§4 of the predecessor](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md#4-true-even-target-density-with-the-reciprocal-loss) gives $\mathcal V(N,R_N)\ll_A(\log(2+v))^{-2}$ outside the same size of exceptional set. That proof is purely a statement about divisors of $N$ and does not restrict $\gamma$. Intersect the two actual integer sets and insert in (1)–(2), proving the density assertion.
