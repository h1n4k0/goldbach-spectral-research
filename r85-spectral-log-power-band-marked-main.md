# A nonzero marked mixed-strip term on both genuine squarefree parities

**Scope.** Small-prime exclusion can leave no trace in a signed main term, but that does not make the genuine mixed coefficient insensitive to primes on every logarithmic scale. This evaluates its true prime-factor mark in a fixed log-power band, on a density-one family, including a nonzero leading term on the odd squarefree parity whose unmarked leading term is zero. The result is unconditional for the genuine full signed correlation and the genuine original moving polynomial major integral. It is not a statement about prime representations, a prescribed target, or weak S.

Use the exact above-BV squarefree $M_\pm$, real hard left $I$, bounded-BV left weight $\omega$, binary singular series $\Sigma(N)$, and original moving polynomial arcs from the [whole mixed parity theorem](r80-spectral-whole-mixed-parity-density.md). Thus $M_>$ is the true mixed coefficient, before its external subtraction, on pairwise coprime squarefree $abcd=m\in[N/3,2N]$, with $D=\sqrt N(\log N)^{-B}$, $H_0=\sqrt N(\log N)^{-B_0}$ and the exact upper/lower cutoffs of that theorem; $M_\pm=(1\pm\mu(m))M_>/2$, where $+$ is even squarefree factor count. Keep fixed admissible $B>B_0>0$. Fix constants satisfying

$$
      0<B-B_0<\theta_1<\theta_2<\min(1,2B),
      \qquad b=\theta_2-\theta_1 .
$$

Use a common dyad $Y\le N\le2Y$, $\ell=\log Y$, $v=\log\ell$, and the actual prime interval

$$
 {\cal P}_Y=\{p:\ell^{\theta_1}<p\le\ell^{\theta_2}\},\qquad
 W_Y(m)=\frac1v\sum_{\substack{p\in{\cal P}_Y\\p\mid m}}\log p .
$$

These are literal primes of the genuine integer, without an independent tagging model. The cutoff ranges are frozen only for this mark, which is common at all targets of the dyad.

**Theorem.** For every fixed $A>0$, outside $O_A(Y\ell^{-A})$ even targets, simultaneously for both signs and the usual $I,\omega$, the full signed correlation with $W_Y(m)M_\pm(m)$ is

$$
 b\,\Sigma(N)\int_I\frac{\omega(u)}{\log(N-u)}\,du
       +o\left(\frac{\Sigma(N)|I|}{\log N}\right)+O_A(Y\ell^{-A}).
 \tag{1}
$$

The identical formula holds on the actual original polynomial majors. The little-oh is uniform on this family. For $\omega=1$ and intervals of at least a fixed inverse-log fraction of $Y$, both signed main terms are positive. The mark is a log-weighted count, not the indicator of at least one prime in the band. The restriction $B-B_0<\theta_1$ ensures the marked band is above the finite lower signed cutoff in logarithmic coordinates.

## 1. The true linear marked completion

Use the common auxiliary arcs $q\le Q_0=\ell^K$, slow radius $2Q_0/Y$, as in the whole mixed proof. Give each actual right-occupied prime $p\in{\cal P}_Y$ the factor $1+t u_p$ with $u_p=(\log p)/v$. The derivative at $t=0$ of the resulting right polynomial is exactly $W_Y(m)$ times the original polynomial, since the partner is squarefree. The multiplier is inserted before the exact $M_>+M_\le=-\Xi_D$ and before splitting into true parity. No divisor or interval gate changes.

