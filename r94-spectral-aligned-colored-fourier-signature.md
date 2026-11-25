# The exact Fourier signature of the aligned colored covariance

**Scope.** This note factors the Fourier transform of the *completed* signed covariance in the [aligned colored cap formula](r93-spectral-completed-colored-caps.md). It identifies when that covariance is positive definite, exhibits genuine negative frequency bands in the other cases, and rewrites the actual first color as an absolutely convergent frequency integral on the original denominator-margin range. Neither a sign nor decay of the original finite cap is inferred from the spectral sign. The second color still depends on separate finite moments. There is no claim about unaligned targets, full exceptional-term smallness, or Hypothesis S.

Use the literal parameters of that formula: $G=\log Y$, $Y\le N\le2Y$ even, $\chi$ the primitive real Page character of conductor $r$, and $\beta>1-4a_0/\sqrt G$ its simple real zero. Assume $r\mid N$; the case with no exceptional character has no covariance to analyze. In particular $.99\le\beta<1$ for sufficiently large $G$. Keep $Q_0=\exp(16\sqrt G/\log G)$ and the denominator condition of that formula whenever applying the completed covariance to the actual correction; the identities for the defined covariance itself do not need the condition.

For $p\nmid r$ write $c_p=\chi(p)p^{-\beta}$. If $p\nmid N$, write $a_p=(p-2)/(p-1)$, $d_p=a_p-2c_p$ and $\alpha_p=c_p/d_p$; if $p\mid N$, put $\alpha_p=0$. These are precisely the local coefficients of the completed formula. Its signed profiles, normalization and mass are

