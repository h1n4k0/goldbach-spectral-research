# Joint critical-shell cancellation across a subpolynomial divisor interval under global GRH

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, and $e(z)=e^{2\pi i z}$. Keep the exact prime polynomial $P$ (its two disjoint prime boxes, permissible bounded selector, hard product and unit tests), the genuine complementary coefficient, and the critical-prime shell of the [single polynomial dyad theorem](weak-s-type-ii-critical-prime-polynomial-single-dyad-grh.md). In particular $J=[N-y,N/2)$ with $N/2\le y\le9N/16$, $I_k$ is the actual hard cofactor interval with $k>t\ge N^{.49999}$, and

$$
 D_m=\mathbf1_{m\in J}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                         (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k).
$$

Here $I_d$ is now any single hard interval in $[X,\infty)$, not confined to one dyad. It may be intersected with $[X,N/(2t))$ without removing any term on $J$; replace it by that intersection below. Let $\mathfrak m$ be the number of ordinary dyads $[\lambda X,2\lambda X)$, $\lambda=2^i\ge1$, that meet this effective interval. The empty case is trivial, and otherwise $1\le\mathfrak m\ll L$ with every used $\lambda\le N^{1/100000}$. Keep the literal energy

$$
 \mathcal E_N(D)=\int_{-1/(10N)}^{1/(10N)}
          \sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}
                  |D(a/q+\beta)|^2\,d\beta ,
 \qquad \mathcal Q=[.8X,.9X]\cap\mathbb P.
$$

**Theorem (global Dirichlet GRH).** Assume GRH for all primitive Dirichlet $L$-functions including $\zeta(s)$. For $L^{-1/2}\le\delta\le L_2^{-4}$, uniformly in the actual target and all its hard cutoffs,

$$
 \mathcal E_N(D)\ll
           N\left(\delta +\delta^{-1}\frac{\mathfrak m L_2^{17}}{L}\right)
                    +O(NL^{-2}).
 \tag{1}
$$

In particular on every full interval $I_d\subset[X,CX\exp(L^\theta)]$ for fixed $C>0$ and $0<\theta<1$ the energy is $O_{C,\theta,\epsilon}(NL^{-(1-\theta)/2+\epsilon})$. On the full, still subpolynomial, interval $I_d\subset[X,CX\exp(L/L_2^{24})]$ it is $O_C(NL_2^{-3})$. The actual signed full shell, separately centered numerator covariance, and parity-preserving signed even-lattice residual consequently satisfy the respective bounds $O_{C,\theta,\epsilon}(NL^{-(1-\theta)/4+\epsilon})$ and $O_C(NL_2^{-3/2})$, keeping all original unit primes. The original averaging length for the signed residual is $M=\lceil XL^2\rceil$. These are genuine interval estimates, not pointwise single-dyad bounds added in norm. An interval with fixed polynomial width can contain $\asymp L$ dyads, for which (1) does **not** give a saving. There is no claim on that full polynomial union, on other shells, on individual compensated offset squares, or on Hypothesis S.

## 1. Common endpoint transfer, before splitting into dyads

Smooth the genuine squarefree and original-unit coefficient using one physical cutoff $\Omega(m/N)$ and one absolute cofactor cutoff $w(k)$ obtained by smoothing the interval $I_k$ inward in $\log k$. Intersect $I_k$ with $(0,X/2)$ first; it removes nothing since $d\ge X$, $m<N/2$. Both weights lie in $[0,1]$, have uniformly bounded variation, and differ from their hard indicators only on respective endpoint strips of widths $O(N\delta)$ and $O(\delta)$ in $\log k$. Use a fixed compact mollifier with the derivative bounds of the single-dyad proof; on a log interval shorter than twice the smoothing width the zero cutoff is also admissible.

