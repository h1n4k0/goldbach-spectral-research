# A logarithmic lower bound for arbitrary fixed selectors on the signed critical shell

Use the exact $N=2^j$, $X=\sqrt N$, $L=\log N$, prime boxes $[.740X,.745X]$ and $[.715X,.720X]$, $I_d=[X,.100N^{.50001}]$, $t=N^{.49999}$ and $y=9N/16$ from [the surviving ordinary carrier](weak-s-type-ii-ordinary-energy-survives-signed-saddles.md). Fix $A>0$ and any fixed finite collection of the true count saddles there, with least prime cutoff $W=L^A$. Below a product mask always keeps the complete original signed coefficient at each selected $m$; it cannot change the sign or select any of that coefficient's constituent divisor terms.

Put $\mathcal Q=\{q\text{ prime}:.8X\le q\le .9X\}$, $\mathcal B=[-1/(10N),1/(10N)]$, and use the exact full signed pairing $\mathcal I$ and double-centered pairing $\mathcal C$ of [the critical shell](weak-s-type-ii-critical-prime-least-prime-boundaries.md). Fix $\epsilon>0$. For every sufficiently large $N=2^j$ (with threshold depending on the fixed saddle collection, $A$ and $\epsilon$), for each pairing separately there are genuine $0$–$1$ prime-pair selectors $E(u,v)$ and $0$–$1$ product masks $\rho_m$ inside the true saddle carrier for which

$$
 \big|\mathcal I(P_E,\rho D)\big|\gg_\epsilon \frac{N}{L^{1+2\log 2+\epsilon}}
 \quad\text{or, respectively,}\quad
 \big|\mathcal C(P_E,\rho D)\big|\gg_\epsilon \frac{N}{L^{1+2\log 2+\epsilon}} .
 \tag{1}
$$

The choices for the two pairings may differ. The masks may be designed once using the target and the fixed shell, but they do not depend on the subsequently summed modulus, numerator or integration point. The integrals and signed sums over the **whole** shell are taken before the absolute value in (1). In particular no uniform $O(N/L^{B_*})$ bound with a fixed $B_*>1+2\log 2$ holds over this selector class. This is unconditional; it neither rules out $o(N)$ nor supplies any signed lower for the unmasked statistic, fixed separated $E$, or weak S.

## 1. Genuine weights with one sign and a modulus with enough matches

Put $L_2=\log L$. Choose fixed $0<\eta\le\min(1,\epsilon/(2\log 2))$, $z=\exp(10/\eta)$, $\delta=1-1/(8z)$ and $Z=\exp(L^\delta)$. Append the additional true count saddle for the band $[2,Z)$ to the prescribed finite collection. Let $D_{\mathrm{car}}$ retain exactly the products in the enlarged finite list of saddles (and with the stipulated least prime cutoff) in the coefficient carrier $m=gk_0$, with $g$ prime in $[N^{.500002},N^{.500006}]$ and $k_0$ odd squarefree in $[.450N/g,.490N/g]$. The cited surviving-energy theorem applies to this enlarged, still fixed collection. Thus $\sum_m|D_{\mathrm{car},m}|^2\gg N$, and its ordinary upper bound is $O(N)$.

Write $\omega_{<Z}(m)$ and $\omega_{\ge Z}(m)$ for the two counts of distinct prime divisors. The appended saddle gives $\omega_{<Z}(m)\le (2\delta+\eta)L_2$ for sufficiently large $N$: its center is $2\log(\log Z/\log 2)=2\delta L_2+O(1)$ and its window width is $o(L_2)$. Every actual coefficient on squarefree support satisfies $|D_{\mathrm{car},m}|^2\le 4^{\omega(m)}$. Rankin's elementary positive bound therefore shows that the squared energy with $\omega_{\ge Z}(m)>\eta L_2$ is at most

$$
 L^{(2\delta+\eta)\log 4-\eta\log z}
   \sum_{m\le N}(4z)^{\omega_{\ge Z}(m)}
 \ll_z N L^{(2\delta+\eta)\log 4-\eta\log z+(4z-1)(1-\delta)} .
$$

To obtain the inequality, expand $(4z)^{\omega_{\ge Z}(m)}$ as the sum of $(4z-1)^{\omega(h)}$ over squarefree divisors $h$ supported on primes $\ge Z$, bound the count of multiples of $h$ by $N/h$, and enlarge the positive sum to the Euler product $\prod_{Z\le p\le N}(1+(4z-1)/p)$. The prime harmonic estimate $\sum_{Z\le p\le N}1/p=(1-\delta)L_2+O(1)$ gives the exponent displayed. It is less than $-5$ by the fixed choices of $z,\delta,\eta$. No unit or squarefree mask has been removed from a signed coefficient sum: the enlargement is only for the nonnegative upper bound on a square.

Discarding this high-count tail therefore still leaves energy $\gg N$. On the retained products $\omega(m)\le(2\delta+2\eta)L_2$, and hence $|D_{\mathrm{car},m}|\le L^{2\log 2+\epsilon}$. Energy divided by this upper bound gives true absolute mass $\gg_\epsilon N/L^{2\log 2+\epsilon}$. The coefficients are real. Retain whichever one of the two coefficient signs carries at least half this absolute mass, and let $b_m$ denote the absolute values on that retained support. Replacing $b_m$ by the genuine same-sign coefficients only multiplies all the pairings below by one constant sign.

