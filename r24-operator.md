# Operator lane: quantitative deletion of separated rectangles of the actual R21 bridge

Work with the microscopic-to-exterior crossing under local GRH(N) in R20–R21. Write $L=\log N,\ \alpha=1/L,\ \beta=1/8,\ S=S(N),\ \delta_N=\sqrt{S/N}L^{3/2}$, and fix $0<\gamma<1,\ Y=N^\gamma,\ 1\le U\le\min(Y,N/4)$. The units are those of R21: $y$ is the dimensionless physical high coordinate and $U$ is the raw low cutoff. Use exactly the R21 columns $c_jb(y_j)$, increment vectors $b_k=b(y_{k+1})-b(y_k)$, weights $W_k=\sum_{j>k}c_j^2$, $W_{-1}=\|c\|^2$, and projection $F_c$. In particular those $b_k$ contain the actual plus-minus prime-power increments in the two opposite reduced residue classes, not random sign proxies. Write $M=RF_c$ where $R$ is the R21 sampled map, not the statement of Hypothesis R. Its exact covariance is $C=MM^*=\sum_{k,\ell}\Gamma_{k\ell}b_k\otimes b_\ell$ in the simultaneous-square sense of R21.

## 1. Statement and scope

Delete the rectangles $V\le y_k<2V,\ Z\le y_\ell<2Z$ and their transposes, where $V,Z$ range over the dyadic grid $Y,2Y,4Y,\ldots$. Each of the following three regions is a uniform trace-norm $o(\delta_N^2)$ deletion from that actual covariance:
$$
\begin{array}{ll}
{\cal D}_1:& Z\ge U^2 V^3,\\
{\cal D}_2:& Z\ge U\sqrt N\, V^{3/2}L^\epsilon,\\
{\cal D}_3:& Z\ge UN V L^{2+\epsilon},
\end{array}\qquad(\epsilon>0\text{ fixed}).
\tag{1}
$$
We assume $N$ sufficiently large so these imply $Z\ge2V$. The bound for the union is also $o(\delta_N^2)$; assign each rectangle to one regime in which it qualifies. For ${\cal D}_1$ the trace estimate is $O_\gamma(S^2 L/N)$ and uses only Brun–Titchmarsh and the elementary proper-power bound of R21 once the covariance is identified. For ${\cal D}_2,{\cal D}_3$ the trace estimates are $O_{\gamma,\epsilon}(S L^{3-\epsilon}/N)$ and $O_{\gamma,\epsilon}( L^{3-\epsilon}/N)$, respectively, using local odd-character GRH for actual signed prefixes. The late phase can be arbitrarily high in these statements.

For example, at $U=Y=N^{3/40}$ the first high dyad at $V=Y$ paired with dyads at $Z\ge N^{3/8}=N^{.375}$ is covered at the R-square scale. This is a substantial but very uneven part of the separated region; it does not cover comparable dyads or even all polynomially separated dyads beginning at $V=Y$. Squared covariance errors are compared via trace bound $\ge$ operator bound and then the inequality $|\sqrt a-\sqrt b|\le\sqrt{|a-b|}$, not multiplied into the original crossing error.

A different statement at any fixed inverse-log S scale: for $A\ge Y$, one may discard **every covariance term with $y_k<A$ or $y_\ell<A$**, including all cross terms with arbitrary late increments, if $AU\le N^{1-\eta}$ for fixed $\eta>0$. Under this condition its trace norm is $O_{\gamma,\eta}(S L^2N^{-\eta/2})$ and hence negligible at every fixed inverse-log rate. In particular $U=N^{3/40}$ allows $A=N^{37/40-\eta}$ if $A\ge Y$. This last statement is about a sector of the actual covariance, and is not a deletion at the R scale.

## 2. Ordered dyads: exact signed separation

The bridge identity of R21 yields for $k<\ell$
$$
\Gamma_{k\ell}=(1-W_k/W_{-1}) W_\ell.
$$
Accordingly the full dyadic rectangle is not a sum estimated termwise. It is exactly the single rank-one operator $a_V\otimes d_Z$, where
$$
a_V=\sum_{V\le y_k<2V}(1-W_k/W_{-1})b_k,\qquad
d_Z=\sum_{Z\le y_\ell<2Z}W_\ell b_\ell .
\tag{2}
$$
This uses the actual bridge weights; replacing either by a count of cells would give a different rectangle. Its trace norm is $\|a_V\|_2\|d_Z\|_2$.

