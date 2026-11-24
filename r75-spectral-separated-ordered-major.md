# The genuinely ordered largest-prime major term on the fixed exponent band

**Scope.** This is a major-arc asymptotic for the actual unique-largest-prime selector on the band of the marked proofs. It uses the same fixed radical and historical Dirichlet GRH prime-progression input, and keeps the original major arcs. The genuine full and minor integrals and weak S are not estimated. We do not impose a small-prime-count selector in this result.

Retain $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, $V=[N/3,2N]$, and $0<\sigma_1<\sigma_2<1/10$. Let $A_{\rm ord}$ be the right polynomial for the true squarefree coefficient $M_>(m)$ on $m=kp\in V$, with $p$ the actual largest prime of $m$ and $D N^{\sigma_1}<k\le D N^{\sigma_2}$. Select either true total parity separately. Put

$$
 C_{\rm ev}^{\rm ord}=
 2\int_{\sigma_1}^{\sigma_2}
        \frac{1+\log(1-2y)}{1/2-y}\,dy,\qquad
 C_{\rm odd}^{\rm ord}=0.
 \tag{1}
$$

The even constant is positive. With the original left test and genuine major arcs,

$$
 \int_{\mathfrak M}P_{I,\omega}(\theta)A_{\rm ord}(\theta)e(-N\theta)\,d\theta
  =\frac{\Sigma(N)}L C_{\rm parity}^{\rm ord}\int_I\omega(u)\,du
       +o(1)\frac{\Sigma(N)|I|}{L}+O(N^{1-10^{-4}}).
 \tag{2}
$$

All uniformities are as in the marked estimates. In particular a positive even major term in (2) is not a sign assertion on the full coefficient.

## 1. Keep the literal ordering and remove the two known ends

Subtract rejected tags from the fully marked branch. For a rejected prime $p$ the unique larger prime is $q$ and $x=pqa$. We use the exact real two-prime transfer and swapped short formulas (3)–(7) of the [balanced correction proof](r75-spectral-balanced-rejected-majors.md). In particular $t=\log(qa/D)$ is the rejected cofactor log and $s=\log(pa/D)$ the kept one. They obey $t+s=h+\log a$, with $h=\log(x/D^2)$ and $\Lambda_x=\log(x/D)$. The true restriction is $\sigma_1L<t\le\sigma_2L$, $s<t$. Put $E=L^{2/3}$ and $\Delta=10E$.

The part $0<t-s\le\Delta$ is $o(\Sigma(N)|I|/L)$ with the original power error by the balanced correction, for both parities. The part $s\le\Delta$, with any separation, uses the actual largest prime $q=(x/D)e^{-s}\gg\sqrt N \exp(-10E)$ up to powers of $L$. Take any fixed $2/3<\gamma<3/4$ and the [near-giant positive reciprocal majorants](r67-spectral-rough-short-shell-energy.md). At fixed kept cofactor $k'=pa$ the smaller $p$ is exactly $P^+(k')$ on this support, since $p>a$. The original rejected eligibility now says $\sigma_1 L<\log(x/(pD))\le\sigma_2 L$ and the gate $q>p$ says $x>k'p$. These are extra hard intervals in real $x$ at fixed $k'$, as is any optional removal of the already included balance. The $s$ gate is constant there. Thus the already positive reciprocal bound of that proof still applies to the subset, and its major-arc transfer still has the same variation bound including the new hard gates. It bounds this actual major term by $o(\Sigma(N)|I|/L)$ plus the original power error. This step is not an inference about a signed sub-polynomial from an unrestricted minor estimate.

It remains to handle exactly $s>\Delta$, $t-s>\Delta$ within the rejected band. The added gates are affine inequalities in $\log x$ at fixed integer $k=qa$, or in $\log q$ at fixed $a,x$. The two-prime transfer of the balanced correction applies unchanged, including the error, since its prime size, support jumps, divisor variation and local factors did not depend on the size of the balance window. It gives

$$
 \Sigma(N)\int_{\Delta}^{\sigma_2 L-\Delta}
    \frac{ds}{\Lambda_x-s}
      \sum_{A_-(s)<a\le A_+(s)}
          \frac{ r(a)\{X_a(s,x)-Y_a(s,x)\}}
             {a\,(\Lambda_x-h-\log a+s)}
 \tag{3}
$$

as the completed density at real $x$ for the surviving rejected tags, apart from a power-small density error. Here the actual selected squarefree parity of $a$ equals that of $m$, and

$$
 \log A_-(s)=s+\max(\sigma_1L,s+\Delta)-h,\qquad
 \log A_+(s)=s+\sigma_2L-h .
 \tag{4}
$$

Use zero if the interval is empty. Endpoints in (4) are those from the original strict/weak band and separation. The two denominators of (3) are kept, not frozen.

