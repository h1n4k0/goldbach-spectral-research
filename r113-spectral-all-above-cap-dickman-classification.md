# Exact sign classification for every smaller prime log above the Dickman cap

**Scope.** This joins the cap-adjacent cusp and the separated above-cap pocket for the ordinary two-missing-prime Dickman profile. It classifies the sign for all real $y\ge x\ge t$ at every sufficiently large fixed cap $t$, with no gap in the smaller-log range. The negative intervals are strictly nested as $x$ moves outward at fixed log difference. The arithmetic consequence remains a fixed-parameter sign of the genuine matched parity mean when the ordinary and exceptional signs reinforce. This is not an arithmetic autocorrelation theorem or a growing-cutoff result.

Use the notation of [the finite ordinary profile](r108-spectral-finite-matched-ordinary-dickman-profile.md) and [the two-prime transition analysis](r110-spectral-three-two-prime-dickman-transitions.md). Thus $C(d)=\int_{\mathbb R}\rho(u)\rho(u+d)\,du$ for the usual cumulative Dickman function, zero on the negative half-line, $\kappa=\int_0^\infty \rho$, and $\mathcal T(d)=\int_d^\infty C(v)\,dv$. The evenized cap $G_t$ is normalized by $\kappa^2$. For $b=y-x\ge0$, define the function on the difference axis

$$
 \mathcal P_t(x,b)=\Phi(t;x,x+b)
 =G_t(0)-2G_t(x)-2G_t(x+b)+2G_t(b)+2G_t(2x+b).
 \tag{1}
$$

Let $a_+(t)$ be the positive threshold of [the cap-adjacent cusp](r112-spectral-dickman-cap-cusp-opening-threshold.md), and set $x_c(t)=t+a_+(t)$.

**Theorem.** For all sufficiently large $t$, the following holds on the entire region $x\ge t$, $b\ge0$.

- If $t\le x<x_c(t)$, then $\mathcal P_t(x,b)>0$ for every $b$. At $x=x_c(t)$ it vanishes exactly at $b=t$ and is positive elsewhere. In particular $x_c(t)=t+2\kappa^2/t+O(t^{-2})$, with the second term in the cusp theorem unchanged.
- If $x>x_c(t)$, there are exactly two simple zeros $b_-(t,x)<t<b_+(t,x)$. The sign is negative strictly between them and positive outside. The functions $b_-$ and $b_+$ of $x$ are continuously differentiable and strictly decreasing and increasing, respectively.
- Write $J_t(b)=G_t(0)+2G_t(b)$ and let $b_\pm^\infty(t)$ be its inner and outer roots from [the separated above-cap analysis](r111-spectral-two-exterior-logs-negative-dickman-pocket.md), Section 2. The finite negative intervals are strictly contained in $(b_-^\infty,b_+^\infty)$ and increase to it as $x\to\infty$. Quantitatively, for $x>x_c(t)$,

$$
 0<b_-(t,x)-b_-^\infty(t),\ b_+^\infty(t)-b_+(t,x)
             \ll -G_t(x)
 \tag{2}
$$

with an absolute implied constant for sufficiently large $t$. The nesting is on the difference axis $b=y-x$, not on the unshifted $y$ axis.

## 1. Relative factorial decay and exterior monotonicity

The correlation is even and nonincreasing on the nonnegative axis. We first prove that there is an absolute $c>0$ such that

$$
 -C'_+(d)\ge c\, C(d)\qquad(d\ge0).
 \tag{3}
$$

Here $C'_+(0)$ is the right derivative and other derivatives are ordinary. From the Dickman equation the derivative of $\rho(u+d)$ is bounded in absolute value by one on the positive axis and is negative for $u+d>1$. Thus the derivative of the correlation is the integral of $\rho(u)\rho'(u+d)$ over $u\ge0$, with an integrable majorant $\rho(u)$, and is strictly negative for every $d\ge0$. Its right restriction is continuous, by dominated convergence and the fact that the exceptional derivative point $u+d=1$ has measure zero. Its ratio against $C(d)>0$ has a positive lower bound on each compact interval. For large $d$, the separated above-cap analysis, (4), gives $-C'(d)=\xi(d)C(d)(1+O(d^{-1}))$ with $\xi(d)\to\infty$. This proves (3) uniformly.

