# Separate actual row dominance on the zero-left-floor axis

Keep exactly the carrier, signs, hard common physical interval and positive unconditioned normalization of the [four actual parity laws](r89-source-four-actual-parity-phases.md). Fix $a=0$ and allow $0\le b\le A_0$ for any fixed finite $A_0$, all true splits $Z$, and both true cofactor parities $\boldsymbol\varepsilon=(\varepsilon_1,\varepsilon_2)$. In particular the left distinguished prime satisfies $F\ge\sqrt N$ literally, including equality, and the right prime satisfies its own original floor $G\ge\sqrt N e^{-bT_N}$. The cutoffs are the actual integers $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$ and $Q_N=\lfloor Ne^{-20T_N}\rfloor$, where $T_N=\log N/\log\log N$, not their fixed-scale log models. The conclusions are unconditional mean-square and density conclusions, not fixed-target assertions, and do not cover growing floor boxes or Hypothesis S.

Let $O_{N,Z}^{b;\boldsymbol\varepsilon}$ be the genuine ordinary–ordinary row of the original parity slice, and $C_{N,Z}^{b;\boldsymbol\varepsilon}$ the genuine left-ordinary/right-containing row. Both include the original external minus and are defined precisely below. Write, with the original notation,

$$
 \mathcal N_{N,Z}=\Sigma(N)B_{\mathcal J}(N)
                    \left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2,
 \qquad
 o_{\boldsymbol\varepsilon}(b)=-\tfrac14\varepsilon_1\varepsilon_2P(0,b),
 \qquad
 c_{\boldsymbol\varepsilon}(b)=-\tfrac14\varepsilon_1 Q(b,0).
 \tag{1}
$$

For an even $N$ let $E_{N,Z}^{b;\boldsymbol\varepsilon}$ be the maximum of the two absolute errors of $O,C$ from $\mathcal N_{N,Z} o_{\boldsymbol\varepsilon}(b),\mathcal N_{N,Z}c_{\boldsymbol\varepsilon}(b)$, respectively.

**Theorem.** On this exact axis the original parity slice is $O+C$, with no third row. The separate actual rows satisfy

$$
 \sum_{\substack{N\in\mathcal X\\ 2\mid N}}
       \sup_{\substack{0\le b\le A_0,\ Z_0\le Z\le X^{\delta_0}\\
                        \boldsymbol\varepsilon\in\{-1,1\}^2}}
          \bigl(E_{N,Z}^{b;\boldsymbol\varepsilon}\bigr)^2
                 \ll X^3\ell^{-1/15}.                    \tag{2}
$$

For any one fixed common $b$ (uniform in that $b$, also if chosen at scale $X$), the same estimate with only $Z,\boldsymbol\varepsilon$ maximized has the sharper bound $O(X^3\ell^{-1/10})$.

In particular, if $A_0>25$, there are two disjoint fixed closed right-floor intervals with nonempty interiors around $b_0=a_Q(0)$ and $25$, respectively. For the same targets, all true splits and all four parity choices, the actual magnitude $|O|$ exceeds $|C|$ by $\gg X$ on the first interval and $|C|$ exceeds $|O|$ by $\gg X$ on the second, on each fixed interior target subwindow outside one $O(X\ell^{-1/15})$ even exceptional set. The dominating actual row has sign $\varepsilon_1\varepsilon_2$ on the first interval and sign $-\varepsilon_1$ on the second. The strict order and signs hold throughout the full target window outside $O(X\ell^{-1/45})$ even targets, with the usual smaller boundary magnitude. These are comparisons of the *two actual arithmetic rows*, not just of their deterministic models.

## 1. Literal cancellation and the surviving true rows

