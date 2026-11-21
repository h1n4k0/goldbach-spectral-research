# R21: Pointwise control of the lower asymmetric part of the genuine mixed remainder

**Theorem (global Dirichlet GRH).** Use the R20 one-good-leg survivor with \(b=N^{3/40},Q=N^{7/8},D=\lfloor\lceil 4bN\rceil^{1/3}\rfloor\). Thus \(n\) has at least two of the indicated small prime factors, \(m\) has at most one, \(L=L(n)\) is the product of the two indicated smallest primes on the good leg, and the actual long divisors obey
\[
 D<d\le D(\log N)^2,\qquad d/(d,L)\le D,\qquad [d/(d,L)]e>Q.
\]
Retain exactly the terms with \(e\le N^{3/5}\). In the full physical prefix \(b=N^{3/40}\), including every hard rectangle and each sign/orientation of the nonzero aliases, the resulting raw line count is \(O_\epsilon(N^{551/600+\epsilon})\). Its actual arithmetic Hardy operator has
\[
\|C_{\mathrm{mix},\le N^{3/5}}\|_{\mathrm{HS}}\ll_\epsilon N^{-1/300+\epsilon}.
\]
The reflected statement also holds. This includes a true product range beyond ordinary term-by-term CRT (e.g. \(de\asymp N^{23/24}\)), and works at the larger R17 prefix where the R19 balanced estimate does not. This does not cover the higher mixed gaps, the rough–rough term, or the exterior. No conclusion on S or R.

## 1. The GRH reciprocal additive input, with hard windows

Write \(e(x)=\exp(2\pi i x)\). Let \(q,F\) and \(|\lambda|\) be polynomial in \(N\); let \(I\) be any hard interval inside \(c\asymp C\), \(C\ge 1/2\) polynomial in \(N\). For \(f=\mu\) or \(f=\mu^2\), any character \(\chi\bmod q\), and either logarithmic marker \((\log c)^i,\ i=0,1\), consider
\[
 \sum_{\substack{c\in I\\(c,F)=1}} f(c)\chi(c)(\log c)^i e(\lambda/c).
\]
Under global GRH this is
\[
 M_\chi + O_\epsilon\big(N^\epsilon C^{1/2}(1+|\lambda|/C)^{1/2}\big),       \tag{1}
\]
where \(M_\chi=0\) unless \(f=\mu^2\) and \(\chi\) is principal; in that case \(|M_\chi|\ll_\epsilon N^\epsilon C\). The following proof records the uniformity for a moving endpoint, which an unweighted progression estimate alone would not furnish.

