# A negative signed arithmetic sector in the retained exterior Gram

**Scope.** The $n=m$ diagonal of the actual long-divisor arithmetic Gram is too large to compare by unsigned pieces. On at least one retained coarse direction its distinct-integer complement is necessarily large and negative. This is not the same-copy or distinct-copy zero diagonal, and it supplies no norm bound or counterexample for the original $T_N$.

Let $N$ be sufficiently large and even, $L=\log N$, $\ell=\log L$, $\alpha=1/L$, and $\beta=1/8$. Use actual physical $L^2(du)$, with

$$
 r_N(u)=u^{-3/2}\big((Nu)^{-2\alpha}+(Nu)^{-2\beta}\big)^{1/2}.
$$

Fix $K>0$, an arbitrary $0<\eta<1$, and $\mathsf A>2K+5,\ \mathsf B>K+4,\ C_0>K+3$ as in the [exterior linear cutoff](r38-operator-exterior-linear-type-i.md). Let

$$
 q_0=N\exp(-C_0\ell^2/\log\ell),\qquad
 (K+3)\ell^2/\log\ell\ \le H\le L^{1-\eta},\qquad Y=e^H .
$$

For the dyads $V=2^jY$, $j\ge0$, choose the maximal common R38 cutoff

$$
 D_V=\left\lfloor\min\{VL^{-\mathsf A},\sqrt{q_0}L^{-\mathsf B}\}\right\rfloor.
$$

On each such dyad, put $\Lambda_{>D_V}(n)=\Lambda(n)-\sum_{d\mid n,\ d\le D_V}\mu(d)\log(n/d)$. Let $t_\chi$ be the exact remaining exterior atom with this coefficient in place of $\Lambda(n)$. Use the total odd-family normalization, writing $\mathbb E_{\rm odd}$ for the average over every odd character modulo $N$, and put $\mathcal F=\{\chi\ {\rm odd}:q_\chi\ge q_0\}$.

There is a fixed $C>1$ such that, for the union $W$ of the whole physical dyads contained in $[Y,e^{CH}]$, the following holds under original local GRH. Write $P^{>}$ for the true long-divisor covariance on $W$, the average of $({\bf1}_Wt_\chi)\otimes({\bf1}_Wt_\chi)$ over $\mathcal F$ with total odd-family denominator. Let $D^{>}_{\rm int}$ denote its exact $n=m$ integer-equality term, and put $O^{>}_{\rm int}=P^{>}-D^{>}_{\rm int}$. Then there is a dyad $I_V=[V,2V)\subseteq W$ whose genuine normalized coarse mean $g_V=r_N{\bf1}_{I_V}/\|r_N{\bf1}_{I_V}\|_2$ satisfies

$$
 \left\langle O^{>}_{\rm int}g_V,g_V\right\rangle\le -cL^2/H
 \tag{1}
$$

with $c>0$ uniform in $N,H$ in the stated range. Since $\log I_V$ has length $\log2$, the [logarithmic separation mask](r31-operator-zero-diagonal.md) makes no difference to this Rayleigh test; $g_V$ lies in the [actual exterior coarse projection](weak-s-exterior-fine.md) for exterior $Y$. The asserted sign is for the signed sum over distinct integers, not for either sign alone, and not for the Gram minus the *original* stationary benchmark.

## 1. Exact same-family operators and orthogonal tests

Let $\rho=\mathbb E_{\rm odd}{\bf1}_{\chi\in\mathcal F}=1-o(1)$ by the [conductor-defect cutoff](r33-operator-conductor-defect.md). For each $n\le N\sup W$ with $(n,N)=1$, define

$$
 a_n(u)=-\frac{\sqrt{2\pi}\sqrt n}{N}\,
        r_N(u)\,{\bf1}_{u\in W,\ n\le Nu}\Lambda_{>D_V}(n),
 \qquad u\in I_V .
$$

