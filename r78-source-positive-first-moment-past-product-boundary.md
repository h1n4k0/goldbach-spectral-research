# A positive-density obstruction just past the two-containing product boundary

Use the prescribed true typical-count carrier and all exact signs of the [finite short-orbit theorem](r77-source-finite-short-orbit-product-boundary.md), now with fixed exponents

$$
                       0<a,b<20,\qquad
                        0<\delta=a+b-20<4.
 \tag{1}
$$

Use the fixed polynomial split $Z=X^{\delta_0}$, where $\delta_0$ is the sufficiently small fixed upper exponent in the [original typical-count construction](r72-source-typical-count-masked-obstruction.md). Write $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\mathcal J=[X/2,(1+\Delta)X/2]$ and $\mathcal X=[X,(1+\Delta)X]$ as there. On the full carrier $n=hF$, $h=sWU$, $m=kG$, $k=s'W'U'$, the primes $F,G$ obey the actual moving floors $\sqrt N e^{-aT_N},\sqrt N e^{-bT_N}$, with $T_N=\log N/\log\log N$. Keep the actual $s,W,U$ masks, including both parities, squarefreeness, genuine $N$-units, and the true typical count of $WU$ with its two excluded neighborhoods. At this fixed split every allowed $U$ prime is above the exceptional band for sufficiently large $X$, so the true count is carried by $W$; no extra parity or sign mask is imposed. Both operands lie in $\mathcal J$ on $n+m=N$, and the exact original strict tests and external minus sign use the actual integers $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$, $Q_N=\lfloor N e^{-20T_N}\rfloor$. Denote the resulting signed full selected sum by $R_N$.

**Theorem (unconditional).** For some $c_1,c_2>0$ depending only on the fixed parameters, for every sufficiently large real $X$ at least $c_2X$ even $N\in\mathcal X$ satisfy $R_N\ge c_1X$. Consequently on this same prescribed carrier

$$
                     \sum_{\substack{N\in\mathcal X\\2\mid N}}
                              |R_N|^2\gg_{\rho,a,b}X^3 .
 \tag{2}
$$

In particular the preceding power saving in the squared mean cannot extend just past $a+b=20$ for this carrier. For $0<\delta<5/4$ the two-containing row is individually nonnegative; for the full range (1) it is the **actual signed first moment**, not individual nonnegativity, that gives the lower bound. This is not a counterexample to the unrestricted central estimate, Hypothesis S, or Goldbach.

## 1. Isolate the two-containing interaction without changing the masks

The four-row algebra in the finite short-orbit theorem is valid individually for $a,b<20$; its only use of $a+b\le20$ is when suppressing the last row. In particular both distinguished primes exceed $D_N$ on the actual carrier, and each complete containing family has the unrestricted signed logarithmic sum $-\Lambda(h)=0$, or $-\Lambda(k)=0$. After excluding the forbidden products and applying the original exterior minus sign, the fourth row is therefore

$$
 H_N=
    \sum_{\substack{n+m=N\\\text{actual carrier and units}}}
        \ \sum_{\substack{z\mid h,\ w\mid k\\FzGw\le Q_N}}
                     \mu(z)\mu(w)\log(h/z)\log(k/w).
 \tag{3}
$$

The test in (3) includes equality literally. For any surviving term $zw\le e^{\delta T_N}$ by the actual prime floors. Since $T_N=T+O(1/\ell)$ uniformly and $\delta<4$, this is below $e^{4T}$ for large $X$. The only possible factors below $e^{4T}$ of the two cofactors are their respective old primes $s,s'$. Thus the **complete** short choices in (3) are tested among $\{1,s\}\times\{1,s'\}$. At $\delta<5/4$ even those nontrivial primes cannot occur. For larger $\delta$ the proof below retains their genuine signs $-1$.

For use here, the sum $E_N$ of the other three actual rows still satisfies

$$
       \sum_{\substack{N\in\mathcal X\\2\mid N}} |E_N|^2
                         \ll_{\rho,a,b} X^3\ell^{-1/5}.
 \tag{4}
$$

To see precisely why the earlier estimates apply, set $F_0=\sqrt X e^{-aT}$ and $G_0=\sqrt X e^{-bT}$. The three rows still reduce to their fixed external floors, with a positive comparison on log-width-$O(1)$ floor slivers. Every active cofactor is above $\tfrac12\sqrt X e^{-20T}$: its ordinary long label requires that directly, or its short containing label is $\le Q_N/(D_N+1)<\sqrt N$ and the corresponding cofactor is $\gg\sqrt X$. The fixed upper windows have log widths $O_{a,b}(T)$. The ordinary omitted label product is $\ll e^{(20+a+b)T}$; a mixed ordinary omission is $\ll e^{(20+\max(a,b))T}$ and its containing omission is $\ll e^{\max(a,b)T}$. The same label cap $M=e^{(22+a+b)T}$ therefore works. It still divides $sW$ on each side, with a bounded number of primes per label and the same $(1+\log\ell)^{O(1)}$ pointwise label multiplicity. The signed Euler band beginning at $e^{(23+a+b)T}$ and ending at $V_X/4$ remains untagged, independent of the labels and of reciprocal mass $\theta\log\ell+O(1)$.

