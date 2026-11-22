# Unconditional cancellation on the general-even moving Vaughan slab

This is an unconditional version of the [R47 signed moving slab](weak-s-type-ii-general-even-moving-slab.md). The separate conditional proof and sharper rates in R47 are unchanged.

Let $N$ be any sufficiently large even integer, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, $V=N^{.2499}$, and $b_{\rm II}(v)=\sum_{r\mid v,\,r>V}\Lambda(r)$. Uniformly for $N^{.49999}\le t\le N^{.50001}$, $N/2\le y\le9N/16$, arbitrary optional hard subintervals in each range below, and $D_{\max}=Xe^H$, put

$$
 \mathcal V_N(D_{\max})=
 \sum_{\substack{uv+dk=N,\ N/2<uv\le y,\ k>t,\ (uv,N)=1\\
            N^{.488}\le u,v\le N^{.512},\quad 1\le d\le D_{\max}}}
         \mu(u)\mu(d)b_{\rm II}(v)\mu^2(dk).
$$

There is **no Riemann hypothesis assumption** in either of these two conclusions:

$$
 \begin{array}{ll}
  H=10L_2:&|\mathcal V_N(XL^{10})|\ll N L_2^6/L,\\
  H=L^\rho,\quad 0<\rho<1/4\ \text{fixed}:&
       |\mathcal V_N(Xe^{L^\rho})|\ll_\rho N L^{4\rho-1}L_2^2 .
 \end{array}                                                   \tag{1}
$$

Both bounds are $o(N)$. Their asymptotic constants and sufficient $N$-threshold are ineffective, through Siegel/Siegel–Walfisz. The larger cap has the separately stated larger error. The result retains the true signs, full unit masks for $N$ including its odd factors, true Vaughan weight and squarefree gate, and the strict moving quotient cutoff. It does not estimate the complement of this slab, weak S, or all of Vaughan Type II.

The changes relative to R47 are (i) the split between high and low primitive conductors is now only a fixed power of $L$; (ii) low conductors need only a relative inverse-log transform estimate, not square-root cancellation; (iii) stop the tag band at $\exp(L/L_2)$, so its finite Euler exclusions stay small on a classical near-$1$ Perron contour. The loss from the lower end of this contour and from the smaller tag band is quantified below.

## 1. Classical transforms at polynomial-logarithmic conductor

The following estimates are for nonprincipal characters $\chi\bmod q$, $q\le N^C$ with fixed $C$, induced by primitive conductor $f\le L^A$, where $A>0$ is any fixed constant. For every prescribed fixed $D>0$, we prove a hard interval bound $O_{A,C,D}(Y L^{-D})$ at any scale $N^{.45}\le Y\le N$, for each of these true sequences:
* Möbius with any fixed polynomial-size coprimality mask, including $N$ or $Ns$ for a tag label.
* $b_{\rm II}$ on $(v,N)=1$, without assuming $v$ squarefree.
* $b_{\rm II}$ on squarefree $(v,N)=1$, optionally with no prime divisor in $\mathcal P=[S_0,\exp(L/L_2)]\cap\mathbb P$, where $S_0=\exp(10^5(H+L_2))$.

The character multiply is $\chi$ in every case. In the tag variant $S_0$ lies below the upper endpoint for large $N$ in both cap cases.

Fix $K,K_T>0$ to be chosen as constants depending on the desired saving, and put $\eta_0=K L_2/L$, $T_P=L^{K_T}$. We need estimates for $1-\eta_0\le\sigma\le1+1/L,\ |\tau|\le T_P$. Put $d_0=L^{-1/3}$ for this paragraph only. The [classical Dirichlet zero-free region (Koukoulopoulos, Theorem 12.3)](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=130) and [Siegel’s theorem (Theorem 12.10)](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=138) imply no zeros of a primitive nonprincipal $L(s,\psi)$, $f\le L^A$, in $\Re s\ge1-2d_0,\ |\Im s|\le T_P+1$ for large $N$. In detail, the nonexceptional gap is $\gg_{A,K_T} 1/L_2$. A possible exceptional real zero has gap $\gg_{\epsilon}f^{-\epsilon}$ with ineffective constant; choose $\epsilon=1/(4A)$, so this is $\gg_A L^{-1/4}\gg 2d_0$ for sufficiently large $N$, ineffectively. We do not assert a quantitative effective threshold for the exceptional case.

