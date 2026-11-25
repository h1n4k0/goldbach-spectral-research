# Small powers of the individual coprime-denominator characters

This removes a third character sector from the actual larger-alias packet. The cut concerns either individual leg on the prime-to-alias part of the denominator, rather than the alias leg of R90 or the product of the two legs in R91. The main issue is to keep the true short-increment estimates when one leg passes the new cut and the other does not.

## 1. Exact input and conclusion

Use the complete even shell, the genuine transported parent profiles $h,f$, the common taper, and the original $J^{-1}$-normalized high-denominator packet $\mathcal C_+(B,R)$ of [R91](r91-operator-denominator-product-power-conductors.md#1-exact-setting-and-bound). Assume original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH up to $\lceil 8MB\rceil+2$, including modulus $1$. Take $Q\le A\le QH/100$ and $A/Q\le K\le4M$, and write $R_*=1+R$. The input $Z_{\rm prod}$ is the actual field retained from R91, with its original high product and product-power conditions, its R90 alias-power condition, high individual character conditions, $(2k,b)<G$, $k>K$, and $z,w>A$. Both versions of R91 are allowed: either the original larger-alias raw field or that field with the exact R86/R87 parity pieces removed, with $K\ge2P$ in the latter case.

For a fixed alias $k$ and denominator $b$, write

$$
q=2k,\qquad b=d\,m,\qquad
 d=\prod_{p\mid q}p^{v_p(b)},\qquad q_0=qd,\qquad
 q'=qb=q_0m,\qquad (q_0,m)=1.
 \tag{1}
$$

The variable $m$ in (1) is a denominator factor, not the shell's half-modulus index. Let $\eta\bmod m$ denote the individual component of $\xi\bmod q'$ on this factor. For fixed $C>0,D_i\ge1$, put

$$
\mathcal L_m=\{\eta\bmod m:
   \operatorname{cond}(\eta^v)\le D_i
     \text{ for some integer }1\le v\le\lfloor(\log Q)^C\rfloor\}.
 \tag{2}
$$

Conductors are primitive inducing conductors, with the usual convention for modulus $1$. Define $Z_{\rm ind}$ by omitting all pairs of $Z_{\rm prod}$ in which **at least one** of the two individual $m$-components belongs to $\mathcal L_m$. The projections occur at the fixed $k,b$, before the original unequal numerator detunings. All raw masks, profiles, signs and earlier selections are preserved. Then

$$
\begin{split}
 \|Z_{\rm prod}-Z_{\rm ind}\|_{\rm pkt}
 &\ll_{\Gamma,\Theta,C,\epsilon} Q^\epsilon B\sqrt{D_i}\,M
       \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right],\\
 \|X\|_{\rm pkt}
 &=\left(\sum_{j\in\mathcal C_+(B,R)}
                            \|X(j)\|_{\rm HS}^2\right)^{1/2}.
 \end{split}
 \tag{3}
$$

This also holds after a fixed orthogonal spatial compression or restriction to a subset of this packet.

With $D_i=Q^{3/1000}, B=\lfloor Q^{39/100}\rfloor, M=Q^{3/5}, R=\lfloor Q^{1/400}\rfloor, S=Q^{249/250}$, and all other scales as in R91, (3) is $O_{\epsilon,C}(Q^{-9/4000+\epsilon})$. For the post-R86/R87 input the inherited sharp $\widehat T,\widehat P$ comparison remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm ind}$. Neither assertion controls the surviving covariance, other packets, any prescribed modulus, or weak S.

## 2. Mixed selections with the same raw vector on both legs

Let $n(m)=|\mathcal L_m|$, $\lambda(m)=n(m)/\phi(m)$. The [R90 (4)–(6)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) argument, with upper cutoff $B$ instead of $8M$, gives

$$
\sum_{m\le B}\lambda(m)\ll_{\Theta,C,\epsilon}Q^\epsilon D_i.
 \tag{4}
$$

The change of cutoff in that unconditional power-fiber proof needs only a polynomial upper bound for $B$: the torsion count is multiplicative, the small powers range over a polylogarithmic set, and the weighted prime harmonic sum in R90 (5) has the same uniform upper bound for a polynomial prime cutoff. The count for (4) allows all individual characters modulo $m$, not only those surviving the earlier high individual condition at $q'$.

