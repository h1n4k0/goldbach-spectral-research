# A local mean-square law at the short-prime sign transition

Retain the entire prescribed both-parity carrier of the [short-prime Euler sign theorem](r79-source-short-prime-euler-sign-transition.md), with its **fixed** polynomial split $Z=X^{\delta_0}$, literal size, total-count and genuine typical exceptional-count gates, and the fixed physical intervals $\mathcal J=[X/2,(1+\Delta)X/2]$ and $\mathcal X=[X,(1+\Delta)X]$. Thus the operands are squarefree $N$-units $n=hF,m=kG\in\mathcal J$ with $n+m=N$, $h=sWU,k=s'W'U'$, and $\log s/T,\log s'/T\in[5/4,7/4]$, where $L=\log X,\ \ell=\log L,\ T=L/\ell$. Keep the original prime floors $F\ge\sqrt N e^{-aT_N}$ and $G\ge\sqrt N e^{-bT_N}$, $T_N=\log N/\log\log N$, for fixed $0<a,b<20$ and $\delta=a+b-20>0$. The original long-divisor and product tests use the literal integer cutoffs $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$, $Q_N=\lfloor N e^{-20T_N}\rfloor$ and the signed selected sum $R_N$ includes the original external minus. There is no extra selector by sign, parity, largest-factor size, or target residue class.

Let $\mathcal C_X$ and $\Psi(\delta)$ be precisely the positive normalization and signed continuum coefficient in (2)–(4) of the sign theorem. In particular the normalization is taken from the actual lower masks, not from a limiting size-gate constant. Write $B_{\mathcal J}(N)=|\mathcal J\cap(N-\mathcal J)|$, with Lebesgue length, and use the binary singular series

$$
 \Sigma(N)=\sum_{q\ge1}\frac{\mu(q)^2 c_q(N)}{\varphi(q)^2},
 \qquad
 c_q(N)=\sum_{\substack{a\bmod q\\(a,q)=1}} e(aN/q),\qquad
 e(v)=\exp(2\pi i v).
$$

**Theorem (unconditional).** On the stated true carrier one has

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
   \left|R_N-\Sigma(N)B_{\mathcal J}(N)
          \left(\frac{\mathcal C_X}{|\mathcal J|}\right)^2
                       \Psi(\delta)\right|^2
                   \ll_{\rho,\delta_0,a,b} X^3\ell^{-1/5}.
 \tag{1}
$$

In particular, let $\delta_*$ be the unique zero of $\Psi$ on the interval $[4,4+4\sqrt{\mathrm e}]$ identified in the sign theorem. For the exact fixed symmetric floors $a=b=(20+\delta_*)/2$, the true squared sum is $O_{\rho,\delta_0}(X^3\ell^{-1/5})$, although $a+b>20$. If $\Psi(\delta)\ne0$, then on any fixed strictly interior subinterval of the target window, its sign holds with magnitude $\gg X$ for all but $O(X\ell^{-1/5})$ even targets in that subinterval (constants also depend on its distance from the endpoints). On the full window the strict sign holds outside $O(X\ell^{-1/15})$ even targets. These are mean-square and density conclusions for the exact selected carrier, not pointwise estimates or statements on Hypothesis S or the unrestricted central sum.

## 1. Exact orbit rows, fixed comparison, and the moving diagonal

By the [finite short-orbit identity](r77-source-finite-short-orbit-product-boundary.md) and the first-three-row bound of the [product-boundary obstruction](r78-source-positive-first-moment-past-product-boundary.md), as extended to the present fixed exponents in §1 of the sign theorem, write $R_N=E_N+H_N$, with

$$
 \|E\|_{\ell^2(\mathcal X\cap 2\mathbb Z)}\ll X^{3/2}\ell^{-1/10},
 \qquad
 H_N=\sum_{\substack{hF+kG=N\\\text{true carrier and units}}}
    \ \sum_{\substack{z\mid h,\ w\mid k\\FzGw\le Q_N}}
       \mu(z)\mu(w)\log(h/z)\log(k/w).
 \tag{2}
$$

The sign of the displayed double-containing row is plus: each unrestricted containing orbit sums to zero, and the forbidden product is subtracted before applying the original exterior minus. The signs in (2) are the actual short signs, with no extra full-cofactor parity. For the first three rows the long tests and mixed short correction have the previous estimate regardless of this fourth row.

