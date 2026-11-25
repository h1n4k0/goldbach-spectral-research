# The unique floor reversal of the actual one-parity contrast

This evaluates the deterministic mixed phase of the [four actual parity laws](r89-source-four-actual-parity-phases.md), with their true divisor and product cuts, prime floors, and carrier unchanged. It gives an arithmetic sign only in the mean-square and common-exception sense of that theorem on fixed bounded parameter boxes. No pointwise assertion for a prescribed target, sign of all four individual phases, or conclusion about Hypothesis S is implied.

Let $A$ be the signed cumulative of the local Euler measure and $M(x)=\int_0^{x_+}A(t)\,dt$ from the [Dickman phase theorem](r86-source-dickman-capped-phase-chart.md). Extend $A$ by zero to negative arguments. In the notation of the four-parity law, the actual right-cofactor parity contrast
$\sum_{\varepsilon_1,\varepsilon_2}\varepsilon_2 R_{N,Z}^{a,b;[\varepsilon_1,\varepsilon_2]}$
has leading scalar $-Q(a,b)$, with exactly the same unconditioned positive normalization as before. We prove a sign chart for that scalar on the full deterministic nonnegative floor plane.

**Theorem.** Put $v=7/4$. For every $b\ge0$, $Q(0,b)=0$, and there is exactly one positive zero $a=a_Q(b)$. It satisfies

$$
 \min(20,b+20-v)<a_Q(b)<20+v,\qquad
 Q(a,b)<0\quad(0<a<a_Q(b)),\qquad
 Q(a,b)>0\quad(a>a_Q(b)).
$$

Each root off $a=20$ has $\partial_a Q(a_Q(b),b)>0$; at a root on $a=20$ both one-sided derivatives are strictly positive. The curve $a_Q(b)$ is continuous for $b\ge0$. There is exactly one $b_*\in(0,v)$ with $a_Q(b_*)=20$, characterized by

$$
                    \int_0^{20}M(s)A(b_*+s)\,ds=0 .
$$

The curve is below $20$ for $b<b_*$, above $20$ for $b>b_*$, and is strictly increasing on $[0,b_*]$. Its deterministic limit as $b\to\infty$ is $20+v$.

## 1. A strict log-slope fact

We need strictness that is not asserted by the ordinary log-concavity statement alone. The Dickman theorem gives $M=4e^{\gamma_{\rm E}}(f*\kappa)$, with the positive scale-four Dickman density $f$ on $(0,\infty)$, and the old-prime survival function $\kappa$ supported on $[0,v]$ and positive on $(0,v)$. It proves that both factors are log-concave, and the proof of the Dickman log-concavity shows that $-f'/f$ is strictly increasing on $(4,\infty)$. Thus $f$ is strictly log-concave on this interval. In addition, $M$ is positive on $(0,\infty)$, is zero for $x\le0$, and is $C^1$ for $x>0$, since the signed cumulative $A=M'$ is continuous there. In particular the sign chart for $A$ is

$$
 A(x)>0\ (0<x<v),\qquad A(x)=0\ (v\le x\le4),
                \qquad A(x)<0\ (x>4).
$$

Near zero $M(x)=x$ on the positive side, so its right and left slopes at zero are $1$ and $0$, respectively.

Here is a strict version of the convolution argument for this use. Fix $x_2>x_1>4$, $0<\vartheta<1$, and put $F_i(u)=f(x_i-u)\kappa(u)$ for $0<u<v$, $Z_i=\int_0^v F_i$. Each $F_i$ is positive and continuous on this common open interval. The increasing quantile map $J$ from $F_1/Z_1$ to $F_2/Z_2$ is $C^1$ in the interior and satisfies $J'=F_1 Z_2/(F_2(J) Z_1)>0$; it takes both endpoints to themselves in the limiting sense. Let $x_\vartheta=(1-\vartheta)x_1+\vartheta x_2$, $u_\vartheta=(1-\vartheta)u+\vartheta J(u)$. The two log-concavities give

$$
 f(x_\vartheta-u_\vartheta)\kappa(u_\vartheta)
             \ \ge\ F_1(u)^{1-\vartheta}F_2(J(u))^\vartheta .
$$

