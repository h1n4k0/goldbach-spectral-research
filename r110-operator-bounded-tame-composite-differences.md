# Composite shared exponent differences with bounded tame torsion

A prime-power difference is not needed if the combined tame torsion on the genuinely shared primes is bounded. The wild part can be averaged over the integers supported on those primes. This removes a new composite-difference sector of the actual previous packet, even when two shared primes both divide the exponent difference.

## 1. The exact additional selection

Start from the genuinely retained $Z_{\rm pp}$ of [R109 §1](r109-operator-polynomial-prime-power-differences.md#1-the-exact-additional-deletion), including its prescribed prior $Z_{\rm top}$ [from R108](r108-operator-top-conductor-subpower-shared-cut.md). Keep the complete even shell, the original transported parent profiles $h,f$, the common taper, the $J^{-1}$ normalization and the separated high-denominator packet $\mathcal C_+(B,R)$. Preserve the original arithmetic gates $z,w_{\rm raw}>A,\ k>K\ge A/Q,\ (2k,b)<G$, the actual orientations and signs, all previous deletions, and the original unequal numerator detunings. Assume the same local Dirichlet GRH at the even target moduli and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Both original parity inputs are allowed, including the sharp variant of R86/R87 with $K\ge2P$. Keep the inherited polynomial parameter ranges.

At each actual alias $q=2k$ and denominator $b$ write

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
     q=r_bh_q,\quad s=dh_q,\quad q'=qb=r_bms .
 \tag{1}
$$

The factors $r_b,m,s$ are pairwise coprime, and $d,h_q$ have the same prime support. The full shared alias part $h_q$ includes every $q$-power on the primes of $b$. Denote the two genuine progression-character components on the three coprime factors by $(\alpha,\eta,\gamma)$ and $(\alpha',\eta',\gamma')$.

Fix $C,C_W>0$, $D,D_0,A_h,A_{\rm tame}\ge1$, and an integer $1\le W\le Q^{C_W}$. Set $V_Q=\lfloor(\log Q)^C\rfloor$ and $L_0=\lfloor\log Q\rfloor$. For a nonzero integer $t$ define the local tame product

$$
\mathcal T_s(t)=
             \prod_{\substack{p\mid(t,s)\\p>2}}\gcd(|t|,p-1).
 \tag{2}
$$

The empty product is one. The new parameter $A_{\rm tame}$ is separate from both the shared alias threshold $A_h$ and the raw cutoff $A$.

Only at $d\ge D_0,\ h_q\ge A_h$, delete the surviving pairs for which some integer tuple satisfies

$$
\begin{gathered}
 \operatorname{cond}(\alpha^j)\,
 \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)\,
 \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D,\\
 1\le j,u,v\le V_Q,\quad u\ne v,\qquad
 1\le a,c\le W,\quad \min(a,c)\le V_Q,\qquad
 |t|>L_0,\quad t=a-c,\quad \mathcal T_s(t)\le A_{\rm tame}.
 \end{gathered}
 \tag{3}
$$

Conductors mean primitive inducing conductors, including one for a principal character. No restriction to prime-power differences is imposed in (3). This is an incremental deletion in the actual R109 survivor, not a replacement of the old R109 cut. It is applied before the original unequal detunings.

With $Z_{\rm tame}$ the resulting field and $R_*=1+R$, the same packet norm satisfies

$$
\|Z_{\rm pp}-Z_{\rm tame}\|_{\rm pkt}
   \ll_{\Gamma,\Theta,C,C_W,\epsilon} Q^\epsilon A_{\rm tame} W
      \frac{BD}{\sqrt{D_0}A_h}
       \left[\frac{R_*^{3/2}+R_*^{5/2}}{Q}
                       +\frac{R_*^{1/2}}{S}\right].
 \tag{4}
$$

The bound permits arbitrary prime powers in the denominators and further restrictions of the deletion fixed by $k,b$, fixed orthogonal spatial compression, or restriction to a subset of the packet. It is uniform in the displayed $W$ range and the explicit $A_{\rm tame}$.

For a concrete choice, keep all previous thresholds and ranges, in particular the R109 numerical example and the prescribed subpower R108 budget at its $Q^{22/25}$ ceiling. At $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, take

$$
W=\lfloor Q^{1/100}\rfloor,\qquad A_{\rm tame}=2,\qquad
       D=Q^{87/100},\quad D_0=Q^{1/5},\quad A_h=Q^{9/50}.
 \tag{5}
$$

The incremental error is $O_{\epsilon,C}(Q^{-3/800+\epsilon})$; the inherited sharp $\widehat T,\widehat P$ comparison in the post-parity version remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm tame}$. This estimates the deleted sector, not the surviving covariance, an individual even modulus, another packet, or weak S. Section 4 supplies an actual newly eligible coefficient with two distinct exceptional shared primes at (5).

