# Dickman formulas for the actual capped phase: a zero plateau and strict sign regions

This evaluates the deterministic coefficient already attached to the genuine sums in the [capped long-floor theorem](r85-source-capped-long-floor-orbits.md). No divisor cut, prime floor, split, parity, unit mask, or typical count is changed. Its arithmetic consequences below refer only to that prescribed carrier and its mean-square result.

Write $v_0=5/4$, $v_1=7/4$, and let $\pi$ be the probability measure with density $\mathbf1_{[v_0,v_1]}(u)/(u\log(v_1/v_0))$. Let $\nu$ denote the locally consistent short signed measure

$$
 \nu=(\delta_0^{\rm at}-\pi)*\exp_*\!\left(-\mathbf1_{[4,\infty)}(t)\frac{dt}{t}\right),
 \qquad A(x)=\nu([0,x]),\qquad M(x)=\int_0^x A(t)\,dt ,
 \tag{1}
$$

with $A,M=0$ for $x<0$ and $M(0)=0$. Interpret the exponential on each bounded interval using any finite cutoff beyond that interval. Let $\Phi(a,b)$ be the capped signed coefficient of that theorem for $a,b\ge0$, and $\Psi$ the earlier uncapped coefficient of the [short-prime sign theorem](r79-source-short-prime-euler-sign-transition.md).

**Results.** There is an exact deterministic identity

$$
 \Phi(a,b)=\int_0^{20} A(a-g)M(b-20+g)\,dg
                         -M(a)M(b-20) .
 \tag{2}
$$

In particular the explicit residue-product contribution in the original two-area formula is $-M(a-20)M(b-20)\le0$. The following sign assertions hold, with symmetry in $a,b$:

- If $a\ge87/4$ and $b>0$, then $\Phi(a,b)=0$ for $a+b\le24$, and $\Phi(a,b)<0$ for $a+b>24$. In particular it is strictly negative for $a\ge24$, $b>0$.
- For each $0<b\le9/4$ the entire horizontal chart is exact: $\Phi=0$ for $a+b\le20$; $\Phi>0$ for $a+b>20$ and $a<87/4$; $\Phi=0$ on $87/4\le a\le24-b$; and $\Phi<0$ for $a>24-b$. The middle plateau has nonempty interior when $b<9/4$.
- If both $a,b\ge20$ then $\Phi(a,b)<0$, including the part below $87/4$ on both axes.
- The uncapped $\Psi(x)$ has exactly one zero on the entire positive half-line, the previously bracketed root $x_*\in(4\sqrt{\mathrm e},51/5)$. Its sign is strictly positive on $0<x<x_*$ and strictly negative on $x>x_*$. This global deterministic uniqueness applies to the old arithmetic region $0<a+b-20\le20$ when both floors are at most $20$; it is not a claim that the **capped** phase equals the uncapped one outside that region.

The zero plateau and other identified zero sets give genuine simultaneous mean-square cancellation via the capped theorem for bounded choices on those sets. Strict signs give true arithmetic signs on the interior away from zero with its earlier common exceptional set, not a pointwise theorem for each target or Hypothesis S. We also give explicit vanishing orders on both sides of the plateau.

## 1. A positive scale-four Dickman probability

On each dyadic subinterval of $(0,4]$ take an independent Poisson point process with intensity $dt/t$ and sum all its points over all intervals. The sum $D$ is finite almost surely since its expectation is $\int_0^4 t\,dt/t=4$. Equivalently this is the nonnegative limit of the usual finite compound Poisson laws with a lower cutoff tending to zero. Its Laplace transform, for $s>0$, is

$$
 \phi(s)=\mathbb E\,e^{-sD}
     =\exp\!\left(\int_0^4(e^{-st}-1)\frac{dt}{t}\right).
$$

