# A negative Dickman pocket with both prime logs above the cap

**Scope.** The ordinary two-missing-prime finite Dickman coefficient has a negative interval even when both prime logs are above the cap, although its distant-from-boundary signed count is always positive there. We prove exactly two simple boundaries, give the two local profiles, and resolve the exterior boundary's displacement relative to the reflected one-prime root. The arithmetic consequence is only for the fixed-parameter genuine matched parity mean when signs reinforce. The asymptotics in the deterministic cap size do not give a growing-cutoff arithmetic limit.

Use the normalization of [the finite ordinary profile](r108-spectral-finite-matched-ordinary-dickman-profile.md), the even cap $G_t=h_t/\kappa^2$ of [the one-prime sign theorem](r109-spectral-finite-dickman-cap-sign-threshold.md), and the notation of [the two-prime transition analysis](r110-spectral-three-two-prime-dickman-transitions.md). Thus $\rho$ is the ordinary cumulative Dickman function, zero on the negative axis, $\kappa=\int_0^\infty \rho$, $C(a)=\int_{\mathbb R}\rho(u)\rho(u+a)\,du$, and $\mathcal T(a)=\int_a^\infty C(v)\,dv$. Let $\lambda_*(t)$ be the unique one-prime zero for $t\ge80$, $d_t=t-\lambda_*(t)$, and $\xi_t=\xi(d_t)$, where $\xi(d)>0$ satisfies $e^{\xi(d)}=1+d\xi(d)$. The previous results give $d_t\sim\log t/\log\log t$, $\xi_t\sim\log\log t$, and $t C(d_t)=\kappa^2+O(t^{-1})$.

**Theorem.** Fix $\delta>0$ and take $t$ sufficiently large depending on $\delta$. Uniformly for $x\ge(1+\delta)t$, the two-prime coefficient $\Phi(t;x,y)$ on $y\ge x$ has exactly two simple zeros $y_-<y_+$, with $y_-<x+t<y_+$. Its signs in the three successive open intervals are positive, negative, positive, and it is positive also at $y=x$. Their locations are

$$
 \begin{split}
 y_-&=x+t-d_t+\frac{\log 3}{\xi_t}
                     +O_\delta\!\left(\frac1{d_t\xi_t}\right),\\
 y_+&=x+t+d_t-\frac4{t\xi_t^2}
                        \left(1+O_\delta(d_t^{-1})\right).
 \end{split}
 \tag{1}
$$

For every fixed $A<\infty$, uniformly at $|v|\le A$ and all these $x$,

$$
 \begin{split}
 \Phi\!\left(t;x,x+t-d_t+\frac v{\xi_t}\right)
     &=3-e^v+O_{\delta,A}(d_t^{-1}),\\
 \Phi\!\left(t;x,x+t+d_t+\frac v{\xi_t}\right)
     &=1-e^{-v}+O_{\delta,A}(d_t^{-1}).
 \end{split}
 \tag{2}
$$

In particular the inside and outside transitions have different centers when measured relative to $t\mp d_t$. The small exterior correction in (1) comes from the integrated correlation tail, not from the distant-from-boundary signed count.

## 1. Correlation tails and derivatives

We use the Dickman ratio in the two-prime transition analysis, (5), proved from Hildebrand--Tenenbaum Corollary 2.4 (2.7). It is uniform for $|u|\le d/2$ as $d\to\infty$:

$$
 \frac{\rho(d+u)}{\rho(d)}
 =\exp\{-u\xi(d)+O((1+u^2)/d)\},
 \qquad \xi'(d)\ll 1/d .
 \tag{3}
$$

Also, from that analysis, $C(d)=\rho(d)\xi(d)^{-1}(1+O(d^{-1}))$ and $\mathcal T(d)\le2C(d)$ for $d\ge1$. We record the two finer local estimates needed for the exterior displacement:

$$
 \mathcal T(d)=\frac{C(d)}{\xi(d)}(1+O(d^{-1})),\qquad
 -C'(d)=\xi(d)C(d)(1+O(d^{-1})) .
 \tag{4}
$$

