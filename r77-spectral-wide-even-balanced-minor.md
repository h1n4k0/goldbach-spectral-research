# Signed integrated cutoff energy widens the even near-balanced minor bound

**Scope.** This strengthens the even-total-parity case of the [actual balanced minor theorem](r76-spectral-balanced-actual-minor.md). It applies to true squarefree partners with their actual largest two primes, on either the kept or rejected exponent-band selector. The full absolute prime mass is bounded unconditionally. The actual minor at the original fixed $Q$ uses only the historical prime-progression Dirichlet GRH input used there. Neither polynomially separated partners nor weak S are estimated.

Keep all variables, cutoff constants, the fixed even radical of $N$, the hard left interval $I$ and the bounded-variation left test $\omega$ of that theorem. In particular $L=\log N$, $L_2=1+\log L$, $0<\sigma_1<\sigma_2<1/10$, $D=\sqrt N L^{-B}$, and the true above-BV mixed coefficient is $M_>(m)$. Write $x=pqa\in V=[N/3,2N]$ with $p<q$ its largest two primes, $s=\log(ap/D)$, $t=\log(aq/D)$, and $\mu(m)=\mu(a)=+1$. The actual right coefficient $A(m)$ equals $M_>(m)$ on either the kept selector $\sigma_1L<s\le\sigma_2L$ or the rejected selector $\sigma_1L<t\le\sigma_2L$, separately, always imposing $0<t-s=\log(q/p)\le E$ and any further integer selector on $a$. Else it is zero. Uniformly for $1\le E\le \sigma_1L/2$, put

$$
 \mathcal B(E)=\frac{(E+1)L_2^5}{L}+L_2^{-7/2}+L^{-1/6}L_2 .
$$

Then

$$
 \begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
 &\ll \frac{\Sigma(N)|I|}{L}\mathcal B(E)+N^{1-10^{-4}},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)
                       e(-N\theta)\,d\theta\right|
 &\ll \frac{\Sigma(N)|I|}{L}\mathcal B(E)+N^{1-10^{-4}} .
 \end{split} \tag{1}
$$

The first line is unconditional. In the second line $\mathfrak m$ is the literal complement of the original arcs $q_{\rm arc}\le Q=N^{1/1000}$ and $|\nu|\le 2Q/N$, with the same historical prime-character hypotheses as before. Thus either quantity is $o(\Sigma(N))$ in the $L/N$ normalization when $E=o(L/L_2^5)$. The odd-total case already has this width without the last two terms, by the actual balanced minor theorem.

## 1. The true inner and wholly rough parts

Set $\Delta_0=L^{1/3}$, $U=L_2^8$, $G=e^U$, and $V_G=\prod_{\ell\le G}(1-1/\ell)$ over primes $\ell$. If $E\le\Delta_0$ the even bound of the actual balanced minor theorem gives (1) already. Otherwise use its same bound on the actual part with $t-s\le\Delta_0$, including its conditional minor estimate. Its relative cost is $O(L^{-1/6}L_2)$, since $(1+\Delta_0)L_2^5/L$ is smaller for large $L$.

