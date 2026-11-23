# Conditional near-square-root rational arcs for the signed seam

Assume global Dirichlet GRH, including RH for the ordinary zeta function. Retain the exact $P_E,D$, hard cuts and even $N$ of [the signed seam major-arc proof](weak-s-type-ii-signed-seam-major-arcs.md), in particular $N/2<uv\le y\le9N/16$, $k>t\ge N^{.49999}$, $d\ge \sqrt N$, and the fixed unit/squarefree gates. The selector $E$ may be arbitrary with $|E|\le1$, independent of $d,k$. It may therefore be the actual no-exchange remainder. In particular, the Fourier coefficient of $P_ED$ still counts the true signed weight $\mu(u)b_{\rm II}(v)\mu(d)\mu^2(dk)$, with the genuine unit condition, not an independent arithmetic model.

**Theorem.** Fix $\kappa>0,\lambda\ge0$ with

$$
           2\kappa+5\lambda<1,\qquad \kappa+3\lambda<1/2.
$$

Put $Q=N^\kappa$, $W=N^\lambda\exp((\log N)^{3/5}(\log\log N)^{-1/5})$, and

$$
 \mathfrak V=\bigcup_{\substack{q\le Q\\ (a,q)=1}}
              \{a/q+\beta\bmod 1:|\beta|\le W/N\}.
$$

For some fixed $\delta'>0$ depending on the two margins above,

