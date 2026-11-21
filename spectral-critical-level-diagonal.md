# The actual diagonal target at the square-root transition

**Scope.** A critical-level refinement of the [weighted parity reduction](spectral-post-r19-weighted-parity.md) for the true $\Lambda$ and $\mu$, assuming global Dirichlet GRH. The pointwise diagonal error and the signed parity primitive are still not estimated throughout the required range. This note does not settle S or R.

Use the same notation $L=\log N$, $S=\mathfrak S(N)$, $G_W$, $P_W$, $A_\mu$, $A_{\mu,q}$, and $E_\mu^\flat$. In particular $W$ is supported in $[7/16,9/16]$ with bounded-variation norm $\|W\|_{\rm BV}$, and all arithmetic prefixes are restricted to $(n,N)=1$. Write
$$
 D=\left\lfloor\sqrt N L^{-C}\right\rfloor,\qquad Q=\left\lfloor N/D\right\rfloor .
$$

## 1. The actual discrepancy only needs a polylogarithmic excess over the square root

For every fixed $A>0$, one may take $C=2A+16$. Uniformly in the central weight,
$$
 G_W=S(\int W-P_W)
       +O_A\left(\|W\|_{\rm BV}
            \left[L^{-A}+L E_\mu^\flat(Q)/N\right]\right).
 \tag{1}
$$
The previous split permitted a fixed cutoff $D=N^\theta$, requiring a level $Q$ genuinely greater than $N^{1/2}$ by a power. Here $Q\asymp\sqrt N L^C$.

For details, take the auxiliary square-free expansion cutoff $B=L^{A+8}$. In the short term the arithmetic and model $b>B$ tails, after normalization, are $O(L^3(\log(2B))^2/B)$ times the weight norm. This is the l.c.m. estimate of the preceding note; it uses only $D\le N$. For $b\le B$, the sum of the GRH errors is $O(DBL^3/\sqrt N)$ times the norm, which is $O_A(L^{-A})$ for this $C$. The divisor Euler tails in the previous proof are uniform at cutoffs bounded below by any fixed positive power of $N$ and above by $N$. This applies to $D\ge N^{1/3}$ for large $N$ and to $(N-n)/D\asymp Q$ on the support of $W$. The rest of the proof, including the exact complement condition $n<N-Dq$ and the factor $L$ from summation by parts in $n$, is unchanged. Thus (1) is a consequence of the same estimate with a cutoff approaching the transition, not an assumption of a new prime distribution theorem. E.g. fixed $A=2$ already gives $o(S)$ error from the short terms in the central comparison.

## 2. A signed rectangle target is enough

Define the actual signed Fourier-free rectangle discrepancy
$$
 \mathcal B(t,y)=
   \sum_{\substack{q\le t\\(q,N)=1}}\mu(q)
         \left(A_{\mu,q}(y)-A_\mu(y)/\varphi(q)\right),\qquad
 \mathcal B_* = \sup_{1\le t\le Q,\ 0\le y\le 9N/16}|\mathcal B(t,y)|.
$$
It does not take separate absolute values across $q$. One can replace the error term in (1) by
$$
 O_A\left(\|W\|_{\rm BV}
            \left[L^{-A}+ L^{A+5}\mathcal B_*/N\right]\right).
 \tag{2}
$$
The integral factor in (2) is polylogarithmic; it pays for the replacement of a moving edge by vertical and horizontal segments.

To verify this, partition the support interval of $W$ into $K=\lceil L^{A+4}\rceil$ equal half-open bins (include the final endpoint in the last bin). In the exact raw long-discrepancy sum, the inner condition $q<(N-n)/D$ on a bin is replaced by $q<(N-n_j)/D$, with $n_j$ the normalized bin's left endpoint multiplied by $N$. In each bin the affected $q$ satisfy $q\asymp Q$ and occupy an interval of length $O(Q/K)$. With the bin's $n$-interval of length $O(N/K)$, the number of $n$ in one progression in that bin is $O(D/K+1)$. The progression baseline has the same bound times $O(L)$ from $1/\varphi(q)\ll L/q$. Bounding $\Lambda(n)$ and the kernel log by $L$ each, the total normalized edge error for the progression and baseline together is therefore
$$
 O\left(\|W\|_\infty
            \frac{L^3 K}{N}(Q/K+1)(D/K+1)\right)
 =
 O\left(\|W\|_\infty L^3
           \left[K^{-1}+(Q+D+K)/N\right]\right)
 = O_A(\|W\|_\infty L^{-A}).
