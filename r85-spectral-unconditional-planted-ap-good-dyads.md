# An unconditional planted AP-radical law along arbitrarily large dyads

**Scope.** The [planted-radical theorem](r84-spectral-planted-ap-radical-full.md) already gives an unconditional genuine original minor bound on a relative-density-one subset of certain sparse divisibility families, but its full Dickman law used historical Dirichlet-GRH inputs. Here there is **no GRH or other unproved input**. For every fixed $0<\vartheta\le1/2$ we obtain the true full and original moving polynomial-major Dickman laws on relative density one of the planted targets along arbitrarily large dyads. The selected dyads follow from the classical uniqueness of an exceptional real zero, not an assumption that exceptional zeros never exist. This is not a theorem on all dyads, exact radicals, predetermined individual targets, or Hypothesis S.

Fix a modulus $q_*$ and a nonempty union $\mathcal P$ of its reduced residue classes, interpreted as a set of primes of density $d\in(0,1]$. Let $Y$ scale the dyad and put

$$
 G=\log Y,\qquad z=\kappa G^\vartheta,\qquad \ell=\log z,\qquad
 K_z=2\!\!\prod_{\substack{2<p\le z\\p\in\mathcal P}}p,\qquad
 \mathcal N_Y=\{N\in[Y,2Y]\cap\mathbb Z:K_z\mid N\}.
 \tag{1}
$$

Here $\kappa>0$ is a sufficiently small fixed constant (needed only at $\vartheta=1/2$). The auxiliary common arcs have $q\le Q_0=\exp(16z)$ and $|\eta|\le2Q_0/Y$ about reduced $a/q$. They are not the original arcs. Keep the exact $M_\pm=(1\pm\mu(m))M_>/2$ from the [pointwise parity formula](r67-spectral-high-mixed-parity-major.md) before its overall subtraction, where $+$ means even squarefree prime-factor count. The true physical support is $m\in V=[N/3,2N]$, $L=\log N$, and the exact cutoffs are $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$ with fixed admissible $B>B_0>0$. The real half-open left interval $I\subset(N/2,9/16\,N]$, $\omega$ with uniformly bounded supremum and variation, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$ are as in the planted theorem. Use $P_{I,\omega}(\phi)=\sum_{n\in I}\lambda(n)\omega(n)e^{2\pi i n\phi}$ and the true right polynomial $\widehat M_\pm(\phi)$. On the original arcs $\mathfrak M_N$ the denominator cap is $N^{1/1000}$ and the radius is $2N^{1/1000}/N$; $\mathfrak m_N$ is their complement.

**Theorem.** There are arbitrarily large $Y$ such that outside a set of
$O((Y/K_z)e^{-\ell^{1/3}}+Y^{1-3/10000})$ targets in $\mathcal N_Y$, both the genuine full correlation and the original $\mathfrak M_N$ integral equal, for each fixed $A>0$,

$$
 \Sigma(N)\mathcal K_{\pm,d}\left(\frac{2B}{\vartheta},\frac{B-B_0}{\vartheta}\right)
               \int_I\frac{\omega(y)}{\log(N-y)}\,dy
  +o\!\left(\frac{\Sigma(N)|I|}{L}\right)+O_{A,B,B_0}(YG^{-A}).
 \tag{2}
$$

The two constants are from the [generalized Dickman law, (4)](r83-spectral-ap-radical-major-law.md), with no quotient or modification of the genuine singular factor $\Sigma(N)$. The original minor remains $O(Y^{1-1/40000})$ there. The exceptional set and the error are simultaneous over the true hard/BV tests and both signs. The ratio of the exceptional count to $|\mathcal N_Y|\sim Y/K_z$ tends to zero. In particular the explicit positive odd constants for $d\le1/2$ and sufficiently small **fixed** positive scaled gap from the AP-radical law also apply here on the ordinary inverse-log length cells with $\omega=1$. This is a signed mixed-composite correction and not a prime-pair count.

## 1. Good dyads are unconditional

