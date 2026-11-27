# The finite Dickman cap changes sign before the one-prime boundary

**Scope.** This determines the entire one-missing-prime sign of the ordinary finite Dickman profile at each sufficiently large fixed cutoff, and gives additional signs for two and three missing primes. The one-prime transition occurs before the cap boundary by an asymptotically specified distance in the deterministic profile. The application concerns the genuine odd-conductor matched parity mean, with the hypotheses of the previous finite-cap result and with reinforcement of the exceptional term. No growing-cutoff arithmetic limit, individual-target conclusion, full signed-shell bound, Weak S, or existence of a Page zero is asserted.

Use the notation of [the finite ordinary Dickman profile](r108-spectral-finite-matched-ordinary-dickman-profile.md). Thus $\rho$ is the usual cumulative Dickman function, extended by zero on the negative axis, $\kappa=\int_0^\infty\rho$, and $C(a)=\int_{\mathbb R}\rho(u)\rho(u+a)\,du$. Let $\mathcal H$ and $\Phi$ have the same normalization as in that proof. Its arithmetic regime has $\ell=\log z$, $g=\log\log Y$, $t_*=2Bg/\ell$ and $\lambda_i=(\log p_i)/\ell$ for the actual missing primes $p_i>z$.

**Theorem 1 (one missing prime).** For each real $t\ge80$ there is exactly one $\lambda_*(t)>1$ at which $\Phi(t;\lambda)=0$ on $\lambda\ge0$. It satisfies $\lambda_*(t)<t-1$, and the profile is strictly positive for $0\le\lambda<\lambda_*(t)$ and strictly negative for $\lambda>\lambda_*(t)$. With $d_t=t-\lambda_*(t)$, the deterministic limit as $t\to\infty$ is

$$
  t C(d_t)\longrightarrow\kappa^2,\qquad
  d_t=(1+o(1))\frac{\log t}{\log\log t}.
  \tag{1}
$$

