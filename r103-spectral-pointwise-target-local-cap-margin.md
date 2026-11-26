# A target-local denominator margin for the pointwise exceptional parity difference

**Scope.** This sharpens the original-cap margin in the [pointwise result with an odd conductor overlap](r102-spectral-sharp-hard-transfer-odd-overlap.md). On targets with suitably small nonconductor prime support, a fixed power of the ambient logarithm in the ratio of the original cap to the actual Page conductor suffices. The conclusion concerns the two actual exceptional corrections only, at an individual target, conditional on the stated zero. It is not a no-margin result, an assertion that such a zero exists, a sign for either entire mixed-strip parity, or a result on Hypothesis S.

Keep the precise original notation: $Y\le N\le2Y$ even, $G=\log Y$, $L=\log N$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$ for the fixed admissible cutoffs $B>B_0>0$. The true test is a bounded nonnegative weight $\omega$ of bounded pointwise variation on a real half-open $I\subset(N/2,9N/16]$, with $\int_I\omega\ge c_{\rm test}Y$ for fixed $c_{\rm test}>0$. The primitive real Page character $\chi$ has conductor $r\le Q_0$ and a simple real zero $\beta$ in the original Page range. Impose $(1-\beta)G\le C_*\log G$ with fixed $C_*>0$. For $K_z=\prod_{p\le z}p$, assume $K_z\mid N$ and $z_*\le z\le Z$ with $z_*$ sufficiently large and fixed, as in the earlier pointwise theorem. In particular $z=z_*$ is admissible. Use the actual quantities

$$
 \gamma_N=\frac{c_r(N)}{\varphi(r)},\qquad
 \mathcal A(N,r)=\sum_{\substack{p\mid N\\p\nmid r}}p^{1/4-\beta}.
 \tag{1}

$$

Here $c_r$ is the Ramanujan sum. The genuine binary singular series with the conductor primes algebraically supplied is denoted by $\Sigma^{(r)}(N)$ as in the [partial-alignment proof](r101-spectral-pointwise-partial-alignment.md). This sets its local factor at every prime of $r$ to $p/(p-1)$, while retaining the actual $N$ at every other prime. It is a factor in the completed model and does not replace the target.

**Theorem.** There exists a fixed $C$ depending only on the fixed data such that if $(N,r_{\rm odd})>1$, $\gamma_N\ne0$ and

$$
                \log(Q_0/r)\ge C\{\log G+\mathcal A(N,r)\},
 \tag{2}

$$

then for sufficiently large $Y$ the true parity difference of the exceptional corrections satisfies

$$
 -\chi(-1)\operatorname{sgn}(\gamma_N)
       \bigl(\mathfrak E_+(N;I,\omega)-\mathfrak E_-(N;I,\omega)\bigr)
 \gg |\gamma_N|\frac{Y^{2\beta-1}}{G}\,
               \frac{\Sigma^{(r)}(N)}{(\log r)^4}.
 \tag{3}

$$