For (2), replace the two actual lower floors by $F_0=\sqrt X e^{-aT},G_0=\sqrt X e^{-bT}$, and remove only the common-unit test temporarily. The fixed floors are lower than the moving floors by monotonicity for large $X$, and differ by a bounded amount in logarithm since $T_N=T+O(1/\ell)$ uniformly. Under these fixed floors the actual product condition gives $F\le Q_N/G_0<\sqrt X$, and $G\le Q_N/F_0<\sqrt X$: indeed $Q_N\asymp_\Delta Xe^{-20T}$, and $a,b<20$. All active cofactors are then $\asymp\sqrt X$ up to factors $e^{O_{a,b}(T)}$. Each distinguished prime is unique (including no square of it): if two prime factors of an operand were at least its fixed floor, their residual cofactor would be $e^{O_{a,b}(T)}$, whereas the genuine typical count supplies a third, distinct prime above $2V_X$, whose logarithm is $\gg T\ell^\theta$ as in the inherited carrier. Hence the fixed comparison still has the unique $h,F,S,U$ decomposition, with $S=sW$, and the two prime exponent coordinates can be restricted to

$$
 \alpha=(L/2-\log F)/T\in[0,a],\qquad
 \alpha'=(L/2-\log G)/T\in[0,b].
$$

For any term surviving the fourth-row test even with fixed floors, $zw\ll_\Delta e^{\delta T}$. Fix $A>\max(4,\delta)$, for instance $A=21$, and in each arm enumerate short labels $z\mid S,\ z\le e^{AT}$ (and analogously $w$). Every relevant label belongs here because every $U$ prime exceeds $X^{\delta_0}$. All such short labels have bounded arity and the inherited true count gives $(1+\log\ell)^{O_A(1)}$ labels per operand. The full positive reciprocal label weight is $\ll\ell$ by (7) of the sign theorem. The total error from removing the unit test is $O_C(XL^{-C})$ for each target and every fixed $C$: a common prime divides $N$, is at least $e^{5T/4}$, and there are $O(\ell)$ possible such primes. For each there are $O(X/p)$ eligible integers on the first side, as $p\ll X$, and the maximum absolute product weight is $O(L^2(1+\log\ell)^{O_A(1)})$. Both operands are still odd after this test is removed.

The genuine floor-restoration error is $O(X^{3/2}\ell/L)$ in $\ell^2(N)$. In fact a changed pair must have one distinguished prime in a fixed log-width-$O(1)$ sliver starting at its fixed floor. Compare positively with all short labels and the other arm's full prime window. The all-label positive fourth norm (7) in the finite short-orbit proof is $O(X^{3/4}\ell(B+1)/L)$ for log width $B$, giving $O(X^{3/4}\ell/L)$ and $O(X^{3/4})$, respectively. Parseval and Hölder prove the error, after taking convolutions of the two positive comparisons.

Use bins of width $1/\ell$ in the two actual coordinates $\gamma=\alpha-\log z/T$ and $\gamma'=\alpha'-\log w/T$. These are hard log bins in the **integer products** $Fz,Gw$ of width $T/\ell$. They cover fixed compact intervals and there are $O(\ell)$ choices on each arm. The true weak test is $\gamma+\gamma'\ge (L-\log Q_N)/T=20+O(1/T)$ uniformly, including the original integer floor. Accept a bin pair if every label in its rectangle satisfies the test for every $N\in\mathcal X$; reject if every label fails it for every such $N$; for definiteness one may use the whole continuous rectangle for both rules, treating undecided endpoints as ambiguous. Only $O(\ell)$ pairs are ambiguous, since each first bin has at most a bounded number of opposite bins within $O(\ell^{-1}+T^{-1})$ of the diagonal. Their actual integer contributions are bounded by the positive bin convolutions. Each bin has positive fourth norm $O(X^{3/4}\ell^{-1})$ by the same estimate with $B=T/\ell$, so these seams cost $O(X^{3/2}\ell^{-1})$ in $\ell^2(N)$. All arithmetic equalities are included in the acceptance test or in the positive ambiguity bound.

Let $\mathcal A$ be the fixed family of accepted bin pairs. Define $A_i(\theta)$ to be the actual first-arm exponential sum $\sum_{n\in\mathcal J}\sum_z\mu(z)\log(h/z)e(n\theta)$ in gamma-bin $i$, with the fixed exponent interval and only the comparison changes just used. Define $B_j(\theta)$ with $\alpha'\in[0,b]$ for the other arm. The accepted part of the double row is **exactly** the Fourier coefficient at $N$ of $\sum_{(i,j)\in\mathcal A}A_i B_j$. Thus the earlier algebra and the exact diagonal leave only these actual separated signed bin polynomials.

## 2. One-bin major density and genuinely hard minors

For a hard bin $J_i$ let

