# Joint alias powers and the shared-prime product

The high full product can coexist with a principal shared-prime component. This gives a further sector of the genuine signed packet, different from the coprime partial-product sectors. Conditioning on the full product costs a local Gauss factor, but the literal alias count absorbs it after averaging the joint conductor bound over the shared characters.

## 1. Actual sector and estimate

Use the field $Z_{\rm signed}$ retained by [R96](r96-operator-equal-and-signed-joint-powers.md#1-exact-enlargement-and-packet-bound). Keep its exact even shell, true transported profiles $h,f$, common taper, original $J^{-1}$, and high-denominator packet $\mathcal C_+(B,R)$. Assume the original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$, exactly as in R96. Keep $k>K\ge A/Q$, $(2k,b)<G$, $z,w>A$, and all earlier selections and signs. Either parity version of R96 is allowed, with or without the two exact parity removals and with $K\ge2P$ in the former case.

For $q=2k,\ q'=qb$, write

$$
b=dm,\qquad d=b_\parallel,\quad m=b_\perp,\quad q'=r_b m s ,
 \tag{1}
$$

as in R96 (1). Thus $d$ is the full part of $b$ on primes dividing $q$, while $r_b$ is the full part of $q$ coprime to $b$; $s$ consists of the shared prime powers of $q'$. The three factors $r_b,m,s$ are pairwise coprime. Write $\nu\bmod b$ for the actual full product character, with components $\nu_d\bmod d$ and $\rho\bmod m$, and $\alpha\bmod r_b$ for the first individual alias component. The original product forcing gives conjugate individual alias components $\alpha,\bar\alpha$ on the two legs.

Let $C>0,\ D,D_0\ge1$, and $V_Q=\lfloor(\log Q)^C\rfloor$. Only on aliases with $d\ge D_0$, remove from $Z_{\rm signed}$ every remaining pair satisfying

$$
\operatorname{cond}(\alpha^j)\,
       \operatorname{cond}(\nu_d^u)\le D
       \quad\text{for some integers }1\le j,u\le V_Q .
 \tag{2}
$$

Here conductors are of primitive inducing characters, with conductor one for the trivial factor. The location in (2) matters: the product component is $\nu_d$, not the coprime component $\rho$ used by the R96 equal-exponent branch, and not the full product $\nu$ used by R91. The earlier full product masks and all earlier leg cuts remain unchanged. Denote the resulting genuine field, with this selection before detuning, by $Z_{\rm sh}$. With the same packet norm as R96 and $R_*=1+R$,

$$
\|Z_{\rm signed}-Z_{\rm sh}\|_{\rm pkt}
 \ll_{\Gamma,\Theta,C,\epsilon}
        Q^\epsilon B^{3/2}\sqrt{MD/D_0}
       \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+
                                  \frac{R_*^{1/2}}S\right].
 \tag{3}
$$

The bound holds after a fixed orthogonal spatial compression or restriction to a subset of the given packet. The deletion may also be restricted to any subset of the eligible aliases fixed by $k,b$.

At the established $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, choose $D_0=Q^{49/250}$ and $D=Q^{51/125}$. Then (3) is $O_{\epsilon,C}(Q^{-11/4000+\epsilon})$ and the inherited post-parity sharp $\widehat T,\widehat P$ comparison remains $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm sh}$. This is a bound on the deleted sector with the shared-part gate, not on the surviving covariance, other packets, a single even modulus, or weak S.

## 2. Fixed full product and exact common-test cost

At fixed $q,b,\nu$, the exact residue incidence forces the unique second character $\xi'=(\nu\circ\pi)\bar\xi$, where $\pi$ reduces units modulo $q'$ to units modulo $b$, as in R93 §3. Thus on $r_b$ the two legs are conjugate, and on $m$ they have components $\eta,\rho\bar\eta$. For this full product, the earlier R94–R96 complements are fixed subsets on the first-leg components $(\alpha,\eta)$ and invariant under the involution $(\alpha,\eta)\mapsto(\bar\alpha,\rho\bar\eta)$. The earlier individual cuts remain fixed leg projections. The new selection (2) at fixed $\nu_d$ depends only on $\alpha$ and is invariant under $\alpha\mapsto\bar\alpha$, since primitive conductors are invariant under conjugation. Thus all these exact pair tests are implemented by the same projected genuine vector on both raw legs at fixed $\nu$, with the optional auxiliary parity projections acting as in the original sharp parity terms. The original high full-product masks merely keep or omit this full coefficient. They are not replaced by a condition only on $\nu_d$.

