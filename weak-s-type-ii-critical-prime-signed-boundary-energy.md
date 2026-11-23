# Signed boundary energy reaches every fixed positive logarithmic exponent

Keep the actual prime box $P$, exact complementary polynomial $D$, and the full and double-centered critical-shell pairings $\mathcal I(P,F),\mathcal C(P,F)$ of the [least-prime boundary reduction](weak-s-type-ii-critical-prime-least-prime-boundaries.md). In particular, $N$ is even, $L=\log N$, $X=\sqrt N$, $y\le9N/16$, $I_0=I_d\cap[X,\infty)$ with its actual endpoints, and $k>t\ge N^{.49999}$. The product $m=dk$ is in $[N-y,N/2)$, with $(m,N)=1$ and true weight $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. The prime selector $|E(u,v)|\le1$ and sharp cuts are fixed independently of $q,\beta$.

Fix $0<\theta<1$, put $L_2=\log L$ and $Z=\exp(L^\theta)$. Let $D^{>Z}$ keep all original common coefficients on $P^-(m)>Z$, and let $D_{\partial,\le Z}$ be the exact three signed boundary classes on the remaining products. Then, unconditionally,

$$
\int_0^1|D^{>Z}(\alpha)|^2\,d\alpha
 \ll_\theta \frac{N L_2}{L^\theta}.
\tag{1}
$$

Consequently

$$
\begin{split}
 &|\mathcal I(P,D)-\mathcal I(P,D_{\partial,\le Z})|
 +|\mathcal C(P,D)-\mathcal C(P,D_{\partial,\le Z})|\\
 &\hspace{45mm}\ll_\theta N\sqrt{L_2/L^\theta}.
\end{split}
\tag{2}
$$

All moduli, numerators and aliases of the critical shell are included. The three remaining signed bands have multiplicative width at most $\exp(L^\theta)$ in their stated original variables. The [absolute two-gate estimate](weak-s-type-ii-critical-prime-boundary-two-gate-energy.md) required $\theta>1/2$ for a saving; the new proof uses the remaining Möbius signs in the boundary energy. It does not bound the signed dense covariance of the low-least-prime bands.

## 1. The exact signs and short divisor windows

For a fixed least prime $p$ write $m=pn$, $Y=N/p$. Then $n$ is squarefree and $p$-rough, meaning that it has no prime factor $\le p$. The prime exchange in the preceding reduction is exact for every $p$, even above $Z$. Each of the three unpaired parts at this $m$ is of the form

$$
 \epsilon_i(n)\sum_{a\mid n}\mu(a)\mathbf1_{a\in I_i}\mathbf1_{n/a\in J_i},
 \qquad |\epsilon_i(n)|=1,
\tag{3}
$$

where the following sets are intervals with the inherited endpoint conventions:
1. $a=d/p$, $I_1=\{a>0:pa\in I_0,\ a\notin I_0\}$, $J_1=(t,\infty)$, and $\epsilon_1=-1$. This $I_1$ lies in $[A/p,A]$ where $A=\inf I_0$; the failed test for $a$ is necessarily at its lower endpoint.
2. $a=d$, $I_2=\{a\in I_0:pa\notin I_0\}$, $J_2=(t/p,\infty)$, and $\epsilon_2=1$. If nonempty, $I_2$ lies in $[U/p,U]$ where $U=\sup I_0<\infty$; the failed test is at its upper endpoint.
3. $a=k/p$, $I_3=(t/p,t]$, $J_3=I_0\cap(I_0/p)$, and $\epsilon_3=\mu(n)$, since $\mu(d)=\mu(n)\mu(a)$ for squarefree $n$.

All original $m$ constraints and unit masks persist in (3). Each nonempty $I_i$ is contained in an interval $[H/p,H]$ with $H=A,U,t$ respectively. For each of the three sums, split into $a\le\sqrt n$ and $a>\sqrt n$. On the latter replace $a$ by $b=n/a<\sqrt n$ and use $\mu(a)=\mu(n)\mu(b)$. Squaring the sum of at most six pieces costs a factor at most six. In each square the common signs disappear, and at this point only, one may drop the squarefree and $N$-unit restrictions on $n$ for an upper bound, extending the resulting nonnegative squares to all $p$-rough $n$.

