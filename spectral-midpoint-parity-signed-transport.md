# Midpoint divisor parity tests for signed coherent reallocations

**Scope.** Two scalar coherent tests, individually unconditional below the Bombieri–Vinogradov level, constrain bounded signed reallocations that erase prime-partner mass on genuine prime positions. Each full midpoint test vanishes identically on one total Möbius-parity class of squarefree composites. The critical-divisor loss on genuine rough partners is smaller than the expected prime-partner scale. This extends the [one-sided prime-spectrum detector](spectral-coherent-prime-spectrum-detector.md) to signed reallocations within either fixed total parity, including the odd class whose sign agrees with the primes. The individual tests do not give a Goldbach lower bound or prove Hypothesis S.

Fix $J\ge1$ and a constant $0<\beta<1/1000$. Let $N$ be sufficiently large and even, $L=\log N$, $S=\mathfrak S(N)$, $z=N^\beta$, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Use the same half-open central cells $I$ of length $H=N/(16\lceil L^J\rceil)$ in $(N/2,9N/16]$. Write $m=N-n$, so $m\asymp N$ and every genuine prime $n$ in the cell has $(m,N)=1$. All roughness conditions mean that there is no prime divisor $<z$.

For $j=0,1$ define weights

$$
 w_0(m,d)=1,\qquad w_1(m,d)=1-\frac{2\log d}{\log m},
$$

and define $F_j(m)=\sum_{d\mid m,\ d<\sqrt m}\mu(d)w_j(m,d)$ for $m>1$. For a fixed $B>0$ put $D=\sqrt N L^{-B}$ and

$$
 F_{j,D}(m)=\sum_{\substack{d\mid m\\d\le D}}\mu(d)w_j(m,d).
$$

For large $N$ one has $D<\sqrt m$ throughout the cell.

## 1. Exact complement identities

For squarefree $m>1$ there is no divisor exactly $\sqrt m$, and $\mu(m/d)=\mu(m)\mu(d)$. In the pairs $d,m/d$,

$$
 \sum_{d\mid m}\mu(d)=(1+\mu(m))F_0(m),\qquad
 \sum_{d\mid m}\mu(d)\log d=-\log m\,F_1(m)
       \quad\text{if }\mu(m)=-1 .
$$

The complete first sum is zero. The complete second sum is $-\log m$ when $m$ is prime and is zero when $m$ is squarefree composite: expand $\log d$ into its individual prime logs, and for each prime there is at least one other prime to cancel the signed divisor subsets. In particular

$$
 \begin{array}{c|cc}
  m & F_0(m)&F_1(m)\\ \hline
  \text{prime} &1&1\\
  \text{squarefree composite},\ \mu(m)=+1 &0&\text{unconstrained}\\
  \text{squarefree composite},\ \mu(m)=-1 &\text{unconstrained}&0.
 \end{array}                                                     \tag{1}
$$

The unconstrained entries need not vanish; no positivity is asserted for them. The prime row also holds for both truncated functions throughout the cell.

## 2. The individual truncated tests are unconditionally measurable

Given $A>0$, choose $B=B(A)$ sufficiently large. On genuine prime positions, only reduced progressions $n\equiv N\bmod d$ occur. [Maximal Bombieri–Vinogradov, Theorem 20.2](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=206), gives uniformly for $I$ and $j$,

$$
 \sum_{n\in I}\lambda(n)F_{j,D}(N-n)
 =\sum_{\substack{d\le D\\(d,N)=1}}
    \frac{\mu(d)}{\varphi(d)}\int_I w_j(N-u,d)\,du
  +O_A(NL^{-A}).                                                \tag{2}
$$

Indeed for each such $d$ the prime count on $I$ or a subprefix of $I$ is a difference of two prefixes. Both weights are bounded by one on the cell and have variation at most one there: for the second, $u\mapsto\log(N-u)$ is decreasing and the weight is monotone and contained in $[0,1]$. Partial summation thus costs an absolute factor against the maximal progression discrepancy. Replacing von Mangoldt by prime-only weight across these moduli costs at most $O(D\sqrt N L^2)$, absorbed by choosing a larger $B$. Formula (2) includes every genuine shifted prime, without a roughness or squarefree gate; no BV assertion conditional on either gate is used.

