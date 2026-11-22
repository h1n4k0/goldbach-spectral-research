# Density-one signed cancellation in the exact dense four-prime rectangle

Fix $0<\rho<1/2$ and $0<\kappa\le1/2000$. Use the exact genuine four-prime rectangle from the [signed major-term evaluation](r43-source-dense-cell-positive-major-obstruction.md) for each sufficiently large even $N$:

$$
 N^{.38}\le q\le N^{.42},\qquad N^{.08}\le s\le N^{.12},\qquad
 I_0(N)=[\rho N,(1-\rho)N].
$$

The original first interval $I$ is any hard subinterval of $I_0(N)$ with either endpoint convention, the second remains $I_0(N)$, and both orders of $qp$, $sv$ are included when allowed. All four constituents are genuine primes, the original unit masks modulo $N$ hold, and the marker is $(\log q)(\log s)$. Let $C_I(N)$ be the true full-torus coefficient at $N$, $S(N)=\mathfrak S(N)$, and $\mathcal B_I(N)$ the exact real density integral of R43 for this rectangle, including its factors $\lambda(q)=(q-1)/(q-2)$ and the original cofactor unit masks.

**Theorem.** Given $A,B>0$ and $X$ large, there is a set of $O_{\rho,A,B}(X(\log X)^{-B})$ exceptional even $N\in[X,2X]$, independent of the moving first interval, such that unconditionally

$$
 C_I(N)
    =S(N)\mathcal B_I(N)
       +O_{\rho,A,B}\bigl(S(N)N(\log N)^{-A}\bigr)                \tag{1}
$$

uniformly in the original hard $I$ on the nonexceptional even moduli. The unconditional constants may be ineffective. Under global Dirichlet GRH, combining with R43 gives for the **[exact Dirichlet complement](r35-source-square-root-dirichlet-arcs.md)** $\mathfrak m(N)$ and actual four-prime product $\mathcal P_I$,

$$
 \left|\int_{\mathfrak m(N)}\mathcal P_I(\alpha)e(-N\alpha)\,d\alpha\right|
 \ll_{\rho,\kappa,B} S(N)N(\log N)^{-13}                         \tag{2}
$$

on the same density-one set (use $A=13$). There is no pointwise claim for the exceptional moduli, and the rectangle is unchanged from R43.

## 1. A finite family which brackets the exact moving cuts

Put $L=\log X$, choose an integer $D>A+3$, and let $\Delta=XL^{-D}$. On a fixed central ambient physical range containing $[\rho X,2(1-\rho)X]$ in its interior and contained in $[\rho X/2,2X]$, use an evenly spaced grid of step at most $\Delta$. The families of all frozen physical intervals $J,K$ with endpoints on this grid each have $O_\rho(L^{2D})$ members. Empty intervals are allowed. For each of the four exponents $u\in\{.38,.42,.08,.12\}$, add a separate grid of step at most $X^uL^{-D}$ covering $[X^u,2^uX^u]$ with one grid step to spare on each side. Taking endpoint choices independently gives frozen prime cofactor intervals $E,F$ below and above the four moving cuts, with $O(L^{2D})$ choices for each side. Altogether the frozen combinations $(J,K,E,F)$ number $O_\rho(L^{8D})$.

For each such combination form the actual transforms without any modulus-dependent unit mask:

$$
 A_{J,E}(\alpha)=
 \sum_{\substack{q\in E\\q\ {\rm prime}}}(\log q)
       \sum_{\substack{p\ {\rm prime}\\qp\in J}}e(\alpha qp),
 \qquad e(x)=e^{2\pi i x},
$$

and similarly $A_{K,F}$. Consider both assignments of the two types $E,F$ to the windows. All occurring prime ranges on opposite or same legs are disjoint by their fixed separated exponents: $q,s$ lie at scales between $X^{.08}$ and $X^{.42}$ in their separate bands, and the attached giant primes lie respectively in the exponent bands $[.58,.62]+O_\rho(1/L)$ and $[.88,.92]+O_\rho(1/L)$. Thus at a target $qp+sv=N$ all four primes automatically are units modulo $N$, since no constituent divides the opposite product. This remains true in the outer brackets.

Define the real profile on the ambient range by

$$
 G_E(t)=\sum_{\substack{q\in E\\q\ {\rm prime}}}\frac{\log q}{q\log(t/q)},
 \qquad V_{J,E}(\beta)=\int_J G_E(t)e(\beta t)\,dt.
$$