$$
 c_i=\frac{1}{\ell}
      \sum_{\substack{S=sW\\\text{true lower gates}}}\frac{1}{S}
       \varrho\!\left(\tfrac12-\frac{\log S}{L}\right)
        \sum_{\substack{z\mid S\\z\le e^{AT}}}\mu(z)
        \left|\left(J_i+\tfrac{\log z}{T}\right)\cap[0,a]\right|.
 \tag{3}
$$

Here $\varrho$ is precisely the fixed-split positive reciprocal density from the sign theorem. Set $d_j$ by reflection with $[0,b]$. Then $|c_i|,|d_j|\ll\ell^{-1}$ and $\sum_i|c_i|+\sum_j|d_j|\ll1$ by the positive reciprocal label bound. Write $J^\wedge(\beta)=\int_{\mathcal J}e(\beta x)\,dx$, $M_X(\beta)=\min(X,|\beta|^{-1})$ (with value $X$ at zero).

Take auxiliary reduced major arcs with denominator $q\le P=L^C$ and radius $1/(q\lfloor X/P\rfloor)$ for a sufficiently large fixed $C$. These auxiliary arcs are disjoint for large $X$; they only decompose the full circle, without changing any original divisor or prime cutoff. At $\theta=a_0/q+\beta$ on these arcs,

$$
 A_i(\theta)=\frac{\mu(q)}{\varphi(q)}
       \left\{c_iJ^\wedge(\beta)+E_i^\wedge(\beta)\right\}
                      +O_H(XL^{-H}),\qquad
 |E_i^\wedge(\beta)|\ll\ell^{-2}M_X(\beta)
 \tag{4}
$$

for arbitrary fixed $H$, with the analogous expansion for $B_j$. Crucially the continuous transforms are independent of the reduced numerator.

Indeed, at fixed $h,z$ the hard product $Fz$ gate is one prime interval, clipped by the fixed floor and $\mathcal J/h$. Apply ordinary Siegel–Walfisz in $F$, with arbitrary fixed log savings after absorbing the polylogarithmic phase variation and the number of residue classes. Every prime factor of $h$ exceeds $P$, as does $F$. Summing the reduced residues of $F$ gives $\mu(q)/\varphi(q)$ since both $a_0$ and $h$ are units. Multiplying by the actual mark and changing physical coordinate to $x=hF$ gives the real measure $dx/h$ with mark $\log(h/z)/\log(x/h)$. The accumulated discrete error is $O_H(XL^{-H})$: the total reciprocal $h,z$ mass is $O(\ell)$ since the upper $U$ alphabet has bounded reciprocal mass at this fixed split.

At fixed physical $x\in\mathcal J$, replace the reciprocal $U$ measure by $\varrho(v-\log S/L)\,dv$, $v=\log h/L$, by the uniform interval and bounded-variation estimate of the sign theorem and its [fixed-polynomial upper-product input](r75-source-dynamic-giant-growing-rough-residual.md). The use of that estimate is literal: the true exceptional count lies entirely in $W$ and the upper primes are above the fixed split, so no moving count or prime factor of $U$ is omitted. The interval arguments lie in the compact $[.4,.6]$ since $S\le X^{1/64}$ and the prime exponent has bounded support. The logarithmic mark as a function of $v$ is uniformly bounded with bounded variation, including a hard endpoint convention. These reciprocal replacements have arbitrary inverse-logarithmic errors and are integrated over $x$ before estimating variation in $x$.

In the continuous expression change variables at each $x$ to $\alpha=(L/2-\log(x/h))/T$. The integration interval is exactly $I_{i,z}=(J_i+\log z/T)\cap[0,a]$, independent of $x$, and $dv=d\alpha/\ell$. With $F(\alpha)=\sqrt X e^{-\alpha T}$, the resulting density on $\mathcal J$ is

$$
 g_i(x)=\frac1\ell\sum_{S,z}\frac{\mu(z)}{S}
       \int_{I_{i,z}}
         \varrho\!\left(\tfrac12+\tfrac{\alpha}{\ell}
                 +\tfrac{\log x-L}{L}-\tfrac{\log S}{L}\right)
         \frac{\log x-\log F(\alpha)-\log z}{\log F(\alpha)}
                                 \,d\alpha .
 \tag{5}
$$

The ratio is $1+O_A(\ell^{-1})$ and changes by $O_A(|x-y|/(XL))$ between two physical points. The density term differs from its value in (3) by $O(\ell^{-1})$ and has the same $O(|x-y|/(XL))$ Lipschitz comparison by compact Lipschitz regularity of $\varrho$. Since each $|I_{i,z}|\le\ell^{-1}$, summing with the **absolute** reciprocal label mass $O(\ell)$ gives
$\sup_{\mathcal J}|g_i-c_i|+\operatorname{Var}_{\mathcal J}(g_i-c_i)\ll\ell^{-2}$.
This is not a relative estimate to the possibly cancelling signed $c_i$. Integration by parts, including the two outer endpoint terms, proves (4).

