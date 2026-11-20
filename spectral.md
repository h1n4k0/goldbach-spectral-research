# The residual has two infinite spectral tails, but only finitely many candidate obstructions

**Status.** These are deductions from the Hardy operator of [J. Li and J. Liu, *A Conditional Proof of the Goldbach Conjecture*](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf), Shandong University version posted 13 November 2026. They concern the actual operator, not a sampled matrix. They establish neither Hypothesis S nor Hypothesis R and do not give a counterexample to either. No claim of priority is made.

Let $N>e^{10}$ be even and satisfy the paper's $\mathrm{GRH}(N)$. Put $L=\log N$, $\alpha=1/L$, $\beta=1/8$, $\Delta=\beta-\alpha$, $S=\mathfrak S(N)$, and $\delta=(S/N)^{1/2}L^{3/2}$. Use the **sum**, not the average, of the boundary $L^2$ norms on the strip. We prove
$$
 \sum_j|\mu_j(T_N)|\ll L^2,\qquad
 \lambda_j^+(T_N),\ |\lambda_j^-(T_N)|\gg_I
       \frac{S}{(j+r_I)^2}\quad(j\ge1),\qquad
 \|T_N\|\gg_I\frac{S}{1+r_I}.
$$
Here $I$ is a fixed nonempty interval compactly contained in $(1/3,1/2)$, and $r_I$ counts its distinct points $n/N$ for which $n$ and $N-n$ are unit prime powers (primes included). The signed sequences are ordered towards zero on their respective half-lines. Constants do not depend on $j$ or $N$. In particular, $T_N$ is trace class but is **not** in the Schatten class $\mathcal S_{1/2}$.

## 1. An exact complementary-interval test

For a real $f\in C_c^\infty(0,1)$, let $v_f$ be the representing vector obtained by using $\Phi_f(u)=\sqrt{u}\,f(u)$ in the paper's Mellin functional. Set $\nu_N=N^{-1}\sum_{0<n<N,(n,N)=1}\Lambda(n)\Lambda(N-n)\,\delta_{n/N}$. For two such weights one has
$$
 B_N(f,g):=\langle T_Nv_f,v_g\rangle
 =\int_0^1 f(u)g(1-u)\,[S\,du-d\nu_N(u)]. \tag{1}
$$
The weights in this identity need not be even under reflection or nonnegative. Here is the extension beyond the paper's preferred test. For a single real test, the two positive difference congruences have no off-diagonal contributions inside $(0,N)^2$; the negative congruence retains only $n+m=N$. On the continuous side, write $C(y)=\int f(u)f(u+y)du$, $J(y)=\int f(u)f(y-u)du$, with zero extension. The Mellin transform of $2C-J$ at 1 is zero: the sum of the two difference masses and the sum-variable mass both equal $(\int f)^2$. Thus no residue is picked up at the density-series pole in the contour shift of Lemma 7.2. At integer $k\ge1$, $C(k)=0$ and $J(k)=0$ unless $k=1$. This gives (1) on the diagonal. Its real polarization gives the stated formula because the measure is reflection invariant and the operator and representing vectors have the corresponding real structure. Equivalently, use the two separate weights in each Mellin integral, where the two difference masses together are $(\int f)(\int g)$. The Hermitian version follows by sesquilinearity.

The proof of Proposition 7.4 gives, without any symmetry condition,
$$
 \|v_f\|^2=\frac{1}{2\pi}\int_0^1
 \frac{(Nu)^{2\alpha}}{1+(Nu)^{-2\Delta}}\,
 \big|f(u)/2-uf'(u)\big|^2\,du
 \ll \|f\|_{H^1(0,1)}^2. \tag{2}
$$
In the inequality use $(Nu)^{2\alpha}\le e^2$. By density, (1) and (2) extend to zero-extended $H_0^1$ tests on closed interior subintervals: the finite atomic evaluations are continuous in one dimension for fixed $N$. This allows corners; no smoothness of a zero-extended Dirichlet sine at the endpoints is assumed.

Let $I^*=1-I$. The two same-side forms on $I\times I$ and $I^*\times I^*$ vanish identically by (1); the cross form survives. The underlying test vectors on disjoint intervals are also orthogonal by polarization of (2)'s exact integral. Vanishing of a compression **does not** mean that $T_N$ kills the subspace.

## 2. Two-sided lower estimates by min–max

