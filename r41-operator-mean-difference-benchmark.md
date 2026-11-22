# The exact benchmark seen by the exterior mean differences

**Scope.** This computes the deterministic comparison on the genuine [exterior mean differences](r40-operator-negative-difference-subspace.md) at inverse-log precision. It proves the sign and size of the Beta-model compression, identifies the corresponding *signed prime-integer* covariance target, and shows why the R40 trace proof cannot decide it. It does not estimate that prime covariance.

Use the physical/log unitary realization and the notation of R40: $L=\log N$, $\ell=\log L$, $Y=e^H$, and

$$
 (K+3)\ell^2/\log\ell\le H\le L^{1-\eta},
 \qquad 0<\eta<1,\quad K>0.
$$

Keep the R38/R39 cutoffs and use the **full odd family** in the long-divisor Gram. Assume the original local Dirichlet GRH at the even modulus $N$. Let $C>1$ be fixed and $W$ the union of the whole physical dyads $I_V=[V,2V)$ contained in $[Y,e^{CH}]$, on the same grid $V=2^jY$. Write $v=\log V$, $m(x)=((Ne^x)^{-2/L}+(Ne^x)^{-1/4})^{1/2}$, and $r_N(u)=u^{-3/2}m(\log u)$. Let $e_V$ be the real unit R40 difference on its dyad, oriented negative on the lower union of cells and positive on the upper union. The test satisfies $\int r_N(u)e_V(u)\,du=0$. Write $\mathcal E=\operatorname{span}\{e_V:I_V\subset W\}$, and represent any compression to $\mathcal E$ as a matrix in these orthonormal vectors. The [log-separation mask](r31-operator-zero-diagonal.md) is one on the entire product of these supports, since $CH=o(L)$.

Set $B_N=D_N+K_N$. For the unitary log image $E_V(x)=e^{x/2}e_V(e^x)$, define $F_V=mE_V$, and put

$$
 \begin{split}
 c_V&=\pi\iint e^{-|x-z|}F_V(x)F_V(z)\,dx\,dz,\\
 \theta_V&=\pi\iint e^{-|x-z|}(\min(x,z)-v)F_V(x)F_V(z)\,dx\,dz,\\
 b_N&=\sum_{p\mid N}\frac{\log p}{p-1},\qquad
 \kappa_j=3/2+2j,\qquad
 \sigma_\psi=\psi(3/4)-\sum_{j\ge0}\frac{2}{\kappa_j(\kappa_j^2-1)} .
 \end{split}
 \tag{1}
$$

Here $\psi=\Gamma'/\Gamma$. Let $G$ be the matrix obtained by testing the weighted kernel $m(x)k_*(x-z)m(z)$ on the $E_V$'s, with

$$
 k_*(s)=\sum_{j\ge0}\frac{2\pi}{\kappa_j^2-1}e^{-\kappa_j|s|}.
 \tag{2}
$$

This is an explicit positive-semidefinite matrix of bounded operator norm. For all distinct $V,U$ on this strip,

$$
 G_{V,U}<0,\qquad |G_{V,U}|\asymp \exp[-(3/2)|\log V-\log U|].
 \tag{3}
$$

The original integer diagonal and the full benchmark satisfy the matrix identity

$$
 (D_N-B_N)_{\mathcal E}
 =
 \operatorname{diag}_{V}
      \big(c_V(v+\log\pi+b_N-\sigma_\psi-1/2)+\theta_V\big)
   -G+o_{\rm op}(L^{-K}).
 \tag{4}
$$

In particular $c_V\asymp1$, $|\theta_V|\ll1$, and $- (K_N)_{\mathcal E}$ lies between $cH I$ and $C' H I$ for positive constants on this strip. The symbols $o_{\rm op}$ refer to operator norm of the entire growing matrix. This is not a per-entry approximation accumulated over the dimension.

## 1. The deterministic calculation and the sign of the matrix remainder

