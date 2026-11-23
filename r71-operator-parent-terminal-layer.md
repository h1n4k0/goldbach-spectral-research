# Full terminal-layer deletion on the surviving parent means

**Scope.** This estimates actual covariance terms of the remaining literal parent-mean matrix of [R70](r70-operator-adaptive-parent-contrast-rank.md). It does not project out another contrast subspace. Each raw parent profile is split exactly into a short terminal layer and a common-shape lower profile. All terms with a terminal layer on at least one leg are small in a selected-moduli fourth mean, including the long crossings and the exact continuum benchmark. The all-alias covariance of the lower profiles remains open.

## Statement and the exact profile split

Use the reference dyads $[V,2V]$ intersected with $[H,M]$, with $4\le H<M\le Q^\Gamma$, $0<\Gamma<1$ fixed. Take the actual transported parent means of R70, with parent intervals $I=[l_I,b_I^{\rm end}]$ of positive lengths at most $W_V$ on one $V$-dyad, where $1\le W_V\le V/20$. Endpoints of adjacent intervals may be assigned consistently. Let $\mathcal A\subset[Q,2Q]$ consist of $J\ge1$ distinct even moduli. Assume original local GRH at each $N\in\mathcal A$ and auxiliary Dirichlet GRH through $\lceil20\sqrt{Q\max_V W_V}\rceil$, including $q=1$. Write $L=\log(3Q)$.

At $t\in[Q,2Q]$ and raw $x>0$, the exact normalized profile of a parent mean, before substituting $t=N$, is [R65](r65-operator-dense-low-raw-alias-deletion.md) (2):

$$
h_{I,t}(x)=\frac{\sqrt{2\pi x}}Q
     \frac{\displaystyle\int_{I,\ z\ge x/Q}w_t(z)\,dz}
          {\displaystyle\left(\int_I w_t(z)\,dz\right)^{1/2}},
 \qquad
 w_t(z)=z^{-3}\big((Qz)^{-2/\log t}+(Qz)^{-1/4}\big).
 \tag{1}
$$

Extend profiles by zero for nonpositive raw inputs. Fix a nondecreasing $C^1$ function $\Theta:\mathbb R\to[0,1]$, zero on $(-\infty,-1]$ and one on $[0,\infty)$, with bounded derivative. On a $V$-dyad put $X=QW_V$ and split the true profile at $t=N$ by the two factors

$$
g_{I,t}(x)=h_{I,t}(x)\Theta((x-Ql_I)/X),\qquad
 f_{I,t}(x)=h_{I,t}(x)-g_{I,t}(x).
 \tag{2}
$$

Thus the entire raw interval $QI$ belongs to the terminal layer $g$, and the extra transition before it has length at most $X$. The same factors are always applied to the prime-power atoms and the continuous line integrals, in all three orientations. Let $T_N^{h,h}$ be the exact signed matrix of the actual parent means, and $T_N^{f,f}$ the same arithmetic and model with $f$ profiles on both legs. In both, all positive aliases $s=kN$ are kept, with the exact $N$-unit condition, positive two difference orientations, negative sum orientation, and the equality line omitted. The result is

$$
\begin{split}
 \left(\frac1J\sum_{N\in\mathcal A}
             \|T_N^{h,h}-T_N^{f,f}\|_{\rm HS}^4\right)^{1/4}
 &\ll_{\Gamma,\epsilon,\Theta} Q^\epsilon
        \sum_V\left[\mathcal A_V^{1/2}
           +\sqrt{W_V/V}+\frac{W_V}{\sqrt{VH}}\right],\\
 \mathcal A_V&=\frac{W_V}{V}\left[
        \sqrt{\frac{W_V}{J}}(QW_V)^{1/4}
                          +\sqrt{\frac{W_V}{Q}}\right].
 \end{split}
 \tag{3}
$$

This is a full matrix estimate on the smaller surviving space, not an estimate of another projection complement.

At R70's parameters $H=Q^{2/5}$, $M=Q^{3/5}$, $W_V=Q^{23/175}V^{4/7}$, the auxiliary range is still $\lceil20Q^{129/175}\rceil$. If $J\gg Q^{99/100}$, the left side of (3) is $O_{\Gamma,\epsilon,\Theta}(Q^{-3/400+\epsilon})$. For arbitrary $J$, there are $O_{\Gamma,\epsilon,\Theta}(Q^{97/100+\epsilon})$ exceptions above $Q^{-1/500}$ for this terminal-layer deletion. These are separate selected-moduli estimates, not a conclusion for an individual prescribed $N$.

