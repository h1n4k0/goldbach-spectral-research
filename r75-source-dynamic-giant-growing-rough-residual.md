# The dynamic giant carrier with an actual growing rough residual

Use the hard central sum and the true moving cuts of the [wide curved carrier](r74-source-full-curved-two-giant-mean-square.md). The scale $X$ is real and large, $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\theta=1/20$, and $\epsilon=1/64$. Fix $0<\rho<1/2$ and the same $\Delta<1/10$ with $1/(2(1+\Delta))>\rho$. Set $\mathcal J=[X/2,(1+\Delta)X/2]$, $\mathcal X=[X,(1+\Delta)X]$. At scale $X$ use the prime exclusions and exceptional cutoff of the [typical-count construction](r72-source-typical-count-masked-obstruction.md):

$$
 V_X=\exp(T\ell^\theta),\quad
 J_X=\left\lfloor\frac{\log\ell}{\log\log\ell}\right\rfloor,\quad
 Y_{*,X}=\exp\!\left(\frac{L}{64(J_X+1)}\right),\qquad
 [V_X/2,2V_X]\ \cup\ [Y_{*,X}^{1/2},Y_{*,X}^2].
 \tag{1}
$$

Choose any real split $Z$ with $V_X^2\le Z\le X^{\delta_0}$, where $\delta_0>0$ is a sufficiently small fixed constant, for example the constant at the top of the old $W$ alphabet. Write $\tau=\log Z/L$. On each leg take a genuine integer $n=hF\in\mathcal J$ with $F$ prime, $F>\sqrt N$ at the **actual** target, and

- $h=sWU$, with $s$ one prime in $[\exp(5T/4),\exp(7T/4)]$;
- $W$ a squarefree product of primes in $[\exp(4T),Z]$ outside the excluded neighborhoods (1), with the same old hard gates $W\le X^{\epsilon/2}$ and $\omega(W)\le2\log\ell$;
- $U>1$ any squarefree product of primes $>Z$ outside the same neighborhoods. There is no imposed arity bound on $U$.

The true exceptional count is the number of prime factors of **$WU$**, not of $W$ alone, in $(V_N,Y_{*,N})$. Require this count to be within $2(\log\ell)^{3/4}$ of $(1-\theta)\log\ell$, as before. Both parities are admitted. As in the typical-count construction, after the exclusions (1) the exceptional count of any such product is the fixed count in $(2V_X,Y_{*,X}^{1/2})$ for every $N\in\mathcal X$. Indeed the $V$ endpoint changes relatively by $1+o(1)$ and the logarithm of the upper endpoint by a ratio $1+o(1)$ even across the floor of $J_N$. All exceptional counts in the Fourier constructions below are these exact fixed counts.

Both operands in the signed sum must be squarefree $N$-units and lie on $n+m=N$, with $I=I_0$ as before. There is **no fixed $h$ window** in the statement: all the allowed $h$ under $F>\sqrt N$ are included, as are all genuine divisor pairs satisfying $d>D_N,e>D_N,de>Q_N$. Denote that sum, with the unchanged external minus sign of the [joint count theorem](r72-source-joint-middle-count-entropy.md), by $R_{N,Z}^{\rm giant}$.

**Theorem (unconditional).** Uniformly in this range of $Z$,

$$
       \sum_{\substack{N\in\mathcal X\\2\mid N}}
                  |R_{N,Z}^{\rm giant}|^2\ll_\rho X^3\ell^{-2/5}.
 \tag{2}
$$

In particular $Z=V_X^2$ allows a superlogarithmic but subpower lower cutoff and a genuinely growing number of upper rough factors, some of which can supply the exact exceptional count. As before, the number of targets with magnitude exceeding $X\ell^{-1/10}$ is $O_\rho(X\ell^{-1/5})$. This is a mean-square theorem for the prescribed giant carrier, not for arbitrary outer masks, no-giant pairs, the unrestricted central sum, or Hypothesis S.

## 1. The exact giant calculation and the fixed Fourier carriers

For a true pair the complete labels containing $F$ pass against every opposite long label, since $F(D_N+1)>\sqrt N(D_N+1)>Q_N$. Their sum is $-\Lambda(h)=0$ because $h$ is squarefree with at least the two distinct factors $s$ and a prime of $U$. Eliminate the other giant family in the same way. The true surviving labels are $d=h/b$, $e=k/c$ with $b\mid h,c\mid k$, exact three moving tests, weights $\log(Fb)\log(Gc)$, and signs $-\mu(h)\mu(k)\mu(b)\mu(c)$.

