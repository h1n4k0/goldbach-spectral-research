# The actual forbidden correction and the sign of the curved containing row

Keep the [actual semiprime-wing enlargement](r105-source-semiprime-wing-and-containing-contrast.md), with exactly the same hard physical window $\mathcal J$, even targets $\mathcal X$, $L=\log X$, $\ell=\log L$, $T=L/\ell$, and $T_N=\log N/\log\log N$. In particular the operands $n=hF,m=kG$ are true squarefree $N$-units, $F=P^+(n),G=P^+(m)$, and each cofactor is $sV$ with $5T/4\le\log s\le7T/4$ and $V$ squarefree with all primes at least $e^{4T}$. The wing $V=1$ is admitted in the final curved row. Fix both common floors at **$a=b=41/2$**. Keep the literal floor inequality on $F,G$, and the actual integer thresholds $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$, $Q_N=\lfloor Ne^{-20T_N}\rfloor$. No test is chosen separately at different targets.

Write $I_N=\Sigma(N)B_{\mathcal J}(N)$, the same singular series and exact physical overlap. Let $V_f(N)$ denote the actual forbidden retained-long correction on **two composite cofactors** in the two-full Walsh channel. Explicitly, on each such pair its contribution is
$$
 \mu(h)\mu(k)
 \sum_{\substack{z\mid h,\ w\mid k\\Fz>D_N,\ Gw>D_N\\(Fz)(Gw)\le Q_N}}
            \mu(z)\mu(w)\log(h/z)\log(k/w).
 \tag{1}
$$
This is the positive-signed correction in the [exact containing orbit algebra](r85-source-capped-long-floor-orbits.md), with the actual inserted full signs; it is not asserted to be nonnegative. Define $V_{\rm curv}(N)$ to be the genuine containing-containing portion on the **enlarged** carrier (including the wings): both long tests and the original strict product test apply, with the original exterior minus and actual Walsh weight $\mu(h)\mu(k)$. It includes no ordinary divisor arms.

