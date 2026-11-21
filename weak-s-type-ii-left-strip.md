# Pointwise removal of a left strip of the actual central Vaughan Type II sum

**Unconditional arithmetic result.** Fix a sufficiently large even integer \(N\), let \(L=\log N\), and use the exact central increment and Vaughan split in the [Vaughan Type I reduction](spectral-vaughan-central-type-i.md). Take

\[
 N^{49999/100000}\le t\le N^{50001/100000},\qquad
 N/2\le y\le9N/16,\qquad
 U=V=N^{2499/10000},\qquad U_1=N^{53/200}.
\]

Put \(b_{\rm II}(v)=\sum_{r\mid v,\,r>V}\Lambda(r)\), and retain the **actual** left strip

\[
 \mathcal L(t,y)=
 \sum_{\substack{uv+dk=N,\,N/2<uv\le y,\,(uv,N)=1\\
                  U<u\le U_1,\,v>V,\,k>t}}
      \mu(u)\mu(d)b_{\rm II}(v)\mu^2(dk).
\]

For every \(A>0\), uniformly in both sharp cutoffs \(t,y\),

\[
 |\mathcal L(t,y)|\ll_A NL^{-A}. \tag{1}
\]

Thus the genuine remaining Type II term in this near-square-root band can be restricted to \(u>N^{.265}\), with its existing \(v>N^{.2499}\) condition. This is a gain for the full strip, with all its actual \(d,k\) and their signs, not a bound after selecting comparable cofactors or changing the signed rectangle. Raising the earlier Type I parameter to \(U_1\) at this fixed \(V\) would exceed its elementary threshold \(UV<N^{.49999}\) (here \(U_1V=N^{.5149}\)). This proof instead uses perturbed trilinear dispersion across the resulting divisor product beyond \(N\). There is no reflection to the \(v\) side, no bound past this left strip, and no conclusion on weak S or Goldbach. No RH or averaging in \(N\) is used for (1).

## 1. Exact square completion and re-expansion of the genuine weight

Write \(n=uv\), \(m=N-n=dk\). Then \((n,N)=1\) is equivalent to \((m,N)=1\), and for each choice of \(d\mid m\), \(k>t\) is the exact condition \(d<m/t\). Use \(\mu^2(m)=\sum_{b^2\mid m}\mu(b)\), truncating at \(b\le B=L^J\). This costs \(O(NL^{C}B^{-1/2})\) for an absolute fixed \(C\), as in the Type I proof: before completion the left strip coefficient has magnitude \(\le L\tau(n)\) and the inner \(d\)-sum at most \(\tau(m)\); the omitted completion contributes another \(\tau(m)\), supported on a set of \(O(N/B)\) integers. Hölder at exponents \(4,4,2\) and the standard fourth and eighth divisor-function moments give this stated bound. Choose \(J\) large in terms of \(A\). This tail is taken before any expansion below.

Use the exact identity

\[
 b_{\rm II}(v)=\log v-\sum_{r\mid v,\,r\le V}\Lambda(r).
\]

All data are retained, including prime powers \(r\), and the condition \(v>V\) is automatic here since \(n>N/2,u\le N^{.265}\). The first piece gives divisors \(a=u\le U_1\) of \(n\), weight \(\mu(a)\log(n/a)\) restricted to \(a>U\). The second collapses to one coefficient at each \(a=ur\le U_1V=N^{.5149}\):

\[
 \alpha(a)=\sum_{ur=a,\,U<u\le U_1,\,r\le V}\mu(u)\Lambda(r),\qquad
 |\alpha(a)|\le\sum_{r\mid a}\Lambda(r)=\log a.
\]

There is no further cutoff on \(r\) or \(u\) left as a joint constraint on \(a,d\); this is why the numerator's coefficient in the dispersion estimate will be separated.

## 2. Exact lattice error, including the slanted strict endpoint