Now the two exact Perron separations for $hF$ and for a genuine containing label $Fz$, the prime comparison and real endpoint-variation bound, and the thin-bin fourth norms of §2 of the finite short-orbit theorem do not use $a+b\le20$. Each ordinary signed bin has fourth norm $O(X^{3/4}\ell^{-1-1/10})$; a positive or containing bin has $O(X^{3/4}\ell^{-1})$. The original strict/weak tests still have only $O(\ell)$ ambiguous bin pairs and $O(\ell^2)$ potentially accepted pairs, because each exact threshold moves by $O(1)$ in log. This gives $O(X^{3/2}\ell^{-1/5})$ in $\ell^2(N)$ for the ordinary row, $O(X^{3/2}\ell^{-1/10})$ each for the two mixed rows, and $O(X^{3/2}\ell^{-1})$ at the seams. The moving prime floors cost $O(X^{3/2}\ell/L)$ by the same positive comparison, and unit errors are individually superlogarithmically small. Thus (4) is precisely the earlier **three-row** estimate, not an extension of its fourth-row bound.

The fourth row itself has the upper estimate

$$
                 \sum_{\substack{N\in\mathcal X\\2\mid N}} |H_N|^2
                           \ll_{\rho,a,b} X^3.
 \tag{5}
$$

Indeed its active cofactors also lie in the full fixed windows just described, since both containing labels are long. On each arm the absolute mark is dominated by a constant times the positive all-label mark from the previous theorem (up to four combined short choices, and $\log(h/z)\ll\log F$). Use those full-window positive polynomials with the fixed external prime floors, dropping the product, moving floor and unit tests only for the upper comparison. Each fourth norm is $O(X^{3/4})$ since its full log width is $O(T)$, by the same positive bound independent of $a+b\le20$. Parseval and Hölder give (5). Thus large positive first moment of (3) will be enough for a positive density of genuine targets.

## 2. Uniform actual one-arm mass in the prime exponent

At this fixed split put $S=sW$. The true positive lower-product mass without a parity selection is

$$
       \sum_{\substack{S=sW\\\text{actual lower gates}}} \frac1S
                         \asymp_\rho\ell.
 \tag{6}
$$

This is the same weighted counting statement as in the original typical-count construction. Briefly, the squarefree product of $1+1/p$ on the permitted $W$ alphabet is $\asymp\ell$ by Mertens (the excluded neighborhoods cost bounded mass). In its normalized reciprocal law, each prime is present independently with probability $1/(p+1)$. The expected $\log W$ is $O(\delta_0 L)$, small against the size cap by the original choice of $\delta_0$. Each count has variance $O(\log\ell)$; its mean is $\log\ell+O(1)$ for all $W$ primes and $(1-\theta)\log\ell+O(\log\log\ell)$ for the exceptional ones. Thus the original total and typical exceptional gates retain all but $o(1)$ of that normalized mass, and Markov applied to the hard size gate leaves a fixed positive fraction. The $s$ reciprocal mass is a positive constant up to fixed factors. Both parities remain in (6); neither is used to alter the actual carrier.

Since $\delta_0$ is fixed, for sufficiently large $X$ all primes above $Z=X^{\delta_0}$ are above the two excluded neighborhoods and the exceptional interval. For fixed allowed $S$, the upper rough product $U$ thus has no residual count condition beyond being squarefree, nonempty, and formed of primes $>Z$. Let $\varrho$ be its positive reciprocal continuum density from the [growing-residual theorem](r75-source-dynamic-giant-growing-rough-residual.md), with kernel $\mathbf1_{[\delta_0,.7]}(u)/u$ exponentiated by convolution. The possible factor bound $X^{.7}$ is immaterial at the relevant products. On the compact $[.4,.6]$ this density is bounded and Lipschitz, and bounded from below by a positive constant since its one-prime term is $1/u$ there. The uniform approximation by this density for a hard interval and bounded-variation mark has error $O_A(L^{-A})$ for any fixed $A$, by the reciprocal PNT proved there. No arithmetic regulator is added to $U$.

For the $a$ arm let

$$
                        \alpha=\frac{\tfrac12 L-\log F}{T}.