On the complementary arcs, the two actual integer tests $hF\in\mathcal J$ and $Fz$ in its hard bin are separated by the two height-$X^4$ half-integer Perron integrals in §2 of the finite short-orbit theorem. No new variable enters its bilinear minor argument: the short-label twist remains inside the coefficient of $h$. The fixed prime interval by $\alpha$ is an existing first-arm prime interval, and the cap $z\le e^{AT}$ only limits the available labels in the coefficient. For every fixed $K$ one therefore has $\sup_{\rm minor}|A_i|,\sup_{\rm minor}|B_j|\ll_K XL^{-K}$ by choosing $C$ large enough. The pointwise label count and unique factorization also give $\|A_i\|_2^2,\|B_j\|_2^2\ll XL^2(1+\log\ell)^{O_A(1)}$. Parseval, the minor supremum on one factor and this energy on the other show that even the sum over $O(\ell^2)$ pairs has Fourier coefficient norm $O_H(X^{3/2}L^{-H})$ for any fixed desired $H$ after choosing $C$. All primes, short labels and hard endpoints in this bound are those of the actual bin polynomials.

## 3. Local complete rational and continuous factors

Let $D_{\mathcal A}=\sum_{(i,j)\in\mathcal A}c_i d_j$. Multiplying (4) and summing over accepted bins gives on each arc the continuous term

$$
 \frac{\mu(q)^2}{\varphi(q)^2}
     \big\{D_{\mathcal A} J^\wedge(\beta)^2+U_{\mathcal A}(\beta)\big\},
 \qquad
 |U_{\mathcal A}(\beta)|\ll\ell^{-1}M_X(\beta)^2 .
 \tag{6}
$$

Each cross term has a factor $\ell^{-1}\ell^{-2}$, and there are $O(\ell^2)$ terms; the double errors are smaller. The remaining discrete errors can be made $O_H(X^2L^{-H})$ pointwise by choosing stronger Siegel–Walfisz savings before summation, since the original sums and continuous terms are bounded polynomially in $L$ times $X$. Their integrated magnitude is negligible uniformly in $N$ because the union has measure $O(P^2/X)$ and $P$ is a fixed power of $L$.

The continuous terms in (6) are independent of the numerator, so sum it **before** taking absolute values. This gives exactly $c_q(-N)=c_q(N)$. On every squarefree $q$ the divisor formula and a count of positive multiples of an lcm give

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}|c_q(N)|^2
  \ll_{\Delta} X\sum_{d,e\mid q}(d,e)
        =X\prod_{p\mid q}(p+3).
 \tag{7}
$$

In fact $|c_q(N)|\le\sum_{d\mid q,\ d\mid N}d$. For the pair $(d,e)$ the count is at most $(1+\Delta)X/[d,e]$ even when the lcm exceeds the top of the interval, since only positive integers are counted. By (7), $\|c_q\|_2/\varphi(q)^2\ll_\epsilon\sqrt X\,q^{-3/2+\epsilon}$ for any fixed $\epsilon>0$ on squarefree $q$. For instance the extra factors after removing $q^{-3/2}$ are $\prod_{p\mid q}(1+3/p)^{1/2}(1-1/p)^{-2}\ll_\epsilon q^\epsilon$ by separating finitely many small primes. In particular the series for $\Sigma$ has $\ell^2(N)$ norm $O(\sqrt X)$. Since $\int M_X(\beta)^2d\beta\ll X$, the grouped $U_{\mathcal A}$ terms in (6) have norm $O(X^{3/2}\ell^{-1})$ by Minkowski and (7).

The finite-width main transform for each $q\le P$ can be extended to all real $\beta$ with integrated error $O(X\min(1,q/P))$, from $|J^\wedge(\beta)|\ll M_X(\beta)$ and the true radius $1/(q\lfloor X/P\rfloor)$. The estimated norms in (7) sum this and the omitted $q>P$ tail to $O_\epsilon(X^{3/2}P^{-1/2+\epsilon})$. Here $D_{\mathcal A}=O(1)$ by the two $\ell^1$ coefficient bounds. The complete $q$ sum is the stated usual singular series; it also converges absolutely at a fixed $N$ by $c_p(N)=-1$ except for the finitely many prime divisors of $N$. The physical Fourier integral is exact:

