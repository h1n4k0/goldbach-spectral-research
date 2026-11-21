# Addendum: exact Type II removal by a character average in the cofactor leg

**Conditional arithmetic result (global Dirichlet GRH).** Keep the notation and exact central Type II geometry of the [unconditional left strip](weak-s-type-ii-left-strip.md). Thus \(N\) is even, \(L=\log N\), \(U_1=N^{.265}\), \(V=N^{.2499}\), \(N^{.49999}\le t\le N^{.50001}\), \(N/2\le y\le9N/16\), and \(b_{\rm II}(v)=\sum_{r\mid v,r>V}\Lambda(r)\). In the genuine correlation

\[
 \sum_{\substack{uv+dk=N,\,N/2<uv\le y,\,(uv,N)=1\\
          u>U_1,\,v>V,\,k>t}}\mu(u)\mu(d)b_{\rm II}(v)\mu^2(dk)
\]

retain the **exact mask** \(d\le D,\ dv\le E\), with real \(1\le D,E\le N^2\). One may additionally retain only \(d\sqrt v>H_0\) at any fixed real \(H_0\ge0\), if a sharper, one-sided mask is desired. Its contribution is bounded by

\[
 O_{A,\epsilon}\!\left(NL^{-A}+ N^{1/2+\epsilon}(D+\sqrt E)\right) \tag{1}
\]

for every fixed \(A,\epsilon>0\), uniformly in the original sharp cutoffs, both mask endpoints and \(H_0\). In particular take \(D=N^{199/400}=N^{.4975}\), \(E=N^{199/200}=N^{.995}\). This deletes the entire specified component to every fixed inverse-logarithmic scale, leaving only those still-present terms with \(d>N^{.4975}\) **or** \(dv>N^{.995}\). For comparison, the simpler mask \(d\sqrt v\le N^{.4975}\) is contained in these cuts (since \(v\le N^{.735}\)), and the extension is nonempty, as verified below. Both signs, the exact unit condition and \(\mu^2(dk)\) are kept. The global rather than local GRH is needed for the auxiliary characters. No pointwise conclusion on balanced remaining terms, a reflected cutoff, or weak S is claimed.

## 1. Truncate the squarefree completion and preserve the hard geometry

Put \(n=uv\), \(m=N-n\). As in the left-strip proof, use \(\mu^2(m)=\sum_{b^2\mid m}\mu(b)\), retaining \(b\le B=L^J\). Its error is \(O(NL^C B^{-1/2})\): Hölder with exponents \(4,4,2\) bounds the sum of \(L\tau(n)\tau(m)^2\) over the \(O(N/B)\) values of \(m\) admitting an omitted square divisor, using the usual fourth and eighth divisor moments. Any exact pair mask can only decrease this absolute bound. Choose \(J\) in terms of \(A\). On retaining \(b\), fix \(d,b\) and a dyad \(W\le v<2W\). The original mask and optional cut are now one-variable restrictions on \(v\), along with \(v>V\), \((v,N)=1\). The cutoff \(d\le D\) is already imposed. We may restrict \(N/(4W)\le u\le N/W\) and \(u>U_1,(u,N)=1\): all originally eligible products lie between \(N/2\) and \(9N/16\). The rectangular ranges before the hard product test then have \(uv\asymp N\) uniformly.

Writing \(q=[d,b^2]\), the requirements \(d\mid m\) and \(b^2\mid m\) become the exact product congruence \(uv\equiv N\pmod q\). Discard \((q,N)>1\), which is impossible for a unit \(uv\). For the remaining \(q\), character orthogonality for this reduced target applies equally to a nonunit candidate product (both sides are zero). The resulting characters are all Dirichlet characters modulo \(q\), with the separate masks \((u,N)=(v,N)=1\) still imposed. The exact remaining product condition is \(N/2<uv\le y\) and \(uv<N-td\). With \(d\) fixed, use the half-integer endpoints

\[
 A_0=N/2+1/2,\qquad A_1=\min\{\lfloor y\rfloor+1/2,\ \lceil N-td\rceil-1/2\}.
\]

Selecting \(A_0<uv<A_1\) gives exactly the original integer choices, including if \(N-td\) is integral. If \(A_1\le A_0\) the interval is empty. Otherwise both endpoints are \(\asymp N\), and every integer product differs from each by at least \(1/2\). No independently varying cutoff on the character factors of the product predicate is being assumed.

## 2. Exact Perron separation and an all-character mean square

Use truncated Perron for each endpoint on the line \(\Re s=1\) at height \(T=N^4\). For \(uv\asymp N\) and half-integer \(A_i\asymp N\), the pointwise error for the indicator is \(O(N^{-3})\), since \(|\log(A_i/(uv))|\gg N^{-1}\). There are \(O(N)\) tuple candidates per \((d,b,W)\) and \(b_{\rm II}(v)\le L\), hence all these errors are negligible even after summing \(d,b\) and dyads. The character average is normalized by \(1/\varphi(q)\), so it gives no extra loss for this error. On the integration line the product separates into the two Dirichlet polynomials on the actual one-variable supports, multiplied by \(A_i^{1+i\tau}/(1+i\tau)\).

