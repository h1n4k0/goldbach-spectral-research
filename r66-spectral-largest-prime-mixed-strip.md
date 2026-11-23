# The above-BV mixed strip can discard every partner with a prime exceeding the sharp cut

**Scope.** After removing the global prime marginal as in [the above-BV strip decomposition](r66-spectral-above-bv-strip-deletions.md), we bound the actual remaining mixed coefficient on **all** squarefree partners whose largest prime exceeds the original $D$, not just partners with a giant prime above $\sqrt m$. This is an unconditional full arithmetic estimate, and a pointwise signed minor-arc estimate under the same prime progression GRH input as the earlier bridge. The result is for the mixed component after exact marginal subtraction; it does not bound the prime marginal with an arbitrary largest-prime mask or the entire original strip under that mask. The residual with largest prime at most $D$, the separate sharp minor, the exterior, and Hypothesis S remain open.

Let even $N$ be sufficiently large, $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$, with fixed $B>B_0>0$. Use $V=[N/3,2N]$, $Q=N^{1/1000}$ and the exact major/minor arcs of the [pointwise central bridge](r64-spectral-pointwise-major-central-bridge.md). For a central half-open $I\subset(N/2,9N/16]$ and bounded-variation weight $\omega$ with fixed uniform norm, set $P_{I,\omega}(\theta)=\sum_{n\in I}\lambda(n)\omega(n)e(n\theta)$, where $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Let $M_>(m)$ be the mixed term of the true squarefree strip union decomposition, with its sign **before** subtraction, namely the four-factor sum on $m=abcd$ squarefree, $abc>H_0$, $D<\min(ab,ac)<\sqrt m$, with sign $\mu(b)\mu(c)$ and weight $1-2\log(ac)/\log m$. Define $M_\le$ with $abc\le H_0$. All right sequences are zero outside squarefree $m\in V$. Set $A_>(m)=M_>(m)\mathbf1_{P^+(m)>D}$.

We prove

$$
 \begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A_>(N-n)|
     &\ll_{B,B_0}\Sigma(N)|I|L_2^{10}/L^2+N^{.76},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)
          \widehat A_>(\theta)e(-N\theta)\,d\theta\right|
     &\ll_{B,B_0}\Sigma(N)|I|L_2^{10}/L^2+N^{1-10^{-4}} .
 \end{split}                                                     \tag{1}
$$

The first line is unconditional. The second assumes the historical Dirichlet GRH prime AP input at $q\le Q$, with no right Möbius GRH input. In the original normalization $L/N$ the second line is $o(\Sigma(N))$, uniformly on each central prefix. Combining with the [below-level minor deletion](r65-spectral-bv-visible-strip-minor.md), the exact marginal cancellation (choose $B_0$ for any fixed required precision), and the high-high reflection, the removed-strip minor reduces, up to $o(\Sigma(N))$ in Hardy normalization, to the genuine above-$H_0$ mixed coefficient in the two previously stated ranges, now with the added selector $P^+(m)\le D$.

## 1. Exact representation after extracting the largest prime

Write the unique largest prime as $p>P^+(k)$, with $m=pk$ and $p>D$. The strict condition is exact; no repeated prime occurs on the squarefree support. The total prime marginal is zero pointwise by the complementary identity in the preceding above-level proof. Hence on squarefree $m$,

$$
                  M_>(m)=-\Xi_D(m)-M_\le(m).                    \tag{2}
$$

Since $p>D$, every divisor in either sharp sum avoids it, and the original full strict midpoint product equals the prime indicator on squarefree partners. Define

$$
 F_{1,D}(k;x)=\sum_{\substack{e\mid k\\e\le D}}
                     \mu(e)\left(1-\frac{2\log e}{\log x}\right).
$$

