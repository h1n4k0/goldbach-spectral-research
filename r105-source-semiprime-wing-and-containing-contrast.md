# The actual semiprime wing and its signed long-containing contrast

Use the [split-free composite carrier](r104-source-split-free-composite-collision-law.md) on the hard interval $\mathcal J=[X/2,(1+\Delta)X/2]$, with $L=\log X$, $\ell=\log L$, $T=L/\ell$, even targets $N\in\mathcal X=[X,(1+\Delta)X]$, and the same fixed $\Delta>0$. Keep both actual squarefree $N$-unit operands, $n=hF,\ m=kG\in\mathcal J$, $n+m=N$, canonical $F=P^+(n)$, $G=P^+(m)$, and the two actual prime floors $F\ge\sqrt N e^{-aT_N}$ and $G\ge\sqrt N e^{-bT_N}$, where $T_N=\log N/\log\log N$. In $h=sV$, $s$ is the unique old prime $5T/4\le\log s\le7T/4$, and $V$ is squarefree with every prime at least $e^{4T}$. Use the same requirements on $k$. The enlargement permits $V=1$ or $V'=1$ on either arm. Call $h=s$ a **wing** and $V>1$ a composite cofactor; there are no other changes of eligibility. In particular the exact original tests
$$
 d>D_N,\quad e>D_N,\quad de>Q_N,\qquad
 D_N=\lfloor\sqrt N e^{-20T_N}\rfloor,\qquad Q_N=\lfloor N e^{-20T_N}\rfloor
$$
and the original external minus still define the full row. All floors below are common fixed choices $0\le a,b\le A_0$, uniform on the fixed box, not separately adaptively chosen at each $N$.

Denote the full signed sum with [actual unnormalized Walsh weight](r96-source-walsh-two-full-and-dominance-switch.md) $\mu(h)^{u_1}\mu(k)^{u_2}$ by $W^{\rm all,\mathbf u}$, and the sum restricted to two composite cofactors by $W^{\rm comp,\mathbf u}$. Thus the latter is the sum of the seven genuine rows of the composite theorem. Write $I_N=\Sigma(N)B_{\mathcal J}(N)$, using its singular series and physical overlap, and $\kappa_X=\mathcal C_X^{\rm comp}/|\mathcal J|\asymp1$, using exactly its composite calibration. Use the signed short measure and old-prime probability of the [capped long-floor calculation](r85-source-capped-long-floor-orbits.md):
$$
 \nu=(\delta_0-\pi)*\exp_*(-\mathbf1_{[4,A]}(t)\,dt/t),\qquad
 \pi(dt)=\frac{\mathbf1_{[5/4,7/4]}(t)\,dt/t}{\log(7/5)},\qquad
 M(x)=\int (x-t)_+\,d\nu(t).
$$
Here $A>24+2A_0$; all uses of $M$ are independent of $A$, and $M(x)=0$ for $x\le0$. Put
$$
 K_{\mathbf u}(a,b)=
   (-1)^{u_1}M(b+20(2u_2-1))+
   (-1)^{u_2}M(a+20(2u_1-1)).
$$

**Theorem (unconditional).** For every one common choice of $(a,b)$ and all four Walsh choices,
$$
 \left\|W^{\rm all,\mathbf u}-W^{\rm comp,\mathbf u}
                  -\frac{\kappa_X}{2\ell}K_{\mathbf u}(a,b)I_N
       \right\|_{\ell^2(N)}
       \ll X^{3/2}\ell^{-2}.                                      \tag{1}
$$
In particular, for $\mathbf u=(1,1)$ the genuine full wing increment is strictly negative and has magnitude $\gg X/\ell$ on any fixed interior target subwindow outside $O(X/\ell^2)$ even targets, uniformly in a common choice of floors. This is not a sign assertion for the sum with the composite-composite portion included.

There is also a separate sharp contrast at $a=b=41/2$, when these floors are in the box. Define $U^{\rm all,\mathbf u}$ to be the exact **uncurved completed containing product** with the original minus: within the enlarged carrier take the product of the two actual long containing sums, but do not apply the product test to this term. Let $U^{\rm comp,\mathbf u}$ restrict it to composite-composite, so $U^{\rm comp,\mathbf u}=W_{D_n}^{\rm comp,\mathbf u}$. With the actual collision constant $\mathfrak c$ of the split-free composite theorem,
$$
 \begin{aligned}
  \left\|U^{\rm all,(1,1)}
           +\frac{(1/2-\mathfrak c)^2}{\ell^2}I_N\right\|_{\ell^2(N)}
      &\ll X^{3/2}\ell^{-3},\\
  \left\|U^{\rm all,(1,1)}-U^{\rm comp,(1,1)}
           +\frac{1/4-\mathfrak c}{\ell^2}I_N\right\|_{\ell^2(N)}
      &\ll X^{3/2}\ell^{-3}.
 \end{aligned}                                                     \tag{2}
