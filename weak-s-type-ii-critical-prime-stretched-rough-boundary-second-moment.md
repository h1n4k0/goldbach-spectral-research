# Stretched-exponential roughness suffices in the actual critical-boundary second moment

Keep the original even target $N$, $X=\sqrt N$, $L=\log N$, hard prime box $P$ (with arbitrary fixed $|E(u,v)|\le1$ and the possibly active $N/2<uv\le y\le9N/16$ gate), and [three signed least-prime boundary branches](weak-s-type-ii-critical-prime-least-prime-boundaries.md). In the genuine complementary polynomial, $d\in I_0=I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le m=dk<N/2$, $(m,N)=1$, and the weight is $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. Write $p=P^-(m)$ on nonzero squarefree terms. The three branches below retain their exact endpoint tests:

1. $p\mid d$, and $d/p$ fails the lower end of $I_0$;
2. $p\mid k$, and $pd$ fails the upper end of $I_0$;
3. $p\mid k$, $pd\in I_0$, and $k/p\le t$.

Let $2\le Z\le X$, $1\le R<Z$, $2\le W<Z$, and put

$$
r_Z(d)=\prod_{\substack{\ell\mid d,\ \ell<Z\\\ell\ {\rm prime}}}\ell.
$$

Retain the exact signed terms of the three branches such that $r_Z(d)\le R$ and $p\le W$, with no additional restriction on $d/r_Z(d)$, and denote their polynomial by $D_{Z,R,W}$. There is no upper bound on the number of prime factors of this quotient. Unconditionally,

$$
\int_0^1|D_{Z,R,W}(\alpha)|^2\,d\alpha
 \ll N(1+\log R)^3\left(\frac{1+\log W}{\log Z}
      +\frac{(1+\log W)^2 L}{(\log Z)^3}\right).
\tag{1}
$$

The true full and double-centered signed pairings with $P$ on the entire critical shell are bounded by $O(N)$ times the square root of the factor multiplying $N$ in (1). Thus for arbitrary fixed $A>0$, $B\ge0$, and $\gamma\in(1/3,1)$, one may take $R=L^B$, $W=L^A$, and $Z=\exp(L^\gamma)$ to get $o(N)$ pointwise for every sufficiently large even $N$. More generally, with $\log R=L^\theta$, $\log W=L^\omega$ and $\log Z=L^\gamma$, it suffices that $3\theta+\omega<\gamma$ and $1+3\theta+2\omega<3\gamma$. All constants in (1) are absolute and the estimate is uniform in the hard cuts. No assertion is made for the actual $r_Z(d)>R$ remainder.

## 1. Absolute dyadic rough count, including the small endpoint

Call an integer $Z$-rough if all its prime factors are at least $Z$, allowing $1$. Uniformly for $H\ge Z/2$, one has

$$
\#\{H\le n\le2H:n\text{ is }Z\text{-rough}\}\ll \frac H{\log Z}.
\tag{2}
$$

Here is a short proof to make the parameter uniform. Take $z=\lfloor Z^{1/10}\rfloor$ and handle bounded $Z$ trivially. Put $G(z)=\sum_{u\le z}\mu^2(u)/\varphi(u)\gg\log z$; the last bound follows from $\varphi(u)\le u$ and the positive proportion of squarefree integers (the union bound over squares already suffices), by partial summation. For $u\le z$ set $b_u=\mu(u)/(\varphi(u)G(z))$, and define $\lambda_d/d=\sum_{d\mid u,\ u\le z}\mu(u/d)b_u$. Thus $\lambda_1=1$ and $b_u=\sum_{u\mid d,\ d\le z}\lambda_d/d$. If $d$ is squarefree, expansion gives

$$
\left|\frac{\lambda_d}{d}\right|
 \le \frac{1}{\varphi(d)G(z)}
      \sum_{\substack{j\le z/d\\(j,d)=1}}\frac{\mu^2(j)}{\varphi(j)}
 \le \frac1{\varphi(d)},
$$

whereas $\lambda_d=0$ for nonsquarefree $d$. In particular $|\lambda_d|\le d$. Each $Z$-rough $n$ has $\sum_{d\mid n,\ d\le z}\lambda_d=1$, since $z<Z$. Sum its square over $n\le2H$ and use

$$
\sum_{d,e\le z}\frac{\lambda_d\lambda_e}{[d,e]}
 =\sum_{u\le z}\varphi(u)b_u^2
 =\frac1{G(z)}
$$

from $\gcd(d,e)=\sum_{u\mid d,e}\varphi(u)$. The result is $O(H/\log z+z^4)$, which gives (2) since $z^4\le Z^{2/5}$ and $H\ge Z/2$.

For any positive multiplicative interval of endpoint ratio at most $C p$ with fixed $C$, the reciprocal sum of its $Z$-rough integers **greater than one** is $O_C((1+\log p)/\log Z)$, by starting the dyadic cover at $Z$. The reciprocal sum over all $Z$-rough integers up to $N$, including $1$, is $O(L/\log Z)$ since $Z\le\sqrt N$. No short-interval sieve estimate beyond (2) is needed.

## 2. Keep both boundary tests in the divisor-pair sum

