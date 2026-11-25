# The actual exceptional residue confined near the square-root scales

**Scope.** This unconditionally sharpens the [long-unsigned deletion](r91-spectral-exceptional-long-unsigned-deletion.md) for the genuine hard Page-character correction of both mixed-strip parities. The surviving signed legs are within a subexponential factor of the square root. A conductor-dependent threshold is given, uniformly in actual even targets and hard tests. The result does not estimate the remaining two signed legs, remove an ultra-close exceptional correction on a prescribed complete planting, or imply Hypothesis S.

Keep the exact notation of the long-unsigned deletion: $Y\le N\le2Y$, $G=\log Y$, $L=\log N$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, left interval $I$ and actual pointwise-BV $\omega$, right $m=N-n$, hard $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$. When there is a primitive real Page character $\chi^*$ of conductor $r\le Q_0$ with real zero $\beta$, use the exact hard functional $\mathcal H$ of that proof and put $H=Q_0/r$. Recall that $A_0=M_>$ and $A_1=\mu(m)M_>$ are its true unsigned/signed decompositions before the two parity projectors: the signs are respectively $\mu(b)\mu(c)$ and $\mu(a)\mu(d)$ on squarefree pairwise coprime $m=abcd$, with the exact gates $D<\min(ab,ac)<\sqrt m$, $abc>H_0$ and centered mark $1-2\log(ac)/\log m$.

For a real $U\ge1$, let $A_{0,U}$ retain $a,d\le U$ in $A_0$, and $A_{1,U}$ retain $b,c\le U$ in $A_1$. These are exact gates on each tuple with its original order and weight. For the original correction set $\mathfrak E_\pm=0$ in the absence of the Page character.

**Theorem.** For every real $\sqrt r\le U\le Y^{1/10}$, the contribution of each discarded actual array satisfies, with a fixed constant $C$,

$$
 \left|\mathcal H(A_i-A_{i,U})\right|
 \ll Y^\beta G^C
       \left(\frac{Q_0}{r^{3/4}\sqrt U}+\frac1{\sqrt r}\right)
                           \qquad (i=0,1).                         \tag{1}
$$

Thus one can take the single conductor-dependent threshold $U=Q_0^2/r\le e^{32Z}$ and, for every fixed $A>0$, write the actual original correction as

$$
        \mathfrak E_\pm
     =\tfrac12\bigl(\mathcal H(A_{0,U})\pm\mathcal H(A_{1,U})\bigr)
                 +O_A(YG^{-A}).                                    \tag{2}
$$

At a fixed requested $A$, one can instead take $U=Q_0^2 r^{-3/2}G^{C_A}$ with $C_A$ sufficiently large. For each of the remaining two signed factors $v$, in either array the actual product and midpoint tests give

$$
       \frac{\sqrt Y}{U L^B}\ll v\ll\sqrt Y\,U L^B .                 \tag{3}
$$

All estimates are uniform in $N$ and in the original hard tests; (2) imposes no new exceptional set on them. The no-Page case is interpreted as an identity of zero corrections.

## 1. A uniform incomplete affine character sum

Write $r=2^e r_{\rm odd}$; $2^e\le8$ and $r_{\rm odd}$ is squarefree by the primitive real character classification in the deletion proof. For integers $a,b$, put $r_u=\prod_{p\mid r_{\rm odd},\,p\nmid b}p$. Suppose $r_u>1$. For any interval of consecutive integers, the sum of $\chi^*(a+bj)$ over that interval is

$$
                         O(\sqrt{r_u}\log(2r_u)).
                                                                    \tag{4}
$$

Indeed, each odd prime of $r$ which divides $b$ gives a constant local factor, which may be zero. Split $j$ into its at most eight residue classes modulo $2^e$ to make its $2$-factor constant as well. On one such progression, for each remaining prime the argument is affine with invertible coefficient. The product of the nonprincipal local factors is the primitive character $\chi_u\bmod r_u$ evaluated at an affine function of the new consecutive progression index, with invertible linear coefficient modulo $r_u$. Multiplicativity therefore replaces it by a constant times $\chi_u$ of a shifted consecutive index.

For completeness, the finite Fourier transform of $\chi_u$ has absolute value at most $\sqrt{r_u}$ at every frequency, and its constant coefficient is zero. On an odd prime this follows from additive orthogonality, since all nonzero frequency magnitudes are the same by multiplication by units and the zero frequency vanishes. The product over the primes follows by the Chinese remainder theorem. Remove complete periods of $\chi_u$, and expand the remainder by finite Fourier inversion. For a frequency $h\ne0\bmod r_u$, the geometric sum over a consecutive interval of length at most $r_u$ is $O(\min(r_u,1/\|h/r_u\|))$, and the sum of these bounds over $h$ is $O(r_u\log(2r_u))$. With the inverse Fourier factor $r_u^{-1}$ this proves (4).

The bound is independent of the affine constant $a$, so applies without $r\mid N$. It remains valid, multiplied by the supremum plus pointwise variation, for any real hard test on the interval, by summation by parts on the actual sampled points. If $r_u=1$, no cancellation is asserted.

## 2. Take the absolute Ramanujan budget before balancing two genuine errors

Fix $i$, and select the first unsigned variable $v>U$ as in the original disjoint deletion, fixing the other three of product $h\le2Y/U$. The actual interval in $v$ is the union of at most two hard intervals, via the original minimum (not an intersection of upper midpoint tests). The other variables and earlier gates are fixed. The full real test $\omega(N-hv)(N-hv)^{\beta-1}(1-2\log(ac)/\log(hv))$ has norm $O(Y^{\beta-1})$ by the same bounded-variation argument on each actual interval.

