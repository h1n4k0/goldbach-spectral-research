# Three fixed 2-adic channels of the complete exceptional mean

**Scope.** This extends the genuine **signed dyadic mean** to fixed bounded modulations of the original full-primorial family. An even Page conductor can vanish from the ordinary signed mean yet survive in exactly one of two fixed 2-adic channels. The amplitude is the same finite completed cap as in the aligned mean, with a known channel factor. The quantitative lower bound is conditional on an actual sufficiently close Page zero whose odd conductor part lies on the primorial. Neither its existence nor pointwise signs or sizes, full mixed-strip positivity, a prime-pair count, or Hypothesis S is asserted. There is no Dirichlet GRH or external zero-gap input.

Keep the [actual complete-planting signed-mean setting](r95-spectral-complete-planting-signed-mean.md): $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, actual even $N\in[Y,2Y]$, fixed admissible $B>B_0>0$, and the original exceptional corrections $\mathfrak E_\pm(N)$ for the even and odd squarefree factor-count sectors. Use the same common scaled tests $I_N=NJ$, where $J\subset(1/2,9/16]$ is real half-open, $\omega_N(u)=w(u/N)$, and the dyad weight $\eta(N/Y)$. The weights are bounded and of bounded variation, uniformly, and common across the dyad. They may be real signed or complex in the exact formulas, by linearity in the left and dyadic weights. Assume $2\le z\le Z$, take the full primorial $K_z=\prod_{p\le z}p$ fixed across the dyad, and put $M=4K_z$, with $M\le e^{2Z}$. The last bound holds throughout this range for all sufficiently large $Y$, since $\sum_{p\le z}\log p\sim z$ as $z\to\infty$; it is also automatic for bounded $z$. Write

$$
  \langle F\rangle_{K_z}
  =\frac{K_z}{Y}
       \sum_{\substack{Y\le N\le2Y\\K_z\mid N}}\eta(N/Y)F(N),
  \qquad
  f_0(N)=1,\quad f_2(N)=(-1)^{N/2},\quad f_3(N)=\cos(\pi N/4).
 \tag{1}
$$

The three $f_j$ are defined on even integers; they do not depend on a character or the scale.

When the actual Page zero $\beta>1-4a_0/\sqrt G$ exists, let $\chi$ be its primitive real character of conductor $r$, and write $r=2^e r_{\rm odd}$. The exponent $e$ is one of $0,2,3$, and $r_{\rm odd}$ is squarefree. If $r_{\rm odd}\mid K_z$, then $r\mid M$; in that case define the cap integrals over real variables from [the aligned complete mean formula](r96-spectral-aligned-mean-euler-collapse.md), used with sampling modulus $M$:

$$
 P_i=\frac1Y\int_Y^{2Y}\eta(v/Y)
          \int_{v-x\in vJ}
           \frac{ w((v-x)/v)(v-x)^{\beta-1}x^{\beta-1}}{\log x}
                    \mathcal A_i(v,x)\,dx\,dv
 \qquad(i=0,1).
 \tag{2}
$$

The caps here are exactly R96 (2)--(4) with $K=M$, $U_v=(B-B_0)\log\log v$, and $T_{v,x}=2B\log\log v+\log(x/v)$. In particular no new Ramanujan range or cap is used. Define $s_0=s_2=1$, $s_3=1/2$.

**Theorem.** If no Page zero exists then all three modulated exceptional means are zero. With the actual zero present but $r_{\rm odd}\nmid K_z$, all three means are $O_A(Y^\beta G^{-A})$ for each fixed $A>0$. If $r_{\rm odd}\mid K_z$, one has, for $j\in\{0,2,3\}$,

$$
 \left\langle f_j\,\mathfrak E_\pm\right\rangle_{K_z}
   = -\frac{\chi(-1)}{2}\,
            \mathbf1_{j=e}\,s_e(P_0\pm P_1)
                                   +O_A(Y^\beta G^{-A}).
 \tag{3}
$$

The exact identity with error requires no extra closeness beyond the original Page threshold. If in addition $(1-\beta)G\le C_*\log G$ with fixed $C_*$, and $w,\eta$ are fixed nonnegative tests with positive integrals $\int_Jw,\int_1^2\eta$, then on all sufficiently large such dyads the matching channel satisfies

$$
 -\chi(-1)
    \left\langle f_e(\mathfrak E_+-\mathfrak E_-)\right\rangle_{K_z}
   \ \gg\
        s_e\left(\int_Jw\right)\left(\int_1^2\eta\right)
           \frac{Y^{2\beta-1}}{G}\,
                 \frac{K_z}{\varphi(K_z)(\log r)^4}.
 \tag{4}
