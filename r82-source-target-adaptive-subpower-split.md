# A common exceptional set for genuinely target-adaptive subpower splits

Use the same true below-square-root carrier as the [variable-split local law](r81-source-variable-split-local-sign-law.md), including its exact short-orbit signs, squarefree $N$-units, prime floors, original integer divisor and product cuts, both parities, and stabilized genuine typical count of the whole product $WU$. Write $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\theta=1/20$, $\epsilon=1/64$, $\mathcal J=[X/2,(1+\Delta)X/2]$, $\mathcal X=[X,(1+\Delta)X]$, and

$$
 Z_0=V_X^2,\qquad V_X=\exp(T\ell^\theta),\qquad
 \tau_0=\log Z_0/L=2\ell^{\theta-1}.
$$

The parameters $\rho,\Delta,\delta_0$ are as in the preceding theorem. In particular $\delta_0$ is a sufficiently small fixed positive constant. Take a common cap $Z_1=X^{\tau_1}$ with $\tau_0\le\tau_1\le\delta_0$, but allow the actual split $Z$ to be chosen separately for each even $N$, in the entire interval $[Z_0,Z_1]$. As before the exact $W$ part contains the permitted primes up to $Z$, with hard size $W\le X^{\epsilon/2}$ and count $\omega(W)\le2\log\ell$; $U>1$ consists of the remaining permitted primes above $Z$. None of these masks is relaxed in the sum being estimated.

Fix $0<a,b<20$ and $\delta=a+b-20>0$ as in the variable-split law. Let $R_{N,Z}$ be its true sum, $\mathcal C_{X,Z}$ its exact positive normalization (1), $B_{\mathcal J}(N)$ the physical overlap, $\Sigma(N)$ the even singular series, and $\Psi(\delta)$ the signed Euler coefficient of the [sign theorem](r79-source-short-prime-euler-sign-transition.md). Put

$$
 \mathcal E_X(\tau_1)=\ell^{-1/10}
       +\exp\!\left(-\frac{\epsilon}{8\tau_1}\log\frac1{\tau_1}\right).
$$

**Theorem (unconditional).** Uniformly for the cap above, one has the actual targetwise supremum bound

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
     \ \sup_{Z_0\le Z\le Z_1}
       \left|R_{N,Z}-
         \Sigma(N)B_{\mathcal J}(N)
            \left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2
                         \Psi(\delta)\right|^2
       \ll X^3\mathcal E_X(\tau_1)^2 .
 \tag{1}
$$

The implicit constant depends on the fixed carrier and floor parameters, not on $Z_1$ or on any selected $Z$ at a target. If $\tau_1\to0$, this yields a **single** $o(X)$ exceptional set for every target-adaptive choice: in any fixed interior subwindow both the sign of a nonzero $\Psi$ and magnitude $\gg X$ hold outside $O(X\mathcal E_X^2)$ exceptions, and on the full window the strict sign holds outside $O(X\mathcal E_X^{2/3})$. At the exact fixed critical zero the entire local term is zero; (1) gives simultaneous mean-square cancellation. In particular if $\tau_1\le (\epsilon/16)\log\log\ell/\log\ell$, this retains the preceding $\ell^{-1/5}$ saving in the sum of squares with a common exceptional set. A fixed positive $\tau_1$ need not give a vanishing error here; the previous common-split law continues to apply to each individual fixed polynomial split, not simultaneously over a polynomial range. Neither result makes a fixed-target or unrestricted claim.

## 1. The actual split masks are nested on the active support

The [finite short-orbit identity](r77-source-finite-short-orbit-product-boundary.md) applies before any comparison. Indeed $F,G>D_N$ since $a,b<20$, and both cofactors are squarefree composite because they have the original prime $s$ and a nonempty upper factor. That identity gives the ordinary-ordinary row, the two mixed rows, and the double-containing row with its genuine plus sign and test $(Fz)(Gw)\le Q_N$. All surviving labels on both arms belong to $sW$ or $s'W'$ and have size at most

$$
                         M=\exp((22+a+b)T)<Z_0
 \tag{2}
$$

