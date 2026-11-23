# An unconditional minor bound on a true rough giant mixed slice

Keep the actual squarefree above-BV mixed coefficient $M_>(m)$ with its sign before subtraction in the [largest-prime mixed proof](r66-spectral-largest-prime-mixed-strip.md), and the genuine polynomials and arcs of the [central bridge](r64-spectral-pointwise-major-central-bridge.md). Thus $N$ is even, $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ with fixed $B>B_0>0$, $m\in V=[N/3,2N]$, and the left interval is an arbitrary hard central $I\subset (N/2,9N/16]$. Its bounded weight $\omega$ is the same one as in the bridge. Keep the actual giant prime $p>\sqrt m$ and its unique cofactor $k=m/p$. Require $k$ to be **composite**, all its prime factors at least a real $Z>2L^B$, and $k\ge\sqrt{2N}e^{-w}$, where $w\ge0$ is arbitrary. There is no restriction on the number of these rough factors or on the total Möbius parity. Write $A(m)$ for $M_>(m)$ on exactly this selector and zero elsewhere. Then, unconditionally and uniformly in these parameters,

$$
 \int_{\mathfrak E}\left|P_{I,\omega}(\theta)
                      \widehat A(\theta)e(-N\theta)\right|\,d\theta
 \ \ll_{B,B_0,\|\omega\|_\infty}
       \frac NL
       \left(\frac{(1+\min(w,B_0\log L+1))^3}{\log Z}\right)^{1/2}
 \tag{1}
$$

for every measurable $\mathfrak E\subseteq\mathbb R/\mathbb Z$. In particular this is a bound for the signed coefficient on the original, unchanged $\mathfrak m$, with **no prime-progression GRH input on either leg**. It is uniform in $I$. Choosing $Z=\exp(L_2^{3+\epsilon})$, for any fixed $\epsilon>0$, makes the bound $O((N/L)L_2^{-\epsilon/2})$ over the entire genuine giant cofactor window. In the near-balanced sector $w=o(L_2^{1/3})$ it is already $o(N/L)$ at the genuinely polylogarithmic floor $Z=L^{B+1}$. These imply $o(\Sigma(N))$ in the original $L/N$ Hardy normalization, since $\Sigma(N)$ is bounded below by a positive constant on even $N$.

The earlier giant result bounded the true full arithmetic coefficient unconditionally and obtained its minor estimate by a historical prime-progression GRH major comparison. Here the same mixed coefficient on the stated rough subset has a direct unconditional argument, not a retuning of the major set or a numerical change of a conditional exponent. The selector does not estimate the omitted prime $k$ block, partners without a giant prime, the prime marginal under this mask, or Hypothesis S.

## 1. Exact coefficient before taking squares

On this squarefree support the [exact largest-prime identity](r66-spectral-largest-prime-mixed-strip.md#1-exact-representation-after-extracting-the-largest-prime) is $M_>=-\Xi_D-M_\le$. The prime $p>\sqrt m$ exceeds $D,H_0$ for all large $N$ and never enters the sharp sums on the divisors at most $D$. If $k\le D$, there is no mixed coefficient by that identity. Suppose $k>D$. Since $k<\sqrt m\le\sqrt{2N}$, a proper divisor $e\mid k$ satisfies $e\le k/Z<D$; the only omitted divisor in either sharp sum is $k$. For composite squarefree $k$ the full divisor sums of $\mu(e)$ and $\mu(e)\log e$ are zero. Thus

$$
 F_{0,D}(k)=-\mu(k),\qquad
 F_{1,D}(k;m)=-\mu(k)\left(1-\frac{2\log k}{\log m}\right),
 \qquad -\Xi_D=F_{0,D}F_{1,D}.
 \tag{2}
$$

This step uses the composite condition, not merely roughness.

For $M_\le$, the LCM $h=abc\le H_0$ divides $k$, because $p>H_0$. The true mixed gate $D<\min(ab,ac)<\sqrt m$ forces $h>D$, hence $h=k$. As $ab,ac\mid k$, the same proper-divisor argument forces both $ab=ac=k$, hence $a=k,b=c=1$. Its coefficient is $1-2\log k/\log m$, and it occurs exactly when $k\le H_0$. Consequently on the stated selector the entire actual above-$H_0$ coefficient is precisely

$$
 M_>(m)={\bf1}_{k>H_0}\frac{\log(p/k)}{\log m}.
 \tag{3}
$$

There is no additional $\mu(k)$ in (3). The identity already accounts for mixed terms with $p$ in the LCM, which cannot simply be omitted in the original above-$H_0$ mixed sum. In particular a prime $k$ cannot be silently included by this proof.

## 2. Two ordinary coefficient energies

Set $w_*=\min(w,B_0\log L+1)$. The nonzero right support has $k<\sqrt{2N}$, $k>H_0$, $k\ge\sqrt{2N}e^{-w}$, so its short cofactor interval has logarithmic width at most $w_*$. There $p/k=m/k^2\le e^{2w_*}$ and $\log m\asymp L$, so $|M_>(m)|\ll(1+w_*)/L$ by (3). The standard [elementary uniform upper rough count](weak-s-type-ii-critical-prime-stretched-rough-boundary-second-moment.md#1-absolute-dyadic-rough-count-including-the-small-endpoint) bounds the reciprocal mass of the nonunit rough integers on this interval by $O((1+w_*)/\log Z)$. Indeed cover the interval by $O(1+w_*)$ ordinary dyads, taking the larger of its lower endpoint and $Z$ as the start; a nonunit $Z$-rough integer is at least $Z$. If $Z>\sqrt{2N}$ the right support is empty.

For each such $k$, all possible $p$ are at most $2N/k$; the prime upper count is $O(N/(kL))$ since $k<\sqrt{2N}$. This uses only the elementary upper bound for the total prime count, not any progression or distribution in a narrow window. The largest prime decomposition is unique, and coefficient squares have no multiplicity. Parseval therefore gives

$$
 \|\widehat A\|_2^2
 \ll \frac{N(1+w_*)^3}{L^3\log Z}.
 \tag{4}
$$

The true left polynomial has $\|P_{I,\omega}\|_2^2\ll NL$ by Parseval and the same prime upper count, uniformly for the sharp $I$. Apply Cauchy to the restriction to $\mathfrak E$, or to the whole torus. This proves (1) with the original phase and exact actual right weight. No comparison of major arc approximations or left error is needed.

The new selector has occupied genuine sum-line examples. At a separate large scale $X$, choose distinct primes $u,v$ near $X^{1/4}$ and $0.60X^{1/4}$, a prime $p$ near $0.75\sqrt X$, and a prime $n$ near $0.55X$, using sufficiently narrow fixed proportional intervals and the ordinary prime number theorem. Put $k=uv$ and $N=n+pk$; then $N$ is even, $N\asymp X$ with ratio arbitrarily close to one for fixed sufficiently narrow intervals, $n\in(N/2,9N/16]$, $m=pk\in V$, and $p>k>H_0$. Equation (3) is strictly positive, and $k\ge\sqrt{2N}e^{-1}$ with room. This has the indicated roughness even at $Z=\exp(L_2^{3+\epsilon})$. Taking instead three distinct rough primes near fixed positive multiples of $X^{1/6}$ with product near $0.60\sqrt X$ gives the other total parity. These are occupancy examples, not aggregate signed lower bounds.
