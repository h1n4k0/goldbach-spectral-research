# True exterior zero-copy diagonal: uniform cancellation against the stationary model

Put $L=\log N$, $\alpha=1/L$, $\beta=1/8$. Assume $N$ is even and satisfies the original local GRH(N). Use the genuine log coordinate $x=\log y$ for dimensionless physical $y$, with $m_N(x)=((Ne^x)^{-2\alpha}+(Ne^x)^{-2\beta})^{1/2}$, and let $Q_H$ stand for $x\ge H$. Fix a desired weak-S exponent $K>0$ and take
$$
 H\ge (K+3)\frac{(\log L)^2}{\log\log L}.
$$
In the notation of the [fine-side exterior reduction](weak-s-exterior-fine.md), define the **zero-copy diagonal** of the actual character Gram by the kernel
$$
 Z_{\rm diag}(x,z)=2\pi m_N(x)m_N(z)\operatorname{Avg}_{\chi\ {\rm odd}}
          \sum_j\frac{e^{i\gamma_{\chi,j}(x-z)}}{1+\gamma_{\chi,j}^2}.
 \tag{1}
$$
Here all nontrivial zeros of the primitive inducing character are indexed by *copies*, so a zero of multiplicity $m$ appears $m$ times. This is the diagonal $j=j'$ of the true residue Gram and has **linear**, not squared, multiplicity. The exact cancellation proved here is
$$
 \big\|{\bf1}_{|x-z|\le B}\,
       [Z_{\rm diag}(x,z)-(D_N+K_N)(x,z)]\big\|_{\rm HS}
       =o(L^{-K}),
 \qquad B=2L-(2K+6)\log L,
 \tag{2}
$$
on $x,z\ge H$, uniformly over such $H$ and all sufficiently large locally GRH-admissible $N$. Here $D_N+K_N$ denotes its log-coordinate kernel, and the indicator masks a Hilbert–Schmidt kernel. In particular the conclusion holds on the broad band $|x-z|\le(2-\eta)L$ for any fixed $\eta>0$, or on two rectangles whose every logarithmic difference lies in (2). On a fixed polynomial exterior $H\ge\gamma L$, with $|x-z|\le(2-\eta)L$, both the stationary and diagonal errors can instead be taken inverse-polynomial in $N$.

On this band the **true** exterior $T_N$ agrees in HS to $o(L^{-K})$ with the contribution from *distinct zero copies* of the same character. The same holds after compression onto the weighted means of the fine-side reduction (after the mask), or for the actual block within any interval of log length $B$ wholly in the exterior. This is a quantitative cancellation of a specific genuinely present component, not an estimate for all zero pairs or all mean–mean entries. Distinct copies at one repeated ordinate are still included in the unknown part. No simplicity, independence, density-one qualifier, or condition on conductors beyond local GRH.

## 1. Exact primitive odd character averages

Let $q_\chi$ be the conductor of the character $\chi\bmod N$ and put $b_N=\sum_{p\mid N}\log p/(p-1)$. Then
$$
 \operatorname{Avg}_{\chi\ {\rm odd}}\log q_\chi=L-b_N+\Delta_N,
 \tag{3}
$$
where $\Delta_N=0$ unless $N=2^a$ or $N=2p^a$ with $p$ odd; the corrections in those two cases, respectively, are $2\log 2/\phi(N)$ and $\log p/\phi(N)$. Here $N$ is large, so the overlap at $N=2$ is irrelevant.

For this calculation select a character uniformly over all characters of $(\mathbb Z/N\mathbb Z)^\times$. Its local components for $p^a\Vert N$ are independent by CRT. If the local conductor exponent is $e_p$, then
$$
 {\bf E}(a-e_p)=\sum_{j=1}^a\frac{\phi(p^{a-j})}{\phi(p^a)}
              =\frac1{p-1}.
$$
Thus the unrestricted conductor mean is $L-b_N$. Since $N>2$, the odd average of any function $F$ is the all-character mean of $(1-\chi(-1))F$. The cross term for the $p$-local exponent vanishes unless $M=N/p^a\le2$, because $\chi(-1)$ on the complementary factor has mean zero when $M>2$. For the exceptional local factor,
$$
 {\bf E}\big[\chi_p(-1)(a-e_p)\big]=\frac{1}{\phi(p^a)}
       \sum_{j=1}^a\sum_{\psi\bmod p^{a-j}}\psi(-1).
$$
Only moduli $1$ or $2$ contribute to the numerator, giving 1 for odd $p$ and 2 for a power of 2 with $a\ge2$. Since the full mean of parity is zero, the $\log q_\chi$ correction has the positive sign in (3).

For a prime power $n=p^k$ define the real coefficient
$$
 B_N(n)=\operatorname{Avg}_{\chi\ {\rm odd}}\chi^*(p^k).
