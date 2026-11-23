# Middle rough arity with a general exceptional reciprocal profile

Keep the original hard central signed sum from the [broad-tag middle-arity bound](r70-source-middle-arity-broad-tag-band.md): $0<\rho<1/2$ is fixed, $I\subseteq I_0=[\rho N,(1-\rho)N]$, $N$ is even, and $L=\log N$, $\ell=\log L$, $T=L/\ell$, $D=\lfloor\sqrt N e^{-20T}\rfloor$, $Q=\lfloor N e^{-20T}\rfloor$. The true squarefree operands are $n=su$, $m=tv$, with $(nm,N)=1$ and $n+m=N$. The two old lower products are nonempty and have all their primes in their respective full bands $[\exp(c_iT/\ell^{a_i}),\exp(d_iT)]$, for fixed $0<c_i<d_i$, $a_i\ge0$. The two old rough parts are nonempty, with all primes $\ge Y=\exp(CT)$, for fixed $C>\max(d_1,d_2)$. Both old lower products are uncapped. Further masks of the actual integers, independent of the interior divisor labels, are permitted. The signed sum is

$$
 R_N(I)=-\!\!\sum_{\substack{n+m=N,\ n\in I,\ m\in I_0\\(nm,N)=1,\ n,m\ {\rm selected}}}
 \;\sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
        \mu(d)\mu(e)\log(n/d)\log(m/e).
 \tag{1}
$$

No proper-divisor gap is imposed. Fix $0<\theta_i<1$, $E_i>0$, $\delta>0$ and put

$$
 V_i=\exp(E_i T\ell^{\theta_i}),\qquad
 B=\exp\left(\frac{L}{\delta\log\ell}\right),\qquad
 \lambda^*(w)=\prod_{\substack{p\mid w\\p>2}}\frac{p-1}{p-2}.
 \tag{2}
$$

For large $N$, $Y<V_i<B$. On leg $i$, let $\mathcal E_i(N)$ be any family of squarefree products of primes in the **actual** exceptional band $(V_i,B)$. Require that the complete product of those prime factors of that operand belongs to the family, including the empty product only if allowed. Assume for fixed $\beta_i\ge0$ and $C_i$ that

$$
 \sum_{w\in\mathcal E_i(N)}\frac{\tau(w)\lambda^*(w)}w
       \le C_i\ell^{\beta_i}.
 \tag{3}
$$

The family may vary with $N$; the bound must be uniform. There is no individual arity restriction in this formulation, and no restriction on the number of actual primes in either $[Y,V_i]$ or $[B,N]$.

**Theorem (unconditional, pointwise).** If
$\sigma=1-2(a_1+a_2+\theta_1+\theta_2)-\beta_1-\beta_2-\delta\log 2>0$,
then for every fixed $A>0$ and $0<\xi<\sigma$, uniformly in all the indicated hard windows and true masks,

$$
           |R_N(I)|\ll
              \mathfrak S(N)\bigl(|I|\ell^{-\sigma+\xi}+NL^{-A}\bigr)
 \tag{4}
$$

for all sufficiently large even $N$. Constants are allowed to depend on the fixed data and the constants in (3), not otherwise on the families, integer masks or windows.

In particular, one can allow $\lfloor\gamma_i\log\ell\rfloor$ prime factors for fixed positive $\gamma_i$ in the **same** exceptional intervals $(V_i,Y_*)$ of the earlier bound, where $Y_*=\exp(L/(64(J+1)))$ and $J=\lfloor\log\ell/\log\log\ell\rfloor$. It suffices that $0<\gamma_i<2(1-\theta_i)$ and that the displayed strict inequality for $\sigma$ holds with $\beta_i$ replaced by
$\gamma_i\log(2e(1-\theta_i)/\gamma_i)$. A separate consequence allows completely uncapped counts from any subalphabet $\mathcal P_i(N)\subset(V_i,B)$ with $\sum_{p\in\mathcal P_i(N)}1/p\le(\beta_i/2)\log\ell+O(1)$, provided all actual exceptional primes belong to that alphabet. Such an alphabet can grow, move and be noncontiguous. The complete unrestricted intermediate band is not covered by either consequence, and neither is Hypothesis S.

