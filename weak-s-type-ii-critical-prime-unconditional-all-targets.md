# Unconditional critical-prime cancellation for every even target at fixed logarithmic width

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$. Keep the actual prime polynomial $P$ and complementary polynomial $D$ of the [joint determinant theorem](weak-s-type-ii-critical-prime-dual-determinant-logarithmic-width.md), with the true two prime boxes, bounded prime selector, unit tests and all hard cutoffs. Thus $J=[N-y,N/2)$, $N/2\le y\le9N/16$, and

$$
 D_m=\mathbf1_{m\in J}
     \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                     (m,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
   \qquad D(\alpha)=\sum_mD_m e(m\alpha),\quad e(z)=e^{2\pi iz}.
$$

Here $I_k$ includes the actual condition $k>t\ge N^{.49999}$, and $I_d$ is any hard interval in $[X,CXL^\gamma]$ for fixed $C>1,\gamma\ge0$. Write $\mathcal Q=[.8X,.9X]\cap\mathbb P$ and retain the literal shell energy

$$
 \mathcal E_N(D)=\int_{-1/(10N)}^{1/(10N)}
           \sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}|D(a/q+\beta)|^2\,d\beta .
$$

**Theorem.** Uniformly on every even target and all the original hard cutoffs,

$$
                         \mathcal E_N(D)=o_{C,\gamma}(N)
 \quad\text{as }N\to\infty .
 \tag{1}
$$

The original signed full shell, its separately centered numerator covariance and the exact parity-preserving signed even-lattice residual with averaging length $M=\lceil XL^2\rceil$ are each $o_{C,\gamma}(N)$, also uniformly in the permissible prime selector. This is unconditional and retains all original unit primes at every even target. In particular there is no radical restriction or exceptional family. The result does not assert an explicit rate for the little-oh, a bound on squares of individual compensated offsets, any polynomial widening or other shells, or Hypothesis S.

More precisely, for each fixed cutoff exponent $A\ge1$ and $\epsilon>0$, the proof gives

$$
 \mathcal E_N(D)
       \ll_{C,\gamma}N e^{-A/2}
           +O_{C,\gamma,A,\epsilon}(N L^{-1/2+\epsilon}),
 \tag{2}
$$

with the first constant independent of $A$. The two limits used for (1) are in order: first $N\to\infty$ with $A$ fixed, then $A\to\infty$.

## 1. The signed lcm form with the full unit mask

Put $V=\varphi(N)/N$, and let $I$ be any hard subinterval of $[X,CXL^\gamma]$. We first prove

$$
 \mathscr B(I,N):=\sum_{\substack{a,b\in I\\(ab,N)=1}}
                    \frac{\mu(a)\mu(b)}{[a,b]}
                 \ll_{C,\gamma}V^{-1}.
 \tag{3}
$$

