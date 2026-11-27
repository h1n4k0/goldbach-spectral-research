# The two-prime Dickman cusp opens a negative interval at distance $2\kappa^2/t$

**Scope.** This determines the exact opening and closing of the negative interval of the ordinary two-missing-prime finite Dickman coefficient when the smaller log is within a fixed small collar of the cap. There are two threshold positions, one on each side of the cap; on the above-cap flank this reaches a smaller log only $O(1/t)$ above it. The arithmetic inference is for the genuine matched parity mean at fixed parameters with reinforcing signs. The large-$t$ cusp expansion is deterministic only, not a growing-cutoff arithmetic limit or a pointwise conductor-wall calculation.

Use the normalization of [the finite ordinary profile](r108-spectral-finite-matched-ordinary-dickman-profile.md) and the even cap $G_t=h_t/\kappa^2$ of [the two-prime transition analysis](r110-spectral-three-two-prime-dickman-transitions.md). The ordinary Dickman function $\rho$ is extended by zero on the negative axis, $\kappa=\int_0^\infty\rho$, $C(a)=\int_{\mathbb R}\rho(u)\rho(u+a)\,du$, and $\mathcal T(a)=\int_a^\infty C(v)\,dv$. Write $C_0=C(0)$ and $\mathcal L=\int_0^\infty |\rho'(u)|^2\,du$, using the ordinary derivative for $u>0$. The argument $y$ is always at least the other prime log $x$. The result is distinct from [the separated above-cap pocket](r111-spectral-two-exterior-logs-negative-dickman-pocket.md), which imposes $x\ge(1+\delta)t$.

**Theorem.** There exists a fixed $h>0$ such that the following holds for all sufficiently large $t$. Put $x=t+a$, with $-h\le a\le h$, and scan $y\ge x$. There are unique thresholds $a_-(t)<0<a_+(t)$ in this collar, with

$$
 a_\pm(t)=\pm\frac{2\kappa^2}{t}
       +\frac{8C_0\kappa^2\mp4\mathcal L\kappa^4}{t^2}
       +O(t^{-3}).
 \tag{1}
$$

If $a_-(t)<a<a_+(t)$, the coefficient $\Phi(t;x,y)$ is positive for every $y\ge x$. If $a=a_\pm(t)$, it has exactly one zero, at $y=x+t$, and is positive elsewhere. If $a<a_-(t)$ or $a>a_+(t)$, it has two simple zeros around $y=x+t$ and signs positive, negative, positive in that order. In the latter case, let $s=\operatorname{sgn}(a)$ and use $a_s=a_+$ or $a_-$ accordingly. If the zeros are $y=x+t+q_\pm$, with $q_-<0<q_+$, their displacements satisfy

$$
 |q_\pm|=|a-a_s(t)|\bigl(1+O(|a|+t^{-1})\bigr).
 \tag{2}
$$

There is also a uniform cusp expansion for bounded real $A,D$:

$$
 \begin{split}
 \kappa^2\Phi\!\left(t;t+\frac A t,\,2t+\frac{A+D}{t}\right)
 ={}&\kappa^2+\frac{|D|-|A|}{2}\\
    &+\frac{2C_0(A-D)+\mathcal L(D^2-A^2)/2}{t}
      +O_{A,D}(t^{-2}).
 \end{split}
 \tag{3}
$$

The constant in the error may be taken uniform on each bounded box of $A,D$. In particular for fixed $|A|>2\kappa^2$ the negative interval has boundaries at $D=\pm(|A|-2\kappa^2)+O_A(t^{-1})$. When $A>2\kappa^2$ both logs are above the cap throughout this interval.

## 1. The autocorrelation cusp

On the positive axis $\rho$ is locally absolutely continuous, with derivative zero on $(0,1)$ and $-\rho(u-1)/u$ for $u>1$. This follows from the defining delay equation. The derivative is bounded by one in magnitude, integrable on $(0,\infty)$, and is nondecreasing for $u>1$ from $-1$ towards zero because $\rho$ is nonincreasing and positive. As an almost-everywhere defined function on $\mathbb R$, extend this derivative by zero on the negative axis. It has total variation $2$. It is not the distributional derivative of the zero-extended $\rho$ at $0$; we only differentiate the positive translated argument for shifts $d\ge0$.

For $d\ge0$, differentiation under the correlation integral on the nonnegative side gives $C'(d)=\int_0^\infty\rho(u)\rho'(u+d)\,du$, interpreting the derivative at zero from the right. The bound $|\rho'|\le1$ gives the majorant $\rho(u)$ for the difference quotient, and the possible derivative exception $u+d=1$ has measure zero. Hence $C'_+(0)=\int_0^\infty\rho(u)\rho'(u)\,du=-1/2$, by integrating the derivative of $\rho^2/2$, since $\rho(0)=1$ and $\rho(\infty)=0$.