For each actual ordered pair $n=hF,m=kG$ on the exact carrier and the two chosen parities, the marks of ordinary divisors $d=h/r$ and $e=k/t$ are
$u_h(r)=\mu(h)\mu(r)\log(Fr)$ and $u_k(t)=\mu(k)\mu(t)\log(Gt)$. The mark of a containing divisor $Fz$ is $-v_h(z)$, with $v_h(z)=\mu(z)\log(h/z)$, and correspondingly $-v_k(w)$ for $Gw$. The divisor variables here range over the corresponding actual cofactors.

For each fixed admissible right long divisor $e$, every $Fz$ is long and passes the curved test:

$$
 Fz\ge\sqrt N>D_N,\qquad
          Fze\ge \sqrt N\, e>N e^{-20T_N}\ge Q_N.
$$

Indeed $e\ge D_N+1>\sqrt N e^{-20T_N}$. Since the actual squarefree $h=sWU$ is composite, their full mark sums to $-\Lambda(h)=0$. The parity mask is independent of $z$. This is the [literal giant cancellation](r88-source-giant-parity-resolved-signs.md) on the left arm alone, valid for each right long divisor of either type, before any enlarged prime or unit comparison. It proves that all original left-containing contributions vanish, with no change to the right floor.

Accordingly $O$ is the sum over the actual pairs of

$$
     -\sum_{\substack{r\mid h,\ t\mid k\\
                  h/r>D_N,\ k/t>D_N,\ (h/r)(k/t)>Q_N}}
                       u_h(r)u_k(t).
 \tag{3}
$$

The row $C$ is the sum over the same pairs of

$$
 -\sum_{\substack{r\mid h\\ d=h/r>D_N}}u_h(r)
        \left\{\sum_{\substack{w\mid k\\Gw\le D_N}} v_k(w)
              +\sum_{\substack{w\mid k\\Gw>D_N,\ dGw\le Q_N}}v_k(w)\right\}.
 \tag{4}
$$

Indeed the original right containing row has the product of the external minus and the original right mark $-v_k(w)$; its accepted sum of $v_k(w)$'s is the negative of the two excluded sums because the complete containing orbit is zero. The two sums in braces are disjoint and use literal weak or strict tests as displayed, including at either equality. This is the containing-right specialization of the [capped long-floor algebra](r85-source-capped-long-floor-orbits.md). The identity $R=O+C$ now holds termwise in the genuine pair sum. In particular $C$ is not defined by subtracting two separately estimated full parity sums.

## 2. The separate fixed-node laws

We detail why the fixed-common-parameter proof of the four-parity law applies separately to (3) and (4), not only to their sum. On their actual active supports the old global cofactor windows
$[\,\tfrac12\sqrt X e^{-20T},\,\tfrac12(1+\Delta)\sqrt X e^{A_0T}\,]$
and common short-label cap $M_{\rm lab}=\exp((24+2A_0)T)<Z_0$ still apply to either arm. For an ordinary label this follows from its long test; for a short containing label it follows either from $Gw\le D_N$ or the genuine forbidden product with a long mate, which forces $Gw<Q_N/(\sqrt N e^{-20T_N})\le\sqrt N$. In particular the cofactor and label support bounds of the four-parity law do not need a positive value of $a$ here. No left-containing term is added back on the fixed external prime windows. The original floor slivers and unit replacements in its §1 cost the same positive norm on each row separately.

On a fixed $b,Z,\boldsymbol\varepsilon$, its §2 bounds each positive or short-sign label-bin arm in fourth norm by $O(X^{3/4}\ell^{-1})$, and the same arm with a full cofactor Möbius sign by $O(X^{3/4}\ell^{-1-1/10})$. This includes a short **containing** label with a full sign, with the genuine $Gw$ integer comparison. In (3) the original parity projectors on both ordinary signs use $\mu(h)\mathbf1_{\mu(h)=\varepsilon_1}=(\mu(h)+\varepsilon_1)/2$ and the right analogue; in (4) only the left arm uses that identity, and the right containing arm uses $(1+\varepsilon_2\mu(k))/2$. Thus the no-full-sign bits have prefactors $-\varepsilon_1\varepsilon_2/4$ for (3) and $-\varepsilon_1/4$ for either subrow of (4).

