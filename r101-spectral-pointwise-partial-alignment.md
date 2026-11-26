# The pointwise exceptional parity difference under partial conductor alignment

This concerns the actual exceptional correction to the two mixed-strip parities, at an individual even target. It extends the [fixed-primorial aligned lower bound](r100-spectral-pointwise-aligned-parity-difference-fixed-primorial.md) to targets which can omit many odd factors of the actual Page conductor. It retains the original denominator margin, and its sign has the actual normalized Ramanujan factor. It is not the matched signed dyadic mean, a claim of existence of a qualifying zero, a bound for the full mixed strip, or a result on Hypothesis S.

Use the exact notation and physical hard test of the fixed-primorial theorem. Thus $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, and $Y\le N\le2Y$ is even. The genuine primitive real Page character $\chi$ has conductor $r\le Q_0$ and a simple real zero $\beta$ in the original Page range, with $(1-\beta)G\le C_*\log G$ for fixed $C_*>0$. Assume $\log(Q_0/r)\ge(\log G)^3$ as before. Fix the original admissible $B>B_0>0$ and the nonnegative bounded-BV test $\omega$ on a real half-open $I\subset(N/2,9N/16]$, with $\int_I\omega\ge c_{\rm test}Y>0$. The prime planting only assumes $K_z=\prod_{p\le z}p\mid N$, with $z_*\le z\le Z$ for a sufficiently large fixed $z_*$. In particular the fixed choice $z=z_*$ is permitted.

Write $r=2^e r_{\rm odd}$ with $e\in\{0,2,3\}$ and squarefree odd part, as in the [two-adic mean channels](r99-spectral-two-adic-exceptional-mean-channels.md). Define the true pointwise response and its missing odd conductor product by

$$
       \gamma_N=\frac{c_r(N)}{\varphi(r)},\qquad
       d_N=\frac{r_{\rm odd}}{(r_{\rm odd},N)} .
 \tag{1}
$$

Here $c_r(N)$ is the ordinary Ramanujan sum. Let $\Sigma^{(r)}(N)$ be the binary singular-series product, with the local factor at each prime of $r$ set to $p/(p-1)$ and all other primes evaluated at the actual $N$. This is a factor in the completed exceptional model, not a replacement of the physical target. For even $N$ it is explicitly

$$
    \Sigma^{(r)}(N)=\Sigma(N)
                   \prod_{\substack{p\mid r\\p\nmid N}}\frac{p-1}{p-2}
                      \ \ge\ \Sigma(N).
 \tag{2}
$$

All primes in this displayed product are odd. At full alignment it reduces to the ordinary $\Sigma(N)$.

**Theorem.** Fix $0<\varepsilon<1/2$. At all sufficiently large targets under these assumptions, if $\gamma_N\ne0$ and $d_N\le r^{1/2-\varepsilon}$, then the original genuine exceptional parity difference satisfies

$$
 -\chi(-1)\operatorname{sgn}(\gamma_N)
       \bigl(\mathfrak E_+(N;I,\omega)-\mathfrak E_-(N;I,\omega)\bigr)
 \gg |\gamma_N|\frac{Y^{2\beta-1}}{G}\,
                   \frac{\Sigma^{(r)}(N)}{(\log r)^4}.
 \tag{3}
$$

Constants can depend on the fixed test, cutoffs and $\varepsilon$. This permits response factors smaller than every fixed inverse power of $G$. No divisibility by the full conductor or inclusion of that conductor in $K_z$ is required. In the case $\gamma_N=0$ only the earlier explicit small absolute error applies, not a nonzero sign statement.

## 1. The all-target formula and its algebraic completion

Let $\mathcal D_i(N)$ for $i=0,1$ be the two algebraic right sides used in the [actual all-target reduction](r94-spectral-all-target-ramanujan-exception.md). That formula, on the literal target, gives

$$
 \mathfrak E_\pm(N;I,\omega)
   =\frac{\gamma_N}{2}(\mathcal D_0(N)\pm\mathcal D_1(N))
                    +O(Y^\beta G^{C}r^{-1/2})
 \tag{4}
$$

with a fixed $C$. We retain its explicit conductor error. This formula uses the same finite $t\le Q_0/r$, the two original geometric kernels, the short labels $u,v\le Y^{1/10}$ with $(uv,r)=1$ and their true coprimality, and the original local arithmetic factor at $p\nmid r$ with the test $p\mid N$. The factor $\gamma_N$ accounts for the exact contraction at $r$. In particular no $r$-prime divides the sums or local products inside $\mathcal D_i$.

