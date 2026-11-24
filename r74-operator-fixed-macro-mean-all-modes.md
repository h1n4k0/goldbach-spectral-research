# All-modulus-frequency mean-square deletion inside the true parent means

**Scope.** A signed modulus first moment and positivity give a full Hilbert–Schmidt mean-square deletion on the genuine remaining parent-mean matrix, not another restriction on modulus frequencies. The original low-dimensional parent space can be reduced further to one fixed weighted direction per larger group of parents, with all mixed matrix crossings controlled and the exact benchmark retained. The whole covariance on those larger mean directions remains open. The result is an ordinary-modulus average, not a prescribed-modulus or arbitrary-subset estimate.

## Statement

Use the genuine transported parent directions of [R70](r70-operator-adaptive-parent-contrast-rank.md) and the unmasked and body profiles $h,f$ of [R71](r71-operator-parent-terminal-layer.md). The reference dyads in $[H,M]$, $4\le H<M\le Q^\Gamma$ with $0<\Gamma<1$ fixed, have lower endpoints $V$. Within a $V$-dyad use the disjoint true parent partition $I$, with lengths at most $W_V$, and denote its number of parents by $d_V$ and the total dimension by $d=\sum_V d_V$. Take an ordinary interval $\mathcal I\subset[Q,2Q]$ containing $J\ge1$ even moduli. Assume the manuscript's original local GRH at each such $N$, and auxiliary Dirichlet GRH for $q\le\lceil8M\rceil+2$, including $1$, as in [R72](r72-operator-principal-modulus-low-modes.md). No separate auxiliary range of R70 or R71 is needed for the estimate **on this already defined parent index space**.

Fix $0<\delta\le1/10$, with $W_V\le\delta V/10$ in every dyad. Group consecutive parents into larger blocks $\mathcal J$ within each dyad, of total span at most $\delta V$. These can be chosen with $O(1+\delta^{-1})$ blocks per dyad by packing consecutive parents up to the span bound. Across each block retain the normalized vector of components

$$
\left(\sqrt{\int_I w_Q(z)\,dz}\right)_{I\subset\mathcal J},
       \qquad
       w_t(z)=z^{-3}\big((Qz)^{-2/\log t}+(Qz)^{-1/4}\big).
 \tag{1}
$$

Write $\Pi$ for the corresponding orthogonal projection on the common parent index space, $R=1-\Pi$, and $L=\log(3Q)$. Both projections are fixed in $N$; the underlying actual basis vectors are the normalized true physical means on $I_N=(Q/N)I$.

In the notation of R72 let $T_N^{u,v}$, $u,v\in\{h,f\}$, be the actual all-alias parent matrix on this index space, allowing either family on either leg. All signs, units and continuous corrections are unchanged. Fix $0<\kappa<1/3$, and set, with a sufficiently large constant $C_\kappa$,

$$
\begin{split}
 E_\kappa&=H^{-\kappa}\exp(C_\kappa L^\kappa)
                       +Q^{-1/2}H^{-1/2}L^3,\qquad
 \tau=L\delta\big(L+\log(2/\delta)\big),\\
 \mathcal B_{\rm tr}&=Q^\epsilon\sum_V
           \big(\sqrt{W_V/V}+\sqrt{d_V}\,W_V/V\big),\\
 \mathcal B_{\rm HS}&=Q^\epsilon\sum_V
           \big(\sqrt{W_V/V}+W_V/\sqrt{VH}\big).
 \end{split}
 \tag{2}
$$

If neither profile is $f$ put $\iota=0$, otherwise put $\iota=1$. Then

$$
\begin{split}
 &\left(\frac1J\sum_{\substack{N\in\mathcal I\\2\mid N}}
       \|T_N^{u,v}-\Pi T_N^{u,v}\Pi\|_{\rm HS}^2\right)^{1/2}\\
 &\qquad\ll_{\Gamma,\kappa,\epsilon,\Theta}
       L^{5/2}
       \left[\tau+\sqrt d\left(E_\kappa+
                  Q^\epsilon\frac{\sqrt{QM}}J\right)
                 +\iota\mathcal B_{\rm tr}\right]^{1/2}
                 +E_\kappa+\iota\mathcal B_{\rm HS}.
 \end{split}
 \tag{3}
$$

The constant is independent of the body cutoff for the unmasked $h,h$ case.

