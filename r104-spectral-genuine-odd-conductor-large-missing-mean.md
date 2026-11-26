# Genuine matched means for an odd conductor with missing primes

**Scope.** The matched signed mean of the actual full mixed-strip correlation and of its original moving-major integral also works for a hypothetical odd Page conductor when its missing part is sufficiently large. Unlike the even-conductor case, the ordinary completed bracket need not vanish in this channel. We bound it directly: every surviving term must occupy every missing prime, and each forced occupancy and its sampling density contribute a separate reciprocal gain. The statement is for modulated means on all targets of the prescribed divisibility family. It does not prove Page-zero existence, an individual-target bound, unweighted positivity, a result on the full signed shell beyond the mixed strip, prime-pair positivity, or Weak S. No Dirichlet GRH or external zero-gap assertion is used.

Use the exact tests and genuine sums of [the genuine matched even-conductor means](r103-spectral-genuine-matched-even-conductor-means.md). Thus $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $Y\le N\le2Y$ even, and the fixed admissible $B>B_0>0$ give the same hard real cuts. The actual common scaled left test is $I_N=NJ$, $J\subset(1/2,9/16]$ real and half-open, $\omega_N(u)=w(u/N)$ with bounded-BV $w$, and the common dyadic weight is $\eta(N/Y)$ with bounded-BV $\eta$. Let $X_\pm$ be either $S_\pm$, the genuine full mixed-strip correlation, or $S_\pm^{\rm maj}$, its **original moving** polynomial-major integral, with actual bound $N^{1/1000}$ on denominators and radius $2N^{1/1000}/N$. The signs still denote the even and odd squarefree factor-count sectors. Keep the family $K=K_z=\prod_{p\le z}p$, with $2\le z\le Z$ and $z$ fixed on each dyad.

Suppose the actual primitive real Page character $\chi$ has **odd** conductor $r$, with its simple real zero $\beta>1-4a_0/\sqrt G$. Then $r$ is squarefree by the local conductor classification in [the fixed two-adic channels](r99-spectral-two-adic-exceptional-mean-channels.md). Assume $M=[K,r]\le e^{2Z}$. Write

$$
 \begin{gathered}
 D=\frac r{(r,K)},\qquad M=KD,\qquad
 \gamma(N)=\frac{c_r(N)}{\varphi(r)},\qquad
 H=\mathbb E_{m\bmod D}\gamma(Km)^2=\frac1{\varphi(D)},\\
 L_\gamma=\mathbb E_{m\bmod D}|\gamma(Km)|,\qquad
 \langle F\rangle_K=\frac K Y
      \sum_{\substack{Y\le N\le2Y\\K\mid N}}\eta(N/Y)F(N).
 \end{gathered} \tag{1}
$$

Here $c_r$ is the ordinary Ramanujan sum, $\mathbb E$ is the exact uniform finite-class average, and $D$ is odd and coprime to $K$. This $D$ is the missing conductor divisor, not the physical lower cutoff. Let $P_i(M)$, $i=0,1$, be the real integrals of [the matched exceptional mean](r100-spectral-matched-ramanujan-exceptional-mean.md) at sampling modulus $M$, with the completed finite caps, original physical endpoints, and without the parity half or the sign $-\chi(-1)$.

**Theorem.** There are fixed constants $C,C_0>0$ such that for either genuine choice of $X_\pm$ and for every fixed $A>0$,

$$
 \begin{split}
 \langle\gamma X_\pm\rangle_K
    ={}&-\tfrac12\chi(-1)H\{P_0(M)\pm P_1(M)\}\\
     &+O\!\left(YG^C\,\frac{C_0^{\omega(D)}}{D^2}\right)
      +O_A(H\,YG^{-A}).
 \end{split} \tag{2}
$$