$$

For $z=1$ or $s$, define the actual positive finite measure $\lambda_{S,z}$ on $[0,a]$ by placing the weight $\log(h/z)$ at the $\alpha$ of each fixed-scale integer $n=S U F\in\mathcal J$, with $h=SU$, $F$ prime, and the actual $U$ gates. This uses the fixed external lower floor and possible primes up to $\sqrt X$. The representations are unique even on the larger fixed carrier, because the true count of $W$ supplies a prime exceeding $2V_X$: two prime factors at least $\sqrt X e^{-aT}$ would leave at most $O(e^{2aT})$ for that prime, which is impossible. This applies also to a repeated $F$. The same discussion gives measures on $[0,b]$ for the other arm, with variable $\beta$ and $w=1$ or $s'$.

Uniformly for any hard interval $J_\alpha\subseteq[0,a]$, with either convention on its endpoints,

$$
 \lambda_{S,z}(J_\alpha)
       =c_S |J_\alpha|
        +O_{\rho,a,A}\left(\frac{X}{S\ell^2}|J_\alpha|
                              +\frac{X}{S}L^{-A}\right),
 \qquad
 c_S=\frac{|\mathcal J|}{S\ell}\,
           \varrho\left(\tfrac12-\frac{\log S}{L}\right).
 \tag{7}
$$