For $0\le d<1$, the change of variable $v=u+d$ gives $C'(d)=\int_1^\infty \rho(v-d)\rho'(v)\,dv$, since $\rho'=0$ on $(0,1)$. Differentiate again on the same side; the integrable majorant is now $|\rho'(v)|$, and $v-d>0$. Thus $C''(d)=-\int_1^\infty\rho'(v-d)\rho'(v)\,dv$, with the one-sided interpretation at zero. The total variation bound implies $\int_{\mathbb R}|\rho'(v-d)-\rho'(v)|\,dv\le2d$, by integrating the variation measure on translated intervals. Therefore $C''(d)=-\mathcal L+O(d)$ near zero. By evenness,

$$
 C(d)=C_0-\frac{|d|}{2}-\frac{\mathcal L d^2}{2}
                      +O(|d|^3)\qquad (|d|\ \text{small}).
 \tag{4}
$$

Choose $0<h<1/8$ so that $C'(d)\le-1/4$ for $0<d\le2h$. This is possible by the right derivative at zero and the bound on $C''$. On the negative side $C'(d)=-C'(-d)$.

## 2. Global exclusion and exact threshold

Put $b=y-x\ge0$, $q=b-t$, and $Q_t(v)=2\mathcal T(v)+tC(v)$ for $v\ge0$. The exact identities from the two-prime transition analysis are

$$
 \begin{split}
 \kappa^2G_t(z)&=\mathcal T(z-t)-\mathcal T(z+t)
                        -\tfrac t2\{C(z-t)+C(z+t)\}\quad(z\ge0),\\
 \Phi(t;x,y)&=G_t(0)-2G_t(x)-2G_t(y)+2G_t(b)+2G_t(x+y).
 \end{split}
 \tag{5}
$$

In particular $G_t(0)\ge0$ and $G_t(z)\le1$ for nonnegative $z$, by the nonnegative endpoint subtraction from an integral of at most $\kappa^2$. For $|a|\le h$ and all $b\ge0$, the $x$ cap contributes $-2\kappa^2G_t(x)\ge t C(a)-2\kappa^2$, using $\mathcal T(a)\le\kappa^2$. Likewise $-2\kappa^2G_t(y)\ge-2\kappa^2$. The $b$ cap satisfies $2\kappa^2 G_t(b)\ge-t C(q)-Q_t(t+b)$ since $\mathcal T(b-t)\ge0$; here $Q_t(t+b)$ is factorial-small. Finally $x+y\ge 2t-2h$ regardless of $b$, so both endpoint tails of its cap are factorial-small and $2\kappa^2 G_t(x+y)\ge-o(1)$. These claims use the correlation tail bounds in the one- and two-prime analyses, with arguments at least $t-2h$. Consequently, uniformly in $b\ge0$,

$$
 \kappa^2\Phi(t;t+a,t+a+b)
   \ge t\{C(a)-C(b-t)\}-4\kappa^2-o(1).
 \tag{6}
$$

When $|q|\ge2h$, monotonicity and the choice of $h$ give
$C(a)-C(q)\ge C(h)-C(2h)\ge h/4$. For sufficiently large $t$, (6) proves positivity on this entire complement, including the starting point $y=x$.

Inside $|q|\le2h$, both $y=2t+a+q$ and $x+y=3t+2a+q$ are a fixed positive proportion of $t$ above the cap. Their $G_t$ values and derivatives are factorial-small by the inactive-argument bounds of the two-prime analysis. The same holds for $Q_t(t),Q_t(2t+a),Q_t(2t+q)$ and their relevant derivatives. More precisely, with $E_t=(1+t)/(\lfloor t/2\rfloor-1)!$ for large $t$, (5) gives the exact form

$$
 \begin{split}
 U_t(a,q)&:=\kappa^2\Phi(t;t+a,2t+a+q)\\
  &=\kappa^2+2\{\mathcal T(q)-\mathcal T(a)\}
               +t\{C(a)-C(q)\}+\mathcal E_t(a,q),\\
 |\mathcal E_t|+|\partial_a\mathcal E_t|
                  +|\partial_q\mathcal E_t|&\ll E_t.
 \end{split}
 \tag{7}
$$

