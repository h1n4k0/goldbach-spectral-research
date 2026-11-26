# A smaller primorial suffices for the pointwise aligned exceptional parity difference

**Scope.** The [pointwise aligned exceptional parity-difference bound](r97-spectral-pointwise-aligned-parity-difference-all-fixed-cuts.md) holds on a wider set of actual targets after reducing the required primorial. The targets still have to align with a hypothetical sufficiently close primitive real Page zero and satisfy the original finite-denominator margin. The result is pointwise for the actual exceptional correction, not a signed dyadic mean, a statement of existence, or a positivity result for the full mixed-strip correlation or either parity separately. No Dirichlet GRH or external zero-gap premise is used.

Use exactly the notation and assumptions of that pointwise theorem, except for the lower bound on the planting cutoff $z$. Thus $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $Y\le N\le2Y$ is even, $K_z=\prod_{p\le z}p\mid N$, and $r\mid N$ is the genuine primitive real Page conductor with simple zero $\beta$. Use the original condition $\log(Q_0/r)\ge(\log G)^3$ and suppose $(1-\beta)G\le C_*\log G$ for fixed $C_*>0$. The margin implies the original completion error $O_A(Y^\beta G^{-A})$ for arbitrary fixed $A>0$; equivalently its actual weaker sufficient margin can be used for a large enough fixed $A$. All hard left and right cuts are unchanged: $I\subset (N/2,9N/16]$ real and half-open, $\omega\ge0$ pointwise BV with fixed bounds and $\int_I\omega\ge c_{\rm test}Y>0$, and any fixed admissible $B>B_0>0$. Put

$$
 \ell=\log z,\qquad U=(B-B_0)\log\log N,\qquad
 M=\max(2,U/\ell),\qquad T_x=\log(x/D^2).
$$

Here $D=\sqrt N(\log N)^{-B}$ is the original divisor cutoff and $N-x\in I$. In particular $U,T_x\asymp\log G$ with fixed constants.

**Theorem.** For a sufficiently large fixed $K_0$ (depending on the fixed cutoffs and the absolute prime-theorem constant), assume only

$$
          K_0\bigl((\log G)\log\log G\bigr)^{2/3}
                            \le \ell,\qquad z\le Z .                \tag{1}
$$

There is a fixed $C_1>0$ such that at every sufficiently large qualifying target

$$
 -\chi(-1)\bigl(\mathfrak E_+(N;I,\omega)-\mathfrak E_-(N;I,\omega)\bigr)
 \gg
   \frac{Y^{2\beta-1}}G\,\frac{\Sigma(N)}{(\log r)^4}
                   \exp\{-C_1M\log(2M)\}.                           \tag{2}
$$

The factor on the right is pointwise $\Sigma(N)$, not an averaged primorial normalization. The extra exponential factor is $G^{-o(1)}$ uniformly in (1). In particular the exceptional parity difference still has the strict sign $-\chi(-1)$. The lower range for $z$ in (1) permits very substantially smaller primorials than $z\ge G^\epsilon$ for any fixed $\epsilon>0$. No assertion is made on an unaligned target or one lacking the actual completion margin.

## 1. Exponential prime-prefix control in the genuine Euler comparison

Use the exact pointwise short factors $\alpha_p$ of the [aligned color model](r93-spectral-completed-colored-caps.md), including all actual additional primes dividing $N$. For $p>z$ set

$$
 a_p=(p-2)/(p-1),\qquad b_p=p^{-\beta}/(a_p+2p^{-\beta}).
$$

The baseline squarefree coefficients have prime values $-b_p$ on $p>z$, zero on smaller primes, and coefficient one at the integer $1$. Let $R_-(u)$ be their sum up to $e^u$, extended by zero for $u<0$. As in the fixed-cut proof, since $\alpha_p\ge-b_p$, the exact local ratio

$$
      \frac{1+\alpha_p X}{1-b_pX}
       =1+(\alpha_p+b_p)\sum_{k\ge1}b_p^{k-1}X^k
$$

has nonnegative coefficients. Thus the actual $R_1$ is the convolution of $R_-$ with a positive correction on nonnegative log positions, with atom one at zero. This is a locally finite coefficient identity and uses no absolute unweighted sum over infinite primes. Those $p>z$ that divide the actual $N$ are included with $\alpha_p=0$ in the ratio.

Let $\nu_z=\sum_{z<p\le z^M}b_p\delta_{\log p/\ell}$ and $\nu=\mathbf1_{[1,M]}(v)\,dv/v$, both nonnegative finite measures. For a finite signed measure $\lambda$ write $\|\lambda\|_{\rm pr}=\sup_s|\lambda((-\infty,s])|$. Uniformly under (1), for an absolute $c>0$ we have

$$
       \|\nu_z-\nu\|_{\rm pr}\ll e^{-c\sqrt\ell},\qquad
       \max(\nu_z(\mathbb R),\nu(\mathbb R))
                        =\log M+O(e^{-c\sqrt\ell}).                 \tag{3}
$$

