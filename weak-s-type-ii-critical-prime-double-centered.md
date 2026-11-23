# Remove the complementary constant mode at critical prime denominators

Retain the even $N$, $X=\sqrt N$, $L=\log N$, fixed proportional prime boxes, arbitrary bounded selector on the prime pairs, hard intervals, and true signed $P$ from [the critical-prime analysis](weak-s-type-ii-critical-prime-arcs-principal-projection.md). Use the **full** complementary $D$ from the [signed-seam analysis](weak-s-type-ii-signed-seam-major-arcs.md), with no extra lower cutoff on $d$ beyond $d\ge X$. Thus it has $N-y\le dk<N/2$, $k>t\ge N^{.49999}$, any prescribed hard $I_d$, both $N$-unit masks, and the weight $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}=\mu(d)\mu^2(dk)$. The shell is $\mathcal Q=\{q\text{ prime}:.8X\le q\le .9X\}$, with complete numerators and $|\beta|\le 1/(10N)$; put $e(z)=e^{2\pi iz}$.

On an arc let $P^*_q(a,\beta)=P(a/q+\beta)-P^{(0)}_q(a/q+\beta)$, where $P^{(0)}_q=-P(\beta)/(q-1)$ is the exact principal projection. Let

$$
 D^{(0)}_q(\beta)=\frac1{q-1}\sum_{a=1}^{q-1}D(a/q+\beta),\qquad
 D^*_q(a,\beta)=D(a/q+\beta)-D^{(0)}_q(\beta).
$$

**Theorem.** Unconditionally, with effective constants, the other one-sided constant projection satisfies

$$
 \int_{|\beta|\le1/(10N)}
      \sum_{q\in\mathcal Q}
       \left|\sum_{a=1}^{q-1}P^*_q(a,\beta)D^{(0)}_q(\beta)
                         e(-N(a/q+\beta))\right|d\beta
           \ll \frac{N}{L^2}.
$$

The numerator sign is kept; this is not a bound for the integral of the absolute values of the individual numerator terms. It treats the actual nonprincipal prime leg against the complementary **constant** mode, including the nonunit complementary products rather than just a constant model for unit products. It does not bound the pairing where both modes are nonprincipal.

## 1. A uniform bound for the complementary constant

Let $B_q(\beta)$ be the sum defining $D(\beta)$ restricted to $q\mid dk$. Exact numerator averaging gives

$$
       D^{(0)}_q(\beta)=\frac{q B_q(\beta)-D(\beta)}{q-1}.
$$

The term $D(\beta)$ is exponentially small by the $q=1$ signed-seam major-arc theorem. If $q\mid N$ then $B_q=0$ by the genuine unit mask. Otherwise $k<N/(2d)\le .5X<q$, so a nonunit product must have $d=qr$. The automatic ceiling $d<N^{.50001}/2$ forces $r\ll N^{.00001}$, and hence $r<q$ for large $N$. The sign is exactly $\mu(d)=-\mu(r)$, also at zeros of $\mu(r)$. Keep $(r,N)=1$ and the hard interval $qr\in I_d\cap[X,\infty)$. Coprimality of $k$ to $q$ is automatic throughout its interval.

For a fixed such $r$, let $J_r$ be the actual real $k$ interval imposed by $t<k$ and $N-y\le qr k<N/2$. Counting squarefree integers coprime to $rN$ by the square-divisor expansion and unit-mask inclusion-exclusion gives a main term with density

$$
       C(rN)=\frac1{\zeta(2)}\prod_{p\mid rN}\frac{p}{p+1}
            = C(N)\prod_{p\mid r}\frac p{p+1}.
$$

In detail, after $k=c^2\ell$ the square base $c$ is coprime to $rN$ and $\ell=h j$ after expanding the latter unit mask by $h\mid rN$. On each prefix the count differs from its continuous length divided by $c^2h$ by $O(1)$. Summing these errors over $c\le\sqrt{N/(qr)}$ and $h\mid rN$, and extending only the main square sum to infinity, yields $O(\sqrt{N/(qr)}\,\tau(rN))$ error. Partial summation against $e(\beta qr k)$ costs $O(1+|\beta|N)=O(1)$, including sharp endpoints. Thus the corresponding main integral is

$$
 \frac{C(rN)}{qr}\,G_\beta(r),\qquad
       G_\beta(r)=\int_{\max(N-y,t q r)}^{N/2} e(\beta z)\,dz
$$

with zero after clipping at the final endpoint. The supremum and total variation of $G_\beta$ are $O(N)$, since the lower endpoint increases monotonically until the integral is empty. Summing the count errors gives at most $N^{.250005+\epsilon}$ for any fixed $\epsilon>0$, hence $o(X)$.

It remains to bound the main signed harmonic sum uniformly in $N$. Let $f_N(r)=\mu(r)\mathbf1_{(r,N)=1}\prod_{p\mid r}p/(p+1)$. It is $\mu * \rho_N$, where $\rho_N$ is multiplicative and on all $p^j$, $j\ge1$, equals $1$ for $p\mid N$ and $1/(p+1)$ otherwise. This follows by dividing the relevant local series by $1-p^{-s}$. The elementary identity $\sum_{n\le T}\mu(n)\lfloor T/n\rfloor=1$ for $T\ge1$ gives $\left|\sum_{n\le T}\mu(n)/n\right|\le2$ by subtracting the fractional parts. Hence all harmonic prefixes of $f_N$, after multiplication by $C(N)$, are bounded uniformly: indeed

$$
 C(N)\sum_{h\ge1}\frac{\rho_N(h)}h
   =\frac1{\zeta(2)}
       \prod_{p\mid N}(1-p^{-2})^{-1}
       \prod_{p\nmid N}\left(1+\frac1{(p+1)(p-1)}\right)\ll1.