$$
Here $\chi^*$ is the primitive inducing character. For $p\nmid N$, standard odd orthogonality gives
$$
 B_N(p^k)={\bf1}_{p^k\equiv1\ (N)}-{\bf1}_{p^k\equiv-1\ (N)}.
 \tag{4}
$$
For $p^a\Vert N$ and $M=N/p^a$ one instead has
$$
 B_N(p^k)=\frac{{\bf1}_{p^k\equiv1\ (M)}-{\bf1}_{p^k\equiv-1\ (M)}}{\phi(p^a)} .
 \tag{5}
$$
In fact a nontrivial $p$-local component makes $p$ divide the primitive conductor, so $\chi^*(p^k)=0$. If that component is trivial, the inducing value at $p^k$ is the character on the complementary modulus $M$, unaffected by its restriction to the primitive inducing conductor because $(p,M)=1$. The surviving characters must be odd on $M$, and normalization of the odd mean over $N$ now gives (5). For $M=1,2$ there are no such complementary odd characters; both indicators are equal, so the formula is still exact. In particular whenever a bad-prime coefficient is nonzero, $M\le p^k+1$, and
$$
 |B_N(p^k)|\le \frac1{\phi(p^a)}\ll \frac{M}{N}\ll \frac{p^k}{N}.
 \tag{6}
$$
The bad Euler factors cannot be omitted by simply extending the primitive values by zero at all nonunits of $N$; (5) deals with the actual inducing values.

## 2. Explicit formula and local uniform HS cancellation

