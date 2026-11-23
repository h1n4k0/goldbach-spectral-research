# A contiguous bulk alias band of the actual exterior means

**Scope.** This is a signed Hilbert–Schmidt second moment for the literal mesowindow means, in a fixed interval of raw alias locations. The interval can be anywhere in the bulk and all three original line orientations are included. In particular the result applies to positive difference aliases far from either edge, with both raw operands in the long–long complement of R65. There is no inference to the sum of all such intervals, to variance at a prescribed modulus, or to weak S.

## Statement

Use the [R60](r60-operator-localized-coarse-contrast-annulus.md)/[R63](r63-operator-signed-window-mean-modulus-average.md) reference partition and exact transported means, with $1\le D\le H<M\le Q^\Gamma$, where $0<\Gamma<1$ is fixed. Let $1\le W\le H/20$, and let $\mathcal A\subset[Q,2Q]$ consist of $J\ge1$ distinct even moduli satisfying original local Dirichlet GRH. Assume auxiliary Dirichlet GRH for every $q\le\lceil20\sqrt{QW}\rceil$, including $1$.

For the entries between any pair of physical dyads of starts $V,U$, take a fixed raw interval of length at most $QW$ in the positive variable $s=kN$, $k\ge1$. Aliases outside the common physical support bound $s\le 4QM$ are identically zero and can be dropped. The location of the interval can differ between the dyad pairs and the orientations, but does not vary with $N$ or with individual windows within the dyad pair. Within that interval, one may further select aliases arbitrarily by entry and by $N$. In the raw legs impose any fixed rectangular interval restriction, also allowed to differ by dyad pair and orientation, but independent of $N$ and of individual windows there. These restrictions are imposed jointly on the unit-restricted prime-power terms and the exact continuous affine integrals with $\mathfrak S(kN)$, retaining the signs $+,+,-$ and excluding the equality line. A bounded disjoint union of such rectangles is also allowed.

Let $C_N(W)$ be the resulting actual signed matrix, with the physical dyad pair matrices assembled on the literal mean space. Then uniformly in interval locations, rectangular cuts and allowed selections,

$$
 \left(\frac1J\sum_{N\in\mathcal A}\|C_N(W)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\epsilon} Q^\epsilon\left[
       \sqrt{\frac{W}{J}}(QW)^{1/4}+\sqrt{\frac WQ}\right].
 \tag{1}
$$

For a single dyad pair one only needs $W\le\min(V,U)/20$. For $H=Q^{2/5},M=Q^{3/5},D=W=Q^{8/25}$, $J\gg Q^{99/100}$, (1) is $O_\epsilon(Q^{-1/200+\epsilon})$. The auxiliary GRH range is through $\lceil20Q^{33/50}\rceil$. For this example and arbitrary selected set size, there are $O_\epsilon(Q^{197/200+\epsilon})$ exceptions at threshold $Q^{-1/400}$. This width is strictly larger than the $Q^{9/50}$ generic sparse allowance in the [R64 example](r64-operator-sparse-alias-window-mean-variance.md), with the essential specialization to a common interval in raw $s$. It is not restricted to the [R66 top sum strips](r66-operator-dense-top-sum-edge.md). E.g. on the top comparable dyads it applies to $y-x$ in a band centered around $QV/3$, with both $x,y$ comparable to $QV$. When both dyad starts are comparable to $V$, the allowed rectangles can impose exactly the R65 raw complement, by splitting its union into two disjoint rectangles.

## 1. Exact partition in the raw coordinate

Write $L=\log(3Q)$, $X=QW$, $a=QV$, $\omega_V=\sqrt{D/V}$. For $Q\le t\le2Q$, the exact normalized raw profile from [R65](r65-operator-dense-low-raw-alias-deletion.md) (2)–(3) is

