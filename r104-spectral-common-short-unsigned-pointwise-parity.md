# The actual pointwise exceptional parity difference on a common short-unsigned sector

**Scope.** Restrict the two genuine right parity polynomials by the **same** short-label test before forming their exceptional integrals. On this restricted sector the exact two-pole approximation has a full reciprocal power of the original denominator cap as error, at every even target. Its conditional parity-difference lower bound consequently needs no odd conductor overlap. This does not remove the long-unsigned contribution from the original, unrestricted parity difference at disjoint targets. It is not a sign for either full parity, an assertion that an exceptional zero exists, a statement on prime pairs, or a result on Hypothesis S.

Use the original parameters of the [all-scale exceptional term](r87-spectral-all-scale-exceptional-left-reduction.md). Thus $Y\le N\le2Y$ is even, $G=\log Y$, $L=\log N$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$ and $\Delta=2Q_0/Y$. Keep the genuine real half-open $I\subset(N/2,9N/16]$ with bounded real test $\omega$ of bounded pointwise variation, and the fixed admissible $B>B_0>0$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$. When the original Page character $\chi$ exists, it is real primitive of conductor $r\le Q_0$, and $\beta$ is its simple real zero in the original Page strip. Put $\gamma_N=c_r(N)/\varphi(r)$, with its actual Ramanujan sum. If no such character exists define all the exceptional integrals below to be zero.

Following the [unsigned-leg notation](r91-spectral-exceptional-long-unsigned-deletion.md), the true right tuples have squarefree pairwise coprime positive $a,b,c,d$, $m=abcd\in[N/3,2N]$, with

$$
       D<\min(ab,ac)<\sqrt m,\qquad abc>H_0,\qquad
       W(m,a,c)=1-\frac{2\log(ac)}{\log m}.
$$

The original parity coefficients $M_\pm$ use $\mu(b)\mu(c)W(m,a,c)$ and restrict respectively to the even and odd total prime-factor counts in $m$. In particular $M_+-M_-=\mu(m)(M_++M_-)$ on their true support. Let $S=Y^{1/10}$. Define $M_\pm^{bc}$ by inserting the same two conditions $b,c\le S$ into **each** $M_\pm$, and $M_\pm^{ad}$ by inserting $a,d\le S$ into **each** $M_\pm$. All other coefficients, cuts and parity tests remain as before. Let $\mathfrak E_\pm^{bc}$ and $\mathfrak E_\pm^{ad}$ be their exact original exceptional integrals: use the left pole term and the actual auxiliary arcs of the all-scale formula with the indicated true right polynomial substituted. No change is made to the left integrals, $Q_0$, $\Delta$, or their denominator or numerator tests.

**Theorem.** If a Page character exists, uniformly on all the stated hard tests, with a fixed $C$ we have

$$
 \begin{split}
 \mathfrak E_+^{bc}-\mathfrak E_-^{bc}
     &= \gamma_N\mathcal D_1(N)+O(Y^\beta G^C Q_0^{-1}),\\
 \mathfrak E_+^{ad}+\mathfrak E_-^{ad}
     &= \gamma_N\mathcal D_0(N)+O(Y^\beta G^C Q_0^{-1}),
 \end{split}                                                       \tag{1}
$$

where $\mathcal D_i(N)$ are the same literal finite algebraic colors as in the [all-target contraction](r94-spectral-all-target-ramanujan-exception.md). In particular (1) does not assert the displayed estimate for either individual parity on either sector. It uses no quantitative denominator margin and no additional zero-closeness condition.

Assume now the physical and analytic hypotheses of the [target-local margin result](r103-spectral-pointwise-target-local-cap-margin.md): $\omega\ge0$, $\int_I\omega\ge c_{\rm test}Y$ with fixed $c_{\rm test}>0$, $(1-\beta)G\le C_*\log G$ with fixed $C_*$, and $K_z=\prod_{p\le z}p\mid N$ for $z_*\le z\le Z$ with the sufficiently large fixed $z_*$. There is a fixed $C_0$ such that if $\gamma_N\ne0$ and

$$
         \log(Q_0/r)\ge C_0\left\{\log G+
                     \sum_{\substack{p\mid N\\p\nmid r}}p^{1/4-\beta}\right\},
                                                                    \tag{2}
$$

then for all sufficiently large $Y$,

