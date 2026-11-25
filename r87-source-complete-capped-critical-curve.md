# The complete capped sign chart and its simple critical curve

This closes the deterministic sign chart of the coefficient in the [capped long-floor theorem](r85-source-capped-long-floor-orbits.md), using the exact [Dickman representation and its sign sectors](r86-source-dickman-capped-phase-chart.md). It does not change the true arithmetic carrier, two prime floors, unit restrictions, divisor tests, or split. Put $v_0=5/4$, $v_1=7/4$, $b_0=4-v_1=9/4$, and write $x_*$ for the unique positive zero of the uncapped $\Psi$, with $4\sqrt{\mathrm e}<x_*<51/5$ as already proved. Let $A$ and its primitive $M$ be the same Dickman functions in the preceding note; in particular $M>0$ on $(0,\infty)$ and is log-concave. Use $x=a+b-20$ as the excess.

**Complete chart.** The coefficient $\Phi(a,b)$ is symmetric. For any fixed $0<b\le20$ and $a\ge0$, it has the following signs:

- If $x\le0$, it is zero.
- If $0<b\le b_0$, it is positive on $x>0$ with $a<20+v_1$, zero on $20+v_1\le a\le24-b$, and negative on $a>24-b$. This is the genuine plateau from the preceding note, including its collapsed case at $b=b_0$.
- If $b_0<b<x_*$, there is a unique positive root $x_b$ with
  $$
             \max(b,4)< x_b< \min(b+v_1,x_*).
  $$
  The sign is positive for $0<x<x_b$ and negative for $x>x_b$. In the floor coordinate the root is $a_*(b)=20-b+x_b>20$.
- If $x_*\le b\le20$, the unique positive root is $x=x_*$, with strict positivity before it and strict negativity afterwards.

On either axis the coefficient is zero, and if $a,b\ge20$ it is strictly negative, by the preceding sign sectors. Swapping the axes when necessary, these cases determine its sign everywhere on the nonnegative quadrant.

The intermediate root satisfies $0<x_b'(b)<1$, so $a_*(b)$ is continuously differentiable and strictly decreasing from $20+v_1$ to $20$ over $b_0<b<x_*$. Its endpoint behavior is

$$
 \begin{split}
 (20+v_1)-a_*(b)
   &=\log(v_1/v_0)\sqrt{v_1/6}\,(b-b_0)^{3/2}
                                +O((b-b_0)^2),\qquad b\downarrow b_0,\\
 a_*(b)-20
   &=\frac{v}{M(x_*)+v}(x_*-b)+O((x_*-b)^2),\qquad b\uparrow x_*,
       \quad v=-\Psi'(x_*)>0.
 \end{split}
 \tag{1}
$$

All assertions on the chart and curve are deterministic. They give arithmetic signs and simultaneous mean-square cancellation only through the earlier capped theorem on fixed bounded parameter boxes. They do not give pointwise control for a prescribed target, a growing parameter box, or Hypothesis S.

## 1. Exact reduction to one truncated convolution

The preceding note established the exact formula

$$
 \Phi(a,b)=\int_0^{20} A(a-g)M(b-20+g)\,dg-M(a)M(b-20).
$$

When $0<b\le20$ the boundary term is zero and $r=b-20+g$ ranges effectively over $[0,b]$, because $M(r)=0$ for $r\le0$. The formula becomes

$$
 T(x,b):=\Phi(a,b)=\int_0^b A(x-r)M(r)\,dr,\qquad x=a+b-20.
 \tag{2}
$$

Extend $A$ by zero below zero as before. Thus $T=0$ if $x\le0$, and for $0<x\le b$ it equals the full convolution $\Psi(x)=(A*M)(x)$. For $x>b$ one has the exact identity

$$
             T(x,b)=\Psi(x)-\int_b^x A(x-r)M(r)\,dr .
 \tag{3}
$$

For reference, the only sign data about the short function needed below are $A(x)>0$ on $(0,v_1)$, $A=0$ on $[v_1,4]$, $A(x)<0$ for $x>4$, and $A=1$ on $(0,v_0)$; moreover $M(r)=r$ on $[0,v_0]$. These follow from the scale-four Dickman formulas of the preceding note.

Take first $x_*\le b\le20$. For $x\le b$, the strict signs and unique positive zero follow from the full $\Psi$. If $b<x<b+v_1$, the omitted integral in (3) is strictly positive, since $0<x-r<v_1$ in its interior and $M(r)>0$. Thus $T<\Psi(x)<0$. For $x\ge b+v_1$ one has $a\ge20+v_1$ and $a+b=x+20>24$, so the earlier outer sign sector gives strict negativity. This includes the transition case $b=x_*$ and all endpoints. The chart for $0<b\le b_0$ was already established in the same earlier note.

