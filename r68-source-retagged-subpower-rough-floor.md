# Retagging capped rough arity at the genuine subpower floor

Use the genuine negative central sum line, squarefree units, independent outer integer masks, hard $I\subseteq I_0=[\rho N,(1-\rho)N]$, and strict tests $d>D,e>D,de>Q$ of the [no-divisor-gap theorem](r68-source-two-higher-bands-no-divisor-gap.md). Thus $L=\log N$, $\ell=\log L$, $T=L/\ell$, and $D,Q$ are the floors of $\sqrt N e^{-20T}$ and $N e^{-20T}$. The two operands are $n=su,m=tv$ with nonempty lower products whose prime alphabets are

$$
    [\exp(c_iT/\ell^{a_i}),\exp(d_iT)],\qquad
                           0<c_i<d_i,\quad a_i\ge0
$$

for fixed constants. The **true** nonempty rough parts have all their primes at least $\exp(CT)$, with $C>\max(d_1,d_2)$ fixed. Impose an actual outer mask that each rough part has at most

$$
               K=K_0+\lfloor\gamma\log\ell\rfloor
$$

prime factors, with $K_0\ge3$ fixed and $0\le\gamma<1$ fixed. There is no original lower-product cap or proper-divisor gap. This is not the larger rough-prime floor $\exp(L/K)$ of the [widened-band theorem](r68-source-widened-higher-bands-growing-rough-arity.md); here primes of size $\exp(CT)$ can occur in the rough part.

**Theorem (unconditional, pointwise).** Put

$$
 b_0=1-2(a_1+a_2)-\gamma\log 2-2\gamma\log(2e/\gamma)
$$

with $\gamma\log(2e/\gamma)$ interpreted as zero when $\gamma=0$. If $b_0>0$, then for every fixed $A>0$, every fixed $0<\xi<b_0$, all sufficiently large even $N$, and all admissible hard intervals and masks, the original signed sum $R_N(I)$ satisfies

$$
          |R_N(I)|\ll
             \mathfrak S(N)\bigl(|I|\ell^{-b_0+\xi}+NL^{-A}\bigr).
 \tag{1}
$$

All constants may depend on the fixed parameters. The use of $\xi$ is explicit; it absorbs subpowers of $\ell$, not subpowers of $N$. This yields true subpower rough primes and slowly growing rough arity for small fixed $\gamma>0$. It does not cover unrestricted arity at that floor, arbitrary dense lower spectra, nonsquarefree inputs, or Hypothesis S.

## 1. Retagging is an exact reorganization of the same divisors

Choose $\varepsilon=1/64$. We may truncate the original $s,t\le N^\varepsilon$ with true error $O_A(NL^{-A})$. The original rough divisor multiplicity is at most $2^K$. The squared reciprocal factors on each original lower alphabet are $1+4/p$, with product $\ell^{O(1)}$ by Mertens; Rankin at $\lambda/T$ for fixed large $\lambda$ changes that product to at most $\prod(1+4e^{d_i\lambda}/p)=\ell^{O_\lambda(1)}$ and pays $L^{-\varepsilon\lambda}$. Cauchy's inequality on the fixed sum line and the bound $N/s$ on multiples of a fixed lower product give precisely the tail estimate of the no-gap theorem, with extra $2^{2K}=\ell^{O(1)}$, which is absorbed by choosing $\lambda$ large. The same absolute estimate applies to all the subsequent switched summands on the discarded tail.

Set $Y_*=\exp(\varepsilon L/K)$. In each retained operand, move the original rough primes below $Y_*$ into an extra factor $w_i$. Thus $w_i$ has all primes in $[\exp(CT),Y_*)$ and $\omega(w_i)\le K$. Set the new lower products to $S=sw_1$ and $U=tw_2$ and call the remaining two rough products $u_*,v_*$. This is a unique split into three disjoint prime ranges. Because $w_i\le Y_*^K=N^\varepsilon$, the new lower products are at most $N^{2\varepsilon}$. Both remaining rough products are nonempty and above $\sqrt N$, since they are at least $\rho N^{1-2\varepsilon}$. Their prime factors are at least $Y_*$.

The actual summands $\mu(d)\mu(e)\log(n/d)\log(m/e)$ and cutoff are unchanged, even if a moved prime occurs in a divisor. The new lower labels are simply taken over the complete new products $S,U$ before any positive enlargement. In particular the least prime used in each true switch is still a prime of the **original** higher lower part: every moved rough prime exceeds $\exp(d_iT)$, and the original lower part is nonempty. Thus the actual least-prime log remains $O(T)$, not $O(L/K)$. The exact double-switch identity and its one-sided necessary strip

$$
          \frac{D}{a c}<f\le \frac{\sqrt N}{c}
 \tag{2}
$$

continue to hold for least prime $a$, lower divisor label $c$, and proper rough label $f$ in the new grouping. Equation (2) follows as before from $D\le\max(D,Q/E)\le\sqrt N$ for every actual opposite long value $E>D$. Its width is $O(T)$ and it does not depend on the opposite rough label.

## 2. Bounded-arity medium-factor Euler costs

Write $\lambda^*(w)=\prod_{p\mid w,\ p>2}(p-1)/(p-2)$. The original lower profile of weight $\tau(s)\lambda^*(s)/s$ is $O(\ell^{2a_i})$ by its moving log endpoints. The new factor's reciprocal profile has local weight $2\lambda^*(p)/p$ at each possible prime. Its total one-prime sum is

$$
       M=\sum_{\exp(CT)\le p<Y_*}\frac{2\lambda^*(p)}p
           \le (2+o(1))\log\ell ,
 \tag{3}
