# All original unit primes in the logarithmically wide critical shell under global GRH

Use the exact actual prime carrier $P$ and complementary coefficient $D$ of the [unconditional dual-determinant theorem](weak-s-type-ii-critical-prime-dual-determinant-logarithmic-width.md). Thus $N$ is even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, $J=[N-y,N/2)$ with $N/2\le y\le9N/16$, and the genuine coefficient is

$$
 D_m=\mathbf1_{m\in J}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                         (m,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k).
$$

The original hard $I_k$ includes $k>t\ge N^{.49999}$, $I_d\subset[X,CXL^\gamma]$ is any hard interval, and $C>1,\gamma\ge0$ are arbitrary fixed. Keep the genuine two disjoint prime boxes, hard prime cutoffs, actual prime unit test and allowed bounded prime selector on $P$. Denote the shell by $\mathcal Q=[.8X,.9X]\cap\mathbb P$, nonzero numerators $1\le a<q$, and $|\beta|\le1/(10N)$.

**Theorem (global Dirichlet GRH).** Assume the generalized Riemann hypothesis for all primitive Dirichlet $L$-functions, including $\zeta(s)$. Then for every $\varepsilon>0$, at **every** even target $N$ and uniformly in the original cutoffs,

$$
 \mathcal E_N(D)=\int_{-1/(10N)}^{1/(10N)}
        \sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}|D(a/q+\beta)|^2\,d\beta
       \ll_{C,\gamma,\varepsilon}N L^{-1/2+\varepsilon}.
 \tag{1}
$$

Consequently the full signed shell, its separately centered numerator covariance, and the exact parity-preserving signed even-lattice residual with $M=\lceil XL^2\rceil$ are $O_{C,\gamma,\varepsilon}(NL^{-1/4+\varepsilon})$. There is no size or factor-count condition on $\operatorname{rad}N$, no term for omitted unit primes, and no exceptional family. The only use of GRH is a uniform power saving for additive Möbius sums (a fixed positive power saving suffices). This result concerns the same critical prime shell, not polynomial divisor widening, other shells, or Hypothesis S.

## 1. Keep exact long units and cut only the auxiliary short inclusion

