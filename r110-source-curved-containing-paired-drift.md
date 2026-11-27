# Paired collision drift and a near-linear adaptive curved-containing box

Use the exact hard physical window $\mathcal J$, even target interval $\mathcal X$, and notation $L=\log X$, $\ell=\log L$, $T=L/\ell$, $T_N=\log N/\log\log N$ of the [growing adaptive box](r109-source-curved-containing-growing-adaptive-box.md). Keep the same actual operands $n=hF,m=kG$ in $\mathcal J$, $n+m=N$, squarefree $N$-units, with largest primes $F=P^+(n),G=P^+(m)$. The cofactor on either side is $sV$ with one old prime $5T/4\le\log s\le7T/4$ and all primes of $V$ at least $e^{4T}$, allowing the wing $V=1$. Keep the literal root floors $F\ge\sqrt N e^{-aT_N},G\ge\sqrt N e^{-bT_N}$ and the original containing divisor tests with $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$, $Q_N=\lfloor Ne^{-20T_N}\rfloor$. Write $U$ for the uncurved completed product (exterior minus) and $V_f$ for the forbidden retained-long correction (exterior plus); $V_{\rm curv}=U+V_f$ is the actual curved containing-containing row. All employ the two-full Walsh weight $\mu(h)\mu(k)$; no ordinary row is included. As in the [fixed-box sign result](r107-source-curved-containing-fixed-box-sign.md), use $I_N=\Sigma(N)B_{\mathcal J}(N)$ and the same real functions $C_a(g),c_a,f(a,b)$.

**Theorem (unconditional).** For sufficiently large $X$, put $A_{\max}=\ell/(10^7\log\ell)$. Uniformly for $1\le A\le A_{\max}$, the floor parameters can be selected independently at each target, with

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}\sup_{0\le a,b\le A}
 \left(
  \left|V_f(N;a,b)-\ell^{-2} I_N f(a,b)\right|^2+
  \left|U(N;a,b)+\ell^{-2} I_N(1/2-c_a)(1/2-c_b)\right|^2
 \right)
 \ll X^3(A+1)^2\ell^{-6}.                                      \tag{1}
$$

The constant is independent of $A$. Thus one even exceptional set of size $O(X(A+1)^2/\ell^2)$ in any fixed interior target subwindow suffices for $V_{\rm curv}\le-cX/\ell^2$ simultaneously for all $a,b$ in the box, where $c>0$ depends on the fixed physical interior. This saves density throughout the stated box, including $A=A_{\max}$, and the squared norm for any target-selected pair has sharp order $X^3\ell^{-4}$. It does not address a box of order $\ell$, a growing physical window, any other signed row, the full original pair sum, or Hypothesis S.

The improvement over flattening the mark in the previous joint-cell estimate is an order of operations: first compare the actual signed cell to a scalar with the prime mark **not flattened**, then sum the two old-prime placements only after the chosen root prefix is put back together. The second cancellation is deterministic and occurs between real measures, not between assumed independent arithmetic errors.

## 1. Exact cuts and uniform Fourier controls at the new scale

On a composite cofactor, its exact long trace is the nonlong residue
$\sum_{Fz\le D_N}\mu(h)\mu(z)\log(h/z)$, since $\Lambda(h)=0$ for squarefree composite $h$. In the [actual wing](r105-source-semiprime-wing-and-containing-contrast.md) the only nonzero mark in that trace is $+\log s$ at its largest prime. This root exceeds $\sqrt N$ and $F(D_N+1)>Q_N$; the wing is therefore independent of either floor, occurs only in $U$, and has its original scalar model $H/(2\ell)$ with fourth norm error $O(X^{3/4}\ell^{-2})$.

