# Two above-BV deletions for the genuine central removed strip

**Scope.** We remove two actual portions of the [central strip minor](r64-spectral-pointwise-major-central-bridge.md) **above** the previous Bombieri–Vinogradov cutoff. First, the exact Möbius prime marginal of the high strip cancels with its low companion by complementary divisors, so its signed minor is arbitrarily small on each modulus. Second, the high strip on squarefree partners having a prime factor above their midpoint has an unconditional full arithmetic bound and a pointwise small minor coefficient (using Dirichlet GRH for two prime progression estimates on the same major arcs). Separately an exact reflection cancels a high-high part of the remaining mixed coefficient. None of these claims estimates the whole remaining strip, the separate corrected sharp-profile minor, the exterior, or Hypothesis S.

Let even $N$ be large, $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$ with fixed $B>B_0>0$. Use $V=[N/3,2N]$, $Q=N^{1/1000}$, the same major arcs $\mathfrak M$ of widths $2Q/N$ and denominators $q\le Q$ as in the earlier bridge, and their complement $\mathfrak m$. Write $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$, $P_{I,\omega}(\theta)=\sum_{n\in I}\lambda(n)\omega(n)e(n\theta)$ with $e(t)=e^{2\pi i t}$, for any real half-open $I\subset(N/2,9N/16]$ and weight $\omega$ of bounded supremum and variation. A right coefficient is always zero outside integer $m\in V$. Write $\Sigma(N)$ for the binary singular series.

For squarefree $m$, the true strip $\Xi_D(m)$ has the factorization $m=abcd$, all four factors squarefree and pairwise coprime, with sign $\mu(b)\mu(c)$ and weight $1-2\log(ac)/\log m$. It retains exactly $ab,ac<\sqrt m$ and $\max(ab,ac)>D$, as in the [squarefree proof](r63-spectral-full-squarefree-crt-strip.md). The actual LCM is $h=abc$. Let $\Xi_>(m)$ retain $h>H_0$ and let $\Xi_{\rm g,>}(m)$ be this restricted to partners with a prime $p>\sqrt m$. All these are zero on nonsquarefree $m$.

**Results.** The above-level prime marginal $\Pi_>$ defined below satisfies, for every fixed $A>0$ and $B_0$ sufficiently large first,

$$
 \int_{\mathfrak m}P_{I,\omega}(\theta)\widehat{\Pi_>}(\theta)e(-N\theta)d\theta
        =O_{A,B,B_0}(NL^{-A}).                                  \tag{1}
$$

For any fixed $B>B_0>0$, the genuine above-level giant-prime strip satisfies

$$
 \begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|\Xi_{\rm g,>}(N-n)|
   &\ll_{B,B_0} \Sigma(N)|I|L_2^{10}/L^2+N^{.76},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)
        \widehat{\Xi_{\rm g,>}}(\theta)e(-N\theta)d\theta\right|
   &\ll_{B,B_0} \Sigma(N)|I|L_2^{10}/L^2+N^{1-10^{-4}} .
 \end{split}                                                     \tag{2}
$$

The first line is unconditional. Equations (1) and the second line of (2) use the historical Dirichlet GRH prime input for $q\le Q$, not RH for the right Möbius function. In the original Hardy normalization $L/N$ with its bounded weight $\omega_N$, (2) is uniformly $o(\Sigma(N))$ on every central prefix. We will also prove (2) separately for the prime and mixed parts of the giant-prime strip.

## 1. Complementary divisors and the entire high prime marginal

For squarefree $h\mid m$ let

$$
 U_h(t;m)=
 \sum_{\substack{abc=h\\\min(b,c)<t}}
     \mu(b)\mu(c)\left(1-\frac{2\log h-2\log b}{\log m}\right)
                \qquad (0<t<h).
$$

The actual $h$-coefficient of $\Xi_D(m)$ is $U_h(h/D;m)-U_h(h/\sqrt m;m)$: indeed $\max(ab,ac)=h/\min(b,c)$, and equality at $\sqrt m$ is impossible on squarefree $m>1$. (All sufficiently large $N$ have $D>1$ in $V$.) Expand the union defining $U_h$ as in the [below-level proof](r65-spectral-bv-visible-strip-minor.md). The sum restricted to $b<t$ with $c$ unrestricted vanishes by $\sum_{c\mid h/b}\mu(c)=0$, since $b<h$. In the opposite one-sided sum the constant term vanishes, and $\sum_{b\mid h/c}\mu(b)\log b$ is nonzero only when $h/c$ is prime, in which case it is $-\log(h/c)$. Subtract the double-small overlap. For each $h$ this gives the exact decomposition into a prime marginal

