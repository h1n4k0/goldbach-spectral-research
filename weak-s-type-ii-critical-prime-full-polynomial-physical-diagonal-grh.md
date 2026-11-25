# The genuine full polynomial divisor interval on the critical prime shell under global GRH

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, and $e(z)=e^{2\pi i z}$. Keep the original prime polynomial $P$, true two prime boxes, permissible bounded selector, unit test and hard cutoffs, and keep the critical prime shell of the [joint subpolynomial-interval theorem](weak-s-type-ii-critical-prime-cross-dyad-subpolynomial-grh.md). Thus $J=[N-y,N/2)$ with $N/2\le y\le9N/16$, the actual hard cofactor interval $I_k$ requires $k>t\ge N^{.49999}$, and the exact complementary coefficient is

$$
 D_m=\mathbf1_{m\in J}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                         (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_mD_m e(\alpha m).
$$

Here $I_d$ is an arbitrary hard interval in $[X,\infty)$; on $J$ it may be intersected with $[X,N/(2t))$ without losing any term. There is **no further restriction on its width**. In particular its effective upper endpoint may be of fixed polynomial ratio to $X$, up to $N^{1/100000}/2$. Write $\mathcal Q=[.8X,.9X]\cap\mathbb P$ and

$$
 \mathcal E_N(D)=\int_{-1/(10N)}^{1/(10N)}
             \sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}
                      |D(a/q+\beta)|^2\,d\beta .
$$

**Theorem (global Dirichlet GRH).** Assume the generalized Riemann hypothesis for all primitive Dirichlet $L$-functions, including $\zeta(s)$. Uniformly in every even target and the entire original admissible divisor interval, keeping all true units and hard cutoffs, we have for every $\epsilon>0$

$$
                           \mathcal E_N(D)\ll_\epsilon N L^{-1/3+\epsilon}.
 \tag{1}
$$

The actual signed full shell, its separately centered numerator covariance and the exact parity-preserving signed even-lattice residual of length $M=\lceil X L^2\rceil$ are consequently $O_\epsilon(NL^{-1/6+\epsilon})$. More precisely the proof gives

$$
 \mathcal E_N(D)\ll N\left(\delta+\frac{\delta^{-2} L_2^{10}}{L}\right)
                       +O(NL^{-2})
             \qquad (L^{-1/2}\le\delta\le L_2^{-4}).
 \tag{2}
$$

Choosing $\delta=(L_2^{10}/L)^{1/3}$ in (2) gives the explicit rate $O(NL^{-1/3}L_2^{10/3})$, and $O(NL^{-1/6}L_2^{5/3})$ for the three signed quantities. There is no dyad count in these bounds. The conditional input is used only for nonzero integer determinants. On the exact determinant diagonal, performing the physical Fourier integrals before the squared-norm estimate gives an unconditional bound uniform over the entire admissible polynomial interval. There is no claim of an unconditional bound (1), other shells, any bound on squares of individual compensated offsets, or Hypothesis S.

## 1. Keep the genuine common smoothing and the original units