For each composite arm put $u=(L/2-\log F)/T$ and $g=(L/2-\log(Fz))/T=u-\log z/T$. The actual root condition is $u\le a+O(1/T)$, using $T_N/T-1=O(1/L)$ and $A=o(\ell)$. Both long labels of every forbidden pair are below $\sqrt N$ since $Q_N/(D_N+1)<\sqrt N$. Thus the forbidden region is the same triangle $0\le g,g'\le20,\ g+g'\ge20$ up to the existing $O(1/T)$ boundary displacement, while composite residue labels satisfy $20+O(1/T)\le g\le a+O(1/T)$. As before use an enclosing coordinate interval from $-1$ to $\max(20,A)+2$, root range from $-1$ to $A+2$, and retain literal sliver terms. The true and comparison labels obey $\log z/T\le A+4$ wherever a root floor and this enclosing label interval are used. Roots and cofactors have logs $L/2+O((A+1)T)$, so three such near-square-root factors (counting multiplicities) cannot occur in one physical integer, even at the new size $A$. Label multiplicities are still $L^{O(1)}$ absolutely, since $\omega(h)\le1+\log h/(4T)$. All these assertions are for the actual labels, not logs assigned to an independent model.

Here are the uniform versions of the growing-box Fourier inputs. Use the same auxiliary arc denominator cap $P_{\rm arc}=L^{C_0}$ with a sufficiently large fixed exponent, and the same common transform $H=(\mu(q)/\varphi(q))\widehat J(\beta)$ on the reduced auxiliary majors $c/q+\beta$, zero elsewhere. On the present ranges all cofactor primes exceed $P_{\rm arc}$. The Siegel–Walfisz step in the prime $F$, at fixed cofactor and short label, and the reciprocal PNT in the other large prime on the rejected arm, work with $X^{1/2+O(1/\log\ell)}$ prime variables and with arbitrary inverse-log errors uniform on the hard endpoints. Their number of dyads, logarithmic marks, and reciprocal sums over cofactors and labels still cost only fixed powers of $L$. For minors the three half-integer separations of $hF$, $Fz$, and $F<P(h)$ are those in the [first curved collision proof](r106-source-curved-containing-forbidden-collision.md), with a root interval imposed separately in $F$. At real part $1/L$ the twists have bounded modulus; the coefficient bounds are fixed $L$-powers; the trivial coefficient energy is $O(XL^{O(1)})$. The same balanced Cauchy reciprocal-distance estimate as in the growing-box proof has squared relative bound
$L^{O(1)}(q^{-1}+K^{-1}+\log(2q)/M+q\log(2q)/X)$
on dyads $h\asymp M,F\asymp K, MK\asymp X$. With $P_{\rm arc}<q\le\lfloor X/P_{\rm arc}\rfloor$ and $M,K=X^{1/2+O(1/\log\ell)}$, this gives arbitrary inverse logs in the minor fourth estimates by first increasing the fixed auxiliary exponent. Half-integer gaps and truncation at $X^4$ are adequate with these same powers and enclosing ranges. A repeat is still disjoint from strict rejection and has form $d_0F^2$ with $d_0\le\exp((2A+1)T)$ on nominal floors, hence support $X^{1/2+o(1)}$ and fourth norm $X^{3/8+o(1)}$. These uniform power estimates do not require fixed arity.

For the rooted density argument, peel through $\log p=100(A+1)T$, a range containing all possible short-label factors besides $s$, and use exact disjoint low and high intervals. The labeled low positive reciprocal product is $O((A+1)^2)$, from factors $1+2/p$. Its exponential tilt at $1/[100(A+1)T]$ increases this bound by a bounded factor: apply $e^v-1=O(v)$ on $[0,1]$ and $\sum_{p\le y}(\log p)/p\ll\log y$. The weight at low displacement $\log d_{\rm low}>L/20$ is consequently

$$
        O\!\left((A+1)^2\exp\!\left[-\frac{\ell}{2000(A+1)}\right]\right)
                                                   \ll \ell^{-2498}. \tag{2}
$$

Indeed $A+1\le2A$ and $\ell/A\ge10^7\log\ell$. This fixed power is more than sufficient for all grids below. In particular it also bounds the possible high empty-product atom, whose support at fixed low tuple and label is an intersection of hard intervals in the physical variable, with bounded variation and mark. Below the displaced threshold the atom cannot reach the near-square-root cofactor.

