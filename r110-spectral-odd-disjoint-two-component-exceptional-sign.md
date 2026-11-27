# Two sufficient signs for the genuine odd-disjoint exceptional parity difference

For an actual odd Page conductor disjoint from the even target, the genuine parity difference of the **exceptional correction** has two pieces with different arithmetic signs. If the signed pole reinforces the separated unsigned piece, or if the pole is sufficiently small because of the real zero gap, their sum has the sign of the unsigned piece. These are pointwise sufficient criteria on the original hard tests. Neither concerns the parity difference of the full mixed correlation, claims the existence of a Page zero, nor estimates the close competing-sign case.

## 1. Setup and statement

Use the genuine dyad $Y\le N\le2Y$, even target $N$, $G=\log Y$, $g=\log G$, $Q_0=\exp(16\sqrt G/g)$ and the original fixed admissible $B>B_0>0$ of the [odd-disjoint two-positive formula](r106-spectral-odd-disjoint-two-positive-unsigned-mode.md). Write $r\le Q_0$ for its actual odd squarefree primitive conductor, $\chi$ for its real character and $\beta$ for its simple real zero in the original Page strip. Require $(N,r)=1$. The genuine half-open $I\subset(N/2,9N/16]$ and bounded pointwise-BV weight $\omega$ are the same as in that theorem. Assume $\omega\ge0$ and $\int_I\omega(u)\,du\ge c_{\mathrm{test}}Y$ for a fixed $c_{\mathrm{test}}>0$. Put

$$
 \begin{split}
 \gamma_N&=\frac{\mu(r)}{\varphi(r)},\qquad b=1-\beta,\qquad
 H=\omega(r)+\sum_{p\mid N}p^{-3/4},\\
 \mathcal I_\beta&=\int_{N-I}
      \frac{\omega(N-m)(N-m)^{\beta-1}}{\log m}\,dm,\qquad
 M_N=\frac{\Sigma(N)}{r}\mathcal I_\beta ,
 \end{split}                                                     \tag{1}
$$

where $\omega(r)$ in $H$ counts prime divisors and $\Sigma(N)$ is the binary singular series at the actual target. In particular $M_N\gg Y^\beta/(rG)$ uniformly on these tests. Impose the local mask and rational-cap conditions

$$
                   H\le g^{1/3},\qquad
                   \log(Q_0/r)\ge g^3 .                           \tag{2}
$$

Fix $\eta>0$, and assume the separated signed shifts of the [unsigned pointwise formula](r109-spectral-pointwise-separated-unsigned-parity.md):

$$
 \left|\sum_{p\mid r}\varepsilon_p\log p\right|\ge(2B+\eta)g
 \quad\text{for every nonzero }(\varepsilon_p)_{p\mid r}
                        \in\{-1,0,1\}^{\omega(r)}.                \tag{3}
$$

Write $\Delta\mathfrak E=\mathfrak E_+-\mathfrak E_-$ for the genuine exceptional correction of the two original parities, with the $+$ parity convention of the two-positive theorem.

**Theorem.** Under the above assumptions the following hold as $Y\to\infty$.

1. **Reinforcing residues for a near zero.** Fix $C_*>0$. Require $bG\le C_*g$, and assume the same sufficiently large fixed primorial $K_{z_*}=\prod_{p\le z_*}p$ divides $N$ as in the fixed-planting signed-pole bound of the [partial alignment proof](r101-spectral-pointwise-partial-alignment.md). If $\chi(N)=\mu(r)\chi(-1)$, then
   $-\chi(N)\Delta\mathfrak E\ge(1-o(1))M_N>0$.
   The same algebraic signed pole, with its exact factor $\gamma_N$, is retained. There is no lower bound on the proportion of $r$ contained in $N$; here it is completely disjoint.