## 1. The grand terminal profile estimates

Here fix a single $V$-dyad, $a=QV$, $X=QW_V$, $X_I=Q|I|$, and $b_I=\sqrt{X_I}/a$. The support of $g_{I,t}$ is contained in $J_I=[Ql_I-X,Qb_I^{\rm end}]$, length at most $2X$ at height $\asymp a$. Formula (1) gives

$$
\|h_{I,t}\|_\infty+\mathrm{TV}(h_{I,t})
       \ll_\Gamma b_I,\qquad
 \sum_I b_I^2\ll a^{-1},\qquad
 \sum_{I:\,x\in J_I} b_I^2\ll X/a^2 .
 \tag{4}
$$

For the last estimate, the disjoint underlying $QI$ for the indices in question all lie in an interval of length $O(X)$ near $x$; use $\sum X_I=O(X)$. This works for clipped or unequal windows. The TV bound for $h$ follows by its square-root derivative and the $L^1$ size of its terminal derivative on $QI$. It also holds for $g$ and $f$, since the multiplier in (2) has bounded variation. All these estimates hold for the normalized derivative $Q\partial_t$ of a profile, because $Q|\partial_t w_t(z)|\ll_\Gamma w_t(z)$ in the polynomial range, also controlling the derivative of the normalizer. The support intervals and the mask are fixed in $t$.

For the prime-in-progression error vector $\mathbf F$ of [R59](r59-operator-balanced-arcs-cuberoot-prefix.md), its finite-height Selberg bound gives

$$
\int\|\mathbf F(x+s)-\mathbf F(x)\|_2^2dx
          \ll_\Gamma a s L^4 \qquad (0<s\le 4X)
 \tag{5}
$$

on our bounded dyadic enlargement of $[a,2a]$, for every needed $q$. For $s\ge1$ cover the range by a bounded number of dyads, noting $4X\le a/5$. For $s<1$, use at most one prime-power atom in a slide interval, with squared total marks $O(aL^2)$ each counted for length at most $s$, and the $O(as^2)$ drift. Negative shifts are treated by translating the integral.

We prove the two grand residue estimates for $\nu_{I,r}=g_{I,t}\,dF_r$,

$$
\begin{split}
 \sum_{I,r}|\widehat\nu_{I,r}(\beta)|^2
         &\ll_{\Gamma,\Theta}(X/a)(1+|\beta|X)^2 L^4,\\
 \int_{\mathbb R}\sum_{I,r}|\nu_{I,r}((s,s+\ell])|^2ds
         &\ll_{\Gamma,\Theta}(X/a)\ell L^4,\qquad 2\le\ell\le X ,
 \end{split}
 \tag{6}
$$

including $Q\partial_t g$ in place of $g$. To see the first, for each $I$ choose $\mathbf m_I$ to be the average of $\mathbf F$ on $[Ql_I-X,Ql_I+X]$. By Jensen, for $x\in J_I$ only shifts of size at most $2X$ occur. Using (5) and (4) gives

$$
\sum_I b_I^2\int_{J_I}\|\mathbf F(x)-\mathbf m_I\|_2^2dx
                       \ll_{\Gamma} X^2 L^4/a .
 \tag{7}
$$

Indeed, inside the integral in the lag $y-x$, the count is bounded by $\sum_{I:x\in J_I}b_I^2\ll X/a^2$; the remaining integral, divided by the averaging length $2X$, is $O(aXL^4)$ by (5). Without weights but with the disjoint $QI$ in place of $J_I$, the corresponding bound is $O(aXL^4)$.

The terminal profile is continuous and zero at both support endpoints. Fourier partial integration therefore permits subtracting $\mathbf m_I$ exactly. On the differentiable pieces $g'$ has bulk terms from the square root and the cutoff, of size $O_\Theta(b_I/X)$, and an actual terminal derivative supported on $QI$. The latter has density

