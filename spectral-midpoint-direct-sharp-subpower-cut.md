# A direct sharp-cut midpoint model at a much smaller least prime

**Scope.** This does not restore the midpoint or use the [previous Lipschitz restoration bound](spectral-midpoint-least-prime-lipschitz-shell.md) to evaluate the new rough range. Instead it models the **actual sharp mixed product** at its own cut via four convolution measures and proves its continuum stability. This gives unconditional signed cancellation on a new shell of genuine less-rough partners, in every original central cell for almost all even moduli. It does not control a prescribed modulus, factors below the new threshold, or Hypothesis S.

Let even $N\in[X,2X]$, $L=\log N$, $\ell=\log X$, $m=N-n$, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Let $\Sigma(N)$ be the usual binary singular series. Fix $J\ge1$, $B>0$, and use the original half-open central cells $I\subset(N/2,9N/16]$ of length $H=N/(16\lceil L^J\rceil)$ and the original sharp $D_N=\sqrt N L^{-B}$. As before, define

$$
 F_{0,D}(m)=\sum_{\substack{d\mid m\\d\le D}}\mu(d),
 \qquad
 F_{1,D}(m)=\sum_{\substack{d\mid m\\d\le D}}
               \mu(d)\left(1-\frac{2\log d}{\log m}\right),
 \qquad
 G_D=F_{0,D}F_{1,D}-F_{0,D}.
$$

These are the [original LCM cut](spectral-midpoint-lcm-complement-frontier.md): $F_{0,D}$ includes moduli $\le D$, and $G_D$ moduli $>D$. For either, retain initially the squarefree gate on $m$.

Fix $C>2$ and put $z_C(N)=\exp((\log L)^C)$. Given any fixed $A_0>0$, outside one set of $O_{B,J,C,A_0}(X\ell^{-A_0})$ even moduli, in **every** cell of each remaining modulus,

$$
 \begin{split}
 \sum_{\substack{n\in I\\m\ {\rm squarefree},\,P^-(m)\ge z_C(N)}}
                  \lambda(n)F_{0,D_N}(m)
       &= O\!\left(\frac{\Sigma(N)H}{L^2}\right),\\
 \sum_{\substack{n\in I\\m\ {\rm squarefree},\,P^-(m)\ge z_C(N)}}
                  \lambda(n)G_{D_N}(m)
       &=\frac{\Sigma(N)H}{L}
          +O\!\left(\frac{\Sigma(N)H}{L}(\log L)^{1-C}\right).
 \end{split}                                                    \tag{1}
$$

Constants may depend on all fixed parameters. In particular, in the genuine intervening shell $z_C(N)\le P^-(m)<\exp(L^{2/3}(\log L)^\kappa)$ with any fixed $\kappa\ge C/3$, the cut high and low sums are each $O((\Sigma(N)H/L)(\log L)^{1-C})$ by subtracting the two verified signed results. The same shell statement holds without the squarefree gate, by the negligible rough squareful contribution shown below. This is a signed statement, not a bound on its absolute mass.

## 1. Exact cut continuum and its stability

For $0<b<1/10$, let $K_b(dt)=\mathbf1_{t\ge b}\,dt/t$ on the nonnegative line, and use the [Dickman convolution exponentials](spectral-midpoint-odd-aggregate-dickman.md)

$$
 \mathcal B_b=\exp_*(K_b)=\delta_0+f_+(t)\,dt,\qquad
 \mathcal M_b=\exp_*(-K_b)=\delta_0+f_-(t)\,dt.
$$

The sums defining the exponentials are finite in convolution index on any bounded support. As proved there, $f_-(t)=0$ for $0<t<b$ and equals $-\rho(t/b-1)/t$ for $t>b$, with $\rho$ positive and $\rho(u)\le1/\lfloor u\rfloor!$. In particular

$$
 \int |f_-|\le1,\qquad \int t|f_-(t)|\,dt\ll b,\qquad
 \sup t|f_-(t)|\le1,\qquad \sup |f_-|\le1/b.
$$

