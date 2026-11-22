# Asymmetric variance for the actual prefix-to-coarse crossing

**Scope.** This extends one actual block left by the full-leg fine bridge: the physical crossing from the entire prefix through $Q^{3/25}$ to all spatial directions up to $Q^{19/100}$, including the retained coarse ones. The result is a Hilbert–Schmidt mean-square estimate over selected even moduli, not a pointwise estimate, not a bound on the doubly coarse exterior, and not a bound on the entire prefix-to-tail crossing.

## Statement

Let $\mathcal A\subset[Q,2Q]$ be any set of $J\ge1$ distinct even moduli. Assume the original local Dirichlet $\mathrm{GRH}(N)$ at each $N\in\mathcal A$ and auxiliary Dirichlet GRH for all $q\le P$, where $P=\lfloor Q^\xi\rfloor$, $0<\xi<1/2$. Write $L=\log Q$. Let $1\le A\le B\le Q^b$ with $b>0$ fixed, and set $Y=Q^{-\sigma}$ for a fixed $0<\sigma<1$. In the genuine physical realization, write $P_A=\mathbf1_{(0,A)}$ and $P_{[A,B]}=\mathbf1_{[A,B]}$. For every $\epsilon>0$,

$$
 \begin{split}
 \left(\operatorname{Avg}_{N\in\mathcal A}
       \|P_A T_N P_{[A,B]}\|_{\rm HS}^2\right)^{1/2}
 \ll_\epsilon Q^\epsilon\Bigg[
 &\sqrt{\frac BJ}\left(\sqrt{\frac{QA}P}+(QA)^{3/10}\right)
  +\frac{B}{\sqrt{JY}}+\frac{P^2 B^{3/2}\sqrt A}{Q}\\
 &+\frac{\sqrt B}{P}\big(Y^{-1/2}+\sqrt A\big)
  +\frac{B}{\sqrt{QY}}+\sqrt{YB}
 \Bigg].
 \end{split}
 \tag{1}
$$

This uses distinct moduli, not an interval property of their set. In particular

$$
 A=Q^{3/25},\quad B=Q^{19/100},\quad
 \xi=13/40,\quad \sigma=21/100,\quad J\gg Q^{99/100}
 \tag{2}
$$

give $O_\epsilon(Q^{-1/400+\epsilon})$. The same estimate holds for a crossing into the [R51](r51-operator-full-leg-fine-bridge.md) coarse cells fully contained in $[A,B]$, by restriction; one can restrict to a dyadic boundary $B'\in(B/2,B]$ with exactly the original cells from $A$ to $B'$. The two GRH assumptions are separate and global Dirichlet GRH suffices. No inference is made for a prescribed individual modulus or a thin family of cardinality comparable to $Q^{1/2}$.

## 1. Substitution on fixed raw sectors and the origin edge

Use the [genuine physical cumulative kernel](source-round2.md) and the common raw spaces of [R49](r49-operator-full-prefix-variance.md). More explicitly, split $[Y,A]$ and $[A,B]$ separately into dyads starting from $Y$ and $A$, shortening the last interval of each if necessary, so the left scales $V$ and right scales $U$ obey $Y\le V\le A\le U\le B$. On each sector beginning at $V$ use the real Hilbert test space $\mathcal H_V=L^2([V,4V])$, and likewise $\mathcal H_U$. Use $a=N/Q$ and the exact Hardy pullback $f(u)\mapsto a^{-2}r_N(z/a)f(z/a)/r_Q(z)$, $z=au$, with zero extension to the fixed space. Here $r_t(u)=u^{-3/2}((tu)^{-2/\log t}+(tu)^{-1/4})^{1/2}$, so the same raw argument $Qz=Nu$ makes the norm of this map uniformly bounded; $QY\ge1$ for large $Q$. The raw Volterra test weights are exactly preserved, since $a^2/(Na)=1/Q$. The raw Hilbert–Schmidt matrix bounds imply bounds on the actual crossing by the ideal property on both sides, irrespective of the infinite spatial rank and without any moving-endpoint approximation.

For a real orthonormal basis of $\mathcal H_V$, let $h_V(x)$ be its vector of raw weights $\rho_{Q,f}(x)=\sqrt{2\pi x}\,Q^{-1}\int_{z\ge x/Q}r_Q(z)f(z)\,dz$. Set $Z_V=QV$ and define $A_V(\alpha)=\sum_p (\log p)h_V(p)e(p\alpha)$, $B_V(\beta)=\int h_V(x)e(x\beta)\,dx$, $e(s)=e^{2\pi i s}$; in $B_V$ the subscript $V$ distinguishes this Fourier function from the spatial cutoff $B$. [R49](r49-operator-full-prefix-variance.md)'s dimension-free weight bounds are

