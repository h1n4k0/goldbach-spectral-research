# A single fixed-modulus L¹ profile for a central positive lower bound

**Scope.** This addendum to the [smooth divisor bridge](spectral-signed-rectangle-smooth-bridge.md) gives a weaker sufficient input for one smooth nonnegative test. It neither estimates that input nor proves Hypothesis S. The implication does not assume GRH.

Retain the notation of the smooth bridge: $L=\log N$, $S=\mathfrak S(N)$ for even $N$, $a=1/2$, $b=9/16$, $D=\lfloor\sqrt N/L^C\rfloor$ with $C$ sufficiently large and fixed, and $Q_0=N/D$. Let $B^+(t,y)$ be the actual signed unit rectangle increment on $aN<n\le y$, as in that note. This is the same arithmetic discrepancy, not a surrogate. Put
$$
 M_1(t)=\int_a^b |B^+(t,Nx)|\,dx,qquad
 \mathcal L_N =
   \int_1^{7Q_0/32}\frac{M_1(t)}t\,dt
   +\frac{L}{Q_0}\int_{7Q_0/32}^{Q_0/2}M_1(t)\,dt.
$$
This averages absolute errors over the two auxiliary endpoints **at one fixed modulus**. It does not average over $N$.

Fix any nonzero nonnegative $W\in C_c^1((a,b))$. If
$$
 \mathcal L_N=o\!\left(\frac{N}{L^2\log L}\right),
 \tag{1}
$$
then $G_W\gg_W S/L$ for the normalized Goldbach sum of the smooth bridge. Consequently there are $\gg_W SN/L^3$ prime pairs on the central support of this fixed test and its reflection. This does not require a uniformly bounded least missing prime or a separate pointwise jump hypothesis. If the least missing prime remains bounded along a sequence, even $\mathcal L_N=o(N)$ on that sequence suffices for $G_W\gg_W S$ and hence for the predicted-order lower bound $\gg_W SN/L^2$ (the fixed bound on that prime may enter the constants).

## 1. Both rectangle endpoints can be integrated for a smooth fixed test

In the smooth bridge's long discrepancy, use the same
$$
 K(x,t)=R\big((1-x)Q_0/t\big)\log\big(N(1-x)/t\big).
$$
After the first Abel step in the modulus variable, fix $t$. The signed prefix of the remaining discrete measure in $x$ is exactly $B^+(t,Nx)$. Since $W$ vanishes near both endpoints of the central interval, exact Stieltjes summation by parts against $W(x)\partial_tK(x,t)$ bounds the inner sum by
$$
 \int_a^b |B^+(t,Nx)|\,
               \left|\partial_x\big(W(x)\partial_t K(x,t)\big)\right|\,dx .
$$
There is no boundary term. An atom at a real prefix endpoint has no effect on the Lebesgue integral of the resulting prefix function. In the lower $t$ range $\partial_t K=-1/t$ and is independent of $x$; in the middle range the first derivative and the mixed derivative are $O(L/Q_0)$; above $Q_0/2$ both vanish. Thus the raw signed discrepancy is $O_W(\mathcal L_N)$. All short and baseline estimates are unchanged. In particular,
$$
 G_W=S\left(\int W-P_W\right)
      +O_{A,W}(L^{-A}+\mathcal L_N/N)
$$
for any prescribed fixed $A$ with $C$ chosen large enough, where $P_W$ is the normalized weighted actual $\Lambda(n)\mu(N-n)$ primitive.

## 2. Obtain a usable prime jump from the same integrated profile

For an odd prime $p\nmid N$ with $p=O(L)$, the difference $B^+(p,y)-B^+(p-1,y)$ is minus the individual side discrepancy at $q=p$, since $\mu(p)=-1$. Summation by parts against $W$ bounds the corresponding raw weighted discrepancy by
$$
 \|W'\|_\infty\big(M_1(p-1)+M_1(p)\big).
$$
On $n\equiv N\pmod p$, use $|\mu(N-n)|=\mu^2(N-n)\le 1-\mathbf1_{p^2\mid N-n}$. The two ordinary Siegel–Walfisz progression estimates at the reduced residues modulo $p$ and $p^2$, rescaled by $\varphi(p)$, give the exact upper-density factor $1-1/p$. Deleting nonunit prime powers is negligible. Therefore
$$
 |P_W|\le (1-1/p)\int W
     +O_{A,W}\left(L^{-A}+\frac{p}{N}\big(M_1(p-1)+M_1(p)\big)\right).
 \tag{2}
$$

There are $\gg L/\log L$ choices of $p\in[4L,8L]$ not dividing $N$: this follows from the PNT since at most $L/\log(4L)$ such primes can divide $N$. For each of them, $M_1(t)$ is constant on the half-open unit intervals $[p-1,p)$ and $[p,p+1)$, with values $M_1(p-1)$ and $M_1(p)$ respectively. These intervals have disjoint interiors across the distinct odd primes, lie in the lower $t$ range for large $N$, and their weight $1/t$ is comparable to $1/L$. Consequently
$$
 \sum_{\substack{4L\le p\le8L\\p\nmid N}}(M_1(p-1)+M_1(p))\ll L\mathcal L_N .
$$
Choose one of these primes with $M_1(p-1)+M_1(p)\ll (\log L)\mathcal L_N$. Under (1), its jump term in (2) is $o(1/L)$, and its lower-density gap $\int W/p$ is of order $1/L$. The long transfer error is also $o(S/L)$ because $S$ is bounded below by a positive constant; choosing $A>2$ handles fixed powers of $L$. Thus $G_W\gg_W S/L$, as claimed. There is no upper assumption on $S$ in this step. Removing proper prime powers costs $O_W(L^2/\sqrt N)$, and dividing the surviving raw weight by the maximum weight $O_W(L^2)$ per pair gives the stated count.

If instead $p_0$ is bounded, take $p=p_0$ in (2). The same pair of unit intervals shows $M_1(p_0-1)+M_1(p_0)\ll_{p_0}\mathcal L_N$. Thus $\mathcal L_N=o(N)$ gives error $o(1)$ in (2), maintaining a fixed positive fraction of the weighted main term. Neither version claims an asymptotic, an estimate on the other central tests, or a small full Hardy operator norm.
