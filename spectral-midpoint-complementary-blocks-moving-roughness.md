# Complementary true midpoint blocks and a moving roughness cutoff

**Scope.** This unconditionally evaluates the low midpoint block complementary to the [Dickman high-LCM term](spectral-midpoint-odd-aggregate-dickman.md), including the opposite signs on each fixed least-factor shell. It also carries both blocks to an explicit subpolynomial roughness cutoff tending down in exponent. The estimates hold simultaneously in every central cell for almost all even moduli. They do not control prescribed exceptional moduli, the remaining less-rough composite blocks, or Hypothesis S.

Use the notation of the [Dickman proof](spectral-midpoint-odd-aggregate-dickman.md): $N\in[X,2X]$ is even, $L=\log N$, $\ell=\log X$, $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$, $m=N-n$, and $\Sigma(N)$ is the usual binary singular series. Fix $J\ge1$ and use its original central cells $I$ of length $H=N/(16\lceil L^J\rceil)$. For a threshold $z$ use the squarefree gate $P^-(m)\ge z$. Put $D=\sqrt N L^{-B}$ for any fixed $B>0$, and set

$$
 \begin{split}
 \mathcal L_z(I)&=\sum_{\substack{n\in I\\m\ {\rm squarefree},\,P^-(m)\ge z}}
                        \lambda(n) F_{0,D}(m),\\
 \mathcal H_z(I)&=\sum_{\substack{n\in I\\m\ {\rm squarefree},\,P^-(m)\ge z}}
            \lambda(n)\big(F_{0,D}(m)F_{1,D}(m)-F_{0,D}(m)\big).
 \end{split}                                                     \tag{1}
$$

By the [LCM coefficient identity](spectral-midpoint-lcm-complement-frontier.md), these are precisely the portions at LCM modulus $\le D$ and $>D$ of the cut mixed product. The full analogues replace $D$ by the divisor midpoint $\sqrt m$ on each partner. Below, $O(X\ell^{-A_0})$ exceptions means one exceptional set for all original cells of a modulus, for any fixed $A_0>0$.

**Fixed thresholds.** For any fixed $0<\beta<1/1000$, outside $O_{\beta,J,A_0}(X\ell^{-A_0})$ even moduli, both true parts satisfy

$$
 (\mathcal L_{N^\beta}(I),\mathcal H_{N^\beta}(I))
 =\frac{\Sigma(N)H}{L}
     \big(\varepsilon_\beta+o(1),\,1-\varepsilon_\beta+o(1)\big),
 \qquad \varepsilon_\beta=1-C_\beta.                             \tag{2}
$$

Here $0<\varepsilon_\beta<1$ is given by the explicit Dickman integral in the earlier proof. It is strictly increasing in $\beta$. Consequently, for fixed $0<\beta_1<\beta_2<1/1000$, the composite shell $N^{\beta_1}\le P^-(m)<N^{\beta_2}$ has main constants $\varepsilon_{\beta_1}-\varepsilon_{\beta_2}<0$ in the low block and $\varepsilon_{\beta_2}-\varepsilon_{\beta_1}>0$ in the high block. A fixed finite list of thresholds works on the same good set, by a finite union. These shell statements are not claims that either of the corresponding coefficients has a pointwise fixed sign.

**Moving threshold.** For all sufficiently large $N$, put $z_N=\exp(100L/\log L)$ (thus its exponent is $100/\log L$). Outside $O_{B,J,A_0}(X\ell^{-A_0})$ even moduli,

$$
 \mathcal L_{z_N}(I)\ll_{B,J,A_0}\frac{\Sigma(N)H}{L^{9/5}},
 \qquad
 \mathcal H_{z_N}(I)=\frac{\Sigma(N)H}{L}
               +O_{B,J,A_0}\!\left(\frac{\Sigma(N)H}{L^{9/5}}\right).
                                                                    \tag{3}
$$

The exponent $9/5$ is inessential. In particular (3) estimates separate signed blocks on a genuine growing family of factor counts, not merely their sum. The gate still excludes integers with a prime factor below $z_N$, even though $z_N=N^{o(1)}$.