## 2. Uniform separated trace of the sharp coefficient

We claim uniformly for $x,s$ as in (3) and every upper endpoint $A\in[A_-,A_+]$, with $w=\log(A/A_-)$ and fixed total parity,

$$
 \sum_{\substack{A_-<a\le A\\\mu(a)=\pm1}}
      \frac{r(a)X_a(s,x)}a
  =\frac{w}{\log x}\bigl(h\mathcal C_r\pm1\bigr)+o(1).
 \tag{5}
$$

The sign at the constant corresponds to the sign of $\mu(a)$; in particular plus means even total. The constant $\mathcal C_r$ is the one in the [weighted odd calculation](r73-spectral-marked-prime-weighted-major.md), also used in the [even calculation](r74-spectral-even-marked-major.md). We give the arithmetic changes needed for this shorter cofactor, where the naive squarefree floor would be too large.

Put $U=\sqrt L$, $G=e^U$, $J_*=\lfloor32\log U\rfloor$, $V_G=\prod_{\ell\le G}(1-1/\ell)$. As in the [weighted count bound](r71-spectral-weighted-high-small-prime-count.md), $j(a)>J_*$ contributes $o(1)$ by positive Rankin on the majorant $\tau_4(a)r(a)/a$ for the two coefficients. The bound is still applicable since $a\le N^{2\sigma_2+o(1)}$ and $r(a)\ll a/\varphi(a)$. Split the rest exactly as $a=bv$, with $b$ squarefree supported on primes at most $G$, $j(b)\le J_*$, and $v$ strictly $G$-rough. Then $\log b=O(U\log U)=o(E)$ and $\sum_b r(b)/b\ll_{\mathcal R}U$. Also $r(v)=1+O((L/U)e^{-U})$, so dropping it costs $o(1)$ by the same coarse positive coefficient bound. Here the short sharp cutoff is fixed at $s$ or $s-h$ when $a$ varies, in either strict or weak form. In the square or bilinear product over $v$ the labels are at most $Z=e^s$.

On a dyad with lower endpoint $V_0\asymp v$ and literal clipped interval of log width $w_0$, the ordinary rough Bonferroni trace for squarefree rough LCM $d$ of two labels has main $w_0 V_G/d$. Its log tail is $O_A(w_0L^{-A}/d)$ for every fixed $A>0$. Indeed truncate the finite small-prime inclusion-exclusion at consecutive parities of degree $\asymp L_2^2$; the separated remainder in its main density follows by the usual factorial bound since $\sum_{\ell\le G}1/\ell=O(L_2)$, and the total modulus-one progression floors are at most $\exp(O(U L_2^2))/V_0$ by the number of retained subsets. For squarefreeness additionally exclude each $\ell^2\mid v$ with $\ell>G$. For $\ell\nmid d$ the intersection consists of multiples of $d\ell^2$, so its reciprocal floor is $O(1/V_0)$ but only $\ell\ll\sqrt{V_0/d}$ need be counted. Their total floor is $O((V_0 d)^{-1/2})$, and their main reciprocal bound is $(w_0/d)O(\sum_{\ell>G}1/\ell^2)$. For $\ell\mid d$ use multiples of $d\ell$, adding $O(L/V_0)$ in floors and $(w_0/d)O((L/U)e^{-U})$ in main. No roughness restriction is required in these positive upper bounds.

For the signed parity piece, $\mu(v)$ on multiples of $d$ is $\mu(d)\mu(v/d)\mathbf1_{(v/d,d)=1}$. Uniformly $v/d\gg\exp(\Delta-o(E))$, since $A_-\ge\exp(2s+\Delta-h)$ and $d\le Z^2$. The coprimality mask excludes all primes up to $G$ and the primes of $d$. Its positive smoothing convolution has exponential reciprocal moment at $1/U$ of size $O(U)$ by the same mask calculation as the prime-free and marked proofs (the extra primes of $d$ add $O((L/U)e^{-U+1})$ to its log). Ordinary Mertens, splitting at the square root of the residual scale, gives relative signed error $O(\exp(-cL^{1/6}))$, hence reciprocal error $O(\exp(-cL^{1/6})/d)$ uniformly on the hard dyad. For example, at variable $y\gg \exp(\Delta-o(E))$ the short mask range gives $O(Ue^{-c\sqrt{\log y}})$ and the long one $O(Ue^{-\log y/(2U)})$, using the ordinary unsigned bound on the remaining partial sums there. Partial summation gives the stated reciprocal error; no Möbius progression input is needed. Taking either $(\mu^2(v)+\mu(b)\mu(v))/2$ or its minus version thus gives main $w_0 V_G/(2d)$.

For the critical squarefree floor, the summed bound is