At each genuine integer $m$, $p=P^-(m)$ is unique. Square the exact coefficient and use Cauchy across the three branches only, at cost at most three. For each $p$ and branch it suffices to bound the unsigned count of pairs of actual divisors $d,d'$ in that same branch with the same $m$. This incurs no extra factor for the number of prime labels. Put $r=r_Z(d)$, $r'=r_Z(d')$, $h=d/r$, $h'=d'/r'$. Both $h,h'>1$ since $r,r'\le R<Z\le X\le d,d'$; they are $Z$-rough, and $(rr',hh')=1$. All of $r,r',h,h'$ are squarefree on true support.

For fixed $p$ and branch there is a common positive interval $J_p$ for both $d,d'$ of endpoint ratio $O(p)$. Use $[\inf I_0,p\inf I_0]$ in branch 1, $[\sup I_0/p,\sup I_0]$ in branch 2 (absent for unbounded $I_0$), and $[7N/(16pt),N/(2t)]$ in branch 3, which follows from $t<k\le pt$ and $7N/16\le m<N/2$. These are redundant closed bounds, not replacements in any signed coefficient. They imply $h\in J_p/r$ and $h'\in J_p/r'$, possibly different intervals but both of endpoint ratio $O(p)$.

In branch 1, $p\mid r,r'$, and for each $r$ the label is unique, $p=P^-(r)$. In branches 2 and 3, $p\nmid rr'$ because $p\mid k,k'$ on squarefree support, while $p\mid m$. Since $p<Z$, in these last branches the exact divisibility needed in the upper count is $[r,r',p][h,h']\mid m$; in branch 1 it is $[r,r'][h,h']\mid m$. Counting by floors under $m<N/2$ gives $N/(2[r,r',p][h,h'])$ or $N/(2[r,r'][h,h'])$, respectively, with no added floor errors even for moduli above $N$. The original $N$-unit and all other masks have only been dropped at this upper-count step.

For fixed $r,r',p$ it remains to estimate

$$
\sum_{\substack{h>1,\ h'>1\ {\rm rough}\\h\in J_p/r,\ h'\in J_p/r'\\ h,h'\le N}}\frac1{[h,h']}.
$$

Write $h=ga$, $h'=gb$ with $g=\gcd(h,h')$ and $(a,b)=1$, so that $[h,h']=gab$. Dropping the coprimality only increases this nonnegative count. Let $V_p=1+\log p$ and $\lambda=\log Z$.

- If $a,b>1$, then for fixed $g$ each of $a,b$ stays in a positive interval of relative endpoint ratio $O(p)$. Their reciprocal sums are $O(V_p/\lambda)$ each, and the free reciprocal sum in $g\le N$ is $O(L/\lambda)$, including the atom $g=1$. This gives $O(V_p^2 L/\lambda^3)$.
- If exactly one of $a,b$ is $1$, then $g>1$ and is directly in one narrow interval. The other variable is also $>1$ and confined to a narrow interval for each $g$. This gives $O(V_p^2/\lambda^2)$, absorbed by the preceding bound.
- If $a=b=1$, the one variable $g>1$ is in the intersection of the two narrow intervals. This gives $O(V_p/\lambda)$.

The distinction between rough $1$ and rough integers $>1$ is essential for these gains.

## 3. Sum the small moduli and pass to the true shell

The unrestricted squarefree $r,r'\le R$ reciprocal least-common-multiple sum is at most $\prod_{\ell\le R}(1+3/\ell)\ll(1+\log R)^3$ (over primes), by Mertens. In branch 1, use the unique $p=P^-(r)\le W$ and bound $V_p,V_p^2$ by $1+\log W,(1+\log W)^2$. In branches 2/3, $p\nmid rr'$, so the extra factor in $[r,r',p]$ is exactly $p$. For $j=1,2$ one has $\sum_{p\le W}(1+\log p)^j/p\ll(1+\log W)^j$ by Chebyshev and partial summation. Combining these with the three relative positions of $a,b$ gives (1) by ordinary Parseval.

The arcs at all $q\in[.8X,.9X]$ prime and all nonzero numerators have radius $1/(10N)$ and are disjoint. Restricting to them contracts $L^2$, and subtracting the numerator mean separately at fixed $q,\beta$ contracts it again, even at $q\mid N$. The genuine prime box has ordinary squared norm $O(N)$ by unique products of primes in its disjoint proportional intervals, with $O(N/L^2)$ possible pairs and weights $O(L)$. Cauchy for the true phase $e(-N\alpha)$ then gives the stated full and centered signed bounds. The proof does not give a signed lower bound or further cancellation for the unremoved terms.

## 4. Genuine new terms absent at every fixed polynomial rough cutoff

For $1/3<\gamma<1$ and $Z=\exp(L^\gamma)$, take arbitrarily large $N=2^j$, $W,R\ge3$, $y=9N/16$, $I_0=[X,2X]$, and $t=N^{.49999}$. Let $s=\lfloor L/(4L^\gamma)\rfloor$ and $H=(1.05X/3)^{1/s}$. Thus $s\to\infty$ and $\log H\sim 2L^\gamma$. Choose $s$ distinct primes in $[H,H(1+.01/s)]$. The classical quantitative prime number theorem ([Montgomery–Vaughan, Theorem 6.9](https://ndl.ethernet.edu.et/bitstream/123456789/23715/1/Hugh%20L.%20Montgomery.pdf)) supplies more than $s$ there, since $s$ is a fixed power of $L$ to within a constant, whereas the relative error decays like $\exp(-c\sqrt{\log H})$. Set $d$ to three times their product; then $1.05X\le d<1.061X$. Choose a prime $k\in[.43X,.44X]$. Every factor is odd, distinct and coprime to $N$, and $7N/16<m=dk<N/2$. Here $p=r_Z(d)=3$ and $d/3<X$, so this is a true branch-1 summand with nonzero sign. Every prime of $d$ is below $N^\kappa$ for any fixed $\kappa>0$ and all sufficiently large $N$; hence $r_{N^\kappa}(d)=d>R$ for polylogarithmic $R$. The example proves strict new coverage of actual terms, not an assertion about their aggregate signed mass.
