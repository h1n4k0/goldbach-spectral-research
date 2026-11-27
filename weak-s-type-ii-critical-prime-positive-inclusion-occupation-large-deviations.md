# A fixed-window occupation large-deviation law for the positive omission test

Use the actual even-target arithmetic failure set of the [constrained collar log-Laplace theorem](weak-s-type-ii-critical-prime-positive-inclusion-collar-field-functional.md). This result concerns only the **positive omission diagnostic**. It neither estimates signed Type II errors nor establishes an individual-prime conditional law or a central limit theorem.

Fix $0<M<Q$, and write

$$
 v=\log\log Y,\quad \ell=\log v,\quad \lambda=Q/M,\quad
 Z=v^\lambda,\quad D=(M/(3\mathrm e))^\lambda,\quad
 K=Z/\ell^2,\quad k=(\lambda-1)/D,\quad y_p=\ell(p/Z-D).
$$

The set $\mathcal F$ consists of the even integers $N\in[Y,2Y]$ with

$$
 \mathcal T_N((\log Y)^Q)>(\log Y)^{-M},\qquad
 \mathcal T_N(H)=\sum_{\substack{d\mid\operatorname{rad}N\\d>H}}
                       \frac{3^{\omega(d)}}{d}.
$$

Let $\mathbb P_{\mathcal F}$ be uniform probability on $\mathcal F$, which is nonempty for all sufficiently large $Y$ by the preceding counting theorem.

Put $u(y)=(1+e^{ky})^{-1}$ and $d\nu=dy/\lambda$ on $\mathbb R$. Fix a compact interval $I=[a,b]$ of positive length, independent of $Y$, and define

$$
 \mu_N=K^{-1}\sum_{\substack{p\ \mathrm{prime}\\y_p\in I}}
                          \mathbf1_{p\mid N}\,\delta_{y_p}.
$$

We use the weak topology of finite positive Borel measures on $I$, that is, the topology of integration against continuous real functions on $I$. Define

$$
 \begin{split}
 H(q\Vert u)&=q\log(q/u)+(1-q)\log((1-q)/(1-u)),\\
 R_{\rm out}(\alpha)&=\int_{\mathbb R\setminus I}
       \big[\log(1-u(y)+u(y)e^\alpha)-\alpha u(y)\big]\,d\nu(y),\\
 R_{\rm out}^*(d)&=\sup_{\alpha\in\mathbb R}
                              \big(\alpha d-R_{\rm out}(\alpha)\big).
 \end{split}
 \tag{1}
$$

The entropy is extended by continuity at $q=0,1$.

**Theorem.** Unconditionally, $\mu_N$ under $\mathbb P_{\mathcal F}$ obeys a large-deviation principle at speed $K$ with good rate function

$$
 {\mathsf I}_I(\mu)=
 \begin{cases}
 \displaystyle\int_I H(g(y)\Vert u(y))\,d\nu(y)
      +R_{\rm out}^*\!\left(-\int_I(g-u)\,d\nu\right),
                      & d\mu=g\,d\nu,\quad 0\le g\le1\ \text{a.e.},\\
 +\infty,             & \text{otherwise}.
 \end{cases}
 \tag{2}
$$

Precisely, for every weakly closed set $C$ and weakly open set $G$ of finite positive measures on $I$,

$$
 \begin{split}
 \limsup_{Y\to\infty}K^{-1}\log\mathbb P_{\mathcal F}(\mu_N\in C)
       &\le-\inf_{\mu\in C}{\mathsf I}_I(\mu),\\
 \liminf_{Y\to\infty}K^{-1}\log\mathbb P_{\mathcal F}(\mu_N\in G)
       &\ge-\inf_{\mu\in G}{\mathsf I}_I(\mu).
 \end{split}
 \tag{3}
$$

Here $\log0=-\infty$ and the infimum of the empty set is $+\infty$. The unique zero of the rate is $u\,d\nu$ restricted to $I$.

The second term in (2) is the outside balancing cost. For each signed imbalance $d$, it equals the minimum of $\int_{\mathbb R\setminus I}H(h(y)\Vert u(y))\,d\nu(y)$ over measurable $0\le h\le1$ with $h-u$ integrable there and $\int_{\mathbb R\setminus I}(h-u)\,d\nu=d$. The minimizing profile is $h(y)=(1+e^{ky-\alpha})^{-1}$ for the unique $\alpha$ giving that imbalance. This variational interpretation does not assert independence of the actual prime-divisibility indicators.