The exact Volterra moment is $\int e^{-x}F_V(x)\,dx=0$, by changing $u=e^x$ in $\int r_N e_V$. For distinct ordered dyads, $x<z$ whenever $x$ is in the earlier support and $z$ in the later one, up to null endpoints. Thus the $e^{-|x-z|}$ kernel tested on the $F_V$'s has zero cross entry, because it factors and the later moment is $\int e^{-z}F_U(z)\,dz=0$. The corresponding matrix with factor $\pi$ is exactly $\operatorname{diag}(c_V)$.

On the strip $m(x)\asymp1$, and the upper part of $F_V$ is uniformly positive and bounded below on a fixed relative log interval inside $(\log(7/4),\log2)$ translated by $v$. This is because the raw full R30 cells fill any fixed inner interval for all large $N$, $\|r_N{\bf1}_{I_V^\pm}\|_2\asymp V^{-1}$, and the log unitary weight is $e^{-x}m(x)$. Pair with a nonnegative fixed smooth compact test in that inner interval. The pairing is bounded below, and the translated test has bounded $H^1$ norm. Consequently $\|F_V\|_{H^{-1}}\gg1$, by Fourier Cauchy–Schwarz with weights $1+t^2$ and $(1+t^2)^{-1}$. The transform of $e^{-|s|}$ is $2/(1+t^2)$ in the ordinary frequency convention, so $c_V\asymp1$ follows from this lower bound and $\|F_V\|_2\ll1$. Also $|\theta_V|\ll1$ because the support has log length $\log2$.

