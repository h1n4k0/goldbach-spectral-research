# Joint medium-prime parity tests and the limit of coherent transport

**Scope.** An unconditional statement about a fixed-dimensional family of genuine factor-count tests on polynomial prime bands. In every central cell the actual shifted-prime reservoir has all joint parity signatures, including simultaneous negative signs. The original coherent transport changes its joint law at the scale of the erased prime-partner mass. A different artificial transport can preserve even the full collection of individually tagged factors. This does not measure total Möbius parity, bound the genuine prime-pair mass below, or resolve Hypothesis S.

Use the notation of the [coherent transport](spectral-coherent-divisor-transport-barrier.md) and [single-tag test](spectral-tagged-parity-transport-test.md). Fix integers $K,k\ge2$ and real $J\ge1$. Let $N$ be a sufficiently large even integer, $L=\log N$, $S=\mathfrak S(N)$, $m=N-n$ and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Use the same partition of $(N/2,9N/16]$ into half-open cells $I$ of length $H=N/(16\lceil L^J\rceil)$.

Choose fixed disjoint real intervals $[\alpha_i,\gamma_i)\subset(0,.41]$, $i=1,\ldots,k$, such that $\sum_i\gamma_i\le .45$, and such that $\sum_i\log(\gamma_i/\alpha_i)$ is below a sufficiently small absolute positive constant. This allows any fixed $k$, including a first interval starting at $.40$ and $k-1$ additional intervals of small positive total upper exponent. Define

$$
 T_i=\{r\text{ prime}:N^{\alpha_i}\le r<N^{\gamma_i},\ r\nmid N\},\qquad
 h_i=\sum_{r\in T_i}\frac1{r-1},\qquad h=\sum_i h_i.
$$

Each $h_i$ tends to $\log(\gamma_i/\alpha_i)>0$ by Mertens, since only $O(1/\alpha_i)$ primes in its band can divide $N$. Choose $\beta>0$ fixed and sufficiently small after these intervals and $K$ are chosen, in particular less than $\min_i\alpha_i$ and $1/2000$. Put $z=N^\beta$ and

$$
 V_z=\prod_{\substack{p<z\\p\nmid N}}\left(1-\frac1{p-1}\right)\asymp S/(\beta L),\qquad
 \omega_i(m)=\#\{r\in T_i:r\mid m\},\qquad
 \boldsymbol\pi(m)=\big((-1)^{\omega_i(m)}\big)_{i=1}^k.
$$

The reservoir $\mathcal C_I$ is the genuine prime $n$ in $I$ for which $m$ is squarefree, has no prime factor $<z$, and has more than $K$ distinct prime factors. For every subset $A\subseteq\{1,\ldots,k\}$, let $C_I(A)$ be its actual $\lambda$-mass with parity negative exactly in the coordinates of $A$. Uniformly in $I,N,A$,

$$
 C_I(A)\asymp H V_z \prod_{i\in A}h_i .                         \tag{1}
$$

Both bounds hold even after restricting to the exact count vector $\omega_i=1$ for $i\in A$ and $\omega_i=0$ otherwise. Here the upper bound for the exact vector follows because it is a subset of the indicated parity vector. The comparability constants can be absolute after the parameter choices; the threshold for $N$ may depend on all fixed parameters. No independence of the full arithmetic counts is asserted.

## 1. Joint forced incidences on the actual shifted primes

For fixed $A$, write $h_A=\prod_{i\in A}h_i$, with value one for the empty set. Consider the first mixed moment

$$
 M_A(I)=\sum_{\substack{n\in I\\m\ z\text{-rough}}}
           \lambda(n)\prod_{i\in A}\omega_i(m),
$$

where $z$-rough means no prime factor $<z$. Expand the product by choosing exactly one prime from each required band, with product $c$. The bands are disjoint, so the tuple is uniquely identified by $c$, which is a unit modulo $N$ and is at most $N^{.45}$. The empty tuple has $c=1$.