for large $X$. Here the ordinary omitted-label product is at most $hk/Q_N\ll e^{(20+a+b)T}$, the mixed ordinary omission is at most $k/D_N$ or $h/D_N$, and the mixed short label is at most $Q_N/(F(D_N+1))$ or its reflection. In the double row the short-label product is at most $Q_N/(FG)$. These are bounds under the literal tests, including the weak short-product inequality. All the cofactors in nonzero terms are at least $H_-=\tfrac12\sqrt X e^{-20T}$. An ordinary long label requires this directly, and a surviving short containing label satisfies $Fz\le Q_N/(D_N+1)<\sqrt N$ because its opposite label is long. That implies the stronger $h\gg\sqrt X$, also in the double row since its opposite containing label exceeds $D_N$. The fixed external prime floor $F_0=\sqrt X e^{-aT}$ and the physical interval give $h\le(1+\Delta)X/(2F_0)$, and similarly for the right arm with $b$. These windows have log width $O(T)$, all prime and cofactor logs are comparable to $L$, and these bounds are independent of the split.

On this fixed comparison the distinguished prime is unique, as in the variable-split law: two factors above the external floor would have product so large that the residual product is only $e^{O(T)}$, whereas the true typical count, in a band below both such near-square-root factors, requires a distinct prime $>2V_X$. This also excludes a repeated distinguished prime, so the squarefreeness restriction does not impose an extra pointwise gate in the fixed-prime interval. The floor includes equality in this argument. The old $s$ is also unique by the disjoint permitted alphabets, and $W_Z$ is the product of all cofactor primes other than $s$ at most $Z$. Moving $Z$ neither changes the total genuine tag count nor the prime exclusions. The only changes are the increasing product $W_Z$ and its increasing number of primes. Once the size gate holds, $U>1$ is automatic on the active window: $W_Z\le X^{\epsilon/2}$ and $s\le e^{7T/4}$ cannot reach $H_-$. Thus **passing the split at any $Z$ implies passing $Z_0$**; on the same operands every signed short-orbit mark is unchanged. The true prime floors and actual unit and curved tests are identical before comparison, including all endpoints.

A tuple present at $Z_0$ but lost at any $Z\le Z_1$ must have an arm with $W_{Z_1}>X^{\epsilon/2}$ or $\omega(W_{Z_1})>2\log\ell$. Define the following positive polynomials at the fixed lower split $Z_0$. For each arm use its fixed cofactor window above, its fixed external prime floor, $hF\in\mathcal J$, and the exact $Z_0$ carrier, including the actual total tag requirement. Count all labels $z\mid sW_{Z_0}$ with $z\le M$, using a positive mark $\log F$ per label, and omit the target-unit and curved tests only for these upper bounds. Denote the resulting polynomials by $A_a,A_b$, their nonnegative sequences by the same names with argument $n$. Put $A_a^{\rm bad},A_b^{\rm bad}$ for their coefficients additionally restricted by either of the exact failure events at $Z_1$. Every absolute short-orbit mark is dominated by a fixed multiple of the corresponding positive mark since $\log(Fr),\log(h/z)\ll\log F$ on these windows; the original label cap (2) was obtained **after** the orbit algebra. Thus on each even target, simultaneously,

$$
 \sup_{Z_0\le Z\le Z_1}|R_{N,Z}-R_{N,Z_0}|
 \ \ll\ (A_a^{\rm bad}*A_b)(N)+(A_a*A_b^{\rm bad})(N).
 \tag{3}
$$

The left-hand side does not use any unsigned replacement of a signed Fourier integral. The right side is a single pair of positive convolutions bounding literal missing terms from the short rows.

## 2. Positive tilted Fourier bounds for the genuinely lost arms

The unweighted fourth norms are $\ll X^{3/4}$ by the positive full-window bound of the finite orbit. We prove the weighted analogue needed for (3). For a positive function $\nu$ on normalized log sizes use the multiplier
$\prod_{p\mid h,\ p\ne s}\nu(\log p/L)$ in the positive polynomial for either arm. Consider two specific choices:

$$
 \begin{array}{ll}
 \nu_{\rm ct}(u)=2 & (u\le\tau_1),\\
 \nu_{\rm sz}(u)=\exp(\lambda u/\tau_1)&(u\le\tau_1),
 \qquad \lambda=\tfrac12\log(1/\tau_1),
 \end{array}
$$

with value one for $u>\tau_1$ in both cases. The endpoint $u=\tau_1$ belongs to the tilted range. Write $A_{a,\nu}$ for the resulting polynomial. These are precisely the discrete weights $2^{\omega(W_{Z_1})}$ and $W_{Z_1}^{\lambda/\log Z_1}$. In particular they also weight the primes **in $U$ at the lower split** between $Z_0$ and $Z_1$.

