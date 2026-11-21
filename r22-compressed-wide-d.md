# R22: the central remainder with the original wide-prefix divisor cutoff

Assume global Dirichlet GRH and take even \(N\). Fix the **wide** prefix \(b_*=N^{3/40}\) and keep its cutoff \(D_*=\lfloor\lceil4b_*N\rceil^{1/3}\rfloor\asymp N^{43/120}\) and \(Q=N^{7/8}\) throughout. Let \(P_c\) be the projection to the physical prefix \(0<x\le c\); define \(C^{*}_{\rm rr}\) as the actual rough–rough high-product arithmetic component of the wide-prefix kernel, with \(d,e>D_*, de>Q\), both integers divisible by at most one prime from \(W=\prod_{p\le\log N,\ p\nmid N}p\), and the original alias signs, unit restriction, and diagonal removal. Then
\[
 \|P_c(T_N-C^{*}_{\rm rr})P_c\|_{\rm HS}\ll_\epsilon N^{-1/1200+\epsilon}
 \quad(1\le c\le N^{1/40}).
\]
For any fixed \(c>0\), the bound is \(O_{c,\epsilon}(N^{-1/120+\epsilon})\). These bounds concern the already-chosen wide decomposition. Neither the compressed rough–rough remainder nor any block outside this central support is bounded here.

This is not the R21 joint corollary evaluated at a new \(c\). The latter resets \(D\) to \(\asymp(cN)^{1/3}\), defining a **different** rough–rough term and a different mixed survivor. Here the divisor indices and the R20 good-leg membership are set using \(D_*\) exactly as in the wide prefix and do not change upon compression. The Boolean selections \(W\), good and rough, and the local product test \(de>Q\) are also unchanged. Only the support of the raw pair and the number of aliases shrink.

## Transfer to the same cut labels

Compress the wide-prefix decomposition from [pinned R17](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e00c099b5f2332ca3bd8fa5856a58af862e/arithmetic-post-r16-mobius-longlong.md), [R18](r18-arithmetic.md), [R19](r19-arithmetic.md), and [R20](r20-arithmetic.md). Their total \(O_\epsilon(N^{-7/480+\epsilon})\) Hilbert–Schmidt error does not increase. A cumulative kernel up to physical \(x,y\le c\) uses only \(n/N\le x,m/N\le y\), so each genuine arithmetic component of the compression is exactly the former component restricted to \(n,m\le cN\), not a new decomposition. Besides \(P_c C^{*}_{\rm rr}P_c\), the exact unestimated terms are the two R20 reflected mixed survivors. On the orientation whose first leg is good, they have \(D_*<d\le D_*(\log N)^2\), \(e>Q/D_*\), and the original membership \(a_*=d/(d,L(n))\le D_*,\ a_*e>Q\).

Take \(X=\lceil4cN\rceil\) as the raw support parameter (**not** in the definition of \(D_*\)). Then there are \(O(c)\) aliases for \(c\ge1\), and every endpoint and line shift in the CRT proof is \(O(X)\). The true pair support is \(n,m\le cN\). Split the exact mixed arithmetic into \(e<E\) and \(e\ge E\), with equality counted exactly once.

* **Low piece.** Apply the proof of [R21 reciprocal GRH dispersion](r21-source.md), frozen SHA-256 21a638f5e2a5e1a913f65d5669f676aa87d4a195442a3d4aca2916fc9d8ddaec. Its raw estimate before substituting exponents is \(N^\epsilon\) times
  \[
  1+X/P_0+UV/H+U\sqrt{UVP_0}+U\sqrt{HX}+V+XV^{-1/2},
  \]
  where \(U,V\) are dyadic \(d,e\) lengths, \(P_0\) the large-mask cutoff, \(H\) the Vaaler degree. The proof uses \(X\) only to bound raw length, endpoints and phases, and uses the actual divisor ranges in the dyadic sums. The exact \(a_*\)-test stays fixed when summing \(e\), so it is still one hard \(e\)-interval for each small-leg divisor. Here \(U\ll_\epsilon N^{43/120+\epsilon}\) and \(V\gg N^{31/60}\), since \(7/8-43/120=31/60\). The low-piece density estimate uses this last lower bound, not a replacement cutoff \((cN)^{1/3}\).
* **High piece.** The raw proof of [R21 high-\(e\)](r21-arithmetic-high-e.md), SHA-256 85cf42fa0ba156594025eee68aeeab450eaeaa6590fe0873400814c1ba30332c, gives \(O_\epsilon(D_*XE^{-1/2}N^\epsilon)\) per alias per hard rectangle. In its exact Boolean and CRT expansion one fixes \(d\le D_*(\log N)^2\) and \(\ell=m/e\le X/E\). The two hard cuts in \(n,m\), the original membership and \(e\ge E\) form one interval for \(e\) contained in \([1,X/\ell]\). The same twisted Mertens estimate of that paper gives \(O_\epsilon(N^\epsilon \sqrt{X/\ell})\) per \(d,\ell\); its modulus and extra excluded Euler factors remain polynomial in \(N\). Summing over \(d,\ell\) gives the displayed bound independently of any relation between \(D_*\) and \(X\).

## Two exact choices of parameters

For \(1\le c\le N^{1/40}\) set \(E=N^{41/50}, P_0=N^{31/600}, H=\lfloor N^{41/200}\rfloor\). Thus \(X\ll N^{41/40}, V\ll N^{41/50}\) in the low part. The first four nonconstant low exponents are all \(73/75\), and the last two are at most \(41/50,23/30\). The high exponent is \(43/120+41/40-41/100=73/75\) too. Divide the raw bound by \(N\) and sum \(O(c)\) aliases: \(73/75+1/40-1=-1/600\). The standard layer-cake and absolute divisor complement from both R21 proofs then give HS \(O_\epsilon(N^{-1/1200+\epsilon})\). In more detail, for rectangle bound \(U_0\) the weighted cumulative is \(O(U_0\sqrt{xy})\), and separately \(O_\epsilon(N^\epsilon (xy)^{3/2})\); their product controls the square of the physical log kernel on \(x,y\ge1/N\), of log-area \(O((\log N)^2)\). At \(x<1/N\) or \(y<1/N\) the mixed arithmetic cumulative is exactly zero. These estimates do not add a continuous model.

For fixed \(c\ge1\) set \(E=N^{3/4}, P_0=N^{1/25}, H=\lfloor N^{1/8}\rfloor\). Now \(X\ll_c N\); the six low exponents are \(24/25,59/60,373/400,221/240,3/4,89/120\), and the high exponent is \(43/120+1-3/8=59/60\). There are only \(O_c(1)\) aliases; the same normalization and transfer give HS \(N^{-1/120+\epsilon}\). For \(0<c<1\), further compress the \(c=1\) estimate; the definition of \(D_*\) and all arithmetic labels stay fixed, so no lower cutoff on a fixed core radius is needed. In both parameter choices \(E\le X\) and the strict endpoint partition remains exact.

The resulting central core estimate is a true transfer with the original wide \(D_*\), but it leaves all noncentral mixed contributions unestimated by this corollary. It supplies neither S nor R.
