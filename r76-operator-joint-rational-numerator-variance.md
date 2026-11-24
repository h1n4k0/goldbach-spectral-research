# Joint rational numerators control more of the true modulus variance

**Scope.** This bounds the genuine all-alias covariance on a larger set of discrete modulus Fourier modes. The saving is from treating the full set of reduced numerators at one denominator as a Hilbert-space vector, including the actual sharp shell edges. In particular, this estimates a polynomially larger family of modes outside the earlier rational collars, on the same retained macro directions of R74 and R75. All original units, prime powers, orientations and continuous centering are retained. It does not treat all off-collar modes, a prescribed modulus, or weak S.

## Statement

Use the exact common transported parent basis of [R70](r70-operator-adaptive-parent-contrast-rank.md), with $4\le H<M\le Q^\Gamma$ for fixed $0<\Gamma<1$. Use either of the actual unmasked, body, and terminal profiles $h,f,g$ on either leg, as defined in [R71](r71-operator-parent-terminal-layer.md). As in [R73](r73-operator-rational-modulus-collars.md), $T_N^{u,v}$ is the matched signed matrix including all positive aliases $kN$ and all three signed affine orientations; there is no equality line. On the complete even shell $N=2m\in[Q,2Q]$, with $m=m_0,\ldots,m_0+J-1$ and $J\asymp Q$, use the unweighted discrete Fourier coefficients

$$
 \widehat T(j)=J^{-1}\sum_m e(-j(m-m_0)/J)T_{2m}^{u,v},
 \qquad e(x)=e^{2\pi i x}.
 \tag{1}
$$

Write $\mathcal C(B,R)$ for the union of the modes within circular index distance $R$ of $Ja/b$ over all reduced fractions $a/b\bmod1$ with $1\le b\le B$. Here $B\ge1$ is an integer, $R\ge1$, and $BM\le Q/100$ for all sufficiently large $Q$. Assume the original local Dirichlet GRH at every even modulus of the shell and auxiliary Dirichlet GRH for all moduli $q'\le\lceil8MB\rceil+2$, including $1$.

For each $b\le B$ and each reduced $a\bmod b$, let $j_0(a)$ be a nearest integer to $Ja/b$, choosing either when tied. For every integer $\ell$, uniformly in $b,\ell$,

$$
 \left(\sum_{a\bmod b}^{*}
        \|\widehat T(j_0(a)+\ell)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\epsilon,\Theta} Q^\epsilon\left[
   \sqrt{\frac{bM}{Q}}
  +b^{-1/2}\sqrt{\frac MQ}(1+|\ell|)
  +\frac{bM}{Q}(1+|\ell|)^2\right].
 \tag{2}
$$

For $b=1$ the reduced numerator set means the singleton $a=0$. The Fourier indices in (2) are taken modulo $J$. Consequently,

$$
 \left(\sum_{j\in\mathcal C(B,R)}
            \|\widehat T(j)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\epsilon,\Theta} Q^\epsilon\left[
   \sqrt{\frac MQ}\,B(1+R)^{1/2}
  +\sqrt{\frac MQ}\,(1+R)^{3/2}
  +\frac MQ B^{3/2}(1+R)^{5/2}\right].
 \tag{3}
$$

Each bound remains valid after compression by any fixed orthogonal projection on the common parent index space, including the true macro means of [R74](r74-operator-fixed-macro-mean-all-modes.md).

For $H=Q^{2/5}$, $M=Q^{3/5}$, $B=\lfloor Q^{17/100}\rfloor$, and $R=\lfloor Q^{1/20}\rfloor$, the right side of (3) is $O_\epsilon(Q^{-1/200+\epsilon})$ and the auxiliary cap is $O(Q^{77/100})$. The $\asymp Q^{39/100}$ modes from the centers with $B/2\le b\le B$ are all outside the R73 and [R75](r75-operator-prime-divisor-fourier-signature.md) example collars of denominators at most $Q^{1/10}$ and radius $Q^{3/40}$. On this newly covered Fourier set, combining (3) with R75 (2) therefore gives the same $O_\epsilon(Q^{-1/200+\epsilon})$ bound for the actual uncentered prime-Gram field on the retained macro directions, for $u,v\in\{h,f\}$ at the R74 parent sizes. This last comparison uses the benchmark bound only after the signed arithmetic estimate.

