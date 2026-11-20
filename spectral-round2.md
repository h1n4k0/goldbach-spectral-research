# Operator-norm certification at a fixed modulus

**Status.** This note gives a finite reduction with an explicit error budget for the Hardy operator in [Li and Liu, *A Conditional Proof of the Goldbach Conjecture*](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf), using its actual normalization. It assumes `GRH(N)` for the analytic operator and the correlation estimate. This is a certification procedure, **not an implemented computation**. The bounds are deliberately conservative and do not establish either eventual hypothesis.

## 1. Exact coordinate representation

Fix admissible even $N>e^{10}$ and write $\alpha=1/\log N$, $\beta=1/8$, $\rho(u)=e^{-2\alpha u}+e^{-2\beta u}$. For $h(s)=\int_{\mathbb R}\phi(u)e^{-su}\,du$, Plancherel on the two boundary lines gives
$$
 \|h\|_{H_N}^2=2\pi\int_{\mathbb R}|\phi(u)|^2\rho(u)\,du.
 \tag{1}
$$
This is Lemma 5.2 with the change of sign in the log coordinate and with the Fourier normalization absorbed into $\phi$. Integrals first defined on compactly supported coefficients extend by this isometry. In these coordinates three types of atoms in $T_N=\mathcal P_N-\mathcal D_N-\mathcal K_N$ take elementary forms:

* **Correlation.** For each odd character modulo $N$ the atom $g_\chi(s)/(1+s)$, where $g_\chi(s)=L'/L(1/2+s,\chi)$, has coefficient
$$
 \phi_\chi(u)=-\mathbf1_{u\ge0} e^{-u}
       \sum_{n\le e^u}\Lambda(n)\chi(n)\sqrt n. \tag{2}