If $h\le D_N$ or $k\le D_N$ the remainder vanishes. Thus we may put both cofactors above $H_-=\tfrac12\sqrt X e^{-20T}$: this is below $D_N$ throughout the window for large $X$. The true giant condition gives $h,k\le H_{\rm top}=(1+\Delta)\sqrt X/2$. Also $bc<hk/Q_N\le M=\exp(21T)$ for every retained label pair. In particular $b\mid sW$ and $c$ lies in the analogous product, since $Z\gg M$. Because every prime in a label is at least $\exp(5T/4)$ and the true $\omega(W)$ is bounded, there are $O((1+\log\ell)^{17})$ labels per operand, regardless of $\omega(U)$. The parity multiplier on one leg is exactly $\mu(h)=-(-1)^{\omega(W)}(-1)^{\omega(U)}$.

For the Fourier polynomials we use fixed $h$ windows inside $[H_-,H_{\rm top}]$, with $hF\in\mathcal J$ and prime $F$, imposing the genuine $s,W,U$ gates. Wherever $h\le H_+=\sqrt X/4$, $F$ is automatically giant for all targets. Above that, some comparisons will positively enlarge the actual dynamic giant constraint. Even on that enlargement $F\ge\sqrt X/(1+\Delta)>H_{\rm top}$, so $F$ is the unique largest prime, and the split $h=sWU$ is unique by its disjoint prime alphabets. Also $S=sW\le X^\epsilon$ and $\log U/L$ lies in $[.4,.6]$ for large $X$. All original integer-label tests are used in the true sum before comparisons on this fixed carrier.

Removing the unit condition from a convolution on this carrier costs individually $O_A(XL^{-A})$ for every fixed $A$. Any nonunit pair has a common prime $p\mid N$ with $p\ge\exp(5T/4)$, there are $O(\ell)$ such divisors of $N$, and there are only $O(X/p)$ possible first operands per prime. The bounded logarithmic weights and the stated label multiplicities are absorbed. This argument also covers the actual positive enlargements involving the top sliver.

## 2. A count-restricted reciprocal density for the upper rough product

The available upper primes in a Fourier comparison can be restricted to $p\le X^{.7}$ without changing any tuple: $U\le h\le H_{\rm top}$. In normalized logarithmic coordinates let $I_{\rm t}$ be the tagged interval of these allowed upper primes and $I_{\rm f}$ the free interval. Explicitly the former is $(\tau,(\log Y_{*,X})/(2L))$ if it is nonempty, and the latter starts at $\max(\tau,2\log Y_{*,X}/L)$ and ends at $.7$. Endpoint conventions match the prime exclusions and the strict split at $Z$; they have no effect on their real measures. The lower neighborhood at $V_X$ lies below $Z$. A tag for $U$ therefore reports genuine membership in the actual exceptional band. For a fixed $W$, let $K$ be the set of allowed upper tag counts after subtracting the actual tagged count of $W$. Nothing here averages the integer count.

Write $g_{\rm t}(t)=\mathbf1_{I_{\rm t}}(t)/t$, $g_{\rm f}(t)=\mathbf1_{I_{\rm f}}(t)/t$, and for $\zeta=1$ or $-1$ define the finite-mass real measure

$$
 A_{\zeta,K}
   =\sum_{\substack{j\ge0,\ j\in K\\k\ge0}}
       \frac{\zeta^{j+k}}{j!\,k!}\,g_{\rm t}^{*j}*g_{\rm f}^{*k}.
 \tag{3}
$$

Convolution-zero powers mean the unit atom at zero. Away from zero let $\varrho_{\zeta,K}$ denote its density. We use the following two uniform properties.

First, for any hard log interval in $[.4,.6]$, integration against $A_{\zeta,K}$ replaces the actual squarefree reciprocal $U$ sum with precisely the weights $\zeta^{\omega(U)}/U$ and the permitted count $K$, to error $O_A(L^{-A})$ for any fixed $A$. The same holds for a bounded-variation mark of uniformly bounded supremum plus variation supported on this interval. To verify it, expand in ordered prime tuples by arity with factorial divisors. For any fixed values of the other coordinates, the allowed interval for the current coordinate is intersected with at most the two tagged/free intervals, and the translated mark has uniformly bounded variation. The ordinary PNT and partial summation for the reciprocal prime measure replace it by $dt/t$ with arbitrary inverse logarithmic error. This is uniform since the smallest $\log p$ is at least $\tau L\ge 2T\ell^\theta$. If $H$ bounds both total continuous and discrete reciprocal prime mass, $H\le\log(1/\tau)+O(1)$, the telescoping errors per arity sum absolutely to $O_A(L^{-A}e^H)$ before increasing the fixed PNT exponent: the combinatorial upper sum is
$\sum_{r\ge1} rH^{r-1}/r!=e^H$. Dropping distinctness during this replacement costs at most
$O(e^H\sum_{p>Z}p^{-2})$ by marking an equal pair in the initially ordered discrete tuples. All these are still arbitrary inverse log powers, because $\tau^{-1}\ll\ell^{1-\theta}$ and $Z$ is superpolynomial in $L$. The argument is uniform in the allowed set $K$, including an empty set.

