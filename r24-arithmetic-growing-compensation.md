# R24: from one compensated test to growing-prefix Hilbert–Schmidt compensation

Assume **global Dirichlet GRH**. Let \(\mathcal E_X=\{N\in[2X,11X/5]:N\text{ even}\}\), an ordinary even-modulus shell, and use the actual Li–Liu residual \(T_N\) in its physical log representation, including its exact unit restriction, zero-shift subtraction, and all signed Beta lines. Let \(P_b\) be the projection onto \(0<x\le b\), including the true edge at zero. For \(1\le b\le X^{1/40}\) and \(X^{-1/4}\le\tau\le1\),

\[
 \#\{N\in\mathcal E_X:\|P_bT_NP_b\|_{\rm HS}>\tau\}
 \ll_\epsilon \tau^{-4}b^{11/3}X^{2/3+\epsilon}.
 \tag{1}
\]

On any fixed window \(J\subset[a,B]\subset(0,\infty)\), if \(P_J\) denotes the physical restriction to \(J\), the corresponding bound improves to \(O_{a,B,\epsilon}(\tau^{-2}X^{2/3+\epsilon})\). This controls all modes of the specified compression, so any finite-dimensional selected family inside it, of arbitrary growing dimension, requires no entropy loss.

In particular set \(b=X^{1/40}\), \(\tau=X^{-1/100}\). Keep the divisor labels of [R22](r22-compressed-wide-d.md), \(b_*=N^{3/40}\), \(D_*=\lfloor\lceil4b_*N\rceil^{1/3}\rfloor\), \(Q=N^{7/8}\), for every \(N\), not a replacement cutoff defined using \(b\). For the exact [R23 prime-cofactor part](r23-arithmetic-prime-cofactors.md) \(C_N^{pp}\) and the complement \(C_N^{\mathrm{rest}}=C_{\rm rr}^*-C_N^{pp}\) in that same wide rough–rough remainder, outside at most \(O_\epsilon(X^{479/600+\epsilon})\) moduli in \(\mathcal E_X\),

\[
 \big\|P_b(C_N^{pp}+C_N^{\mathrm{rest}})P_b\big\|_{\rm HS}
 \ll_\epsilon X^{-1/1200+\epsilon}.
 \tag{2}
\]

On \(\gg X\) of these same moduli the two parts each have operator norm bounded below by an absolute positive constant, witnessed with opposite signs by the same R23 central test. Thus the cancellation holds in HS norm across the entire growing prefix, not just on that test. This uses global GRH for the auxiliary major arcs and the R22 comparison, and local GRH(N) for the identification of the physical kernel. Neither a pointwise bound for every even \(N\), a bound on exterior crosses, nor S or R follows.

## 1. Selected moving rectangles, with frequency repetitions counted once

Put \(Y=\lceil 8bX\rceil\), \(P=Y^{1/3}\), and \(L=\log(2Y)\). For each \(N\in\mathcal E_X\) prescribe any two intervals \(I_N,J_N\subset[0,b]\), chosen completely arbitrarily, possibly using knowledge of the signed measure. Let \(\mu_N\) be the true signed line measure after diagonal subtraction, arithmetic weight \(\Lambda(n)\Lambda(m)/N\) for each unit pair, minus the line model of density \(\mathfrak S(kN)\) in the dimensionless first coordinate. Use the original outer signs: minus for \(n+m=kN\), plus for each difference orientation. We prove uniformly over all the interval choices that

\[
 \sum_{N\in\mathcal E_X}|\mu_N(I_N\times J_N)|^2
 \ll_\epsilon b^{11/3}X^{2/3+\epsilon}.
 \tag{3}
\]

