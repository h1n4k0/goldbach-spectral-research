# One curved containing exceptional set for growing adaptive floor boxes

Keep the [adaptive curved-containing setting](r108-source-curved-containing-adaptive-floors.md) and its exact definitions. Thus the hard physical window $\mathcal J$, even targets $\mathcal X$, $L=\log X$, $\ell=\log L$, $T=L/\ell$, and $T_N=\log N/\log\log N$ are unchanged. Both operands $n=hF,m=kG\in\mathcal J$ are genuine squarefree $N$-units, $n+m=N$, and $F=P^+(n),G=P^+(m)$. The cofactor on either side is $sV$ with exactly one old prime $5T/4\le\log s\le7T/4$ and all primes of $V$ at least $e^{4T}$; the wing $V=1$ is allowed. The actual floors are $F\ge\sqrt N e^{-aT_N}$, $G\ge\sqrt N e^{-bT_N}$. Keep $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$ and $Q_N=\lfloor Ne^{-20T_N}\rfloor$ with the original strict and weak tests.

As before, $V_f$ is the containing-containing forbidden retained-long correction with exterior plus, $U$ is the uncurved product of the two actual long containing traces with exterior minus, and $V_{\rm curv}=U+V_f$ is the actual curved containing-containing row; all three have the two-full Walsh weight $\mu(h)\mu(k)$. There are no ordinary divisor arms. Retain the real functions $C_a(g),c_a,f(a,b)$ and $I_N=\Sigma(N)B_{\mathcal J}(N)$ of the [fixed-floor sign calculation](r107-source-curved-containing-fixed-box-sign.md).

**Theorem (unconditional).** For $1\le A\le\sqrt\ell$, uniformly in both $A$ and the independently target-selected parameters $a,b\in[0,A]$,

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}\sup_{0\le a,b\le A}
 \left(
    \left|V_f(N;a,b)-\frac{I_N}{\ell^2}f(a,b)\right|^2+
    \left|U(N;a,b)+\frac{I_N}{\ell^2}(1/2-c_a)(1/2-c_b)\right|^2
 \right)
       \ll X^3(A+1)^4\ell^{-6}.                                  \tag{1}
$$

The constant is independent of the box size $A$. On any fixed interior target subwindow one common exceptional set of size $O(X(A+1)^4/\ell^2)$ suffices for $V_{\rm curv}(N;a,b)\le-cX/\ell^2$ simultaneously for all choices in the box. This yields a density-one conclusion if $A=o(\sqrt\ell)$; at $A=\sqrt\ell$ the stated exceptional estimate alone need not save a density. In particular, for any fixed $0<\epsilon<1/2$, the growing box $A=\ell^{1/2-\epsilon}$ has common exception size $O_\epsilon(X\ell^{-4\epsilon})$, and the squared norm is of order $X^3\ell^{-4}$ for any choice of floors in this range. The physical window has not grown. This is not a sign for a prescribed exceptional target, any remaining signed row, the full original sum, or Hypothesis S.

## 1. Uniform hard geometry and arithmetic Fourier inputs

The exact complement and wing identities of the [wing calculation](r105-source-semiprime-wing-and-containing-contrast.md) hold without assuming a fixed $A$. On a composite cofactor, the signed long containing trace is exactly the nonlong residue $\sum_{Fz\le D_N}\mu(h)\mu(z)\log(h/z)$ because $\Lambda(h)=0$. A wing has only the nonzero long signed mark $+\log s$ at $F>\sqrt N$, and $F(D_N+1)>Q_N$ for all the present floors. Thus $V_f$ involves composite-composite only, and the actual wing in $U$ is independent of the floor, with exactly its previous one-arm model.

On the composite arm use the literal coordinates $u=(L/2-\log F)/T$, $g=(L/2-\log(Fz))/T$, so $g=u-\log z/T$. Over the target dyad, the actual root floor is

$$
 u\le a+(L-\log N)/(2T)+a(T_N/T-1)=a+O(1/T)
$$