We use the actual coefficient-norm arithmetic of Section 1 of the [bounded-pattern completion](r83-spectral-adaptive-bounded-pattern-main.md). The expanded alphabet causes no change in that arithmetic: its prime product has logarithm $O(\ell^{\theta_2})=o(\ell)$, there are at most $\exp(O(\ell^{\theta_2}))=Y^{o(1)}$ positive marked-part allocations, and the reciprocal pattern sum is bounded since $\sum_{p\in{\cal P}_Y}1/p=O_{\theta_1,\theta_2}(1)$. To explain the distinction in the errors, in a large signed sector write the signed variable $s d$ at each fixed true marked part $s$, impose $(d,s)=1$, exclude the rest of the alphabet from $d$, retain the other unit and coprime factors, and solve its rational residue as one class modulo $q/(q,s)$ when possible. Its scale $Y/(hs)$, with $h$ the product of the other three factors, is polynomial. The masked Möbius Siegel--Walfisz error is $O_A(Y/(hs)\ell^{-A})$ in that class and sums harmonically over $s$, not by counting the alphabet. In the two positive variables the squarefree floors and harmonic-convolution errors save a fixed power, which absorbs the $Y^{o(1)}$ allocations. The low untwisted fold uses the same two-variable calculation, and its twisted fold is a large signed sector. All cuts remain actual hard cuts on the four factors. The coefficient-norm errors handle the derivative too: the weight on each exact pattern is at most $\log m/v=O(\ell)$, a fixed log loss. The same local sup/variation bound $O(\ell^C C_1^{\omega(q)}/q)$, the BV real-line completion, and the mean Ramanujan tail from that proof give arbitrary log accuracy at sufficiently large fixed $K$. Left prime Siegel--Walfisz is unchanged. These are unconditional inputs on the auxiliary arcs.

Put $u_p=0$ outside the mark band. The real completed density before differentiating is the [actual parity formula](r67-spectral-high-mixed-parity-major.md) with local parameters

$$
 d_p(t)=r_p(1+t u_p),\qquad
 \alpha_p(t)=\frac{d_p(t)}{p+2d_p(t)},\qquad
 P(t)=\prod_p(1-1/p)^2(1+2d_p(t)/p),
 \tag{2}
$$

where $r_p=0$ at $p\mid N$, and $r_p=(p-1)/(p-2)$ otherwise. This is precisely the marked local rule: at an occupied prime the multiplier occurs once, independent of which of the four pairwise coprime factors occupies it. The true $\Sigma(N)$ is unchanged. All primes in the band are large, and for $|t|\le1/4$ the factors in (2) are analytic and uniformly comparable in absolute value to their unmarked counterparts. The normalized variation and harmonic bounds of the marked arithmetic apply to the derivative as described above.

For clarity on taking the derivative of the infinite real expressions, one can first keep the finite cutoffs of the parity proof. Its signed reciprocal primitives at the distant artificial clip $L/10-\log j$ ($L=\log N$) extend with a negligible error on the complex disk $|t|\le1/4$. Indeed the correcting log convolution relative to the ordinary reciprocal primitive has weighted total variation at exponent $1/v$ at most $O(\mathcal A(N)\mathcal A(j))$, with $\mathcal A$ the quarter-power radical factor of the [radical criterion](r81-spectral-radical-criterion-and-log-exceptions.md). Use the usual unmarked kernel factors; the marked primes cost $\exp(O(\sum_{p\in{\cal P}_Y}p^{-1+1/v}))=O(1)$. Here $p^{1/v}\le e^{\theta_2}$ on the band and the reciprocal mass is bounded. Splitting its shifts at half the clipping level gives a tail $O(\mathcal A(N)\mathcal A(j)(e^{-c\sqrt L}+e^{-cL/v}))$ when $j\le e^{L/20}$. Larger $j$ have negligible Euler square tail. On the good radical family below these are arbitrary inverse-log errors, including after the derivative by Cauchy's estimate. This justifies use of the exact finite-low and full autocorrelation formula and its derivative, rather than assuming analyticity of an unbounded formal signed array at its endpoints.

## 2. Unmarked mass concentrates, and the derivative fills the actual band

Write $\alpha_p=\alpha_p(0)$, $P=P(0)$, and let $R_{N,j}$ be the unmarked signed reciprocal primitive in log coordinates, zero below zero, with mass $M_j=\int R_{N,j}\ge1$. Write $R$ for the ordinary reciprocal Möbius primitive. It is integrable with $\int R=1$, bounded, and $|R(u)|\ll e^{-c\sqrt u}$ on $u\ge0$, as in the whole mixed theorem. The exact positive correcting kernel relative to $R$ has local transform $(1-\alpha_p\mathbf1_{p\nmid j}\,p^{-s})/(1-p^{-1-s})$. Set