For a finite positive real measure define $\mathcal P=\exp_*(\mathbf1_{[4,42]}(y)\,dy/y)$, including its unit atom at zero, with $\exp_*(\lambda)=\sum_{j\ge0}\lambda^{*j}/j!$. Let $\rho$ be the continuous Dickman function and write $\rho_+(v)=\mathbf1_{v\ge0}\rho(v)$, extending by zero to negative arguments. For $0\le g\le20$ put
$$
 \begin{split}
 C(g)=2\int_{5/4}^{7/4}\frac{dt}{t}\int d\mathcal P(\eta)
 \bigg\{&
  \mathbf1_{g+\eta\le41/2}\rho_+\!\left(\frac{2g+\eta-t}{4}\right)\\[-1mm]
  &-\mathbf1_{g+\eta+t\le41/2}\rho_+\!\left(\frac{2g+\eta+t}{4}\right)\bigg\},\\
 \mathfrak f&=\iint_{\substack{0\le g,g'\le20\\g+g'\ge20}}
                                  C(g)C(g')\,dg\,dg'.
 \end{split}
 \tag{2}
$$
Endpoint assignments on a null set do not affect either real integral. Denote by $\mathfrak c$ the actual nonlong collision constant of the [composite collision calculation](r104-source-split-free-composite-collision-law.md), (2).

**Theorem (unconditional).** The actual correction (1) and the actual curved containing-containing term have the two mean-square asymptotics
$$
 \left\|V_f-\frac{\mathfrak f}{\ell^2}I_N\right\|_{\ell^2(N)}
                    \ll X^{3/2}\ell^{-3},\qquad
 \left\|V_{\rm curv}
          +\frac{(1/2-\mathfrak c)^2-\mathfrak f}{\ell^2}I_N
             \right\|_{\ell^2(N)}
                    \ll X^{3/2}\ell^{-3}.
 \tag{3}
$$
The first coefficient satisfies the rigorous bound $|\mathfrak f|<1/5$. The second has a strict negative sign, since
$$
 (1/2-\mathfrak c)^2-\mathfrak f
                   >43681/202500-1/5>0.
 \tag{4}
$$
On any fixed interior subwindow of $\mathcal X$, off $O(X/\ell^2)$ even targets, the actual $V_{\rm curv}$ is therefore negative of magnitude $\gg X/\ell^2$. Its squared norm is of order $X^3\ell^{-4}$. This is not a sign of $V_f$ alone, the composite-only curved contribution, an individual prescribed modulus, an adaptive floor choice, the original total pair sum, or Hypothesis S.

## 1. Exact separation and geometry of the new correction

With $v_h(z)=\mu(z)\log(h/z)$ the including-root mark is $-v_h(z)$. The uncurved product of the two actual long sums of these marks, with exterior minus, is exactly the quantity $U^{\rm all,(1,1)}$ evaluated in the semiprime-wing theorem. At the integer pair level the deletion of products $\le Q_N$ adds the expression (1), including the correct weak product boundary. In a wing the only nonzero containing long mark is at its root $F>\sqrt N$; for a long mate $e\ge D_N+1$ we have $Fe>Q_N$, exactly as in that theorem. Consequently the correction has no wing term, and
$$
                  V_{\rm curv}=U^{\rm all,(1,1)}+V_f
 \tag{5}
$$
on the actual target set. We evaluate only $V_f$ below.

Use the original containing-label coordinate $g=(L/2-\log(Fz))/T$, and independently $g'$ for the mate. Each of the two retained labels on (1) is below $\sqrt N$, since $Q_N/(D_N+1)<\sqrt N$. The other cutoff inequalities are the actual two long tests and one product boundary. Because $\log D_N=L/2-20T+O(1)$ and $\log Q_N=L-20T+O(1)$ on $\mathcal X$, its fixed real comparison is exactly the triangle in (2), with possible displacement $O(1/T)$ of each boundary. This geometry applies to the **label** $Fz$, not the root $F$. In particular $z$ is bounded by $\exp((41/2+O(1/T))T)$ on (1), even when $z$ has several prime factors. Both roots and cofactors on the comparison are in fixed log windows $L/2+O(T)$; for the cofactor this follows from $hF\in\mathcal J$ and the upper label and lower root bounds. The actual floor can be fixed temporarily at $\sqrt X e^{-(41/2)T}$, with an enclosing log-width-$O(1)$ root sliver.

Subdivide a fixed interval containing $[0,20]$ in each label coordinate into intervals of width at most $\delta=\ell^{-3}$, with $O(\delta^{-1})$ of them and the grid containing $0,20$. The actual off-boundary products are exact convolutions on fully accepted cells after fixing the floors and suppressing target-unit conditions. Every uncertain cell lies along one of the fixed triangle boundaries within $O(\delta+1/T)$, so there are only $O(\delta^{-1})$ such cells. Keep the original tests in the arithmetic terms of these cells and bound them by positive arm convolutions, rather than selecting terms on the real boundary. The all-label positive bin fourth norm of the composite calculation, §1, is $O(X^{3/4}\delta)$ on each arm, applicable here with precisely the same bin width, label cap and cofactor windows. Thus the total uncertainty costs at most $O(X^{3/2}\delta)$ in target norm, by Hölder and Parseval. This includes cells just outside the fixed triangle, in particular the true upper label and equality slivers. The prime-floor displacement costs $O(X^{3/2}/T)$ in target norm: one positively marked arm on the enclosing root sliver has fourth norm $O(X^{3/4}/T)$ by the same log-density bound, and its mate without a label bin is $O(X^{3/4})$. Here the short-label multiplicity is bounded using the same fixed short block, and no comparison depends on a regularity assumption for $N$. A lost target-unit factor divides both operands, thus divides $N$, and is at least $e^{5T/4}$. There are $O(\ell)$ such primes, each allowing $O(X/p+1)$ first operands. The two root and short label multiplicities cost fixed powers of $L$, so these literal terms contribute $O_D(XL^{-D})$ per target. This restores actual units in the same manner as in the previous collision calculation.

## 2. The signed response of a genuine rejected-root label bin

Use the same auxiliary arcs and the same function $H$ as in the semiprime-wing theorem: on a reduced auxiliary major $c/q+\beta$, $q\le P=L^{C_0}$, put $H=(\mu(q)/\varphi(q))\widehat J(\beta)$, and put it equal to zero off them. Here $\widehat J(\beta)=\int_{\mathcal J}e(\beta x)\,dx$. This model has $\|H\|_4\ll X^{3/4}$, and $C_0$ is a sufficiently large fixed exponent. It is independent of the hard label bin. On an interval $B$ of the label grid in $[0,20]$, let $A_B$ be the Fourier arm with the fixed common floor, hard $hF\in\mathcal J$, true composite cofactor and canonical root, exact label $z\mid h$ and $g\in B$, and mark $\mu(h)\mu(z)\log(h/z)$. Target-unit restoration is as above. We will show, for any fixed sufficiently large $D$,
$$
 \left\|A_B+\frac{H}{\ell}\int_B C(g)\,dg\right\|_4
 \ll X^{3/4}\left(\delta\ell^{-2}+\frac1{T\ell}+L^{-D}\right).
 \tag{6}
$$

To prove this statement, first admit a separated prime root without canonical or repeat veto, keeping the actual squarefree composite cofactor. Its signed bin fourth norm is $O_{B'}(X^{3/4}\delta\ell^{-B'})$ for any fixed $B'$ by the signed Dickman argument of the composite calculation, §1: the full factor sign is exactly the signed high-prime product after fixing the labeled short block, and the compact cofactor interval and $g$ bin are unchanged. This step is on the full bin arm, not on a completed real two-variable triangle. The two rejected possibilities are the strict collision with some other cofactor prime $P_1>F$, or a repeat $F\mid h$. They are disjoint for large $X$: three near-square-root factors, with multiplicities, have product exceeding every operand in $\mathcal J$. In the strict collision $P_1$ is unique by the same argument; write $h=sWP_1$ with the true squarefree factors. Since $u=(L/2-\log F)/T\le41/2$ and $P_1>F$, the part $d_0=sW$ satisfies $\log d_0\le42T$. The repeated terms have the form $d_0F^2$ with the same bound; they are supported on $X^{1/2+o(1)}$ integers, with at most a fixed power of $L$ in coefficient size including every eligible label. Their fourth norm is $X^{3/8+o(1)}$ by interpolating Fourier supremum and Parseval. They are negligible in (6).