The main coefficient is independent of $z$, and the reflected (7) has the same $c_{S'}$. Verify this by first fixing $U$ and applying the ordinary PNT to the unweighted prime $F$ in the exact intersection of $\mathcal J/(SU)$ with its requested log band. On nonempty support the prime and cofactor coordinates have logarithms comparable to $L$. After including the mark $\log(SU/z)\ll L$ and summing the uniform prime errors over $U$, the error is $O_A(XL^{-A}/S)$: the rough reciprocal mass of all eligible $U\le X$ is bounded by $\prod_{Z<p\le X}(1+1/p)=O_{\delta_0}(1)$. This PNT step is valid on arbitrary hard subintervals, including the exact single-endpoint discrepancy, whose weight is negligible at these sizes.

Make the change $x=SU F$ in the real prime integral, obtaining the factor $1/(SU)$ and the mark $\log(SU/z)/\log(x/(SU))$. At each fixed $x\in\mathcal J$ replace the reciprocal $U$ measure by $\varrho(v-\log S/L)\,dv$, $v=\log(SU)/L$, using the uniform hard interval and bounded-variation comparison. The mark is uniformly bounded with bounded variation there; the relevant arguments stay in $[.4,.6]$ because $S\le X^{1/64}$ and $\alpha$ stays bounded. The resulting change of variable back to $\alpha$ has $dv=d\alpha/\ell$ and $v=\tfrac12+\alpha/\ell+O(1/L)$. The mark equals $1+O(1/\ell)$ uniformly since $z=1$ or $s$ with $\log s\le7T/4$; the Lipschitz density differs from its value at $\tfrac12-\log S/L$ by $O(1/\ell)$. Integrating over the exact physical interval and over $J_\alpha$ proves (7). This is an ordinary prime density calculation on the actual carrier, with no prime progression or random phase assumption.

In particular $c_S\asymp X/(S\ell)$ uniformly, and (6) yields $\sum_S c_S\asymp X$. Summing (7)'s upper bounds over $S$ shows that the mass of an arm in any fixed log-exponent interval of width $\eta$ is $O(X(\eta+\ell L^{-A}))$ for arbitrary $A$. We will also use (7) with the reflecting fixed arm cut, independently of the other operand.

## 3. The true averaged fourth row and its signed area

We calculate the first moment of $H_N$ over even $N\in\mathcal X$. All chosen numbers are odd; every pair in $\mathcal J^2$ therefore has a target in this sum before the unit comparison. The latter costs $o(X^2)$ in absolute value over the target window: at a fixed target any common prime divides $N$, is at least $e^{5T/4}$, and allows only $O(X/p)$ actual first operands. There are $O(\ell)$ such primes, only four labels per pair, and logarithmic marks $O(L^2)$. Thus the summed cost is $O(X^2L^2\ell e^{-5T/4})$. This proves that using the independent real mass in the two arms below has not inserted a loss from common-prime collisions.

The real exponent comparison also costs $o(X^2)$. On actual fourth-row support the two exponents are nonnegative for large $X$: e.g. even the fixed lower floor of $G$ gives $\sqrt X G\ge Xe^{-bT}\gg Q_N$ because $b<20$, so $F\ge\sqrt X$ could not enter (except that its excluded endpoint is harmless). Work in the fixed windows $[0,a]\times[0,b]$. The true floors differ from these upper endpoints in exponent by $O(1/T)$. Write $u_z=\log z/T$, $v_w=\log w/T$. The true product test has boundary

$$
                \alpha+\beta
                   = 20+u_z+v_w+O(1/T)
$$

uniformly in the actual target, from $\log Q_N=L-20T+O(1)$ after the integer floor. Replace it by the fixed comparison $\alpha+\beta\ge20+u_z+v_w$, leaving the actual integer condition in the definition of $H_N$. Any difference lies in an endpoint strip or diagonal strip of exponent width $O(1/T)$, with exact endpoint equalities included. For fixed $S,S',z,w$ and a fixed $\alpha$, a diagonal strip allows a $\beta$ interval of this width. Apply (7) uniformly, then bound the whole first-arm mass by $O(X/(S\ell))$. The same bound holds for coordinate strips after reflection. Summing over $S,S'$ and the four choices with (6), these absolute errors are $O(X^2(1/T+\ell L^{-A}))=o(X^2)$. The fixed comparison itself still tests only the four short choices because $\delta<4$ with a fixed margin. No signs were discarded outside these positive error estimates.

For fixed $S,S',z,w$, apply (7) to the inner $\beta$ interval cut by the fixed diagonal at every $\alpha$. It gives the constant $c_{S'}$ times its real length, with uniform error $O(X/(S'\ell^2)+X L^{-A}/S')$. That length as a function of $\alpha$ is bounded and of bounded variation; Stieltjes partial summation using (7) replaces the outer measure by $c_S\,d\alpha$ with the same type of error. Thus this pair main is the area of the frozen rectangle part multiplied by $c_S c_{S'}$, with error $O(X^2/(SS'\ell^3)+X^2 L^{-A}/(SS'))$ after enlarging $A$ if needed. Summing all errors gives $o(X^2)$ by (6). The area is

$$
              \frac12(\delta-u_z-v_w)_+^2 .
$$

Indeed at the corner $(a,b)$ its two equal legs have length $(\delta-u_z-v_w)_+$, less than both $a,b$ because $a,b<20$.

Now impose the actual short signs from (3). For $u=\log s/T$, $v=\log s'/T$, both in $[5/4,7/4]$, the four terms give the **signed** area

$$
 \begin{aligned}
 \Phi_\delta(u,v)
   &=\tfrac12\{\delta^2-(\delta-u)_+^2-(\delta-v)_+^2
                                   +(\delta-u-v)_+^2\}\\
   &=\int_0^u\int_0^v \mathbf1_{r+t<\delta}\,dt\,dr.
 \end{aligned}
 \tag{8}
$$

The equality is the mixed finite difference of $x\mapsto(x_+)^2/2$. In particular $\Phi_\delta(u,v)\ge c_\delta>0$ uniformly, for example by integrating on a fixed square strictly inside the triangle with side $\min(5/4,\delta/4)$. This positivity derives from the genuine short signs; when multiple short terms occur it is not an estimate of each pair by a positive mark. Combining the comparison, the unit bound, and the actual reciprocal masses gives

$$
       \sum_{\substack{N\in\mathcal X\\2\mid N}}H_N
          =\sum_{S,S'}c_S c_{S'}\Phi_\delta(\log s/T,\log s'/T)
                     +o_{\rho,a,b}(X^2)
          \gg_{\rho,a,b} X^2 .
 \tag{9}
$$

The input at each fixed $S$ was an actual real density with uniform interval trace, not a continuous model replacing the four signs or an arbitrary post-selection of favorable targets.

## 4. Transfer to the full selected sum on a positive density

Even when $H_N$ takes both signs, (5) and (9) imply that $H_N\ge cX$ for at least $c'X$ even targets. Choose $c$ small enough that the targets below that threshold contribute at most half the positive lower bound in (9). The remaining targets contribute $\gg X^2$, and Cauchy with (5) forces their count to be $\gg X$. By (4), only $O(X\ell^{-1/5})=o(X)$ targets can have $|E_N|>cX/2$. Hence on a positive density of even targets

$$
                             R_N=H_N+E_N\ge cX/2 .
$$

This proves the theorem and (2). If desired, shrinking that subset by a fixed factor also ensures a bounded binary singular series, since $\sum_{N\in\mathcal X,\,2\mid N}\mathfrak S(N)\ll X$ by the same positive Euler expansion as in the typical-count construction. On such a subset the lower bound is also $\gg \mathfrak S(N)N$. The result does not make any sign, size, or cancellation claim about other carriers or correlations. The upper limit $\delta<4$ is where the proof has only the one old prime per side in the short double orbit; any larger excess can introduce actual $W$-prime removals, so this positivity argument is not extended there.