The first bound follows also from the cumulative $\mathcal M_b([0,t])=\rho(t/b)$ and its limit zero. We use $\sup f_+\le 1/b$ as well: scaling reduces it to $b=1$, where the convolution Euler identity gives $t f_+(t)=\mathcal B_1([0,t-1])$ for $t>1$. Start on $1<t<2$ with $f_+(t)=1/t$ and induct in unit intervals, since $1+\int_1^{t-1}f_+(u)du\le1+(t-2)_+\le t$. Statements about densities use their bounded one-sided representatives at jumps.

For a normalized simplex with total exponent one, write the cutoff exponent as $\nu=1/2-\eta$, $0<\eta<1/10$. The signed low model is

$$
 \mathcal L_b(\nu)=\int_{[0,\nu]}\mathcal M_b(ds)f_+(1-s).
$$

The continuum model of the product $F_{0,D}F_{1,D}$, not yet subtracting its low term, is

$$
 \mathcal P_b(\nu)=
 \int_{\substack{x,y,z\ge0\\x+y\le\nu,\ x+z\le\nu}}
         \mathcal B_b(dx)\mathcal M_b(dy)\mathcal M_b(dz)
         \bigl(1-2(x+z)\bigr) f_+(1-x-y-z).                    \tag{2}
$$

Indeed each prime label belongs to both selected divisor sets, only the first, only the second, or neither. These are respectively the variables $x,y,z,w$ of the positive, negative, negative, positive convolution exponentials; the product of Möbius coefficients gives exactly these signs, and the second divisor carries weight $1-2(x+z)$. Multinomial coefficients on the symmetric simplex give precisely the reciprocal factorials of the four exponential series. The fourth variable is $w=1-x-y-z>0$ wherever there is a contribution, so its zero atom is absent. The same holds at $\nu=1/2$ with strict midpoint conditions: $x+y<1/2$ and $x+z<1/2$ imply $x+y+z<1$. Changing a nonzero boundary from strict to weak is immaterial in the resulting positive-coordinate simplex integrals; the variable-sum atoms occur only at zero.

At the full strict midpoint the product equals the prime indicator on the exponent simplex except on the finitely many midpoint hyperplanes in each dimension: pairing complementary subsets is the [squarefree midpoint identity](spectral-midpoint-parity-signed-transport.md), and holds for arbitrary positive exponent labels. The only surviving term is the one-prime weight, with density $K_b(1)=1$. Hence $\mathcal P_b(1/2)=1$. The low model at $1/2$ is the earlier $\varepsilon_b$ from the [complementary-block evaluation](spectral-midpoint-complementary-blocks-moving-roughness.md); both that constant and the strip change from $\nu$ to $1/2$ are smaller than every power of $b$ as $b\downarrow0$. For the strip change, the density $f_-(s)$ on $s\ge2/5$ has the factorial decay above while $f_+(1-s)\le1/b$.

The main new signed stability assertion is

$$
       |\mathcal P_b(\nu)-1|\ll \eta/b+\eta^2/b^2.             \tag{3}
$$

Here is a direct strip proof, which avoids differentiating discontinuous sharp cuts. In the difference of domains in (2), use the union of the two strips $x+z\in[\nu,1/2]$ and $x+y\in[\nu,1/2]$ inside the full domain, and take absolute measures. Away from zero the density of $\mathcal B_b*|\mathcal M_b|$ is $O(1/b)$: expand its two atoms and densities, using $\|f_+\|_\infty,\|f_-\|_\infty\le1/b$ and $\int|f_-|\le1$. The density of $\mathcal B_b*(t|\mathcal M_b|)$ is $O(1)$ by the same expansion, using $\sup t|f_-|\le1$ and $\int t|f_-|\ll b$. Neither convolution has an atom in the indicated strips. In the first strip the log weight in (2) is at most $2\eta$, so using $f_+(w)\le1/b$ and $|\mathcal M_b|([0,\infty))\le2$ gives $O(\eta^2/b^2)$. In the second strip use $0\le1-2(x+z)\le1-2x\le2\eta+2y$. Its integral is $O(\eta^2/b^2+\eta/b)$ by the two density bounds. This proves (3). The two model blocks are therefore separately negligible low and high $1+O(\eta/b+\eta^2/b^2)$, even when an absolute arithmetic endpoint restoration is too costly.

## 2. Freeze moving arithmetic cutoffs and dispose of very smooth partners

