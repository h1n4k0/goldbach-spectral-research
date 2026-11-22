# A least-prime gain for the genuine sharp midpoint remainder

**Scope.** The previous [deeper less-rough midpoint bound](spectral-midpoint-deeper-less-rough-high-shell.md) controlled both actual sharp-cut LCM terms above $\exp((\log N)^\alpha)$ for fixed $\alpha>3/4$. A pointwise Lipschitz identity in the least prime of the partner now improves the true critical-divisor restoration for **both parities**. Together with the genuine circle model it lowers the threshold to $\exp((\log N)^{2/3}(\log\log N)^\kappa)$ for any fixed $\kappa>1/3$. The new intervening shell has negligible **signed** low and high contributions. The endpoint restoration inequality is individually uniform in $N$; the signed asymptotics are only almost all. Neither the remaining lower thresholds nor Hypothesis S are settled.

Let even $N\in[X,2X]$, $L=\log N$, $\ell=\log X$, $m=N-n$, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Let $\Sigma(N)$ be the usual binary singular series. Keep the original half-open central cells $I\subset(N/2,9N/16]$ of length $H=N/(16\lceil L^J\rceil)$, $J\ge1$ fixed, and the original sharp cutoff $D=\sqrt N L^{-B}$, $B>0$ fixed. Define $F_{0,D},F_{1,D}$ as in the earlier midpoint notes, with respective weights $\mu(d)$ and $\mu(d)(1-2\log d/\log m)$ for $d\mid m$, $d\le D$. Write $F_0,F_1$ for the full midpoint versions $d<\sqrt m$, and

$$
 G_D=F_{0,D}F_{1,D}-F_{0,D},\qquad G=F_0F_1-F_0 .
$$

The [exact low-LCM calculation](spectral-midpoint-lcm-complement-frontier.md) identifies $F_{0,D}$ and $G_D$ with the respective portions of the original mixed product at LCM $\le D$ and $>D$. For a threshold $z$ denote their true $\lambda$-sums on squarefree $m$ with $P^-(m)\ge z$ by $\mathcal L_z(I)$ and $\mathcal H_z(I)$.

Fix $\kappa>1/3$ and put $z_\kappa(N)=\exp(L^{2/3}(\log L)^\kappa)$. For every fixed $A_0>0$, outside one set of $O_{\kappa,B,J,A_0}(X\ell^{-A_0})$ even moduli, uniformly in all their cells,

$$
 \begin{split}
 |\mathcal L_{z_\kappa(N)}(I)|
      &\ll \frac{\Sigma(N)H}{L}(\log L)^{1-3\kappa},\\
 \mathcal H_{z_\kappa(N)}(I)
      &=\frac{\Sigma(N)H}{L}
          +O\!\left(\frac{\Sigma(N)H}{L}(\log L)^{1-3\kappa}\right).
 \end{split}                                                     \tag{1}
$$

Constants may depend on the fixed parameters above. Therefore for every fixed $a\in(3/4,1)$ the actual signed low and high contributions on $z_\kappa(N)\le P^-(m)<\exp(L^a)$ are both bounded by the error in (1), by subtracting the two true sharp-cut evaluations. The shell conclusion also holds without the squarefree gate, as noted at the end. There is no bound for its absolute mass.

## 1. A pointwise least-prime derivative gain

On a squarefree $m$ with a prime divisor $p$, pair the divisors $d\mid m/p$ with $pd$. For $f(x)=(1-2x/\log m)_+$, the full centered weight gives exactly

$$
 F_1(m)=\sum_{d\mid m/p}\mu(d)\big(f(\log d)-f(\log d+\log p)\big),
 \qquad |F_1(m)|\le \tau(m)\frac{\log p}{\log m}.                \tag{2}
$$

Indeed $f$ is $2/\log m$-Lipschitz on $[0,\infty)$, and $\tau(m/p)=\tau(m)/2$. The positive part correctly includes the moving midpoint because its value there is zero. This holds for either total Möbius sign; the odd composite case has $F_1=0$ already.

Let $E_j=F_j-F_{j,D}$ and $K_D(m)=\#\{d\mid m:D<d<\sqrt m\}$. Uniformly for $m$ in the central range,

$$
 |E_0|\le K_D(m),\qquad
 |E_1|\ll_B \frac{1+\log L}{L}K_D(m).