uniformly for $a\le\sqrt\ell$, since $T_N/T-1=O(1/L)$. An analogous relation holds on the right. Both labels in a forbidden pair are below $\sqrt N$ by $Q_N/(D_N+1)<\sqrt N$; the two label long inequalities and product inequality are within $O(1/T)$ of the fixed triangle $0\le g,g'\le20,\ g+g'\ge20$. The exact composite nonlong residue uses $g\ge20+O(1/T)$ and $g\le a+O(1/T)$. Accordingly a single enclosing pair of $g,u$ windows of width $O(A+1)$ covers all actual terms and comparison slivers. For example on the lower end one may allow $g,u\ge-1$, and on the upper end use $\max(20,A)+2$. Throughout the active enclosing range the cofactor and root satisfy $\log h,\log F=L/2+O((A+1)T)$, and the eligible labels have $\log z=O((A+1)T)$. All constants in these assertions are absolute for the given fixed physical window. No capped number of prime factors of a label is necessary.

In fact there are at most two possible separated root choices at a physical integer, since three such near-square-root factors (with multiplicity) would exceed the window. Also $\omega(h)\le 1+(\log h)/(4T)=O(\ell)$ absolutely, so all label multiplicities and log weights together give $L^{O(1)}$ with fixed exponents. In strict rejection $F<P(h)$ there is only one cofactor prime $P=P(h)$ above $F$, and $h=sWP$ with $\log(sW)\le (2A+1)T$ on fixed floors by $sW<x/F^2$ at $x=hF$. Repeats $F\mid h$ are disjoint and have physical integer $d_0F^2$ with $d_0\le e^{(2A+1)T}$. Even counting every label, their support is $X^{1/2+O(1/\sqrt\ell)}$ and the coefficient size is bounded by a fixed power of $L$. Their fourth norm, by interpolation with Parseval, is $X^{3/8+O(1/\sqrt\ell)}$ times a fixed power of $L$, negligible even over a polynomial number of cells in $\ell$.

Use the common auxiliary major/minor arcs and model $H$ of the [first curved collision calculation](r106-source-curved-containing-forbidden-collision.md), with fixed sufficiently large exponent in its denominator cutoff $P_{\rm arc}=L^{C_0}$. We explain why the Fourier inputs remain uniform. Applying Siegel–Walfisz in $F$ at fixed $h,z$ gives an arbitrary inverse-log major error: the prime is in $X^{1/2+O(1/\sqrt\ell)}$, every prime factor of $h$ is larger than $P_{\rm arc}$, all endpoints are hard, the phase variation costs a fixed power of $L$, and the sum of $h^{-1}$ with its label multiplicity is at most a fixed $L$-power. The reduced numerator factor is exactly $\mu(q)/\varphi(q)$. In strict rejection the remaining reciprocal prime count in $P$ at fixed $x$ and low data is likewise uniform on hard intervals, with logarithm comparable to $L$. On the minors use the same half-integer separations of $hF\in\mathcal J$, the integer $Fz$ label interval, and $F<P(h)$, the last at $P(h)-1/2$. A root interval is separately just an interval in $F$. Dividing into dyads on $h\asymp M,F\asymp K$, $MK\asymp X$, only adds powers of $L$. After the Perron twists of bounded modulus (on the line $\Re s=1/L$), the coefficients are $L^{O(1)}$ as above. The usual reciprocal-distance squared relative estimate is

$$
 L^{O(1)}\biggl(q^{-1}+K^{-1}+
        \frac{\log(2q)}M+\frac{q\log(2q)}X\biggr),
 \qquad P_{\rm arc}<q\le\lfloor X/P_{\rm arc}\rfloor .
$$

It gives arbitrary inverse-log supremum relative to $X$, since $M,K=X^{1/2+O(1/\sqrt\ell)}$. Half-integer Perron truncation at $X^4$ is uniform because the products and separating endpoints are $O(X^{1+o(1)})$, and the total integrated overhead is a fixed power of $L$; no new coupled inequality was introduced. Parseval and the coefficient bound give energy $O(XL^{O(1)})$. Thus all such minor fourth errors are arbitrary inverse logs, uniformly even for small comparison grid cells. Rooted and positive arms simply omit the strict-rejection Perron cutoff. Hereafter arbitrary inverse powers of $L$ can be chosen small enough to cover all polynomially many cells and all polynomial factors in $A$ below.