$$
Here $0<\mathfrak c\le(16/153)\log(7/5)<1/4$. Both actual quantities in (2) therefore have squared norm of order $X^3\ell^{-4}$ and are strictly negative of magnitude $\gg X/\ell^2$ on fixed interior target subwindows off $O(X/\ell^2)$ even targets. The correction of the uncurved completed containing product by the **forbidden retained-long product** remains exactly the composite-composite correction, and is not estimated in (2). Neither (1) nor (2) is an all-target sign or a claim about the complete Goldbach operator or Hypothesis S.

## 1. Exact wing insertion, including the literal cut

For a genuine operand $n=hF$, put
$$
 O_h=\sum_{\substack{r\mid h\\h/r>D_N}}\mu(h)\mu(r)\log(Fr),
 \qquad
 C_h=-\sum_{\substack{z\mid h\\Fz>D_N}}\mu(z)\log(h/z).
                                                                    \tag{3}
$$
The analogous $O_k,C_k$ are on the other arm. For a composite cofactor, the full containing sum is zero by $\Lambda(h)=0$, so the second sum in (3) equals the positive-signed nonlong residue $\sum_{Fz\le D_N,\ z\mid h}\mu(z)\log(h/z)$. For a wing, the ordinary divisors are $1,s<D_N$ for large $X$, $F=X e^{-O(T)}\gg\sqrt N$, and the fully containing label $Fs=n$ has mark zero. The only nonzero retained long mark is at $d=F$ and is $-\log s$. Thus $O_s=0$, $C_s=-\log s$ and $\mu(s)=-1$. All literal external floors hold on a wing for every allowed $a$.

For every opposite long label $e\ge D_N+1$,
$$
 Fe\ge F(D_N+1)>F\sqrt N e^{-20T_N}>N e^{-20T_N}\ge Q_N .
$$
Consequently no nonzero wing term can enter a forbidden retained-long product. This also applies if the orientation is reflected or if both arms are wings. On left wing/right composite the exact full weighted difference term is
$(-1)^{u_1}\log s\,\mu(k)^{u_2}(O_k+C_k)$;
on right wing/left composite it is the reflection. On two wings it is
$-(-1)^{u_1+u_2}\log s\log s'$.
These are disjoint and exhaustive, with the true exterior minus already included. In particular a wing is not a purported additional term in the vanishing $\Lambda(h)=0$ operation. The exact double-containing subrow with the product test is always its uncurved completed product plus its positive-signed forbidden retained-long correction as in the capped proof. In the difference of the two carriers that correction is identically zero, not merely small.

## 2. One actual wing with a single old prime

Let $e(t)=\exp(2\pi it)$, and adopt the auxiliaries of the [rational completion proof](r80-source-local-mean-square-at-sign-transition.md), §2: reduced $c/q$, $q\le P=L^C$, radius $1/(q\lfloor X/P\rfloor)$. Write $H(\theta)=(\mu(q)/\varphi(q))\widehat J(\beta)$ on such an arc, $\theta=c/q+\beta$, and zero off these arcs; $\widehat J(\beta)=\int_{\mathcal J}e(\beta x)\,dx$. The exponent $C$ is a sufficiently large fixed constant. Let
$$
 B(\theta)=\sum_{\substack{s\ {\rm old},\ F\ {\rm prime}\\sF\in\mathcal J}}
                      \log s\,e(\theta sF).
$$
For large $X$ every such $F>s$ and no floor can remove a term; this is the true squarefree canonical wing, with only the target-unit condition temporarily suppressed. We prove
$$
 \|H\|_4\ll X^{3/4},\qquad
 \left\| B-\frac{1}{2\ell}H\right\|_4\ll X^{3/4}\ell^{-2}.           \tag{4}
$$
For a reduced major numerator, apply Siegel–Walfisz in $F$ at fixed $s$; all occurring primes are greater than $P$, and multiplication by $s$ permutes the reduced residues. Partial summation on the literal hard interval $sF\in\mathcal J$ gives
$$
 B(c/q+\beta)=\frac{\mu(q)}{\varphi(q)}
      \int_{\mathcal J} e(\beta x)\sum_{s\ {\rm old}}
                                       \frac{\log s}{s\log(x/s)}\,dx
                  +O_D(XL^{-D}).
