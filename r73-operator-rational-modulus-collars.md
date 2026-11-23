# Rational collars of the actual principal modulus Fourier field

**Scope.** This bounds a growing collection of high as well as low discrete modulus Fourier modes of the true all-alias parent matrix. The prime-power units, the three original signs, and the exact continuous benchmark are retained. The frequency neighborhoods are around reduced rationals in the modulus variable, not restrictions on the arithmetic alias index. The complement of these neighborhoods, the full mean square, and individual-modulus smallness remain open.

## Statement

Use the literal parent means of [R70](r70-operator-adaptive-parent-contrast-rank.md), their exact terminal/body masks in [R71](r71-operator-parent-terminal-layer.md), and the unweighted complete even-modulus field and discrete Fourier normalization of [R72](r72-operator-principal-modulus-low-modes.md) (2). Thus $4\le H<M\le Q^\Gamma$ for fixed $0<\Gamma<1$, $N=2m\in[Q,2Q]$ runs over all $J\asymp Q$ even moduli, and $T_N^{u,v}$, for either of the true raw families $u,v\in\{h,f,g\}$, is the matched signed matrix of all aliases $kN$ with the original units and no equality line. Its Fourier coefficients are

$$
\widehat T(j)=\frac1J\sum_{m=m_0}^{m_0+J-1}
                e\big(-j(m-m_0)/J\big)T_{2m}^{u,v},
       \qquad e(z)=\exp(2\pi iz).
 \tag{1}
$$

Assume original local GRH on this shell and auxiliary Dirichlet GRH for every modulus $q'\le \lceil8MB\rceil+2$, including $1$, where $B\ge1$ is an integer and $BM\le Q/100$ for all large $Q$.

For any reduced rational $a/b\bmod1$ with $1\le b\le B$, and any Fourier index $j\bmod J$, put $r=\operatorname{dist}(j,Ja/b+J\mathbb Z)$. Then

$$
\|\widehat T(j)\|_{\rm HS}
   \ll_{\Gamma,\epsilon,\Theta} Q^\epsilon
   \left[\sqrt{\frac{bM}{Q}}
      +\frac1{\sqrt b}\sqrt{\frac MQ}(1+r)
      +\frac{bM}{Q}(1+r)^2\right].
 \tag{2}
$$

For the union $\mathcal C(B,R)$ of the modes with $r\le R$ for some such fraction, for any $R\ge1$, it follows that

$$
\left(\sum_{j\in\mathcal C(B,R)}\|\widehat T(j)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\epsilon,\Theta} Q^\epsilon
  \left[
   \sqrt{\frac MQ} B^{3/2}(1+R)^{1/2}
   +\sqrt{\frac MQ} B^{1/2}(1+R)^{3/2}
   +\frac MQ B^2(1+R)^{5/2}\right].
 \tag{3}
$$

This is the true Hilbert–Schmidt RMS of the orthogonal projection of the original field onto those modes. In particular at $M=Q^{3/5}$, $B=\lfloor Q^{1/10}\rfloor$ and $R=\lfloor Q^{3/40}\rfloor$, the bound in (3) is $O_\epsilon(Q^{-1/80+\epsilon})$. The separated collars in this example contain $\asymp Q^{11/40}$ modes, including modes near $J/2$, far from the zero-frequency window. The auxiliary GRH cap is $O(Q^{7/10})$. The same estimate covers the actual unmasked $h,h$ parent compression and the surviving $f,f$ square-root prefix mixture directly, without a transfer approximation.

## 1. Switch with a rational modulus frequency

