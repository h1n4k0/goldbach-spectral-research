# A larger shared-equal three-factor cut from two Gauss bounds

When the two shared exponents are equal, their mixed conductor is a power of the shared product. The earlier joint alias and coprime-denominator cutoff then bounds that shared conductor from above on any newly selected pair. Retaining the primitive shared-product conductor in the local incidence, as well as the bound by arithmetic excess, allows a larger cutoff than the unweighted average over full products.

## 1. Exact selection and packet estimate

Use the field $Z_{\rm eq}$ retained by [R101 §1](r101-operator-three-factor-equal-exponents.md#1-the-exact-additional-deletion). Keep the complete even shell, exact transported profiles $h,f$, common taper, original $J^{-1}$ normalization, high packet $\mathcal C_+(B,R)$, raw restrictions $z,w>A$, $k>K\ge A/Q$, and $(2k,b)<G$. All earlier selections, orientations and signs are in force. Assume original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. The theorem applies to both R101 inputs, including the post-R86/R87 parity version with $K\ge2P$.

At a true alias $q=2k$ and denominator $b$, keep

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
 q=r_bh_q,\quad s=dh_q,\qquad q'=qb=r_bms .
 \tag{1}
$$

Thus $r_b,m,s$ are pairwise coprime, and $d,h_q$ have precisely the same prime support. Use $(\alpha,\eta,\gamma)$ and $(\alpha',\eta',\gamma')$ for the two individual leg factors on these three moduli. Let $D_J$ be the actual earlier [R96 joint threshold](r96-operator-equal-and-signed-joint-powers.md#1-exact-enlargement-and-packet-bound). Take $C>0,\ V_Q=\lfloor(\log Q)^C\rfloor$, with the three ranges $1\le j\le V_Q,\ 1\le |u|,|v|\le V_Q$ all contained in the power ranges of that earlier cut. This containment is an assumption about the actual retained input, not a change to it. The exponent on the shared factor has no such restriction beyond $1\le a\le V_Q$. One can equivalently require the containment for the three indicated coordinates separately.

For $D,D_0\ge1$, delete from $Z_{\rm eq}$, only when $d\ge D_0$, the remaining pairs satisfying

$$
\operatorname{cond}(\alpha^j)\,
 \operatorname{cond}\bigl(\eta^u(\eta')^v\bigr)\,
 \operatorname{cond}\bigl(\gamma^a(\gamma')^a\bigr)\le D
 \quad
 \text{for some integers }
   1\le j,a\le V_Q,\qquad 1\le|u|,|v|\le V_Q .
 \tag{2}
$$

Conductors always mean primitive inducing conductors, including conductor one for a trivial component. There is no inequality or sign constraint on $u,v$ beyond the displayed ranges. In contrast, both shared exponents are **the same** $a$. This selection, like the earlier ones, is applied before the different numerator detunings.

Write $Z_{\rm gauss}$ for the new field. With $R_*=1+R$, the packet estimate is

$$
\|Z_{\rm eq}-Z_{\rm gauss}\|_{\rm pkt}
 \ll_{\Gamma,\Theta,C,\epsilon}
  Q^\epsilon\,\frac{B M^{1/2}D^{3/4}}{(D_JD_0)^{1/4}}
   \left[\frac{R_*^{3/2}+R_*^{5/2}}{Q}
                         +\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

It permits arbitrary denominator prime powers and restriction of the deletion to any subset fixed by $k,b$. It continues to hold after a fixed orthogonal spatial compression or restriction to a subset of the packet.

For the R101 numerical scales take $B=\lfloor Q^{39/100}\rfloor,\ M=D_J=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$ and $D_0=Q^{1/5},D=Q^{133/200}$, with a common fixed log-power range for the new and R96 alias and coprime factors. Keep the earlier thresholds unchanged, in particular $Q^{6032/10000}$ in R101. Then (3) is $O_{\epsilon,C}(Q^{-1/200+\epsilon})$. The inherited sharp $\widehat T,\widehat P$ comparison in the post-parity input remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm gauss}$. This extends the shared-equal sector to a larger conductor threshold; it does not extend that threshold to the other R101 branch with unequal shared exponents. It is not a bound on the surviving covariance, a prescribed even modulus, other packets, or weak S.

## 2. Keep the smaller true scalar coefficient

At fixed $q,b$ and exact full product $\nu=\nu_d\rho\bmod b$, the individual partners satisfy [R100 (4)](r100-operator-three-factor-joint-powers.md#2-exact-joint-fibers-at-one-full-product):

$$
\alpha'=\bar\alpha,\qquad
    \eta'=\rho\bar\eta,\qquad
    \gamma'=(\nu_d\circ\pi_s)\bar\gamma ,
 \tag{4}
$$

where $\pi_s$ reduces units from $s$ to $d$. In (2) the shared factor is therefore a lift of $\nu_d^a$, with the same inducing conductor as on $d$. The new union is invariant under interchanging the true partners, because this conjugates the alias power and swaps the two coprime-denominator exponents. Thus at this full product, after all earlier pair and full-product masks, use the same selected genuine progression vector $F_\nu$ on both legs. Auxiliary parity projections, where present, are still applied on their corresponding legs.

Every actual pair eligible for (2) survives the entire [R96 selector](r96-operator-equal-and-signed-joint-powers.md#2-exact-conditioning-and-the-averaged-character-count). In particular for its witnessing triple $(j,u,v)$, the product of the first two conductors in (2) is strictly greater than $D_J$, by the stipulated range containment, whether or not $u=v$. Hence any full product with nonempty new support obeys

$$
\operatorname{cond}(\nu_d^a)\le D/D_J
       \quad\hbox{for at least one }a\le V_Q .
 \tag{5}
$$

For characters on arbitrary $d$, [R98 (4)](r98-operator-shared-product-power-cut.md#2-the-actual-conductor-in-the-scalar-gauss-bound) bounds the conductor before powering by $2a\,\operatorname{rad}(d)\operatorname{cond}(\nu_d^a)$. This is the actual primitive-conductor loss, including the extra factor at $2$ and the tame prime support. Thus for every nonempty product in (5),

$$
\operatorname{cond}(\nu_d)
                 \le 2V_Q\,\operatorname{rad}(d)\,D/D_J .
 \tag{6}
$$

No condition is inferred for empty products, whose new coefficients are zero. In particular the whole new support is empty if $D\le D_J$.

At this fixed full product let $\mathscr C_\nu(U,V)$ be the true bilinear coefficient of the reduced numerator character $\nu$ in the original residue incidence on complex vectors $U,V$. The unrelaxed local estimate of [R91 §2](r91-operator-denominator-product-power-conductors.md#2-a-mixed-crt-bound-for-the-true-restricted-numerator-vector), as made explicit in [R98 §2](r98-operator-shared-product-power-cut.md#2-the-actual-conductor-in-the-scalar-gauss-bound), is

$$
|\mathscr C_\nu(U,V)|
    \ll_\epsilon Q^\epsilon
           \sqrt{\operatorname{cond}(\nu_d)}\,\|U\|_2\|V\|_2 .
 \tag{7}
$$

Indeed the $qd$-part has a pair coefficient bounded by $Q^\epsilon\phi(qd)\sqrt{\operatorname{cond}(\nu_d)}$, and the coprime $m$-part by $m$ from two primitive-additive Gauss bounds for the individual characters. With $m/\phi(m)\ll Q^\epsilon$ the full pair bound is $Q^\epsilon\phi(q')\sqrt{\operatorname{cond}(\nu_d)}$. In the two normalized residue expansions, there is just one possible partner at each first-leg character; Cauchy and Parseval give the cancellation of the remaining normalizing factor. In particular (7) is an estimate on general vectors, including the raw Fourier arguments in the skew part. It is not an estimate solely on the original individual progression coefficients.

The other valid bound for the **same** coefficient is [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms), with $Q^\epsilon\sqrt{\mathfrak e(q,b)}$ in place of the conductor factor, where $\mathfrak e(q,b)=d/(q,d)$. Both respect the transpose factor $\nu(-1)$ for the two differences at fixed product. Take their minimum using (6), and absorb the log power into $Q^\epsilon$. On the nonempty products we can therefore use the common scalar factor $Q^\epsilon\sqrt{\mathfrak a(q,b)}$, with

$$
\mathfrak a(q,b)=
                  \min\!\left(\mathfrak e(q,b),
                              D\operatorname{rad}(d)/D_J\right).
 \tag{8}
$$

Neither cap is applied to an arbitrary pair mask; the common vector projection from (4) implements the new selection inside each exact full product.

## 3. Average the support and sum the actual aliases

Let $f_\nu=f_\nu(q,b)$ be the fraction of all progression characters on $q'$ in the actual selected support at fixed full product. Set it to zero on discarded products and put $g(q,b)=\phi(b)^{-1}\sum_{\nu\bmod b}f_\nu$. For $T_j(n)=|\ker(\xi\mapsto\xi^j)|$ on the character group of $n$, put $H(n)=\sum_{j\le2V_Q}T_j(n)$. We have

$$
g(q,b)\ll_{\Theta,C,\epsilon}Q^\epsilon\,
                        \frac{D H(r_b)H(m)H(d)}{r_bmd}.
 \tag{9}
$$

For the upper count only, relax all earlier cuts. At fixed $\rho$, if $u\ne v$ the relevant variables are $(\alpha,\eta,\nu_d)$, going to
$(\alpha^j,\eta^{u-v}\rho^v,\nu_d^a)$ on $r_bmd$. The free $\gamma$-group cancels in the fraction of characters. If $u=v$, instead average over $\rho,\nu_d$ and count $(\alpha,\rho,\nu_d)$ mapped to $(\alpha^j,\rho^v,\nu_d^a)$. This is the two shared-equal cases of [R101 §2](r101-operator-three-factor-equal-exponents.md#2-average-the-exact-conditional-support). The absolute value of the nonzero translated power exponent lies at most $2V_Q$. The output count is at most $D\tau(r_bmd)$ by CRT and the count by inducing divisors. Divide by $\phi(r_b)\phi(m)\phi(d)$ and sum over the allowed tuples, absorbing their subpower lengths and divisor and inverse totient factors. This proves (9), which bounds an average, not a pointwise support fraction.

The uniform individual auxiliary-GRH pointwise and progression-increment estimates, with centered residue Parseval, give exactly [R101 (8)](r101-operator-three-factor-equal-exponents.md#3-weighted-numerator-parseval-and-actual-aliases) with this $f_\nu$. Apply the original same-vector common-test argument at fixed $\nu$ with (8). The cosine difference and skew raw translation use the same $F_\nu$; the signed sum and reflected sharp parity terms use their original pointwise bounds with the same support factor. The exact parity commutations and overlap remain those of [R101 §3](r101-operator-three-factor-equal-exponents.md#3-weighted-numerator-parseval-and-actual-aliases), so no marginal identity is applied to the sharp parity regions. This gives a fixed-product HS bound $O_\epsilon(Q^\epsilon\sqrt{\mathfrak a(q,b)}\, f_\nu\mathcal K)$, with old common seminorms $\mathcal K=K_1+QK'_2$, or this plus $Q(E_\infty+E_1)$ when needed. Full numerator Parseval then costs at most $b\sqrt{g(q,b)}$ in place of $f_\nu$, since $\sqrt{\phi(b)\sum_\nu f_\nu^2}\le\phi(b)\sqrt g$. The resulting per-alias bound is

$$
O_\epsilon\!\left(Q^\epsilon b
                         \sqrt{\mathfrak a(q,b) g(q,b)}\,
                                  \mathcal K\right).
 \tag{10}
$$

Fix $b,d=b_\parallel$ and write $m=b/d$. The genuine group has at most $O(M/\operatorname{rad}(d))$ aliases, as $\operatorname{rad}(d)\mid 2k$ and $k\le4M$; for each $r_b$ there are at most $O_\epsilon(Q^\epsilon)$ realizations, by the [R89 §4](r89-operator-prime-to-denominator-alias-conductors.md#4-count-the-actual-aliases-then-restore-the-fourier-packet) Rankin count for the shared part $h_q$. The actual aliases can only be fewer with additional gates. Thus summing (9) as in [R101 (10)](r101-operator-three-factor-equal-exponents.md#3-weighted-numerator-parseval-and-actual-aliases), and using the [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) harmonic estimate for $H(r_b)/r_b$, gives $\sum_k g(q,b)\ll Q^\epsilon D H(m)H(d)/(md)$ within this group. Also $\mathfrak e(q,b)\le d/\operatorname{rad}(d)$. Cauchy over the literal aliases now gives

$$
\begin{split}
 L_{b,d}^{\,2}
 &\ll_{\Theta,C,\epsilon} Q^\epsilon\,\frac{H(m)H(d)}m
       \min\!\left(\frac{MD}{\operatorname{rad}(d)^2},
                         \frac{MD^2}{D_Jd}\right)\\
 &\ll_{\Theta,C,\epsilon} Q^\epsilon
        \frac{MD^{3/2}}{\sqrt{D_J}}\,
        \frac{H(m)H(d)}{m\operatorname{rad}(d)\sqrt d},
 \qquad L_{b,d}=\sum_{k:\,d(k,b)=d}
                             \sqrt{\mathfrak a(q,b)g(q,b)} .
 \end{split}
 \tag{11}
$$

Set $L_{b,d}=0$ for $d<D_0$. The last step uses the geometric mean of the two estimates, not alias orthogonality. No $k$-independent approximation of the actual covariance is made.

The radical-weighted moment required for (11) follows directly from the Euler estimates behind R90:

$$
\sum_{d\le B}\frac{H(d)d^{-\delta}}{\operatorname{rad}(d)}
              \ll_{\Theta,C,\delta,\epsilon} Q^\epsilon
               \qquad(\delta>0\text{ fixed}).
 \tag{12}
$$

To see this, work first with one $T_j$. It is multiplicative in coprime moduli. By positivity the sum is at most $\prod_{p\le B}(1+p^{-1}\sum_{e\ge1} T_j(p^e)p^{-e\delta})$. For $p\nmid2j$, the local increment is
$\gcd(j,p-1)/(p(p^\delta-1))\ll_\delta\gcd(j,p-1)/p$.
The sum of these bounds is $O_\delta((1+\log\log(10Q))\tau(j))$ by precisely the divisor identity and progression reciprocal-prime estimate in [R90 §2](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers), here with $p\le B$ instead of $8M$; both cutoffs are polynomial in $Q$. This is $o(\log Q)$ uniformly for $j\le2V_Q$, by the arbitrary-fixed-power divisor bound. At $p\mid2j$, $T_j(p^e)\le2j$ and the geometric series gives logarithmic cost $O_\delta(\log(2j))$ per prime, hence $o(\log Q)$ in total. The product bound and the final subpower sum in $j$ prove (12).

Take $0<\delta<1/2$ sufficiently small relative to the target $\epsilon$. For nonempty $D_0\le B$, use (12) and $D_0^\delta\ll Q^\epsilon$ to get
$\sum_{D_0\le d\le B}H(d)/(\operatorname{rad}(d)\sqrt d)\ll Q^\epsilon D_0^{-1/2}$.
Square the numerator sum at fixed $b$ by Cauchy over at most $\tau(b)$ unitary divisors, bound $b^2\le B^2$, and enlarge only the positive upper sum to all $dm\le B$. Equations (11) and (12), and the $H(m)/m$ harmonic sum from [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers), give

$$
\sum_{b\le B} b^2
         \left(\sum_{\substack{d\mid b\\(d,b/d)=1}} L_{b,d}\right)^2
       \ll_{\Theta,C,\epsilon}
              Q^\epsilon B^2\frac{MD^{3/2}}{\sqrt{D_JD_0}} .
 \tag{13}
$$

All relaxations here occur in positive majorants. One may take smaller intermediate epsilons for the finitely many subpower factors.

Use [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) with the original common Taylor tests at each offset $\ell$. The original exterior unit phases and the exact numerator coefficients, of size at most $2^{-n}$ at Taylor order $n$, remain in the recovery. With the original factorial weights, $K_1=O(1+|\ell|)$ and the other seminorms have cost $O(S^{-1}+(1+|\ell|)^2/Q)$, as in [R101 §3](r101-operator-three-factor-equal-exponents.md#3-weighted-numerator-parseval-and-actual-aliases). Divide by $J\asymp Q$ and square-sum over $|\ell|\le R+1$ using (13), giving (3). At the example scales the arithmetic exponent is $791/800$; the three total exponents are $-3/400,-1/200,-3/500$, respectively. The earlier sharp comparison follows by the triangle inequality with all unchanged benchmark and restoration terms.

## 4. A live coefficient beyond the R101 cutoff

At the numerical choices take $d=2^e$ to be the least power of two at least $Q^{1/5}$, prime $m\in(B/(2d),B/d)$, and $k=r\asymp Q^{83/200}$ an odd prime. Bertrand's postulate supplies both primes for sufficiently large $Q$. Thus $b=dm$ is in the high band, $q=2r,\ r_b=r,\ h_q=2,\ s=2^{e+1}$ and $(2k,b)=2<G$. Also $k>K,\ d\ge D_0$. On $r$ take a generator-order character and its conjugate. On $m$ take a generator $\eta$ and $\eta'=\eta^{2V^*}$ with $V^*$ at least all the finitely many relevant fixed log-power ranges. All previous individual, product and signed mixed powers on $m$ are nonprincipal, because the corresponding exponents are nonzero and smaller than $m-1$ in absolute value. Thus the full product remains high from its $m$-component, the old joint alias and $m$ conductor is $rm\asymp Q^{121/200}>D_J$, and all individual alias powers have conductor $r>Q^{51/125}$, which also precludes the R97 joint cutoff.

At $s$, take the primitive sign-trivial $\gamma$ of order $2^{e-1}$ on $5$, and put

$$
\gamma'=\gamma^{-1+2^{e-1-t}},
                     \qquad t=\left\lfloor\tfrac1{20}\log_2 Q\right\rfloor .
$$

It is also primitive, and their product induces $\nu_d$ of conductor $2^{t+2}$ on $d$. Every previously allowed small shared-product power thus has conductor $Q^{.05-o(1)}>Q^{3/1000}$, surviving R98. For earlier positive unequal shared exponents $a,c$, the power exponent is $a-c+c2^{e-1-t}$ and has valuation $v_2(a-c)=O(\log\log Q)$. These powers have conductor $Q^{.20-o(1)}$, surviving R99. The earlier R100 three-factor products therefore have size $Q^{.805-o(1)}>Q^{.70}$. In R101 the products involving equal shared exponents have size $Q^{.655-o(1)}$, and those with unequal shared exponents have size $Q^{.805-o(1)}$. Both exceed $Q^{.6032}$, so R101 also retains the pair.

The local incidence is nonzero in the unmodified input: on $s$ the original congruence reduces modulo $2$, automatic for two odd units, and the primitive additive Gauss factors are nonzero at the unit frequencies. The conjugate pairing at $r$ and the primitive coprime Gauss factors at $m$ are also nonzero, as in [R101 §4](r101-operator-three-factor-equal-exponents.md#4-a-live-shared-equal-coefficient-retained-by-r100). Finally $(j,u,v,a)=(1,2,1,1)$ lies in the stated ranges for large $Q$ and gives conductor product $rm\,2^{t+2}\asymp Q^{.655}<Q^{.665}$ in (2). This establishes genuine strict new eligibility of a nonzero incidence coefficient, not a lower bound on the integrated packet field.
