# A common exceptional set across the full target-adaptive polynomial split range

Use the same true below-square-root carrier, exact adapted normalizations and fixed floor parameters as the [common-split local law](r81-source-variable-split-local-sign-law.md) and its [subpower maximal version](r82-source-target-adaptive-subpower-split.md). Thus $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\theta=1/20$, $\epsilon=1/64$, $\mathcal J=[X/2,(1+\Delta)X/2]$, $\mathcal X=[X,(1+\Delta)X]$, and $Z_0=V_X^2$ with $V_X=\exp(T\ell^\theta)$. Keep the old $s,W,U$ alphabets, the two deleted neighborhoods, both Möbius parities, the actual typical count for the whole $WU$, true squarefree $N$-units, and the original prime, divisor and curved product tests. In particular at split $Z$, $W_Z$ contains exactly the permitted cofactor primes up to $Z$ other than $s$, with the two actual gates $W_Z\le X^{\epsilon/2}$ and $\omega(W_Z)\le 2\log\ell$; $U_Z>1$ collects the remaining permitted factors. Fix $0<a,b<20$ and $\delta=a+b-20>0$ as before.

Write $R_{N,Z}$ for the genuine signed selected sum, $\mathcal C_{X,Z}$ for the exact lower/upper count-sensitive positive normalization, and $\Psi(\delta)$ for the same short-prime Euler coefficient as before. Put

$$
 {\cal L}_{N,Z}=
     \Sigma(N)B_{\mathcal J}(N)
     \left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2\Psi(\delta),
 \qquad B_{\mathcal J}(N)=|\mathcal J\cap(N-\mathcal J)|.
$$

Here $\Sigma(N)$ is the even binary singular series. Retain the same sufficiently small fixed upper exponent $\delta_0$ of the carrier.

**Theorem (unconditional).** The split can be chosen independently at each target anywhere in the **full original range** $[Z_0,X^{\delta_0}]$. There is the common maximal estimate

$$
    \sum_{\substack{N\in\mathcal X\\2\mid N}}
       \sup_{Z_0\le Z\le X^{\delta_0}}
               |R_{N,Z}-{\cal L}_{N,Z}|^2
                  \ll X^3\ell^{-1/10}.
 \tag{1}
$$

All constants can depend on the fixed parameters of the prescribed carrier. If $\Psi(\delta)\ne0$, its sign holds for all splits simultaneously, with magnitude $\gg X$, in each fixed strictly interior subwindow outside $O(X\ell^{-1/10})$ even targets. On the full window the strict sign holds simultaneously outside $O(X\ell^{-1/30})$ even targets. At the exact fixed critical zero of $\Psi$ this is genuine simultaneous cancellation in mean square. The stronger squared saving $\ell^{-1/5}$ on the small subpower range remains available by the subpower theorem. No conclusion is asserted at a prescribed exceptional modulus, on other carriers, or on Hypothesis S.

## 1. An actual loss in a mesh gap requires two events

Write $\tau=\log Z/L$ and $\tau_0=2\ell^{\theta-1}$. Start the upper mesh at

$$
       \tau_*=(\epsilon/16)\frac{\log\log\ell}{\log\ell},
       \qquad \eta=\ell^{-1/10}.
$$

For large $X$, $\tau_0<\tau_*<\delta_0$ and $\eta=o(\tau_*)$. Put mesh nodes $\tau_j$, indexed by $1\le j\le J$ with $\tau_1=\tau_*$ and $\tau_J=\delta_0$, with increments $\Delta_j=\tau_{j+1}-\tau_j\le\eta$, using increments $\eta$ until the last piece; an empty last piece is omitted. Use $Z_j^{\rm mesh}=X^{\tau_j}$, distinct from the carrier's lower endpoint $Z_0$. There are $O(\eta^{-1})$ nodes. Every gap has $\tau_{j+1}\le2\tau_j$ and normalized reciprocal logarithmic length

