# Fixed Taylor rank for the true early-profile larger-alias field

On each physical dyad the genuine parent profiles have a common raw square-root shape up to half the dyad's raw starting scale. Their scalar parent coefficients still vary with the real shell parameter. Approximating that variation in a fixed Taylor span gives a spatial rank reduction for the actual integrated early sectors, on all auxiliary character parities. It does not bound the retained coefficients or their crossings.

## 1. Actual fields and conclusion

Use the complete even shell, $N=2m$, genuine transported parent basis and $h,f$ profiles, with $4\le H<M\le Q^\Gamma$ and fixed $\Gamma<1$. Keep the high-denominator packet $\mathcal C_+(B,R)$, exact Fourier normalization $J^{-1}$, and common smooth taper of [R85](r85-operator-skew-translation-all-short-aliases.md). As there assume original local Dirichlet GRH at the shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Write $R_*=1+R$.

Take either the exact larger-alias field $\mathcal Z_{>K}$ of R85 or the exact reduced larger-alias field

$$
\mathcal Z_{>K}-\mathcal E_{P,K}-\mathcal R^{\rm rem}_{P,K}
 \tag{1}
$$

of [R87](r87-operator-adaptive-raw-minimum-even.md), in the latter case with the same admissible $P,K$. Denote the chosen field by $Z$. In particular $Z$ includes both genuine high individual selections, high product conductor selection, $(2k,b)<G$, raw $z,w>A$, and the original affine orientations with signs $+,+,-$. In (1) the remaining odd projections prescribed by [R86](r86-operator-long-alias-short-leg-even.md) and R87 are kept exactly. Neither auxiliary character parity is assumed small.

At an entry from physical dyads $V,U$, call the first raw coordinate early if $z\le QV/2$, and the second early if $w\le QU/2$. Split the actual integral **after** taking its mixed derivative into four disjoint sectors $E_{ij}$, where $i,j\in\{0,1\}$ record the early flags. Their raw indicators do not change any prime-power or model term and are not differentiated. Thus $Z=\sum_{i,j}E_{ij}$.

Put $L=\log Q$. For every integer $d\ge1$ there is a fixed real orthogonal projection $\Pi_d$ on the parent space, independent of $N,k,b,a$, and of the Fourier index, of rank $O_\Gamma(d(1+L))$. It is the same for either actual family $h,f$ on each leg. For sufficiently large $Q$, writing

$$
{\mathcal B}_{d}
 = Q^\epsilon(C_\Gamma/L)^d B^{3/2}M
       \left[\frac{R_*^{3/2}+R_*^{5/2}}{Q}
                         +\frac{R_*^{1/2}}S\right],
 \tag{2}
$$

where $C_\Gamma$ is fixed, we have

$$
\|E_{10}-\Pi_dE_{10}\|_{\rm pkt}
 +\|E_{01}-E_{01}\Pi_d\|_{\rm pkt}
 +\|E_{11}-\Pi_dE_{11}\Pi_d\|_{\rm pkt}
       \ll_{\Gamma,\Theta,\epsilon}{\mathcal B}_{d}.
 \tag{3}
$$

Here $\|X\|_{\rm pkt}=(\sum_{j\in\mathcal C_+(B,R)}\|X(j)\|_{\rm HS}^2)^{1/2}$, and each spatial projection in (3) is applied at every index. The estimates persist after restricting to any subset of the selected packet. For the exact R85–R87 parameters, every prescribed accuracy $Q^{-\mathcal A}$, with $\mathcal A>0$ fixed, is attained by $d=O_{\Gamma,\mathcal A}(L/\log L)$. Indeed the factor in (2) other than the Taylor error is $O_\epsilon(Q^{1/5+\epsilon})$ at those parameters. The total rank is then $O_{\Gamma,\mathcal A}(L^2/\log L)$.

Consequently the part $E_{10}+E_{01}+E_{11}$ is within this error of the sum of a field with fixed low-dimensional image and a field with fixed low-dimensional row space. Its double spatial complement is small:

$$
\|(1-\Pi_d)(Z-E_{00})(1-\Pi_d)\|_{\rm pkt}
                 \ll_{\Gamma,\Theta,\epsilon}\mathcal B_d .
 \tag{4}
$$

This is an estimate on spatial approximation of the actual early sectors. It gives no full HS bound on the early sectors, no estimate on $E_{00}$, and no bound for the retained low-dimensional directions or mixed crossings. It does not improve the prior sharp-shell comparison of $Z$ with $\widehat T,\widehat P$, and does not extend to all modulus Fourier modes, prescribed individual moduli, or weak S. In particular it differs from [R74](r74-operator-fixed-macro-mean-all-modes.md), which bounds a fixed coarse spatial deletion in the full all-mode parent field using an ordinary-modulus mean square.

## 2. A common fixed analytic spatial span

