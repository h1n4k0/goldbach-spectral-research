# Small powers of the actual denominator product characters

The product of the two progression characters lives on the rational denominator. Splitting that denominator into its shared and coprime parts gives a sharper joint bound for a small set of such products. This removes actual high product characters with a small-conductor power, separately from the alias-leg power cut of R90. The shared-prime cost is summed over the actual aliases and over all denominators, including high prime powers.

## 1. Exact setting and bound

Use the complete even shell, genuinely transported parent $h,f$ profiles, original normalization $J^{-1}$, high-denominator packet $\mathcal C_+(B,R)$, and common taper of [R90](r90-operator-small-power-conductor-aliases.md). Assume the original local Dirichlet GRH at the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. As in [R89](r89-operator-prime-to-denominator-alias-conductors.md), keep $Q\le A\le QH/100$, $A/Q\le K\le4M$, and larger aliases $k>K$. Write $R_*=1+R$.

Let $Z_{\rm pow}$ be the actual retained R90 field for either input allowed there. This includes its true prime-to-denominator alias character power condition, either with or without the exact [R86](r86-operator-long-alias-short-leg-even.md)/[R87](r87-operator-adaptive-raw-minimum-even.md) parity deletions and the corresponding $K\ge2P$. Keep both high individual character selections, the exact $(2k,b)<G$ and $z,w>A$ masks, and the high product selection from [R82](r82-operator-low-product-character-long-quotient.md). The same argument applies if the R90 alias character power restriction is absent, since all estimates below are stable under these fixed leg projections.

For each denominator $b$, fix $C>0,D_*\ge1$ and put

$$
\mathscr S_b
    =\left\{\nu\bmod b:\ \operatorname{cond}(\nu)>D_\times,\
            \operatorname{cond}(\nu^m)\le D_*
            \text{ for some }1\le m\le\lfloor(\log Q)^C\rfloor\right\}.
 \tag{1}
$$

Here $\nu$ is the **product** character of a pair after reduction to $b$, not an individual $r_b$-character of R90. All conductors are primitive inducing conductors. Let $Z_{\rm pow}^{\rm prod}$ be the same actual field with the products in $\mathscr S_b$ omitted on each alias, before the original numerator-specific detuning. Thus all raw regions and signs, the high selections on each leg, the original high product threshold for the other products, and every earlier exact mask are unchanged. For the actual packet norm $\|X\|_{\rm pkt}=(\sum_{j\in\mathcal C_+(B,R)}\|X(j)\|_{\rm HS}^2)^{1/2}$,

$$
\|Z_{\rm pow}-Z_{\rm pow}^{\rm prod}\|_{\rm pkt}
 \ll_{\Gamma,\Theta,C,\epsilon} Q^\epsilon B\sqrt{D_*}\,M
       \left[\frac{R_*^{3/2}+R_*^{5/2}}{Q}
                         +\frac{R_*^{1/2}}S\right].
 \tag{2}
$$

This holds on the whole parent space and after fixed orthogonal spatial compression or restriction to any subset of the specified packet.

At the concrete R89–R90 parameters use $D_*=Q^{3/1000}$, $B=\lfloor Q^{39/100}\rfloor$, $M=Q^{3/5}$, $R=\lfloor Q^{1/400}\rfloor$, $S=Q^{249/250}$, $D_\times=Q^{1/1000}$, and all other original scales. Then (2) is $O_{\epsilon,C}(Q^{-9/4000+\epsilon})$. For the input with the R86/R87 parity deletions, the inherited sharp $\widehat T,\widehat P$ comparison is still $O_{\epsilon,C}(Q^{-1/500+\epsilon})$, now to $Z_{\rm pow}^{\rm prod}$. This is only deletion of one product sector. It does not bound the retained high-product covariance, other Fourier modes, an individual modulus, or weak S.

For example, take odd prime $k=r>D=K$ of size $Q^{11/20}$ and a prime denominator $b$ in the high band, so $(2r,b)=1$; such choices exist for large $Q$ by Bertrand's postulate. A quadratic product $\nu\bmod b$ has conductor $b>D_\times$ but square of conductor one. Choose nonprincipal characters of $b$ on the two legs with that product (avoid the two choices that give a principal on either leg). On $2r$ pair a character of order $r-1$ with its conjugate, so every power in the actual R90 range keeps conductor $r>D$. The coprime Gauss factors of the original incidence are nonzero and both $b$-leg characters are high. This shows new eligibility beyond both R82 and R90, not a lower bound on the size of the field.