In the genuine finite Ramanujan factor use $c_t(n)=\sum_{d_0\mid(t,n)}d_0\mu(t/d_0)$, retaining $t\le H$, $(t,r)=1$ and only squarefree $t$. This time the total absolute coefficient budget without restricting $n$ is

$$
  \sum_{\substack{t\le H\\t\ {\rm sf}}}\frac{\sigma(t)}{\varphi(t)}
    \ll H .
                                                                    \tag{5}
$$

For squarefree $t$ the ratio is $\prod_{p\mid t}(1+2/(p-1))$. Expand this as a positive divisor sum, and bound each number of multiples of the divisor $d$ by $H/d$. The resulting Euler bound is $\prod_p(1+2/[p(p-1)])<\infty$, proving (5) for all real $H\ge1$. This bound is used for the summation errors, **not** to estimate the genuinely thin noncancelling terms by the number of possible $t$.

Expand the exact coprimality $(v,h)=1$ by $a_0\mid h$ and impose $a_0\mid v$. Expand $\mu^2(v)$ by $b_0^2\mid v$, with coefficients $\mu(a_0),\mu(b_0)$. For an integer square cutoff $J\ge1$, the size of the $b_0>J$ part, **with the original unit test restored before the absolute bound**, is at fixed $h,t,d_0$ at most $O(Y^{\beta-1}(Y/h)/J)$: the unrestricted upper count is $\sum_{b_0>J}\lfloor2Y/(h b_0^2)\rfloor$. Summing the actual other triples by $\tau_3(h)$ and its harmonic sum $O(G^3)$, then using (5), yields

$$
                     O(Y^\beta G^C H/J).                           \tag{6}
$$

For $b_0\le J$ put $s=[a_0,b_0^2]$ and write $v=sw$. The true congruence $d_0\mid N-hv$ is empty or one residue class for $w$ modulo $e_0=d_0/(d_0,hs)$, prime to $r$. In that class, the affine coefficient for the character is $-hs e_0$. Whenever not all odd conductor primes divide $hs$, (4) and summation by parts therefore give $O(Y^{\beta-1}\sqrt r\log(2r))$ at fixed $h,t,d_0,a_0,b_0$. There are at most $J\tau(h)$ pairs $(a_0,b_0)$ at each $h$. The point is to **average** $\tau_3(h)\tau(h)$ over $h\le2Y/U$: since $\tau_3(h)\tau(h)\le\tau(h)^3\le\tau_8(h)$, this costs $O((Y/U)G^7)$, with the same true support. Now (5) gives

$$
                    O(Y^\beta G^C H\sqrt r\,J/U).                  \tag{7}
$$

The fixed $G^C$ in (6)--(7) absorbs $r/\varphi(r)$ and $\log(2r)$. No subpower losses in $Y$ have been used against the subexponential cutoff.

For all other retained $b_0$ terms, every odd conductor prime divides $hs$, hence $r_{\rm odd}\mid m$ on their exact integer support. The rare-class argument (3)--(4) of the long-unsigned deletion does not depend on the size of either the unsigned or square cutoff. More explicitly, restore the count by actual $n=N-m$ first. At fixed $n$ the absolute sum of the Ramanujan divisor coefficients is $O((\log(2Q_0))\tau(n)^2)$, by extending its positive local Euler factors. The count of quadruples and both auxiliary divisors at fixed $m$ is at most $\tau_4(m)\tau(m)^2\le\tau(m)^5$. Cauchy on the class $r_{\rm odd}\mid N-n$ and the genuine full-interval fixed divisor moments give $O(Y^\beta G^C r_{\rm odd}^{-1/2})$, hence $O(Y^\beta G^C r^{-1/2})$ since $r_{\rm odd}\ge r/8$. No extra target-unit condition is inserted, including on off-squarefree terms of this truncated expansion.

Take $J=\lfloor\sqrt U/r^{1/4}\rfloor$, at least one and within a factor two of its unfloored value under the hypothesis $U\ge\sqrt r$. The sum of (6)--(7) is $O(Y^\beta G^C Q_0/(r^{3/4}\sqrt U))$. Together with the genuine rare class this proves (1).

## 3. Return to the original exceptional correction

When $U=Q_0^2/r$, the first term in (1) is $r^{-1/4}$. The bound $r>G^J$ eventually for each fixed $J$ for this Page choice follows by classical Siegel as used in the [all-scale reduction, §1](r87-spectral-all-scale-exceptional-left-reduction.md#1-remove-only-multiples-of-the-exceptional-conductor-in-the-auxiliary-calculation). Thus both terms give arbitrary inverse-log gain, with no lower bound on $(1-\beta)G$. With $U=Q_0^2r^{-3/2}G^{C_A}$ the first term is $G^{-C_A/2}$; both values of $U$ lie between $\sqrt r$ and $Y^{1/10}$ for the declared large dyads, using $r\le Q_0$.

The [literal hard transfer](r88-spectral-hard-exceptional-residue-transfer.md) is applied only to the full original $M_\pm=(A_0\pm A_1)/2$, with its own $O_A(YG^{-A})$ error. Then subtract the discarded **actual** coefficient sums by (1) to obtain (2); there is no use of that transfer on a new independent tuple gate. In $A_{0,U}$, $a,d\le U$ implies $b,c>D/U$. In $A_{1,U}$, $b,c\le U$ implies $a>D/U$ and $abc<\sqrt m\max(b,c)\le\sqrt m\,U$, hence $d>\sqrt m/U$. Their respective upper bounds in (3) follow by the product $m\asymp Y$ and the lower bound on the other signed leg. This confines the correction to its stated near-square-root regions, not a proof that the remaining $\mu$-weighted legs cancel.