$$
 -\chi(-1)\operatorname{sgn}(\gamma_N)
             \bigl(\mathfrak E_+^{bc}-\mathfrak E_-^{bc}\bigr)
   \gg |\gamma_N|\frac{Y^{2\beta-1}}G
                    \frac{\Sigma^{(r)}(N)}{(\log r)^4}.              \tag{3}
$$

Here $\Sigma^{(r)}(N)$ is the singular factor of the [partial-alignment calculation](r101-spectral-pointwise-partial-alignment.md), filling the $p\mid r$ local factors algebraically but preserving the actual target elsewhere. The conditions allow $(N,r_{\rm odd})=1$. Neither (1) nor (3) limits the size of the actual long-unsigned complement relative to a small $\gamma_N$ at such a target.

## 1. Linear restriction and the exact hard test

Set $A_0=M_++M_-$ and $A_1=M_+-M_-$. Because $m$ is squarefree, on each individual tuple the signs of $A_0$ and $A_1$ are exactly $\mu(b)\mu(c)$ and $\mu(a)\mu(d)$, respectively. Therefore $M_+^{ad}+M_-^{ad}$ is exactly $A_0^{\rm ss}$ of the unsigned-leg calculation, and $M_+^{bc}-M_-^{bc}$ is exactly $A_1^{\rm ss}$. The identities are congruence-free equalities of literal coefficient arrays, prior to integration. The common test used in the two parities within each identity is essential.

For either such right array $A$ write $\mathfrak E(A)$ for its original exceptional integral. By linearity in the right array and the primitive Gauss calculation of the all-scale formula, the exact discrete expression is

$$
 \mathfrak E(A)
    =-\frac r{\varphi(r)}
          \sum_{m\in[N/3,2N]\cap\mathbb Z}
            A(m)\chi(N-m)\mathcal C_{r,Q_0}(N-m)W_{\beta,Q_0}(N-m),
                                                                    \tag{4}
$$

with $\mathcal C_{r,Q_0}(n)=\sum_{t\le Q_0/r,(t,r)=1}\mu(t)c_t(n)/\varphi(t)$ and the same band projection $W_{\beta,Q_0}$ on $[-\Delta,\Delta]$ of $F(x)=\mathbf1_I(x)\omega(x)x^{\beta-1}$ as in that formula. All manipulations giving (4) use the right polynomial linearly and exact finite sums; no replacement for the original right array on an arc is being made.

Each of the two $A_i^{\rm ss}$ is bounded by $C\tau_4(m)$ on the same actual support, since the marks are bounded and each tuple contributes at most one bounded weight. Thus the [sharp hard transfer](r102-spectral-sharp-hard-transfer-odd-overlap.md), Section 1, applies directly to (4): its only right-side input is that pointwise divisor majorant. In detail for $n\ne0$, $|\mathcal C_{r,Q_0}(n)|\ll G^C\tau(|n|)$ by the literal divisor expansion; the genuine $n=0$ term vanishes because $\chi(0)=0$. The relevant sums of $\tau(|n|)\tau_4(N-n)$ on lengths $H\ge\Delta^{-1}$ are $O(HG^C)$ by Cauchy--Schwarz and the local divisor moment (6) there, without any target residue restriction. The band projection's difference from the right-continuous test is a Stieltjes integral of the step error $O(\min(1,(\Delta|n-u|)^{-1}))$. Its central interval and dyadic rings cost $O(\Delta^{-1}G^C)$ after the local moment, uniformly in the shift $u$. Finally the actual values at the designated integers differ from the right-continuous representative by a sum at most $\operatorname{Var}(F)$; after the pointwise subpower divisor bound this error is $O(Y^{\beta-1+o(1)})$. Using $\operatorname{Var}(F)\ll Y^{\beta-1}$ and $r/\varphi(r)\ll G^C$, we obtain exactly

$$
 \mathfrak E(A)=\mathcal H(A)+O(Y^\beta G^C Q_0^{-1}),\qquad
 \mathcal H(A)=-\frac r{\varphi(r)}
     \sum_{n\in I\cap\mathbb Z} F(n)\chi(n)\mathcal C_{r,Q_0}(n)A(N-n).
                                                                    \tag{5}
$$

There is no assumption here about whether a prime of $r$ divides $N$.

## 2. Evaluate the already retained arrays, without a deletion error

