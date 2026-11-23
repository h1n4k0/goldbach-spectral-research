# A fixed-sign masked obstruction at typical true middle counts

Take the original true marked central sum (1) and strict integer $D_N=\lfloor\sqrt N\exp(-20T_N)\rfloor$, $Q_N=\lfloor N\exp(-20T_N)\rfloor$ of the [joint actual-count bound](r72-source-joint-middle-count-entropy.md), with $L_N=\log N$, $\ell_N=\log L_N$, $T_N=L_N/\ell_N$. Fix $0<\rho<1/2$ and take $I=I_0=[\rho N,(1-\rho)N]$. Use the same parameters on the two legs:
$a_i=0$, $c_i=1$, $d_i=2$, $C=3$, $E_i=1$, $\theta_i=\theta=1/20$.
In particular the old lower primes lie in $[\exp(T_N),\exp(2T_N)]$, old rough primes are at least $\exp(3T_N)$, and the actual exceptional interval is $(V_N,Y_{*,N})$, where

$$
 V_N=\exp(T_N\ell_N^\theta),\qquad
 Y_{*,N}=\exp\!\left(\frac{L_N}{64(J_N+1)}\right),\qquad
 J_N=\left\lfloor\frac{\log\ell_N}{\log\log\ell_N}\right\rfloor.
$$

All operand selections below refer to genuine integers, not to interior divisor labels. The original squarefree and $N$-unit conditions are imposed.

**Theorem (unconditional).** There are arbitrarily large even $N$ and masks on the actual operands, with every selected operand having exceptional count $(1-\theta+o(1))\log\ell_N$ and total old rough arity $O(\log\ell_N)$, for which the genuine signed sum satisfies

$$
                  R_N(I_0)\le-c_\rho\mathfrak S(N)N
 \tag{1}
$$

for a fixed $c_\rho>0$. In fact for every sufficiently large real scale $X$ one can choose one fixed integer mask $\mathcal A_X$ for **both** legs, before summing over $N$ in $[X,(1+\Delta)X]$ with fixed small $\Delta>0$; at least one even $N$ there satisfies (1) for this mask. The two shrinking proper-divisor gap orientations are not imposed. The statement rules out a uniform $o(\mathfrak S(N)N)$ estimate over all arbitrary outer masks in this genuine typical-count block. It does **not** bound the corresponding unmasked sum from below, disprove Hypothesis S, or exclude cancellation with other operands or other arithmetic blocks.

## 1. A reciprocal mass of true typical products

Choose fixed $\Delta>0$ so $1/(2(1+\Delta))>\rho$ and $\Delta<1/10$. Write $L=\log X$, $\ell=\log L$, $T=L/\ell$ and use the same subscript $X$ for external thresholds defined by these quantities. Let $\epsilon=1/64$. Choose a sufficiently small fixed $\delta>0$ with $\delta<\epsilon/10$, as specified below. The eligible primes for a squarefree product $W$ are

$$
 \mathcal P_X=\{p:\exp(4T)\le p\le X^\delta\}
 \setminus\bigl([V_X/2,2V_X]\ \cup\ [Y_{*,X}^{1/2},Y_{*,X}^2]\bigr).
 \tag{2}
$$

The deleted bands cost $O(1)$ reciprocal prime mass by Mertens, uniformly in $X$. The full reciprocal product weight on all subsets of the remaining primes is therefore

$$
              \prod_{p\in\mathcal P_X}(1+1/p)\asymp_\delta \ell.
 \tag{3}
$$

With this weight normalized to one, membership of each prime in $W$ is independent with probability $1/(p+1)$. The reciprocal product weight of every individual $W$ is exactly $1/W$ before normalization. Chebyshev's prime bound and partial summation give $\mathbb E\log W\le C_0\delta L$ for an absolute $C_0$. Choose $\delta$ sufficiently small so that the probability of $W>X^{\epsilon/2}$ is at most $1/10$ by Markov. The total prime count of $W$ has mean $\log\ell+O(1)$ and variance $O(\log\ell)$ by Mertens and independence, so $\omega(W)\le 2\log\ell$ except on a set of probability $o(1)$.

Let $\mathcal P_X'$ be the primes of $\mathcal P_X$ in $(2V_X,Y_{*,X}^{1/2})$. Their count in $W$ has mean