Second, on $[.4,.6]$ there is a Lipschitz representative satisfying

$$
 \|\varrho_{\zeta,K}\|_\infty+
           \operatorname{Lip}(\varrho_{\zeta,K})\ll \tau^{-1}.
 \tag{4}
$$

Indeed the total variation of (3) is dominated by $A_{1,\mathbb Z_{\ge0}}$, whose mass is at most $e^{\int(g_{\rm t}+g_{\rm f})}\ll\tau^{-1}$. Marking one coordinate in the identity $z=\sum t_i$ in each convolution gives, as densities for $z>0$,

$$
 z\varrho_{\zeta,K}(z)
   =\zeta\bigl(\mathbf1_{I_{\rm t}}*A_{\zeta,K-1}
                 +\mathbf1_{I_{\rm f}}*A_{\zeta,K}\bigr)(z),
 \quad K-1=\{j-1:j\in K,\ j\ge1\}.
 \tag{5}
$$

The factorials give one copy of the tagged or free marked coordinate, and multiplication by its coordinate converts $g$ to the interval indicator. This first gives a bound $O(\tau^{-1})$ on the densities for $z\ge .3$. Differentiate the right-hand side in the sense of distributions: interval indicators give the difference of their endpoint shifts. All endpoints except $.7$ are $\le \max(\delta_0,2\log Y_{*,X}/L)=o(1)+O(\delta_0)$, so on $[.4,.6]$ those shifts meet the bounded density range. The $.7$ shift has negative argument there. The only possible atom, at zero, shifts outside that compact region. The weak derivative is therefore bounded by $O(\tau^{-1})$; divide by $z$ to get (4). This proves the claim even with an arbitrary selected count set and either sign. In particular no smooth approximation to the exceptional count is being substituted.

## 3. Bin density bounds with the actual logarithmic mark

For a fixed hard $h$ window $\mathcal H\subseteq[H_-,H_{\rm top}]$ and a hard log-label bin $J$, form the signed and positive polynomials exactly as in the wide curved theorem: sum over actual $h=sWU\in\mathcal H$, $b\mid sW$ with $b\le M$ and $\log(h/b)\in J$, and prime $F$ with $hF\in\mathcal J$; the positive mark is $\log F+\log b$, and the signed mark is multiplied by $\mu(h)\mu(b)$. If all labels are to be used simply omit the test in $J$. Let $\mathcal D$ be a bound for the logarithmic length of $[H_-,H_{\rm top}]\cap\mathcal H\cap b\exp(J)$ for each fixed $b$; use the corresponding expression without $J$ if omitted. We will use $\mathcal D=T/\ell$, $O(T)$ or $O(1)$. Throughout, the true factor and count gates are imposed on each polynomial.

A positive $s,W,b$ profile is $O_\rho(\ell\tau)$ for the weight $1/(sW)$, with the choices of $b$ counted. This follows as in the wide curved proof by allowing each prime of $W$ with $p\le M$ weight $\nu_p=2$, others weight $\nu_p=1$, and allowing at most two choices for $s$ to appear in $b$. The doubling affects only primes of bounded reciprocal mass in $[\exp(4T),M]$. Mertens gives $\prod(1+\nu_p/p)\ll\log Z/(4T)\ll\ell\tau$. It also shows that, under this normalized positive profile, the mean number of $W$ primes is at most $\log\ell+O(1)$ and the moment of $2^{\omega(W)}$ is $O(\ell)$. Multiplying the profile by (4) and integrating in $d(\log h/L)$ over length at most $\mathcal D/L$ gives the uniform positive reciprocal label bound $O_\rho(\ell\mathcal D/L)$; the arbitrary inverse logarithmic replacement error in §2 is negligible.

