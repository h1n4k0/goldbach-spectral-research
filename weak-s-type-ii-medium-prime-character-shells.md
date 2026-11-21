# Dyadic-character shells for the actual balanced medium-prime remainder

Keep the exact $N=2^j$ balanced boxes of the [short-divisor result](weak-s-type-ii-balanced-short-divisor.md) with $X=\sqrt N,\ L=\log N$:

$$
 I=[.740X,.745X],\qquad J=[.715X,.720X],\qquad D=[.445X,.450X].
$$

Take $Y=N^{.024},\ V=N^{.2499}$ and the genuine remaining weight

$$
 w(v)=\sum_{\substack{Y<p\le V\\p\,{\rm prime},\,p\mid v}}\log p.
$$

Let $\mathcal S=\mathcal A_N(w)$ with the exact squarefree gate and cutoffs in that result. Thus the original balanced contribution is $-\mathcal S+O_A(NL^{-A})$. The following statements concern this same signed statistic.

1. **Unconditional:** in the exact fixed-modulus expansion, each of the leading six primitive shells is proportional to $\mathcal S$, and for the leading three this holds in each parity separately. In the $c=1$ summand, the product of the four separate Hölder norms with exponents $p_i\ge2$ is at least of order $NL$ on each leading parity shell. This bounds the size of that separate-norm estimate from below, not the absolute moment of the product or the signed remainder.
2. **Global Dirichlet GRH:** in that exact expansion the principal term contributes $O_\epsilon(N^{1/2+\epsilon})$, and any subfamily of at most $M_*$ nonprincipal characters (with arbitrary additional weights of modulus at most 1) contributes $O_\epsilon(M_*N^\epsilon)$. In particular, characters of conductor at most $N^{1-\kappa}$ are discardable at a power saving for every fixed $\kappa>0$. No claim of cancellation of the remaining dense high-conductor shell is made.

The representation, shell identities, and conditional subfamily bound also hold for arbitrary subintervals of $I,J,D$, with the same cutoffs. The lower bound for the separate Hölder method uses the full displayed boxes. These are statements about a method and a filtered contribution, not a lower or upper bound on the unfiltered signed $\mathcal S$, all Type II, or weak S.

## 1. Exact geometry and algebra of the fixed modulus

Add $K=[1.03X,1.06X]$ for $k$. On the true equality $uv+dk=N$ in $I,J,D$, the quotient $(N-uv)/d$ lies in $K$; indeed its extremes are $(1-.5364)X/.450>1.03X$ and $(1-.5291)X/.445<1.06X$. The gate $k>\sqrt N$ is unchanged. On the entire independent box $I\times J\times D\times K$ we have

$$
 .98745N\le uv+dk\le1.0134N,\qquad
 .0521N\le uv-dk\le.07805N .
$$

As $N=2^j$, the unit condition on the actual equality is precisely that all four variables are odd. For $q=N/2^s,\ 0\le s\le6$, the congruence $uv\equiv -dk\pmod q$ on the whole box is therefore precisely equality. For $0\le s\le3$, $uv\equiv dk\pmod q$ is impossible. These comparisons do not use an average or an approximation of a moving cutoff.

Expand $\mu(d)\mu^2(dk)=\mu(d)\mu^2(k)\sum_{c\mid(d,k)}\mu(c)$. For $d=cd_1,\ k=ck_1$ the summand $\mu(c)\mu(d)\mu^2(k)$ is exactly

$$
 \mu^2(c)\mu(d_1)\mu^2(k_1){\bf1}_{(d_1k_1,c)=1}.
$$

For instance the factor is zero if $c$ is not squarefree or some prime of $c$ divides either quotient; otherwise the two signs $\mu(c)$ cancel. For a character $\chi$ modulo an even $q\mid N$, define

$$
 \begin{array}{ll}
 U(\chi)=\sum_{u\in I}\mu(u)\chi(u),&
 V_w(\chi)=\sum_{v\in J}w(v)\chi(v),\\[2pt]
 D_c(\chi)=\sum_{\substack{d_1\in D/c\\(d_1,c)=1}}\mu(d_1)\chi(d_1),&
 K_c(\chi)=\sum_{\substack{k_1\in K/c\\(k_1,c)=1}}\mu^2(k_1)\chi(k_1).
 \end{array}
$$

Even integers are discarded by the characters themselves. Put

