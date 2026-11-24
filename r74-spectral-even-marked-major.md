# A positive even-parity term on the genuine marked prime major arcs

**Scope.** This is the even-total-parity counterpart of the [odd marked major calculation](r73-spectral-marked-prime-weighted-major.md). It uses the same historical Dirichlet GRH prime-progression input, the same original major arcs, and actual primes on both sides. There is no largest-prime ordering on the marked right branch; an eligible product can be counted twice. Neither a full or minor bound, nor an estimate after unique-largest selection, nor a statement about weak S follows.

Fix $B>B_0>0$, $0<\sigma_1<\sigma_2<1/10$, and a fixed squarefree even radical $\mathcal R$ of $N$. Use $L=\log N$, $L_2=1+\log L$, $U=\sqrt L$, $G=e^U$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ and $V=[N/3,2N]$. As before $j(k)$ is the number of distinct primes at most $G$ dividing $k$. Put

$$
 \mathcal E_N=\{k:\ \mu(k)=-1,\quad
      \lfloor(2/5)\log U\rfloor< j(k)<\lceil(5/2)\log U\rceil\}.
$$

The actual right polynomial is

$$
 A_{\rm ev}(\theta)=
 \sum_{\substack{D N^{\sigma_1}<k\le D N^{\sigma_2}\\ k\in\mathcal E_N}}
    \ \sum_{\substack{p\ {\rm prime},\ p\nmid k\\ kp\in V}}
       M_>(kp)e(kp\theta).
 \tag{1}
$$

Here $M_>$ is the genuine squarefree above-BV mixed coefficient. The tagged product has $\mu(kp)=+1$, and $p\gg N^{1/2-\sigma_2}L^B$ for the actual terms. In the notation of the odd marked proof, for the genuine left prime polynomial $P_{I,\omega}$ and original major arcs $\mathfrak M$,

$$
 \begin{split}
 \int_{\mathfrak M}P_{I,\omega}(\theta)A_{\rm ev}(\theta)
                         e(-N\theta)\,d\theta
   ={}&\frac{2\Sigma(N)}{L}
        \log\frac{1/2-\sigma_1}{1/2-\sigma_2}
          \int_I\omega(t)\,dt\\
       &+o(1)\frac{\Sigma(N)|I|}{L}+O(N^{1-10^{-4}}).
 \end{split} \tag{2}
$$

The $o(1)$ is uniform on the same hard left intervals and bounded family of bounded-variation weights. The coefficient of the real integral is positive; in particular this gives a leading positive major term for a nonnegative test with $\int_I\omega\gg N$. The major asymptotic is the same if the count restriction on $j(k)$ is removed, while still requiring $\mu(k)=-1$.

## 1. The signed even sharp calculation

Use the real integer-cofactor comparison of the [prime-free odd calculation](r72-spectral-cofactor-saddle-cancellation.md) and the fixed-radical weight $r(k)$ of the odd marked proof: $r(k)=\prod_{\ell\mid k}r_\ell$ for squarefree $k$, with $r_\ell=0$ on the prime factors of $\mathcal R$ and $r_\ell=(\ell-1)/(\ell-2)$ otherwise. On $x\in V$, write $h=\log(x/D^2)>0$, $t=\log(k/D)$, and set $S_1=S_k(e^{t-})$, $S_2=S_k(e^{t-h})$, $J_1=J_k(e^t)$, $J_2=J_k(e^{t-h})$, where $S_k(z)=\sum_{d\mid k,d\le z}\mu(d)$ and $J_k(z)=\int_1^z S_k(v)dv/v$ for $z\ge1$, zero below 1. On the $\mu(k)=-1$ branch the exact sharp coefficient is

$$
 X_k(x)=F_{0,D}F_{1,D}
       =\frac{h(S_1-S_2)^2-2(S_1-S_2)(J_1+J_2)}{\log x}.
 \tag{3}
$$

This is the same sharp formula as in the [signed Euler slot calculation](r70-spectral-signed-shift-euler-slots.md), with actual strict/weak cutoff at the first/second endpoint. The low coefficient $Y_k(x)$ is exactly the previous two-fold $M_\le$ model, with the same weights and endpoints. At actual squarefree $m=kp$ with $p$ prime, $p\nmid k$, and $kp\in V$, one has $M_>(m)=X_k(m)-Y_k(m)$. Indeed $M_>=-\Xi_D-M_\le$ after the prime marginal has been removed, and $m$ here is composite. The derivation of the sharp and low formulas only uses that the distinguished prime exceeds the short labels, not that it is largest.