There are $O(\ell^2)$ hard bin pairs per subrow and $O(\ell)$ near its moving boundary lines. The latter are estimated positively at $O(X^{3/2}\ell^{-1})$ in target norm, keeping the exact inequalities inside those comparisons. Every full-sign bit in the accepted pairs has norm $O(X^{3/2}\ell^{-1/10})$ after summing the bin-pair bounds by Hölder and Parseval. Neither bound combines opposite rows before taking norms. In §§3–4 of the same proof the accepted no-full-sign bits have the shared bin scalars (6), and the rational and signed Euler completions are done on each fixed real region. In (3) its area is $P_{0,b}$; in (4) its two areas are the reflected nonlong rectangle and retained-long forbidden wedge, whose *sum* is $Q_{b,0}$. Their real limit with the same $\mathcal C_{X,Z}$ gives $P(0,b)$ and $Q(b,0)$ without mixing rows. The remaining bin/completion and signed Euler errors are $O(X^{3/2}\ell^{-1/10})$ in the same norm, using $B_{\mathcal J}\ll X$ and $\|\Sigma\|_2\ll\sqrt X$. Thus for every one common $b,Z,\boldsymbol\varepsilon$,

$$
       \sum_{\substack{N\in\mathcal X\\2\mid N}}
           (E_{N,Z}^{b;\boldsymbol\varepsilon})^2
                    \ll X^3\ell^{-1/5}.
 \tag{5}
$$

This proof preserves the two signed arrays separately; it proves the same size of error for the no-full-sign model of each of them.

## 3. Two-axis joint maximum with actual parameters

Vary the true right floor and the split, holding the literal left floor fixed. In the exact row formulas (3)–(4) the divisor tests, arithmetic labels and marks do not change on a pair retained at two choices of parameters. The distinguished-prime representation is unique uniformly on the global windows, as proved in the four-parity law, and hence the actual cofactor parity is also unchanged. The cutoff $M_{\rm lab}<Z_0$ makes every short label independent of the split decomposition. Consequently the same positive all-label envelopes used in §4 of the four-parity law and §5 of the capped theorem apply **to each row change**, with no reliance on cancellation across rows or across parities. More precisely these are pointwise nonnegative majorants independent of the unspecified coordinate, not just a collection of uniform norm bounds. On a floor gap enlarge the eligible splits to their common $Z_0$ carrier and keep the fixed enclosing prime slab on the changed side. On a split gap take the fixed global prime window on both arms and a full $Z_0$ envelope on the unchanged side. If a pair is lost through either arm, add the two respective positive convolutions. These enlargements are valid because the true total tag event is split invariant, $W_Z$ grows with $Z$, and its size cap on these active windows already ensures $U_Z>1$ when that gate passes. The nonnegatively labeled comparisons therefore dominate the exact differences even when both parameters vary at the target.

For clarity, a gap of width $d$ in $b$ restricts the true affected prime to the enclosing log slab of width $dT+O(1)$, uniformly in $N$. The positive prime-slab estimate and the full opposite arm yield a target norm $O(X^{3/2}(d+\ell/L))$ for this gap, uniform in the other coordinate. For a split gap use the [marked fixed-axis estimate](r83-source-full-polynomial-adaptive-split.md), which requires an actual gap prime and failure of an upper $W$-gate. Put $\tau=\log Z/L$, and use its original start

$$
       \tau_*=(\epsilon/16)\frac{\log\log\ell}{\log\ell}.
$$