Fix \(b\) and write \(d'=[b^2,d]\), the combined modulus on \(m\). Only \(b,d\) squarefree contribute. We can discard \((ab d,N)>1\) by the unit condition, and discard \((a,d')>1\) since any common factor would divide \(m,n\) and hence \(N\). Include the remaining unit condition by summing \(\mu(r_0)\mathbf1_{r_0\mid n}\) over **all** \(r_0\mid N\). In \(n=r_0 a j\) the congruence is

\[
 j\equiv (N/r_0)\overline a\pmod {d'}.
\]

The raw interval for \(n\) has lower endpoint \(E_0=N/2+1/2\) and upper endpoint the lesser of \(E_1=\lfloor y\rfloor+1/2\) and \(N-t'd\), where \(t'=\lfloor t\rfloor+1/2\). These substitutions preserve the **integer** count: \(k>t\) is equivalent to \(k>t'\). The moving endpoint is never a progression point, as equality would give the noninteger \(k=t'\). The fixed endpoints are half-integers and are also never progression points. If the upper endpoint is at most the lower one use the empty interval. Split the support of \(d\) at the two thresholds where the moving upper endpoint crosses \(E_0,E_1\); each piece selects a separated interval on \(d\). For each selected \(d\), the density term is exactly its continuous length divided by \(r_0 a d'\). Summing densities over \(r_0\mid N\) gives unit density \((\varphi(N)/N)/(a d')\) in the real interval with these chosen endpoints. There is no need to replace it by a different real interval with \(t\) or \(y\) unrounded.

For the log piece, direct CRT costs \(O(L\tau(N))\) per \((b,a,d)\), including partial summation for \(\log(n/a)\); since \(a\le N^{.265},\ d\ll N^{.50001}\), this is \(O(N^{.76501+o(1)})\). For the \(\alpha(a)\) piece, fix \(g=(b,d)\). Then \(d'=b^2d/g\) is injective in \(d\) on this separated group, and \(d'\ll N^{.50001}B^2\). The coefficient \(\mu(d)\) (and this group restriction) becomes a bounded separated coefficient in \(d'\). Work in dyadic intervals of scales \(C,D\) on \(a,d'\). If \(CD\le N^{.999}\), the direct CRT floor cost after summing all coefficients, dyads, \(b,g,r_0\), is \(O(N^{.999+o(1)})\).