$$

The constants in (4) may depend on the fixed tests, threshold and cutoffs; the large-scale implication is ineffective as in the preceding aligned proof. No added lower bound on $z$ is needed. Unlike the ordinary unweighted mean, the matching channels $f_2$ and $f_3$ do not annihilate the correction from a supported even conductor. These are statements about the original correction alone.

## 1. The same finite model on four true residue classes

A primitive real character has odd conductor exponents at most one: at an odd prime $p$ a character to $\{1,-1\}$ is trivial on the odd-order kernel of the reduction of units to modulus $p$. At $2$, every unit congruent to $1$ modulo $8$ is a square in the units modulo $2^k$ for $k\ge3$. For example lift an odd square root modulo $2^k$ to $2^{k+1}$ by choosing it or adding $2^{k-1}$, which toggles the extra square bit. Thus any real character at $2$ factors through modulus $8$, and modulus $2$ has trivial unit group, giving $e\in\{0,2,3\}$. This proves the conductor classification used above.

For $a\in\{0,K_z,2K_z,3K_z\}$ let
$\langle F\rangle_{M,a}=(M/Y)\sum_{Y\le N\le2Y,\ N\equiv a\ (\mathrm{mod}\ M)}\eta(N/Y)F(N)$.
All four residue classes consist of even integers. We claim that in the presence of the zero, if $r\nmid M$ then their separate means of $\mathfrak E_\pm$ are all $O_A(Y^\beta G^{-A})$. If $r\mid M$, then on each class

$$
   \left\langle\mathfrak E_\pm\right\rangle_{M,a}
     =-\frac{\chi(-1)}2\,\frac{c_r(a)}{\varphi(r)}
                       (P_0\pm P_1)+ O_A(Y^\beta G^{-A}) .
 \tag{5}
$$

Here $c_r$ is the ordinary Ramanujan sum. We verify the residue change before any limit is taken in the denominator labels.

Use the [actual all-target Ramanujan formula](r94-spectral-all-target-ramanujan-exception.md) with its uniform error, changing the normalized mean to $\langle\cdot\rangle_{M,a}$. That error is unchanged in order since the number of sampled points is $O(Y/M)$. With each finite short pair and each $q\mid t$ fixed, the R95 expansion (5) of the local arithmetic factor gives constraints $d\mid N$ for $d\mid q$, with $(d,r)=1$. The modulus $q$ remains squarefree. Because $a$ is a multiple of $K_z$ and the set of primes dividing $M$ is exactly the same as the set dividing $K_z$, the constraint $N\equiv a\bmod M$ is compatible with every $d\mid q$. Their intersection is a single residue class modulo $[M,d]$, and $(r,[M,d])=(r,M)$.

In the case $r\nmid M$, expand $c_r(N)/\varphi(r)$ into its unit additive modes on that single class. For each numerator, the step $\exp(2\pi i b[M,d]/r)$ has period $r/(r,M)>1$ and the complete-period sum is zero. A constant phase from the starting residue only multiplies that zero. Partial sums of the normalized Ramanujan factor on the class are therefore $O(r)$, and the literal real physical weight for each term has supremum plus variation $\ll Y^{2\beta-1}G^{O(1)}$ by R95 (6)--(7). Partial summation bounds the unnormalized class error by the product of these two bounds.

If $r\mid M$, the Ramanujan factor is exactly $c_r(a)/\varphi(r)$ on the whole class, regardless of $d$. The ordinary BV sampling estimate on one residue class modulo $[M,d]$ gives its continuum integral divided by $[M,d]$, plus $O(Y^{2\beta-1}G^{O(1)})$. The estimate uses cells of that length with the point in its assigned cell and two boundary cells; it is valid for every translate, including the endpoints of the dyad. Multiplying by $M/Y$ gives continuum multiplier $(M,d)/(dY)$. Thus the surviving averaged local factors are **identical** to the R95 aligned model on multiples of $M$, with occupancy $1$ at primes dividing $M$ and $1/p$ at other primes. There is no change to the finite physical kernels or weights.

In either case the sum of all discretization errors is absorbed by $O(Y^\beta G^C r^{-1/2})$, by the same absolute estimates as R95 Section 1: the divisor/denominator expansion has total $G^{O(1)}Q_0^{O(1)}$, the finite short masses are $\ll G^2Y^{(1-\beta)/5}$, and the extra sampling factor is bounded by $(M/Y)r$ times fixed powers of $G$. Here $M,r,Q_0=Y^{o(1)}$ and $2\beta-1+(1-\beta)/5\le\beta$. The original all-target error is also of this order. By the original Page conductor lower bound this is $O_A(Y^\beta G^{-A})$ for all fixed $A$. In the aligned case the continuum factor just obtained is the same as for the zero residue of $M$, up to the multiplier $c_r(a)/\varphi(r)$ of absolute value at most one. Applying the exact R96 completion to that same averaged model proves (5), including the signs and the parity factor $1/2$. In particular all legitimately surviving denominator labels still fit the original finite bound because their product with $r$ divides $M$. No extra denominator-gap hypothesis appears.