Write $r=r_b$, and let $g_{\nu_d}(r,d)$ be the fraction of all $\alpha\bmod r$ satisfying (2) at fixed $\nu_d$, with $g_{\nu_d}\in[0,1]$. Count freely the two remaining CRT factors of the progression character in (1). The actual vector uses at most $\phi(q')g_{\nu_d}(r,d)$ coefficients, since the old cuts only shrink its support. Normalized residue Parseval and the same uniform per-character Dirichlet GRH estimates give the genuine squared pointwise and increment bounds

$$
\begin{split}
  \|F_\nu(z)\|_2^2 &\ll_\epsilon Q^\epsilon g_{\nu_d}(r,d)\,z,\\
  \int_X^{2X}\|F_\nu(z+h)-F_\nu(z)\|_2^2\,dz
       &\ll_\epsilon Q^\epsilon g_{\nu_d}(r,d)\,X|h|,
               \qquad 1\le |h|\le X/4 .
 \end{split}
 \tag{4}
$$

Here $X$ ranges over the true polynomial raw scales, and the individual increment input is [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference). The common vector and projection may depend on the fixed full product but do not depend on the raw variables, parameters of the common test, or the numerator.

For any complex unit residue vectors $U,V$, the coefficient at one full product $\nu$ defines the bilinear form $\mathscr C_\nu(U,V)$ of [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms), bounded by

$$
|\mathscr C_\nu(U,V)|\ll_\epsilon
      Q^\epsilon\sqrt{\mathfrak e(q,b)}\,\|U\|_2\|V\|_2,
              \qquad \mathfrak e(q,b)=d/(q,d).
 \tag{5}
$$

This is the fixed-full-product bound after both normalized residue expansions. The local shared-prime Fourier support entering R93 (6) leaves $p^{(v_p(b)-\min(v_p(q),v_p(b)))/2}$ at a common prime $p$. Thus (5) permits arbitrary prime powers without an excess cutoff. It also applies to the raw-line Fourier transforms of the same projected vectors. In this step one cannot simply use the R94 $\ell^2(a_d)$ partial-product coefficient bound with a single vector, since the new vector can vary with $\nu_d$.

In the difference orientations, transpose at fixed full product multiplies $\mathscr C_\nu$ by $\nu(-1)$, as follows from the exact reflection of the reduced numerators in R93 §3. The projection to the same vector on each raw side preserves this symmetry or skew symmetry. Use the common-test proof of R93 §4 at this product and insert (4) and (5). The original cosine marginal identity uses the same projected vector on its two legs; the skew part uses the same vector with its common raw interval restriction before applying the raw Fourier bound. The two pointwise factors and the squared increment factor both contribute $g_{\nu_d}$. The sum orientation keeps its original sign. For the optional exact parity removals, use the two reflected derivative estimates exactly as in R93, not a marginal identity applied to their sharp raw masks. The fixed character projections commute with the auxiliary parity operators, so the numerator equality for the reflected incidence holds on the relevant even leg, and the original overlap convention is unaffected.

More explicitly, the complete fixed-$\nu,k,b$ common-test HS bound is

$$
O_\epsilon\!\left(Q^\epsilon\sqrt{\mathfrak e(q,b)}\,
                         g_{\nu_d}(r,d)\mathcal K\right),
 \tag{6}
$$

where $\mathcal K=K_1+QK'_2$ with the test seminorms of R94 §4, enlarged by $Q(E_\infty+E_1)$ for the parity-reduced input because its extra cost has $QP/k$ and $P/k\le1/2$. This is a fixed common test, not yet the distinct detunings. Parseval on the full reduced numerator group, with counting measure, gives the joint numerator cost by multiplying the $\ell^2$ norm of (6) over all $\nu$ by $\sqrt{\phi(b)}$. Define

$$
g(r,d)=\phi(d)^{-1}\sum_{\nu_d\bmod d}g_{\nu_d}(r,d).
$$

For an upper bound permit every $\rho\bmod m$, and use $g_{\nu_d}^2\le g_{\nu_d}$. Then the square of the arithmetic factor from (6), before the seminorm, is bounded by

$$
O_\epsilon\!\left(Q^\epsilon\mathfrak e(q,b)\phi(b)
       \phi(m)\sum_{\nu_d\bmod d}g_{\nu_d}(r,d)^2\right)
       \ \ll_\epsilon\ Q^\epsilon b^2\mathfrak e(q,b)g(r,d).
 \tag{7}
$$

The full product tests only decrease this bound. Thus the joint numerator cost per actual alias is at most $Q^\epsilon b\sqrt{\mathfrak e(q,b)g(r,d)}\mathcal K$ up to the stated fixed-parameter constants. Importantly, no uniform small-support bound over $\nu_d$ has been used.

## 3. Weighted alias summation

For any positive integer $h$ write $T_h(n)=|\ker(\chi\mapsto\chi^h)|$ on the character group of $n$, with $T_h(1)=1$, and $H(n)=\sum_{1\le h\le V_Q}T_h(n)$. For each $j,u$ in (2), map the pair $(\alpha,\nu_d)$ on the disjoint moduli $r,d$ to $(\alpha^j,\nu_d^u)$. Its fibers have size at most $T_j(r)T_u(d)$. The coprime product conductor is the conductor of the corresponding character modulo $rd$, so there are at most $D\tau(rd)$ possible image characters with conductor $\le D$. Summing over $j,u$, dividing by $\phi(r)\phi(d)$, and using the standard subpower bounds for $\tau(rd),rd/\phi(rd)$ yields

$$
g(r,d)\ll_{\Theta,C,\epsilon}
                     Q^\epsilon\frac{D H(r)H(d)}{rd}.
 \tag{8}
$$

The estimate concerns the unweighted average over the genuine full product components; allowing every $\rho$ in (7) did not change a single eligibility test in the field.

Fix $b$ and its unitary divisor $d=b_\parallel$. There are $O(M/\operatorname{rad}(d))$ eligible $k\le4M$ in this group since $\operatorname{rad}(d)\mid2k$, and none when $\operatorname{rad}(d)>8M$. For each $r_b=r$, their multiplicity is $O_\epsilon(Q^\epsilon)$: $2k/r\le8M$ has all prime factors in $b$, so the uniform Rankin count of [R89 §4](r89-operator-prime-to-denominator-alias-conductors.md#4-count-the-actual-aliases-then-restore-the-fourier-packet) applies. Consequently (8) and the [R90 (4)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers) harmonic torsion estimate give

$$
\sum_{k:\ d(k,b)=d} g(r_b,d)
                \ll_{\Theta,C,\epsilon}Q^\epsilon D H(d)/d .
 \tag{9}
$$

Use $d/(q,d)\le d/\operatorname{rad}(d)$ on the group, since every prime of $d$ divides $q$. Let $L_{b,d}$ be its sum over true eligible aliases of $\sqrt{\mathfrak e(q,b)g(r_b,d)}$, and zero if $d<D_0$. Cauchy in the actual alias group and (9) give

$$
L_{b,d}^2\ll_{\Theta,C,\epsilon}Q^\epsilon
        \frac{d}{\operatorname{rad}(d)}
        \frac{M}{\operatorname{rad}(d)}\frac{D H(d)}d
       =Q^\epsilon O_{\Theta,C,\epsilon}\!
                              \left(MD\,\frac{H(d)}{\operatorname{rad}(d)^2}\right).
 \tag{10}
$$

No cancellation across aliases is assumed.

The remaining torsion sum with a radical weight is subpower:

$$
\sum_{d\le B}\frac{H(d)}{\operatorname{rad}(d)^2}
                       \ll_{\Theta,C,\epsilon}Q^\epsilon .
 \tag{11}
$$

Indeed, for a fixed exponent $h$ the function $T_h$ is multiplicative. By positivity the sum at that $h$ is bounded by $\prod_{p\le B}(1+p^{-2}\sum_{e=1}^{E_p}T_h(p^e))$, where $E_p=\lfloor\log B/\log p\rfloor$. Put $\mathcal L=\log Q$. For $p\le\sqrt{\mathcal L}$ or $p\mid2h$, the local bound $T_h(p^e)\le2h$ from the unit group decomposition gives a local logarithmic cost $O_{\Theta,C}(\log(2\mathcal L))$; there are at most $\sqrt{\mathcal L}+O_C(\log(2\mathcal L))$ such primes. For the rest use $T_h(p^e)=\gcd(h,p-1)\le p$, because $p\nmid2h$. Their logarithmic contributions are bounded by

$$
O_\Theta\!\left(\mathcal L\sum_{p>\sqrt{\mathcal L}}\frac1{p\log p}\right)
       =O_\Theta(\mathcal L/\log\mathcal L)=o(\mathcal L)
$$

by Chebyshev and partial summation, as in [R91 §4](r91-operator-denominator-product-power-conductors.md#4-sum-over-all-actual-denominator-types-and-restore-the-packet). This is uniform in $h\le V_Q$; summing that subpower number of exponents proves (11). In particular the weight does not require a squarefree $d$.

The exact per-denominator numerator bound from (7) and the alias sum has arithmetic factor $Q^\epsilon b\sum_{d\mid b,\,(d,b/d)=1}L_{b,d}$. Square by Cauchy over at most $\tau(b)$ divisors, and enlarge only the positive upper sum from unitary factorizations to all $dm\le B$. The number of such $m$ at fixed $d$ is at most $B/d$. By (10)–(11),

$$
\begin{split}
 \sum_{b\le B} b^2
          \left(\sum_{\substack{d\mid b\\(d,b/d)=1}}L_{b,d}\right)^2
 &\ll_{\Theta,C,\epsilon} Q^\epsilon B^2MD
       \sum_{\substack{d\le B\\d\ge D_0}}
              \frac{H(d)}{\operatorname{rad}(d)^2}\frac{B}{d}\\
 &\ll_{\Theta,C,\epsilon} Q^\epsilon\frac{B^3 MD}{D_0}.
 \end{split}
 \tag{12}
$$

The gate $d\ge D_0$ is used here, and is present literally in the theorem. Restricting to any fixed subset of aliases only improves these positive counts.

Use the exact common Taylor tests of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) after the preceding estimates. At integer offset $\ell$ the weighted $K_1$ is $O(1+|\ell|)$; the other weighted seminorms cost $O(S^{-1}+(1+|\ell|)^2/Q)$ as in R94 §4. The numerator-specific coefficients of absolute value $\le2^{-n}$ at Taylor order $n$ and the original unit-modulus outside phases are unchanged. Divide by $J\asymp Q$, square-sum $|\ell|\le R+1$, and apply (12) to yield (3). At the numerical parameters the arithmetic prefactor in (3) is $O(Q^{991/1000})$ before the three bracket factors, which give powers $-21/4000,-11/4000,-15/4000$ after multiplication. The same sharp comparison then follows by triangle with the inherited separately estimated pieces, without changing any benchmark or boundary terms.

## 4. Strict eligibility after the signed joint cut

At the numerical parameters choose $d=2^e$ the least power of $2$ at least $Q^{49/250}$, an odd prime $m\asymp Q^{97/500}$ with $b=dm$ in the high band, and an odd prime $r=k\asymp Q^{407/1000}$. The prime choices follow from Bertrand's postulate. Then $r_b=r,\ (2k,b)=2<G,\ k>K$, and $d\ge D_0$. On $r$ a generator-order character and its conjugate keep conductor $r>Q^{81/200}$ for every earlier allowed power. On $m$ take a generator $\eta$, and take $\eta'=\eta^t$ where $t=2V^*$ and $V^*$ bounds the finitely many preceding and present polylogarithmic exponent ranges. For all permitted signed nonzero mixed exponent pairs $u,v$ on $m$, one has $0<|u+tv|<m-1$ for large $Q$. The individual powers and product powers are also nonprincipal. Thus all these conductors are $m$, and the earlier signed joint selection remains inapplicable because

$$
rm\asymp Q^{601/1000}>Q^{3/5}.
$$

In particular the earlier unequal and positive joint selections also do not delete this pair.

At the shared factor $2^{e+1}$ take conjugate primitive characters as in [R94 §5](r94-operator-ungated-mixed-denominator-powers.md#5-a-nonzero-incidence-above-the-former-excess-gate). Their local product is principal and their original local incidence is nonzero with magnitude $2^{e+1}$. The full product is high on $m$ and all its earlier permitted powers retain conductor $m$, so both original full-product cuts are respected. The coprime primitive Gauss factors on $m$ and the alias conjugacy factor on $r$ are nonzero as well. Now $\nu_d=1$, so (2) holds with $j=u=1$ because $r<D=Q^{51/125}$ for large $Q$. This witnesses an actual additional incidence coefficient for the unmodified input, not a lower bound on the integrated packet field.
