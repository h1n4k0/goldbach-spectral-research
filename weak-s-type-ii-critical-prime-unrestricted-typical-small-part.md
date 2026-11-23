# Fully unassigned small-prime allocations through the typical total count

Keep the true central fixed-target prime polynomial $P$ with any fixed $|E(u,v)|\le1$, the actual active or inactive hard product gate, and the three genuine signed least-prime branches of the [signed rough-exponent proof](weak-s-type-ii-critical-prime-signed-all-rough-exponents.md). Thus $N$ is even, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, $d\in I_0=I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le m=dk<N/2$, $(m,N)=1$, with actual weight $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. The branches retain their original sharp endpoints, with $p=P^-(m)$: (1) $p\mid d$ and $d/p$ fails the lower endpoint; (2) $p\mid k$ and $pd$ fails the upper endpoint; (3) $p\mid k$, $pd\in I_0$, and $k/p\le t$.

Fix $0<\gamma<1$ and $0<c<1/\log 2$, put $Z=\exp(L^\gamma)$, $\lambda=\log Z$, and set $K=\lfloor c\log\lambda\rfloor$. For any squarefree $m$, let $b=r_Z(m)$ be the product of its prime factors strictly below $Z$. For $2\le W<Z$, let $D_{\le K,W}$ retain all genuine boundary terms with $p\le W$ and $\omega(b)\le K$. For each retained product, every actual allocation of its small factors to $d$ and $k$ is kept, without an alphabet, individual arity, or size condition on either side. For every fixed $J>0$ the ordinary coefficient energy satisfies

$$
\int_0^1|D_{\le K,W}(\alpha)|^2\,d\alpha
\ll_{\gamma,c,J}
 N(1+\log W)^2(1+L_2)
 \left(\lambda^{-1+c\log2}+\lambda^{-3+\eta(c)}\right)
 +NL^{-J},
\qquad \eta(c)=c(1+\log(4/c)).
\tag{1}
$$

In particular for fixed polylogarithmic $W$, both the full and double-centered true signed pairings on the entire critical-prime shell are $o(N)$ for every sufficiently large even $N$, uniformly in the original hard cuts. This reaches beyond the typical scale $\log\lambda$ of the total small-prime count in the unweighted reciprocal Euler measure. It does not estimate the unrestricted higher counts.

## 1. What the absolute allocation bound gives

