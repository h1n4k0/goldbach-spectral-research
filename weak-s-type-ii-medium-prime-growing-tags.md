# A disjoint medium-prime slice with a growing reciprocal-mass tag band

Let $N=2^j$, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, $L_3=\log L_2$ (take $N$ sufficiently large), and keep

$$
 I=[.740X,.745X],\qquad J=[.715X,.720X],\qquad D=[.445X,.450X].
$$

Let $w(v)=\sum_{N^{.024}<p\le N^{.2499},\,p\mid v}\log p$, over primes. Define one moving tag band, independent of any requested error power, by

$$
 K=\left\lceil L_2/\sqrt{L_3}\right\rceil,\qquad
 \delta=(1000K)^{-1},\qquad S=N^\delta,\qquad
 \mathcal P=\{s\text{ prime}:S\le s\le S^2\}.
$$

An integer $v$ is selected if it is nonsquarefree, has at least one divisor in $\mathcal P$, and has **no** prime divisor in $[N^{.002},2N^{.002}]$. Write $F(v)$ for this exact indicator. For the genuine signed statistic with unchanged physical cutoffs,

$$
 Z=\sum_{\substack{u\in I,\ v\in J,\ d\in D\\
                    u,v,d\ {\rm odd},\ uv\equiv N\bmod d}}
       \mu(u)\mu(d)\mu^2(N-uv)\,w(v)F(v),
$$

we have

$$
 |Z|\ll_A NL^{-A}\quad\text{for every fixed }A>0
       \quad\text{under global Dirichlet GRH};\qquad
 \sum_{\text{same tuples}}|\text{summand of }Z|\asymp NL
       \quad\text{unconditionally}. \tag{1}
$$

The signed estimate is uniform on arbitrary subintervals of $I,J,D$; the unsigned lower bound uses the full boxes. The selecting window has reciprocal mass tending to $\log 2$, rather than $O(L^{-1})$. The slice is disjoint from the [squarefree-$v$ tagged result](weak-s-type-ii-medium-prime-tagged-slice.md) and the [previous nonsquarefree fixed-band result](weak-s-type-ii-medium-prime-nonsquarefree-tags.md). On both the true support and the tiny enlargements below, $N/2<uv<9N/16$, $k=(N-uv)/d>\sqrt N$ whenever integral, and oddness is the exact unit condition. This does not estimate the complement without a moving tag, the full balanced remainder, or weak S.

## 1. Quantitative reciprocal $L$ bound and interval Möbius sums

Assume global Dirichlet GRH. Uniformly for **nonprincipal** $\chi\bmod q$, $q\le N^C$, $|t|\le N^C$, and $1/2+L_2^{-1}\le\sigma\le2$, with fixed $C$, we will use

$$
 |1/L(\sigma+it,\chi)|\le \exp(O_C(L/L_2)). \tag{2}
$$