Use the Guinand–Weil formula with ordinary Fourier transform $\widehat h(v)=\int_{\mathbb R}h(t)e^{-itv}\,dt$; see [Chirre–Hagen–Simonič, Lemma 8](https://arxiv.org/pdf/2206.00819v2#page=6) for the primitive-character form and test conditions. For an odd primitive character the gamma logarithmic derivative in the real-part density is $\Re\psi(3/4+it/2)$. Use
$$
 h_\xi(t)=\frac{\cos(t\xi)}{1+t^2},\qquad
 \widehat h_\xi(v)=\frac{\pi}{2}\big(e^{-|v-\xi|}+e^{-|v+\xi|}\big)
$$
for the real log difference $\xi=x-z$. For each fixed $\xi$ the test is analytic on each closed strip of half-width less than 1, with quadratic decay there, so the standard formula applies. The zeros are counted with multiplicity and the averaged zeros are symmetric under $t\mapsto-t$ by pairing $\chi$ with $\bar\chi$, so the cosine suffices for (1). Multiplying by $2\pi$ to match that kernel, (3)–(5) give the following exact identity for its bare translation kernel $z_N(\xi)$:
$$
 \begin{split}
 z_N(\xi)-k_N(\xi)
   ={}&\pi\Delta_N e^{-|\xi|}\\
     &-\pi\sum_{n\ge2}\frac{\Lambda(n)B_N(n)}{\sqrt n}
       \big(e^{-|\log n-\xi|}+e^{-|\log n+\xi|}\big).
 \end{split}
 \tag{7}
$$
Here $k_N$ is precisely the stationary kernel of the [diagonal and Beta benchmark](operator-post-r15-stationary-tail.md) with Fourier multiplier $2\pi[L-\log\pi-b_N+\Re\psi(3/4+it/2)]/(1+t^2)$. The series in (7) absolutely converges for each fixed $\xi$. There is no principal-character term, since the inducing characters of the odd characters are all odd.

A direct uniform bound makes (7) useful at full weak-S scale. Write $D=|\xi|$, $X=e^D$. For unit prime powers, the congruences in (4) force $n\ge N-1$ and restrict to two translates of $N\mathbb Z$. The two exponential weights are at most twice $e^{-|\log n-D|}$. For $N-1\le n\le X$, there are $O(X/N)$ candidates whenever there are any, and $\Lambda(n)n^{-1/2}e^{-|\log n-D|}\le (\log(2X))\sqrt n/X$. This gives $O(\sqrt X\log(2X)/N)$. For $n>X$, the summand is at most $X(\log n)n^{-3/2}$. Summing over either progression gives $O(\sqrt X\log(2X)/N)$ when $X\ge N/2$ by a first term plus the tail integral with progression spacing. If $X<N/2$, the bound is instead $O(X L/N^{3/2})$, which is still $O(\sqrt X L/N)$.

For primes dividing $N$, (6) gives a bound by a constant times
$$
 \frac{1}{N}\sum_{p\mid N}\log p
       \sum_{k\ge1} \sqrt{p^k}e^{-|\log(p^k)-D|}.
$$
The inner sum is $O(\sqrt X)$ uniformly in $p\ge2$: below $X$ it is a geometric sum of $(p^k)^{3/2}/X$, and above it is a geometric sum of $X/(p^k)^{1/2}$. Therefore for all real $\xi$,
$$
 |z_N(\xi)-k_N(\xi)|
 \ll \frac{L}{\phi(N)}e^{-|\xi|}
     + \frac{(L+|\xi|)e^{|\xi|/2}}{N}.
 \tag{8}
$$
For $|\xi|\le(2-\eta)L$ this saves a power of $N$; for $|\xi|\le B$ the latter term is $O(L^{-K-2})$. Multiplying by the true Hardy factors $m_N(x)m_N(z)$ and using $\int_H^\infty m_N(x)^2dx\ll L$ shows the claimed masked HS gain for the difference of the zero-copy diagonal and the stationary model. The first term of (8) is harmless by $1/\phi(N)\ll\log\log N/N$. Finally the stationary approximation in [the stationary benchmark](operator-post-r15-stationary-tail.md), with the [uniform moving-contour estimate](weak-s-exterior-fine.md#diagonal-and-beta-benchmark), gives $o(L^{-K})$ error in HS on the whole exterior at this $H$. This proves (2).

## 3. Relation to the actual two-zero Gram and its cutoff

The [one-sided shift for the physical atoms](r20-operator.md#3-exact-arithmetic-target-on-the-retained-coarse-cells-at-the-natural-height), expressed in the log coordinate, is
$$
 p_\chi(x)=\sqrt{2\pi}\,m_N(x)
        \sum_j\frac{e^{i\gamma_{\chi,j}(L+x)}}{1+i\gamma_{\chi,j}}
      +\epsilon_\chi(x),\qquad
 \|Q_H\epsilon_\chi\|_2\ll_\kappa L(Ne^H)^{-\kappa}
 \tag{9}
$$
for fixed $0<\kappa<1/2$ with $\alpha<\kappa$. Here $p_\chi(x)$ is already interpreted after the exact unitary log change. The shifted line is still to the right of the imprimitive Euler-factor zeros after the shift in $s$ of $g_\chi(s)=L'/L(1/2+s,\chi)$, so precisely the nontrivial primitive zeros are crossed.

For completeness, cutoff sums in (9) converge locally in $L^2$ and also with the exterior weight. Let $T\ge2$ and consider a finite height segment $T<|\gamma_{\chi,j}|\le T'$. On any interval in $x$ of length 1, majorize its indicator by a translate of a fixed nonnegative smooth bump. Expanding the square of that finite series, the bump transform is $O((1+|\gamma-\gamma'|)^{-2})$ in absolute value, independently of the translation. Grouping ordinates by unit bins gives a summable Schur majorant in the bin difference, and the unit-bin zero count bounds the $\ell^2$ sum of the bin coefficient masses by
$$
 O\left(\sum_{|k|\ge T-1}
       \frac{\log^2(N(2+|k|))}{(1+|k|)^2}\right)
  \ll \frac{(L+\log(2+T))^2}{T}.
$$
Summing over the whole exterior with $m_N(x)^2\ll e^{-2\alpha(L+x)}$ costs $O(L)$ uniformly for $H\ge0$. This proves weighted $L^2$ convergence, and the cutoff error for the weighted atom is $O(\sqrt L\,(L+\log(2+T))/\sqrt T)$. It is consistent with the distributional contour identity, hence the same realization as (9).

The true atom average has $\operatorname{Avg}_\chi\|Q_Hp_\chi\|_2^2\ll L^2$ by Li–Liu Proposition 6.5. Thus replacing these atoms by the infinite residue atoms changes their exterior Gram in HS by $O_\kappa(L^2(Ne^H)^{-\kappa})$; use the rank-one HS norm and Cauchy–Schwarz in the character average. Replacing the latter by the common cutoff $T=L^{2K+6}$ adds $O(L^{-K-1/2})$ by the preceding weighted $L^2$ bound. The discarded tail of the linear diagonal (1) is $O(L(L+\log(2+T))/T)$ in HS by the same bin count and the $O(L)$ squared weight mass. These errors are uniform and smaller than the required inverse log.

The exact finite residual kernel is therefore
$$
 2\pi m_N(x)m_N(z)\operatorname{Avg}_{\chi\ {\rm odd}}
 \sum_{\substack{j\ne j'\\|\gamma_{\chi,j}|,|\gamma_{\chi,j'}|\le L^{2K+6}}}
 \frac{e^{i\gamma_{\chi,j}(L+x)-i\gamma_{\chi,j'}(L+z)}}
      {(1+i\gamma_{\chi,j})(1-i\gamma_{\chi,j'})}.
 \tag{10}
$$
Masking to $|x-z|\le B$ is a contraction in HS. Equations (2) and (9) therefore identify the true masked weak-S residual with (10), with $o(L^{-K})$ error. Additional orthogonal compression, including the weighted means of the fine-side reduction, is also an HS contraction. On actual full sub-blocks whose supports have log separations at most $B$ the mask can simply be omitted. Formula (10) includes distinct copies of a repeated ordinate. Neither its covariance magnitude nor its comparison to zero on the individual modulus is assessed by a single-level explicit formula. Outside the displayed log band, even the correction in (8) has no inverse-log consequence from the given absolute bound. This note therefore estimates a genuine signed component but not the whole mean–mean block.