Use a real target mesh of maximal length $\delta=X\ell^{-J-12}$, also cutting at changes of $\lceil(\log N)^J\rceil$. On each piece fix $N_0$ in its closure and the piece's actual cell count, and freeze $D=D_{N_0}$, $z=z_C(N_0)$. There are $O_J(\ell^{2J+12})$ choices of fixed first interval $U$ over all cells of all pieces. Take $V=[X/3,2X]$ for the second coordinate. Put $t_0=\log z$, $b_0=t_0/\ell$, so $t_0\asymp_C(\log\ell)^C$ and $b_0^{-1}\ll\ell$. Set $y=\exp(\ell/(\log\ell)^2)$ and initially keep only $m$ with largest prime at least $y$. All these frozen coefficients are functions of $m$ and the piece alone, not of the target within it.

All these changes can be bounded on the true sequence in absolute value. Here are exact budgets:
- On any interval of length $d_0$ in $[X/3,2X]$, $\sum\tau(m)^2\le\sum d_4(m)\ll d_0\ell^3+X^{3/4}\ell^2$. In a fourfold factorization choose one largest factor, so the product of the other three is $\ll X^{3/4}$, then count the last variable by length divided by that product plus one. Thus moving the cell endpoints costs $O(\delta\ell^4+X^{3/4}\ell^3)$ with $\lambda\le L$ and both coefficients bounded by $O(\tau(m)^2)$.
- The interval of divisors changed by moving $D$ has length $O(D\delta/X)$ at scale $D\asymp\sqrt X\ell^{-B}$. The absolute difference of the two high coefficients is at most $O(\tau(m))$ times the number of its divisors in that interval, using product differences and $D<\sqrt m$ throughout $V$ for large $X$. The low coefficient satisfies the same looser bound. Sum over all $m\le 2X$ by writing $m=da$ and using $\tau(da)\le\tau(d)\tau(a)$. Since $\sum_{a\le2X/d}\tau(a)\ll X\ell/d$ and the divisor hyperbola bounds $\sum_{d\in J_0}\tau(d)\ll |J_0|\ell+\sqrt D$ at scale $D$, the resulting weighted cost is $O(\delta\ell^3+X^{3/4}\ell^{B/2+2})$.
- Moving $z$ changes its value by relative size $O_C(\delta/X)$, by differentiation of $\log z_C(N)=(\log\log N)^C$. A changed partner has a prime divisor $r$ in that short interval. The sum of $1/r$ there is $O_C(\delta/X+1/z)$ even if all integers are counted. With $\tau(ra)^2\le4\tau(a)^2$, summing over all $a\le2X/r$ and multiplying by $\lambda\le L$ bounds the error by $O_C(X\ell^4(\delta/X+1/z))$.
- The number of $y$-smooth integers up to $2X$ is $O_A(X\ell^{-A})$ for every fixed $A$. Indeed Rankin with $\sigma=1-1/\log y$ bounds it by $(2X)^\sigma\prod_{p\le y}(1-p^{-\sigma})^{-1}$; the product is at most a fixed power of $\ell$, since $p^{1/\log y}\le e$ and the logarithm of the product is $O(1+\sum_{p\le y}1/p)$. The prefactor divided by $X$ is $O(\exp(-(\log\ell)^2))$. Cauchy--Schwarz with $\sum_{m\le2X}\tau(m)^4\ll X\ell^{15}$ bounds the true smooth contribution to either weighted test by $O_A(X\ell^{-A})$ after choosing the saving larger.

All displayed costs are $O(H/L^2)$ (in fact smaller), uniformly in $N,I$. The inequalities $\tau^2\le d_4$, $\tau^4\le d_{16}$ and their ordinary moment upper bounds follow as in the [complete cut low estimate](spectral-midpoint-complete-low-squarefree-bv.md).

## 3. Circle transfer of the actual cut and one-coordinate model comparison

