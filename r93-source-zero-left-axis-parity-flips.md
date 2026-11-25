# Two individual parity flips on the genuine zero-left-floor axis

Use exactly the true carrier, moving prime floors, and divisor/product tests of the [four actual parity laws](r89-source-four-actual-parity-phases.md). The coordinate $a=0$ means the literal left prime floor $F\ge\sqrt N$, including any equality; the right coordinate $b$ still uses its own original moving floor. We compare individual parity slices, not their signed aggregates. The coefficient statements below are deterministic. Their arithmetic consequences use the existing common mean-square estimate on fixed bounded boxes, with no bound at prescribed exceptional targets and no conclusion about Hypothesis S.

Write $b_0=a_Q(0)$ for the unique positive zero of $Q(b,0)$ furnished by the [unique reversal theorem](r90-source-unique-parity-floor-reversal.md). It lies in $(20-7/4,20)$. At $(0,b_0)$ the four individual phase signs are exactly $\varepsilon_1\varepsilon_2$. For every deterministic $b\ge25$ the four signs at $(0,b)$ are instead $-\varepsilon_1$, already with a fixed strictly positive magnitude bound at $b=25$. In particular the $++$ phase switches from positive to negative and the $-+$ phase switches from negative to positive between the two witnesses. We do not classify additional reversals.

## 1. The exact axis expression

Set $p(b)=-P(b,0)>0$, by the [global ordinary-phase sign](r91-source-monotone-parity-kink-positive-two-parity.md). The actual capped phase satisfies $\Phi(0,b)=0$ on the axis, as in the [Dickman phase theorem](r86-source-dickman-capped-phase-chart.md). Also $Q(0,b)=0$ by the unique reversal theorem, and $P$ is symmetric. Consequently the exact four-phase formula reduces to

$$
  \phi_{\varepsilon_1,\varepsilon_2}(0,b)
       =\frac{\varepsilon_1}{4}
               \bigl(\varepsilon_2 p(b)-Q(b,0)\bigr).
 \tag{1}
$$

At $b_0$ this is $\varepsilon_1\varepsilon_2 p(b_0)/4$. In particular these are strict signs, not a claim of vanishing of an individual slice at the zero of a mixed coefficient.

## 2. An explicit fixed high-floor witness

Use the continuous signed cumulative $A$ on the positive half-line and its primitive $M$ from the Dickman theorem, extending them by zero on negative arguments. Write $v=7/4$ and $v_0=5/4$. In particular $A=1$ on $0<x<v_0$, $A\ge0$ up to $4$, and $A<0$ above $4$. Also $M>0$ on the positive half-line, decreases above $4$, and tends to zero. The exact positive representation is $M=\rho_4*\kappa$, with $\rho_4=4e^{\gamma_{\rm E}}f$, $f$ the scale-four Dickman density and $\kappa$ the survival function of the old prime on $[0,v]$. It has $0\le\kappa\le1$, $\kappa=1$ below $v_0$ on its positive support, and $0<\rho_4\le1$. Thus $M(v)\le v$. The positive and negative masses of $A(x)\,dx$ both equal $M(v)$, by its sign chart and the decay of $M$.

We need only a simple explicit one-sided estimate for $M$. From the Dickman integral and derivative identities, for $t>4$,

