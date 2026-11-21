# R21 joint corollary: the entire mixed sector disappears on a growing prefix

Assume global Dirichlet GRH and let \(N\) tend through even moduli. Use the physical Hardy prefix \(P_b\), the R17 cutoff \(D=\lfloor\lceil4bN\rceil^{1/3}\rfloor\), and \(Q=N^{7/8}\). Set \(W=\prod_{p\le\log N,\ p\nmid N}p\). Let \(C_{\rm rr}\) be the **unmodified arithmetic** long–long sector \(d,e>D,\ de>Q\) with both raw integers \(n,m\) divisible by **at most one distinct prime** from \(W\), keeping all original signs, unit restrictions, and exact \(n=m\) deletion. This sector includes “one small prime” cases, not just fully rough integers. Then
\[
\|P_bT_NP_b-C_{\rm rr}\|_{\mathrm{HS}}\ll_\epsilon N^{-1/200+\epsilon}
\qquad (1\le b\le N^{1/40}),
\]
uniformly in \(b,N\). For any fixed \(b>0\), there is the stronger bound \(O_{b,\epsilon}(N^{-1/50+\epsilon})\). The result removes the entire mixed sector on these prefixes, but does not bound \(C_{\rm rr}\), prove S or R, or reach the larger prefix \(b=N^{3/40}\).

**Exact inputs.** This uses the [R17 long–long compensation](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e00c099b5f2332ca3bd8fa5856a58af862e/arithmetic-post-r16-mobius-longlong.md), [R18 low-product component](r18-arithmetic.md), [R19 two-good-leg cancellation](r19-arithmetic.md), [R20 one-good-leg narrowing](r20-arithmetic.md), plus the explicit raw bound of [R21 reciprocal GRH dispersion](r21-source.md) (frozen SHA-256 21a638f5e2a5e1a913f65d5669f676aa87d4a195442a3d4aca2916fc9d8ddaec) and the uniform [R21 high-\(e\) bound](r21-arithmetic-high-e.md) (85cf42fa0ba156594025eee68aeeab450eaeaa6590fe0873400814c1ba30332c).

## Growing prefix

The first four inputs together leave just \(C_{\rm rr}\) and the actual two reflected mixed survivors, with error \(O_\epsilon(N^{-1/20+\epsilon})\) uniformly for \(1\le b\le N^{1/40}\). Indeed their worst bound is \(b^{1/2}(Q/N)^{1/2}+b^{11/12}N^{-1/12}\) up to \(N^\epsilon\). Throughout this range \(D^2<Q\) for all sufficiently large \(N\). On the mixed survivor with the good leg first, the small good divisor lies in \(D<d\le D(\log N)^2\), the other divisor satisfies \(e>Q/D\), and the exact additional membership remains \([d/(d,L)]e>Q,\ d/(d,L)\le D\), with \(L=L(n)\) as in R20. Write the reflected survivor with the same convention for the other divisor.

Split at \(E=N^{5/6}\): the low piece has \(e<E\), the high piece \(e\ge E\). The low proof in [R21 reciprocal GRH dispersion](r21-source.md) admits any hard upper endpoint in \(e\) and proves, before specialization of its parameters, the raw upper bound \(N^\epsilon\) times
\[
1+X/P_0+UV/H+U\sqrt{UVP_0}+U\sqrt{HX}+V+XV^{-1/2}.
\]
Here \(X=\lceil4bN\rceil\), \(d\asymp U,e\asymp V\), \(P_0\) is the cutoff for a large Boolean mask (the mask is estimated absolutely when \(P>P_0\) or \(R>P_0\)), and \(H\) is the Vaaler degree. All mask, phase, and Mellin steps are uniform in these polynomial parameters; that bound is used with
\[
X\ll N^{41/40},\quad U\ll_\epsilon N^{41/120+\epsilon},\quad
N^{8/15}\ll V\ll N^{5/6},\quad P_0=N^{3/50},\quad
H=\lfloor N^{11/50}\rfloor .
\]
The lower exponent for \(V\) is \(7/8-41/120=8/15\), from \(e>Q/D\). The six nonconstant exponents in the raw bound are at most \(193/200,191/200,1151/1200,1157/1200,5/6,91/120\), respectively. The maximum is \(193/200\). After dividing by \(N\) and summing \(O(b)\) aliases this is \(O_\epsilon(N^{-1/100+\epsilon})\) on rectangles; the same R21 cumulative Hilbert–Schmidt transfer takes its square root, giving \(N^{-1/200+\epsilon}\). No endpoint smoothing is being substituted for an actual hard \(e<E\) cut.

For the complementary high piece \(E\le X\) since \(b\ge1\), and [R21 high-\(e\) bound (1)](r21-arithmetic-high-e.md) gives \(b^{7/6}N^{1/6+\epsilon}E^{-1/4}\ll_\epsilon N^{-1/80+\epsilon}\). The cuts partition the actual integer divisors, including equality if it occurs. Add the two reflected orientations and the previous errors to conclude.

## Fixed prefix

For fixed \(b\ge1\), instead choose \(E=N^{3/4}, P_0=N^{1/25},H=\lfloor N^{1/8}\rfloor\). In the low bound \(X\ll_b N\), \(U\ll_{b,\epsilon}N^{1/3+\epsilon}\), \(N^{13/24}\ll_b V\ll N^{3/4}\). The corresponding nonconstant exponents are \(24/25,23/24,179/200,43/48,3/4,35/48\). Therefore the low HS bound is \(N^{-1/50+\epsilon}\), and the high bound is \(N^{-1/48+\epsilon}\). The previous errors are \(O_{b,\epsilon}(N^{-1/16+\epsilon})\), so the largest remaining error is \(N^{-1/50+\epsilon}\). For \(0<b<1\), compress the \(b=1\) result and keep its chosen \(D\); if one insists on \(D=\lfloor\lceil4bN\rceil^{1/3}\rfloor\) instead, run the exact same estimates with that cutoff and \(O_b(1)\) aliases, since the arguments only use \(X\asymp_b N\) and \(D\asymp_b N^{1/3}\) there. In particular no lower cutoff on a fixed positive physical prefix is required to interpret the compressed result.