## 2. Uniform rooted positive and signed estimates

Choose a fixed sufficiently large $K_0$ and peel the low prime block through $\log p=K_0(A+1)T$, containing all label factors besides the old $s$. Partition at its exact endpoint, with the high block running up to $p\le X^{.7}$, which excludes no active cofactor factor. For each low prime the two label occupations are absent or present **in** or **out of** the label; the positive product over low primes has factors at most $1+2/p$. Its total reciprocal weight, also with the old-prime choices, is $O((A+1)^2)$ by the prime reciprocal harmonic bound. The same bound holds after multiplying each low product's weight by the exponential of its log displacement divided by $K_0(A+1)T$: use $e^{v}-1=O(v)$ for $0\le v\le1$ and $\sum_{p\le y}(\log p)/p\ll\log y$ in its Euler product. Thus the weight of low products of displacement above $.05L$ is

$$
             O((A+1)^2 e^{-c\ell/(A+1)}).
                                                                    \tag{2}
$$

This is smaller than every fixed inverse power of $\ell$ on $A\le\sqrt\ell$. In particular the possible high empty-product atom at such a low tuple has negligible physical supremum and variation: at each fixed tuple its coefficient is bounded and its hard physical support is an intersection of intervals. With low displacement below $.05L$ the high empty product cannot reach an active cofactor.

For precision about the expanding arities, every discrete-to-real reciprocal replacement here uses ordinary reciprocal prime number theorem on intervals, uniformly with error $O_D(L^{-D})$ for any fixed $D$ when all primes exceed $e^{5T/4}$. At fixed other factors the conditions on the one remaining log coordinate are intersections of affine half-lines and hard intervals, with a bounded-variation mark of uniform or polynomial-log size. Expand into ordered tuples with factorial denominators and telescope one coordinate at a time. The total positive prime reciprocal mass in all ranges is $O(\log\ell)$, including a fixed occupation factor of at most two. The arity factor in this telescoping sum is controlled by $\sum_{j\ge1} j M^{j-1}/j!=e^M$ and, with two distinct labels, by the corresponding product of two such exponential sums, where $M=O(\log\ell)$ is enlarged to include both the discrete and continuous masses. The repeated-coordinate upper bound uses the same exponentials times $\sum_{p\ge e^{5T/4}}p^{-2}$ (and an additional fixed arity moment), negligible. This applies across low and high blocks, or two differently marked low groups, while preserving the actual signs. Thus the replacement has arbitrary fixed inverse-log accuracy without a constant depending on the maximal tuple arity. It applies to the physical Fourier density at fixed $x$; the reciprocal approximation errors use supremum in $x$ and need not be differentiated.

Write $\xi=K_0(A+1)/\ell$ for the normalized high lower endpoint. After this replacement the residual positive log density off its unit atom is $O(1/\xi)=O(\ell/(A+1))$: marking one coordinate in the reciprocal convolution exponential bounds the density times its coordinate by the mass of the exponential truncated there. For the signed residual its density in the active compact range is $-\rho(v/\xi-1)/v$, by the [signed Dickman identity](r98-source-tag-full-sign-stretched-cancellation.md), §3, using the high support up to $.7$; the compact argument is below the upper truncation. For low products outside (2) all active residual arguments lie in $[.4,.6]$ for large $X$ since $A T=o(L)$. Factorial decay then makes this signed density smaller than every fixed power of $\ell^{-1}$ uniformly, even multiplied by (2)'s uncropped positive mass bound $O((A+1)^2)$.

For clarity, after Siegel–Walfisz in $F$ at fixed lower data and actual label, the real cap is on $\log h$ at fixed $x=hF$. A $g$-bin or a $u$-slab of normalized width $d$ has log-width $O(Td)$ there; all such hard conditions translate by $\log x$, so their physical variation moves each endpoint by $O(1)$ in log over the window. The Jacobian for the normalized high coordinate gives widths $O(d/\ell)$ and endpoint movement $O(1/L)$. The real prime mark $\log(h/z)/\log(x/h)$ is bounded and at fixed $h,z$ its physical derivative is $O(1/(XL))$. Thus the positive supremum and variation bounds are $O((A+1)(d+1/T))$, using the above positive density and total low reciprocal mass. The far atom from (2) is negligible even for every inverse-$\ell$ grid width used below. For the signed separated root, the same estimate on the compact range uses the small absolute signed density, and the far tail including its atom again costs (2). These physical bounds, their major transform and the uniform minor estimates imply, on each comparison slab or bin of width $d$, a positive fourth norm