Here are estimates for these two linear sums. Put $\ell_v=\log(2Nv)$. For any consecutive subinterval of indices in a dyad at $v\ge Y$,
$$
\left\|\sum_{k\in I} b_k\right\|_2
 \ll_\gamma \sqrt{U/N}\,F(v),\qquad
F(v)=\min\bigl(Sv^{3/2},\sqrt N\,v\,\ell_v^2\bigr).
\tag{3}
$$
For the first estimate apply the genuine per-progression first moment (R22 (4), proved via Montgomery–Vaughan Brun–Titchmarsh and R21's unit-root counting) at $3v$, and bound the $\sqrt{m/N}$ factor by $O(\sqrt v)$ on the segment. This bounds the signed increment in each $A_n$ even by absolute values. For the second estimate, exact odd-character orthogonality expresses the resulting signed unweighted opposite-residue prefix as
$$
{\rm Avg}_{\chi\bmod N,\ \chi(-1)=-1}\overline{\chi(n)}
                       \sum_{m\le Nv}\Lambda(m)\chi(m).
$$
The standard local GRH explicit-formula bound for each odd character in this average is $O(\sqrt{Nv}\log^2(2Nv))$, including the inducing Euler factors, as used in R21. Partial summation of this estimate over the raw segment in the dyad, with weight $\sqrt{m/N}$, gives $O(\sqrt N\,v\,\ell_v^2)$ for the signed increment of $A_n$. No GRH for an auxiliary modulus or for the principal character enters. Either per-$n$ estimate converts to (3) by the raw low map $\mathcal V_U$ of R22 and its elementary Chebyshev envelope $\|\mathcal V_U z\|_2\ll\sqrt U\sup_n|z_n|$: in raw low coordinates $b(y)=(2\pi/\sqrt N)\mathcal V_U A(y)$.

The weights of $a_V$ in (2) are nonnegative, nondecreasing, and at most 1. The weights of $d_Z$ are nonnegative, nonincreasing, and bounded by
$$
W_\ell\ll Z^{-2}(NZ)^{-2\alpha},\qquad y_\ell\ge Z
\tag{4}
$$
for large $N$ with $\alpha\le\beta$. A weighted consecutive sum with such a monotone weight has norm at most twice the weight supremum times the supremum of partial-sum norms, by discrete partial summation; this is valid for vectors. The bounds from (3) thus give
$$
\|a_V\otimes d_Z\|_1
 \ll_\gamma \frac{U}{N}\,
 Z^{-2}(NZ)^{-2\alpha}F(V)F(Z).
\tag{5}
$$
In the GRH regimes the cancellation is the one in the actual signed AP partial sums, made available by the exact factorization and monotonicity. The Brun–Titchmarsh regime alone does not assert arithmetic sign cancellation: it disposes of that region by the bridge weight and the arithmetic mass bound.

## 3. Sum the infinitely many separated dyads

For a positive threshold $Z_0=Z_0(V)\ge2V$, the first actual dyad $Z\ge Z_0$ lies in $[Z_0,2Z_0)$. For fixed $b>0$ and integer $m\ge0$, summation of a geometric tail gives
$$
 \sum_{Z\ge Z_0,\ Z\text{ a dyad}} Z^{-b}(NZ)^{-2\alpha}\ell_Z^m
 \ll_{b,m} Z_0^{-b}(NZ_0)^{-2\alpha}\ell_{Z_0}^m .
\tag{6}
$$
The remaining $V=2^jY,\ j\ge0$, sum with even small $\alpha=1/L$ is important. In each regime $Z_0=C_N V^p$ with fixed $p>0$, and $L\lesssim\log(2NC_NY^p)\lesssim_{\gamma,\epsilon} L$ for $U\le Y=N^\gamma$. For any fixed integer $m\ge0$,
$$
 \sum_{V=2^j Y} (N Z_0(V))^{-2\alpha}\ell_{Z_0(V)}^m
 \ll_{\gamma,\epsilon,p,m} L^{m+1}.
\tag{7}
$$
Indeed this is dominated by $\sum_{j\ge0}e^{-c_p j/L}(L+j)^m$, bounded by comparing with a rescaled integral. In regime 3 one may also multiply by $\ell_V^2$ and use $m=4$ for the same reason.

* In ${\cal D}_1$, use the BT choices $F(V)\le SV^{3/2}, F(Z)\le SZ^{3/2}$. Sum (5) over $Z$ by (6) with $b=1/2,m=0$; the factor $V^{3/2}Z_0^{-1/2}=1/U$. Sum (7) with $m=0$; the result is $O_\gamma(S^2L/N)$. Compared with $\delta_N^2=S L^3/N$, the ratio is $O(S/L^2)=o(1)$.
* In ${\cal D}_2$, choose $F(V)\le SV^{3/2}, F(Z)\le\sqrt N\, Z\ell_Z^2$. Now (6) has $b=1,m=2$; the factor $U\sqrt N V^{3/2}/Z_0=L^{-\epsilon}$ after the prefactor $S/N$. Equation (7) gives $O_{\gamma,\epsilon}(S L^{3-\epsilon}/N)$.
* In ${\cal D}_3$, use both GRH choices. Now the prefactor is $U V/Z_0=1/(N L^{2+\epsilon})$ after (6) with $b=1,m=2$. The two squared logs give the $m=4$ bound in (7), for $O_{\gamma,\epsilon}(L^{3-\epsilon}/N)$. Divide by $\delta_N^2$ using $S\gg1$.

The transpose at most doubles each estimate. The sums over these rectangles converge absolutely in trace norm even if the original simultaneous-square covariance does not converge absolutely term by term. Hence the deletion is an actual bounded operator subtracted from $MM^*$. If the remaining operator $C_{\rm rem}$ is not positive, use $|\|MM^*\|-\|C_{\rm rem}\||\le o(\delta_N^2)$; this still compares their square roots. Only after that comparison is it legitimate to compare the original physical crossing with the R21 $o(\delta_N)$ operator approximation.

## 4. Early increment sector, including all late cross weights, at S scale

Truncate the increments at $y_k<A$. With $u_k=(c_j{\bf1}_{j>k})_j$ as in R21, put $R_E=\sum_{y_k<A}b_k\otimes u_k$, $M_E=R_E F_c$, and $M_L=M-M_E$. Let $A^*=Y+\#\{k:y_k<A\}$, an exact cell endpoint in $[A,A+1)$ except equality permitted. The columns of $R_E$ are exactly
$$
 c_j[b(\min(y_j,A^*))-b(Y)] .
$$
The first moment (4) of R22 and the same low envelope prove $\|b(y)\|_2\ll_\gamma S\sqrt{U/N}\,y^{3/2}$ for all $y\ge Y$. For $y_j\le A^*$, $c_j^2\ll y_j^{-3}$, giving a squared column sum $O_\gamma(S^2 UA/N)$ over those columns. For $y_j>A^*$, all columns use the frozen pair of endpoints, and $\sum_{y_j>A^*}c_j^2\ll (A^*)^{-2}$; this gives the same bound. Thus
$$
 \|M_E\|_{\rm HS}\le\|R_E\|_{\rm HS}\ll_\gamma S\sqrt{UA/N}.
\tag{8}
$$
Also $\|M\|_{\rm HS}\ll L^2$: the unsampled covariance $P_N$ is positive with $\|P_N\|_{\rm HS}\le{\rm tr}P_N={\rm Avg}_\chi\|p_\chi\|_2^2\ll L^2$ by the mean atom bound used in R20 §3. Restriction to the crossing and R21's explicit HS sampling comparison (as applied to $P_N$ alone) preserves this bound. Therefore the exact sector containing at least one early index satisfies
$$
 \|C-M_LM_L^*\|_1
  \le \|M_E\|_{\rm HS}(\|M\|_{\rm HS}+\|M_L\|_{\rm HS})
  \ll_\gamma S\sqrt{UA/N}\,[L^2+S\sqrt{UA/N}].
\tag{9}
$$
The identification with the designated covariance terms follows by simultaneous cutoffs: the early increment map is finite, and the remaining F_c increment sum converges in HS as in R21. Under $UA\le N^{1-\eta}$ the displayed estimate proves the S-scale claim; in particular no sign assumption is made about the mixed early–late contribution. Its smallness is from smallness of the actual centered early map and the exact product inequality.

These results leave unresolved the genuine signed covariance on most of the surviving high–high dyadic comparisons, especially rows with nearby comparable heights not discarded in R21. They neither give a proof of a required S hypothesis for the full operator nor reach R on the whole crossing.