$$
 a_v(x)=v R(vx),\qquad f_j(x)=v R_{N,j}(vx)/M_j,\qquad
 g_j(x)=v\,\partial_t R_{N,j,t}(vx)|_{t=0}/M_j .
$$

Importantly the mass $M_j$ in the derivative normalization is kept unmarked. Then $f_j=\pi_{N,j}*a_v$ with a positive probability measure $\pi_{N,j}$ on the nonnegative half-line. In particular $\|f_j\|_1\ll1$, $\|f_j\|_2\ll\sqrt v$, and $\int f_j=1$.

Restrict to $\log \mathcal A(N)\le v^{1/3}$. The positive Euler moment argument of the radical criterion gives this outside $O_A(Y\ell^{-A})$ for every $A$: for moment $m$ its log average is $O(m^{4/3})$, and taking $m$ a sufficiently small fixed multiple of $v$ gives decay $e^{-c v^{4/3}}$. On this family, for fixed $j$ the first moment of $\pi_{N,j}$ is

$$
 O\left(v^{-1}\left(1+\sum_{p\mid Nj}\frac{\log p}{p}\right)\right)=o(1).
 \tag{3}
$$

Indeed the logarithmic derivative of the positive local normalized transform gives an expected raw shift $O(\log p/p^2)$ at a nondeleted prime and $O(\log p/p)$ at a deleted prime. The sum over $p\mid N$ is $O(1+\log\mathcal A(N))$, since $\log p/p\ll p^{-3/4}$. Convolution and (3) show that $f_j$ has bounded absolute integral concentrated at zero and acts as a signed approximate identity of mass one, for fixed $j$ uniformly on this family. The unmarked kernel's quarter-power moment also gives $\sup_{x\ge\epsilon}|f_j(x)|=o(1)$ for each fixed $\epsilon>0$ and fixed $j$: split the raw shifts as usual to bound this supremum by $O(v\mathcal A(N)\mathcal A(j)e^{-c\sqrt{\epsilon v}})$.

We will use additionally the uniform bound $\sup_{x>0}|x f_j(x)|\ll1$, valid for all $N,j$. This is the real-space bound (7) of the [AP-radical major law](r83-spectral-ap-radical-major-law.md): its proof needs only $0\le\alpha_p\mathbf1_{p\nmid j}\le1/p$, not an AP restriction on the mask. Explicitly the normalized correction probability has position-multiplied convolution measure with atoms
$(\log p)(p^{-k}-(\alpha_p\mathbf1_{p\nmid j})^k)/v$ at $k\log p/v$. Its mass in each bin of width $1/v$ is uniformly $O(1/v)$ by Chebyshev on the $k=1$ part and the summable higher powers. Convolving with $a_v$ bounds this part uniformly by the sum of the ordinary primitive suprema on unit log bins. The term from $x a_v(x)$ is bounded as well. This proof allows general even $N$.

Differentiate the local ratio between the marked and unmarked reciprocal primitive at zero. For $p\in{\cal P}_Y$, $p\nmid Nj$, the derivative contributes the signed log-shift measure

$$
 -\alpha'_p(0)\sum_{k\ge1}\alpha_p^{k-1}\delta_{k u_p},
 \qquad
 \alpha'_p(0)=u_p\alpha_p(1-2\alpha_p).
$$

Let $\Lambda_{N,j}$ be their sum. There is no term for $p\mid Nj$, and no additional product term at first order because each undifferentiated correcting ratio is the unit atom. Thus

$$
                 g_j=f_j*\Lambda_{N,j}
                        =\pi_{N,j}*(a_v*\Lambda_{N,j}).
 \tag{4}
$$

Uniformly in $N,j$, its total variation is $O(1)$, and the $k=1$ part has mass $O(1/v)$ in each bin of width $1/v$, by the elementary prime upper bound in a unit raw-log interval and the lower cutoff $\theta_1 v$. Higher powers have total variation $O(e^{-\theta_1 v})$. Therefore $\|g_j\|_\infty+\|g_j\|_1\ll1$: apply the log-bin argument to convolve the first powers with $a_v$, use $\|a_v\|_\infty\ll v$ for higher powers, and use the probability convolution in (4).

