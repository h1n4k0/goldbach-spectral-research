# An explicit hard unsigned mode for the odd-disjoint exceptional term

**Scope.** For an odd primitive Page conductor coprime to the true even target, the actual exceptional mixed-strip term has a second finite expression in addition to the two signed-pole colors. It is a real hard integral over each genuine long unsigned sector with an explicit, signed local density. The principal two-pole cap is unchanged. This identifies the previously bounded rare contribution; it does not assert its relative smallness, its sign after the short signed sums, or a sign for the actual unrestricted parity difference. It is not a claim that the exceptional zero exists, a prime-pair result, or a result on Hypothesis S.

Take the true original exceptional pieces $\mathfrak E_\pm(N;I,\omega)$ of the [all-scale reduction](r87-spectral-all-scale-exceptional-left-reduction.md). In particular $Y\le N\le2Y$ is even, $G=\log Y$, $L=\log N$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$ for the fixed original $B>B_0>0$. The test is bounded real $\omega$ of bounded pointwise variation on its genuine real half-open $I\subset(N/2,9N/16]$. Suppose that the actual primitive real character $\chi$ has odd conductor $r\le Q_0$, with $(N,r)=1$, and simple real zero $\beta$ in the original Page strip. Then $r$ is squarefree and $\gamma_N=c_r(N)/\varphi(r)=\mu(r)/\varphi(r)$. If there is no Page zero at all under the original cap, the original exceptional pieces are zero. An existing Page input outside these conductor and target hypotheses is not covered here. No closeness or denominator margin beyond the Page choice is needed here.

The two color arrays of the [long unsigned calculation](r91-spectral-exceptional-long-unsigned-deletion.md) have pairwise coprime squarefree $a,b,c,d$, with $m=abcd\in[N/3,2N]$, $D<\min(ab,ac)<\sqrt m$, $abc>H_0$ and mark $W(m,a,c)=1-2\log(ac)/\log m$. The signs of colors $i=0,1$ are $\mu(b)\mu(c)$ and $\mu(a)\mu(d)$ respectively; thus their unsigned ordered lists are $(a,d)$ and $(b,c)$. Set $S=Y^{1/10}$. For each color in its actual unsigned complement, choose disjointly the first unsigned coordinate $v>S$ in its indicated order. Fix the other three true integer coordinates, of product $h$, keeping their squarefreeness, mutual coprimality and any earlier coordinate's bound $\le S$. Write $\epsilon_i$ for the now fixed color sign. On these data let $\mathcal I_{i,v}$ be the real $v$-set with $v>S$, all the unchanged product/divisor restrictions above and $N-hv\in I$, and put

$$
 J_{i,v}=\int_{\mathcal I_{i,v}}
           \omega(N-hv)(N-hv)^{\beta-1} W(hv,a,c)\,dv .
                                                                    \tag{1}
$$

Here $a,c$ inside $W$ are their literal coordinate values, using the real variable if it is one of them. An empty interval contributes zero. Conditions on the fixed coordinates are literal; the squarefreeness, unit and congruence conditions in the real variable are evaluated by the local density below, not imposed on its continuum.

For any such $h$ set

$$
 \begin{split}
 A_r(h)&=\prod_{p\mid(r,h)}[-p(p-1)],\\
 V_r(h)&=\prod_{\substack{p\nmid r\\p\mid h}}(1-1/p)
                   \prod_{p\nmid rh}(1-p^{-2}).
 \end{split}                                                        \tag{2}
$$

Define a squarefree coefficient at each $p\nmid r$ by

$$
 b_{p,h}(N)=
 \begin{cases}
       -1,&p\mid h,\ p\mid N,\\
       1/(p-1),&p\mid h,\ p\nmid N,\\
       1/(p^2-1),&p\nmid h,\ p\mid N,\\
       -1/((p-1)(p^2-1)),&p\nmid h,\ p\nmid N .
 \end{cases}                                                        \tag{3}
$$

Its finite signed sum is

$$
 \mathcal B_h(N)
   =\sum_{\substack{t\le Q_0/r\\t\ {\rm sf},\ (t,r)=1}}
                           \prod_{p\mid t}b_{p,h}(N).
                                                                    \tag{4}
$$

The term $t=1$ has empty product one. No denominator tail is extended. For $i=0,1$ let