The [stationary kernel](operator-post-r15-stationary-tail.md) (with the [uniform moving-contour error](weak-s-exterior-fine.md#diagonal-and-beta-benchmark)) has bare multiplier density $[L-\log\pi-b_N+\Re\psi(3/4+it/2)]/(1+t^2)$, and kernel given by its integral against $e^{its}$. The convergent digamma series gives

$$
 \Re\psi(3/4+it/2)
 =\psi(3/4)+\sum_{j\ge0}\frac{2t^2}{\kappa_j(t^2+\kappa_j^2)} .
$$

After division by $1+t^2$, partial fractions and the integral
$\int_{\mathbb R}e^{its}(t^2+a^2)^{-1}dt=(\pi/a)e^{-a|s|}$
show that the model kernel equals

$$
 (L-\log\pi-b_N+\sigma_\psi)\pi e^{-|s|}+k_*(s).
 \tag{5}
$$

The partial-fraction integrals are absolutely summable in $j$, since the sum of their $L^1(dt)$ bounds is $O(\sum_j \kappa_j^{-2})$. The kernel in (2) is a positive mixture of PSD convolution kernels and has $L^1(ds)$ norm $O(1)$, so $\|G\|\ll1$ and $G\ge0$.

For ordered $V<U$ and any fixed $\kappa>1$, the off-diagonal entry of $e^{-\kappa|s|}$ on these profiles factors as

$$
 \left(\int e^{\kappa x}F_V(x)\,dx\right)
 \left(\int e^{-\kappa z}F_U(z)\,dz\right).
$$

The signed measures $e^{-x}F_V(x)\,dx$ each have total zero, with all their negative mass below their positive mass. Since $e^{(\kappa+1)x}$ is strictly increasing and $e^{-(\kappa-1)x}$ strictly decreasing, the first factor is positive and the second negative. At $\kappa=3/2$ their absolute sizes are comparable to $e^{3v/2}$ and $e^{-3\log U/2}$. Indeed the positive and negative masses of $e^{-x}F_V(x)\,dx$ each have size $\asymp e^{-v}$, and their supports are separated by a fixed positive log gap; factoring out the indicated $e^{\pm3v/2}$ bounds the corresponding increasing/decreasing relative weights away from equal values on the two supports. Every mixture term therefore has the same negative off-diagonal sign, and the first proves the lower size in (3). For the upper size, $|x-z|\ge|\log U-\log V|-\log2$; since the left-hand side is nonnegative, every $e^{-\kappa_j|x-z|}$ is at most $e^{(3/2)\log2}e^{-(3/2)|\log U-\log V|}$. Use $\|F_V\|_1\ll1$ and the convergent sum of mixture coefficients. This also covers adjacent dyads.

The original $D_N$ is exactly diagonal on these directions because its unit prime-power prefix atoms pair with $e_V$ only for $n\in(NV,2NV)$, by the R40 Volterra identity. On its diagonal use the R17 true log-coordinate expansion with bare kernel $\pi e^{-|x-z|}(L+\min(x,z)-1/2)$ at uniformly inverse-polynomial HS error. The resulting compressed matrix is $\operatorname{diag}(c_V(L+v-1/2)+\theta_V)+o_{\rm op}(L^{-K})$; for the diagonal error one can just take its supremum (or the global HS estimate). By R30 and (5), $B_N$ compresses to $\operatorname{diag}(c_V(L-\log\pi-b_N+\sigma_\psi))+G+o_{\rm op}(L^{-K})$. This proves (4). Finally $b_N=O(\log L)$ by Chebyshev and splitting its prime divisors at $L$, whereas $H\gg\log L$. Hence the claimed semidefinite comparison for $-K_N$ follows. No global Dirichlet GRH is used.

## 2. The true signed target and the limit of the trace route

For each $V$ set

$$
 \beta_V(n)=\frac{\sqrt{2\pi n}}{N}\Lambda(n){\bf1}_{(n,N)=1}
                  \int_{u\ge n/N}r_N(u)e_V(u)\,du .
$$

These are genuine nonnegative prime-power weights. The integral is nonnegative because the signed measure $r_N e_V\,du$ has negative mass only below its positive mass and total zero. It vanishes outside the raw dyad. Character orthogonality therefore gives the exact matrix of $P_N-D_N$ on $\mathcal E$:

$$
 \mathcal A_{V,U}=
 \sum_{n\ne m}\beta_V(n)\beta_U(m)
     \big({\bf1}_{n\equiv m\ (N)}-{\bf1}_{n\equiv-m\ (N)}\big).
 \tag{6}
$$

The full-family deletion estimate from the [finite-strip full-family estimate](r39-operator-long-divisor-diagonal-inflation.md#4-full-odd-family-corollary-literal-signed-congruence-aliases-on-this-strip) and the original trace imply $\|(P^{>}-P_N)_{\mathcal E}\|_{\rm HS}=o(L^{-K})$, by rank-one Cauchy–Schwarz. Thus both the original signed compression $T_{N,\mathcal E}$ and the actual long-divisor compression $(P^{>}-B_N)_{\mathcal E}$ equal, up to $o_{\rm op}(L^{-K})$,

$$
 \mathcal A+
 \operatorname{diag}_{V}\big(c_V(v+\log\pi+b_N-\sigma_\psi-1/2)+\theta_V\big)-G .
 \tag{7}
$$

In particular an inverse-log norm bound would require reflected prime-power pairs to exceed the same-residue distinct pairs on each individual $e_V$ by $c_V(v+b_N)+O(1)$. For adjacent log dyads it would also require the signed off-diagonal matrix entry $\mathcal A_{V,U}$ to be negative of order one, matching $G_{V,U}$, not merely to be small. Neither requirement follows from (4) alone.

Finally, even keeping the true inflated integer diagonal on $\mathcal E$, positivity and the trace bound used in R40 cannot on their own force cancellation or even a sign in (7). Concretely, that inflated compressed diagonal is at least $cL^2/H$ times the identity by R40. The actual benchmark compression is positive with eigenvalues $\asymp L$ by (5), and has trace $\asymp LH=o(L^2)$ as $\dim\mathcal E\asymp H$. If one retains only these facts and the $O(L^2)$ positive Gram trace constraint, the hypothetical PSD matrices $0$, $B_{N,\mathcal E}$, and $2 B_{N,\mathcal E}$ all have that trace budget and all obey the strong negative comparison against the inflated diagonal, since $H=o(L)$. Their differences from the actual benchmark nevertheless have negative, zero, and positive signs, respectively. This is only a logical limit of that trace argument, not a model or counterexample for the actual prime matrices. Formula (7) preserves both signs and the benchmark; its true arithmetic cancellation, the original norm, and weak S remain open.
