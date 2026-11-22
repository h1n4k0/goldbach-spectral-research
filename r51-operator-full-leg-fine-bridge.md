# Full-leg fine-side deletion and the remaining coarse-tail bridge

**Scope.** The true Hardy operator may be projected away from the fine directions of the entire distant exterior even when the other leg crosses the origin or central range. This was not covered by the doubly exterior fine-side theorem. A pointwise bound for the deterministic separated crossing follows from the same signed calculation. The two surviving actual blocks are explicitly stated; they are not estimated here. No auxiliary Dirichlet GRH or modulus average is used for the new deletion or for the tail cutoff.

## Statement

Assume only the original local Dirichlet $\mathrm{GRH}(N)$ at a sufficiently large even $N$. Work in the genuine physical $L^2((0,\infty),du)$ realization. Put $L=\log N,\ \ell=\log L,\ \alpha=L^{-1},\ \beta=1/8$, and

$$
 r_N(u)=u^{-3/2}m_N(\log u),\qquad
 m_N(t)=\left((Ne^t)^{-2\alpha}+(Ne^t)^{-2\beta}\right)^{1/2}.
$$

Write $P_A=\mathbf 1_{0<u<A}$, $Q_A=\mathbf 1_{u\ge A}$, and $S(n)=\mathfrak S(n),\ S_N=S(N)$. Fix $K,\epsilon>0$, $0\le\vartheta<1$, and use exactly the published [R30](weak-s-exterior-fine.md) cell grid at $Y$, with

$$
 \log Y\ge (K+3)\ell^2/\log\ell,\quad
 V=2^jY,\quad
 d_V=\left\lfloor V^{1/2}(NV)^{\vartheta/L}L^{-K-2-\epsilon}\right\rfloor .
 \tag{1}
$$

The cells partition each $[V,2V)$ into length $d_V$ intervals and the one last shorter interval if needed. Let $\Pi$ project onto the sum of the lines $\mathbb C r_N\mathbf 1_I$ for these cells, and $E=Q_Y-\Pi$ be the high fine projection. Uniformly in $Y$ in (1),

$$
 \|T_NE\|_{\rm HS}+\|ET_N\|_{\rm HS}=o(L^{-K}).
 \tag{2}
$$

In particular the low leg can be **all** $0<u<Y$, not a microscopic raw prefix or another exterior leg. For any $1\le A\le B$, $B\ge2$, the deterministic crossing alone also satisfies

$$
 \|P_A(D_N+K_N)Q_B\|_{\rm HS}
 \ll \frac{A}{B}\log(2NA) + S_N\log(2B)\sqrt{A/B}.
 \tag{3}
$$

Here $D_N$ is the exact integer diagonal and $K_N$ the signed continuous Beta model in $T_N=P_N^{\rm arith}-D_N-K_N$; $P_N^{\rm arith}$ is the actual positive odd-character Gram, not the physical projection $P_A$.

## 1. Two deterministic signed cancellation bounds for the mixed model

For $0<x\le y$, write

$$
 \mathcal M_K(x,y)=\int_0^x \sqrt u\, B_u(y)\,du,\qquad
 B_u(y)=\sum_{k\ge1}S(kN)\left[
 \sqrt{u+k}\mathbf1_{u+k\le y}
 +\sqrt{u-k}\mathbf1_{0<u-k\le y}
 -\sqrt{k-u}\mathbf1_{0<k-u\le y}\right].
 \tag{4}
$$

Each term with a square root is interpreted as zero outside its indicated domain. The physical kernel of $K_N$ is $2\pi r_N(x)r_N(y)\mathcal M_K(x,y)$, by the [exact cumulative kernel](source-round2.md). The two difference signs are positive and the reflected sum is negative. The line parameter is $du$, not arclength.

For $N$ even the singular series expansion is

$$
 S(kN)=S_N\sum_{d\mid k} a_N(d),\qquad
 a_N(d)=\mathbf1_{d\ {\rm odd,\ squarefree},\ (d,N)=1}
                    \prod_{p\mid d}(p-2)^{-1}.
 \tag{5}