$$
 \Pi_h(m)=-\frac{2}{\log m}
           \sum_{\substack{p\mid h,\ p\ {\rm prime}\\D<p<\sqrt m}}
                            \mu(h/p)\log p                       \tag{3}
$$

minus the mixed signed sum over $abc=h$ with
$D<\min(ab,ac)<\sqrt m$, using the same weight. The overlap difference is precisely this latter gate since $\min(ab,ac)=h/\max(b,c)$. Equality at $D$ is excluded in both forms.

The full sum of (3) over $h\mid m$ is zero **pointwise**:

$$
 \sum_{h\mid m}\Pi_h(m)
   =-\frac{2}{\log m}
      \sum_{\substack{p\mid m,\ D<p<\sqrt m\\p\ {\rm prime}}}
                 (\log p)\sum_{k\mid m/p}\mu(k)
   =0.                                                          \tag{4}
$$

Here $m/p>1$. With squarefree mask and physical support retained, $\Pi_>=\sum_{h>H_0}\Pi_h$ is therefore the negative of $\Pi_\le=\sum_{h\le H_0}\Pi_h$ as **actual right coefficient sequences**. In particular every prime $p>H_0$ contributes zero to the high marginal already for each $m$. For $h\le H_0$ with $m\in V$, the upper bound $p<\sqrt m$ in (3) is automatic. Its weight is bounded in supremum plus variation by $O(\tau_3(h))$. The [exact below-level BV and CRT proof](r65-spectral-bv-visible-strip-minor.md) applies verbatim to this weight: Sections 1–2 of that proof use only support in squarefree $h\le H_0$ and the indicated variation bound before comparing their common density. Thus its signed minor is $O(NL^{-A})$ after choosing $B_0$ as there. Identity (4) proves (1). There is no change to the original coefficient inside the remaining mixed part and no cancellation claimed for arbitrary unsummed subfamilies of the high prime marginal.

There is also an exact cancellation in the mixed part for $h>H_0$. Swap $b,c$ to replace the centered factor by its symmetric average $\log(d/a)/\log m$; both the sign and all gates are invariant for this swap. Write $s=\min(ab,ac)$ and $t=\max(ab,ac)$. On swapping $a,d$ these become $m/t$ and $m/s$ respectively, and the log factor changes sign. The mixed gate $D<s<\sqrt m$ and its swapped version overlap precisely when

$$
                   D<s<\sqrt m<t<m/D .                           \tag{5}
$$

Both LCMs $abc$ and $dbc$ are $>\sqrt m$ in (5), because each contains a divisor above $\sqrt m$. Thus this involution cancels the whole overlap **within the above-$H_0$ range** for each fixed $m$. Up to the overall minus sign from the union expansion, the residual mixed part is exactly supported on

$$
 \begin{array}{ll}
 D<s\le t<\sqrt m, &\log(d/a)\ge0,\quad
             \max(b,c)/\min(b,c)<\sqrt m/D,\\
 D<s<\sqrt m,\ t\ge m/D, &\log(d/a)<0,\quad
             \max(b,c)/\min(b,c)>\sqrt m/D .
 \end{array}                                                     \tag{6}
$$

The strict upper endpoint $m/D$ of (5) goes into the second row at equality. The displayed signs follow from $st=m(a/d)$. The identity cancels the overlap, not the two surviving signed projections in (6).

## 2. Above-level giant partners: a true full arithmetic upper bound

For a squarefree giant partner write $m=pk$ with its unique prime $p>\sqrt m$. Then $p>k$, all divisors below $\sqrt m$ avoid $p$, and every relevant LCM divides $k<\sqrt m$. Equivalently $p$ lies in the last positive factor of every original strip term. For fixed $k$ and $x\in V$, $x>k^2$, the above-level strip coefficient is therefore

$$
 G_k(x)=\sum_{\substack{h\mid k\\h>H_0}}W_h(x),
                                                                  \tag{7}
$$

