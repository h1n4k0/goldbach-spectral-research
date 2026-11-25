# The genuine critical prime shell on one polynomial divisor dyad under global GRH

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$ and $e(v)=e^{2\pi i v}$. Keep the genuine prime polynomial $P$, including its two disjoint prime boxes, actual product unit test and permissible bounded selector, and the actual critical prime shell of the [unconditional fixed-log-width theorem](weak-s-type-ii-critical-prime-unconditional-all-targets.md). In its complementary coefficient now restrict the signed long divisor to **one** dyad. Thus take a real $1\le\lambda\le N^{1/100000}$, put $A_0=\lambda X$, $K=X/\lambda$, and let $I_d\subset[A_0,2A_0)$ be any hard interval. Let $J=[N-y,N/2)$, $N/2\le y\le9N/16$, and retain the actual hard cofactor interval $I_k$, which includes $k>t\ge N^{.49999}$. Write

$$
 D_m=\mathbf1_{m\in J}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                        (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_mD_m e(m\alpha).
$$

The critical shell uses prime $q\in\mathcal Q=[.8X,.9X]\cap\mathbb P$, nonzero numerators $1\le a<q$, and $|\beta|\le1/(10N)$.

**Theorem (global Dirichlet GRH).** Assume GRH for all primitive Dirichlet $L$-functions, including $\zeta(s)$. Uniformly in the even target, the moving single dyad, and all actual hard endpoints, for each $\epsilon>0$,

$$
 \mathcal E_N(D)
   :=\int_{-1/(10N)}^{1/(10N)}
      \sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}|D(a/q+\beta)|^2\,d\beta
    \ll_\epsilon N L^{-1/2+\epsilon}.
 \tag{1}
$$

The actual signed full shell, its separately centered numerator covariance and the exact parity-preserving signed even-lattice residual of length $M=\lceil XL^2\rceil$ are consequently $O_\epsilon(N L^{-1/4+\epsilon})$, with every original unit prime retained. The only use of GRH is the off-diagonal additive Möbius estimate in §3; the new signed estimate for determinant zero is unconditional. The exponent $1/100000$ covers every dyad with nonempty actual support under the given $k>t$ and $dk<N/2$. This is a bound for each individual dyad, not for their full union: a polynomial-width interval can meet $\asymp L$ dyads. There is no claim on other shells, individual compensated-offset squares, or Hypothesis S.

## 1. Literal endpoint and arithmetic transfers on the polynomial dyad

