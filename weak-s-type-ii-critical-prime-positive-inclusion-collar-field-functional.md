# A constrained collar log-Laplace functional for the positive omission test

Use the positive cutoff test of the [marked prime profile](weak-s-type-ii-critical-prime-positive-inclusion-marked-prime-profile.md). This result concerns only the actual even integers failing that **positive** test. It is unconditional and makes no assertion about signed Type II errors, individual-prime independence, or a central limit theorem.

Fix $0<M<Q$. Define

$$
 v=\log\log Y,\quad \ell=\log v,\quad \lambda=Q/M,\quad
 Z=v^\lambda,\quad D=(M/(3\mathrm e))^\lambda,\quad
 K=Z/\ell^2,\quad k=(\lambda-1)/D,\quad y_p=\ell(p/Z-D).
$$

For $H>0$ let $\mathcal T_N(H)=\sum_{r\mid\operatorname{rad}N,\,r>H}3^{\omega(r)}/r$. Let $\mathcal F$ consist of the even $N\in[Y,2Y]$ with $\mathcal T_N((\log Y)^Q)>(\log Y)^{-M}$, and let $\mathbb E_{\mathcal F}$ be uniform expectation on this set. Put $S_0=\pi^2/(6\lambda k)$ and $\mathfrak L(z)=(1+e^{-z})^{-1}$.

**Theorem.** For each fixed real bounded, compactly supported Riemann-integrable field $\psi$, set

$$
 \begin{split}
 \mathcal J_\psi(\alpha)&=\frac1\lambda\int_{\mathbb R}
    \left(\log(1+e^{-ky+\alpha+\psi(y)})
             -\mathbf1_{y\le0}(-ky+\alpha)\right)dy,\\
 \Lambda(\psi)&=\min_{\alpha\in\mathbb R}\mathcal J_\psi(\alpha)-S_0 .
 \end{split}
 \tag{1}
$$

Then

$$
 \lim_{Y\to\infty}K^{-1}\log\mathbb E_{\mathcal F}
       \exp\left(\sum_p\psi(y_p)\mathbf1_{p\mid N}\right)
                  =\Lambda(\psi).
 \tag{2}
$$

The minimizer is unique and is the solution of

$$
       \int_{\mathbb R}\left(
          \mathfrak L(-ky+\alpha+\psi(y))-\mathbf1_{y\le0}\right)\,dy=0 .
 \tag{3}
$$

In particular this limiting functional is generally not the one obtained from independent logistic occupations.

For a fixed field $\phi$ of the same class, let $u(y)=\mathfrak L(-ky)$ and $r(y)=u(y)(1-u(y))$. The first two derivatives of the **limiting functional** are

$$
 \begin{split}
 \left.\frac{d}{dt}\Lambda(t\phi)\right|_{t=0}
       &=\frac1\lambda\int_{\mathbb R}u\phi\,dy,\\
 \left.\frac{d^2}{dt^2}\Lambda(t\phi)\right|_{t=0}
       &=\frac1\lambda\left[
         \int_{\mathbb R}r\phi^2\,dy
         -\frac{(\int_{\mathbb R}r\phi\,dy)^2}{\int_{\mathbb R}r\,dy}\right].
 \end{split}
 \tag{4}
$$

The second identity does not interchange limit and derivative in (2).

## 1. The exact balancing parameter

Since $\psi$ is zero off a compact interval, the integrands in (1), (3) and their derivatives in $\alpha$ are integrable, with exponentially decaying tails locally uniformly in $\alpha$. Differentiation gives $\mathcal J_\psi'(\alpha)$ equal to the integral in (3) divided by $\lambda$, and $\mathcal J_\psi''(\alpha)>0$ since the logistic derivative is positive. For $\psi=0$ the integral in (3) equals $\alpha/k$: at zero it vanishes by oddness, and its derivative is
$\int_{\mathbb R}\mathfrak L'(-ky+\alpha)\,dy=1/k$.
For general $\psi$, monotone comparison to constants $\pm\|\psi\|_\infty$ therefore brackets the root in $[-\|\psi\|_\infty,\|\psi\|_\infty]$. This proves existence and uniqueness and that the root is a global minimum. In particular $\min_\alpha\mathcal J_0(\alpha)=\mathcal J_0(0)=S_0$, the last integral being the unmarked soft transition of the [second-order count](weak-s-type-ii-critical-prime-positive-inclusion-second-order-constant.md).

