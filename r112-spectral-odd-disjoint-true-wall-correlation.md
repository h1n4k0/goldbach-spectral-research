# The ordinary autocorrelation at a true odd-disjoint conductor wall

When one prime of a hypothetical two-prime Page conductor passes near the physical cap wall, the unsigned exceptional component has a boundary term proportional to the cap length. At fixed target radical its shape is the exact ordinary autocorrelation, not a Dickman limit or a matched mean. The formula retains the cumulative term beside the boundary term and recovers opposite signs on the two sides. It does not establish that a Page conductor with any of these properties exists.

## 1. Actual scope and wall profile

Use the genuine even $Y\le N\le2Y$, original $D=\sqrt N(\log N)^{-B}$ for fixed admissible $B>B_0>0$, and real half-open $I\subset(N/2,9N/16]$ with bounded pointwise-BV test $\omega$ of the [interior shift formula](r111-spectral-odd-disjoint-interior-conductor-shifts.md). Write $G=\log Y$, $g=\log G$, and $Q_0=\exp(16\sqrt G/g)$. Fix an even squarefree target radical $R$, namely $\operatorname{rad}(N)=R$. Suppose the actual odd primitive Page conductor is $r=pq$ for distinct odd primes, $(N,r)=1$, with real character $\chi$ and simple real zero $\beta$ in the original Page strip. Assume $\log(Q_0/r)\ge g^3$ and, for fixed $0<c_-<c_+<\infty$,

$$
                       c_-g\le\log p\le c_+g.                    \tag{1}
$$

On the genuine physical $m\in N-I$ put

$$
 \begin{split}
   F(m)&=\omega(N-m)(N-m)^{\beta-1},\qquad L_m=\log m,\\
   T_m&=\log(m/D^2),\qquad d_m=T_m-\log p .
 \end{split}                                                       \tag{2}
$$

The actual unsigned contribution $\mathcal U=-\chi(N)C_r^{[2]}\mathcal P_1/\varphi(r)$ has exactly the convention of the interior shift formula, with the literal finite rational $t\le Q_0/r$ in $\mathcal P_1$. Here $C_r^{[2]}=\prod_{v\mid r,\ v\ {\rm prime}}(1-1/v)(1-2/v)$. The separate signed pole in the genuine exceptional difference is not included in $\mathcal U$.

Let $C_R$ be the ordinary counterpart of (1) of the [shifted autocorrelation proof](r108-spectral-odd-disjoint-shifted-autocorrelation.md) with mask $R$ only. Precisely, for squarefree $j$ coprime to $R$ set

$$
 \begin{split}
 R_{R,j}(u)&=\sum_{\substack{n\le e^u,\;(n,Rj)=1}}
                        \mu(n)\alpha^\circ(n),\\
 C_R(t)&=\sum_{\substack{j\ {\rm sf},\;(j,R)=1}}
       \mu(j)\alpha^\circ(j)^2
       \int_{\mathbb R}R_{R,j}(u)R_{R,j}(u+t)\,du,\qquad
 M_R=\int_{\mathbb R} C_R(t)\,dt .
 \end{split}                                                       \tag{3}
$$

The weights are multiplicative on squarefree integers, with $\alpha^\circ_v=(v-1)/(v^2-2)$ at allowed odd primes, and each primitive is zero below $0$. The same rules with mask $Rr$ define $C_{Rr}$ and $M_{Rr}$. Neither masking notation changes the physical even target. One has $M_R>0$ and $C_R$ even and continuous, with $C_R(0)>0$.

**Theorem.** Under (1) and the above assumptions, uniformly on the same physical tests one has, for a fixed $c>0$,

$$
 \mathcal U=
 -\frac{\chi(N)\Sigma(N)}{r M_R}
   \int_{N-I}\frac{F(m)}{L_m}
           \left[T_m C_R(d_m)-2\int_0^{d_m}C_R(t)\,dt\right]\,dm
       +O_R\!\left(\frac{Y^\beta}{rG}e^{-c\sqrt g}\right).          \tag{4}
$$

The inner integral is directed when $d_m<0$. The factor $\Sigma(N)$ is the binary singular series at the actual target. Constants may depend on original fixed parameters, $R,c_-,c_+$, and the test bound.