The comparison is strict on a positive-length interval near $u=0$, because both $u,J(u)\to0$ there, the two distinct $f$ arguments are above $4$, and strictness holds for $f$. The substitution $u\mapsto u_\vartheta$ is increasing onto $(0,v)$. By weighted arithmetic-geometric mean its derivative is at least $J'^\vartheta$. Integrating the right-hand side after this lower derivative bound gives exactly $Z_1^{1-\vartheta}Z_2^\vartheta$, while the left-hand side is strictly greater. This proves that $M$ is strictly log-concave on $(4,\infty)$. Consequently $m'(x)=(\log M)'(x)$ is nonincreasing on $(0,\infty)$ and strictly decreasing on $(4,\infty)$. The latter follows because equality of two derivatives of a differentiable concave function forces linearity between those points.

We will also use the following immediate variant of this substitution. For $0<d\le20$ set $G_d(c)=\int_0^d M(s)M(c+s)\,ds$, with $c\ge20-d$. It is strictly log-concave in $c$: use the same normalized maps on the common support $(0,d)$, now with $F_i(s)=M(s)M(c_i+s)$, and take the interval of strictness near the *upper* endpoint $d$. The two second-factor arguments then approach $c_i+d\ge20$, and are distinct and above $4$ for $c_1<c_2$. Their endpoint limits also ensure a genuine interval of strictness. $G_d$ is positive and differentiable in the interior, with the respective right derivative at its left boundary; differentiation gives $G_d'(c)=\int_0^d M(s)A(c+s)\,ds$, by bounded differentiation on compact ranges. Its logarithmic derivative therefore strictly decreases, also in comparison with the right derivative at the left endpoint.

## 2. A single upward crossing of the genuine mixed coefficient

Integrate the exact formula (7) of the four-parity law by parts in the integration variable $g$. Writing $B=b+20$ gives the identity

$$
 Q(a,b)=M(a-20)M(b)+\int_0^{20}M(a-g)A(B-g)\,dg .
 \tag{1}
$$

Indeed the first formula after taking out the nonlong terms is $M(a)M(B)-\int_0^{20}A(a-g)M(B-g)\,dg$. Since $M$ is locally absolutely continuous, the boundary evaluation is valid even when $a-g=0$ inside the interval or at an endpoint. The positive atom $M(b)\delta_{20}$ in (1) is essential; omitting it would replace the actual nonlong residue.

Define the finite signed measure $d\Lambda_b(g)=\mathbf1_{[0,20]}(g)A(B-g)\,dg+M(b)d\delta_{20}(g)$. Its negative part is left of $g_0=\min(20,B-v)$ and its positive part is at or right of $g_0$. In fact its density is negative when $g<B-4$, zero in the intermediate plateau, and positive when $g>B-v$, restricted to $g\in[0,20]$ and apart from measure-zero endpoint conventions. It is strictly negative on $(0,1)$ for every $b\ge0$. For $0<a\le g_0$, the positive part has weight zero in (1), and some of the negative part has positive weight $M(a-g)$. Hence $Q(a,b)<0$ there. Also $Q(0,b)=0$.

At a positive zero $a>g_0$, write $D(g)=m'(a-g)$ where $g<a$. For $a\ne20$, differentiate (1) in $a$, and use $Q(a,b)=0$ to rewrite the derivative as

$$
 \partial_a Q(a,b)
      =\int_{g<a}\bigl(D(g)-D(g_0)\bigr)M(a-g)\,d\Lambda_b(g).
 \tag{2}
$$

The absolutely continuous part may be differentiated by domination, since $M$ is locally Lipschitz and $g=a$ is a single integration point. The term $D(g)M(a-g)=A(a-g)$ stays bounded even at an endpoint. The atom is differentiable off $a=20$; its zero-weight part for $g\ge a$ contributes nothing there. The integrand with the signed measure in (2) is nonnegative, since $D$ is nondecreasing in $g$. It is strictly positive in integral on $0<g<1$: there the measure has strictly negative density, $a-g>4$, and $a-g>a-g_0>0$, so the strict log-slope comparison gives $D(g)<D(g_0)$. This proves a strictly upward crossing. At a root with $a=20$, the same argument for the absolutely continuous part yields a positive derivative: the atom has $M(a-20)=0$ at that point, so subtracting $D(g_0)$ is still justified. The atom adds $0$ to the derivative from the left and $M(b)\ge0$ from the right. Thus both one-sided derivatives are positive.