Let $b$ be the product of all the actual primes of $a$ at most $G$. If $b=1$, the whole squarefree partner $m$ is $G$-rough, since both tags are larger than $G$. On either eligibility selector its actual largest prime $q$ exceeds $N^{.4}$ for large $N$: in the kept case use $s\le\sigma_2L<.1L$ and $q=(x/D)e^{-s}$, and in the rejected case use $p=(x/D)e^{-t}$ and $q>p$. Apply the [true rough-kernel theorem](r69-spectral-rough-reciprocal-kernel-sampling.md) with $U_0=U$ and $\delta=1/10$. Its positive reciprocal cofactor majorants on the actual largest-prime split give relative bound $O(\sqrt{L_2/U})=O(L_2^{-7/2})$. To impose the extra gates for the genuine major, write $k'=ap$ for its fixed cofactor in that split. On this two-giant support $p=P^+(k')$, so $s=\log(k'/D)$ is fixed, while $t=\log(x/(pD))$ and $t-s=\log(x/(pk'))$ yield only hard interval cuts in $x$. Any restriction on $a=k'/p$ is constant at fixed $k'$. To specify the support from this largest-prime split, take $p=P^+(k')$ with $p>a$; the two-giant size bounds of the balanced theorem make this equivalent on the indicated band and near-gap gates. Such restrictions preserve the original bounded variation and can only reduce the positive reciprocal bound. Thus the same two-prime count and major completion of the rough theorem apply to the actual restricted polynomial, and yield the stated bound on its minor by subtraction. This is not a claim that a subset of a signed minor bound inherits the bound. The power errors of the rough theorem fit those in (1).

## 2. Integrated energy with a nonempty exact small factor

Retain $b>1$ and $t-s>\Delta_0$. Use the physical logarithmic cells of width $\eta=L^{-2}$ and the reference $x_0$ within each cell, exactly as in the actual balanced minor proof. Write $s_0=\log(x_0/(qD))$, $h_0=\log(x_0/D^2)$. In particular $s-h=s_0-h_0$ exactly throughout the cell. Impose also the widened positive-envelope condition $t-s_0>\Delta_0-\eta$. For fixed $x_0,s_0$ the widened $a$ support is a hard interval of log width $w\le E+2\eta$, or a subinterval, with

$$
             a\ge \exp(2s_0+\Delta_0-h_0-\eta).
 \tag{2}
$$

Here $s_0$ and $t$ are between positive fixed multiples of $L$ and $(\sigma_2+\sigma_1/2)L+O(\eta)$. There is no need to move the cutoff for an arithmetic average at fixed $s_0$.

Remove large $j(a)=\omega(b)$ using the uniform positive envelope bound of the balanced theorem. For any desired fixed inverse-log saving choose $J_*=\lceil C_*\log L\rceil$ with sufficiently large fixed $C_*$. Indeed

$$
 \sum_{\substack{a\le N,\ a\ {\rm sf}\\j(a)>J_*}}\frac{\tau_8(a)}a
  \ll 2^{-J_*}\!\prod_{\ell\le N}\left(1+\frac{8\cdot 2^{\mathbf1_{\ell\le G}}}{\ell}\right)
  \ll 2^{-J_*}L^8U^8 .
 \tag{3}
$$

The crude fixed-cell envelope is at most $L^{C'}\tau_8(a)$ uniformly in the real coordinate, so these extreme counts are negligible in the reciprocal envelope bound after choosing $C_*$. This removes actual terms by positivity; it does not require any analytic cancellation in the high counts.

For the remaining terms we prove the new arithmetic estimate, uniformly for $u_0=s_0$ or $u_0=s_0-h_0$ on the fixed cell support:

$$
   \sum_{\substack{a\text{ in }(2)\text{ and the widened interval}\\
             a\ {\rm sf},\ 1<b,\ j(a)\le J_*,\ \mu(a)=+1}}
                  \frac{|J_a(u_0)|^2}{a}
                  \ll (E+1)U.
 \tag{4}
$$

An additional selector on $a$ is immaterial. To prove (4), write $a=bv$ with strictly $G$-rough $v$. For each allowed $b$, form the nonnegative square and then drop the restrictions on the squarefreeness and parity of $v$ and the extra subset in this upper bound; keep the roughness and the hard interval on $v$. Only now expand the signed label pairs from

$$
 J_{bv}(u_0)
   =\sum_{d\mid b}\mu(d)\!
          \sum_{\substack{r\mid v\\ \log r\le u_0-\log d}}
                 \mu(r)(u_0-\log d-\log r).
 \tag{5}
$$

This identity is valid also for these rough integers $v$ after the squarefree mask is dropped, since $(b,v)=1$. Pair labels satisfy $r_1,r_2\le Z=e^{u_0}$, and the rough lcm $d'=[r_1,r_2]$ is fixed in each trace. The log widths of the clipped $v$ intervals add to $w$. On a dyad $v\asymp V_0$ of width $w_0$, its precise harmonic trace is

$$
 \sum_{\substack{v\ {\rm in\ that\ interval}\\P^-(v)>G,\ d'\mid v}}\frac1v
 =\frac{w_0 V_G}{d'}
   +O_A\!\left(\frac{w_0L^{-A}}{d'}
               +\frac{\exp(O_A(U L_2^2))}{V_0}\right).
 \tag{6}
$$

This is the rough Bonferroni trace used in the [ordered-major separated calculation](r75-spectral-separated-ordered-major.md), now without its squarefree or Möbius correction. In detail, inclusion-exclusion for the primes up to $G$, at consecutive parities of depth $\asymp_A L_2^2$, bounds the density error by an arbitrary inverse power of $L$, since the sum of prime reciprocals is $O(\log U)$. The weight on each retained progression of multiples of $d'$ times the coprime small-prime product costs $O(1/V_0)$ in floor error, also on literal hard endpoints. The number of retained products is at most $\exp(O_A(U L_2^2))$. The log weights from (5) are at most $O(L)$, and since $\log b=O(U\log L)=o(\Delta_0)$, (2) gives

$$
          \frac{Z^2\exp(O_A(U L_2^2))}{V_0}
                     \ll \exp(-\Delta_0/2).
 \tag{7}
$$

This bound uses the true separation, not the width alone. All extra factors from the $b$ shifts, the powers of the log weights, the summation over dyads and $\sum_b1/b\ll U$ cost only fixed powers of $L$. The errors with $1/d'$ sum against a fixed log power, since $\sum_{r_1,r_2\le Z}1/[r_1,r_2]\ll (1+\log(2Z))^3$. Taking $A$ after $C_*$ makes the aggregate error $O(L^{-2})$. We emphasize that (6) is used with signed coefficients in its main term; an upper-bound sieve for each label pair alone would not suffice.

## 3. Sampling the actual rough gcd in the integrated variable

Let $R_{G,e}(u)$ denote the reciprocal Möbius primitive over strictly $G$-rough integers with prime factors of rough $e$ omitted, zero for $u<0$. Write $R_G$ if $e=1$. For squarefree $b>1$ supported on primes at most $G$, put

$$
 \mathcal D_b f(u)=\sum_{d\mid b}\mu(d) f(u-\log d),
 \qquad J_{b,e}(u)=\int_{-\infty}^u(\mathcal D_bR_{G,e})(v)\,dv .
$$

Expand the gcd identity $1/[r_1,r_2]=\sum_{e\mid r_1,r_2}\varphi(e)/(r_1r_2)$ in the main term of (6) and use (5). The resulting main term in the upper estimate of (4) is exactly

$$
 w V_G\!
 \sum_{\substack{1<b,\ b\ {\rm sf},\ P^+(b)\le G\\j(b)\le J_*}}
    \frac1b
    \sum_{\substack{e\le Z\\ e\ {\rm rough}}}
       \frac{\varphi(e)\mu^2(e)}{e^2}
                |J_{b,e}(u_0-\log e)|^2 .
 \tag{8}
$$

If one started with a smaller subset of the support, use the whole positive interval of width $w$ before (6). This expression keeps the actual rough gcd weight and all the signs in the divisor shifts.

We next sample the rough harmonic $e$ trace at the fixed $u_0$, as opposed to averaging $u_0$ over a moving arithmetic cell. The key is that $J_{b,e}$ decays at both ends for $b>1$. Extract any prime $\ell\mid b$; its signed shift turns the indefinite integral of $R_{G,e}$ into the finite integral $\int_{u-\log\ell}^u R_{G,e}(v)\,dv$, followed by the other signed shifts. The ordinary reciprocal Mertens estimate convolved with the positive smooth mask shows, uniformly for rough $e\le Z$, that for $u\ge0$,

$$
 |R_{G,e}(u)|\ll U\big(e^{-c\sqrt u}+e^{-u/(2U)}\big),\qquad
 \|R_{G,e}\|_1\ll U .
 \tag{9}
$$

The pointwise estimate follows by splitting the mask at log shift $u/2$, with exponential moment $O(U)$ at $1/U$. The same bound for that moment is used in the ordered-major proof: for primes below $G=e^U$, the corresponding Euler product is $O(U)$ (its ratio to the unshifted product is bounded, by $\sum_{\ell\le G} (\log\ell)/(U\ell)\ll1$); the extra rough primes of $e$ contribute only $O((L/U)e^{-U+1})$ to its log. The $L^1$ bound also follows directly by ordinary $L^1$ Mertens and the unshifted positive kernel mass $O(U)$.

Omit $e<\exp(u_0-\Delta_0/4)$ in (8). Every active log argument of the above short integral is then at least $\Delta_0/4-\log b\ge\Delta_0/8$, and (9) saves more than any inverse log. The outer harmonic mass is only $O(L)$ even without roughness; the shift count and other factors are polynomial in $L$. On the remaining interval replace $R_{G,e}$ by $R_G$ and $\varphi(e)/e$ by 1. Indeed the difference of the extra positive mask from its atom of mass one at zero has mass $O((L/U)e^{-U})$. By (9) and the positive convolution the difference of primitives in both sup and $L^1$ norm is $O(L e^{-U})$. Summing the signed shifts gives the same times $\tau(b)$ for sup differences of integrated primitives. Since $U=L_2^8$ this costs less than every inverse log even after all sums.

Write $J_b=J_{b,1}$. On the surviving interval the bounded-variation test in $\log e$ is now $|J_b(u_0-\log e)|^2$. Its sup and total variation are polynomial in $L$ uniformly for $j(b)\le J_*$: the integrated primitive has sup bounded by $\|\mathcal D_bR_G\|_1\ll U\tau(b)$ and its derivative has that same $L^1$ bound. Thus it suffices to approximate the harmonic measure of rough squarefree $e$ on arbitrary hard subintervals of $[\exp(u_0-\Delta_0/4),\exp(u_0)]$. It equals $V_G\,d\log e$ with errors smaller than any fixed inverse power of $L$ on prefixes. For verification, (6) at $d'=1$ gives the pure rough harmonic trace. Excluding rough prime squares costs on each ordinary dyad $e\asymp Y$ at most

$$
          O\!\left((1+\log 2)\sum_{\ell>G}\ell^{-2}+Y^{-1/2}\right)
$$

by the reciprocal progression main and the floor summed up to $\sqrt{2Y}$. There are only $O(L)$ dyads, the lower endpoint is $\exp(cL)$ for a fixed $c>0$ on our fixed exponent band, and $G=e^{L_2^8}$. All its errors have the required saving, also when the original interval is shortened arbitrarily. Stieltjes partial summation against the finite-variation test now makes the sum in (8) equal to its real log integral, with $O(L^{-2})$ aggregate error after choosing the available fixed exponent sufficiently large. The log integral may be extended to the full real line by (9) and $\log b=o(\Delta_0)$, since $J_b=0$ below zero and decays beyond $\Delta_0/4$ by its finite-interval representation. Thus the expression in (8) is bounded by

$$
             wV_G^2\sum_{\substack{b>1,\ b\ {\rm sf}\\P^+(b)\le G}}
                            \frac{\|J_b\|_2^2}{b}+O(L^{-2}).
 \tag{10}
$$

Only the last extension in $b$ has used positivity of the Fourier energies. The $b=1$ term has not been restored; its true arithmetic class was treated separately.

Under the Fourier convention $\widehat f(\xi)=\int f(u)e^{-i\xi u}du$, $\widehat J_b(\xi)=q_b(\xi)\widehat R_G(\xi)/(i\xi)$, where $q_b(\xi)=\prod_{\ell\mid b}(1-e^{-i\xi\log\ell})$. This follows from the finite-interval representation, including the value at zero by continuity. The [signed cutoff Euler proof](r70-spectral-signed-shift-euler-slots.md), §1, gives the following uniform estimates for any growing $U=\log G$: for $|\xi|\le1$, $|\widehat R_G(\xi)|\ll U/(1+U|\xi|)$, and

$$
 \sum_{b>1}\frac{|q_b(\xi)|^2}{b}
 \ll
 \begin{cases}
   (U|\xi|)^2,&|\xi|\le 1/U,\\
   (1+U|\xi|)^2,&1/U<|\xi|\le1,\\
   U^2(1+\log(3+|\xi|))^{C},&|\xi|>1 .
 \end{cases}
$$

The sum is over the same squarefree $b$ supported on primes up to $G$. Indeed it is the actual Euler product with its unit term subtracted, with $z=1$ in that proof. For high frequency $|\widehat R_G(\xi)|\ll (1+\log(3+|\xi|))^4/|\xi|$ by its same ordinary PNT comparison. The proofs of these frequency estimates use $U$ only as the upper prime log parameter and so apply to $U=L_2^8$. Plancherel with the additional $\xi^{-2}$ bounds the sum of the integrated squares by $O(U^3)$: on $|\xi|\le1/U$ its integrand is $O(U^4)$; between $1/U$ and 1 it is $O(U^2/\xi^2)$; the remaining integrable tail costs $O(U^2)$. Since $V_G\asymp U^{-1}$, (10) is $O(w U+L^{-2})$, proving (4).

## 4. Real prime upper bound and unchanged minor comparison

Use the same physical-cell envelopes and true prime counts as the actual balanced minor proof. In its notation, $C_0^2$ still has reciprocal sum $O(E+1)$ by the moving signed and unsigned shell floors. On the retained even part, (4) now bounds the reciprocal sum of $C_1^2$ by $O((E+1)U)$, instead of $O((E+1)L)$. The $\eta C_0$ endpoint term in $C_1$ is already covered by the former estimate. The low divisor folds have exactly the same positive contribution $O((E+1)L_2^4/L)$ before the local sieve factor; no small-factor mask was removed from a signed low sum. Cauchy for the sharp $C_0C_1/L$ gives reciprocal contribution $O((E+1)\sqrt U/L)$, plus the unchanged centered-square term. Together with the rare counts (3), the relative bound after the $O(L_2)$ local loss is

$$
   O\!\left(\frac{(E+1)L_2^5}{L}+
             \frac{(E+1)L_2\sqrt U}{L}\right)
    =O\!\left(\frac{(E+1)L_2^5}{L}\right).
$$

Here the choice $U=L_2^8$ balances the last log power with the already required low-fold bound. A smaller polylogarithmic $U$ with $U/L_2\to\infty$ would give the same width but a weaker error on the completely rough family.

At fixed actual $k=aq$ on the two-root sieve the added restrictions are constant in $a$ or ordinary intervals in $x$, including the true lower gap $t-s>\Delta_0$. Thus the original bounded-variation envelope in the second prime $q$ and the genuine upper sieve in $p,N-kp$ are unchanged, as are their floors. The new estimate is exactly the needed fixed-$s_0$ reciprocal bound under the ordinary (unconditional) second-prime PNT of that proof. It consequently proves the retained contribution to the first line of (1). For the major the same support restrictions are bounded-variation gates and the same fixed-$Q$ two-prime completion applies. Its real density has the same two logarithmic prime factors, and our bound on the positive reciprocal envelope applies with $x_0=x$. Hence the resulting major has the same bound; subtract it from the genuine full correlation to obtain the claimed estimate on the actual minor. Add the already handled inner and wholly rough branches (disjointly if necessary); all estimates are for genuine restricted polynomials and have the errors displayed in (1).
