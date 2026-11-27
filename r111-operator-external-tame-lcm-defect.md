# Averaging the external tame torsion of shared exponent differences

The tame factors at shared primes can have large values on particular exponent differences. Their part coprime to the shared modulus can nevertheless be averaged over the exterior part of the difference. It costs only a product-to-lcm defect and the intrinsic shared-prime contribution. This yields an incremental deletion in the actual packet and a new live coefficient whose pointwise tame factor grows without bound.

## 1. The actual further deletion

Start from the genuine $Z_{\rm tame}$ of [R110 §1](r110-operator-bounded-tame-composite-differences.md#1-the-exact-additional-selection), with the prescribed earlier R108 subpower range and all earlier deletions still in force. Use the same complete even shell, true transported parent profiles $h,f$, common taper, $J^{-1}$ normalization and high-denominator packet $\mathcal C_+(B,R)$. Keep the original $z,w_{\rm raw}>A,\ k>K\ge A/Q,\ (2k,b)<G$, the actual orientations and signs and the original unequal numerator detunings. Assume the same local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Both original parity versions apply, including the sharp variant of R86/R87 with $K\ge2P$. All inherited polynomial parameter ranges remain unchanged.

For each actual $q=2k,b$ use the factorization

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
 q=r_bh_q,\quad s=dh_q,\quad q'=qb=r_bms .
 \tag{1}
$$

The full shared alias part $h_q$ has exactly the prime support of $d$, and $r_b,m,s$ are pairwise coprime. The two genuine progression-character components on these moduli are denoted by $(\alpha,\eta,\gamma)$, $(\alpha',\eta',\gamma')$.

For a nonzero signed difference $t$, write $|t|=a_0b_0$, where $a_0=n_s(t)=\prod_{p\mid s}p^{v_p(|t|)}$ has its full prime-power part on $s$ and $(b_0,s)=1$. For each odd $p\mid a_0$ define

$$
I_p=\prod_{\ell\mid s,\ \ell\ {\rm prime}}\ell^{v_\ell(p-1)},
 \quad L_p=(p-1)/I_p,\qquad
 L=\operatorname{lcm}_{\substack{p\mid a_0\\p>2}} L_p .
 \tag{2}
$$

Thus $(L_p,s)=1$. The following defect depends on $s,a_0$ alone, not on the coprime complement $b_0$:

$$
\mathcal E_s(a_0)=
       \left(\prod_{\substack{p\mid a_0\\p>2}}\gcd(a_0,I_p)\right)
                   \frac{\prod_{\substack{p\mid a_0\\p>2}}L_p}{L}.
 \tag{3}
$$

Empty products and the empty lcm are one. The quotient in (3) occurs only because the exterior tame moduli can share prime powers.

Fix $C,C_W>0$, $D,D_0,A_h,A_{\rm def}\ge1$, and an integer $1\le W\le Q^{C_W}$. Let $V_Q=\lfloor(\log Q)^C\rfloor$, $L_0=\lfloor\log Q\rfloor$. Only at $d\ge D_0,\ h_q\ge A_h$, delete from the actual $Z_{\rm tame}$ its remaining pairs satisfying

$$
\begin{gathered}
 \operatorname{cond}(\alpha^j)
 \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)
 \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D,\\
 1\le j,u,v\le V_Q,\quad u\ne v,\qquad
 1\le a,c\le W,\quad \min(a,c)\le V_Q,\qquad
 t=a-c,\quad |t|>L_0,\quad \mathcal E_s(n_s(t))\le A_{\rm def}
 \end{gathered}
 \tag{4}
$$

for at least one tuple of integers. Conductors are primitive inducing conductors, with one for the principal character. There is no new pointwise bound on the tame product $\mathcal T_s(t)$ from [R110 (2)](r110-operator-bounded-tame-composite-differences.md#1-the-exact-additional-selection). The current estimate is incremental and does not assert that the new gate contains the old one on all $s,t$. Apply (4) before the original unequal detunings.

Let $Z_{\rm def}$ be the resulting field and $R_*=1+R$. Then

$$
\|Z_{\rm tame}-Z_{\rm def}\|_{\rm pkt}
  \ll_{\Gamma,\Theta,C,C_W,\epsilon} Q^\epsilon A_{\rm def} W
          \frac{BD}{\sqrt{D_0}A_h}
       \left[\frac{R_*^{3/2}+R_*^{5/2}}{Q}
                               +\frac{R_*^{1/2}}{S}\right].
 \tag{5}
$$

The bound allows arbitrary denominator prime powers, restrictions of the deletion fixed by $k,b$, a fixed orthogonal spatial compression, or restriction to a subset of the packet. As always, the predicate in (4) uses the original signed character pairing, not an arbitrary joint mask.

For a concrete example, keep the full numerical choices of R110, with its actual tame ceiling $A_{\rm tame}=2$ and the earlier R108/R109 thresholds unchanged. Use $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, and choose the new parameters

$$
D_0=Q^{1/5},\quad A_h=Q^{9/50},\quad
 W=\lfloor Q^{1/100}\rfloor,\quad D=Q^{87/100},\quad A_{\rm def}=2.
 \tag{6}
$$

The deletion costs $O_{\epsilon,C}(Q^{-3/800+\epsilon})$, with the inherited sharp $\widehat T,\widehat P$ comparison $O_{\epsilon,C}(Q^{-1/500+\epsilon})$ in the post-parity input, now to $Z_{\rm def}$. Section 4 gives a genuinely newly eligible coefficient at (6) with $\mathcal T_s(t)\to\infty$. The bound is not on the surviving covariance, an individual even modulus, other packets, or weak S.

## 2. Average the exterior gcd before summing the aliases

Fix the actual $q,b$ and full product $\nu=\nu_d\rho\bmod b$. The genuine partner of $(\alpha,\eta,\gamma)$ is

$$
\alpha'=\bar\alpha,\qquad
 \eta'=\rho\bar\eta,\qquad
 \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{7}
$$

with $\pi_s$ the unit reduction to $d$. The new condition preserves this involution: interchange $u,v$ and $a,c$ simultaneously, use conjugation invariance of the alias power conductor, and note that $n_s(t)$ and the short-leg test depend only on the unordered pair of shared exponents. All earlier masks also preserve the involution. Thus this is the same character projection on both actual legs at fixed $\nu$, commuting with the inherited fixed parity projections.

Keep the exact top-primitivity reduction of [R108 §2](r108-operator-top-conductor-subpower-shared-cut.md#2-count-only-the-true-live-shared-fibers): on each shared prime the unit translation annihilates every incidence at a primitive numerator in every original orientation if either shared leg is below full conductor there. For a fixed tuple $t=a-c\ne0$, write $s=s_t s_{\rm o}$, where $s_t$ is the full part of $s$ on the primes of $t$. By [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation), the translated shared output $\gamma^t(\nu_d\circ\pi_s)^c$ has full conductor $s_{\rm o}$ there, since $t$ is prime to every such local prime and the product lift is below the top. On the remaining part keep the genuine local fibers, without assuming any primitivity of that output. Write $T_l(n)$ for the size of the $l$-th power kernel in the character group of $n$, with $T_l(1)=1$, and $H(n)=\sum_{1\le l\le V_Q}T_l(n)$. The normalized fixed-tuple fraction at this exact product is bounded by the [R108 (6)](r108-operator-top-conductor-subpower-shared-cut.md#2-count-only-the-true-live-shared-fibers) count

$$
O_{\Theta,\epsilon}\!\left(
    Q^\epsilon\frac{D\,T_j(r_b)T_{|u-v|}(m)T_{|t|}(s_t)}
                           {r_b m s}\right).
 \tag{8}
$$

In detail, $\phi(s_{\rm o})$ bounds the unrestricted input on that component and cancels its factor in $\phi(q')$. The other three outputs must have total conductor at most $D/s_{\rm o}$, giving at most $(D/s_{\rm o})\tau(r_b m s_t)$ choices and the displayed kernel sizes per fiber; the set is empty if $D<s_{\rm o}$.

At an odd $p^E\parallel s_t$ the local kernel size is $\gcd(|t|,p-1)p^{\min(v_p(|t|),E-1)}$. The prime $2$, if present, contributes at most $2$ times its wild factor $2^{v_2(|t|)}$. All wild factors together are bounded by $a_0$. By the exact support split $|t|=a_0b_0$ and (2), the tame factor at an odd $p\mid a_0$ is
$\gcd(a_0,I_p)\gcd(b_0,L_p)$. Therefore

$$
\begin{split}
 T_{|t|}(s_t)
  &\le 2a_0\prod_{\substack{p\mid a_0\\p>2}}
                       \gcd(a_0,I_p)\,\gcd(b_0,L_p)\\
  &\le 2a_0\,\mathcal E_s(a_0)\,\gcd(b_0,L).
 \end{split}
 \tag{9}
$$

For the second inequality, compare valuations at each prime $\ell$ of $L$. One index with maximal $v_\ell(L_p)$ supplies the $\ell$-part of $\gcd(b_0,L)$, while all other $\ell$-parts are bounded by their contribution to $\prod L_p/L$. The maximizing index may depend on $\ell$, which is harmless since this is a primewise upper bound. No disjointness of the $L_p$ is assumed.

At fixed $a_0$, the divisor identity for the gcd gives

$$
\sum_{1\le b_0\le W/a_0}\gcd(b_0,L)
       =\sum_{l\mid L}\phi(l)\left\lfloor\frac{W}{a_0 l}\right\rfloor
       \le \frac{W}{a_0}\tau(L).
 \tag{10}
$$

We have dropped $(b_0,s)=1$ here only in a positive upper sum. In particular the possible large actual value of $\gcd(b_0,L)$ for some eligible differences is not bounded pointwise. Uniformly in the true support,
$L\le\prod L_p\le\operatorname{rad}(a_0)\le W$, so $\tau(L)\ll_{C_W,\epsilon}Q^\epsilon$. The number of $a_0\le W$ supported on the primes of the polynomially bounded $s$ is $O_{\Theta,C_W,\epsilon}(Q^\epsilon)$ by the supported Rankin bound of [R110 §2](r110-operator-bounded-tame-composite-differences.md#2-separate-the-tame-factors-from-an-arithmetic-support-average). Summing (9) by (10) consequently gives

$$
\sum_{\substack{1\le n\le W\\ \mathcal E_s(n_s(n))\le A_{\rm def}}}
                    T_n(s_n)
        \ll_{\Theta,C_W,\epsilon} Q^\epsilon A_{\rm def} W .
 \tag{11}
$$

The defect gate allows the upper bound in (11) at fixed $a_0$, before summing $b_0$. This step would not justify dropping the internal factor or the product-to-lcm quotient without other input.

At a signed difference $t$ there are at most $V_Q$ possible ordered pairs $(a,c)$ by the short-leg gate. Sum both signs and all $j,u,v$ in (8), as in [R109 §2](r109-operator-polynomial-prime-power-differences.md#2-sum-the-actual-exceptional-local-fibers-over-the-differences). The coprime-denominator signed difference multiplicities cost only a fixed log power beyond $H(m)$. The actual selected fraction at each $q,b,\nu$ is at most

$$
O_{\Theta,C,C_W,\epsilon}\!\left(
       Q^\epsilon A_{\rm def} W
             \frac{D H(r_b)H(m)}{r_bm d h_q}\right).
 \tag{12}
$$

This is an upper count for the union, so previously deleted masks and multiple witnesses cause no overcounting problem for the inequality.

## 3. Restore the original full-product estimates and detunings

Apply the unchanged [R110 §3](r110-operator-bounded-tame-composite-differences.md#3-transfer-with-the-actual-aliases-orientations-and-detunings) transfer with (12) in place of [R110 (10)](r110-operator-bounded-tame-composite-differences.md#2-separate-the-tame-factors-from-an-arithmetic-support-average). The projected squared pointwise and integrated increment estimates on the genuine progression vectors under the auxiliary GRH use the same fraction by normalized residue Parseval. At fixed product the two factors are in the same projected vector of (7) and the genuine bilinear norm is $O_\epsilon(Q^\epsilon\sqrt{d/(q,d)})$ by [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms). The original difference orientations use the cosine marginal and skew common-interval translation with the original transpose sign. The sum orientation uses its two pointwise bounds; the optional sharp reflected pieces use their fixed original derivative bounds, not a substituted marginal formula. Full numerator Parseval gives the same factor $b$, and multiplying the two square-root vector bounds uses (12) once. Hence the per-alias common-test bound is

$$
O_\epsilon\!\left(
 Q^\epsilon A_{\rm def} W b\sqrt{\frac d{(q,d)}}
       \frac{D H(r_b)H(m)}{r_bm d h_q}\,\mathcal K\right)
 \tag{13}
$$

with precisely the common seminorms, including reflected terms, of [R110 (11)](r110-operator-bounded-tame-composite-differences.md#3-transfer-with-the-actual-aliases-orientations-and-detunings).

At fixed $b,d$, group genuine aliases by $r_b,h_q$. Their supported harmonic sum with $h_q\ge U=\max(A_h,\operatorname{rad}d)$, $(q,d)\ge\operatorname{rad}d$, $r_bh_q\le8M$, and the $H(r_b)/r_b$ harmonic bound gives
$O_\epsilon(Q^\epsilon D H(m)/(m\sqrt{d\operatorname{rad}d}\,U))$
before the common $A_{\rm def}W b\mathcal K$, exactly as [R108 (10)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration). Cauchy over the true unitary divisor groups, the radical harmonic sum, and the same $H(m)$ bound give the unchanged denominator square sum $O_\epsilon(Q^\epsilon B^2D^2/(D_0A_h^2))$ of [R108 (12)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration) before the common $A_{\rm def}W$. Finally apply the exact [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) Taylor recovery with every original exterior phase and the $2^{-n}$ coefficient bound at Taylor order $n$. The costs at integer offset $\ell$ are $O(1+|\ell|)$ and $O(S^{-1}+(1+|\ell|)^2/Q)$ as in [R110 §3](r110-operator-bounded-tame-composite-differences.md#3-transfer-with-the-actual-aliases-orientations-and-detunings). The square sum over $|\ell|\le R+1$ and the original $J\asymp Q$ give (5). At (6) the prefactor before the bracket has exponent $99/100$, giving $-1/160,-3/800,-19/4000$ for the three terms. The prior sharp comparison and all benchmark, parity and edge restorations have not changed.

## 4. A live coefficient with unbounded exterior tame torsion

We use a subpower odd shared prime, rather than a distribution theorem for primes in progressions. Let $n=\lfloor \tfrac12\log_3\log Q\rfloor$, so $3^n\to\infty$ and $3^n\ll\sqrt{\log Q}$. For large $Q$, the integer

$$
M_n=1+5^{3^{n-1}}+5^{2\cdot3^{n-1}}
$$

is $3\bmod4$ and $1\bmod3$. Some prime $p\mid M_n$ is $3\bmod4$, since $M_n$ is odd and its prime divisors $3\bmod4$ cannot all occur to even powers. Every prime $p\mid M_n$ is coprime to $5$ and $3$. The order of $5$ modulo $p$ divides $3^n$ because $M_n(5^{3^{n-1}}-1)=5^{3^n}-1$, but cannot divide $3^{n-1}$: in that case $M_n\equiv3\bmod p$. Thus our $p$ has $3^n\mid p-1$, $v_2(p-1)=1$, and $p\le M_n=\exp(O(\sqrt{\log Q}))=Q^{o(1)}$.

Choose $d=p\,2^e\asymp Q^{1/5}$ minimally at least $D_0$, and $\ell=\lfloor(37/200)\log Q/\log p\rfloor$, so $p^\ell=Q^{37/200+o(1)}$. Choose distinct odd primes $r\asymp Q^{411/1000},\ m\in(B/(2d),B/d)$ as in [R109 §4](r109-operator-polynomial-prime-power-differences.md#4-an-actual-new-coefficient-at-polynomial-exponent-size); both exceed $p$ for large $Q$. Set

$$
b=dm,\quad k=p^\ell r,\quad q=2k,\quad
              h_q=2p^\ell,\quad s=2^{e+1}p^{\ell+1}.
 \tag{14}
$$

These choices give the actual high denominator band, $k=Q^{596/1000+o(1)}$ in the inherited long-alias range, $h_q\ge Q^{9/50}$ and $(q,b)=2p<Q^{1/5}=G$ at the inherited numerical gate of [R82 §1](r82-operator-low-product-character-long-quotient.md#1-exact-setup-and-assertions). As in R109, use a generator and its conjugate at $r$, and a generator $\eta$ and $\eta'=\eta^{2V^*}$ at $m$, where $V^*$ bounds all the finitely many fixed log-power ranges on those two factors. The previously tested nontrivial powers and mixed powers keep conductors $r,m$; in particular $r>Q^{51/125}$, $rm=Q^{601/1000+o(1)}>Q^{3/5}$, and the true full product retains its high $m$-part. At $p^{\ell+1}$ take a primitive conjugate pair trivial on the tame factor, with principal product.

Let $j_2$ be the largest integer with $W_*=1+p\,3^n2^{j_2}\le W$, and $t_0=\lfloor(8/100)\log_2Q\rfloor$. For large $Q$, $j_2=(1/100+o(1))\log_2 Q$, $W_*$ is odd and $W_*-1\asymp W$. At $2^{e+1}$ use sign-trivial primitive $\gamma_2$ of $5$-order $2^{e-1}$, and put

$$
\gamma'_2=\gamma_2^{-W_*+2^{e-1-t_0}} .
 \tag{15}
$$

Its exponent is odd, so it is primitive. The true product on this component has exponent $-p\,3^n2^{j_2}+2^{e-1-t_0}$ of valuation $j_2$, since $e-1-t_0>j_2$. Thus its conductor is $2^{e+1-j_2}=Q^{19/100+o(1)}$, dividing $2^e$; the product at $p$ is principal, so it is a genuine pair with the required product lift from $d$. The old shared-product powers retain $Q^{19/100-o(1)}$ conductor at $2$, and the old equal-shared joint conductors are at least $Q^{791/1000-o(1)}$. This avoids the previous [R98](r98-operator-shared-product-power-cut.md), [R101](r101-operator-three-factor-equal-exponents.md) and [R102](r102-operator-shared-equal-gauss-conductor.md) cuts on those branches; other old product/alias choices are excluded as in the [R109 witness](r109-operator-polynomial-prime-power-differences.md#4-an-actual-new-coefficient-at-polynomial-exponent-size) by the unchanged coprime legs.

For every R108 old subpower or earlier polylogarithmic unequal pair, $a-W_*c\ne0$ with $|a-W_*c|\le Q^{1/100+o(1)}$; hence the conductor of $\gamma_2^a(\gamma'_2)^c$ is at least $Q^{19/100-o(1)}$, because the term $c2^{e-1-t_0}$ cannot affect that valuation. At $p$, the old difference has $v_p(a-c)\log p=o(\log Q)$, so its conductor is $Q^{37/200-o(1)}$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation). Thus all such older joint tests have conductor at least $Q^{976/1000-o(1)}>Q^{22/25}$, and the earlier small direct shared cut is also excluded.

For the actual R109 and R110 polynomial selections, if $a=W_*c$, the difference $p\,3^n2^{j_2}c$ cannot be a prime power and its tame factor at $p$ is at least $2\cdot3^n>2$. Thus neither earlier predicate then holds. Otherwise $0<|a-W_*c|\le Q^{2/100+o(1)}$ since both exponents are at most $W$, so the $2$-conductor is at least $Q^{18/100-o(1)}$. The nonzero difference has $|a-c|\le W$, giving $v_p(a-c)\log p\le (1/100)\log Q$, strictly below the wild threshold at $p$. The $p$-conductor is therefore at least $Q^{175/1000-o(1)}$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation). The joint product is at least $Q^{956/1000-o(1)}>Q^{87/100}$ for every tested old tuple in this case. This verifies retention for the actual preceding field, not just failure of an earlier test at one tuple.

The actual primitive numerator coefficient is nonzero in the unmodified input. At $p$ in [R93 (4)](r93-operator-unequal-mixed-denominator-powers.md#2-a-shared-prime-restriction-of-the-exact-gauss-factor), $v_p(b)=1$ and $v_p(q)=\ell$. The primitive character on $1+p^\ell x,\ x\bmod p$, is a nontrivial additive character, so the local transform is $p$ at its unique nonzero Fourier frequency and vanishes at all others. The unit numerator coefficient permutes the nonzero frequencies as the outer unit varies; the product factor there is principal. Thus the local absolute value is $p^{\ell+1}$. This is the same exact reasoning as in [R105 §4](r105-operator-large-shared-alias-joint-cut.md#4-a-live-witness-on-a-large-shared-alias-with-radical-six), valid also for the present growing prime. At $2$ congruence modulo $2$ is automatic on units and both Gauss sums are primitive at unit frequencies. At $r$ the genuine conjugate pairing is nonzero, and at $m$ the primitive additive Gauss factors are nonzero.

Now choose $(j,u,v,a,c)=(1,2,1,W_*,1)$. Its difference is $t=p\,3^n2^{j_2}$, with shared part $a_0=p\,2^{j_2}$ and exterior part $b_0=3^n$. In (2) the sole odd shared prime is $p$, so $I_p=2$, $L_p=(p-1)/2=L$; hence $\mathcal E_s(a_0)=2$. But the true tame factor is $\mathcal T_s(t)=\gcd(t,p-1)=2\cdot3^n\to\infty$. Its $2$-conductor is exactly $2^{t_0+2}$ by (15), and its $p$-conductor is $p^\ell$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation), since $v_p(t)=1$. Thus

$$
rm\,p^\ell\,2^{t_0+2}
                        =Q^{866/1000+o(1)}<Q^{87/100}.
$$

This is strict new eligibility of a nonzero original incidence, not a lower bound after integration or sharp parity projection and not an estimate of the surviving covariance.