Indeed $y$ and $x+y$ have lower endpoint distances from the cap at least $t/2$ for large $t$, while the removed $Q_t$ arguments are at least $t$; (5) and the factorial derivative bound for $C'$ apply on those ranges. All these errors are continuously differentiable throughout the collar. The nondifferentiability at $q=0$ of the retained $C(q)$ is not part of the error.

For $0<q\le2h$, (7) gives $\partial_q U_t=-2C(q)-t C'(q)+O(E_t)\gg t$. For $-2h\le q<0$ it gives $\partial_q U_t\ll-t$ by evenness and the choice of $h$. Thus the unique minimum within this window is exactly at $q=0$. At the minimum,

$$
 m_t(a):=U_t(a,0)=\kappa^2+2\int_0^a C(v)\,dv
             +t\{C(a)-C_0\}+\mathcal E_t(a,0).
 \tag{8}
$$

For $a<0$ in the collar it is strictly increasing with derivative $\gg t$, and for $a>0$ strictly decreasing with derivative $\ll-t$, by the sign of $C'(a)$. At zero its value is $\kappa^2+O(E_t)>0$, and at $a=\pm h$ it is negative for large $t$, since $C(h)<C_0$. The two thresholds are the unique roots of $m_t$ on the respective sides. Positivity outside the $q$ window, continuity and strict monotonicity on each side inside it give the complete sign statement and simplicity of the two noncentral zeros. At the thresholds the sole zero is the cusp at $q=0$.

## 3. Expansions and opening law

Both threshold distances from zero are $O(1/t)$ by the size of the derivatives of $m_t$ and its value at zero. For such $a$, (4) and (8) give

$$
 m_t(a)=\kappa^2-\tfrac t2|a|+2C_0 a
                       -\tfrac{t\mathcal L}{2}a^2+O(t^{-2}).
 \tag{9}
$$

For $s=\pm1$, substitute the proposed value $a=s\,2\kappa^2/t+(8C_0\kappa^2-s\,4\mathcal L\kappa^4)/t^2$. The constant and $1/t$ terms cancel in (9). The derivative lower bound on each side converts this $O(t^{-2})$ residual to location error $O(t^{-3})$, proving (1).

If $a$ is outside the thresholds and the zeros are $q_\pm$, the derivative bounds just proved give $|q_\pm|\ll |a-a_s|$ by comparison with the depth $-m_t(a)$; also $|m_t'(a)|\ll t$ on both sides. More precisely, (4), or the one-sided derivative estimates leading to it, give $|m_t'(v)|=t/2+O(t|v|+1)$ between $a_s$ and $a$, and $|\partial_q U_t(a,q)|=t/2+O(t|q|+1)$ between zero and either noncentral root. Both error factors are $O(t|a|+1)$, since $|a-a_s|\le|a|$ and $|q_\pm|\ll|a-a_s|$. Integrating these slopes and using their uniform positive lower bounds gives (2), with no lower bound imposed on the distance to the exact threshold. Equation (3) follows by substituting $a=A/t,q=D/t$ in (7), using (4) and $2\{\mathcal T(q)-\mathcal T(a)\}=2C_0(a-q)+O(a^2+q^2)$. When fixed $|A|>2\kappa^2$, (1) and (2) imply the stated locations in the scaled $D$-variable.

## 4. Fixed-parameter arithmetic consequence

Retain all hypotheses of the original finite ordinary profile: in particular the actual odd Page conductor if one exists, its bounded missing part with two primes, the complete primorial family, the fixed tests, and the positively scaled primorial parameter. Suppose $t_*=2Bg/\ell\to t$ for a fixed sufficiently large $t$, and the actual scaled prime logs converge to $x,y$ in the collar's stated range. At any such limiting point with $\Phi(t;x,y)\ne0$, the actual ordinary coefficient is eventually bounded away from zero with its deterministic sign $s$, by continuity. In particular the above-cap subcase of the negative interval yields $s=-1$ even when both prime logs exceed the literal cap.

If also $(1-\beta)G\le C_*\log G$ with fixed $C_*$ and $\chi(-1)=-s$, then $P_1(M)>0$ by [the matched exceptional comparison](r100-spectral-matched-ramanujan-exceptional-mean.md), and the ordinary and exceptional terms reinforce. The original finite-profile formula gives the sign $s$ and magnitude $\gg\mathcal R+HP_1(M)$ for the genuine matched parity mean, for either the full mixed strip or its original moving-major integral. There is no claim at a zero, in the competing-sign case, for a growing arithmetic cutoff, for an individual target, for the full signed shell, or for Weak S. Neither Dirichlet GRH nor an external zero-gap result is assumed, and no Page-zero existence is asserted.