$$
                \ll X^{3/4}(A+1)(d+1/T)
                                                                    \tag{3}
$$

for the inverse-$\ell$ widths in use. The global positive arm over the enclosing window has fourth norm $\ll X^{3/4}(A+1)^2$. The extra fixed joint interval on $u$ in a $g$ bin clips a translated interval at fixed label and does not change the signed estimate; every such separated full-sign fourth norm is $O_D(X^{3/4}\ell^{-D})$ for every fixed $D$. The continuum calculations are made only after temporarily separating the root, and the positive arm is used as a domination of the actual canonical one.

## 3. Joint-cell signed rejection, without the growing absolute low-product loss

Take label width $\delta=\ell^{-5}$ and root width $\eta_0=\ell^{-10}$ in the [disjoint joint cells](r108-source-curved-containing-adaptive-floors.md) of the two real coordinates of actual integers, using exact half-open conventions. Include $0,20$ among label nodes; include $0,A$ among the root nodes, with all gaps comparable to the indicated widths (split fixed equal subdivisions between designated endpoints). Nonnegative $g$ requires $u\ge g$; the true outer slivers are handled by positive collars as before. Write a cell as $(B,J)$ with root interval $J=(a_-,a_+]$. Denote its actual composite canonical signed Fourier arm (only the target-unit mask temporarily suppressed) by $A_{B,J}$, and its scalar by

$$
       m_{B,J}=-\ell^{-1}\int_B
                                    (C_{a_+}(g)-C_{a_-}(g))\,dg .
                                                                    \tag{4}
$$

For these modeled bins $g>0$; equality with zero is included in the collar. The following are the summed one-arm estimates, with a uniform improvement over using the absolute low-product mass to flatten the mark:

$$
 \sum_{B,J}\|A_{B,J}-m_{B,J}H\|_4
                      \ll X^{3/4}(A+1)^2\ell^{-2},\qquad
              \sum_{B,J}|m_{B,J}|\ll \ell^{-1}.                    \tag{5}
$$

The separated signed and repeated roots are negligible in this sum by Sections 1–2; the grid has $O((A+1)^2\delta^{-1}\eta_0^{-1})$ cells. In strict rejection use $h=sW_1W_0P$, $z=s^jW_1$, $j\in\{0,1\}$, and the exact sign $(-1)^j\mu(W_0)$. Put $t=\log s/T$, $\lambda=\log W_1/T$, $w=\log W_0/T$ and $B_x=\log x-L$. The root test is $u=g+\lambda+jt\in J$ and rejection is $w<Z+B_x/T$ with

$$
                       Z=2g+\lambda+(2j-1)t .
$$

One may first freeze the physical shift $B_x/T$ at zero. Slicing at fixed actual low data in $g$ and taking supremum and variation in $x$ costs $O((A+1)^2/(T\ell))$ per cell: for each low tuple, the collision interval moves monotonically through length $O(1/T)$, the mark is $O(1/\ell)$, and the full positive labeled low reciprocal mass is $O((A+1)^2)$. Integration on a common region has smaller variation, by the bounded physical derivative of the mark below. This freezes only a real major density after the prime replacements in $F,P$, not the original arithmetic rejection. It is negligible when summed over the grid.

After freezing this shift, do **not** yet flatten the prime mark in the signed real integral. At fixed $g,\lambda,t,j,x$ it is

$$
 R(w,x)=
 \frac{T}{L/2+(g+(j-1)t-w)T+B_x}\,
 \frac{L/2+gT+B_x}{L/2-(g+\lambda+jt)T}.
                                                                    \tag{6}
$$

