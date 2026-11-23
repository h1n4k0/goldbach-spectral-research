# A signed modulus mean for the surviving exterior window means

**Scope.** This estimates the signed first moment, over an ordinary interval of even moduli, of the **actual** weighted mesowindow-mean block left after contrast deletion. It is not a mean of norms, a variance bound, an estimate on an arbitrary selected set, or a pointwise cancellation statement. The proof uses the true continuous singular-series model and improves the auxiliary arithmetic estimate by exploiting a residue-vector GRH bound even at moving endpoints.

## Statement

Write $L=\log Q$, and fix $0<\Gamma<1$. Use the [R60 reference partition](r60-operator-localized-coarse-contrast-annulus.md), $1\le D\le H<M\le Q^\Gamma$, with transported physical window $I_N=(Q/N)I$ at every even $N\in[Q,2Q]$. Let $e_{I,N}=r_N\mathbf1_{I_N}/\|r_N\mathbf1_{I_N}\|_2$ be its genuine unit mean direction. Let $\mathcal F,\mathcal G$ be two fixed collections of reference windows, contained in $[H,M_1]$, $[H,M_2]$ respectively, with $M_i\le M$. Their physical isometries $U_{\mathcal F,N},U_{\mathcal G,N}$ send the common $\ell^2$ index bases to these unit mean directions. Take any real half-open interval $\mathcal I\subset[Q,2Q]$ of length $\Delta$ with $J=\#(\mathcal I\cap2\mathbb Z)\ge1$. Assume the manuscript's local Dirichlet GRH at each even $N$ in $\mathcal I$, and auxiliary Dirichlet GRH for all characters of integer moduli $q\le\lceil8M\rceil+2$, including $q=1$. Then

$$
 \left\|\frac1J\sum_{\substack{N\in\mathcal I\\N\ {\rm even}}}
             U_{\mathcal F,N}^{*}T_N U_{\mathcal G,N}\right\|_{\rm HS}
 \ll_{\Gamma,\epsilon} Q^\epsilon\frac{\sqrt{Q M_1M_2}}{J}.
 \tag{1}
$$

The estimate holds for either assignment of the two families to the two legs. On a full shell, it gives $O_\epsilon(Q^{-1/100+\epsilon})$ for all genuine means up to $M_1=M_2=Q^{49/100}$; one can take $D=Q^{8/25}$ and $H=Q^{7/20}$, so these windows are beyond the [R59 full-prefix cutoff](r59-operator-balanced-arcs-cuberoot-prefix.md) for large $Q$. The same rate holds for a separated rectangle with lower family up to $M_1=Q^{19/50}$ and upper family up to $M_2=Q^{3/5}$, for example starting the upper family at $Q^{11/20}$. Other conditions with $M_1M_2=o(Q)$ give the corresponding signed mean estimate where the $Q^\epsilon$ loss is affordable. If using [R62](r62-operator-full-mixed-contrast-deletion.md) on the same moduli for contrast deletion, its additional auxiliary range is a separate hypothesis.

## 1. Exact transported means and regularity

Fix reference window $I$ of positive length $\ell_I\le D$ in the dyadic piece $[V,2V]$. For real $t\in[Q,2Q]$ define

$$
 w_t(z)=z^{-3}\left((Qz)^{-2/\log t}+(Qz)^{-1/4}\right),\qquad
 h_{I,t}(x)=\frac{\sqrt{2\pi x}}{Q}
       \frac{\int_{I,\;z\ge x/Q}w_t(z)\,dz}
            {\left(\int_I w_t(z)\,dz\right)^{1/2}},
 \qquad x>0 .
 \tag{2}
$$

Extend $h_{I,t}$ by zero at $x\le0$. This is the **exact** raw Volterra weight of $e_{I,N}$ when $t=N$. Indeed, with $a=N/Q,\ z=au$, one has $r_N(z/a)^2=a^3w_N(z)$ and $du=dz/a$. In the raw test formula $\sqrt{2\pi x}N^{-1}\int_{u\ge x/N}r_N(u)e_{I,N}(u)du$, the numerator gains $a^2$, the mean normalizer gains $a$, and $a/N=1/Q$. There is no moving raw support or discarded normalization scalar. In particular the raw weight below $QI$ is a genuine $\sqrt x$-prefix, retained here.