2. **Large gap.** There is a sufficiently large fixed $C_{\mathrm{gap}}$ such that if $bG\ge C_{\mathrm{gap}}g$, no planting or character-sign condition beyond $(N,r)=1$ is needed, and
   $\Delta\mathfrak E=-\chi(N)M_N+o(Y^\beta/(rG))$.
   In particular it has sign $-\chi(N)$.

For an actual prime conductor the separation (3) is automatic eventually. In the first criterion the reinforcing residues then comprise one half of the unit classes. The lower cap margin (2) is still needed even for a prime conductor. Neither branch makes a conclusion when the stated sufficient conditions fail.

## 2. Start from the sharp raw decomposition, not the old transport error

Let $\mathcal D_1$ be the *finite algebraic* signed-pole color one, with its original $t\le Q_0/r$, and let $\mathcal U$ be the actual unsigned term (2) of the separated formula. Cancel color zero by taking the difference of the genuine $+$ and $-$ expressions (5) of the odd-disjoint two-positive theorem. The exact surviving terms and its raw error are

$$
        \Delta\mathfrak E=\gamma_N\mathcal D_1+\mathcal U
                               +O(Y^\beta G^{C_0}/Q_0).          \tag{4}
$$

Their coefficients have no remaining $1/2$. The two terms are kept separately: $\mathcal D_1$ is the same algebraic pole used in the alignment calculation, while $\mathcal U$ includes the exterior sign of the unsigned contribution and its literal finite denominator restriction.

Apply the separated formula (4) with conditions (2)–(3). Since $g^3$ exceeds every fixed $C_A(g+H)$ for large $Y$, its first error on the $Y^\beta/(rG)$ scale is $o(1)$ and its second error is $O_A(Y^\beta/(rG^A))$ for every fixed $A$. The raw term in (4) is also $O_A(Y^\beta/(rG^A))$, because $r/Q_0\le e^{-g^3}$. Consequently

$$
        \Delta\mathfrak E=\gamma_N\mathcal D_1-\chi(N)M_N
                                      +o(Y^\beta/(rG)).          \tag{5}
$$

These are errors at the genuine disjoint response scale. In contrast, the older $O(Y^\beta G^C r^{-1/2})$ of the all-target single-expression transfer would not give (5) on completely disjoint targets. That error is not used here.

## 3. Sign of the algebraic pole and reinforcement

The real comparison (5) and the cap lower bound (7) of the partial alignment proof apply to $\mathcal D_1$ itself, **before** its Section 3 divides the old transport error by the target response. To clarify that application in the fully disjoint setting, the algebraic expression in that proof is exactly the same one as in (4). The finite $t$ is unchanged before its controlled completion. In Sections 1–2 of the partial alignment proof, the local $q$ and $t$ identities test the actual $p\mid N$ only off $r$, and all $p\mid r$ have zero short-prime coefficient independent of their alignment. Such a zero coefficient is covered by the same nonnegative quotient against the all-minus comparison arrays. At $K_{z_*}\mid N$ all the required small primes are excluded. The identified Euler mass $\Sigma^{(r)}(N)$ is $\Sigma(Nr)$ for disjoint $r,N$, but this changes neither the physical $N$ nor the true test window. In particular none of those steps requires the missing odd conductor factor to be small.

Thus in the first criterion one may write, for every fixed $A$,

$$
 \begin{split}
 \mathcal D_1&=-\chi(-1)J_\chi+O_A(Y^\beta G^{-A}),\\
 J_\chi&=\int_{N-m\in I}
   \frac{\omega(N-m)(N-m)^{\beta-1}m^{\beta-1}}{\log m}
                           B_1(m)\,dm\\
 &\gg \frac{Y^{2\beta-1}\Sigma(Nr)}{G(\log r)^4}>0.
 \end{split}                                                      \tag{6}
$$

Here $B_1$ is the completed cap from the cited proof, not an unsigned model for it. The inequality uses the original nonnegative test of macroscopic mass and $m,N-m\asymp Y$. This comparison does not assume a sign for the genuine full exceptional difference.