$$
           \sum_{p\in\mathcal P_X'}\frac1{p+1}
                 =(1-\theta)\log\ell+O(1+\log\log\ell)
$$

and variance $O(\log\ell)$. Thus within $2(\log\ell)^{3/4}$ of $(1-\theta)\log\ell$ has probability $1-o(1)$. Also the probability of even $\omega(W)$ is at least $1/2$, since $\mathbb E(-1)^{\omega(W)}=\prod_{p\in\mathcal P_X}(1-2/(p+1))\ge0$. Keep the intersection of all four requirements: $W\le X^{\epsilon/2}$, total count $\le2\log\ell$, exceptional count in that window, and even total count. It still has probability at least $1/3$ for large $X$ by the union bound. Its original reciprocal mass is therefore $\asymp_\delta\ell$.

For all $N\in[X,(1+\Delta)X]$ the same actual primes in $W$ belong to the moving exceptional band as to $\mathcal P_X'$. Indeed $\log V_N-\log V_X=o(1)$ by differentiation with respect to $\log N$ over a bounded interval. The real expression before taking the floor in $J_N$ varies by $o(1)$, so $\log Y_{*,N}/\log Y_{*,X}=1+o(1)$. The discarded neighborhoods in (2) handle both boundaries including possible jumps of the floor. In addition all retained primes in $W$ are $>\exp(3T_N)$, and the occupancy window above is $(1-\theta+o(1))\log\ell_N$ uniformly over targets in this range.

Choose a single old lower prime $s$ in $[\exp(5T/4),\exp(7T/4)]$. It stays strictly inside the genuine old lower band over the same targets. Its reciprocal mass is bounded above and below by positive constants by Mertens, and its alphabet is disjoint from that of $W$. Let $\mathcal S_X$ be all the admitted products $S=sW$. Each $S\le X^\epsilon$ for large $X$ and has a unique such split. We have

$$
 \sum_{S\in\mathcal S_X}\frac1S\asymp \ell,\qquad
 \sum_{\substack{S\in\mathcal S_X\\p\mid S}}\frac1S
                                      \ll \frac{\ell}{p}.
 \tag{4}
$$

The upper bound drops the count, size and parity conditions positively and uses the product in (3) with membership of the specified prime; it also holds for a prime in the single lower slot. For an ineligible prime the sum is zero.

## 2. One fixed integer mask, constructed before the target

Set $\kappa=1/16$. Let $\mathcal A_X$ consist of all $n=S f F$ with $S\in\mathcal S_X$ and primes $f,F$ satisfying

$$
 \sqrt{Q_X}\,e^{\kappa T}\le Sf\le\sqrt{Q_X}\,e^{2\kappa T},
       \qquad
 \frac X2\le SfF\le\frac{(1+\Delta)X}{2}.
 \tag{5}
$$

These are integer masks on $n$ only; they do not restrict which divisors enter its true inner sum. For large $X$, the whole $f$ range in (5) is above $X^{.4}$ and below $\sqrt X$, while $F>\sqrt{(1+\Delta)X}$. This follows from $S\le X^\epsilon$, $Q_X\sim X e^{-20T}$ and the two intervals in (5). Consequently all factors in a representation are distinct, the split into $S,f,F$ is unique, and $f,F$ are beyond all old exceptional bands. The old rough parts on both legs are actual products $W f F$ and their count of factors in the exact moving exceptional interval is exactly the count from §1. Total old rough arity is at most $2\log\ell+2$, far below the very-high-arity tail.

For each fixed $S$, the reciprocal prime mass of $f$ in (5) is $\asymp T/L$. This follows by partitioning the log interval of width $\kappa T$ into a proportional number of fixed-ratio intervals, on which the PNT gives $\asymp1/L$ uniformly since all $f\ge X^{.4}$. For each such prime the $F$ interval has fixed relative width and both endpoints have logarithm comparable to $L$, so the PNT counts $\asymp_\Delta X/(SfL)$ choices, also uniformly. Thus the number of elements in the representation fiber for $S$ is

$$
                      \asymp_\Delta \frac{XT}{SL^2}.
 \tag{6}
$$

The total by (4) and $T=L/\ell$ is $\#\mathcal A_X\asymp_\rho X/L$. To check the unit exclusion, if $p$ is in an $S$ alphabet, (4) and (6) give
$\#\{n\in\mathcal A_X:p\mid n\}\ll_\rho X/(pL)$.
All these primes are $\ge\exp(5T/4)$. Any remaining prime that divides a mask element is $\ge X^{.4}$, and its incidence is at most $(1+\Delta)X/p$ by the trivial multiple count. Therefore the number of ordered pairs in $\mathcal A_X^2$ having a common prime is at most

$$
 \ll_\rho \frac{X^2}{L^2}\sum_{j\ge e^{5T/4}}\frac1{j^2}
                       +X^2\sum_{j\ge X^{.4}}\frac1{j^2}
     =o(X^2/L^2).
 \tag{7}
$$

Since the two operands lie in the same tight central interval and are odd, every coprime ordered pair yields an even target $N\in[X,(1+\Delta)X]$ with true central units. Explicitly, $(nm,N)=1$ for $N=n+m$ is equivalent to $(n,m)=1$. There are $\gg_\rho X^2/L^2$ such pairs.

## 3. The true signed mark on every retained pair

Take any genuine coprime pair $n=SfF, m=UgG$ from these masks and its actual even target $N$. Put $A=Sf$, $B=Ug$. Throughout this target window $\log N-\log X=O(1)$, $T_N-T=o(1)$, and $Q_N/Q_X=(N/X)(1+o(1))$. From (5) we therefore have the strict inequalities

$$
 D_N<A,B<\sqrt N,\qquad F,G>\sqrt N,\qquad
       Q_N<AB< e^{T}Q_N .
 \tag{8}
$$

The upper bound uses $4\kappa=1/4<1$, with ample room for the change of target. The two rough divisors $A/s$ and $B/t$ (writing $U=tW'$) exceed $D_N/s,D_N/t$ respectively and lie below $\lfloor Q_N/(D_N+1)\rfloor$ for large $X$, so both old [shrinking proper-divisor gap](r67-source-two-higher-bands-shrinking-divisor-gap.md) orientations indeed fail.

Every divisor label $Fz$, $z\mid A$, is long and passes the product gate against every opposite long label $e$: $F(D_N+1)>\sqrt N(D_N+1)>Q_N$. Holding $e$ fixed, their complete signed logarithmic sum on the first leg is

$$
       \sum_{z\mid A}\mu(Fz)\log(A/z)=-\Lambda(A)=0
$$

because $A$ has at least the two distinct primes $s,f$. Hence all those labels disappear by exact signed cancellation. For the remaining labels, the same argument eliminates the whole opposite family containing $G$. In the remaining families $d\mid A,e\mid B$, the only labels that can pass $de>Q_N$ are $d=A,e=B$: omitting any prime factor on either side divides the maximum product by at least $\exp(5T/4)$, which exceeds the allowance in (8). These two maximum labels pass both individual long tests. Their Möbius signs are $+1$ since, on each side, the number of factors in $W$ is even and two more factors enter the maximum label. Thus the genuine inner sum, including the exterior minus sign in (1) of the joint-count note, is precisely $-\log F\log G$. This is negative of magnitude $\gg L^2$, uniformly in the retained pairs. No other labels are artificially removed by the masks.

## 4. A target with normalized nonvanishing

For each target use the same mask $\mathcal A_X$ on each leg and $I=I_0$. All unit pairs from these masks have the same sign by §3, and every point counted in (7) as nonunit is excluded by the original mask. Summing the true signed magnitudes over even targets in $[X,(1+\Delta)X]$ gives $\sum_N |R_N(I_0)|\gg_\rho X^2$. The standard binary singular series is a fixed positive constant times $\prod_{p\mid N,\,p>2}(1+1/(p-2))$ for even $N$. Expanding the latter product and using the convergent Euler product $\prod_{p>2}(1+1/(p(p-2)))$ gives $\sum_{N\le(1+\Delta)X,\, 2\mid N}\mathfrak S(N)\ll X$. In particular $\sum_{X\le N\le(1+\Delta)X,\,2\mid N}\mathfrak S(N)N\ll X^2$. Comparing the two sums proves (1) for at least one even target in the window.

At these occupancies the entropy bound does not apply: each normalized count approaches $1-\theta$, whose rate is $(1-\theta)(1+\log 2)$, whereas the budget for the two rates is below $1-4\theta$. The obstruction is now an actual normalized lower bound for a **masked** statistic, not just a large reciprocal majorant. However it is the mask that prevents contributions from other actual operands from canceling it. No inference to the unrestricted signed central sum or the spectral conjecture follows.