## 2. All intermediate zeros are strict downward crossings

Suppose $b_0<b<x_*$. The full convolution is positive on $0<x\le b$, since $b<x_*$. If $b<x\le4$, then $0<x-b< v_1$ and the integrand in (2) is nonnegative, with a positive subinterval near $r=b$ since $M(b)>0$. This supplies strict positivity up to $x=\max(b,4)$. At and beyond $x=b+v_1$ we again have the already strictly negative outer sector, because $b>b_0$. A positive zero must therefore lie in the open mixed interval

$$
                       \max(b,4)<x<b+v_1 .
 \tag{4}
$$

There is at least one such zero by continuity. On this open interval $x>b$, so write (2) in the form $\int_{x-b}^x A(y)M(x-y)\,dy$. Its first partial derivatives are

$$
 \begin{split}
 T_x(x,b)&=-A(x-b)M(b)
                  +\int_{x-b}^x A(y)A(x-y)\,dy,\\
 T_b(x,b)&= A(x-b)M(b)>0 .
 \end{split}
 \tag{5}
$$

For the first formula use absolute continuity of $M$, the vanishing $M(0)=0$ at the upper endpoint and continuity of $A$ at the positive lower endpoint. The integrands for the differentiated integral are bounded on these compact coordinate ranges, and the jump at a zero argument occurs at a single integration point. Continuity of both partial derivatives in this region follows directly by writing the integral in (5) over $0<r<b$ as $A(x-r)A(r)$; $x-r$ stays positive nearby. Thus we can use the continuous partial derivatives in an implicit function argument.

At a zero in (4), let $y_0$ be any point of $(v_1,4)$, which lies strictly inside $[x-b,x]$ there. Put $q(y)=A(x-y)/M(x-y)$ on the open integration interval. Log-concavity of $M$ gives that its logarithmic derivative $A/M$ is nonincreasing on the positive half-line, so $q$ is nondecreasing in $y$. Using $T(x,b)=0$ in (5) gives

$$
 \int_{x-b}^x A(y)A(x-y)\,dy
     =\int_{x-b}^x A(y)M(x-y)\bigl(q(y)-q(y_0)\bigr)\,dy<0.
 \tag{6}
$$

Indeed below $v_1$ the factor $A(y)$ is positive and $q(y)-q(y_0)\le0$; between $v_1$ and $4$ it vanishes; above $4$ the factor $A(y)$ is negative and $q(y)-q(y_0)\ge0$. The inequality is strict near $y=x$: there $A(y)<0$ and $q(y)=1/(x-y)$ for sufficiently small positive $x-y$. There is no integrability issue, since the factor $M(x-y)$ cancels the possible singularity and both $A$ and $M$ are bounded on the interval. This proves the stronger strict bound

$$
                      T_x(x,b)<-T_b(x,b)<0
 \tag{7}
$$

at every zero of (4).

Thus every zero is isolated and crosses strictly from positive to negative. The zero set is compactly contained in (4), by the strict endpoint signs and continuity, so it is finite (an infinite subset would have an accumulation point which is itself a zero and not isolated). Two consecutive zeros with strictly downward crossings would require another zero between them, by the conflicting interior signs. Hence there is exactly one, denoted $x_b$, and the signs on its two sides are strict for all $x>0$. At that zero the omitted integral in (3) is strictly positive because $0<x_b-b<v_1$. It follows that $\Psi(x_b)>0$ and therefore $x_b<x_*$, proving the stronger bracket in the statement. The implicit function theorem applies by (5)–(7); uniqueness joins the local curves to one continuously differentiable function, with

$$
                x_b'(b)=-T_b(x_b,b)/T_x(x_b,b)\in(0,1).
$$

Subtracting the linear shift from $x$ to $a$ then gives the asserted strictly decreasing critical floor. Its endpoint limits already follow from the bracket: $x_b\to4$ as $b\downarrow b_0$, and $x_b\to x_*$ as $b\uparrow x_*$.

## 3. The fractional-power endpoint and the upper tangent

For the lower endpoint put $\beta=b-b_0>0$, $h=x_b-4$ and $p=b+v_1-x_b=\beta-h$. Thus $0<h,p<\beta$. In (2) the positive part and the negative part are disjoint: $A(x_b-r)>0$ only for $b-p<r<b$, and $A(x_b-r)<0$ only for $0<r<h$. On the positive part $M(r)$ is the same constant $m_0=M(b_0)$ for all sufficiently small $\beta$, since its entire interval lies strictly inside the initial plateau $[v_1,4]$. From the Dickman formula $M=4e^{\gamma_{\rm E}}f*\kappa$, this plateau value is

$$
               m_0=\int_0^{v_1}\kappa(r)\,dr
                   =\mathbb E_\pi U=\frac{v_1-v_0}{\log(v_1/v_0)}.
