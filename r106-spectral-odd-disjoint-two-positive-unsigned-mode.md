# The odd-disjoint actual exceptional remainder has two positive long legs

For the genuine mixed-strip exceptional pieces at an odd Page conductor coprime to the actual even target, the [one-unsigned calculation](r105-spectral-odd-disjoint-explicit-unsigned-mode.md) separates a signed real remainder from the two original long-Möbius poles. We now reduce that remainder to two **short signed** coordinates and perform **both** long positive counts with their exact squarefree and coprime densities. This gives an explicit finite hard formula, not an estimate for its remaining signed short sum. It does not determine the pointwise sign of the unrestricted exceptional difference or of either total mixed parity, assert a Page zero exists, or establish Hypothesis S.

Use the exact $Y\le N\le2Y$ even, $G=\log Y$, $L=\log N$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, $I\subset(N/2,9N/16]$, and bounded real pointwise-BV $\omega$ of the one-unsigned calculation. The actual Page character $\chi$ is primitive real of odd squarefree conductor $r\le Q_0$ with $(N,r)=1$, and $\beta$ is its real simple zero in the original strip. Thus $\gamma_N=c_r(N)/\varphi(r)=\mu(r)/\varphi(r)$. No additional closeness or denominator margin is assumed. Let $S=Y^{1/10}$.

Use the actual color-0 sign $\mu(b)\mu(c)$ and color-1 sign $\mu(a)\mu(d)$, with the same tuples $a,b,c,d$ as in the [original long-unsigned decomposition](r91-spectral-exceptional-long-unsigned-deletion.md). For each color take its two sign-bearing coordinates to be positive squarefree integers at most $S$, mutually coprime, and let $h$ be their product and $\epsilon_i$ their sign product. Denote the other two, now real positive coordinates by $v,w$. Their region $\Omega_i(h;v,w)$ means the original hard product range $m=hv w\in[N/3,2N]$, the genuine minimum, lower, and high tests
$D<\min(ab,ac)<\sqrt m$ and $abc>H_0$, and $N-m\in I$, all with the actual coordinates in their original positions. The two fixed integers themselves, not just $h$, determine this region. Put

$$
 J_i=\iint_{\Omega_i}
       \omega(N-hvw)(N-hvw)^{\beta-1}
       \left(1-\frac{2\log(ac)}{\log(hvw)}\right)\,dv\,dw.
 \tag{1}
$$

The notation $J_i$ includes the dependence on both fixed integer coordinates. Their true unit constraints with $v,w$, and squarefreeness and mutual coprimality of $v,w$, will be counted by densities, not imposed on a real continuum.

For $U_p=1-1/p$ define

$$
 \begin{split}
 V_r^{[2]}(h)&=\prod_{\substack{p\nmid r\\p\mid h}}U_p^2
                    \prod_{p\nmid rh}U_p^2(1+2/p),\\
 C_r^{[2]}&=\prod_{p\mid r}(1-1/p)(1-2/p),\\
 A_r^{[2]}(h)&=\prod_{p\mid(r,h)}\frac{p(p-1)}{p-2}.
 \end{split}
 \tag{2}
$$

At $p\nmid r$ use the actual target local coefficients

$$
 b_{p,h}^{[2]}(N)=
 \begin{cases}
 -1,&p\mid h,\ p\mid N,\\
 1/(p-1),&p\mid h,\ p\nmid N,\\
 (2-p)/((p-1)(p+2)),&p\nmid h,\ p\mid N,\\
 (p-2)/((p-1)^2(p+2)),&p\nmid h,\ p\nmid N .
 \end{cases}
 \tag{3}
$$

In particular $p=2$ is tested on the actual even target, as a nonconductor prime. Set

