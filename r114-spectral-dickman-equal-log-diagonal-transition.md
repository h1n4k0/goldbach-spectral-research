# The first two-prime Dickman zero reaches the equal-log diagonal

**Scope.** This classifies the ordinary two-missing-prime finite Dickman profile for every smaller log whose ratio to the cap stays in a fixed compact subinterval of $(0,1)$, including the crossover near half the cap. The first of three sign transitions reaches the equal-log diagonal at a unique threshold and then disappears from the ordered domain. We locate the threshold relative to half the one-prime root, including a positive factorial-scale correction. The arithmetic application is only a fixed-parameter genuine matched parity mean under reinforcing signs; the diagonal is a continuum boundary, not an assertion that one actual missing prime is repeated.

Use the notation of [the ordinary finite profile](r108-spectral-finite-matched-ordinary-dickman-profile.md). In particular $\rho$ is the cumulative Dickman function, zero on the negative axis, $\kappa=\int_0^\infty\rho$, $C(a)=\int_{\mathbb R}\rho(u)\rho(u+a)\,du$, and $\mathcal T(a)=\int_a^\infty C(v)\,dv$. Let $G_t$ be the normalized evenized cap from [the earlier two-prime analysis](r110-spectral-three-two-prime-dickman-transitions.md), and write $F_t(a)=2G_t(a)-G_t(0)$ for the one-prime coefficient. Let $\lambda_*(t)$ denote its unique zero from [the one-prime sign theorem](r109-spectral-finite-dickman-cap-sign-threshold.md), $d_t=t-\lambda_*(t)$, and $\xi_t=\xi(d_t)$, where $e^{\xi(d)}=1+d\xi(d)$ and $\xi(d)>0$. Thus $d_t\sim\log t/\log\log t$, $\xi_t\sim\log\log t$ and $t C(d_t)=\kappa^2+O(t^{-1})$.

**Theorem.** Fix $0<c<1/2$. For all sufficiently large $t$ depending on $c$, put $\eta=c/10$ and $E_t=(1+t)/(\lfloor\eta t\rfloor-1)!$. There exists a unique diagonal threshold $x_{\mathrm d}(t)$ on $ct\le x\le(1-c)t$. Writing $x_0(t)=\lambda_*(t)/2$,

$$
 x_{\mathrm d}(t)-x_0(t)
   =\frac{t C(t-x_0(t))}{\kappa^2\xi_t}
      \bigl(1+O_c(d_t^{-1})\bigr)>0.
 \tag{1}
$$

For every $ct\le x\le(1-c)t$, scan the ordered domain $y\ge x$:

- If $x<x_{\mathrm d}$, there are exactly three simple zeros; the signs are positive, negative, positive, negative in that order, with positivity at $y=x$.
- If $x=x_{\mathrm d}$, the first zero is at $y=x$ and is simple from the right. The other two zeros remain interior. The sign is negative immediately to the right of the diagonal, then positive, then negative.
- If $x>x_{\mathrm d}$, exactly the two interior zeros remain, with negative, positive, negative signs, starting with negativity at $y=x$.

Where the three roots exist, in increasing order they satisfy

$$
 y_1=\lambda_*(t)-x+O_c(E_t/\xi_t),\qquad
 y_2=\lambda_*(t)+O_c(E_t/\xi_t),\qquad
 y_3=\lambda_*(t)+x+O_c(E_t/\xi_t).
 \tag{2}
$$

The first estimate includes $y_1=x$ at contact, and the other two hold throughout the full smaller-log range. The first-root graph is continuously differentiable for $x<x_{\mathrm d}$ in the interior of the stated range and satisfies

$$
 y_1'(x)=-1+O_c(E_t/\xi_t),\qquad
 y_1(x)-x=2(x_{\mathrm d}-x)
                       \bigl(1+O_c(E_t/\xi_t)\bigr).
 \tag{3}
$$

Thus the boundary disappearance has a transverse slope; (3) has no minimum size requirement on $x_{\mathrm d}-x$.

## 1. Exact diagonal crossing and its location

For $y\ge x$, the exact profile is

$$
 \Phi(t;x,y)=G_t(0)-2G_t(x)-2G_t(y)+2G_t(y-x)+2G_t(y+x).
 \tag{4}
$$

