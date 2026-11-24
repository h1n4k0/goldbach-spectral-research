# The genuine full mixed strip on almost all even targets

**Scope.** This unconditionally evaluates the actual above-BV mixed strip's full signed prime correlation separately on its two true squarefree Möbius parities, on a density-one family of even targets. The original moving polynomial-major integral has the same asymptotic there. No conclusion is made for prescribed targets, any prescribed sparse radical family (such as powers of two), prime representations, the exterior, or weak S.

Keep the notation of the [pointwise parity major calculation](r67-spectral-high-mixed-parity-major.md): fixed $B>B_0>0$, even $N$, $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, $V=[N/3,2N]$, and the exact mixed coefficient $M_>$ before its subtraction in the central decomposition. Put $M_\pm=(1\pm\mu(m))M_>/2$ on squarefree $m\in V$, zero elsewhere, plus meaning even total parity. Use any actual hard half-open $I\subset(N/2,9N/16]$, a uniformly bounded BV left weight $\omega$, and $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$. Write $S_\pm=\sum_{n\in I}\lambda(n)\omega(n)M_\pm(N-n)$.

There is a fixed $c>0$ depending on $B,B_0$ such that for each fixed $A>0$, outside $O_A(Y\exp(-c\sqrt{\log\log Y}))$ even $N\in[Y,2Y]$, simultaneously for all these $I,\omega$,

$$
\begin{split}
 S_+&=\Sigma(N)\int_I\frac{\omega(u)}{\log(N-u)}du
     +O_A\!\left(\frac{\Sigma(N)|I|}{L}e^{-c\sqrt{L_2}}+Y L^{-A}\right),\\
 S_-&=O_A\!\left(\frac{\Sigma(N)|I|}{L}e^{-c\sqrt{L_2}}+Y L^{-A}\right).
\end{split}\tag{1}
$$

The same holds for the **actual** moving major-arc integrals with denominators $q\le N^{1/1000}$ and radius $2N^{1/1000}/N$. The error $e^{-c\sqrt{L_2}}$ is not a fixed reciprocal log power of $N$. The even leading term is a signed composite cutoff contribution, not a prime representation count.

## 1. Unconditional parity calculation on common polylogarithmic arcs

Put $\ell=\log Y$ and take common arcs $\mathfrak M_0$ of reduced denominator $q\le Q_0=\ell^K$ and radius $2Q_0/Y$, with fixed $K$ chosen large. The actual $D,H_0,V$ stay in the major arithmetic. The [global marginal identity](r66-spectral-above-bv-strip-deletions.md) is $M_>+M_\le=-\Xi_D$. In $\Xi_D$ the mutually coprime squarefree factors $m=abcd$ obey $ab,ac<\sqrt m$ and $\max(ab,ac)>D$. In $M_\le$ the actual inequalities are $D<\min(ab,ac)<\sqrt m$ and $abc\le H_0$. The original sign is $\mu(b)\mu(c)$; multiplying by $\mu(m)$ makes it $\mu(a)\mu(d)$ with exactly the same gates.

Here are the unconditional inputs replacing the polynomial-modulus ones in §1 of the parity calculation.

* The untwisted strip uses §1 of the [squarefree CRT calculation](r63-spectral-full-squarefree-crt-strip.md), already at polylogarithmic moduli. Its arithmetic progression estimates and real caps are uniform in the indicated genuine hard cutoffs; freezing was needed for its later mean square, not here.
* On the twisted strip, in the two disjoint signed sectors $a>N^{.1}$ and $d>N^{.1}$ with $a\le N^{.1}$, fix the other three factors of product $h$. The signed factor is at polynomial scale $N/h$, on hard intervals with the same coprimality mask of size at most $2N$. The masked unconditional Möbius Siegel--Walfisz estimate for every residue in §1 of the squarefree CRT calculation gives arbitrary inverse-log errors times $N/h$. These survive the triple reciprocal sums, the polylogarithmic number of residue classes and the slow phase variation $O(1+Q_0)$, by choosing a stronger input log power. Similarly the twisted $M_\le$ has signed $d=m/(abc)\ge N/(3H_0)$ and is negligible, using that same estimate in the true $d$ interval.
* In the twisted strip with $a,d\le N^{.1}$ both positive $b,c$ exceed $N^{.39}$ by the exact midpoint inequalities. The ordinary squarefree CRT progression count with error $O(\tau(w)\sqrt x)$ at scale $x$ and coprimality mask $w$ is unconditional. Follow the same two-positive-variable harmonic computation as the parity proof: its Euler convolution moment at exponent $3/4$ is $O_\epsilon(q^3(ad)^\epsilon)$ with prefactor $O(q^2)$, more than sufficient at $q\le Q_0$. The untwisted $M_\le$ similarly uses the actual [below-level mixed density](r65-spectral-bv-visible-strip-minor.md), with $b,c<H_0/D$ and both positive variables $a,d$ at polynomial scale; only its unconditional CRT arithmetic is used, not its pointwise result on the original minor.
* Prime Siegel--Walfisz gives the left factor $\mu(q)V_I(\beta)/\varphi(q)$ with $V_I(\beta)=\int_I\omega(u)e(\beta u)du$. Prime powers, BV partial summation and the total arc measure $O(Q_0^3/Y)$ preserve integrated error $O_A(Y\ell^{-A})$ after choosing the input log accuracy for the fixed $K$.