For $k>1$ and actual $m=pk$ this gives $\Xi_D(m)=-F_{0,D}(k)F_{1,D}(k;m)$. For $k=1$ the two full and sharp products on the prime $m$ both equal one and $\Xi_D=0$. If $1<k\le D$ the $F_{0,D}(k)$ factor vanishes. Moreover if $k\le D$ and $m\in V$, then $p\ge (N/3)/D>H_0$, so every $h\le H_0$ divides $k$ and no mixed low term can have $\min(ab,ac)>D$. Thus only

$$
                 D<k\le 2N/D=2\sqrt N L^B                      \tag{3}
$$

can contribute.

For a fixed $k$ describe the low term in (2) by $h=abc\le H_0<\sqrt m$. Its mixed gate is exactly $b,c<h/D$. If $p\nmid h$, then $h\mid k$ and these inequalities do not involve $p$. If $p\mid h$, put $h=pr$, $r\mid k$. The two signed divisors cannot contain $p$ because $b,c<h/D\le H_0/D=L^{B-B_0}<p$ for large $N$. Thus $b,c\mid r$, $(b,c)=1$ and $a=pr/(bc)$. For fixed $r,b,c$ the additional interval in $p$ is exactly

$$
                 D\max(b,c)/r<p\le H_0/r.                       \tag{4}
$$

The corresponding centered weight is $1-2\log(pr/b)/\log(pk)$. Formula (4) keeps both strict lower and weak upper endpoints. The inequalities $p>D$, $p>P^+(k)$, and $pk\in V$ are all also kept. In both low sectors each active log factor is $O_B(L_2/L)$, because $D<h/b\le H_0<\sqrt m$.

Put $Z=2L^{2B}$ and $\tau_{\le Z}(k)=\#\{r\mid k:r\le Z\}$. For $p\nmid h$ the three labels $k/h,b,c$ are divisors of $k$ bounded by $Z$ (use (3) and $h>D$). For $p\mid h$, the three labels $r,b,c$ in (4) are divisors of $k$ bounded by $H_0/D\le Z$. This bounds the entire low mixed term by $O_B((L_2/L)\tau_{\le Z}(k)^3)$, with no uncanceled prime marginal included.

For composite squarefree $k$ the two complete divisor sums $\sum_{e\mid k}\mu(e)$ and $\sum_{e\mid k}\mu(e)\log e$ vanish. The cut sums therefore equal the negatives of their omitted terms, with $e>D$. Each such $e$ has $k/e\le Z$, and its centered factor on real $x\in V$ is $O_B(L_2/L)$ in absolute value: $D<e\le2\sqrt N L^B$ and $\log x=L+O(1)$. This proves the bound $O_B((L_2/L)\tau_{\le Z}(k)^2)$ for the product. For prime $k>D$ the product equals one. In total the actual coefficient in (2), and its real function in $x=kp$ defined by these formulas, have pointwise absolute bound

$$
       C(k)\ll_B \frac{L_2}{L}\tau_{\le Z}(k)^3+
                         \mathbf1_{\,k\ {\rm prime}}.             \tag{5}
$$

Only require this bound where $x\in V$ and $x/k>\max(D,P^+(k))$, and extend this real weight by zero outside. This notation includes the step gates (4) with $p=x/k$. On that real line the supremum plus variation is also $O(\tau_4(k))$ as a coarser but uniform bound: the product has at most $\tau(k)^2$ terms with monotone log ratios; the two low sums have at most $\sum_{r\mid k}\tau_3(r)=\tau_4(k)$ candidates each, and each extra interval gate in (4) adds at most two bounded jumps. In the $h=pr$ sector the ratio is $\log(pr/b)/\log(pk)$, monotone in $p$ because its derivative in $\log p$ has fixed numerator $\log k-\log(r/b)$. The other ratios are monotone with fixed numerator, so no bound on arbitrary sharp discontinuity statistics is needed.

## 2. Transfer at every modulus