$$
 \begin{gathered}
 \operatorname{supp}h_V\subset[0,4Z_V],\quad
 \|h_V(x)\|\ll \sqrt{x}/Z_V,\quad
 \int\|h_V\|^2\ll1,\quad
 \|A_V\|_{L^2(\mathbb R/\mathbb Z)}\ll L^{1/2},\\
 \|B_V(\beta)\|\ll\sqrt{Z_V}\min(1,(Z_V|\beta|)^{-1}),
 \qquad \|B_V\|_{L^2(\mathbb R)}\ll1 .
 \end{gathered}
 \tag{3}
$$

They apply also for $V<1$ since $Z_V\ge QY\ge1$; see [R49](r49-operator-full-prefix-variance.md), which keeps the nonzero raw prefix $\sqrt{x}$ down to the origin. All vector/tensor calculations can be made first in finite basis truncations with constants independent of the truncations.

The arithmetic side has lines $m=x+kN,\ m=x-kN,\ m=kN-x$, signs $+,+,-$, with no $k=0$. On raw dyads $V,U$, $1\le k\le8U$ suffices because both axes are positive and supported in $[0,4QU]$. The model on a line is exactly $\mathfrak S(kN)\int h_V(x)\otimes h_U(m(x,N))\,dx$, no adjustment. Remove proper powers and allow all primes, temporarily dropping the units at $N$: each proper power or prime divisor of $N$ has only $O(U)$ alias partners. The counts over both raw coordinates are $O(\sqrt{QU}L)$ and $O(L)$, respectively. By (3), the tensor point weight has HS norm $O((Q\sqrt{VU})^{-1})$. Including $O(L^2)$ prime marks, the total per sector is $O(L^3 U/\sqrt{QV})$; over all sectors this is bounded by $Q^\epsilon B/\sqrt{QY}$.

For the omitted origin $x<Y$, with $y\in[A,B]$, [R49](r49-operator-full-prefix-variance.md)'s exact-kernel estimate applies with the same upper cutoff $B$: the cumulative weighted signed atom-minus-model mass is $O_\epsilon(Q^\epsilon x^{3/2}y^{3/2})$, since $O(y)$ alias lines each have at most $Nx$ points or an $O(x)$ continuum segment, and the cumulative weight is at most $\sqrt{xy}$. For $x<1/N$ only the model remains, and the Hardy factor at $x$ is $O((Nx)^{-1/8})$, whose square integrates to $O(1/N)$ there. This gives $O_\epsilon(Q^\epsilon\sqrt{YB})$ for the actual omitted crossing. These arguments do not omit any center or interface directions.

## 2. Common sampling lemma and the shorter-leg minor arcs

For a fixed pair $V,U$ and orientation, the raw alias coefficient at $N=2n$ is the tensor Fourier coefficient at $s=2kn$ of $A_V(\varepsilon_1\alpha)\otimes A_U(\varepsilon_2\alpha)$, with $(\varepsilon_1,\varepsilon_2)=(-,+),(+,-),(+,+)$ in line order. Write $c_s$ for the Fourier coefficients of any $L^2$ tensor function on the torus. The same incidence argument as [R47](r47-operator-direct-short-window-variance.md) gives

$$
 \sum_{2n\in\mathcal A}\Big\|\sum_{1\le k\le8U}c_{2kn}\Big\|_{\rm HS}^2
 \ll_\epsilon UQ^\epsilon\sum_{s\in\mathbb Z}\|c_s\|_{\rm HS}^2 .
 \tag{4}
$$

Indeed Cauchy in $k$ costs $O(U)$ and any $s=2kn\le16QU$ has at most $\tau(s)\ll_\epsilon Q^\epsilon$ such representations. The bound also holds with only the nonempty alias indices included.

Use disjoint raw major arcs with centers $a/q$ reduced, $q\le P$, radius $\delta_q=2P/(qQ)$, and symmetric complementary minor arcs $\mathfrak m$. The disjointness follows from $4P^2<Q$, and Dirichlet approximation gives $P<q\le Q/P,\ |\alpha-a/q|\le q^{-2}$ on $\mathfrak m$. The [R49](r49-operator-full-prefix-variance.md) Abel–Bessel Vaughan bound applied to the **shorter** vector $V$ reads

$$
 \sup_{\mathfrak m}\|A_V\|\ll L^{O(1)}
   \big(\sqrt{QV/P}+(QV)^{3/10}+\sqrt{Q/P}\big)
 \ll L^{O(1)}\big(\sqrt{QA/P}+(QA)^{3/10}\big).
 \tag{5}