$$
 h_{I,t}(x)=\frac{\omega_V}{\sqrt a}\sqrt{x/a}
                 \int_{QI}\mathbf1_{x\le u}\,d\mu_{I,t}(u)
 \quad(x>0).
 \tag{2}
$$

Extend by zero to nonpositive $x$. For either the undifferentiated cutoff measure or $Q\partial_t\mu_{I,t}$, its TV norm is $O_\Gamma(1)$ and

$$
 \|\mu_{I,t}\|_{\rm TV}\,|d\mu_{I,t}(u)|
                    \ll_\Gamma (QD)^{-1}du .
 \tag{3}
$$

Indeed its density and total variation are bounded by $O_\Gamma((Q\sqrt{D|I|})^{-1})$ and $O_\Gamma(\sqrt{|I|/D})$, respectively, including for clipped final windows and with the derivative of the normalizer; see R66 §1. Use $\mu$ for either choice in the estimates below.

The tent partition $\zeta_i(x)=(1-|x/X-i|)_+$, $i\in\mathbb Z$, has overlap at most two and $\sum_i\zeta_i(x)=1$. Put

$$
 g_{I,i,t}(x)=h_{I,t}(x)\zeta_i(x)\mathbf1_R(x),
 \tag{4}
$$

where $R$ is the leg's fixed raw interval, with exactly its desired endpoint conventions at integers. An infinite or absent restriction is permitted. For orientation $\sigma_1 x+\sigma_2 y=s$, $\sigma_1,\sigma_2\in\{-1,1\}$, and the chosen band $s\in[s_0,s_0+X]$, only tile pairs with $|\sigma_1 i+\sigma_2 j-s_0/X|\le3$ can contribute, because $|x/X-i|,|y/X-j|\le1$ on their supports. Call this the tile relation. It is fixed in $t$ and $N$; both row and column degrees are $O(1)$. When the raw coefficient has $s$ in the band, summing the terms over this relation gives exactly the original restriction, by the partition of unity. This holds for the continuous model and the actual atom, regardless of profile variation or integer endpoints.

For vectors $B_i$ indexed by windows at $V$ and $C_j$ indexed by windows at $U$, the relation gives

$$
 \left\|\sum_{i\sim j} B_i\otimes C_j\right\|_{\rm HS}
 \ll \left(\sum_i\|B_i\|^2\right)^{1/2}
      \left(\sum_j\|C_j\|^2\right)^{1/2}.
 \tag{5}
$$

This is Cauchy on the edge set and the two degree bounds. No assumption about signs in the tensor sum is made. We apply it with Fourier arguments of the required signs on each leg.

## 2. Aggregate local residue estimates with no tile-count loss

Let $\mathbf F(z)$ be the reduced-residue vector
$\psi(z;q,r)-z/\phi(q)$, with zero on nonreduced residues and with $\mathbf F(z)=0$ for $z\le0$. The pointwise GRH bound of R59/R60 is $\|\mathbf F(z)\|_2\ll_\Gamma\sqrt z L^2$ in our polynomial ranges for $z>0$. The finite-height Selberg estimate of [R59](r59-operator-balanced-arcs-cuberoot-prefix.md), as used in R66, implies

$$
 \int_{-2X}^{4a}\|\mathbf F(z+h)-\mathbf F(z)\|_2^2dz
                    \ll_\Gamma a h L^4
           \qquad (0<h\le2X).
 \tag{6}
$$

For $h\ge1$, use the pointwise bound on $-h\le z\le 2h$, then sum the local dyadic Selberg bounds on $z\ge2h$, with the geometric sum of the dyad lengths $O(a)$. For $h<1$, a slide interval contains at most one integer, each atom is included on slide measure at most $h$, and the drift gives $O(ah^2)$. This uses the assumed GRH on the single $q$ in question. All estimates below are uniform for the auxiliary range.

