# A polynomial shared exponent range for prime-power differences

A prime-power exponent difference has at most one exceptional prime in the forced-conductor split. Summing those differences in the true top-primitive fibers, and allowing either shared exponent to be the short one, lowers the cost of the shared exponent range from the fourth power to the first power. This allows a genuinely polynomial shared range on a further sector of the actual preceding packet.

## 1. The exact additional deletion

Start from the genuine field $Z_{\rm top}$ of [R108 §1](r108-operator-top-conductor-subpower-shared-cut.md#1-the-exact-incremental-deletion) with a prescribed old shared budget $W_{\rm old}=Q^{o(1)}$ and all its previous selections unchanged. Use the same complete even shell, original transported parent profiles $h,f$, common taper, $J^{-1}$ normalization and separated high-denominator packet $\mathcal C_+(B,R)$. Preserve the genuine $z,w_{\rm raw}>A,\ k>K\ge A/Q,\ (2k,b)<G$, original signs, and all distinct numerator detunings. Assume the same local Dirichlet GRH at the even target moduli and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Both original parity inputs are allowed, including the sharp parity variant of R86/R87 with $K\ge2P$. Keep the original polynomial parameter bounds.

At each actual alias $q=2k$ and denominator $b$, keep the exact factorization

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
        q=r_bh_q,\quad s=dh_q,\quad q'=qb=r_bms .
 \tag{1}
$$

Here $d,h_q$ have the same prime support and $r_b,m,s$ are pairwise coprime. Write $(\alpha,\eta,\gamma)$, $(\alpha',\eta',\gamma')$ for the two genuine progression-character factors on these three moduli. In particular $h_q$ is the full part of $q$ on primes of $b$, not just $(q,b)$.

Fix $C>0$, $D,D_0,A_h\ge1$, and integer $W\ge1$. Put $V_Q=\lfloor(\log Q)^C\rfloor$, $L_0=\lfloor\log Q\rfloor$. Only at $d\ge D_0,\ h_q\ge A_h$ delete the remaining pairs for which

$$
\begin{gathered}
 \operatorname{cond}(\alpha^j)\,
 \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)\,
 \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D,\\
 1\le j,u,v\le V_Q,\quad u\ne v,\qquad
 1\le a,c\le W,\quad \min(a,c)\le V_Q,\qquad
 |a-c|=p^\beta>L_0
 \end{gathered}
 \tag{2}
$$

for at least one integer tuple, with $p$ any prime and $\beta\ge1$ an integer. Conductors always mean primitive inducing conductors, with one for a principal character. The inequality on the minimum allows either leg to be short; fixing the same leg as short would not preserve the partner symmetry used below. This is a deletion in the actual R108 survivor, before the original distinct detunings. All previous deletions remain part of the input.

With $Z_{\rm pp}$ denoting the resulting field and $R_*=1+R$, the packet estimate uniform in $W$ is

$$
\|Z_{\rm top}-Z_{\rm pp}\|_{\rm pkt}
   \ll_{\Gamma,\Theta,C,\epsilon} Q^\epsilon W
        \frac{BD}{\sqrt{D_0} A_h}
     \left[\frac{R_*^{3/2}+R_*^{5/2}}Q
                             +\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

It allows arbitrary prime powers in the denominators and persists after the inherited fixed orthogonal compression, restriction to a subset of the packet, or further deletion restrictions fixed by $k,b$. An empty exponent range is immediate.

At $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, keep the earlier thresholds, including the old $Q^{22/25}$ threshold at the prescribed subpower range in R108, and set

$$
D_0=Q^{1/5},\qquad A_h=Q^{9/50},
       \qquad W=\lfloor Q^{1/100}\rfloor,\qquad D=Q^{87/100}.
 \tag{4}
$$

Then the new deletion is $O_{\epsilon,C}(Q^{-3/800+\epsilon})$. The inherited sharp $\widehat T,\widehat P$ comparison in the post-parity input remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm pp}$. At the same $W,D$ the general fourth-power estimate alone from R108 pays an extra $Q^{3/100}$, more than the saving in (3). The present bound is for the specified deleted sector, not a bound on the surviving covariance, a prescribed even modulus, other packets, or weak S.

## 2. Sum the actual exceptional local fibers over the differences

Fix the actual $q,b$ and full product $\nu=\nu_d\rho\bmod b$. The genuine partner remains

$$
\alpha'=\bar\alpha,\qquad
    \eta'=\rho\bar\eta,\qquad
    \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{5}
$$

where $\pi_s$ is unit reduction to $d$. The same-vector projection at fixed $\nu$ is valid for (2): conjugating the alias character does not change the conductor of its power, and the simultaneous swaps $u\leftrightarrow v$, $a\leftrightarrow c$ preserve the product of the other two conductors and the prime-power and short-leg gates. All the earlier true retained selections preserve this partner involution.

As in [R108 §2](r108-operator-top-conductor-subpower-shared-cut.md#2-count-only-the-true-live-shared-fibers), terms in which a shared leg misses the top local conductor vanish at each primitive numerator in each original orientation before the detunings. Thus both shared legs can be assumed locally primitive, exactly and with no change to the field. For a fixed allowed tuple and $t=a-c\ne0$, divide $s=s_t s_{\rm o}$, with $s_t$ the full prime-power part of $s$ supported on primes dividing $t$. On $s_{\rm o}$ the true translated power $\gamma^t(\nu_d\circ\pi_s)^c$ has forced full conductor $s_{\rm o}$. This is [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation) at valuations zero, or equivalently the fact that the $\gamma^t$ factor survives on every top local kernel there while the lifted product is trivial on it. In counting support at fixed full $\nu$, count the shared inputs on $s_{\rm o}$ freely and require the remaining output conductor on $r_bms_t$ to be at most $D/s_{\rm o}$. In particular there is no support if $D<s_{\rm o}$.

For an integer $l\ge1$, let $T_l(n)$ be the size of the kernel of the $l$-th power map on the character group of $n$, including $T_l(1)=1$, and put $H(n)=\sum_{1\le l\le V_Q}T_l(n)$. Exactly as in [R108 (6)](r108-operator-top-conductor-subpower-shared-cut.md#2-count-only-the-true-live-shared-fibers), the fraction of normalized progression-character support at the fixed tuple is

$$
O_{\Theta,\epsilon}\!\left(
   Q^\epsilon\frac{D T_j(r_b) T_{|u-v|}(m) T_{|t|}(s_t)}
                          {r_bms}\right).
 \tag{6}
$$

Indeed the $\phi(s_{\rm o})$ upper bound for its unrestricted inputs cancels the identical factor in $\phi(q')$, and the translated-power fibers on the other factors have the three displayed torsion counts. A product output conductor of size at most $D/s_{\rm o}$ on those factors has at most $(D/s_{\rm o})\tau(r_bms_t)$ possible choices. This uses the actual product in (5), not a count on two independent progression-character legs.

Here $|t|=p^\beta$ has just one prime. If $p\nmid s$ then $T_{p^\beta}(s_t)=1$. If $p\mid s$ and $E=v_p(s)$, then

$$
T_{p^\beta}(p^E)\le 2p^\beta .
 \tag{7}
$$

For odd $p$, the cyclic unit group gives the sharper $p^{\min(\beta,E-1)}$ since $p^\beta$ is coprime to $p-1$. For $p=2$, the sign and cyclic factors give at most $2^{1+\min(\beta,E-2)}$ for $E\ge3$, and the small exponents also satisfy (7). Thus

$$
\sum_{\substack{L_0<n\le W\\ n\ \mathrm{prime\ power}}}T_n(s_n)
        \le W+\sum_{p\mid s}\sum_{\substack{\beta\ge1\\p^\beta\le W}}2p^\beta
        \ll W(1+\omega(s)).
 \tag{8}
$$

The first term covers differences with no prime on $s$, and for each remaining prime the geometric sum is at most $4W$. The bound is uniform in all local powers $E$, and $1+\omega(s)\ll_\Theta 1+\log Q$ in the inherited polynomial range. At a fixed signed difference $t$, the short-leg gate in (2) allows at most $V_Q$ ordered pairs: the smaller exponent is the free one, and the larger is determined. Both signs cost a factor at most two. For $u,v$ of a prescribed nonzero signed difference there are at most $V_Q$ pairs, so the sum over the $j,u,v$ ranges in (6) is bounded by $O(V_Q H(r_b)H(m))$. Combining with (8) proves that the support for the full union at each actual $q,b,\nu$ has fraction

$$
O_{\Theta,C,\epsilon}\!\left(
        Q^\epsilon W\,\frac{D H(r_b)H(m)}{r_bm d h_q}\right).
 \tag{9}
$$

This is a sum of positive upper counts, hence allows overlaps, and all previously retained restrictions only reduce it. No equidistribution of the eligible differences or covariance of their fields is assumed.

## 3. Keep the true signs, aliases and detuning

Apply the original [R108 §3](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration) transfer with (9) in place of [R108 (8)](r108-operator-top-conductor-subpower-shared-cut.md#2-count-only-the-true-live-shared-fibers). For clarity, the fixed-product bilinear estimate on the genuine pair has unchanged norm $O_\epsilon(Q^\epsilon\sqrt{d/(q,d)})$ as in [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms). The uniform fraction (9) multiplies the squared projected pointwise norm and the squared integrated increment bound on the true GRH progression vectors by normalized residue Parseval. Their square-root factors multiply to one power of the fraction. The same projection acts on both legs by (5) and the invariant sector in (2), and fixed reflected parity projections still commute with it. Thus the cosine marginal and skew common-interval raw translation for the original difference signs, the two pointwise factors for the sum sign, and the original derivative bounds on the sharper reflected inputs all apply. No marginal identity on a reflected input is substituted for its actual one. Full numerator Parseval then contributes the same factor $b$ uniformly in the full product. The resulting per-alias common-test bound is

$$
O_\epsilon\!\left(Q^\epsilon\,W b\sqrt{\frac{d}{(q,d)}}
       \frac{D H(r_b)H(m)}{r_bm d h_q}\,\mathcal K\right),
 \tag{10}
$$

with precisely the common seminorms $\mathcal K$ of [R108 (9)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration), including the extra reflected terms when used.

For fixed $b,d$, set $U=\max(A_h,\operatorname{rad}d)$. The actual aliases have $r_bh_q\le8M$, their $h_q$'s are supported on the primes of $d$ with $h_q\ge U$, and $(q,d)\ge\operatorname{rad}d$. Without the common $Q^\epsilon Wb\mathcal K$, their summed factor in (10) is therefore bounded by

$$
Q^\epsilon\frac{D H(m)}{m\sqrt{d\operatorname{rad}d}\, U}.
 \tag{11}
$$

This is [R108 (10)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration), using the supported harmonic tail and the harmonic $H(r_b)/r_b$ bound on the genuine alias grouping. Cauchy over the unitary divisor groups at each $b$, $U\ge A_h$, and $\sum_{d\le B}1/\operatorname{rad}d\ll_\epsilon Q^\epsilon$ give the identical denominator square bound $O_\epsilon(Q^\epsilon B^2D^2/(D_0A_h^2))$ in [R108 (12)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration) before restoring the common $W$. The $m$-weight there is the same convergent-in-budget harmonic square from [R90](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) as in R108; no joint independence or additional control of $m,d$ is required.

Restore the original Taylor detunings by [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) as in [R108 §3](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration), keeping the actual exterior phase and its $2^{-n}$ output coefficient bound at Taylor order $n$. At integer offset $\ell$, the costs are $O(1+|\ell|)$ and $O(S^{-1}+(1+|\ell|)^2/Q)$, and the $J^{-1}$ normalization with $J\asymp Q$ gives precisely the bracket in (3) by the square sum over $|\ell|\le R+1$. This proves (3). At (4), $WBD/(\sqrt{D_0}A_h)$ has exponent $99/100$; the three terms of the bracket give final exponents $-1/160,-3/800,-19/4000$. The inherited sharp comparison follows by the triangle inequality with no change to the sharp edge, parity or benchmark restorations.

## 4. An actual new coefficient at polynomial exponent size

Use the scales (4) and the genuine alias of [R108 §4](r108-operator-top-conductor-subpower-shared-cut.md#4-a-live-coefficient-with-strictly-larger-shared-exponents). Choose $d=3\cdot2^e\asymp Q^{1/5}$ by taking the least $e$ with $d\ge D_0$, $3^\ell\asymp Q^{37/200}$, and distinct odd primes $r\asymp Q^{411/1000}$ and $m\in(B/(2d),B/d)$ as in that proof. Put $k=3^\ell r,\ q=2k,\ b=dm$, so $h_q=2\cdot3^\ell$, $s=2^{e+1}3^{\ell+1}$. The same arithmetic gates hold ($k$ has exponent $596/1000$, $(q,b)=6<G$, $h_q\ge A_h$, with the denominator in the true high band). Keep the conjugate generators on $r$, the generator $\eta$ and partner $\eta'=\eta^{2V^*}$ on $m$, and the primitive conjugate pair trivial on the tame part at $3^{\ell+1}$. Here $V^*$ bounds all finitely many fixed polylog ranges on the alias and coprime denominator legs. Their old powers and mixed powers keep the required prime conductors $r,m$, as in R108. In particular $r>Q^{51/125}$, $rm\asymp Q^{601/1000}>Q^{3/5}$, and the full product retains its high $m$-part.

Write $\delta=1/100$, select the integers

$$
j_2=\lfloor\delta\log_2Q\rfloor-1,\qquad
 W_*=1+2^{j_2},\qquad
 t_0=\left\lfloor\tfrac8{100}\log_2Q\right\rfloor .
 \tag{12}
$$

For large $Q$ we have $W_*\le W$, $W_*$ odd, and $W_*-1\asymp Q^\delta>L_0$. At $2^{e+1}$, keep the sign-trivial primitive $\gamma_2$ of $5$-order $2^{e-1}$ and take

$$
\gamma'_2=\gamma_2^{-W_*+2^{e-1-t_0}} .
 \tag{13}
$$

This is primitive since the exponent is odd. The true product has exponent $1-W_*+2^{e-1-t_0}$, with valuation exactly $j_2$ since $e-1-t_0>j_2$. Its conductor is $2^{e+1-j_2}=Q^{1/5-\delta+o(1)}$ and divides $2^e$. Its fixed polylog powers retain conductor $Q^{1/5-\delta-o(1)}$; the $3$-product is principal, so the character pair satisfies the actual full-product condition. These conductors exclude the earlier shared-product cut [R98](r98-operator-shared-product-power-cut.md) and the small shared-equal branches: the latter have joint conductor at least $Q^{801/1000-\delta-o(1)}$, above the [R101](r101-operator-three-factor-equal-exponents.md) and [R102](r102-operator-shared-equal-gauss-conductor.md) ceilings. The other earlier masks involving only $r,m$ or products are the same as in the R108 witness.

For every old pair of positive unequal shared exponents in R108's prescribed subpower range, and likewise in each of the older fixed polylog ranges, $a-W_*c\ne0$, since $W_*\asymp Q^\delta$ exceeds the entire old range and $c\ge1$. Its absolute size is at most $Q^{\delta+o(1)}$, so its $2$-adic valuation is at most $(\delta+o(1))\log_2Q$, less than $e-1-t_0$. Hence the exponent $a-W_*c+c2^{e-1-t_0}$ in the old mixed power has that same valuation. The $2$-conductor is at least $Q^{1/5-\delta-o(1)}$; the $3$-conductor is $Q^{37/200-o(1)}$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation), because the nonzero old difference is subpower. Thus in every old jointly tested unequal relation the true product conductor is at least $Q^{986/1000-\delta-o(1)}$, above even the largest old $Q^{22/25}$. The earlier smaller individual shared cut [R99](r99-operator-unequal-shared-leg-powers.md) also fails. This checks retention when all qualifying tuples in the old ranges are tested up to their respective ceilings, not only retention of the one tuple used next.

The original incidence is genuinely nonzero at a primitive numerator in the unmodified parity input. At $2$, congruence modulo $2$ is automatic on the odd units and both new primitive Gauss factors at the actual unit frequencies are nonzero. The unchanged $3,r,m$ local factors are nonzero by the exact computation in [R105 §4](r105-operator-large-shared-alias-joint-cut.md#4-a-live-witness-on-a-large-shared-alias-with-radical-six) and [R108 §4](r108-operator-top-conductor-subpower-shared-cut.md#4-a-live-coefficient-with-strictly-larger-shared-exponents): the $3$-part has the unique surviving unit frequency of the primitive local Fourier transform, the $r$-part is the actual conjugate pairing, and the $m$ factors are primitive additive Gauss sums.

Finally choose $(j,u,v,a,c)=(1,2,1,W_*,1)$. It has $\min(a,c)=1$ and $|a-c|=2^{j_2}$, a genuine prime power at polynomial size. The shared $2$-conductor is now exactly $2^{t_0+2}$, because (13) cancels $W_*$ in this relation. Its $3$-conductor is the full $3^{\ell+1}$ since $3\nmid W_*-1$. The total is

$$
rm\,3^{\ell+1}\,2^{t_0+2}
                       =Q^{866/1000+o(1)}<Q^{87/100}.
$$

This is strictly new eligibility of a nonzero original incidence coefficient beyond the prescribed subpower selections. It is not an integrated decrement lower bound, a statement about survival in the sharply projected parity input, or a bound on the residual covariance.
