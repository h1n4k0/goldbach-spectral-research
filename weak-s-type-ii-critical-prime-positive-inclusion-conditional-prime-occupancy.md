# Prime occupancy among failures of the positive omission criterion

Use the positive omission statistic and even-target count of [the leading-constant theorem](weak-s-type-ii-critical-prime-positive-inclusion-tail-leading-constant.md). Fix $0<M<Q$, put $v=\log\log Y$, $\lambda=Q/M>1$, $Z=v^\lambda$ and $D_*=(M/(3\mathrm e))^\lambda$. Let $\mathcal F_Y$ be the even integers $N\in[Y,2Y]$ for which

$$
 \mathcal T_N((\log Y)^Q)>(\log Y)^{-M},\qquad
 \mathcal T_N(H)=\sum_{\substack{r\mid\operatorname{rad}N\\r>H}}
                                    \frac{3^{\omega(r)}}r .
$$

Here $\omega(r)$ counts distinct prime factors and $\mathrm e=\exp(1)$. The leading-constant theorem gives $\#\mathcal F_Y=Y\exp[-(D_*+o(1))Z]$. For fixed $B\ge1$, define the weighted prime disagreement with the primorial cutoff $D_*Z$ by

$$
 J_N(B)=\sum_{p\le Z^B}
          \big|\mathbf1_{p\mid N}-\mathbf1_{p\le D_*Z}\big|\log p .
                                                                    \tag{1}
$$

**Theorem.** For every fixed $B\ge1$ and $\tau>0$, there is a constant $c=c(Q,M,B,\tau)>0$ such that for all sufficiently large $Y$,

