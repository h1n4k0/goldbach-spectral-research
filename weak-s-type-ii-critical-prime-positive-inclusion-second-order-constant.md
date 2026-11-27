# The second-order constant for the positive omission test

This concerns only the positive cutoff diagnostic of the [second-order rarity and occupancy estimate](weak-s-type-ii-critical-prime-positive-inclusion-second-order-occupancy.md). No hypothesis on zeros is used. It does not count failures of the actual signed approximation or bound the signed contribution.

Fix $0<M<Q$. Let

$$
 v=\log\log Y,\qquad \ell=\log v,\qquad
 \lambda=Q/M,\qquad Z=v^\lambda,\qquad
 \sigma_0=1/\lambda,\qquad a_0=1-\sigma_0,\qquad
 D=(M/(3\mathrm e))^\lambda .
$$

For $H=(\log Y)^Q$ set

$$
\mathcal T_N(H)
 =\sum_{\substack{r\mid\operatorname{rad}N\\r>H}}\frac{3^{\omega(r)}}r,
 \qquad
 E=\#\{Y\le N\le 2Y:\ 2\mid N,\ \mathcal T_N(H)>(\log Y)^{-M}\}.
$$

**Theorem.** As $Y\to\infty$,

$$
\log(E/Y)=-DZ+
 D\left(\frac{\lambda}{2}+\frac{\pi^2}{6\lambda(\lambda-1)}\right)
           \frac{Z}{\ell^2}+o_{Q,M}(Z/\ell^2).
\tag{1}
$$

The finite-width transition in the Euler product contributes the term with $\pi^2$; to attain it from below we count actual residue patterns in a finite primorial modulus, rather than use only multiples of a single primorial.

## 1. Expansion of the upper count

Use the quantitative prime number theorem

$$
\vartheta(t)=t+O(te^{-c_0\sqrt{\log t}})
\tag{2}
$$

