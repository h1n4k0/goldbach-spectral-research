# A joint count bound for the true sparse middle

Use the exact hard central sum, squarefree unit operands and uncapped lower products of the [factorial-profile theorem](r71-source-middle-arity-factorial-profile.md). Thus even $N$ has $L=\log N$, $\ell=\log L$, $T=L/\ell$, $D=\lfloor\sqrt N e^{-20T}\rfloor$, $Q=\lfloor N e^{-20T}\rfloor$. Write $n=su,m=tv$, with $s,t>1$ made up of primes in their respective complete lower bands $[\exp(c_iT/\ell^{a_i}),\exp(d_iT)]$ for fixed $0<c_i<d_i$, $a_i\ge0$. Both old rough parts are nonempty and have every prime $\ge Y=\exp(CT)$ with fixed $C>\max(d_1,d_2)$. On the true sum line $n+m=N$ require $(nm,N)=1$, $n\in I\subseteq I_0=[\rho N,(1-\rho)N]$, $m\in I_0$, where $0<\rho<1/2$ is fixed and $I$ is a hard interval with arbitrary endpoint conventions. The negative marked sum is

$$
 R_N(I)=-\!\!\sum_{\substack{n+m=N,\ n\in I,\ m\in I_0\\(nm,N)=1,\ n,m\ {\rm selected}}}
     \ \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
       \mu(d)\mu(e)\log(n/d)\log(m/e).
 \tag{1}
$$

No gap on proper rough divisors is assumed. Additional actual-integer masks independent of the internal divisor labels are permitted.

Fix $0<\theta_i<1$, $E_i>0$, and put $V_i=\exp(E_iT\ell^{\theta_i})$. Use the same exceptional-band endpoint as the [original broad-tag bound](r70-source-middle-arity-broad-tag-band.md):

$$
 J=\left\lfloor\frac{\log\ell}{\log\log\ell}\right\rfloor,\qquad
 Y_*=\exp\left(\frac{L}{64(J+1)}\right).
$$

Let $r_1,r_2$ count **all** actual old rough prime factors of the respective operands in $(V_i,Y_*)$, not the factors of a selected divisor. Define $F_i(0)=0$ and, for $x>0$, set

$$
     b_i=2(1-\theta_i),\qquad F_i(x)=x\log(e b_i/x).
$$

**Theorem (unconditional, pointwise).** For any fixed $\eta>0$ retain the exact actual pairs satisfying the joint count condition

$$
 F_1(r_1/\log\ell)+F_2(r_2/\log\ell)
       \le 1-2(a_1+a_2+\theta_1+\theta_2)-\eta .
 \tag{2}
$$

Then for every fixed $A>0$ and $0<\xi<\eta$, all sufficiently large even $N$, and all admitted hard $I$ and actual masks,

$$
              |R_N(I)|\ll
         \mathfrak S(N)\bigl(|I|\ell^{-\eta+\xi}+NL^{-A}\bigr).
 \tag{3}
$$

There is no total rough arity cap, and (2) does not impose a separate cap in either actual band. For $a_i=0,\theta_i=1/20$, this includes both counts at least $5\log\ell$ on the respective legs, and alternatively either count at least $7\log\ell$ with the other completely unrestricted. These are complementary to small-count control, not a bound for all intervening counts or for Hypothesis S.

## 1. A genuine top-occupancy tail

Put $\epsilon=1/64$ and $B=\exp(L/\log\ell)$. For large $N$, $Y<V_i<B<Y_*$. Use the [very-high-arity tail](r69-source-very-high-arity-rough-tail.md) with $\beta>\eta+1$ on the actual selected pairs, including its old lower-product truncation. We can restrict the old lower products to $s,t\le N^\epsilon$ at cost $O_A(NL^{-A})$, and old rough arities to $O(\log\ell)$ with an explicit fixed constant depending on $\beta,a_i$, at cost $O(\mathfrak S(N)(|I|\ell^{-\beta}+NL^{-A}))$. On the remaining actual pairs the absolute mark at fixed $n,m$ is at most $O(L^2\ell^{K_0}\tau(s)\tau(t))$ for some fixed $K_0$ depending only on that old rough-arity threshold. Also use the genuine first-crossing argument of §1 in the factorial-profile theorem with its $\delta=1$, to restrict the complete moved old rough products in $[Y,B)$ to at most $N^\epsilon$ in each leg. That argument puts no hypothesis on their count or reciprocal profiles. Although its stated earlier truncation used $\beta=2$, its proof takes any fixed bound on $K_0$: the Rankin factor $\ell^{-\epsilon b}$ there can have arbitrarily large exponent by choosing fixed $b$. Thus the complete-product tail costs $O(\mathfrak S(N)(|I|\ell^{-\beta}+NL^{-A}))$ here as well.

