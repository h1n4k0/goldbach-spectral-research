# Joint alias-power and mixed-denominator conductors

A pair can survive both separate power cuts and still have a small product of the two primitive conductors. The exact alias conjugacy and the partial denominator product allow this joint selection on the same two progression vectors. Summing the smaller of a literal alias count and a character-fiber count gives a gain without a shared-prime excess cutoff.

## 1. Exact sector and packet estimate

Use the genuine field $Z_{\rm all}$ retained in [R94](r94-operator-ungated-mixed-denominator-powers.md#1-the-same-selected-sector-with-no-excess-cutoff), with its complete even shell, actual parent profiles $h,f$, original common taper, $J^{-1}$ normalization, and high-denominator packet $\mathcal C_+(B,R)$. Keep the original local Dirichlet GRH at the shell targets and auxiliary Dirichlet GRH up to $\lceil8MB\rceil+2$, including modulus $1$. Keep all original ranges, the larger aliases $k>K\ge A/Q$, $(2k,b)<G$, the sharp raw cut $z,w>A$, and every earlier character selection and sign. As in R94 either raw input is allowed, with or without both exact parity removals, and with $K\ge2P$ in the former case.

For $q=2k,\ q'=qb$, write

$$
b=dm,\qquad d=b_\parallel,\quad m=b_\perp,\qquad
    r_b=\prod_{\substack{p\mid q\\p\nmid b}}p^{v_p(q)},\qquad
    q'=r_b m s .
 \tag{1}
$$

Here $d$ is the full part of $b$ on primes dividing $q$, and the last three factors are pairwise coprime, with $s$ supported on the common primes of $q,b$. For the two progression characters modulo $q'$, let $\alpha,\alpha'\bmod r_b$ and $\eta,\eta'\bmod m$ be their respective individual components on those two CRT factors. Fix $C>0,D\ge1$ and $V_Q=\lfloor(\log Q)^C\rfloor$. Delete from $Z_{\rm all}$ precisely the pairs satisfying

$$
\operatorname{cond}(\alpha^j)\,
             \operatorname{cond}(\eta^u(\eta')^v)\le D
   \quad\text{for some integers }1\le j,u,v\le V_Q,\qquad u\ne v .
 \tag{2}
$$

Conductors are primitive inducing conductors, including conductor one for the trivial factor. The incidence already forces $\alpha'=\bar\alpha$, so (2) is invariant under interchange of the two legs on every eligible pair. The two displayed conductor factors are on disjoint arithmetic moduli; this is not the earlier full product-character restriction.

Denote the resulting genuine field by $Z_{\rm joint}$, with the deletion before the original unequal numerator detunings. With $R_*=1+R$ and the packet norm of R94,

$$
\|Z_{\rm all}-Z_{\rm joint}\|_{\rm pkt}
 \ll_{\Gamma,\Theta,C,\epsilon} Q^\epsilon B\sqrt{MD}
       \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

It is valid for all denominator prime powers and after a fixed orthogonal spatial compression or restriction to a subset of the packet. The deletion may also be restricted to any alias subset fixed by $k,b$.

For the established scales $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, one can take the joint threshold $D=M$ in (3), giving $O_{\epsilon,C}(Q^{-3/800+\epsilon})$. In the version with both earlier parity removals the sharp $\widehat T,\widehat P$ comparisons remain $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm joint}$. This is an estimate of the deleted sector of the given packet. It gives no bound on the surviving covariance, another packet, an individual even modulus, or weak S.

## 2. True same-vector selection at fixed partial product

Fix $q,b$ and use the R94 partial product $\rho\bmod m$. In its coefficient in the original reduced numerator output, the only possible second $m$-character is $\eta'=\rho\bar\eta$, by R94 (6). Also $\alpha'=\bar\alpha$ by [R89 (5)](r89-operator-prime-to-denominator-alias-conductors.md#2-exact-forcing-of-a-pair-and-the-smaller-progression-norms). The latter forcing remains valid before projecting on full product characters: in the $q_0=qd$ incidence of R94, the local part of the rational phase at $r_b$ is constant on the congruence, and the unit congruence pairs each unit with a fixed signed unit multiple of it. The sum on that factor vanishes by character orthogonality unless the two $r_b$-characters are conjugate. Equivalently, the R82 lift-product support applied to the $q_0$ incidence at denominator $d$ enforces the same condition. Thus this is forcing for each partial-product coefficient vector, not a statement relying on cancellations among different $\rho$'s.

In the eligible $\rho$-coefficient (2) becomes the single-leg subset

$$
\mathcal L_{r_b,m}(\rho)=
 \left\{(\alpha,\eta):
 \operatorname{cond}(\alpha^j)\,
      \operatorname{cond}(\eta^{u-v}\rho^v)\le D
           \text{ for some }j,u,v\text{ as in (2)}\right\}.
 \tag{4}
$$

It is preserved by the involution $(\alpha,\eta)\mapsto(\bar\alpha,\rho\bar\eta)$: the alias factor is invariant under conjugation, and the denominator condition after interchanging the two legs uses the swapped exponent pair $(v,u)$. The R94 retained mixed condition is the complement of its earlier product-dependent subset on $m$, and is invariant under the same $\eta$ involution. At fixed $\rho$, restrict the actual progression vector first by all [the original individual cuts](r92-operator-individual-denominator-power-conductors.md#1-exact-input-and-conclusion), then by this R94 retained subset, and then by (4). This is the **same** fixed projected progression vector on the two raw legs. Indeed every original matched pair is either selected on both or on neither by each of the last two cuts; all original individual projections still act on both legs as originally prescribed. Thus this implements the desired additional deletion exactly, not a bilinear multiplier asserted to be contractive for arbitrary pair masks.

Write $r=r_b$. At fixed $\rho,j,u,v$, the image map

$$
(\alpha,\eta)\longmapsto(\alpha^j,\eta^{u-v}\rho^v)
 \tag{5}
$$

is a translate of a homomorphism on the character group modulo $rm$. Since $(r,m)=1$, the conductor of the character corresponding to the displayed pair is the product of its component conductors, by CRT and the definition of primitive induction. There are at most $D\tau(rm)$ characters modulo $rm$ with conductor $\le D$, by summing the bound $\phi(c)\le D$ over the possible conductor divisors $c\le D$. The fibers in (5) have size at most $T_j(r)T_{|u-v|}(m)$, where $T_a(n)=|\ker(\chi\mapsto\chi^a)|$ for $a>0$. Negative exponents have the same kernels up to inversion, and $T_a(1)=1$. Allow every character on $s$ in (1), so the fraction of all full progression coefficients in the desired projected vector is at most

$$
f(r,m)=\min\!\left(1,\,
       \frac{D\tau(rm)}{\phi(r)\phi(m)}
         \sum_{\substack{1\le j,u,v\le V_Q\\u\ne v}}
                    T_j(r)T_{|u-v|}(m)\right).
 \tag{6}
$$

This bound is uniform in $\rho$ and valid also with all earlier cuts; the empty exponent range gives no terms. For the genuine projected vector the squared pointwise bound and the squared integrated increment bound [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference) therefore have factors $f(r,m)$ in place of $f(m)$ in R94 (8). This uses normalized residue Parseval: the number of allowed coefficients is at most $\phi(q')f(r,m)$, and the same auxiliary Dirichlet GRH gives the uniform individual character estimates.

Keep the full R82/R91 product and product-power masks as the conditional orthogonal projection on $a_d$ at fixed $\rho$, as in R94 §3. The estimate R94 (7) there applies to arbitrary complex residue vectors, so the additional leg projection, fixed for the actual $q,b,\rho$ and independent of the raw variables, does not change it. In the difference orientations the same numerator involution $L(a_d)\mapsto\rho(-1)L(-a_d)$ splits the projected form into symmetric and skew complex bilinear forms; neither the full product projection nor the new leg subset changes this involution. In particular the R94 common-test cosine argument uses the same selected vector in both raw legs, and its skew argument uses that same vector on the common restricted raw interval. Both use the squared increment bounds just proved, and the other terms and the signed sum orientation use the pointwise bounds. For the parity-reduced input the two sharp parity pieces are treated by the same reflected derivative kernels, not by introducing a marginal cancellation after sharp clipping. The leg parity projections commute with (4) and the earlier fixed character selections, since residue reflection is diagonal in characters. Extracting $\rho$ and applying its fixed full product projection preserves the true equality of the reflected incidence on an auxiliary-even leg.

It follows from R94 §4, with this replacement of the squared estimates, that for a common test $\omega$ the complete joint reduced numerator HS cost per eligible $k,b$, after Parseval in $a_m$, is at most

$$
Q^\epsilon b f(r_b,m)
       [K_1+QK'_2]
 \tag{7}
$$

up to the optional additional $O_\epsilon(Q^\epsilon b f(r_b,m)(QP/k)(E_\infty+E_1))$. Here $K_1=\|\omega\|_\infty+\|\omega'\|_1,\ K'_2=\|\omega''\|_1+K_1/Q$ and $E_\infty,E_1$ are those in R94 (10). Their parameters and the exact earlier parity overlap rule do not change. To see the numerator cost explicitly, R94 (7) uses a joint bound $Q^\epsilon d$ for each partial product, and the squared norm of its common vector now contributes $f(r_b,m)$. Multiplicative Parseval on $m$ and the at most $\phi(m)$ possible partial products then cost a total $\phi(m)$, so $d\phi(m)\le b$. No interchange with unequal numerator detuning is used.

## 3. Joint alias and denominator counting

For fixed $b$ group its eligible $k\le4M$ by the unitary divisor $d=b_\parallel$, and set $m=b/d$. Let $F_{b,d}$ be the sum of $f(r_b,m)$ over this group. First $f\le1$ and $\operatorname{rad}(d)\mid2k$, so

$$
F_{b,d}\ll M/\operatorname{rad}(d).
 \tag{8}
$$

This includes $d=1$, and when the radical is too large the group is empty. It does not change the real support or signs of the field. Second, for each $r_b=r\le8M$ the multiplicity of $k$ is $O_\epsilon(Q^\epsilon)$: $2k/r\le8M$ has all its prime factors in $b$, and the uniform Rankin count in R89 §4 applies. Drop the gates only for this positive count. Let

$$
H(m)=\sum_{1\le a\le V_Q}T_a(m).
$$

On the polynomial scales $\tau(rm),r/\phi(r),m/\phi(m)\ll_\epsilon Q^\epsilon$. Sum the second bound in (6) over $r$, allowing all $r\le8M$, and use [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) on each $T_j(r)/r$. For any difference order $a$ the number of $(u,v)$ with $|u-v|=a$ is at most $2V_Q$. Including the subpower number of choices of $j$ and the multiplicity just proved yields

$$
F_{b,d}\ll_{\Theta,C,\epsilon} Q^\epsilon D H(m)/m,
       \qquad
       \sum_{m\le B}H(m)/m\ll_{\Theta,C,\epsilon}Q^\epsilon .
 \tag{9}
$$

The last bound uses the same R90 positive harmonic estimate at the polynomial cutoff $B$, [as in R93](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms). No summation over the true $\rho$-dependent selected sets occurs in this positive harmonic upper count.

At each $b$ use $P/k\le1/2$ if needed in (7). The common-test cost after summing aliases then has factor $Q^\epsilon b\sum_{d\mid b,\ (d,b/d)=1}F_{b,d}$. Square this factor first by Cauchy over the at most $\tau(b)$ unitary divisors. The smaller of (8) and (9) is available for each $F_{b,d}$, and its square is at most the product of the two upper bounds. Thus, enlarging only the positive upper sum to every factorization $dm\le B$,

$$
\begin{split}
 \sum_{b\le B} b^2
        \left(\sum_{\substack{d\mid b\\(d,b/d)=1}}F_{b,d}\right)^2
   &\ll_{\Theta,C,\epsilon}Q^\epsilon B^2 M D
       \sum_{d\le B}\frac1{\operatorname{rad}(d)}
       \sum_{m\le B}\frac{H(m)}m \\
   &\ll_{\Theta,C,\epsilon} Q^\epsilon B^2 M D .
 \end{split}
 \tag{10}
$$

For the radical sum use the positive finite Euler product $\prod_{p\le B}(1+E_p/p)$ with $E_p=\lfloor\log B/\log p\rfloor$. For $p\le\sqrt{\log Q}$, the sum of local logarithms is $O_\Theta(\sqrt{\log Q}\log\log(3Q))$. For larger primes use $E_p\ll_\Theta\log Q/\log p$ and
$\sum_{p>x}(p\log p)^{-1}\ll 1/\log x$, by elementary Chebyshev bounds and partial summation as in [R91 §4](r91-operator-denominator-product-power-conductors.md#4-sum-over-all-actual-denominator-types-and-restore-the-packet). This contributes $O_\Theta(\log Q/\log\log Q)=o(\log Q)$. In particular the radical sum is subpower for arbitrary, not only squarefree, denominators. Choose smaller intermediate $\epsilon$'s to absorb all subpower weights.

Now use the exact common Taylor tests of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field). The original numerator-specific coefficients have magnitude at most $2^{-n}$ in Taylor order $n$, the exterior phases have modulus one, and all restrictions above act before them. At offset $\ell$, the weighted common $K_1$ is $O(1+|\ell|)$, and the corresponding $K'_2,E_\infty,E_1$ are $O(S^{-1}+(1+|\ell|)^2/Q)$, as in R94 §4. Divide by $J\asymp Q$, square-sum over $|\ell|\le R+1$, and apply (10). The three offset factors are $R_*^{3/2},R_*^{5/2},R_*^{1/2}$, giving (3) with all original Taylor weights, rounding choices and detunings. At $D=M$ the three exponents in (3) are $-1/160,-3/800,-19/4000$, respectively. Every original independently estimated sharp or model term is unchanged, which proves the stated sharp comparison by the triangle inequality.

## 4. A genuine additional pair

In the established numerical setting take $d=2^e\asymp Q^{7/25}$, an odd prime $m\asymp Q^{11/100}$ with $b=dm$ in the high denominator band, and $k=r\asymp Q^{9/20}$ an odd prime. Choose the primes by Bertrand's postulate. Then $(2k,b)=2<G,\ r_b=r,\ k>K$. At $r$ choose a generator-order character and its conjugate. Every earlier allowed alias power retains conductor $r>Q^{81/200}$. At the shared factor $2^{e+1}$, choose a conjugate primitive pair as in R94 §5, with principal local product and nonzero incidence of magnitude $2^{e+1}$.

On $m$, choose a generator $\eta$ and let $\eta'=\eta^t$, with $t=2V^*$ and $V^*$ the maximum of the finitely many polylogarithmic exponent cutoffs here and in the earlier cuts. For all earlier individual powers, product powers, and mixed denominator powers of the two legs, the exponent in this generator is positive and $O((V^*)^2)<m-1$ for large $Q$. Thus these conductors are all $m$, above the earlier thresholds. Both original coprime Gauss factors are nonzero. The conductor threshold (2) holds with $j=1,u=2,v=1$ for large $Q$, since $rm\asymp Q^{14/25}<Q^{3/5}=D$. This yields an eligible, nonzero original incidence coefficient newly selected after all earlier cuts for the unmodified input. It is not a lower bound on the integrated packet field.