In the strict collision the near-square-root prime $P_1$ cannot divide the short label $z$. Factor $z=s^jW_1$ with $j\in\{0,1\}$ and $W=W_1W_0$, where the two latter products are coprime squarefree and each uses primes at least $e^{4T}$. Put $t=\log s/T$ and $\eta=\log W_1/T$. The exact arithmetic mark sign is
$$
                  \mu(h)\mu(z)=(-1)^j\mu(W_0).
 \tag{7}
$$
Indeed the signs of $s,P_1$ cancel in $\mu(h)$, and all primes marked in $W_1$ then have their sign canceled by $\mu(z)$. This is not an independence assumption about labels or a signed-to-unsigned upper bound.

Let $R_B$ be the genuine rejected-root polynomial for this strict collision and label bin. On each reduced auxiliary major apply Siegel–Walfisz to $F$ at fixed $h,z$, with the original hard $hF\in\mathcal J$, $Fz$ in the bin, fixed lower root floor, and the strict $F<P_1$. All prime factors of $h$ are greater than the polylogarithmic denominator, so the numerator factor is exactly $\mu(q)/\varphi(q)$. With $x=hF$ the weight is $\log(h/z)/(h\log F)$ including (7). The summed error is $O_D(XL^{-D})$ for any fixed $D$: the hard $F$ interval has scale $X/h$ with logarithm comparable to $L$, variation in the oscillatory factor costs a fixed power of $L$, and the $h,z$ reciprocal-weight sum costs a fixed power of $L$. As in the composite collision proof, after this step use ordinary reciprocal PNT in $P_1$ at fixed $x,s,W_1,W_0$; it is now an ordinary real prime interval, with no imposed residue modulo $q$. The product interval at fixed $x$ and the strict $F<P_1$ give hard endpoints; bounded-variation marks and the near-square-root prime scale give arbitrary inverse powers of $L$ in the summed discrete error. In both prime comparisons the $P_1$-dependent cutoff is evaluated as an endpoint, not approximated by flattening the label.

For the resulting integral,
$$
 \begin{split}
 u&=g+\eta+jt,\qquad
 \log P_1=\log x-\log(sW)-L/2+uT,\\
 F<P_1
   &\ \Longleftrightarrow\
  \log W_0/T<2g+\eta+(2j-1)t+(\log x-L)/T .
 \end{split}
 \tag{8}
$$
The change of variable is $d\log P_1=T\,dg$. Its reciprocal prime density times the real mark, after removing $1/(sW)$, is
$$
             \frac{T}{\log P_1}\frac{\log(h/z)}{\log F}
                    =\frac2\ell+O(\ell^{-2}),
 \tag{9}