$$

Uniformly in $N$, $\sum_{d\le t}a_N(d)\ll\log(2t)$ for $t\ge1$: the positive sum is bounded by the Euler product over odd primes $p\le t$ of $1+(p-2)^{-1}$, whose ratio to the ordinary Mertens product is bounded by the convergent product of $1+1/(p(p-2))$. The same factor estimate gives $S_N\ll\log\log(3N)$, by taking $p\le\log N$ in Mertens and bounding $\sum_{p\mid N,\,p>\log N}1/p=O(1)$.

For a bounded-variation function $g$ of compact support on $[0,\infty)$,

$$
 \left|\sum_{j\ge1}g(jd)-\frac1d\int_0^\infty g(t)\,dt\right|
 \le \mathrm{TV}(g)
 \tag{6}
$$

with endpoint jumps included. Integrate the difference between the endpoint value and the function over each length $d$ interval and sum. For fixed $u\le x\le y$, all three $k$-profiles in (4) have variation $O(\sqrt y)$ on extending by zero. Their integrals are, respectively, $\int_u^y\sqrt v\,dv,\int_0^u\sqrt v\,dv,\int_0^y\sqrt v\,dv$, so the signed total is zero. Apply (6) to each progression $d\mid k$ in (5) and sum $d\le y+u$ (larger $d$ have no samples), keeping the same cutoff for the cancelling integrals. This gives

$$
 |B_u(y)|\ll S_N\sqrt y\log(2y),\qquad
 |\mathcal M_K(x,y)|\ll S_N x^{3/2}\sqrt y\log(2y)
 \quad (0<x\le y,\ y\ge2).
 \tag{7}
$$

A stronger dependence on $x$ holds for the $y$-derivative. For fixed $x$, $\mathcal M_K(x,y)$ is locally absolutely continuous in $y$ because each line has slope of absolute value one and the sum is locally finite. For $y>x$, the reverse difference $u=y+k$ does not occur inside $u\le x$; in the other two orientations differentiation yields, for almost every $y$,

$$
 \partial_y\mathcal M_K(x,y)
 =\sqrt y\sum_{k\ge1}S(kN)
   \left[\sqrt{y-k}\mathbf1_{0<y-k\le x}
              -\sqrt{k-y}\mathbf1_{0<k-y\le x}\right].
 \tag{8}
$$

On each $d$-lattice the two integrals over $k$ are both $\int_0^x\sqrt v\,dv$, since $y>x$ keeps both sampled ranges on the positive $k$-axis. The two variations are $O(\sqrt x)$. Apply (6) and (5), this time with $d\le y+x$, to obtain

$$
 |\partial_y\mathcal M_K(x,y)|\ll S_N\sqrt{xy}\log(2y)
 \quad(0<x<y,\ y\ge2).
 \tag{9}
$$

Both cancellations use the reflected term; taking absolute values of the three original line contributions would not yield these bounds.

## 2. The full mixed fine crossing

Fix a high cell $I=[a,b)$ in a dyad $[V,2V)$. Subtract the kernel obtained by replacing $\mathcal M_K(x,y)$ on that cell by $\mathcal M_K(x,a)$; this subtracted kernel is killed on the right by $E$, since its $y$-dependence on the cell is proportional to $r_N(y)$. For $x<Y\le a\le y$ the minimum of (7) on the two endpoints and the integrated bound (9) gives the difference-kernel envelope

$$
 \ll S_N\,\frac{\log(2V)}{V}\,
             m_N(\log x)m_N(\log y)\min(1,d_V/x).
 \tag{10}
$$

This controls the origin as well, without a derivative bound at $x=0$. For $d\ge1$,

$$
 \int_0^Y m_N(\log x)^2\min(1,d/x)^2\,dx\ll d.
 \tag{11}
$$