Apply Sections 2--3 of the all-target contraction **starting with the arrays $A_i^{\rm ss}$ already present in (5)**. The original deletion of a long unsigned leg, with its rare divisibility class, is not a step in this comparison. Both remaining signed legs are polynomially long on the genuine real slices, by Section 3 of the unsigned-leg calculation, even when the upper hard gate is the true minimum rather than a pair of upper gates.

We detail the inherited errors to distinguish them from the deletion error. At the finite $t\le Q_0/r$ and $q\mid t$ use the same mutual coprimality expansion of the two long signed variables $kz_1,kz_2$, with only the literal constraints at this step. Absolute square-label tail at $k>Y^{1/100}$ costs $O(Y^{\beta-1/100+o(1)})$ with the actual positive floor upper bound; the algebraic extension of $k$ in its final main term has a fixed power saving too. For remaining $k$, both real signed lengths after scaling exceed $Y^{.37}$ on the genuine slices. Enumerate the actual $rq$ residue pairs before assuming any conductor coprimality. The two sequential masked Möbius pole estimates in those residues, with the unchanged intervals, BV mark and real Fubini, give the same total error $O(Y^\beta G^{C_1}Q_0^{C_2}e^{-c\sqrt G})$ as there. It includes the untreated nonunit residue errors; no character pole is inserted in a nonunit $r$-class. These errors, and the fixed-power short or coprimality restoration errors remaining in the finite algebraic expression, are $O(Y^\beta G^C Q_0^{-1})$, since $\log Q_0=o(\sqrt G)$.

On the two actual pole terms the product fiber modulo $r$ is the exact primitive character contraction (6)--(7) of the all-target proof. If a conductor prime divides the two short product times $k$, the primitive local fiber vanishes; no term was pre-removed from the true input on that assumption. On the surviving coprime main terms, the contraction compared with the aligned Gauss sign is exactly $\gamma_N$. The normalized two-adic factors and the opposite geometric orientations stay those of that proof. Its subsequent real integration, $q$-unit and nonunit factors, and coprime $k$ completion give the original finite $\mathcal D_i(N)$ with no change to the $t$ limit. Consequently (5) gives (1), **without** the $r^{-1/2}$ or the rare-class error incurred when converting an unrestricted parity integral to this sector. For $\gamma_N=0$ both combinations in (1) satisfy only its absolute error bound.

## 3. Relative sign on the genuine short sector

The algebraic completion (8) of the target-local margin result, and the exact color-one cap lower (9) there, apply to the literal $\mathcal D_1(N)$ in (1). Neither algebraic calculation uses an odd conductor overlap; in that result overlap was used only to dispose of the raw deletion error on the *unrestricted* parity difference. In particular if $\mathcal A(N,r)=\sum_{p\mid N,p\nmid r}p^{1/4-\beta}$, the algebraic error before multiplication by $\gamma_N$ is

$$
 O_A\left(Y^\beta G^{-A}
       +Y^{2\beta-1}G^{C_3}e^{C_3\mathcal A(N,r)}(Q_0/r)^{-1/4}\right).
$$

The integral in $\mathcal D_1$ has outside sign $-\chi(-1)$ and positive size $\gg Y^{2\beta-1}\Sigma^{(r)}(N)/(G(\log r)^4)$ under the stated actual test. By (2) for sufficiently large $C_0$, by $Y^{1-\beta}\le G^{C_*}$ and by $\log r\ll\sqrt G$, the algebraic error is smaller than this bound by a factor tending to zero. In the raw error of (1), if $\gamma_N\ne0$ then $|\gamma_N|=1/\varphi(r_{\rm odd}/(r_{\rm odd},N))\ge1/r$ including its nonzero two-adic response. Thus after division by the actual response, the raw error is $O(Y^\beta G^C r/Q_0)$, also negligible at (2). This gives (3).

For instance, conditional on such a zero in the requisite margin and on $(r_{\rm odd},K_z)=1$ for fixed allowable $z$, the genuine even targets $N=2^kK_z\in[Y,2Y]$ have odd disjointness, bounded $\mathcal A(N,r)$, and nonzero response when $Y$ is large (the fixed two-power is then supplied by $2^k$). This is a compatible target choice for a hypothetical Page input, not evidence that such an input occurs. At these targets the unrestricted difference additionally contains the original sector $b>S$ or $c>S$, for which the above argument gives no response-relative bound or sign.