where $W_h(x)$ is the exact below-midpoint union coefficient of the previous proof, with no need here for $h\le H_0$: its justification uses $h<\sqrt x$, which now follows from $h\mid k<\sqrt x$. Only $D<k<\sqrt{2N}$ can contribute. Let $Z=2L^B$ and set $\tau_{\le Z}(k)=\#\{r\mid k:r\le Z\}$. In the mixed term of (7), $b,c<h/D\le Z$. Also $k/h\le Z$, and $h/b>D$, so the centered factor there is bounded by $O_B(L_2/L)$. The total magnitude of this mixed portion is at most $O_B((L_2/L)\tau_{\le Z}(k)^3)$, by counting $k/h,b,c$ separately. For its prime marginal, a prime $p_0>D$ dividing $k$ is unique because $D^2>\sqrt{2N}$. Write $k=p_0 r$ with $r\le Z$; the number of contributing $h\mid k$ is at most $\tau(r)$ and $2\log p_0/\log x$ is bounded. Thus there is a pointwise absolute bound for the two portions separately and their sum by

$$
 C_B(k)=O_B\!\left(
            \frac{L_2}{L}\tau_{\le Z}(k)^3+
            \mathbf1_{\,k=p_0r,\ p_0>D\ {\rm prime},\ r\le Z}\tau(r)
                       \right).                                 \tag{8}
$$

This is an absolute majorant for the **regrouped** coefficient, not for the individual four-factor terms. We record the uniform harmonic estimate

$$
 \sum_{\substack{D<k<\sqrt{2N}\\k\ {\rm sf}}}
             \frac{C_B(k)}{k}\frac{k}{\varphi(k)}
                    \ll_B \frac{L_2^{10}}{L}.                    \tag{9}
$$

In the mixed portion expand the three short divisors. For their LCM $\ell$, the reciprocal sum of its multiples in $D<k<\sqrt{2N}$ is $O_B(L_2/\ell+1/D)$ by the integral count, valid also when $\ell>D$. The three divisors are squarefree, hence for each prime of $\ell$ there are at most seven assignments to the three divisors. It follows that the sum of $1/\ell$ over triples is at most $\prod_{p\le Z}(1+7/p)\ll (1+\log Z)^7$, and the total endpoint cost is $O(Z^3/D)$. This bounds the mixed short-divisor harmonic sum by $O_B(L_2^8)$. For the prime portion use $\sum_{r\le Z}\tau(r)/r\ll (1+\log Z)^2$ and $\sum_{D<p_0\le\sqrt{2N}}1/p_0\ll_B L_2/L$ by ordinary PNT and partial summation. Multiply both by $k/\varphi(k)\ll L_2$ and by the extra $L_2/L$ in the mixed portion. This proves (9).

On genuine prime positions $(k,N)=1$. For fixed $k$ in (9), the primes $p$ with $p>k$ and $n=N-kp\in I$ lie in an interval of length at most $|I|/k$. Both $p$ and $N-kp$ are above $N^{1/100}$ on this support. Apply the [dimension-two fundamental upper sieve, Corollary 19](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/) to these two linear forms in the integer $p$ at sifting height $N^{1/100}$ and level $N^{1/4}$. There are two roots at primes not dividing $kN$, and one root at primes dividing $kN$, since $(k,N)=1$ and $N$ is even (in particular at $2$). The sieve dimension bound is uniform, by comparison with two roots at all odd primes. CRT gives error $O(2^{\omega(d)})$ per squarefree modulus $d$, even on a short interval. The local product is

$$
 \ll \frac{\Sigma(N)}{L^2}
               \prod_{\substack{\ell\mid k\\ \ell>2}}
                         \frac{\ell-1}{\ell-2}
       \ll \frac{\Sigma(N)}{L^2}\frac{k}{\varphi(k)} ,
$$

by Mertens and the convergent ratio $\prod_{\ell>2}(\ell-1)^2/(\ell(\ell-2))$. Thus the count for fixed $k$ is at most $O(\Sigma(N)|I|/(kL^2)\cdot k/\varphi(k)+N^{1/4}L)$. Empty intervals contribute zero. Multiply by the bound $O(L C_B(k))$ for the actual $\lambda$ weight times coefficient and use (9). The sum of the sieve errors is $O(N^{.76})$, because each $C_B(k)$ is bounded by a fixed power of $L$ by (8), and there are $O(\sqrt N)$ choices of $k$. This proves the first line of (2), and its separate version for either part.

## 3. The same upper scale for the actual giant major arcs

