# A masked hit-moment obstruction with vanishing central moments

At an even $N$, put $X=\sqrt N$, $L=\log N$ and $\mathcal Q=[.8X,.9X]\cap\mathbb P$. Let $P_n,D_m$ be the genuine prime-box and complete signed complementary coefficients of [the critical-prime setup](weak-s-type-ii-critical-prime-least-prime-boundaries.md). Write

$$
 \mathcal H_N=\{h\in\mathbb Z:0<|h|<N/20,\ \exists q\in\mathcal Q:\ q\mid h\}.
$$

For each $h\in\mathcal H_N$ this $q=q(h)$ is unique, since the product of two distinct critical primes exceeds $N/20$. Also $\#\mathcal H_N\ll N/L$ by counting multiples for each prime. A product multiplier $0\le\rho_m\le1$ is applied to the entire coefficient: $F_m=\rho_m D_m$, not independently to its different divisor representations. Put $F(\alpha)=\sum_m F_m e(\alpha m)$, $e(z)=e^{2\pi iz}$, and

$$
 T_F(M)=\sum_n P_n F_{M-n},\qquad
 T_F^{\mathrm{u}}(N+h)=\sum_{\substack{n+m=N+h\\q(h)\nmid m}}P_n F_m
 \quad(h\in\mathcal H_N).
$$

The prime factors of $n$ are smaller than every $q\in\mathcal Q$, so the latter is the genuine unit part of the hit.

**Theorem.** Fix $A>0$. For every sufficiently large $N=2^j$, keep the actual $I_d=[X,.100N^{.50001}]$, $t=N^{.49999}$ and $y=9N/16$ of [the fixed-prime-box example](weak-s-type-ii-fixed-prime-box-minor-l2.md). There exist two true hard subintervals of its original prime boxes, each of length $\asymp X/K$ with $K=\lceil C_A L/\log L\rceil$, and a genuine product mask $0\le\rho_m\le1$, all fixed before summing over the critical primes. The prime leg is unselected in those intervals: $E=1$ on the actual prime pairs. The mask preserves every sign and gives

$$
 \sum_m m^r F_m=0\quad(0\le r\le K),\qquad
 \sup_{|\beta|\le1/(10N)} |F(\beta)|\ll_A N^{-A}.
 \tag{1}
$$

Nevertheless, both signed shifted-moment sums satisfy

$$
 \sum_{h\in\mathcal H_N}|T_F(N+h)|^2
     \gg_A \frac{N^3}{K^6L^{17}},
 \qquad
 \sum_{h\in\mathcal H_N}|T_F^{\mathrm{u}}(N+h)|^2
     \gg_A \frac{N^3}{K^6L^{17}}.
 \tag{2}
$$

These are lower bounds for a squared-moment method on arbitrary genuine **masked** coefficients, not lower bounds for the signed shell pairing, and not estimates for the unmasked $F=D$. No hypothesis about GRH or about shifted Möbius correlations is used. The low-frequency assertion in (1) is at the central interval around zero only, not at other rational points.

## 1. Each small physical bin has both signs on the true carrier

Place $K+2$ disjoint half-open bins $J_i$ in $[.450N,.490N]$, each with length and successive gap $\asymp N/K$, in increasing order. For instance, split the ambient interval into $K+2$ equal parts and take the middle half of each. We first prove, uniformly in these bins,

$$
 \sum_{m\in J_i}|D_m|^2\gg N/K,\qquad
 \sum_{\substack{m\in J_i\\ \pm D_m>0}} |D_m|
       \gg \frac{N}{K L^7}
 \quad\text{for each choice of sign}.
 \tag{3}
$$

For the squared lower bound use the original giant-prime carrier from the fixed-box example. For each genuine prime $g\in[N^{.500002},N^{.500006}]$ take $m=gk$ with $k\in J_i/g$ odd squarefree. The giant is unique, $k<X$, and the complete coefficient is exactly $-\theta_{B_g}(k)$, where

$$
 B_g=\lfloor.100N^{.50001}/g\rfloor,\qquad
 \theta_{B_g}(k)=\sum_{\substack{b\mid k\\ b\le B_g}}\mu(b).
$$

