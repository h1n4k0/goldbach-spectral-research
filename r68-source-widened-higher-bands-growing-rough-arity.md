# Widened higher bands and slowly growing rough arity without a divisor gap

Use the exact signed central sum, squarefree unit masks, strict $d>D,e>D,de>Q$, and independent integer masks of the [no-divisor-gap theorem](r68-source-two-higher-bands-no-divisor-gap.md). Thus $I\subseteq I_0=[\rho N,(1-\rho)N]$ is hard, $L=\log N$, $\ell=\log L$, $T=L/\ell$, and the original $D,Q$ are $\lfloor\sqrt N e^{-20T}\rfloor,\lfloor N e^{-20T}\rfloor$. In the slots $n=su,m=tv$, the nonempty lower products have all primes in

$$
   [\exp(c_i T/\ell^{a_i}),\exp(d_i T)],\qquad
                   0<c_i<d_i,\quad a_i\ge0
 \tag{1}
$$

with fixed constants. In particular $a_i>0$ admits complete bands with reciprocal mass growing as $a_i\log\ell+O(1)$; these are not fixed sparse alphabets. No lower-product cap or proper-divisor gap is imposed. The nonempty rough parts consist of primes $\ge Y=\exp(L/K)$, where

$$
           K=K_0+\lfloor\gamma\log\ell\rfloor,\qquad
           K_0\ge5\ {\rm fixed\ integer},\quad \gamma\ge0\ {\rm fixed}.
 \tag{2}
$$

These rough and lower ranges are disjoint eventually. The case $\gamma>0$ allows actual rough arity to grow.

**Theorem (unconditional, pointwise).** Suppose

$$
                  b=1-2(a_1+a_2)-\gamma\log 2>0 .
$$

For every fixed $A>0$, every sufficiently large even target and every admitted hard $I$ and integer mask, the exact signed quantity $R_N(I)$ obeys

$$
      |R_N(I)|\ll_{\rho,c_i,d_i,a_i,K_0,\gamma,A}
         \mathfrak S(N)\bigl(|I|K^4\ell^{-b}+NL^{-A}\bigr).
 \tag{3}
$$

For fixed arity parameter $\gamma=0$ this widens both higher bands as long as $a_1+a_2<1/2$. For $\gamma>0$, the factor $K^4=O((1+\log\ell)^4)$ does not prevent a loglog saving. The statement has no exceptional moduli or first-moment transfer. It does not reach the rough floor $\exp(C L/\log L)$ with fixed $C$, the full dense intermediate range, nonsquarefree inputs, or Hypothesis S.

## 1. Positive moment and pointwise tail budgets

The unmarked lower profile on slot $i$ is

$$
 \sum_{\substack{w\ {\rm squarefree}\\p\mid w\Rightarrow p\ {\rm in\ band}\ i}}
       \frac{\tau(w)\lambda^*(w)}w
  =\prod_{p\ {\rm in\ band}\ i}(1+2\lambda^*(p)/p)
     \ll \ell^{2a_i},\qquad
 \lambda^*(w)=\prod_{\substack{p\mid w\\p>2}}\frac{p-1}{p-2}.
 \tag{4}
$$

Indeed the log endpoint ratio is $(d_i/c_i)\ell^{a_i}$, so Mertens and the $O(p^{-2})$ correction give (4). Inserting one least-prime log on $w>1$ costs at most $O(T)$ by the upper endpoint of (1). For the square of the divisor count the corresponding Euler factors are $1+4/p$, giving $\ell^{O(1)}$ instead of $O(1)$.

Each true rough part has at most $K$ prime factors and hence at most $2^K$ divisor labels. We may truncate $s,t\le N^\varepsilon$ with $\varepsilon=1/32$, losing $O_A(NL^{-A})$, without changing the stated original selection. To check this use Cauchy on the true sum line as in §1 of the no-gap theorem. Counting all multiples of one lower product gives at most $N/w$ possibilities, and each absolute marked divisor sum is at most $L 2^K\tau(w)$. Rankin at fixed $\lambda/T$ gives the squared reciprocal tail $L^{-\varepsilon\lambda}$ times $\prod(1+4e^{d_i\lambda}/p)=\ell^{O_\lambda(1)}$. This uses Mertens on (1); the exponent is fixed after choosing $\lambda$ sufficiently large given $A$. The square-root loss, polynomial factors of $\ell$, and $L^2 2^{2K}=\!L^2\ell^{O(1)}$ are all absorbed. This calculation uses no maximum lower-divisor count in the opposite tail.

The unrestricted rough reciprocal profile is $O(K)$ since

$$
             \prod_{Y\le p\le N}(1+1/p)
                         \ll \log N/\log Y=K .
$$

For a nonempty rough product in a log interval of width $W$, split off one prime and overcount by all such choices. With its complementary rough product fixed, the prime reciprocal profile in that interval is $O((1+W)/\log Y)$ by Chebyshev. Summing the complementary reciprocal weights gives

$$
                 O\left(K^2(1+W)/L\right).
 \tag{5}
$$

This avoids counting as though there were $K$ independent positions with growing harmonic mass on each. The frozen rough factors of $\lambda^*$ are still bounded, since a true rough product has at most $K$ prime factors $\ge Y$, hence contributes $\exp(O(K/Y))$.

## 2. Same exact one-freeze strip at variable sieve depth

The proof of §2 of the no-gap theorem is independent of the arities. Its exact signed least-prime expansion has two heavy logs, two heavy–light terms, and a light–light term. A nonzero second difference has a genuine switch on a chosen side (take the first), and the mixed terms switch on their heavy side. For example if $a=P^-(s)$ and a first-side divisor base is $cf$, an actual opposite long value $E>D$ implies on a switch

