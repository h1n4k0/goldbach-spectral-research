# Even-conductor deletion for the unrestricted actual exceptional parity difference

For the original mixed-strip exceptional term, the genuinely long unsigned sectors have an additional exact cancellation whenever the actual Page conductor is even. This holds at every even target, including those coprime to the entire odd part of that conductor. Consequently the original unrestricted exceptional parity difference, subject to the same near-zero and finite-cap assumptions as before, admits the conditional sign and lower bound without odd overlap in the even-conductor case. This says nothing about the existence of a qualifying zero, either total mixed-strip parity, prime pairs or Hypothesis S.

Use the genuine exceptional integrals $\mathfrak E_\pm(N;I,\omega)$ of the [all-scale calculation](r87-spectral-all-scale-exceptional-left-reduction.md), with **no new right restrictions**. Thus $Y\le N\le2Y$ is even, $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$ and $I\subset(N/2,9N/16]$ is the original real half-open interval with bounded real test $\omega$ of bounded pointwise variation. Keep the true $D,H_0$, cutoffs and tuple weights from the [long unsigned decomposition](r91-spectral-exceptional-long-unsigned-deletion.md). The actual primitive real Page character $\chi$ has conductor $r\le Q_0$ and real simple zero $\beta$ in the original Page strip. When there is no such character both exceptional terms are zero. Throughout the new result suppose $2\mid r$; the primitive two-part has modulus $2^e$ with $e=2$ or $3$.

**Theorem.** With a fixed $C$ the true unrestricted exceptional terms satisfy

$$
 \mathfrak E_\pm(N;I,\omega)
   =\frac{\gamma_N}{2}(\mathcal D_0(N)\pm\mathcal D_1(N))
                  +O(Y^\beta G^C Q_0^{-1}),
 \qquad \gamma_N=\frac{c_r(N)}{\varphi(r)} .                          \tag{1}
$$

Here $\mathcal D_i$ are the exact finite algebraic colors in the [all-target contraction](r94-spectral-all-target-ramanujan-exception.md), with their original $t\le Q_0/r$. This raw error uses no distance below the cap and no extra proximity of $\beta$ to one.

In addition take $\omega\ge0$ with $\int_I\omega\ge c_{\rm test}Y$, $(1-\beta)G\le C_*\log G$, and $K_z=\prod_{p\le z}p\mid N$ for the genuine $z_*\le z\le Z$ with sufficiently large fixed $z_*$. These are the actual physical and analytic conditions of the [target-local margin result](r103-spectral-pointwise-target-local-cap-margin.md). There is a fixed $C_0$ such that when $\gamma_N\ne0$ and

$$
          \log(Q_0/r)\ge C_0\left\{\log G+
                     \sum_{\substack{p\mid N\\p\nmid r}}p^{1/4-\beta}\right\},
                                                                    \tag{2}
$$

the original unrestricted exceptional difference has the conditional lower bound

$$
 -\chi(-1)\operatorname{sgn}(\gamma_N)
                       (\mathfrak E_+-\mathfrak E_-)
       \gg |\gamma_N|\frac{Y^{2\beta-1}}G\,
                          \frac{\Sigma^{(r)}(N)}{(\log r)^4}.        \tag{3}
$$

The factor $\Sigma^{(r)}(N)$ is the same completed singular factor as before. In particular (3) requires neither odd overlap nor a bound on the missing odd product. It still does not assert the lower bound when the exact response vanishes.

## 1. Exact two-adic cancellation before restoring squarefreeness

In the hard exceptional functional use the two exact colors $A_0=M_++M_-$ and $A_1=M_+-M_-$ from the long unsigned decomposition. Their signs on a true tuple are respectively $\mu(b)\mu(c)$ and $\mu(a)\mu(d)$; the complementary unsigned variables are $(a,d)$ and $(b,c)$ respectively. Put $S=Y^{1/10}$. In the part discarded from either color, choose disjointly the first unsigned variable $v>S$ in the usual order and fix the other three factors, with product $h$. This fixes the signs. All actual gates in $v$ partition into at most two intervals and the physical weight $\omega(N-hv)(N-hv)^{\beta-1}W(hv,a,c)$ on each has supremum plus pointwise variation $O(Y^{\beta-1})$, exactly as in the unsigned calculation. On the actual support $h\le 2Y^{9/10}$.

For clarity keep every finite range and every expansion in that calculation. In particular expand the Ramanujan factor at $n=N-hv$ by $d_0\mid(t,n)$, where $t\le Q_0/r$ is squarefree and $(t,r)=1$. Expand the unit mask $(v,h)=1$ by $a_0\mid h$ and squarefreeness of $v$ by $b_0^2\mid v$. Truncate the latter at $b_0\le Y^{1/30}$. The high square-label terms still cost $O(Y^{\beta-1/30+o(1)})$ by the original absolute positive floor estimate. There is no new conductor assumption in that bound.