For a fixed piece use either exact cut coefficient, on squarefree $z$-rough integers $m\in V$ with largest prime $\ge y$, and zero off this support. Denote its polynomial by $T(\theta)$. Its squared torus norm is $O(X\ell^{15})$ by the fourth divisor moment. Write each such $m=cp$ with unique largest prime $p$ and squarefree prefix $c$. For fixed $c$, its real cofactor weight on $p$ is the same sum over divisors $a\mid c$ and $ap$, with exact gates $a\le D$ or $p\le D/a$. For the centered weight, the ratio $\log a/\log(cp)$ or $(\log a+\log p)/\log(cp)$ is monotone in $p$ on each interval; the weights take values in $[0,1]$ on their cutoff support. Thus the low and high coefficient functions in $p$, including the largest-prime gate $p>P^+(c)$ and $p\ge y$, have supremum and total variation $O(\tau(c)^2)$ by adding the individual terms and applying the product rule for variation. The possible empty prefix is interpreted in the obvious way as the one-prime term.

For any fixed $j$, the prefix product bound is $\sum_c\tau(c)^j/c\ll_j b_0^{-2^j}$ by Mertens and squarefreeness. The real major density $a(x)$ for the piece is the exact sum of these signed cofactor weights at $p=x/c$, times $1/(c\log(x/c))$. Its supremum and total variation, extended by zero off $V$, are $O((b_0^5\ell)^{-1})$, a fixed power of $\ell$. On polylogarithmic major arcs $a_0/q+\eta_0$, $q\le Q=\ell^{C_0}$, $|\eta_0|\le2Q/X$, use the [Siegel--Walfisz theorem](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF) on the final prime. Here $\log(X/c)\ge \ell/(\log\ell)^2-O(1)$ on contributing prefixes and all prime factors of both $c,p$ exceed $q$, since $z=\exp((\log L)^C(1+o(1)))$ and $C>2$. For each reduced residue, partially sum the signed variation weight times the additive phase; these lose only logarithmic powers by the prefix bounds. The residue sum after multiplication by $c$ is $\mu(q)$. The resultant major polynomial is

$$
       \frac{\mu(q)}{\varphi(q)}\int_V a(x)e(\eta_0x)\,dx
                  +O_T(X\ell^{-T})
$$

for arbitrarily large fixed $T$. The genuine first-prime polynomial over $U$ has the same factor with density $\mathbf1_U$. On the minor arcs the [Vaughan estimate](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=77) bounds this first polynomial by $O_E(X\ell^{-E})$ for arbitrary $E$ as $C_0$ increases. Bessel for the minor coefficient in the integer target, with the displayed $\|T\|_2^2$, bounds its squared sum by $O_E(X^3\ell^{15-2E})$. Threshold $X\ell^{-J-2}$ and union over the fixed $O_J(\ell^{2J+12})$ intervals and both coefficients cost $O(X\ell^{-A_0})$ exceptions by taking $E$ large.

The real convolution and summation of the main term then proceed as in the [original Dickman transfer](spectral-midpoint-odd-aggregate-dickman.md). In detail the product of the two Fourier transforms has tail $O(X/(Qb_0^5\ell))$ by the density variation and the first interval's transform decay. The sum over $N\le2X$ of absolute Ramanujan tails beyond $Q$ is $O(XQ^{-1/2})$ by the squarefree divisor formula. Use Markov at any sufficiently small inverse-log threshold and take $C_0$ large. Thus on the common good moduli the actual correlation is $\Sigma(N)\int_U a(N-u)du+O(\Sigma(N)H/L^2)$. Its continuum endpoint change is at most $O(\Sigma(N)\delta/(b_0^5\ell))$, smaller than the error. The first interval and $N-U$ are inside $V$ on the central cells, as in the prior cover.

The new transfer to the limiting cut model does **not** use a separate grid in every factor coordinate. Let $\xi=\log x/\ell=1+O(1/\ell)$ and write $s_k=\xi-\sum_{i<k}s_i$ for the last prime exponent when $s_i=\log p_i/\ell$. Compare the reciprocal-prime measure $\nu_X=\sum_{z\le p\le2X}p^{-1}\delta_{\log p/\ell}$ with $\nu=1_{[b_0,\log(2X)/\ell]}ds/s$. Their masses are $O(1+\log(1/b_0))$, and their discrepancy on **every** interval is $O(\exp(-c\sqrt{t_0}))$ by the [prime-number-theorem zero-free-region error](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287) and partial summation. Endpoint atoms cost at most $1/z$.