The coefficient with $D_V$ is interpreted on the dyad containing $u$; off $W$ the function is zero. On $W$ the exact atom is $\sum_n\chi(n)a_n$. In particular

$$
 D^{>}_{\rm int}=\rho\sum_n a_n\otimes a_n,\qquad
 O^{>}_{\rm int}
   =\mathbb E_{\rm odd}{\bf1}_{\chi\in\mathcal F}
                    \sum_{n\ne m}\chi(n)\overline{\chi(m)}\,a_n\otimes a_m .
 \tag{2}
$$

These are finite sums. The factor $\rho$ is exact because each $n$ retained here is a unit of $N$. No full-family orthogonality is applied to the high-conductor subset. Under original local GRH, the full atom trace bound gives $\mathbb E_{\rm odd}\|p_\chi\|_2^2\ll L^2$. The R38 bound for the deleted atoms, in the same space and normalization, therefore yields

$$
 \operatorname{tr}P^{>}
 =\mathbb E_{\rm odd}{\bf1}_{\chi\in\mathcal F}
                           \|{\bf1}_Wt_\chi\|_2^2
 \le C_1L^2
 \tag{3}
$$

with an absolute $C_1$ for all sufficiently large $N$ at the fixed parameters, independently of $C$. This uses positivity of the actual full long-divisor Gram, not positivity of its distinct-integer part.

The functions $g_V$ for the distinct dyads in $W$ are orthonormal. Each is a linear combination of the mean profiles $r_N{\bf1}_I$ on the constituent R30 cells, since those cells partition its entire dyad with the same starting $Y$. For fixed $C$, $\log V\le CH=o(L)$, so $\|r_N{\bf1}_{I_V}\|_2^2\asymp V^{-2}$ uniformly. The cap in $D_V$ is inactive on this range: $\sqrt{q_0}L^{-\mathsf B}=N^{1/2-o(1)}$ and $V\le e^{CH}=N^{o(1)}$. Also $\log D_V\asymp\log V$ since $\log V\gg\ell$.

## 2. Elementary lower bound for the diagonal inflation

On a dyad let $X=NV$, $D=D_V$. We claim the number of integers $n\in(X/2,X]$ coprime to $N$, with all prime factors $>D$, and not prime powers is $\gg X/\log D$.

Here a direct lower sieve suffices. Set $S=\sum_{p\le D}1/p\ll\log\log(3D)\ll \ell$ by Chebyshev and partial summation. Choose an odd Bonferroni order $k$ of size a sufficiently large fixed multiple of $\ell$, so that
$\sum_{j>k}S^j/j!\ll L^{-5}$; this follows from $j!\ge(j/e)^j$ and the geometric tail after $k>S$. The density obtained from the truncated reciprocal inclusion–exclusion differs from $\prod_{p\le D}(1-1/p)$ by at most this last error, since the $j$th elementary symmetric sum of $1/p$'s is at most $S^j/j!$. The counting remainder on $(X/2,X]$ from the floors is $O((k+1)D^k)=\exp(o(L))$, since $k\ll\ell$ and $CH\ll_C L^{1-\eta}$. The reciprocal Euler product is $\gg 1/\log D$: take $\sigma=1/\log D$, compare its inverse to the product with $1/p^{1+\sigma}$, and use

$$
 \prod_{p\le D}(1-p^{-1})^{-1}
 \le \zeta(1+\sigma)\exp\!\left(O\!\left(\sigma\sum_{p\le D}(\log p)/p\right)\right)
 \ll \log D .
$$

Here the logarithmic prime sum is $O(\log D)$ by Chebyshev and partial summation. Thus the odd Bonferroni lower bound gives $\gg X/\log D$ integers avoiding all primes $\le D$.

Primes dividing $N$ that are $>D$ account for at most $O(XL/D+L)=o(X/\log D)$ excluded integers, using at most $O(L)$ distinct prime divisors and the superpolylogarithmic lower bound for $D$. All primes through $X$ number $O(X/\log X)$, and proper powers number $O(\sqrt X\log X)$. Both are $o(X/\log D)$ since $\log D=o(L)$ and $\log X\asymp L$. This proves the claim, uniformly on the selected dyads.