For these right main terms the squarefree-$q$ sup plus variation in $x$ is $O(\ell^C C_1^{\omega(q)}/q)$ with fixed constants. This is the same occupancy proof as in the squarefree CRT and parity calculations: at a prime of $q$ either a signed variable is occupied with a reciprocal gain $1/p$, or the two-positive-variable local factor gives $O(1/p)$; the actual caps and unforced harmonic sums cost fixed log powers. The occupation bound holds even for each formal coefficient beyond $Q_0$, because it uses the local factor expressions, not progression estimates at larger $q$. The left factor removes nonsquarefree $q$. Extending the slow Fourier parameter to the line costs at most

$$
 YQ_0^{-1}\ell^C\sum_{q\le Q_0,\ q\ {\rm sf}}C_1^{\omega(q)}/q
       \ll YQ_0^{-1}\ell^C(1+\log Q_0)^{O(1)},
$$

by BV on both transforms and $|c_q(N)|/\varphi(q)\le1$.

To complete the rational series at this small cutoff, use the mean

$$
 Y^{-1}\sum_{Y\le N\le2Y}|c_q(N)|
 \le Y^{-1}\sum_{d\mid q}\varphi(d)\#\{N\le2Y:d\mid N\}
 \le2\tau(q).
$$

Thus the mean absolute tail, normalized by $Y$, is

$$
 O\!\left(\ell^C\sum_{q>Q_0,\ q\ {\rm sf}}
       \frac{\tau(q)C_1^{\omega(q)}}{q\varphi(q)}\right)
        =O(\ell^C Q_0^{-1/2}),
$$

by inserting $q^{1/2}$ and summing the convergent Euler factors. Markov gives $O_A(Y\ell^{-A})$ integrated error off $O_A(Y\ell^{-A})$ targets after increasing $K$, uniformly in the left hard and BV inputs. Hence the exact same real cap and completed local calculation as §§1--2 of the parity proof gives

$$
 \frac{\Sigma(N)P_N}{2}\int_I\frac{\omega(u)}{\log x}
 \left\{T(x)(Q_N-Q_{N,U})+J_{N,U}
      \ \pm\left(\int_{-T(x)}^{T(x)} C_N(t)dt-T(x)C_N(T(x))\right)\right\}du,
 \quad x=N-u. \tag{2}
$$

Here the local quantities $P_N,Q_N,Q_{N,U},J_{N,U},C_N$ are those of that proof ($Q_N$ in (2) is its quadratic coefficient, not the arc cutoff), with $U=(B-B_0)\log L$, $T(x)=\log(x/D^2)$. All operations after progression replacement and rational tail completion are the identical unconditional real-factor integration and large-log reciprocal Mertens truncations of that proof. Thus (2), with the stated error and exceptional count, is now an unconditional small-major evaluation on the genuine coefficients.

## 2. The moving radical tails

For odd primes set $\alpha_p^\circ=(p-1)/(p^2-2)$, and put $\alpha_2^\circ=0$. The parity formula uses $\alpha_p=\alpha_p^\circ$ when $p\nmid N$ and zero otherwise. Write $R(u)$ for the ordinary reciprocal Möbius primitive, zero below zero, with unconditional decay $O(e^{-c_0\sqrt u})$ and integral $1$. The primitive $R_{N,j}$ is its convolution with a positive kernel: first replace $1-p^{-1}e^{-z\log p}$ by $1-\alpha_p^\circ e^{-z\log p}$, whose ratio has nonnegative coefficients, then delete primes dividing $Nj$. At a fixed positive exponential moment $\delta=1/4$ the base kernel has bounded mass (odd prime factors $1+O(p^{-2+\delta})$ and one finite factor at 2). Set

$$
 {\mathcal A}(v)=\prod_{p\mid v,\ p>2}(1-\alpha_p^\circ p^\delta)^{-1}.
$$

The full kernel moment is therefore $O({\mathcal A}(N){\mathcal A}(j))$. This also bounds the full $L^1,L^2$ norms by Minkowski. For $V_0\ge1$, split shifts at $V_0/2$, using the ordinary Mertens tail below that point, and exponential Markov on the positive kernel above it. This yields

$$
 \|R_{N,j}\mathbf1_{[V_0,\infty)}\|_\nu
   \ll {\mathcal A}(N){\mathcal A}(j)e^{-c_1\sqrt{V_0}},
           \qquad \nu=1,2.
 \tag{3}
$$

Since $\alpha(j)\le1/j$, the sums of $\alpha(j)^2{\mathcal A}(j)^2$ also with an extra factor $j^{1/2}$ are uniformly bounded by Euler products.