For $s\in[\sigma_1,\sigma_2]$ put $K=D N^s$. First average (3) over all $D<k\le K$ with $\mu(k)=-1$. As in the two odd precedents, remove $j(k)>J_*=\lfloor32\log U\rfloor$ by the positive Rankin bound of the [weighted high-count calculation](r71-spectral-weighted-high-small-prime-count.md). This step costs $o(1)$ in the reciprocal comparison, by $r(k)\ll k/\varphi(k)$ and the bound by $\tau_4(k)$ on both coefficients. For the remainder write $k=bv$ with $b$ the exact squarefree product of primes at most $G$ and $v$ strictly $G$-rough. Thus $b=N^{o(1)}$; also $r(v)=1+O((L/U)e^{-U})$ as in the odd weighted trace, an error costing $o(1)$ by the same positive divisor bound.

For the rough $v$ in a hard logarithmic cell the parity selector is now
$(\mu^2(v)-\mu(b)\mu(v))/2$. The preceding weighted trace still has factor $wV_G/(2d)$ for a rough squarefree LCM $d$ and cell log width $w$, where $V_G=\prod_{\ell\le G}(1-1/\ell)$. The Möbius error only changes sign, and the same arithmetic hypotheses hold: the label bound on a cell is $O(k/D)$, $v\asymp k/b$, the squarefree floors summed over label pairs are $O(N^{-1/4+3\sigma_2/2+o(1)})$, and the masked Möbius variable $v/d$ is polynomially large. The error with $1/d$ is summed by the same polylogarithmic reciprocal LCM bound. The hard endpoints use the same positive unsigned brackets for each shifted primitive separately and the same small-width integrated brackets separately; taking a difference or a sum costs only an absolute constant. The endpoint squares summed over $b$ with $r(b)/b$ still cost $O(L^{-5})$ (or smaller with the original $\eta=L^{-100}$). To see that the even integrated factor does not prevent the concluding Cauchy step, the $b>1$ model-integral square summed over $b$ is $O_{\mathcal R}(U^3)$ at each fixed rough gcd $e$, by the signed full integrated-primitive bound at generating parameter $1$ (see below). The $b=1$ integrated function is bounded by $O(U)$, and the comparison log interval has length $O(L)$, so its finite-interval squared integral is $O(L U^2)$. Multiplication by the trace factor and summation over $e$ cost $O(V_G(1+L/U))=O(1)$. These bounds give $o(1)$ by Cauchy even before using any finer cancellation of the even product. The same errors apply to the actual squares by the hard brackets. No whole-line square for an indefinite primitive at $b=1$ has been asserted.

More explicitly, put $A=A_{b,e}$, where

$$
 A_{b,e}(u)=\sum_{d\mid b}\mu(d)R_{G,e}(u-\log e-\log d),\qquad
 J_{b,e}(u)=\int_{-\infty}^{u}A_{b,e}(v)\,dv.
$$

Here $R_{G,e}$ is the reciprocal Möbius primitive with primes up to $G$ and the additional primes of the rough $e$ omitted. It vanishes for negative log argument. Use the shift subscript $A_h(u)=A(u-h)$ and $J_h(u)=J(u-h)$. The exact even trace obtained by the rough gcd expansion is

$$
 \sum_{\substack{D<k\le K\\\mu(k)=-1}}\frac{r(k)X_k(x)}k
 =\frac{V_G}{2\log x}
     \sum_{\substack{b\ {\rm sf},\ P^+(b)\le G\\ j(b)\le J_*}}\frac{r(b)}b
       \sum_{\substack{e\le N^s\\ e\ {\rm rough}}}
         \frac{\varphi(e)\mu(e)^2}{e^2}
         \int_0^{sL}\{h(A-A_h)^2-2(A-A_h)(J+J_h)\}(u)\,du+o(1).
 \tag{4}
$$

The convergence and endpoint justification just given uses the same trace and finite hard-cell proof as (5) of the prime-free odd calculation, with the displayed signed even factors. In particular strict and weak comparison cutoffs agree almost everywhere in this real integral, while the original discrete endpoints remain those of (3).

## 2. The indefinite primitive and the constant sign

