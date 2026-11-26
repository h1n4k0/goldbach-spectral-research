# The exact exponential scale of the positive short-inclusion omission criterion

Keep the positive divisor statistic of [the double-logarithmic rarity proof](weak-s-type-ii-critical-prime-positive-inclusion-tail-sharp-rarity.md):

$$
 \mathcal T_N(H)=\sum_{\substack{r\mid\operatorname{rad}N\\ r>H}}
                                      \frac{3^{\omega(r)}}r ,
$$

where $\omega(r)$ counts the distinct prime divisors of $r$. Fix $0<M<Q$. Let $\mathcal L=\log Y$, $v=\log\mathcal L$, $\lambda=Q/M>1$, and let $E_{Q,M}(Y)$ count the even integers $Y\le N\le2Y$ for which

$$
                        \mathcal T_N(\mathcal L^Q)>\mathcal L^{-M}.
                                                                    \tag{1}
$$

**Theorem.** There are positive constants $c_{Q,M},C_{Q,M}$ such that for all sufficiently large $Y$,

$$
 Y\exp(-C_{Q,M}v^\lambda)\ \le\ E_{Q,M}(Y)\
                        \le\ Y\exp(-c_{Q,M}v^\lambda).
                                                                    \tag{2}
$$

In particular $\log(Y/E_{Q,M}(Y))\asymp_{Q,M}(\log\log Y)^{Q/M}$, with no exponent loss or logarithmic factor. This measures failure of the **positive omission criterion only**. It is not a lower bound for a true signed short-inclusion error, a centered-energy transport error, or Weak S.

## 1. Upper bound at the critical prime scale

Let $\sigma_0=M/Q=1/\lambda$, and set

$$
    \sigma=\sigma_0+\frac1{\log v},\qquad
    a_0=1-\sigma_0,\qquad a=1-\sigma .
$$

For all sufficiently large $Y$, $a_0/2\le a\le a_0$; in particular $a$ lies in a fixed compact subinterval of $(0,1)$ depending on $Q,M$. Write $W_N=\prod_{p\mid N}(1+3p^{-a})$. Since $\operatorname{rad}N$ is squarefree, positive Rankin gives $\mathcal T_N(\mathcal L^Q)\le\mathcal L^{-Q\sigma}W_N$. Thus (1) implies

$$
                       W_N>\exp(Qv/\log v).
                                                                    \tag{3}
$$

For any real $s\ge1$, expand $W_N^s$ into its nonnegative coefficients at squarefree divisors. The count of multiples of each divisor $d$ up to $2Y$ is at most $2Y/d$. It follows that

$$
 \frac1Y\sum_{Y\le N\le2Y}W_N^s
       \le 2\prod_p
                   \left(1+\frac{(1+3p^{-a})^s-1}{p}\right).
                                                                    \tag{4}
$$

The sum may include odd targets, as it is nonnegative. For each $s,Y$ the product converges since $a>0$. The mechanism is a positive divisor expansion, not an independence assertion.

Take a real splitting point $P=d_1v^\lambda$ with $0<d_1\le1$ fixed later and set $s=P^a\log P/12$. This satisfies $s\ge1$ for large $Y$. For $p\le P$, the factor in (4) is at most $(1+3p^{-a})^s$. The bound $\pi(x)\ll x/\log x$ and partial summation yield

$$
                         \sum_{p\le P}p^{-a}
                          \ll_{Q,M}\frac{P^{1-a}}{\log P}
$$

uniformly in $a_0/2\le a\le a_0$. For example, below $\sqrt P$ one may sum over all integers, costing $O_{Q,M}(P^{(1-a)/2})$, and above $\sqrt P$ the dyadic geometric sum using $\pi(x)\ll x/\log x$ gives the asserted bound. The small-prime logarithmic cost in (4) is therefore at most $O_{Q,M}(sP^{1-a}/\log P)=O_{Q,M}(P)$.

