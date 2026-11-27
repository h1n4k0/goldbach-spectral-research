# Clipping the tame lcm defect at the actual finite complement budget

The exterior part of a shared exponent difference cannot test arbitrarily high prime powers. Clipping the exterior tame moduli by its actual finite range leaves every relevant gcd unchanged, while potentially lowering the product-to-lcm defect. This gives a new actual deletion at the same analytic cost. A strict witness has two different odd shared primes and a smaller finite defect at the same cutoff.

## 1. Exact further deletion

Start from the genuine field $Z_{\rm def}$ of [R111 §1](r111-operator-external-tame-lcm-defect.md#1-the-actual-further-deletion), including all its earlier selections and the prescribed R108 subpower range. Keep the same complete even shell, original transported profiles $h,f$, common taper, $J^{-1}$ normalization and separated high-denominator packet $\mathcal C_+(B,R)$. The original gates $z,w_{\rm raw}>A,\ k>K\ge A/Q,\ (2k,b)<G$, true orientations and signs and original unequal numerator detunings are unchanged. Assume the same local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Both original parity inputs apply, including the sharp R86/R87 variant with $K\ge2P$. Keep all inherited polynomial parameter ranges.

At each actual $q=2k,b$, retain

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
       q=r_bh_q,\quad s=dh_q,\quad q'=qb=r_bms .
 \tag{1}
$$

The moduli $r_b,m,s$ are pairwise coprime, and $h_q$ has exactly the prime support of $d$. Denote the two genuine progression-character components on these three factors by $(\alpha,\eta,\gamma)$ and $(\alpha',\eta',\gamma')$.

Fix $C,C_W>0$, $D,D_0,A_h,A_{\rm fin}\ge1$ and an integer $1\le W\le Q^{C_W}$. Put $V_Q=\lfloor(\log Q)^C\rfloor$, $L_0=\lfloor\log Q\rfloor$. For nonzero $t$ with $|t|\le W$, let $|t|=a_0b_0$ where $a_0=n_s(t)=\prod_{p\mid s}p^{v_p(|t|)}$ and $(b_0,s)=1$. At fixed supported $a_0\le W$, put $V=\lfloor W/a_0\rfloor$; each actual $b_0$ is at most $V$. For each odd $p\mid a_0$ take $I_p,L_p$ of [R111 (2)](r111-operator-external-tame-lcm-defect.md#1-the-actual-further-deletion), the full parts of $p-1$ supported on and coprime to $s$, respectively. Define

$$
\begin{gathered}
 L_{p,[V]}=\prod_{\substack{\ell\mid L_p\\\ell\ {\rm prime}}}
                \ell^{\min(v_\ell(L_p),\lfloor\log_\ell V\rfloor)},\qquad
 L_{[V]}=\operatorname{lcm}_{\substack{p\mid a_0\\p>2}}L_{p,[V]},\\
 \mathcal E^{\rm fin}_{s,W}(a_0)=
      \left(\prod_{\substack{p\mid a_0\\p>2}}\gcd(a_0,I_p)\right)
                    \frac{\prod_{\substack{p\mid a_0\\p>2}}L_{p,[V]}}{L_{[V]}} .
 \end{gathered}
 \tag{2}
$$

Empty products and the empty lcm are one, also when $V=1$ clips all exterior factors to one. This parameter depends on the actual supported $a_0$ and range $W$, not the value of the particular coprime complement $b_0$ inside its range.

Only at $d\ge D_0,\ h_q\ge A_h$, delete from $Z_{\rm def}$ its surviving pairs for which some integer tuple satisfies

$$
\begin{gathered}
 \operatorname{cond}(\alpha^j)
 \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)
 \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D,\\
 1\le j,u,v\le V_Q,\quad u\ne v,\qquad
 1\le a,c\le W,\quad \min(a,c)\le V_Q,\\
 t=a-c,\quad |t|>L_0,\qquad
                     \mathcal E^{\rm fin}_{s,W}(n_s(t))\le A_{\rm fin}.
 \end{gathered}
 \tag{3}
$$

Conductors mean primitive inducing conductors, with one for the principal character. The test takes place before the actual distinct numerator detunings. It retains all preceding deletions.

Let $Z_{\rm fin}$ be the resulting field and $R_*=1+R$. Then the same packet norm satisfies

$$
\|Z_{\rm def}-Z_{\rm fin}\|_{\rm pkt}
 \ll_{\Gamma,\Theta,C,C_W,\epsilon} Q^\epsilon A_{\rm fin}W
       \frac{BD}{\sqrt{D_0} A_h}
   \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{4}
$$

The estimate permits arbitrary prime powers in $b$, any further deletion restriction fixed by $k,b$, fixed orthogonal spatial compression and restriction to a subset of the packet. No estimate for an arbitrary joint character mask is claimed.

For example, keep the numerical scales and old thresholds of [R111 §1](r111-operator-external-tame-lcm-defect.md#1-the-actual-further-deletion), including $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, and take

$$
D_0=Q^{1/5},\quad A_h=Q^{9/50},\quad
       W=\lfloor Q^{1/100}\rfloor,\quad D=Q^{87/100},\quad A_{\rm fin}=12 .
 \tag{5}
$$

Then (4) is $O_{\epsilon,C}(Q^{-3/800+\epsilon})$, and the inherited sharp $\widehat T,\widehat P$ comparison in the post-parity version remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm fin}$. Section 4 gives a newly eligible genuine coefficient even if the old R111 numerical defect bound is increased from $2$ to the same $12$ in (5) with its other settings unchanged. The numerical R111 bound with that fixed change has the same exponents. Nothing here bounds the surviving covariance, an individual even modulus, another packet, or weak S.

## 2. Exact clipping and the finite exterior average

At each actual $q,b$ and full product $\nu=\nu_d\rho\bmod b$, use the original pairing

$$
\alpha'=\bar\alpha,\qquad
      \eta'=\rho\bar\eta,\qquad
      \gamma'=(\nu_d\circ\pi_s)\bar\gamma
 \tag{6}
$$

of [R111 (7)](r111-operator-external-tame-lcm-defect.md#2-average-the-exterior-gcd-before-summing-the-aliases), with $\pi_s$ unit reduction to $d$. The selection (3) preserves this involution by interchanging both mixed exponent pairs, using conjugation invariance on the alias power and observing that $|t|$ and $\min(a,c)$ are unchanged. The fixed $s,W,a_0$ in (2) are therefore unchanged. Together with the inherited masks this is the same genuine character projection on each leg, commuting with the original reflected parity projections.

Retain the exact top conductor vanishing of [R108 §2](r108-operator-top-conductor-subpower-shared-cut.md#2-count-only-the-true-live-shared-fibers) before detuning, so both shared legs are locally primitive in any contributing original incidence. For a fixed tuple let $s_t=\prod_{p\mid(t,s)}p^{v_p(s)}$. Outside $s_t$ the translated output $\gamma^t(\nu_d\circ\pi_s)^c$ has forced full local conductor by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation), since $t$ is prime to that local prime. Write $T_l(n)$ for the $l$-th power kernel size in the character group of $n$, with $T_l(1)=1$, and $H(n)=\sum_{1\le l\le V_Q}T_l(n)$. At the fixed tuple and true product, [R111 (8)](r111-operator-external-tame-lcm-defect.md#2-average-the-exterior-gcd-before-summing-the-aliases) bounds the normalized support fraction by

$$
O_{\Theta,\epsilon}\!\left(
 Q^\epsilon \frac{D\,T_j(r_b)T_{|u-v|}(m)T_{|t|}(s_t)}{r_bms}\right).
 \tag{7}
$$

In this true count, the $\phi(s/s_t)$ bound for the free input there cancels that factor of $\phi(q')$; its conductor has already consumed $s/s_t$ of the conductor budget. The remaining translated output fibers are on the pairwise coprime $r_b,m,s_t$.

For $b_0\le V$, each prime valuation $v_\ell(b_0)\le\lfloor\log_\ell V\rfloor$, so
$\gcd(b_0,L_p)=\gcd(b_0,L_{p,[V]})$ exactly. The finite defect is always at most its full counterpart of [R111 (3)](r111-operator-external-tame-lcm-defect.md#1-the-actual-further-deletion):

$$
\mathcal E^{\rm fin}_{s,W}(a_0)\le\mathcal E_s(a_0).
 \tag{8}
$$

Indeed at each prime $\ell$ contributing to the exterior quotient, select an index with maximal $v_\ell(L_p)$, which remains a maximizer after the same clipping of all indices. In the product-to-lcm quotient only the other indices contribute. Their combined exponent cannot increase under clipping. The intrinsic product in (2) is unchanged.

The same local group calculation as [R111 (9)](r111-operator-external-tame-lcm-defect.md#2-average-the-exterior-gcd-before-summing-the-aliases) bounds the product of wild factors by $a_0$, with one extra sign factor at $2$, giving

$$
\begin{split}
 T_{|t|}(s_t)
 &\le 2 a_0 \prod_{\substack{p\mid a_0\\p>2}}
              \gcd(a_0,I_p)\gcd(b_0,L_p)\\
 &=2 a_0 \prod_{\substack{p\mid a_0\\p>2}}
              \gcd(a_0,I_p)\gcd(b_0,L_{p,[V]})\\
 &\le 2 a_0\,\mathcal E^{\rm fin}_{s,W}(a_0)\,\gcd(b_0,L_{[V]}).
 \end{split}
 \tag{9}
$$

For the last line the maximizer at each prime supplies its part of the gcd with $L_{[V]}$; bound the other factors by their prime powers in the quotient. The upper bound allows overlapping exterior moduli and is made only on the actual truncated complement range.

The basic divisor identity gives

$$
\sum_{1\le b_0\le V}\gcd(b_0,L_{[V]})
   =\sum_{l\mid L_{[V]}}\phi(l)\lfloor V/l\rfloor
   \le V\tau(L_{[V]}).
 \tag{10}
$$

Dropping the original $(b_0,s)=1$ for this upper sum adds only nonnegative terms. Also $L_{[V]}\le\prod L_p\le\operatorname{rad}(a_0)\le W$, so $\tau(L_{[V]})\ll_{C_W,\epsilon}Q^\epsilon$ uniformly. After summing at fixed $a_0$ passing the gate, its $a_0 V$ cost is at most $W$. The number of supported $a_0\le W$ is $O_{\Theta,C_W,\epsilon}(Q^\epsilon)$ by [R110 §2](r110-operator-bounded-tame-composite-differences.md#2-separate-the-tame-factors-from-an-arithmetic-support-average): insert $a_0^{-\xi}$ at cost $W^\xi$, and bound the Euler product logarithm by $O_{\xi,\Theta}((1+\log Q)^{1-\xi})$ for fixed small $0<\xi<1$. Hence

$$
\sum_{\substack{1\le n\le W\\
        \mathcal E^{\rm fin}_{s,W}(n_s(n))\le A_{\rm fin}}}T_n(s_n)
                   \ll_{\Theta,C_W,\epsilon}Q^\epsilon A_{\rm fin}W .
 \tag{11}
$$

This sum clips at the range $V$ of each true supported part before adding those parts; it does not replace the original characters by an unrestricted modulus average.

As in [R111 §2](r111-operator-external-tame-lcm-defect.md#2-average-the-exterior-gcd-before-summing-the-aliases), each signed $t$ permits at most $V_Q$ pairs $(a,c)$, and the $u,v$ multiplicities with each nonzero $|u-v|$ are at most $2V_Q$. Accounting for both signs and all the allowed $j,u,v$, (7) and (11) give the true selected fraction

$$
O_{\Theta,C,C_W,\epsilon}\!\left(
    Q^\epsilon A_{\rm fin}W\frac{D H(r_b)H(m)}{r_bm d h_q}\right).
 \tag{12}
$$

The bound is uniform in the fixed real $q,b,\nu$. The positivity of the upper count permits all prior exclusions and multiple witnesses of (3).

## 3. Preserve the signs and restore the original detunings

Apply [R111 §3](r111-operator-external-tame-lcm-defect.md#3-restore-the-original-full-product-estimates-and-detunings) with (12) in place of [R111 (12)](r111-operator-external-tame-lcm-defect.md#2-average-the-exterior-gcd-before-summing-the-aliases). The normalized pointwise and integrated-increment squared projection estimates on the actual progression vectors under the same auxiliary GRH scale by (12). The two vector factors use the same selected support by (6), and the original fixed-product bilinear norm remains $O_\epsilon(Q^\epsilon\sqrt{d/(q,d)})$ by [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms). This retains the cosine marginal and skew common-interval translation for the original difference orientations, their original transpose sign and the two pointwise bounds for the sum. The sharp reflected pieces keep their original derivative bounds and fixed commuting projections; no marginal identity is substituted on those pieces. Numerator Parseval gives the unchanged $b$ factor. Thus at each actual alias the common-test bound is

$$
O_\epsilon\!\left(
 Q^\epsilon A_{\rm fin} W b\sqrt{\frac{d}{(q,d)}}
      \frac{D H(r_b)H(m)}{r_bm d h_q}\,\mathcal K\right),
 \tag{13}
$$

with exactly the original common seminorms of [R111 (13)](r111-operator-external-tame-lcm-defect.md#3-restore-the-original-full-product-estimates-and-detunings), including the extra reflected terms when used.

Group the actual $k$ at fixed $b,d$ by $r_b,h_q$, with the supported tail $h_q\ge U=\max(A_h,\operatorname{rad}d)$. The harmonic sums in [R108 (10)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration), using $(q,d)\ge\operatorname{rad}d$, give
$O_\epsilon(Q^\epsilon D H(m)/(m\sqrt{d\operatorname{rad}d}\,U))$
for the alias sum before $A_{\rm fin}W b\mathcal K$. Cauchy over the unitary divisor groups, the radical sum and the harmonic bound for $H(m)$ give the same denominator square sum $O_\epsilon(Q^\epsilon B^2D^2/(D_0A_h^2))$ of [R108 (12)](r108-operator-top-conductor-subpower-shared-cut.md#3-arithmetic-on-the-actual-aliases-and-restoration) before $A_{\rm fin}W$. Only positive upper sums are relaxed in that step.

Finally apply the exact [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) Taylor recovery, preserving all exterior phases and the $2^{-n}$ bound on the original Taylor coefficient at order $n$. The common costs at integer offset $\ell$ are $O(1+|\ell|)$ and $O(S^{-1}+(1+|\ell|)^2/Q)$, as in [R111 §3](r111-operator-external-tame-lcm-defect.md#3-restore-the-original-full-product-estimates-and-detunings). The square sum over $|\ell|\le R+1$ with $J\asymp Q$ gives the bracket in (4). At (5) the prefactor has exponent $99/100$, giving the three final exponents $-1/160,-3/800,-19/4000$. All earlier benchmark, edge and parity restorations are unchanged, as required for the sharp comparison.

## 4. A live coefficient with a strictly smaller finite defect

Use fixed odd shared primes $p_1=19,p_2=163$, and let $d=p_1p_2\,2^e\asymp Q^{1/5}$ be minimally at least $D_0$. Choose $p_i^{\ell_i}\asymp Q^{37/400}$ for $i=1,2$, and the distinct odd primes $r\asymp Q^{411/1000},\ m\in(B/(2d),B/d)$ from the predecessor witness construction, both larger than $p_2$ for large $Q$. Put

$$
b=dm,\quad k=p_1^{\ell_1}p_2^{\ell_2}r,\quad q=2k,\quad
  h_q=2p_1^{\ell_1}p_2^{\ell_2},\quad
                 s=2^{e+1}p_1^{\ell_1+1}p_2^{\ell_2+1}.
 \tag{14}
$$

Then $k\asymp Q^{596/1000}$ is in the original long-alias range and $b$ in the actual high band, $h_q\ge Q^{9/50}$, and $(q,b)=2p_1p_2<G=Q^{1/5}$ for large $Q$, using the inherited numerical gate of [R82 §1](r82-operator-low-product-character-long-quotient.md#1-exact-setup-and-assertions). Keep a generator and its conjugate at $r$, and a generator $\eta$ and $\eta'=\eta^{2V^*}$ at $m$, where $V^*$ bounds all the fixed log-power ranges for the $r,m$ factors. All earlier tested nontrivial powers and signed mixed powers on them retain their prime conductors. In particular $r>Q^{51/125}$, $rm\asymp Q^{601/1000}>Q^{3/5}$, and the actual full product retains its $m$-component. At each odd $p_i^{\ell_i+1}$ use a primitive tame-trivial conjugate pair with principal product.

Choose $j_2$ as the largest integer with $W_*=1+3p_1p_2\,2^{j_2}\le W$, and put $a_*=p_1p_2\,2^{j_2}$. Then $W_*$ is odd, $W_*-1=3a_*\asymp Q^{1/100}$, and $V_*=\lfloor W/a_*\rfloor$ satisfies $3\le V_*\le6$. The upper bound follows from $1+6a_*>W$; at equality $6a_*=W$ the value $6$ is allowed. Put $t_0=\lfloor(8/100)\log_2 Q\rfloor$. At $2^{e+1}$ use sign-trivial primitive $\gamma_2$ of $5$-order $2^{e-1}$ and set

$$
\gamma'_2=\gamma_2^{-W_*+2^{e-1-t_0}} .
 \tag{15}
$$

Its odd exponent makes it primitive. Their true product has exponent $-3p_1p_2\,2^{j_2}+2^{e-1-t_0}$ of exact valuation $j_2$; its conductor $2^{e+1-j_2}=Q^{19/100+o(1)}$ divides $2^e$. Together with the principal odd shared products this meets the actual lift requirement. The earlier shared-product powers retain $Q^{19/100-o(1)}$ conductor, so the small shared-product cut fails and equal shared joint conductors are at least $Q^{791/1000-o(1)}$, above the [R101](r101-operator-three-factor-equal-exponents.md) and [R102](r102-operator-shared-equal-gauss-conductor.md) ceilings. The remaining early product and alias conditions on the unchanged $r,m$ components exclude those cuts as in [R111 §4](r111-operator-external-tame-lcm-defect.md#4-a-live-coefficient-with-unbounded-exterior-tame-torsion).

For each earlier positive unequal subpower or polylog tuple at the shared leg, $a-W_*c\ne0$ with $|a-W_*c|\le Q^{1/100+o(1)}$. Thus the $2$-conductor is at least $Q^{19/100-o(1)}$: the added term $c2^{e-1-t_0}$ cannot affect the valuation of that nonzero difference. At the two odd shared primes the total loss in the logarithm of the conductor is at most $\log|a-c|=o(\log Q)$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation); each local valuation is strictly below $\ell_i$. Their combined conductor is $Q^{37/200-o(1)}$, so the joint conductor is at least $Q^{976/1000-o(1)}>Q^{22/25}$. The earlier direct small shared cut also fails.

For any tested positive $a,c\le W$ in R109, R110 or R111, if $a\ne W_*c$, then $0<|a-W_*c|\le Q^{2/100+o(1)}$. The corresponding $2$-conductor is at least $Q^{18/100-o(1)}$. The odd valuations each lie below $\ell_i$, and their sum weighted by $\log p_i$ is at most $\log|a-c|\le\log W$. By [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation) the combined odd conductor is at least $Q^{175/1000-o(1)}$. Hence the full jointly tested conductor is at least $Q^{956/1000-o(1)}>Q^{87/100}$.

It remains to rule out the preceding predicates at an exact match $a=W_*c$. Then the difference $3a_*c$ is not a prime power. Both odd primes are shared, and neither odd prime divides the other's predecessor, so their intrinsic factors are $I_{19}=I_{163}=2$ and the exterior ones are $L_{19}=9,L_{163}=81$. For the difference $3a_*c$ its full exterior quotient in [(3) of R111](r111-operator-external-tame-lcm-defect.md#1-the-actual-further-deletion) is $9$ and the intrinsic product is $4$. Thus the full defect is $36$, and the pointwise tame product is at least $36$ since both $\gcd(|a-c|,18)$ and $\gcd(|a-c|,162)$ are divisible by $6$. The old R109–R111 gates fail, even at the hypothetical same-cap R111 choice $A_{\rm def}=12$. This checks every previously tested tuple, not merely one old relation.

The original incidence is truly nonzero in the unmodified parity input. At either $p_i$, $v_{p_i}(b)=1$ and $v_{p_i}(q)=\ell_i$. In [R93 (4)](r93-operator-unequal-mixed-denominator-powers.md#2-a-shared-prime-restriction-of-the-exact-gauss-factor), the primitive restriction to $1+p_i^{\ell_i}x,\ x\bmod p_i$, is a nontrivial additive character; its transform equals $p_i$ at one nonzero frequency and vanishes otherwise. The outer unit variable at a primitive numerator traverses all the nonzero frequencies, so the single surviving term gives the local absolute value $p_i^{\ell_i+1}$, as in the predecessor construction. At $2$, congruence modulo $2$ is automatic on odd units and both new Gauss factors are primitive at unit frequencies. At $r$ the conjugate unit pairing is nonzero; at $m$ both primitive additive Gauss factors are nonzero.

Finally choose $(j,u,v,a,c)=(1,2,1,W_*,1)$. Its genuine shared difference $t=3a_*$ has supported part $a_*$ and complement $3$. Each of $9,81$ clips to $3$ at $3\le V_*\le6$. Thus the finite defect is $4\cdot3=12$, while the full defect is $36$. Its $2$-conductor is exactly $2^{t_0+2}$ by (15). Each $p_i$-conductor is $p_i^{\ell_i}$ by [R104 (2)](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation), since $v_{p_i}(t)=1$. The full joint conductor equals

$$
rm\,p_1^{\ell_1}p_2^{\ell_2}2^{t_0+2}
                 =Q^{866/1000+o(1)}<Q^{87/100}.
$$

This witnesses strict new eligibility of an actual nonzero original incidence at the same $12$ defect cap. It is not an integrated packet lower bound, a sharply parity-projected lower bound, or a bound on the residual covariance.
