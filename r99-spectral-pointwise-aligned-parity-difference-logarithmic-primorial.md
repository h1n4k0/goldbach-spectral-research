# Full-strength pointwise exceptional parity difference with a logarithmic-size primorial cutoff

This concerns the real, actually retained exceptional correction to the two original mixed-strip parities. It strengthens the [smaller-primorial pointwise bound](r98-spectral-pointwise-aligned-parity-difference-small-primorial.md), not the [separate complete-family signed mean](r98-spectral-all-primorial-aligned-mean.md). In particular it keeps the pointwise completion margin; the mean does not need that margin. There is no claim that a qualifying zero exists, that either full parity is positive, or that the full mixed correlation or Hypothesis S is controlled.

Use the original tests and notation of the [pointwise aligned theorem](r97-spectral-pointwise-aligned-parity-difference-all-fixed-cuts.md). Thus $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, and the even target $N\in[Y,2Y]$ is divisible by $K_z=\prod_{p\le z}p$. The actual primitive real Page character $\chi$ has conductor $r\mid N$ and simple zero $\beta$ with $(1-\beta)G\le C_*\log G$, for fixed $C_*>0$. Keep $\log(Q_0/r)\ge(\log G)^3$ and the original nonnegative bounded-BV test $\omega$ on the real half-open $I\subset(N/2,9N/16]$, with $\int_I\omega\ge c_{\rm test}Y>0$. Let $B>B_0>0$ be fixed admissible cuts, $D=\sqrt N(\log N)^{-B}$, $\ell=\log z$, $U=(B-B_0)\log\log N$ and $T_x=\log(x/D^2)$ on $N-x\in I$. Both $U$ and $T_x$ are comparable to $\log G$ with fixed constants, and they are positive eventually.

**Theorem.** There is a sufficiently large fixed $K_0$ such that for all sufficiently large qualifying targets with

$$
    K_0\frac{\log G}{(\log\log G)^2}\le z\le Z
$$

the original actual exceptional parity difference satisfies

$$
 -\chi(-1)\bigl(\mathfrak E_+(N;I,\omega)-\mathfrak E_-(N;I,\omega)\bigr)
     \gg \frac{Y^{2\beta-1}}{G}\,\frac{\Sigma(N)}{(\log r)^4}.
 \tag{1}
$$

Constants may depend on the stated fixed parameters. No extra alignment $r\mid K_z$ is needed. When $r\mid K_z$ does happen, the same classical conductor growth used in R98's mean, $r>G^A$ for every fixed $A$ eventually in the near-zero range, gives $z/\log G\to\infty$ by $\log K_z\ll z$. Thus the new planting threshold is eventually automatic in that case, but the pointwise finite-denominator condition remains.

## 1. An ordinary reciprocal primitive with a uniform unintegrated bound