For a fixed sufficiently small $d_R>0$, if $\omega\ge0$, $\int_I\omega(u)\,du\gg Y$, and $|d_m|\le d_R$ throughout its support in $N-I$, then $\mathcal U$ has sign $-\chi(N)$ and magnitude $\asymp_R gY^\beta/(rG)$. With the same positive macroscopic test, if $d_m\ge \eta g$ throughout that support for fixed $\eta>0$, its sign is instead $+\chi(N)$ with magnitude $\asymp_R Y^\beta/(rG)$. If $d_m\le-\eta g$ there, the sign is $-\chi(N)$ on the smaller $Y^\beta/(rG)$ scale. These are conditional statements on the unsigned contribution, not on the signed pole, the full exceptional difference, or a full mixed correlation.

## 2. Removing the two large primes from the ordinary mask

The primitive norms, tails, and $j$-weight moment of Section 1 of the shifted proof apply to (3) for either mask. They use only the ordinary reciprocal Möbius primitive and its positive Euler ratio. At fixed $j$ prime to $Rr$, extending the mask from $Rj$ to $Rrj$ acts by convolution with the positive shift measure corresponding to

$$
             \prod_{v=p,q}
                 (1-\alpha_v^\circ e^{-z\log v})^{-1}.           \tag{5}
$$

These are the extra prime deletions; the convolution identity follows at finite logarithmic cutoffs by local series expansion. The zero shift has mass $1$ and the other shifts have total mass $O(p^{-1}+q^{-1})$. By Minkowski, both $L^1,L^2$ norms of $R_{Rr,j}-R_{R,j}$ are $\ll_R (p^{-1}+q^{-1})A(j)$, with $A$ the positive ratio moment in (6) of the shifted proof. The $L^1$ and uniform bounds for the difference of the corresponding correlations follow by expanding that difference into two products and applying the $L^1$ convolution bound or $L^2$ Cauchy--Schwarz, respectively. Both are $\ll_R (p^{-1}+q^{-1})A(j)^2$. These estimates are summable against $\alpha^\circ(j)^2$ by (7) of the shifted proof.

The $j$ terms of $C_R$ divisible by $p$ or $q$ do not occur in $C_{Rr}$. Their $L^1$ and uniform norms cost $O_R(p^{-2}+q^{-2})$ by the same Euler majorant: one occupied prime supplies $(\alpha_v^\circ)^2 A(v)^2=O(v^{-2})$. In particular there is no repetition of (5) on a prime already deleted by $j$. Hence

$$
       \|C_{Rr}-C_R\|_1+\|C_{Rr}-C_R\|_\infty
                                        \ll_R p^{-1}+q^{-1}.     \tag{6}
$$

Evenness and continuity follow by $L^2$ translation and uniform summability. Positivity at zero follows from (11) of the shifted proof with mask $R$: all Euler factors are strictly positive with a uniform product lower bound, since $\alpha_v^\circ<1/2$ and the local correction is $O(v^{-2})$. The nonnegative Fourier transform is in $L^1$. The primitive $R_{R,1}$ equals $1$ on $0\le u<\log 2$, so its transform is nonzero in $L^2$ by Plancherel. Fourier inversion at $0$ gives $C_R(0)>0$. Finally $M_R>0$ follows by evaluating that transform at frequency zero: the ordinary primitive has integral $1$ before the positive Euler ratios and all their masses are positive, while the indicated Euler product is positive. This is the same ordinary Euler mass as in Section 3 of the shifted proof. These facts do not assert that $C_R(t)$ is nonnegative for all $t$.

## 3. Compute the true paired endpoints

By the classical conductor growth in the [all-scale exceptional reduction](r87-spectral-all-scale-exceptional-left-reduction.md), the actual Page conductor satisfies $r>G^J$ eventually for every fixed $J$. Since $p\le G^{c_+}$, so does $q$. Every shift involving $\pm\log q$, even after adding $\pm\log p$, has distance $\gg g$ beyond the physical wall. At fixed $R$ and two conductor primes, the moment $H$ of the interior shift proof is $O_R(1)$. Its tail estimate (6), which itself requires no wall gap, bounds the integrated tails and point evaluations at these far shifts by $O_R(e^{-c_1\sqrt g})$, also after multiplying by $T_m\ll g$ and reducing $c_1$.

Here the genuine $T_m=2Bg+O(1)$. For a translate $a$ write the paired physical bracket for $C=C_{Rr}$ as

$$
 K_m(a)=\int_{a-T_m}^{a+T_m} C(t)\,dt
                -\frac{T_m}{2}\big(C(a-T_m)+C(a+T_m)\big).       \tag{7}
