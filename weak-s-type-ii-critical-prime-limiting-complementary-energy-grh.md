# A positive limiting constant for genuine critical-shell energy on powers of two

Let $N=2^J$, $J\to\infty$ through integers, $X=\sqrt N$, $L=\log N$, and $e(z)=e^{2\pi i z}$. Use exactly the [genuine energy example](weak-s-type-ii-critical-prime-sharp-complementary-energy-example-grh.md):

$$
 \begin{gathered}
 I_d=[X,1.01X],\qquad I_k=(\max(N^{.49999},.42X),.50X),\qquad y=9N/16,\\
 D_m=\mathbf1_{7N/16\le m<N/2}
        \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                         (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_m D_m e(\alpha m).
 \end{gathered}
$$

Let $\mathcal Q=[.8X,.9X]\cap\mathbb P$, let $|\beta|\le1/(10N)$, and denote by $\Pi_q$ the orthogonal projection off the constant vector on the nonzero numerators $a=1,\ldots,q-1$. The full energy $\mathcal E_N(D)$ uses the squared sum over those numerators at $a/q+\beta$, summed over $q\in\mathcal Q$ and integrated over $\beta$. Write $\mathcal E_N^0(D)$ for the corresponding energy after applying $\Pi_q$ in each group.

**Theorem (global Dirichlet GRH).** Assume GRH for all primitive Dirichlet $L$-functions, including $\zeta$. There is a constant $C_{\rm ex}\in(0,\infty)$, specified by the convergent finite-integral approximations below, such that

$$
        \mathcal E_N(D)\sim C_{\rm ex}\frac{N}{\log N},
        \qquad
        \mathcal E_N^0(D)\sim C_{\rm ex}\frac{N}{\log N}.
$$

The conclusion concerns the one stated shell and the one family of actual hard cuts. It is a complementary energy asymptotic, not a lower bound for a signed prime pairing, an individual compensated offset, or Hypothesis S.

## 1. Replace the true energy by its coherent rational diagonal

Use the original inward cutoffs $\Omega(x)$ and $w(k)=W(\log k)$ at $\delta=L^{-2}$ from [the literal transfer](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#1-actual-transfers-at-the-smaller-smoothing-width). These weights are in $[0,1]$, of bounded variation uniformly, and equal their hard indicators away from the genuine endpoint strips. For large $N$, $N^{.49999}<.42X$, so the lower cofactor endpoint is $.42X$. The square cutoff is $T=L^{16}$. The approximated polynomial, denoted $D^\dagger$, uses the exact long unit and the common signed squarefree odd labels $l\le T$, $s=(l,d)\mid l$, $d=su$, $(u,2l)=1$. Its remaining parity labels are exactly $h=1,2$, with the true short variable $k$ a positive multiple of $l^2h/s$. The scalar sign is $\mu(l)\mu(s)\mu(h)\mu(u)$. The ordinary squared error from the hard polynomial is $O(NL^{-2})$ including the smaller arithmetic cutoff errors. Consequently disjointness of the actual arcs and ordinary Parseval bound the squared error in each of the full and centered shell norms by $O(NL^{-2})$ as well.

For fixed $q,\beta$ define the completed physical rational array, with coordinate $\rho\in\mathbb Q\setminus\{0\}$, by

$$
 \mathcal R_q(\rho;\beta)=
 \sum_{\substack{l\le T,\ l\ \mathrm{odd\ squarefree},\ s\mid l,\ h=1,2\\
                  su\in I_d,\ (u,2l)=1\\
                  \rho l^2 h u\in\mathbb Z\setminus\{0\}}}
 \frac{\mu(l)\mu(s)\mu(h)\mu(u)N}{q l^2 h u}
       \int_{\mathbb R}\Omega(x)e(\beta Nx)w(Nx/(su))e(-\rho Nx/q)\,dx .
 \tag{1}
$$

Set

$$
 \mathscr D_N=
  \int_{-1/(10N)}^{1/(10N)}
       \sum_{q\in\mathcal Q}q(q-1)\sum_{\rho\ne0}|\mathcal R_q(\rho;\beta)|^2\,d\beta .
 \tag{2}
$$

Then

$$
              \mathcal E_N^0(D)=\mathscr D_N+o(N/L),
              \qquad \mathcal E_N(D)=\mathscr D_N+o(N/L).
 \tag{3}
$$

Here is the two-sided justification of (3). The [coherent construction, §1](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#1-complete-the-square-only-after-adding-the-square-labels) first forms its finite modular vector on the residue $l^2 h u/j\bmod q$. In the present fixed cuts, $q\nmid d$ since $q<X$ and $2q>1.01X$, and $k<X/2<q$, so the artificial residue-zero term vanishes. The [exact subtraction of the artificial principal](weak-s-type-ii-critical-prime-sharp-complementary-energy-example-grh.md#3-subtract-the-artificial-term-and-return-to-actual-numerator-energy) gives cost $O(N^{1.8}L^{O(1)})$, uniformly before the $\beta$ integral. The total of the off-diagonal integer determinants $bq\ne0$ is $O(N^{1.91}L^{O(1)})$ by the same global Dirichlet GRH argument, also uniformly in $\beta$. On the exact zero determinant only, restoring the full rational indices and physical Fourier inversion changes the squared norm by $O_K(N^2L^{-K})$ for every fixed $K>0$ and gives (1). The actual additive normalization has an extra factor $q/(q-1)$ on each positive finite nonprincipal character norm; replacing that factor by $1$ changes the squared norm by relative $O(X^{-1})$. Since the completed rational norm at fixed $\beta$ is $O(N^2/L)$ by the coherent upper bound, these errors give $o(N/L)$ after integration. The finite time and dual truncations also have negligible error in the actual nonprincipal sampled norm, as in the same construction. This proves the first equality of (3) for $D^\dagger$. The true hard transfer follows by norm triangle and $\mathscr D_N=O(N/L)$; the cross term from the squared error $O(NL^{-2})$ is $O(NL^{-3/2})$.

For the full energy it remains to see that the **actual**, rather than artificial, constant on each nonzero-numerator group is negligible. For $D^\dagger$ every term remains a $q$-unit, as above, so this group mean equals $-D^\dagger(\beta)/(q-1)$. At fixed $l,s,h,k$ evaluate the signed $u$ sum first. Its hard prefix is at scale $U=X/s$, with $\mu(u)$ and the true mask $(u,2l)=1$. The factor $\Omega(suk/N)e(\beta s u k)$ has uniformly bounded sup norm and variation in $u$: the physical phase has bounded variation on the fixed supported $x=suk/N$ interval since $|\beta|N\le.1$. The inherited GRH additive Möbius bound, at zero frequency and then by partial summation with this weight, gives $O(U^{4/5})$. The short weights $w(k)$ are bounded and there are $O(X)$ choices of $k$, even before the multiple test. Summing the fixed-polylogarithmic number of $l,s$ and the two $h$ labels gives

$$
                 |D^\dagger(\beta)|\ll N^{.9}L^{O(1)} .
$$

Since $\sum_{q\in\mathcal Q}(q-1)^{-1}\ll L^{-1}$ and the $\beta$ interval has length $1/(5N)$, the actual constant energy of $D^\dagger$ is $o(N/L)$. The hard-cut approximation has smaller squared norm, so the second equality of (3) follows as well.

## 2. Uniform truncations that leave a finite-dimensional limit

Use three fixed cutoffs $B\ge2$, $0<\varepsilon<1$, and $A\ge1$. In (1) retain only $l\le B$, and in (2) retain only reduced $\rho=a/c$ with $a\ne0$, $(a,c)=1$, $c\ge\varepsilon X$, and $|a|\le A$. Denote this resulting positive integrated form by $\mathscr D_N(B,\varepsilon,A)$. For any fixed $0<\theta<1$, uniformly for all large enough $N$ (so $T\ge B$), the following normalized tail estimates hold:

$$
 \frac{L}{N}\left|\mathscr D_N-\mathscr D_N(B,\varepsilon,A)\right|
   \ll_\theta B^{-\theta}+O_B(\varepsilon)+O_{B,\varepsilon}(A^{-1}) .
 \tag{4}
$$

For the first truncation, expand the square and use the absolute paired-label Euler majorant of [the coherent proof, §2](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#2-factor-the-common-rational-denominator-before-the-square-label-sum). In the paired product a prime exclusive to one square label costs $O(p^{-2})$, and a prime shared by both also costs $O(p^{-2})$. Multiplying that nonnegative majorant by $l_i^{\theta}$, for either fixed side $i$, changes these prime costs at most to $O(p^{-2+\theta})$, still absolutely summable. The contribution of all pairs with either label above $B$ therefore costs $O_\theta(B^{-\theta})$ times the original scale. This comparison is valid on the exact signed form: the coherent absolute bound is taken only after the actual same-gcd $h$ grouping within each square-label pair, and cutting $l$ is independent of $h$.

For clarity, take a fixed pair $l_i,s_i,h_i$ for $i=1,2$, with $b_i=l_i^2h_i$, and a reduced coordinate $a/c$. Both arms can contribute only when $c\mid b_i u_i$. Let $c_i=c/(c,b_i)$, and write $c=c_0m$ where $c_0$ is supported on $2l_1l_2$, $(m,2l_1l_2)=1$. On nonzero squarefree long support $c_i=m_i m$, where $m_i$ is the part of $c_0$ supported on the primes exclusive to the other $l$ label. The local list established in the coherent proof is exact: the exponent of $2$ in $c_0$ is at most one, and may be one only when $h_1=h_2=2$; primes in both $l_i$ have exponent at most two, and primes in just one at most one. Thus for fixed labels there are finitely many $c_0,m_i$ and all are independent of $N$; for this fixed-$B$ argument absolute values may also be taken over the finitely many $h$ labels. On any nonzero support, $c\le b_i u_i\le 2.02B^2 X$.

For the small-denominator truncation, fix these labels and $c_0$ and apply Cauchy to the two transformed arms in the remaining coordinates $(m,a)$ with weight $m^{-2}$. The physical sample step is $C_*/m$ with $C_*=N/(qc_0)$. If $c=c_0m<\varepsilon X$, then $m/C_*<.9\varepsilon$ by $q\le.9X$, so only the sparse integration-by-parts estimate of [the inverse-logarithmic sampling proof, §3](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#3-keep-the-stronger-sparse-sampling-bound-and-integrate-the-actual-derivative) is needed. It has squared sampled weight $C_*^{-2}$ times the integrated physical derivative squared. For the derivative on $\Omega(x)e(\beta Nx)$, use

$$
                    C_*^{-2}\le\frac{.9\varepsilon}{C_*m}
$$

on this range, and apply the same masked signed reciprocal norm at the exact $I_d/(s_i m_i)$, with mask $2l_i m_i$. For the derivative on the genuine $w(Nx/(s_i m_i m v))$, its individual integrated $L^1$ norm is $O(1)$ by the same two-endpoint argument; at most $.9\varepsilon C_*$ positive $m$ are involved. Thus each square after Cauchy has bound $O_B(\varepsilon/C_*)$. Multiplying by the original paired factors and summing the fixed labels, $q$, and $\beta$ gives $O_B(\varepsilon N/L)$. Numerator zero is not added anywhere.

For the large-numerator truncation, $c\in[\varepsilon X,2.02B^2 X]$. For each such $c$ and the fixed pair, $c_i\ge\varepsilon X/(2B^2)$. The reciprocal $v$ sum in each transformed arm is now individually bounded, since the $v$ interval has fixed ratio $1.01$ and in fact $v\le2.02 B^2/\varepsilon$. The physical derivative on $\Omega(x)e(\beta Nx)$ therefore has $L^1$ norm $O_{B,\varepsilon}(1)$ after multiplication by that reciprocal sum; the cofactor derivative has the same bound by the integrated endpoint estimate. As $N/(qc)\gg_B1$, integration by parts bounds each transform at $aN/(qc)$ by $O_{B,\varepsilon}(1/|a|)$. The arm prefactor $N/(q b_i c_i)$ is $O_{B,\varepsilon}(1)$. Summing $a^{-2}$ over $|a|>A$, then $O_B(X)$ denominators and $\sum_q q(q-1)\ll X^3/L$, gives $O_{B,\varepsilon}(A^{-1}N^2/L)$ before the $\beta$ integration. This proves (4).

## 3. The finite integrals and their limit

We give a formula for the finite constant $C(B,\varepsilon,A)$ representing the limit of $(L/N)\mathscr D_N(B,\varepsilon,A)$. Sum over odd squarefree $l_1,l_2\le B$, $s_i\mid l_i$, $h_i=1,2$, and enumerate $c_0,m_1,m_2$ by the exact local list in §2. Sum also over positive integers $v_i\le 2.02B^2/\varepsilon$ with $(v_i,2l_i m_i)=1$, and over integers $0<|a|\le A$ with $(a,c_0)=1$. The endpoint values in these finite sums are ordinary real bounds on integer variables. For each choice set

$$
 \begin{split}
 M_0&=\operatorname{rad}(2l_1l_2|a|v_1v_2),
   & d(M_0)&=\frac{1}{\zeta(2)}
                    \prod_{p\mid M_0}(1+1/p)^{-1},\\
 \kappa_i&=\frac{\mu(l_i)\mu(s_i)\mu(h_i)\mu(m_i)\mu(v_i)}
                    {l_i^2 h_i m_i v_i},
   & D_i(z)&=\mathbf1_{1\le s_i m_i v_i z\le1.01}.
 \end{split}
 \tag{5}
$$

For $\xi\in[.8,.9]$, $\eta\in[-.1,.1]$ and $z>0$, put

$$
 H_i(\xi,\eta,z)=
     \int_{7/16}^{1/2}
           \mathbf1_{.42<x/(s_i m_i v_i z)<.50}\,
           e\big((\eta-a/(\xi c_0 z))x\big)\,dx .
 \tag{6}
$$

The finite sum is

$$
 \begin{split}
 C(B,\varepsilon,A)=2
   \sum_{\text{labels in (5)--(6)}} d(M_0)\kappa_1\kappa_2
     \int_{.8}^{.9}\int_{-.1}^{.1}
        \int_{\varepsilon/c_0}^{\,2.02 B^2/c_0}
       \frac{D_1(z)D_2(z)H_1(\xi,\eta,z)\overline{H_2(\xi,\eta,z)}}{z^2}
                 \,dz\,d\eta\,d\xi .
 \end{split}
 \tag{7}
$$

This expression is real and nonnegative by its limiting interpretation below; it does not take absolute values of the cross terms.

Indeed, at fixed labels write $z=m/X$, $\xi=q/X$, $\eta=\beta N$. The reduced coordinate contributes to arm $i$ with $u_i=m_i m v_i$. The harmonic prefactor in (1) becomes $1/(\xi l_i^2 h_i m_i v_i z)$. The exact hard condition on $u_i$ is $D_i(z)$. The remaining integral in each arm converges to (6) uniformly on the indicated compact ranges. To see this, the omitted physical endpoint strips have length $O(\delta)$, and the cofactor endpoint strips in $x$ are of length $O_{B,\varepsilon}(\delta)$ after multiplication by the bounded scales $s_i m_i v_i z$. The phase is bounded in absolute value by one. The uniform replacement follows without differentiating an indicator. The final integer unit $(a,c)=1$ imposes $(m,|a|)=1$ after $(a,c_0)=1$; all other nonzero sign tests precisely impose $(m,M_0)=1$ and squarefreeness of $m$. Under those tests the product of the two Möbius factors for $u_i=m_i m v_i$ is $\mu^2(m)\mu(m_1)\mu(v_1)\mu(m_2)\mu(v_2)$. The exact Möbius signs therefore give (5). Outside those tests either an original mask or a squarefree sign vanishes, so no artificial mass is added.

For fixed $M_0$ the number of squarefree $M_0$-units in a prefix of length at most $O_B(X)$ is $d(M_0)$ times the length plus $O_{M_0,B}(\sqrt X+1)$. This follows by expanding $\mu^2(m)=\sum_{d^2\mid m}\mu(d)$, applying the fixed unit inclusion at each $d$ coprime to $M_0$, and bounding the tail of the convergent density. It also applies to hard intervals upon taking prefix differences. Thus the scaled empirical measure for $z=m/X$ converges to $d(M_0)\,dz$ on the finite bands used here. The prime number theorem likewise gives $d\xi$ after scaling the prime sum by $\log X/X$ on $[.8,.9]$. These two measures are independent sums; the integrand in (7) is jointly bounded and continuous off the finitely many long-gate boundary planes in $z$. More explicitly, the endpoints of the $x$ integration in (6) are maxima and minima of continuous functions, and extending by zero at an empty interval gives continuity. Fixed rectangular approximation or interval-prefix differences thus give the joint Riemann limit, with the continuous $\eta$ integral on its fixed compact interval. The prefactor $q(q-1)$ cancels the two inverse $\xi$ factors, leaving $X^2(1-1/q)$. Changing from $\beta$ to $\eta$ divides this by $N$. The two empirical measures contribute $X^2/\log X$ before the outer normalization $L/N$, so the remaining factor is exactly $2=L/\log X$. This establishes

$$
              \lim_{J\to\infty}\frac{L}{N}\mathscr D_N(B,\varepsilon,A)
                        = C(B,\varepsilon,A).
$$

By (4), first choose $B$ large, then $\varepsilon$ small for that fixed $B$, then $A$ large for both. The resulting normalized finite form approximates the original uniformly for all sufficiently large $J$ with arbitrarily small error. This proves existence of the limit $C_{\rm ex}$ and identifies it with the corresponding iterated limit of (7), namely take $A\to\infty$ first for fixed $B,\varepsilon$, then $\varepsilon\downarrow0$ for fixed $B$, then $B\to\infty$. The same tail inequalities control the Cauchy differences at each of these steps. Its finiteness follows from the coherent upper bound; its strict positivity follows from the actual centered lower bound in the fixed example. Equation (3) now proves the two asserted asymptotics, with no inference about the sign or size of any prime pairing.