There are at most \(3\lfloor2b\rfloor\) lines of these forms. Restrict first to one orientation, using \(n\pm m=kN\), and swap \(n,m\) for the other. Let \(h=kN\). For each \((N,k)\), collapse the two raw interval cuts to their intersection on the \(n\)-coordinate after solving for \(m\). This is a single interval \(I_{N,k}'\), possibly empty; it also includes the requirement \(m\in[0,Y]\), redundant for the initial interval cuts. The second exponential sum can be the fixed full sum \(U(\alpha)=\sum_{1\le m\le Y}\Lambda(m)e(m\alpha)\), conjugated for the difference. Here both raw coordinate supports and \(h=kN\) are \(O(bX)\) and in \([0,Y]\). Initially omit the exact unit restriction for the integer count; the model remains unchanged. The fixed-second-factor overlap integral is exactly the raw length of the collapsed real interval for both orientations. Endpoints matter only for the arithmetic sum, and the major estimate is for exactly the chosen interval, not a bracketing by other moduli.

Take the major arcs at reduced \(a/q\), \(q\le P\), of width \(P/(qY)\). They are disjoint as \(2P^2<Y\). On the complement Dirichlet approximation gives a denominator \(P<q\ll Y/P\) and error at most \(q^{-2}\). The classical Vinogradov–Vaughan estimate, as in [Ren, Corollary 1.2](https://hkumath.hku.hk/~imr/IMRPreprintSeries/2004/IMR2004-9.pdf), gives \(\sup_{\rm minor}|U|\ll_\epsilon Y^{5/6+\epsilon}\); the three powers are bounded by \(Y/\sqrt q+Y^{4/5}+\sqrt{Yq}\ll Y^{5/6}\). Dyadic sums and harmless logarithms pass the stated dyadic prime bound to the full sum. In estimating minor errors only, partition the **integer points** of each \(I_{N,k}'\) into dyadic integer intervals, at most two at each level of a common grid on \([1,2^{\lceil\log_2Y\rceil}]\), with \(U\) and all other sums extended by zero past \(Y\). There are \(O(L)\) intervals for each \((N,k)\). Cauchy–Schwarz bounds its squared minor error by \(O(L)\) times the sum of the squared Fourier coefficients for these individual dyadic blocks. For a fixed dyadic interval \(I\) and orientation write those coefficients as

\[
 b_I(h)=\int_{\rm minor} P_I(\alpha)\,U^\pm(\alpha)e(-h\alpha)\,d\alpha,
 \qquad P_I(\alpha)=\sum_{n\in I\cap[1,Y]}\Lambda(n)e(n\alpha),
\]

with \(U^+=U\), \(U^-=\overline U\). As \((N,k)\) vary, a positive frequency \(h\le Y\) has at most \(d(h)\ll_\epsilon Y^\epsilon\) representations as \(kN\), regardless of the chosen interval per pair. Thus summing over eligible pairs for each dyadic block and then over blocks at one level costs at most

\[
 \begin{split}
 Y^\epsilon \sum_I\sum_{h\in\mathbb Z}|b_I(h)|^2
 &\ll_\epsilon Y^\epsilon\sup_{\rm minor}|U|^2\sum_I\int_0^1 |P_I(\alpha)|^2\,d\alpha\\
 &\ll_\epsilon Y^{8/3+\epsilon},
 \end{split}
\]

by Parseval and disjoint integer dyadic blocks at that level, since \(\sum_{n\le Y}\Lambda(n)^2\ll YL\). Including all levels and the Cauchy factor merely relabels \(\epsilon\). In particular **the sum of squared raw minor errors over all \((N,k)\)**, for each orientation, is \(O_\epsilon(Y^{8/3+\epsilon})\), not that bound times the number of aliases. Neither sparse-family fourth-moment estimates nor a moving grid are needed.

For the major part use the [R13 integrated GRH estimate](spectral-post-r12-major-plancherel.md), already proved for arbitrary hard intervals in a common raw range. For clarity, the uniform bound in raw coordinates is

\[
 O_\epsilon\big(\sqrt{Y}P L^3+P^2 L^5+Y^{1+\epsilon}/P\big).
 \tag{4}
\]

It applies to each collapsed real interval and the uncut second factor, independently of their location and of the phase \(h\le Y\); complex conjugation for the difference does not change the errors. The improved double-error size in (4) uses Abel summation before squaring the \(\beta\)-integral: with \(B_q=P/(qY)\) and \(\Psi_\chi(u)=\sum_{n\le u}\Lambda(n)\chi(n)-\delta_\chi u\), one has \(\sup_{[0,Y]}|\Psi_\chi|\ll\sqrt Y L^2\) under the GRH character PNT. Endpoint terms have square integral \(O(YB_q L^4)\), and the Fourier transform of \(1_{I'}\Psi_\chi\) occurs multiplied by \(\beta\), giving \(O(Y^2B_q^2 L^4)\) by real-line Plancherel. Then finite Parseval in the numerator \(a\bmod q\) bounds the denominator's integrated error energy by \(O(P^2L^4/q)\); Cauchy bounds the double error by the same expression. The mixed error is \(O(\sqrt Y P L^2/\sqrt{q\varphi(q)})\) at denominator \(q\), by finite Parseval and the interval transform bound \(Y/(1+Y|\beta|)\). Its sum is \(O(\sqrt Y PL^3)\). The singular-series and real-integral tails are \(O_\epsilon(Y^{1+\epsilon}/P)\) uniformly as in R13, with the full model at shift \(h\) and **exact** archimedean overlap. This explains the inputs needed from R13 and in particular why \(P=Y^{1/3}\) is allowed here; a pointwise-in-\(\beta\) product estimate alone would not give (4). With this \(P\), (4) is \(O_\epsilon(Y^{5/6+\epsilon})\) raw per line.

On any included line the removal of nonunit Mangoldt pairs costs only \(O(L^3)\) raw. For each prime \(p\mid N\), the total \(\Lambda\) weight over its powers \(\le Y\) is \(O(L)\), the partner is unique on the line and has weight at most \(L\), and the number of such primes is \(O(L)\). This unit correction also respects the original interval conventions and does not modify the Beta density. Normalize every line by \(1/N\), not \(1/h\). For the minor contribution to (3), Cauchy over \(O(b)\) aliases gives

\[
 \ll_\epsilon \frac{bY^{8/3+\epsilon}}{X^2}
 \ll_\epsilon b^{11/3}X^{2/3+\epsilon},
\]

where we relabel \(\epsilon\) using \(b\le X^{1/40}\). For the major and unit contribution, summing the uniform pointwise bound over the aliases before squaring gives

\[
 \ll_\epsilon X\left(\frac{bY^{5/6+\epsilon}}{X}\right)^2
 \ll_\epsilon b^{11/3}X^{2/3+\epsilon}.
\]

The constant number of orientations does not change either exponent. The original signs are applied before comparing the actual combined discrepancy to these bounds, and (3) follows.

## 2. Worst rectangles determine all within-prefix modes

Define \(U_N^* = \sup_{I,J\subset[0,b]}\left|\mu_N(I\times J)\right|\), with the supremum over intervals, all including the actual one-dimensional real cuts and the corresponding integer endpoint convention. The interval masses are bounded for each \(N\); select intervals approaching each individual supremum in (3) and pass to the limit in the finite shell. This proves

\[
 \sum_{N\in\mathcal E_X}(U_N^*)^2\ll_\epsilon b^{11/3}X^{2/3+\epsilon}.
 \tag{5}
\]

No supremum was moved through an integral. If the measure has a nonzero mass on an endpoint, half-open or closed cut conventions can equally be treated with the collapse proof; the layer-cake rectangles below can use the matching convention.

Let \(M_N(x,y)=\int_{(0,x]\times(0,y]}\sqrt{uv}\,d\mu_N\) and \(K_N(\log x,\log y)=2\pi M_N(x,y)/(xy\sqrt{w_N(x)w_N(y)})\). This is precisely the R22 kernel, with \(w_N(x)=((Nx)^{-2/\log N}+(Nx)^{-1/4})^{-1}\). By representing \(\sqrt{uv}\) using positive superlevel cutoffs in its two variables, \(|M_N(x,y)|\le U_N^*\sqrt{xy}\).

A complementary elementary bound, valid all the way to the true edge, is

\[
 |M_N(x,y)|\ll L^2(xy)^{3/2},\qquad 0<x,y\le b.
 \tag{6}
\]

If \(x\le y\), the kernel vanishes unless \(x+y\ge1\), hence \(y\ge1/2\). For each integer \(n\le Nx\) there are at most \(O(y)\) eligible partners over the three nonzero orientations, each with Mangoldt product bounded by \(L^2\); normalizing by \(1/N\) gives mass \(O(L^2xy)\) (no additive edge count). On the continuous lines the smaller-coordinate overlap per shift is \(\le x\), and \(\sum_{k\le 2y}\mathfrak S(kN)\ll y\mathfrak S(N)\ll y L^2\). For the first inequality, expand the positive inflation \(\mathfrak S(kN)/\mathfrak S(N)=\prod_{p\mid k,\,p\nmid 2N}(1+1/(p-2))\) and use convergence of \(\prod_{p>2}(1+1/(p(p-2)))\); for the second use the usual Euler factors and Mertens' product bound. Thus both parts obey the mass cap, and multiplying by \(\sqrt{xy}\) proves (6).

On \(x,y\ge1/N\), \(w_N(x),w_N(y)\ge1/2\). Multiplying the two respective estimates for absolute kernel size therefore gives \(|K_N|^2\ll L^2 U_N^*\). The area in \((\log x,\log y)\) is \(O(L^2)\). If \(x<1/N\) there are no arithmetic atoms in that leg and a nonzero model term forces \(y\ge1-1/N\); the reflected edge is analogous. Square (6) divided by the kernel denominator and use \(d\log x\,d\log y=dx\,dy/(xy)\). Since

\[
 \int_0^{1/N}\frac{dx}{w_N(x)}=\frac1N\int_0^1(t^{-2/\log N}+t^{-1/4})\,dt\ll \frac1N,
\]

and \(1/w_N(y)\le2\) on this remaining edge, its squared HS contribution is \(O(b L^4/N)\). This proves the full physical estimate

\[
 \|P_bT_NP_b\|_{\rm HS}^2\ll L^4\big(U_N^*+b/N\big).
 \tag{7}
\]

For the range in (1) the additive term is \(o(\tau^2)\). Each exceptional modulus must have \(U_N^*\gg\tau^2/L^4\). Equation (5) proves (1) after absorbing logarithms. For a fixed window away from zero, take fixed \(b\ge\max(1,B)\) and integrate only over \(x,y\in[a,B]\); the first bound on \(M_N\) gives \(\|P_JT_NP_J\|_{\rm HS}\ll_{a,B} U_N^*\) directly, proving the stated \(\tau^{-2}\) exception bound.

## 3. Actual compensation, with both pieces non-negligible on the same moduli

At \(b=X^{1/40}\), \(\tau=X^{-1/100}\), the exponent in (1) is \(2/3+11/120+1/25=479/600\). Since \(b\le N^{1/40}\) for every \(N\in\mathcal E_X\), [R22](r22-compressed-wide-d.md) gives

\[
 \|P_b(T_N-C_{\rm rr}^*)P_b\|_{\rm HS}\ll_\epsilon X^{-1/1200+\epsilon}.
\]

This proves (2) by the triangle inequality on the same physical prefix, preserving all cutoff labels rather than resetting them at \(b\). Its exceptions are \(o(X)\). Thus the set of \(\gg X\) moduli from the [R23 prime-cofactor proposition](r23-arithmetic-prime-cofactors.md), where \(\mathfrak S(N)\) is bounded and its form is negative with magnitude bounded below on a fixed bounded central test, retains \(\gg X\) members after those exceptions are removed. That test is supported in \(P_b\) for all the chosen \(b\), so (2) forces an opposite non-negligible form for the exact complementary part on it; it simultaneously bounds the residual sum on **all** directions of this prefix. Neither part is estimated independently by a small norm. The proof does not identify the moduli which remain exceptional, and gives no bound on the original operator outside this compression.