$$

The bracket in the shifted proof equals the sum of $K_m(a)$ against the actual finite conductor shift coefficients, as in (5) of the interior shift proof. In particular $K_m(-a)=K_m(a)$. Discarding only the far $q$ translates with the error above leaves

$$
                       K_m(0)-2\kappa_p K_m(\log p)
                            +O_R(e^{-c_1\sqrt g}),                \tag{8}
$$

with $\kappa_p=(p-1)/(p-2)$. The unshifted $K_m(0)$ equals $M_{Rr}+O_R(e^{-c_2\sqrt g})$ by the same tail. The upper endpoint $\log p+T_m\gg g$, whereas the lower endpoint in $K_m(\log p)$ is exactly $-d_m$. Therefore

$$
 K_m(\log p)
       =\int_{-d_m}^\infty C_{Rr}(t)\,dt
                    -\frac{T_m}{2}C_{Rr}(d_m)
                               +O_R(e^{-c_2\sqrt g}).             \tag{9}
$$

In (8)–(9) replace $C_{Rr}$ by $C_R$ and $\kappa_p$ by $1$ at cost $O_R((1+g)(p^{-1}+q^{-1}))$ by (6) and the fixed norms. This is absorbed in $O_R(e^{-c_2'\sqrt g})$ since $p\ge G^{c_-}$. Evenness gives $M_R-2\int_{-d_m}^\infty C_R=-2\int_0^{d_m}C_R$, also for $d_m<0$. Consequently the actual finite ordinary bracket is

$$
             T_m C_R(d_m)-2\int_0^{d_m}C_R(t)\,dt
                              +O_R(e^{-c_2'\sqrt g}).             \tag{10}
$$

The term $T_m C_R(d_m)$ is the retained near endpoint after the two shifted coefficients $-\kappa_p$; it is absent from the whole-line replacement.

## 4. Restore the finite arithmetic and the exterior sign

The shifted proof multiplies (10) by $\mathcal V_{N,r}$ and integrates against $F(m)/L_m$. Its unshifted normalization is $\mathcal V_{N,r}M_{Rr}=(r/\varphi(r))\Sigma(Nr)$, where $Nr$ only labels the local Euler identity. With the exterior $C_r^{[2]}/\varphi(r)$, this equals $\Sigma(N)/r$ by the primewise cancellation of [the separated unsigned formula](r109-spectral-pointwise-separated-unsigned-parity.md). Thus the true coefficient before the bracket is $-\chi(N)\Sigma(N)/(rM_{Rr})$. By (6), $M_{Rr}=M_R+O_R(p^{-1}+q^{-1})$, and $M_R>0$. The bracket is $O_R(g)$, so replacing $M_{Rr}$ by $M_R$ is within the declared error. The integral has absolute mass $O(Y^\beta/G)$ and the even-target singular series is fixed at this radical.

For clarity the wall computation uses the completed algebraic short kernel only as an intermediate step. The true endpoint reduction has error $O(Y^\beta e^{-c_3\sqrt G}/r)$ after its exterior $C_r^{[2]}/\varphi(r)\le1/r$. The original $t$-cap approximation in the [short-log formula](r107-spectral-odd-disjoint-short-log-kernels.md) costs $O(Y^\beta G^C e^{CH}(Q_0/r)^{-1/4}/r)$ with $H=O_R(1)$. Because $\log(Q_0/r)\ge g^3$, both are smaller than $Y^\beta e^{-c\sqrt g}/(rG)$ for suitably reduced $c$. This proves (4) for the original finite $\mathcal P_1$. The distinct raw two-positive error would also be smaller under this margin, but its signed pole is not estimated here.

Since $C_R(0)>0$ and $C_R$ is continuous, choose $d_R>0$ with $C_R(d)\gg_R1$ for $|d|\le d_R$. The integral in (10) is $O_R(1)$ whereas the first term is $\asymp_R g>0$. In the regimes $d_m\ge\eta g$ and $d_m\le-\eta g$, the same tails in (10) make the bracket equal to $-M_R+O_R(e^{-c_\eta\sqrt g})$ and $+M_R+O_R(e^{-c_\eta\sqrt g})$, respectively. Applying the nonnegative test with $\int|F|/L_m\asymp Y^\beta/G$ proves the stated signs and scales. They compare conditional regimes only; they do not assert one can vary an actual Page conductor through the wall.