Uniformly in $t$, $h_{I,t}$ is supported on $[0,2QV]$, has size at most $C b_V$ with $b_V=\sqrt D/(\sqrt Q V)$, and

$$
 |t\partial_t h_{I,t}(x)|\ll b_V,\qquad
 |\partial_x h_{I,t}(x)|\le G_I(x),\qquad
 \int_{\mathbb R}G_I(x)\,dx\ll b_V .
 \tag{3}
$$

The first follows by logarithmic differentiation of $w_t(z)$, since $t|\partial_t w_t(z)|\ll_\Gamma w_t(z)$. To see the common integrable envelope for all $t$, use $b_{V,I}=\sqrt{\ell_I}/(\sqrt Q V)\le b_V$. The derivative of $\sqrt x$ contributes $O(b_{V,I}(\sqrt{QV\,x})^{-1}\mathbf1_{0<x\le2QV})$. Differentiating the lower cumulative endpoint contributes $O(b_{V,I}/(Q\ell_I))\mathbf1_{QI}$; these both have $L^1$ norm $O(b_{V,I})$. This also justifies Abel summation for the actual weights including the square-root origin. The derivative in $t$ vanishes outside the fixed raw support.

For a pair $I,I'$ in dyadic pieces $V,U$ assume $V\le U$ by symmetry. The genuine matrix entry of $T_N$ has the exact three oriented aliases

$$
 m=n+kN,\quad m=n-kN,\quad m=kN-n,
 \qquad k\ge1,\quad\hbox{signs }+,+,-.
$$

On each line the arithmetic weight is $\Lambda(n)\Lambda(m)h_{I,N}(n)h_{I',N}(m)$ with the original units, and the model is $\mathfrak S(kN)\int h_{I,N}(x)h_{I',N}(m(x,N))\,dx$. This is the genuine signed physical realization, with no equality line $k=0$. Since $n\le2QV,\ m\le2QU$, only $k\le4U$ can occur. Dropping the original unit restrictions temporarily changes the sum over $N$ by $O_\epsilon(Q^\epsilon D/V)$: on each raw leg the total $\Lambda$-weight of the prime powers of primes dividing $N$ is $O(L^2)$; each such power has $O(U)$ possible partners with bounded log mark, and a term has test weight at most $b_Vb_U$. Now sum over $J\ll Q$. All proper powers not disallowed by units are retained.

## 2. Switch a line and exploit residue vectors under moving endpoints