## 1. Exact complementary model and a strict shell sign

Write $K_\beta(dt)=\mathbf1_{t\ge\beta}\,dt/t$, $\mathcal B_\beta=\exp_*(K_\beta)$ and $\mathcal M_\beta=\exp_*(-K_\beta)$, where all convolution series are locally finite in the convolution index. Write $f_{+,\beta}$ and $f_{-,\beta}$ for their densities away from zero; both have an atom of mass one at zero. In the notation of the Dickman proof,

$$
 A_-=\int_{[0,1/2)} f_{+,\beta}(1-s)\,\mathcal M_\beta(ds),
 \qquad
 A_+=\int_{[0,1/2)} f_{-,\beta}(1-s)\,\mathcal B_\beta(ds),
 \qquad A_-+A_+=0.
$$

The unrestricted parity sum of the exponent simplices with the weight
$\sum_{A}(-1)^{|A|}\mathbf1_{\sum_{i\in A}t_i<1/2}$ is exactly $A_-$, by expanding the two convolution measures and using the coefficient $1/(j!l!)$ for $j$ subset factors and $l$ remaining factors. This is the continuum coefficient for the full true low $F_0$ on rough squarefree partners. It includes the one-prime term, unlike the full high block. The Dickman result says $C_\beta=1+A_+$, so $A_-=\varepsilon_\beta$. There is no circular appeal here to an asymptotic for two primes: the constants come from the signed and unsigned convolution exponentials.

For the strict comparison, differentiate with respect to the lower support endpoint. On compact positive $\beta$ intervals, in the sense of convolution measures tested on a bounded support, the derivatives are

$$
 \partial_\beta\mathcal B_\beta
       =-\beta^{-1}\delta_\beta*\mathcal B_\beta,\qquad
 \partial_\beta\mathcal M_\beta
       =+\beta^{-1}\delta_\beta*\mathcal M_\beta .
$$

Indeed the cut difference in $K_\beta$ is minus the thin interval measure $dt/t$ adjoining $\beta$; take its difference quotient and differentiate the finite-on-support convolution series. Applying the two signs to $A_+$ gives

$$
 \varepsilon_\beta'
   =-\frac1\beta\int_{1/2-\beta}^{1/2}
         f_{-,\beta}(1-\beta-s)\,f_{+,\beta}(s)\,ds>0.            \tag{4}
$$

In detail, the $\mathcal B_\beta$ derivative shifts $s$ by $\beta$, hence has upper cut $1/2-\beta$, while the $f_{-,\beta}(1-s)$ derivative shifts only its argument. Their difference leaves exactly the displayed interval. To justify this calculation for the sharp cutoff, fix a compact interval of $\beta$ values in $(0,1/1000)$. Each convolution exponential and its cut differences have uniformly bounded densities away from the atom at zero on $[0,1]$. In the linear term from changing $\mathcal B_\beta$, the signed convolution difference quotient is integrated against the shifted density and the half cutoff; the limiting shifted measure has an atom at $\beta$, not at $1/2$. The density $f_{-,\beta}(t)$ is continuous on $[1/2-\beta,1]$ for fixed $\beta$, since there is no single-factor breakpoint there and every higher convolution density is continuous. In its own change, the linear term is convolution with the thin interval measure, and its density quotient converges uniformly on $[1/2,1]$ to $\beta^{-1} f_{-,\beta}(t-\beta)$. The higher interval-measure terms have total mass $O(h^2)$ for a cut increment $h$, and also $O(h^2)$ density on $[1/2,1]$: convolution against the bounded continuous part uses the mass bound; for the atom part the twofold interval convolution is supported below $1/2$, while terms of order at least three have density $O(h^{j-1})$ in order $j$. This verifies the derivative for either increment sign and the product rule. In (4), $f_{-,\beta}(t)=-\rho(t/\beta-1)/t<0$ throughout the integration range, and $f_{+,\beta}(s)\ge1/s>0$. The proposed derivative therefore has a strict sign. Subtracting (2) at the two actual sharp thresholds proves the shell statement; both the prime term and the gate change are treated by that literal subtraction.