$$

The density cancels the possible loss from the $N$-unit mask. Abel summation with $G_\beta$ and the exact hard $r$ interval therefore costs $O(N/q)=O(X)$. We conclude that $B_q(\beta)\ll X$, and hence $D^{(0)}_q(\beta)\ll X$, uniformly in the shell and $\beta$.

## 2. The exact remaining numerator on the prime side

Write $P_q(N,\beta)$ for the weighted prime sum on the $P$ support with $uv\equiv N\bmod q$ imposed. If $q\mid N$, all $uv$ are units modulo $q$, and $\sum_a P^*_q(a,\beta)e(-Na/q)=0$ by the zero mean. If $q\nmid N$, finite geometric summation and the principal subtraction give exactly

$$
  \sum_{a=1}^{q-1} P^*_q(a,\beta)e(-Na/q)
       =q\left(P_q(N,\beta)-\frac{P(\beta)}{q-1}\right).
$$

We show $|P_q(N,\beta)|\ll X/L$ uniformly at actual $q$. It suffices to bound the number of prime solutions in the two complete fixed proportional intervals by $O(X/L^2)$, since $|E|\le1$, the exponential is bounded by one, and the weight is at most $L$. The optional product and $N$-unit cuts can be dropped for this upper bound.

Here are direct elementary sieve details. Put $R=N^{.01}$, $G=\sum_{r\le R}\mu^2(r)/\varphi(r)\gg\log R$ by the usual elementary squarefree count and $\varphi(r)\le r$. Choose real $\lambda_d$ supported on $d\le R$ by finite Möbius inversion so that

$$
       \sum_{\substack{d\le R\\r\mid d}}\frac{\lambda_d}{d}
                   =\frac{\mu(r)}{G\varphi(r)}\qquad(r\le R).
$$

Inversion gives $\lambda_1=1$, zero on nonsquarefree $d$, and $|\lambda_d|\le d/\varphi(d)\le\tau(d)$ on squarefree $d$. To see the latter, write $\lambda_d/d=\sum_{j\le R/d}\mu(j)\mu(dj)/(G\varphi(dj))$ and factor $\varphi(dj)=\varphi(d)\varphi(j)$ on the nonzero squarefree coprime terms; the resulting restricted sum is at most $G$. Thus $\sum_{d\le R}|\lambda_d|\ll R\log(2R)$. The weight $\nu(n)=(\sum_{d\mid n,\ d\le R}\lambda_d)^2$ is nonnegative and equals one for every prime in the boxes. Its model density is

$$
 \sum_{d,e\le R}\frac{\lambda_d\lambda_e}{[d,e]}
   =\sum_{r\le R}\varphi(r)
          \left(\sum_{\substack{d\le R\\r\mid d}}\frac{\lambda_d}{d}\right)^2
   =G^{-1},
$$

using $(d,e)=\sum_{r\mid d,e}\varphi(r)$.

Expand $\nu(u)\nu(v)$. The divisibility conditions become $\ell_1\mid u,\ell_2\mid v$, with $\ell_i$ least common multiples of two sieve indices, at most $R^2<q$ and units modulo $q$. After rescaling both intervals the exact congruence is $x z\equiv N(\ell_1\ell_2)^{-1}\bmod q$ with unit numerator. The rectangular estimate is

$$
   \frac{|I_u||I_v|}{\ell_1\ell_2}\frac{q-1}{q^2}
         + O(q^{1/2}L^2).
$$

For completeness, complete each rescaled interval on $\mathbb Z/q\mathbb Z$. Its normalized additive Fourier coefficients have absolute sum $O(\log(2q))$ by the geometric sum bound. For the inverse-residue graph the double Fourier coefficient before normalization is a Kloosterman sum, of magnitude $O(q^{1/2})$ away from the double zero, by the [Weil bound, Iwaniec–Kowalski Cor. 11.12](https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf#page=14); a single zero frequency gives $-1$. The zero pair has $q-1$ points, and rounding interval lengths costs $O(1)$. This gives the displayed estimate.

The total sieve main term is $O(X G^{-2})=O(X/L^2)$ by the density identity applied separately on each variable, while the absolute error is $O(q^{1/2}L^2(R\log(2R))^4)=O(N^{.29} L^6)$, smaller than the main upper bound. Hence $|P_q(N,\beta)|\ll X/L$ as claimed. Also $|P(\beta)|\ll N/L$ by the elementary prime upper bound.

The exact signed prime numerator is therefore $O(N/L)$. Since $D^{(0)}_q\ll X$, $\#\mathcal Q\ll X/L$, and the integration width is $O(1/N)$, this proves the theorem.

## 3. An exact bilinear description of what still remains

For fixed $q,\beta$, write $p_q(r)$ and $d_q(r)$ for the exact additive residue masses of the two polynomials with their slow phase $e(\beta m)$. On the units subtract their separate means: $p^*_q(r)=p_q(r)-P(\beta)/(q-1)$ and $d^*_q(r)=d_q(r)-(D(\beta)-B_q(\beta))/(q-1)$. Set both centered masses to zero at $r=0$. Their additive transforms at nonzero $a$ are exactly $P^*_q(a,\beta)$ and $D^*_q(a,\beta)$, and at $a=0$ both are zero. Thus the remaining signed product on a shell denominator has the exact form

$$
  \sum_{a=1}^{q-1} P^*_q(a,\beta)D^*_q(a,\beta)e(-Na/q)
       =q\sum_{\substack{r\bmod q\\ r\ne0,\ N-r\ne0}}
                         p^*_q(r)d^*_q(N-r).
$$

This is an identity, not an upper bound on the double-centered covariance. Neither one-sided projection result estimates that covariance, the full critical shell, or weak S.
