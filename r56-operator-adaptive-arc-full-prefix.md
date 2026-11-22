# Adaptive raw arcs give full physical-prefix variance below the quarter-power scale

**Scope.** The result controls the entire original physical prefix, including all retained coarse–coarse directions between the previous prefix and the new cutoff. It is an ordinary mean-square and exceptional-count estimate over selected even moduli. It uses local and auxiliary Dirichlet GRH as separate assumptions. It does not bound the tail past the new radius, a specified modulus, a prescribed thin family, or the full Hardy operator.

## Statement

Let $\mathcal A\subset[Q,2Q]$ be any set of $J\ge1$ distinct even integers. For fixed $0<\xi<1/2,\ 0<\sigma<1$, put $P=\lfloor Q^\xi\rfloor,\ Y=Q^{-\sigma}$, and $1\le M\le Q^\gamma$ for fixed $\gamma>0$. Assume the manuscript's local Dirichlet $\mathrm{GRH}(N)$ at every $N\in\mathcal A$ and auxiliary Dirichlet GRH for all moduli $q\le P$. Let $P_M=\mathbf1_{(0,M]}$ in the true unitary physical $L^2(du)$ realization. Then for every $\epsilon>0$,

$$
 \begin{split}
 \left(\operatorname{Avg}_{N\in\mathcal A}
     \|P_MT_NP_M\|_{\rm HS}^2\right)^{1/2}
 \ll_\epsilon Q^\epsilon\Bigg[
 &\sqrt{\frac MJ}\left(\sqrt{\frac{QM}P}+(QM)^{3/10}\right)
        +\frac M{\sqrt{JY}}+\frac{P^2}{Q}\\
 &+\frac{M^{3/2}}{P\sqrt Y}+\frac MP
        +\frac M{\sqrt{QY}}+\sqrt{YM}\Bigg].
 \end{split}
 \tag{1}
$$

The fixed exponents may enter the implied constant. No interval or upper-diameter condition on the selected set is used beyond the shell. If $J\gg Q^d$, it is sufficient for a power saving that

$$
 0<\gamma<\sigma,\qquad
 \tfrac32\gamma+\tfrac12\sigma<\xi<\tfrac12,\qquad
 \gamma<\tfrac12(1-\sigma),\qquad
 \max\{1+2\gamma-\xi,\tfrac35+\tfrac85\gamma,2\gamma+\sigma\}<d\le1 .
 \tag{2}
$$

Such parameters exist for every fixed $\gamma<1/4$: take $\sigma$ slightly above $\gamma$, $\xi$ slightly below $1/2$ but above $3\gamma/2+\sigma/2$, and $d$ sufficiently close to one. Two explicit cases are

$$
 \begin{array}{c|c|c|c}
 \gamma&\sigma&\xi&d\\ \hline
 1/5&21/100&9/20&24/25\\
 6/25&1/4&49/100&199/200
 \end{array}
 \tag{3}
$$

with rates $O_\epsilon(Q^{-1/200+\epsilon})$ and $O_\epsilon(Q^{-1/400+\epsilon})$, respectively. In the second case, the number with HS norm greater than $Q^{-1/800}$, among any selected moduli (without a lower bound on $J$), is $O_\epsilon(Q^{397/400+\epsilon})$. Global Dirichlet GRH suffices for the hypotheses but is not a conclusion. In particular the concrete second case uses auxiliary moduli up to $Q^{49/100}$, more than [R49](r49-operator-full-prefix-variance.md)'s explicit $Q^{127/400}$ at $\gamma=3/25$.

## 1. True raw dyads, edge and sampling

As in [R49](r49-operator-full-prefix-variance.md), treat $[Y,M]$ by dyads $I_V=[V,2V)\cap[Y,M]$ with $V=2^jY$, the last possibly shortened. Work on the fixed direct sum of $\mathcal H_V=L^2([V,4V])$. For $a=N/Q$ the exact pullback of an actual test on $I_V$ is

$$
 g(z)=a^{-2}\frac{r_N(z/a)}{r_Q(z)}f(z/a)\mathbf1_{aI_V}(z),\qquad
 r_t(u)=u^{-3/2}\big((tu)^{-2/\log t}+(tu)^{-1/4}\big)^{1/2}.
$$

The pullback has uniformly bounded norm and preserves the raw weights $\sqrt{2\pi x}\,N^{-1}\int_{u\ge x/N}r_N(u)f(u)\,du$ exactly by $a^2/(aN)=1/Q$. Thus actual compression bounds follow by the HS ideal property from the fixed raw matrices. This does not require any mean-zero test or basis truncation loss. For a real orthonormal basis of $\mathcal H_V$ denote the vector of preserved raw weights by $h_V(x)$, let $Z_V=QV$, and set

