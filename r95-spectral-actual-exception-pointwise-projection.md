# Keep the exact exceptional projection until after the two poles

**Scope.** This refines the error term in the [all-target finite Ramanujan formula](r94-spectral-all-target-ramanujan-exception.md). It uses the original band-limited left weight throughout the integer arithmetic, and returns to the genuine hard left test only in the resulting real integrals. Neither the original finite Ramanujan range nor the possible exceptionally aligned main term is changed. The conclusion is pointwise for the exceptional correction, not for the full mixed sum. No Dirichlet GRH, external zero-gap result, or denominator-completion margin is assumed.

Retain the exact setup of that formula and of the [all-scale reduction](r87-spectral-all-scale-exceptional-left-reduction.md): $Y\le N\le2Y$ even, $G=\log Y$, $L=\log N$, $Q_0=\exp(16\sqrt G/\log G)$, and $\Delta_0=2Q_0/Y$. The cutoffs are $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$ for the same fixed admissible $B>B_0>0$. The original left interval is real and half-open, $I\subset(N/2,9N/16]$, and its weight $\omega$ has uniformly bounded supremum and pointwise variation. The original right support is $V=[N/3,2N]$. Keep the actual primitive real Page character $\chi$ of conductor $r\le Q_0$ with simple real zero $\beta>1-4a_0/\sqrt G$, if present; otherwise the exceptional correction is zero. Let $r_o$ be the odd part of $r$, so $r_o\ge r/8$.