$$

The second estimate uses $0\le 1-2\log d/\log m\le 2B\log L/\log m$ for $d>D$. The exact difference of high weights is

$$
       G_D-G=E_0(1-F_1)-F_{0,D}E_1.                            \tag{3}
$$

Hence, taking $p=P^-(m)$, their error plus the low error is at most

$$
 O_B\!\left(K_D(m)\left[1+\tau(m)
          \left(\frac{\log P^-(m)}{L}+\frac{1+\log L}{L}\right)\right]\right).
                                                                    \tag{4}
$$

This uses $\log m=L+O(1)$ and $|F_{0,D}|\le\tau(m)$. In particular the even class is not omitted: there $F_0=G=0$ for a composite, and (3) gives exactly its remaining cut contribution. The factor in (2), not a parity assumption on the sequence of shifted primes, controls it.

## 2. Uniform genuine critical-incidence bounds and summation

For $L^{1/2}\le t\le L/1000$ put $z=e^t$, $b=t/L$. Define

$$
 E^{(j)}(z)=\sum_{\substack{n\in I\\m\ {\rm squarefree},\,P^-(m)\ge z}}
                    \lambda(n)\tau(m)^j K_D(m),\qquad j=0,1 .
$$

Uniformly in this range and in every even $N$,

$$
 \begin{split}
 E^{(0)}(z)&\ll_B
      \frac{\Sigma(N)H(1+\log L)}{b^2 L^2}+N^{3/4}L^2,\\
 E^{(1)}(z)&\ll_B
      \frac{\Sigma(N)H(1+\log L)}{b^4 L^2}+N^{.88}L^3 .
 \end{split}                                                     \tag{5}
$$

Here are the uniformity details needed for using (5) across varying cutoffs. For a rough modulus $q\le N^{4/5}$ coprime to $N$, the genuine arithmetic mass of $q\mid m$ with rough $m/q$ is, by the [cofactor sieve used earlier](spectral-midpoint-deeper-less-rough-high-shell.md),

$$
 \ll \frac{\Sigma(N)H}{bL\varphi(q)}+L^2(H/q)^{1/2}.
$$

The cofactor interval has length $U=H/q$, the sieve cutoff is $Y=U^{1/100}>z$ since $\log U\ge(1/5-o(1))L$ and $b\le1/1000$, and the root counts and CRT errors are uniform. Mertens gives the rough conditional Euler factor $\ll\Sigma(N)/\log z$. The reciprocal sum of rough $a\le N$ with weight $1/\varphi(a)$ is $O(b^{-1})$ by the positive Euler product. Also $d/\varphi(d)\le2$ on rough $d\le N$, since the number of factors is at most $L/t$ and they are all $\ge e^t$.

On a dyad $R\le d\le2R$ intersecting $(D,\sqrt N]$, the dimension-one upper sieve at $z^{1/3}$ counts rough $d$ by $O(R/(bL)+R^{1/2})$. Its parameter is bounded below by one because $R\gg\sqrt N L^{-B}$ and $b\le1/1000$. Thus the reciprocal mass $\sum 1/\varphi(d)$ in the whole critical band is $O_B((1+\log L)/(bL))$. For the $\tau(d)$-weighted reciprocal mass, expand by the divisor hyperbola, forcing a rough divisor $u\le\sqrt{2R}$, and use the same upper sieve on the cofactor in its interval of length $R/u$. The resulting unweighted-in-$d$ bound is $O(R/(b^2L)+R^{3/4})$ for the $\tau(d)$-mass in the dyad, since $\sum_{u\ {\rm rough}}1/u\ll b^{-1}$. Divide by $R$ and sum dyads to get $O_B((1+\log L)/(b^2L))$ for the weighted reciprocal mass. For $E^{(0)}$ use $q=d$ and the first reciprocal sum. For $E^{(1)}$ write $\tau(m)\le\tau(d)\tau(m/d)$, expand the second factor by the divisor hyperbola, and force a rough $a\le\sqrt{m/d}\le N^{.26}$ in the cofactor. Now $q=da\le N^{.76}$; $1/\varphi(da)\le1/(\varphi(d)\varphi(a))$. This adds $O(b^{-1})$ to the main bound for the weighted reciprocal mass. The errors sum using $\sum_{d\le\sqrt N}\tau(d)d^{-1/2}\ll N^{1/4}L$ and $\sum_{a\le N^{.26}}a^{-1/2}\ll N^{.13}$, giving the second error in (5); dropping $\tau(d)$ and $a$ gives the first. Thus (5) is available at every threshold required here, not only at a fixed power.

