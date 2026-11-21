# A signed bound on narrow rational cores inside the minor arcs

Assume global Dirichlet GRH and retain the exact definitions of $F_I,\xi,\mathcal Q,W,K,L,S,I_0$ and the interval conventions of [the R32 major-arc calculation](r32-source-double-giant-major-arcs.md). In particular $I\subseteq I_0=[\rho N,(1-\rho)N]$, $0<\kappa\le1/2000$ is fixed, $S=\mathfrak S(N)$, and
$$
 F_I(\alpha)=\sum_{\substack{q\in\mathcal Q,\ p\ge1\\qp\in I,\ (p,N)=1}}
       (\log q)\left({\bf1}_{p\ {\rm prime}}-\frac{K}{\log p}{\bf1}_{(p,W)=1}\right)e(\alpha qp).
$$
Let $R_0=\lfloor N^{1/4}\rfloor$ be the R32 arc cutoff, and $R_1=\lfloor N^{1/2-\kappa/4}\rfloor$. For reduced fractions put
$$
 \mathfrak C=
 \bigcup_{R_0<r\le R_1}\ \bigcup_{\substack{a\bmod r\\(a,r)=1}}
    \{\alpha:\|\alpha-a/r\|\le 1/N\}.
$$

**Theorem.** For all sufficiently large even $N$, $\mathfrak C$ is a disjoint union contained in the **original R32 minor arcs**. Uniformly over all moving hard $I\subseteq I_0$,
$$
 \left|\int_{\mathfrak C} F_I(\alpha)F_{I_0}(\alpha)e(-N\alpha)\,d\alpha\right|
 \ll_{\rho,\kappa}\frac{SN}{L\log L}. \tag{1}
$$
This is a pointwise signed Fourier estimate on a newly covered denominator range, not a bound on the whole remaining minor arc. The measure of these cores is $\asymp R_1^2/N\asymp N^{-\kappa/2}$, in contrast to $O(N^{-1/2})$ for the earlier arcs. To verify the geometry, core–core widths have sum $2/N<1/R_1^2$. A core of denominator $r$ and an R32 arc of denominator $s\le R_0$ have widths with sum at most $1/N+R_0/(sN)<1/(sr)$, since $2R_0R_1<N$. The measure follows from $\sum_{r\le X}\varphi(r)\sim 3X^2/\pi^2$, or by summing $\varphi(r)=r\sum_{d\mid r}\mu(d)/d$.

## 1. Preserve the moving hard cut by small Fourier energy at real edges

Put $M=\operatorname{rad}(NW)$ as in R32, so $K=M/\varphi(M)$, $K\ll L^2$, and $\tau(M)\le N^{\kappa/100+o(1)}$. The last estimate uses $W\le N^{\kappa/100}$ by Chebyshev at $z=\kappa L/1000$, and $2^{\omega(N)}=N^{o(1)}$. Set $\epsilon=L^{-40}$. Split the cofactor support into dyads $q\in[U,2U]$ and within each dyad into disjoint multiplicative intervals of ratio at most $1+\epsilon$ (at most $O(L^{41})$ bins in total). In a bin with reference point $q_0$ replace $qp\in I$ by $p\in Y=I/q_0$, with the inherited hard endpoint convention. Call the resulting whole transform $F_I^*$, independent of $r,a,\beta$. Its physical $n=qp$ support differs from the original selection only within distance $O(\epsilon N)$ of the two endpoints of $I$. Each integer $n$ in that support has at most $O_\kappa(1)$ distinct prime divisors $q\ge N^\kappa$ and total absolute coefficient $O_{\rho,\kappa}(L^2)$ in either transform. Hence
$$
 \|F_I-F_I^*\|_{L^2(\mathbb T)}^2\ll_{\rho,\kappa}(\epsilon N+1)L^4 . \tag{2}
$$
This approximation does not assume distribution of primes in the moving edge.

Write the R32 trace main term on every reduced core, with $r_q=r/(r,q)$ and $\Delta_N(d)=\mu(d){\bf1}_{d\nmid M}/\varphi(d)$, as
$$
 M_{I,r}(\beta)=
 \sum_{q\in\mathcal Q}\frac{\log q}{q}\Delta_N(r_q)
                 \int_I\frac{e(\beta t)}{\log(t/q)}\,dt .
$$
For $F_I^*$ replace $I$ separately for each $q$ by $I_q^*=qY$. This gives the corresponding main $M_{I,r}^*$. Indeed the R32 prime residue main measures and synthetic CRT main measures apply to an arbitrary real interval for each individual $q$; they are numerator-independent on reduced $a$. Here all $p$ in the actual or altered support are $\gg_\rho N^{1/2+\kappa}>r$, as required for the prime unit assertion. Uniformly on this real central neighborhood,
$$
 \sum_{q\in\mathcal Q}\frac{\log q}{q\log(t/q)}|\Delta_N(r_q)|
 \ll_\rho 1/\varphi(r).
