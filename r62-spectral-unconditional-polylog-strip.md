# Unconditional evaluation of the actual sharp strip at a polylogarithmic least prime

**Scope.** For an original sharp central divisor cut $D_N=\sqrt N(\log N)^{-B}$, we evaluate the signed high LCM block unconditionally down to a fixed power of $\log N$ in the least prime. The main term includes a positive sharp-boundary correction. The proof counts the actual removed midpoint strip by two positive rough factors and two signed rough factors; it does not make a global ordered-prime continuum replacement at this least prime. This is an almost-all theorem, not a pointwise Goldbach or spectral result. It does not estimate the residual below the stated least-prime threshold.

Fix $B>0$, $J\ge1$, $A_0>0$, set $L=\log N$, $\ell=\log X$, and let even $N\in[X,2X]$. Let $I$ range over the original half-open cells in $(N/2,9N/16]$, with length $H=N/(16\lceil L^J\rceil)$. Set $m=N-n$ and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Write $\Sigma(N)$ for the binary singular series. Use the original coefficients

$$
 F_{0,D}(m)=\sum_{\substack{e\mid m\\e\le D}}\mu(e),\qquad
 F_{1,D}(m)=\sum_{\substack{f\mid m\\f\le D}}\mu(f)
               \left(1-\frac{2\log f}{\log m}\right),\qquad
 G_D=F_{0,D}F_{1,D}-F_{0,D}.
$$

For $E=A_0+4J+40$, $C_0=10(E+1)$, any fixed $K>2C_0+2J+100$ suffices. Write $z_N=L^K$ and

$$
 c_*=2e^{-2\gamma_{\!E}}\int_0^\infty \rho(t)^2dt>0,
$$

where $\gamma_{\!E}$ is Euler's constant and $\rho$ is the Dickman function. Outside $O_{B,J,A_0,K}(X\ell^{-A_0})$ even moduli, in **every** cell for each remaining modulus,

$$
 \begin{split}
 \sum_{\substack{n\in I\\P^-(m)\ge z_N}}\lambda(n)F_{0,D_N}(m)
        &=O\!\left(\frac{\Sigma(N)H}{L^2}\right),\\
 \sum_{\substack{n\in I\\P^-(m)\ge z_N}}\lambda(n)G_{D_N}(m)
        &=\frac{\Sigma(N)H}{L}
          \left(1+c_*\frac{B}{K}+O\!\left(\frac1{\log L}\right)\right).
 \end{split}                                                     \tag{1}
$$

The two estimates also hold with the squarefree restriction on $m$. In particular the genuine less-rough shell $L^K\le P^-(m)<\exp((\log L)^C)$, for any fixed $C>2$, has signed high sum asymptotic to $c_* (B/K)\Sigma(N)H/L$. This follows by subtracting the [earlier subpower sharp result](spectral-midpoint-direct-sharp-subpower-cut.md) on the common good moduli; no assumption on zeros is used. The shell's signed low contribution remains $O(\Sigma(N)H/L^2)$.

## 1. The exact strip on squarefree partners

For squarefree $m>1$, at the full strict midpoint $e,f<\sqrt m$ the product of the two truncated sums equals $\mathbf1_{m\ {\rm prime}}$, by [complementary pairing](spectral-midpoint-parity-signed-transport.md): the first sum is zero on even-parity composites, and the second sum is zero on odd-parity composites. Define the removed arithmetic strip $\Xi_D(m)$ to be the full product minus the genuine product at $e,f\le D$. Throughout $V=[X/3,2X]$ we have $D<\sqrt m$ for all large $X$ at the eventual frozen $D$'s. On squarefree $m\in V$, put $a=(e,f)$, $e=ab$, $f=ac$, and $m=abcd$, so all four factors are squarefree and mutually coprime and the sign is $\mu(b)\mu(c)$. Then

$$
 \Xi_D(m)=
 \sum_{\substack{abcd=m\\ab<cd,\ ac<bd\\a\max(b,c)>D}}
       \mu(b)\mu(c)\left(1-\frac{2\log(ac)}{\log m}\right),\qquad
 G_D(m)=\mathbf1_{m\ {\rm prime}}-F_{0,D}(m)-\Xi_D(m).
                                                                    \tag{2}
$$