Indeed the [classical quantitative PNT, Montgomery--Vaughan, Theorem 6.9 (6.14)](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287) gives $\pi(t)=\operatorname{li}(t)+O(t e^{-c_0\sqrt{\log t}})$ uniformly for $t\ge2$. In Stieltjes partial summation against $t^{-1}$, the $\operatorname{li}$ contribution on $(z,z^s]$ is **exactly** $\int_z^{z^s}dt/(t\log t)=\log s$. The endpoint residuals are $O(e^{-c_0\sqrt\ell})$; the remaining error is bounded by an absolute constant times

$$
               \int_\ell^\infty e^{-c_0\sqrt w}\,dw
                              \ll e^{-c\sqrt\ell}.
$$

This is uniform in real $1\le s\le M$, including all literal weak endpoint primes. Below $1$ both prefixes vanish and above $M$ they are the two total masses. Also $M\ell=\max(2\ell,U)\ll\log G$ and $1-\beta=O(G^{-1/2})$ by the Page range. Uniformly in the primes in $\nu_z$,

$$
 b_p=\frac1p+O\!\left(\frac{G^{-1/2}\log G}{p}+\frac1{p^2}\right).
$$

This follows by writing $p^{1-\beta}=\exp((1-\beta)\log p)$ and using $a_p=1+O(1/p)$. The total weight change is $O(G^{-1/2}\log G\log(2M)+z^{-1})$, which is absorbed by the error in (3) since $\ell\le\log G$. In particular (3) is not a claim from an unquantified prime asymptotic.

## 2. Sum convolution errors before comparing with the positive profile

Let $A_0=\max(\nu_z(\mathbb R),\nu(\mathbb R))$ and $E=\|\nu_z-\nu\|_{\rm pr}$. Convolution of a signed prefix discrepancy with a nonnegative finite measure of total mass $A$ costs at most $EA$, by integrating the signed prefix shifted by each atom or integration variable of the latter. Telescope the $j$th powers, using this bound on each term to obtain

$$
          \|\nu_z^{*j}-\nu^{*j}\|_{\rm pr}
                                      \le j E A_0^{j-1}\quad (j\ge1).
$$

The absolutely weighted sum of errors with factors $1/j!$ is therefore at most $Ee^{A_0}\ll M e^{-c\sqrt\ell}$, by (3). For the prime tuples the contribution from repeated primes is bounded before imposing the sum cutoff by $\binom j2 A_0^{j-2}\sum_{p>z}b_p^2$ for $j\ge2$; summing with $1/j!$ costs $O(e^{A_0}z^{1-2\beta})$, again smaller. Here $\beta\ge .99$ eventually and the integer sum bounds the square tail. The true expansion of $R_-(\ell t)$ over distinct ordered prime factors uses the sign $(-1)^j$ and the factor $1/j!$, and every such prime is in the window when $t\le M$. Thus exactly as in the finite formula of the fixed-cut theorem,

$$
       R_-(\ell t)=\rho(t)+O(M e^{-c\sqrt\ell})
                       \qquad (0\le t\le M),                       \tag{4}
$$

where $\rho$ is the Dickman function in that theorem. Its alternating convolution expression with $\nu$ agrees up to $M$, since no summand greater than $M$ can be involved in any of these prefixes. The atom for $j=0$ is exactly one. No convergence of signed transforms in total variation or restriction of the target family has been used.

For an explicit lower over this growing range, the fixed-cut Dickman proof gives $\rho(t)=1$ on $0\le t\le1$, positivity, $t\rho'(t)=-\rho(t-1)$ a.e. for $t>1$, and
$t\rho(t)=\int_{t-1}^t\rho(v)\,dv$ for $t\ge1$. It is therefore nonincreasing on the nonnegative half-line. For $t\ge1$ that integral is at least $\tfrac12\rho(t-1/2)$; iteration yields

$$
              \rho(t)\ge \exp\{-C_2 t\log(2t)\}
                                 \quad(t\ge1)
$$

with an absolute $C_2$, by replacing each of the $O(t)$ inverse factors $1/(2v)$ by $1/(2t)$. Under (1), $M\log(2M)\ll 1+(\log G)\log\log G/\ell$ with a constant depending only on the fixed cuts. Our choice of sufficiently large $K_0$ ensures

$$
 M e^{-c\sqrt\ell}=o\!\left(e^{-C_2 M\log(2M)}\right).
$$

For example $\ell^{3/2}\ge K_0^{3/2}(\log G)\log\log G$ allows $c\sqrt\ell$ to exceed $4(1+C_2)M\log(2M)$ for large $G$; if $M$ is bounded the comparison follows directly. The positive correction then uses only positive $R_-$ values on the appropriate nonnegative interval or zero below zero. Its atom at zero and (4) yield

$$
             R_1(u)\gg e^{-C_2 M\log(2M)}\qquad (0\le u\le U).      \tag{5}
$$

We also need a polynomial upper independent of the character's signs. For $p>z$ in the same window,

