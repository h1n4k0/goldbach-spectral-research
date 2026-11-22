# Unconditional Vaughan Type II beyond the near-balanced slab

Let $N$ be a sufficiently large even integer, $X=\sqrt N$, $L=\log N$, and $V=N^{.2499}$. Use the actual signed summand

$$
      \mu(u)\mu(d)b_{\rm II}(v)\mu^2(dk),
         \qquad b_{\rm II}(v)=\sum_{r\mid v,\ r>V}\Lambda(r),
$$

with $uv+dk=N,\ N/2<uv\le y,\ (uv,N)=1,\ k>t$, where $N/2\le y\le9N/16$. Both estimates below are **unconditional**; the implied constants and sufficiently-large thresholds are ineffective.

1. **All factor lengths at small complementary modulus.** For every fixed $A>0$, put $P=\lceil A\rceil+5,\ R_A=10000P$. The actual sum with

   $$
       u>V,\quad v>V,\qquad 1\le d\le X L^{-R_A}
   $$

   is $O_A(NL^{-A})$, uniformly for all real $t\ge0$. There is no comparable-factor restriction. In particular, for $t\ge XL^{R_A}$ this includes **every** $d$ in the full switched Type II term, since $d=(N-uv)/k<N/(2t)$. Combining with the [actual central Type I and baseline identity, equation (5)](spectral-vaughan-central-type-i.md#the-remaining-term), the full central increment $\mathcal B_\Lambda^+(t,y)$ is $O_{A,\theta}(NL^{-A})$ on $XL^{R_A}\le t\le N^\theta$ for each fixed $1/2<\theta<1$ (take $U=V=N^{.2499}$ and for example $\theta_0=.49999,\ \varepsilon=.0001$ in that identity).

2. **Two unbalanced wings with no additional $d$-cap.** For the original $t\ge N^{.49999}$, the actual sum with

   $$
       N^{.487}\le u,v\le N^{.513},\qquad
       \max(u,v)\ge N^{.50002}
   $$

   is $O_A(NL^{-A})$ for every fixed $A>0$. There is no imposed $d$-cap: the physical cutoff gives $d<N^{.50001}/2$. These disjoint wings apply even to $d$ polynomially above $\sqrt N$, unlike the stretched-exponential cap of [R48](weak-s-type-ii-unconditional-moving-slab.md). There are no tags or raw-density deletions in this part.

Optional arbitrary hard subintervals of $u,v,d$ can be imposed in either assertion. The corollary for the full $\mathcal B_\Lambda^+$ uses no deletions other than its defining cuts. This does not estimate the remaining joint near-square-root seam beyond the R48 cap, other regions of large $d$ with very unequal factors, or weak S.

## 1. Exact reduction of strict moving cuts and square completion

Write $n=uv$, $m_0=N-n$. Retain separately $(u,N)=(v,N)=1$. Then $d\mid m_0$ implies $(d,N)=1$. In the expansion $\mu^2(m_0)=\sum_{c^2\mid m_0}\mu(c)$ any $c$ is also a unit modulo $N$. As in [R47 §1](weak-s-type-ii-general-even-moving-slab.md#1-common-conventions-and-exact-boundary-control), partition $u,d$ into half-open relative cells of ratio at most $1+\eta$, with $\eta=L^{-20P}$. In each cell freeze the cuts on $v$ to $v>N/(2u_0)$, $v\le y/u_0$, $v<(N-td_0)/u_0$, where $u_0,d_0$ are left endpoints. Do not change strict inequalities. For part 2 split the domain first into the two wings by the actual factor meeting $N^{.50002}$ (both cannot meet it), and split the $d$-partition at $N^{.495}$. Also impose a deterministic $d\le N^{.50001}/2$ from the original conditions before freezing. Each surviving $v$ interval can be handled by a bounded number of dyadic pieces, since $u_0v\asymp N$. There are $O_A(L^{40P+2})$ rectangles and their factor scales $U_0,V_0$ satisfy $U_0V_0\asymp N$. In part 1 both are $\gg N^{.2499}$ and $\ll N^{.7501}$.

At any changed tuple one of $|n-N/2|,|n-y|,|n+td-N|$ is $O(\eta N)$: either accepted side ensures $td=O(N)$, so freezing changes it by $O(\eta N)$. The argument keeps all equality cases at the strict boundaries, and $n,m_0\asymp N$ on both supports. For fixed $d$ there are $O(1+\eta N/d)$ congruent boundary $n$; hence the total changed $(d,n)$ count is $O(\eta NL+N^{.50001})$, once across the grid. The absolute weight for a given $(d,n)$ is at most $L\tau(n)$. Cauchy with

$$
  \sum_{d,n:d\mid N-n,\ n,N-n\asymp N}\tau(n)^2
       \le\sum_n\tau(n)^2\tau(N-n)\ll N L^9
$$

from the fourth and second divisor moments bounds the total error by $O_A(NL^6\sqrt\eta+N^{.750005}L^6)=O_A(NL^{-A-1})$.

Truncate the completion at $c\le B=L^{400P}$. The omitted square divisor bases affect only $O(N/B)$ possible $m_0$, each carrying at most $L\tau(n)\tau(m_0)^2$ after counting factorizations, genuine divisor multiplicity, and the completion tail. Hölder $4,4,2$ and the fourth/eighth divisor moments give $O(NL^{70}/\sqrt B)$ per rectangle, which is harmless even after summing the entire grid. Nonzero $c,d$ are squarefree and both prime to $N$. At fixed $c,g=(c,d)$, use $q=[d,c^2]=c^2 d/g$, injective in $d$ on the group and a unit modulus for $N$. The exact congruence is $uv\equiv N\bmod q$. We can sum all of its dyads ($O(L)$ many) and there are at most $B^2$ external $(c,g)$ pieces. To simplify estimates, use $1$-bounded normalized weights, restoring one factor $L$ for the Vaughan weight.

## 2. Low-conductor transforms without any hypothesis

Set $F_0=L^{10000P}$, $D_1=20000P$. The following applies to every nonprincipal $\chi\bmod q$, $q\le N^{O(1)}$, induced by primitive $f\le F_0$; only twists by the character itself are used. At all underlying interval scales $Y\ge N^{.24}$ the normalized transform estimates needed below are $O_A(YL^{-D_1})$. Constants are ineffective.

For the Möbius coefficients with any finite polynomial-size unit mask use the [R48 near-$1$ Perron proof, §1](weak-s-type-ii-unconditional-moving-slab.md#1-classical-transforms-at-polynomial-logarithmic-conductor). This proof works at every fixed positive-power scale: for $Y\ge N^{.24}$ choose its parameter $K$ so $.24K>D_1+C_2+3$, where $C_2$ bounds the logarithmic losses on the contour, and make the same choice of polynomial-logarithmic height $T_P$. The unit mask can include $N$ and the missing imprimitive primes dividing $q$. More explicitly its reciprocal $L$-series has those finite inverse Euler corrections, Siegel and the classical zero-free region give the same zero-free disk width $L^{-1/3}$ at height $T_P$, and $L^{\pm1}$ there near $1$ is bounded by a fixed power of $L$ by the stated Borel–Carathéodory step. The half-integer hard Perron truncation and horizontal loss still cost $O(YL^{O(1)}/T_P)$, and the vertical shift costs $Y^{-K L_2/L}$. No excluded tag Euler product is needed in this round.

For the true non-squarefree $b_{\rm II}$ transform use directly its defining prime-power mark. On a hard interval $J\subset[c_0Y,C_0Y]$ at scale $Y$ (with fixed comparability constants), its sum before normalization is exactly

$$
 \sum_{\substack{a\le \sup J/V\\(a,N)=1}}
  \chi(a)\!\sum_{\substack{r\in J/a,\ r>V\\(r,N)=1}}\Lambda(r)\chi(r).
 \tag{1}
$$

Here the inner $r$ ranges over all prime powers through $\Lambda$, not only primes. By [Siegel–Walfisz, Koukoulopoulos, Theorem 12.1](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=129), for the primitive inducing nonprincipal $\psi$, its $\Lambda$-sum through $x\in[V,N]$ is $O_A(xe^{-c_A\sqrt L})$. Indeed $f\le(\log x)^{10000P+1}$ eventually, and summing the progression errors over $\varphi(f)$ classes is absorbed in the exponential; the principal main disappears by $\sum\psi=0$. Omitting prime powers based at $p\mid qN$ costs $O(L^2)$ by counting at most $O(L)$ such primes, so the same bound holds with $\chi$ and the extra unit mask (with a smaller $c_A$). If the inner interval is nonempty, both endpoints in the difference of prefixes can be taken $\ge V$, and each is $O(Y/a)$; arbitrary strict endpoints are handled by the corresponding integer cut. The inner error is therefore $O_A((Y/a)e^{-c_A\sqrt L})$, uniformly. Summing $1/a$ gives $O_A(YL e^{-c_A\sqrt L})$. This proves the stated low-conductor saving for the actual $b_{\rm II}$, uniformly even if the interval is short or $Y/V$ is small.

When using squarefree $b$ in a wing, its weighted transform with $(b,N)=1$ is exactly the squarefree marked series of R48 without a tag exclusion: use $L(s,\chi)/L(2s,\chi^2)$ with the inverse $1+\chi(p)p^{-s}$ factors for $p\mid N$, marked by $\sum_{p>V,\ p\nmid N}\log p\,\chi(p)p^{-s}/(1+\chi(p)p^{-s})$. In the Perron range only $p\le N$ need be retained. The linear mark is bounded on the R48 near-$1$ contour by the same Siegel–Walfisz bound and partial summation, and the quadratic correction and $L(2s,\chi^2)^{-1}$ are absolute. The proof just recalled works for $Y\ge N^{.24}$ here too. This excludes any reliance on GRH, even for a real nonprincipal inducing character.

For a principal Möbius transform use the standard unconditional masked Mertens form $O(Y e^{-c\sqrt L})$ uniformly for polynomial-size masks and $Y\ge N^{.24}$, proved via convolution in [R40 §1](weak-s-type-ii-medium-prime-growing-tags.md#1-quantitative-reciprocal-l-bound-and-interval-m%C3%B6bius-sums). This use of the zeta zero-free region does not inherit Siegel ineffectivity.

## 3. Small $d$: the full factor range

On a rectangle use $\alpha_u=\mu(u){\bf1}_{u\in I,(u,N)=1}$, $\beta_v=L^{-1}b_{\rm II}(v){\bf1}_{v\in J,(v,N)=1}$; neither $v$ nor the second coefficient is replaced by its squarefree version. Orthogonality is exact in the actual $q$-unit congruence; the principal is $O(Ne^{-c\sqrt L})$ per dyad after the above masked-Möbius estimate with mask $qN$, the trivial second transform, and $\sum_{q\asymp Q}1/\varphi(q)\ll1$. No special lower bound on $d$ is necessary.

For the nonprincipal part use two-leg primitive-conductor averaging as in R48 §3. For clarity, when $q=fh$, $\varphi(q)\ge\varphi(f)\varphi(h)$ even if $f,h$ share primes. At fixed $f$ the reciprocal totient sum of the admissible dyadic extensions $h$ is $O(1)$. Hence $f\le F_0$ costs $O_A(N F_0 L^{-2D_1})$ by the true transforms above and at most $\varphi(f)$ primitive characters per $f$. The actual phase $\overline{\chi(N)}$ and the modulus signs can be bounded by 1 here.

For $f>F_0$, expand both unit masks in $h$ into squarefree divisors $r,s$. For fixed $r,s$, $\sum_{h\asymp Q/f,\,[r,s]\mid h}\varphi(h)^{-1}\ll\varphi([r,s])^{-1}$; use $\varphi([r,s]k)\ge\varphi([r,s])\varphi(k)$. In a primitive-conductor dyad $f\asymp F$, the primitive large sieve with weight $1/\varphi(f)$ (divide $f/\varphi(f)$ by $F$) and Cauchy give the product cost

$$
     \frac{X}{\sqrt{rs}}\sqrt{(F+U_0/F)(F+V_0/F)} .
$$

The sequences after $u=rj,v=sk$ have squared norms $O(U_0/r),O(V_0/s)$. The joint multiplier sum $\sum_{r,s\ {\rm sf}}(\sqrt{rs}\varphi([r,s]))^{-1}$ converges as an Euler product; see [R44 §2](weak-s-type-ii-near-full-conductor-core.md#2-large-sieve-over-the-remaining-variable-part). The key is the two-length bound

$$
 \sqrt{(F+U_0/F)(F+V_0/F)}
       \le F+\sqrt{U_0}+\sqrt{V_0}+O(X/F).
$$

Holding both lengths distinct retains the correct small-$F$ term even when the factors are very unequal. Summation over $F_0\ll F\ll Q$ thus gives

$$
    O\!\left(X Q+X(\sqrt{U_0}+\sqrt{V_0})L+N/F_0\right).
$$

The middle term is $O(N^{.87505}L)$ uniformly throughout the actual factor range. Here $Q\ll XL^{-R_A} B^2$ since $d$ is within the cap, so $X Q\ll N L^{-R_A+800P}$. All these estimates absorb the normalization, the $O_A(L^{40P+2})$ grid, the $O(L)$ modulus dyads and the at most $B^2=L^{800P}$ completion/gcd groups, leaving $O_A(NL^{-A})$. The proof also covers very small $Q<F_0$ (the high-conductor part is then empty). This completes part 1, and the Type I corollary follows with the exact negative sign of equation (5).

## 4. The two wings: direct long-leg dispersion, with the physical $d$-range

In each wing, $d\le N^{.495}$ is covered by part 1 since $N^{.495}<XL^{-R_A}$ eventually. Now $d>N^{.495}$, so all completed modulus dyads satisfy $N^{.495}\ll Q\ll N^{.50001}B^2$. If $u$ is the large factor, use the true Möbius coefficient on odd squarefree $u>1$ with $(u,N)=1$ as long variable, and $b_{\rm II}(v)/L$ with $(v,N)=1$ as short. If $v$ is large, write $v=a^2b$ uniquely with $b$ squarefree. Discard $a>B$ before completion: at most $O(N/B)$ underlying factor pairs are affected, and Cauchy with $\sum_{u,v}\tau(N-uv)^2\ll NL^9$ gives $O(NL^6B^{-1/2})$ per rectangle. Keep $(a,N)=(b,N)=1$. For $a\le B$, $b_{\rm II}(v)=b_{\rm II}(b)$, since at each prime dividing $a$ the entire power in $a^2b$ is at most $B^3<V$. Take long $b$, short $a^2u$, with product exactly $uv$; both remain units modulo $N$. No factorization changes the numerator, unit masks or Möbius signs. In either case the long scale $U$ and short $M$ satisfy

$$
      MU\asymp N,\quad
      N^{.50002}/O(B^2)\ll U\ll N^{.513},\quad
      Q/U\ll N^{-.00001}B^4 .
$$

The base intervals for the long-character transforms have scale at least $N^{.24}$. The long coefficient is $1$-bounded on odd squarefree $n>1$, $(n,N)=1$.

Use the actual unconditional averaged-zero argument of [R48 §3](weak-s-type-ii-unconditional-moving-slab.md#3-rebalance-the-averaged-energy-the-conductor-split-is-polylogarithmic), with $F_0,D_1$ as above. The high $f$ part of $\sum_q(q\varphi(q))^{-1}\sum_{\chi\ne\chi_0}|\widehat\beta(\chi)|^2$ is $O(U(1+U/(QF_0)))$; the low part is $O_A(U^2 L^{-2D_1}F_0/Q)$ by §2. After multiplication by the Poisson factor $M$ and squared Cauchy factor $MQ$, this yields $O_A(N^2(Q/U+F_0^{-1}+F_0L^{-2D_1}))$. Both exponents in the last two terms beat the total reassembly overhead after square roots.

For the nonzero modes use only the genuine fixed-residue neighboring-tile Bettin–Chandee fallback of R45/R47, including the divisor-moment large-gcd correction. No earlier GRH-dependent diagonal is being used. The two trilinear squared exponents are bounded by $1+(15/8)p$ and $23/20+(9/5)p-(3/20)z_1$, $p=\log U/L,\ z_1=\log Q/L$, plus $30\kappa+\epsilon+o(1)$, $\kappa=10^{-5}$ as there. At $p\le .513+o(1), z_1\ge .495+o(1)$ the maxima before that loss are $1.961875$ and $1.99915$; even after the loss there is a fixed margin. The constant/mixed terms have exponent at most $1+1.5p+2\kappa+\epsilon+o(1)$, and the $1/N^\kappa$ large-gcd term has fixed margin as well. The diagonal-type remainder from the divisor moments is $O(N^2L^{10}Q/U)$, still a power saving here. The old Kloosterman cross is valid with arbitrary even $N$ because the actual long variable is coprime to $N$, and $mn=N$ is impossible on its support $n>1$, even on the smoothed all-$q$ enlargement. These are the exact unit arguments of R47.

For the principal use the signed harmonic reversal of R47 with the true $\mu(d)$: at $q=c^2d/g$ it leaves $e=d/g$ on a hard interval and $(e,2cNmn)=1$, with $e\gg N^{.495-o(1)}$. Its exponential saving permits reassembly. There are at most $B^3$ external square-part/completion/gcd pieces, and the full overhead including grid and normalization and any $L^6$ diagonal factor is $O_A(L^{1240P+10})$. After square roots $F_0^{-1}$, $F_0L^{-2D_1}$ save $L^{-5000P}$ and $L^{-15000P}$, and the fixed power terms absorb the rest. Boundary, completion and large-square deletions already beat the required scale. This proves part 2. No conclusion is made for the symmetric seam with both factors nearer to $\sqrt N$ and polynomially larger $d$.