The part in which either leg has at least $\lceil H\log\ell/\log\log\ell\rceil$ actual primes in $[B,Y_*)$ is also an arbitrarily small log-log power tail, if the fixed $H$ is large enough in terms of $\beta,K_0,a_i$. On the affected leg let $q$ be its actual count in this top slice and freeze the product $G$ of the smallest $j=\lfloor q/3\rfloor$ of those primes. These factors are definite on the true operand. By the average of the first $j$ sorted prime logarithms, $G\le N^{1/3}$. On that side freeze its old lower product times $G$ and on the other side freeze just the old lower product. If the frozen coefficients are $h,k$ on $hP+kW=N$, then $hk\le N^{1/3+2\epsilon}=N^{1-\omega_0}$ where $\omega_0=2/3-2\epsilon>0$. Both remaining factors are nonempty old $Y$-rough products, since the frozen factors alone are smaller than $\rho N$. The original units imply $(h,k)=(hk,N)=1$. The [affine rough sieve](r65-source-pointwise-rough-complements.md) at $Z=N^{\omega_0/24}$ and $z=\exp(\nu T)$, $0<\nu<C$ fixed, counts these hard-window points from above by

$$
 \ll \frac{\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)}
                {hkT^2}+N^{\omega_0/4},
      \qquad \lambda^*(w)=\prod_{\substack{p\mid w\\p>2}}\frac{p-1}{p-2}.
 \tag{4}
$$

Here the interval in the integer parameter of the two affine forms has length $|I|/(hk)$, their determinant is $N$ up to sign, and their product has one root at primes dividing $hkN$ and two otherwise. The size of the cutoff ensures the truncated Euler denominator as in the cited sieve. The small-root parity at two follows from even $N$ and the units.

The reciprocal prime mass weighted by $\lambda^*(p)$ in $[B,Y_*)$ is $O(1+\log\log\log\ell)=o(\log\ell)$ by Mertens, since $\log Y_*/\log B=O(\log\log\ell)$. For $j\ge (H/4)\log\ell/\log\log\ell$ and large $N$, the sum over frozen $G$ of $\lambda^*(G)/G$ is bounded by the corresponding sum of $M^j/j!$, where $M$ is that top-slice prime mass. For each $j$ the bound follows by counting ordered tuples; the ratio of successive terms tends to zero throughout the tail. Since $\log(j/(eM))\ge(4/5)\log\log\ell$ for large $N$, this tail is $O(\ell^{-H/5})$. The old lower profiles with numerator $\tau(w)\lambda^*(w)$ cost $O(\ell^{2(a_1+a_2)})$ and the original absolute mark in (4) costs at most $\ell^{K_0}L^2/T^2=\ell^{K_0+2}$ before these profiles. Choose $H$ large enough. The bounded number $O(N^{1-\omega_0}L)$ of integer frozen pairs and the unique old lower/rough split give total floor error $O(N^{1-3\omega_0/4+o(1)})$: inside the hard lattice the physical rough-label and logarithmic weights are $N^{o(1)}$, as are the lower divisor multiplicities. The reflected orientation satisfies the same bound without altering $I$. Enlargements here are only positive after the actual unit pair and its true frozen prefix are fixed. This proves the asserted top tail, including its boundary $p=B$.

## 2. The joint reciprocal profiles transfer the actual counts

Retag all actual old rough primes below $B$ into the new lower products $S,U$. Then $S,U\le N^{2\epsilon}$ and their nonempty remaining rough parts $u_*,v_*>\sqrt N$ have primes $\ge B$. The least primes of $S,U$ are still in their old lower products and their logs are $O(T)$. Let $j_i$ be the counts of **moved** exceptional factors in $(V_i,B)$. By the true top removal, $0\le r_i-j_i=O(\log\ell/\log\log\ell)$ on each actual pair. The original old lower and complete low rough bands $[Y,V_i]$ give reciprocal profiles with numerator $\tau(w)\lambda^*(w)$ of size $O(\ell^{2a_i+2\theta_i})$ in slot $i$ by Mertens, as in the factorial-profile theorem. At fixed $j_i$ the remaining moved exceptional factor profile is at most $M_i^{j_i}/j_i!$, with