Here are explicit upper bounds for the amounts of tilt. Let $B=\|\nu\|_\infty$ and let $\mathcal D_\nu$ be the unconditioned total extra logarithmic mass, with the harmless allowed-alphabet restrictions dropped for the upper bound:

$$
 \mathcal D_\nu=
    \sum_{e^{4T}\le p\le Z_0}
        \frac{\nu(\log p/L)-1}{p}
       +\int_{\tau_0}^{.7}\frac{\nu(u)-1}{u}\,du .
 \tag{4}
$$

For $\nu_{\rm ct}$, reciprocal PNT on the discrete part and direct integration give $\mathcal D_\nu\le\log\ell+O(1)$ uniformly. For $\nu_{\rm sz}$, reciprocal PNT replaces the discrete sum by the corresponding normalized integral to negligible error: the increasing weight on the tilted range has supremum and total variation $O(e^\lambda)$, which is at most a fixed power of $\ell$ by the lower bound on $\tau_1$. Consequently

$$
       \mathcal D_{\nu_{\rm sz}}
          \le O(1)+\int_0^1\frac{e^{\lambda t}-1}{t}\,dt
          \le O(1)+\lambda e^\lambda .
 \tag{5}
$$

Integer endpoints in (4) match the actual weights; a real endpoint in the comparison integral causes at most the arbitrary inverse-logarithmic reciprocal PNT error. The lower Euler estimate with label counts includes at most two choices for the old $s$ and an occupation factor two on $[e^{4T},M]$, arising from bounding the number of labels by allowing every subset in that band. In bounding the *extra* lower logarithmic mass one must therefore also allow the cross-term from the label tilt. Its logarithm is at most
$\sum_{e^{4T}\le p\le M}(\nu(\log p/L)-1)/p$.
This is $O(1)$ in the counting case (the band has bounded reciprocal mass). In the size case it is at most the discrete term already used in (4), so using $2\mathcal D_{\nu_{\rm sz}}$ suffices in all upper bounds below. In particular this does not square the counting growth in $\ell$.

For completeness, apply the [count-restricted reciprocal product argument](r75-source-dynamic-giant-growing-rough-residual.md) at the lower split with upper kernels $\nu g_{\rm t},\nu g_{\rm f}$, and with the exact $K(W_{Z_0})$ appropriate to each lower factor. Its replacement proof works unchanged in precision. In each ordered prime tuple, the new one-coordinate weight has supremum plus variation $O(B)$, so ordinary reciprocal PNT on the true hard interval in that coordinate has arbitrary inverse-logarithmic error after this factor. The telescoping errors over arities cost at most a constant times the exponential of the total tilted reciprocal mass, since $\sum_{r\ge1}rH^{r-1}/r!=e^H$ for an upper bound $H$ on that mass. Here $B=O(\ell)$ and $H\ll\log\ell+\lambda e^\lambda=o(\ell)$ in the size case, or $H\ll\log\ell$ in the count case, using $e^\lambda=\tau_1^{-1/2}\ll\ell^{(1-\theta)/2}$. In particular the amplification is $L^{o(1)}$, uniformly. The distinct-prime correction is bounded by $O(e^H B^2\sum_{p>Z_0}p^{-2})$, by marking an equal pair, and is smaller still. This proves arbitrary inverse-logarithmic accuracy of the count-restricted replacement with hard endpoints for the weighted reciprocal measure. The sum of the lower labeled tilted reciprocals is also at most $L^{o(1)}$ by (4)–(5).

Let $\rho_{\nu,K}$ be the density of this positive real upper measure on the relevant compact range. Multiplying by its total coordinate and marking one coordinate, exactly as in the growing-rough theorem, gives for positive $v$

$$
 v\rho_{\nu,K}(v)=
   \bigl((\nu\mathbf1_{I_{\rm t}})*A_{\nu,K-1}
         +(\nu\mathbf1_{I_{\rm f}})*A_{\nu,K}\bigr)(v).
 \tag{6}
$$

Here the $A$ are the same exponential measures with the indicated exact count condition. The mass in each term is dominated by the full positive tilted mass, which is
$O(\tau_0^{-1}\exp(\int_{\tau_0}^{.7}(\nu(u)-1)du/u))$.
Thus for $v\in[.4,.6]$ the density is bounded by this number times $O(B)$. No derivative of the tilted density is needed below. Multiplying the density bound by the lower labeled tilted product gives, relative to the unweighted scale $O(\ell\tau_0)\,\tau_0^{-1}=O(\ell)$, a factor at most