The bound $\sum_{p\le Y}(\log p)/p\ll\log(2Y)$ gives $G_E(t)\ll_\rho1$, and differentiation gives $G'_E(t)\ll_\rho (XL)^{-1}$. These bounds also apply to $F$. If a cofactor endpoint moves by one grid step, the corresponding pointwise profile difference is $O_\rho(L^{-D}+X^{-.08})$ by bounding the affected prime sum by the integer harmonic sum over that edge. If a physical endpoint moves by one grid step, the real convolution changes by $O_\rho(\Delta)$ at every target because the profile is bounded. These quantitative comparisons use neither short-interval primes nor averaged estimates.

## 2. Fixed frozen boxes: bilinear bound on small-major complementary arcs

Choose $P=L^M$ with fixed $M$ sufficiently large in terms of $A,B,D$. Introduce auxiliary classic arcs $\mathfrak D_X'$ with all reduced denominators $1\le r\le P$ and widths $P/(rX)$, and write $\mathfrak m_X'=\mathbb T\setminus\mathfrak D_X'$. These are not the exact R35 arcs. They are disjoint for large $X$ since the sum of widths times $rr'$ is at most $2P^2/X<1$. For $\alpha\in\mathfrak m_X'$ Dirichlet approximation yields $a/r$ reduced with $P<r\le X/P$, up to integer rounding, and $|\alpha-a/r|\le1/r^2$. One can take the Dirichlet parameter $\lceil X/P\rceil$, making the inclusion into a width-$P/(rX)$ arc exact for $r\le P$.

For one cofactor dyad $q\in[U,2U)$ let $V=X/U$, so the corresponding giant prime lies in a fixed proportional range around $V$. Apply Cauchy–Schwarz in $p$ and then sum over all integers $p$ in that proportional range. The intersection of the hard intervals in $p$ for two fixed $q,q'$ is again an interval, so geometric summation gives

$$
 |A_{J,E}^{(U)}(\alpha)|^2
  \ll_\rho V L^2 U
     \left[V+\sum_{1\le h\le 2U}\min(V,\|\alpha h\|^{-1})\right].
$$

For the stated approximation to $\alpha$, the points $\alpha h$ spaced within a block of at most $\lfloor r/2\rfloor$ successive integers $h$ are pairwise separated modulo 1 by at least $1/(2r)$. This follows from the reduced rational spacing and $|\alpha-a/r|\cdot|h-h'|\le1/(2r)$. Counting by distance from zero in each block therefore bounds the bracketed sum over $h$ by $O((1+U/r)(V+r\log(2r)))$. Hence

$$
 |A_{J,E}^{(U)}(\alpha)|^2\ll_\rho X^2 L^3
       (U^{-1}+V^{-1}+r^{-1}+r/X).
$$

In all the eligible frozen dyads $U,V$ are polynomial in $X$, while $r>P$ and $r/X\ll P^{-1}$. Summing the $O(L)$ dyads by the triangle inequality gives