For each $q',k,b$, let $F(z)$ be the genuine centered progression vector of [R81 (5)](r81-operator-low-conductor-long-quotient.md#2-exact-local-power-vanishing-and-the-low-conductor-fourth-moment) with the inherited individual projections (including R90). They are fixed orthogonal projections on the character basis, independently of the raw variable, real shell parameter and numerator. On that basis decompose $F=F_L+F_H$ by (2). The retained product-character selection of R91 is a separate orthogonal projection $\Pi_b$ in the reduced numerator index: its character set consists of the [R82 high products](r82-operator-low-product-character-long-quotient.md#2-exact-dependence-on-the-product-of-the-two-characters) with the R91 product-power deletions made. This projection does not change $F$. From R81 (5), normalized residue Parseval, and the per-character estimates in the proof of [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference), one has

$$
\begin{array}{ll}
 \|F_L(z)\|_2^2\ll_\epsilon Q^\epsilon\lambda(m)z,&
 \displaystyle\int_X^{2X}\|F_L(z+h)-F_L(z)\|_2^2\,dz
                  \ll_\epsilon Q^\epsilon\lambda(m) X|h|,\\[4pt]
 \|F_H(z)\|_2^2\ll_\epsilon Q^\epsilon z,&
 \displaystyle\int_X^{2X}\|F_H(z+h)-F_H(z)\|_2^2\,dz
                         \ll_\epsilon Q^\epsilon X|h|.
 \end{array}
 \tag{5}
$$

Here $X$ is in the original polynomial raw range and $1\le |h|\le X/4$; the pointwise estimates hold on the full original raw ranges. Indeed, allowing every character modulo $q_0$, at most $\phi(q_0)n(m)$ coefficients occur for $F_L$, out of $\phi(q')=\phi(q_0)\phi(m)$. The squared norm has the divisor $\phi(q')$, not its square, because the residue index set carries the unnormalized counting norm. This uses the uniform bound on each character's integrated increment, not just contraction of an averaged estimate. The same pointwise bounds are valid after the optional even or odd projections on either individual leg.

The bilinear field at fixed $k,b$ with a common test, any fixed parent entry and the unmodified raw masks will be denoted $\mathscr B(X,Y)$, with the two arguments replacing $F(z),F(w)$. It includes all original signs and the linear projection $\Pi_b$. It is bilinear over $\mathbb C$, using transposes, not Hermitian adjoints, since the switched residue incidence has $X^{\mathsf T}A_aY$ as its raw integrand. The two actual profiles need not be equal. The removed field is exactly
$\mathscr B(F_L,F_L)+\mathscr B(F_L,F_H)+\mathscr B(F_H,F_L)$.
In particular the mixed terms are not presumed zero. For $\lambda=\lambda(m)>0$, set

$$
F_\pm=\lambda^{-1/4}F_L\ \pm\lambda^{1/4}F_H .
$$

Then the exact identity on each entry before detuning is

$$
\mathscr B(F_+,F_+)-\mathscr B(F_-,F_-)
             =2\big[\mathscr B(F_L,F_H)+\mathscr B(F_H,F_L)\big].
 \tag{6}
$$

If $\lambda=0$ there is nothing to estimate. Each $F_\pm$ satisfies both squared estimates of (5) with upper factor $O(\sqrt\lambda)$ in place of the displayed factors $\lambda,1$: the character supports are disjoint even for the differences in (5), so the squared estimates add with factors $\lambda^{-1/2},\lambda^{1/2}$. The argument is for the genuine linear combinations of the centered prime-progression coefficients. It does not rely on favorable correlations between the two mixed terms.

## 3. Fixed-alias inheritance, including the exact parity pieces