## 2. The three rows are orthogonal on the literal four classes

If $r_{\rm odd}\nmid K_z$, then $r\nmid M$ by the conductor classification, so the first case of Section 1 applies to each class. If $r_{\rm odd}\mid K_z$, on each class the normalized odd Ramanujan factor equals one, since $r_{\rm odd}\mid N$. Thus only the $2$-part remains. Summing over the units modulo $4$ and $8$ respectively gives $c_4(N)/\varphi(4)=(-1)^{N/2}$ and $c_8(N)/\varphi(8)=\cos(\pi N/4)$ for even $N$. For the second identity the units $1,3,5,7$ pair to give the average of $\cos(\pi N/4)$ and $\cos(3\pi N/4)$, which agree on even integers. With the notation of (1) the normalized conductor factor is therefore $f_e$ on the four classes when the odd conductor part is supported.

Because $K_z/2$ is odd, as $a=mK_z$ runs through the classes with $m=0,1,2,3$, the three rows of values are

$$
  \begin{array}{c|rrrr}
             &0&1&2&3\\ \hline
          f_0&1&1&1&1\\
          f_2&1&-1&1&-1\\
          f_3&1&0&-1&0
  \end{array}
 \tag{6}
$$

The last row does not depend on which odd residue $K_z/2$ has modulo $4$. Their dot products divided by four are exactly the diagonal $s_0,s_2,s_3$. The normalized mean over all genuine $K_z$ multiples is exactly one fourth of the sum of the four $\langle\cdot\rangle_{M,a}$, including the weights and without discarding endpoint points. Each $f_j$ is constant on those classes. Multiply (5) by the literal row $f_j(a)$ and take the normalized sum. Orthogonality gives (3). For example when $e=2$ the positive and negative classes exchange sign, and when $e=3$ the two other classes have zero leading term; the matching weighted mean loses exactly a factor $1/2$ in the latter case and no factor in the former.

## 3. The original cap lower bound is unchanged by the power of two in the modulus

When the odd conductor part is supported and $r\mid M$, the averaged Euler coefficients of R96 (2) depend on $M$ only through the primes dividing $M$. Thus they vanish for every $p\le z$, and on every $p>z$ they are the same exterior coefficients used in [the integrated rough-primitive bound](r98-spectral-all-primorial-aligned-mean.md). The normalizing product in the R98 proof uses these same prime sets and the factor $r/\varphi(r)$, without using squarefreeness of the *sampling integer*. Repeating the assumptions of that bound with $K=M$ causes no change to any estimate: $\log r\le\log M=\log4+\sum_{p\le z}\log p\ll z$, so the same Page conductor growth still forces $z/\log G\to\infty$; the R98 signed short primitive, positive and inverse shift measures, and original real cutoffs are unchanged; and $M/\varphi(M)=K_z/\varphi(K_z)$. In particular its finite cap estimate and normalization give throughout the real support

$$
 \mathcal A_1(v,x)\gg M_K\ell^2
       \gg \frac{K_z}{\varphi(K_z)(\log r)^4},
 \qquad \ell=\log z,
 \tag{7}
$$

where $M_K$ denotes the R96 prefactor with sampling modulus $K=M$, not the modulus itself. This is the lower bound already proved by keeping the true $J_K(U_v)$ and inverse-shift moment; there is no claim about the sign of the unsmoothed primitive or of color zero.

With the nonnegative tests of (4), the genuine correction is real. Subtract the two parities in (3), so that only $P_1$ remains and the factor $1/2$ cancels. The physical integral in (2) with (7) has the stated lower scale, since $x,v-x\asymp Y$, $\log x\asymp G$, and substitution of $(v-x)/v$ and $v/Y$ gives the positive test integrals. As $Y^{2\beta-1}\ge YG^{-2C_*}$ and $\log r\le2Z$, the error in (3) is negligible by taking $A$ sufficiently large. This proves (4), and since $|f_e|\le1$ it also gives the same lower bound on the normalized mean of the **absolute** parity correction on this family. That last bound does not determine a sign at any individually specified $N$. None of the signed or absolute statements concerns the exceptional correction after replacing it by a known main term of the whole mixed-strip correlation.