$$
       \int_{\mathfrak V}|D(\alpha)|^2\,d\alpha
                    \ll_{\kappa,\lambda} N^{1-2\delta'},
       \qquad
       \int_{\mathfrak V}|P_E(\alpha)D(\alpha)|\,d\alpha
                    \ll_{\kappa,\lambda} N^{1-\delta'/2}.
$$

The estimates are uniform in the original hard cuts. For example, this controls the absolute integral on $q\le N^{.48}$ and $|\beta|\le N^{-.995}$, including a substantial region outside the [unconditional quarter-range arcs](weak-s-type-ii-polynomial-rational-wings-length.md), which remain unconditional. Nothing is asserted about the whole signed complement. In §4, the fixed prime-box separate-$L^2$ obstruction is shown to persist even after deleting this larger region, under the same GRH.

## 1. A hard product wall may be frozen in global quadratic norm

Write $X=\sqrt N$, $L=\log N$ and $e(z)=e^{2\pi iz}$. In the complementary polynomial keep $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$ and both $N$-unit masks exactly. Its cut is $k>t$ and $N-y\le dk<N/2$; automatically $X\le d<N^{.50001}/2$ on the nonempty support. Impose this last hard $d$ range before any changes. Choose a small fixed $\rho>0$, to be specified from the margins, and partition each $d$ dyad of scale $D_0$ into intervals of relative width at most $N^{-\rho}$. Freeze only the two product walls using the left endpoint $d_0$ of each interval: require $N-y\le d_0k<N/2$. Keep $k>t$ exactly as an independent hard cut, and do not change the actual exponential $e(\alpha dk)$. This yields a polynomial $\widetilde D$ formed from $O(N^\rho L)$ rectangles, each with $d\asymp D_0$, $k\asymp K_0=N/D_0$, $D_0\gg X$.

Every altered product $m=dk$ lies within $O(N^{1-\rho})$ of $N-y$ or $N/2$, because on either support $dk,d_0k\asymp N$. The number of products is $O(1+N^{1-\rho})$, and the difference coefficient is bounded by $\tau(m)$; every pair is assigned to its single $d$ cell. The sharp endpoints need no other treatment. For every fixed $\epsilon>0$, Parseval and the elementary divisor bound give

$$
             \|D-\widetilde D\|_2^2\ll_\epsilon N^{1-\rho+\epsilon}.
$$

This is a global circle bound. In particular it does not multiply the freezing error by the number of rational arcs.

## 2. Exact character strata on one rectangle

We first record the GRH prefix bounds used below. For a character $\chi\bmod l$ with $l\le N^{O(1)}$, an extra unit mask $M\le N^{O(1)}$, and any hard subinterval of integers up to $O(Y)$, $1\le Y\le O(N)$, we use

$$
 \begin{aligned}
  \sum_{n\ {\rm in\ interval}}\mu(n)\chi(n)\mathbf1_{(n,M)=1}
                       &\ll_\epsilon \sqrt Y\,N^\epsilon,\\
  \sum_{n\ {\rm in\ interval}}\mu^2(n)\chi(n)\mathbf1_{(n,M)=1}
                       &\ll_\epsilon \sqrt Y\,N^\epsilon
                         \quad(\chi\ne\chi_0).
 \end{aligned}
$$

For the first bound at nonprincipal $\chi$ use [the uniform reciprocal-$L$ and hard Perron proof](weak-s-type-ii-medium-prime-growing-tags.md#1-quantitative-reciprocal-l-bound-and-interval-m%C3%B6bius-sums). At principal $\chi$ use the [ordinary RH Mertens bound](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf), Theorem 14.25(C), and convolve with the coefficients of $\prod_{p\mid lM}(1-p^{-s})^{-1}$; their sum weighted by $n^{-1/2-\epsilon}$ is $N^{o(1)}$ by splitting the primes at $\log N$. For the second bound the Dirichlet series is $L(s,\chi)/L(2s,\chi^2)$ with finite inverse factors $(1+\chi(p)p^{-s})^{-1}$ at primes of $M$. The real-logarithm estimate in that same GRH proof bounds $L$ itself as well as its reciprocal for nonprincipal $\chi$. On any fixed line $\Re s=1/2+\eta$ the denominator reciprocal at $2s$ is absolutely bounded, and the finite factors have size $N^{o(1)}$. Use hard Perron on that line with half-integer endpoints and polynomial height, as in the cited argument, taking $\eta$ small compared to $\epsilon$, then differences of prefixes. There is no pole for the nonprincipal numerator. The principal squarefree sum will instead be used with its trivial $O(Y)$ bound. All uses below have polynomial masks and endpoint scales at most $O(N)$.

Fix a $d,k$ rectangle of the preceding construction. Write $\alpha=a/q+\beta$ with $(a,q)=1$. Since the exact weight vanishes except at squarefree $dk$, the number $g=(dk,q)$ is squarefree. Split it uniquely into $g=g_dg_k$, where $g_d\mid d$ and $g_k\mid k$, and put $d=g_d x$, $k=g_k z$, $l=q/g$. Only $(g,N)=1$ can occur. The remaining masks are exactly $(xz,qN)=1$ and $(x,z)=1$, because $dk$ is squarefree and no prime divisor of $q$ can remain in $xz$. Conversely, with $g\mid\operatorname{rad}q$, these conditions and the weights $\mu(x)\mu^2(z)$ reconstruct the exact gcd group. The weight is $\mu(g_d)\mu(x)\mu^2(z)$ and the rational phase is $e(a xz/l)$.

For a character $\chi\bmod l$, let $H_{\chi,g_d,g_k}(\beta)$ be the sum of the preceding weights on this group, with the phase $e(\beta g xz)$ and the factor $\chi(xz)$. Expand the remaining $(x,z)=1$ by $\sum_{r\mid(x,z)}\mu(r)$ and put $x=ri$, $z=rj$. The original squarefree weights force $r$ squarefree and $(ij,r)=1$. Each term has separate unit masks with modulus $qNr$, a constant of modulus at most one (including $\chi(r)^2$), two factor intervals of scales $Y_d=D_0/(g_d r)$ and $Y_k=K_0/(g_k r)$, and phase $e(\beta g r^2ij)$. If a factor interval is nonempty its scale is bounded below by an absolute positive constant, and the stated prefix bounds apply with a harmless constant at $Y<1$.

Put $B=N|\beta|$. On the scaled rectangle the one-variable variation of the phase is $O(B)$, and the integral of the absolute mixed derivative is $O(B+B^2)$, independent of $r,g$. Indeed each derivative brings the relevant reciprocal side length times $O(B)$, and differentiating the factor $ij$ itself produces the $O(B)$ mixed term. Twice using Abel summation and the two square-root prefix bounds therefore gives, for nonprincipal $\chi$,

$$
 |H_{\chi,g_d,g_k}(\beta)|
    \ll_\epsilon \frac{\sqrt N\,N^\epsilon}{\sqrt g}(1+B)^2.
$$

Here $\sum_r 1/r$ is absorbed in $N^\epsilon$. For the principal $\chi$ use just the $\mu$ prefix bound, summing the other factor trivially for each fixed $j$, and one application of Abel. The $r$-sum now has $r^{-3/2}$, so

$$
 |H_{\chi_0,g_d,g_k}(\beta)|
    \ll_\epsilon N^\epsilon
          \frac{\sqrt{D_0}K_0}{\sqrt{g_d}\,g_k}(1+B)
    \ll_\epsilon \frac{N^{3/4+\epsilon}}{\sqrt g}(1+B),
$$

using $D_0\gg\sqrt N$, $D_0K_0=N$. No sign of an exterior divisor has been changed in forming these character sums.

## 3. Numerator norms and the near-square-root range

On the reduced residue group modulo $l$, expand $e(a xz/l)$ in multiplicative characters. With $\tau_l(\chi)=\sum_{w\bmod l}^{*}\chi(w)e(w/l)$, its principal coefficient is $\mu(l)/\varphi(l)$; the remaining coefficients have the corresponding $\tau_l(\overline\chi)/\varphi(l)$ times a character in $a$. This includes $l=1$ with empty nonprincipal sum. Parseval on the unit group gives $\sum_\chi|\tau_l(\chi)|^2=\varphi(l)^2$. The map from units modulo $q$ to units modulo $l$ is onto with multiplicity $\varphi(q)/\varphi(l)$. Thus the nonprincipal part of a fixed stratum has numerator $\ell^2$ norm at most $\sqrt{\varphi(q)}\sup_{\chi\ne\chi_0}|H_\chi|$. No individual estimate for a Gauss sum or primitivity of $\chi$ is needed.

Sum the strata using the elementary divisor bound to absorb the number of $g$ and decompositions into $N^\epsilon$. Their combined nonprincipal numerator norm on one rectangle is at most $N^{1/2+\epsilon}\sqrt q(1+B)^2$. In the principal part, $\varphi(l)^{-1}\ll_\epsilon N^\epsilon g/q$, hence the sum of principal absolute values pointwise in $a$ is bounded by

$$
 \ll_\epsilon N^{3/4+\epsilon}(1+B)
   \sum_{g\mid\operatorname{rad}q}\sum_{g_dg_k=g}
                       \frac{\sqrt g}{q}
 \ll_\epsilon N^{3/4+\epsilon}q^{-1/2}(1+B).
$$

The corresponding numerator $\ell^2$ norm is at most $N^{3/4+\epsilon}(1+B)$. These bounds are uniform for all $q\le Q$ and all $\beta$, including non-coprimality of $q$ and $N$.

Sum the $O(N^\rho L)$ rectangles by Minkowski. Since $2\kappa+\lambda<1$, the centers' separation at least $Q^{-2}$ makes the arcs disjoint for large $N$. Integrating the two squared bounds over $|\beta|\le W/N$ and all numerators therefore gives

$$
 \int_{\mathfrak V}|\widetilde D|^2
   \ll_\epsilon N^{2\rho+\epsilon}
              \bigl(Q^2(1+W)^5+N^{1/2}Q(1+W)^3\bigr).
$$

In the nonprincipal term sum $q$ after squaring and use $\int_{-W/N}^{W/N}(1+N|\beta|)^4d\beta\ll(1+W)^5/N$. For the principal term sum $1$ and integrate the second power instead. The respective power exponents before $2\rho+\epsilon$ are $2\kappa+5\lambda$ and $1/2+\kappa+3\lambda$, both strictly below one. Pick $\rho$ sufficiently small and then $\epsilon$ smaller than $\rho$, and absorb the subpower part of $W$. Combine the resulting power saving with the global freezing error from §1 to obtain the claimed $D$ estimate. As in the unconditional proof, $\|P_E\|_2^2\ll NL^5$ by its coefficient bound $L\tau(n)$, so localized Cauchy proves the second estimate. The remaining signed coefficient outside $\mathfrak V$ is still open.

## 4. The actual fixed prime-box obstruction on the smaller complement

Take exactly the hard box and $N=2^j$ of the [fixed-prime obstruction](weak-s-type-ii-fixed-prime-box-minor-l2.md). Its full circle norms satisfy $\|P\|_2^2\asymp N$, $\|D\|_2^2\gg N$ unconditionally with all competing $d$ representations included. The theorem above gives $\int_{\mathfrak V}|D|^2=o(N)$ even though we enlarged the deleted region. We also have $\int_{\mathfrak V}|P|^2=o(N)$ under the same GRH, as follows.

All actual $u,v$ primes in the box exceed $q$, since $\kappa<1/2$. Use the unit-group character expansion modulo $q$ for $e(auv/q)$ on $P$, with
$F_\chi(\beta)=-\sum_{u,v\ {\rm prime}}\chi(uv)\log v\,e(\beta uv)$ in its exact fixed intervals. For nonprincipal $\chi$, the [GRH prime explicit-formula bound, Lee, Theorem 4.3 and Corollary 4.4](https://arxiv.org/pdf/2301.13457v2#page=17) bounds each single-variable prefix of the weighted prime sum by $O(X^{1/2}L^2)$ and, by partial summation, also the unweighted prime prefix. The cases $q=1,2$ have no nonprincipal character. Apply the same two-dimensional Abel estimate to get $|F_\chi(\beta)|\ll X L^4(1+B)^2$. The preceding numerator Parseval therefore gives an integrated nonprincipal squared bound $O(Q^2(1+W)^5 L^8)=o(N)$.

For the exact principal $F_{\chi_0}$ use the ordinary RH prime estimate only on the $v$ sum, with one Abel factor $1+B$ and error $O(X^{1/2}L^2(1+B))$ per $u$. Its continuous integral has size $O(X/(1+B))$ since $u\asymp X$ and the interval is fixed of length $\asymp X$. Summing over the $O(X/L)$ primes $u$ gives a principal coefficient before multiplication by $\mu(q)/\varphi(q)$ of size bounded by
$O(N/(L(1+B))+N^{3/4}L^2(1+B))$.
Squaring and summing over the reduced fractions cancels one factor of $\varphi(q)$, and $\sum_{q\le Q}\varphi(q)^{-1}\ll\log(2Q)$. The integrated bound is

$$
 \ll \frac{N\log(2Q)}{L^2}
       +N^{1/2}(1+W)^3 L^4\log(2Q)
       =o(N),
$$

since $\lambda<1/6$. Therefore both separate $L^2$ norms on $(\mathbb R/\mathbb Z)\setminus\mathfrak V$ are still $\gg\sqrt N$. This is only an obstruction to bounding the signed minor integral by their product. It gives no sign or lower bound for that integral, and does not settle weak S.