For either orientation the needed moment is thus a sum of squares of $\sum_{a\mid n,\ a\in J(n)}\mu(a)$, with $n$ in the original interval $\Omega=[(N-y)/p,N/(2p))\subset[7Y/16,Y/2)$, and with these properties:
- for each real $n\in\Omega$, $J(n)$ is a contiguous interval of allowed positive real divisors, bounded above by $\sqrt n$ (strict on the complemented piece);
- for each fixed integer $a$, the set of real $n\in\Omega$ for which $a\in J(n)$ is an interval;
- all these $J(n)$ lie in one fixed envelope $[H_0/(C p),H_0]$ for an absolute $C$.

Indeed, the first orientation requires $a\in I_i$, $n/a\in J_i$, $a\le\sqrt n$. The second exchanges $I_i,J_i$ and uses $a<\sqrt n$. These are interval conditions in either variable separately. In the complemented orientation $n/a$ lies in the narrow interval $[H/p,H]$ and $7Y/16\le n<Y/2$, so the new envelope can be $[7Y/(16H),pY/(2H)]$. This preserves the moving endpoints rather than replacing the signed interval by its envelope. The envelope is used only for estimates.

## 2. Rough harmonic control and an elementary rough density

Write $V(p)=\prod_{\ell\le p,\ \ell\ {\rm prime}}(1-1/\ell)\asymp1/\log p$. We use the elementary bounds from the two-gate estimate: the number of $p$-rough integers up to $B\ge p$ is $O(B/\log p)$, and the reciprocal sum of $p$-rough integers in an interval of ratio at most $R\ge1$ is

$$
O\!\left(1+\frac{\log R}{\log p}\right).
\tag{4}
$$

The factor one is allowed in rough sums. The latter bound follows from the former by partial summation starting at $\max(p,\text{lower endpoint})$, treating one separately. The unrestricted harmonic sum up to $N$ is $O(L/\log p)$ by prime Mertens.

For later uniformity choose any fixed $\theta'$ with $\theta<\theta'<1$ and $2\theta'-1>\theta$, for example $(3+\theta)/4$. For now take