Fix a parent dyad pair $V\le U$, working first with a single matrix entry indexed by $I,I'$. As in R72 (4)–(5), the raw profiles have exact $t$-independent supports in $[0,2QV]$, $[0,2QU]$ for $t\in[Q,2Q]$. Put $b_I=\sqrt{|I|}/(\sqrt Q V)$ and $b_{I'}=\sqrt{|I'|}/(\sqrt Q U)$. The first two normalized parameter derivatives obey the pointwise envelope $O(b_I)$, and each spatial derivative thereof has a fixed $L^1$ envelope of mass $O(b_I)$. The identical bounds hold for $I'$. In particular this includes the actual terminal and body masks. The factors $b_I b_{I'}$ cost $O((Q\sqrt{VU})^{-1})$ when assembled in the dyad-pair HS norm by R72 (5).

Let $\omega\in C_c^2((Q,2Q))$ be a possibly complex smooth modulus test and put $K_1=\|\omega\|_\infty+\|\omega'\|_1,\ K_2=\|\omega''\|_1$. We first establish, for every reduced $a/b$,

$$
\left\|\sum_{2\mid N}\omega(N)e(aN/(2b))T_N^{u,v}\right\|_{\rm HS}
 \ll_{\Gamma,\epsilon,\Theta} Q^\epsilon
     \big[(bM+b^{-1/2}\sqrt{QM})K_1+bQM K_2\big].
 \tag{4}
$$

For one of the three orientations write $t=(\sigma_1 x+\sigma_2y)/k$, $q=2k$, $q'=qb$. On an actual switched arithmetic point one has $q\mid\sigma_1x+\sigma_2y$, $t=N$ even, and the twist is $e(a(\sigma_1x+\sigma_2 y)/q')$. It depends only on the residues $r,s\bmod q'$. The remaining smooth weight is precisely the weight $\mathcal H(x,y)=\omega(t)u_{I,t}(x)v_{I',t}(y)$ of R72 (7). In particular the first and mixed derivative bounds there remain valid:

$$
\begin{split}
   \iint|\partial_y\mathcal H|&\ll QV b_I b_{I'}K_1,\qquad
   \iint|\partial_x\mathcal H|\ll QU b_I b_{I'}K_1,\\
   \iint|\partial_{xy}^2\mathcal H|
       &\ll b_I b_{I'}
                     [K_1+(QV/k)(K_2+K_1/Q)] .
 \end{split}
 \tag{5}
$$

The phase has been moved into the residue matrix, so it does not differentiate into this bound.

The original $N$-nonunit terms can be dropped temporarily exactly as in R72 §2, with entrywise cost $O_\epsilon(Q^\epsilon QU b_Ib_{I'}K_1)$ across $k,N$. The switch imposes $q=2k$ congruence; discard also the $q'$-nonunits on either leg temporarily, at the same total cost. For fixed $k$, a discarded prime-power leg has total mark $O(L^2)$, with $L=\log(3Q)$, and each atom has $O(QU/q+1)$ partners by congruence modulo $q$, not assumed modulo $q'$. Sum this over $k\le4U$; the hypotheses ensure $q'\le8MB$. Not all $q'$-nonunit pairs are simultaneously nonunit on both legs, and the estimate counts either leg. No admissible proper powers are deleted in the final estimate.

## 2. Residue row and column sums and two centered errors

For units $r,s\bmod q'$, define the weighted incidence matrix

$$
A_{r,s}=\mathbf1_{q\mid \sigma_1r+\sigma_2s}
                     e\big(a(\sigma_1r+\sigma_2s)/q'\big).
 \tag{6}
$$

The unit reduction onto $q$ has fiber size $\phi(q')/\phi(q)\le b$. Thus row and column absolute sums give $\|A\|_{\ell^2\to\ell^2}\le b$.

Both the row sum and the column sum of (6) vanish if $b$ is not squarefree or if $(b,q)>1$. In the other case the row sum is

$$
\sum_s A_{r,s}
                       =\mu(b)e(a\sigma_1\overline q r/b),
 \tag{7}
$$

where $\overline q$ denotes the inverse modulo $b$; the column formula replaces $\sigma_1r$ by $\sigma_2s$. At $b=1$ the additive expression is interpreted as 1. To prove this, write the allowed $s=s_0+q z\bmod q'$ for $z\bmod b$, with $s_0$ a unit modulo $q$ and $\sigma_1r+\sigma_2s_0\equiv0\bmod q$. At a prime $p\mid b$ also dividing $q$ no restriction on $z$ is imposed by primitivity at $p$; its complete primitive exponential sum is zero. For $p\mid b,\ p\nmid q$, primitivity excludes exactly one residue of $z\bmod p$. At a power $p^e$, $e\ge2$, its primitive exponential sum over the allowed $z$ is zero as well, by summing lifts of each residue modulo $p$. This proves the vanishing cases by CRT. Otherwise let $z_0\equiv-s_0\overline q\bmod b$. The allowed $z$'s are those with $(z-z_0,b)=1$, and the primitive exponential sum is $\mu(b)e(a\sigma_2 z_0/b)$. The combined phase in (6) after this shift reduces to $e(a\sigma_1\overline q r/b)$, since $s_0+qz_0\equiv0\bmod b$ and $\sigma_1r+\sigma_2s_0\equiv0\bmod q$. This proves (7) and, by the same calculation on the other leg, the column formula.

Write $F_{q',r}(x)=\psi(x;q',r)-x/\phi(q')$ for units. Expanding both residue measures against the kernel (6), the double principal coefficient multiplying $\iint\mathcal H\,dx\,dy$ is

$$
\frac1{\phi(q')^2}\sum_{r,s}A_{r,s}
           =
          \begin{cases}
             1/(\phi(q)\phi(b)^2),& b\ {\rm squarefree},\ (b,q)=1,\\
             0,&\text{otherwise}.
          \end{cases}
 \tag{8}
$$

Indeed in the admissible case $\sum_r e(a\sigma_1\overline q r/b)=\phi(q)\mu(b)$, by CRT. The double error is estimated as in the twice-centered R72 argument: integrate both legs by parts in $\mathcal H$ and use $\|A\|\le b$ and the residue-vector GRH bounds $O(L^2\sqrt{QV})$, $O(L^2\sqrt{QU})$ at modulus $q'$. Thus its cost per $k$ is at most

$$
O_{\Gamma,\Theta}\big(
        b Q\sqrt{VU} L^4 b_I b_{I'}
              [K_1+(QV/k)(K_2+K_1/Q)]\big).
 \tag{9}
$$

As in R72, the square-root origin presents no boundary term; the profile vanishes there and its derivative is integrable. The smooth modulus test has no sharp affine boundary.

The single-error terms vanish in the inadmissible case of (8) by (7). In the admissible case, after summing the other leg, the primitive additive twist at modulus $b$ in (7) **collapses** the residue error:

$$
\sum_{r\bmod q'}^{*} e(c r/b)F_{q',r}(x)
   =\sum_{u\bmod b}^{*} e(cu/b)F_{b,u}(x)
       - \sum_{\substack{n\le x\\(n,b)=1,\ (n,q)>1}}
                    \Lambda(n)e(cn/b).
 \tag{10}
$$

The continuum mean agrees by CRT, each unit modulo $b$ having $\phi(q)$ unit lifts. The last sum has absolute size $O(L^2)$, and by GRH at $b$ and Cauchy in its residue vector the first has sup bound $O(L^2\sqrt{bQV})$ for $x\le2QV$. For the other leg replace $V$ by $U$. The coefficient $1/\phi(q')=1/(\phi(q)\phi(b))$ is from the principal measure of the other raw variable. Thus partial integration and (5) give entrywise single-error cost per $k$

$$
O_\epsilon\!\left(Q^\epsilon b_Ib_{I'} K_1\,
             \frac{b^{-1/2}}{\phi(2k)}
               (QV\sqrt{QU}+QU\sqrt{QV})\right).
 \tag{11}
$$

This use of the exact row sums is needed to avoid a spurious factor from $\phi(q')$ in the single errors.

## 3. Matching the true twisted continuous coefficient

Let $I_k(t)=\int u_{I,t}(x)v_{I',t}(\sigma_2(kt-\sigma_1x))dx$; its product $\omega I_k$ has sup plus TV $O(QVb_I b_{I'}K_1)$ by R72 §3, without the rational twist. The Jacobian in the double principal term (8) is $dy=k\,dt$ at fixed $x$. For the actual twisted model on the line, write $N=2m$ and expand

$$
\mathfrak S(kN)=\mathfrak S(2k)
        \sum_{\substack{d\mid m,\ d\ {\rm odd,\ squarefree}\\(d,k)=1}}
                 \rho(d),\qquad \rho(d)=\prod_{p\mid d}(p-2)^{-1}.
$$

On $m=dn$ the rational phase is $e(a d n/b)$. When $b\nmid d$, geometric summation and Abel give size $O(b\,\|\omega I_k\|_{\rm BV+sup})$ with no main term. When $b\mid d$, the main term is $(2d)^{-1}\int\omega I_k(t)dt$, with ordinary BV error. Such divisors $d$ exist only in the admissible case of (8). The main coefficient in that case is

$$
\frac{\mathfrak S(2k)}2\!
      \sum_{\substack{b\mid d,\ d\ {\rm odd,\ squarefree}\\(d,k)=1}}\frac{\rho(d)}d
       =\frac{k}{\phi(2k)}
             \prod_{p\mid b}\frac{1}{p(p-2)+1}
       =\frac{k}{\phi(2k)\phi(b)^2}.
 \tag{12}
$$

The first Euler equality uses the untwisted R63 model coefficient and imposes the Euler divisor choice at each $p\mid b$. It exactly matches (8) with its Jacobian. The extension of the coefficient past the actual $d\le2Q$ and the sum of progression errors are $O_\epsilon(Q^\epsilon b QV b_I b_{I'}K_1)$ per $k$, since $\rho(d)\ll_\epsilon d^{-1+\epsilon}$ and $\int|\omega I_k|\ll Q\|\omega I_k\|_\infty$. This applies also in the vanishing cases and keeps the original model, not a replacement by an independent one.

Finally sum $k\le4U$, take HS using (5) of R72 and the $b_Ib_{I'}$ factor, and sum the three orientations with signs $+,+,-$. From (9) the dyad-pair cost is $O_\epsilon(Q^\epsilon b[U K_1+QV K_2])$, using the harmonic sum over $k$. From (11) it is $O_\epsilon(Q^\epsilon b^{-1/2}\sqrt{QU}K_1)$, using $\sum_{k\le4U}\phi(2k)^{-1}\ll_\epsilon Q^\epsilon$. The model and unit restorations are bounded by $O_\epsilon(Q^\epsilon b U K_1)$. Summing over the dyads proves (4).

## 4. From a smooth tested proof to the actual complete-shell projection

The crude pointwise $\|T_N^{u,v}\|_{\rm HS}\ll_\epsilon Q^\epsilon$ from R72 §1 holds for all the chosen actual masks. For a fixed denominator $b$ choose a shell cutoff that is one except on endpoint strips of length $O(E_b)$, $E_b=\sqrt{bQM}$, and has $L^1$ norm of its first and second derivatives $O(1)$, $O(E_b^{-1})$, respectively. Our assumption $BM\le Q/100$ makes this choice possible with support strictly inside the shell. Approximate the modulus Fourier frequency $j/J$ by $a/b$ modulo 1 and modulate the cutoff by the **detuning** frequency, taking the rational phase in (4) with the appropriate sign. The detuning has absolute value $r/J$ per unit $m=N/2$, so

$$
K_1\ll1+r,\qquad K_2\ll E_b^{-1}+(r+r^2)/Q.
$$

Restore the actual unweighted shell on the endpoint strips at cost $O_\epsilon(Q^\epsilon E_b)$ before division by $J$, using the modulus-one Fourier weights. Substituting in (4) and using $J\asymp Q$ proves (2). There is no smoothing of the final field in (1).

For each denominator $b$ there are at most $b$ reduced centers and $O(1+R)$ modes per collar. Bound the three squared contributions of (2) over the union by summing them over these centers, using $r\le R$ and $\sum_{b\le B}b^2=O(B^3)$, $\sum_{b\le B}1=O(B)$, and $\sum_{b\le B}b^3=O(B^4)$. Taking square roots and using the finite Fourier Parseval identity gives (3), regardless of overlaps. In the numerical example the three exponents are $-1/80,-3/80,-1/80$, respectively. Distinct reduced rational centers are at circular distance at least $1/B^2$, so the example's collars are disjoint because $1+R\ll J/B^2$. The elementary count $\sum_{b\le B}\phi(b)\asymp B^2$, with $\asymp R$ mode indices in each collar, gives the stated cardinality. A degree bound on alias indices is not applied anywhere in the switch, and no conclusion is obtained for the complementary modulus frequencies.
