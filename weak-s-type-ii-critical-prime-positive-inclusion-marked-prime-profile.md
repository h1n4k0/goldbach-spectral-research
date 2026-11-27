# Conditional prime profile and the marked positive omission count

This is a theorem about the actual even integers failing the **positive** omission test in the [second-order counting result](weak-s-type-ii-critical-prime-positive-inclusion-second-order-constant.md). It concerns neither the signed Type II approximation error nor the full signed shell. No hypothesis on zeros is used.

Fix $0<M<Q$, and set

$$
 v=\log\log Y,\quad \ell=\log v,\quad \lambda=Q/M,\quad
 Z=v^\lambda,\quad K=Z/\ell^2,\quad
 D=(M/(3\mathrm e))^\lambda,\quad k=(\lambda-1)/D.
$$

Define $\mathcal T_N(H)=\sum_{r\mid\operatorname{rad}N,\,r>H}3^{\omega(r)}/r$. Let $\mathcal F$ consist of the even integers $N\in[Y,2Y]$ with $\mathcal T_N((\log Y)^Q)>(\log Y)^{-M}$.
Write $\mathbb P_{\mathcal F},\mathbb E_{\mathcal F}$ for the uniform probability and expectation on this finite set, and let $y_p=\ell(p/Z-D)$.

**Theorem.** The following hold as $Y\to\infty$.

1. For each fixed real bounded, compactly supported Riemann-integrable $\phi$, put

$$
 \mathcal O_N(\phi)=K^{-1}\sum_p \phi(y_p)\mathbf1_{p\mid N},
 \qquad
 \mathcal O(\phi)=\frac1\lambda\int_{\mathbb R}
                   \frac{\phi(y)}{1+e^{ky}}\,dy .
$$

For each fixed $\epsilon>0$, there is $c_{\phi,\epsilon}>0$ such that

$$
 \mathbb P_{\mathcal F}\big(|\mathcal O_N(\phi)-\mathcal O(\phi)|
                    \ge\epsilon\big)\le e^{-c_{\phi,\epsilon} K}
 \tag{1}
$$

for sufficiently large $Y$. On any fixed bounded $y$ interval the same exponential conclusion holds uniformly for interval discrepancies: the supremum over its subintervals may be put inside the event in (1), with $\phi$ the subinterval indicator.

2. For fixed $B\ge1$, set

$$
 J_N(B)=\sum_{p\le Z^B}
       |\mathbf1_{p\mid N}-\mathbf1_{p\le DZ}|\log p,\qquad
 X_N(B)=\frac{J_N(B)}{Z/\ell},
$$

and define

$$
 \rho=\begin{cases}
 1,&B>1\text{ or }(B=1,\ D<1),\\
 1/2,&B=1,\ D=1,\\
 0,&B=1,\ D>1.
 \end{cases}
$$

For every fixed real $t$,

$$
 \lim_{Y\to\infty}K^{-1}\log\mathbb E_{\mathcal F}
              e^{tK X_N(B)}=G(\rho t),\qquad
 G(t)=\frac1\lambda\int_{\mathbb R}
            \log\frac{1+e^{\lambda t-k|y|}}{1+e^{-k|y|}}\,dy .
 \tag{2}
$$

In particular $X_N(B)$ differs from $2\rho\log 2/k$ by at least any fixed $\epsilon>0$ with probability at most $e^{-c_\epsilon K}$ for a fixed $c_\epsilon>0$ and all sufficiently large $Y$. The half-collar exponent in (2) is $G(t/2)$, **not** $G(t)/2$.

These are conditional empirical or aggregate statements. They do not claim independent prime divisibility on $\mathcal F$ or determine the conditional probability of any prescribed individual prime.

## 1. Upper moment comparison and the local profile