To bound $L^{\pm1}$, on the disk of radius $4d_0$ centered at $1+2d_0+i\tau$ use periodic character cancellation to get $|L(s,\psi)|\ll_{A,K_T} L_2$: truncate at an integer $R\asymp f(T_P+10)$, bound the terms through $R$ by $(1+\log R)R^{2d_0}$, and the tail by $O(f(1+|s|)R^{-\sigma})=O(1)$ by partial summation over the periodic remainder. These statements use $\log R=O_{A,K_T}(L_2)$ and $d_0L_2=o(1)$. The disk is zero free, so choose the analytic logarithm of $L$ there with its Euler logarithm at the center. The absolute value at the center is $O(L_2)$ from the Euler series and $\log\zeta(1+2d_0)=O(L_2)$. The real part elsewhere is $\le \log(O_{A,K_T}(L_2))$. Borel–Carathéodory on the inner disk of radius $3d_0$ thus gives $|\log L(s,\psi)|=O(L_2)$. In particular $|L(s,\psi)|^{\pm1}\ll L^{C_1}$ throughout the required rectangle; for fixed $A,K_T$ the exponent $C_1$ can be chosen absolute, with constants and the large-$N$ threshold allowed to depend on the fixed parameters. Indeed $\log(O_{A,K_T}(L_2))\le L_2$ eventually. The finite imprimitive and other polynomial-sized masks cause only $L^{O(1)}$: on this contour split primes at $L^2$, use $p^{\eta_0}=1+o(1)$ below that, and use the bound $O_C(L)$ on the number from a polynomial-sized mask above $L^2$. This last observation applies to factors $1\pm\chi(p)p^{-s}$ and their inverses. Thus there is no requirement that the *imprimitive* modulus be polylogarithmic.