Indeed on $Nx\ge1$ the factor $m_N^2\le2$ and the integral of $\min(1,d/x)^2$ over $x>0$ is $2d$; on $Nx<1$ its integral is $O(1/N)$ because $2\beta=1/4<1$. On each $y$-dyad the total length is $V$, and $m_N(\log y)^2\le2(NV)^{-2/L}$. Square (10), use (11), and sum the **actual**, possibly infinite set of dyads:

$$
 \|P_Y K_NE\|_{\rm HS}^2
 \ll S_N^2\sum_{V=2^jY}\frac{d_V}{V}
                    (\log(2V))^2(NV)^{-2/L}
 \ll S_N^2 Y^{-1/3}(\log(2Y))^2.
 \tag{12}
$$

For the last step (1) gives $1\le d_V\ll V^{2/3}$ uniformly for all large $N$, since $V^{1/2}(NV)^{\vartheta/L}=e^\vartheta V^{1/2+\vartheta/L}$ and the expression before flooring exceeds one already at $Y$. The dyadic geometric series with factor $V^{-1/3}$ dominates the quadratic logs uniformly in $Y$. Equation (12) is $o(L^{-2K})$ with the threshold (1). On $(0,Y)\times [Y,\infty)$ the unfrozen model is Hilbert–Schmidt by (7) and (11) with the factor $\min(1,d/x)$ omitted and finite $Y$. Thus the subtracted kernel is Hilbert–Schmidt as well; alternatively apply the subtraction first on finitely many cells, then take the justified HS limit. This verifies deletion by the genuine orthogonal projection, not by independent estimates of each cell's operator norm.

The exact diagonal kernel is

$$
 D_N(x,y)=2\pi r_N(x)r_N(y)N^{-2}
        \sum_{\substack{n\le N\min(x,y)\\(n,N)=1}}\Lambda(n)^2 n.
 \tag{13}
$$

For the mixed crossing its minimum equals $x$; the $y$-leg is proportional to $r_N(y)$ on each cell. Hence $P_YD_NE=0$ exactly.

For the actual prime Gram, the character argument of [R30](weak-s-exterior-fine.md) proves the **global** estimate $\|P_N^{\rm arith} E\|_{\rm HS}\ll L^{-K-\epsilon}$ before restricting the other leg: it combines the full Gram trace $O(L^2)$ with $\operatorname{Avg}_{\chi\ {\rm odd}}\|Ep_\chi\|_2^2\ll L^{-2K-2-2\epsilon}$ for the actual Volterra atoms. This and (12) control $P_Y T_NE$. The doubly exterior estimate $\|Q_YT_NE\|_{\rm HS}=o(L^{-K})$ is [R30](weak-s-exterior-fine.md) with exactly (1). Adding the two orthogonal outputs and using self-adjointness proves (2).

## 3. Entire deterministic separated crossing and truncation to a finite coarse tail

Bound the model kernel from (7) by $S_N\log(2y)m_N(\log x)m_N(\log y)/y$ for $0<x\le A\le B\le y$. Since $\int_0^A m_N(\log x)^2\,dx\ll A$ when $A\ge1$, and $\int_B^\infty y^{-2}(\log(2y))^2\,dy\ll (\log(2B))^2/B$, this gives the second term in (3) on the entire crossing, not just fine directions. For (13), Chebyshev yields $\sum_{n\le t}\Lambda(n)^2 n\ll t^2\log(2+t)$ and there are no terms if $t<1$. Then the kernel bound is $O(\log(2NA)\sqrt x\,y^{-3/2}m_N(\log x)m_N(\log y))$, and $\int_0^A xm_N(\log x)^2\,dx\ll A^2$ gives the first term in (3). Neither bound claims cancellation in $P_N^{\rm arith}$.

For clarity the following finite-tail cutoff is a consequence of standard local-GRH damping and the published stationary benchmark, not a new estimate in the intervening coarse region. For fixed $K>0$ and an [R30](weak-s-exterior-fine.md) starting point $Y$ with $Y\le W$, take $W$ to be a dyadic boundary $2^jY$ at least $\exp((2K+12)L\log L)$. The full row and column outside $W$ satisfy

