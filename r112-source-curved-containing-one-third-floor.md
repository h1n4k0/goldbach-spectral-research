# A common negative curved containing sign down to the true one-third root floor

Keep the precise carrier and the two-full Walsh channel of the [polynomial-floor comparison](r111-source-curved-containing-polynomial-floors.md). Thus $\mathcal J$ is its fixed hard physical window, $\mathcal X$ its even target dyad, $L=\log X$, $\ell=\log L$, $T=L/\ell$, $T_N=\log N/\log\log N$, and $n=hF,m=kG\in\mathcal J$, $n+m=N$, are actual squarefree $N$-units with largest primes $F,G$. Each cofactor has the prescribed one old prime $s$ with $5T/4\le\log s\le7T/4$, every other prime at least $e^{4T}$, and the actual semiprime wing is allowed. Retain the true root floors $F\ge\sqrt N e^{-aT_N}$, $G\ge\sqrt N e^{-bT_N}$ and integer $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$, $Q_N=\lfloor Ne^{-20T_N}\rfloor$. Use the same $U$ (uncurved two actual long containing traces with exterior minus), $V_f$ (forbidden retained-long correction with exterior plus), and $V_{\rm curv}=U+V_f$ (actual curved containing-containing row). All three have Walsh factor $\mu(h)\mu(k)$, and no ordinary divisor arm.

Use the same refined $\ell$-dependent $K_a$ of the [paired-drift calculation](r110-source-curved-containing-paired-drift.md), and let

