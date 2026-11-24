# Parity compensation in the critical-prime shell

Fix a sufficiently large even $N$, write $X=\sqrt N$, $L=\log N$, and use the genuine Type II coefficients of [the critical-prime setup](weak-s-type-ii-critical-prime-least-prime-boundaries.md). Thus $P_n=-E(u,v)\log v$ at $n=uv$ with true primes in the original disjoint boxes for $u,v$, true hard cuts $N/2<uv\le y\le9N/16$, and $(uv,N)=1$. The full coefficient $D_m$ includes every original splitting $m=dk$ with $d\in I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le m<N/2$, $(dk,N)=1$, and $(d,k)=1$, weighted by $\mu(d)\mu^2(k)$. Allow $F_m=\rho_mD_m$ with $|\rho_m|\le1$ fixed at the target independently of the sampled arc. The unmasked case is $F=D$. Set

$$
\begin{aligned}
\mathcal Q&=[.8X,.9X]\cap\mathbb P,\qquad
\mathcal B=[-1/(10N),1/(10N)],\\
A(h)&=\operatorname{sinc}\big(h/(5N)\big)\sum_{n+m=N+h}P_n F_m,\qquad
\operatorname{sinc}(z)=\frac{\sin(\pi z)}{\pi z},\\
Z_N&=\frac{|\mathcal Q|}{5N}\sum_h A(h),\qquad
\mathcal H_N=\{0<|h|<N/20:\exists q\in\mathcal Q,\ q\mid h\}.
\end{aligned}
$$

At zero the sinc is interpreted continuously. The two genuine $N$-unit masks give odd $n,m$, hence $A(h)=0$ on odd $h$. The physical boxes give $|h|\le .037N$ on the support. Each $h\in\mathcal H_N$ has a unique associated $q=q(h)$, since two distinct critical primes have product at least $.64N$.

The following statements distinguish the signed pairing from a possible estimate using squared moments.

1. **Genuine signed part, pointwise for all even $N$.** If $E(u,v)=E_1(u)E_2(v)$ with $|E_i|\le1$, including $E=1$, the signed contribution of all odd-start blocks in the literal $q$-block compensation is $-Z_N/2+O(N/\sqrt L)$, uniformly in all original moving hard cuts and even when the prime product gate is active. This applies to the full unmasked complementary coefficient. In particular it computes a dense signed piece, without assuming that $Z_N$ is small.
2. **Squared-moment obstruction for the literal blocks.** For all sufficiently large $N=2^j$, the very same genuinely prime $E=1$ construction and sign-preserving product mask of [the masked hit-moment obstruction](weak-s-type-ii-critical-prime-masked-hit-moment-barrier.md) can make $F$ polynomially small at the central interval while its literal block-compensated moment is $\gg_A N^3/(K^6L^{17})$, where $K=\lceil C_A L/\log L\rceil$ for any fixed $A>0$.
3. **Even-lattice blocks are not enough for a uniform squared estimate.** With the same genuine original hard cuts and complete $D_m$, there also exist separated $0/1$ prime selectors and true sign-preserving product masks at every sufficiently large $N=2^j$ giving the same polynomially small central transform but even-lattice compensated moment $\gg_A N^{5/2}/(K^6L^{16})$. This witness does not use odd offsets. It has a different prime selector from part 2 and need not have the raw-hit lower bound there.

All statements are unconditional. Neither lower bound is for the original unmasked $F=D$ or for the sum of the signed block discrepancies. Part 1 does not estimate the signed even-hit remainder.

## 1. Exact compensation and a signed estimate on its odd blocks

Define the two block choices at odd $q\in\mathcal Q$ by

$$
 B_q(j)=A(qj)-\frac1q\sum_{r=0}^{q-1} A(qj+r),
 \qquad
 B_q^{\rm ev}(j)=A(2qj)-\frac1q\sum_{r=0}^{q-1} A(2qj+2r).
$$

