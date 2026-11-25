# Complete the aligned two-pole correction into two signed colored caps

**Scope.** For the genuine exceptional correction of the mixed strip, assume the actual Page conductor divides the target, and that its distance below the **original** auxiliary conductor cap satisfies a stated finite-denominator bound. Under these conditions the [aligned two-pole formula](r92-spectral-aligned-exceptional-two-pole-formula.md) can be written with two explicit signed autocorrelation expressions. The total colored autocorrelation has exactly the genuine binary singular-series mass, not a probability-model normalization. Neither that identity nor the formula bounds the mass inside the moving finite caps. There is no amplitude-smallness result, no use of Dirichlet GRH or an external zero-gap result, and no assertion about unaligned targets, an uncorrected prescribed planting, prime pairs, or Hypothesis S.

Keep exactly the parameters and actual tests of the aligned formula: $Y\le N\le2Y$ even, $G=\log Y$, $L=\log N$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$ for fixed admissible $B>B_0>0$. The left interval $I\subset(N/2,9N/16]$ is real and half-open, and $\omega$ has uniformly bounded supremum and pointwise variation. The Page character $\chi$ is primitive real of conductor $r\le Q_0$, with the simple real zero $\beta>1-4a_0/\sqrt G$. We assume throughout the nonzero-correction case that $r\mid N$. Let $S=Y^{1/10}$, the literal unsigned cutoff in the aligned formula, $U=\log(H_0/D)=(B-B_0)\log L$, and $T_x=\log(x/D^2)$. The integral variable is always the physical $x$ with $N-x\in I$.

For $p\nmid r$ set $c_p=\chi(p)p^{-\beta}$, $E_p=(1-c_p)^{-1}$, and for $p\nmid N$ set $d_p=(p-2)/(p-1)-2c_p$. The short reciprocal coefficients are multiplicative on squarefree integers, with

$$
 \alpha_p=
 \begin{cases}
 0,&p\mid N,\\
 c_p/d_p,&p\nmid N,
 \end{cases}
 \qquad
 P_{\chi,N}=\prod_{p\nmid r}\frac{pE_p^2}{p-1}
                   \begin{cases}1,&p\mid N,\\d_p,&p\nmid N.\end{cases}
 \tag{1}
$$

Here $p\nmid N$ implies $p\ge3$ and $p\nmid r$. For all sufficiently large $Y$, $\beta\ge.99$; then $d_3$ is bounded away from zero for either possible value of $\chi(3)$, and $d_p$ is positive and bounded away from zero for $p\ge5$. This permits the indicated factorization after completion, not any division by uncompleted local factors. The ordinary-factor part of $P_{\chi,N}$ converges absolutely. It is not assumed positive.

For squarefree $j$ let $R_j(v)=\sum_{n\le e^v,(n,j)=1}\alpha(n)$ for $v\ge0$, extended by zero for $v<0$; the function $\alpha(n)$ vanishes off squarefree integers and $\alpha(1)=1$. Define

