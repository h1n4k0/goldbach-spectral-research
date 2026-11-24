# The short-prime Euler profile gives a sign reversal on the true carrier

Use the full prescribed both-parity carrier of the [product-boundary obstruction](r78-source-positive-first-moment-past-product-boundary.md), at the same fixed polynomial split $Z=X^{\delta_0}$ and with all its size, total-count, genuine exceptional-count, unit and interval masks. In particular $n=hF\in\mathcal J$, $h=sWU$, and $m=kG\in\mathcal J$, $k=s'W'U'$; the old primes obey $\log s/T,\log s'/T\in[5/4,7/4]$, and $N\in\mathcal X=[X,(1+\Delta)X]$. Write $L=\log X$, $\ell=\log L$, $T=L/\ell$ and $T_N=\log N/\log\log N$. The actual distinguished primes satisfy $F\ge\sqrt N e^{-aT_N}$ and $G\ge\sqrt N e^{-bT_N}$ with fixed

$$
                  0<a,b<20,\qquad 0<\delta=a+b-20<20 .
 \tag{1}
$$

Let $R_N$ be the original selected signed sum, with all actual squarefree $N$-units, exact moving $D_N,Q_N$ and external minus sign. There is no extra sign or parity selector. Let $\varrho$ be the positive reciprocal density of the fixed-polynomial upper product from the same proof, given by the positive convolution-exponential of $\mathbf1_{[\delta_0,.7]}(t)\,dt/t$ away from zero. Put

$$
 \mathcal C_X=\frac{|\mathcal J|}{\ell}
      \sum_{\substack{S=sW\\\text{true lower masks}}}
         \frac1S\,
         \varrho\!\left(\tfrac12-\frac{\log S}{L}\right)
             \asymp_{\rho,\delta_0} X .
 \tag{2}
$$

Define $K(x)=0$ for $x<0$. For $x\ge0$ set

$$
       K(x)=\sum_{j\ge0}\frac{(-2)^j}{j!}
           \int_{\substack{t_1,\ldots,t_j\ge4\\ t_1+\cdots+t_j\le x}}
                     \frac{dt_1\cdots dt_j}{t_1\cdots t_j},
 \tag{3}
$$

where $j=0$ contributes one, and the sum is finite for every $x$. Let $\pi(du)=du/[u\log(7/5)]$ on $[5/4,7/4]$. The deterministic coefficient for the mean is

$$
 \Psi(\delta)=\int\!\!\int
     \left\{\int_0^u\int_0^v K(\delta-r-t)\,dt\,dr\right\}
                                  \pi(du)\,\pi(dv).
 \tag{4}
$$

**Theorem (unconditional).** For each fixed pair of exponents in (1),

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}} R_N
       =\mathcal C_X^2\Psi(\delta)+o_{\rho,a,b}(X^2),
 \qquad
 \sum_{\substack{N\in\mathcal X\\2\mid N}} |R_N|^2
       \ll_{\rho,a,b}X^3 .
 \tag{5}
$$

Thus whenever $\Psi(\delta)\ne0$, its sign holds with magnitude $\gg X$ for the genuine $R_N$ on a positive density of even targets in each sufficiently large scale window. In particular the positive sign holds for $0<\delta\le4\sqrt{\mathrm e}$, whereas at $\delta=11$ (for instance $a=b=15.5$), the actual $R_N$ is at most $-cX$ on a positive density of even targets. The coefficient has a unique zero on $[4,4+4\sqrt{\mathrm e}]$, bracketed strictly between $4\sqrt{\mathrm e}$ and $51/5$. This is a sign reversal between different floor selections of the same structured carrier, not a pointwise sign prediction or a claim about the unrestricted central sum, Hypothesis S or Goldbach.

## 1. The three saving rows and the actual double row

The exact four-row orbit identity of the [finite short-orbit theorem](r77-source-finite-short-orbit-product-boundary.md) is valid whenever the two primes exceed $D_N$, as they do here. It uses the true complete zero signed sums of the containing families and the exact forbidden product test. The first three rows have total squared mean $O(X^3\ell^{-1/5})$ for the exponents in (1), exactly as checked in §1 of the product-boundary obstruction: independently of the double row, their true label caps are at most $\exp((22+a+b)T)$, their log windows are $O(T)$, the untagged signed band above those caps still has reciprocal mass $\theta\log\ell+O(1)$, and their exact moving seams and prime-floor slivers have the same bounds. None of these three-row estimates uses an upper bound below $20$ on $a+b$; it uses fixed exponents, each below $20$. Thus both their first moment in absolute value and their eventual contribution to the leading coefficient are $o(X^2)$ by Cauchy.

