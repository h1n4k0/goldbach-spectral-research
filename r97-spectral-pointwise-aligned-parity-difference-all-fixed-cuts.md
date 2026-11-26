# A pointwise lower bound for the aligned exceptional parity difference at all fixed cuts

**Scope.** On a hypothetical sufficiently close aligned Page-zero dyad, the **actual exceptional parity difference at each sufficiently planted target** has a strict sign and an inverse-logarithmic lower bound. This is not an average, and the cutoff restriction $U\le\log z$ of the earlier [complete-planting mean bound](r96-spectral-aligned-mean-euler-collapse.md) is not needed. The statement asserts no existence of such Page zeros or targets, gives no sign for either parity separately or for the full mixed-strip coefficient, and uses neither Dirichlet GRH nor an external zero-gap theorem. It says nothing about Hypothesis S.

Use the exact [aligned colored cap](r93-spectral-completed-colored-caps.md) notation: $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $Y\le N\le2Y$ even, $D=\sqrt N(\log N)^{-B}$, $H_0=\sqrt N(\log N)^{-B_0}$, with any fixed admissible $B>B_0>0$. Let $\chi$ be the genuine primitive real Page character of conductor $r\le Q_0$ and simple zero $\beta>1-4a_0/\sqrt G$. Assume $r\mid N$, $(1-\beta)G\le C_*\log G$ for a fixed $C_*>0$, and the literal denominator margin
$$
                  \log(Q_0/r)\ \ge\ (\log G)^3 .
$$
This last convenient sufficient margin can instead be the one of the aligned cap theorem with a sufficiently large fixed error exponent, as explained below. Assume $K_z=\prod_{p\le z}p$ divides this particular $N$, where $G^\epsilon\le z\le Z$ and $0<\epsilon<1/2$ is fixed. It is **not** assumed that $r\mid K_z$ or that $N$ has no additional prime factors. If $r\mid K_z$ then the displayed margin holds for all sufficiently large admissible $G$, by the prime number theorem and $z\le Z$.

The genuine left interval $I\subset(N/2,9N/16]$ is real and half-open. Its pointwise-BV weight $\omega$ is nonnegative, has uniformly bounded supremum and variation, and for the strict sign conclusion satisfies $\int_I\omega(n)\,dn\ge c_{\rm test}Y$ for a fixed $c_{\rm test}>0$. The test can vary with the target; there is no common-shape requirement. Let $\mathfrak E_\pm$ be the original two squarefree parity exceptional corrections, not their main terms.

**Theorem.** Uniformly under these hypotheses and for all sufficiently large qualifying targets,
$$
 -\chi(-1)\bigl(\mathfrak E_+(N;I,\omega)-\mathfrak E_-(N;I,\omega)\bigr)
        \gg \frac{Y^{2\beta-1}}{G}
                  \frac{\Sigma(N)}{(\log r)^4}.                    \tag{1}
$$
The constant can depend on the fixed cutoffs, $\epsilon,C_*,c_{\rm test}$ and the uniform bound on the tests. Here $\Sigma(N)$ is the **pointwise** binary singular factor, not the averaged $K_z/\varphi(K_z)$. In particular the exceptional parity difference has sign $-\chi(-1)$ on these targets only. More generally, without the lower normalization of the integral of $\omega$, the same lower bound holds with the extra factor $Y^{-1}\int_I\omega$ and with a subtractive error $O_A(Y^\beta G^{-A})$ at each fixed $A$ permitted by the aligned completion margin. This is a conclusion about the actual second-color scalar in the [two-frequency cap formula](r96-spectral-aligned-second-color-two-frequency.md), not a positivity claim for its indefinite clipped kernel.

## 1. A finite all-negative comparison on the true logarithmic short range

Put $\ell=\log z$, $U=\log(H_0/D)$, and $T_x=\log(x/D^2)$ for $N-x\in I$. Since $\epsilon\log G\le\ell\le\log G$, one has $T_x\asymp\ell$ and $0<U\le C\ell$ with a fixed $C>1$ depending on $\epsilon,B,B_0$. We keep the actual $U$ and $T_x$ throughout. All estimates on $[0,C\ell]$ below are uniform in the admissible targets, primes and character data.

