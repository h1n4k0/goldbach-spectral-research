# The actual curved containing sign on every fixed bounded floor box

Use the [actual semiprime-wing carrier](r105-source-semiprime-wing-and-containing-contrast.md), the same hard physical window $\mathcal J$, even target interval $\mathcal X$, $L=\log X$, $\ell=\log L$, $T=L/\ell$, and $T_N=\log N/\log\log N$. In particular both operands $n=hF,m=kG$ are genuine squarefree $N$-units, $F=P^+(n),G=P^+(m)$, and $h=sV$ has $5T/4\le\log s\le7T/4$, with every prime of $V$ at least $e^{4T}$; the same holds for the other arm. The wing $V=1$ is admitted. Keep the actual root floors $F\ge\sqrt N e^{-aT_N}$ and $G\ge\sqrt N e^{-bT_N}$ and the exact integer thresholds $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$, $Q_N=\lfloor Ne^{-20T_N}\rfloor$. The two floors are one **common** choice $0\le a,b\le A_0$ for the whole dyad, with arbitrary fixed finite $A_0$. They are not independently chosen at each target.

Let $V_{\rm curv}(N;a,b)$ be just the genuine containing-containing portion of the pair sum on this enlarged carrier: the divisors are $d=Fz,e=Gw$, $z\mid h,w\mid k$, and the three genuine tests are $d>D_N,e>D_N,de>Q_N$, with the original exterior minus and actual full Walsh weight $\mu(h)\mu(k)$. It includes no ordinary divisor arms. Write $V_f(N;a,b)$ for the forbidden retained-long correction (both long tests, $de\le Q_N$, with exterior plus) and $U(N;a,b)$ for the uncurved product of the two genuine long containing traces with exterior minus. As in the [first curved calculation](r106-source-curved-containing-forbidden-collision.md), $V_{\rm curv}=U+V_f$ identically and the correction is composite-composite only. Write $I_N=\Sigma(N)B_{\mathcal J}(N)$ for the same singular series and hard physical overlap.

Let $\mathcal P=\exp_*(\mathbf 1_{y\ge4}\,dy/y)$ on the nonnegative line, with unit atom at zero and the convolution exponential interpreted on compact intervals. Let $\rho$ be Dickman's function and $\rho_+(v)=\mathbf1_{v\ge0}\rho(v)$, with value zero for $v<0$. For $a\ge0,g\ge0$ set