$$
 \mathcal P_i(N;I,\omega)=\sum_{\text{two true short signed coordinates}}
   \epsilon_i A_r^{[2]}(h)V_r^{[2]}(h)J_i
       \sum_{\substack{t\le Q_0/r\\t\ {\rm sf},\ (t,r)=1}}
                    \prod_{p\mid t} b_{p,h}^{[2]}(N).
 \tag{4}
$$

**Theorem.** With a fixed $C$ and the same finite algebraic signed-pole colors $\mathcal D_i(N)$ as in the [all-target contraction](r94-spectral-all-target-ramanujan-exception.md), the original exceptional pieces satisfy

$$
 \mathfrak E_\pm
   =\frac{\gamma_N}{2}\bigl(\mathcal D_0(N)\pm\mathcal D_1(N)\bigr)
     -\frac{\chi(N) C_r^{[2]}}{2\varphi(r)}
                     \bigl(\mathcal P_0(N;I,\omega)\pm\mathcal P_1(N;I,\omega)\bigr)
     +O(Y^\beta G^C Q_0^{-1}).
 \tag{5}
$$

No rational denominator is extended, and there is no inserted condition $(h,N)=1$ on (4). The true Möbius signs remain in (4).

## 1. Remove any polynomially long signed coordinate from the one-unsigned mode

Start from the retained real long-unsigned term of the one-unsigned proof, before the contraction over $q\mid t$. In each color, choose the first unsigned coordinate $v>S$, with its previous unsigned bounds literally fixed. Fix $q\mid t$ and view the exact product of local densities in that proof as a weight on the three other integer coordinates. Its $q$-dependent part already represents the positive-variable congruence averaged in $v$; it depends on occupancy of $p$ in the other product and on $p\mid N$, not on a new progression congruence for a signed coordinate.

If any of the two signed coordinates exceeds $S$, choose the first such coordinate $w>S$ and fix the other two actual integers, with product $H$. The preceding signed-coordinate bound, if any, concerns a fixed integer. Exchange the finite sum in $w$ and real integral in $v$. At fixed $v$, the $w$ slices are at most two real intervals, by the same individual gate argument of the one-unsigned proof, and their mark and physical test have supremum plus pointwise variation $O(Y^{\beta-1})$. The actual positive range has $w\ll Y/(Hv)$ and $v\ll Y/H$; on a nonempty slice $w>S$. The bound on the first chosen unsigned coordinate and that on any preceding unsigned one are fixed during this exchange.

Now assign which primes of $rq$ divide the actual squarefree $w$, with fixed product $d\mid\operatorname{rad}(rq)$ of those that do. The factors of the real one-unsigned product at primes of $rq$ are fixed by this assignment and the already fixed variables; their absolute values are at most one. Outside $rq$, a prime dividing $H$ cannot divide $w$ by the true coprimality. The remaining variable density factor at each $p\mid w$ is $(1-1/p)/(1-p^{-2})=p/(p+1)$ relative to the unoccupied density. Hence, up to a factor independent of $w$ of modulus at most one, this variable factor is exactly

$$
 \prod_{\substack{p\mid w\\ p\nmid rqH}}\left(1-\frac1{p+1}\right)
       =\sum_{\substack{\ell\mid w\\(\ell,rqH)=1}}\xi(\ell),
 \qquad
 \xi(\ell)=\mu^2(\ell)\prod_{p\mid\ell}\left(-\frac1{p+1}\right).
 \tag{6}
$$

In particular $|\xi(\ell)|\le1/\ell$. For $\ell>Y^{1/100}$ the absolute tail, at each fixed $v$, is at most a constant times
$Y^{\beta-1}(Y/(Hv))\sum_{\ell>Y^{1/100}}\ell^{-2}$, just by the floor bound for multiples of $\ell$. For the remaining labels write $w=d\ell x$. The genuine signed factor is now $\mu(d\ell)\mu(x)$ with $(x,d\ell rqH)=1$. In particular the assigned primes of $rq$ are extracted exactly, and all are excluded from $x$. No residue class modulo $r$ or $q$ remains in this Möbius count. Prefix scales in the allowed $x$ intervals lie between fixed positive powers of $Y$ (for instance $x\ge Y^{.08}$ for large $Y$ since $d\le rq\le Q_0$). The mask $d\ell rqH$ has polynomial size.

