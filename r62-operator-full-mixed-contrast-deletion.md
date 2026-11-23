# Full mixed deletion of the localized exterior contrasts

**Scope.** This addresses the mixed blocks left open by the localized-contrast theorem. On its selected moduli, a contrast supported in one or more exterior mesowindows can be coupled to **any** vector of the true Hardy space, including the original central prefix, the mesowindow means, or the still later exterior. The estimate does not delete the mean–mean block or establish a full weak-S bound. Auxiliary GRH is used only through the input contrast–contrast theorem; the deterministic benchmark estimate and the positive-Gram lift require no extra auxiliary moduli.

## Statement

Use the exact settings of [R60](r60-operator-localized-coarse-contrast-annulus.md): $\mathcal A$ consists of $J\ge1$ distinct even $N\in[Q,2Q]$; $1\le D\le H<M\le Q^\Gamma$ with $H\ge4$, and $R_N$ is the orthogonal projection onto the true weighted-zero subspace on each [R60](r60-operator-localized-coarse-contrast-annulus.md) mesowindow, physically transported by $Q/N$. Thus every window belongs to $[H/2,M]$, has length at most $D$, and the constraint in an individual window $I_N$ is $\int_{I_N}r_N(u)f(u)\,du=0$. Fix $0<\kappa<1/3$ and write $L=\log Q$. Assume the original local GRH at each selected $N$ and auxiliary Dirichlet GRH for all moduli $q\le\lceil20\sqrt{QD}\rceil$, including $q=1$, exactly as in [R60](r60-operator-localized-coarse-contrast-annulus.md). Then

$$
 \left(\operatorname{Avg}_{N\in\mathcal A}
             \|T_NR_N\|_{\rm HS}^4\right)^{1/4}
 \ll_{\Gamma,\kappa,\epsilon} Q^\epsilon
 \left(\frac{Q^{1/8}D^{3/8}}{J^{1/4}}+
       (D/Q)^{1/4}+(D/H)^{1/4}+H^{-\kappa/2}\right).
 \tag{1}
$$

The same bounds hold with adjunction and, up to a factor two, for the full deletion error

$$
 \mathcal E_N=\|T_N-(1-R_N)T_N(1-R_N)\|_{\rm HS}.
 \tag{2}
$$

In the example $H=Q^{2/5},\ M=Q^{3/5},\ D=Q^{8/25},\ J\gg Q^{99/100}$, use $\kappa=1/4$. Both (1) and (2), in fourth-root fourth mean, are $O_\epsilon(Q^{-1/400+\epsilon})$. With these same spatial parameters and no lower bound on $J$, at most $O_\epsilon(Q^{197/200+\epsilon})$ selected $N$ can have $\mathcal E_N>Q^{-1/1000}$. This does not ensure a conclusion for a specified modulus or a predetermined thinner selection.

## 1. Small full-leg contrast of the deterministic benchmark

Write $T_N=P_N^{\rm arith}-B_N$, with the actual positive odd-character Gram $P_N^{\rm arith}$ and $B_N=D_N+K_N$, the exact diagonal plus continuous Beta model. Here $D_N$ is an operator, not the mesowindow length $D$. Put $Y_0=H/2$ and let $P_{Y_0}$ and $Q_{Y_0}$ project onto $u<Y_0$ and $u\ge Y_0$, respectively, in the true physical coordinate. We prove, using only local GRH,

$$
 \|B_NR_N\|_{\rm HS}
 \ll_{\Gamma,\kappa,\epsilon} Q^\epsilon
                \left(\sqrt{D/H}+H^{-\kappa}\right)=:b.
 \tag{3}
$$

The right-hand side $b$ will denote a common bound on the selected shell, with its implied constant increased when necessary.

For the mixed deterministic crossing $x<Y_0\le y$, now in physical coordinates, the exact diagonal kernel is proportional to $r_N(y)$ on each mesowindow: its cumulative prime-power sum has upper endpoint $Nx$, since $x<y$. Thus $P_{Y_0}D_NR_N=0$. For $K_N$ let $\mathcal M_K(x,y)$ be the signed cumulative continuous model of [R51](r51-operator-full-leg-fine-bridge.md), so that its physical kernel is $2\pi r_N(x)r_N(y)\mathcal M_K(x,y)$. The two signed estimates of [R51](r51-operator-full-leg-fine-bridge.md) (7), (9) give for $x\le y,\ y\ge2$

$$
 |\mathcal M_K(x,y)|\ll S_N x^{3/2}\sqrt y\log(2y),\qquad
 |\partial_y\mathcal M_K(x,y)|\ll S_N\sqrt{xy}\log(2y),
 \quad S_N=\mathfrak S(N).
 \tag{4}