$$

Use the $L^2$ bound (3) on the longer vector, tensor Parseval, and (4). The RMS minor contribution is $O_\epsilon(Q^\epsilon\sqrt{B/J}(\sqrt{QA/P}+(QA)^{3/10}))$, summing the $O(L^2)$ sector pairs and the three orientations.

## 3. Single major errors: use weighted Plancherel before sampling

On each major arc $a/q+\beta$, write $A_V=M_V+E_V+Z_V^{\rm nu}$. The main vector is $M_V=(\mu(q)/\phi(q))B_V(\beta)$; $Z_V^{\rm nu}$ is the vector of the nonunit primes $p\mid q$, whose norm is $O(L/\sqrt{QV})$ pointwise by (3). The unit-residue error $E_V$ is the one in [R49](r49-operator-full-prefix-variance.md), with $F_r(x)=\theta(x;q,r)-x/\phi(q)$ for unit $r$, zero for nonunits. Auxiliary Dirichlet GRH gives $\sum_r|F_r(x)|^2\ll xL^4$, uniformly for $0<x\le4QV$, by character Parseval, the ordinary GRH prime sum, and removal of proper powers. The bound for $0<x<2$ is immediate from $F_r=-x/\phi(q)$ for unit $r$. These are the only auxiliary GRH estimates used. Uniformity in all characters and imprimitive Euler factors is as in [R49](r49-operator-full-prefix-variance.md). In particular $E_V$ has the vector component form

$$
 -\sum_{r\bmod q}e(ar/q)\big(\widehat f_{r,i}(\beta)+2\pi i\beta\widehat g_{r,i}(\beta)\big),
 \quad
 f_{r,i}=\rho_{Q,\varphi_i}'F_r,\qquad
 g_{r,i}=\rho_{Q,\varphi_i} F_r ,
 \tag{6}
$$

with positive-sign Fourier transforms and zero-extended weights. The exact dimension-free [R49](r49-operator-full-prefix-variance.md) estimates are

$$
 \sup_{\beta}\sum_{r,i}|\widehat f_{r,i}(\beta)|^2\ll L^4,\qquad
 \sum_{r,i}\int_{\mathbb R}|\widehat g_{r,i}(\beta)|^2\,d\beta
 \ll QV L^4 .
 \tag{7}
$$

For clarity the first uses the two derivative terms in $\sqrt{x}$ times a Volterra cumulative: the $x^{-1/2}$ factor is canceled by $\sqrt{x}$ in the residue-vector GRH bound, and differentiation of the moving lower limit is handled by Bessel over the spatial test basis. The second is real-line Plancherel and $\int x\|h_V(x)\|^2dx\ll QV$. The same statements with $V$ replaced by $U$ hold for the other leg.

The nonunits can be discarded in both major products at per-alias cost $O(L^{O(1)}/\sqrt{QY})$: the nonunit terms have the displayed uniform bound, and the other actual factors have $L^2$ norm $O(L^{1/2}+L/\sqrt{QY})$ on the torus or the majors. This controls both nonunit changes by Cauchy and their total arc measure at most one; summing aliases gives the same $B/\sqrt{QY}$ term already in (1).

It is unnecessary to use $L^1$ (pointwise coefficient) bounds for the two single-error products $M_V\otimes E_U$, $E_V\otimes M_U$. On arcs of denominator $q$, square the tensor norm, majorize the sum over reduced $a$ of (6) by the full $a\bmod q$ sum using finite Parseval, and note that $M_V$ does not depend on $a$. For the $f$-term on the $U$ leg use (7) and $\int\|B_V\|^2\ll1$. For the $g$-term on the $U$ leg use

$$
 \sup_\beta |\beta|\|B_V(\beta)\|\ll (QV)^{-1/2}
$$

from (3) and then (7) on the $U$ leg. This yields squared norm $O(L^4 q/\phi(q)^2\, (1+U/V))$ when summing all arcs of that denominator. Negative signs in Fourier arguments merely permute the centers and change $\beta$ to $-\beta$, with the same bounds. Sum $q/\phi(q)^2\ll_\epsilon Q^\epsilon$ in total over $q\le P$. Thus

$$
 \|M_V\otimes E_U\|_{L^2(\mathfrak M;\rm HS)}
    \ll_\epsilon Q^\epsilon\sqrt{1+U/V},
 \qquad
 \|E_V\otimes M_U\|_{L^2(\mathfrak M;\rm HS)}
    \ll_\epsilon Q^\epsilon\sqrt{1+V/U}.
 \tag{8}
$$

