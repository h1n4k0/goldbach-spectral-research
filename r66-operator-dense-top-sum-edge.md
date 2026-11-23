# Dense top-sum edges of the genuine exterior means

**Scope.** This is an HS second moment of the actual negative sum-line term in the surviving literal mesowindow means. It covers all aliases near each entry's upper sum endpoint, including high shifts. The integer and continuous terms have the same cut, and both raw operands stay in the high–high region. It does not estimate the full dense covariance, the positive difference-line orientations, or an individual prescribed modulus.

## Statement

Use the [R60](r60-operator-localized-coarse-contrast-annulus.md)/[R63](r63-operator-signed-window-mean-modulus-average.md) reference windows and literal means. Let $1\le D\le W\le H/20$ and $H<M\le Q^\Gamma$, for fixed $0<\Gamma<1$. Let $\mathcal A\subset[Q,2Q]$ consist of $J$ distinct even moduli with original local Dirichlet GRH at each. Assume auxiliary Dirichlet GRH for every $q\le\lceil20\sqrt{QW}\rceil$, including $q=1$. We use the convention of [R65](r65-operator-dense-low-raw-alias-deletion.md), with raw arguments $x$ and $y$ supported below $Qb_I$ and $Qb_{I'}$, respectively, where $b_I=\sup I$.

In each entry $(I,I')$, retain just the genuine negative sum aliases $x+y=s=kN$, $k\ge1$, with

$$
 Q(b_I+b_{I'}-W)<s\le Q(b_I+b_{I'}).
 \tag{1}
$$

The term includes both the prime-power atom with its original unit condition and the original continuous affine integral multiplied by $\mathfrak S(s)$, with the signed difference taken before summation. The selection can be restricted further in an arbitrary entry- and modulus-dependent manner, using the same indices for the atom and model. For $I,I'$ in reference dyads starting at $V,U$, write $C_{N;V,U}(W)$ for this matrix between the full sets of means of those dyads. Then

$$
 \left(\frac1J\sum_{N\in\mathcal A}
        \|C_{N;V,U}(W)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\epsilon} Q^\epsilon\frac W{\sqrt{VU}}
          \left[\sqrt{\frac WJ}(QW)^{1/4}+\sqrt{\frac WQ}\right].
 \tag{2}
$$

One can instead require $W\le\min(V,U)/20$ for a particular dyad pair; $W\le H/20$ is only needed for a common global choice. The implicit constants are independent of the actual cuts and the selected set. The resulting operator matrix can be assembled by summing squares over the dyad pairs.

For example take $D=Q^{8/25},H=Q^{2/5},M=Q^{3/5}$, $J\gg Q^{99/100}$. The common $W=Q^{9/25}$ gives HS RMS $O_\epsilon(Q^{-3/200+\epsilon})$ on the whole annular edge component, with auxiliary range through $\lceil20Q^{17/25}\rceil$. Without a lower bound on $J$, the number of exceptions at threshold $Q^{-1/200}$ is $O_\epsilon(Q^{97/100+\epsilon})$ among the selected moduli satisfying the hypotheses. In the top comparable dyads $V,U\asymp Q^{3/5}$, $W=Q^{47/100}$ alone gives HS RMS $O_\epsilon(Q^{-9/400+\epsilon})$ and needs auxiliary moduli through $\lceil20Q^{147/200}\rceil$. These are genuine larger per-entry alias windows than the [R64 power-saving sparse bound](r64-operator-sparse-alias-window-mean-variance.md) at this annulus. No low-raw-coordinate cut is involved: (1) implies $x/Q>b_I-W,\ y/Q>b_{I'}-W$ and $k\gtrsim V+U$. In particular these edges lie entirely outside the R65 deleted low regions in its example and outside the uniformly small-$k$ deletion.

## 1. An exact short representation only on the selected lines

Put $L=\log(3Q)$, $X=QW$, and $\omega_V=\sqrt{D/V}$. At $Q\le t\le2Q$, the genuine normalized raw mean $h_{I,t}$ is R65 (2). In the cutoff representation R65 (3) write $a_V=QV$ and use $\omega_V/\sqrt{a_V}$ outside the profile $\sqrt{x/a_V}$. Denote the cutoff measure on $QI$ by $\mu_{I,t}$. If $\ell_I=|I|$, its density is $\ll_\Gamma (Q\sqrt{D\ell_I})^{-1}$, and its total variation is $\ll_\Gamma\sqrt{\ell_I/D}$. These follow directly from $w_t(z)=z^{-3}[(Qz)^{-2/\log t}+(Qz)^{-1/4}]\asymp_\Gamma V^{-3}$ in R65 (2), including for a clipped final window. The same holds for $Q\partial_t\mu_{I,t}$, since $Q|\partial_t w_t(z)|\ll_\Gamma w_t(z)$ also bounds the derivative of the normalizer. In particular, for either measure,

$$
 \|\mu_{I,t}\|_{\rm TV}\,|d\mu_{I,t}(u)|\ll_\Gamma (QD)^{-1}du.
 \tag{3}
$$

Below the notation for $\mu$ also permits that signed derivative.

Let $d\eta(Z)=X^{-1}\mathbf1_{[X,2X]}(Z)dZ$. Replace each raw profile, only for the computation of the selected lines, by

$$
 g_{I,t}(x)=\frac{\omega_V}{\sqrt{a_V}}
 \int_{QI}\int_X^{2X}\sqrt{x/a_V}\,
        \mathbf1_{u-Z<x\le u}\,d\eta(Z)\,d\mu_{I,t}(u).
 \tag{4}
$$

If $x$ appears on (1) in the original support, necessarily $x>Qb_I-X$; thus for every $u\in QI$ with $x\le u$, the new lower constraint is automatic up to an $\eta$-null endpoint. Conversely (4) introduces no points outside the old upper support. The same holds on the other leg. This is an equality for each integer point and the original continuum integral on those lines, not a smoothing approximation to the target. The new support lies in $[Qb_I-QD-2X,Qb_I]$, of length $O(X)$ in a fixed dyad at scale $a_V$. Its sup norm plus total variation is $O(\omega_V/\sqrt{a_V})$, by the elementary weights in (4). The same is true for $Q\partial_t g_{I,t}$. Below the actual $t$-dependence is retained throughout.

## 2. Averaging the internal raw cutoffs

For a modulus $q$ in the auxiliary range, let $\mathbf F(z)$ be the vector over reduced residues of $\psi(z;q,r)-z/\phi(q)$, extended by zero on nonreduced residues. The finite-height local Selberg estimate of [R59](r59-operator-balanced-arcs-cuberoot-prefix.md), as used in R60 (7), gives

$$
 \int_{a/2}^{3a}\|\mathbf F(z+h)-\mathbf F(z)\|_2^2dz
       \ll_\Gamma a h L^4\qquad (1\le h\le a/4)
 \tag{5}
$$

on our raw scales $a=a_V,a_U$; a bounded dyadic cover suffices. This also holds for $0<h<1$: at most one integer atom occurs per slide interval, and each atom is included for slide measure at most $h$; the total squared marks are $O(aL^2)$. The continuous drift contributes $O(ah^2)$. We will integrate starting points and endpoints in slightly shifted dyads within this range.

For an elementary interval $(u-Z,u]$ in (4), with $e(z)=\exp(2\pi iz)$, Abel's right-end form is

$$
 \int_{(u-Z,u]} b(x)\,d\mathbf F(x)
 =b(u-Z)[\mathbf F(u)-\mathbf F(u-Z)]
    +\int_{u-Z}^u b'(x)[\mathbf F(u)-\mathbf F(x)]dx ,
 \tag{6}
$$

where $b(x)=\sqrt{x/a_V}\,e(\beta x)$. Its derivative is $O(a_V^{-1}+|\beta|)$ on the interval. By (5) and Minkowski, the $L^2(du;\ell^2)$ norm over the whole cutoff dyad $u\in[a_V,2a_V]$ in (6) is

$$
 \ll L^2\sqrt{a_V X}\,(1+|\beta|X).
 \tag{7}
$$

In fact the first term uses the lag $Z$, and the integral uses lags between $0$ and $Z$, with integral of $h^{1/2}$ of size $O(X^{3/2})$. This avoids using two separate pointwise GRH prefix estimates. By (3), Cauchy in the signed cutoff measure, and disjointness in $u$ of the $QI$ for one dyad,

$$
 \sum_{I,r}\left|\int g_{I,t}(x)e(\beta x)\,dF_r(x)\right|^2
       \ll_\Gamma (W/V)(1+|\beta|X)^2 L^4 .
 \tag{8}
$$

Indeed the factor from (4) and (3) outside the integrated squared norm is $(\omega_V^2/a_V)(QD)^{-1}$, and $(\omega_V^2/a_V)(QD)^{-1}a_VX=W/V$. The probability average in $Z$ is handled by Jensen.

There is the same improvement in the integrated short-increment estimate. For $\ell\ge2$, with $\ell\le X$, put $v=s-u$ in the slide interval $(s,s+\ell]$ and intersect with $(u-Z,u]$. The intersection is an interval with endpoints $u+\max(v,-Z)$, $u+\min(v+\ell,0)$ when nonempty, and has length $h(v)\le \ell$. For fixed $v$, (5), (6) with $\beta=0$, and Minkowski give squared $L^2(du;\ell^2)$ bound $O(a_V h(v)L^4)$ for the weighted intersection. The assertion includes $h(v)<1$ by (5). All the offsets are at most $2X$ in magnitude when the interval is nonempty. Integrating in $v$ uses
$\int_{\mathbb R} h(v)\,dv=Z\ell$, the integral of the overlap of two intervals. Hence (3) and (4) give

$$
 \int_{\mathbb R}\sum_{I,r}
       \left|\int_{(s,s+\ell]}g_{I,t}(x)\,dF_r(x)\right|^2ds
   \ll_\Gamma (W/V)\ell L^4 .
 \tag{9}
$$

In particular this argument averages across the disjoint exact cutoff supports, regardless of whether $\ell$ is shorter or longer than $QD$. No random shift of the reference windows is used. By convolution with the length-$\ell$ indicator, the corresponding Fourier squared integral for each $|\beta|\le 1/(4\ell)$, summed over $I,r$, is $\ll (W/V)L^4/\ell$. Equations (8) and (9) hold with the normalized $t$-derivative on the leg as well.

## 3. Balanced arcs at the width, not the height

For all the windows in the $V$-dyad write the vectors

$$
 A_V(\alpha)_I=\sum_n\Lambda(n)g_{I,t}(n)e(n\alpha),
 \qquad B_V(\beta)_I=\int g_{I,t}(x)e(x\beta)\,dx,
 \qquad c_V=\sqrt{W/V}.
$$

By Parseval, the length $O(X)$ and the per-window sup and variation bounds in §1,

$$
 \|A_V\|_{L^2(\mathbb T;\ell^2)}\ll L c_V,\quad
 \|B_V(\beta)\|_2\ll a_V^{-1/2}\min(X,|\beta|^{-1}).
 \tag{10}
$$

We used that there are $O(V/D)$ windows and $\omega_V^2=D/V$. All vector statements below have the analogous form for the $U$-dyad.

Take $P=\lfloor\sqrt X/10\rfloor$, with the R59 disjoint major arcs of radii $\delta_q=2P/(qX)$. Off the majors, Dirichlet approximation with integer cutoff $\lceil X/P\rceil$ gives a rational center of denominator $P<q\le\lceil20\sqrt X\rceil$ and $|\beta|X\le1$, for large $Q$. At any rational approximation $a/q+\beta$ write $A_V=M_V+E_V+Z_V$, with $M_V=\mu(q)B_V(\beta)/\phi(q)$. The error $E_V$ is the additive residue transform of the vector in (8), and $Z_V$ is the original nonunit prime-power term at $q$. The latter has $\|Z_V\|_2\ll L^2/\sqrt{a_V}$ uniformly. Equation (8) yields

$$
 \|E_V(a/q+\beta)\|_2\ll c_V\sqrt q\,(1+|\beta|X)L^2 .
 \tag{11}
$$

In particular the minor $\ell^2$ supremum of $A_V$ is $\ll_\epsilon Q^\epsilon c_V X^{1/4}$, including the principal term by (10). Thus the minor part of $A_V\otimes A_U$ has $L^2(\mathbb T;{\rm HS})$ norm $\ll_\epsilon Q^\epsilon c_V c_U X^{1/4}$.

On the majors use $\ell=qX/(8P)\le X$ in (9) and finite additive Parseval over $a\bmod q$. The $q$-arc integrated square norm of $E_U$ is $\ll c_U^2 L^4 P/X$. Multiply it by the squared supremum (11) for $E_V$, and use $\sum_{q\le P}q(1+P/q)^2\ll P^2\log(2P)$: the double error has the same $L^2$ bound as the minors. For the single error $E_V\otimes M_U$, additive Parseval and (8) bound its squared norm by

$$
 \ll c_V^2 L^4\frac{X^2}{a_U}\sum_{q\le P}
                         \frac{q}{\phi(q)^2}\delta_q
 \ll c_V^2c_U^2 L^4 P ,
 \tag{12}
$$

since $(1+|\beta|X)\|B_U(\beta)\|_2\ll X/\sqrt{a_U}$ and $\sum_q\phi(q)^{-2}<\infty$. This suffices for the same bound. Transpose for the other single error. The normalized derivative of the product has two terms, each satisfying the same estimates because every one-leg bound includes $Q\partial_t g$.

## 4. Sampling and restoring the exact model

For a fixed entry, there are $O(W)$ selected positive $k$ in (1), since $N\ge Q$ and $W\ge1$. If $c_{s,I,I'}(t)$ is any fixed Fourier coefficient tensor, the squared HS sum over $N$ after this entry-dependent selection is at most

$$
 \ll_\epsilon WQ^\epsilon
           \sum_s\|c_s(t)\|_{\rm HS}^2 .
 \tag{13}
$$

Apply Cauchy across the selected $k$ in each entry, then sum entries and use that the number of representations $s=kN$ is at most $\tau(s)\ll_\epsilon Q^\epsilon$ for the positive selected indices $s\ll QM$. Dropping masks is legitimate only after the entrywise Cauchy. The actual profiles move with $N$; apply $c_{s}(N)=c_s(Q)+\int_Q^{2Q}\mathbf1_{t\le N}\partial_t c_s(t)\,dt$, the derivative bounds just proved, and Minkowski with the same estimate for each subset $N\ge t$. This gives the first term in (2) from the three major error products and the minor product, since $c_Vc_U=W/\sqrt{VU}$.

The terms involving $q$-nonunits on the majors are pointwise errors in $N$. Write them as $Z_V\otimes A_U+A_V\otimes Z_U-Z_V\otimes Z_U$ on the union of arcs. For each entry the absolute sum of its selected Fourier coefficients is bounded by $O(W)$ times the $L^1$ norm of its entrywise product. Taking HS and Minkowski, using (10) and the $Z$ sup norm, gives $\ll L^{O(1)}(W/\sqrt{VU})\sqrt{W/Q}$; the product of two unit errors is smaller. This argument does not impose a common alias mask on the entry pairs. The original $N$-nonunits can also be removed pointwise: for an $N$-nonunit prime power on one leg, each fixed line has at most one partner. Bounding the total nonunit marks by $O(L^2)$, per-window sup weights by $O(\omega_V/\sqrt{QV})$, and counting $O(W)$ lines per entry gives, after HS aggregation, $\ll L^{O(1)}W/(Q\sqrt{VU})$. This retains all admissible proper powers.

It remains to extend the main arc model integral and Ramanujan series exactly as in R65, but with the new width $X$. For an individual pair put $b_V'=\omega_V/\sqrt{QV}$, $b_U'=\omega_U/\sqrt{QU}$. The full continuous integral on a line is bounded by $O(b_V'b_U'X)$ from support lengths and sup weights. The omitted $\beta$-tail at denominator $q\le P$ is $O(b_V'b_U'/\delta_q)=O(b_V'b_U'qX/P)$ by the two BV Fourier decays. Uniformly at sampled $s$, the absolute Ramanujan sums satisfy

$$
 \sum_{q\le P}\frac{\mu(q)^2|c_q(s)|q}{\phi(q)^2}\ll_\epsilon Q^\epsilon,
 \qquad
 \sum_{q>P}\frac{\mu(q)^2|c_q(s)|}{\phi(q)^2}\ll_\epsilon Q^\epsilon/P .
 \tag{14}
$$

For squarefree $q$, use $|c_q(s)|\le(q,s)$, $\phi(q)^{-2}\ll_\epsilon q^{-2+\epsilon}$, and split by $d=(q,s)$; both estimates follow from divisor multiplicity. Summing errors over the $O(W)$ lines and aggregating windows multiplies by $O(W\sqrt{VU}/D)$; hence the pointwise RMS cost is $\ll_\epsilon Q^\epsilon W^2/(P\sqrt{VU})$, the second term in (2). Fourier inversion for the product $B_V B_U$ on the sum line restores the continuous affine integral with exactly the weights (4); their equality to the original weights there was proved in §1. The full Ramanujan series gives the original $\mathfrak S(s)$. The negative sign, operator normalization and unit convention have therefore not changed.

Finally for the example, the leading power for the common width is $1/4+(7/4)(9/25)-(99/100)/2-2/5=-3/200$. The pointwise term is smaller, and the unnormalized primary mass is $O_\epsilon(Q^{24/25+\epsilon})$; summing the logarithmically many dyad pairs and Chebyshev give the stated exception count. At the top comparable dyads the power is $1/4+(7/4)(47/100)-(99/100)/2-3/5=-9/400$. None of these estimates covers the part of a high–high dyad with sum separated from its top endpoint by more than $QW$. In particular, tiling the full raw dyad into short subrectangles and applying the estimate without new cross-tile cancellation does not give a full mean–mean bound.