Let $\omega\in C_c^2((Q,2Q))$ be a common test before the different fractional detunings, and write $K_1=\|\omega\|_\infty+\|\omega'\|_1$, $K'_2=\|\omega''\|_1+K_1/Q$. For arbitrary complex residue vectors $X,Y$, [R76 (7)](r76-operator-joint-rational-numerator-variance.md#2-additive-parseval-in-the-exact-incidence-and-the-continuous-term) bounds the joint incidence vector by $b\|X\|_2\|Y\|_2$. The projected numerator family costs no more. In the difference orientations, $A_a^{\mathsf T}=A_{-a}$ and the reflection multiplies a numerator character $\nu(a)$ by $\nu(-1)$. Thus $\Pi_b$ commutes with this reflection and can be kept in both cosine and skew arguments. This is not a projection on the finally detuned packet. The same joint bound applies pointwise to the sum orientation.

For clarity, the fixed-alias argument of [R89 §3](r89-operator-prime-to-denominator-alias-conductors.md#3-per-alias-weighted-estimates-and-the-exact-masks), before either sharp parity piece has been removed, applies to any common vector $G(z)$ on the two legs with (5)'s squared pointwise and increment bounds both scaled by $\mu$. For the two differences, use the [R84 raw cutoff](r84-operator-short-cosine-and-sum-aliases.md#2-common-test-and-an-adaptive-raw-cutoff) at $\rho_k=A+8kQ$ on pairs $4\rho_k\le X=QV$ in the shorter-support dyad, and the direct estimate on other pairs. The sharp-to-smooth change and the direct estimate on other pairs use only products of two pointwise bounds, so scale by $\mu$; also $\rho_k\le9kQ$ since $k>K\ge A/Q$. On good pairs both mixed-derivative marginal integrals of the smoothly cut common weight vanish. R84 (8) therefore uses the same $G$ on both legs and replaces the symmetric product by the quadratic increment. The first three derivative terms use squared pointwise bounds; the fourth uses the squared increment over the raw dyads at fixed shift $h=\pm kt$ with $|h|\le\rho_k/4$. Both bounds scale by $\mu$.

In the skew argument of [R85 §3](r85-operator-skew-translation-all-short-aliases.md#3-a-weighted-raw-translation-estimate-for-the-skew-incidence) restrict the same $G$ on both legs to the common interval. Its endpoint cost and its interior increment cost retain the factor $\mu$ in the squared estimates R85 (3); the odd Fourier weight in R85 (5) times the squared Fourier norm therefore has the same factor. The joint incidence bound holds for those transformed complex vectors too, without any reality assumption. Weighted summation in the raw variable at fixed $t$, and the $w\mapsto t$ change that leaves $1/k$, are unchanged, as is the comparison $|h|/k\le 2Q$. The resulting per-alias HS bound scales by $\mu$. The signed sum orientation uses the same factor $\mu$ from the two pointwise estimates in R84 (12). Thus, on the actual unmodified larger-alias raw domain, the common-test joint HS cost is $O_\epsilon(Q^\epsilon b\mu[K_1+QK'_2])$ after the original spatial parent aggregation. This derivation uses only the two squared bounds on $G$, the actual derivative envelopes, and the joint numerator bound, with no diagonal reality, equality of parent profiles, or inter-alias cancellation.

Apply this estimate to $G=F_L$ with $\mu=\lambda$ and to $G=F_\pm$ with $\mu=O(\sqrt\lambda)$ in (6). The deleted part of the unmodified field costs

$$
O_\epsilon(Q^\epsilon b\sqrt{\lambda(m)}
                                [K_1+QK'_2])
 \tag{7}
$$

per alias. It is important here that the quadratic increment or the skew pairing was applied with the same vector on both raw legs. Inserting two different vectors into those identities would not prove (7).

For the post-R86/R87 input, subtract the deleted parts of the two exact parity pieces from the just-estimated deleted part of the unmodified field. For these two pieces one can expand the individual selection as the three actual low–low, low–high and high–low terms, without using (6). The individual character selections commute with reflection of an auxiliary residue or its even/odd projection; [R86 (2)](r86-operator-long-alias-short-leg-even.md#2-reflection-in-the-exact-switched-incidence) and [R87 (3)–(4)](r87-operator-adaptive-raw-minimum-even.md#2-exact-reflection-on-the-raw-order) compare the same residue incidence on the relevant even leg. The product projection $\Pi_b$ is then applied linearly to that identity. Thus the two reflected derivative kernels can still be combined before the absolute value, including the exact earlier overlap convention (R87 removes only the R86 complement). In their pointwise estimates each selected product has at least one factor $\sqrt\lambda$ by (5). Hence R89 (8) gives the cost

$$
O_\epsilon\!\left(Q^\epsilon b\sqrt{\lambda(m)}
                 \frac{QP}{k}(E_\infty+E_1)\right),
 \quad E_\infty=\|\omega'\|_\infty+\|\omega\|_\infty/Q,\qquad
 E_1=\|\omega''\|_1+\|\omega'\|_1/Q+\|\omega\|_1/Q^2 .
 \tag{8}
$$

In particular this does not apply a cosine marginal or a skew translation identity after insertion of the sharp ordered raw masks. No unit restorations or continuous benchmark terms are newly asserted: the input is already the exact projected two-error field of R91.

## 4. Exact summation and packet transfer

At a fixed denominator $b$, group the actual $k\le4M$ by their unitary divisor $d=b_\parallel$ in (1). For such a $k$, $\operatorname{rad}(d)\mid 2k$; thus there are $O(M/\operatorname{rad}(d))$ possible $k$ at that $d$, with none when $\operatorname{rad}(d)>8M$. This is the alias count of R91 (8) and includes the prime $2$. Only in this positive upper count is the common-divisor gate relaxed. Since $P/k\le1/2$ in the reduced input, (7)–(8) give the denominator factor $Q^\epsilon bM L_b$ times the corresponding test seminorms, where

$$
L_b=\sum_{\substack{d\mid b\\(d,b/d)=1}}
                 \frac{\sqrt{\lambda(b/d)}}{\operatorname{rad}(d)} .
$$

By Cauchy over the $d$'s, $\tau(b)\ll_\epsilon Q^\epsilon$, $b\le B$, and (4),

$$
\begin{split}
 \sum_{b\le B}b^2L_b^2
  &\ll_\epsilon Q^\epsilon B^2
           \sum_{d\le B}\operatorname{rad}(d)^{-2}
                        \sum_{m\le B/d}\lambda(m)
   \ll_{\Theta,C,\epsilon} Q^\epsilon B^2D_i .
 \end{split}
 \tag{9}
$$

In the first bound only the positive majorant was enlarged from unitary factorizations to all $dm\le B$. For the second bound use the finite positive Euler product

$$
\sum_{d\le B}\operatorname{rad}(d)^{-2}
       \le \prod_{p\le B}(1+E_p/p^2),\qquad
                     E_p=\lfloor\log B/\log p\rfloor .
$$

The logarithmic contribution for $p\le\sqrt{\log Q}$ is $O_\Theta(\sqrt{\log Q}\log\log(3Q))$. For larger primes the positive increments are bounded by $O_\Theta(\log Q\sum_{n>\sqrt{\log Q}}n^{-2})=O_\Theta(\sqrt{\log Q})$. The log is therefore $o(\log Q)$ even for high prime powers, and all subpower factors in (9) are absorbed by taking smaller intermediate $\epsilon$'s.

Use the exact common Taylor tests of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) at offset $\ell$, with the original numerator-dependent coefficients bounded by $2^{-n}$ at Taylor index $n$, and the exterior unit-modulus phases unchanged. The summably weighted $K_1$ is $O(1+|\ell|)$; the corresponding $K'_2,E_\infty,E_1$ are $O(S^{-1}+(1+|\ell|)^2/Q)$, by the same derivative bounds used in R89 §4. In particular the common taper has first derivative supremum $O(S^{-1})$, while the derivative of the bulk phase costs $O((1+|\ell|+n)/Q)$ under the Taylor factorial bound. Applying all projections before these scalar multipliers and dividing by $J\asymp Q$ gives the joint estimate

$$
O_\epsilon\!\left(Q^\epsilon b M L_b
       \left[\frac{1+|\ell|}{Q}
                +\frac{(1+|\ell|)^2}{Q}+\frac1S\right]\right)
$$

for each $b,\ell$. Sum in the squared numerator, denominator and offset norm with $|\ell|\le R+1$; (9) gives $B\sqrt{D_i}$, and the three offset sums give $R_*^{3/2},R_*^{5/2},R_*^{1/2}$. This proves (3) on the actual packet. The three powers in the stated example are $-19/4000,-9/4000,-13/4000$, so the inherited comparison carries over by the triangle inequality.

## 5. Distinct eligibility after all earlier character cuts

At the example scales take $k=r$ an odd prime of size $Q^{11/20}$, and $b$ a prime in the high denominator band, so $(2r,b)=1$, $m=b$, and $r_b=2r$. Such choices exist for large $Q$ by Bertrand's postulate. On the $2r$-leg take a character of order $r-1$ and its conjugate. Their product on $2r$ is principal and each allowed small power has conductor $r$, beyond the R90 threshold. Modulo $b$ choose a quadratic $\eta$ and take $\eta'=\nu\bar\eta$, where $\nu$ generates the character group of $b$. Both are nonprincipal and have ordinary conductor $b$, so survive R81. Every allowed small power of the product $\nu$ has conductor $b$, so the pair survives the two earlier product cuts. In fact the order of $\eta'$ is at least $(b-1)/2$: in generator coordinates its exponent $1-(b-1)/2$ has gcd at most $2$ with $b-1$. Thus this is mixed eligibility for (2): $\eta^2=1$, whereas every allowed small power of $\eta'$ has conductor $b>D_i$. The coprime Gauss factors on $b$ are nonzero for both nonprincipal prime-modulus characters, and the $2r$ conjugacy pairing is the nonzero unit sum. This is strict eligibility for the unmodified input; it gives no lower bound on the field.
