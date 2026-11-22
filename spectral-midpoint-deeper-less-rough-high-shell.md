# Cancellation in a deeper genuine less-rough high-LCM shell

**Scope.** This extends the [moving-roughness midpoint bounds](spectral-midpoint-complementary-blocks-moving-roughness.md) for the actual sharp-cut mixed product, not just for the full midpoint surrogate. It controls the signed net contribution from a growing shell of previously excluded less-rough partners. The threshold is lowered from $\exp(100\log N/\log\log N)$ to $\exp((\log N)^\alpha)$ for each fixed $3/4<\alpha<1$. The proof is unconditional, simultaneously in every original central cell for almost all even moduli. It does not control prescribed exceptional moduli or partners with still smaller least factors, and does not imply weak S.

Write $N\in[X,2X]$, $L=\log N$, $\ell=\log X$, $m=N-n$, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Let $\Sigma(N)$ be the binary singular series. Fix $J\ge1$ and the original half-open cells $I$ of length $H=N/(16\lceil L^J\rceil)$ in $(N/2,9N/16]$. Fix $B>0$ and $D=\sqrt N L^{-B}$. Use the exact [cut low and high blocks](spectral-midpoint-complementary-blocks-moving-roughness.md):

$$
 \mathcal L_z=\sum_{\substack{n\in I\\m\ {\rm squarefree},\,P^-(m)\ge z}}
                  \lambda(n)F_{0,D}(m),\qquad
 \mathcal H_z=\sum_{\substack{n\in I\\m\ {\rm squarefree},\,P^-(m)\ge z}}
                  \lambda(n)(F_{0,D}(m)F_{1,D}(m)-F_{0,D}(m)).
$$

Here $F_{0,D}$ and $F_{1,D}$ use the sharp cutoff $d\le D$ and weights $\mu(d)$ and $\mu(d)(1-2\log d/\log m)$, respectively. For any $A_0>0$, outside one set of $O_{\alpha,B,J,A_0}(X\ell^{-A_0})$ even moduli in the dyad, uniformly in all their cells, the new cutoff $z_\alpha(N)=\exp(L^\alpha)$ satisfies

$$
 \begin{split}
 |\mathcal L_{z_\alpha(N)}|
      &\ll_{\alpha,B,J,A_0}
           \frac{\Sigma(N)H(1+\log L)}{L^{4\alpha-2}},\\
 \mathcal H_{z_\alpha(N)}
      &=\frac{\Sigma(N)H}{L}
          +O_{\alpha,B,J,A_0}
                 \left(\frac{\Sigma(N)H(1+\log L)}{L^{4\alpha-2}}\right).
 \end{split}                                                       \tag{1}
$$

In particular at $\alpha=9/10$, the error is $O(\Sigma(N)H/L^{3/2})$. Subtract the preceding bounds at $z_{\rm old}(N)=\exp(100L/\log L)$ (which is greater than $z_\alpha(N)$ for all sufficiently large $N$). On

$$
               z_\alpha(N)\le P^-(m)<z_{\rm old}(N)
\tag{2}
$$

the separate **true signed** low and high contributions are both
$O(\Sigma(N)H[(1+\log L)L^{2-4\alpha}+L^{-9/5}])$, with no main term. The same statement on this shell holds if the squarefree gate is omitted, since the discarded rough nonsquarefree terms are smaller than any inverse-log target. This is a signed comparison of actual arithmetic sums, not an absolute-mass bound on (2).

## 1. A cofactor-weighted sieve for exact midpoint restoration

Freeze roughness at $z=\exp(\ell^\alpha)=X^b$, $b=\ell^{\alpha-1}$. For all large $X$, this is no larger than $z_\alpha(N)$, and the ratio is at most two by the mean-value theorem applied to $u^\alpha$ for $u\in[\ell,\ell+\log2]$.

