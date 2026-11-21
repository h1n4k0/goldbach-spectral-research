# R27: a signed subexponential-factor sector inside the actual zero-small remainder

Use the accepted [R25 central one-giant/no-giant selection](r25-source-one-giant-no-giant-orbit.md), retaining the exact least eligible nonrepeated \(e\), the original fixed central support \(J_-\times J_+\), normalization, unit and sign conventions, and the original wide \(D=D_*\asymp N^{43/120}\). Thus \(n=pq\) with \(q\) prime in \([N^{1/10},N^{3/25}]\), \(e\) prime in \([N^{37/100},N^{39/100}]\), \(n+m=N\) even, and \(s=m/e\). Work with the actual right nonmultiples of \(e\) left over after R25, whose coefficient on this pair is \(\sum_{t\mid s,\ t>D}\mu(t)\log(m/t)\) before the original left and outer factors.

Fix \(0<\tau<1/3\), put \(L=\log N,\ Y=\exp(L^\tau)\), and select pairs with
\[
 s=A s_0,\qquad A>1,\qquad
   L<\ell\le Y\text{ for every prime }\ell\mid A,\qquad
   P^-(s_0)>N^{1/6}.
\]
Here \(P^-(1)=+\infty\). The factorization of \(s\) is unique for sufficiently large \(N\), since \(Y<N^{1/6}\); \(A\) can have arbitrarily many distinct prime bases. Both actual raw legs have **zero** prime factors at or below \(L\), stronger than their required original roughness. For the Hilbert–Schmidt norm of this actual signed subcomponent on the physical prefix \(P_1\),
\[
 \|P_1C_{\rm zm,subpower}P_1\|_{\rm HS}
      \ll_{\tau} L^{3\tau-1}.                                      \tag{1}
\]
This tends to zero, belongs to the zero-small class not covered by R26, and does not cover \(A=1\) or the forbidden factor-gap cases. The arithmetic proof is unconditional, with local GRH(N) only for identification with the manuscript's Hardy realization.

## 1. Exact complete orbit for all the subexponential prime factors

For each \(a\mid s_0\), sum over all divisors \(B\mid A\) with \(Ba>D\). Since \((A,s_0)=1\), nonzero terms have \(\mu(Ba)=\mu(B)\mu(a)\) and \(B\mid\operatorname{rad}A\). The raw masks are on \(n,m\) and on the R25 choice of \(e\); none of these varies with \(B\). The original product cutoff is automatic for these long right divisors, because the left giant satisfies \(pD>Q\).

If \(a>D\), every divisor \(B\mid A\) is permitted. The coefficient sum in this complete orbit is
\[
 \sum_{B\mid A}\mu(B)\log(m/(aB))
       =-\sum_{B\mid A}\mu(B)\log B=\Lambda(A),
\]
since \(A>1\) and \(\sum_{B\mid A}\mu(B)=0\). In particular the complete contribution is identically zero when \(A\) has at least two distinct prime factors. If \(a\le D/\operatorname{rad} A\), no nonzero term is long. Thus the exact right coefficient is
\[
 \Lambda(A)\sum_{\substack{a\mid s_0\\ a>D}}\mu(a)
 +\sum_{\substack{a\mid s_0\\D/\operatorname{rad}A<a\le D}}
     \mu(a)\sum_{\substack{B\mid A\\Ba>D}}\mu(B)\log(m/(aB)).          \tag{2}
\]
The lower endpoint of the boundary is strict. This is genuine same-pair signed cancellation, not a replacement by a second affine counting problem. The rest of the proof uses upper bounds only after taking the orbit sums in (2).

## 2. Weighted exclusions; no \(N^\epsilon\) hidden in subpower sparsity

Write \(w(A)=2^{\omega(A)}\). Since \(s_0\le N/e\ll N^{.63}\), it has at most three prime factors counted with multiplicity. The total weight of an actual selected pair, using the original unsigned divisor majorant and including \(\log q\), is at most \(O(L^2 w(A))\). Here it is important not to replace \(w(A)\) by a generic \(N^\epsilon\) in treating the smooth tail. For original units \(m\le N\), \(eA\mid m\); ignoring the least-\(e\) restriction in a positive upper bound gives at most \(N/(eA)\) points for fixed \(e,A\). Each \(m\) fixes \(n\) and at most one \(p,q\) by uniqueness of the left giant.

