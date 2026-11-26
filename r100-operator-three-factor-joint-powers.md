# Joint conductor powers on all three CRT factors

A pair can survive all the preceding one- and two-factor cuts and still have a small product of the three conductors. The exact partner forces a translated power map on each of the two mixed factors. Because the count is now sparse in the entire CRT modulus, the actual alias sum can use a harmonic bound on its coprime factor rather than the length of the alias range.

## 1. A three-factor sector of the retained field

Work with $Z_{\rm shmix}$ from [R99](r99-operator-unequal-shared-leg-powers.md#1-exact-selection-and-packet-estimate) on the same complete even shell, with the genuine transported profiles $h,f$, common taper, original $J^{-1}$ normalization, and high-denominator packet $\mathcal C_+(B,R)$. Assume original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Preserve $k>K\ge A/Q$, $(2k,b)<G$, $z,w>A$, all earlier selections and the original signs. Both R99 inputs are allowed, with or without the two exact R86/R87 parity removals and with $K\ge2P$ in the former case.

At fixed $q=2k,b$ use the genuine decomposition

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
  q=r_b h_q,\quad s=d h_q,\qquad q'=qb=r_b m s ,
 \tag{1}
$$

as in R99 (1). The factors $r_b,m,s$ are pairwise coprime, $r_b$ is the full alias part on primes outside $b$, and $h_q$ has the same prime support as $d$. The individual leg factors are denoted by $\alpha,\alpha'\bmod r_b$, $\eta,\eta'\bmod m$, and $\gamma,\gamma'\bmod s$, respectively.

Fix $D,D_0\ge1,\ C>0$, and $V_Q=\lfloor(\log Q)^C\rfloor$. Only on the true aliases with $d\ge D_0$, delete from $Z_{\rm shmix}$ the remaining pairs satisfying

$$
\operatorname{cond}(\alpha^j)\,
 \operatorname{cond}(\eta^u(\eta')^v)\,
 \operatorname{cond}(\gamma^a(\gamma')^c)\le D
 \quad\text{for some }1\le j,u,v,a,c\le V_Q,\quad u\ne v,\quad a\ne c ,
 \tag{2}
$$

with integer exponents. Conductors are primitive inducing conductors, with conductor one at the trivial factor. Both unequal conditions are part of this selection. Every earlier leg or product condition remains in force. Denote the resulting field by $Z_{\rm three}$; this is a deletion before the original unequal numerator detunings.

With $R_*=1+R$ and the same packet norm,

$$
\|Z_{\rm shmix}-Z_{\rm three}\|_{\rm pkt}
 \ll_{\Gamma,\Theta,C,\epsilon}
      Q^\epsilon\frac{BD}{\sqrt{D_0}}
      \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

The estimate includes arbitrary prime powers in the denominators. It persists under fixed orthogonal spatial compression or restriction to a subset of the packet. The deletion can also be restricted to any subset fixed by $k,b$.

At $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, take $D_0=Q^{1/5},D=Q^{7/10}$, keeping the previous thresholds exactly as in R99's example. Then (3) is $O_{\epsilon,C}(Q^{-3/800+\epsilon})$. In the post-parity version the inherited sharp $\widehat T,\widehat P$ comparison remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm three}$. This bounds a deleted sector on one packet; it is not a surviving-covariance, individual even modulus, other packet, or weak S estimate.

## 2. Exact joint fibers at one full product

At fixed $q,b$, let $\nu=\nu_d\rho\bmod b$ be the genuine full product. The original incidence forces the unique partner on the whole progression modulus, namely $\xi'=(\nu\circ\pi)\bar\xi$ with $\pi$ unit reduction to $b$. On the factors of (1), its components satisfy

$$
\alpha'=\bar\alpha,\qquad
  \eta'=\rho\bar\eta,\qquad
  \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{4}
$$

where $\pi_s$ reduces units modulo $s$ to units modulo $d$. These are the original full-product equalities, not an imposed diagonal.

For this fixed full product, the displayed conductors in (2) are the conductors of the three components

$$
\bigl(\alpha^j,\ \eta^{u-v}\rho^v,\
                         \gamma^{a-c}(\nu_d\circ\pi_s)^c\bigr).
 \tag{5}
$$

The union of their selection conditions is invariant under the original partner involution: the alias power conductor is invariant under conjugation and the two mixed exponent pairs can be swapped simultaneously. All previous paired supports are likewise fixed and invariant at this full product, as in R99 §2. In particular the R99 complement on the shared pair remains on the same true legs, rather than being replaced by a product-only condition. The old full-product projectors simply keep or omit the coefficient indexed by $\nu$. Thus (2) inside this retained field is implemented by the same genuine projected progression vector $F_\nu$ on both raw legs. The optional parity pieces have their original per-leg projections. No norm inequality for arbitrary pair masks is being used.

For $j\ge1$ write $T_j(n)=|\ker(\chi\mapsto\chi^j)|$ on the character group of $n$, with $T_j(1)=1$, and $H(n)=\sum_{j\le V_Q}T_j(n)$. For each tuple of exponents in (2), the map (5) is a translate of a homomorphism on the character group of the coprime product $r_b m s=q'$, with attained fibers of size

$$
T_j(r_b)T_{|u-v|}(m)T_{|a-c|}(s).
$$

Both differences are nonzero. The number of output characters of conductor $\le D$ on $q'$ is at most $D\tau(q')$ by counting possible inducing conductor divisors. Their total conductor is the product of the three component conductors because the three moduli are coprime. Summing over the exponent tuples, using at most $2V_Q$ choices of a pair per absolute difference, and dividing by $\phi(q')$ proves that the fraction of all original progression characters used by $F_\nu$ is bounded by

$$
O_{\Theta,C,\epsilon}\!\left(
             Q^\epsilon\frac{D H(r_b)H(m)H(s)}{r_b m s}\right).
 \tag{6}
$$

This bound is uniform in $\nu$; all earlier cuts can only shrink it. It uses the subpower divisor and totient costs on the actual polynomial parameter ranges. For $V_Q<2$ the deletion is empty.

The genuine centered vector has the usual normalized residue Parseval, so the pointwise squared upper bound $O_\epsilon(Q^\epsilon z)$ and the per-character [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference) integrated squared increment bound $O_\epsilon(Q^\epsilon X|t|)$ for $1\le|t|\le X/4$ both scale by (6). Here $X$ is on the original polynomial raw scales. This follows by summing the uniform individual estimates on the genuine selected character set, not from independence of different characters or aliases. We always absorb finitely many subpower factors by taking smaller intermediate $\epsilon$'s.

## 3. Common-test transfer and the harmonic alias sum

At fixed full product $\nu$, the true scalar incidence bilinear form of [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms) has bound $O_\epsilon(Q^\epsilon\sqrt{\mathfrak e(q,b)}\,\|U\|_2\|V\|_2)$ for arbitrary complex unit residue vectors $U,V$, where $\mathfrak e(q,b)=d/(q,d)$. It holds after the two normalized residue expansions, and for raw-Fourier-transformed arguments as well. The two difference orientations have transpose factor $\nu(-1)$, furnishing the exact symmetric and skew forms. One must not replace this fixed-full-product estimate by a shared numerator Parseval on a leg support depending on $\nu_d$.

Use the exact common-test argument of R99 §2 with the new squared bounds from (6). For the cosine marginal identity and the skew interval-restricted raw translation, the same genuine $F_\nu$ appears in both arguments. The direct bounds and the signed sum orientation use its squared pointwise bound. For the optional parity pieces the fixed character restrictions commute with their auxiliary leg parity projections. The two exact reflected incidences coincide on the relevant even leg, so the prior reflected derivative estimates apply on the sharp masks; the genuine signs and overlap rule remain unchanged. No marginal identity is applied to those masks. Thus, with the same common-test seminorms $\mathcal K=K_1+QK'_2$ and, when needed, the extra $Q(E_\infty+E_1)$ from $P/k\le1/2$, the fixed-product HS bound is
$O_\epsilon(Q^\epsilon\sqrt{\mathfrak e(q,b)}\,D H(r_b)H(m)H(s)(r_bms)^{-1}\mathcal K)$.
All products Parseval on the reduced numerator group adds a factor at most $\phi(b)\le b$, since the bound is uniform in $\nu$. The exact per-alias joint numerator cost is therefore bounded by

$$
O_\epsilon\!\left(Q^\epsilon b\sqrt{\mathfrak e(q,b)}
                      \frac{D H(r_b)H(m)H(s)}{r_bms}\,\mathcal K\right).
 \tag{7}
$$

This is still at a common test before the unequal detunings.

Fix $b$ and a unitary divisor $d=b_\parallel$, putting $m=b/d$. Write $L_{b,d}$ for the sum over its genuine eligible aliases of the arithmetic factor in (7) without $Q^\epsilon b$ and $\mathcal K$, and put it equal to zero for $d<D_0$. Each possible pair $r_b,h_q$ determines at most one $k$, and $r_b h_q\le8M$. Since $d,h_q$ have the same prime support, R99 (9) gives $H(dh_q)\le2V_Q H(d)$. Moreover every $h_q$ is divisible by $\operatorname{rad}(d)$, as is $(q,d)$. Thus

$$
L_{b,d}
   \ll_{\Theta,C,\epsilon} Q^\epsilon
       \frac{D H(m)H(d)}{m\sqrt d\,\sqrt{\operatorname{rad}(d)}}
       \sum_{\substack{\operatorname{rad}(d)\mid h\\
                             p\mid h\Rightarrow p\mid d}}
                 \frac1h\sum_{r\le8M/h}\frac{H(r)}r .
 \tag{8}
$$

Here $h>8M$ has empty inner sum. The replacement is only a positive upper count over $h$ and $r$; in the field the actual common-divisor and all other gates remain. The inner sum is uniformly $O_\epsilon(Q^\epsilon)$ by the [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) harmonic torsion bound, summed over the polylogarithmic number of power orders. The remaining positive geometric sum is

$$
\sum_{\substack{\operatorname{rad}(d)\mid h\\
                              p\mid h\Rightarrow p\mid d}}\frac1h
             =\frac1{\operatorname{rad}(d)}
                         \prod_{p\mid d}(1-1/p)^{-1}
             \ll_\epsilon \frac{Q^\epsilon}{\operatorname{rad}(d)} .
$$

These statements also hold for $d=1$. Consequently

$$
L_{b,d}\ll_{\Theta,C,\epsilon}Q^\epsilon
                       \frac{D H(m)H(d)}
                              {m\sqrt d\,\operatorname{rad}(d)^{3/2}} .
 \tag{9}
$$

This step uses the $r_b^{-1}$ in the three-factor support bound, not cancellation in the alias signs or a total count proportional to $M$.

We will use

$$
\sum_{m\le B}\frac{H(m)^2}{m^2}\ll_\epsilon Q^\epsilon,\qquad
       \sum_{d\le B}\frac{H(d)^2}{\operatorname{rad}(d)^3}
                                      \ll_{\Theta,C,\epsilon}Q^\epsilon .
 \tag{10}
$$

The first is bounded by the square of the positive R90 harmonic sum at polynomial cutoff $B$. For the second, $H(d)^2\le V_Q\sum_{j\le V_Q}T_j(d)^2$. At fixed $j$ apply Rankin with any fixed $\delta>0$ to obtain the upper bound

$$
B^\delta\prod_p
          \left(1+\frac1{p^3}\sum_{e\ge1}
                                  \frac{T_j(p^e)^2}{p^{e\delta}}\right).
$$

At $p\nmid2j$, $T_j(p^e)=\gcd(j,p-1)\le p$; its logarithmic cost summed over those primes is $O_\delta(\sum_p p^{-1-\delta})=O_\delta(1)$. At $p\mid2j$, $T_j(p^e)\le2j$ gives a local logarithm $O_\delta(\log(2j))$ and an aggregate $O_\delta(\log^2(2j))=o(\log Q)$, uniformly in the stated exponent range. Positivity justifies the Euler majorant, including all powers of a prime. Choosing $\delta$ small relative to the desired $\epsilon$, using polynomial $B$, proves the second estimate in (10) including the extra $V_Q$ factors.

At fixed $b$, the joint numerator bound from (7) has arithmetic factor $Q^\epsilon b\sum_{d\mid b,\,(d,b/d)=1}L_{b,d}$. Square by Cauchy over the at most $\tau(b)$ unitary divisors, then use $b^2\le B^2$ and relax to all $dm\le B$ in this positive bound. By (9), the gate $d\ge D_0$, and (10),

$$
\begin{split}
 \sum_{b\le B}b^2
       \left(\sum_{\substack{d\mid b\\(d,b/d)=1}}L_{b,d}\right)^2
 &\ll_{\Theta,C,\epsilon}Q^\epsilon \frac{B^2D^2}{D_0}
           \sum_{m\le B}\frac{H(m)^2}{m^2}
           \sum_{d\le B}\frac{H(d)^2}{\operatorname{rad}(d)^3}\\
 &\ll_{\Theta,C,\epsilon} Q^\epsilon B^2D^2/D_0 .
 \end{split}
 \tag{11}
$$

All restrictions on a subset fixed by $k,b$ only lower these positive counts.

Finally use the exact [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) common Taylor tests. Keep the original output coefficient of modulus at most $2^{-n}$ at Taylor order $n$, and every original outer unit-modulus phase. At offset $\ell$, the weighted $K_1$ cost is $O(1+|\ell|)$, and the other weighted seminorms cost $O(S^{-1}+(1+|\ell|)^2/Q)$ as in R99. Divide by $J\asymp Q$ and sum in squared norm over $|\ell|\le R+1$. Equation (11) yields (3) with its three offset factors and the true detuning. The numerical arithmetic exponent is $99/100$, giving final exponents $-1/160,-3/800,-19/4000$. The inherited sharp comparison then follows by triangle. No independently estimated unit, boundary, or deterministic term is altered here.

## 4. An eligible nonzero coefficient after all earlier cuts

At the example scales take $d=2^e$ the least power of $2$ at least $Q^{1/5}$, an odd prime $m\asymp Q^{19/100}$ with $b=dm$ in the high band, and $r=k\asymp Q^{9/20}$ an odd prime. Such primes can be chosen by Bertrand's postulate. Then $q=2r,\ r_b=r,\ h_q=2,\ s=2^{e+1}$, and the common-divisor, lower alias, and $d$ gates are satisfied. On $r$ take generator-order characters that are conjugate partners, keeping conductor $r$ under every preceding small power. On $m$ use a generator $\eta$ and pair it with $\eta'=\eta^{2V^*}$, where $V^*$ bounds the finitely many log-power cutoff ranges here and in earlier rounds. All earlier signed mixed nonzero exponent pairs on $m$ have exponent of absolute value between $1$ and $m-2$ for large $Q$, and all earlier individual and product powers are also nonprincipal there. Thus the $m$-conductors are $m$, the earlier signed joint test fails since $rm\asymp Q^{16/25}>Q^{3/5}$, and the R97 alias/shared test already fails because $r>Q^{51/125}$.

On $s$, use a primitive character $\gamma$ of sign value one and $5$-generator order $2^{e-1}$. Put $t=\lfloor(\log_2 Q)/25\rfloor$ and set

$$
\gamma'=\gamma^{-3+2^{e-1-t}} .
$$

The exponent is odd, so $\gamma'$ is primitive. Their product is $\gamma^{-2+2^{e-1-t}}$, whose exponent has $2$-adic valuation one for large $Q$. It induces a primitive $\nu_d$ of conductor $2^e$ on $d$, and all its allowed powers have conductor $2^{e-O(\log\log Q)}$, so [R98](r98-operator-shared-product-power-cut.md#1-exact-sector-and-packet-estimate) does not select this pair. The full product also stays high on $m$.

For every old R99 shared pair of exponents $a,c$, the exponent is $a-3c+c2^{e-1-t}$. If $a=3c$, its conductor is $2^{t+2-v_2(c)}$ for large $Q$, since the resulting $5$-generator order is $2^{t-v_2(c)}$. If $a\ne3c$, the $2$-adic valuation is $v_2(a-3c)=O(\log\log Q)<e-1-t$, so its conductor is $2^{e+1-O(\log\log Q)}$. Both cases exceed the prior $Q^{3/1000}$ threshold. The original local incidence is nonzero: modulo $2$ its congruence is automatic for odd units, and the two primitive additive Gauss factors at $s$ are nonzero, as are the alias and coprime Gauss factors. Now $j=1,u=2,v=1,a=3,c=1$ in (2) gives product $rm\,2^{t+2}\asymp Q^{17/25}<Q^{7/10}$. This is strict eligibility of a live original coefficient in the unmodified input, not a lower bound on the integrated packet field.