The following consequences of the [rough-cofactor sieve](spectral-midpoint-lcm-complement-frontier.md) hold here with uniform constants. For any rough modulus $q\le N^{4/5}$ let $M_I(q)$ be the $\lambda$-mass on $n\in I$ with $q\mid m$ and $m/q$ rough. There is no contribution if $(q,N)>1$. Otherwise

$$
 M_I(q)\ll \frac{\Sigma(N)H}{bL\varphi(q)}
                +L^2(H/q)^{1/2}.                              \tag{3}
$$

To see uniformity, sieve the integer cofactor in its actual interval of length $U=H/q$. At primes below $Y=U^{1/100}$ exclude the root of the form $N-qx$ when one exists, and below $z$ also exclude $x\equiv0$. Here $\log U\gg L$ and $Y>z$ for large $N$, since $b\to0$. At primes dividing $q$ the first root is absent; these primes are not below $z$. At primes dividing $N$ below $z$ the roots coincide, including at $2$. The other primes below $z$ have two distinct roots. Thus the sieve product is $\prod_{p<Y,\ p\nmid q}(1-1/p)$ times $V_z=\prod_{p<z,\ p\nmid N}(1-1/(p-1))\ll\Sigma(N)/(bL)$. The latter uniform comparison follows from Mertens and the singular factors, since even the count $L/\log z$ of omitted large divisors of $N$ gives negligible total reciprocal above $z$. The [dimension-two upper sieve](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/) at level $U^{1/2}$ has CRT error $O(2^{\omega(a)})$ per squarefree sieve modulus $a$; their sum is $O(U^{1/2}\log(2U))$. Both the product and remainder yield (3) after weighting by $L$. This proof needs no primality of the cofactor.

Also, uniformly in this roughness range,

$$
  \sum_{\substack{a\le N\\a\text{ rough}}}\frac1{\varphi(a)}
       \ll b^{-1},\qquad
  \sum_{\substack{D<d\le\sqrt N\\d\text{ rough}}}
                    \frac{\tau(d)}{\varphi(d)}
       \ll_B \frac{1+\log L}{b^2L}.                            \tag{4}
$$

The first follows by extending to the positive Euler product over $z\le p\le N$: the local added mass $\sum_{j\ge1}1/\varphi(p^j)$ is $1/p+O(1/p^2)$, so the product is $O(\log N/\log z)$. In the second, $d/\varphi(d)\le2$ uniformly for large $X$, since there are at most $L/\log z$ primes, all at least $z$. On each dyad $d\in[R,2R]$, majorize $\tau(d)$ by twice the incidences $u\mid d,\ u\le\sqrt{2R}$. Then $u$ and $d/u$ are rough. The dimension-one upper sieve up to $z^{1/3}$, at level $(R/u)^{1/2}$, bounds this second integer in its interval of length $R/u$ by
$O(R/(ubL)+(R/u)^{1/2})$: the CRT error per squarefree modulus is bounded, and the fundamental-lemma parameter is at least one because $R\gg \sqrt N/L^B$ and $b\to0$. Summing over rough $u$ by the first bound in (4) and over all $u$ for the errors bounds the dyadic divisor mass by $O(R/(b^2L)+R^{3/4})$. Divide by $R$ and sum $O_B(1+\log L)$ dyads. The power remainder is negligible.

Let $E_\tau$ denote the positive critical incidence

$$
 E_\tau=\sum_{\substack{n\in I\\ m\ {\rm squarefree},\,P^-(m)\ge z}}
       \lambda(n)\tau(m)
          \sum_{\substack{d\mid m\\D<d\le\sqrt m}}1.
$$

For a contributing $d$ put $y=m/d$. Then $\tau(m)\le\tau(d)\tau(y)$; apply the divisor hyperbola bound $\tau(y)\le2\sum_{a\mid y,\ a\le\sqrt y}1$. Both $d,a$ and the remaining cofactor are rough. Here $d\le\sqrt N$ and $a\le N^{1/4}L^{B/2}\le N^{.26}$ for large $N$, since $d>D$. Thus $q=da\le N^{.76}$, where (3) applies, and $1/\varphi(da)\le1/(\varphi(d)\varphi(a))$. Sum its main terms using (4). For the power error, one may drop roughness and use
$\sum_{d\le\sqrt N}\tau(d)d^{-1/2}\ll N^{1/4}L$ and
$\sum_{a\le N^{.26}}a^{-1/2}\ll N^{.13}$.
This proves