The only prime input is $\vartheta(x)=x+O(xe^{-c_0\sqrt{\log x}})$ from [Johnston–Yang, Corollary 1.2, (1.5)](https://arxiv.org/pdf/2204.01980#page=2). It implies that on every fixed bounded $y$ interval the measure $K^{-1}\sum_p\delta_{y_p}$ tends to $dy/\lambda$, also when tested against bounded Riemann-integrable functions there. In fact $\log p\sim\lambda\ell$ and each such interval $(a,b]$ corresponds to a prime interval of length $(b-a)Z/\ell$, for which the two endpoint errors in $\vartheta$ are $o(Z/\ell)$. Moreover any unit interval of $y$ in a fixed compact interval in $p/Z$ around $D$ has $O(K)$ primes uniformly, by the same estimate.

Use the following parameters, initially with $\gamma=c=0$:

$$
 \sigma_0=1/\lambda,\quad a_0=1-\sigma_0,\quad
 b=\frac{\lambda-\log D}{\lambda^2},\quad
 \sigma=\sigma_0+\frac{\sigma_0}{\ell}+\frac b{\ell^2},\quad
 s_*=\frac{\lambda}{3\mathrm e}D^{a_0}v^{\lambda-1}\ell,\quad
 s=s_* \exp\left(\frac{-\lambda b+\gamma}{\ell}+\frac{c}{\ell^2}\right).
 \tag{3}
$$

Let

$$
 w_p(\sigma)=\log(1+3p^{\sigma-1}),\quad
 V_p=e^{s w_p(\sigma)},\quad \eta_p=s w_p(\sigma)-\log p,\quad
 A_p=1-1/p+V_p/p,\quad T_0=(\sigma Q-M)v.
$$

Positive Rankin majorization shows that every $N\in\mathcal F$ has $\prod_{p\mid N}V_p>e^{sT_0}$. More generally, if a nonnegative marked product is of the form $C\prod_p(1+g_p\mathbf1_{p\mid N})$ with $g_p\ge0$ and constant $C>0$, its integer average on $[Y,2Y]$ is at most $2C\prod_p(1+g_p/p)$. This is the divisor expansion and the bound $2Y/d$ for multiples of $d$ in the interval. One may expand first over primes up to $2Y$ together with the finite marker support and then enlarge the unmarked majorant. No probability model for the integers has been used.

For the local profile use the marker $\exp(\theta\sum_p\phi(y_p)\mathbf1_{p\mid N})$ at any fixed real $\theta$. Multiplying by $\prod_{p\mid N}V_p$ preserves nonnegative divisor coefficients: $V_p e^{\theta\phi(y_p)}\ge1$ on the marker support since $sw_p(\sigma)\sim\lambda\ell$ uniformly there. The logarithmic change in Euler moment from the unmarked one is

$$
 \sum_p\log(1-u_p+u_p e^{\theta\phi(y_p)}),\qquad
 u_p=\frac{V_p}{p-1+V_p}.
$$

At $\gamma=c=0$, the calculation underlying the second-order count gives $\eta_p\to-ky$ uniformly on bounded $y=y_p$ intervals; it is also verified in (6) below. Thus $u_p\to u(y)=(1+e^{ky})^{-1}$ uniformly there. The prime measures just described give the log change divided by $K$ tending to

$$
 H_\phi(\theta)=\frac1\lambda\int_{\mathbb R}
                      \log(1-u(y)+u(y)e^{\theta\phi(y)})\,dy .
$$

Uniform boundedness and Riemann integrability permit this comparison even for discontinuous $\phi$. By the second-order count, at the fixed unmarked parameters the exponent $\sum_p\log A_p-sT_0$ equals $\log(|\mathcal F|/Y)+o(K)$. Consequently

$$
 \limsup_{Y\to\infty}K^{-1}\log\mathbb E_{\mathcal F}
                         e^{\theta K\mathcal O_N(\phi)}
       \le H_\phi(\theta).
$$

Here $H_\phi(0)=0$ and $H_\phi'(0)=\mathcal O(\phi)$ by bounded differentiation on the support. Chernoff's inequality at a sufficiently small fixed positive or negative $\theta$ gives (1), adjusting the positive constant for the two tails. For the uniform subinterval claim, choose a fixed finite mesh of the prescribed compact interval sufficiently fine that every mesh gap has limiting prime measure less than $\epsilon/16$. On grid-node intervals (1) applies simultaneously by a finite union. Any arbitrary subinterval differs from an enclosing grid-node interval only on two mesh gaps and possibly their endpoints; both empirical measures are dominated there by the unconditioned prime counts divided by $K$, and the deterministic limit is likewise dominated by $dy/\lambda$. The PNT bound for the fixed mesh then gives the claimed uniform version with a fixed positive exponent.

## 2. The marked Euler exponent, including the endpoint cutoff

Write $\xi_p=t\log p/\ell$. The literal marker in (2) is $F_N=e^{tJ_N(B)/\ell}$. If $p\le Z^B$ and $p\le DZ$, its local factor is $e^{\xi_p}$ when $p\nmid N$; if $DZ<p\le Z^B$, it is $e^{\xi_p}$ when $p\mid N$. If the prime is unmarked, put $\xi_p=0$ in the corresponding local formula. After multiplying by $\prod_{p\mid N}V_p$, the Euler factors are therefore

$$
 A_p^\natural=
 \begin{cases}
 (1-1/p)e^{\xi_p}+V_p/p,&p\le DZ,\\
 1-1/p+e^{\xi_p}V_p/p,&p>DZ.
 \end{cases}
 \tag{4}
$$

We use either the full marker, or trim it to a fixed compact interval $\mathcal I$ of $p/Z$ around $D$. Choose $\mathcal I$ small enough that $1\notin\mathcal I$ when $B=1,\ D\ne1$. In $\mathcal I$ the low and high sides have constant marked status $m_-,m_+\in\{0,1\}$ respectively. They are $(1,1)$, $(1,0)$ and $(0,0)$ in the three cases of the theorem. The low side includes the endpoint $p=DZ$ if prime; a single endpoint has no effect on the limits below. Thus $\rho=(m_-+m_+)/2$.

In (3) now choose

$$
                   \gamma=\frac{t(m_--m_+)}2 .
 \tag{5}
$$

The parameter $c$ may vary over a fixed bounded interval; the following asymptotics are uniform on such an interval, with $Q,M,B,t$ fixed. Take a sufficiently large fixed $R>2D+1$ and $J_0>6/\sigma_0$ and put $\delta=\ell^{-J_0}$. For $\delta Z\le p\le RZ$ write $x=p/Z$ and $h(x)=(D/x)^{a_0}$. Exactly as in the unmarked expansion, $sw_p=3s p^{\sigma-1}+o(\ell^{-A})$ for any fixed $A$, uniformly on this range. With $u=\sigma_0\log x/\ell$ the linearized ratio is

$$
 \frac{3s p^{\sigma-1}}{\log p}
   =h(x)\frac{e^u}{1+u}e^{\gamma/\ell+(b\log x+c)/\ell^2}.
$$

Its expansion gives

$$
 \frac{\eta_p}{\log p}
 = h(x)-1+\frac{\gamma h(x)}{\ell}
 +\frac{h(x)}{\ell^2}
    \left(\frac{\sigma_0^2}{2}(\log x)^2+
                  b\log x+c+\frac{\gamma^2}{2}\right)
 +O\left(\frac{h(x)(1+|\log x|^3)}{\ell^3}\right)+o(\ell^{-A}).
 \tag{6}
$$

The nonlinear error is indeed smaller than any $\ell^{-A}$ since $\lambda>1$; the fixed power-log factor from $\delta^{-1}$ does not offset $v^{1-\lambda}$. The remainder involving $h$ is summable against $\log p$ with total $O(Z/\ell^3)$ by ratio-two intervals, using the majorants $Z(1+j^3)2^{-j\sigma_0}$ before multiplying by $\ell^{-3}$.

For (4) do not expand a moving positive part. Instead split **exactly** at $p\le DZ$:

$$
 \log A_p^\natural-\mathbf1_{p\le DZ}\eta_p
 =\begin{cases}
 \log(1+(1-1/p)e^{\xi_p-\eta_p}),&p\le DZ,\\
 \log(1-1/p+e^{\xi_p+\eta_p}),&p>DZ.
 \end{cases}
 \tag{7}
$$

On the middle range replacing $1-1/p$ by $1$ in these expressions has total cost $O(\sum_{\delta Z<p\le RZ}1/p)=O(1+\log\ell)$. The local expansion on $\mathcal I$ follows from (6):

$$
  \eta_p=-k y_p+\lambda\gamma+
                   O((1+y_p^2)/\ell),\qquad
 |\eta_p|\ge c_1|y_p|-C_1 .
 \tag{8}
$$

The second bound, with matching signs to $-y_p$ when $|y_p|$ is sufficiently large, follows from the strictly negative derivative of $h$ on the compact $x$ interval and bounded shift $\gamma$. On fixed bounded $y$ intervals $\xi_p\to\lambda t m_\pm$ on the respective marked side. By (5), the exponent on the low side of (7) tends to $ky+\lambda\rho t$ and on the high side to $-ky+\lambda\rho t$. Thus (7), summed and divided by $K$, tends to

$$
 S(\rho t)=\frac1\lambda\int_{\mathbb R}
                     \log(1+e^{\lambda\rho t-k|y|})\,dy.
 \tag{9}
$$

To justify the full integral, use the unit $y$ bins with $O(K)$ primes and, away from a large fixed $y$ interval, exponential bounds from (8) on the corresponding side of (7). Outside $\mathcal I$ within the middle range, $\eta_p$ has the correct sign and magnitude $\gg\ell$ by monotonicity and the signs at the endpoints of $\mathcal I$, while $|\xi_p|=O_{t,B,Q,M}(1)$. The sum of the logarithmic remainders there is $o(K)$ even over all integers.

At $p<\delta Z$, for either marker or no marker, the absolute Euler log is at most $3s p^{\sigma-1}+O_t(1)$, by comparison with the unmarked factor and bounded $p^{t/\ell}$. As in the unmarked bound, its sum is $O(Z\delta^{\sigma_0/2}+\delta Z)=o(K)$ by partial summation. For $p>RZ$, the unmarked tail is $O(Z^{1/4}\ell)=o(K)$: one has $V_p\le Z^{1/4}$ upon choosing $R$ large, and the unmarked difference from one is $\ll Z^{1/4}s p^{\sigma-2}$. The change from high marked primes $RZ<p\le Z^B$, if any, is $O_{t,B}(Z^{1/4}(1+\log Z))=o(K)$ by the integer harmonic majorant. These bounds also hold for real negative $t$ in (4), because the factor is then still positive and the high change from marking is of relative size $O_t(V_p/p)$, which is uniformly small there. In (9) it is therefore enough to sum the middle-range residual and extend the integral.

Now compute the literal prefix $\sum_{\delta Z\le p\le DZ}\eta_p$. Use (6) and partial summation: the normalized weights and their variation on $[\delta,D]$ are fixed powers of $\ell$, hence the prime input at the start of §1 gives an error $o(K)$. The omitted integrals to zero are negligible by integrability of $x^{-a_0}(1+|\log x|^2)$ and the chosen $J_0$. The prefix equals

$$
 Z\int_0^D(h-1)\,dx+\frac{\gamma Z}{\ell}\int_0^D h\,dx
 +K\int_0^D h(x)
  \left(\frac{\sigma_0^2}{2}(\log x)^2+
       b\log x+c+\frac{\gamma^2}{2}\right)\,dx+o(K).
$$

The threshold expansion at (3) is

$$
 sT_0=\lambda DZ\left[
     1+\frac{\gamma}{\ell}
      +\frac{c+\gamma^2/2-\lambda^2 b^2/2}{\ell^2}
      +O(\ell^{-3})\right].
$$

Using $\int_0^D h(x)\,dx=\lambda D$, both new shift terms $\gamma$ and $\gamma^2/2$ cancel in the difference, as does $c$. The remaining sharp-prefix coefficient is $D\lambda/2$: this follows by substituting the two moments $\int_0^D h\log x=\lambda D(\log D-\lambda)$ and $\int_0^D h(\log x)^2=\lambda D((\log D-\lambda)^2+\lambda^2)$ and the value of $b$. Combined with (7)–(9), this proves the uniform marked exponent

$$
             \sum_p\log A_p^\natural-sT_0
                =-DZ+K\big(D\lambda/2+S(\rho t)\big)+o(K).
 \tag{10}
$$

It holds for either trimmed or full marker. It also holds when the $V_p$ factor is restricted to $p\le RZ$ in the product, still allowing markers for $p>RZ$: this changes only the negligible high tail, since each high marked factor with $V_p=1$ differs from one by $O_{t,B}(1/p)$. In the unmarked count $S(0)=\pi^2/(6\lambda k)$, as computed in the second-order theorem.

For the marked upper bound use the full marker when $t\ge0$. Its divisor expansion is nonnegative on the marked low side because there $V_p\ge e^{\xi_p}$: the smallest $V_p$ for $p\le DZ$ is attained at the upper endpoint, where $sw_p\sim\lambda\ell$, while $\xi_p$ is bounded. The high factors are also nonnegative in this expansion when $t\ge0$. For $t<0$, trim to $\mathcal I$. Since the mismatch sum is nonnegative termwise, $e^{tJ_N(B)/\ell}$ is bounded above by the trimmed marker. On its support $V_p\gg e^{|\xi_p|}$ still ensures all divisor coefficients are nonnegative, including those on the high side. Apply the upper moment comparison of §1 and the Rankin threshold on $\mathcal F$ to get

$$
  \frac1Y\sum_{N\in\mathcal F}e^{tJ_N(B)/\ell}
      \le 2\exp\left(\sum_p\log A_p^\natural-sT_0\right).
 \tag{11}
$$

Dividing by the second-order failure count and using (10) proves the upper side of (2), since $G=S-S(0)$ as functions of their argument.

## 3. Strict marked lower bound using true finite residue patterns

For the lower bound use the **full** marker for all real $t$. Set $P=\prod_{p\le\max(RZ,Z^B)}p=Y^{o(1)}$, since $\log P=O_{Q,M,B}(Z^B+RZ)=o(\log Y)$. On uniform even residue classes modulo $P$, let $\mathbb P_0$ be the exact finite probability and $I_p=\mathbf1_{p\mid N}$. The Chinese remainder theorem gives independent inclusion for odd primes with probability $1/p$, and $I_2=1$. Each class has $Y/P+O(1)$ representatives in $[Y,2Y]$, so any nonnegative weighted sum over the finite even patterns agrees with the true counting sum normalized by $Y$ up to the same relative factor $\frac12(1+O(P/Y))$. This is relative even for exponentially small sets: it is checked separately for each residue class before summing nonnegative weights.

Restrict the first tilt to smaller primes:

$$
 L_0=\sum_{p\le RZ}I_p w_p(\sigma),\qquad
 m_0=\sum_{p\le RZ}I_p w'_p(\sigma),
 \qquad
 \frac{d\mathbb P_{t,c}}{d\mathbb P_0}
    =\mathcal Z_{t,c}^{-1}\exp(s L_0+tJ_N(B)/\ell).
 \tag{12}
$$

Here $\mathcal Z_{t,c}$ is the finite normalizer; all terms depend only on the pattern. The forced prime 2 changes the unforced local multiplier by a factor bounded above and below by positive constants, as $V_2\ge1$ and its mismatch weight is bounded. Thus (10), in its version with $V_p$ restricted to $p\le RZ$, gives

$$
 \log\mathcal Z_{t,c}-sT_0=-DZ+
                 K\big(D\lambda/2+S(\rho t)\big)+o(K).
 \tag{13}
$$

It is important that the primes beyond $RZ$ enter only the marker, not $L_0$ or the later divisor measure. Their contribution to this finite log normalizer is $O_{t,B}(1+\log Z)=o(K)$, directly by comparison with the integer harmonic sum.

We verify the two mean and variance estimates needed to match (11) strictly:

$$
 \begin{split}
 \mathbb E_{t,c} L_0&=T_0+O(v/\ell^3),&
 \mathbb E_{t,c} m_0&=Qv+O(v/\ell^2),\\
 \operatorname{Var}_{t,c}(L_0)&\asymp v^{2-\lambda}/\ell^2,&
 \operatorname{Var}_{t,c}(m_0)&\ll v^{2-\lambda}.
 \end{split}
 \tag{14}
$$

The constants may depend on fixed $t$, and the estimates are uniform for $c$ on bounded intervals. Under (12) the indicators remain independent. For odd $p\le RZ$ their inclusion probabilities $u_p^\natural$ are logistic values at

$$
  \widetilde\eta_p=
  \begin{cases}
   \eta_p-\log(1-1/p)-\xi_p,&p\le DZ,\\
   \eta_p-\log(1-1/p)+\xi_p,&p>DZ .
  \end{cases}
$$

On $\mathcal I$ the respective marker statuses are constant. With $\mathfrak L(a)=(1+e^{-a})^{-1}$, (5) and (8) give

$$
 u_p^\natural-\mathbf1_{p\le DZ}
 =\mathfrak L(-k y_p+\lambda\rho t\,\operatorname{sgn}_+(y_p))
       -\mathbf1_{y_p\le0}
 +O_t\left(\frac{(1+y_p^2)e^{-c_2|y_p|}}{\ell}\right),
 \tag{15}
$$

where $\operatorname{sgn}_+(y)=1$ for $y>0$ and $-1$ otherwise. The approximation of the arguments has error $O_t((1+y^2)/\ell)$, and outside a fixed bounded $y$ interval both segments of arguments have magnitude $\gg|y|$ and the sign of $-y$; the logistic derivative gives the exponential saving in the error. The limiting difference is **odd** away from zero. At the half edge this requires exactly the shift (5): without it the two limiting arguments would not be negatives of one another across zero.

For detail on the precision in the signed mean comparison, choose $\mathcal I$ symmetric around $D$ (and still excluding 1 when required). Put $f_0(p)=w_p$, $f_1(p)=w'_p$ and $W_0=v^{1-\lambda}$, $W_1=v^{1-\lambda}\ell$. On $\mathcal I$ the weight $f_j(p)/\log p$ is $O(W_j/\ell)$ with derivative $O(W_j/(Z\ell))$, by direct differentiation. On each half of $\mathcal I$, $\widetilde\eta_p$ is decreasing as a function of real $p$: its unmarked derivative is less than $-1/(p-1)$, and the marker derivative is $O_t(1/(p\ell))$. Thus the logistic probability and the step together have bounded variation, including their one internal jump. Partial summation via the prime input replaces the signed sum on $\mathcal I$ by its integral against $f_j(p)\,dp/\log p$, at error $O(Z e^{-c_3\sqrt{\ell}} W_j/\ell)$. In the integral $dp=Z\,dy/\ell$. Replacing $f_j(p)/\log p$ by its central value costs $O(W_j |y|/\ell^2)$ pointwise, and the constant term integrates the odd main function to zero. With (15) this gives total $O(Z W_j/\ell^3)$. Equality at a single cutoff prime, if present, is harmless in the partial summation or by direct error.

Outside $\mathcal I$ with $\delta Z\le p\le RZ$, the occupation difference from the step is $O_t(e^{-c_4\ell})$, even at any other marker endpoint, by (8), monotonicity of $\eta_p$ and bounded marker shifts. The weights there are $O(W_j\ell^{C_2})$. For $p<\delta Z$, (6) at $x=\delta$ and monotonicity give $\widetilde\eta_p\gg\ell^{1+J_0 a_0/2}$, uniformly despite the bounded marker. Thus the missing probability there is smaller than any power of $v^{-1}$, even summed with $O(Z)$ terms and weights bounded by $O(1+\ell)$. The forced prime 2 gives no difference. This proves that the two means differ from their primorial-prefix counterparts by $O(v/\ell^3)$ and $O(v/\ell^2)$ respectively. These primorial values depend on $\sigma$ alone, not on $s$, hence still are $T_0+O(v/\ell^3)$ and $Qv+O(v/\ell^2)$ by equation (13) and the subsequent expansion of the second-order proof, using the same $b$ in (3).

For the variance of $L_0$, independence gives $\sum_{2<p\le RZ}w_p^2 u_p^\natural(1-u_p^\natural)$. On $\mathcal I$ the weights are $\asymp W_0$ and the probability variances are $O_t(e^{-c_2|y_p|})$; unit bins with $O(K)$ primes prove the upper bound there. The two outer estimates just proved work also with squared weights, including the small-prime bound stronger than all powers of $v^{-1}$, so are negligible even if $v^{2-\lambda}$ tends to zero. In $|y_p|\le1$, the probabilities are uniformly away from zero and one for fixed $t$, and there are $\asymp K$ primes, giving the lower bound $\gg K W_0^2$. This lower comparison can be made eventually with the same constant on every fixed interval of $c$, because the collar limits are independent of $c$; the sufficiently large $Y$ may depend on the interval. Also $w'_p\le(\log p)w_p$, so independence gives $\operatorname{Var}(m_0)\ll\ell^2\operatorname{Var}(L_0)$. This proves (14).

For fixed $Y,t$, varying $c$ does not change the marker or the weights $w_p$. Therefore exactly

$$
        \partial_c\mathbb E_{t,c} L_0
            =\frac{s}{\ell^2}\operatorname{Var}_{t,c}(L_0)
            \gg v/\ell^3.
$$

As at $c=0$ the distance from $T_0$ is $O(v/\ell^3)$, bracket on a sufficiently large fixed interval of $c$ and then choose $c=c(t,Y)$ to tune the mean to $T_0+3v/\ell^4$. The derivative comparison just proved validates this fixed interval even for the moving exact tune. Chebyshev's inequality from (14) gives a pattern event $\mathcal G$ of $\mathbb P_{t,c}$ probability $1-o(1)$ on which

$$
       T_0+2v/\ell^4\le L_0\le T_0+4v/\ell^4,\qquad
       |m_0-Qv|\ll v/\ell^2.
 \tag{16}
$$

On $\mathcal G$ we also require at least half the primes with $D/3<p/Z<D/2$ occupied. All those primes have missing probability $o(1)$ uniformly by monotonicity, fixed-side gap and bounded marker, so this extra condition has probability $1-o(1)$ by Markov's inequality. That interval has $\asymp Z/\ell$ primes.

Here is the strict lower check on the actual positive test. For each good pattern let $P_I$ be the product of its occupied primes up to $RZ$ only, and set $F_I(\sigma')=\sum_{p\mid P_I}w_p(\sigma')$. For any fixed shift window of size $O(\ell^{-3})$ around $\sigma$ one has $F_I''(\sigma')\asymp v\ell$: for the lower bound use the abundant occupied fixed interval just described, with each second derivative $\asymp W_0\ell^2$; the upper bound is $(\log(RZ))\sum_{p\le RZ}w'_p(\sigma')\ll v\ell$ by the same weighted PNT as in the second-order proof. Choose $\Delta=v/\ell^5$. By (16) one may tune $\sigma_I=\sigma+O(\ell^{-3})$ so that $F_I'(\sigma_I)=Qv+\Delta/2$. The initial derivative discrepancy is $O(v/\ell^2)$, so the lower curvature ensures this tune in a fixed sufficiently large shift window. Taylor's formula gives

$$
 F_I(\sigma_I)-\sigma_I Qv=L_0-\sigma Qv+O(v/\ell^5).
$$

On the finite divisor space $r\mid P_I$ tilted by $3^{\omega(r)}r^{\sigma_I-1}$, the variance of $\log r$ is at most $\log(RZ)(Qv+\Delta/2)=O(v\ell)$, because the Bernoulli divisor choices are independent. Hence the **strict** band $Qv<\log r\le Qv+\Delta$ has mass $1-O(\ell^{11}/v)$. Un-tilting this divisor law and keeping only this band gives

$$
 \log\mathcal T_N((\log Y)^Q)
        \ge L_0-\sigma Qv-O(v/\ell^5)
        \ge -Mv+2v/\ell^4-O(v/\ell^5)>-Mv
$$

for every actual $N$ with the good pattern. We used only divisors of $P_I$, so primes outside this product do not alter the lower implication.

Finally undo only the $sL_0$ tilt of the target-pattern law, leaving the marker intact. By (12) and (16),

$$
 \mathbb E_0\big(e^{tJ_N(B)/\ell}\mathbf1_{\mathcal G}\big)
 =\mathcal Z_{t,c}\mathbb E_{t,c}\big(e^{-sL_0}\mathbf1_{\mathcal G}\big)
 \ge \mathcal Z_{t,c}e^{-s(T_0+4v/\ell^4)}(1-o(1)).
$$

CRT counting with relative factor $\frac12(1+O(P/Y))$ now gives a lower bound for the positive weighted count on $\mathcal F$. Its exponent is that in (13), up to $o(K)$ since $s v/\ell^4=O(Z/\ell^3)$. This matches (11) and proves (2). The derivative at zero of $G(\rho t)$ is $2\rho\log 2/k$, by differentiation of the absolutely integrable expression in (2). Using a fixed sufficiently small marker of each sign gives its stated concentration by Chernoff, including the degenerate zero limit. All spaces and tilts in the proof were used either for bounding a nonnegative arithmetic sum or for counting actual finite residue classes, never to assume independent primes on the rare failure set.