For \(\sigma>1\) the two Dirichlet series without the logarithmic marker are
\[
 L(s,\chi)^{-1}\prod_{p\mid F}(1-\chi(p)p^{-s})^{-1},\qquad
 \frac{L(s,\chi)}{L(2s,\chi^2)}
       \prod_{p\mid F}(1+\chi(p)p^{-s})^{-1}.
\]
The excluded factors on \(\sigma\ge1/2+\eta\), for fixed \(\eta>0\), contribute \(N^\epsilon\): uniformly for polynomially bounded integer \(B\), \(\prod_{p\mid B}(1-p^{-(1/2+\eta)})^{-1}\ll_{\epsilon,\eta}B^\epsilon\), by treating a finite initial set of primes separately. The denominator \(L(2s,\chi^2)\) is bounded away from zero on that strip by absolute convergence. The standard GRH subpower bound for \(L\) and \(1/L\) at fixed distance to the right of \(1/2\) follows from the Littlewood argument (compare [Simonič, Theorem 1 and Example 2](https://doi.org/10.1007/s00009-023-02289-2)); here are the details to ensure the conductor is uniform. For a primitive nonprincipal \(L\), use its zero-free analytic log in \(\sigma>1/2\); for \(\zeta\), first multiply by \((s-1)/(s+1)\) to remove its pole. Polynomial bounds on fixed strips follow by summation by parts (periodic character partial sums are \(O(q)\); for \(\zeta\) subtract the continuous counting term). Borel–Carathéodory on a disk centered at \(2+it\) with larger radius \(3/2-\eta/4\) and smaller \(3/2-\eta/2\) gives \(|\log L|\ll_\eta\log(q(2+|t|))\) at \(\sigma=1/2+\eta/2\), because the log at \(2+it\) is bounded. On \(1+\eta/2\) the log is bounded uniformly by the Euler product. Apply three-lines to this analytic log multiplied by \(\exp((s-it)^2)\) for each fixed target \(t\). On the left the Gaussian bounds the supremum by \(O_\eta(\log(q(2+|t|)))\), on the right by \(O_\eta(1)\). Hence the log on \(\sigma=1/2+\eta\), for \(0<\eta<1/4\), is \(O_\eta(\log^{1-\eta}(q(2+|t|)))\). Restoring primitive-to-imprimitive Euler factors costs another subpower. This proves the needed \((q(2+|t|))^\epsilon\) bounds on the integration line, and for contour movement at large height. The only pole crossed is at \(s=1\) in the squarefree principal case, with residue at most \(1\).

To apply Mellin, put the endpoints at half-integers and smooth the indicator within transitions of fixed width \(<1/2\) so its values on all integers are exact. In \(u=\log(c/C)\), the Mellin transform on a fixed line is \(C^{\sigma+it}\) times the Fourier-type transform of a supported bounded-variation smooth amplitude (up to \(\log N\)) times \(e((\lambda/C)e^{-u})\). The amplitude's total variation is \(O((\log N)^i)\), and derivatives of every fixed order have polynomial bounds, uniformly in the chosen interval. A nonempty interval can always be taken with width at least one between its half-integer endpoints; empty integer intervals need not be estimated. On \(|t|\lesssim 1+|\lambda|/C\), use Plancherel and Cauchy–Schwarz to bound the transform's \(L^1\) mass by \(O((\log N)^i\sqrt{1+|\lambda|/C})\). For larger \(t\), nonstationary integration by parts gives \(O((\log N)^i/|t|)\): derivative of total phase has size \(\gg |t|\), its second derivative is \(O(|\lambda|/C)\), and the amplitude has bounded variation. Integrate this up to a fixed sufficiently large power of \(N\); beyond it use twice integration by parts with the crude polynomial derivative bounds, absorbing the allowed subpower growth of \(L\). Mellin inversion and shifting to \(1/2+\eta\) prove (1), with \(C^\eta\) and logarithms absorbed by choosing small auxiliary exponents. The pole contribution is its residue times \(\int W(c)(\log c)^i e(\lambda/c)\,dc\), so the stated absolute bound is uniform including non-stationary endpoints.

If \(q\ge1\) and \(\bar c\) denotes inverse among its units, expand \(e(J\bar c/q)\) into multiplicative characters of the unit group. Its coefficients have square-sum 1, hence absolute sum at most \(\sqrt{\varphi(q)}\); its principal coefficient is the Ramanujan sum \(c_q(J)/\varphi(q)\). It follows from (1) that the same sum with \(\chi(c)\) replaced by the reciprocal phase, and with \((c,qF)=1\), has error
\[
 O_\epsilon\big(N^\epsilon\sqrt{q C}\sqrt{1+|\lambda|/C}\big).           \tag{2}
\]
For \(f=\mu^2\) the separate principal term is \(O_\epsilon(N^\epsilon C |c_q(J)|/\varphi(q))\). Character orthogonality in (2) is at an **auxiliary** modulus; local GRH(N) alone does not suffice.

## 2. Apply to exact R20 masks and each hard line

Let \(X=\lceil4bN\rceil\), \(W=\prod_{p\le\log N,\ p\nmid N}p\). Fix \(h=jN\), one line, and any hard rectangle, giving one raw interval in \(n\). Expand the least-two selection of \(L\) and the rough selection as in R20 into conditions \(P\mid n,R\mid m\), \(P,R\mid W\), with \(N^{o(1)}\) total coefficient mass and \(L\) fixed for each term. If \(\max(P,R)>N^{4/25}\), bound each such term in absolute value by \(O_\epsilon(N^\epsilon(XN^{-4/25}+1))\): that line is parametrized injectively by either raw coordinate, the large divisibility reduces the number of raw integers, and each integer pair's divisor coefficient is \(O_\epsilon(N^\epsilon)\) even with all markers. There is no continuous model to discard for these masks.

For the remaining masks consider divisor boxes \(d\asymp U,e\asymp V\). We have
\[
  U\ll_\epsilon N^{43/120+\epsilon},\qquad
  N^{31/60}\ll V\ll N^{3/5}.
\]
Split \(d=u d_0,e=v e_0\), with \(u,v\mid W\), \((d_0e_0,W)=1\). Only unit \(d,e\) and nonzero Möbius weights matter. Put
\[
 A=[u,P],\quad B=[v,R],\quad G=(A,B),\quad A'=A/G,\ B'=B/G,
 \qquad d_0=g a,\quad e_0=g c,\quad g=(d_0,e_0).
\]
The dyadic lengths of \(a,c\) are \(A_0\asymp U/(ug)\), \(C\asymp V/(vg)\), with scale at least \(1/2\) for nonempty dyads. Their coprimalities are \((a,c)=1,(ac,gNW)=1\), and the line is compatible if and only if \(Gg\mid h\). These conditions factor because \(g,a,c\) are coprime to \(W\), and hence to \(A',B'\). The exact survivor constraint \(d/(d,L)\le D\) restricts only \(a\) for fixed factors. The condition \([d/(d,L)]e>Q\) makes the permitted \(c\)-window a **single** interval once \(a\) is fixed; it can be intersected with its dyad and the hard cap \(e\le N^{3/5}\). No separability of that lower endpoint is assumed.

Unit inclusion–exclusion uses \(r\mid N\), \(r\mid n\), since \(m\equiv\pm n\pmod N\). For \(\widetilde h=\pm h\) appropriate to the line, the \(n\)-progression is \(n=rGg A'a t\) with
\[
 t\equiv \frac{\widetilde h}{rGg}\,\overline{A'a}\pmod{B'c}.
\]
The compatibility guarantees \(rGg\mid h\), since \(Gg\) is coprime to \(N\). Denote a raw interval endpoint (half-integer as in R19) by \(E\). Use [Vaaler, Theorem 18](https://doi.org/10.1090/S0273-0979-1985-15349-2) precisely as in R19, with \(H=\lfloor N^{1/25}\rfloor\). For signed nonzero frequency \(\nu\), the sawtooth argument or its negative gives, after reciprocal reciprocity,
\[
 e\!\left(-\frac{\nu\widetilde h}{rGg}
                 \frac{\overline{B'c}}{A'a}
           +\frac{\nu(\widetilde h-E)}{rGg A'B'a c}\right).             \tag{3}
\]
Changing the common sign of this formula has no effect on its estimates. This identity uses \(\overline x/y+\overline y/x\equiv1/(xy)\pmod 1\) for coprime \(x,y\); it retains the entire endpoint phase. It takes modulus \(q=A'a\), which lies on the small divisor leg, not \(B'c\) on the large leg.

At fixed \(a\), write \(\overline{B'c}=\overline{B'}\bar c\bmod q\), and apply (2) with \(F=gNW\),
\[
 J=-\frac{\nu\widetilde h}{rGg}\overline{B'},\qquad
 \lambda=\frac{\nu(\widetilde h-E)}{rGg A'B'a}.
\]
Logarithmic factors \(\log c\) cause only the already allowed log marker. The signed polynomial uses \(f(c)=\mu(c)\), while its pointwise positive Fejér error uses \(f(c)=|\mu(c)|=\mu^2(c)\). Also take absolute values of the fixed weight on the small \(a\)-leg for the error. The zero frequency of the Fejér majorant costs \(O_\epsilon(N^\epsilon UV/H)\) since there are \(O(UV/(uvg^2))\) divisor pairs at fixed factors. For a nonzero frequency the total error from (2), summed over \(a\), is at most
\[
 N^\epsilon\left[U\sqrt{UVP}+U\sqrt{|\nu|X}\right].
\]
Indeed \(A'\le uP\); the untwisted part costs \((U/(ug))\sqrt{A'UV/(uvg^2)}\le U\sqrt{UVP}\). The phase part costs \((U/(ug))\sqrt{|\nu|X/(rGgB')}\le U\sqrt{|\nu|X}\), since \(q\) cancels the denominator \(A'a\) in \(|\lambda|\). This cancellation is why the large divisor \(P\) does not compound the phase loss. Sum the Vaaler coefficients \(O(1/|\nu|)\) and the nonzero Fejér coefficients \(O(1/H)\), using \(|\nu|\le H\), for at most logarithmic additional loss.

The Fejér principal part is also small. The factors \((a,A')=1\) give
\[
 \frac{|c_q(J)|}{\varphi(q)}
 \ll_\epsilon N^\epsilon\,\frac{(a,\nu h)}a ,
\]
using \(|c_q(J)|\le(q,J)\), the inverse of \(B'\) being a unit. This holds also for \(q=1\). For a dyad in \(a\), \(\sum_{a\asymp A_0}(a,\nu h)/a\ll\tau(|\nu h|)\) by summing over divisors of \(\nu h\); each divisor at most a constant times \(A_0\) contributes \(O(1)\). The principal contribution after summing \(a\) therefore costs only \(O_\epsilon(N^\epsilon C)\), bounded by \(O_\epsilon(N^\epsilon V)\), uniformly in each frequency. It must not be treated as a zero-main-term Möbius estimate.

## 3. Density, exponents, and Hardy transfer

Expanding \(\log(n/d)\log(m/e)\) separates the divisor log markers from \(\log n,\log m\); restore the latter via bounded-variation partial summation in the raw interval, as in R19. The zero term of the **exact signed** sawtooth calculation restores the CRT density \((\varphi(N)/N)/[d,e,P,R]\), with the compatibility condition above. Its density contribution after summing the true signed weights is \(O_\epsilon(X V^{-1/2}N^\epsilon)\). For completeness, group by the same \(u,v,g\). At fixed \(a\), the model denominator is \([u,v,P,R]\,g a c\), and the \(c\)-variables range over one interval in the dyad \(C\asymp V/(vg)\). The coprime RH Mertens tail with log marker saves \(C^{-1/2+\epsilon}\); summed with the other harmonic leg, \([u,v,P,R]\ge v\) absorbs \(v^{1/2}\), while summing \(g\mid h\) with \(g^{-1/2}\) costs \(N^\epsilon\). This works equally for \(C\asymp1\). All splittings into \(u,v,P,R\) have \(N^{o(1)}\) total absolute mass; \(r\mid N,\ Gg\mid h\) cost \(N^\epsilon\). Moving the raw endpoint back from half-integers changes the density by only \(O_\epsilon(N^\epsilon)\), from its \(1/[d,e,P,R]\) summability.

The total bound for a raw line, including the discarded large masks, is consequently at most \(N^\epsilon\) times
\[
  1+XN^{-4/25}+\frac{UV}{H}
    +U\sqrt{UV\,N^{4/25}}+U\sqrt{HX}+V+X V^{-1/2}.
\]
The nonconstant exponent bounds, in order, are \(183/200,\ 551/600,\ 367/400,\ 1099/1200,\ 3/5,\ 49/60\); the last uses the lower endpoint \(V\gg N^{31/60}\). Thus the maximum is \(551/600=37/40-1/150\), strictly below the full-prefix requirement \(37/40\). Sum the \(O(b)\) lines after normalizing by \(1/N\), obtaining a rectangle discrepancy \(O_\epsilon(N^{-1/150+\epsilon})\). With the cumulative \(\sqrt{uv}\) weight, layer cake gives \(O_\epsilon(N^{-1/150+\epsilon}\sqrt{xy})\); the independent per-atom divisor bound and nonzero line geometry give \(O_\epsilon(N^\epsilon(xy)^{3/2})\). Multiplying these bounds in the squared physical log kernel and integrating on \(x,y\ge1/N\) as in R18/R19 proves the claimed HS estimate. At either edge \(<1/N\) there are no atoms, hence no contribution. The sector controlled retains the genuine mixed masks and original line signs; no Beta density was subtracted from the operator.
