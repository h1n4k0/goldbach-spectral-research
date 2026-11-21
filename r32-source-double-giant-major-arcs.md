# Major arcs of the genuine two-prime interior covariance

Assume global Dirichlet GRH. Fix $0<\rho<1/2$, $0<\kappa\le1/2000$, and take all sufficiently large even $N$. Use $L=\log N$, $S=\mathfrak S(N)$, $I_0=[\rho N,(1-\rho)N]$, and any moving hard interval $I\subseteq I_0$, with either endpoint convention. This controls a Fourier part of the remaining **two-sided** covariance, not the one-sided terms or a pointwise Goldbach count.

As in the [one-sided centering theorem](r31-source-double-giant-one-leg-centering.md), let $\mathcal Q=\{q\text{ prime}:N^\kappa\le q\le N^{1/2-\kappa},\ (q,N)=1\}$, $z=\kappa L/1000$, $W=\prod_{\ell\le z,\,\ell\nmid N}\ell$ over primes, and $K=(N/\varphi(N))(W/\varphi(W))$. For centrally occurring $p$ put $b(p)=K{\bf1}_{(p,W)=1}/\log p$ and $\xi(p)={\bf1}_{p\text{ prime}}-b(p)$. With $e(t)=e^{2\pi it}$ put

$$
 F_I(\alpha)=\sum_{\substack{q\in\mathcal Q,\,p\ge1\\qp\in I,\ (p,N)=1}}
          (\log q)\,\xi(p)e(\alpha qp).
$$

The exact same-target covariance with the original unit masks is

$$
 [\xi,\xi]_I=\int_{\mathbb T}F_I(\alpha)F_{I_0}(\alpha)e(-N\alpha)\,d\alpha .
 \tag{1}
$$

By orthogonality $qp+se=N$, so $se\in I_0$ automatically and $q=s$ is impossible by the units. Holding the second factor fixed makes each partial-circle coefficient additive in the first interval. Set $R=\lfloor N^{1/4}\rfloor$, $B_r=R/(rN)$, and take

$$
 \mathfrak M=\bigcup_{r\le R}\ \bigcup_{a\bmod r,\ (a,r)=1}
               \{\alpha:\|\alpha-a/r\|\le B_r\},\qquad
 \mathfrak m=\mathbb T\setminus\mathfrak M .
$$

The arcs are disjoint, since distinct reduced rationals have circle separation at least $1/(r_1r_2)$ and $2R^2<N$.

**Theorem.** Uniformly over these hard intervals and the full fixed cofactor exponent interior,

$$
 \left|\int_{\mathfrak M} F_I(\alpha)F_{I_0}(\alpha)e(-N\alpha)\,d\alpha\right|
 \ll_{\rho,\kappa}N^{1-\kappa/3}+\frac{SN}{L\log L}. \tag{2}
$$

For an interval $I$ of positive proportional length, the complementary energy satisfies

$$
 \int_{\mathfrak m}|F_I(\alpha)|^2d\alpha\gg_{\rho,\kappa}|I|L . \tag{3}
$$

Thus taking absolute values of the actual minor integrand in (1) for $I=I_0$ cannot yield $o(SN)$. This is not a lower bound for the **signed** minor coefficient.

## 1. The numerator-independent arc main term

Put $M=\operatorname{rad}(NW)$, $r_q=r/(r,q)$ and $a_q=aq/(r,q)$, so $a_q$ is reduced modulo $r_q$, even when $q\mid r$. Write

$$
 \Delta_N(d)=\frac{\mu(d)}{\varphi(d)}{\bf1}_{d\nmid M},\qquad
 G_r(t)=\sum_{q\in\mathcal Q}\frac{\log q}{q\log(t/q)}\Delta_N(r_q),
 \qquad M_{I,r}(\beta)=\int_I G_r(t)e(\beta t)\,dt.
$$