## 2. Uniform transfer when the smallest exponent decreases

Here are the uniformity details for (2) and (3). On the dyad take a frozen threshold $z=X^b$, where either $b=\beta$ is fixed or $b=100/\log\ell$. For large $X$ we have $b<1/1000$ in either case. Take

$$
 K=\lfloor2/b\rfloor,\qquad
 \nu_X=\sum_{\substack{z\le p\le2X\\p\ {\rm prime}}}\frac1p\,
                       \delta_{\log p/\ell}.
$$

Every relevant partner has at most $K$ factors, and both full coefficients are bounded by $2^K$. In the moving case, $K\ll\log\ell$, $4^K\le\ell^{1/20}$ for large $X$, and

$$
 \nu_X(\mathbb R)\ll 1+\log(1/b),\qquad
 \sum_c \frac1c\le\prod_{z\le p\le2X}(1+1/p)\ll b^{-1}.
                                                                    \tag{5}
$$

Here $c$ ranges over all possible sorted prefixes of distinct primes, including the empty prefix. These are Mertens bounds and remain uniform for $b\ell\to\infty$. In the fixed case the corresponding bounds are constants depending on $\beta$.

Apply the same circle argument as in the Dickman proof, separately for the exact coefficient $F_0$ on rough squarefree $m$ or the exact full high coefficient on those $m$. Both coefficients are functions of $m,X$ only. If $m=cp$ with $p$ the unique largest prime and $c$ the sorted prefix, the signed short-divisor indicator is, up to the fixed sign selecting the high block,

$$
 \sum_{a\mid c}\mu(a)
      \big(\mathbf1_{a^2<cp}-\mathbf1_{a^2p<c}\big).
$$

Thus the sign function is constant on at most $O(2^K)$ intervals of $p$, with the original exact endpoints. For the low block all $k$ are allowed, including $c=1$ with coefficient one. For the high block only odd $k\ge3$ is included, with the negative sign. The moving gates $p\ge z$ and $p>P^+(c)$ merely add endpoints. When the summand is nonzero and $m\in[X/3,2X]$, one has $X/c\ge z/2$. For $q\le\ell^C$, this implies $q\le(\log(X/c))^{C+1}$ for any fixed $C$ and sufficiently large $X$. Every prime concerned is also above $q$. The unweighted prime form of [Siegel–Walfisz](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF) on $p$, summing reduced residues and using the bounded phase variation on each interval, supplies arbitrary fixed inverse-log accuracy. The loss from all signed intervals, their endpoints, and the reciprocal prefixes (5) is at most a fixed power of $\ell$; the latter log change uses $\log(X/c)\gg \ell/\log\ell$. The major density $a_X(x)$ is therefore exactly the same cofactor model as in that proof, using $1/(c\log(x/c))$ and the sign function above. Again multiplication by $c$ permutes residues and gives $\mu(q)/\varphi(q)$.

On $V=[X/3,2X]$, extending by zero at the ends, the density has supremum and total variation at most $O(4^K/(b^2\ell))$, since for each $c$ there are $O(2^K)$ sign intervals, its magnitude is at most $2^K/(cb\ell)$, and (5) bounds the reciprocal prefixes. This is sufficient to restore the real-line singular integral with error $O(X4^K/(Qb^2\ell))$ before its singular-series factor, for major arc width $2Q/X$, $Q=\ell^C$. The true coefficient polynomial has squared torus norm $O(X4^K)$. The [Vaughan bound](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=77) for the first genuine prime factor on the minor arcs is $O_E(X\ell^{-E})$ for arbitrary fixed $E$ by enlarging $C$. Accordingly the squared Bessel budget is $O_E(X^3 4^K\ell^{-2E})$. Take minor error $X\ell^{-J-2}$ and use the same endpoint cover of $O_J(\ell^{2J+4})$ frozen real cells at mesh $X\ell^{-J-4}$. The new loss $4^K$ is absorbed by $E$, and the error from moving cell endpoints is bounded trivially by $O((X\ell^{-J-4}+1)L2^K)=O(\Sigma H/L^2)$ in the moving case and by the corresponding fixed-$\beta$ bound. The absolute Ramanujan-series tail estimate and Markov argument are unchanged, and the major errors can be made $O(X\ell^{-J-3})$. Thus on a common set outside $O_{J,A_0}(X\ell^{-A_0})$ exceptions (with fixed-$\beta$ constants allowed when applicable) the exact full arithmetic sums are the continuum integrals on the actual cells times $\Sigma(N)$, with errors $O(\Sigma(N)H/L^2)$.

