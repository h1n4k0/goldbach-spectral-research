# A vanishing first correction to positive-test rarity and finer prime occupancy

This is a statement about the **positive omission diagnostic**, not about the signed Type II contribution or the error of an energy transport. No hypothesis on zeros is used. It sharpens [quantitative occupancy](weak-s-type-ii-critical-prime-positive-inclusion-quantitative-occupancy.md) and retains the threshold of the earlier [leading-constant law](weak-s-type-ii-critical-prime-positive-inclusion-tail-leading-constant.md).

Fix $0<M<Q$ and $B\ge1$. Write

$$
v=\log\log Y,\qquad \ell=\log v,\qquad \lambda=Q/M,\qquad
\sigma_0=1/\lambda,\qquad a_0=1-\sigma_0,\qquad Z=v^\lambda,\qquad
D_*=(M/(3\mathrm e))^\lambda .
$$

Let $H=(\log Y)^Q$ and define

$$
\mathcal T_N(H)=\sum_{\substack{r\mid\operatorname{rad}N\\r>H}}\frac{3^{\omega(r)}}r,
\qquad
\mathcal F_Y=\{N\in[Y,2Y]\cap 2\mathbb Z:\mathcal T_N(H)>(\log Y)^{-M}\},
\qquad E=|\mathcal F_Y|.
$$

The disagreement on primes up to $Z^B$ is

$$
J_N(B)=\sum_{p\le Z^B}
   \big|\mathbf1_{p\mid N}-\mathbf1_{p\le D_*Z}\big|\log p.
$$

**Theorem.** As $Y\to\infty$,

$$
\log(E/Y)=-D_*Z+O_{Q,M}(Z/\ell^2).
\tag{1}
$$

There exist $K,c,\tau_0>0$, depending only on $Q,M,B$, such that uniformly for $K/\ell\le\tau\le \tau_0$ and sufficiently large $Y$,

