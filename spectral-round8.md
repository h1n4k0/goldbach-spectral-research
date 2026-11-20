# Round 8: validated function evaluation for an exact finite-height Gram

This is a fixed-modulus **finite-height** check. It validates the $L'/L$ input and the arithmetic-block matrix element introduced in [spectral-round7.md](spectral-round7.md), not the whole operator or the entire arithmetic cross. No inference about S or R is made.

Take $N=32768=2^{15}$ and the true physical low prefix $0<x<4/N$. Its only active unit prime power is $3$; the low-to-high arithmetic cross has rank one (and its beta-model part is distinct). In the notation of Round 7 put
$$
d=\|D_{\mathrm{low}}\|
 =6\pi(\log3)^2\int_3^4 v^{-3}\left(v^{-2\alpha}+v^{-1/4}\right)dv,
 \qquad \alpha=1/\log N,\quad\beta=1/8.
$$
The finite-height arithmetic Gram has the single potentially nonzero eigenvalue
$$
m_H=d\sum_{\sigma\in\{\alpha,\beta\}}\int_{-H}^H
 \frac{|R_3(\sigma+it)|^2}{(1+\sigma)^2+t^2}\,dt .
$$
This uses the sum of the two boundaries and cancels the factor $N/(2\pi)$ of the right Gram against the coefficient normalization $2\pi/N$. The finite height $[-H,H]$ is imposed on the transform variable; it is not a cutoff on zeros, raw prime sizes, or the additive coordinates.

## Validated evaluator

Let $q=N/4=8192$, let $r_j=5^j\bmod N$, and choose $\omega=e^{-2\pi i/q}$. The code verifies that $r_j$, $0\le j<q$, are exactly the units $1\bmod 4$. Every odd character has $\chi_k(r_j)=\omega^{kj}$ and $\chi_k(-r_j)=-\omega^{kj}$, so
$$
L(z,\chi_k)=N^{-z}\sum_{j=0}^{q-1}\omega^{kj}
  \left[\zeta(z,r_j/N)-\zeta(z,1-r_j/N)\right].
$$
Here $z=1/2+s$. The finite Fourier sums and their first $z$-derivatives are evaluated simultaneously by two interval radix-2 transforms. If $r_{j_3}\equiv-3\bmod N$, then $\overline\chi_k(3)=-\overline{\omega^{kj_3}}$. The constant $-\log N$ in $L'/L$ cancels exactly in this nontrivial residue character average. The script adds the exact subtraction $-(\log3)\,3^{-z}$ for the $m=n$ diagonal. It checks numerically with interval lower endpoints that no Fourier denominator contains zero anywhere in either entire input rectangle. Therefore this finite computation does not infer zero-freeness from an unverified numerical sample or assume GRH to avoid a local pole. Use of the resulting matrix for the original operator is still conditional on GRH($N$) as in Round 7.

The Hurwitz sums and derivatives are evaluated by an explicitly implemented Euler–Maclaurin formula, not by a library call to a special function. With $J=8$, six Bernoulli terms, $a\in(0,1)$, and on either Cauchy disk of radius $1/32$ around the input $z$ rectangles, one has $\Re z\ge1/2$ and $|z|\le1$. Thus the periodic Bernoulli bound gives
$$
 |E_6(z,a)|\le
 \frac{2\zeta(12)}{(2\pi)^{12}}\frac{|(z)_{12}|(J+a)^{1-\Re z-12}}{\Re z+11}
 \le \frac{4(12)!}{6^{12}}\,\frac{J^{1/2-12}}{12-1/2}.
$$
Its derivative is bounded by 32 times the same displayed magnitude by Cauchy's formula. The verifier inserts these analytic remainder radii into each input rectangle before Fourier transformation. In the centered transform it first evaluates a certified enclosure of the DFT of the interval midpoints, then adds the sum of the individual complex perturbation radii to every output. This is rigorous because the exact DFT entries have modulus one. It avoids repeatedly inflating coefficient uncertainty with rectangular enclosures of rotations. The last integral is bounded by the rectangle enclosure for $|R_3|^2/|1+s|^2$ over the whole band times the band width. It uses no unvalidated numerical integrator.

The elementary arithmetic uses [mpmath 1.3.0's interval context](https://mpmath.org/doc/current/contexts.html), with basic arithmetic, $\pi$, elementary logarithms and exponentials. Interval correctness is conditional on those elementary enclosures being implemented correctly; this is not a formal verification of the library. Endpoint comparisons for nonzero denominators are part of the run. No black-box evaluations of $L,\zeta$, or their derivatives are used.

## Reproduction and interpretation

Run `python3 spectral_round8_band.py` in an environment with mpmath 1.3.0. The checked run used $H=2^{-24}$ and gave these outward-rounded enclosures:

| Boundary | $\Re R_3$ throughout the band | $\lvert\Im R_3\rvert$ | Smallest lower bound on the unscaled $\lvert\mathrm{DFT}\rvert^2$ |
|---|---:|---:|---:|
| $\alpha$ | $[0.05651,0.07262]$ | $<0.008315$ | $>1304.88$ |
| $\beta$ | $[0.03890,0.05039]$ | $<0.005945$ | $>3729.39$ |

The scalar $d$ is approximately $0.84341554$ and the finite squared-norm Gram satisfies
$$
 3.875\times10^{-10}<m_{2^{-24}}<6.515\times10^{-10}.
$$
These margins are wider than the raw interval returned by the script. This validates only the finite band. Applying exactly this small-width interval-box implementation to $[-1,1]$ by tiling would take $2^{24}$ panels; that count is a property of this implementation, not a limit for higher-order centered quadrature, a different validated evaluator, or the actual operator. The omitted-height error was not bounded at a useful numerical precision, nor was the beta-model cross or the high-to-high block. In particular, the **upper** endpoint of $m_H$ is not an upper bound on $\|B_{\rm arith}\|^2$. The band can at most furnish a lower bound for that squared norm. This remains a limited validation of one feasible component of the full certificate.