$$

These estimates retain both difference and reflected-sum terms; the derivative bound is almost everywhere and the cumulative function is absolutely continuous in $y$ on compact intervals. On a mesowindow $[a,a+\ell)$, $\ell\le D,\ a\ge Y_0$, subtract the constant-in-cumulative-coordinate kernel $2\pi r_N(x)r_N(y)\mathcal M_K(x,a)$, which vanishes after $R_N$ on the right. The resulting physical difference kernel is bounded by

$$
 S_N\,m_N(\log x)m_N(\log y)
          \frac{\log(2y)}{y}\min(1,D/x),
 \qquad
 m_N(\log t)=\big((Nt)^{-2/\log N}+(Nt)^{-1/4}\big)^{1/2}.
 \tag{5}
$$

Indeed the first bound in (4) controls the two endpoints and the second controls the increment. For any $D\ge1$, $\int_0^{Y_0}m_N(\log x)^2\min(1,D/x)^2\,dx\ll D$, using the bounded factors at $Nx\ge1$ and integrability of $(Nx)^{-1/4}$ below one. Also $m_N(\log y)\ll1$ for $y\ge Y_0$ and $\int_{Y_0}^\infty y^{-2}\log^2(2y)\,dy\ll H^{-1}\log^2(2H)$. Consequently

$$
 \|P_{Y_0}K_NR_N\|_{\rm HS}
        \ll S_N\log(2H)\sqrt{D/H}.
 \tag{6}
$$

The subtraction is an exact projection argument on the union of the mesowindows, not a sum of individual operator norms. Bound (4) also makes the mixed deterministic kernel itself Hilbert–Schmidt, so taking the difference and passing to the orthogonal projection is legitimate.

For the other output leg $u\ge Y_0$, use log coordinate $s=\log u$ with the unitary $\sqrt u$ factor. The deterministic stationary benchmark of [post-R15](operator-post-r15-stationary-tail.md) gives the exact comparison on the entire doubly exterior quadrant: $Q_{Y_0}B_NQ_{Y_0}$ differs from the kernel $m_N(s)k_N(s-t)m_N(t)$ by a HS operator of size

$$
 \ll_\kappa
       Y_0^{-\kappa}\exp(C_\kappa(\log N)^\kappa)
         +N^{-1/2}Y_0^{-1/2}\log^3(2NY_0).
 \tag{7}
$$

We omit the additional bounded Hardy damping factor from that theorem. The log-space mean direction on each mesowindow is $\rho(t)=e^{-t}m_N(t)$ restricted to it, because the physical mean direction is $r_N(u)$. Its logarithmic derivative is bounded absolutely; in particular this is the genuine transformed direction, not ordinary unweighted mean. Each log-window has length at most $2D/H\le2$. By the weighted interval Poincaré estimate in the proof of [R30](weak-s-exterior-fine.md), for any $g\in H^1$ on such a window $J_0$, projection $R_{J_0}$ to the complement of $\rho|_{J_0}$ obeys