For fixed $j$, on the good radical family, the measure $\Lambda_{N,j}$ may be replaced in $a_v*\Lambda_{N,j}$ by

$$
             \Lambda_v=-\sum_{p\in{\cal P}_Y}
                                \frac{\log p}{v p}\,\delta_{u_p}
 \tag{5}
$$

with $o(1)$ error in both $L^1$ and supremum norms. Higher powers and the $O(p^{-2})$ first-power coefficient error are exponentially small in $v$ before convolution. Actual deleted marked primes satisfy $\sum_{p\mid N,p\in{\cal P}_Y}p^{-1}\ll e^{-\theta_1 v/4}\log\mathcal A(N)$, by comparing $p^{-1}$ with $p^{-3/4}$ there; fixed $j$ has no such primes eventually. Multiplying these variation errors by $\|a_v\|_\infty\ll v$ still gives $o(1)$.

The convolution $\Lambda_v*a_v$ tends to $g(x)=-\mathbf1_{\theta_1<x<\theta_2}$ in $L^1$, is uniformly bounded, and tends uniformly to zero on $x\ge\theta_2+\epsilon$ for each fixed $\epsilon>0$. Here is a direct verification that retains the actual hard endpoints. Let $H=(1+\log v)^4$ and in the convolution first remove terms with $vx-\log p>H$ using the decay of $R$ and the bounded mass of $\Lambda_v$; the removed supremum is $O(v e^{-c\sqrt H})=o(1)$. Negative values of $vx-\log p$ contribute zero. On a compact subinterval of $(\theta_1,\theta_2)$, all remaining log primes are in $[vx-H,vx]$ inside the band. The sum there is the Stieltjes integral of $-e^{-u} R(vx-u)$ against $d\vartheta(e^u)$, with $\vartheta$ the ordinary prime Chebyshev function. Its prime-number-theorem main term is $-\int_0^H R(w)dw\to-1$. The error is $O((1+H)e^{-c\sqrt{\theta_1 v/2}})$ by the ordinary prime number theorem with classical zero-free error, partial summation, and the variation $O(1+H)$ of $R$ on $[0,H]$ (sum its jumps $|\mu(n)|/n$). In this partial summation the factor $e^u$ of the PNT error cancels the $e^{-u}$ of the test, so there is no exponential loss in $H$. Moving integer seams have the same endpoint bounds. Below $\theta_1$ the convolution vanishes, and above $\theta_2+\epsilon$ it is bounded by the removed pointwise tail. The uniform log-bin bound controls the narrow endpoint strips; its far $L^1$ tail is bounded by the ordinary primitive tail times the bounded total variation in (5). These facts prove the stated $L^1$ limit. By the positive approximate identity (3) and (4), for each fixed $j$ we obtain uniformly

$$
 g_j\longrightarrow g\text{ in }L^1,\qquad
          \sup_{x\ge\theta_2+\epsilon}|g_j(x)|\longrightarrow0 .
 \tag{6}
$$

The latter follows by splitting the shifts of $\pi_{N,j}$ at $\epsilon/2$ and using the uniform supremum bound.

## 3. The two parity derivatives and the original Fourier integrals

In the normalized parity bracket put $U=(B-B_0)\log\log N$, $T(x)=\log(x/D^2)$, $U_j=(U-\log j)_+/v$ and $V_x=T(x)/v$. For each $j$, with the weight $c_j=P\mu(j)\alpha(j)^2 M_j^2$, its unmarked bracket before the outer factor $1/2$ is

$$
 V_x\int_{U_j}^\infty f_j(u)^2du
 +\left(\int_0^{U_j} f_j(u)du\right)^2
 \ \pm\
 \left(\int_{-V_x}^{V_x} C_{f_j}(s)\,ds-V_x C_{f_j}(V_x)\right)
 \tag{7}
$$