$$
 \begin{split}
  D&=\{0\le g,g'\le20,\ g+g'\ge20\},\qquad
     I_N=\Sigma(N)B_{\mathcal J}(N),\\
  \mathfrak F_\ell(a,b)&=\iint_D K_a(g)K_b(g')\,dg\,dg',\\
  \mathfrak U_\ell(a,b)
    &=\left(\frac1{2\ell}-\int_{20}^\infty K_a(g)\,dg\right)
      \left(\frac1{2\ell}-\int_{20}^\infty K_b(g')\,dg'\right).
 \end{split}                                                     \tag{1}
$$

**Theorem (unconditional).** Put $A_*=\ell/6+1/T$. The two floors can be selected independently at every actual target anywhere in $[0,A_*]$, and

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
 \ \sup_{0\le a,b\le A_*}
   \bigl(
     |V_f(N;a,b)-I_N\mathfrak F_\ell(a,b)|^2
        +|U(N;a,b)+I_N\mathfrak U_\ell(a,b)|^2
   \bigr)\ll X^3\ell^{-6}.                                      \tag{2}
$$

Moreover $\mathfrak U_\ell-\mathfrak F_\ell\gg\ell^{-2}$ uniformly on this entire box. Thus, in each fixed interior physical subwindow, one exceptional set of $O(X/\ell^2)$ even targets suffices for $V_{\rm curv}(N;a,b)\le-cX/\ell^2$ simultaneously for all choices of $a,b$. The squared norm for any such selection has order $X^3\ell^{-4}$. The selectable endpoint includes the **exact** floor $N^{1/3}$ on either or both sides: put $a=(\log\log N)/6$ or $b=(\log\log N)/6$, which lies below $A_*$ since $\log\log N-\ell=O(1/L)$. There is no sign assertion below this floor, for other rows or Walsh channels, for an individual prescribed exception, or for the full pair sum or Hypothesis S.

The sign step is directional, rather than an absolute small-drift estimate over a macroscopic box: on the common part of the two old-prime placements the smooth Stieltjes derivative moves in the favorable direction. At the exact one-third endpoint a separate arithmetic fact is needed: the mandatory distinct old prime prevents three nominal root-sized factors even at the cube-root threshold.

## 1. Nominal two-root geometry and the genuine enlarged positive enclosure

On a composite cofactor the complete containing orbit vanishes, so its exact long Walsh trace equals
$\sum_{Fz\le D_N}\mu(h)\mu(z)\log(h/z)$.
A [genuine wing](r105-source-semiprime-wing-and-containing-contrast.md) has only the nonzero signed long mark $+\log s$ at its canonical root, with $F>\sqrt N$ and $F(D_N+1)>Q_N$. It never occurs in $V_f$, and is independent of the two floor choices exactly as before.

For a composite arm use the actual coordinates

$$
    u=(L/2-\log F)/T,\qquad g=(L/2-\log(Fz))/T=u-\log z/T .
                                                                    \tag{3}
$$

The true root threshold is $u\le a+O(1/T)$ uniformly for all $a\le A_*$, because $T_N/T-1=O(1/L)$ and $a=O(\ell)$. The true triangular walls of $V_f$ differ from $D$ by $O(1/T)$: the two long conditions and the product cap have log displacement $O(1)$, and each actual label is below $\sqrt N$ by $Q_N/(D_N+1)<\sqrt N$. The nonlong composite trace has $g\ge20+O(1/T)$ and $g\le a+O(1/T)$. For positive domination allow $g,u\ge-1$, $g\le\max(20,A_*)+2$, $u\le A_*+2$, covering the end slabs and all possible floor slivers. Then $F$ is between $X^{1/3-o(1)}$ and $X^{1/2+o(1)}$, the cofactor $h=x/F$ for $x\in\mathcal J$ is between $X^{1/2-o(1)}$ and $X^{2/3+o(1)}$, and $z\le X^{1/6+o(1)}$. A physical integer in this positive enclosure can have at most three eligible separated roots (counting multiplicities), since four factors of size at least $X^{1/3-o(1)}$ already exceed the window. This enclosure is only for positive bounds and does not require unique rejection.

The **nominal** hard root cells have $u\le A_*$ exactly, so $F\ge e^{-1}X^{1/3}$. If the separated integer $hF$ on these cells had three primes at least $F$ counting multiplicities, they would contribute at least $e^{-3}X$, and the compulsory old prime $s\ge e^{5T/4}$ is distinct from each of them. Their product would exceed the entire physical window. Thus if a root is rejected because some $P\mid h$ is greater than $F$, that $P$ is unique. Rejection by a repeat $F\mid h$ is disjoint from this strict rejection, by the same argument with two copies of $F$. A repeated integer has form $d_0F^2$ with $d_0\ll e^{(2A_*+1)T}=X^{1/3+o(1)}$ and $F\le X^{1/2+o(1)}$. Its total support is $X^{5/6+o(1)}$, and its coefficient has fixed polylogarithmic size, so interpolation of Fourier supremum and Parseval bounds its fourth norm by $X^{5/8+o(1)}$. That is negligible even when summed over the cell grid. All label multiplicities used here, including in the positive enclosure, are fixed $L$-powers because the actual cofactor has at most $1+\log h/(4T)=O(\ell)$ primes. No support strengthening from the nominal cells is imposed on the actual end slabs.

## 2. Fourier comparison at the extended prime ranges

We verify the extension of the marked/unmarked rooting and the refined cell comparison to these new scales. Use the same auxiliary polylogarithmic arcs and common transform $H=(\mu(q)/\varphi(q))\widehat J(\beta)$ on reduced majors, zero off, as in the [first curved calculation](r106-source-curved-containing-forbidden-collision.md). All cofactor primes are larger than the denominator cap $P_{\rm arc}=L^{C}$, and on the occupied intervals all large prime and cofactor variables have scale between $X^{.32}$ and $X^{.69}$. Siegel–Walfisz in $F$ at fixed cofactor/label therefore gives the same exact numerator factor with arbitrary inverse-log absolute errors after phase and coefficient powers of $L$. When there is a strict rejection, ordinary reciprocal PNT in the prime $P$ at fixed remaining variables and physical $x=hF$ is still on a hard interval with $\log P\asymp L$. No congruence on $P$ is introduced after evaluating the prime $F$.

For minors divide into dyads $h\asymp M,F\asymp K$ with $MK\asymp X$, both lengths between the above fixed polynomial bounds. The original Cauchy reciprocal-distance squared relative bound

$$
 L^{O(1)}\left(q^{-1}+K^{-1}
                      +\frac{\log(2q)}{M}+\frac{q\log(2q)}{X}\right)
$$

uses only these lower bounds and Dirichlet $P_{\rm arc}<q\le\lfloor X/P_{\rm arc}\rfloor$. It gives arbitrary inverse-log supremum relative to $X$ when $C$ is increased. The half-integer Perron separations for $hF,Fz,F<P(h)$ are exactly as before: the positive and separated arms omit the last, and an actual root bin is simply a hard interval in $F$. The separating numbers and all products are at most $X^{1+o(1)}$ on the relevant supports, so truncation $X^4$ with line $\Re s=1/L$ and the same bounded twists is adequate. All coefficients are $L^{O(1)}$ by Section 1, with energy $O(XL^{O(1)})$ even in the positive enclosure allowing three candidate roots. This proves the required small minor fourth norms and leaves no implicit near-equal-power dyadic assumption.

In a separated composite arm use exactly $h=sW_1W_0,z=s^jW_1$ with $j=0,1$, and thus the full sign $-(-1)^j\mu(W_0)$. At fixed physical $x=hF$ set $t=\log s/T$, $\lambda=\log W_1/T$. Then the true unmarked log for the real density satisfies

$$
 v=\log W_0/L
   =\tfrac12+(\log x-L)/L+[g+(j-1)t]/\ell,
                    \qquad u=g+\lambda+jt .                    \tag{4}
$$

Here $v\in[.4,.69]$ throughout the enclosing active support due to $g\le\ell/6+O(1)$. Thus the unmarked argument is still in a fixed compact domain away from zero and below the permitted alphabet cap $.7$, **independent of $\lambda$**. This is what extends the no-peeling argument to one-third. In particular no real empty unmarked product can occur on these active slices, while the actual empty marked part is kept.

The reciprocal tuple replacement on the two groups holds with arbitrary fixed inverse-$L$ accuracy: through $X^{.7}$ each group has total prime reciprocal mass $O(\log\ell)$, and all primes start above $e^{5T/4}$. At fixed other factors the conditions are affine hard slices in one log coordinate; the bare ratio is bounded with uniform or fixed-polylog variation. Expanding ordered tuples and telescoping comparisons costs the same factorial generating sums as in the polynomial-floor proof, with the distinctness difference bounded by the reciprocal-square tail, including across the two groups. This procedure does not remove any true squarefree or coprimality condition from the arithmetic polynomial. In the resulting real density the unmarked signed factor on (4) is $-\rho(v\ell/4-1)/v$, retaining the complete signed rough alphabet from $4/\ell$ up to $.7$; the positive version is $O(\ell)$ by coordinate marking. The signed value is smaller than every fixed inverse power of $\ell$ on the entire compact domain, and never needs a peeled-atom tail bound. The positive marked mass through $\lambda\le A_*+O(1)$ is $O(A_*+1)$ by the positive convolution estimate in the [fixed-box sign proof](r107-source-curved-containing-fixed-box-sign.md). At fixed marked data a $g$-bin or $u$-slab of width $d$ clips $v$ at width $O(d/\ell)$ with variation in its endpoints $O(1/L)$ across $\mathcal J$. The prime ratio $\log(h/z)/\log F$ is bounded there and physically differentiable on the common interiors with derivative $O(1/(XL))$ at fixed cofactor/label. Integrating the common intervals and the moved endpoints therefore gives exactly the fourth norms required on these inverse-$\ell$ widths:

$$
 \|A^+_{\rm slab}\|_4\ll X^{3/4}(A_*+1)(d+1/T),\qquad
 \|A^+_{\rm full}\|_4\ll X^{3/4}(A_*+1)^2,\qquad
 \|A^{\rm root}_{B,J}\|_4\ll_D X^{3/4}\ell^{-D}.                  \tag{5}
$$

For each major estimate use physical supremum plus variation and the same fourth integral of $\min(X,|\beta|^{-1})$; the inverse-$L$ discrete errors use supremum in the physical variable and need not be differentiated. This is a uniform proof on the new enclosing range.

In strict rejection on nominal cells the unique $P$ gives $h=sW_1W_0P$ and $z=s^jW_1$ (the label is too small to contain $P$). There the sign is $(-1)^j\mu(W_0)$, and, writing $w=\log W_0/T$, the hard real condition is
$w<Z_j+(\log x-L)/T$ with $u_j=g+\lambda+jt$ and $Z_j=2g+\lambda+(2j-1)t$ as before. Freezing only the physical shift and smooth physical mark at $x=X$ gives exactly the rational mark
$R_j(w)=(1/2+g/\ell)/[\ell D_{p,j}(w)D_{f,j}]$, where

$$
         D_{p,j}(w)=\tfrac12+(g+(j-1)t-w)/\ell,\qquad
              D_{f,j}=\tfrac12-u_j/\ell .                        \tag{6}
$$

On each occupied frozen cap $0\le w\le Z_j$, $D_{p,j}(w)\ge D_{p,j}(Z_j)=D_{f,j}\ge1/3-O(1/L)$; upper bounds on both denominators are absolute. The small physical shifts preserve polynomial ranges and these absolute ratio bounds. For fixed low data the wall moves a total $O(1/T)$ in $g$ and the physical derivative of the mark on common intervals is $O(1/(X\ell L))$. The positive weight of the two low labeled groups through their necessary log cutoff $2A_*+O(1)$ is $O((A_*+1)^2)$; all freeze errors in physical supremum and variation are thus inverse-log small after any polynomial grid in $\ell$. Only a real density is frozen. The tuple replacements with the literal interval caps and mark are as in the preceding paragraph. The signed unmarked cumulative is $S(w)=\rho_+(w/4)$ including its unit atom, and the positive marked measure is $\mathcal P(d\lambda)$. On the occupied cap $t+\lambda+w\le2u_j\le2A_*$, so locally using the full exponential real measures changes no active cap. The atom equality after freezing is null in $g$ at fixed other data. This gives exactly the refined profile $K_a$ of the paired-drift proof, with $R_j$ kept inside its Stieltjes integral.

Take the label mesh $\delta=\ell^{-6}$ split at $0,20$ and the right-closed root mesh $\eta_0=\ell^{-14}$ split at $0,A_*$, as in the [adaptive cell argument](r108-source-curved-containing-adaptive-floors.md). For modeled cells $g>0$ forces $u>0$; outer and equality slivers stay at the literal collar. There are $O(\ell^{22})$ joint cells. For the actual composite canonical signed cell arm $A_{B,J}$ (only units temporarily suppressed), $J=(a_-,a_+]$, its scalar is
$m^\natural_{B,J}=-\int_B(K_{a_+}-K_{a_-})\,dg$.
The minus sign is the subtraction of the strict rejected-root arm from the separated arm. Altogether (5), the repeat bound and the uniform real comparison show

$$
 \sum_{B,J}\|A_{B,J}-m^\natural_{B,J}H\|_4\ll X^{3/4}\ell^{-20},
 \qquad
 \sum_{B,J}|m^\natural_{B,J}|
       \ll \ell^{-1}+(A_*+1)^2\ell^{-2}=O(1).                    \tag{7}
$$

For the last budget use the integrable factorial envelope of each of the two leading positive summands $2S(Z_j)/\ell$, partitioning $g$ over all joint cells at fixed $(t,\lambda,j)$. By partial summation the endpoint difference from $2S(Z_j)/\ell$ is absolutely integrable over $(g,\lambda,t)$ with $O(\ell^{-2})$, since it is bounded by $O(\ell^{-2})(1+g+\lambda)S(Z_j)$ and $\mathcal P$ has unit atom and density $\le1/4$. The derivative correction is uniformly $O(\ell^{-2})$ per $(g,\lambda,t,j)$ since $R'_j=O(\ell^{-2})$ and $\int_0^\infty S<\infty$. Its total absolute area budget is $O((A_*+1)^2)$ when summing the partition. This does not assume a pairwise sign for arithmetic bin errors.

## 3. Directional drift and the refined sign

Let $C_a,c_a,f(a,b)$ denote the simple functions of the fixed-box proof, so replacing $R_j$ by $2/\ell$ in the refined profile gives $C_a/\ell$ and $c_a=\int_{20}^\infty C_a$. We prove the uniform estimates

$$
 \begin{split}
  \|K_a\|_1+\|K_a\|_\infty&\ll\ell^{-1},\\
  \|K_a-C_a/\ell\|_{L^1([0,20])}&\ll\ell^{-2},\\
  \int_{20}^\infty K_a(g)\,dg&\le c_a/\ell+O(\ell^{-2}),
                 \qquad 0\le a\le A_* .                         \tag{8}
 \end{split}
$$

For $Z_j\ge0$ use the literal Stieltjes integration by parts including its unit atom:

$$
  \int_{[0,Z_j]}(R_j(w)-2/\ell)\,dS(w)
    =S(Z_j)(R_j(Z_j)-2/\ell)
                 -\int_0^{Z_j}S(w)R'_j(w)\,dw .                  \tag{9}
$$

For $Z_j<0$ it is simply zero. The endpoint differences are absolutely integrable with budget $O(\ell^{-2})$ as above. Indeed $D_{p,j}(Z_j)=D_{f,j}$, factors remain in a fixed compact positive interval, and hence $|R_j(Z_j)-2/\ell|\ll(1+g+\lambda)/\ell^2$; any polynomial in $g+\lambda$ is defeated by the factorial $S(Z_j)$ for $Z_j\ge0$, after integration against the unit and bounded density of $\mathcal P$. The extra derivative interval where both placements fit but $Z_0<w\le Z_1$ has $\ell^{-2}$ times the integrable envelope $O(S(\max(0,Z_0)))$, since $Z_1-Z_0=2t=O(1)$; when $Z_0<0$ the $(g,\lambda)$ range $2g+\lambda<t$ is bounded. Thus it too costs $O(\ell^{-2})$ in absolute norm on either domain in (8).

For the common derivative interval interpolate the placements by $q\in[0,1]$ in (6), not to be confused with a rational denominator. Both placements fitting gives $u_q=g+\lambda+qt\le a$ and $w\le Z_0\le Z_q=2g+\lambda+(2q-1)t$. Then all denominators are positive and

$$
 \begin{split}
 R'_q(w)&=\frac{1/2+g/\ell}{\ell^2 D_{p,q}(w)^2D_{f,q}},\\
 \partial_q\log R'_q(w)
   &=\frac{t}{\ell}\left(\frac1{D_{f,q}}-\frac2{D_{p,q}(w)}\right),\\
 D_{p,q}(w)-2D_{f,q}
   &\le -\tfrac12+(g+2u_q)/\ell
      \le -\tfrac12+3a/\ell
      \le 3/L .
 \end{split}                                                       \tag{10}
$$

The last step uses precisely $A_*=\ell/6+1/T$. Thus the positive part of $R'_1-R'_0$ is $O(\ell^{-3}/L)$ throughout the common interval (if $a\le\ell/6$ it is zero). Its absolute value is $O(\ell^{-3})$ by the same derivative with the fixed denominator bounds. In the difference of the two old placements in $K_a$, the derivative term on this interval is $+\int S(w)(R'_1-R'_0)(w)dw$. Consequently its positive part, integrated over all $g,\lambda,t$, is $O((A_*+1)^2/(\ell^3 L))$. The other derivative interval, where only $u_0\le a<u_1$ fits, has sign $-\int S R'_0\le0$. There is no singly allowed $j=1$ interval. This proves the last bound in (8), after the absolutely integrable endpoint and extra terms. The slight endpoint padding contributes only the displayed negligible positive error.

For the absolute bound on the fixed forbidden label strip $0\le g\le20$, the common derivative difference costs $O(\ell^{-3})$ before the $g,\lambda,t$ integration, whose area is $O(A_*+1)$ on this strip. The singly allowed derivative strip at fixed $g,t$ is an interval of length at most $t$ in $\lambda$; its $\mathcal P$ measure is at most $1+t/4$, including the unit atom. Thus it costs $O(\ell^{-2})$ as well, with no growing-area loss. This proves the second bound of (8). The absolute all-$g$ comparison follows from the same $O(\ell^{-3})$ common difference on area $O((A_*+1)^2)$, and singly allowed strip of length at most $t$ in $g$ at fixed $\lambda,t$, area $O(A_*+1)$ and derivative bound $O(\ell^{-2})$. It gives $\|K_a-C_a/\ell\|_1\ll (A_*+1)/\ell^2=O(\ell^{-1})$; the simple profiles have uniform $L^1$ by the fixed-box envelope. In supremum, at fixed $g$ use (9) directly: $S(Z_j)$ integrated over $\lambda,t$ is bounded by its decaying envelope, and the derivative term costs $O((A_*+1)/\ell^2)$. This completes (8).

The fixed-box absolute scalar bounds are $|f(a,b)|<1/20$ and $|c_a|\le17/2041200$ for every $a,b\ge0$. By the second and first bounds in (8), the refined triangle scalar satisfies
$\mathfrak F_\ell=f(a,b)/\ell^2+O(\ell^{-3})$ uniformly. By the **one-sided** last bound, each uncurved factor in (1) is at least $(1/2-17/2041200-o(1))/\ell$, and hence their product exceeds the forbidden scalar by a fixed positive multiple of $\ell^{-2}$. This uses the refined comparator as a signed deterministic model. It does not charge a fixed-fraction simple nonlong comparison to the arithmetic error, and does not assign a sign to $V_f$ by itself.

## 4. Simultaneous arithmetic transfer with literal endpoints

At nominal root nodes keep the original $D_N,Q_N$ pair cuts. Use safe label cells in the interior of $D$ for $V_f$ and away from the $g=20$ seam for each nonlong trace, permitting $O(\delta)$ label collars because the actual displacements are $O(1/T)$. On any choice of accepted safe cell pairs, bound the absolute coefficient error by the sum of all individual cell product errors. Hölder and Parseval with (7) control this single target majorant negligibly relative to $X^{3/2}\ell^{-3}$; it is independent of the two root-prefix choices at each target. Safe root nodes are exact right-closed prefixes obeying the nominal integer root inequality, not averaged smooth cutoffs.

For $U$ the semiprime wing is the same on every safe nonlong prefix. Telescope each composite scalar before multiplying by the wing Fourier error. The whole composite prefix scalar is the negative integral of $K_a$ over the safe nonlong bins, hence $O(\ell^{-1})$ by (8). Its cross product with the one fixed error $B_{\rm wing}-H/(2\ell)$ costs $O(X^{3/2}\ell^{-3})$, uniformly by bounding the selected scalar pointwise and using the wing's $O(X^{3/4}\ell^{-2})$ fourth error. The composite cell errors against the whole wing are negligible under the summed bound (7), and the two-wing comparison has the same leading error scale by itself. In particular this step does not multiply a wing error by the unpaired $O(1)$ cell size.

The real collar costs $O(\delta/\ell^2)$ in the scalar by (8), and the [common rational completion](r80-source-local-mean-square-at-sign-transition.md), §3, replaces $[H^2]_N$ by $I_N$ in target norm with arbitrary fixed inverse-log error, uniformly multiplying only the common scalar bound. This yields the refined scalars of (1). In the **actual** label collars retain every literal integer term, using positive domination only on their total. There are $O(\delta^{-1})$ forbidden label-pair cells and a bounded number of nonlong seam bins against a whole positive mate. By (5) these cost respectively
$O(X^{3/2}(A_*+1)^2\delta)$ and $O(X^{3/2}(A_*+1)^3\delta)$, both at most $O(X^{3/2}\ell^{-3})$. Restore true units uniformly on the union of all floor choices: any shared prime divides $N$, is at least $e^{5T/4}$, and permits $O(X/p+1)$ first operands, with at most $O(\ell)$ candidate primes and fixed polylogarithmic label multiplicity. This is $O_D(XL^{-D})$ per target, also for wing overlap.

Finally for any selected actual floor choose its nominal lower root node. The intervening roots lie in one of $O((A_*+1)/\eta_0)$ fixed enlarged root slabs of width $O(\eta_0)$, including the actual normalized $O(1/T)$ shift and the two end slabs. Keep all other tests on that difference; dominate absolutely by the positive slab against a whole positive mate, using the exact composite nonlong identity first for $U$. Each has target norm $O(X^{3/2}(A_*+1)^3\eta_0)$ by (5). Summing squares to obtain the common maximum on each side costs $O(X^{3/2}(A_*+1)^{7/2}\eta_0^{1/2})\ll X^{3/2}\ell^{-7/2}$ in norm. Telescope the two sides with no other floor count. The refined comparator interpolates too: at fixed marked $(t,\lambda,j)$ the changed floor clips a $g$ interval of the same width; bounded $R_j=O(\ell^{-1})$ and $\|dS\|_{\rm TV}\le2$ give $\|K_a-K_{a'}\|_1\ll(A_*+1)|a-a'|/\ell$. By (8) the gap in the model has negligible norm at this mesh. These estimates prove (2) for every genuinely selected pair and all exact integer tests.

On the fixed physical interior $I_N\gg X$ for all even targets, while $\|I_N\|_2\ll X^{3/2}$. The strict refined margin and Chebyshev at a fixed multiple of $X/\ell^2$ on the one common maximum give the stated exceptional set and the negative scale, including at the exact selectable cube-root floor. The same comparisons give the sharp squared norm, with no inference beyond this particular signed containing row.
