# Exact Euler collapse of the aligned complete-planting exceptional mean

**Scope.** This evaluates the genuine **signed dyadic mean** of the exceptional mixed-strip correction on an entire divisibility family when its actual Page conductor divides the planting integer. The finite Ramanujan sum of the signed-mean formula then completes exactly, with no denominator-gap hypothesis. The resulting two colored finite caps have total autocorrelation mass $K/\varphi(K)$. On a hypothetical sufficiently close aligned Page-zero dyad for a complete primorial with a specified low cutoff, the actual **parity difference** of the two signed means has a fixed sign and a quantitative lower bound. This implication does not assert existence of such dyads or of any exceptional zero. There is no use of Dirichlet GRH or an external zero-gap input. No pointwise result for aligned targets, full-coefficient positivity, prime-pair count, or Hypothesis S is claimed.

Keep exactly the setting of [the complete-planting signed mean](r95-spectral-complete-planting-signed-mean.md). Thus $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $Y\le N\le2Y$ even, and a possible primitive real Page character $\chi$ of conductor $r\le Q_0$ has its actual simple zero $\beta>1-4a_0/\sqrt G$. Assume that the zero exists and that $r\mid K$ for the **fixed on the dyad** even integer $K\le e^{2Z}$. When it does not exist the earlier correction is zero. Use the genuine common scaled left interval $I_N=NJ$, fixed $J\subset(1/2,9/16]$ real and half-open, the common bounded-BV weights $\omega_N(u)=w(u/N)$ and $\eta(N/Y)$, and the normalized signed mean

$$
       \langle F\rangle_K=\frac K Y
               \sum_{\substack{Y\le N\le2Y\\K\mid N}}\eta(N/Y)F(N).
 \tag{1}
$$

The actual $\mathfrak E_\pm$ is the correction of the original R87 auxiliary decomposition, not a new correction after widening its cap. Use the same even/odd squarefree factor-count colors and the same fixed admissible $B>B_0>0$. At real $v\in[Y,2Y]$ put $D_v=\sqrt v(\log v)^{-B}$, $H_{0,v}=\sqrt v(\log v)^{-B_0}$, $U_v=\log(H_{0,v}/D_v)$ and $T_{v,x}=\log(x/D_v^2)$ for $v-x\in vJ$.

For $p\nmid r$ put $c_p=\chi(p)p^{-\beta}$ and $E_p=(1-c_p)^{-1}$. Define the averaged short coefficients, multiplicative on squarefree integers and zero otherwise, and their prefactor by