## 1. Rational switch with a common smooth parameter

We first prove the joint numerator estimate for a common weight $\omega\in C_c^2((Q,2Q))$, writing $K_1=\|\omega\|_\infty+\|\omega'\|_1$ and $K_2=\|\omega''\|_1$:

$$
 \left(\sum_{a\bmod b}^{*}
      \left\|\sum_{2\mid N}\omega(N)e(aN/(2b))T_N^{u,v}\right\|_{\rm HS}^2
 \right)^{1/2}
 \ll_{\Gamma,\epsilon,\Theta}Q^\epsilon
       \big[(bM+b^{-1/2}\sqrt{QM})K_1+bQM K_2\big].
 \tag{4}
$$

This has the strength of the previous bound for a single numerator in R73 (4), now for the full numerator vector, with exactly the same auxiliary GRH range.

Here are the required fixed supports and weights. Work in one dyad pair $V\le U$ and one pair $I,I'$ of parents, and one orientation $(\sigma_1,\sigma_2)\in\{(+,-),(-,+),(+,+)\}$. Their signed coefficients are $+,+,-$. The raw profile bounds of [R72](r72-operator-principal-modulus-low-modes.md) (4) apply with $b_I=\sqrt{|I|}/(\sqrt Q V)$, $b_{I'}=\sqrt{|I'|}/(\sqrt Q U)$; the supports are fixed in $[0,2QV]$, $[0,2QU]$. For one $k\le4U$, put $t=(\sigma_1x+\sigma_2 y)/k$, $q=2k$ and $q'=qb$. The affine raw weight
$\mathcal H(x,y)=\omega(t)u_{I,t}(x)v_{I',t}(y)$
is independent of $a$. As in R73 (5), its first partials have $L^1$ bounds $O(QU b_I b_{I'}K_1)$ in $x$ and $O(QV b_Ib_{I'}K_1)$ in $y$, and

$$
 \|\partial_{xy}^2\mathcal H\|_1
 \ll b_I b_{I'}
          [K_1+(QV/k)(K_2+K_1/Q)] .
 \tag{5}
$$

The smooth weight is extended by zero outside its support in real $t$; there are no tilted boundary measures in (5).

The original $N$-nonunit raw atoms and the temporary $q'$-nonunit atoms are accounted for with unchanged cost per $a$ as in R73 §1, namely $O_\epsilon(Q^\epsilon QU b_I b_{I'}K_1)$ in the entry after summing $k$. For clarity, for an original modulus $N$ the nonunit carriers on a fixed leg, necessarily prime powers of primes dividing $N$, have total Mangoldt mass $O((\log(3Q))^2)$; they have $O(U)$ possible partners over all aliases. After the switch, at a fixed $k$, a $q'$-nonunit prime power has $O(QU/q+1)$ partners by the exact relation modulo $q$. These estimates apply when *either* leg fails its respective unit mask. Summing over $k$, restoring the units, and taking the joint numerator norm costs at most an extra $\sqrt b$, within the $bM K_1$ term in (4) after HS aggregation below.

## 2. Additive Parseval in the exact incidence and the continuous term

Write $F_{q',r}(x)=\psi(x;q',r)-x/\phi(q')$ on unit residues. Expand both measures about their principal parts after the switch, as in R73. The phase is in the $a$-dependent residue incidence, and not in $\mathcal H$. For $c\bmod b$ let $P_c$ be the matrix on the unit residue index sets modulo $q'$ with entries

$$
 P_c(r,s)=\mathbf1_{\sigma_1r+\sigma_2s\equiv q c\pmod {q'}} .
 \tag{6}
$$

For each $c$, each row and each column has at most one $1$, since both $\sigma_i$ are units with an inverse modulo $q'$. Thus $\|P_c\|_{\ell^2\to\ell^2}\le1$ even when one residue in the full permutation is not a unit. The exact incidence (R73 (6)) is $A_a=\sum_{c\bmod b}e(ac/b)P_c$. For any vectors $X,Y$ on these residue index sets, finite additive Parseval and restriction to reduced numerators imply

$$
 \left(\sum_{a\bmod b}^{*}|X^{\mathsf T}A_aY|^2\right)^{1/2}
 \le\left(b\sum_{c\bmod b}|X^{\mathsf T}P_cY|^2\right)^{1/2}
 \le b\|X\|_2\|Y\|_2 .
 \tag{7}
$$

In particular the right side has $b$, not $b^{3/2}$. Apply (7) pointwise to the double-error integrand after two partial integrations. Auxiliary GRH and residue character Parseval give $\|(F_{q',r}(x))_r\|_2\ll\sqrt{QV}\log^2(3Q)$ on the first support and the analogous bound with $U$ on the second. Minkowski under the common derivative in (5) gives the per-$k$ joint numerator bound

$$
 \ll_\epsilon Q^\epsilon b Q\sqrt{VU}\, b_I b_{I'}
                 [K_1+(QV/k)(K_2+K_1/Q)] .
 \tag{8}
$$

These integrations by parts are the same on each component as in R72–R73; the vector estimate is finite and creates no new boundary terms.

The row and column sums in R73 (7) vanish when $b$ is not squarefree or $(b,q)>1$. Otherwise the single error collapses to the additive transform of $(F_{b,r}(x))_r$ at $a\sigma_1\bar q\bmod b$, with the nonunit correction in R73 (10). Multiplication by $\sigma_1\bar q$ permutes reduced numerators; the analogous map on the other leg does as well. Thus by *additive Parseval* its joint norm is at most $\sqrt b\,\|(F_{b,r}(x))_r\|_2$, plus $O(\sqrt b\,\log^2(3Q))$ for the temporary correction. Division by $\phi(q')=\phi(q)\phi(b)$ and partial integration using the first derivative bounds gives

$$
 \ll_\epsilon Q^\epsilon b_I b_{I'}K_1
       \frac{b^{-1/2}}{\phi(2k)}
                 (QV\sqrt{QU}+QU\sqrt{QV})
 \tag{9}
$$

for the joint single-error norm per $k$. This too is the old individual bound, not that bound multiplied by $\sqrt b$. For $b=1$, the additive transform is the single residue at $1$ and auxiliary $q=1$ gives the ordinary principal estimate.

It remains to restore the exact continuous model in the joint norm. Let $I_k(t)$ be the unweighted affine line integral of the two actual raw profiles as in R73 §3. Its product with $\omega$ has variation plus supremum $K\ll QV b_I b_{I'}K_1$. Use the same squarefree divisor expansion of $\mathfrak S(2km)$ there, with $d\mid m,\ (d,2k)=1$, and $\rho(d)=\prod_{p\mid d}(p-2)^{-1}$. On $m=dj$ the phase is $e(ad j/b)$. If $b\mid d$, the phase is constant; replace the sum with its integral divided by $2d$ at scalar error $O(K)$, hence at joint error $O(\sqrt b K)$. If $b\nmid d$, set $s=b/(b,d)>1$. Each geometric sum weighted by $\omega I_k$ is $O(K/\operatorname{dist}(ad/b,\mathbb Z))$. The residues $a\bmod b$ reduced modulo $s$ have multiplicity at most $b/s$, and multiplication by $d/(b,d)$ permutes the residues modulo $s$. None of the resulting residues is zero. Hence the joint error in this case is bounded by

$$
 K\left[\frac bs\sum_{r=1}^{s-1}
                \operatorname{dist}(r/s,\mathbb Z)^{-2}\right]^{1/2}
 \ll K\sqrt{bs}\le bK .
 \tag{10}
$$

The main coefficient for $b\mid d$ is exactly the R73 (12) coefficient $k/(\phi(2k)\phi(b)^2)$ when $b$ is squarefree and $(b,2k)=1$, and zero otherwise. It agrees with the switched double principal term, including the factor $k$ from the affine Jacobian. This comparison is made on each original line before the three signs are reassembled. Summing the errors over $d\le2Q$ costs $O_\epsilon(Q^\epsilon bK)$ including $\mathfrak S(2k)$, because $\rho(d)\ll_\epsilon d^{-1+\epsilon}$ and $\mathfrak S(2k)\ll_\epsilon Q^\epsilon$. Extending the main coefficient over $d>2Q$ costs $O_\epsilon(Q^\epsilon\sqrt b K)$ since the integral is $O(QK)$ and the extended divisor tail has weights $O_\epsilon(d^{-2+\epsilon})$. This proves the same exact continuous restoration with denominator factor $b$ in the joint norm, rather than $b^{3/2}$.

## 3. Summing entries, aliases, and orientations

For each dyad, $\sum_I b_I^2\ll (QV)^{-1}$ and likewise for $U$, by R72 (5); thus a shared entrywise factor $b_I b_{I'}$ costs $O((Q\sqrt{VU})^{-1})$ in the joint HS norm. Sum (8)–(9) over $k\le4U$, using the triangle inequality in the numerator vector and $\sum_{k\le4U}1/k\ll_\epsilon Q^\epsilon$, $\sum_{k\le4U}\phi(2k)^{-1}\ll_\epsilon Q^\epsilon$. The first term costs $O_\epsilon(Q^\epsilon b(UK_1+QV K_2))$ on the pair, and the single errors cost $O_\epsilon(Q^\epsilon b^{-1/2}\sqrt{QU}K_1)$. The model restoration just proved costs $O_\epsilon(Q^\epsilon b\sqrt{VU}K_1)$. The unit restorations in §1 cost $O_\epsilon(Q^\epsilon\sqrt b\,\sqrt{U/V}K_1)$, which is within $O_\epsilon(Q^\epsilon b U K_1)$. We have $U\ge V\ge1$; summing the $O((\log(3Q))^2)$ dyad pairs and the three orientations yields (4). Transposition handles the reversed dyad order, and exact basis compression costs no factor.

## 4. Sharp shell, fractional detunings, and projection energy

For a fixed $b$ use the smooth shell cutoff $\omega_b$ of R73 §4, whose edge strips have length $O(E_b)$, $E_b=\sqrt{bQM}$, with $\|\omega_b\|_\infty+\|\omega_b'\|_1\ll1$ and $\|\omega_b''\|_1\ll E_b^{-1}$. Write $x(t)=(t/2-m_0)/J$ so $|x(t)|\le2$ on $[Q,2Q]$ and $|x'(t)|=O(Q^{-1})$. For $j=j_0(a)+\ell$, put $s_a=j_0(a)-Ja/b$, so $|s_a|\le1/2$. The phase in (1), up to the scalar $e(a m_0/b)$, is $e(-am/b)e(-\ell x(2m))e(-s_a x(2m))$.

The fractional detuning can differ for every $a$. Use its absolutely convergent expansion

$$
 e(-s_a x(t))=\sum_{n\ge0}s_a^n\,\frac{(-2\pi i x(t))^n}{n!}.
 \tag{11}
$$

After extracting the scalar $s_a^n$ on the $a$-th component, apply (4) to the common weight
$\omega_{\ell,n}(t)=\omega_b(t)e(-\ell x(t))(-2\pi i x(t))^n/n!$.
Use the negative numerators modulo $b$ in (4); this is a permutation of the index set. By Leibniz, with $K_i(\cdot)$ defined above,

$$
 \sum_{n\ge0}2^{-n}K_1(\omega_{\ell,n})\ll1+|\ell|,
 \qquad
 \sum_{n\ge0}2^{-n}K_2(\omega_{\ell,n})
               \ll E_b^{-1}+(1+|\ell|)^2/Q .
 \tag{12}
$$

Indeed each derivative on the bulk factor of order at most two contributes $O((1+|\ell|+n)/Q)$ per derivative with the remaining absolutely summable bound $C^n/n!$, for an absolute constant $C$. The cutoff derivative costs its $L^1$ norm, and the factor with no cutoff derivative integrates over length $O(Q)$. This proves (12) and justifies termwise use of (4).

For the edges use additive Parseval *before* summing over numerators. If $Y_m$ is any Hilbert-valued sequence supported in the union of the two edge strips, then

$$
 \sum_{a\bmod b}
     \left\|\sum_m e(-am/b)Y_m\right\|^2
  =b\sum_{r\bmod b}\left\|\sum_{m\equiv r\bmod b}Y_m\right\|^2
  \ll (E_b+b)\sum_m\|Y_m\|^2 .
 \tag{13}
$$

The last inequality uses Cauchy and $O(E_b/b+1)$ occupants in each residue of the two strips combined. Since $E_b\gg b$, the bound is $O(E_b\sum_m\|Y_m\|^2)$. Apply it to the $n$-th term of (11), with $Y_m$ the actual $T_{2m}^{u,v}$ times $(1-\omega_b(2m))e(-\ell x(2m))(-2\pi i x(2m))^n/n!$. Its HS norm is $O_\epsilon(Q^\epsilon C^n/n!)$ pointwise from the local-GRH pointwise bound in R72 §1. Consequently the unsmoothed edge restoration has joint numerator norm $O_\epsilon(Q^\epsilon E_b)$ before dividing by $J$, by (13) and summation with $2^{-n}$. The scalar outside each component has absolute value one. This avoids the loss $\sqrt b$ one would incur by bounding the edges separately for each numerator.

Combining (4), (12) and this restoration, then dividing by $J\asymp Q$, gives (2): both the restored edge term and $bQM/E_b$ before division have size $O(E_b)$. Thus the final field has its original sharp shell and no taper. Every collar mode is $j_0(a)+\ell\bmod J$ for some integer $|\ell|\le R+1$. To prove (3), sum the three squared majorants of (2) first over these integer shifts and then over $b\le B$. The denominator square sums use $\sum b\ll B^2$, $\sum b^{-1}\ll\log(2B)$, and $\sum b^2\ll B^3$, respectively; the corresponding shift sums are $O(1+R)$, $O((1+R)^3)$, $O((1+R)^5)$. Counting overlaps only increases the sum. This proves (3) for the actual unweighted Fourier field. Orthogonal projection in space commutes with (1) when fixed, and is an HS contraction.

In the numerical example the three exponents are $-1/200,-1/8,-1/50$. Pairwise distinct reduced centers with denominators at most $B$ are separated by at least $J/B^2$ in circular index distance, much larger than both the original and new collar radii. The denominators in $[B/2,B]$ therefore supply $\asymp B^2(1+R)$ disjoint new modes, by the elementary totient sum $\sum_{n\le X}\phi(n)=3X^2/\pi^2+O(X\log(2X))$. That sum follows by counting coprime integer pairs up to $X$ using Möbius inversion. The selected higher denominators do not intersect the R75 example collars. The signed bound (3), plus the independent exact benchmark off-collar bound of R75 and $P=T+(D+K)$, proves the stated prime-Gram bound on this same new subset, with the same true profiles and retained macro directions. Neither the new subset nor its union with the previous collars exhausts the modulus frequencies.
