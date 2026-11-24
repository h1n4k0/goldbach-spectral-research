# Actual moving mixed minors with adaptive prime counts and whole small-prime patterns

**Scope.** This extends the [moving true-label minor estimate](r80-spectral-adaptive-divisor-label-minor.md). It controls arbitrary target-dependent selections by exact prime counts in finitely many moving prime intervals, and by the actual product of all prime factors up to a moving polylogarithmic bound. These are selections on the actual integers, not approximated counts or a fixed common roughness gate. An arbitrary unrelated per-target right sequence is still not permitted. The theorem is unconditional on a density-one set; there is no fixed-target, major, or weak S conclusion.

Retain the ambient scale $Y$, even targets $N\in[Y,2Y]$, $\delta,\kappa,Q_N,B_N$, the actual moving minor $\mathfrak m_N$, squarefree tuples $abcd=m$, their weight $w(a,b,c,d)$, fixed common multiplier $\rho_m$, and the six independently moving label intervals of the preceding paper. Write $L=\log Y$ and $\mathbf t=(ab,ac,abc,P^+(m),m/P^+(m))$. Fix $C>0$ and a nonnegative integer $r$. For each $N$ choose any $1\le Z_N\le L^C$, and attach to the tuple its exact small-prime part

$$
 b_N^{\rm sm}(m)=\prod_{\substack{p\mid m\\p\le Z_N}}p .
$$

This variable is distinct from the divisor label named $b$ in the decomposition $abcd=m$. Also choose $r$ arbitrary real prime intervals, each to count prime divisors in one of $m,t_1,\ldots,t_5$ (the choice of which coordinate for each interval is fixed). Let $\mathbf c_N$ be the resulting exact count vector. Multiply the chosen tuple by any bounded function of this whole pattern and the actual target gcds,

$$
 F_N\bigl(b_N^{\rm sm}(m),\mathbf c_N,(t_1,N),\ldots,(t_5,N)\bigr),
 \qquad |F_N|\le1 .
$$

There is no regularity or relationship required between these functions or intervals at different $N$. Let $A_N(m)$ be the resulting signed coefficient. The left test $P_{I,\omega}$ is the same actual hard central interval and bounded-variation prime test as in the preceding paper.

**Theorem.** There exists $c>0$ depending only on $\delta,C$ such that, for each fixed common $\rho$, outside $O_{\delta,\kappa,C,r}(Y^{1-c})$ even targets one has

$$
 \sup\left|\int_{\mathfrak m_N}P_{I,\omega}(\theta)
                    \widehat A_N(\theta)e(-N\theta)\,d\theta\right|
                \ll_{\delta,\kappa,C,r}Y^{1-c}.
 \tag{1}
$$

The supremum is simultaneous in all the moving selectors just described, as well as $I,\omega,Q_N,B_N$, and the bounds are independent of the fixed common $\rho$. For $C\le2$ the stronger mean-square estimate $O_{\delta,\kappa,C,r,\epsilon}(Y^{3-\delta/2+\epsilon})$ holds as in the preceding paper. Thus in this range one can keep the whole adaptive small-prime pattern without an additional power cost.

## 1. Encode the exact comparators, not the moving output sequences

For a squarefree integer $d$ list its distinct prime divisors increasingly as $p_j(d)$. Pad every position beyond the end by $10\lceil Y\rceil$, and set $p_0(d)=1$. Every count of primes at most a real $u$ can be encoded on the ambient support by a threshold $1\le u\le5Y$, using an integer-equivalent threshold if the endpoint was strict. The statement that this cumulative count equals $k$ is exactly

$$
                         p_k(d)\le u<p_{k+1}(d).
 \tag{2}
$$