## 1. The conditional Laplace functional in reservoir form

Write $L_y(z)=\log(1-u(y)+u(y)e^z)$ and $u_\alpha(y)=(1+e^{ky-\alpha})^{-1}$. The function $L_y(\alpha)-\alpha u(y)$ and its derivatives in $\alpha$ have integrable exponentially decaying tails for $\alpha$ in each fixed bounded range. For example the first derivative is $u_\alpha-u$ and the second is $u_\alpha(1-u_\alpha)$. Also

$$
              \int_{\mathbb R}(u_\alpha-u)\,d\nu=\frac{\alpha}{\lambda k}
 \tag{4}
$$

by differentiation in $\alpha$ and integration of the logistic derivative. It vanishes at zero. It follows that $R_{\rm out}$ is smooth strictly convex, with derivative

$$
 R_{\rm out}'(\alpha)=\int_{\mathbb R\setminus I}(u_\alpha-u)\,d\nu
      =\frac{\alpha}{\lambda k}-\int_I(u_\alpha-u)\,d\nu .
$$

The last integral is bounded, so $R_{\rm out}'$ is onto $\mathbb R$. Thus for each $d$ there is a unique $\alpha$ with $R_{\rm out}'(\alpha)=d$, and the supremum in (1) is attained there. In particular $R_{\rm out}^*$ is finite and continuous, nonnegative because $R_{\rm out}(0)=0$, and zero at $d=0$.

For any real bounded Riemann-integrable $\psi$ on $I$, extend it by zero off $I$ while keeping its values at the endpoints of $I$. Its log-Laplace exponent conditional on the actual failure event is, by the preceding log-Laplace theorem,

$$
 \begin{split}
 \Lambda_I(\psi)&=\lim_{Y\to\infty}K^{-1}
             \log\mathbb E_{\mathcal F}e^{K\langle\psi,\mu_N\rangle}\\
  &=\inf_{\alpha\in\mathbb R}\left\{
      \int_I [L_y(\alpha+\psi(y))-\alpha u(y)]\,d\nu(y)
                           +R_{\rm out}(\alpha)\right\}.
 \end{split}
 \tag{5}
$$

Indeed subtract the unmarked constant $S_0$ in that theorem by subtracting $\log(1+e^{-ky})-\mathbf1_{y\le0}(-ky)$ under its integral. The remaining sharp-step subtraction $-\alpha\mathbf1_{y\le0}$ can be changed to $-\alpha u$, since $\int_{\mathbb R}(u-\mathbf1_{y\le0})d\nu=0$. Both comparisons are differences of absolutely integrable residuals. The possible endpoint jumps in the extended field are permitted by that theorem.

The optimizer in (5) is unique: the function minimized has strictly positive second derivative and its first derivative is the full signed occupation imbalance. Explicitly, if $\psi$ is extended by zero, that derivative is $\int_{\mathbb R}(u_{\alpha+\psi(y)}-u)\,d\nu$. It is zero at the optimizer. Monotone comparison with (4) gives existence and bounds it in absolute value by $\|\psi\|_\infty$.

## 2. Dual computation, including the boundary densities

First suppose $\mu=g\,d\nu$ on $I$ with $0\le g\le1$ almost everywhere. Taking the Legendre dual of (5) over continuous $\psi$ on $I$, and interchanging the two suprema (one is the negative of the infimum over $\alpha$), gives

$$
 \begin{split}
 \sup_{\psi\in C(I)}\big(\langle\psi,\mu\rangle-\Lambda_I(\psi)\big)
  &=\sup_{\psi,\alpha}\left\{\int_I
      \big[(\psi+\alpha)g-L_y(\psi+\alpha)\big]\,d\nu
        -\alpha\int_I(g-u)\,d\nu-R_{\rm out}(\alpha)\right\}\\
  &=\int_I H(g\Vert u)\,d\nu+
         R_{\rm out}^*\!\left(-\int_I(g-u)\,d\nu\right).
 \end{split}
 \tag{6}
$$