by the exact rescaling in the parity formula; $C_f(s)=\int f(u)f(u+s)du$. In the derivative, replace one of each pair of $f_j$ by $g_j$ in turn, and differentiate the local weight in addition. The elementary signed Euler normalization gives $\sum_j c_j=1$, $\sum_j j^{1/2}|c_j|\ll1$ as in the AP-radical proof.

For fixed $j$, $U_j\to B-B_0>0$, $V_x\to2B$ uniformly on the physical $x$, and the unmarked parts of (7) tend respectively to $1$ and $1$ (untwisted and twisted). Indeed $f_j$ concentrates at zero, with vanishing sup at positive distance, so the terminal square and the positive-shift term vanish. Its full autocorrelation-integral is one, and tails at fixed positive distance have vanishing absolute $L^1$ by concentration in each factor.

The derivative of the untwisted portion of (7) tends to zero: the terminal cross $\int_{U_j}^\infty f_j g_j$ tends to zero by the bounded supremum of $g_j$ and concentration of $f_j$, and the truncated integral of $g_j$ vanishes in the limit by $B-B_0<\theta_1$ and (6). The derivative of the twisted portion tends to $-2b$. Its integrated derivative autocorrelation tends in $L^1(ds)$ to $g(s)+g(-s)$: convolve the strong $L^1$ limit in (6) with the signed approximate identity $f_j$ or its reflection. The interval $[-V_x,V_x]$ contains the support in the limit, by $\theta_2<2B$. At the single positive shift, the term $\int f_j(u)g_j(u+V_x)du$ tends to zero by (6), and $\int g_j(u)f_j(u+V_x)du$ tends to zero by the unmarked positive-distance supremum estimate. No convergence of an unweighted global square at the atom is needed.

These passages through $j$ are uniform. First discard $j>e^{U/2}$ at cost $o(1)$ using the crude $O(1+v)$ bounds on (7) and its derivative (whole $L^1,L^2$ norms above), and the Euler half-moment. Below that threshold, $U_j$ and $V_x$ stay uniformly positive, so $|u f_j(u)|\ll1$, $\|f_j\|_1\ll1$ and the uniform norms of $g_j$ bound all the brackets and derivatives by $O(1)$. One can therefore pass through finitely many $j$ and let their threshold grow, as in the AP-radical proof. The extra derivative of $\alpha(j)^2$, relative to its unmarked value when nonzero, is bounded by $2\sum_{p\mid j}u_p\le2\log j/v$; when zero it stays zero. Its weighted total effect is $o(1)$ by the same Euler moment and the separate treatment of large $j$. Meanwhile

$$
       \frac{P'(0)}{P}=2\sum_{p\in{\cal P}_Y}u_p\alpha_p
                          \longrightarrow 2b .
$$

This is prime partial summation of $\sum \log p/p$, with the absolutely negligible corrections from $O(p^{-2})$ and from actual $p\mid N$ already checked in (5).

Thus the even derivative coefficient is
$\tfrac12[(2b)(1+1)+0-2b]=b$, and the odd is
$\tfrac12[(2b)(1-1)+0+2b]=b$. This gives (1) on the common auxiliary majors, with the actual singular factor and uniformly in the left hard/BV tests. The sign difference here comes from the exact Möbius twist, not an arbitrary choice of parity signs.

On the fixed auxiliary complement, $W_Y(m)=O(\ell)$ is a fixed common multiplier throughout the dyad. Divide it by that bound and use the maximal hard-cut Bessel proof of the whole mixed theorem with this fixed multiplier; its right divisor-moment energy only contracts. Increasing $K$ absorbs the fixed log loss and gives $O_A(Y\ell^{-A})$ for the actual auxiliary complement outside $O_A(Y\ell^{-A})$ targets. This proves the full identity by Fourier inversion. Lastly the [original moving minor theorem](r79-spectral-original-minor-power-exception.md) accepts this same fixed common right multiplier and either true parity (after the same normalization). Its power error and power-small exceptional set absorb that normalization; subtract this actual minor from the full identity. This proves the original polynomial major formula without any Dirichlet GRH, and finishes the proof within the stated density and signed-weight scope.