Work on one actual half-open divisor dyad with $A_0=\lambda X\le d<2A_0$, $1\le\lambda\ll_C L^\gamma$, $K=X/\lambda$, and intersect it with $I_d$. On the physical gate $k\asymp K$ and $k<X/2$. Define $\delta=L^{-B}$ and $T=L^\eta$, with fixed $B,\eta>0$. Apply the genuine endpoint transfers of [R86 §2 and the start of §3](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md#2-uniform-exact-transfers-on-one-divisor-dyad) **while the complete original unit mask is present**. They smooth only the physical and short cofactor gates, at relative width $O(\delta)$ with weights $0\le W(m/N),w(k/K)\le1$ supported inside those gates, then insert the squarefree cutoff $S_T(m)=\sum_{l\le T,l^2\mid m}\mu(l)$. Those transfers apply to any fixed $\gamma$: their forced square and smoothing estimates are independent of the older completion restriction. They give ordinary squared cost

$$
 O_{C,\gamma,\rho,B,\eta}(N\delta L_2+N^{3/4}+NT^{-1+\rho}L_2)
 \tag{2}
$$

for every fixed $\rho>0$. Their proofs keep the full unit mask as a contraction in the genuine squarefree norm or in the signed square tail. No long endpoint is moved.

For the smoothed coefficient impose the exact long mask $(d,N)=1$ inside the signed dyad sum; denote this raw, not necessarily squarefree, auxiliary by $F_{m,N}^{\rm sm}$. The approximant from (2) is exactly $\mathbf1_{(m,N)=1}S_{T,N}(m)F_{m,N}^{\rm sm}$, where
$S_{T,N}(m)=\sum_{l\le T,l^2\mid m,(l,N)=1}\mu(l)$: on a true unit, the inserted conditions are automatic. We now approximate this by

$$
 D_m^\dagger=S_{T,N}(m) F_{m,N}^{\rm sm}
   \sum_{\substack{h\mid(m,N)\\h\mid\operatorname{rad}N,\ h\le H}}\mu(h),
 \qquad H=\exp(C_0 L_2^2).
 \tag{3}
$$

Here $C_0$ is a sufficiently large fixed constant. On the exact long unit support $h\mid(m,N)$ is equivalent to $h\mid(k,N)$, so the new inclusion acts only on the short variable when splitting the coefficient. Its ordinary norm error is estimated next; (3) is not asserted equal to the genuine unit coefficient.

For any squarefree $r\mid N$ we have the forced first-divisibility estimate

$$
 \sum_{r\mid m}|F_{m,N}^{\rm sm}|^2
   \ll_{C,\gamma}\frac Nr\left(L_2^2+1+\log(2\lambda r)\right).
 \tag{4}
$$

To prove it first take hard $m,k$ intervals with the exact long and unit gates. In the square expansion, two signed divisors $a,b$ are units, so $[a,b,r]=r[a,b]$ exactly. At each real physical value, the continuous signed main is $1/r$ times the lcm form of the exact signed interval on $(a,N)=1$. The unmasked lcm norm squared of an arbitrary signed interval $\mu(a)\mathbf1_{a\in I}$ is bounded by the usual [Dress–Iwaniec–Tenenbaum interval bound in the original endpoint argument](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy). We need its masked version for the possibly large radical:

$$
 \sum_{a,b\in I:(ab,N)=1}\frac{\mu(a)\mu(b)}{[a,b]}
       \ll (N/\varphi(N))^2 .
 \tag{5}
$$

Indeed by the totient identity for the gcd the left side is the squared norm, with positive weights $\varphi(j)/j^2$, of the array

$$
 \mathbf1_{(j,N)=1}\mu(j)
     \sum_{\substack{j u\in I\\(u,jN)=1}}\frac{\mu(u)}u .
$$

Inside its reciprocal sum convolve $\mu$ with the indicator of integers $b_0$ supported on the primes of $N$. Because $(b_0,j)=1$ for the retained $j$, the inner term at $b_0$ is $1/b_0$ times the unmasked norm array for $I/b_0$ restricted to those same $j$. Minkowski and the unmasked bound give norm $O(\sum_{b_0}1/b_0)=O(N/\varphi(N))$, proving (5). In particular the cost is a reciprocal, not the inverse square root of the inclusion divisor. The elementary bound $N/\varphi(N)\ll L_2$ follows from Mertens' product for primes up to $L^2$ and the trivial number of remaining prime factors.

At $g=(a,b)>G=\lceil\lambda^2 r\rceil$ the floor error is $O(A_0^2/G)=O(N/r)$. At smaller $g$, write $a=gu,b=gv,m=guv z$ at the actual multiples. Thus $u,v\asymp A_0/g$, $z\ll g/\lambda^2$ and $r\mid z$ because $(guv,N)=1$. Counting multiples by their positive upper bound divided by their modulus (even when there are none) gives $O(N/(gr))$ choices at each $g$. The continuous small-gcd correction has the same bound by its denominator $rguv$ and proportional harmonic sums on $u,v$. Summing over $g\le G$, subtracting that continuous part from the full signed main bounded by (5), and inserting the actual part proves (4) for hard gates. Smoothing preserves it by bounded-BV summation by parts in $k$ and contraction by the product weight. This proof does not require that $r$ be a small or retained divisor.

To bound the error in (3), use $|S_{T,N}|\le T$. Expanding the absolute square of the discarded unit inclusion, group the two squarefree divisors by their lcm $r>H$, with at most $3^{\omega(r)}$ choices. By (4) the ordinary squared discrepancy is at most

$$
 O_{C,\gamma}\!\left(NT^2 L
              \sum_{\substack{r\mid\operatorname{rad}N\\r>H}}
                     \frac{3^{\omega(r)}}r\right).
$$

Use Rankin at $1/L_2$ on this last sum. Its upper bound is

$$
 e^{-C_0L_2}\prod_{p\mid N}(1+3p^{-1+1/L_2})
                  \ll e^{-C_0L_2}L_2^{O(1)}.
$$

For the Euler bound, $p^{1/L_2}\le e^2$ on $p\le L^2$, and for $p\mid N$ beyond $L^2$, at most $O(L)$ primes each contribute $O(L^{-2+2/L_2})$. This makes the squared discrepancy $O(NL^{-A})$ for any fixed desired $A$ by choosing $C_0$ in terms of $A,\eta$. In particular $\|D^\dagger\|_2^2=O_{C,\gamma,\eta}(N)$ by the ordinary bound and (2).

## 2. Joint Poisson norm with every allowed inclusion label

Use the exact normalized product Fourier inversion and notation of the [dual-determinant completion, §2](weak-s-type-ii-critical-prime-dual-determinant-logarithmic-width.md#2-dual-cutoff-and-true-square-expansion), with $G_\beta(z)=W(e^z)e(\beta N e^z)$. For each squarefree $l\le T$ with $(l,N)=1$ and $s\mid l$, write $d=su,\ k=l^2hv/s$ where $s=(l,d)$. The true common long array does not vary with $h$:

$$
 a_u=\mu(u)\mathbf1_{su\in I_d\cap[A_0,2A_0)}
        \mathbf1_{(u,lN)=1} e(\tau\log(su/A_0)),
 \qquad U=A_0/s,\quad x_q=Ks/(q l^2),\quad x_0=Ks/(X l^2).
$$

Put $f_\tau(z)=w(z)e(\tau\log z)$. The conditions on $u$ are exact, since $s=(l,d)$ and $d$ has squarefree sign support. For nonprincipal $\chi\bmod q$ its transformed $(l,s)$ block, up to the common unit multiplier $\mu(l)\mu(s)\chi(l^2)$, is

$$
 \tau_q(\chi)\,U_\chi\,
    \sum_{\substack{h\mid\operatorname{rad}N\\h\le H}}
        \frac{\mu(h)x_q\chi(h)}h
           \sum_{j\ne0}\overline{\chi(j)}
                         \widehat f_\tau(jx_q/h),\qquad
 U_\chi=\sum_u a_u\chi(u),
 \tag{6}
$$

with $|\tau_q(\chi)|=\sqrt q$. The scale of the original cofactor is $Ks/(l^2h)$. Inclusion coefficients are thus inside the norm, not estimated separately by their number.

The analytic truncations can be taken at $|\tau|\le\exp(C_\tau L_2^2)$ and $0<|j|\le\exp(C_j L_2^2)$ with fixed $C_\tau>0$ and $C_j>C_0+C_\tau+2$. To see this, the predecessor's elementary periodization/long residue bound gives the $\ell^2(q,\chi\ne\chi_0)$ norm per $h$ at most $O(N L^{O_{\gamma,B}(1)}(1+\sqrt{|\tau|}))$. Sum this bound trivially over at most $H$ possible terms; by
$|\widehat G_\beta(\tau)|\ll_r\delta^{1-r}|\tau|^{-r}$
with sufficiently large fixed $r$, its integrated high-$\tau$ norm is $O(NL^{-A})$ for every fixed $A$. On retained $\tau$, put $J_d=\exp(C_j L_2^2)$ and mesh $x=x_q/h$. Integration by parts gives

$$
 x\sum_{|j|>J_d}|\widehat f_\tau(jx)|
   \ll_r(1+\delta^{-1}+|\tau|)^r(xJ_d)^{1-r}.
$$

Uniformly $x_q/h\gg_C L^{-\gamma-2\eta}/H$. Thus fixed large $r$ absorbs the number $H$ and all remaining fixed logarithmic factors. These choices are identical for each $q,\beta$ and block; all retained $h,j,l$ are nonzero modulo every shell prime for large $N$. The use of an exponential-in-$L_2^2$ logarithmic Fourier cutoff as well as the dual cutoff ensures that the discarded tails need not absorb $H$ with an arbitrarily fixed inverse log power alone.

After removing the Gauss magnitude in the square, add the principal character algebraically and add the square of the zero residue class, just as in the predecessor. Then multiplicative orthogonality groups (6) by the common residue $hu/j\bmod q$. For fixed $h,h',j,j',q$ the resulting weight in front of the $u,u'$ sum is

$$
 \frac{q(q-1)x_q^2\mu(h)\mu(h')}{hh'}\,
      \widehat f_\tau(jx_q/h)\overline{\widehat f_\tau(j'x_q/h')},
$$

and its exact equation is

$$
                h j'u-h' j u'\equiv0\bmod q.
 \tag{7}
$$

As in the predecessor, the added principal and zero class only give a positive upper bound; neither replaces its actual additive counterpart.

## 3. Use the original units on the determinant diagonal

For zero determinant, put $g=(h,h')$. From (7) as an equality and $(u u',N)=1$ we have $h/g\mid j$ and $h'/g\mid j'$. Write $j=(h/g)i,\ j'=(h'/g)i'$. The meshes in both Fourier factors are now $x_q/g$, and the equality is $i'u=i u'$. For $i,i'$ of the same sign the number of positive solutions in the actual $u$ range is at most
$2U\,\gcd(|i|,|i'|)/\max(|i|,|i'|)$; opposite signs give none. As in the [weighted zero determinant estimate](weak-s-type-ii-critical-prime-dual-determinant-logarithmic-width.md#3-nonzero-determinants-and-the-weighted-zero-determinant), the two Fourier envelopes at mesh $x_0/g$ give an absolute double sum against this gcd kernel bounded by

$$
 O\!\left(U\,(gY_\tau/x_0)\log(2+gY_\tau/x_0)\right),
 \qquad Y_\tau=1+\delta^{-1/2}+|\tau|.
$$

This uses the first two localized derivatives and the elementary divisor sum on positive $i,i'$; the dual cutoffs can be enlarged for this positive estimate. On retained $\tau$ the logarithm is $O_{C_0,C_\tau,\gamma,\eta,B}(L_2^2)$. Multiplying by $x_q^2/(hh')$, use the exact balance $U x_0=X/l^2$ and $g/(hh')=1/[h,h']$. The total squared diagonal at fixed $l,s,\tau$ is therefore at most

$$
 O\!\left(\frac{N^2Y_\tau L_2^2}{L\,l^2}
                      \sum_{h,h'\mid\operatorname{rad}N}\frac1{[h,h']}\right)
          \ll \frac{N^2Y_\tau L_2^5}{L\,l^2}.
 \tag{8}
$$

Here $\sum_q q(q-1)\ll X^3/L$, and the positive sum of lcm reciprocals equals $\prod_{p\mid N}(1+3/p)\ll L_2^3$ by Mertens and the same tail split. Both original long unit masks were required for the congruence scaling on this diagonal.

For nonzero determinant write the exact equality $h j'u-h'j u'=bq$ with $b\ne0$. The weights have modulus $O(X^2)$. For each fixed $h,h',j,j',b$, the sum over $q$ is the same Fourier integral as before with frequencies $h j'\theta,h'j\theta,-bq\theta$. The finite number of tuples is $\exp(O_{C_0,C_j,\gamma}(L_2^2))=N^{o(1)}$: $|b|\ll_C L^\gamma H J_d$, and each of the other four labels is at most $H$ or $J_d$. The last polynomial in $q$ has norm $O(X^2\sqrt{\#\mathcal Q})$ by distinct nonzero frequencies. One long factor has norm $O(\sqrt U)$ by Plancherel. For the other long factor use [Baker–Harman (1991)](https://academic.oup.com/jlms/article-abstract/s2-43/2/193/862020), whose global GRH bound for the uniform Möbius additive sum is $O_\epsilon(z^{3/4+\epsilon})$ (see its explicit statement in [He–Huang, equation (1.4), PDF p. 1](https://www.impan.pl/shop/en/publication/transaction/download/product/91740?download.pdf=)). This also gives $\sup_\theta|\sum_u a_u e(u\theta)|\ll U^{4/5}$ for large $N$ with our complete mask. Indeed convolve with the indicator of $(lN)$-smooth integers. The Euler cost at exponent $3/4$ is $\prod_{p\mid lN}(1-p^{-3/4})^{-1}=N^{o(1)}$, by splitting primes at $L^2$ and estimating their sum over all smaller integers. Hard intervals and the Abel cost $1+|\tau|$ do not destroy the power saving because $U\gg X/L^\eta$ and $|\tau|=N^{o(1)}$. The bound for any individual tuple is then $O(U^{4/5}\sqrt U\,X^2\sqrt{\#\mathcal Q})$, and their sum is $O(N^{2-\sigma})$ for some fixed $\sigma>0$. This is the only conditional step; Davenport's arbitrary fixed inverse log powers alone do not pay the number of superpolylogarithmic dual labels in this implementation.

## 4. Restore the actual finite expansion and hard coefficients

Take square roots in (8) and integrate in $\tau$ by Minkowski. The same estimate as in R87,
$\int|\widehat G_\beta(\tau)|\sqrt{Y_\tau}\,d\tau\ll\delta^{-1/2}$,
uses the minimum of $1,|\tau|^{-1},\delta^{-1}|\tau|^{-2}$. The $l,s$ tuples cost $\sum_{l\le T}\tau_{\rm d}(l)/l\ll(1+\log T)^2$ in norm, where $\tau_{\rm d}$ is the divisor function. The actual $\beta$ integration has length $1/(5N)$. The negligible parts of §§2–3 can use the crude $T(1+\log T)$ tuple count. Hence the squared nonprincipal norm contributes $O_{C,\gamma,\varepsilon}(N L^{-1+B+\varepsilon})$ on one dyad.

The exact nonzero-numerator expansion multiplies this by at most $q/(q-1)$. It still has its actual $q$-nonunit and principal components. If $q\mid N$, the long unit restriction rules out $q\mid d$, and $k<X/2<q$, so the nonunit polynomial is zero. Otherwise for $q\mid m$ we need $q\mid d$ and $d=j q$ with $j=O(\lambda)$. For a fixed such $d$, the required $h$ and $l^2/(l,d)$ short moduli are coprime because $(l,N)=1$ and $h\mid N$. The absolute sum over $k\ll K$ is

$$
 O\!\left(K\sum_{h\mid\operatorname{rad}N}\frac1h
        \sum_{l\ {\rm sf}}\frac{(l,d)}{l^2}\right)
        \ll_{C,\gamma,\varepsilon} K L^\varepsilon.
$$

Indeed $\sum_h1/h\ll L_2$ and $\sum_{l\ {\rm sf}}(l,d)/l^2\ll\prod_{p\mid d}(1+1/p)\ll 2\tau_{\rm d}(j)$. Consequently its squared shell energy is $O(N L^{-1+\varepsilon})$ as before. The principal contribution follows from the actual numerator-zero ordinary squared norm $O(N)$ of $D^\dagger$, subtraction of these nonunits, and $\sum_q1/(q-1)\ll1/L$. It is not the principal term artificially added in the positive square.

Set $B=\eta=1/2$, take $\rho$ sufficiently small in (2), restore (3)'s discarded tail, and sum the $O_{C,\gamma}(L_2)$ dyads in norm. These ordinary transfers apply to the exact disjoint arcs by Parseval. This proves (1) for the genuine $D$ with every required unit prime. The true $D$ and $P$ have full-circle squared norms $O(N)$ as in R87. Cauchy, the contraction of separate numerator centering, and the same parity-preserving identity with error $O(N/L+N(X/M)^2)$ give the claimed signed consequences. They contain no assertion about squares of individual compensated offsets.