$$
  \alpha_p^K=
   \begin{cases}
     0,&p\mid K,\\
     c_p/(1-2c_p),&p\nmid K,
   \end{cases}
  \qquad
  P_K=
     \prod_{\substack{p\mid K\\p\nmid r}}\frac {p E_p^2}{p-1}
          \prod_{p\nmid K}E_p^2(1-2c_p),
  \qquad
  M_K=\frac{rP_K}{\varphi(r)L'(\beta,\chi)^2}.
 \tag{2}
$$

Here $\alpha^K(1)=1$ and $r\mid K$, so all primes outside $K$ are outside $r$ and odd. All denominators are bounded away from zero uniformly for $\beta\ge.99$; the infinite product in $P_K$ converges absolutely and is positive. For squarefree $j$ use the signed primitive $R_j(u)=\sum_{n\le e^u,\,(n,j)=1}\alpha^K(n)$ for $u\ge0$, zero below zero. With bilinear products define

$$
 \begin{split}
 C_K(t)&=M_K\sum_{j\ {\rm sf}}\mu(j)\alpha^K(j)^2
                                      \int_{\mathbb R}R_j(u)R_j(u+t)\,du,\\
 Q_K(U)&=M_K\sum_{\substack{j\le e^U\\j\ {\rm sf}}}
                \mu(j)\alpha^K(j)^2\int_0^{U-\log j}R_j(u)^2du,\\
 J_K(U)&=M_K\sum_{\substack{j\le e^U\\j\ {\rm sf}}}
                \mu(j)\alpha^K(j)^2\left(\int_0^{U-\log j}R_j(u)du\right)^2.
 \end{split}                                                     \tag{3}
$$

For the two colored kernels put

$$
 \begin{split}
 \mathcal A_0(v,x)&=\int_{-T_{v,x}}^{T_{v,x}}C_K(t)\,dt
                                    -T_{v,x}C_K(T_{v,x}),\\
 \mathcal A_1(v,x)&=T_{v,x}\{C_K(0)-Q_K(U_v)\}+J_K(U_v).
 \end{split}                                                     \tag{4}
$$

The color index on $\mathcal A_0,\mathcal A_1$ is distinct from the parity index and from the fixed cutoff constants.

**Theorem 1.** In the stated aligned case, for each fixed $A>0$ the genuine means are

$$
 \begin{split}
 \langle\mathfrak E_\pm\rangle_K
 ={}&-\frac{\chi(-1)}{2Y}
       \int_Y^{2Y}\eta(v/Y)
           \int_{v-x\in vJ}
               \frac{w((v-x)/v)(v-x)^{\beta-1}x^{\beta-1}}{\log x}
                 \{\mathcal A_0(v,x)\pm\mathcal A_1(v,x)\}\,dx\,dv\\
    &+O_A(Y^\beta G^{-A}).
 \end{split}                                                     \tag{5}
$$

All the moving hard cuts on the underlying true arithmetic are retained through the displayed real integrals. The exact signed normalization is

$$
                         \int_{\mathbb R}C_K(t)\,dt=\frac K{\varphi(K)} .
 \tag{6}
$$

The profile here is an averaged aligned one; in general its local coefficients (2) differ from the [pointwise aligned colored caps](r93-spectral-completed-colored-caps.md). Identity (6) alone is not an estimate on either finite cap.

**Theorem 2.** In addition assume $K=K_z=\prod_{p\le z}p$ is the **full primorial** with $G^\epsilon\le z\le Z$ for fixed $0<\epsilon<1/2$, put $\ell=\log z$, and suppose $U_v\le\ell$ throughout the dyad. Require $(1-\beta)G\le C_*\log G$ for a fixed $C_*>0$. For a fixed $J$ and fixed nonnegative $w,\eta$ with positive integrals $\int_J w$ and $\int_1^2\eta$, independent of the dyad, one has for all sufficiently large such dyads

$$
 -\chi(-1)\langle\mathfrak E_+-\mathfrak E_-\rangle_{K_z}
 \ \gg\
      \left(\int_J w\right)\left(\int_1^2\eta\right)
      \frac{Y^{2\beta-1}}{G}\frac{K_z}{\varphi(K_z)}\,
                         \frac{1}{(\log r)^4}  .
 \tag{7}
$$

In particular the mean parity difference has sign $-\chi(-1)$ and it is not an arbitrary inverse-logarithmic error under these conditions. For instance, the condition $U_v\le\ell$ allows any fixed positive gap $B-B_0<\epsilon$. The lower bound is for the **exceptional correction** rather than for a difference of the two whole mixed-strip means after replacing their base by an approximate Dickman profile.

## 1. The finite denominator sum collapses before taking a limit

Apply Theorem 1 of the complete-planting signed mean in the case $r\mid K$. Its true error is $O(Y^\beta G^C r^{-1/2})$, hence $O_A(Y^\beta G^{-A})$ for every fixed $A$ by the classical conductor lower bound for this Page threshold. Its retained term is the average of the finite algebraic two-pole model, with the local replacements (2) of that theorem. We write $\overline l_{p,1}$ for its averaged local factor at a prime $p\mid q$, and $l_{p,0}$ for the unchanged factor at $p\nmid q$, depending on whether $p$ is in the short product $h=u_1u_2$. All these primes are outside $r$. Thus $l_{p,0}=E_p^2$ if $p\mid h$, and $l_{p,0}=1-p^{-2\beta}E_p^2=E_p^2(1-2c_p)$ otherwise. The letter $q$ here is the genuine divisor of the finite Ramanujan label $t$, as in the [two-pole formula](r92-spectral-aligned-exceptional-two-pole-formula.md).

At each prime $p\mid t$, contracting the two alternatives of $q\mid t$ with the $\mu(t)/\varphi(t)$ factor gives occupied weight $(l_{p,0}-p\overline l_{p,1})/(p-1)$; the other primes retain $l_{p,0}$. This identity multiplies local factors and involves no division by an unoccupied one. At $p\nmid K$, the averaged divisibility factor of the signed-mean formula is $1/p$. If $p\mid h$, this gives $\overline l_{p,1}=E_p^2/p$; if $p\nmid h$, it gives
$E_p^2((1-1/p)/(p-1)-2c_p/p)=E_p^2(1-2c_p)/p$.
Thus in both cases **every occupied weight at $p\nmid K$ is zero exactly**.

All possibly surviving $t$ are consequently squarefree divisors supported on $p\mid K,\ p\nmid r$. For any such $t$ one has $rt\mid K$, as $r\mid K$ and $(r,t)=1$. Hence $t\le Q_0/r$ already, using $K\le e^{2Z}\le Q_0$. No estimate beyond the original finite denominator range is used. Summing the two choices of $t$ occupancy at each $p\mid K$ outside $r$ gives $p(l_{p,0}-\overline l_{p,1})/(p-1)$. Here the averaged divisibility factor is one, so at $p\mid h$ the result is zero, and at $p\nmid h$ it is $pE_p^2/(p-1)$. The resulting short product must be coprime to $K$ in the **completed model**. At $p\nmid K$ the unoccupied-$h$ factor is $E_p^2(1-2c_p)$ and the occupied-$h$ factor is $E_p^2$. With the signed $\chi(h)h^{-\beta}$ weights from the two-pole model, the finished short arithmetic is therefore $P_K\alpha^K(u_1)\alpha^K(u_2)$ on mutually coprime squarefree short labels, with their original bound $S=Y^{1/10}$.

At $p\nmid K$ the factors are $1+O(p^{-2\beta})$, uniformly for the actual strip, and at $p\mid K$ the remaining factors have $\log$ absolute value $O(p^{-\beta}+p^{-1})$, since $p^{-\beta}<1$ and $\beta\ge.99$. Thus $P_K\ll G^{O(1)}$ by $K\le e^{2Z}$ or the elementary splitting at $G$. The corrections with $p\mid K$ are finite. This proves (2) as an exact replacement of the finite averaged model; there is no prime-divisibility independent-random-variable assumption in this step.

## 2. Colored Euler primitive, convergence and exact mass

For clarity we give the analytic checks for the **new** $\alpha^K$, before transferring the cap calculation. Let
$R_*(u)=\sum_{n\le e^u}\chi(n)n^{-\beta}$ for $u\ge0$, zero below zero. The mean-zero period of $\chi$ gives $|\sum_{n\le X}\chi(n)|\ll r$. Since its Dirichlet series at $\beta>0$ converges to $L(\beta,\chi)=0$, partial summation gives $|R_*(u)|\ll r e^{-\beta u}$. Its Laplace transform at positive argument $s$ is $L(\beta+s,\chi)/s$, first by absolute summation at large $s$, then by continuation. Taking $s\downarrow0$ using the tail gives

$$
                   \int_0^\infty R_*(u)\,du=L'(\beta,\chi).
 \tag{8}
$$

For squarefree $j$ define a signed measure on nonnegative log positions by the following Euler Laplace transform:

$$
 H_j(s)=\prod_{p\nmid r}
              (1+\alpha_p^K\mathbf1_{p\nmid j}p^{-s})
                                      (1-c_p p^{-s}).
 \tag{9}
$$

Each factor has at most the three locations $0,\log p,2\log p$. Outside $Kj$, the nonconstant coefficients have magnitude $O(p^{-2\beta})$ at large primes, as $\alpha_p^K-c_p=2c_p^2/(1-2c_p)$; at primes of $Kj$ the factor is $1-c_p p^{-s}$. Thus for $\delta=1/8$ the convolution product exists in total variation with exponential absolute moment at most
$\exp(O(1+\sum_{p\mid Kj}p^{-\beta+\delta}))$.
The small primes are bounded uniformly and are retained exactly. This also follows by multiplying absolute local moments and using absolute convergence of the large-prime deviations. Comparing Euler coefficients proves that $R_j=R_*\ast H_j^\vee$, where $H_j^\vee$ denotes this log-position measure, not an inverse of a signed function. Consequently $\int R_j=L'(\beta,\chi)H_j(0)$.

In more detail let $M_j(\delta)=\int e^{\delta u}\,d|H_j^\vee|(u)$. The $K$ portion of the last bound is $\exp(O(G^\delta))$ by splitting its prime factors at $G$ and using $1-\beta=O(G^{-1/2})$. The remaining factor is bounded by $\prod_{p\mid j}(1+C p^{-\beta+\delta})$. Hence

$$
       \sum_{j\ {\rm sf}}j^{1/4}|\alpha^K(j)|^2 M_j(\delta)^2
                                      \ll\exp(O(G^\delta)).
 \tag{10}
$$

Indeed the remaining product in $j$ has increments $O(p^{-2\beta+1/4})$ at large primes. Both $\|R_j\|_1$ and $\|R_j\|_2$ are $O(r M_j(\delta))$. Splitting shifts at half the argument in $R_*\ast H_j^\vee$ also gives $|R_j(u)|\ll r M_j(\delta)e^{-c u}$ for some fixed $c>0$, with the corresponding $L^1,L^2$ tails. These controls justify absolutely the series in (3), both in $L^1$ of the autocorrelation variable and uniformly in its pointwise values. Continuity of each autocorrelation uses continuity of $L^2$ translations. No positive-definiteness of the signed combined function is assumed.

For its total mass, integrate each term of (3). By (8)--(10) and signed Fubini this replaces the paired integral by $L'(\beta,\chi)^2 H_j(0)^2$. The two choices for including $p$ in the common divisor $j$ therefore give local sum
$(1-c_p)^2((1+\alpha_p^K)^2-(\alpha_p^K)^2)=(1-c_p)^2(1+2\alpha_p^K)$.
There is no division by $1+\alpha_p^K$. Integrability and the absolute bound (10) justify the computation first on finite prime sets and then by convergence. Outside $K$ it cancels the prefactor in (2) exactly since $(1-2c_p)(1+2\alpha_p^K)=1$. At $p\mid K,\ p\nmid r$, only $p/(p-1)$ is left. The factor $r/\varphi(r)$ restores the conductor primes, which all divide $K$. The result is (6), including the prime $2$.

## 3. Exact positive cuts, not an uncapped replacement

After the local collapse, for each real $v,x$ the two remaining geometric kernels are exactly (2) in the two-pole formula. The normalization before the physical integral is $-\chi(-1)M_K$, and the short arrays are those of Section 2 with the genuine finite cut $S$. We verify that the two actual real caps are (4). The proof of the [pointwise cap conversion, Section 3](r93-spectral-completed-colored-caps.md#3-convert-both-actual-geometric-kernels-keeping-the-finite-cutoff) applies with these coefficients; the specific convergence and sign checks are as follows.

Expanding $(u_1,u_2)=1$ by the exact $\sum_{j\mid(u_1,u_2)}\mu(j)$ leaves primitive $R_j$ for each variable after factoring out $j$ and the common factor $\alpha^K(j)^2$. For $j\le S^{1/2}$ its real log endpoint is $V_j=\log(S/j)\ge G/20$. The preceding tail and (10) give $\sup_{u\ge V_j}|R_j(u)|+\|R_j\mathbf1_{u>V_j}\|_1+\|R_j\mathbf1_{u>V_j}\|_2\ll Y^{-c_2}$ for some fixed $c_2>0$ in this range, since $r\le e^{2Z}$ and $M_j(\delta)\le\exp(O(G^\delta))$ for $Kj\le Y^{O(1)}$. The underlying finite unsigned coefficient mass is $Y^{o(1)}$ uniformly in these $j$ (bound it by the signed-convolution variation times $\sum_{n\le S}n^{-\beta}$). Subtracting the total mass $R_j(V_j)$ at the artificial endpoint to get a zero-total array thus costs a fixed power saving, uniformly for the displayed geometric kernels on the finite log square, which are bounded by powers of $G$. Its primitive is the clipped $R_j$ almost everywhere. Restoring the whole primitive costs a power saving by the same norm tails after integration by parts. The finite array terms at $j>S^{1/2}$ have the same power saving: for $j\le S$ their finite unsigned coefficient mass is still $Y^{o(1)}$, and $\sum_{j>S^{1/2}}|\alpha^K(j)|^2\ll S^{-1/8}\exp(O(G^\delta))$ by (10). The infinite-autocorrelation side past that $j$ cutoff is bounded by the full $rM_j(\delta)$ norms and the same moment. Thus all these artificial-cut errors, after the physical integrals and normalization, are $O_A(Y^\beta G^{-A})$, since $Y^{2\beta-1}\le Y^\beta$, $|1/L'(\beta,\chi)|\ll1$, and all remaining global factors are subpower.

For color zero the kernel is minus one-half the function $g_T(s)=|s|\min(T,|s|)$, divided by $\log x$, evaluated at $s=\log(u_1/u_2)$ and $T=T_{v,x}$. Signed integration by parts twice gives the **negative** pairing of the two primitives against $g_T''=2\mathbf1_{(-T,T)}-T(\delta_{-T}+\delta_T)$. This holds by smoothing for finite signed arrays with zero total; continuity of the autocorrelation handles the two endpoint masses. The geometric $-1/2$ then yields $\mathcal A_0(v,x)/\log x$, with its stated sign.

For color one, put $\rho=|\log(u_1/u_2)|$ and $k=(U_v-\log\max(u_1,u_2))_+$. The true width equals $T_{v,x}/2-k$ because $T_{v,x}/2-U_v>0$ for large $Y$ by the fixed $B_0>0$. Its numerator before division by $\log x$ is $(T_{v,x}/2)^2-(T_{v,x}/2)\rho-T_{v,x}k+k^2+k\rho$. The constant factor vanishes on zero-total coefficients and the $|\cdot|''=2\delta_0$ term gives $T_{v,x} C_K(0)$ after normalization. The two other terms retain their **finite** cuts exactly, since
$k=\int_0^{U_v}\mathbf1_{\log u_1\le s}\mathbf1_{\log u_2\le s}\,ds$ and
$k^2+k\rho=(U_v-\log u_1)_+(U_v-\log u_2)_+$.
The latter identity follows by taking the larger logarithm first. Their associated labels are at most $e^{U_v}<S$; after factoring $j$ they give respectively $Q_K(U_v)$ and $J_K(U_v)$ by finite signed Fubini. Thus the actual second kernel is $\mathcal A_1(v,x)/\log x$. This proves (4) with both genuine moving endpoints and distinct colors. Inserting them into the aligned case of the signed-mean projection gives (5), including the parity half factor.

## 4. Conditional sign of the actual aligned parity difference

Use the full primorial assumptions of Theorem 2. For $p>z$, $\alpha_p^K=O(p^{-\beta})$ with small absolute value, and for every other prime it is zero. Thus $R_1(u)=1$ for $0\le u\le\ell$; no integer with a prime factor greater than $z$ has entered. Moreover if $\alpha^K(j)\ne0$ and $j>1$ then $j>z$. Since $U_v\le\ell$, (3) gives exactly

$$
          Q_K(U_v)=M_K U_v,\qquad J_K(U_v)=M_K U_v^2.
 \tag{11}
$$

There is no need to infer a sign for the whole signed autocorrelation. Its value at zero has a direct lower bound. For any $j$ occurring with nonzero weight, removing its prime Euler factors convolves $R_1$ with the signed geometric product
$\prod_{p\mid j}\sum_{k\ge0}(-\alpha_p^K)^k\delta_{k\log p}$,
whose total variation is at most $\prod_{p\mid j}(1-|\alpha_p^K|)^{-1}$. This uses $|\alpha_p^K|<1$ here, since all these primes exceed $z$. Hence the whole $j>1$ absolute contribution at zero in (3), after dividing by $M_K$, is at most

$$
   \|R_1\|_2^2
   \left\{\prod_{p>z}\left(1+\frac{|\alpha_p^K|^2}{(1-|\alpha_p^K|)^2}\right)-1\right\}
                 \ll z^{1-2\beta}\|R_1\|_2^2 .
 \tag{12}
$$

The infinite product is bounded by its summable positive exponents, using the integer sum $p^{-2\beta}$ beyond $z$. As $M_K>0$, this gives
$C_K(0)\ge M_K(1-O(z^{1-2\beta}))\|R_1\|_2^2
\ge M_K(1-O(z^{1-2\beta}))\ell$.
On the true central support $T_{v,x}\asymp\ell$ uniformly, since $\ell$ ranges between $\epsilon\log G$ and $\log G$ while $T_{v,x}=2B\log\log v+O(1)$. By (11),

$$
     \mathcal A_1(v,x)
       \ge M_K\{T_{v,x}(\ell-U_v)+U_v^2
                              - O(z^{1-2\beta}T_{v,x}\ell)\}
       \gg M_K\ell^2 .
 \tag{13}
$$

To see the last lower bound uniformly up to $U_v=\ell$, split at $U_v=\ell/2$. In the first range use $T_{v,x}(\ell-U_v)\ge T_{v,x}\ell/2$; in the second use $U_v^2\ge\ell^2/4$ while the other main term is still nonnegative. The subtracted term is negligible. This argument gives a fixed sign for this color in the averaged primitive model without making a claim about the other color.

To quantify the normalization, the ordinary factor product in (2) over $p>z$ is $1+O(z^{1-2\beta})$, positive. The conductor factor and the $p/(p-1)$ terms over the other primes of $K_z$ together give $K_z/\varphi(K_z)$. For the remaining real positive finite factors,
$\prod_{p\mid K_z,\ p\nmid r}E_p^2\ge\exp(-2\sum_{p\le z}p^{-\beta})\gg\ell^{-2}$.
Indeed $E_p^2\ge(1+p^{-\beta})^{-2}$, and the reciprocal prime sum is $\log\log z+O(1)$ also at this exponent: the difference from exponent one is at most
$(1-\beta)e^{(1-\beta)\ell}\sum_{p\le z}(\log p)/p=O((1-\beta)\ell e^{(1-\beta)\ell})=o(1)$.
We used the elementary reciprocal prime estimates here. Finally the near-exception inequality (11.10) of [Montgomery--Vaughan, Chapter 11](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF), also the reciprocal bound in the two-pole proof, gives $|L'(\beta,\chi)|\ll(\log r)^2$ by taking the limit at the simple zero. Thus $M_K\ell^2\gg(K_z/\varphi(K_z))(\log r)^{-4}$.

Subtract the two parities in (5): only color one remains, with coefficient $-\chi(-1)$ rather than a half. The genuine correction is real on these tests, since the band projection of the real left profile in R87 (9) is real and the remaining factors there are real. For nonnegative fixed weights its sign-adjusted integral is at least a constant times
$Y^{2\beta-1}G^{-1}(K_z/\varphi(K_z))(\log r)^{-4}(\int_J w)(\int_1^2\eta)$,
using $x,v-x\asymp Y$ and the true physical change of variables. The factor $Y^{2\beta-1}$ is $Y\exp(-2(1-\beta)G)$, so under the stated small-gap assumption this lower bound is at least an inverse fixed log power of $Y$ times $Y$; use $\log r\le2Z$ and $K_z/\varphi(K_z)\ge1$. Choosing the error exponent in (5) sufficiently large relative to $C_*$ makes the error smaller than half the lower bound on the given fixed tests. This proves (7), as a conditional implication for the actual signed means on the complete aligned family.