To obtain a uniform upper bracket write $a=20+x$ with $x\ge0$. In (1) change $s=20-g$ and integrate by parts once more. This gives

$$
 Q(20+x,b)=M(x+20)M(b+20)-\int_0^{20}A(x+s)M(b+s)\,ds .
 \tag{3}
$$

At $x=v$ the integral is nonpositive and the first term is strictly positive, for all $b\ge0$. By continuity there is a root strictly between $g_0$ and $20+v$. Every positive zero has the strictly upward orientation proved above, so there cannot be two: a positive point just right of the first and a negative point just left of the second would force a first zero between them with nonnegative values on its left. That contradicts the local upward orientation. Near zero $Q$ is negative, and above its unique positive root it is positive; otherwise continuity gives another zero. Joint continuity of $Q$ follows from (1) (the only possible jump of $A$ is at zero, a null endpoint in the integral), so bracketing the root by two nearby points with strict opposite signs proves continuity of the curve, including at $b=0$.

## 3. The seam location, subfloor monotonicity, and limit

At $a=20$, (1) gives $Q(20,b)=G_{20}'(b)$. At $b=0$ this equals $\tfrac12M(20)^2>0$ by the chain rule for the absolutely continuous $M$. At $b=v$ it is strictly negative by the sign chart of $A$; the integrand is negative for $s>4-v$ and nonpositive elsewhere. Strict decrease of $G_{20}'/G_{20}$ and continuity imply a unique seam value $b_*\in(0,v)$. The sign orientation of the unique $a$-root then gives the claimed below, at, and above $20$ alternatives.

For a fixed $0<a\le20$, the residue term in (1) is zero, and $Q(a,b)=G_a'(b+20-a)$. If $a=a_Q(b_1)\le20$ and $b_2>b_1$, strict decrease of $G_a'/G_a$ shows $Q(a,b_2)<0$. Thus $a_Q(b_2)>a$, which in particular proves strict increase on $[0,b_*]$. No monotonicity above that subfloor branch is needed for the theorem.

For the last limit, the Dickman theorem's factorial bound on $f$ and the compact support of $\kappa$ give faster-than-exponential decay of $M$. Hence its nonincreasing log slope $m'(x)$ tends to $-\infty$: a finite lower bound on it would give an exponential lower bound for $M$. It follows that $M(b+\xi)/M(b+\eta)\to0$ as $b\to\infty$ for fixed $\xi>\eta\ge0$. Now fix $0<x<v$ and take $d>0$ small enough that $x+d<v$. On $[0,d]$ the integrand $A(x+s)M(b+s)$ in (3) contributes at least $c_x d M(b+d)$ for large $b$, since $A$ has positive minimum there and $M$ is eventually decreasing. Its possibly negative part begins only at $s>4-x>d$, and is $O_x(M(b+4-x))$ in absolute integral. The first term of (3) is $O_x(M(b+20))$. Both are little-oh of $M(b+d)$ by the fixed-shift ratios. Thus $Q(20+x,b)<0$ for sufficiently large $b$, and $a_Q(b)>20+x$. Letting the fixed $x$ approach $v$ and using the uniform upper bracket proves the limit. This proof is entirely about the deterministic phase, not growing floors in the arithmetic theorem.

Finally the exact right-parity contrast has the signs opposite to $Q$ wherever its leading scalar is bounded away from zero in a fixed bounded box. For example it is positive below the reversal and negative above on compact subsets of the respective strict-sign regions with $a>0$. The maximal squared error remains $O(X^3\ell^{-1/20})$ (up to constants from summing four terms), uniformly over the true adaptive floors and split in each fixed box. On each fixed interior target subwindow the sign is simultaneous off $O_\kappa(X\ell^{-1/20})$ even targets in any sign region with $|Q|\ge\kappa>0$; on the whole window the corresponding count is $O_\kappa(X\ell^{-1/60})$. On the exact reversal or $a=0$ the estimate gives cancellation in mean square. The reflected left-parity contrast has the same chart with the floors interchanged.