$$
 A_V(\alpha)=\sum_p(\log p)\,h_V(p)e(p\alpha),\qquad
 B_V(\beta)=\int h_V(x)e(x\beta)\,dx,\qquad e(t)=e^{2\pi it}.
$$

The dimension-free [R49](r49-operator-full-prefix-variance.md) bounds from the Volterra formula are

$$
 \operatorname{supp}h_V\subset[0,4Z_V],\quad
 \|h_V(x)\|\ll \sqrt{x}/Z_V,\quad \|A_V\|_{L^2(\mathbb R/\mathbb Z)}\ll L^{1/2},
 \quad \|B_V\|_{L^2(\mathbb R)}\ll1,\quad
 \|B_V(\beta)\|\ll\sqrt{Z_V}\min(1,(Z_V|\beta|)^{-1}),
 \tag{4}
$$

where $L=\log Q$. The raw $\sqrt{x}$ prefix is present on each test. We can take finite test-basis truncations and then pass to the HS limit, with uniform constants.

For a pair $V\le U$, the exact signed positive-coordinate lines are $m=x+kN,\ m=x-kN,\ m=kN-x$, with signs $+,+,-$ respectively and $k\ge1$. There is no $k=0$ line. The continuous model on each is exactly

$$
 \mathfrak S(kN)\int h_V(x)\otimes h_U(m(x,N))\,dx.
 \tag{5}
$$

The same lines carry the arithmetic weights with the original units and prime powers. The raw sectors with $U<1/8$ vanish because $x+m\le8QU<N$ throughout their weights, excluding all three orientations. Otherwise put $S=\max(1,U)$, so $S\asymp U$ and $S\le M$; then only $1\le k\le8S$ can occur. Removing proper powers and temporarily permitting ordinary primes dividing $N$ costs $O_\epsilon(Q^\epsilon M/\sqrt{QY})$ in the full HS matrix per modulus. Indeed there are $O(\sqrt{QU}L)$ proper powers and $O(L)$ nonunit primes across the two legs, each with $O(S)$ alias partners, each tensor weight bounded by $O((Q\sqrt{VU})^{-1})$; the original log weights add $O(L^2)$. The $O(L^2)$ dyad-pair count is absorbed. No model term is removed.

The origin cross with $0<x<Y,\ y\le M$ (and its transpose) costs $O_\epsilon(Q^\epsilon\sqrt{YM})$ in HS. This is the [R49](r49-operator-full-prefix-variance.md) exact-kernel edge bound: no alias is possible unless $y\ge3/4$, where for $x<Y<1/4$ the $O(y)$ lines each carry at most $Nx$ atoms or an $O(x)$ continuum segment, and the cumulative weight is at most $\sqrt{xy}$. Restoring the Hardy multipliers yields the constant pointwise envelope $Q^\epsilon$ except when $Nx<1$; then there is no atom, and the extra $(Nx)^{-1/8}$ has square integral $O(1/N)$. Since $Y\ge1/N$, this proves the asserted edge bound.

Put $N=2n$. The ordinary prime contribution for a sector and a line orientation is the Fourier coefficient at $s=2kn$ of $A_V(\varepsilon_1\alpha)\otimes A_U(\varepsilon_2\alpha)$, where $(\varepsilon_1,\varepsilon_2)=(-,+),(+,-),(+,+)$ in line order. If $c_s$ are the tensor Fourier coefficients of any fixed $L^2$ torus function, the divisor-multiplicity sampling estimate is

$$
 \sum_{2n\in\mathcal A}\Big\|\sum_{1\le k\le 8S}c_{2kn}\Big\|_{\rm HS}^2
 \ll_\epsilon S Q^\epsilon\sum_{s\in\mathbb Z}\|c_s\|_{\rm HS}^2 .
 \tag{6}
$$

Indeed Cauchy in $k$ costs $O(S)$, and a positive $s\le16QS$ has at most $\tau(s)$ pairs $(k,n)$. It is immaterial that we shall choose different arcs for different pairs $V,U$; within each pair the function whose coefficients are sampled is fixed independently of $N,k$.

## 2. Adaptive arcs: minor bound and both major error types

For a fixed active pair set $X=QS$ and use disjoint raw major arcs