For each remaining term put $s=[a_0,b_0^2]$ and $v=sw$. The congruence $d_0\mid N-hsw$ is either impossible or specifies $w=w_0+e_0j$ for one class modulo $e_0=d_0/(d_0,hs)$. As $(d_0,r)=1$, $e_0$ is odd. We are left with the exact character

$$
                 \chi(N-hs w_0-hs e_0j).                            \tag{4}
$$

If $hs$ is even, then every argument of (4) is even because the **actual** target $N$ is even. Since $2\mid r$, the character is identically zero, not just zero on average. If $hs$ is odd, the slope $-hs e_0$ is odd. Varying $j$ through a full period modulo $r$ and using CRT, the local argument modulo $2^e$ is an affine permutation of all the residues. The primitive local character at $2^e$ is nonprincipal and sums to zero on the full residues (with its nonunit value zero). The local factors at the odd part of $r$ are independent of this variable under the CRT, whether their affine slopes are units or not. Consequently the complete-period mean of (4) is exactly zero in this case too. This checks all terms of the expanded literal square sieve, before requiring $v$ itself squarefree again. In particular there is no rare progression to bound for even $r$.

In each real interval of $v$, the corresponding integer interval of $j$ hence has incomplete-period error $O(r)$, times $O(Y^{\beta-1})$ by the unchanged BV weight. The number of $a_0,b_0$ choices per $h$ is at most $\tau(h)Y^{1/30}$, there are $Y^{9/10+o(1)}$ fixed triples, and the positive absolute $t,d_0$ weights and $r$ cost $Y^{o(1)}$. These are precisely the counts of the original unsigned calculation and give $O(Y^{\beta-1/10+1/30+o(1)})$. The exact hard functional on either color therefore changes by only

$$
                         O(Y^{\beta-1/30+o(1)})
                                                                    \tag{5}
$$

when restricting its unsigned variables to $\le S$, with no contribution of the old odd-conductor rare-class size. The comparison has neither enlarged the original arcs nor introduced the restriction $r\mid N$.

## 2. Transfer to the original exceptional integrals and take the parity difference

Apply Section 1 of the [sharp hard transfer](r102-spectral-sharp-hard-transfer-odd-overlap.md) to the two **unrestricted** original parity integrals. It has error $O(Y^\beta G^C Q_0^{-1})$ on those integrals, without any parity assumption on $r$. In their literal hard expressions apply (5) to the two colors just as in the previous deletion proof. On these retained arrays the two masked long Möbius counts and the exact primitive contraction of the all-target proof, Sections 2--3, give $\gamma_N\mathcal D_i(N)$. Their remaining errors are fixed-power savings, or $O(Y^\beta G^{C_1}Q_0^{C_2}e^{-c\sqrt G})$, by the actual short mutual gcd tail and the two finite progression estimates there. Each is $O(Y^\beta G^C Q_0^{-1})$ since $\log Q_0=o(\sqrt G)$. There is no separate long-unsigned error to add after (5). Taking the original half-sum and half-difference gives (1).

For the lower bound, the exact $\mathcal D_1(N)$ is unchanged from the target-local margin proof, whose algebraic fixed-moment completion and positive lower on the completed color-one physical integral only use (2), the hypotheses on the zero and test, and planting. Neither uses odd overlap. Those bounds show that $-\chi(-1)\mathcal D_1(N)$ is bounded below by a fixed positive multiple of $Y^{2\beta-1}\Sigma^{(r)}(N)/(G(\log r)^4)$ under (2). The algebraic error in that comparison already carries the response when inserted in (1). In (1), if the response is nonzero, $|\gamma_N|=1/\varphi(r_{\rm odd}/(r_{\rm odd},N))\ge1/r$. Dividing the raw error by it costs at most $Y^\beta G^C r/Q_0$, which is negligible compared with the same lower scale by (2), $Y^{1-\beta}\le G^{C_*}$, $\log r\ll\sqrt G$ and $\Sigma^{(r)}(N)\gg1$. Subtracting the two parities proves (3) with the exact sign.

If the actual even conductor has odd part disjoint from $K_z$ for a permitted fixed $z$, a hypothetical example of the target conditions is $N=2^kK_z\in[Y,2Y]$ with sufficiently large $k$: its two-adic response has modulus one, its odd part has no overlap, and its target-local prime moment is bounded. The assertion still requires the independent near-zero and denominator-margin hypotheses. For an odd conductor, the affine two-adic argument above is absent; the original rare complement without odd overlap is not controlled by this result.