After the harmless effective intersection of $I_d$, write its ordinary dyadic pieces as $I_i=I_d\cap[A_i,2A_i)$, $A_i=\lambda_iX$, $K_i=X/\lambda_i$, $\lambda_i=2^i\le N^{1/100000}$. There are $O(L)$ of them. Use the **common** physical smoothing $\Omega(m/N)$ supported inside $J/N$, and the **common** absolute cofactor smoothing $w(k)$ obtained by an inward mollification in $\log k$ at relative width $\delta$. These are the cutoffs of [the joint theorem, §1](weak-s-type-ii-critical-prime-cross-dyad-subpolynomial-grh.md#1-common-endpoint-transfer-before-splitting-into-dyads), with $I_k$ first intersected with $k<X/2$. Both tests are in $[0,1]$ and have total variation $O(1)$. In particular this physical smoothing costs $O(N\delta)$ in ordinary squared norm **on the whole genuine interval**, by the signed small-gcd short-divisor sum at its natural scale $N/(guz)$ and the uniform DIT continuous interval bound there. That proof only uses $\lambda_i\le N^{1/100000}$, not a bound on the number of dyads better than $O(L)$. A cofactor edge intersects only $O(1)$ dyads because $m\in J$ and the edge has relative width $O(\delta)$; the same reference bounds its squared cost by $O(N\delta)$. The relevant ordinary errors and their constants are uniform for the stated range of $\delta$.

For completion only, take $w_i(z)=w(K_i z)$ multiplied by the fixed smooth compact positive-proportional bump of the joint theorem, equal to one on $[7/32,1/2]$. This changes no value with $\Omega$ present. Keep the exact long unit $(d,N)=1$, truncate the squarefree expansion at $l\le T=L^{16}$ while retaining the full product unit, then truncate the short unit inclusion at squarefree $h\mid N$, $h\le H_0=\exp(C_0L_2^2)$ with fixed sufficiently large $C_0$. These are exactly the coefficients $B_{i,m}^{\dagger}$ from [equation (2) of the joint theorem](weak-s-type-ii-critical-prime-cross-dyad-subpolynomial-grh.md#2-exact-auxiliary-truncations-and-joint-fourier-completion). Explicitly

$$
 B_{i,m}^{\dagger}=
 \left(\sum_{\substack{dk=m,\ d\in I_i\\(d,N)=1}}
                  \mu(d)w_i(k/K_i)\right)
 \left(\sum_{\substack{l\le T,\ l^2\mid m\\(l,N)=1}}\mu(l)\right)
 \left(\sum_{\substack{h\mid\operatorname{rad}N,\ h\mid m\\h\le H_0}}\mu(h)\right).
$$

The support of each $B_{i,m}^{\dagger}$ in $m/N$ is compact even before $\Omega$. Those uniform forced-divisibility and squarefree-tail proofs give its ordinary norm $O(\sqrt N)$ and squared approximation error $O(NL^{-10})$ on one dyad. With $O(L)$ dyads the squared error is $O(NL^{-8})$ by Minkowski. The true hard coefficient on the whole interval has ordinary squared norm $O(N)$ by the unmasked signed short-label DIT form and the absolute $O(X^2)$ floor total. The full approximant $\Omega(m/N)\sum_i B_{i,m}^{\dagger}$ also has norm $O(\sqrt N)$ by these errors and the true smoothing. The exact long unit in this approximant implies $h\mid m$ iff $h\mid k$ in every summand. The restriction $(l,N)=1$ was imposed on the full true unit coefficient before the short inclusion truncation and has the same meaning here.

Put $G_\beta(v)=\Omega(e^v)e(\beta Ne^v)$; use $\widehat f(\xi)=\int f(z)e(-z\xi)\,dz$. The true physical Fourier interval and its common smoothing give, uniformly in the actual $\beta$,

$$
 |\widehat G_\beta(\tau)|\ll\min(1,|\tau|^{-1},\delta^{-1}|\tau|^{-2}),
 \qquad
 |\widehat G_\beta(\tau)|\ll_r\delta^{\,1-r}|\tau|^{-r}\quad(r\ge2).
 \tag{3}
$$

In particular $\|\widehat G_\beta\|_1\ll L_2$. As in the joint theorem, truncate $|\tau|\le L^4$ in the **actual** additive sampled vector. At each $\tau$ the two normalized product phases multiply to $e(\tau\log(m/N))$, independent of $i$. The pre-$\Omega$ ordinary norm of that vector's coefficient is $O(L\sqrt N)$ and its degree is $O(N)$; the separated-center sampling bound gives $O(LN)$ in norm at the actual centers $a/q$. Then (3) gives error $O_A(NL^{-A})$ in the sampled norm, for each fixed $A>0$, uniformly in $\beta$. Projection to the nonconstant component of each actual nonzero-numerator group is a contraction. No numerator-zero samples are introduced by this truncation.

## 2. Integrate in the complete square and dispatch its off-diagonal

Fix $l,s$ with $l\le T$ squarefree, $(l,N)=1$, $s\mid l$. In the exact split $s=(l,d)$ write $d=su$, $k=(l^2/s)hv$, with the actual mask $(u,lN)=1$. Set

$$
 \begin{split}
 U_i&=A_i/s,\qquad x_{q,i}=K_i s/(q l^2),\qquad x_{0,i}=K_i s/(Xl^2),\\
 a_{i,\tau}(u)&=\mu(u)\mathbf1_{su\in I_i}\mathbf1_{(u,lN)=1}
                            e(\tau\log(su/A_i)),\qquad
 f_{i,\tau}(z)=w_i(z)e(\tau\log z).
 \end{split}
$$

Thus $U_i x_{0,i}=X/l^2$, and $x_{q,i}\asymp x_{0,i}$. The short Fourier envelope and derivative bounds of the [single-dyad proof, §2](weak-s-type-ii-critical-prime-polynomial-single-dyad-grh.md#2-the-two-different-fourier-truncations) hold also here: with $Y_\tau=1+\delta^{-1/2}+|\tau|$ one has $|\widehat f_{i,\tau}(\xi)|\ll\min(1,(Y_\tau/|\xi|)^2)$ and higher-order integration by parts as in that reference. For $|\tau|\le L^4$ truncate the dual index at $0<|j|\le J_i=\lambda_iN^{1/1000}$ as before, at negligible sampled norm cost. The actual mesh $x_{q,i}/h\gg(\lambda_iT^2 H_0)^{-1}$ makes its tail power-small by using sufficiently high fixed derivative order. All retained $j,h,l$ are nonzero modulo every $q$.

For each fixed $\tau$, the nonprincipal Poisson expression at $q$ consists of Fourier transform in the unit character $\chi$ of the array on $v_0=hu/j\bmod q$, followed by the common factor $\tau_q(\chi)\mu(l)\mu(s)\chi(l^2)$. Its factor $\tau_q(\chi)$ has modulus $\sqrt q$ and is independent of $\tau$ and of the dyad. We now keep the $\tau$ integral **inside** the square. For each $q$ and every residue $v_0$ form

$$
 \mathcal S_q(v_0)=
  \int_{|\tau|\le L^4}\widehat G_\beta(\tau)
       \sum_i\sum_{\substack{h\mid\operatorname{rad}N,\ h\le H_0\\
                             0<|j|\le J_i\\ u\in\operatorname{supp}(a_{i,\tau}),\ hu/j\equiv v_0\bmod q}}
       \frac{\mu(h)x_{q,i}}h\,a_{i,\tau}(u)
                         \widehat f_{i,\tau}(jx_{q,i}/h)\,d\tau ,
 \tag{4}
$$

Remove the common Gauss magnitude, add the principal character algebraically on the units, then add the square of the residue zero. Multiplicative orthogonality bounds the actual squared character norm at this block by

$$
                      \sum_q q(q-1)\sum_{v_0\in\mathbb F_q}
                                            |\mathcal S_q(v_0)|^2 .
 \tag{5}
$$

This is the same positive completion as in the joint theorem, now on the integrated vector. It makes no assertion about the actual principal unit character or the original nonunit additive contribution.

Expand (5) as the two integrals in $\tau,\tau'$ and the dyad pair sum. The exact condition in the expansion is

$$
                         h_1 j' u-h_2 j u'=bq .
 \tag{6}
$$

For $b\ne0$, the [single-dyad nonzero-determinant estimate](weak-s-type-ii-critical-prime-polynomial-single-dyad-grh.md#3-the-nonzero-determinant-the-only-conditional-step) and its extension to dyad pairs apply with independent $\tau,\tau'$. Indeed, with $(h_1,h_2,j,j',b)$ fixed the factors of the exact Fourier integral over one torus are $A_{i,\tau}(h_1j'\theta)$ and $\overline{A_{i',\tau'}(h_2j\theta)}$, where $A_{i,\tau}(\theta)=\sum_u a_{i,\tau}(u)e(u\theta)$, and $\sum_q\omega_q e(-bq\theta)$ with the actual weights $|\omega_q|\ll X^2$. The $bq$ frequencies are distinct. Global GRH and the uniform [Baker–Harman bound](https://academic.oup.com/jlms/article-abstract/s2-43/2/193/862020) give $\|A_{i,\tau}\|_\infty\ll U_i^{4/5}$ after the exact coprimality convolution and Abel summation as in that proof (the underlying exponent is $3/4+\varepsilon$). The other two norms are $O(\sqrt{U_{i'}})$ and $O(X^2\sqrt{\#\mathcal Q})$ by ordinary Parseval. Uniformly in both independent frequencies, the label count is at most

$$
 O(\lambda_{\max}^4 N^{3/1000+o(1)}),
 \qquad |b|\ll \lambda_{\max}^2N^{1/1000+o(1)} ,
$$

and $U_i,U_{i'}\le X\lambda_{\max}$ with $\lambda_{\max}\le N^{1/100000}$. Thus each dyad pair contributes $O(N^{1.91})$ before the two frequency integrals. Integrating in absolute value costs $O(L_2^2)$ by (3), and there are only $O(L^2)$ pairs. This is negligible, uniformly for each $l,s,\beta$, even after the later label sum and shell integration. It is the only step using GRH.

## 3. Restore the exact physical integral on the rational diagonal only

For $b=0$ equality in (6) is literal equality of the two nonzero rationals $\rho=j/(hu)$. The determinant-zero part of (5) is thus a positive squared norm in the coordinates $(q,\rho)$ with weights $q(q-1)$, of the integrated vector analogous to (4) with $j/(hu)=\rho$ instead of the congruence. We restore both truncated frequency tails in this **analytical rational norm only**, not in a modular inverse identity for possibly nonunit $j$.

For each dyad and any real $\tau$, call $\Phi_i(\tau)$ its vector in this rational space with all $j\ne0$ (no $\tau$ integration). The arithmetic on one dyad gives

$$
 \|\Phi_i(\tau)\|_{\mathrm{rat}}^2
 \ll \frac{N^2Y_\tau L_2^3}{L l^2}
                      \bigl(L+\log(2+|\tau|)\bigr).
 \tag{7}
$$

Here the subscript means the squared sum weighted by $q(q-1)$. For completeness, on an $h_1,h_2$ cross write $g=(h_1,h_2)$. The true long units force $j=(h_1/g)i_1$, $j'=(h_2/g)i_2$, $i_2 u=i_1 u'$. The positive $u,u'$ count is at most $2U_i\gcd(|i_1|,|i_2|)/\max(|i_1|,|i_2|)$ when $i_1,i_2$ have the same sign; otherwise there is none. Use the envelopes with scale $Y_\tau g/x_{0,i}$ on the two indices; the elementary gcd sum weighted by these envelopes is $O(B\log(2+B))$ at $B=Y_\tau g/x_{0,i}$, as in the [weighted determinant-zero proof](weak-s-type-ii-critical-prime-dual-determinant-logarithmic-width.md#3-nonzero-determinants-and-the-weighted-zero-determinant). Multiplying by the actual mesh prefactor, $U_i x_{0,i}=X/l^2$ and $g/(h_1h_2)=1/[h_1,h_2]$ give (7) after $\sum_q q(q-1)\ll X^3/L$ and the $O(L_2^3)$ lcm reciprocal sum over the $h$ pairs. The logarithm is $\ll L+\log(2+|\tau|)$ because $\lambda_i\le N^{1/100000}$ and $g\le H_0$; there is no power of $\lambda_i$.

Triangle over the $O(L)$ dyads in this rational space and use arbitrarily high fixed derivative order in (3). This extends $|\tau|\le L^4$ to the entire line with $\mathrm{rat}$-norm difference $O_A(NL^{-A})$ for any fixed $A>0$. For the retained $\tau$ we also bound the rational norm of the omitted $j$-tail vector. If $|j|>J_i$, its sampled magnitude $|j|x_{q,i}/h$ is at least $N^{1/1000-o(1)}$. Set $F=N^{1/2000}$. Within one dyad on the diagonal, both samples are comparable by the exact ratio $i_2/i_1=u'/u\asymp1$. Write $i_1=\sigma d_0 r,i_2=\sigma d_0 r'$ with $(r,r')=1$, $u=r z,u'=r' z$ and $\sigma=\pm1$ as in the single-dyad proof. On $r\asymp R$ there are $O(R^2)$ possible $(r,r')$ and $O(U_i/R)$ positive $z$. Both samples are $\gg F$, so the product of the two Fourier envelopes summed over $d_0$ is

$$
          O\left(\frac{Y_\tau^4}{R (x_{0,i}/g)F^3}\right).
$$

This is the ordinary fourth-power tail sum, valid also when the positive lower bound on $d_0$ is below one. Even with all $j$ restored there are only $O(L)$ ratio dyads, since $r\le u<2U_i$. Thus the unweighted inner bound is $O((U_i/(x_{0,i}/g))\,L Y_\tau^4/F^3)$. Insert the same $q,h_1,h_2$ prefactor and lcm weight as in (7). This gives power savings in the squared rational norm of the omitted-dual vector on each dyad, as $Y_\tau$ is fixed-polylogarithmic for retained $\tau$. Minkowski over the $O(L)$ dyads and (3) integrate this difference at arbitrary log accuracy. Together the two extensions change the rational **norm** by $O_A(NL^{-A})$ for all $A$. Equation (7) and (3) bound both integrated norms by $N$ times a fixed power of $L$, so the extension also changes the squared diagonal by $O_A(N^2L^{-A})$ for every fixed $A$. This does not modify the off-diagonal estimate of §2.

In the fully extended positive rational space the integral can now be inverted **exactly**. At each fixed rational coordinate there are only finitely many terms in $h,u$ and for each such pair at most one nonzero integer $j$ with $j/(hu)=\rho$; the integral converges absolutely there, and (7) and (3) give convergence in norm. At any fixed term, Fourier inversion and $x=(su/A_i)z$ give

$$
 \frac{x_{q,i}}h\int_{\mathbb R}\widehat G_\beta(\tau)
       e(\tau\log(su/A_i))\,\widehat f_{i,\tau}(jx_{q,i}/h)\,d\tau
 =\frac{N}{q l^2 h u}
       \int_{\mathbb R}\Omega(x)e(\beta Nx)
          w(Nx/(su))\,e\!\left(-\frac{jN x}{q l^2 h u}\right)dx .
 \tag{8}
$$

The factor $w_i(z)$ in the inner Fourier transform becomes the actual common $w(Nx/(su))$ once $\Omega$ is present: its normalized argument is then in the bump's plateau. The exact product phase has therefore eliminated all dependence on the dyad other than the location of the actual $u$ label. Sum those disjoint intervals to restore the full $I_d/s$.

## 4. A compact physical sampling bound for the masked divisor norm

In the exact extended diagonal, fix $q,h_1,h_2$ and $g=(h_1,h_2)$. If $j/(h_1u)=j'/(h_2u')$, the true $(u u',N)=1$ again forces
$j=(h_1/g)i_1$, $j'=(h_2/g)i_2$ with $i_1/u=i_2/u'=a/c$ in reduced terms, $c\ge1$, $a\ne0$. Hence $u=cv$, $u'=cv'$ and the two physical frequencies in (8) agree, equal to $a\Lambda_c$ where $\Lambda_c=N/(q l^2 g c)$. Define the actual finite divisor array

$$
 R_c(x)=\sum_{\substack{scv\in I_d\\(cv,lN)=1}}
                   \frac{\mu(cv)}v\,w(Nx/(scv)),
 \qquad F_c(x)=\Omega(x)e(\beta Nx)R_c(x).
 \tag{9}
$$

The integrals on the two arms are now the **same** Fourier transform $\widehat F_c(a\Lambda_c)$, with prefactors $N/(q l^2 h_1c)$ and $N/(q l^2 h_2c)$. In detail, (8) supplies the weight $1/u=1/(cv)$, and summing $v$ on each arm gives (9) with the exact signed $\mu(cv)$ and unit mask. Each $a/c$ produces the indices $i_1=a v$, $i_2=a v'$; conversely these describe all exact equalities. Thus the $h$ pair's contribution to the extended diagonal, with $q(q-1)$ included, is exactly

$$
 \frac{q(q-1)N^2\,\mu(h_1)\mu(h_2)}{q^2 l^4 h_1 h_2}
      \sum_{c\ge1}\frac1{c^2}
          \sum_{\substack{a\ne0\\(a,c)=1}}|\widehat F_c(a\Lambda_c)|^2 .
 \tag{10}
$$

Only here take the absolute value of the two exterior inclusion signs; the signed divisor array remains unchanged. The extension has preserved the nonzero numerator $a$ in the rational sampling, even though residue zero was added to the earlier **modular** positive norm. They are distinct operations.

For any smooth compactly supported $F$ on this fixed physical interval of length less than one, and any $\Lambda>0$,

$$
 \sum_{a\ne0}|\widehat F(a\Lambda)|^2
         \ll \Lambda^{-1}\bigl(\|F\|_2^2+\|F'\|_1^2\bigr).
 \tag{11}
$$

If $\Lambda\le1$, periodize at period $1/\Lambda\ge1$, where the translates of the support are disjoint, and use Fourier Parseval with that period. This gives $\Lambda^{-1}\|F\|_2^2$ even including $a=0$. If $\Lambda>1$, integrate by parts and sum $1/a^2$ over $a\ne0$ for the stronger $\Lambda^{-2}\|F'\|_1^2$. In this second range a numerator-zero sample cannot simply be added. Apply (11) after dropping the coprimality $(a,c)=1$ in the positive sum (10). The normalization identity

$$
 \frac{q(q-1)N^2}{q^2 l^4 h_1h_2}\cdot\frac1{c^2}\cdot\Lambda_c^{-1}
                 =\frac{N(q-1)}{l^2[h_1,h_2]}\cdot\frac1c
 \tag{12}
$$

is the joint unit saving. It is obtained before summing $h$ and avoids any independent inverse-square-root moment over the divisors of $N$.

We now bound the weighted $c$ sum, maintaining the signs of (9) globally across $I_d$. Only $c\le\max(I_d/s)\le N$ can occur, and $1/c\ll L_2\varphi(c)/c^2$ in that range. At each fixed $x$ in the support of $\Omega$, the identity for the signed lcm kernel shows

$$
 \sum_c\frac{\varphi(c)}{c^2}|R_c(x)|^2
   =\sum_{u,u'}\frac{b_x(u)\overline{b_x(u')}}{[u,u']},
 \quad b_x(u)=\mu(u)\mathbf1_{su\in I_d}
                        \mathbf1_{(u,lN)=1}\,w(Nx/(su)).
 \tag{13}
$$

The [reciprocal masked DIT estimate (7)](weak-s-type-ii-critical-prime-unconditional-all-targets.md#1-the-signed-lcm-form-with-the-full-unit-mask) gives an $O(L_2^2)$ squared bound for the signed interval with arbitrary mask $lN\le N^2$. It does not require a proportional interval. At each $x$, the weight $w(Nx/(su))$ as a function of $u$ has bounded sup norm and variation, because $Nx/(su)$ is monotone and the absolute $w$ is one bounded-BV cutoff. The hard $I_d/s$ remains one interval. The bounded-BV weighted version of (13) follows directly by partial summation and Minkowski for the positive lcm norm, expressing the weight as a signed superposition of prefixes on that interval. The cost in norm is at most the sup norm plus total variation. This proves $\|R_c(x)\|_{\ell^2(\varphi(c)/c^2)}\ll L_2$, uniformly in $x$.

For the derivative use the actual global log-coordinate mollification: write $w(k)=W(\log k)$, where

$$
      \|W'\|_\infty+\operatorname{Var}(W')\ll\delta^{-1}.
$$

Indeed the derivative of the convolution of the shrunken interval indicator with a scaled mollifier is a difference of its translates, with sup norm and variation $O(\delta^{-1})$; for the interval too short to retain, use the zero cutoff. Since $x\asymp1$ on the physical support, the differentiated weight in (13) is
$\partial_x w(Nx/(su))=W'(\log(Nx/(su)))/x$, with sup norm plus variation in $u$ bounded by $O(\delta^{-1})$. Hence $\|R_c'(x)\|_{\ell^2(\varphi(c)/c^2)}\ll L_2\delta^{-1}$ by the same signed interval norm. The product $\Omega(x)e(\beta Nx)$ has bounded sup norm and its derivative has $L^1$ norm $O(1)$, using $|\beta|N\ll1$. Integrating over a fixed-length physical interval and taking Minkowski for the derivative yields

$$
 \sum_c\frac{\varphi(c)}{c^2}\|F_c\|_2^2\ll L_2^2,\qquad
 \sum_c\frac{\varphi(c)}{c^2}\|F_c'\|_1^2\ll L_2^2\delta^{-2}.
 \tag{14}
$$

Thus the $1/c$-weighted expression in (11)–(12), summed over $c$, is $O(L_2^3\delta^{-2})$.

Finally use $\sum_{q\in\mathcal Q}(q-1)\ll N/L$ and
$\sum_{h_1,h_2\mid\operatorname{rad}N}1/[h_1,h_2]=\prod_{p\mid N}(1+3/p)\ll L_2^3$. Equations (10)–(14) bound the full integrated rational diagonal in (5) at each fixed $(l,s,\beta)$ by

$$
                              O\left(\frac{N^2\delta^{-2}L_2^6}{L l^2}\right).
 \tag{15}
$$

No use of GRH and no factor counting dyads appears in (15). The signs used in (13)–(14) run over the whole actual interval: bounding the Fourier samples separately by the energy of dyadic packets would not recover (15).

## 5. The genuine original shell

Combine (15) and its rational restoration with the nonzero-determinant error in §2. Now use Minkowski only over the $(l,s)$ labels, with $\sum_{l\le T}\tau_{\rm d}(l)/l\ll L_2^2$ in norm. Extend back to the actual additive nonprincipal component using the original $\tau$ and dual tail estimates, and the bounded factor $q/(q-1)$ in its finite Gauss expansion. After squared estimates and the real $\beta$ interval of length $1/(5N)$, its energy is

$$
                     O\left(\frac{N\delta^{-2}L_2^{10}}{L}\right)+O(NL^{-2}).
$$

The actual principal character and original $q$-nonunits are not the artificial additions in (5). Their estimates from [the joint theorem, §4](weak-s-type-ii-critical-prime-cross-dyad-subpolynomial-grh.md#4-actual-nonunits-and-the-literal-complete-shell) apply unchanged to this full polynomial admissible interval. In particular when $q\mid N$ the actual long unit precludes nonunits; otherwise write $d=qsu$ in the nonunit piece, keep the true signed $\mu(u)$ with mask $lNq$, and use the original uniform bounded-variation physical factor at fixed $k$. The signed Mertens bound on $u\ge\exp(L_2^5)$ and reciprocal count below give uniformly $O(XL_2^6)$ per $q,\beta$, independently of the number of dyads. Their shell energy is $O(NL_2^{12}/L)$. For the actual principal unit term use its true numerator-zero ordinary polynomial value minus these nonunits, the ordinary squared norm $O(N)$ in §1, and $\sum_q (q-1)^{-1}\ll1/L$, as there. These two contributions are dominated by the displayed nonprincipal bound.

The original arcs are disjoint. Ordinary Parseval therefore transfers the genuine common smoothing error $O(N\delta)$ and the smaller squarefree and short-unit truncation errors to the shell. This proves (2); choose $\delta=(L_2^{10}/L)^{1/3}$, which lies in the stated range for sufficiently large $N$, to obtain the explicit rate and (1). The true $P$ and $D$ have ordinary norm $O(\sqrt N)$, so Cauchy and contraction of separate centering prove the first two signed bounds. Apply the [exact parity-preserving identity](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md) only after restoration of the true odd supports and original product geometry, with its error $O(N/L+N(X/M)^2)$; this gives the third signed bound. Neither the auxiliary rational diagonal nor its unit-truncated coefficients have been substituted for the genuine odd signed residual.