For the physical transfer it is essential to use the **entire** interval $I_d$. Let $J_{\mathrm e}\subset J$ be a physical endpoint strip or any real hard interval of length $H\ll N\delta$ in $J$. On squarefree $m$ the genuine signed sum equals $\mu(m)$ times the sum of $\mu(k)$ over the actual short labels, with the true cofactor and long cuts. After squaring, drop the product-unit and squarefree masks by nonnegativity. We prove the ordinary bound $O(N\delta+N^{.99}+NL^3e^{-c\Phi})=O(N\delta)$, where $\Phi=L^{3/5}(\log L)^{-1/5}$, for this actual physical edge.

For any two signed short labels $a,b<X/2$, the allowed $m$ form the exact interval $J_{\mathrm e}\cap aI_d\cap bI_d$, and they are multiples of $[a,b]$. The signed continuous lcm contribution is $O(H)$ by the uniform unmasked DIT interval form (stated and used in the [full-unit lcm proof](weak-s-type-ii-critical-prime-unconditional-all-targets.md#1-the-signed-lcm-form-with-the-full-unit-mask)), since at each real product $x$ the short-label set is the single interval $I_k\cap (x/I_d)$. For $g=(a,b)>G=\lfloor N^{1/100}\rfloor$, the total absolute floor error is $O(X^2/G)$. For $g\le G$ keep the sign of the free variable. In the actual discrete count put $a=gu,b=gv,m=guv z$ with pairwise coprimality on the squarefree signed support. Fix $g,u,z$. Every retained $v$ is in one hard interval with mask $(v,gu)=1$, because $gv\in I_k$, $v z,u z\in I_d$, and $guv z\in J_{\mathrm e}$; the $u z$ condition is already fixed. The nonempty interval is at scale $N/(guz)$ by the physical gate, regardless of how short it is. Its endpoints are polynomial since $gv>t$ and $gv<X/2$. The ordinary signed masked Mertens estimate of the [reciprocal unit-tail proof, §1](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md#1-the-true-global-omitted-unit-cost) therefore bounds its signed sum by

$$
                  O\big((N/(guz))e^{-c\Phi}\big).
$$

Indeed $v\gg N^{.48999}$ and $gu\ll X$; subtraction of prefixes handles every strict or moving endpoint. Sum $1/z,1/u,1/g$ over their positive ranges, each bounded by a power of $N$, at total cost $O(L^3)$. This gives a small-gcd actual signed error $O(NL^3e^{-c\Phi})$ with no width factor from $I_d$. Likewise the signed continuous small-gcd term is negligible: at fixed real $x,g,u$ its free $v$ interval has the same coprime mask and polynomial endpoints, with denominator $guv$; use the reciprocal masked bound by Abel and sum the remaining reciprocal weights. Subtract it from the full continuous contribution and insert the true small-gcd count. This proves the global physical edge bound.

For either cofactor edge the labels $k$ lie in a relative strip of width $O(\delta)$ about a single $k_{\mathrm e}$. Then $d=m/k$ for actual $m\in J$ belongs to a proportional interval of bounded ratio (at most $(8/7)e^{O(\delta)}$), meeting $O(1)$ dyads regardless of $\mathfrak m$. On each such dyad the sharp cofactor-edge proof of the [single polynomial dyad theorem, §1](weak-s-type-ii-critical-prime-polynomial-single-dyad-grh.md#1-literal-endpoint-and-arithmetic-transfers-on-the-polynomial-dyad) gives ordinary squared error $O(N\delta)$ also at the present $\delta$. Its narrow continuous form is $O_B(\delta+K^{-1}+\delta^2L_2^3+L^{-B})=O(\delta)$, since $K=X/\lambda$ is still at polynomial scale and $\delta\le L_2^{-4}$. Its fixed cutoff $G=\lfloor L^3\rfloor$ gives the absolute actual small-gcd terms $N\delta^2(1+\log(2G))+\delta A_0G+\lambda^2G^2=O(N\delta)$ and large floor $O(K^2/G)$, uniformly for $A_0=\lambda X$. Sum by the triangle inequality only over this bounded number of dyads. Bounded-BV weights are handled by the same hard-prefix representation in the actual ordinary norm. No loss proportional to $\mathfrak m$ multiplies either physical or short edge. The combined genuine smoothing squared error is thus $O(N\delta)$.

## 2. Exact auxiliary truncations and joint Fourier completion

On a true dyad $i$, write $A_i=\lambda_iX$, $K_i=X/\lambda_i$ and let $I_i=I_d\cap[A_i,2A_i)$. For completion only, let $w_i(z)$ be $w(K_i z)$ times one fixed compact smooth bump supported on a positive proportional interval and equal to one on $[7/32,1/2]$. The actual short normalized range for $m\in J$ lies there, so with $\Omega$ present this changes no coefficient. The derivatives of these $w_i$ satisfy the single-dyad bounds uniformly; the fixed bump gives only bounded derivative terms. Each pre-$\Omega$ coefficient has support in a fixed compact $m/N$ interval.

Keep exact $(d,N)=1$ inside each dyad sum and use the auxiliary squarefree and short inclusion truncations exactly as in the single polynomial dyad theorem. More explicitly, define

$$
 B_{i,m}^{\dagger}
  =\left(\sum_{\substack{dk=m,\ d\in I_i\\(d,N)=1}}\mu(d)w_i(k/K_i)\right)
        \left(\sum_{\substack{l\le T,\ l^2\mid m\\(l,N)=1}}\mu(l)\right)
        \left(\sum_{\substack{h\mid\operatorname{rad}N,\ h\mid m\\h\le H_0}}\mu(h)\right),
 \qquad T=L^{16},\quad H_0=\exp(C_0L_2^2).
 \tag{2}
$$

As before squarefree truncation occurs while true product units are still present, so $l$ is restricted to units in the approximation, and only afterward short inclusion is shortened. The true long unit makes $h\mid m$ equivalent to $h\mid k$ in each summand. Equations (3)–(5) of the cited single-dyad proof, with their $\log(2\lambda\ell)$ or $\log(2\lambda r)$ terms bounded by $O(L)$, give ordinary norm $O(\sqrt N)$ per dyad and ordinary approximation squared errors $O(NL^{-10})$ per dyad. Indeed the square tail is $O(NL T^{-3/4})$, and the truncated short-unit tail is $O(NT^2L e^{-C_0L_2}L_2^{O(1)})$, with $C_0$ a sufficiently large fixed constant. The bounds remain valid before the common physical weight, on the compact proportional supports of each localized $w_i$. The approximation to the actual common smooth coefficient is $\Omega(m/N)\sum_i B_{i,m}^{\dagger}$. The errors just estimated sum to $O(NL^{-8})$ in squared norm by Minkowski, since $\mathfrak m\ll L$. In particular this full approximant with $\Omega$ has ordinary norm $O(\sqrt N)$: the true ordinary norm on the full interval is $O(\sqrt N)$ by the same unmasked signed short-label DIT form plus the absolute $O(X^2)$ floor total, and the approximation errors have just been bounded.

For the joint product inversion put $G_\beta(v)=\Omega(e^v)e(\beta N e^v)$. Use the single common $\tau$ Fourier integral of $G_\beta$. The two phase factors at each dyad multiply to $e(\tau\log(m/N))$, since $A_iK_i=N$. For the high $\tau$ tail use the full additive sampled vector before any character expansion: the ordinary norm of $\sum_i B_{i,m}^\dagger e(\tau\log(m/N))$ is at most $O(\mathfrak m\sqrt N)$, with degree $O(N)$. The separated-center derivative bound of the [single dyad Fourier truncation](weak-s-type-ii-critical-prime-polynomial-single-dyad-grh.md#2-the-two-different-fourier-truncations) gives sampled norm $O(\mathfrak m N)$. Since $|\widehat G_\beta(\tau)|\ll_r\delta^{1-r}|\tau|^{-r}$ and $\delta^{-1}\le L^{1/2}$, truncate at $|\tau|\le L^4$ with an arbitrary fixed inverse-log error, uniformly in $\beta$. This avoids any polynomial loss from the longest dyad. Projection to the nonconstant component of each group of actual nonzero numerators is a contraction, so the same estimate holds for its high $\tau$ tail without introducing any repeated numerator-zero samples.

For each fixed squarefree $l\le T$, $s\mid l$, $(l,N)=1$, write $d=su$, $k=(l^2/s)hv$ with the exact $(u,lN)=1$ and $su\in I_i$. Define

$$
 U_i=A_i/s,\quad x_{q,i}=K_i s/(q l^2),\quad x_{0,i}=K_i s/(Xl^2),\quad
 f_i(z)=w_i(z)e(\tau\log z),\quad Y_\tau=1+\delta^{-1/2}+|\tau|,
$$

and

$$
 a_i(u)=\mu(u)\mathbf1_{su\in I_i}\mathbf1_{(u,lN)=1}
                                    e(\tau\log(su/A_i)).
$$

Thus $U_i x_{0,i}=X/l^2$, and $\widehat f_i$ has the uniform envelope $\ll\min(1,(Y_\tau/|\xi|)^2)$ and derivative $O(1)$ at every real $\xi$. The true nonprincipal expression is the sum across dyads of the Poisson formula (7) of the single-dyad theorem, with the same common $\tau_q(\chi)\mu(l)\mu(s)\chi(l^2)$ factor. Truncate each dual variable to $0<|j|\le J_i=\lambda_iN^{1/1000}$. The mesh $x_{q,i}/h\gg(\lambda_i T^2H_0)^{-1}$ makes the remainder power-small by the same repeated integration by parts, even after summing all dyads and all labels. All retained $j,h,l$ are nonzero modulo shell primes.

For fixed $(l,s,\tau)$ the square of the actual joint nonprincipal norm can now be bounded by adding the principal algebraically after removing the Gauss magnitude, and then adding the square of residue zero. Precisely, for each $q$ and $v\in\mathbb F_q$ define the completed vector

$$
 S_{i,q}(v)=
   \sum_{\substack{h\mid\operatorname{rad}N,\ h\le H_0\\
                   0<|j|\le J_i\\ u\in\operatorname{supp}(a_i),\ hu/j\equiv v\bmod q}}
      \frac{\mu(h)x_{q,i}}h\,a_i(u)\widehat f_i(jx_{q,i}/h),
$$

Multiplicative orthogonality gives the upper bound

$$
                    \sum_q q(q-1)
                     \sum_{v\in\mathbb F_q}\left|\sum_i S_{i,q}(v)\right|^2 .
 \tag{3}
$$

The weights $q(q-1)$ are common; both added squares in (3) apply to the full sum, not to an independently approximated dyad. They do not replace the actual principal and nonunit components, treated in §4 below.

## 3. Distant cross-dyad correlations on the determinant diagonal

Equip the vector in $(q,v)$ with the positive weights $q(q-1)$ of (3). The [single dyad proof, §§3–4](weak-s-type-ii-critical-prime-polynomial-single-dyad-grh.md#3-the-nonzero-determinant-the-only-conditional-step) bounds each completed individual squared norm by $O(N^2Y_\tau L_2^8/(L l^2)+N^{1.91})$, not merely the corresponding genuine nonprincipal squared norm. Let $Z_*=\exp(L_2^5)$ and $F_*=\exp(L_2^2)$. Each dyad meets $O(L_2^5)$ other dyads of ratio at most $8 Z_*$ in either direction. Apply Cauchy to these near correlations in the completed positive norm. Their entire cost is

$$
        O\left(\frac{N^2Y_\tau\mathfrak m L_2^{13}}{L l^2}
                              +\mathfrak m L_2^5 N^{1.91}\right).
 \tag{4}
$$

For every remaining ordered pair of dyads, assume without loss of generality $\Delta=\lambda_2/\lambda_1>8 Z_*$ (the reversed cross term is conjugate), with long supports of lengths $O(U_1)$, $O(U_2)$. Its exact residue equation is

$$
                            h_1 j' u-h_2 j u'=bq.
 \tag{5}
$$

For $b\ne0$ the same GRH additive Möbius estimate gives $O(N^{1.91})$ per pair. In fact fix $(h_1,h_2,j,j',b)$; the three Fourier factors are $A_1(h_1j'\theta)$, $\overline{A_2(h_2j\theta)}$, and a sum over $q$ at distinct frequencies $-bq$, where $A_i(\theta)=\sum a_i(u)e(u\theta)$. The exact third-factor weights now contain $x_{q,1}x_{q,2}$ and satisfy the same bound $O(X^2)$. Since $U_i\le X\lambda_{\max}$, the uniform Baker–Harman bound after the actual coprimality convolution gives $\|A_1\|_\infty\ll U_1^{4/5}$, and the other norm is $O(\sqrt{U_2})$. The tuple count is $\ll\lambda_{\max}^4N^{3/1000+o(1)}$ by $|j|,|j'|\le\lambda_{\max}N^{1/1000}$ and $|b|\ll\lambda_{\max}^2N^{1/1000+o(1)}$. Exactly the exponent $1.9+5.3/100000+3/1000+o(1)<1.91$ results. Even $O(L^2)$ such errors are harmless. This step and the corresponding individual off-diagonal input in (4) are the only uses of GRH.

For $b=0$, fix $q,h_1,h_2$ and put $g=(h_1,h_2)$, $w_{q,i}=x_{q,i}/g$, $w_{0,i}=x_{0,i}/g$. The exact $(uu',N)=1$ implies $h_1/g\mid j,h_2/g\mid j'$. After rescaling these dual indices the equality is $i'u=i u'$; as usual write $i=\sigma d_0 r$, $i'=\sigma d_0 r'$ for the common sign $\sigma$, positive $d_0,r,r'$ and $(r,r')=1$, and then $u=r z,u'=r'z$ for positive $z$. Partition $r$ into dyads $R\le r<2R$. The actual supports now force

$$
 U_2=\Delta U_1,\qquad w_{q,2}=w_{q,1}/\Delta,\qquad
 \tfrac12\Delta R\le r'\le4\Delta R,\qquad z\ll U_1/R .
 \tag{6}
$$

In particular the sampled arguments $d_0r w_{q,1}$ and $d_0r'w_{q,2}$ are comparable despite the disparate dyads. The long phase carries an additional constant of modulus one from the normalizations $A_1,A_2$, and the remaining phase is $e(\tau\log(r/r'))$; $z$ cancels exactly. The signed squarefree support and all exact hard cutoffs are the same as in the single-dyad diagonal calculation, with the two possibly different intervals $I_1/s,I_2/s$.

We bound the unweighted inner integer diagonal before multiplication by $q(q-1)x_{q,1}x_{q,2}\mu(h_1)\mu(h_2)/(h_1h_2)$.

* **High sampled arguments.** If either sample exceeds $F_*$, both exceed a constant times $F_*$ by (6). The fourth-power envelope in $d_0$ gives $\ll Y_\tau^4/(Rw_{0,1}F_*^3)$ exactly as in the single-dyad proof. There are $O(\Delta R^2)$ possible $(r,r')$ and at most $O(U_1/R)$ positive $z$ per pair. Thus at one ratio dyad the cost is $\ll(\Delta U_1 Y_\tau/w_{0,1})(Y_\tau/F_*)^3$. The number of possible ratio dyads is $O(L)$ and $Y_\tau$ is fixed-polylogarithmic. This error is negligible to every fixed inverse log power.
* **Low sampled arguments and squarefree floors.** Now $d_0\ll F_* /(Rw_{0,1})$ and the surviving $R\ll F_*/w_{0,1}\le\lambda_1 N^{o(1)}$, while $r'\le\lambda_2N^{o(1)}$. The exact positive integer $z$ interval is $(I_1/s)/r\cap(I_2/s)/r'$, with all actual endpoints, and $z$ carries $\mu^2(z)\mathbf1_{(z,lNrr')=1}$. Formula (12) of the single-dyad theorem replaces this count by its exact continuous density, with error $O(\sqrt{U_1/R}\,N^{o(1)})$ per $(r,r')$. The mask $lNrr'$ is at most $N^{1+2/100000+o(1)}$. Since $R/U_1\le N^{-1/2+o(1)}$, the full error per ratio dyad, including its $d_0$ and $(r,r')$ counts, is

$$
 \ll \Delta R^2(F_* /(Rw_{0,1}))\sqrt{U_1/R}\,N^{o(1)}
      \ll (\Delta U_1/w_{0,1})N^{-1/4+o(1)} .
$$

The enlarged $\Delta$ count is canceled by the mesh product below, rather than by taking independent absolute bounds on the dyads.
* **Signed continuous contribution.** In the exact density use the factorization $\mathfrak d(lN)\kappa(r)\kappa(r')$, where $\kappa(r)=\prod_{p\mid r}(1+1/p)^{-1}$ and $r,r'$ are units and coprime before this factorization. Impose $(r,r')=1$ by $\sum_{c\mid r,r'}\mu(c)$. Fix $z,d_0,c$; the remaining two sums have separate genuine hard tests of the ratio range, long label $rz$ or $r'z$, dual cut $J_1$ or $J_2$, and each low sampled argument. Hence each is a single hard interval with its actual coprimality mask. Every possible $c\ll R$ divides the smaller $r$, so in the larger variable $n'=r'/c\gg\Delta>Z_*$ up to fixed factors. Thus **all** these $c$, rather than only a small-$c$ region, admit the signed damped Mertens estimate (14) of the single-dyad theorem on the larger leg. The true mask there is $lNc\le N^2$ and the sign is $\mu(c)\mu(n')$ with $(n',c)=1$. Its continuous test has variation $O(1+|\tau|+F_*)$ by the derivative of $\widehat f_2$ and (6). Abel therefore bounds this leg by $O((\Delta R/c)\exp(-c_1L_2^{5/2}))$; the smaller leg is bounded by $O(R/c)$ by counting positive multiples. Sum over $c$, at cost $O(\Delta R^2\exp(-c_1L_2^{5/2}))$. The $z$ interval has length $O(U_1/R)$ and the $d_0$ count is $O(F_* /(Rw_{0,1}))$. Their product yields

$$
           O\big((\Delta U_1/w_{0,1})F_*
                           \exp(-c_1 L_2^{5/2})\big)
$$

per ratio dyad. This is negligible after all $O(L)$ ratio dyads, to any fixed inverse log power.

When each inner bound is multiplied by the actual weight, the $\Delta$ cancels, because exactly

$$
        x_{0,1}x_{0,2}\frac{\Delta U_1}{w_{0,1}h_1h_2}
              =\frac{X}{l^2[h_1,h_2]}.
$$

Uniform constant factors suffice to replace the ratio $q/X$ in the actual meshes. Sum over $q$ using $\sum q(q-1)\ll X^3/L$, and over the $h$ pairs using $\sum_{h_1,h_2\mid\operatorname{rad}N}1/[h_1,h_2]\ll L_2^3$. The resulting distant cross determinant-zero norm contribution is $O_A(N^2Y_\tau L^{-A}/l^2)$ per pair for any fixed $A$. These far-cross estimates retain the genuine signs through the old squarefree count, the larger reduced ratio, and the actual moving gates. The positive norm (3) now follows from (4) with negligible errors.

Minkowski in the shared $\tau$ and in the $(l,s)$ labels finishes the genuine nonprincipal norm. As before,
$\int|\widehat G_\beta(\tau)|\sqrt{Y_\tau}\,d\tau\ll\delta^{-1/2}$ by the minimum envelope from the compact physical test, and $\sum_{l\le T}\tau_{\mathrm d}(l)/l\ll(1+\log T)^2\ll L_2^2$. After squaring this gives $L_2^4$ times (4), and integrating $\beta$ has length $1/(5N)$. The true additive nonprincipal factor $q/(q-1)$ is bounded. Hence the genuine nonprincipal contribution on the full interval is

$$
                 O\big(N\delta^{-1}\mathfrak m L_2^{17}/L\big)
$$

plus negligible errors. This estimates the exact sum over dyads using the near and distant covariances, rather than a triangle inequality over $\mathfrak m$ at the main scale.

## 4. Actual nonunits and the literal complete shell

One may not sum absolute nonunit estimates across all dyads. Instead use the original signed $\mu(d)$ in the untruncated physical expression. When $q\mid N$, there are no $q$-nonunits: $k<X/2<q$ and the exact long unit prevents $q\mid d$. Otherwise, $q\mid m$ still forces $d=qj$, with $\mu(qj)=-\mu(j)\mathbf1_{(j,q)=1}$. With $\Omega$ restored the local smooth bumps all equal one, so the actual cofactor test is the same global $w(k)$ over the entire interval. Since $l\le T<q$, $s=(l,d)=(l,j)$, and $j=su$. For each fixed $l,s,h$, the exact cutoff is $k\equiv0\bmod l^2h/s$ and $(u,lNq)=1$, with the sign $\mu(u)$ times a fixed signed factor.

If $u\ge Z_*$ split into $u\asymp R$. The number of actual $k$ in its required positive multiples is $O(X/(R l^2h))$, since $qsu k\asymp N$ and $q\asymp X$. For each fixed such $k$, $u$ lies in one actual hard interval with mask $(u,lNq)=1$. Its factor $\Omega(qsu k/N)e(\beta qsu k)$ has uniformly bounded variation on that interval, independently of smoothing width: $\Omega$ has bounded variation and $|\beta|N\ll1$ on the real product support. The signed Mertens estimate (14) of the single-dyad theorem applies with $\kappa=1$, at cost $O(R\exp(-c_2L_2^{5/2}))$ with the mask $lNq\le N^2$. After summing the $k$ count and the $O(L)$ dyads of $u$, this leaves a negligible bound at scale $X/(l^2h)$. For $u<Z_*$ count $k$ absolutely at each $u$, at most $O(X/(u l^2h))$, and sum harmonically. The total nonunit value at any $q,\beta$ is consequently $O(XL_2^6)$, since $\sum_{l\le T}\tau_{\mathrm d}(l)/l^2\ll1$, $\sum_{h\mid\operatorname{rad}N}1/h\ll L_2$ and $\log Z_*=L_2^5$. Its actual nonzero-numerator squared shell contribution is $O(N L_2^{12}/L)$, independently of $\mathfrak m$.

The actual principal unit character contribution uses the exact ordinary numerator-zero value minus this actual $q$-nonunit value, with factor $(q-1)^{-1}$ after summation over nonzero numerators. The ordinary squared norm of the full approximant with $\Omega$ is $O(N)$, as shown in §2, and $\sum_q(q-1)^{-1}\ll1/L$. This gives $O(NL_2^{12}/L)$ as well (a weaker bound than needed for the nonunit subtraction here). Neither is the principal term artificially added in the positive square (3).

Finally the literal critical arcs are disjoint, so ordinary Parseval transfers the full original smoothing error $O(N\delta)$ and the smaller truncation errors to the shell; combine with the joint bound and the two constant components. This proves (1). Optimize the displayed bound at $\delta=L^{-(1-\theta)/2}$ on a width $\exp(L^\theta)$, with $\mathfrak m=O(1+L^\theta)$, and at $\delta=L_2^{-4}$ when $\mathfrak m=O(L/L_2^{24})$. The relevant large-$N$ inequalities on $\delta$ hold in both cases. The genuine $P,D$ have ordinary norm $O(\sqrt N)$, so Cauchy and the contraction of separate centering give the first two signed bounds. The [parity-preserving signed identity](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md) uses the genuine odd supports, the original physical product bounds and these ordinary norms, with its additive error $O(N/L+N(X/M)^2)$. Applying it only after returning to the true coefficients gives the last signed bound.
