# A structured actual sector below the square-root transition

**Scope.** An unconditional estimate for a defined sector of the complementary-divisor form of the genuine signed Möbius diagonal discrepancy. It uses [Maynard III, Theorem 1.2](https://ora.ox.ac.uk/objects/uuid%3Ada3b7279-d413-4ab1-962e-afa5d67507c2/files/s6w924c97m) and the classical prime number theorem. It removes a positive fraction of *admissible divisor indices* in the transition dyads, not a known fraction of the signed norm or mass. Divisors lacking the designated factorization remain unresolved; no S or R claim is made.

Let $N$ be large and even, $L=\log N$, and use the actual unit prefixes $A_\mu$, $A_{\mu,q}$ and discrepancy $\mathcal B(t,y)$ of the [critical-level note](spectral-critical-level-diagonal.md). All prefixes here have $0\le y\le9N/16$. Put $\eta=10^{-5}$, $\varepsilon_0=10^{-6}$, $a_2=200/10000$, $a_3=851/10000$, and define fixed exponent bands
$$
 \mathcal P_i=\{p\text{ prime}: N^{a_i-\varepsilon_0}\le p\le N^{a_i+\varepsilon_0}\},\qquad i=2,3.
$$
Call a squarefree $d$ **structured** if a prime from each of $\mathcal P_2,\mathcal P_3$ divides $d$. Write $\mathcal G$ for this set, and define
$$
 C_{\mathcal G}(t,y)=
 \sum_{\substack{d\le N/t;\ d\in\mathcal G\\(d,N)=1}}\mu(d)
 \sum_{\substack{n\le y;\ n<N-td;\ n\equiv N\bmod d\\(n,N)=1}}
      \Lambda(n)\mu^2(N-n).
$$
For every fixed $A>0$, uniformly for $N^{1/2-\eta}\le t\le N^{1/2+\eta}$ and all these prefixes,
$$
 |C_{\mathcal G}(t,y)|\ll_A NL^{-A}. \tag{1}
$$
In the exact identity
$$
 \mathcal B(t,y)
  =-C_{\mathcal G}(t,y)-C_{\mathcal G^c}(t,y)
    -A_\mu(y)\sum_{\substack{q\le t\\(q,N)=1}}\frac{\mu(q)}{\varphi(q)}
$$
the complement notation denotes all remaining squarefree divisors (the nonsquarefree terms vanish). The identity keeps the strict boundary $n<N-td$. The last term is also $O_A(NL^{-A})$ here by the elementary Euler-factor estimate in §2, with $g(p)$ replaced by $1/(p-1)$. Thus the *remaining actual signed discrepancy* in this power window comes only from the unstructured sector up to inverse-log errors.

## 1. Prime progression estimates for the actual structured square completion

In the expression for $C_{\mathcal G}$ write $\mu^2(N-n)=\sum_{b^2\mid (N-n)}\mu(b)$ and set $B=L^C$, with $C$ fixed sufficiently large in terms of $A$. The $b>B$ tail in the actual sum is bounded by
$$
 NL\sum_{\substack{b>B,\ d\le N/t\\b,d\ \mathrm{squarefree}}}[b^2,d]^{-1}
 \ll NL^2\frac{\log(2B)}{B}.
$$
This counts positive multiples of the l.c.m. exactly by $N/[b^2,d]$ as an upper bound. To sum over $d$, write $d=(b,d)d'$ and then $[b^2,d]=b^2d'$; the harmonic sum in $d'$ is $O(L)$ for each divisor of $b$. In the extended progression model use additionally $1/\varphi([b^2,d])\ll (L+\log(2b))/[b^2,d]$; its tail is $O(NL^2(\log(2B))^2/B)$. Terms with $(bd,N)>1$ do not occur under the unit restriction.

For $b\le B$ each progression modulus $\ell=[b^2,d]$ has primes $r\in\mathcal P_2$, $s\in\mathcal P_3$ with $rs\mid\ell$; indeed they already divide $d$, and are larger than $B$. The moduli may contain square factors from $b$, which the primary theorem permits. Every actual modulus is coprime to $N$. All lie below $H=B^2N^{1/2+\eta}$.

We claim a maximal estimate over these **distinct** moduli:
$$
 \sum_{\ell}\sup_{0\le v<N}
 \left|\psi_N(v;\ell,N)-\frac{v}{\varphi(\ell)}\right|
       \ll_A NL^{-A}, \tag{2}
$$
where $\psi_N$ retains $(n,N)=1$. Here and below, a stronger prescribed log power on the right is available to absorb fixed losses. First fix an ordinary prime-count endpoint $x$ with $N/L^J\le x\le N$, for any fixed $J$. Divide the two prime bands into dyads $[U,2U)$ and $[V,2V)$, costing $O(L^2)$ choices. In one such pair apply Maynard III, Theorem 1.2 with
$$
 \delta=1/5000,\qquad Q_2=2U,\qquad Q_3=2V,\qquad
 Q_1=x^{1/2+\delta}/(Q_2Q_3).
$$
The base-$x$ exponents of $Q_2,Q_3$ are respectively in $(.01999,.02001)$ and $(.08509,.08511)$ for sufficiently large $N$, uniformly in $x$ in this range. These lie strictly in the theorem's inequalities: the $Q_2$ window is $(.008,.0486)$, and the lower exponent for $Q_3$ is at most $.1024-.01999=.08241$ while the upper is at least $.0992-.6(.02001)=.087194$. Also $4H\le x^{1/2+\delta}$ for all sufficiently large $N$. Hence the triple
$$
 (q_1,q_2,q_3)=(\ell/(rs),r,s)
$$
is admissible: $q_1\le H/(UV)\le Q_1$. Choose one factorization of each $\ell$; summing instead over all triples only increases the positive error sum. For each $(q_1,q_2)$ the residue in the outer supremum is the same $N\bmod q_1q_2$ for every $q_3$, and its continuation is $N\bmod\ell$. Both are reduced because $(\ell,N)=1$. No independently chosen residue for each $q_3$ is required. The theorem gives the required inverse-log estimate at endpoint $x$ for $\pi(x;\ell,N)-\pi(x)/\varphi(\ell)$, including the dyadic cost.

For the maximal prefix, use a grid of mesh $N/\lceil L^J\rceil$ including zero and $N$ (changing the constant in the bound $x\ge N/L^J$ is immaterial). By monotonicity, for $v$ between two grid points the absolute prime-count discrepancy is bounded by the larger endpoint discrepancy plus $O((N/L^J+1)/\varphi(\ell))$. This follows by comparing the increasing progression count to the model at the two endpoints separately. Sum the grid estimates and use $\sum_{\ell\le H}1/\varphi(\ell)\ll L$. Choose $J$ and then the theorem's prescribed log saving large. Abel summation with the weight $\log p$ costs at most another $O(L)$, and the ordinary prime number theorem replaces the resulting model $\theta(v)/\varphi(\ell)$ by $v/\varphi(\ell)$ with the same arbitrarily high log saving. The proper prime powers cost $\ll_{\epsilon}N^{1/2+\epsilon}L^2$ in the total, not $\sqrt N$ per modulus: each power $n<N$ lies in at most $\tau(N-n)\ll_\epsilon N^\epsilon$ of these progressions. Removing powers at primes dividing $N$ costs $O(HL^2)$. Both are negligible for small fixed $\epsilon$. This proves (2).

For fixed $b\le B$, the same $\ell=[b^2,d]$ has at most $2^{\omega(b)}\le b$ squarefree preimages $d$: outside primes dividing $b$, all factors of $d$ are prescribed. The total multiplicity over $b$ is $O(B^2)$ and the coefficients $\mu(b)\mu(d)\mathbf1_{d\in\mathcal G}$ have absolute value at most one. Thus (2) justifies all simultaneous progression replacements, including each $n\le y$ and $n<N-td$. Their main length is the Lebesgue length of $[0,y]\cap[0,N-td)$; integer endpoint differences are handled by the same prefix estimate, or by the negligible cost of a single endpoint per pair. Extend the model $b$ sum to infinity using its tail above. For squarefree unit $d$, its Euler product is $A_Ng(d)$ with
$$
 A_N=\prod_{p\nmid N}\left(1-1/[p(p-1)]\right),\qquad
 g(p)=\frac{p-1}{p^2-p-1}.
$$
Here the $p\nmid d$ factor is $1-1/[p(p-1)]$; the $p\mid d$ factor before division is $1/p$. Reversing the $x,d$ order, the model for $C_{\mathcal G}$ is therefore
$$
 A_N\int_0^y
    \sum_{\substack{d<(N-x)/t;\ d\in\mathcal G\\(d,N)=1}}
             \mu(d)g(d)\,dx. \tag{3}
$$

## 2. The structured Euler sum really cancels

For $Y=(N-x)/t$ in (3), $N^{.49998}\le Y\le N^{.50001}$ for large $N$ (since $x\le9N/16$). The structured indicator expands by finite inclusion-exclusion:
$$
 \mathbf1_{d\in\mathcal G}
 =\prod_{i=2,3}
       \left(-\sum_{\substack{R_i\mid d;\ R_i>1\\p\mid R_i\Rightarrow p\in\mathcal P_i}}\mu(R_i)\right)
$$
for squarefree $d$. The bands are disjoint. In each term take $R=R_2R_3$ and $d=Rk$ with $(k,NR)=1$. The signed coefficient in front of the remaining $k$-sum is $g(R)$, since $\mu(R_2)\mu(R_3)\mu(R)=1$.

Crucially, $R<Y$ implies $Y/R\ge N^{.00004}$ here. In fact if $R$ uses $j$ primes from $\mathcal P_2$ and $k'$ primes from $\mathcal P_3$, then $1\le j\le26$ and $1\le k'\le6$ by $R<Y\le N^{.50001}$. The exponent $\log R/L$ is within $(j+k')10^{-6}$ of $(200j+851k')/10000$. The latter cannot equal $1/2$: reducing modulo 200 would give $51k'\equiv0\pmod{200}$, impossible for $1\le k'\le6$. The distance from $1/2$ is at least $10^{-4}$ before the band widths, and at least $.000068$ after. Since $R<Y$, the exponent must be on the lower side, at most $.499932$. This proves the cofactor bound using $Y\ge N^{.49998}$.

Here one needs no RH for the remaining signed Euler sum. Uniformly for integers $M\le N^2$ and $X$ between a fixed positive power of $N$ and $N$,
$$
 \sum_{k<X,(k,M)=1}\mu(k)g(k)=O_A(L^{-A}).
$$
For completeness, factor its Dirichlet series into $\zeta(1+s)^{-1}H_M(s)$ as in the weighted parity proof. At $\Re s=-1/4$, the absolute weighted coefficient sum of $H_M$ is $\exp(O(L^{1/4}))$: good-prime differences are $g(p)-1/p=O(p^{-3})$, and the bad primes $p\mid M$ are bounded by splitting $\sum p^{-3/4}$ at $\log(2M)$. Write the truncated sum as the convolution of the $H_M$ coefficients with $\mu(n)/n$. For the coefficient index $u\le\sqrt X$ use the classical zero-free-region Mertens estimate $\sum_{n<X/u}\mu(n)/n\ll\exp(-c\sqrt{\log X})$, after decreasing $c$; its limiting full sum is zero. Multiplying by $\exp(O(L^{1/4}))$ still gives every log saving. For $u>\sqrt X$ use the uniformly bounded inner partial sums and the absolute weighted coefficient tail $O(X^{-1/8}\exp(O(L^{1/4})))$. The same proof works for $g(p)=1/(p-1)$, whose good-prime difference is $O(p^{-2})$, and neutralizes the discrepancy baseline because $|A_\mu(y)|\le NL$. Strict versus weak cutoff does not change these estimates.

Apply this estimate to $M=NR\le N^2$, $X=Y/R$. The outer $g(R)$ coefficients have bounded total mass, since they are dominated by $\prod_{p\in\mathcal P_2\cup\mathcal P_3}(1+g(p))=O(1)$ by Mertens' prime reciprocal estimate in the two fixed exponent bands. The inner sum in (3) is $O_A(L^{-A})$ uniformly, completing (1).

## 3. The excluded sector is nonempty on the scale of the admissible indices

Uniformly for $D$ between $N^{1/2-\eta}$ and $N^{1/2+\eta}$, the dyad $D/2<d\le D$ contains $\gg D\varphi(N)/N$ structured squarefree unit integers. For primes $r\in\mathcal P_2$, $s\in\mathcal P_3$, both coprime to $N$, count $d=rsk$ with $k$ squarefree, coprime to $Nrs$, and $D/(2rs)<k\le D/(rs)$. The elementary squarefree count gives a main term $\asymp (D/(rs))\varphi(N)/N$ and error $O(\tau(Nrs)\sqrt{D/(rs)})$, by expanding the squarefree indicator and counting reduced integers. The total error is $O(N^{.38})$, for example by the divisor bound, $\#\mathcal P_2\#\mathcal P_3\le N^{.105102}$ and $\sqrt D\le N^{.250005}$. Each reciprocal prime sum over its band tends to a positive constant, and the $O(1)$ primes in that band dividing $N$ contribute $o(1)$. Each $d$ is represented at most $26\cdot6$ times. This proves the lower bound, while the total number of admissible squarefree units in that dyad is $\asymp D\varphi(N)/N$ by the same squarefree count. This is a fixed positive index fraction; the constants may be small. No conclusion about the fraction of actual $\Lambda$-weighted signed magnitude follows.
