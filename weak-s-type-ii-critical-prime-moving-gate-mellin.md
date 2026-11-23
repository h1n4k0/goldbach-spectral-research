# The sharp moving prime product gate retains the stronger critical-shell mean square

Use the actual signed critical-shell pairings, the sharp target-dependent cuts, and the genuine full or three-band complementary coefficients of the [almost-all critical-shell theorem](weak-s-type-ii-critical-prime-signed-almost-all-boundaries.md). The prime factors stay in their original hard proportional boxes with true weight $-\log v$ and selector $E=1$ (or a fixed bounded separated multiplier as there). In particular the prime product gate $N/2<uv\le y\le9N/16$ may be active. The actual $N$-unit masks and the choice of either full or double-centered covariance are unchanged.

The stronger unconditional bound holds with $y$ included in the supremum:

$$
\sum_{\substack{Y\le N\le2Y\\2\mid N}}
 \sup_{\text{permitted sharp cuts including } y}
 \bigl(|\mathcal I_N|^2+|\mathcal C_N|^2\bigr)
 \ll_\epsilon Y^{5/2+\epsilon}.
\tag{1}
$$

Consequently the power threshold $N^{1-\delta}$ for any fixed $0<\delta<1/4$ fails for at most $O_\epsilon(Y^{1/2+2\delta+\epsilon})$ even targets in the dyad. Only the pointwise square-sum estimate for active prime product cells in the previous proof is replaced below; all exact moving complementary masks, shell arcs, cutoff and unit bookkeeping remain as in that theorem.

## 1. A sharp product-cell Mellin bound

Fix the ambient scale $Y$, a pair of $u,v$ cells $U,V$, and a dyadic level for the integer product $m=uv$ whose cells $J$ have length $H$. The only relevant products satisfy $cY\le m\le CY$ for absolute positive $c,C$, since the prime boxes are bounded proportional intervals at square-root scale. Define

$$
P_{U,V,J}(\alpha)=
 \sum_{\substack{u\in U,\ v\in V\\uv\in J}}
 a_u b_v e(\alpha uv),
$$

where $a_u,b_v$ include the unchanged common prime weights and primality masks before restoring the $N$-unit estimate of the preceding theorem. All estimates below in fact hold for complex $a_u,b_v$ on the given integer supports. Let $\alpha=a/q+\beta$ be an ambient reduced prime arc of that theorem.

We claim that

$$
\sum_J|P_{U,V,J}(\alpha)|^2
 \ll (\log Y)^2 q\left(\sum_{u\in U}|a_u|^2\right)
                    \left(\sum_{v\in V}|b_v|^2\right).
\tag{2}
$$

If $H$ is at least a fixed small multiple of $Y$, only $O(1)$ cells meet the ambient product support and (2) follows by the rectangular row-decomposition argument for an individual product cell in the preceding theorem. Otherwise take that multiple sufficiently small in terms of $c$ so the endpoints of every relevant cell lie within another fixed positive proportional interval of scale $Y$.

By duality in $\ell^2(J)$ take arbitrary complex coefficients $c_J$ with $\sum_J|c_J|^2=1$. For the integer cell $J=\{r,r+1,\dots,r+H-1\}$ put a step function $A(z)$ equal to $c_J$ on

$$
[\log((r-\tfrac12)/Y),\ \log((r+H-\tfrac12)/Y)).
$$

Set it to zero on the unused cells and elsewhere. The positive log boundaries have spacing $\gg\Delta=H/Y$, cell widths are $O(\Delta)$, and hence $\|A\|_2^2\ll\Delta$. The jump weights $d_j$ at the distinct log boundaries $z_j$ satisfy $\sum_j |d_j|^2\le4$: each is a difference of neighboring coefficients (or of one coefficient and zero), and each coefficient can occur at two boundaries.

Convolve $A$ with a fixed smooth nonnegative compactly supported unit-mass bump at logarithmic scale $\eta=c_0/Y$ for a sufficiently small absolute $c_0>0$. Denote the resulting function by $A_\eta$. Its values at all $\log(m/Y)$ for relevant integer products $m$ are exactly unchanged, since the half-integer boundaries are at log distance $\gg1/Y$ from every such integer. With Fourier convention $e(-tz)$ in the transform, we have

$$
\|\widehat A_\eta\|_1\ll\log Y.
\tag{3}
$$

For $|t|\le\Delta^{-1}$ use Cauchy–Schwarz and Plancherel to obtain $O(\Delta^{-1/2}\|A\|_2)=O(1)$. For every positive or negative dyad with $|t|\asymp T\ge\Delta^{-1}$, the distributional derivative identity gives

$$
 2\pi i\,t\widehat A(t)=\sum_j d_j e(-t z_j).
$$

The latter exponential sum has squared integral $O(T)$ on the dyad. To see this, majorize the dyad by a fixed nonnegative smooth cutoff rescaled by $T$. On expansion its kernel is bounded by $O(T(1+T|z_j-z_k|)^{-2})$. The boundary spacing and $T\Delta\gg1$ make its row sums $O(T)$, so the bound follows from $\sum|d_j|^2\le4$. Cauchy–Schwarz and division by $|t|\asymp T$ now give an $O(1)$ Fourier one-norm contribution per dyad. There are only $O(\log Y)$ such dyads until $T\asymp\eta^{-1}$. Beyond that, the multiplier from the convolution bump decays rapidly in $\eta T$, giving a convergent tail. This proves (3).

Fourier inversion and the exact smoothing on integers express the dual linear combination $\sum_J c_J P_{U,V,J}(\alpha)$ using separated factors:

$$
\int_{\mathbb R}\widehat A_\eta(t)
 \sum_{u\in U,\,v\in V} a_u b_v
   e(\alpha uv)e(t\log(u/\sqrt Y))e(t\log(v/\sqrt Y))\,dt.
$$

For every real $t$ the two new factors have modulus one. The complete matrix $e(aij/q)$ has operator norm $\sqrt q$ on residues, with bounded integer-to-residue multiplicity on the ambient supports. The phase $e(\beta uv)$ is separated by its absolutely summable Taylor series as before because $|\beta|Y\le1/10$. Therefore the inner bilinear sum has absolute value at most a constant times $\sqrt q\|a_U\|_2\|b_V\|_2$, uniformly in $t$. Use (3) and take the dual supremum to get (2).

## 2. Consequence for the whole target average

For fixed levels of all prime coordinates, sum (2) over the disjoint $U,V$. Their coefficient-square totals are $O(\sqrt Y)$ and $O(\sqrt Y(\log Y)^2)$ respectively, so

$$
\sup_{\alpha\ {\rm on\ ambient\ arcs}}\sum_{U,V,J}|P_{U,V,J}(\alpha)|^2
 \ll Y^{3/2}(\log Y)^4.
\tag{4}
$$

The same estimate holds after subtracting the separate means over all nonzero numerators, by Jensen and uniformity in $a$. No rounding of the prime product interval has occurred. In the preceding theorem, substitute (4) for its weaker active-cut square sum. Summed complementary cell energies remain $O_\epsilon(Y^{1+\epsilon})$ with the exact divisor expansion for the complementary $N$-unit mask. The common-coefficient Bessel argument, maximization over hard cuts, and restoration of the actual prime-unit mask and exact $\beta$ endpoints then give (1) as stated.

This is a signed maximal mean square with the original active prime cutoff and every critical alias. It estimates neither the exceptional targets pointwise, nor other arc ranges, nor weak S.