The remaining containing-containing row is genuinely

$$
 H_N=\sum_{\substack{n+m=N\\\text{true carrier and units}}}
            \ \sum_{\substack{z\mid h,\ w\mid k\\FzGw\le Q_N}}
                       \mu(z)\mu(w)\log(h/z)\log(k/w) .
 \tag{6}
$$

The positive outer sign is the result of subtracting forbidden products from two complete zero sums and then applying the original global minus. There is no full cofactor-parity multiplier on either side of (6). For any true term, $zw\le e^{\delta T_N}$ by the actual $F,G$ floors. Choose fixed $A>\max(4,\delta)$, for example $A=21$. Then both short factors are at most $\exp(AT)$, for large $X$, and each divides the old $s$ or some of the $W$ primes at most this bound. No $U$ prime can enter. Each such divisor has bounded arity, with actual pointwise multiplicity $(1+\log\ell)^{O_A(1)}$; its allowed prime factors are all $\ge e^{5T/4}$. The full positive reciprocal label profile is

$$
      \sum_{\substack{S=sW\\\text{true lower gates}}}\frac1S
                    \sum_{\substack{z\mid S\\z\le e^{AT}}}1
                                  \ll_{\rho,A}\ell . 
 \tag{7}
$$

Indeed the upper bound doubles the $1/p$ occupation weight only for $W$ primes in $[e^{4T},e^{AT}]$, whose reciprocal sum is bounded in terms of $A$, and allows two choices for including $s$. This gives the same order as the original reciprocal profile.

The square upper bound $\sum_N |H_N|^2\ll X^3$ follows by the same positive full-window convolution as in the product-boundary obstruction. All its active $h,k$ are above the old fixed $H_-$: each containing label has an opposite long label, so it is $\le Q_N/(D_N+1)<\sqrt N$, giving this lower cofactor bound. Above, the fixed external prime floors give log width $O_{a,b}(T)$. Enumerate all positive labels up to the cap used for the finite short-orbit estimates (or a larger fixed-exponent cap if needed). Their all-label fourth norms are $O(X^{3/4})$ by the full-window positive estimate: the prime comparisons, hard double Perron and reciprocal profiles are the same, and do not rely on $a+b\le20$. The absolute marks of (6) are dominated by products of these marks since $\log(h/z)\ll\log F$. Dropping the product, moving floor and coprimality conditions **only in this positive comparison**, Parseval and Hölder give the square upper. Together with the other rows this proves the second assertion in (5).

## 2. Actual first moment before peeling the low factors

For fixed true $S=sW$ and a short label $z\mid S$, $z\le e^{AT}$, the positive measure of one arm is defined as in §2 of the product-boundary obstruction: give each integer $n=S U F\in\mathcal J$ with prime exponent $\alpha=(\tfrac12 L-\log F)/T$ the actual weight $\log(h/z)$ on the fixed external interval $0\le\alpha\le a$. Both arms have unique integer factorizations already for the fixed external floors; the old true count forces at least one third prime above $2V_X$, precluding two near-square-root factors by product size. For a hard $\alpha$ interval $I$ its mass is

$$
     c_S |I|+
       O\!\left(\frac{X}{S\ell^2}|I|+\frac{X}{S}L^{-B}\right),
 \qquad c_S=\frac{|\mathcal J|}{S\ell}
          \varrho\!\left(\tfrac12-\frac{\log S}{L}\right),
 \tag{8}
$$

for every fixed $B$, uniformly in $z$ and interval endpoints. This is precisely that real density argument with the larger permitted logarithm $\log z\le AT$. Indeed ordinary PNT is applied first to the prime in $\mathcal J/(SU)$ with its hard band. Its real term in the physical coordinate $x$ has mark $\log(SU/z)/\log(x/(SU))$, equal to $1+O_A(1/\ell)$ on the scale of interest and of bounded variation in the rough-product log coordinate. At this fixed polynomial split all upper primes are beyond the actual exceptional band, and the reciprocal upper trace is therefore precisely $\varrho$, independent of the $W$ count once $S$ is chosen. Its argument differs from $\tfrac12-\log S/L$ by $O_{a,b}(1/\ell)$, and $d(\log h/L)=d\alpha/\ell$. The reciprocal PNT errors remain arbitrary inverse log powers because the upper mass is $O_{\delta_0}(1)$ per fixed lower product. This establishes (8) with the actual logarithmic weight, not with an assumed uniform distribution of its sign. The same argument gives the reflected arm with exponent $\beta$.

