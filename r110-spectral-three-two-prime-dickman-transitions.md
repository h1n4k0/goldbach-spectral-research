# Three sign transitions in the two-prime finite Dickman profile

**Scope.** For one fixed sub-half-cap prime log, the ordinary two-missing-prime Dickman profile has exactly three sign transitions as the second log increases, for every sufficiently large fixed cap. Their locations and signed transition profiles are given below. This refines the distant-from-boundary signed count, not the pointwise exceptional-slice analysis. The arithmetic consequence is for the genuine matched parity mean at fixed parameters when the ordinary and exceptional signs reinforce. The large-cap transition limit is deterministic only; it is not a growing-cutoff arithmetic estimate.

Use the notation of [the original finite Dickman profile](r108-spectral-finite-matched-ordinary-dickman-profile.md) and [the one-prime sign threshold](r109-spectral-finite-dickman-cap-sign-threshold.md). In particular, $\rho$ is the usual cumulative Dickman function, zero on the negative axis; $\kappa=\int_0^\infty\rho$, $C(a)=\int_{\mathbb R}\rho(u)\rho(u+a)\,du$, and $\mathcal T(a)=\int_a^\infty C(v)\,dv$. For the evenized cap $h_t(a)$ of the one-prime proof put $G_t(a)=h_t(a)/\kappa^2$. For $a\ge0$,

$$
 G_t(a)=\frac{\mathcal T(a-t)-\mathcal T(a+t)
              -\frac t2\{C(a-t)+C(a+t)\}}{\kappa^2}.
 \tag{1}
$$

Write $F_t(a)=2G_t(a)-G_t(0)=\Phi(t;a)$. The previous result gives its unique zero $\lambda_*(t)\in(1,t-1)$ for $t\ge80$. Set $d_t=t-\lambda_*(t)$. Then $d_t\to\infty$, $d_t\sim\log t/\log\log t$ and $t C(d_t)\to\kappa^2$.

For $d>1$, let $\xi(d)$ be the positive solution of $e^\xi=1+d\xi$, and put $\xi_t=\xi(d_t)$. In particular $\xi_t\sim\log\log t$.

**Theorem 1 (the one-prime transition shape).** For each fixed $A<\infty$, uniformly for $|v|\le A$ as $t\to\infty$,

$$
 F_t\!\left(\lambda_*(t)+\frac v{\xi_t}\right)
        =1-e^v+O_A(d_t^{-1}).
 \tag{2}
$$

On the same interval of arguments, $-F_t'(a)\gg_A \xi_t$ for all sufficiently large $t$.

**Theorem 2 (three two-prime sign transitions).** Fix $0<c_1<c_2<1/2$ and let
$c_1t\le x\le c_2t$. With $\delta=\min(c_1,1-2c_2)/10$ and
$E_t=(1+t)/(\lfloor\delta t\rfloor-1)!$ for sufficiently large $t$, the profile $\Phi(t;x,y)$ on $y\ge x$ has exactly three zeros $y_1<y_2<y_3$. Uniformly in $x$,

$$
 y_j=\lambda_*(t)+(j-2)x+O_{c_1,c_2}(E_t/\xi_t),
 \qquad j=1,2,3.
 \tag{3}
$$

The signs on the four successive intervals are positive, negative, positive and negative, starting at $y=x$. In each of the three transition windows,

$$
 \Phi\!\left(t;x,\lambda_*(t)+(j-2)x+\frac v{\xi_t}\right)
 =(-1)^{j-1}(1-e^v)+O_{c_1,c_2,A}(d_t^{-1})
 \quad (|v|\le A).
 \tag{4}
$$

Thus the first and third transitions are positive to negative, and the middle one is negative to positive. All three occur before their respective literal endpoints $t-x,t,t+x$ by the common Dickman distance $d_t$ up to the error in (3).

## 1. Correlation tail at the transition scale