Use the genuine Dirichlet-series marks from [R47 §2](weak-s-type-ii-general-even-moving-slab.md#2-the-individual-transforms-with-all-finite-unit-masks). The first sequence uses the masked $1/L(s,\chi)$. The second uses

$$
 L(s,\chi)\prod_{p\mid N}(1-\chi(p)p^{-s})\!
        \sum_{\substack{V<p^k\le N\\p\nmid N}}(\log p)\chi(p)^k p^{-ks};
$$

the cutoff at $p^k\le N$ leaves all coefficients under consideration unchanged. For the third sequence use $L(s,\chi)/L(2s,\chi^2)$, with inverse $1+\chi(p)p^{-s}$ factors on the union of $p\mid N$ and the optional tag primes, marked by

$$
   \sum_{\substack{V<p\le N\\p\nmid N}}
        (\log p)\frac{\chi(p)p^{-s}}{1+\chi(p)p^{-s}} .
$$

The inverse $L(2s,\chi^2)$ is absolute. Higher-prime-power terms in the second series and the quadratic correction from the denominator in the third are absolutely bounded on this contour. The linear prime mark is bounded by ordinary [Siegel–Walfisz, Koukoulopoulos, Theorem 12.1](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=129) and partial summation. For $V\le x\le N$, one has $f\le(\log x)^{A+1}$ eventually, so the *primitive nonprincipal* character prime sum is $O(x e^{-c_A\sqrt L})$, ineffectively. This follows by combining the progression version over reduced classes with the vanishing sum of $\psi$; the polynomial-logarithmic number of classes is absorbable. Removing primes dividing $qN$ costs $O_C(L)$. Partial summation against $p^{-\sigma-i\tau}$ costs at most $O(T_P L N^{\eta_0})$, still giving $o(1)$ for each fixed $K,K_T$. This argument is used only on the medium/large prime mark $p>V$, not on tag primes potentially as small as a fixed power of $L$.

For the extra tag product, write $z=\exp(L/L_2)$. On this contour the absolute linear sum through $z$ is bounded by

$$
 \sum_{p\le z}p^{-1+\eta_0}
 \le \sum_{p\le z}\frac1p
       +e^K\eta_0\sum_{p\le z}\frac{\log p}{p}
 = O(L_2)+O_K(1),
$$

since $\eta_0\log z=K$. Higher terms converge absolutely. Therefore all Dirichlet series used have modulus $\ll_{A,C,K,K_T} L^{C_2}$ on the contour with a fixed absolute exponent $C_2$ for sufficiently large $N$, independent of $K,K_T$. This independence also follows directly from the $O_K(1)$ excess in the last display; it is not the coarse bound $e^K\sum 1/p$.

For precision in hard Perron, take a half-integer endpoint $Y'\asymp Y$, start at $\sigma_+=1+1/L$, and use the ordinary truncated integral at height $T_P$. Every coefficient of the three masked series is $O(\log(2n))$ in absolute value. The kernel error away from $n\in[Y'/2,2Y']$ is $O(Y L^2/T_P)$, by the convergent $\sum \log(2n)n^{-1-1/L}\ll L^2$. Inside it, use the bound $\min(1,O(Y/(T_P|n-Y'|)))$; the half-integer spacing and harmonic summation also give $O(Y L^2/T_P)$. No smoothing or hypotheses on short intervals are necessary. Upon shifting, the vertical segment is $O(Y^{1-\eta_0} L^{C_2}\log(2T_P))$, and the horizontal pieces are $O(Y L^{C_2}/T_P)$. There are no poles: the inducing character is nonprincipal, the inverse factors have no zeros on the contour, and $L(2s,\chi^2)^{-1}$ is absolute. Choose $K$ so $.45K>D+C_2+3$, and then $K_T>D+C_2+3$, to bound all errors by $O(Y L^{-D})$. The same holds for interval differences. This proves the three asserted transforms, without GRH and with the ineffectivity just specified.

## 2. The geometric and arithmetic reductions remain exact

