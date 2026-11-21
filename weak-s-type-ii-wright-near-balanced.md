# A near-balanced pointwise Type II sector via neighboring-tile dispersion

**Conditional arithmetic result (global Dirichlet GRH).** Let $N$ be even and $L=\log N$, and keep the exact geometry of the [previous character-average deletion](weak-s-type-ii-character-average.md). Uniformly for $N^{.49999}\le t\le N^{.50001}$ and $N/2\le y\le9N/16$, the genuine raw contribution

$$
 \mathcal C=
 \sum_{\substack{uv+dk=N,\ N/2<uv\le y,\ (uv,N)=1\\
          v>N^{.2499},\ k>t,\ d>N^{.4975}\\
          N^{.5099}\le u\le N^{.5101}}}
       \mu(u)\mu(d)b_{\rm II}(v)\mu^2(dk),\qquad
 b_{\rm II}(v)=\sum_{j\mid v,\ j>N^{.2499}}\Lambda(j),
$$

is $O(N^{1-10^{-7}})$. The entire $u$ band can thus be removed from the residual of the previous mask $d\le N^{.4975},\,dv\le N^{.995}$: in this $u$ band, $d\le N^{.4975}$ already implies $dv\ll N^{.9876}<N^{.995}$. This is an estimate for one specified part of one central increment, not for the other balanced order, all Type II, or weak S.