For reference the error in (6) is smaller than $J_\chi$: $bG\le C_*g$ gives $Y^{\beta-1}\ge G^{-C_*}$, $\log r\ll\sqrt G$ and $\Sigma(Nr)\gg1$, so any $A>C_*+4$ suffices. Also, after restoring $\gamma_N$, the error in (6) is $o(Y^\beta/(rG))$ for a large fixed $A$, since (2) implies

$$
       \frac r{\varphi(r)}
               \le (3/2)^{\omega(r)}
               \le \exp(O(g^{1/3}))=G^{o(1)}.                   \tag{7}
$$

Substitute (6) in (5). On the prescribed reinforcing residues, the sign of $-\chi(-1)\gamma_N$ is $-\chi(N)$, and therefore

$$
      -\chi(N)\Delta\mathfrak E
           =|\gamma_N|J_\chi+M_N+o(Y^\beta/(rG)).                 \tag{8}
$$

The unsigned scale suffices to absorb the genuine raw error even when the signed-pole term is much smaller than the unsigned term. This proves the first criterion. If the two signs oppose, the same formula before sign simplification does not compare their magnitudes.

## 4. Sufficient large-gap pole bound

For the second criterion use only the direct finite-pole estimate proved near the end of the [all-target Ramanujan calculation](r94-spectral-all-target-ramanujan-exception.md) before it bounds the actual transport error. Its absolute zero-order $q$-before-$t$ Euler estimate applies off the conductor at these literal $N,r$. The two short weights cost $Y^{(1-\beta)/5}$ times a power of $G$, and the real physical integral and prefactors cost $Y^{2\beta-1}$ times a power of $G$. This is an estimate at the original finite $t$, not a new infinite completion:

$$
      |\mathcal D_1|\ll Y^{2\beta-1+(1-\beta)/5}G^{C_1}
                    =Y^\beta G^{C_1}e^{-4bG/5}.                  \tag{9}
$$

Together with (7), this gives $|\gamma_N\mathcal D_1|=o(Y^\beta/(rG))$ once the fixed $C_{\mathrm{gap}}$ is chosen, for instance, larger than $5(C_1+3)/4$. No planting is used in (9). Equation (5) now proves the second criterion.

## 5. Conditional prime-conductor interpretation

The automatic separation for a prime $r$ is exactly the one in the unsigned proof: the original strip and the classical Siegel bound as used in the [all-scale exceptional reduction](r87-spectral-all-scale-exceptional-left-reduction.md) force $\log r/g\to\infty$. For a prime $r$, the nonzero signed shifts are only $\pm\log r$, and $\mu(r)=-1$. The quadratic character is nontrivial on the units, so precisely one half of their classes satisfy $\chi(N)=-\chi(-1)$. For the fixed $K_{z_*}$, $r\nmid K_{z_*}$ eventually, and multiplication by $K_{z_*}$ permutes units modulo $r$. In a hypothetical dyad satisfying the prime conductor, gap and rational margin hypotheses of the first criterion, the reinforcing planted family has size

$$
      \frac{Y}{K_{z_*}}\,\frac{r-1}{2r}+O(r).
                                                               \tag{10}
$$

This is counting the complete residue blocks of the integer variable $N/K_{z_*}$; all such $N$ are even. Since $r\le Q_0=Y^{o(1)}$ and $K_{z_*}$ is fixed, the ambient $O(Y e^{-g^{1/3}/2})$ exceptional set for the small target mask in the unsigned proof has relative size $o(1)$ in this **whole** family of reinforcing residues. It need not be divided by the size of an individual residue class. Thus the first criterion describes the stated sign on relative density one of the complete reinforcing family when its dyad hypotheses hold and the tests have the stated uniform mass. This is conditional on such a dyad, not a statement about density of qualifying dyads or existence of a Page zero.