$$
 \|R_{J_0}g\|_{L^2(J_0)}
 \ll |J_0|\big(\|g'\|_{L^2(J_0)}+\|g\|_{L^2(J_0)}\big).
$$

This follows from applying ordinary interval Poincaré to $g/\rho$, then multiplying by $\rho$, whose supremum and infimum are comparable on each window. Apply it along the input $t$-leg of the stationary kernel and sum the squared estimates over disjoint mesowindows. Since $\|k_N\|_{H^1(\mathbb R)}\ll L$, $m_N,m_N'$ are bounded on $s,t\ge\log Y_0$, and $\int_{\log Y_0}^\infty m_N(s)^2ds\ll L$, this costs $O(L^{3/2}D/H)$ in the HS norm including all outputs $u\ge Y_0$. No derivative across a boundary is taken. Equations (6) and (7), $S_N\ll\log\log(3N)$, and $D/H\le1$ prove (3); the subpower exponential in (7) is absorbed by $Q^\epsilon$.

## 2. Positive trace lifts the contrast compression to every mixed block

Under local GRH, the actual covariance is the positive operator $P_N^{\rm arith}=\operatorname{Avg}_{\chi\ {\rm odd}}p_\chi\otimes p_\chi$ in the unitary physical realization. Its full trace is $O(L^2)$ by Li–Liu Proposition 6.5 as used in [R30](weak-s-exterior-fine.md), not a trace taken on the mesowindows. Factor $P_N^{\rm arith}R_N=(P_N^{\rm arith})^{1/2}((P_N^{\rm arith})^{1/2}R_N)$. The HS ideal bound and positivity give

$$
 \|P_N^{\rm arith}R_N\|_{\rm HS}^2
 \le \operatorname{tr}(P_N^{\rm arith})\,\|R_NP_N^{\rm arith}R_N\|_{\rm op}
 \ll L^2\big(\|R_NT_NR_N\|_{\rm HS}+b\big).
 \tag{8}
$$

The last step uses $R_NP_N^{\rm arith}R_N=R_NT_NR_N+R_NB_NR_N$ and (3). In particular it does not apply positivity to $T_N$ itself.

The pointwise consequence of (3), (8) is

$$
 \|T_NR_N\|_{\rm HS}
 \ll L\big(\|R_NT_NR_N\|_{\rm HS}+b\big)^{1/2}+b .
 \tag{9}
$$

Taking fourth-root fourth means and using the triangle inequality in mean square for the right-hand side inside the square root bounds this by $O(L(A+b)^{1/2}+b)$, with $A=(\operatorname{Avg}_{N\in\mathcal A}\|R_NT_NR_N\|_{\rm HS}^2)^{1/2}$. Insert [R60](r60-operator-localized-coarse-contrast-annulus.md)'s $A\ll_\epsilon Q^\epsilon(Q^{1/4}D^{3/4}/\sqrt J+\sqrt{D/Q})$. This gives (1): to absorb $b$ in the displayed terms one may use the explicit bound (3), $D/H\le1,\ H\ge4$, and a smaller $\epsilon$ there. Adjunction and the exact identity $T_N-(1-R_N)T_N(1-R_N)=T_NR_N+R_NT_N(1-R_N)$ give (2). The argument uses the same actual directions, not a new compression responsive to the selected moduli. It controls, for example, the genuine mixed blocks from those contrasts against both the window means and the whole previously estimated prefix.

For the printed example, [R60](r60-operator-localized-coarse-contrast-annulus.md)'s leading RMS is $O_\epsilon(Q^{-1/200+\epsilon})$, while (3) gives $b\ll_\epsilon Q^{-1/25+\epsilon}$ at $\kappa=1/4$. The fourth-moment exponent in (1) is therefore $-1/400$ before $\epsilon$. For every $N$ at which [R60](r60-operator-localized-coarse-contrast-annulus.md) has $\|R_NT_NR_N\|_{\rm HS}\le Q^{-1/400}$, (9) gives $\mathcal E_N\ll LQ^{-1/800}$, which is below $Q^{-1/1000}$ for all large $Q$. Hence the example's exceptional count transfers with no new modulus loss. This step uses the [R60](r60-operator-localized-coarse-contrast-annulus.md) pointwise-good set, not just Markov at a weaker asymptotic rate.

## 3. The surviving window means are not negligible term by term

Let $W_N$ be the projection onto the weighted mean lines of all transported mesowindows. In the example the deterministic block $\|W_NB_NW_N\|_{\rm op}\gg L$. In fact, in log coordinate choose a fixed smooth nonzero bump translated to a length-one interval in the **interior** of the transported annulus, for example to a position at distance two from its lower log endpoint for large $Q$. Normalize $f$ proportional to that bump divided by $m_N$. The normalization factor is bounded above and below because these raw logarithmic sizes are polynomial in $Q$. The stationary multiplier is bounded below by $cL/(1+\xi^2)$ for all real frequencies $\xi$ at large $N$, as proved for the [post-R15](operator-post-r15-stationary-tail.md) benchmark. Plancherel gives stationary Rayleigh form $\gg L$ on this normalized $f$; (7) makes the actual $B_N$ form differ negligibly. The bump is entirely in the physical annulus, so $f=W_Nf+R_Nf$, and replacing $f$ by $W_Nf$ changes the form by $O(b)$ by (3). Since $\|W_Nf\|\le1$, the asserted lower bound follows. This is **not** a lower bound on the signed $T_N$; it says that its remaining mean–mean problem requires actual prime covariance cancellation against a non-negligible benchmark.

[R60](r60-operator-localized-coarse-contrast-annulus.md) also identified the contrast subspace of the original [R51](r51-operator-full-leg-fine-bridge.md) coarse cells, leaving at most $O(M/D)$ independent coarse directions in the transported annulus. Inequality (2) now deletes these coarse contrasts with **all** crossings, but the remaining means, boundary coarse cells, and the later coarse tail are untouched wherever no such contrast is a leg. There is still no bound at a specified modulus or full weak S.
