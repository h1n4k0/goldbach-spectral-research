# Full signed modulus means and a low-frequency variance of the actual parent covariance

**Scope.** This treats the principal all-alias matrix of the remaining literal parent means, including the square-root lower-profile mixture of [R71](r71-operator-parent-terminal-layer.md). A double residue-error integration gives a signed first moment on every ordinary interval of even moduli, beyond the radius of the earlier one-error argument. On the complete even shell it also controls the contribution of a growing set of low discrete modulus Fourier modes to the actual Hilbert–Schmidt mean square. It does not control the remaining high modes, an arbitrary selected family, or an individual modulus.

## Statement

Use the reference dyads and physical parent mean directions of [R70](r70-operator-adaptive-parent-contrast-rank.md) and R71, with $4\le H<M\le Q^\Gamma$, $0<\Gamma<1$ fixed. Write $L=\log(3Q)$. The $V$-dyad consists of disjoint intervals $I$ of lengths at most $W_V$, $1\le W_V\le V/20$, each transported to $I_N=(Q/N)I$. The profile $h_{I,N}$ is the exact normalized true weighted mean; $f_{I,N}$ is its exact lower-profile mask in R71 (14), and $g_{I,N}=h_{I,N}-f_{I,N}$ its terminal profile. Pick one family from $h,f,g$ on each of the two legs, not necessarily the same choice. Let $T_N^{u,v}$ denote the resulting signed finite matrix on the common parent index space. Thus its every entry has the actual unit-restricted prime-power sum minus the matched continuous singular-series model, with all positive aliases $s=kN$, the two positive difference orientations, the negative sum orientation, and no equality line. In particular $T_N^{h,h}$ is the whole original literal parent compression, not an approximate scalar test, and $T_N^{f,f}$ is the full all-alias sharp-prefix mixture.

Assume the original local GRH at every even modulus used in an estimate, and auxiliary Dirichlet GRH through $\lceil8M\rceil+2$, including $q=1$. No other auxiliary moduli from R70 or R71 are needed for this theorem. For every ordinary interval $\mathcal I\subset[Q,2Q]$, with $J=\#(\mathcal I\cap2\mathbb Z)\ge1$, one has

$$
\left\|\frac1J\sum_{\substack{N\in\mathcal I\\2\mid N}}T_N^{u,v}\right\|_{\rm HS}
       \ll_{\Gamma,\epsilon,\Theta} Q^\epsilon\frac{\sqrt{QM}}J.
 \tag{1}
$$

The constant for the unmasked $h,h$ choice is independent of $\Theta$. On the complete shell of even moduli, $J\asymp Q$, this is $O_\epsilon(Q^\epsilon\sqrt{M/Q})$, in particular $O_\epsilon(Q^{-1/5+\epsilon})$ for $M=Q^{3/5}$. This goes beyond the condition $M_1M_2<Q$ for a saving from [R63](r63-operator-signed-window-mean-modulus-average.md), and still estimates only a signed first moment when used alone.

More precisely on the entire even shell let $N=2m$, indexed by the $J$ consecutive integers $m_0,\ldots,m_0+J-1$, and set

$$
\widehat T(j)
       =\frac1J\sum_m e\big(-j(m-m_0)/J\big)T_{2m}^{u,v},
        \qquad e(z)=\exp(2\pi iz).
 \tag{2}
$$

For any integer $R\ge0$ with $R\le \sqrt{Q/M}$ and $2R<J$, the Hilbert–Schmidt RMS of the orthogonal projection onto the modes $|j|\le R$ of the **unweighted original field** $m\mapsto T_{2m}^{u,v}$ satisfies

$$
\left(\sum_{|j|\le R}\|\widehat T(j)\|_{\rm HS}^2\right)^{1/2}
       \ll_{\Gamma,\epsilon,\Theta}
           Q^\epsilon\sqrt{M/Q}\,(1+R)^{3/2}.
 \tag{3}
$$

For $M=Q^{3/5}$, $R=\lfloor Q^{3/25}\rfloor$ this is $O_\epsilon(Q^{-1/50+\epsilon})$. The projection is in the **modulus variable**, not a restriction of alias indices or raw pair geometry. Its orthogonality is the finite Fourier orthogonality of the complete ordinary shell.

## 1. Exact fixed supports and parameter envelopes