$$
 \|T_N Q_W\|_{\rm HS}+\|Q_W T_N\|_{\rm HS}=o(L^{-K})
 \tag{14}
$$

provided $Y\le N^C$ for any fixed $C$. To check this with the current normalization, the local GRH character prime number theorem for a nonprincipal odd $\chi\bmod N$ gives $|\sum_{n\le Nu}\Lambda(n)\sqrt n\,\chi(n)|\ll Nu(\log(2Nu))^2$ by Abel from the usual square-root prime sum, including imprimitive $\chi$ after the missing Euler terms. Then

$$
 \operatorname{Avg}_{\chi\ {\rm odd}}\|Q_Wp_\chi\|_2^2
 \ll\int_{\log(NW)}^\infty e^{-2z/L}(1+z)^4\,dz
 \ll L^5 e^{-\log(NW)/L}.
$$

The full Gram trace $O(L^2)$ and rank-one Cauchy give $\|P_N^{\rm arith} Q_W\|_{\rm HS}\ll L^{7/2}(NW)^{-1/(2L)}$. For $P_Y(D_N+K_N)Q_W$, use (3), with $Y\le N^C$. On $Q_Y(D_N+K_N)Q_W$, the [R30 stationary benchmark](weak-s-exterior-fine.md#diagonal-and-beta-benchmark) differs in HS by $o(L^{-K})$ from $m_N(s)k_N(s-t)m_N(t)$ in the log coordinate, and $\|k_N\|_2\ll L$. Restricting $t\ge\log W$ in this kernel gives HS $O(L^{3/2}(NW)^{-1/L})$, since $\int_{\log W}^\infty m_N(t)^2dt\ll L(NW)^{-2/L}$ and $m_N(s)$ is bounded on the other exterior side. This proves (14). The opposite row follows by adjunction. One can pick $W$ within a factor two of that stated threshold for any polynomial $Y$.

Let $\Pi_{[Y,W)}$ be the coarse projection on the finitely many original cells up to this dyadic boundary. From (2) and (14), on the physical Hilbert space

$$
 \|T_N-(P_Y+\Pi_{[Y,W)})T_N(P_Y+\Pi_{[Y,W)})\|_{\rm HS}=o(L^{-K}).
 \tag{15}
$$

For this, first remove $Q_W$ on both sides using (14), then remove the remaining fine projection $E(1-Q_W)$ using (2); the dyadic boundary makes the cell and cutoff projections commute. The prefix itself is not claimed finite rank.

## 4. What this closes after the prefix theorem

Take $Y=M=Q^\gamma$ on the selected shell, with the parameters, local assumptions and the **additional** auxiliary Dirichlet GRH required by the [R49](r49-operator-full-prefix-variance.md) prefix theorem. The new deletion and extreme cutoff are local-GRH only and uniform on the shell; [R49](r49-operator-full-prefix-variance.md)'s $P_YT_NP_Y$ bound is still a selected-modulus estimate, $O_\eta(Q^{-1/400+\eta})$ in RMS in the three stated regimes, not an assertion for a specified modulus. Up to that prefix term and the uniform $o(L^{-K})$ error, the following two *actual* blocks remain:

$$
 P_YT_N\Pi_{[Y,W)},\qquad
 \Pi_{[Y,W)}T_N\Pi_{[Y,W)} .
 \tag{16}
$$

In operator norm, the larger of the two is at most $\|T_N\|$, and the sum of the second and twice the first plus the prefix and the error bounds $\|T_N\|$ from above. Thus (15) removes the entire high fine crossing, including central-to-exterior, and the entire extreme tail. It leaves the two explicitly coarse blocks in a finite-height but still large intermediate region. None of (2)–(16) establishes a bound on these blocks, on pointwise success, or on any prescribed thin set not already covered by [R49](r49-operator-full-prefix-variance.md).