$$
For $q\nmid r$ use $\sum_q\log q/q\ll L$, and for $q\mid r$ use $\varphi(r)/\varphi(r_q)\le q$ and $\sum_{q\mid r}\log q\le\log r$. Therefore Plancherel on $\beta\in\mathbb R$ bounds the squared model-difference energy at one $r$ (summing the reduced numerators) by $O_\rho(\epsilon N/\varphi(r))$. Summing gives $O_\rho(\epsilon NL^2)$, using $\sum_{r\le R_1}1/\varphi(r)\ll L^2$. The same profile bound gives $\|M_{I,\cdot}\|_{L^2(\mathfrak C)}^2\ll_\rho NL^2$.

## 2. Saving the cofactor factor on each hard product box

We prove
$$
 \|F_I^*-M_{I,\cdot}^*\|_{L^2(\mathfrak C)}^2
       \ll_{\rho,\kappa}N^{1-\kappa/3}. \tag{3}
$$
Fix a bin at scale $U$ and put $P=N/U$; its $p$ interval $Y$ stays in a fixed compact multiple of $P$. On $|\beta|\le1/N$ separate the smooth phase by the absolutely convergent expansion
$$
 e(\beta qp)=\sum_{j\ge0}\frac{(2\pi i\beta N)^j}{j!}
                               (q/U)^j(p/P)^j .
$$
Bounds below for the individual $j$'s can carry $C_\rho^j(j+1)$ in norm: the supremum and variation of the normalized $p$ weight on $Y$ have this bound, also after inserting $1/\log p$. The factorial makes summation uniform. Principal main measures after this summation retain the exact $e(\beta qp)$, not an approximated phase.

### Genuine prime part, $q$ a unit modulo $r$

Write the unit additive phase $e(a q p/r)$ by Dirichlet character inversion on $(\mathbb Z/r\mathbb Z)^\times$. For modulus $d$, Gauss coefficients satisfy $|\tau_d(\chi)|\le\sqrt d$ also for induced characters: inducing a primitive character of conductor $d_0\mid d$, inclusion–exclusion on extra prime exclusions reduces the complete sum to the single term indexed by $d/d_0$ if that term is coprime to $d_0$, and zero otherwise. Indeed every other complete sum over a nontrivial multiple of the primitive period vanishes by its additive progression. The remaining Gauss magnitude is at most $\sqrt{d_0}$. For any divisor $d$ of $r$, the unit cofactor character energy is
$$
 \frac1{\varphi(d)}\sum_{\chi\bmod d}
       \left|\sum_{\substack{q\ {\rm in\ bin}\\(q,r)=1}}A_j(q)\chi(q)\right|^2
 \ll C_\rho^{2j}L^2 U(1+U/d),\qquad A_j(q)=(\log q)(q/U)^j. \tag{4}
$$
Orthogonality reduces it to pairs of integers in the bin congruent modulo $d$; the prime restrictions and the $N$-unit exclusions need not be relaxed in the sum itself.

The GRH character PNT on the $p$ interval, after subtracting the principal integral, gives error $O_\rho(C_\rho^j(j+1)\sqrt P L^C)$ for each char mod $r$. This is the [weighted character estimate of Lee, Thm. 4.3 and Cor. 4.4](https://arxiv.org/html/2301.13457v2#S4) and partial summation, valid since $p\gg_\rho P>r$, with $p\mid N$ deletions negligible. Character Parseval in the numerator contributes $1/\varphi(r)$ times the sum of squared products of Gauss, cofactor, and prime-error coefficients. By (4) at $d=r$ the squared error summed over reduced $a$ is thus at most
$$
 \ll_\rho C_\rho^{2j}(j+1)^2 L^C rP\,U(1+U/r)
 \ll_\rho C_\rho^{2j}(j+1)^2 L^C N(r+U). \tag{5}
$$

### Synthetic part, $q$ a unit modulo $r$, including nonunit $p$

Expand the exact indicator $(p,M)=1$ by $\sum_{h\mid M}\mu(h){\bf1}_{h\mid p}$. Fix $h$ and stratify by $f=(p,r)$, $d=r/f$. Then $p=fv$, $(v,d)=1$, $h'=h/(h,f)\mid v$. A stratum is empty if $(h',d)>1$; otherwise $p=f h'k$ with $(k,d)=1$. Hence the additive phase is exactly $e(a q h'k/d)$ on units mod $d$, including when $p$ is not a unit mod $r$. No character expansion on nonunits of its own modulus has been used.

