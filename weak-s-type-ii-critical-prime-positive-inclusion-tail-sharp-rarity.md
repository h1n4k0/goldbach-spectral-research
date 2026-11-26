# A sharp double-logarithmic rarity exponent for the positive short-inclusion criterion

This note quantifies a specific arithmetic test used in [the typical-target hard rational proof, §1](weak-s-type-ii-critical-prime-typical-target-hard-rational-transport.md#1-average-the-actual-short-inclusion-tail-without-capping-the-retained-radical). It is not a lower bound for the actual signed inclusion error, centered energy error, or Weak S.

For $H>0$ and a positive integer $N$, set

$$
  \mathcal T_N(H)=
    \sum_{\substack{r\mid\operatorname{rad}N\\r>H}}\frac{3^{\omega(r)}}r ,
$$

where $\omega(r)$ counts distinct prime factors. Fix constants $0<M<Q$. Let $\mathcal L=\log Y$, $v=\log\mathcal L$, and let $E_{Q,M}(Y)$ count the even integers $Y\le N\le2Y$ for which

$$
                      \mathcal T_N(\mathcal L^Q)>\mathcal L^{-M}.
                                                                    \tag{1}
$$

**Theorem.** Put $\lambda=Q/M$. For each $0<\varepsilon<\lambda-1$ there exist positive constants $c_\varepsilon,C_\varepsilon$ (also depending on $Q,M$) such that, for every sufficiently large $Y$,

$$
 Y\exp(-C_\varepsilon v^{\lambda+\varepsilon})
      \ \le\ E_{Q,M}(Y)\ \le\
                   Y\exp(-c_\varepsilon v^{\lambda-\varepsilon}).
                                                                    \tag{2}
$$

In particular $\log\log(Y/E_{Q,M}(Y))/\log\log\log Y\to\lambda$. The targets counted here fail only the stated nonnegative criterion. The centered energy can still obey its transport formula on any or all of them.

## Upper bound

Fix $\sigma=1/(\lambda-\varepsilon)$, so $0<\sigma<1$ and $Q\sigma>M$. For $W_N=\prod_{p\mid N}(1+3p^{-1+\sigma})$, positive Rankin gives $\mathcal T_N(\mathcal L^Q)\le\mathcal L^{-Q\sigma}W_N$. For $s\ge1$, the positive expansion of $W_N^s$ over squarefree divisors and the count of multiples up to $2Y$ give

$$
   \frac1Y\sum_{Y\le N\le 2Y}W_N^s
       \le 2\prod_p
         \left(1+\frac{(1+3p^{-1+\sigma})^s-1}{p}\right).
                                                                    \tag{3}
$$

At $P=s^{1/(1-\sigma)}$, the logarithm of the contribution of $p\le P$ is $O_\sigma(sP^\sigma)$ by summing $s n^{-1+\sigma}$ over all integers $n\le P$, since the individual factor in (3) is at most $(1+3p^{-1+\sigma})^s$. For $p>P$, one has $s p^{-1+\sigma}\le1$, and the logarithms sum to $O_\sigma(s P^{-1+\sigma})=O_\sigma(1)$ by summing $s n^{-2+\sigma}$ over $n>P$. Hence (3) has logarithm at most $A_\sigma s^{1/(1-\sigma)}$ for some $A_\sigma>0$. In (1) necessarily $W_N>\exp((Q\sigma-M)v)$. Choose

$$
    s=\left(\frac{(Q\sigma-M)v}{2A_\sigma}\right)^{(1-\sigma)/\sigma},
$$

which is at least one for all large $Y$. Markov gives at most $Y\exp[-(Q\sigma-M)vs/2]$ such targets. This gives the upper bound in (2) because $1/\sigma=\lambda-\varepsilon$. No independence of prime divisibility is used.

## Lower bound using a fixed divisor of each constructed target

Put $\nu=\lambda+\varepsilon$, $z=v^\nu$, and let $\mathcal P_z$ be the set of primes in $(z/2,z]$. For large $Y$ they are all odd. Write

$$
 m=\#\mathcal P_z,\qquad S_z=2\prod_{p\in\mathcal P_z}p,\qquad
 k=\left\lfloor\frac{Qv}{\log(z/2)}\right\rfloor+1 .
$$

The prime number theorem gives $m\asymp z/\log z$ and $\log S_z\ll z$. Since $\nu>1$, one has $k\le m$ for large $Y$ and $k\sim (Q/\nu)v/\log v$. For every multiple of $S_z$, all products of $k$ distinct primes from $\mathcal P_z$ are distinct squarefree divisors of $\operatorname{rad}N$, exceed $\exp(Qv)=\mathcal L^Q$ by the choice of $k$, and are at most $z^k$. Consequently each such target has

$$
 \mathcal T_N(\mathcal L^Q)
       \ge \binom{m}{k}(3/z)^k
       \ge \left(\frac{3m}{kz}\right)^k
       \ge \left(\frac{c_1}{k\log z}\right)^k ,
                                                                    \tag{4}
$$

with an absolute $c_1>0$. Here $\binom{m}{k}\ge (m/k)^k$ follows by multiplying the $k$ factors $(m-i)/(k-i)\ge m/k$. The logarithm of the right side of (4) equals $-(Q/\nu+o(1))v$, because $\log k+\log\log z=\log v+O(1)$. Since $Q/\nu<M$, each constructed target satisfies the strict failure (1) for large $Y$.

Every multiple of $S_z$ is even. There are $Y/S_z+O(1)$ of them in $[Y,2Y]$, and $\log S_z=O(v^\nu)=o(\log Y)$ for this fixed $\nu$. Thus at least $Y\exp(-C_\varepsilon v^\nu)$ of these targets occur for all sufficiently large $Y$. This supplies the lower bound in (2), and the limit follows because $\varepsilon$ is arbitrary. It establishes the double-logarithmic order of the exceptional set defined by (1) for fixed $Q,M$, not a necessary exceptional set of the genuine energy theorem.