Fix $j\ge1$. In the complex span of the first $j+r_I$ Dirichlet sine modes on $I$, impose $f(a)=0$ at each of the $r_I$ active abscissae. These are at most $r_I$ linear conditions, leaving a space of dimension at least $j$. The basis and the conditions have real forms. Set $f^*(u)=f(1-u)$ and use $v_{f+f^*}$ or $v_{f-f^*}$. All atoms in (1) disappear, including the reflected ones. The two Rayleigh numerators are
$$
 \langle T_N v_{f\pm f^*},v_{f\pm f^*}\rangle
       =\pm 2S\|f\|_{L^2(I)}^2.
$$
This is first checked for real weights; real symmetry and polarization give the Hermitian assertion for complex coefficients. In particular the two maps into the Hilbert space are injective on the chosen subspace (antilinearity of the representing-vector convention is immaterial). The derivative norm of $f$ is at most $\pi(j+r_I)\|f\|_2/|I|$. Applying (2), the denominator is $\ll_I(j+r_I)^2\|f\|_2^2$. The compact self-adjoint min–max principle applied separately to $T_N$ and $-T_N$ gives the asserted eigenvalue estimates. In particular, for fixed $N$ each sign occurs infinitely often. The harmonic-series test on these lower bounds excludes $\mathcal S_{1/2}$.

A stronger **top** lower bound uses unequal probes. Fix a closed interval $I_0$ inside $I$ and take $f$ to be the distance on $I_0$ to its endpoints and its active abscissae, extended by zero. Take $g$ smooth on $I^*$, equal to 1 on $1-I_0$ and compactly supported in $I^*$. Both $H^1$ norms are bounded independently of $N$. If the gaps on $I_0$ have lengths $d_k$, (1) gives
$$
 B_N(f,g)=\frac{S}{4}\sum_k d_k^2
 \ \ge\ \frac{S|I_0|^2}{4(r_I+1)}.
$$
Divide by $\|v_f\|\|v_g\|$ using (2). For a scale comparison, the standard upper-bound sieve gives $O(SN/L^2)$ prime pairs; see [Tao, 254A Notes 4, Exercise 25(i)](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/). At most $O(\sqrt N+N^{1/3}\log N)$ additional points involve a proper prime power. Hence $\|T_N\|\gg_I L^2/N$. This guaranteed floor is **below** $\delta$ by a factor of order $\sqrt{N S/L}$, not a contradiction to R. It does identify a finite-arithmetic way of producing rigorous lower certificates: any pair of tests in (1) with a certified numerator and norm product gives one, without truncating $L$-functions. A small value certifies no upper bound.

## 3. Trace-norm control for the continued beta model

Proposition 6.5 of the source controls the positive finite-character and diagonal terms in trace norm, but estimates the beta term only in Hilbert–Schmidt norm. Here is a trace-class factorization of the latter. Denote the paper's gamma quotient by $X_1(s)=\Gamma((3/2-s)/2)/\Gamma((3/2+s)/2)$, and in the strip Hardy space set
$$
 F_x(s)=x^s X_1(s)/(1+s),\qquad A_x=F_x\otimes F_x\quad (x>0).
$$
Uniform Stirling estimates in $0\le\Re s\le\beta$ give $|X_1(s)|\ll1$. Thus $F_x$ belongs to the strip Hardy space and $\|F_x\|\ll\max(x^\alpha,x^\beta)$. For $n\le x\le n+1$,
$$
 \|F_x-F_n\| \ll n^{\beta-1/2}.
$$
Indeed on either boundary $|(x/n)^s-1|\ll\min(1,(1+|\Im s|)/n)$; the squared integral after division by $|1+s|^2$ is $O(1/n)$. The same estimate on shorter intervals gives norm continuity. The trace norm of $a\otimes a-b\otimes b$ is at most $(\|a\|+\|b\|)\|a-b\|$. Consequently the following operator is defined by absolutely convergent trace-norm integrals and a trace-norm convergent series:
$$
 Z=-\int_0^1 A_x\frac{dx}{x}
 +\sum_{n\ge1}\left(\frac{A_n}{n}
       -\int_n^{n+1} A_x\frac{dx}{x}\right). \tag{3}
$$
The first term costs $O(1/\alpha)$. Each difference costs $O(n^{2\beta-2}+n^{2\beta-3/2})$ by adding and subtracting $A_n/x$ inside the integral. Both series converge for $\beta=1/8$. Thus $\|Z\|_1\ll1+1/\alpha$.

