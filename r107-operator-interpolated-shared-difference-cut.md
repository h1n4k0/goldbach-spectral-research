# Interpolating the shared-alias saving for longer exponent differences

The shared square-torsion argument can distinguish any fixed logarithmic power budget for the exponent difference. Interpolating the radical weight with the full shared-alias cutoff then gives a new range between the original large-alias deletion and its logarithmic-difference refinement. The larger-difference range is treated on the actual field left by both earlier deletions.

## 1. The actual further deletion

Use the genuine field $Z_{\log}$ of [R106 §1](r106-operator-logarithmic-shared-difference-cut.md#1-the-exact-incremental-deletion), with the original complete even shell, genuine transported parent profiles $h,f$, common taper, original $J^{-1}$ normalization and high-denominator packet $\mathcal C_+(B,R)$. All earlier signs and selection masks remain, including $z,w>A,\ k>K\ge A/Q,\ (2k,b)<G$. Assume exactly the original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Both original parity inputs are allowed, including the post-R86/R87 input with $K\ge2P$. All polynomial parameter ranges are inherited.

At each real $q=2k,b$, use the genuine factorization

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
 q=r_bh_q,\qquad s=dh_q,\qquad q'=qb=r_bms .
 \tag{1}
$$

The three factors $r_b,m,s$ are pairwise coprime. The full shared alias part $h_q$ contains every power in $q$ on the primes of $b$, not merely the common divisor $(q,b)$. Denote the two progression-character factors on $r_b,m,s$ by $(\alpha,\eta,\gamma)$ and $(\alpha',\eta',\gamma')$, respectively.

Fix $C>0,\ C_s>1$, $D,D_0,A_h\ge1$ and put

$$
V_Q=\lfloor(\log Q)^C\rfloor,\qquad
 V_s=\lfloor(\log Q)^{C_s}\rfloor,\qquad L_0=\lfloor\log Q\rfloor .
$$

Delete from $Z_{\log}$, only at $d\ge D_0$ and $h_q\ge A_h$, its remaining pairs with

$$
\begin{gathered}
 \operatorname{cond}(\alpha^j)\,
 \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)\,
 \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D
 \quad\text{for some integers }1\le j,u,v,a,c\le V_Q,\\
                     u\ne v,\qquad L_0<|a-c|\le V_s .
 \end{gathered}
 \tag{2}
$$

Conductors mean primitive inducing conductors, with one for the principal character. The lower difference gate in (2) makes this a different sector from the logarithmic-difference one in R106. The earlier cuts still apply to the same field; no relation between the new power ranges and those in R96 is assumed. Make the deletion before the original distinct numerator detunings.

Write $Z_{\rm poly}$ for the retained field and $R_*=1+R$, with the packet norm of R106. The estimate is

$$
\|Z_{\log}-Z_{\rm poly}\|_{\rm pkt}
  \ll_{\Gamma,\Theta,C,C_s,\epsilon}
     Q^\epsilon\,\frac{BD}{\sqrt{D_0}\,A_h^{(1+1/C_s)/2}}
       \left[\frac{R_*^{3/2}+R_*^{5/2}}Q
                               +\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

It permits arbitrary denominator prime powers, further restrictions of the deletion fixed by $k,b$, and fixed orthogonal spatial compression or restriction to a subset of the packet. If the exponent range in (2) is empty, the estimate is immediate.

At the R106 scales $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, keep $D_0=Q^{1/5},A_h=Q^{9/50}$ and take $D=Q^{79/100+9/(100C_s)}$. The bound is $O_{\epsilon,C,C_s}(Q^{-3/800+\epsilon})$. In particular at $C_s=2$, take $C\ge2$; this allows the logarithm-squared shared difference, with $D=Q^{167/200}$. The larger old $Q^{22/25}$ cutoff remains on its logarithmic range only. The existing sharp $\widehat T,\widehat P$ comparison in the post-parity version remains $O_{\epsilon,C,C_s}(Q^{-1/500+\epsilon})$, now to $Z_{\rm poly}$. This is a bound on the specified deletion, not the surviving covariance, an individual even modulus, other packets, or weak S.

## 2. The same fixed-product estimate on the actual legs

At fixed $q,b$ and exact full product $\nu=\nu_d\rho\bmod b$, the original incidence forces the unique partner, with

$$
\alpha'=\bar\alpha,\qquad
       \eta'=\rho\bar\eta,\qquad
       \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{4}
$$

where $\pi_s$ is unit reduction to $d$. The new test is invariant under this involution: alias power conductors are unchanged by conjugation, and both mixed exponent pairs can be interchanged simultaneously, preserving the two bounds on the shared difference. All earlier retained supports preserve this involution, including R106. Thus (2) acts by the same selected genuine progression vector $F_\nu$ on both raw legs; each inherited sharp parity piece keeps its original per-leg projections.

For positive $j_0$, write $T_{j_0}(n)=|\ker(\chi\mapsto\chi^{j_0})|$ on the character group of $n$, with value one at $n=1$, and set

$$
H(n)=\sum_{j_0\le V_Q}T_{j_0}(n),\qquad
          H_s(n)=\sum_{j_0\le V_s}T_{j_0}(n).
$$

The actual output at fixed $\nu$ is the translated power map
$(\alpha^j,\eta^{u-v}\rho^v,\gamma^{a-c}(\nu_d\circ\pi_s)^c)$.
Its nonempty fibers at a fixed exponent tuple have size
$T_j(r_b)T_{|u-v|}(m)T_{|a-c|}(s)$. Both differences are nonzero. The product modulus is coprime across the three factors of (1), so the product of the three inducing conductors is the inducing conductor of the output. The number of possible outputs with conductor at most $D$ is at most $D\tau(q')$ by summing over inducing divisors of $q'$ of size at most $D$. Thus, just as in [R106 §2](r106-operator-logarithmic-shared-difference-cut.md#2-the-true-shared-power-map-needs-only-its-difference), dividing by $\phi(q')$ and summing over the polylogarithmic number of allowed tuples bounds the fraction of genuine progression characters used by

$$
O_{\Theta,C,C_s,\epsilon}\!\left(
        Q^\epsilon\,\frac{D H(r_b)H(m)H_s(s)}{r_bms}\right).
 \tag{5}
$$

The tighter difference range is used only on $s$. The lower difference gate, and all previous masks, only reduce this positive count. The bound is uniform in the full product.

For the actual arithmetic vectors under the stated auxiliary GRH, the individual pointwise and integrated increment estimates from [R106 §2](r106-operator-logarithmic-shared-difference-cut.md#2-the-true-shared-power-map-needs-only-its-difference) scale by (5) in squared norm, by normalized residue Parseval. Use the true fixed-product coefficient bound of [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms), with bilinear norm $O_\epsilon(Q^\epsilon\sqrt{\mathfrak e(q,b)})$, where $\mathfrak e(q,b)=d/(q,d)$, including for raw Fourier arguments. The transpose sign $\nu(-1)$ for the difference orientations is unchanged. The cosine marginal and skew common-interval raw translation in R106 therefore apply with the same genuine vector on each side. The sum orientation uses both pointwise factors; the reflected sharp parity pieces use their exact inherited derivative bounds with fixed commuting character projections. No marginal identity on their sharp masks is asserted. Full numerator Parseval, using uniformity in $\nu$, gives per actual alias the common-test bound

$$
O_\epsilon\!\left(Q^\epsilon b\sqrt{\mathfrak e(q,b)}
                 \frac{D H(r_b)H(m)H_s(dh_q)}{r_bms}\,
                 \mathcal K\right),
 \tag{6}
$$

with $\mathcal K=K_1+QK'_2$ and, when needed, the inherited extra $Q(E_\infty+E_1)$ using $P/k\le1/2$. This is at the common test before the different numerator detunings. There is no estimate for arbitrary pair masks.

## 3. The interpolated square-torsion moment

Let $\kappa=2-1/C_s\in(1,2)$. The new arithmetic estimate is

$$
\sum_{d\le B}\frac{H_s(d)^2}{\operatorname{rad}(d)^\kappa}
             \ll_{\Theta,C_s,\epsilon} Q^\epsilon .
 \tag{7}
$$

Indeed $H_s(d)^2\le V_s\sum_{j_0\le V_s}T_{j_0}(d)^2$. At fixed $j_0$ insert $d^{-\delta}$, with fixed $0<\delta<1/C_s$ sufficiently small, at cost $B^\delta$. By positivity and multiplicativity the upper product has local factor

$$
1+p^{-\kappa}\sum_{e\ge1}T_{j_0}(p^e)^2p^{-e\delta}
$$

at every $p\le B$. Away from $p\mid2j_0$, $T_{j_0}(p^e)=\gcd(j_0,p-1)$, so the sum of the local increments is at most

$$
O_\delta\!\left(\sum_{p\le B}
              \frac{\gcd(j_0,p-1)^2}{p^{\kappa+\delta}}\right)
    \ll_{\delta,C_s}\sum_{v\mid j_0} v^{2-\kappa-\delta}
    \ll_{\delta,C_s} j_0^{1/C_s-\delta/2}.
 \tag{8}
$$

For the middle inequality, expand the square of the gcd by the Jordan totient identity of [R106 §3](r106-operator-logarithmic-shared-difference-cut.md#3-a-one-radical-square-torsion-moment), $J_2(v)\le v^2$. The primes $p\equiv1\bmod v$ are bounded above by the integers $nv+1,\ n\ge1$, whose reciprocal $(\kappa+\delta)$-powers sum to $O_{\delta,C_s}(v^{-\kappa-\delta})$ since $\kappa+\delta>1$. For the last inequality use $\tau(j_0)\ll_\delta j_0^{\delta/2}$ and $2-\kappa-\delta>0$.

The bound in (8) is $O((\log Q)^{1-C_s\delta/2})=o(\log Q)$ uniformly for $j_0\le V_s$. At $p\mid2j_0$ the uniform prime-power bound $T_{j_0}(p^e)\le2j_0$ gives total log cost $O_\delta(\log^2(2j_0))=o(\log Q)$. Thus the Euler product is a subpower, uniformly. Take $\delta$ sufficiently small relative to the intended $\epsilon$ and the polynomial bound for $B$ so $B^\delta$ fits the budget, and sum the polylogarithmic number of orders. This proves (7), allowing all powers of the shared divisor. No prime-in-progression estimate is used for (7).

## 4. How the radical weight changes the actual alias saving

At fixed $b,d=b_\parallel$, let $L_{b,d}$ be the sum of the arithmetic factors in (6) over genuine eligible aliases, without $Q^\epsilon b$ and $\mathcal K$; it is zero for $d<D_0$. Put $U=\max(A_h,\operatorname{rad}(d))$. The [R106 §4](r106-operator-logarithmic-shared-difference-cut.md#4-the-actual-weighted-alias-sum-and-detuning) grouping uses $r_bh_q\le8M$, uniqueness of $k$ for the pair $r_b,h_q$, $(q,d)\ge\operatorname{rad}(d)$ and $H_s(dh_q)\le2V_sH_s(d)$ by [R99 (9)](r99-operator-unequal-shared-leg-powers.md#3-sum-the-full-shared-part-of-each-actual-alias) on identical prime support. The $r_b$-weighted sum has the same [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) harmonic estimate with $H$. For the $h_q$ sum the exact support $p\mid h_q\Rightarrow p\mid d$ and the lower bound $U$ give $O_\epsilon(Q^\epsilon/U)$ by [R105 (9)](r105-operator-large-shared-alias-joint-cut.md#3-sum-the-large-shared-alias-parts-and-restore-the-packet). Thus

$$
L_{b,d}\ll_{\Theta,C,C_s,\epsilon} Q^\epsilon\,
              \frac{D H(m)H_s(d)}
                         {m\sqrt{d\operatorname{rad}(d)}\,U}.
 \tag{9}
$$

These sums dominate the actual aliases positively, not by any independence or cancellation assumption.

Since $U$ is at least each of $A_h,\operatorname{rad}(d)$, and $3-\kappa$ and $\kappa-1$ are nonnegative and sum to two, we have

$$
U^2\ge A_h^{3-\kappa}\operatorname{rad}(d)^{\kappa-1}.
$$

Consequently

$$
L_{b,d}^2\ll_{\Theta,C,C_s,\epsilon}Q^\epsilon
       \frac{D^2 H(m)^2H_s(d)^2}{m^2 d\,A_h^{3-\kappa}
                                        \operatorname{rad}(d)^\kappa}.
 \tag{10}
$$

At fixed $b$, Cauchy over the at most $\tau(b)$ unitary divisor groups, $b^2\le B^2$, and the true lower gate on $d$ give, by (7) and the square of the nonnegative R90 $m$ harmonic sum,

$$
\begin{split}
 \sum_{b\le B}b^2
      \left(\sum_{\substack{d\mid b\\(d,b/d)=1}}L_{b,d}\right)^2
   &\ll_{\Theta,C,C_s,\epsilon} Q^\epsilon
           \frac{B^2D^2}{D_0 A_h^{3-\kappa}}
              \sum_{m\le B}\frac{H(m)^2}{m^2}
              \sum_{d\le B}\frac{H_s(d)^2}{\operatorname{rad}(d)^\kappa}\\
   &\ll_{\Theta,C,C_s,\epsilon}Q^\epsilon
                          \frac{B^2D^2}{D_0 A_h^{3-\kappa}} .
 \end{split}
 \tag{11}
$$

The relaxation to all $dm\le B$ is in a positive upper sum only. We may take smaller intermediate epsilons in the finitely many subpower budgets.

Apply the exact common Taylor recovery of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field), keeping each original exterior phase and original output coefficient of absolute value at most $2^{-n}$ at Taylor order $n$. At integer offset $\ell$, the weighted costs are $O(1+|\ell|)$ and $O(S^{-1}+(1+|\ell|)^2/Q)$ for the common seminorms, as in R106. Divide by $J\asymp Q$ and square-sum over $|\ell|\le R+1$ using (11), giving the bracket of (3). The power of $A_h$ in (3) is $(3-\kappa)/2=(1+1/C_s)/2$. At the stated parameters the prefactor has exponent
$39/100+(79/100+9/(100C_s))-1/10-(9/50)(1+1/C_s)/2=99/100$;
the three resulting exponents are $-1/160,-3/800,-19/4000$, respectively. The inherited sharp comparison follows by the triangle inequality with all other restorations and benchmark terms unchanged.

## 5. A new live coefficient with difference of order $(\log Q)^2$

Take $C_s=2$ and $C\ge2$. Use the large shared alias of [R105 §4](r105-operator-large-shared-alias-joint-cut.md#4-a-live-witness-on-a-large-shared-alias-with-radical-six) and [R106 §5](r106-operator-logarithmic-shared-difference-cut.md#5-strict-eligibility-after-the-older-large-alias-cutoff):

$$
d=3\cdot2^e\asymp Q^{1/5},\quad
 3^\ell\asymp Q^{37/200},\quad
 r\asymp Q^{411/1000},\quad m\in(B/(2d),B/d).
$$

As there $d$ is the least such number at least $D_0$, and $r,m>3$ are distinct odd primes available by Bertrand's postulate. Put $k=3^\ell r,\ q=2k,\ b=dm,\ h_q=2\cdot3^\ell,\ s=2^{e+1}3^{\ell+1}$. The high band and all actual gates hold: $k\asymp Q^{596/1000}$, $(q,b)=6$, $h_q\ge Q^{9/50}$, and $\operatorname{rad}(d)=6$. Keep the conjugate generators on $r$, the generator $\eta$ and $\eta'=\eta^{2V^*}$ on $m$, and a primitive conjugate pair trivial on the tame part at $3^{\ell+1}$. Here $V^*$ bounds all finitely many relevant fixed log-power ranges. All previously tested individual alias and coprime mixed powers keep their prime conductors, since their generator exponents are nonzero and smaller than the respective group orders. Thus $r>Q^{51/125}$, $rm\asymp Q^{601/1000}>Q^{3/5}$, and the full product remains high on $m$.

Choose an odd positive integer $W_*\asymp\frac12(\log Q)^2$ with $W_*-1>\log Q$ and $W_*\le\lfloor(\log Q)^2\rfloor$, for example $2\lfloor(\log Q)^2/4\rfloor+1$ for large $Q$. At $2^{e+1}$ use the same sign-trivial primitive $\gamma_2$ of $5$-order $2^{e-1}$, but put

$$
\gamma'_2=\gamma_2^{-W_*+2^{e-1-t}},
               \qquad t=\left\lfloor\tfrac3{100}\log_2Q\right\rfloor .
 \tag{12}
$$

This exponent is odd, so $\gamma'_2$ is primitive. The true shared product on this factor has exponent $1-W_*+2^{e-1-t}$ with valuation $v_2(1-W_*)\ge1$ of order $O(\log\log Q)$. It therefore induces from $2^e$, with conductor $Q^{1/5-o(1)}$; every previously allowed small power also has conductor $Q^{1/5-o(1)}$. The product on the $3$-factor is principal, so the pair satisfies the true product condition.

For earlier positive unequal shared exponents $a,c$, their exponent at $2$ is $a-W_*c+c2^{e-1-t}$. If $a=W_*c$, its conductor is $2^{t+2-v_2(c)}=Q^{3/100-o(1)}$; otherwise its valuation is $v_2(a-W_*c)=O(\log\log Q)$, so its conductor is $Q^{1/5-o(1)}$. The conductor at $3$ is $Q^{37/200-o(1)}$ by [R104 §1](r104-operator-single-unequal-shared-alias.md#1-exact-local-law-for-one-unequal-relation), since the nonzero difference is polylogarithmic. Thus every earlier unequal R105 joint product is at least $Q^{816/1000-o(1)}>Q^{79/100}$. The R99 small shared cut and the R100 joint cut likewise fail. Earlier equal shared powers retain $2$-conductor $Q^{1/5-o(1)}$ by the product computation, so their joint products are $Q^{801/1000-o(1)}$, outside the R101 and R102 thresholds; unequal shared products in R101 also exceed its threshold. The R98 cut is avoided by the high shared product. If the earlier R106 logarithmic difference bound holds, $a=W_*c$ is impossible because $c\ge1$ gives $|a-c|\ge W_*-1>\log Q$. Hence every candidate in that R106 sector has high $2$-conductor and joint product $Q^{986/1000-o(1)}>Q^{22/25}$. This verifies retention at the actual preceding field, not merely failure of R106 for one chosen tuple.

The genuine primitive-numerator incidence is nonzero: congruence modulo $2$ is automatic on the odd units and both two-adic Gauss factors remain primitive. The unchanged $3,r,m$ factors have the exact nonvanishing of [R105 §4](r105-operator-large-shared-alias-joint-cut.md#4-a-live-witness-on-a-large-shared-alias-with-radical-six), including its unique unit frequency at the large $3$-power. Finally choose $(j,u,v,a,c)=(1,2,1,W_*,1)$. Its shared difference $W_*-1$ lies above $L_0$ and at most $V_s$, and its conductor product is
$rm\,3^{\ell+1-v_3(W_*-1)}2^{t+2}=Q^{816/1000+o(1)}<Q^{167/200}$.
This is a strict new eligible nonzero original incidence coefficient, not a lower bound for an integrated or parity-reduced packet field.
