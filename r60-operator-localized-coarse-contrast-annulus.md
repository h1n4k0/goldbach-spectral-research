# Localized true coarse contrasts beyond the cube-root prefix

**Scope.** This estimates an actual doubly exterior subspace of the original Hardy operator, well above the previous complete prefix. On growing mesowindows it retains every spatial direction with zero true weighted mean. In particular, it controls contrasts between many of the actual exterior coarse cells, simultaneously and including interactions between distinct mesowindows. It does not estimate their window means, their mixed blocks, the whole annulus, a prescribed modulus, or weak S.

## Statement

Write $L=\log Q$ and let $\mathcal A\subset[Q,2Q]$ be any set of $J\ge1$ distinct even integers. Fix a polynomial bound $1\le D\le H<M\le Q^\Gamma$. Partition the reference annulus $[H,M]$ into dyadic pieces beginning at $V=2^jH$, then split each piece into intervals of length $D$ and at most one shorter last interval. For $N\in\mathcal A$, transport a reference interval $I$ to $I_N=(Q/N)I$ in the true physical coordinate. Let $R_N$ be the orthogonal projection onto

$$
 \bigoplus_{I}\{f\in L^2(I_N):\ \int_{I_N}r_N(u)f(u)\,du=0\},
 \qquad r_N(u)=u^{-3/2}\big((Nu)^{-2/\log N}+(Nu)^{-1/4}\big)^{1/2}.
 \tag{1}
$$

Assume original local Dirichlet $\mathrm{GRH}(N)$ at each selected $N$ and auxiliary Dirichlet GRH for every integer modulus $q\le\lceil20\sqrt{QD}\rceil$, including $q=1$. Then, for every $\epsilon>0$,

$$
 \left(\operatorname{Avg}_{N\in\mathcal A}\|R_NT_NR_N\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\epsilon} Q^\epsilon
       \left(\frac{Q^{1/4}D^{3/4}}{\sqrt J}+\sqrt{D/Q}\right).
 \tag{2}
$$

Notably the leading term depends on the window size $D$, not the outer scale $M$. No consecutive-modulus condition is imposed. For

$$
 H=Q^{2/5},\quad M=Q^{3/5},\quad D=Q^{8/25},\quad J\gg Q^{99/100},
 \tag{3}
$$

the RMS bound is $O_\epsilon(Q^{-1/200+\epsilon})$; without a lower bound on $J$, there are $O_\epsilon(Q^{197/200+\epsilon})$ exceptions above $Q^{-1/400}$ among the selected moduli. Global Dirichlet GRH suffices for both hypotheses but is not proved. The physical annulus itself drifts by the explicit bounded dilation $Q/N$; in (3) it lies completely beyond the $Q^{8/25}$ complete-prefix radius for all sufficiently large $Q$.

## 1. True support localization and dimension-free norms

Use the [R49](r49-operator-full-prefix-variance.md) and [R59](r59-operator-balanced-arcs-cuberoot-prefix.md) exact pullback $f(u)\mapsto a^{-2}r_N(z/a)f(z/a)/r_Q(z)$, with $a=N/Q,\ z=au$. Here $r_Q$ is the same explicit Hardy weight with parameter $Q$, not an arithmetic character at the anchor. On $I_N$ the map has uniformly bounded norm, since the raw argument $Qz=Nu$ is unchanged and $u,z\asymp V$ in the reference $V$-dyad. It maps (1) into the fixed test space $\mathcal H_I=\{g\in L^2(I):\int_I r_Qg=0\}$, since the weighted integrals differ by $a^{-1}$. It preserves the raw Volterra weights exactly by $a^2/(Na)=1/Q$. The assembled true compression is a two-sided bounded pullback of the fixed raw tensor matrix, so the HS ideal property transfers the bound with no dimension loss.

For an orthonormal real basis $(f_i)$ of $\mathcal H_I$, the vector of raw weights is $h_I(x)=(\rho_i(x))_i$, with

