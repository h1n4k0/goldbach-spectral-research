# Jointly attainable exterior tame overlap on the finite range

Clipping an exterior tame modulus at the finite complement budget still counts overlaps at different primes independently. A single complement may be too small to realize all of them together. Maximizing over jointly attainable divisors gives a stronger conditional deletion in the actual packet. A two-sided statement below concerns only the underlying arithmetic gcd average, not the selected character count or the packet norm.

## 1. Exact further deletion

Start from the genuine $Z_{\rm fin}$ of [R112 §1](r112-operator-finite-complement-defect.md#1-exact-further-deletion), preserving all earlier deletions and the prescribed R108 subpower range. Keep the complete even shell, actual transported parent profiles $h,f$, common taper, $J^{-1}$ normalization, and separated high-denominator packet $\mathcal C_+(B,R)$. The true orientations, signs and unequal numerator detunings, and the original $z,w_{\rm raw}>A,\ k>K\ge A/Q,\ (2k,b)<G$, are unchanged. Assume original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Both original parity inputs apply, including the sharp variant of R86/R87 with $K\ge2P$. Keep the inherited polynomial parameter ranges.

For each actual alias $q=2k$ and denominator $b$ write

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
         q=r_bh_q,\quad s=dh_q,\quad q'=qb=r_bms .
 \tag{1}
$$

The factors $r_b,m,s$ are pairwise coprime, and $d,h_q$ have the same prime support. Write $(\alpha,\eta,\gamma)$, $(\alpha',\eta',\gamma')$ for the two genuine progression-character components on these three factors.

Fix $C,C_W>0$, $D,D_0,A_h,A_{\rm joint}\ge1$, and an integer $1\le W\le Q^{C_W}$; write $V_Q=\lfloor(\log Q)^C\rfloor$, $L_0=\lfloor\log Q\rfloor$. For a nonzero signed difference $t$ with $|t|\le W$, put $|t|=a_0b_0$ where $a_0=n_s(t)=\prod_{p\mid s}p^{v_p(|t|)}$ and $(b_0,s)=1$. With fixed $s,a_0,W$, let $V=\lfloor W/a_0\rfloor$. For odd $p\mid a_0$ let $I_p$ be the full part of $p-1$ supported on the primes of $s$, and $L_p=(p-1)/I_p$, as in [R111 (2)](r111-operator-external-tame-lcm-defect.md#1-the-actual-further-deletion). In the notation of [R112 (2)](r112-operator-finite-complement-defect.md#1-exact-further-deletion), take the clipped $L_{p,[V]}$ and put $L=L_{[V]}=\operatorname{lcm}_{p\mid a_0,\,p>2}L_{p,[V]}$. For $g\mid L$ define

$$
B_L(g)=\frac{\prod_{p\mid a_0,\,p>2}\gcd(g,L_{p,[V]})}{g},\qquad
 J_L(V)=\max_{\substack{g\mid L\\1\le g\le V}}B_L(g),\qquad
 \mathcal E^{\rm joint}_{s,W}(a_0)
        =J_L(V)\prod_{\substack{p\mid a_0\\p>2}}\gcd(a_0,I_p).
 \tag{2}
$$

Empty products and the empty lcm are one, and $g=1$ is always eligible for the maximum. The defect in (2) depends on $s,a_0,W$, not the actual individual complement $b_0$.

Only at $d\ge D_0,\ h_q\ge A_h$, delete the remaining pairs for which some integer tuple satisfies

$$
\begin{gathered}
 \operatorname{cond}(\alpha^j)
 \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)
 \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D,\\
 1\le j,u,v\le V_Q,\quad u\ne v,\qquad
 1\le a,c\le W,\quad\min(a,c)\le V_Q,\\
 t=a-c,\quad |t|>L_0,\qquad
                    \mathcal E^{\rm joint}_{s,W}(n_s(t))\le A_{\rm joint}.
 \end{gathered}
 \tag{3}
$$

Conductors are primitive inducing conductors, with one for the principal character. Use the actual original pairing, not an arbitrary joint mask. This deletion is taken before the original unequal detunings. We retain all previous deletions.

Let $Z_{\rm joint}$ be the resulting field and $R_*=1+R$. The packet estimate is

$$
\|Z_{\rm fin}-Z_{\rm joint}\|_{\rm pkt}
  \ll_{\Gamma,\Theta,C,C_W,\epsilon} Q^\epsilon A_{\rm joint}W
       \frac{BD}{\sqrt{D_0} A_h}
   \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{4}
$$

It allows arbitrary denominator prime powers, further deletion restrictions fixed by $k,b$, fixed orthogonal spatial compression, and restriction to a subset of the packet.

At the inherited numerical choices $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, keep all preceding thresholds and take

$$
D_0=Q^{1/5},\quad A_h=Q^{9/50},\quad W=\lfloor Q^{1/100}\rfloor,\quad
                    D=Q^{87/100},\quad A_{\rm joint}=20 .
 \tag{5}
$$

The new error is $O_{\epsilon,C}(Q^{-3/800+\epsilon})$, with the same inherited sharp $\widehat T,\widehat P$ comparison $O_{\epsilon,C}(Q^{-1/500+\epsilon})$ in the post-parity version, now to $Z_{\rm joint}$. Section 4 gives a new genuine coefficient surviving the earlier masks even if the old R112 finite cap is raised to the same $20$ as (5), with its other choices kept fixed. The claim only estimates this deletion, not the surviving covariance, an individual even modulus, another packet, or weak S.

## 2. The finite exterior average and its arithmetic size

Write $I=\prod_{p\mid a_0,\,p>2}\gcd(a_0,I_p)$ and $P_V(b_0)=\prod_{p\mid a_0,\,p>2}\gcd(b_0,L_{p,[V]})$ at this fixed support. For any $g\mid L$, $B_L(g)$ is an integer: at every prime of $g$, an index attaining the maximal modulus valuation supplies the full $g$-valuation. By the same comparison, if $g_\ell$ denotes $v_\ell(g)$ and $e_{p,\ell}=v_\ell(L_{p,[V]})$, the valuation of $B_L(g)$ is
$\sum_p\min(g_\ell,e_{p,\ell})-g_\ell$. Removing a maximizing index of $e_{p,\ell}$ leaves only the other terms, all bounded by the corresponding modulus valuations. Consequently

$$
J_L(V)\le \frac{\prod_{p\mid a_0,\,p>2} L_{p,[V]}}{L},
            \qquad \mathcal E^{\rm joint}_{s,W}(a_0)
                       \le\mathcal E^{\rm fin}_{s,W}(a_0).
 \tag{6}
$$

This is a simultaneous bound across primes. The maximum can be smaller because the divisor containing every individually admissible overlap need not be at most $V$.

For any positive $b_0\le V$, its $g=\gcd(b_0,L)$ is an admitted divisor. Since each $L_{p,[V]}\mid L$,

$$
P_V(b_0)= B_L(\gcd(b_0,L))\,\gcd(b_0,L)
                            \le J_L(V)\gcd(b_0,L).
 \tag{7}
$$

By the divisor identity, $\sum_{b_0\le V}\gcd(b_0,L)\le V\tau(L)$. Thus the arithmetic mean $V^{-1}\sum_{b_0\le V,\,(b_0,s)=1}P_V(b_0)$ is at most $J_L(V)\tau(L)$. Here the units have the original finite complement range, and we dropped the coprimality only in an upper sum of positive terms.

In fact this scale of the exterior gcd average is sharp up to $Q^\epsilon$ in the stated polynomial parameter ranges:

$$
J_L(V)Q^{-\epsilon}\ll_{\Theta,C_W,\epsilon}
   \frac1V\sum_{\substack{1\le b_0\le V\\(b_0,s)=1}}P_V(b_0)
       \le J_L(V)\tau(L)
       \ll_{C_W,\epsilon} J_L(V)Q^\epsilon .
 \tag{8}
$$

For the lower bound take a maximizing $g_*\mid L$, $g_*\le V$. All positive $b_0=g_*j\le V$ have $P_V(b_0)\ge P_V(g_*)=g_*J_L(V)$. Also $(g_*,s)=1$, so the allowed $j$'s are those coprime to $s$. For real $U=V/g_*\ge1$, the number of $j\le U$ coprime to $s$ is $\gg_{\Theta,\epsilon}UQ^{-\epsilon}$: when $U<Q^{\epsilon/2}$, use $j=1$; when $U\ge Q^{\epsilon/2}$, inclusion–exclusion gives $U\phi(s)/s+O(2^{\omega(s)})$. Uniformly for polynomially bounded $s$, $2^{\omega(s)}=Q^{o(1)}$ and $\phi(s)/s\ge2^{-\omega(s)}$, so for large $Q$ the main term dominates the error and gives the claimed bound. One can see the uniform subpower bound by ordering distinct primes $p_i\mid s$ and using $p_i\ge i+1$, hence $s\ge(\omega(s)+1)!$. Integrating this positive subfamily over $b_0$ proves the lower estimate in (8). The final upper bound follows from $L\le\prod L_p\le\operatorname{rad}(a_0)\le W$. Without the unit restriction the same argument even gives $J_L(V)/2$ as a lower bound.

The sharpness in (8) is only for the arithmetic exterior gcd envelope over all unit complements at fixed support. It is not a lower bound after the shared exponent, conductor or prior selection masks, is not a claim about the actual number of participating character pairs, and gives no operator or covariance lower bound.

## 3. True support count and packet transfer

Fix $q,b$ and the actual full product $\nu=\nu_d\rho\bmod b$. The original pairing is

$$
\alpha'=\bar\alpha,\qquad
  \eta'=\rho\bar\eta,\qquad
  \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{9}
$$

where $\pi_s$ is unit reduction to $d$. Swapping the two mixed exponent pairs, and conjugating the alias power, leaves the condition (3) unchanged. In particular the sign of $t$ does not affect the supported part, the finite defect or the short exponent gate. Hence the new test, together with all inherited masks, is the same true character projection on both legs at fixed $\nu$, commuting with the fixed reflected parity projections.

Use the exact top-primitivity reduction of [R108 §2](r108-operator-top-conductor-subpower-shared-cut.md#2-count-only-the-true-live-shared-fibers) on the actual original incidences. For $s_t=\prod_{p\mid(t,s)}p^{v_p(s)}$, the shared output $\gamma^t(\nu_d\circ\pi_s)^c$ has forced full conductor on $s/s_t$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation). Let $T_l(n)$ be the size of the $l$-th power kernel on the character group of $n$, with $T_l(1)=1$, and $H(n)=\sum_{l\le V_Q}T_l(n)$. At fixed tuple the normalized support fraction is bounded by

$$
O_{\Theta,\epsilon}\!\left(
       Q^\epsilon\frac{D\,T_j(r_b)T_{|u-v|}(m)T_{|t|}(s_t)}{r_bms}\right)
 \tag{10}
$$

as in [R112 (7)](r112-operator-finite-complement-defect.md#2-exact-clipping-and-the-finite-exterior-average). This uses the full conductor factor $s/s_t$ in the budget, cancels its free input count against its totient factor, and counts the three remaining translated power fibers at the true fixed product.

For each actual $b_0\le V$, the clipping equality $\gcd(b_0,L_p)=\gcd(b_0,L_{p,[V]})$ is exact. The product of local wild kernel factors is at most $a_0$, with cost at most $2$ for the sign part at $2$. On this range the exterior tame product is $P_V(b_0)$ and the intrinsic tame product is $I$. Thus the local group bounds used in [R112 (9)](r112-operator-finite-complement-defect.md#2-exact-clipping-and-the-finite-exterior-average) give $T_{|t|}(s_t)\le2a_0 I P_V(b_0)$. By (7) and the upper bound of (8), at a supported $a_0$ passing the gate the sum over its true complement range is at most $2a_0 V\tau(L)A_{\rm joint}$. Since $a_0V\le W$ and the number of supported $a_0\le W$ is subpower by the Rankin count of [R112 §2](r112-operator-finite-complement-defect.md#2-exact-clipping-and-the-finite-exterior-average), it follows that

$$
\sum_{\substack{1\le n\le W\\
          \mathcal E^{\rm joint}_{s,W}(n_s(n))\le A_{\rm joint}}}
       T_n(s_n)\ll_{\Theta,C_W,\epsilon} Q^\epsilon A_{\rm joint}W.
 \tag{11}
$$

Restriction to the desired nonzero large differences only reduces this upper sum. As in R112, at most $V_Q$ ordered pairs $(a,c)$ occur per signed difference; both signs and the $|u-v|$ multiplicities cost only fixed log powers. Thus (10) yields the genuine selected fraction at each $q,b,\nu$

$$
O_{\Theta,C,C_W,\epsilon}\!\left(
       Q^\epsilon A_{\rm joint}W\frac{D H(r_b)H(m)}{r_bm d h_q}\right).
 \tag{12}
$$

This positive union bound allows all earlier exclusions and overlapping tuple witnesses.

Apply the actual [R112 §3](r112-operator-finite-complement-defect.md#3-preserve-the-signs-and-restore-the-original-detunings) packet transfer with (12) as the uniform support fraction. The projected squared pointwise and integrated increment estimates under the same auxiliary GRH scale by (12). Both vectors use the same true character projection, and the fixed-product bilinear norm is $O_\epsilon(Q^\epsilon\sqrt{d/(q,d)})$ by [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms). This preserves the two difference orientations' cosine and skew common-interval estimates, their transpose sign, and the two pointwise factors for the sum orientation. Reflected sharp pieces keep their original fixed commuting projections and derivative estimates, not a substituted marginal. Numerator Parseval adds the original $b$ factor. The common-test per-alias bound is consequently

$$
O_\epsilon\!\left(
 Q^\epsilon A_{\rm joint}W b\sqrt{\frac{d}{(q,d)}}
         \frac{D H(r_b)H(m)}{r_bm d h_q}\,\mathcal K\right),
 \tag{13}
$$

with the actual common seminorms of [R112 (13)](r112-operator-finite-complement-defect.md#3-preserve-the-signs-and-restore-the-original-detunings), including the reflected terms when used.

For fixed $b,d$, the real $r_b,h_q$ grouping, $h_q\ge U=\max(A_h,\operatorname{rad}d)$ on precisely the shared primes, and $(q,d)\ge\operatorname{rad}d$ give the same harmonic upper sum $O_\epsilon(Q^\epsilon D H(m)/(m\sqrt{d\operatorname{rad}d}\,U))$ before $A_{\rm joint}W b\mathcal K$ by [R108 (10)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration). Then Cauchy over the true unitary divisor groups and the radical/harmonic sums of [R108 (12)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration) give the bound $O_\epsilon(Q^\epsilon B^2D^2/(D_0 A_h^2))$ before $A_{\rm joint}W$. The original [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) Taylor recovery keeps all exterior phases and the $2^{-n}$ coefficient bound at order $n$. Its original costs at integer offset $\ell$ are $O(1+|\ell|)$ and $O(S^{-1}+(1+|\ell|)^2/Q)$. The square sum over $|\ell|\le R+1$ with $J\asymp Q$ gives the bracket of (4). At (5) the prefactor has exponent $99/100$; the three resulting exponents are $-1/160,-3/800,-19/4000$, respectively. All earlier benchmark, edge and parity restorations remain unchanged for the sharp comparison.

## 4. A live coefficient for which two overlaps cannot occur together

Use two fixed odd shared primes $p_1=31,p_2=211$, with $d=p_1p_2\,2^e\asymp Q^{1/5}$ the least of that form at least $D_0$. Take $p_i^{\ell_i}\asymp Q^{37/400}$, and the distinct odd primes $r\asymp Q^{411/1000},\ m\in(B/(2d),B/d)$ as in [R112 §4](r112-operator-finite-complement-defect.md#4-a-live-coefficient-with-a-strictly-smaller-finite-defect). Put

$$
b=dm,\quad k=p_1^{\ell_1}p_2^{\ell_2}r,\quad q=2k,\qquad
  h_q=2p_1^{\ell_1}p_2^{\ell_2},\quad
     s=2^{e+1}p_1^{\ell_1+1}p_2^{\ell_2+1}.
 \tag{14}
$$

Then $k\asymp Q^{596/1000}$ lies in the inherited long-alias range, $h_q\ge Q^{9/50}$, $(q,b)=2p_1p_2<G=Q^{1/5}$ for large $Q$, and $b$ is in the true high denominator band. Use a generator and its conjugate at $r$ and the generator $\eta$ and $\eta'=\eta^{2V^*}$ at $m$, where $V^*$ bounds the finitely many fixed log-power ranges for those factors. Thus the earlier tested nontrivial and signed mixed powers on $r,m$ keep their prime conductors, with $r>Q^{51/125}$, $rm\asymp Q^{601/1000}>Q^{3/5}$, and the high full-product $m$-part as in the predecessor. At both $p_i^{\ell_i+1}$ take a primitive tame-trivial conjugate pair with principal product.

Choose $j_2$ largest with $W_*=1+5p_1p_2\,2^{j_2}\le W$, and set $a_*=p_1p_2\,2^{j_2}$, $t_0=\lfloor(8/100)\log_2 Q\rfloor$. Then $5\le V_*=\lfloor W/a_*\rfloor\le10$, $W_*>W/2$, and $W_*-1\asymp Q^{1/100}$. The bounds follow from $1+5a_*\le W<1+10a_*$ and integrality. At $2^{e+1}$ keep the sign-trivial primitive $\gamma_2$ of $5$-order $2^{e-1}$ and put

$$
\gamma'_2=\gamma_2^{-W_*+2^{e-1-t_0}}.
 \tag{15}
$$

It is primitive because the exponent is odd. The true product on this component has exponent $-5a_*+2^{e-1-t_0}$ of valuation $j_2$, so conductor $2^{e+1-j_2}=Q^{19/100+o(1)}$ dividing $2^e$. This and the principal products at the odd shared primes meet the actual lift from $d$.

The earlier product and equal branches are excluded as in [R112 §4](r112-operator-finite-complement-defect.md#4-a-live-coefficient-with-a-strictly-smaller-finite-defect): fixed polylogarithmic powers of the shared product have $2$-conductor $Q^{19/100-o(1)}$, equal shared joint conductors are at least $Q^{791/1000-o(1)}$, and the alias and coprime factors are unchanged. For the older unequal subpower or polylog ranges, $a-W_*c$ cannot vanish and has size at most $Q^{1/100+o(1)}$, giving $2$-conductor at least $Q^{19/100-o(1)}$. The total odd conductor loses at most $\log|a-c|=o(\log Q)$ in its logarithm by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation), because the two valuations are below their respective $\ell_i$. Their combined conductor is $Q^{37/200-o(1)}$. Thus all those earlier unequal joint products are at least $Q^{976/1000-o(1)}>Q^{22/25}$, and the earlier small individual shared cut also fails.

For any old tested polynomial pair $a,c\le W$, if $a\ne W_*c$ then $0<|a-W_*c|\le Q^{2/100+o(1)}$. Its corresponding valuation at $2$ is unchanged by the extra $c2^{e-1-t_0}$ in the mixed exponent, and the $2$-conductor is at least $Q^{18/100-o(1)}$. Each odd valuation of nonzero $a-c$ is below its local $\ell_i$, with total weighted by $\log p_i$ at most $\log W$. Thus the combined odd conductor is at least $Q^{175/1000-o(1)}$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation), and the full joint floor $Q^{956/1000-o(1)}$ exceeds $Q^{87/100}$. At an exact match $a=W_*c$, one has $c=1$ because $W_*>W/2$; its difference is $t=5a_*$, not a prime power. The intrinsic factors at $31,211$ are each $2$; neither odd shared prime divides the other prime's predecessor. The exterior moduli are $15,105$, and each of $3,5$ is retained by the clipping since $V_*\ge5$. The prime $7$, if retained, occurs in only one exterior modulus. The pointwise tame product is $100$, while both the full and the clipped exterior defect contribute $15$ times the intrinsic $4$, giving $60$. This excludes every earlier polynomial gate R109–R112, even at the same $20$ finite cap for R112.

The genuine primitive numerator incidence is nonzero in the unmodified parity input. At each odd $p_i$ in the exact [R93 (4)](r93-operator-unequal-mixed-denominator-powers.md#2-a-shared-prime-restriction-of-the-exact-gauss-factor) formula, $v_{p_i}(b)=1$, $v_{p_i}(q)=\ell_i$; the primitive local character on $1+p_i^{\ell_i}x,\ x\bmod p_i$, has a transform supported at one nonzero frequency with magnitude $p_i$. The outer unit variable traverses those frequencies, and the principal product gives the nonzero local magnitude $p_i^{\ell_i+1}$. At $2$, congruence modulo $2$ is automatic on units and both primitive Gauss sums are nonzero at unit frequencies. The actual conjugate pairing at $r$ and primitive additive Gauss sums at $m$ supply the other nonzero factors.

Finally choose $(j,u,v,a,c)=(1,2,1,W_*,1)$. Its difference $t=5a_*$ has supported part $a_*$ and complement $5$. In (2) the repeated exterior primes $3,5$ cannot both divide any eligible $g\le V_*\le10$, so $J_L(V_*)=5$, attained by $g=5$; the singly occurring $7$ cannot increase the quotient. Thus $\mathcal E^{\rm joint}_{s,W}(a_*)=4\cdot5=20<60$. Its $2$-conductor is exactly $2^{t_0+2}$ by (15), and the odd $p_i$-conductors are $p_i^{\ell_i}$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation) with $v_{p_i}(t)=1$. The actual product conductor is

$$
rm\,p_1^{\ell_1}p_2^{\ell_2}2^{t_0+2}
                   =Q^{866/1000+o(1)}<Q^{87/100}.
$$

This certifies strict new eligibility of a nonzero original coefficient at the same $20$ cap. It is not a lower bound for its integrated decrement or its sharply parity-projected field.