$$
        G_{\rm ct}\ll\ell,\qquad
        G_{\rm sz}\ll e^\lambda\exp(2\mathcal D_{\nu_{\rm sz}})
                  \ll \exp\bigl(O(1)+\lambda+2\lambda e^\lambda\bigr).
 \tag{7}
$$

The normalized $W_{Z_0}$ cap and $K(W_{Z_0})$ are retained in the actual density. They are omitted only for bounding the mass and density from above.

We now show that $\|A_{a,\nu}\|_4\ll X^{3/4}G_\nu$, with the corresponding statement for $b$ and with $G_\nu$ a positive upper factor at least one as in (7). On the auxiliary reduced polylogarithmic arcs of the finite orbit apply Siegel–Walfisz to the hard prime interval for $F$ with weight $\log F$, holding the true cofactor fixed. Every prime divisor of $h$ exceeds the denominators. The rational factor is $\mu(q)/\varphi(q)$; the real density in $x=hF$ uses exactly the tilted reciprocal mass weighted by $1/h$. The weight $\log F$ cancels the real prime density denominator, leaving no additional dependence on $x$ at fixed $h$. For each $s,W_{Z_0}$ and short label its log interval for $h$ has length $O(T)$, clipped by the external floor via $\log h\le\log x-\log F_0$. Its arguments on the relevant interval are in $[.4,.6]$ after subtracting $\log(sW_{Z_0})/L$. Thus (6)–(7), with the interval of normalized length $O(T/L)=O(1/\ell)$, bound the supremum by $O(G_\nu)$. Between two physical points $x,y$ the only endpoint moves by at most $|\log x-\log y|/L$ in normalized coordinates. The same positive supremum bounds the resulting variation by $O(G_\nu\ell/L)$ on $\mathcal J$. All discrete PNT replacement errors are estimated first in supremum and integrated directly; they are $O_H(XL^{-H})$ after increasing the chosen PNT exponent. Siegel–Walfisz errors are likewise of this size because the phase variation and numerator count are at most fixed powers of $L$, and the total reciprocal tilted label mass is $L^{o(1)}$ (indeed its full-window real bound is $O(G_\nu)$). Thus the real transform is $O(G_\nu\min(X,|\beta|^{-1}))$. Summing the major fourth norms uses $\int_{\mathbb R}\min(X,|\beta|^{-1})^4d\beta\ll X^3$ and $\sum_q\mu(q)^4/\varphi(q)^3<\infty$ as before.

On the auxiliary minors the actual hard product $hF\in\mathcal J$ is separated by the same half-integer Perron integral, keeping the tilt inside the single $h$ coefficient of the bilinear form. The coefficient enlargement is a fixed power of $L$ uniformly: the number of eligible $W_{Z_1}$ factors is $O(\ell)$, and in the size case the pointwise multiplier is at most $\exp(O(\lambda/\tau_1))=L^{o(1)}$ since $\tau_1\ge2\ell^{\theta-1}$ and $\lambda=O(\log\ell)$. The original pointwise label count is $(1+\log\ell)^{O(1)}$ and no bound on upper arity is imposed. Hence the same bilinear minor argument with sufficiently large fixed polylogarithmic arc exponent gives arbitrary inverse-logarithmic saving in the supremum, and the squared coefficients are $O(XL^C)$ for a fixed constant. The minor fourth norms are negligible. This proves the stated weighted estimates with their actual hard prime and physical cutoffs.

## 3. A uniform Rankin loss and the exact normalization

For the two true failure conditions the elementary pointwise bounds are

$$
 \mathbf1_{\omega(W_{Z_1})>2\log\ell}
          \le \ell^{-2\log2}\,2^{\omega(W_{Z_1})},
 \qquad
 \mathbf1_{W_{Z_1}>X^{\epsilon/2}}
          \le e^{-\lambda\epsilon/(2\tau_1)}
                  W_{Z_1}^{\lambda/\log Z_1}.
$$

Because all coefficients of the comparison polynomials are nonnegative, their fourth norms respect coefficientwise domination: the fourth power is the sum of the squares of the two-fold convolution coefficients. The triangle inequality and (7) consequently show that either bad arm has fourth norm

