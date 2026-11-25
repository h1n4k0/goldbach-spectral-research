# The second aligned color has an exact two-frequency formula

**Scope.** This note treats the other *genuine completed* finite cap of the [aligned two-pole correction](r93-spectral-completed-colored-caps.md). The formula keeps the actual two moving limits and the same denominator-margin error. It also proves that the nonstationary kernel of these cuts has positive and negative directions, even when its stationary autocorrelation has nonnegative spectrum. There is no estimate of the cap amplitude or of its sign, no new assertion on the finite-denominator correction outside the original margin, and no conclusion about an unaligned target or Hypothesis S.

Use the exact aligned notation $r\mid N$, $G=\log Y$, $Y\le N\le2Y$ even, $Q_0=\exp(16\sqrt G/\log G)$, and the primitive real Page character $\chi$ with its simple real zero $.99\le\beta<1$ for sufficiently large $G$. When the exceptional character is absent the original correction vanishes. Write $U=\log(H_0/D)$ and $T=T_x=\log(x/D^2)>0$, with the actual physical $x$ and the two original scales $D,H_0$. All local coefficients, $R_j$, $\mathcal N_\chi$, $\Sigma(N)$, and $C_\chi$ are precisely those of the completed aligned formula. In particular $\alpha(1)=1$, and $\alpha$ is squarefree and vanishes if a prime of $N$ divides its argument. The normalization $\mathcal N_\chi$ is real and nonzero, not presumed positive.

Define the shifted profiles $A_j(v)=R_j(v-\log j)$ and the real symmetric kernel

$$
 \mathcal K_\chi(v,w)=\mathcal N_\chi
 \sum_{j\ {\rm squarefree}}\mu(j)\alpha(j)^2A_j(v)A_j(w).
 \tag{1}
$$

It has the literal pointwise representative

$$
 \mathcal K_\chi(v,w)=\mathcal N_\chi
    \sum_{\substack{a\le e^v,\ b\le e^w\\(a,b)=1}}\alpha(a)\alpha(b),
 \tag{2}
$$

