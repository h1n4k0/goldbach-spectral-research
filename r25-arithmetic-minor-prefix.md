# R25: pointwise minor-arc isolation on the full wide prefix

Assume **global Dirichlet GRH**, with local GRH(N) for the physical representation of Li–Liu's residual. Let \(N\) range over the ordinary even shell \(\mathcal E_X=[2X,11X/5]\cap2\mathbb Z\), \(1\le b\le(11X/5)^{3/40}\), \(Y=\lceil8bX\rceil\), \(L=\log(2Y)\), and \(Y^{1/3}\le P\le Y^{2/5}\). Use the common minor arcs \(\mathfrak m\) complementary to the reduced fractions \(a/q\) with \(q\le P\), \(|\alpha-a/q|\le P/(qY)\) on \(\mathbb R/\mathbb Z\). There is an explicit arithmetic minor-arc operator \(\mathcal M_{N,b,P}\) defined below, such that for **every** \(N\) in the shell

\[
 \|P_bT_NP_b-\mathcal M_{N,b,P}\|_{\rm HS}
 \ll_\epsilon b^{1/2}P X^{-1/2+\epsilon}.
 \tag{1}
\]

The same error applies to the difference of the two operator norms. In particular with \(b=(11X/5)^{3/40}\), \(P=Y^{2/5}\), this is \(O_\epsilon(X^{-13/400+\epsilon})\), so an exceptional modulus at an inverse-log threshold or the power thresholds below must come from this concrete minor-arc operator, not the genuine major-arc contribution or the near-zero edge. Estimates for its norm on individual exceptional moduli are still missing. Statement (1) concerns the full physical prefix, not just the fixed central test.

There is also a stronger averaged consequence than the [R24 wide addendum](r24-arithmetic-wide-prefix-addendum.md):

\[
 \sum_{N\in\mathcal E_X}\!\|\mathcal M_{N,b,P}\|_{\rm HS}^{2}
 \ll_\epsilon \frac{Y^{2+\epsilon}}{X P}.
 \tag{2}
\]

At the full original wide prefix \(b_N=N^{3/40}\), this gives \(O_\epsilon(X^{29/40+\epsilon})\) exceptions to \(\|P_{b_N}T_NP_{b_N}\|_{\rm HS}\le X^{-1/400}\), and \(O_\epsilon(X^{37/50+\epsilon})\) at the stronger threshold \(X^{-1/100}\). Both counts are among the ordinary even moduli in the shell, not a bound within a prescribed sparse subfamily. The pure rough–rough comparison from R22 remains restricted to its stated narrower prefix. No bound for exterior crosses, or proof or refutation of S/R, is asserted.

## 1. An actual minor operator with exact line geometry

Use the exact physical log kernel of [R24](r24-arithmetic-growing-compensation.md). It is \(2\pi A_N(x,y)/(xy\sqrt{w_N(x)w_N(y)})\), where \(A_N\) is the normalized signed cumulative with weight \(\sqrt{uv}\), and \(w_N(x)=((Nx)^{-2/\log N}+(Nx)^{-1/4})^{-1}\). The three nonzero alias orientations are \(n+m=kN\) with sign minus, and \(n-m=kN,m-n=kN\) with sign plus. The zero-shift diagonal is not included. On each line the genuine normalized arithmetic count is restricted to units modulo \(N\), and the continuous model is \(\mathfrak S(kN)\) times archimedean length in the dimensionless first coordinate, with the same outer sign. All of these facts refer to the exact weight/diagonal/model of the residual, not a centered surrogate.