Use ordered prefix tuples of length $k-1$ with weight $1/(k-1)!$; define the labeled divisor weight even on repeated tuples for purposes of this comparison, removing repeats afterward. For fixed other coordinates the gates $s_k\ge \log y/\ell$, $s_k\ge b_0$, and $s_k>\max_{i<k}s_i$ cut out an interval in the varying coordinate. Every divisor's cut is one affine inequality in that coordinate; every second-divisor log weight is affine there with bounded variation on the support. Thus the normalized integrand for $\ell a(x)$ has one-coordinate supremum plus variation $O(4^k/b_0)$: use the variation product rule for the two divisor sums and monotonicity of $1/s_k$ on the support. The integrand is symmetric in the $k-1$ prefix coordinates. Replace the measures one coordinate at a time using the Stieltjes bound against interval discrepancy, holding the others fixed. If $M_0$ is the larger total measure mass, the error in degree $k\ge2$ before the factorial division is

$$
 O\!\left((k-1)4^k b_0^{-1}M_0^{k-2}\exp(-c\sqrt{t_0})\right).
$$

Sum after division by $(k-1)!$: the total is at most $\exp(-c\sqrt{t_0})$ times a fixed power of $b_0^{-1}$. This is smaller than every inverse-log power because $t_0\asymp(\log\ell)^C$ with $C>2$. Repeated prime indices in the discrete tuples cost equally little: choose one repeated pair, bound its squared reciprocal mass by $\sum_{p\ge z}p^{-2}\ll1/z$, use $M_0^{k-3}$ for the other entries, and sum $O(k^2 4^k/b_0)$ after the factorial division. This costs at most $z^{-1}$ times a fixed power of $b_0^{-1}$. The $k=1$ term is direct. These bounds remain uniform in $x$ and in the frozen $D,z$.

In the resulting continuum remove the temporary largest-prime lower bound with a negligible error. If all $s_i\le \gamma=(\log\ell)^{-2}$, the prefix sum is at least $\xi-\gamma$. Use the positive Rankin bound $e^{-(\xi-\gamma)/\gamma}\prod_{i<k}e^{s_i/\gamma}$, the integrand amplitude $O(4^k/b_0)$, and integrate each prefix on $[b_0,\gamma]$. The integral of $e^{s/\gamma}ds/s$ is $O(1+\log(1/b_0))$. Factorial summation shows that the excluded continuous density costs at most $\exp(-c/\gamma)$ times a fixed power of $b_0^{-1}$, hence is negligible. No one-prime term meets that small-largest condition.

Finally scale the exponent simplex by $\xi$, giving overall factor $\xi^{-1}$ in $\ell a(x)$, rough parameter $b=t_0/\log x$ and normalized cut $\nu=\log D/\log x$. The rule that the last coordinate is the largest, together with the prefix factorial, gives the full symmetric simplex factor $1/k!$ because permutations preserve its coordinate volume and its signed integrand. For each frozen piece, uniformly on $V$, $0<\eta=1/2-\nu\ll_B(\log L)/L$ for large $X$, since $\log D=(1/2)\log N_0-B\log\log N_0$ and $\log x-\log N_0=O(1)$. Therefore $\eta/b\ll_{B,C}(\log L)^{1-C}$. The exact continuum results of Section 1 give low $a(x)=o(\ell^{-T})$ for every fixed $T$, and high

$$
       a(x)=\frac{1+O((\log L)^{1-C})}{\log x}.
$$

Since $\log(N-u)=L+O(1)$ on the actual cell, integration, the genuine circle transfer, and the true parameter restoration of Section 2 prove (1). The proof uses the original discontinuous $d\le D_N$ cut throughout.

Finally among partners with least prime at least $z_C(N)$, there are $O(N/z_C(N))$ nonsquarefree integers, since some $p^2$ with $p\ge z_C(N)$ must divide each. Their raw weighted mass with either cut coefficient is $O(NL^{17/2}/\sqrt{z_C(N)})$ by the fourth divisor moment and Cauchy--Schwarz; this is smaller than any inverse-log target. This justifies the claimed shell extension without the squarefree gate, and gives no corresponding deletion below $z_C(N)$.