For every prime $p$, use the exact pointwise $\alpha_p$ of the aligned cap formula, with $\alpha_p=0$ at $p\mid N$. In particular the conductor primes are excluded, and $\alpha_p=0$ for $p\le z$. For $p>z$ let
$$
       a_p=\frac{p-2}{p-1},\qquad
       b_p=\frac{p^{-\beta}}{a_p+2p^{-\beta}} .
$$
Then $b_p>0$ and $\alpha_p\ge-b_p$. Indeed if $p\nmid N$ and $\chi(p)=-1$, this is equality, since the denominator for $\alpha_p$ is $a_p-2\chi(p)p^{-\beta}$. If $\chi(p)=+1$ outside $N$ then the denominator is positive for large $z$, and $\alpha_p>0$. If $p\mid N$ the coefficient is zero. These are the actual unit masks; primes $p>z$ belonging to $N$ are not removed from the comparison.

Let $R_-(u)$ be zero for $u<0$ and otherwise the sum up to $n\le e^u$ of the squarefree multiplicative coefficient whose prime values are $-b_p$ at $p>z$ and zero at other primes. Its coefficient at $1$ is one. With $X$ a formal variable, the local quotient
$$
          \frac{1+\alpha_p X}{1-b_p X}
          =1+(\alpha_p+b_p)\sum_{j\ge1}b_p^{j-1}X^j
                  \qquad(p>z)                                  \tag{2}
$$
has nonnegative coefficients and constant one. Comparing coefficients of integers amounts to an exact convolution on log positions: the true primitive $R_1(u)=\sum_{n\le e^u}\alpha(n)$ is the convolution of $R_-$ with the nonnegative discrete measure given primewise by (2). This only requires finitely many primes and powers at each real $u$, so no unrestricted unweighted convergence is assumed. In particular the correcting measure has atom one at zero, and all shifts are nonnegative.

We claim uniformly on $0\le t\le C$ that
$$
 \begin{split}
 R_-(\ell t)&=\rho(t)+o_C(1),\\
 \rho(t)&=1+\sum_{1\le j\le\lfloor C\rfloor}
          \frac{(-1)^j}{j!}
        \int_{\substack{t_1,\ldots,t_j\ge1\\t_1+\cdots+t_j\le t}}
                      \frac{dt_1\cdots dt_j}{t_1\cdots t_j}.
 \end{split}                                                     \tag{3}
$$
To prove this, expand $R_-(\ell t)$ over the finite number of distinct prime factors of each squarefree $n$. No more than $\lfloor C\rfloor$ can occur, and every possible prime lies in $(z,z^C]$. On that range $b_p=(1+o_C(1))/p$ uniformly: use $(1-\beta)\ell=O(G^{-1/2}\log G)=o(1)$ and $a_p=1+O(1/p)$. The finite reciprocal prime measures on the normalized log range, $\sum_{z<p\le z^C}p^{-1}\delta_{\log p/\ell}$, converge weakly to $\mathbf1_{[1,C]}(t)\,dt/t$. Indeed the prime number theorem and partial summation give, uniformly in $1\le s\le C$,
$$
                        \sum_{z<p\le z^s}\frac1p=\log s+o_C(1).
$$
The endpoint terms are $O(1/\log z)$, and the asymptotic error in the prime count relative to $x/\log x$ is uniformly $o(1)$ for $x\ge z$. With $j$ fixed, repeated primes among the ordered tuples cost $O_C(\sum_{p>z}p^{-2})=o_C(1)$ before imposing the sum condition; the other reciprocal masses are bounded. The positive $j$-fold finite measures converge on the sum cutoff by product convergence (or finite rectangular approximation); their limiting cumulative distribution is continuous, since the component measures have densities. The convergence is uniform in the cutoff by a finite grid and monotonicity of each of these positive cumulative functions. This includes the weak endpoints, and the $j=0$ term is exactly one. These arguments prove (3), using one $j!$ to undo the ordering.

For clarity, the limiting function in (3) is the positive Dickman function, as can be seen directly. Extend it by zero below zero. It is one on $[0,1]$ and continuous on the nonnegative half-line when the same finite formula is used on successive compact intervals. Write $f(t)=\mathbf1_{t\ge1}/t$ and $f^{*0}=\delta_0$. For $j\ge1$, the derivative of the $j$th cumulative integral is $f^{*j}$ almost everywhere. By symmetry of its $j$ inputs,
$t f^{*j}(t)=j(\mathbf1_{[1,\infty)}*f^{*(j-1)})(t)$.
Hence $t\rho'(t)=-\rho(t-1)$ for almost every $t>1$, after changing the index in the finite sum. Integrating the resulting derivative identity for $t\rho(t)$ proves
$$
                         t\rho(t)=\int_{t-1}^t\rho(s)\,ds
                              \qquad(t\ge1),