We also need decay relative to an arbitrarily small value of $C(d)$, not merely an absolute tail. For real $L\ge2$ and any $d\ge0$,

$$
 C(d+L)\le\frac{C(d)}{\lfloor L\rfloor!},\qquad
 |C'(d+L)|\le\frac{C(d)}{\lfloor L\rfloor!}.
 \tag{4}
$$

Indeed the Dickman identity $v\rho(v)=\int_{v-1}^v\rho(u)\,du$ for $v\ge1$ implies $\rho(u+j)\le\rho(u)/j!$ for $u\ge0$ and integer $j\ge0$, by monotonicity and iteration. If $j=\lfloor L\rfloor$, the delay equation also yields
$|\rho'(u+L)|=\rho(u+L-1)/(u+L)\le \rho(u+j-1)/j\le\rho(u)/j!$. Apply both estimates with $u$ replaced by $u+d$ and integrate against $\rho(u)$.

For $z=t+a$ with $a\ge0$, the exact evenized cap identity gives

$$
 2\kappa^2 G_t'(z)
 =2\{C(2t+a)-C(a)\}-t\{C'(a)+C'(2t+a)\},
 \tag{5}
$$

with the right derivative at $a=0$. By (3) and the nonpositive derivatives, it is at least $(ct-2)C(a)$. Also $G_t(z)\to0$ as $z\to\infty$, since $C$ and its integrable tail vanish at infinity. Consequently $G_t$ is strictly increasing and strictly negative on the entire exterior half-line $z\ge t$, for sufficiently large $t$. Moreover, for $z\ge t,L\ge2$, (4) bounds the absolute derivative at $z+L$ by

$$
 2\kappa^2 |G_t'(z+L)|
 \le (4+2t)\,\frac{C(z-t)}{\lfloor L\rfloor!}.
 \tag{6}
$$

In (1), differentiate in $x$ at fixed $b$. The sum apart from $G_t(0)+2G_t(b)$ has derivative
$-2G_t'(x)-2G_t'(x+b)+4G_t'(2x+b)$.
Since $2x+b=x+L$ with $L=x+b\ge t$, the last term is uniformly factorial-small relative to $G_t'(x)>0$ by (5)--(6), even as $x$ is unbounded. The middle term is nonpositive. Hence

$$
 \partial_x \mathcal P_t(x,b)<0\qquad (x\ge t,\ b\ge0)
 \tag{7}
$$

with a right derivative at $x=t$. In addition, the exterior ordering from (5) gives $G_t(x)\le G_t(x+b)\le G_t(2x+b)<0$ and therefore

$$
 0< \mathcal P_t(x,b)-J_t(b)
   =-2G_t(x)+2\{G_t(2x+b)-G_t(x+b)\}\le -4G_t(x).
 \tag{8}
$$

The bound is uniform for all $b$.

## 2. Confine all possible zeros and fix the derivative directions

As in the one- and two-prime analyses, let $\lambda_*(t)$ denote the one-prime zero, $d_t=t-\lambda_*(t)$ and $\xi_t=\xi(d_t)$, where $e^{\xi(d)}=1+d\xi(d)$. By the correlation calibration and local ratio there,

$$
 d_*:=d_t+3/\xi_t=o(t),\qquad
 tC(d_*)=\kappa^2e^{-3}\bigl(1+O(d_t^{-1})\bigr).
 \tag{9}
$$

In particular $d_*\to\infty$. For $d=|b-t|\ge d_*$, the exact formula for $J_t$ in the separated above-cap analysis, (6), gives
$\kappa^2 J_t(b)\ge \kappa^2-(t+4)C(d)-o(1)$, uniformly in $b$. This uses $\mathcal T(d)\le2C(d)$ and factorial-small far tails at $t$ and $t+b$. By monotonicity of $C$ and (9), $J_t(b)>1/2$ there for sufficiently large $t$. Equation (8) gives strict positivity of the full profile outside $|b-t|<d_*$.

On the inside part $t-d_*\le b<t$, put $d=t-b>0$. Differentiating the exact cap gives