For \(A>N^{1/20}\), use \(t=1/\log Y=L^{-\tau}\). Over integers \(A\) supported on \(L<\ell\le Y\),
\[
 \sum_{A>N^{1/20}}\frac{w(A)}{A}
 \le N^{-t/20}
      \prod_{L<\ell\le Y}
           \left(1+\frac{2}{\ell^{1-t}-1}\right)
 \ll_\tau e^{-L^{1-\tau}/20}\,L^{O(1)}.
\]
Indeed \(\ell^t\le e\), so the logarithm of the product is \(O(\sum_{\ell\le Y}1/\ell)=O(\log L)\). Multiply by \(N L^2\sum_e1/e\); the raw tail is \(O_{\tau,M}(N L^{-M})\) for any fixed \(M\). This proves the stated sparsity with the actual logarithms and divisor multiplicity, rather than absorbing them in an unavailable power saving.

Also temporarily discard any \(r^2\mid s_0\) for a prime \(r>N^{1/6}\). The nonrepeated \(e\) condition implies \(r\ne e\), and \(r\nmid A\) by the gap, so \(eAr^2\mid m\). The raw bound after \(\sum_{r>N^{1/6}}r^{-2}\) is \(O_\tau(N^{1-1/6}L^{2+2\tau})\), using \(\sum_A w(A)/A\ll(\log Y)^2\) from the Euler product below, and \(\sum_e1/e\ll1\). This is negligible for (1). In the remaining proof \(A\le N^{1/20}\), \(s_0\) is squarefree and \(s_0\gg N^{.56}\) on the fixed right support.

## 3. Uniform finite sieve and the divisor-boundary log moment

Use the same finite uniform Selberg upper bound as in [R23](r23-source-double-giant-proper.md) and [R26](r26-source-nonmultiple-small-prime-orbit.md). For fixed \(q,K\) the line \(q p+K b=N\) with \((q,K)=1\) parametrizes two affine forms in an integer variable with steps \(K,-q\), determinant of magnitude \(N\). In all our uses \(N\mid n+m\) and units imply \(q\nmid K\mid m\), so \((q,K)=1\). The parameter interval is no longer than \(N/(qK)\) and can be enlarged to length \(H\asymp N/(qK)\). If \(H\gg N^\delta\) and both forms are free of prime divisors up to \(H^{1/10}\), the bound is \(O_\delta(H(\log\log(3N))^2/L^2)\); this is justified by the explicit Selberg quadratic with the primes dividing \(2qKN\) omitted. All omitted-prime products have the stated log-log bound uniformly since \(q,K,N\) are polynomially bounded. Only an upper sieve is used, and extra exact masks may be dropped there.

For the complete term in (2), take \(K=eA,\ b=s_0\). Then \(H\gg N^{1-.12-.39-.05}=N^{.44}\), and \(H^{1/10}\) lies below \(N^{1/6}\) and below the giant \(p\). Thus \(b\) is sifted whether or not prime. At most \(2^3\) divisors \(a\mid s_0\) occur. The raw upper bound for this part is
\[
 \ll \frac{N(\log\log(3N))^2}{L^2}
   \sum_q\frac{\log q}{q}\sum_e\frac1e\sum_A\frac{\Lambda(A)}{A}
 \ll_\tau N(\log\log(3N))^2 L^{\tau-1},
\]
because \(\sum_q\log q/q\ll L,\ \sum_e1/e\ll1\) on their fixed exponent bands, and \(\sum_A\Lambda(A)/A\ll \log Y=L^\tau\) on the indicated subexponential prime powers.