**Theorem 2 (several missing primes).** For $m\ge0$, let $a_\epsilon=\sum_i\epsilon_i\lambda_i$ and $\sigma_\epsilon=(-1)^{\#\{i:\epsilon_i=0\}}$, where $\epsilon\in\{-1,0,1\}^m$. If an integer $q\ge1$ satisfies $\big||a_\epsilon|-t\big|\ge q$ for every $\epsilon$, define the signed cap count

$$
 V(t;\lambda)=\sum_{\epsilon:\,|a_\epsilon|<t}\sigma_\epsilon .
$$

Then $V$ is an odd integer and

$$
 |\Phi(t;\lambda)-V(t;\lambda)|\le
             \frac{3^m(4+t)}{q!}.
 \tag{2}
$$

In particular the sign of $V$ is the sign of $\Phi$ when the bound is less than one. For instance, at $t\ge80$ the following new regimes give coefficients with absolute value at least $1/2$.

- Two prime logs: $3t/5\le\lambda_1\le\lambda_2\le7t/10$ give $\Phi\le-1/2$. This has the opposite sign to the very-far separated two-prime regime.
- Three prime logs: for a real $u\ge2t$, let $|\lambda_i-iu|\le t/12$ for $i=1,2,3$. Then $\Phi\ge1/2$, the opposite sign to the very-far separated three-prime regime. Here the pair of opposite signed relations near $\lambda_1+\lambda_2-\lambda_3=0$ is inside the finite cap; it is not discarded as a tail.

**Arithmetic consequence.** Retain all hypotheses of the finite ordinary profile, including the fixed positive primorial scale, $D\le G^{J_1}$ of bounded arity, the complete $K_z$-multiple family, its fixed tests and the actual odd Page conductor. Retain its notation $\mathcal R,H,M,P_1(M),\gamma,X_\pm$, where $X_\pm$ are either the genuine full mixed-strip sums or their original moving-major integrals. Suppose additionally $(1-\beta)G\le C_*\log G$ with fixed $C_*$, so $P_1(M)>0$ by [the matched exceptional comparison](r100-spectral-matched-ramanujan-exceptional-mean.md). With one missing prime, if $t_*\to t\ge80$ and $\lambda_1\to\lambda\ne\lambda_*(t)$, take $s=+1$ below this threshold and $s=-1$ above. For either multi-prime regime just given, imposed on the actual $t_*,\lambda_i$ for all sufficiently large $Y$, take $s$ to be its stated sign. Whenever $\chi(-1)=-s$, the actual matched parity mean has sign $s$ and magnitude $\gg \mathcal R+HP_1(M)$. These are implications for eligible label and zero data only, not an existence statement or a sign in the competing case. No Dirichlet GRH or external zero-gap result is used.

## 1. The even cap and its tails

The Dickman equation and normalization imply $u\rho(u)=\int_{u-1}^u\rho(v)\,dv$ for $u\ge1$: the two sides have equal derivatives above $1$ and agree at $1$. This identity precludes a first zero, since the preceding interval would then have positive integral. The delay equation in turn gives that $\rho$ is nonincreasing and positive. Iterating $\rho(u)\le\rho(u-1)/u$ yields $\rho(u)\le1/\lfloor u\rfloor!$ for $u\ge0$. In particular $1\le\kappa\le\sum_{n\ge0}1/n!<3$. The correlation is even, continuous by continuity of translations in $L^2$, nonnegative and nonincreasing on $[0,\infty)$, with total integral $\kappa^2$ by Tonelli. Its restriction to $[1,\infty)$ is strictly decreasing and convex. Indeed $\rho$ is strictly decreasing and convex there: on $u>1$ its derivative is $-\rho(u-1)/u$, which is negative and increasing. Integrate the translated function $\rho(u+a)$ against nonnegative $\rho(u)$ on $u\ge0$. With $\mathcal T(x)=\int_x^\infty C(v)\,dv$ for real $x$, for $d\ge1$ the factorial estimates give

$$
 C(d)\le\frac{\kappa}{\lfloor d\rfloor!},\qquad
 \mathcal T(d)\le\frac{2\kappa}{\lfloor d\rfloor!}.
 \tag{3}
$$

For the second inequality use $\sum_{n\ge\lfloor d\rfloor}1/n!\le 2/\lfloor d\rfloor!$. Also $C(v)\ge1-v$ for $0\le v\le1$, by the overlap where both arguments are at most $1$, and $C(1)\ge1/4$, by integrating over $0\le u\le1/2$ where $\rho(1+u)=1-\log(1+u)\ge1/2$.

Define the evenized cap $h_t(a)=(\mathcal H(t,a)+\mathcal H(t,-a))/2$. The signed weights are invariant under $\epsilon\mapsto-\epsilon$, so $\Phi=\kappa^{-2}\sum_\epsilon\sigma_\epsilon h_t(a_\epsilon)$. For $b=|a|$, direct integration gives

$$
 h_t(a)=\int_{b-t}^{b+t}C(v)\,dv-\frac{t}{2}\big(C(b-t)+C(b+t)\big)
       =\mathcal T(b-t)-\mathcal T(b+t)
                        -\frac{t}{2}\big(C(b-t)+C(b+t)\big).
 \tag{4}
$$

If $|b-t|\ge q$, then $b+t\ge q$, and evenness gives $\mathcal T(-d)=\kappa^2-\mathcal T(d)$. Apply (3) to both ends of (4). After division by $\kappa^2$, the difference from $\mathbf1_{b<t}$ is at most $(4+t)/q!$, since $\kappa\ge1$. This proves (2). The zero vector contributes $(-1)^m$; all other vectors come in opposite pairs, proving oddness.

In the two-prime example the centered vector contributes $+1$, the two pairs of single-prime vectors contribute $-4$, the difference pair contributes $+2$, and the sum pair is outside. Thus $V=-1$; every shift is separated from the cap boundary by at least $t/5$. In the three-prime example consider the integer $\epsilon_1+2\epsilon_2+3\epsilon_3$. Its zero vectors are the centered one and the two opposite relation vectors $(1,1,-1),(-1,-1,1)$. Their actual shifts have absolute value at most $t/4$, whereas all others have absolute value at least $u-t/4\ge7t/4$. Thus $V=-1+2=1$ with distance at least $3t/4$ from the cap boundary. For $t\ge80$, the error bound (2) is less than $1/2$ using $q=\lfloor t/5\rfloor$ and $q=\lfloor3t/4\rfloor$, respectively. For example both estimates follow from $t+4<5q+9$ for their respective $q\ge16$ and $27(5q+9)/q!<1/2$; the latter decreases for $q\ge16$.

## 2. The one-prime threshold

Here $\kappa^2\Phi(t;\lambda)=2h_t(\lambda)-h_t(0)$. The centered value $h_t(0)=2\int_0^t C-tC(t)\ge tC(t)>0$. For $0<\lambda\le t-1$ the integral on the right of (4) is strictly decreasing as a function of $\lambda$: its derivative is $C(t+\lambda)-C(t-\lambda)<0$ by the strict decrease of $C$ on $[1,\infty)$. The function $C(t-\lambda)+C(t+\lambda)$ is even and convex on $[-(t-1),t-1]$, so is nondecreasing on $[0,t-1]$. It follows that $h_t(\lambda)$ is strictly decreasing there.

For $t-1\le\lambda\le t+1$, equation (4) gives $h_t(\lambda)\le\kappa^2-tC(1)/2<0$ if $t\ge80$: use $\kappa<3$ and $C(1)\ge1/4$. For $\lambda\ge t+1$ the cap integral is at most $\mathcal T(1)$; therefore

$$
 \begin{split}
 2h_t(\lambda)-h_t(0)
     &\le 2\mathcal T(1)-h_t(0)\\
     &= -2\int_0^1 C(v)\,dv+2\mathcal T(t)+tC(t)<0 .
 \end{split}
 \tag{5}
$$

The last strictness uses $2\int_0^1 C\ge1$ and (3), since $3(4+t)/\lfloor t\rfloor!<1$ for $t\ge80$. At $\lambda=1$, all three shifts are inside the cap, with $V=1$ and $q=\lfloor t-1\rfloor$ in (2); hence $\Phi(t;1)>0$. Continuity, strict decrease up to $t-1$, and (5) prove the unique zero and the full sign statement for $t\ge80$.

For each fixed $D_0\ge1$, $h_t(t-D_0)\le\kappa^2-tC(D_0)/2$ for $t>D_0$, so is eventually negative. This and the strict sign already proved give $d_t>D_0$ eventually, hence $d_t\to\infty$. The exact root equation using (4) is

$$
 0=\kappa^2-2\mathcal T(d_t)-tC(d_t)
   -2\mathcal T(t+\lambda_*(t))-tC(t+\lambda_*(t))
   +2\mathcal T(t)+tC(t).
 \tag{6}
$$

The last four terms tend to zero by (3) and $t+\lambda_*(t)\ge t$. Since $\mathcal T(d_t)\to0$, this proves $tC(d_t)\to\kappa^2$.

For completeness the logarithmic size of $d_t$ needs only elementary Dickman bounds. Fix $0<h<1$. The first $h$-length subinterval of the Dickman identity gives $\rho(u)\ge(h/u)\rho(u-1+h)$ for $u\ge1$. Iterate until the argument first lies in $[0,1]$. There are at most $u/(1-h)+1$ steps, each giving a factor at least $h/u$. Thus $\limsup_{u\to\infty}(-\log\rho(u))/(u\log u)\le1/(1-h)$. Let $h\downarrow0$, and use the factorial upper bound and $\log(n!)=n\log n+O(n)$ for the reverse inequality. Also $\rho(d+1/2)/2\le C(d)\le\kappa\rho(d)$ for $d\ge0$: integrate $u\in[0,1/2]$ for the lower bound and use monotonicity for the upper one. Consequently $-\log C(d)\sim d\log d$. By (6), $d_t\log d_t\sim\log t$. The function $x\log x$ is increasing for $x\ge1$, and evaluating it at $(1\pm\varepsilon)\log t/\log\log t$ for fixed $\varepsilon>0$ gives the second formula in (1).

## 3. Transfer at fixed arithmetic parameters

The finite-profile arithmetic formula is $\mathcal R\Phi(t_*;\lambda)-\chi(-1)HP_1(M)+o(\mathcal R)$ for either genuine matched mean. For fixed limiting one-prime parameters away from the threshold, continuity of (4) makes its coefficient eventually bounded away from zero with the stated sign. The two multi-prime tests have the explicit half-unit margin from (2). Under the close-zero assumption and $\chi(-1)=-s$, the two terms therefore reinforce and dominate the $o(\mathcal R)$ error with magnitude bounded below by a positive constant times $\mathcal R+HP_1(M)$. The limit $t\to\infty$ in (1) describes the deterministic threshold function; the arithmetic transfer fixes $B$ and the other declared parameters first and does not let the cutoff grow with $Y$.