from [Johnston–Yang, Corollary 1.2, equation (1.5)](https://arxiv.org/pdf/2204.01980#page=2), decreasing the positive constant $c_0$ to absorb a logarithmic factor. Write

$$
 b=\frac{\lambda-\log D}{\lambda^2},\qquad
 \sigma=\sigma_0+\frac{\sigma_0}{\ell}+\frac b{\ell^2},\qquad
 s_*=\frac{\lambda}{3\mathrm e}D^{a_0}v^{\lambda-1}\ell,\qquad
 s=s_*e^{-\lambda b/\ell+c/\ell^2}.
\tag{3}
$$

Here $c$ stays in a fixed bounded interval, to be chosen later; all asymptotics in this section are uniform in such an interval. Define

$$
 w_p=w_p(\sigma)=\log(1+3p^{\sigma-1}),\quad
 t_p=e^{s w_p},\quad A_p=1-1/p+t_p/p,\quad
 \eta_p=sw_p-\log p,\quad T_0=(\sigma Q-M)v .
$$

For large $Y$ we have $0<\sigma<1,\ s>0$. At a failure, positive Rankin majorization gives $\sum_{p\mid N}w_p>T_0$. Since
$\prod_{p\mid N}t_p=\sum_{d\mid N,\ d\ \mathrm{squarefree}}\prod_{p\mid d}(t_p-1)$,
each coefficient is nonnegative. The number of multiples of $d$ in $[Y,2Y]$ is at most $2Y/d$. Summing over all integers for this upper bound yields

$$
 \frac{E}{Y}\le 2\exp\left(\sum_p\log A_p-sT_0\right).
\tag{4}
$$

One can first expand over $p\le 2Y$ and then enlarge the positive majorant to the convergent full product.

We evaluate the exponent in (4). Fix sufficiently large constants $K,R>0$ with $R>2D+1$, and put $\delta=\ell^{-K}$. At $p\le\delta Z$, $\log A_p\le sw_p\le 3s p^{\sigma-1}$. The elementary consequence of (2)
$\sum_{p\le t}p^{\sigma-1}\ll t^\sigma/\log t$
holds uniformly on compact subintervals of $0<\sigma<1$ by partial summation. It shows that the small-prime contribution is $O(Z\delta^{\sigma_0/2})=o(Z/\ell^2)$ when $K>6/\sigma_0$. For $p>RZ$, $sw_p\le 3s p^{\sigma-1}\le\frac14\log Z$ for large $R$, since the ratio of $3s(RZ)^{\sigma-1}$ to $\log Z$ tends to $(D/R)^{a_0}$. Thus $t_p-1\ll Z^{1/4}s p^{\sigma-1}$ here. Summing against $1/p$ even over integers gives $O(Z^{1/4}\ell)=o(Z/\ell^2)$.

On the remaining range put $x=p/Z$ and $h(x)=(D/x)^{a_0}$. There is a uniform expansion

$$
\frac{\eta_p}{\log p}
 =h(x)-1+\frac{h(x)}{\ell^2}B_c(x)
  +O\left(\frac{h(x)(1+|\log x|^3)}{\ell^3}\right)
  +o(\ell^{-J}),\qquad
 B_c(x)=\frac{\sigma_0^2}{2}(\log x)^2+b\log x+c.
\tag{5}
$$

Here $J$ is any fixed positive constant. To verify (5), first use
$w_p=3p^{\sigma-1}+O(p^{2(\sigma-1)})$; after multiplication by $s$, the error is $O(v^{1-\lambda}\ell^{C_1})$ for fixed $C_1$ on this range, hence smaller than all fixed powers of $\ell^{-1}$. With $u=\sigma_0\log x/\ell$, the exact ratio for the linearized term is

$$
 \frac{3s p^{\sigma-1}}{\log p}
 =h(x)\frac{e^u}{1+u}
              e^{(b\log x+c)/\ell^2}.
$$

The factor $e^u/(1+u)=1+u^2/2+O(|u|^3)$, and $|\log x|=O(\log\ell)$, proving the expansion.

The corresponding positive-part sum is

$$
\sum_{\delta Z<p\le RZ}(\eta_p)_+
 = Z\int_0^D(h(x)-1)\,dx
   +\frac{Z}{\ell^2}\int_0^Dh(x)B_c(x)\,dx
   +o(Z/\ell^2).
\tag{6}
$$

Indeed on the fixed compact interval $\mathcal I=[D/2,3D/2]$ the function $h-1$ has strictly negative derivative bounded away from zero. Formula (5) shows agreement of its sign with $\eta_p$ outside $|x-D|\ll\ell^{-2}$. The function $\eta_p$ decreases as a function of the real variable $p$, so signs agree also outside $\mathcal I$. Replacing the positive part by the prefix $p\le DZ$ therefore costs at most $O(Z/\ell^4)$: the possible error is $O(\ell^{-2})$ after dividing by $\log p$, and the total $\log p$ weight in that range is $O(Z/\ell^2)$ by (2). The summed remainder from (5) is $O(Z/\ell^3)+o(Z/\ell^2)$ by ratio-two intervals down to $\delta$: the bound $\vartheta(t)\ll t$ gives the summable majorant $Z(1+j^3)2^{-j\sigma_0}$ for $x\asymp2^{-j}$ before multiplying by $\ell^{-3}$. For the two main terms use Stieltjes integration against (2). The suprema and total variations of their weights on $[\delta,R]$ are bounded by a fixed power of $\ell$, so the prime error is $O(Z\ell^{O(1)}e^{-c_2\sqrt{\ell}})=o(Z/\ell^2)$. Extending the integrals to zero is permissible: the missing integrals are $O(\delta^{\sigma_0}(1+|\log\delta|^2))$, which is more than sufficient for the chosen $K$.

The transition difference from the positive part in (6) has an actual second-order contribution:

$$
 \sum_{\delta Z<p\le RZ}
     \big(\log A_p-(\eta_p)_+\big)
  =\frac{Z}{\ell^2}\frac{\pi^2}{6\lambda k}
     +o(Z/\ell^2),
 \qquad k=\frac{\lambda-1}{D}.
\tag{7}
$$

To see this, first replace $1-1/p$ by $1$ in $A_p$ at total cost $O(\sum_{\delta Z<p\le RZ}1/p)=O(1+\log\ell)$. The summand now is $\log(1+e^{-|\eta_p|})$. On $\mathcal I$, with $y=\ell(x-D)$, (5) and Taylor expansion give, uniformly,

$$
 \eta_p=-ky+O((1+y^2)/\ell),\qquad
 |\eta_p|\ge c_3|y|-C/\ell
\tag{8}
$$

for a fixed $c_3>0$. The second bound uses monotonicity and the negative derivative of $h$ on the entire compact interval, not just Taylor near $D$. In each unit interval of $y$ inside $\mathcal I$, (2) gives $O(Z/\ell^2)$ primes, since the interval in $p$ has length $Z/\ell$ and $\log p\asymp\ell$. Thus, after normalization by $Z/\ell^2$, the tails $|y|>J_0$ are dominated by a summable geometric series in $J_0$. Outside $\mathcal I$ monotonicity gives $|\eta_p|\gg\ell$ (both ends have fixed sign), so that portion is negligible. On every fixed bounded $y$ interval the scaled prime counting measures tend to $(1/\lambda)dy$ by (2) and $\log p/(\lambda\ell)\to 1$ uniformly there. Formula (8) then identifies the limit with

$$
 \frac1\lambda\int_{\mathbb R}\log(1+e^{-k|y|})\,dy
   =\frac{2}{\lambda k}\sum_{j\ge1}\frac{(-1)^{j-1}}{j^2}
   =\frac{\pi^2}{6\lambda k}.
$$

Termwise integration of the series is valid because the integrated absolute coefficients have finite sum. This proves (7).

Since $s_*Mv/\ell=\lambda D Z$, multiplying out the threshold gives

$$
 sT_0=\lambda DZ\left(1+\frac{c-\lambda^2 b^2/2}{\ell^2}
                                  +O(\ell^{-3})\right).
\tag{9}
$$

The main integral of (6) is $(\lambda-1)D$, and $\int_0^D h(x)\,dx=\lambda D$ cancels the $c$ term when (9) is subtracted. The coefficient at $Z/\ell^2$ in the resulting exponent is

$$
 \frac{\sigma_0^2}{2}\int_0^D h(x)(\log x)^2\,dx
 + b\int_0^D h(x)\log x\,dx + \frac{\lambda^3D b^2}{2}
 +\frac{\pi^2}{6\lambda k}.
$$

The two log moments are $\lambda D((\log D-\lambda)^2+\lambda^2)$ and $\lambda D(\log D-\lambda)$, respectively. Substitution of $b$ from (3) gives exactly the coefficient of (1). Thus (1) holds as an upper bound with a remainder $o(Z/\ell^2)$, and the exponent $\sum_p\log A_p-sT_0$ has that expansion for **all** bounded choices of $c$ in (3). The same expansion holds if the Euler product is cut at $p\le RZ$.

## 2. Exact residue patterns and two concentrated sums

Let $P=\prod_{p\le RZ}p=Y^{o(1)}$, the last estimate following from (2) and $Z=(\log\log Y)^\lambda$. On the uniform even residue classes modulo $P$, prime divisibility indicators $I_p$ are independent with $I_2=1$ and $\mathbb P_0(I_p=1)=1/p$ for odd $p\le RZ$, by the Chinese remainder theorem. This is an exact finite experiment. For any set of patterns its fraction of all integers in $[Y,2Y]$, normalized by $Y$, is its $\mathbb P_0$ probability times $\frac12(1+O(P/Y))$, since each residue class has count $Y/P+O(1)$ with uniform relative error. Thus even exponentially rare pattern events in this finite space can be counted in the integer interval without an additive error in their probability.

Write

$$
 L_0=\sum_{p\le RZ}I_p w_p,\qquad
 m_0=\sum_{p\le RZ}I_p w'_p,\qquad
 \mathcal Z=\mathbb E_0 e^{sL_0},
$$

where $w'_p$ is the derivative of $w_p(\sigma)$ in $\sigma$. Tilt the pattern measure to $\mathbb P_c$ by the density $e^{sL_0}/\mathcal Z$. It is still an exact finite product with independent odd-prime occupations of probability

$$
 u_p=\frac{t_p}{p-1+t_p},\qquad I_2=1 .
$$

Also $\mathcal Z=t_2\prod_{2<p\le RZ}A_p$ differs from $\prod_{p\le RZ}A_p$ by a factor in $[1,2]$.

We next prove, uniformly for bounded $c$,

$$
\begin{split}
 \mathbb E_c L_0&=T_0+O(v/\ell^3),&
 \mathbb E_c m_0&=Qv+O(v/\ell^2),\\
 \operatorname{Var}_c(L_0)&\asymp v^{2-\lambda}/\ell^2,&
 \operatorname{Var}_c(m_0)&\ll v^{2-\lambda}.
\end{split}
\tag{10}
$$

The precision of the two means uses the signed transition about $DZ$. We detail it first. In the fixed interval $\mathcal I$ of $x=p/Z$, let $\widetilde\eta_p=\eta_p-\log(1-1/p)$. With $\mathfrak L(t)=(1+e^{-t})^{-1}$, the occupation is $u_p=\mathfrak L(\widetilde\eta_p)$. By (8),

$$
 u_p-\mathbf1_{p\le DZ}
 =\mathfrak L(-ky)-\mathbf1_{y\le0}
    +O\left(\frac{(1+y^2)e^{-c_4|y|}}{\ell}\right).
\tag{11}
$$

For bounded $y$ this follows by the bounded derivative of $\mathfrak L$; for large $|y|$ both logistic arguments have the same sign and size $\gg|y|$ by (8) and the sign conclusion following (5). Thus its derivative on the segment between those arguments is $O(e^{-c_4|y|})$, proving the stated bound on the full compact $x$ interval. The function $\mathfrak L(-ky)-\mathbf1_{y\le0}$ is odd except for its value at zero, and is absolutely bounded by $e^{-k|y|}$. The equality prime at $y=0$, if any, is harmless in the partial summation below.

For $j=0,1$ put $f_0(p)=w_p$, $f_1(p)=w'_p$, and
$W_0=v^{1-\lambda}$, $W_1=v^{1-\lambda}\ell$. On $\mathcal I$,

$$
 f_j(p)\ll W_j,\qquad
 \frac{f_j(p)}{\log p}\ll W_j/\ell,\qquad
 \left|\frac{d}{dp}\frac{f_j(p)}{\log p}\right|
       \ll\frac{W_j}{Z\ell}.
\tag{12}
$$

These follow directly by differentiating $w_p=\log(1+3p^{\sigma-1})$ and $w'_p=(\log p)\,3p^{\sigma-1}/(1+3p^{\sigma-1})$, treating $p$ as a real variable. Since $\widetilde\eta_p=sw_p-\log(p-1)$ decreases, $u_p$ has total variation at most one. The step $\mathbf1_{p\le DZ}$ also has variation at most one. Stieltjes integration against $\vartheta$ thus replaces the prime sum of $f_j(p)(u_p-\mathbf1_{p\le DZ})$ on $\mathcal I$ by its integral in $dp/\log p$, with error $O(Z e^{-c_5\sqrt{\ell}} W_j/\ell)$ by (2) and (12), including endpoint terms. In the integral put $p=Z(D+y/\ell)$. The constant weight $f_j(DZ)/\log(DZ)$ times the first term of (11) integrates to zero on the symmetric interval in $y$. The error in (11) and the Lipschitz error from replacing the weight by that constant, bounded by $O(W_j |y|/\ell^2)$, together cost $O(ZW_j/\ell^3)$.

Outside $\mathcal I$ but with $\delta Z\le p\le RZ$, the mismatch of $u_p$ with the step is $O(e^{-c_6\ell})$ by monotonicity and the two endpoint signs. There $f_j(p)\ll W_j\ell^{C_2}$ for fixed $C_2$, so the same sum over these primes is $o(ZW_j/\ell^3)$ even if bounded using all integers. At $p<\delta Z$ the step is one, and monotonicity with (5) at $x=\delta$ gives $\widetilde\eta_p\gg \ell^{1+K a_0/2}$; even $O(Z)$ such primes with $f_j(p)\ll 1+\ell$ contribute a negligible error. The forced prime 2 has mismatch zero. Thus the full signed differences in both means versus the prefix $p\le DZ$ are $O(ZW_j/\ell^3)$, i.e. $O(v/\ell^3)$ and $O(v/\ell^2)$.

By the weighted PNT and partial summation, uniformly for $\sigma$ near $\sigma_0$, at $z=DZ$,

$$
 m_z:=\sum_{p\le z}w'_p
   =\frac{3z^\sigma}{\sigma}\big(1+O(e^{-c_7\sqrt{\log z}})\big),
 \qquad
 L_z:=\sum_{p\le z}w_p
   =\frac{m_z}{\log z}\left(1+\frac1{\sigma\log z}
                                     +O((\log z)^{-2})\right).
\tag{13}
$$

These are the same weighted PNT estimates used in the preceding rarity bound: the nonlinear corrections to linear prime weights are power smaller by splitting at $\sqrt z$, and the first two endpoint terms for $L_z$ are obtained by twice integrating $\int_2^z t^{\sigma-1}\,dt/\log t$ by parts. Applying the expansion (3) gives

$$
 m_z=Qv\left[1+\frac{\lambda b+\sigma_0(\log D-\lambda)}{\ell}
                      +O(\ell^{-2})\right]=Qv+O(v/\ell^2).
$$

Here $3\lambda \mathrm e D^{\sigma_0}=Q$, and the chosen $b$ makes the displayed correction zero. Substituting in $L_z$ gives

$$
 L_z=\frac{Mv}{\ell}
        +M\left(1-\frac{\log D}{\lambda}\right)\frac{v}{\ell^2}
        +O(v/\ell^3)
     =T_0+O(v/\ell^3).
$$

This and the signed transition comparison prove the first line of (10).

For the variance of $L_0$, use independence and $\sum_{p>2} w_p^2 u_p(1-u_p)$. On $\mathcal I$, $w_p\asymp W_0$ and $u_p(1-u_p)\ll e^{-c_3|y|}$. The unit $y$ bins from (7) give the upper bound $O(ZW_0^2/\ell^2)$. Outside $\mathcal I$ the same exponential bounds and polylogarithmic weights used in the mean comparison apply to $w_p^2$ instead of $w_p$, so give $o(ZW_0^2/\ell^2)$. In particular the guard at $p<\delta Z$ is stronger than any $v^{-J}$, which matters even when $ZW_0^2$ tends to zero. For the lower bound, a fixed interval $|y|\le1$ has $\asymp Z/\ell^2$ primes by (2), and there $u_p(1-u_p)$ is bounded below by a positive constant. This gives $\operatorname{Var}_c(L_0)\asymp ZW_0^2/\ell^2=v^{2-\lambda}/\ell^2$. Since $0\le w'_p\le(\log p)w_p$ and $\log(RZ)\ll\ell$, the variance of $m_0$ is at most $O(\ell^2)\operatorname{Var}_c(L_0)$. This completes (10). The eventual lower comparison constant for $\operatorname{Var}_c(L_0)$ can be chosen independent of any fixed bound on $|c|$, since the fixed-$y$ limit (8) and the main comparison $w_p\asymp W_0$ there have leading constants independent of $c$; the size at which the bound holds may depend on that bound.

## 3. Strict lower count at the same exponent

For fixed $Y,\sigma$, the dependence on $c$ of the tilted mean of $L_0$ is only through $s$. The finite measure identity

$$
 \frac{\partial}{\partial c}\mathbb E_c L_0
       =\frac{s}{\ell^2}\operatorname{Var}_c(L_0)
       \gg v/\ell^3
\tag{14}
$$

follows by differentiating $\mathcal Z$ and (3), using (10). At $c=0$, the distance from $T_0$ is $O(v/\ell^3)$. The lower comparison in (14) has the same eventual constant on every fixed bounded interval as just noted. Choose a sufficiently large fixed $C>0$, and take $Y$ sufficiently large for (14) on $[-C,C]$. The mean then brackets $T_0+3v/\ell^4$, and by continuity we can fix $c=c(Y)$ in this interval so that

$$
                       \mathbb E_c L_0=T_0+3v/\ell^4 .
$$

With this choice there is a pattern event of $\mathbb P_c$ probability $1-o(1)$ on which

$$
  T_0+2v/\ell^4\le L_0\le T_0+4v/\ell^4,\qquad
  |m_0-Qv|\le C_3v/\ell^2,
\tag{15}
$$

and at least half the primes with $D/3<p/Z<D/2$ are occupied. Indeed the two Chebyshev estimates from (10) are $O(\ell^6/v^\lambda)$ and $O(\ell^4/v^\lambda)$, taking $C_3$ larger than the uniform mean-error constant. In the fixed lower interval the occupation misses only an $o(1)$ fraction in expectation by monotonicity and (5), hence at most half with high probability by Markov's inequality. That interval has $\asymp Z/\ell$ primes by (2).

For any pattern satisfying (15) and the fixed-interval occupancy, let $P_I$ be the product of its occupied primes, and let

$$
 F_I(\sigma')=\sum_{p\mid P_I} w_p(\sigma').
$$

For $\sigma'$ in any fixed multiple of $\ell^{-3}$ around $\sigma$ we have

$$
                  F_I''(\sigma')\asymp v\ell .
\tag{16}
$$

For the upper bound, each second derivative is at most $(\log(RZ))w'_p(\sigma')$, and the sum over all primes up to $RZ$ is $O(v)$ by the weighted prime estimate as in (13). For the lower bound sum over the occupied fixed interval of primes just obtained: there $w_p''(\sigma')=(\log p)^2 3p^{\sigma'-1}/(1+3p^{\sigma'-1})^2\asymp\ell^2 W_0$, and at least $\gg Z/\ell$ primes are occupied. The eventual lower constant is uniform for shifts up to any fixed multiple of $\ell^{-3}$.

Set $\Delta=v/\ell^5$. From (15), (16) and the intermediate value theorem we can choose $\sigma_I=\sigma+O(\ell^{-3})$ with
$F_I'(\sigma_I)=Qv+\Delta/2$ exactly. The constant in the shift is fixed and uniform on the good patterns: the first derivative at $\sigma$ differs from the desired value by $O(v/\ell^2)$, and the second derivative is $\gg v\ell$ throughout a sufficiently large fixed shift window. Taylor's formula gives

$$
 F_I(\sigma_I)-\sigma_I Qv
       = L_0-\sigma Qv+O(v/\ell^5),
\tag{17}
$$

since the initial derivative of $F_I(\sigma')-\sigma'Qv$ is $O(v/\ell^2)$ and its second derivative is $O(v\ell)$.

In the auxiliary divisor space $r\mid P_I$, use the probability proportional to $3^{\omega(r)}r^{\sigma_I-1}$. Its normalizer is $\exp F_I(\sigma_I)$, and its mean of $\log r$ is the tuned value $Qv+\Delta/2$. Independence of its divisor prime selections gives variance at most $\log(RZ)(Qv+\Delta/2)=O(v\ell)$. The strict band $Qv<\log r\le Qv+\Delta$ therefore has probability $1-O(\ell^{11}/v)$ uniformly, including the strict lower endpoint. Every actual integer with this pattern has $P_I\mid\operatorname{rad}N$. By un-tilting in this divisor space and keeping only the strict band,

$$
\begin{split}
 \log\mathcal T_N(H)
  &\ge F_I(\sigma_I)-\sigma_I(Qv+\Delta)
                          +\log(1-O(\ell^{11}/v))\\
  &\ge L_0-\sigma Qv-O(v/\ell^5)\\
  &\ge -Mv+2v/\ell^4-O(v/\ell^5)>-Mv
\end{split}
\tag{18}
$$

for large $Y$. We have used no primes outside $P_I$ in this lower bound. In particular every good pattern in (15) forces a strict failure of the original positive test.

Finally un-tilt the **target pattern** law, distinct from the divisor law in (18). If $\mathcal G$ is the good event, then

$$
 \mathbb P_0(\mathcal G)
   =\mathcal Z\,\mathbb E_c(e^{-s L_0}\mathbf1_{\mathcal G})
   \ge\mathcal Z e^{-s(T_0+4v/\ell^4)}(1-o(1)).
$$

The CRT count converts this probability to a lower bound for $E/Y$ with factor $\frac12(1+O(P/Y))$. The cost $O(sv/\ell^4)=O(Z/\ell^3)$ is $o(Z/\ell^2)$, and $\log\mathcal Z=\sum_{p\le RZ}\log A_p+O(1)$. Hence the lower count has the same expansion as the upper exponent in §1, even though $c=c(Y)$ was selected there to enforce the strict margin. This proves (1). No description of individual prime occupancy, signed transport, or the full arithmetic error is part of this theorem.