The algebraic completion in [R93 Sections 1–3](r93-spectral-completed-colored-caps.md) applies to the finite $\mathcal D_i(N)$ with no $r\mid N$ hypothesis. We check where alignment could have mattered. The two local $q\mid t$ options, including $(q,r)=1$, are combined into the same $b_p$ of R93 (6) for $p\nmid r$. Their absolute moving moment depends only on the true $p\mid N$ for those primes and is bounded by the same upper envelope, since the full $\sum_{p\mid N}p^{\vartheta-\beta}\ll\log G$ also bounds its subset away from $r$. Therefore completing $t$ past the original $Q_0/r$ costs $O_A(Y^\beta G^{-A})$ under the displayed margin. This is an error **inside** $\mathcal D_i$, so it will carry $\gamma_N$ in (4).

After that completion the occupied-prime factors restore $(uv,N)=1$ outside $r$, and $(uv,r)=1$ already holds. At every nonconductor prime the exact completed product and coefficient are those of R93 (1), including the actual $p\mid N$ branch. At $p\mid r$ there is no factor in either completed local product. We extend $\alpha_p=0$ there, and the remaining numerator $r/\varphi(r)$ is literal. The primitive $R_*(v)=\sum_{n\le e^v}\chi(n)n^{-\beta}$ still has the same tail and integral $L'(\beta,\chi)$ by periodicity and the actual zero, with no target-alignment assumption. Its signed Euler convolution in R93 (10) uses only $p\nmid r$; all its tail bounds with the mask $Nj$ follow unchanged. The geometric completion of both caps uses the same physical $x$ with $N-x\in I$, the same functions of $\log u,\log v$, and the original upper bound $S=Y^{1/10}$. Neither the clipped primitive argument nor its $Y^{-c}$ short-tail error tests $r\mid N$. Thus, with $\mathcal N_\chi$ and $B_i(x)$ from the completed model for these coefficients, one obtains

$$
 \mathcal D_i(N)
   =-\chi(-1)\int_{N-x\in I}
       \frac{\omega(N-x)(N-x)^{\beta-1}x^{\beta-1}}{\log x}B_i(x)\,dx
      + O_A(Y^\beta G^{-A}).
 \tag{5}
$$

This checks completion of the algebraic model, not application of the aligned arithmetic theorem to an unaligned target. No target or hard endpoint has been changed.

The exact total colored mass calculation in R93 (13) is unchanged as an Euler identity, except for its final identification: $r/\varphi(r)$ supplies the $p/(p-1)$ factor at each prime of $r$, whether or not it divides $N$. The genuine nonconductor factors keep their $p\mid N$ vs $p\nmid N$ choices. This gives exactly $\Sigma^{(r)}(N)$, in particular (2) since the usual missing odd local factor is $p(p-2)/(p-1)^2$. The pointwise prefactor normalized by this mass is consequently

