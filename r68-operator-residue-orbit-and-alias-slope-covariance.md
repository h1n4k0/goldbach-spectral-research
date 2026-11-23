# Pointwise residue-orbit covariance and reduced alias slopes in the exterior means

**Scope.** These are two decompositions of the actual signed all-alias second moment in the literal exterior mesowindow means. In the first, local odd Dirichlet GRH gives pointwise smallness of the complete centered covariance on bounded-degree graphs of antipodal unit residue orbits. This includes distinct orbits, four distinct raw primes, and aliases in arbitrarily separated raw bands, with the benchmark retained. In the second, auxiliary Dirichlet GRH gives an averaged deletion for alias-pair graphs, including large common divisors of two distant alias indices. These estimates leave a dense complementary covariance; neither proves its smallness or weak S.

## Definitions

Use the reference dyads and exact transported means of [R60](r60-operator-localized-coarse-contrast-annulus.md) and [R63](r63-operator-signed-window-mean-modulus-average.md). Let $1\le D\le H<M\le Q^\Gamma$ with $0<\Gamma<1$ fixed. Write $L=\log(3Q)$, and let $N>2$ be even with $Q\le N\le2Q$. Write $V,U$ for the starts of a pair of physical dyads and $I,I'$ for their respective windows. We use the exact normalized raw profiles $h_{I,N}$ of [R65](r65-operator-dense-low-raw-alias-deletion.md) (2)–(3), with raw support in $0\le x\le 2QV$ on the $V$-leg. Put $\omega_V=\sqrt{D/V}$ and $b_V=\omega_V/\sqrt{QV}$. The profile, also after multiplying by a fixed raw interval indicator, has

$$
\|h_{I,N}\|_\infty+\mathrm{TV}(h_{I,N})\ll_\Gamma b_V,
        \qquad \#\{I\text{ in the }V\text{-dyad}\}\ll V/D.
 \tag{1}
$$

This uses R65 (3) and the monotone square-root cutoff with variation $O(\sqrt{QV})$, and includes clipped final windows. We also use the same notation after a raw interval cut. Endpoints may be chosen with their exact intended integer inclusion.

