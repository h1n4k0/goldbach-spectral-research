# Round 4: a certified Rayleigh lower bound for the actual operator at N=30030

At the modulus used in the numerical appendix of [Li and Liu](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf), a reproducible rational calculation certifies
$$
 \lambda_{\min}(T_{30030})<-0.135\quad\text{and}\quad
 0.43<\delta_{30030}<0.44.
$$
Identifying the arithmetic pairing with the Hardy operator assumes the paper's `GRH(30030)`; the finite arithmetic and interval bounds do not assume it. The modulus is one instance and was chosen to match the paper. This is a **lower** bound for the full operator norm; it neither certifies nor refutes even the individual R bound at this modulus. The paper's Appendix C estimate comes from a different finite model and must not be used as an upper bound here.

## Reproduction

Run from the directory containing this note:

```sh
python3 spectral_round4_verify.py
```

The verifier uses only the Python standard library. There are no floating-point calculations, no external packages, no downloaded data, no zero tables, and no numerical $L$-function evaluations. It prints decimal endpoints rounded outwards. The checked output is:

```text
N = 30030 ; nonzero atoms = 11089 ; ordered difference / sum terms = 15644 / 20966
singular series in [5.12121603, 5.12125868]
arithmetic form in [-1995854.06852923, -1995854.06852922] ; exact signed continuous mass multiplier = -1121827/3
residual numerator in [-80814.59343976, -80798.65045472] ; squared Hardy norm <= 594851.97154438
certified: lambda_min(T_30030) < -0.135, and 0.43 < delta_30030 < 0.44.
Only a lower bound for ||T_30030||; GRH(N) is assumed for operator identification.
```

## Why this tests the true operator

The trial function $f$ is the fixed piecewise-affine function with knot heights listed in the script. The knots are at $i/16$, and the zero extension is supported in $[1/16,4]$. The large integer heights are a convenient exact normalization; multiplying all by a common constant does not change the Rayleigh quotient. The function was selected by an exploratory double-precision calculation, but the verified result does not depend on that approximate eigenproblem.

Apply the arithmetic pairing of [arithmetic.md](arithmetic.md) or [source-round2.md](source-round2.md), extending smooth tests to compactly supported $H^1$ by density. The weighted Hardy norm is continuous in this topology; finite prime-power evaluations are continuous by the one-dimensional Sobolev embedding and the finite continuous model integrals are continuous under uniform approximation. Thus the unsmoothed affine corners do not add an arithmetic or boundary term. The exact numerator is
$$
 \langle T_Nv_f,v_f\rangle=
 \frac1N\sum_{(nm,N)=1}\Lambda(n)\Lambda(m)
 f(n/N)f(m/N)
 \big(\mathbf1_{n\equiv m\bmod N}-\mathbf1_{n=m}-\mathbf1_{n\equiv-m\bmod N}\big)
 -\sum_{k=1}^{8}\mathfrak S(kN)
 \int_{\mathbb R}\big(2f(u)f(u+k)-f(u)f(k-u)\big)\,du.
$$
The modulus is divisible by every prime at most 8, so all $\mathfrak S(kN)=\mathfrak S(N)$ in this finite sum. The exact continuous mass multiplying this singular series is $-1121827/3$. Products of affine functions on each knot interval are integrated as quadratic polynomials: for endpoint pairs $(a,b)$ and $(c,d)$ the product integral on a unit interval is $(2ac+ad+bc+2bd)/6$. Orthogonality and the zero extension exclude all other congruence partners and model lines. In particular, this is not a sampled kernel or an estimate that omits high-height directions: it is one exact quadratic form of the true operator, and the variational lower bound needs no spectral-tail estimate.

The finite numerator is enclosed using integer sieve enumeration and outward rational bounds on $\log p$. Binary range reduction and the geometric remainder of the positive $2\operatorname{arctanh}$ series give the log intervals. For the singular series, the finite product is outward rounded and the tail is bounded by
$$
 \prod_{p>M}(1-(p-1)^{-2})\ge1-\sum_{n>M}(n-1)^{-2}\ge1-1/(M-1),
 \qquad M=4N.
$$
Finally Proposition 7.4 gives
$$
 \|v_f\|^2=\frac{1}{2\pi}\int_0^4
 \frac{|f(u)/2-uf'(u)|^2}{(Nu)^{-2/\log N}+(Nu)^{-1/4}}\,du .
$$
This positive weight increases with $u$. On each subinterval the right-endpoint weight is bounded above using rational enclosures for $\log$ and the exponential (a Taylor polynomial plus an explicit geometric bound on the remaining positive series). The integral of the remaining square is exact, and replacing $\pi$ by its elementary lower bound $3.14$ gives a genuine upper bound on $\|v_f\|^2$. The displayed numerator **upper** endpoint is negative, and dividing it by the norm-squared **upper** bound yields the certified upper bound on this negative Rayleigh quotient. The spectral scale comparison is made by squaring the rational endpoint candidates and bounding $\mathfrak S(N)(\log N)^3/N$.

## Why the preceding global finite approximation was not run

This is a limitation of the **particular sufficient error budget** in [spectral-round2.md](spectral-round2.md), not a lower bound on the complexity of every method. At $N=30030$, even allowing error $0.05$ solely for the beta term, the conservative inequalities there are not close to practical implementation. Indeed $\mathfrak S(N)>4$, $(\pi/N)^{2/\log N}>e^{-2}>1/8$, and $P_N(\sigma)\ge1$ on the positive real axis. Hence in that budget the coefficient multiplying each positive beta-tail term is above $1/2$. The condition on the Euler-summation truncation is at least
$$
 B_0>(84000)^4>10^{19}.
$$
For the Euler density cutoff it entails
$$
 D_0>(105000)^{\log 30030}>10^{50}.
$$
These are thresholds for the **bounds**, not demonstrated necessities for the true tails. The lower-Rayleigh certificate above avoids both. A useful full-norm upper certificate will need a different global compression and a much sharper quantitative tail analysis.