Their signed sums over $j\in\mathbb Z$ are exactly the same at each $q$. For the first formula the blocks partition $\mathbb Z$; for the second the blocks partition $2\mathbb Z$, and $q\mid h$ on even $h$ is equivalent to $2q\mid h$. In particular, integrating over all original nonzero numerators and $\mathcal B$, the exact full pairing is

$$
 \mathcal I_N=\frac1{5N}\sum_{q\in\mathcal Q}q\sum_j B_q(j)
             =\frac1{5N}\sum_{q\in\mathcal Q}q\sum_j B_q^{\rm ev}(j).
 \tag{1}
$$

This uses the exact Ramanujan kernel $q\mathbf1_{q\mid h}-1$ and the exact integral $\int_{\mathcal B}e(\beta h)\,d\beta=(5N)^{-1}\operatorname{sinc}(h/(5N))$, with $e(x)=\exp(2\pi i x)$. The $j=0$ contribution is always $O(N/L)$ in either formula, by $\|P\|_2,\|F\|_2\ll\sqrt N$ for the coefficient $\ell^2$ norms, Cauchy for each convolution value, and $\sum_{q\in\mathcal Q}q\ll N/L$. The prime norm follows by unique factorization and the prime counts, and the complementary norm is the [sharp ordinary energy bound](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy). All nonzero active starts in (1) lie in $\mathcal H_N$, since the blocks extend by at most $2q$ beyond the physical support. Thus each corresponding block-square sum $o(N^2L)$ would suffice for $\mathcal I_N=o(N)$ by Cauchy and $|\mathcal H_N|\ll N/L$.

Let

$$
 \mathcal O_N=\frac1{5N}\sum_{q\in\mathcal Q}q\sum_{j\ {\rm odd}} B_q(j).
$$

Here the point evaluations vanish. For $h=2z$ the periodic indicator of an odd floor $\lfloor h/q\rfloor$ is exactly

$$
 W_q(z)=\mathbf1_{\{(q+1)/2,\dots,q-1\}}(z\bmod q).
$$

Strictly, the result holds for any functions $W_q:\mathbb Z/q\to\mathbb C$ of normalized mean square at most one: writing $\nu_q=q^{-1}\sum_z W_q(z)$, we prove

$$
 \frac1{5N}\sum_{q\in\mathcal Q}
 \left|\sum_{h\ {\rm even}} A(h)\big(W_q(h/2)-\nu_q\big)\right|
 \ll \frac{N}{\sqrt L}.
 \tag{2}
$$

Write $W_q(z)=\sum_{|a|\le(q-1)/2} c_q(a)e(az/q)$; finite Parseval gives $\sum_a|c_q(a)|^2\le1$. For $a\ne0$, the exact Fourier expression for one inner sum after its $1/(5N)$ factor uses the integrals

$$
 \int_{\mathcal B}P(a/(2q)+\beta)F(a/(2q)+\beta)
      e\big(-N(a/(2q)+\beta)\big)\,d\beta,
 \tag{3}
$$

