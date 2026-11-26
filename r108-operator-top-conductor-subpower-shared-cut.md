# Forced top conductors allow subpower shared exponent ranges

A shared output character is already forced to have full local conductor at every prime not dividing its nonzero exponent difference. Counting those coordinates before taking a power-fiber bound gives the full large-shared-alias saving without restricting the shared exponent range to a fixed power of the logarithm. The bound below deletes a further sector of the actual preceding field. It does not bound the covariance still retained.

## 1. The exact incremental deletion

Start with the genuine retained field $Z_{\rm poly}$ of [R107 §1](r107-operator-interpolated-shared-difference-cut.md#1-the-actual-further-deletion), at its specified earlier cutoff. Keep the complete even shell, true transported parent profiles $h,f$, common taper, original $J^{-1}$ normalization and high-denominator packet $\mathcal C_+(B,R)$. Keep all prior masks and signs, including $z,w_{\rm raw}>A,\ k>K\ge A/Q,\ (2k,b)<G$, and the original distinct numerator detunings. Assume the same local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Both original parity inputs are allowed, including the post-R86/R87 sharp parity input with $K\ge2P$. Keep the same polynomial parameter ranges.

At each real $q=2k,b$, write the true shared factorization

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
 q=r_b h_q,\qquad s=dh_q,\qquad q'=qb=r_bms.
 \tag{1}
$$

The three factors $r_b,m,s$ are pairwise coprime, and $d,h_q$ have the same prime support. Denote the two progression-character factors on $r_b,m,s$ by $(\alpha,\eta,\gamma)$ and $(\alpha',\eta',\gamma')$, respectively.

Fix $C>0$, $D,D_0,A_h\ge1$, define $V_Q=\lfloor(\log Q)^C\rfloor$ and $L_0=\lfloor\log Q\rfloor$, and let $W\ge1$ be an integer. Delete from $Z_{\rm poly}$, only at $d\ge D_0,\ h_q\ge A_h$, its surviving pairs satisfying

$$
\begin{gathered}
 \operatorname{cond}(\alpha^j)
 \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)
 \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D,\\
 1\le j,u,v\le V_Q,\quad u\ne v,\qquad
 1\le a,c\le W,\quad |a-c|>L_0
 \end{gathered}
 \tag{2}
$$

for at least one tuple of integers. Conductors are primitive inducing conductors, including one for a principal character. The alias and coprime-denominator exponents remain in the fixed polylogarithmic range; only the two shared exponents are enlarged. Apply the deletion to character pairs before detuning. The lower difference gate expressly leaves the logarithmic R106 sector unchanged; the R107 sector also remains deleted.

Write $Z_{\rm top}$ for the resulting field and $R_*=1+R$. In the same packet norm as R107, the bound uniform in $W$ is

$$
\|Z_{\rm poly}-Z_{\rm top}\|_{\rm pkt}
   \ll_{\Gamma,\Theta,C,\epsilon} Q^\epsilon W^4
      \frac{BD}{\sqrt{D_0}A_h}
       \left[\frac{R_*^{3/2}+R_*^{5/2}}{Q}
                        +\frac{R_*^{1/2}}{S}\right].
 \tag{3}
$$

The same bound holds for arbitrary denominator prime powers, further restrictions fixed by $k,b$, and inherited fixed orthogonal compression or restriction to a subset of the packet. An empty range in (2) is immediate. For any specified $W=Q^{o(1)}$, the factor $W^4$ is absorbed in $Q^\epsilon$, by taking a smaller intermediate exponent. In particular $W=\lfloor \exp((\log Q)^\theta)\rfloor$ for fixed $0<\theta<1$ is allowed.

At the R107 scales $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, put $D_0=Q^{1/5},\,A_h=Q^{9/50}$. For every such subpower $W$, (3) now allows $D=Q^{22/25}$, with error $O_\epsilon(Q^{-3/800+\epsilon})$ on the new sector. The inherited sharp $\widehat T,\widehat P$ comparison in the post-parity version remains $O_\epsilon(Q^{-1/500+\epsilon})$, now to $Z_{\rm top}$. These are packet bounds on this deletion and the previously established restorations only, not a bound on the surviving covariance, on an individual target modulus, on other packets, or on weak S.

## 2. Count only the true live shared fibers

At each $q,b$ and fixed actual full product $\nu=\nu_d\rho\bmod b$, the exact pairing on the three factors in (1) is

$$
\alpha'=\bar\alpha,\qquad \eta'=\rho\bar\eta,\qquad
 \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{4}
$$

where $\pi_s$ is unit reduction from $s$ to $d$, as in [R107 §2](r107-operator-interpolated-shared-difference-cut.md#2-the-same-fixed-product-estimate-on-the-actual-legs). We can first restrict both shared legs to full local primitivity, exactly and without error. Indeed, at every $p\mid s$ we have $p\mid d$ and $v_p(q')=v_p(d)+v_p(h_q)\ge2$. If a first-leg character misses top $p$-power conductor, translate its unit variable in the original orientation by $q'/p$. This preserves the unit domain, the congruence modulo $q$, and the character factor, while the reduced numerator phase is multiplied by $e(-A_0\sigma_1/p)\ne1$, with $A_0$ coprime to $b$ and $\sigma_1=\pm1$. The entire coefficient is zero, and the same argument applies to the second leg with $\sigma_2$. This is the literal [R103 §2](r103-operator-independent-shared-relation-obstruction.md#2-proof-using-the-literal-unit-fibers) unit-fiber vanishing; it holds at each primitive numerator before detuning and for each original orientation. By (4) top local primitivity is equivalent on the two legs, since the lifted product factors through $d$ whose local exponent is strictly smaller than the corresponding top one.

All earlier retained masks preserve the partner involution. In (2), alias power conductor is unchanged by conjugation, and on simultaneously interchanging $u,v$ and $a,c$ the same mixed conductors occur on the exchanged legs. The difference gates are unchanged. Thus top primitivity and (2) give the same character projection on both genuine legs at fixed $\nu$. These character projections commute with the optional reflected parity projections. In particular the construction is not an application of a bilinear estimate with an arbitrary joint mask.

For a fixed tuple from (2), let $t=a-c\ne0$, and split the actual $s$ into its full parts

$$
s_t=\prod_{\substack{p\mid s\\ p\mid t}}p^{v_p(s)},\qquad
        s_{\rm o}=s/s_t .
 \tag{5}
$$

At every $p\mid s_{\rm o}$, the true mixed shared output $P=\gamma^t(\nu_d\circ\pi_s)^c$ has full conductor $p^{v_p(s)}$. This follows from [R104 §1](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation) with $v_p(t)=0$, including the exceptional case at $2$ where the adjusted shared alias exponent is at least one. Equivalently the power is invertible on the local top kernel of order $p$ and the lifted product is trivial on that kernel. Hence this conductor contributes a factor exactly $s_{\rm o}$ to every admissible output, independently of the input on that part.

Let $T_l(n)$ count the kernel of raising a character modulo $n$ to its $l$-th power, for $l\ge1$, with $T_l(1)=1$. The number of possible shared inputs on $s_{\rm o}$ is at most $\phi(s_{\rm o})$. On the coprime product $r_b m s_t$ the remaining three output characters must have total conductor at most $D/s_{\rm o}$; this is impossible if $D<s_{\rm o}$. Otherwise there are at most $(D/s_{\rm o})\tau(r_b m s_t)$ such ordered outputs: CRT combines them into one character, and each conductor divisor of size at most $D/s_{\rm o}$ contributes at most its size. For each such output the fiber is at most $T_j(r_b)T_{|u-v|}(m)T_{|t|}(s_t)$, by (4); primitivity and earlier masks can only reduce it. Importantly no $T_{|t|}(s_{\rm o})$ is needed. Dividing by the real $\phi(q')$, and using the usual subpower divisor and inverse totient factors in the inherited polynomial range, gives at fixed $\nu$ and tuple

$$
\text{support fraction}\ \ll_{\Theta,\epsilon} Q^\epsilon
      \frac{D\,T_j(r_b)T_{|u-v|}(m)T_{|t|}(s_t)}{r_b m s}.
 \tag{6}
$$

Indeed the factor $\phi(s_{\rm o})$ cancels its exact factor in $\phi(q')$, leaving $1/s_{\rm o}$ from the remaining conductor budget.

The surviving torsion bound is elementary:

$$
T_{|t|}(s_t)\le |t|\operatorname{rad}(|t|)
                                           \le |t|^2 .
 \tag{7}
$$

For an odd $p^A\parallel s_t$, the unit group is cyclic and the local factor equals $\gcd(|t|,p-1)p^{\min(v_p(t),A-1)}\le p^{1+v_p(t)}$. For $p=2$, splitting its unit group into the sign and cyclic parts gives at most $2^{1+v_2(t)}$, also at the small exponents. Multiplying over $p\mid s_t$ proves (7), since every such prime divides $t$. The bound is uniform even when the prime powers in $s_t$ are arbitrarily large. This step uses the literal support split in (5); the corresponding bound for the unsplit $s$ is not asserted.

Define $H(n)=\sum_{1\le l\le V_Q}T_l(n)$. Summing (6) over $j$, the $u,v$ pairs with each difference (multiplicity at most $2V_Q$), and the at most $W^2$ shared pairs, yields

$$
\text{support fraction}\ \ll_{\Theta,C,\epsilon} Q^\epsilon W^4
              \frac{D\,H(r_b)H(m)}{r_b m d h_q}.
 \tag{8}
$$

All factors depending on the old fixed polylogarithmic range other than $H$ fit into the $Q^\epsilon$ budget. This is a uniform bound at each real $q,b,\nu$, not an averaged suppression of the actual $\nu$ field.

## 3. Arithmetic on the actual aliases and restoration

By normalized residue Parseval and the same auxiliary GRH, the individual progression pointwise and integrated increment estimates in [R106 §2](r106-operator-logarithmic-shared-difference-cut.md#2-the-true-shared-power-map-needs-only-its-difference) and [R107 §2](r107-operator-interpolated-shared-difference-cut.md#2-the-same-fixed-product-estimate-on-the-actual-legs) scale by (8) in squared norm. Use the unchanged fixed-product bilinear norm $O_\epsilon(Q^\epsilon\sqrt{d/(q,d)})$ of [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms), valid also at the required raw Fourier arguments. Because both legs have the same true $F_\nu$ projection, the R106/R107 common-test transfer applies: the original difference orientations use the cosine marginal and the skew common-interval raw translation, with the same transpose sign $\nu(-1)$, the sum orientation uses both pointwise factors, and the optional reflected sharp parity pieces use their original commuting per-leg projections and derivative bounds. This does not assert a marginal identity for the reflected masks. Full numerator Parseval uses the uniformity in $\nu$ and produces the same factor $b$. Thus the per-alias common-test bound is

$$
O_\epsilon\!\left(
 Q^\epsilon W^4 b\sqrt{\frac{d}{(q,d)}}
              \frac{D H(r_b)H(m)}{r_bm d h_q}\,\mathcal K\right),
 \tag{9}
$$

where $\mathcal K=K_1+QK'_2$, with the inherited extra $Q(E_\infty+E_1)$ when needed using $P/k\le1/2$. These are the same common-test seminorms as in [R107 (6)](r107-operator-interpolated-shared-difference-cut.md#2-the-same-fixed-product-estimate-on-the-actual-legs); the $W^4$ is once, not squared in (9), because the selected fraction is used once in each of two squared vector estimates, followed by the product of their square roots. No numerator-dependent character selection has been made.

At a fixed $b,d=b_\parallel$ let $L_{b,d}$ sum the arithmetic factors in (9) without $Q^\epsilon W^4 b$ or the seminorms. This is zero for $d<D_0$. For $U=\max(A_h,\operatorname{rad}(d))$, the actual aliases have $h_q\ge U$, with all primes of $h_q$ dividing $d$; also $(q,d)\ge\operatorname{rad}(d)$ and $r_bh_q\le8M$. The pair $(r_b,h_q)$ determines $k$. Relaxing only positive upper sums gives

$$
L_{b,d}\ll_{\Theta,C,\epsilon}Q^\epsilon
           \frac{D H(m)}
                       {m\sqrt{d\operatorname{rad}(d)}\,U}.
 \tag{10}
$$

Indeed the $r_b$ sum of $H(r_b)/r_b$ is subpower by [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers). The $h_q$ harmonic tail is $O_{\Theta,\epsilon}(Q^\epsilon/U)$, by the supported tail bound [R105 (9)](r105-operator-large-shared-alias-joint-cut.md#3-sum-the-large-shared-alias-parts-and-restore-the-packet). Explicitly it is bounded by $U^{-1+\delta}\prod_{p\mid d}(1-p^{-\delta})^{-1}$ for fixed $0<\delta<1$; for polynomial $d,U$ the product is subpower after adjusting the $\epsilon$ budgets, uniformly, and $\delta$ can be made arbitrarily small. No independence between $r_b$ and $h_q$ is used in the original selection.

Now $U\ge A_h$ suffices: there is no longer a shared torsion factor in (10). The elementary radical sum

$$
\sum_{d\le B}\frac{1}{\operatorname{rad}(d)}
                          \ll_{\Theta,\epsilon}Q^\epsilon
 \tag{11}
$$

follows by inserting $d^{-\delta}$ at cost $B^\delta$. The positive Euler product then has local factors $1+1/[p(p^\delta-1)]$, whose infinite product converges for fixed $\delta>0$. Take $\delta$ small relative to the intended $\epsilon$ and polynomial bound on $B$. By Cauchy across the true unitary divisor groups of $b$, the lower gate $d\ge D_0$, and the square of the nonnegative R90 harmonic sum for $H(m)/m$, it follows that

$$
\begin{split}
  \sum_{b\le B} b^2
    \left(\sum_{\substack{d\mid b\\(d,b/d)=1}}L_{b,d}\right)^2
   &\ll_{\Theta,C,\epsilon} Q^\epsilon
       \frac{B^2D^2}{D_0A_h^2}
       \sum_{d\le B}\frac{1}{\operatorname{rad}(d)}
       \sum_{m\le B}\frac{H(m)^2}{m^2}\\
   &\ll_{\Theta,C,\epsilon}Q^\epsilon\frac{B^2D^2}{D_0A_h^2}.
 \end{split}
 \tag{12}
$$

All enlarged denominator ranges here are positive upper sums only.

Apply the original [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) Taylor recovery from the common test, keeping the actual exterior phase and exact Taylor output coefficient, of absolute value at most $2^{-n}$ at order $n$. At integer offset $\ell$, the weighted seminorm costs are $O(1+|\ell|)$ and $O(S^{-1}+(1+|\ell|)^2/Q)$, exactly as in [R107 §4](r107-operator-interpolated-shared-difference-cut.md#4-how-the-radical-weight-changes-the-actual-alias-saving). With $J\asymp Q$, the square sum over $|\ell|\le R+1$ and the square root of (12) give the bracket of (3) with the single factor $W^4$ of (9). At the displayed scales $BD/(\sqrt{D_0}A_h)$ has exponent $99/100$, so the three resulting exponents are $-1/160,-3/800,-19/4000$ after absorption of the subpower factor. All earlier sharp restoration and benchmark terms are unchanged. The asserted sharp comparison follows by the triangle inequality.

## 4. A live coefficient with strictly larger shared exponents

Take $W=\lfloor\exp(\sqrt{\log Q})\rfloor$, with the R107 comparison at $C_s=2$, so its old longer-difference ceiling is $Q^{167/200}$. Use the same actual large alias of [R105 §4](r105-operator-large-shared-alias-joint-cut.md#4-a-live-witness-on-a-large-shared-alias-with-radical-six) and [R107 §5](r107-operator-interpolated-shared-difference-cut.md):

$$
d=3\cdot2^e\asymp Q^{1/5},\quad
 3^\ell\asymp Q^{37/200},\quad
 r\asymp Q^{411/1000},\qquad m\in(B/(2d),B/d).
$$

Choose $d$ minimally at least $D_0$, and choose distinct odd primes $r,m>3$ as there. Put

$$
k=3^\ell r,\quad q=2k,\quad b=dm,\quad
 h_q=2\cdot3^\ell,\quad s=2^{e+1}3^{\ell+1}.
$$

Thus $k\asymp Q^{596/1000}$ lies in the inherited alias range, $(q,b)=6<G$, $h_q\ge Q^{9/50}$, and $b$ is genuinely in the high denominator band. Use a generator and its conjugate on $r$, and $\eta,\eta'=\eta^{2V^*}$ on $m$ for a generator $\eta$, where $V^*$ bounds all finitely many relevant fixed polylogarithmic ranges on $r,m$, including the new $V_Q$. As in R105/R107, all old allowed alias powers and all old individual, product and signed coprime-denominator powers retain their respective prime conductor. Their generator exponents are nonzero and strictly smaller than the respective orders in absolute value. In particular $r>Q^{51/125}$, $rm\asymp Q^{601/1000}$ exceeds the earlier $Q^{3/5}$ ceiling, and the true full product retains the $m$-part. On $3^{\ell+1}$ keep the same primitive conjugate pair, trivial on the tame factor, whose product is principal.

Choose an odd integer $W_*\asymp \tfrac12\exp(\sqrt{\log Q})$ with $W_*\le W$. Let $\gamma_2$ be sign-trivial and primitive of $5$-order $2^{e-1}$ at $2^{e+1}$ and set

$$
\gamma'_2=\gamma_2^{-W_*+2^{e-1-t_0}},\qquad
                         t_0=\left\lfloor\tfrac{8}{100}\log_2 Q\right\rfloor .
 \tag{13}
$$

It is primitive because its exponent is odd. Their product has exponent $1-W_*+2^{e-1-t_0}$ of valuation $v_2(1-W_*)$, which is at least one and $o(\log Q)$, since $1<W_*=Q^{o(1)}$ and $e-1-t_0$ has positive order $\log Q$. Hence this true product induces from $2^e$ with conductor $Q^{1/5-o(1)}$, as do all its previously tested small powers. Together with the principal $3$-product this verifies the actual product condition. The earlier equal-shared branches have joint conductor $Q^{801/1000-o(1)}$, outside both [R101](r101-operator-three-factor-equal-exponents.md) and [R102](r102-operator-shared-equal-gauss-conductor.md); the high shared product also avoids [R98](r98-operator-shared-product-power-cut.md).

For every old tested positive unequal shared pair $(a,c)$, with both exponents bounded by any of the earlier fixed log powers, $a-W_*c\ne0$ and $|a-W_*c|=Q^{o(1)}$. At $2$ the exponent of its mixed output is $a-W_*c+c2^{e-1-t_0}$; the valuation is that of the first summand, $o(\log Q)$, so its conductor there is $Q^{1/5-o(1)}$. At $3$ all such pairs have conductor $3^{\ell+1-v_3(a-c)}=Q^{37/200-o(1)}$ by [R104 §1](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation). This verifies jointly the survival of the earlier small shared cuts and the paired unequal cuts of R105–R107: their actual jointly tested conductors have size $Q^{986/1000-o(1)}$, exceeding even the earlier largest $Q^{22/25}$. It also excludes the smaller three-factor ceilings in [R100](r100-operator-three-factor-joint-powers.md) and the unequal branches in [R101](r101-operator-three-factor-equal-exponents.md). The other earlier masks are as in the inherited witness, since the shared product and all its previously tested powers still have conductor $Q^{1/5-o(1)}$, the unchanged alias and coprime legs keep all their prime conductors, and the genuine arithmetic gates are the same.

The true primitive-numerator coefficient is nonzero in the unmodified parity input. On $2$ the congruence modulo $2$ is automatic on units and both primitive Gauss factors are nonzero at the actual unit frequencies. On $3$, the unchanged primitive character restricted to $1+3^\ell x,\ x\bmod3$ has exactly one nonzero Fourier frequency. The outer unit in the literal local formula traverses both nonzero frequencies, and the principal product yields the same single surviving term as in [R105 §4](r105-operator-large-shared-alias-joint-cut.md#4-a-live-witness-on-a-large-shared-alias-with-radical-six); its local absolute value is $3^{\ell+1}$. On $r$ the congruence gives the nonzero conjugate pairing, and on $m$ both coprime primitive Gauss factors are nonzero.

The new tuple $(j,u,v,a,c)=(1,2,1,W_*,1)$ is allowed for large $Q$. Its difference exceeds every fixed power of $\log Q$; the $2$-component of the mixed character has conductor exactly $2^{t_0+2}$, since the exponent in (13) now cancels $W_*$. At $3$ the shared conductor is $3^{\ell+1-v_3(W_*-1)}$ by [R104 §1](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation), since $v_3(W_*-1)=o(\log Q)$. Thus its true product conductor is

$$
rm\,3^{\ell+1-v_3(W_*-1)}\,2^{t_0+2}
                     =Q^{866/1000+o(1)}<Q^{22/25}.
$$

The witness is an actual nonzero original incidence eligible strictly after the earlier deletions. It is not a lower bound for the integrated decrement or for either parity-reduced packet field.