Indeed the finite compound Poisson formula follows by summing the Poisson probabilities and the Laplace transform of one point, and passage to the limit follows by bounded convergence. This also shows the law has no atom at zero, since $\phi(s)\to0$ as $s\to\infty$. Denote the law by $\mathcal D$. Differentiating its Laplace transform gives $-\phi'(s)=\phi(s)(1-e^{-4s})/s$. By uniqueness of Laplace transforms this means that the measure $x\,\mathcal D(dx)$ is $\mathcal D*\mathbf1_{[0,4]}(x)\,dx$; in this notation the right-hand side is convolution with Lebesgue measure restricted to $[0,4]$. Both measures are finite, of mass four. Hence $\mathcal D$ has a density $f$ on $(0,\infty)$ and no missing atom. There is a continuous representative on $(0,\infty)$, directly from

$$
        x f(x)=\int_{(x-4)_+}^x f(y)\,dy.
 \tag{3}
$$

Extend $f$ by zero on $x<0$ and take its initial right value at zero. For $0<x<4$ it is constant, since differentiating (3) gives $xf'(x)=0$ there. Let $\gamma_{\rm E}$ be Euler's constant. The elementary exponential integral identity
$E_1(w)=\int_w^\infty e^{-t}\,dt/t
       =-\gamma_{\rm E}-\log w+\int_0^w(1-e^{-t})\,dt/t$
gives $s\phi(s)\to e^{-\gamma_{\rm E}}/4$ as $s\to\infty$. Thus the initial constant is $f(0+)=e^{-\gamma_{\rm E}}/4$, since the tail of the Laplace integral from $4$ on is at most $e^{-4s}$. Equation (3) makes $f(x)>0$ for every $x>0$ by induction on intervals of length four: up to the next endpoint the integration interval always meets a previously positive interval of positive length, and at the endpoint use (3) with the newly established positivity immediately below it. For $x>4$ differentiation gives $x f'(x)=-f(x-4)$. In particular $f$ is nonincreasing on the positive half-line and strictly decreasing for $x>4$. This is the scale-four Dickman density, with the normalization established directly.

The measure in (1) is locally finite because each positive atom variable of the exponential is at least four, so only finitely many convolution orders meet a fixed compact interval. Globally it has finite total variation after multiplication by $e^{-sx}$ for every $s>0$: the weighted exponential mass is at most $\exp(\int_4^\infty e^{-st}dt/t)$. Consequently its Laplace transform and the transform of its locally integrable cumulative are unambiguous:

$$
 \widehat\nu(s)=(1-\widehat\pi(s))e^{-E_1(4s)},\qquad
       \widehat A(s)=\widehat\nu(s)/s,\qquad
       \widehat M(s)=\widehat\nu(s)/s^2.
$$

The last two equalities follow by Fubini with the exponentially weighted absolute measure. The identity for $E_1$ gives $e^{-E_1(4s)}=4e^{\gamma_{\rm E}}s\phi(s)$. By uniqueness of the transform, for instance after an exponential weighting of both sides, it follows that

$$
 \begin{split}
 A(x)&=4e^{\gamma_{\rm E}}\bigl(f(x)-(\pi*f)(x)\bigr)
                                  &&\text{for almost every }x,\\
 M(x)&=4e^{\gamma_{\rm E}}\bigl(F_D(x)-(\pi*F_D)(x)\bigr)
                      =4e^{\gamma_{\rm E}}(f*\kappa)(x),&
 \kappa(r)&=\mathbf1_{r\ge0}\,\mathbb P_\pi(U>r),
 \end{split}
 \tag{4}
$$

where $F_D$ is the distribution function of $D$ and $U$ has law $\pi$. The formula for $M$ is exact everywhere by continuity and Fubini. The cumulative $A$ has the displayed continuous representative on $x>0$; any choice at jump points does not affect the area integrals. Since $f>0$ on the positive half-line and the old shifts are all positive, $M(x)>0$ for $x>0$ and $M=0$ on $x\le0$. Also $M$ is bounded, integrable and globally Lipschitz, and its almost-everywhere derivative $A$ is bounded and integrable by (4).

## 2. Exact boundary cancellation and the two plateau edges

The first area in the capped kernel is the triangle with $0\le g,g'\le20$, $g+g'\ge20$, restricted by $t\le a-g$ and $u\le b-g'$. Integrating the two signed label measures first is legitimate on this bounded set, and gives $A(a-g)A(b-g')$ inside the triangle. The inner integral in $g'$ is