$$
 \int_{\mathbb R}J^\wedge(\beta)^2 e(-N\beta)\,d\beta
             =(\mathbf1_{\mathcal J}*\mathbf1_{\mathcal J})(N)
             =B_{\mathcal J}(N).
$$

Thus the accepted bins have local leading term $\Sigma(N)B_{\mathcal J}(N)D_{\mathcal A}$ and error $O(X^{3/2}\ell^{-1})$ in $\ell^2(N)$. This is a local arithmetic multiplier, not a replacement of $\Sigma(N)$ by its average over even integers.

## 4. Quantitative scalar identification and the zero

Pass from the accepted bin pairs in (3) to the continuous diagonal $\gamma+\gamma'\ge20$. The difference concerns at most $O(\ell)$ bin pairs, each of positive absolute scalar area $O(\ell^{-2})$ by the reciprocal label bound. The full continuous scalar is exactly the right-hand area expression (9) of the sign theorem divided by $|\mathcal J|^2$, before the latter's first-moment error. Indeed for fixed $z,w$ its area in $[0,a]\times[0,b]$ is $\tfrac12(\delta-(\log z+\log w)/T)_+^2$: the triangle lies in that rectangle since $\delta<\min(a,b)$. Labels larger than $e^{AT}$ have zero area. This uses (3) directly, not an upgrade of the earlier first moment to a local assertion.

For this literal real scalar the peeling proof in §§3–4 of the sign theorem is quantitative. Under its positive labeled reciprocal measure, the total-count replacement and eventual release of the temporary low count have normalized errors $O(\ell^{1-2\log 2})$, from the $O(\ell)$ normalized moment of $2^{\omega(W)}$ and the true $2\log\ell$ cap. The low-part logarithm is temporarily $O(T\log\ell)$, so the hard-size-strip and Lipschitz density errors together cost $O(\log\ell/\ell)$; the strip remains controlled by marking one high factor with its $\log p$ weight. The exact true exceptional count is wholly high in this peeling, since $e^{AT}$ is below its low endpoint for all sufficiently large $X$. The same two estimates apply without the label factor to $\mathcal C_X$. The local weights of the low short primes after peeling are precisely $-1/(p+1)$, not $-1/p$ and not an additional full-parity sign. On the two arms they converge via the convolution exponential of the positive reciprocal measure with coefficient $-2$, with total-variation exponential-replacement error $O(\sum_{p\ge e^{4T}}p^{-2})$. To pass to the real kernel, quantitative ordinary PNT with partial summation on the fixed log-coordinate intervals $[4,A]$ and $[5/4,7/4]$ gives uniform reciprocal interval errors $O_H(L^{-H})$ for any fixed $H$ (their least prime size is $e^{cT}$). Only boundedly many convolution orders are active, and the test area and its translates have uniform bounded variation; the normalized old-prime integral uses the same measure $\pi$ as in the sign theorem. These errors all beat $\ell^{-1/10}$. In particular the earlier exact normalization comparison with $B_X\log(7/5)$ has error $O(X\ell^{-1/10})$, not just an unspecified $o(X)$. This proves

$$
 D_{\mathcal A}
      =\left(\frac{\mathcal C_X}{|\mathcal J|}\right)^2
                \Psi(\delta)+O_{\rho,\delta_0,a,b}(\ell^{-1/10}).
 \tag{8}
$$

By $B_{\mathcal J}\ll X$ and (7), the resulting local coefficient error is $O(X^{3/2}\ell^{-1/10})$ in $\ell^2(N)$. Combine it with (2), the fixed-floor, unit and diagonal-seam errors and the circle analysis. Squaring proves (1).

For even $N$, the singular series is bounded below by the positive absolute constant $2\prod_{p>2}(1-1/(p-1)^2)$, since the additional factors for odd primes dividing $N$ are $(p-1)/(p-2)\ge1$. Also $\mathcal C_X/|\mathcal J|\asymp1$. The overlap length is the distance of $N$ from the nearer endpoint of $\mathcal X$. Therefore when $\Psi(\delta)\ne0$ the claimed magnitude and sign in any fixed interior subinterval follow from (1) and Chebyshev's inequality. For the full window remove endpoint strips of width $X\ell^{-1/15}$; outside them every wrong or zero sign contributes at least $\gg X^2\ell^{-2/15}$ to (1). This gives $O(X\ell^{-1/15})$ exceptions including the removed strips. When $\delta=\delta_*$ and $a=b=(20+\delta_*)/2$, the entire deterministic term is exactly zero and (1) is the stated genuine selected-carrier saving beyond the product boundary. No estimate is inferred on the unused carriers or on a prescribed target.