$$
 \sup_{\mathfrak m_X'}|A_{J,E}|^2\ll_\rho X^2 L^5/P.
$$

The squared full-torus norm of either leg is $O_\rho(XL^2)$ by Parseval and the uniquely oriented representation of each index as a product of one small and one large prime. Thus, for fixed frozen $J,K,E,F$, Bessel on the **actual**, signed complementary coefficients gives

$$
 \sum_{n\in\mathbb Z}
 \left|\int_{\mathfrak m_X'} A_{J,E}(\alpha)A_{K,F}(\alpha)e(-n\alpha)\,d\alpha\right|^2
 \ll_\rho X^3 L^7/P .
$$

At threshold $X L^{-A-2}$, a union bound over both orientations and all grid choices fails on at most $O(X L^{8D+2A+11}/P)$ integers in $[X,2X]$. Taking $M>8D+2A+B+12$ makes this $O(XL^{-B})$. The bound is simultaneous over the frozen family, not over a single chosen window.

## 3. Major term for the same frozen family

For $r\le P$ and reduced $a$, all occurring $q,p$ exceed $r$, so multiplying the additive phase by $q$ permutes the unit residues of $p$ modulo $r$. The classical [Siegel–Walfisz prime progression theorem](https://link.springer.com/article/10.1007/BF01218882) gives, on the proportional $p$-range of length scale $V=X/q$, each hard prime progression discrepancy $O_{M,C,\rho}(V L^{-C})$ for arbitrarily large fixed $C$, uniformly for $r\le P$. Abel summation with $e(\beta qp)$ costs $O(1+P)$ since $|\beta|qV\le P$, and summing reduced residues costs at most $P$. The possible hard endpoint atoms are absorbed. Summing with $\log q$ times $V=X/q$ yields the true prime transform model

$$
 A_{J,E}(a/r+\beta)
     =\frac{\mu(r)}{\varphi(r)}V_{J,E}(\beta)+O_{\rho,M,C}(X P^2 L^{1-C})
$$

on each auxiliary arc. The factor $\mu(r)$ is the reduced additive sum, not a modulus-dependent approximation. Using $\operatorname{meas}(\mathfrak D_X')\ll P^2/X$ and the trivial bounds $O_\rho(X L)$ for each actual or model factor, choose $C>A+5M+30$ to make total major-product replacement $O_\rho(X L^{-A-3})$, uniformly in all the frozen choices.

After summing the reduced numerators the coefficient at $N$ is weighted by $\mu^2(r)c_r(N)/\varphi(r)^2$. Denote its absolute tail by

$$
 T_Y(N)=\sum_{r>Y}\frac{\mu^2(r)|c_r(N)|}{\varphi(r)^2}.
$$

The divisor identity gives $\sum_{n\le 2X}|c_r(n)|\le 2X\tau(r)$, hence

$$
 X^{-1}\sum_{n\in[X,2X]}T_Y(n)
   \ll\sum_{r>Y}\frac{\mu^2(r)\tau(r)}{\varphi(r)^2}
   \ll Y^{-1/2}.
$$

The second inequality is Rankin at $1/2$ and the convergent Euler product with local terms $1+2\ell^{1/2}/(\ell-1)^2$. Take $Y=\sqrt P$. Except on $O(XL^{A+3}P^{-1/4})$ integers one has $T_Y(N)\le L^{-A-3}$, so choosing also $M/4>A+B+5$ makes the exceptional count $O(XL^{-B})$.

Integration by parts at the original hard edges gives $|V_{J,E}(\beta)|\ll_\rho\min(X,|\beta|^{-1})$. Thus extension of the real integration beyond $P/(rX)$ has error $O_\rho(X r/P)$ per model pair; the full real product integral is $O_\rho(X)$. For $r\le\sqrt P$ use $r/P\le P^{-1/2}$ and the absolute Euler bound $\sum_r\mu^2(r)|c_r(N)|/\varphi(r)^2\ll S(N)$ on even $N$. For $r>\sqrt P$ use the tail $T_{\sqrt P}$ for both the extension and denominator completion. The complete signed series is exactly $S(N)$ by its ordinary Euler factors. The whole real integral is the convolution of the two hard profiles at $N$, namely

$$
 \int_{\mathbb R}V_{J,E}(\beta)V_{K,F}(\beta)e(-N\beta)\,d\beta
  =\int_{\substack{t\in J\\N-t\in K}}G_E(t)G_F(N-t)\,dt .
$$

Combining this major approximation, the Bessel exceptional count, and the other orientation yields the indicated signed full coefficient asymptotic for every frozen box simultaneously, with error $O_\rho(S(N)X L^{-A-2})$ on the good even moduli. The lower bound $S(N)\gg1$ for even $N$ absorbs the unscaled errors.

## 4. Restoring exact hard endpoints and the R43 comparator

On a good modulus choose inner and outer grid brackets of all the actual cuts, allowing an extra step if necessary for an included or excluded endpoint. An inner physical interval may be empty. The actual counts are nonnegative and contained between the respective frozen counts, with the automatic target unit masks already verified. The real convolutions of the upper and lower brackets differ by $O_\rho(X L^{-D}+X^{1-.08})$ by §1; this also controls the difference from the moving exact real integral. The lower and upper counts thus yield the same asymptotic for the exact moving hard rectangle and arbitrary $I$.

Finally the real models just used sum all primes in the cofactor bands. To recover exactly $\mathcal B_I(N)$ of R43, removing primes that divide $N$ and inserting $\lambda(q)\lambda(s)$ cost $O_\rho(X^{1-.08})$ in the real integral: the number of excluded primes above $X^{.08}$ is $O(1)$ and each carries $O(X^{-.08})$ pointwise weight, and $\lambda(q)-1,\lambda(s)-1=O(X^{-.08})$. This is negligible to every fixed logarithmic order. We have proved (1) with its stated uniformity and quantifiers.

Subtract the signed major evaluation of R43 on the exact R35 set from (1) to obtain (2) under global Dirichlet GRH. The auxiliary arcs used to prove the full-torus asymptotic need not be identified with the R35 arcs. In particular, this establishes genuine signed cancellation on the exact R35 complement for a density-one family in the stated dense rectangle, not for every even modulus. Since the unconditional full coefficient and the GRH major coefficient are each $O_{\rho,\kappa}(S(N)N)$ by the [unconditional full-target sieve](r41-source-unmasked-separated-cofactor-cells.md) and the [signed major evaluation](r43-source-dense-cell-positive-major-obstruction.md), it also gives a normalized squared mean $O_{\rho,\kappa}((\log X)^{-26})$ for the supremum over $I$ on this rectangle by taking $B>26$. No other parts of the weak-S operator are estimated by this result.