Let $a_n=\log v$ when $n=uv$ comes from the complete two prime boxes, and zero otherwise. The two boxes are disjoint, so the ordered factorization is unique. Their products lie in $[.5291N,.5364N]\subset (N/2,9N/16)$ and are odd, so all original prime cuts and units are respected. The true sign on the prime leg is one constant minus, and we temporarily use $a_n\ge0$. Set

$$
 A_1=\sum a_n\asymp N/L,\qquad B_1=\sum b_m\gg N/L^{2\log 2+\epsilon}.
 \tag{2}
$$

Here the first bound is the prime number theorem in fixed proportional intervals. Also $\sum a_n^2\ll N$ by the prime counts and $\sum b_m^2\ll N$ by the actual ordinary estimate. All $n,m$ now used are units modulo *every* shell prime: $u,v<q$, while $g>q$ and $k_0<X/2<q$. No shell prime divides $N=2^j$.

For each $q$ put $J_q=\sum_{n+m\equiv N\pmod q}a_n b_m$. Define $A(\alpha)=\sum a_n e(n\alpha)$ and $B(\alpha)=\sum b_m e(m\alpha)$, with $e(x)=e^{2\pi i x}$. Exact finite orthogonality gives

$$
 qJ_q-A_1 B_1
   =\sum_{a=1}^{q-1} A(a/q)B(a/q)e(-Na/q).
$$

The fractions from these primes with nonzero numerators are spaced by $\gg 1/N$ on $\mathbb R/\mathbb Z$. The [additive large sieve, Montgomery–Vaughan Theorem 1](https://backend.production.deepblue-documents.lib.umich.edu/server/api/core/bitstreams/5adbb05b-05d0-4779-b1fd-304ec1ec257a/content#page=1), applied separately to each genuinely bounded coefficient support of length at most $N$, and Cauchy–Schwarz give

$$
 \sum_{q\in\mathcal Q}|qJ_q-A_1B_1|\ll N^2.
 \tag{3}
$$

There are $\gg X/L$ shell primes. Thus by (2)–(3) some $q_0\in\mathcal Q$ satisfies $q_0J_{q_0}\ge A_1 B_1/2$; in fact at most $O_\epsilon(L^{1+2\log 2+\epsilon})$ primes can fail this inequality. The construction did not assume a pointwise lower bound for a prime hyperbola.

## 2. A lower for the exact congruence slice of the whole shell

For a pair $n,m$ put $h=n+m-N$. Its full numerator coefficient at $q$, leaving out $e(\beta h)$, equals $q\mathbf 1_{q\mid h}-1$. For the double-centered pairing the corresponding coefficient is

$$
 q\mathbf1_{q\mid h}
 -\frac{q^2}{(q-1)^2}
 +\frac{q}{q-1}
        \big(\mathbf1_{n\equiv N\pmod q}+\mathbf1_{m\equiv N\pmod q}\big).
 \tag{4}
$$

Indeed the centered residue mass of the single integer $n$ on nonzero residues is $\mathbf1_{r=n}-1/(q-1)$, extended by zero at $r=0$, and likewise for $m$. Expanding $q$ times their product with residues adding to $N$ gives (4): two possible missing unit rows occur at $r=0$ and $r=N$, distinct since $q\nmid N$. This identity retains the exact centered signs, not a per-alias recentering.

On all pairs with $q_0\mid h$ the sum of the full coefficients over $\mathcal Q$ is at least $q_0-|\mathcal Q|$, and the sum of coefficients in (4) is at least $q_0-4|\mathcal Q|$. Both are $\gg q_0$. Also $|h|<N/10$ on the actual products and $\operatorname{Re}e(\beta h)\ge1/2$ throughout $\mathcal B$. Thus, in either pairing, the **whole shell** contribution $S_{\mathrm{hit}}$ of pairs satisfying $q_0\mid h$, evaluated with the nonnegative weights $a_n,b_m$, is real and satisfies

$$
 S_{\mathrm{hit}}\gg \frac{q_0 J_{q_0}}N
       \gg \frac{A_1 B_1}N
       \gg_\epsilon \frac{N}{L^{1+2\log 2+\epsilon}}.
 \tag{5}
$$

The real assertion follows also from the even integration interval and the real kernels. This is an intermediate positive two-variable slice, not itself claimed to be a product of two separately allowed selectors.

## 3. Realize the obstruction with separately legal masks

Independently color each residue modulo $q_0$ red or blue with probability $1/2$. Select $n=uv$ into the prime polynomial iff its residue is red, and select $m$ into the one-sign coefficient carrier iff $N-m\bmod q_0$ is blue. Both masks are real $0$–$1$ and depend only on their own variables; after the colors have been chosen they remain fixed at all $q,a,\beta$. At a pair with $q_0\mid h$ the colors are incompatible and it is never included. Otherwise the two residues are distinct, and the pair is included with probability $1/4$.

Let $S_0$ be either the full or centered **signed whole-shell** pairing on the uncolored nonnegative supports of §1, and $S_{\rm color}$ its value on the two selected supports. Both pairings are bilinear in the underlying coefficients even after centering. Consequently

$$
 4\,\mathbb E S_{\rm color}=S_0-S_{\mathrm{hit}}.
$$

This proves $S_{\mathrm{hit}}\le |S_0|+4\max |S_{\rm color}|$. For at least one legitimate choice (the uncolored supports or a fixed coloring), (5) therefore forces the respective bound (1) after restoring the original two fixed signs. The result only exploits the freedom to choose arbitrary fixed masks; it does not assert that the original dense nonprincipal covariance fails to cancel, or that these choices exhaust its relevant selectors.