The organization into neighboring tiles follows [Wright, arXiv:2608.27732v1, §2](https://arxiv.org/html/2608.27732v1#S2). We record his short-sum improvement from Theorem 2.1 in the estimates below, but the standard [Bettin–Chandee trilinear bound, Theorem 1](https://arxiv.org/pdf/1502.00769#page=2) on the same tiles already suffices for the stated narrow range. We do not apply Wright's Theorem 2.2, which requires $|a|\le MU$ with $M,U$ the dyadic starts; here $a=N$ can exceed $MU$ by a fixed factor. Instead we prove a restricted fixed-residue estimate (squarefree Möbius leg, global GRH, only the needed range). The key is to extend a nonnegative variance to all moduli *before* Poisson and use GRH on its zero-frequency part. This also retains the exact unit mask without requiring a second sieve in the shifted Kloosterman modulus.

## 1. The needed fixed-residue dispersion estimate

Use $N$ also as the size parameter, and let the fixed integer $a\ne0$ satisfy $|a|\le C N$ with $C$ fixed. Take

$$
 M\asymp N/U,\qquad \tfrac12N^{.5099}\le U\le N^{.5101},\qquad
 N^{.4974}\le Q\le N^{.5001}.
$$

Let $\alpha_m$ be any sequence of modulus at most $1$ on $[M,2M]$. Let

$$
 \beta_n=\mu(n)\mathbf1_{n\in I}\mathbf1_{(n,a)=1}(U/n)^{1+i\tau},
 \quad I\subset[U,2U]\ \text{an interval},\qquad |\tau|\le N^4 .
$$

Uniformly in these parameters, we prove

$$
 \sum_{\substack{Q\le q<2Q\\(q,a)=1}}
 \left|\sum_{mn\equiv a\pmod q}\alpha_m\beta_n\right|
 \ll N^{1-\kappa/3},\qquad \kappa=10^{-5}. \tag{1}
$$

Allow integer truncations at either endpoint of $I$. We use the global-GRH height-uniform twisted Möbius estimate explained in [the earlier character average, §2](weak-s-type-ii-character-average.md#2-exact-perron-separation-and-an-all-character-mean-square), with $|a|$ replacing $N$ in the finite Euler mask:

$$
 \left|\sum_n\beta_n\chi(n)\right|\ll_\epsilon N^\epsilon\sqrt U
 \quad(q\ll N,\ |\tau|\le N^4). \tag{2}
$$

In fact the Dirichlet series before the real $1/n$ weight is
$L(s+i\tau,\chi)^{-1}\prod_{p\mid a}(1-\chi(p)p^{-s-i\tau})^{-1}$.
The shift to $\Re s=1/2+\delta$ in Perron is pole-free, including for the principal character; the finite mask and imprimitive Euler factors cost $N^\epsilon$. The same bound therefore holds on every subinterval $I$, after scaling the weight $U/n$ by partial summation on the real factor only.

Take a nonnegative smooth function $\psi$, supported in $[1/2,5/2]$ and equal to $1$ on $[1,2]$, and write

$$
 B_{q,\delta}=\sum_{n\equiv\delta\ (q)}\beta_n,\qquad
 W=\sum_q\psi(q/Q)\sum_{\delta\bmod q}^{*}|B_{q,\delta}|^2
           \sum_{m\equiv a\bar\delta\ (q)}\psi(m/M).
$$

For good $q$ (those coprime to $a$), $m\bmod q\mapsto a\bar m\bmod q$ permutes the units. Bound $\alpha_m$ by 1 after triangle in $m$, then apply Cauchy over $(q,m)$ and majorize the original good-modulus variance by the displayed $W$, where the additional bad-modulus terms are nonnegative. Thus the left side of (1), squared, is at most $O(MQ\,W)$. The variance with all moduli is an auxiliary sum, not an assertion that the original congruence has unit solutions for bad moduli.

Expand $|B_{q,\delta}|^2$. It couples $n_1,n_2\sim U$ with $n_1\equiv n_2\bmod q$ and $(n_1n_2,q)=1$. Put $g=(n_1,n_2)$ and $G=N^\kappa$. The large-$g$ part, $g>G$, has absolute value

$$
 \ll_\epsilon N^\epsilon M\sum_{G<g\le2U}\frac Ug
          \left(1+\frac U{gQ}\right)
 \ll_\epsilon N^\epsilon\big(MU+MU^2/(QG)\big). \tag{3}
$$

Here for each $m,n_1$, $q\mid mn_1-a$ gives $O_\epsilon(N^\epsilon)$ choices, because $mn_1=O(N)$, $|a|\le CN$, and $mn_1-a\ne0$ on the support: $n_1>1$, and $(n_1,a)=1$. Since $(q,g)=1$, there are $O(1+U/(gQ))$ admissible $n_2/g$. Logarithms are absorbed into $\epsilon$.

For $g\le G$ use Poisson in $m$, with $|h|\le H=(Q/M)N^\kappa$; the discarded frequency tail is $O(N^{-100})$ uniformly in each progression sum, by Schwartz decay with sufficiently many integrations by parts. Restore all $g$ in the zero frequency: the absolute restoration error is bounded by (3), this time by first summing the dyadic $q$ with weight $M/q$ and counting $n_1,n_2$ for each $q$. The resulting zero frequency is

$$
 \widehat\psi(0)M\sum_q\frac{\psi(q/Q)}q\sum_{\delta\bmod q}^{*}|B_{q,\delta}|^2
 \ll_\epsilon N^\epsilon MU. \tag{4}
$$

Indeed the inner sum is $\phi(q)^{-1}\sum_{\chi\bmod q}|\sum_n\beta_n\chi(n)|^2$, bounded by $N^\epsilon U$ by (2), with $\epsilon$ relabeled.

For the remaining frequencies $h\ne0$, write $n_i=g\nu_i$. Möbius support implies $(g,\nu_i)=1$, and $(\nu_1,\nu_2)=1$. Since $g\le G<U$, the diagonal $n_1=n_2$ is absent. Now $\nu_1-\nu_2=qr$ with a signed integer $0<|r|\ll U/(gQ)$. Group $\nu_i$ by their classes modulo $g|r|$, the two classes agreeing modulo $|r|$. There are at most $g^2|r|$ pairs of classes. For fixed such classes, the integer $q=(\nu_1-\nu_2)/r$ has fixed residue modulo $g$; discard pairs not satisfying $(q,g)=1$. The other requirements $(q,\nu_i)=1$ follow from $(\nu_1,\nu_2)=1$ and $q\mid\nu_1-\nu_2$. Hence no unimplemented modulus restriction remains. By elementary reciprocity and CRT,

$$
 e\!\left(\frac{ah\overline{g\nu_1}}{q}\right)
 = e\!\left(\frac{ah}{g\nu_1q}\right)
   e\!\left(-\frac{ah\,\overline q\,\overline{\nu_1}}g\right)
   e\!\left(\frac{ahr\,\overline{g\nu_2}}{\nu_1}\right).
 \tag{5}
$$

Here $e(z)=e^{2\pi iz}$; the sign of $h$ can be chosen to match Poisson. The reciprocal modulo $1$ has the trivial phase $1$. In the last factor use $qr\equiv-\nu_2\bmod\nu_1$; the middle phase depends only on $h$ after $g,r$ and the two classes are fixed.

To apply Wright's Theorem 2.1, tile the two $\nu_i$-intervals by consecutive intervals of length $8Q|r|$. Only the same and a bounded number of neighboring tile pairs meet $|\nu_1-\nu_2|\le(5/2)Q|r|$. For each $g,r$, there are $O(U/(gQ|r|))$ such pairs and $O(gU/Q)$ combinations of tiles with residue classes. Summing over $r$ gives $O(U^2/Q^2)$ combinations per $g$. Each support has $O(1+Q/g)=O(Q)$ consecutive progression elements. The reciprocals in (5) are in the variables $g\nu_2\asymp U$ and $\nu_1\asymp U/g$; the former remains a progression after scaling, and the condition $(g\nu_2,\nu_1)=1$ is exactly the required Kloosterman coprimality. Existing $(g,\nu_i)=1$ and unit masks can be left in each individual coefficient (by zeroing terms). If necessary split any endpoints so each lies in a single applicable dyad.

The smooth factor after extracting $M/Q$ is

$$
 \frac{Q}{q}\psi(q/Q)\widehat\psi(hM/q)\,
 e\!\left(\frac{ah}{g\nu_1q}\right).
$$

It can be extended by zero near $q=0$. On any fixed $h$-dyad of length scale $H_0\le H$ (and fixed sign), and the two tiles, the mixed derivatives of order at most one in each variable are $O_C(N^{10\kappa})$ after rescaling the $\nu_i$ variables by $Q|r|$ and $h$ by $H_0$. Indeed $g\nu_1\asymp U$, $gQ|r|\ll U$, $q\asymp Q$ on the support, and $|a|H/(UQ)\ll_C N^\kappa$, $HM/Q=N^\kappa$; the product rule uses at most three derivatives. Three-variable partial summation therefore costs at most $O_C(N^{10\kappa})$ and simply truncates the progression supports to subintervals.

With $\vartheta=ar$ the prefactor in Wright is bounded by $O_C(N^\kappa)$, since $|a||r|H/((U/g)U)\ll_C N^\kappa$. The ratio of support cardinality to the smaller dyadic start is $O(gQ/U)$. Throughout the given range this is $O(N^{-.0097})$. In the theorem we can take $\eta=.009$: even with its scale parameter $X_1=(U/g)U\le O(N^{1.021})$, $O(gQ/U)\ll X_1^{-\eta}$ and $X_1^{-2\eta/5}\ll N^{-.0036}$ since $X_1\gg N$. The product of coefficient norms in each tile and $h$-dyad is $O(Q\sqrt{H_0})$. Bounding both ambient starts by $O(U)$, the conclusion per tile and residue pair (before counting and $M/Q$) is

$$
 \ll_\epsilon N^{11\kappa+\epsilon}\,
 Q\bigl(H_0 U^{7/8}+H_0^{17/20}U^{19/20}N^{-.0036}\bigr).
$$

Sum over dyads of $h$, $g\le G$, and tile/class combinations, and substitute $H=(Q/M)N^\kappa$. A conservative resulting bound for the nonzero frequency part is

$$
 \ll_\epsilon N^{30\kappa+\epsilon}
 \left[Q^{-1}U^{23/8}
       + M^{3/20}U^{59/20}Q^{-23/20}N^{-.0036}\right]. \tag{6}
$$

This reassembly gains from the *neighboring* tiles compelled by $\nu_1-\nu_2=qr$, not from applying a short-interval theorem independently to all short tiles of the original Type II box.

Multiplying (3), (4), and (6) by $MQ$, write $U=N^{p+o(1)}$, $M\asymp N/U$, $Q=N^z$. The first large-gcd term and (4) have squared-bound exponent at most $2-.5099+.5001=1.9902$ before $\epsilon+o(1)$, and the second term of (3) has exponent $2-\kappa+\epsilon+o(1)$. The two terms of (6), before the common $30\kappa+\epsilon+o(1)$, have squared-bound exponents at most

$$
 1+(15/8)\cdot.5101 <1.957,\qquad
 23/20+(9/5)\cdot.5101-(3/20)\cdot.4974-.0036 <1.991.
$$

The specialized short-support factor $N^{-.0036}$ is not needed for this numerical band. Applying Bettin–Chandee's Theorem 1 on exactly the same progression tiles, with coefficients set to zero off their stated supports, gives the two pre-reassembly terms $Q H_0 U^{7/8}$ and $QH_0^{17/20}U^{19/20}$, up to the same $N^{11\kappa+\epsilon}$ factor. Thus (6) holds also without $N^{-.0036}$; the second squared-bound exponent then is at most $1.99357+30\kappa+\epsilon+o(1)$, still below $2-2\kappa/3$. This fallback still uses the neighboring-tile organization, not the trilinear estimate on an unrestricted large box.

Choose $\epsilon>0$ sufficiently smaller than $\kappa$. All terms are $O(N^{2-2\kappa/3})$, proving (1). The only size uses of $a$ were the divisor bound for the nonzero $mn_1-a$, and (5) with the displayed smooth and trilinear prefactors. Consequently $|a|\le CN$ is genuine uniformity, not a citation of Theorem 2.2 beyond its statement.

## 2. Square completion and every moving threshold

Complete $\mu^2(m)=\sum_{b^2\mid m}\mu(b)$, $m=N-uv$, and truncate at $B=N^{10^{-6}}$. The number of $m\le N$ divisible by any $b^2$, $b>B$, is $O(N/B)$. The absolute combined summand for each such $m$ is at most $L\tau(N-m)\tau(m)^2\ll_\epsilon N^\epsilon$. The truncation therefore costs $O_\epsilon(N^{1+\epsilon}/B)$. Squarefree $d$ comes from $\mu(d)$. For fixed $b\le B$ and $g_0=(b,d)$, put $q=[b^2,d]=b^2d/g_0$, an injective function of $d$ in this group. If $q$ is not coprime to $N$, there is no unit solution; otherwise the exact two divisibilities become $uv\equiv N\pmod q$. Since $d>N^{.4975}$ and $d<(N/2)/t\le\tfrac12N^{.50001}$, all these $q$ lie in dyads of (1), retaining only those actually arising from $d$.

Use dyads $u\sim U$, $v\sim M$ with $M\asymp N/U$ on all occupied boxes. For each $d$ set

$$
 A_0=N/2+1/2,\qquad
 A_1(d)=\min\{\lfloor y\rfloor+1/2,\ \lceil N-td\rceil-1/2\}.
$$

Omit the box for this $d$ if $A_1(d)\le A_0$. For integer $uv$, the exact cutoff is $A_0<uv<A_1(d)$, with both cutoffs separated by at least $1/2$ from every integer. Use height $N^4$ Perron for each endpoint on $\Re s=1$ with pointwise error $O(N^{-3})$. The number of raw candidate tuples $(b,d,u,v)$ in these dyads is $O(BN^2L^2)$, so these endpoint errors, even with weight $L$, are negligible.

For each $\tau$ use $\beta_u$ in (1) with $a=N$ and the true $u$ subinterval, and

$$
 \alpha_v=\mathbf1_{v>N^{.2499}}\mathbf1_{(v,N)=1}
                \frac{b_{\rm II}(v)}L (M/v)^{1+i\tau}.
$$

The remaining per-$d$ factors $\mu(d)$, the possible omission, and $[ (A_1(d)/(MU))^{1+i\tau}-(A_0/(MU))^{1+i\tau} ]/(1+i\tau)$ have absolute combined size $O((1+|\tau|)^{-1})$ as $A_i(d),MU\asymp N$. Thus for each $\tau$ apply (1) to the sum over all good moduli in the dyad, dominating the exact subfamily using injectivity. The $L$ from normalization and $O(L)$ from its absolute integral, the number of dyads, and the $\tau(b)$ possible $g_0\mid b$ cost $O_\epsilon(N^\epsilon)$ after $\sum_{b\le B}\tau(b)\ll B\log(2B)$. The bound on the retained terms is therefore $O_\epsilon(BN^{1-\kappa/3+\epsilon})$. Together with the square tail this is $O(N^{1-10^{-7}})$ with a sufficiently small fixed $\epsilon$, uniformly in $t,y$.

For a strict new-region witness, let $X\to\infty$ and choose distinct odd primes $u,v,d,k$ in sufficiently short fixed relative intervals about $X^{.51}, .53X^{.49}, .45\sqrt X, (.47/.45)\sqrt X$. The prime number theorem gives such choices. Then $N=uv+dk$ is even, $uv/N$ is close to $.53$, $(uv,N)=1$, and $k>\sqrt N$. With $t=\sqrt N$, $y=9N/16$, both exact new ranges hold; $d>N^{.4975}$ puts the term in the previous residual. Its original coefficient is $\log v>0$. This only certifies an actually occupied sector; it is not an assertion of aggregate noncancellation or any conclusion on the full operator.