## 2. Separate the tame factors from an arithmetic support average

At fixed actual $q,b$ and full product $\nu=\nu_d\rho\bmod b$, the genuine partner is

$$
\alpha'=\bar\alpha,\qquad
      \eta'=\rho\bar\eta,\qquad
      \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{6}
$$

where $\pi_s$ is unit reduction to $d$. All earlier retained selections preserve the partner involution. The new selection (3) likewise preserves it: interchange both mixed exponent pairs, use conjugation invariance of the alias power conductor, and note $\mathcal T_s(-t)=\mathcal T_s(t)$. The smaller of the shared exponents is invariant. Therefore the same true character projection applies to each leg at fixed $\nu$, commuting with the original fixed reflected parity projections.

As in [R108 §2](r108-operator-top-conductor-subpower-shared-cut.md#2-count-only-the-true-live-shared-fibers), the literal unit translation by $q'/p$ at a shared prime annihilates the original coefficient if either shared leg misses its top local conductor. It fixes the congruence and the character of that leg but changes the phase by a nontrivial $p$-th root at each primitive numerator. Thus both shared legs may be taken locally primitive in each original orientation, exactly and before detuning. Split $s=s_t s_{\rm o}$, with $s_t=\prod_{p\mid(t,s)}p^{v_p(s)}$ its full prime-power part supported on primes dividing $t$. At every prime of $s_{\rm o}$, the shared output $\gamma^t(\nu_d\circ\pi_s)^c$ from (6) retains the top primitive conductor because $t$ is a unit there and the product lift factors below the top. In particular the shared power output has full conductor $s_{\rm o}$ on that factor, by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation). This step does not make any primitivity assertion about the output on $s_t$.

Write $T_j(n)$ for the size of the $j$-power kernel of the character group modulo $n$, with $T_j(1)=1$, and $H(n)=\sum_{1\le j\le V_Q}T_j(n)$. At a fixed tuple, the exact support fraction from [R108 (6)](r108-operator-top-conductor-subpower-shared-cut.md#2-count-only-the-true-live-shared-fibers) is bounded by

$$
O_{\Theta,\epsilon}\!\left(
        Q^\epsilon\frac{D\,T_j(r_b)T_{|u-v|}(m)T_{|t|}(s_t)}{r_bms}
                         \right).
 \tag{7}
$$

Indeed count the inputs on $s_{\rm o}$ by $\phi(s_{\rm o})$, canceling this factor in $\phi(q')$. On $r_bms_t$ the three translated power outputs must have product conductor at most $D/s_{\rm o}$. Their number is at most $(D/s_{\rm o})\tau(r_bms_t)$, with empty set if $D<s_{\rm o}$, and each output has at most the product of the three displayed kernel sizes as preimage. This is a count for the true fixed product (6), not for independent legs.

For every nonzero $t$ let $n_s(t)=\prod_{p\mid s}p^{v_p(|t|)}$, the entire part of $|t|$ supported on the primes of $s$, with no cutoff at the exponents of $s$. At an odd $p^E\parallel s_t$ the cyclic unit group gives the exact local kernel size $\gcd(|t|,p-1)p^{\min(v_p(|t|),E-1)}$. At $p=2$ its sign factor costs at most $2$, and the remaining cyclic part costs at most $2^{v_2(|t|)}$, including the small exponents. Multiplying gives, on (3),

$$
T_{|t|}(s_t)\le 2\mathcal T_s(t)n_s(t)
                                              \le 2A_{\rm tame}n_s(t).
 \tag{8}
$$

The tame product contains only actual shared primes of $t$; no bound on the full radical of $t$ or on the number of its prime factors is imposed.

Write each positive $n\le W$ as $n=a_0 b_0$, with $a_0=n_s(n)$ supported on the primes of $s$ and $(b_0,s)=1$. After dropping this coprimality in a positive upper sum, (8) gives

$$
\begin{split}
 \sum_{\substack{1\le n\le W\\\mathcal T_s(n)\le A_{\rm tame}}}
          T_n(s_n)
   &\le 2A_{\rm tame}
       \sum_{\substack{a_0\le W\\p\mid a_0\Rightarrow p\mid s}}
                      a_0\lfloor W/a_0\rfloor\\
   &\ll_{\Theta,C_W,\epsilon} Q^\epsilon A_{\rm tame}W .
 \end{split}
 \tag{9}
$$

For the last step, fix $0<\xi<1$. The number of supported $a_0\le W$ including $1$ is at most

$$
W^\xi\prod_{p\mid s}(1-p^{-\xi})^{-1}.
$$

The logarithm of the product is $O_\xi(\sum_{p\mid s}p^{-\xi})$. Ordering the distinct primes $p_i\mid s$ gives $p_i\ge i+1$; their number is $O_\Theta(1+\log Q)$ since $s$ is polynomially bounded. Therefore the logarithm is $O_{\Theta,\xi}((1+\log Q)^{1-\xi})=o(\log Q)$ uniformly. Choose $\xi$ small relative to $C_W,\epsilon$ and absorb $W^\xi$ and the product in $Q^\epsilon$. The argument allows any multiplicities in $s$, without a distribution result for primes.

At each signed difference $t$, the number of short-leg choices $(a,c)$ is at most $V_Q$, because the smaller member determines the larger. The two signs cost at most two. Likewise the multiplicity of each absolute nonzero $|u-v|$ is at most $2V_Q$. Sum (7), using (9), to bound the complete selected support fraction at fixed $q,b,\nu$ by

$$
O_{\Theta,C,C_W,\epsilon}\!\left(
        Q^\epsilon A_{\rm tame}W\,
          \frac{D H(r_b)H(m)}{r_bm d h_q}
                                   \right).
 \tag{10}
$$

Overlapping witnesses are allowed in this positive upper count. All earlier exclusions only reduce the support. In contrast to R109, the proof does not require a single exceptional prime on the actual $s_t$.

## 3. Transfer with the actual aliases, orientations and detunings

Apply the [R108 §3](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration) common-test estimate, or equivalently the transfer in [R109 §3](r109-operator-polynomial-prime-power-differences.md#3-keep-the-true-signs-aliases-and-detuning), with (10) in place of the original fraction. At each real $q,b,\nu$ this fraction scales the squared projected pointwise and integrated increment estimates for the genuine progression vectors, by normalized residue Parseval and the same auxiliary GRH. The fixed-product bilinear norm remains $O_\epsilon(Q^\epsilon\sqrt{d/(q,d)})$ by [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms), with the same arithmetic scalar and transpose sign. The same-vector selection in (6) preserves the cosine marginal and the skew common-interval raw translation in the two original difference orientations. The sum orientation uses the two pointwise factors and the optional reflected inputs keep their fixed commuting restrictions and derivative bounds. No marginal identity is asserted on a reflected input. Full numerator Parseval uses uniformity in $\nu$ and gives the unchanged additional $b$ factor. The per-alias common-test bound is consequently

$$
O_\epsilon\!\left(Q^\epsilon A_{\rm tame}W b
      \sqrt{\frac{d}{(q,d)}}\
       \frac{D H(r_b)H(m)}{r_bm d h_q}\,\mathcal K\right)
 \tag{11}
$$

with exactly the original seminorms from [R109 (10)](r109-operator-polynomial-prime-power-differences.md#3-keep-the-true-signs-aliases-and-detuning) and [R108 (9)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration), including the additional reflected terms when used. The fraction occurs once in this bound, from the product of the square roots of the two vector estimates, not squared.

At fixed $b,d$, the true alias group has $h_q\ge U=\max(A_h,\operatorname{rad}d)$, all its primes in $d$, $r_bh_q\le8M$, and $(q,d)\ge\operatorname{rad}d$. As in [R108 (10)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration), use the harmonic sum of $H(r_b)/r_b$ from [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) and the supported $h_q$ harmonic tail to obtain $O_\epsilon(Q^\epsilon D H(m)/(m\sqrt{d\operatorname{rad}d}\,U))$ for the sum of the arithmetic factors in (11) before the common $A_{\rm tame}W b\mathcal K$. Then the true unitary divisor groups, $d\ge D_0,\ U\ge A_h$, the radical sum and the $H(m)/m$ harmonic bound give the exact same positive denominator square bound $O_\epsilon(Q^\epsilon B^2D^2/(D_0 A_h^2))$ before the common $A_{\rm tame}W$, as in [R108 (12)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration). No primality of $d$ or $h_q$ is needed in that step.

For the original unequal detunings take the Taylor recovery of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field), keeping the true exterior phase and coefficient bounded by $2^{-n}$ at order $n$. The weighted seminorms at integer offset $\ell$ are $O(1+|\ell|)$ and $O(S^{-1}+(1+|\ell|)^2/Q)$, exactly as in [R109 §3](r109-operator-polynomial-prime-power-differences.md#3-keep-the-true-signs-aliases-and-detuning). With the original $J\asymp Q$, the square sum over $|\ell|\le R+1$ supplies the bracket of (4). This proves (4). At (5) the prefactor $WBD/(\sqrt{D_0}A_h)$ has exponent $99/100$, so the bracket yields the three exponents $-1/160,-3/800,-19/4000$, respectively. All other sharp parity, edge and benchmark restorations are unchanged, giving the stated sharp comparison by the triangle inequality.

## 4. A live coefficient beyond every earlier prime-power selection

At the concrete scales (5) use the genuine alias of [R109 §4](r109-operator-polynomial-prime-power-differences.md#4-an-actual-new-coefficient-at-polynomial-exponent-size):

$$
d=3\cdot2^e\asymp Q^{1/5},\quad
 3^\ell\asymp Q^{37/200},\quad
 r\asymp Q^{411/1000},\quad m\in(B/(2d),B/d),
 \qquad k=3^\ell r,\quad q=2k,\quad b=dm .
$$

Here $d$ is the least number of that form at least $D_0$; $r,m>3$ are distinct primes as in R109. Thus $h_q=2\cdot3^\ell,\ s=2^{e+1}3^{\ell+1}$, $(q,b)=6<G$, and $h_q\ge A_h$. The true denominator band and long-alias gate are the same as there, with $k\asymp Q^{596/1000}$. Keep the conjugate generators at $r$, the generator $\eta$ and partner $\eta'=\eta^{2V^*}$ on $m$, and the primitive conjugate tame-trivial pair at $3^{\ell+1}$ of R109. The integer $V^*$ bounds all finitely many fixed log-power ranges of $r,m$-leg exponents, so their previously tested nonzero powers and mixed powers have conductors $r,m$ as there. In particular $r>Q^{51/125}$ and $rm\asymp Q^{601/1000}>Q^{3/5}$, and the true full product keeps its $m$-component.

Put $\delta=1/100$ and choose

$$
j_2=\lfloor\delta\log_2 Q\rfloor-3,\qquad
       W_*=1+3\cdot2^{j_2},\qquad
       t_0=\left\lfloor \tfrac8{100}\log_2Q\right\rfloor .
 \tag{12}
$$

Then $W_*\le W$ for large $Q$, $W_*$ is odd, and $W_*-1\asymp Q^\delta$. At $2^{e+1}$ let $\gamma_2$ be the same sign-trivial primitive character of $5$-order $2^{e-1}$, and set

$$
\gamma'_2=\gamma_2^{-W_*+2^{e-1-t_0}} .
 \tag{13}
$$

Its odd exponent makes it primitive; the true product has exponent $-3\cdot2^{j_2}+2^{e-1-t_0}$ of valuation exactly $j_2$. Its conductor $2^{e+1-j_2}=Q^{1/5-\delta+o(1)}$ divides the true $2^e$-part of $d$. Together with the principal $3$-product this verifies the genuine product condition. Fixed polylog powers of the shared product retain conductor $Q^{1/5-\delta-o(1)}$; hence the earlier small shared-product cut is avoided and the earlier shared-equal joint conductors are at least $Q^{801/1000-\delta-o(1)}$, above the [R101](r101-operator-three-factor-equal-exponents.md) and [R102](r102-operator-shared-equal-gauss-conductor.md) ceilings. The other earlier cuts involving only the unchanged $r,m$ factors and the full product have the same exclusions as the R109 witness.

For every pair of unequal positive shared exponents from the old R108 subpower range or any older fixed log-power range, $a-W_*c\ne0$ and $|a-W_*c|\le Q^{\delta+o(1)}$. Its $2$-adic valuation is less than $e-1-t_0$, so the exponent $a-W_*c+c2^{e-1-t_0}$ at $2$ has that same valuation. The resulting $2$-conductor is at least $Q^{1/5-\delta-o(1)}$, and the $3$-conductor remains $Q^{37/200-o(1)}$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation) since the old nonzero difference is subpower. Thus the older jointly tested unequal products have conductor at least $Q^{986/1000-\delta-o(1)}>Q^{22/25}$, and the earlier small individual shared cut also fails.

It remains to check every R109 prime-power tuple at its actual polynomial range. If $a=W_*c$ for positive $a,c$, their difference would be $3\cdot2^{j_2}c$, which is not a prime power. Otherwise $|a-W_*c|\le Q^{2\delta+o(1)}$ since $a,c\le W$, and its valuation again stays below $e-1-t_0$. The old $2$-conductor is therefore at least $Q^{1/5-2\delta-o(1)}$. For any nonzero old difference of absolute size at most $W$, the $3$-conductor is at least $Q^{37/200-\delta-o(1)}$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation), because its valuation at $3$ is strictly below $\ell$. Multiplying these two bounds and the unavoidable $r m$ shows that every R109 tested tuple has joint conductor at least

$$
Q^{986/1000-3\delta-o(1)}
                         =Q^{956/1000-o(1)}>Q^{87/100}.
$$

This verifies survival on the actual preceding field, not just failure of the old test for one tuple.

The original primitive-numerator incidence is nonzero in the unmodified parity input. At $2$ the congruence modulo $2$ is automatic on the odd units; both new primitive Gauss factors are nonzero at the actual unit frequencies. The unchanged $3,r,m$ factors are the exact nonzero factors of [R105 §4](r105-operator-large-shared-alias-joint-cut.md#4-a-live-witness-on-a-large-shared-alias-with-radical-six) and [R109 §4](r109-operator-polynomial-prime-power-differences.md#4-an-actual-new-coefficient-at-polynomial-exponent-size): the unique unit frequency on the $3$-part, the conjugate pairing at $r$, and the primitive additive Gauss factors at $m$.

Now choose the tuple $(j,u,v,a,c)=(1,2,1,W_*,1)$. Its difference $t=3\cdot2^{j_2}$ has two distinct prime factors, both genuinely shared; moreover $\mathcal T_s(t)=\gcd(t,2)=2$ at the odd exceptional prime $3$. Its $2$-conductor is exactly $2^{t_0+2}$, since (13) cancels $W_*$. Its $3$-conductor is $3^\ell$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation) with $v_3(t)=1<\ell$. Thus the new joint conductor is

$$
rm\,3^\ell\,2^{t_0+2}
                    =Q^{866/1000+o(1)}<Q^{87/100}.
$$

This coefficient is an actual original nonzero incidence strictly newly eligible at (5). It gives no lower bound after integration or sharp parity projection, and no bound for the remaining covariance.