We may suppress the unit mask at total absolute cost $o(X^2)$ in this first moment: for a fixed $N$ a common prime on the two actual squarefree operands divides $N$, is at least $\exp(5T/4)$, and permits $O(X/p)$ possible first operands. There are $O(\ell)$ such primes; product log weights are $O(L^2)$ and the above pointwise label count is only $(1+\log\ell)^{O(1)}$. Summing the small error over the target window gives the assertion. No other arithmetic condition has been dropped here. All operands are odd, so the resulting independent pair still has an even target in the window.

In these fixed exponent variables the actual floors differ from the endpoints $a,b$ by $O(1/T)$, and the actual curved boundary has

$$
            \alpha+\beta
              =20+\frac{\log z+\log w}{T}+O(1/T).
$$

Neither exponent can be negative on double-row support, since $a,b<20$ fixed. The changes to the fixed endpoints or fixed diagonal are supported on strips of exponent width $O(1/T)$; exact equalities are included in the strips. Use (8) with one exponent fixed for the curved strip, and its whole-arm mass for the other coordinate, then sum the labels by (7). The resulting absolute error is $O(X^2(1/T+\ell L^{-B}))=o(X^2)$, including the prime-floor slivers. The exact condition is thus compared in first moment, not redefined for the individual $H_N$.