$$
 \rho_i(x)=\frac{\sqrt{2\pi x}}Q\int_{z\in I,\ z\ge x/Q}r_Q(z)f_i(z)\,dz
 \quad (x>0).
 \tag{4}
$$

Its support is contained in the actual raw interval $QI$, of length at most $QD$: below it the entire integral is zero by the true mean condition, and above it the integral is empty. At each endpoint the scalar weight vanishes. Since $x\asymp QV$ on $QI$ and $r_Q(z)\ll V^{-3/2}$, Bessel gives
$\|h_I(x)\|\ll b_V=\sqrt D/(\sqrt Q V)$.
For a unit linear combination of basis elements, the weight has variation $O(b_V)$: the square-root derivative costs $O(b_V D/V)$, while the derivative of the integral at $z=x/Q$ has $L^1$ norm $O(b_V)$ by Cauchy over $I$. This gives the vector transform estimates

$$
 B_I(\beta)=\int h_I(x)e(x\beta)\,dx,\qquad
 \|B_I(\beta)\|\ll b_V\min(QD,|\beta|^{-1}),\qquad
 \|B_I\|_{L^2(\mathbb R)}\ll D/V .
 \tag{5}
$$

The first Fourier bound follows by duality and integration by parts, the second by vector Plancherel. Define $A_I(\alpha)=\sum_m\Lambda(m)h_I(m)e(m\alpha)$, $e(t)=e^{2\pi it}$. By Parseval and the trivial $O(QD)$ number of integers on $QI$,

$$
 \|A_I\|_{L^2(\mathbb R/\mathbb Z)}\ll L\,D/V.
 \tag{6}
$$

These remain uniform for short last windows; one may work first with finite basis truncations throughout.

## 2. Short-interval and pointwise errors on a genuine localized test

For a denominator $q$ in the stated auxiliary range, let $F_r(t)=\psi(t;q,r)-t/\phi(q)$ on units and zero on nonunits. Use the local-GRH estimates established in [R59](r59-operator-balanced-arcs-cuberoot-prefix.md), including the finite-height Selberg–Prachar proof there:

$$
 \sum_r|F_r(t)|^2\ll tL^4,\qquad
 \int_{x_0}^{2x_0}\sum_r|F_r(t+h)-F_r(t)|^2dt
 \ll x_0hL^4\quad (x_0\ge2,\ 1\le h\le x_0)
 \tag{7}
$$

in the polynomial ranges. Their GRH scope is only the characters of the given $q$. Put $\nu_{r,i}=\rho_i\,dF_r$ supported in $QI$. The localized, dimension-free counterpart of [R59](r59-operator-balanced-arcs-cuberoot-prefix.md)'s weighted Selberg bound is

$$
 \int_{\mathbb R}\sum_{r,i}|\nu_{r,i}((t,t+h])|^2\,dt
 \ll \frac{D}{V}hL^4\qquad(h\ge2).
 \tag{8}
$$

To prove it, write $I=[c,b]$ up to endpoints. Use (4) after restricting the integration variable $x$ to $QI$, and apply Bessel in $z$ to the pairing of $f_i(z)$ with

$$
 \frac{\sqrt{2\pi}}Q\,r_Q(z)
       \int_{(t,t+h]\cap[Qc,Qz]}\sqrt x\,dF_r(x).
$$

Uniformly in $z\in I$, the squared sum in $r$ of the latter *inner integral*, integrated in $t$, is $O((QV)^2 h L^4)$. For the proof, any such interval endpoints $\ell\le b'$ in $QI$ have weighted residue-vector norm $O(QV L^2)$ by Abel and the first bound of (7). If $h>QD$, the range of $t$ has length $O(h)$, which suffices. Otherwise the $t$-intervals crossing either cutoff $Qc,Qz$ occupy $O(h)$ measure and have the same cost. On the interior windows, use Abel in the form

$$
 \sqrt{t+h}\,[F_r(t+h)-F_r(t)]
    -\int_t^{t+h}\frac{F_r(x)-F_r(t)}{2\sqrt{x}}\,dx .