$$
 {\cal W}(\chi)=U(\chi)V_w(\chi)
  \sum_{\substack{c\le .450X\\c\ {\rm odd}}}
    \mu^2(c)\overline{\chi(c)}^{\,2}
                     D_c(\overline\chi)K_c(\overline\chi).
$$

There is no truncation of $c$. Orthogonality gives, for all $q=N/2^s,\ 0\le s\le6$,

$$
 \sum_{\chi\bmod q}\chi(-1){\cal W}(\chi)=\varphi(q)\mathcal S . \tag{1}
$$

The weighting is $\chi(-1)$, not a chosen parity: the congruence indicator is the average of $\chi(-1)\chi(uv)\overline{\chi(dk)}$. For $0\le s\le3$, orthogonality without $\chi(-1)$ likewise gives $\sum_{\chi\bmod q}{\cal W}(\chi)=0$.

All factors are unchanged when lifting a character modulo $q/2$ to $q$, because both characters vanish at even integers and agree everywhere else. Subtracting (1) at consecutive levels, for $0\le s\le5$ and $q=N/2^s$,

$$
 \sum_{\chi\bmod q}^{\rm primitive}\chi(-1){\cal W}(\chi)
     =\bigl(\varphi(q)-\varphi(q/2)\bigr)\mathcal S. \tag{2}
$$

For $0\le s\le2$, (2) holds with the sum restricted to either parity and the factor on the right divided by 2; this follows by the vanishing of the unweighted primitive sum from the two exact absence statements. Thus dropping a dyadic high-conductor shell or switching parity does not bypass the true signed correlation. The identities alone do not bound that correlation.

## 2. Separate-moment obstruction on leading shells

Use $c=1$ in the exact coprimality expansion. For any of the four Dirichlet polynomials $P=U,V_w,D_1,K_1$ with coefficients $a_n$ on its indicated odd integers, and either parity $\pm$, orthogonality gives

$$
 \sum_{\substack{\chi\bmod q\ {\rm primitive}\\\chi(-1)=\pm1}}
                |P(\chi)|^2
   =\frac{\varphi(q)-\varphi(q/2)}{2}\sum_n|a_n|^2
       \qquad(q=N/2^s,\ 0\le s\le5). \tag{3}
$$

Indeed the two projectors for parity involve the congruences $n\equiv m$ and $n\equiv-m$; at both moduli $q,q/2$, all sums $n+m$ and differences $|n-m|$ from a single support are strictly smaller than the modulus for large $N$, so only the equality diagonal occurs. The bar on the character in two of the factors has no effect on these moments.

In the three $U,D_1,K_1$ factors the coefficient square sum is $\asymp X$, by the elementary count of odd squarefree integers. For $V_w$, take primes in the subband $N^{.10}\le p\le N^{.11}$ of the true medium range. The number of odd multiples in $J$ is $|J|/(2p)+O(1)$, so their total incidences are $\gg X$ by the prime number theorem and partial summation, since the reciprocal prime sum tends to $\log(.11/.10)>0$ and the $O(N^{.11})$ error is smaller than $X$. Each $v$ has at most five such prime divisors and its weight is at least $.10L$ if one occurs. Hence $\sum_{v\ {\rm odd}}w(v)^2\asymp XL^2$, using $w(v)\le\log v$ for the upper bound.

Normalize the sums in (3) by $\varphi(N)$. The measure of any indicated primitive parity shell is bounded below by a positive absolute constant. Each of its $L^{p_i}$ norms for $p_i\ge2$ is at least the $L^2$ norm on that subprobability space. The product of four such norms is therefore $\gg X^2L=NL$. This includes $(4,4,4,4)$ Hölder, on the exact high-conductor shell rather than just on all characters. Its failure to yield a saving does not imply the signed four-factor correlation is large; in particular it says nothing about cancellation within a shell or before absolute values across $c$.

## 3. Uniform global-GRH sparse-family estimate

