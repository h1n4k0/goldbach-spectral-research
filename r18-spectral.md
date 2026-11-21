# Round 18: a pointwise finite-moment certificate on the actual central block

**Scope.** This gives a quantitative sufficient test for one true block and an arithmetic limit on a class of localized counterexample mechanisms. It estimates the omitted directions in the test, **not** the remaining finite arithmetic moments. It gives no full-operator or pointwise S/R assertion. The arithmetic estimates below are unconditional; the identification with the [Li–Liu Hardy operator](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf) uses local GRH(N). No averaging, synthetic replacement of $\Lambda$, or auxiliary Dirichlet GRH is needed.

## 1. The exact two-dimensional part of the central compression

Write $a=1/2$, $b=9/16$, $\ell_0=b-a$, and $I=[a,b]$ on the normalized physical axis. This is the same compression as $J=[\log a,\log b]$ on the physical **logarithmic** axis. Let
$$
 d\mu_N(u)=\sqrt{u(1-u)}
   \left(\frac1N\sum_{\substack{n+m=N\\(nm,N)=1}}
        \Lambda(n)\Lambda(m)\delta_{n/N}(du)
     -\mathfrak S(N)\,du\right)
$$
on $0<u<1$. Put $S=\mathfrak S(N)$ and $F(x)=\mu_N((a,x])$ on $I$. The reflection $u\mapsto1-u$ preserves $\mu_N$; the unit restriction removes any atom at $a$. In the exact cumulative kernel of [Round 2](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e0/source-round2.md), $x,y\in I$ allow no nonzero difference alias and only the first sum alias. The diagonal is subtracted exactly. Thus $\mu_N([1-y,x])=F(x)+F(y)$ and the compressed kernel is
$$
 -2\pi r_N(x)r_N(y)(F(x)+F(y)),\qquad
 r_N(x)=x^{-3/2}\sqrt{(Nx)^{-2/\log N}+(Nx)^{-1/4}}.                  \tag{1}
$$
The minus sign is the first sum alias sign. In particular the block has rank at most two, even though the signed measure has many atoms. This rank limit also follows from the Round 2 interface decomposition; the quantitative moment tail below is the new input.

More explicitly, put $U=r_N|_I$, $V=r_NF|_I$. The operator is $-2\pi(U\otimes V+V\otimes U)$, with possible nonzero eigenvalues $-2\pi(\langle U,V\rangle\pm\|U\|_2\|V\|_2)$. This follows by restricting to the span of $U,V$ and resolving $V$ into components parallel and orthogonal to $U$; dependent and zero cases follow directly. In particular its norm is $2\pi(|\langle U,V\rangle|+\|U\|_2\|V\|_2)\asymp\|F\|_{L^2(I)}$ with uniform constants because $r_N$ is bounded above and below on this fixed interval.

## 2. Actual arithmetic gives very fine local mass control

For every fixed $0<\rho<1$ and every subinterval $B\subset I$,
$$
 |\mu_N|(B)\ll_\rho S\bigl(|B|+N^{-\rho}\bigr).                      \tag{2}
$$
Indeed one may enlarge the raw interval to length $H\asymp N(|B|+N^{-\rho})$, keeping both summand locations in a fixed compact fraction of $(0,N)$. The two-form upper sieve on the interval in $n$ gives $O(SH/\log^2 H)$ prime–prime pairs. To see its uniformity, the forbidden residue count is one at primes dividing $N$, two at other primes, with the parity prime included in the first case. Upper-bound sieve at level $D=H^{1/2}$ and fixed sufficiently small sieve exponent $z=H^c$ gives the local product $O(S/\log^2 H)$ by Mertens and the two-form Euler factors. The interval remainder before weights is $O(H^{1/2}\log^{O(1)}H)$ since squarefree progression errors are $O(2^{\omega(d)})$ for $d\le D$; it is absorbed. This is the same short-interval upper-sieve argument as [operator-round6.md](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e0/operator-round6.md), applied far from the additive endpoints. Since $\log H\gg_\rho\log N$, Mangoldt weights bounded by $(\log N)^2$ preserve $O_\rho(SH)$ on this raw interval.

The proper prime powers need a **localized**, not global $O(\sqrt N)$, count. For each exponent $j\ge2$, consecutive integer $j$-th powers in the relevant raw range are spaced by $\gg\sqrt N$: if the smaller is $z^j\gg N$, the gap is at least $jz^{j-1}\gg \sqrt N$. Thus there are $O(H/\sqrt N+1)$ possibilities per exponent on either side of the relation; the other summand is determined. The total weighted error is $O((H/\sqrt N+1)(\log N)^3)=O_\rho(H)$, since $H\ge N^{1-\rho}$. The continuous measure in (2) also has bounded density $O(S)$.

## 3. Only finitely many moments need to cancel, with a proved tail