A real interval with either type of endpoint gives the difference of two such cumulative counts after converting the endpoints on integers. The empty case is immediate. Counts are therefore selected by two fixed order-statistic axes for each member of a vector of $2r$ cumulative ranks. There are $O((1+\log Y)^{2r})$ rank vectors because every $d$ divides an integer at most $5Y$. At a fixed rank vector all order-statistic coordinates are fixed functions of the original tuple, not of the target. The relation in (2) gives one product of hard intervals on those coordinates.

Write $P=L^C$. For each fixed squarefree $s$ with $P^+(s)\le P$, require $s\mid m$. Use $P^+(1)=1$ and $P^-(1)=10\lceil Y\rceil$. The exact criterion for selecting this fixed $s$ as the true $b_N^{\rm sm}(m)$ is

$$
                       P^+(s)\le Z_N<P^-(m/s).
 \tag{3}
$$

The first inequality is a scalar test on $s$ at the target. The second uses one additional true axis of the fixed tuple with $s\mid m$. Even after padding the prime-order axes and taking minima in (3), all their values are integers in a polynomial-size fixed range. At each tuple the small-prime part is unique.

For each fixed $s$ and rank vector the function of the five gcds is still bounded by one, so apply the coordinatewise exact divisor-lattice expansion (3) of the preceding paper. For the resulting common divisibility vector {\bf h}$, every requirement $h_i\mid t_i$ uses a divisor of $m$. The original coefficients and physical domain are unchanged. Thus the remaining function for a fixed $s$, rank vector and {\bf h}$ is one hard rectangle on the original axes and the added prime-order and rough-suffix axes. The left tests, torus rectangles and slow-grid rounding are the same as in that proof. In particular before expansion the right sup norm remains $O(Y(1+\log Y)^3)$ and rounding costs a negligible error uniformly in all the genuine adaptive masks.

## 2. Common squared energy before taking target suprema

For each fixed $s$, rank vector and {\bf h}$, take the same maximal Bessel estimate as in §3 of the preceding paper, with the additional right axes encoded above. Their number is fixed in terms of $r$, so the canonical dyadic expansions and sums over levels cost fixed powers of $1+\log Y$. At each fixed set of right levels, every contributing signed tuple is assigned to exactly one cell. For a given $m$ the sum over these cells of the squared absolute coefficients is at most $\tau_4(m)^2$ by positive domination. It remains to sum the right norms over all fixed $s$, rank vectors and {\bf h}$; these indices may be summed in the Bessel bound because all resulting Fourier-coefficient squares are nonnegative.

For each $m$ there are at most $\tau(m)$ eligible $s$, irrespective of how many squarefree integers have prime factors at most $P$, and at most $\tau(m)^5$ eligible vectors {\bf h}$. Hence the summed right energy is

$$
 \ll_r(1+\log Y)^{2r}
      \sum_{\substack{m\le5Y\\m\ {\rm squarefree}}}\tau(m)^6\tau_4(m)^2
       \ll_r Y(1+\log Y)^{1023+2r}.
 \tag{4}
$$

The last summand is $\tau_{1024}(m)$ on squarefree $m$. For any fixed family of $s$ this proves the same joint maximal square sum $Y^{3-\delta/2+o(1)}$ as in the predecessor *before* taking the target-specific sum of signed $s$ contributions. The factor $Y^{2-\delta/2}$ in it is the pointwise sum of squared left disjoint-interval transforms on the fixed common minor, as there; the extra prime axes do not interact with the left estimate or with the disjoint rational cells. Summation over each rank vector and each {\bf h}$ is likewise over fixed Bessel functions; it does not replace any mask by a continuous prime density.

At a specific target, sum the output values for the finitely many rank vectors and divisibility vectors using Cauchy. These lose only $Y^{o(1)}$ by the rank count and $\tau(N)^{15}$ as in the predecessor. The signs and coefficients across $s$, including their eligibility in (3), may depend completely arbitrarily on $N$. Thus an additional Cauchy factor is required for this last sum; we control it in two ways.

## 3. Full polylogarithmic alphabet and exact tail