$$
Here $C$ is fixed first, then the Siegel–Walfisz exponent is increased for any fixed $D$; the oscillatory derivative costs at most $O(1+X|\beta|)\ll P$, and $\log(X/s)\asymp L$ uniformly. The ordinary prime number theorem and partial summation give $\sum_{s\ {\rm old}}\log s/s=T/2+O_D(TL^{-D})$. Since $\log(x/s)=L+O(T)$, the density on $\mathcal J$ differs from $1/(2\ell)$ by $O(\ell^{-2})$ in supremum and total variation, including its endpoint jumps. For the variation between endpoints use $|d/dx\,(\log(x/s))^{-1}|\ll1/(XL^2)$. Thus the real transform error is $O(\ell^{-2}\min(X,|\beta|^{-1}))$ with the same rational factor. The fourth moment uses $\int_{\mathbb R}\min(X,|\beta|^{-1})^4d\beta\ll X^3$ and $\sum_q\mu(q)^4/\varphi(q)^3<\infty$. The discrete errors on the arcs also give a negligible fourth norm, since their total measure is $O(P^2/X)$ and $D$ is arbitrary after $C$ is fixed.

The wing's very unequal factors require a separate minor check. Keep both hard physical endpoints by subtracting upper cutoff sums and take their height-$X^4$ Perron integrals, with a half-integer separating each actual integer cutoff. This contributes polylogarithmic overhead and negligible truncation: distinct integers are at least $1/2$ from a shifted endpoint, and all determining products are $\asymp X$ on dyads meeting the physical window. The separated factor powers at real part $1/L$ and arbitrary imaginary parts leave coefficients bounded by $L^{O(1)}$. On each dyad write $s\asymp M_0,\ F\asymp K_0,\ M_0K_0\asymp X$; both lengths exceed all fixed powers of $L$. For arbitrary such bounded coefficients Cauchy in $s$, followed by expansion of the square in $F$, bounds the squared bilinear sum by
$$
 X L^{O(1)}
       \sum_{|j|\ll K_0}\min(M_0,\|j\theta\|^{-1})
 \ll X L^{O(1)}(1+K_0/q)(M_0+q\log(2q)).
\tag{5}
$$
The zero term uses the value $M_0$. For the second bound use a reduced approximant $|\theta-c/q|\le1/q^2$; on blocks of consecutive $j$ of size at most $q/2$ their phases are mutually separated by at least $1/(2q)$, by applying the rational approximation to their pairwise differences. Sum the reciprocals of the ordered distances to zero on a block, with the nearest point capped by $M_0$. Dirichlet on the complementary arcs gives $P<q\le\lfloor X/P\rfloor$, so after division by $X^2$ the right side is at most
$$
 L^{O(1)}
  \left(\frac1q+\frac1{K_0}+\frac{\log(2q)}{M_0}
                    +\frac{q\log(2q)}{X}\right).
$$
Take $C$ large for any fixed desired minor saving, absorbing the Perron and dyadic losses. This gives a supremum $O_D(XL^{-D})$ for the chosen sufficient $C$ on the minors. Finally $\|B\|_2\ll\sqrt X L$, since factorization as $sF$ is unique. Hence the minor fourth norm follows by $\int_{\mathfrak m}|B|^4\le\sup_{\mathfrak m}|B|^2\,\|B\|_2^2$. This establishes (4) without using a balanced-only minor estimate.

## 3. Composite mate matching and the full increment

We record the two one-arm scalar comparisons needed to use (4), rather than inferring them from a two-arm target bound. Temporarily put the mate prime floor at $\sqrt X e^{-bT}$ and the long cutoff at $D_*=\sqrt X e^{-20T}$, with the same strict and weak inequalities at these fixed thresholds, and suppress target-unit restrictions. Let $P_b^{(u)}$ and $C_b^{(u)}$ be the ordinary and containing Fourier polynomials on the true canonical composite support, using (3), the actual nonlong residue for $C$, and the factor $\mu(k)^u$. In the convention of (4) they satisfy
$$
 \begin{aligned}
 \|P_b^{(u)}-\mathbf1_{u=1}\kappa_X M(b+20)H\|_4
      &\ll X^{3/4}\ell^{-1},\\
 \|C_b^{(u)}-\mathbf1_{u=0}\kappa_X M(b-20)H\|_4
      &\ll X^{3/4}\ell^{-1}.
 \end{aligned}                                                     \tag{6}
