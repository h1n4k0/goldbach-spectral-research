# Unequal mixed powers on the actual coprime-denominator legs

Fixing the true product character turns a mixed power of the two individual characters into a translated power of one character. An exact finite Fourier restriction at the primes shared by alias and denominator is sufficient to use that sparsity on the whole squarefree-denominator subpacket, and more generally on an explicit alias sector of the original packet. This removes a part of the true signed field left by the preceding individual, alias and product power cuts.

## 1. Exact sector and bound

Use the genuine [R92 retained field](r92-operator-individual-denominator-power-conductors.md#1-exact-input-and-conclusion) $Z_{\rm ind}$ on the complete even shell with its common taper, original $J^{-1}$, actual transported parent profiles $h,f$, and original high-denominator packet $\mathcal C_+(B,R)$. As there, assume original local Dirichlet GRH at the shell targets and auxiliary Dirichlet GRH up to $\lceil8MB\rceil+2$, including modulus $1$. Keep the range $Q\le A\le QH/100,\ A/Q\le K\le4M,\ k>K$ and both inputs of R92: with or without the exact [R86](r86-operator-long-alias-short-leg-even.md#3-bound-the-integrated-difference-at-a-fixed-alias)/R87 parity deletions (and with $K\ge2P$ for the former). Keep all prior individual, alias and product selectors, $(2k,b)<G$, and $z,w>A$.

For fixed $k,b$, put $q=2k,\ q'=qb$ and take the same CRT decomposition $b=d\,m,\ d=\prod_{p\mid q}p^{v_p(b)}$, so $(qd,m)=1$. Let $\eta,\eta'\bmod m$ be the two individual components of the genuine characters $\xi,\xi'\bmod q'$ on this coprime denominator factor. Fix $C>0,D_{\rm mix}\ge1,Z\ge1$, let $V_Q=\lfloor(\log Q)^C\rfloor,\ R_*=1+R$, and define

$$
\mathfrak e(q,b)=\frac{d}{(q,d)}.
 \tag{1}
$$

From $Z_{\rm ind}$, delete a pair only at aliases with $\mathfrak e(q,b)\le Z$, and only when

$$
\operatorname{cond}(\eta^u(\eta')^v)\le D_{\rm mix}
       \quad\hbox{for some integers }1\le u,v\le V_Q,\quad u\ne v .
 \tag{2}
$$

The test (2) is symmetric in the legs. Conductors are primitive inducing conductors, with conductor one on the trivial factor. Denote the resulting exact field by $Z_{\rm mix}$; the deletion is applied before the unequal numerator detunings. With the packet norm of R92,

$$
\|Z_{\rm ind}-Z_{\rm mix}\|_{\rm pkt}
 \ll_{\Gamma,\Theta,C,\epsilon} Q^\epsilon B\sqrt{Z D_{\rm mix}}\,M
       \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

The same bound holds after a fixed orthogonal spatial compression or restriction to a subset of the packet. On squarefree denominators every alias has $\mathfrak e(q,b)=1$, so $Z=1$ deletes all the relation pairs there. Even for $Z=1$, repeated primes in the denominator are allowed when they are coprime to $q$ or their exponents in $q$ are at least those in $b$. The condition in (1) thus gates aliases, not necessarily whole denominators.

At the R92 parameters $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, take $D_{\rm mix}=Q^{3/1000}$. Then (3) gives $O_{\epsilon,C}(Q^{-9/4000+\epsilon})$ when $Z=1$; even with $Z=Q^{1/2500}$ it gives $O_{\epsilon,C}(Q^{-41/20000+\epsilon})$. For the input with both earlier parity deletions the inherited sharp $\widehat T,\widehat P$ comparison therefore remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$ in these examples, now to $Z_{\rm mix}$. This is not a bound on the covariance of the remaining pairs, on a prescribed even modulus, on other packets, or on weak S.

## 2. A shared-prime restriction of the exact Gauss factor

Fix $q,b$ and one original orientation $\sigma=(\sigma_1,\sigma_2)$. For units modulo $q'$ the actual incidence from [R82 (4)](r82-operator-low-product-character-long-quotient.md#2-exact-dependence-on-the-product-of-the-two-characters) sums $\overline{\xi(r)}\overline{\xi'(s)}$ with $q\mid\sigma_1r+\sigma_2s$ and $e(-a(\sigma_1r+\sigma_2s)/q')$ for a reduced numerator $a\bmod b$. Write $e(x)=e^{2\pi i x}$. By R82 (5)–(6) it vanishes unless the full character product is the lift of a unique $\nu\bmod b$; if so its numerator dependence is exactly a constant times $\nu(a)$. The constant is the incidence at $a=1$, interpreted in the unique class for $b=1$. This support assertion holds before any of the power selections.

For an eligible pair factor that constant by CRT into prime powers. At a prime with $p^a\parallel q,\ p^e\parallel b,\ a,e\ge1$, write $A_p$ for the unit CRT factor of the numerator at $p^{a+e}$ (the inverse of $q'/p^{a+e}$ modulo this prime power). The local admissible $s$ are parameterized uniquely by

$$
s=-\sigma_1\sigma_2r(1+p^a x)\pmod {p^{a+e}},
                         \qquad x\bmod p^e ,
$$

for each unit $r\bmod p^{a+e}$. They are all units. The affine combination in the exponential is $-\sigma_1r p^a x$ modulo $p^{a+e}$. Denote local character factors by the same letters with subscript $p$. Then the exact local coefficient is

$$
C_p=\bar\xi'_p(-\sigma_1\sigma_2)
       \frac{\phi(p^{a+e})}{\phi(p^e)}
       \sum_{r\bmod p^e}^{*}\bar\nu_p(r)\,
                            T(A_p\sigma_1 r),\qquad
 T(c)=\sum_{x\bmod p^e}\bar\xi'_p(1+p^a x)e(cx/p^e).
 \tag{4}
$$

The ratio $\phi(p^{a+e})/\phi(p^e)$ comes from reducing the unit $r$, since its character factor is the full lifted product and the displayed phase depends only on this smaller residue.

Set $h_0=\min(a,e)$. Translation of $x$ by $p^{e-h_0}j$ multiplies $1+p^a x$ by
$1+p^{a+e-h_0}j(1+p^a x)^{-1}$ modulo $p^{a+e}$.
The inverse in this expression is $1\bmod p^{h_0}$ because $a\ge h_0$. The subgroup $1+p^{a+e-h_0}j$ has the additive law in $j\bmod p^{h_0}$, since $a+e-h_0\ge h_0$. Therefore $\xi'_p(1+p^{a+e-h_0}j)=e(\kappa j/p^{h_0})$ for some integer $\kappa\bmod p^{h_0}$, independent of $x$. After translation the summand of $T(c)$ is multiplied by $e((c-\kappa)j/p^{h_0})$. It follows that $T(c)=0$ unless $c\equiv\kappa\bmod p^{h_0}$, including at the prime $2$. This argument does not assume $\kappa$ is a unit; if it is nonunit there is no contribution to the unit sum in (4).

The unconditional finite Parseval identity is $\sum_{c\bmod p^e}|T(c)|^2=p^{2e}$, since the original character values all have modulus one. There are at most $p^{e-h_0}$ supported frequencies in (4), as $A_p\sigma_1$ permutes the units. Cauchy and (4) give

$$
|C_p|\le\phi(p^{a+e})\frac p{p-1}\,p^{(e-h_0)/2}.
 \tag{5}
$$

At a prime dividing $q$ only, the phase is constant on the congruence, and the unit sum is bounded by $\phi(p^a)$. At a prime dividing $b$ only, the two unit coordinates are unrestricted relative to one another. The local coefficient is the product of two single Gauss factors at primitive additive frequency, each bounded by $\sqrt{p^e}$ by the imprimitive computation of [R81 §2](r81-operator-low-conductor-long-quotient.md#2-exact-local-power-vanishing-and-the-low-conductor-fourth-moment). Thus its absolute size is at most $p^e=\phi(p^e)p/(p-1)$. Multiplying the exact local factors, using $\prod_{p\mid b}p/(p-1)\ll_\epsilon Q^\epsilon$, proves for the coefficient of $\nu(a)$ in every eligible original pair

$$
|C_{\xi,\xi'}|\ll_\epsilon Q^\epsilon\phi(q')\sqrt{\mathfrak e(q,b)} .
 \tag{6}
$$

This also covers the trivial coprime factors. In particular at squarefree $b$ there is no shared-prime power loss, even if $q$ shares every prime of $b$.

## 3. Condition on the true product before taking norms

Fix $\nu\bmod b$ retained by R91, and use $\pi:(\mathbb Z/q'\mathbb Z)^\times\to(\mathbb Z/b\mathbb Z)^\times$ for reduction. The only possible partner is $\xi'=(\nu\circ\pi)\bar\xi$, so on $m$ one has $\eta'=\nu_m\bar\eta$. In particular (2) for this fixed product is

$$
\operatorname{cond}(\eta^{u-v}\nu_m^v)\le D_{\rm mix}
                          \quad\hbox{for some }u,v\text{ as in (2)}.
 \tag{7}
$$

Let $\mathcal L_m(\nu_m)$ be this subset of the $m$-character group. The map $\eta\mapsto\nu_m\bar\eta$ preserves the subset, since the original union in (2) includes both exponent orders. Write $T_j(m)=|\ker(\chi\mapsto\chi^j)|$ for positive integers $j$. For a single exponent pair the number of possible $\eta$'s in (7) is at most $D_{\rm mix}\tau(m)T_{|u-v|}(m)$: the permitted image set is a translate of the characters of primitive conductor $\le D_{\rm mix}$, and negative exponents have the same kernel size as positive ones. Thus both $m$-legs are confined to a common class of relative size at most

$$
f(m)=\min\!\left(1,\ \frac{D_{\rm mix}\tau(m)}{\phi(m)}
                  \sum_{\substack{1\le u,v\le V_Q\\u\ne v}}
                                      T_{|u-v|}(m)\right),
 \qquad \sum_{m\le B} f(m)\ll_{\Theta,C,\epsilon}Q^\epsilon D_{\rm mix}.
 \tag{8}
$$

The last estimate is [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) applied to each kernel order with upper cutoff $B$, along with $\tau(m),m/\phi(m)\ll_\epsilon Q^\epsilon$ and the subpower number of exponent pairs. If $V_Q<2$ the sector is empty. The bound is uniform in $\nu$ because it bounds the fiber sizes, not the distribution of its translate over the actual characters.

Use the genuine unmodified R92 progression vector, with all its individual projections, and restrict it to $\mathcal L_m(\nu_m)$, denoting the same function on both legs by $F_\nu(z)$. For the $\nu$-coefficient of the removed sector, both legs may be replaced by $F_\nu$ **exactly**: the product forces the unique partner, and the symmetric selection imposes the common subset just described. No further pair-dependent indicator is required for a fixed $\nu$. Since there are at most $\phi(qd)\phi(m) f(m)$ retained coefficients, the per-character pointwise GRH and [R83 increment estimates](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference), with residue Parseval as normalized in R92 (5), give

$$
\begin{split}
 \|F_\nu(z)\|_2^2&\ll_\epsilon Q^\epsilon f(m)\,z,\\
 \int_X^{2X}\|F_\nu(z+h)-F_\nu(z)\|_2^2\,dz
       &\ll_\epsilon Q^\epsilon f(m)\,X|h|,\qquad 1\le|h|\le X/4,
 \end{split}
 \tag{9}
$$

in the true polynomial raw scales. In particular one does not take a residue norm over $\nu$ before the fixed-product selection.

For arbitrary complex residue vectors $X,Y$ with these projections, let $\mathscr C_\nu(X,Y)$ be the original incidence coefficient at product $\nu$. Using the barred character expansion, say $X_r=\phi(q')^{-1}\sum_\xi\mathsf X_\xi\bar\xi(r)$, it has the exact formula

$$
\mathscr C_\nu(X,Y)=\phi(q')^{-2}
       \sum_\xi \mathsf X_\xi\mathsf Y_{(\nu\circ\pi)\bar\xi}\,
                              C_{\xi,(\nu\circ\pi)\bar\xi}.
$$

Any inactive term is zero. Cauchy over the unique partner and $\sum_\xi|\mathsf X_\xi|^2=\phi(q')\|X\|_2^2$, together with (6), prove

$$
|\mathscr C_\nu(X,Y)|\ll_\epsilon
                Q^\epsilon\sqrt{\mathfrak e(q,b)}\,\|X\|_2\|Y\|_2 .
 \tag{10}
$$

This scalar bound applies also to raw-line Fourier transformed vectors. For a difference orientation the exact residue transpose identity $A_a^{\mathsf T}=A_{-a}$ implies
$\mathscr C_\nu(Y,X)=\nu(-1)\mathscr C_\nu(X,Y)$, by coefficient comparison on all reduced numerators. The masks in (7) and on both inherited legs are symmetric, so the transpose identity persists on this fixed projected space. In particular the even $\nu$-forms are exactly symmetric bilinear forms and the odd $\nu$-forms exactly skew. This is not a claim about transposing the modes after their distinct detunings.

## 4. Fixed aliases, parity masks, and full packet summation

For a common test $\omega\in C_c^2((Q,2Q))$ let $K_1=\|\omega\|_\infty+\|\omega'\|_1$, $K'_2=\|\omega''\|_1+K_1/Q$. Use the [R89 §3](r89-operator-prime-to-denominator-alias-conductors.md#3-per-alias-weighted-estimates-and-the-exact-masks) fixed-alias argument, now for the scalar form at each fixed $\nu$, with (10) instead of the earlier joint numerator estimate. Specifically, the R84 cutoff at $\rho_k=A+8kQ$ satisfies $\rho_k\le9kQ$. Its comparison on good dyad pairs and the direct bound on other pairs use two pointwise norms from (9). On the smoothly cut good pairs, [R84 (8)](r84-operator-short-cosine-and-sum-aliases.md#3-two-exact-marginal-cancellations-on-the-symmetric-difference) applies to the same $F_\nu$ on both legs of a symmetric coefficient by (10) and the two vanishing raw marginals. Its fourth term uses the squared increment in (9) at the actual fixed translation $h=\pm kt$; the $w\mapsto t$ substitution leaves $1/k$, and $|h|/k\le2Q$. On a skew coefficient the common interval cut and the interior increment in [R85 (3)](r85-operator-skew-translation-all-short-aliases.md#3-a-weighted-raw-translation-estimate-for-the-skew-incidence) both have the squared factor $f(m)$ from (9). R85 (4)–(6) then applies to the skew scalar form: oddness of the translated pairing uses transpose, and the bilinear Plancherel bound uses (10) at the two opposite raw frequencies. The raw endpoint error, the first three derivative terms and the sum orientation use only the pointwise part of (9) with the same factor. Thus the common-test cost per alias and $\nu$, after spatial HS aggregation, is

$$
O_\epsilon\!\left(Q^\epsilon\sqrt{\mathfrak e(q,b)} f(m)
                                       [K_1+QK'_2]\right).
 \tag{11}
$$

This uses the original masks and both raw difference orientations, not just the symmetric difference.

For the post-R86/R87 version, separately subtract the selected parts of the two exact parity deletions, as in R92 (8). The fixed $\nu$ and its permitted subset are unchanged under reflection of a residue on an auxiliary-even leg: the transformation acts diagonally by $\xi(-1)$ and does not change any conductor test. Therefore the equal incidence for the two reflected raw kernels persists coefficient by coefficient, and the selected raw masks and the [R87 overlap convention](r87-operator-adaptive-raw-minimum-even.md#2-exact-reflection-on-the-raw-order) are the same. The even or odd projections on either leg only decrease the pointwise bounds (9). The R86/R87 derivative proof and (10) give additional cost

$$
O_\epsilon\!\left(Q^\epsilon\sqrt{\mathfrak e(q,b)} f(m)
                   \frac{QP}{k}(E_\infty+E_1)\right),
 \quad
 E_\infty=\|\omega'\|_\infty+\|\omega\|_\infty/Q,\quad
 E_1=\|\omega''\|_1+\|\omega'\|_1/Q+\|\omega\|_1/Q^2 .
 \tag{12}
$$

No raw marginal identity is used on either sharp parity mask. The original common-divisor and excess gates depend only on $k,b$, not on the common test or the raw variables.

For each $k,b$ and common test, the genuine numerator output is the sum of these coefficient matrices times the characters $\nu(a)$. Multiplicative Parseval in $a\bmod b$ gives the joint numerator HS norm as $\sqrt{\phi(b)}$ times the square norm over $\nu$; allowing $\phi(b)$ coefficient bounds costs at most a total factor $\phi(b)\le b$ on (11)–(12). Hence on the deleted sector $\mathfrak e(q,b)\le Z$ the joint cost is bounded by $Q^\epsilon b\sqrt Z f(m)$ times the same seminorms, with $P/k\le1/2$ for the optional pieces. This step is before detuning; it is not an asserted numerator contraction for an arbitrary restriction of character pairs.

For fixed $b$, group $k\le4M$ by $d=b_\parallel$, necessarily unitary in $b$, with $\operatorname{rad}(d)\mid2k$. The number of those aliases is $O(M/\operatorname{rad}(d))$, as in [R91 (8)](r91-operator-denominator-product-power-conductors.md#3-sum-the-shared-factor-cost-in-the-actual-raw-estimates). Thus the total cost up to test seminorms is at most

$$
O_\epsilon(Q^\epsilon b M\sqrt Z\, L_b),\qquad
  L_b=\sum_{\substack{d\mid b\\(d,b/d)=1}}
                         \frac{f(b/d)}{\operatorname{rad}(d)}.
$$

By Cauchy over $d$, relaxation to all $dm\le B$ in the positive upper sum, and $f(m)^2\le f(m)$, (8) and R92 (9) give

$$
\sum_{b\le B}b^2L_b^2
    \ll_\epsilon Q^\epsilon B^2\sum_{d\le B}\operatorname{rad}(d)^{-2}
                                  \sum_{m\le B/d}f(m)^2
    \ll_{\Theta,C,\epsilon}Q^\epsilon B^2D_{\rm mix}.
 \tag{13}
$$

The radical sum is subpower by the positive finite Euler product in R92, uniformly also for nonsquarefree $b$. Nothing about original pair eligibility was enlarged in the field.

Finally apply the exact [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) common Taylor tests, with the original $a$-dependent coefficients bounded by $2^{-n}$ at Taylor index $n$, the original exterior unit phases, and division by $J\asymp Q$. At offset $\ell$, the effective seminorms are $K_1=O(1+|\ell|)$ and $K'_2,E_\infty,E_1=O(S^{-1}+(1+|\ell|)^2/Q)$ after summing the Taylor bounds, as verified in R92 §4. Square-sum the offsets $|\ell|\le R+1$ and denominators with (13). This yields (3) with all original differing detunings, and proves the stated comparisons by the triangle inequality. No centering, edge, or continuous model term has been replaced by this character argument.

## 5. Strict eligibility in the actual selector

In the numerical setting, take $k=r$ an odd prime of size $Q^{11/20}$ and prime $b$ in the high band, so $m=b$ and $\mathfrak e(2r,b)=1$. On $2r$ pair a character of order $r-1$ with its conjugate; all allowed powers retain conductor $r$. On $b$ take a generator $\eta$ and $\eta'=\eta^{-2}$. Their orders are $b-1$ and $(b-1)/2$, and the product $\eta^{-1}$ has order $b-1$. For sufficiently large $Q$, all allowed small powers of these individual characters and their product are nonprincipal and keep conductor $b$, so all three earlier cuts are respected. Yet $\eta^2\eta'=1$, satisfying (2). The two Gauss factors at $b$ and the $2r$ conjugate pairing are nonzero. This is strict eligibility for the unmodified input, not a lower bound on the actual field.