$$
-\Theta((x-Ql_I)/X)\,
      \frac{\sqrt{2\pi x}}{Q^2}
      \frac{w_t(x/Q)}{\sqrt{\int_I w_t}}
 \quad (x\in QI),
 \tag{8}
$$

of magnitude $O_\Gamma(b_I/X_I)$. The phase derivative is $O(|\beta|b_I)$. Cauchy in $J_I$ and (7) bound the squared contribution of the bulk and phase derivatives by $O((X/a)(1+|\beta|X)^2 L^4)$. For (8), Cauchy in $QI$ gives $b_I^2/X_I=a^{-2}$ times the squared integral of $\mathbf F-\mathbf m_I$ on $QI$. Sum over the disjoint $QI$ and use the unweighted bound just after (7). This proves the first line of (6).

For the second use the exact Abel identity

$$
\int_{(s,s+\ell]}g\,dF_r
 =g(s+\ell)[F_r(s+\ell)-F_r(s)]
         -\int_s^{s+\ell}g'(x)[F_r(x)-F_r(s)]\,dx .
 \tag{9}
$$

The first term gives $O((X/a)\ell L^4)$ by (4), (5). For the bulk derivative its squared pointwise envelope summed over $I$ is $O(1/(Xa^2))$. Minkowski in the lag $u=x-s$ gives squared integral $O(\ell^3/(Xa)L^4)$, within the claimed bound. For (8) Cauchy in each $QI$ has the same $a^{-2}$ factor as above; then sum the disjoint $QI$ and integrate $s$. Using (5) gives $O(\ell^2/a)L^4$, again admissible. The derivative in $t$ has identical estimates since (8) only differentiates its density and normalizer. The second line of (6) gives its Fourier integral version on $|\beta|\le 1/(4\ell)$, of size $O((X/a)L^4/\ell)$, by convolution with the interval indicator and Plancherel.

## 2. All-alias terminal square with exact masks and moving normalization

We give the circle argument on one $V$-dyad; it is the R70 grand estimate applied to the actual terminal mean profiles, not to projected contrasts. By Parseval, (4), and the support and TV bounds, the grand vectors of prime sums $A(\alpha)_I=\sum_n\Lambda(n)g_{I,t}(n)e(n\alpha)$ and continuum integrals $B(\beta)_I=\int g_{I,t}(x)e(\beta x)dx$ satisfy

$$
\|A\|_{L^2(\mathbb T;\ell^2)}\ll L\sqrt{X/a},
       \qquad
        \|B(\beta)\|_2\ll a^{-1/2}\min(X,|\beta|^{-1}).
 \tag{10}
$$

Use disjoint balanced major arcs with $P=\lfloor\sqrt X/10\rfloor$ and $\delta_q=2P/(qX)$, as in R70. At $c/q+\beta$, write $A=\mu(q)B/\phi(q)+E+Z$ for the principal, residue-error and $q$-nonunit pieces. Equation (6) gives $\|E\|_2\ll\sqrt{X/a}\sqrt q(1+|\beta|X)L^2$, and the arc square integral for fixed $q$ of $E$ is $O((X/a)L^4P/X)$ by using $\ell=qX/(8P)$ in (6) and finite additive Parseval. The pointwise $Z$ bound is $O(L^2/\sqrt a)$. On the minors, Dirichlet approximation gives $P<q\le\lceil20\sqrt X\rceil$, $|\beta|X\le1$, yielding grand supremum $O_\epsilon(Q^\epsilon\sqrt{X/a}X^{1/4})$ by the same formula. Combine with the other leg's first bound in (10), or on the majors combine the error supremum and integrated square by $\sum_{q\le P}q(1+P/q)^2\ll P^2\log(2P)$. The minor tensor and the major double error have $L^2({\rm HS})$ norms $O_\epsilon(Q^\epsilon (X/a)X^{1/4})$. The single errors have that bound by finite additive Parseval, $(1+|\beta|X)\|B(\beta)\|_2\ll X/\sqrt a$, and $\sum_{q\le P}(q/\phi(q)^2)\delta_q\ll P/X$. This includes the normalized derivative on one leg and the two Fourier argument signs, by reflection symmetry.