Now fix $t_0$ in the range of (5) and let $t_j=2^j t_0$. Partition the partners with $\log P^-(m)\ge t_0$ into the shells $t_j\le\log P^-(m)<2t_j$, stopping at the first $t_{j_*}\in[L/2000,L/1000]$ if $t_0<L/2000$; the last shell is the entire tail above $t_{j_*}$. If $t_0\ge L/2000$, there is just the tail. On a finite shell the factor $\log P^-(m)/L$ in (4) is $O(b_j)$, $b_j=t_j/L$, and the same is true with an absolute larger constant on the terminal tail, since $b_{j_*}\ge1/2000$ and $\log P^-(m)\le L$. Bound each shell's arithmetic mass by the corresponding tail in (5). Since $t_j\gg1+\log L$, the $E_1$ weight in (4) is also $O(b_j)$. The tail estimates yield per shell

$$
 \ll_B \frac{\Sigma(N)H(1+\log L)}{b_j^3 L^2}
             +O_B(N^{.88}L^3).
$$

The first bound sums geometrically to the contribution at $b_0=t_0/L$, and the number of shells is $O(1+\log L)$. In particular

$$
 \sum_{\substack{n\in I\\m\ {\rm squarefree},\,\log P^-(m)\ge t_0}}
     \lambda(n)\bigl(|F_{0,D}-F_0|+|G_D-G|\bigr)
  \ll_B \frac{\Sigma(N)H(1+\log L)L}{t_0^3}+N^{.89}L^3 .        \tag{6}
$$

This is the all-modulus true endpoint bound; it improves the former $b_0^{-4}$ by one factor $b_0$ without changing the cut.

## 3. Full midpoint models at the new threshold

Freeze $z=e^t$ on the dyad at $t=\ell^{2/3}(\log\ell)^\kappa$, $b=t/\ell$, and use the full genuine coefficients $F_0$ and $G$ only on squarefree partners with $P^-\ge z$. The Fourier and density proof is that of the [deeper less-rough shell](spectral-midpoint-deeper-less-rough-high-shell.md), with the following exact parameter checks. Each coefficient has modulus at most $\tau(m)$: for $G$ use $G=-F_0$ on odd squarefree composites and $G=0$ otherwise. Its torus squared norm on $m\in[X/3,2X]$ is $O(X\ell^3)$. The exact largest-prime decomposition applies, with signed count and variation $O(\tau(c))$ for each cofactor prefix $c$, because each divisor gives only one jump in each of the two midpoint conditions. The positive sum $\sum_c\tau(c)^j/c\ll_j b^{-2^j}$ still holds by the Euler product for squarefree $c$. Thus the model density has supremum and total variation $O((b^3\ell)^{-1})$.

In the final prime interval the logarithm of the underlying scale $X/c$ is at least $t-O(1)$ on its support. A fixed polylogarithmic arc denominator remains below a fixed power of that logarithm. The [Siegel--Walfisz](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF) error is exponential in $\sqrt t$; with the same signed intervals and cofactor weights it gives any prescribed fixed inverse-log saving. The [Vaughan](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=77) minor bound on the first prime, the divisor $L^2$ bound above, and the same polylogarithmic physical cell cover give $O_{A_0}(X\ell^{-A_0})$ exceptions at raw error $O(H/L^2)$. In the major computation the Ramanujan tail is controlled over the same dyad by $O(XQ^{-1/2})$ in absolute sum, as before, and Fourier inversion uses the displayed total variation. The parameters $b^{-1}=O(\ell^{1/3})$ and $(b^3\ell)^{-1}=O((\log\ell)^{-3\kappa})$ are harmless at arbitrarily large fixed polylogarithmic arc budget. Finally the cell endpoint replacement uses $\sum_{m\in U}\tau(m)\ll |U|\log X+\sqrt X$, not a uniform bound $2^{O(1/b)}$. Consequently the true weighted sums have the previous continuum integrals times $\Sigma(N)$ with error $O(\Sigma(N)H/L^2)$ in every cell of the common good set.