zero when either variable is negative. Use \(\widehat f(\xi)=\int f(v)e^{-i\xi v}\,dv$ and the corresponding product convention for $\widehat{\mathcal K}_\chi$. Put

$$
 G_\chi(\xi)=\frac{L(\beta+i\xi,\chi)}{i\xi L'(\beta,\chi)},
 \qquad G_\chi(0)=1,\qquad I_U(\xi)=\int_0^U e^{i\xi v}\,dv .
$$

For $p\nmid r$ use $c_p=\chi(p)p^{-\beta}$, $\alpha_p=\alpha(p)$ and set $z=p^{-i\xi},w=p^{-i\eta}$ in the local factor

$$
 \mathscr B_p(z,w)=
   \frac{(1-c_p z)(1-c_p w)}{(1-c_p)^2}
    \frac{1+\alpha_p(z+w)}{1+2\alpha_p}.
 \tag{3}
$$

All displayed normalization denominators are nonzero, including at the exceptional small primes.

**Theorem.** For all real $\xi,\eta$,

$$
 \widehat{\mathcal K}_\chi(\xi,\eta)
  =\Sigma(N)G_\chi(\xi)G_\chi(\eta)
     \prod_{p\nmid r}\mathscr B_p(p^{-i\xi},p^{-i\eta}).
 \tag{4}
$$

Outside the finite $N$ factors and the fixed primes $3,5$, the product converges absolutely and uniformly for real $(\xi,\eta)$. Its restriction to $\eta=-\xi$ is the [first-color Fourier signature](r94-spectral-aligned-colored-fourier-signature.md) $\widehat C_\chi(\xi)$, with the same normalization.

The full second color $B_1(x)$ of the genuine completed formula has the representation

$$
 \begin{split}
 B_1(x)
   &=T\int_U^\infty\mathcal K_\chi(v,v)\,dv
             +\int_{[0,U]^2}\mathcal K_\chi(v,w)\,dv\,dw\\
   &=\frac{T}{2\pi}\int_{\mathbb R}\widehat C_\chi(\xi)\,d\xi
    +\frac1{(2\pi)^2}\iint_{\mathbb R^2}
       \widehat{\mathcal K}_\chi(\xi,\eta)
          \big[I_U(\xi)I_U(\eta)-T I_U(\xi+\eta)\big]\,d\xi\,d\eta .
 \end{split}
 \tag{5}
$$

All integrals in (5) are absolutely convergent. At the actual physical $x$, insertion into the correction uses the same physical prefactor, parity half-sum and original approximation error of the completed formula. In particular the cut $U$ has not been replaced by a total moment.

Finally the self-adjoint integral operator of $\mathcal K_\chi$ on $L^2(\mathbb R)$ is trace class, with infinitely many positive and infinitely many negative eigenvalues. More quantitatively, let $p_1,\dots,p_s$ be any distinct primes not dividing $N$, with $s\ge1$. If their product is strictly less than $e^U$, its compression to $L^2([0,U])$ has at least $2^{s-1}$ positive and at least $2^{s-1}$ negative eigenvalues. This is a property of the exact clipped two-variable kernel, not either sign of the scalar in (5).

## 1. Keep the common divisor inside both size cuts

The absolute signed Euler-moment estimate (12) of the completed formula gives

$$
 \sum_j|\mu(j)|\alpha(j)^2
       \big(\|A_j\|_1^2+\|A_j\|_2^2\big)<\infty .
 \tag{6}
$$

A shift by $\log j$ preserves both norms. In particular (1) is absolutely convergent as an $L^1(\mathbb R^2)$ sum, and its explicitly given diagonal is absolutely convergent as an $L^1(\mathbb R)$ sum. For finite $v,w$ only $j\le\min(e^v,e^w)$ contribute. Each surviving $A_j(v)$ is the sum of $\alpha(a')$ for $a'\le e^v/j$ and $(a',j)=1$. Multiplicativity and squarefree support give
$\alpha(j)A_j(v)=\sum_{a\le e^v,\ j\mid a}\alpha(a)$
whenever $j$ contributes in (1); the same identity is zero on either side when $j$ is squarefree with $\alpha(j)=0$. Expanding the finite sums and using $\sum_{j\mid(a,b)}\mu(j)=\mathbf1_{(a,b)=1}$ proves (2). This uses the true common-divisor restriction and holds at every genuinely weak endpoint.

From (1) and (6), literal finite-cut integration gives

$$
 \begin{split}
 \int_{\mathbb R}\mathcal K_\chi(v,v)\,dv&=C_\chi(0),\\
 \int_0^U\mathcal K_\chi(v,v)\,dv&=Q_\chi(U),\\
 \int_{[0,U]^2}\mathcal K_\chi(v,w)\,dv\,dw&=J_\chi(U).
 \end{split}
 \tag{7}
$$

For example, for $j\le e^U$ the last limit for the original $R_j$ is $U-\log j$ on each leg; above $e^U$ both integrals vanish. Thus there is no replacement of the one-sided upper limit by zero or infinity before summing $j$. These are exactly the two distinct finite moments of the completed formula. Its $B_1(x)=T_x(C_\chi(0)-Q_\chi(U))+J_\chi(U)$ becomes the first line of (5).

## 2. Exact local shift and absolute cap tests

The shift in $A_j$ multiplies $\widehat R_j(\xi)$ by $j^{-i\xi}$. The primitive identity (5) of the first-color note gives $\widehat R_j(\xi)=L'(\beta,\chi)G_\chi(\xi)H_j(i\xi)$, with $H_j$ as in the completed formula. Its value at zero uses the simple zero and the original signed primitive, not a mass-one approximation. Applying (6) permits transforming the $j$ sum in (1) term by term. At $p\nmid r$, for $z=p^{-i\xi}$, $w=p^{-i\eta}$, the two choices of $p$ in $j$ give

$$
 (1-c_p z)(1-c_p w)
       \big((1+\alpha_p z)(1+\alpha_p w)-\alpha_p^2zw\big)
  =(1-c_p z)(1-c_p w)(1+\alpha_p(z+w)).
 \tag{8}
$$

The shift contributes the full $zw$ in the subtracted term. Without this shift the exact cut $U$, and the local cancellation in (8), would both be lost. There is no division by an uncombined factor $1+\alpha_p$.

To justify the Euler passage, first restrict $j$'s occupied primes to a finite set, retaining all $H_j$ factors. The tail of the unoccupied Euler product converges to 1 by the absolute signed total-variation covariance estimates of the completed formula. Identity (6) gives absolute passage through the $j$ sum. At $(0,0)$ the combined local factor is $(1-c_p)^2(1+2\alpha_p)$, so normalization by the exact total mass $\Sigma(N)$ of the completed autocorrelation gives (3)–(4). Equivalently $\iint\mathcal K_\chi=\int C_\chi=\Sigma(N)$, using (6) in (1) before integrating. At $p\mid N$ the second quotient in (3) is 1. Otherwise let $a_p=(p-2)/(p-1)$; since $r\mid N$, $p\nmid N$ implies $p\ge3$. Then the second quotient is $1-c_p((1-z)+(1-w))/a_p$. The first two factors in (3) are $1+c_p(1-z)/(1-c_p)$ and $1+c_p(1-w)/(1-c_p)$. Their combined linear deviations are bounded by $O(p^{-\beta-1}+p^{-2\beta})$ at large $p$, uniformly for $|z|=|w|=1$, since $a_p=1+O(p^{-1})$ and $|c_p|=p^{-\beta}$. All terms of degree at least two have magnitude $O(p^{-2\beta})$. The finite remaining factors are bounded for fixed $N$, and the displayed tail estimate proves uniform absolute convergence. Setting $\eta=-\xi$ cancels all shift phases, and realness of $R_j$ gives the first-color transform; (8) also reduces to its exact local formula.

For completeness no absolute inversion of the entire unrestricted bivariate transform is needed. By the elementary Abel bound of the first-color note,

$$
 |G_\chi(\xi)|\ll_{r,\beta,L'}
     (1+|\xi|)^{-\beta}\big(1+\log(2+|\xi|)\big).
 \tag{9}
$$

It follows from truncating the character Dirichlet series at $r(1+|\xi|)$, controlling the prefix absolutely and the tail by periodic sums, and using the simple zero on a fixed compact neighborhood of zero. In particular $G_\chi\in L^{4/3}\cap L^2$ since $\beta\ge.99>3/4$. Also $I_U\in L^2$, by Plancherel for the interval. The total multiplier in (4) is bounded for fixed $N$. The rectangle test in (5) is therefore absolutely integrable by Cauchy–Schwarz in each variable. For the diagonal test, put $g=|G_\chi|$; then

$$
 \iint g(\xi)g(\eta)|I_U(\xi+\eta)|\,d\xi\,d\eta
   \le\|g*g\|_2\|I_U\|_2
   \le \|g\|_{4/3}^2\|I_U\|_2 .
 \tag{10}
$$

The ordinary Young inequality proves the last step. The dependence of these absolute estimates on the fixed target, conductor or zero is not an asymptotic cap bound.

To identify the integrals with the true physical finite tests, multiply (4) by $e^{-\varepsilon(\xi^2+\eta^2)}$, $\varepsilon>0$. The corresponding kernel is the sum (1) with each $A_j$ convolved with the real Gaussian approximate identity. Its Fourier transform is now integrable on the whole plane, so ordinary inversion and integrations over the rectangle or the finite diagonal identify the respective integrals, with precisely $I_U(\xi)I_U(\eta)$ and $I_U(\xi+\eta)$. The mollified profiles converge to $A_j$ in $L^2$ and their norms are bounded by the original norms. Products on the diagonal converge in $L^1$ by the two $L^2$ factors, uniformly summably over $j$ by (6); rectangle averages converge by the same $L^2$ convergence against the fixed interval. Dominated convergence on the Fourier side follows from (10) and rectangle absolute integrability, and thus returns the genuine finite tests, regardless of individual jumps of $A_j$. Finally $C_\chi(0)=(2\pi)^{-1}\int\widehat C_\chi$ by the first-color inversion; insertion in (7) proves (5). The original denominator-margin error remains exactly that of the completed formula, since no changes were made to either $B_i$ or the actual real prefactors.

## 3. Both signs of the exact clipped two-variable operator

By (6), the signed rank-one representation (1) converges in trace norm on $L^2(\mathbb R)$: a rank-one operator with kernel $A_j(v)A_j(w)$ has trace norm $\|A_j\|_2^2$. Its sum is self-adjoint because all coefficients and profiles are real. Compression to $[0,U]$ remains trace class. The stationary covariance need not have the same positivity behavior: it averages along translations, whereas the present cutoff keeps both log size axes.

Choose distinct $p_1,\dots,p_s\nmid N$, $s\ge1$, and for every subset $E\subset\{1,\dots,s\}$ write $n_E=\prod_{i\in E}p_i$. On the real axis one can use actual local averages of (2) to isolate the jump at $\log n_E$. For $n_E>1$, take the difference of normalized indicators of short intervals immediately above and below $\log n_E$, choosing their length small enough to cross no other $\log n$ with integer $n$. For $n_E=1$, use just a normalized indicator of a short interval to the right of zero and strictly below $\log 2$, which isolates the initial coefficient $1$. These real $L^2$ tests can have all their involved intervals disjoint across the finitely many $n_E$. If $\prod_{i=1}^s p_i<e^U$, choose all the intervals within $[0,U]$: the strict inequality allows a nonempty right interval at the largest log. At each variable these tests integrate the difference of two literal integer cuts, so no regularization is involved in the matrix that follows.

The matrix of the exact bilinear form on these tests, by (2), is

$$
   \big(\mathcal N_\chi\,\alpha(n_E)\alpha(n_F)
                                     \mathbf1_{E\cap F=\varnothing}\big)_{E,F}.
 \tag{11}
$$

Each $\alpha(n_E)\ne0$ since the primes are outside $N$. Dividing the tests by those real coefficients is an invertible diagonal congruence. The remaining matrix apart from the nonzero real $\mathcal N_\chi$ is the tensor product of $s$ copies of $\begin{pmatrix}1&1\\1&0\end{pmatrix}$: each prime independently forbids only simultaneous membership in $E,F$. That $2$-by-$2$ matrix has one strictly positive and one strictly negative eigenvalue, from its negative determinant. Tensor products multiply eigenvalues, so for $s\ge1$ exactly $2^{s-1}$ eigenvalues of the finite matrix have either sign. The sign of $\mathcal N_\chi$ only interchanges them. The test functions are linearly independent (also forced by nonsingularity of (11)); the spectral theorem for a compact self-adjoint operator now gives at least that dimension of each signed spectral subspace. There are arbitrarily many primes not dividing the fixed $N$, so globally both eigenvalue sequences are infinite. The clip conclusion uses only the stated strict product condition. It rules out a generic positivity argument for the true two-variable kernel, but does not evaluate the particular trace tail and rectangle combination in (5).
