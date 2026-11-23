# A pointwise bound for large small parts with few genuine prime slots

Keep the full signed central Type II critical-shell setting, sharp cuts, exact three boundary branches and true coefficients of the [signed rough-exponent proof](weak-s-type-ii-critical-prime-signed-all-rough-exponents.md). In particular $p=P^-(m)$, $m=dk$ is squarefree on support, $d\ge X=\sqrt N$, $k>t\ge N^{.49999}$, and $(m,N)=1$. The prime-box selector $|E(u,v)|\le1$ is fixed independently of the rational point and may have the original active upper gate. Put $L=\log N$, $L_2=\log L$, $Z=\exp(L^\gamma)$ for fixed $0<\gamma<1$, and $\lambda=\log Z$. For $2\le W<Z$, retain exactly $p\le W$ as before. Here we replace the previous magnitude condition on the exact $Z$-small part $r=r_Z(d)$ by a different actual mask.

Let $\mathcal A$ be any set of squarefree integers supported on primes below $Z$; it may depend on $N$ and contains no rational-point dependence. Impose only $r_Z(d)\in\mathcal A$ on the true signed boundary branches. Define

$$
\mathcal M(\mathcal A)=\sum_{r,r'\in\mathcal A}\frac1{[r,r']}.
$$

If $D_{\mathcal A}$ is the resulting polynomial, the ordinary squared coefficient estimate is, for each fixed $J>0$,

$$
\int_0^1|D_{\mathcal A}(\alpha)|^2\,d\alpha
\ll_{\gamma,J}
 \frac{N(1+\log W)(1+L_2)}{\lambda}\,\mathcal M(\mathcal A)
 +N L^{-J}.
\tag{1}
$$

Both full and centered actual signed pairings on the whole shell are bounded by $O(\sqrt N)$ times the square root of the right-hand side. As an actual new sector, if $\mathcal A$ comprises every squarefree $Z$-small integer having at most $\lfloor\log\lambda/6\rfloor$ prime factors, then for any fixed polylogarithmic $W$ the result is $o(N)$ pointwise on every sufficiently large even target. The small part has **no magnitude cap**. In particular this is not achieved by changing to a different fixed exponent and keeping the old magnitude condition.

## 1. Exact allocation and its reciprocal moment

Write every genuine $m=bv$ where $b=r_Z(m)$, and keep $r=r_Z(d)\mid b$ as the exact allocation. Set $T_{\mathcal A}(b)=\#\{r\in\mathcal A:r\mid b\}$. For $b\le N^{1/10}$ the two true rough partners are $a=d/r\ge X/b$ and $c=k/(b/r)>t/b$, so each is at least $N^{.39}$. This verifies the required lower bound for either short orientation in the preceding signed proof, without any assumption $r<Z$. Other conditions of its fixed-$b,r$ argument are unchanged: $p=P^-(b)\le W$ is determined, actual branch tests are separate intervals in $a,c$, and complementing to the short variable preserves the $\mu$ sign up to the true common squarefree factor $\mu(v)$. Thus its fixed-$b,r$ signed square, summed on $v$, is $O_\gamma((N/b)(1+\log W)(1+L_2)/\lambda^2)$, uniformly in the mask. One may drop the squarefree/unit conditions only after these signed squares, as in that proof.

For each $b$ Cauchy across its $T_{\mathcal A}(b)$ allocations, combined with disjoint $b$ supports in $m$, consequently asks for

$$
\sum_{\substack{b\ {\rm squarefree}\\P^+(b)<Z}}\frac{T_{\mathcal A}(b)^2}{b}
\le
\mathcal M(\mathcal A)\prod_{\substack{\ell<Z\\\ell\ {\rm prime}}}(1+1/\ell)
\ll\lambda\,\mathcal M(\mathcal A).
\tag{2}
$$

The inequality is exact from expanding the two labels $r,r'$ and writing the compulsory divisor $[r,r']\mid b$ before summing the remaining squarefree factors. The set $\mathcal A$ is finite at every $Z$; superpolynomial elements cannot affect the original support unless they divide $m$.

The $b>N^{1/10}$ part permits a uniform negligible error without making any restriction on $\mathcal A$. Bound the actual absolute coefficient at $m=bv$ by $\tau(b)\tau(v)$. The divisor-square bound $\sum_{v\le x}\tau(v)^2\ll x(1+\log x)^3$ gives a cost $O(N(1+L)^3)$ times

$$
\sum_{\substack{b>N^{1/10}\\ b\ {\rm squarefree},\,P^+(b)<Z}}\frac{4^{\omega(b)}}b
\le e^{-L/(10\lambda)}
  \prod_{\ell<Z}(1+4\ell^{-1+1/\lambda})
