# The true signed critical boundary reaches a logarithmic rough cutoff

Keep the genuine fixed-target critical-shell prime polynomial $P$, with arbitrary fixed $|E(u,v)|\le1$ and its original possibly active product gate, and the three actual signed least-prime boundaries as in the [signed stretched-exponential proof](weak-s-type-ii-critical-prime-signed-all-rough-exponents.md). Thus $N$ is even, $X=\sqrt N$, $d\in I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le m=dk<N/2$, $(m,N)=1$, and the nonzero weight is $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. All the original sharp tests and the actual least prime $p=P^-(m)$ are retained. Put $L=\log N$, $L_2=\log L$, $L_3=\log L_2$.

Fix $a>0$, $B\ge1$ and $C_0>0$. Use any real threshold $Z$ with

$$
aL_2\le\lambda:=\log Z\le C_0 L_2^B .
$$

Write $r_Z(s)$ for the product of prime factors strictly below $Z$ in a squarefree $s$. Let $\mathcal A$ be an arbitrary collection of squarefree products of primes below $Z$, allowed to depend on the target and not on the rational point. Retain the true boundary terms whose $r_Z(d)$ lies in $\mathcal A$ and whose $p$ is at most $W$, where $2\le W<Z$; write their polynomial as $D_{\mathcal A,W}$. No size or arity cap is imposed on $\mathcal A$. As in the [allocation moment](weak-s-type-ii-critical-prime-few-small-prime-slots.md), write $\mathcal M(\mathcal A)=\sum_{r,r'\in\mathcal A}1/[r,r']$.

For every fixed $J>0$, unconditionally and uniformly in all the above choices,

$$
\int_0^1 |D_{\mathcal A,W}(\alpha)|^2\,d\alpha
\ll_{a,B,C_0,J}
 \frac{N\,\mathcal M(\mathcal A)(1+\log W)(1+L_2/L_3)}{\lambda}
 +N L^{-J}. \tag{1}
$$

The sum of the absolute values of its full and double-centered **signed** pairings with the true $P$ over the entire critical-prime shell is $O(\sqrt N)$ times the square root of the right side. For example, $Z=L^a$ now gives $o(N)$ at each sufficiently large even $N$ whenever $\mathcal M(\mathcal A)(1+\log W)=o(L_3)$; this includes fixed $W$ and a fixed size cap $r_Z(d)\le R$. For $R,W$ any fixed powers of $L$, the choice $Z=\exp(L_2^5)$ gives the same $o(N)$ conclusion. No zero hypothesis or exceptional-target deletion is used.

## 1. Full small part and exact short divisor geometry

Put $b=r_Z(m)$, $v=m/b$, and $r=r_Z(d)\mid b$ on true squarefree support. Thus $d=rh$, $k=(b/r)c$, $hc=v$, and $v$ is squarefree with no prime factor below $Z$. The least-prime label $p\le W<Z$ is fixed by $b$. For $b\le N^{1/10}$ the two genuine rough partners $h,c$ are both at least $N^{.39}$, since $h=d/r\ge X/b$ and $c>t/b$. The weight $\mu(r)\mu(h)$ retains its sign; on the long half $h>\sqrt v$ use $\mu(h)=\mu(v)\mu(c)$ and switch to the short coordinate. The inherited short-divisor interval $J(v)\subset(1,\sqrt v]$ for each branch and orientation obeys the identical exact geometric conditions of the signed predecessor: all $v$ lie in a fixed $\Omega\subset[7Y/16,Y/2)$ with $Y=N/b$, each fixed divisor has an interval of allowable $v$, and all $J(v)$ lie in a fixed $[H/(C p),H]$, where $N^{.39}\le H\le\sqrt Y$ on a nonempty piece and $C$ is absolute. This follows from the failed endpoint test in types 1/2, or $t<k\le pt$ in type 3, including after complementing using $v\asymp Y$. No rounding of an actual interval is used. On squarefree $m=bv$ these changes preserve all stated original gcd, unit and squarefree masks through the signed square. Only then can one add nonnegative squares over all $Z$-rough $v\in\Omega$.

The large-$b$ portion $b>N^{1/10}$ is negligible at every fixed power of $L$, exactly as in the allocation-moment proof: $|\text{coefficient at }bv|\le\tau(b)\tau(v)$, $\sum_{v\le x}\tau(v)^2\ll x(1+\log x)^3$, and Rankin at $1/\lambda$ bounds the squarefree $Z$-small sum $\sum_{b>N^{1/10}}4^{\omega(b)}/b$ by $O(\lambda^4 e^{-L/(10\lambda)})$. This is uniform here since $\lambda\le C_0 L_2^B$. Thus only $Y\ge N^{9/10}$ is needed below.

## 2. Narrow-cutoff rough counts and the exact gcd mask