For a pair $I,I'$ the exact supports $J_I,J_{I'}$ permit only $O(W_V)$ positive aliases in the actual affine sum or difference interval, including for the continuum. Cauchy in these $k$ within each entry and the divisor bound for the multiplicity $s=kN$, $s\ll QM$, cost $O_\epsilon(Q^\epsilon\sqrt{W_V/J})$ in the modulus RMS. Although the support mask varies by entry and modulus, it is fixed in $t$; for the moving profiles use the exact fundamental theorem of calculus of R65 §3, on each $c_{kN}(N)=c_{kN}(Q)+\int_Q^{2Q}\mathbf1_{t\le N}\partial_t c_{kN}(t)dt$. Minkowski and the same square sampling for $N\ge t$ preserve the bound, using (6) and (10) for the normalized derivative.

For the pointwise errors, per entry the $q$-nonunit products cost at most $O(W_V)$ times their $L^1$ tensor bound. Taking HS and Minkowski and using the $Z$ supremum and (10) gives $O(L^{O(1)}(W_V/V)\sqrt{W_V/Q})$. To restore the exact $N$-unit condition, each prime-power nonunit on a leg has at most one possible partner on a fixed line. Its total marks are $O(L^2)$, so the weight $O(b_Ib_{I'})$ and $O(W_V)$ lines, then (4), give $O(L^{O(1)}W_V/(QV))$. Using the individual TV bounds on each parent in (10), the principal continuum tail is $O(b_Ib_{I'}qX/P)$ per denominator per line, and the full continuum coefficient is $O(b_Ib_{I'}X)$. The absolute Ramanujan estimates of [R66](r66-operator-dense-top-sum-edge.md) (14) give total restoration error $O_\epsilon(Q^\epsilon W_V^2/(PV))$ after summing the lines and taking HS by (4). Fourier inversion restores exactly the affine profile integral at that line, and the restored Ramanujan series is $\mathfrak S(kN)$. Together these give

$$
\left(\frac1J\sum_{N\in\mathcal A}
            \|T^{g,g}_{N;V,V}\|_{\rm HS}^2\right)^{1/2}
                    \ll_{\Gamma,\epsilon,\Theta}Q^\epsilon\mathcal A_V .
 \tag{11}
$$

Sampled and pointwise parts are separate in the proof. The sampled square sum before dividing by $J$ is $O_\epsilon(Q^\epsilon Q^{1/2}W_V^{7/2}/V^2)$. This treats every actual sign and every allowed positive alias in the terminal square. The treatment of the broad mixed aliases uses positivity below, not a sparse mask assumption on those aliases.

## 3. The exact mixed benchmark and positive Gram

For any two profile families $u,v\in\{h,f,g\}$, write $T^{u,v}=P^{u,v}-D^{u,v}-K^{u,v}$. These are exact restricted raw matrices: $P$ is the odd-character Gram, $D$ the equality atom, and $K$ the continuous model with the same $u,v$ profiles. The representation is the all-alias identity of [R68](r68-operator-residue-orbit-and-alias-slope-covariance.md) (2), (5) before grouping by orbit; the prime Gram is positive on a common family. In fact $P^{u,v}$ is the product of the two families of row vectors of odd character sums with the normalization $2/\phi(N)$ in their inner products. This identity holds for the masked real profiles as well. For any family $h,f,g$, local odd GRH, partial summation and (4) give trace $O(L^{O(1)})$ on the entire parent space. Indeed for one odd character the prime sum against one profile is $O_\Gamma(L^2\sqrt{QV}\,b_I)$ by the local GRH prime-sum bound, and $\sum_{I\subset[V,2V]}QV b_I^2=O(1)$. Sum over the logarithmically many dyads, then average over odd characters.

For the equality term the terminal self-diagonal trace is $O_\Gamma(L^2 W_V/V)$, by the envelope (4) and the raw length $O(QV)$. The trace with a full or body profile family is $O(L^{O(1)})$ by the unweighted envelope $\sum_I b_I^2\ll a^{-1}$ per dyad. Treating $D^{g,v}$ as the mixed Gram on this integer atom space gives pointwise HS bound $O(L^{O(1)}\sqrt{W_V/V})$ from the $V$-terminal family to the entire other side.

For the continuous term, the cumulative singular series formula of R68 (8) is

$$
\sum_{1\le k\le t}\mathfrak S(kN)
      = (N/\phi(N))t+O_{\Gamma,\epsilon}(Q^\epsilon)
      \qquad(0\le t\le 4M+1).
$$

As in R68 (9)–(10), the continuous integrals of the two positive difference orientations cancel that of the negative sum over $t>0$ at the constant density $N/\phi(N)$, for **each** pair of profiles: the whole raw quadrant is covered with the same Jacobian and the equality line is null. If $g$ is on the $V$-leg and $v\in\{h,f,g\}$ on a $U$-leg, the sup plus variation of each line profile is bounded by $O_\Theta(X b_I b_{I'})$, taking the short terminal weight's $L^1$ norm and the other weight's sup plus TV. Thus partial summation and $\sum b_I^2$ yield the pointwise bound

$$
\|K^{g,v}_{N;V,U}\|_{\rm HS}
                      \ll_{\Gamma,\epsilon,\Theta}
                               Q^\epsilon\frac{W_V}{\sqrt{VU}} .
 \tag{12}
$$

In particular the actual terminal self-benchmark $D^{g,g}_{N;V,V}+K^{g,g}_{N;V,V}$ is $O_\epsilon(Q^\epsilon W_V/V)$ in HS. No absolute summation of the continuum lines is used in (12).

For the mixed prime Gram use its positive factorization, giving

$$
\|P^{g,v}_{N;V,\mathrm{all}}\|_{\rm HS}^2
       \le \|P^{g,g}_{N;V,V}\|_{\rm op}\,\mathrm{tr}(P_N^{v,v})
       \ll_{\Gamma,\epsilon,\Theta}
          Q^\epsilon\big(\|T^{g,g}_{N;V,V}\|_{\rm HS}+W_V/V\big).
 \tag{13}
$$

This is valid for the full or body family, using the exact self-benchmark for the terminal leg and not positivity of $T$ or $K$. Combine (12), the equality estimate, (13), and the fourth mean from (11) to obtain the $V$-summand of (3), for its terminal leg against the entire remaining parent space. The sum over output dyads in (12) costs at most $O(1)/\sqrt H$ after factoring $W_V/\sqrt V$. Finally the exact bilinear identity $T^{h,h}-T^{f,f}=T^{g,h}+T^{f,g}$ and adjunction prove (3). Unlike the positive lift of R70, this lift is on raw masked profile families and does not discard any new physical direction.

## 4. Rates and the remaining arithmetic fields

With R70's example, $Q^{1/4}W_V^{7/4}/V=Q^{12/25}$, $W_V/V\le Q^{-1/25}$, and $W_V/\sqrt{VH}\le Q^{-9/350}$. Thus (3) has the claimed rate. The unnormalised sampled square bound after (11) is $O_\epsilon(Q^{24/25+\epsilon})$ for each $V$, and its other errors are pointwise smaller than $Q^{-1/200}$. Chebyshev gives $O_\epsilon(Q^{97/100+\epsilon})$ exceptions to the $Q^{-1/200}$ terminal-square HS bound, allowing the logarithmically many dyads. At each other selected $N$, the pointwise lift (13) with (12) and the equality estimate makes the deletion $O_\epsilon(Q^{-1/400+\epsilon})$; choose a smaller $\epsilon$ to place it below $Q^{-1/500}$.

On the remaining body in (2), one always has $x<Ql_I$ where the numerator in (1) is the whole integral. Consequently the remaining profile is **exactly**

$$
f_{I,N}(x)=
 \frac{\sqrt{2\pi}}Q\!\left(\int_Iw_N(z)\,dz\right)^{1/2}
 \sqrt x\,\big(1-\Theta((x-Ql_I)/X)\big)
 \qquad (x>0).
 \tag{14}
$$

It is a fixed probability mixture of sharp weighted prefixes, because
$1-\Theta((x-Ql_I)/X)=\int_{-1}^0\mathbf1_{x\le Ql_I+uX}\Theta'(u)\,du$.
Each entry is therefore the signed, matched two-prefix covariance for these explicit weights, integrated over the two independent endpoint parameters. This does not bound it, nor does it give a result for arbitrary unsmoothed choices of thresholds. The body-only dense principal covariance, with its exact benchmark and all aliases, is the remaining problem.