$$
 \mathfrak M_{V,U}=\bigcup_{\substack{q\le P\\(a,q)=1}}
       \{a/q+\beta:\ |\beta|\le\delta_q\},
 \qquad \delta_q=\frac{2P}{qX}.
 \tag{7}
$$

Here $\xi<1/2,\ X\ge Q$ give $4P^2<X$; against the rational spacing this implies disjointness on the torus. On the symmetric complement, Dirichlet approximation with denominator bound $\lfloor X/P\rfloor$ gives $P<q\le X/P,\ |\alpha-a/q|\le q^{-2}$. If the reduced $q$ were $\le P$, the approximation would place $\alpha$ in (7). Vaughan's prime exponential sum and the dimension-free weighted dynamic from [R49](r49-operator-full-prefix-variance.md) give, on the **shorter** test,

$$
 \|A_V(\alpha)\|\ll L^{O(1)}
        \big(\sqrt{QV/P}+(QV)^{3/10}+\sqrt{X/P}\big)
 \ll L^{O(1)}\big(\sqrt{QM/P}+(QM)^{3/10}\big).
 \tag{8}
$$

In fact, using $h_V(x)=Z_V^{-1/2}\sqrt{2\pi x/Z_V}$ times the Volterra cumulative in scaled coordinate, evaluate the weighted prime prefix $\sum_{p\le Z_Vv}\sqrt p(\log p)e(p\alpha)$ by Abel summation and apply Bessel to the scaled spatial tests. The upper term in the Vaughan estimate $t/\sqrt q+t^{4/5}+\sqrt{tq}$ becomes $\sqrt{X/P}$ after normalization, not a larger loss. This is why decreasing the major width to the longer raw support scale does not worsen (8). Proper powers in this scalar estimate are absorbed. By (4), tensor Parseval and (6), the minor terms give the first term of (1), after summing sectors and orientations.

On each arc $a/q+\beta$, write $A_V=M_V+E_V+Z_V^{\rm nu}$, where $M_V=(\mu(q)/\phi(q))B_V(\beta)$, $E_V$ is the unit-residue error, and $Z_V^{\rm nu}$ collects the finitely many primes dividing $q$. The latter has norm $O(L/\sqrt{QV})$ by (4), and can be dropped from both products at a coefficient cost $O(L^{O(1)}/\sqrt{QY})$ by Cauchy with the actual vectors' $L^2$ norms. After summing aliases and sectors this belongs in $M/\sqrt{QY}$. Auxiliary GRH gives the unit residue square bound $\sum_r|F_r(t)|^2\ll tL^4$, where $F_r(t)=\theta(t;q,r)-t/\phi(q)$ on the reduced residues and zero on the others. Here $0<t\le4QV$ and $q\le P$, including $t<2$ directly. The same holds on the $U$ leg. The [R49](r49-operator-full-prefix-variance.md) unit error is the finite additive transform of $-\widehat f_{r,i}(\beta)-2\pi i\beta\widehat g_{r,i}(\beta)$ with $f_{r,i}=\rho_{Q,\varphi_i}'F_r,\ g_{r,i}=\rho_{Q,\varphi_i}F_r$. Bessel on the moving-endpoint term and cancellation of the square-root derivative singularity by $F_r$ give $\sup_\beta\sum_{r,i}|\widehat f_{r,i}|^2\ll L^4$; real-line Plancherel gives $\sum_{r,i}\int|\widehat g_{r,i}|^2\ll QV L^4$.

First, the [R54](r54-operator-asymmetric-crossing.md) weighted-Plancherel argument for the **single** major errors is independent of the widths. The $f$-term of $M_V\otimes E_U$ costs $O(L^4q/\phi(q)^2)$ in squared norm across the $q$-arcs, by finite Parseval over $a$ and $\|B_V\|_2\ll1$. In the $g$-term use $\sup_\beta|\beta|\|B_V(\beta)\|\ll(QV)^{-1/2}$, giving the extra ratio $U/V$. Summing $q/\phi(q)^2$ up to $P$ costs $Q^\epsilon$. Thus the two product $L^2$ norms are $O_\epsilon(Q^\epsilon\sqrt{1+U/V})$ and $O_\epsilon(Q^\epsilon\sqrt{1+V/U})$. Negative signs in a Fourier argument just permute the centers and reverse $\beta$. Apply (6); since $U\asymp S$, the two errors after sampling and summing sectors are $O_\epsilon(Q^\epsilon M/\sqrt{JY})$.

Second, the **double** major error improves by (7). Finite Parseval over $a$, the same $f$-supremum and $g$-Plancherel, and $QV\le QU\le X$ give on either leg the bound

