# A genuine critical-shell energy lower bound on powers of two

Keep the exact critical-shell setup and notation of [the polynomial-width inverse-logarithmic energy theorem](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md). In particular $X=\sqrt N$, $L=\log N$, $e(z)=e^{2\pi iz}$, $\mathcal Q=[.8X,.9X]\cap\mathbb P$, and

$$
 D_m=\mathbf1_{N-y\le m<N/2}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                        (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_mD_m e(\alpha m).
$$

**Theorem (global Dirichlet GRH).** Assume GRH for all primitive Dirichlet $L$-functions, including $\zeta$. For $N=2^J$ as the integer $J$ tends to infinity, take the actual hard intervals

$$
 y=9N/16,\qquad I_d=[X,1.01X],\qquad
 I_k=(\max(N^{.49999},.42X),.50X).
$$

Then there is an absolute $c_*>0$ such that

$$
 \int_{-1/(10N)}^{1/(10N)}
       \sum_{q\in\mathcal Q}\sum_{1\le a<q}|D(a/q+\beta)|^2\,d\beta
       \ \ge\ c_*\frac{N}{L} \tag{1}
$$

for all sufficiently large $J$. The same lower bound holds after projecting away the constant on each $q$'s nonzero-numerator group. This is a lower bound for the **complementary energy**, not for either signed pairing, an individual compensated offset, or Hypothesis S. Its scale shows that a uniformly smaller energy bound is not available on these hard intervals under the stated assumptions.

## 1. The full modular norm and its exact rational part

Use the common genuine smoothing at $\delta=L^{-2}$ and cutoff $T=L^{16}$ of [the preceding transfer](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#1-actual-transfers-at-the-smaller-smoothing-width), with $\Omega(x)$ inward on $[7/16,1/2)$, and the common cofactor cutoff $w(k)=W(\log k)$ inward on $I_k$. We use the usual mollifications equal to one on the interior beyond the endpoint strips. The true squared ordinary error is $O(NL^{-2})$, with the smaller $O(NL^{-8})$ arithmetic truncation error included. Here all retained squarefree $l$ are odd, the short inclusion labels are exactly $h=1,2$ with signs $\mu(h)$, and $d=su,\ s=(l,d)\mid l,\ (u,lN)=1$, $k$ a multiple of $l^2h/s$. The hard divisor interval lies in a single dyad with $A_0=K_0=X$, so $x_q=Xs/(q l^2)$.

In the finite character transform of [the integrated determinant proof, §2](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#2-integrate-in-the-complete-square-and-dispatch-its-off-diagonal), put the character factor $\chi(l^2)$ into the residue rather than outside the sum. Explicitly, let $\mathcal S_q(v)$ be its integrated vector extended to all retained $l,s$ with scalar signs $\mu(l)\mu(s)$ and residue $v=l^2hu/j\bmod q$. It retains $|\tau|\le L^4$ and $0<|j|\le N^{1/1000}$, with weight

$$
 \widehat G_\beta(\tau)\,
 \mu(l)\mu(s)\frac{\mu(h)x_q}h\,a_\tau(u)\,
                           \widehat f_\tau(jx_q/h)\,d\tau ,
 \qquad
 a_\tau(u)=\mu(u)\mathbf1_{su\in I_d}\mathbf1_{(u,lN)=1}
                        e(\tau\log(su/X)).
$$

All $l,h,j$ are units modulo $q$ for large $N$. Also $q\nmid d$ on the actual hard support, since $q\le.9X<X$ and $2q\ge1.6X>1.01X$, so no multiple of $q$ is in $I_d$. In particular $q\nmid u$ and $\mathcal S_q(0)=0$. Its transform on units, $Z_q(\chi)=\sum_{v\ne0}\mathcal S_q(v)\chi(v)$, gives the true nonprincipal character polynomial of the finite approximation times the inverse of the common Gauss factor, whose modulus is $\sqrt q$.

By exact orthogonality the pre-additive squared nonprincipal character norm of this approximation, summed over $q$, is

$$
 \sum_q q\sum_{\chi\ne\chi_0}|Z_q(\chi)|^2
 =\sum_q q(q-1)\sum_v|\mathcal S_q(v)|^2
       -\sum_q q\left|\sum_{v\ne0}\mathcal S_q(v)\right|^2 . \tag{2}
$$

The subtractand must be removed for a lower bound. It is the artificial principal of the finite character formula, not the actual constant additive mode.

The completed term in (2), on expansion with both integrated frequencies, is determined by
$l_1^2h_1 j' u_1-l_2^2h_2j u_2=bq$.
The $b\ne0$ terms in absolute total are $O(N^{1.91}L^{O(1)})$, uniformly in $\beta$. In fact the inherited GRH sup norm for $a_\tau$ is $O((X/s)^{4/5})$ on the exact interval and with its true mask; the second long Fourier factor has $L^2$ norm $O(\sqrt X)$, and the distinct $bq$ frequencies give $O(X^2\sqrt{\#\mathcal Q})$ for the third. The new $l_i^2$ factors are only integral dilations and enlarge the $b$ range by $T^2$; all $h,l,s$ labels and time $L^1$ weights cost only logarithmic powers, and the $j,j',b$ count costs $N^{3/1000}$ times logarithmic powers. This is the same conditional additive-Möbius input as in that proof.

For $b=0$, the condition is equality of $\rho=j/(l^2hu)$, and the result is a positive squared norm in the genuine common rational coordinates $(q,\rho)$, with weights $q(q-1)$. The [rational-only $j,\tau$ restoration, §3](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#3-restore-the-exact-physical-integral-on-the-rational-diagonal-only) at $\delta=L^{-2}$ changes the squared norm by $O_A(N^2L^{-A})$ for any fixed $A$: at fixed $l,s$, rescaling its old coordinate by $l^{-2}$ is an isometric relabeling, and triangle across the logarithmically many labels pays for only negligible errors. There is no $h$ restoration here. Invert the physical Fourier integral on this analytical diagonal only. Each coordinate is now the sum

$$
 \mathcal R_q(\rho)=
  \sum_{\substack{l\le T,\ l\ \mathrm{odd\ squarefree},\ s\mid l,\ h=1,2\\
                         su\in I_d,\ (u,lN)=1\\
                         \rho l^2hu\in\mathbb Z\setminus\{0\}}}
   \frac{\mu(l)\mu(s)\mu(h)\mu(u)N}{q l^2h u}
   \int \Omega(x)e(\beta Nx)w(Nx/(su))e(-\rho Nx/q)\,dx . \tag{3}
$$

The normalized cofactor bump equals one on the physical support. This common physical formula is exact in the rational vector and is not applied to a modular inverse of an unrestricted $j$.

## 2. A positive proportion of denominators with a nonzero coherent coordinate

Fix a sufficiently large constant $B$, independent of $J$. Consider squarefree integers $c\in[1.002X,1.008X]$ with no prime factor $\le B$. At $\rho=1/c$, whenever $l\le B$ the integrality condition in (3) reduces to $c\mid u$, since $c$ is coprime to $l$ and $h$. The original divisor support forces $u=c,s=1$ (every larger positive multiple or $s\ge2$ leaves $I_d$). Both $h=1,2$ then contribute. On the support of $\Omega$, $Nx/c$ lies strictly inside the fixed proportional cofactor interval, a fixed positive relative distance from both endpoints for all large $J$, since $N^{.49999}/X\to0$. Hence $w(Nx/c)=1$. The total part with $l\le B$ is exactly

$$
 \frac{\mu(c)N}{2q c}
      \left(\sum_{\substack{l\le B\\l\ \mathrm{odd}}}\frac{\mu(l)}{l^2}\right)
      \int \Omega(x)e((\beta N-N/(qc))x)\,dx . \tag{4}
$$

Its modulus has an absolute positive lower bound, independently of $B\ge2$. Indeed the odd sum is at least $1-\sum_{n\ge3}n^{-2}>0$. Also $\int\Omega\gg1$, $|\beta N-N/(qc)|\le1.35$, and the physical support has length $1/16$. After rotating by the phase at its midpoint the real part of the exponential is bounded below by a positive constant throughout; the test is nonnegative. Finally $N/(q c)\asymp1$. Write $a_0>0$ for this uniform lower bound on (4).

For a larger $l$, put $r=(c,l)$. Squarefree $c$ and $h\in\{1,2\}$ give $c/r\mid u$ exactly. On writing $u=(c/r)v$, the true $su\in I_d$ places $v$ in an interval of fixed ratio $1.01$ around $r/s$. Thus the absolute reciprocal sum $1/v$ on this interval is $O(1)$, including empty or short intervals; any remaining unit restrictions can only reduce it. Since the integral in (3) is $O(1)$ and $N/(qc)\asymp1$, the total tail at this coordinate is bounded uniformly in $q,\beta$ by a fixed constant times

$$
                  \mathcal T_B(c)=
                   \sum_{B<l\le T}\frac{\tau_{\rm d}(l)(c,l)}{l^2}. \tag{5}
$$

Here $\tau_{\rm d}$ is the divisor function; extending the positive $l$ bound is harmless.

Average (5) over all integers in the interval for $c$. By $(c,l)=\sum_{d\mid(c,l)}\varphi(d)$, the sum of $(c,l)$ is $O(X\tau_{\rm d}(l)+l)$, because each modulus $d$ has $O(X/d+1)$ multiples and $\sum_{d\mid l}\varphi(d)=l$. Consequently the sum of (5) divided by $X$ is at most

$$
 O\left(\sum_{l>B}\frac{\tau_{\rm d}(l)^2}{l^2}
       +\frac1X\sum_{l\le T}\frac{\tau_{\rm d}(l)}l\right)
                       = O(B^{-3/4})+o(1). \tag{6}
$$

Use $\tau_{\rm d}(l)^2\ll l^{1/4}$ and $T=L^{16}$.

For the fixed mask $M_B=\prod_{p\le B}p$, the squarefree $M_B$-units have density
$\zeta(2)^{-1}\prod_{p\le B}(1+1/p)^{-1}$
with hard-prefix error $O_B(\sqrt X)$ on this interval: expand $\mu^2(c)=\sum_{a^2\mid c}\mu(a)$, count units at each progression $c=a^2v$, and bound the tail of the absolutely convergent density. The density is $\gg B^{-1/2}$, even by replacing the odd primes by all odd integers in $\sum_{3\le p\le B}\log(1+1/p)$. The length of the interval is $.006X$. Choose $B$ fixed large enough that (6) makes the number of bad $c$ for which the tail bound exceeds $a_0/2$ less than half this density times the length, for all sufficiently large $J$. This uses only the nonnegative first moment (6) and holds simultaneously for all $q,\beta$. At least a fixed positive multiple of $X$ of the admissible squarefree $c$ therefore satisfy

$$
                         |\mathcal R_q(1/c)|\ge a_0/2
$$

for every $q\in\mathcal Q$ and every $\beta$ under consideration. These rational coordinates are distinct. Since the prime number theorem gives $\#\mathcal Q\gg X/L$, their contribution is

$$
    \sum_q q(q-1)\sum_{\rho\ne0}|\mathcal R_q(\rho)|^2
                                   \gg N^2/L                 \tag{7}
$$

uniformly in $\beta$. This is the exact completed rational diagonal; no other rational coordinates are needed for (7).

## 3. Subtract the artificial term and return to actual numerator energy

For the subtractand in (2) use the **finite** array, not (3). Summing its $v$ labels imposes no further restrictions because all are units. At fixed $l,s,h,\tau$ the $u$ and $j$ sums factor. The signed $u$ sum is $O((X/s)^{4/5})$, the same uniform GRH bound as above at zero additive frequency. For $z=x_q/h>0$ the Fourier envelope $|\widehat f_\tau(\xi)|\ll\min(1,(Y_\tau/|\xi|)^2)$ yields

$$
 z\sum_{j\ne0}|\widehat f_\tau(jz)|\ll Y_\tau,
       \qquad Y_\tau=1+L+|\tau|,
$$

by separating $0<|j|\le Y_\tau/z$ and its tail. This bounds the truncated $j$ sum as well. Since $|\tau|\le L^4$, the $L^1$ norm of $\widehat G_\beta$ and the exterior $l,s,h$ counts give
$\left|\sum_{v\ne0}\mathcal S_q(v)\right|\ll X^{4/5}L^{O(1)}$.
Using $\sum_q q=O(X^2)$, the subtractand in (2) is therefore $O(N^{1.8}L^{O(1)})$. Subtracting it, the nonzero determinant error, and arbitrarily small rational restoration errors from (7) leaves a lower bound $\gg N^2/L$ for the finite nonprincipal character norm.

For clarity, the exact additive projection identity at each prime $q$ sends the nonprincipal character sums $\sum_m C_m e(\beta m)\chi(m)$ of a coefficient array $C$ to the mean-zero part of its additive vector on $1\le a<q$. By the finite Gauss identity the squared factor is $q/(q-1)$, since each nonprincipal Fourier coefficient on the multiplicative numerator group is that sum times a Gauss factor, and Parseval divides by $q-1$. It is at least one, so the same lower bound transfers to the finite approximation's centered additive energy for each $\beta$. The original modular time and dual cutoff errors are negligible in the sampled norm, uniformly in $\beta$, by the inherited separated-center and Fourier-tail bounds. Over the $\beta$ interval of length $1/(5N)$ this gives $\gg N/L$ for the centered smoothed polynomial. Finally the disjoint arcs and ordinary Parseval bound the true squared hard-cut discrepancy by $O(NL^{-2})$; projection is a contraction. Norm triangle gives the same lower bound for the literal hard coefficient. Adding the true additive constants cannot decrease its squared norm. This proves (1), including the centered assertion; it leaves the signed covariance open at this lower-bound scale.