$$
 \begin{split}
 \mathcal N_\chi&=\frac{rP_{\chi,N}}{\varphi(r)L'(\beta,\chi)^2},\\
 C_\chi(t)&=\mathcal N_\chi\sum_{j\ {\rm sf}}\mu(j)\alpha(j)^2
                         \int_{\mathbb R}R_j(v)R_j(v+t)\,dv,\\
 Q_\chi(U)&=\mathcal N_\chi\sum_{\substack{j\ {\rm sf}\\j\le e^U}}
            \mu(j)\alpha(j)^2 \int_0^{U-\log j}R_j(v)^2\,dv,\\
 J_\chi(U)&=\mathcal N_\chi\sum_{\substack{j\ {\rm sf}\\j\le e^U}}
            \mu(j)\alpha(j)^2
                           \left(\int_0^{U-\log j}R_j(v)\,dv\right)^2 .
 \end{split}
 \tag{2}
$$

All profiles are signed, all products bilinear. Write

$$
 \begin{split}
 B_0(x)&=\int_{-T_x}^{T_x}C_\chi(t)\,dt-T_x C_\chi(T_x),\\
 B_1(x)&=T_x\{C_\chi(0)-Q_\chi(U)\}+J_\chi(U),\\
 \mathcal V_i&=-\chi(-1)\int_{N-x\in I}
  \frac{\omega(N-x)(N-x)^{\beta-1}x^{\beta-1}}{\log x}\,B_i(x)\,dx .
 \end{split}
 \tag{3}
$$

The subscript in $B_i(x)$ is a color index, unrelated to the fixed cutoff exponent $B_0$ in $H_0$.

**Theorem.** There is a fixed $C$ such that the two genuine exceptional corrections satisfy, uniformly in the true $N,I,\omega$ and for each fixed $A>0$,

$$
 \mathfrak E_\pm=\tfrac12(\mathcal V_0\pm\mathcal V_1)
   +O_A\!\left(Y^\beta
     \left[G^{-A}+G^C
       \exp\left(-\frac{\log\log G}{\log G}\log(Q_0/r)\right)\right]\right).
 \tag{4}
$$

In particular the total error is $O_A(Y^\beta G^{-A})$ when
$\log(Q_0/r)\ge (C+A)(\log G)^2/\log\log G$.
This uses the original $Q_0$, with no enlargement of any common arc set. The exact normalization is

$$
                    \int_{\mathbb R}C_\chi(t)\,dt=\Sigma(N),
 \tag{5}
$$

where $\Sigma(N)$ is the genuine binary singular factor of the [whole mixed-strip theorem](r80-spectral-whole-mixed-parity-density.md). Identity (5) holds for the defined complete profile irrespective of the approximation error in (4). The sign $+$ in (4) has the same even squarefree total prime-factor count meaning as in the aligned formula. If the zero does not exist the original correction is zero, and no colored profile is needed.

## 1. The moving moment for the original finite Ramanujan range

Use the four local factors of $\mathcal L(h;q,N)$ from (1) of the aligned formula. Write $\mathcal L(h;q,N)=\prod_{p\nmid r}l_{p,\mathbf1_{p\mid q}}$ for each squarefree short product $h=uv$ with $(h,r)=1$, so $l_{p,0}$ is its local factor for $p\nmid q$ and $l_{p,1}$ that for $p\mid q$. In the exact $t$ sum of that formula, the effect of an occupied prime $p\mid t$ after summing both choices of $q\mid t$, including the $\mu(t)/\varphi(t)$ factor, is

$$
 b_p=\frac{l_{p,0}-p\,l_{p,1}}{p-1}.
 \tag{6}
$$

No division by $l_{p,0}$ is used. Indeed the two local choices in $\sum_{q\mid t}q\mu(t/q)$ give $-l_{p,0}$ and $p l_{p,1}$, multiplied by $-1/(p-1)$. The coefficient $A_h(t)$ of the resulting $t$ sum is the product of $l_{p,0}$ at its unoccupied primes and $b_p$ at the occupied ones.

For large $G$ use the moving exponent $\vartheta=(\log\log G)/\log G\le1/4$. By absolute sums over squarefree $t$ coprime to $r$ the corresponding moment is at most $\prod_{p\nmid r}(|l_{p,0}|+p^\vartheta|b_p|)$. This can be shown by finite Euler expansions followed by passage to the limit; no nonvanishing of a small-prime unoccupied factor is required. The local upper bounds, uniformly for $\beta\ge.99$ in its stated strip, are

$$
 \begin{array}{c|c}
 \text{case}& |l_{p,0}|+p^\vartheta|b_p|\ \text{is at most}\\ \hline
 p\nmid h,\ p\nmid N &1+C_1(p^{-2\beta}+p^{\vartheta-1-\beta})\\
 p\nmid h,\ p\mid N  &1+C_1(p^{-2\beta}+p^{\vartheta-\beta})\\
 p\mid h,\ p\nmid N  &1+C_1(p^{-\beta}+p^{\vartheta-1})\\
 p\mid h,\ p\mid N   &1+C_1p^\vartheta .
 \end{array}
 \tag{7}
$$

For example, in the first two cases $l_{p,0}=1-p^{-2\beta}E_p^2$. In the first case $b_p=E_p^2(-2c_p-1/(p-1))/(p-1)$; in the second case $b_p=E_p^2(2c_p+1/(p-1))$. In the last two cases $l_{p,0}=E_p^2$ and $b_p=E_p^2/(p-1)$ or $-E_p^2$, respectively. These identities give (7) for $p\ge2$ with uniform constants.

Bound the whole product first by the **positive generic envelope** given by the first two rows of (7), evaluated at all primes; then insert the extra factors $1+w_p$ on the occupied $h$ primes given by the last two rows. This is an upper bound because every generic factor is at least one. The generic envelope is bounded by
$\exp(O(1+\sum_{p\mid N}p^{\vartheta-\beta}))$.
To sum over actual short products, use $h^{-\beta}=(uv)^{-\beta}$, drop the coprime and squarefree restrictions only for the positive upper bound, and enlarge $\prod_{p\mid h}(1+w_p)$ to $\prod_{p\mid u}(1+w_p)\prod_{p\mid v}(1+w_p)$. The divisor expansion of either factor and $\sum_{d\mid u,u\le S}u^{-\beta}\le d^{-\beta}\sum_{u\le S}u^{-\beta}$ give a cost at most

$$
 \left(\sum_{u\le S}u^{-\beta}\right)^2
                  \prod_p(1+w_p p^{-\beta})^2
   \ll G^2Y^{(1-\beta)/5}
          \exp\left(O\left(1+\sum_{p\mid N}p^{\vartheta-\beta}\right)\right).
 \tag{8}
$$

In (8) the increments from $p\nmid N$ are summable uniformly in $\vartheta,\beta$, and the increments from $p\mid N$ have the asserted bound by (7).

There is the following elementary uniform bound, sufficient for a much smaller denominator margin than a fixed positive-power moment. For $p\le\sqrt G$ one has $p^{\vartheta+1-\beta}\ll(\log G)^{1/2}$ since $1-\beta=O(G^{-1/2})$, and $\sum_{p\le\sqrt G}1/p\ll\log\log G$. For $\sqrt G<p\le G$, the reciprocal mass is $O(1)$ by Chebyshev's prime bound and partial summation, and the additional factor is $\ll\log G$. There are $O(G/\log G)$ prime divisors of $N$ exceeding $G$, and each contributes at most $G^{\vartheta-\beta}\ll(\log G)/G$. Together these prove $\sum_{p\mid N}p^{\vartheta-\beta}\ll\log G$, so (8) and the generic envelope cost only $G^{O(1)}Y^{(1-\beta)/5}$.

The missed tail of $t>Q_0/r$ in the aligned formula now inserts $(Q_0/r)^{-\vartheta}$ by this absolute moment. Each real integral there has modulus $O(Y^{2\beta-1}G^{O(1)})$ uniformly in the actual short labels, and $|1/L'(\beta,\chi)|\ll1$ by the near-exception estimate checked in the aligned formula. Also $r/\varphi(r)\ll G^{O(1)}$ and $2\beta-1+(1-\beta)/5\le\beta$. The total completed-tail error is thus bounded by the second term of (4). This proof controls the actual signed $t$ sum by combining its two local $q$ options first. Taking absolute values of the original $q$ sum separately would not supply (7).

After completion the exact local factor is $l_{p,0}+b_p=p(l_{p,0}-l_{p,1})/(p-1)$. At $p\mid h$ it is $pE_p^2\mathbf1_{p\nmid N}/(p-1)$, restoring the true short unit restriction $(h,N)=1$ **in the completed expression**, not changing a finite Ramanujan coefficient by fiat. At $p\nmid h,p\mid N$ it is $pE_p^2/(p-1)$. At $p\nmid h,p\nmid N$ it is $pE_p^2d_p/(p-1)$. Multiplying by the short $\chi(h)h^{-\beta}$ gives exactly $P_{\chi,N}\alpha(u)\alpha(v)$ when $(u,v)=1$ and the same expression is zero if $(h,N)>1$. The factors of $P_{\chi,N}$ at $p\nmid N$ are $1+O(p^{-2}+p^{-1-\beta}+p^{-2\beta})$, by expansion; the finitely many exceptional small primes and $p\mid N$ are kept exactly. The latter factors give $|P_{\chi,N}|ll G^{O(1)}$ since $\sum_{p\mid N}p^{-\beta}\ll\log G$ by the preceding bound. This proves (1) and the absolute convergence used here.

## 2. The colored primitive, its actual tails, and its mass

Let $R_*(v)=\sum_{n\le e^v}\chi(n)n^{-\beta}$ on $v\ge0$, zero on $v<0$. Periodicity of the nonprincipal primitive $\chi$ gives $\sum_{n\le X}\chi(n)=O(r)$. It follows by Abel summation that its Dirichlet series agrees with $L(s,\chi)$ for real part positive and that the full value at $\beta$ is zero. In particular

$$
           |R_*(v)|\ll r e^{-\beta v}\quad(v\ge0),\qquad
           \int_0^\infty R_*(v)\,dv=L'(\beta,\chi).
 \tag{9}
$$

For the first bound take the tail beyond $e^v$ and use the zero total value. For the second, the Laplace transform of the primitive is $L(\beta+s,\chi)/s$, first for sufficiently large real $s>0$ by direct Fubini, and then for every $s>0$ by analytic continuation or summation by parts. Passing to $s\downarrow0$ using the first bound gives the displayed **positive derivative sign**.

Incorporate the exact short weights and common-divisor mask by the signed Euler convolution $\kappa_j$ whose Laplace transform is

$$
 H_j(s)=
  \prod_{p\nmid r}(1+\alpha_p\mathbf1_{p\nmid j}p^{-s})(1-c_p p^{-s}).
 \tag{10}
$$

For example each factor is a sum of signed atoms at log positions $0,\log p,2\log p$. Outside the primes of $Nj$ its nonconstant coefficients have magnitude $O(p^{-1-\beta}+p^{-2\beta})$, since $\alpha_p-c_p=O(p^{-1-\beta}+p^{-2\beta})$ for large $p$. At the primes of $Nj$ it is $1-c_p p^{-s}$. The finitely many small-prime factors have bounded total variation. With any sufficiently small fixed $\delta>0$, for example $\delta=1/8$, this gives an exponential absolute moment

$$
 M_j(\delta):=\int e^{\delta v}\,d|\kappa_j|(v)
       \ll \exp\left(C_2\sum_{p\mid Nj}p^{-\beta+\delta}\right).
 \tag{11}
$$

The product of these finite signed measures exists in the indicated norm by absolute convergence of the large-prime deviations. Multiplying Euler coefficients by $(1-c_p p^{-s})^{-1}$, or comparing each finite prefix, shows $R_j=R_* *\kappa_j$ exactly. In particular
$\int R_j=L'(\beta,\chi)H_j(0)$, with the masks and sign convention of (9).

These facts justify all infinite operations in (2) and will allow removal of the artificial polynomial short cutoff. Indeed $M_j(\delta)\ll\exp(O(G^\delta))\prod_{p\mid j}(1+C_3p^{-\beta+\delta})$ by splitting primes dividing $N$ at $G$ and using $\beta=1+O(G^{-1/2})$. The bound here only uses the integer sum at $p\le G$ and the log product bound for $p>G$. We have $\|R_j\|_1+\|R_j\|_2\ll r M_j(\delta)$. From the same convolution, split its shifts at half the argument; for $v\ge0$ this gives $|R_j(v)|\ll r M_j(\delta)e^{-c v}$ with fixed $c>0$, using (9) and (11). Consequently its $L^1,L^2$ tails beyond $V$ have the same bound with $e^{-c' V}$. Moreover

$$
 \sum_{j\ {\rm sf}}j^{1/4}|\alpha(j)|^2 M_j(\delta)^2
                                      \ll \exp(O(G^\delta)),
 \tag{12}
$$

since after the $N$ factor the remaining Euler product has increments $O(p^{-2\beta+1/4})$ at large primes, and the bounded small-prime factors are finite. Thus the defining sum of $C_\chi$ is absolutely convergent in $L^1(dt)$ and uniformly in the point value by Young and Cauchy--Schwarz. Its terms are continuous (by $L^2$ translation continuity) and even. There is no assumption that the combined function is nonnegative.

For the exact normalization integrate each term in (2) and use (9)--(10). Summing over $j$ gives the Euler factor $(1-c_p)^2((1+\alpha_p)^2-\alpha_p^2)=(1-c_p)^2(1+2\alpha_p)$ at $p\nmid r$: the two options for $p\mid j$ give the subtraction, and there is no need to divide by $1+\alpha_p$. The resulting product, with the one from (1), is

$$
 \int_{\mathbb R} C_\chi(t)\,dt
    =\frac r{\varphi(r)}\prod_{p\nmid r}\frac p{p-1}
                  \begin{cases}
                   1,&p\mid N,\\
                   d_p(1+2\alpha_p),&p\nmid N.
                  \end{cases}
    =\Sigma(N).
 \tag{13}
$$

Indeed $d_p(1+2\alpha_p)=(p-2)/(p-1)$ for $p\nmid N$, and because $r\mid N$ the missing primes of $r$ from the usual $\Sigma(N)$ are supplied exactly by $r/\varphi(r)$. Absolute justification for the Euler-factor computation follows from (12) for the sum and from the summable large-prime differences in (10); alternatively perform the computation first at finite prime sets. This identity does not remove the signed cutoff or distinguish the finite-cap value from the total mass.

## 3. Convert both actual geometric kernels, keeping the finite cutoff

Expand $(u,v)=1$ in the completed model as $\sum_{j\mid(u,v)}\mu(j)$ and write $u=ja$, $v=jb$. Squarefreeness leaves outer $\mu(j)\alpha(j)^2$, and the two remaining signed arrays are masked exactly by $j$. The reciprocal primitive at the literal upper bound is $R_j(V_j)$, where $V_j=\log(S/j)$. The ratio logarithm is unchanged. For $j\le S^{1/2}$, $V_j\ge G/20$ and the just-proved estimates bound the endpoint and beyond-endpoint norms by $Y^{-c_4}$ for some fixed $c_4>0$, uniformly in this range (here $r\le e^{16Z}=Y^{o(1)}$ and $M_j(\delta)\le \exp(O(G^\delta))$ because $Nj\le O(Y^{1.1})$). The total absolute mass of either finite short array is $Y^{o(1)}$: use the Euler convolution of the coefficients, its absolute variation, and $\sum_{n\le S}n^{-\beta}\ll G Y^{(1-\beta)/10}$. Thus for each such bounded array one may subtract its total mass at the endpoint $V_j$ with a power-small weighted error for any of the displayed geometric kernels, whose suprema are bounded by a fixed power of $G$. The new zero-total array has primitive $R_j(v)\mathbf1_{[0,V_j)}(v)$ almost everywhere. Replacing this clipped primitive by the whole $R_j$ after integration by parts has the same type of power-small error using the tail and global norms. At $j>S^{1/2}$ the finite arrays and the completed autocorrelations both cost a fixed power saving by (12) and the same finite absolute mass bound. All such errors, multiplied by the actual real integrated prefactor and the $Y^{o(1)}$ normalizations of (1)--(2), have arbitrary log saving with scale $Y^\beta$.

For color zero, set $g_T(s)=|s|\min(T,|s|)$. The geometric mark from the aligned formula is $-g_{T_x}(\log(u/v))/(2\log x)$. The same signed integration by parts as for the [uncolored cap](r67-spectral-high-mixed-parity-major.md) gives the quadratic signed array of this kernel as minus the primitive pairing against its second derivative. Explicitly for a compact zero-total array with primitive $F$, it is
$-\iint F(v)F(w)g_T''(v-w)\,dv\,dw$.
Here $g_T''=2\mathbf1_{|s|<T}-T(\delta_T+\delta_{-T})$ as a distribution, and the point evaluations are legitimate by continuity of the autocorrelation; smoothing the kernel gives the same identity. After multiplying by $-1/2$, summing the $j$ and inserting $\mathcal N_\chi$, this is exactly $B_0(x)$ of (3). This keeps the moving positive cap $T_x$ and both Dirac endpoints.

For color one put $A_x=T_x/2$ and $k=(U-\log\max(u,v))_+$. Since $A_x-U>0$ for large $Y$ (the fixed $B_0$ is positive), the width $W_x$ of the aligned formula equals $A_x-k$. If $\rho=|\log(u/v)|$, its numerator is

$$
       W_x^2-W_x\rho=A_x^2-A_x\rho-2A_x k+(k^2+k\rho).
 \tag{14}
$$

The full signed coefficient array has total zero; the constant term uses $R_j(V_j)^2$ in the finite sums, making its contribution power-small as above. This is not a zero integral of the primitive. For the second term use $|s|''=2\delta_0$ in the same signed integration by parts, giving $2A_x C_\chi(0)=T_x C_\chi(0)$ after normalization. For the remaining terms one must **not** extend the low cutoff to infinity. On the original finite sums one has

$$
 \begin{split}
 k&=\int_0^U\mathbf1_{\log u\le t}\mathbf1_{\log v\le t}\,dt,\\
 k^2+k\rho&=(U-\log u)_+(U-\log v)_+ .
 \end{split}
 \tag{15}
$$

The second identity holds by taking the larger of the two logarithms; if it exceeds $U$ both sides vanish. After $u=ja$, $v=jb$, the finite integrals in (15) have exact upper endpoint $(U-\log j)_+$, and they probe only labels $u,v\le e^U<S$ for large $Y$. Finite signed Fubini gives precisely the square primitive and squared integrated-primitive terms of (2), with respectively $-2A_x$ and $+1$. Thus (14) yields $B_1(x)$, retaining the actual hard low cut, with no limit through $U$ or the endpoints.

Finally multiply each normalized cap by the unchanged physical factor and the outer $-\chi(-1)$ of the actual hard correction. The signs precede the genuine parity half-sum. This gives (3)--(4), combining the aligned arithmetic error, the denominator completion, and the power-small artificial-cut errors. The total signed mass in (5) supplies no bound for $B_0(x)$ or $B_1(x)$: the former retains endpoint and truncated autocorrelation, while the latter retains two independent finite moments.