We use the ordinary Möbius bound $O(xe^{-c\sqrt{\log x}})$ and its masked version at polynomial lengths (the principal reciprocal-zeta estimate in the [polynomial-scale Möbius calculation](r85-spectral-unconditional-planted-ap-good-dyads.md)). To see the mask uniformity directly, $\mu(n)\mathbf1_{(n,M)=1}$ is the convolution of $\mu$ with the indicator of integers supported on primes of $M$. For those integers $u\le\sqrt x$, the unmasked bound at $x/u$ and $\sum 1/u=\prod_{p\mid M}(1-1/p)^{-1}\ll G^C$ suffice. For $u>\sqrt x$, the absolute tail after the floor count is at most $x^{7/8}\prod_{p\mid M}(1-p^{-3/4})^{-1}=x^{7/8}e^{O(G^{1/4})}$ for polynomial $M$: split primes at $G$ and bound the larger divisor primes by $O(G/\log G)$ in number. Thus the masked prefix has error $O(x G^C e^{-c_1\sqrt G})$ at all the present lengths. Applied by BV to the exact intervals, the contribution at fixed $v,d,\ell$ is
$O(Y^{\beta-1}Y/(Hv d\ell)\,G^C e^{-c_1\sqrt G})$.

Integrate $dv/v$ on the actual positive $v>S$ range, and use the harmonic sum in the two fixed integer coordinates; together they cost fixed powers of $G$. Summing (6) after either bound and all assignments and absolute finite $t,q$ factors costs at most $Q_0^{O(1)}G^{O(1)}$. The two errors save a fixed power of $Y$ or $\exp(-c_2\sqrt G)$, and are $O(Y^\beta G^C Q_0^{-1})$. This does not compare them to an assumed sign of a short signed sum.

## 2. Complete both truly positive long variables

When both signed coordinates are at most $S$, both unsigned coordinates are polynomially long in the actual domain. In color 0, $b,c\le S$ imply $a>D/S$ and $abc<\sqrt m\,\max(b,c)$, so $d>\sqrt m/S$. In color 1, $a,d\le S$ imply both $b,c>D/S$. In particular each unsigned coordinate is at least $Y^{.39}$ for large $Y$. Thus the disjoint first-unsigned selection here is just its first coordinate, with no bound on either long beyond the actual region. At fixed short $h\le S^2$, both long coordinates are also $O(Y^{.61})$ by their product bound. The complete one-unsigned mode restricted to these short signed coordinates equals the hard two-unsigned sum restricted to them up to its original fixed-power floor and tail errors: the proof of the one-unsigned comparison is unchanged by restricting its fixed integer coordinates. We now evaluate that hard sum directly.

For fixed short coordinates and fixed finite $q\mid t$, expand the two positive squarefree tests via labels $b_1^2\mid v,b_2^2\mid w$, mutual coprimality via $g\mid v,w$, and the two coprimalities with $h$ via $a_1,a_2\mid h$. Their usual coefficients are Möbius factors. Temporarily cut $g,b_1,b_2$ at $Y^{1/100}$. The hard-sum tails have fixed power savings: the number of positive pairs with $vw\ll Y/h$ and $g\mid v,w$ is $O(Y(1+G)/(h g^2))$, and with $b_i^2$ in the indicated arm is $O(Y(1+G)/(h b_i^2))$. Telescope the three truncations, first the gcd expansion and then the two squarefree expansions. Remaining truncated factors cost at most subpower divisor counts, so the same tails apply. The units can be kept as exact indicators for these tail estimates. The harmonic sum in the two short coordinates and exterior subpower coefficients do not erase the saving.

