# A whole-line mismatch large-deviation law for the positive omission test

Use the actual arithmetic failure set of the [fixed-window occupation law](weak-s-type-ii-critical-prime-positive-inclusion-occupation-large-deviations.md). The probability space consists only of even integers failing that **positive** diagnostic. No result here estimates signed Type II errors or establishes an individual-prime law or a central limit theorem.

Fix $0<M<Q$, and put

$$
 v=\log\log Y,\quad \ell=\log v,\quad \lambda=Q/M,\quad
 Z=v^\lambda,\quad D=(M/(3\mathrm e))^\lambda,\quad
 K=Z/\ell^2,\quad k=(\lambda-1)/D,\quad y_p=\ell(p/Z-D).
$$

For $H>0$ set $\mathcal T_N(H)=\sum_{d\mid\operatorname{rad}N,\,d>H}3^{\omega(d)}/d$. Let $\mathcal F$ be the even integers $N\in[Y,2Y]$ with $\mathcal T_N((\log Y)^Q)>(\log Y)^{-M}$, and use the uniform probability $\mathbb P_{\mathcal F}$ there. This set is nonempty for all sufficiently large $Y$ by the preceding count.

Fix **full-collar** parameters: either $B>1$, or $B=1$ and $D<1$. Let $d\nu=dy/\lambda$ on $\mathbb R$, and define

$$
 \sigma(y)=\begin{cases}-1&y\le0,\\ 1&y>0,\end{cases}
 \qquad r(y)=(1+e^{k|y|})^{-1}.
$$

The observed mismatch measure is

$$
 \zeta_N=\frac1K\sum_{\substack{p\ \mathrm{prime}\\p\le Z^B}}
               \big|\mathbf1_{p\mid N}-\mathbf1_{p\le DZ}\big|\,\delta_{y_p}.
$$

The cutoff at $Z^B$ is part of the observation; no claim is made for the half-collar or no-collar parameter cases.

**Theorem.** In the weak topology of finite positive Borel measures on $\mathbb R$ (testing against bounded continuous functions), the laws of $\zeta_N$ under $\mathbb P_{\mathcal F}$ obey a large-deviation principle at speed $K$ with good rate

$$
 {\mathsf J}(\zeta)=
 \begin{cases}
 \displaystyle\int_{\mathbb R}H(h(y)\Vert r(y))\,d\nu(y),
   & d\zeta=h\,d\nu,\quad 0\le h\le1\ \text{a.e.},\
                            \displaystyle\int_{\mathbb R}\sigma h\,d\nu=0,\\
 +\infty,&\text{otherwise},
 \end{cases}
 \tag{1}
$$

where $H(q\Vert r)=q\log(q/r)+(1-q)\log((1-q)/(1-r))$ is Bernoulli entropy, extended by continuity at $q=0,1$. As $\zeta$ is a finite measure, $h$ in the first case is integrable. Precisely, for closed $C$ and open $G$ in this topology,

$$
 \limsup_{Y\to\infty}K^{-1}\log\mathbb P_{\mathcal F}(\zeta_N\in C)
                   \le-\inf_C {\mathsf J},
 \qquad
 \liminf_{Y\to\infty}K^{-1}\log\mathbb P_{\mathcal F}(\zeta_N\in G)
                   \ge-\inf_G {\mathsf J}.
 \tag{2}
$$

Use $\log0=-\infty$ and the empty infimum $+\infty$. There is a unique zero $r\,d\nu$ of the rate. In this whole-line measure no exterior balancing term remains: instead there is an exact balance constraint on finite-rate limiting profiles. In particular for every fixed $\epsilon>0$,

$$
 \limsup_{Y\to\infty}K^{-1}\log\mathbb P_{\mathcal F}
                          (|\langle\sigma,\zeta_N\rangle|\ge\epsilon)
                   =-\infty .
 \tag{3}
$$

This does not state that a finite-$Y$ pattern has literal zero imbalance, nor does it give the probability of an individual discrete pattern.

## 1. Exponential tightness from true prime tail marking