For the actual R70 parameters

$$
H=Q^{2/5},\quad M=Q^{3/5},\quad
 W_V=Q^{23/175}V^{4/7},\quad d\ll Q^{22/175},
$$

take $\kappa=1/4$, $J\gg Q^{9/10}$, and $\delta=Q^{-1/30}$. Then the RMS in (3) is $O_\epsilon(Q^{-1/60+\epsilon})$ for $h,h$ and $O_\epsilon(Q^{-1/100+\epsilon})$ if a body profile is present. The retained rank is $O(LQ^{1/30})$. Alternatively, for every fixed $K>0$, with $\delta=L^{-2K-10}$ at the same spatial parameters and modulus range, the RMS in (3) is $O_K(L^{-K-1})$ and the retained rank is $O(L^{2K+11})$. These are estimates for a full deletion in the existing actual matrix, not for the smaller retained block itself.

In particular on a complete shell, or on any ordinary interval indexed by its consecutive even moduli, write $\widehat T^{u,v}(j)$ for the discrete modulus Fourier transform normalized as in R72 (2). Since $\Pi$ is fixed, the square of the left side in (3) is exactly

$$
\sum_{j\bmod J}
                    \|\widehat T^{u,v}(j)
                         -\Pi\widehat T^{u,v}(j)\Pi\|_{\rm HS}^2.
 \tag{4}
$$

There is no collar restriction on this sum.

## 1. Stationary benchmark and the fixed macro projection

Write $T_N^{u,v}=P_N^{u,v}-B_N^{u,v}$, with the exact positive-Gram factorization of the prime part, and $B=D+K$ the equality atoms plus signed continuous model, as in R71 §3. For $h,h$ these are the genuine compressions of the full physical operators to the transported literal mean basis. In logarithmic physical coordinate $x=\log u$ use the unitary change of measure with factor $\sqrt u$. The benchmark theorem [post-R15](operator-post-r15-stationary-tail.md) gives

$$
\|B_N^{h,h}-S_N\|_{\rm HS}\ll_\kappa E_\kappa,
 \tag{5}
$$

where $S_N$ is the compression to this exact basis of the stationary comparison $M_{m_N} C_N M_{m_N}$ on the log annulus. Here $m_N(x)=((Ne^x)^{-2/\log N}+(Ne^x)^{-1/4})^{1/2}$ is the actual physical Hardy damping in post-R15, not the reference density $w_t(z)$ in (1). It is bounded on the log annulus, whose length is $O(L)$. The convolution kernel of $C_N$ is

$$
\int_{\mathbb R}e^{i\xi(x-y)} a_N(\xi)\,d\xi,\qquad
        0\le a_N(\xi)\ll \frac{L+\log(2+|\xi|)}{1+\xi^2}
$$

for sufficiently large $Q$, by that theorem. In particular $S_N$ is positive and $\|S_N\|_{\rm op}\ll L$. For (5) the bottom of the physical annulus is at least $H/2$, so use $h=\log(H/2)$ in the post-R15 comparison. Its diagonal error and shifted-contour error are within $E_\kappa$.

For each $N$ there is a moving comparison projection $\Pi_N$, defined on the same parent index space by the normalized components $\|r_N\mathbf1_{I_N}\|_2$ on each block $\mathcal J$, where $r_N$ is the exact physical mean weight. Its image is the true normalized mean on the union of the block's physical parents. In fact if $p=N/Q$, then $\|r_N\mathbf1_{I_N}\|_2=p\sqrt{\int_I w_N(z)\,dz}$ with the reference density of (1). On a block of span $\delta V$, $\log(w_N(z)/w_Q(z))$ changes by $O(\delta)$: each logarithmic derivative of $w_t$ in $z$ is $O(1/z)$ uniformly there. Taking ratios of the integrals over each $I$ shows that the reference and moving vectors differ, before normalization, by one common scalar and $1+O(\delta)$ componentwise factors. After normalization their Euclidean difference is $O(\delta)$. Direct sums of the rank-one blocks therefore give

$$
\|\Pi_N-\Pi\|_{\rm op}\ll \delta .
 \tag{6}
$$