## 3. A fine exponent grid controls all moving polytopes

For fixed $\beta$, the weak-convergence proof in the Dickman note applies to both signs; the low block has constant $A_-$. For the moving case, the following quantitative version avoids any uniformity inference from fixed-dimensional weak convergence.

Put $\omega_X=\log(2X)/\ell$, and compare $\nu_X$ to $\nu(dt)=\mathbf1_{b\le t\le\omega_X}\,dt/t$. By the prime number theorem with its usual zero-free-region error, equivalently the modulus-one form of the prime theorem used above followed by partial summation, on any real interval of exponents contained in $[b,\omega_X]$ their mass difference is $O(\exp(-c\sqrt{b\ell}))$ for an absolute $c>0$ (endpoint atoms cost at most $1/z$). Partition the exponent interval into bins of mesh at most

$$
 \Delta=\exp(-(\log\ell)^2)
$$

with at most $O(1/\Delta)$ bins, and replace each bin's mass by an atom at a representative in it. The total variation discrepancy between the two binned measures is $O(\Delta^{-1}\exp(-c\sqrt{b\ell}))$. For their $j$-fold tensor products it is at most $j$ times this discrepancy times the maximum of the two total masses to the power $j-1$, by telescoping the product. Those masses are $O(1+\log(1/b))$.

For any $x\in V$ put $\xi=\log x/\ell$ and $t_k=\xi-\sum_{i<k}t_i$. In both cofactor models the ordering, support $t_k\ge b$, and the midpoint comparisons are finitely many affine inequalities in the first $k-1$ exponents: the threshold for a subset is $\xi/2$. Apart from the empty and full subsets, which need no cuts, each hyperplane has a nonzero coefficient of magnitude at least one, and all coefficients are bounded absolutely. There are $O(k+2^k)$ planes. A product of bins can change any comparison only if it touches a strip of width $O(K\Delta)$ in the defining linear functional. The continuous product mass of one strip is at most

$$
 O(K\Delta/b)\big(O(1+\log(1/b))\big)^{k-2}\quad (k\ge2)
$$

by integrating first a coordinate with coefficient bounded below. The mass of bins meeting the strip satisfies the same bound with a larger width, and their discrete mass is at most this bound plus the binned-product discrepancy. The magnitude of the integrated sign divided by $t_k$ is at most $2^K/b$ on the good support. On bins meeting no strips this quotient varies by at most $O(2^K K\Delta/b^2)$, from the reciprocal $t_k$ alone. These bounds are uniform in $\xi$, including when a small polytope disappears. The one-prime term $k=1$ is immediate without a grid.

Summing these errors over $k\le K$ gives $o(\ell^{-A})$ for every fixed $A$: in the strip and within-bin estimates, $\Delta$ dominates $\exp(O(K\log(2+\log(1/b))+K+\log(1/b)))=\exp(o((\log\ell)^2))$, and in the bin-mass discrepancy the term $\sqrt{b\ell}$ dominates $(\log\ell)^2$. Repeated prime coordinates cause no issue, since their diagonals are among the ordering strips. The continuous polytope has exact total logarithmic mass $\xi$, not a rounded value of one. Change variables $t_i=\xi u_i$ to scale to the unit simplex. The factor from $k$ reciprocal weights and $k-1$ integration coordinates is $\xi^{-1}$, and the roughness lower bound becomes $b/\xi$. As in the fixed proof, symmetry gives $1/k!$ for the ordered region. Hence, uniformly in $V$,