$$
since every clipped logarithm in the ratios is $L/2+O(T)$, and $\log z=O(T)$. The floor is exactly $g+\eta+jt\le41/2$ in this common comparison. At fixed $s,W_1,W_0,j$ the shifted strict inequality (8) removes or adds at most a length $O(1/T)$ inside $g\in B$, and its endpoint moves monotonically by $O(|x-y|/(XT))$ between physical points $x,y$. This statement holds even for $W_0=1$. The variation in the two ratios on any common interval is $O(\ell^{-1}|x-y|/(XL))$ after their product is taken. Therefore freezing the shift and replacing (9) by $2/\ell$ costs $O(\delta\ell^{-2}+1/(T\ell))$ in real supremum and total variation; the jumps at the endpoints of $\mathcal J$ cost the same bound. The positive reciprocal mass of the allowed low **labeled** products is bounded: the factors are in $[e^{4T},e^{42T}]$ with at most two occupation choices and the old prime is in a fixed log-ratio band. Hence summing over them is harmless. In particular this variation bound does not assume a pointwise derivative for a discrete prefix.

Replace old and small primes in the fixed real scalar after this freezing. All necessary prime exponents are bounded by $42$ in units of $T$, and the distinct tuple expansion has bounded arity and bounded positive reciprocal mass. Replace the one-prime reciprocal sums in turn by $dt/t$ on their literal intervals at fixed other coordinates (or by partial summation for bounded-variation tests); their arbitrary inverse-log errors are uniform since the smallest scale is $e^{5T/4}$. Distinctness deletions cost the reciprocal square tail, including a repetition **across** $W_1,W_0$. Thus the marked variables yield the positive measure $\mathcal P(d\eta)$ and the unmarked ones its signed exponential with integrator $-\mathbf1_{[4,42]}dy/y$. Its cumulative up to argument $w$ is $\rho_+(w/4)$ for $w\le42$, by the signed Dickman identity used in the composite proof; the effect of an atom at $w=0$ is dealt with by integrating the hard $g$ offset, whose equality set has measure zero. In fact after freezing, the active bound is $t+\eta+\log W_0/T\le2u\le41$, so no excluded large prime or detached endpoint is reintroduced by this step. Consequently the constant density on the physical window is exactly $\ell^{-1}\int_B C(g)\,dg$, up to arbitrary inverse-log discrete errors. The two alternatives of $j$ give the two signed terms of (2), not an unsigned occupancy weight. The real transform error has the previous supremum/variation size times $\min(X,|\beta|^{-1})$ with the same rational factor. This gives the corresponding fourth-norm error on the majors using the fourth power of this integrable transform bound and $\sum_q\mu(q)^4/\varphi(q)^3<\infty$.

For completeness, the strict rejected-root polynomial has negligible actual minor fourth norm despite its extra root comparison. On the near-square-root dyads in $h,F$ separate three kinds of integer cut by height-$X^4$ Perron, with half-integer positions: the physical endpoint tests on $hF$, the label-bin endpoint tests on $Fz$, and the extra strict bound $F\le P_1(h)-1$ separated by $P_1(h)-1/2$. In each of the first two kinds, a difference of upper cutoffs makes the hard interval. The fixed root floor stays a hard endpoint of the prime factor independently. The cutoff for $P_1(h)$ twists only the $h$ coefficient by $(P_1(h)-1/2)^{\sigma+i\tau}$ (with a corresponding twist of the $F$ coefficient), and the $z$ twists remain with the cofactor and label. At real part $\sigma=1/L$ all these powers have bounded modulus on the ranges used, and the integrated overhead is a fixed power of $L$. The distinct half-integer separating positions give negligible truncation, even after summing $O(XL^{O(1)})$ possible dyadic products with short labels: products, roots and separating boundaries are at most $O(X^{1+o(1)})$, so relative gaps are at least $X^{-1-o(1)}$. The coefficient twists and extra labels leave absolute dyadic coefficients bounded by a fixed power of $L$. For such coefficients ordinary bilinear Cauchy and the reciprocal-distance estimate of the semiprime-wing proof, (5), give squared relative bound
$$
 L^{O(1)}\left(q^{-1}+K^{-1}+\frac{\log(2q)}{M}
                                  +\frac{q\log(2q)}{X}\right)