The subscript $+$ still denotes even squarefree factor count. Here $r_{\rm odd}$ is the odd part of the actual primitive conductor. There is no size requirement on the missing odd part $r_{\rm odd}/(r_{\rm odd},N)$. In particular (2) requires only $Q_0/r\ge G^{C'}$ when $\mathcal A(N,r)\ll\log G$ with a fixed implied constant.

## 1. Take a fixed denominator moment on the actual algebraic coefficients

Let $\mathcal D_i(N)$, $i=0,1$, have their exact definition in the [all-target Ramanujan contraction](r94-spectral-all-target-ramanujan-exception.md). They carry the finite $t\le Q_0/r$, both positive short labels $u,v\le S=Y^{1/10}$ with their literal squarefreeness and coprimalities, the original geometric kernels, and the actual tests of $p\mid N$ at all $p\nmid r$. In particular every short product $h=uv$ and every squarefree $t$ is coprime to $r$. All completions in the proof below are algebraic operations on these coefficients; there is no estimate in progressions with a modulus beyond the original $Q_0$.

For a fixed $h$ write $l_{p,0},l_{p,1}$ for its two local factors according as $p$ is absent from or present in $q$. They are the factors of the [two-pole formula](r92-spectral-aligned-exceptional-two-pole-formula.md), used at $p\nmid r$ only. Perform the full $q\mid t$ sum before taking an absolute value. At each occupied $p\mid t$, the two choices contribute $-l_{p,0}$ and $p l_{p,1}$, times $-1/(p-1)$ from $\mu(t)/\varphi(t)$. Thus its occupied factor is $b_p=(l_{p,0}-p l_{p,1})/(p-1)$; at an unoccupied prime the factor is $l_{p,0}$. With $a_h(t)$ this resulting coefficient, the absolute $\vartheta$-moment is bounded by

$$
       \sum_{\substack{t\ {\rm sf}\\(t,r)=1}} t^\vartheta |a_h(t)|
               \le\prod_{p\nmid r}(|l_{p,0}|+p^\vartheta|b_p|),
                  \qquad \vartheta=\tfrac14 .
 \tag{4}

$$

Use finite Euler expansions and absolute convergence; there is no division by the unoccupied factor, including at small primes.

For completeness put $c_p=\chi(p)p^{-\beta}$ and $E_p=(1-c_p)^{-1}$ on $p\nmid r$. The exact factors after contraction in the [cap completion](r93-spectral-completed-colored-caps.md) are

$$
\begin{array}{c|c|c}
 & l_{p,0}& b_p\\ \hline
 p\nmid h,\ p\nmid N & 1-c_p^2E_p^2&
 E_p^2(-2c_p-1/(p-1))/(p-1)\\
 p\nmid h,\ p\mid N & 1-c_p^2E_p^2&
 E_p^2(2c_p+1/(p-1))\\
 p\mid h,\ p\nmid N & E_p^2 & E_p^2/(p-1)\\
 p\mid h,\ p\mid N & E_p^2 &-E_p^2 .
\end{array}
 \tag{5}

$$

These give generic positive envelopes $1+C(p^{-2\beta}+p^{\vartheta-1-\beta})$ at $p\nmid N$ and $1+C(p^{-2\beta}+p^{\vartheta-\beta})$ at $p\mid N$, independent of $h$. If $p\mid h$ multiply by an extra $1+w_p$, with $w_p=C(p^{-\beta}+p^{\vartheta-1})$ at $p\nmid N$ and $w_p=Cp^\vartheta$ at $p\mid N$. This dominates the last two rows since the generic envelopes are at least one. For large $G$, $\beta\ge .99$, so the outside-$N$ factors in the generic product are uniformly summable, and the inside-$N$ factors cost at most $\exp(O(1+\mathcal A(N,r)))$. There is no $p\mid r$ in either bound.

Sum (4) with $h^{-\beta}=(uv)^{-\beta}$ over the actual two short labels. For a positive bound only, enlarge the extra factor to one copy on each short label and drop their mutual coprimality and squarefreeness, keeping both labels coprime to $r$. The divisor expansion of $\prod_{p\mid u}(1+w_p)$ and the bound

$$
        \sum_{\substack{u\le S\\d\mid u}}u^{-\beta}
                        \le d^{-\beta}\sum_{u\le S}u^{-\beta}

$$

give a factor at most

$$
 \left(\sum_{u\le S}u^{-\beta}\right)^2
        \prod_{p\nmid r}(1+w_p p^{-\beta})^2
 \ll G^2 Y^{(1-\beta)/5}\exp(O(1+\mathcal A(N,r))).
 \tag{6}

$$

Indeed the outside-$N$ increments in this product are $O(p^{-2\beta}+p^{\vartheta-1-\beta})$, and its inside-$N$ increments are $O(p^{\vartheta-\beta})$. Here $\sum_{u\le S}u^{-\beta}\le S^{1-\beta}(1+\log S)$, and the upper bound $Y^{(1-\beta)/5}\le G^{C_*/5}$ uses the specified near zero, not any new zero-free input.

The clipping error from completing $t$ in either $\mathcal D_i$ is therefore at most

$$
         Y^{2\beta-1}G^{C_1}\exp(C_1\mathcal A(N,r))
                           (Q_0/r)^{-1/4}
 \tag{7}

$$

after increasing the fixed $C_1$. This uses the uniform geometric integral bound $O(Y^{2\beta-1}G^{O(1)})$ from the same cap completion, with the unchanged physical test; the prefactor costs $G^{O(1)}$ there as $r/\varphi(r)\ll G^{O(1)}$ and $|1/L'(\beta,\chi)|\ll1$ for the stated Page zero. Estimate (7) is before multiplying by the actual response. Every prime in the short reciprocal sum and in the moment was examined on the $p\nmid r$ side of the contraction.

## 2. Separate the remaining algebraic and genuine errors

After completing $t$, its local factors are $l_{p,0}+b_p$ and are exactly those of the earlier completion. In particular at $p\mid h,p\mid N$ their sum is zero, so the true short-unit mask is restored *after* the completion. The remainder of the algebraic completion of $\mathcal D_i$ is the argument of the partial-alignment proof: the primitive truncation and the geometric transfer of the squarefree short-label sum retain the original $D,H_0,S$ and $N-x\in I$, and cost $O_A(Y^\beta G^{-A})$ for any fixed $A$. Their signed Euler tails use the actual mask independently of the denominator gap. The earlier gap in that proof controlled only the step now bounded by (7). The ensuing exact colored kernels $B_i$ consequently satisfy

$$
 \mathcal D_i(N)
 =-\chi(-1)\int_{N-x\in I}
 \frac{\omega(N-x)(N-x)^{\beta-1}x^{\beta-1}}{\log x}
                     B_i(x)\,dx
   +O_A\!\left(Y^\beta G^{-A}
     +Y^{2\beta-1}G^{C_1}e^{C_1\mathcal A(N,r)}(Q_0/r)^{-1/4}\right).
 \tag{8}

$$

The analytic positivity of the second capped kernel is also unchanged. The proof of the partial-alignment bound on $B_1$ requires the actual zero coefficients and $K_z\mid N$, the specified zero range and fixed cutoffs, but no clipping estimate and no size of the missing odd product. It gives $B_1(x)\gg\Sigma^{(r)}(N)/(\log r)^4$ uniformly on the physical support. Thus the unsigned integral of $B_1$ in (8) is at least a fixed positive constant times

$$
                    \frac{Y^{2\beta-1}\Sigma^{(r)}(N)}{G(\log r)^4}.
 \tag{9}

$$

Here $\Sigma^{(r)}(N)\ge\Sigma(N)\gg1$ for even $N$. This analytic step makes no statement about the sign of the actual correction until the two errors are controlled.

For the genuine arithmetic error, use the sharper hard-transfer formula (2) of the odd-overlap result. With $(N,r_{\rm odd})>1$ the residual rare class is exactly zero, and it yields

$$
     \mathfrak E_\pm
        =\frac{\gamma_N}{2}(\mathcal D_0(N)\pm\mathcal D_1(N))
                         +O(Y^\beta G^{C_2}Q_0^{-1}).
 \tag{10}

$$

No denominator gap was used for this raw estimate. For nonzero $\gamma_N$, the normalized primitive $2$-part has modulus one and the normalized odd factors give
$|\gamma_N|=1/\varphi(r_{\rm odd}/(r_{\rm odd},N))\ge1/r$.
Hence dividing the raw error by the actual response costs at most $Y^\beta G^{C_2}r/Q_0$. In contrast, the error of (8) already lies inside the response. As $Y^{1-\beta}\le G^{C_*}$ and $\log r\ll\sqrt G$, a sufficiently large fixed constant in (2) and a choice $A>C_*+4$ make both relative errors $o$ of (9). For example the logarithm of the factor multiplying $Y^{2\beta-1}$ in (7) is at most $C_1\log G+C_1\mathcal A(N,r)-\tfrac14\log(Q_0/r)$, so (2) makes it at most $-5\log G$. Similarly the raw relative error is at most $Y^{2\beta-1}G^{C_*+C_2}\exp(-\log(Q_0/r))$. Now subtract the two actual parities in (10). Color zero cancels and color one keeps the sign $-\chi(-1)\gamma_N$, proving (3).

## 3. Concrete target-local instances and limitation

If $z$ is fixed sufficiently large and $\operatorname{rad}N\mid\operatorname{rad}(rK_z)$, then $\mathcal A(N,r)=O_z(1)$ irrespective of the size or support of $r$. In particular for a hypothetical eligible zero satisfying $Q_0/r\ge G^{C'}$, the fully aligned integer construction $N=2^k\operatorname{lcm}(r,K_z)\in[Y,2Y]$ has this control: the base is $Y^{o(1)}$, so one can take a nonnegative $k$. At sufficiently large $Y$ the original Page conductor in this range is unbounded and hence has an odd factor; the construction has $\gamma_N=1$ and genuine odd overlap. The construction does not establish that such a zero exists.

More generally if all nonconductor prime divisors of $N$ are at most $(\log G)^4$, then $\mathcal A(N,r)\ll\log G$. Indeed $\beta=1-O(\log G/G)$ makes $p^{1-\beta}$ uniformly bounded in that range, and $\sum_{p\le X}p^{-3/4}\ll X^{1/4}$ even by summing over all integers. Partial alignment, nonzero response and the same actual overlap are permitted here. With a larger fixed threshold exponent one still uses the original cutoff, now with a polynomial-in-$G$ *ratio*. The argument does not remove this finite cap restriction or the need for odd overlap: in the disjoint case the additional actual rare-class error from the odd-overlap result is not bounded relatively to a small $\gamma_N$ by (2).