## 2. A mixed CRT bound for the true restricted numerator vector

Fix $q=2k,b$, and split the denominator as

$$
b=b_\parallel b_\perp,\qquad
 b_\parallel=\prod_{p\mid q}p^{v_p(b)},\qquad
 q_0=q b_\parallel,\qquad q'=q_0 b_\perp,\qquad (q_0,b_\perp)=1 .
 \tag{3}
$$

For a fixed original orientation $\sigma=(\sigma_1,\sigma_2)$, $A_a$ has unit-residue indicator $q\mid \sigma_1r+\sigma_2s$ and phase $e(-a(\sigma_1r+\sigma_2s)/q')$, for reduced numerator $a\bmod b$, with the R82 negative rational twist. The character-pair coefficient is exactly [R82 (4)–(6)](r82-operator-low-product-character-long-quotient.md#2-exact-dependence-on-the-product-of-the-two-characters): it vanishes unless $\xi\xi'$ is the lift of a unique $\nu\bmod b$, and otherwise depends on $a$ by the factor $\nu(a)$.

The original coefficient before expanding its dependence on $a$ factors under (3). The $q$-divisibility condition lives wholly on $q_0$. The additive phases on the two factors have numerators $a\overline{b_\perp}$ and $a\overline{q_0}$, respectively, with the same orientation coefficients; this is the ordinary CRT identity for the additive character modulo $q_0b_\perp$. The coefficient on $q_0$ is exactly the R82 incidence with denominator part $b_\parallel$ and primitive numerator modulo $b_\parallel$. Its size is $O_\epsilon(Q^\epsilon\phi(q_0)\sqrt{\operatorname{cond}(\nu_\parallel)})$, by R82 (8), where $\nu_\parallel$ is the component of $\nu$ on $b_\parallel$. This is at most $O_\epsilon(Q^\epsilon\phi(q_0)\sqrt{b_\parallel})$. If $b_\parallel=1$, the unit condition alone forces the two $q_0$ characters to be conjugate, and the bound is the elementary $\phi(q_0)$.

On $b_\perp$ the unit variables are unrestricted apart from their own unit masks; the phase gives the product of two primitive-additive Gauss factors. For any character modulo $b_\perp$, including an imprimitive one, each such factor is at most $\sqrt{b_\perp}$, by the unit-exclusion computation in [R81 §2](r81-operator-low-conductor-long-quotient.md#2-exact-local-power-vanishing-and-the-low-conductor-fourth-moment). The trivial modulus has factor one. Since $b_\perp/\varphi(b_\perp)\ll_\epsilon Q^\epsilon$, the coefficient of $\nu(a)$ for every eligible $\xi,\xi'$ in the full incidence therefore has absolute value at most

$$
O_\epsilon(Q^\epsilon\phi(q')\sqrt{b_\parallel}).
 \tag{4}
$$

This improves the relevant joint bound also for arbitrary residue vectors, not just for individual progression coefficients. Indeed let $X,Y$ be two complex vectors on the units modulo $q'$, and use the normalization

$$
X_r=\phi(q')^{-1}\sum_\xi\overline{\xi(r)}\,\mathsf X_\xi,\qquad
        \sum_\xi|\mathsf X_\xi|^2=\phi(q')\|X\|_2^2 ,
$$

and the analogous formulas for $Y$. For a fixed product $\nu$, each $\xi$ has just one partner $\xi'=(\nu\circ\pi)\bar\xi$, where $\pi$ is reduction to $b$. Thus the absolute sum of products $|\mathsf X_\xi\mathsf Y_{\xi'}|$ is at most $\phi(q')\|X\|_2\|Y\|_2$ by Cauchy. Combining this with the two $\phi(q')^{-1}$ factors and (4), the coefficient of $\nu(a)$ in $X^{\mathsf T}A_a Y$ is $O_\epsilon(Q^\epsilon\sqrt{b_\parallel}\|X\|_2\|Y\|_2)$. Orthogonality over the ordinary reduced numerator set gives

$$
\big\|\Pi_{\mathscr S_b}(X^{\mathsf T}A_aY)_{a\bmod b}^*\big\|_2
  \ll_\epsilon Q^\epsilon
          \sqrt{\phi(b)|\mathscr S_b|b_\parallel}\,\|X\|_2\|Y\|_2 .
 \tag{5}
$$

Here $\Pi_{\mathscr S_b}$ is the orthogonal projection onto those multiplicative numerator characters. The reflection $a\mapsto-a$ multiplies the coefficient of each $\nu$ by $\nu(-1)$, so commutes with the projection. In particular (5) is also valid for the symmetric and skew difference incidences of R84/R85, using the same two-vector bound and the triangle inequality. We will use (5) on raw Fourier transformed vectors as well; it does not require an individual pointwise estimate on their character Fourier coefficients. No product projection is moved past the different final fractional detunings.

## 3. Sum the shared-factor cost in the actual raw estimates

Write $n_b=|\mathscr S_b|$ and $L_{k,b}=\sqrt{\phi(b)n_b b_\parallel}$. For a common real-parameter shell test $\omega\in C_c^2((Q,2Q))$ before the fractional detunings, define $K_1=\|\omega\|_\infty+\|\omega'\|_1,\ K'_2=\|\omega''\|_1+K_1/Q$. The genuine pointwise and conditional progression-increment bounds for the actual vectors used by [R89 §3](r89-operator-prime-to-denominator-alias-conductors.md#3-per-alias-weighted-estimates-and-the-exact-masks) hold also with the R90 alias projection on each leg. It is fixed at $q',b,k$ and the projection is a contraction before applying the raw estimates. In this argument those bounds use no reduction of the two leg vector norms from the new selection; all the improvement from (1) is on the joint numerator factor in (5).

Apply the fixed-alias R89 argument for unmodified raw masks with $L_{k,b}$ replacing $b$. For the differences, the true sharp-to-smooth raw comparison uses (5) with the same two pointwise norm estimates. On good pairs the exact symmetric increment uses the same vector on both legs, and the skew estimate uses (5) after the raw-line Fourier transform of its common interval-restricted vector. Thus that transform keeps the smaller numerator factor instead of reverting to the unrestricted $b$. On bad pairs the unmodified derivative estimate applies, and for the sum orientation the early support or the direct shorter raw bound applies as in R89. In every case the true high product projection can be further restricted by $\Pi_{\mathscr S_b}$, since they are diagonal in the same numerator characters and independent of the test and raw variables. This gives a joint HS numerator cost at each $k$ of

$$
O_\epsilon(Q^\epsilon L_{k,b}[K_1+QK'_2]).
 \tag{6}
$$

The aliases being considered satisfy $k>K\ge A/Q$, exactly as required for this fixed-alias bound.

For the post-R86/R87 input, take the difference between this field and the two actual earlier parity deletions projected to the same product sector, as in R89 (8). The exact reflection is compatible with the product mask, and the leg projections are still contractions. With (5) in their pointwise estimates the two earlier deletions together cost

$$
O_\epsilon\!\left(Q^\epsilon L_{k,b}\frac{QP}{k}(E_\infty+E_1)\right)
 \tag{7}
$$

at that alias, with the derivative seminorms of R89. In particular no symmetric or skew raw marginal identity is applied directly to the R87 sharp raw-order mask. The exact R87 complement from the earlier formula preserves the overlap convention.

For fixed $b$, group aliases by the value $d=b_\parallel$, consisting of some subset of the full prime powers of $b$. Necessarily $\operatorname{rad}(d)\mid2k$. For $k\le4M$ there are at most $O(M/\operatorname{rad}(d))$ such aliases, since the step in $k$ is $\operatorname{rad}(d)/(2,\operatorname{rad}(d))$; if the radical exceeds $8M$ there are none. Thus for

$$
\mathfrak w(b)=\prod_{p^e\parallel b}\big(1+p^{e/2-1}\big)
$$

one has

$$
\sum_{k\le4M}\sqrt{b_\parallel(2k,b)}
      \ll M\sum_{\substack{d\mid b\\(d,b/d)=1}}
                    \frac{\sqrt d}{\operatorname{rad}(d)}
      =M\mathfrak w(b).
 \tag{8}
$$

This includes the prime $2$. The original common-divisor mask is only dropped in this positive upper count. In (7) also use $P/k\le P/K\le1/2$ for the reduced input. Therefore, for either input, the larger-alias sum in the common tests costs $Q^\epsilon M\sqrt{\phi(b)n_b}\mathfrak w(b)$ times the same seminorms $K_1+QK'_2$, and if necessary $Q(E_\infty+E_1)$.

## 4. Sum over all actual denominator types and restore the packet

Let $T_m(b)=\#\{\chi\bmod b:\chi^m=1\}$ on units, with $T_m(1)=1$. From the exact power-map fiber count of [R90 §2](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers),

$$
n_b\le D_*\tau(b)\sum_{m\le(\log Q)^C}T_m(b).
 \tag{9}
$$

We need the weighted form of that harmonic average:

$$
\sum_{b\le B}\frac{\mathfrak w(b)^2 T_m(b)}b
                 \ll_{\Theta,C,\epsilon} Q^\epsilon
                                   \quad(1\le m\le(\log Q)^C).
 \tag{10}
$$

To see it, bound the sum by a positive Euler product over $p\le B$, with locally truncated exponent $e\le E_p=\lfloor\log B/\log p\rfloor$. The local summand multiplying $T_m(p^e)$ is exactly

$$
\frac{(1+p^{e/2-1})^2}{p^e}
                        =p^{-e}+2p^{-e/2-1}+p^{-2}.
$$

Put $L=\log Q$. If $p\nmid2m$, then $T_m(p^e)=\gcd(m,p-1)$ for every $e$, as in R90. The sum of the first two weights over $e$ is $O(1/(p-1))$, so their total in the log-Euler upper bound is $O_\Theta(\tau(m)(1+\log\log(10Q)))=o(L)$ by [R90 (5)](r90-operator-small-power-conductor-aliases.md#2-a-harmonic-average-of-character-power-fibers), with prime cutoff $B$ in place of $8M$. For the third weight on $p>\sqrt L$, use $\gcd(m,p-1)\le p$ and $E_p\ll_\Theta L/\log p$. Its sum is $O_\Theta(L/\log L)=o(L)$, since Chebyshev and partial summation give $\sum_{p>x}(p\log p)^{-1}\ll(\log x)^{-1}$. Explicitly the tail integral after using the prime counting bound $O(t/\log t)$ is at most a constant times $\int_x^\infty dt/(t(\log t)^2)$.

For the small primes $p\le\sqrt L$ or the exceptional primes $p\mid2m$, handle the whole local factor by its logarithm. The cyclic and two-component unit group formulas of R90 give $T_m(p^e)\le2m$ uniformly, and $E_p\ll_\Theta L$, so each log is $O_{\Theta,C}(\log(2L))$. There are at most $\sqrt L+O_C(\log(2L))$ of these primes. Summing all these estimates proves the uniform $o(L)$ log-Euler bound needed for (10). There is no requirement that $b$ be squarefree or cube-free; the exponent truncation in this positive product is essential for the third weight.

Since $\phi(b)\le b$ and $b\le B$, (9)–(10), $\tau(b)\ll_\epsilon Q^\epsilon$, and the subpower number of choices of $m$ give

$$
\sum_{b\le B}\phi(b)n_b\mathfrak w(b)^2
                      \ll_{\Theta,C,\epsilon} Q^\epsilon D_* B^2 .
 \tag{11}
$$

In (11) the actual projection still uses (1); the count only enlarged the possibilities for a positive majorant.

Restore the true numerator-specific Taylor weights of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field). At integer offset $\ell$ the effective $K_1$ is $O(1+|\ell|)$; $K'_2,E_\infty,E_1$ cost $O(S^{-1}+(1+|\ell|)^2/Q)$ as in R89. Keep the exterior unit-modulus phase and divide by $J\asymp Q$. Summing the resulting common-test bounds with $|\ell|\le R+1$ produces the three offset factors $R_*^{3/2},R_*^{5/2},R_*^{1/2}$ in (2). For the denominator square sum use (11), yielding $B\sqrt{D_*}$ instead of the unrestricted $B^{3/2}$. This proves the exact packet estimate. At the stated parameters the respective powers are $-19/4000,-9/4000,-13/4000$. The original sharp-shell comparison and separately treated model benchmark have not been altered.