$$
                  \xi_j=\int_{\tau_j}^{\tau_{j+1}}\frac{dt}{t}
                      \le 2\Delta_j/\tau_{j+1}.
 \tag{2}
$$

The subpower theorem covers the whole interval below the first mesh node without a mesh loss.

For the upper mesh, first apply the exact four-row short-orbit identity, as in §1 of the subpower proof. In all surviving terms each cofactor lies above $H_-=\frac12\sqrt X e^{-20T}$, and its fixed-window upper bound comes from $hF\in\mathcal J$ and the fixed external prime floor. These log windows have width $O(T)$, and all omission or short labels are at most $M=\exp((22+a+b)T)<Z_0$. Their genuine signed marks, actual units, real floors and original integer strict/weak product tests are independent of how a fixed cofactor is split. The true typical count is on all factors, so it is unchanged by reallocation across a split. Once the size condition is met, $U_Z>1$ is automatic in these active windows. Thus the actual split masks remain nested for the full original range and every eligible operand at a higher split is in the lower $Z_0$ carrier. A distinguished prime is unique even under the fixed comparison: two factors at or above the near-square-root floor would leave only $e^{O(T)}$ for a distinct prime in the true exceptional band, which is impossible.

At a gap $[Z_j^{\rm mesh},Z_{j+1}^{\rm mesh}]$ put

$$
 M_j(h)=\sum_{\substack{p\mid h\\Z_j^{\rm mesh}<p\le Z_{j+1}^{\rm mesh}}}1,\qquad
 \mathcal B_j(h)=
     \{W_{Z_{j+1}^{\rm mesh}}>X^{\epsilon/2}
                 \text{ or }\omega(W_{Z_{j+1}^{\rm mesh}})>2\log\ell\}.
$$

An operand lost on going from $Z_j^{\rm mesh}$ to a split in its gap must satisfy **both** $M_j(h)\ge1$ and $\mathcal B_j(h)$. Without a prime in that gap the lower part cannot change. If lost, a lower gate has failed at the chosen split and is still failed at the upper endpoint by monotonicity. Endpoint primes are included precisely if they can change the split: the bottom is strict, the top is weak. These observations apply before taking absolute values of any pair.

Use the two positive comparison polynomials $A_a,A_b$ at the **fixed base split** $Z_0$ from the subpower proof: exact lower carrier, fixed external prime and cofactor windows, exact physical interval $hF\in\mathcal J$, all short labels $\le M$, and mark $\log F$. Define $A_{a,j}^{\rm loss}$ and $A_{b,j}^{\rm loss}$ by adding the nonnegative multiplier $M_j(h)\mathbf1_{\mathcal B_j(h)}$. All labels and factor allocations of these comparisons are the fixed base ones. The pointwise genuine-loss domination, omitting the target-unit and curved tests only on its positive right, is

$$
 \sup_{Z_j^{\rm mesh}\le Z\le Z_{j+1}^{\rm mesh}}
         |R_{N,Z}-R_{N,Z_j^{\rm mesh}}|
 \ll (A_{a,j}^{\rm loss}*A_b)(N)+(A_a*A_{b,j}^{\rm loss})(N).
 \tag{3}
$$

It bounds actual missing terms of the four signed rows; it is not an assertion that the signed total itself is monotone. Requiring only a prime in the gap and dropping its simultaneous gate failure would not give the linear-scale bound below.

## 2. The marked upper reciprocal density and its genuine endpoints

We prove the following positive norm bound, uniformly in the upper-mesh gaps:

$$
       \|A_{a,j}^{\rm loss}\|_4,\ \|A_{b,j}^{\rm loss}\|_4
                          \ll_A X^{3/4}(\Delta_j+L^{-A})
                    \quad\text{for every fixed } A>0 .
 \tag{4}
$$

The same comparison bounds their positive sums at frequency zero by $O_A(X(\Delta_j+L^{-A}))$. The harmless additive error permits arbitrarily tiny final pieces.