$$
 \sum_{d_1,d_2\le Z}[d_1,d_2]^{-1/2}\ll Z.
 \tag{6}
$$

Indeed set $d_1=g u,d_2=g v$ with coprime $u,v$ and sum two copies of $\sum_{u\le Z/g}u^{-1/2}\ll\sqrt{Z/g}$ against $g^{-1/2}$. Thus the squarefree floors and basic rough-count floors in the product are bounded by a fixed power of $L$ times

$$
 \frac Z{\sqrt{V_0}}+\frac{Z^2\exp(O(U L_2^2))}{V_0}
       \ll \exp(-cE),
$$

uniformly before summing dyads and the weighted $b$. The coefficients of the expanded products cost only powers of $L$, since their log weights are at most $O(L)$ and $\tau(b)\le2^{J_*}$. The reciprocal LCM sum of all labels has at most a fixed log power, so all errors with $1/d$ sum to $o(1)$ as well. This argument works also for the least partial upper intervals, with no lower bound on $w$.

Expand the gcd as in the preceding Euler proofs, and use the notation $A_{b,e}(u)=\sum_{d\mid b}\mu(d)R_{G,e}(u-\log e-\log d)$ for the signed shifted reciprocal Mertens primitive. At the presently fixed $s$, the sharp main trace has factor $w V_G/(2\log x)$ times the sum over $b$ with weight $r(b)/b$ and rough $e\le e^s$ of weight $\varphi(e)\mu^2(e)/e^2$ times the pointwise odd/even quadratic of the two shifted primitives and their integrals at $s$. This follows from the exact gcd identity by finite summation of the signed short labels, with the strict/weak convention still retained at this point.

To convert this new $e$ sum to an integral, omit $e<\exp(s-E)$. Its primitive factors have all log arguments at least $E-O(U\log U+h)\ge E/2$ after the shifts; the ordinary smoothed Mertens decay, as in the even proof, makes the product negligible even when an indefinite primitive is merely bounded. On the retained interval, replace $R_{G,e}$ by $R_G$ using the positive extra-prime-mask mass $1+O((L/U)e^{-U})$: the difference in supremum and $L^1$ norms is $O(L e^{-U})$, as are the differences of integrated primitives in supremum. This is because the remaining convolution has norm $O(U)$ before removing the extra primes, and that extra positive kernel has an atom of mass 1 at 0. The uniform difference $\varphi(e)/e-1=O((L/U)e^{-U})$ is harmless for the same reason. Now all appearances of $e$ in the pointwise product are through the real argument $s-\log e$. This function on the window $0\le s-\log e\le E$ has supremum plus variation bounded by a fixed power of $L$, uniformly for each retained $b$: the unintegrated primitive has variation at most the unsigned divisor reciprocal step sum $O(1+E)$ before $\tau(b)$ signed shifts, and the integrated versions are bounded by their full $L^1$ norms and their absolute variation on the window. At most one translated cutoff for a given label can lie at its endpoint; either convention is covered by the same variation estimate.

The rough harmonic trace through any subinterval of $[\exp(s-E),\exp(s)]$ is $V_G\,d\log e$ with error smaller than any inverse power of $L$, uniformly for all primitive intervals, after excluding rough prime squares as above. Indeed $s>\Delta$ makes the floor $\exp(O(U L_2^2))\exp(-(s-E))$ negligible, and the square exclusions have exponentially small floors and reciprocal tail on $O(L)$ dyads. Stieltjes partial summation against the just bounded variation therefore converts the $e$ sum to the stated real log integral uniformly. If the strict or weak representative at an interior jump is not chosen right-continuously, use both one-sided forms of this uniform trace, or bound atomic contributions by the same uniform endpoint error and total variation. Extending from the window to the full real line is again allowed by Mertens decay and $o(E)$ shifts. All these extra errors are $o(1)$ after the harmless factors $w/\log x$, $V_G$, the harmonic $e$ sum and $\sum_b r(b)/b$. In particular no parity-free replacement was made at the arithmetic square-root edge.

The prefactor is now $w V_G^2/(2\log x)$, times the same whole-line integral and weighted $b$ sum as the odd and even marked calculations. At $b=1$ use the exact even identity involving a centered finite interval convolution, not an assertion that the indefinite even primitive is in $L^2$. The multipliers are $h(2+2\cos(h\xi))-4\sin(h\xi)/\xi$ for odd, and $h(2-2\cos(h\xi))+4\sin(h\xi)/\xi$ for even. Extend the formal $b$ sum by the same weighted $z=2$ signed-shift bound and $O(U^4 2^{-J_*})$ tail; this is separate from the true Rankin truncation, and $w/\log x=O(1)$. The Euler factor $V_G^2$ and Fourier integral now give $w/\log x$ times $h\mathcal C_r-1$ or $h\mathcal C_r+1$ respectively, including the same $W^{1,1}$ cosine cancellation and sine limit. This proves (5).