For any ordinary tile $J_i=[X(i-1),X(i+1)]$ not touching $x<X$ or a cutoff endpoint of $R$, use the residue constant $\mathbf m_i=(2X)^{-1}\int_{J_i}\mathbf F(z)dz$. Sum only tiles meeting the support in (4), so they lie in $[0,3a]$. Jensen, bounded tile overlap and (6) give

$$
 \sum_i\int_{J_i}\|\mathbf F(z)-\mathbf m_i\|_2^2dz
 \ll \frac1X\int_{-2X}^{2X}\int_{-2X}^{3a}
                    \|\mathbf F(z+h)-\mathbf F(z)\|_2^2dz\,dh
 \ll a X L^4 .
 \tag{7}
$$

For negative $h$ one translates to an increment of lag $|h|$; the relevant pairs have both endpoints nonnegative in the ordinary tiles, so (6) covers them.

Write $d\nu_{r,I,i}=g_{I,i,t}\,dF_r$. On ordinary tiles, partial integration for the Fourier coefficient $\widehat\nu(\beta)=\int e(\beta x)d\nu(x)$, $e(z)=\exp(2\pi iz)$, permits subtracting $\mathbf m_i$, since $g_{I,i,t}$ vanishes at the tile ends and is absolutely continuous. Its differentiated weight has bulk terms from $\sqrt{x/a}$, $\zeta_i$ and the phase, bounded by $O(\omega_V(1+|\beta|X)/(\sqrt a X))$ since $x\ge X$ and $X\le a/20$. Summing squared integrated bulk terms over $I,i$ costs at most

$$
 \ll \frac{(1+|\beta|X)^2}{aX}
           \sum_i\int_{J_i}\|\mathbf F-\mathbf m_i\|_2^2 ,
$$

using Cauchy over the length $2X$ and $\sum_I\omega_V^2=O(1)$. The terminal derivative from (2) is the cutoff density on $QI$, and its squared integrated terms cost at most

$$
 \ll \frac{\omega_V^2}{aQD}
           \sum_i\int_{J_i}\|\mathbf F-\mathbf m_i\|_2^2 .
$$

Here Cauchy in the measure uses (3) and the $QI$ for one dyad are disjoint. This is $\ll (X/a)L^4$ by (7), not a cost proportional to the number of tiles or windows. There are $O(1)$ exceptional tile indices at $x<X$ and at the endpoints of $R$. For each use partial summation with the pointwise bound for $\mathbf F$, and $\|g_{I,i,t}\|_\infty+\mathrm{TV}(g_{I,i,t})\ll\omega_V/\sqrt a$, including any endpoint atoms selected in $R$. The resulting vector bound per $I$ is $O(\omega_V(1+|\beta|X)L^2)$; summing the squares as above is sufficient. We obtain

$$
          \sum_{I,i,r}|\widehat\nu_{r,I,i}(\beta)|^2
                 \ll_\Gamma (1+|\beta|X)^2 L^4 .
 \tag{8}
$$

For the weighted short-increment analogue, take $2\le\ell\le X$, and discard temporarily the sliding starts $s<\ell$ or whose interval crosses an endpoint of $R$. The nonempty starts among these have total measure $O(\ell)$, and only $O(1)$ tile indices are involved for each such start. Partial summation with the same sup and variation bounds proves an $O(\ell L^4)$ contribution to the integrated squared norm. Otherwise, use Abel in the form

$$
 \int_{(s,s+\ell]}g(x)dF_r(x)
 =g(s+\ell)[F_r(s+\ell)-F_r(s)]
       -\int_s^{s+\ell}g'(x)[F_r(x)-F_r(s)]dx .
 \tag{9}
$$

The first term costs $O(\ell L^4)$ by (6) and $\sum_{I,i}|g_{I,i,t}(x)|^2\ll a^{-1}$. In the bulk derivative terms now $x\ge\ell$, so the sum of pointwise squares of those derivatives is $O((a\ell^2)^{-1})$. Minkowski in $x=s+u$ and (6) show their squared norm is $O(\ell L^4)$, since $\int_0^\ell \sqrt u\,du/\ell=O(\sqrt\ell)$. For the terminal term, at each $s$ use (3), cutoff disjointness in $I$, and tent overlap in $i$, giving the squared bound