Above $\tau_*$, any exponent gap of length $d$ with endpoint ratio at most two has target envelope norm $O_H(X^{3/2}(d+L^{-H}))$. The same proof bounds the zero-frequency calibration by $O_H(X(d+L^{-H}))$, giving normalization change $O(X(d+\ell^{-1}))$ from a bracket node. From $Z_0$ to $X^{\tau_*}$, the [initial subpower comparison](r82-source-target-adaptive-subpower-split.md) gives target envelope $O(X^{3/2}\ell^{-1/10})$ and normalization change $O(X\ell^{-1/10})$. These are the positive tilted-window bounds of those proofs and the global-window comparison already used in the capped law. The normalization is unconditioned and independent of the two floors; one may use the same auxiliary one-arm calibration at a fixed positive reference exponent, not a nonexistent interior exponent below $a=0$. Neither the marked estimate nor the calibration changes the true split gates.

Mesh the $b$ axis with intervals of length at most $\eta=\ell^{-1/15}$ and the split exponent linearly with those spacings above $\tau_*$, retaining the single initial gap between the true lower split and $\tau_*$. Since $\eta=o(\tau_*)$, all ordinary split gaps meet the endpoint-ratio condition. For each target, bracket its chosen $b,Z$ below and move one axis at a time. The envelopes are uniform in the other coordinate; for each axis the squared maximum over its gaps is at most the sum of the squared one-axis envelopes, with **no** product number of gaps. The total of these squared gap norms is $O(X^3\eta)$, since $\sum d^2=O(\eta)$ on each axis and the initial gap's squared budget $O(X^3\ell^{-1/5})$ is smaller. The phases in (1) are Lipschitz on the fixed interval, from the compact kernels of the four-parity law, and the exact calibration just stated gives comparator change $O(X\eta|\Sigma(N)|)$ relative to the bracket node, hence squared norm $O(X^3\eta^2)$ even after the pointwise supremum.

There are $O(\eta^{-2})$ joint nodes. Estimate (5) on each node, and take the finite maximum over four parities and two rows by summing their squared bounds. The total node cost is $O(X^3\eta^{-2}\ell^{-1/5})=O(X^3\eta)$. This proves (2). With a single fixed $b$ no floor mesh is used, and the split mesh spacing $\ell^{-1/10}=o(\tau_*)$ balances the one-axis node cost and its gap cost, proving the claimed sharper rate. There is no differentiability or regularity requirement on the independently chosen actual floors or splits.

## 4. Genuine dominance at the two witnesses

The [axis phase witnesses](r93-source-zero-left-axis-parity-flips.md) give $Q(b_0,0)=0$, $p(b_0)=-P(0,b_0)>0$, and $Q(25,0)-p(25)>5/512$, where $p(b)=-P(0,b)>0$. Equivalently, in (1) the magnitude gap in favor of the ordinary row is $p(b_0)/4>0$ at $b_0$, and the magnitude gap in favor of the containing row exceeds $5/2048$ at $25$. The latter uses the stated strict bound $M(6)>5/8$. The winning model signs are respectively $\varepsilon_1\varepsilon_2$ and $-\varepsilon_1$, for all four choices. Take the two fixed closed intervals small enough for a uniform positive gap and the model signs to persist throughout them.

On a fixed interior target subwindow $\mathcal N_{N,Z}\gg X$ uniformly in true splits. By (2) and Markov, off $O(X\ell^{-1/15})$ even targets both actual row errors are smaller than a sufficiently small fixed fraction of that local scale, simultaneously on the two intervals, all splits and parities. The strict row inequalities and the signs therefore follow for the arithmetic rows themselves. For the full window omit endpoint strips of width $X\ell^{-1/45}$; the remaining overlap is $\gg X\ell^{-1/45}$, so the same Markov calculation costs $O(X\ell^{-1/45})$ in total. If only the two exact fixed witness values are needed, the one-axis bound instead gives $O(X\ell^{-1/10})$ interior or $O(X\ell^{-1/30})$ whole-window exceptional counts by taking the finite union. No exact arithmetic zero of either row or the full parity slice is asserted.