For fixed $q$, all centrally occurring $p$ satisfy $p\ge \rho N^{1/2+\kappa}>R$, so no genuine prime is nonunit mod $r_q$. In each residue $u\bmod r_q$ the genuine prime main measure is $\mathbf1_{(u,r_q)=1}\,dt/(\varphi(r_q)q\log(t/q))$, where $t=qp$. Its additive transform over $u$ gives the factor $\mu(r_q)/\varphi(r_q)$ for reduced $a_q$.

For the synthetic term, the two unit restrictions at $W$ and $N$ combine as $\sum_{h\mid M,\ h\mid p}\mu(h)$. In the class $u\bmod r_q$ the density of $h\mid p$ is $\mathbf1_{(h,r_q)\mid u}/[h,r_q]$ in the $p$ coordinate. Summing this density times $e(a_q u/r_q)$ over $u$ gives zero unless $r_q\mid h$, when the sole residue is zero and the density is $1/h$. Including $K=M/\varphi(M)$ yields $K\sum_{h\mid M,\,r_q\mid h}\mu(h)/h$, equal to $\mu(r_q)/\varphi(r_q)$ if $r_q\mid M$, and zero otherwise. This proves the stated main term $M_{I,r}$ for the difference, independently of $a$.

One integration by parts gives $\int_I e(\beta t)/\log(t/q)\,dt=O_\rho(L^{-1}\min(N,|\beta|^{-1}))$, with the usual convention at zero. For $q\nmid r$ use $\sum_{q}(\log q)/q\ll L$; for $q\mid r$ use $\varphi(r)/\varphi(r_q)\le q$ and $\sum_{q\mid r}\log q\le\log r$. This gives

$$
 |M_{I,r}(\beta)|\ll_\rho \varphi(r)^{-1}\min(N,|\beta|^{-1}). \tag{4}
$$

For squarefree $r\mid M$ the main term vanishes. A nonsquarefree $r$ can have any nonzero main summand only if $r=q^2h$ for some $q\in\mathcal Q$, squarefree $h$ coprime with $q$: division by the single prime $q$ must make $r_q$ squarefree. Then $q\nmid N$ gives $c_r(N)=0$ for the Ramanujan sum. These statements distinguish zero covariance main terms from the individual signals at nonsquarefree denominators.

## 2. The integrated error, with exact hard endpoints

Write $E_I(a/r+\beta)=F_I(a/r+\beta)-M_{I,r}(\beta)$. We claim

$$
 \int_{\mathfrak M}|E_I|^2d\alpha
 \ll_{\rho,\kappa} N^{1/2-\kappa}R^2 L^C
 \ll_{\rho,\kappa} N^{1-\kappa}L^C . \tag{5}
$$

For fixed $q,r,I$ write $P=N/q$. Let $D_u(x)$ be the cumulative discrepancy of the actual residual measure against the §1 prime-minus-synthetic main measure in class $u\bmod r_q$, taken on $I\cap(-\infty,x]$ in the raw coordinate $t=qp$. Uniformly in $x$,

$$
 \sum_{u\bmod r_q}|D_u(x)|^2\ll_{\rho,\kappa} P L^C . \tag{6}
$$

