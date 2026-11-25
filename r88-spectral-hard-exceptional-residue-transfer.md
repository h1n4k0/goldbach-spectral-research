# The exceptional residue can use the literal hard central cutoff

**Scope.** The [all-scale exception formula](r87-spectral-all-scale-exceptional-left-reduction.md) retained one actual exceptional-character correlation, with a band-limited left test and right variables on the whole physical support. Here that correction can be replaced, to arbitrary inverse-logarithmic precision, by a discrete sum on the **original hard left interval**, with the **actual** bounded-variation weight and signed mixed coefficient. The transfer is unconditional and uniform even before any planted-family exceptions are discarded. It does not bound the resulting hard correlation on ultra-close exceptional scales, establish the uncorrected all-scale law, or imply Hypothesis S.

Use $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $\Delta_0=2Q_0/Y$, and $e(t)=e^{2\pi it}$ as in the exception formula. Let $Y\le N\le2Y$ be even, $V=[N/3,2N]$, and $M_\pm(m)$ the exact two true squarefree parities of the above-BV mixed coefficient, with zero outside $V$. The notation $+$ means an even number of distinct prime factors, not numerical evenness of $m$. Keep the literal half-open $I\subset(N/2,9N/16\,N]$ and $\omega$ of uniformly bounded supremum and pointwise variation on $I$. If an exceptional primitive real character $\chi^*$ of conductor $r\le Q_0$ with real zero $\beta>1-4a_0/\sqrt G$ is present, define the compactly supported function

$$
   F(u)=
   \begin{cases}
    \omega(u)u^{\beta-1},&u\in I,\\
    0,&u\notin I.
   \end{cases}
$$

Use its actual representative at integer arguments, with the designated hard endpoints. For integer $n$ put

$$
 \mathcal C_{r,Q_0}(n)=
     \sum_{\substack{t\le Q_0/r\\(t,r)=1}}
                              \frac{\mu(t)c_t(n)}{\varphi(t)}.
$$

Here $c_t(n)=\sum_{a\bmod t,(a,t)=1}e(na/t)$ is the ordinary Ramanujan sum. Define the hard correction

$$
 \mathfrak H_\pm=
   -\frac r{\varphi(r)}\sum_{n\in I\cap\mathbb Z}
        \omega(n)n^{\beta-1}\chi^*(n)
                   \mathcal C_{r,Q_0}(n)M_\pm(N-n).
 \tag{1}
$$

If no zero is present, take both this correction and the preceding $\mathfrak E_\pm$ equal to zero.

**Theorem.** Uniformly on every sufficiently large dyad, in all its even $N$, both signs and all the indicated tests, in the presence of the zero one has

$$
       \mathfrak E_\pm=\mathfrak H_\pm+
                 O\!\left(Y^\beta Q_0^{-1/2}G^C\right)
 \tag{2}
$$

with a fixed $C$. In particular the error is $O_A(YG^{-A})$ for every fixed $A>0$. Thus in the [corrected full and original-major formula, (3)](r87-spectral-all-scale-exceptional-left-reduction.md), $\mathfrak H_\pm$ may replace $\mathfrak E_\pm$ with the same planted-family exception counts and the same Dickman base. The smoothing and the contribution from all integer $n$ outside the hard central interval have both been removed from the retained term.

## 1. A BV sampling estimate with the true point values

Let $W(x)=\int_{-\Delta_0}^{\Delta_0}V_\beta(\eta)e(-\eta x)d\eta$, with $V_\beta(\eta)=\int F(u)e(\eta u)du$ as in the exception formula. This is the Fourier projection of $F$ to the real frequency interval $[-\Delta_0,\Delta_0]$. Both the supremum norm and the total pointwise variation of $F$ are $O(Y^{\beta-1})$. Indeed $u\asymp Y$ throughout $I$, $u^{\beta-1}$ is monotone there and comparable to $Y^{\beta-1}$ uniformly for the allowed $\beta$, and the two endpoints of the zero extension cost at most twice the supremum. This estimate also covers a weight with jumps at integer points.

In the convention above, integration by parts for a compactly supported BV function gives $|V_\beta(\eta)|\ll Y^{\beta-1}/|\eta|$ for $\eta\ne0$. By real-line Plancherel and the same bound for the derivative of the band projection,

$$
 \|W-F\|_{L^2(\mathbb R)}
      \ll Y^{\beta-1}\Delta_0^{-1/2},\qquad
 \|W'\|_{L^2(\mathbb R)}
      \ll Y^{\beta-1}\Delta_0^{1/2}.
 \tag{3}
$$

The latter follows by integrating $4\pi^2|\eta|^2|V_\beta(\eta)|^2$ over the band. The projection has a continuously differentiable representative by its finite-band integral, so its samples are well-defined. The line norm in (3), on its own, would not control the prescribed integer values of an arbitrary BV representative. We compare with unit-cell means to handle them.

For $n\in\mathbb Z$ let $J_n=[n-1/2,n+1/2)$ and write $F_{J_n},W_{J_n}$ for the integrals over this unit cell. Jensen's inequality and disjointness give

$$
 \sum_n|W_{J_n}-F_{J_n}|^2
                      \le \|W-F\|_{L^2(\mathbb R)}^2.
$$