We use the usual height-uniform consequences of global Dirichlet GRH on $\sigma\ge1/2+\delta$, for each fixed $\delta,\epsilon>0$: $1/L(s,\chi)\ll (q(|\Im s|+2))^\epsilon$ for all characters (including the reciprocal zero at the principal pole), and $L(s,\chi),\, L'/L(s,\chi)$ have this bound for nonprincipal characters. These follow from the same zero-free half-plane logarithm and interpolation argument as in the [twisted Möbius estimate](weak-s-type-ii-character-average.md#2-exact-perron-separation-and-an-all-character-mean-square). For nonprincipal $\chi$, fix a logarithm by the Euler product; Borel–Carathéodory just to the right of the line $\sigma=1/2$ gives $O_\delta(\log(q(|t|+2)))$, using the polynomial growth bound for $L$; interpolate with its bounded Euler expansion at $1+\delta'$ to get $o_\delta(\log(q(|t|+2)))$ on the indicated half-plane. Cauchy's formula on a smaller fixed-margin disk bounds the logarithmic derivative. The principal logarithm uses the removable normalization $(s-1)/(s+1)$. Missing imprimitive factors and extra finite factors $\prod_{p\mid c}(1\pm\chi(p)p^{-s})^{\pm1}$ cost $N^\epsilon$ for $c,q\le N$ on this line, by splitting the product at a sufficiently large fixed prime bound. The estimate can therefore be used throughout polynomial heights, with any prescribed exponent $N^\epsilon$ after relabeling small constants.

For interval sums on scale $Z\le O(N)$, apply truncated Perron at half-integer endpoints on $\Re s=2$, with height $T=N^4$, and shift to $\Re s=1/2+\delta$. For coefficients $O(\log n)$ or bounded, the initial error is $O(Z^2\log^2(2N)/T)$; the horizontal integrals are $O(N^\epsilon Z^2/T)$ for a pole-free subpower Dirichlet series throughout the strip. The shifted line gives $O_\epsilon(N^\epsilon\sqrt Z)$, with $\delta$ small enough and the integration logarithm absorbed. Only interval differences at endpoints in the same indicated scale are needed. For $\mu(n)\chi(n){\bf1}_{(n,c)=1}$, the series is $1/L(s,\chi)$ with finite corrections; thus $U\ll_\epsilon N^\epsilon\sqrt X$ and $D_c\ll_\epsilon N^\epsilon\sqrt{X/c}$, even for the principal character. For nonprincipal $\chi$, the squarefree series for $K_c$ is $L(s,\chi)/L(2s,\chi^2)$ with the factors $(1+\chi(p)p^{-s})^{-1}$ at $p\mid c$; the denominator inverse is absolutely bounded for $\Re s>1/2+\delta$, also when $\chi^2$ is principal. Thus $K_c\ll_\epsilon N^\epsilon\sqrt{X/c}$ for nonprincipal $\chi$.

For precision the $V_w$ bound here treats the actual medium primes and hard $v$-interval, not prime averages at a different scale. Its series is

$$
 L(s,\chi)\sum_{Y<p\le V}(\log p)\chi(p)p^{-s}.
$$

For nonprincipal $\chi$, the finite factor is $O_\epsilon(N^\epsilon)$ on $\Re s\ge1/2+\delta,\ |\Im s|\le T$. To see this, apply the same Perron shift to $-L'/L(s+i\tau,\chi)$ for prime-power prefixes $z\le V,\ |\tau|\le T$, with height $T$ so the entire contour lies at heights at most $2T$ in the unshifted $L$-function. There is no pole in this nonprincipal case. It gives $O_\epsilon(N^\epsilon\sqrt z)$ for the twisted Λ sums; removing proper prime powers costs $O(\sqrt z\log^2(2z))$ in absolute terms. Partial summation on the *real* weight $p^{-\sigma}$, with the imaginary twist already included, gives the finite factor bound. The product series is then holomorphic and subpower throughout the Perron shift for $V_w$, yielding $V_w\ll_\epsilon N^\epsilon\sqrt X$ uniformly over the hard interval $J$. For the principal character use only $V_w\ll XL,\ K_c\ll X/c$, where $c\le.450X$.

Consequently each nonprincipal ${\cal W}(\chi)$ is $O_\epsilon(N^{1+\epsilon})$: its per-$c$ product is at most $N^\epsilon X^2/c$, and the harmonic $c$-sum costs a logarithm. For the principal character the analogous bound is $O_\epsilon(N^{3/2+\epsilon})$ via $X^3/c^{3/2}$. Dividing by $\varphi(N)$ proves the stated two contribution estimates. Lifting counts at most $\varphi(2^r)$ characters of conductor at most $2^r$, which proves the stated power saving for the sparse low-conductor set. This only controls thin subfamilies of the exact signed response; it neither provides nor assumes joint cancellation in a positive-density family of large conductors.