For the last equality, at each $\alpha$ the continuous field $j=\psi+\alpha$ ranges over all $C(I)$. Pointwise, the supremum of $jq-L_y(j)$ is $H(q\Vert u(y))$: for $0<q<1$ its maximizing argument is $\log(q/(1-q))+ky$, and at $q=0,1$ take the one-sided infinite limit. To justify the integrated equality even at measurable boundary densities, take the measurable optimizer clipped to $[-A,A]$, with the endpoint values $\mp A$ when $q=0,1$. Its pointwise payoff is the maximum on $[-A,A]$, nonnegative and increasing to $H$, so monotone convergence applies. For each fixed $A$, approximate this bounded measurable clipped field in $L^1(I,d\nu)$ by continuous fields. The payoff changes by at most $2$ times the $L^1$ error because $g\in[0,1]$ and $0\le L_y'(j)\le1$. This proves the equality over continuous fields without any regularity assumption on $g$.

If $\mu$ is not dominated by $\nu$ on $I$, there exists a continuous $\phi\ge0$ on $I$ with $\langle\phi,\mu\rangle>\int_I\phi\,d\nu$, by regularity of finite Borel measures on a compact interval. For $t\ge0$, choosing $\alpha=0$ in (5) and using $L_y(t\phi)\le t\phi$ gives $\Lambda_I(t\phi)\le t\int_I\phi\,d\nu$. Letting $t\to\infty$ proves that the continuous dual is infinite. Thus the dual in (6) equals (2) on the full space.

For the outside characterization, fix $d$ and its maximizing $\alpha$ in (1). Pointwise Fenchel's inequality gives

$$
 H(h\Vert u)\ge
         \alpha(h-u)-[L_y(\alpha)-\alpha u].
$$

The right side is integrable for each of the admissible outside profiles. Integrating yields the cost at least $\alpha d-R_{\rm out}(\alpha)=R_{\rm out}^*(d)$. For $h=u_\alpha$ equality holds pointwise and its tails and imbalance satisfy the admissibility conditions by (4) and the defining equation of $R_{\rm out}'$. This proves the claimed minimum. The unique zero of (2) is $g=u$ almost everywhere because the Bernoulli entropy has that unique zero and both rate terms are nonnegative.

The dual over continuous functions is lower semicontinuous in the weak topology. Every finite rate measure is dominated by $\nu$, hence has mass bounded by $\nu(I)$. Sets of positive measures of bounded mass are weakly compact on the compact interval (by weak compactness of the bounded positive cone in the dual of $C(I)$). Thus the closed rate sublevel sets are compact. This verifies goodness.

## 3. Closed-set upper bound on actual integers

