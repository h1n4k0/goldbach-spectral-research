# The odd mixed strip outside a moving weighted-count saddle

**Scope.** Continue the [actual weighted count estimate](r71-spectral-weighted-high-small-prime-count.md). Let $L=\log N$, $L_2=1+\log L$, $U=\sqrt L$, $G=e^U$, and write $\ell_U=\log U$. On squarefree partners of **odd total Möbius parity** $\mu(m)=-1$, put

$$
 j(m)=\#\{p\mid m:p\le G,\ p\ {\rm prime}\}.
$$

Retain the genuine $M_>$ and the true largest-prime gate $P^+(m)>N^\kappa$. This note controls the actual weighted coefficient whenever $\lvert j(m)-2\ell_U\rvert\ge a$, uniformly for real $0<a\le\ell_U$. In particular the unresolved odd count region can be restricted to

$$
 |j(m)-2\log U|<12\sqrt{\log U\,\log L_2}.
 \tag{1}
$$

This is an upper bound outside a moving region, not a claim about the count distribution of the original primes or about any coefficient inside that region. No even-parity bound is added.

Keep the exact hard central interval $I$, bounded-variation left weight $\omega$, actual polynomials, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, and $V=[N/3,2N]$ of the preceding work. Let $A(m)$ be $M_>(m)$ on the stated odd, squarefree, largest-prime, and count selector, zero off $V$. Define

$$
 \mathcal B(a)=L_2^8 \exp\!\bigl(-a^2/(10\ell_U)\bigr)+L^{-1/2}.
$$

Then

$$
\begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
    &\ll \Sigma(N)|I|\mathcal B(a)/L+N^{1-c},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)
                              e(-N\theta)\,d\theta\right|
    &\ll \Sigma(N)|I|\mathcal B(a)/L+N^{1-c}.
\end{split} \tag{2}
$$

The first line is unconditional for each fixed $0<\kappa<1/2$. The second uses the historical prime-character Dirichlet GRH inputs, at the unchanged genuine arcs $Q=N^{1/1000}$, for each fixed $1/500<\kappa<1/2$. One can take $c=\min(10^{-4},\kappa/10)$ in the first line and $c=\min(10^{-4},(\kappa-1/500)/10)$ in the second. Here $\lambda(n)=(\log n)\mathbf 1_{n\ {\rm prime}}$ as before. Constants are uniform in $a$ in the indicated range, with $\kappa,B,B_0$ fixed. For (1) take $a=12\sqrt{\ell_U\log L_2}$, which eventually lies below $\ell_U$. Then $\mathcal B(a)\ll L_2^{-6}$. The original $L/N$ normalization therefore gives $o(\Sigma(N))$ on this selector.

## 1. Two-sided weighting of the actual moderate counts

On a true largest-prime representation $m=pk$, $p>\max(N^\kappa,P^+(k))$, the count $j(m)=j(k)$ because $p>G$ eventually. It is constant at fixed $k$, as is the actual parity. For $j(k)>J_*=\lfloor32\log U\rfloor$, the previous unconditional $\tau_4(k)$-weighted Rankin bound supplies reciprocal majorant $O(U^{-9})$, including $k/\varphi(k)$, without a restriction on the small-factor product. The remaining counts use the exact product $k=bv$ with $b$ the squarefree product of its primes $\le G$ and $v$ strictly $G$-rough. The same true sharp factors and low mixed subtraction are retained; in particular neither the count nor the hard divisor cut is moved.

