# Unconditional hard rational transport at logarithmic width outside a small exceptional set

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $R=\operatorname{rad}N$, and $e(z)=e^{2\pi iz}$. Keep the genuine coefficient and shell of [the hard rational profile theorem](weak-s-type-ii-critical-prime-cutoff-free-rational-profile-grh.md):

$$
 D_m=\mathbf1_{N-y\le m<N/2}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                       (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_m D_m e(\alpha m).
$$

Here $N/2\le y\le9N/16$, $I_k$ is a hard interval including the strict restriction $k>t\ge N^{.49999}$, and the original arithmetic restrictions and endpoints are retained. As before we can clip $I_d$ at $d<N/(2t)$ and $I_k$ at $k<X/2$. In this note assume that $I_d\subset[X,CXL^\gamma]$ for fixed $C>1$ and $\gamma\ge0$. There is **no** radical bound. Write $\mathcal Q=[.8X,.9X]\cap\mathbb P$ and let $\mathcal E_N^0(D)$ be the squared critical-shell norm, integrated for $|\beta|\le1/(10N)$, after subtracting the mean on $a=1,\ldots,q-1$ separately for each $(q,\beta)$ at $a/q+\beta$. Let $\mathscr H_N$ be the cutoff-free hard rational squared norm [defined in (1)–(2) of the profile theorem](weak-s-type-ii-critical-prime-cutoff-free-rational-profile-grh.md), with all its true individual long-unit masks, all rational square labels and every $h\mid R$.

**Theorem.** Fix $A,B>0$. For sufficiently large $Y$, outside a set of at most $O_{A,B,C,\gamma}(Y(\log Y)^{-B})$ even $N\in[Y,2Y]$, one has unconditionally

$$
                    \mathcal E_N^0(D)
                   =\mathscr H_N+O_{A,B,C,\gamma}(N L^{-A}) ,
                                                                    \tag{1}
$$

uniformly in all the permitted hard cuts. The exceptional set depends only on the targets and the fixed parameters, not on any of those cuts. Taking $A=2$ gives in particular that the centered energy, and also the ordinary uncentered energy by [the true constant profile bound](weak-s-type-ii-critical-prime-polynomial-width-true-constant-profile.md), are $O_{B,C,\gamma}(N/L)$ outside such an exceptional set. No effectiveness claim is made for the Davenport comparison constants. This is an unconditional typical-target restriction of the hard rational transport at fixed logarithmic width, not an all-target result, polynomial widening, signed lower bound, or Weak S.

## 1. Average the actual short inclusion tail without capping the retained radical

Put $\mathcal L=\log Y$ and take a common cutoff $H=\mathcal L^Q$, for a fixed $Q$ to be chosen later. Use the nonnegative arithmetic statistic

$$
                      \mathcal T_N(H)
          =\sum_{\substack{r\mid\operatorname{rad}N\\r>H}}
                                    \frac{3^{\omega(r)}}r .
$$

No prime factor of $N$ is deleted from a mask. We use only that multiples of $r$ up to $2Y$ number at most $2Y/r$, with no need to estimate independence of divisibility events. Consequently

$$
 \begin{split}
  \frac1Y\sum_{\substack{Y\le N\le2Y\\N\ {\rm even}}}\mathcal T_N(H)
      &\ll \sum_{r>H}\frac{\mu^2(r)3^{\omega(r)}}{r^2}\\
      &\le H^{-1/2}\prod_p(1+3p^{-3/2})\ll H^{-1/2}.
 \end{split}                                                        \tag{2}
$$

For any fixed $M>0$, the set failing $\mathcal T_N(H)\le\mathcal L^{-M}$ therefore has size $O(Y\mathcal L^{M-Q/2})$. Take $M$ sufficiently large for the approximation costs below, then $Q>2(M+B+1)$. On the remaining targets we may use $\mathcal T_N(H)\ll_M L^{-M}$, since $L=\log N$ and $\mathcal L$ are comparable uniformly in the dyad. The parameters controlling the square and physical cutoffs below are chosen before $M,Q$.

Here are both places in which this tail is used. First take the exact inward physical and logarithmic cofactor smoothing at $\delta=L^{-K}$ and the auxiliary square cutoff $T=L^J$, with sufficiently large fixed $K,J$. All true physical and cofactor edge bounds and the true square cutoff bound from [the hard profile transport, §1](weak-s-type-ii-critical-prime-cutoff-free-rational-profile-grh.md#1-arbitrary-fixed-logarithmic-accuracy-in-the-genuine-finite-transport) are unconditional. They give squared ordinary cost $O(N\delta)$ for the two genuine edge transfers, and $O(NLT^{-3/4})$ for the square omission per divisor dyad; the localization before the common physical weight is exactly as there. Use that approximant, preserving its true long mask, but cut only the short inclusion to $h\mid R,\ h\le H$. In particular the square sieve is first truncated while the true full unit is still present, with $l$ squarefree, $l\le T$, $(l,N)=1$.

To check the new short omission quantitatively, let $F_{i,m}$ be the genuine localized unmasked-short polynomial prior to both arithmetic inclusions on divisor dyad $i$, retaining $(d,N)=1$ in its signed long sum. The forced-divisibility estimate [in the single-dyad approximation, §1, (4)](weak-s-type-ii-critical-prime-polynomial-single-dyad-grh.md#1-literal-endpoint-and-arithmetic-transfers-on-the-polynomial-dyad) gives $\sum_{r\mid m}|F_{i,m}|^2\ll NL/r$ for squarefree $r\mid R$, on the original fixed compact product support, also before the common physical weight. Indeed the logarithmic factor there is $O(L)$ on the true dyad range and masks. The short difference at each $m$ has magnitude at most $T|F_{i,m}|\sum_{h\mid(m,R),\,h>H}1$. Squaring, setting $r=[h_1,h_2]$, and counting at most $3^{\omega(r)}$ ordered pairs gives squared error $O(N T^2 L\mathcal T_N(H))$ per dyad. Multiplication by the common physical cutoff is a contraction. Even allowing $O(L)$ dyads and the resulting $O(L^2)$ factor in squared norm, all genuine approximation errors can be made $O(NL^{-E})$ for any fixed desired $E$: take $K>E+2$, then $J$ so $(3/4)J>E+3$, and $M>2J+E+4$ before choosing $Q$. The approximant $D^\dagger$ thus keeps the exact split $s=(l,d)\mid l$, $d=su$, $(u,lN)=1$, $k=(l^2h/s)v$ with the same signs $\mu(l)\mu(s)\mu(h)\mu(u)$ as before. Its pre-physical ordinary squared norm per dyad is $O(N)$ by the single-dyad argument and the small errors just bounded.

Second, the analytic rational tail for restoring $h>H$ at fixed $(l,s)$, after physical inversion, is bounded in squared norm before integrating $\beta$ by

$$
        \frac{O(N^2)}{L l^2 V(lN)}
                 \sum_{\substack{h_1,h_2\mid R\\h_1,h_2>H}}
                                \frac1{[h_1,h_2]}
        \le \frac{O(N^2)}{L l^2 V(lN)}\,\mathcal T_N(H),
        \qquad V(b)=\frac{\varphi(b)}b .
                                                                    \tag{3}
$$

This is the [exact rational sampling bound, §3](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#3-keep-the-stronger-sparse-sampling-bound-and-integrate-the-actual-derivative). Its hypotheses hold at any fixed $K,J$ above, as checked in the hard rational profile: $s\le L^J$ leaves polynomial long scale, the reciprocal $1/c$ bound is uniform at the true polynomial mask, and the real cofactor derivative is integrated separately at its actual edges, not bounded by a supremum of order $\delta^{-1}$. Summing its norm over $l,s$ costs at most $O(L^{2J+1})$ by the crude label count $O(T^2)$ and $1/V(lN)\ll 1+\log L$. Accordingly choose $M$ still larger after $J$ to obtain any required fixed log precision in this rational restoration too. The bound (3) is for rational labels only; no $h>H$ enters the finite modular expansion.

## 2. Unconditional cancellation in the true long mask

For any fixed $C_1$ and polynomial-sized mask $B_0\le N^{C_1}$, and a hard interval of scale $U$ inside $[U,2U]$ with $U$ between two fixed positive powers of $N$, the genuine Möbius transform restricted by $(u,B_0)=1$ has the unconditional additive bound $O_D(UL^{-D})$ for every fixed $D>0$, uniformly in the additive frequency. To show this, use the exact identity

$$
       \mu(u)\mathbf1_{(u,B_0)=1}
           =\sum_{\substack{r\mid u\\p\mid r\ \Rightarrow\ p\mid B_0}}
                    \mu(u/r).
                                                                    \tag{4}
$$

At allowed primes it leaves $\mu$ unchanged, and at a forbidden prime the convolution kills every positive exponent. For $r\le\sqrt U$, after writing $u=rz$, the hard endpoints obtained within $[U/r,2U/r]$ have logs comparable to $L$, and [Davenport's unconditional additive Möbius bound, as in He–Huang (1.2), p. 1](https://www.impan.pl/shop/en/publication/transaction/download/product/91740?download.pdf=#page=1) gives $O_D((U/r)L^{-D})$ by subtracting prefixes. Subtracting prefixes includes strict endpoints, or a loss of at most two singletons per interval before the prefix estimate. The total smooth reciprocal factor is $1/V(B_0)\ll_{C_1}1+\log L$; for example split its primes at $L^2$ and use Mertens for the smaller primes and $\omega(B_0)\ll_{C_1} L$ for the rest. For $r>\sqrt U$, positive counting of $u=rz$ and fixed Rankin exponent $1/4$ bound the absolute tail by

$$
   O\left(U^{7/8}\prod_{p\mid B_0}(1-p^{-3/4})^{-1}\right)
                                      =U^{7/8}N^{o(1)}
                                                                    \tag{5}
$$

uniformly. In the product logarithm the contribution of $p\le L^2$ is $O(L^{1/2})$ by summing over all integers, and that of the other $p$ is $o(1)$ by their count and sizes. This proves the bound at every fixed log exponent, increasing the initial Davenport exponent to absorb $1/V(B_0)$. The actual dyadic long twist $e(\tau\log(su/A_i))$ costs $O(1+|\tau|)$ by Abel's inequality, using the same bound uniformly on subintervals of the dyad. In particular the long array of the genuine approximation with mask $B_0=lN$ has transform $O_D(U_i L^{-D})$ at every fixed precision on any retained fixed-polylogarithmic $\tau$ range. This proof never replaces $N$ by a smaller radical.

## 3. Finite logarithmic dual completion and both exact center subtractions

Use the notation of [the logarithmic-width completion, §1](weak-s-type-ii-critical-prime-polylog-radical-width-inverse-log.md#1-the-same-arithmetic-and-smoothing-with-the-wider-logarithmic-cutoff). On each actual divisor dyad let $A_i=\lambda_iX,\ K_i=N/A_i,\ U_i=A_i/s$, and put $\xi_i=K_i s/(q l^2 h)$. Now $1\le\lambda_i\ll_C L^\gamma$, and, on $h\le H$,

$$
            L^{-P_0}\ll_{C,Q}\xi_i\ll1,\qquad
            U_i\xi_i=\frac{N}{q l^2h}\ll X,\qquad
            P_0=\gamma+2J+Q .
                                                                    \tag{6}
$$

The unblended $s$ labels are actual divisors of $l$. The $l,s,h,i$ count, including all values $h\le H$ whether or not they divide $R$, is a fixed power of $L$. All true masks and the normalized cofactor bump are unchanged.

Write $G_\beta(v)=\Omega_\delta(e^v)e(\beta Ne^v)$ for the common physical weight in the product variable, and $f_{i,\tau}(z)=w_i(z)e(\tau\log z)$ for the localized short weight and twist. Use $|\tau|\le L^P$ with fixed $P>K+2$ and a logarithmic nonzero dual cutoff $|j|\le J_*=\lfloor L^{P_j}\rfloor$ for fixed $P_j$ chosen sufficiently large after all preceding exponents. With $Y_\tau=1+\delta^{-1/2}+|\tau|$, the short envelope is $\ll\min(1,(Y_\tau/|\xi|)^2)$ at frequency $\xi$, its higher derivatives have fixed log costs on the retained time range, and $\|\widehat G_\beta\|_1\ll_K1+\log L$. The $|\tau|>L^P$ tail in the genuine separated-center norm is $O_D(NL^{-D})$ for any fixed $D$, since the pre-physical sample norm is $O(NL)$, and $|\widehat G_\beta(\tau)|\ll_r\delta^{1-r}|\tau|^{-r}$ at every fixed derivative order. Centering is a contraction for this initial tail.

For the omitted $j$ tail in the actual nonprincipal character expansion, use

$$
             \xi_i\sum_{|j|>J_*}|\widehat f_{i,\tau}(j\xi_i)|
        \ll_r \|f_{i,\tau}^{(r)}\|_1 (J_*\xi_i)^{1-r}.
                                                                    \tag{7}
$$

The true long array occupies each residue at most $O(1+U_i/q)=O_C(1+L^\gamma)$ times, with coefficients bounded by one. Multiplicative Parseval therefore bounds the sum of its character squares by $O(q(1+U_i/q)U_i)$. Weighting by the Gauss square $q$, summing $q\in\mathcal Q$, and taking a square root costs at most $O_C(N L^\gamma)$. This is the long residue factor in (7), not an absolute pointwise sum over all $u$. The remaining exterior label counts and retained time envelope cost only fixed log powers. Thus (7) gives any specified fixed log-accuracy actual norm truncation, by (6) and sufficiently large fixed $P_j$ and derivative order. All retained $l,h,j$ are genuine units modulo $q$ for sufficiently large $Y$.

Keep the new finite coherent vector $\mathcal S_q(v)$ on $v=l^2hu/j\bmod q$ with all the original signs, including the $\tau$ integral inside the vector. Its complete square is weighted by $q(q-1)$. The nonzero determinant condition is exactly

$$
                        l_1^2h_1 j' u_1-l_2^2h_2 j u_2=bq,
                        \qquad b\ne0 .
                                                                    \tag{8}
$$

All parameters in this equation other than the long variables $u_i$ and $q$ have fixed logarithmic ranges. In particular $|b|\ll_C L^{2J+Q+P_j+\gamma}$, by bounding the two products by $q$ times this quantity. For fixed labels and $b$, [the determinant Fourier argument, §2](weak-s-type-ii-critical-prime-polylog-radical-width-inverse-log.md#2-complete-coherently-and-remove-the-nonzero-modular-determinants) is the scalar product on the unit torus of the two long arrays at nonzero integer dilations and the $q$-sum at distinct frequencies $bq$. The two short factors with their mesh prefactors are bounded independently of the parameters, so the $q$-sum has $L^2$ norm $O(X^2\sqrt{\#\mathcal Q})$. Apply the unconditional supremum bound from §2 above to one long factor and the ordinary $O(\sqrt{U_{i'}})$ $L^2$ bound to the other. Even after both independent time integrals and all finite label sums, this gives $O_D(N^2 L^{-D})$ for any prescribed $D$: the long support lengths satisfy $U_i\ll_C X L^\gamma$, and the fixed polylogarithmic losses can be paid by increasing the Davenport exponent. Only the exact rational diagonal $b=0$ remains at the required accuracy.

For the actual centered norm, use the exact [two-square subtraction, §1](weak-s-type-ii-critical-prime-centered-rational-profile-grh.md#1-subtract-the-two-artificially-completed-squares) in this same finite vector. Specifically the nonprincipal character squares are the completely weighted squares minus

$$
                 \sum_q q(q-1)|\mathcal S_q(0)|^2,\qquad
                 \sum_q q\left|\sum_{v\ne0}\mathcal S_q(v)\right|^2.
                                                                    \tag{9}
$$

Since $v=0$ means exactly $q\mid u$, there are at most $O(1+L^\gamma)$ long elements per outer tuple there. The short absolute sum $\xi_i\sum_{j\ne0}|\widehat f_{i,\tau}(j\xi_i)|$ is $O(Y_\tau)$ by its two-piece envelope. Thus $\mathcal S_q(0)$ is bounded by a fixed power of $L$ and the first sum in (9) is $O(X^3L^{O(1)})$. For the second sum, first sum over **all** residues, where the short and long arrays separate. The long sum has the unconditional arbitrary-log bound from §2 above at zero frequency; the short bound is again $O(Y_\tau)$ and all outer counts are fixed logarithmic powers. Removing the single zero residue just bounded gives $O_D(X L^{-D})+O(L^{O(1)})$ for this sum at each $q$, hence arbitrary fixed log precision for its contribution at squared scale $N^2$. These estimates include $q\mid N$, where in fact the exact long unit excludes the zero residue. Neither sum in (9) is the actual additive group mean. The nonprincipal finite norm after these exact subtractions is nonnegative on each $q$ and has the additional true numerator normalization $q/(q-1)=1+O(X^{-1})$. This factor may be dropped once the finite squared norm is bounded: its error is at most $O(X^{-1})$ times that nonnegative total. We obtain that bound in the rational transfer next.

## 4. Restore only the exact rational coordinates and compare with hard samples

On $b=0$ the coordinate $\rho=j/(l^2 h u)\ne0$ is a rational equality, not a modular inverse. Both frequency cutoffs can now be restored at arbitrary fixed log accuracy in the squared rational norm. For precision about the small logarithmic $j$ cutoff, at fixed $(l,s,h,i,\tau)$ write $u=r z,\ u'=r'z,\ j=d_0r,\ j'=d_0r'$ with $(r,r')=1$ and integer $d_0\ne0$. On a dyad $r\asymp V_0$ also $r'\asymp V_0$ by the true long support. There are $O(V_0^2)$ pairs and $O(U_i/V_0)$ choices of $z$. The Fourier envelopes summed over $d_0$ have product sum $O(Y_\tau/(V_0\xi_i))$ by a split at the Fourier envelope scale. If both samples lie beyond magnitude $F$, the fourth-power tail gives instead $O(Y_\tau^4/(V_0\xi_i F^3))$ by summing $|d_0|^{-4}$; it is also valid when the implied lower bound for $|d_0|$ is below one. There are $O(L)$ such ratio dyads. Multiply by $\xi_i^2$ and use (6), then sum $q(q-1)$ to get the fixed-label squared rational bound $O(N^2 L Y_\tau)$, and its omitted-dual bound $O(N^2 L Y_\tau^4/F^3)$ when both arms of its own norm have $|j|,|j'|>J_*$. This is the [exact rational logarithmic tail, §3](weak-s-type-ii-critical-prime-polylog-radical-width-inverse-log.md#3-the-rational-restoration-and-the-genuine-full-energy), with (6) now giving $F=L^{P_j-P_0-1}$ for large $N$. Increase fixed $P_j$ to absorb the exterior log powers and $Y_\tau^4$ at retained $\tau$. The first envelope bound and the high derivatives of $G_\beta$ give the analogous arbitrary-log time restoration. Both errors may be combined by triangle across the fixed-polylogarithmic exterior labels. The full preliminary rational norm is $N$ times a fixed log power, so the corresponding changes in the squared norm are $O_D(N^2L^{-D})$ at chosen fixed precision.

Termwise Fourier inversion on this analytical rational vector now gives exactly the smoothed version of the hard rational model, at $l\le T,h\le H$. As in the hard profile, the normalized localized bump equals one on each term's physical support and the dyads exactly reassemble $su\in I_d$. The rational amplitude has its genuine sign and the factor $N/(q l^2 h u)$. Apply (3) to restore all $h\mid R$ **in this rational norm only**. By the unconditional paired-label estimate [in the hard rational profile, §1, (4)](weak-s-type-ii-critical-prime-cutoff-free-rational-profile-grh.md#1-arbitrary-fixed-logarithmic-accuracy-in-the-genuine-finite-transport), the resulting fixed-$\beta$ squared norm is $O_{K,J}(N^2/L)$. All comparisons with the squared modular norm and the positive group normalization from §3 therefore have negligible error to the prescribed accuracy. The $O(X^{-1})$ normalization error is power smaller at scale $N^2/L$. The two original truncation errors in actual sample norm similarly retain the desired squared-norm accuracy by choosing their norm errors with sufficient fixed margin, and then we integrate over $|\beta|\le1/(10N)$.

Finally use the unconditional [hard cutoff removal and square-label tail, §§2–3](weak-s-type-ii-critical-prime-cutoff-free-rational-profile-grh.md#3-transfer-to-the-literal-hard-limit). The squared norm of the difference between this finite-square-label smoothed rational vector and the cutoff-free hard model is at most $O((N^2/L)L^3(T^{-1/2}+\delta))$ before $\beta$ integration. Choosing $J,K$ sufficiently large at the outset makes the difference of their squared norms $O_A(NL^{-A})$ after integration by Cauchy and the unconditional sharp rational bound. For the actual transfer, ordinary Parseval on the disjoint original arcs and orthogonality of centering imply squared shell approximation error at most the $O(NL^{-E})$ genuine ordinary error from §1. The centered approximant has energy $O(N/L)$ by the preceding comparison, so the difference of true squared energies is $O(NL^{-E}+NL^{-(E+1)/2})$. Taking $E$ sufficiently large in terms of $A$ proves (1). The exceptional count was set solely by (2) after the ordinary and rational unit-tail accuracy choices, and was thus independent of all hard interval endpoints. This completes the unconditional proof on the stated typical targets.
