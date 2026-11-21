# R23 follow-through: actual central compensation on a positive proportion of moduli

Assume **global Dirichlet GRH**. Use exactly the wide divisor labels of the [R22 central comparison](r22-compressed-wide-d.md): \(b_*=N^{3/40}\), \(D_*=\lfloor\lceil4b_*N\rceil^{1/3}\rfloor\), and \(Q=N^{7/8}\), unchanged when restricting to \(P_1\). Let \(C_N^{pp}\) be the pure rough–rough component in the [prime-cofactor proposition](r23-arithmetic-prime-cofactors.md), and let \(C_N^{\mathrm{rest}}=C_{\mathrm{rr}}^*-C_N^{pp}\) be its exact arithmetic complement in the R22 remainder. These operators carry all genuine signs, no added model. Fix the **same** nonnegative \(f\in C_c^\infty((2/5,3/5))\), \(f=1\) on \([9/20,11/20]\), and the **same** bounded test \(g_N(\log x)=-x^2\sqrt{w_N(x)}f'(x)\) of that proposition.

For every sufficiently large \(X\), on all but \(O_{f,\epsilon}(X^{4/5+\epsilon})\) even moduli in \([2X,11X/5]\),

\[
 |\langle T_N g_N,g_N\rangle|\ll_f X^{-1/40},\qquad
 \langle C_N^{\mathrm{rest}}g_N,g_N\rangle
   =-\langle C_N^{pp}g_N,g_N\rangle+O_{f,\epsilon}(X^{-1/120+\epsilon}).
 \tag{1}
\]

In particular, on \(\gg_f X\) even moduli in every such shell, with \(\mathfrak S(N)\ll1\), the negative form of the prime-cofactor piece is bounded away from zero, and the complementary rough–rough piece has a positive form equal to its magnitude up to that error. This verifies compensation on these moduli, without assuming S. It is a result about this one selected central form, not a statement about the norm of either complementary sector, the full compressed norm, or S/R.

## 1. Mean square with fixed raw intervals, among the ordinary even moduli

Let \(Y=4X\), \(P=Y^{1/4}\); for arbitrary fixed intervals \(I_1,I_2\subseteq[0,Y]\) put

\[
 \begin{split}
 E_N(I_1,I_2)={1\over N}\bigg[&\sum_{n+m=N}\Lambda(n)\Lambda(m)1_{I_1}(n)1_{I_2}(m)\\[-2pt]
 &-\mathfrak S(N)\int_{\mathbb R}1_{I_1}(t)1_{I_2}(N-t)\,dt\bigg].
 \end{split}
\]

The sum is initially not unit-restricted. Uniformly in the two intervals,

\[
 \sum_{\substack{2X\le N\le11X/5\\N\ \mathrm{even}}}|E_N(I_1,I_2)|^2\ll_{\epsilon} X^{3/4+\epsilon}.
 \tag{2}
\]

Here is the elementary circle-method input, including the dependence on the intervals. Write \(e(t)=e^{2\pi i t}\), \(S_j(\alpha)=\sum_{n\in I_j}\Lambda(n)e(n\alpha)\), \(V_j(\beta)=\int_{I_j}e(\beta t)dt\) and \(L=\log(2Y)\). Take disjoint major arcs \(\alpha=a/q+\beta\), \(q\le P\), \(|\beta|\le P/(qY)\) at reduced fractions modulo one. They are disjoint because \(2P^2<Y\). On the complement, Dirichlet approximation with denominator ceiling \(Y/P\) gives \(P<q\ll Y/P\) and \(|\alpha-a/q|\le q^{-2}\). The classical Vinogradov–Vaughan bound (for example also [Ren, Corollary 1.2](https://hkumath.hku.hk/~imr/IMRPreprintSeries/2004/IMR2004-9.pdf) with the divisor factors absorbed into \(Y^\epsilon\)) gives \(\sup_{\mathrm{minor}}|S_j|\ll_\epsilon Y^{7/8+\epsilon}\). Use dyadic intervals for prefixes, then differences for general \(I_j\): the three terms, before logarithmic or divisor losses, are \(Y/\sqrt q+Y^{4/5}+\sqrt{Yq}\ll Y^{7/8}\). Thus Parseval on the full integer sequence of Fourier coefficients gives

\[
 \sum_{N\in\mathbb Z}\left|\int_{\mathrm{minor}}S_1(\alpha)S_2(\alpha)e(-N\alpha)\,d\alpha\right|^2
 \le \sup_{\mathrm{minor}} |S_1|^2\int_{\mathbb R/\mathbb Z}|S_2|^2
 \ll_\epsilon Y^{11/4+\epsilon},
\]

using \(\sum_{n\le Y}\Lambda(n)^2\ll Y\log(2Y)\). This step is over *ordinary* moduli; no fourth moment for a sparse family is needed.

For major arcs use the individual-modulus estimate as in [R11](arithmetic-post-round10-exceptions.md):

\[
 S_j(a/q+\beta)=\frac{\mu(q)}{\varphi(q)}V_j(\beta)+O\!\left(\sqrt{Yq}\,L^2(1+Y|\beta|)\right).
\]

Indeed the [GRH character PNT, Lee Theorem 4.3](https://arxiv.org/pdf/2301.13457), gives prefix error \(O(\sqrt Y L^2)\) for each character modulo \(q\le P\), including the principal main term. For prefixes below \(\max(q,e^{10})\) the elementary bound suffices since \(q\le P\ll\sqrt Y\); \(q=1,2\) use the ordinary RH PNT, in the latter case omitting powers of 2. Finite character Parseval for \(e(ab/q)\) on the units gives Gauss-coefficient \(\ell^1\) cost at most \(\sqrt{\varphi(q)}\le\sqrt q\) after division by \(\varphi(q)\). Nonunit prime powers cost \(O(L^2)\), and Abel summation gives \(1+Y|\beta|\). Also \(|V_j(\beta)|\ll Y/(1+Y|\beta|)\) uniformly for intervals, including empty ones.

For each fixed \(N\), the integrated mixed terms summed over \(a\) at denominator \(q\) are \(O(\sqrt Y,P L^2/\sqrt q)\). For the product of both errors, after the substitution \(t=Y\beta\), the integral summed over \(a\) is \(O(\varphi(q)q L^4\int_{|t|\le P/q}(1+|t|)^2dt)=O(P^3L^4/q)\). Therefore the total major-arc error from these terms is \(O(\sqrt Y P^{3/2} L^2+P^3L^5)\).

The remaining principal terms have coefficient \(\mu^2(q)c_q(N)/\varphi(q)^2\). Uniformly for \(N\asymp Y\), the absolute sum for \(q>P\) is \(O_\epsilon(Y^\epsilon/P)\), and the absolute sum for \(q\le P\) with an extra factor \(q\) is \(O_\epsilon(Y^\epsilon)\). For instance \(\mu^2(q)|c_q(N)|\le(q,N)=\sum_{d\mid(q,N)}\varphi(d)\); split \(q=dk\) and sum \(k\) with the bounds \(1/\varphi(q)^2\ll_\eta q^{-2+\eta}\). In the first sum, \(d\le P\) gives each divisor at most \(O_\eta(P^{-1+\eta})\) by the tail in \(k\), and \(d>P\) gives at most the same by convergence of the \(k\)-sum. In the second sum each divisor gives \(O_\eta(P^\eta)\). Absorb the divisors of \(N\) into \(Y^\epsilon\). The discarded integral at any \(q\le P\) costs \(O(qY/P)\). The full real integral yields the overlap length by convolution and the absolutely convergent series yields the exact \(\mathfrak S(N)\). This adds \(O_\epsilon(Y^{1+\epsilon}/P)\) error. With \(P=Y^{1/4}\) the total individual major error before normalization is \(O_\epsilon(Y^{7/8+\epsilon})\). Its squared normalized contribution over the shell, and the squared normalized minor contribution computed above, both prove (2).

## 2. Exact moving tests without partitioning the moduli

Write \(B(u)=\sqrt u f(u)\) for \(u>0\), extended by zero for \(u\le0\). For \(c_N=N/X\in[2,11/5]\), put \(W_N(v)=B(v/c_N)\) on \([0,4]\), so \(W_N(4)=0\) and \(\sup_N\|W'_N\|_\infty\ll_f1\). Use the exact identity

\[
 B(n/N)=W_N(n/X)=-\int_0^4 W'_N(v)1_{[0,vX]}(n)\,dv
\]

on the raw support. It also holds with a real continuous argument. Define the test discrepancy without the unit restriction,

\[
 E_N(f)={1\over N}\sum_{n+m=N}\Lambda(n)\Lambda(m)B(n/N)B(m/N)
    -\mathfrak S(N)\int_0^1 B(u)B(1-u)\,du.
\]

It is exactly the integral in two thresholds \(v,w\) of \(W'_N(v)W'_N(w)E_N([0,vX],[0,wX])\). The coefficient depending on \(N\) is a bounded diagonal multiplier on \(\ell^2\) of the shell. Apply Minkowski there using (2) for each pair \(v,w\), and integrate over the fixed square \([0,4]^2\). This proves \(\sum_N |E_N(f)|^2\ll_{f,\epsilon}X^{3/4+\epsilon}\) with neither a grid nor an implicit uniform-in-\(N\) choice of exceptional sets inside the integral.

Restoring \((nm,N)=1\) changes each \(E_N(f)\) by \(O_f(X^{-1}L^3)\). Indeed any nonunit nonzero term has one leg equal to a power of a prime dividing \(N\). For each such prime the sum of its von Mangoldt weights over all powers up to \(Y\) is at most \(L\), and each fixes the other leg uniquely with weight at most \(L\). The number of such primes is \(O(L)\). Thus the same squared estimate holds for the unit-restricted discrepancy, denoted \(E_N^{\mathrm{unit}}(f)\).

## 3. Opposite signed terms in the genuine decomposition

In the exact log-cumulative physical representation, the test \(g_N\) acts on an atom at \((u,v)\) by \(2\pi\sqrt{uv}f(u)f(v)\), in the original normalized line measure; this is the integration identity of the prime-cofactor proposition. The same identity applies to the Beta line model by integration. Both supports lie in \((2/5,3/5)\); after the diagonal cancellation, the only line that meets them is the sum \(u+v=1\) with sign minus. Thus

\[
 \langle T_N g_N,g_N\rangle=-2\pi E_N^{\mathrm{unit}}(f).
\]

In particular the second moment gives at most \(O_{f,\epsilon}(X^{3/4+1/20+\epsilon})=O_{f,\epsilon}(X^{4/5+\epsilon})\) exceptions to \(|E_N^{\mathrm{unit}}(f)|\le X^{-1/40}\). The fixed-prefix R22 comparison has error \(\|P_1(T_N-C^*_{\rm rr})P_1\|_{\rm HS}\ll_\epsilon N^{-1/120+\epsilon}\) under the same global GRH, with all of \(D_*,Q,W\) kept fixed as above. As \(\|g_N\|_2\ll_f1\), this proves the second identity in (1).

Finally the prime-cofactor proposition supplies \(\gg_f X\) moduli in the same shell with bounded \(\mathfrak S(N)\) and \(-\langle C_N^{pp}g_N,g_N\rangle\ge c_f>0\). Remove the \(O_{f,\epsilon}(X^{4/5+\epsilon})=o(X)\) exceptional moduli (take \(\epsilon<1/120\) as well for the comparison error to shrink). The lower bound from that proposition and the positive complementary form then hold on exactly the same surviving moduli, and compensate each other to the accuracy in (1). This uses majority information only for the *sum* of the two parts on the specified form; it does not give a pointwise mechanism that controls their compensation for every \(N\).
