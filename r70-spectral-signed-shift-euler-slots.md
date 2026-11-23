# Signed cutoff shifts enlarge the actual small-prime slot ranges

**Scope.** This controls the genuine above-BV mixed coefficient on many more small-prime slots than the [direct multiple-shift estimate](r69-spectral-bounded-density-small-prime-slots.md), with no least-prime restriction. Retain the true largest-prime gate $P^+(m)>N^{1/2-\delta}$, for fixed $0<\delta<1/4$, and put

$$
 L=\log N,\quad L_2=1+\log L,\quad U=\sqrt L,\quad G=\exp U.
 \tag{1}
$$

For odd total parity $\mu(m)=-1$ allow up to $r_o=\lfloor\log U\rfloor$ distinct prime factors of $m$ at most $G$. For even total parity $\mu(m)=+1$ allow up to $r_e=\lfloor(2/5)\log U\rfloor$. In particular both parities are controlled up to $r_e$. These are conditions on the actual small-prime count, not exclusions of fixed tiny primes. We do not estimate either complementary count, smaller-largest-prime partners, or weak S.

Keep $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ with fixed $B>B_0>0$, $V=[N/3,2N]$, the hard central $I$, bounded-variation $\omega$, prime polynomial $P_{I,\omega}$, and major arcs with $Q=N^{1/1000}$ from the [polynomial largest-prime argument](r68-spectral-polynomial-largest-rough-mixed-minor.md). Let $A(m)$ be the actual squarefree mixed $M_>(m)$ restricted to $V$ and one of the two stated parity-and-count selectors, or to their union. With $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$ and $c_\delta=\min(10^{-4},(1/4-\delta)/4)$, we prove

$$
\begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
       &\ll \Sigma(N)|I|\mathcal B/L+N^{1-c_\delta},\\
 \left|\int_{\mathfrak m} P_{I,\omega}(\theta)\widehat A(\theta)
                          e(-N\theta)\,d\theta\right|
       &\ll \Sigma(N)|I|\mathcal B/L+N^{1-c_\delta}.
\end{split}
\qquad
 \mathcal B_o=L^{-1/20},\quad \mathcal B_e=L^{-1/100}.
 \tag{2}
$$

Use $\mathcal B_o$ for odd only and $\mathcal B_e$ otherwise. The full absolute bound is unconditional; the actual minor estimate uses only the same historical prime-progression Dirichlet GRH input for the two primes at $q\le Q$. The desired scale follows after the original $L/N$ normalization.

## 1. Fourier weight of the rough reciprocal primitive

Write $R(u)=\sum_{n\le\exp u}\mu(n)/n$, zero for $u<0$. The [ordinary reciprocal Mertens bound](r68-spectral-least-prime-conditioned-mixed-minor.md) gives $|R(u)|\ll e^{-c\sqrt u}$ for $u\ge0$. With Fourier convention $\widehat f(\xi)=\int f(u)e^{-i\xi u}\,du$, one has

$$
 |\widehat R(\xi)|\ll 1,\qquad
 |\widehat R(\xi)|\ll
       \frac{(1+\log(3+|\xi|))^2}{|\xi|}\quad(|\xi|\ge1).
 \tag{3}
$$

For the second, truncate at $u=C(1+\log(3+|\xi|))^2$, taking $C$ sufficiently large. The decaying tail has $L^1$ cost $O(|\xi|^{-2})$. The bounded part has variation $O(1+u)$ because its absolute jumps sum to at most $\sum_{n\le\exp u}1/n$, with the unit and truncation endpoints included. Integration by parts proves (3).

Let $R_G$ be the primitive restricted to $G$-rough integers, and $R_{G,e}$ additionally exclude prime factors of a rough $e$. All the convolutions from the [common-kernel proof](r69-spectral-rough-reciprocal-kernel-sampling.md) converge in $L^1$, as the positive mask Euler measures have finite total mass. In particular

$$
 \widehat R_G(\xi)=\widehat R(\xi)
            \prod_{p\le G}(1-p^{-1-i\xi})^{-1}.
 \tag{4}
$$

The extra factors for $R_{G,e}$ multiply this by $\prod_{p\mid e}(1-p^{-1-i\xi})^{-1}$. Uniformly for rough $e\le Z=10N^\delta L^B$ their modulus is $O(1)$, since $\sum_{p\mid e}1/p\ll (L/U)e^{-U}$.