At $s=kN$, $k\ge1$, let $A_{N,k}$ be the signed unit-restricted integer matrix and $B_{N,k}$ the signed continuous benchmark. The orientations $\sigma_1x+\sigma_2y=s$ are $(+,-),(-,+),(+,+)$ with weights $+,+,-$, respectively. In each, the atom has weights $\Lambda(n)\Lambda(m)h_{I,N}(n)h_{I',N}(m)$, with $(nm,N)=1$, and the benchmark is $\mathfrak S(s)$ times the corresponding affine integral in $x$ with these raw profiles. Let $E_{N,k}=A_{N,k}-B_{N,k}$. There is no $s=0$ term. For every $N$, each sum in $k$ is finite by the true raw support.

## 1. Antipodal residue orbit covariance, with exact centering

For this section retain all aliases, and let the raw restriction in a dyad pair be a fixed rectangle $R\times R'$, common to the three orientations. No condition on how far the raw coordinates are from zero is needed. A bounded number of rectangles combined with bounded coefficients is also allowed, by the triangle inequality. This includes the genuine long–long raw complement in R65, written as two disjoint rectangles; it does not require limiting the number or position of aliases.

Let $\mathscr U_N=(\mathbb Z/N\mathbb Z)^\times/\{\pm1\}$ be the set of antipodal unit orbits, of cardinality $m_N=\phi(N)/2$. Let $A_{N,\mathcal O}$ be the full integer contribution from orbit $\mathcal O$ across the three orientations and all $k\ge1$. On every affine line with $s=kN$, the local factor at primes dividing $N$ distributes uniformly over the unit residues of the free variable $x$: at $p^a\Vert N$ the corresponding admissible $x$'s are exactly the units, each giving the same prime density factor. Prescribing a unit residue modulo $p^a$ therefore takes exactly the fraction $1/\phi(p^a)$ of that local factor. At primes not dividing $N$ the local factors are unchanged by CRT. A given orbit takes the fraction $1/m_N$, also for the continuous density in the fixed raw rectangle. Consequently the exact orbit-centered decomposition is

$$
C_{N,\mathcal O}:=A_{N,\mathcal O}-B_N/m_N,\qquad
    \sum_{\mathcal O\in\mathscr U_N} C_{N,\mathcal O}
        =\sum_{k\ge1}E_{N,k},\qquad B_N=\sum_{k\ge1}B_{N,k}.
 \tag{2}
$$

No approximation of the benchmark or the literal weights is used in this identity.

Assume original local GRH at this modulus, in fact only for its odd characters in the proof below. In any physical dyad pair,

$$
\sum_{\mathcal O}\|C_{N,\mathcal O}\|_{\rm HS}^2
        \ll_{\Gamma,\epsilon} Q^\epsilon\frac{\min(V,U)+1}{Q}.
 \tag{3}
$$

Hence, for any graph $\mathcal G_N\subset\mathscr U_N^2$ of maximal row and column degrees at most $R_0$, the genuine covariance piece satisfies

$$
\sum_{(\mathcal O,\mathcal O')\in\mathcal G_N}
       |\langle C_{N,\mathcal O},C_{N,\mathcal O'}\rangle_{\rm HS}|
    \ll_{\Gamma,\epsilon} Q^\epsilon R_0\,\frac{M}{Q}.
 \tag{4}
$$

The same conclusion holds after summing over dyad pairs, at a logarithmic cost absorbed in $Q^\epsilon$. The graph can depend on $N$ and on the physical dyad pair. A sample graph relates $r$ to $r'$ if $r'\equiv \pm r+h\bmod N$ for some integer $|h|\le R_1$, with degree $O(1+R_1)$. Another takes $r'\equiv\pm a r$ for $a$ in a list of $O(R_1)$ units. These include distinct orbits even after discarding the exact diagonal. At $M=Q^{3/5}, R_1=Q^{7/20}$, (4) is $O_\epsilon(Q^{-1/20+\epsilon})$ in the **squared** norm expansion, pointwise at every $N$ satisfying local GRH. No auxiliary moduli are needed.

### Integer part

Define the grand window vector $P_{V,r}$ by the entries $\sum_{n\equiv r\bmod N}\Lambda(n)h_{I,N}(n)$ for $I$ in the $V$-dyad with its chosen raw cut. With a representative $r$ of $\mathcal O$, let $d_{V,r}=P_{V,r}-P_{V,-r}$. For the exact signs in the definition,

$$
A_{N,\mathcal O}=d_{V,r}\otimes d_{U,r}-D_{N,\mathcal O},
  \qquad
  D_{N,\mathcal O}=\sum_{n\bmod N\in\mathcal O}
     \Lambda(n)^2 h_V(n)\otimes h_U(n).
 \tag{5}
$$

Here $h_V(n)$ is the vector of cut profiles. Indeed the two difference orientations together run over all unequal pairs with the same unit residue; the sum orientation runs over the opposite residues. This gives (5) after removing the equality atoms, not a positive unsigned estimate. The sum orientation has no equality atom because $N>2$ and $N\mid2n$ cannot hold for a unit $n$.

Bounds (1) show that $\|h_V(n)\|_2\ll(QV)^{-1/2}$. There are $O(V)$ raw integers in a residue class within this support, so $\sup_r\|d_{V,r}\|_2\ll L\sqrt{V/Q}$. On the other hand define $F_r^-(z)=\psi(z;N,r)-\psi(z;N,-r)$. Character orthogonality gives

$$
\sum_{r\in(\mathbb Z/N\mathbb Z)^\times}|F_r^-(z)|^2
       =\frac4{\phi(N)}\sum_{\chi\bmod N,\;\chi(-1)=-1}
                                      |\psi(z,\chi)|^2
       \ll_\Gamma zL^4\qquad(1\le z\le4QM).
 \tag{6}
$$

The final bound is the standard GRH prime-sum bound, applied only to the odd characters. Inducing from a primitive character adds $O(\log N\log(2z))$ from the missing prime powers, within the bound. Partial summation in each cut window profile using (1), (6) gives $\ell^2(r)$ norm $O(L^2\omega_V)$; choosing the integer endpoint convention of the cut adds at most the matching endpoint atom bound. Sum the squares over $I$ to obtain $\sum_{\mathcal O}\|d_{V,r}\|_2^2\ll_\Gamma L^4$. Applying these supremum and square estimates on opposite legs gives

$$
\sum_{\mathcal O}\|d_{V,r}\otimes d_{U,r}\|_{\rm HS}^2
           \ll_\Gamma L^6\frac{\min(V,U)}{Q}.
 \tag{7}
$$

For the equality matrix in (5), each orbit has $O(\min(V,U))$ raw integers in the common support. From the pointwise profile norms,
$\|D_{N,\mathcal O}\|_{\rm HS}\ll_\Gamma L^2\min(V,U)/(Q\sqrt{VU})\ll L^2/Q$.
The orbit sum of its squared norms is $O(L^4/Q)$. This proves (3) for the integer part.

### Exact continuous benchmark

For $0\le T\le 4M+1$, the usual Euler factors for even $N$ imply

$$
\sum_{1\le k\le T}\mathfrak S(kN)
          =\frac{N}{\phi(N)}T+O_{\Gamma,\epsilon}(Q^\epsilon)
 \tag{8}
$$

uniformly in the range, as follows directly from the divisor expansion
$\mathfrak S(kN)=\mathfrak S(N)\sum_{d\mid k}a_N(d)$, where $a_N$ vanishes off squarefree $d$ prime to $2N$ and equals $\prod_{p\mid d}(p-2)^{-1}$ there. For any fixed $\delta>0$, $a_N(d)\ll_\delta d^{-1+\delta}$; hence both $\sum_{d\le T}a_N(d)$ and $T\sum_{d>T}a_N(d)/d$ are $O_\delta((1+T)^\delta)$. The main coefficient $\mathfrak S(N)\sum_da_N(d)/d$ equals $N/\phi(N)$ by canceling the Euler factor at every odd $p\nmid N$, leaving $p/(p-1)$ at each $p\mid N$, including $2$. In particular $\mathfrak S(N)\le N/\phi(N)\ll_\delta Q^\delta$. This proves (8) also for $0\le T<1$.

In an entry let $b_\sigma(t)$ denote the raw continuous integral for the orientation $\sigma$ at $s=Nt$, without $\mathfrak S(s)$. Its supremum plus total variation on $t\ge0$ is

$$
\ll_\Gamma Q\min(V,U)b_Vb_U .
 \tag{9}
$$

Use the $L^1$ norm of one cut weight and the sup and variation of the other, then swap legs and take the smaller bound; scaling or reversing the line parameter does not change the variation bound. These convolution profiles are continuous, including for hard raw interval cuts. Their signed combination has integral in $t>0$ equal to zero: the two positive differences cover $x>y$ and $x<y$, and the negative sum covers the same whole positive quadrant, with the same Jacobian $1/N$ and the same raw rectangle. The line $x=y$ is Lebesgue null in this statement. Applying (8) by partial summation to (9) and aggregating windows proves

$$
\|B_N\|_{\rm HS}\ll_{\Gamma,\epsilon}
              Q^\epsilon\frac{\min(V,U)}{\sqrt{VU}}\ll Q^\epsilon.
 \tag{10}
$$

Thus the contribution of the orbit-shared benchmark to the left side of (3) is at most $O_\epsilon(Q^\epsilon/m_N)=O_\epsilon(Q^{-1+\epsilon})$. Combining (5)–(10) proves (3). Cauchy and $2ab\le a^2+b^2$ on the graph, with both degree bounds, give (4). There is no implication for the dense graph of all distinct orbits.

## 2. Reduced alias slopes: a complementary selected-moduli estimate

This section concerns graphs of the indices $k$, not the preceding graphs of residue orbits. Let $\mathcal A\subset[Q,2Q]$ consist of $J\ge1$ distinct even moduli satisfying original local Dirichlet GRH. Assume additionally auxiliary Dirichlet GRH for every $q\le\lceil20\sqrt{QM}\rceil$, including $q=1$. Retain fixed raw rectangular cuts in the physical dyad pair within $x,y\ge Q$, as appropriate for the R65 long–long complement in its example. The raw cuts can differ by orientation, and the alias mask can now be arbitrary by entry and $N$. Put $E_{N,k}=0$ at masked entries. Then

$$
\frac1J\sum_{N\in\mathcal A}\sum_{k\ge1}\|E_{N,k}\|_{\rm HS}^2
 \ll_{\Gamma,\epsilon} Q^\epsilon
       \left[\frac{(QM)^{1/2}}{J}+\frac{M}{JH}+\frac{M}{QH}\right].
 \tag{11}
$$

In particular for any graph on the positive retained alias indices with row and column degrees at most $R_2$, independent choices at each $N$ allowed, the average of the sum of absolute covariance terms $|\langle E_{N,k},E_{N,k'}\rangle_{\rm HS}|$ over the graph is bounded by $R_2$ times (11). One can even allow pair graphs chosen separately for each entry by applying the scalar degree bound before summing entries. For positive $K\ge1$, one such graph is

$$
\frac{\max(k,k')}{(k,k')}\le K ,
 \tag{12}
$$

of degree $O_\epsilon(KQ^\epsilon)$: for fixed $k$, choose $d\mid k$, then $k'=d b$ with $1\le b\le K$. Another is $|k-k'|\le K$. The first graph includes genuine distant cross-band terms, e.g. $k'=2k$ with $k$ large, which need not fit in any one [R67 band](r67-operator-contiguous-bulk-alias-band.md). At $H=Q^{2/5},M=Q^{3/5},J\gg Q^{99/100},K=Q^{9/50}$, both removals are $O_\epsilon(Q^{-1/100+\epsilon})$ in the squared norm expansion.

To prove (11), follow the shorter raw arc decomposition of R65 for a fixed pair of raw dyads $v,w$ with $1\le v\le w$, paired with physical dyads $V,U$ respectively after transposing if necessary. Put $\lambda_v=v/V,\lambda_w=w/U$, $a_v=\omega_V\lambda_v,a_w=\omega_U\lambda_w$. R65 (4)–(8) give coefficient $\ell^2$ bounds for the minor and major double-error tensors, per entry, $O_\epsilon(Q^\epsilon a_va_w(Qv)^{1/4})$. The single-error coefficient norm is $O_\epsilon(Q^\epsilon a_va_w\sqrt{1+w/v})$. These include the normalized derivative in $t\in[Q,2Q]$ on the exact moving profiles. Aux GRH at this pair is needed only up to $\lceil20\sqrt{Qv}\rceil$.

For a fixed Fourier coefficient array $c_s(t)$, before applying any alias Cauchy, the sum over $N,k$ of its squared values at $s=kN$ is $\ll_\epsilon Q^\epsilon\sum_s\|c_s(t)\|_{\rm HS}^2$, because a given positive $s\ll QM$ has at most $\tau(s)$ representations. Entry masks may be dropped after squaring, not before. For the actual $t=N$, apply the fundamental theorem of calculus in the parameter $t$, then Minkowski and the same divisor count restricted to $N\ge t$. Thus no factor $\sqrt w$ occurs in the sampled error norms here. Pointwise, the unit-error and model-restoration cost in R65 §3 is $\ll_\epsilon Q^\epsilon a_va_w/\sqrt{Qv}$ **per alias**, before the summation over its $O(w)$ possibilities. More explicitly the $q$-nonunit product has this cost by its supremum and the other leg's Fourier $L^2$ norm, the $N$-nonunit product costs $O(L^{O(1)}a_va_w/(Q\sqrt{vw}))$ by unique partners, and the restored continuous-plus-Ramanujan tail costs $O_\epsilon(Q^\epsilon a_va_w\sqrt{v/w}/\sqrt{Qv})$ by R65 §3. Their squared sum costs the factor $w$, not $w^2$.

Use the same HS aggregation as R65, with multiplier $O(\sqrt{VU}/D)$ canceling $\omega_V\omega_U$. Consequently the square root of the mean in (11) from this dyad pair is at most

$$
Q^\epsilon\lambda_v\lambda_w
       \left[\frac{(Qv)^{1/4}}{\sqrt J}
                 +\frac{\sqrt{1+w/v}}{\sqrt J}
                 +\sqrt{\frac{w}{Qv}}\right].
 \tag{13}
$$

For nonempty raw supports, $\lambda_v,\lambda_w\le2$ and, notably,
$\lambda_v\lambda_w\sqrt{w/v}\ll \sqrt{M/H}$, by writing $\lambda_v/\sqrt v=\sqrt{\lambda_v}/\sqrt V$. Sum the logarithmically many dyads, take squares, and obtain (11). The slope estimates follow by $2ab\le a^2+b^2$. This proof is not an inference from random phases or from a fixed contiguous alias band.

## 3. A collision count and the scope of the two deletions

There is also a pointwise elementary estimate for collisions among the raw arguments in the integer–integer part of the square, all aliases included. Take any two atoms occurring in the same matrix entry; retain those for which some prime base is shared across the two atom pairs. Their total absolute contribution, summed over entries and dyad pairs, is $O_\epsilon(Q^\epsilon M/Q)$. This applies to proper powers with the same base as well as repeated raw integers, and does not rely on odd GRH.

For example, if the shared base is between the two $V$-legs, there are $O_\Gamma(QV L^{O(1)})$ choices for the corresponding two raw powers since each first raw integer can be partnered with at most $O(L)$ powers of its prime. Each of their respective $U$-partners lies in one congruence class up to orientation, with $O(U)$ choices. After summing profiles over window entries, the bound on the product of four weights is $O(1/(Q^2VU))$ by (1), giving $Q^\epsilon U/Q$ including the marks. When the shared base is between a $V$- and a $U$-leg use $O_\Gamma(Q\min(V,U)L^{O(1)})$ base-power choices and $O(VU)$ partners. This yields the same bound. Masks may only decrease this absolute counting estimate.

A shared base within one pair requires a proper power: raw equality is impossible in either a nonzero difference or a unit sum alias. The number of such ordered same-base raw pairs is $O_\Gamma(\sqrt{QM}L^{O(1)})$, by choosing a base at most $O(\sqrt{QM})$ and two exponents. An unrestricted partner pair on the same modulus has $O(QVU)$ possibilities, by first specifying one raw integer and choosing its other leg in the required congruences. The absolute contribution from these within-pair collisions is $O_\epsilon(Q^\epsilon\sqrt{M/Q})$. The same bound holds for that integer collision paired with the continuous benchmark, whose entrywise absolute sum over lines is $\ll_\epsilon Q^\epsilon QVU b_V b_U$ by the line-length bound and $O(V+U)$ aliases. This counting does not alter the benchmark for distinct bases.

The pointwise orbit covariance decomposition (2) requires the same raw rectangle on the three orientations and all aliases: the factorization (5) can fail after arbitrary alias truncation. The averaged alias graph result (11)–(13) instead retains arbitrary masks in its scope and does not use that factorization. They are complementary estimates, not an assertion that their overlapping parts may be subtracted independently without controlling the intersection. The still-uncontrolled all-alias variance includes genuine four-distinct-base interactions between densely many distinct residue orbits, and the exact benchmark remains part of that residual.