The harmonic bound of the [giant-prime calculation](r66-spectral-above-bv-strip-deletions.md#2-above-level-giant-partners-a-true-full-arithmetic-upper-bound) applies to (3)–(5):

$$
  \sum_{\substack{D<k\le2N/D\\ k\ {\rm sf}}}
               \frac{C(k)}k\frac{k}{\varphi(k)}
                       \ll_B L_2^{10}/L.                         \tag{6}
$$

For clarity the reciprocal count of multiples of a fixed lcm in (3) is $O_B(L_2/\ell+1/D)$, as its relative width is a fixed power of $L$. The lcm sum of the three fixed short divisors is bounded by $\prod_{p\le Z}(1+7/p)\ll_B L_2^7$, and the floor error $Z^3/D$ is negligible. The prime term in (5) has reciprocal sum $O_B(L_2/L)$ by PNT on the exact endpoints of (3). Finally $k/\varphi(k)\ll L_2$ uniformly. These facts give (6).

On true prime positions $(k,N)=1$. For fixed $k$, sieve $p$ and $N-kp$ in their actual interval of length at most $|I|/k$, retaining $p>\max(D,P^+(k))$. Both forms exceed $N^{1/100}$ for large $N$. The [dimension-two CRT sieve](r66-spectral-above-bv-strip-deletions.md#2-above-level-giant-partners-a-true-full-arithmetic-upper-bound) depends only on this fact, the interval length and $(k,N)=1$, giving at most
$O(\Sigma(N)|I|/(k L^2)\cdot k/\varphi(k)+N^{1/4}L)$ pairs per $k$ (sift at $N^{1/100}$, level $N^{1/4}$). Its use is valid even though some $p$ are **below** $\sqrt m$ now. Sum $L C(k)$ against this bound using (6). There are only $O(\sqrt N L^B)$ possible $k$ and $C(k)$ is at most a fixed power of $L$. This proves the first line of (1).

For the major comparison evaluate the actual prime polynomial in $p$ on $p>\max(D,P^+(k))$, with the exact piecewise weight of Section 1 and $\eta$ phase. The bounded variation just proved and $p\gg\sqrt N/L^B\gg Q$ show that the same prime AP argument as in the [previous completed giant major](r66-spectral-above-bv-strip-deletions.md#3-the-same-upper-scale-for-the-actual-giant-major-arcs) applies without deleting any nonunit $k$ on the right. More explicitly, for each squarefree $q\le Q$ the real right density is the sum over (3) of its real weight at $x$ times $c_q(k)/[k\,\varphi(q)\log(x/k)]$, with the just stated support. This follows by summing the reduced residues of $p$ as $c_q(k)$; the per-$k$ progression error after variation and slow phase is $O_\epsilon(q Q\sqrt{N/k}N^\epsilon)$. Summing (3) gives $O_\epsilon(Q^2 N^{3/4+\epsilon})$ (the extra fixed log powers are absorbed). The right sup and variation bound $O(L^4C^{\omega(q)}/q)$ follows exactly by occupation of primes of $q$ in the squarefree $k$ reciprocal sum, now up to (3), with $\log(x/k)\gg L$. Thus the Fourier and pointwise rational tails are controlled as before, and the integrated error is $O(N^{1-10^{-4}})$.

For fixed $k$ the completed local factor is the same $\sum_q \mu(q)c_q(N)c_q(k)/\varphi(q)^2$: it is zero on $(k,N)>1$ and otherwise equals $\Sigma(N)\prod_{\ell\mid k}(\ell-1)/(\ell-2)\ll\Sigma(N)k/\varphi(k)$. All additional step gates depended on $x$ and $k$ only, never on a residue of $p$, so the local factors are unchanged. Equations (5)–(6) bound the completed real density by $O(\Sigma(N)L_2^{10}/L^2)$ everywhere on $V$. The major coefficient is bounded by this times $|I|$ plus its power error. Subtract it from the genuine full coefficient just estimated to prove the second line of (1).

Finally apply this removal to the mixed projection only: the global prime marginal was separately deleted by complementary divisors, and the high-high reflection does not change the partner $m$, so it respects $P^+(m)\le D$. No need to estimate the prime marginal under the new selector. The all-modulus result removes its stated large-prime partners but makes no claim about the distribution or the sign of the surviving mixed minor.