$$
 E_\tau\ll_B
       \frac{\Sigma(N)H(1+\log L)}{b^4L^2}+N^{.88}L^3.          \tag{5}
$$

For each retained partner, the difference between the full and cut $F_j$ is bounded by the critical incidence with all weights at most one. The product difference is then at most twice $\tau(m)$ times that incidence. Thus (5) controls the passage from the full to the sharp-cut low and high blocks, in absolute value on the genuine sequence, without a factor $2^{O(1/b)}$.

The same argument restores the **moving rough threshold**. A changed term has a prime $r\in[z,2z]$ and rough cofactor. Majorize $\tau(m)$ by $2\tau(m/r)$ and apply the hyperbola bound to $m/r$; here its small divisor is $\le\sqrt N$, so $ra\le N^{.51}$ eventually. The sum of $1/\varphi(r)$ over the prime interval is $O(1/(bL))$, and the rough divisor sum is $O(b^{-1})$. The cost in either full test is therefore $O(\Sigma(N)H/(b^3L^2)+N^{.76}L^2)$ by (3) and elementary summation of its remainder. One may either restore $z_\alpha(N)$ after restoring the sharp cut, applying (5) to the frozen threshold as an upper bound on the true critical incidences at the tighter threshold, or compare the full tests first. No factor $\sup\tau$ is needed.

Finally on both thresholds of (2), nonsquarefree rough partners count $O(N/z)$, by summing over their prime square divisors. The cut weights have absolute value at most $O(\tau(m)^2)$; Cauchy--Schwarz and $\sum_{m\le N}\tau(m)^4\ll NL^{15}$ give $O(NL^{17/2}/\sqrt z)$ for these true prime-position weights. This proves the optional gate removal stated above, which applies only on rough partners or the intervening shell.

## 2. Full genuine coefficients: circle transfer with divisor moments

On squarefree partners denote by $F_j$ the full midpoint versions with $d<\sqrt m$. The full high coefficient is $G(m)=-F_0(m)$ if $m$ has odd factor count at least three, and zero otherwise, by the [exact high-LCM parity identity](spectral-midpoint-lcm-complement-frontier.md). In each proof below take $g_X(m)$ to be either full coefficient restricted to squarefree $z$-rough $m$ in $V=[X/3,2X]$, and zero off $V$. It is independent of $N$, and $|g_X(m)|\le\tau(m)$. Thus its Fourier polynomial $T_X$ has squared torus norm $O(X\ell^3)$ by the ordinary divisor moment (one may bound $\tau^2\le d_4$).

Use the same exact largest-prime decomposition as in the [Dickman transfer](spectral-midpoint-odd-aggregate-dickman.md). Write $m=cp$ with sorted prefix $c$ and unique largest prime $p$; on the low prime term $c=1$. For fixed $c$, the short divisor part is

$$
 w_c(y)=\sum_{a\mid c}\mu(a)
              \big(\mathbf1_{a^2<cy}-\mathbf1_{a^2 y<c}\big).
$$

The high version takes its negative on odd factor count at least three. On $c=1$ the low coefficient is one. For either version the absolute value and the total variation of this piecewise constant factor with its gate $y\ge z$, $y>P^+(c)$ are $O(\tau(c))$, because each individual indicator has bounded variation and the gates add only endpoints. Let $a_X(x)$ be the exact real model obtained by replacing the final prime sum by measure $dy/\log y$, with $y=x/c$. Thus each prefix contributes its signed, gated $w_c(x/c)/(c\log(x/c))$. For any fixed nonnegative integer $j$, the prefix bound

