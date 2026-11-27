# The exact quarter-root floor for the curved containing row

Use exactly the carrier and physical tests of the [below-cube result](r113-source-below-cube-double-competitor.md). Thus $L=\log X,\ \ell=\log L,\ T=L/\ell,\ T_N=\log N/\log\log N$, each operand $n=hF$ or $m=kG$ is squarefree in the fixed hard physical window $\mathcal J$, the two operands sum to the even $N\in\mathcal X$, and both are actual $N$-units. Each cofactor has one prescribed old prime $s$ with $5T/4\le\log s\le7T/4$, the other prime factors are at least $e^{4T}$, and $F,G$ are the largest roots. The two selectable floors are the literal $F\ge\sqrt N e^{-aT_N}, G\ge\sqrt N e^{-bT_N}$. Retain the semiprime wing and the literal divisor/product cuts $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor,\ Q_N=\lfloor Ne^{-20T_N}\rfloor$. Write $U$ for the uncurved product of the two retained-long containing traces with exterior minus, $V_f$ for the forbidden-product correction with exterior plus, and $V_{\rm curv}=U+V_f$. The Walsh factor is $\mu(h)\mu(k)$, with no ordinary divisor arm.

Keep the refined single and double rejection profiles $K_a^{(1)},K_a^{(2)}$ of the below-cube proof, and put $J_a=K_a^{(1)}+K_a^{(2)}$. In contrast with that proof, the double profile is retained in the **forbidden** comparator as well as in the uncurved one. Set