For $u\ge0$, put $m(u)=\sum_{n\le e^u}\mu(n)/n$ and $A^m(u)=\int_0^u m(v)\,dv$, with both zero for $u<0$. We use $0\le A^m(u)\ll1$, $A^m(u)\to1$, as in the [integrated rough argument](r98-spectral-all-primorial-aligned-mean.md). These follow from Theorem 1.2 with $q=k=\sigma=1$ and Corollary 3.4 of [Ramaré–Zuniga Alterman](https://arxiv.org/pdf/2312.05138v3), with the classical ordinary Möbius prime number theorem in the latter. We also use the stronger unintegrated bound $m(u)\ll(1+u)^{-2}$. Indeed the ordinary-frequency specialization of Davenport's bound, as recorded in [He–Huang (1.2)](https://www.impan.pl/shop/en/publication/transaction/download/product/91740?download.pdf=#page=1), gives $\sum_{n\le x}\mu(n)\ll x(\log x)^{-4}$ for $x\ge2$. Partial summation gives the convergence of $\sum_n\mu(n)/n$ and its tail bound $O((1+\log x)^{-3})$. The convergent sum is zero: partial summation against $n^{-s}$ makes its Abel limit at $s\downarrow0$ equal to its ordinary sum, and $1/\zeta(1+s)\to0$. This yields the claimed bound, including bounded $u$.

The reciprocal rough primitive $R_z^m$ only counts integers whose prime factors exceed $z$, and $A_z^m$ is its integral. Both are the respective convolutions of $m,A^m$ with the positive measure

$$
     \lambda_z=\sum_{a:\,p\mid a\Rightarrow p\le z}
                           \frac1a\,\delta_{\log a}.
$$

This is an exact Euler coefficient identity followed by integration. The full mass is $O(\ell)$ by the reciprocal prime bounds; in any unit real log interval the mass is $O(1)$ by comparison with the harmonic mass of all integers in that interval. Dividing distances $u-\log a\ge0$ into unit intervals and using $(1+u-\log a)^{-2}$ proves $\sup_u|R_z^m(u)|=O(1)$, uniformly in $z$. Positivity and boundedness of $A^m$ give $0\le A_z^m\ll\ell$; the terms $a\le\sqrt z$ alone give $A_z^m(u)\gg\ell$ for $u\ge\ell$, since $u-\log a\ge\ell/2$ there. For $0\le u\le\ell$ the two rough primitives are exactly $1,u$.

## 2. Transfer to the actual pointwise coefficients and real unit mask

Use the exact pointwise short coefficients $\alpha_p$ and prefactor $M=\mathcal N_\chi$ of the [completed aligned formula](r93-spectral-completed-colored-caps.md). In particular $\alpha_p=0$ at all primes dividing $N$. Set $b=1-\beta$ and for every $p>z$ put

$$
     a_p=(p-2)/(p-1),\qquad b_p=\frac{p^{-\beta}}{a_p+2p^{-\beta}}.
$$

The actual $\alpha_p\ge-b_p$, including zero at primes in $N$. Fix $U_*=C\log G$ with sufficiently large fixed $C$ so that $[0,U_*]$ includes $[0,U]$ and $[0,\ell]$ for all permitted targets. On this interval the primes above $e^{U_*}$ have no effect on any primitive. Each use of a series in $X$ at $p$ below encodes the shifts $k\log p$ for terms $X^k$.

Compare the all-minus factors $1-b_pX$ on $z<p\le e^{U_*}$ to the ordinary reciprocal factors $1-X/p$. The signed inverse quotient product $(1-b_pX)/(1-X/p)$ has atom one at zero, with remaining variation at most

$$
  \ll \sum_{z<p\le e^{U_*}}\frac{|b_p-1/p|}{1-1/p}
  \ll z^{1-2\beta}+bU_*e^{bU_*}=o(1).
 \tag{2}
$$

For the first estimate multiply one plus each local nonconstant variation; their sum is small. For the second, $|b_p-p^{-\beta}|\ll p^{-2\beta}+p^{-1-\beta}$ and $0\le p^{-\beta}-1/p\le b e^{bU_*}(\log p)/p$, with $\sum_{p\le t}(\log p)/p\ll\log t$. The square tails converge uniformly as $\beta\ge .99$ eventually. Convolve both primitives of Section 1 by this signed measure. On $[0,U_*]$ the resulting all-minus primitives satisfy $|R_-|\ll1$, $|A_-|\ll\ell$ and $A_-(u)\gg\ell$ for $u\ge\ell$, by (2), and they retain the exact shelf $1,u$ up to $\ell$. In particular $A_-(u)\ge0$ throughout this real interval.

To get the actual $R=R_1$ and its integral $A$, convolve $R_-,A_-$ with the finite-prime shift product of

$$
    \frac{1+\alpha_pX}{1-b_pX}
       =1+(\alpha_p+b_p)\sum_{k\ge1}b_p^{k-1}X^k .
$$

Every term is nonnegative and the local atom at zero is one. In particular at an actual extra prime $p\mid N$, $p>z$, the ratio is the **positive geometric series** $(1-b_pX)^{-1}$, not one. Let $D_+(v)$ denote the cumulative mass of the positive shift product up to $v$, including the atom at zero. Then

$$
   \sup_{0\le u\le U}|R(u)|\ll D_+(U),\quad
   \sup_{0\le u\le U}|A(u)|\ll \ell D_+(U),\quad
   A(U)\gg\ell D_+(U)\quad(U\ge\ell).
 \tag{3}
$$

The uppers follow from the actual finite convolution. To see the lower, when $\ell\le U\le2\ell$ use the zero shift and $D_+(U)\ll1$ by $\sum_{z<p\le z^2}1/p=O(1)$. For $U\ge2\ell$, retain the factors with $p\le\exp(U/M_0)$, for a large fixed $M_0$. Each local normalized mean log shift is
$(\alpha_p/(1+\alpha_p)+b_p/(1-b_p))\log p$, nonnegative and $O((\log p)/p)$ in the finite window. The total mean log shift is $O(U/M_0)$, so at least half of their positive mass lies at shifts $\le U/2$ by Markov. The remaining primes up to $e^U$ enlarge the total Euler mass by at most a fixed factor: their reciprocal sum is $O_{M_0}(1)$ by the reciprocal prime bounds. Primes beyond $e^U$ cannot enter the cumulative mass. As all omitted factors have a unit zero atom, $D_+(U/2)\gg D_+(U)$. Apply $A_-(U-s)\gg\ell$ for $s\le U/2$, obtaining (3). If $U<\ell$, the exact values are $D_+(U)=1$ and $R(U)=1,A(U)=U$ on the entire shelf.

## 3. Absolute log moments bound the true shifted tail error

The genuine color-one scalar in the pointwise theorem is $B_1(x)=T_x(C_\chi(0)-Q_\chi(U))+J_\chi(U)$. As in the [exact square-label form](r97-spectral-pointwise-aligned-parity-difference-all-fixed-cuts.md) (6), on division by $M$ the first cap is the signed sum of $\|R_j\mathbf1_{u>U-\log j}\|_2^2$ and the second is the signed sum of the squares of the integrals up to $U-\log j$. The common weight is $\mu(j)\alpha(j)^2$. For $j>e^U$ the first takes the whole norm and the second is zero. All functions vanish below zero. Global $L^2$ and convergence follow from the completed formula, with no bound on $E(U)=\int_U^\infty R^2$ needed below.

Inverse removal for a squarefree $j$ with $\alpha(j)\ne0$ is the exact convolution $R_j=R*\kappa_j$, where the local inverse factors are $(1+\alpha_pX)^{-1}$ at $p\mid j$. With $a'_p=|\alpha_p|$, let $V_j=\prod_{p\mid j}(1-a'_p)^{-1}$. The variation mass is at most $V_j$ and the absolute first shift moment is at most $V_j\sum_{p\mid j}a'_p\log p/(1-a'_p)$, by the geometric series. All $p$ here exceed $z$. The weighted absolute sums over $j>1$ satisfy