$$
   \ll X^{3/4}\left(\ell^{\,1-2\log2}
        +\exp\!\left(-\frac{\epsilon}{8\tau_1}\log\frac1{\tau_1}\right)\right).
 \tag{8}
$$

Indeed in the size bound the extra exponent $\lambda+2\lambda e^\lambda+O(1)$ is at most $\epsilon\lambda/(4\tau_1)$ for all sufficiently small fixed $\tau_1$, since $e^\lambda=\tau_1^{-1/2}$. The remaining exponent is $-\epsilon\lambda/(4\tau_1)$, giving the stated rate. On the complementary fixed compact interval of possible $\tau_1$, enlarge the constant in (8). No saving uniformly in a positive polynomial cap is obtained from this estimate.

By (3), Parseval and Hölder this proves

$$
 \left\|\sup_{Z_0\le Z\le Z_1}|R_{N,Z}-R_{N,Z_0}|
          \right\|_{\ell^2(N\in\mathcal X\cap2\mathbb Z)}
  \ll X^{3/2}
       \left(\ell^{\,1-2\log2}
             +e^{-(\epsilon/(8\tau_1))\log(1/\tau_1)}\right).
 \tag{9}
$$

In particular this is already a simultaneous law if one uses the fixed base normalization. We also verify the claimed use of the truly adapted normalization in (1). Choose a fixed nonzero interval $J_*$ in the prime exponent $\alpha=(L/2-\log F)/T$ contained in $(0,\min(a,b,1))$. In one arm with this exponent interval, physical $hF\in\mathcal J$, and the exact count and size gates at split $Z$, sum $\log F$ over the actual operands, with no unit test, label, or paired target. This is a fixed one-arm calibration, not a replacement of any pair mark. The same Siegel–Walfisz evaluation at frequency zero and count-sensitive reciprocal replacement as in §2 of the variable-split law give this total as

$$
                   |J_*|\,\mathcal C_{X,Z}+O(X/\ell),
 \tag{10}
$$

uniformly in $Z$. Specifically at fixed physical $x$ the $\log F$ weight cancels the real prime denominator, the change of variable in that proof gives $|J_*|/\ell$, and the count-restricted density argument differs from $1/2-\log(sW)/L$ by $O(\ell^{-1})$. Its $\tau^{-1}$ Lipschitz bound times the lower profile $O(\ell\tau)$ gives the displayed $O(X/\ell)$ error. The original fixed $J_*$ and $\mathcal J$ ensure these one-arm operands are inside the comparison window and their factorizations are unique.

The genuine one-arm support at $Z$ is contained in that at $Z_0$ by the same nesting. Its loss is at most the Rankin-weighted total at zero of the two enlarged positive polynomials; here the label $1$ suffices for domination. The real major supremum proof above, at zero frequency, bounds this loss by $O(X)$ times the expression in parentheses in (8); the discrete errors are negligible. It follows from (10) that

$$
 \sup_{Z_0\le Z\le Z_1}|\mathcal C_{X,Z}-\mathcal C_{X,Z_0}|
                           \ll X\mathcal E_X(\tau_1).
 \tag{11}
$$

This calibration changes no sign, support, or mask in the desired two-arm result.

Apply the variable-split law at the fixed choice $Z_0$. Its mean-square norm of the local error is $O(X^{3/2}\ell^{-1/10})$. Combine it with (9), where $\ell^{1-2\log2}\ll\ell^{-1/10}$. Finally (11), the uniform bounds $\mathcal C_{X,Z}\asymp X$, $B_{\mathcal J}\ll X$, $\|\Sigma\|_{\ell^2(N)}\ll\sqrt X$, and bounded $\Psi(\delta)$ let us move the fixed-base comparator to the exact adapted comparator at cost $O(X^{3/2}\mathcal E_X)$ in the same supremum norm. Squaring proves (1). If $\tau_1\le(\epsilon/16)\log\log\ell/\log\ell$ then $(\epsilon/8)\tau_1^{-1}\log(1/\tau_1)\ge\log\ell$ for large $X$, giving the stated original rate. For $\tau_1\to0$, on a fixed interior interval the comparator has the asserted sign and magnitude uniformly over $Z$ by the same positive even singular lower bound. For the full window, discard endpoint strips of width $X\mathcal E_X^{2/3}$ and apply (1) to any target where at least one allowed split has the wrong or zero sign. At the exact fixed critical zero (1) applies directly to the actual signed sum. All these exceptions are common to the allowed independently moving splits.