The first factor has the uniform bound

\[
 \left|\sum_{u\in I,\ (u,N)=1}\mu(u)\chi(u)u^{-1-i\tau}\right|
 \ll_\epsilon N^\epsilon (N/W)^{-1/2}, \qquad |\tau|\le N^4, \tag{2}
\]

for the indicated \(u\) interval \(I\) at scale \(N/W\), all characters modulo \(q\), and \(q\le dB^2\le N^{O(1)}\). To verify the height-uniform version, apply the same reciprocal bound as in [R21 §1](r21-arithmetic-high-e.md) to the Dirichlet series of \(\mu(u)\chi(u)\mathbf1_{(u,N)=1}u^{-i\tau}\). It is

\[
 L(s+i\tau,\chi)^{-1}\prod_{p\mid N}(1-\chi(p)p^{-s-i\tau})^{-1}.
\]

On \(\Re s\ge1/2+\delta\) this is \(O_{\delta,\epsilon}((qN(|\Im s+\tau|+2))^\epsilon)\) by global Dirichlet GRH. The same bound applies to imprimitive characters, whose finite missing Euler factors have absolute cost \(O(q^\epsilon)\); for a principal character the reciprocal of the zeta pole is a zero. Truncated Perron at a half-integer endpoint \(Y\le N\), on \(\Re s=2\) with height \((Y+2)^3\), shifts without any pole to \(\Re s=1/2+\delta\). The coefficients have modulus at most one; the starting-line error is \(O(Y^2/(Y+2)^3)\) up to harmless logarithms, and the horizontal segments are at most this times \(N^{O(\epsilon)}\). Throughout, \(|\Im s+\tau|\ll N^4\), so the new side gives \(O(N^{O(\epsilon)}Y^{1/2+\delta})\). Choose \(\delta\) and the auxiliary \(\epsilon\) small and take interval differences, then partial summation for \(u^{-1}\) on scale \(N/W\), proving (2). This avoids a spurious polynomial loss from attempting to add the twist by direct partial summation in \(\tau\).

For the second factor orthogonality over **all** characters gives, for each \(\tau\),

\[
 \frac1{\varphi(q)}\sum_{\chi\bmod q}
 \left|\sum_{v\in J} b_{\rm II}(v)\chi(v)v^{-1-i\tau}\right|^2
 \ll \frac{L^2}{W}\left(1+\frac{W}{q}\right). \tag{3}
\]

Here \(J\) is the actual v-support for fixed \(b,d,W\), including all masks specified above. Indeed orthogonality gives only unit pairs of equal residue, at most \(O(W(1+W/q))\) even on the full dyad, and each product of coefficient magnitudes is at most \(L^2/W^2\). Thus this estimate does not need cancellation in \(b_{\rm II}\), nor any averaging of \(q\) or \(N\). Use Cauchy in the normalized character average for this factor and (2) for the other. The Perron factor contributes at most \(O(NL)\) in absolute integral weight. Consequently the signed raw contribution for fixed \(d,b,W\) is

\[
 \ll_\epsilon N^{1/2+\epsilon}\sqrt{1+W/q}
 \le N^{1/2+\epsilon}\sqrt{1+W/d},
\]

up to the negligible endpoint error. The factors \(\mu(b),\mu(d)\) are retained (bounding their magnitudes in this final estimate); the cancellation used here is in the actual \(\mu(u)\) twists.

## 3. Sum the actual adaptive cut and verify its reach

For this dyad all eligible \(d\) satisfy \(d\le D_W=\min(D,E/W)\), though the exact restriction \(dv\le E\) was kept inside (3). If \(D_W<1\) there is no term, and otherwise

\[
 \sum_{1\le d\le D_W}\sqrt{1+W/d}\ll D_W+\sqrt{WD_W}\le D+\sqrt E.
\]

Sum over \(O(L)\) dyads and \(b\le B\), absorb logarithms and add the squarefree tail. This proves (1). In the specified example \(D\) and \(\sqrt E\) both equal \(N^{.4975}\), leaving a positive power saving in the second term.

For a nonempty witness outside the narrower \(d\sqrt v\)-mask, take independent \(X\to\infty\) and choose distinct odd primes \(u,v,d,k\) in fixed sufficiently short relative intervals at \(X^{.70}, .53X^{.30}, X^{.42}, .47X^{.58}\), respectively. Then \(N=uv+dk\asymp X\) is even with unit summands, \(uv/N\) close to \(.53\) strictly inside the true interval, and \(k>N^{.50001}\). The actual coefficient is \(\log v>0\) since \(u,d\) are primes, \(dk\) is squarefree, and \(v>V\) is prime. But \(d\sqrt v\asymp N^{.57}>N^{.4975}\), while \(d\le N^{.4975}\) and \(dv\asymp N^{.72}<N^{.995}\). This proves a strict nonempty mask extension, not a noncancellation claim about an aggregate. At the remaining boundary \(d\asymp\sqrt N\) the character estimate used here retains an unsaved \(\sqrt N\) per modulus; this argument does not reach that central endpoint at weak-S scale.