$$
 C_\chi(t)=\mathcal N_\chi
   \sum_{j\ {\rm squarefree}}\mu(j)\alpha(j)^2
     \int_{\mathbb R}R_j(v)R_j(v+t)\,dv,\qquad
 \mathcal N_\chi=\frac{rP_{\chi,N}}{\varphi(r)L'(\beta,\chi)^2},
 \qquad \int_{\mathbb R}C_\chi(t)\,dt=\Sigma(N).
$$

Here $\alpha(j)$ is the original squarefree multiplicative coefficient, $R_j(v)=\mathbf1_{v\ge0}\sum_{n\le e^v,(n,j)=1}\alpha(n)$, $P_{\chi,N}$ is the real Euler factor in the completed formula, and $\Sigma(N)>0$ is the true binary singular factor. In particular this is the signed actual coefficient, not a substitution of positive weights or a changed normalization.

Use $\widehat f(\xi)=\int_{\mathbb R} f(t)e^{-i\xi t}\,dt$. Set $y_p(\xi)=1-\cos(\xi\log p)$ and define

$$
 \begin{split}
 D_p(\xi)
 &=\frac{|1-c_p e^{-i\xi\log p}|^2}{(1-c_p)^2}
       \frac{1+2\alpha_p\cos(\xi\log p)}{1+2\alpha_p}\\
 &=\left(1+\frac{2c_py_p(\xi)}{(1-c_p)^2}\right)
   \begin{cases}
     1,&p\mid N,\\
     1-2c_py_p(\xi)/a_p,&p\nmid N.
   \end{cases}
 \end{split}
 \tag{1}
$$

The real denominators in this formula are nonzero. In particular $1+2\alpha_p=a_p/d_p$ when $p\nmid N$. The prime 2, if it occurs in (1), lies in the $p\mid N$ case, because $N$ is even. No division by $1+\alpha_p$ is used.

**Theorem.** For real $\xi$ the exact signature is

$$
 \widehat C_\chi(\xi)
  =\Sigma(N)\left|\frac{L(\beta+i\xi,\chi)}{\xi L'(\beta,\chi)}\right|^2
        \mathscr D_{\chi,N}(\xi),\qquad
 \mathscr D_{\chi,N}(\xi)=\prod_{p\nmid r}D_p(\xi).
 \tag{2}
$$

At $\xi=0$ read the squared ratio as 1. The product over $p\nmid N$ converges uniformly on the real line, after keeping $p=3,5$ separately. The remaining product is finite. More precisely:

1. The Euler multiplier is strictly positive on $|\xi|\le1/10$; on $|\xi|\le1/\log G$ it is bounded above and below by positive absolute constants for all large $G$. Thus on this smaller window the only factor in (2) not accounted for by $\Sigma(N)$ and absolute constants is the squared normalized $L$-profile. The Fourier transform itself can have zeros there.
2. The covariance is positive definite if and only if there is **no** prime $p\in\{3,5\}$ such that $p\nmid N$ and $\chi(p)=+1$. If there is such a prime, $\widehat C_\chi$ is strictly negative on a nonempty open interval of real frequencies. This assertion classifies a possible Page character and target satisfying the hypotheses; it asserts no existence of a Page zero.
3. Let $T_x=\log(x/D^2)>0$ on the physical interval of the completed formula, with its original $D=\sqrt N(\log N)^{-B}$. Then the first color of its actual completed correction has the exact representation

$$
 B_0(x)=\frac{\Sigma(N)}{2\pi}
  \int_{\mathbb R}
  \left|\frac{L(\beta+i\xi,\chi)}{\xi L'(\beta,\chi)}\right|^2
       \mathscr D_{\chi,N}(\xi)
  \left(\frac{2\sin(T_x\xi)}{\xi}-T_x\cos(T_x\xi)\right)\,d\xi .
 \tag{3}
$$

The integral is absolutely convergent and the value of the last parenthesis at zero is $T_x$. It applies to the genuine first exceptional color with exactly the original approximation error and prefactor of the completed formula, not to the uncompleted finite denominator term without that error. The test in parentheses takes both signs; even global spectral positivity does not by itself give a sign for this finite-cap test.

## 1. Transform the genuine signed primitives

Use the real profile $R_*(v)=\mathbf1_{v\ge0}\sum_{n\le e^v}\chi(n)n^{-\beta}$. Periodicity and the zero $L(\beta,\chi)=0$ give $|R_*(v)|\ll r e^{-\beta v}$ for $v\ge0$. The signed convolution $R_j=R_* *\kappa_j$ of the completed formula has Laplace factor

$$
 H_j(s)=\prod_{p\nmid r}
     (1+\alpha_p\mathbf1_{p\nmid j}p^{-s})(1-c_p p^{-s}).
 \tag{4}
$$

The exponential total variation moment $M_j(\delta)$ of $\kappa_j$ is finite for a fixed small $\delta>0$; that formula proves both $\|R_j\|_1+\|R_j\|_2\ll r M_j(\delta)$ and $\sum_j|\mu(j)|\alpha(j)^2M_j(\delta)^2<\infty$. This controls the absolute sum of the $L^1$ norms of the autocorrelations and their sup norms. In particular no sign assumption on $\mathcal N_\chi$ or the terms is required for interchanging the sum and Fourier transform.

For real $\xi\ne0$, the Laplace identity and a limit from $\Re(s)>0$ yield

$$
 \widehat R_j(\xi)=\frac{L(\beta+i\xi,\chi)}{i\xi}H_j(i\xi).
 \tag{5}
$$

In detail, the Laplace transform of $R_*$ is $L(\beta+s,\chi)/s$, first by absolute summation for real $s>1-\beta$ and then by analyticity on $\Re(s)>0$. The exponential bound on $R_*$ justifies passage to $s=i\xi$, and the absolute convolution bound permits multiplication by $H_j(i\xi)$. Both sides extend at zero to $L'(\beta,\chi)H_j(0)$ since the zero is simple. This deals in particular with the jump of $R_*$ at log position zero without imposing a differentiability condition on the primitive.

Because $R_j$ is real, the transform of its displayed autocorrelation in $C_\chi$ is $|\widehat R_j(\xi)|^2$, by $L^1$ Fubini. The local two choices in the squarefree $j$ sum of $\mu(j)\alpha(j)^2|H_j(i\xi)|^2$ give

$$
 |1-c_pe^{-i\xi\log p}|^2
   \bigl(|1+\alpha_pe^{-i\xi\log p}|^2-\alpha_p^2\bigr)
 = |1-c_pe^{-i\xi\log p}|^2
   (1+2\alpha_p\cos(\xi\log p)).
 \tag{6}
$$

One rigorous factorization is to retain all factors of $H_j$ but restrict the occupied $j$-primes to a finite initial set in the sum. The outside $H_j$-factors then do not depend on $j$; their product tends to 1 as the initial set grows by the total-variation convergence in (4) for unoccupied primes of fixed $N$. The absolute bound for the $j$ sum permits passage to the limit. This argument also covers a zero of any local factor: it uses the subtraction of the two choices and no division by their uncombined factors. Dividing the *combined* Euler product by its nonzero value at zero yields exactly (1). The completed mass identity gives the normalization $\Sigma(N)$, since (5) at zero contains $L'(\beta,\chi)$, which was squared in the denominator of $\mathcal N_\chi$. Thus (2) includes any negative factor in $P_{\chi,N}$ correctly.

## 2. Uniform low frequencies and the exact sign test

For $p\nmid N$, formula (1) gives the useful cancellation

$$
 D_p(\xi)-1=
    2c_py_p(\xi)\left(\frac1{(1-c_p)^2}-\frac1{a_p}\right)
     -\frac{4c_p^2y_p(\xi)^2}{a_p(1-c_p)^2}.
 \tag{7}
$$

For $p\ge7$ all denominators are bounded away from zero. Since $|y_p|\le2$ and $|(1-c_p)^{-2}-a_p^{-1}|\ll p^{-1}+p^{-\beta}$, the bound $O(p^{-\beta-1}+p^{-2\beta})$ in (7) is uniform on the whole line. The tail is absolutely summable uniformly for $\beta\ge.99$. If $|\xi|\le1/10$, one can also use $y_p\le(\xi\log p)^2/2$ and $y_p^2\le 2y_p$; for $p\nmid N,\ p\ge7$ this yields $\sum_p|D_p(\xi)-1|\ll \xi^2$. The same estimate holds after separately including 3 and 5 whenever they do not divide $N$, on this frequency interval: their denominators in the second line of (1) are uniformly bounded below and the argument uses finite fixed primes only.

The first quotient in (1) is strictly positive, because $|c_p|<1$. For $p\ge7$, $4p^{-\beta}<(p-2)/(p-1)$ once $\beta\ge.99$, so the second factor is strictly positive and bounded below by an absolute constant there. For $p=3,5$ it is also positive on $|\xi|\le1/10$, using the quadratic bound on $y_p$ just noted, with $a_3=1/2$ and $a_5=3/4$. The resulting product over $p\nmid N$ stays between positive absolute constants on that interval: use (7) for the large primes and the positive, uniformly bounded factors for the finitely many remaining primes.

For $p\mid N,\ p\nmid r$, the first quotient in (1) is uniformly bounded below by $((1-|c_p|)/(1+|c_p|))^2$, at least a positive absolute constant for any such prime (including 2). Hence

$$
 \left|\log\prod_{\substack{p\mid N\\p\nmid r}} D_p(\xi)\right|
   \ll \xi^2\sum_{p\mid N} p^{-\beta}(\log p)^2
   \ll \xi^2(\log G)^2.
 \tag{8}
$$

For the second bound split at $G$. For $p\le G$ use $p^{1-\beta}\ll1$ and partial summation of the elementary Chebyshev bound $\sum_{p\le t}\log p\ll t$ to get $\sum_{p\le G}(\log p)^2/p\ll 1+(\log G)^2$. Above $G$, $p^{-\beta}\log p$ is decreasing and at $G$ is $O(\log G/G)$; use $\sum_{p\mid N}\log p\le\log N\ll G$ for the other log. This proves the claimed absolute-scale comparison on $|\xi|\le1/\log G$ without using any lower bound on the normalized $L$-profile. It proves positivity of the local product on the larger fixed window as well.

Outside $N$, a negative local factor can now occur only at 3 or 5, and only for $c_p>0$; for $c_p<0$ the second factor is at least 1. At either small prime with $c_p>0$, $4p^{-\beta}\ge4/p>a_p$, so its second factor is strictly negative when the cosine is sufficiently near $-1$, and strictly positive sufficiently near $+1$. If both small primes are eligible, $\log3/\log5$ is irrational by unique prime factorization. There exist real frequencies with the chosen one of the two phases equal to $\pi$ modulo $2\pi$ and the other arbitrarily close to 0 modulo $2\pi$: use the density of the integer multiples of the irrational ratio on the circle. For completeness, density follows by pigeonholing multiples to obtain a nonzero circle increment of any prescribed small size, then iterating that increment to approximate an arbitrary point. Continuity gives a nonempty open interval with exactly one negative factor. If only one prime is eligible, simply take its phase close to $\pi$. The absolutely convergent product of the remaining positive factors is nonzero throughout such an interval. Zeros of the analytic function $L(s,\chi)$ are isolated, so (2) is strictly negative on a nonempty open subinterval. In the absence of either eligible prime all factors are positive on the line and (2) is nonnegative everywhere.

## 3. Absolute inversion and what it implies

The signature is integrable, with no appeal to a bound on $1/L'(\beta,\chi)$ for this assertion at fixed $N$. At infinity split the character series for $L(\beta+i\xi,\chi)$ at an integer $M$ comparable with $r(1+|\xi|)$. Its absolute prefix is $O(M^{1-\beta}(1+\log M))$. Periodicity and Abel summation bound the tail by $O(r(1+|\xi|)M^{-\beta})$ since $\beta\ge.99$. Thus the squared $L$-ratio without the Euler multiplier is $O_{r,\beta,L'}((1+|\xi|)^{-2\beta}(1+\log(2+|\xi|))^2)$ for $|\xi|\ge1$. The fixed-$N$ multiplier is uniformly bounded on the whole line, by (7), the two small-prime factors, and the finite $N$-product. Near zero use analyticity and the simple zero. Therefore $\widehat C_\chi\in L^1$, and $C_\chi$ is continuous, real and even by the translation and absolute summability bounds already given. Fourier inversion applies pointwise; one can obtain this directly by inserting $e^{-\epsilon \xi^2}$, using the Gaussian approximate identity, and taking $\epsilon\downarrow0$ by dominated convergence.

With positive definite meaning $\sum_{j,k}z_j\overline{z_k}C_\chi(t_j-t_k)\ge0$ for every finite list of points and complex coefficients, inversion gives this immediately when the signature is nonnegative. Conversely, if that matrix inequality held, Riemann sums on compact supports would give a nonnegative quadratic form against each continuous compactly supported test function. By a compact cutoff approximation it would give the same for Schwartz tests, since the kernel is bounded. A nonzero smooth Fourier test supported inside the open negative interval just proved has a Schwartz inverse and a strictly negative quadratic form by inversion. Thus a negative interval actually disproves positive definiteness, not just a specific proof of it.

Finally insert inversion into $\int_{-T_x}^{T_x}C_\chi(t)\,dt-T_xC_\chi(T_x)$ and use evenness. The integral spans a finite interval and $\widehat C_\chi\in L^1$, so ordinary Fubini gives (3). The test is positive at zero and equals $-T_x$ at $2\pi/T_x$. This explains why a sign classification of the transform is not a sign classification of the finite cap. It also does not estimate the other color $T_x(C_\chi(0)-Q_\chi(U))+J_\chi(U)$, which depends on the separately clipped quantities $Q_\chi,J_\chi$ of the actual completed formula.
