# Round 9: bounded Gauss go/no-go at H=1/16

**Status: do not continue this implementation toward a full upper certificate.** One validated symmetric two-point Gauss sum is evaluated below for the same $N=32768$, $a=4/N$, $n=3$ arithmetic cross as Round 8. Its node uncertainty is small, but the available rigorous Gauss truncation error is not useful at this degree. The full arithmetic cross, high-to-high block, S, and R are not bounded. The continuous model in this particular cross can be bounded separately.

## Exact test and analytic error

Write $H=1/16$ and use the rank-one normalization from [spectral-round8.md](spectral-round8.md):
$$
 m_H=d\sum_{\sigma=\alpha,\beta}\int_{-H}^H f_\sigma(t)\,dt,\qquad
 f_\sigma(t)=\frac{R_3(\sigma+it)R_3(\sigma-it)}{(1+\sigma)^2+t^2}.
$$
On real $t$, $f_\sigma(t)$ is real nonnegative and even by the real coefficients of $R_3$. The two-point Gauss rule on $[-H,H]$ has nodes $\pm H/\sqrt3$ and weights $H$. Only the positive node on each boundary needs evaluation. The new script uses the frozen Round 8 Euler–Maclaurin and interval FFT primitives with the same analytic remainders. At these **points** the arithmetic and all denominator comparisons are enclosed. This is not an assumption that the interpolant already encloses the integral.

For a rigorous truncation error, take the Bernstein ellipse of parameter 2 for $[-H,H]$. Its semiminor is $3/64<\alpha/2$ and its semimajor is $5/64$. Both factors in $f_\sigma(t)$ stay in real-part positions at least $\alpha/2$ for the $s$ variable. Their denominators $|1+\sigma\pm it|$ are at least 1. Thus the elementary local-GRH bound of [spectral-round7-effective.md](spectral-round7-effective.md), and the finite diagonal subtraction, give
$$
 |f_\sigma(t)|\le V:=
 \left(22L^2\log(4N(4+5/64))+\log3\right)^2
$$
throughout this ellipse. In particular the integrand is holomorphic there under local GRH(N). Cauchy's estimate in the annulus after the Joukowski map bounds the degree-$j$ Chebyshev coefficient by $2V2^{-j}$. The degree-$(2m-1)$ polynomial therefore has sup error at most $4V2^{-2m}$. An $m$-node Gauss rule is exact on that polynomial and has positive weights of total mass $2H$, hence its integral error is at most $16HV2^{-2m}$ per line. For the summed Gram the proved error is
$$
 |m_H-Q_m|\le 32HdV2^{-2m}. \tag{1}
$$
Here $Q_m$ is the exact Gauss sum, distinct from the output enclosure of that sum. The ellipse and positivity bounds are mathematical; the node computation also depends on correct elementary mpmath 1.3.0 interval enclosures, as in Round 8.

The explicit prefactor $32HdV$ is approximately $1.659767193\times10^9$. Thus (1) at $m=2$ gives an error bound of approximately $1.037354495\times10^8$, whether or not the nodes are evaluated to very high precision. Even the illustrative target $10^{-4}$ **squared Gram** uncertainty first passes this particular bound at $m=22$, i.e. 22 distinct boundary evaluations after using evenness. This is a bound-specific scenario, not an inherent requirement of Gauss quadrature, a better analytic majorant, or the actual operator.

## Reproduction, measured limits, and decision

Run `PYTHONDONTWRITEBYTECODE=1 python3 spectral_round9_gauss.py` beside the frozen Round 8 script with mpmath 1.3.0. The one bounded run took **65.353 s total** in the cloud environment: **34.804 s** for the positive node on the $\alpha$ boundary and **29.875 s** on $\beta$. No additional nodes were launched. The checked two-point **Gauss sum**, rounded outward, was
$$
 0.00053552439<Q_2<0.00053552599 ,
$$
with raw interval width $1.587\times10^{-9}$ (rounded upward). All 8192 odd-character denominators on each line excluded zero at the evaluated node. In the script their minimum lower bounds on the unscaled squared DFT were $>1317.89$ and $>3772.01$, respectively. The positive-node enclosures are reproduced directly in the output; the negative node is determined by reflection.