Define

$$
 M(\xi)=\sum_{p\le G}\frac{|1-e^{-i\xi\log p}|^2}{p},
 \qquad y=U|\xi|.
$$

The ordinary quantitative prime number theorem (e.g. [Montgomery–Vaughan, Chapter 6, Theorem 6.9](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287)), by partial summation, gives the following bounds, with fixed absolute constants:

$$
\begin{array}{lll}
 |\xi|\le1: &|\widehat R_G(\xi)|\ll U/(1+y),&
          M(\xi)\le 2\log(1+y)+O(1);\\
 y\le1: && M(\xi)\ll y^2;\\
 |\xi|\ge1: &|\widehat R_G(\xi)|\ll
                  (1+\log(3+|\xi|))^4/|\xi|,&
          M(\xi)\le 2\log U+O(1+\log\log(3+|\xi|)).
\end{array} \tag{5}
$$

Here are explicit details for the logarithmic coefficients. Partial summation with $\pi(x)-\operatorname{Li}(x)\ll x e^{-c\sqrt{\log x}}$ compares the prime exponential reciprocal sum on $e^a<p\le e^b$ with $\int_a^b e^{i\xi u}\,du/u$, with error $O((1+|\xi|)(1+a)e^{-c'\sqrt a})$ for $b\ge a\ge\log2$. For $|\xi|\le1$ start at $\log 2$ and absorb a possible endpoint. The real integral is $\log(\min(U,1/|\xi|))+O(1)$ by splitting at $1/|\xi|$ and integrating the tail by parts, with the limiting interpretation at zero. This bounds the log modulus of the Euler factor in (4), and subtraction from $\sum_{p\le G}1/p=\log U+O(1)$ proves the first $M$ bound, including the coefficient 2. For $y\le1$ use $|1-e^{-it}|\le |t|$ and $\sum_{p\le G}(\log p)^2/p\ll U^2$ by partial summation. For $|\xi|\ge1$, let $a=C(1+\log(3+|\xi|))^2$. If $a<U$, the same error and integral on $[a,U]$ are $O(1)$; before $a$, Mertens bounds the absolute cosine sum by $\log a+O(1)$. If $a\ge U$ this last bound alone suffices. Expanding the Euler log, all powers above the first contribute $O(1)$, so the Euler modulus is $O(a)$ and the stated high-frequency $M$ estimate follows from the lower cosine bound as well. Combine with (3).

## 2. Signed small-factor Euler products in cutoff space

Use the exact factorization $m=pk$, $p>\max(P^+(k),N^{1/2-\delta})$, $k=bv$ from the previous slot proof. Thus $b$ is the squarefree product of all the actual primes $\le G$ in $k$, $v$ is strictly $G$-rough, and $t=\omega(b)$ is the retained count. Since $p>G$ eventually, this is also the small-prime count of $m$. In particular $b\le G^{\log U}=N^{o(1)}$. For each such $b$, the signed divisor shift operator on a log-coordinate function is

$$
 (\mathcal D_b f)(u)=\sum_{d\mid b}\mu(d) f(u-\log d),\qquad
 q_b(\xi)=\prod_{p\mid b}(1-e^{-i\xi\log p}).
 \tag{6}
$$

The exact cut identities $S_k(T)=\sum_{d\mid b}\mu(d)S_v(T/d)$ and their integrated analogues give this signed operator after the LCM expansion, not its unsigned norm. Its squared multiplier has a useful positive generating bound at each $\xi$:

$$
 \sum_{\substack{b\ {\rm sf}\\P^+(b)\le G}}
             \frac{z^{\omega(b)}}{b}|q_b(\xi)|^2
       =\prod_{p\le G}\left(1+\frac{z|1-e^{-i\xi\log p}|^2}{p}\right)
       \le \exp(zM(\xi))\qquad(z>0).
 \tag{7}
$$

Thus a fixed count $t$ costs a multiplier $z^{-t}e^{zM(\xi)}$ under summation with $1/b$; if $t\ge1$, one can instead use $z^{-t}(e^{zM(\xi)}-1)$. The count range $0\le t\le r$ at $0<z<1$ costs $z^{-r}e^{zM(\xi)}$.

Let $W=C_B L_2$ bound the log distance between $T_1=k/D$ and $T_2=Dk/x$, $x=pk\in V$, together with the later cell uncertainties. The following global Plancherel bounds are uniform in a fixed distance $0\le h\le W$ and also for $R_{G,e}$ with $e$ as in Section 1. Norms integrate over the whole real cutoff coordinate $u$.

- The primitive $\mathcal D_b R_{G,e}$, squared and summed over $0\le t\le r$ with $1/b$, has bound $O(U z^{-r})$ for any fixed $0<z<1/2$. The same bound holds for a sum of two such primitives at distance $h$, up to the factor 4.
- Its two-endpoint signed difference at distance $h$, squared and summed over a fixed count $t$, has bound $O(W U^{1/2}4^t)$.
- For $t\ge1$, its full signed integrated primitive, squared and summed over a fixed count $t$, has bound $O(U^3(20/29)^t)$.

For the first use (5) and (7), integrating on $|\xi|\le1$ with $y=U|\xi|$. The integral is $O(U\int_0^U(1+y)^{-2+2z}dy)=O(U)$; the high-frequency part is $O(U^{2z})$ from (5), since the log powers are integrable against $\xi^{-2}$. The signed difference in the second case adds $O(\min((W|\xi|)^2,1))$ to the squared multiplier. At $z=1/4$, split $y$ at $U/W$ (eventually $W<U$); integrating the smaller factor and the tail gives $O(W(U/W)^{1/2})$, with the high part $O(U^{1/2})$. This proves the stated slightly coarser bound. For the last use the squared multiplier $|q_b(\xi)|^2/\xi^2$. It is valid since $b>1$: extract any one prime of $b$, write the resulting integrated difference as a convolution with an interval in the log coordinate, and apply the other signed translates. At $z=29/20$, use $e^{zM}-1=O(y^2)$ for $y\le1$ and $O((1+y)^{2z})$ beyond. The low-frequency integral after scaling is $O(U^3)$ since $2z<3$, and the high part is $O(U^{2z})$. All three estimates use the exact signs in (6). An integral of the ordinary primitive between two cutoffs at distance $h$ instead has multiplier bounded by $h$ times the ordinary signed shift multiplier, so its squared bound in the first case is at most $O(W^2 U z^{-r})$.

## 3. Pass from the signed cutoff energies to the true hard cells

The exact support has $D<k\le2N^{1/2+\delta}$, and $M_>=-\Xi_D-M_\le$. Prime $k$ forces $D<k<\sqrt x$ and its reciprocal mass is $O(L_2/L)$, as before. For composite squarefree $k$, the sharp product for $-\Xi_D$ has the exact factors

$$
 F_0=-\mu(k)S_k(T_1^-)-S_k(T_2),\qquad
 F_1=a(x) F_0+\frac2{\log x}\{\mu(k)J_k(T_1)-J_k(T_2)\},
 \quad a(x)=O(W/L).
 \tag{8}
$$

The arithmetic border $k\le10DL^{2B}$ stays harmless: both cutoffs are fixed powers of $L$ at most, so only divisors of $b$ can enter because $v$ is $G$-rough. The reciprocal product over that log interval is $O(4^r W^2/L)$ on either chosen cap $r\le\log U$, using the pointwise product bound and the interval's log width $O(W)$. We henceforth stay above this border.

Choose hard geometric physical and arithmetic cells of log width at most $\eta=L^{-10}$; the number of cells in each variable is polylogarithmic. For each physical cell choose a fixed $x_0$ in it and moreover fix the distance $h=\log(x_0/D^2)\in(0,W]$. On an arithmetic cell $K<k\le K'$ of log width $w$ let $\mathcal U$ be the interval of log cutoffs $u=\log(k/D)$ for that cell. Each $u\in\mathcal U$ gives comparison cutoffs $\exp u,\exp(u-h)$, within $O(\eta)$ in log of the actual cutoffs for every admissible $k,x$ in the cell pair.

For fixed $b$ the rough arithmetic variable is $K/b<v\le K'/b$. Denote by $C_0(v)$ a majorant of the absolute sharp factor $F_0$ uniform in $x$ on the physical cell, and by $C_1(v)$ one for the absolute **unscaled** integrated combination in braces in (8). Construct each as the square root of the mean of the corresponding model square over $u\in\mathcal U$, plus an endpoint error envelope. This follows from Minkowski in $u$, since at every comparison $u$ the difference from the actual factor is bounded by the same envelope. For $F_0$ the envelope is a sum over $d\mid b$ of unsigned short shell counts for the two endpoint brackets, of log width $O(\eta)$ after translation by $\log d$. These cover strict/weak discrepancies at integers. For the integrated term, the envelope is a sum of endpoint integrals of $|S_v|$ on such brackets, after all translates; equality in integrated cutoffs has no jump.

We give error bounds before using the Plancherel integrals because endpoint rounding used no cancellation of the moving terms. Rough-cell reciprocal counts refine the old unsigned boundary-shell energy to $O(\eta/U)$ if the interval excludes 1, or $O(1)$ otherwise. Indeed the diagonal has these bounds by the rough harmonic sieve (its floor $e^{-3U/4}\ll\eta/U$). For two nonunit co-prime parts after gcd decomposition the bound $O((\eta/U)^2(1+L/U))$ is $O(\eta/U)$ here; exactly one unit is impossible by $U\gg\eta$. An arithmetic cell's bracket can contain 1 for a given $d$ only within $O(\eta)$ of $\log d$ or $\log d+h$ in the $u$ coordinate. Thus for fixed $b$ the total log width of marked boundary cells is $O(2^t\eta)$. The trace factor $w/U$ and a triangle at most $2^t$ in norm now bound the squared $F_0$ envelope, summed over the arithmetic cells for that $b$, by

$$
 O\!\left(4^t L\eta/U^2+8^t\eta/U\right)
 \tag{9}
$$

apart from the reciprocal floors. The squared integrated envelope per cell is $O(4^t\eta^2 w/U)$ by Cauchy on each fixed bracket and the signed primitive energy $O(1)$ of the common-kernel proof. Its sum is $O(4^t\eta^2 L/U)$. After summing $b$ with $1/b$, both squared envelope totals are $O(L^{-5})$, since $t\le\log U$ and $\sum_{b\ {\rm sf},P^+(b)\le G}1/b\ll U$. The estimates also hold when restricted to one exact count.

For the model squares, the exact reciprocal trace on rough $v$ has main term $w \prod_{p\le G}(1-1/p)$ times its signed LCM energy, and error $O_A(wL^{-A}+N^{-1/2+2\delta+o(1)})$. This is the Bonferroni argument in the common-kernel and previous slot proofs: $K/b\ge N^{1/2-o(1)}$, all divisor labels in the relevant cutoff cells are at most $Z$, and the coefficients are at most $2^t O(L)=L^{O(1)}$; take a larger fixed log saving for the individual counts before summing label pairs. It applies pointwise in the comparison parameter $u$ and also to the boundary envelopes. The factor $1/w$ from taking the mean cancels the $w$ in the main term, and leaves the uniform floor unchanged. After all arithmetic cells and $b$ with $1/b$, the power floor stays $N^{-1/2+2\delta+o(1)}$ before final Cauchy, since every number of cells is only polylogarithmic. The $wL^{-A}$ errors can be made smaller than $L^{-5}$ here. The parity and squarefree masks can be dropped only on these nonnegative squares, after evaluating the signed energy. The rough $v$ mask remains exact throughout.

Expanding the gcd, the inner contribution to the LCM energy at a rough $e\le Z$ is the corresponding squared cutoff function of Section 2, translated by $\log e$, times $\varphi(e)\mu(e)^2/e^2$. In this expansion the strict and weak endpoint versions agree almost everywhere in $u$. For the integrated factors this is just integration of the same reciprocal primitive. After summing $\int_{\mathcal U}$ over the disjoint arithmetic cells, increase the integral of each nonnegative square to the whole real line, keeping $e\le Z$. Its harmonic sum costs $O(L/U)$ by the rough sieve. Together with the trace density $O(1/U)$ the final multiplier of each Plancherel bound is $O(L/U^2)=O(1)$. Only the arithmetic cutoff integral was enlarged, not the actual partner or Fourier support.

## 4. The two parity rates and the low mixed term

With $C_0,C_1$ as above, the product reciprocal estimate uses
$|F_0F_1|\ll (W C_0^2+C_0C_1)/L$. Sum over $b$ with $1/b$ and $v$ with $1/v$, applying Cauchy to the second term jointly over the arithmetic cells and $b$. All estimates are for a fixed physical cell and its original coefficient.

For odd total parity $\mu(k)=+1$, the $F_0$ model is a sum of two primitives at distance $h$ and the $C_1$ model is their intervening signed integral. The summed squared bounds on the cap $r_o$ are $O(U(20/9)^{r_o})$ and $O(W^2 U(20/9)^{r_o})$, respectively, by the first Plancherel estimates with $z=9/20$. The envelopes just estimated are absorbed. The reciprocal product is $O(W U^{-1}(20/9)^{r_o})$, saving the power $1-\log(20/9)>0.20$ in $U$, up to the factor $W$. For even total parity $\mu(k)=-1$, the $F_0$ model is an open shell and the braces in (8) are, up to sign, the sum of two integrated cutoffs. The $t=0$ contribution is covered by the common-kernel proof with $U_0=U$. At each count $1\le t\le r_e$ the summed squared bounds for $C_0,C_1$ are $O(W U^{1/2}4^t)$ and $O(U^3(20/29)^t)$. Thus the reciprocal product is bounded by

$$
 O\left(W^2 U^{-3/2}4^t+
       \sqrt W\,U^{-1/4}(80/29)^{t/2}\right).
 \tag{10}
$$

Since $t\le(2/5)\log U$, the exponent on the second term is at most $-1/4+(1/5)\log(80/29)<-0.046$. The borderline product, prime $k$, and power floors are smaller. Summing at most $1+r_e$ counts only adds a log factor. Endpoints were never averaged in the actual polynomial: the cutoff integral furnished a majorant and preserved the true hard positions.

It remains to transfer the actual low mixed subtraction $M_\le$. Its signed labels are below $Y_0=H_0/D=L^{B-B_0}$, so only the small primes of $b$ at most $Y_0$ have three assignments to those labels, while the allocation of $b$ between the two complementary factors has two choices per prime. With $t_0=\#\{p\mid b:p\le Y_0\}$ the same true $h\mid k$ or $h=pr$ split as in the previous slot proof therefore gives harmonic weight at most

$$
 \frac{2^t3^{t_0}}b
       \cdot O\!\left(\frac WL\frac WU(1+L/U)\right).
 \tag{11}
$$

One rough factor is in a log interval of width $O(W)$, away from the unit because $b=N^{o(1)}$, and the other is at most $Z$. The two signed labels are coprime since the actual partner is squarefree. Bound the sum of $2^t3^{t_0}/b$ over $t\le\log U$ by weighting each count with $z^t$ at $z=1/2$, then multiplying by $2^{\lfloor\log U\rfloor}$. The resulting Euler product is at most

$$
 \exp\left(\sum_{p\le G}\frac1p+
                         2\sum_{p\le Y_0}\frac1p\right)
       \ll U\,L_2^{O(1)} .
 \tag{12}
$$

Thus (11) totals at most $U^{-1+\log2}L_2^{O(1)}$, since $U=\sqrt L$. The more costly factor 3 was not charged to primes too large to occur in the true signed labels. This error is harmless for both claimed rates.

Finally multiply by $k/\varphi(k)\ll L_2$ as required for the genuine two-prime sieve and completed major density. The odd exponent and (10), including this factor and all powers of $L_2$, imply $O(L^{-1/20})$ and $O(L^{-1/100})$, respectively, for the corresponding reciprocal majorant sums. The true two-prime count at fixed $k$ and physical cell still sieves $p,N-kp$ on its exact hard interval, with length at most $|I_{\rm cell}|/k$; the sum of the physical lengths is $|I|$. The coefficient majorants are $N^{o(1)}$ by the divisor bound, so the two-prime floor $N^{3/4+\delta+o(1)}$ fits the same power error as before. For the conditional major calculation the small-prime count and parity selectors are constant at fixed $k$, and do not change the exact weight of variation $O(\tau_4(k))$. The same prime AP approximation, actual local factor and reciprocal prime denominator, with the unchanged Fourier and Ramanujan completion tails, bound the actual major integral by the right side of (2). The integrated reciprocal floors from Section 3, after Cauchy, also fit $N^{1-c_\delta}$. This proves (2) by subtracting the actual major integral from the true full coefficient. No statement about partners outside the stated parity and count cuts follows.