where $P(\alpha)=\sum_n P_ne(n\alpha)$ and $F(\alpha)=\sum_m F_me(m\alpha)$. The rational centers $a/(2q)$ in this range are distinct modulo one: distinct primes require any cross-equality to have $q\mid a$, and none has $a=0$. Distances on the torus are at least $1/(2qq')$ across distinct $q,q'$ and $1/(2q)$ for the same $q$. These exceed $2/(10N)$, so all translated intervals in (3) are disjoint.

Uniformly at every center of (3) and every $\beta\in\mathcal B$ the true separated prime polynomial satisfies

$$
 |P(a/(2q)+\beta)|\ll X^{3/2}.
 \tag{4}
$$

Here is a proof retaining an active hard product gate. The sampling grids used are $r/Q$ for $Q=q$ when $a$ is even, and $Q=2q$ when $a$ is odd. The multiplier of $u/Q$ in the center is coprime to $Q$ in either case. Both $u,v$ are smaller than $q$, so each supported $u$ has a distinct sampling node. For any complex weights $b_v$ supported on $1\le v<Q$, let $G_\ell(x)=\sum_{v\le\ell} b_v e(vx)$. The continuous $L^2$ maximal Fourier bound (for instance [Oberlin–Seeger–Tao–Thiele–Wright, Theorem 1.1 with $p=2$ and $r>2$](https://arxiv.org/pdf/0910.1555v2#page=2)) gives

$$
 \int_{\mathbb T}\sup_\ell |G_\ell(x)|^2\,dx\ll\sum_v|b_v|^2,\qquad
 \int_{\mathbb T}\sup_\ell |G'_\ell(x)|^2\,dx\ll Q^2\sum_v|b_v|^2.
$$

For the derivative use the same theorem on coefficients $2\pi i v b_v$. On a length-$1/Q$ cell $I_r$ centered at $r/Q$, the fundamental theorem of calculus and Cauchy give

$$
 \sup_\ell|G_\ell(r/Q)|^2\le
   2Q\int_{I_r}\sup_\ell|G_\ell(x)|^2\,dx
      +\frac2Q\int_{I_r}\sup_\ell|G'_\ell(x)|^2\,dx.
$$

Sum over disjoint cell interiors to bound the discrete maximal sample square sum by $O(Q\sum|b_v|^2)$. At fixed $u$ the genuinely allowed $v$ form a single interval inside their hard interval and the two product walls; thus a difference of at most two such prefixes suffices. Leave all prime and $N$-unit masks in the separated coefficient weights. Expand $e(\beta uv)=\sum_{s\ge0}(2\pi i\beta N)^s(u/X)^s(v/X)^s/s!$. At each $s$, the $u$ and $v$ weights have $\ell^2$ norms $O((X/L)^{1/2})$ and $O((XL)^{1/2})$, respectively. Apply Cauchy over the supported $u$ and the discrete maximal bound to the $v$ polynomial. This gives $O(\sqrt Q X)$ for each unscaled tensor term, uniformly in $s$. Since $|\beta N|\le1/10$, the Taylor coefficients are absolutely summable with bounded sum, proving (4). If the prime product gate is inactive, the discrete maximal bound can be replaced by elementary complete additive orthogonality.

Cauchy for (3), with $|c_q(a)|$ on the $P$ side, gives (2): the weighted $P$ energy is $\ll |\mathcal B||\mathcal Q|X^3\ll N/L$ by (4), and the unweighted $F$ energy is $\ll N$ by disjoint arcs and ordinary Parseval. No squared-moment estimate in offset space is used. For the odd-start selector, $\nu_q=(q-1)/(2q)$. Since $\sum_q q^{-1}\ll1/L$ and $\sum_h|A(h)|\le\sum_n|P_n|\sum_m|F_m|\ll N^2/L$, the constant part differs from $-Z_N/2$ by $O(N/L^2)$. This proves part 1. In (1) the signed even-start part is therefore the unrestricted hit minus half the same exact base, up to the error in (2); no claim is made that the natural zero-numerator base is itself negligible.

## 2. Literal block moments with the original unselected prime intervals

Fix the test of the masked hit-moment obstruction, at $N=2^j$ with $I_d=[X,.100N^{.50001}]$, $t=N^{.49999}$, $y=9N/16$, the two genuine short hard prime intervals and $E=1$. That construction gives $K+2$ physical sign bins of length and gap $\asymp N/K$, with all shifted supports pairwise separated by $\gg N/K$. It gives a real product multiplier $0\le\rho_m\le1$ with $\sum_m m^rF_m=0$ for $0\le r\le K$ and $\sup_{\beta\in\mathcal B}|F(\beta)|\ll_A N^{-A}$. One selected bin has signed weights all of one sign and absolute mass $B\gg N/(K L^7)$. Put $a_n=|P_n|$, $b_m=|F_m|\mathbf1_{m\ {\rm in\ this\ bin}}$ and $A_0=\sum_n a_n\asymp N/(K^2L)$. Their coefficient square sums are $O(N)$.

For each $q$ put

$$
 J_q=\sum_{n,m}a_n b_m\,W_q((n+m-N)/2)
$$

with the odd-block $W_q$ above. In this incidence calculation there is no $\beta$ modulation. Ordinary additive large sieve on the same distinct centers $a/(2q)$ and Cauchy give

$$
 \sum_{q\in\mathcal Q}|J_q-\nu_q A_0 B|\ll N^2.
 \tag{5}
$$

Indeed each Fourier expansion for $J_q$ has coefficient $c_q(a)$ of modulus at most one, a unit phase, and the two transforms of $a_n,b_m$ at $a/(2q)$. The center spacing is $\gg1/N$ and both supports are of length $O(N)$, so each of their summed sample energies is $O(N^2)$. This step is the same additive-large-sieve input as [the uncentered incidence calculation](weak-s-type-ii-critical-prime-fixed-selector-logarithmic-barrier.md#1-genuine-weights-with-one-sign-and-a-modulus-with-enough-matches). By (5), all but $O(K^3L^8)$ primes have $J_q\gg A_0B$, and this exceptional count is $o(|\mathcal Q|)$.

For each such $q$, every odd-start block meeting the winning bin's shifted support meets no other shifted bin, because its length $q$ is much smaller than the gaps. Its point evaluation is zero by parity. All its nonzero $A(h)$ are of one sign, and the sinc is positive and bounded below on physical support. Consequently its block absolute discrepancies, summed over these odd-start blocks, total at least a constant times $A_0B/q$. There are $O(X)$ such blocks per prime, so their squared discrepancies sum to $\gg (A_0B)^2/(q^2 X)$. Each corresponding start $qj$ is odd, nonzero, and belongs to $\mathcal H_N$. By uniqueness the starts from different $q$ do not overlap. Summing over $\gg X/L$ primes yields

$$
 \sum_{h\in\mathcal H_N}\left|B_{q(h)}(h/q(h))\right|^2
       \gg_A \frac{N^3}{K^6L^{17}} .
 \tag{6}
$$

This construction uses the *same* unselected prime leg and permissible complementary mask as the raw hit lower bound. Its proof for (6) deliberately uses offsets at which the raw hit is zero, not the incidence lower for actual hit values. Moreover (2) and the central smallness show that the total signed odd contribution in this witness is $O(N/\sqrt L)$, despite (6).

## 3. A separated obstruction on the even lattice

To ensure the method limitation is not confined to odd starts, keep all the original $D_m$ cuts in §2 but place the $K+2$ sign bins in $[.450N,.460N]$ (same orders of length and gaps), and take the same type of narrow true prime intervals. As in [§1 of the masked hit-moment obstruction](weak-s-type-ii-critical-prime-masked-hit-moment-barrier.md#1-each-small-physical-bin-has-both-signs-on-the-true-carrier), the variance and signed hard-interval mean are uniform for these choices. In each bin preselect the sign $(-1)^i$ and let $b^{(i)}_m=|D_m|$ on precisely that sign within the bin, zero elsewhere, with total mass $B_i\gg N/(KL^7)$.

For almost every critical $q$, in every bin both quadratic classes of $N-m$ carry a fixed positive proportion of $B_i$. To prove this, let $\chi_q$ be the Legendre character, with zero at multiples of $q$. The integer $N-m$ on these supports is odd and in $[.540N,.550N]$, so write it uniquely as $r s^2$ with $r$ odd and squarefree. Then $s\le\sqrt{.550}\,X<q$ and $\chi_q(N-m)=\chi_q(r)$ including the zero values. For a fixed bin write $c_r$ for the sum of its $b^{(i)}_m$ over all $s$ giving that $r$. The divisor bound $|D_m|\le\tau(m)\ll_\eta N^\eta$ gives

$$
 |c_r|\ll_\eta N^\eta \sqrt{N/r},\qquad
 \sum_r|c_r|^2\ll_\eta N^{1+2\eta}L .
$$

By [Heath-Brown, Theorem 1, p. 237](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/72/3/108575/a-mean-value-estimate-for-real-character-sums), the real-character large sieve over odd squarefree numerators and denominators gives

$$
 \sum_{q\in\mathcal Q}\left|\sum_m b^{(i)}_m\chi_q(N-m)\right|^2
       \ll_\eta (XN)^\eta(X+N)N^{1+2\eta}L.
$$

Hence, choosing a fixed small $\eta>0$, the number of primes failing $|\sum_m b^{(i)}_m\chi_q(N-m)|\le B_i/4$ for some bin is $\ll_\eta N^{4\eta}K^3L^{15}=o(X/L)$. Here the implied bound uses the displayed $B_i$ lower; a possible factor $L$ has been retained. The mass in each of $q\mid m$ and $q\mid N-m$ is $O_\eta(N^{1/2+\eta})$ by the uniform number of integers in a residue and the same divisor bound. Both are negligible relative to $B_i$. Thus choose one prime $q_0$ good for all bins.

Among the true primes in the first narrow interval choose the majority Legendre class $\lambda_u\in\{\pm1\}$ by count, and in the second choose its majority class $\lambda_v$ by the weight $\log v$. All these primes are below $q_0$. The separated selector

$$
 E(u,v)=\mathbf1_{\chi_{q_0}(u)=\lambda_u}\mathbf1_{\chi_{q_0}(v)=\lambda_v}
$$

retains a constant fraction of the original prime mass, $A_1\gg N/(K^2L)$, and makes $\chi_{q_0}(n)=\lambda_u\lambda_v$ throughout. In each sign bin retain only its $b^{(i)}_m$ with $q_0\nmid m$ and $\chi_{q_0}(N-m)=-\lambda_u\lambda_v$. The preceding class bound leaves each mass $\gg N/(KL^7)$. Apply the exact alternating-cofactor moment construction of [§2 of the masked hit-moment obstruction](weak-s-type-ii-critical-prime-masked-hit-moment-barrier.md); it uses only the ordered positive supports in their prescribed signs. This gives $F_m=\rho_m D_m$ with $0\le\rho_m\le1$, the same moment equations and central bound, and a winning bin with $B_1=\sum_{\rm winning\ bin}|F_m|\gg N/(KL^7)$. All choices are fixed once at the target and used for the entire shell, not re-selected on each arc.

The genuine pair congruence $n+m\equiv N\bmod q_0$ is now impossible by the two opposing character classes. Thus every $A(2q_0j)$ vanishes; this still holds if the hits require $q_0\nmid m$, which was retained. Actual even offsets in the winning bin fall in the even-lattice blocks, with no other bin in a common block by the physical gaps. They are bounded away from zero, since here $n/N\le .5364$ and $m/N\le .460$. The sum of the absolute block averages on these blocks is $\gg A_1 B_1/q_0$, because they partition the even offsets and the sinc is uniformly positive. Cauchy over $O(X)$ blocks proves

$$
 \sum_{\substack{h\in\mathcal H_N\\h\ {\rm even}}}
  \left| B_{q(h)}^{\rm ev}\big(h/(2q(h))\big)\right|^2
       \gg_A \frac{(A_1B_1)^2}{q_0^2 X}
       \gg_A \frac{N^{5/2}}{K^6L^{16}}.
 \tag{7}
$$

The first lower bound in (7) comes from $q_0$ alone, and all its block centers are nonzero within the actual offset range allowed for $\mathcal H_N$. Later and earlier sign bins may cancel in the signed sum (1); indeed at $q_0$ the signed sum reduces to a central term which is small by construction. This rules out the uniform Cauchy criterion even on the even lattice using the stated wider class of selected genuine coefficients, not on the fixed original unmasked statistic. Neither (6) nor (7) precludes proving signed cancellation of the true remaining even-lattice blocks with the original $E=1$ and $F=D$.