$$
                  M_i=\sum_{V_i<p<B}\frac{2\lambda^*(p)}p
                         =(b_i+o(1))\log\ell .
$$

The bound includes $j_i=0$, where it is one. Using $j_i!\ge(j_i/e)^{j_i}$, uniformly on the bounded normalized count range from §1 this is
$\ell^{F_i(j_i/\log\ell)+o(1)}$. The estimate also holds for negative values of $F_i$. The functions $F_i$ are continuous on this compact range, including zero. Thus for every possible retained $(j_1,j_2)$ induced by (2),

$$
  F_1(j_1/\log\ell)+F_2(j_2/\log\ell)
       \le 1-2(a_1+a_2+\theta_1+\theta_2)-\eta+o(1)
 \tag{5}
$$

uniformly. There are only $O((1+\log\ell)^2)$ such pairs. In all the freezes below the new lower factors are recovered uniquely from primes below $B$ in the frozen coefficients; the two moved counts are therefore known. We may apply the joint envelope (5) to their sum of positive reciprocal profiles, without bounding either exceptional marginal by its unconditional maximum. The unrestricted labels on high rough factors are handled separately below.

## 3. Use a second affine freeze to count the unfrozen rough labels

Use the [exact double least-prime switch](r68-source-two-higher-bands-no-divisor-gap.md) on the actual newly grouped squarefree factors. For a heavy–heavy second difference to be nonzero there must be a genuine first-side switch for an actual opposite divisor $E>D$. If $a=P^-(S)$, $c\mid S/a$, and $f\mid u_*$ is the switching rough label, its exact condition is $cf\le\max(D,Q/E)<acf$. Consequently

$$
               \frac{D}{ac}<f\le\frac{\sqrt N}{c}.
 \tag{6}
$$

Here $\max(D,Q/E)\le\sqrt N$ uses the exact original integer $E\ge D+1$. The label is nonempty and proper because $S<D$ and $u_*>\sqrt N$. The log width in (6) is $O(T)$ independently of the opposite label. In either heavy–light term there is a switch on the heavy side, and the two-light term has none. This identity is used before replacing the curved cutoff by the positive necessary condition (6).

In the first-side switch case, freeze $h=Sf$ as before. **Also** freeze $k=UG$ where now $G$ is the product of the smallest $\lfloor r_*/3\rfloor$ primes of the actual $v_*$, with $r_*=\omega(v_*)$. This is a new freeze of an ordinary part of the opposite operand; $G$ need not be part of its divisor label. Its product is at most $N^{1/3}$ by the same sorted-log average. Therefore $hk\le N^{5/6+4\epsilon}=N^{1-\omega_1}$ with $\omega_1=1/6-4\epsilon>0$, and both affine variables are nonempty $B$-rough. Use the reflected construction for a second-side heavy switch. For two light sides freeze the smallest third of each rough part times its lower product, so the envelope is even smaller. The true exact interval and coprimalities are retained in every case. The upper rough sieve at $Z=N^{\omega_1/24}$ and $z=B^\nu$ with fixed $0<\nu<1$ gives a main count
$O(\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)(\log\ell)^2/(hkL^2))$ and floor error $O(N^{\omega_1/4})$ per frozen pair.

The purpose of the extra freeze is to average the otherwise unbounded number of omitted rough labels. Given $G$ with $j=\omega(G)$, their true number on that side is at most $2^{r_*}\le4\cdot8^j$. The positive reciprocal profile of all such $G$, allowing arbitrary $j$, is thus at most a constant times

$$
 \prod_{B\le p\le N}(1+8\lambda^*(p)/p)
                      \ll (\log N/\log B)^8=(\log\ell)^8.
 \tag{7}
$$

This holds also if $G=1$. A switched label $f$ is already frozen. Its reciprocal weight in (6) is $O(T(\log\ell)^2/L)$, since one prime factor ranges over a log interval of width $O(T)$ at primes $\ge B$ while the reciprocal profile of the other factors costs $O(\log\ell)$. Precisely, Chebyshev over unit log intervals costs $O((1+T)/\log B)$ for the chosen prime, and all decompositions can be counted from above. In the two-light term use (7) independently for both freezes. The weights $\lambda^*$ on frozen factors split because the prime alphabets are disjoint and all genuine coefficients are squarefree.