$$
\frac{\#\{N\in\mathcal F_Y:J_N(B)\ge\tau Z\}}{E}
   \le \exp(-c\tau^2Z).
\tag{2}
$$

Thus there is no $Z/\ell$ correction in the logarithm of the positive failure count, and conditional weighted occupancy can be controlled at a radius of order $Z/\ell$. This is an aggregate statement, not one about every individual prime. Neither (1) nor (2) estimates the number of failures of the actual signed approximation or proves a signed shell estimate.

## 1. The upper count and the local Euler transition

The prime input is $\vartheta(x)=x+O(xe^{-b\sqrt{\log x}})$ with some absolute $b>0$, from [Johnston–Yang, Corollary 1.2, (1.5)](https://arxiv.org/pdf/2204.01980#page=2), after absorbing a power of $\log x$. Write

$$
\sigma=\sigma_0+\frac{\sigma_0}{\ell},\quad a=1-\sigma,\quad
s=\frac{\lambda}{3\mathrm e}D_*^{a_0}v^{\lambda-1}\ell,\quad
t_p=(1+3p^{-a})^s,\quad A_p=1-\frac1p+\frac{t_p}{p}.
$$

In this section and in §3 these are fixed upper-tilt parameters, and $Y$ is large enough that $0<\sigma<1$. For $r>H$, the factor $(r/H)^\sigma$ is greater than one. Thus at any failure

$$
\prod_{p\mid N}(1+3p^{-a})>H^\sigma e^{-Mv},
\qquad
X_N:=\prod_{p\mid N}t_p>e^{\lambda D_* Z}.
\tag{3}
$$

Indeed $\sigma Q-M=M/\ell$, and $s Mv/\ell=\lambda D_* Z$. The true divisor expansion of $X_N$ has nonnegative coefficients. Since at most $2Y/d$ integers in $[Y,2Y]$ are multiples of a positive integer $d$,

$$
\frac1Y\sum_{Y\le N\le2Y} X_N
 \le 2\prod_p A_p .
\tag{4}
$$

Here and below a sum without the even restriction is over all integers, for an upper bound only. One can first expand over $p\le2Y$ and then enlarge the positive majorant to the convergent full product. No statistical independence of prime divisibility of integers is invoked.

We will prove

$$
\sum_p\log A_p=(\lambda-1)D_*Z+O_{Q,M}(Z/\ell^2).
\tag{5}
$$

Fix a constant $K_0>6/\sigma_0$, put $\delta_0=\ell^{-K_0}$, and fix a sufficiently large constant $R>\max(2D_*,1)$, also to be used in §3. On $p\le\delta_0Z$, use $\log A_p\le\log t_p\le3s p^{-a}$. Quantitative PNT and partial summation give $\sum_{p\le x}p^{-a}\ll x^\sigma/\log x$ uniformly for $\sigma$ in a compact subset of $(0,1)$ and $x$ sufficiently large. For example, this follows by splitting at $\sqrt x$, using $\pi(t)\ll t/\log t$ on $[\sqrt x,x]$ and summing on dyadic pieces below $\sqrt x$. Thus the small part is $O(Z\delta_0^{\sigma_0/2})=O(Z/\ell^3)$. For $p>RZ$ we have $3s p^{-a}\le (\log Z)/4$ for fixed $R$ large enough: at $p=RZ$ the ratio to $\log Z$ tends to $(D_*/R)^{a_0}$. Consequently $t_p\le Z^{1/4}$ and $t_p-1\le 3s Z^{1/4}p^{-a}$. Comparison with the integer tail gives $\sum_{p>RZ}\log A_p\ll Z^{1/4}\ell$.

For $\delta_0 Z<p\le RZ$ put $x=p/Z$, $h(x)=(D_*/x)^{a_0}$, $u=\sigma_0\log x/\ell$, and $\eta_p=\log(t_p/p)$. The linearization $\log t_p=3s p^{-a}+O(s p^{-2a})$ is uniform. Here $s p^{-2a}\ll v^{-(\lambda-1)}\ell^{C_0}$ for a fixed $C_0$. Hence this error is $o(\ell^{-j})$ uniformly for every fixed $j>0$. Since $\log p=\lambda\ell(1+u)$, the normalization of $s$ gives

$$
\frac{\eta_p}{\log p}=h(x)\frac{e^u}{1+u}-1+O\left(\frac{s p^{-2a}}{\log p}\right)
 =h(x)-1+O\left(\frac{h(x)\log^2 x}{\ell^2}
                 +\frac{s p^{-2a}}{\log p}\right).
\tag{6}
$$

We used $|u|=O(\log\ell/\ell)$ and $e^u/(1+u)=1+O(u^2)$. In particular the first-order term in $u$ vanishes.

The positive-part function is $1$-Lipschitz. The error in replacing $(\eta_p)_+$ by $(h(x)-1)_+\log p$, summed over the middle range, is $O(Z/\ell^2)$. For the term with $\log^2 x$, partition small $x$ into ratio-two intervals. The bound $\vartheta(t)\ll t$ on an interval with $x\asymp 2^{-j}$ yields a contribution at most $C Z(1+j^2)2^{-j\sigma_0}/\ell^2$, and these majorants are summable. Bounded $x$ away from zero is immediate from the same bound. The uniform $s p^{-2a}$ error summed over at most $RZ$ integers is negligible compared with $Z/\ell^2$.

Here an $O(1)$ estimate for the difference between $\log A_p$ and $(\eta_p)_+$ at every prime would be too large. Instead,

$$
\big|\log A_p-(\eta_p)_+\big|\le e^{-|\eta_p|}+O(1/p),
\tag{7}
$$

by first comparing $\log(1+e^{\eta_p})$ with $(\eta_p)_+$, and then replacing $1$ by $1-1/p$ in its argument. Fix the compact interval $\mathcal I=[D_*/2,3D_*/2]$. On $\mathcal I$, (6) and the strict negative derivative of $h$ show

$$
|\eta_p|\ge c_0\ell |x-D_*|-C_1/\ell ,
\tag{8}
$$

for fixed $c_0,C_1>0$. At the two ends of $\mathcal I$ the signs are respectively positive and negative for large $Y$. Since $\eta_p$ is decreasing in the positive real variable $p$, outside $\mathcal I$ its absolute value is $\gg\ell$ in the middle range. Even allowing all the integer points there this contributes $O(Ze^{-c_1\ell})$ to the first error in (7). On either side of $D_*$ in $\mathcal I$, partition into bins of length $1/\ell$ in the $x$ variable, with the last bin possibly shortened. Each bin contains $O(Z/\ell^2)$ primes: the endpoint $\vartheta$ bound gives weighted mass $O(Z/\ell+Ze^{-b_1\sqrt{\ell}})$, and $\log p\asymp\ell$ there. In the bin at distance $j/\ell$ the exponential in (7) is $\ll e^{-c_0j}$. Hence its sum is also $O(Z/\ell^2)$. Finally the sum of $1/p$ over the middle range is $O(1+\log\ell)$ even over integers.

It remains to evaluate the main sum

$$
\sum_{\delta_0 Z<p\le R Z}(h(p/Z)-1)_+\log p.
$$

Apply Stieltjes partial summation against $\vartheta(t)-t$ on $[\delta_0 Z,RZ]$. The boundary values and total variation of the weight are $O(\delta_0^{-a_0})$. On this interval $\sup_t|\vartheta(t)-t|\ll Ze^{-b_2\sqrt{\ell}}$. Their product is $o(Z/\ell^2)$. The missing integral from $0$ to $\delta_0$ costs $O(Z\delta_0^{\sigma_0})$. Thus the main sum is

$$
Z\int_0^{D_*}\big((D_*/x)^{a_0}-1\big)\,dx+O(Z/\ell^2)
  =(\lambda-1)D_*Z+O(Z/\ell^2),
$$

which proves (5). Combining (3)–(5) gives the upper bound in (1).

## 2. A true lower family with the strict inequality

In this section the lower tilt $\sigma$ will be chosen anew. Let $D=D_*+A/\ell^2$ for a positive fixed constant $A$ to be specified, $z=DZ$, and $P_z=\prod_{p\le z}p$. In the finite space of divisors $r\mid P_z$, give $r$ weight $3^{\omega(r)}r^{\sigma-1}/W_z(\sigma)$ with

$$
W_z(\sigma)=\prod_{p\le z}(1+3p^{\sigma-1}).
$$

In this auxiliary space the prime selections are independent with probabilities $3p^{\sigma-1}/(1+3p^{\sigma-1})$. Denote the mean of $\log r$ by $m_z(\sigma)$.

For $\sigma$ in a fixed compact subset of $(0,1)$ around $\sigma_0$, quantitative PNT and endpoint integration give

$$
m_z(\sigma)=\frac{3z^\sigma}{\sigma}
     \big(1+O(e^{-b_3\sqrt{\log z}})\big),\qquad
\log W_z(\sigma)=\frac{m_z(\sigma)}{\log z}
      \left(1+\frac1{\sigma\log z}+O((\log z)^{-2})\right).
\tag{9}
$$

For completeness the two nonlinear corrections are $O(\sum_{p\le z} p^{2(\sigma-1)}\log p)$ and $O(\sum_{p\le z}p^{2(\sigma-1)})$, respectively, by comparing the selection probability and the product logarithm with $3p^{\sigma-1}$. Split at $\sqrt z$. The first part is bounded using $\sum_{p\le\sqrt z}p^{\sigma-1}\log p\ll z^{\sigma/2}$ and the second costs the extra factor $z^{-(1-\sigma)/2}$ against the leading bound $O(z^\sigma)$. This controls both errors by a power saving uniformly and applies also to the errors without $\log p$. The prime sums with linear weights are $3\int_2^z t^{\sigma-1}\,dt$ and $3\int_2^z t^{\sigma-1}\,dt/\log t$, up to $O(z^\sigma e^{-b_4\sqrt{\log z}})$ by partial summation: below $\sqrt z$ the terms are power smaller, and above it one uses the uniform relative bound for $\vartheta(t)-t$. Twice integrating the latter integral by parts gives $3z^\sigma/(\sigma\log z)$ times $1+1/(\sigma\log z)+O((\log z)^{-2})$; the remainder integral with $(\log t)^{-3}$ obeys this bound by the split at $\sqrt z$. This proves (9).

Put $\Delta=v/\ell^4$ and tune the exact mean to

$$
m_z(\sigma)=Qv+\Delta/2.
\tag{10}
$$

To see this exists with uniform control, allow $D$ in any fixed closed positive interval around $D_*$, and put

$$
u_D=\lambda^{-1}\log\left(\frac{M}{3D^{\sigma_0}}\right),\qquad
\sigma=\sigma_0+w/\ell .
$$

The continuous mean is strictly increasing. By (9), taking $w=u_D-1$ and $u_D+1$ brackets (10) uniformly for large $Y$. On the resulting bounded $w$ interval,

$$
\log\left(\frac{m_z(\sigma)}{Qv}\right)
  =\lambda(w-u_D)+\frac{w(\log D-\lambda)}{\ell}+O_{Q,M}(\ell^{-2}).
$$

The left side is $O(\ell^{-4})$ at (10). First $w=u_D+O(\ell^{-1})$, and substitution gives

$$
w=u_D-\frac{u_D(\log D-\lambda)}{\lambda\ell}+O_{Q,M}(\ell^{-2}).
\tag{11}
$$

Also $\log z=\lambda\ell+\log D$ changes (9) and (10) to

$$
\log W_z(\sigma)=\frac{Mv}{\ell}
   \left(1+\frac{\lambda-\log D}{\lambda\ell}+O_{Q,M}(\ell^{-2})\right).
\tag{12}
$$

All constants in (9)–(12) can be fixed on the same interval for $D$, independently of the eventual fixed $A$.

Independence in the finite divisor space gives $\operatorname{Var}(\log r)\le (\log z)m_z(\sigma)\ll v\ell$, since each Bernoulli variance is at most its probability. Chebyshev's inequality at the exact tuned center (10) yields mass $1-O(\ell^9/v)$ in the interval $Qv<\log r\le Qv+\Delta$: both excluded tails are at least $\Delta/2$ from the mean, including equality at the lower truncation. For any $N$ divisible by $P_z$, we can lower bound its positive tail by these divisors, un-tilting with the factor $r^{-\sigma}\ge e^{-\sigma(Qv+\Delta)}$. Thus

$$
\log\mathcal T_N(H)\ge -Mv+(M-Q u_D)\frac{v}{\ell}
  +(M-Q u_D)\frac{\lambda-\log D}{\lambda}\frac{v}{\ell^2}
  -C_2\frac{v}{\ell^3}.
\tag{13}
$$

Indeed substitute (11)–(12) in $\log W_z-\sigma(Qv+\Delta)+\log(1-O(\ell^9/v))$; the $\Delta$ and log-mass losses are both $o(v/\ell^3)$. The equality $u_{D_*}=\sigma_0$ is the cancellation in the lower estimate. More explicitly,

$$
 M-Q u_D=\frac{M}{\lambda}\log(D/D_*).
$$

For $D=D_*+A/\ell^2$ this is positive, $\gg_{Q,M} A/\ell^2$ for sufficiently large $Y$, and the next term in (13) is relatively $O(1/\ell)$. Since $C_2$ does not depend on any fixed $A$, a sufficiently large fixed $A$ gives a **strict** positive margin above $-Mv$ in (13). Thus all multiples of $P_z$ in $[Y,2Y]$ fail the positive test. They are even, and the prime input gives

$$
\log P_z=\vartheta(z)=D_*Z+O_{Q,M}(Z/\ell^2).
$$

The interval contains $Y/P_z+O(1)$ such multiples, and $P_z=Y^{o(1)}$. This gives the lower bound in (1).

## 3. Prime disagreement at the finer shrinking radius

Return to the fixed parameters of §1. Let $\tau\ge K/\ell$, where $K\ge1$ is to be increased below. Choose a sufficiently small fixed $\tau_0>0$, depending only on $Q,M,B$, and suppose $\tau\le\tau_0$. Ignore $p\le\delta Z$ and $|p/Z-D_*|\le\delta$, with $\delta=\tau/16$, and write $J'_N$ for $J_N(B)$ on the retained primes. By the prime input, the combined possible log weight of the ignored primes is at most $3\delta Z+o(\tau Z)$, uniformly over this range. In fact $\vartheta(\delta Z)=\delta Z+o(\delta Z)$ since $\delta Z\gg Z/\ell$, and the two endpoints of the interval at $D_*Z$ give the mass at most $2\delta Z+O(Ze^{-b_5\sqrt{\ell}}+\ell)$, including any endpoints. Thus $J_N(B)\ge \tau Z$ implies $J'_N\ge \tau Z/2$.

Set $\kappa=k_0\tau$ with a sufficiently small fixed $k_0>0$. Mark a retained prime on the low side $p/Z<D_*-\delta$ by $p^\kappa$ when $p\nmid N$, and one on the high side $p/Z>D_*+\delta$ by $p^\kappa$ when $p\mid N$. The retained primes are restricted to $p\le Z^B$. The product $X_N e^{\kappa J'_N}$ has a nonnegative divisor expansion. On the low side its factor is

$$
p^\kappa\big[1+(t_pp^{-\kappa}-1)\mathbf1_{p\mid N}\big],
$$

and $t_pp^{-\kappa}\ge1$: on $\mathcal I$ we have $\eta_p>0$ below $D_*-\delta$ by (6), since the signed leading term there dominates $C_1/\ell$ for large $Y$ uniformly with $\ell\delta\ge K/16$. Below $\mathcal I$ use monotonicity. In particular $t_p>p$ and $\kappa<1$ suffice. The high side has factor $1+(t_pp^\kappa-1)\mathbf1_{p\mid N}$. As before, count genuine multiples and enlarge the unmarked product. We obtain

$$
\frac1Y\sum_{Y\le N\le2Y} X_N e^{\kappa J'_N}\le 2\prod_p A'_p,
\quad
A'_p=
\begin{cases}
p^\kappa(1-1/p)+t_p/p &\text{on the marked low side},\\
1-1/p+t_pp^\kappa/p &\text{on the marked high side},\\
A_p &\text{otherwise}.
\end{cases}
\tag{14}
$$

We claim $\sum_p\log(A'_p/A_p)=O_{Q,M,B}(Z/\ell^2)$ uniformly. On the respective marked sides the log increment is at most $(p^\kappa-1)e^{-\eta_p}$ or $(p^\kappa-1)e^{\eta_p}$: use $A_p\ge e^{\eta_p}$ on the low side and $A_p\ge1$ on the high side. On $\mathcal I$ the correct signs hold by (6) and the argument above, also on the high side. Further $\kappa\log p\le c_0\ell|x-D_*|/2$ there for sufficiently small $k_0$, since $|x-D_*|\ge\tau/16$ and $\log p\ll\ell$. Using (8) the increment is therefore $\ll \exp(-c_0\ell|x-D_*|/2)$. Summing over the same bins used in (7) gives $O(Z/\ell^2)$, even when the ignored collar is only of order $1/\ell$.

For $p\le RZ$ outside $\mathcal I$, monotonicity and the signs at its ends imply $|\eta_p|\ge c_3\ell$ on the correct side, so by decreasing $k_0$ or $\tau_0$ the increment is $O(e^{-c_3\ell/2})$ even at the larger $p$ in this range. For $RZ<p\le Z^B$, only the high side is possible; $t_p\le Z^{1/4}$ and $A_p\ge1$ give the majorant $Z^{1/4}p^{\kappa-1}$. Hence its full sum is at most $O(Z^{1/4+B\kappa}(1+B\log Z))$ by the integer harmonic sum, with no division by $\kappa$. Take $B k_0\tau_0\le1/4$. This completes the claimed uniform bound.

At a failure counted in the numerator of (2), the product on the left of (14) exceeds $\exp(\lambda D_*Z+\kappa\tau Z/2)$ by (3). Apply (14), (5) and the increment bound to count such integers, and divide by the lower bound in (1). The fraction is at most

$$
\exp\left(-\tfrac12 k_0\tau^2Z+C_3 Z/\ell^2\right)
$$

with $C_3$ independent of $\tau$ and $K\ge1$. Taking $K$ sufficiently large gives (2), for instance with $c=k_0/4$. Throughout the only probability on actual targets in (2) is the ratio of counts; the Euler expansions inserted no probabilistic model for the integers.