Fix cumulative endpoints \(x\le y\) in \((0,b]\). For each layer-cake rectangle \([s,x]\times[t,y]\) with \(0<s<x,0<t<y\), and each of the three orientations and each positive \(k\le2y\), collapse the raw cut to an interval \(I\) in the **first, shorter-axis** variable \(n\): require \(Ns\le n\le Nx\) and \(Nt\le m(n)\le Ny\), where \(m(n)\) is uniquely determined by the line. For an empty interval set both the major and minor line integrals to zero. For a nonempty interval, \(I\subset[0,Nx]\), and its raw length is exactly the continuous overlap on the line. The partner \(m(n)\) is within \([0,Y]\), so unweighting the partner cutoff after collapsing does not change the line count or its model. Define \(S_I(\alpha)=\sum_{n\in I\cap\mathbb Z_{>0}}\Lambda(n)e(n\alpha)\) and \(U(\alpha)=\sum_{1\le m\le Y}\Lambda(m)e(m\alpha)\), where \(e(u)=e^{2\pi i u}\). Define \(D_N^{\mathfrak m}(s,x;t,y)\) as the sum over these lines of their signed minor integrals, all normalized by \(1/N\):

\[
 \begin{array}{c|c}
 \text{line} & \text{integrand before outer sign and }1/N\\ \hline
 n+m=kN & S_I U e(-kN\alpha)\\
 n-m=kN & S_I\overline U e(-kN\alpha)\\
 m-n=kN & S_I\overline U e(kN\alpha).
 \end{array}
\]

There is no unit restriction in \(S_I,U\); its correction on each *actual* line is inserted in the deterministic error below. This definition freezes the short-axis choice for the enclosing pair \(x,y\), and need not be interpreted as a single globally additive rectangle measure. For \(x\le y\), define

\[
 A_N^{\mathfrak m}(x,y)=\int_0^x\!\int_0^y D_N^{\mathfrak m}(s,x;t,y)\,\frac{dt\,ds}{4\sqrt{st}}.
\]

Use its transpose for \(x>y\). The minor arcs are symmetric under \(\alpha\mapsto-\alpha\), so the integrals are real. Put \(a_N=P^2/N\). The kernel of \(\mathcal M_{N,b,P}\), in physical log coordinates, is \(2\pi A_N^{\mathfrak m}(x,y)/(xy\sqrt{w_N(x)w_N(y)})\) on \(a_N\le x,y\le b\), and zero otherwise. Values on the logarithmic diagonal do not affect the operator. This is an actual symmetric square-integrable kernel. The point of collapsing before taking minors is that **no** terms are introduced from lines disjoint from the rectangle, and only \(O(y)\) integer shifts can contribute for \(x\le y\). Both the exact cumulative and its minor version vanish for \(x+y<1\).

## 2. Uniform major error saving the shorter physical axis