The uniform expanding-arity tuple replacement in the growing-box proof applies here without an $A$-dependent constant. In fact the total prime reciprocal mass up through $X^{.7}$, counting low label occupations, is still $O(\log\ell)$, since the smallest available prime is at least $e^{5T/4}$. At fixed other coordinates each hard log cut gives an interval in a remaining coordinate and the mark has bounded or fixed-polylog variation on that interval. Telescoping the coordinate replacements costs exponential generating sums $\sum j M^{j-1}/j!$ with $M=O(\log\ell)$ (one such factor for each marked group), and distinctness errors are bounded by the reciprocal square tail with the same fixed arity moments. Ordinary reciprocal PNT on intervals therefore has arbitrary inverse-$L$ precision after all tuple losses. Use supremum in the physical coordinate for these discrete replacement errors, not a derivative of the discrete sums.

The residual positive log density off its atom is $O(\ell/(A+1))$, from the coordinate-marking bound at high normalized lower endpoint $\xi=100(A+1)/\ell$. The signed high density on $[.4,.6]$ is $-\rho(v/\xi-1)/v$, and has arbitrary inverse-$\ell$ decay because $\ell/[100(A+1)]\gg\log\ell$ and the Dickman bound there is factorial. The undisplaced low products fall in this compact high range since $\log h=L/2+o(L)$. At fixed low data and label, the cap in normalized $\log h/L$ cut by a $g$ bin or a $u$ slab of width $d$ has width $O(d/\ell)$, moves by $O(1/L)$ across the actual physical window, and has the same bounded bare ratio with $O(1/(XL))$ physical derivative. This gives the uniform positive fourth norm

$$
          O\!\left(X^{3/4}(A+1)(d+1/T)\right),                    \tag{3}
$$

at all inverse-$\ell$ widths below; the full enclosing positive mate has fourth norm $O(X^{3/4}(A+1)^2)$. The separated signed arm on a joint cell has fourth norm $O(X^{3/4}\ell^{-100})$ by the compact density and (2), also for simultaneous root and label clipping (the intervals translate together at fixed label). The positive and signed suprema and variations follow by the same clip measure and mark bounds even when a low-tail atom occurs, using (2). This supplies the required uniform extension of both rooted estimates rather than importing their former numerical box restriction.

## 2. Refined scalar on an actual joint cell

Use label mesh $\delta=\ell^{-6}$, with $0,20$ among its nodes, and root mesh $\eta_0=\ell^{-14}$, with $0,A$ among its right-closed nodes. On the modeled region $g>0$ the root necessarily satisfies $u\ge g>0$, so no initial root interval is missing. Actual lower-label slivers and $g=0$ belong to the collars. Choose comparable mesh widths in each subinterval cut by designated endpoints and pad the enclosing positive windows as above. This gives $O((A+1)^2/(\delta\eta_0))=O(\ell^{22})$ joint cells, with exact half-open integer predicates as in the [adaptive cell proof](r108-source-curved-containing-adaptive-floors.md).

For strict rejected root $F<P=P(h)$ retain the exact factorization $h=sW_1W_0P$, $z=s^jW_1$, $j=0,1$, with signed mark factor $(-1)^j\mu(W_0)$. As before write $t=\log s/T,\lambda=\log W_1/T,w=\log W_0/T$ and put

$$
 \begin{split}
 u_j&=g+\lambda+jt,\qquad Z_j=2g+\lambda+(2j-1)t,\\
 D_{p,j}(w)&=\tfrac12+(g+(j-1)t-w)/\ell,\qquad
 D_{f,j}=\tfrac12-(g+\lambda+jt)/\ell,\\
 R_j(w)&=\frac{\tfrac12+g/\ell}{\ell\,D_{p,j}(w)D_{f,j}} .
 \end{split}                                                     \tag{4}
$$