For each retained term put $s_1=[a_1,g,b_1^2]$, $s_2=[a_2,g,b_2^2]$ and enumerate the two genuine quotient residues of $v/s_1,w/s_2$ modulo $rq$. On a residue pair both $\chi(N-hvw)$ and the real counting constraint $hv w\equiv N\pmod q$ on the integers are constant. In each long variable at fixed value of the other, the same true interval argument and BV bounds apply. Count the first variable on its affine lattice, then exchange its real integral with the second summation and count the second variable. In the resulting real integral there is no congruence restriction on the continuous variables. Each one-variable replacement costs $O(Y^{\beta-1})$ at fixed other variable by bounded lattice discrepancy; the number or length of the other variable is $O(Y^{.61})$. Thus the aggregate error, using $O(Y^{.2})$ choices for short coordinates, $O(Y^{.03})$ for the three truncated labels, subpower $\tau(h)^2$ and residue and exterior counts, is $O(Y^{\beta-.16+o(1)})$. This sequence keeps the hard upper minimum as a union of intervals at each slicing step. No moving-boundary derivative of an already integrated function is needed.

Restore all three infinite labels in the resulting real density. Their absolute contribution at fixed $h,q$ is at most

$$
 \tau(h)^2 \sum_{g,b_1,b_2\ {\rm sf}}
          \frac1{[g,b_1^2][g,b_2^2]} .
$$

The sum still converges if $(g b_1 b_2)^{1/4}$ is inserted: if $p$ occupies at least one label then the two denominator factors cost at least a total $p^2$, and the insertion is at most $p^{3/4}$, so the finite number of nontrivial local increments is $O(p^{-5/4})$. An omitted label therefore costs a fixed power of $Y$. The two-variable real integral has area $O((Y/h)(1+G))$ before the bounded mark, and $\tau(h)^2$ is subpower, so the fully summed restoration still saves a fixed power. Finite prime inclusion–exclusion followed by this absolute convergence justifies the CRT product for the real main term.

## 3. The actual two-coordinate local factors

At $p\mid r$ the local target is a unit. If $p\mid h$, both long variables are units, and the local average is $\chi_p(N) U_p^2$. Otherwise the contribution from two units is $-\,\chi_p(N)U_p^2/(p-1)$, since their product is uniform on the units modulo $p$ and the nonprincipal affine character sums to zero on all residues. The two ways for exactly one variable to have valuation one contribute $2\chi_p(N)U_p^2/p$. Both divisible is forbidden. Their sum is $\chi_p(N)U_p(p-2)/p^2$, and its ratio to the occupied case gives (2). The full conductor product is $\chi(N)C_r^{[2]} A_r^{[2]}(h)/r$.

At $p\nmid r$, before $q$ is imposed the positive densities are $U_p^2$ if $p\mid h$ and $U_p^2(1+2/p)$ otherwise. If $p\mid q$ and $p\mid h$ the extra multiplier is $\mathbf1_{p\mid N}$. If $p\nmid h,p\mid N$, exactly one valuation-one variable must occur, giving multiplier $2/(p+2)$. If $p\nmid h,p\nmid N$, the pair must be two units of a specified product modulo $p$, giving $p/((p-1)(p+2))$. The two local choices in $q\mid t$ with their stipulated factor $\mu(t)/\varphi(t)$ give $(1-p\lambda)/(p-1)$ at each occupied $p\mid t$, with $\lambda$ the extra multiplier just computed. These are exactly (3); no $t$ tail was used. This proves (4) for the remaining signed-short part.

Finally the hard functional contributes its exact factor $-r/\varphi(r)$, giving the second term of (5) after the parity half-sum and half-difference. The original signed-pole components of the one-unsigned evaluation have not been changed. Its sharp band-to-hard error, and the new fixed-power and stretched-exponential errors, are all $O(Y^\beta G^C Q_0^{-1})$. This proves (5) with no comparison between the sizes of its two explicit parts.