The only potential additional problem is the dimension-growing prime-exponent grid. Here the factor count is at most $K=\lfloor2/b\rfloor$, and take grid mesh $\Delta=\exp(-\ell^{1/3})$. The binned reciprocal prime measure differs from $dt/t$ on the exponent range in total variation by $O(\Delta^{-1}\exp(-c\sqrt t))$, because the interval-by-interval unbinned discrepancy is $O(\exp(-c\sqrt t))$ from the quantitative prime number theorem. The number of fixed linear walls, the possible magnitudes of signed coefficients, and the tensor product masses together amplify both strip and bin errors by at most

$$
 \exp\big(O(K\log(2+\log(1/b))+K+\log(1/b))\big)
             =\exp(o(\ell^{1/3})).
$$

Indeed $K=O(\ell^{1/3}(\log\ell)^{-\kappa})$ and $\kappa>0$. On each wall use the same continuous strip bound $O(K\Delta/b)(O(1+\log(1/b)))^{k-2}$ in dimension $k-1$, by integrating one coordinate with nonzero bounded-below coefficient. The bins touching it enlarge its width by at most the same order. Off the walls the reciprocals vary by $O(K\Delta/b^2)$, with signed amplitudes at most $2^K$. These checks include ordering diagonals and the exact midpoint subset cuts. Since $\sqrt t=\ell^{1/3}(\log\ell)^{\kappa/2}$, the decay in the binned error still dominates all these losses. The total error in the signed simplex densities is therefore smaller than every prescribed negative power of $\ell$, uniformly in the physical coordinate $x\in[X/3,2X]$.

Scaling the simplex from total mass $\xi=\log x/\ell$ to one gives the original [Dickman constants](spectral-midpoint-complementary-blocks-moving-roughness.md) $\varepsilon_{b/\xi}$ and $1-\varepsilon_{b/\xi}$ times the scale $\xi^{-1}$. The factorial bound on $\varepsilon$ is smaller than every prescribed inverse power of $\ell$ since $b^{-1}$ grows as a positive power up to logarithms. Thus the low continuum density is negligible to every inverse-log power and the high density is $1/\log x+O(\ell^{-2})$. This proves full midpoint low $O(\Sigma H/L^2)$ and full midpoint high $\Sigma H/L+O(\Sigma H/L^2)$ at the frozen threshold, on all the asserted good moduli.

## 4. Return to the actual cutoff and the intervening shell

The function $u^{2/3}(\log u)^\kappa$ is increasing eventually and has derivative tending to zero, so the frozen and actual rough thresholds have ratio at most two for $N\in[X,2X]$. For this change, the genuine discrepancy is supported where $r\in[z,2z]$ is a prime divisor and $m/r$ remains rough. For the full test weights, bounded by $\tau(m)$, apply the same cofactor hyperbola argument as in Section 2 to $m/r$. Its small divisor $a$ satisfies $a\le\sqrt N$ and $ra\le N^{.51}$ eventually; the sum of $1/\varphi(r)$ over the narrow prime interval is $O(1/(bL))$, and the sum over rough $a$ is $O(b^{-1})$. Thus this change costs $O(\Sigma H/(b^3L^2)+N^{.76}L^2)$, where the powers follow from the same CRT sum as in (5). It is smaller than the bound in (1).

For the actual $D$ cutoff take $t_0=L^{2/3}(\log L)^\kappa$ in (6). The main error there is exactly $O(\Sigma H L^{-1}(\log L)^{1-3\kappa})$, and the power error is negligible uniformly in the cells. This proves (1). Intersecting its good moduli with those of the previous sharp-cut theorem at a fixed $a>3/4$ proves the actual signed shell statement. The moving threshold is smaller than $\exp(L^a)$ for large $N$ and the previous relative error is a negative power of $L$ up to logs, smaller than this relative error.

The squarefree condition may be removed from the shell because any rough nonsquarefree partner has a square divisor $p^2$ with $p\ge z_\kappa(N)$, so there are $O(N/z_\kappa(N))$ of them. With cut weights $O(\tau(m)^2)$, Cauchy--Schwarz and $\sum_{m\le N}\tau(m)^4\ll NL^{15}$ bound their true prime-position mass by $O(NL^{17/2}/\sqrt{z_\kappa(N)})$. The argument gives no analogous deletion for the remaining lower-roughness high block.