$$
 \|E_V\|_{L^2(\mathfrak M_{V,U})}^2
 \ll L^4\sum_{q\le P}q(\delta_q+\delta_q^2 QV)
 \ll L^5 P^2/X,
 \quad
 \|E_U\|_{L^2(\mathfrak M_{V,U})}^2\ll L^5P^2/X.
 \tag{9}
$$

For example $\sum_{q\le P}q\delta_q\ll P^2/X$ and the quadratic term is at most $P^2\log(2P)/X$. The per-coefficient norm of $E_V\otimes E_U$ is therefore $O(L^5P^2/X)$ by Cauchy on the torus. There are $O(S)$ aliases, leaving $O(L^5P^2/Q)$ uniformly in $N$, independent of this pair's physical size. This is the third term in (1), up to absorbed logarithms. In contrast the common width at the scale $Q$ would leave an additional physical-size loss on the double error.

## 3. Exact model, exponents and remaining blocks

The major main coefficient has the exact expression

$$
 \sum_{q\le P}\frac{\mu^2(q)c_q(s)}{\phi(q)^2}
    \int_{-\delta_q}^{\delta_q}
         B_V(\varepsilon_1\beta)\otimes B_U(\varepsilon_2\beta)e(-s\beta)\,d\beta .
 \tag{10}
$$

By (4) the omitted $\beta$-tail has norm at most $1/(\delta_q Q\sqrt{VU})\ll qS/(P\sqrt{VU})$. The full integral equals the unsigned line tensor in (5) by Fourier inversion and has norm $O(\sqrt{V/U})$, by the shorter leg's $L^1$ bound $O(\sqrt{QV})$ and the longer leg's pointwise $O((QU)^{-1/2})$. The elementary Ramanujan bounds used in [R49](r49-operator-full-prefix-variance.md) and [R54](r54-operator-asymmetric-crossing.md) are $\sum_{q\le P}q|c_q(s)|/\phi(q)^2\ll_\epsilon Q^\epsilon$ and $\sum_{q>P}\mu^2(q)|c_q(s)|/\phi(q)^2\ll_\epsilon Q^\epsilon/P$ for $1\le s\le16QS$; they follow by $|c_q(s)|\le\sum_{d\mid(q,s)}d$ and writing $q=de$. The full absolutely convergent series is $\mathfrak S(s)$, including the factor at $2$ for even $s$. Therefore restoring the exact signed model costs

$$
 O_\epsilon\left(Q^\epsilon\frac{S}{P}
       \left[\frac{S}{\sqrt{VU}}+\sqrt{V/U}\right]\right)
 \ll_\epsilon Q^\epsilon\left(\frac{M^{3/2}}{P\sqrt Y}+\frac MP\right)
$$

after the $O(S)$ alias count, before absorbing dyad-pair logs. The inequalities use $U\asymp S,\ V\le U$. This matches the original model, not a substitute with an averaged singular series or a discarded orientation.

Summing the established terms proves (1). With $J\gg Q^d$ the eight exponents in order are $(1+2\gamma-\xi-d)/2,\ 3/10+4\gamma/5-d/2,\ \gamma+\sigma/2-d/2,\ 2\xi-1,\ 3\gamma/2+\sigma/2-\xi,\ \gamma-\xi,\ \gamma-(1-\sigma)/2,\ (\gamma-\sigma)/2$. These give (2)–(3); in particular the second case has worst exponent $-1/400$. All non-sampled terms in that case are uniformly $o(Q^{-1/800})$ for sufficiently small $\epsilon$. Use (6) without normalization and Chebyshev on the minor and single-error terms; the exceptional number is

$$
 \ll_\epsilon Q^{1/400+\epsilon}
       \left[M\big(QM/P+(QM)^{3/5}\big)+M^2/Y\right]
 \ll_\epsilon Q^{397/400+\epsilon}.
 \tag{11}
$$

The $J$ lower bound is not needed for (11), but this upper bound need not be informative on arbitrary smaller selected sets.

This is a true coarse–coarse extension: in particular all pairs of retained coarse directions supported in $[Q^{3/25},Q^{6/25}]$ obey the same RMS bound in the second case, because a contraction of $P_MT_NP_M$ cannot increase its HS norm. The same statement controls every other direction of that prefix and its genuine crossing to the lower region. [R51](r51-operator-full-leg-fine-bridge.md)'s local-only fine bridge can therefore begin at the new $M$; the prefix-to-coarse and coarse-to-coarse blocks outside this new radius are still not bounded here. Nothing proves a pointwise or full weak-S bound.