The pointwise discrepancy $|F(n)-F_{J_n}|$ is bounded by the actual pointwise variation of $F$ on $J_n$, including any jump or isolated prescribed value at $n$. These variations sum to at most the global variation: for any finite selection of cells one can concatenate approximating partitions in their natural order. Hence their square-sum is at most the square of the total variation. Finally $|W(n)-W_{J_n}|\le\int_{J_n}|W'(t)|dt$, so the square-sum of these errors is at most $\|W'\|_{L^2(\mathbb R)}^2$. The triangle inequality with (3), using $\Delta_0=2Q_0/Y=o(1)$, proves

$$
        \big\|(W(n)-F(n))_{n\in\mathbb Z}\big\|_{\ell^2}
                 \ll Y^{\beta-1/2}Q_0^{-1/2}.
 \tag{4}
$$

In particular there is no replacement of the hard endpoints by a Lebesgue-a.e. convention in the final integer sum.

## 2. Uniform weight for the actual right sequence

For $n\ne0$, dropping the cutoff and coprimality only in the bound on absolute local factors yields

$$
 \begin{split}
 |\mathcal C_{r,Q_0}(n)|
   &\le \prod_{p\mid n}(1+1)
                 \prod_{\substack{p\le Q_0\\p\nmid n}}
                              \left(1+\frac1{p-1}\right)\\
   &\ll \tau(|n|)\log(2Q_0).
 \end{split}
 \tag{5}
$$

Indeed only squarefree $t$ contribute, and $|c_p(n)|/\varphi(p)$ is one when $p\mid n$ and $1/(p-1)$ otherwise. The second product is bounded by the ordinary prime Mertens product, and $2^{\omega(|n|)}\le\tau(|n|)$. For $n=0$, the true color $\chi^*(0)=0$ applies since this is a nonprincipal exceptional conductor. Thus no bound in (5) is needed there.

The exact right coefficient obeys $|M_\pm(m)|\le\tau_4(m)$ on its squarefree support: each of the admissible ordered four-factor tuples has weight of magnitude at most one. Here $\tau_4$ is the ordered four-divisor function. In the range $m\in V$ the integer $n=N-m$ satisfies $|n|\ll Y$. The shifted divisor-weight bound, by Cauchy–Schwarz, is

$$
 \begin{split}
 \sum_{\substack{m\in V\cap\mathbb Z\\ m\ {\rm sf},\,m\ne N}}
        \tau_4(m)^2\tau(|N-m|)^2
 &\le
 \left(\sum_{\substack{m\le4Y\\m\ {\rm sf}}}\tau_4(m)^4\right)^{1/2}
 \left(2\sum_{1\le k\le4Y}\tau(k)^4\right)^{1/2}\\
 &\ll YG^C .
 \end{split}
 \tag{6}
$$

For the first sum $\tau_4^4=\tau_{256}$ on squarefree $m$, and for the second $\tau^4\le\tau_{16}$. The latter follows prime by prime: four exponents between $0$ and $k$ are the four marginals of a nonnegative composition of $k$ into $16$ parts indexed by four bits, by taking $k$ columns of four bits with the specified row sums. The elementary divisor moment estimate $\sum_{n\le X}\tau_j(n)\ll_j X(1+\log X)^{j-1}$ follows by summing over the first $j-1$ factors and using harmonic sums. This proves (6) without assuming independence of the shifted divisor quantities. Combining with (5) gives

$$
 \big\|\big(M_\pm(N-n)\chi^*(n)\mathcal C_{r,Q_0}(n)\big)_{n\in\mathbb Z}
       \big\|_{\ell^2}\ll Y^{1/2}G^C .
 \tag{7}
$$

Now apply Cauchy–Schwarz to (4) and (7) in the [exact discrete exception formula, (9)](r87-spectral-all-scale-exceptional-left-reduction.md#3-an-exact-discrete-form-of-the-residual). The factor $r/\varphi(r)\ll\log(2r)\ll G$ is harmless. This proves (2). Since $\beta<1$ and $\log Q_0=16\sqrt G/\log G$ exceeds every constant multiple of $\log G$ eventually, the error in (2) has the stated arbitrary log saving. Fourier inversion in the preceding all-scale formula is unchanged; only the representation of its one retained correction changes.

For reference, the Ramanujan weight in (1) also has the exact finite divisor form

$$
 \mathcal C_{r,Q_0}(n)=
  \sum_{\substack{d\mid n,\ d\le Q_0/r\\(d,r)=1}}
       \frac{\mu(d)d}{\varphi(d)}
       \sum_{\substack{k\le Q_0/(rd)\\(k,rd)=1}}
                                    \frac{\mu(k)^2}{\varphi(k)} ,
             \qquad n\ne0 .
 \tag{8}
$$

To obtain it, expand $c_t(n)=\sum_{d\mid(t,n)}d\,\mu(t/d)$, which follows by inclusion–exclusion in the reduced residues. On the squarefree support of $t$, put $t=dk$, so $\mu(t)\mu(t/d)=\mu(d)\mu(k)^2$ and $\varphi(t)=\varphi(d)\varphi(k)$; conversely the summation conditions in (8) impose exactly that support. Thus the unresolved ultra-close term is a true signed central correlation with a real primitive color and a finite arithmetic divisor weight. Neither the color nor the weight has been treated as random, and no new cancellation of (1) is asserted.