On an active cap, these denominators are comparable to one uniformly. The expression $R_j$ is the exact real ratio of the growing-box proof (6) at $x=X$. It is **not** replaced by $2/\ell$ in any arithmetic cell. Let $S(w)=\rho_+(w/4)$ be the right-continuous signed Dickman cumulative including its unit atom at zero and equal to zero below zero, and let $\mathcal P$ be the positive reciprocal exponential of the fixed-box theorem. Define the refined rejected-root profile for $g\ge0$ by

$$
 K_a(g)=\int_{5/4}^{7/4}\frac{dt}{t}\int d\mathcal P(\lambda)
       \sum_{j=0}^1(-1)^j\,{\bf1}_{u_j\le a}
                 \int_{[0,Z_j]} R_j(w)\,dS(w) ,                   \tag{5}
$$

with the inner integral zero for $Z_j<0$. Each term need only evaluate (4) on its active interval. This profile vanishes for $g>a$. Replacing $R_j$ by $2/\ell$ gives exactly $C_a(g)/\ell$.

Indeed on the auxiliary majors first use the true hard prime intervals in $F$ and then ordinary reciprocal PNT in $P$ at fixed physical $x$ and remaining factors, as in the growing-box proof. Only now freeze the real threshold $w<Z_j+(\log x-L)/T$ at $Z_j$, and the smooth prime ratio at $x=X$. At fixed actual low data this lower-log wall moves in $g$ by total length $O(1/T)$, while the ratio is $O(\ell^{-1})$ and has physical derivative $O(1/(X\ell L))$ on the active range. Therefore the change, including physical supremum and variation, is bounded in each cell by
$O((A+1)^2[(T\ell)^{-1}+(A+1)/(\ell L)])$ after using the total positive labeled reciprocal mass. This is smaller than any fixed inverse-$\ell$ power even after the whole grid. No integer prime test is frozen in this step. The subsequent uniform tuple replacement of Section 1 can use the **exact** frozen ratios because the mark is smooth in each occupied log variable with uniform variation and every other cut is affine. On a nonempty frozen cap $t+\lambda+w\le2u_j\le2A$, so both exponentials in (5) can be taken locally finite on the full half-line without adding any contribution. The discrete tight endpoint is included before reciprocal replacement. The strict or weak convention at the zero atom of $S$ in the final model occupies only a null set of $g$ at fixed other data.

For a cell $(B,J)$ with root interval $J=(a_-,a_+]$, use the **canonical** scalar $m^\natural_{B,J}=-\int_B(K_{a_+}-K_{a_-})\,dg$ (the negative is the subtraction of the rejected root). By the above real density bound, the fourth arc integral, and the separated signed/repeat estimates,

$$
 \sum_{B,J}\|A_{B,J}-m^\natural_{B,J}H\|_4
                                          \ll X^{3/4}\ell^{-20}.
                                                                    \tag{6}
$$

Here $A_{B,J}$ is the actual canonical signed composite bin polynomial with only the target-unit mask suppressed. The displayed power follows, for example, from the separated estimate $\ell^{-100}$ per cell and the other arbitrary inverse-log errors. The scalar size budget needed for product errors is

$$
                   \sum_{B,J}|m^\natural_{B,J}|
                              \ll \ell^{-1}+(A+1)^2\ell^{-2}.    \tag{7}
$$

To see (7), first use the integrable, floor-independent envelope of the fixed-box theorem on the two nonnegative leading summands **separately**, and partition in $u_j$. For the correction integrate by parts as in the growing-box proof: on $Z_j\ge0$ the difference of the integral in (5) from $(2/\ell)S(Z_j)$ is
$S(Z_j)(R_j(Z_j)-2/\ell)-\int_0^{Z_j} S(w)R'_j(w)\,dw$.
The first term is bounded by $(1+g+\lambda)S(Z_j)O(\ell^{-2})$, and the second by $O(\ell^{-2})$, using $R'_j=O(\ell^{-2})$ and the integrability of $S$. Summing across cells uses disjoint $g$ intervals at each fixed $(\lambda,t,j)$ and total positive area $O((A+1)^2)$. This gives (7). It does not yet use cancellation between the placements. The bound retains its explicit size because the independent wing error is of order $X^{3/4}\ell^{-2}$ rather than (6).