$$
 2\kappa^2 G_t'(b)
   = -2C(d)+t C'(d)
      +2C(t+b)-t C'(t+b).
 \tag{10}
$$

On the outside part $t<b\le t+d_*$, use $d=b-t>0$ and (5) in the same form except that the first derivative term is $-tC'(d)$. In the inside case the first two terms of (10) are at most $-ct C(d)$; in the outside case the first two are at least $(ct-2)C(d)$. The far terms $2C(t+b)-t C'(t+b)$ are factorial-small uniformly, since $t+b\ge2t-d_*$, using for instance (4) from zero. Also $tC(d)\ge tC(d_*)$ is bounded away from zero by (9). These facts give derivative bounds with absolute positive margin: $G_t'(b)\le-c_0$ on the inside side of the collar and $G_t'(b)\ge c_0$ on the outside side, where $c_0>0$ is fixed.

In the same collar $x+b\ge 2t-d_*$, and $2x+b$ is even farther above the cap, uniformly in $x\ge t$. Their $G_t'$ terms are again factorial-small by (6) or (4)--(5). Thus differentiating (1) in $b$ proves that $\mathcal P_t(x,b)$ is strictly decreasing with slope bounded away from zero on $[t-d_*,t)$, and strictly increasing with slope bounded away from zero on $(t,t+d_*]$. It is continuous at $b=t$; no differentiability there is asserted. The one-sided slopes and positivity outside the collar give the global zero structure once the sign of $\mathcal P_t(x,t)$ is known.

## 3. Complete classification and nesting

By the cap-adjacent cusp theorem $\mathcal P_t(x_c(t),t)=0$. Equation (7) extends uniqueness and determines the sign of $\mathcal P_t(x,t)$ on all $x\ge t$: it is positive below $x_c$, zero exactly there, and negative above it. Together with the preceding collar result this gives all asserted signs and zero counts. The noncentral zero on each side is simple. In a neighborhood of either such zero for $x>x_c$, the cap terms are continuously differentiable: the endpoint arguments avoid the only relevant cusp at zero, and $C'$ is continuous for all nonzero lags. The implicit function theorem, (7), and the opposite signs of the $b$ derivatives give $\partial_x b_-<0<\partial_x b_+$.

For comparison with the limiting interval, $J_t$ has one root on each side of $t$ in the same collar and has the corresponding derivative lower bounds there by (10) and its exterior counterpart. This also follows directly from the separated above-cap proof of the $J_t$ roots. Since $\mathcal P_t-J_t$ is strictly positive by (8), $J_t$ is negative wherever $\mathcal P_t$ is nonpositive when $x>x_c$. The two roots of the finite profile thus lie strictly inside the limiting interval. At either finite root, $|J_t(b_\pm)|\le-4G_t(x)$ by (8); the derivative lower bound between it and the corresponding root of $J_t$ proves (2). As $G_t(x)\to0$, the two bounds in (2) show convergence to the endpoints of the limiting open interval. The strict derivatives in $x$ give the claimed nesting.

## 4. Fixed-parameter arithmetic consequence

Retain the assumptions of the original finite ordinary profile, with the actual odd Page conductor if one occurs, its two-prime missing part, the complete primorial family, the fixed weights and the positively scaled primorial parameter. If $t_*=2Bg/\ell\to t$ for fixed sufficiently large $t$ and the two actual scaled prime logs converge to $x,y$ with $y\ge x\ge t$, the sign classification gives an eventual coefficient of the same nonzero sign as $\Phi(t;x,y)$ at any nonzero point, by continuity. If the ordinary sign is $s$ and also $(1-\beta)G\le C_*\log G$ with fixed $C_*$ and $\chi(-1)=-s$, then $P_1(M)>0$ by [the matched exceptional comparison](r100-spectral-matched-ramanujan-exceptional-mean.md). The two terms of the genuine finite-profile mean reinforce, giving sign $s$ and magnitude $\gg \mathcal R+HP_1(M)$ for the full mixed strip or its original moving-major integral. No claim is made at a zero, in the competing-sign case, for an arithmetic cutoff growing with $Y$, for an individual target, for the full signed shell, or for Weak S. No Page-zero existence is asserted. Neither Dirichlet GRH nor an external zero-gap result is used.