For the boundary \(D/\operatorname{rad}A<a\le D\), \(a>1\) since \(A\le N^{1/20}\); any such \(a\) has at most two remote prime factors (all \(>N^{1/6}\)). Also \(s_0/a>1\) since \(s_0\gg N^{.56}\). Fix a prime \(b\mid(s_0/a)\), choose it canonically if needed, and put \(b'=s_0/(ab)\). Now fix \(q,e,A,a,b'\) and take \(K=eAab'\). If these parameters have any eligible raw pair then \(Kb=m\asymp N\), \(b>N^{1/6}\), so \(H\gg N^{1/6-3/25}=N^{7/150}\). Both prime values \(p,b\) exceed the sieve level. This gives the same finite upper bound after fixing the *actual* remaining factors. In summing positive majorants the harmonic \(b'\) sum costs \(O(1)\), since \(b'\) has at most two remote primes and \(\sum_{N^{1/6}<\ell\le N^{.63}}1/\ell=O(1)\).

As in R26, fix one of the factors if \(a\) has two, then the other lies in an interval of multiplicative factor \(\operatorname{rad}A\); dyadic prime bounds, restricted to primes \(>N^{1/6}\), give
\[
 \sum_{\substack{D/\operatorname{rad}A<a\le D\\
                  P^-(a)>N^{1/6},\ \mu(a)^2=1}}\frac1a
       \ll \frac{1+\log\operatorname{rad}A}{L}.
\]
The original inner boundary marker is bounded in absolute value by \(O(Lw(A))\). To sum these bounds without losing the gain, use the exact Euler product and its additive log moment:
\[
 E_Y:=\sum_A\frac{w(A)}{A}
        =\prod_{L<\ell\le Y}\left(1+\frac2{\ell-1}\right)
        \ll \left(\frac{\log Y}{\log L}\right)^2,\qquad
 \sum_A\frac{w(A)(1+\log\operatorname{rad}A)}{A}
   =E_Y\left(1+\sum_{L<\ell\le Y}\frac{2\log\ell}{\ell+1}\right)
   \ll\frac{(\log Y)^3}{(\log L)^2}.
\]
The product bound follows from the prime Mertens product because \(1+2/(\ell-1)\) and \((1-1/\ell)^{-2}\) have ratio \(1+O(\ell^{-2})\). The log identity is the finite-prime Euler factor probability of a nonzero exponent, \(2/(\ell+1)\), followed by the usual Chebyshev harmonic prime-log bound. The lower endpoint \(L\) in the Euler product pays for the rough singular-factor \((\log\log(3N))^2\).

Combining these bounds, the raw boundary majorant is
\[
 \ll \frac{N(\log\log(3N))^2}{L^2}
          L\sum_q\frac{\log q}{q}\sum_e\frac1e
           \sum_A\frac{w(A)(1+\log\operatorname{rad}A)}{A L}
 \ll_\tau N\,L^{3\tau-1}.
\]
The complete term is smaller for fixed \(\tau>0\) because \((\log L)^2=O_\tau(L^{2\tau})\); both excluded tails are smaller as well.

## 4. Fixed-prefix transfer, nonemptiness, and what is still missing

After the signed summation (2), these are bounds on total raw absolute variation uniform over subrectangles of the fixed central support. Normalize by \(1/N\) and use the original cumulative \(\sqrt{uv}\) weighted kernel. On \(P_1\) it vanishes unless \(x\ge\inf J_->0,\ y\ge\inf J_+>0\), where the Hardy normalization and log-area are bounded. This gives (1) for the actual Hilbert–Schmidt norm. The reflected copy, if included, is bounded by the same argument.

For a nonempty actual family, let \(T\) grow, choose \(q\asymp T^{.11}\), \(e\asymp T^{.38}\) prime, and choose a prime \(\ell\asymp(\log T)^2\). Put \(A=\ell\) or the product of two distinct such primes in disjoint proportional intervals, and choose a prime \(v_0\asymp T^{.62}/A\). Set \(m=eA v_0\asymp T\). As in R26, ordinary PNT gives a prime \(p\asymp T/q\) putting \(n=pq\) inside the prescribed fixed ratio interval relative to this \(m\). Then \(N=n+m\asymp T\) is even, the raw integers are coprime by the disjoint ranges of the prime bases, \(e\) is the unique eligible nonrepeated right prime, and \(s=A v_0\) satisfies the actual masks and factor thresholds (including \(L<\ell\le Y\)). Here \(A<D<v_0\). For \(A=\ell\), the right signed nonmultiple coefficient is \(-\log\ell\), nonzero; for two distinct prime bases in \(A\) its constituent long divisor terms are nonzero but cancel exactly. This is a witness within the original sum alias, not a lower bound for the total operator.

In contrast, the fully polynomial-rough class \(A=1\) has no local orbit gain. Its R25 right nonmultiples already have opposite order-\(\log N\) signs on \(s\) prime and on squarefree \(s=r_1r_2\) with both primes \(\le D\): \(-\log e\) and \(+\log e\), respectively. For example, the latter admits scales \(r_1\asymp N^{.30},r_2\asymp N^{.32},e\asymp N^{.38},q\asymp N^{.11}\). Fixing \(q,e,r_1\) leaves the two-prime line \(qp+e r_1r_2=N\) with parameter length \(\asymp N^{.21}\). The primitive-line upper sieve used here gives no matching signed asymptotic across that family and the one with \(s\) prime. A usable pointwise comparator would have to estimate their weighted difference at the same \(N\), after averaging the **specified** polynomial prime coefficients and keeping the same raw ratio and least-\(e\) restrictions. This proof does not provide that comparator or any conclusion on S/R.
