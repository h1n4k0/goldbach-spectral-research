# Balanced raw arcs and a genuine prefix approaching the cube-root scale

**Scope.** This bounds the full original physical prefix, including spatial coarse–coarse and prefix–coarse directions beyond the previous $Q^{6/25}$ cutoff. It is a conditional Hilbert–Schmidt mean square over selected even moduli, not a bound at an assigned modulus or on the full Hardy operator. It uses the original local Dirichlet GRH to identify the operator and a broader, explicitly bounded auxiliary Dirichlet GRH range for the arithmetic.

## Statement

Let $\mathcal A$ be any set of $J\ge1$ distinct even integers in $[Q,2Q]$. Fix $0<\gamma<1/3$, take $1\le M\le Q^\gamma$, and put $Y=Q^{-\sigma}$ with $0<\sigma<1$. Assume the original local $\mathrm{GRH}(N)$ at each $N\in\mathcal A$, and GRH for all Dirichlet characters of integer moduli $q\le\lceil20\sqrt{QM}\rceil$, including $q=1$. Global Dirichlet GRH suffices. In the true unitary physical realization write $P_M=\mathbf1_{(0,M]}$. For every $\epsilon>0$,

$$
 \left(\operatorname{Avg}_{N\in\mathcal A}
       \|P_MT_NP_M\|_{\rm HS}^2\right)^{1/2}
 \ll_\epsilon Q^\epsilon\left[
        \frac{Q^{1/4}M^{3/4}}{\sqrt J}
       +\frac{M}{\sqrt{JY}}+\frac{M}{\sqrt{QY}}+\sqrt{YM}
 \right].
 \tag{1}
$$

The fixed exponents may enter the constant. For each fixed $\gamma<1/3$, choose $\gamma<\sigma<1-2\gamma$ and $d\le1$ with
$d>\max\{1/2+3\gamma/2,\ 2\gamma+\sigma\}$.
Then $J\gg Q^d$ gives a power saving in (1). For example

$$
 (\gamma,\sigma,d)=(3/10,8/25,24/25)
 \quad\hbox{or}\quad
 (8/25,33/100,99/100)
 \tag{2}
$$

both give $O_\epsilon(Q^{-1/200+\epsilon})$, controlling the full prefix through $Q^{3/10}$ or $Q^{8/25}$, respectively. Without requiring the lower bound on $J$, the number of selected $N$ whose compression has HS norm exceeding $Q^{-1/400}$ is $O_\epsilon(Q^{191/200+\epsilon})$ or $O_\epsilon(Q^{197/200+\epsilon})$ in these two cases. No interval hypothesis within the shell is needed. These exponents do not establish success on every modulus or on a prescribed thin set.

## 1. Exact raw transference and a local short-interval input

Apply the fixed raw dyad construction of [R49](r49-operator-full-prefix-variance.md) and [R56](r56-operator-adaptive-arc-full-prefix.md) on $[Y,M]$: for the actual dyad starting at $V=2^jY$, use the external space $\mathcal H_V=L^2([V,4V])$, the common anchor $Q$, and $a=N/Q$. The map $f(u)\mapsto a^{-2}r_N(z/a)f(z/a)/r_Q(z)$ with $z=au$ and support restricted to the dilated physical dyad has uniformly bounded operator norm and preserves the raw Volterra weight exactly by $a^2/(Na)=1/Q$. This uses $r_t(u)=u^{-3/2}((tu)^{-2/\log t}+(tu)^{-1/4})^{1/2}$ and $QY\ge1$. The fixed matrix bounds therefore imply the actual compression bounds by the HS ideal property, with no rank loss. In a real orthonormal test basis write $h_V(x)=(\rho_i(x))_i$, $Z=QV$, and, in scaled coordinates $v\in[1,4]$,

$$
 \rho_i(x)=\frac{\sqrt{2\pi x}}{Z}
       \int_1^4 {\bf1}_{x\le Zv}R(v)\phi_i(v)\,dv ,
 \qquad R(v)=V^{3/2}r_Q(Vv)\ll1 ,
 \tag{3}
$$

