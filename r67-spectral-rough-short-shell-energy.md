# Rough short-shell energy for the even part of the above-BV mixed strip

**Scope.** The [integrated short-cutoff theorem](r66-spectral-integrated-short-cutoff.md) treats the true mixed coefficient on squarefree partners with a large prime, for every fixed $\gamma<2/3$ without a parity restriction and every fixed $\gamma<1$ on the odd parity. We increase the all-parity range to every fixed $\gamma<3/4$. The new input is that the true signed sharp primitive on the other parity is supported on a short log shell. Combining its rough-cofactor energy with the earlier **signed** integrated energy improves the product estimate. This is not an asymptotic or a bound on the remaining smaller-largest-prime mixed term, a masked prime marginal, the exterior, or Hypothesis S.

Keep exactly the preceding notation and masks: $N$ even, $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ for fixed $B>B_0>0$, $V=[N/3,2N]$, and the same historical major arcs at $Q=N^{1/1000}$ and complement $\mathfrak m$. Put $s=L^\gamma$, $P_*=\sqrt N e^{-s}$, and let $A(m)=M_>(m)\mathbf1_{P^+(m)>P_*}$ on squarefree $m\in V$, zero otherwise. Here $M_>$ is the actual above-$H_0$ mixed strip coefficient, before its minus sign in the exact global marginal decomposition. For the same true left prime test $P_{I,\omega}$ on every central hard interval $I$, with weight of uniformly bounded supremum and variation, we prove

$$
 \begin{split}
  \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
    &\ll_{B,B_0,\gamma}\Sigma(N)|I|
        \frac{s^{4/3}L_2^2+sL_2^6}{L^2}+N^{.76},\\
  \left|\int_{\mathfrak m}P_{I,\omega}(\theta)
                    \widehat A(\theta)e(-N\theta)d\theta\right|
    &\ll_{B,B_0,\gamma}\Sigma(N)|I|
        \frac{s^{4/3}L_2^2+sL_2^6}{L^2}+N^{1-10^{-4}} .
 \end{split}                                                    \tag{1}
$$

The first bound is unconditional, the second uses historical Dirichlet GRH for the two prime progression sums at $q\le Q$ only. In particular the Hardy-normalized $L/N$ error is $o(\Sigma(N))$ for $0<\gamma<3/4$. The stronger odd-parity range $\gamma<1$ of the preceding theorem is unaffected.

## 1. Exact parity and cell estimates

Write the unique largest prime on this support as $p>P^+(k)$, $m=pk$, $p>P_*$. By the preceding exact representation only $D<k\le2\sqrt N e^s$ contributes, and $M_>=-\Xi_D-M_\le$. The low mixed subtraction already has a uniform-in-$p$ majorant in each physical $x=pk$ cell of reciprocal sum $O(s L_2^5/L)$, before multiplying by $k/\varphi(k)$, by Section 3 of the integrated theorem. We keep this majorant. Prime $k>D$ contributes $O(s/L)$ to the sharp-product reciprocal sum (its true sharp product is one); $k=1$ contributes nothing. We may now work with composite squarefree $k$.

For $\mu(m)=-1$ use the integrated theorem's stronger bound. In the remaining case $\mu(m)=+1$, one has $\mu(k)=-1$ exactly. For $T_1=k/D$ and $T_2=D/p=Dk/x$, equation (5) of the [subpower proof](r66-spectral-subpower-largest-prime.md) gives

$$
       F_{0,D}(pk)=S_k(T_1^-)-S_k(T_2).
                                                               \tag{2}
$$

In this notation $S(T_1^-)$ is the strict cutoff and $S(T_2)$ the weak cutoff. We also use the preceding exact integrated identity

$$
 F_{1,D}(pk;x)=a(x)F_{0,D}(pk)
          +\frac{2}{\log x}\bigl(\mu(k)J_k(T_1)-J_k(T_2)\bigr),
 \qquad a(x)=\frac{\log(x/D^2)}{\log x}=O(L_2/L),
                                                               \tag{3}
$$

where $J_k(T)=\int_1^T S_k(t)\,dt/t$ for $T\ge1$ and zero below 1. Here $T_1/T_2=x/D^2$, so $\log(T_1/T_2)=2B\log L+O(1)>0$. These are identities for the unchanged sharp factors, including divisors containing $p$ when $p\le D$.