Let $J_{N,\infty}=\sum_{j\ {\rm sf}}\mu(j)\alpha(j)^2(\int R_{N,j})^2$. Split the two truncations at $j=e^{U/2}$: at small $j$ their upper log limits $U-\log j$ are at least $U/2$, so use (3), and use the Euler half moment for the rest. Taking the difference of squares in the $J$ case gives

$$
 |Q_N-Q_{N,U}|+|J_{N,U}-J_{N,\infty}|
                       \ll {\mathcal A}(N)^2 e^{-c_2\sqrt U}.
$$

For the autocorrelation, each pointwise $C_N(T)$ is bounded termwise by the $L^2$ norm times its tail at $T$, since the primitives vanish below zero. The absolute tail integral over $|t|>T$ is bounded by twice the $L^1$ norm times its tail at $T$ in each term. The full integral is $J_{N,\infty}$ by Fubini. Therefore

$$
 |C_N(T)|+\left|\int_{-T}^T C_N(t)dt-J_{N,\infty}\right|
                     \ll {\mathcal A}(N)^2 e^{-c_2\sqrt T}.
$$

For every even $N$ the exact identity $P_NJ_{N,\infty}=1$ follows from the local factor $(1-2\alpha_p)/(1-1/p)^2$ of the integrated $j$ sum and $(1-1/p)^2(1+2r_p/p)$ of $P_N$, since $\alpha_p=r_p/(p+2r_p)$, including inactive primes. The factor for the integrated sum uses $\int R=1$ and deletion multiplying the positive kernel mass by $(1-\alpha_p)^{-1}$. These products are absolutely convergent for each $N$ as in the parity proof. With $P_N\ll1$, $T(x)=2B\log L+O(1)$ uniformly, and $U=(B-B_0)\log L$, the bracket of (2) multiplied by $P_N$ is

$$
 (1\pm1)+O\!\left({\mathcal A}(N)^2e^{-c_3\sqrt{L_2}}\right).
 \tag{4}
$$

Decrease $c_3>0$ to absorb the extra factor $T(x)$.

The positive factor $\mathcal A(N)^2$ has bounded mean over $N$. Expand over squarefree divisors with coefficient $g(d)=\prod_{p\mid d}({\mathcal A}(p)^2-1)$ (zero for even $d$). Then $\sum_{N\le2Y}{\mathcal A}(N)^2\le2Y\sum_d g(d)/d\ll Y$, since the increments in the Euler product are $O(p^{-2+\delta})$. Markov at $\exp((c_3/2)\sqrt{\log\log Y})$ loses at most $O(Y e^{-c_4\sqrt{\log\log Y}})$ targets; on the remainder (4) gives the stated two densities. This controls the actual radicals on a dense family, not any prescribed modulus.

## 3. Genuine full and original polynomial major

To estimate the complement of the common arcs, use §1 of the [divisor-threshold proof](r79-spectral-original-minor-power-exception.md) to freeze only $D,H_0$ on $O(\ell^{C_m})$ target blocks of relative width $\ell^{-C_m}$. Its true divisor-strip argument gives squared error $O(Y\ell^{-C_m+30}+Y^{1-c_5})$ for a fixed $c_5>0$; the two parity masks contract this error. The actual right physical interval $V_N$ stays exact. By the left squared norm $O(Y\ell)$, large fixed $C_m$ makes the deterministic integral error $O(Y\ell^{-A})$. The frozen right square norm is $O(Y\ell^{15})$.

On the complement of $\mathfrak M_0$, use the Dirichlet approximant of denominator at most $\lceil Y/Q_0\rceil$. Its denominator must exceed $Q_0$, so the genuine hard-interval prime sums have Vaughan bound $O(Y Q_0^{-1/2}\ell^4)$, as in the original-minor proof. The prime-power error is negligible. At a fixed dyadic left level, the pointwise sum of squares across its disjoint cells is at most $O(Y)$ times that supremum, by Chebyshev plus the triangle inequality. On a fixed right physical level, torus squared energies of the disjoint cells sum to the squared norm of the frozen coefficient. The two-physical-axis maximal Bessel of the original-minor proof therefore gives squared sum over integer targets $O(Y^3 Q_0^{-1/2}\ell^{O(1)})$ per frozen block. Here the arc set is fixed, so rational and slow axes are unnecessary. Sum the log number of blocks, choose $K$ large after $C_m,A$, and use Markov at $Y\ell^{-A}$ to lose only $O_A(Y\ell^{-A})$ targets. BV left weights are handled by the same integer prefix partial summation uniformly on all hard intervals.

The full coefficient equals the actual common small-major integral plus this common-complement integral by Fourier inversion. Combining §§1--2 proves (1). Finally, the original moving polynomial-minor theorem applies unconditionally to the two fixed common parity masks and gives power saving for that true minor off a power-small exceptional set. Subtract that actual minor from the full correlation. This produces (1) for the genuine original polynomial major, without any polynomial-modulus GRH input, on the union of the stated exceptions. It says nothing about the original full or minor on all powers of two or any specified exceptional modulus.