where the $\phi_i$ are the scaled orthonormal basis. Extend the weights by zero off $[0,4Z]$. Then $\|h_V(x)\|\ll\sqrt x/Z$. In contrast to [R56](r56-operator-adaptive-arc-full-prefix.md)'s optional prime-only intermediary, keep **all** von Mangoldt weights, and set

$$
 A_V(\alpha)=\sum_{m\ge1}\Lambda(m)h_V(m)e(m\alpha),\qquad
 B_V(\beta)=\int h_V(x)e(x\beta)\,dx,\qquad e(t)=e^{2\pi it}.
$$

Parseval and Chebyshev give $\|A_V\|_{L^2(\mathbb R/\mathbb Z)}\ll(\log Q)^{1/2}$; the [R49](r49-operator-full-prefix-variance.md) Volterra bounds give $\|B_V\|_2\ll1$ and $\|B_V(\beta)\|\ll\sqrt Z\min(1,(Z|\beta|)^{-1})$.

Here is the requisite localized short-interval comparison. For $q$ in the auxiliary range let $F_r(t)=\psi(t;q,r)-t/\phi(q)$ on unit residues, zero otherwise, and extend by zero for $t\le0$. The standard GRH character prime number theorem plus finite character Parseval gives $\sum_r|F_r(t)|^2\ll t L^4$ throughout the raw range, $L=\log Q$; for $0<t<2$ it follows directly. For $x_0\ge2,\ 1\le h\le x_0$, the short-interval estimate in the needed polynomial ranges is

$$
 \int_{x_0}^{2x_0}\sum_r|F_r(t+h)-F_r(t)|^2\,dt
 \ll x_0 h L^4 .
 \tag{4}
$$

This is the Selberg–Prachar upper bound (compare Goldston–Yıldırım, *Primes in Short Segments of Arithmetic Progressions*, (1.4)); here is a local-GRH justification sufficient for the claimed auxiliary range. Use the classical truncated explicit formula at the same height $x_0$ for $t$ and $t+h$, both in $[x_0,3x_0]$ ([Koukoulopoulos, The Distribution of Prime Numbers, Theorem 11.3](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=125)). Its centered increment is the negative of the nontrivial zero sum over $|\Im\rho|\le x_0$ of $((t+h)^\rho-t^\rho)/\rho$, with pointwise error $O(L^2)$ in the polynomial ranges: the $-1$ in each numerator cancels, and the separate errors are $O(t\log^2(2qt)/x_0)$. The theorem applies to all characters modulo $q$, since the missing Euler terms are also $O(L^2)$. This pointwise remainder contributes $\ll x_0hL^4$ in squared integral.

For the nontrivial zeros, $\rho=1/2+i\eta$. On a fixed-length real log interval $I$ the elementary estimate

$$
 \int_I\left|\sum_\eta b_\eta e^{i\eta u}\right|^2 du
 \ll \sum_{j\in\mathbb Z}\left(\sum_{j\le\eta<j+1}|b_\eta|\right)^2
 \tag{5}
$$