$$

The first part gives $O((QV)^2 h L^4)$ by (7) over at most a bounded number of dyads at scale $QV$ (here $h\le QD\le QV$). The second has pointwise residue-vector norm $O(hL^2)$ and $t$-range $O(QV)$, so its squared integral $O(QVh^2 L^4)$ is admissible. This proves the claimed inner bound. Multiply by $Q^{-2}\int_I r_Q(z)^2 dz\ll Q^{-2}D V^{-3}$ to get (8). The full zero weighted moment in each window is used in the raw support restriction; there is no approximation by a localized proxy. By convolution with the length-$h$ indicator and Plancherel, (8) gives

$$
 \sum_{r,i}\int_{-\delta}^{\delta}|\widehat\nu_{r,i}(\beta)|^2d\beta
 \ll (D/V)L^4/h \quad(\delta h\le 1/4).
 \tag{9}
$$

For the principal-density and unit-error decomposition on a rational center $a/q$, write

$$
 A_I(a/q+\beta)=M_I+E_I+Z_I,\qquad
 M_I=\frac{\mu(q)}{\phi(q)} B_I(\beta),\quad
 (E_I)_i=\sum_{r\bmod q} e(ar/q)\widehat\nu_{r,i}(\beta).
 \tag{10}
$$

Here $Z_I$ is supported on the prime powers of primes dividing $q$, in the underlying raw sum, and $\|Z_I\|\ll L^2 b_V$ since their total $\Lambda$-weight in the polynomial range is $O(L^2)$. Abel gives $\widehat\nu_{r,i}=-\widehat f_{r,i}-2\pi i\beta\widehat g_{r,i}$, $f_{r,i}=\rho_i'F_r,\ g_{r,i}=\rho_iF_r$. The localized vector bounds are

$$
 \sup_\beta\sum_{r,i}|\widehat f_{r,i}|^2\ll (D/V)L^4,
 \qquad
 \sup_\beta\sum_{r,i}|\widehat g_{r,i}|^2\ll (D/V)(QD)^2L^4,
 \qquad
 \sum_{r,i}\int_{\mathbb R}|\widehat g_{r,i}|^2\ll (D/V)(QD)L^4 .
 \tag{11}
$$

For the first, differentiating (4) splits the square-root term (bounded in vector norm after integration by $L^2\sqrt{D/V}(D/V)$) from the terminal derivative at $z=x/Q$. After substituting $x=Qz$, the terminal term pairs $f_i(z)$ with $-\sqrt{2\pi Qz}\,r_Q(z)F_r(Qz)e(Qz\beta)/Q$; Bessel in $i$ and (7) give $O((D/V)L^4)$ for its squared sum. The second follows by Minkowski from $\|h_I(x)\|\|(F_r(x))_r\|\ll b_V\sqrt{QV}L^2$ over length $QD$. The third is Plancherel and the squared pointwise bounds integrated over that length. In particular, Cauchy in $r$ gives

$$
 \|E_I(a,\beta)\|\ll \sqrt{D/V}\sqrt q\,(1+|\beta|QD)L^2 .
 \tag{12}
$$

## 3. Balanced arcs, exact aliases, and HS aggregation

For any fixed pair of reference windows $I,J'$, lying in dyads of first scales $V,U$, put $X=QD,\ P=\lfloor\sqrt X/10\rfloor$. The disjoint major arcs around reduced $a/q,\ q\le P$, have radius $\delta_q=2P/(qX)$. On the minor set Dirichlet approximation gives $P<q\le20\sqrt X$ and $|\beta|\le2P/(qX)$, hence $|\beta|QD\le2$. Equations (5), (10), (12) and $q\asymp\sqrt X$ imply

$$
 \sup_{\rm minor}\|A_I\|\ll_\epsilon Q^\epsilon X^{1/4}\sqrt{D/V}.
 \tag{13}
$$

