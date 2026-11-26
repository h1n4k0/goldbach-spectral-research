# The aligned exceptional parity mean needs no extra lower bound on the primorial

**Scope.** This extends the actual complete signed mean of [R96](r96-spectral-aligned-mean-euler-collapse.md) to every full primorial in its construction that contains the actual Page conductor, without the lower bound on the planting prime cutoff in [R97](r97-spectral-aligned-mean-dickman-lower.md). It is conditional on a sufficiently close aligned Page zero. No existence claim, sign or size at an individual target, full mixed-strip positivity, prime-pair result, or Hypothesis S is asserted. The proof uses a classical smoothed ordinary Möbius sum, not a cutoff-uniform Dickman positivity assertion, and neither Dirichlet GRH nor an external assertion about the Page-zero gap.

Keep the exact R96 dyad and tests. In particular, $G=\log Y$, $Z=\sqrt G/\log G$, $Y\le v\le2Y$, and the possible primitive real Page character $\chi$ of conductor $r$ has its actual simple zero $\beta>1-4a_0/\sqrt G$. Assume it exists and has $(1-\beta)G\le C_*\log G$ for fixed $C_*>0$. Take the full primorial $K_z=\prod_{p\le z}p$ fixed on the dyad, with $r\mid K_z$, $2\le z\le Z$ and $K_z\le e^{2Z}$. No further lower bound on $z$ is assumed. Fix the same admissible $B>B_0>0$ and the same fixed interval $J\subset(1/2,9/16]$, nonnegative fixed bounded-BV weights $w,\eta$ with positive integrals $\int_Jw,\int_1^2\eta$, and angle brackets for the R96 normalized mean on **all** targets in $[Y,2Y]$ divisible by $K_z$. The genuine positive cuts are $U_v=(B-B_0)\log\log v$ and $T_{v,x}=2B\log\log v+\log(x/v)$ when $v-x\in vJ$. In particular no change is made to the finite denominator range of the original auxiliary exceptional correction.

**Theorem.** For all sufficiently large dyads with these hypotheses, the actual signed parity correction satisfies

$$
 -\chi(-1)\langle\mathfrak E_+-\mathfrak E_-\rangle_{K_z}
 \ \gg\
      \left(\int_J w\right)\left(\int_1^2\eta\right)
      \frac{Y^{2\beta-1}}{G}\,
      \frac{K_z}{\varphi(K_z)(\log r)^4}.
 \tag{1}
$$

Here $+$ and $-$ retain the original even and odd squarefree factor-count sectors. Constants can depend on the fixed cutoffs, tests, Page threshold and $C_*$. As in R96 the assertion for sufficiently large dyads is ineffective. In particular the classical conductor growth already forced by a Page zero in this setting is used; no new claim about that zero is made.

## 1. Integrated rough Möbius at the exact reciprocal weights

Put $\ell=\log z$ and $b=1-\beta$. The classical Page conductor bound already used in R96 gives $r>G^A$ for each fixed $A$ at sufficiently large $Y$. The elementary prime bound $\sum_{p\le z}\log p\ll z$, together with $r\mid K_z$, thus gives

$$
                         z/\log G\ \longrightarrow\ \infty .
 \tag{2}
$$

All limits here and below are restricted to the stated actual aligned dyads. In particular $\ell\to\infty$ and $\ell\le\log G$ at large $Y$.