$$
since both sides agree at $1$. A first zero above $1$ would make the right side positive by continuity and its preceding positivity, a contradiction. In particular $\min_{[0,C]}\rho>0$. It follows from (3) that $R_-\ge c_C>0$ on the needed interval for large $Y$. In the exact convolution (2), all arguments encountered are either below zero, where $R_-=0$, or within that positive interval. Its mass at zero proves the lower bound below for the true signed coefficients:
$$
             c_C\le R_1(u)\le C_C \qquad(0\le u\le C\ell).
                                                                    \tag{4}
$$
For the upper bound, sum all absolute coefficients, bounded by $\prod_{z<p\le z^C}(1+|\alpha_p|)$, and use $|\alpha_p|\ll p^{-\beta}\ll_C p^{-1}$ on this log range and the same bounded reciprocal mass. Also $R_1(u)=1$ for $0\le u\le\ell$, since every prime up to $z$ is excluded.

## 2. Keep the shifted diagonal tails in the true second color

Let $M=\mathcal N_\chi$ be the exact pointwise prefactor of the aligned cap and let $R=R_1$. Since all small primes are in $N$ and the remaining factors $a_p-2c_p$ are positive, $M>0$. All primitives $R_j$ and their norms are those of the aligned formula and finite by its moment argument. For squarefree $j$ with $\alpha(j)\ne0$, removing its prime factors in the Euler coefficients convolves $R$ with the product of the finite-variation signed geometric measures
$$
          \prod_{p\mid j}\ \sum_{k\ge0}(-\alpha_p)^k\delta_{k\log p}.
$$
This is an exact coefficient identity: multiplication by the local series inverts $1+\alpha_p p^{-s}$. All these $p$ exceed $z$ so $|\alpha_p|<1$, and the variation is at most $\prod_{p\mid j}(1-|\alpha_p|)^{-1}$. Young's inequality and the absolutely convergent Euler sum therefore give
$$
 \sum_{\substack{j>1\\ j\ {\rm squarefree}}}|\alpha(j)|^2\|R_j\|_2^2
 \le \|R\|_2^2
  \left\{\prod_{p>z}\left(1+\frac{|\alpha_p|^2}{(1-|\alpha_p|)^2}\right)-1\right\}
 \ll z^{1-2\beta}\|R\|_2^2.                                      \tag{5}
$$
Zero coefficient terms do not enter. The bound follows also by replacing the prime sum of $p^{-2\beta}$ by the integer sum; $\beta\ge.99$ uniformly eventually.

In the exact second color write $a_j=(U-\log j)_+$. From the pointwise definitions of $C_\chi(0)$, $Q_\chi(U)$ and $J_\chi(U)$, including the true shared cutoff shift,
$$
 B_1(x)=M\sum_{j\ {\rm squarefree}}\mu(j)\alpha(j)^2
         \left\{T_x\int_{a_j}^{\infty} R_j(u)^2\,du+
                          \left(\int_0^{a_j}R_j(u)\,du\right)^2\right\}.
                                                                    \tag{6}
$$
If $j>e^U$ the square integral is zero and the lower limit of the tail is zero, exactly as needed; the tail is not truncated there. Equation (6) is the genuine scalar of the completed model. It does not assert positive definiteness of the bivariate kernel. The absolute sum of $j>1$ in (6) is at most
$$
          O\!\left(M z^{1-2\beta}(T_x+U)\|R\|_2^2\right),           \tag{7}
$$
by (5) and Cauchy–Schwarz for the interval square.

To get a uniform lower bound, split by $\|R\|_2^2$ relative to a large fixed multiple of $\ell$. If $\|R\|_2^2\ge 2C C_C^2\ell$, then (4) shows $\int_U^\infty R^2\ge\|R\|_2^2/2$. As $T_x\asymp\ell$ and $U\le C\ell$, the positive $j=1$ tail absorbs (7) for large $Y$, leaving $\gg M\ell^2$. In the other case, (7) is $o(M\ell^2)$. If $U\le\ell/2$, the interval $[U,\ell]$ where $R=1$ makes the $j=1$ tail at least $\ell/2$. If $U>\ell/2$, (4) makes the $j=1$ square at least $c_C^2\ell^2/4$. The remaining $j=1$ part is nonnegative in both cases. We obtain
$$
                            B_1(x)\gg M\ell^2                     \tag{8}