For $k$ in the resulting interval the nonprincipal character discrepancy in the smooth weight $(p/P)^j/\log p$ is at most $O_\rho(C_\rho^j(j+1)\tau(d)\sqrt d L^C)$ by [Pólya–Vinogradov](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primitive-characters-and-gauss-sums/267951F517AD4E1411297F5AC998CD4F) (Montgomery–Vaughan, Theorem 9.18; inclusion–exclusion on extra primes of an induced character would also suffice). The principal discrepancy versus $\varphi(d)/d$ times the real $k$ integral is bounded by $O_\rho(C_\rho^j(j+1)\tau(d)L^C)$ by the unit sieve. These are elementary bounds for all integers $k$, independent of the length and location of their interval. The factor $\chi(h')$ in the expansion has modulus one. The reduction of units mod $r$ to units mod $d$ is surjective with multiplicity $\varphi(r)/\varphi(d)\le r/d$. Character Parseval with (4) then bounds the squared error for this $h,f,j$ by
$$
 \ll_\rho C_\rho^{2j}(j+1)^2 L^C \tau(d)^2
      (r/d)d^2 U(1+U/d)
 \ll_\rho C_\rho^{2j}(j+1)^2 L^C \tau(d)^2N(r+U).
$$
The last step uses $d\le r$ and $rU\le N$. The main terms summed across $f,h$ are precisely the R32 CRT main measure: for fixed $h$, the strata partition the periodic set $h\mid p$, each with exact density $1/(f h')$ times the density of units in $k$ mod $d$. Hence there is no alteration to $\Delta_N(r_q)$ after recombination. Summing the norms for $h\mid M$, $f\mid r$ and the Taylor terms, and restoring $K$, costs at most $N^{\kappa/100+o(1)}L^C$ in norm. Equations (5) and this estimate give a per-bin integrated error of $N^{2\kappa/100+o(1)}L^C(R_1^2+UR_1)$ over the cores of width $2/N$. Summing the polylogarithmically many bins in norm and using $U\le N^{1/2-\kappa}$ and $R_1\le N^{1/2-\kappa/4}$ yields the bound in (3) for $q$ coprime to $r$.

### Shared primes $q\mid r$

For each $r$ there are $O_\kappa(1)$ such $q$. Work individually on its exact $Y$ for the perturbed indicator. Modulo $r_q=r/q$ the prime cumulative residue error has squared class norm $\ll_\rho P L^C$ by the R32 character argument. The synthetic class norm is $\ll_\rho\sqrt{r_q}K\tau(M)/L$, absorbed by the prime norm since $r_q/P=r/N\ll N^{-1/2}$ (here use $P=N/q$). With $|\beta|\le1/N$, Abel summation in $t=qp$ has bounded variation cost, and additive finite Parseval multiplies the class squared norm by $r$ when summing all $a\bmod r$. Including the $O_\kappa(1)$ choices and log markers gives per-denominator squared error $\ll_{\rho,\kappa}rN^{1-\kappa}L^C$. The width and sum over $r$ cost $O(R_1^2/N)$, giving $O_{\rho,\kappa}(N^{1-3\kappa/2}L^C)$. This proves (3) for the whole residual. All uses of $N^{o(1)}$ here can be bounded by a fixed small fraction of $\kappa$ in the exponent, since $\kappa$ is fixed.

## 3. Reassemble the true signed cores

From (2), (3) and the model-edge estimate, $\|F_I-M_{I,\cdot}\|_{L^2(\mathfrak C)}^2\ll_{\rho,\kappa} NL^{-30}+N^{1-\kappa/3}$. Cauchy–Schwarz against the main and the corresponding errors for $I_0$ makes all product errors $O_{\rho,\kappa}(NL^{-8})$. For the main product retain $e(-N\alpha)$ and first sum over reduced numerators, giving $c_r(N)$. If a nonsquarefree $r$ has a surviving main coefficient, it must be $q^2h$ for a cofactor prime $q\in\mathcal Q$, squarefree $h$ coprime to $q$; then $q\nmid N$ makes $c_r(N)=0$. Squarefree $r\mid M$ have zero signal. In the remaining terms the same $O_\rho(N/\varphi(r))$ profile bound and the width $2/N$ give
$$
 \ll_\rho N\sum_{\substack{r\ {\rm squarefree}\\r\nmid M}}
             |c_r(N)|/\varphi(r)^2
 \ll_{\rho,\kappa}\frac{SN}{L\log L}.
$$
This is the R32 signed singular tail: the positive Euler product is $O(S)$ and every retained term contains a prime $\ell>z,\ell\nmid N$, whose tail coefficients are $O(\ell^{-2})$. This proves (1) for the exact original hard windows. No absolute value was taken on the rational main product before summing its numerator phase.

Only the complement of both R32 major arcs and these new narrow cores still needs a bound for the signed same-target covariance; controlling the wider arcs near those fractions, or the rest of the circle, is not claimed. Since $F_{I_0}$ stays fixed, the new core contribution is an additive functional of the first interval and the estimate passes by Abel summation to the bounded-variation central cumulative weight. Neither the full weak-S operator nor Goldbach is established.