Transfer $I$ affinely to $0\le t\le1$ by $u=a+\ell_0 t$, and let $\bar\mu_N$ be the pushforward measure, $G(t)=F(a+\ell_0t)$. Use the orthonormal cosine basis $\phi_0=1,\ \phi_k=\sqrt2\cos(\pi k t)$. Signed Fubini gives its exact coefficients:
$$
 c_0=\int(1-t)\,d\bar\mu_N(t),\qquad
 c_k=-\frac{\sqrt2}{\pi k}\int\sin(\pi k t)\,d\bar\mu_N(t)
                 \quad(k\ge1).                                   \tag{3}
$$
Because the sine in (3) vanishes at both endpoints, no periodic endpoint jump has to be estimated separately.

For $K\ge0$ let $G_K=\sum_{k=0}^K c_k\phi_k$. Then the actual tail satisfies
$$
 \|G-G_K\|_2\ll_\rho S\bigl((K+1)^{-1}+N^{-\rho}\bigr).             \tag{4}
$$
To prove it, partition the unit interval into $\lceil N^\rho\rceil$ equal cells and put a constant density on each cell with the original signed mass. By (2) the density $g_*$ is $O_\rho(S)$ everywhere, and its cumulative $G_*$ differs from $G$ by $O_\rho(SN^{-\rho})$, since only the unresolved part of the current cell can differ. The derivative formula $G_*'=g_*$ and sine Parseval give $\|\Pi_{>K}G_*\|_2\le (\pi(K+1))^{-1}\|g_*\|_2$. Orthogonal projection and the uniform cumulative approximation prove (4). In contrast the measure's mere total variation gives a cosine tail only $O(S/\sqrt K)$.

Consequently one may insert $V_K(x)=r_N(x) G_K((x-a)/\ell_0)$ into the explicit rank-two formula of (1). The error in the **operator norm of this block** is at most $O_\rho(S((K+1)^{-1}+N^{-\rho}))$, by the difference of the two rank-one terms. In particular, for a prescribed $h\to\infty$ with $hN^{-\rho}\to0$, $K/h\to\infty$ makes the tail $o(S/h)$. The remaining sufficient arithmetic input on this block is
$$
 |c_0|^2+\sum_{k=1}^K |c_k|^2=o(S^2/h^2).                         \tag{5}
$$
Smallness of the block at that scale also implies (5), by the uniform lower comparison in (1). The ratio $K/h$ can tend to infinity arbitrarily slowly in this test. At the R error scale $\delta_N=\sqrt{S/N}(\log N)^{3/2}$, a block approximation with error $o(\delta_N)$ is also possible by choosing $\rho>1/2$ and $K\gg S/\delta_N$ with ratio diverging. Neither (4) nor (5) estimates the moment sums themselves, the other blocks, or the precise coefficient in a full R threshold.

## 4. Localized singleton anomalies: what this exact block cannot amplify

The preceding geometry limits localized mechanisms on this block. A change to a pair product affects both orders equally; below we describe its signed defect measure on the upper half $I$, with its reflection determining the lower half.

* A defect changing coefficients of only $k$ actual unit prime-power pairs by bounded multiplicative factors changes the block norm by at most $O(k(\log N)^2/N)$, by (1) and total variation. To cause an order-$S$ change by this mechanism alone would need $k\gg SN/(\log N)^2$ active pairs. Likewise a defect consisting of a bounded-factor deletion or reweighting in one interval of normalized length $\ell$ changes the block at most $O_\rho(S(\ell+N^{-\rho}))$ by (2). If it preserves signed mass inside its interval, its cumulative is supported there and this improves to $O_\rho(S\sqrt\ell(\ell+N^{-\rho}))$. None of these restricts a coordinated change on a total macroscopic range.
* Conversely, write $A=\|F\|_\infty$ with essential supremum. From (2), $|F(x)-F(y)|\ll_\rho S(|x-y|+N^{-\rho})$. If $A$ exceeds a sufficiently large multiple of $SN^{-\rho}$, a point near its supremum has a one-sided subinterval in $I$ of length $\gg_\rho A/S$ on which $|F|\gg A$. This uses $A\ll S$, also by (2). The lower comparison in (1) thus gives $\|T_{N,J}\|\gg_\rho A^{3/2}/\sqrt S$ above the mesh floor. Equivalently $A\ll_\rho S^{1/3}\|T_{N,J}\|^{2/3}+SN^{-\rho}$. The $3/2$ exponent is sharp for bounded-density defects of zero mass on a short interval, as illustrated by a triangular cumulative profile. That is a geometric test, not an assertion that the true primes exhibit such a profile.

These are pointwise certificates and limits for the actual central geometry, not substitutes for the missing signed sine-moment cancellation in (5). The exterior and cross-block parts of $T_N$ remain independent.