The two heavy logs cost $O(L^2)$, so the normalized main term uses the factor $T/L=\ell^{-1}$ from (6), times at most a fixed power of $\log\ell$. With one light log there is an additional factor $T/L$ from the log weight; with two light logs there is no strip but the two log weights themselves give $(T/L)^2$. In every case the reciprocal profiles of the two new lower products are summed together, using the old/low profile exponents $2(a_1+a_2+\theta_1+\theta_2)$ and then (5). Combining yields a bound $O(\mathfrak S(N)|I|\ell^{-\eta+o(1)})$. The total lattice floor error is $O(N^{1-3\omega_1/4+o(1)})$, since there are $O(N^{1-\omega_1}L)$ frozen integer pairs, each has unique lower/rough splits, and individual divisor-label multiplicities and log weights are $N^{o(1)}$. The number of possible bits in the first-side switch is bounded by two, independent of $N$. This proves (3) after adding the true tails; no length lower bound is needed for the hard interval.

## 4. Actual new count pairs and what remains

For $a_i=0,\theta_i=1/20$ both $b_i=1.9$ and the unsigned rate budget in (2) before choosing $\eta$ is $0.8$. For $x\ge5$ the function is decreasing and $2F_i(5)=10\log(1.9e/5)<0.325$. Thus both true occupancies at least $5\log\ell$ allow, for example, $\eta=0.4$. On the other hand $\max_x F_i(x)=1.9$ and $F_i(7)+1.9<-0.22$, so either true occupancy at least $7\log\ell$ allows $\eta=1$ without *any* bound on the other count. More generally the contour compares the two actual counts rather than declaring an intermediate one good or bad by itself.

There are nonzero original summands with each count asymptotic to $5\log\ell$, below that single-leg example and the earlier very-high tail. At external scale $X$ take $c_i=1,d_i=2,C=3$, $E_i=1$ and the other constants from the numerical example. On each leg take one interior original lower prime and $\lceil 5\log\ell_X\rceil+2$ distinct old rough primes near $\exp(T_X\ell_X^{1/10})$. These are in $(V_i,B)$ and thus in the true old exceptional bands. The products $S,U$ on the respective legs have log size $o(\log X)$. By the PNT take four further distinct primes $f,F,g,G$ so $Sf,Ug$ are each in sufficiently narrow fixed proportional windows near $\sqrt{2Q_X}$ and $SfF,UgG$ near $X/2$. All primes in different slots can be taken distinct. At $N=SfF+UgG$ there are two central units, $N$ is even, and bounded variation of $\log N-\log X$ preserves all bands, with the strict product inequalities $Q_N<(Sf)(Ug)<3Q_N$, $Sf,Ug>D_N$ and $F,G>\sqrt N$. Both old proper-divisor gaps fail, using the old rough divisors $Sf/s$ and $Ug/t$, in their exact old forbidden intervals. The whole leg of labels containing $F$ is admissible against any opposite long label and sums to zero by $\Lambda(Sf)=0$, and similarly for $G$. After those cancellations only the two maximum labels $Sf,Ug$ can pass the strict product gate, since deleting a prime divides their product by more than three. Their Möbius parity agrees, so the genuine original summand is $-\log F\log G$. This demonstrates occupied new coverage, not an aggregate lower bound.

Finally the positive profile itself need not improve near its maximum upon imposing the movable-product cap or the cross coprimality. Indeed restrict the available exceptional primes further to $(V_i,B^{1/(\log\ell)^2})$; their weighted prime mass is still $(b_i+o(1))\log\ell$, and every product with $j_i=O(\log\ell)$ then lies below $N^\epsilon$ on that leg. Removing primes dividing $N$ changes the mass by $o(1)$, since each prime is at least $V_i$ and $\omega(N)\le L/\log2$. Among the ordered tuples the normalized weighted loss from a prime repetition (within or between legs) is $o(1)$ by a union bound, since the square sum of prime weights is $O(1/\min V_i)$ while the number of prime pairs in the tuple is $O((\log\ell)^2)$. Dividing by the two factorials gives the positive logarithmic rates $F_i(j_i/\log\ell)+o(1)$ by Stirling for fixed positive normalized counts. At $j_i/\log\ell\to b_i$ these rates sum to $b_1+b_2$, exceeding the allowed budget. This is an obstruction only for that positive reciprocal calculation, not a lower bound for the true additive sum or a disproof of Weak S. In particular the central count pairs near those values still require additional genuine cancellation.