Here are the detailed bounds for extending the integrals in (4). Uniformly for rough $e\le N^s$, the weighted primitive-square sum over $b$ is $O_{\mathcal R}(U^2)$ on the whole line, by the signed Euler bound at parameter $1$ as in the odd weighted proof. At $b>1$, the exact signed shift $q_b(\xi)=\prod_{\ell\mid b}(1-e^{-i\xi\log\ell})$ makes $J_{b,e}$ square integrable: extract any prime of $b$ to write its integrated shift as a convolution of the unintegrated primitive with a finite log interval. The weighted square sum for these $J$ is $O_{\mathcal R}(U^3)$. Indeed the weighted squared Euler generator with $b=1$ subtracted is $O_{\mathcal R}((U|\xi|)^2)$ when $|\xi|\le 1/U$, and $O_{\mathcal R}((1+U|\xi|)^2)$ for $1/U<|\xi|\le1$. With $|\widehat R_{G,e}(\xi)|\ll U/(1+U|\xi|)$ in this range, division by $\xi^2$ in Plancherel gives $O_{\mathcal R}(U^3)$. On $|\xi|>1$, the generator is $O_{\mathcal R}(U^2(1+\log(2+|\xi|))^{C})$ and the high-frequency bound on $\widehat R_{G,e}$ of the signed Euler proof gives an integrable majorant of total $O_{\mathcal R}(U^2)$. The finite-prime weight $r_\ell$ changes the exponents in these bounds by $O_{\mathcal R}(1)$, and the small-$\xi$ bound still follows from $r_\ell\le2$ and the actual squared shifts. These bounds also hold with any restriction on the $b$ sum because it is a sum of nonnegative squares. At $b=1$ the positive smooth-mask convolution gives $\|A\|_1\ll U$ and $\|J\|_\infty\ll U$ uniformly in $e$; thus the absolute cross-term integral on any truncation is $O(U^2)$.

Omit the terminal rough gcd range $\exp(sL-L^{2/3})<e\le\exp(sL)$. Its harmonic weight is $O(L^{2/3}/U)$ by the usual rough harmonic bound. By Cauchy over $b>1$ and $u$, its absolute weighted $(A-A_h)(J+J_h)$ integral at each $e$ is $O(U^{5/2})$; the squared term is $O(hU^2)$ and the $b=1$ bound is as above. With the prefactor of (4) this costs

$$
 O_{\mathcal R}\!\left(\frac{1}{LU}\frac{L^{2/3}}{U}
                                  (U^{5/2}+hU^2)\right)=o(1).
 \tag{5}
$$

For the retained $e$, enlarge the log integral to the full line. On $u<0$ the integrand vanishes. Beyond $sL$ the ordinary reciprocal Mertens convolution estimate for every shifted $A$ has log argument at least $L^{2/3}-O(U\log U+h)\ge \tfrac12 L^{2/3}$. The two integrable decays of that estimate, $O(U(e^{-c\sqrt z}+e^{-z/(2U)}))$ at log argument $z$, beat all powers of $L$ after integration. The indefinite shifted $J$ are at worst $O(U2^{J_*})$ there, by their $L^1$ bound in the unintegrated factors. Thus the full-line replacement costs $o(1)$.

For every $b$ including $1$, $A$ is real and in $L^1\cap L^2$, and $J$ is bounded but need not be in $L^2$. The exact whole-line identity for this case is

$$
 \int_{\mathbb R}(A-A_h)(J+J_h)(u)\,du
      =-\int_{\mathbb R} A(u)\int_{u-h}^{u+h} A(v)\,dv\,du .
 \tag{6}
$$

Indeed the two self terms $\int AJ$ and $\int A_hJ_h$ are equal by translation. For the remaining cross terms, translate the term $\int A_h(u)J(u)\,du$ to $\int A(u)J(u+h)\,du$; subtracting this from $\int A(u)J(u-h)\,du$ gives (6). Every term is absolutely integrable from $A\in L^1$ and $J$ bounded. The centered finite interval convolution on the right of (6) has Fourier multiplier $2\sin(h\xi)/\xi$. Thus the whole-line quadratic expression in (4) has the multiplier

$$
 h|1-e^{-ih\xi}|^2+4\frac{\sin(h\xi)}{\xi},
 \tag{7}
$$

with the value at zero given by continuity. The higher sign of the constant term is the sign from (6), not an arbitrary parity convention.

The remainder of the Euler reduction now uses exactly the weighted odd sharp calculation, with the multiplier (7) bounded by $8h$ and the terminal error already checked. The retained $e$ harmonic weight is $sL V_G+O(L^{4/5}V_G)+o(1)$ by that calculation: its small end is truncated at $\exp(L^{4/5})$, and the new terminal $L^{2/3}$ buffer is smaller than the allowed error. Removing the extra rough $e$ mask in the squared transform costs relative $O((L/U)e^{-U})$; the formal positive transform tail $j>J_*$ costs weighted primitive energy $O_{\mathcal R}(U^4 2^{-J_*})$. This reinstates no $b$ terms into the original arithmetic comparison. The resulting integral is

$$
 \frac{s}{2}\frac1{2\pi}
     \int_{\mathbb R}\left[h(2-2\cos(h\xi))+4\frac{\sin(h\xi)}{\xi}\right]
                        J_r(\xi)\,d\xi+o(1),
 \tag{8}
$$