The support satisfies $7/32\le k/K<1/2$ when $m\in J$. As in the [signed endpoint proof for logarithmically wide dyads](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md#2-uniform-exact-transfers-on-one-divisor-dyad), smooth only the physical and short-label gates at relative width $\delta=L^{-1/2}$, preserving their actual interiors and retaining the hard $d$ cut. Write the real weights as $\Omega(m/N),w(k/K)$, with the short weight compactly supported in a fixed positive proportional interval, and with localized first and higher derivatives as in that proof. An extra fixed smooth bump equal to one on the actual normalized cofactor range is harmless (it need not be localized). A cutoff shorter than the chosen smoothing width may be replaced by zero and charged to its endpoint layer.

We check the scope of the ordinary endpoint estimates here. On squarefree support use the genuine signed short label $\mu(k)$, with the common factor $\mu(m)$ and masks removed only after squaring. For a physical strip of length $H_{\rm phys}\asymp N\delta$ the proof just cited gives

$$
 O\big(H_{\rm phys}(1+\log(N/H_{\rm phys}))+K\sqrt{A_0}\big)
          \ll N\delta L_2+N^{3/4}.
$$

Indeed the fixed-$g$ short-divisor floor bound is $O(H_{\rm phys}/g+A_0)$, and the large-$g$ floor is $O(K^2/G)$; its cutoff $\lfloor\min(N/H_{\rm phys},K/\sqrt{A_0})\rfloor$ is still at least one. Here $K\sqrt{A_0}=N^{3/4}/\sqrt\lambda$. For a sharp cofactor strip of width $O(\delta K)$, the signed narrow lcm bound used in that proof applies at $K$ because $\log K\asymp L$ and its masked reciprocal estimates and cutoff $\exp(L_2^3)$ are uniform at this scale. Its continuous main is $O(N\delta)$: the form is $O_B(\delta+K^{-1}+\delta^2L_2^3+L^{-B})$ for fixed $B$. The quoted actual small-gcd corrections are bounded by

$$
 N\delta^2(1+\log(2G))+\delta A_0G+\lambda^2G^2
$$

with large-gcd floor $O(K^2/G)$. Taking $G=\lfloor L^3\rfloor$ makes this $O(N\delta)$ throughout $\lambda\le N^{1/100000}$. Indeed the latter two displayed terms are $N^{1/2+1/100000+o(1)}$ and $N^{2/100000+o(1)}$. These arguments handle moving strict endpoints and finite-BV weights by the same prefix Minkowski principle. Thus the smoothing squared error is $O_\epsilon(NL^{-1/2+\epsilon})$.

As in [the exact all-unit transfer, §1](weak-s-type-ii-critical-prime-full-unit-dual-determinant-grh.md#1-keep-exact-long-units-and-cut-only-the-auxiliary-short-inclusion), put

$$
 F_{m,N}=\sum_{\substack{dk=m,\ d\in I_d\\(d,N)=1}}\mu(d)w(k/K).
$$

This raw coefficient is supported on a fixed compact proportional $m/N$ range, even before multiplication by $\Omega$. On the actual product-unit support, the squarefree coefficient is $\mu^2(m)\mathbf1_{(m,N)=1}F_{m,N}$, before $\Omega$. Keep the exact long units, insert a squarefree cutoff $T=L^4$ while the true unit mask is present, and then approximate the short units with inclusion labels $h\mid\operatorname{rad}N$, $h\le H_0:=\exp(C_0L_2^2)$, for a sufficiently large fixed $C_0$. The resulting coefficient before the physical weight is

$$
 B_m^\dagger=F_{m,N}
 \left(\sum_{\substack{l\le T,\ l^2\mid m\\(l,N)=1}}\mu(l)\right)
 \left(\sum_{\substack{h\mid\operatorname{rad}N,\ h\mid m\\h\le H_0}}\mu(h)\right).
 \tag{2}
$$

The exact long unit test implies $h\mid m$ iff $h\mid k$ in each summand. The condition $(l,N)=1$ is imposed when the full product unit is still present, before broadening the short inclusion. Thus (2) represents a controlled approximation, not a claim of coefficient equality after the two truncations.

Here are the needed uniform ordinary estimates on the present dyad, including without $\Omega$. Restrict the product variable to a fixed broad interval $[cN,CN]$ that contains the exact dyadic support with $w$; the proofs count intervals on this same scale. The signed forced-square estimate of the endpoint proof extends with the exact long units, just as in [the unconditional all-target proof, §3](weak-s-type-ii-critical-prime-unconditional-all-targets.md#3-preserve-the-exact-cuts-through-smoothing-and-squarefree-truncation):

$$
 \sum_{\ell^2\mid m}|F_{m,N}|^2
 \ll C_1^{\omega(\ell)}\frac{N}{\ell^2}
             \bigl(L_2^2+1+\log(2\lambda\ell)\bigr)
 \qquad(\ell\text{ squarefree}).
 \tag{3}
$$

The signed continuous form is bounded by removing the prime divisors of $\ell$ from the two squarefree signed labels, then applying the reciprocal coprime DIT norm at mask $N\ell$; it costs at most $L_2^2$ and the displayed fixed Euler factor. Only $\ell\ll\sqrt N$ need be used. With $g=(a,b)$ for the signed labels, the large-gcd floor uses $G=\lceil\lambda^2\ell^2\rceil$, giving $O(A_0^2/G)=O(N/\ell^2)$. On the small-gcd side write $m=guv z$, $u,v\asymp A_0/g$, $z\asymp g/\lambda^2$. The four disjoint possibilities for a prime of $\ell$ (occurring in exactly one of $g,u,v$, or in none of them) give the same elementary upper integer counts and reciprocal continuous correction as in the cited proof, since the imposed total modulus in all four coordinates is $\ell^2$. No extra $+1$ in counting positive multiples is needed; empty intervals count zero. Thus only $\log(2\lambda\ell)=O(L)$ replaces previous logarithmic-width losses.

For squarefree $r\mid N$, the [true forced divisibility estimate of the all-unit transfer](weak-s-type-ii-critical-prime-full-unit-dual-determinant-grh.md#1-keep-exact-long-units-and-cut-only-the-auxiliary-short-inclusion) similarly remains

$$
 \sum_{r\mid m}|F_{m,N}|^2
       \ll \frac Nr\bigl(L_2^2+1+\log(2\lambda r)\bigr).
 \tag{4}
$$

In detail, $[a,b,r]=r[a,b]$ because both signed $d$ labels are exact $N$-units. The continuous signed lcm bound is $O(NL_2^2/r)$ by the reciprocal coprime DIT form. With $G=\lceil\lambda^2r\rceil$, large-$g$ floors are $O(N/r)$. In the actual small-$g$ range $r\mid z$ exactly, so the positive integer upper count at $g$ is $O(N/(gr))$; its continuous counterpart follows from $rguv$ in the denominator. These bounds require only the dyadic geometry, not polylogarithmic $\lambda$. Bounded-BV short weights follow in (3)–(4) by hard prefixes and Minkowski as before.

The squarefree omission squared costs $O(N L T^{-1+\rho})$ for fixed $\rho>0$, by grouping the two omitted labels by their squarefree lcm as in (3). At $\rho=1/4$ and $T=L^4$ this is $O(NL^{-2})$. The full short-unit tail squared costs at most

$$
 NT^2 L\sum_{\substack{r\mid\operatorname{rad}N\\r>H_0}}\frac{3^{\omega(r)}}r
       \ll NT^2 L\,e^{-C_0L_2}L_2^{O(1)}
$$

by (4) and Rankin at $1/L_2$ exactly as in the cited all-unit argument; choose $C_0$ so it is $O(NL^{-2})$. These ordinary errors hold also with $\Omega$ by contraction. Finally the genuine ordinary squared norm without $\Omega$ is $O(N)$: on squarefree product support use the signed short $k$ and DIT form on the interval of $k$ at each real product, with absolute floor total $O(K^2)\le O(N)$. The remaining bounded-BV $w$ is obtained from hard prefixes. Therefore

$$
                         \sum_m|B_m^\dagger|^2=O(N).
 \tag{5}
$$

No GRH has been used in these transfers.

## 2. The two different Fourier truncations

Put $G_\beta(v)=\Omega(e^v)e(\beta N e^v)$ and use ordinary Fourier transform $\widehat f(\xi)=\int f(z)e(-z\xi)\,dz$. Exact product inversion for the approximant gives

$$
 \sum_m \Omega(m/N)B_m^\dagger e((a/q+\beta)m)
   =\int_{\mathbb R}\widehat G_\beta(\tau)
               \sum_m B_m^\dagger e(\tau\log(m/N))e(am/q)\,d\tau.
 \tag{6}
$$

Uniformly on the actual $\beta$ interval,

$$
 |\widehat G_\beta(\tau)|\ll\min(1,|\tau|^{-1},\delta^{-1}|\tau|^{-2}),
 \qquad |\widehat G_\beta(\tau)|\ll_r\delta^{1-r}|\tau|^{-r}\quad(r\ge2).
$$

For the large $\tau$ tail use the entire actual additive expression (6), not a termwise long-residue bound. For each $\tau$ its coefficient norm is the same as (5). The distinct reduced centers $a/q$ have spacing $\gg N^{-1}$, so for any such Fourier polynomial $F$ of degree $O(N)$,
$\sum_{q,a}|F(a/q)|^2\ll N\int_0^1 |F|^2$.
Indeed take disjoint intervals of length $\asymp1/N$ at the centers, average the inequality from integrating $(|F|^2)'$, and sum; the derivative error is at most $2\|F\|_2\|F'\|_2$ and $\|F'\|_2\ll N\|F\|_2$. Thus the vector norm in $(q,a)$ of the inner sum in (6) is $O(N)$ uniformly in $\tau$. With the true bounded support, higher derivatives of $G_\beta$ make the integrated norm from $|\tau|>L^{D_\tau}$ negligible to any fixed inverse log power, for instance with fixed $D_\tau=4$ and a sufficiently high fixed derivative order. This step incurs no factor $\lambda$.

For retained $\tau$, now split (2) exactly as in the [joint all-unit completion, §2](weak-s-type-ii-critical-prime-full-unit-dual-determinant-grh.md#2-joint-poisson-norm-with-every-allowed-inclusion-label). For a squarefree $l\le T$, $(l,N)=1$, take $s=(l,d)$, $d=su$, $k=(l^2/s)hv$, with the actual long conditions $(u,lN)=1$ and $su\in I_d$. Put

$$
 U=A_0/s,\quad x_0=Ks/(Xl^2),\quad x_q=Ks/(q l^2),\quad
 f_\tau(t)=w(t)e(\tau\log t),\quad Y_\tau=1+\delta^{-1/2}+|\tau|.
$$

Then $U x_0=X/l^2$ and $x_q\asymp x_0$. The common long array is $a_u=\mu(u)\mathbf1_{su\in I_d}\mathbf1_{(u,lN)=1}e(\tau\log(su/A_0))$. With $U_\chi=\sum_u a_u\chi(u)$, the nonprincipal character expression at this $l,s$ is, up to the common factor $\mu(l)\mu(s)\chi(l^2)$,

$$
 \tau_q(\chi) U_\chi
    \sum_{\substack{h\mid\operatorname{rad}N\\h\le H_0}}
     \frac{\mu(h)x_q\chi(h)}h
         \sum_{j\ne0}\overline{\chi(j)}\,\widehat f_\tau(jx_q/h),
       \qquad |\tau_q(\chi)|=\sqrt q .
 \tag{7}
$$

Fourier decay and the positive support give

$$
 |\widehat f_\tau(\xi)|\ll\min(1,(Y_\tau/|\xi|)^2),\qquad
               |(\widehat f_\tau)'(\xi)|\ll1
 \tag{8}
$$

(the second inequality follows from $\|t f_\tau(t)\|_1\ll1$). The first two localized physical derivatives give the first inequality using the Fourier transform of $f_\tau''$; higher derivatives cost $O_r((1+\delta^{-1}+|\tau|)^r)$.

For the dual cutoff, unlike the product-frequency cutoff, keep $0<|j|\le J_d:=\lambda N^\zeta$ with fixed $\zeta=1/1000$. The actual mesh $x_q/h\gg1/(\lambda T^2H_0)$, so $(x_q/h)J_d\ge N^{\zeta-o(1)}$. Hence

$$
 (x_q/h)\sum_{|j|>J_d}|\widehat f_\tau(jx_q/h)|
  \ll_r (1+\delta^{-1}+|\tau|)^r ((x_q/h)J_d)^{1-r}
       =O_A(N^{-A})
$$

for every fixed $A$ by taking fixed $r$ large enough. This pays for the entire finite sum, even using elementary polynomial-size bounds for the long residue norm and number of tuples. All retained $j,h,l$ are nonzero modulo $q$.

After removing the Gauss magnitude in the positive squared norm of (7), add the principal character algebraically, and then add the square of the zero residue group. The exact completed residue equation is

$$
                  h_1j' u-h_2j u'\equiv0\pmod q ,
 \tag{9}
$$

with weight

$$
 \frac{q(q-1)x_q^2\mu(h_1)\mu(h_2)}{h_1h_2}\,
     \widehat f_\tau(jx_q/h_1)
       \overline{\widehat f_\tau(j'x_q/h_2)}
$$

in front of $a_u\overline{a_{u'}}$. These positive additions are only an upper bound for the nonprincipal norm. They do not remove the actual principal and nonunit additive contributions.

## 3. The nonzero determinant, the only conditional step

When the determinant in (9) is a nonzero $bq$, fix $h_1,h_2,j,j',b$. For $A_\tau(\theta)=\sum_u a_u e(u\theta)$ the exact sum over $q$ is a Fourier integral of

$$
 A_\tau(h_1j'\theta)\overline{A_\tau(h_2j\theta)}
                       \sum_{q\in\mathcal Q}\omega_q e(-bq\theta),
             \qquad |\omega_q|\ll X^2.
$$

Since $b\ne0$, the last factor has squared norm $O(X^4\#\mathcal Q)$ by distinct frequencies. Either long factor has ordinary norm $O(\sqrt U)$ under its nonzero integral dilation. Under global GRH, the uniform additive bound of [Baker–Harman (1991)](https://academic.oup.com/jlms/article-abstract/s2-43/2/193/862020), stated in [He–Huang (1.4), p. 1](https://www.impan.pl/shop/en/publication/transaction/download/product/91740?download.pdf=), gives $O_\varepsilon(z^{3/4+\varepsilon})$ for all real frequencies of a Möbius prefix of length $z$. It gives here $\|A_\tau\|_\infty\ll U^{4/5}$: convolve with the indicator of $(lN)$-smooth integers to restore its complete mask, at reciprocal $3/4$-moment cost $\prod_{p\mid lN}(1-p^{-3/4})^{-1}=N^{o(1)}$; use Abel on the actual hard endpoints with the $(1+|\tau|)$ cost. The harmless losses are absorbed since $U\ge X/L^4$ and $\tau$ is fixed-polylogarithmic.

The number of tuples is at most $\lambda^4 N^{3\zeta+o(1)}$: $h_i\le H_0=N^{o(1)}$, each $j$ has length $O(\lambda N^\zeta)$, and $|b|\ll\lambda^2N^{\zeta+o(1)}$. Hölder using the preceding three norms bounds the combined nonzero determinant by

$$
 O\!\left(\lambda^4 N^{3\zeta+o(1)}
          U^{4/5+1/2}X^2\sqrt{\#\mathcal Q}\right)
       \ll N^{1.9+5.3/100000+3\zeta+o(1)}
       \ll N^{1.91}.
 \tag{10}
$$

This is a bound at each fixed $(l,s,\tau)$; every constant is uniform in the actual endpoints. It is here that fixed-power additive cancellation is used. No GRH estimate enters the signed zero determinant below.

## 4. The genuine signed zero determinant

Fix $q,h_1,h_2$ and let $g=(h_1,h_2)$, $w_q=x_q/g$, $w_0=x_0/g$. When (9) is an equality with value zero, the actual $N$-units $u,u'$ imply $h_1/g\mid j$ and $h_2/g\mid j'$. Write $j=(h_1/g)i$, $j'=(h_2/g)i'$. The new equation is $i' u=i u'$ and both sampled Fourier meshes are $w_q$. The two $i$ have the same sign $\sigma$. Uniquely write $i=\sigma d_0 r,\ i'=\sigma d_0 r'$ with $d_0,r,r'>0$ and $(r,r')=1$. Then $u=r z$, $u'=r'z$ for a positive integer $z$. Thus the signed factor before $z$ is $\mu(r)\mu(r')e(\tau\log(r/r'))$; the actual remaining count is

$$
       \sum_{\substack{z>0:\;r z,r'z\in I_u\\(z,lNrr')=1}}\mu^2(z),
            \qquad I_u=\{u:su\in I_d\}\subset[U,2U),
 \tag{11}
$$

with $(rr',lN)=1$. This uses the exact identity
$\mu(rz)\mu(r'z)=\mu(r)\mu(r')\mu^2(z)\mathbf1_{(z,rr')=1}$
on the squarefree $r,r'$ terms; nonsquarefree $r$ or $r'$ are zero. Both Fourier samples have arguments $\sigma d_0 r w_q,\sigma d_0 r'w_q$, and the original dual cutoffs remain two separate hard upper tests.

Partition $r$ dyadically, $R\le r<2R$, so the actual $r'$ lies in $[R/2,4R]$ whenever (11) is nonempty. Imposing this latter range is harmless. For $r,r'$ there are $O(R^2)$ choices and there are at most $O(U/R)$ positive $z$ per pair, with no additional $1$ required since $u\le2U$. Write $Z_*=\exp(L_2^5)$ and $F_*=\exp(L_2^2)$. These are subpower cutoffs.

### Large sampled arguments, and the short ratio region

First remove only from the zero determinant the contribution where at least one sampled argument has magnitude above $F_*$. Both then have magnitude $\gg F_*$ since $r,r'$ are comparable. By (8) at a fixed ratio dyad, the sum of absolute products over $d_0$ in this case is

$$
 \ll \sum_{d_0\gg F_*/(Rw_0)}
               \left(\frac{Y_\tau}{d_0 Rw_0}\right)^4
 \ll \frac{Y_\tau^4}{Rw_0F_*^3}.
$$

The estimate holds even if the indicated lower bound is below one, by the positive integer tail bound with $\max(1,F_*/(Rw_0))$. Multiplying by $O(R^2 U/R)$, then summing over $O(L)$ ratio dyads (all retained dual indices are polynomial), gives
$O((UY_\tau/w_0)L (Y_\tau/F_*)^3)$, negligible compared with $UY_\tau/w_0$ for fixed $D_\tau$.

Henceforth both arguments have magnitude at most $F_*$. Also, for $R\le Z_*^2$ use the unsigned bound without a squarefree count: the full Fourier envelope sum over $d_0\ge1$ is $\ll Y_\tau/(Rw_0)$ by (8), and the same $O(R^2 U/R)$ count gives $O(UY_\tau/w_0)$ per ratio dyad. The number of such dyads is $O(L_2^5)$. This pays only $L_2^5$ instead of a logarithm of $\lambda$.

### A squarefree count on the actual long common multiplier

On $R>Z_*^2$ with both sampled arguments still bounded, we can replace (11) by its continuous density. For a hard interval at upper size $B$ the elementary squarefree progression calculation, uniformly in integer mask $M_0$, is

$$
 \sum_{\substack{z\in I\\(z,M_0)=1}}\mu^2(z)
   = |I|\,\frac1{\zeta(2)}\prod_{p\mid M_0}(1+1/p)^{-1}
                   +O\big(\sqrt B\,2^{\omega(M_0)}\big).
 \tag{12}
$$

Indeed expand $\mu^2(z)=\sum_{a^2\mid z}\mu(a)$, restrict $(a,M_0)=1$, count units by inclusion with error $O(2^{\omega(M_0)})$, and extend the reciprocal-square sum above $\sqrt B$ at cost $O(\sqrt B)$. Endpoints preserve the uniform floor error. In (11), $B\asymp U/R$ and $M_0=lNrr'\le N^{1+2/100000+o(1)}$. The surviving ratio range is $R\ll F_*/w_0\le\lambda N^{o(1)}$, and $R/U\le N^{-1/2+o(1)}$ since $U x_0=X/l^2$ and $1/w_0=g/x_0$. Thus the full error of (12) at a fixed ratio dyad before $q$ weights is

$$
 \ll R^2\,\frac{F_*}{w_0 R}\sqrt{\frac UR}\,N^{o(1)}
        =\frac{U}{w_0}\,F_*\sqrt{\frac RU}\,N^{o(1)}
        \ll \frac{U}{w_0}N^{-1/4+o(1)} .
 \tag{13}
$$

Here $F_*/(w_0 R)$ is the positive upper count for $d_0$, and we used the uniform absolute bound on each Fourier sample. Summing over the ratio dyads keeps the power saving. Multiplication by the actual prefactor $q(q-1)x_q^2/(h_1h_2)$ turns $U/w_0$ into $O(q^2 X/(l^2[h_1,h_2]))$, so this error is compatible with the full subsequent $q,h_1,h_2$ sums, not only a per-pair comparison to an unrelated size.

### Signed reduced-variable cancellation for the remaining ratios

In the real $z$ integral of (12), the density is
$\mathfrak d(lN)\kappa(r)\kappa(r')$ with $\mathfrak d(lN)\le1$ and
$\kappa(a)=\prod_{p\mid a}(1+1/p)^{-1}$, since $(rr',lN)=1$ and $(r,r')=1$. Its factorization is used before removing the coprimality $ (r,r')=1$. Impose that condition by $\sum_{c\mid r,r'}\mu(c)$. For each fixed $z,d_0,c$ the two sums now separate, with possibly different hard intervals in $r$ and $r'$: intersect the ratio dyad, the $rz$ or $r'z$ condition, the original dual index bounds, and each low sampled-argument bound. All are genuine real intervals. The terms carry $\mu(r)\kappa(r)e(\tau\log r)\widehat f_\tau(\sigma d_0 r w_q)$ and the conjugate expression for $r'$.

For $c>R/Z_*$, count absolutely: the bounded-interval integer multiples give $O(R/c)$ choices on each side, and their product summed over such $c$ is $O(R Z_*)$. Keep the envelopes in $d_0$, whose sum is $O(Y_\tau/(Rw_0))$. The real $z$ interval has length $O(U/R)$, so this part at ratio $R$ is $O((UY_\tau/w_0)Z_*/R)$. It sums geometrically over $R>Z_*^2$.

For $c\le R/Z_*$, keep the signs. If $c$ is nonsquarefree or not a unit modulo $lN$, the corresponding array is zero. Otherwise substitute $r=c n$, retain $(n,lNc)=1$, and use
$\mu(r)\kappa(r)=\mu(c)\kappa(c)\mu(n)\kappa(n)$ on that exact coprime support. The new hard interval endpoints are $\asymp R/c\gg Z_*$ and the analogous relation holds for $r'$. Uniformly for any mask $M_1\le N^2$ and any prefix at size $v\gg Z_*$, the signed damped sum is

$$
 \sum_{\substack{n\le v\\(n,M_1)=1}}\mu(n)\kappa(n)
                  \ll v\exp(-c_1 L_2^{5/2}).
 \tag{14}
$$

Here and below $c_1>0$ denotes an absolute constant, not the divisor $c$. To prove (14), convolve ordinary $\mu$ with the nonnegative multiplicative coefficients at each prime: if $p\nmid M_1$, its local ratio is
$1+(1-\kappa(p))\sum_{j\ge1}p^{-js}$, and if $p\mid M_1$ its ratio is $(1-p^{-s})^{-1}$. This follows by dividing the local signed series by $1-p^{-s}$. The reciprocal moment at exponent $1-1/L_2$ is $L_2^{O(1)}$ uniformly: the unmasked Euler product converges uniformly since $1-\kappa(p)\le1/p$, and the masked factor is split at $L^2$ as in the [masked reciprocal estimate](weak-s-type-ii-critical-prime-unconditional-all-targets.md#1-the-signed-lcm-form-with-the-full-unit-mask). For convolution labels not exceeding $\sqrt v$ use the unconditional [Lee–Leong Mertens bound, (23)](https://arxiv.org/html/2208.06141v5#S2.SS2). Its exponent at $\log v\gg L_2^5$ dominates $L_2^{5/2}$ even after its $\log\log v$ factor. For the remaining labels, reciprocal Rankin gives cost $v^{-1/(2L_2)} L_2^{O(1)}$ after extracting the common $v$. This proves (14), including the hard interval version by subtracting prefixes. In our actual application $M_1=lNc\le N^2$ for large $N$.

On the exact retained interval the continuous weight has sup norm $O(1)$ and variation $O(1+|\tau|+d_0R w_q)=O(1+|\tau|+F_*)$, by (8) and the lower comparable ratio sizes. Thus Abel and (14) give $O((R/c)\exp(-c_2L_2^{5/2}))$ per inner sum, after decreasing the constant $c_2>0$. This also handles very short intervals. Multiply the two bounds and sum $c\le R/Z_*$ to obtain $O(R^2\exp(-c_2L_2^{5/2}))$. The number of allowed $d_0$ is $O(F_*/(Rw_0))$ and the real $z$ length is $O(U/R)$. Their product costs
$O((U/w_0)F_*\exp(-c_2L_2^{5/2}))$ for each ratio dyad. Summing the $O(L)$ dyads is harmless because the exponential dominates both these factors. This is the signed step that prevents a logarithm of $\lambda$ from surviving on the determinant-zero locus.

Combining the short ratio count, high sampled-argument bounds, the squarefree floors, and both continuous contributions, the completed inner diagonal at fixed $q,h_1,h_2$ is bounded in absolute value by $O(UY_\tau L_2^5/w_0)$, before its external weight. Multiplication by $q(q-1)x_q^2/(h_1h_2)$ and $U x_0=X/l^2$ give the reciprocal joint weight $1/[h_1,h_2]$. Summing $\sum_q q(q-1)\ll X^3/L$ and $\sum_{h_1,h_2\mid\operatorname{rad}N}1/[h_1,h_2]=\prod_{p\mid N}(1+3/p)\ll L_2^3$, the total zero determinant at a fixed $(l,s,\tau)$ is at most

$$
                         \ll \frac{N^2Y_\tau L_2^8}{L l^2}.
 \tag{15}
$$

This is unconditional. In particular the logarithm of the long dyad ratio, which can be of order $L$ in the unsigned count, has been replaced by fixed powers of $L_2$ with the actual signs and endpoints.

## 5. Restore the exact shell and the true coefficient

Take square roots of (10) and (15), and use Minkowski over $\tau,l,s$. The physical Fourier estimate gives $\int|\widehat G_\beta(\tau)|\sqrt{Y_\tau}\,d\tau\ll\delta^{-1/2}$ as in the fixed logarithmic theorem. The diagonal label sum costs $\sum_{l\le T}\tau_{\rm d}(l)/l\ll(1+\log T)^2$, with $\tau_{\rm d}$ the divisor function. The power error (10) and all discarded tails absorb the crude fixed-polylogarithmic label count, or the tail of (6) measured directly there. The exact additive nonprincipal expansion changes the squared norm by at most $q/(q-1)$. Integrating on the real $\beta$ interval of length $1/(5N)$ and using $\delta=L^{-1/2}$ now gives $O_\epsilon(N L^{-1/2+\epsilon})$ for the nonprincipal term.

The discarded high-$\tau$ full vector in (6) is negligible after projection on the nonprincipal component as well. Indeed on $a\ne0$ both the actual $q$-nonunit contribution and the principal unit character contribution are constant in $a$, while multiplicative orthogonality makes the nonprincipal contribution orthogonal to constants. Its projection is thus a contraction on the exact sampled numerator vector, with no estimate needed on a repeated numerator-zero value. Bound the two actual constant components using the untruncated product with $\Omega$ as follows.

On the genuine product support $k<X/2<q$, so $q\mid dk$ implies $q\mid d$; if $q\mid N$ this is impossible by the exact long unit. Otherwise there are $O(\lambda)$ possible $d=j q$. For each such $d$, the $h$ and $l^2/(l,d)$ conditions are coprime, because $h\mid N$ and $(l,N)=1$. Taking absolute values and counting required positive multiples gives

$$
 \ll K\sum_{h\mid\operatorname{rad}N}\frac1h
       \sum_{l\ {\rm sf}}\frac{(l,d)}{l^2}
 \ll K L_2^2.
$$

The last bound uses $\prod_{p\mid d}(1+1/p)\ll L_2$ uniformly for $d\le N$, not a polylogarithmic size bound on the number $j$. Thus the nonunit value at each $q,\beta$ is $O(X L_2^2)$, with shell energy $O_\epsilon(N L^{-1+\epsilon})$. The principal unit value is obtained from the ordinary additive value at numerator zero by subtracting these actual nonunits, and its contribution uses $\sum_q (q-1)^{-1}\ll1/L$ and the ordinary squared norm $O(N)$ from (5). Thus it too costs $O_\epsilon(N L^{-1+\epsilon})$. Neither term has been equated with the principal character added for the positivity upper bound in (9).

The original arcs are disjoint. Therefore all ordinary transfers in §1 apply to the shell by Parseval. The smoothing error and unit and squarefree truncation errors prove (1) for the actual hard $D$. Its full-circle squared norm and that of $P$ are $O(N)$, by the primal signed short-divisor estimate and the true prime boxes. Cauchy and contraction of separate numerator centering give the first two signed claims. The original [parity-preserving signed identity](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md) uses only the true odd support, actual product geometry, and these ordinary norms; apply it only after restoring the genuine $(dk,N)=1$ coefficient, with error $O(N/L+N(X/M)^2)$. This proves the signed residual claim on the single dyad, without a conclusion about the full polynomial divisor union.