$$
Here the two intrinsic full signs are different. The ordinary mark contains $\mu(k)$; the nonlong residue does not. Thus in each nonmatching case there is exactly one full sign on the arm. Summing the split-free proof's single-bin fourth bounds over the allowed normalized bin coordinate at fixed floor gives its unbinned $O(X^{3/4}/\ell)$ bound, also when the fixed long endpoint clips a bin. Equivalently the compact signed Dickman density there is negligible in the rooted comparison, and restoring the removed roots costs $O(X^{3/4}/\ell)$.

For matching, the real-density calculation of that same proof applies unbinned; the shapes can be read directly. Fix the old prime and the short prime block up to $\exp(AT)$ containing every possible actual label. Fix a label of coordinate $t=\log r/T$ or $t=\log z/T$ and set $\alpha=(L/2-\log G)/T$ and $x=kG$. Ordinary $k/r>D_*$ clips $\alpha$ below by $t-20-(\log x-L)/T$, whereas containing $Gz\le D_*$ clips it below by $20+t$. Its upper bound is $b$ in both cases. No fixed upper comparison of $G$ can remove positive length: for ordinary the consequence $G<x/D_*$ follows from $k/r>D_*$ and $r\ge1$; in the containing case $G\le D_*$. Thus lengths are $(b+20-t)_+$ and $(b-20-t)_+$ up to $O(1/T)$. Keep physical $x\in\mathcal J$ hard. The Jacobian is $d\alpha/\ell$ in the normalized cofactor argument. Both bare mark ratios $\log(Gr)/\log G$ and $\log(k/z)/\log G$ equal $1+O(\ell^{-1})$ throughout these active compact windows. As in the [one-arm real calibration](r103-source-canonical-size-free-real-upper-factor.md), §2, the residual positive rough density is $O(\ell)$ and compact Lipschitz with constant $O(\ell)$, the fixed short block has bounded positive labeled reciprocal mass and mean log displacement $O(T)$, and its far displacement (including any atom) is exponentially small in $\ell$. Replacing the active density argument by $1/2-\log s/L$ therefore costs $O(\ell^{-1})$ after the Jacobian. These bounds also control the total variation error in $x$: the translated endpoint has movement at most $O(|x-y|/(XT))$, and the other bare factors and density on a common interval vary on normalized scale $O(|x-y|/(XL))$ after accounting for their sizes. The fixed window jumps cost the supremum error.

For clarity, at an eligible low prime $p$ other than $s$, the fixed positive reciprocal factor $1+1/p$ leaves a signed label coefficient $-1/(p+1)$ at position $\log p/T$; this follows by separating the case where $p$ is in the label. At the old prime the exact label factor is $\delta_0-\delta_{\log s/T}$. The ordinary and residue labels both carry these very short signs. Reciprocal PNT and reciprocal-square errors give $\exp_*(-\mathbf1_{[4,A]}dt/t)$ for the former factors on the fixed support. For $s$, replacing the weighted short displacement law by $\pi$ costs $O(\ell^{-1})$ after the Jacobian: the argument of the compact positive density varies by $O(T/L)$ across the old band, and its normalized Lipschitz bound is $O(1)$. The independent positive product from the peeled band has mass $A/4+O_D(L^{-D})$ and mean displacement $O(\ell^{-1})$ on the normalized log scale. Convolving that product back into the residual density changes the real factor only by $O(\ell^{-1})$ after multiplication by $1/\ell$, and gives exactly the calibration (1) of the composite theorem divided by $|\mathcal J|$. This proves the stated matching scalars $M(b+20)$ and $M(b-20)$, with the same $\kappa_X$ on either arm, not a second choice of normalization.

The discrete major errors and minor cancellations are those of the split-free proof, or may be summed over its $O(\ell^3)$ bins with a larger fixed log precision. The real supremum and variation errors just checked cost $O(X^{3/4}/\ell)$ in fourth norm, and the unsigned veto correction restoring canonical roots also costs $O(X^{3/4}/\ell)$ before any product. This proves (6). The two actual thresholds can differ from their fixed versions only in log-width-$O(1)$ slivers on the prime floor or divisor line, including equality at the integer cutoff. On either such sliver the positive rooted one-arm bound of the composite proof is $O(X^{3/4}/T)$: the normalized interval width is $O(1/T)$ at a fixed label, the positive density has size $O(\ell)$ and Jacobian $1/\ell$, and hard arc errors are negligible as before. The ordinary shifted $x$ endpoint also changes by at most $O(1)$ in log. Domination by the whole positive marked arm and by $B$ therefore allows literal target restoration inside the product at norm $O(X^{3/2}/(T\ell))$. A suppressed target-nonunit is negligible by the shared-prime multiple estimate: each offending prime is at least $e^{5T/4}$, divides $N$, and permits $O(X/p+1)$ operands; there are $O(\ell)$ such primes, and the marks and active label multiplicity cost only fixed powers of $L$. This is a bound on the actual overlap terms at each target, not removal of a local factor in the rational comparator.