For example its principal-density bound there is $O_\epsilon(Q^\epsilon D/V)$, and $D/V\le1$. The other leg can use (6). These arguments need auxiliary GRH up to the displayed $20\sqrt{QD}$, not up to the raw center $QV$.

With $h=qX/(8P)\ge2$ for large $Q$, (9) and additive Parseval in $a$ give $\int_{\text{reduced }q\text{-arcs}}\|E_I\|^2\ll (D/V)L^4P/X$. Using (12) on the other leg and $\sum_{q\le P}q(1+P/q)^2\ll P^2\log(2P)$, the double-error product satisfies

$$
 \|E_I\otimes E_{J'}\|_{L^2({\rm majors};\rm HS)}
 \ll L^{9/2}\frac{D}{\sqrt{VU}}\,\frac{P^{3/2}}{\sqrt X}
 \ll L^{9/2}X^{1/4}\frac{D}{\sqrt{VU}} .
 \tag{14}
$$

The two single-error products have norms $O_\epsilon(Q^\epsilon D^{3/2}/(V\sqrt U))$ and $O_\epsilon(Q^\epsilon D^{3/2}/(U\sqrt V))$, respectively: apply Parseval over $a$ with $q/\phi(q)^2$ mass, the first of (11) with the other leg's $\|B\|_2$, and the last of (11) with $\sup|\beta|\|B\|\ll b_V$ or $b_U$ from (5). The sum over denominators is $Q^\epsilon$. By (6) and (13) the minor tensor $L^2$ norm is bounded by the right side of (14) up to $Q^\epsilon$, because $\sqrt{D/V}(D/U)\le D/\sqrt{VU}$. All estimates hold with either Fourier argument reversed by the arc symmetry.

The genuine fixed raw tensor for $N=2n$ uses three alias equations $m=x+kN,\ m=x-kN,\ m=kN-x$, signs $+,+,-$, and $k\ge1$. For a fixed orientation $(\varepsilon_1,\varepsilon_2)=(-,+),(+,-),(+,+)$, restrict the $k$-sum to $s=kN$ in the interval $\varepsilon_1 QI+\varepsilon_2 QJ'$, which has length at most $2QD$. Both the exact prime-power term and the model vanish outside that interval, because the raw weights actually have these supports. This is true even though the separate Fourier major or minor terms need not vanish there. For each $N$ there are $O(D)$ retained positive $k$, using $N\ge Q,D\ge1$. All have $s\ll QM$, so $\tau(s)\ll_{\Gamma,\epsilon}Q^\epsilon$. Therefore for the Fourier coefficients $c_s$ of each fixed tensor product, Cauchy in the restricted $k$-set and then divisor multiplicity give

$$
 \sum_{2n\in\mathcal A}
   \left\|\sum_{k:\,2kn\in\varepsilon_1 QI+\varepsilon_2QJ',\ k\ge1}
          c_{2kn}\right\|_{\rm HS}^2
 \ll_{\Gamma,\epsilon} D Q^\epsilon\sum_s\|c_s\|_{\rm HS}^2 .
 \tag{15}
$$

Thus (13)–(14) after sampling have RMS at most $Q^\epsilon \sqrt{D/J}X^{1/4}D/\sqrt{VU}$ per window pair. For the single errors use the just-stated two norms and the same factor $\sqrt{D/J}$.

The exact model weights on a line are still $\mathfrak S(kN)\int h_I(x)\otimes h_{J'}(m(x,N))dx$. Indeed the full $\beta$-integral of the product in (10) restores the corresponding linear relation and the Ramanujan series restores the singular series, as in [R59](r59-operator-balanced-arcs-cuberoot-prefix.md). More precisely the $\beta$-tail per $q$ is $O(b_Vb_U/\delta_q)=O(qD^2/(P VU))$ by (5); the full integral is $O(D^2/(VU))$ by support lengths and sup weights. Apply [R59](r59-operator-balanced-arcs-cuberoot-prefix.md)'s elementary sums $\sum_{q\le P}q|c_q(s)|/\phi(q)^2\ll_\epsilon Q^\epsilon$, $\sum_{q>P}\mu^2(q)|c_q(s)|/\phi(q)^2\ll_\epsilon Q^\epsilon/P$, valid uniformly for $s\ll QM$. There are $O(D)$ aliases per orientation, so the model error per pair is $O_\epsilon(Q^\epsilon D^3/(P VU))$ pointwise. This retains every sign, the proper powers, and the removal of the equality line.

On the arithmetic side, dropping the original unit holes costs at most $O(L^{O(1)}D^2/(QVU))$ per pair: each nonunit prime power has $O(D)$ partners, its side has total $\Lambda$-mass $O(L^2)$, and the raw tensor weight is $O(b_Vb_U)$. On the major arcs the $Z_I,Z_{J'}$ nonunit terms from (10) can likewise be dropped in the products at cost $O(L^{O(1)}D^{5/2}/(\sqrt Q\,VU))$ per pair after counting aliases, by $L^2$ Cauchy with (6). The full arithmetic has no other deletions.

There are $O(V/D)$ windows in dyad $V$ and $O(U/D)$ in dyad $U$, since $D\le H$. Their fixed Hilbert test spaces are orthogonal direct sums. Consequently, pass from a uniform per-window-pair HS or RMS bound to the whole dyad pair by multiplying by $O(\sqrt{VU}/D)$, not by the product of the counts; this is the sum-of-squares identity for HS blocks followed by the modulus mean. The leading terms become $O_\epsilon(Q^\epsilon Q^{1/4}D^{3/4}/\sqrt J)$ because the factor $D/\sqrt{VU}$ exactly cancels. The single errors become $O_\epsilon(Q^\epsilon D/\sqrt{J\min(V,U)})$, which is smaller since $V,U\ge D$. The pointwise model and unit errors after the same multiplication are at most $Q^\epsilon(D/P+\sqrt{D/Q}+1/Q)$, using $\sqrt{VU}\ge D$; $D/P\ll\sqrt{D/Q}$. Summing the $O(L^2)$ dyad pairs and three signs and applying the true pullback proves (2).

## 4. Actual coarse directions and exceptions

For (3) the first power in (2) is $1/4+3(8/25)/4-(99/100)/2=-1/200$, and the pointwise term is smaller. By (15) without dividing by $J$, the squared HS sum of the sampled components is $O_\epsilon(Q^\epsilon Q^{1/2}D^{3/2})$. The other errors are pointwise $o(Q^{-1/400})$, so Chebyshev gives the stated $O_\epsilon(Q^{197/200+\epsilon})$ exception count. It need not be informative on a prescribed thin selection.

To explicitly connect to the actual [R51](r51-operator-full-leg-fine-bridge.md) coarse cells, start its grid at $Q^{8/25}$ and take the normalized mean lines of cells wholly in the physical annulus $[(Q/N)H,(Q/N)M]$. In each transported mesowindow, the span of coarse cells wholly contained there has a genuine codimension-one hyperplane (if nonempty) in (1), obtained by the single constraint $\int r_N f=0$. In (3), each full mesowindow contains $\gg Q^{1/50}$ complete [R51](r51-operator-full-leg-fine-bridge.md) coarse cells for all large $Q$, since their lengths on the annulus are $O(Q^{3/10})$ with fixed [R51](r51-operator-full-leg-fine-bridge.md) parameters. Thus (2) genuinely acts on contrasts of many retained coarse cells, not just the already discarded fine directions. The orthogonal complement inside the original coarse annulus has dimension $O(M/D)$: at most one weighted-mean direction per mesowindow and at most one unassigned coarse cell per internal mesowindow boundary, plus endpoints. No estimate of the matrix terms having a leg in this complement is inferred. More generally for any fixed outer exponent $\Gamma<2/3$, one can take $D=Q^\eta$ with $\Gamma/2<\eta<1/3$, an inner power radius $H\ge D$, and $J\gg Q^d$ with $d>1/2+3\eta/2$, so the same contrast theorem applies. The full true coarse tail and its crossing to the prefix remain open.