All $\mu_N$ have mass deterministically bounded by the count of primes with $y_p\in I$ divided by $K$. The quantitative prime number theorem of [Johnston–Yang, Corollary 1.2, (1.5)](https://arxiv.org/pdf/2204.01980#page=2), also used in the collar theorem, gives

$$
      K^{-1}\#\{p:y_p\in I\}=\nu(I)+o(1).
$$

Indeed the prime interval has length $(b-a)Z/\ell$, its log prime weight is $\sim\lambda\ell$, and the two endpoint errors in $\vartheta$ are $o(Z/\ell)$. Thus the supports of the laws for all sufficiently large $Y$ lie in some common compact set $\mathcal C$ of mass-bounded positive measures.

Let $C$ be closed. If $C\cap\mathcal C$ is empty the desired bound is automatic. Otherwise fix any finite $s<\inf_{\mu\in C}{\mathsf I}_I(\mu)$. For each $\mu\in C\cap\mathcal C$, choose a continuous $\psi$ such that $\langle\psi,\mu\rangle-\Lambda_I(\psi)>s$, using the dual (6). The corresponding strict inequality defines an open neighborhood of $\mu$ in the weak topology. A finite subcover exists for $C\cap\mathcal C$. On each of these neighborhoods, the exponential Markov inequality and (5) bound the limsup of the scaled log probability by $-s$. The same bound holds for their finite union. Letting $s$ approach the infimum, including arbitrarily large $s$ for an infinite infimum, proves the first part of (3).

## 4. Open-set lower bound by an exact conditional tilt

First take a step density $g$ on $I$ with $\epsilon\le g\le1-\epsilon$ on each of its finitely many steps for some $\epsilon>0$. Put $d=-\int_I(g-u)\,d\nu$ and choose the balancing $\alpha$ with $R_{\rm out}'(\alpha)=d$. The bounded Riemann-integrable field

$$
            \psi(y)=\log\frac{g(y)}{1-g(y)}+ky-\alpha,\qquad y\in I
 \tag{7}
$$

extended by zero outside $I$, produces the occupation $u_{\alpha+\psi(y)}=g(y)$ on $I$. The outside occupation is $u_\alpha(y)$ and compensates the signed imbalance, so $\alpha$ is precisely the optimizer in (5) for this field. It follows that the dual value is attained at (7) if bounded Riemann-integrable fields are allowed:

$$
                   \langle\psi,g\,d\nu\rangle-\Lambda_I(\psi)
                          ={\mathsf I}_I(g\,d\nu).
 \tag{8}
$$

Indeed the inner payoff then attains the pointwise entropy and the outer one attains its scalar dual.

For any fixed bounded Riemann-integrable $\phi$ on $I$, the function $t\mapsto\Lambda_I(\psi+t\phi)$ differentiates at zero with derivative $\int_I\phi g\,d\nu$. To see this use the minimizing equation in (5); the derivative of the equation in $\alpha$ is the strictly positive integral of the logistic derivative, with integrable tails. Differentiation in $t$ is permitted by compact support and boundedness of the field. The implicit function theorem gives a differentiable minimizing $\alpha(t)$ near zero, and its contribution to the derivative of the objective vanishes by stationarity. The derivative thus obtained is the asserted integral. This step is only about the limiting functional; no differentiation of finite-size conditional moments has been interchanged with the limit.

Now give the actual finite failure set the new probability law

$$
 \frac{d\mathbb P_{\psi,Y}}{d\mathbb P_{\mathcal F}}
 =\exp\big(K\langle\psi,\mu_N\rangle-K\Lambda_{I,Y}(\psi)\big),
 \qquad \Lambda_{I,Y}(\psi)=K^{-1}
                    \log\mathbb E_{\mathcal F}e^{K\langle\psi,\mu_N\rangle}.
$$

For every such fixed $\phi$, its log-Laplace functional under this law, in direction $\phi$ and parameter $t$, is
$\Lambda_{I,Y}(\psi+t\phi)-\Lambda_{I,Y}(\psi)$.
Equation (5) holds for both fields. The derivative just computed and Chernoff's inequality at small fixed parameters of both signs show that $\langle\phi,\mu_N\rangle$ deviates from $\int_I\phi g\,d\nu$ by more than any fixed positive tolerance with probability $O(e^{-cK})$ under $\mathbb P_{\psi,Y}$, for some $c>0$. This applies in particular to the field $\phi=\psi$ itself.

For a weakly open set $G$ containing $g\,d\nu$, choose a finite list of continuous test functions and positive tolerances defining a weak neighborhood of that measure contained in $G$. Under the tilted law, all these inequalities hold together with probability $1-o(1)$, and so does $\langle\psi,\mu_N\rangle\le\langle\psi,g\,d\nu\rangle+\eta$ for any fixed $\eta>0$. Undoing the exact tilt on that joint event,

$$
 \liminf_{Y\to\infty}K^{-1}\log\mathbb P_{\mathcal F}(\mu_N\in G)
   \ge \Lambda_I(\psi)-\langle\psi,g\,d\nu\rangle-\eta .
$$

Send $\eta$ to zero and use (8).

Finally, each admissible measurable $g$ with $0\le g\le1$ almost everywhere can be approximated in $L^1(I,d\nu)$ by step densities staying strictly between $0$ and $1$. For instance first average $g$ on successive finer fixed interval partitions (convergence in $L^1$ follows by density of continuous functions and the $L^1$ contraction of averaging), then mix with a small positive proportion of the constant $1/2$. This approximation converges weakly as measures and also in rate value: the entropy integral is continuous in $L^1$ on these bounded densities because $u$ stays in a compact subinterval of $(0,1)$ on $I$ and binary entropy is uniformly continuous, and the reservoir cost is a continuous function of the single integrated imbalance. Hence if $g\,d\nu\in G$, the approximants are in $G$ for all sufficiently fine stages and give the same lower bound $-{\mathsf I}_I(g\,d\nu)$ in the limit. Taking the infimum over the finite-rate measures in $G$ proves the second part of (3); if there are none the inequality is automatic. All probabilities here are conditional counts of actual even targets failing the positive test.