Indeed all possible $d\ge X$ divide $gk$ as $d=gb$, and for every such $b\le B_g$ the quotient $k/b$ exceeds $t$ even at the lowest endpoint $.450N$ for $m$. The variance computation in [§2 of the fixed-box example](weak-s-type-ii-fixed-prime-box-minor-l2.md#2-the-squarefree-variance-of-the-truncated-möbius-divisor-sum) is uniform with $J_i/g$ in place of its original proportional interval. In detail, put $V_g=N/g$. For each odd squarefree $\ell=[b,b']$ the main squarefree count is $c_{\rm odd}|J_i/g|\prod_{p\mid\ell}(p+1)^{-1}$, with the same uniform error $O(\sqrt{V_g/\ell}\,\tau(2\ell))$ from squarefree expansion and floor counts. The associated Bernoulli second moment is bounded below uniformly as $B_g\to\infty$ by the top interval $B_g/2<\ell\le B_g$ of the centered expansion. It does not depend on the physical bin length. The total floor error in this variance is $O_\eta(\sqrt{V_g} B_g^{2+2\eta})=o(V_g/K)$ uniformly, since $K$ is polylogarithmic, $B_g\ll N^{.000008}$ and $V_g\ge N^{.499994}$. Thus each prime $g$ gives $\gg V_g/K$ and their disjoint support and prime reciprocal sum give the first part of (3).

On true squarefree support $|D_m|^3\le\tau(m)^3=\tau_8(m)$. An interval of length $U\asymp N/K$ at scale $N$ has

$$
 \sum_{m\ {\rm in\ interval}}\tau_8(m)\ll U L^7 +N^{7/8}L^6\ll (N/K)L^7 .
$$

To see this, designate the largest of the eight factors, in at most eight ways. The product of the other seven is $O(N^{7/8})$. With those seven fixed the last factor has $O(U/(\text{their product})+1)$ choices. Sum using seven reciprocal harmonics for the first part and $O(N^{7/8}L^6)$ seven-tuples for the second. Cauchy on $\sum_{J_i}|D_m|^2$ now gives $\sum_{J_i}|D_m|\gg N/(K L^7)$. Finally, the $q=1,\beta=0$ case of [the effective signed major bound](weak-s-type-ii-signed-seam-major-arcs.md) gives

$$
 \left|\sum_{m\in J_i}D_m\right|
 \ll N\exp(-cL^{3/5}(\log L)^{-1/5}).
$$

For a bin $[a,b)$, subtract the two permitted hard lower product walls $N-y=a$ and $N-y=b$ at the same $I_d,t$. This is why no major-arc estimate for an arbitrary product mask is used here. The error is smaller than the absolute mass, proving the two sign bounds in (3).

## 2. A sign-preserving mask with exact vanishing moments

For each $i$ let $\nu_i$ be the nonnegative atomic measure on $J_i$ whose weights are $|D_m|$ at integers where $D_m$ has prescribed sign $(-1)^i$, and zero elsewhere. Every $\nu_i$ has mass $\gg N/(K L^7)$ by (3). Form the $(K+1)$-by-$(K+2)$ real matrix with columns $\big(\int m^r\,d\nu_i(m)\big)_{r=0}^K$. Its maximal minors with columns in increasing order are strictly positive: by multilinear expansion and the Vandermonde determinant each is the integral of $\prod_{a<b}(x_b-x_a)>0$ with $x_a$ in their ordered disjoint support intervals. The alternating cofactors give a null vector $(c_i)$ with signs $(-1)^i$. Normalize it by a positive scalar so $\max_i |c_i|=1$.

Set $F_m=c_i |D_m|$ on the support of $\nu_i$, and zero elsewhere. This is exactly $F_m=\rho_mD_m$ with a nonnegative true multiplier $0\le\rho_m\le1$: the matching coefficient sign is never flipped. The null vector gives the moment equations in (1). By [the sharp ordinary complementary energy](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy), $\sum_m|F_m|^2\ll N$ and hence $\sum_m|F_m|\ll N$. On $|\beta|\le1/(10N)$ one has $|2\pi\beta m|\le\pi/10$. Subtract the Taylor polynomial of degree $K$ inside $\sum_m F_m e(\beta m)$ and use its remainder. This gives $O(N C_0^K/(K+1)!)$ for some absolute $C_0$, which is $O_A(N^{-A})$ for $C_A$ sufficiently large. All coefficients were fixed using the actual divisor sums, not any rational point.

## 3. Incidence of actual shifted products on the critical hits

Choose the two hard prime intervals starting, for example, at $.741X$ and $.716X$, each of length $c_0 X/K$ for a small positive absolute $c_0$. Prime counts there are $\asymp X/(K L)$ by the effective prime number theorem (e.g. [Johnston–Yang, Corollary 1.3](https://arxiv.org/pdf/2204.01980#page=2)); the relative widths are only reciprocal polylogarithms. Their product interval has length $O(c_0 N/K)$, less than every gap between the $J_i$ by choice of $c_0$. Thus the shifted supports from different bins in $T_F(M)$ do not intersect. This remains true after the actual unit restriction for any $h\in\mathcal H_N$.

Choose an index $i_0$ where $|c_{i_0}|=1$. On this bin the complementary terms all have one sign, and the selected actual prime coefficient on the other leg is $-\log v$. Denote by $a_n=|P_n|$ and $b_m=|F_m|\mathbf1_{m\in J_{i_0}}$ the nonnegative weights, and their total masses by $A_1,B_1$. The factorization $n=uv$ in the disjoint prime intervals is unique. We have

$$
 A_1\asymp \frac{N}{K^2L},\qquad B_1\gg \frac{N}{K L^7},
 \qquad \sum a_n^2+\sum b_m^2\ll N.
$$

For each $q\in\mathcal Q$ let $J_q^{\rm hit}=\sum_{n+m\equiv N\bmod q}a_n b_m$. By the same finite identity and [additive-large-sieve incidence](weak-s-type-ii-critical-prime-fixed-selector-logarithmic-barrier.md#1-genuine-weights-with-one-sign-and-a-modulus-with-enough-matches) as for the fixed selector lower,

$$
 \sum_{q\in\mathcal Q}|qJ_q^{\rm hit}-A_1B_1|\ll N^2.
$$

Indeed finite orthogonality removes the product $A_1B_1$ at zero numerator, and Cauchy with the additive large sieve on the distinct nonzero fractions $a/q$ spaced by $\gg1/N$ proves this bound. Therefore all but $O(K^3L^8)=o(\#\mathcal Q)$ primes have $J_q^{\rm hit}\ge A_1B_1/(2q)$. It follows that $\sum_q J_q^{\rm hit}\gg A_1B_1/L\gg N^2/(K^3L^9)$.

The zero offset costs at most $O(N\#\mathcal Q)=O(N^{3/2}/L)$ by the ordinary coefficient energies, which is negligible here. All actual offsets satisfy $|n+m-N|<N/20$ by the stated prime boxes and physical bins. Each nonzero hit therefore occurs in just one $q$ sum. At any hit generated by the selected bin, $|T_F(N+h)|$ equals the nonnegative bin convolution, because no other bin shares its shifted support. This proves

$$
 \sum_{h\in\mathcal H_N}|T_F(N+h)|\gg N^2/(K^3L^9).
$$

The same lower holds for the unit-hit version. To see this, a deleted term at $q$ requires $q\mid m$ and $n\equiv N\bmod q$. The total weight of possible $n$ in one such residue is $O(X)$: for each true $u<q$ there is at most one $v$ in the allowed range below $q$, and the prime count cancels its weight $O(L)$. Each $m<N/2$ is divisible by at most one distinct prime in $\mathcal Q$, so all the deleted mass is $O(X\sum_m|F_m|)=O(N^{3/2})$, still negligible. The single-bin signs and the separation between bins are unchanged by this deletion. Now Cauchy on the $O(N/L)$ hits proves both bounds in (2).

## 4. Scope of the obstruction for the natural pointwise problem

In the exact full signed shell the nonzero hit term, after including the true $\beta$ phase, is

$$
 \sum_{h\in\mathcal H_N} q(h)\,\sigma_N(h)\,T_F(N+h),
 \qquad
 \sigma_N(h)=\int_{-1/(10N)}^{1/(10N)}e(\beta h)\,d\beta
 =\frac1{5N}\operatorname{sinc}\big(h/(5N)\big),
$$

where $\operatorname{sinc}(x)=\sin(\pi x)/(\pi x)$ continuously at zero. The full pairing also has the $h=0$ term weighted by $\sum_q q$ and the **subtracted** zero-numerator base

$$
 |\mathcal Q|\int_{-1/(10N)}^{1/(10N)}P(\beta)F(\beta)e(-N\beta)\,d\beta.
$$

The base is negligible for the constructed multiplier by (1); it cannot be dropped for the natural unmasked $D$ merely using the effective stretched-exponential pointwise $q=1$ bound in §1, because that assertion has a $\#\mathcal Q\asymp\sqrt N/L$ factor here. The actual [full-vs-centered comparison](weak-s-type-ii-critical-prime-global-shift-rows.md) changes the entire shell by only $O(N/L^{3/2})$ when applicable, but does not independently remove this base.

Cauchy would give $o(N)$ for the hit term from a squared-moment bound $o(N^2L)$, since $q(h)\ll X$, $|\sigma_N(h)|\ll N^{-1}$ and there are $O(N/L)$ hits. The bounds (2) disprove such a uniform squared-moment estimate using only a genuine mask, the actual signs/units and even the strong central bound (1). They do not evaluate the sum of the signed hit offsets: the different signs of the retained bins can cancel there. Neither the signed full-shell covariance at these witnesses, nor the natural unmasked pointwise bound, nor weak S is settled by this construction.