## 3. The omitted band has smaller true weighted mass

Define the positive critical-divisor incidence count

$$
 E_I=\sum_{\substack{n\in I\\m\ z\text{-rough}}}
       \lambda(n)\sum_{\substack{d\mid m\\D<d\le\sqrt m}}\mu(d)^2 .
$$

This count is allowed to include nonsquarefree $m$. Uniformly in the cells,

$$
 E_I\ll_{\beta,B,J}\frac{SH(1+\log L)}{L^2}.                     \tag{3}
$$

To see this, fix a squarefree $z$-rough $d$ in $(D,\sqrt N]$ with $(d,N)=1$. In $m=dq$ the cofactor $q$ is an integer in the actual interval for $n\in I$ of length $U=H/d$. For an upper bound, drop the restriction $d\le\sqrt m$. All original points have $q$ $z$-rough and $n=N-dq$ prime. Let $Y=U^{1/100}>z$ for large $N$; also $\log U\asymp L$ uniformly here. Sieve the form $N-dq$ at primes $p<Y$ and the roughness of $q$ at $p<z$. There is one root of the primality form when $p\nmid d$, and none when $p\mid d$ because $(d,N)=1$. At $p<z$ the roughness adds a distinct root precisely when $p\nmid N$: all such primes are coprime to $d$, and if $p\mid N$ the existing root is already zero. In particular there is only one root at $2$. Thus the local product is

$$
 \prod_{\substack{p<Y\\p\nmid d}}(1-1/p)\cdot V_z,\qquad
 V_z=\prod_{\substack{p<z\\p\nmid N}}(1-1/(p-1))
     \asymp \frac{S}{\beta L}.
$$

Mertens bounds the first product by $O((d/\varphi(d))/\log Y)$, and the estimate for $V_z$ is the Euler product comparison of the coherent transport proof. The dimension condition is uniform: there are at most two forbidden residues at odd primes and one at $2$. The [fundamental upper sieve, Corollary 19](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/) with level $U^{1/2}$ and the CRT error $O(2^{\omega(a)})$ at squarefree sieve modulus $a$ gives an unweighted count at most

$$
 \ll \frac{U V_z}{\log Y}\frac{d}{\varphi(d)}
       +U^{1/2}\log(2U).
$$

All true $n$ are above $Y$, as required. Multiplying by $L$ gives main bound $O(H V_z/\varphi(d))$, and summing the additive errors over all $d\le\sqrt N$ costs $O(N^{3/4}L^2)$.

For the main term,

$$
 \sum_{\substack{D<d\le\sqrt N\\ d\ z\text{-rough}}}\frac1{\varphi(d)}
        \ll_{\beta,B}\frac{1+\log L}{L}.
$$

Indeed $d/\varphi(d)\le2$ for large $N$ here, since such a $d$ has at most $1/\beta$ prime factors, all at least $z$. Cover the band by $O_B(1+\log L)$ intervals of the form $(X,2X]$ with $X\ge D$. The dimension-one upper sieve on the integer variable $d$, at sifting threshold $z$ and level $X^{1/2}$, bounds the rough count in each by $O_\beta(X/L+X^{1/2})$: there is one forbidden residue at each prime, and an interval gives error $O(1)$ per squarefree modulus. Dividing by $X$ and summing proves the reciprocal bound. Now $S$ is bounded below and the power remainder is negligible relative to the right of (3) for fixed $J$. This proves (3). No estimate of the number of prime pairs was needed.

For every $D<d\le\sqrt m$ the additional centered weight satisfies

$$
 0\le w_1(m,d)
   \le \frac{2B\log L}{\log m}
   \ll_B \frac{1+\log L}{L}.
$$

Consequently, writing $\mathcal C$ for any subset of genuine prime positions in the cell with squarefree rough composite partners, one has