To identify the kernel, take bounded point evaluations at interior $s,z$ and put $w=s+\bar z$. The scalar multiplier in (3) is
$$
 -1/w+\sum_{n\ge1}\left(n^{w-1}-\int_n^{n+1}x^{w-1}dx\right)
 =\zeta(1-w),\qquad 0<\Re w<1.
$$
This follows from Euler summation, or analytic continuation of the normally convergent difference series from $\Re w<0$ (there the integral over $[1,\infty)$ cancels $-1/w$). The remaining kernel factors are $X_1(s)\overline{X_1(z)}/[(1+s)(1+\bar z)]$.

Write the source's density Euler product $P_N(w)$ as $\sum_d b_d d^{-w}$, with $b_d\ge0$, absolutely convergent for $\Re w>0$. Let $M_d$ multiply by $(\pi/(Nd))^s$; its multiplier norm is at most $(\pi/(Nd))^\alpha$. Then the full beta operator is
$$
 \mathcal K_N=S\sum_d b_d M_d ZM_d^*,\qquad
 \|\mathcal K_N\|_1\ll (1+1/\alpha)(\pi/N)^{2\alpha} S P_N(2\alpha)
 \ll \alpha^{-2}. \tag{4}
$$
For the last step use the Euler-product comparison in §6.4.2 of the source, $N^{-\sigma}SP_N(\sigma)\ll1/\sigma$ for $0<\sigma\le2\beta$. Equality of the operators follows from equality of their interior reproducing-kernel matrix elements by (2.12) of the source and density of the span of the point-evaluation vectors. Combining (4) with the two trace estimates of Proposition 6.5 proves $\|T_N\|_1\ll L^2$ under $\mathrm{GRH}(N)$. The beta estimate itself does not use GRH. This gain in the *summability* of the spectrum does not improve the presently available $O(L^2)$ bound for its largest magnitude.

## 4. What this says about S, R, and the spectral function

For a nonzero eigenvalue $\mu$ write $a=|\mu|/\delta$. The associated factor vanishes where $(q-1/2)^2=(1-a^{-2})/4$. If $a<1$ this is the two-sphere of purely imaginary displacements of radius $\sqrt{a^{-2}-1}/2$ from $1/2$; if $a=1$ it is the single real point $1/2$; if $a>1$ it is a pair of distinct real points in $(0,1)$. These alternatives follow directly by squaring a quaternion with real and vector parts; no sign of $\mu$ survives. Thus the two infinite eigenvalue tails imply infinitely many distinct critical-hyperplane zero spheres for every admissible $N$, even if there are also exceptional real zeros.

* R requires $\|T_N\|\le\delta$, **with coefficient 1**. Independently of R, (4) gives
  $$\#\{j:|\mu_j|>\delta\}\ll\sqrt{N\log N/S}.$$
  Count spectral factors with multiplicity, not individual points on quaternionic spheres. This is smaller than the Hilbert–Schmidt-only bound $O(N\log N/S)$, but is not zero.
* For a **prescribed** $h(N)\to\infty$ with $\eta=h^2L^3/(NS)\le1/4$ eventually, S is exactly the bound $\|T_N\|\le S/(2h\sqrt{1-\eta})$ for every sufficiently large admissible even modulus. The number of spectral factors that can violate that threshold is $O(hL^2/S)$. This does not establish the absence of a single violation. The obstruction of Proposition A.4 in the source sends a *different* parameter to zero at fixed modulus and does not settle this large-$N$, fixed-normalization case.
* On a complex slice, $X_N$ has entire-function order between $1/2$ and $1$ for each fixed admissible $N$. For the upper bound, bound each log factor by $\log(1+4|\mu|^2 |q(1-q)|/\delta^2)\le 4|\mu|\sqrt{|q(1-q)|}/\delta$ and sum using trace class. For the lower bound, select the positive eigenvalues from §2. The associated roots have modulus $\delta/(2|\mu|)$ once $|\mu|<\delta$ and hence are $O_N((j+r_I)^2)$. Counting with multiplicity gives zero-count exponent at least $1/2$ and Jensen's formula gives the order bound. This is a statement about the population of small modes, not the position of the largest one.

**Unresolved step.** The trace bound still permits all the admissible bad mass to concentrate in one eigenvalue or in a direction interacting with the arithmetic vector. One needs top-mode cancellation in the signed operator, or a separate bound on the arithmetic vector's overlap with the bad subspace for a weaker Goldbach-only result. Controlling a projection of the operator, finding infinitely many critical-line modes, or observing that the total number of possible exceptions is finite for each $N$ does not supply that cancellation.