## 3. Cancel the two smooth drifts only after the prefix

The refined profile satisfies the key deterministic estimate

$$
       \int_0^\infty |K_a(g)-C_a(g)/\ell|\,dg
                          \ll (A+1)\ell^{-2},
               \qquad 0\le a\le A.                              \tag{8}
$$

At a fixed $g,\lambda,t$, use the integration by parts of Section 2 for each allowed placement. All endpoint contributions
$S(Z_j)(R_j(Z_j)-2/\ell)$ integrate absolutely to $O(\ell^{-2})$ over $g,\lambda,t$, because $\mathcal P$ consists of its unit atom and a density bounded by $1/4$, and factorial decay of $S(Z_j)$ dominates $(1+g+\lambda)$ and the volume of $2g+\lambda$ level strips. Values with $Z_j<0$ do not contribute. For the derivative term one has exactly

$$
 R'_j(w)=\frac{\tfrac12+g/\ell}
                   {\ell^2D_{p,j}(w)^2D_{f,j}} .
$$

On the common $w$ range for two permitted placements, $D_{p,1}-D_{p,0}=t/\ell$ and $D_{f,1}-D_{f,0}=-t/\ell$. All endpoints and interpolated denominators there are uniformly bounded away from zero by (4); hence $|R'_1-R'_0|\ll\ell^{-3}$. Integrating $S(w)$ first bounds the common derivative difference by $O(\ell^{-3})$ at each $g,\lambda,t$. Its total contribution is $O((A+1)^2/\ell^3)$, using the total $g$ range and $\mathcal P([0,A])\ll A+1$. The unmatched derivative interval has length at most $2t$, as $Z_1-Z_0=2t$. It is bounded by $O(\ell^{-2})S(\max(0,Z_0))$, integrable absolutely in $g,\lambda,t$; when $Z_0<0$ the region $2g+\lambda<t$ is compact, and the same bound covers the full remaining interval. This also handles a zero endpoint without presuming a derivative for the atom.

The only case with just one allowed root placement is $u_0\le a<u_1$. At fixed $\lambda,t$ it gives an interval of length at most $t$ in $g$; after integrating $\lambda$ its weighted area is $O(A+1)$. On it the derivative term is $O(\ell^{-2})$ by $\int S<\infty$. Adding these estimates proves (8), since $A+1=O(\ell)$. This cancellation is valid for each whole selected prefix **after** its cells telescope; independent arithmetic cells themselves need not have matched signs or small flattened errors.

For use at real collars, also $\sup_{g\ge0}|K_a(g)|\ll\ell^{-1}$. Apply integration by parts directly to (5). At fixed $g$, the integral in $\lambda,t$ of each $S(Z_j)$ is bounded by its decaying $\lambda$ envelope and the unit plus bounded density of $\mathcal P$, while the derivative part contributes $O((A+1)\ell^{-2})$. Use (8) and the uniform fixed-box envelope to get $\int_0^\infty|K_a(g)|\,dg\ll\ell^{-1}$ as well. Since (8) is an actual $L^1$ estimate on a profile, it bounds the triangle-product replacement (a subset of the full product) and the two nonlong integrals without a new loss from the positions of the labels.

## 4. Signed maximal transfer and exact exception geometry

As in the adaptive proof, at nominal root nodes keep the true divisor tests away from a fixed $O(\delta)$ label collar, and use the exact right-closed root prefixes. A subset of accepted products at any target is bounded in error by summing the absolute coefficients of **all** individual cell product errors; Hölder and Parseval apply to this one common majorant. On composite-composite, (6) and (7) give negligible total target norm. In $U$ add the actual wing always present in each prefix. Its fourth error costs at most

$$
  O\!\left(X^{3/2}\ell^{-2}
                      [\ell^{-1}+(A+1)^2\ell^{-2}]\right)
          \ll X^{3/2}(A+1)\ell^{-3}                               \tag{9}