$$
 \mathcal L_i(N;I,\omega)
       =\sum_{v\ {\rm selected}}\ \
           \sum_{\text{other three true integer coordinates}}
             \epsilon_i\,A_r(h)V_r(h)\mathcal B_h(N)J_{i,v}.
                                                                    \tag{5}
$$

The first sum refers to one of the two position choices, not values of the integrated coordinate. The finite inner sum is over the original fixed-coordinate conditions above and the bound $h\le 2N/S$, since larger $h$ cannot contribute. In particular it does not include any additional condition $(h,N)=1$.

**Theorem.** Let $\mathcal D_i(N)$ be the literal finite two-pole colors of the [all-target Ramanujan contraction](r94-spectral-all-target-ramanujan-exception.md). Uniformly at the specified odd-disjoint inputs and hard tests, with a fixed $C$,

$$
 \mathfrak E_\pm
     =\frac{\gamma_N}{2}
         \left\{\mathcal D_0(N)\pm\mathcal D_1(N)
              -\frac{\chi(N)}{r}
                         \bigl(\mathcal L_0(N;I,\omega)
                                      \pm\mathcal L_1(N;I,\omega)\bigr)\right\}
                      +O(Y^\beta G^C Q_0^{-1}).
                                                                    \tag{6}
$$

Neither $\chi(N)$ nor the signed factor $A_r(h)$ may be replaced by its absolute value in this identity. In particular a prime of $r$ occupied by a fixed coordinate changes the true local long-unsigned density by a factor $-p(p-1)$ compared with an unoccupied one. Consequently (6) is not a bound for $\mathcal L_i/r$ relative to either $\mathcal D_i$.

## 1. Retain the complete-period contribution

Let $\mathcal H(A)$ be the literal hard functional with the exact finite Ramanujan factor on an original right color. The [sharp band-to-hard comparison](r102-spectral-sharp-hard-transfer-odd-overlap.md), Section 1, changes the full parity pieces by $O(Y^\beta G^C Q_0^{-1})$, independent of odd overlap. For the hard colors with both unsigned coordinates $\le S$, the [common short-unsigned calculation](r104-spectral-common-short-unsigned-pointwise-parity.md), Section 2, gives $\mathcal H(A_i^{\rm ss})=\gamma_N\mathcal D_i(N)+O(Y^\beta G^C Q_0^{-1})$. This uses its evaluation of the already retained hard arrays, not any deletion of the long-unsigned complement.

Now work with the actual omitted hard color $A_i-A_i^{\rm ss}$ via the disjoint choices of (1). At fixed \(h\) the true allowed real set is a union of at most two intervals: all lower gates are interval conditions in the individual variable and the upper minimum gate is a union of its two upper alternatives. The actual real weight on each interval has supremum plus pointwise variation $O(Y^{\beta-1})$ by the same affine-log mark and hard weight argument as before. Its support has length $O(Y/h)$ and $h\ll Y^{9/10}$.

Expand the literal finite Ramanujan sum with $q\mid t$, actual congruence $hv\equiv N\pmod q$, and coefficient $q\mu(t/q)$ multiplied by $\mu(t)/\varphi(t)$. Thus $q$ is squarefree and $(q,r)=1$. At fixed $h,q$ expand the unit by $\sum_{u\mid(h,v)}\mu(u)$ and the squarefree condition by $\sum_{b^2\mid v}\mu(b)$. For this proof only, cut that second sum at $b\le Y^{1/30}$. The tail costs $O(Y^{\beta-1/30+o(1)})$ in the complete hard color: one may keep or restore the unit indicator, count at most $O(Y/(hb^2))$ positive multiples on the true support, and sum reciprocal weights of the three fixed coordinates. The total exterior $t,q$ weight is $Q_0^{O(1)}=Y^{o(1)}$, and $r/\varphi(r)$ is harmless.

For a remaining term put $s=[u,b^2]$. The actual congruence $hsv'\equiv N\pmod q$, with integer $v=sv'$, is either infeasible or specifies one class modulo $q/(q,hs)$. Then $\chi(N-hv)$ as a function of the free progression integer is periodic of period dividing $r$. Subtract its complete-period mean without assuming that mean is zero. On the original real hard interval, the sum of this difference is $O(r)$ times the exact BV norm. For the mean term, the sum of the BV weight on this progression differs from its real integral times the progression density by $O(Y^{\beta-1})$, by the bounded discrepancy of the integer lattice with the same endpoints. This is also valid for a short or empty piece and for the specified values at an endpoint, by bounded pointwise variation. Thus each retained expanded term gives precisely the mean times its progression density times (1), with error $O(rY^{\beta-1})$. Summing over $h\ll Y^{9/10}$ and its actual triples, the $\tau(h)Y^{1/30}$ choices of the two labels, and the subpower exterior costs, gives error $O(Y^{\beta-1/10+1/30+o(1)})$.