All denominators are comparable to $L$ uniformly when $0\le w\le Z$, since then their log offsets are $O((A+1)T)=o(L)$. Formula (6) is the actual reciprocal giant-prime density $T/\log P$ times the real mark $\log(h/z)/\log F$. Retaining it, apply the uniform tuple replacement of Section 2 to the two low groups, with their true distinctness, as well as the old prime. At fixed other coordinates the bin and $w\le Z$ cuts are affine one-variable limits, and (6) has uniformly bounded variation on its occupied positive-length intervals, by its denominators. The active frozen points obey $t+\lambda+w\le2u\le2A$, so real restrictions may be taken on the complete locally finite convolution exponentials with no introduced tail. The marked measure is the positive $\mathcal P(d\lambda)$ of the fixed-floor proof; the unmarked measure has signed cumulative $S(w)=\rho_+(w/4)$, including its unit atom at zero. The strict/weak difference at that atom concerns only a null set in $g$. Thus the contribution of flattening (6) to $2/\ell$ is the integral of $R(w,x)-2/\ell$ against $dS(w)$ up to $Z$, with the other data still as variables.

For $Z<0$ there is no integral. For $Z\ge0$ integrate by parts on the true signed cumulative, including its initial atom:

$$
 \int_{[0,Z]}(R(w,x)-2/\ell)\,dS(w)
   =S(Z)(R(Z,x)-2/\ell)
               -\int_0^Z S(w)\partial_wR(w,x)\,dw.                \tag{7}
$$

This yields a uniform bound $O(\ell^{-2})$ for each $g,\lambda,t,j$. Indeed
$|R(Z,x)-2/\ell|\ll (1+g+\lambda)/\ell^2$ and
$|\partial_w R|\ll\ell^{-2}$. On $Z\ge0$ the factor $1+g+\lambda$ is at most a constant times $1+Z$, and $\sup_{Z\ge0}(1+Z)S(Z)$ and $\int_0^\infty S(w)\,dw$ are absolute constants by Dickman decay. The estimates for $\partial_xR$ and $\partial_x\partial_wR$ on the fixed domain are $O(1/(X\ell L))$ and $O(1/(X\ell^2 L))$ respectively directly from (6). Since $Z$ is now independent of $x$, (7) therefore also has physical total variation $O(\ell^{-2})$ on $\mathcal J$, including its endpoint jumps when extended by zero. This signed integration must precede flattening; using the absolute unmarked mass at this point would lose the stated box rate.

For each fixed marked $\lambda,t,j$, the intervals in $g$ for the different cells are disjoint, since they are $B\cap(J-\lambda-jt)$, and their combined length is $O(A+1)$. On their support $\lambda\le A$, and $\mathcal P([0,A])\ll A+1$ by marking a coordinate or restricting the exponential to jumps at most $A$. Thus the sum of the physical density and variation errors from (7) is $O((A+1)^2/\ell^2)$. The normalized limiting scalar after flattening is exactly $-m_{B,J}$ for the rejected arm, by the two signed choices of $j$ that give (4). The second inequality of (5) is uniform: bound the **two nonnegative summands** in the formula for $C_a$ separately, sum over the partition in $u$ first, and then use the integrable version of the floor-independent factorial envelope (7) of the fixed-floor proof. That envelope bounds each summand by the atom plus integral against the positive $\mathcal P$ density $\le1/4$, with $\rho$ decaying factorially in $g$. Hence the summed scalar has no $A$-loss. The first inequality of (5) now follows from the major transform bound using physical supremum plus variation and the original fourth arc integral, the negligible shifted-boundary and reciprocal errors, and the uniform minor bound of Section 1. Subtracting the strict rejected and repeated arms from the separated one gives the minus sign in (4).

## 4. Actual maximum, literal collars, and exceptions

At the nominal root nodes, away from the $O(\delta)$ label collars the original divisor and product tests are satisfied on exactly the corresponding accepted cell pairs for every target. The two root floor choices give independent true prefixes of the right-closed root cells. For any subset of accepted pairs, bound the absolute coefficient error by the sum of absolute cell product errors as in the adaptive proof. Hölder, Parseval and (5) give target norm

$$
 \ll X^{3/2}\left((A+1)^2\ell^{-3}+(A+1)^4\ell^{-4}\right)
 \ll X^{3/2}(A+1)^2\ell^{-3},
                                                                    \tag{8}