For every fixed squarefree $k>D$ use the actual prime progression polynomial on $p>k$ and $kp\in V$. The weight in it is $G_k(kp)$ or its separate prime or mixed portion. It has supremum and variation $O(\tau_4(k))$ on $x\in V$, $x>k^2$, since the divisors in (7) are fixed as $x$ varies and the log ratio is monotone term by term. Its extension by zero off $x>k^2$ adds only the endpoint jump. The exact inequality $p>k$ ensures $(p,k)=1$, without an artificial Fourier mask; also every such $p$ is $\gg\sqrt N\gg Q$ and hence prime to $q\le Q$.

Under the prime GRH progression estimate at $q\le Q$, sum over the reduced classes of $p$ on an arc $a/q+\eta$. Since $\sum_{v\bmod q}^*e(a k v/q)=c_q(k)$, the resulting real density is

$$
 D_q^{\rm g}(x)
 =\sum_{\substack{D<k<\sqrt x\\k\ {\rm sf}}}
       \frac{c_q(k)}{\varphi(q)}
           \frac{G_k(x)}{k\log(x/k)}\qquad(x\in V).
                                                                  \tag{10}
$$

The right polynomial error is $O_\epsilon(Q^2 N^{3/4+\epsilon})$: per $k$ use $q$ residue errors of size $O(\sqrt{N/k}\,L^2)$ and $O(Q\tau_4(k))$ variation, then sum $\sqrt{N/k}$ over $k\ll\sqrt N$. Centering and endpoint changes are included in that variation. The left prime approximation is the earlier one with factor $\mu(q)/\varphi(q)$. Nonsquarefree $q$ have zero left main term.

For squarefree $q$, the supremum plus variation of (10), extended by zero off $V$, is $O(L^4 C^{\omega(q)}/q)$. Indeed $\log(x/k)\gg L$ on this support and the step $x>k^2$ costs only the single bounded jump. For each $p\mid q$, when $p\nmid k$ its factor in $|c_q(k)|/\varphi(q)$ is $1/(p-1)\ll1/p$; when $p\mid k$ that factor is one but occupancy gains $4/p$ on summing the squarefree reciprocal $\tau_4(k)/k$. Expand these two choices and sum the remaining harmonic weights. Thus both the Fourier tail and the **pointwise** Ramanujan tail are covered by the [earlier completed density argument](r64-spectral-pointwise-major-central-bridge.md), with at most one extra factor of $L$ in the density bound. Together with the polynomial errors on arcs of total measure $O(Q^3/N)$, this gives $O(N^{1-10^{-4}})$ in the integrated major approximation on every modulus and every interval.

To calculate its completed density, combine (10) with the left multiplier and the reduced numerator sum. For fixed $k$ the local factors of the resulting absolutely convergent series $\sum_q\mu(q)c_q(N)c_q(k)/\varphi(q)^2$ give

$$
 S(N,k)=
 \begin{cases}
  \displaystyle \Sigma(N)\prod_{\ell\mid k}\frac{\ell-1}{\ell-2},
                                  &(k,N)=1,\\[1mm]
  0, &(k,N)>1 .
 \end{cases}                                                     \tag{11}
$$

Indeed the local factor is zero if a prime divides both $N,k$, is $1+1/(\ell-1)$ if it divides exactly one, and is $1-1/(\ell-1)^2$ if it divides neither. The apparent denominator at $2$ in the first branch is absent because $N$ is even. Thus no nonunit $k$ was deleted from the actual Fourier leg. The completed density is $\sum_{D<k<\sqrt x,\,k\ {\rm sf}}S(N,k)G_k(x)/(k\log(x/k))$. Using (8)–(9), its magnitude is at most $O(\Sigma(N)L_2^{10}/L^2)$ uniformly on $V$. The integrated major is bounded by $O(\Sigma(N)|I|L_2^{10}/L^2+N^{1-10^{-4}})$. Subtract the major from the full coefficient to prove the second line of (2), including its separate bounds for either part.

Consequently the above-$H_0$ remainder of the original signed strip minor can be restricted, up to (1) and (2) in their stated regimes, to squarefree partners **with no giant prime**, the mixed coefficient only, and the two exact ranges (6). To remove both the prime marginal and the giant selector without double counting, use (2) also on the giant prime marginal, then subtract it from (1); the involution (5) respects the nongiant selector since it leaves $m$ unchanged. There is no bound here on the surviving two ranges.