where $J_r=|\widehat R|^2F_r$ and $\mathcal C_r=(2\pi)^{-1}\int J_r$ are exactly (5)–(6) of the odd marked proof. In particular $J_r\in W^{1,1}$ is Lipschitz near zero and $J_r(0)=1$. Integration by parts gives $h\int J_r(\xi)\cos(h\xi)d\xi=o(1)$ and the sine term is the standard Dirichlet integral with limit $\pi J_r(0)$. These estimates are uniform since $h=2B\log L+O(1)\to\infty$ uniformly on $V$. Thus (8) equals $s(h\mathcal C_r+1)+o(1)$.

## 3. Low folds, count restrictions and true prime arcs

The weighted low coefficient calculation of the odd marked proof changes only the sign of the Möbius difference. Its two complementary integer pairs and forced-label occupancies are unchanged, and the use of $\tfrac12(\mu^2(uv)-\mu(uv))$ instead of $\tfrac12(\mu^2(uv)+\mu(uv))$ leaves the same factor $1/2$, since the signed term was bounded absolutely after the masked Mertens cancellation. Consequently, with the same strictly enforced endpoints and uniformly in $s,x$,

$$
 \sum_{\substack{D<k\le D N^s\\\mu(k)=-1}}
                       \frac{r(k)Y_k(x)}{k}=s(h\mathcal C_r-1)+o(1).
 \tag{9}
$$

The locally weighted Euler constant integral in that proof is independent of the sign of $\mu(k)$ after the half-trace step. In particular (9) does not change to $+1$.

The low even count tail $j\le\lfloor(2/5)\log U\rfloor$ and the high even tail $j\ge\lceil(5/2)\log U\rceil$ can be removed from (4) and (9) at $o(1)$ cost. Use respectively the arithmetic reciprocal bounds in the [signed Euler slot](r70-spectral-signed-shift-euler-slots.md), [lower-largest-prime transfer](r70-spectral-lowest-largest-prime-transfer.md) and [weighted high-count](r71-spectral-weighted-high-small-prime-count.md) proofs. These are bounds separately for $|X|$ and $|Y|$, with weight $k/\varphi(k)$, before the sieve on actual primes. Their proof uses the same real cutoffs, squarefree parity and $k$ range with local label floor, and its positive subset bounds do not use the prime being largest. It applies on the present range $D<k\le DN^{\sigma_2}$ (for example one can use the earlier arithmetic floor with $\kappa=1/4$). This includes the zero-slot low even case there, for which the least-prime rough-kernel comparison was proved separately, and the extreme-count high case from Rankin. Thus uniformly through the compact set of upper exponents,

$$
 \sum_{\substack{D<k\le D N^s\\ k\in\mathcal E_N}}
        \frac{r(k)\{X_k(x)-Y_k(x)\}}k=2s+o(1).
 \tag{10}
$$

The genuinely prime-weighted major transfer is the one in §2 of the odd marked proof, not the prime-free comparison. All its inputs are unchanged: the selector is constant at fixed $k$, the real weight $X-Y$ has supremum plus variation $O(\tau_4(k))$ on its literal real range including endpoint jumps, and $p$ exceeds every arc modulus for large $N$. Restoring $p\mid k$ only for the progression comparison is power-small by $\sum_k \tau_4(k)\omega(k)$; those terms are not part of (1). For all other primes the exact composite squarefree coefficient is (3) minus its true low folds. The circle integral major error uses the same pointwise right bound $O_\epsilon(Q^2N^{3/4+\sigma_2/2+\epsilon})$, the same occupation/variation bounds, and the same left and completed Ramanujan tails (tag multiplicity is at most two). Thus the error retains $O(N^{1-10^{-4}})$ and the completed density is

$$
 \Sigma(N)\sum_{\substack{D N^{\sigma_1}<k\le D N^{\sigma_2}\\ k\in\mathcal E_N}}
           \frac{r(k)(X_k(x)-Y_k(x))}{k\log(x/k)} .
 \tag{11}
$$

The local factor $r(k)$ is unchanged. No extra prime estimate is being consumed for the change of sign.

For fixed $x$, the reciprocal logarithm in (11), as a function of $s=\log(k/D)/L$, is precisely $(\log(x/D)-sL)^{-1}$, with supremum plus variation $O(1/L)$ on $[\sigma_1,\sigma_2]$. Stieltjes partial summation of (10) on the exact half-open interval therefore gives $2\int_{\sigma_1}^{\sigma_2} ds/(\log(x/D)-sL)+o(1/L)$. Since $\log(x/D)=L/2+B\log L+O(1)$ uniformly, this equals

$$
 \frac2L\log\frac{1/2-\sigma_1}{1/2-\sigma_2}+o(1/L).
$$

Integrate against the genuine left test on $I$ to obtain (2). This establishes a nonzero completed major term in the previously uncontrolled intermediate even count band, not a conclusion on the actual minor or the order correction.
