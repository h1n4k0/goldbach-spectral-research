# The only remaining all-scale planted correction is one exceptional left residue

**Scope.** On every sufficiently large dyad, the genuine full and original moving polynomial-major mixed-strip correlations on relative density one of the planted AP targets equal the [unconditional Dickman base](r86-spectral-universal-good-scale-windows.md) plus one explicit correction. The correction is from the possible single Page zero on the **left prime leg** and retains the actual, unmodified right arithmetic. The entire statement is unconditional. The correction is negligible on a strictly enlarged sufficient scale set, but its smallness for an ultra-close zero is not proved. This is not an uncorrected law on all scales, a theorem on exact radicals or fixed targets, or Hypothesis S.

Use $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16 Z}$, $\Delta_0=2Q_0/Y$, and the same true coefficients $M_\pm$, hard tests $I,\omega$, and original arcs $\mathfrak M_N,\mathfrak m_N$ as in the [universal-scale theorem](r86-spectral-universal-good-scale-windows.md). In particular $M_\pm$ are the even/odd **squarefree factor-count** selectors of the actual above-BV mixed coefficient, with both literal cutoffs and physical support. Write $e(t)=e^{2\pi i t}$ and $\widehat M_\pm(\phi)=\sum_m M_\pm(m)e(m\phi)$, retaining its dependence on $N$. Fix a nonempty set $\mathcal P$ of reduced classes of a fixed modulus, of prime density $d>0$, and $0<\epsilon<1/2$. At each dyad choose any $G^\epsilon\le z\le Z$, with $K_z=2\prod_{2<p\le z,\,p\in\mathcal P}p$, $K_z\mid N$, and $\theta_z=(\log z)/\log G$. Put

$$
 \mathcal D_\pm(N;I,\omega;z)=
 \Sigma(N)\mathcal K_{\pm,d}\!\left(\frac{2B}{\theta_z},
                               \frac{B-B_0}{\theta_z}\right)
       \int_I\frac{\omega(u)}{\log(N-u)}\,du ,
 \tag{1}
$$

using the genuine singular series and the [actual-cut Dickman coefficients](r83-spectral-ap-radical-major-law.md). Keep the fixed admissible cutoffs $B>B_0>0$ and $L=\log N$.

Let $\chi^*$ be the primitive real character of conductor $r\le Q_0$ with a real zero $\beta>1-4a_0/\sqrt G$ if it exists, where $a_0>0$ is chosen sufficiently small as in the [good-dyad proof](r85-spectral-unconditional-planted-ap-good-dyads.md#1-good-dyads-are-unconditional), and if necessary further decreased for the contour below. There is at most one such zero and character, by Page. For $r\mid q$ write $\chi_q$ for the induced character modulo $q$ and $\tau_q(\chi_q)=\sum_{b\bmod q}\chi_q(b)e(b/q)$. In the presence of the zero define $V_\beta(\eta)=\int_I\omega(u)u^{\beta-1}e(\eta u)\,du$ and the actual right-dependent correction

$$
 \mathfrak E_\pm=
 -\sum_{\substack{q\le Q_0\\r\mid q}}
       \frac{\tau_q(\chi_q)}{\varphi(q)}
   \sum_{\substack{a\bmod q\\(a,q)=1}}\chi_q(a)
     \int_{-\Delta_0}^{\Delta_0}
          V_\beta(\eta)\widehat M_\pm(a/q+\eta)
                                e(-N(a/q+\eta))\,d\eta .
 \tag{2}
$$

Without the zero set $\mathfrak E_\pm=0$.

**Theorem.** On every sufficiently large dyad, for each prescribed $z$ as above, outside
$O((Y/K_z)e^{-(\log z)^{1/3}}+Y^{1-3/10000})$ members of the planted family, both the full correlation and the integral on the **original** $\mathfrak M_N$ are

$$
 \mathcal D_\pm(N;I,\omega;z)+\mathfrak E_\pm
      +o\!\left(\frac{\Sigma(N)|I|}{L}\right)+O_{A,B,B_0}(YG^{-A})
 \tag{3}
$$

for each fixed $A>0$. Errors are uniform in $z$ for fixed $\epsilon,\mathcal P,B,B_0$, and the exceptional sets are per prescribed $z$ and simultaneous over both signs and the usual tests. The exact original moving minor keeps its unconditional $O(Y^{1-1/40000})$ bound there. Uniformly even before discarding exceptional targets, the correction in the presence of the zero satisfies

$$
               |\mathfrak E_\pm|\ll Y^\beta G^{C}
                       =Y e^{-(1-\beta)G}G^C
 \tag{4}
$$

with a fixed $C$. In particular the uncorrected law (3) with $\mathfrak E_\pm$ absorbed holds whenever there is no zero with $1-\beta<(\log G)^2/G$ under the cap. This last sufficient scale set has upper logarithmic density at least $1/2$ in $G$, in addition to containing arbitrarily long windows of relative length tending to one. Neither assertion gives a lower-density estimate on the scales.

## 1. Remove only multiples of the exceptional conductor in the auxiliary calculation

The [classical Page uniqueness region](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF) (Montgomery–Vaughan, Corollary 11.10) contains every such zero under $Q_0$, since $\log Q_0=o(\sqrt G)$. If present, its conductor satisfies $r>G^K$ for every fixed $K$ eventually, uniformly over the possible exceptional zeros. Indeed from the same chapter's Corollary 11.15 (Siegel's theorem), $1-\beta\gg_\delta r^{-\delta}$ for any fixed $\delta>0$. The zero is inside the classical exceptional region for its own conductor because $\log r\le\log Q_0=o(\sqrt G)$. If $r\le G^K$, choose $\delta<1/(2K)$ to contradict $1-\beta<4a_0/\sqrt G$ for large $G$. This step is ineffective, but not conditional.