$$
             O\left(\frac{\omega_V^2}{aQD}
                   \int_s^{s+\ell}\|\mathbf F(x)-\mathbf F(s)\|_2^2dx\right).
$$

After integration in $s$, (6) bounds this by $O((\ell^2/a)L^4)$, which suffices. Thus the full integrated slide estimate is

$$
 \int_{\mathbb R}\sum_{I,i,r}|\nu_{r,I,i}((s,s+\ell])|^2ds
                                      \ll_\Gamma \ell L^4 .
 \tag{10}
$$

The exact endpoint convention in a hard raw restriction is harmless here: in the exceptional partial summation estimate one may bound the $O(1)$ separate endpoint atoms as well. Equations (8) and (10) also hold with $Q\partial_t g$, by (3). By convolution and Plancherel, (10) gives the integrated squared Fourier norm, over $|\beta|\le 1/(4\ell)$ and summed over indices, of $O(L^4/\ell)$.

## 3. Circle estimates for the tile relation

Write $A_{i,V}(\alpha)$ for the vector of $\sum_n\Lambda(n)g_{I,i,t}(n)e(n\alpha)$ in $I$, and $B_{i,V}(\beta)$ for the vector of continuous Fourier integrals. A grand norm on a leg sums the squared norms over $i$. On each leg,

$$
 \|A_V\|_{L^2(\mathbb T;{\rm grand})}\ll L,\qquad
 \|B_V(\beta)\|_{\rm grand}\ll
               X^{-1/2}\min(X,|\beta|^{-1}).
 \tag{11}
$$

The first follows by Parseval and overlap. The second uses the per-tile sup and variation bounds, $O(a/X)$ tile indices and $\sum_I\omega_V^2=O(1)$. Both include $Q\partial_t$ on that profile.

Use $P=\lfloor\sqrt X/10\rfloor$, disjoint major arcs at $a'/q$ of radii $\delta_q=2P/(qX)$. Off these arcs Dirichlet approximation gives $P<q\le\lceil20\sqrt X\rceil$, $|\beta|X\le1$. Decompose the grand vectors at $a'/q+\beta$ as $A_V=M_V+E_V+Z_V$, with $M_V=\mu(q)B_V(\beta)/\phi(q)$, $E_V$ the additive transform of the residue errors, and $Z_V$ the $q$-nonunit atoms. Equation (8) yields