Let $\alpha_N(\xi)$ be the coefficient vector of the log function $x\mapsto m_N(x)e^{i\xi x}$ against the actual orthonormal parent means; restrict that function to the log annulus. Then
$S_N=\int a_N(\xi)\alpha_N(\xi)\alpha_N(\xi)^*d\xi$.
The physical mean direction on a log block is proportional to $\rho_N(x)=e^{-x}m_N(x)$. If $x_0$ is its left endpoint, subtracting $e^{(1+i\xi)x_0}\rho_N(x)$ leaves the pointwise factor $1-e^{-(1+i\xi)(x-x_0)}$ in $m_N(x)e^{i\xi x}$. The log block spans at most $\delta$, since the physical dilation $Q/N$ cancels in the length ratio. Hence

$$
\|(1-\Pi_N)\alpha_N(\xi)\|_2^2
                 \ll \min(1,\delta^2(1+\xi^2)) L.
$$

This follows by projection onto the true weighted-zero complement in the entire block first, then compressing to the subset of literal parent directions. Equation (6) and $\|\alpha_N(\xi)\|_2^2\ll L$ give the same bound with $R$, since $\delta^2\le\min(1,\delta^2(1+\xi^2))$. Integrate the positive Fourier factor, splitting at $|\xi|=1/\delta$, to obtain

$$
\operatorname{tr}(R S_N R)\ll \tau,\qquad
              \|S_N R\|_{\rm HS}^2\ll L\tau.
 \tag{7}
$$

The second follows from positivity and $\|S_N\|_{\rm op}\ll L$. In the trace estimate, $\int a_N(\xi)\min(1,\delta^2(1+\xi^2))\,d\xi\ll \delta(L+\log(2/\delta))$ by elementary integration. Thus no factor $\sqrt d$ multiplies this principal deterministic trace.

## 2. Exact body masks in the benchmark

This section uses only the deterministic estimates in R71 §3, not its selected-moduli arithmetic theorem. Write $g=h-f$ for the actual terminal profile. The difference between $B_N^{h,h}$ and any $B_N^{u,v}$, $u,v\in\{h,f\}$, is a sum of at most two exact terms with one terminal leg. For a $V$-terminal leg and an arbitrary other family, the equality Gram has full mixed HS norm $O(L^{O(1)}\sqrt{W_V/V})$, by the terminal equality trace $O(L^2 W_V/V)$ and the HS ideal inequality against the other full equality Gram. For the signed model, R71 (12) gives $O_\epsilon(Q^\epsilon W_V/\sqrt{VU})$ on the $V,U$ block. This estimate uses the cancellation of the three continuum signs at constant density and retains the actual singular series. Summing $U$ gives

$$
\|B_N^{u,v}-B_N^{h,h}\|_{\rm HS}
                             \ll_{\Gamma,\epsilon,\Theta}\mathcal B_{\rm HS}
 \tag{8}
$$

whenever at least one profile is $f$, using the geometric dyad sum $\sum_U U^{-1/2}\ll H^{-1/2}$.

A better bound for the trace against $R$ follows because $R$ is block-diagonal by dyad. Only same-dyad blocks contribute. For an equality term, factor $D^{g,v}=Y_g^*Y_v$ on the actual raw atom space, with mark $\Lambda(n)^2$ and unit mask. Cauchy on the HS pair $Y_gR_V,Y_vR_V$ gives

$$
|\operatorname{tr}(R_V D^{g,v}_{N;V,V}R_V)|
 \le \sqrt{\operatorname{tr}(D^{g,g}_{N;V,V})\,
                 \operatorname{tr}(D^{v,v}_{N;V,V})}
                \ll L^2\sqrt{W_V/V},
$$

where $R_V$ is the restriction of $R$ to dyad $V$, and the second trace is $O(L^2)$ by the ordinary envelope and the raw length. For the continuous term use the same-dyad bound $O_\epsilon(Q^\epsilon W_V/V)$ in HS and $\|R_V\|_{\rm HS}\le\sqrt{d_V}$. Thus for either self-family with a body profile,

$$
|\operatorname{tr}(R(B_N^{f,f}-B_N^{h,h})R)|
                             \ll_{\Gamma,\epsilon,\Theta}\mathcal B_{\rm tr}.
 \tag{9}
$$

This trace saving uses the actual same-dyad dimensions rather than the total dimension in a mixed raw error.

## 3. Signed first moment and positive mean square