## 1. A true product tail independent of the exceptional bound

Use the [very-high-arity tail bound](r69-source-very-high-arity-rough-tail.md) with its exponent $2$, on the same true selection. Its §1 also truncates the old lower products at $s,t\le N^\epsilon$, $\epsilon=1/64$, at cost $O_A(NL^{-A})$, with no original cap. The first removal costs $O(\mathfrak S(N)(|I|\ell^{-2}+NL^{-A}))$ and leaves $\omega(u),\omega(v)<3\lceil H_2\log\ell\rceil$ for the explicit fixed $H_2$ there. In particular the two old rough divisor-label multiplicities are together $O(\ell^{b_0})$, with $b_0=6H_2\log2$.

For either operand let $W$ be the complete product of its actual rough prime factors below $B$, with no restriction yet on its exceptional part. The true block $W>N^\epsilon$ on either side contributes at most
$O_{A,\mathcal B}(\mathfrak S(N)(|I|\ell^{-\mathcal B}+NL^{-A}))$ for every fixed $\mathcal B>0$ in the current truncation. To prove this on the first side, select the shortest initial segment of the increasing primes of $W$ whose product $F$ exceeds $N^\epsilon$. This is unique on the actual operand, and

$$
 N^\epsilon<F\le N^\epsilon B\le N^{2\epsilon}
 \tag{5}
$$

for large $N$. Freeze $h=sF$, $k=t$. The two affine integers $u/F,v$ are true nonempty $Y$-rough products: the first is nonempty since $sF\le N^{3\epsilon}<\rho N$, and the second is nonempty from the original selection. The true units imply $(h,k)=(hk,N)=1$. We have $hk\le N^{4\epsilon}=N^{1-\omega_0}$, where $\omega_0=1-4\epsilon$. Apply the [affine rough upper sieve](r65-source-pointwise-rough-complements.md) with $Z=N^{\omega_0/24}$ and $z=\exp(\eta T)$, $0<\eta<C$ fixed; the condition for the truncated Euler denominator holds since $\log z/\log Z\to0$. The exact solution lattice for the hard interval has length $|I|/(hk)$, with determinant $N$ and one root at primes dividing $hkN$, two elsewhere. The bound is

$$
 \ll \frac{\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)}{hkT^2}
      +N^{\omega_0/4}.
 \tag{6}
$$

Enlarging to that sieve count discards the initial-segment condition only positively. The absolute original marked weight is $O(L^2\ell^{b_0}\tau(s)\tau(t))$ per pair of operands. The factors $s,F$ split uniquely in $h$ by the disjoint old lower and rough alphabets. With $O(N^{1-\omega_0}L)$ frozen integer pairs, the floor errors sum to $O(N^{1-3\omega_0/4+o(1)})$. Here the lower divisor weights on $s,t\le N^\epsilon$ are $N^{o(1)}$ uniformly, for example by splitting the primes at $\sqrt L$; all remaining weights in the floor error are $N^{o(1)}$ as well.

For the main part of (6), the old lower profiles with $\tau(w)\lambda^*(w)$ in the numerator contribute $O(\ell^{2(a_1+a_2)})$. Given any fixed $b>0$, use Rankin with exponent $x=b/\log B$ on the products $F>N^\epsilon$. Their reciprocal profile is bounded by

$$
 N^{-\epsilon x}\prod_{Y\le p<B}(1+\lambda^*(p)p^{x-1})
      \ll_b \ell^{-\epsilon b\delta}\,\frac{\log B}{\log Y}
      \ll_b \ell^{1-\epsilon b\delta}.
 \tag{7}
$$

Indeed $p^x-1\le b e^b\log p/\log B$, and
$\sum_{p<B}\lambda^*(p)(\log p)/p\ll\log B$ by Chebyshev and $\lambda^*(p)=1+O(1/p)$; hence the shift changes the unshifted product by at most a fixed factor. The latter product is $O(\log B/\log Y)$ by Mertens. The factor $N^{-\epsilon x}$ is exactly $\ell^{-\epsilon b\delta}$. The absolute mark costs at most $\ell^{b_0} L^2/T^2=\ell^{b_0+2}$ before lower profiles, so a sufficiently large fixed $b$ gives the asserted $\ell^{-\mathcal B}$. The same construction on the opposite side, keeping $hP\in I$, bounds its tail; a positive upper bound may count their intersection twice. This new truncation uses neither (3) nor a count cap in the exceptional band. Its saving comes from the genuine prefix crossing (5), not by assuming that an unbounded product fits into a short affine freeze.

