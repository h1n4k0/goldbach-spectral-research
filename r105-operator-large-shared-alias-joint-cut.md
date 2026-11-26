# A larger joint conductor cutoff on large shared alias parts

Retaining the full shared part of the original alias, rather than only its radical or its common divisor with the denominator, gives a savings in the alias sum. This permits a larger three-factor conductor cutoff on those actual aliases. The conclusion concerns one deletion in the specified packet, not the covariance that remains.

## 1. Exact selected sector and estimate

Use the genuine field $Z_{\rm gauss}$ after [R102 §1](r102-operator-shared-equal-gauss-conductor.md#1-exact-selection-and-packet-estimate), on the original complete even shell. Keep the transported parent profiles $h,f$, common taper, $J^{-1}$ normalization, high-denominator packet $\mathcal C_+(B,R)$, and all original signs and gates $z,w>A$, $k>K\ge A/Q$, $(2k,b)<G$. Assume original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Both R102 inputs are allowed, with or without the two exact R86/R87 parity removals and with $K\ge2P$ in the former case. All polynomial parameter ranges are inherited.

For the actual $q=2k$ and denominator $b$, retain the [R100 factorization](r100-operator-three-factor-joint-powers.md#1-a-three-factor-sector-of-the-retained-field)

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
 q=r_bh_q,\qquad s=dh_q,\qquad q'=qb=r_bms .
 \tag{1}
$$

Here $d$ consists of the full powers in $b$ at primes dividing $q$, and $h_q$ of the full powers in $q$ at these shared primes. In particular $h_q$ is not generally $(q,b)$ or $\operatorname{rad}(d)$. The factors $r_b,m,s$ are pairwise coprime. Denote the two character-leg components on these factors by $(\alpha,\eta,\gamma)$ and $(\alpha',\eta',\gamma')$, respectively.

Take $D,D_0,A_h\ge1$, $C>0$, and $V_Q=\lfloor(\log Q)^C\rfloor$. Only at actual aliases with $d\ge D_0$ and $h_q\ge A_h$, delete from $Z_{\rm gauss}$ its retained pairs satisfying

$$
\operatorname{cond}(\alpha^j)
     \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)
     \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D
  \quad\text{for some integers }1\le j,u,v,a,c\le V_Q,\quad
              u\ne v,\quad a\ne c .
 \tag{2}
$$

As always a conductor is the primitive inducing conductor, and the principal conductor is one. The new masks are applied before the original numerator-specific detunings. Both preceding unequal and equal cuts remain in force. No new exponent range must be covered by R96 for the estimate below.

Write $Z_{\rm large}$ for this new field, $R_*=1+R$, with the exact packet norm of R100. Then

$$
\|Z_{\rm gauss}-Z_{\rm large}\|_{\rm pkt}
  \ll_{\Gamma,\Theta,C,\epsilon} Q^\epsilon
      \frac{BD}{\sqrt{D_0A_h}}
       \left[\frac{R_*^{3/2}+R_*^{5/2}}Q
                          +\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

This permits arbitrary denominator prime powers, restricting the deletion to any subset fixed by $k,b$, and fixed orthogonal spatial compression or restriction to any subset of the packet.

For the established scales $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, and $D_0=Q^{1/5}$, one may take either

$$
(A_h,D)=(Q^{1/20},Q^{29/40})
            \quad\hbox{or}\quad
 (A_h,D)=(Q^{9/50},Q^{79/100}) .
 \tag{4}
$$

Both choices give $O_{\epsilon,C}(Q^{-3/800+\epsilon})$; all old thresholds, including $Q^{7/10}$ for R100, stay unchanged. The sharp $\widehat T,\widehat P$ comparison in the post-parity input therefore still has error $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm large}$. At the second choice this is a larger conductor range on the stated large-$h_q$ subset only. It does not estimate the surviving covariance, an individual even modulus, other packets, or weak S.

## 2. Same-vector support and the uniform product-conditioned estimate

For a fixed actual $q,b$ and full product $\nu=\nu_d\rho\bmod b$, the original incidence forces a unique second progression character, with component equalities

$$
\alpha'=\bar\alpha,\qquad
      \eta'=\rho\bar\eta,\qquad
      \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{5}
$$

where $\pi_s$ is unit reduction to $d$. The old retained pair masks on $Z_{\rm gauss}$ preserve this involution as in [R102 §2](r102-operator-shared-equal-gauss-conductor.md#2-keep-the-smaller-true-scalar-coefficient). The new mask (2) does also: the alias power conductor is unchanged by conjugation, and the two mixed exponent pairs may be interchanged simultaneously while staying in the range. Both alias gates are fixed by $k,b$. Thus at each full product the deletion is implemented by the same projected genuine progression vector $F_\nu$ on its two raw legs; discarded full products have zero coefficients. The earlier leg parity projections on the reflected sharp pieces remain as in the original calculation.

Write $T_j(n)=|\ker(\chi\mapsto\chi^j)|$ on the character group of $n$, with $T_j(1)=1$, and $H(n)=\sum_{j\le V_Q}T_j(n)$. For fixed $(j,u,v,a,c)$, (5) makes the selected output a translated power map on the true product $r_bms$, with components

$$
\bigl(\alpha^j,\ \eta^{u-v}\rho^v,\
                      \gamma^{a-c}(\nu_d\circ\pi_s)^c\bigr).
$$

The cardinality of each nonempty fiber is $T_j(r_b)T_{|u-v|}(m)T_{|a-c|}(s)$. Both differences are nonzero. There are at most $D\tau(q')$ output characters of primitive conductor at most $D$: sum the possible counts at inducing divisors $c_0\mid q'$, $c_0\le D$, noting that there are at most $\phi(c_0)$ for each one. The inducing conductor of the three components is their product by coprimality. Divide by $\phi(q')$, sum over all exponent tuples, and absorb the polylogarithmic factor and the inverse totient/divisor costs. The support fraction is at most

$$
O_{\Theta,C,\epsilon}\!\left(
          Q^\epsilon\,\frac{D H(r_b)H(m)H(s)}{r_bms}\right)
 \tag{6}
$$

uniformly in $\nu$, since the older masks only reduce the count. This is the exact fixed-product argument of [R100 §2](r100-operator-three-factor-joint-powers.md#2-exact-joint-fibers-at-one-full-product) with the new alias gates. If $V_Q<2$, the deletion is empty.

The normalized residue Parseval and the pointwise and [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference) integrated increment estimates hold for each individual progression character under the same auxiliary GRH assumption. In the genuine projected vector both squared bounds thus scale by the fraction in (6). For each full product, use the true scalar form of [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms) on arbitrary unit residue vectors, with bilinear norm $O_\epsilon(Q^\epsilon\sqrt{\mathfrak e(q,b)})$ where $\mathfrak e(q,b)=d/(q,d)$. This is also the bound for raw Fourier transformed arguments. The transpose factor is exactly $\nu(-1)$ on the difference orientations. Therefore the fixed-product common-test bound of [R100 §3](r100-operator-three-factor-joint-powers.md#3-common-test-transfer-and-the-harmonic-alias-sum) applies: the cosine marginal identity and skew raw translation use the same selected $F_\nu$, and the signed sum uses the two pointwise factors. In the optional post-parity input the exact character masks commute with the old parity projections; the reflected derivative bounds use their actual pointwise estimates, and no marginal identity is applied on the sharp parity gates. All original signs and the overlap convention are kept.

Full numerator Parseval adds a factor at most $\phi(b)\le b$, since the bounds are uniform in $\nu$. Thus the per-alias joint numerator cost, at a **common** test before detuning, is

$$
O_\epsilon\!\left(Q^\epsilon b\sqrt{\mathfrak e(q,b)}
             \frac{D H(r_b)H(m)H(dh_q)}{r_bm d h_q}\,\mathcal K\right),
 \tag{7}
$$

with the inherited $\mathcal K=K_1+QK'_2$, enlarged by $Q(E_\infty+E_1)$ for the reflected parity pieces when needed. This uses the true $P/k\le1/2$ in that input.

## 3. Sum the large shared alias parts and restore the packet

At fixed $b$ group the actual aliases by their unitary divisor $d=b_\parallel$, with $m=b/d$ within the group. Let $L_{b,d}$ be the sum of the arithmetic factors in (7) without $bQ^\epsilon$ and $\mathcal K$, over the genuine eligible aliases. It is zero when $d<D_0$. Each $r_b,h_q$ determines at most one alias and $r_bh_q\le8M$. Also $(q,d)\ge\operatorname{rad}(d)$, and $H(dh_q)\le2V_QH(d)$ by [R99 (9)](r99-operator-unequal-shared-leg-powers.md#3-sum-the-full-shared-part-of-each-actual-alias) on identical prime support. Thus, with $U=\max(A_h,\operatorname{rad}(d))$,

$$
L_{b,d}\ll_{\Theta,C,\epsilon} Q^\epsilon
       \frac{D H(m)H(d)}{m\sqrt{d\operatorname{rad}(d)}}
      \sum_{\substack{U\le h_0\le8M\\p\mid h_0\Rightarrow p\mid d}}
          \frac1{h_0}\sum_{r\le8M/h_0}\frac{H(r)}r .
 \tag{8}
$$

In this positive upper bound we have allowed any $h_0$ with the indicated prime support and lower bound, rather than enforcing all the true alias constraints. No such constraint is changed in the field being estimated. The cutoff $U$ is necessary because every actual $h_q$ is divisible by $\operatorname{rad}(d)$.

The inner sum in (8) is $O_{\Theta,C,\epsilon}(Q^\epsilon)$ by [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers). If the group is nonempty, $U\le8M$ is in the fixed polynomial range. For a fixed $\delta>0$, the outer harmonic sum may be enlarged and bounded by

$$
\sum_{\substack{h_0\ge U\\p\mid h_0\Rightarrow p\mid d}}\frac1{h_0}
   \le U^{-1+\delta}\prod_{p\mid d}(1-p^{-\delta})^{-1}
   \ll_{\Theta,\epsilon} Q^\epsilon/U .
 \tag{9}
$$

For the last bound, take a fixed sufficiently small $\delta>0$ so $U^\delta$ fits the prescribed subpower budget. For any $\epsilon'>0$ and fixed $\delta$, the product in (9) is $O_{\delta,\epsilon'}(d^{\epsilon'})$: compare the large-prime factors to $p^{\epsilon'}$ and bound the product over the fixed set of smaller primes. Then take $\epsilon'$ suitably small since $d\le B$ is polynomial. The same conventions include $d=1$, when the only supported alias part is $1$. These are weighted positive sums of actual factor possibilities, not a cancellation assumption on the aliases.

Combining (8) and (9) and using $U^2\ge A_h\operatorname{rad}(d)$ gives

$$
L_{b,d}^2
    \ll_{\Theta,C,\epsilon} Q^\epsilon
        \frac{D^2 H(m)^2H(d)^2}
                        {m^2 d A_h\,\operatorname{rad}(d)^2}.
 \tag{10}
$$

The required square-torsion moment with this smaller radical exponent is

$$
\sum_{d\le B}\frac{H(d)^2}{\operatorname{rad}(d)^2}
       \ll_{\Theta,C,\epsilon} Q^\epsilon .
 \tag{11}
$$

Here is the extra Euler step. By $H(d)^2\le V_Q\sum_{j\le V_Q}T_j(d)^2$, fix $j$ and majorize its sum by the positive Euler product with local factor
$1+p^{-2}\sum_{e\ge1}T_j(p^e)^2p^{-e\delta}$ for $p\le B$, at cost $B^\delta$, with fixed small $\delta>0$. For $p\nmid2j$, $T_j(p^e)=\gcd(j,p-1)\le p$, and its local increment is at most $T_j(p)/(p(p^\delta-1))\ll_\delta T_j(p)/p$. The sum of these increments over $p\le B$ is $O_\delta((1+\log\log(10Q))\tau(j))=o(\log Q)$ uniformly for $j\le V_Q$: expand the gcd by the totient divisor identity and use the reciprocal-prime progression estimate in [R90 §2](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) with the polynomial cutoff $B$. At $p\mid2j$ the bound $T_j(p^e)\le2j$ gives a logarithmic cost $O_\delta(\log(2j))$ per prime, thus $o(\log Q)$ in total. Choose $\delta$ small relative to the desired $\epsilon$ and absorb the polylogarithmic $j$ sums. This proves (11) for unrestricted prime powers in $d$. The other needed moment $\sum_{m\le B}H(m)^2/m^2\ll_\epsilon Q^\epsilon$ is bounded by the square of the nonnegative [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) harmonic sum.

At fixed $b$, Cauchy over the at most $\tau(b)$ unitary divisor groups, then $b^2\le B^2$, (10)–(11), and the positive enlargement to all $dm\le B$ give

$$
\begin{split}
 \sum_{b\le B}b^2
   \left(\sum_{\substack{d\mid b\\(d,b/d)=1}}L_{b,d}\right)^2
 &\ll_{\Theta,C,\epsilon}Q^\epsilon
       \frac{B^2D^2}{D_0A_h}
        \sum_{m\le B}\frac{H(m)^2}{m^2}
        \sum_{d\le B}\frac{H(d)^2}{\operatorname{rad}(d)^2}\\
 &\ll_{\Theta,C,\epsilon} Q^\epsilon B^2D^2/(D_0A_h).
 \end{split}
 \tag{12}
$$

This uses the true gate $d\ge D_0$, and all omitted restrictions were dropped only in positive upper sums. We take smaller intermediate $\epsilon$'s for the finitely many subpower factors.

Apply the exact common Taylor tests of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field), keeping the original coefficient bounded by $2^{-n}$ at Taylor order $n$ and every original exterior phase. The weighted common $K_1$ cost is $O(1+|\ell|)$ at offset $\ell$, and $K'_2,E_\infty,E_1$ cost $O(S^{-1}+(1+|\ell|)^2/Q)$ as in R100. Dividing by $J\asymp Q$ and square-summing over $|\ell|\le R+1$ in (12) yields (3), without removing any detuning. At both choices in (4) the arithmetic prefactor has exponent $99/100$; the three final exponents are $-1/160,-3/800,-19/4000$. The earlier sharp comparison follows by the triangle inequality with all independent restoration and benchmark estimates intact.

## 4. A live witness on a large shared alias with radical six

Consider the scales in (4). Choose $d=3\cdot2^e$ with the least $e$ making $d\ge Q^{1/5}$. Choose an odd prime $m\in(B/(2d),B/d)$ and an odd prime $r\asymp Q^{411/1000}$ by Bertrand's postulate. They are distinct and exceed $3$ for large $Q$. Choose $3^\ell\asymp Q^t$, taking $t=11/100$ at the first scales and $t=37/200$ at the second. Set

$$
b=dm,\quad k=3^\ell r,\quad q=2k,\qquad
         h_q=2\cdot3^\ell,\quad r_b=r,\quad s=2^{e+1}3^{\ell+1}.
$$

These are genuine aliases: $k\asymp Q^{411/1000+t}$ is larger than the old $K$ and smaller than $4M$, even at $t=37/200$, where it has exponent $596/1000$. The common divisor $(q,b)=6<G$, $h_q\ge A_h$, and $\operatorname{rad}(d)=6$; the new gate truly uses $h_q$, not a large radical. The denominator lies in the high band by the choice of $m$.

On $r$ choose a generator and its conjugate. On $m$ use a generator $\eta$ and $\eta'=\eta^{2V^*}$, with $V^*$ an integer bounding all finitely many relevant fixed log-power ranges, as in [R102 §4](r102-operator-shared-equal-gauss-conductor.md#4-a-live-coefficient-beyond-the-r101-cutoff). All earlier tested alias powers have conductor $r>Q^{51/125}$, and all previously tested individual, product and signed mixed $m$-powers have conductor $m$. Indeed their generator exponents are nonzero and smaller than $m-1$ in absolute value. Thus the old alias gates and the earlier alias/shared joint test survive, the full product remains high from $m$, and $rm\asymp Q^{601/1000}$ exceeds the old alias/coprime joint ceiling $Q^{3/5}$.

At $2^{e+1}$ use a sign-trivial primitive $\gamma_2$ of $5$-order $2^{e-1}$ and $\gamma'_2=\gamma_2^{-3}$, also primitive. Their product has conductor $2^e$ and induces from $d$. At $3^{\ell+1}$ take a primitive conjugate pair that is trivial on the tame part of the local unit group. Their product is principal and also induces from $d$. This is an actual full-product pair. Every earlier small power of the shared product retains conductor $2^{e-O(\log\log Q)}=Q^{1/5-o(1)}$, so R98 does not remove it. Every earlier unequal shared exponent pair has $v_3(a-c)=O(\log\log Q)<\ell$ and hence conductor at $3$ exactly $3^{\ell+1-v_3(a-c)}$, by the actual local law of [R104 §1](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation). This is $Q^{t-o(1)}$, bigger than the R99 threshold, and the corresponding earlier R100 products are at least $Q^{601/1000+t-o(1)}>Q^{7/10}$ for both choices of $t$. R101 unequal-shared products likewise exceed its threshold. For the equal shared branches in R101 and R102 the $2$-part still has conductor $Q^{1/5-o(1)}$, so their total conductor is $Q^{801/1000-o(1)}$, outside both earlier cutoffs. Therefore the pair survives the stated prior selections.

Its original primitive-numerator coefficient is nonzero. On the $2$-part congruence modulo $2$ is automatic on the odd units, and both primitive additive Gauss factors at the actual unit frequencies are nonzero. At $3$, use the exact [R93 §2](r93-operator-unequal-mixed-denominator-powers.md#2-a-shared-prime-restriction-of-the-exact-gauss-factor) parameterization with $v_3(q)=\ell$ and $v_3(b)=1$. The $x\bmod3$ transform of $\overline{\gamma'_3(1+3^\ell x)}$ is $3$ at exactly one nonzero frequency and zero elsewhere, because the local character is primitive on $3^{\ell+1}$. The outer unit variable runs through all nonzero frequencies in the exact CRT local formula, so one nonzero term survives, with principal product factor; the local coefficient has absolute value $3^{\ell+1}$. This is the same finite mechanism as in [R103 §4](r103-operator-independent-shared-relation-obstruction.md#4-the-quadratic-determinant-loss-can-occur-on-a-retained-coefficient), here at a large alias power rather than modulus $3^2$. On $r$ the original congruence gives the nonzero conjugate pairing, and the coprime factors on $m$ are nonzero primitive additive Gauss sums.

Finally $(j,u,v,a,c)=(1,2,1,3,1)$ in the new test kills the $2$-part and keeps full $3^{\ell+1}$. The product in (2) is therefore $rm\,3^{\ell+1}\asymp Q^{601/1000+t}$, with exponents $711/1000<29/40$ and $786/1000<79/100$, respectively. This witnesses strict eligibility of an actual nonzero incidence coefficient in the unmodified input, not a lower bound on the integrated or parity-reduced packet field.