$$
 \sum_c\frac{\tau(c)^j}{c}
   \le\prod_{z\le p\le2X}(1+2^j/p)\ll_j b^{-2^j}               \tag{6}
$$

uses squarefree $c$ and Mertens. Therefore the supremum and total variation of $a_X\mathbf1_V$ are $O((b^3\ell)^{-1})$, using $j=1$ and $\log(x/c)\ge b\ell$ on the support.

For a hard fixed first interval $U\subset V$, let $P_U(\theta)=\sum_{n\in U}\lambda(n)e(n\theta)$. Take the arc denominator bound $Q=\ell^C$ and widths $2Q/X$ as in the previous proof. On major arcs $a/q+\eta$, [Siegel--Walfisz](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF), applied to the final prime in each signed interval, gives

$$
 T_X(a/q+\eta)=\frac{\mu(q)}{\varphi(q)}
     \int_V a_X(x)e(\eta x)\,dx+O_{\alpha,C,T}(X\ell^{-T})
$$

for every fixed $T$. Indeed $\log(X/c)\ge b\ell-O(1)$ on contributing prefixes, so $q\le \ell^C$ is at most a sufficiently large fixed power of $\log(X/c)$; all primes exceed $q$ and multiplication by $c$ permutes the unit classes. The prime theorem has exponential error in $\sqrt{\log(X/c)}\gg\ell^{\alpha/2}$. Partial summation, the reduced residue count, and the number and sizes of signed subintervals lose at most powers of $Q$ and $\tau(c)^2$ for each prefix. The total prefix loss is polynomial in $\ell$ by (6) with $j=2$. Isolated endpoints cost at most the same and are absorbed since $X/c\gg z$. The model for $P_U$ has the same factor with the indicator density of $U$.

On the minor arcs the [Vaughan estimate](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=77) gives $\sup|P_U|\ll_E X\ell^{-E}$ for arbitrary fixed $E$ upon enlarging $C$. By Parseval for $T_X$ and Bessel for the minor coefficient at $N$, its squared sum is $O_E(X^3\ell^{3-2E})$. The major model is the same truncated Ramanujan sum times the real Fourier convolution. The summed absolute Ramanujan tail is $O(XQ^{-1/2})$ by the earlier dyad argument, so outside $O(X\ell^2Q^{-1/2})$ moduli it is $O(\ell^{-2})$. The transform of $a_X$ has high-frequency decay $O((b^3\ell|\eta|)^{-1})$ by total variation, so the singular integral tail beyond $2Q/X$ is $O(X/(Qb^3\ell))$ before its singular factor. All these losses fit $O(\Sigma(N)H/L^2)$ by taking $C$ and the major-arc approximation precision sufficiently large, using the bounds on $\ell$ and $b$ above.

For completeness, moving physical endpoints now use a divisor estimate rather than a supremum. Freeze cells at mesh $\delta=X\ell^{-J-5}$, also cutting at changes of $\lceil(\log N)^J\rceil$. There are $O_J(\ell^{2J+5})$ fixed intervals $U$ in this cover. At a target $N$ in each piece the endpoint discrepancy has length $O(\delta)$, and on any such integer interval
$\sum\tau(m)\ll\delta L+\sqrt X$ by the divisor hyperbola bound and counting multiples at each small divisor. The discrete weighted error is therefore $O(\delta L^2+\sqrt X L)=o(H/L^2)$. The continuum endpoint error is $O(\delta/(b^3\ell))$ before its singular factor. Apply the Bessel bound at threshold $X\ell^{-J-2}$ and union over all fixed intervals and both coefficients; $E$ can make the exception $O(X\ell^{-A_0})$. Thus in every original cell on the same good moduli the true sum is

$$
                  \Sigma(N)\int_I a_X(N-u)\,du
                     +O(\Sigma(N)H/L^2).                    \tag{7}
$$

## 3. The degree-growing simplex limit

