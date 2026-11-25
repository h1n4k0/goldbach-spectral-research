# The actual all-target exceptional correction has an exact Ramanujan contraction

**Scope.** The genuine mixed-strip exceptional correction can be evaluated by an explicit finite two-pole expression at **every** even target, without assuming its Page conductor divides the target. The extra factor is exactly an ordinary Ramanujan sum at the conductor. It can make the correction pointwise small, or cancel its leading term exactly, even when the real zero is extremely close to one. This is not a bound for the highly aligned residual, an assertion that the correction is negligible on every prescribed planting, or a result on prime pairs or Hypothesis S. No Dirichlet GRH or external zero-gap input is used.

Use the exact parameters of [the all-scale exceptional-left reduction](r87-spectral-all-scale-exceptional-left-reduction.md): $Y\le N\le2Y$ even, $G=\log Y$, $L=\log N$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$, with fixed admissible $B>B_0>0$. The actual left test has real half-open $I\subset(N/2,9N/16]$ and uniformly bounded supremum and pointwise variation of $\omega$. Suppose the genuine Page character $\chi$ exists, primitive and real of conductor $r\le Q_0$, with its simple real zero $\beta>1-4a_0/\sqrt G$. We do not assume $r\mid N$. If there is no such character the correction is zero as before. Write $c_r(N)=\sum_{k\bmod r,\,(k,r)=1}e(kN/r)$, where $e(t)=e^{2\pi it}$.

