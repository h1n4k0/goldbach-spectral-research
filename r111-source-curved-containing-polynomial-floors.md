# Polynomial adaptive root floors for the actual curved containing row

Keep the actual two-full Walsh containing-containing setting of the [paired-drift theorem](r110-source-curved-containing-paired-drift.md). The hard physical window $\mathcal J$, even target interval $\mathcal X$, $L=\log X$, $\ell=\log L$, $T=L/\ell$, and $T_N=\log N/\log\log N$ are unchanged. The actual operands $n=hF,m=kG\in\mathcal J$, $n+m=N$, are squarefree $N$-units, with their largest primes $F,G$. Each cofactor has the prescribed single old prime $s$ with $5T/4\le\log s\le7T/4$ and a squarefree residual product with all primes at least $e^{4T}$; the empty residual is the genuine semiprime wing. Keep the exact root floors $F\ge\sqrt N e^{-aT_N}$, $G\ge\sqrt N e^{-bT_N}$ and original integer $D_N,Q_N$ of that theorem. In particular $U$ is the uncurved product of the two actual long containing traces, with exterior minus, $V_f$ is the genuine forbidden retained-long correction with exterior plus, and $V_{\rm curv}=U+V_f$ is the actual curved containing-containing row. The two full signs $\mu(h)\mu(k)$ stay in all three definitions. No ordinary divisor row is included.

Use the **refined** real rejected-root profile $K_a(g)$ of (4)–(5) in the paired-drift theorem, and keep its actual $\ell$ dependence. Put