Use the boundary and square completion reductions of [R47 §1](weak-s-type-ii-general-even-moving-slab.md#1-common-conventions-and-exact-boundary-control): the $u,d$ relative grid $\eta=L^{-100}$ and truncation $B=L^{1000}$ give $O(L^{202})$ rectangles and log-small boundary/completion errors. In particular the changed boundary $(d,n=uv)$ count is $O(\eta NL+X e^H)$ summed once, and all sign and cutoff comparisons precede square completion. Both chosen $H$'s are $o(L)$. The unit conditions on the actual summand are exact: from $(uv,N)=1$ and $d,c^2\mid N-uv$, both $d,c$ and $q=[d,c^2]$ are coprime to $N$. At fixed $c,g=(c,d)$ the modulus $q=c^2d/g$ is injective on its group.

Use the same direct test $\max(U_0,V_0)\ge D_0 L^{20000}$ when $d>N^{.49}$, and otherwise the two R47 first-cell transfers, but with the amended upper tag endpoint $z=\exp(L/L_2)$ above. For large $N$, $z<N^{.001}<V$. All factor and parity masks from R47 remain:
1. A direct long $u$ uses the actual squarefree Möbius coefficient with $(u,N)=1$. A direct long $b$ from $v=a^2b$ is squarefree, $(b,N)=1$, and uses the genuine $b_{\rm II}(b)$; for $a\le B$ this equals $b_{\rm II}(v)$, as $B^3<V$. The short variable is $a^2u$, with $(a,u)$ not assumed coprime to each other but separately both prime to $N$.
2. A first-cell tag $s$ transferred from $v=s\ell$ has $(s,N)=1$, so $\ell$ inherits the mask; remove $s\mid u$ by the same pair-count/divisor-moment estimate, obtaining the long squarefree $n=su$. Weight transfer $b_{\rm II}(v)\to b_{\rm II}(\ell)$ differs only if $s^2\mid v$ and that error is as in R47. The long transform is a cell prime sum times the ordinary unit-masked $\mu(u)$-transform, plus exact $s\mid u$ correction with $\mu$ on $I/s$ and mask $Ns$. The earlier-cell mask stays short.
3. On $v$ with no tag, split $v=a^2b$, $a\le B$ and $a,b$ separately coprime to $N$. A first-cell tag from $u=s\ell$ gives $m=a^2\ell,\ n=sb$, with $(s\ell b,N)=1$ and $s\nmid b$ because $b$ has no tag. The mask and $b_{\rm II}$ pass exactly from $v$ to $b$; the earlier-cell mask stays short. The Möbius replacement $\mu(s\ell)\to-\mu(\ell)$ only differs on $s^2\mid u$. The long transform is the cell prime sum times the masked squarefree transform of §1.

In both directions tag prime sums at a cell of scale $T$ can be bounded trivially by $O(T)$, including the mask $(s,N)=1$. A $\mu$-transform on $I/s$ has scale $U_0/T$, so the summed restriction correction is $O(U_0L^{-D})$, no larger than the main target $O(UL^{-D})$. Thus every long coefficient, after its exact normalization, satisfies $\left|\sum\beta_n\chi(n)\right|\ll U L^{-D}$ for all low conductors, with no short prime progression input. All base interval scales in these transforms are $\ge N^{.45}$ eventually: original scales are $\ge N^{.488}$, and tag or square-part division costs at most $zB^2=N^{o(1)}$. The deterministic comparison errors of R47 only depend on the lower tag endpoint, cell ratio $1+L^{-2000}$, and the elementary reciprocal upper bound $O(L_2)$ on the tag band. They remain $O(NL^{-10})$ after summation. The signed principal reversal is unchanged and uses the real $\mu(d)$, unit mask $(e,2cNmn)=1$ with $e=d/g$ in the $d>N^{.49}$ branch, and unconditional harmonic Mertens. Where principal estimates in the smaller branch used individual masked Möbius sums, they remain classical and unconditional.

## 3. Rebalance the averaged energy: the conductor split is polylogarithmic

Take $F_0=L^{30000}$ and the bounds of §1 with $A=30000,\ D=60000$. For $d>N^{.49}$, let

$$
 Z_\beta=\sum_{q\asymp Q}\frac1{q\varphi(q)}
                   \sum_{\chi\bmod q,\ \chi\ne\chi_0}|\widehat\beta(\chi)|^2 .
$$

All moduli are allowed in this nonnegative variance quantity. The [R45 induction-mask argument](weak-s-type-ii-balanced-polylog-tags.md#1-a-centered-dispersion-bound-with-only-logarithmic-loss-in-the-diagonal-terms) gives, for $f>F_0$, at most $O((U/Q)(F+U/F))$ per primitive conductor dyad $f\asymp F$, without a character hypothesis. To recall the point: $q=fh$, $\varphi(q)\ge\varphi(f)\varphi(h)$, remove both $(n,h)=1$ masks by squarefree divisors $r,s$, and sum $h$ with $1/\varphi(h)$ at cost $O(1/\varphi([r,s]))$. The primitive large sieve gives the factor $F+U/F$ and norms with scale $U/\sqrt{rs}$; their joint Euler sum converges, as in R45 §1. Summing $F_0\ll F\ll Q$ gives

$$
             Z_{\beta,{\rm high}}\ll U(1+U/(QF_0)).
$$

For $1<f\le F_0$, using $\sum_{h\asymp Q/f}1/\varphi(h)\ll1$ and at most $\varphi(f)$ primitive characters per $f$, the total weighting in $Z_\beta$ is $O(F_0/Q)$. With the true low-conductor transform this gives

$$
             Z_{\beta,{\rm low}}\ll U^2 L^{-120000} F_0/Q.
$$

These are estimates for imprimitive as well as primitive $\chi$. The exact centered Poisson zero mode is $O(M Z_\beta)$ and the Cauchy factor is $MQ$. Thus the zero contribution to the **squared** final estimate is

$$
        O\bigl(N^2(Q/U+1/F_0+F_0 L^{-120000})\bigr).
$$

This is why the high-conductor remainder $U/(QF_0)$ in $Z_\beta/U$ need not itself be small. After square roots the two new terms contribute $O(NL^{-15000})$.

The other variance pieces are exactly R47 §§4–5: the large-gcd moment loss $MU L^{10}(1+U/(GQ))$, the nonzero neighboring-tile and center-cross terms with fixed power margins, and the same complete unit support $n>1,\ (n,N)=1$ needed in reciprocity. None of them used GRH. The new top $z=N^{o(1)}$ only shortens the scales in tag rectangles, and the full direct scales still satisfy $U\le N^{.512+o(1)},\,Q\gg N^{.49}$. In particular the largest squared exponent $1.9981+30\kappa+\epsilon+o(1)$ is unchanged. The new $NL^{-15000}$ terms absorb every external $O(L^{5212})$ reassembly loss. All signed terms in this large-$d$ branch are $O(NL^{-10})$ as in R47.

For $d\le N^{.49}$ use the separate two-leg induction-mask argument of [R47 §3](weak-s-type-ii-general-even-moving-slab.md#3-the-small-moduli-dle-n49-a-separate-two-leg-estimate), also with $F_0=L^{30000}$. The low-conductor contribution is now $O(N F_0 L^{-120000})$, because the true $\mu$ and $b_{\rm II}$ transforms are each small relative to their length. In the high part it is important not to bound both interval lengths by their larger scale. At $f\asymp F$, the factor after joint mask summation is

$$
   O\bigl(X\sqrt{(F+U_0/F)(F+V_0/F)}\bigr)
    \ll X(F+\sqrt{U_0}+\sqrt{V_0}+X/F),
$$

since $U_0V_0\asymp N$. Sum $F_0\ll F\ll Q$ to get $O(XQ+X(\sqrt{U_0}+\sqrt{V_0})L+N/F_0)$. Here $Q\ll N^{.49}B^2$, $\max(U_0,V_0)\ll N^{.512}$, so the first two terms have fixed power saving, and $N/F_0$ absorbs the outer sums. The principal and square completion were unconditional, and this proves $O(NL^{-10})$ in the complete small-$d$ branch, down to $d=1$.

## 4. The remaining unsigned bound and the claimed rates

The direct/tag dichotomy implies the same area bound as R47: on tag rectangles the harmonic $u$-range and $d$-range each cost $O(H+L_2)$. At each fixed $d$, its cell is unique and the $u$-cells are disjoint; $|J|\ll N/u_0$. Thus $\sum |I||J|/d\ll N(H+L_2)^2$, without counting the rectangles again. For the remaining doubly untagged tuples, the [R41 product upper sieve](weak-s-type-ii-medium-prime-first-cell.md#3-a-small-elementary-sieve-sandwich) has divisor level $z^{30}\le N^{.03}$ for large $N$, and each one-variable density is now

$$
         O(\log S_0/\log z)=O((H+L_2)L_2/L).
$$

Removing primes dividing the actual $d$ changes its log product by $O(L/S_0)=o(1)$. Apply precisely the parity-sensitive rectangular Weil upper count of [R47 §6](weak-s-type-ii-general-even-moving-slab.md#6-the-unsigned-term-and-the-distinction-between-the-two-caps). The true $d$-mask is $(d,N)=1$, and discarding the other masks and squarefree conditions only for this positive upper bound is valid. Period splitting costs $N^{o(1)}$ and all grid/divisor errors remain $O_\epsilon(N^{.81+\epsilon+o(1)})$. Multiplying the area by the two densities and the weight $b_{\rm II}\le L$ proves the residual bound

$$
                     O\bigl(N(H+L_2)^4 L_2^2/L\bigr).
$$

This gives precisely the two different rates in (1), after all signed and boundary errors. Ineffectivity comes from the classical low-conductor analytic estimates, not from a hidden hypothesis about any Dirichlet $L$-function.