For a fixed gap put $\sigma=\tau_{j+1}$. Use the two Rankin tilts of the subpower proof with upper boundary $\sigma$: $\nu_{\rm ct}=2$ on $u\le\sigma$ and one above, or $\nu_{\rm sz}=\exp(\lambda u/\sigma)$ on $u\le\sigma$ and one above, where $\lambda=\frac12\log(1/\sigma)$. Apply them to every prime of $h$ except $s$ in its correct base alphabet. These give exactly $2^{\omega(W_{X^\sigma})}$ and $W_{X^\sigma}^{\lambda/\log X^\sigma}$, including the true intermediate primes that are in $U$ at $Z_0$. Put $B_\nu=\|\nu\|_\infty$. In addition to a tilt insert the mark $M_j(h)$. Its primes are greater than the base split and thus lie in the genuine **upper** product.

At fixed base $W=W_{Z_0}$ retain the exact remaining upper tag set $K(W)$. Write $A_{\nu,K}$ for the positive upper exponential measure of the [count-restricted reciprocal calculation](r75-source-dynamic-giant-growing-rough-residual.md) with kernels $\nu g_{\rm t},\nu g_{\rm f}$. With $J^{\rm p}_j=(\tau_j,\tau_{j+1}]$, the real marked measure is exactly

$$
 (\mathbf1_{J^{\rm p}_j}\nu g_{\rm t})*A_{\nu,K(W)-1}
        +(\mathbf1_{J^{\rm p}_j}\nu g_{\rm f})*A_{\nu,K(W)} ,
 \tag{5}
$$

where $K-1=\{k-1:k\in K,\ k\ge1\}$ and a zero-order convolution is an atom at zero. In each ordered, factorial-weighted tuple mark one of its coordinates in the given interval. Marking one tagged or free coordinate removes exactly its factorial multiplicity; the tagged choice removes one from the prescribed total and the free choice removes none. Every occurrence is counted, as in $M_j$, even on operands with several primes in the interval. The decomposition into tagged and free ranges remains the actual fixed permitted alphabet, including both removed neighborhoods.

The reciprocal replacement has arbitrary inverse-logarithmic precision uniformly for (5), even with the moving mesh edges. In the ordered prime tuples mark one coordinate first, then telescope the discrete-to-continuous replacement over the coordinates. At fixed other coordinates the hard log-product interval, its bounded-variation mark when present, the fixed tag/free intervals and the single hard marked interval give the same one-coordinate reciprocal PNT estimate, with either endpoint convention. The additional tilt has supremum plus variation $O(B_\nu)$. If $H$ bounds both total tilted reciprocal masses, the telescoping sums cost at most $O((1+H)e^H)$ times the one-coordinate error, by summing the at most $r^2$ marks and replacements against $H^{r-1}/r!$ in total order $r$. For this upper error one can sum the tagged/free patterns for the fixed remaining coordinates against their combined total mass. Dropping repetitions costs at most a fixed polynomial in $1+H$ times $e^H B_\nu^2\sum_{p>Z_0}p^{-2}$ by marking the repeated pair and the requested coordinate. This includes the case where the requested coordinate belongs to that pair. Here in the counting case $H=O(\log\ell)$, and in the size case $H=O(\log\ell+\lambda e^\lambda)=o(\ell)$ since $\sigma\ge\tau_0$; $B_\nu$ costs at most a fixed power of $\ell$. These amplifications are $L^{o(1)}$, and no division by $\xi_j$ is needed to obtain the additive error.

Let $v$ be the normalized upper product coordinate on the fixed active cofactor window. It lies in $[.4,.6]$. A marked coordinate $t$ in (5) is at most $\delta_0$, so $v-t$ stays in a fixed compact subset of $(0,\infty)$ and does not meet the atom at zero. The single-coordinate mass identity of the subpower proof gives

