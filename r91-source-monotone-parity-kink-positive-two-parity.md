# The exact monotone parity reversal and the positive two-parity contrast

Use the unchanged signed carrier, genuine cofactor parities and scales of the [four actual parity laws](r89-source-four-actual-parity-phases.md). This note evaluates two consequences of their deterministic phases. Its arithmetic conclusions use the same unconditional mean-square and exceptional-set estimates on fixed bounded parameter boxes, not a pointwise statement at prescribed moduli or a statement about Hypothesis S.

Write $P(a,b)$ and $Q(a,b)$ for the ordinary and mixed scalars of that law, respectively. The [unique floor reversal](r90-source-unique-parity-floor-reversal.md) gives a continuous root $a_Q(b)>0$ for each $b\ge0$, negative $Q$ at $0<a<a_Q(b)$, positive $Q$ above it, and

$$
           \min(20,b+20-v)<a_Q(b)<20+v,\qquad v=7/4.
$$

There is one $b_*\in(0,v)$ with $a_Q(b_*)=20$, and $\lim_{b\to\infty}a_Q(b)=20+v$. Below we show:

1. $a_Q$ is **strictly increasing for all $b\ge0$**, and $C^1$ with strictly positive derivative on the branches off $b_*$, with a positive right derivative at $b=0$. At the actual seam $b_*$ both one-sided derivatives are strictly positive and the right derivative is strictly smaller.
2. **$P(a,b)<0$ for every $a,b\ge0$.** Thus on almost all targets the actual signed same-parity sum strictly exceeds the actual signed opposite-parity sum, simultaneously across each fixed box of target-adaptive floors and all true splits. This compares the two sums, not the signs of their individual constituents.

## 1. Negative transverse derivative at every true mixed root

Let $A$ be the signed cumulative and $M(x)=\int_0^{x_+}A(t)\,dt$ of the [Dickman phase theorem](r86-source-dickman-capped-phase-chart.md), with $A(x)=0$ for $x<0$. Recall $M>0$ on $(0,\infty)$, $M'=A$ there, and $M=0$ on the negative half-line. Its right slope at zero is $1$, its left slope is $0$. The signs of $A$ are strictly positive on $(0,v)$, zero on $[v,4]$, and strictly negative on $(4,\infty)$. As proved in the unique reversal theorem, the log slope $m'(x)=(\log M)'(x)$ is nonincreasing on $(0,\infty)$ and strictly decreasing on $(4,\infty)$.

The formula for $Q$ in (7) of the actual parity law, with the change $s=a-g$, gives

$$
 \begin{split}
 Q(a,b)&=\int M(b+20-a+s)\,d\Xi_a(s),\\
 d\Xi_a(s)&=M(a)\,d\delta_a(s)
          -\mathbf1_{[(a-20)_+,a]}(s)A(s)\,ds .
 \end{split}                                                    \tag{1}
$$

Indeed the atom produces $M(a)M(b+20)$, and $A=0$ on the negative half-line clips the integral at $(a-20)_+$. The signs in (1) differ from the orientation used for the $a$ derivative; they are needed for the transverse derivative in $b$.

At a positive root, $a>20-v>v$ and $(a-20)_+<v$ by the previously proved root brackets. The measure in (1) is negative only below $v$ and positive only above $v$, with a strictly positive atom at $s=a$. All arguments $b+20-a+s$ in (1) are positive near a root: their minimum is $b+(20-a)_+$, and when $b=0$ the root has $a_Q(0)<20$. The benchmark argument $b+20-a+v$ is positive by $a<20+v$. Differentiation in $b$ and subtraction of this benchmark log slope, justified by $Q(a,b)=0$, yield at the root

$$
 Q_b(a,b)=\int
   \big\{m'(b+20-a+s)-m'(b+20-a+v)\big\}
            M(b+20-a+s)\,d\Xi_a(s)<0 .                          \tag{2}
$$

Indeed the expression in braces is nonnegative below $v$ and nonpositive above $v$, making both signed contributions nonpositive. At the positive atom the argument is $b+20>4$ and strictly larger than the benchmark, so the log slope is strictly smaller. If the benchmark is at or below $4$, combine ordinary monotonicity below $4$ with the strict inequality on $(4,b+20)$. The atom gives the strict sign in every case.

## 2. Smooth branches and the exact kink

For the $a$ derivative retain the other orientation

$$
 Q(a,b)=M(a-20)M(b)+\int_0^{20}M(a-g)A(b+20-g)\,dg.              \tag{3}
$$

The continuous part has partial derivative in $a$ equal to $\int_0^{20}A(a-g)A(b+20-g)\,dg$. At the single integration point $g=a$ either representative of $A(0)$ is harmless; local Lipschitz bounds for $M$ justify differentiation under the integral and dominance. This partial derivative is jointly continuous, including at the seam, by the continuity of $A$ except at zero and bounded convergence on compact sets. For the $b$ derivative one may equivalently use the fixed $g$ domain before the change in (1):

$$
 Q_b(a,b)=M(a)A(b+20)-\int_0^{20}A(a-g)A(b+20-g)\,dg.
 \tag{4}
$$

This is jointly continuous locally at every root, including the seam. Both (3) and (4) allow ordinary differentiability off $a=20$. At $b=0$ near its root $a<20$, these formulas also give a local $C^1$ extension through $b=0$, since the arguments $b+20-g$ on the effective support $g<a$ stay positive. The atom $M(a-20)M(b)$ is identically zero in that neighborhood.