Here are details to keep the approach to $1/2$ uniform. For primitive nonprincipal $\chi$, the [Guinand–Weil explicit formula for primitive characters](https://arxiv.org/pdf/2005.02393v3#page=3), (2.1), applied to $f_v(x)=[\sin(\alpha(x-v))/(\alpha(x-v))]^2$, $\alpha=L_2/8$, gives

$$
 \#\{\gamma:|\gamma-v|\le L_2^{-1}\}\ll_C L/L_2
                     \qquad(|v|\le 2N^C+10).
$$

Under GRH the ordinates $\gamma$ here are real; the test is nonnegative and bounded below on the indicated interval. With the Fourier convention $e^{-2\pi i x\xi}$, its transform has support $|\xi|\le\alpha/\pi$ and size $O(1/\alpha)$. Thus the prime term is bounded by $\alpha^{-1}\sum_{n\le L^{1/4}}\Lambda(n)n^{-1/2}=o(L/L_2)$. The conductor term is $O(\log q/\alpha)$; Stirling bounds the archimedean term by $O((1+\log(|v|+2))/\alpha)$ using the decay of $f_v$. Translation is allowed for this real analytic test; the Fourier shift has unit modulus. On grouping these short bands in the zero sum and bounding the very far ordinates by the ordinary $O(\log(q(|\gamma|+2)))$ unit-band zero count, we obtain, uniformly for $L_2^{-1}\le b\le3/2$,

$$
 \sum_\gamma (b^2+(t-\gamma)^2)^{-1}\ll_C L/b .
$$

Indeed the near sum is bounded by $(L/L_2)$ times $O(L_2/b)$, and the distant tail beyond $N^C$ is $O_C(L/N^C)$.

Apply the pole-free primitive Dirichlet [Selberg smoothing identity](https://arxiv.org/html/2206.00819v2#S2), (2.1), with both smoothing parameters $x=y=\sqrt L$, and integrate $L'/L(b+1/2+it,\chi)$ horizontally from $b=\sigma-1/2$ to $3/2$. This bounds the difference of the real logarithms of the modulus. The integrated prime term is at most $\sum_{n\le L}\Lambda(n)n^{-\sigma}/\log n\ll\sqrt L$; the trivial-zero term is bounded. The absolute integrated nontrivial-zero term is at most

$$
 \frac{O_C(L)}{\log y}\int_{\sigma-1/2}^{3/2}
                              \frac{y^{-b}}{b}\,db
                      \ll_C L/L_2
$$

since $(\sigma-1/2)\log y\ge1/2$. The Euler product at $\Re s=2$ has bounded logarithm. This proves (2) for primitive nonprincipal characters. Missing factors for an imprimitive character and finite factors at primes of any extra polynomial-sized mask cost $\exp(O_C(\sqrt L))$: split the sum of $p^{-1/2}$ at $p=L$, using at most $O_C(L/\log L)$ larger prime divisors. All are holomorphic in the contours used.

By Perron on half-integer endpoints, at height $N^4$ from $\Re s=2$ to $\Re s=1/2+L_2^{-1}$, (2) implies for every hard interval at scale $V_0\le N$

$$
 \left|\sum_{\substack{n\ {\rm in\ interval}\\(n,W)=1}}\mu(n)\chi(n)\right|
       \ll_C \sqrt{V_0}\exp(O_C(L/L_2)),
                 \qquad W\le N^C,\quad \chi\ne\chi_0. \tag{3}
$$

The series is $1/L(s,\chi)$ times finite Euler corrections, with no pole. The start-line truncation error is $O(V_0^2\log(2N)/N^4)$, horizontal sides cost $O(V_0^2\exp(O_C(L/L_2))/N^4)$, and the new vertical side loses only $V_0^{1/L_2}\log N$. As usual the GRH bound for nonprincipal prime sums on any subinterval of $[Y,2Y]$ is $O_C(\sqrt Y L^2)$ for moduli $\le N^C$ and $Y\le N$, from the explicit formula for $\psi$ and partial summation (remove prime powers at trivial square-root cost). Only untwisted prime sums are needed. For a principal masked Möbius sum at scale $X$ we use instead

$$
 \sum_{\substack{u\in I\\(u,W)=1}}\mu(u)\ll_C X e^{-c\sqrt L}
 \quad(W\le N^C). \tag{4}
$$

This is unconditional: convolve $\mu$ with the coefficients of $\prod_{p\mid W}(1-p^{-s})^{-1}$, split its index at $\sqrt X$, and use the classical zero-free-region Mertens bound for the smaller indices. Their $1/d$ mass is at most $\exp(O_C(\log L))$; the Rankin tail with quarter-power costs $X^{-1/8}\exp(O_C(L^{1/4}))$. The same argument is recalled for the harmonic version in the [left-strip density proof](weak-s-type-ii-left-strip.md#3-cancel-the-combined-actual-density).

## 2. Deterministic errors for growing-depth transfer

For each fixed $v,d$ there is at most one $u$, and conversely each $u,d$ determines at most one $v$: the appropriate interval is shorter than $d$ and the congruence has no solution with a nonunit fixed variable. If $\omega(v)=\#\{s\in\mathcal P:s\mid v\}$, apply Bonferroni through order $K$ with discrepancy $\le\binom{\omega(v)}{K+1}$. Since $\sum_{s\in\mathcal P}1/s\to\log 2$ by the prime number theorem, the error in $Z$ is at most

$$
 O\!\left(NL\,\frac{(\sum_{s\in\mathcal P}1/s)^{K+1}}{(K+1)!}\right)
          =O_A(NL^{-A})
$$

for every fixed $A$: $K\log K=(1+o(1))L_2\sqrt{L_3}$. At each retained order $h\le K$, represent the tags as ordered distinct primes $s_1,\ldots,s_h$ with factor $1/h!$, and put $r=\prod_i s_i$, $v=rm$. Then $S\le r\le N^{.002}$ and $r$ is squarefree. Each integer of size $O(N)$ has $O(K)$ tag primes and at most
$\mathfrak C=\exp(O(K\log(2K)))=\exp(o(L_2^2))$ tag tuples over all retained orders. For all integer arguments of polynomial size we use $\tau(n)\le\exp(O(L/L_2))$; this follows, for example, by splitting prime factors at $\sqrt L$ (small primes contribute $O(\sqrt L L_2)$ to $\log\tau$, and large prime factors counted with multiplicity are $O(L/L_2)$).

Discard $(r,u)>1$ at total absolute cost $N\exp(-\delta L+O(L/L_2+K\log(2K)))$, with any $\log N$ factor absorbed in the $O(L/L_2)$: for each common tag $s$, both $u,v$ are multiples of $s$, with $O(N/s^2)$ such pairs and at most $\tau(N-uv)$ possible $d$. Further replace $1-\mu^2(rm)$ by $1-\mu^2(m)$; an error implies $s^2\mid v$ for some tag, and costs no more by uniqueness of $u$ for each $v,d$. These costs beat every inverse logarithm since
$\delta L_2\asymp\sqrt{L_3}\to\infty$.
The medium weight $w(rm)=w(m)$ exactly. For all large $N$, $S^2<N^{.002}$; the old-tag exclusion is also exactly equivalent on $rm$ and $m$, with no approximation.

Partition the tag positions into separate multiplicative blocks of ratio at most $1+\eta$, $\eta=\exp(-L_2^2)$. If $r_0$ is the product of the block left endpoints, replace $m\in J/r$ by $m\in J/r_0$. Any mismatch restricts $v$ to $O(K\eta X+1)$ integers near the two exact endpoints of $J$. Counting $v,d$ and their at most $\mathfrak C$ tag tuples gives $O(LX\mathfrak C(K\eta X+1))$, again below all inverse-log scales. In particular the ratio error sums over actual affected $v$, not over the number of block tuples. Geometry is unchanged on the enlarged support by its fixed margins. Complete the $N-uv$ square gate with $b^2\mid N-uv$, up to $B=\exp(L_2^2)$. The old divisor-moment and $4,4,2$ Hölder argument gives at most $N L^{O(1)}\mathfrak C B^{-1/2}$, since the support of a missing square divisor has $O(N/B)$ values of $N-uv$; this too is below every inverse-log scale. All freezes and exclusions were compared before square completion.

The number of block tuples, dyads, completion variables, and their gcd groups has logarithm $O(K L_2^2)=o(\delta L)$, since at each position the number of blocks is $\ll 1+(\log S)/\eta$. The same holds including $\mathfrak C$ and powers of $L$.

## 3. A uniform centered dispersion budget

On each block tuple let $n=ru$ be the long leg and $m=v/r$ the short. The short coefficient, divided by $L$, is $w(m)(1-\mu^2(m))$, with the exact old-tag exclusion, oddness, and $m\in J/r_0$ imposed. It is $1$-bounded. The long coefficient $\beta_n$ is the sum of $\mu(u)$ over its ordered tag tuples in the given blocks, with $ru=n$, odd $u\in I$, and $(u,r)=1$, divided by a common upper bound $\mathfrak C$. It is $1$-bounded and supported on odd squarefree $n$. Both supports fit single dyadic intervals with

$$
 U\asymp X r_0,\qquad M\asymp X/r_0,\qquad
         N^\delta\le r_0\le N^{.002}.
$$

For nonprincipal $\chi$, expand $(u,r)=1$ by $a\mid(u,r)$. On choosing a subset of tag positions for $a$, use $u=a\ell$ and $\mu(a)\mu(u)=\mu(\ell){\bf1}_{(\ell,a)=1}$; oddness adds a $2$-mask to $\ell$. Write $T_i$ for the left endpoint in position $i$. For fixed assigned primes of $a$, (3) supplies $\sqrt X\prod_{i\in a}T_i^{-1/2}\exp(O(L/L_2))$, where $i\in a$ denotes those positions. The remaining prime product can be summed before taking absolute values. Impose distinctness by inclusion–exclusion on pairs of remaining positions; in each collision group of size $k\ge2$, if the intervals intersect at all their scales are comparable within $1+\eta$, and summing $\chi^k$ trivially over the common interval is $O(\prod_{\rm group}T_i^{1/2})$. Singletons use the GRH prime bound and may exclude the at most $K$ assigned primes. Thus the unassigned product costs $\prod_{i\notin a}\sqrt{T_i}$ times at most $\exp(O(K^2+K L_2))$. There are $O(\prod_{i\in a}T_i)$ choices for the assigned primes and $2^h$ choices of positions. Factors $\chi(a)^2$ have modulus at most one. We conclude, uniformly,

$$
             \Big|\sum_n\beta_n\chi(n)\Big|
             \ll \sqrt U\,\exp(O(L/L_2))
                                  \quad(\chi\ne\chi_0), \tag{5}
$$

since the combinatorial logarithm is $o(L/L_2)$. For the principal comparison use (4) with the exact odd mask $2rq$ before summing the $O(r_0)$ tag tuples. Its transform is $O(r_0 X e^{-c\sqrt L})$. With the short coefficient bounded, summing the principal densities over a modulus dyad costs $O(N e^{-c'\sqrt L})$, absorbing the subpolynomial $\sum_{q\asymp Q}\varphi(q)^{-1}$ by the elementary bound $\varphi(q)^{-1}\ll \log(2q)/q$. This survives the number of block tuples and completions because $K L_2^2=o(\sqrt L)$.

At fixed odd squarefree $b$ split by $g_0=(b,d)$, so $q=[d,b^2]=b^2d/g_0$ is injective in $d$, odd and coprime to $N$. The two exact divisibilities become $mn\equiv N\bmod q$. All dyads $Q\asymp q$ satisfy $X/5\le Q\le O(XB^2)$, hence $Q\ll U$ with a factor tending to zero. Use the [centered neighboring-tile proof](weak-s-type-ii-medium-prime-tagged-slice.md#2-a-centered-neighboring-tile-estimate), taking the ordinary Bettin–Chandee fallback of the [underlying off-diagonal estimate](weak-s-type-ii-wright-near-balanced.md#1-the-needed-fixed-residue-dispersion-estimate). To specify its uniformity, fix the original numerical $\kappa=10^{-5}$, with Poisson cutoff $H_f=(Q/M)N^\kappa$ and gcd cutoff $G=N^\kappa$. In the centered variance $W$, the exact zero term is $O(MU\exp(O(L/L_2)))$ by Parseval and (5) (principal omitted). The large-gcd terms are

$$
 \exp(O(L/L_2))\left(MU+\frac{MU^2}{QG}\right).
$$

Here use the quantitative divisor bound in §2 when counting $q\mid mn-N$, which is nonzero on odd $n>1$. The harmonic gcd sum in the $MU$ term is also absorbed. The other terms retain the usual fixed-parameter estimates (with any small **fixed** $\epsilon>0$):

$$
 \begin{array}{rl}
 W_{\rm nonzero\ square}&\ll_\epsilon
 N^{30\kappa+\epsilon}
   \bigl(Q^{-1}U^{23/8}+M^{3/20}U^{59/20}Q^{-23/20}\bigr),\\
 W_{\rm cross,\ center\ square}&\ll_\epsilon
 N^{2\kappa+\epsilon}U^{5/2}/Q+N^{\kappa+\epsilon}U^2/Q .
 \end{array}
$$

The neighboring tile counts only use $Q\ll U$ and squarefree $n_i$; the local class count is $O(U^2/Q^2)$ per small gcd. The two center terms use reciprocity with $(N,n_i)=1$, the variation $NH_f/(UQ)=O(N^\kappa)$, and the same incomplete Weil and Ramanujan bounds as in the cited centered proof. Thus these displayed bounds do not assume an $\epsilon$ or a trilinear theorem constant that varies with $N$.

Multiply by $MQ$ for Cauchy. The $MU$ terms become at most $N^2\exp(-\delta L+O(L/L_2+L_2^2))$, since $Q/U\ll B^2/r_0$; the $1/G$ term keeps a fixed power gain. Write $p=\log U/L$, $z=\log Q/L$. The two trilinear exponents are bounded by $1+(15/8)p$ and $23/20+(9/5)p-(3/20)z$ before $30\kappa+\epsilon+o(1)$; with $p\le.502+o(1),z=.5+o(1)$ both have a fixed margin below 2. The other squared terms have exponent at most $1+1.5p+2\kappa+\epsilon+o(1)$. Consequently the absolute centered $q$-sum is $O(N\exp(-c\delta L))$ for some absolute $c>0$, on all actual dyads. The $\mu(d)$ signs and selection of a subfamily of moduli do not cost anything extra for this bound. All prefactors and the number of summands external to dispersion in §2 have logarithm $o(\delta L)$; the principal bound also survives. This proves the signed part of (1) after the deterministic errors.

## 4. Unconditional mass and strict novelty

To count occupied tuples, force $9\mid v$, one tag $s\in\mathcal P$, and an additional prime $p\in[N^{.10},N^{.11}]$ dividing $v$; require odd $u,v,d$, squarefree $u,d,N-uv$, and the same congruence. Initially permit the old fixed tags. Complete the two squarefree conditions $a^2\mid u,\ b^2\mid N-uv$ at $B_0=S^{1/10}<S$. The omitted-square incidence errors cost $N\exp(-\delta L/10+O(L/L_2+\log K))=o(N)$, by the elementary $O(X/B_0)$ or $O(N/B_0)$ square-divisor support counts, polynomial-argument divisor bounds, and $O(K)$ multiplicity of the two prime labels. With $q=[d,b^2]$ discard $(9spa,q)>1$; otherwise put $u=a^2u_1,v=9sp v_1$ with $u_1,v_1$ odd. The [parity-sensitive rectangular Weil calculation](weak-s-type-ii-exactly-balanced-diagonal.md#1-exact-support-and-a-squarefree-counting-lemma), formula (4), gives main term $|I||J|\varphi(q)/(36sp a^2q^2)$ and error $O_\epsilon(q^{1/2+\epsilon})$. Summing this error over $d,s,p,a,b$ is $O_\epsilon(N^{.86+2.3\delta+\epsilon})=o(N)$, since $q\ll X B_0^2$.

Here $s,p$ cannot divide $b$, so the main-term $s,p$ mask is $(sp,d)=1$. The remaining main coefficients and Euler factors are precisely those of the [fixed nonsquarefree result, §4](weak-s-type-ii-medium-prime-nonsquarefree-tags.md#4-unconditional-occupied-mass-with-9mid-v): $3\nmid db$, one squarefree choice at 3, and at primes $\ell\nmid 6d$ the factor $1-2\ell^{-2}+\ell^{-3}$. To check the now-moving cutoff, the absolutely convergent $a,b$ extension costs, per $d,s,p$ after factoring out $|I||J|/(36sp)$, at most

$$
       d^{-1}B_0^{-1/2}\exp(O(L/L_2)).
$$

Use a half-power Rankin factor on the $a$ or $b$ tail. Only $b$-primes dividing $d$ have multiplier $1/\ell$ rather than $1/\ell^2$; their weighted local product $\prod_{\ell\mid d}(1+\ell^{-1/2})$ is $\exp(O(\sqrt L))$ by splitting prime factors at $L$. This is an extension of the main-coefficient model only. Its positive Euler product is $\gg d^{-1}(\varphi(d)/d)^2$ for odd squarefree $3\nmid d$. A positive proportion of $d\in D$ meet those conditions with $\varphi(d)/d$ bounded below, by the elementary squarefree count and averaging reciprocal prime divisors. Their exclusions $s\mid d$, $p\mid d$ change the two reciprocal sums by $O(K/S)$ and $O(N^{-.10})$, respectively. Both remaining prime sums are of order 1 by the prime number theorem; in particular the tag sum tends to $\log 2$. Hence there are $\gg N$ labeled incidences.

The medium prime $p$-multiplicity is bounded, so the sum of $\omega(v)$ over the occupied tuples with a medium $p$ is $\gg N$. On all candidate tuples, $\sum\omega(v)^2\ll N$: each $v,d$ gives at most one $u$; for the first tag moment count multiples of $s$, and for the second count multiples of distinct $s,t$, using $\sum_{s\in\mathcal P}1/s=O(1)$. Cauchy now yields $\gg N$ **distinct** occupied tuples. The old fixed tag sector can remove only $O(N/L)$ of these, by counting its tagged $v$ and then $d$, with uniqueness of $u$. The surviving tuples have $w(v)\ge .10L$, so their unsigned contribution is $\gg NL$. The upper bound $O(NL)$ follows by counting $v,d$ and using $w(v)\le L$. This proves the unconditional scale and confirms that the moving-band saving controls a genuinely new portion, not an overlap with either earlier tag.