$$
 \int_{20-g}^{20}A(b-g')\,dg'=M(b-20+g)-M(b-20).
$$

The second, residue-product area factors as the product of two ramp integrals. Indeed $\int (q-t)_+\,d\nu(t)=M(q)$ by Fubini with the locally finite signed measure, for positive or nonpositive $q$. Thus the contribution is $-M(a-20)M(b-20)$. Since

$$
 \int_0^{20}A(a-g)\,dg=M(a)-M(a-20),
$$

subtracting that residue cancels the endpoint term and gives (2). The identity includes every real parameter value; no arithmetic equality has been changed. A symmetric alternative follows by integration by parts of the absolutely continuous factors.

By (4) and the constant initial segment of $f$, $A(x)=\kappa(x)$ for $0<x\le4$. In particular $A>0$ on $(0,v_1)$ and $A=0$ on $[v_1,4]$. For $x>4$ all shifted arguments $x-u$ are positive and strictly below $x$. As $f$ strictly decreases above $4$ and is constant below it, $f(x-u)>f(x)$ for every such old shift; consequently $A(x)<0$ for $x>4$. On negative $x$, $A=0$. These sign properties are sufficient for the explicit outer sectors without relying on log-concavity.

If $a\ge20+v_1$, then $a-g\ge v_1$ for $0\le g\le20$, so the integral in (2) is nonpositive and the subtracted product is nonnegative before subtraction. If also $b>0$ and $a+b\le24$, then $b\le9/4<20$ and $M(b-20)=0$. The integrand can be nonzero only for $g>20-b$, where $a-g<a+b-20\le4$ and $a-g\ge v_1$. It therefore vanishes. If $a+b>24$, the open interval

$$
     \max(0,20-b)<g<\min(20,a-4)
$$

has positive length: $b>0$, $a\ge20+v_1>4$, and $20-b<a-4$. On it $M(b-20+g)>0$ and $A(a-g)<0$. This proves strict negativity. The axes $a=0$ or $b=0$ give zero directly from the two-area kernel, as does $a+b\le20$.

For the complete small-$b$ chart it remains to check $0<b\le9/4$, $a<20+v_1$, and $a+b>20$. Now $M(b-20)=0$. Where $M(b-20+g)>0$, one has $a-g<a+b-20<4$; hence the integrand in (2) is nonnegative. It is strictly positive on the open interval

$$
       \max(0,20-b,a-v_1)<g<\min(20,a),
$$

which has positive length by the stated bounds. This proves the remaining strict positivity and gives the full chart claimed.

The approach to this plateau has different exact orders on the two sides. For $0<b\le9/4$ and $0<h<\min(b,1/2)$, substitute $r=20-g$ in (2) at $a=20+v_1-h$. Only $0<r<h$ contributes, since $a-g=v_1-h+r$ then lies in the nonconstant part of $\kappa$ and is above it thereafter. This gives

$$
 \begin{split}
 \Phi(20+v_1-h,b)
   &=\int_0^h M(b-r)
       \frac{\log(v_1/(v_1-h+r))}{\log(v_1/v_0)}\,dr\\
   &=\frac{M(b)}{2v_1\log(v_1/v_0)}h^2+O(h^3).
 \end{split}
 \tag{5}
$$

The error uses the boundedness and Lipschitz bound of $M$ and the Taylor expansion on an interval separated from zero. On the other side put $h=a+b-24$ and suppose $a\ge20+v_1$ and $0<h<\min(b,v_0)$. Then $b<9/4+v_0<20$, and in (2) put $r=b-20+g$. Only $0<r<h$ contributes, with $a-g=4+h-r$. In this interval $4<a-g<4+v_0$, so the delay equation gives $f(a-g)=f(0+)(1-\log((a-g)/4))$ and every shifted value used by $\pi$ is still $f(0+)$. Also $M(r)=r$ on this $r$ interval. Therefore

$$
 \Phi(a,b)=-\int_0^h r\log\!\left(1+\frac{h-r}{4}\right)dr
                  =-\frac{h^3}{24}+O(h^4).
 \tag{6}
$$

These are deterministic asymptotic formulas for the exact coefficient, not arithmetic error estimates near a moving zero.

## 3. Log-concavity and the unique uncapped zero

We give the needed log-concavity of the Dickman density directly. For $x>4$ put $h(x)=-f'(x)/f(x)=f(x-4)/(xf(x))$, and put $h=0$ on $(0,4)$. The right limit at $4$ is $1/4$. On $(4,8)$ the delay equation has constant right-hand density, so

$$
       h(x)=\frac1{x(1-\log(x/4))},
$$

whose derivative is strictly positive. Dividing (3) by $f(x-4)$ gives, for $x>4$,

$$
 \frac1{h(x)}
     =\int_0^4\frac{f(x-4+t)}{f(x-4)}\,dt.
$$

For $x>8$ this is differentiable with derivative

$$
     \int_0^4\frac{f(x-4+t)}{f(x-4)}
                         \{h(x-4)-h(x-4+t)\}\,dt .
 \tag{7}
$$

The right limit of (7) at $8$ is strictly negative: $h(4+)=1/4$ and on $(4,8)$ one has $h>1/4$. The passage to the limit is justified by continuity from the right, positivity of the denominators and boundedness on that compact range. Hence $h'>0$ just beyond $8$. On $(8,\infty)$, $h'$ is continuous by the delay equation. If some nonpositive value of $h'$ occurred there, let $x_0>8$ be its first such point. The previous positive derivative, together with continuity of $h$ at $8$ and the initial formula, imply that $h$ is strictly increasing on $[x_0-4,x_0)$ (one-sided conventions where needed). Then (7) at $x_0$ is strictly negative, making $h'(x_0)>0$, a contradiction. Thus $h$ is nondecreasing on the full positive support, with its upward jump at $4$. This proves log-concavity of $f$ there and of its extension by zero on the negative half-line.

The function $\kappa$ is one on $[0,v_0]$, then $\log(v_1/r)/\log(v_1/v_0)$ up to $v_1$, and zero afterwards or below zero. In the transition its log derivative is $-1/(r\log(v_1/r))$, with derivative

$$
       \frac{\log(v_1/r)-1}{r^2\log(v_1/r)^2}<0 .
$$

The log slope moves down from zero at $v_0$, so $\kappa$ is log-concave on its support as well. Convolution preserves log-concavity by the [Prékopa–Leindler integral inequality](https://acta.bibl.u-szeged.hu/14411/1/math_034_335-343.pdf) (Theorem 3 there, applied to the marginal of the product under a linear change of variables). Indeed the product $f(x-r)\kappa(r)$ is jointly log-concave, and the integral in $r$ retains this inequality. Thus $M$ is log-concave by (4), and so is $M*M$.

For $x\ge0$, let $\Psi(x)$ be the uncapped signed integral $\frac12\iint(x-t-u)_+^2\,d\nu(t)d\nu(u)$. This is precisely the earlier deterministic $\Psi$ for every positive $x$: apply the two factors $\delta_0^{\rm at}-\pi$, whose second difference integrates the two old shifts, and the remaining signed exponential is $\exp_*(-2\mathbf1_{[4,\infty)}dt/t)$, the cumulative used in that theorem. All these operations can first be performed with a finite cutoff greater than $x$. Its Laplace transform is $\widehat\nu(s)^2/s^3$ by the same exponentially weighted Fubini argument as in §1. Since $\widehat M=\widehat\nu/s^2$, this is the transform of $(M*M)'$. The derivative is continuous: $M$ is bounded and globally Lipschitz, $A=M'$ almost everywhere is integrable, and $(M*M)'=A*M$. Both sides are continuous on $(0,\infty)$, so uniqueness of the transform gives

$$
                           \Psi(x)=(M*M)'(x).
 \tag{8}
$$

The convolution $M*M$ is positive for every $x>0$, and its logarithmic derivative is nonincreasing by log-concavity. This derivative is $\Psi(x)/(M*M)(x)$. The earlier sign theorem proves $\Psi>0$ at $4\sqrt{\mathrm e}$, $\Psi<0$ at $51/5$ and strict decrease on the interval between them. Thus there is exactly one zero inside that interval and the signs there are strict on the two sides. At earlier positive arguments the logarithmic derivative is at least its strictly positive value at the left endpoint. At later arguments it is at most its strictly negative value at the right endpoint. This proves the asserted global deterministic uniqueness without presuming strictness of Prékopa–Leindler.

## 4. Strict negativity when both floors are at least twenty

For the remaining double-high corner, define

$$
 {\cal H}(a,b)=\int_0^{20}M(a-g)M(b-20+g)\,dg.
$$

For fixed $b$ this is log-concave in $a$: it is the convolution of $M$ and the log-concave function $M(b-20+g)\mathbf1_{[0,20]}(g)$. Differentiation in $a$ gives the integral in (2), using bounded $A$ and absolute continuity; the derivative is continuous by translation of the integrable functions or bounded convergence away from the null set of endpoints. In particular at $b=20$ it is $\Phi(a,20)$, since $M(0)=0$. At $a=11$ this is $\Psi(11)<0$ by the earlier theorem and the capped kernel on the old edge. The function $\mathcal H(a,20)$ is positive for every $a>0$, so its nonincreasing logarithmic derivative is strictly negative for $a\ge20$.

Fix $a\ge20$ and compare $b\ge20$ to $b=20$. Under the probability measure on $(0,20)$ proportional to $M(a-g)M(g)\,dg$, set

$$
       r(g)=\frac{A(a-g)}{M(a-g)},\qquad
       q(g)=\frac{M(b-20+g)}{M(g)}.
$$

These are well-defined in the open interval. Because $M$ is log-concave and positive on the positive half-line, $r$ is nondecreasing in $g$, whereas $q$ is nonincreasing: the log of the latter is the forward increment of $\log M$ by the fixed nonnegative length $b-20$. All the expectations of $|r|$, $q$ and $|rq|$ are finite directly from the weighting and boundedness of $A,M$ on the finite range, even at $a=20$ or $b=20$. The covariance of oppositely monotone functions is nonpositive, by writing twice the covariance as the expectation of $(r(g_1)-r(g_2))(q(g_1)-q(g_2))$ under the product probability. It follows that

$$
      \partial_a\log{\cal H}(a,b)
       =\frac{\mathbb E(rq)}{\mathbb E q}
       \le \mathbb E r
       =\partial_a\log{\cal H}(a,20)<0 .
$$

Thus the integral in (2) is strictly negative in this entire corner, and its subtracted boundary product cannot increase it. This completes the sign assertions. None requires a claim about the other uncategorized capped signs, or an evaluation of any different arithmetic carrier.

## 5. Deterministic limits far from the floor line

The same representation gives decay with no additional arithmetic hypothesis. Since $f$ is nonincreasing, (3) gives $xf(x)\le4f(x-4)$ for $x\ge4$, using the initial right value at zero. Iterating at $x=4n+r$, $0\le r<4$, shows

$$
                      f(x)\le \frac{f(0+)}{\lfloor x/4\rfloor!}.
$$

For $x\ge v_1$, the formulas (4) then give $|A(x)|+M(x)\ll f(x-v_1)$: for $A$ use both positive density values, and for $M$ use its convolution with $\kappa$, supported on $[0,v_1]$. In (2), $a-g\ge a-20$ and $M$ is globally bounded. In particular

$$
    \sup_{b\ge0}|\Phi(a,b)|
           \ll \frac1{\lfloor(a-20-v_1)/4\rfloor!}
                   \qquad (a\ge20+v_1).
 \tag{9}
$$

For every fixed $b>0$ the limit as $a\to\infty$ is therefore zero from the strictly negative side. The uncapped coefficient also tends to zero from below: use (8), split the convolution $A*M$ according to which argument is at least $x/2$, then apply the displayed factorial bound and the integrability of both factors. These are limits of the deterministic coefficient only. The constants in the underlying mean-square theorem were for fixed bounded parameter boxes; nothing here lets those boxes grow with the arithmetic scale.
