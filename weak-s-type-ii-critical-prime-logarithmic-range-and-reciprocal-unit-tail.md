# A logarithmically wider critical-prime shell bound with reciprocal unit loss

Let $N$ be even, $X=\sqrt N$, $L=\log N$, and $L_2=1+\log L$. Keep the true two-prime polynomial $P$ and the complementary coefficient $D_m$ of the [composite-square and unit-tail theorem](weak-s-type-ii-critical-prime-composite-square-and-unit-tail.md), including the permissible bounded prime selector, its two true prime boxes and unit tests, and all actual hard cutoffs. The new allowed range is any hard interval $I_d\subset[X,C X L^\gamma]$, with fixed $C>1$ and $\gamma\ge0$. In detail, $J=[N-y,N/2)$ with $N/2\le y\le9N/16$, and the complementary coefficient is

$$
 D_m=\mathbf1_{m\in J}
        \sum_{\substack{dk=m,\ d\in I_d,\ k\text{ in its true hard range}\\
                        (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k).
$$

The true interval of $k$ includes $k>t\ge N^{.49999}$. Write $D(\alpha)=\sum_mD_m e(m\alpha)$ with $e(z)=\exp(2\pi iz)$ and denote its squared norm on the original critical prime arcs by

$$
 \mathcal E_N(D)=
 \int_{-1/(10N)}^{1/(10N)}
 \sum_{\substack{q\ {\rm prime}\\ .8X\le q\le .9X}}
            \sum_{a=1}^{q-1}|D(a/q+\beta)|^2\,d\beta .
$$

**Pointwise theorem.** Fix $c>0,\gamma\ge0$ with $2c+2\gamma<1$, an even divisor $R\mid N$ with $2^{\omega(R)}\le L^c$, and any $\varepsilon>0$. Define

$$
 \eta_0=(1-2c-2\gamma)/4,\qquad
 \mathcal V(N,R)=\sum_{\substack{p\mid N\\p\nmid R}}\frac1p .
$$

Then, uniformly in all original hard cutoffs,

$$
 \mathcal E_N(D)
 \ll_{C,c,\gamma,\varepsilon}
       N\big(L^{-\eta_0+\varepsilon}+\mathcal V(N,R)\big).
 \tag{1}
$$

The original signed full shell, the covariance after subtracting the two numerator means separately, and the parity-preserving signed even-lattice residual with averaging length $M=\lceil XL^2\rceil$ are all

$$
 O_{C,c,\gamma,\varepsilon}\!\left(
       N L^{-\eta_0/2+\varepsilon}+N\sqrt{\mathcal V(N,R)}\right).
 \tag{2}
$$

Here the signed residual is its signed sum, not a squared bound on its individual offsets. The factor $\log p$ from the former omitted-unit weight is absent. In particular $R=\operatorname{rad}N$ gives no unit error on the low-radical family.

**Density consequence.** Fix $C>1$, $0\le\gamma<1/2$ and $A>0$. For each sufficiently large $Y$, outside $O_{C,\gamma,A}(Y(\log Y)^{-A})$ even targets in $[Y,2Y]$, the true energy is $O_{C,\gamma,A}\big(N/\log^2(2+\log\log N)\big)$ and each signed bound is $O_{C,\gamma,A}\big(N/\log(2+\log\log N)\big)$. Alternatively, excluding only a density-zero family of size $O(Y/\log(2+\log\log Y))$ in each dyad, the energy is $O_{C,\gamma}\big(N/((1+\log\log N)\log(2+\log\log N))\big)$ and the signed bound is its square root times $\sqrt N$. These are simultaneous in the original cutoffs and selectors. All results are unconditional. They do not treat pointwise unrestricted unit radicals, polynomial growth of $d/X$, the other shells, or Hypothesis S.

## 1. The true global omitted-unit cost

Put

$$
 F_m=\mathbf1_{m\in J}
            \sum_{\substack{dk=m,\ d\in I_d\\
                          k\text{ in its true hard range}}}\mu(d).
$$

We have $D_m=\mu^2(m)\mathbf1_{(m,N)=1}F_m$ exactly. On squarefree $m$, $k$ is automatically squarefree and $(d,k)=1$; every nonzero term of $D_m$ is on that support. Below, $F$ without these restrictions is used solely as an auxiliary signed ordinary norm.

We prove for the full, possibly several-dyad divisor interval the stronger estimate

$$
        \sum_{p\mid m}|F_m|^2\ll_{C,\gamma}N/p
                       \qquad(p\le N^{1/100},\ p\ {\rm prime}).
 \tag{3}
$$

Use the square expansion of the preceding theorem: $a,b$ are its squarefree signed divisors, $g=(a,b)$, and the integer $m$ conditions become a single interval and the divisibility $[a,b,p]\mid m$. Set $U=C X L^\gamma$ and $G=\lceil (U/X)^2p\rceil$. For $g>G$, the absolute floor error is $O(U^2/G)=O(N/p)$. At fixed real $x\in J$ the continuous signed form is on the true interval $I(x)$ imposed by $I_d$ and the reciprocal $k$ conditions. Stripping $p$ from each of $a,b$ gives $p^{-1}$ times the positive lcm form of the difference of two signed $p$-coprime interval vectors, exactly as the preceding proof with $\ell=p,j=1$. The positive coprime convolution and the Dress–Iwaniec–Tenenbaum signed interval bound are uniform in the interval, not in a bounded ratio of its endpoints only. Thus the full continuous contribution is $O(N/p)$.

It remains to bound the actual and continuous $g\le G$ terms, keeping a sign in one long coordinate. The uniform ordinary estimate used here is, for polynomial-scale $N^{.45}\le Z\le N^2$ and any integer $B_0\le N^2$,

$$
 \left|\sum_{\substack{n\le Z\\(n,B_0)=1}}\mu(n)\right|
 \ll Z\exp\!\left(-b(\log N)^{3/5}(\log\log N)^{-1/5}\right)
 \tag{4}
$$

for some absolute $b>0$ and sufficiently large $N$. It is a consequence of [Lee–Leong, Theorem 2.2, (23)](https://arxiv.org/html/2208.06141v5#S2.SS2) for the ordinary Mertens sum. Indeed impose $(n,B_0)=1$ by convolving $\mu$ with the indicator of integers all of whose prime factors divide $B_0$. For convolution divisor $h\le\sqrt Z$, use the ordinary Mertens bound at $Z/h$ and the reciprocal weight $\prod_{p\mid B_0}(1-1/p)^{-1}=L^{O(1)}$. For $h>\sqrt Z$, use the trivial bound $Z/h$ and Rankin at $1/4$, at cost at most $Z^{7/8}\prod_{p\mid B_0}(1-p^{-3/4})^{-1}=Z^{7/8}\exp(o(L))$. For these Euler bounds split at $p=L^2$: the sums over smaller primes are at most the corresponding sums over all integers, and there are $O(L/\log L)$ larger prime divisors. This proves (4) and also gives the same type of bound on hard intervals with polynomial-scale endpoints. By Abel summation, the corresponding signed reciprocal sum over an interval between $N^{.45}$ and $N^2$ is at most $O(L\exp(-b L^{3/5}(\log L)^{-1/5}))$. After decreasing $b$, denote the stretched exponential savings in these bounds by $e^{-b\Phi}$, with $\Phi=L^{3/5}(\log L)^{-1/5}$.

For the actual small-gcd term write $a=gu$, $b=gv$, $m=guvr$, where $g,u,v$ are squarefree and pairwise coprime when the signed summand is nonzero. For fixed $g,u,r$, the true conditions on $v$ are a single hard interval: $gv\in I_d$, $vr$ in the cofactor range, and $guvr\in J$. The remaining cofactor condition $ur$ is already fixed. Keep the exact $(v,gu)=1$ and the sign $\mu(v)$. One has $u,v\in[X/g,U/g]$ and $1\le r\ll g$, since $[a,b]\ge X^2/g$. If $p\mid gur$, the divisibility $p\mid m$ is automatic; use (4) on $v$. Save a factor $1/p$ when summing whichever of $g,u,r$ is forced to be divisible by $p$, partitioning with any fixed priority when several divide. In detail the unrestricted harmonic sum over $g$ is $O(1+\log G)$, while the $p$-divisible one is $O((1+\log G)/p)$; the integer counts of $u$ and $r$ are $O(U/g)$ and $O(g)$, respectively, with a factor $1/p$ if the corresponding divisibility is imposed. If $p\nmid gur$, require $v=pw$ and use $\mu(v)=-\mu(w)\mathbf1_{p\nmid w}$ with $(w,gu)=1$. This gains $1/p$ in the scale of the free variable and still has exactly one hard interval. All nonempty $v$ or $w$ intervals have endpoints between $X/(G p)$ and $U$, apart from a bounded floor adjustment. Since $p\le N^{1/100}$, $X/(G p)\gg N^{.48}L^{-2\gamma}$ up to a fixed factor, which is greater than $N^{.45}$ for large $N$. The coprimality parameter is at most $pgu\le pU<N^2$. Thus (4) is uniform in every actual summation. After summing $g,u,r$ as just described, the absolute bound on the resulting signed small-gcd term is

$$
 O_{C,\gamma}\left(\frac{U^2}{p}(1+\log G)e^{-b\Phi}\right)=O_{C,\gamma}(N/p).
$$

For the continuous small-gcd term, fix real $x$ and $g,u$, retaining the sign in $v$. Its interval now has $gv\in I(x)$ and $(v,gu)=1$. When $p\mid gu$, the denominator is $guv$ and the $g$ or $u$ harmonic sum gains $1/p$ by that divisibility. When $p\nmid gu$, split $p\mid v$ (denominator $guv$, use $v=pw$) and $p\nmid v$ (denominator $pguv$, add $p$ to the coprimality mask). In each case the reciprocal version of (4) gives $e^{-b\Phi}$ up to fixed logarithmic factors and the total retains $1/p$. The $u$ reciprocal sum on $[X/g,U/g]$, with any prescribed divisibility, is $O((1+\log U)/A_u)$ for modulus $A_u$; the $g$ reciprocal sum obeys the same type of elementary bound. The continuous small-gcd part is therefore $O_{C,\gamma}(N/p)$ after integration. Subtract it from the full continuous main and insert the actual small-gcd contribution. With the large-gcd floor estimate this proves (3).

For the omitted primes $p\mid N$ above $N^{1/100}$, the elementary divisor bound $|F_m|\le\tau(m)\ll_\epsilon N^\epsilon$ and the count of multiples $O(N/p)$ give total $O(N^{1-\delta_0})$ for some absolute $\delta_0>0$, by choosing $\epsilon$ small. Since the change of a product indicator is at most one and occurs only on a multiple of a genuinely omitted prime, (3) implies

$$
 \left\|D-\mu^2(\cdot)\mathbf1_{(\cdot,R)=1}F\right\|_2^2
              \ll_{C,\gamma} N\mathcal V(N,R)+N^{1-\delta_0}.
 \tag{5}
$$

This is an ordinary coefficient norm for the entire long interval, before any dyadic decomposition, so no dyadic summation multiplies the unit error.

## 2. Uniform exact transfers on one divisor dyad

From now on retain the $R$-unit gate. Partition the actual divisor interval into disjoint half-open dyadic pieces, with $A_0=\lambda X\le d<2A_0$, $\lambda=2^j$ and $1\le\lambda\ll_C L^\gamma$, and write $K=X/\lambda$. Intersect these with the actual hard interval; bounding $k$ on the physical support gives $k\asymp K$ with fixed absolute proportional constants. For one such piece all estimates below are uniform in $\lambda$ within this range. The modest number of pieces is $O_C(L_2)$.

### Squarefree cutoff

The ordinary forced-square estimate on each dyad is

$$
       \sum_{\ell^2\mid m}|F_m|^2
 \ll C_1^{\omega(\ell)} N\ell^{-2}(1+\log(2\lambda\ell))
                  \qquad(\ell\text{ squarefree}),
 \tag{6}
$$

where here $F$ is restricted to that dyad. This is the composite forced-lcm proof in the preceding theorem, with the following change of scales. In its large-gcd floor error take $G=\lceil\lambda^2\ell^2\rceil$, giving $A_0^2/G\ll N/\ell^2$. The full continuous signed form remains $O(C_1^{\omega(\ell)}N/\ell^2)$, by the same $\ell^2$ factor in the lcm after stripping the prime divisors of $\ell$ from $a,b$. In its actual small-gcd count with $a=gu,b=gv$, we now have $u,v\asymp A_0/g$ and $r=m/[a,b]\asymp g/\lambda^2$. Thus at fixed $g$ the product of the three upper lengths is $O((A_0/g)^2(g/\lambda^2))=O(N/g)$; if the upper length for $r$ is below one there is no tuple. For each $p\mid\ell$ either it divides none of $g,u,v$ and $p^2\mid r$, or it divides exactly one of them and $p\mid r$. The same four allocations have moduli product $\ell^2$, and the required multiples each save their modulus by counting up to the positive upper bound. In the continuous small-gcd term the denominator $guv$ times the required modulus on $r$ gives the same savings by harmonic sums on the proportional $u,v$ ranges. Summing $g$ costs $1+\log G$. This proves (6), also with bounded-BV label weights via Minkowski in the restricted ordinary norm.

### Smoothing the genuine short label and physical gate

We smooth only the physical and $k$ endpoints within their actual hard intervals, leaving the long $d$ cut sharp. Put $\delta=L^{-B}$ with fixed $B>0$. Use normalized weights $W(m/N), w(k/K)$ as in the preceding theorem, with edge width $O(\delta)$ in each corresponding coordinate. The required ordinary squared error on the genuine squarefree coefficient on this dyad is

$$
                O_B(N L^{-B}L_2+N^{3/4}).
 \tag{7}
$$

For a proof, on squarefree $m$ use $k$ as the signed divisor: $\mu(d)=\mu(m)\mu(k)$, and the common factor has absolute value one. After squaring it is legitimate to enlarge by dropping the common unit and squarefree indicators, exactly as in the [actual endpoint proof](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md). At each real physical variable the signed allowed interval in $k$ stays one actual interval. The signed continuous lcm form is bounded by the same DIT interval theorem. For a physical strip of length $H\ge1$, the actual small-gcd bound at fixed $g$ is $O(H/g+A_0)$: in the representation $m=guvr$ one has $u,v\asymp K/g$, $r\asymp \lambda^2g$, and for fixed $g,r,u$ the free $v$ length is $H/(gru)$. Their reciprocal sums give $H/g$, and the floor part counts $O((K/g)(\lambda^2g))=O(A_0)$ pairs. The continuous small-gcd correction costs $O(H/g)$. The large-gcd floors cost $O(K^2/G)$ at cutoff $G$. Choose $G=\lfloor \min(N/H,K/\sqrt{A_0})\rfloor$, at least one on the used ranges for large $N$. The total is $O(H(1+\log(N/H))+N^{3/4})$, since $K\sqrt{A_0}=X^{3/2}/\sqrt\lambda\le N^{3/4}$. This gives the physical edge cost in (7).

For a short-label edge of width $O(\delta K)$, apply the signed narrow lcm bound (7) of the endpoint proof with $K$ in place of $X$ and the same $L_2$: its proof applies because $\log K\asymp L$, with all the coprime parameters at most $O(K)$, so the same uniform masked reciprocal Mertens estimate and cutoff $\exp(L_2^3)$ work. The form is $O_A(\delta+K^{-1}+\delta^2L_2^3+L^{-A})$, which gives continuous main $O_B(N\delta)$ at $A>B$. For $g\le G$ the small-gcd actual count is bounded by

$$
 \sum_{g\le G}O\!\left(\lambda^2 g(1+\delta K/g)^2\right)
 \ll N\delta^2(1+\log(2G))+\delta A_0G+\lambda^2G^2.
$$

The same bound applies to the small-gcd continuous contribution using $|J|\ll N$ and $1/[a,b]\ll g/K^2$. Take $G=\lfloor L^{B+2}\rfloor$, with large-gcd floors $O(K^2/G)$; all these errors are $O_{B,C,\gamma}(N\delta)$ for polylogarithmic $\lambda$. Bounded-BV weights are handled by summation by parts as in the endpoint theorem and the shorter interval can be empty. These two edge estimates give (7) for the actual smoothing, also with any retained product unit mask. No sharp $d$ endpoint is moved.

## 3. Completion at the longer residue scale

In the smoothed dyad truncate the exact squarefree identity $\mu^2(m)=\sum_{l^2\mid m}\mu(l)$ at $l\le T=L^\eta$, with fixed $\eta>0$. The squared tail is bounded by $\sum_{\ell>T}3^{\omega(\ell)}\sum_{\ell^2\mid m}|F_m^{\rm sm}|^2$, by grouping the two omitted squarefree divisors by their lcm. Thus (6) gives $O_{\rho,C,\gamma}(N T^{-1+\rho} L_2)$ for any fixed small $\rho>0$. The true smoothed squarefree coefficient has ordinary squared norm $O(N)$: use the signed short divisor $k$, the bounded DIT form, and absolute floor count $O(K^2)$ on a dyad, with bounded-BV smoothing applied by Minkowski. The truncated approximant also has squared norm $O_{C,\gamma,\eta}(N)$ by this tail bound.

The exact completion of the preceding theorem retains $l,s\mid l$ and the actual $R$-unit inclusion variables $h\mid R$: on each squarefree signed divisor slice $s=(l,d)$, write $d=su$ and $k=(l^2/s)hv$ with the exact coprime masks and signs. In the logarithmic product Fourier inversion normalize by $d/A_0$ and $k/K$, so their product is $m/N$. The smooth $v$ scale is $V=Ks/(l^2h)\le K$ and the Poisson mesh $V/q\le5/4$ still has uniform compact-support overlap as in the preceding proof. Its integrated square-root Gauss completion cost is the same $\delta^{-1/2}$, using the same first and second physical derivative $L^1$ bounds and cofactor derivative $L^2$ bound at relative width $\delta$. This preserves the exact original $\beta$ interval and all true $k$ gates after (7).

The changed factor is the long $u$ residue norm. Its coefficients are bounded by one in a range of length $O(A_0)$. Every residue occurs $O(1+A_0/q)=O(\lambda)$ times, so multiplicative orthogonality gives its $\ell^2$ norm over characters at most $O(\lambda\sqrt{qX})$. This is a factor $\lambda$ in norm relative to the fixed proportional case. There are still at most $O(T(1+\log T))$ pairs $(l,s)$ and $L^c$ unit choices. Hence, applying the very same Minkowski completion and integrating on the true critical arcs, the nonprincipal squared energy on this dyad is

$$
 O_{C,\eta}\!\left(N\lambda^2 L^{-1+B+2\eta+2c}L_2^2\right).
 \tag{8}
$$

The principal unit character and the $q$-nonunit term are retained in the exact finite Gauss decomposition. For the latter, $k\le X/2<q$ implies $q\mid d$ when $q\mid m$. There are $O(\lambda)$ such $d=jq$ with $j\ll\lambda$; at each $d$ the truncated square multiplier summed absolutely over $k\ll K$ costs at most $O(K\prod_{p\mid d}(1+1/p))$ by the same elementary count of the required multiples $l^2/(l,d)$ as in the preceding theorem. Since $\prod_{p\mid d}(1+1/p)\le2\tau(j)\ll_\varepsilon L^\varepsilon$ uniformly, the $q$-nonunit central value is $O_\varepsilon(XL^\varepsilon)$ per dyad. After summing the nonzero numerator contribution and integrating, this costs $O_\varepsilon(N L^{-1+\varepsilon})$. The principal unit character is bounded by its numerator-zero ordinary integral and this nonunit part, using $\sum_q 1/(q-1)\ll1/L$ and the full-circle norm just proved; its squared contribution is also $O_\varepsilon(N L^{-1+\varepsilon})$. The R82 signed subtracted zero-numerator base is not an isolated term discarded here.

Set $B=\eta=\eta_0$. Since $\lambda\ll_C L^\gamma$, the exponent in (8) is at most $-\eta_0$. The truncation and actual smoothing errors from (6)–(7) also have squared norm $O_\varepsilon(N L^{-\eta_0+\varepsilon})$. Transfer them to the original disjoint arcs by ordinary Parseval. Sum dyads by Minkowski, absorbing the resulting $L_2$ powers into $\varepsilon$. This proves the first part of (1) with the retained $R$ unit mask. The global transfer (5) gives (1) itself, with no dyadic loss on $\mathcal V(N,R)$.

Finally the true hard coefficient on the entire log-wide interval has ordinary energy $O(N)$: use the signed short divisor $k\le X/2$ on squarefree $m$ over the full interval, with the same DIT form and the absolute full floor count $O(X^2)$. The prime-side ordinary energy is $O(N)$. Thus (1) proves the full and centered signed bounds by Cauchy and the contraction of centering. For the exact even-lattice signed residual, the proof of the high-pass identity in the endpoint theorem uses only the physical product support, oddness of both unit legs, and these two ordinary energy bounds. They hold here for the true hard $D$ as well; in particular the multiplier estimate and repeated-zero term still cost $O(N(X/M)^2+N/L)$. This yields (2) at the stated $M$ without an assertion about compensated-offset squared moments.

## 4. True even-target density with the reciprocal loss

Fix $\gamma<1/2$ and choose a fixed $c>0$ such that $2c+2\gamma<1$. For $v=\log\log N$ take $z_N=\kappa v\log(2v)$ and $R_N=\prod_{p\mid N,\ p\le z_N}p$. With fixed sufficiently small $\kappa>0$, the elementary prime upper bound gives $2^{\omega(R_N)}\le2^{\pi(z_N)}\le L^c$; the retained radical is even. On $[Y,2Y]$ use $v_Y=\log\log Y$, $z_*=\kappa v_Y\log(2v_Y)$ and dominate $\mathcal V(N,R_N)$ by $V_N=\sum_{p\mid N,p>z_*}1/p$. Counting actual multiples and using prime dyads gives

$$
 \sum_{N\le2Y}V_N\le2Y\sum_{p>z_*}p^{-2}
                      \ll Y/(z_*\log z_*).
$$

Markov at $1/(v_Y\log(2v_Y))$ gives $O(Y/\log(2v_Y))$ exceptions, proving the faster density-one assertion.

For arbitrary fixed inverse-logarithmic exception count, use $s=z_*\log(2v_Y)/8$. For $p>z_*$, $s/p\le\log(2v_Y)/8$, so the positive divisor expansion on the actual integers gives

$$
 (2Y)^{-1}\sum_{N\le2Y}e^{sV_N}
 \le\prod_{p>z_*}\left(1+\frac{e^{s/p}-1}{p}\right)
 \le\exp(O_\kappa(v_Y^{1/8})).
$$

Indeed its logarithm is at most $s(2v_Y)^{1/8}\sum_{p>z_*}p^{-2}=O_\kappa(v_Y^{1/8})$. Since $s\asymp_\kappa v_Y(\log(2v_Y))^2$, Markov at $K_A/(\log(2v_Y))^2$ for a sufficiently large fixed $K_A$ costs $O_A(Y e^{-A v_Y})$. Inserting this reciprocal cutoff in (1)–(2) proves the stated density conclusion for the genuine hard coefficients. Both exceptional families depend only on the target integers and the fixed parameters, not on the prime selector or the cutoffs.