$$
        cf\le\max(D,Q/E)<a c f,\qquad
                         \frac{D}{a c}<f\le\frac{\sqrt N}{c}.
 \tag{6}
$$

The other-side label is not needed for the latter positive envelope. Its log width is $20T+\log a+o(1)=O_{d_i}(T)$. Since $s,t<D$ and $u,v>\sqrt N$ after the Rankin truncation, a switched rough label is nonempty and proper. These are the original strict shifted endpoints; no substitution of $Q$ or assumption about which branch triggered the switch is made.

Freeze $h=sf,k=t$ on a first-side switch, $h=s,k=tg$ on a second-side switch, and $h=s,k=t$ for the light–light term. Thus $hk\le N^{1-\omega}$ for $\omega=1/2-2\varepsilon$, and the two actual affine remaining variables are nonempty rough products with smallest prime at least $Y$. Use the same quadratic affine upper sieve, now at

$$
        Z=N^{\omega/24},\qquad z=\exp(\eta L/K),
         \qquad 0<\eta<\min(1,\eta_0\omega/24)
$$

with $\eta_0$ its small absolute constant. Then $z<Y$ and $\log z/\log Z=24\eta/(\omega K)<\eta_0$. The normalized truncated Euler weight still leaves at least half its mass below $Z$ by the usual $\log d$ expectation. Each genuine frozen pair has $(h,k)=1$ and $(hk,N)=1$, so the determinant $N$ and local root factors are exactly the same. The interval in its integer parameter has length $|I|/(hk)$, and the main upper term is

$$
           O\left(
             \frac{\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)}{hk}
                                \frac{K^2}{L^2}\right),
$$

with $O(Z^6)=O(N^{\omega/4})$ absolute floor error. The $K^2$ loss is precisely from $(\log z)^{-2}$. The floor-error proof uses only the support up to $Z$, the coefficient bound $\le d$ and the local root bound, and remains uniform in $K$.

There are $O(N^{1-\omega}L)$ ordered frozen pairs with unique rough/lower splits. Their lower-label multiplicities are $N^{o(1)}$ on the truncation (split the factors at $\sqrt L$), and all omitted rough-label costs are at most $2^{2K}=\ell^{O(1)}$. The original log weights are at most $L^2$. The total floor error is once again $O(N^{1-3\omega/4+o(1)})=O_A(NL^{-A})$, even for a short hard interval.

## 3. Exact counts of omitted labels and the final powers

For a switched term the chosen rough label is frozen as the whole integer $f$ or $g$, not expanded into multiple assignments of its prime factors. Only the **opposite rough label** is omitted, and its multiplicity on the actual operands is at most $2^K$. The lower divisor labels are included in (4). Use (5) with $W=O(T)$ in (6), main sieve density $K^2/L^2$, and the unchanged absolute mark bounds. After factoring out $\mathfrak S(N)|I|\ell^{2(a_1+a_2)}$, the positive main bounds are

$$
 \begin{array}{ll}
  \text{two-heavy second difference:}&O(K^4\,2^K/\ell),\\
  \text{either heavy--light term:}&O(K^4\,2^K/\ell^2),\\
  \text{light--light term:}&O(K^2\,2^{2K}/\ell^2).
 \end{array}
$$

The first row uses $L^2$, the second the actual light $O(T)$ in place of one heavy $L$, and the third two light $O(T)$ logs, no strip, and both omitted rough labels. These are positive enlargements only **after** the genuine signed switches and widths have been found. Since $2^K\le2^{K_0}\ell^{\gamma\log 2}$ and $b>0$, all rows yield (3). The loglog factors are not absorbed into a silently fixed arity constant.

To witness simultaneous widening and growing arity, take fixed $a_i>0,\gamma>0$ satisfying $b>0$ and band constants with $d_1+d_2<20$. About an external scale $X$, choose one lower prime $s$ or $t$ near $\exp(2c_iT_X/\ell_X^{a_i})$ in each slot. Let $r$ be the largest even integer at most $K_X/3$ for large $X$, which tends to infinity. On each side choose $r-1$ distinct rough primes in a fixed narrow relative interval around $X^{1/r}$, and the last one in a narrow relative interval around $X/(2s\prod p_j)$ or $X/(2t\prod p_j)$. The ordinary PNT supplies more than enough distinct primes in those intervals, whose centers grow, and all factors can be chosen globally distinct. The operands are near $X/2$, so the resulting $N$ is even with central units and $\log N=\log X+O(1)$. The moving lower endpoints and the possible change of at most one in $K$ do not consume the margins. All rough prime logs are $L/r+O(T+r)$, with the last log equal to $L/r-\log s+O(r)$ or $L/r-\log t+O(r)$. Hence they all exceed $L/K$. Any size-$r/2$ proper divisor containing the last rough prime has log $\tfrac12 L-\log s+O(r)$ or $\tfrac12 L-\log t+O(r)$, strictly inside both earlier shrinking gaps since $\log s,\log t\gg r$ and $T\gg r$. Nevertheless on this witness all rough labels with at least $r/2$ factors exceed D and pass the product test across the pair (the smallest such logs are $\tfrac12 L-\log s+O(r)$ and $\tfrac12 L-\log t+O(r)$); smaller rough labels are short even with the whole lower product since $L/r\gg T$. The summed long rough sign per side is $(-1)^{r/2}\binom{r-1}{r/2-1}$, so the actual summand is $-\binom{r-1}{r/2-1}^{2}\log s\log t$. This establishes nonvacuity and an unbounded admissible arity, not a lower bound on the aggregate.