This estimate does not bring down the arc width $\delta_q$ as a separate loss. Instead the complementary raw weight itself supplies the $\beta$-decay. Apply (4) and torus Parseval to the two products extended by zero off the major arcs. Since $V\le U$, the resulting RMS per sector is at most $Q^\epsilon U/\sqrt{JV}$, hence at most $Q^\epsilon B/\sqrt{JY}$ after summing all sectors and signs.

For the double error $E_V\otimes E_U$ retain the pointwise coefficient estimate. From (6)–(7), finite Parseval, integration over $|\beta|\le\delta_q$ and $\sum_{q\le P}q(\delta_q+\delta_q^2 QV)\ll L P^2(1+V)/Q$, one has
$\|E_V\|_{L^2(\mathfrak M)}\ll L^{5/2}P\sqrt{(1+V)/Q}$
and the same with $U$. Cauchy bounds each coefficient of the double error by the product; multiplying by $O(U)$ aliases and summing the sector pairs gives $O_\epsilon(Q^\epsilon P^2 B^{3/2}\sqrt A/Q)$, using $U\ge A\ge1$ and $V\le A$.

## 4. Asymmetric model tails and conclusion

Both main vectors' coefficient at $s=2kn$ on the major arcs is exactly

$$
 \sum_{q\le P}\frac{\mu^2(q)c_q(s)}{\phi(q)^2}\!
     \int_{-\delta_q}^{\delta_q}
       B_V(\varepsilon_1\beta)\otimes B_U(\varepsilon_2\beta)e(-s\beta)\,d\beta .
 \tag{9}
$$

The integral tail is $O(q/(P\sqrt{VU}))$ by the two Fourier decays (3). The full integral equals the true signed-line spatial tensor before its singular factor, by Fourier inversion; it has HS norm $O(\sqrt{V/U})$ because the shorter raw leg has $\int\|h_V(x)\|dx\ll\sqrt{QV}$ and the longer weight has supremum $O((QU)^{-1/2})$. For $s\le16QU$, the Ramanujan estimates of [R49](r49-operator-full-prefix-variance.md) give $\sum_{q\le P} q|c_q(s)|/\phi(q)^2\ll_\epsilon Q^\epsilon$, and $\sum_{q>P}\mu^2(q)|c_q(s)|/\phi(q)^2\ll_\epsilon Q^\epsilon/P$; they follow by writing $q=de$ with $d\mid s$ in $|c_q(s)|\le\sum_{d\mid(q,s)}d$. The full series equals $\mathfrak S(s)$, including the factor at $2$ because $s$ is even. Restoring the full series and integral gives precisely the original continuous model with the exact line orientation. Therefore after summing aliases the model error per sector is bounded by

$$
 Q^\epsilon \frac{\sqrt U}{P}\big(V^{-1/2}+\sqrt V\big).
$$

Summing dyads and using $Y\le V\le A\le U\le B$ gives the asserted asymmetric model term in (1). Every projection and normalization used so far concerned the genuine operator; there is no independent-sign approximation.

Sum all six estimates to prove (1). In (2) the two minor powers are $-1/400$ and $-8/125$, respectively; the single-error, double-error, two model, proper-power/unit, and origin powers are $-1/5,-1/200,-1/8,-17/100,-41/200,-1/100$, respectively. Thus the first minor term determines the displayed RMS rate. In fact, with (2)'s spatial and auxiliary exponents but no lower bound on $J$, the number of selected moduli where this HS crossing exceeds $Q^{-1/800}$ is

$$
 \ll_\epsilon Q^{1/400+\epsilon}
   \left[B\big(QA/P+(QA)^{3/5}\big)+B^2/Y\right]
 \ll_\epsilon Q^{79/80+\epsilon}.
 \tag{10}
$$

Indeed remove the uniformly $o(Q^{-1/800})$ terms and apply (4), without dividing by $J$, to the minor and two single-error products. This does not identify the exceptions or show success on an arbitrary thinner set.

The upper radius $Q^{19/100}$ in this asymmetric crossing is beyond the symmetric [R49](r49-operator-full-prefix-variance.md) proof's parameter range: its inequalities $\gamma<\sigma,\ \gamma+\sigma<\xi,\ \xi+\tfrac32\gamma<\tfrac12$ force $\gamma<1/7$. [R51](r51-operator-full-leg-fine-bridge.md) removes the high fine directions and the extreme tail. This note additionally covers the actual coarse crossing from the full $Q^{3/25}$ prefix to the cells wholly below $Q^{19/100}$, for the stated large selected sets and auxiliary range. It still leaves the prefix crossing to later coarse cells and all coarse–coarse blocks outside [R49](r49-operator-full-prefix-variance.md)'s prefix uncontrolled.