Fix a dyad pair $V\le U$, without loss of generality by transposition, and one pair $I,I'$ of reference parents on it. Write $b_I=\sqrt{|I|}/(\sqrt Q V)$, $b_{I'}=\sqrt{|I'|}/(\sqrt Q U)$. For real $t\in[Q,2Q]$ use the exact profile $h_{I,t}$ of R71 (1) with raw support in $[0,2QV]$, and its fixed masks in R71 (2) when using $f,g$. A profile is zero at zero. For $0\le j\le2$ the actual weights $u_{I,t}$ satisfy

$$
\sup_x |Q^j\partial_t^j u_{I,t}(x)|\ll_{\Gamma,\Theta} b_I,\qquad
 |Q^j\partial_t^j\partial_x u_{I,t}(x)|\le G_I(x)\ \text{a.e.},\qquad
 \int_{\mathbb R}G_I(x)\,dx\ll_{\Gamma,\Theta} b_I .
 \tag{4}
$$

Here $G_I$ is fixed in $t$. For $h$ this follows by differentiating the actual integrand $w_t(z)=z^{-3}((Qz)^{-2/\log t}+(Qz)^{-1/4})$ and the mean normalizer: the first two normalized $t$-derivatives of $w_t$ are $O_\Gamma(w_t)$ in the polynomial range. The $x$-derivative uses the square-root derivative, bounded by $O_\Gamma(b_I/\sqrt{QVx})$ for $0<x\le 2QV$, and the terminal derivative bounded by $O_\Gamma(b_I/(Q|I|))$ on $QI$. Both have $L^1$ norm $O_\Gamma(b_I)$, including clipped windows. For the fixed masks defining $f,g$, the extra derivative has size $O_\Theta(b_I/(QW_V))$ on their transition interval of length $QW_V$. Thus (4) holds for either masked or unmasked weights with the exact transported normalization and body/terminal split. Also,

$$
\sum_{I\subset[V,2V]} b_I^2\ll (QV)^{-1}.
 \tag{5}
$$

We will use the crude **pointwise** bound $\|T_N^{u,v}\|_{\rm HS}\ll_{\Gamma,\epsilon,\Theta}Q^\epsilon$, which is only for controlling modulus boundary strips. The exact odd-character Gram on each raw family has trace $O(L^{O(1)})$ by partial summation against the local GRH character prime-sum bounds and (4), (5), as in R71 §3. The equality Gram has the same bound from the raw profile suprema and $\Lambda(n)^2\ll L^2$; mixed versions follow by Gram factorization. For the exact continuous model use the signed cancellation at constant density in [R68](r68-operator-residue-orbit-and-alias-slope-covariance.md) (8)–(10). In a pair of entries the sup plus variation of each continuum line profile is $O(QV b_I b_{I'})$ by convolution with the shorter raw support. Thus this signed model is $O_\epsilon(Q^\epsilon\sqrt{V/U})$ in a dyad-pair HS norm. Sum over dyads for the stated pointwise bound. The sign cancellation is used for this crude estimate; we do not assume smallness of any unweighted signed arithmetic response.

## 2. Twice-centered divisor switching with a smooth modulus test

Let $\omega$ be any complex $C_c^2$ weight on $(Q,2Q)$. Write

$$
K_1=\|\omega\|_\infty+\|\omega'\|_{L^1(\mathbb R)},\qquad
        K_2=\|\omega''\|_{L^1(\mathbb R)}.
$$

Assume local GRH at the even moduli in its support. We prove the weighted matrix estimate

$$
\left\|\sum_{\substack{Q\le N\le2Q\\2\mid N}}
             \omega(N)T_N^{u,v}\right\|_{\rm HS}
     \ll_{\Gamma,\epsilon,\Theta}
          Q^\epsilon\left[\sqrt{QM}\,K_1+QM\,K_2\right].
 \tag{6}
$$

For one orientation $(\sigma_1,\sigma_2)=(+,-),(-,+),(+,+)$, fix $k\ge1$ and set $t=(\sigma_1x+\sigma_2 y)/k,\ q=2k$. Only $k\le4U$ can occur, by the fixed raw supports. The exact even-modulus switch gives the congruence $y\equiv-\sigma_1\sigma_2 x\bmod q$ on the arithmetic points, with weight

$$
\mathcal H(x,y)
          =\omega(t) u_{I,t}(x)v_{I',t}(y).
 \tag{7}
$$

The weight is zero when $t$ is outside the support, so its extension by zero there has no boundary derivative. In particular no sharp tilted boundary is being integrated by parts. At an allowed arithmetic point $t=N$ exactly, and the continuum uses the same weights.

Temporarily drop the original $N$-unit conditions: for each fixed $N$, the exceptional prime powers on a raw leg have total marks $O(L^2)$, and each has $O(U)$ possible partners across all positive $k$, using $N\ge Q$. Including all $N$ this costs $O_\epsilon(Q^\epsilon QU b_I b_{I'}K_1)$ in an entry. Now, in the switch, drop the $q$-nonunits: both residues are then nonunits, and the exceptional prime powers on the $x$-leg have total marks $O(L^2)$ and $O(QU/q+1)$ partners per $k$. Summing $k$ restores this error within the same entrywise bound. These steps do not drop any admissible proper powers from the actual final expression.

On units write $\Psi_r(z)=\psi(z;q,r)=z/\phi(q)+F_r(z)$, with $F_r=0$ on nonunits. The weighted switched atom sum is exactly

$$
\sum_{r\bmod q}^{*}\iint\mathcal H(x,y)
                   \,d\Psi_r(x)\,d\Psi_{-\sigma_1\sigma_2 r}(y).
$$

Expand both measures. The double principal term is $\phi(q)^{-1}\iint\mathcal H(x,y)dx\,dy$. In each single-error term the residue sum is $F_{\rm tot}(z)=\sum_r F_r(z)=\psi(z)-z$ minus the total nonunit marks at $q$. By RH (part of the auxiliary hypothesis) its sup norm on $z\le 2QV$ or $2QU$ is $O_\Gamma(L^2\sqrt{QV})$ or $O_\Gamma(L^2\sqrt{QU})$, respectively. The bounded variation estimates (4) and the $t$-change at fixed $x$ or $y$ imply

$$
\iint|\partial_y\mathcal H(x,y)|dx\,dy
       \ll_{\Gamma,\Theta} QV b_I b_{I'}K_1,
 \qquad
 \iint|\partial_x\mathcal H(x,y)|dx\,dy
       \ll_{\Gamma,\Theta} QU b_I b_{I'}K_1 .
 \tag{8}
$$

For example the $y$-derivative on the profile at fixed $t$ uses $\int G_{I'}$, and the parameter derivative uses $\int (|\omega'(t)|+|\omega(t)|/Q)dt$ since $dy=k\,dt$ in absolute value. The $x$-leg then has length $O(QV)$. Partial integration gives single-error costs per $k$ of

$$
O_{\Gamma,\Theta}\big(L^2 b_I b_{I'} K_1
           (QV\sqrt{QU}+QU\sqrt{QV})/\phi(2k)\big).
 \tag{9}
$$

For the double error we use **two** residue-vector GRH bounds after partial integration on both legs:

$$
\sum_r^{*}\iint F_r(x)F_{-\sigma_1\sigma_2 r}(y)
                  \partial_{xy}^2\mathcal H(x,y)\,dx\,dy .
$$

Character Parseval gives $\|\mathbf F(x)\|_2\ll_\Gamma L^2\sqrt{QV}$ on the first support and $\|\mathbf F(y)\|_2\ll_\Gamma L^2\sqrt{QU}$ on the other, as in R63 (4). To estimate the mixed derivative of (7), differentiate at fixed $t$ on the two raw legs or apply $\sigma_i\partial_t/k$ on leg $i$. When both derivatives are at fixed $t$, use $G_I G_{I'}\|\omega\|_\infty$. When just one is a parameter derivative, integrate along its affine variable and use $\int(|\omega'|+|\omega|/Q)\ll K_1$, as in (8). When both are parameter derivatives, use

$$
\frac{b_I b_{I'}}{k^2}
       \big(|\omega''(t)|+C|\omega'(t)|/Q+C|\omega(t)|/Q^2\big)
$$

and integrate over $y$ for fixed $x$, giving one factor $k$; the remaining $x$-support has length $O(QV)$. Consequently

$$
\iint|\partial_{xy}^2\mathcal H|dx\,dy
       \ll_{\Gamma,\Theta}
            b_I b_{I'}\big[K_1+(QV/k)(K_2+K_1/Q)\big].
 \tag{10}
$$

There are no endpoint terms at zero where the actual weight is continuous and vanishes, or at infinity by compact support. All the derivatives in (8)–(10) are integrable by (4); the integration by parts also follows by smooth approximation of the fixed absolutely continuous profiles. It handles the square-root origin and the actual terminal derivative of the literal mean. By Cauchy in residues, multiply (10) by $O(Q\sqrt{VU}L^4)$ for the double-error cost. This avoids the absolute one-leg prime error summed against the other unswitched prime marks.

## 3. The original singular-series benchmark and HS aggregation

Let
$I_k(t)=\int u_{I,t}(x)v_{I',t}(\sigma_2(kt-\sigma_1x))dx$.
The double principal term just found is the exact

$$
\frac{k}{\phi(2k)}
                    \int \omega(t) I_k(t)\,dt .
 \tag{11}
$$

Here $dy=k\,dt$ in absolute value. The sup plus total variation of $\omega(t)I_k(t)$ is $O_{\Gamma,\Theta}(QV b_I b_{I'}K_1)$: for fixed $x$ use (4), the $\omega$ derivative, and the monotone affine argument of $v$ to integrate its spatial derivative in $t$. This uses the actual moving weight rather than freezing its normalization.

For even $N$, expand the true model $\mathfrak S(kN)$ by squarefree odd divisors $d\mid N$ prime to $k$, weighted by $\prod_{p\mid d}(p-2)^{-1}$ times $\mathfrak S(2k)$, exactly as in R63 §3. The average of $\omega I_k$ on the $2d$-lattice is its integral divided by $2d$, with error controlled by its sup and variation. The absolutely extended Euler coefficient is

$$
\frac{\mathfrak S(2k)}2\prod_{\substack{p>2\\p\nmid k}}
                   \left(1+\frac1{p(p-2)}\right)
                    = \frac{k}{\phi(2k)}.
$$

Since the divisor factors are $O_\epsilon(d^{-1+\epsilon})$, summing the $d\le2Q$ errors and extending the coefficient past $2Q$ gives $O_\epsilon(Q^\epsilon QV b_I b_{I'}K_1)$ per $k$, with the bound $\int|\omega I_k|\ll Q\|\omega I_k\|_\infty$ for the tail. Thus the original model subtracts (11) exactly up to that stated error, for each orientation separately, before recombining $+,+,-$.

Now sum $k\le4U$, using $\sum_k\phi(2k)^{-1}\ll_\epsilon Q^\epsilon$ and $\sum_{k\le4U}k^{-1}\ll L$. Take HS over the parent entries: (5) on both legs makes the common $b_I b_{I'}$ factor cost $O((Q\sqrt{VU})^{-1})$. In (9) this gives $O_\epsilon(Q^\epsilon\sqrt{QU}K_1)$. The double error from (10) gives $O_\epsilon(Q^\epsilon[U K_1+QV K_2])$. The total model-restoration error is $O_\epsilon(Q^\epsilon\sqrt{VU}K_1)$, and the original and auxiliary unit errors are smaller than $O_\epsilon(Q^\epsilon U K_1)$. Since $U\le M<Q$, sum the logarithmically many dyad pairs and combine the signs to prove (6).

## 4. Restoring ordinary shells and projecting their true Fourier field

Put $B=\sqrt{QM}$. For an interval $\mathcal I$ with length at least a sufficiently large multiple of $B$, choose a smooth $\omega$ that is one except in its two endpoint strips of lengths $O(B)$, supported in its interior, with $K_1\ll1,\ K_2\ll B^{-1}$. If an endpoint is the edge of $[Q,2Q]$, take the support strictly inside that edge. Equation (6) gives $O_\epsilon(Q^\epsilon\sqrt{QM})$ before dividing by $J$. The difference from the unsmoothed interval sum is bounded by $O_\epsilon(Q^\epsilon B)$ using the pointwise bound in §1 on its endpoint strips. For intervals of length $O(B)$, that same pointwise bound proves (1) directly. This proves the sharp ordinary signed interval statement.

For (2), on the full ordinary shell use the same smooth cutoff and multiply it by $e(-j(t/2-m_0)/J)$. Then

$$
K_1\ll 1+|j|,\qquad
       K_2\ll B^{-1}+(|j|+j^2)/Q
$$

because $J\asymp Q$. The boundary strips are restored with the same error $O_\epsilon(Q^\epsilon B)$ even for these frequency weights, which have modulus one. Divide (6) by $J$ to get

$$
\|\widehat T(j)\|_{\rm HS}
        \ll_{\Gamma,\epsilon,\Theta}
              Q^\epsilon\left[
                  \sqrt{M/Q}\,(1+|j|)
                      +(M/Q)(1+|j|)^2\right].
$$

For $|j|\le\sqrt{Q/M}$ the square term is absorbed. Finite Fourier Parseval for the complexified HS space on the complete field proves (3); $\sum_{|j|\le R}(1+|j|)^2\ll (1+R)^3$. Neither the smoothing step in the proof nor the final projection modifies any raw cut, alias list, or continuous correction in the field itself. The high modulus Fourier modes may still carry the full unresolved variance.