$$
 \begin{split}
 \sum_{n\in\mathcal C}\lambda(n)\,|F_0(m)-F_{0,D}(m)|
      &\ll E_I,\\
 \sum_{n\in\mathcal C}\lambda(n)\,|F_1(m)-F_{1,D}(m)|
      &\ll_B E_I(1+\log L)/L.
 \end{split}                                                    \tag{4}
$$

In particular the second error is $O_{\beta,B,J}(SH(1+\log L)^2/L^3)$.

## 4. Necessary conditions on signed transport

Remove nonnegative weight $P$ in total from genuine prime-partner positions in the cell. On genuine prime positions with squarefree rough composite partners add a signed weight $\eta(n)$ of net mass $P$, with $|\eta(n)|\le C_{\rm cap}\lambda(n)$ for a fixed $C_{\rm cap}$. All other positions are unchanged. The removed mass can be all actual prime-partner weight or any amount no larger than it. Denote by $\Delta_j$ the resulting change in the total $F_{j,D}$ test. From (1) and (4),

$$
 \begin{split}
 \Delta_0&=-P+\sum_{\substack{n\text{ receiving}\\\mu(m)=-1}}
                   \eta(n)F_0(m)+O(C_{\rm cap}E_I),\\
 \Delta_1&=-P+\sum_{\substack{n\text{ receiving}\\\mu(m)=+1}}
                   \eta(n)F_1(m)+O_B(C_{\rm cap}E_I(1+\log L)/L).
 \end{split}                                                    \tag{5}
$$

Here the receiving positions are the support of the signed composite change, not only its positive part. If the altered weight has the same precision in (2) as the true weight, then $\Delta_j=O_A(NL^{-A})$. Thus a signed transport confined to $\mu(m)=+1$ can erase only $O(C_{\rm cap}E_I+NL^{-A})$, and one confined to $\mu(m)=-1$ only $O_B(C_{\rm cap}E_I(1+\log L)/L+NL^{-A})$. In either case take $A>J+4$ to get $o(SH/L)$. Negative weights in the composite change are allowed throughout this conclusion.

For mixed-parity reallocation, both opposite-class moments in (5) must equal $P$ within their respective errors. If the total signed $\mu(m)$ test is also preserved, cancellation of the net mass and of the total Möbius test forces $\sum_{\mu(m)=+1}\eta(n)=0$: the donors have sign $-1$. Define $T_\beta=2^{\lfloor1/\beta\rfloor}$; then $|F_1(m)|\le T_\beta$, because $m<N$ is squarefree rough and every weight in the half-divisor sum has absolute value at most one. As a result, the positive and negative masses of the even class, which are equal, must each be at least

$$
 \frac{\max\{0,P-O_B(C_{\rm cap}E_I(1+\log L)/L)-O_A(NL^{-A})\}}
      {2T_\beta}.                                               \tag{6}
$$

Here (6) assumes that total $\mu(m)$ data are preserved; it does not evaluate those data on the actual primes. No mixed-parity impossibility is claimed.

## 5. A true mixed moment remains outside the argument

Let $\mathcal P_I$ be the actual prime-partner weight in the cell. By (1), $F_0F_1$ is precisely the prime indicator on the squarefree integers $m>1$. All genuine prime partners in the cell are also rough. On squarefree rough integers all four functions $F_j,F_{j,D}$ are bounded by $T_\beta$, so the difference of products is bounded by $T_\beta$ times the sum of the two truncation errors. Thus (4) implies

$$
 \mathcal P_I=
 \sum_{\substack{n\in I\\ m\ {\rm squarefree},\ z\text{-rough}}}
     \lambda(n)F_{0,D}(m)F_{1,D}(m)
      +O_{\beta,B,J}\!\left(\frac{SH(1+\log L)}{L^2}\right).
$$

This identity only specifies the remaining true arithmetic target. In a divisor expansion of the product, the moduli are $\operatorname{lcm}(d,e)$, which can be as large as $D^2$, and the squarefree and rough gates remain. The one-test BV estimates (2) say nothing of the required mixed moment at the scale $SH/L$. The transport constraints above do not substitute for that estimate.