Fix one of the collapsed intervals with \(I\subset[0,T]\), \(T=Nx\), \(P^2\le T\le Y\); the other Fourier factor is the full interval \([0,Y]\). The same calculation applies to its conjugate. Let \(B_q=P/(qY)\), \(V_I(\beta)=\int_I e(\beta u)\,du\), and write the major approximation for each factor as \(\mu(q)V/\varphi(q)+E\) on \(\alpha=a/q+\beta\). The key mixed-scale version of [R13's integrated major estimate](spectral-post-r12-major-plancherel.md) is

\[
 \sum_{a\bmod q}\int_{-B_q}^{B_q}|E_I(a,q,\beta)|^2,d\beta
 \ll q L^4(TB_q+T^2B_q^2)
 \ll \frac TY\frac{P^2L^4}{q}.
 \tag{3}
\]

Here \(E_I\) off the reduced numerator classes means the same finite Fourier transform of the unit-residue error plus the nonunit part, so the finite Parseval identity is legitimate. To prove (3), the conditional character PNT gives \(\sup_{u\le T}|\sum_{n\le u}\Lambda(n)\chi(n)-\delta_\chi u|\ll\sqrt T L^2\) for every \(q\le P\). In the small endpoint range \(u<\max(q,e^{10})\), the elementary bound suffices since \(q\le\sqrt T\); for \(q=1,2\) use the ordinary RH PNT, accounting for the powers of 2. Partial summation leaves endpoint terms of that size and \(\beta\) times the real Fourier transform of the prefix discrepancy restricted to \(I\). Their squared \(\beta\) integrals cost \(O(L^4(TB_q+T^2B_q^2))\) by real Plancherel. Finite Parseval in \(a\) converts to (3) as in R13, and the omitted nonunit prime-power term contributes at most \(O(qL^4 B_q)\). For the long factor take \(T=Y\) in (3). The same estimates use the exact open/closed endpoints for the arithmetic sum, even when the continuous interval has zero length.

By real Plancherel, \(\int_{\mathbb R}|V_I(\beta)|^2d\beta\le T\), and the corresponding bound for the long interval is \(Y\). Apply Cauchy–Schwarz jointly in \(a,\beta\) at each denominator. For **either** mixed term, (3) and these main-term energies give

\[
 O\!\left(\frac{\sqrt T P L^2}{\sqrt{q\varphi(q)}}\right).
\]

Summing over \(q\le P\) gives \(O(\sqrt T P L^3)\) (e.g. use the convergent divisor mean of \(q/\varphi(q)\)). The two-error product costs \(O(\sqrt{T/Y}P^2L^4/q)\) at denominator \(q\), and thus \(O(\sqrt{T/Y}P^2L^5)\) in all. These are bounds for individual phases \(e(\pm kN\alpha)\), whose modulus is one. No averaging in \(N\) is used here.

For the principal term, after summing the reduced numerators its coefficient is \(\mu^2(q)c_q(kN)/\varphi(q)^2\) (unchanged for the reflected difference). The [individual Ramanujan tails from R11](arithmetic-post-round10-exceptions.md) are \(O_\epsilon(Y^\epsilon/P)\) for the absolute sum over \(q>P\), and \(O_\epsilon(Y^\epsilon)\) for the sum over \(q\le P\) with an additional factor \(q\). These bounds follow from \(\mu^2(q)|c_q(kN)|\le(q,kN)\) by the usual divisor split and hold because \(kN\le Y\). The full real singular integral is the exact collapsed overlap length, at most \(T\). For \(q\le P\), since \(B_q\ge1/Y\) and the two interval transforms are bounded by \(\min(T,|\beta|^{-1})\) and \(\min(Y,|\beta|^{-1})\), its truncated tail is

\[
 O\!\left(\min\{Yq/P,,TL\}\right)
 \ll (TYq/P)^{1/2}L^{1/2}.
\]

Summing this tail with the absolute Ramanujan coefficients costs \(O_\epsilon((TY/P)^{1/2}Y^\epsilon)\); tails over \(q>P\) cost \(O_\epsilon(TY^\epsilon/P)\). As \(Y^{1/3}\le P\le Y^{2/5}\) and \(T\le Y\), all these errors, mixed and double ones included, are \(O_\epsilon(\sqrt T P\,Y^\epsilon)\). The full singular series is precisely the model \(\mathfrak S(kN)\). Thus the major arcs minus the exact continuous model for **one line** have error \(O_\epsilon(\sqrt T P\,Y^\epsilon)\) raw, uniformly for the collapsed interval and for each orientation.

On such a line removal of nonunits changes the arithmetic count by \(O(L^3)\): the only nonunit \(\Lambda\)-support is powers of primes dividing \(N\), whose weights sum to \(O(L)\) per base, and each fixes a partner of weight \(O(L)\). Assign this change to the deterministic error. After summing \(O(y)\) possible aliases and division by \(N\), the difference between the actual weighted line geometry before the square-root layer cake and the corresponding minor rectangle discrepancy is \(O_\epsilon(y\sqrt{Nx} P Y^\epsilon/N)\), for \(x\le y\) and \(x,y\ge a_N\). The weights of the layer cake have total mass \(\sqrt{xy}\). Divide by the log-kernel denominator and note \(w_N(x),w_N(y)\ge1/2\) on this bulk. Its error kernel is bounded pointwise by

\[
 O_\epsilon\big(\sqrt y\,P X^{-1/2+\epsilon}\big),\qquad x\le y.
\]

The integral of \(y\) over \(a_N\le x\le y\le b\) in measure \(dx\,dy/(xy)\) is \(O(bL)\), giving a bulk HS error \(O_\epsilon(b^{1/2}P X^{-1/2+\epsilon})\). At \(x<a_N\), the minor kernel is zero and the true kernel has \(|A_N(x,y)|\ll L^2(xy)^{3/2}\) by the exact arithmetic/model mass cap in R24. As \(a_N<1/4\) for large \(X\) in the stated range, a nonzero term forces \(y\ge3/4\). Squaring and applying \(\int_0^{a_N}dx/w_N(x)\ll a_N+1/N\ll a_N\) gives edge HS\(^2\) \(O(bL^4a_N)\). This same estimate applies with the variables reversed. Its square root has the same size as the bulk error, proving (1). In particular the reduction does not presume uniformly bounded Hardy coordinates at the actual endpoint zero.

## 3. A localized minor mean square before integrating the kernel

For fixed \(x\le y\) in \((0,b]\) and fixed thresholds \(s,t\) in the layer cake, include only those moduli for which \(x,y\ge a_N\). All collapsed intervals at those moduli, for every relevant alias, consist of raw integer points in \([1,(11X/5)x]\). In each dyadic level the disjoint blocks that occur are therefore supported within this common shorter prefix. Adapt the [R24 divisor-multiplicity calculation](r24-arithmetic-growing-compensation.md) without replacing the shorter prefix by \([1,Y]\): the sum of the squared \(L^2\) norms of those block prime sums on one level is at most

\[
 \sum_{n\le(11X/5)x}\Lambda(n)^2\ll Xx L.
\]

For each block, the number of pairs \((N,k)\) with the same nonzero frequency \(\pm kN\) is \(O_\epsilon(Y^\epsilon)\). By ordinary Fourier Parseval the total squared minor coefficient sum over all \((N,k)\) in each orientation is thus \(O_\epsilon(Y^\epsilon\sup_{\mathfrak m}|U|^2 Xx)\), absorbing dyadic-level and Cauchy–Schwarz logarithms. On these minor arcs the classical Vinogradov–Vaughan bound (e.g. [Ren, Corollary 1.2](https://hkumath.hku.hk/~imr/IMRPreprintSeries/2004/IMR2004-9.pdf)) gives \(\sup|U|\ll_\epsilon Y^{1+\epsilon}P^{-1/2}\), since \(Y^{4/5}\le YP^{-1/2}\) for \(P\le Y^{2/5}\). Where a line is possible \(y\ge1/2\); Cauchy–Schwarz across the at most \(O(y)\) aliases and dividing by \(N^2\asymp X^2\) give the uniform localized moment

\[
 \sum_N |D_N^{\mathfrak m}(s,x;t,y)|^2\ll_\epsilon xy\frac{Y^{2+\epsilon}}{XP}.
\]

For \(x+y<1\) the left side is zero. This is before integrating in \(s,t\), and requires no simultaneous choice of a favorable rectangle. By Minkowski in \(\ell_N^2\), integrating the positive layer-cake weights adds a factor \(\sqrt{xy}\) to the square root of this bound; squaring gives \(\sum_N|A_N^{\mathfrak m}(x,y)|^2\ll_\epsilon (xy)^2Y^{2+\epsilon}/(XP)\). The square of the exact log-kernel denominator cancels this \((xy)^2\) on the bulk, with bounded Hardy weights there. Integrate over the common log square from \(\min_N a_N\) to \(b\), of area \(O(L^2)\), and use symmetry. This proves (2).

Finally take \(P=Y^{2/5}\), for which the right side of (2) is \(O_\epsilon(b^{8/5}X^{3/5+\epsilon})\). For any chosen fixed \(\eta>0\), as long as \(\tau\ge X^{-13/400+\eta}\), the deterministic error (1) is \(o(\tau)\) (choose its internal \(\epsilon<\eta\)). Thus the actual prefix has at most \(O_{\eta,\epsilon}(\tau^{-2}b^{8/5} X^{3/5+\epsilon})\) exceptions. At the common \(b=(11X/5)^{3/40}\), the moment has exponent \(3/5+(8/5)(3/40)=18/25\). Compression from this common \(b\) to the individual \(b_N\) cannot increase HS. The two claimed exception exponents are \(18/25+1/200=29/40\) and \(18/25+1/50=37/50\). Conversely for an individual modulus, the reverse triangle inequality in (1) forces the minor operator's norm to be within its stated power error of the actual norm, in either the HS or the operator norm. That conclusion does not make a minor-arc Fourier cancellation claim at a singleton modulus.