For fixed $S,S',z,w$ the interval in $\beta$ cut by the fixed diagonal has bounded-variation length as a function of $\alpha$. Apply (8) and Stieltjes partial summation to the two arms. The area is $\tfrac12(\delta-(\log z+\log w)/T)_+^2$ since this is a triangle at the top corner and $\delta<\min(a,b)$. The uniform error is $O(X^2/(SS'\ell^3)+X^2L^{-B}/(SS'))$, summed against (7) to $o(X^2)$. If a divisor contains a prime greater than $\exp(AT)$ its area is zero. We have consequently obtained the genuine signed first-moment formula

$$
 \sum_N H_N
   = \sum_{S,S'}c_S c_{S'}
          \sum_{\substack{z\mid sW,\ w\mid s'W'}}
                   \mu(z)\mu(w)\,
          f_\delta\!\left(\frac{\log z+\log w}{T}\right)
                   +o(X^2),
       \qquad f_\delta(y)=\tfrac12(\delta-y)_+^2 .
 \tag{9}
$$

Here and below $\sum_N$ is over the even targets in $\mathcal X$. The nonzero short labels in (9) still arise from the true masks and their signs have not been changed. The next factorization concerns the real expression on its right, not the original integer condition.

## 3. Detach the genuinely short $W$ factors in the real trace

Split $W=W_{\rm l} W_{\rm h}$ at $e^{AT}$. Every prime of $W_{\rm l}$ is below the entire exceptional range for large $X$ and none is in an excluded neighborhood. The true exceptional-count gate depends only on $W_{\rm h}$. Because $A>\delta$, the only $W$ factors ever used in a nonzero term of the marked area are divisors of $W_{\rm l}$. We justify the following real-trace replacement, with total error $o(X^2)$ in (9): release the $W_{\rm l}$ product from the total-count and size gates, keep the size and exact typical count gates on $W_{\rm h}$, and replace $\varrho(\tfrac12-\log(sW_{\rm l}W_{\rm h})/L)$ by $\varrho(\tfrac12-\log W_{\rm h}/L)$.

For positive error bounds use the labeled reciprocal law from (7) before the true gates: independent occupancies with probability $(\nu_p/p)/(1+\nu_p/p)$, where $\nu_p=2$ on the low band, one otherwise. The full product is $O(\ell)$, since the low-band reciprocal mass is bounded. The total mean count is at most $\log\ell+O_A(1)$ by Mertens, and the moment of $2^{\omega(W)}$ is $O(\ell)$. Replacing the original total count cap by a temporary $\omega(W_{\rm l})\le3\log\ell$ changes only normalized mass $O(\ell^{1-2\log2})$, by taking the union of either failed upper count and applying the moment bound. This is a positive error bound even with all genuine signs and all the low short-label choices, since $f_\delta$ is uniformly bounded and the labels are paid for by the same positive law. The density is bounded on the true size gate. On the temporary support $\log W_{\rm l}\le \Delta_{\rm l}=3AT\log\ell=o(L)$. Replace the hard size gate of $W$ by the $W_{\rm h}$ size gate; the ambiguity is a log strip of width $\Delta_{\rm l}$ immediately below the old size cutoff. Its normalized weighted positive mass is $O((1+\Delta_{\rm l})/L)$: on that strip $\log W_{\rm h}\gg L$, so mark one factor with weight $\log p$ in $\log W_{\rm h}=\sum_{p\mid W_{\rm h}}\log p$. At fixed other factors the permitted mark has log width $\Delta_{\rm l}$ and its reciprocal logarithmic mass is $O(1+\Delta_{\rm l})$ by Chebyshev over unit log intervals. Sum the remaining factors by their full positive product. This is an upper count, not a congruence or independence assertion about the size-gated set.

On the remaining support the continuum-density argument after deleting $\log(sW_{\rm l})/L$ stays in the positive fixed compact and incurs $O((\Delta_{\rm l}+T)/L)$ by Lipschitz continuity. This also separates the old prime $s$ from that real density. The actual $\log s/T$ remains in the area kernel. Then remove the temporary low count cap at the same positive moment cost. All errors are $o(1)$ times the positive scale of the main expression, which is $O(X^2)$ after normalization by $\ell^2$, as required. The same comparisons with **no label multiplicity** (or dominated by its positive envelope) also apply to the scalar positive coefficient (2).

Let

$$
 \mathcal P_{\rm l}=\prod_{e^{4T}\le p\le e^{AT}}(1+1/p),
 \qquad
 B_X=\frac{|\mathcal J|\mathcal P_{\rm l}}{\ell}
      \sum_{\substack{W_{\rm h}\ \text{on its upper alphabet}\\
                      \text{hard size and true typical count}}}
       \frac1{W_{\rm h}}\,
       \varrho\!\left(\tfrac12-\frac{\log W_{\rm h}}L\right).
 \tag{10}
$$

The two arms now have the very same $B_X$. Its nonnegative profile is $O(X)$ by Mertens; also the unsigned trace replacement just proved gives
$\mathcal C_X=B_X\sum_s1/s+o(X)$. Since $\mathcal C_X\asymp X$ and $\sum_s1/s\to\log(7/5)$, it follows that $B_X\asymp X$. This normalization does not assume a limiting density for the exact original hard size cutoff.

## 4. The signed arithmetic factor and its finite continuum law

On summing the independent reciprocal $W_{\rm l}$ choices, a short divisor $d$ supported in the low band has presence weight
$\mathcal P_{\rm l}\prod_{p\mid d}(p+1)^{-1}$. This is exact: in the positive product, imposing membership of $p$ costs $(1/p)/(1+1/p)$. Hence after extracting $\mathcal P_{\rm l}$ from each arm as in (10), its signed low-divisor convolution measure is

$$
       \nu_X=\mathop{*}_{e^{4T}\le p\le e^{AT}}
                \left(\delta_0^{\rm atom}
                    -\frac{1}{p+1}\,\delta_{\log p/T}^{\rm atom}\right).
 \tag{11}
$$

Here $\delta_y^{\rm atom}$ denotes a unit atom at $y$; it is unrelated to the fixed split exponent $\delta_0$. The old $s$ label contributes a separate two-point factor $\delta_0^{\rm atom}-\delta_u^{\rm atom}$, with $u=\log s/T$. This retains its original $\mu(s)=-1$ sign. The second arm contributes the same $\nu_X$ and its old-prime factor at $v=\log s'/T$. We have already compared true units with the independent pair at negligible total collision cost, before (9); (11) does not make a coprimality assumption about sums over the two arms.

For clarity, put $\lambda_X=\sum_{e^{4T}\le p\le e^{AT}}(p+1)^{-1}\delta_{\log p/T}^{\rm atom}$. Its mass is bounded in terms of $A$. If $\exp_*(\lambda)=\sum_{j\ge0}\lambda^{*j}/j!$, then

$$
           \big\|\nu_X^{*2}-\exp_*(-2\lambda_X)\big\|_{\rm TV}
                  \ll_A\sum_{p\ge e^{4T}}p^{-2}=o(1).
 \tag{12}
$$

Indeed each local factor differs from its exponential by $O((p+1)^{-2})$ in total variation; multiply and telescope using the bounded product of the local total-variation norms. Then convolve twice, with bounded norms again. On the finite normalized log interval $[4,A]$, ordinary reciprocal PNT gives uniform interval convergence of $\lambda_X$ to $\lambda(dt)=\mathbf1_{[4,A]}(t)\,dt/t$, since $(p+1)^{-1}-p^{-1}$ is summably negligible. Only $j\le \lfloor\delta/4\rfloor$ convolution terms can meet $f_\delta$ or its nonnegative translates. On each such product the convergence of integrals of $f_\delta(y)$, $f_\delta(y+u)$, $f_\delta(y+v)$ and $f_\delta(y+u+v)$ is uniform in $u,v\in[5/4,7/4]$, by iterating the uniform interval convergence with bounded-variation marks in each coordinate. Their variation bounds are uniform on this compact range. Thus substituting $\exp_*(-2\lambda)$ in the real area is valid at $o(X^2)$ total error, not as an identity for individual arithmetic sums.

Apply the two old-prime factors to $f_\delta$. The mixed difference of $(x_+)^2/2$ gives the integral of $\mathbf1_{\{r+t<\delta-y\}}$ over $0\le r\le u,0\le t\le v$ when the low coordinates sum to $y$. Interchange these bounded real integrals with the finite signed measure terms just obtained. The cutoff $A>\delta$ does not matter on any active argument; the signed cumulative factor is exactly $K(\delta-r-t)$ in (3). The value at an equality of real coordinates is immaterial for this area calculation; all arithmetic equalities were already counted or charged to the actual strip errors. Write $\Phi_\delta(u,v)=\int_0^u\int_0^v K(\delta-r-t)\,dt\,dr$. The resulting leading expression for $\sum_N H_N$ is

$$
            B_X^2 \sum_{s,s'}\frac1{s s'}\,
                       \Phi_\delta(\log s/T,\log s'/T)+o(X^2).
$$

The function is bounded and Lipschitz in $u,v$ on these intervals since $K$ is bounded on the finite range of arguments. Applying ordinary reciprocal PNT in the two old primes gives the product measure $du/u\,dv/v$ there. Combining with $\mathcal C_X=B_X\log(7/5)+o(X)$, and adding the $o(X^2)$ signed first moment of the other three rows, proves the first assertion of (5).

## 5. The deterministic sign and the genuine density consequence

For $0\le x<4$, $K(x)=1$. For $4\le x<8$,

$$
                         K(x)=1-2\log(x/4).
 \tag{13}
$$

Thus for $0<\delta\le4\sqrt{\mathrm e}$ the integral in (4) is strictly positive: the integrand is nonnegative on its full range and is positive on an open region of $r,t$ with $0<\delta-r-t<4\sqrt{\mathrm e}$. At $\delta=11$ all the arguments $\delta-r-t$ are in $[7.5,11]$. On $[7.5,8]$ formula (13) is at most $1-2\log(15/8)<-1/5$. On $[8,11]$ only the positive double integral adds to (13); because each $t_i\ge4$ it is at most $(x-8)^2/16$. Thus

$$
           K(x)\le 1-2\log(x/4)+(x-8)^2/16,\qquad 8\le x\le11.
$$

The right side is convex and both endpoint values are less than $-1/5$ (for instance use $\log y\ge 2(y-1)/(y+1)$ for $y\ge1$). Hence $\Phi_{11}(u,v)$ and $\Psi(11)$ are strictly negative.

For the transition bracket, differentiating the actual double-simplex integral on $8<x<12$ gives

$$
               K'(x)=\frac{-2+4\log((x-4)/4)}{x}.
$$

Indeed the derivative of the unsigned integral is $\int_4^{x-4}dt/[t(x-t)]=(2/x)\log((x-4)/4)$. Together with (13) this makes $K$ constant on $[0,4]$ and strictly decreasing on $[4,4+4\sqrt{\mathrm e}]$. For $\delta$ in this latter interval all arguments $\delta-r-t$ are positive, as $r+t\le7/2$. Moreover any increase in $\delta$ makes the integrand strictly smaller on a positive-area subset near $r=t=0$ crossing or above $4$. Therefore $\Psi$ is continuous and strictly decreasing there. It is positive at $4\sqrt{\mathrm e}$, and negative at $51/5$, since its arguments then lie above $67/10>4\sqrt{\mathrm e}$ and at most $51/5<4+4\sqrt{\mathrm e}$. This proves the stated unique zero in the bracket without claiming uniqueness outside the interval.

Finally if $\Psi(\delta)\ne0$, (2) and (5) give an actual signed first moment of magnitude $\gg X^2$ and square upper bound $O(X^3)$. In its sign, targets with magnitude below a sufficiently small $cX$ cannot supply more than half the first-moment lower bound. Cauchy applied to the remaining targets forces $\gg X$ of them. This proves the positive-density conclusion for the original true sum, not just the sign of an Euler comparator. No claim is made about the full arithmetic problem outside the indicated masks.