## 2. Retag the entire movable product after the tail

Now retag every old rough prime below $B$, including the whole low bands $[Y,V_i]$ and the actual exceptional products, into the lower products $S=sW_1$, $U=tW_2$. We have $S,U\le N^{2\epsilon}$; the two remaining products $u_*,v_*$ are $>\sqrt N$ and all their primes are $\ge B$. These are exact factorizations of the same squarefree operands, with a unique split at the fixed disjoint alphabets. The least prime of either new lower product is still drawn from its **old** lower product; its logarithm is $O(T)$.

The reciprocal profile of a new lower product, weighted by $\tau(S)\lambda^*(S)/S$, is at most $O(\ell^{2a_i+2\theta_i+\beta_i})$ in its slot: the original range gives $O(\ell^{2a_i})$, the entire low rough band costs
$\prod_{Y\le p\le V_i}(1+2\lambda^*(p)/p)=O(\ell^{2\theta_i})$ and (3) supplies the last factor. An actual least-prime logarithm on this profile costs at most $O(T)$. No approximation to either Möbius sign or logarithmic mark has been made.

The number of divisor labels of each remaining rough part is at most
$2^{L/\log B}=\ell^{\delta\log2}$. The unweighted squarefree $B$-rough reciprocal profile with weight $\lambda^*$ is $O(\log N/\log B)=O(\log\ell)$. In particular in any log strip of width $W_0$ the reciprocal mass of **nonempty** rough products up to $N$ is $O((1+W_0)(\log\ell)^2/L)$: freeze all but one prime of the product, the last prime costing $O((1+W_0)/\log B)$ by Chebyshev over unit log intervals and the frozen profile costing $O(\log\ell)$. Counting all such decompositions only gives a positive upper bound.

## 3. Use the true signed switch before enlarging any support

Write $a=P^-(S)$, $b'=P^-(U)$, and use the [exact least-prime switch](r68-source-two-higher-bands-no-divisor-gap.md) on both legs. Its four terms are still the true divisor terms of (1), since the newly grouped factors are disjoint. In the heavy–heavy second difference there must be a switch on the first side for an actual fixed opposite bit. For a given actual opposite divisor $E>D$, it is $cf\le\max(D,Q/E)<acf$, with $c\mid S/a$, $f\mid u_*$. Because $E\ge D+1$ and the original integer thresholds give $D\le\max(D,Q/E)\le\sqrt N$, a true switch places $f$ in $(D/(ac),\sqrt N/c]$. It is nonempty and proper since $S<D$ and $u_*>\sqrt N$. The log width is $O(T)$ uniformly in the unconditioned opposite divisor. In either mixed term use the switch on its heavy side; the two-light term needs none. These facts apply with the exact strict curved test, including when $Q/E$ is not an integer.

Freeze $(h,k)=(Sf,U)$ on a first-side switch, the reflected pair on a second-side switch, and $(S,U)$ for two light sides. Then $hk\le N^{1/2+4\epsilon}=N^{1-\omega_1}$, with $\omega_1=1/2-4\epsilon>0$, and both remaining integers are true nonempty $B$-rough products. The same affine sieve applies on the exact lattice with $Z=N^{\omega_1/24}$, $z=B^\eta$ for fixed $0<\eta<1$. The main term is
$O(\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)(\log\ell)^2/(hk L^2))$, and the floor error is $O(N^{\omega_1/4})$ per freeze. The true coprimalities still hold; the bound applies before dropping any integer, mask or divisor-label condition. The total floor error is $O(N^{1-3\omega_1/4+o(1)})$, by the same integer-pair count, unique splits and subpower multiplicity bounds. For the true hard $I$ these errors do not require a minimum lattice-interval length.