The [fixed-allocation result](weak-s-type-ii-critical-prime-signed-all-rough-exponents.md#4-the-signed-positive-form-and-summation) bounds each true small allocation at fixed $b\le N^{1/10}$ by $O_\gamma((N/b)(1+\log W)(1+L_2)/\lambda^2)$ in the ordinary squared norm. Cauchy over at most $2^{\omega(b)}$ allocations, and then disjointness of distinct $b$ in the integer product, costs the positive sum

$$
S_K=\sum_{\substack{b\ {\rm squarefree},\,P^+(b)<Z\\\omega(b)\le K}}\frac{4^{\omega(b)}}b
\le u^{-K}\prod_{\ell<Z}(1+4u/\ell)
\ll_c\lambda^{\eta(c)},\qquad u=c/4.
\tag{2}
$$

The products here and below are over primes. This uses $0<u<1$ and prime Mertens. The part $b>N^{1/10}$ is uniformly $O_{\gamma,J}(NL^{-J})$ in squared energy: an absolute coefficient is at most $\tau(b)\tau(m/b)$, and $\sum_{n\le x}\tau(n)^2\ll x(1+\log x)^3$. Rankin at $1/\lambda$ bounds the large-$b$ reciprocal sum with weight $4^{\omega(b)}$ by $O(\lambda^4e^{-L/(10\lambda)})$, as in the [previous mask proof](weak-s-type-ii-critical-prime-few-small-prime-slots.md#1-exact-allocation-and-its-reciprocal-moment). Thus the positive method already proves the genuinely unassigned range $c=7/10$, since $\eta(7/10)<2$, but not the typical count $c=1$. In (1), the use of signs for the *long*-lcm correction is what changes the needed exponent in this part from $2$ to $3$.

## 2. Retain the signed sum of all allocations at fixed small part

Fix $b\le N^{1/10}$, let $v=m/b$, $Y=N/b$, and $p=P^-(b)\le W$. In each allocation $r=r_Z(d)\mid b$, the two rough partners are $h=d/r$ and $h'=k/(b/r)$, with $hh'=v$. They exceed $N^{.39}$ on true support because $d\ge X$ and $k>t$. In each single branch split the divisor $h$ at $h\le\sqrt v$. On the other half use $\mu(h)=\mu(v)\mu(h')$ on the true squarefree support and switch to $h'$. Thus the common factor $\mu(v)$ is independent of the allocation. Cauchy across the three branches and the two orientations costs only an absolute factor; **do not** use Cauchy across allocations at this step.

For a fixed branch and orientation the integer sum whose square is taken is

$$
\sum_{r\in\mathcal R(b)}\mu(r)\sum_{\substack{a\mid v\\ a\in J_r(v)}}\mu(a),
\tag{3}
$$

where $\mathcal R(b)$ restricts $r$ by the branch's condition $p\mid r$ or $p\nmid r$. The other tests stay in the true interval $J_r(v)$. All $v$ lie in an interval $\Omega\subset[7Y/16,Y/2)$, and $a\le\sqrt v$ (strict after the exchange). Each $J_r(v)$ lies in an $r$-dependent envelope $[H_r/(C p),H_r]$, where $N^{.39}\le H_r\le\sqrt Y$ on a nonempty piece, because one of $d,k$ is restricted to a fixed ratio-$p$ interval and $v\asymp Y$. For each allocation the sharp tests are intersections of separate intervals in $a$ and $v/a$, together with this square-root inequality. In particular for fixed $a$ their allowable real $v$ form an interval.

For later use there is also a **common** test at each fixed $m=bv$ and single branch: all its allowed $d$ lie in the same interval of ratio at most $C p$, independent of $r$. In branches 1 and 2 this follows directly from the failed endpoint; in branch 3 use $t<k\le pt$, equivalently an interval of the same ratio for $d=m/k$. The exact $d$ for a short variable $a$ is $r a$ in the direct orientation and $r v/a$ in the exchanged one. Thus if $a$ is allowed for two allocations in the same branch and orientation, then

$$
|\log(r/r')|\le\log(Cp).
\tag{4}
$$

The original unit and squarefree constraints remain until after squaring (3). Only at that point add nonnegative squares at every $Z$-rough $v\in\Omega$, including nonsquarefree ones. Throughout, $Z$-rough means every prime factor is at least $Z$, with $1$ included.

## 3. Signed main and signed long-lcm transfer

Use the ordinary rough bounds and short-lcm Bonferroni approximations of the signed predecessor at the same fixed $\gamma$: write $V(Z)=\prod_{\ell<Z}(1-1/\ell)\asymp1/\lambda$, $U_p=1+\log p$, and choose $Q=Z^{O_D(1+L_2)}=Y^{o(1)}$ with a sufficiently large constant for fixed $D$. For any fixed $r,r'$ and rough $a,a'$ with $l=[a,a']\le Y/Q$, count the allowable rough $v=lz$ by the continuous density $V(Z)\,dv/l$. The interval in $v$ at fixed $a,a'$ is an intersection of intervals from §2. The total discrepancy at this pair of allocations is $O_{\gamma,D}(Y L^{3-D})$ by the Bonferroni floor error and the three harmonic variables in $l=gxy$, $a=gx,a'=gy$. The same estimates give a ratio-$O(p)$ harmonic interval bound $O(U_p/\lambda)$ for rough integers **greater than one**, and the rough reciprocal sum up to $Q$ is $O(1+L_2)$ including $1$.

Consider $l>Y/Q$ for this fixed $r,r'$. In both the true count and its continuous main, $v=gxyz$, $1\le z<Q$, and $x,y>1$: $a,a'\le\sqrt v$ implies $l\le v$, and $x=1$ or $y=1$ would make $l$ one short divisor, at most $\sqrt Y$. The largest of $g,x,y,z$ is among $g,x,y$, since $z<Q=Y^{o(1)}$ and $v\asymp Y$. Partition into these three largest cases with any fixed deterministic priority on ties. In the $g$-largest case take absolute weights. At fixed $z$, the $x$ and $y$ gates have ratio $O(p)$, since $xz=v/a'$ and $yz=v/a$ and the two envelopes can be different but each of ratio $C p$. The rough integer $g$ is counted up to $Y/(xyz)$ with density bound $O(1/\lambda)$: this upper cutoff is $\gg Y^{1/4}\gg Z$ on nonempty tuples. Each of $x,y>1$ supplies a factor $O(U_p/\lambda)$ by its narrow reciprocal interval, and $z$ contributes $O(1+L_2)$ from the rough harmonic sum up to $Q$. Thus the bound is

$$
O\bigl(Y\,U_p^2(1+L_2)/\lambda^3\bigr).
\tag{5}
$$

For the continuous main change variables exactly from $dv/l$ to $dz$. The density is $V(Z)$, so the shared harmonic integral is also $O(1+L_2)$. The largest integer $g$ is counted as before, yielding the same (5).

In the $x$-largest case retain the sign $\mu(x)$: on nonzero support the true divisor weights satisfy

$$
\mu(gx)\mu(gy)=\mu(g)^2\mu(x)\mu(y),\qquad (x,gy)=1,\quad (g,y)=1.
$$

At fixed $g,y,z$, every exact test on $x$ defines an interval: $v=g y z x$ is linear in $x$; the four tested arguments $a,a',v/a,v/a'$ are respectively $gx,gy,yz,xz$; the two short inequalities are $gx\le yz$ and $gy\le xz$, with the inherited strictness. The conditions $l>Y/Q$, largest coordinate and its tie order are interval tests as well. The same is true at each fixed real $z$ in the continuous model. All feasible $x$ in such an interval are $\gg Y^{1/4}$, and upper cutoff $Y/(gyz)\le N$. Uniformly for $u\gg N^{.2}$, $u\le N$, $h\le N^2$ one has the **ordinary**, not reciprocal, masked Mertens bound

$$
\sum_{\substack{x\le u,\ x\ Z\text{-rough}\\(x,h)=1}}\mu(x)
 =O_{\gamma,D}(u L^{-D}).
\tag{6}
$$

Indeed remove primes in $\mathscr S=\{\ell<Z\text{ or }\ell\mid h\}$ by the exact reciprocal-zeta coefficient convolution, so the left side is $\sum_{e\le u;\,P(e)\subset\mathscr S} M(u/e)$, with $M(x)=\sum_{n\le x}\mu(n)$. The [unconditional effective ordinary Mertens estimate](https://arxiv.org/pdf/2208.06141v5#page=5) (Lee--Leong, Theorem 2.2 (19), shrinking the exponent constant to absorb logarithms) handles $e\le\sqrt u$. For $e>\sqrt u$, use $|M(u/e)|\le u/e$ and Rankin at $1/\lambda$: the shifted reciprocal Euler product is $O_\gamma(\lambda)$ and the factor $u^{-1/(2\lambda)}$ beats every fixed power of $L$. The product estimate below $Z$ follows by Chebyshev and Mertens at shift $1/\lambda$; primes $\ge Z$ dividing $h$ are at most $2L/\lambda$ in number and add $O(L/(\lambda Z))$ to the logarithm. The same product at zero shift is also $O(\lambda)$. This proves (6) and, by differences of prefixes, an interval bound $O(Y L^{-D}/(gyz))$ for the exact feasible interval; taking or omitting its endpoints costs at most $O(1)$, absorbed since the feasible scale is polynomially large. Therefore summing over $g,y$ and the discrete $z$ costs $O(YL^{3-D})$ even by unrestricted harmonic sums on the other variables. In the continuous main, $dv/l=dz$ has constant density independent of $x$ at fixed $z$, so integrating $1/z$ over $[1,Q]$ gives the same error bound. Largest $y$ is symmetric.

We may consequently replace the short-lcm main by the full signed continuous lcm form, at total error per fixed $r,r'$ of (5) and a negligible power-log term; (5) includes both long corrections. The cancellation (6) is performed *before* bounding the larger-coordinate sums absolutely, and does not average over targets or aliases.

## 4. The positive form and its one common-divisor atom

At fixed real $v$ the full continuous lcm form for (3), before density $V(Z)$, is exactly

$$
\sum_{\substack{g\ Z\text{-rough}\\g\le \sqrt Y}}
  \frac{\varphi(g)\mu^2(g)}{g^2}
 \left|\sum_{r\in\mathcal R(b)}\mu(r)
   \sum_{\substack{x\in J_r(v)/g,\ x\ Z\text{-rough}\\(x,g)=1}}\frac{\mu(x)}x
 \right|^2 .
\tag{7}
$$

This is the identity $\gcd(a,a')=\sum_{g\mid a,a'}\varphi(g)$ and completing the inner square. Separate $x=1$ from $x>1$ at an absolute factor two, keeping the aggregate across allocations in the atom. For $x>1$, per $r$ the signed reciprocal prefix bound of the [predecessor, §2](weak-s-type-ii-critical-prime-signed-all-rough-exponents.md#2-inputs-for-a-fixed-signed-square) gives a negligible contribution when $g<H_r/(2Cp\Xi)$, $\Xi=Z^{O_D(1+L_2)}=N^{o(1)}$. For larger $g$, the $g$ harmonic mass is $O(1+L_2)$ and the inner $x>1$ sum is $O(U_p/\lambda)$ by its narrow ratio. Cauchy may now be used just on these $x>1$ terms, giving a bound $O(4^{\omega(b)}\,U_p^2(1+L_2)/\lambda^2)$ for this part of (7), up to negligible power-log error. Thus it has the same integrated estimate as (5) summed over allocation pairs.

In the atom, a pair $r,r'$ must have $g\in J_r(v)\cap J_{r'}(v)$, which forces (4). The common $g$ interval, containing only $g>1$, has harmonic mass $O(U_p/\lambda)$, by either one of its narrow envelopes. Define 

$$
A_b(B)=\#\{r,r'\mid b:\ |\log(r/r')|\le B\},\qquad B=\max(1,\log(CW)).
$$

After integrating with $V(Z)$, the atom is bounded by $O(Y U_p A_b(B)/\lambda^2)$. The signs of competing atoms need not be estimated. Thus the signed arithmetic remaining in (7) has reduced the large loss to a positive *close-allocation* count, not all allocation pairs.

## 5. Close-allocation moment through the typical count

For a squarefree $b$ and $r,r'\mid b$, partition its primes into those in both, neither, only $r$, and only $r'$. This expresses their ratio as $i/j$, with disjoint squarefree differing factors $i,j$. Tilt by $2^{K-\omega(b)}$ on $\omega(b)\le K$. The reciprocal sum for both and neither statuses costs at most $\prod_{\ell<Z}(1+1/(2\ell))^2\ll\lambda$, after dropping coprimality with the other factors. Keeping $i,j\le N$ (automatic for $b\le N^{1/10}$) and even dropping their rough prime mask and mutual coprimality, obtain

$$
\sum_{\substack{b\le N^{1/10},\ b\ {\rm squarefree}\\P^+(b)<Z,\ \omega(b)\le K}}
       \frac{A_b(B)}b
 \ll 2^K\lambda
 \sum_{\substack{i,j\le N\\|\log(i/j)|\le B}}\frac{f(i)f(j)}{ij},
 \qquad f(n)=\mu^2(n)\,2^{-\omega(n)} .
\tag{8}
$$

Here the two dropped restrictions only enlarge nonnegative sums.

For completeness the needed elementary short log-bin estimate uses no distribution of primes in short intervals. On squarefree $n$, $\log n=\sum_{\ell\mid n}\log\ell$ and $f(\ell m)=f(m)/2$ if $(\ell,m)=1$. Thus for $x\ge3$,

$$
\sum_{n\le x} f(n)\log n
\le \frac12\sum_{m\le x}f(m)\sum_{\ell\le x/m}\log\ell
\ll x\sum_{m\le x}f(m)/m
\ll x(\log x)^{1/2}
$$

by Chebyshev and the positive reciprocal Euler product. It follows by separating $n\le\sqrt x$ that $\sum_{n\le x}f(n)\ll x(\log x)^{-1/2}$. Hence a unit log-bin at ordinate $j$ has reciprocal weight $O((1+j)^{-1/2})$. Partition the log-coordinate into width-$B$ bins indexed by $k\ge0$. Their weights are $O(\sqrt{B/(k+1)})$ by summing unit bins; the first uses the Euler bound up to $e^B$. The near condition in (8) only connects the same or adjacent bins (allowing at most a fixed extra neighbor on endpoints). Summing squared bin weights up to $\log N$ shows the double reciprocal sum is $O(B(1+L_2))$. Therefore (8) is

$$
O\bigl((1+\log W)(1+L_2)\lambda^{1+c\log2}\bigr).
\tag{9}
$$

Sum the atom bound from §4 by (9), and (5) and the nonatom main by (2), with $Y=N/b$ and $U_p\le1+\log W$. All power-log errors after the allocation and $b$ sums are negligible by choosing $D$ sufficiently large; the full reciprocal allocation envelope is $O(\lambda^4)$ by $\prod_{\ell<Z}(1+4/\ell)$. Include the $b>N^{1/10}$ tail from §1. Parseval gives (1). The exponent $\eta(c)$ increases on $0<c<4$ and $\eta(3/2)<3$; also $1/\log2<3/2$. Both powers in (1) are therefore negative. Restriction to the disjoint critical arcs and separate numerator centering each contract ordinary $L^2$, while the genuine fixed prime box has squared ordinary norm $O(N)$ by unique prime pairs from the disjoint intervals, even with the fixed general selector. Cauchy with the exact phase $e(-N\alpha)$ gives the stated full and centered signed pairings on all numerators, moduli and aliases.

## 6. Actual support and the remaining high-count range

Take $N$ along large powers of two, $W=3$, $I_0=[X,2X]$, $t=N^{.49999}$ and $y=9N/16$. For every odd prime $q_0\ge5$ below $Z$, there is an actual branch-1 term with this prime in the small part of $d$: set $d=3q_0 g$, $k=h$, with primes $g,h$ selected to put $d\in[1.05X,1.06X]$, $k\in[.43X,.44X]$. There is also one with the same $q_0$ in the small part of $k$: set $d=3g'$, $k=q_0 h'$, fitting the same intervals. Proportional prime intervals work uniformly here since $q_0<N^{o(1)}$; choose distinct rough partners above $Z$, all are $N$-units, and $p=3$, $d/3<X$. In both configurations $b=3q_0$ is included for large $N$. Consequently no *single* pair of alphabets satisfying the small-overlap condition of the [two-sided result](weak-s-type-ii-critical-prime-two-sided-small-prime-alphabets.md) can contain this genuine sector: its overlap would have to contain all odd primes $q_0\ge5$ below $Z$.

The same construction may give many factors to both legs, not only two in $b$. For example take $\gamma=1/2$ and $J_0=\lfloor17\log\lambda/50\rfloor$; take two distinct primes for each of the disjoint intervals $[\exp(L^{j/(2(J_0+1))}),4\exp(L^{j/(2(J_0+1))})]$, $1\le j\le J_0$, by applying Bertrand twice. Assign one prime from each interval to each side, and append $3$ to the $d$ side. Their total count is $1+2J_0\le (7/10)\log\lambda$ eventually, so this already occurs in the elementary unrestricted range of §1, and in (1) whenever $c\ge7/10$. Their small parts have subpower product, so two more distinct rough primes fit the same $d,k$ intervals by the prime number theorem, with the same sharp masks and nonzero sign. For every fixed older exponent $\gamma'\in(0,1)$, the $d$ side contains a prime at an exponent in a fixed subinterval of $(\gamma'/3,\min(\gamma',1/2))$ for sufficiently large $N$. Thus its exact old small part exceeds the earlier magnitude cutoff $\log R=O(L^{\gamma'/3})$. For $\gamma'\le1/2$, counting exponents below $\gamma'/2$ gives at least $(.17\gamma'+o(1)) L_2$ factors below $\exp(L^{\gamma'})$ on each side; for $\gamma'>1/2$ it includes all $J_0\sim .17 L_2$. Both beat the previous $(\gamma'/6)L_2$ slot cap. These are genuine support statements, not lower bounds for the signed statistic.

Under the reciprocal weight $1/b$ on squarefree products of primes below $Z$ normalized to a probability measure, the mean of $\omega(b)$ is $\log\lambda+O(1)$ and its variance is $O(\log\lambda)$, directly by independent prime choices. Thus $1<c<1/\log2$ indeed reaches the ordinary reciprocal Euler typical count, but this model is not a bound on the true signed contribution of the discarded actual high counts. Those terms, the remaining full critical covariance, and weak S are not resolved here.