$$
  \rho_{\nu,K'}(v-t)
         \ll B_\nu\,\tau_0^{-1}
                 \exp\!\left(\int_{\tau_0}^{.7}(\nu(u)-1)\frac{du}{u}\right)
$$

for either remaining count set $K'$. This uses positivity and the total upper mass, not independence of the true gate. The total mass of either marked kernel in (5) is at most $B_\nu\xi_j$. Thus the real marked density has the displayed bound with one additional factor $O(B_\nu\xi_j)$. An almost-everywhere representative suffices, because each ensuing real evaluation integrates over a hard cofactor interval.

Combine this with the lower labeled reciprocal product of the subpower proof. The unweighted product bound is $O(\ell\tau_0)$; its extra tilt is already bounded there, including the overlap with the occupation factor used for short labels. In the counting case the combined polynomial has extra factor $O(\ell\xi_j)$, since $B_\nu=2$. In the size case (5) costs at most an extra $e^\lambda$ beyond that proof. The combined factors, relative to the unweighted density scale over a full cofactor window, can therefore be taken to be

$$
       \xi_j\,O(\ell),\qquad
       \xi_j\exp\bigl(O(1)+2\lambda+2\lambda e^\lambda\bigr),
 \tag{6}
$$

respectively. This uses the total tilt mass estimate of the subpower proof and never averages $K(W)$ away.

## 3. Pass the marked gain through the actual Fourier window

The norm calculation of the subpower proof applies to the positive marked tilted polynomials with factors (6). On auxiliary polylogarithmic major arcs use Siegel–Walfisz in the fixed prime $F$ with weight $\log F$, for each actual cofactor and its label. This is one hard interval for $F$, with the cofactor phase and given physical cutoff. The rational factor is exactly $\mu(q)/\varphi(q)$ because the cofactor has no such small prime factors. At physical $x=hF$ the weighted prime density cancels its logarithmic denominator and leaves the weight $1/h$. Thus after the marked reciprocal replacement, for every base $W,s$ and label the real density is an integral in the normalized upper coordinate over the hard cofactor window, clipped by the external floor. The window has length $O(T/L)=O(1/\ell)$, canceling the unweighted overall reciprocal scale $O(\ell\tau_0)\tau_0^{-1}$. Its endpoints move by at most $|\log x-\log y|/L$ as $x$ changes, so the same real supremum bound controls total variation. No derivative of the marked density is needed.

The transforms are bounded by their factors (6) times $\min(X,|\beta|^{-1})$ in the major real coordinate, with the rational factor. All discrete errors have the arbitrary inverse-logarithmic precision just proved and that from Siegel–Walfisz. The arc fourth means follow as in the subpower proof, using $\int_{\mathbb R}\min(X,|\beta|^{-1})^4d\beta\ll X^3$ and $\sum_q\mu(q)^4/\varphi(q)^3<\infty$. At zero frequency the same calculation directly gives $X$ times (6), with arbitrary inverse-logarithmic additive error. On the auxiliary minors the mark stays in the actual cofactor coefficient with the tilt; the number of occurrences is $O(\ell)$ since every prime in $h$ except $s$ exceeds $e^{4T}$ and $h\ll X^{.6}$. The counting tilt costs only a fixed power of $L$, and the size tilt costs $\exp(O(\lambda/\sigma))=L^{o(1)}$ as in the subpower proof. Thus the original hard half-integer Perron separation in the **integer** product $hF$ and bilinear minor bound give arbitrary inverse-logarithmic saving in the fourth norms. This preserves the physical endpoints.

For joint loss from a gap prime and upper failure, apply the same genuine count and size Rankin penalties $\ell^{-2\log2}$ and $\exp(-\lambda\epsilon/(2\sigma))$ to (6). Coefficientwise domination for nonnegative polynomials is valid in fourth norm by the identity with the squared positive two-fold convolution. It follows that both norms in (4), after division by $X^{3/4}$, are at most

$$
 O_A\!\left(
       \xi_j\left\{\ell^{\,1-2\log2}
                +\exp\!\left(-\frac{\epsilon}{8\sigma}
                                      \log\frac1{\sigma}\right)\right\}
                         +L^{-A}\right).
 \tag{7}
$$

The additional size-tilt cost $2\lambda+2\lambda e^\lambda+O(1)$ is absorbed by $\epsilon\lambda/(4\sigma)$ for sufficiently small $\sigma$; on a fixed compact range of larger $\sigma$ adjust the constant as in the subpower proof. The same argument at zero frequency applies to sums, with positivity immediate. Since $\sigma\ge\tau_*$, the counting loss in braces divided by $\sigma$ is $O(1)$, using $2\log2>1$ and the definition of $\tau_*$. The size loss divided by $\sigma$ is bounded on $(0,\delta_0]$. Combining with (2) proves (4), with the **linear** width $\Delta_j$ rather than the reciprocal width alone, and also its zero-frequency version.

## 4. Exact calibration inside gaps and the common exceptional set

The normalization is controlled in each gap without replacing it by its limiting value. Use the one-arm calibration from the subpower proof: the genuine positive prime weight $\log F$ on a fixed nonzero hard interval $J_*\subset(0,\min(a,b,1))$ in the exponent $(L/2-\log F)/T$, actual physical interval $\mathcal J$, and exact masks at the chosen split. Its mass is $|J_*|\mathcal C_{X,Z}+O(X/\ell)$ uniformly by the count-sensitive density calculation. Between a node and a split in its gap the calibration loses only operands meeting **both** events $M_j\ge1$ and $\mathcal B_j$, independently of whether any paired target is present. This actual loss is at most the positive zero-frequency envelope from (7); the label $1$ suffices for domination. Thus

$$
 \sup_{Z_j^{\rm mesh}\le Z\le Z_{j+1}^{\rm mesh}}
   |\mathcal C_{X,Z}-\mathcal C_{X,Z_j^{\rm mesh}}|
                 \ll X(\Delta_j+\ell^{-1}).
 \tag{8}
$$

Since $\mathcal C_{X,Z}\ll X$ uniformly, $B_{\mathcal J}\ll X$, and $\|\Sigma\|_{\ell^2(N)}\ll\sqrt X$, this gives $\ell^2(N)$ norm $O(X^{3/2}(\Delta_j+\ell^{-1}))$ for the supremum of the change in the exact local comparator over the gap.

By (3), (4), Hölder and Parseval, the target $\ell^2$ norm of the genuine signed change from a node through its gap is similarly $O_A(X^{3/2}(\Delta_j+L^{-A}))$, since the opposite unmarked positive fourth norm is $O(X^{3/4})$. At each mesh node apply the common-split theorem, with squared norm $O(X^3\ell^{-1/5})$ uniformly. Take the supremum inside each gap after comparing to its bottom node. The square of the maximum over gaps is at most the sum of their squares, so the total over all even targets is

$$
 O_A\!\left(
    X^3\left\{\eta^{-1}\ell^{-1/5}
        +\sum_j \Delta_j^2
        +\eta^{-1}(\ell^{-2}+L^{-2A})\right\}\right)
     \ll X^3\ell^{-1/10}.
$$

Here $\sum_j\Delta_j^2\le\eta\sum_j\Delta_j=O(\eta)$, and $\eta=\ell^{-1/10}$. The lower interval from $Z_0$ to $X^{\tau_*}$ contributes only $O(X^3\ell^{-1/5})$ by the subpower theorem with its exact normalization. This proves (1) across the entire real split range. In particular choices can depend on the target with no extra continuity assumption.

For the sign consequences use the uniform $\mathcal C_{X,Z}\asymp X$, the positive absolute lower bound on the even singular series, and the fixed physical overlap. In the interior the comparator has magnitude $\gg X$ and fixed sign for all splits, so (1) gives the common interior exception count. On the full window discard endpoints within $X\ell^{-1/30}$ and apply (1) to any target admitting a wrong or zero sign outside those strips. The comparator's exact critical zero is unchanged. Nothing here bounds a single prescribed exceptional target.