On the same arcs as the wide curved theorem, apply Siegel–Walfisz only in the prime $F$ with both weights $1$ and $\log F$. The complete reduced residues give $\mu(q)$ because all prime factors of $h$ exceed the polylogarithmic denominators. The hard $F$ interval $\mathcal J/h$ and the slow phase cost bounded interval variation times a fixed power of $L$, with an arbitrary inverse logarithmic error remaining. As in that theorem the actual major approximation is

$$
 \frac{\mu(q)}{\varphi(q)}\int_{\mathcal J}e(\beta x)D^\pm(x)\,dx
                                      +O_{\rho,A}(XL^{-A}),
 \qquad
      K_x(h,b)=1+\frac{\log b}{\log(x/h)},
 \tag{6}
$$

where the exact finite density $D^\pm(x)$ sums $K_x(h,b)/h$ over the indicated actual $h,b$, with the corresponding signs. The term $\log b/\log(x/h)$ comes from the unweighted prime $F$ density; this keeps the actual $\log(Fb)$. Suppressing signs gives at once
$|D^+(x)|+X|\partial_xD^+(x)|\ll_\rho \ell\mathcal D/L$.

For the signed density, apply §2 for fixed $s,W,b$ and the exact relevant $K$. The mark $K_x(h,b)$ or $X\partial_x K_x(h,b)$ has uniformly bounded supremum and variation in the relevant hard $h$ interval. After changing variables to $v=\log h/L$, the real integral has mark $K_x(h,b)$ times $\varrho_{-1,K}(v-\log(sW)/L)\,dv$ and the separate weight $1/(sW)$, with the signs from $s,W,b$. This replaces only the real density in (6). The product-support width is at most $\mathcal D/L$, independent of $W$ for fixed $b$. The accumulated PNT error using the positive label profile is negligible.

Factor $W=W_0W_1$, with all primes of $W_0$ in $[\exp(22T),V_X/4]$. They belong to the old $W$ alphabet for every allowed $Z$, lie above $M$, and do not affect any actual exceptional count. Thus both $K$ and $b\mid sW$ depend only on $s,W_1$; the latter restriction is exactly $b\mid sW_1$. First replace the old total arity gate by the temporary $\omega(W_0)\le3\log\ell$ inside this real estimate. The replacement affects a relative mass $O(\ell^{-(2\log2-1)})$ by the preceding moment bound in the positive $\nu$ profile, even after all label multipliers are allowed. The density bound (4) makes its total error $O((\ell\mathcal D/L)\ell^{-(2\log2-1)})$.

On this temporary support $\log W_0\le\Delta_0=3(\log\ell)\log V_X=o(L)$. Replace the density argument by $v-\log(sW_1)/L$. The arguments stay in the fixed compact range, so the Lipschitz bound (4) costs a relative $O(\Delta_0/L)$ with respect to $\ell\mathcal D/L$. Replacing the hard $W_0W_1$ product gate by the $W_1$ gate alone produces the size strip of width $\Delta_0$ below $\epsilon L/2$. Its weighted relative mass is $O((1+\Delta_0)/L)$ as in the wide curved theorem: since $\log W_1\gg L$, mark a constituent prime with weight $\log p$ by expanding $\log W_1$, freeze all other factors, and use $\sum \nu_p\log p/p=O(1+\Delta_0)$ in the resulting log interval by Chebyshev. This argument does not alter the actual count selector in $K$. Both errors also bound the scaled derivative in $x$, since that only differentiates $K_x$.

Now remove the temporary cap of $W_0$ at the same positive moment error and factor its signed reciprocal product. It gives the ratio $\prod(1-1/p)/\prod(1+1/p)\ll\ell^{-2\theta}$, since the indicated band has reciprocal prime mass $\theta\log\ell+O(1)$. No other remaining restriction uses $W_0$. Using $\Delta_0/L\ll\ell^{-1+\theta}(1+\log\ell)$ and $2\theta=1/10$ proves

$$
 |D^-(x)|+X|\partial_xD^-(x)|\ll_\rho
                     (\ell\mathcal D/L)\ell^{-1/10}.
 \tag{7}
$$

This is uniform in the actual split and the allowed count function $K$ used at each $W_1$. No assumption about the sign or a lower bound for the rough density was made.