Use the uniform elementary rough count of the [unsigned stretched-rough proof](weak-s-type-ii-critical-prime-stretched-rough-boundary-second-moment.md#1-absolute-dyadic-rough-count-including-the-small-endpoint). In particular, if $U_p=1+\log p$, a ratio-$O(p)$ interval has harmonic mass $O(U_p/\lambda)$ on $Z$-rough integers greater than one, and including one costs $O(1+U_p/\lambda)=O(1)$. The corresponding unrestricted mass up to $N$ is $O(L/\lambda)$.

Fix a large error exponent $D>0$. For the signed long-lcm proof it suffices to change the two auxiliary scales to

$$
j\asymp_{B,C_0,D} 1+L_2/L_3,\quad j\ \text{even},\qquad
Q=Z^{2(j+2)},\qquad
\Xi=Z^{C_{a,B,C_0,D}(1+L_2/L_3)} . \tag{2}
$$

Indeed prime Mertens gives $\sum_{\ell<Z}1/\ell=O_{B,C_0}(L_3)$. For even/odd Bonferroni order $j,j+1$, Stirling bounds the density gap by $O_D(L^{-D})$ by increasing the constant in $j$. The total interval floor error is at most $O(Z^{j+1})$, since all included squarefree moduli are at most $Z^{j+1}$. Thus for a real interval $A$ counting positive rough integers gives

$$
\#\{z\in A:z\text{ positive integer and $Z$-rough}\}
=V(Z)|A|+O_{B,C_0,D}(|A|L^{-D}+ Z^{j+1}),
\quad V(Z)=\prod_{\ell<Z}(1-1/\ell)\asymp1/\lambda .
$$

Here and below products over $\ell$ are over primes. In particular $\log Q=O_{B,C_0,D}(L_2^{B+1}/L_3)=o(L)$, so $Q=Y^{o(1)}$, and $Z^{j+1}\ll (Y/l)L^{-D}$ whenever an lcm $l\le Y/Q$.

For the signed prefix it is essential to keep the joint prime mask rather than omit the $g$-coprimality crudely. Put $\mathscr S=\{\ell:\ell<Z\text{ or }\ell\mid g\}$ with $g\le N$, $T=\max(Z,L)$ and $\delta=L_3/(2\log T)$. The exact reciprocal-zeta convolution gives

$$
\sum_{\substack{h\le u,\ h\ Z\text{-rough}\\(h,g)=1}}\frac{\mu(h)}h
=\sum_{\substack{b'\le u\\\ell\mid b'\Rightarrow\ell\in\mathscr S}}
 \frac{M_1(u/b')}{b'},\qquad M_1(x)=\sum_{n\le x}\mu(n)/n .
$$

One has $\log T\ll_a\lambda$. At zero shift the total reciprocal Euler product on $\mathscr S$ is $O(\log T)$, by prime Mertens below $T$ and the bound $L/\log T$ for the number of $\ell>T$ dividing $g$. At positive shift,

$$
\prod_{\ell\in\mathscr S}(1-\ell^{-1+\delta})^{-1}
\ll \log T\,\exp(O(\sqrt{L_2}\,L_3)).
\tag{3}
$$

For $\ell\le T$, compare at zero shift using $\ell^\delta-1\le\delta e^{\delta\log T}\log\ell$ and $\sum_{\ell\le T}(\log\ell)/\ell\ll\log T$; the higher powers are uniformly summable. The large primes cost at most $O((L/\log T)T^{-1+\delta})=O(\sqrt{L_2}/\log T)$ in the logarithm of the product. Thus (3) is $\exp(o(L_2))$ up to its indicated uniform constants.

The [effective Mertens bound of Lee–Leong, Theorem 2.2 (19)](https://arxiv.org/pdf/2208.06141v5#page=5) by Abel summation gives convergence of the infinite harmonic Möbius sum; its value is zero by $1/\zeta(s)$ as $s\downarrow1$. Summing its tail gives $M_1(x)=O(\exp(-c(\log x)^{3/5}(\log\log x)^{-1/5}))$ for large $x$, and $M_1$ is bounded everywhere. In the convolution, $b'\le\sqrt u$ contributes $O_{a,B,C_0,D}(L^{-D})$ when $u\ge\Xi$: there $\log u\gg_a L_2^2/L_3$, so the ordinary decay exponent dominates $L_2$. For $b'>\sqrt u$ use the factor $u^{-\delta/2}$ times (3); a sufficiently large constant in $\Xi$ gives the same power-log bound because $\log T\ll_a\lambda$. This proves the required signed prefix uniformly for $\Xi\le u\le N$ and $g\le N$, including every omitted prime divisor of $g$. A difference of prefixes treats intervals wholly above $2\Xi$ with arbitrary open/closed endpoints.

## 3. Verify the unchanged lcm proof at the new scales

Apply the signed predecessor's short-divisor argument, retaining the following quantitative changes. For $[h,h']\le Y/Q$, the above floor/density approximation gives the full signed lcm main with absolute cumulative error $O(Y L^{3-D})$ by the three harmonic variables of $[h,h']=gxy$, $h=gx,h'=gy$. In the complementary long range write $v=gxyz$. Because $h,h'$ are short, $1\le z<Q$ holds even for the continuous model, and $x,y>1$ before coprimality is dropped (otherwise the lcm is one short divisor). Count the largest of $g,x,y$ at density $O(1/\lambda)$ after keeping the same two-sided gates $gx,gy\in[H/(Cp),H]$ and $xz,yz\in[cY/H,C'pY/H]$. Its upper-bound length is $\gg Y^{1/4}>Z$ on feasible tuples, since $z<Q=Y^{o(1)}$ cannot be largest. If $g$ is largest, the $x,y$ gates cost $O(U_p^2/\lambda^2)$ and the free $z$ harmonic is $O(1+\log Q/\lambda)$. If $x$ is largest, use $gy,yz$: the shared $y$ ranges over relative ratio $O(pQ)$ and costs $O(1+\log Q/\lambda)$, as $\log p\le\lambda$. In the discrete count $g=z=1$ is impossible before dropping $(x,y)=1$, since both short divisors would force $x=y$; in the continuous count $z$ carries $V(Z)\,dz/z$. Thus the two narrow gates together cost $O(U_p/\lambda)$ in either case. Largest $y$ interchanges $x,y$. Since $\log Q/\lambda=O(1+L_2/L_3)$ and $U_p\ll\lambda$, both actual and continuous long-lcm corrections are

$$
O\!\left(Y U_p(1+L_2/L_3)/\lambda^2\right).
$$

In the full positive signed lcm form use the exact $\gcd$ expansion (the [signed predecessor, §4](weak-s-type-ii-critical-prime-signed-all-rough-exponents.md#4-the-signed-positive-form-and-summation)). When $g<H/(2Cp\Xi)$ the entire inner interval is above $2\Xi$ and the joint gcd prefix from §2 applies. On the other $g$ range, its harmonic mass is $O(1+\log\Xi/\lambda)=O(1+L_2/L_3)$. Extract the $x=1$ atom, possible only for $g\in J(v)\subset(1,\sqrt v]$, costing $O(U_p/\lambda)$; the $x>1$ terms contribute $O(U_p^2(1+L_2/L_3)/\lambda^2)$. Integration in $v$ with $V(Z)$ and addition of the two corrections prove the per-allocation signed squared bound $O_{a,B,C_0}(Y U_p(1+L_2/L_3)/\lambda^2)$. All negligible errors are absorbed by choosing $D$ in (2) sufficiently large.

At fixed $b$, Cauchy across the allowed allocations $r\mid b$, $r\in\mathcal A$ incurs their number, so summing the squared bounds asks for the sum of their squared number divided by $b$. Expanding two labels $r,r'$ and imposing $[r,r']\mid b$ bounds that sum by $\mathcal M(\mathcal A)\prod_{\ell<Z}(1+1/\ell)\ll\lambda\mathcal M(\mathcal A)$. This and disjoint $b$ prove (1). Restricting to the disjoint critical arcs and separately centering each nonzero numerator array are contractions in ordinary $L^2$. The fixed prime box has squared ordinary norm $O(N)$; Cauchy with the exact phase $e(-N\alpha)$ proves the signed estimates for all original moduli and aliases.

## 4. Nonzero new terms invisible to the older cutoffs

Take large $N$ along powers of two, $Z=L^2$, $W=3$, and $\mathcal A=\{3\}$. By the prime number theorem select $M=\lfloor L/(10\log(4Z))\rfloor$ distinct primes in $[2Z,4Z]$, and let $B_1$ be their product, so $B_1=N^{1/10+o(1)}$. Select a prime $g\in[1.05X/(3B_1),1.06X/(3B_1)]$ and a prime $k\in[.43X,.44X]$. Put $d=3B_1g$, $I_0=[X,2X]$, $t=N^{.49999}$ and $y=9N/16$. Then $N-y<dk<N/2$, all factors are distinct odd primes and $N$-units, and $p=r_Z(d)=3$, $d/3<X$. This is a genuine nonzero branch-1 term. Its old small part at every fixed $Z'=\exp(L^{\gamma'})$, $0<\gamma'<1$, contains $B_1$: neither the previous subpower size cutoff nor the previous $O(L_2)$ slot cap includes it. The example proves actual new coverage, not a lower bound for a signed sum.

The theorem does not estimate the full dense small-part residual, the general pointwise critical covariance, or weak S.