In this real main term restore all square labels $b$: their absolute density is at most $1/b^2$ regardless of the congruence or $u$. With the integral length $O(Y/h)$ and the subpower $\tau(h)$ this again costs $O(Y^{\beta-1/30+o(1)})$ after summing all exterior factors. Absolute convergence at fixed $h,q$ now permits evaluating the progression density by CRT. More explicitly, first restrict the prime factors of $b$ to a finite prime set containing $rhq$; inclusion–exclusion is then a finite periodic identity enforcing that $v$ is not divisible by the square of any of those primes. The complete means with the actual $\chi(N-hv)$ and $hv\equiv N\pmod q$ factor over these local periods. Let the prime set increase to all primes by the absolute bound $\tau(h)\sum_{b\ge1}b^{-2}$. This restores the true long variable's squarefree density without any order-dependent infinite sum.

## 2. The exact local averages and the finite contraction

At a conductor prime $p\mid r$ the local character is primitive nonprincipal modulo $p$, and $p\nmid N$. If $p\mid h$, the true unit condition makes the variable a unit and the character is the constant $\chi_p(N)$ on it. The density including the character is $\chi_p(N)(1-1/p)$. If $p\nmid h$, the affine argument is a permutation modulo $p$, and averaging on the entire residue system modulo $p^2$ gives zero. The excluded class $v=0\bmod p^2$ has character $\chi_p(N)$, giving the exact density $-\chi_p(N)/p^2$. These are independent of $q$. Their product is $\chi(N)\mu(r)r^{-2}A_r(h)$.

Away from $r$, the default local density is $1-1/p$ at $p\mid h$ and $1-p^{-2}$ otherwise; this gives $V_r(h)$. At $p\mid q$ there is the extra condition $hv\equiv N\pmod p$. If $p\mid h$ it leaves the density unchanged when $p\mid N$ and makes it zero otherwise. If $p\nmid h,p\mid N$ the forced class is $v=0\bmod p$, of squarefree density $1/p-1/p^2$. If $p\nmid h,p\nmid N$ the forced class is a unit, of density $1/p$. Thus the multipliers relative to the default are respectively

$$
  \lambda_{p,h}(N)=
  \begin{cases}
     \mathbf 1_{p\mid N},&p\mid h,\\
     1/(p+1),&p\nmid h,\ p\mid N,\\
     p/(p^2-1),&p\nmid h,\ p\nmid N .
  \end{cases}
                                                                    \tag{7}
$$

These also apply at $2$, which is a nonconductor prime here. In particular the actual nonunit progression classes have been retained. For a fixed squarefree $t$ the two choices of $p$ in $q\mid t$ give the joint multiplier $(1-p\lambda_{p,h}(N))/(p-1)$ after including the outside $\mu(t)/\varphi(t)$. Substitution gives precisely (3), so the **original finite** sum equals (4). No exterior coprimality of $h$ with $N$ has been substituted for this finite contraction.

Combine the integrated means of Section 1 with these local densities and the exact exterior factor $-r/\varphi(r)$ of the hard functional. For either color this gives

$$
 \mathcal H(A_i-A_i^{\rm ss})
     =-\frac{\chi(N)\gamma_N}{r}\mathcal L_i(N;I,\omega)
                                   +O(Y^{\beta-1/30+o(1)}).
                                                                    \tag{8}
$$

The sign follows from $\mu(r)/\varphi(r)=\gamma_N$, and from averaging $\chi(N-hv)$ rather than $\chi(hv-N)$. The fixed-power error is absorbed in $Y^\beta G^C/Q_0$ since $Q_0=Y^{o(1)}$. Adding the two-pole part, then using the exact parity half-sum and half-difference and the true band error, proves (6). The conditional pointwise sign of the common short-unsigned difference does not determine the size or sign of (5) after summing its genuine fixed coordinates.