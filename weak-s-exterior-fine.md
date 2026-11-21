# A fine-side reduction for the doubly exterior Hardy block

This result concerns the actual operator $T_N=P_N-D_N-K_N$ from [Li–Liu](https://mrc.sdu.edu.cn/english/info/1018/1514.htm), under local Dirichlet GRH at the even modulus $N$. It does not discard the full exterior. It controls every block with two exterior arguments and at least one argument orthogonal to a specified set of local mean directions.

Put $L=\log N$, $\alpha=L^{-1}$, $\beta=1/8$, and
$$
 r(u)=u^{-3/2}\big((Nu)^{-2\alpha}+(Nu)^{-2\beta}\big)^{1/2},
 \qquad Q_Y=\mathbf 1_{u\ge Y}.
$$
All projections are in the unitary physical realization on $L^2(du)$. Fix $K,\epsilon>0$ and $0\le\vartheta<1$. Write $\ell=\log L$, and assume
$$
 \log Y\ge H_0=(K+3)\ell^2/\log\ell.
$$
For $V=2^jY$, $j\ge0$, partition $[V,2V)$ into cells of length
$$
 d_V=\left\lfloor V^{1/2}(NV)^{\vartheta/L}L^{-K-2-\epsilon}\right\rfloor
$$
and at most one shorter last cell. Let $\Pi$ project onto the orthogonal sum of the lines $\mathbb C r\mathbf 1_I$ over these cells and put $E=Q_Y-\Pi$. Then
$$
 \|Q_Y T_NE\|_{\mathrm{HS}}+\|E T_NQ_Y\|_{\mathrm{HS}}=o(L^{-K}),
 \qquad
 \|Q_Y T_NQ_Y-\Pi T_N\Pi\|_{\mathrm{HS}}=o(L^{-K}).
 \tag{1}
$$
The estimates are uniform in $Y$ in the stated range. The grid uses $O(V/d_V+1)$ mean profiles per dyadic shell.

## Character covariance

The [physical Volterra realization](r20-operator.md) writes $P_N$ as the average of rank-one maps $p_\chi\otimes p_\chi$ over odd characters modulo $N$, where
$$
 p_\chi(u)=-\frac{\sqrt{2\pi}}{N}\,r(u)\sum_{m\le Nu}\Lambda(m)\sqrt m\,\chi(m).
$$
In the original Hardy norm $\operatorname{tr}P_N\ll L^2$ by [Li–Liu, Proposition 6.5](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf). Freeze the prefix sum at the left end $a$ of a cell $I$. This gives a particular multiple of the coarse profile there, so the squared projection error is at most the squared error from the increment over $(Na,Nu]$. For any nonnegative numbers $z_m$ supported on the units of that interval, odd orthogonality gives
$$
 \operatorname{Avg}_{\chi\ {\rm odd}}\left|\sum_m z_m\chi(m)\right|^2
 =\sum_{m\equiv n\ (N)}z_mz_n-\sum_{m\equiv -n\ (N)}z_mz_n
 \le (d_V+1)\sum_m z_m^2.
$$
The subtracted sum is nonnegative. In the remaining sum each residue has at most $d_V+1$ terms, which gives the last inequality by Cauchy–Schwarz. Apply this to $z_m=\Lambda(m)\sqrt m$ on the unit increment. On a shell $r(u)^2\ll V^{-3}(NV)^{-2\alpha}$. Enlarge each increment to the cell's half-open raw interval and integrate over its physical length, at most $d_V$. Those terminal raw intervals are disjoint up to the assigned endpoints. The Chebyshev bound $\sum_{m\le 2NV}m\Lambda(m)^2\ll (NV)^2\log(2NV)$ therefore yields
$$
 \operatorname{Avg}_\chi\|Ep_\chi\|_{L^2([V,2V))}^2
 \ll \frac{d_V(d_V+1)}{V}(NV)^{-2\alpha}\log(2NV).
$$
For large $N$, $1\le d_V\le V/2$: the expression floored grows with $V$, its ratio to $V$ decreases, and $e^{H_0/2}$ dominates every fixed power of $L$. After inserting $d_V$, the remaining shell sum is
$$
 \sum_{j\ge0}\log(2N2^jY)(N2^jY)^{-2(1-\vartheta)/L}\ll_\vartheta L^2 .
$$
Indeed, for $z=\log(N2^jY)$ the summand is $O_\vartheta(L e^{-(1-\vartheta)z/L})$. Thus $\operatorname{Avg}\|Ep_\chi\|^2\ll L^{-2K-2-2\epsilon}$. The rank-one HS identity and Cauchy–Schwarz against $\operatorname{tr}P_N$ give $\|P_NE\|_{\rm HS}\ll L^{-K-\epsilon}$.

## Diagonal and Beta benchmark

Use the log coordinate $x=\log u$, set $H=\log Y$, and let $m(x)=((Ne^x)^{-2\alpha}+(Ne^x)^{-2\beta})^{1/2}$. The [published stationary benchmark](operator-post-r15-stationary-tail.md) identifies $D_N+K_N$ on $x,y\ge H$ with the kernel $m(x)k_N(x-y)m(y)$ plus a diagonal RH error and a shifted Mellin integral. Its normalization is
$$
 k_N(v)=\int_{\mathbb R}e^{itv}
 \frac{L-\log\pi-\sum_{p\mid N}\log p/(p-1)+\Re\psi(3/4+it/2)}
      {1+t^2}\,dt ,
 \qquad \psi=\Gamma'/\Gamma.
$$
The published argument for fixed contours must be made uniform here. Choose $\kappa=(\log\ell)/\ell$. In the joint Mellin variable $w$, the shift to $\Re w=-\kappa$ crosses the same residue at $0$ as in the stationary calculation. The shifted factor is $\pi^w\zeta(1-w)\zeta(1+w)A_N(w)$, with $A_N$ as in the benchmark. Good Euler factors are $1+O(p^{-2+2\kappa})$ and the factor at two is bounded. The primes dividing $N$ cost at most
$$
 \exp\left(O\!\left(\sum_{p\mid N}(p^{-1}+p^{-1+\kappa})\right)\right)=L^{o(1)}.
$$
For $p>L$, there are at most $L/\log L$ such prime divisors, and each $p^{-1+\kappa}\le \ell/L$. For $p\le L$, Chebyshev and partial summation bound the sum by $O(1+\int_1^\ell e^{\kappa v}dv/v)=O(\log\ell+\ell/\log\ell)=o(\ell)$. The zeta factors are $O(\kappa^{-1})$ and $O(\kappa^{-1}(2+|\Im w|)^\kappa)$ by the series and Euler summation respectively. Each Gamma-ratio factor including $1/(1+s)$ is $O((1+|\Im s|)^{-1+\kappa/2})$ at $\Re s=-\kappa/2$, uniformly by Stirling. Hence the squared joint height integrand is bounded, up to $L^{o(1)}$, by a product of factors $(1+|t|)^{-2+3\kappa}$, each integrable uniformly. The shift can be made against compact smooth tests as in the benchmark, then extended by two-dimensional Plancherel. The multiplier $e^{-\kappa(x+y)/2}$ on the shifted inverse gives HS error $O(L^{o(1)}e^{-\kappa H})=O(L^{-K-3+o(1)})$. The separately published diagonal error $O(N^{-1/2}e^{-H/2}(L+H)^3)$ is negligible uniformly.

## Projecting the benchmark

On the log cell $J=\log I$ the coarse profile is $\rho(x)=e^{-x}m(x)$. Its logarithmic derivative is bounded by $1+\beta$, and the largest log-cell width satisfies
$$
 \Delta\ll L^{-K-2-\epsilon}Y^{-1/3}.
$$
For $f\in H^1(J)$, approximate it by $\rho$ times the ordinary average of $f/\rho$ on $J$. Interval Poincaré and the bounded variation of $\log\rho$ across the cell show
$$
 \|E_Jf\|_{L^2(J)}\ll |J|\big(\|f'\|_{L^2(J)}+\|f\|_{L^2(J)}\big).
$$
The displayed convolution multiplier gives $\|k_N\|_{H^1(\mathbb R)}\ll L$, since its numerator is $O(L+\log(2+|t|))$. Both $m$ and $m'$ are bounded on $x\ge H$ and $\int_H^\infty m(y)^2dy\ll L$. Apply the cell inequality inside each cell to $f(x)=m(x)k_N(x-y)m(y)$ and integrate the square in $y$. This gives the benchmark HS error on a fine side $O(L^{3/2}\Delta)$; no derivative across the exterior boundary is used. Combine this with the contour and character errors. Self-adjointness gives the estimate for either fine side, and $Q_Y T_NQ_Y-\Pi T_N\Pi=E T_NQ_Y+\Pi T_NE$ gives (1).

This leaves the actual mean–mean operator $\Pi T_N\Pi$, and the crossing between the exterior and its complement, uncontrolled. The result is at inverse-logarithmic precision, not the refuted R scale and not a proof of weak S.