Partition the physical $x$ interval and the allowed $k$ range as before into hard geometric cells of relative width at most $\eta=s^{-1/2}$. Write $K<k\le K'$, $w=\log(K'/K)$ for one arithmetic cell; taking either actual endpoint convention changes only the floor counts. We may add the single cut $k=10D L^{2B}$. Below that cut the log length is $O_B(L_2)$; the preceding integrated cell estimate bounds the whole product there by $O_B(\sqrt{s}L_2/L)$ in reciprocal sum, plus power-small errors. Above it $T_1,T_2>1$ uniformly, even at the physical endpoints. Fix one physical cell for the following bounds. On each $k$ cell $T_1,T_2$ are at most $Z=10e^{2s}$ and each varies in a multiplicative shell of width $O(\eta)$. From the earlier primitive and integrated-energy estimates there are uniform-in-$p$ majorants for $|F_{0,D}|$, $|F_{1,D}|$ with squared reciprocal sums bounded respectively by $O(w+Z^2/K)$ and

$$
                  O\bigl(L^{-2}(s w+s^2 Z^2/K)\bigr).           \tag{4}
$$

They have size $N^{o(1)}$ on their support; all divisor counts and logarithms used in making them have this size. One can always use a majorant for a subset by applying the bound to the square first and then enlarging the positive sum.

## 2. Small least prime of the true cofactor

Set $U=s^{1/3}$ and $G=e^U$. Suppose $\ell=P^-(k)\le G$ and write $k=\ell v$, so $\ell$ is prime and $(\ell,v)=1$ on the actual squarefree support. Separating divisors of $k$ according as they contain $\ell$ gives the exact identities

$$
 S_k(T)=S_v(T)-S_v(T/\ell),\qquad
 J_k(T)=J_v(T)-J_v(T/\ell)=\int_{T/\ell}^T S_v(t)\frac{dt}{t}.
                                                               \tag{5}
$$

The first also holds with strict cutoffs on both right terms. In the second, extend the integrand by zero below 1. At a fixed $\ell$, the $v$ cell is $K/\ell<v\le K'/\ell$ and has the same log length $w$. The earlier squared moving-primitive bound applies to each $S_v$ with threshold $T_j$ or $T_j/\ell$; this also includes an endpoint crossing 1. Its reciprocal sum over $v$ is $O(w+\ell Z^2/K)$. For each $J_k(T_j)$ in (3), the integration interval in (5) lies in a fixed interval in $\log t$ of length $O(\log\ell+\eta)$. By Cauchy in this fixed integral and the fixed-primitive bound on $v$, its squared reciprocal sum is $O((\log\ell)^2(w+\ell Z^2/K))$.

Use Cauchy for the product in (2)–(3), and $1/k=1/(\ell v)$. For each fixed $\ell$ its reciprocal contribution is bounded by

$$
        O_B\!\left(\frac{L_2+\log\ell}{\ell L}
                                     (w+\ell Z^2/K)\right).
$$

This uses the actual least-prime class before the positive upper bound; there is no summation over possible $\ell$ inside a squared coefficient. Mertens and Chebyshev give $\sum_{\ell\le G,\ \ell\ {\rm prime}}(L_2+\log\ell)/\ell\ll U+L_2^2$. Summing the endpoint terms costs at most $N^{-1/2+o(1)}$ per cell since $G,Z=N^{o(1)}$ and $K\ge D$. Sum all $k$-cell widths $O(s)$. The resulting small-least-prime reciprocal bound in the fixed physical cell is $O(s(U+L_2^2)/L)$ with power-small error.

## 3. Large least prime and the two shell labels

Suppose $P^-(k)>G$. Above the additional cut of Section 1, equation (2) gives

$$
 |F_{0,D}(pk)|\le\#\{d\mid k:\ \log d\in\mathcal J\},
                                                               \tag{6}
$$

where $\mathcal J$ is one deterministic log interval containing the interval from $T_2$ to $T_1$ for every $x,k$ in the cell pair. We take its length at most $W=C_B L_2$, and its lower endpoint positive, so $d=1$ is absent. This uses the exact parity identity, not a replacement of the signed coefficient in the Fourier sum. For sufficiently large $N$, $W<U$.

We need two elementary harmonic bounds for integers with no prime factor $\le G$, called $G$-rough and permitting 1 when not explicitly excluded. The harmonic sum up to $Z$ is $O(s/U)$ by the Euler product. The harmonic sum of **nontrivial** $G$-rough integers in any log interval of length at most $W$ is $O((1+W)/U)$. To prove the second, use the one-dimensional Selberg square at modulus one, as in the [two-gate energy proof](weak-s-type-ii-critical-prime-boundary-two-gate-energy.md), now with level $R=\lfloor e^{U/10}\rfloor$. On any hard interval of ordinary length $H$ its count is $O(H/U+e^{U/4})$, by the floor error $O(R^2(1+\log R)^2)$. Cover the log interval above $\log G$ by $O(1+W)$ unit log bins (the part below contains no nontrivial $G$-rough integers); the reciprocal weight per bin has upper bound $O(1/U)$ since its scale is $\gg G$. This proof is uniform in its position.