The value on the diagonal is therefore
$D_t(x):=\Phi(t;x,x)=F_t(2x)+4\{G_t(0)-G_t(x)\}$.
For any nonnegative argument $a$ with $|a-t|\ge\eta t$, the earlier two-prime analysis gives
$G_t(a)=\mathbf 1_{a<t}+O_c(E_t)$ and $G_t'(a)=O_c(E_t)$, since the two endpoints in its exact cap formula and their derivatives have factorial tails. In particular $G_t(0)-G_t(x)=O_c(E_t)$ and its derivative in $x$ is $O_c(E_t)$ on the entire required range.

The uniform one-prime separation from the earlier two-prime analysis, Section 2, bounds $|F_t(a)|$ below by a positive constant for $|a-\lambda_*|\ge1/\xi_t$, all $a\ge0$ and large $t$. Inside the remaining interval, $-F_t'(a)\gg\xi_t$, and the values at its two endpoints have opposite signs. Applied to $a=2x$, this proves that $D_t(x)$ has exactly one zero $x_{\mathrm d}$, with positive sign before and negative sign after, since $2x_0=\lambda_*$ and the whole microinterval is contained in $[ct,(1-c)t]$ as $t$ becomes large. The mean value theorem gives $x_{\mathrm d}-x_0=O_c(E_t/\xi_t)$. At $x=x_0$, the value $4(G_t(0)-G_t(x_0))$ is strictly positive by strict decrease of $F_t$ on $[0,t-1]$. This already fixes the sign of the shift.

For its relative asymptotic, use the exact cap, with $d_0=t-x_0$:

$$
 \begin{split}
 \kappa^2\{G_t(0)-G_t(x_0)\}
   ={}&\mathcal T(d_0)+\tfrac t2 C(d_0)
       +\mathcal T(t+x_0)+\tfrac t2 C(t+x_0)\\
      &-2\mathcal T(t)-tC(t).
 \end{split}
 \tag{5}
$$

The first term is at most $2C(d_0)$ by the [separated above-cap analysis](r111-spectral-two-exterior-logs-negative-dickman-pocket.md), Section 1. All the terms at $t$ or $t+x_0$ are factorial-small relative to $C(d_0)$ by the relative shifted-tail inequality in [the all-exterior analysis](r113-spectral-all-above-cap-dickman-classification.md), (4), since $t-d_0=x_0\sim t/2$ and the same integrated comparison uses $\mathcal T\le2C$. Hence

$$
 D_t(x_0)=\frac{2t C(d_0)}{\kappa^2}(1+O(t^{-1})).
 \tag{6}
$$

The derivative of $F_t$ at $a=\lambda_*+v/\xi_t$ for $|v|\le1$ satisfies
$F_t'(a)=-\xi_t e^v(1+O(d_t^{-1}))$. Indeed the exact cap derivative is
$\kappa^2 F_t'(a)=2\{C(t+a)-C(t-a)\}-t\{C'(t+a)-C'(t-a)\}$.
The far terms are factorial-small, while $-C'(d)=\xi(d)C(d)(1+O(d^{-1}))$ from the separated above-cap analysis, (4), and
$t C(d_t-v/\xi_t)=\kappa^2 e^v(1+O(d_t^{-1}))$ by the correlation ratio and calibration in the two-prime analysis. Also $\xi(d_t-v/\xi_t)/\xi_t=1+O(d_t^{-1})$ there. Consequently on the segment between $x_0$ and $x_{\mathrm d}$ we have $D_t'(x)=-2\xi_t(1+O_c(d_t^{-1}))$: the corresponding $v=(2x-\lambda_*)\xi_t$ is $O_c(E_t)$, and the inactive derivative contributes only $O_c(E_t)$. Combining this with (6) proves (1).

## 2. The truncated first scan and the two surviving roots

For fixed $x$, take closed windows of radius $\eta t$ on the $y$ line centered at $t-x$, $t$, and $t+x$. They are disjoint, since the separation is $x\ge ct=10\eta t$. The second and third windows lie strictly in $y>x$, since $t-x\ge ct$. The first window can be truncated at $y=x$ or lie entirely to its left. In each window intersected with $y\ge x$, only the indicated argument of (4) can be within $\eta t$ of the cap:

- Near $t-x$, the argument $y+x$ is active, and $x,y,y-x$ are inside the cap. In fact $y\le (1-c+\eta)t$ and $0\le y-x\le y$.
- Near $t$, the argument $y$ is active, $x,y-x$ are inside, and $y+x$ is outside. Use $x\ge ct$ and $x\le(1-c)t$.
- Near $t+x$, the argument $y-x$ is active, $x$ is inside, and $y,y+x$ are outside, again with the required margin.

