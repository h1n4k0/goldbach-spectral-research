# Removing two Vaughan Type I terms from the actual central increments

The argument concerns the signed Möbius discrepancy in the [central positivity criterion](spectral-signed-rectangle-central-positivity.md). It is arithmetic and unconditional. It removes two exact Type I parts individually, without estimating the remaining Type II term.

Let $N$ be even, $L=\log N$, and $I_y=(N/2,y]$ for $N/2\le y\le9N/16$. For an arithmetic function $F$ define
$$
 \mathcal B_F^+(t,y)=
 \sum_{\substack{q\le t\\(q,N)=1}}\mu(q)
 \sum_{\substack{n\in I_y\\(n,N)=1}}
 F(n)\mu(N-n)\left(\mathbf 1_{q\mid N-n}-\frac1{\varphi(q)}\right).
$$
These are increments in the first-prime endpoint, not prefixes from zero. The actual signed discrepancy is obtained by taking $F=\Lambda$.

Fix $0<\varepsilon<\theta_0\le\theta_1<1$, and assume $N^{\theta_0}\le t\le N^{\theta_1}$ and $U,V\ge1$ with $UV\le N^{\theta_0-\varepsilon}$. Write the [Vaughan decomposition](https://doi.org/10.1112/S0025579300009025) as
$$
 \begin{aligned}
 F_1&=\mu_{\le U}*\log,&
 F_2&=-\mu_{\le U}*\Lambda_{\le V}*1,\\
 F_3&=\mu_{>U}*\Lambda_{>V}*1,&
 \Lambda&=F_1+F_2+F_3+\Lambda_{\le V}.
 \end{aligned}
$$
Here $*$ is Dirichlet convolution and the subscripts restrict the support. This identity follows by splitting $\mu$ in $\Lambda=\mu*\log$, using $\log=\Lambda*1$ on the second part, and using $\mu*1=\mathbf 1_{\{1\}}$ on $\Lambda_{\le V}$. The final term vanishes on $I_y$ since $V\le N^{\theta_0-\varepsilon}<N/2$ for large $N$. Then, for every fixed $A>0$,
$$
 |\mathcal B_{F_1}^+(t,y)|+|\mathcal B_{F_2}^+(t,y)|
 \ll_{A,\varepsilon,\theta_0,\theta_1} NL^{-A},
 \tag{1}
$$
with uniformity in the cutoffs above.

## Complementary divisor and square completion

Write $m=N-n$. In the progression term, all divisors of $m$ are coprime to $N$ by the unit condition. For squarefree $m>1$, $\mu(m)\mu(q)=\mu(m/q)$ for $q\mid m$, and the total over all such $q$ is zero. Thus the progression part of $\mathcal B_F^+$ is exactly
$$
 -\sum_{\substack{n\in I_y\\(n,N)=1}}F(n)\mu^2(m)
       \sum_{\substack{d\mid m\\d<m/t}}\mu(d).
 \tag{2}
$$
Both sides vanish termwise when $m$ is not squarefree. The inequality $d<m/t$ is strict, including integral endpoints.

For either Type I coefficient, expand along $a\mid n$ with $a\le UV$. For $F_1$ the summand is $\mu(a)\log(n/a)$ with the smaller $a\le U$. For $F_2$ the coefficient at $a$ is $-\sum_{uv=a,u\le U,v\le V}\mu(u)\Lambda(v)$ and its absolute value is at most $\sum_{v\mid a}\Lambda(v)=\log a$. In particular $|F_j(n)|\le L\tau(n)$ on $I_y$. Expand $\mu^2(m)=\sum_{b^2\mid m}\mu(b)$ in (2) and retain $b\le B=L^J$. There are $O(N/B)$ values of $m<N$ divisible by a square $b^2$ with $b>B$. The discarded summands are bounded by $L\tau(n)\tau(m)^2$ there, accounting for both the switched divisors and the omitted square bases. Hölder with exponents $(4,4,2)$ and the divisor moment bound $\sum_{j\le N}\tau(j)^k\ll_k NL^{2^k-1}$ give total $O(N L^{70}/\sqrt B)$. We may take $J$ arbitrarily large in terms of the required saving.

For any retained $a,b,d$ with nonzero coefficients, the unit condition and $n+m=N$ require $(abd,N)=(a,bd)=1$. Put $k=m/d$. Since $d$ is squarefree, $b^2\mid kd$ is equivalent to $b^2/(b,d)\mid k$. The additional conditions are $k\equiv Nd^{-1}\pmod a$ and $(k,N)=1$. Chinese remaindering and unit inclusion–exclusion give density $\varphi(N)/(Na[b^2,d])$ in the raw $n$ coordinate and endpoint error $O(\tau(N))$ per interval. Apply this on $I_y\cap(-\infty,N-td)$, including empty intervals. Partial summation for $\log(n/a)$, or the constant coefficient for $F_2$, costs at most $L$ in the error. Summing over $a,b,d$ costs
$$
 O(UVB(N/t)\tau(N)L)=N^{1-\varepsilon+o(1)}.
 \tag{3}
$$

## Main terms, including the independent progression baseline

Reverse the continuous integration in $n=x$ and summation in $d$. With $Y=(N-x)/t$, the $d$ contribution to the density is
$$
 \sum_{\substack{d<Y\\(d,aN)=1}}\frac{\mu(d)}{[b^2,d]}
 =\frac1{b^2}\sum_{\substack{c\mid b\\(c,aN)=1}}\mu(c)
       \sum_{\substack{j<Y/c\\(j,abN)=1}}\frac{\mu(j)}j .
 \tag{4}
$$
To see this, take $c=(b,d)$ and use $d=cj$ and $(j,b)=1$. The squarefree factors and the density denominator leave precisely the $j^{-1}$ coefficient.

For a modulus $M\le N^2$ and cutoff $X$ of fixed positive-power size in $N$, the coprime sum $\sum_{j<X,(j,M)=1}\mu(j)/j$ is smaller than any fixed inverse power of $L$. Here is the uniformity needed in (4). Its Dirichlet series is $\zeta(1+s)^{-1}H_M(s)$ with $H_M(s)=\prod_{p\mid M}(1-p^{-1-s})^{-1}$. The absolute coefficient norm at $s=-1/4$ is $\exp(O(L^{1/4}))$ by splitting the divisor prime sum at $p=2L$. Convolve with $\mu(j)/j$. For indices of $H_M$ up to $\sqrt X$, the ordinary zero-free-region Mertens estimate and partial summation give an $O(\exp(-c\sqrt{\log X}))$ bound for the truncated sum with zero full value. This saving absorbs $\exp(O(L^{1/4}))$. The remaining indices cost $O(X^{-1/8}\exp(O(L^{1/4})))$ using the weighted coefficient norm and bounded partial sums of $\mu(j)/j$. The same proof works with strict real endpoints. Here $M=abN\le N^2$ and $Y/c\ge (7/16)N^{1-\theta_1}/B$. The inner sum in (4) therefore has arbitrary inverse-log decay. Sum $\tau(b)/b^2$, use $\sum_{a\le UV}L/a\ll L^2$, and integrate over an interval of length $O(N)$. This bounds the progression main term as in (1).

The term with $1/\varphi(q)$ in $\mathcal B_F^+$ did not enter (2). It factors separately as $\sum_{q\le t,(q,N)=1}\mu(q)/\varphi(q)$ times the unit sum in $n$. The $q$ factor has arbitrary inverse-log decay by the same convolution argument, now with the good-prime factors $(1-p^{-s}/(p-1))/(1-p^{-1-s})=1+O(p^{-2-\Re s})$ on $\Re s=-1/4$ in absolute coefficient norm. The $n$ factor is $O(NL^2)$ for either Type I term. This proves (1).

## The remaining term

Let $b_V(v)=\sum_{r\mid v,r>V}\Lambda(r)$, with $0\le b_V(v)\le\log v$ and support on $v>V$. Then $F_3=(\mu\mathbf 1_{>U})*b_V$, and its $1/\varphi(q)$ baseline is inverse-log small by the same trivial bound for the $n$ factor. Applying (2) to it now gives
$$
 \mathcal B_\Lambda^+(t,y)
 =-\!\!\sum_{\substack{uv+dk=N,\ uv\in I_y,\ (uv,N)=1\\
                 u>U,\ v>V,\ k>t}}
      \mu(u)\mu(d)b_V(v)\mu^2(dk)
       +O_{A,\varepsilon,\theta_0,\theta_1}(NL^{-A}).
 \tag{5}
$$
The index $k>t$ is the same strict complementary cutoff, not a replacement by a dyadic threshold. For instance on $N^{.49999}\le t\le N^{.50001}$, both Vaughan thresholds can be $N^{.2499}$. The sum in (5) still has to be estimated, and a central positivity criterion requires control of the necessary endpoint ranges outside this band as well. Neither this reduction nor (1) proves the required rectangle bound or weak S.
