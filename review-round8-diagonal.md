# Round 8: replace the very long exact diagonal by a smooth prime-density tail

**Scope.** The arithmetic diagonal $D_N$ is one separate positive term in the true Hardy residual $P_N-D_N-K_N$. The estimate below controls its approximation in **full operator norm**. It applies under the ordinary Riemann hypothesis, which is included in the paper's local GRH(N) by the primitive conductor 1. It gives a concrete cutoff for evaluating the diagonal contribution, not cancellation with the character and Beta terms, or verification of S or R.

Use the full Hardy logarithmic coordinates of [operator-round4.md](operator-round4.md), in which $x=\log(Nu)$ is the log of raw additive size. Write $L=\log N$, $\alpha=1/L$, $\beta=1/8$, $W(x)=1+e^{-2(\beta-\alpha)x}$. Here $N$ is sufficiently large that $\alpha\le\beta$. Define
$$
 D_N^{\rm mass}(X)=\sum_{n\le X,\,(n,N)=1} n\Lambda(n)^2.
$$
The kernel of the exact diagonal in these unitary coordinates is
$$
 2\pi\sqrt{W(x)W(y)} e^{-(1+\alpha)(x+y)}
            D_N^{\rm mass}(e^{\min(x,y)}).
$$
For example this follows from the physical causal atom $\sqrt{2\pi}(n/N)x_{\rm phys}^{-3/2}w(x_{\rm phys})^{-1/2}\mathbf1_{n\le Nx_{\rm phys}}$ in [operator-round7.md](operator-round7.md) with diagonal weight $\Lambda(n)^2/n$, then changing measure to the log variable in both slots. In particular the leading mass is of order $X^2\log X$, not $X\log X$.

Fix a raw cutoff $X_0\ge600$, set $u_0=\log X_0$, and replace the mass by
$$
 D_{N,X_0}^{\rm mass}(X)
 =D_N^{\rm mass}(\min(X,X_0))
  +\mathbf1_{X\ge X_0}\int_{X_0}^{X} t\log t\,dt.
$$
Write $D_{N,X_0}$ for the resulting kernel operator. This keeps the low arithmetic exactly, then inserts only a primitive polynomial-logarithmic antiderivative. The correction is zero whenever either coordinate lies below $u_0$. Uniformly over the full upper quadrant,
$$
 \bigl\|D_N-D_{N,X_0}\bigr\|
 \le \frac{8\pi}{1+\alpha}\,X_0^{-2\alpha}
 \left[
 X_0^{-1/2}\left(\frac{3}{8\pi}\log^3X_0+\log^2X_0\right)
  +X_0^{-1}L\log X_0
 \right].\tag{1}
$$
The bound is numerically explicit, though conservative. The error is also Hilbert–Schmidt by the same exponential envelope. It holds without discarding any high-to-high directions, and because the difference vanishes on mixed low/high coordinates it also certifies a full-matrix replacement, not only a high diagonal compression.

## Proof of the effective error

By [Schoenfeld, Theorem 10, equation (6.3)](https://www.ams.org/mcom/1976-30-134/S0025-5718-1976-0457374-X/S0025-5718-1976-0457374-X.pdf), RH gives $|\vartheta(t)-t|\le (8\pi)^{-1}\sqrt t\log^2 t$ for $t\ge599$. Use it on $X\ge X_0\ge600$. Abel summation against $t\log t$ bounds the weighted prime-only discrepancy on $(X_0,X]$ by
$$
 \frac{1}{8\pi}\left(
 X^{3/2}\log^3X+X_0^{3/2}\log^3X_0
 +\int_{X_0}^X\sqrt t\log^2t(\log t+1)dt
 \right)\le\frac{3}{8\pi}X^{3/2}\log^3X .
$$
For the inequality, the integral is at most $(2/3)(1+1/\log X_0)X^{3/2}\log^3 X$. Proper prime powers with exponent $k\ge2$ have total squared-weight contribution at most
$$
 X\sum_{k\ge2} X^{1/k}(\log X/k)^2
 \le X^{3/2}\log^2X
$$
by counting bases by all integers, bounding each term $p^k$ by $X$, and using $\sum_{k\ge2}k^{-2}<1$. Excluding the primes dividing $N$ costs at most $X L\log X$ because $\sum_{p\mid N}\log p\le L$ and the contributing primes are at most $X$. The power correction already bounds all proper powers whether or not they are units. Thus the same three displayed errors bound $|D_N^{\rm mass}(X)-D_{N,X_0}^{\rm mass}(X)|$ for $X\ge X_0$.

Insert $X=e^{\min(x,y)}$ in the kernel. On its support $x,y\ge u_0$ we have $\sqrt{W(x)W(y)}\le2$. For $u=\min(x,y)$,
$$
 e^{-(1+\alpha)(x+y)}
  =e^{-2(1+\alpha)u}e^{-(1+\alpha)|x-y|}.
$$
Each of $e^{-(1/2+2\alpha)u}u^3$, $e^{-(1/2+2\alpha)u}u^2$ and $e^{-(1+2\alpha)u}u$ is nonincreasing on $u\ge u_0>6$. The absolute kernel is therefore at most $4\pi$ times the bracketed weighted amplitude in (1), times $e^{-(1+\alpha)|x-y|}$. Its row and column integrals cost at most $2/(1+\alpha)$ by the elementary exponential integral, proving (1) by the Schur test. The decay of the same amplitude in $u$ also gives square integrability without a height cutoff.

## What size needs actual raw prime data?

For any fixed $A>0$, choose $X_0=L^{2A+2}$ for large $N$. Formula (1) is $o(L^{-A})$; notably even the diagonal's needed prime data extend only polylogarithmically far in raw size in this bound. For the paper's R accuracy $\delta_N=\sqrt{\mathfrak S(N)/N}L^{3/2}$, one may choose $X_0=N L^4$ for large $N$: (1) is $O(N^{-1/2}L)=o(\delta_N)$, as $\mathfrak S(N)\gg1$. These cutoffs concern the exact diagonal term only; they are not lower complexity bounds, a numerical certificate at a particular $N$, or claims that one should enumerate the true character Gram or Beta term to the same threshold. The latter two terms require their own, independent error budgets.