$$
on dyads $h\asymp M,F\asymp K$, $MK\asymp X$. On minors $P<q\le\lfloor X/P\rfloor$, and $M,K=X^{1/2+o(1)}$. Enlarging the fixed exponent $C_0$ pays for every prescribed fixed log saving and for all three Perron factors. The coefficient energy is $O(XL^{O(1)})$ by bounded root multiplicity and the short-label cap; hence the supremum saving implies the desired fourth-norm saving. This estimates the actual polynomial with the three hard cuts. Subtracting $R_B$ and repeats from the separated arm proves (6), with a **negative** model on the canonical arm.

## 3. Complete the signed pair and certify the margin

Sum (6) over all bins. Its errors sum to $O(X^{3/4}\ell^{-2})$, because $\delta^{-1}/(T\ell)$ is smaller, and the model bin norms sum to $O(X^{3/4}/\ell)$ by the bounded continuum envelope of (2). Hölder and Parseval thus give total product error $O(X^{3/2}\ell^{-3})$ on the accepted cells. Both canonical arm signs in (6) are negative, and the divisor correction (1) has exterior plus, so the coefficient of $H^2$ has the **positive** prefactor $\ell^{-2}$ times the signed product of bin integrals. The [exact reduced-numerator rational completion](r80-source-local-mean-square-at-sign-transition.md), §3, gives for the coefficient of $H^2$ at $N$ the comparator $I_N$ with arbitrary fixed inverse-log saving in target norm, by summing reduced numerators before absolute values to obtain $c_q(N)$, keeping the finite arc radius, and extending only the auxiliary main-term tails. This is the same $I_N$ as in the wing theorem; no new density normalization is put into (2). The model integral on the missing or ambiguous cells differs from the triangle integral by $O(\delta)$ since $C$ is bounded. The already estimated literal cell error is $O(X^{3/2}\delta)$, sufficient at the stated scale $\delta=\ell^{-3}$. Together with the unit and external-floor checks this proves the first asymptotic in (3) on the actual target set.

Here is an independent rigorous envelope for (2). At fixed $t,\eta,g$ the two expressions in braces are nonnegative before subtraction, so the absolute bracket is at most their maximum. Each expression is bounded by
$$
  \mathbf1_{\eta\le41/2-g}\rho\!\left(\max(0,(2g-7/4)/4)\right).
$$
This holds also when a Dickman argument is negative: that expression is zero by definition, and the bound never exceeds one. The truncated positive exponential satisfies $\mathcal P([0,v])\le\max(1,v/4)$ because only jumps at most $v$ can contribute, and the exponential restricted to those jumps has this or smaller total mass. Monotonicity and $y\rho(y)=\int_{y-1}^y\rho(s)\,ds$ give $\rho(y)\le1/\lfloor y\rfloor!$ for $y\ge0$: iterate $y\rho(y)\le\rho(y-1)$ down to $[0,1]$. Also $\log(7/5)<17/50$ follows, for example, by using the first five alternating terms for $\log(1+2/5)$. Therefore on the unit cell $i\le g\le i+1$ an upper bound for $|C(g)|$ is the rational
$$
 A_i=\frac{17}{25}\,
      \frac{\max(1,(41-2i)/8)}
           {\bigl(\max(0,\lfloor(8i-7)/16\rfloor)\bigr)!},
                     \qquad 0\le i\le19 .
$$
A pair of such cells can meet the triangle only if $i+j\ge18$. Bounding each contributing cell by its full unit area gives, with no numerical approximation to $\rho$,
$$
 |\mathfrak f|\le
       \sum_{\substack{0\le i,j\le19\\i+j\ge18}}A_iA_j
  =\sum_{i=0}^{19}A_i\sum_{j=\max(0,18-i)}^{19}A_j
  =\frac{15868494897049}{82301184000000}<\frac15 .
 \tag{10}
$$
For the second comparator, the semiprime-wing theorem gives $\mathfrak c\le(16/153)\log(7/5)<8/225$, whence $(1/2-\mathfrak c)^2>(1/2-8/225)^2=43681/202500$. Thus the full completed comparator is separated from zero by the margin in (4), regardless of the sign of the deterministic forbidden integral. Combine the semiprime-wing uncurved asymptotic with (5) and the first part of (3). Finally $I_N\gg X$ at every even target in a fixed interior subwindow, while $\|I_N\|_{\ell^2(N)}\ll X^{3/2}$. Chebyshev at the fixed signed scale $X/\ell^2$ gives the exceptional count and the squared norm stated in the theorem. Nothing in the comparison estimates the other signed rows or conditions on an exceptional fixed modulus.