Choose $\eta=\delta/8$ and a fixed $0<t<1/4$ with $Ct<1/4$. Retain $s\le Y^\eta$ and use unweighted Cauchy in the sum over $s$ for a factor at most $Y^\eta$ in the square. Combining (4) and the divisor and rank losses gives squared maximal bound $Y^{3-\delta/2+\eta+o(1)}$ for this retained actual integral.

For the omitted tail define $B(m)=\prod_{p\mid m,\ p\le P}p$. Since $Z_N\le P$, the omitted coefficient is supported only where $B(m)>Y^\eta$. Its absolute value is at most $\tau_4(m)$ by the exact tuple count (each tuple would have a single actual output $s,\mathbf c_N$). The positive divisor expansion of $B(m)^t$, followed by $\tau_4(m)^2=\tau_{16}(m)$ on the squarefree support, gives

$$
 \sum_{\substack{m\le5Y\\m\ {\rm squarefree}}}\tau_{16}(m)B(m)^t
 \ll Y(1+\log Y)^{15}
        \prod_{p\le P}\left(1+\frac{16(p^t-1)}p\right)
      =Y^{1+o(1)}.
 \tag{5}
$$

Indeed the local divisor weight is $p^t-1$ where $p\mid m$ and $p\le P$. If the expansion prescribes a squarefree $d\mid m$, write $m=dv$ with $(d,v)=1$, use multiplicativity and sum $\tau_{16}(v)$ positively. The product logarithm is $O_t(P^t)=o(\log Y)$ by summing even over all integers. Rankin now bounds the omitted squared coefficient norm by $Y^{1-\eta t+o(1)}$. Cauchy against the $Y^{1/2+o(1)}$ left norm on the actual moving minor gives the deterministic omitted error at most $Y^{1-\eta t/2+o(1)}$. This tail argument does not require any regularity of the new selector.

For example take $c=\eta t/8$. Markov at $Y^{1-c}$ bounds the number of exceptional even targets for the retained integral by $Y^{1-\delta/2+\eta+2c+o(1)}=O(Y^{1-c})$; the actual omitted error is uniformly smaller. Restore the exact slow-coordinate endpoints as in the predecessor. This proves (1) without rank or occupancy restrictions on the actual integers themselves.

## 4. No extra fixed power when $C\le2$

Use all $s$ without trimming and replace the preceding Cauchy by weighted Cauchy: the first factor in the square is $\sum_s s^{-1/2}$, and the summed Bessel squares carry the weight $s^{1/2}$. The first factor is at most

$$
 \prod_{p\le P}(1+p^{-1/2})
 \le \exp\!\left(O\!\left(\frac{\sqrt P}{\log(2P)}\right)\right)=Y^{o(1)},
$$

by Chebyshev's bound and partial summation (with constants adjusted below any fixed $P$). In place of (4), the right energy weighted by $s^{1/2}$ is at most the log rank factor times

$$
 \sum_{\substack{m\le5Y\\m\ {\rm squarefree}}}
       \tau(m)^5\tau_4(m)^2
         \sum_{\substack{s\mid m\\P^+(s)\le P}}s^{1/2}
 \ll Y(1+\log Y)^{511}
             \prod_{p\le P}(1+512p^{-1/2})=Y^{1+o(1)}.
$$

To obtain this inequality expand the inner divisor sum directly; for prescribed $s$, the squarefree main weight is $\tau_{512}(s)\tau_{512}(m/s)$ and its unrestricted positive sum costs $O(Y/s)$ times the displayed log power. Both Euler-product estimates are uniform also at $P=(\log Y)^2$ because $\sqrt P/\log(2P)=o(\log Y)$. The same Bessel argument now gives the asserted full exponent $3-\delta/2+o(1)$ with no additional power loss. None of these arguments implies cancellation on the major arcs or allows a completely arbitrary target-dependent multiplier on the complementary rough integer $m/s$.