The main failure is **quadrature error, not node rounding**. At the current evaluator speed, 22 distinct boundary evaluations would extrapolate to approximately 11.9 minutes of sequential node work, but that run was not made and a parallel or optimized implementation could differ. More importantly, even an exact value of $m_{1/16}$ leaves the positive omitted-height contribution to $\|B_{\rm arith}\|^2$. The fully numerical tail majorant in [spectral-round7-effective.md](spectral-round7-effective.md) extends to $H>0$ by the same integral proof and is above $10^9$ at this cutoff, hence gives no useful residual margin. This is not a lower bound on the true tail. The go/no-go is therefore **no-go** for extending this particular evaluator and majorants by adding nodes. A credible next upper certificate would require a substantially tighter validated analytic envelope and a useful omitted-height bound (or an alternative certificate avoiding that tail), in addition to the still-independent high-to-high bound.

## A useful model estimate, independent of the height test

The model cross in this prefix has $\|B_{\rm model}\|<8Sa<1/512$, where $S=\mathfrak S(32768)<2$ and $a=1/8192$. This is an explicit instance of the signed cumulative argument of [spectral-round6.md](spectral-round6.md); it is not a bound on the arithmetic cross.

Here are details of the constants. For $u<x\le a$ and $y\ge1-a$, split the model mass into the completed difference $\sqrt{k+u}-\sqrt{k-u}$ for those $u$ with both terms present, and a solely negative unmatched part on $|y-k|<x$. For completed portions, the difference is at most $(1-a)^{-1/2}u/\sqrt{k}$, and
$$
 \sum_{k\le y}\frac{\mathfrak S(kN)}{\sqrt k}
 \le 2 S\sqrt y\prod_{p>2}\left(1+\frac1{p(p-2)}\right)
 \le2S\sqrt y\,e^{3/4}.
$$
The final Euler bound uses $\sum_{j\ge3}1/(j(j-2))=3/4$. Thus the completed part of the cumulative mass is bounded by $2Sx^{5/2}\sqrt y$. For the unmatched part its absolute value is at most $(2/3)\mathfrak S(kN)\sqrt{k}(x^{3/2}-|y-k|^{3/2})$ on its single possible interval. One has
$$
 \sum_{k\ge1}\frac{\mathfrak S(kN)^2}{k^2}
 \le S^2\zeta(2)\prod_{p>2}(1+(2a_p+a_p^2)/p^2)<9S^2,\quad a_p=1/(p-2).
$$
Indeed $2a_p+a_p^2\le3$, $\sum_{j\ge3}j^{-2}\le4/9$, $\zeta(2)<2$, and $e^{4/3}<4$. Also $w(y)^{-1}<1/4$ for $y\ge1-a$, using $e^{-2}<1/7$, $N^{-1/4}<1/12$, and $(1-a)^{-1/4}<1.001$. Finally $\int_0^a x^i w(x)^{-1}\,dx\le 2a^{i+1}/(i+1-2\beta)$ for $i=1,2$, because $Na=4$. After the physical kernel multiplier $2\pi/(x^{3/2}y^{3/2}\sqrt{w(x)w(y)})$, the completed part has Hilbert–Schmidt norm $<a S/4$ by integrating $y^{-2}$ and then $x^2/w(x)$. For the unmatched part,
$$
 \int_{-x}^x (1-(|u|/x)^{3/2})^2\,du=\tfrac9{10}x,
$$
and $\sqrt{k}/y^{3/2}\le (1-a)^{-3/2}/k$. Its Hilbert–Schmidt norm is at most
$$
 \frac{4\pi}{3}(1-a)^{-3/2}\frac12\sqrt{\frac9{10}\cdot9\cdot\frac87}\, Sa <7Sa .
$$
Both estimates are on the true entire right output. Summing the norms yields the claimed explicit upper. This shows that, at this fixed prefix, the separate beta cross can be essentially removed from a moderate-precision budget. It does not cure the height or high-block obstacle.