We first prove (2) for step fields with finitely many intervals and arbitrary values allowed at their finite set of endpoints. A single endpoint can meet at most one $p$; altering the values at a fixed finite number of endpoints multiplies the exponential in (2) by bounded positive factors. The detailed estimates below also keep such endpoints at a negligible cost.

## 2. Upper moment and its minimized exponent

Use $\vartheta(x)=x+O(xe^{-c_0\sqrt{\log x}})$ from [Johnston–Yang, Corollary 1.2, (1.5)](https://arxiv.org/pdf/2204.01980#page=2). On each fixed bounded $y$ interval this gives the limiting prime counting measure $K^{-1}\sum_p\delta_{y_p}=dy/\lambda$ in the limit, tested against bounded Riemann-integrable functions. Indeed at $p\asymp DZ$ one has $\log p\sim\lambda\ell$ and the prime interval of $y$ length $d$ has $p$ length $dZ/\ell$, with endpoint error $o(Z/\ell)$ for $\vartheta$. The same argument gives $O(K)$ primes uniformly in any unit $y$ bin in a fixed compact $p/Z$ interval about $D$.

Use the same parameters as in the marked-prime proof, allowing an arbitrary fixed transition shift $\alpha$:

$$
 \begin{gathered}
 \sigma_0=1/\lambda,\quad a_0=1-\sigma_0,\quad b=(\lambda-\log D)/\lambda^2,
 \quad \sigma=\sigma_0+\sigma_0/\ell+b/\ell^2,\\
 s_*=\frac{\lambda}{3\mathrm e}D^{a_0}v^{\lambda-1}\ell,\qquad
 s=s_*\exp\left(\frac{-\lambda b+\alpha/\lambda}{\ell}+\frac{c}{\ell^2}\right),\\
 w_p=\log(1+3p^{\sigma-1}),\quad V_p=e^{s w_p},\quad
 \eta_p=sw_p-\log p,\quad T_0=(\sigma Q-M)v .
 \end{gathered}
 \tag{5}
$$

Here $c$ is in a fixed bounded interval and will be tuned only for the lower count. Since $\sigma>0$, positive Rankin majorization implies $\sum_{p\mid N}w_p>T_0$ at any $N\in\mathcal F$. The marked local factor in the actual integer product is $V_p e^{\psi(y_p)}$ when $p\mid N$, $1$ otherwise. It is at least $1$ on occupied primes: on the marker support $sw_p\sim\lambda\ell$ while the field is bounded; outside it $V_p\ge1$. Expand the nonnegative divisor coefficients, count multiples by $2Y/d$, and allow all integers for the upper bound. For

$$
 \mathcal M(\psi)=Y^{-1}\sum_{N\in\mathcal F}
              e^{\sum_p\psi(y_p)\mathbf1_{p\mid N}},
 \qquad A_p^\psi=1-1/p+e^{\psi(y_p)}V_p/p,
$$

this proves

$$
          \mathcal M(\psi)\le 2\exp\left(\sum_p\log A_p^\psi-sT_0\right).
 \tag{6}
$$

The full product is convergent, and can first be truncated at primes $\le2Y$ plus the finite marker support in the divisor argument.

For clarity the full marked exponent, uniformly for fixed bounded $c$, is

$$
 \sum_p\log A_p^\psi-sT_0
      =-DZ+K\big(D\lambda/2+\mathcal J_\psi(\alpha)\big)+o(K).
 \tag{7}
$$

Here is the calculation retaining the literal sharp prefix that makes the balancing shift available. Put $\gamma=\alpha/\lambda$, fix large $R>2D+1$ and $J_0>6/\sigma_0$, and let $\delta=\ell^{-J_0}$. At $\delta Z\le p\le RZ$, put $x=p/Z$, $h=(D/x)^{a_0}$. The marked-prime proof's expansion, obtained by $w_p=3p^{\sigma-1}+O(p^{2(\sigma-1)})$ and $e^z/(1+z)=1+z^2/2+O(|z|^3)$ for $z=\sigma_0\log x/\ell$, is

$$
 \frac{\eta_p}{\log p}
 =h-1+\frac{\gamma h}{\ell}
 +\frac{h}{\ell^2}\left[\frac{\sigma_0^2}2(\log x)^2+
                              b\log x+c+\frac{\gamma^2}{2}\right]
 +O\big(h(1+|\log x|^3)\ell^{-3}\big)+o(\ell^{-J}).
 \tag{8}
$$

Here $J$ may be any fixed constant; the nonlinear error after multiplication by $s$ is bounded by $v^{1-\lambda}$ times a fixed power of $\ell$. Weighted PNT sums the displayed remainder using ratio-two majorants $Z(1+j^3)2^{-j\sigma_0}$. The relevant weights and their variations on $[\delta,D]$ are bounded by fixed powers of $\ell$; the uniform endpoint $\vartheta$ error is exponentially smaller. Extending to $x=0$ is justified by the cutoff $J_0$ and the integrable bound $h(1+|\log x|^2)$. It follows that the prefix $\sum_{\delta Z\le p\le DZ}\eta_p$ is given to $o(K)$ by integration of the terms of (8) against $Z\,dx$ on $(0,D]$.

On the threshold side, $s_*Mv/\ell=\lambda DZ$ gives

$$
 sT_0=\lambda DZ\left[1+\frac{\gamma}{\ell}
             +\frac{c+\gamma^2/2-\lambda^2b^2/2}{\ell^2}
             +O(\ell^{-3})\right].
$$

Since $\int_0^D h\,dx=\lambda D$, the linear and quadratic terms in $\gamma$ cancel between threshold and prefix, as does $c$. The prefix minus threshold is thus $-DZ+K D\lambda/2+o(K)$: the remaining moments are $\int_0^D h\log x=\lambda D(\log D-\lambda)$ and $\int_0^D h(\log x)^2=\lambda D((\log D-\lambda)^2+\lambda^2)$, with $b$ as in (5).

The residual in the Euler log sum is exactly

$$
 \log(1-1/p+e^{\eta_p+\psi(y_p)})
                         -\mathbf1_{p\le DZ}\eta_p .
$$

On the middle range $1-1/p$ may be replaced by $1$ at total $O(\sum_{\delta Z\le p\le RZ}1/p)=o(K)$. Near $D$ use (8), uniformly on a fixed compact $x$ interval containing $D$:

$$
 \eta_p=-ky_p+\alpha+O((1+y_p^2)/\ell),\qquad
 |\eta_p|\ge c_1|y_p|-C_1 .
 \tag{9}
$$

Outside a fixed bounded $y$ interval the signs there are those of $-y_p$. The second assertion follows from the negative derivative of $h$ on the compact $x$ interval and bounded $\alpha$. For fixed bounded $y$ the residual thus tends to the integrand in (1) before its factor $1/\lambda$, uniformly away from its finitely many endpoints for step $\psi$. The remaining unit $y$ bins have $O(K)$ primes and an exponentially decaying bound, since the field vanishes in the tails and the subtraction matches the sign. On the middle range outside the compact $x$ interval, monotonicity of $\eta_p$ bounds the residual by $O(e^{-c_2\ell})$ per integer after the $1/p$ change. This proves that the residual sum there and in the transition together give $K\mathcal J_\psi(\alpha)+o(K)$.

For $p<\delta Z$, the field is absent for large $Y$ and $\log A_p^\psi\le3s p^{\sigma-1}$, giving $O(Z\delta^{\sigma_0/2})=o(K)$ by partial summation. For $p>RZ$ the field is also absent, and the unmarked bound $V_p\le Z^{1/4}$ for large fixed $R$ yields $\sum_{p>RZ}\log A_p^\psi\ll Z^{1/4}\ell=o(K)$, since $V_p-1\ll Z^{1/4}s p^{\sigma-1}$. Thus (7) follows and is unchanged if the product is cut at $p\le RZ$. This is the same sharp-prefix mechanism as [§2 of the marked-prime calculation](weak-s-type-ii-critical-prime-positive-inclusion-marked-prime-profile.md#2-the-marked-euler-exponent-including-the-endpoint-cutoff), now with an arbitrary field rather than a half-collar marker.

Use the root (3) in (7). Dividing (6) by the established second-order count

$$
       |\mathcal F|/Y=\exp(-DZ+K(D\lambda/2+S_0)+o(K))
$$

proves the desired upper bound.

## 3. Matching lower by two finite tilts

Keep the root $\alpha$ of (3) fixed. Let $P=\prod_{p\le RZ}p=Y^{o(1)}$ and put the uniform probability $\mathbb P_0$ on the even residue classes modulo $P$. For odd primes in this finite set the indicators $I_p=\mathbf1_{p\mid N}$ are independent with inclusion probability $1/p$, while $I_2=1$ by the Chinese remainder theorem. Each residue class has $Y/P+O(1)$ actual representatives in $[Y,2Y]$. Thus every nonnegative weighted set of even residue patterns has integer count normalized by $Y$ given by its weighted $\mathbb P_0$ measure times $\tfrac12(1+O(P/Y))$. This relative transfer holds even for very rare events.

All marked primes are $\le RZ$ for large $Y$. Put $L_0=\sum_{p\le RZ}I_p w_p$, $m_0=\sum_{p\le RZ}I_p w'_p$, where the prime weight derivative is in $\sigma$, and define the tilted pattern law $\mathbb P_c$ by

$$
 \frac{d\mathbb P_c}{d\mathbb P_0}
       =\mathcal Z_c^{-1}\exp\left(sL_0+\sum_{p\le RZ}\psi(y_p)I_p\right).
 \tag{10}
$$

Its normalizer satisfies $\log\mathcal Z_c=\sum_{p\le RZ}\log A_p^\psi+O(1)$, since forcing $2$ changes the corresponding unmarked factor by a factor in $[1,2]$. Odd-prime inclusion probabilities are now

$$
 u_p^\psi=\mathfrak L\!\left(\eta_p-\log(1-1/p)+\psi(y_p)\right).
$$

They remain independent in this exact finite experiment.

We show the two means are centered precisely enough for the strict test:

$$
 \mathbb E_c L_0=T_0+O(v/\ell^3),\qquad
 \mathbb E_c m_0=Qv+O(v/\ell^2).
 \tag{11}
$$

In the fixed compact $p/Z$ interval about $D$ in (9), the signed occupation difference from the step satisfies

$$
 u_p^\psi-\mathbf1_{p\le DZ}
    =F_\psi(y_p)+O((1+y_p^2)e^{-c_3|y_p|}/\ell),\qquad
 F_\psi(y)=\mathfrak L(-ky+\alpha+\psi(y))-\mathbf1_{y\le0}.
 \tag{12}
$$

This follows from (9) and bounded logistic derivative on bounded $y$ intervals. For large $|y|$ the two arguments being compared have the same sign and magnitudes $\gg |y|$, so the derivative on the segment between them is exponentially small. In particular $F_\psi$ has integrable exponential tails and, crucially, **its integral is zero** by (3). Oddness is not required.

Put $f_0(p)=w_p$, $f_1(p)=w'_p$, $W_0=v^{1-\lambda}$, $W_1=v^{1-\lambda}\ell$. On the fixed compact $x$ interval, $f_j(p)/\log p=O(W_j/\ell)$ with $p$ derivative $O(W_j/(Z\ell))$ by direct differentiation. On each step subinterval the real argument of the logistic defining $u_p^\psi$ decreases in $p$, since $s w_p-\log(p-1)$ does. Therefore its total variation on the compact $x$ interval, allowing the finitely many jumps and endpoint values, is $O_\psi(1)$. Partial summation against $\vartheta$ for the signed mismatch times $f_j(p)/\log p$ costs $O_\psi(Z e^{-c_4\sqrt{\ell}}W_j/\ell)$ in replacing the prime sum by the integral; any isolated boundary prime has size $O_\psi(W_j)$, also smaller than $ZW_j/\ell^3$.

In the integral put $p=Z(D+y/\ell)$, hence $dp=Z\,dy/\ell$. By (12), replacing $f_j(p)/\log p$ by its central value incurs $O(W_j |y|/\ell^2)$ times the exponentially decaying profile. The constant-weight integral of $F_\psi$ is zero on the whole real line, and extending the resulting interval in $y$ (length comparable to $\ell$ on both sides) to that line loses exponentially little. Thus the difference from the sharp primorial-prefix moment on the compact interval is $O(ZW_j/\ell^3)$.

Outside that interval but with $\delta Z\le p\le RZ$ the field is absent for large $Y$, the mismatch is $O(e^{-c_5\ell})$ by monotonicity and the endpoint gaps, and $f_j(p)\ll W_j\ell^{C_2}$ for a fixed $C_2$. At $p<\delta Z$, (8) at $x=\delta$ and monotonicity imply the argument of the logistic is $\gg\ell^{1+J_0a_0/2}$; the missing probability there is smaller than every fixed power of $v^{-1}$. Even $O(Z)$ such terms with $f_j\ll1+\ell$ are negligible. The forced prime $2$ has no mismatch. These bounds give total errors $O(v/\ell^3)$ and $O(v/\ell^2)$ compared with the two primorial-prefix moments. The latter are $T_0+O(v/\ell^3)$ and $Qv+O(v/\ell^2)$ by (13) and its ensuing expansion in the second-order counting proof: they use $\sigma$ and $b$ of (5), not $s$ or its new shift. This proves (11).

The variance bounds are

$$
       \operatorname{Var}_c(L_0)\asymp v^{2-\lambda}/\ell^2,
       \qquad \operatorname{Var}_c(m_0)\ll v^{2-\lambda}.
 \tag{13}
$$

Indeed use independence and $w_p\asymp W_0$ on the compact interval. The logistic variances are exponentially small in $|y|$ outside a fixed bounded $y$ interval, so the unit prime-bin bound gives the required upper estimate $O(KW_0^2)$. The two outer estimates used for (11) also apply to squared weights; in particular the stronger small-prime guard remains negligible when $v^{2-\lambda}$ tends to zero. On $|y|\le1$ the probabilities are bounded away from $0,1$ since the field is bounded, and there are $\asymp K$ primes, giving a matching lower bound. The eventual lower constant works on every fixed bounded interval of $c$, as the leading logistic arguments on $|y|\le1$ and the leading prime weights there do not involve $c$. Finally $w'_p\le(\log p)w_p$ gives the second bound by independence.

At fixed $Y$ the exact differential identity

$$
                  \partial_c\mathbb E_c L_0
                     =\frac{s}{\ell^2}\operatorname{Var}_c(L_0)
                     \gg v/\ell^3
$$

holds, since the marker and $w_p$ do not depend on $c$. At $c=0$ the first discrepancy in (11) is $O(v/\ell^3)$, so on a sufficiently large fixed bounded interval we may choose $c=c(Y)$ to tune $\mathbb E_c L_0=T_0+3v/\ell^4$. By (13) and Chebyshev the pattern event

$$
  T_0+2v/\ell^4\le L_0\le T_0+4v/\ell^4,\qquad |m_0-Qv|\ll v/\ell^2
 \tag{14}
$$

has probability $1-o(1)$. On this event also require at least half of the $\asymp Z/\ell$ primes in $D/3<p/Z<D/2$ to be occupied; each has missing probability $o(1)$ uniformly by monotonicity and the fixed-side gap, which makes the extra condition hold with probability $1-o(1)$. Denote the resulting event by $\mathcal G$.

We verify its implication for the genuine strict divisor test. If $P_I$ is the product of the occupied primes in a good pattern, define $F_I(\sigma')=\sum_{p\mid P_I}\log(1+3p^{\sigma'-1})$. On any fixed window of radius $O(\ell^{-3})$ around $\sigma$, its second derivative is $\asymp v\ell$ uniformly: for the lower bound use the abundant occupied interval and each prime's second derivative of size $\asymp W_0\ell^2$ there, and for the upper bound use $\log(RZ)$ times the full weighted prime first-derivative sum $O(v)$ from the second-order proof. Take $\Delta=v/\ell^5$ and tune $\sigma_I=\sigma+O(\ell^{-3})$ so that $F_I'(\sigma_I)=Qv+\Delta/2$ by (14) and that curvature. The resulting change of $F_I(\sigma')-\sigma'Qv$ is $O(v/\ell^5)$ by Taylor's theorem. On divisors $r\mid P_I$, the finite tilt proportional to $3^{\omega(r)}r^{\sigma_I-1}$ has mean $\log r$ equal to $Qv+\Delta/2$, and variance at most $(\log(RZ))(Qv+\Delta/2)=O(v\ell)$ by independence of its Bernoulli prime selections. Therefore the strict band $Qv<\log r\le Qv+\Delta$ has mass $1-O(\ell^{11}/v)$. Keeping only this band and undoing the divisor tilt proves for every actual integer with the good pattern

$$
 \log\mathcal T_N((\log Y)^Q)
        \ge L_0-\sigma Qv-O(v/\ell^5)>-Mv .
$$

The last inequality uses the margin $2v/\ell^4$ in (14); the log-loss from the discarded tilted mass is $o(v/\ell^5)$. Primes outside $P_I$ are not used in this lower bound.

Undo only the $sL_0$ tilt of the target law (10), leaving the field in the weighted count. We obtain

$$
 \mathbb E_0\!\left(e^{\sum_p\psi(y_p)I_p}\mathbf1_{\mathcal G}\right)
 \ge \mathcal Z_c e^{-s(T_0+4v/\ell^4)}(1-o(1)).
$$

CRT transfers this with the relative factor already checked to a lower bound for $\mathcal M(\psi)$. The loss $s v/\ell^4=O(Z/\ell^3)=o(K)$ and the matching expression (7), which was uniform on the bounded interval from which $c$ was chosen, show that (6) is sharp to $o(K)$ in its logarithm. This proves (2) for step fields.

## 4. Riemann-integrable fields and the response of the limit

For fixed bounded Riemann-integrable $\psi$ supported on a compact interval, choose two fixed Darboux step bounds pointwise below and above $\psi$, with arbitrarily small $L^1$ gap, extended by zero outside the interval. At the finitely many endpoints one can enforce the inequalities with bounded values; this does not affect the integrals. The conditional exponential moment is monotone under these bounds because $I_p\ge0$. The Lipschitz bound

$$
 |\min_\alpha\mathcal J_\psi(\alpha)
              -\min_\alpha\mathcal J_{\widetilde\psi}(\alpha)|
             \le \lambda^{-1}\|\psi-\widetilde\psi\|_{L^1}
$$

is immediate from the derivative bound $0\le\mathfrak L\le1$ in the logarithmic integrand, uniformly before taking minima. The step-field result therefore gives (2) by bracketing.

For (4), along $t\phi$, differentiation under the integrals is justified by bounded compact support and exponential tails. The unique minimizer $\alpha(t)$ is smooth near zero by the scalar implicit function theorem, as the derivative in $\alpha$ of (3) at zero is $\int r=1/k>0$. Equation (3) gives $\alpha'(0)=-\int r\phi/\int r$. The first derivative of the minimum is its partial derivative in $t$, because $\mathcal J_{t\phi}'(\alpha(t))=0$ in the minimizing variable. Substitution of the implicit derivative in its second derivative proves (4). For example, a nonnegative field that is positive on a set of positive measure has a strictly positive projection correction in (4), whereas independent logistic occupation would give only the first integral. This calculation identifies the response of the limiting log-Laplace functional, not the actual variance at a varying finite-size marker or any individual-prime law.