$$
 t f(t)=\int_0^4 f(t-y)\,dy\le4f(t-4),
             \qquad -\frac{f'(t)}{f(t)}
                       =\frac{f(t-4)}{t f(t)}\ge\frac14.
$$

Here the inequality uses that $f$ is nonincreasing on its positive support. Integrating the logarithmic derivative shows $f(t+s)\le e^{-s/4}f(t)$ for $s\ge0$. Apply this pointwise inside $M=\rho_4*\kappa$. If $x>4+v$, then every argument $x-u$ with $0\le u\le v$ exceeds $4$, so

$$
                  M(x+s)\le e^{-s/4}M(x)
                         \qquad(x>4+v,\ s\ge0).              \tag{2}
$$

The exact mixed and ordinary formulas of the two reversal theorems at the opposite floor zero are

$$
 \begin{split}
 Q(b,0)&=\int_0^{20}M(b-20+s)A(s)\,ds,\\
 P(b,0)&=\int_0^{20}M(b+20-s)A(s)\,ds .
 \end{split}                                                 \tag{3}
$$

The first follows from (1) of the unique reversal theorem by $s=20-g$; its nonlong boundary term is zero because $M(0)=0$. The second follows from (6) of the ordinary-phase theorem; its boundary term likewise has $M(0)=0$. Neither formula replaces the cutoff $20$ by an infinite integral.

For $b\ge25$, the part $0<s<1$ in the first integral of (3) has $A(s)=1$ and contributes at least $M(b-19)$, since $M$ is decreasing there. The negative support begins at $s>4$, so its absolute contribution is at most $vM(b-16)$ by the negative mass bound. The other contributions are nonnegative. For the second integral of (3), all arguments of $M$ are at least $b$, hence its absolute value is at most $2vM(b)$. Use (2) with $x=b-19\ge6>4+v$ for both upper bounds to get

$$
 \begin{split}
 Q(b,0)&\ge\bigl(1-ve^{-3/4}\bigr)M(b-19)>\tfrac18 M(b-19),\\
 p(b)&\le2v e^{-19/4}M(b-19)<\tfrac7{64} M(b-19).
 \end{split}
$$

Indeed $e^{3/4}>1+3/4+(3/4)^2/2>2$ and $e^{19/4}>e^4>32$. Thus

$$
                    Q(b,0)-p(b)>\tfrac1{64}M(b-19)
                                     \qquad(b\ge25).          \tag{4}
$$

In particular every phase in (1) has sign $-\varepsilon_1$ and magnitude exceeding $M(b-19)/256$ in this deterministic region. At the actual fixed witness $b=25$ one may use $M(6)>5/8$: the delay derivative and the initial constant give $\rho_4(6)=1-\log(3/2)>1/2$, and monotonicity in the positive convolution gives $M(6)\ge \rho_4(6)\int\kappa>5/8$. Hence each of the four high-witness absolute phase values exceeds $5/2048$. The fixed-shift ratio in the unique reversal theorem, together with $p(b)\le2vM(b)$, also gives $Q(b,0)/p(b)\to+\infty$ as a purely deterministic limit; this limit is not used to justify the finite witness.

The two specified phases in (1) are exact negatives of one another along the axis. By continuity they therefore have a common deterministic zero in $(b_0,25)$; the opposite signs at the two endpoints show a reversal for each, without a uniqueness assertion.

## 3. Tests on the same actual even targets

Take a fixed box with $A_0>25$. By continuity of the four phases, choose small fixed disjoint closed right-floor intervals around $b_0$ and $25$, on the true left-floor axis, such that all four signs just established are strict throughout their respective intervals. Their absolute phases have a common positive lower bound on this finite union. This is a fixed full-model comparison of the individual parity phases, including the ordinary term $P$, not an asymptotic comparison of magnitudes of two individual exact arithmetic sums at growing floors.

The common maximal estimate of the four-parity law gives a single $O(X\ell^{-1/20})$ even exceptional set on each fixed interior target subwindow. Outside it all four actual parity sums have their respective signs and magnitudes $\gg X$, simultaneously on both fixed intervals and for every allowed true split. The sign version on the entire target window holds off $O(X\ell^{-1/60})$ even targets by the same positive-overlap trimming. In particular the two opposite directions of the specified $++$ and $-+$ flips can be witnessed at the **same** even target and at the same split, or with independently chosen allowed splits. We do not assert that either arithmetic step function has an exact zero or that the two arithmetic changes occur at the same right-floor value.