The inequalities $ab<cd$ and $ac<bd$ are respectively equivalent to $ab<\sqrt m$ and $ac<\sqrt m$. The strict lower bound $a\max(b,c)>D$ removes exactly the complement of both weak cuts $e,f\le D$. The weight lies in $[0,1]$. We extend the displayed four-factor sum to all integers $m\in V$ with $P^-(m)\ge z$ without the squarefree or cross-coprimality conditions, retaining the same strict inequalities; call the extension $\Xi_D^*(m)$. It is bounded by the four-divisor count $\tau_4(m)$ and agrees on squarefree $m$. We also use the extension $F_{0,D}$ with no squarefree gate.

The number of exceptional partners in a rough range $P^-(m)\ge z$ that are not squarefree is $O(X/z)$, by summing the counts of multiples of $p^2$ for $p\ge z$. The moment bound $\sum_{m\le2X}\tau_4(m)^2\ll X\ell^{15}$ follows from $\tau_4(m)^2\le\tau_{16}(m)$ (for each prime exponent, a pair of four-tuples of exponents can be realized as row and column sums of a nonnegative $4$-by-$4$ array). Cauchy–Schwarz and $\lambda(n)\le L$ bound any of these squarefree changes by $O(X\ell^{17/2}/\sqrt z)=O(H/L^2)$. The same bound covers the true $G_D$ since $|G_D|\ll\tau(m)^2\le\tau_4(m)$.

## 2. Three unconditional one-variable facts

On a frozen piece below, $z=(\log N_0)^K\asymp\ell^K$. Put $\kappa_z=\prod_{p<z}(1-1/p)$, and set $P^-(1)=+\infty$, $P^+(1)=1$. Fix $\delta_1>0$ and let $X^{\delta_1}\le Y\le2X$, $q\le Q=\ell^{C_0}<z$, and $(r,q)=1$. Uniformly in these parameters, with arbitrarily large fixed $A$,

$$
 \begin{split}
 \#\{d\le Y:P^-(d)\ge z,\ d\equiv r\pmod q\}
          &=\frac{\kappa_z}{\varphi(q)}Y+O_A(Y\ell^{-A}),\\
 \sum_{\substack{d\le Y\\P^-(d)\ge z\\d\equiv r\ ({\rm mod}\ q)}}\mu(d)
          &=O_A(Y\ell^{-A}).
 \end{split}                                                       \tag{3}
$$

For the first assertion, apply the elementary upper/lower Bonferroni truncations to divisibility by primes $p<z$ with $p\nmid q$, at two consecutive indices of size $j=\lfloor \delta_1\ell/(4\log z)\rfloor$. Multiples of each retained squarefree product have count $Y/(qd)+O(1)$ by CRT. Products used are all at most $z^{j+1}=O(X^{\delta_1/3})$, so the total floor error has that bound. The corresponding main terms sandwich the exact Euler product, with difference bounded by $(\sum_{p<z}1/p)^j/j!$, which is less than every fixed inverse power of $\ell$ by Stirling and $\sum_{p<z}1/p=O(1+\log\log z)$. Primes dividing $q$ impose no further condition on this progression. Removing their Euler factors gives $q^{-1}\prod_{p<z,p\nmid q}(1-1/p)=\kappa_z/\varphi(q)$.

For the second assertion, let $1_{{\rm sm},z}(h)=\mathbf1_{P^+(h)<z}$. The Euler convolution

$$
 \mu(d)\mathbf1_{P^-(d)\ge z}=(\mu*1_{{\rm sm},z})(d)
                                                                    \tag{4}
$$