$$

against the summed scalar budgets (and both wing errors give only $X^{3/2}\ell^{-4}$). This checks the wing at the claimed scale even when the absolute cell budgets in (7) exceed $1/\ell$. The common reduced-numerator and arc-tail [rational completion](r80-source-local-mean-square-at-sign-transition.md), §3, replaces $[H^2]_N$ by $I_N$ in target norm with arbitrary fixed inverse-log saving, incurring only the common scalar bound from (7). There is no union over node pairs in this step.

For off-collar products, telescoping gives the refined profiles $-K_a,-K_b$ on the two canonical composite legs. The forbidden sign is exterior plus, and the uncurved sign exterior minus with each wing contributing $1/(2\ell)$ to its own composite long trace. The real collar costs $O(\delta/\ell^2)$ from the above uniform supremum and integral bounds. Thus the refined scalars are $\int_D K_a(g)K_b(g')\,dg\,dg'$ and
$-(1/(2\ell)-\int_{20}^\infty K_a)(1/(2\ell)-\int_{20}^\infty K_b)$,
where $D$ is the same fixed comparison triangle. The deterministic estimate (8) replaces them by the two claimed fixed-box scalars with error $O((A+1)\ell^{-3})$, because the other factors have $L^1$ norm or size $O(\ell^{-1})$. Multiplying by $I_N$ uses its uniform $O(X^{3/2})$ target norm, so this replacement is uniform under independent target choices.

The actual forbidden collar has $O(\delta^{-1})$ label-only cells and the nonlong seam boundedly many g-bins; keep every strict and weak product/divisor condition in them, then use the positive common enclosing arms of (3) for domination. Their respective target norm costs are $O(X^{3/2}(A+1)^2\delta)$ and $O(X^{3/2}(A+1)^3\delta)$ below (9). Suppressed target-unit contributions are negligible on the union of choices: any shared prime divides $N$, exceeds or equals $e^{5T/4}$, and allows only $O(X/p+1)$ first operands. There are $O(\ell)$ of these primes for a target, and the coefficient multiplicities are fixed $L$-powers from Section 1. This gives $O_D(XL^{-D})$ per target, including wing overlap. Neither removal counts an approximate integer test as the true one.

At an arbitrary actual floor choose its lower root node and absorb both its mesh gap and its real $O(1/T)$ target displacement in an enlarged fixed root slab of width $O(\eta_0)$. There are $O((A+1)/\eta_0)$ such slabs on each side including the end slabs. A positive root slab against the global positive mate has norm $O(X^{3/2}(A+1)^3\eta_0)$ by (3). Sum squares to dominate their maximum, yielding $O(X^{3/2}(A+1)^{7/2}\eta_0^{1/2})$ in target norm. Telescope the two changes independently, applying the exact nonlong identity before taking a positive bound for $U$; the other floor is never counted as an additional choice factor. These bounds are smaller than (9) at the indicated widths. For the comparator interpolation use the **simple** $C_a$, after its deterministic comparison at the nodes: at each marked $(\lambda,t,j)$ a changed root floor clips a $g$ interval of the same width, so the change in $C_a$ in $L^1$ is $O((A+1)\eta_0)$, using $\mathcal P([0,A+1])\ll A+1$. This gives negligible change after multiplying the model by $I_N/\ell^2$. Every selected true floor in the continuum is now covered, with its original inequalities.

Together these common norm bounds prove (1). The fixed-box determinant margin is an absolute lower bound for $(1/2-c_a)(1/2-c_b)-f(a,b)$ for every real $a,b\ge0$ by its global real envelope. On the fixed physical interior, $I_N\gg X$ for even $N$. Chebyshev at scale $X/\ell^2$ on (1) gives the common exceptional count and the sharp squared norm; the count is $o(X)$ since $A/\ell\le 1/(10^7\log\ell)$. No sign is inferred for a named exceptional target or for a different Walsh or divisor row.