We first bound the mass escaping every compact $y$ interval. Use the positive Rankin parameters of the [marked prime profile, §2](weak-s-type-ii-critical-prime-positive-inclusion-marked-prime-profile.md#2-the-marked-euler-exponent-including-the-endpoint-cutoff), with its $\gamma=c=0$. In detail, put $\sigma_0=1/\lambda$, $b=(\lambda-\log D)/\lambda^2$, $a_0=1-\sigma_0$,

$$
 \beta=\sigma_0+\sigma_0/\ell+b/\ell^2,\qquad
 s=\frac{\lambda}{3\mathrm e}D^{a_0}v^{\lambda-1}\ell\,e^{-\lambda b/\ell},
 \qquad
 V_p=(1+3p^{\beta-1})^s,\quad A_p=1-1/p+V_p/p .
$$

The letter $\beta$ here denotes the divisor tilt, distinct from the sign function $\sigma(y)$. Set $T_0=(\beta Q-M)v$ and $\eta_p=\log(V_p/p)$. At any failure $\prod_{p\mid N}V_p>e^{sT_0}$. Put $u_p=V_p/(p-1+V_p)$, which is just the occupation ratio in the unmarked Euler product comparisons. We use no independent prime law for $\mathcal F$.

Fix $t>0$ and $L_0\ge0$. Multiply the Rankin product by $e^{tK\zeta_N(\{|y|>L_0\})}$, i.e. put a factor $e^t$ on each marked mismatch at $p\le Z^B$, $|y_p|>L_0$. The marked low-prime factor is $e^t[1+(V_pe^{-t}-1)\mathbf1_{p\mid N}]$ and the high one is $1+(e^tV_p-1)\mathbf1_{p\mid N}$. The divisor coefficients are nonnegative for large $Y$: on the low side $V_p\ge V(DZ)\to\infty$ by monotonicity and $\log V(DZ)\sim\lambda\ell$, and the high side is immediate. Count multiples by $2Y/d$ after expanding the divisor product. Relative to the unmarked Euler product, the marked local ratios are exactly $1+(e^t-1)(1-u_p)$ on the low side and $1+(e^t-1)u_p$ on the high side. Thus, after dividing by the [matched second-order failure count](weak-s-type-ii-critical-prime-positive-inclusion-second-order-constant.md), the conditional moment is bounded by the exponential of the sum of the log increments plus $o(K)$. Indeed $\sum_p\log A_p-sT_0=\log(|\mathcal F|/Y)+o(K)$ at these fixed parameters, and the counting factor $2$ costs only $O(1)$.

Here are the required tail estimates in this comparison. On a fixed compact interval of $p/Z$ around $D$, the marked-prime expansion gives $|\eta_p|\ge c_1|y_p|-C_1$, with the sign of $-y_p$ outside a fixed bounded $y$ interval. This follows from the bounded transition expansion in that proof and from the strictly negative derivative of $(D/x)^{a_0}$ on a compact positive interval in $x=p/Z$. The points $|y_p|\le O(1)$ can be included in the bound with a larger constant. Hence the appropriate mismatch ratio $1-u_p$ or $u_p$ is $O(e^{-c_1|y_p|})$ throughout the interval. Every unit $y$ bin there contains $O(K)$ primes uniformly, by the quantitative prime number theorem of [Johnston–Yang, Corollary 1.2, (1.5)](https://arxiv.org/pdf/2204.01980#page=2): the prime interval has length $Z/\ell$, and the endpoint errors in $\vartheta$ are $o(Z/\ell)$. The tail sum of the log increments in this physical compact interval is therefore $O_t(Ke^{-c_2 L_0})$.

Outside the compact interval but for $p\le RZ$, with $R>2D+1$ sufficiently large and fixed, $\eta_p$ is monotone and has the appropriate sign and magnitude $\gg\ell$ already at the two adjacent endpoints of the compact interval. This gives $O_t(Ze^{-c_3\ell})=o(K)$ for all such marked primes, even counting integers. For $p>RZ$, the unmarked estimate $V_p\le Z^{1/4}$ for large $R$ follows from $s\log(1+3p^{\beta-1})\le3s p^{\beta-1}$ at the left endpoint and monotonicity. Only high marks can occur, with log increment $O_t(Z^{1/4}/p)$; their sum up to $Z^B$ is $O_{t,B}(Z^{1/4}(1+\log Z))=o(K)$. The same arguments, including the central bin, apply to a marker on the total mass. Thus for some $c_2>0$ and each fixed $t>0$,

$$
 \limsup_{Y\to\infty}K^{-1}\log
       \mathbb E_{\mathcal F}e^{tK\zeta_N(\{|y|>L_0\})}
                  \le C_t e^{-c_2L_0},
 \tag{4}
$$

and the total-mass log moment has a finite limsup at $t=1$. In particular Chernoff first with arbitrary fixed $t$, then $L_0\to\infty$, gives for each fixed $\epsilon>0$

$$
 \lim_{L_0\to\infty}\limsup_{Y\to\infty}K^{-1}\log
    \mathbb P_{\mathcal F}(\zeta_N(\{|y|>L_0\})>\epsilon)=-\infty .
 \tag{5}
$$

For detail on how this gives compact exponential tightness, fix $H>0$. At $t=1$ choose a sufficiently large mass cap $M_H$ so that its exceedance costs at least $H+1$ in the negative rate. For each $j\ge1$ take $\epsilon_j\downarrow0$ and choose $L_j^0,Y_j$ via (5) so that

$$
 \mathbb P_{\mathcal F}(\zeta_N(\{|y|>L_j^0\})>\epsilon_j)
                   \le e^{-K(H+j+1)}\quad(Y\ge Y_j).
$$

Enlarge $L_j^0$ to $L_j$ if necessary so it encloses the support of every $\zeta_N$ when $Y$ lies between a fixed sufficiently large starting value and $Y_j$: the deterministic restriction $p\le Z^B$ gives a finite bound on $|y_p|$ on each such range. The tail probability is therefore zero earlier, and the eventual bound is preserved by monotonicity. The set

$$
 \mathcal C_H=\{\zeta:\zeta(\mathbb R)\le M_H,\
                        \zeta(\{|y|>L_j\})\le\epsilon_j\ \forall j\}
$$

is weakly closed, as the exterior sets are open and their masses are lower semicontinuous. Its measures have bounded mass and are uniformly tight, so it is weakly compact by the weak compactness criterion for finite measures on $\mathbb R$. Taking a union of the cap and all tail exceptions, the geometric sum over $j$ gives

$$
    \limsup_{Y\to\infty}K^{-1}\log
              \mathbb P_{\mathcal F}(\zeta_N\notin\mathcal C_H)\le-H .
 \tag{6}
$$

In particular (5) has been promoted to a compactness statement uniform in the initial ranges of $Y$, not merely a bound at each fixed $L_0$.

## 2. Compact mismatch fields and the global dual

Let $\phi$ be any real bounded compactly supported Riemann-integrable field. The prime cutoff $Z^B$ includes its entire support for all sufficiently large $Y$, by the full-collar hypothesis. On low primes a mismatch is $1-\mathbf1_{p\mid N}$, and on high primes it is $\mathbf1_{p\mid N}$. Consequently the exponent $K\langle\phi,\zeta_N\rangle$ is a deterministic low-prime exponent $\sum_{y_p\le0}\phi(y_p)$ plus the marked occupation exponent $\sum_p \sigma(y_p)\phi(y_p)\mathbf1_{p\mid N}$. The deterministic exponent divided by $K$ tends to $\int_{y\le0}\phi\,d\nu$, by the same PNT on fixed bounded $y$ intervals. The field $\sigma\phi$ is permitted in the [constrained collar log-Laplace theorem](weak-s-type-ii-critical-prime-positive-inclusion-collar-field-functional.md).

Put $L_r(z)=\log(1-r+r e^z)$, with $r=r(y)$ at each $y$. The resulting limiting log-Laplace exponent is

$$
 \Lambda_{\rm mis}(\phi)
     =\lim_{Y\to\infty}K^{-1}
                    \log\mathbb E_{\mathcal F}e^{K\langle\phi,\zeta_N\rangle}
     =\inf_{\alpha\in\mathbb R}\int_{\mathbb R}
                          L_{r(y)}(\phi(y)+\alpha\sigma(y))\,d\nu(y).
 \tag{7}
$$

To check the rewrite, let $u(y)=(1+e^{ky})^{-1}$. After subtracting the unmarked soft constant, the occupation limit is the infimum of $\int [\log(1-u+u e^{\alpha+\sigma\phi})-\alpha u]d\nu$ (the change from the sharp step to $u$ integrates to zero, as in the fixed-window proof). On the low side $r=1-u$, and adding $\phi$ from the deterministic term changes the integrand to $L_r(\phi-\alpha)+\alpha r$. On the high side $r=u$ the integrand is $L_r(\phi+\alpha)-\alpha r$. The linear terms integrate to zero since $r$ is even. The two rearrangements preserve integrability: outside compact support their residuals decay exponentially. The value of $\sigma$ at zero is chosen to preserve the literal prime flip; it does not affect integrals.

We compute the dual of (7) over continuous compactly supported fields. First let $\zeta=h\,d\nu$ with $0\le h\le1$ and $h$ integrable. For each fixed $\alpha$,

$$
 \sup_{\phi\in C_c(\mathbb R)}
 \left\{\int_{\mathbb R}\phi h\,d\nu
                  -\int_{\mathbb R} L_r(\phi+\alpha\sigma)\,d\nu\right\}
      =\int_{\mathbb R}H(h\Vert r)\,d\nu
                      -\alpha\int_{\mathbb R}\sigma h\,d\nu .
 \tag{8}
$$

The upper bound is pointwise Bernoulli Fenchel inequality. For the lower bound, first on $[-A,A]$ choose the bounded measurable field $\phi=j-\alpha\sigma$, where $j$ is the pointwise optimizer of $jh-L_r(j)$ clipped to $[-C,C]$; at $h=0,1$ use $j=-C,C$ respectively. Put $\phi=0$ off the compact interval. Approximate this field in $L^1(d\nu)$ by continuous fields supported in $[-A-1,A+1]$; both terms in the payoff are $L^1$-Lipschitz because $h\le1$ and $0\le L_r'\le1$. Send $C\to\infty$. The clipped payoff is nonnegative and increases to entropy, so monotone convergence gives the compact-interval integral. The off-interval term is $-\int_{|y|>A}L_r(\alpha\sigma)\,d\nu$ and tends to zero as $A\to\infty$, since at fixed $\alpha$ it is absolutely bounded by a constant times $r$. Also $\int_{|y|>A}h\to0$. This establishes (8), including if the whole-line entropy is infinite. Taking the supremum over $\alpha$ enforces precisely the balance condition in (1). The order of the two suprema is immaterial because the negative of the infimum in (7) is a supremum.

If $\zeta$ is not dominated by $\nu$ then some nonnegative continuous compact field $\phi$ has $\int\phi\,d\zeta>\int\phi\,d\nu$, by local regularity of the measures (one can first restrict to a bounded interval). With $\alpha=0$ in (7), for $t\ge0$ we have $\Lambda_{\rm mis}(t\phi)\le t\int\phi\,d\nu$. The continuous compact dual is thus infinite in this case. It follows on the full space that

$$
 {\mathsf J}(\zeta)=\sup_{\phi\in C_c(\mathbb R)}
                       (\langle\phi,\zeta\rangle-\Lambda_{\rm mis}(\phi)).
 \tag{9}
$$

In particular the proposed rate is weakly lower semicontinuous, even though the balance test uses a discontinuous sign. It is a good rate: for any finite-entropy profile of rate at most $H_0$, any Borel $E$ and any $t>0$, Fenchel on $E$ gives

$$
 t\zeta(E)\le H_0+\int_E L_r(t)\,d\nu
                       \le H_0+(e^t-1)\int_E r\,d\nu .
$$

At $E=\mathbb R$, $t=1$ this bounds the mass; at $E=\{|y|>L_0\}$ choosing $t$ large and then $L_0$ large gives uniform tightness. Thus the closed sublevels are weakly compact. Nonnegativity and the unique zero $r\,d\nu$ follow from pointwise entropy and the evenness of $r$.

## 3. Closed-set upper bound

Fix a weakly closed set $C$ and a finite $s<\inf_C{\mathsf J}$. Choose $H>\max(s,0)$ in (6). At each $\zeta\in C\cap\mathcal C_H$, select by (9) a continuous compact field $\phi$ such that $\langle\phi,\zeta\rangle-\Lambda_{\rm mis}(\phi)>s$. These strict inequalities define weakly open neighborhoods; finitely many cover the compact $C\cap\mathcal C_H$. For each one (7) and the exponential Markov inequality give upper scaled log probability at most $-s$. The finite union has the same limsup, and its complement outside $\mathcal C_H$ is bounded by (6). An empty compact intersection requires no neighborhoods. Letting $s$ tend to the infimum, or become arbitrarily large when the infimum is infinite, proves the upper bound in (2).

## 4. Matching lower bounds, first at balanced interior profiles

Start with a balanced density $h_*$ that equals $r$ off a compact interval, and is an interior step density on that interval, meaning it is uniformly between $0$ and $1$ there. Define the fixed bounded compactly supported Riemann-integrable field

$$
       \phi(y)=\log\frac{h_*(y)}{1-h_*(y)}
                       -\log\frac{r(y)}{1-r(y)}
$$

on that interval and zero off it. In (7) this field produces the profile $h_*$ at $\alpha=0$ and that is the unique optimizer: the derivative in $\alpha$ is the integrated signed tilted occupation, here zero by balance, and the second derivative is strictly positive. Derivatives have integrable tails for bounded $\alpha$ because $r$ decays exponentially and the field is compactly supported. Pointwise Fenchel equality now gives

$$
     {\mathsf J}(h_*\,d\nu)
                      =\langle\phi,h_*\,d\nu\rangle-\Lambda_{\rm mis}(\phi).
 \tag{10}
$$

For any fixed bounded compactly supported Riemann-integrable $\psi$, the derivative at $t=0$ of $\Lambda_{\rm mis}(\phi+t\psi)$ is $\int \psi h_*\,d\nu$. Indeed the strictly positive scalar second derivative and differentiation under the integral give a differentiable minimizing $\alpha(t)$ near zero by the implicit function theorem; its effect in the derivative of the objective vanishes by stationarity. This differentiates only the limiting functional, not the finite-size moments.

Use on the actual failure set the probability tilt with density

$$
     \frac{d\mathbb P_{\phi,Y}}{d\mathbb P_{\mathcal F}}
       =\exp(K\langle\phi,\zeta_N\rangle-K\Lambda_{{\rm mis},Y}(\phi)),
       \qquad
       \Lambda_{{\rm mis},Y}(\phi)
        =K^{-1}\log\mathbb E_{\mathcal F}e^{K\langle\phi,\zeta_N\rangle}.
$$

Its log moments in direction $\psi$ converge by (7) to $\Lambda_{\rm mis}(\phi+t\psi)-\Lambda_{\rm mis}(\phi)$. The directional derivative and Chernoff at small fixed parameters of both signs show that $\langle\psi,\zeta_N\rangle$ concentrates at $\int \psi h_*\,d\nu$, with exponentially small probability at any fixed positive deviation tolerance. This applies also to $\psi=\phi$.

For weak neighborhoods on the whole line the test functions may be bounded continuous rather than compact. This causes no tail loss under the tilted law. The tilting density is bounded above by $\exp(O_\phi(K))$: the mass on the fixed compact support of $\phi$ is bounded deterministically by its prime count divided by $K$, and the normalizer exponent converges to a finite limit. By (5), for any fixed tolerance the mass outside a sufficiently large compact interval therefore exceeds that tolerance with probability $o(1)$ under the tilted law as well. The trial measure $h_*\,d\nu$ is finite so its own tail mass tends to zero. For any finite family of bounded continuous tests and positive tolerances, multiply the tests by a continuous compact cutoff equal to one on a sufficiently large interval. The discarded integrals are bounded by their sup norms times these tail masses. Compact-field concentration then gives the required inequalities for the original tests simultaneously with probability $1-o(1)$.

Thus if $G$ is a weakly open set containing $h_*\,d\nu$, choose a finite such neighborhood in $G$. Its inequalities and $\langle\phi,\zeta_N\rangle\le\langle\phi,h_*\,d\nu\rangle+\eta$ hold jointly with probability $1-o(1)$ under the tilted law, for each fixed $\eta>0$. Undo the tilt on that event to obtain

$$
 \liminf_{Y\to\infty}K^{-1}\log\mathbb P_{\mathcal F}(\zeta_N\in G)
     \ge \Lambda_{\rm mis}(\phi)-\langle\phi,h_*\,d\nu\rangle-\eta.
$$

Let $\eta\downarrow0$ and use (10).

To extend this lower bound to any finite-rate profile $h$, the approximations must preserve the balance constraint. First mix with the reference profile: $h_\epsilon=(1-\epsilon)h+\epsilon r$, with $0<\epsilon<1$. It is balanced, tends to $h$ in $L^1(d\nu)$ as $\epsilon\downarrow0$, and its entropy tends to that of $h$ by convexity and Fatou's inequality (its entropy is at most $(1-\epsilon)$ times the original). At fixed $\epsilon$, replace $h_\epsilon$ outside $[-A,A]$ by $r$, where $A\ge3$. The resulting imbalance $d_A$ tends to zero as $A\to\infty$, since both densities are integrable. Subtract $d_A/\nu([1,2])$ from the resulting profile on $[1,2]$ only. This restores exact balance, since that patch is on the positive side. There the original mixture is uniformly separated from $0$ and $1$, so the change stays inside $[0,1]$ and strictly interior for large $A$. On all of $[-A,A]$ the resulting profile is interior with a positive bound allowed to depend on $A,\epsilon$. The patch correction tends to zero in $L^1$ and entropy: the reference $r$ there is bounded away from $0,1$ and the entropy integrand is uniformly continuous in the density. The rest of the removed entropy tail tends to zero by integrability. Thus these balanced truncated profiles converge in $L^1$ and entropy to $h_\epsilon$.

Finally for each such fixed compact interval, average its profile on successively finer interval partitions which include $0$ as a dividing point. Preserve the same $r$ outside the compact interval. This keeps the mass of each side, hence balance, exactly and preserves the interior bounds on the compact interval. Interval averaging converges in $L^1$ by density of continuous functions and the $L^1$ contraction of averaging. Entropy converges because on the compact interval the reference stays bounded away from $0,1$ and binary entropy is uniformly continuous. The resulting step profiles have the lower bound just proved. Successively taking these approximations, any weakly open set containing a finite-rate measure also contains trial measures with rate arbitrarily close to its rate. Taking the infimum proves the open-set lower bound of (2).

To prove (3), choose $\delta>0$ small. The deterministic bound on $\zeta_N([-\delta,\delta])$ is $2\delta/\lambda+o(1)$ by the prime counting estimate. The corresponding bound on every finite-rate $\zeta$ is $2\delta/\lambda$ by domination by $\nu$. Replace $\sigma$ by a bounded continuous function equal to it off $[-\delta,\delta]$ and with absolute value at most one. Taking $\delta$ small enough, both replacement errors are less than $\epsilon/4$ for large $Y$. The event in (3) then implies a weakly closed event in which the absolute integral against that continuous function is at least $3\epsilon/4$. No finite-rate profile lies there by balance. The closed-set bound in (2) yields (3), completing the result for the stated positive diagnostic.
