# Flat numerator tests control most actual modes at large denominators

**Scope.** This estimates the actual signed exterior covariance, on the common fixed macro directions of R74, at most of a new and substantially larger collection of discrete modulus Fourier modes. The exceptional modes are determined by the true matrix field and need not lie in any prescribed set. The proof uses a square-root saving for flat linear combinations of the exact switched quotient incidences, and keeps all prime-power units, orientations, and the continuous benchmark. There is no bound for the energy on the exceptional modes, the full complement of the earlier collars, a prescribed modulus, or weak S.

## 1. Statements and the new frequency set

Use the same common transported parent basis, profiles $u,v\in\{h,f,g\}$, physical scales $4\le H<M\le Q^\Gamma$ with fixed $0<\Gamma<1$, and exact signed matrices $T_N^{u,v}$ as in [R76](r76-operator-joint-rational-numerator-variance.md) and [R77](r77-operator-common-shell-rational-packets.md). The matrices retain every positive alias and the two positive difference orientations and negative sum orientation; the equality line is removed in their exact centering. On the complete consecutive even shell $N=2m\in[Q,2Q]$, $m_0\le m\le m_0+J-1$, $J\asymp Q$, use

$$
 \widehat T(j)=J^{-1}\sum_m e(-j(m-m_0)/J)T_{2m}^{u,v},
              \qquad e(x)=e^{2\pi i x}.
 \tag{1}
$$

Let $\Pi$ be any fixed orthogonal projection on the common parent index space, of rank $r_*$. The physical basis vectors and their raw weights retain the same moving normalizers. Denote by $\mathcal C_+(B,R)$ the union of radius-$R$ circular index collars around the reduced rational centers $Ja/b$ with $\lceil B/2\rceil\le b\le B$, where $B\ge2$ is integer, $R\ge1$, and $BM\le Q/100$. Set $R_*=1+R$. Assume original local Dirichlet GRH at each even modulus in the shell and auxiliary Dirichlet GRH at every $q'\le\lceil8MB\rceil+2$, including $1$, as in R76.

For any $2\le S\le Q/100$ and any cutoff $\omega_S$ of the type in R77 (5) with two edge strips of total length $O(S)$, put $Z_{2m}=\omega_S(2m)T_{2m}^{u,v}$. Then

$$
 \begin{split}
 \sum_{j\in\mathcal C_+(B,R)}
         \|\Pi\widehat Z(j)\Pi\|_{\rm HS}
 \ll_{\Gamma,\Theta,\epsilon} Q^\epsilon r_*^2 B^2 R_*
     \left[\frac M Q R_*^2+
            \frac{\sqrt{M/Q}}{B}R_*+\frac M S\right].
 \end{split}
 \tag{2}
$$

Consequently, for any $\lambda>0$, the number of $j\in\mathcal C_+(B,R)$ with $\|\Pi\widehat T(j)\Pi\|_{\rm HS}>2\lambda$, for the actual sharp shell, is

$$
 \ll_{\Gamma,\Theta,\epsilon} Q^\epsilon
 \left[
    \frac{r_*^2B^2R_*}{\lambda}
       \left(\frac M Q R_*^2+
            \frac{\sqrt{M/Q}}B R_*+\frac M S\right)
      +\frac{S}{Q\lambda^2}
 \right].
 \tag{3}
$$


For an explicit example use the actual spatial parameters of [R74](r74-operator-fixed-macro-mean-all-modes.md), namely $H=Q^{2/5}$, $M=Q^{3/5}$, $W_V=Q^{23/175}V^{4/7}$ at each parent dyad, and its logarithmic-rank fixed true macro projection with any one fixed allowed logarithmic exponent, so $r_*\ll(\log(3Q))^C$ for a fixed $C$. Take

$$
 B=\lfloor Q^{39/100}\rfloor,\qquad
 R=\lfloor Q^{1/400}\rfloor,\qquad
 S=Q^{497/500},\qquad \lambda=Q^{-393/1000}.
 \tag{4}
$$

The auxiliary cap is $O(Q^{99/100})$. The set $\mathcal C_+(B,R)$ has $\asymp Q^{313/400}$ distinct modes, all outside both example sets of R77 and the older R73/R75 examples. Equation (3) bounds its actual sharp-shell exceptional count by $O_\epsilon(Q^{1563/2000+\epsilon})$. On the remaining modes, the RMS of the signed projection, in the normalized Fourier convention (1), satisfies

$$
 \left(\sum_{\substack{j\in\mathcal C_+(B,R)\\
          \|\Pi\widehat T(j)\Pi\|_{\rm HS}\le2\lambda}}
             \|\Pi\widehat T(j)\Pi\|_{\rm HS}^2\right)^{1/2}
          \ll Q^{-7/4000}.
 \tag{5}
