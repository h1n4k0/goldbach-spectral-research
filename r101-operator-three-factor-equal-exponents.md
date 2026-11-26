# Equal-exponent branches of the three-factor conductor cut

A mixed exponent can become a power of the product rather than a power of either individual leg. On the retained packet this can happen on either denominator factor, or on both. Counting these branches at a fixed product would miss the gain. Averaging over the genuine products after the fixed-product estimate gives an additional deletion, with the original signs and detunings.

## 1. The exact additional deletion

Use the genuine field $Z_{\rm three}$ retained by [R100 §1](r100-operator-three-factor-joint-powers.md#1-a-three-factor-sector-of-the-retained-field) on the complete even shell. Keep the original transported parent profiles $h,f$, common taper, $J^{-1}$ normalization, separated high-denominator packet $\mathcal C_+(B,R)$, polynomial parameter ranges, $k>K\ge A/Q$, $(2k,b)<G$, $z,w>A$, and all the earlier selections and signs. Assume original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Both R100 inputs are allowed: the original one and the one after the two exact R86/R87 parity removals, with $K\ge2P$ for the latter.

At each actual $q=2k,b$, use the R100 factorization

$$
b=dm,\qquad d=b_\parallel,\quad m=b_\perp,\qquad
  q=r_bh_q,\qquad s=dh_q,\qquad q'=qb=r_bms .
 \tag{1}
$$

The factors $r_b,m,s$ are pairwise coprime and $h_q$ is supported on precisely the primes of $d$. Write $(\alpha,\eta,\gamma)$ and $(\alpha',\eta',\gamma')$ for the individual components of the two progression characters on $r_b,m,s$, respectively.

Fix $D,D_0\ge1$, $C>0$, and $V_Q=\lfloor(\log Q)^C\rfloor$. Only at genuine aliases with $d\ge D_0$, delete from $Z_{\rm three}$ the remaining pairs satisfying

$$
\operatorname{cond}(\alpha^j)
 \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)
 \operatorname{cond}\bigl(\gamma^a(\gamma')^c\bigr)\le D
 \quad\text{for some integers }1\le j,u,v,a,c\le V_Q
             \text{ with }u=v\text{ or }a=c .
 \tag{2}
$$

Both equalities together are allowed. A conductor is the primitive inducing conductor, including conductor one for a trivial component. This is an incremental deletion before the original unequal numerator detunings. In particular (2) does not change the earlier R100 deletion with both exponent pairs unequal.

Denote the new field by $Z_{\rm eq}$. With $R_*=1+R$ and the packet norm of R100,

$$
\|Z_{\rm three}-Z_{\rm eq}\|_{\rm pkt}
   \ll_{\Gamma,\Theta,C,\epsilon}
   Q^\epsilon B\sqrt{MD}\left[
       \frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

The estimate permits arbitrary denominator prime powers. It holds after fixed orthogonal spatial compression or restriction to a subset of the packet. The deletion can also be limited to any subset fixed by $k,b$.

At $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, keep every previous numerical threshold and take $D_0=Q^{1/5}$ and $D=Q^{6032/10000}$ in (2). Then (3) is $O_{\epsilon,C}(Q^{-43/20000+\epsilon})$, so the post-parity sharp $\widehat T,\widehat P$ comparison remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm eq}$. This choice of $D$ for the new branches is separate from the R100 $Q^{7/10}$ cutoff for both unequal. The bound is only for the specified deletion, not the surviving covariance, other packets, a prescribed even modulus, or weak S.

## 2. Average the exact conditional support

Fix $q,b$ and its true full product $\nu=\nu_d\rho\bmod b$. Put $r=r_b$. The unique actual partner has

$$
\alpha'=\bar\alpha,\qquad
 \eta'=\rho\bar\eta,\qquad
 \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{4}
$$

where $\pi_s$ reduces units from $s$ to $d$. This is the genuine full-product conditioning of [R100 (4)](r100-operator-three-factor-joint-powers.md#2-exact-joint-fibers-at-one-full-product). The union in (2) is invariant under this partner involution. The alias conductor is unchanged by conjugation and interchanging the two exponents in each mixed pair simultaneously preserves the allowed union, including its equality branches. The previous paired masks stay fixed and partner-invariant at this same full product. The previous full-product masks just keep or omit its coefficient. Thus intersecting with (2) is implemented by exactly the same genuine selected progression vector $F_\nu$ on both raw legs of that coefficient, with the earlier leg parity projections kept in their corresponding terms.

Let $f_\nu=f_\nu(q,b)$ be the fraction of all first-leg characters on $q'$ in this exact selected support at fixed $\nu$, set to zero at a discarded full product. Let

$$
g=g(q,b)=\frac1{\phi(b)}\sum_{\nu\bmod b} f_\nu ,
           \qquad 0\le f_\nu,g\le1 .
 \tag{5}
$$

We relax prior masks only to upper-bound (5), not in the field. For integers $j\ge1$ put $T_j(n)=|\ker(\chi\mapsto\chi^j)|$ on the character group of $n$, including $T_j(1)=1$, and $H(n)=\sum_{j\le V_Q}T_j(n)$. We claim

$$
g(q,b)\ll_{\Theta,C,\epsilon}
        Q^\epsilon\,\frac{D H(r)H(m)H(d)}{rmd}.
 \tag{6}
$$

In fact fix an exponent tuple. On the coprime factors of (1) the output character in (2) has components

$$
\bigl(\alpha^j,\ \eta^{u-v}\rho^v,\
                            \gamma^{a-c}(\nu_d\circ\pi_s)^c\bigr).
 \tag{7}
$$

For any coprime product of factors used below, the number of candidate outputs of product conductor at most $D$ is at most $D\tau$ of that modulus: choose the inducing conductor among its divisors at most $D$, then at most that divisor's totient many characters. Translated nonzero power maps on their finite character groups have attained fibers of size $T_j$ for the absolute value $j$ of the exponent. We use these facts for the following three counts.

* If $u=v$ and $a\ne c$, the $m$-output is $\rho^v$ regardless of $\eta$. At fixed $\nu_d$ the count in the averaged fraction is now over $(\alpha,\rho,\gamma)$; the entire $\eta$-group cancels between numerator and denominator. On $rms$ the relevant map has fibers of size $T_j(r)T_v(m)T_{|a-c|}(s)$. Divide the resulting upper count by $\phi(r)\phi(m)\phi(s)$, then average over $\nu_d$. This step does not replace the $\eta$ component of the actual progression vector.
* If $u\ne v$ and $a=c$, the shared output is the lift of $\nu_d^c$, so its primitive conductor is the same as on $d$ and does not depend on $\gamma$. At fixed $\rho$, count $(\alpha,\eta,\nu_d)$ on $rmd$ and divide by $\phi(r)\phi(m)\phi(d)$. The attained fiber has size $T_j(r)T_{|u-v|}(m)T_c(d)$. Now average over $\rho$.
* If both are equal, the count is on $(\alpha,\rho,\nu_d)$ mapping to $(\alpha^j,\rho^v,\nu_d^c)$, with denominator $\phi(r)\phi(m)\phi(d)$ and fiber size $T_j(r)T_v(m)T_c(d)$.

The averaging in each branch is exactly (5), since the full product factors as independent indices over $d,m$. The exponent-tuple union introduces only a fixed polylogarithmic loss, and all divisor and inverse totient ratios of the displayed moduli are $O_\epsilon(Q^\epsilon)$. In the first branch we initially obtain $H(s)/s$ in place of $H(d)/d$. From [R99 (9)](r99-operator-unequal-shared-leg-powers.md#3-sum-the-full-shared-part-of-each-actual-alias), $T_j(dh_q)\le2jT_j(d)$ on the same prime support, so $H(s)/s\le2V_Q H(d)/d$. After absorbing the subpower factor this proves (6). All subpower factors in this proof use smaller intermediate $\epsilon$'s where necessary. Equation (6) is not a uniform upper bound on $f_\nu$ by a small quantity.

## 3. Weighted numerator Parseval and actual aliases

At each fixed $\nu$, normalized residue Parseval and the same uniform per-character auxiliary GRH bounds as R100 §2 give

$$
\begin{split}
   \|F_\nu(z)\|_2^2
     &\ll_\epsilon Q^\epsilon f_\nu z,\\
   \int_X^{2X}\|F_\nu(z+t)-F_\nu(z)\|_2^2\,dz
     &\ll_\epsilon Q^\epsilon f_\nu X|t|,
                  \qquad 1\le |t|\le X/4,
 \end{split}
 \tag{8}
$$

on the original polynomial raw scales. The second estimate is obtained by retaining the individual character bounds in [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference) before residue Parseval. Neither estimate uses a support average in either raw vector.

The original scalar incidence on general complex raw residue vectors at fixed full product is bounded by $Q^\epsilon\sqrt{\mathfrak e(q,b)}$ times their two norms, where $\mathfrak e(q,b)=d/(q,d)$, by [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms). This holds after the two normalized residue expansions, including their raw-Fourier arguments. The difference transpose at this product has factor $\nu(-1)$. Apply the common-test argument of [R100 §3](r100-operator-three-factor-joint-powers.md#3-common-test-transfer-and-the-harmonic-alias-sum) with (8): its cosine marginal identity and its skew common interval-restricted translation use $F_\nu$ on both legs, and the signed sum uses the pointwise factors from (8). For the optional post-parity input the fixed character restrictions commute with both leg parity projections. The reflected identities for the auxiliary-even leg and the original overlap convention are unchanged. Their pointwise bounds use (8); no uncut marginal formula is applied to the sharp parity masks.

Consequently the fixed-product common-test HS bound is $O_\epsilon(Q^\epsilon\sqrt{\mathfrak e(q,b)} f_\nu\mathcal K)$ with $\mathcal K=K_1+QK'_2$, enlarged by $Q(E_\infty+E_1)$ when using the parity pieces and $P/k\le1/2$, as in R100. Now use full numerator Parseval in counting measure. Its factor is

$$
\sqrt{\phi(b)\sum_{\nu\bmod b} f_\nu^2}
          \ \le\ \phi(b)\sqrt{g(q,b)} .
$$

The inequality uses $f_\nu^2\le f_\nu$ only **after** the individual coefficient estimates. Thus the joint numerator cost per actual alias, still at a common test before detuning, is

$$
O_\epsilon\bigl(Q^\epsilon b
                \sqrt{\mathfrak e(q,b)g(q,b)}\,\mathcal K\bigr).
 \tag{9}
$$

In particular this step has not used orthogonality across aliases or a shared numerator Parseval with a single vector in spite of its dependence on the full product.

At fixed $b$ group the true aliases by their unitary divisor $d=b_\parallel$, so $m=b/d$ within a group. There are $O(M/\operatorname{rad}(d))$ such aliases since $\operatorname{rad}(d)\mid2k$ and $k\le4M$, with the group empty if $\operatorname{rad}(d)>8M$. For each $r_b=r$ the count is $O_\epsilon(Q^\epsilon)$ uniformly by the [R89 §4](r89-operator-prime-to-denominator-alias-conductors.md#4-count-the-actual-aliases-then-restore-the-fourier-packet) Rankin count on the actual shared part $h_q=2k/r\le8M$ supported on primes of $b$. Thus (6) and the [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) harmonic torsion bound give

$$
\sum_{k:\,d(k,b)=d} g(q,b)
      \ll_{\Theta,C,\epsilon}Q^\epsilon\frac{D H(m)H(d)}{md},
       \qquad
       \sum_{m\le B}\frac{H(m)}m
                             \ll_{\Theta,C,\epsilon} Q^\epsilon .
 \tag{10}
$$

Only positive upper counts are enlarged; no alias restriction is changed in (9). Define $L_{b,d}=\sum_{k:\,d(k,b)=d}\sqrt{\mathfrak e(q,b)g(q,b)}$ on the actual eligible aliases and put it equal to zero if $d<D_0$. Since $(q,d)\ge\operatorname{rad}(d)$, Cauchy in the actual alias group gives

$$
L_{b,d}^2\ll_{\Theta,C,\epsilon}
       Q^\epsilon\frac{M}{\operatorname{rad}(d)}
       \frac{d}{\operatorname{rad}(d)}
       \frac{D H(m)H(d)}{md}
    = Q^\epsilon O_{\Theta,C,\epsilon}\!\left(
           \frac{MD H(m)H(d)}{m\operatorname{rad}(d)^2}\right).
 \tag{11}
$$

There is no $D_0$ improvement claimed for the new branches. Cauchy over the at most $\tau(b)$ unitary divisor groups, $b^2\le B^2$, and the positive enlargement to $dm\le B$ give

$$
\sum_{b\le B}b^2
     \left(\sum_{\substack{d\mid b\\(d,b/d)=1}}L_{b,d}\right)^2
 \ll_{\Theta,C,\epsilon}Q^\epsilon B^2 MD
        \sum_{m\le B}\frac{H(m)}m
        \sum_{d\le B}\frac{H(d)}{\operatorname{rad}(d)^2}
 \ll_{\Theta,C,\epsilon} Q^\epsilon B^2 MD .
 \tag{12}
$$

The second sum is the radical-square torsion estimate [R97 (11)](r97-operator-shared-product-joint-conductor.md#3-weighted-alias-summation), uniform on the polynomial ranges and allowing all powers of $d$. Restrictions fixed by $k,b$ only decrease these positive sums.

Finally use the exact distinct-detuning recovery of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) and [R100 §3](r100-operator-three-factor-joint-powers.md#3-common-test-transfer-and-the-harmonic-alias-sum). The Taylor coefficient at order $n$ in each numerator has absolute value at most $2^{-n}$; its exterior phase is kept unchanged. At offset $\ell$, the effective $K_1$ cost is $O(1+|\ell|)$, and $K'_2,E_\infty,E_1$ cost $O(S^{-1}+(1+|\ell|)^2/Q)$ with the original factorial weights. Divide by $J\asymp Q$ and square-sum over $|\ell|\le R+1$ using (12). This gives (3), including the independent $R_*^{3/2},R_*^{5/2},R_*^{1/2}$ offset factors. At the numerical choices the arithmetic exponent of $B\sqrt{MD}$ is $2479/2500$, and the largest final exponent is $-43/20000$, from the $R_*^{5/2}$ term. The inherited sharp comparison follows by the triangle inequality with all independent restoration and benchmark estimates unchanged.

## 4. A live shared-equal coefficient retained by R100

At the example scales take $d=2^e$ to be the least power of two at least $Q^{1/5}$ and choose an odd prime $m$ in $(B/(2d),B/d)$, so $b=dm$ lies in the high band. Take $k=r\asymp Q^{4101/10000}$ an odd prime. Both choices are possible by Bertrand's postulate. Then $q=2r,\ h_q=2,\ r_b=r,\ s=2^{e+1}$. In particular $d\ge D_0,\ (2k,b)=2<G,\ k>K$ at the preceding scales, and the optional $K\ge2P$ does not change the exponents.

On $r$ use a generator-order character and its conjugate; all individual alias powers in the preceding log ranges have conductor $r$. On $m$ take a generator $\eta$ and $\eta'=\eta^{2V^*}$, where $V^*$ bounds the finitely many fixed log-power ranges here and earlier. Every earlier mixed signed exponent on $m$ is nonzero and smaller in absolute value than $m-1$: if the coefficients of $\eta,\eta'$ are $u,v$, the exponent is $u+2V^*v$, with $1\le |u|,|v|\le V^*$. The individual and product powers also stay nonprincipal. Thus the earlier individual and mixed $m$ cuts do not apply, the joint alias/$m$ conductor exceeds its old threshold since $rm\asymp Q^{6001/10000}>Q^{3/5}$, and the R97 joint alias/shared product cut fails already from $r>Q^{51/125}$. The original high full product and its small-power cuts are respected by the high $m$-component.

On $s=2^{e+1}$ take the primitive character $\gamma$ with trivial sign on $-1$ and order $2^{e-1}$ on $5$. Put $t=\lfloor(305/100000)\log_2 Q\rfloor$, and set

$$
\gamma'=\gamma^{-1+2^{e-1-t}} .
$$

This odd exponent gives another primitive character. Their product is $\gamma^{2^{e-1-t}}$, with order $2^t$ on $5$, hence conductor $2^{t+2}$ and induced from $\nu_d$ on $d$ for sufficiently large $Q$. Each allowed small power of $\nu_d$ has conductor $Q^{.00305-o(1)}>Q^{3/1000}$, as its $5$-order loses only the $2$-valuation of that exponent. This is not deleted by the R98 shared product cut. For every earlier unequal shared pair the $\gamma$ exponent is $a-c+c\,2^{e-1-t}$, with valuation $v_2(a-c)=O(\log\log Q)$. Its conductor is $2^{e+1-O(\log\log Q)}=Q^{.20-o(1)}$, so the pair avoids R99. Each prior R100 test has both exponent pairs unequal, and every such product is $Q^{.8001-o(1)}>Q^{7/10}$. Thus the pair is present after R100.

The original incidence coefficient is nonzero for this pair in the unmodified input: at the $2$-adic factor the congruence modulo $2$ is automatic on odd unit arguments and both additive Gauss factors at $s$ are primitive and nonzero at unit frequencies. The conjugate factor at $r$ and the two coprime primitive Gauss factors at $m$ are also nonzero, as in [R100 §4](r100-operator-three-factor-joint-powers.md#4-an-eligible-nonzero-coefficient-after-all-earlier-cuts). Now take $j=1,\ u=2,\ v=1,\ a=c=1$; the product in (2) is $rm\,2^{t+2}\asymp Q^{.60315}<Q^{.6032}=D$ for sufficiently large $Q$. This gives strict eligibility of an actual new, nonzero incidence coefficient, not a lower bound for the integrated packet field or for the parity-reduced field.
