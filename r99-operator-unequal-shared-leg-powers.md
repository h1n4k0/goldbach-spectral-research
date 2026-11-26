# Unequal powers of the two individual shared-prime characters

The full shared product can remain primitive after all small powers, even when an unequal combination of the two individual shared characters is principal. This removes such combinations from the genuine packet. Grouping the actual alias by its full shared part is what keeps the cost of those individual characters at their true, possibly high, prime-power modulus.

## 1. Exact selection and packet estimate

Use the genuine $Z_{\rm shpow}$ retained by [R98](r98-operator-shared-product-power-cut.md#1-exact-sector-and-packet-estimate), with the original complete even shell, true transported parent profiles $h,f$, common taper, $J^{-1}$ normalization, and high-denominator packet $\mathcal C_+(B,R)$. Assume the same original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Keep $k>K\ge A/Q$, $(2k,b)<G$, $z,w>A$, all previous masks, and the actual signs. Both inputs of R98 are allowed, with or without the exact raw R86/R87 parity removals, and with $K\ge2P$ in the former version.

At $q=2k,\ q'=qb$, use the true decomposition

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
  q=r_b h_q,\quad (r_b,b)=1,\qquad
  s=d h_q,\quad q'=r_b m s .
 \tag{1}
$$

Here $r_b$ is the full part of $q$ on primes outside $b$, and $h_q$ is its full part on primes in $b$. Thus $d,h_q$ have exactly the same prime support, and $r_b,m,s$ are pairwise coprime. The two individual shared-prime components of the progression characters are denoted $\gamma,\gamma'\bmod s$; this shared-leg modulus is not just the denominator factor $d$.

Fix $D,D_0\ge1,\ C>0$, and $V_Q=\lfloor(\log Q)^C\rfloor$. Only at aliases with $d\ge D_0$, remove from $Z_{\rm shpow}$ every remaining pair satisfying

$$
\operatorname{cond}(\gamma^u(\gamma')^v)\le D
      \quad\text{for some integers }1\le u,v\le V_Q,\qquad u\ne v .
 \tag{2}
$$

Conductors are primitive inducing conductors, with conductor one on the trivial factor. The condition is on the two individual shared components; equal exponents would instead give a power of the lifted shared product, the location used by R98. No lower cutoff on the $r_b$ factors is added here. The deletion keeps all previous selections and is made before the original unequal detunings.

Write $Z_{\rm shmix}$ for the resulting genuine field and keep the packet norm of R98. With $R_*=1+R$,

$$
\|Z_{\rm shpow}-Z_{\rm shmix}\|_{\rm pkt}
   \ll_{\Gamma,\Theta,C,\epsilon}Q^\epsilon\frac{B^{3/2}MD}{D_0}
       \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+
                                   \frac{R_*^{1/2}}S\right].
 \tag{3}
$$

This permits arbitrary prime powers in the denominators. The estimate holds after a fixed orthogonal spatial compression or restriction to a subset of the packet, and it also applies if the deletion is limited to a subset of eligible aliases fixed by $k,b$.

At $B=\lfloor Q^{39/100}\rfloor,\ M=Q^{3/5},\ R=\lfloor Q^{1/400}\rfloor,\ S=Q^{249/250}$, choose $D_0=Q^{1/5}$ and $D=Q^{3/1000}$, with the earlier numerical thresholds unchanged. Then (3) is $O_{\epsilon,C}(Q^{-23/4000+\epsilon})$. The inherited sharp $\widehat T,\widehat P$ comparisons in the post-parity version remain $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm shmix}$. This estimates only the deleted sector of the stated packet. It does not bound the surviving covariance, a prescribed even modulus, another packet, or weak S.

## 2. Condition on the exact full product

Fix $q,b$ and the true full product $\nu=\nu_d\rho\bmod b$, with components modulo $d,m$, respectively. As in R93 §3, the original incidence forces the unique second progression character $\xi'=(\nu\circ\pi)\bar\xi$, where $\pi$ is unit reduction to $b$. On the shared factor this gives $\gamma'=(\nu_d\circ\pi_s)\bar\gamma$, with $\pi_s$ the unit reduction from $s$ to $d$. Hence at fixed $\nu$ condition (2) is the following single-leg subset of characters $\gamma\bmod s$:

$$
\operatorname{cond}(\gamma^{\,u-v}(\nu_d\circ\pi_s)^v)\le D
                     \quad\text{for at least one pair in (2)} .
 \tag{4}
$$

This subset is invariant under the forced partner map, since the union in (2) is unchanged by interchanging $u,v$. The earlier paired selections are also fixed, partner-invariant leg subsets after conditioning on the full product; at fixed $\rho$ they are the earlier conditions on the outside alias and coprime denominator components, with the earlier R97 condition at fixed $\nu_d$. The R98 and other full-product tests simply keep or omit the entire $\nu$-coefficient. The original individual projections stay in force. Accordingly the exact new deletion in that coefficient is implemented with the same projected genuine progression vector on both raw legs, with the earlier parity projections applied in their corresponding sharp parity terms. There is no assumption of boundedness for arbitrary pair masks.

For $j\ge1$ write $T_j(n)=|\ker(\chi\mapsto\chi^j)|$ in the character group of $n$, including $T_j(1)=1$, and put $H(n)=\sum_{j\le V_Q}T_j(n)$. For a single $(u,v)$ the map in (4) is a translate of the $(u-v)$-power map, whose attained fibers have size $T_{|u-v|}(s)$. Its number of candidate images of primitive conductor $\le D$ is at most $D\tau(s)$ by the count over inducing conductor divisors, as in [R90 §2](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers). There are $O(V_Q)$ exponent pairs with any fixed nonzero absolute difference. Count both other CRT factors freely in the full progression vector. This proves that the fraction of all progression characters used in the genuine selected vector $F_\nu$ is bounded above by

$$
O_{\Theta,C,\epsilon}\!\left(
                    Q^\epsilon\frac{D H(s)}s\right) ,
 \tag{5}
$$

as well as by one. The bound is uniform in the true $\nu$, using $\tau(s),s/\phi(s)\ll_\epsilon Q^\epsilon$ on the given polynomial scales. If $V_Q<2$ the deleted sector is empty. All prior cuts only decrease this fraction.

Normalized residue Parseval and the same uniform per-character GRH pointwise and integrated increment estimates give

$$
\begin{split}
   \|F_\nu(z)\|_2^2
     &\ll_\epsilon Q^\epsilon\frac{D H(s)}s\, z,\\
   \int_X^{2X}\|F_\nu(z+a)-F_\nu(z)\|_2^2\,dz
     &\ll_\epsilon Q^\epsilon\frac{D H(s)}s\,X|a|,
                                           \qquad 1\le |a|\le X/4 .
 \end{split}
 \tag{6}
$$

Here $X$ is on the true polynomial raw scales, and the per-character incremental input is [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference). These bounds are on the actual centered vectors after the fixed projections, with the finite-residue counting norm; they make no estimate of the relation at an individual spatial profile after detuning. Whenever a $Q^\epsilon$ factor is reused, one can choose smaller intermediate epsilons.

At a fixed $\nu$, [R93 (10)](r93-operator-unequal-mixed-denominator-powers.md#3-condition-on-the-true-product-before-taking-norms) bounds the scalar bilinear incidence coefficient for arbitrary complex vectors $U,V$ by

$$
|\mathscr C_\nu(U,V)|\ll_\epsilon
          Q^\epsilon\sqrt{\mathfrak e(q,b)}\,\|U\|_2\|V\|_2,\qquad
                       \mathfrak e(q,b)=d/(q,d).
 \tag{7}
$$

This is already after both normalized residue expansions and applies also to raw Fourier transforms. We do not apply the R94 partial-product estimate here to a $\nu_d$-dependent leg subset. The difference transpose at fixed $\nu$ is multiplication by $\nu(-1)$, so reflection of the reduced numerator gives the exact symmetric or skew complex bilinear form, with no conjugation of the argument vectors. The same-vector subset from (4) preserves that symmetry or skew symmetry.

Now apply the fixed common-test argument R93 §4 with (6) and (7). The cosine marginal identity uses $F_\nu$ on both raw legs, and the skew argument uses that same vector with the common raw interval restriction before taking the raw Fourier transform. The uniform squared estimates in (6) thus give their factor $DH(s)/s$ both for the direct pointwise bounds and for the increment and raw Fourier steps. The signed sum orientation keeps its original sign. For the post-parity version, the optional sharp pieces are subtracted separately using their identical reflected incidences on the relevant auxiliary-even leg. Every character selection commutes with the auxiliary reflection and parity operations, because those act diagonally on the same character basis. Their pointwise bounds are contracted by the per-leg projections, and the original reflected derivative costs and overlap convention stay unchanged. No raw marginal identity is applied on the sharp parity masks.

In this way the fixed $\nu,k,b$ common-test HS cost is at most
$Q^\epsilon\sqrt{\mathfrak e(q,b)}\,DH(s)s^{-1}\mathcal K$
up to the usual fixed-parameter constant. Here $\mathcal K=K_1+QK'_2$, enlarged by $Q(E_\infty+E_1)$ for the optional parity-reduced input as in [R97 §2](r97-operator-shared-product-joint-conductor.md#2-fixed-full-product-and-exact-common-test-cost); the latter uses $P/k\le1/2$. These are the original common-test seminorms. Multiplicative Parseval over full products in the reduced numerator group (counting measure) costs at most $\phi(b)\le b$, since the bound is uniform in $\nu$. Thus the genuine full numerator HS bound per alias is

$$
O_\epsilon\!\left(Q^\epsilon b\sqrt{\mathfrak e(q,b)}
                          \frac{D H(dh_q)}{dh_q}\,\mathcal K\right).
 \tag{8}
$$

Any previous full-product cut only decreases the positive norm in this step. All of (8) is before the original different detunings.

## 3. Sum the full shared part of each actual alias

Fix $b$ and its unitary divisor $d=b_\parallel$. In this group each $h_q$ is supported exactly on primes of $d$ and divisible by $\operatorname{rad}(d)$. For a fixed $h_q=h$ there are at most $8M/h$ possible $r_b$'s, because $q=r_bh\le8M$ and $q=2k$ determines the alias. We use this elementary count of the real aliases, allowing extra $r_b$'s only for a positive upper bound.

For a fixed power $j$, if $h,d$ have the same prime support then

$$
T_j(hd)\le 2j\,T_j(d).
 \tag{9}
$$

At odd primes, if $p^e\parallel d,\ p^a\parallel h$, the tame factor $\gcd(j,p-1)$ is unchanged. The wild factor is $p^{\min(v_p(j),e-1)}$ at $p^e$ and at most $p^{v_p(j)}$ times this after enlarging to $p^{e+a}$. At $2$ the unit group is trivial at level one, has a sign factor at level two, and for larger levels has that sign factor and a cyclic wild factor of order $2^{e-2}$. Its kernel growth is at most $2^{1+v_2(j)}$ between any two such levels with initial exponent at least one. Multiply over $p\mid d$ and use $\prod_{p\mid d}p^{v_p(j)}\le j$. The result includes $h=d=1$. In particular $H(dh)\le2V_Q H(d)$.

Write $L_{b,d}$ for the sum over the actual alias group of $\sqrt{\mathfrak e(q,b)}\,DH(dh_q)/(dh_q)$, and put it equal to zero for $d<D_0$. Use $(q,d)\ge\operatorname{rad}(d)$, the literal alias count at fixed $h$, and (9). The subpower cost $V_Q$ is absorbed, and

$$
\begin{split}
 L_{b,d}
 &\ll_{\Theta,C,\epsilon} Q^\epsilon
   \sqrt{\frac d{\operatorname{rad}(d)}}\frac{MDH(d)}d
       \sum_{\substack{\operatorname{rad}(d)\mid h\\
                          p\mid h\Rightarrow p\mid d}}h^{-2}\\
 &\ll_{\Theta,C,\epsilon}Q^\epsilon
              \frac{MDH(d)}{\sqrt d\,\operatorname{rad}(d)^{5/2}} .
 \end{split}
 \tag{10}
$$

The positive $h$-sum here equals
$\operatorname{rad}(d)^{-2}\prod_{p\mid d}(1-p^{-2})^{-1}$.
This counts the actual shared prime powers rather than treating $s$ as an independent parameter. The two signs and profiles have not been changed in the field.

To sum (10) over denominators we use

$$
\sum_{d\le B}\frac{H(d)^2}{\operatorname{rad}(d)^5}
                                 \ll_{\Theta,C,\epsilon}Q^\epsilon .
 \tag{11}
$$

Indeed, $H(d)^2\le V_Q\sum_{j\le V_Q}T_j(d)^2$. For any such $j$, by multiplicativity and positivity the sum with this fixed square is at most the finite Euler product with local factor $1+p^{-5}\sum_{e=1}^{E_p}T_j(p^e)^2$, $E_p=\lfloor\log B/\log p\rfloor$. Put $L=\log Q$. At primes $p\le\sqrt L$ or $p\mid2j$, the bound $T_j(p^e)\le2j$ gives at most $O_{\Theta,C}(\log(2L))$ for each local logarithm, with at most $\sqrt L+O_C(\log(2L))$ such primes. At the other primes $T_j(p^e)=\gcd(j,p-1)\le p$. Their total logarithm is at most $O_\Theta(L\sum_{n>\sqrt L}n^{-3})=O_\Theta(1)$. This is $o(L)$ uniformly over $j$; the two polylogarithmic factors in the $j$ count are subpower. This proves (11) even for unrestricted prime-power $d$'s.

At fixed $b$, (8) gives arithmetic factor at most $Q^\epsilon b\sum_{d\mid b,\,(d,b/d)=1}L_{b,d}$. Square by Cauchy over at most $\tau(b)$ divisors, use $b^2\le B^2$, and enlarge to all $dm\le B$ for this positive bound. Equations (10)–(11) give

$$
\begin{split}
 \sum_{b\le B} b^2
       \left(\sum_{\substack{d\mid b\\(d,b/d)=1}}L_{b,d}\right)^2
 &\ll_{\Theta,C,\epsilon}Q^\epsilon B^3M^2 D^2
      \sum_{D_0\le d\le B}\frac{H(d)^2}{d^2\operatorname{rad}(d)^5}\\
 &\ll_{\Theta,C,\epsilon}Q^\epsilon B^3M^2D^2/D_0^2 .
 \end{split}
 \tag{12}
$$

The extra $B/d$ in the first line counts the possible $m$'s. The factor $D_0^{-2}$ comes from the genuine lower gate on $d$.

Finally apply the exact [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) common Taylor tests. At offset $\ell$ the weighted common $K_1$ is $O(1+|\ell|)$, and the other weighted seminorms are $O(S^{-1}+(1+|\ell|)^2/Q)$, as in R98. Keep every original scalar detuning coefficient, bounded by $2^{-n}$ at Taylor order $n$, and each original unit-modulus exterior phase. Divide by $J\asymp Q$ and square-sum $|\ell|\le R+1$. Equation (12) now gives (3) with the actual numerator detunings. The arithmetic prefactor has the same exponent $988/1000$ as in R98's example and the largest final exponent is $-23/4000$. The inherited comparison follows by adding the preceding errors. No benchmark, boundary, or unselected sector estimate has been changed.

## 4. Strict eligibility beyond the shared-product cut

At the numerical parameters take $d=2^e$ to be the least power of $2$ at least $Q^{1/5}$, an odd prime $m\asymp Q^{19/100}$ with $b=dm$ in the high band, and $k=r\asymp Q^{9/20}$ an odd prime. The primes exist by Bertrand's postulate. Thus $q=2r,\ r_b=r,\ h_q=2,\ s=2^{e+1}$, and $(2k,b)=2<G,\ d\ge D_0,\ k>K$. On $r$ use a generator-order character and its conjugate, retaining conductor $r$ in all earlier power families. On $m$, take a generator $\eta$ and set $\eta'=\eta^{2V^*}$, where $V^*$ bounds all finitely many relevant polylogarithmic exponent ranges. All previous signed mixed exponents on $m$ are nonzero in absolute value and less than $m-1$ for large $Q$, and all the preceding individual and product powers on $m$ are nonprincipal. Thus the $m$-conductors are $m$, and $rm\asymp Q^{16/25}>Q^{3/5}$, excluding the earlier signed joint cut. The alias conductor also exceeds the R97 shared joint threshold $Q^{51/125}$.

At $s=2^{e+1}$, choose primitive $\gamma$ with sign value one and $5$-generator order $2^{e-1}$. Take $\gamma'=\gamma^{-3}$, which is also primitive, and $\gamma\gamma'=\gamma^{-2}$ induces a primitive character $\nu_d$ on $2^e$. Every allowed power of this lifted product has conductor $2^{e-O(\log\log Q)}$ and hence exceeds $Q^{3/1000}$, by the same cyclic unit-group computation as in [R96 §4](r96-operator-equal-and-signed-joint-powers.md#4-nonzero-incidence-in-both-additional-sectors). Thus the genuine R98 shared-product cut does not delete the pair. The full product has its high $m$-component as before. At this $2$-adic factor the original congruence is modulo $2$, automatic on two odd units with the actual signs; the two primitive additive Gauss factors on $s$ are nonzero. The local factors on $r,m$ are nonzero by their conjugate unit pairing and primitive additive Gauss sums, respectively. Finally $\gamma^3\gamma'=1$ gives (2) for $u=3,v=1$. This is a live additional original incidence coefficient for the unmodified input, not a lower bound on the integrated field.