For the first, the same ratio (3) and the asymptotic for $C(d)$ give
$C(d+u)=C(d)e^{-u\xi(d)}(1+O(1/d))$ uniformly for $0\le u\le1$. Integrate over that interval. The remaining tail satisfies $\mathcal T(d+1)\le2C(d+1)\ll C(d)e^{-\xi(d)}$. Since $\xi(d)e^{-\xi(d)}\le1/d$, the resulting relative error is $O(1/d)$. For the second, the delay equation and (3) with shift $-1$ show on $0\le u\le1$ that
$-\rho'(d+u)/\rho(d+u)=\xi(d)(1+O(1/d))$. Integrate against $\rho(u)$ there. The remaining derivative integral is at most $\kappa \rho(d)/d$ because for $u\ge1$, $-\rho'(d+u)=\rho(d+u-1)/(d+u)\le\rho(d)/d$. The same range of the undifferentiated integral costs only $O(C(d)/d)$ by (3) and monotonicity, as in the two-prime analysis. These bounds prove (4). Differentiation under the integral here is valid for $d\ge2$ by the integrable majorant $\rho(u)/(d-1)$ in a fixed small neighborhood of the differentiation point.

## 2. Isolate the two roots of the difference term

For $y\ge x\ge(1+\delta)t$, the exact signed sum is
$\Phi(t;x,y)=G_t(0)-2G_t(x)-2G_t(y)+2G_t(y-x)+2G_t(y+x)$. Put $b=y-x\ge0$ and $J_t(b)=G_t(0)+2G_t(b)$. The other three arguments have distance at least $\delta t$ above the cap. By the inactive value and derivative bounds of the two-prime transition analysis (its Section 3, or the factorial bound and its derivative estimate applied to the exact cap),

$$
 \Phi(t;x,x+b)=J_t(b)+\mathcal E_{t,x}(b),\qquad
 |\mathcal E_{t,x}(b)|+|\mathcal E_{t,x}'(b)|
 \ll_\delta E_t,\qquad E_t=\frac{1+t}{(\lfloor\delta t\rfloor-1)!}.
 \tag{5}
$$

Here and below the estimates at $b=0$ may be read from the right. The bound is uniform for unbounded $x,b$ on the indicated side of the cap.

Write $d=|b-t|$ and put
$A_t(b)=2\mathcal T(t)+t C(t)+2\mathcal T(t+b)+t C(t+b)$.
The exact even-cap identity, with $\mathcal T(-d)=\kappa^2-\mathcal T(d)$, gives

$$
 \kappa^2 J_t(b)=
 \begin{cases}
  3\kappa^2-2\mathcal T(d)-t C(d)-A_t(b), & b<t,\\
  \kappa^2+2\mathcal T(d)-t C(d)-A_t(b),& b\ge t .
 \end{cases}
 \tag{6}
$$

The two formulae agree at $b=t$ by $\mathcal T(0)=\kappa^2/2$. The nonnegative $A_t(b)$ and its derivative are uniformly $O((1+t)/(\lfloor t\rfloor-1)!)$ for $b\ge0$ by the factorial estimates for $C,\mathcal T,C'$. For $d\ge1$, the value in (6) lies between
$k\kappa^2-(t+4)C(d)-A_t(b)$ and $k\kappa^2-(t-4)C(d)$, where $k=3$ inside and $k=1$ outside. These bounds use $\mathcal T(d)\le2C(d)$.

By the local correlation ratio of the two-prime analysis and its calibration $t C(d_t)=\kappa^2+O(t^{-1})$, for bounded $v$,

$$
 t C(d_t+v/\xi_t)=\kappa^2 e^{-v}(1+O_A(d_t^{-1}))
 \qquad (|v|\le A).
 \tag{7}
$$

In particular, by monotonicity of $C$, for $d\ge d_t+3/\xi_t$ the lower bound from (6) gives $J_t(b)>1/2$ for large $t$. For $1\le d\le d_t-3/\xi_t$ its upper bound gives $J_t(b)<-1/2$. For $0\le d\le1$, use directly $C(d)\ge C(1)>0$ and $2\mathcal T(d)\le\kappa^2$ in (6) to give $J_t(b)<-1/2$ for large $t$. Thus (5) excludes all zeros except in the two disjoint intervals of radius $3/\xi_t$ centered at $b=t-d_t$ and $b=t+d_t$.

With $b$ in each such interval (or in an analogous window of any fixed multiple of $\xi_t^{-1}$), equations (6)--(7) give (2): the term $2\mathcal T(d)$ is $O_A(1/t)$, and the far tails are factorial-small. For the derivative inside the first interval, write $b=t-d_t+v/\xi_t$ and use $d=t-b$; outside write $b=t+d_t+v/\xi_t$ and use $d=b-t$. Differentiating (6) and using (4)--(7) yields