For either color $i=0,1$ let $\mathcal D_i(N)$ be the **algebraic right hand side** (3) of [the aligned two-pole formula](r92-spectral-aligned-exceptional-two-pole-formula.md), at this actual $N$. This definition makes sense also when $r\nmid N$. In particular its prefactor includes $-r\chi(-1)/(\varphi(r)L'(\beta,\chi)^2)$, its finite sum is $t\le Q_0/r$, and its local factors use the actual test $p\mid N$ for $p\nmid r$. Its two short labels are at most $S=Y^{1/10}$, squarefree, coprime to one another and to $r$. Its physical real kernels have the original $D,H_0$ and $x=N-n$, and all the $r$-prime factors are excluded from the local product. No infinite Ramanujan completion is made.

**Theorem.** Uniformly in these targets and all genuine hard tests, with a fixed $C$ one has

$$
 \mathfrak E_\pm(N;I,\omega)
   =\frac{c_r(N)}{\varphi(r)}
          \frac{\mathcal D_0(N)\pm\mathcal D_1(N)}2
       +O\!\left(Y^\beta G^C r^{-1/2}\right).
 \tag{1}
$$

The error also has size $O_A(Y^\beta G^{-A})$ for every fixed $A>0$ by the classical conductor lower bound at this Page choice. The sign $+$ denotes the true even squarefree factor-count color. The actual bound following from (1) is

$$
 \begin{split}
 |\mathfrak E_\pm(N;I,\omega)|
 &\ll Y^\beta G^C\left[
             e^{-4(1-\beta)G/5}\frac{|c_r(N)|}{\varphi(r)}
                            +r^{-1/2}\right]\\
 &\ll Y^\beta G^C\left[
             e^{-4(1-\beta)G/5}\frac{(r,N)}{r}
                            +r^{-1/2}\right],
 \end{split}                                                         \tag{2}
$$

after adjusting $C$. Thus in particular the correction is $O_A(Y^\beta G^{-A})$ pointwise if $r/(r,N)$ exceeds every fixed power of $G$ along the targets in question. If $c_r(N)=0$ the leading term of (1) is exactly absent: for example this holds when $8\mid r$ and $N\equiv2\pmod4$. No relative distance between $r$ and the original $Q_0$ is required. These conclusions are about the genuine correction before any planted-family exceptional-set restrictions, not a new pointwise estimate of the full mixed sum.

## 1. The ordinary Möbius pole on a genuinely full residue

Fix $q$ squarefree, $(q,r)=1$, $rq\le Q_0$, and a coprimality mask $w\le Y^{C_0}$ for fixed $C_0$. A class $B\bmod rq$ has components $B_r,B_q$. Let $B_*(w;q,B_q)$ be the coefficient (5) of the aligned formula (renamed to avoid confusion with the class or cutoff exponent). Thus for $g_q=(B_q,q)$,

$$
 B_*(w;q,B_q)=\mathbf1_{(g_q,w)=1}
       \frac{\mu(g_q)\chi(g_q)g_q^{-\beta}}{\varphi(q/g_q)}
                 \prod_{p\mid wq}(1-\chi(p)p^{-\beta})^{-1}.
 \tag{3}
$$

For $Y^{1/4}\le X\le4Y$ the required **ordinary** Möbius progression is

$$
 \sum_{\substack{n\le X,\ n\equiv B\ (rq)\\(n,w)=1}}\mu(n)
   =\frac{\chi(B_r)}{\varphi(r)}
       \frac{B_*(w;q,B_q)}{L'(\beta,\chi)}
           \frac{X^\beta}{\beta}
      +O(Xe^{-c\sqrt G})
 \tag{4}
$$

with uniform fixed $c>0$. In particular the pole is absent if $B_r$ is not a unit. The two long variables in the eventual arithmetic are ordinary $\mu$-weighted before (4) is applied; they are not twisted by $\chi$ by fiat.

To check this, put $g=(B,rq)$. If $\mu(g)=0$ or $(g,w)>1$ the sum is zero, and the stated pole term is zero as well. Otherwise write $n=g\ell$. The reduced class $B/g\bmod rq/g$ and mask $gw$ are exact, with outside factor $\mu(g)$. Orthogonality there uses the reciprocal Dirichlet functions of the characters in those progressions. If $(g,r)>1$, then $r$ cannot divide $rq/g$, since $(q,r)=1$ and one of its prime exponents has decreased. So no character on this reduced modulus induces the unique Page character. Its corresponding real pole is absent, and Page uniqueness excludes the rest of the near-real poles under the cap. If $(g,r)=1$, then $g=g_q$. On $rq/g$, the unique pole-producing character is induced from $\chi$; its residue-class factor is $\chi(B/g)=\chi(B_r)\chi(g)$, since $\chi$ is quadratic and $g$ is a unit. The $\varphi$ factor is $\varphi(r)\varphi(q/g)$. The masks and imprimitive Euler omissions give the product in (3) because $\chi(p)=0$ for $p\mid r$, and because $g$ restores the missing $q$ primes. Evaluating the pole contribution at $X/g$ gives $g^{-\beta}$ exactly.

For clarity the contour is the one checked in [Section 1 of the aligned formula](r92-spectral-aligned-exceptional-two-pole-formula.md#1-exact-single-pole-progression-including-nonunits): height $e^{\sqrt G}$, shifted line $1-5a_0/\sqrt G$, uniform primitive reciprocal bounds, half-integer Perron and polynomially sized mask. After the gcd reduction $X/g\ge Y^{1/5}$ for large $Y$, since $rq\le Q_0=Y^{o(1)}$. All conductors remain at most $Q_0$, and the same finite Euler products are $G^{O(1)}$ on the contour by splitting the primes of the mask at $G^2$. The ordinary principal character, now possible, uses $1/\zeta$ with those finite omissions: it is holomorphic in the narrow rectangle, with a zero at the pole $1$ of $\zeta$, and the classical reciprocal bounds used in [the good-dyad contour](r85-spectral-unconditional-planted-ap-good-dyads.md#1-good-dyads-are-unconditional) apply. Thus the earlier uniform horizontal, truncation and vertical errors give the error in (4) for all these characters. The derivative denominator is unchanged and $|1/L'(\beta,\chi)|\ll1$ by the same near-exception bound. The real pole density from (4) is its displayed residue times $x^{\beta-1}dx$, without a further $\beta$ factor. For $q=1$ use $g_q=1$ and its trivial residue.

## 2. Apply (4) without discarding any nonaligned terms first

Work in the [actual hard exceptional transfer](r88-spectral-hard-exceptional-residue-transfer.md) followed by the [long unsigned deletion](r91-spectral-exceptional-long-unsigned-deletion.md). Both apply to all actual even targets. For the two true colors $A_0=M_>$ and $A_1=\mu(m)M_>$ their retained unsigned labels are respectively $(a,d)$ and $(b,c)$, each at most $S$. Their other labels are the true signed long ones, with original coprime squarefree and geometric conditions. The old replacement errors are bounded by

$$
    O\!\left(Y^\beta G^{C_1}
                    (Q_0^{-1/2}+r_{\rm odd}^{-1/2})
                      +Y^{\beta-1/40}\right).
 \tag{5}
$$

No alignment hypothesis was needed in these statements.

Fix the two short labels $(u,v)$ and $h=uv$ in either retained color. For $q\mid t$ in the finite Ramanujan divisor expansion, the actual congruence is $h b_1b_2\equiv N\bmod q$, with $b_1,b_2$ the two signed variables. As in the aligned proof, expand their mutual coprimality by $\sum_{k\mid(b_1,b_2)}\mu(k)$ and put $b_i=kz_i$. The true squarefreeness and fixed short coprimality give $k$ squarefree, $(k,h)=1$, and the remaining signs $\mu(z_1)\mu(z_2)$ with $(z_1z_2,kh)=1$ and outside factor $\mu(k)$. **At this point neither $h$ nor $k$ is restricted relative to $r$.** The actual color factor is still $\chi(N-hk^2z_1z_2)$. The tail $k>Y^{1/100}$ costs $O(Y^{\beta-1/100+o(1)})$ by the same floor bound $\ll Y(1+\log Y)/(hk^2)$ for pairs and the positive absolute $t,q$ budget of the aligned proof. This tail uses no conductor coprimality. The weight $n^{\beta-1}\omega(n)$ and the actual centered mark are bounded by $O(Y^{\beta-1})$.

For remaining $k$ enumerate the two full residues modulo $rq$. There are at most $(rq)^2\le Q_0^2$ residue pairs, and in each the actual color is constant, with the $q$-component constraint $hk^2z_1z_2\equiv N\bmod q$. The genuine minimum upper gate still gives at most two intervals in a long variable when the other is fixed. The original pointwise-BV weight in one variable is $O(Y^{\beta-1})$ in supremum plus variation. Also both $z_i$ exceed $Y^{.37}$ on the admissible real slices by the actual lower bounds in the long unsigned deletion, and the slices have scale comparable to $Y/(hk^2z_{\rm fixed})$. Hence (4) and pointwise summation by parts apply on every literal hard interval. Apply first in $z_2$, exchange its real integral and the finite sum in $z_1$, and apply in $z_1$ on the same hard real slices, exactly as in the aligned argument. The first-step error sums a reciprocal harmonic weight in $z_1$. The second integrates $z_2^{\beta-2}$ from a polynomial lower bound, hence costs $O(G)$. The residue choices, $t,q$ weights and polynomial norms cost $G^{O(1)}Q_0^{O(1)}$ altogether beyond the same reciprocal $(hk^2)^{-1}$. Thus these two errors total $O(Y^\beta G^{O(1)}Q_0^{O(1)}e^{-c\sqrt G})$. By working slice by slice no variation of a moving integrated boundary is required.

By (4) the pole has nonzero weight only on unit $r$-classes, and there the two factors of its density depending on these classes are $\chi(a_1)\chi(a_2)/\varphi(r)^2$. The $q$-classes and all masks are exactly those of (3), with no dependence on $a_1,a_2$. The double pole on the real variables is as in the earlier formula, but now multiplied by the local contraction

$$
 \frac1{\varphi(r)^2}
  \sum_{a_1,a_2\in(\mathbb Z/r\mathbb Z)^\times}
       \chi(a_1)\chi(a_2)\chi(N-hk^2a_1a_2)
       =\frac1{\varphi(r)}\sum_{a\bmod r}\chi(a)\chi(N-hk^2a).
 \tag{6}
$$

For each unit $a$, its product fiber on the left has exactly $\varphi(r)$ pairs; nonunits on the right have zero weight.

## 3. The primitive contraction and its exact conductor dependence

If a prime power $p^\nu\parallel r$ has $p\mid hk$, the local factor $\chi_p(N-hk^2a)$ on the right of (6) is constant on every fiber of
$(\mathbb Z/p^\nu\mathbb Z)^\times\to(\mathbb Z/p^{\nu-1}\mathbb Z)^\times$. Indeed varying $a$ within that fiber changes $hk^2a$ by a multiple of $p^\nu$; if $\nu=1$ use the full unit group over modulus one. By primitivity the local character $\chi_p(a)$ is nontrivial on the kernel, hence sums to zero on each fiber. The other local factors are independent by the CRT, so (6) is zero. This includes primes of the two-primary part, without any assumption on $N$. Consequently the class sum enforces $(hk,r)=1$ in the **double-pole** term, not on the input or single-leg error budgets.

If $(hk,r)=1$, substitute $a'=hk^2a$ on the right of (6). The resulting value is $\chi(h)J_\chi(N)/\varphi(r)$, where

$$
                 J_\chi(N)=\sum_{a\bmod r}\chi(a)\chi(N-a).
$$

This last sum has an exact evaluation, including the two-primary part. For the additive Fourier transform on $\mathbb Z/r\mathbb Z$ in the negative exponential convention, primitive Gauss induction gives
$\widehat\chi(b)=\chi(-b)\tau_r(\chi)$, zero for $(b,r)>1$. Its real-character square is $\widehat\chi(b)^2=\chi(-1)r\,\mathbf1_{(b,r)=1}$ since $\tau_r(\chi)^2=\chi(-1)r$. These are the same [primitive Gauss identities](r87-spectral-all-scale-exceptional-left-reduction.md#3-an-exact-discrete-form-of-the-residual) used for the hard transfer. Inverting the squared transform gives

$$
                       J_\chi(N)=\chi(-1)c_r(N).
 \tag{7}
$$

In particular when $r\mid N$ the factor in (6) is exactly the previous $\chi(-1)\chi(h)$. Formula (7) requires neither evaluating a generic nonprimitive Jacobi sum nor dropping nonunit residues before (4).

After (6)--(7), all remaining $q$ factors, coprime $k$ completion, and genuine two real geometric kernels are exactly those of the aligned proof. In detail the squarefree $t$ finite coefficients are unchanged and $(k,hr)=1$ in the main term just as before. The two exact residue pole coefficients (3) give (8) of that proof at $q$. Their completed $k$ sum equals its product $\mathcal L(h;q,N)$, with the same power-saving tail and the same treatment of actual nonunits at $q$. Those local identities use only $(q,r)=1$, never $r\mid N$. The short arithmetic normalization is $\chi(h)h^{-\beta}$, while the old factor $\chi(-1)$ is now multiplied by $c_r(N)/\varphi(r)$. The real measure still has physical weight $(N-x)^{\beta-1}x^{\beta-1}\omega(N-x)$ and both original signed kernels since the genuine intervals were never altered. This proves precisely the claimed multiple of the algebraic $\mathcal D_i(N)$ in each color. Neither the scale of the pole nor the actual $t$ endpoint has changed.

All new errors just displayed and the model $k$ tail are stretched exponentials or fixed power savings at scale $Y^\beta$ after fixed $Q_0$ powers. They are in particular $O(Y^\beta G^{O(1)}r^{-1/2})$ since $\log r\le16Z=o(\sqrt G)$. Equation (5) has the same bound because $Q_0\ge r$ and $r_{\rm odd}\ge r/8$, the latter by the primitive quadratic conductor property in the deletion proof. The true parity half-sum gives (1). The same classical lower bound $r>G^J$ for every fixed $J$ eventually, in [R87 Section 1](r87-spectral-all-scale-exceptional-left-reduction.md#1-remove-only-multiples-of-the-exceptional-conductor-in-the-auxiliary-calculation), converts its error to arbitrary log saving. No lower bound on $(1-\beta)G$ has been used.

## 4. Absolute size and pointwise consequences without completing the denominators

We record the absolute model estimate to distinguish it from an assumption on the signed cap. For a fixed short product $h$ write $l_{p,0},l_{p,1}$ for the two local factors of the aligned $\mathcal L(h;q,N)$ at an ordinary prime $p\nmid r$, according to whether $p$ divides $q$. As in [the completed colored caps, (6)--(8)](r93-spectral-completed-colored-caps.md), the coefficient after summing $q\mid t$ has occupied local $(l_{p,0}-p l_{p,1})/(p-1)$ and unoccupied local $l_{p,0}$. Use only the **zero-order** absolute moment there, not any completion of the signed model. Equations (6)--(8) of that proof are direct bounds on its local factors; they apply at every actual $N$ for primes $p\nmid r$, with no alignment requirement on the bound. In particular the generic unoccupied-$h$ envelope product is
$\exp(O(1+\sum_{p\mid N}p^{-\beta}))$, and the occupied correction factors $1+w_p$ can be taken with
$w_p=O(p^{-\beta}+p^{-1})$ if $p\nmid N$ and $w_p=O(1)$ if $p\mid N$. No division by a possibly small unoccupied prime factor is involved. Summing the finite absolute $t$ coefficients is bounded by this Euler envelope over all $t$.

Summing the short weights in absolute value then costs at most
$(\sum_{u\le S}u^{-\beta})^2\prod_p(1+w_p p^{-\beta})^2$,
by expanding the nonnegative divisor weights independently in the two short labels. The prime increments off $N$ are summable uniformly for $\beta\ge.99$. Moreover $\sum_{p\mid N}p^{-\beta}\ll\log\log G$: at $p\le G$ use $p^{1-\beta}\ll1$ from the actual zero range and the reciprocal prime bound; above $G$ use the log product bound on the number of factors. Thus the total short harmonic budget is $\ll G^{O(1)}Y^{(1-\beta)/5}$ as in the earlier moment calculation. The real physical integrals cost at most $Y^{2\beta-1}G^{O(1)}$, and the derivative and conductor factors in $\mathcal D_i(N)$ are $G^{O(1)}$. With the original finite $t$ this proves

$$
       |\mathcal D_i(N)|\ll Y^{2\beta-1+(1-\beta)/5}G^C
                =Y^\beta e^{-4(1-\beta)G/5}G^C.
 \tag{8}
$$

This uses cancellation of the **two local denominator options** before taking absolute values, not a bound on the finite signed caps. It is valid whether or not the auxiliary denominator gap from the completed-cap theorem holds.

The prime-power Ramanujan factor is $\varphi(p^\nu)$ if $p^\nu\mid N$, $-p^{\nu-1}$ if $v_p(N)=\nu-1$, and zero if $v_p(N)<\nu-1$, by the geometric sum over units. Together with multiplicativity this gives $|c_r(N)|\le(r,N)$ and the example of exact vanishing in the theorem. Finally $r/\varphi(r)\ll G^{O(1)}$ for $r\le Q_0$, proving (2) from (1) and (8). The formula makes no smallness claim if most of the conductor divides the target and the zero is extremely close. Any use in a full or original-major formula must still retain the hypotheses and true exceptional target sets of that formula.