By Hölder and Parseval, (4) and (6) give the Fourier coefficient of $H^2$ times the sum of the two wing/mate scalars with norm error $O(X^{3/2}\ell^{-2})$. The both-wing product costs $O(X^{3/2}\ell^{-2})$ here. The coefficient of $H^2$ is $I_N+O_{\ell^2(N)}(X^{3/2}L^{-D})$ for desired fixed $D$ by the original rational completion: sum the reduced numerators first, then use the summable bound $\|c_q(N)\|_2/\varphi(q)^2\ll_\epsilon\sqrt X q^{-3/2+\epsilon}$ for squarefree $q$, and extend the real beta integral and $q$ series with the stated finite-arc tails. The full beta integral is exactly the physical overlap $B_{\mathcal J}$. Keeping the signs from Section 1 proves (1).

For $x>0$ the cumulative of the signed reciprocal exponential at $y\ge0$ is $\rho(y/4)$ up to its unused truncation, by the Dickman law. Integration of cumulatives thus gives
$$
 M(x)=\int\pi(dt)\int_{(x-t)_+}^x \rho(v/4)\,dv>0 .
\tag{7}
$$
For $\mathbf u=(1,1)$, $K_{\mathbf u}=-M(b+20)-M(a+20)$, bounded away from zero negatively on the compact floor box. On each fixed interior target subwindow $I_N\gg X$ for every even target and $\kappa_X\asymp1$; compare (1) at threshold a fixed small multiple of $X/\ell$ by Chebyshev. This proves the stated sign and exceptional size. It requires no pointwise upper bound for $\Sigma(N)$.

## 4. The two-full-sign collision after insertion

Set $a=b=41/2$, use actual bits $(1,1)$, and consider just the containing traces. On the composite side the only possible nonlong label is one because $Fz\le D_N$ and the actual floor imply $z\le e^{T_N/2}$, below every genuinely allowed cofactor prime for large $X$. The detailed one-arm calculation in the split-free composite theorem, §2, accordingly gives
$$
        \|C_{41/2}^{(1)}+(\mathfrak c/\ell)H\|_4
                              \ll X^{3/4}\ell^{-2}.                \tag{8}
$$
In fact that proof shows the rooted full-sign arm is negligible, the strict rejected-root arm with $F<P$ has real transform $(\mathfrak c/\ell)H$ plus error of precisely this scale, and the repeated root is negligible. The strict rejection has genuine $\mu(h)=\mu(W)$ on $h=sWP$, and the cofactor $P>F$ is unique; the leading sign for the actual canonical arm is negative. This uses the upper $F\le D_N$ cut and the actual lower floor via the already bounded slivers, not a new larger prime interval. On a wing the actual long mark times $\mu(s)$ is $+\log s$, so its model is $+(1/(2\ell))H$ by (4). In particular the completing wing has the opposite per-arm sign, not another collision veto. The exact uncurved containing product still has the common exterior minus.

Multiply the actual arm $C_{41/2}^{(1)}+B$ by itself with the exterior minus. Its difference from the model $-(1/2-\mathfrak c)^2H^2/\ell^2$ has coefficient norm $O(X^{3/2}\ell^{-3})$ by Hölder and Parseval. For the composite-only analogue use $-(C_{41/2}^{(1)})^2$ with comparator $-\mathfrak c^2H^2/\ell^2$. The two sums after restoration have precisely the original target-unit restrictions and both true floors and long cuts; the positive sliver estimate multiplied by the bounded whole mate remains negligible here, as $1/T$ is smaller than every fixed negative power of $\ell$. Use the same rational completion as in Section 3 and subtract the two formulas. This proves both bounds in (2).

For the numerical inequality $(2u-t)/4\ge153/16>1$ on the integral defining $\mathfrak c$, and the Dickman identity $v\rho(v)=\int_{v-1}^v\rho(w)\,dw$ gives $\rho(v)\le1/v$. Since $2(41/2-20)=1$, the claimed upper bound follows; $\rho$ is strictly positive at finite positive arguments so $\mathfrak c>0$. The same lower and upper $\ell^2$ control of $I_N$ as in the split-free theorem and Chebyshev at scale $X/\ell^2$ prove the final sharp sizes and signs. All these comparisons concern the actual wing increment or actual uncurved containing terms only. In particular the retained-long forbidden product, though unchanged by the wing enlargement, must still be added for the complete curved containing row.