For a parent $I$ on a $V$-dyad put $X=QV$ and $b_I=\sqrt{|I|}/(\sqrt Q V)$. From the actual weight in [R71 (1)–(2)](r71-operator-parent-terminal-layer.md#statement-and-the-exact-profile-split) and the support observation in [R84 §2](r84-operator-short-cosine-and-sum-aliases.md#2-common-test-and-an-adaptive-raw-cutoff), for $0<z\le X/2$ both profiles equal $c_{I,t}\sqrt z$, where

$$
c_{I,t}=\frac{\sqrt{2\pi}}Q
     \left(\int_I x^{-3}
               [(Qx)^{-2/\log t}+(Qx)^{-1/4}]\,dx\right)^{1/2}.
 \tag{5}
$$

The raw cutoff $X/2$ is below every true terminal transition on this dyad. In particular the two profiles use the same coefficient.

Set $s_t=(\log t)^{-1}-L^{-1}$. For a complex $s$ define $c_I(s)$ by replacing $(Qx)^{-2/\log t}$ in (5) by $(Qx)^{-2/L}\exp(-2s\log(Qx))$, using the analytic square root that is positive at $s=0$. This is defined on $|s|\le a_\Gamma/L$ for small fixed $a_\Gamma>0$: since $x\asymp V$ and $V\le M\le Q^\Gamma$, $\log(Qx)=O_\Gamma(L)$. Choose $a_\Gamma$ so the exponential changes by at most $1/4$ in absolute value from $1$ throughout the disk. The integrated argument then differs from its positive value at zero by at most one quarter of that value, uniformly in the interval $I$. The other summand in (5) is unchanged and positive. This proves analyticity there and

$$
\sup_{|s|\le a_\Gamma/L}|c_I(s)|
   \ll_\Gamma Q^{-1}|I|^{1/2}V^{-3/2}
                      = b_I/\sqrt X .
 \tag{6}
$$

The constants are uniform on clipped parents and do not need a lower bound on $|I|$.

Let $c_{I,n}$ be the Taylor coefficients at $s=0$ and let $\Pi_{V,d}$ project onto the real span of $(c_{I,n})_{I\text{ on }V}$, $0\le n<d$. These vectors are real since the chosen square root is real for nearby real $s$. Put $\Pi_d=\bigoplus_V\Pi_{V,d}$ and use its complex-linear extension on the Fourier matrices. At every real $t\in[Q,2Q]$ the polynomial coefficient $p_{I,d}(t)=\sum_{n<d}c_{I,n}s_t^n$ and each of its real $t$-derivative vectors lie in this fixed span. The number of physical dyads is $O_\Gamma(1+L)$.

There is a fixed-radius complex $t$ disk of radius $cQ$, with small absolute $c>0$, about every $t\in[Q,2Q]$, on which the principal logarithm is analytic and $|\log t-L|=O(1)$, with $t$ interpreted as complex in that estimate. Thus $|s_t|=O(L^{-2})$ there. The ordinary Taylor remainder from (6), and Cauchy's derivative estimate in those $t$ disks, give for $0\le j\le2$

$$
\big|Q^j\partial_t^j(c_{I,t}-p_{I,d}(t))\big|
       \ll_\Gamma \frac{b_I}{\sqrt X}(C_\Gamma/L)^d
                  \qquad(Q\le t\le2Q).
 \tag{7}
$$

For example $|c_{I,n}|\ll(b_I/\sqrt X)(L/a_\Gamma)^n$, and summing the geometric tail in the complex $t$ disk gives (7) for $j=0$ there; Cauchy on a concentric disk of smaller fixed radius yields the other two estimates. This avoids allowing $d$-dependent constants in the derivatives. Thus on the early strip the error profile $(c_{I,t}-p_{I,d}(t))\sqrt z$ has sup at most $O(b_I(C_\Gamma/L)^d)$; its fixed spatial derivative envelope can be taken to be $O((C_\Gamma/L)^d b_I/\sqrt{Xz})$. These bounds hold also for its first two normalized $t$ derivatives. The normalizing polynomial profile itself has the same early-region bounds as the original profile up to an absolute constant.

## 3. Transfer to the exact larger-alias integrals

Fix a pair of dyads $V,U$ and entries $I,I'$. Set $X=QV,Y=QU$, and use a common scalar $\omega\in C_c^2((Q,2Q))$ before the numerator-specific detunings. Define $K_1=\|\omega\|_\infty+\|\omega'\|_1$ and $K'_2=\|\omega''\|_1+K_1/Q$. For each orientation put $t=(\sigma_1z+\sigma_2w)/k$; primes in derivatives of $\omega$ refer to this parameter before substitution. Use the genuine four-term raw chain rule [R80 (7)](r80-operator-early-quotient-resonance.md#3-common-weighted-derivative-on-the-two-early-strips) on $\omega(t)u_{I,t}(z)v_{I',t}(w)$. Products with $\omega$ are extended by zero off the support in $t$. In each early sector replace just each designated early profile by $p_{I,d}(t)\sqrt z$ or $p_{I',d}(t)\sqrt w$ in the four chain terms; never differentiate a spatial indicator.

When both profiles are replaced, telescope the difference of the two products into two terms, each containing one error profile. This may be done before taking the mixed derivative at each point interior to the raw masks. By (7) the error leg has sup and fixed raw derivative $L^1$ envelopes carrying the factor $e_d=(C_\Gamma/L)^d$, and the other leg keeps the analogous unrestricted estimates, using [R72 (4)–(5)](r72-operator-principal-modulus-low-modes.md#1-exact-fixed-supports-and-parameter-envelopes) for genuine profiles. These bounds suffice on the raw support in play, since the derivative kernel is then restricted and the boundary has zero area. In particular $\int_0^{X/2} dz/\sqrt{Xz}=O(1)$. A term with zero raw and two parameter derivatives is estimated by changing one coordinate to $t$ at fixed other coordinate; keep the coordinate with the shorter of the physical support lengths in the outer integral. The jacobian cancels one factor $1/k$ and leaves that short support length. A term with one parameter derivative changes the coordinate without a raw derivative to $t$, leaving a fixed raw derivative envelope on the other leg. The pure raw-derivative term just uses both fixed $L^1$ envelopes. Exactly as in [R76 (5)](r76-operator-joint-rational-numerator-variance.md#1-rational-switch-with-a-common-smooth-parameter), this gives absolute derivative integral

$$
\ll_{\Gamma,\Theta} e_d b_I b_{I'}
          \left[K_1+\frac{\min(X,Y)}k K'_2\right]
 \tag{8}
$$

at each alias and orientation. Any additional fixed raw mask of the actual sector can only shrink this absolute integral. No assertion about differentiating the sharp masks or comparing arithmetic at differently cut endpoints is needed.

In the residual (1), at any raw point the R86/R87 selections are equivalent to fixed leg projections for that point, or to leaving that leg unchanged. These selections depend on the dyad pair and raw order and cutoffs, not on the individual parent index within a dyad. They commute with the original character projections, and each is an $\ell^2$ contraction in the progression residue space. The R82 high product projection is a contraction on the complete common-test numerator vector. Applying the [R76 (7) joint incidence bound](r76-operator-joint-rational-numerator-variance.md#2-additive-parseval-in-the-exact-incidence-and-the-continuous-term) and auxiliary GRH bounds the joint numerator vector by $O_\epsilon(Q^\epsilon b\sqrt{XY})$ on the support. This applies also in $Z=\mathcal Z_{>K}$ and in each outer raw flag sector. The product $b_I b_{I'}\sqrt{XY}$ costs $O(1)$ after the parent square sums. Use (8), sum $k\le4\max(V,U)$ (harmonically for $1/k$), and sum dyad pairs. The total common-test approximation cost is at most

$$
O_\epsilon(Q^\epsilon e_d bM[K_1+QK'_2]).
 \tag{9}
$$

The genuine signed terms are being approximated, though a triangle bound is sufficient for the errors.

Restore the exact numerator-specific Taylor weights of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) for the common taper and integer offset $\ell$. The effective $K_1,K'_2$ bounds are $O(1+|\ell|)$ and $O(S^{-1}+(1+|\ell|)^2/Q)$. The true fractional coefficients act after the common tests and the product projection; all masks and the outer phase are unchanged. Dividing (9) by $J\asymp Q$, then square-summing over $b,\ell$ in the selected packet using $\sum b^2=O(B^3)$, gives the bound (2) for the difference between each original early field and its polynomial-profile field.

## 4. Exact spatial support after the approximation

For the approximation of $E_{10}$, at fixed $V,U,k,b,z,w$ its first-parent dependence is always a linear combination of the coefficient vectors of §2. This is true for every chain term because at most two parameter derivatives act on a scalar coefficient and a raw derivative only differentiates $\sqrt z$. All arithmetic incidence coefficients, raw indicators, and detunings are independent of the first parent index within the $V$-dyad. Hence at every Fourier index the approximate $E_{10}$ has image in $\Pi_d$. The analogous statement for $E_{01}$ is a fixed row-space inclusion. With both profiles replaced the approximation to $E_{11}$ has both inclusions. Since the basis vectors $c_{I,n}$ are real, the row statement uses the same $\Pi_d$ even for complex Fourier entries.

Left and right orthogonal projection are contractions for Hilbert–Schmidt norm, and $F\mapsto \Pi_d F\Pi_d$ is an orthogonal projection on the Hilbert–Schmidt space. Thus applying each corresponding complementary projection to its original field produces an error at most the approximation error just proved. This yields (3) and (4). For the concrete parameters, the three exponents in $B^{3/2}M$ times the respective terms of (2) are $151/800,\ 153/800,\ 761/4000$, all less than $1/5$. The geometric Taylor factor proves the arbitrary fixed power precision at the claimed rank. Neither this spatial containment nor its approximation says that the corresponding low-dimensional coefficient matrices are small.