The first error bounds the ordinary component that can still correlate with the odd conductor; its exponent $C$ is independent of $A$. The second is genuinely relative to the exact response $H$. In particular a condition forcing $D$ to exceed every fixed power of $G$ makes both errors $O_A(HYG^{-A})$ for each fixed $A$.

For the quantitative sign, additionally assume $(1-\beta)G\le C_*\log G$ with $C_*$ fixed, $z\ge A_0\log G$ with the sufficiently large fixed $A_0$ of R100, and that $w,\eta$ are fixed nonnegative tests with positive integrals. There is a fixed $J_0$ (depending on the declared parameters) for which $D\ge G^{J_0}$ suffices for

$$
 -\chi(-1)\langle\gamma(X_+-X_-)\rangle_K
       \gg H\left(\int_J w\right)\left(\int_1^2\eta\right)
             \frac{Y^{2\beta-1}}G
              \frac{M}{\varphi(M)(\log r)^4}.
 \tag{3}
$$

The comparison for sufficiently large dyads is ineffective as before. Neither sign nor negligibility of the first error is inferred for small $D$.

## 1. The ordinary continuum term requires every missing prime

Let $\mathcal B_\pm(N)$ be the exact ordinary completed bracket. Use [the odd-divisor expansion](r102-spectral-genuine-two-adic-mixed-means.md) (5)--(8), with its exact finite geometric cutoffs. In its expanded tuples, $j,k,d_0,d_1,d_2$ are odd and squarefree, $d_0\mid j$, and the only remaining arithmetic constraint in the target variable is $d\mid N$ with $d=[k,d_0,d_1,d_2]$. The bounded-BV real profile of any such tuple, including the time weight $\eta$ and common left test, has supremum plus variation at most $YG^C V_j^2 b_{d_1}b_{d_2}$, in the notation of that expansion. Its remaining absolute scalar factor is at most a fixed constant times $\alpha^\circ(j)^2|\delta(k)|$, since the $d_0$ coefficient $\mu(d_0)$ has modulus at most one. Here $V_j=\prod_{p\mid j}(1-\alpha_p^\circ)^{-1}$, $\alpha^\circ_p=(p-1)/(p^2-2)$ at odd primes, $b_{d_i}$ is multiplicative over its squarefree shifts, and $|\delta(k)|$ is the absolute Euler occupancy coefficient of the common scalar prefactor $\Sigma(N)P_N$. In particular $|\delta(p)|,b_p\ll1/p$. No regular bracket is replaced by a limiting profile.

On all genuine sampled targets one may impose $d\le2Y$ in these tuples, exactly as in R102 Section 3. For each fixed tuple the two sampling conditions give precisely $N=[K,d]n$. At primes of $r$ that divide $K$ the local factor in $\gamma$ is identically one. At a missing prime $p\mid D$ the factor is one if $p\mid d$; otherwise it is the function $c_p(n)/\varphi(p)$ on this progression, since $[K,d]$ is a unit at $p$. Its complete-period mean is zero, and its absolute sum over a complete period is exactly two. Therefore by CRT the mean of $\gamma([K,d]n)$ over its literal residual period is exactly $\mathbf1_{D\mid d}$. If it is zero, the absolute sum over one residual period is at most $2^{\omega(D)}$ and consequently bounds partial sums on every interval in $n$, including shorter intervals and translated starts. If $D\mid d$, the factor is one everywhere and ordinary BV sampling on the progression applies. In either case the sample of the tuple's profile $F(v)$ differs from its continuum term by

$$
 \sum_{\substack{Y\le N\le2Y\\K\mid N,\ d\mid N}}
       \gamma(N)F(N)
   =\frac{\mathbf1_{D\mid d}}{[K,d]}
                    \int_Y^{2Y}F(v)\,dv
        +O\!\left(2^{\omega(D)}
              (\|F\|_\infty+\operatorname{Var}F)\right).
 \tag{4}
$$