$$
 \#\{N\in\mathcal F_Y:J_N(B)\ge\tau Z\}
       \ \le\ Y\exp[-(D_*+c)Z],\qquad
 \frac{\#\{N\in\mathcal F_Y:J_N(B)\ge\tau Z\}}{\#\mathcal F_Y}
       \ \le\ \exp(-c Z).
                                                                    \tag{2}
$$

The cutoff in (1) is literal. In particular, for $B>1$ this identifies the prime-divisor pattern in logarithmically weighted mass both below $D_*Z$ and above it up to any fixed power of $Z$. It does not require exact divisibility by that primorial or restrict larger primes. No claim is made about the true signed truncation error, the centered energy error, or Weak S.

## 1. Mark missing and extra primes away from the transition

Set $\sigma_0=1/\lambda$, $a_0=1-\sigma_0$, and use precisely the optimal upper-bound parameters of the leading-constant theorem:

$$
 u=\frac1\lambda,\qquad
 \sigma=\sigma_0+\frac{u}{\log v},\qquad a=1-\sigma,\qquad
 s=\frac{\lambda}{3\mathrm e}D_*^{a_0}v^{\lambda-1}\log v.
$$

Write $t_p=(1+3p^{-a})^s$ and $X_N=\prod_{p\mid N}t_p$. Positive Rankin at $\sigma$ gives the necessary implication

$$
 N\in\mathcal F_Y\quad\Longrightarrow\quad
                   X_N>\exp(\lambda D_* Z).
                                                                    \tag{3}
$$

Indeed the bound before the power $s$ is $\mathcal T_N((\log Y)^Q)\le (\log Y)^{-Q\sigma}\prod_{p\mid N}(1+3p^{-a})$. Multiplication of the resulting logarithmic threshold $(Q\sigma-M)v$ by $s$ gives $\lambda D_*Z$. The unmarked Euler product satisfies

$$
 \sum_p\log A_p=(\lambda-1)D_*Z+o(Z),
                   \qquad A_p=1-\frac1p+\frac{t_p}p .
                                                                    \tag{4}
$$

This is exactly the Euler limit in §1 of the leading-constant theorem at the displayed $u,s$. On every fixed compact $0<\delta_1\le p/Z\le R_0$ its local scaling gives

$$
 \frac{\log(t_p/p)}{\log Z}
           =\left(\frac{D_*}{p/Z}\right)^{a_0}-1+o(1)
                                                                    \tag{5}
$$

uniformly. In fact $p^{-a}=v^{1-\lambda}e^{\lambda u}(p/Z)^{-a}$, so the first-order term in $s\log(1+3p^{-a})/\log Z$ tends to $(D_* /(p/Z))^{a_0}$, while $\log p/\log Z\to1$.

Take a fixed $0<\delta<\min(D_*/4,\tau/12)$. Ignore the primes $p\le\delta Z$ and $(D_*-\delta)Z\le p\le(D_*+\delta)Z$. The total possible ignored mass in (1) is at most $(3\delta+o(1))Z$ by the prime number theorem for the sum of $\log p$. Endpoints do not affect this asymptotic. Define the retained prime sets

$$
 \begin{split}
 \mathcal P_-&=\{p\le Z^B:\ \delta Z<p<(D_*-\delta)Z\},\\
 \mathcal P_+&=\{p\le Z^B:\ p>(D_*+\delta)Z\}
 \end{split}
$$

and the retained disagreement

$$
 J'_N=\sum_{p\in\mathcal P_-}(1-\mathbf1_{p\mid N})\log p
                        +\sum_{p\in\mathcal P_+}\mathbf1_{p\mid N}\log p .
\tag{6}
$$

Then $J_N(B)\ge\tau Z$ implies $J'_N\ge\tau Z/2$ for large $Y$.

Choose a fixed large $R_0>D_*+\delta$ with $(D_*/R_0)^{a_0}<1/8$. By the same scaling for $\log t_p$ and its monotonicity in $p$, for large $Y$ we have $t_p\le Z^{1/4}$ for every $p>R_0Z$. On $(\delta Z,(D_*-\delta)Z)$ formula (5) gives $t_p/p\ge Z^{2\eta}$ for some fixed $\eta>0$ and all large $Y$. On $((D_*+\delta)Z,R_0Z]$ it gives $t_p/p\le Z^{-2\eta}$ after possibly reducing $\eta$. Both margins are uniform in the indicated ranges, independently of whether the sets are shortened by $Z^B$. Fix $0<\kappa<\min(\eta/2,1/(2B))$. For primes in these fixed compact ranges, $p^\kappa\le Z^{2\kappa}\le Z^\eta$ for large $Y$.

## 2. The marked positive moment and its unchanged leading cost

In the exact quantity $X_Ne^{\kappa J'_N}$ the factor at a marked low prime is $p^\kappa$ if $p\nmid N$ and $t_p$ if $p\mid N$. At a marked high prime the two cases are $1$ and $t_p p^\kappa$. In particular the factor at a low prime has the expansion

$$
 p^\kappa\bigl(1+(t_p p^{-\kappa}-1)\mathbf1_{p\mid N}\bigr).
$$

Its internal coefficient is nonnegative by $t_p/p\ge Z^{2\eta}$ and $p^\kappa\le Z^\eta$. The high and unmarked coefficients are also nonnegative. Factor the finite product of low-prime external factors outside the moment, expand all the remaining factors by squarefree divisors, and count multiples of a divisor $d$ up to $2Y$ by at most $2Y/d$. This gives

$$
 \frac1Y\sum_{Y\le N\le2Y}X_N e^{\kappa J'_N}
                         \ \le\ 2\prod_p A'_p ,
 \qquad
 A'_p=
 \begin{cases}
 p^\kappa(1-1/p)+t_p/p,&p\in\mathcal P_-,\\
 1-1/p+t_p p^\kappa/p,&p\in\mathcal P_+,\\
 A_p,&\text{otherwise}.
 \end{cases}
                                                                    \tag{7}
$$

For rigor one can first set a finite prime cutoff exceeding both $2Y$ and $Z^B$, then extend the positive upper product. At each $Y$ it converges because only finitely many factors are marked and the unmarked logarithms are $O_Y(p^{-1-a})$ as $p\to\infty$. Neither the moment (7) nor any subsequent probability statement assumes independence of prime divisibility of integers.

For marked low primes, $A_p\ge t_p/p$, so each change in the logarithm is in $[0,Z^{-\eta}]$ by $p^\kappa/(t_p/p)\le Z^{-\eta}$ and $\log(1+x)\le x$. There are $O(Z)$ such primes. For marked high primes up to $R_0Z$, the new logarithm is at most $t_p p^\kappa/p\le Z^{-\eta}$, and $A'_p\ge A_p\ge1$, so the change has total $o(Z)$ there too. For the remaining marked high primes $R_0Z<p\le Z^B$, use $t_p\le Z^{1/4}$ to obtain

$$
 \sum_{\substack{p>R_0Z\\p\in\mathcal P_+}}\log A'_p
             \ \le\ Z^{1/4}\sum_{n\le Z^B} n^{\kappa-1}
             \ll_\kappa Z^{1/4+B\kappa}=o(Z).
                                                                    \tag{8}
$$

Unmarked primes retain their contribution in (4), including all primes above $Z^B$. Thus

$$
                         \log\prod_p A'_p=(\lambda-1)D_*Z+o(Z),
                                                                    \tag{9}
$$

because all the changes were nonnegative and totaled $o(Z)$.

For integers counted on the left of (2), equations (3) and (6) give

$$
             X_N e^{\kappa J'_N}>
                       \exp[(\lambda D_*+\kappa\tau/2)Z].
$$

Apply (7) and (9), averaging even targets by the upper bound on all integers. The count is at most $Y\exp[-(D_*+\kappa\tau/2+o(1))Z]$. Dividing by the exact leading-constant asymptotic for $\#\mathcal F_Y$ gives conditional fraction at most $\exp[-(\kappa\tau/2+o(1))Z]$. For example, taking $c=\kappa\tau/4$ in both inequalities proves (2) for all sufficiently large $Y$.

For $B>1$, an immediate consequence is that among the failures, $\sum_{p\mid N,\ p\le Z^B}\log p$ is within any fixed multiple of $Z$ of $D_*Z$ up to an exponentially small conditional exceptional fraction: subtract $\sum_{p\le D_*Z}\log p=(D_*+o(1))Z$ and use (1)–(2). The stronger statement (1) compares the actual weighted prime sets and separates missing from excess mass. Both statements condition on the positive omission test alone.