To square (6), let its ordered divisor labels be $d,t$ and write $d=ga,\ t=gb$ for $g=(d,t)$. All factors are $G$-rough, and $[d,t]=gab$. If exactly one of $a,b$ were 1, the other would exceed $G=e^U$, contradicting $|\log(d/t)|\le W<U$. For $a=b=1$, the reciprocal $1/[d,t]$ sums over $g>1$ in the shell at cost $O(W/U)$. If both exceed 1, fixing $g\le Z$ restricts each of $a,b$ to a log interval of length $W$. Their separate costs are $O(W/U)$, and the unrestricted $g$ cost is $O(s/U)$. Thus

$$
     \sum_{\substack{d,t\ G{\rm\text{-}rough}\\
                     \log d,\log t\in\mathcal J}}\frac1{[d,t]}
                  \ll W/U+W^2 s/U^3.                           \tag{7}
$$

Dropping the cofactor coprimalities here only enlarges a nonnegative sum.

For each pair in (7), applying the same rough sieve to $k/[d,t]$ on the $k$ cell shows

$$
 \sum_{\substack{K<k\le K'\\[d,t]\mid k,\ P^-(k)>G}}\frac1k
   \ll \frac{w}{U[d,t]}+\frac{e^{U/4}}K.
$$

This follows since $K'-K\ll Kw$; it does not assume any lower bound on the cell length. There are at most $Z^2$ possible pairs, so the floor term summed over them is $N^{-1/2+o(1)}$. Consequently the squared reciprocal sum of the majorant in (6) is

$$
       O\bigl(w(W/U^2+W^2s/U^4)+N^{-1/2+o(1)}\bigr).           \tag{8}
$$

Keep the **signed** estimate (4) for the second factor $F_{1,D}$, rather than upper-bounding its integrated primitive by its own unsigned divisor count. Cauchy on the arithmetic cell, followed by summing widths $O(s)$, gives a reciprocal product bound

$$
   O\!\left(\frac{s^{3/2}\sqrt W/U+s^2 W/U^2}{L}\right)
$$

with power-small error. Both this and the small-prime bound are $O(s^{4/3}L_2/L)$ at $U=s^{1/3}$. Clipped cells and the earlier discarded narrow border were already included. Together with the prime-$k$ contribution, and adding the low mixed $M_\le$ cost, the fixed physical cell has reciprocal majorant sum $O((s^{4/3}L_2+sL_2^5)/L)$. Multiplying by $k/\varphi(k)\ll L_2$ gives the two terms in the numerator of (1).

## 4. Preserve the two prime forms and the actual major model

The bounds above apply to unchanged coefficients, with masks that depend on $k$, $x$ or the actual primality of $p$; no new progression-residue condition was imposed. In each physical cell use the same actual two-prime upper sieve for $p,\ N-kp$ on its hard interval with $(k,N)=1$ and $p>\max(P_*,P^+(k))$. As in the integrated proof, it gives the main term per $k$ of size $\Sigma(N)|I_{\rm cell}|(k/\varphi(k))/(kL^2)$, plus $O(N^{1/4}L)$. Sum against the positive reciprocal majorant, one left log weight, and $\sum |I_{\rm cell}|=|I|$. There are $N^{1/2+o(1)}$ candidate $k$, polynomially many physical cells and only subpower-sized coefficient bounds. The total sieve error is absorbed in $N^{.76}$.

For the exact major calculation, the weight at each **fixed** $k$ still has variation $O(\tau_4(k))$; the new inequalities were estimates of it, not substitutions or added Fourier cutoffs. The parity selector is constant at fixed $k$. The previous prime-progression calculation is unchanged, including the $c_q(k)/\varphi(q)$ factor, the $O_\epsilon(N^{3/4+\epsilon}Q^2)$ right error, and the pointwise Fourier and Ramanujan tails with error $O(N^{1-10^{-4}})$ in the major integral. In the completed real density the local factor vanishes on $(k,N)>1$, and is $O(\Sigma(N)k/\varphi(k))$ otherwise, with the $1/[k\log(x/k)]$ cofactor. Since $\log(x/k)\gg L$, the same reciprocal bounds now bound this real density. Subtract the actual estimated major from the full coefficient to get the second line of (1). No conclusion about the surviving mixed minor is asserted.