For the zero-mean case this is discrete partial summation; for the other case it is the ordinary BV comparison to integral averages on the progression cells, with the two end cells bounded by the supremum. The estimate is valid even if $[K,d]>Y$.

Multiply (4) by $K/Y$ and sum the absolute discrepancy weights using R102 (8). The result is $O(KG^C2^{\omega(D)})$. To bound the surviving continuum terms, $D\mid d$ and $(D,K)=1$ imply $K/[K,d]\le1/D$. Furthermore, the total absolute scalar/shift weight of tuples with $D\mid d$ is at most $G^C C_0^{\omega(D)}/D$, as follows. Write $A_p=(\alpha_p^\circ)^2(1-\alpha_p^\circ)^{-2}\ll p^{-2}$. For this upper bound drop the coprimality requirements and enlarge $k,d_1,d_2\le2Y$ to all squarefree products of odd primes at most $2Y$. The prime-local unrestricted sum at an odd $p\le2Y$ is then

$$
           (1+|\delta(p)|)(1+b_p)^2(1+2A_p).
 \tag{5}
$$

The last factor records absence from $j$, or presence in $j$ with either of the two possibilities for $d_0$. The choices of $p$ in $d_0$ are independent at the primes of this upper bound. For $p\mid D$ we must require at least one of $k,d_0,d_1,d_2$ to contain $p$. The excluded flat choice is exactly $1+A_p$: $j$ may or may not contain $p$ but $d_0$ must not. Thus subtract $1+A_p$ from (5) at every forced prime, leaving $O(1/p)$ uniformly. At every other prime below $2Y$ the increment of (5) is $O(1/p)$ and costs at most a fixed power of $G$ over all such primes. All $p\mid D$ lie below $2Y$, and for primes above $2Y$ one may even allow the convergent $1+2A_p$ factors to bound the $j$ sum. This gives the stated absolute forced-prime product, without assuming that the original signed coefficients have one sign.

The continuum integral divided by $Y$ is bounded by the profile supremum, and we have its first $1/D$ from sampling and its second from the forcing product. Consequently

$$
       |\langle\gamma\mathcal B_\pm\rangle_K|
          \ll YG^C\,\frac{C_0^{\omega(D)}}{D^2}
                          + KG^C 2^{\omega(D)} .
 \tag{6}
$$

The first term need not vanish: for odd conductors the ordinary expansion can itself supply all missing primes. In particular the two-adic cancellation of R103 has not been inferred in an odd channel.

## 2. The extra ordinary terms on $r$-multiple arcs are still harmless

Let $\mathcal U_\pm$ be the actual auxiliary major integral with the same common cutoff $Q_0$ and radius $2Q_0/Y$. The rate-keeping argument in R103 Section 1 still applies to the ordinary nonmultiple arcs and to the ordinary slow and real-cap conversions, with one change. Since an odd $r$ is squarefree, the omitted formal terms with $r\mid q$ and the actual ordinary principal Fourier density on these arcs cannot be discarded by $\mu(q)=0$. Use the quantitative estimates in [the original all-scale decomposition](r87-spectral-all-scale-exceptional-left-reduction.md) (5) and (7), rather than merely their inverse-log corollaries.

In detail, the formal squarefree $r$-multiple Euler tail, divided by $Y$, is at most $G^C C_1^{\omega(r)}/r\ll G^C r^{-1/2}$ by R87 (5). For the actual ordinary principal term, its left Fourier $L^2$ norm squared on those arcs is at most $O(Y\log(2Q_0)/\varphi(r))$ by R87 (7), and the true right polynomial has torus $L^2$ norm at most $O(\sqrt Y G^{15/2})$ there. Cauchy--Schwarz bounds the integrated principal term by $YG^C r^{-1/2}$, using $r/\varphi(r)\ll G$. The Page left term is exactly $\mathfrak E_\pm$ by the original construction, and its residual left contour error is already included in the explicit R103 rate. All other rates in that argument only used the absence of the Page character on the $r\nmid q$ moduli and the same cap, not non-squarefreeness of $r$: the analytic and fixed-power errors, slow extension, rational tail $\exp(-4Z+O(G^{1/4}))$, and uniform ordinary long-log clipping continue unchanged. Hence on every true target before any averaging,