For the genuine prime part the nonunits are identically zero. On the units, character Parseval gives the sum of squared class discrepancies as the average of squared character discrepancies. Each is $O_\rho(\sqrt P L^C)$ under the GRH character PNT, for example [E. S. Lee, Theorem 4.3 and Corollary 4.4](https://arxiv.org/html/2301.13457v2#S4) and partial summation after removing $\log p$. The relevant $p$ endpoints are $\asymp_\rho P$ and exceed $r_q$; modulus $1$ or $2$ reduces to ordinary RH. Deleting the at most $\omega(N)$ primes dividing $N$ is within this character error. The character average in (6) does not cost an additional factor $r_q$. For the synthetic part CRT and Abel summation against $1/\log p$ give per-class error $O_\rho(K\tau(M)/L)$, even in nonunit classes. Its residue norm is therefore $O_\rho(\sqrt{r_q}K\tau(M)/L)\ll_{\rho,\kappa}\sqrt P L^C$, since $r_q\le N^{1/4}$, $P\ge N^{1/2+\kappa}$, $K\ll L^2$, and $\tau(M)\le N^{o(1)}N^{\kappa/100}$ by $2^{\omega(N)}=N^{o(1)}$ and Chebyshev at $z=\kappa L/1000$. This proves (6).

For $I$ ending at $Y$, Stieltjes integration in each residue gives the error transform as $e(\beta Y)D_u(Y)-2\pi i\beta\int_I e(\beta x)D_u(x)\,dx$, where $D_u(Y)$ means total mass with the prescribed endpoint convention. From (6), using real-line Plancherel for the second term, the integrated squared class norm on $|\beta|\le B_r$ is $O_{\rho,\kappa}(P L^C(B_r+N B_r^2))$. Additive finite Parseval multiplies by $r_q$ on summing all numerators mod $r_q$, or by $r$ on summing all $a\bmod r$, since $a\mapsto a_q\bmod r_q$ has constant multiplicity $r/r_q$. Restricting to reduced numerators decreases the nonnegative error sum; the main coefficient was needed only on that restricted set. Minkowski with the $\log q$ weights now gives squared error at denominator $r$ at most

$$
 \ll_{\rho,\kappa}r(B_r+N B_r^2)L^C
          \left(\sum_{q\in\mathcal Q}(\log q)\sqrt{N/q}\right)^2
 \ll_{\rho,\kappa}r(B_r+N B_r^2)N^{3/2-\kappa}L^C .
$$

The last inequality even follows by summing over all integers $q\le N^{1/2-\kappa}$. Since $\sum_{r\le R}r(B_r+N B_r^2)\ll R^2 L/N$, this proves (5). No moving endpoint was smoothed.

## 3. The signed major contribution is small

From (4), $\|M_{I,\cdot}\|_{L^2(\mathfrak M)}^2\ll_\rho N\sum_{r\le R}1/\varphi(r)\ll N L^C$; likewise for $I_0$. Cauchy–Schwarz and (5) bound every term with at least one error in the integrated product by $O_{\rho,\kappa}(N^{1-\kappa/3})$ after absorbing log powers. In the remaining product, sum the reduced numerators before taking absolute values, obtaining $c_r(N)$; no nonsquarefree contribution remains. The squarefree term is bounded by

$$
 \ll_\rho N\!\!\sum_{\substack{r\ {\rm squarefree}\\r\nmid M}}
           \frac{|c_r(N)|}{\varphi(r)^2}
 \ll_{\rho,\kappa}\frac{SN}{L\log L}.
$$

The last bound follows from the exact local coefficients $1/(\ell-1)$ at $\ell\mid N$ and $1/(\ell-1)^2$ elsewhere. The full nonnegative Euler product is $O(S)$, since the first family contributes $N/\varphi(N)$ and the other factors converge absolutely; the convergent good-prime factors in $S$ have absolute positive lower product. Every retained $r\nmid M$ contains a prime $\ell>z$ with $\ell\nmid N$, giving a further factor $O(\sum_{\ell>z}\ell^{-2})=O_\kappa((L\log L)^{-1})$ by Chebyshev on dyadic prime ranges. This proves (2).

## 4. A positive amount of genuine minor energy remains

For $|I|\asymp N$ Parseval on $\mathbb T$ gives

$$
 \int_{\mathbb T}|F_I|^2
 = |I|L\,(d_\kappa+o(1)),\quad
 d_\kappa=\int_\kappa^{1/2-\kappa}\frac{v\,dv}{1-v},\qquad
 c_\kappa=\log\!\left(\frac{1-\kappa}{1/2+\kappa}\right).
 \tag{7}
$$

The genuine prime portion has unique $qp$ representations since $q<p$, with $q<N^{1/2}$ and $p>N^{1/2}$ for all large $N$. Its energy is the sum of $(\log q)^2$ over those semiprimes. The prime count for each $q$ has main $(1/q)\int_I dt/\log(t/q)$ and ordinary RH error $O_\rho(\sqrt{N/q}L^C)$, including deletion of primes dividing $N$. The summed weighted errors are $o(NL)$. Replacing $\log(t/q)$ by $L-\log q$ costs $O_\rho(N)$. Partial summation against $\sum_{\ell\le x,\ \ell\text{ prime}}(\log\ell)/\ell=\log x+O(1)$ gives $Ld_\kappa+O_{\rho,\kappa}(1)$ for the resulting prime harmonic sum. Deleting $q\mid N$ in this polynomial range is negligible since there are at most $1/\kappa$ of them. Meanwhile each synthetic coefficient is $O_{\rho,\kappa}(K)$, by the divisor count for primes $\ge N^\kappa$ and the log ratio bound. Here $K\ll(\log L)^2$: split the primes dividing $N$ at $L$, use Mertens below and $\sum_{\ell\mid N,\ell>L}1/\ell\le 1/\log L$ above, and use Mertens at $z$ for $W$. The synthetic energy and its cross term are $o(NL)$, proving (7).

Put $g_q(t)=\log q/(q\log(t/q))$. The same partial summation gives $\sum_qg_q(t)=c_\kappa+o_{\rho,\kappa}(1)$ uniformly on $I_0$. For squarefree $r\nmid M$, $G_r(t)$ is $\mu(r)/\varphi(r)$ times this last sum minus a nonnegative correction inside the bracket. A divisor $q\in\mathcal Q$ of $r$ subtracts $g_q(t)$ if $r_q\mid M$, and $qg_q(t)$ otherwise, since $\mu(r/q)=-\mu(r)$ and $\varphi(r)/\varphi(r/q)=q-1$. The total correction is at most $\log r/(L-\log r+O_\rho(1))\le 1/3+o_\rho(1)$, whereas $c_\kappa>0.69$. The absolute bracket is thus at most $c_\kappa+o_{\rho,\kappa}(1)$. For squarefree $r\mid M$ the bracketed term is zero. Real Plancherel bounds the squarefree major-signal energy by

$$
 |I|(c_\kappa^2+o_{\rho,\kappa}(1))
          \sum_{r\le R}\frac{\mu^2(r)}{\varphi(r)}
 = |I|L(c_\kappa^2/4+o_{\rho,\kappa}(1)).
$$

For the reciprocal-totient estimate, $\mu^2(n)/\varphi(n)$ is the convolution of $1/n$ with the multiplicative function having $h(\ell)=1/(\ell(\ell-1))$, $h(\ell^2)=-h(\ell)$ and $h(\ell^j)=0$ for $j\ge3$. The total sum $\sum_n h(n)$ is one and $\sum_n|h(n)|(1+\log n)<\infty$, so the reciprocal-totient sum is $\log R+O(1)$. For nonsquarefree signals $r=q^2h$ of §1 their weighted reciprocal mass $\sum 1/\varphi(r)$ is $O(L\sum_{q\ge N^\kappa}q^{-2})=O(LN^{-\kappa})$ by this same harmonic estimate on squarefree $h$. Their major energy is $o(|I|L)$ by the pointwise bound $O_\rho(1/\varphi(r))$ on $G_r$ and real Plancherel, even though those signals must not be discarded before taking energy. The error (5) and its cross term are $o(|I|L)$. Finally $d_\kappa=c_\kappa-(1/2-2\kappa)$ gives $d_\kappa-c_\kappa^2/4>0.06$ throughout $0<\kappa\le1/2000$, using $0.69<c_\kappa<0.70$. Subtracting this major-energy upper bound from (7) proves (3).

## 5. Exact remaining input

The missing bound for this sector is $\sup_{I\subset I_0}|\int_{\mathfrak m}F_I(\alpha)F_{I_0}(\alpha)e(-N\alpha)d\alpha|=o_{\rho,\kappa}(SN)$, or true compensation against other sectors. Because the second factor in (1) is fixed, (2) transfers by Abel summation to central cumulative tests with the bounded-variation weight $\sqrt{(t/N)(1-t/N)}$, but the arc decomposition is a Fourier split rather than a pairwise arithmetic restriction. No estimate for the remaining signed coefficient, the full operator, or Hypothesis S is claimed.