For each $c$, apply the dimension-one fundamental sieve to the true positive prime-only sequence in $I$ satisfying $c\mid m$, with the small-prime restrictions $p<z,\ p\nmid N$. At a squarefree sieve modulus $d\le D=N^{.05}L^{-B}$ the actual coherent progression is $n\equiv N\bmod cd$ with reduced residue. The map $(c,d)\mapsto cd$ is injective for this fixed $A$: the prime factors in $c$ are in the tag bands and those of $d$ are below $z$. Its range lies below $\sqrt N L^{-B}$. Thus [maximal Bombieri–Vinogradov](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=206) bounds the total error of replacing progression counts by $H/(\varphi(c)\varphi(d))$, over all these tuples and sieve divisors for one cell, by $O_{A_0}(NL^{-A_0})$ for every fixed prescribed $A_0$ on taking $B$ large. Each cell is a difference of two real prefixes; prime powers cost $O(D_{\rm BV}\sqrt N L)$ in the aggregate, where $D_{\rm BV}=\sqrt N L^{-B}$. Every actual prime $n$ in the central range is a unit, since $N/2<n<N$.

The local density at a sifted prime is $1/(p-1)$, so the common Euler product is $V_z$. The [fundamental lemma, Corollary 19](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/) applies with $s=\log D/\log z\to .05/\beta$. Choose $\beta$ so small that its relative error is at most $1/2$. This choice is independent of the cell and of $J$; the arithmetic remainder is already aggregated over distinct moduli. Since $\sum_c1/\varphi(c)=h_A$, on taking $A_0>J+5$ we obtain

$$
 \tfrac13 H V_z h_A \le M_A(I)\le 2 H V_z h_A.                \tag{2}
$$

Here the $h_i$ have fixed positive limits, so all finitely many $h_A$ are bounded below in terms of the fixed intervals. The standard comparison $V_z\asymp S/(\beta L)$ is the Mertens and Euler product calculation in the transport proof.

## 2. Excluding extra tags controls all exact signatures

For each forced tuple for $A$ count every extra tag prime $r$ not already in that tuple, provided $cr\mid m$. Denote the total $\lambda$-weighted incidence over the $z$-rough $m$ by $E_A(I)$. This is deliberately an upper bound, without any squarefree or total-factor gate. Put $Q=cr\le N^{.86}$ and $U=H/Q$. In the equation $m=Qu$ the integer $u$ runs over the exact cell interval of length $U\ge N^{.14-o(1)}$. Take $Y=U^{1/100}$ and sieve level $U^{1/2}$. Then $z<Y$ by our restriction on $\beta$. Sieve the primality form $n=N-Qu$ at every prime $p<Y$ and the roughness condition $u\not\equiv0\bmod p$ at $p<z$, $p\nmid N$. All original points pass: $n$ is a true prime $>Y$ and $Q$ has no factors below $z$.

The primality root is absent at $p\mid Q$ and is a single class otherwise. The extra root is distinct at all primes where it is present, because these are coprime to $NQ$; in particular there is no second root at $2$. The fixed dimension-two upper sieve therefore gives main product at most

$$
 \ll (Q/\varphi(Q))\,V_z/\log Y .
$$

Each squarefree sieve modulus has CRT error $O(2^{\omega(d)})$, so the total error per $Q$ is $O(U^{1/2}\log(2U))$. The constants are absolute since $\log U\gg L$ uniformly. After weighting by $\lambda(n)\le L$, the main contribution is $O(HV_z/\varphi(Q))$. The sum of $1/\varphi(Q)$ over the forced tuples and the distinct extra primes is at most $h_A h$: for distinct choices the reciprocal factors multiply, and dropping distinctness from this *positive* product-sum only increases it. For the additive errors, a given squarefree $Q$ has at most two representations for the fixed $A$: when the extra prime lies in a required band with two members present there are two choices, and otherwise its extra band and all chosen primes are determined. The errors sum to at most $O(N^{.93}L^2)$ using

$$
 H^{1/2}\sum_{Q\le N^{.86}}Q^{-1/2}\ll N^{.93}.
$$

Consequently, for an absolute $B_0$ independent of $k$ and the particular bands in the exponent envelope,