The continuum density can still be evaluated at this much lower roughness cutoff. Here the factor count is at most $K=\lfloor2/b\rfloor=O(\ell^{1-\alpha})$. Put $\xi=\log x/\ell=1+O(1/\ell)$ for $x\in V$, and define exponent measures

$$
 \nu_X=\sum_{z\le p\le2X}\frac1p\,\delta_{\log p/\ell},
 \qquad
 \nu(dt)=\mathbf1_{b\le t\le\log(2X)/\ell}\frac{dt}{t}.
$$

Their total masses are $O(1+\log(1/b))$ and their mass difference on any interval is $O(\exp(-c\ell^{\alpha/2}))$, by the usual prime-number-theorem error and partial summation. Choose a fixed exponent $\gamma$ with $1-\alpha<\gamma<\alpha/2$ (possible here), and a bin mesh $\Delta=\exp(-\ell^\gamma)$. Collapsing each bin to one representative makes the total variation difference of the binned measures $O(\Delta^{-1}\exp(-c\ell^{\alpha/2}))$. In a $j$-fold product the difference is bounded by this times $j$ and the $(j-1)$-st power of the maximum total mass, by telescoping.

For $k$ factors use $t_k=\xi-\sum_{i<k} t_i$. The exact sign and gate inequalities for the density in (7) are the same linear midpoint, lower-prime-cut, and ordering inequalities as in the previous proof. There are $O(k+2^k)$ boundary planes. Every nonconstant plane has one coefficient of magnitude at least one; all coefficients are bounded absolutely. A bin product can change a comparison only in a strip of width $O(K\Delta)$. For any such strip, the continuous product mass is at most

$$
 O(K\Delta/b)\big(O(1+\log(1/b))\big)^{k-2}
$$

by integrating a coordinate with coefficient bounded below. The union of entire bins that touch the strip satisfies the same estimate with a larger width, and its discrete mass is bounded by this and the binned-product discrepancy. Off the strips the sign is constant on the bins, its absolute value is at most $2^K$, and the reciprocal $1/t_k$ on the support varies by at most $O(K\Delta/b^2)$. This also controls ordering diagonals, so no squarefree multiplicity term is missing. For $k=1$ there is no grid. Summing over $k\le K$ gives $o(\ell^{-T})$ for every fixed $T$: all factors from counts, product masses, and magnitudes are $\exp(O(K\log(2+\log(1/b))+K+\log(1/b)))=\exp(o(\ell^\gamma))$, whereas the bin discrepancy also has $\ell^{\alpha/2}$ dominating $\ell^\gamma$.

Scale the continuous simplex variables by $\xi$, preserving the relative midpoint and producing a factor $\xi^{-1}$, with new rough parameter $b/\xi$. Permutation symmetry gives the same ordered factor $1/k!$ as before. The [Dickman constants](spectral-midpoint-complementary-blocks-moving-roughness.md) of the low and high tests are $\varepsilon_{b/\xi}$ and $1-\varepsilon_{b/\xi}$, respectively. These are exact constants of the continuous models at each parameter, not a uniformity deduction from a fixed-dimensional limit. The factorial bound for $\varepsilon$ implies that it is $o(\ell^{-T})$ for every fixed $T$ since $1/b=\ell^{1-\alpha}$. Thus uniformly for $x\in V$ the low model is $o(\ell^{-T})$ for arbitrary fixed $T$, and the high model is $1/\log x+O(\ell^{-2})$. In (7) one has $\log(N-u)=L+O(1)$ throughout the central cells. This yields full low $O(\Sigma H/L^2)$ and full high $\Sigma H/L+O(\Sigma H/L^2)$ before the two restorations.

Finally (5) and the rough gate change cost $O(\Sigma H(1+\log L)/(b^4L^2))$, with power errors negligible. Since $b\asymp L^{\alpha-1}$, this is precisely the error in (1) and is $o(\Sigma H/L)$ when $\alpha>3/4$. This proves (1) and the signed less-rough shell conclusion for the original sharp cut. It does not identify or estimate the remaining high block below $z_\alpha(N)$.