$$
 \begin{split}
 A&=\ell/4+1/T,\qquad D=\{0\le g,g'\le20,\ g+g'\ge20\},
       \qquad I_N=\Sigma(N)B_{\mathcal J}(N),\\
 \mathfrak F_\ell(a,b)&=\iint_D J_a(g)J_b(g')\,dg\,dg',\\
 \mathfrak U_\ell(a,b)&=
      \left(\frac1{2\ell}-\int_{20}^\infty J_a(g)\,dg\right)
      \left(\frac1{2\ell}-\int_{20}^\infty J_b(g')\,dg'\right).
 \end{split}                                                        \tag{1}
$$

**Theorem (unconditional).** On the larger box $0\le a,b\le A$, independently selectable at each target, one has

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
  \sup_{0\le a,b\le A}
     \bigl(|V_f(N;a,b)-I_N\mathfrak F_\ell(a,b)|^2
              +|U(N;a,b)+I_N\mathfrak U_\ell(a,b)|^2\bigr)
      \ll X^3\ell^{-6}.                                            \tag{2}
$$

The comparator satisfies $\mathfrak U_\ell-\mathfrak F_\ell\gg\ell^{-2}$ uniformly on this box. On each fixed physical interior, one exceptional set of $O(X/\ell^2)$ even targets suffices for $V_{\rm curv}(N;a,b)\le -cX/\ell^2$ simultaneously for every such selection. The squared norm for any selection is of order $X^3\ell^{-4}$ on the target dyad. In particular the box includes the **exact** floor $N^{1/4}$ by choosing $a=(\log\log N)/4$ on either side. There is no conclusion below this root floor, for an individual exceptional target, for another row, or for the full sum or Hypothesis S.

The new sign bound pairs the two old-prime placements **by translation in the integrated nonlong variable**. It keeps the common-interval derivative of the sum of the two Stieltjes marks rather than estimating the two positive losses separately.

## 1. Nominal candidates and the quarter label seam

For a composite cofactor keep the exact completion of the long containing orbit to its nonlong complement $Fz\le D_N$, with Walsh mark $\mu(h)\mu(z)\log(h/z)$. The [genuine semiprime wing](r105-source-semiprime-wing-and-containing-contrast.md) still has the same unique nonzero retained-long mark $+\log s$, independent of the floor since $F>\sqrt N$, and no forbidden contribution since $F(D_N+1)>Q_N$. We do not change that wing model.

Take $u=(L/2-\log F)/T,\ g=(L/2-\log(Fz))/T$ on the actual integers. The true floor differs from $u\le a$ by $O(1/T)$ in this range; the physical reference triangle and the nonlong $g=20$ threshold differ from the literal divisor/product cuts by $O(1/T)$, just as in the below-cube proof. For the positive envelopes allow $g,u\ge-1$, $g\le\max(20,A)+2,\ u\le A+2$. On these bounds $F\ge X^{1/4-o(1)}$, and there are at most four separated roots in any operand counting multiplicity since five factors of this order exceed the physical window. The old prime is unique and every other cofactor prime has log at least $4T$, so the maximum number of labels and competitor choices per eligible operand remains a fixed power of $L$.

On a nominal cell $u\le A$, one has $F\ge e^{-1}X^{1/4}$. Four prime factors at least $F$, counted with multiplicity, would give a product at least $e^{-4}X$; the compulsory old prime $s\ge e^{5T/4}$ is distinct from all these factors and would make the operand exceed the entire physical window. Consequently on the nominal cells there can be only zero, one or two strict competitors $P>F$ in the cofactor. With a squarefree cofactor and after removing $F\mid h$, the exact canonical indicator is $1-r+\binom r2$, where $r$ is their count. As before we can subtract the repeated-root effect after applying this identity to the candidate sums: all such operands have the form $dF^2=O(X)$, and their support is

$$
   \ll \sum_{F\ge e^{-1}X^{1/4}} \frac{X}{F^2}\ll X^{3/4},          \tag{3}
$$

even summing over integers. With polylogarithmic weights, the fourth norm from this support is $X^{9/16+o(1)}$, negligible after counting all joint cells. This argument does not restrict the larger positive enclosure to the nominal candidate count.

There is a **new literal label issue at the quarter floor**. If any strict competitor $P>F$ divides $z$, then $Fz>F^2$, so $g<2u-\ell/2\le2/T$ on a nominal cell. Therefore on every safe cell with $g\ge\delta=\ell^{-6}$, the label has $z<F$ (indeed $2u-g<\ell/2$), and neither competitor is in $z$. The entire possible marked-competitor band belongs to the $g=0$ collar. It is estimated by the positive slab bound on the **actual canonical terms**, not by a model that wrongly prohibits a competitor there. In the nonlong part $g\ge20+O(1/T)$ it does not arise. This collar also includes any physical shift at the $g=0$ wall. No double rejection is discarded from the remaining forbidden cells, even when $0<g\le20$.

On every safe cell, with $z=s^jW_1$, the separated, singly selected and doubly selected cofactors $h=sW_1W_0,\ sW_1W_0P,\ sW_1W_0PQ$ respectively have signs $-(-1)^j\mu(W_0),\ (+1)(-1)^j\mu(W_0),\ -(-1)^j\mu(W_0)$. The second is subtracted and the third is added. The exact same nominal scalar $-J_a$ thus applies on safe labels, now including the whole modeled forbidden bulk.

## 2. The continued arithmetic comparator

Here are the range and boundary checks for reusing the below-cube Fourier proof at this endpoint. All occupied $F,h$ dyads, and the selected strict competitor scales, have log sizes in $[.24L,.76L]$ for sufficiently large $X$, and $hF\asymp X$. The argument only forces these scales on those variables, not on the remaining cofactor after removing marked or selected factors. The lower dyadic powers still make the reciprocal-distance minor supremum arbitrarily inverse-log small on the same auxiliary polylogarithmic arcs. No prime distribution in progressions beyond polylogarithmic moduli is needed. The half-integer Perron separations for $hF,Fz,F<\min(P,Q)$ on the double and the fewer separations on the other arms are unchanged. One or two selected factors are part of the cofactor coefficient before the $h,F$ bilinear minor estimate. The weight and multiplicity budgets in Section 1 still give Parseval energy $O(X L^{O(1)})$.

On majors, at fixed cofactor and candidate label, Siegel–Walfisz in $F$ on the clipped hard interval gives the common $H=(\mu(q)/\varphi(q))\widehat J_{\mathcal J}(\beta)$ on reduced major fractions, zero off the majors. All cofactor prime divisors exceed the polylogarithmic denominator cap. Subsequent reciprocal PNT on a selected $P$ is the same interval calculation as previously, with $\log P\asymp L$. For the double, order the selected primes $P>Q$, and first replace $P$ at fixed $x=hF,Q,s,W_1,W_0$. The two strict inequalities $P>F,\ Q>F$ and $P>Q$ and the label/root cells still bound $P$ by an interval; then change to $g$ and replace $Q$ on the half fiber $D_{f,j}<\log Q/L<(S_j^*(w)+\xi)/2$, $\xi=(\log x-L)/L$. Here $w=\log W_0/T,\ \lambda=\log W_1/T,\ t=\log s/T,\ u_j=g+\lambda+jt$, as previously, and $D_{f,j}=1/2-u_j/\ell,\ S_j^*(w)=1/2+[g+(j-1)t-w]/\ell$. The paired cap is $S_j^*(w)+\xi>2D_{f,j}$. The resulting exact real mark is the R113 double half-fiber; its shifted cap has continuous zero extension, and on it the derivative in $\xi$ is $O(\ell^{-1})$. Both real models have denominators bounded away from zero, now $D_{f,j}\ge1/4-O(1/L)$; on the occupied single cap $S_j^*\ge D_{f,j}$, on a double cap $S_j^*\ge2D_{f,j}$. Thus physical freezing, BV bounds, polylogarithmic absolute errors, and the ordered competitor and low-tuple replacement steps have the same quantitative bounds as in Sections 2 and 4 of the below-cube proof. No reciprocal prime approximation is made on an unsafe $g=0$ collar.

In the separated signed term the unmarked log at fixed $x$ is $v=1/2+\xi+[g+(j-1)t]/\ell$, independent of the marked log. It lies in a fixed compact subset of $(0,.80)$ on the active slices. Use working rough alphabet upper cap $.80$, instead of $.70$, which changes no active low tuple. The signed unmarked Dickman density $-\rho(v\ell/4-1)/v$ on this range is $O_B(\ell^{-B})$ for every fixed $B$; the positive unmarked density is $O(\ell)$. The positive marked mass through $A+O(1)$ is $O(A+1)$. Integrating the reference $g$- or $u$-slab of width $d$ clips the unmarked log to width $O(d/\ell)$, total moving physical endpoint variation $O(1/L)$, holding the marked data fixed. The resulting positive fourth bounds on inverse-$\ell$ widths and on the enlarged full support are

$$
  \|A^+_{\rm slab}\|_4\ll X^{3/4}(A+1)(d+1/T),\qquad
   \|A^+_{\rm full}\|_4\ll X^{3/4}(A+1)^2 .                       \tag{4}
$$

These use separated positive domination of all candidate roots, not their signed difference, and can be used on every unsafe collar and floor-restoration slab. Squarefree tuple replacement errors are negligible by the same reciprocal-square estimates, since the smallest prime remains at least $e^{5T/4}$.

Take $g$ mesh $\delta=\ell^{-6}$, split at $0,20$, and right-closed $u$ mesh $\eta=\ell^{-14}$, split at $0,A$. On the safe nominal cells with label $B$ and root interval $(a_-,a_+]$, $m_{B,(a_-,a_+]}=-\int_B(J_{a_+}-J_{a_-})\,dg$ is therefore the signed composite scalar, and the sum of fourth norm errors against $m_{B,(a_-,a_+]}H$ is $O(X^{3/4}\ell^{-20})$ over $O(\ell^{22})$ cells. The unpaired scalar budget $\sum|m_{B,(a_-,a_+]}|=O(1)$ still follows separately for each model: for the single use the endpoint factorial bound and the per-placement derivative $O(\ell^{-2})$ on a total marked area $O(\ell^2)$; for the double its cap mark vanishes and the Stieltjes integral is bounded by the same derivative using $\int S\le12$, likewise before the placement pairing. Fixed constants from all these ranges are independent of $a,b$.

## 3. The integrated old-placement bound

We establish the uniform controls needed for sign and transfer. Denote by $S(w)=\rho_+(w/4)$ the Dickman cumulative, with its atom at zero, and by $\mathcal P$ the positive marked measure with a unit atom and density at most $1/4$, as in the [fixed-box comparator](r107-source-curved-containing-fixed-box-sign.md). For the $j=0$ placement define $Z_1=2g+\lambda-t,\ Z_2=3g+2\lambda-t-\ell/2,\ d=1/2-(g+\lambda)/\ell,\ s(w)=1/2+(g-t-w)/\ell$. The variable $s(w)$ here is a normalized **logarithmic sum** and not the old prime. Strip off the common numerator $Q(g)=1/2+g/\ell$ from the two R113 marks:

$$
 G_1(w)=\frac1{\ell d\,s(w)},\qquad
 G_2(w)=\frac1{\ell d\,s(w)}
                   \log\frac{s(w)-d}{d}.
                                                                    \tag{5}
$$

Use each mark only on $0\le w\le Z_i$, with zero contribution for a negative cap. Here $Z_2\le Z_1$ since $Z_1-Z_2=\ell d$. The double endpoint has $G_2(Z_2)=0$ and the single endpoint has $s(Z_1)=d$. All right-continuous integration by parts below includes the initial $dS$ atom, so its endpoint term is $S(Z_i)G_i(Z_i)$, with no additional left endpoint.

At fixed $t,\lambda$, the $j=1$ term at $g$ has exactly the $j=0$ cap and denominators at $g+t$, and $u_1(g)=u_0(g+t)$. Indeed the $j=1$ normalized cofactor log is $1/2+(g-w)/\ell$, which agrees with $s(w)$ at $g+t$; the root log agrees as well, so both caps and (5) align. The numerator in the $j=1$ term is $Q(g)$, whereas the $j=0$ term at $g+t$ has $Q(g+t)$. Write $V(g,\lambda,t)=\sum_{i=1}^2\int_{[0,Z_i]}G_i\,dS$ and $\mathbf 1_a(g,\lambda)=1_{g+\lambda\le a}$. The **exact** identity is

$$
 \int_{20}^\infty J_a(g)\,dg
   =\int_{5/4}^{7/4}\frac{dt}{t}\int d\mathcal P(\lambda)
      \left[
        \int_{20}^{20+t}\mathbf 1_a(g,\lambda)Q(g)V(g,\lambda,t)\,dg
       +\frac{t}{\ell}\int_{20+t}^\infty
                \mathbf 1_a(g,\lambda)V(g,\lambda,t)\,dg
      \right].
                                                                    \tag{6}
$$

The same change of variables in the simple model $C_a/\ell$ (single mark $2/\ell$, no double) cancels the entire common tail, and leaves just $2S(Z_1)/\ell$ in the boundary integral.

On the boundary $20\le g\le20+t$, subtract this simple scalar. In the single mark the endpoint difference is $S(Z_1)[Q(g)/(\ell d^2)-2/\ell]$, bounded in absolute value by $O(\ell^{-2})(1+g+\lambda)S(Z_1)$, integrable against $dg\,d\mathcal P\,dt/t$. Its derivative term has nonpositive sign because $G_1'\ge0$. The double contribution is $O(\ell^{-2})$ after these same integrations: with $g=O(1)$, its active condition $3g+2\lambda-t\ge\ell/2$ and the floor $g+\lambda\le A$ force $\lambda=\ell/4+O(1)$; the marked measure there is $O(1)$, and $\|\partial_w G_2\|_\infty\ll\ell^{-2}$ times $\int S\le12$ bounds the signed Stieltjes value. The single endpoint on the common tail is $O(\ell^{-2})$ after the coefficient $t/\ell$, by the factorial $S(Z_1)$ envelope. The double endpoint is zero there too.

Only a positive bound on the remaining minus derivative integrals in the common tail is needed. Outside the double cap $G_1'\ge0$ gives the helpful nonpositive sign. Inside that cap, put $x=s(w)/d\ge2$. Direct differentiation of (5), with $s'(w)=-1/\ell$, gives

$$
   G_1'(w)+G_2'(w)
      =\frac{\log(x-1)-1/(x-1)}{\ell^2 d\,s(w)^2}
      \ge -\frac{16+O(1/L)}{\ell^2}.                             \tag{7}
$$

The logarithmic expression is at least $-1$; $d\ge1/4-1/L$, $s(w)\ge2d$. For each $t$ the occupied double area under $dg\,d\lambda$ is at most $\ell^2/96+O(\ell)$: putting $u=g+\lambda\le A$ and retaining $\lambda\ge0$, the cap implies $g+2u\ge\ell/2+t$. The $g$ width is at most $(3u-\ell/2-t)_+$; integrate from $0$ to $A$. Under $dg\,d\mathcal P$ the continuous part is at most one quarter of this area and the atom costs $O(\ell)$. The positive common derivative loss in (6) is therefore at most

$$
 \frac{1}{\ell}\left(\frac74-\frac54\right)
       \frac{16+O(1/L)}{\ell^2}\,12
       \left(\frac{\ell^2}{384}+O(\ell)\right)
    =\frac{1}{4\ell}+O(\ell^{-2}).                                \tag{8}
$$

This is a one-sided upper bound, not a claimed signed asymptotic for the drift on its own. Altogether, if $c_a=\int_{20}^\infty C_a(g)\,dg$, then $\int_{20}^\infty J_a\le (c_a+1/4)/\ell+O(\ell^{-2})$.

For completeness the absolute controls survive on the quarter box:

$$
    \|J_a\|_1+\|J_a\|_\infty\ll\ell^{-1},\qquad
          \|J_a-C_a/\ell\|_{L^1([0,20])}\ll\ell^{-2}.             \tag{9}
$$

For the single use the endpoint factorial bounds of the below-cube proof and the common derivative difference $O(\ell^{-3})$ (in absolute value the interpolation only needs fixed positive denominators). The total common area is $O(\ell^2)$, the fixed-strip area $O(\ell)$, the extra cap has bounded width and integrable factorial envelope, and the singly fitting old-placement strip has bounded width in $g$ at fixed $\lambda,t$, or bounded $\mathcal P$ mass at fixed $g,t$. This yields the two $L^1$ estimates; at fixed $g$ the unpaired derivative costs $O(\ell^{-2})$ against marked mass $O(\ell)$, giving supremum. For the double the same common derivative difference $O(\ell^{-3})$, zero-cap endpoint, extra interval of width at most $3t$ with integrable $S(\max(0,Z_0^{(2)}))$ in $g$, and singly allowed strip give $L^1=O(\ell^{-1})$. The unpaired derivative gives the same supremum bound. On the fixed forbidden strip $g\in[0,20]$ **both** fitted double placements have $\lambda=\ell/4+O(1)$, by the active double cap and the floor; this includes both hard endpoints and bounds the double profile uniformly there by $O(\ell^{-2})$. This proves (9), without asserting the double is absent from the actual forbidden strip.

The fixed-box bounds are $|c_a|\le17/2041200$ and $|f(a,b)|<1/20$ for $f(a,b)=\iint_D C_a(g)C_b(g')\,dg\,dg'$. From (9), $\mathfrak F_\ell=f(a,b)/\ell^2+O(\ell^{-3})$. By (8), each uncurved factor in (1) is at least $[1/4-17/2041200-O(1/\ell)]/\ell$. The square of the constant $1/4-17/2041200$ exceeds $1/20$. This gives the uniform strict comparand gap. It is essential to compare to the fully refined model in (1) on the arithmetic side, not to drop the common-tail derivative term at fixed $\ell$ or to replace the double forbidden model by zero.

## 4. Common exceptional set for the exact predicates

For the selected row, apply the nominal cell transfer of the below-cube proof with the new safe $g=0$ exclusion. On safe cells multiply signed bulk cell polynomials before taking absolute errors, and use Hölder–Parseval with the summed cell budget in Section 2. This is one target majorant independent of the accepted root prefixes. The forbidden scalar is obtained from $J_aJ_b$, with no discarded bulk term. For $U$, telescope the whole nonlong composite prefix before multiplying against the fixed wing Fourier error: (9) bounds that summed prefix scalar by $O(\ell^{-1})$, and the wing error is $O(X^{3/4}\ell^{-2})$ in fourth norm. Thus the wing comparisons still cost $O(X^{3/2}\ell^{-3})$ in target norm. The common factor $[H^2]_N$ is replaced by $I_N$ at arbitrarily small inverse-log target norm by the [rational completion](r80-source-local-mean-square-at-sign-transition.md), Section 3.

The real collars are $O(\delta/\ell^2)$ by (9). Treat every actual label collar by positive domination, including the whole marked-competitor band near zero from Section 1. There are $O(\delta^{-1})$ forbidden label cell pairs including those at the zero boundary, and $O(1)$ nonlong seam bins against a whole positive mate. The two target norm costs are $O(X^{3/2}(A+1)^2\delta)$ and $O(X^{3/2}(A+1)^3\delta)$ by (4). Return all true $N$-unit constraints uniformly: shared primes divide $N$, are at least $e^{5T/4}$ and give $O(X/p+1)$ allowed first operands, with at most $O(\ell)$ candidates and fixed polylogarithmic multiplicity. This is an inverse-power-of-$L$ pointwise cost, also when a wing occurs.

Passing from nominal mesh nodes to any actual selected floor costs at most the maximum positive root slab of width $O(\eta)$ including endpoint slivers and the $O(1/T)$ shift, against a whole positive mate. Use the exact nonlong complement first for $U$, keep all other actual cuts, and note the wing has no root-floor difference. Summing squared norms over $O((A+1)/\eta)$ slabs yields $O(X^{3/2}(A+1)^{7/2}\eta^{1/2})=O(X^{3/2}\ell^{-7/2})$ per side in target norm. The model interpolates by $\|J_a-J_{a'}\|_1\ll(A+1)|a-a'|/\ell$, by clipping $g$ at fixed marked data and bounding the two marks and the $dS$ variation. This interpolates the model at negligible cost and proves (2) without a union over the continuum of floor pairs.

On a fixed physical interior $I_N\gg X$ for even targets and $\|I_N\|_2\ll X^{3/2}$ globally. The strict deterministic gap and Chebyshev for the common maximum give the asserted exceptional set and norm order. Since $\log\log N-\ell=O(1/L)$, the exact quarter-root selections lie in the allowed box even at the physical endpoints.