Define the compact hard left function $F(n)=\mathbf1_I(n)\omega(n)n^{\beta-1}$, with zero understood outside $I$ and the actual representative on $I$. Let $\mathcal D_i(N)$ for $i=0,1$ be exactly the two finite real expressions named $\mathcal D_i$ in the all-target formula, with that $F$ and the original short cutoff $S=Y^{1/10}$. In particular their prefactor includes $-r\chi(-1)/(\varphi(r)L'(\beta,\chi)^2)$, and their finite sum is over squarefree $t\le Q_0/r$ prime to $r$, with the same $q\mid t$ options. No global Euler completion in $t$ is used.

**Theorem.** There are fixed $C,c>0$ such that for each fixed $\epsilon>0$, uniformly in the true $N,I,\omega$,

$$
 \begin{split}
 \mathfrak E_\pm(N;I,\omega)
 &=\frac{c_r(N)}{\varphi(r)}
          \frac{\mathcal D_0(N)\pm\mathcal D_1(N)}2\\
 &\quad+O_\epsilon\!\left(
 Y^\beta G^C\left[
     \mathbf1_{(N,r_o)=1}r^{-1+\epsilon}
      +\frac{|c_r(N)|}{\varphi(r)}
              e^{-4(1-\beta)G/5}Q_0^{-1}\right]
      +Y^\beta e^{-c\sqrt G}\right).
 \end{split}                                                        \tag{1}
$$

Here the $+$ sign denotes the true even squarefree prime-count color. In particular, if $(N,r_o)>1$ and $c_r(N)=0$, then the entire correction is $O(Y^\beta e^{-c\sqrt G})$. These two arithmetic conditions are compatible, for example when $8\mid r$, $N\equiv2\bmod4$ and an odd prime of $r$ divides $N$; this is not an existence claim for such a Page character. If $r\mid N$, the first error in brackets is absent for all sufficiently large dyads with a Page character, and the second is the stated $Q_0^{-1}$ error, not a bound on the remaining real expression.

## 1. Use the literal band-limited representative in the integer sum

Write $e(x)=e^{2\pi i x}$, $\widehat F(\eta)=\int F(u)e(-\eta u)\,du$ and

$$
 W(n)=\int_{-\Delta_0}^{\Delta_0}\widehat F(\eta)e(\eta n)\,d\eta,
 \qquad
 K_{\Delta_0}(u)=\frac{\sin(2\pi\Delta_0 u)}{\pi u},
 \qquad W=F*K_{\Delta_0}.
 \tag{2}
$$

The frequency convention in the all-scale reduction writes both signs the other way; by symmetry of the band this is its same function. Its exact identity (9), **without** the intervening hard-cut replacement, is

$$
 \mathfrak E_\pm=
  -\frac r{\varphi(r)}\sum_{m\in V\cap\mathbb Z}
    M_\pm(m)\chi(N-m)\mathcal C_{r,Q_0}(N-m)W(N-m),
 \qquad
 \mathcal C_{r,Q_0}(n)=
  \sum_{\substack{t\le Q_0/r\\(t,r)=1}}\frac{\mu(t)c_t(n)}{\varphi(t)} .
 \tag{3}
$$

In particular $m$ still ranges across all of $V$, not just $N-I$. Negative $n=N-m$ have their actual values in (3), and $n=0$ has zero contribution because $\chi(0)=0$. All corrections below keep (3) as an identity on this whole support.

On $N-V$, both the supremum and variation of $W$ are $O(Y^{\beta-1}(1+\log(2Q_0)))$. To see this, $\|F\|_\infty+\operatorname{Var}F\ll Y^{\beta-1}$ on the real line including its two hard jumps. For $n$ in a fixed $O(Y)$ interval containing $N-V$ and $u$ in the support of $F$, $|n-u|\ll Y$. The integral of $|K_{\Delta_0}|$ on that difference range is $O(1+\log(2Q_0))$ by splitting the bound $\min(2\Delta_0,1/(\pi|n-u|))$. This proves the supremum estimate. In the variation estimate differentiate the convolution in the sense of distributions, $W'=dF*K_{\Delta_0}$, then use the total variation measure of the compactly supported distributional derivative of $F$. The same truncated kernel integral bounds the $L^1$ norm of $W'$ on the interval. This argument holds for the actual continuous band projection in (2) even if the initial $F$ has prescribed point values at jumps. Thus no factor of $Q_0$ is lost in this pointwise-BV norm. Composition with any of the one-variable affine product maps used below has the same bound on the genuine intervals.

## 2. The long unsigned deletion and its true rare class

Use the two actual signed arrays $A_0=M_>$ and $A_1=\mu(m)M_>$ in the [long unsigned deletion](r91-spectral-exceptional-long-unsigned-deletion.md). Thus $M_\pm=(A_0\pm A_1)/2$ with the original squarefree and coprime tests and the original centered logarithmic mark. In $A_0$ the two unsigned labels are $(a,d)$ and in $A_1$ they are $(b,c)$. We retain both of the corresponding labels at most $S$ exactly, and show that the discarded part of (3) costs

$$
 O_\epsilon\!\left(
   Y^\beta G^C\mathbf1_{(N,r_o)=1}r^{-1+\epsilon}
   +Y^{\beta-c_1}\right)                                             \tag{4}
$$

for a fixed $c_1>0$.

Here are the details of carrying over and improving that deletion. Select an unsigned label $v>S$ in the original disjoint order and fix the other three labels of product $h$. The true support $m=hv\in V$ gives $h\ll Y^{9/10}$. The genuine product tests, the two lower gates, and the **minimum** upper gate leave at most two intervals in $v$, by separating its two upper branches and taking a disjoint union. The interval $hv\in V$ is just another linear test; there is no restriction $N-hv\in I$ here. The true one-variable mark is a bounded monotone ratio of affine logarithms, so after multiplication by $W(N-hv)$ it has sup plus variation $O(Y^{\beta-1}G^C)$ by Section 1.

Expand $c_t(n)=\sum_{d_0\mid(t,n)}d_0\mu(t/d_0)$, the mask $(v,h)=1$ by its divisor sum, and $\mu^2(v)=\sum_{b_0^2\mid v}\mu(b_0)$. The square-label tail $b_0>Y^{1/30}$ has the same positive floor bound $O(Y^{\beta-1}G^C (Y/h)Y^{-1/30})$ per fixed $h,t,d_0$, with the original unit mask restored before taking its absolute value. Summing triples reciprocally and the finite absolute $t,d_0$ weights by $Q_0^{O(1)}$ makes this a fixed power saving. For the remaining terms put $s=[a_0,b_0^2]$ with $a_0\mid h$ the unit label, and write $v=s(w_0+e_0j)$ on the exact congruence if it is solvable, where $e_0=d_0/(d_0,hs)$ is prime to $r$. The phase is $\chi(N-hsw_0-hse_0j)$. If some odd $p\mid r$ does not divide $hs$, its local complete mean is zero by affine bijectivity. CRT then makes full periods modulo $r$ zero. A partial interval and the exact BV weight cost $O(rY^{\beta-1}G^C)$ per $h,a_0,b_0,t,d_0$. As $h\ll Y^{9/10}$, there are at most $Y^{1/30}$ square labels, and $r,Q_0$ have subpower size, this is still a fixed power saving. These are pointwise-in-target arguments applying to the new genuine weight.

On every remaining expansion term $r_o\mid hs$, hence $r_o\mid m$ at its true integer values. If an odd $p\mid (N,r_o)$, then $\chi(N-m)=0$ on **all** these terms before any absolute bound, regardless of a deleted squarefree condition in the truncated expansion. Otherwise $(N,r_o)=1$ and $n=N-m$ is a genuinely coprime residue modulo $r_o$. At fixed $m\ne N$, keep the same positive Ramanujan envelope from the deletion proof: summing the absolute $t,d_0$ weights costs $O(G^C\tau(|n|)^2)$ since divisibility is of the true nonzero signed integer $n$. The genuine quadruple count and the extra expansion labels cost at most $\tau(m)^5$ as in that proof. It remains to bound

$$
 \sum_{\substack{m\in V\cap\mathbb Z\\m\ne N,\ r_o\mid m}}
             \tau(|N-m|)^2\tau(m)^5
          \ll_\epsilon (Y/r_o)G^C r_o^\epsilon
       \qquad ((N,r_o)=1).                                         \tag{5}
$$

Use Cauchy–Schwarz **within** this progression. For the sum of $\tau(m)^{10}$, write $m=r_ow$ and use $\tau(r_ow)\le\tau(r_o)\tau(w)$ and the usual elementary fixed divisor moment bound in $w\ll Y/r_o$. This costs $(Y/r_o)G^C\tau(r_o)^{10}$. For the other factor $\tau(|N-m|)^4\le\tau_{16}(|N-m|)$, split by the two signs of $N-m$. Both resulting classes are units. For any fixed $k$, a unit class $a\bmod q$ with $q\le Q_0$ has $\sum_{u\le4Y,\,u\equiv a(q)}\tau_k(u)\ll_k (Y/q)G^k$: in each ordered factorization select a largest factor in one of at most $k$ ways; the product $P$ of the others is at most $(4Y)^{1-1/k}$ and is coprime to $q$. The remaining variable has at most $4Y/(qP)+1$ choices. The reciprocal tuple sum costs $O(G^{k-1})$, and the ordinary tuple sum for the extra $1$ costs $O(Y^{1-1/k}G^{k-2})$ when $k\ge2$, absorbed since $q\le Q_0=Y^{o(1)}$; the case $k=1$ is immediate. These tuple bounds follow by iterating the ordinary harmonic sum. The inequality $\tau^4\le\tau_{16}$ and the analogous fixed moments follow by grouping prime-exponent choices or standard divisor convolution. Taking square roots and using $\tau(r_o)^5\ll_\epsilon r_o^\epsilon$ proves (5). Multiplying by $\|W\|_\infty$, the Ramanujan envelope and the outside $r/\varphi(r)$ now gives (4), with $r_o\ge r/8$. Zero never entered the shifted moment.

## 3. Apply the two ordinary poles on the full physical field

The remaining signed labels after Section 2 have the same lower bounds as in the all-target formula across the full $V$: each is at least $Y^{.39}$ for large $Y$. For color zero this follows from $D<\min(ab,ac)$ and $a\le S$; for color one it follows from $a>D/S$ and $d>\sqrt m/S$ by the actual minimum upper gate and $b,c\le S$. All these steps use only $m\asymp Y$. Keep the actual pairwise masks and the finite $t,q$ coefficients. At fixed short labels $u,v$ of product $h$, expand mutual coprimality of the two signed labels by $k$ and write them as $kz_1,kz_2$. The tail $k>Y^{1/100}$ has the same floor count $O(YG/(hk^2))$ per $h,k$, and Section 1's supremum replaces the old $O(Y^{\beta-1})$ by $O(Y^{\beta-1}G^C)$ only. For remaining $k$, both $z_i>Y^{.37}$ on the genuine discrete and real domains.

Use the exact full residues modulo $rq$ and the two ordinary masked Möbius pole formulas (4) of the all-target theorem. There are at most $Q_0^2$ residue pairs. For one fixed $z_i$ the other is confined to at most two true intervals with scale comparable to $Y/(hk^2z_i)$: the restriction $x=hk^2z_1z_2\in V$ is an interval and the same two upper branches apply. Compose $W$ with this affine relation and multiply by the actual centered mark; Section 1 gives supremum plus variation $O(Y^{\beta-1}G^C)$ on each slice. Apply the first pole via real endpoint summation by parts; interchange the resulting integral with the other finite sum; apply the second pole on the true remaining slices. The first error is summed with $1/z_i$, and the second with $\int_1^{4Y}z_i^{\beta-2}\,dz_i\ll G$, after extracting $(hk^2)^{-1}$ as in the all-target proof. The additional fixed powers of $Q_0$ from the residue and finite divisor expansions and all log factors still give $O(Y^\beta e^{-c_2\sqrt G})$ for some fixed $c_2>0$, since $\log Q_0=o(\sqrt G)$. Both uses of the pole are on the original signed arithmetic, not on any changed unit test. The weight $W$ remains exactly as in (3), on every slice including the allowed negative $N-x$ values.

The two pole densities have their original residue coefficients. The full $r$-residue contraction, including cancellation if $(hk,r)>1$, is unchanged since the tested weight is a function of the continuum variables only. Thus the exact contraction in Sections 2–3 of the all-target theorem yields the same multiplier $c_r(N)/\varphi(r)$. The local $q$ coefficients and the completion in $k$ are unchanged; the latter's power error is unchanged up to fixed log powers since $\sup|W|\ll Y^{\beta-1}G^C$. In changing real variables to $x=hk^2z_1z_2$, the weight $W(N-x)$ is independent of the remaining log variable. The two original real geometries of the [aligned two-pole formula](r92-spectral-aligned-exceptional-two-pole-formula.md), Section 4, used only $x\asymp Y$, the same cutoffs, and short labels at most $S$. They give exactly the same kernels $\mathcal G_i(x;u,v)$ at every $x\in V$. Thus after the double pole the finite principal term is the same $\mathcal D_i$ expression, with its full real support $V$ and with $W(N-x)$ in place of $F(N-x)$. No replacement at integer arguments, including near the hard endpoint of $I$, has been made.

## 4. Change to the genuine hard test only in the real model

For fixed short labels define the compact real test

$$
             g_i(x)=\mathbf1_V(x)x^{\beta-1}\mathcal G_i(x;u,v).
 \tag{6}
$$

Its sup plus variation is $O(Y^{\beta-1}G^C)$ uniformly. In color zero, the fixed log ratio $\rho=|\log(u/v)|$ and the positive moving cap $T_x=\log(x/D^2)$ give the kernel $-\rho\min(T_x,\rho)/(2\log x)$. The minimum is Lipschitz as a function of $T_x$, and $T_x$ varies by $O(1)$ on $V$. In color one, the geometric width is the positive part of $\frac12\log x$ minus a constant determined by the fixed short labels and cutoffs; its variation is $O(1)$. Its square and its product with the fixed $\rho$ are divided by $\log x\asymp G$. The endpoints of $V$ after zero extension and the smooth weight $x^{\beta-1}$ cost the same bound. This verifies compact-BV control at every seam without modifying any geometric domain.

By Plancherel in the real variable, the error from replacing $W$ by $F$ in each such real integral satisfies

$$
 \left|\int_{\mathbb R}(W-F)(N-x)g_i(x)\,dx\right|
 \ll Y^{2\beta-2}G^C\int_{|\eta|>\Delta_0}|\eta|^{-2}\,d\eta
 \ll Y^{2\beta-1}G^C Q_0^{-1}.                                    \tag{7}
$$

Here compact BV gives $|\widehat F(\eta)|\ll Y^{\beta-1}/|\eta|$ and $|\widehat g_i(\eta)|\ll Y^{\beta-1}G^C/|\eta|$ by distributional integration by parts. Reflection/translation by $N$ changes only phase and sign of frequency. Both functions are in $L^2$, and the product-tail estimate is absolutely integrable. This is an actual continuum pairing after extracting the arithmetic, not the earlier comparison of band-limited and hard integer samples. In the resulting hard real integral the support of $F(N-x)$ is exactly $N-I\subset V$. Individual endpoint representatives need not be chosen anew in this integral.

For each fixed short product $h$, (7) is independent of $t,q$. Combine the two local $q$-options for each allowed $t$ before taking absolute values, as in Section 4 of the all-target formula. Its zero-order finite-moment bound for the weighted short sum is $G^C Y^{(1-\beta)/5}$. The shared $r/\varphi(r)$ and derivative denominator there cost only a fixed log power. The contraction has already been applied, so multiplication by $|c_r(N)|/\varphi(r)$ is exact for this change. The resulting bound is

$$
      O\!\left(Y^\beta G^C \frac{|c_r(N)|}{\varphi(r)}
                  e^{-4(1-\beta)G/5}Q_0^{-1}\right).
 \tag{8}
$$

No tail in $t$ is introduced. Combine (4), the two-pole errors, and (8), and take the same signed parity half-sum as in (3). This proves (1). At $r\mid N$ the odd part of the actual growing Page conductor is nontrivial for sufficiently large $Y$ (the even part is bounded and the finitely many fixed conductors have no zeros arbitrarily close to one). At $c_r(N)=0$ the real principal term and the projection error both vanish, by the exact contraction before the BV comparison. The formula does not give a bound for the size of the signed finite real caps when the conductor aligns strongly and that multiplier is not small.