$$
 \begin{split}
 J_t'(t-d_t+v/\xi_t)&=-\xi_t e^v(1+O_A(d_t^{-1})),\\
 J_t'(t+d_t+v/\xi_t)&=+\xi_t e^{-v}(1+O_A(d_t^{-1})).
 \end{split}
 \tag{8}
$$

Indeed the leading terms are respectively $t C'(d)/\kappa^2$ and $-t C'(d)/\kappa^2$, and the $\mathcal T$ derivative has magnitude $O_A(1/t)$. The derivative of the far tail is smaller still. Also $\xi(d)=\xi_t+O_A(1/(d_t\xi_t))$ by (3). The derivative error in (5) cannot spoil either sign. The endpoint values of each interval have opposite signs by the estimates at its endpoints in (6). The intermediate value theorem and strict monotonicity give one simple zero in each and the asserted sign pattern. The inside location in (1) follows by evaluating (2) at $v=\log 3$ and using the derivative bound there and between that point and the zero.

## 3. Exterior displacement relative to the reflected one-prime root

For $a\ge0$ let $Q_t(a)=2\mathcal T(a)+t C(a)$, a nonnegative quantity. The calibrated one-prime zero obeys exactly

$$
 t C(d_t)=\kappa^2-2\mathcal T(d_t)
                      -Q_t(2t-d_t)+Q_t(t),
 \tag{9}
$$

by applying the one-prime identity of the two-prime analysis, (8), at $\lambda_*(t)=t-d_t$. Evaluating (6) at $b=t+d_t$ and substituting (9) gives

$$
 \kappa^2 J_t(t+d_t)=4\mathcal T(d_t)
                      +Q_t(2t-d_t)-2Q_t(t)-Q_t(2t+d_t).
 \tag{10}
$$

Since $d_t=o(t)$, the three $Q_t$ terms on the right are factorial-small. By (4) and the calibrated $t C(d_t)=\kappa^2+O(t^{-1})$, the residual value including (5) is

$$
 \Phi(t;x,x+t+d_t)
   =\frac4{t\xi_t}\left(1+O_\delta(d_t^{-1})\right)>0 .
 \tag{11}
$$

In the exterior window the derivative in (8) is $\gg\xi_t$, even after adding (5). Thus the exterior zero lies to the left of $x+t+d_t$ by $O_\delta(1/(t\xi_t^2))$. On that shorter interval (8) and (5) sharpen the derivative to $\xi_t(1+O_\delta(d_t^{-1}))$, because the corresponding $v$ changes only by $O_\delta(1/(t\xi_t))$. Divide the value (11) by this derivative using the mean value theorem. This proves the exterior location in (1) including its sign and leading constant.

## 4. Transfer to the fixed-parameter matched mean

Retain the full hypotheses and notation of the original finite ordinary profile, including the genuine odd Page conductor if one exists, the complete primorial family, the bounded two-prime missing part, the fixed tests, and the positively scaled primorial parameter. Take $t_*=2Bg/\ell\to t$ and the actual scaled logs of the two missing conductor primes to converge to $x,y$ in the stated regime, with fixed sufficiently large $t$. If $y$ is strictly between the two exact zeros, the ordinary normalized coefficient is negative. It is positive outside the closed negative interval, with the same statement at $y=x$. For these fixed parameters the corresponding coefficient is bounded away from zero along the sequence by continuity. Thus the theorem can give a negative genuine ordinary mean even with both prime logs above the cap, in a region not detected by the far-from-boundary count.

Let $s$ be the nonzero sign just obtained. If also $(1-\beta)G\le C_*\log G$ and $\chi(-1)=-s$, then the genuine matched parity mean has sign $s$ and magnitude $\gg \mathcal R+HP_1(M)$ for the full mixed strip and for its original moving-major choice. This is the original finite-profile formula with the exceptional sign from [the matched exceptional comparison](r100-spectral-matched-ramanujan-exceptional-mean.md): $P_1(M)>0$ under the displayed closeness and the two terms reinforce. The limiting large-$t$ equations (1)--(2) are deterministic statements made before this fixed-parameter arithmetic transfer. No assertion is made at the exact zeros, for competing signs, for individual targets, for the full signed shell, or for Weak S. No Page-zero existence is asserted, and neither Dirichlet GRH nor external zero-gap bounds are assumed.