For \(CD>N^{.999}\), the discrepancy from the density is a difference of sawtooth terms at the endpoints. Use [Vaaler's Theorem 18](https://doi.org/10.1090/S0273-0979-1985-15349-2) with degree \(H=\lfloor N^{.016}\rfloor\). The zero Fourier mode of the nonnegative Fejér error majorant contributes \(O(N^{o(1)}CD/H)\). In a nonzero signed frequency dyad \(|\nu|\asymp K\le H\), either the approximation or the majorant has coefficient \(\ell^2\) norm \(O(K^{-1/2})\). For the approximation use the \(O(1/|\nu|)\) coefficients; for the majorant use \(O(1/H)\) and \(K\le H\). Apply the majorant with absolute values of the two arithmetic coefficients when estimating the approximation error.

For the other modes the actual phase is, up to a global frequency sign,

\[
 e\!\left(\nu (N/r_0)\overline a/d' - \nu E(d')/(r_0 a d')\right).
\]

Here \(E(d')\) is one of the two constants \(E_0,E_1\), or is \(N-t'(g/b^2)d'\) on the slanted endpoint piece. The latter perturbation is a sum of the smooth terms \(-\nu N/(r_0 a d')\) and \(\nu t'g/(r_0 b^2 a)\). On each actual dyad \(t'(g/b^2)d'\ll N\), including the full dyadic interval by a factor of at most two. Its derivatives are therefore \(O(KN/(r_0 a^2d'))\) and \(O(KN/(r_0 a(d')^2))\); the constant endpoint has the same bounds. They meet [Bettin–Chandee, Theorem 1 and Remark 1, (1.2)–(1.3)](https://arxiv.org/pdf/1502.00769#page=2), extending smoothly off the positive dyads if desired. There is no coupled cutoff inserted into an arithmetic coefficient. The unit divisor \(r_0\) decreases the phase parameter. The size multiplier from the theorem is at most \(O(N^{.0005}K^{1/2})\), using \(CD>N^{.999}\) and \(K\ge1\). The two arithmetic coefficient norms are \(O(L(CD)^{1/2})\) in product. The dyadic estimate from the two terms of that theorem and from the zero Fejér mode is thus, after summing frequencies and absorbing all log and divisor factors into \(N^{o(1)}\),

\[
 O\!\left(N^{o(1)}\left[
 CD/H + N^{.0005}H^{7/20}(CD)^{17/20}(C+D)^{1/4}
       + N^{.0005}H^{1/2}(CD)^{7/8}(C+D)^{1/8}\right]\right).
\]

Indeed the \(K^{1/2}\) multiplier cancels the frequency coefficient norm, and the second term of the source bound carries \((K(C+D))^{1/8}\) as well as \((KCD)^{3/8}\). With \(CD\le N^{1.01491+o(1)}\), \(C+D\le N^{.5149+o(1)}\), the exponents are at most \(.99891,.9974985,.96090875\), respectively. Consequently the uniform floor discrepancy for this whole piece is \(O(N^{.999+o(1)})\), giving more than any fixed logarithmic saving. The exponent includes the potentially large set of divisors \(r_0\mid N\) in the \(N^{o(1)}\) term; none was thrown out.

## 3. Cancel the *combined* actual density

Recombine all dyads, endpoint pieces and \(g\) for their density terms (those partitions were needed only for the floor discrepancy). At a real \(x\in(E_0,E_1)\), a nonempty contribution now requires exactly \(d<Y_x=(N-x)/t'\). This retains a single full upper-prefix constraint, with \(Y_x\gg N^{.49999}\) uniformly. The finite \(b\)-sum and the signed density for either separated left coefficient are then reduced to the inner factor

\[
 \sum_{\substack{d<Y_x\\(d,aN)=1}}\frac{\mu(d)}{[b^2,d]}
 =b^{-2}\sum_{c\mid b,\,(c,aN)=1}\mu(c)
       \sum_{\substack{j<Y_x/c\\(j,abN)=1}}\frac{\mu(j)}j .
\]

The equality uses \(c=(b,d)\) and squarefree \(b,d\), with the shared factor \(c\) canceling. No bounds on the signed means of \(\alpha(a)\) are needed. Use the unconditional coprime Mertens bound from the Type I note: \(\sum_{j<Y,(j,W)=1}\mu(j)/j=O_{A'}(L^{-A'})\) uniformly for polynomial-sized \(W\le N^2\) and \(Y\) between a fixed positive power of \(N\) and \(N\). To recall the proof, the reciprocal zeta series is multiplied by the Euler factors at \(p\mid W\); their absolute coefficient mass at \(s=-1/4\) is at most \(\exp(O(L^{1/4}))\). Convolve, split at coefficient index \(\sqrt Y\), and use the ordinary zero-free-region reciprocal zeta bound for the shorter-index portion and the weighted coefficient tail for the other. In this application \(W=abN\le N^2\) and \(Y_x/c\gg N^{.49999}/L^J\). Summing over \(b\) costs \(\sum_b\tau(b)/b^2\ll1\), and the outer left weights including the factor \(1/a\) cost \(O(L^2)\) for either piece (for the log piece use \(\log(x/a)\le O(L)\)). The density integration length is at most \(N\). Taking \(A'\) large proves (1) together with the tail and floor bounds.

Only the switched progression part is displayed in \(\mathcal L\); the original Vaughan baseline has already been bounded separately in the companion note and there is no new continuous Goldbach model here. The result is uniform in the exact upper central prefixes (also in any fixed difference of two such prefixes), including nonintegral \(t,y\); it does not add a lower cutoff on \(d\), for which a separate density argument would be needed. The remaining range has \(u>N^{.265},v>N^{.2499}\) and both original signs. This file asserts no reflected cutoff for \(v\) and no control of that remaining correlation.