$$
 \|E_V(a'/q+\beta)\|_{\rm grand}
               \ll \sqrt q(1+|\beta|X)L^2 .
 \tag{12}
$$

For $Z_V$, the total nonunit marks are $O(L^2)$ and the grand norm at one raw point is $O(a^{-1/2})$, so its norm is $O(L^2/\sqrt a)$. It follows from (11), (12) that the minor arc grand supremum of $A_V$ is $\ll_\epsilon Q^\epsilon X^{1/4}$. Apply (5) and the other leg's $L^2$ norm.

On the majors (10) with $\ell=qX/(8P)$ and finite additive Parseval show that the integrated grand square of $E_V$ over the reduced $q$-arcs is $O(L^4P/X)$. Combine (5), (12), and $\sum_{q\le P}q(1+P/q)^2\ll P^2\log(2P)$. The $L^2({\rm HS})$ norm of the double error is $\ll_\epsilon Q^\epsilon X^{1/4}$. For a single error $E_V,M_U$, apply (5) and finite additive Parseval, then (8) with $(1+|\beta|X)\|B_U(\beta)\|_{\rm grand}\ll\sqrt X$ from (11). Its squared norm is bounded by

$$
             \ll L^4 X\sum_{q\le P} q\,\phi(q)^{-2}\delta_q
             \ll L^4P.
 \tag{13}
$$

The same argument applies in the reverse order and to both sign choices of each Fourier argument, since balanced arcs are reflection symmetric. Thus both the minor tensor and each major single or double error have $L^2({\rm HS})$ norm $\ll_\epsilon Q^\epsilon X^{1/4}$, uniformly in $t$. These bounds include the normalized $t$-derivative of the product by applying the one-leg differentiation bounds.

## 4. Sampling, signs and exact benchmark

For the fixed band there are $O(W)$ possible $s=kN$ per modulus, and we keep only the physically possible range $s\le4QM$ before extending the Fourier terms. Cauchy in the selected aliases entry by entry and the divisor bound on the number of representations $s=kN$ give the unnormalised square sampling bound

$$
  \sum_{N\in\mathcal A}
        \left\|\sum_{\text{selected }k}c_{kN}(t)\right\|_{\rm HS}^2
       \ll_\epsilon W Q^\epsilon\sum_s\|c_s(t)\|_{\rm HS}^2
 \tag{14}
$$

for any fixed coefficient tensor. Even with entry masks one first applies entrywise Cauchy and then discards the masks in the square sum. Because the tensor and band are fixed at each $t$, replace $t$ by the live $N$ using the fundamental theorem of calculus and Minkowski as in R64–R66. Explicitly $c_s(N)=c_s(Q)+\int_Q^{2Q}\mathbf1_{t\le N}\partial_t c_s(t)dt$, and (14) applies on each smaller selected set. Parseval and §3 yield the first term in (1).

The $q$-nonunit products are handled pointwise by (5), the grand sup bound on $Z$, and (11), giving $O(L^{O(1)}W/\sqrt{Q\min(V,U)})$ after summing the $O(W)$ possible lines. This is $\ll L^{O(1)}\sqrt{W/Q}$. Indeed the products involving $Z$ are $Z_V,A_U$, $A_V,Z_U$, and minus $Z_V,Z_U$; use Fourier coefficient $L^1$ bounds, and restricting entries cannot increase the HS norm for a fixed $s$. For the original $N$-nonunits at a fixed $s$, each nonunit prime-power atom on one leg has at most one candidate partner on the line. The actual profiles have pointwise window norm $O((QV)^{-1/2})$ or $O((QU)^{-1/2})$. Removing these atoms with the exact original unit rule costs $O(L^{O(1)}W/(Q\sqrt{VU}))$ and removes no admissible proper powers.

Finally (5) and the two decays (11) give HS norm $O(1)$ for the full continuous tensor Fourier coefficient on a line, and $O(1/(X\delta_q))=O(q/P)$ for the tail of its $\beta$ integral on the $q$-arcs. The two absolute Ramanujan estimates of R66 (14) extend the series and integrals at pointwise cost $O_\epsilon(Q^\epsilon W/P)$ after summing the selected aliases, also within the second term of (1). The full Fourier integral for each tile pair is exactly its continuum sum or difference integral; Fourier inversion applies since the products are integrable and the convolution is continuous. For $s$ in the band, the tile relation and partition unity restore the original raw profiles with their exact interval cuts. The sum of rational centers is $c_q(s)$ for each orientation, so the full series is $\mathfrak S(s)$. Put back the three original signs and sum over the logarithmically many dyad pairs. This proves (1) and the exceptions by Chebyshev, since at $W=Q^{8/25}$ the unnormalized primary square is $O_\epsilon(Q^{49/50+\epsilon})$, and the pointwise term is smaller than the target threshold.

The proof uses bounded degree of the tile relation for a **common raw band**. An arbitrary collection of bands whose centers span the bulk can have degree of order the number of bands. There can be $O(M/W)$ disjoint bands. At the displayed parameters, the triangle bound across these bands has primary power $3/5-8/25-1/200=11/40>0$. The estimate for each band does not control covariance across bands and gives no full surviving mean–mean second moment.