$$

On $b-p<r<b$, set $z=b-r$. Then $x_b-r=v_1-p+z$ and $A$ is the original $\log(v_1/(v_1-p+z))/\log(v_1/v_0)$ branch. The positive part is exactly

$$
       \frac{m_0}{\log(v_1/v_0)}
          \{p+(v_1-p)\log(1-p/v_1)\}
       =\frac{m_0}{2v_1\log(v_1/v_0)}p^2+O(p^3).
$$

On the negative part $M(r)=r$ and, for small $\beta$, $x_b-r=4+h-r$ lies just in the logarithmic negative branch of $A$ identified in the preceding note. Its contribution is

$$
        -\int_0^h r\log\!\left(1+\frac{h-r}{4}\right)dr
                                       =-\frac{h^3}{24}+O(h^4).
$$

At the root the two contributions cancel. For small $\beta$ this implies $p^2\asymp h^3$, hence $p=O(\beta^{3/2})$ and $h=\beta+O(\beta^{3/2})$. Substituting into the leading constants gives

$$
       p=\sqrt{\frac{2v_1\log(v_1/v_0)}{24m_0}}\,
                             \beta^{3/2}+O(\beta^2)
        =\log(v_1/v_0)\sqrt{v_1/6}\,\beta^{3/2}+O(\beta^2).
$$

The last equality uses $v_1-v_0=1/2$, and $p=(20+v_1)-a_*(b)$, proving the first line of (1).

For the upper endpoint we first verify that the uncapped root is simple, not just unique. By differentiating $\Psi=A*M$ using bounded $A$ and absolutely continuous $M$, one obtains $\Psi'(x)=(A*A)(x)$ on $x>0$. The convolution is continuous: $A$ is bounded and integrable, so translation continuity in $L^1$ in one factor and boundedness of the other suffice. The same argument as (6) on $0<y<x_*$, using $\Psi(x_*)=0$ and any $y_0\in(v_1,4)$, gives $\Psi'(x_*)<0$, with strictness near $y=x_*$ since $x_*>4$. In fact $\Psi'$ is Lipschitz. The Dickman density is monotone on its positive support and zero on the negative side, with only its finite jump at zero, so has globally bounded variation. The formula $A=4e^{\gamma_{\rm E}}(f-\pi*f)$ implies the same for $A$; the convolution with $\pi$ contracts total variation. Hence $\|A(\cdot+t)-A\|_1\le |t|\operatorname{Var} A$, which after convolution with bounded $A$ proves the Lipschitz assertion.

Now let $\beta=x_*-b>0$, $h=x_b-b=a_*(b)-20>0$, and $d=x_*-x_b=\beta-h>0$. They are all small at this endpoint, and $A(x_b-r)=1$ on the interior of the removed integral in (3) for $b<r<x_b$, once $\beta<v_0$. Thus

$$
  \Psi(x_b)=\int_b^{x_b}M(r)\,dr
           =M(x_*)h+O(\beta h).
$$

Writing $v=-\Psi'(x_*)>0$, Lipschitz continuity of $\Psi'$ also gives
$\Psi(x_b)=v d+O(d^2)$. Since $h+d=\beta$, we obtain
$h=v\beta/(M(x_*)+v)+O(\beta^2)$, as claimed. In particular this endpoint tangent is strictly between zero and one in magnitude for the decreasing floor graph; the old straight branch for $b\ge x_*$ is stated separately in the chart.

## 4. Arithmetic meaning of the classification

The symmetry, the old small-$b$ chart, the just-proved intermediate branch, the old unique uncapped threshold, and strict negativity for both floors at least twenty exhaust the full quadrant. The plateaus, axes, zero excess region and simple critical graph are zeros of the exact deterministic local term in the earlier carrier theorem. Thus that theorem supplies simultaneous mean-square cancellation for arbitrary targetwise selections on these zero sets inside any fixed bounded floor box, with its original simultaneous split range.

On any fixed interior target interval and compact part of a sign region separated from zero, the earlier joint estimate gives the corresponding strict arithmetic sign outside its common exceptional set. One can also quantify separation locally along the intermediate curve: fix a compact subinterval of $b_0<b<x_*$, then (5)–(7), continuity and the compact root graph give a fixed neighborhood in which $|\Phi(a,b)|\gg |a-a_*(b)|$. For choices in that neighborhood at horizontal distance at least $s>0$ from the curve, a wrong sign in a fixed interior target interval contributes $\gg X^2s^2$ to the squared error. The simultaneous bound of the capped theorem therefore gives at most $O(X\ell^{-1/20}s^{-2})$ such even targets, with its original $\ell=\log\log X$. This does not extend the estimate to any prescribed exceptional target or to an unrelated carrier.