Substituting the corresponding inactive indicator values into (4), while keeping the active cap, gives the three formulas

$$
 F_t(y+x)+O_c(E_t),\qquad
 -F_t(y)+O_c(E_t),\qquad
 F_t(y-x)+O_c(E_t).
 \tag{7}
$$

In all three formulas both errors' first partial derivatives in $x,y$ are $O_c(E_t)$ by the inactive derivative estimates: the arguments in (4) are affine, and the errors consist of differences of inactive values from constants. At $y=x$ the derivative of the even cap at the zero argument is zero since its formula differentiates there at lag endpoints $\pm t$, away from the correlation cusp. Thus one-sided derivatives on the ordered domain are also covered.

Outside the three windows all arguments are inactive, so substitution into (4) gives the signs of the signed indicator count. Concretely, on $y<t$ the count is $+1$ for $x+y<t$ and $-1$ for $x+y>t$; on $y>t$ it is $+1$ for $y-x<t$ and $-1$ for $y-x>t$. These signs persist under $O_c(E_t)$. In the full second and third windows, use the uniform one-prime separation and the strict derivative inside $|a-\lambda_*|\le1/\xi_t$ from Section 1. Each contains one simple root, respectively negative to positive and positive to negative, and their locations are as in (2).

For the first window, any root must have $|(y+x)-\lambda_*|\le1/\xi_t$ by the uniform separation and (7). In the part of this microinterval on the ordered domain, $\partial_y\Phi\ll-\xi_t$, so there is at most one root there. The active argument at the right edge of the first window is $t+\eta t$, where the sign is negative whenever this edge is in the domain. If its left edge is in the domain, its sign is positive by the corresponding $t-\eta t$ comparison, giving the first crossing. If the first window is truncated at the diagonal, its starting value is exactly $D_t(x)$; the global separation and strict derivative on the only possible zero interval yield an interior crossing if this value is positive, a boundary crossing if zero, and no crossing if negative. If the entire first window lies left of the domain, then its active argument on the remaining scan starts above $t+\eta t$, the diagonal value is negative by Section 1, and there is no first crossing. This also accounts for endpoint coincidences with a window edge, where the signed comparison is strict. It proves the stated sign patterns and the first location in (2), including contact.

At a first root, differentiate the first approximation in (7): both $\partial_x\Phi$ and $\partial_y\Phi$ equal $F_t'(y+x)+O_c(E_t)$, whose magnitude is $\gg\xi_t$. The implicit function theorem gives $y_1'=-1+O_c(E_t/\xi_t)$ for interior $x<x_{\mathrm d}$. The graph extends continuously to $y_1(x_{\mathrm d})=x_{\mathrm d}$: any limiting root at $x_{\mathrm d}$ is still in the first microinterval, whose only root is that diagonal point. Integrating $y_1'-1$ up to this endpoint proves the second formula of (3). The same partial derivative bound gives simplicity from the right at contact.

## 3. Arithmetic consequence at fixed parameters

Keep all hypotheses of the original finite ordinary profile, with two actual missing conductor primes, the complete primorial divisibility family, fixed weights, and an actual odd Page conductor if one occurs. Let $t_*=2Bg/\ell\to t$ for a fixed sufficiently large $t$, and let the two actual scaled logs converge to $x,y$ in the ordered range of the theorem. A limiting point off the zero set has a fixed nonzero ordinary sign $s$ by continuity, including possible equal limiting scaled logs of distinct primes. Under the additional closeness $(1-\beta)G\le C_*\log G$ for fixed $C_*$ and $\chi(-1)=-s$, the exceptional term reinforces, since $P_1(M)>0$ by [the matched exceptional comparison](r100-spectral-matched-ramanujan-exceptional-mean.md). The genuine matched parity mean has sign $s$ and magnitude $\gg\mathcal R+HP_1(M)$, for the full mixed strip or its original moving-major integral, by the original finite-profile formula. This does not give an arithmetic estimate with cutoff growing with $Y$, a sign at exact zeros or with competing terms, a pointwise arithmetic autocorrelation statement, a full signed-shell estimate, or Weak S. No Page-zero existence is asserted, and neither Dirichlet GRH nor an external zero-gap result is used.