$$
For $\Re s>1/2$ this follows from absolute convergence and integration of each summand on $[\log n,\infty)$. Under GRH the ordinary nonprincipal character estimate $|\psi(x,\chi)|\le C_{\psi,N}\sqrt{x}(1+\log N+\log x)^2$ has an effective constant, used here with a common $C_{\psi,N}$ for fixed modulus. For an explicit input, see [E. S. Lee, *The prime number theorem for primes in arithmetic progressions at large values*, Thm. 4.2](https://arxiv.org/abs/2301.13457) in its range $x\ge\max(N,e^{10})$; use $|\psi(x,\chi)|\le x\log x$ for the finite lower range if needed. Lee's nonprincipal proof uses the inducing primitive function and RH for $\zeta$ in §3; conductor $1$ divides $N$, so these hypotheses are covered by $\mathrm{GRH}(N)$. Partial summation gives $|\phi_\chi(u)|\le(3/2)C_{\psi,N}(1+\log N+u)^2$ on $u\ge0$. Thus (2) belongs to (1), its transform is holomorphic for $\Re s>0$, and the identity extends there. On a finite cut $[0,U]$ it is exactly a step function times $e^{-u}$, with finitely many breaks at $\log n$.
* **Diagonal.** $d_n(s)=n^{-s}/(1+s)$ has coefficient $D_n(u)=\mathbf1_{u\ge\log n}e^{-(u-\log n)}$; its squared norm is at most $2\pi n^{-2\alpha}$.
* **Beta.** $F_x(s)=x^sX_1(s)/(1+s)$ for $x>0$, where $X_1(s)=\Gamma((3/2-s)/2)/\Gamma((3/2+s)/2)$, has coefficient $B(u+\log x)$ with
$$
 B(v)=\frac{2e^{-v}}{\sqrt\pi}\int_0^{e^v}\sqrt t\,\sin(2t)\,dt. \tag{3}
$$
Indeed $(1+\partial_v)B=(2/\sqrt\pi)e^{v/2}\sin(2e^v)$, so bilateral integration by parts followed by $t=e^v$ gives $(1+s)\mathcal L B(s)=(2/\sqrt\pi)\int_0^\infty t^{-1/2-s}\sin(2t)dt$. The sine integral with exponent $a=1/2-s$, gamma duplication, and reflection give $X_1(s)$ for $\alpha\le\Re s\le\beta$. Integration by parts here is justified at both endpoints by the following bounds, and the derivative's transform can be taken as the limit of truncated intervals. From $|\sin(2t)|\le2t$ and one ordinary integration by parts,
$$
 |B(v)|\le\frac{2}{\sqrt\pi}
 \begin{cases}e^{3v/2}&v\le0,\\e^{-v/2}&v\ge0.\end{cases} \tag{4}
$$
In particular the use of (3) never needs numerical quadrature of an $L$-function or high vertical values of the gamma quotient.

## 2. Explicit error budget for a finite-rank operator

All the following bounds are in operator norm; for the beta term they are obtained in the stronger trace norm. Errors can be assigned separately and added. For vectors $v,w$, $v\otimes w$ means $h\mapsto\langle h,w\rangle v$.

**Correlation.** Let $Q_U$ be restriction of the log-coordinate coefficient to $[0,U]$, considered as an orthogonal projection by (1). Keep all odd characters, replace atoms $p_\chi=g_\chi/(1+s)$ by $Q_Up_\chi$, and put $\mathcal P_{N,U}=\frac{2}{\varphi(N)}\sum_{\chi\text{ odd}}Q_Up_\chi\otimes Q_Up_\chi$. Set
$$
 E_P^2=9\pi C_{\psi,N}^2\int_U^\infty (1+\log N+u)^4e^{-2\alpha u}\,du.
$$
Then $\|p_\chi-Q_Up_\chi\|\le E_P$ for each $\chi$, and by the rank-one triangle inequality and Cauchy–Schwarz,
$$
 \|\mathcal P_N-\mathcal P_{N,U}\|
 \le 2 E_P\sqrt{\operatorname{tr}\mathcal P_{N,U}}+E_P^2.\tag{5}
$$
The traces in (5) are positive finite sums, and the integral defining $E_P$ is an elementary polynomial times an exponential. The truncation in (2) must restrict the **coefficient** in $u$; dropping all summands with $n>e^U$ without restricting $u$ leaves a different extension above $U$.

There is no need to enumerate characters in the finite matrix. For a unit residue $amod N$, let $r_a$ be the vector with coefficient $mathbf1_{0le ule U}e^{-u}sum_{nle e^u,, nequiv amod N}Lambda(n)sqrt n$. Odd-character orthogonality gives
$$
 mathcal P_{N,U}
 = sum_{{a,-a}} (r_a-r_{-a})otimes(r_a-r_{-a}),
$$
where each unordered unit-residue pair is used once. This is the same positive Gram operator, with neither a character evaluation nor a primitive-conductor lookup in the finite part. Its trace and all correlation–correlation Gram entries reduce to finite sums over intervals on which the residue counts are constant after factoring out $e^{-u}$.


**Diagonal.** Use $\mathcal D_{N,M}=\sum_{n\le M,(n,N)=1}(\Lambda(n)^2/n)d_n\otimes d_n$. For integer $M\ge e^2$,
$$
 \|\mathcal D_N-\mathcal D_{N,M}\|
 \le E_D:= 2\pi\int_M^\infty (\log x)^2 x^{-1-2\alpha}\,dx. \tag{6}
$$
Here $\Lambda(n)^2\le(\log n)^2$, and the majorant is decreasing above $M$. Prime estimates could make this less conservative.

**Beta model.** Put $A_x=F_x\otimes F_x$. The trace-class representation in the first spectral note uses
$$
 Z=-\int_0^1 A_x\,dx/x
 +\sum_{n\ge1}\left(A_n/n-\int_n^{n+1}A_x\,dx/x\right);
 \qquad \mathcal K_N=S\sum_{d\ge1}b_d M_d ZM_d^*. \tag{7}
$$
Here $S=\mathfrak S(N)$, $M_d$ multiplies by $(\pi/(Nd))^s$, and $P_N(w)=\sum b_d d^{-w}=\prod_{p>2,p\nmid N}(1+p^{-w}/(p-2))$. The scalar kernel identity for (7) is Euler summation of $\zeta(1-w)$, including its term $-1/w$.

One can obtain constants directly, without an unspecified Stirling error: (1) and (4) give $\|F_x\|\le 6m(x)$ where $m(x)=\max(x^\alpha,x^\beta)$. For $0<h\le1$ the derivative identity for $B$ gives
$$
 |B(u+h)-B(u)|\le
 \begin{cases}20h e^{3u/2}&u<0,\\20\min(he^{u/2},e^{-u/2})&u\ge0.\end{cases}
$$
For the first bound split the derivative integral if $u+h$ crosses zero; then $u>-1$ gives the same constant. For the second use both the derivative bound and (4). Splitting the positive-part norm integral at $u=\log(1/h)$ gives $\|F_{xe^h}-F_x\|\le128m(x)h^{1/2+\alpha}$. Hence $\|A_{xe^h}-A_x\|_1\le2048m(x)^2\sqrt h$.

Take integers $B_0,D_0\ge1$, $V>0$, and subdivide the log interval $[-V,\log(B_0+1)]$ with left endpoints $a_i$ and widths $h_i\le h\le1$. Use the finite sum
$$
 Z_* =\sum_{n\le B_0} A_n/n-\sum_i h_i A_{e^{a_i}},
 \qquad \mathcal K_{N,*}=S\sum_{d\le D_0}b_d M_d Z_* M_d^*.
$$
The three sources of $Z$ error are the omission of $x<e^{-V}$, omission of paired intervals above $B_0+1$, and the log quadrature:
$$
 \|Z-Z_*\|_1\le E_Z:=
 \frac{18}{\alpha}e^{-2\alpha V}+8400 B_0^{-1/4}
 +2048\sqrt h\left(\frac1{2\alpha}+\frac{(B_0+1)^{2\beta}}{2\beta}\right).
 \tag{8}
$$
For the middle estimate each paired term has trace norm at most $2100n^{2\beta-3/2}$, by adding and subtracting $A_n/x$ under the integral; $2\beta=1/4$. The same bounds yield $\|Z\|_1\le 18/\alpha+10500=:C_Z$. Since $\|M_d\|\le(\pi/(Nd))^\alpha$, the full error is at most
$$
 E_K:= S(\pi/N)^{2\alpha}
   \left[P_N(2\alpha)E_Z+P_N(\alpha)D_0^{-\alpha}C_Z\right].
 \tag{9}
$$
For a fully explicit majorant for the products one can use $N^{-\sigma}SP_N(\sigma)\le2e^{3/2}(1+1/\sigma)$ for $0<\sigma\le2\beta$: compare factors with $\zeta(1+\sigma)$ as in the source's §6.4.2, and bound the remaining product by $\exp(\sum_{j\ge3}2/(j(j-2)))=e^{3/2}$. Factors at primes dividing $N$ cost at most $N^\sigma$. The finite rank expression itself uses only $b_d$ for finite $d$; $S$ can be computed with a controlled tail by $|\log(1-(p-1)^{-2})|\ll(p-1)^{-2}$ and the elementary integer series tail.

## 3. Norm and zero certification

Let $A=\mathcal P_{N,U}-\mathcal D_{N,M}-\mathcal K_{N,*}$ and $\varepsilon=2 E_P\sqrt{\operatorname{tr}\mathcal P_{N,U}}+E_P^2+E_D+E_K$. Then $\|T_N-A\|\le\varepsilon$, and $\varepsilon$ can be made arbitrarily small for a fixed admissible $N$. The ranges of $A$ are spanned by the retained atoms. If $W$ is their span and $Q_W$ its orthogonal projection, then $\|T_N-Q_WT_NQ_W\|\le2\varepsilon$. Moreover any eigenvector $T_Ne=\mu e$ with $\mu\ne0$ obeys $\|(1-Q_W)e\|\le(\varepsilon/|\mu|)\|e\|$. Thus the approximation includes a quantitative localization statement for all modes above any chosen magnitude threshold, not just agreement on a chosen Mellin test.

Write $A=V C V^*$ with columns of $V$ the atoms and $C$ the signed diagonal coefficients. Form the finite Gram matrix $G=V^*V$ via (1)–(4). For a beta multiplier, $M_d F_x=F_{\pi x/(Nd)}$, so the coefficients remain explicit shifts of (3). All integrals on bounded intervals can be enclosed by subdividing at the $\log n$ breaks and using interval integration; the cutoffs on the unbounded ends have exponential tails from (4) and the shifted exponentials. In (3) substituting $t=w^2$ makes its finite inner integral smooth at zero. On ranges with large $e^u$ rigorously integrating rapidly oscillatory terms may be costly, but in principle it suffices to refine on a finite interval. No approximate sample of beta or correlation kernel values is needed.

The nonzero spectrum of $A$ is that of $G^{1/2} C G^{1/2}$, using the polar decomposition of $V$ on the support of $G$. This formulation handles dependent atoms without trying to invert a Gram matrix. Certified enclosure of this finite Hermitian spectrum, plus Weyl's error bound $\varepsilon$, decides strict inequality versus a proposed norm threshold whenever the enclosures separate. For an ordered positive or negative eigenvalue lying above the relevant uncertainty, interval bounds for its magnitude larger than $\delta_N$ translate monotonically into bounds for the exceptional real roots
$$
 \frac12\ \pm\ \frac12\sqrt{1-\delta_N^2/|\mu|^2}.
$$
Intervals straddling $\delta_N$ leave line-versus-off-line status unresolved. The $\mathcal S_1$ bound from the first note independently gives $s_j(T_N)\ll(\log N)^2/j$, so sufficiently small modes can never produce exceptions; this does not identify the exceptional directions. Equality at a norm threshold is also not decided by an arbitrarily narrow two-sided interval alone.

**Scope.** At fixed $N$ all these are constructive analytic estimates, conditional on GRH for the correlation continuation. The finite Gram dimensions can be enormous, because the chosen absolute error tails are not adapted to signed cancellation and the analytic strip approaches the critical line with $N$. No modulus was certified by this note and finite evidence, whether for or against a single instance, is not the paper's eventual assertion. The remaining obstacle is uniform control as $N$ varies, not the formal existence of a finite approximation for each individual operator.