$$
uniformly on the original physical support, with no special placement of $U$ within the bounded log scale.

## 3. Pointwise normalization and the actual error

At $p\nmid r$ use $c_p=\chi(p)p^{-\beta}$ as in the aligned formula. The exact pointwise normalization can be divided by $\Sigma(N)>0$ using the aligned mass identity:
$$
 \frac{M}{\Sigma(N)}
 =\frac1{L'(\beta,\chi)^2}
    \prod_{\substack{p\mid N\\p\nmid r}}(1-c_p)^{-2}
    \prod_{p\nmid N}(1-c_p)^{-2}(1-2c_p/a_p).
                                                                    \tag{9}
$$
The conductor factor $r/\varphi(r)$ cancels since $r\mid N$; each $p\nmid N$ contributes the exact quotient of its ordinary Euler factor by $a_p$. No small primes divide that last product's index set. Its logarithm has absolute sum $O(\sum_{p>z}(p^{-\beta-1}+p^{-2\beta}))=o(1)$, by first-order cancellation and the uniform strip. For the finite $N$-product, each factor is at least $(1+p^{-\beta})^{-2}$. Thus
$$
      \prod_{\substack{p\mid N\\p\nmid r}}(1-c_p)^{-2}
                   \ge \exp\left(-2\sum_{p\mid N}p^{-\beta}\right)
                   \gg \ell^{-2}.
$$
Indeed the reciprocal-prime estimate up to $G$ with leading coefficient one gives $\sum_{p\le G}1/p\le \log\log G+O(1)$; it also follows from the Euler product at $1+1/\log G$ and Chebyshev partial summation of $\sum_{p\le G}(\log p)/p$. The change to exponent $\beta$ costs $O((1-\beta)e^{(1-\beta)\log G}\log G)=o(1)$. Above $G$, there are at most $O(G/\log G)$ prime divisors of $N$, and each $p^{-\beta}\ll1/G$. Since $\ell\asymp\log G$, the required bound follows. The upper half of the near-exception inequality (11.10) of [Montgomery--Vaughan, Chapter 11](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF), by continuity at the simple zero after division by $|s-\beta|$, gives $|L'(\beta,\chi)|\ll(\log r)^2$ as used in the complete-planting mean. Consequently (8)--(9) imply the uniform pointwise lower bound
$$
                         B_1(x)\gg\frac{\Sigma(N)}{(\log r)^4}.
                                                                    \tag{10}
$$

Finally apply the original actual aligned completion theorem. Under the displayed margin its error is $O_A(Y^\beta G^{-A})$ for each fixed $A>0$; for a single sufficiently large such $A$, its weaker original requirement $\log(Q_0/r)\ge(C_0+A)(\log G)^2/\log\log G$ also suffices, with the fixed $C_0$ there. Subtracting the two parities preserves exactly the second-color contribution and cancels the first. Thus
$$
 -\chi(-1)(\mathfrak E_+-\mathfrak E_-)
   =\int_{N-x\in I}
      \frac{\omega(N-x)(N-x)^{\beta-1}x^{\beta-1}}{\log x}
            B_1(x)\,dx
                       +O_A(Y^\beta G^{-A}).                    \tag{11}
$$
The integrand is real and nonnegative under the given tests and (10). Since $x,N-x\asymp Y$, its integral has the stated lower bound with the factor $Y^{-1}\int_I\omega$. If this factor is at least $c_{\rm test}$, the admissible $(1-\beta)G\le C_*\log G$, $\log r\le16Z\ll\sqrt G$, and the positive absolute lower bound for $\Sigma(N)$ at even $N$ make the error smaller than half the lower bound by choosing a sufficiently large fixed $A$. The latter singular-factor bound follows from its product: the $p=2$ factor is positive and every permitted odd local factor is bounded below by $1-1/(p-1)^2$, whose product is positive. This proves (1) with the actual moving cuts and original numerical denominator. No claim about zeros or wider exceptional-free ranges follows from this sign implication.