The unique reversal theorem gives $Q_a>0$ at every root not on the seam. Formula (2) and the implicit function theorem now give $a_Q'(b)=-Q_b/Q_a>0$ on both branches, with the indicated right derivative at zero. Together with continuity and the known location on either side of $b_*$ this proves global strict monotonicity.

Set $D=-Q_b(20,b_*)>0$ and $L_*=\partial_a^-Q(20,b_*)>0$. By (3) the right $a$ derivative at the seam is $L_*+M(b_*)$; only the actual nonlong residue contributes to the jump. For the curve derivative as $b\to b_*^\pm$, write

$$
 0=\{Q(a_Q(b),b)-Q(20,b)\}+\{Q(20,b)-Q(20,b_*)\}.
$$

Apply the one-variable mean value theorem to the first difference in $a$. Its intermediate point stays on the same branch as $a_Q(b)$, so its partial derivative tends to the corresponding positive one-sided value by the continuity just proved. The second difference divided by $b-b_*$ tends to $Q_b(20,b_*)$. Consequently

$$
    a_Q'(b_*-)={D\over L_*}>
    {D\over L_*+M(b_*)}=a_Q'(b_*+)>0 .                          \tag{5}
$$

Here $M(b_*)>0$ since $b_*>0$. Thus the loss of slope follows from the actual residue, not an arbitrary convention at the floor.

In particular the curve increases from $a_Q(0)$ to $20+v$, not attaining the latter. Equivalently, for fixed $a\in(a_Q(0),20+v)$ there is a unique $b$ reversal: $Q(a,b)$ is positive below it and negative above it. For $0<a<a_Q(0)$ it is always negative, and for $a\ge20+v$ it is always positive; at $a=a_Q(0)$ only $b=0$ is a zero. The axis $a=0$ remains a zero axis for this mixed phase.

## 3. The global sign of the ordinary contrast

The ordinary region in the proof of the four-parity law is the triangle cut by the two long bounds:

$$
 s,t\ge0,\qquad s\le a+20,\qquad t\le b+20,\qquad
                       s+t\le a+b+20.
$$

After integrating the two short Euler measures it has integrand $A(s)A(t)$. Integrating first in $s$ and splitting at $t=b$ gives the exact relation

$$
 P(a,b)=M(a+20)M(b)+\int_0^{20}M(a+20-g)A(b+g)\,dg.             \tag{6}
$$

Indeed the full bound $s\le a+20$ applies for $t\le b$, and the upper bound for $t=b+g>b$ is $a+20-g$. This derivation keeps the two individual long bounds rather than replacing the region by the uncapped triangle. It also shows symmetry $P(a,b)=P(b,a)$.

At fixed $b$ write (6) as an integral against the signed measure $M(b)\delta_0+\mathbf1_{[0,20]}(g)A(b+g)\,dg$. Its positive part lies at or to the left of $g_0=(v-b)_+$ and its negative part lies to the right. At any root with $a>0$, all arguments $a+20-g$ are positive. Differentiate (6) in $a$ and center the log slope by $m'(a+20-g_0)$, which does not change the derivative at the root. The centered slope is nonpositive for $g\le g_0$ and nonnegative for $g\ge g_0$, giving only nonpositive contributions. There is strict negativity from $5<g<6$, where $A(b+g)<0$ and $a+20-g>4$, and where the argument is strictly below the benchmark (also above $4$). Thus every strictly positive $a$ root would be an isolated **downward** crossing.

Now $P(0,0)=\Psi(20)<0$ by the original parity and Dickman phase laws. First take $b=0$. Starting at a negative value, continuity precludes any positive $a$ zero: the first such zero would need nonpositive values immediately to its left, which is impossible for a downward crossing. Hence $P(a,0)<0$ everywhere. Symmetry gives $P(0,b)<0$ for every $b$. Apply the same argument with any fixed $b$ to obtain the asserted strict negativity on the whole plane.

## 4. The actual parity aggregates

Let $S_{N,Z}^{a,b}$ denote the sum of the two genuine same-parity slices and $O_{N,Z}^{a,b}$ the sum of the two opposite-parity slices, with their original signs. The exact four coefficient identities give

$$
 S_{N,Z}^{a,b}-O_{N,Z}^{a,b}
  =-P(a,b)\,\Sigma(N)B_{\mathcal J}(N)
              \left({\mathcal C_{X,Z}\over|\mathcal J|}\right)^2
       +\text{the summed four-parity error}.
$$

The summed error keeps the common maximal squared norm $O(X^3\ell^{-1/20})$, by the triangle inequality over four terms. On each fixed box $[0,A_0]^2$, the continuous function $-P$ has a strictly positive minimum. Thus $S>O$ simultaneously for all allowed target-adaptive floor pairs and splits on an interior target window off $O(X\ell^{-1/20})$ even targets, with the positive difference $\gg X$ there. Over the whole target window the strict inequality holds off $O(X\ell^{-1/60})$ targets by the same overlap-strip argument as in the four-parity law. The constants may depend on the fixed box and carrier. The right-parity contrast has the signs opposite to $Q$ on compact sign-separated subsets, now with the globally monotone reversal and exact slope kink above; the left contrast is its reflection. No concentration rate for growing boxes, pointwise sign at a specified target, or separate signs for the two same-parity terms is asserted.