## 3. The same separated trace of the true two low folds

Uniformly for the same intervals and either parity,

$$
 \sum_{\substack{A_-<a\le A\\\mu(a)=\pm1}}
       \frac{r(a)Y_a(s,x)}a
   =\frac{w}{\log x}(h\mathcal C_r-1)+o(1).
 \tag{7}
$$

The low formulas (7) of the balanced proof express both folds through $a=uv$, where the log range of $v$ lies within $O(L_2)$ of $s$, and $u$ then satisfies $A_-/v<u\le A/v$. In particular both variables exceed $\exp(8E)$ for large $N$. The same weighted two-factor CRT argument of §1 of the odd marked proof applies on these literally moving bounds. To check the slightly smaller lower size, the finite occupied/forbidden expansion through primes $\le L^{C_0}$ has total size and moduli $\exp(O_{B,C_0}(L_2^3))$, with the fixed radical excluded in both variables. The remaining square and collision tails can be bounded without the masks on ordinary dyads at cost $O(L^{-C_0}+\exp(-cE))$ per dyad pair, times powers of $L$; lower size $\exp(8E)$ suffices for the previous square-root floors, and $C_0$ can absorb every short label count. For the parity part, after fixing one integer factor and dividing the other by all prescribed polylogarithmic or $\exp(O(L_2^3))$ primes, its size still exceeds $\exp(7E)$. Its signed coprimality mask again has moment $O(U)$ at $1/U$ and the same split gives $O(\exp(-cL^{1/6}))$ relative. All these errors are uniform even on arbitrarily clipped reciprocal intervals. The actual unsigned half-density has factor $K_r/2$ and force-label factor $\alpha(d_1d_2)$, with exactly the weighted Euler factors of the odd marked proof. The sign of the negligible parity discrepancy does not matter.

For each fixed $v$ the integral in the other factor has exactly the log length $w$. In the two folds, change $\log v$ to $z=s-\log v$ and $z=h-s+\log v$ respectively. The integrals, including the two strict label constraints $d_i<e^z$ and weights $h-2z+\log(d_1d_2)$, both now use $0<z\le (B-B_0)\log L$ and have the same orientation after correcting the first Jacobian's sign. The two identical $w$ factors cancel the $1/2$ of the parity trace. The same $H_\alpha,D_\alpha$ of the odd proof therefore give (7) via $K_r\int H_\alpha=\mathcal C_r$, $K_r\int D_\alpha=-1$; extending those integrals to infinity costs $o(1)$ by the same first moments. There is no additional moving interval or small-factor exclusion.

## 4. From the exact separated density to the unique-largest result

Subtracting (7) from (5) shows that the numerator partial sums are $o(1)$ for odd and $2w/\log x+o(1)$ for even, uniformly in the literal endpoint. The weight $1/(\Lambda_x-h-\log a+s)$ has supremum plus variation $O(1/L)$ on (4). Partial summation, holding $s$ and $x$ fixed, yields the odd $o(1/L)$ and the even main

$$
 \frac2{\log x}\int_{\max(\sigma_1L,s+\Delta)}^{\sigma_2L}
                       \frac{dt}{\Lambda_x-t}+o(1/L).
$$

Restoring the outer $s$ integral and weight in (3) preserves the orders of these errors, since the support length is $O(L)$ and that weight is $O(1/L)$. Write $s/L=y'$, $t/L=y$, and use $\Delta/L=o(1)$, $\log x/L\to1$ and $\Lambda_x/L\to1/2$ uniformly. The rejected even density becomes

$$
 \frac{2\Sigma(N)}L
    \int_{\sigma_1}^{\sigma_2}\int_0^{y}
             \frac{dy'\,dy}{(1/2-y')(1/2-y)}+o(\Sigma(N)/L),
$$

since the denominators are bounded away from zero and the excluded edge areas tend to zero. The odd rejected density is $o(\Sigma(N)/L)$. The two ends from §1 retain the original weak uniformity on $I$ and the original major power error.

Finally the ordinary odd marked proof gives its zero main without its count restriction: the positive reciprocal tails separately remove both $X$ and $Y$ outside that window before the same marked major transfer. Its local floors and exact BV did not require a largest order. The even marked proof already states the count-unrestricted asymptotic. Each actual eligible largest tag is counted once in the marked sum, and each actual eligible smaller tag exactly once in the rejected sum; subtract the latter polynomials prior to using their asymptotics. Their even constants differ by (1), using $\int_0^y dy'/(1/2-y')=-\log(1-2y)$, and $1+\log(1-2y)>0$ for $y<1/10$. This proves (2). No estimate on the actual unique-largest minor follows from this subtraction of actual major coefficients.