$$
 E_A(I)\le B_0 H V_z h_A h+O(N^{.93}L^2).                    \tag{3}
$$

The parameter smallness in the statement can, for example, enforce $h<1/(100(1+B_0))$ for large $N$; no circular choice is needed because the upper sieve constant used a fixed exponent envelope and fixed dimension.

For a given $m$ with all demanded tags, if it does not have the exact target count vector, every forced tuple has at least one unused tag prime. The exact-vector indicator is therefore at least the forced-tuple count minus the forced-tuple-plus-extra count, pointwise. At an integer with a missing required tag both counts are zero; at an integer with the exact vector the first count is one and the second zero. This also covers the empty pattern: the first count is one and the second counts all tags. It follows from (2)–(3) that the true mass of every exact target vector on the rough sequence is at least $c_0 H V_z h_A$ for an absolute $c_0>0$.

Now delete squareful rough $m$ at raw cost $O(NL/z)$ by counting multiples of a prime square with base at least $z$. Delete squarefree rough integers with at most $K$ factors at the cost from the coherent-transport proof:

$$
 O_K\!\left(SH L^{-1}(1+\log(1/\beta))^{K-1}
                 +N^{1-1/(4K)}L^2\right).
$$

These losses are on the genuine exact-vector **indicator**, not on a multiplicity-weighted count. Choose the fixed $\beta$ even smaller, after the bands and $K$, so that the first term is less than a fixed small fraction of $H V_z\min_A h_A$; this is possible because $\beta(1+\log(1/\beta))^{K-1}\to0$. All power or BV errors are negligible relative to that mass for each fixed $J$. This proves the exact-vector lower bound on $\mathcal C_I$. The parity-vector upper bound follows from (2), since whenever parity is negative in every required band the forced count is at least one. This proves (1).

## 3. The jointly observable defect and a transport preserving the full tag data

The signature of every true prime partner $m$ is the all-positive vector, since $m\asymp N$ is above all tag bands. Let $P_I$ be its actual prime-partner $\lambda$-mass in $I$, $C_I=\sum_A C_I(A)$, and $\nu_I(A)=C_I(A)/C_I$. The R40 uniform transport modifies the entire signature measure by exactly

$$
 P_I\,(\nu_I-\delta_{\emptyset}),
$$

where $\delta_{\emptyset}$ stands for unit mass at the all-positive pattern. Its total variation, in the convention of half the $\ell^1$ distance of the mass vectors, equals $P_I(1-\nu_I(\emptyset))\asymp hP_I$. For the lower bound, sum the disjoint singleton-negative patterns using (1). For the upper bound, a non-all-positive pattern has at least one tag, whose mass is at most $\sum_i M_{\{i\}}(I)\ll HV_z h$ by (2). The denominator $C_I\asymp H V_z$ follows from the empty exact-vector lower bound and (2) with $A=\emptyset$. This detection is on the scale of the genuine prime-partner mass when it is present; it is not a proof that it is present.

In contrast, distribute $P_I$ only onto the actual high-factor reservoir with the **exact all-zero count vector**. Its mass is $\asymp HV_z$, so the cap $1+O(\beta)$, the exact cell totals, and the coherent and squarefree preservation of the earlier transport remain valid. Both removed and receiving points have the identical list of tagged divisors: the empty list. Thus every bounded function of those individually present tagged primes, including the full joint signature and all its Walsh moments, is preserved exactly on each complete cell. For a prefix within a cell the corresponding perturbation has absolute value at most $\|f\|_\infty P_I$ for such a test $f$, since all moved points have the same test value. The pointwise signed composite coefficient for splits with $b\le\beta$ is also unchanged: every receiving squarefree composite has no divisor between $1$ and $z$, so its complete long sum is affine and zero.

This bound applies to each prescribed fixed finite dimension satisfying the exponent and harmonic-mass conditions; it does not cover a tag family whose forced products pass the level of distribution, or growing dimension at fixed $\beta$. It gives neither control of the actual sign $\mu(m)$ nor an obstruction to using that sign. It specifies a tested family of authentic signed observables which detects one transport but can all be preserved by another.