For each self-family $u\in\{h,f\}$, $P_N^{u,u}$ is positive. Its trace and operator norm are $O_\Gamma(L^5)$ by R71 §3: for an odd character the prime sum against a single normalized profile on dyad $V$ is $O(L^2\sqrt{QV}\,b_I)$ by local GRH and Abel, with $b_I=\sqrt{|I|}/(\sqrt Q V)$; the squared sum of these bounds is $O(L^4)$ per dyad. Sum the logarithmically many dyads and use the true odd-character Gram normalization. Only the local assumption is used in this bound.

As $R$ is fixed, R72 (1) directly gives

$$
\left|\frac1J\sum_{N\in\mathcal I,\,2\mid N}
             \operatorname{tr}(R T_N^{u,u} R)\right|
    \le\sqrt d\left\|\frac1J\sum_{N\in\mathcal I,\,2\mid N}
                                      T_N^{u,u}\right\|_{\rm HS}
    \ll_\epsilon \sqrt d\,Q^\epsilon\frac{\sqrt{QM}}J .
 \tag{10}
$$

This is precisely where the ordinary **signed** mean is used, not a bound on any sample's norm. On every modulus,
$\operatorname{tr}(R B_N^{u,u}R)$ is at most the positive trace in (7), the stationary-error trace $O(\sqrt d E_\kappa)$ by (5), and for $u=f$ the additional (9). Since $P_N^{u,u}=T_N^{u,u}+B_N^{u,u}$, (10) implies

$$
\frac1J\sum_{N\in\mathcal I,\,2\mid N}
                     \operatorname{tr}(R P_N^{u,u}R)
      \ll \tau+\sqrt d(E_\kappa+Q^\epsilon\sqrt{QM}/J)
                               +\mathbf1_{u=f}\mathcal B_{\rm tr}.
 \tag{11}
$$

The left side is nonnegative. In particular the mean of this positive tail mass is small even without any individual bound or cancellation on the retained principal block.

For a mixed prime matrix $P_N^{u,v}=X_u^*X_v$, use
$\|P_N^{u,v}R\|_{\rm HS}^2\le\|P_N^{u,u}\|_{\rm op}\operatorname{tr}(R P_N^{v,v}R)$.
The adjoint handles the opposite leg. Equations (7)–(8) and (5) likewise give the pointwise HS bound $O(\sqrt{L\tau}+E_\kappa+\iota\mathcal B_{\rm HS})$ for either benchmark crossing. The exact decomposition

$$
T_N^{u,v}-\Pi T_N^{u,v}\Pi
                     =T_N^{u,v}R+R T_N^{u,v}\Pi
$$

then gives (3) by taking the square means of these estimates. This proves the full mixed deletion, with positive arguments applied to the Gram, not to the signed original matrix. Equation (4) is finite Fourier Parseval in the fixed index basis.

## 4. Explicit rates and limits

At the specified R70 parameters $W_V/V\le Q^{-1/25}$, $d_V\ll 1+V/W_V$ by its parent construction, and $W_V/\sqrt{VH}\le Q^{-9/350}$. Hence both mask errors in (2) are $O_\epsilon(Q^{-1/50+\epsilon})$. With $\kappa=1/4$, $E_\kappa=O_\epsilon(Q^{-1/10+\epsilon})$. At $J\gg Q^{9/10}$, the R72 mean factor is also $O_\epsilon(Q^{-1/10+\epsilon})$; multiplication by $\sqrt d$ makes both $O_\epsilon(Q^{-13/350+\epsilon})$. For $\delta=Q^{-1/30}$ the trace term is $O(L^2Q^{-1/30})$; this proves the two claimed power savings. For $\delta=L^{-2K-10}$ every power-saving term is smaller than the chosen log scale, and $L^{5/2}\sqrt{\tau}=O_K(L^{-K-3/2})$; this suffices for the stated inverse-log bound. The rank count follows from $O(1+\delta^{-1})$ blocks per dyad and $O(L)$ dyads.

The retained directions in (1) are true linear combinations of the parent means, not independent or random model vectors. In particular the result covers all modulus Fourier frequencies of the removed and mixed spatial parts, including frequencies outside the [R73](r73-operator-rational-modulus-collars.md) rational collars. It does not show smallness of the full variance of $\Pi T_N^{u,v}\Pi$, nor change the local/auxiliary hypotheses for the earlier reductions outside this parent space.