$$
 \sum_{j>1}|\alpha(j)|^2V_j^2\ll z^{1-2\beta},\qquad
 \sum_{j>1}|\alpha(j)|^2V_j^2\sum_{p\mid j}\frac{\log p}{1-a'_p}
                      \ll z^{1-2\beta}.
 \tag{4}
$$

Indeed set $w_p=(a'_p)^2/(1-a'_p)^2$. The first bound is from $\prod(1+w_p)-1$; the second expands as $\prod(1+w_p)\sum_{p>z}w_p\log p/[(1+w_p)(1-a'_p)]$. Here $a'_p\ll p^{-\beta}$ on the whole half-line $p>z$ by the actual aligned coefficients. The log-weighted prime tail is $O(z^{1-2\beta})$ by partial summation of $\sum_{p\le t}\log p\ll t$, without an extra factor $\log z$.

Let $S(U)=\sup_{0\le u\le U}|R(u)|$. Cauchy–Schwarz in $d|\kappa_j|(s)$ before the norm integration gives

$$
 \|R_j\mathbf1_{u>U-\log j}\|_2^2
 \le V_j^2 E(U)+V_j^2S(U)^2\sum_{p\mid j}\frac{\log p}{1-a'_p}.
$$

The extra portion below $U$ after shifting has length at most $\log j+s$, and the first log moment yields precisely the second term. The $j=1$ contribution to the cap is $E(U)$, hence (4) implies
$(C_\chi(0)-Q_\chi(U))/M\ge -O(z^{1-2\beta}S(U)^2)$.
For the other cap, the shifted integral of $R_j$ equals $(A*\kappa_j)(U-\log j)$ when $j\le e^U$. Thus by (3)–(4),
$J_\chi(U)/M\gg\ell^2D_+(U)^2$ for $U\ge\ell$, and it is exactly $U^2$ for $U\le\ell$ because no $j>1$ contributes there.

As $z\le Z$ and $b\ell=o(1)$, $z^{1-2\beta}\ll1/z$. Our lower assumption gives $\ell\ge\tfrac12\log\log G$ eventually, and therefore $T_x z^{1-2\beta}/\ell^2\ll 1/K_0$. Choosing $K_0$ sufficiently large absorbs the possible negative tail into the lower for the squared integral when $U\ge\ell$. For $U\le\ell$, $S(U)=1$ and $U\asymp T_x\asymp\log G$, so absorption into $U^2$ follows directly. Also $U\gg\ell$ there, using $\ell\le\log G$. Uniformly on the actual physical support this proves

$$
                         B_1(x)\gg M\ell^2D_+(U)^2 .
 \tag{5}
$$

## 4. The same shifts recover the pointwise normalization

The exact normalized prefactor is R97's identity (9), which we keep pointwise:

$$
 \frac{M}{\Sigma(N)}
 =\frac1{L'(\beta,\chi)^2}
    \prod_{\substack{p\mid N\\p\nmid r}}(1-\chi(p)p^{-\beta})^{-2}
    \prod_{p\nmid N}(1-\chi(p)p^{-\beta})^{-2}
                          (1-2\chi(p)p^{-\beta}/a_p).
 \tag{6}
$$

All $p\nmid N$ exceed $z$ and their coupled logarithms have total absolute value $O(\sum_{p>z}(p^{-1-\beta}+p^{-2\beta}))=o(1)$ by first-order cancellation. By R97 and the small-exception-branch estimate in [Montgomery–Vaughan, Chapter 11 (11.10)](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF), $|L'(\beta,\chi)|\ll(\log r)^2$. The finite $N$-product is bounded below by $\exp(-2\sum_{p\mid N,\,p\nmid r}p^{-\beta})$. Its part at $p\le z$ is $\gg\ell^{-2}$ by the reciprocal prime bound with leading coefficient one and $b\ell=o(1)$, more precisely the sum of the exponent changes is $O(b\ell e^{b\ell})$.

For larger primes dividing the real $N$ and not $r$, retain in the positive shift product just the factors with $z<p\le \exp(U/M_0)$. Their exact geometric Euler mass is $\prod(1-b_p)^{-1}\gg\exp(\sum p^{-\beta})$ over that subset, since $b_p=p^{-\beta}+O(p^{-2\beta}+p^{-1-\beta})$ and the error sum is bounded. The normalized mean log shift from just these factors is again $O(U/M_0)$; marking shifts $\le U/2$ keeps at least half of this mass. As all other positive factors carry unit atoms at zero, $D_+(U)$ dominates the resulting mass. This argument also holds with the empty retained product (notably if $U<\ell$). The other $p\mid N$ above $\exp(U/M_0)\ge G^c$ for a fixed $c>0$ have $\sum p^{-\beta}=O(1)$: between $G^c$ and $G$ this follows from the reciprocal prime estimate and the uniform exponent change; above $G$ there are at most $O(G/\log G)$ actual prime divisors of $N$, each at most $G^{-\beta}\ll1/G$. In particular no upper bound on the number of prime factors in the small retained range is used. Combining these facts with (6) gives

$$
                      M\ell^2D_+(U)^2\gg
                                      \frac{\Sigma(N)}{(\log r)^4}.
 \tag{7}
$$

Finally subtract the two actual exceptional parities in the original aligned completion. By R97 (11), multiplication by $-\chi(-1)$ leaves the real integral of $\omega(N-x)(N-x)^{\beta-1}x^{\beta-1}B_1(x)/\log x$, with $O_A(Y^\beta G^{-A})$ for every fixed $A$ under the retained denominator margin. Equations (5) and (7), nonnegative $\omega$ and its physical mass give (1), since $x,N-x\asymp Y$. The absolute error is absorbed by choosing $A>C_*+4$: $Y^{\beta-1}\ge G^{-C_*}$, $\log r\ll\sqrt G$, and $\Sigma(N)$ has a positive absolute lower bound for even $N$. This is only a sign and size statement for the genuine exceptional parity difference on the specified hypothetical aligned targets.