Let $a_0>0$ be a sufficiently small fixed constant, chosen using the classical zero-free regions for $\zeta$ and Dirichlet $L$-functions. Call $G$ good if there is no primitive real character of conductor at most $Q_0=\exp(16\kappa G^\vartheta)$ with a real zero $\beta>1-4a_0/\sqrt G$. We use [Montgomery–Vaughan, Chapter 11, Corollary 11.10](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF): for every conductor cap $Q$ there is at most one zero, counted in the product over primitive characters up to that cap, in the real interval $\beta\ge1-c_P/\log(4Q)$ for an absolute $c_P>0$. It is necessarily a real zero of a quadratic character. If the bad scales are bounded, all sufficiently large scales are good. Otherwise take an arbitrarily large bad $G$ and a zero with $b=1-\beta<4a_0/\sqrt G$. Put $G'=(8a_0/b)^2>4G$. The old conductor is still at most $Q_0(G')$, and its zero now fails the bad test at $G'$, having $b=8a_0/\sqrt{G'}$. Nevertheless it belongs strictly to the Page interval at $Q_0(G')$. For $\vartheta<1/2$ this holds for large $G'$ since $b\log(4Q_0(G'))\to0$; at $\vartheta=1/2$ it holds by taking $128a_0\kappa<c_P/2$. Any new zero giving a bad $G'$ would be different and would also lie in that Page interval, which is impossible. Thus $G'$ is good. This proves the existence of unbounded good scales, without assuming there are only finitely many exceptional zeros.

We spell out the uniform analytic replacements on such a scale. Take $T_*=e^{\sqrt G}$ and $\sigma_*=1-a_0/\sqrt G$. For $q\le Q_0$, $|\operatorname{Im}s|\le T_*$ and $\operatorname{Re}s\ge\sigma_*$, the classical regions exclude all zeros. Indeed $\log(q(4+T_*))\le2\sqrt G$ for large $G$ if $\kappa$ is small at the endpoint, and choose $a_0$ so the contour lies inside the half-width regions of [Montgomery–Vaughan, Theorems 11.3–11.4](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF) and [Theorems 6.6–6.7](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287). An exceptional real zero still allowed further to the left is at distance at least $3a_0/\sqrt G$ from the rectangle. An imprimitive character has only extra Euler zeros on $\operatorname{Re}s=0$, so the test on primitive conductors suffices.

For nonprincipal characters the bounds in Theorem 11.4 give $1/L(s,\chi)$ and $L'(s,\chi)/L(s,\chi)$ of size $G^{O(1)}$ on the contour. Indeed the exceptional-distance case of that theorem uses $O(\log(q(4+|\operatorname{Im}s|)))$ away from the zero, and near it uses $1/|s-\beta|$ and $O(\log q)$, all bounded by fixed powers of $G$. For the principal character use $\zeta$ and its finite Euler factors at $p\mid q$. At $\operatorname{Re}s\ge\sigma_*$ one has $p^{a_0/\sqrt G}\le O(1)$ for $p\mid q$, and for all large $G$ also $\operatorname{Re}s>.9$. The inverse finite product is at most $\exp(O(\sum_{p\mid q}p^{-1}))=G^{O(1)}$, and its logarithmic derivative is $O(\log(2q))$ there. The $\zeta$ bounds of Theorem 6.7 apply, with the pole term in its logarithmic derivative of size $O(\sqrt G)$ on the new contour. The only pole crossed for the negative logarithmic derivative is the simple principal one at $1$; the reciprocal $L$-function has no pole in the rectangle.

Thus for some fixed $c_0>0$ and $Y^{1/100}\le X\le4Y$, uniformly over $q\le Q_0$, one gets

$$
 \sum_{n\le X}\mu(n)\chi(n)\ll Xe^{-c_0\sqrt G},\qquad
 \sum_{n\le X}\Lambda(n)\chi(n)
       =\mathbf1_{\chi\ {\rm principal}}X+O(Xe^{-c_0\sqrt G}).
 \tag{3}
$$

For detail, take the Perron integral for $1/L$ or $-L'/L$ on $\sigma_0=1+1/\log X$, height $T_*$. Replace the evaluation point by $\lfloor X\rfloor+1/2$ to preserve the sharp sum. The truncated Perron error by [Montgomery–Vaughan, Corollary 5.3](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/dirichlet-series-ii/40A964C62758CB5A294D9C158B5F9036) is $O(XG^{O(1)}/T_*)$: near $X$ sum $\min(1,X/(T_*|n-X|))$ using the half-integer distances and $|\Lambda(n)\chi(n)|\le\log n$, and off that range use absolute convergence at $\sigma_0$. The horizontal integrals after shifting cost $XG^{O(1)}/T_*$ as well. The new vertical integral costs $X^{\sigma_*}G^{O(1)}$ (the $1/s$ integration costs $O(\log(2T_*))$), giving $Xe^{-c_0\sqrt G}$ since $\log X\ge G/100$. The shift by at most $1/2$ in the principal main is harmless. All constants can be chosen uniformly as $\kappa$ decreases subject to $16\kappa\le1/2$: the bounds used only $\log q\le\sqrt G/2$, the stated good-scale margin, and fixed strip constants. This matters when shrinking $\kappa$ below to absorb the circular-method losses.

Orthogonality gives the reduced-class prime progression estimate with main $X/\varphi(q)$ and the same total error; replacing $\Lambda$ by $\lambda$ loses $O(\sqrt X\log^2 X)$. The reduced-class Möbius sum has only error. We need also the masked bound in **every** residue, not only the units:

$$
 \sum_{\substack{n\le X\\n\equiv b\ (q)\\(n,w)=1}}\mu(n)
       \ll Xe^{-c_1\sqrt G}
       \quad\bigl(Y^{1/20}\le X\le4Y,\ q\le Q_0,\ w\le Y^C\bigr)
 \tag{4}
$$

for any fixed $C$ and a fixed $c_1>0$. First take $(b,q)=1$ on the slightly larger lower range $X\ge Y^{1/30}$. The convolution of $\mu$ with the indicator of integers supported only on primes dividing $w$ equals $\mu(n)\mathbf1_{(n,w)=1}$, by Euler factors. For a smoothing divisor $h\le\sqrt X$, now coprime to $q$, apply (3) in the reduced class $b h^{-1}$ at $X/h\ge Y^{1/60}>Y^{1/100}$. Summing its reciprocal losses costs $w/\varphi(w)\ll_C\log\log(3Y)$. For $h>\sqrt X$ use $X/h$ and Rankin with exponent $1/4$: the contribution is at most $X^{1-1/8}\prod_{p\mid w}(1-p^{-3/4})^{-1}\ll_\epsilon X^{1-1/8}w^\epsilon$, negligible for suitably small fixed $\epsilon$. The last Euler bound follows by bounding each sufficiently large local factor by $p^\epsilon$.

For any $b$, put $g=(b,q)$. If $(g,w)>1$ or $\mu(g)=0$, the masked sum is zero. Otherwise write $n=g u$ in the reduced class $b/g\bmod q/g$. The identity $\mu(gu)=\mu(g)\mu(u)\mathbf1_{(u,g)=1}$ makes its unit-class mask $gw$, still of fixed polynomial size, and $X/g\ge Y^{1/30}$ in the range of (4), since $q\le Y^{o(1)}$. The reduced estimate just proved yields (4), without assuming that $b$ was a unit originally. On each hard signed sector below the variable itself is above $Y^{1/10}$ up to a fixed constant, so differences of such prefixes give (4) at the needed scale, even when the interval is short or empty.

## 2. Unconditional auxiliary majors at the planted scale

Two extra-prime checks hold outside a relative set $O(e^{-\ell^{1/3}})$ in $\mathcal N_Y$:

$$
 \sum_{\substack{p\mid N\\p\nmid K_z}}\frac{\log p}{p}\le\ell^{1/3},
 \qquad
 \sum_{\substack{p\mid N\\p\nmid K_z}}p^{-3/4}\le z^{1/2}.
 \tag{5}
$$

The first is the exponential moment in the planted theorem. For the second expand the exponential over squarefree $a\mid N/K_z$ with $(a,K_z)=1$ and coefficients $\prod_{p\mid a}(e^{p^{-3/4}}-1)$. The upper count for multiples of $a$ is $2Y/(K_z a)$, and the positive Euler product has convergent increments $O(p^{-7/4})$. Markov loses at most a relative $O(e^{-\sqrt z})$, which is smaller than the stated loss. The prime number theorem in the fixed AP gives $\log K_z\sim dz$, hence $\log K_z\le 2z$ for large $Y$.

On a good dyad apply the arithmetic of [the common auxiliary-major calculation](r80-spectral-whole-mixed-parity-density.md#1-unconditional-parity-calculation-on-common-polylogarithmic-arcs) at the present $Q_0$, using (3)–(4) instead of Siegel–Walfisz. Here is why the larger cap is valid before rational completion. In the untwisted and twisted strips the large signed sectors keep the other three factors of product $h$ fixed. Their signed variable is on a genuine interval at scale $N/h\gg Y^{1/10}$, with coprimality to the fixed factors and each actual residue; the twisted low mixed term has an even larger signed variable. Estimate (4) is uniform there. Summing the reciprocal triple labels, residue classes, and the slow phase variation costs $G^{O(1)}Q_0^2$. In the complementary positive bulk and the untwisted low term the two counted variables are polynomially long, and the squarefree floor plus the $3/4$ harmonic-convolution errors of the [squarefree CRT proof](r63-spectral-full-squarefree-crt-strip.md#2-exact-squarefree-bulk-densities-with-the-additive-phase) retain a fixed power saving even after every fixed power of $Q_0$, since $Q_0=Y^{o(1)}$. There is no extra analytic assumption on those positive variables. The left constant term is $\mu(q)\widehat{\mathbf1_I\omega}(-\eta)/\varphi(q)$ in the $e^{-2\pi i\eta u}$ Fourier convention, by the prime progression estimate and the Ramanujan sum; the actual slow factor is $\int_I\omega(u)e^{2\pi i\eta u}du$. Its error also costs at most $G^{O(1)}Q_0^2$ times the exponential error of (3). Nonunit primes are absent on the original hard left support, since $q\ll Y$. Nonsquarefree $q$ have zero left main; for them use the trivial right bound $O(YG^3)$.

The total auxiliary arc measure is $O(Q_0^3/Y)$, and the trivial polynomial bounds are $YG^{O(1)}$. Hence the integrated analytic errors from (3)–(4) are $O(YQ_0^5G^{O(1)}e^{-c_2\sqrt G})$ for a fixed $c_2>0$ chosen no larger than $c_0,c_1$, and the positive-variable errors retain a power saving. At $\vartheta<1/2$ the first error is exponentially small in $\sqrt G$ for any fixed admissible $\kappa$. At the endpoint choose also $80\kappa<c_2/2$. The constants in (3)–(4) are uniform under this choice by the previous section. No uncontrolled power of $Q_0$ enters this exponential error.

Before completing, the formal right profile for squarefree $q$ has supremum plus total variation $O(G^{C_3}C_4^{\omega(q)}/q)$ by the occupancy argument in the same auxiliary-major calculation; this bound is on formal density factors and does not require progression estimates beyond the auxiliary arcs. The slow Fourier integral can be extended to the line at cost $O(YQ_0^{-1}G^{O(1)}(1+\log Q_0)^{O(1)})$, using the two BV profiles as there. Pointwise, the normalized rational tail is bounded by

$$
 G^{O(1)}Q_0^{-1/4}\mathcal A(N)^{C_5},
 \qquad
 \mathcal A(N)=\prod_{\substack{p\mid N\\p>2}}
      \left(1-\frac{p-1}{p^2-2}p^{1/4}\right)^{-1},
 \tag{6}
$$

by the [rational-tail estimate in the radical criterion](r81-spectral-radical-criterion-and-log-exceptions.md#1-complete-the-auxiliary-major-at-each-such-target). This uses the positive $q^{1/4}$ insertion and thus holds also at the present nonpolylogarithmic cap. On the second part of (5),
$\log\mathcal A(N)\ll\sum_{p\le z}p^{-3/4}+z^{1/2}\ll z^{1/4}+z^{1/2}=o(z)$. The right side of (6) therefore decays exponentially in $z$. Both completion errors are $O_A(YG^{-A})$ after integration. These bounds are pointwise on (5); they do not use an exceptional count on the ambient dyad to justify rational completion on the sparse family.

Thus the actual auxiliary major integral equals the real completed density (2) of [the whole mixed proof](r80-spectral-whole-mixed-parity-density.md), with the true $D,H_0,V$ and an $O_A(YG^{-A})$ error. The remaining operations there, including signed cap completion and the hard short cut, are unconditional real integral and ordinary reciprocal-Mertens calculations; the large-log clipping tails of the primitives can also be bounded by that proof's tail estimate with $\log\mathcal A(N)=o(z)$ and large argument comparable to $G$. In particular this density is the exact finite parity bracket from the pointwise formula, not yet a claim about the original arc set.

The convergence argument in Sections 2–3 of [the planted theorem](r84-spectral-planted-ap-radical-full.md#2-perturb-the-genuine-radical-in-log-coordinates) evaluates that real bracket unconditionally on the first part of (5). It used only the extra-prime probability convolution, the uniform $v f$ bound, and the signed mass cancellation, not GRH. The positive terminal limit is $(B-B_0)/\vartheta$ and the positive shift is $2B/\vartheta$, since $\log z\sim\vartheta\log G$ and $L=G+O(1)$. The cusp when $d\le1/2$ is therefore handled exactly as there by weighted $L^2$ away from zero and global $L^1$. It follows that the true auxiliary major has the right side of (2) on the set (5).

## 3. The two actual arc complements

For the common auxiliary complement, use the exact true-divisor-label partition of [the moving label proof](r80-spectral-adaptive-divisor-label-minor.md#1-arithmetic-axes-rather-than-threshold-freezing), but without any target gcd masks or moving arc boundaries. In a fixed dyadic level partition on the right put each true tuple in its assigned cells for $m,ab,ac,abc$, keeping the fixed upper gate $\min(ab,ac)<\sqrt m$ and its sign and parity. The moving hard lower and physical cutoffs then select unions of canonical cells on these axes. At each level the sum of the squared right coefficient norms is at most $\sum_{m\le5Y}\tau_{16}(m)\ll YG^{15}$: the sum of underlying tuple counts across disjoint cells is at most $\tau_4(m)$, whose square equals $\tau_{16}(m)$ on squarefree $m$. This estimate needs no freezing of $D$ or $H_0$ at a mesh that would depend on $Q_0$.

On the common auxiliary complement, the usual Dirichlet approximation with denominator limit $\lceil Y/Q_0\rceil$ finds a reduced denominator $q>Q_0$; otherwise the point would lie on a removed arc. The Vaughan bound as in [the common-complement proof](r80-spectral-whole-mixed-parity-density.md#3-genuine-full-and-original-polynomial-major) bounds each hard left polynomial by $O(YQ_0^{-1/2}G^4)$ (the prime-power error and $Y^{4/5}$ are smaller since $Q_0=Y^{o(1)}$). At a fixed left dyadic level the sum of squares across disjoint left intervals is pointwise bounded by this supremum times $O(Y)$, because their total absolute $\lambda$ mass is $O(Y)$. Each hard rectangle is a union of $G^{O(1)}$ canonical left/right cells over the fixed axes, so Cauchy–Schwarz and Bessel over integer targets bound the sum of the squared supremum of the common-complement Fourier coefficients by $O(Y^3 G^{C_6}Q_0^{-1/2})$, with fixed $C_6$. In detail, sum the Bessel estimates for each product of a left cell polynomial and a right cell polynomial, and use the left pointwise square bound times the summed right torus energies. The bounded variation left tests follow from partial summation on the same integer prefixes. All counts are for the actual right labels and exact cutoff endpoints.

Markov at $Y e^{-z}$ thus excludes $O(YG^{C_6}e^{-6z})$ ambient targets, since $Q_0=e^{16z}$; on $\mathcal N_Y$ this has relative size $O(G^{C_6}e^{-4z})$ by $K_z\le e^{2z}$. The common-complement integral is at most $Ye^{-z}$ off this set, and hence absorbed by the error in (2). Fourier inversion now proves (2) for the **full** sum. This uses the true auxiliary integral and its true complement, not equality of an auxiliary arc set with the original one.

Finally apply the [unconditional original-moving-minor theorem](r79-spectral-original-minor-power-exception.md) to the two fixed parity masks and the original arcs. Its exceptions cost $O(Y^{1-3/10000})$ in the entire dyad, negligible relative to $Y/K_z=Y^{1-o(1)}$ here, and its original minor is $O(Y^{1-1/40000})$. Subtract this actual minor from the full result to obtain (2) on the original $\mathfrak M_N$. The exponential auxiliary exceptions and the second part of (5) are absorbed in the stated relative $e^{-\ell^{1/3}}$ count. This proves the unconditional good-dyad law and explains precisely which restriction replaced the earlier GRH input.