$$
 \mathcal U_\pm(N)
  =\mathcal B_\pm(N)+\mathfrak E_\pm(N)
    +O\!\left(YG^C
       \{e^{-4Z+C G^{1/4}}+r^{-1/2}\}\right).
 \tag{7}
$$

There is no new unquantified inverse-log error in (7). In particular it may be averaged against a matched response much smaller than a fixed inverse power of $G$.

## 3. Keep the true errors relative to the response

The exact finite calculation in R100 gives $L_\gamma/H=\prod_{p\mid D}2(1-1/p)\le2^{\omega(D)}$. For $s=1,2$ the physical unweighted moment of $|\gamma(N)|^s$ on the $K$ sample, normalized by $K/Y$, is at most $(1+O(M/Y))\mathbb E_{m\bmod D}|\gamma(Km)|^s$, as in R103 (7), by counting each of the actual $M$ residue classes. It follows that the weighted error in (7), divided by $H$, is at most
$YG^C (e^{-4Z+C G^{1/4}}+r^{-1/2})2^{\omega(D)}$.
This is $O_A(YG^{-A})$ for each fixed $A$: use $2^{\omega(D)}\ll r^{1/4}$, $r\le e^{2Z}$ for the first term, and the classical Page conductor growth $r>G^J$ eventually for every fixed $J$ for the second. Also the discrepancy in (6) divided by $H$ is $O(KD G^C 2^{\omega(D)})=Y^{o(1)}$, since $M=KD\le e^{2Z}$.

For the actual common auxiliary complement and original moving minor use the quantitative weighted estimates in R103 Section 3; they do not use an even-conductor classification after the two $\gamma$ moments have been specified. In particular the ambient squared bound for the true auxiliary complement gives $YG^C Q_0^{-1/4}\sqrt{KH}$ before dividing by $H$. As $K/H=K\varphi(D)\le M$, this is at most $H\,YG^Ce^{-3Z}$. The genuine original moving minor contributes at most $Y^{1-1/40000}L_\gamma+KG^C Y^{1-3/10000}$, keeping its actual power-exception set rather than discarding any sampled points. After dividing by $H$ both terms retain fixed power savings since $K/H\le M$, $L_\gamma/H\ll r^{1/4}$ and $M=Y^{o(1)}$. Add the true common complement and, for the original-major result, subtract the true original moving minor, as in R103.

The actual exceptional term alone has the R100 formula with the exact factors (1) and error $O(Y^\beta G^C r^{-1/2}L_\gamma)$; this has arbitrary inverse-log saving after dividing by $H$ by the same conductor growth. Combining it with (6)--(7) and these two genuine arc comparisons proves (2).

Finally subtract the parity formulas in (2). The color-one cap alone remains, with the original factor $-\chi(-1)H$. Its positive lower bound under the stated hypotheses is (6) of R100. In particular after division by $H$ the lower scale is $\gg YG^{-2C_*-3}$ for the fixed positive tests: use $Y^{2\beta-1}\ge YG^{-2C_*}$, $M/\varphi(M)\ge1$ and $\log r\le2Z\ll\sqrt G$. After the same division the remaining ordinary error in (2) is at most $YG^C C_0^{\omega(D)}/D$, by $\varphi(D)\le D$. The elementary bound $C_0^{\omega(D)}\ll D^{1/2}$, obtained by absorbing the finitely many small primes, makes this smaller than half the asserted lower scale for sufficiently large fixed $J_0$ in $D\ge G^{J_0}$. The other error is smaller too by choosing $A$ sufficiently large. This proves the conditional actual modulated lower bound (3) without claiming it when the missing part is small.