holds for finite sums with multiplicities, uniformly under translations of $I$. Multiply by a smooth bump dominating its indicator, use Fourier decay $O((1+|\eta-\eta'|)^{-2})$, and sum unit bins by Schur. Split the finite zero sum at $T=x_0/h\ge1$. Low zeros are integrals $\int_0^h(t+v)^{-1/2+i\eta}dv$; by Minkowski, $dt/(t+v)=d\log(t+v)$, (5), and the usual unit-bin zero count $O(\log(2q(|j|+2)))$, their squared norm is $O(h^2(T+1)\log^2(2q(T+2)))$. For high zeros use the separate endpoint functions $t^{1/2}\sum_{|\eta|>T}t^{i\eta}/\rho$ and the same at $t+h$. The squared norm is $O(x_0^2\log^2(2q(T+2))/T)$ by (5) and the convergent sum of squared high-bin masses. The bound is uniform for the finite high group ending at $x_0$; enlarging the squared-bin majorant to infinity does not require any infinite explicit-formula limit. Both estimates are $O(x_0hL^2)$ in the polynomial ranges. Finite character Parseval proves (4) without any other conductors. The usual unit-bin zero count follows from the Riemann–von Mangoldt formula, for example [Koukoulopoulos, Exercise 11.6(b)](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=128) for primitive nonprincipal characters and the ordinary zeta formula for the principal inducing character. No zero-pair-correlation hypothesis enters (4).

## 2. Dimension-free short-interval-to-arc transfer

Let $\nu_{r,i}(dx)=\rho_i(x)\,dF_r(x)$, a finite signed measure supported on $[0,4Z]$. For $h\ge2$ in the polynomial ranges in use,

$$
 \int_{\mathbb R}\sum_{r,i}|\nu_{r,i}((t,t+h])|^2\,dt\ll h L^4.
 \tag{6}
$$

Indeed by (3) and Bessel in $v$, it suffices, uniformly for $w=Zv\in[Z,4Z]$, to bound
$\int_{\mathbb R}\sum_r|\int_{(t,t+h]\cap(0,w]}\sqrt x\,dF_r(x)|^2dt$
by $O(Z^2 h L^4)$. Abel and the pointwise residue-square bound give

$$
 \left(\sum_r\left|\int_{(\ell,b]}\sqrt x\,dF_r(x)\right|^2\right)^{1/2}
 \ll bL^2 \quad(0\le\ell\le b).
$$

If $h>Z$, the integrand is supported in a $t$-range of length $O(h)$ and the last bound with $b\le4Z$ suffices. Otherwise, for $-h\le t<h$ use the bound with $b\le2h$; a square integral $O(h^3L^4)$ is admissible. Windows crossing the cutoff $w$ have $t$-length at most $h$ and cost $O(Z^2hL^4)$ by the same bound. For the remaining nonempty windows, $h\le t,\ t+h\le w$. Write the weighted increment as

$$
 \sqrt{t+h}\,[F_r(t+h)-F_r(t)]
   -\int_t^{t+h}\frac{F_r(x)-F_r(t)}{2\sqrt x}\,dx .
$$

The leading term, squared and integrated in $t$, is $O(Z^2hL^4)$ by (4), covering $t$ by dyads starting at $h$ and using geometric summation. The integral term has residue-vector norm $O(hL^2)$ by the pointwise bound because $t\ge h$; its squared integral is $O(Zh^2L^4)$, also admissible. This proves (6) with the full square-root prefix and the moving cutoff from the true test.

Use positive-sign Fourier transforms. Plancherel for the convolution of $\nu_{r,i}$ with the length-$h$ indicator shows

$$
 \sum_{r,i}\int_{-\delta}^{\delta}|\widehat{\nu}_{r,i}(\beta)|^2\,d\beta
 \ll L^4/h
 \qquad(\delta h\le1/4).
 \tag{7}
$$

The multiplier of the indicator has absolute value $\gg h$ there, and its convolution is, up to reflection/translation, the interval measure from (6). This is the Gallagher argument for these Hilbert-valued measures. The proof applies to finite basis truncations with uniform constants, and then by monotone convergence of squared norms.

## 3. Each dyad pair uses balanced arcs

For $V\le U$ only pairs with $U\ge1/8$ can have an alias. Write $S=\max(1,U)$, $X=QS$, $P=\lfloor\sqrt X/10\rfloor$ for this pair (so $P$ is not constant over the entire matrix). The exact lines are $m=x+kN,\ m=x-kN,\ m=kN-x$ with signs $+,+,-$ and $1\le k\le8S$; no equality line $k=0$ is present. Removing only the original units temporarily costs $O_\epsilon(Q^\epsilon M/\sqrt{QY})$ in HS: the nonunit prime powers on each leg have total $\Lambda$-weight $O(L^2)$, each has $O(S)$ partners of mark $O(L)$, and pointwise tensor weight is $O((Q\sqrt{VU})^{-1})$. This is bounded by the stated looser envelope since $U\ge1/8,\ QY\ge1$. The exact signed continuous model remains $\mathfrak S(kN)\int h_V(x)\otimes h_U(m(x,N))dx$. The origin edge $x<Y,\ y\le M$ costs $O_\epsilon(Q^\epsilon\sqrt{YM})$ by the [R49](r49-operator-full-prefix-variance.md) physical cumulative kernel bound, also for its transpose.

Take disjoint major arcs with reduced $a/q,\ q\le P$, and radius $\delta_q=2P/(qX)$. They are disjoint by rational spacing since $4P^2<X$. On the complement Dirichlet approximation yields $P<q\le\lfloor X/P\rfloor\le20\sqrt X$, $|\beta|\le2P/(qX)$; $X/P$ is within the stated auxiliary cap since $S\le M$. At any such rational displacement decompose

$$
 A_V(a/q+\beta)=\frac{\mu(q)}{\phi(q)}B_V(\beta)
     +E_V(a,\beta)+Z_V^{\rm nu}(a,\beta),\qquad
 (E_V)_i=\sum_{r}e(ar/q)\widehat{\nu}_{r,i}(\beta).
 \tag{8}
$$

Here the nonunit ordinary and higher prime powers $p^j,\ p\mid q$ have total weight $O(L^2)$, so $\|Z_V^{\rm nu}\|\ll L^2/\sqrt{QV}$. These terms on the major arcs are discarded in the tensor products at per-alias cost $O(L^{O(1)}/\sqrt{QY})$ by Cauchy against the other actual factor's $L^2$ norm. This cost is absorbed above.

For completeness the [R49](r49-operator-full-prefix-variance.md) Abel vector decomposition gives, before the additive sum in $r$,
$\widehat{\nu}_{r,i}=-\widehat f_{r,i}-2\pi i\beta\widehat g_{r,i}$
with $f_{r,i}=\rho_i'F_r,\ g_{r,i}=\rho_iF_r$. Its uniform bounds are

$$
 \sup_\beta\sum_{r,i}|\widehat f_{r,i}|^2\ll L^4,\qquad
 \sup_\beta\sum_{r,i}|\widehat g_{r,i}|^2\ll (QV)^2L^4,\qquad
 \sum_{r,i}\int_{\mathbb R}|\widehat g_{r,i}|^2\ll QV L^4 .
 \tag{9}
$$

For the first, the derivative of $\sqrt x$ in (3) is canceled by the $\sqrt x$ in $\|(F_r(x))_r\|$; the moving-endpoint derivative pairs the basis with $R(v)F_r(QVv)$ and is bounded by Bessel. The second follows by Minkowski from $\|h_V(x)\|\|(F_r(x))_r\|\ll xL^2/(QV)$; the third is real-line Plancherel. Consequently the pointwise $\|E_V(a,\beta)\|\ll\sqrt q(1+|\beta|QV)L^2$, and analogously for $U$.

On the minor set $|\beta|QV\le2$, $q\asymp\sqrt X$. The main term in (8) is $O_\epsilon(Q^\epsilon\sqrt X/P)$, and therefore $\sup_{\mathfrak m}\|A_V\|\ll_\epsilon Q^\epsilon X^{1/4}$. This is where auxiliary GRH replaces the earlier $4/5$ Vaughan term; it genuinely uses moduli beyond $P$. The $L^2$ norm of the other factor costs only logs.

For the double major error, at each $q\le P$ choose $h=1/(4\delta_q)=qX/(8P)\ge2$ for sufficiently large $Q$. By (7) and finite additive Parseval summing over all residues $a$, the integrated squared norm of the $U$-error over its reduced $q$-arcs is $O(qL^4/h)=O(L^4P/X)$. The other leg's pointwise norm squared is $O(q(1+P/q)^2L^4)$ by (9), uniformly on these arcs, because $QV\le X$. Thus on the full major set,

$$
 \|E_V\otimes E_U\|_{L^2({\rm majors};\rm HS)}^2
 \ll L^8\frac{P}{X}\sum_{q\le P}q(1+P/q)^2
 \ll L^9 P^3/X.
 \tag{10}
$$

All signed Fourier-argument variants follow by changing $a,\beta$ to $-a,-\beta$. In particular this controls the double error in $L^2$ rather than bounding each Fourier coefficient by a uniform $L^1$ estimate.

For each of the two single-error products, the [R54](r54-operator-asymmetric-crossing.md) weighted Plancherel bound still applies. For $M_V\otimes E_U$, where $M_V=\mu(q)B_V/\phi(q)$ on each arc, apply additive Parseval in $a$. The $f$-part uses $\int\|B_V\|^2\ll1$, and the $g$-part uses $\sup_\beta|\beta|\|B_V(\beta)\|\ll(QV)^{-1/2}$ and the last estimate of (9) on the other leg. The integrated squared norm is bounded by $L^4(1+U/V)\sum_{q\le P}q/\phi(q)^2$, hence $O_\epsilon(Q^\epsilon(1+U/V))$; the opposite product uses $1+V/U$. This step is independent of the arc widths.

## 4. True signed benchmark, sampling, and bounds

For each fixed pair the minor and error products on their respective fixed arc sets give tensor Fourier coefficients $c_s$, sampled at $s=2kn$ for $N=2n$, with orientations $(- ,+),(+,-),(+,+)$ in the displayed line order. Cauchy in $k$, the $\tau(s)$ bound for the multiplicity of $(k,n)$ with $s=2kn\le16QS$, and torus Parseval give

$$
 \sum_{2n\in\mathcal A}\left\|\sum_{k\le8S}c_{2kn}\right\|_{\rm HS}^2
 \ll_\epsilon S Q^\epsilon\|c\|_{\ell^2}^2 .
 \tag{11}
$$

Pair-specific arcs are fixed independently of $N,k$, so they do not alter this argument. The normalized minor contribution is $Q^\epsilon\sqrt{S/J}X^{1/4}$ up to logs. By (10), the double error is $Q^\epsilon\sqrt{S/J}\,P^{3/2}/\sqrt X$, bounded by the same quantity since $P\asymp\sqrt X$. The single errors give $Q^\epsilon S/\sqrt{JV}$, up to absorbed logarithms and the $O(L^2)$ dyad pairs. These are the first two terms of (1).

The major main term is the [R56](r56-operator-adaptive-arc-full-prefix.md) Ramanujan sum

$$
 \sum_{q\le P}\frac{\mu^2(q)c_q(s)}{\phi(q)^2}
       \int_{-\delta_q}^{\delta_q}
            B_V(\varepsilon_1\beta)\otimes B_U(\varepsilon_2\beta)
              e(-s\beta)\,d\beta.
$$

The omitted $\beta$-tail has tensor norm $O(qS/(P\sqrt{VU}))$, using the two Fourier decays and $\delta_q=2P/(qX)$. The full integral equals the actual continuous-line tensor without its singular factor and has norm $O(\sqrt{V/U})$, by the shorter leg's $L^1$ norm and the longer one's supremum. The elementary absolute Ramanujan bounds from [R49](r49-operator-full-prefix-variance.md) are
$\sum_{q\le P} q|c_q(s)|/\phi(q)^2\ll_\epsilon Q^\epsilon$ and
$\sum_{q>P}\mu^2(q)|c_q(s)|/\phi(q)^2\ll_\epsilon Q^\epsilon/P$.
The full series equals $\mathfrak S(s)$, including the factor at $2$; Fourier inversion restores exactly the signed model of the three lines. After counting aliases the model error is at most

$$
 Q^\epsilon\frac{S}{P}\left(\frac{S}{\sqrt{VU}}+\sqrt{V/U}\right)
 \ll Q^\epsilon\frac{M}{\sqrt{QY}},
$$

since $U\asymp S,\ P\asymp\sqrt{QS},\ Y\le V\le U\le M$. Combining with the origin and unit errors and summing the dyad pairs proves (1).

With $J\gg Q^d$ the four powers in (1) are $1/4+3\gamma/4-d/2,\ \gamma+\sigma/2-d/2,\ \gamma-(1-\sigma)/2,\ (\gamma-\sigma)/2$; the largest is $-1/200$ in each example (2). Independently, terms estimated pointwise are $o(Q^{-1/400})$, with small $\epsilon$. Use (11) without normalizing and Chebyshev on the three sampled products. The exceptional count at that threshold is at most

$$
 \ll_\epsilon Q^{1/200+\epsilon}
       \left[Q^{1/2}M^{3/2}+M^2/Y\right],
$$

giving the two stated exponents. Compressing by any retained coarse projection inside this prefix only decreases the norm; thus the earlier unestimated genuine coarse–coarse and prefix–coarse directions inside the new radius are covered. [R51](r51-operator-full-leg-fine-bridge.md) can start its local-GRH fine deletion at the new radius. The later true prefix–coarse and coarse–coarse blocks, a specified modulus, and full weak S remain open.