The [Dress–Iwaniec–Tenenbaum prefix theorem, §2](https://tenenb.perso.math.cnrs.fr/PPP/Somme-Moebius.pdf#page=2) gives the same bound with constant $O(1)$ in the unmasked form for any interval of positive integers, by writing its coefficient as the difference of two prefix vectors in the positive form. The kernel identity $1/[a,b]=\sum_{j\mid a,b}\varphi(j)/(ab)$ is exact. Thus (3)'s left side is

$$
 \sum_{(j,N)=1}\frac{B(j)}j
      \left|\sum_{\substack{ju\in I\\(u,jN)=1}}\frac{\mu(u)}u\right|^2,
      \qquad B(j)=\frac{\mu^2(j)\varphi(j)}j .
 \tag{4}
$$

The elementary prime-factor estimates used here are uniform for $B_0\le N^2$: $\prod_{p\mid B_0}(1-1/p)^{-1}\ll L_2$, and for $\theta=1/L_2$, $\prod_{p\mid B_0}(1-p^{-1+\theta})^{-1}\ll L_2^{O(1)}$. Indeed for $p\le L^2$ one has $p^\theta\le e^2$, and there are $O(L)$ remaining prime factors; use the usual prime harmonic estimate on the small ones. At a fixed exponent $3/4$ the corresponding product is $\exp(o(L))$ by summing $p^{-3/4}$ even over the integers up to $L^2$. These same arguments show $V^{-1}\ll L_2$.

Take $Z=\exp(C_*L_2^2)$ with fixed $C_*$ sufficiently large, independent of $A$ in (2). The part $j<X/Z$ in (4) is $O(L^{-9})$. In fact the inner reciprocal sum, on any interval above $Z$ with prime mask $jN\le N^2$, is $O(L^{-5})$ (or any specified fixed log power by increasing $C_*$). The ordinary zero-free-region Mertens bound, for instance [Lee–Leong, §2.2, (23)](https://arxiv.org/html/2208.06141v5#S2.SS2), gives by partial summation an ordinary reciprocal interval bound $O(\exp(-c\sqrt{\log Y}))$ on every interval above $Y\ge2$, uniformly in its upper endpoint. To impose the mask, convolve $\mu$ with the indicator of integers $b_0$ supported on its primes, with weight $1/b_0$ in the reciprocal sum. For $b_0\le\sqrt Z$ the ordinary estimate applies above $\sqrt Z$ with total reciprocal weight $O(L_2)$; for $b_0>\sqrt Z$, the unsigned inner reciprocal interval is $O(L)$ and the $b_0$ tail is $\ll Z^{-1/(2L_2)}L_2^{O(1)}$ by Rankin. Summing $B(j)/j\le1/j$ over the small $j$ proves the bound.

For $j\ge X/Z$, convolve the inner $\mu$ in (4) just with the indicator of $N$-smooth integers, meaning integers all of whose prime factors divide $N$. Because the retained $j$ are $N$-units, each such convolution factor $b_0$ is coprime to $j$. Minkowski in the $j$ norm costs $\sum_{b_0}1/b_0=V^{-1}$. To prove (3) it therefore suffices to prove, for each scaled interval $I'=I/b_0$ with $b_0$ a positive integer, the comparator bound

$$
 \sum_{\substack{j\ge X/Z\\(j,N)=1}}\frac{B(j)}j
        \left|\sum_{\substack{ju\in I'\\(u,j)=1}}\frac{\mu(u)}u\right|^2
                  \ll_{C,\gamma} V .
 \tag{5}
$$

The sum is empty if $b_0>C ZL^\gamma$, and all inner $u,u'$ are at most $C ZL^\gamma=N^{o(1)}$ when nonempty.

Here is an exact comparison that preserves the signs in (5). At fixed $u,u'$ the $j$ interval $\mathcal I$ is the intersection of $[X/Z,\infty)$, $I'/u$ and $I'/u'$. It has polynomial-scale endpoints when nonempty and is bounded above by $CXL^\gamma$. For any of the masks $M_0$ in this step ($M_0=Nuu'$ or $uu'$), write $B(j)\mathbf1_{(j,M_0)=1}=1*g_{M_0}$. Away from the primes of $M_0$ the local coefficients are $g_{M_0}(p)=-1/p$, $g_{M_0}(p^2)=-(1-1/p)$ and zero at higher powers. At omitted primes they are $-1$ at $p$ and zero at higher powers. Consequently $\sum_d |g_{M_0}(d)|/d^{3/4}=N^{o(1)}$ (absolute convergence away from the mask, and the same prime-factor split just used, also for $M_0\le N^{1+o(1)}$). Counting multiples with the truncated convolution yields

$$
 \sum_{\substack{j\le x\\(j,M_0)=1}}B(j)
  =c(M_0)x+O(x^{3/4}N^{o(1)}),\qquad
 c(M_0)=c(1)\prod_{p\mid M_0}(1+a_p)^{-1},\quad a_p=\frac1p-\frac1{p^2}.
$$

The latter factors are the independent local ratios, since the unmasked local density is $(1-1/p)(1+(1-1/p)/p)$ and the masked density is $1-1/p$. By Abel, the true harmonic sum over $\mathcal I$ is therefore
$c(M_0)\int_\mathcal I dx/x+O(N^{-1/8+o(1)})$. This is uniform even for a point interval, and includes all strict endpoint choices.

We have the exact density relation

$$
 c(Nuu')= \frac{c(N)}{c(1)}c(uu')
                       \prod_{p\mid(N,uu')}(1+a_p),
      \qquad \frac{c(N)}{c(1)}\asymp V,
 \tag{6}
$$

the comparison with $V$ following from a convergent product of factors $1+O(p^{-2})$. For each $p\mid N$ expand its correction using
$\mathbf1_{p\mid uu'}=\mathbf1_{p\mid u}+\mathbf1_{p\mid u'}-\mathbf1_{p\mid u}\mathbf1_{p\mid u'}$.
Thus the correction imposes $r_1\mid u,r_2\mid u'$ with local allocations neither, first, second, or both, and with coefficients $1,a_p,a_p,-a_p$, respectively. For each term transfer the harmonic integral with density $c(uu')$ back to the same $j$ interval with mask just $(j,uu')=1$. The total transfer error, both directions together, is $O(N^{-1/8+o(1)})$: even the unsigned $u,u'$ count is $N^{o(1)}$ and the sum of absolute expansion coefficients is $\prod_{p\mid N}(1+3a_p)\ll L_2^3$. No cancellation of this error is required.

For a fixed allocation, the discrete comparator is a scalar product in the positive $B(j)/j$ norm over $j\ge X/Z$. The individual array with $r\mid u$ has norm $O(1/\varphi(r))$: for squarefree $r$, substitute $u=r v$, keep $(j,r)=1$ from the $(j,u)=1$ condition, write $\mu(u)=\mu(r)\mu(v)\mathbf1_{(v,r)=1}$, and use the $r$-smooth reciprocal convolution on the inner sum. The cost before the unmasked DIT interval bound is $r^{-1}\sum_{b\ r\text{-smooth}}1/b=1/\varphi(r)$. The outer restriction $j\ge X/Z$ and $(j,r)=1$ are contractions in this norm. Cauchy now bounds each cross term by $O(1/(\varphi(r_1)\varphi(r_2)))$. Summing all allocation coefficients times these bounds costs at most

$$
 O\!\left(\prod_{p\mid N}
         \left(1+a_p\left(\frac{2}{p-1}+\frac1{(p-1)^2}\right)\right)\right)=O(1),
$$

again by convergence of $\sum p^{-2}$. With (6) and $V^{-1}\ll L_2$ this proves (5). The convolution norm cost $V^{-1}$ and the square of (5)'s norm yield $O(V^{-1})$ in (4), establishing (3). In particular the extra factor $V^{-1}$ from a plain unaveraged coprime convolution is absent.

We will also use the simpler bound for an arbitrary mask $B_0\le N^2$ and any integer interval $I_0$,

$$
 \sum_{\substack{a,b\in I_0\\(ab,B_0)=1}}
             \frac{\mu(a)\mu(b)}{[a,b]}\ll L_2^2.
 \tag{7}
$$

This follows directly by the reciprocal convolution in the gcd-index norm, at cost $B_0/\varphi(B_0)$ in norm, then the unmasked DIT theorem. Unlike (3), this weaker assertion requires no proportional support.

## 2. Approximate the product unit condition in a global signed norm

Let $W(m)=\mathbf1_{(m,N)=1}$, $H=L^A$ with fixed $A\ge1$, and define the real divisor polynomial

$$
 W_H(m)=V\!\!\sum_{\substack{r\mid\operatorname{rad}N\\r\le H}}
       \mu(r)\prod_{p\mid r}\frac{\mathbf1_{p\mid m}-1/p}{1-1/p}
       =\!\sum_{\substack{h\mid\operatorname{rad}N\\h\le H}}
                          w_h\mathbf1_{h\mid m}.
 \tag{8}
$$

Expansion gives $w_h=\mu(h)Vh\sum_{r\mid\operatorname{rad}N,\ h\mid r,\ r\le H}1/\varphi(r)$, so $|w_h|\le1$ by extending that positive sum to all $r$ and taking the Euler product. In particular $|W_H|\le H$. On true units $W_H=c_H:=V\sum_{r\mid\operatorname{rad}N,\ r\le H}1/\varphi(r)\in[0,1]$. This gives the literal identity

$$
             (W-W_H)^2=(1-2c_H)W+W_H^2 .
 \tag{9}
$$

For the auxiliary period mean over residues modulo $\operatorname{rad}N$, the tests $\mathbf1_{p\mid m}$ are independent Bernoulli of mean $1/p$, by CRT. Their centered normalized products in (8) are orthogonal, with squared norms $1/\varphi(r)$. The complete product equals $W$. Consequently the exact mean of (9) is

$$
 \nu_H=V^2\sum_{\substack{r\mid\operatorname{rad}N\\r>H}}\frac1{\varphi(r)}
       \ll V e^{-A/2}.
 \tag{10}
$$

For the bound use Rankin at $\theta=1/L_2$. The normalized Euler product equals
$\prod_{p\mid N}(1+(p^\theta-1)/p)=O(1)$:
for $p\le L^2$, use $p^\theta-1\le e^2\theta\log p$ and $\sum_{p\le L^2}(\log p)/p\ll L$ with the sharper bound $O(\log(L^2))$ from Chebyshev and partial summation; for $p>L^2$, use the prime-factor count and $p^{-1+\theta}\le L^{-2+2\theta}$. Finally $H^{-\theta}\le e^{-A/2}$ for large $N$. In particular the implied constant in (10) is independent of $A$.

Put $U_*=CXL^\gamma$ and define the raw signed coefficient on the **entire** interval, with exact long unit,

$$
 F_{m,N}=\mathbf1_{m\in J}
              \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\(d,N)=1}}\mu(d).
$$

We claim the actual norm approximation

$$
 \sum_m (W(m)-W_H(m))^2 |F_{m,N}|^2
       \ll_{C,\gamma}N e^{-A/2}+O_{C,\gamma,A,B_*}(NL^{-B_*})
 \tag{11}
$$

for every fixed $B_*>0$. In the square of $F_{m,N}$ the two signed labels $a,b$ are $N$-units, so their lcm stride is coprime to $N$. For fixed $a,b$, the allowed $m$ in this expansion form the single hard interval $J\cap aI_k\cap bI_k$. The continuous model at this stride uses exactly the period mean $\nu_H$, because multiplication by $[a,b]$ permutes the residues modulo $\operatorname{rad}N$. Thus the full continuous contribution is

$$
 \nu_H\int_J \mathscr B\big(I_d\cap (x/I_k),N\big)\,dx ,
$$

where $x/I_k$ means the interval of positive $d$ with $x/d\in I_k$. By (3) and (10) this is $O_{C,\gamma}(Ne^{-A/2})$.

For the actual-to-continuous comparison, split at $g=(a,b)=G=\lfloor N^{1/100}\rfloor$. For $g>G$ use (9), exact inclusion over all squarefree $h\mid N$ for $W$, and the finite inclusion (8) for each of the two copies of $W_H$. In the resulting congruences the modulus is the product of $[a,b]$ and the corresponding forcing divisor of $N$. Each floor error is $O(1)$ times its coefficient and their sum over large $g$ is

$$
        O((2^{\omega(N)}+H^2)U_*^2/G)=N^{.99+o(1)} .
$$

Here $A$ is fixed; half-open or closed endpoints cost the same. The continuous constants of these exact congruences give precisely $\nu_H/[a,b]$ by CRT.

At $g\le G$ keep the sign instead. Write $a=gu,b=gv,m=guv z$ on the actual multiples, so $g,u,v$ are pairwise coprime and squarefree on the signed support and are all $N$-units. It follows that $W(m)=W(z)$ and $W_H(m)=W_H(z)$; the mask discrepancy is independent of $v$. Fix $g,u,z$. We have $u,v\in[X/g,U_*/g]$ and $1\le z\ll g$, since $m\ll N$ and $[a,b]\ge X^2/g$. The free $v$ is restricted by $gv\in I_d,vz\in I_k,guvz\in J$, and by $(v,guN)=1$, with the $uz\in I_k$ gate already fixed. These are one hard interval and a coprimality mask. The uniform masked ordinary Mertens estimate of the [reciprocal-unit theorem, §1](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md#1-the-true-global-omitted-unit-cost) applies: all nonempty endpoints are $\gg X/G$ and $(guN)\ll N^2$. It gives $O((U_*/g)e^{-c\Phi})$ for the signed free interval, with $\Phi=L^{3/5}(\log L)^{-1/5}$, even if the interval is very short (subtract the two hard prefixes). Multiplying by $(1+H)^2$ and summing $(g,u,z)$ gives $O((1+H)^2 U_*^2(1+\log G)e^{-c\Phi})$, negligible to every fixed log power. The signed continuous $g\le G$ term is also negligible: fix $x,g,u$ and use the harmonic masked Mertens bound on the analogous $v$ interval with denominator $guv$; $\nu_H\le1$, and the remaining harmonic sums are bounded by fixed powers of $L$. Replace the continuous small-$g$ part by the actual one. This proves (11), including the independence of the leading constant from $A$.

Estimate (11) continues to hold with a bounded-BV short-label weight on its original interval and a bounded physical weight, with the squared cost multiplied at most by the square of the total-variation and supremum bounds. This follows from Minkowski in the ordinary norm weighted by $|W-W_H|^2$, using the summation-by-parts representation of the short-label test as a signed combination of hard prefixes, and by contraction for the physical weight. In particular (11) is a full-interval transfer, not a per-dyad error.

## 3. Preserve the exact cuts through smoothing and squarefree truncation

First smooth the true squarefree **full-unit** coefficient. Put $\delta=L^{-1/2}$. The physical cutoff is smoothed by one function $\Omega(m/N)$ supported inside the original interval. For the cofactor cutoff choose a single weight in $\log k$, smoothed by an inner mollification at scale $O(\delta)$, valued in $[0,1]$, of bounded variation at most two and supported inside the true hard cofactor interval. Before forming it, intersect the interval with $[X/(10CL^\gamma), X/2]$, which does not remove any actual terms. If a log interval is shorter than twice the chosen smoothing width the zero test suffices. Both mollifications may be taken with derivative bounds of order $r$ given by $O_r(\delta^{-r})$ in their normalized coordinate and localized to their endpoint layers.

On a half-open dyad $A_0=\lambda X\le d<2A_0$, $K=X/\lambda$, the actual product support has $7/32\le k/K<1/2$. The global cofactor weight pulled back by $k=Kz$ has the same uniform derivative bounds on this range, with layers of width $O(\delta)$ in $z$. Multiply its pullback by a fixed smooth bump supported in a fixed compact subinterval of $(0,\infty)$ and equal to one on $[7/32,1/2]$ for purposes of completion. This does not change a single coefficient since the physical weight is supported in $J$. The derivative outside the thin layers now costs only fixed constants. The [actual endpoint estimates for logarithmically wide dyads](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md#2-uniform-exact-transfers-on-one-divisor-dyad) apply with the exact genuine units, with ordinary squared error $O_{C,\gamma}(N\delta L_2+N^{3/4})$ per dyad, and $O_{C,\gamma,\epsilon}(NL^{-1/2+\epsilon})$ over all $O_{C,\gamma}(L_2)$ dyads by Minkowski. The same global cofactor smoothing weight was used on all dyads before inserting the harmless proportional bump.

The smoothed true coefficient is $\mu^2(m)W(m)F_{m,N}^{\rm sm}$, with the exact $(d,N)=1$ kept internally. Replace it by $\mu^2(m)W_H(m)F_{m,N}^{\rm sm}$. By (11) and its BV extension this is a single full-interval squared error $\ll_{C,\gamma}Ne^{-A/2}+O_{C,\gamma,A,B_*}(NL^{-B_*})$; there is no dyadic factor on its first term. The equality with the true original squarefree coefficient before this approximation uses exactly that $\mu(d)$ has squarefree support and that, on squarefree $m$, $d,k$ are automatically coprime.

Next on each dyad truncate only the squarefree identity at $T=L^\eta$, for example with $\eta=8A+10$. The approximate coefficient on that dyad is

$$
            \widetilde D_m
         =W_H(m)F_{m,N}^{\rm sm}
                         \sum_{\substack{l\le T\\l^2\mid m}}\mu(l).
 \tag{12}
$$

One must allow $l$ sharing primes with $N$ after the unit approximation. For squarefree $\ell$ the necessary signed forced-square estimate, now with the exact internal long mask, is

$$
 \sum_{\ell^2\mid m}|F_{m,N}^{\rm sm}|^2
   \ll_{C,\gamma} C_1^{\omega(\ell)}\frac N{\ell^2}
                         \big(L_2^2+1+\log(2\lambda\ell)\big).
 \tag{13}
$$

Indeed the forced-square proof on one logarithmically wide dyad just cited applies with this change: after stripping the parts of the two signed labels dividing $\ell$, the continuous kernel is $\ell^{-2}$ times the lcm kernel on at most $2^{\omega(\ell)}$ interval vectors carrying mask $N\ell$. Use (7) and Minkowski. The signed divisors remain squarefree, and the stripped parts are necessarily $N$-units. Only $\ell\le\sqrt{N/2}$ need be considered. In the large-gcd floor error use $G=\lceil\lambda^2\ell^2\rceil$ as before. In the remaining absolute corrections, dropping the added $N$ mask only enlarges counts: write $m=guv z$, $u,v\asymp A_0/g$, $z\asymp g/\lambda^2$; for each prime $p\mid\ell$ allocate it to none or exactly one of $g,u,v$ and use the required complementary power of $p$ on $z$. Each allocation has divisibility moduli product $\ell^2$ and integer positive multiples are bounded by upper length divided by modulus, with no additive $1$. The reciprocal continuous correction obeys the same bound, summing harmonically in $g$; this is the $\log(2\lambda\ell)$ term. BV and the physical weight are handled as in (11).

Group the two discarded square labels by their squarefree lcm $\ell>T$, with at most $3^{\omega(\ell)}$ choices, and use $|W_H|\le H$ pointwise. The squared error of (12) is at most $O_{C,\gamma,A,\eta,\rho}(N H^2 T^{-1+\rho} L_2^2)$ for fixed $\rho>0$, by (13) and the elementary divisor growth bound on fixed powers of $C_1^{\omega(\ell)}$. With $\rho=1/4$ and the chosen $\eta$ this is $O(NL^{-2})$, harmless even after summing dyads. In particular (12) on each dyad has ordinary squared norm $O_{C,\gamma,A}(N)$, by the true ordinary energy bound and the preceding transfers (the argument of (11) also holds for that dyad by intersecting the hard long interval).

## 4. Joint determinant completion with fixed logarithmic cutoffs only

We give the required modification of the [all-unit joint $h,h'$ determinant calculation](weak-s-type-ii-critical-prime-full-unit-dual-determinant-grh.md). No use is made of its conditional Möbius estimate. Fix squarefree $l\le T$, and $s=(l,d)\mid l$ with $(s,N)=1$. Write $d=su$, $(u,lN)=1$. The cutoff $l^2\mid dk$ requires $l^2/s\mid k$. For an original summand $h$ of (8), the exact long unit gives $h\mid m$ iff $h\mid k$. Let $h'=h/(h,l)$. Since $h$ is squarefree, the two conditions are equivalent to $k=(l^2/s)h'v$. For fixed $l,s$ group terms with the same $h'$ and write their total coefficient as $c_{l,h'}$; there are at most $\tau_{\rm d}(l)$ original $h$ in the group, hence $|c_{l,h'}|\le\tau_{\rm d}(l)$, where $\tau_{\rm d}$ is the divisor-counting function. All these coefficients are independent of $q,\beta,u$. We have $h'\mid\operatorname{rad}N$, $(h',l)=1$, and $h'\le H$. Signs $\mu(l)\mu(s)$ can be kept as common factors. This collapse also handles $p\mid(l,N)$; imposing $(l,N)=1$ would instead change the actual approximation.

Normalize as in the [unconditional dual determinant proof, §2](weak-s-type-ii-critical-prime-dual-determinant-logarithmic-width.md#2-dual-cutoff-and-true-square-expansion), using physical test $G_\beta(z)=\Omega(e^z)e(\beta N e^z)$ and short test $f_\tau(z)=w_\lambda(z)e(\tau\log z)$ with the proportional bump just specified. With $U=A_0/s$, $x_q=Ks/(q l^2)$ and $x_0=Ks/(Xl^2)$, the long array is

$$
 a_u=\mu(u)\mathbf1_{su\in I_d\cap[A_0,2A_0)}
             \mathbf1_{(u,lN)=1}e(\tau\log(su/A_0)),
       \qquad A_\tau(\theta)=\sum_u a_u e(u\theta).
$$

For a nonprincipal character $\chi\bmod q$, the exact normalized Gauss-poisson expression for the sum of all grouped $h'$ is, apart from the common multiplier $\mu(l)\mu(s)\chi(l^2)$,

$$
 \tau_q(\chi)\!\left(\sum_u a_u\chi(u)\right)
       \sum_{\substack{h'\mid\operatorname{rad}N\\h'\le H}}
          c_{l,h'}\,\frac{x_q}{h'}\chi(h')
                 \sum_{j\ne0}\overline{\chi(j)}\,
                                      \widehat f_\tau(jx_q/h'),
     \qquad |\tau_q(\chi)|=\sqrt q .
 \tag{14}
$$

Here Fourier transform uses $e(-z\xi)$ and the Mellin frequency $\tau$ is integrated against $\widehat G_\beta(\tau)$. The supports, the compactness bounds, and the actual $\beta$ range are unchanged. The formula is Poisson on the actual short variable with scale $Ks/(l^2h')$, with ordinary extension by zero outside its positive support.

All Fourier cutoffs may now be chosen as fixed powers of $L$, with exponents depending on $A,\eta,\gamma$. Specifically take $|\tau|\le L^{D_\tau}$ with $D_\tau>2$ and $0<|j|\le L^{D_j}$ with $D_j>A+\gamma+2\eta+D_\tau+2$. The mesh $x_q/h'$ is at least $\gg_C L^{-A-\gamma-2\eta}$. For the high $\tau$ tail, the uniform sampled periodization norm estimate in the [composite-square completion](weak-s-type-ii-critical-prime-composite-square-and-unit-tail.md#3-smooth-completion-at-the-literal-rational-points) bounds the short factor, after removing $\sqrt q$, by $O(\delta^{-1/4}+\sqrt{1+|\tau|})$. The elementary long residue norm (occupancy $O_C(\lambda)$) then bounds the full $q,\chi$ norm in any term by $N$ times fixed powers of $L$ times $1+\sqrt{|\tau|}$. The tuple count and coefficients $c_{l,h'}$ also cost at most fixed powers of $L$. Because $|\widehat G_\beta|\ll_r\delta^{1-r}|\tau|^{-r}$, arbitrary fixed integration-by-parts order pays for this tail. On retained $\tau$ the dual tail estimate

$$
 (x_q/h')\sum_{|j|>J_d}|\widehat f_\tau(jx_q/h')|
 \ll_r (1+\delta^{-1}+|\tau|)^r((x_q/h')J_d)^{1-r},
 \qquad J_d=L^{D_j},
$$

similarly gives any fixed inverse log by increasing $r$. All retained $j,h',l$ are nonzero modulo shell primes.

Remove the Gauss modulus in the square of (14), add the principal character algebraically by positivity, and add the square of the zero residue class. This is an inequality as in the joint determinant theorem, with the actual principal and nonunit components still to be restored. The exact signed square is grouped by $h'u/j\bmod q$; the determinant for two terms with labels $h_1,h_2$ is $h_1 j' u-h_2 j u'$. For determinant zero put $g=(h_1,h_2)$; $(u u',N)=1$ implies $h_1/g\mid j,h_2/g\mid j'$. After dividing the dual labels by these factors the two Fourier meshes become $x_q/g$, and the exact reduced equality is $i' u=i u'$ for positive $u,u'$. The divisor-weight envelope estimate of the [fixed log-width diagonal, §3](weak-s-type-ii-critical-prime-dual-determinant-logarithmic-width.md#3-nonzero-determinants-and-the-weighted-zero-determinant) thus gives, with $Y_\tau=1+\delta^{-1/2}+|\tau|$,

$$
 \ll_{C,\gamma,A} \frac{N^2Y_\tau L_2}{L\,l^2}\,\tau_{\rm d}(l)^2
                     \sum_{h_1,h_2\mid\operatorname{rad}N}\frac1{[h_1,h_2]}
 \ll_{C,\gamma,A} \frac{N^2Y_\tau L_2^4}{L\,l^2}\,\tau_{\rm d}(l)^2 .
 \tag{15}
$$

For clarity, the upper envelope at the new mesh is
$\min(1,(gY_\tau/(x_0|i|))^2)$ up to a constant. The number of positive solutions to $i'u=iu'$ has bound $2U\gcd(|i|,|i'|)/\max(|i|,|i'|)$ with no additive $1$. Summing against the two envelopes costs $O(U(gY_\tau/x_0)\log(2+gY_\tau/x_0))$. Multiply by $x_q^2/(h_1h_2)$, use $U x_0=X/l^2$, and sum $q(q-1)$ over the shell. The logarithm is $O_{C,\gamma,A}(L_2)$. The Euler sum is $\prod_{p\mid N}(1+3/p)\ll L_2^3$. The weights $c_{l,h_i}$ give only the stated $\tau_{\rm d}(l)^2$. This recovers the exact joint diagonal without any square-root moment of all the divisors of $N$.

For nonzero determinant equal to $bq$, $b\ne0$, fix $h_1,h_2,j,j',b$. The sum over $q$ is the Fourier integral of

$$
 A_\tau(h_1j'\theta)\overline{A_\tau(h_2j\theta)}
                    \sum_q \omega_q e(-bq\theta).
$$

Here $\omega_q$ is the exact Poisson weight with the indicated fixed labels, bounded by $X^2$ times fixed powers of $L$. Nonzero distinct frequencies $bq$ give the last factor norm $O(X^2\sqrt{\#\mathcal Q})$ times the same powers of $L$, and one long factor has norm $O(\sqrt U)$ by Plancherel for its nonzero integer dilation. For the other use the unconditional [Davenport bound](https://academic.oup.com/qjmath/article-abstract/os-8/1/313/1564796), stated explicitly in [He–Huang (1.2), PDF p. 1](https://www.impan.pl/shop/en/publication/transaction/download/product/91740?download.pdf=), to get $|A_\tau(\theta)|\ll_{C,\gamma,A,D_\tau,B_*} U L^{-B_*}$ for each fixed $B_*>0$. In detail, convolve with the indicator of $(lN)$-smooth integers, treat convolution label $r\le\sqrt U$ by Davenport at its two rescaled hard endpoints, and use reciprocal Rankin at $1/4$ for $r>\sqrt U$. The Euler cost on the first part is $O(L_2)$ and on the tail is $\exp(o(L))$, since $lN\le N^2$. Abel on the actual log twist costs $O(1+|\tau|)$, which remains a fixed power of $L$. There are only fixed powers of $L$ possible tuples; in particular $|b|\ll_C L^\gamma H J_d$. Hence their combined signed nonzero-determinant contribution is $O(N^2L^{-B_*})$ for every fixed $B_*$. It is here that retaining a fixed-logarithmic, rather than superlogarithmic, short mask matters; no uniform bound as $A\to\infty$ is needed.

Take square roots in (15), then Minkowski across the common product frequency and over $(l,s)$. The integral $\int |\widehat G_\beta(\tau)|\sqrt{Y_\tau}\,d\tau\ll\delta^{-1/2}$ is the same as before, from the minimum of $1,|\tau|^{-1},\delta^{-1}|\tau|^{-2}$. The norm tuple cost is now $\sum_{l\le T,\ l\ {\rm sf}}\tau_{\rm d}(l)^2/l\ll (1+\log T)^4$, by the four-fold divisor convolution. Integrate over the actual $\beta$ interval of length $1/(5N)$. The nonprincipal energy on one dyad is $O_{C,\gamma,A,\epsilon}(NL^{-1/2+\epsilon})$, since $\delta=L^{-1/2}$.

For the exact additive expansion at nonzero numerators, the squared nonprincipal norm changes by at most the factor $q/(q-1)$. In the actual nonunit part $q\mid d$, since $k<X/2<q$. This is impossible if $q\mid N$ due to the unchanged $d$ unit test. Otherwise $d=j q$ with $j=O_C(\lambda)$; bound absolutely the truncated squarefree and collapsed inclusion coefficient at each such $d$ by counting their genuinely required common multiples on $k$:

$$
 O\!\left(K
       \sum_{h'\mid\operatorname{rad}N}\frac1{h'}
       \sum_{l\ {\rm sf}}\frac{\tau_{\rm d}(l)(l,d)}{l^2}\right)
     \ll_{C,\gamma,\epsilon} K L^\epsilon .
$$

Here $(h',l)=1$ in the true terms, the $h'$ sum is $O(L_2)$, and the $l$ sum is at most a fixed constant times $\prod_{p\mid d}(1+2/p)$, which is $O_{C,\gamma,\epsilon}(L^\epsilon)$ for $d=j q$. Thus the actual nonunit value is $O(XL^\epsilon)$, giving squared energy $O(NL^{-1+\epsilon})$. The principal unit character term is bounded as usual by its actual numerator-zero value (subtracting the nonunit value from the ordinary full polynomial), (12)'s ordinary $O(N)$ squared norm, and $\sum_q(q-1)^{-1}\ll1/L$. This, too, costs $O(NL^{-1+\epsilon})$, and is not the character added in (14)'s square.

Finally the arcs are disjoint, so the ordinary coefficient transfers apply by Parseval. Sum the ordinary dyad smoothing and squarefree errors and the completed arc norms by Minkowski, absorbing $L_2$ powers. Insert the global undivided transfer (11) only once, with its constant independent of $A$. This proves (2) and the ordered-limit conclusion (1). The true $P,D$ have ordinary squared norm $O(N)$ as in the unconditional joint determinant theorem; Cauchy and contraction under separate centering give the first two signed consequences. The [parity-preserving residual identity](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md) uses only the actual odd supports, physical bounds and these ordinary norms. Apply it to the genuine coefficients **after** all transfers, with its original error $O(N/L+N(X/M)^2)$. The auxiliary (12) need not have odd support, and no parity identity has been applied to it.