$$
 \begin{split}
 C_a(g)=2\int_{5/4}^{7/4}\frac{dt}{t}\int d\mathcal P(\eta)\bigg[
   &\mathbf1_{g+\eta\le a}\rho_+\!\left(\frac{2g+\eta-t}{4}\right)\\[-1mm]
   &-\mathbf1_{g+\eta+t\le a}\rho_+\!\left(\frac{2g+\eta+t}{4}\right)
                          \bigg],\\
 c_a&=\int_{20}^{\infty} C_a(g)\,dg,\qquad
 f(a,b)=\iint_{\substack{0\le g,g'\le20\\g+g'\ge20}}
                      C_a(g)C_b(g')\,dg\,dg'.
 \end{split}                                                     \tag{1}
$$

The support is $g\le a$. In particular $c_a$ is zero in the real model for $a\le20$. At $a=41/2$, $c_a$ is the one-label collision constant of the first curved calculation; the general expression keeps **all** old and rough short labels, not just the empty label.

**Theorem (unconditional).** Uniformly for each common pair $a,b\in[0,A_0]$, with constants allowed to depend on $A_0$,

$$
 \begin{split}
  \left\|V_f-\frac{f(a,b)}{\ell^2}I_N\right\|_{\ell^2(N)}
                  &\ll_{A_0} X^{3/2}\ell^{-3},\\
  \left\|U+\frac{(1/2-c_a)(1/2-c_b)}{\ell^2}I_N\right\|_{\ell^2(N)}
                  &\ll_{A_0} X^{3/2}\ell^{-3}.
 \end{split}                                                     \tag{2}
$$

The scalar margins have the **absolute** bounds

$$
     |f(a,b)|<\frac1{20},\qquad
     |c_a|,\ |c_b|\le\frac{17}{2041200},\qquad
     (1/2-c_a)(1/2-c_b)-f(a,b)>
                \left(\frac12-\frac{17}{2041200}\right)^2-\frac1{20}>0 .
                                                               \tag{3}
$$

Thus the full **curved containing-containing** term $V_{\rm curv}$ is negative of magnitude $\gg X/\ell^2$ on any fixed interior target subwindow outside $O_{A_0}(X/\ell^2)$ even targets, and its squared norm is of order $X^3\ell^{-4}$. The implicit exceptional set can depend on the common pair. This does not assign a sign to the forbidden correction alone, to the composite-only curved row, or to the complete pair sum. It is not simultaneous for all floor choices. No floor growing beyond a fixed box, individual prescribed target or Hypothesis S is concluded.

## 1. Genuine labels on both sides of the long threshold

On one arm write $v_h(z)=\mu(z)\log(h/z)$. The actual containing mark before the full Walsh sign is $-v_h(z)$. For a squarefree composite cofactor $\sum_{z\mid h}v_h(z)=\Lambda(h)=0$. Consequently its actual long Walsh containing trace is exactly

$$
   \mu(h)\sum_{\substack{z\mid h\\Fz>D_N}}(-v_h(z))
       =\mu(h)\sum_{\substack{z\mid h\\Fz\le D_N}}v_h(z).           \tag{4}
$$

A wing has only the nonzero long mark $-\log s$ at $F$, and its Walsh sign $\mu(s)=-1$ gives the actual positive mark $+\log s$. Its root exceeds $\sqrt N$, and $F(D_N+1)>Q_N$, independent of how large the fixed box $A_0$ is. The elementary product identity for two long traces therefore gives $V_{\rm curv}=U+V_f$ on the exact integer pairs, with no contribution from wings in $V_f$. In particular (4) is only used on composite cofactors, and the underlying algebra never replaces a retained product test by the two separate long tests.

On a composite arm put $u=(L/2-\log F)/T$ and $g=(L/2-\log(Fz))/T=u-\log z/T$. A forbidden retained-long pair has each label less than $\sqrt N$, since $Q_N/(D_N+1)<\sqrt N$. Thus it lies in the fixed comparison triangle in (1) up to boundary displacements $O(1/T)$: use $\log D_N=L/2-20T+O(1)$ and $\log Q_N=L-20T+O(1)$, while the label cap $\sqrt N$ gives $g\ge -O(1/T)$. Independently, a nonlong label in (4) has $g\ge20-O(1/T)$ and $g\le a+O_{A_0}(1/T)$ from the actual root floor and $z\ge1$. Both domains use $g$ for the **actual label**, not for a root. We temporarily replace the floor on $F$ by $F\ge \sqrt X e^{-aT}$, uniformly within a log-width-$O_{A_0}(1)$ sliver from the real floor. In the fixed comparison this is $u\le a$, and every accepted label has $g\le u$. An interval with no available label causes no difficulty, including at $a=0$ or $a=20$.

All roots, marked labels and corresponding composite cofactors have logarithms $L/2+O_{A_0}(T)$ on these regions and their enclosing slivers. The label size bound is $\log z\le(A_0+O(1))T$; for example a nonlong label satisfies $\log z\le(a-20)T+O_{A_0}(1)$ when it exists. The [split-free composite bin estimates](r104-source-split-free-composite-collision-law.md), §1, apply on a fixed enclosing label window with bin width $\delta=\ell^{-3}$: both the positive fourth norm $O_{A_0}(X^{3/4}\delta)$ and the rooted full-sign fourth norm $O_{A_0,B}(X^{3/4}\delta\ell^{-B})$ use the corresponding fixed short-label block, without fixing a number of short labels equal to one. At most two separated root choices can appear at a physical integer, as otherwise three near-square-root factors are present; each short label includes only a bounded number of primes at least $e^{4T}$, plus possibly $s$. Hence every coefficient multiplicity is bounded by a fixed power of $L$, uniformly in the chosen common floors.

For a precise hard transfer, take a grid of such bins in a fixed enclosing interval of $g$, with $0$ and $20$ endpoints, and similarly for the other arm. In the forbidden term only $O_{A_0}(\delta^{-1})$ cells meet a true moving edge of the triangle. Keep the literal product and long tests in all these cells, and dominate them by positive full-bin convolutions. The resulting target norm is $O_{A_0}(X^{3/2}\delta)$ by Hölder and Parseval. In the uncurved product, the composite trace (4) differs from its fixed comparison $g\ge20$ in a bounded number of bin slivers, costing the same norm even with the other factor's full positive fourth norm $O_{A_0}(X^{3/4})$. The same componentwise positive bounds apply when that other factor is a wing, using its fourth norm from the semiprime-wing analysis. A change in the root floor has enclosing normalized root width $O(1/T)$: the positive marked bound comes from the same single-arm density, changed only by this root interval, and costs $O_{A_0}(X^{3/2}/T)$ in target norm against any relevant full positive mate. All these bounds allow the strict and weak endpoints appearing in (4) and in $V_f$; they do not discard exact integer equality by fiat. Omitting target-unit masks for the Fourier comparisons, then restoring them, costs $O_{A_0,B}(XL^{-B})$ per target. Indeed a lost prime divides both operands and hence $N$, is at least $e^{5T/4}$, and permits $O(X/p+1)$ first operands; there are $O(\ell)$ such primes and only polylogarithmic weights/labels per operand. This also covers a wing with an old prime shared by its mate.

The later floors genuinely allow nonempty labels beyond the empty label. For example, at $a=23$ choose $s$ with $\log s=(3/2)T+O(1)$ and $F$ with $\log F=L/2-22T+O(1)$. Choose distinct primes $P_1,P_2$ of sizes $X^{.24+o(1)}$ and $X^{.26+o(1)}$ making $sFP_1P_2$ lie in a fixed interior subinterval of $\mathcal J$, by the prime number theorem in proportional intervals. Then $F$ is the true largest prime, $s$ is an eligible nonlong label since $\log(Fs)=L/2-20.5T+O(1)$, and its term in (4) is not zero. An odd wing with disjoint primes in the same physical interior supplies a genuine even target satisfying the units and the other floor. This example is not an estimate for the total of labels.

## 2. A single common signed collision model on both domains

Use the auxiliary major/minor arcs and the model $H$ in the first curved calculation, §2, with arc exponent sufficiently large depending on the fixed box. Thus on $\theta=c/q+\beta$ it is $H=(\mu(q)/\varphi(q))\widehat J(\beta)$, with $\widehat J$ the Fourier transform of the indicator of $\mathcal J$, and it is zero off the majors. We verify the one-arm estimate required on both sides of $g=20$. For any bin $B$ in the positive portion of the enclosing label window, let $A_{a,B}$ be the canonical composite arm with fixed floor, physical window and actual integer label bin, carrying the mark $\mu(h)v_h(z)$. For any fixed sufficiently large $D$ it satisfies

$$
 \left\|A_{a,B}+\frac H\ell\int_B C_a(g)\,dg\right\|_4
      \ll_{A_0}X^{3/4}
           \left(\delta\ell^{-2}+\frac1{T\ell}+L^{-D}\right).      \tag{5}
$$

To check the range of the first curved calculation in proving (5), separate the root first, retaining the full signed composite cofactor and its short label, then subtract the strict and repeated root violations. The separated signed contribution is inverse powers of $\ell$ smaller than $X^{3/4}\delta$, by the split-free rooted fourth norm. A strict rejection has a unique other prime $P>F$ in $h$; writing $h=sWP$ one has $\log(sW)\le(2A_0+1)T$ for large $X$, since $sW< x/F^2$ with $x=hF\in\mathcal J$. The same upper bound holds for a repeated root $F\mid h$. Three near-square-root factors are still impossible since $A_0$ is fixed. Hence the repeated-root class is disjoint from strict rejection and supported on $X^{1/2+o_{A_0}(1)}$ physical integers with polylogarithmic marks, so its fourth norm is $X^{3/8+o_{A_0}(1)}$ as before. In the strict class every short label is $z=s^jW_1$, $j\in\{0,1\}$, $W=W_1W_0$ squarefree with disjoint factors, because $P$ is too large to divide $z$. The sign is exactly $\mu(h)\mu(z)=(-1)^j\mu(W_0)$, including for a label containing both the old prime and rough factors.

Here are the moving limits explicitly. At fixed $x$, set $t=\log s/T,\eta=\log W_1/T$. Then the floor says $u=g+\eta+jt\le a$, and the strict collision is

$$
 \log W_0/T<2g+\eta+(2j-1)t+(\log x-L)/T .                        \tag{6}
$$

The major proof applies Siegel–Walfisz to $F$ at fixed cofactor and label, with all hard endpoints, as in the first curved calculation. No cofactor factor lies in a polylogarithmic denominator, so the reduced numerator factor is exactly $\mu(q)/\varphi(q)$. Now use ordinary reciprocal PNT in $P$ at fixed $x,s,W_1,W_0,j$: its interval is the actual intersection of the bin, floor and (6), after $d\log P=T\,dg$. The real mark times reciprocal density, excluding the factor $1/(sW_1W_0)$, is $(T/\log P)(\log(h/z)/\log F)=2/\ell+O_{A_0}(\ell^{-2})$. Old-prime and low-prime reciprocal masses on the relevant fixed log-ratio ranges, also with both label occupations, are bounded by a constant depending on $A_0$. At fixed labels, the wall in (6) shifts monotonically by $O(|x-y|/(XT))$ between physical points. Its clipped bin length is always at most $\delta$, even if a root-floor endpoint coincides with the label-bin endpoint or the wall. The real marks on common subintervals have total variation at most $O_{A_0}(1/(\ell L))$ before integrating in $g$. Thus replacing the shift by zero and the displayed mark by $2/\ell$ gives supremum plus total-variation error $O_{A_0}(\delta/\ell^2+1/(T\ell))$ for the physical density, including its jumps at the fixed $\mathcal J$ endpoints. It is a fixed-label integration estimate, so permits the atom $W_0=1$ and does not need a derivative of the Dickman prefix.

After freezing the shift, the signed unmarked reciprocal prime sum, at its actual affine cap in (6), tends to $\rho_+((2g+\eta+(2j-1)t)/4)$ by the signed reciprocal Dickman identity. The marked reciprocal sum is the positive exponential $\mathcal P(d\eta)$. To see the exact extent of these replacements, all occupied products on (6) obey $t+\eta+\log W_0/T\le2u+O(1/T)\le2A_0+O(1/T)$, so one can use only primes in a fixed log-ratio interval up to $(2A_0+2)T$. Expand distinct prime tuples and replace one reciprocal measure at a time on hard slices, with the other coordinates fixed, using uniform prime reciprocal interval errors at prime scales $\ge e^{5T/4}$. The only distinctness deletions, including any repetition across the two partitions, cost a reciprocal prime-square tail. The arities and total reciprocal weights are bounded in terms of $A_0$, so all these errors, and the earlier major prime replacement errors, are arbitrary inverse powers of $L$. Strict versus weak real equality on (6) meets the unmarked atom only on a null set of $g$ (after the integration into the bin); every arithmetic equality was still present before this approximation. With the $dt/t$ old weight, $j=0,1$ give the precise difference in (1). The positive exponential may therefore be taken locally finite on all $y\ge4$ without altering any bounded-floor integrals. No part of this argument puts $z=1$ past the seam.

For the strict rejected-root polynomial's actual minors, the three hard integer cuts separated in the first curved calculation are unchanged: $hF$ in $\mathcal J$, $Fz$ in the bin, and $F<P(h)$. Their half-integer Perron boundaries give a fixed power of $L$ overhead, and the root floor is still a hard interval endpoint of the prime factor. This holds also for $g\ge20$, since $h,F=X^{1/2+o_{A_0}(1)}$, $z\le e^{O_{A_0}(T)}$, and exactly the same $P(h)-1/2$ boundary applies. Coefficient bounds and dyadic comparability $hF\asymp X$ on relevant dyads are unchanged. The reciprocal-distance Cauchy bound with $P_{\rm arc}<q\le\lfloor X/P_{\rm arc}\rfloor$ makes the minor supremum arbitrarily inverse-log small relative to $X$, where $P_{\rm arc}$ is the auxiliary denominator cap; coefficient energy is $O_{A_0}(XL^{O_{A_0}(1)})$. This yields the same minor fourth saving. On the majors the fixed-label variation bound gives the real transform error times $\min(X,|\beta|^{-1})$ with the same rational factor. The fourth moment uses its integrable fourth power and the convergent norm series in the auxiliary denominators. This proves (5) with the minus sign for the true canonical arm, by subtracting the rejected arm, not by modeling it as a second admissible root.

For $V_f$, sum the fourth errors in (5) over the bins: this costs $O_{A_0}(X^{3/4}\ell^{-2})$ because $\delta^{-1}/(T\ell)\ll\ell^{-2}$. The summed main norms are $O_{A_0}(X^{3/4}/\ell)$. Thus the accepted two-arm products have coefficient error $O_{A_0}(X^{3/2}\ell^{-3})$ by Hölder and Parseval. The signs of the two canonical arms cancel in the product and leave the exterior plus of the correction. The accepted bin model converges to $f(a,b)$ with error $O_{A_0}(\delta)$ in the coefficient before $\ell^{-2}$, since only boundary cells omitted from the triangle matter and $C_a,C_b$ are bounded. The hard error was already bounded in Section 1. For $U$, sum (5) on each arm on $g\ge20$ to get composite scalar $-c_a/\ell$ or $-c_b/\ell$ with summed fourth error $O_{A_0}(X^{3/4}\ell^{-2})$. If $a\le20$ this region contains no positive model length, and the fixed-to-actual sliver bound still applies. The actual wing fourth comparison in the semiprime-wing theorem contributes $+(1/2)/\ell$ to each scalar with the same error; the wing support and major polynomial have no dependence on $a$ or $b$. Apply the exterior minus to their product. Finally the [reduced-numerator rational completion](r80-source-local-mean-square-at-sign-transition.md), §3, gives $I_N$ for $[H^2]_N$ in target norm with arbitrary inverse-log error: sum reduced numerators before absolute values, retain the actual finite widths, and complete only the auxiliary continuous and denominator tails. This proves both arithmetic statements of (2), with the same physical normalization and both literal masks restored. It does not multiply an existing target $\ell^2$ error by a target-dependent Fourier term.

## 3. A floor-independent deterministic margin

For completeness the density of $\mathcal P$ away from its atom is at most $1/4$. If $v\ge4$, marking one occupied coordinate in its convolution expansion gives $v\,p(v)=\mathcal P([0,v-4])$ for almost every $v$, where $p$ is the density. Only jumps at most $w$ can contribute to $\mathcal P([0,w])$, so $\mathcal P([0,w])\le\max(1,w/4)$ by the total mass of that finite exponential. Hence $v\,p(v)\le v/4$. The density is zero below $4$, and the zero-coordinate mass is exactly one.

Set $z_g=(2g-7/4)/4$ for this deterministic inequality only. The two expressions in brackets in (1) are nonnegative before subtraction, so their absolute difference is at most their maximum. By monotonicity and $\rho_+=0$ at negative arguments, either expression is bounded by $\rho(\max(0,z_g+\eta/4))$. Combining the atom and density estimate and using $2\log(7/5)<17/25$ yields, for every $a\ge0$,

$$
 |C_a(g)|\le\frac{17}{25}
       \left\{\rho(\max(0,z_g))
                +\int_1^\infty \rho(\max(0,z_g+y))\,dy\right\}.   \tag{7}
$$

This bound uses no growth of the arithmetic box; it is purely deterministic. From $v\rho(v)=\int_{v-1}^v\rho(w)\,dw$ and monotonicity, $\rho(v)\le1/\lfloor v\rfloor!$ for $v\ge0$. The factorial tail satisfies $\sum_{n\ge k+1}1/n!\le(k+2)/((k+1)(k+1)!)$ for $k\ge0$, by bounding the successive ratios by $1/(k+2)$. For $g\in[i,i+1]$, $1\le i\le19$, define $k_i=\lfloor(8i-7)/16\rfloor$. The right side of (7) on that cell is bounded by

$$
 A_i=\frac{17}{25}
       \left\{\frac1{k_i!}+\frac{k_i+2}{(k_i+1)(k_i+1)!}\right\}.
$$

For $i=0$, the atom contributes at most one inside the braces; the integral in (7) is at most $7/16+\sum_{n\ge1}1/n!\le7/16+2$, since $z_g\ge-7/16$. Thus use $A_0^{\rm env}=(17/25)(55/16)$ for this cell, writing $A_0^{\rm env}$ as $A_i$ at $i=0$ in the following finite sum to avoid confusing it with the floor box endpoint. Taking the full area of every unit cell that can touch the triangle gives the exact rational bound

$$
 |f(a,b)|\le\sum_{i=0}^{19} A_i
                    \sum_{j=\max(0,18-i)}^{19}A_j
       =\frac{2268576190953089179}{51039593640000000000}<\frac1{20}.
$$

For $g\in[20+2j,22+2j]$, $j\ge0$, one has $\lfloor z_g\rfloor\ge9+j$. The braces in (7) are then at most $2/(9+j)!$. Therefore

$$
 |c_a|\le\int_{20}^{\infty}|C_a(g)|\,dg
      \le\frac{68}{25}\sum_{n\ge9}\frac1{n!}
      \le \frac{68}{25}\frac{10}{9\cdot9!}
      =\frac{17}{2041200}.
$$

This proves (3) without numerically evaluating Dickman's function or assigning a sign to the forbidden integral. Since $I_N\gg X$ at each even target in a fixed interior physical subwindow and $\|I_N\|_{\ell^2(N)}\ll X^{3/2}$, the sum of the asymptotics in (2) and Chebyshev at scale $X/\ell^2$ give the stated exceptional count and sharp squared scale. All arithmetic error bounds above are for one common pair of floors, so no union over a variable floor parameter at each target has been taken.