$$
This uses $QD\le N$, the explicit $K$, and $D,Q=N^{1/2+o(1)}$; it bounds either inclusion or exclusion of the edge with the same result.

On each resulting rectangle, split the weight as
$W(n/N)\log((N-n)/q)=W(n/N)\log(N-n)-W(n/N)\log q$.
For the first part, Abel summation in $n$ costs $O(L\|W\|_{\rm BV}\mathcal B_*)$, since the $q$ cutoff is fixed. For the second part, Abel summation in $q$ costs at most $O(L\mathcal B_*)$ for each $n$ prefix; Abel summation against $W$ in $n$ again gives the same bound. Partial sums with endpoints of either orientation are obtained by left limits from prefixes; no atom on the moving edge is lost. Sum over the $K$ bins and divide by $N$ to obtain (2). For $q=1$ the discrepancy term is identically zero. The bound $\mathcal B_*\le E_\mu^\flat(Q)$ is automatic, but (2) is useful as a different hypothesis: cancellation across $q$ can matter.

## 3. The genuine signed discrepancy is small above this transition

Fix $A,\epsilon>0$. For $T=\sqrt N L^{2A+16}$ and all $T\le t\le N^{1-\epsilon}$, the actual quantities obey
$$
 \sup_{0\le y\le9N/16}|\mathcal B(t,y)|\ll_{A,\epsilon} NL^{-A}.
 \tag{3}
$$
This upper range can be empty; the assertion is uniform where it is not. It is not a bound on the absolute-modulus sum.

To see (3), put $m=N-n>1$ for the relevant prefixes. If $m$ is squarefree, use $\sum_{q\mid m}\mu(q)=0$ and $\mu(m)\mu(q)=\mu(m/q)$ for $q\mid m$. If $m$ is not squarefree, both sides below vanish. Thus exactly
$$
 \mu(m)\sum_{\substack{q\mid m\\q\le t}}\mu(q)
    =-\mu^2(m)\sum_{\substack{d\mid m\\d<m/t}}\mu(d).
$$
In consequence,
$$
 \sum_{\substack{q\le t\\(q,N)=1}}\mu(q) A_{\mu,q}(y)
  =-\sum_{\substack{d\le N/t\\(d,N)=1}}\mu(d)
    \sum_{\substack{n\le y;\ n<N-td;\ n\equiv N\bmod d\\(n,N)=1}}
          \Lambda(n)\mu^2(N-n).
 \tag{4}
$$
Keep the strict endpoint $n<N-td$. Expand $\mu^2$ using $b^2\mid(N-n)$ and truncate $b$ at $L^{A+8}$. The exact positive-multiple tail bound, the model tail bound, and the uniform GRH progression estimate of §1 hold also for these individual truncated prefixes: there is no $\log d$ present, and $N/t\le\sqrt N L^{-(2A+16)}$. In the progression model use the Lebesgue length of $0\le x\le y$, $x<N-td$, then reverse the $x,d$ order. The extended model equals
$$
 - A_N\int_0^y
    \sum_{\substack{d<(N-x)/t\\(d,N)=1}}\mu(d)g(d)\,dx ,
$$
where $A_N$ and $g(p)=(p-1)/(p^2-p-1)$ are the squarefree short-divisor factors of the preceding note. The lower cutoff $(N-x)/t\ge (7/16)N^\epsilon$ is uniform. The zeroth version of its Euler-convolution argument gives $\sum_{d<Y,(d,N)=1}\mu(d)g(d)=O_{A,\epsilon}(L^{-A})$ at these cutoffs: $1/\zeta(1+s)$ vanishes at $s=0$ and the same tail bound applies (with no logarithmic weight). Thus (4) is $O_{A,\epsilon}(NL^{-A})$. Finally $\sum_{q\le t,(q,N)=1}\mu(q)/\varphi(q)=O_A(L^{-A-1})$ by the corresponding zeroth model with $g(p)=1/(p-1)$; even the elementary $|A_\mu(y)|\le NL$ suffices. This proves (3).

Combining these observations leaves an actual signed-diagonal estimation problem concentrated at or below the square-root transition, rather than the full super-square-root absolute-modulus problem. For instance, (2) can take a larger fixed polylogarithmic $C$ if desired, and (3), with a stronger prescribed logarithmic saving, removes the checked upper portion though it does not estimate the lower rectangles. The signed parity primitive in $P_W$ and the noncentral blocks remain separate inputs.