$$
 \ell a_{X,\mathrm{low}}(x)
      =\xi^{-1}\varepsilon_{b/\xi}+o(\ell^{-A}),\qquad
 \ell a_{X,\mathrm{high}}(x)
      =\xi^{-1}(1-\varepsilon_{b/\xi})+o(\ell^{-A}).             \tag{6}
$$

All possible continuous factor counts occur among $k\le K$ for large $X$. Because $b=100/\log\ell$ and $\xi=1+O(1/\ell)$, the factorial bound in the Dickman formula gives $\varepsilon_{b/\xi}=o(\ell^{-A})$ for every fixed $A$: its factorial index is bounded below by a positive constant times $\log\ell$, and the factorial logarithm grows faster than any fixed multiple of $\log\ell$. Also $\xi^{-1}=1+O(1/\ell)$. Equations (5)–(6) give the full midpoint estimates with the frozen rough cutoff and errors $O(\Sigma H/L^2)$ in the moving case.

## 4. Return to true moving roughness and the cut LCM blocks

For the moving threshold, the function $u\mapsto100u/\log u$ is increasing for $u>e$ and has derivative $100(\log u-1)/(\log u)^2\to0$. Thus on the dyad $X^b\le z_N\le2X^b$ for large $X$. The same factor-two containment holds for a fixed $\beta$ and $N^\beta$. Changing the threshold can only affect squarefree partners having a prime factor $r\in[z,2z]$ and rough cofactor at $z=X^b$. Use the [two-form rough-cofactor sieve](spectral-midpoint-lcm-complement-frontier.md). Its bound is uniform here: in each needed modulus range $r\le\sqrt N$ the cofactor interval has length $U\gg X^{1/2}/\ell^J$, so $Y=U^{1/100}>z$ eventually, and $\log U\asymp L$. The Euler product is $V_z\asymp\Sigma(N)/(bL)$, with uniform constants; discarded primes dividing $N$ above $z$ have total reciprocal at most $O(L/(z\log z))=o(1)$. The accumulated main bound for changing the gate is $O(\Sigma H/(b^2L^2))$, since $\sum_{z\le r\le2z,\ r\ {\rm prime}}1/\varphi(r)\ll 1/(bL)$. The power error is $O(X^{(1+b)/2}L^2)$ by summing the CRT errors. Multiply by $2^K$ for the sign weights.

For truncating the midpoint at $D$, the same sieve applied to rough squarefree $d\in(D,\sqrt N]$ gives raw critical divisor incidence

$$
 E_I\ll_B\frac{\Sigma(N)H(1+\log L)}{b^2L^2}+X^{3/4}L^2.        \tag{7}
$$

Indeed their rough reciprocal sum is $O_B((1+\log L)/(bL))$ by dyadic intervals and the dimension-one upper sieve up to $z^{1/3}$, as in the [uniform rough reciprocal proof](spectral-midpoint-lcm-complement-frontier.md). Here $r/\varphi(r)\le2$ for all relevant rough moduli, since they have at most $K$ primes all at least $z$, and $K/z=o(1)$. Thus neither this bound nor the two-form bound introduces constants growing with the number of factors. All cutoff errors are on the true prime sequence: a lost short divisor lies in the band of (7), with weight of modulus at most one, while a product difference uses at most another factor $O(2^K)$. This proves the signed block errors $O(2^K E_I)$.

In the moving case, $b^{-2}\ll(\log L)^2$ and $2^K\le L^{1/40}$ for large $X$, so both (7) times this factor and the roughness replacement error are $O(\Sigma H/L^{9/5})$. In the fixed case both are $o(\Sigma H/L)$. Together with the true circle transfer and the signed continuum constants, these estimates prove (2) and (3).

The aggregate of the two cut blocks is the earlier approximation to the true prime-partner weight, but the separate signed conclusions are stronger than that identity: the falling low term and the rising net high term, as well as the negative and positive shell constants, are determined here independently of any binary-prime count. Nothing in this argument estimates the full high term on the exceptional set or uniformly controls the less-rough signed composites that lie outside the stated cuts.
