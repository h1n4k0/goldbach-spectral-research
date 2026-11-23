# Full complementary support for the signed critical principal projection

This is a corollary of the [critical-prime principal projection](weak-s-type-ii-critical-prime-arcs-principal-projection.md). Keep its even $N$, exact fixed prime-box transform $P$, arbitrary selector on those primes, upper window $y$, strict $k>t$, and critical prime denominator shell $\mathcal Q=\{q\text{ prime}:.8\sqrt N\le q\le .9\sqrt N\}$ with $|\beta|\le1/(10N)$. Put $L=\log N$ and $L_2=\log L$. Now use the **full** complementary polynomial $D$ with actual $d\ge\sqrt N$, any prescribed hard interval $I_d$, and no extra lower threshold. All original signs, unit masks and $\mu^2(dk)$ are unchanged.

**Corollary.** Unconditionally, with effective constants,

$$
 \int_{|\beta|\le1/(10N)}\sum_{q\in\mathcal Q}
    \left|\sum_{a=1}^{q-1}
      P^{(0)}_q(a/q+\beta)D(a/q+\beta)e(-N(a/q+\beta))\right|\,d\beta
       \ll \frac{N L_2}{L^2}.
$$

Here $P^{(0)}_q=-P(\beta)/(q-1)$ is the exact principal projection at $q$. The bound is for the signed full numerator sum, not for its individual terms, and gives no estimate on the nonprincipal projection of $P$.

**Proof.** Fix $A=3$ in the critical-prime theorem and split $D$ at its resulting threshold $\mathcal D_A=\sqrt N L^{2000(\lceil A\rceil+10)}$. The signed bound for $d\ge\mathcal D_A$ is $O(N L^{-3})$. For the lower part split $\sqrt N\le d<\mathcal D_A$ into $O(1+L_2)$ dyads of scale $D_0\ge\sqrt N$. If $q\mid N$ the congruence $dk\equiv N\bmod q$ has no terms by the true $N$-unit mask. Otherwise, for each actual $k$, the congruence has no solution if $q\mid k$, and at most one residue class of $d$ if $(k,q)=1$. The number of $d$ in the dyad in one class is $O(D_0/q+1)=O(D_0/q)$ because $q\asymp\sqrt N$. The condition $dk<N/2$ allows only $O(N/D_0)$ values of $k$. Thus even in absolute values this congruence part costs $O(N/q)$ on the dyad. The prime number theorem, or its elementary upper bound, yields $\sum_{q\in\mathcal Q}q^{-1}\ll1/L$. Consequently the sum over $q$ of the absolute lower-$d$ congruence values $A_q(\beta)$ is $O(N(1+L_2)/L)$ uniformly in $\beta$.

Use the exact finite numerator identity $q A_q(\beta)-D(\beta)$ separately for this lower piece. Its baseline at $\beta$ is exponentially small by the $q=1$ case of the [signed-seam major-arc analysis](weak-s-type-ii-signed-seam-major-arcs.md), which permits this hard $I_d$ restriction. The remaining factors are $|P(\beta)|\ll N/L$, $q/(q-1)=O(1)$ and an integration width $O(1/N)$. They prove the asserted bound. The actual signed contribution from the lower and upper $d$ parts is combined by the triangle inequality after the full numerator sum. No estimate follows for the whole rational shell or for weak S.