$$

For $u,v\in\{h,f\}$, the same RMS estimate holds for the true projected prime Gram on this same good set, by the off-collar bound for the exact benchmark in [R75 (2)](r75-operator-prime-divisor-fourier-signature.md#1-statement-and-exact-indexing). In particular (5) does not use a proxy for the Gram, and (3) is an exceptional count in **Fourier modes**, not in the physical modulus $N$. One can take the union of exceptional sets over the bounded number of choices of actual masks if simultaneous good modes are desired.

## 2. The flat weighted quotient incidence

Here is the smooth arithmetic estimate underlying (2). For each fixed $b\le B$, let $\lambda_a$, over reduced numerators modulo $b$, be arbitrary complex numbers satisfying $|\lambda_a|\le b^{-1/2}$. In particular $\sum_a|\lambda_a|^2\le1$. For $\omega_0\in C_c^2((Q,2Q))$ write $K_1=\|\omega_0\|_\infty+\|\omega_0'\|_1$ and $K_2=\|\omega_0''\|_1$. We prove

$$
 \left\|\sum_{a\bmod b}^{*}\lambda_a
      \sum_{2\mid N}\omega_0(N)e(aN/(2b))T_N^{u,v}\right\|_{\rm HS}
 \ll_{\Gamma,\Theta,\epsilon}Q^\epsilon
       \big[(\sqrt b\,M+b^{-1/2}\sqrt{QM})K_1
                         +\sqrt b\,QM K_2\big].
 \tag{6}
$$

This is not an estimate of the full numerator vector in $\ell^2$; its gain uses the flatness condition on the test, and it is uniform over all its possible phases.

In R76's switch on one dyad pair $V\le U$, one fixed alias $k\le4U$, and one orientation $(\sigma_1,\sigma_2)$, set $q=2k,\ q'=qb$. Its twisted incidence on the unit residues modulo $q'$ is the compression of the full residue matrix

$$
 (A_a)_{r,s}
   =\mathbf1_{q\mid\sigma_1r+\sigma_2s}
                       e\big(a(\sigma_1r+\sigma_2s)/q'\big),
       \qquad r,s\bmod q'.
 \tag{7}
$$

The raw derivative in the two centered errors is common to all $a$, since the rational factor is in (7).

To estimate the weighted incidence before the unit compression, split its row and column residue sets according to $r_0,s_0\bmod q$. Each $r_0$ matches exactly one $s_0\equiv-\sigma_1\sigma_2r_0\bmod q$, and the matching is a bijection. Write $r=r_0+qv,\ s=s_0+qw$, with $v,w\bmod b$, and $c_0=(\sigma_1r_0+\sigma_2s_0)/q$ for the chosen representatives of the matched block. On this block (7) equals

$$
        e(ac_0/b)\,e(a\sigma_1 v/b)\,e(a\sigma_2 w/b).
$$

For different $a\bmod b$, the unit-normalized left Fourier vectors $b^{-1/2}e(a\sigma_1 v/b)$ are orthogonal, and the right vectors $b^{-1/2}e(-a\sigma_2w/b)$ are orthogonal as well. In each matched block, the singular values for the linear combination $\sum_a\lambda_a A_a$ are therefore $b|\lambda_a|$, with zero for unused numerators. Distinct matched blocks have orthogonal supports on both sides. Restricting rows and columns to units does not increase operator norm, and gives

$$
           \left\|\sum_a\lambda_a A_a\right\|_{\ell^2\to\ell^2}
                   \le b\max_a|\lambda_a|\le\sqrt b .
 \tag{8}
$$

No coprimality condition between $b$ and $q$ is needed for (8). This is the square-root gain over bounding individual incidence matrices or taking the full joint numerator norm in R76 (7).

Apply (8) after the twice-centered partial integrations used in R76 (8): for fixed $x,y$ the two residue vectors are the actual $F_{q',r}(x)=\psi(x;q',r)-x/\phi(q')$ on units, and likewise at $y$. Their GRH bounds and the same common mixed derivative (R76 (5)) give the right side of R76 (8) with $b$ replaced by $\sqrt b$. This follows from the complex operator norm (8) even if the bilinear expression is written with a transpose, since its absolute value is bounded by the product of Euclidean norms. The single errors use the R76 joint numerator bound (9), followed by Cauchy with $\|\lambda\|_2\le1$. Their factor $b^{-1/2}$ is unchanged. Both temporary unit restorations from R76 §1 use their scalar bounds times $\sum_a|\lambda_a|\le\sqrt b$, hence have the same improved denominator size as the double error. This includes either raw leg with the original $N$-nonunits and either raw leg with the temporary $q'$-nonunits. We have not modified which terms appear in the final prime-power sums.

## 3. Flat geometric sums and the exact model restoration

Use the exact singular-series divisor expansion for the continuous line of R76 §2. For one $d\mid m$ in the expansion, after setting $m=dn$, the phase factor is $e(adn/b)$. Let $K$ be the supremum plus variation of the common weight $\omega_0(t)I_k(t)$ there, so on one entry $K\ll QV b_I b_{I'}K_1$. If $b\mid d$, the phase is constant, the lattice-to-integral error is $O(K)$ per numerator, and its weighted sum costs $O(\sqrt b K)$. If $b\nmid d$, let $s=b/(b,d)>1$. The summation-by-parts bound for a geometric progression is $O(K/\operatorname{dist}(ad/b,\mathbb Z))$. As $a\bmod b$ runs over reduced numerators, none of the residues $a(d/(b,d))\bmod s$ is zero, and each appears at most $b/s$ times. Consequently

$$
  \sum_a\frac{|\lambda_a|}{\operatorname{dist}(ad/b,\mathbb Z)}
       \le b^{-1/2}\frac b s
                     \sum_{r=1}^{s-1}\operatorname{dist}(r/s,\mathbb Z)^{-1}
       \ll \sqrt b\,\log(2b).
 \tag{9}
$$

Thus the combined nonresonant lattice error is $O(\sqrt b K\log(2b))$, not the $O(bK)$ in the full joint numerator estimate.

The principal coefficient on each orientation is the one already matched exactly in [R73](r73-operator-rational-modulus-collars.md) (12), as used in R76 §2: $k/(\phi(2k)\phi(b)^2)$ if $b$ is squarefree and $(b,2k)=1$, and zero otherwise. This equality is true before the sum in $a$, so multiplying by the same scalar tests on both sides keeps the equality with the true singular-series model. Summing the errors (9) and the $b\mid d$ floors over the actual divisors costs $O_\epsilon(Q^\epsilon\sqrt b K)$ by the pointwise divisor weight $\rho(d)\ll_\epsilon d^{-1+\epsilon}$. Extending the resonant sum to $d>2Q$ costs at most the same, using the common integral $O(QK)$ and $\sum_{d>2Q}\rho(d)/d\ll_\epsilon Q^{-1+\epsilon}$. This handles the continuum without assuming it stationary or dropping an original affine sign.

Now sum over $k$ and the physical dyad pairs and aggregate entries as in R76 §3. The factor $b_Ib_{I'}$ costs $O((Q\sqrt{VU})^{-1})$ in HS, by square summation in the two parent indices. The double error is $O_\epsilon(Q^\epsilon\sqrt b(UK_1+QV K_2))$ per dyad pair after the harmonic sum in $k$. The single errors are $O_\epsilon(Q^\epsilon b^{-1/2}\sqrt{QU}K_1)$; the model and the unit restorations are bounded by the displayed double-error envelope. Sum the three signed orientations and use $V,U\le M$, absorbing the dyad count in $Q^\epsilon$, to prove (6).

## 4. Actual nearest modes and phase duality on the fixed macro space

Fix $b$, let $j_0(a)$ be a nearest integer to $Ja/b$, and set $s_a=j_0(a)-Ja/b$, $|s_a|\le1/2$. As in R77 §3 use $x(t)=(t/2-m_0)/J$, so for $j=j_0(a)+\ell$ the phase in (1) is, up to $e(a m_0/b)$, the product $e(-am/b)e(-\ell x(2m))e(-s_a x(2m))$. In the power series for the last factor the coefficients $s_a^n$ can multiply the flat scalar tests in (6) at a cost at most $2^{-n}$ in their sup norm. The constant phase of absolute value one also preserves their bound. Use the common cutoff test
$\omega_S(t)e(-\ell x(t))(-2\pi i x(t))^n/n!$
in each term, and the R77 (7) derivative sums $O(1+|\ell|)$ for $K_1$ and $O(S^{-1}+(1+|\ell|)^2/Q)$ for $K_2$. Reverse the numerator labels for the sign of the exponential; this is a permutation of the set and preserves flatness. In (6) divide by $J\asymp Q$. The result, with $G_a=\Pi\widehat Z(j_0(a)+\ell)\Pi$, is

$$
 \left\|\sum_a\lambda_aG_a\right\|_{\rm HS}
 \ll Q^\epsilon\left[
    \sqrt b\,\frac M Q (1+|\ell|)^2
      + b^{-1/2}\sqrt{\frac M Q}(1+|\ell|)
      + \sqrt b\,\frac M S\right].
 \tag{10}
$$

Here compression is a contraction, and the tests may have different phases at every numerator. All these operations are applied to the exact tapered shell, not to its edge error.

Use any fixed orthonormal basis of the $r_*$-dimensional projected space. For an entry $G_a(i,j)$, take $\lambda_a=b^{-1/2}\overline{G_a(i,j)}/|G_a(i,j)|$ when that entry is nonzero, and zero otherwise. This is allowed by the uniformity of (10); the phases may depend on the actual field. The same entry of $\sum_a\lambda_aG_a$ is $b^{-1/2}\sum_a|G_a(i,j)|$. Since $\|G_a\|_{\rm HS}\le\sum_{i,j}|G_a(i,j)|$, summing this scalar duality over the $r_*^2$ entries gives

$$
 \sum_a\|G_a\|_{\rm HS}
 \ll Q^\epsilon r_*^2
 \left[b\,\frac M Q(1+|\ell|)^2+
              \sqrt{\frac M Q}(1+|\ell|)
                    +b\,\frac M S\right].
 \tag{11}
$$

This use of the fixed low macro rank matters; (11) with that dimension factor would be weaker on an arbitrary very large space.

Every mode in the selected collars is a $j_0(a)+\ell$ with $|\ell|\le R+1$ modulo $J$ for its denominator. Count overlaps only to increase the sum. Summing (11) over these shifts and over $\lceil B/2\rceil\le b\le B$ proves (2). In particular $\sum b=O(B^2)$ on this denominator range and the three shift sums are $O(R_*^3)$, $O(R_*^2)$, and $O(R_*)$. It would be incorrect to substitute the improvement for flat tests into the full numerator $\ell^2$ bound; (11) is an $\ell^1$ estimate obtained by this explicit entrywise duality.

Finally let $W_{2m}=(1-\omega_S(2m))T_{2m}^{u,v}$ be the single edge field. As in R77 (6), full normalized Parseval and the actual local-GRH pointwise envelope of [R72 §1](r72-operator-principal-modulus-low-modes.md#1-exact-fixed-supports-and-parameter-envelopes) give

$$
 \sum_{j\bmod J}\|\Pi\widehat W(j)\Pi\|_{\rm HS}^2
                   \ll_\epsilon Q^\epsilon S/Q.
 \tag{12}
$$

Markov's inequality with (2) counts those modes where $\|\Pi\widehat Z(j)\Pi\|_{\rm HS}>\lambda$, and (12) counts those where the analogous sharp edge coefficient exceeds $\lambda$. Since $T=Z+W$ on the literal shell, their union contains the full exceptional set at threshold $2\lambda$. This proves (3). In particular its count concerns the true sharp-shell coefficients, and the cutoff sets no restriction on the final shell.

## 5. Exponents, mode count, and the remaining variance

At (4), the three terms in the bracket of (2) have powers respectively $-79/200$, $-47/80$, and $-197/500$; the last dominates. The first term of the counting bound (3), with logarithmic rank absorbed in $Q^\epsilon$, has power $313/400-197/500+393/1000=1563/2000$. The edge count has power $497/500-1+2(393/1000)=39/50$, which is smaller. In particular for fixed sufficiently small $\epsilon>0$, a fraction tending to one of the tested modes is good.

The total cardinality follows by the elementary totient sum in R77 §4: the number of reduced centers is $\asymp B^2$. Any distinct rational centers with denominators at most $B$ are separated by at least $J/B^2\asymp Q^{11/50}$ in circular index distance, much greater than both $R$ and any of the radii of the earlier examples. All selected denominators grow like $Q^{39/100}$ and hence are strictly beyond the high R77 packet of order $Q^{9/25}$ as well as the older uniform denominator caps. This proves both $\asymp B^2 R_*$ cardinality and disjointness from the earlier examples. On the good set the norm of every true coefficient is at most $2\lambda$; thus its total Fourier RMS is at most $O(\lambda B\sqrt{R_*})=O(Q^{-7/4000})$, proving (5).

For the actual prime Gram on the same modes, use the exact identity $P=T+(D+K)$. These modes are all off the R75 collars, so its benchmark RMS is $O_\epsilon(Q^{-3/80+\epsilon})$ for $h,h$ and $O_\epsilon(Q^{-1/50+\epsilon})$ if a body leg is present, both smaller than (5). This shows genuine arithmetic control on the stated good set. The excluded $O_\epsilon(Q^{1563/2000+\epsilon})$ modes may still carry substantial energy; no conclusion is made about them or the untested sparser rational and nonrational parts of the true Fourier field.