Combine the two lower profiles with the uniform strip bound in §2 after the exact switch. In the heavy–heavy term the logs cost $O(L^2)$, the strip contributes $\ell^{-1}(\log\ell)^{O(1)}$, and the opposite unfrozen rough labels cost at most $\ell^{\delta\log2}$. The heavy–light bounds gain another $\ell^{-1}$ from their light logarithm. The light–light term has no strip, two $O(T)$ logarithms, and at most $\ell^{2\delta\log2}$ rough label choices. It is no larger than the heavy–heavy bound since $\delta\log2<1$, which follows from $\sigma>0$. Thus the main part is $O(\mathfrak S(N)|I|\ell^{-\sigma}(\log\ell)^{O(1)})$. The old true tails and the new product tail at $\mathcal B=2$ give (4), and the fixed $\xi$ absorbs the displayed powers of $\log\ell$.

## 4. Larger masks and an actual occupied example

For the count consequence, $B<Y_*$ for all sufficiently large $N$, since $\delta\log\ell>64(J+1)$. The mask $\omega(w)\le\lfloor\gamma_i\log\ell\rfloor$ in $(V_i,Y_*)$ therefore induces the same upper count inside $(V_i,B)$. By Mertens the available reciprocal prime mass with weight $2\lambda^*(p)$ is $M_i=(2(1-\theta_i)+o(1))\log\ell$. Ordered distinct tuples bound the profile by $\sum_{j\le \lfloor\gamma_i\log\ell\rfloor} M_i^j/j!$. Since $\gamma_i<2(1-\theta_i)$, these terms increase up to the endpoint for all sufficiently large $N$. Using $j!\ge(j/e)^j$ there gives the stated exponent $\gamma_i\log(2e(1-\theta_i)/\gamma_i)+o(1)$. The strict inequality for $\sigma$ allows an arbitrarily small increase in each $\beta_i$ if needed. For the uncapped alphabet consequence, the direct product $\prod_{p\in\mathcal P_i}(1+2\lambda^*(p)/p)$ bounds (3) using $\sum_p p^{-2}<\infty$. Neither argument needs any distribution of those exceptional factors in residue classes.

The increasing-count example is outside the former $J$ mask on both sides. At an external scale $X$, take $a_i=0$, $c_i=1,d_i=2,C=3$, $\theta_i=1/20,E_i=1$, $\delta=\gamma_i=1/100$, which satisfy the strict numerical condition. On each side use one old lower prime from the interior of the band, $\lfloor2\log\ell_X\rfloor$ different old rough primes near $\exp(4T_X)$, and $\lfloor(\gamma_i/2)\log\ell_X\rfloor$ further old rough primes near $\exp(T_X\ell_X^{1/10})$. The latter are in both exceptional bands $(V_i,B)$ and $(V_i,Y_*)$. All slots use distinct primes. Write $S,U$ for these products, whose log sizes are $o(\log X)$. Then use further distinct primes $f,F$ or $g,G$ so $Sf,Ug$ are each in a sufficiently narrow fixed relative interval about $\sqrt{2Q_X}$ and $SfF,UgG$ each similarly about $X/2$. The ordinary PNT guarantees each selection. Take $N=SfF+UgG$: it is even, both operands are genuine central units, and $\log N=\log X+O(1)$ preserves all the moving bands and gives $Q_N/Q_X=(N/X)(1+o(1))$. Choose the proportional intervals sufficiently narrow that $Q_N<(Sf)(Ug)<3Q_N$; also $Sf,Ug>D_N$ and $F,G>\sqrt N$. The old proper rough label $f$ times the old rough factors already included in $S$ lies strictly between $D_N/s$ and $\max(D_N,\lfloor Q_N/(D_N+1)\rfloor)$, and the other side has the analogous label. Thus the old proper-divisor gap is not satisfied on either side.

All true long labels containing $F$ pass against every true opposite long label and sum to zero on their own leg, since $\Lambda(Sf)=0$; then the same holds for $G$. Without $F,G$, the two maximum labels $Sf,Ug$ alone can pass the product gate, since omitting any factor divides their product by more than three. They have equal prime counts, so the remaining actual signed summand in (1) is $-\log F\log G$, for example with $I=I_0$. The arities are in the earlier middle rather than the very-high-arity tail. The example establishes genuine enlarged coverage but gives no aggregate lower bound.