$$

since $(A+1)^2\ll\ell$ on the stated range. This works for any selected pair of nodes at every individual target because the majorant includes every individual cell error, not a union of errors for whole settings. In $U$ also include the genuine wing as a cell always present with model $H/(2\ell)$ and fourth error $O(X^{3/4}\ell^{-2})$ from its original asymptotic. This preserves (5)–(8).

The $O(\delta^{-1})$ forbidden collar cells retain the literal strict and weak cuts; they are dominated with all root choices by positive label-bin convolutions. By (3) their common target norm is $O(X^{3/2}(A+1)^2\delta)$. The uncurved composite nonlong collar near $g=20$ is a bounded number of such bins against the global positive mate, costing $O(X^{3/2}(A+1)^3\delta)$, also when the mate is a wing. Each estimate is smaller than (8) at the chosen width. Restoring the true target units is uniform as well: an offending shared prime divides $N$, is at least $e^{5T/4}$, and allows only $O(X/p+1)$ first operands, with $O(\ell)$ candidate primes of $N$. The absolute $L$-power for label multiplicities and log marks from Section 1 therefore makes the omitted contribution $O_D(XL^{-D})$ pointwise, independently of the selected floors.

The nominal model telescopes in the right-closed root intervals in (4). For the real label collars lost in this summation, the fixed-floor envelope gives absolute bounded $C_a$ and uniformly bounded $\int_0^\infty|C_a(g)|\,dg$ even as $A$ grows. Thus passing to the full triangle or to $g\ge20$ costs $O(\delta)$ in the scalar before $\ell^{-2}$. The [common rational completion](r80-source-local-mean-square-at-sign-transition.md), §3, then replaces $[H^2]_N$ by $I_N$ at arbitrary inverse-log target-norm cost, multiplying only the common bounded scalar rather than the number of nodes. In particular this keeps the same arithmetic comparator for all floors.

To move from a nominal lower mesh node to the actual selected floor at a target, use a fixed enlarged root slab of width $O(\eta_0+1/T)$ covering the gap, and likewise independently on the right (with enclosing end slabs at $0,A$). Keep all genuine divisor and product tests in the difference, then dominate by the positive slab against a global positive mate; for $U$ this follows after the exact nonlong-orbit identity, so no absolute sum of an unclosed long orbit is used. The wing itself is unchanged. Uniformly each slab error has target norm $O(X^{3/2}(A+1)^3\eta_0)$ by (3). There are $O((A+1)/\eta_0)$ slabs, hence the maximum on a side costs at most $O(X^{3/2}(A+1)^{7/2}\eta_0^{1/2})$ in norm by summing the squares. Telescope the two sides using the same global mate upper bound in each, without multiplying by the number of choices on the other side. This is smaller than (8) at $\eta_0=\ell^{-10}$. The true thresholds are included because the normalized shift is $O(1/T)$, much smaller than $\eta_0$.

Finally the real functions in the model vary contiguously in this interpolation. At fixed marked $\lambda,t,j$, changing $a$ by a root mesh width clips an interval of at most that length in $g$. Integrating the positive marked mass through $A+1$ bounds the $L^1$ change by $O((A+1)\eta_0)$. The same envelope bounds $c_a$ and $f(a,b)$ changes (for $f$, use the absolute bound on the other factor on its triangle). Thus model interpolation costs $O(X^{3/2}(A+1)\eta_0/\ell^2)$, smaller than (8). Both choices are the actual target-selected continuum choices after this step. Squaring the summed target norm for each row proves (1).

The deterministic margin of the fixed-floor proof is absolute for every real $a,b\ge0$, independently of any box size, and $I_N\gg X$ at even targets in a fixed interior subwindow. Chebyshev on the common supremum at the signed scale $X/\ell^2$ gives the stated exception bound. The upper and lower norm comparisons for $A=\ell^{1/2-\epsilon}$ follow since the maximal error is $o(X^{3/2}/\ell^2)$, while the comparator has sharp norm $X^{3/2}/\ell^2$ by its upper singular-series moment and positive interior size. No choice of floors is asserted to remove exceptional targets at the endpoint box size $\sqrt\ell$.