Write $r_-=\lfloor2\ell_U-a\rfloor$, $r_+=\lceil2\ell_U+a\rceil$. On the lower selector set $z=1-s$, and on the upper selector set $z=1+s$, where $s=a/(8\ell_U)$. Thus $z\in[7/8,9/8]$, uniformly bounded away from $1/2$. The exact positive generating sum for the signed divisor-shift multiplier at frequency $\xi$ is bounded by $\exp(zM(\xi))$, in the notation of [the weighted count proof](r71-spectral-weighted-high-small-prime-count.md#2-signed-fourier-moments-on-the-upper-tail). Extracting $j\le r_-$ at $z<1$ costs $z^{-r_-}$; extracting $j\ge r_+$ at $z>1$ costs $z^{-r_+}$. The temporal sign here is entirely in the exact multiplier $q_b(\xi)=\prod_{p\mid b}(1-e^{-i\xi\log p})$, not the absolute number of translates.

The signed primitive Plancherel bound $O(U^{2z})$ is **uniform on this compact range of $z$**: in its low-frequency part $U\int_0^U(1+y)^{-2+2z}dy\ll U^{2z}$, with $2z-1\ge3/4$; the high-frequency integrable log power can be taken at $z=9/8$. A sum of two primitives preserves this bound up to a fixed factor, and the integral between them of width at most $W=C_B L_2$ has squared bound $O(W^2 U^{2z})$. These are exactly the two odd factors before reinstating the centered term and the physical denominators. In particular the centered term, which has size $O(W/L)$ times the first factor, is not dropped.

Use the same reciprocal rough trace, signed cutoff averages, local pair floors, and fine $\eta=L^{-100}$ hard cells as in the previous proof, with all moderate counts $j\le J_*$. At $U=\sqrt L$ the outer rough harmonic sum and true rough density contribute $O(L/U^2)=O(1)$ to the aggregated squared Plancherel bounds. The old positive endpoint envelopes are uniform over all these counts and hence uniform in $a,z$, including cutoff integers; the reciprocal floors are $N^{-\kappa+o(1)}$ before the last Cauchy. Thus the genuine sharp product has reciprocal main bound on each physical cell

$$
 O\bigl(W U^{2z-2}z^{-r_\pm}\bigr)
 \tag{3}
$$

prior to multiplying by $k/\varphi(k)$. The same preceding proof deals with the prime-$k$ and near-unit border contributions; they are $O(L^{-1+o(1)})$ in these reciprocal sums. The nonnegative square comparisons do not alter the actual prime polynomial or its hard weights.

The centered exponents on either tail satisfy

$$
 U^{2z-2}z^{-r_\pm}\le \exp\!\bigl(-a^2/(10\ell_U)\bigr).
 \tag{4}
$$

Indeed on the lower tail the integer floor only improves the bound, and

$$
 -2\ell_U s-(2\ell_U-a)\log(1-s)
 \le -a s+\frac{(2\ell_U-a)s^2}{2(1-s)}
 \le-\frac{a^2}{10\ell_U}
$$

for $a\le\ell_U$, $s\le1/8$. On the upper tail the ceiling only improves it, and $2\ell_U s-(2\ell_U+a)\log(1+s)\le -as+(2\ell_U+a)s^2/2\le-a^2/(10\ell_U)$. Here we used the elementary logarithm bounds on $0\le s\le1/8$. The argument retains the exact two disjoint integer tails.

## 2. Low mixed piece and the original prime transfer

For the actual $M_\le$ portion, small factor allocation costs $2^j3^{j_0}$, with the costly signed-label primes restricted to $j_0=\#\{p\mid b:p\le H_0/D\}$. The old positive harmonic bound before summing $b$ is $O((W^2/U^2)2^j3^{j_0}/b)$ on each physical cell, since $U^2=L$. Weighted by $z^j$, the harmonic sum of the tag factor is at most

$$
 \exp\!\left(2z\sum_{p\le G}1/p+
              4z\sum_{p\le H_0/D}1/p\right)
       \ll U^{2z}L_2^{9/2}
$$

uniformly over $[7/8,9/8]$ by Mertens, since $H_0/D=L^{B-B_0}$, with fixed $B>B_0$. Extracting the corresponding lower or upper count gives $z^{-r_\pm}$ just as before. Include $k/\varphi(k)\ll L_2$ and $W=O(L_2)$. The total log-log factor in the low portion is $O(L_2^{15/2})$, dominated by $L_2^8$; the sharper loss in (3) is also dominated by $L_2^8$. The border, extreme tail, and envelope terms fit the added $L^{-1/2}$ term, and the reciprocal power floors remain smaller than $N^{-\kappa/2+o(1)}$ after Cauchy. This proves the required subpower-sized reciprocal upper envelope on every physical cell, with $k/\varphi(k)$ included.

For the unconditional full coefficient use the same actual two-root sieve of the [lower-largest-prime transfer](r70-spectral-lowest-largest-prime-transfer.md): level $N^{\kappa/4}$ and sifting at $N^{\kappa/100}$, actual interval length at most $|I_{\rm cell}|/k$, and total arithmetic floor $N^{1-3\kappa/4+o(1)}$. The physical lengths add to $|I|$. The reciprocal floor also fits the first exponent $c$ in (2).

For the real fixed-$Q$ minor assertion the [band-limited left transfer](r71-spectral-bandlimited-left-transfer.md) applies to these selectors, as follows. That calculation needs the unique largest-prime representation with $k\le2N^{1-\kappa}$ and $p>Q$, right weight $F_k(x)$ supported on $V$ with size and variation $O(\tau_4(k))$, and the positive reciprocal envelope for the completed major density on each physical cell. Its prime-character and numerator Parseval steps do not use the earlier numerical slot caps. Here the revised masks are constant at fixed $k$, even above $J_*$, so the exact right $F_k$ retains the asserted variation; the reciprocal envelope was just established and $p>Q$ follows from $\kappa>1/500$. In particular the band-limited exact hard-left weight $W_Q(x)$, with size plus variation $O(\log(2Q))$ on $V$, integrates the right error before applying the two Parsevals; this yields the same integrated error $O_\epsilon(Q^{1+\epsilon}N^{1-\kappa/2+\epsilon})$. The left error against the actual right polynomial is $N^{1/2+o(1)}Q^5$, unchanged. All rational and Fourier main-model completions use the same occupation estimate and the same local factor $O(\Sigma(N)k/\varphi(k))$ (zero on nonunit $k$); the continuous denominator is still $k\log(x/k)\gg_\kappa kL$. These verify the hypotheses of the transfer for the new selector with no reduction of the arc set. The resulting major bound has the right side of (2) at the second exponent $c$. Subtract the actual major integral from the actual full coefficient. This leaves (1) as a genuine unresolved odd count region, not a solution of it.
