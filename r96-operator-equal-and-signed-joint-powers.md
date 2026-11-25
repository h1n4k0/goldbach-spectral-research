# Equal and signed mixed powers in the joint conductor cut

Allowing opposite signs detects low ratio powers that are invisible to the positive-exponent cut. Allowing equal exponents adds a different sector: the second conductor then belongs to the partial product itself, and the conditioned leg count can be large for some products. Taking its average only after the correct partial-product Parseval, then using Cauchy over the actual aliases, bounds both additions at the same rate.

## 1. Exact enlargement and packet bound

Use the true field $Z_{\rm joint}$ retained by [R95](r95-operator-joint-alias-and-mixed-denominator-conductors.md#1-exact-sector-and-packet-estimate), with all original selections and signs on the complete even shell, its real-parameter taper, true parent profiles $h,f$, original $J^{-1}$ normalization, and high-denominator packet $\mathcal C_+(B,R)$. As there, assume original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Keep all original ranges, $k>K\ge A/Q$, $(2k,b)<G$, and $z,w>A$. Either input of R95 is allowed, with or without the exact R86/R87 parity removals and with $K\ge2P$ in the former case.

At fixed $q=2k,b$ use the R95 CRT

$$
b=dm,\qquad d=b_\parallel,\quad m=b_\perp,\qquad
     q'=qb=r_b m s ,
 \tag{1}
$$

where $r_b$ is the full part of $q$ coprime to $b$, the factors $r_b,m,s$ are pairwise coprime, and $s$ is supported on the shared primes. Write $\alpha,\alpha'\bmod r_b$ and $\eta,\eta'\bmod m$ for the two leg components. Fix $D\ge1,C>0$ and $V_Q=\lfloor(\log Q)^C\rfloor$. In $Z_{\rm joint}$ omit the remaining pairs satisfying

$$
\operatorname{cond}(\alpha^j)
       \operatorname{cond}(\eta^u(\eta')^v)\le D
 \quad\text{for some integers }1\le j\le V_Q,\quad
       1\le |u|,|v|\le V_Q .
 \tag{2}
$$

Both $u=v$ and opposite signs are allowed. All conductors are primitive inducing conductors, with conductor one on the trivial factor. The earlier R95 deletion remains in force, so (2) is an incremental deletion even on its overlapping exponent triples. There are no altered profiles, raw masks, signs, benchmark terms, or numerator detunings.

Denote the resulting field by $Z_{\rm signed}$. With $R_*=1+R$ and the packet norm of R95,

$$
\|Z_{\rm joint}-Z_{\rm signed}\|_{\rm pkt}
    \ll_{\Gamma,\Theta,C,\epsilon} Q^\epsilon B\sqrt{MD}
       \left[\frac{R_*^{3/2}+R_*^{5/2}}Q
                           +\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

The deletion may be restricted to a subset fixed by $k,b$, and the estimate is also valid after fixed orthogonal spatial compression or restriction to a subset of the packet. It permits all denominator prime powers.

Take $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250},\ D=M$, and both the earlier R95 cutoff and every other scale as in the R95 example. Then (3) is $O_{\epsilon,C}(Q^{-3/800+\epsilon})$. The post-R86/R87 sharp $\widehat T,\widehat P$ comparisons still have $O_{\epsilon,C}(Q^{-1/500+\epsilon})$ error to $Z_{\rm signed}$. Neither bound estimates the surviving covariance, other packets, an individual even modulus, or weak S.

## 2. Exact conditioning and the averaged character count

In the R94 partial-product coefficient $\rho\bmod m$, one has $\eta'=\rho\bar\eta$, and the original alias incidence already forces $\alpha'=\bar\alpha$ before any full product projection, by R95 §2. Thus (2), at fixed $\rho,r=r_b,m$, is a subset of $(\alpha,\eta)$ described by

$$
\operatorname{cond}(\alpha^j)
          \operatorname{cond}(\eta^{u-v}\rho^v)\le D
                      \quad\hbox{for a triple in (2)}.
 \tag{4}
$$

It is invariant under $(\alpha,\eta)\mapsto(\bar\alpha,\rho\bar\eta)$. Indeed the first conductor is unchanged by conjugation, and swapping $u,v$ in the original two-leg formula keeps the union unchanged, with or without equal exponents. The earlier R94 complement is invariant under the same partner map on $m$, and the earlier R95 complement is invariant on $(\alpha,\eta)$. Consequently (4) is imposed by exactly the same projected progression vector on both raw legs at fixed $q,b,\rho$, after the earlier projected supports. No pair-dependent incidence bound is assumed. The original high **full-product** masks remain the orthogonal projection in the $a_d$-vector conditioned on $\rho$, as in [R94 §3](r94-operator-ungated-mixed-denominator-powers.md#3-exact-selections-and-the-conditional-raw-estimates).

Let $g_\rho(r,m)$ be the fraction of all $(\alpha,\eta)$ on the coprime factors $r,m$ satisfying (4), *before* counting any earlier restrictions, and write

$$
g(r,m)=\frac1{\phi(m)}\sum_{\rho\bmod m} g_\rho(r,m),
                 \qquad 0\le g_\rho(r,m),g(r,m)\le1 .
 \tag{5}
$$

The actual earlier restrictions only decrease these fractions. For $h\ge1$ define $T_h(n)=|\ker(\chi\mapsto\chi^h)|$ on the character group of $n$, and $T_h(1)=1$. Put $H(n)=\sum_{1\le h\le2V_Q}T_h(n)$. We prove

$$
g(r,m)\ll_{\Theta,C,\epsilon}
                     Q^\epsilon\frac{D H(r) H(m)}{rm}.
 \tag{6}
$$

If $V_Q=0$, the deleted set is empty. The bounds below use fixed polynomial parameter ranges for $r,m$.

For a fixed triple with $u\ne v$, the translated map $(\alpha,\eta)\mapsto(\alpha^j,\eta^{u-v}\rho^v)$ has fibers of size at most $T_j(r)T_{|u-v|}(m)$. This is true for both signs of $u-v$, because inversion of a character is a bijection. The displayed image is a character on $rm$ by CRT with conductor the product of the two component conductors. There are at most $D\tau(rm)$ images of conductor $\le D$, by summing the number of inducing primitive characters over divisor conductors $c\mid rm,c\le D$. Hence the corresponding fraction at each fixed $\rho$ is at most $D\tau(rm)T_j(r)T_{|u-v|}(m)/(\phi(r)\phi(m))$, uniformly in $\rho$.

For a fixed equal pair $u=v\ne0$, the second factor in (4) is $\operatorname{cond}(\rho^u)$, and imposes no condition on $\eta$. The conditional fraction for that triple is now the number of allowed $\alpha$'s divided by $\phi(r)$. Average this fraction over $\rho\bmod m$ before bounding it. The map on $(\alpha,\rho)$ sending it to $(\alpha^j,\rho^u)$ has fibers of size at most $T_j(r)T_{|u|}(m)$, and the same $D\tau(rm)$ count of potentially attained images. Its contribution to (5) is at most $D\tau(rm)T_j(r)T_{|u|}(m)/(\phi(r)\phi(m))$. This is an averaged statement, not a claim of uniform smallness at each $\rho$. Combining the two bounds by the union estimate and absorbing the subpower exponent multiplicities, $\tau(rm)$, and $rm/(\phi(r)\phi(m))$ proves (6).

## 3. Weighted partial-product Parseval and the actual alias sum

At fixed $q,b,\rho$, allow every character on the third factor $s$ of (1) in the support count. The projected genuine vector thus uses at most $\phi(q')g_\rho(r_b,m)$ of the full progression characters. The uniform pointwise GRH bound and the per-character incremental estimate [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference) with normalized residue Parseval give both squared bounds with the factor $g_\rho(r_b,m)$. These are for the actual centered progression vector, not a proxy or an estimate of a product of raw coefficients by a mean support size.

In the finite numerator space $\ell^2(a_d)$ at fixed $\rho$, R94 (7) holds on arbitrary complex vectors, including the corresponding raw Fourier transforms. All character restrictions are fixed in the raw coordinates. The original two difference orientations retain the exact transpose relation with the involution $L(a_d)\mapsto\rho(-1)L(-a_d)$. The conditional full-product projection and the two eigenspace projections are contractions and commute. Therefore the fixed common test proof of R94 §4 applies with the squared-norm factor $g_\rho(r_b,m)$ in place of $f(m)$, since the actual leg vector is the same on both raw sides. This applies to both the cosine marginal identity and the skew raw translation argument; the sum orientation keeps its original negative sign. For the optional parity-reduced input, apply those same pointwise bounds to the two reflected R86/R87 derivative pieces and subtract them with the original overlap convention. The fixed character restrictions commute with residue reflection and auxiliary parity projections; no marginal identity is asserted on their sharp raw masks.

In particular, at each $\rho,k,b$ the conditional joint HS bound is $O_\epsilon(Q^\epsilon d g_\rho(r_b,m)\mathcal K)$, where $\mathcal K=K_1+QK'_2$ for the common test of R94 §4, and $\mathcal K$ can be enlarged by $Q(E_\infty+E_1)$ in the parity-reduced input since $P/k\le1/2$. The traditional $QP/k$ factor is within that enlargement. Now apply multiplicative Parseval in the $m$ numerator dimension without taking a uniform supremum over $\rho$. Since the norm uses counting measure, the $\ell^2$ aggregate of the preceding coefficients gives the complete numerator bound

$$
\begin{split}
   O_\epsilon\!\left(Q^\epsilon d\sqrt{\phi(m)
                         \sum_{\rho\bmod m}g_\rho(r_b,m)^2}\,\mathcal K\right)
       &\le O_\epsilon\!\left(Q^\epsilon d\phi(m)
                                       \sqrt{g(r_b,m)}\,\mathcal K\right)\\
       &\le O_\epsilon\!\left(Q^\epsilon b
                                       \sqrt{g(r_b,m)}\,\mathcal K\right).
 \end{split}
 \tag{7}
$$

Here $g_\rho^2\le g_\rho$ is used only after computing the genuine conditional numerator bounds. In particular the factor in (7) is $\sqrt g$, not $g$. This estimate is still before the different numerator detunings.

For fixed $b$ group the actual $k\le4M$ by their unitary divisor $d=b_\parallel$, so $m=b/d$ within the group, as in R95 §3. There are $O(M/\operatorname{rad}(d))$ aliases in it because $\operatorname{rad}(d)\mid2k$. For fixed $r_b=r\le8M$, their multiplicity is $O_\epsilon(Q^\epsilon)$ by the [R89 Rankin count](r89-operator-prime-to-denominator-alias-conductors.md#4-count-the-actual-aliases-then-restore-the-fourier-packet), since $2k/r$ is supported on primes of $b$ and at most $8M$. The original gates can be dropped in these positive bounds, but not in the field. Equation (6) and the [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) harmonic power-fiber estimates yield

$$
\sum_{\substack{k\ {\rm actual}\\d(k,b)=d}}g(r_b,m)
        \ll_{\Theta,C,\epsilon}Q^\epsilon D H(m)/m,\qquad
       \sum_{m\le B} \frac{H(m)}m\ll_{\Theta,C,\epsilon}Q^\epsilon .
 \tag{8}
$$

The latter uses a polynomial cutoff $B$; extending the individual exponent range from $V_Q$ to $2V_Q$ fits another fixed log power. Define $L_{b,d}=\sum_{k:\,d(k,b)=d}\sqrt{g(r_b,m)}$ over the actual group. Cauchy over its aliases and (8) give

$$
L_{b,d}^2\ll_{\Theta,C,\epsilon}Q^\epsilon
             \frac{M}{\operatorname{rad}(d)}\,\frac{D H(m)}m .
 \tag{9}
$$

This replaces the minimum-of-two-bounds estimate in R95. Now Cauchy over the at most $\tau(b)$ unitary divisors and enlarge from unitary to arbitrary $dm\le B$ in the positive upper sum:

$$
\sum_{b\le B} b^2
        \left(\sum_{\substack{d\mid b\\(d,b/d)=1}}L_{b,d}\right)^2
 \ll_{\Theta,C,\epsilon} Q^\epsilon B^2 M D
          \sum_{d\le B}\frac1{\operatorname{rad}(d)}
          \sum_{m\le B}\frac{H(m)}m
 \ll_{\Theta,C,\epsilon} Q^\epsilon B^2 M D .
 \tag{10}
$$

The radical sum is the same subpower estimate for arbitrary prime powers proved in R95 (10). A restriction on the alias subset fixed by $k,b$ only lowers the positive upper bounds here.

Finally use the exact common Taylor tests of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field), including the original differing factorial-series coefficients and unit-modulus outside phases. At integer offset $\ell$, their weighted common $K_1$ is $O(1+|\ell|)$ and the other weighted seminorms are $O(S^{-1}+(1+|\ell|)^2/Q)$, as in R94. Division by $J\asymp Q$, the squared offset sums $|\ell|\le R+1$, and (10) give (3). Nothing was moved past the numerator-specific detuning. The sharp packet comparison follows with the unchanged separate errors of R95.

## 4. Nonzero incidence in both additional sectors

For the numerical example with $D=M$ both here and in R95, choose odd primes $r=k\asymp Q^{9/20}$ and $m\asymp Q^{9/50}$, and take $d=2^e\asymp Q^{21/100}$ with the prime $m$ chosen so $b=dm$ is in the high band. This is possible by Bertrand's postulate. Then $q=2r,\ r_b=r,\ (2k,b)=2<G,\ k>K$, and $rm\asymp Q^{63/100}>Q^{3/5}=D$. On $r$ take a generator-order character and its conjugate, so all the permitted small alias powers have conductor $r>Q^{81/200}$.

For the **equal-power** example, on $m$ choose a generator $\eta$ and $\eta'=\bar\eta$, so $\rho=1$. Every nonzero signed unequal exponent difference in the range is nonzero modulo $m-1$ for large $Q$, so all these mixed powers have conductor $m$. The individual small powers keep conductor $m$ as well. Thus the R94 unequal cut is avoided, and no signed unequal joint condition, including the entire preceding R95 condition, can hold because $rm>D$. But $u=v=1$ gives the principal character on $m$, so (2) holds with $j=1$.

For this example the earlier full product is kept high by the shared factor. Use the same primitive character $\chi_2\bmod 2^{e+1}$ on both legs there, with $\chi_2(-1)=1$ and $\chi_2(5)$ of order $2^{e-1}$, using the usual decomposition into the sign and $5$-generated unit factors. The square induces a character on $2^e$ of conductor $2^e$. For any allowed positive exponent $w$ the conductor of $(\chi_2^2)^w$ is $2^{e-v_2(w)}$ for sufficiently large $Q$: its value on $5$ has order $2^{e-2-v_2(w)}$ and the sign value is still one. Hence the original full product and all its allowed powers exceed the [earlier R82/R91 conductor cutoffs](r91-operator-denominator-product-power-conductors.md#1-exact-setting-and-bound). The local incidence here has congruence modulo $2$, automatic for two odd unit residues with either sign. The two separate primitive additive Gauss factors on $2^{e+1}$ are both nonzero. The alias factor at $r$ and the coprime additive Gauss factors at $m$ are nonzero as well. This pair is truly added by the equal powers even if all signed unequal powers are applied first.

For a distinct **opposite-sign** example, keep $r,m,d$ but set $\eta'=\eta$. All previous positive powers on $m$ have positive exponent $u+v$ less than $m-1$ for large $Q$, so keep conductor $m$ and again $rm>D$. The full product has a generator-square $m$-component and all its small powers also retain conductor $m$, so the shared leg can use the conjugate primitive pair of R94 §5. Each local incidence is still nonzero. Now $u=1,v=-1$ gives the principal character on $m$, meeting (2) with $j=1$. These examples apply to the unmodified input; they prove strict selector eligibility, not a lower bound for the integrated packet field.
