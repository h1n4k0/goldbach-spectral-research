# A conductor-defect cutoff for genuine exterior zero pairs

**Scope.** This gives an unconditional bound on the number of odd characters with large conductor defect and, under local Dirichlet GRH at $N$, removes their contribution from the [exterior distinct-copy residue kernel](r31-operator-zero-diagonal.md#3-relation-to-the-actual-two-zero-gram-and-its-cutoff) without translation averaging. Conductors comparable to $N$ are not controlled. For example, when $N=2p$ with $p$ an odd prime, every odd character has conductor $p=N/2$. The matching lower bound below is for character counts, not for the operator norm.

Write $L=\log N$, $\ell=\log L$, and let $q_\chi$ be the primitive conductor of $\chi\bmod N$ for even $N>2$. For every fixed $C>0$, set
$$
 \mathcal E_C(N)=\{\chi\bmod N:\chi(-1)=-1,\ 
              \log(N/q_\chi)\ge C\ell^2/\log\ell\}.
$$
Uniformly as $N\to\infty$ through even integers,
$$
 \Pr_{\chi\ {\rm odd}}(\mathcal E_C(N))\le L^{-C+o(1)} . \tag{1}
$$
This counting statement is unconditional. Under the original local GRH at $N$, the contribution to the true distinct-copy Gram kernel from these characters alone, still normalized by the total number of odd characters as in R31, has HS norm
$$
 O\big(L^{3-C+o(1)}\big) \tag{2}
$$
on the unbounded log exterior $x,z\ge H$ for any $H\ge0$. It holds with or without the R31 mask and with a common finite ordinate cutoff or its weighted $L^2$ limit. For a desired inverse-log error $o(L^{-K})$, take any fixed $C>K+3$ and apply (2) to the finite residual of R31 on its own prescribed $(H,B)$ domain. No smoothing or averaging over $N$ is used.

## 1. The uniform conductor count

For each $p^a\Vert N$, let $d_p=a-e_p$ where $e_p$ is the local conductor exponent of a uniformly selected character. By CRT these defects are independent for the full character family, and
$$
 \Pr(d_p\ge j)=\frac{\phi(p^{a-j})}{\phi(p^a)}\le 2p^{-j},
 \qquad 1\le j\le a .
$$
Indeed the allowed local characters are exactly those factoring through $p^{a-j}$. For $0<\kappa\le1/2$, summing by levels of $d_p$ gives
$$
 \mathbb E p^{\kappa d_p}
 =1+\sum_{j=1}^a(p^{\kappa j}-p^{\kappa(j-1)})\Pr(d_p\ge j)
 \le 1+O(p^{-1+\kappa}),
$$
with an absolute constant by the geometric sum. Set $\kappa=\log\ell/\ell$. The primes $p>L$ dividing $N$ number at most $L/\log L$, and each $p^{-1+\kappa}\le\ell/L$; they cost $O(1)$ in the sum. For $p\le L$, Chebyshev's bound and partial summation yield
$$
 \sum_{p\le L}p^{-1+\kappa}
 \ll 1+\int_1^\ell e^{\kappa v}\frac{dv}{v}
 =O(\log\ell+\ell/\log\ell)=o(\ell).
$$
For the integral, split at $1/\kappa$ and use $\int_1^R e^v\,dv/v\ll e^R/R$ on the second piece. Multiplication gives
$\mathbb E_{\chi\ {\rm all}}(N/q_\chi)^\kappa\le \exp(o(\ell))$.
The odd mean of this nonnegative variable is at most twice the full mean since $N>2$. Markov's inequality at the threshold $C\ell^2/\log\ell$ now gives (1).

## 2. The actual operator component

Use the exact log-coordinate Hardy weight $m(x)^2=(Ne^x)^{-2/L}+(Ne^x)^{-1/4}$, so $\int_H^\infty m(x)^2dx\ll L$. For a primitive inducing character define, on this exterior and with cutoff $T$,
$$
 f_{\chi,j}(x)=m(x)\frac{e^{i\gamma_{\chi,j}(L+x)}}{1+i\gamma_{\chi,j}},
 \qquad U_{\chi,T}=\sum_{|\gamma_{\chi,j}|\le T}f_{\chi,j}.
$$
All zeros are indexed by copies. The exact $j\ne j'$ residue component from this character is
$$
 2\pi\left(U_{\chi,T}\otimes U_{\chi,T}
                  -\sum_{|\gamma_{\chi,j}|\le T}f_{\chi,j}\otimes f_{\chi,j}\right).
 \tag{3}
$$
The standard primitive unit-bin zero count used in R31 is $O(\log(q_\chi(2+|b|)))$ for bin $[b,b+1)$, $b\in\mathbb Z$. On any unit spatial interval, majorize its indicator by a translate of a fixed nonnegative smooth compact test. Expand the squared unweighted residue series with this test; its Fourier transform is bounded by $O((1+|b-b'|)^{-2})$ for ordinates in the indicated two bins. The unit-bin coefficient masses are $O(\log(q_\chi(2+|b|))/(1+|b|))$. The summable bin-difference bound, or scalar Cauchy–Schwarz for each translate in bin index, gives squared mass $O(\log^2(2q_\chi))$, uniformly in the spatial translation and cutoff. Summing unit spatial intervals with the Hardy weight costs $O(L)$, so
$$
 \|U_{\chi,T}\|_2^2\ll L\log^2(2q_\chi),\qquad
 \sum_j\|f_{\chi,j}\|_2^2\ll L\log(2q_\chi).
$$
The second estimate follows directly by the same unit-bin count with the squared denominator. The first argument also gives weighted $L^2$ Cauchy convergence by restricting to the tails of a square-summable coefficient-mass sequence; the second sum converges absolutely in trace norm. Thus (3) has HS norm $O(L\log^2(2q_\chi))=O(L^3)$ uniformly, with or without finite $T$. Average (3) only over the subset $\mathcal E_C(N)$ using the total odd-family normalization and insert (1). Masking an HS kernel and further orthogonal compression are contractions in HS. This proves (2). The remaining high-conductor different-copy contribution is unestimated.

## 3. Sharpness of the count

For the even primorial $N_X=\prod_{p\le X}p$ one has $\ell=\log X+O(1)$ by Chebyshev. Put $\eta=1/\log\ell$ and $I=[X^{1-\eta},X]$. At each $p\in I$ the event of dropping $p$ from the conductor is independent in the full character family with probability $a_p=(p-1)^{-1}$. Its sum $S=\sum_{p\in I}a_p$ is $\asymp\eta$. For a direct verification, partition $I$ into full intervals $[t/R,t]$ of fixed ratio $R>1$ large enough that the upper and lower Chebyshev bounds give $\pi(t)-\pi(t/R)\asymp t/\log t$. Each full interval contributes $\asymp1/\log X$, and there are $\asymp\eta\log X$ such intervals; the possible end interval cannot change the upper bound. Write
$$
 m_0=\left\lceil\frac{C\ell^2}{(1-\eta)(\log X)\log\ell}\right\rceil
     =(C+o(1))\,\ell/\log\ell .
$$
Dropping $m_0$ of these primes forces the conductor defect in (1). The probability of exactly $m_0$ drops is at least $\prod_{p\in I}(1-a_p)e_{m_0}((a_p)_{p\in I})$, where $e_{m_0}$ is the elementary symmetric function. In $m_0$ independent selections with replacement and individual probabilities $a_p/S$, the repeat probability is at most $\binom{m_0}{2}\max a_p/S=o(1)$; hence $e_{m_0}\ge(1-o(1))S^{m_0}/m_0!$. The product is at least $e^{-2S}$. Now $m_0\log m_0=(C+o(1))\ell$ and $m_0|\log S|=o(\ell)$, so the probability is $\ge L^{-C+o(1)}$. The event uses only the large prime factors; the unused factor at $3$ gives a fair independent parity, so the same lower bound holds after conditioning on odd characters. Together with (1) this attains the exponent $C+o(1)$ on this family.

In particular, for any fixed $a>0$ one cannot just discard $q_\chi\le N/L^a$ as a uniformly vanishing fraction: on these primorials use instead $I=[X^{1/2},X]$ and any fixed integer $m_0>2a$. The same argument has $S\asymp1$, a fixed positive probability, and a defect at least $a\ell$ for all large $X$. This is a limitation of removing conductors by counting alone; it gives no lower estimate for the signed distinct-copy sum.