Let $R^{\mathrm m}(u)=\sum_{n\le e^u}\mu(n)/n$ for $u\ge0$, set it to zero below zero, and put $A^{\mathrm m}(u)=\int_0^u R^{\mathrm m}(t)\,dt$ for $u\ge0$, also zero below zero. The floor identity $\sum_{n\le x}\mu(n)\lfloor x/n\rfloor=1$ gives $|R^{\mathrm m}(u)|\le2$. We also use $0\le A^{\mathrm m}(u)\ll1$ and $A^{\mathrm m}(u)\to1$. Indeed Theorem 1.2 with $q=k=\sigma=1$ of [Ramaré and Zuniga Alterman, arXiv:2312.05138v3](https://arxiv.org/pdf/2312.05138v3) gives the former. Their Corollary 3.4 gives the latter using the classical prime number theorem in its ordinary Möbius forms $\sum_{n\le x}\mu(n)=o(x)$ and $\sum_{n\le x}\mu(n)/n=o(1)$. In that corollary the harmonic remainder $\log t+\gamma+1/t-\sum_{n\le t}1/n$ is $O(1/t)$, so its integral term tends to zero by dominated convergence. This is an unconditional ordinary-zeta input, not an estimate on a twisted Möbius sum.

Let $R^{\mathrm m}_z$ be the same reciprocal primitive with all prime factors greater than $z$, and $A^{\mathrm m}_z$ its integral with the same zero extension. Omitting each factor $1-p^{-1}X$ at $p\le z$ amounts to convolving both primitives with the positive measure

$$
     \lambda_z=\sum_{\substack{a\ge1\\p\mid a\ \Rightarrow\ p\le z}}
                          \frac1a\,\delta_{\log a}.
 \tag{3}
$$

The full mass is $\prod_{p\le z}(1-1/p)^{-1}\asymp\ell$ by the reciprocal prime bounds, and the two identities $R^{\mathrm m}_z=R^{\mathrm m}*\lambda_z$, $A^{\mathrm m}_z=A^{\mathrm m}*\lambda_z$ follow by exact Euler coefficients and then integration. This gives a uniform $O(\ell)$ upper bound on $|R^{\mathrm m}_z|$ and $A^{\mathrm m}_z$. For $u\ge\ell$, the convolution terms with $a\le\sqrt z$ have $u-\log a\ge\ell/2$, where $A^{\mathrm m}\ge1/2$ for large $\ell$; all other terms are nonnegative. Since every positive integer $a\le\sqrt z$ is in (3) and the reciprocal sum over them is $\gg\ell$, this gives $A^{\mathrm m}_z(u)\gg\ell$. For $0\le u\le\ell$ these exact rough primitives are $R^{\mathrm m}_z(u)=1$ and $A^{\mathrm m}_z(u)=u$. We have in particular a positive integrated primitive at all log scales, without requiring the discrete unsmoothed primitive to have a fixed sign.

## 2. Transfer to the actual completed coefficients with both signs

Write $\alpha_p$ for the actual completed coefficient in R96 (2). It vanishes for $p\le z$. For $p>z$ put $a_p=|\alpha_p|$; then $a_p\ll p^{-\beta}$ and $a_p<1/2$ for large $Y$, since all those primes are outside $r$. Uniformly for either sign of $\chi(p)$, $|a_p-p^{-\beta}|\ll p^{-2\beta}$. Choose $U_*=C\log G$ for a sufficiently large fixed $C$ so that it exceeds $\ell$ and all the actual $U_v$. On the log interval $[0,U_*]$ any prime larger than $e^{U_*}$ is irrelevant to the primitive. Use the finite prime product of ratios
$(1-a_pX)/(1-X/p)$ at $z<p\le e^{U_*}$, where $X$ encodes a shift by $\log p$. Denote its measure by $\nu_-$. The sum of the absolute nonconstant coefficients at $p$ is $|a_p-1/p|/(1-1/p)$. Consequently

$$
 \|\nu_- -\delta_0\|_{\rm TV}
     \ll \sum_{z<p\le e^{U_*}}|a_p-1/p|
     \ll z^{1-2\beta}+bU_*e^{bU_*}=o(1).
 \tag{4}
$$

For the first inequality, multiply the bounds one plus the absolute nonconstant mass and subtract one; the sum tends to zero. For the second, use the integer tail for $p^{-2\beta}$, the inequality $p^{-\beta}-1/p\le b e^{bU_*}(\log p)/p$, and $\sum_{p\le t}(\log p)/p\ll\log t$. In particular $bU_*=o(1)$ from the hypothesis on $bG$.

On $[0,U_*]$ let $R_-$ and $A_-$ be the squarefree all-minus rough primitive with coefficients $-a_p$ at the primes and its integral. They equal $R^{\mathrm m}_z*\nu_-$ and $A^{\mathrm m}_z*\nu_-$ there, retaining zero extension for negative arguments. Inequality (4) and the global bounds of Section 1 give $|R_-|,|A_-|\ll\ell$ throughout and $A_-(u)\gg\ell$ for $\ell\le u\le U_*$. On $0\le u\le\ell$ they are exactly 1 and $u$, since the first nonconstant possible shift is beyond $\ell$. Thus $A_-\ge0$ on this whole finite range.

The actual primitive $R_1(u)=\sum_{n\le e^u}\alpha(n)$ of R96 and its integral $A(u)$ are the convolutions of $R_-,A_-$ with the **positive** shift measure $\nu_+$ obtained from the finite product
$(1+\alpha_pX)/(1-a_pX)$ at the same primes. At a negative prime the quotient is one, and at a positive prime it is $1+2\sum_{k\ge1}a_p^k X^k$. The measure has unit mass at zero, so in particular $A(u)\ge0$ on $[0,U_*]$. For $D(U)=\nu_+([0,U])$, these convolutions give

$$
   \sup_{0\le u\le U}\{|R_1(u)|+|A(u)|\}\ll \ell D(U)
      \quad(0\le U\le U_*),\qquad
   A(U)\gg \ell D(U)\quad(\ell\le U\le U_*).
 \tag{5}
$$

Here is the proof of the lower bound in (5). If $\ell\le U\le2\ell$, the unit shift gives $A(U)\ge A_-(U)\gg\ell$, and $D(U)\ll1$ because the total mass of factors at $z<p\le e^U\le z^2$ is at most $\exp(O(\sum_{z<p\le z^2}1/p))$. Indeed $a_p\ll1/p$ throughout the finite prime set since $bU_*=o(1)$. No primes beyond $e^U$ can enter the cumulative mass. For $U\ge2\ell$, we claim $D(U/2)\gg D(U)$. Take a sufficiently large fixed $M_0$ and retain only the quotient factors at primes $p\le\exp(U/M_0)$. Normalize their positive convolution by its total mass. Its mean log shift is
$\sum_{\alpha_p>0,\ p\le\exp(U/M_0)}2a_p\log p/(1-a_p^2)\ll U/M_0$
by the elementary reciprocal prime logarithmic bound. For a fixed large enough $M_0$ this is at most $U/4$, so at least half the mass lies at shifts $\le U/2$ by Markov. The full Euler mass at $p\le e^U$ is at most a fixed multiple of this retained total mass, since the ratio is bounded by $\exp(O(\sum_{\exp(U/M_0)<p\le e^U}1/p))=O_{M_0}(1)$. These comparisons apply regardless of which signs occur; an empty small-prime product is allowed. Nonnegative masses and unit local atoms imply $D(U/2)$ is at least the retained mass at shifts $\le U/2$, whereas $D(U)$ is no more than the full Euler mass at $p\le e^U$. This proves the claim. The $A_-$ convolution with shifts up to $U/2$ now gives $A(U)\gg\ell D(U/2)\gg\ell D(U)$, since all leftover arguments are at least $\ell$. We used the elementary bounds $\sum_{p\le t}1/p=\log\log t+O(1)$ and $\sum_{p\le t}(\log p)/p=\log t+O(1)$ as in R97; no distribution of positive or negative primes for $\chi$ is assumed.

## 3. Keep the tail cutoff in the squared norm before summing signs

Use precisely $M_K,C_K,Q_K,J_K$ from R96 (2)--(3), with $K=K_z$. For a squarefree $j$ with $\alpha(j)\ne0$ the genuine inverse removal is $R_j=R_1*\kappa_j$, where $\kappa_j$ is the signed shift measure with local factors $\sum_{k\ge0}(-\alpha_p)^k X^k$ at $p\mid j$. Write $V_j=\prod_{p\mid j}(1-a_p)^{-1}$. Its absolute mass is at most $V_j$ and its absolute first log moment is at most
$V_j\sum_{p\mid j}a_p\log p/(1-a_p)$. These follow by the geometric sums of the nonnegative coefficient bounds; both include the exact shifts by $k\log p$. Put $w_p=a_p^2/(1-a_p)^2$ at $p>z$. The two aggregate bounds are

$$
 \begin{split}
 \Delta_0
   &=\sum_{\substack{j>1\\j\ {\rm sf},\,\alpha(j)\ne0}}
                  |\alpha(j)|^2 V_j^2
     =\prod_{p>z}(1+w_p)-1\ll z^{1-2\beta},\\
 \Delta_1
   &=\sum_{\substack{j>1\\j\ {\rm sf},\,\alpha(j)\ne0}}
             |\alpha(j)|^2 V_j^2\sum_{p\mid j}\frac{\log p}{1-a_p}\\
   &=\prod_{p>z}(1+w_p)
               \sum_{p>z}\frac{w_p\log p}{(1+w_p)(1-a_p)}
     \ll z^{1-2\beta}.
 \end{split} \tag{6}
$$

The first uses the integer tail, and the second uses $\sum_{p>z}(\log p)p^{-2\beta}\ll z^{1-2\beta}$ by partial summation from $\sum_{p\le t}\log p\ll t$. All these bounds are uniform because $\beta\ge.99$. In particular the second inequality has **no extra $\log z$**.

Fix $U\ge0$ in the original range and write $E(U)=\int_U^\infty R_1(u)^2\,du$ and $S(U)=\sup_{0\le u\le U}|R_1(u)|$. In R96, $C_K(0)-Q_K(U)$ divided by $M_K$ is exactly the signed sum of squared norms $\|R_j\,\mathbf1_{u>U-\log j}\|_2^2$ with weights $\mu(j)\alpha(j)^2$. If $j>e^U$ this notation correctly takes the whole norm since $R_j=0$ below zero; equality at an endpoint does not affect the integrals. Cauchy--Schwarz in the inverse-shift measure **before** integration gives

$$
 \begin{split}
 \|R_j\,\mathbf1_{u>U-\log j}\|_2^2
 &\le V_j\int
       \|R_1\,\mathbf1_{t>U-\log j-s}\|_2^2\,d|\kappa_j|(s)\\
 &\le V_j^2 E(U)
      +V_j^2 S(U)^2\sum_{p\mid j}\frac{\log p}{1-a_p}.
 \end{split} \tag{7}
$$

Indeed the additional portion of the integrand below $U$ is bounded by $(\log j+s)S(U)^2$ since $R_1$ is zero below zero. The second estimate follows after the first log moment above and $\log j=\sum_{p\mid j}\log p$. This bounds contamination through the true shifted tail endpoint, rather than charging the entire interval $[0,U]$ for each $j>1$. The $j=1$ term is exactly $E(U)$, so by signed summation in the exact cap

$$
 \frac{C_K(0)-Q_K(U)}{M_K}
       \ge (1-\Delta_0)E(U)-\Delta_1 S(U)^2
       \ge -O\bigl(z^{1-2\beta}S(U)^2\bigr).
 \tag{8}
$$

Global $L^2$ and convergence in this step follow from R96; the positive term $E(U)$ need not be bounded from below.

For $J_K(U)$ the signed $j>1$ terms are similarly controlled, now directly on the integrated primitive. Indeed $\int_0^{U-\log j} R_j$ for $j\le e^U$ equals $(A*\kappa_j)(U-\log j)$ by support and finite integration; its absolute value is at most $V_j\sup_{0\le u\le U}|A(u)|$. When $U\ge\ell$ use (5) and $\Delta_0=o(1)$ in (6) to obtain

$$
   J_K(U)/M_K
        \ge A(U)^2-\Delta_0\sup_{0\le u\le U}|A(u)|^2
        \gg \ell^2D(U)^2 .
 \tag{9}
$$

If $U\le\ell$, instead $J_K(U)/M_K=U^2$ exactly, since $j=1$ is the only possible nonzero term and $R_1=1$ on $[0,\ell]$. In this latter case $S(U)=1$.

On the original geometric support $T_{v,x}>0$ for large $Y$, and $T_{v,x}\ll\log G$. Equations (2) and $b\ell=o(1)$ give $T_{v,x} z^{1-2\beta}=o(1)$ uniformly. If $U_v\ge\ell$, combining (5), (8), (9) for the actual color-one cap of R96 shows
$\mathcal A_1(v,x)/M_K\gg \ell^2D(U_v)^2\ge\ell^2$ for large $Y$, with a positive implied lower constant. If $U_v\le\ell$, it gives
$\mathcal A_1(v,x)/M_K\ge U_v^2-o(1)\gg\ell^2$ as well: $U_v=(B-B_0)\log\log v\gg\ell$ from the upper bound on $z$ and the fixed positive cutoff gap. Thus in all cases

$$
                         \mathcal A_1(v,x)\gg M_K\ell^2 .
 \tag{10}
$$

In particular this conclusion at smaller $z$ need not use positivity of the unsmoothed rough primitive or a positive lower bound on its late tail. It is the exact finite squared integral $J_K(U_v)$ that supplies the lower bound, after controlling the negative tail shift by its actual aggregated log moment.

## 4. Transfer to the actual complete signed mean

The normalization check in R96 Section 4 uses only the primorial factor, reciprocal prime estimates, $b\ell=o(1)$ and the same classical upper bound $|L'(\beta,\chi)|\ll(\log r)^2$ from the cited Montgomery--Vaughan formula there. Those estimates give exactly $M_K\ell^2\gg K_z/(\varphi(K_z)(\log r)^4)$ here as well: the ordinary exterior factor is $1+O(z^{1-2\beta})$; the interior factor after extracting $K_z/\varphi(K_z)$ is at least $\exp(-2\sum_{p\le z}p^{-\beta})\gg\ell^{-2}$. This normalization does not depend on a lower bound of the form $z\ge G^\epsilon$.

Subtracting the parity signs of the exact R96 mean (5) leaves just $\mathcal A_1$ with factor $-\chi(-1)$. The genuine mean corrections are real on these tests. The nonnegative physical integrals have scale $Y^{2\beta-1}/G$ times the product of integrals in (1), using $x,v-x\asymp Y$ and substituting $(v-x)/v$ and $v/Y$. Inequality (10) and the normalization now give (1) after choosing the inverse-log error exponent in R96 sufficiently large: the main scale has $Y^{2\beta-1}\ge YG^{-2C_*}$ and $\log r\le2Z$. This closes the same actual signed-mean comparison with all its finite cutoffs intact. It is not an assertion about any individual aligned target or the sign of an uncorrected prime-pair count.