$$
 \begin{split}
  \mathfrak F_\ell(a,b)
   &=\iint_{D}K_a(g)K_b(g')\,dg\,dg',
       \qquad D=\{0\le g,g'\le20,\ g+g'\ge20\},\\
  \mathfrak U_\ell(a,b)
   &=\left(\frac1{2\ell}-\int_{20}^\infty K_a(g)\,dg\right)
     \left(\frac1{2\ell}-\int_{20}^\infty K_b(g')\,dg'\right),\\
  I_N&=\Sigma(N)B_{\mathcal J}(N).
 \end{split}                                                        \tag{1}
$$

**Theorem (unconditional).** For sufficiently large $X$, uniformly for $1\le A\le\ell/100$, the actual floors are allowed to be selected independently at each target and satisfy

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}\ \sup_{0\le a,b\le A}
   \bigl(
     |V_f(N;a,b)-I_N\mathfrak F_\ell(a,b)|^2+
     |U(N;a,b)+I_N\mathfrak U_\ell(a,b)|^2
   \bigr)\ll X^3\ell^{-6}.                                      \tag{2}
$$

The constant does not depend on $A$. There is an absolute fixed $c_0>0$, for instance $c_0=10^{-10}$ for sufficiently large $X$, for which $\mathfrak U_\ell-\mathfrak F_\ell\gg\ell^{-2}$ throughout $0\le a,b\le c_0\ell$. Consequently on each fixed interior target subwindow a **single** exceptional set of $O(X/\ell^2)$ even targets suffices for the genuine $V_{\rm curv}(N;a,b)\le-cX/\ell^2$ simultaneously for all $a,b$ in that box. Its squared norm has order $X^3\ell^{-4}$ for every such selection of floors. In particular the box includes the exact polynomial floor $N^{1/2-c_0/2}$ by taking $a=(c_0/2)\log\log N\le c_0\ell$ for large $X$; the endpoint $a=c_0\ell$ gives the floor $N^{1/2-c_0+o(1)}$. The sign is not asserted throughout the larger comparison box $\ell/100$, for another Walsh or divisor row, for a prescribed exceptional integer, for a growing physical window, the full pair sum, or Hypothesis S.

## 1. Arithmetic geometry and one-arm separation without a peeled high cutoff

On a composite cofactor its actual long containing trace is exactly the nonlong residue $\sum_{Fz\le D_N}\mu(h)\mu(z)\log(h/z)$, by the complete zero orbit for squarefree composite $h$. The genuine wing contributes its only nonzero long containing mark $+\log s$ and always has $F(D_N+1)>Q_N$. Hence it is independent of either selected floor and occurs only in $U$, by the [wing proof](r105-source-semiprime-wing-and-containing-contrast.md). Nothing below treats a wing as a composite residue.

Use the actual coordinates

$$
       u=(L/2-\log F)/T,\qquad g=(L/2-\log(Fz))/T ,
       \qquad u=g+\log z/T.                                    \tag{3}
$$

The exact root floor is $u\le a+O(1/T)$, uniformly on $a\le\ell/100$, since $T_N/T-1=O(1/L)$. The actual forbidden pair has labels below $\sqrt N$ and its three walls are at distance $O(1/T)$ from those of $D$, because $Q_N/(D_N+1)<\sqrt N$ and $\log D_N,\log Q_N$ differ from their fixed comparison logs by $O(1)$. The composite nonlong domain has $g\ge20+O(1/T)$ and $g\le a+O(1/T)$. Enclose these domains and both floor slivers by $g,u\ge-1$, $g\le\max(20,A)+2$, $u\le A+2$. On this actual enclosing support every label satisfies $\log z/T\le A+4$; root and cofactor logs are between $.48L$ and $.52L$ for large $X$. At most two separated near-square-root roots can occupy one physical integer, including multiplicity. The same is true in testing strict rejection $F<P(h)$, where there is exactly one such prime $P$ greater than $F$. Repeats have form $d_0F^2$ with $d_0\le e^{(2A+1)T}$ on nominal floors, yielding support $O(X^{.52+o(1)})$ and fourth norm $X^{.39+o(1)}$ by the usual coefficient energy and supremum bounds. The number of labels per cofactor is at most $2^{1+\log h/(4T)}=L^{O(1)}$ with an absolute exponent, without requiring fixed arity.

In the temporary separated-root arm there is an exact alternative to peeling a universal low block. Split the *actual* cofactor and label as

$$
     h=sW_1W_0,\qquad z=s^jW_1,\quad j\in\{0,1\},
          \qquad \mu(h)\mu(z)=-(-1)^j\mu(W_0).                   \tag{4}
$$

Here the rough parts are squarefree and coprime on the literal arm. This sign is for the **rooted** arm, not for the strict collision arm that also contains the other large prime $P$. Apply Siegel–Walfisz in $F$ at fixed integer cofactor and label on their actual hard intervals, as in the [growing box proof](r109-source-curved-containing-growing-adaptive-box.md). Every factor of $h$ exceeds the polylogarithmic denominator, so the same reduced multiplier $\mu(q)/\varphi(q)$ is exact. Prime length is polynomial, all endpoint errors are absolute inverse-log estimates after fixed $L$-powers, and the marks and coefficient bounds are uniform. Once in the real density at physical $x=hF$, let $t=\log s/T$ and $\lambda=\log W_1/T$. Then **exactly**

$$
         \frac{\log W_0}{L}
           =\frac12+\frac{\log x-L}{L}
                +\frac{g+(j-1)t}{\ell},\qquad
                 u=g+\lambda+jt.                              \tag{5}
$$

The normalized *unmarked* argument lies in $[.4,.6]$ on every active enclosing slice; it is independent of the size of the marked product. In particular it cannot meet the unmarked unit atom. The possible empty marked group is retained. A cofactor with both products empty cannot reach (5), so the literal composite condition introduces no continuum atom on these domains.

All reciprocal replacements in these actual products have arbitrary fixed inverse-$L$ accuracy, uniformly as in the growing box estimate: the individual prime reciprocal intervals start above $e^{5T/4}$, and the total reciprocal mass up to $X^{.7}$ in the two marked groups is $O(\log\ell)$. At fixed all other coordinates each hard log cut gives a real interval with a bounded-variation mark. Expand distinct ordered tuples with factorial denominators; one-coordinate replacement costs the generating sums $\sum k M^{k-1}/k!$ or their product for the two groups with $M=O(\log\ell)$. The true coprimality of $W_0,W_1$ is relaxed only in this real replacement: repeated coordinates anywhere in the two groups are bounded by the prime reciprocal-square tail times the same fixed generating moments. The old prime cannot be repeated across either group because of the disjoint bands. These estimates also justify comparisons on hard endpoints and do not require a derivative of the prime sums. No changed prime condition is imposed on the original integer arm.

Thus the unmarked rough density is the complete **signed** Dickman density with lower normalized endpoint $4/\ell$ and cap through $X^{.7}$, equal on (5) to $-\rho(v\ell/4-1)/v$ at $v=\log W_0/L$, by the [signed reciprocal identity](r98-source-tag-full-sign-stretched-cancellation.md), §3. This is smaller than every fixed inverse power of $\ell$ by factorial decay. There is **no far block estimate** and no high atom to discard: it is the specific label geometry (5) that forces the argument into the compact range, even when the marked product is of polynomial size. In the positive arm the same unmarked density is $O(\ell)$ off its unit atom, by the standard coordinate-marking identity. The positive marked reciprocal mass through $\lambda\le A+4$ is $O(A+1)$ by the positive exponential $\mathcal P([0,A+4])\ll A+1$ of the [fixed-box envelope](r107-source-curved-containing-fixed-box-sign.md). At fixed marked data the two exact bins in (3) intersect to clip the same $g$ variable. Via (5) a single $g$ bin or $u$ slab of width $d$ has normalized unmarked length $O(d/\ell)$, with endpoint movement $O(1/L)$ over the physical window. The real prime ratio $\log(h/z)/\log F$ is bounded and has physical derivative $O(1/(XL))$ at fixed cofactor and label. Holding common subintervals and then moving the endpoints gives positive physical supremum and variation $O((A+1)(d+1/T))$, and arbitrary inverse-$\ell$ in the signed separated arm. The latter estimate uses the actual signed density on the whole compact interval, including the endpoint moves. It remains true on a simultaneous joint cell.

Use the same auxiliary $H$ from the [first curved Fourier proof](r106-source-curved-containing-forbidden-collision.md): $H=(\mu(q)/\varphi(q))\widehat J(\beta)$ on the fixed polylogarithmic reduced majors, and zero otherwise. The real physical variation bounds give the fourth norms using the arc transform $\min(X,|\beta|^{-1})$ and the summable denominator fourth norm. The minor bound is uniform on the new powers: $h,F$ in a relevant dyad obey $h\asymp M,F\asymp K,MK\asymp X$ with $M,K\ge X^{.48}$; the three half-integer separations for $hF,Fz,F<P(h)$ have the same polynomial truncation and fixed log twists as before (skip the last one for the separated or positive arm). A root bin is a fixed prime interval. Coefficients are fixed $L$-powers, and with $P_{\rm arc}<q\le\lfloor X/P_{\rm arc}\rfloor$ the same bilinear reciprocal-distance bound gives arbitrary inverse-log fourth saving after enlarging the fixed denominator exponent $P_{\rm arc}=L^{C}$. Thus the whole-circle fourth estimates are, on inverse-$\ell$ bin widths in use,

$$
 \|A^+_{\rm slab}\|_4\ll X^{3/4}(A+1)(d+1/T),\qquad
 \|A^+_{\rm full}\|_4\ll X^{3/4}(A+1)^2,\qquad
 \|A^{\rm root}_{B,J}\|_4\ll_D X^{3/4}\ell^{-D} .               \tag{6}
$$

Here the last arm is full-signed and separated, and the positive arms dominate genuine canonical weights. No constant in (6) depends on the selectable $A$ in the stated range.

## 2. Refined joint cells and uniform scalar control

Use the disjoint right-closed root and label cells of the [adaptive cutoff proof](r108-source-curved-containing-adaptive-floors.md), with label mesh $\delta=\ell^{-6}$ split at $0,20$ and root mesh $\eta_0=\ell^{-14}$ split at $0,A$. On the modeled positive label bins $g>0$ we have $u\ge g$; equality and the true negative sliver will be dealt with at the literal collar. The total number of joint cells is $O(\ell^{22})$.

In strict rejection $F<P=P(h)$ factor $h=sW_1W_0P$ and $z=s^jW_1$, since the short label cannot contain $P\ge X^{.48}$. The sign is now $(-1)^j\mu(W_0)$, which differs from (4) by the extra prime. Put $u_j=g+\lambda+jt,\ Z_j=2g+\lambda+(2j-1)t,\ w=\log W_0/T$. At fixed $x$ the real collision wall is $w<Z_j+(\log x-L)/T$. After Siegel–Walfisz on $F$, reciprocal PNT in $P$ at fixed remaining data is on its actual clipped interval. Its scale is at least $X^{.48}$ on strict rejection, and the only denominator factor is the one already evaluated in $F$. The exact ratio after freezing just $x=X$ is
$R_j(w)=(1/2+g/\ell)/[\ell D_{p,j}(w)D_{f,j}]$, with
$D_{p,j}(w)=1/2+(g+(j-1)t-w)/\ell$, $D_{f,j}=1/2-u_j/\ell$.
At the new box scale these denominators and their common-interval interpolants are all in $[.4,.6]$ on the occupied caps. In particular every hard reciprocal replacement remains uniform. Freezing the wall and this physical mark has arbitrary inverse-$\ell$ cost after the grid: at each fixed low tuple the wall moves by $O(1/T)$ in $g$ and the mark has physical derivative $O(1/(X\ell L))$ on common regions, while the total positive low labeled reciprocal mass is $O((A+1)^2)$ by the two positive rough groups through log cutoff $(2A+1)T$. This freeze is only in the real density, not on any integer prime. The fixed cap still ensures $t+\lambda+w\le2u_j$, so extending the model measures locally to the half-line introduces no excess tail. The signed cumulative of $w$ is $S(w)=\rho_+(w/4)$ including its unit atom, and the marked measure is $\mathcal P(d\lambda)$. These are exactly the choices in the paired-drift $K_a$; an atom-boundary ambiguity is null after integrating $g$ for fixed other data.

If $J=(a_-,a_+]$, the canonical collision scalar in this joint cell is
$m^\natural_{B,J}=-\int_B(K_{a_+}-K_{a_-})\,dg$.
The negative subtracts the strict rejected root. In view of the uniform major/minor controls, negligible repeats and (6) on the separated arm,

$$
        \sum_{B,J}\|A_{B,J}-m^\natural_{B,J}H\|_4
                            \ll X^{3/4}\ell^{-20},\qquad
        \sum_{B,J}|m^\natural_{B,J}|\ll
                                   \ell^{-1}+(A+1)^2\ell^{-2}. \tag{7}
$$

Here $A_{B,J}$ is the actual canonical composite signed arm on the joint cell with only target-unit deletion suppressed. For the first bound take, for instance, $D>60$ in (6) before summing cells; all real physical freezes and discrete reciprocal errors are smaller. For the second use the leading $2S(Z_j)/\ell$ reciprocal measure and its integrable factorial envelope **separately** for the two placements: when summing over cells at fixed $(t,\lambda,j)$ the corresponding intervals in $g$ partition their domain. For the derivative correction use the Stieltjes equality
$\int_{[0,Z_j]} R_j\,dS=R_j(Z_j)S(Z_j)-\int_0^{Z_j}S(w)R'_j(w)\,dw$,
valid including the unit atom, on $Z_j\ge0$. The endpoint difference from the leading term is integrable at scale $\ell^{-2}$ (see below), and the derivative correction is $O(\ell^{-2})$ per $(g,\lambda,t,j)$ by $\int_0^\infty S<\infty$; the total positive marked area is $O((A+1)^2)$. This bound still permits an $O(1)$ absolute cell sum in the linear box; one cannot multiply that crude bound by the wing error when aiming at the sharp scale.

We give a quantitative version of the paired drift valid on $A\le\ell/100$:

$$
 \|\ell K_a-C_a\|_{L^1(g\ge0)}
       \le 10^6(A+1)/\ell,\qquad
       \|K_a\|_{L^1}+\|K_a\|_\infty\ll \ell^{-1}.               \tag{8}
$$

Indeed at $w=Z_j$ the two denominators coalesce,
$D_{p,j}(Z_j)=D_{f,j}$. In the above uniform range this gives
$|R_j(Z_j)-2/\ell|\le100(1+g+\lambda)/\ell^2$.
Also $|R'_j(w)|\le10/\ell^2$ and on the common $w$ interval
$|R'_1-R'_0|\le200/\ell^3$, using explicitly
$R'_j=(1/2+g/\ell)/(\ell^2 D_{p,j}^2D_{f,j})$ and the changes $\pm t/\ell$ in its denominators. Put $k=2g+\lambda$ and $h_*(k)=\rho(\max(0,(k-7/4)/4))$. The positive measure $\mathcal P$ has unit atom and density at most $1/4$ away from zero, and the elementary factorial Dickman envelope gives
$\int_0^\infty S(w)\,dw\le12$ and
$\int_0^\infty\int(1+k)h_*(k)\,d\mathcal P(\lambda)dg<2000$.
For the latter, use at most $\int_0^\infty(1+k)^2h_*(k)dk$ from the unit and density; beyond $k=7/4$ put $v=(k-7/4)/4$ and bound by $64\int_0^\infty(v+1)^2\rho(v)dv\le1920$ using $\rho(v)\le1/\lfloor v\rfloor!$. The bounded initial interval costs less than $14$.

For a chosen whole prefix $a$, both endpoint differences are therefore at most $400000\,\ell^{-2}$ after integration, allowing log old-prime mass less than one. If both placements fit, the common derivative error is at most $2400(A+1)^2/\ell^3$ and the unmatched interval (length at most $2t\le7/2$) costs at most $70000\,\ell^{-2}$ after integration by $h_*(k)$. When $Z_0<0$, the remaining $Z_1$ interval obeys that same length bound and has compact $(g,\lambda)$ support with $h_*=1$. If only the unshifted placement fits, the strip $u_0\le a<u_1$ has $g$ length at most $t$ for each marked $\lambda$, giving derivative error at most $210(A+1)/\ell^2$. All such bounds follow using $\int S\le12$ and $\mathcal P([0,A])\le A+1$. They imply the explicit first bound of (8), since $(A+1)/\ell\le .02$ for large $X$. The second follows in $L^1$ from this result and the absolute integrable simple envelope; in supremum use the endpoint decay in $\lambda$ and the pointwise derivative bound integrated over $\mathcal P([0,A])$, which costs only $O((A+1)/\ell^2)$. These deterministic estimates concern the **whole** prefix and do not assert paired smallness for individual arithmetic bin errors.

## 3. Why the sharp error survives the wing and target maximum

As in the adaptive cutoff proof, first use nominal root nodes and keep the exact $D_N,Q_N$ tests. Choose a common set of interior safe label pairs inside $D$ for the forbidden term, and safe nonlong bins away from $g=20$ for the composite trace. On any subset of accepted off-collar pair products the absolute coefficient error is bounded by summing all individual cell product errors. The common target norm is negligible for the composite-composite products by Hölder, Parseval and (7), even though the absolute scalar sum is only $O(1)$ here.

For products containing a wing in the uncurved term, use **a different grouping**. The whole off-collar nonlong composite prefix on one arm is $M_aH+E_a$, with $M_a$ its sum of refined cell scalars and with $\|E_a\|_4$ bounded by the summed errors in (7). The wing has the same Fourier polynomial on the entire prefix. After telescoping the root nodes the scalar $M_a$ is the negative $K_a$ integral over the safe nonlong bins, hence $|M_a|\ll\ell^{-1}$ by (8). Consequently the error from the wing against this scalar is bounded uniformly at every target by $\sup_a|M_a|$ times the absolute coefficient of the one fixed error product $H(B_{\rm wing}-H/(2\ell))$. Its target norm is $O(X^{3/2}\ell^{-3})$ by the actual wing fourth norm error. The wing against the remaining composite errors is negligible **uniformly**, by summing all corresponding cell errors before the supremum as in the previous paragraph. The two-wing product has the same stated comparison scale by itself. This argument never pays the raw cell absolute sum on a wing error, and uses the exact fact that a wing does not occur in the product-boundary cells of $V_f$.

After the two root prefixes telescope, use (8) to fill the omitted **real** label collars at scalar expense $O(\delta/\ell^2)$ and hence obtain (1). The [common rational completion](r80-source-local-mean-square-at-sign-transition.md), §3, for $[H^2]_N$ has arbitrary inverse-log target error, using reduced numerators first; multiplying by the bounded scalar at the selected floors requires no union over floor settings. The refined profile is retained in this comparison; its deterministic difference from $C_a/\ell$ is **not** charged to the arithmetic error at the linear box size.

In the actual label collars keep every strict and weak condition and dominate only their contributions by positive enclosing convolutions. The forbidden collar has $O(\delta^{-1})$ bins of pairs and costs $O(X^{3/2}(A+1)^2\delta)$; the nonlong seam has boundedly many bins against a whole positive mate and costs $O(X^{3/2}(A+1)^3\delta)$. These are at most $O(X^{3/2}\ell^{-3})$ by (6) and the chosen mesh. True units are restored on the union of all choices just as before: an offending shared prime divides $N$, is at least $e^{5T/4}$ and allows $O(X/p+1)$ first operands; coefficient multiplicities are fixed $L$-powers. This is a uniform $O_D(XL^{-D})$ per target, including the two-wing overlap.

Now replace each true selected root floor by the nominal lower node. Each difference sits in a fixed enlarged positive root slab of width $O(\eta_0)$, including the actual $O(1/T)$ displacement and the end slabs. Dominate absolutely against the whole positive mate using (6); for $U$ do this only after the exact nonlong-orbit identity. Each such slab costs $O(X^{3/2}(A+1)^3\eta_0)$ in target norm. Summing their squares over $O((A+1)/\eta_0)$ possibilities independently for each side, then telescoping the two sides, bounds the maximum by $O(X^{3/2}(A+1)^{7/2}\eta_0^{1/2})\ll X^{3/2}\ell^{-7/2}$. No other floor count multiplies this bound. The refined scalar itself interpolates: at fixed $(t,\lambda,j)$ a change of floor clips an interval of the same width in $g$, and the mark integral in (5) of the paired-drift definition is absolutely $O(\ell^{-1})$ by bounded $R_j$ and $\|dS\|_{\rm TV}\le2$. This gives $\|K_a-K_{a'}\|_1\ll(A+1)|a-a'|/\ell$ and hence negligible comparator gap at width $\eta_0$. All concluding target errors are controlled by common positive majorants at most $O(X^{3/2}\ell^{-3})$ in norm. This proves (2) for the original hard cuts and independent selected floors.

## 4. Sign of the retained refined comparator on a polynomial box

The fixed-box simple scalar satisfies
$(1/2-c_a)(1/2-c_b)-f(a,b)>.19$
by its explicit factorial bounds for all real $a,b\ge0$. Also $\|C_a\|_1<20$ uniformly: integrate its floor-independent bound by the change $z=g/2-7/16$, using $\int_0^\infty\rho(v)\,dv\le3$ and $\int_0^\infty v\rho(v)\,dv\le6$ from the factorial envelope. For $a,b\le A=c_0\ell$ the first bound of (8) is at most $\varepsilon_0=10^6(A+1)/\ell$. Thus replacing $\ell K_a,\ell K_b$ by $C_a,C_b$ in the normalized forbidden scalar costs at most $(40+\varepsilon_0)\varepsilon_0$, since $D$ is a subset of the product domain. On the two nonlong integrals the normalized full $U$ comparator changes at most $(2+\varepsilon_0)\varepsilon_0$, because $|c_a|,|c_b|<1/2$. With $c_0=10^{-10}$ one has $\varepsilon_0\le10^{-3}$ for large $X$, so the combined drift costs less than $.05$, leaving an absolute strict negative margin. This establishes the claimed sign of the **refined** deterministic model uniformly, not an analytical error at a fixed fraction of the model.

Finally $I_N\gg X$ for even $N$ on a fixed interior physical subwindow and $\|I_N\|_2\ll X^{3/2}$. Equation (2) and Chebyshev at a fixed multiple of $X/\ell^2$ give the one exceptional set and the uniform sign, and the same comparison gives the sharp squared norm for every choice in the smaller polynomial box. The argument outside it asserts the mean-square comparison (2) only.