\ll \lambda^4 e^{-L/(10\lambda)}.
$$

The last comparison is from Chebyshev and $\sum_{\ell<Z}(\ell^{1/\lambda}-1)/\ell=O(1)$ as in the previous proof. Since $\gamma<1$ is fixed, this is negligible at every fixed power of $L$. Together with (2) this proves (1). Restriction to the disjoint shell arcs and numerator centering contract ordinary $L^2$, so the true signed conclusion follows by the original Cauchy step.

## 2. A prime-slot mask without a size or gap condition

Take $\mathcal A=\{r\ {\rm squarefree}:P^+(r)<Z,\ \omega(r)\le K\}$, with $K=\lfloor\log\lambda/6\rfloor$. For $0<u<1$, indicator majorization by $u^{\omega(r)+\omega(r')-2K}$ gives

$$
\mathcal M(\mathcal A)\le u^{-2K}\prod_{\ell<Z}\left(1+\frac{2u+u^2}\ell\right).
$$

The terms $2u$ and $u^2$ correspond to a marked prime present in only one of $r,r'$ or in both, respectively. At $u=1/7$, prime Mertens gives

$$
\mathcal M(\mathcal A)\ll \lambda^\nu,\qquad
\nu=\frac{15}{49}+\frac{\log7}{3}<1.
$$

In particular the total true full and double-centered signed shell contribution is

$$
O_\gamma\!\left(
 N\,\lambda^{-(1-\nu)/2}
      \sqrt{(1+\log W)(1+L_2)}
\right)
$$

up to $O_{\gamma,J}(N L^{-J/2})$. This saves for fixed polylogarithmic $W$ or for $\log W=L^\omega$ with fixed $0<\omega<\gamma(1-\nu)$.

A related genuine mask comes from an arbitrary allowed prime set $\mathcal P\subset\{\ell<Z\}$ with $\sum_{\ell\in\mathcal P}1/\ell\le (1/3-\varepsilon)\log\lambda+O(1)$ for fixed $\varepsilon>0$. Permit all squarefree products of those primes, with no arity limit. Then $\mathcal M=\prod_{\ell\in\mathcal P}(1+3/\ell)\ll \lambda^{1-3\varepsilon}$. Both conditions are on the exact small part of $d$, not on a surrogate sequence, on the target's avoided primes, or on an arbitrary truncation of the alias set.

## 3. Actual terms missed by every previous fixed-exponent size condition

Fix $\gamma=1/2$, $\lambda=\sqrt L$, and take $N$ along large powers of two. Set $J_0=\lfloor\log\lambda/12\rfloor$ and for $1\le j\le J_0$ choose a prime $q_j$ in

$$
\left[\exp(L^{j/(2(J_0+1))}),\ 2\exp(L^{j/(2(J_0+1))})\right].
$$

Bertrand's postulate supplies these choices; the intervals are pairwise disjoint and lie in $(3,Z)$ for large $N$. Indeed the ratio of successive **logarithms** of the lower endpoints tends to $e^{12}$, the first logarithm tends to $e^{12}$, and the last is asymptotic to $e^{-12}\lambda$. Put $r=3\prod_{j\le J_0}q_j$. Then $\log r=O(\lambda(1+\log\lambda))=o(L)$ and $1+J_0\le K$. Take a prime $g$ in $[1.05X/r,1.06X/r]$, a prime $k\in[.43X,.44X]$, $d=rg$, and $m=dk$. The two prime choices exist by the prime number theorem, are distinct since $r\to\infty$, and are both above $Z$. Set $I_0=[X,2X]$, $t=N^{.49999}$, $y=9N/16$, and $W\ge3$. The product and unit masks hold, $p=P^-(m)=3$, $r_Z(d)=r$, and $d/3<X$ gives a genuine nonzero branch-1 term.

For every fixed $0<\gamma'<1$ choose a nonempty closed subinterval of $(\gamma'/3,\min(\gamma',1/2))$. For all sufficiently large $N$, one of the exponents $j/(2(J_0+1))$ lies in it. The corresponding $q_j$ is then below $\exp(L^{\gamma'})$ but its logarithm exceeds $L^{\gamma'/3}$ by a fixed power of $L$. So the exact small part for the cutoff $\exp(L^{\gamma'})$ exceeds $\exp(C L^{\gamma'/3})$ for every fixed $C$. This strict witness for the true slot condition is missed by every fixed-exponent size condition with $\log R=O(L^{\gamma'/3})$. It is a support assertion only, not an assertion about a signed lower bound.

The dense $Z$-small parts not covered by these reciprocal-lcm conditions remain. The estimate does not close the generic signed critical covariance or weak S.