$$

by Mertens: the log endpoint ratio is $\varepsilon\ell/(CK)$ and $\lambda^*(p)=1+O(1/p)$. The sum over products of at most $K$ such distinct primes with the $\tau(w_i)\lambda^*(w_i)/w_i$ weight is bounded by

$$
          \sum_{j\le K}\frac{M^j}{j!}.
 \tag{4}
$$

The factorial follows by counting all ordered distinct tuples first. When $\gamma>0$ with $\gamma<1$, take an upper envelope $M_+=(2+o(1))\log\ell\ge M$ with $M_+>K$ eventually. Then the right side of (4) is at most $(K+1)(eM_+/K)^K=\ell^{\gamma\log(2e/\gamma)+o(1)}$. If $\gamma=0$, it is $O((1+\log\ell)^{K_0})=\ell^{o(1)}$. This accounts for the moved factors without treating their arity as constant. Multiplying by the original profiles shows that the joint unmarked lower factor costs

$$
          \ell^{\,2(a_1+a_2)+2\gamma\log(2e/\gamma)+o(1)} .
 \tag{5}
$$

One least-prime mark multiplies its own slot by at most $O(T)$, by the exact retagging. Dropping correlations between original and moved arities after identifying all true labels can only increase these positive reciprocal sums.

## 3. Polynomial parameter range and the signed upper bounds

On a first-side switch freeze $(h,k)=(S f,U)$ as in (2), leaving both genuine rough complements. On a second-side switch the roles reverse, and in the two-light term freeze just $(S,U)$. Thus $hk\le N^{1-\omega}$ with $\omega=1/2-4\varepsilon>0$. On the genuine frozen pairs both coprimalities hold because the operands are exact units and sum to $N$. The same affine quadratic sieve as in the no-gap theorem applies with $Z=N^{\omega/24}$ and $z=\exp(\eta\varepsilon L/K)$ for fixed $0<\eta<\min(1,\eta_0\omega/(24\varepsilon))$. Indeed $z<Y_*$ and $\log z/\log Z<\eta_0$, where $\eta_0$ is the small absolute sieve constant from its $\log d$ moment. Its main count is $O(\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)K^2/(hkL^2))$ and error $O(N^{\omega/4})$ including hard floors; the determinant and root counts are unchanged.

An unrestricted reciprocal sum of retained rough products costs $O(K)$ by Mertens in $[Y_*,N]$, and their sum in a log strip of width $O(T)$ costs $O(K^2T/L)$ by factoring off a prime and using Chebyshev on unit-log intervals. Any rough part of $\lambda^*$ costs a bounded factor (at most $\exp(O(K/Y_*))$). Only the other rough label is omitted on a switched term, at most $2^K$ on the actual pairs; the light–light term omits both, at most $2^{2K}$. No such cost is incurred for the chosen frozen switched label. It follows from the true switches and (2) that the second difference costs $K^4 2^K/\ell$ times (5) and $\mathfrak S(N)|I|$. The two mixed terms have $K^4 2^K/\ell^2$ in its place because one heavy $L$ is replaced by a least-prime $O(T)$; the light–light has $K^2 2^{2K}/\ell^2$. Thus the stated $b_0$ is sufficient, since $2^K\le 2^{K_0}\ell^{\gamma\log2}$ and the remaining $K$ powers and (5)'s $o(1)$ are absorbed by the requested $\xi$.

The summed floor error is $O_A(NL^{-A})$. There are at most $O(N^{1-\omega}L)$ ordered frozen pairs. Each cofactor splits uniquely by the three ranges, there are $N^{o(1)}$ lower-label choices since $S,U\le N^{2\varepsilon}$ (split their prime factors at $\sqrt L$), and the other label losses $2^{2K}$ are $\ell^{O(1)}$. With absolute log marks at most $L^2$ this gives $O(N^{1-3\omega/4+o(1)})$. The original signs were used to derive the exact switched supports before taking any of these sieve upper bounds. This proves (1).

For a genuine lower-floor witness, choose fixed parameters with $b_0>0$. At an external scale $X$, take one lower prime in each original band and the same positive number of distinct moved primes on each side near $\exp((C+1)T_X)$, with all primes distinct. Take one moved prime on each side when $\gamma=0$; for $\gamma>0$ one may take $\lfloor K_X/2\rfloor$ on each side for large $X$. Write $S,U$ for their products with the lower primes. Take two further rough primes on each side, $f,F$ or $g,G$, with $Sf,Ug$ close to $\sqrt{2Q_X}$, and $SfF,UgG$ close to $X/2$. The PNT in narrow proportional windows supplies all these degrees of freedom: $\log S,\log U=O(K_XT_X)=o(L_X)$, so $f,g,F,G$ are at genuine near-half polynomial sizes, and the moved primes have room on both sides of their moving split. All factors can be chosen distinct so the even sum gives central units. The moving parameters are stable under $\log N=\log X+O(1)$ (and $K_N$ changes by at most one eventually). In particular $F,G>\sqrt N$, whereas the two maximum proper labels satisfy $Q<(Sf)(Ug)<3Q$ and $Sf,Ug>D$. The complete lower orbits involving $F,G$ vanish because $S,U$ are composite; among the remaining $f,g$ orbits only the maximum lower multipliers pass the product cutoff, since every omitted lower prime is at least three. Thus the **actual original** pair has summand $-\log F\log G$. The moved primes satisfy the true $\exp(CT)$ floor but lie below $\exp(L/K)$, and the example may have growing rough arity. This is a nonvacuity witness, not a lower bound for the aggregate.