For every integer counted in the claim, its only divisor $\le D$ is $1$, and $\Lambda(n)=0$; hence $\Lambda_{>D}(n)=-\log n$ exactly. Its cutoff $n\le Nu$ is in force throughout $I_V$. Consequently

$$
 |\langle a_n,g_V\rangle|^2
 =\frac{2\pi n}{N^2}|\Lambda_{>D}(n)|^2\,\|r_N{\bf1}_{I_V}\|_2^2
 \gg \frac{L^2}{NV}.
$$

Summing these genuine terms in (2), and using $\rho\ge1/2$, gives

$$
 \langle D^{>}_{\rm int}g_V,g_V\rangle
 \ge c_0\frac{L^2}{\log V}.
 \tag{4}
$$

The lower estimate (4) is independent of GRH; the comparison (3) uses local GRH.

## 3. Negative complement on a retained mean mode

Let $J=\lfloor (C-1)H/\log2\rfloor$, the number of selected whole dyads. Their sum in (4) is at least

$$
 c_0L^2\sum_{j=0}^{J-1}(H+j\log2)^{-1}
 \ge \frac{c_0L^2}{\log2}\big(\log C-o(1)\big).
$$

Choose the fixed $C$ sufficiently large that this exceeds $(C_1+1)L^2$ for all large $N$. By orthonormality, the sum over these same $g_V$'s of the true positive Gram's Rayleigh quotients is at most (3). Thus the sum for $O^{>}_{\rm int}$ is at most $-L^2$. Since $J\ll_C H$, one of its quotients is at most $-cL^2/H$, proving (1).

This is a quantified obstruction to treating every integer-equality contribution of the long-divisor convolution as its positive main term while claiming all signed aliases are small. It does not exclude cancellation between those two arithmetic parts (it requires it), and says nothing about the remaining comparison of their sum with the R31 same-copy benchmark. Neither weak S nor any unsmoothed bound on $T_N$ follows.

## 4. Full odd-family corollary: literal signed congruence aliases on this strip

On the same finite $W$, the conclusion holds also for the full odd-family long-divisor Gram with the same $D_V$. In that case (2) has $\rho=1$, and the coefficient for $(nm,N)=1$ is exactly

$$
 {\bf1}_{n\equiv m\pmod N}-{\bf1}_{n\equiv -m\pmod N}.
$$

Thus the negative operator sector in (1) can be taken to be the literal signed two-alias sum over $n\ne m$, not only the high-conductor restriction.

To see why the full-family trace is still $O(L^2)$ on this strip, set $q_c=e^{3CH}=N^{o(1)}$ and choose the same $D_V$ on $W$, with zero cutoffs on the later dyads. These choices fit the R38 cap with threshold $q_c$, since $D_V\le V\le e^{CH}\ll\sqrt{q_c}L^{-\mathsf B}$. So the deleted-atom squared budget from conductors at least $q_c$ is $o(L^{-2K-2})$. The fraction of odd characters with conductor below $q_c$ is at most $2\sum_{q\le q_c}\phi(q)/\phi(N)=N^{-1+o(1)}$. For each of these characters, the uniform per-character dyad estimate from the [previous exterior Type-I bound](r34-operator-exterior-type-i.md) gives squared deleted-atom norm $O(L^2(1+V))$ on $I_V$, using $D_V\le V$ and $\log(2NV)\asymp L$. Summing the $O_C(H)$ selected dyads costs $N^{o(1)}$ per character, so their contribution to the full average is negligible. Thus (3) holds for the full family as well, with a common absolute trace constant after increasing $C_1$ if needed. The identical test and diagonal argument proves (1) after choosing $C$ with that common constant. This additional full-family argument is valid only on the displayed finite strip, not an extension of the cutoff on arbitrarily late dyads.