On the minors the same bilinear estimate, hard half-integer Perron separation of $hF\in\mathcal J$, and dyads from the wide curved theorem apply. Here $h,F\le X^{.6}$ on all relevant rectangles. The factorization $h=sWU$ is unique; the pointwise coefficient bound after splitting $\log F+\log b$ is $O(L(1+\log\ell)^{17})$ in product across the two variables, with no loss from the arity of $U$. Thus one can take $\sup_{\mathfrak m}|\mathcal B^\pm|\ll_K XL^{-K}$ for any desired fixed $K$ by choosing the fixed polylogarithmic arc exponent large enough. Parseval gives ordinary coefficient square norm at most $O(X L^2(1+\log\ell)^{34})$. The minor fourth means are superlogarithmically small relative to $X^3$. On the majors, (6), the bounds on the magnitude and variation of the real density, and $\sum_q\mu(q)^4/\varphi(q)^3<\infty$ give the fourth-mean bounds

$$
 \int_0^1|\mathcal B^+|^4\ll_\rho X^3(\ell\mathcal D/L)^4,
 \qquad
 \int_0^1|\mathcal B^-|^4\ll_\rho
                   X^3\bigl((\ell\mathcal D/L)\ell^{-1/10}\bigr)^4 .
 \tag{8}
$$

In particular these hold for the three specified widths; the major uniform substitution errors are negligible because the arc measure is $O(L^{2C}/X)$ for fixed $C$. Integration by parts on the fixed real physical interval gives the same $\min(X,|\beta|^{-1})$ transforms after multiplying the indicated density bounds.

## 4. The bulk, the dynamic sliver and the true moving seams

On the fixed bulk $H_-\le h,k\le H_+$ both giants pass for all targets. Partition the log labels into the same $O(\ell)$ bins of width $L/\ell^2$ as in the wide curved proof. All three original strict cuts are used: the ranges of $\log D_N,\log Q_N$ over the scale are $O(1)$, so accepted bin pairs have all their labels truly accepted, rejected pairs none, and only $O(\ell)$ ambiguous pairs are left by the two single-coordinate seams and the curved sum seam. Reconstruct the accepted contribution as the sum of true signed convolutions from (8), and majorize the remaining exact terms only in absolute value by the associated positive convolutions. Per signed pair the $\ell^2(N)$ norm is $O_\rho(X^{3/2}\ell^{-11/5})$ by Hölder and Parseval; per positive pair it is $O_\rho(X^{3/2}\ell^{-2})$. Summing at most $O(\ell^2)$ of the former and $O(\ell)$ of the latter gives norm $O_\rho(X^{3/2}\ell^{-1/5})$. This uses the actual curved test, not a fixed-target approximation on the seams.

If either $h$ or $k$ lies in the top sliver $H_+< h\le H_{\rm top}$, use a positive comparison only after the true giant-orbit identity in §1. The sliver has log width $O(1)$, so its all-label fourth mean in (8) is $O_\rho(X^3(\ell/L)^4)$. The whole opposite window and all labels have log width $O(T)$ and positive fourth mean $O_\rho(X^3)$. By Hölder and Parseval the convolution norm is $O_\rho(X^{3/2}\ell/L)=O_\rho(X^{3/2}/T)$. This dominates the corresponding terms with the actual dynamic giant restriction on the sliver; there is no extra extrapolation to targets where the selected prime is not giant. Sum the two orientations. After the negligible individual unit comparison, the full norm is $O_\rho(X^{3/2}\ell^{-1/5})$. This proves (2).

## 5. An actual growing-arity example

Set $Z=V_X^2$. Take one old lower prime per leg near $\exp(3T/2)$ and $W=1$. Take on each side $\lfloor(1-\theta)\log\ell\rfloor$ distinct prime factors of $U$ near $\exp(3T\ell^\theta)$, all above $Z$ and in the interior of the true exceptional interval. Their product has log size $O(T\ell^\theta\log\ell)=o(L)$. Choose one further prime factor in each $U$ by the PNT so that $h,k$ are in fixed small proportional windows around $\sqrt{Q_X}\exp(6T/5)$, and take distinct primes $F,G$ placing the two integers in $\mathcal J$. The latter are true giants. All primes across the two operands can be chosen distinct, giving genuine central units and an even target. The complete exceptional count is supplied by $U$, which has genuinely growing arity and is not the single-prime cofactor of the preceding theorem.

The only omitted labels on the two sides are $1,s$ and $1,t$. All four choices pass the individual long tests, while exactly the pair $(s,t)$ fails the curved product test, as in the [wide curved example](r74-source-full-curved-two-giant-mean-square.md). The two parities agree, so the remaining actual mark is $\log F\log G+\log s\log G+\log F\log t\ne0$. The top sliver is occupied too: with the same small products choose $h,k$ near $.40\sqrt X$ instead, placing the operands in $\mathcal J$ with true giants; all four pairs then pass and the signed mark is $-\log s\log t\ne0$. Neither example asserts an aggregate lower bound.