For $p>P$, one has $3sp^{-a}\le(\log P)/4$. Use $\log(1+u)\le u$ for $u\ge0$ and $(1+3p^{-a})^s-1\le e^{3sp^{-a}}-1\le 3sp^{-a}e^{3sp^{-a}}$. The tail logarithmic cost is at most

$$
 O\left(sP^{1/4}\sum_{n>P} n^{-1-a}\right)
        =O_{Q,M}(sP^{1/4-a})=O_{Q,M}(P^{1/4}\log P).
$$

Thus for a constant $A_{Q,M}$ independent of the fixed $d_1$,

$$
     \log\left(\frac1Y\sum_{Y\le N\le2Y}W_N^s\right)
                                  \le A_{Q,M}P
                                                                    \tag{5}
$$

for large $Y$. On the other hand the Markov exponent from (3) is

$$
 sQv/\log v
    =\frac{Q}{12}\,d_1^{a} e^{-\lambda} v^\lambda
                                             \frac{\log P}{\log v}
    \ge \frac{Q\lambda e^{-\lambda}}{24}\,d_1^{a_0}v^\lambda
                                                                    \tag{6}
$$

for all sufficiently large $Y$ with $d_1$ fixed. The equality uses $\lambda a+1=\lambda-\lambda/\log v$, and the inequality uses $d_1^a\ge d_1^{a_0}$ and $\log P/\log v\ge\lambda/2$. Choose $d_1$ so small that $A_{Q,M}d_1$ is at most half the coefficient on the right of (6); this is possible since $a_0<1$. Equations (3), (5), and (6) give the upper bound in (2).

## 2. Lower bound from a fixed multiple at the same scale

Choose $z=Dv^\lambda$, with $D>1$ fixed later, let $m$ be the number of primes in $(z/2,z]$, and put

$$
       S_z=2\prod_{z/2<p\le z}p,\qquad
       b=\log(z/2),\qquad
       k=\left\lfloor\frac{Qv}{b}\right\rfloor+1 .
$$

The prime number theorem gives $m\asymp z/\log z$ and $\log S_z\ll z$. Since $\lambda>1$, we have $k\le m$ for all large $Y$, with $k\asymp_{Q,M}v/\log v$ for fixed $D$. Each product of $k$ distinct primes from $(z/2,z]$ strictly exceeds $\mathcal L^Q$ and is at most $z^k$. Every positive multiple of $S_z$ is even, and its radical is divisible by every such squarefree product. For each of these multiples,

$$
 \mathcal T_N(\mathcal L^Q)\ge \binom{m}{k}(3/z)^k
                            \ge \left(\frac{c_1}{k\log z}\right)^k
                                                                    \tag{7}
$$

with an absolute constant $c_1>0$, using $\binom{m}{k}\ge(m/k)^k$. To preserve the strict threshold exactly at this scale, observe that $k\log z\le 2Qv+\log z\le(2Q+1)v$ for large $Y$ and any fixed $D$, using $\log(z/2)\ge(\log z)/2$. Consequently $\log(k\log z/c_1)\le\log v+C_1$ for a constant $C_1=C_1(Q)>0$ independent of $D$. Choose $\log(D/2)\ge\lambda(C_1+1)$, so $b=\lambda\log v+\log(D/2)\ge\lambda(\log v+C_1+1)$. Then

$$
 \begin{split}
 k\,\log(k\log z/c_1)
    &\le \frac{Qv}{b}(\log v+C_1)+O_Q(\log v)\\
    &\le Mv-\frac{Qv}{b}+O_Q(\log v)<Mv ,
 \end{split}
                                                                    \tag{8}
$$

because $Q/\lambda=M$ and $v/b\gg_{Q,M}v/\log v$ for large $Y$. Thus (7) is strictly above $\exp(-Mv)=\mathcal L^{-M}$. There are $Y/S_z+O(1)$ multiples in $[Y,2Y]$, and $\log S_z\ll Dv^\lambda=o(\log Y)$ for fixed $D$. This gives at least $Y\exp(-C_{Q,M}v^\lambda)$ such even targets for large $Y$, completing (2). The construction gives lower bounds only on the number of failures of (1), not on any true signed remainder.