$$
     |\alpha_p|\le p^{-1}
                +O\!\left(\frac{G^{-1/2}\log G}{p}+\frac1{p^2}\right)
$$

by the formula for its local denominator (a zero coefficient only helps). Consequently the absolute coefficient sum up to $e^u$ is bounded by $\prod_{z<p\le z^M}(1+|\alpha_p|)\ll M$, by the sharp reciprocal mass in (3), not merely a constant multiple of $\log M$ in the exponent. This proves $R_1(u)\ll M$ on $[0,U]$. The constants in (5) and this upper are uniform throughout (1).

## 3. Absorbing the signed tails in the actual cap

Use the same real positive prefactor $\mathcal N_\chi$ of the aligned model; all sufficiently small primes divide $N$, so all remaining ordinary local factors are positive. Put $R=R_1$ and $a_j=(U-\log j)_+$. The exact shifted scalar of the [second-color proof](r96-spectral-aligned-second-color-two-frequency.md) is

$$
 B_1(x)=\mathcal N_\chi\sum_j\mu(j)\alpha(j)^2
       \left\{T_x\int_{a_j}^\infty R_j(v)^2dv+
                               \left(\int_0^{a_j} R_j(v)\,dv\right)^2\right\},
                                                                     \tag{6}
$$

with squarefree $j$. In particular the real tail starts at zero and the finite square vanishes if $j>e^U$. The masked profiles are the same as before. For each nonzero $\alpha(j)$, removing its prime factors is convolution by the signed geometric measure of variation at most $\prod_{p\mid j}(1-|\alpha_p|)^{-1}$; this follows by coefficient identity since each $|\alpha_p|<1$ for $p>z$. Young's inequality and the product of the resulting square weights yield

$$
 \sum_{j>1}|\alpha(j)|^2 \|R_j\|_2^2
 \le
    \|R\|_2^2
     \left\{\prod_{p>z}
          \left(1+\frac{|\alpha_p|^2}{(1-|\alpha_p|)^2}\right)-1\right\}
 \ll z^{1-2\beta}\|R\|_2^2 .
$$

Thus the whole $j>1$ term of (6) is
$O(\mathcal N_\chi z^{1-2\beta}(T_x+U)\|R\|_2^2)$, by the finite-interval Cauchy estimate. Choose a fixed $C_3$ with $\int_0^U R^2\le C_3 U M^2$, using the genuine upper just proved. If $\|R\|_2^2\ge2 C_3 U M^2$, the $j=1$ tail is at least half the total norm, and $T_x\asymp U$ allows it to absorb the error. The resulting lower is at least a constant times $\mathcal N_\chi T_x U M^2$.

Otherwise the error is $O(\mathcal N_\chi (\log G)^2 M^2 z^{1-2\beta})$. Since $\ell\gg M\log(2M)$ with ratio tending to infinity under (1), this is negligible relative to the $j=1$ square from (5), which is $\gg\mathcal N_\chi U^2\exp(-2C_2 M\log(2M))$. Thus in either case

$$
           B_1(x)\gg \mathcal N_\chi(\log G)^2
                           e^{-C_1 M\log(2M)}
$$

uniformly for the literal physical $x$. Here fixed $B-B_0>0$ implies $U\asymp\log G$; no bound depending on a presumed relation $U\le\ell$ is needed. In particular this is a lower for the specific finite scalar, not an operator positivity conclusion.

The pointwise prefactor proof of the earlier theorem applies with $\log G$ instead of $\ell$: outside $N$ all primes exceed $z$, their factor ratio has absolutely summable logarithmic error $O(\sum_{p>z}(p^{-\beta-1}+p^{-2\beta}))=o(1)$, and the exact finite $N$-product is bounded below by $\exp(-2\sum_{p\mid N}p^{-\beta})\gg(\log G)^{-2}$. That reciprocal bound requires only true $N\in[Y,2Y]$, splitting at $G$ and using the leading coefficient one in the reciprocal prime estimate, independent of the planting size. With the same near-exception derivative bound $|L'(\beta,\chi)|\ll(\log r)^2$, this gives
$\mathcal N_\chi/\Sigma(N)\gg(\log G)^{-2}(\log r)^{-4}$.
It is important here to pair this estimate with $U^2\asymp(\log G)^2$, not $\ell^2$.

Finally subtract the two actual parities as in the preceding pointwise theorem. The first color cancels, the second has prefactor $-\chi(-1)$, and the real integral gives exactly the lower in (2), apart from the original $O_A(Y^\beta G^{-A})$ error. Nonnegative $\omega$ with the stated integral and $x,N-x\asymp Y$ ensure the physical lower factor $Y^{2\beta-1}/G$. Under (1), $M\log(2M)=o(\log G)$; also $Y^{\beta-1}\ge G^{-C_*}$, $(\log r)^4\ll G^2$, and $\Sigma(N)$ is bounded below in the even case. A sufficiently large fixed $A$ absorbs the error. The argument uses the same original denominator and gives no implication of the existence of the designated exceptional zero.