$$
\exp(L^\theta)<p\le \exp(L^{\theta'}).
$$

Choose a large fixed $B$, say $B=20$, and a sufficiently large even $r\asymp_B L_2$. By upper and lower elementary Bonferroni truncation, for every real interval $\mathcal Z$ of nonnegative numbers the count of positive $p$-rough integers in it is

$$
 V(p)|\mathcal Z|+O_B\bigl(|\mathcal Z|L^{-B}+p^{r+1}\bigr).
\tag{5}
$$

Here the even order $r$ and odd order $r+1$ truncate at the number of prime factors $\le p$. For the main densities, the gap between the two truncations is at most $(\sum_{\ell\le p}1/\ell)^{r+1}/(r+1)!\ll_B L^{-B}$ by Stirling and $\sum_{\ell\le p}1/\ell=O(L_2)$. For the integer count, each squarefree divisor uses at most $r+1$ primes $\le p$, so the accumulated $O(1)$ floor errors are $O(p^{r+1})$. This includes arbitrary open/closed endpoints.

We also require a signed harmonic bound. For each fixed $B$, there is a fixed $C_B$ such that uniformly for $\Xi=p^{C_B L_2}$ and $\Xi\le u\le N$ in the above range of $p$,

$$
\left|\sum_{\substack{a\le u\\a\ p\text{-rough}}}\frac{\mu(a)}a\right|
\ll_{\theta,B} L^{-B}.
\tag{6}
$$

To prove it, let $M_1(u)=\sum_{a\le u}\mu(a)/a$. The effective ordinary Mertens estimate, for example [Lee–Leong, Theorem 2.2 (19)](https://arxiv.org/pdf/2208.06141v5#page=5) for the unweighted summatory function, gives $M_1(u)\ll \exp(-c(\log u)^{3/5}(\log\log u)^{-1/5})$ for sufficiently large $u$ by Abel summation, with a smaller $c$. The full harmonic sum converges to zero by $1/\zeta(s)$ as $s\downarrow1$; in particular $M_1$ is bounded on all $u\ge1$. The exact coefficient convolution for removing primes $\le p$ gives the sum in (6) as

$$
\sum_{\substack{b\le u\\P^+(b)\le p}}\frac{M_1(u/b)}b
$$

with one included. For $b\le\sqrt u$, apply the ordinary bound to $u/b$ and use the total $p$-smooth harmonic sum $O(\log p)$. Since $\log u\ge C_B L_2 L^\theta$, this contribution is $O_{\theta,B}(L^{-B})$. For the remaining $b$, Rankin with $\delta=1/\log p$ gives reciprocal weight

$$
 \ll u^{-\delta/2}\prod_{\ell\le p}(1-\ell^{-1+\delta})^{-1}
 \ll u^{-\delta/2}\log p.
$$

The last Euler product is $O(\log p)$ by comparison with its value at $\delta=0$: $\sum_{\ell\le p}(\ell^\delta-1)/\ell\ll\delta\sum_{\ell\le p}\log\ell/\ell\ll1$, and the higher powers are uniformly bounded. Increasing $C_B$ bounds this tail by $O_B(L^{-B})$, proving (6). If the signed sum additionally restricts $(a,g)=1$ for any $g\le N$, omitting excluded $p$-rough multiples costs at most

$$
\sum_{\substack{\ell\mid g,\ \ell>p\\\ell\ {\rm prime}}}\frac1\ell
 \sum_{\substack{b\le N\\b\ p\text{-rough}}}\frac1b
\ll\frac{L^2}{p(\log p)^2},
\tag{7}
$$

which is negligibly small here. Differences of prefixes prove the same power-log bound for a hard interval entirely above $2\Xi$; this margin also handles open/closed integer cutoffs.

## 3. Signed lcm main, with uniform control of its long tail

For one piece in §1 expand the extended nonnegative square over two $p$-rough integers $a,b$ with weights $\mu(a)\mu(b)$. For fixed $a,b$ put $l=[a,b]$, and write $a=gx,b=gy$, $(x,y)=1$, $l=gxy$. The underlying $n$ must be in the interval where both $a,b\in J(n)$ and be divisible by $l$. As $l$ is itself rough, writing $n=lz$ reduces the count to rough $z$ in a hard real interval. Put $Q=p^{2(r+2)}$, so $Q=Y^{o(1)}$ uniformly in the present prime range. If $l\le Y/Q$, (5) gives main term $V(p)/l$ times the interval length in $n$. Its error is $O_B(YL^{-B}/l)$ since $Y/l\ge Q$. The total of these individual errors is $O_B(YL^{3-B})$, using $\sum_{g,x,y\le N}(gxy)^{-1}\ll L^3$.

We next verify that both the actual count and the would-be full main term in the range $l>Y/Q$ have total absolute weight

$$
 O_\theta(YL_2/\log p).
\tag{8}
$$

For this bound drop signs and coprimality. Both short divisors are at most $\sqrt n$, so $l\le a b\le n$ and hence $1\le z=n/l<Q$. This applies even when $n$ is a continuous variable in the main term. From the fixed envelope in §1 and $n\asymp Y$, the four variables satisfy

$$
 gx,gy \in[H_0/(Cp),H_0],
 \qquad xz,yz\in[cY/H_0,C' pY/H_0],
$$

with absolute $c,C'$. The variable $z<Q=Y^{o(1)}$ cannot be a largest variable, since $gxyz\ge7Y/16$. For each of the other three choices of a largest variable its upper bound is $Y/W$, where $W$ is the product of the other three, and this upper bound is at least $(7Y/16)^{1/4}>p$ on any nonempty tuple. Count that largest integer by $O(Y/(W\log p))$. Keeping two product gates as in the two-gate argument leaves harmonic sums in three variables. If $g$ was largest, use $xz,yz$ and the shared variable $z<Q$; its rough harmonic sum is $O(1+\log Q/\log p)=O(L_2)$. The two gated harmonic sums cost $O(1)$ each. If $x$ was largest, use $gy,yz$ and the shared variable $y$, which now satisfies $cY/(H_0 Q)\le y\le C' pY/H_0$ because $1\le z<Q$. Its rough harmonic sum is again $O(L_2)$, and the two other gated sums cost $O(1)$ each. Largest $y$ interchanges $x,y$. This proves (8) for the discrete count.

For the main term exactly change variables from $dn/l$ to $dz$ at fixed $g,x,y$, and use density $V(p)$ on this continuous $z$. The same bounds apply: where $z$ is shared, its integral against $V(p)\,dz/z$ up to $Q$ is $O(L_2)$, and where it is gated for fixed shared variable the ratio is $O(p)$, giving integral $O(1)$. The counted largest variable remains integral. This proves (8) for the main-term tail as well. Thus we may add the full lcm main term including $l>Y/Q$, while charging (8) for both tails. The short-divisor step is essential to keep the continuous tail at $z\ge1$.

For each real $n\in\Omega$, the full signed lcm form is exactly

$$
\sum_{\substack{a,b\in J(n)\\a,b\ p\text{-rough}}}
 \frac{\mu(a)\mu(b)}{[a,b]}
=\sum_{\substack{g\le\min(H_0,\sqrt N)\\g\ p\text{-rough}}}
 \frac{\phi(g)\mu(g)^2}{g^2}
 \left|\sum_{\substack{x\in J(n)/g\\x\ p\text{-rough},\ (x,g)=1}}
 \frac{\mu(x)}x\right|^2 .
\tag{9}
$$

This follows from $\gcd(a,b)=\sum_{g\mid a,b}\phi(g)$ and completing the inner square before estimating it. If $g\ge H_0/(2Cp\Xi)$, the harmonic sum of these $g$ up to $H_0$ is $O(L_2)$ by (4). Their inner sums in (9) are $O(1)$ by the ratio $Cp$ and (4). For the other $g$, the inner interval is entirely above $2\Xi$, so (6)–(7) bound it by $O_{\theta,B}(L^{-B})$ with $B$ made sufficiently large. Thus the entire form (9) is $O_\theta(L_2)$, uniformly in the moving interval and endpoints. Integrating over $n\in\Omega$ with factor $V(p)$ yields $O_\theta(YL_2/\log p)$. Together with the floor and tail estimates this proves that bound on the whole signed square for a fixed $p$.

## 4. Summation and scope

Sum the last bound over primes $Z<p\le\exp(L^{\theta'})$. Distinct least primes have disjoint supports in the original integer coefficient $m$; the upper bounds were summed only after squaring each coefficient. The prime upper bound gives $\sum_{p>Z}(p\log p)^{-1}\ll1/\log Z$ by partial summation. Thus the ordinary squared energy from this middle range is $O_\theta(N L_2/\log Z)$. For $p>\exp(L^{\theta'})$, the absolute two-gate estimate gives energy $O(NL^{1-2\theta'})$, absorbed by the same bound. This proves (1).

Finally, the prime box has ordinary squared energy $O(N)$ even with the arbitrary fixed selector and active product gate, since the prime factors are from disjoint boxes and each product has a unique such factorization. The critical arcs are disjoint, and subtracting the means in the nonzero numerator coordinates is an orthogonal contraction. Cauchy–Schwarz with (1), and the exact common-coefficient identity $D=D^{>Z}+D_{\partial,\le Z}$, prove (2). No filter involving $q\mid m$ is added to the polynomial or the uncentered sum; such terms merely project to zero in the centered numerator array.

This removes the true high-least-prime portion of the signed boundary contribution in the entire shell. The remaining low-least-prime boundary covariance, the whole shell, and weak S are not bounded here.