is exact. In the reduced progression of (3) use $h\le\sqrt Y$ first. For each such $h$, the surviving condition is $(h,q)=1$ and the ordinary Möbius [Siegel–Walfisz bound](https://doi.org/10.1090/coll/053), in the reduced class $r\bar h\bmod q$, gives $O_A((Y/h)\ell^{-A})$ after increasing the logarithmic saving. This is the usual estimate $\sum_{j\le t,\,j\equiv b\bmod q}\mu(j)\ll_{A,M} t(\log t)^{-A}$ for fixed $M$, $q\le(\log t)^M$, $(b,q)=1$; see Iwaniec–Kowalski, Corollary 5.29, and the explicit formulation in [Matomäki–Radziwiłł–Shao–Tao–Teräväinen, (1.13)](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/higher-uniformity-of-arithmetic-functions-in-short-intervals-i-all-intervals/6DF08E2A3EFABB2DD0DA6CDA38649B18). Here $\log(Y/h)\gg_{\delta_1}\ell$, so the fixed logarithmic modulus range suffices. Also $\sum_{P^+(h)<z}1/h\ll\log z$ by Mertens. For $h>\sqrt Y$ drop the progression and bound trivially by $Y/h$. Rankin with $\sigma_z=1/\log z$ bounds that reciprocal tail by

$$
 Y^{-\sigma_z/2}\prod_{p<z}(1-p^{-1+\sigma_z})^{-1}
       \ll e^{-\log Y/(2\log z)}(\log z)^{C_1}.
                                                                    \tag{5}
$$

The fixed absolute exponent $C_1$ follows from $p^{\sigma_z}\le e$, separating bounded primes, then taking logarithms and using Mertens. The right side of (5) is less than every inverse power of $\ell$. This proves (3). All its conclusions allow interval endpoints anywhere in the stated range and bounded-variation weights by partial summation.

For the final fact let the actual signed rough reciprocal cumulative be

$$
 R_z(v)=\sum_{\substack{h\le z^v\\P^-(h)\ge z}}\frac{\mu(h)}h
        \qquad(v\ge0),
$$

and put $U=\ell/(10\log z)$. We will use

$$
 R_z(U),\ R_z(\log D/\log z)\ll_A\ell^{-A},\qquad
 \int_0^U R_z(v)\,dv=O(1),\qquad
 \int_0^U R_z(v)^2\,dv=\int_0^\infty\rho(v)^2dv+O((\log z)^{-2}).
                                                                    \tag{6}
$$

Here $D\asymp\sqrt X\ell^{-B}$. For a proof use (4) and the ordinary classical bound $\sum_{j\le T}\mu(j)/j\ll \exp(-c\sqrt{\log T})$ for $T\ge2$ (Montgomery–Vaughan, [Chapter 6](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287), Eq. 6.18). Split the convolution at $h\le z^{v/2}$, where that bound applies to the remaining ratio, and use (5), with $Y=z^v$, on the other half. The result on $v\ge2$ is

$$
 |R_z(v)|\ll (\log z)e^{-c\sqrt{v\log z}}
            +(\log z)^{C_1}e^{-v/2}.
                                                                    \tag{7}
$$

The initial cumulative sum for bounded real $T$ is uniformly bounded, as also follows from the same quoted estimate, so the Rankin tail has no further factor depending on $v$. Formula (7) proves the two endpoint bounds in (6). Both its first and second powers have arbitrarily small inverse powers of $\log z$ as integrals over $v\ge U_0=C_2\log\log z$, when the fixed $C_2$ is sufficiently large.

For $0\le v\le U_0$, ordinary PNT partial summation gives interval discrepancy $O(\exp(-c\sqrt{\log z}))$ for the prime measure $\sum_{z\le p\le z^{U_0}}p^{-1}\delta_{\log p/\log z}$ versus $dt/t$ on $[1,U_0]$. Both masses are $\log U_0+O(1)$. Write $R_z(v)$ as the ordered-prime factorial sum for $\exp_*(-K_1)$, with distinct primes in its discrete version, testing $\sum t_i\le v$. One-coordinate replacement uses this interval discrepancy and product masses; after division by the factorial it costs $O(U_0\exp(-c\sqrt{\log z}))$ in total. Removing repeated indices costs $O(U_0/z)$ by choosing one pair, using $\sum_{p\ge z}p^{-2}\ll1/z$, then summing the remaining product masses with the same factorial. The continuous cumulative is exactly $\rho(v)$ by the [Dickman convolution identity](spectral-midpoint-odd-aggregate-dickman.md). Together with the factorial tail of $\rho$ and (7), this proves all integral assertions of (6), with absolute integrability for the first as well.

## 3. Major arcs by treating the actual factors

Freeze the moving $N$ parameters on a mesh of width at most $X\ell^{-J-12}$, cutting also at changes of $\lceil L^J\rceil$, exactly as in the [direct sharp-cut proof](spectral-midpoint-direct-sharp-subpower-cut.md). In a frozen piece use a first interval $I_0$, $z=(\log N_0)^K$, $D=\sqrt{N_0}(\log N_0)^{-B}$, and $m\in V$. Approximate the Fourier polynomial of each of the three right coefficients in (2) on arcs $h/q+\eta$, $(h,q)=1$, $q\le Q$, $|\eta|\le 2Q/X$. Estimates will have error $O_A(X\ell^{-A})$ for every fixed $A$. All factors in the retained rough products are coprime to $q$ because $q<z$.

For the strip first treat $b>X^{1/10}$; then treat $c>X^{1/10}$ with $b\le X^{1/10}$. In each sector freeze the other three factors and sum the indicated signed factor. For example, when summing $b$, the inequalities $ab<cd$, $ac<bd$ are one upper and one lower bound; $a\max(b,c)>D$ is either automatic or a single lower bound. The physical restriction $abcd\in V$ and the sector gate are also an interval. For $c$ the same description holds with the roles reversed. The centered weight as a function of the summed variable is monotone between its endpoints and bounded by one on the support: for $c$ the ratio $\log(ac)/\log(abcd)$ is nondecreasing, and for $b$ its numerator is fixed. The phase $e(\eta abcd)$ has variation $O(Q)$ on $V$. The second estimate in (3) therefore gives $O_A((X/s)\ell^{-A})$ after summing all residues and variation, where $s$ is the product of the other three factors. Summing $1/s$ costs at most $O(\ell^3)$. Thus both large signed sectors are negligible on the major arcs. This is a signed cancellation using the actual Möbius coefficient, not an absolute tail estimate.

In the remaining bulk $b,c\le X^{1/10}$, $a>D/\max(b,c)>X^{.39}$ and $d>\sqrt m/\min(b,c)>X^{.39}$ for large $X$. For fixed $a,b,c$, apply the positive rough estimate in (3) in $d$ with the actual interval of admissible $d$ and the bounded-variation centered weight. The residue sum of $e(h abc\,d/q)$ is $\mu(q)$, since $abc$ is a unit. Errors are again $O_A(X\ell^{-A})$ after summing $1/(abc)$. Write $x=ab c\,d$ for the resulting real variable. The remaining sum over $a$ is exactly on the interval $D/\max(b,c)<a<\sqrt{x}/\max(b,c)$. This follows from the two strict midpoint inequalities, with $x$ fixed. Apply the positive rough estimate in (3) at $q=1$ to its weight $a^{-1}(1-2\log(ac)/\log x)$. Its supremum and variation on the interval are $O(1/a_{\min})$ and partial summation yields arbitrarily many logarithmic savings: more explicitly the endpoint errors are $O(\ell^{-A})$, and the integral error is $O(\ell^{-A}\int_{a_{\min}}^{a_{\max}}da/a)$ since the weight derivative is $O(a^{-2})$. The integral ratio is $O_B(\log\ell)$ after taking logarithms. Summing the signed factors in absolute weight for this error costs at most $O(\ell^2)$; any such log losses are absorbed.

Consequently the Fourier polynomial of $\Xi_D^*$ equals $\mu(q)/\varphi(q)$ times the Fourier transform on $V$ of the exact real model density

$$
 A_\Xi(x)=\kappa_z^2
   \sum_{\substack{b,c\le X^{1/10}\\P^-(bc)\ge z}}
      \frac{\mu(b)\mu(c)}{bc}
      \int_{D/\max(b,c)}^{\sqrt x/\max(b,c)}
             \left(1-\frac{2\log(ac)}{\log x}\right)\frac{da}{a},
                                                                    \tag{8}
$$

up to $O_A(X\ell^{-A})$. The factor $q^{-1}$ has become $\varphi(q)^{-1}$ before summing the reduced residues, as in (3); the second $\kappa_z$ comes from the real sum in $a$ only. All endpoint choices in the discrete argument were exact; the continuous endpoints have measure zero.

For the low term, write $m=ab$ with $a\le D$ signed by $\mu(a)$ and $b$ positive and rough. The latter is at least $X^{.49}$ for large $X$. Applying the positive bound in (3) directly in $b$ proves the same major formula with density
$A_{\rm low}(x)=\kappa_z R_z(\log D/\log z)$ on $V$, which is superlogarithmically small by (6). The prime indicator in (2) has the standard major formula with density $1/\log x$ on $V$ by ordinary prime Siegel–Walfisz, and every such prime already exceeds $z$.

## 4. The exact signed first moment and the circle transfer

In (8) change variables $\log a=\frac12\log x-\log\max(b,c)-u\log z$. Let $a_x=(\frac12\log x-\log D)/\log z$, and let $M_{z,U}$ be the restriction of the signed cumulative measure $dR_z(v)$ to $[0,U]$. Then, with $y=\log b/\log z$ and $v=\log c/\log z$, the inner weight times $da/a$ becomes

$$
 \frac{2(\log z)^2}{\log x}\big((y-v)_++u\big)\,du,
                 \qquad 0\le u\le a_x .
$$

In particular both the scale and the sign are governed by the *actual* signed max moment. Signed Fubini for the finite discrete measure gives

$$
 \iint (y-v)_+\,M_{z,U}(dy)M_{z,U}(dv)
     =R_z(U)\int_0^U R_z(w)\,dw-\int_0^U R_z(w)^2\,dw .
                                                                    \tag{9}
$$

The $u$ term gives $\tfrac12 a_x^2R_z(U)^2$. Formula (9) follows by integrating the indicator $v\le w<y$; endpoints of $w$ integration do not matter. By (6), the first term in (9) is negligible, while the second converges with the displayed error to $-\int\rho^2$. Also $\kappa_z\log z=e^{-\gamma_{\!E}}(1+O(1/\log z))$ by the ordinary Mertens product with its classical error, and $a_x=B/K+O_K(1/\log L)$ for the frozen $D,z$ and $x\in V$. We conclude uniformly that

$$
 A_\Xi(x)=-\frac1{\log x}\left(c_*\frac{B}{K}
                                     +O\!\left(\frac1{\log L}\right)\right).
                                                                    \tag{10}
$$

For Fourier truncation use the exact expression (8), or equivalently the polynomial in $a_x$ with the constants in (9), rather than the pointwise approximation (10). Formula (6), $\kappa_z\log z=O(1)$, and the smooth dependence of $a_x$ and $1/\log x$ give supremum and total variation $O(1/\ell)$ for $A_\Xi$ extended by zero off $V$. The low and prime densities obey the same bound.

We record the remaining transfer to quantify the exceptional set. On the minor arcs the left genuine weighted prime polynomial over $I_0$ has sup $O(X\ell^{-E})$ by Vaughan at the chosen $Q$, since the effective rational denominator is between $Q$ and $X/Q$. The squared torus norm of each right polynomial is $O(X\ell^{15})$ by Section 1. By Bessel, the squared sum of minor correlations in the integer target is $O(X^3\ell^{15-2E})$. At threshold $X\ell^{-J-2}$ and over all $O_J(\ell^{2J+12})$ frozen first intervals and the three right tests, this gives $O(X\ell^{31+4J-2E})$ exceptions. The left major formula has density $\mathbf1_{I_0}$ and the same residue factor $\mu(q)/\varphi(q)$ via ordinary prime Siegel–Walfisz. Multiplying the major factors and extending the Fourier integral to the whole real line costs $O(X\ell^{-1}Q^{-1}\log(2Q))$, using the two variation bounds and $\sum_{q\le Q}\varphi(q)^{-1}\ll\log(2Q)$. The true major errors are negligible after taking their arbitrary log exponent large enough. The complete real convolution is therefore multiplied by $\Sigma(N)$ with additive $O(\Sigma(N)H/L^2)$ outside a further $O(X\ell^{6-C_0/2})$ moduli: the mean absolute Ramanujan tail past $Q$ is $O(XQ^{-1/2})$ by $\sum_{N\le2X}|c_q(N)|\ll X\tau(q)$ and the convergent squarefree Euler product with extra factor $q^{1/2}$, and Markov at threshold $\ell^{-6}$ suffices. Both exception counts are $O(X\ell^{-A_0})$ for the stated parameters.

Finally, the original intervals and moving cuts can be restored with error $O(H/L^2)$ before using the squarefree identity (2). More precisely first make the transfer for the original cutoff coefficients on the frozen intervals using (2) and the uniform squarefree replacement from Section 1, then undo the parameter freezing on the **original** cut coefficients. The hyperbola and fourth-moment estimates of [the direct-cut proof](spectral-midpoint-direct-sharp-subpower-cut.md), Section 2, bound the changes in the cell endpoints and $D$. Moving the least-prime gate has relative width $O_K(\ell^{-J-12})$, so its potential primes have sum of reciprocals $O_K(\ell^{-J-12}+1/z)$ by counting even all integers. Summing $\tau(m)^2\lambda(n)$ over partners divisible by those primes costs $O_K(X\ell^4(\ell^{-J-12}+1/z))=O(H/L^2)$. The continuum change of the integration interval is smaller by the variation and uniform sup bounds just proved. Coupled with $\log(N-u)=L+O(1)$, equation (10) gives the **positive** correction after subtracting the removed strip in (2). This proves (1), with the stated squarefree option and the genuine signed shell consequence.
