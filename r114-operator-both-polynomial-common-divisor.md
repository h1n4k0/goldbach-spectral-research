# A common divisor allows both shared exponents to be polynomial

The previous joint-overlap deletion uses a short shared exponent to count the allowable pairs at a fixed difference. A large common divisor gives a different count without requiring either exponent to be short. The resulting conditional deletion applies to a new part of the genuine field. The witness below has both shared exponents of polynomial size and survives every preceding short-leg cut.

## 1. The genuine further deletion

Start from the actual $Z_{\rm joint}$ of [R113 §1](r113-operator-joint-attainable-tame-overlap.md#1-exact-further-deletion), retaining all earlier deletions, including its short-leg cut and the prescribed R108 subpower range. Keep the complete even shell, original transported parent profiles $h,f$, common taper, $J^{-1}$ normalization and separated high-denominator packet $\mathcal C_+(B,R)$. Preserve $z,w_{\rm raw}>A,\ k>K\ge A/Q,\ (2k,b)<G$, the true signs and orientations, and the original distinct numerator detunings. Assume the same original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Both original parity inputs are allowed, including the sharp R86/R87 version with $K\ge2P$. The inherited polynomial parameter ranges are unchanged.

At each actual $q=2k$ and denominator $b$, write

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
        q=r_bh_q,\quad s=dh_q,\quad q'=qb=r_bms .
 \tag{1}
$$

The factors $r_b,m,s$ are pairwise coprime, and $h_q$ and $d$ have the same prime support. Denote the two genuine progression-character factors on these moduli by $(\alpha,\eta,\gamma)$, $(\alpha',\eta',\gamma')$.

Fix $C,C_W>0$, $D,D_0,A_h,A_{\rm joint}\ge1$, an integer $1\le W\le Q^{C_W}$, and a real number $1\le X\le W$. Set $V_Q=\lfloor(\log Q)^C\rfloor$ and $L_0=\lfloor\log Q\rfloor$. For nonzero $t$ with $|t|\le W$ write $a_0=n_s(t)=\prod_{p\mid s}p^{v_p(|t|)}$, and use the exact jointly attainable defect $\mathcal E^{\rm joint}_{s,W}(a_0)$ of [R113 (2)](r113-operator-joint-attainable-tame-overlap.md#1-exact-further-deletion). Thus the exterior complement bound is $V=\lfloor W/a_0\rfloor$ and the maximum is over divisors of the finite clipped lcm at most $V$. This defect depends on $s,W,a_0$, not on which one of the two shared exponents is smaller.

Only at $d\ge D_0,\ h_q\ge A_h$, delete from $Z_{\rm joint}$ the remaining pairs satisfying

$$
\begin{gathered}
 \operatorname{cond}(\alpha^j)\,
 \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)\,
 \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D,\\
 1\le j,u,v\le V_Q,\quad u\ne v,\qquad
 1\le a,c\le W,\quad \gcd(a,c)\ge X,\\
 t=a-c,\quad |t|>L_0,\qquad
       \mathcal E^{\rm joint}_{s,W}(n_s(t))\le A_{\rm joint}
 \end{gathered}
 \tag{2}
$$

for some integer tuple. All conductors are primitive inducing conductors, with one for the principal character. There is no imposed short-leg condition in (2). This replaces that condition only for the new deletion; the old selected masks remain part of the input. Apply (2) to the true original pairing before the actual unequal detunings.

Let $Z_{\gcd}$ be the resulting field and $R_*=1+R$. Then the same packet norm satisfies

$$
\|Z_{\rm joint}-Z_{\gcd}\|_{\rm pkt}
  \ll_{\Gamma,\Theta,C,C_W,\epsilon}
 Q^\epsilon A_{\rm joint}\frac{W^2}{X}\frac{BD}{\sqrt{D_0}A_h}
     \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

The estimate permits arbitrary prime powers in $b$, any further deletion restriction fixed by $k,b$, fixed orthogonal spatial compression and restriction to a subset of the packet. It does not apply to an arbitrary joint character mask.

For a concrete choice keep all earlier thresholds and the scales $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, and take

$$
\begin{gathered}
 D_0=Q^{1/5},\quad A_h=Q^{9/50},\quad W=\lfloor Q^{1/100}\rfloor,\qquad
 X=W/10,\quad A_{\rm joint}=1,\quad D=Q^{871/1000}.
 \end{gathered}
 \tag{4}
$$

For sufficiently large $Q$ these satisfy $X\ge1$. The incremental packet bound is $O_{\epsilon,C}(Q^{-11/4000+\epsilon})$, and the inherited sharp $\widehat T,\widehat P$ comparison in the post-parity version remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\gcd}$. The witness in Section 4 has $a,c\asymp Q^{1/100}$ and meets the new bound even though all earlier eligible short or subpower tuples fail. Nothing here bounds the surviving covariance, an individual even modulus, another packet or weak S.

## 2. Count the exponent choices at fixed signed difference

At fixed actual $q,b$ and full product $\nu=\nu_d\rho\bmod b$, the genuine partner is

$$
\alpha'=\bar\alpha,\qquad \eta'=\rho\bar\eta,\qquad
                \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{5}
$$

where $\pi_s$ is unit reduction to $d$. The predicate (2) preserves this involution. Indeed, interchange $u,v$ and $a,c$ together, use conjugation invariance of the alias power conductor, and note that $\gcd(a,c)$ and the supported part of $|t|$ are unchanged. All earlier masks also preserve the partner. Thus the same true character projection acts on the two vectors at fixed $\nu$, commuting with the original fixed reflected parity projections.

Use the exact top-primitivity reduction of [R108 §2](r108-operator-top-conductor-subpower-shared-cut.md#2-count-only-the-true-live-shared-fibers) for the original primitive numerator incidences. For $s_t=\prod_{p\mid(t,s)}p^{v_p(s)}$, the shared output $\gamma^t(\nu_d\circ\pi_s)^c$ has forced full conductor on $s/s_t$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation). Write $T_l(n)$ for the $l$-th power kernel size on the character group of $n$, with $T_l(1)=1$, and $H(n)=\sum_{1\le l\le V_Q}T_l(n)$. As in [R113 (10)](r113-operator-joint-attainable-tame-overlap.md#3-true-support-count-and-packet-transfer), the fraction at a fixed exponent tuple and the true full product is bounded by

$$
O_{\Theta,\epsilon}\!\left(
 Q^\epsilon \frac{D\,T_j(r_b)T_{|u-v|}(m)T_{|t|}(s_t)}{r_bms}\right).
 \tag{6}
$$

The factor $s/s_t$ is already used from the conductor budget, its free input count is canceled against the corresponding totient, and the remaining translated outputs are counted only on the three pairwise coprime factors $r_b,m,s_t$.

The genuine finite overlap estimate of [R113 (11)](r113-operator-joint-attainable-tame-overlap.md#3-true-support-count-and-packet-transfer) yields

$$
\sum_{\substack{1\le n\le W\\
             \mathcal E^{\rm joint}_{s,W}(n_s(n))\le A_{\rm joint}}}
       T_n(s_n)\ll_{\Theta,C_W,\epsilon}Q^\epsilon A_{\rm joint}W .
 \tag{7}
$$

This remains an upper bound with the added nonzero-difference range from (2). Explicitly, at fixed $a_0=n_s(n)$ the full product of wild kernel factors is at most $a_0$, with at most one extra sign factor $2$. At the true unit complements $b_0\le V$, the intrinsic and finite exterior tame factors have total sum at most $V\tau(L)\mathcal E^{\rm joint}_{s,W}(a_0)$, by [R113 (7)–(8)](r113-operator-joint-attainable-tame-overlap.md#2-the-finite-exterior-average-and-its-arithmetic-size). Use $a_0V\le W$ and sum over the subpower number of supported $a_0$'s. There is no short-leg assumption needed in this arithmetic difference sum.

Now fix a signed $t\ne0$. There is at most one $a$ for every $c$, since $a=c+t$. Moreover $\gcd(a,c)=\gcd(c,|t|)$. If the required gcd is at least $X$, there is a divisor $g_0\mid |t|$, $g_0\ge X$, that divides $c$. Consequently, allowing an overcount,

$$
\#\{(a,c):a-c=t,\ 1\le a,c\le W,\ \gcd(a,c)\ge X\}
   \le\sum_{\substack{g_0\mid |t|\\g_0\ge X}}
                       \left\lfloor\frac{W}{g_0}\right\rfloor
   \le \tau(|t|)\frac{W}{X}
   \ll_{C_W,\epsilon}Q^\epsilon\frac{W}{X}.
 \tag{8}
$$

The count also holds for $t<0$, and does not require either positive exponent to be small. Since $|t|\le W\le Q^{C_W}$, the divisor bound is uniform. For $u,v$ at a specified nonzero $|u-v|$ there are at most $2V_Q$ choices, as before. Summing (6) using (7), (8), the two signs of $t$, and the fixed polylogarithmic $j,u,v$ ranges gives normalized support fraction

$$
O_{\Theta,C,C_W,\epsilon}\!\left(
 Q^\epsilon A_{\rm joint}\frac{W^2}{X}
                 \frac{D H(r_b)H(m)}{r_bm d h_q}\right).
 \tag{9}
$$

This is a positive count for the true union. Overlapping witnesses and all prior exclusions preserve the upper bound.

## 3. The packet estimate with the original signs and detunings

Apply the exact signed transfer of [R113 §3](r113-operator-joint-attainable-tame-overlap.md#3-true-support-count-and-packet-transfer) with the uniform fraction (9). At fixed true $q,b,\nu$, normalized residue Parseval scales the squared pointwise and integrated increment estimates of the actual progression vectors under the same auxiliary GRH by that fraction. The actual fixed-product bilinear norm is $O_\epsilon(Q^\epsilon\sqrt{d/(q,d)})$ by [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms); both vector factors have the same genuine projection by (5). This retains the cosine marginal and skew common-interval translation, with their original transpose sign in the difference orientations, and the two pointwise factors for the sum orientation. The sharp reflected pieces keep their original commuting projections and derivative estimates, not a substituted marginal. Full numerator Parseval contributes the unchanged $b$ factor. The common-test estimate per real alias is therefore

$$
O_\epsilon\!\left(
 Q^\epsilon A_{\rm joint}\frac{W^2}{X}\,
 b\sqrt{\frac{d}{(q,d)}}\,
 \frac{D H(r_b)H(m)}{r_bm d h_q}\,\mathcal K\right)
 \tag{10}
$$

with the exact common seminorms of [R113 (13)](r113-operator-joint-attainable-tame-overlap.md#3-true-support-count-and-packet-transfer), including the reflected terms when used.

At fixed $b,d$, group the actual aliases by $r_b,h_q$. The supported $h_q$ tail above $U=\max(A_h,\operatorname{rad}d)$, $(q,d)\ge\operatorname{rad}d$, and the harmonic $H(r_b)/r_b$ bound give $O_\epsilon(Q^\epsilon DH(m)/(m\sqrt{d\operatorname{rad}d}\,U))$ before the common $A_{\rm joint}(W^2/X)b\mathcal K$, by [R108 (10)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration). The square sum across denominators is then $O_\epsilon(Q^\epsilon B^2D^2/(D_0A_h^2))$ before the common multiplier by [R108 (12)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration), using Cauchy over the true unitary divisor groups, the radical sum and the harmonic $H(m)$ estimate. Only positive upper sums are relaxed.

Finally the [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) Taylor recovery preserves every original exterior phase and $2^{-n}$ coefficient bound at order $n$. The weighted costs at integer offset $\ell$ are $O(1+|\ell|)$ and $O(S^{-1}+(1+|\ell|)^2/Q)$, as in [R113 §3](r113-operator-joint-attainable-tame-overlap.md#3-true-support-count-and-packet-transfer). Sum the square over $|\ell|\le R+1$ with $J\asymp Q$ to obtain the bracket in (3). At (4), $W^2/X=10W$ and the prefactor $WBD/(\sqrt{D_0}A_h)$ has exponent $991/1000$; the three terms give the exponents $-21/4000,-11/4000,-15/4000$, respectively. Earlier benchmark, edge and parity restorations are unchanged, so the claimed sharp comparison follows by the triangle inequality.

## 4. A nonzero original incidence with both exponents polynomial

Use the actual large alias of [R109 §4](r109-operator-polynomial-prime-power-differences.md#4-an-actual-new-coefficient-at-polynomial-exponent-size). Let $d=3\cdot2^e\asymp Q^{1/5}$, minimally at least $D_0$, take $3^\ell\asymp Q^{37/200}$, and choose distinct odd primes $r\asymp Q^{411/1000}$, $m\in(B/(2d),B/d)$ larger than $3$. Set

$$
b=dm,\quad k=3^\ell r,\quad q=2k,\qquad
               h_q=2\cdot3^\ell,\quad s=2^{e+1}3^{\ell+1}.
 \tag{11}
$$

Then $k\asymp Q^{596/1000}$ is in the original long-alias range, $h_q\ge A_h$, $(q,b)=6<G=Q^{1/5}$, and $b$ is in the genuine high denominator band. Use a generator and its conjugate at $r$, and a generator $\eta$ and $\eta'=\eta^{2V^*}$ at $m$, where $V^*$ bounds all finitely many old and new fixed log-power ranges there. All the previously tested nontrivial and signed mixed powers keep their respective conductors $r,m$, as in R109. In particular $r>Q^{51/125}$, $rm\asymp Q^{601/1000}>Q^{3/5}$ and the true product retains the high $m$-part. Take the primitive tame-trivial conjugate pair on $3^{\ell+1}$, with principal product.

At $2^{e+1}$ let $\gamma_2$ be sign-trivial primitive of $5$-order $2^{e-1}$, and take

$$
t_1=\left\lfloor\tfrac{189}{2000}\log_2 Q\right\rfloor,\qquad
                       \gamma'_2=\gamma_2^{-3+2^{e-1-t_1}}.
 \tag{12}
$$

This is primitive because its exponent is odd. Their true product has exponent $-2+2^{e-1-t_1}$ of valuation one, hence conductor $2^e$, inducing from $d$. This and the principal odd shared product fulfill the true full-product condition. The earlier small shared-product cut fails, since the old polylogarithmic powers of that product have conductor $Q^{1/5-o(1)}$. The earlier equal-shared joint tests have total conductor at least $Q^{801/1000-o(1)}$, and the unchanged $r,m$ and actual full product exclude the earlier cuts involving only the corresponding single or product legs.

For any earlier tested unequal shared pair $(a,c)$, if $a=3c$, then $c=Q^{o(1)}$: the older subpower ranges impose this directly, and every earlier polynomial selection from R109 through R113 has $\min(a,c)\le V_Q$, which here is $c\le V_Q$ in its own fixed log-power range. In this case the mixed exponent at $2$ is $c2^{e-1-t_1}$, of conductor $2^{t_1+2-v_2(c)}=Q^{189/2000-o(1)}$. At $3$ the nonzero difference is $2c$, of subpower size, so the conductor is $Q^{37/200-o(1)}$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation). Thus the joint conductor at every such exact-slope tuple is at least

$$
Q^{1761/2000-o(1)}>Q^{22/25}.
$$

This exceeds even the largest old threshold $Q^{22/25}$. If $a\ne3c$, then $0<|a-3c|\ll W+Q^{o(1)}$; hence $v_2(a-3c)\le(1/100+o(1))\log_2Q$. It is unchanged on adding $c2^{e-1-t_1}$, so the $2$-conductor is at least $Q^{19/100-o(1)}$. The $3$-conductor is at least $Q^{175/1000-o(1)}$: the nonzero old difference has logarithm at most $(1/100+o(1))\log Q$, well below $\ell\log 3$, and [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation) applies. The joint conductor is then at least $Q^{966/1000-o(1)}$ and exceeds every earlier cutoff. The older direct small individual shared cut also fails: it only uses fixed polylogarithmic unequal pairs, for which the $3$-conductor alone is $Q^{37/200-o(1)}$. This checks all preceding tested shared relations, not just their evaluation at the new tuple.

The true primitive-numerator incidence is nonzero in the unmodified parity input. At $3$, $v_3(b)=1$, and the exact [R93 (4)](r93-operator-unequal-mixed-denominator-powers.md#2-a-shared-prime-restriction-of-the-exact-gauss-factor) local formula has a unique nonzero transform frequency for the primitive restriction to $1+3^\ell x,\ x\bmod3$. The nonzero frequency is attained by an outer unit, and the principal product gives the local absolute value $3^{\ell+1}$, as in [R109 §4](r109-operator-polynomial-prime-power-differences.md#4-an-actual-new-coefficient-at-polynomial-exponent-size). Congruence at $2$ is automatic on the odd units and both primitive additive Gauss sums are nonzero at unit frequencies. At $r$ the genuine conjugate pairing is nonzero, and at $m$ both primitive additive Gauss sums are nonzero.

Take $g=2^{\lfloor\log_2(W/3)\rfloor}$, so $W/6<g\le W/3$, and choose $(j,u,v,a,c)=(1,2,1,3g,g)$. Both shared exponents have order $Q^{1/100}$, and $\gcd(a,c)=g\ge X$. Its difference $t=2g>L_0$ is a power of $2$, so $a_0=2g$, the odd tame product is empty and $\mathcal E^{\rm joint}_{s,W}(a_0)=1$. At $2$ the mixed exponent in (12) is $g2^{e-1-t_1}$, of conductor $2^{t_1+2-\log_2 g}=Q^{169/2000+o(1)}$. At $3$ the conductor is the full $3^{\ell+1}$, since $3\nmid t$. The total joint conductor equals

$$
rm\,3^{\ell+1}2^{t_1+2-\log_2 g}
                           =Q^{1741/2000+o(1)}<Q^{871/1000}.
$$

This is genuinely new eligibility of a nonzero original incidence with both shared exponents polynomial. It is not a lower bound on its integrated or sharply projected packet decrement, nor a bound on any surviving covariance.