Use the primary Dickman estimate of [Hildebrand and Tenenbaum, Section 2, Lemma 2.2 and Corollary 2.4 (2.7)](https://www.numdam.org/item/JTNB_1993__5_2_411_0.pdf), printed pages 423--425. In its notation $\xi(d)\sim\log d$, $\xi'(d)\asymp d^{-1}$, and uniformly for $|u|\le d/2$ as $d\to\infty$,

$$
 \frac{\rho(d+u)}{\rho(d)}
   =\exp\{-u\xi(d)+O((1+u^2)/d)\}.
 \tag{5}
$$

These are ordinary Dickman estimates, with no Dirichlet-zero hypothesis. To pass to $C(d)$, integrate over $0\le u\le1$ using $\rho(u)=1$ there. By (5) that integral is
$\rho(d)(1-e^{-\xi(d)})/\xi(d)$ times $1+O(1/d)$. The remaining part is at most $\kappa\rho(d+1)$ by monotonicity. The ratio of this bound to $\rho(d)/\xi(d)$ is $O(\xi(d)e^{-\xi(d)})=O(1/d)$, since $e^{\xi(d)}=1+d\xi(d)$. It follows that

$$
 C(d)=\frac{\rho(d)}{\xi(d)}(1+O(d^{-1})),\qquad
 \frac{C(d+v/\xi(d))}{C(d)}=e^{-v}(1+O_A(d^{-1}))
       \quad (|v|\le A).
 \tag{6}
$$

For the second formula use (5) again and $\xi'(d)\ll1/d$ on the bounded interval between the two arguments. Also, for $d\ge1$ one has $\mathcal T(d)\le2C(d)$. In fact the Dickman integral equation gives $\rho(u+1)\le \rho(u)/(u+1)$ for $u\ge1$. Thus $C(d+n)\le C(d)/(d+1)^n$ for integer $n\ge0$; sum these bounds using monotonicity of $C$ on consecutive unit intervals.

For $d\ge2$ the derivative can be taken inside the integral; the derivative of $\rho(d+u)$ is bounded in magnitude by $1/d$ for $u\ge0$, giving an integrable dominating function after multiplication by $\rho(u)$. The delay equation and (5) at shift $-1$ give, uniformly for $r\ge d\to\infty$, $-\rho'(r)/\rho(r)=(\xi(r)+1/r)(1+O(1/r))$. Since $\xi$ increases, this implies

$$
 -C'(d)\gg \xi(d) C(d) \quad(d\ \text{large}), \qquad
 |C'(d)|\le\kappa\,\frac{\rho(d-1)}d
       \quad(d\ge2).
 \tag{7}
$$

The upper bound follows directly from monotonicity in the delay equation and is also useful well away from the transition.

## 2. Proof of the one-prime shape and isolation of its zero

For $0\le a<t$, let $d=t-a$. Using evenness of $C$ in (1) yields the exact expression

$$
 \begin{split}
 \kappa^2 F_t(a)={}&\kappa^2-2\mathcal T(d)-t C(d)\\
 &-2\mathcal T(t+a)-t C(t+a)+2\mathcal T(t)+t C(t).
 \end{split}
 \tag{8}
$$

By the previous one-prime result, $t C(d_t)\to\kappa^2$. Equation (8) at its zero, with $\mathcal T(d_t)\le 2C(d_t)$ and the factorial bounds for $C,\mathcal T$ at $t$ or beyond, improves this to $t C(d_t)=\kappa^2+O(t^{-1})$. For $a=\lambda_*(t)+v/\xi_t$, its gap is $d=d_t-v/\xi_t$ and (6) gives $t C(d)=\kappa^2 e^v(1+O_A(d_t^{-1}))$. The remaining tails in (8) are then $O_A(t^{-1})$. This gives (2).

For the derivative, at these arguments with $d>1$,

$$
 \kappa^2 F_t'(a)
   =2\{C(t+a)-C(d)\}-t\{C'(t+a)-C'(d)\}.
$$

The first brace is nonpositive. By (7), $-t C'(d)\gg_A \xi_t$; here $\xi(d)\asymp \xi_t$ and $t C(d)\asymp_A1$. The upper bound in (7) and the factorial decay of $\rho$ make $t|C'(t+a)|=o(1)$. This proves the derivative assertion.

We will use the additional uniform separation $|F_t(a)|\gg1$ for all $a\ge0$ with $|a-\lambda_*(t)|\ge\xi_t^{-1}$, as $t$ becomes large. On $[0,t-1]$ this follows from the strictly decreasing one-prime profile and the nonzero limits at $v=-1,1$ in (2). For $t-1\le a\le t+1$ equation (1) gives $G_t(a)\le1-t C(1)/(2\kappa^2)$, and $G_t(0)>0$. For $a\ge t+1$, the previous proof's equation (5) bounds $\kappa^2F_t(a)$ above by $-2\int_0^1 C+2\mathcal T(t)+tC(t)\le-1+o(1)$. This verifies the separation on the rest of the half-line without assuming monotonicity there.

## 3. Proof of the exact two-prime sign pattern

For $y\ge x$ the nine signed terms, paired into opposite shifts, give the exact identity

$$
 \Phi(t;x,y)=G_t(0)-2G_t(x)-2G_t(y)
                      +2G_t(y-x)+2G_t(y+x).
 \tag{9}
$$

For a nonnegative argument $a$ whose distance from $t$ is at least $\delta t$, the factorial tail bounds in the one-prime proof yield
$G_t(a)=\mathbf 1_{a<t}+O(E_t)$. Its derivative has magnitude $O(E_t)$ there as well. To see the latter, differentiate (1), where both endpoints have absolute value at least $\delta t>1$. The two $C$ terms have the factorial bound and the $tC'$ terms use (7) and $\rho(u)\le1/\lfloor u\rfloor!$; the smallest possible factorial index is at least $\lfloor\delta t\rfloor-1$. At $a=0$ one may use the right derivative, though that constant term of (9) does not vary.

Center three closed windows of radius $\delta t$ at $t-x,t,t+x$ on the $y$ line. They are disjoint and lie strictly to the right of $x$: consecutive centers are separated by $x\ge 10\delta t$, and $t-2x\ge 10\delta t$. Throughout the first window, $y+x$ is the only variable argument in (9) that can be within $\delta t$ of $t$; the other arguments are inside the cap. In the second window only $y$ is active: $x,y-x$ are inside and $y+x$ is outside. In the third window only $y-x$ is active: $x$ is inside and $y,y+x$ are outside. These assertions follow by subtracting each window's center and using $x\ge10\delta t$, $t-2x\ge10\delta t$. In these windows respectively, (9) therefore equals

$$
 F_t(y+x)+O(E_t),\qquad -F_t(y)+O(E_t),\qquad
 F_t(y-x)+O(E_t).
 \tag{10}
$$

The errors each have derivative $O(E_t)$ with respect to $y$ by the same inactive-argument bounds. Outside all three windows, every shift in (9) stays at least $\delta t$ from the cap endpoint, and substituting the indicators gives $1,-1,1,-1$ on the four consecutive complementary intervals. The $O(E_t)$ error there cannot change these signs.

Within each window the active argument ranges from $t-\delta t$ to $t+\delta t$. Since $d_t=o(t)$ and $\xi_t^{-1}=o(t)$, its entire central interval $|a-\lambda_*(t)|\le\xi_t^{-1}$ lies strictly within the window for large $t$. The uniform separation following (8) excludes zeros elsewhere in it by (10). At the ends of the central interval, (2) gives opposite signs of fixed positive margins; throughout it the derivative bound from (2) and the $O(E_t)$ derivative error in (10) give strict monotonicity in the stated direction. There is exactly one simple zero in each window by continuity. Evaluating (10) at active argument $\lambda_*(t)$ gives an error $O(E_t)$, and the derivative bound then locates the zero within $O(E_t/\xi_t)$ of that point in the active coordinate. This proves (3) and the four signs. For fixed $A$, the full bounded-$v$ windows in (4) also lie strictly inside the respective wide windows for large $t$; combine (2) and (10) there to obtain (4).

## 4. Arithmetic consequence at fixed parameters

Retain all hypotheses and notation of the original finite-profile result. In particular the odd Page conductor is actual if one occurs, the complete primorial family is $K_z\mid N$, the scaled primorial parameter stays in its asserted positive range, and the missing conductor part is within its polynomial-in-$G$ bound with bounded arity. For two actual missing primes, take the scaled prime logs to converge to $x,y$ with $y\ge x$, $c_1t\le x\le c_2t$, and $t_*=2Bg/\ell\to t$ for a fixed $t$ large enough for Theorem 2. If $y$ is not one of the exact zeros in (3), the finite ordinary coefficient is bounded away from zero with the indicated sign $s$, by continuity of the Dickman profile. An analogous conclusion uses (2) and the exact one-prime threshold for one missing prime.

If also $(1-\beta)G\le C_*\log G$ for fixed $C_*$, then $P_1(M)>0$ in [the matched exceptional comparison](r100-spectral-matched-ramanujan-exceptional-mean.md). Under $\chi(-1)=-s$, the genuine matched parity mean has sign $s$ and magnitude $\gg\mathcal R+HP_1(M)$, for either the full mixed strip or its original moving-major integral: the two signed main terms of the original finite-profile formula reinforce and dominate its $o(\mathcal R)$ error. There is no asserted conclusion at a zero, in the competing-sign case, for a growing arithmetic cutoff, for an individual target, for the full signed shell, or for Weak S. This neither assumes Dirichlet GRH nor asserts Page-zero existence.