Fix $k$ and one orientation. Switch the even-modulus condition by writing $t=(m-n)/k,\ (n-m)/k,\ (m+n)/k$ respectively, and requiring $t\in\mathcal I,\ m\equiv \pm n\bmod q$ with $q=2k$. In each case, $t$ is strictly monotone in either raw variable with slope of absolute value $1/k$. For fixed $n$, allowed $m$ lies in an interval $J_k(n)$, clipped to $[0,2QU]$, whose two endpoints are $1$-Lipschitz in $n$ (choose the clipped endpoints by monotone minima and maxima; empty intervals may be discarded). The corresponding weight is $H(n,m)=h_{I,t}(n)h_{I',t}(m)$. Its modulus variable in the switched sum is exactly the original $t=N$ on allowed integer pairs. For $q\le8M$, the total $\Lambda(n)$ over nonunit residues $(n,q)>1$ is $O(L^2)$, and each such $n$ has $O(QU/q+1)$ possible $m$. These can be dropped at total cost $O_\epsilon(Q^\epsilon D/V)$ after summing $k$, by $b_Vb_U=D/(QVU)$. They can also be restored when replacing the $n$-leg's prime sum by its integral, at that same scale.

For a unit residue $r\bmod q$, set $F_r(x)=\psi(x;q,r)-x/\phi(q)$ and put $F_r=0$ for nonunits. The [auxiliary GRH progression estimate](r43-operator-signed-modulus-window.md) in its character form and character Parseval yield

$$
 \sum_r|F_r(x)|^2\ll QU L^4\qquad (0\le x\le2QU).
 \tag{4}
$$

For the short raw endpoint range near zero this also holds trivially. Uniformly for $x,x'\in[0,2QU]$ with $|x-x'|\le q$,

$$
 |F_r(x)-F_r(x')|\ll_\epsilon Q^\epsilon
 \tag{5}
$$

for the same residue $r$: there are at most two raw integers in that residue in such an interval, each of mark $O(L)$, and the mean change is at most $q/\phi(q)\ll_\epsilon Q^\epsilon$. Endpoint convention changes are also covered.

Replace the $m$-sum over its actual residue in $J_k(n)$ by the Lebesgue integral with density $1/\phi(q)$, using Abel summation. The two endpoint terms are at most $Cb_Vb_U|F_{\pm n}(x(n))|$ per fixed $n$ in the inner replacement. Group the $n$-range $[0,2QV]$ in integer blocks of length $q$. The endpoint within each block differs from one common value by at most $q$. By (4) and Cauchy in residues, at the common value the total of $|F_r|$ over the block is $O(\sqrt{qQU}L^2)$; (5) adds $O_\epsilon(qQ^\epsilon)$, absorbed as $q\ll U$ and $\sqrt{qQU}\ge c q$ for large $Q$. The prime mark of the $n$-leg is bounded by $O(L)$. As $q\le8M=o(Q)$ and $V\ge1$, there are $O(QV/q)$ such blocks. This bounds the endpoint errors by

$$
 O_\epsilon\big(Q^\epsilon b_Vb_U QV\sqrt{QU/q}\big).
 \tag{6}
$$

This residue averaging uses a separate GRH $\ell^2$ input, not a supremum of each residue error over individually chosen endpoints.

For completeness there are two parts of the interior variation error. From (3) on the interval of allowed $m$,

$$
 |\partial_m H(n,m)|\ll b_V\big(G_{I'}(m)+b_U/(Qk)\big).
 \tag{7}
$$

For the $G_{I'}$-part, fix $m$, sum $\Lambda(n)|F_{\pm n}(m)|$ by $q$-blocks using (4), and integrate $G_{I'}$ with its $L^1$ bound in (3). This gives (6). For the parameter-derivative part keep the restriction $t\in\mathcal I$ while summing over $n$: at fixed $m$ the allowed $n$-range has length $O(\min(QV,k\Delta))$, so only this many integers plus a partial $q$-block need be counted through (4). Also, whenever any $n$ is allowed, $m\ll Q(V+k)$ by the actual alias orientation. After integrating in $m$, the bound is again (6), because

$$
 \frac{V+k}{k}\left(\min(QV,k\Delta)+q\right)\ll QV .
 \tag{8}
$$

For $k\le V$ use $\Delta\le Q,\ q=2k$; for $k>V$ use $q\ll U=o(Q)\le QV$. Thus variation in the exact $t$-dependent mean profiles causes no new loss. The above uses the whole ordinary interval of even moduli in the switch; it does not apply to an arbitrary sparse subset of $t$.

After this replacement change the $n$-leg's $\Lambda(n)$ to Lebesgue measure, restoring the temporarily discarded nonunit $n$ at the already stated cost. For fixed $m$, the $n$-weight has sup norm and total variation $O(b_Vb_U)$ on its clipped interval: its genuine spatial derivative envelope integrates as (3), its parameter derivative is $O(b_Vb_U/(Qk))$ over a range of length at most $k\Delta$, and the interval indicator adds at most two endpoint jumps. Thus ordinary RH and Abel summation integrated over $m\le2QU$ give error $O(b_Vb_U QU\sqrt{QV}L^2/\phi(2k))$. Sum this and (6) over $k\le4U$, using $\sum_{k\le4U}k^{-1/2}\ll\sqrt U$ and $\sum_{k\le4U}\phi(2k)^{-1}\ll_\epsilon Q^\epsilon$. The total unnormalized error is

$$
 O_\epsilon(Q^\epsilon D\sqrt Q),
 \tag{9}
$$

because the first sum is $O_\epsilon(Q^\epsilon b_Vb_U QV\sqrt{QU}\sqrt U)=O_\epsilon(Q^\epsilon D\sqrt Q)$, and the second is $O_\epsilon(Q^\epsilon D\sqrt{Q/V})$. This is for one fixed window pair and retains an exact signed benchmark for comparison.

## 3. The original model has exactly the switched coefficient

The resulting arithmetic main term for each line is

$$
 \frac{k}{\phi(2k)}\int_{\mathcal I} I_k(t)\,dt,\qquad
 I_k(t)=\int h_{I,t}(n)h_{I',t}(m(n,t))\,dn .
 \tag{10}
$$

Here $dm=k\,dt$ in absolute value at fixed $n$ for all three orientations. Uniformly in $k$ the function $I_k(t)$ has sup norm plus total variation $O(b_Vb_U QV)=O(D/U)$. Indeed each fixed $n$-factor has this regularity in $t$ from (3); in the moving $m(n,t)$ factor, the spatial derivative is dominated by $G_{I'}$ on a monotone affine image, and its parameter derivative by (3) over $[Q,2Q]$. Then integrate over $n\le2QV$.

For even $N$ use the exact expansion

$$
 \mathfrak S(kN)=\mathfrak S(2k)
 \sum_{\substack{d\mid N,\ d\ {\rm odd,\ squarefree}\\(d,k)=1}}
       \prod_{p\mid d}(p-2)^{-1}.
$$

The $2d$-progression average of $I_k$ is its integral divided by $2d$ with a uniform BV error $O(D/U)$, by elementary floor discrepancy and Abel summation. Sum the resulting model errors for $d\le2Q$ and extend the main coefficient to all $d$: using $\prod_{p\mid d}(p-2)^{-1}\ll_\epsilon d^{-1+\epsilon}$ and $\mathfrak S(2k)\ll_\epsilon k^\epsilon$ costs $O_\epsilon(Q^\epsilon D/U)$ per $k$. The exact Euler product for the extended mean coefficient is

$$
 \frac{\mathfrak S(2k)}2\prod_{p>2,\;p\nmid k}
       \left(1+\frac1{p(p-2)}\right)=\frac{k}{\phi(2k)}.
$$

Thus the original model cancels precisely (10), on each orientation before applying $+,+,-$. Summing the model errors is $O_\epsilon(Q^\epsilon D)$, absorbed in (9). Afterwards restore the original units; their cumulative cost was also smaller. No replacement by an averaged independent model has been made.

## 4. Signed HS aggregation and limits

Dividing (9) by $J$ bounds each actual signed first-moment entry by $O_\epsilon(Q^\epsilon D\sqrt Q/J)$. There are $O(V/D)$ windows in dyad $V$ and $O(U/D)$ in dyad $U$, because $D\le H$. Therefore the signed HS bound on this dyad pair is $O_\epsilon(Q^\epsilon\sqrt{QVU}/J)$. Sum the $O(L^2)$ dyad pairs and apply $V\le M_1,\ U\le M_2$ for the assigned families, with transposition if needed. This proves (1) for the true normalized moving physical directions. For $J\asymp Q$, its power is $\tfrac12(\gamma_1+\gamma_2-1)$ when $M_i=Q^{\gamma_i}$, giving the stated two examples.

The argument genuinely addresses the window means surviving [R62](r62-operator-full-mixed-contrast-deletion.md): the tests are the normalized $r_N$ directions themselves, and their nonlocal raw prefix was kept. It controls only their **signed first moment**, which permits cancellation across different moduli. It neither estimates the norm for most of the moduli nor controls the same signed mean over a prescribed sparse subfamily. The full signed/operator covariance at one $N$, its variance on these scales, and weak S remain open.