$$
 \frac{\mathcal N_\chi}{\Sigma^{(r)}(N)}
 =\frac1{L'(\beta,\chi)^2}
      \prod_{\substack{p\mid N\\ p\nmid r}}
                  (1-\chi(p)p^{-\beta})^{-2}
      \prod_{p\nmid Nr}
                  (1-\chi(p)p^{-\beta})^{-2}
             (1-2\chi(p)p^{-\beta}/a_p),
 \qquad a_p=\frac{p-2}{p-1}.
 \tag{6}
$$

No exterior factor at a conductor prime has been inserted in this ratio.

## 2. A lower bound on the second cap with the true masks

We use the proof of the fixed-primorial aligned lower bound on the coefficients just verified. All small primes $p\le z$ vanish from $\alpha$, since $K_z\mid N$. The coefficients with $p>z$ remain bounded in magnitude by a constant times $p^{-\beta}$. With the all-minus baseline
$b_p=p^{-\beta}/(a_p+2p^{-\beta})$ for all $p>z$, the inequality $\alpha_p\ge-b_p$ holds both on the ordinary nonconductor factors and on every prime with a zero coefficient. Thus the positive quotient $(1+\alpha_p X)/(1-b_p X)$ still has its unit atom and nonnegative shifts. In particular a conductor prime missing from $N$ now joins the geometric factors $(1-b_p X)^{-1}$, rather than making a new signed or singular factor. All such factors have the same uniform local mass and logarithmic moment bounds as in the fixed-primorial theorem.

For $z\le\log G$ this verifies the whole analytic inequality (11) of that proof: its reciprocal all-minus comparison does not depend on the target mask, the logarithmic marking controls the actual positive unit intervals, and the signed inverse-removal sums run over nonzero $\alpha_p$ only. In particular the near-$U$ supremum and the large-displacement absolute exponential moment apply with the present extra zero coefficients. Thus the genuine $B_1(x)$ of (5), with $U=(B-B_0)\log\log N$ in the original shifted caps, is bounded below by a positive constant times $\mathcal N_\chi\ell^2D_+(U)^2$, where $\ell=\log z$ and $D_+$ is its actual positive cumulative shift mass. For $z>\log G$ use the corresponding [logarithmic-primorial lower-cap proof](r99-spectral-pointwise-aligned-parity-difference-logarithmic-primorial.md), Sections 1–3, already in its range. Its comparison, first moments and tail estimate likewise only require the stated coefficient bounds, the actual zero factors and nonnegative quotient.

The normalization step with (6) also follows directly. Under $K_z\mid N$ its exterior paired factors stay positive and their absolute log sum is bounded by $O(\sum_{p>z}(p^{-1-\beta}+p^{-2\beta}))$. The interior finite factors cost at most $\exp(2\sum_{p\mid N,\,p\nmid r}p^{-\beta})$ in the reciprocal. Its primes at most $z$ cost $O(\ell^2)$, and the positive geometric factors at the actual interior primes $z<p\le\exp(U/M_0)$ recover their exponential reciprocal-prime mass in $D_+(U)^2$ by the same normalized first-moment comparison, for fixed large $M_0$. For $p\mid N$ above $\exp(U/M_0)\ge G^c$, the remaining sum is bounded by splitting at $G$. If $U<\ell$, all primes above $z$ are already in that bounded range. Missing conductor primes do not occur in the interior product and their shifts only increase the positive cumulative mass. With the same near-exception bound $|L'(\beta,\chi)|\ll(\log r)^2$, this proves uniformly on the physical support

$$
                            B_1(x)\gg
                                \frac{\Sigma^{(r)}(N)}{(\log r)^4}.
 \tag{7}
$$

This is a lower bound for the exact completed algebraic cap, not an assumption on either genuine parity. By nonnegative $\omega$ with the stipulated mass and $N-x,x\asymp Y$, the positive integral of $B_1(x)$ in (5) is consequently at least a constant times $Y^{2\beta-1}\Sigma^{(r)}(N)/[G(\log r)^4]$.

## 3. Divide only by the actual nonzero response

At each odd prime of the squarefree conductor, the normalized local Ramanujan factor is $1$ if $p\mid N$ and $-1/(p-1)$ otherwise. The normalized $2$-part at an even target is either zero or of modulus one, by the explicit primitive exponent list (for $e=2$ it is $(-1)^{N/2}$; for $e=3$ it vanishes if $4\nmid N$ and otherwise is $(-1)^{N/4}$). By CRT, when $\gamma_N\ne0$ this gives exactly $|\gamma_N|=1/\varphi(d_N)$. Thus under the bound on $d_N$, the raw absolute error of (4), divided by the actual response, is

$$
          O\!\left(Y^\beta G^C r^{-1/2}\varphi(d_N)\right)
             =O\!\left(Y^\beta G^C r^{-\varepsilon}\right).
 \tag{8}
$$

Classical growth of the Page conductor in this zero range, $r>G^J$ eventually for every fixed $J$, makes (8) $O_A(Y^\beta G^{-A})$ for every fixed $A$. The completion error in (5) already had this strength **relative to** $\gamma_N$. Subtract the two actual parity formulas (4); color zero cancels and the sign from the remaining physical integral is $-\chi(-1)\gamma_N$. The two errors are absorbed in (7) after multiplying by $|\gamma_N|$, since $Y^{\beta-1}\ge G^{-C_*}$, $\log r\ll\sqrt G$, and $\Sigma^{(r)}(N)\ge\Sigma(N)$ has an absolute positive lower bound at even $N$. Taking $A>C_*+4$ suffices. This proves (3) at the specified individual targets without using a signed average or any assertion of existence.