Partition the common auxiliary arcs into those with $r\mid q$ and all others, with the first set empty if the zero does not exist. On the latter arcs the [uniform prime and masked Möbius estimates of R85, (3)–(4)](r85-spectral-unconditional-planted-ap-good-dyads.md#1-good-dyads-are-unconditional) apply unconditionally. Indeed all induced characters mod $q$ have conductor dividing $q$, so none has the excluded real zero. The same is true on any divisor modulus arising when reducing an actual nonunit residue or imposing one of the coprimality masks. Every further real zero is outside the narrow strip used there, and the classical region excludes the nonreal zeros. The error budget $Y G^{O(1)}Q_0^5e^{-c\sqrt G}$ and the positive-variable power savings from the [universal-cap argument](r86-spectral-universal-good-scale-windows.md#2-common-analytic-inputs-and-disjoint-error-budgets) are unchanged, as are the real hard amplitudes. Extend the slow integral for these arcs by the same BV bound. Restrict to the two moment conditions (7) of that argument, so the rational large-$q$ tail also has arbitrary fixed log saving.

To complete the rational series it remains to justify adding the formal terms with $r\mid q$. These are absent when $r$ is not squarefree, since $\mu(q)$ from the left principal character restricts the formal sum to squarefree $q$. Otherwise write $q=rt$ with $(r,t)=1$. The formal sup/variation bound $O(G^{C_1}C_2^{\omega(q)}/q)$ used in the same argument holds for these denominators too: it is an occupancy bound on the formal coefficients, independent of any actual progression estimate at $q$. Their total absolute cost, normalized by $Y$, is at most

$$
 G^{C_1}\sum_{\substack{r\mid q\\q\ {\rm sf}}}
    \frac{C_2^{\omega(q)}|c_q(N)|}{q\varphi(q)}
 \ \ll\ G^{C_3}\,\frac{C_2^{\omega(r)}}{r}
 \ \ll\ G^{C_3}r^{-1/2}.
 \tag{5}
$$

Here Ramanujan sums are multiplicative for coprime moduli, $|c_r(N)|\le\varphi(r)$, and the remaining $t$ Euler product has $O(p^{-1})$ increments on primes dividing $N$ and $O(p^{-2})$ elsewhere. Prime harmonic summation bounds that product by $G^{O(1)}$ uniformly. In the last bound use $C_2^{\omega(r)}\ll r^{1/2}$ by absorbing finitely many small primes into a constant. By the conductor bound (5) is negligible to arbitrary inverse-logarithmic precision. Thus the actual auxiliary integral on the **nonmultiple** denominators is already the full formal parity bracket, up to arbitrary fixed log error. On the moment-good targets it has the profile (1) plus the little-oh in (3), by the [uniform cutoff transfer](r86-spectral-universal-good-scale-windows.md#3-uniform-cutoff-profile-and-exact-arc-conclusions).

## 2. Treat only the left arithmetic on the excluded arcs

For each $q$ divisible by $r$, the left progression formula has its ordinary principal density on the units and the one additional pole term $-\chi_q(b)X^\beta/(\varphi(q)\beta)$ in the prefix ending at $X$ in unit residue $b\bmod q$. Its error is $O(Xe^{-c\sqrt G})$ uniformly at the polynomial scales used here. To check this, repeat the finite-height Perron proof of R85 for the negative logarithmic derivative. In the exceptional character only, shift to $\sigma=1-5a_0/\sqrt G$, with height $e^{\sqrt G}$ as before. The farther line is still inside the half-width zero-free bounds of [Montgomery–Vaughan, Theorems 11.3–11.4](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF) when $a_0$ is small. The classical region and Page exclude any competing zero in this strip. The unique real zero is simple, and its distance from the new vertical line is at least $a_0/\sqrt G$; the horizontal sides are at height $e^{\sqrt G}$. Thus the estimates away from or near the real zero of Theorem 11.4 give the same polynomial bounds in $G$ on the new contours, and the only additional crossed pole of $-L'/L$ is at $\beta$, with residue $-1$. The same half-integer Perron truncation and bounds on the three new sides give the asserted error. The other characters use the original narrower contour, and the principal one uses the usual residue at $1$. Orthogonality and the negligible prime-power error give the left progression counts for the log-weighted primes.

By BV partial summation with the true hard test on $I$, write $V(\eta)=\int_I\omega(u)e(\eta u)du$. Since $q\ll Y$, the prime weights on $I$ have no nonunit residues. On the actual auxiliary arc at $a/q$ with $r\mid q$, the left Fourier polynomial has the approximation

$$
        \frac{\mu(q)}{\varphi(q)}V(\eta)
           -\frac{\chi_q(a)\tau_q(\chi_q)}{\varphi(q)}V_\beta(\eta)
           +O(YG^{O(1)}Q_0^2e^{-c\sqrt G}).
 \tag{6}
$$

The derivative of $X^\beta/\beta$ gives $u^{\beta-1}$ with no remaining factor of $\beta$. The Gauss multiplier uses the real character, and the ordinary constant uses the Ramanujan sum of a reduced numerator. Multiplying the error by the true right polynomial of trivial size $YG^{O(1)}$, and integrating over total measure $O(Q_0^3/Y)$, gives arbitrary fixed log saving. No approximation for the right polynomial on these denominators is invoked.

The first term of (6) on the $r\mid q$ arcs is negligible against the **actual** right polynomial. Indeed the arcs are disjoint because $Q_0=Y^{o(1)}$, and Plancherel on the line gives $\|V\|_2^2\ll Y$ for these bounded left tests. Its squared norm on the arcs is at most

$$
  O(Y)\sum_{\substack{q\le Q_0\\r\mid q}}
                 \frac{\mu(q)^2}{\varphi(q)}
       \ \ll\ Y\frac{\log(2Q_0)}{\varphi(r)} .
 \tag{7}
$$

If $r$ is not squarefree the left side is zero; otherwise use $q=rt$ squarefree and $(r,t)=1$. The standard reciprocal sum $\sum_{t\le X}1/\varphi(t)\ll\log(2X)$ follows by expanding $t/\varphi(t)=\sum_{h\mid t}\mu^2(h)/\varphi(h)$ and summing harmonically. The actual right $\|\widehat M_\pm\|_{2}\ll\sqrt Y\,G^{15/2}$ follows from the $\tau_4(m)^2=\tau_{16}(m)$ squarefree tuple bound. Cauchy–Schwarz in (7) and $r>G^K$ for each fixed $K$ prove the saving, since $r/\varphi(r)\ll\log(2r)\ll G$. The second term of (6) integrated against the actual right is exactly (2). This proves that no other unknown contribution from these arcs is left in (3).

For (4), the [Gauss induction identity](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primitive-characters-and-gauss-sums/267951F517AD4E1411297F5AC998CD4F) (Montgomery–Vaughan, Theorems 9.7 and 9.10) gives $\tau_q(\chi_q)=\mu(t)\chi^*(t)\tau_r(\chi^*)$ for $q=rt$, with $|\tau_r(\chi^*)|=\sqrt r$. Hence only squarefree $t$ coprime with $r$ contribute, and the squared norm of the exceptional left term is at most

$$
 \|V_\beta\|_2^2\,
       r\sum_{\substack{q=rt\le Q_0\\(t,r)=1}}
                           \frac1{\varphi(q)}
       \ \ll\ Y^{2\beta-1}G^C .
 \tag{8}
$$

The line norm bound uses $u\asymp Y$ on the exact $I$. Combine this with the same true right $\|\widehat M_\pm\|_2$ and Cauchy–Schwarz. This proves (4), with no assertion of saving when $1-\beta$ is too small.

## 3. An exact discrete form of the residual

For use in studying (2), set

$$
 W_{\beta,Q_0}(x)=\int_{-\Delta_0}^{\Delta_0}V_\beta(\eta)e(-\eta x)\,d\eta,
 \qquad
 \mathcal C_{r,Q_0}(n)=
     \sum_{\substack{t\le Q_0/r\\(t,r)=1}}
                              \frac{\mu(t)c_t(n)}{\varphi(t)}.
$$

The first is the finite-frequency projection of the exact left test, not that test itself. The sums $c_t(n)=\sum_{a\bmod t,(a,t)=1}e(na/t)$ are Ramanujan sums for integer $n$. Expanding the true right Fourier sum in (2) gives the exact identity

$$
 \mathfrak E_\pm=-\frac r{\varphi(r)}
       \sum_{m\in V\cap\mathbb Z}M_\pm(m)\,
          \chi^*(N-m)\,\mathcal C_{r,Q_0}(N-m)\,
                                      W_{\beta,Q_0}(N-m).
 \tag{9}
$$

To check it, put $n=N-m$ and $q=rt$ with $(r,t)=1$ after Gauss induction. CRT gives
$\sum_{a\bmod q,(a,q)=1}\chi_q(a)e(-na/q)
=\chi^*(-n)\chi^*(t)\tau_r(\chi^*)c_t(n)$,
valid also when $(n,r)>1$ by the vanishing of a primitive Gauss sum at nonunit frequency. Multiply by
$\tau_q(\chi_q)=\mu(t)\chi^*(t)\tau_r(\chi^*)$. Then $\chi^*(t)^2=1$ and $\tau_r(\chi^*)^2=\chi^*(-1)r$ because the character is real. Together with $\varphi(rt)=\varphi(r)\varphi(t)$ and the common slow-frequency interval this gives (9), including the minus sign. All sums are finite. This isolates the actual remaining correlation; it does not replace the color, Ramanujan weight, or smoothing by any probability model.

## 4. Complete the two actual arc decompositions and enlarge the sufficient scales

The [fixed auxiliary complement and actual original minor bounds](r86-spectral-universal-good-scale-windows.md#2-common-analytic-inputs-and-disjoint-error-budgets) did not require good scales. They hold at every large $G$ for the exact coefficients, with ambient exceptional sets whose sum has the size stated in (3) after intersecting the prescribed planted family and adding the two moment failures. In particular the common auxiliary complement is $O(Ye^{-Z})$ off its smaller exceptional set; the original moving minor has the stated unconditional power bound. Add the true common complement to the auxiliary contributions just evaluated to obtain the full formula by Fourier inversion. Then subtract the **actual original moving minor** to obtain (3) on its major. The auxiliary and original arc sets are not identified. Because $\log K_z=O(Z)=o(G)$, the stated exceptions have relative density zero for each prescribed $z$.

If $1-\beta\ge(\log G)^2/G$, (4) makes the correction $O_A(YG^{-A})$ for every fixed $A$. For the stated geometry, let $\mathcal G_{\rm thin}$ contain the large $G$ with no zero violating this threshold under the cap (a violating zero necessarily lies in the wider definition for large $G$). If its complement is bounded, the scale claims follow immediately. Otherwise take arbitrarily large violating $G_0$ and its zero with gap $b=1-\beta<(\log G_0)^2/G_0$, so $b\to0$. Put $w=\log(1/b)$, $H=4 b^{-1}w^2$, and $R=c b^{-2}w^2$ with a sufficiently small fixed $c>0$. The function $(\log G)^2/G$ is decreasing for $G>e^2$, and its value at $H$ is $b(1+o(1))/4<b$. Hence $H>G_0$ and the old zero no longer violates the threshold anywhere on $[H,R]$. Its conductor remains below the increasing cap, and the zero still occupies the Page interval throughout this window, since
$b\log(4Q_0(R))=8\sqrt c+o(1)<c_P$. Any new violating zero would also lie in that same interval, as
$(\log G)^2\log(4Q_0(G))/G=o(1)$, which would contradict uniqueness. Thus $[H,R]\subset\mathcal G_{\rm thin}$. We have $H/R\to0$ and $\log H/\log R\to1/2$; evaluating densities at the endpoints $R$ gives upper density one in $G$ and upper logarithmic density at least $1/2$. These are unconditional sufficient-scale conclusions. The ultra-close residual (9) on the other scales is not estimated beyond (4).
