# Weak S: the microscopic crossing is negligible; a two-way first-alias criterion

Assume local GRH(N) to identify the arithmetic kernel with the original Li–Liu operator; extra global Dirichlet GRH is only used for the final circle-method comparison. Fix \(0<\rho\le1/20\), set \(J=(4/5,6/5)\) in physical ratios, and put

\[
 \begin{gathered}
 L=\log N,\qquad S=\mathfrak S(N),\qquad
 B_{N,a}=\mathbf 1_{0<x\le a}T_N\mathbf 1_J,\qquad 0<a\le\rho,\\
 E_N^\pm(t)=\frac1N\sum_{\substack{1\le m\le Nt\\ (m,N)=1}}\Lambda(m)\Lambda(N\pm m)-St,\quad
 E_N^*=\max_{\pm}\sup_{0\le t\le\rho}|E_N^\pm(t)| .
 \end{gathered}
\]

All projections are in physical log coordinates. The following estimates hold pointwise for every sufficiently large even \(N\):

\[
 \begin{aligned}
 \|B_{N,a}\|_{\mathrm{HS}}&\ll S\sqrt a+L N^{-3/8}, &\quad \|B_{N,a}\|_{\mathrm{HS}}&\ll L\sqrt{a+1/N}, \tag{1}\\
 \|B_{N,\rho}\|_{\mathrm{HS}}/S&\ll (E_N^*/S)^{1/2}+L N^{-3/8}, &\quad
 E_N^*/S&\ll_\rho (\|B_{N,\rho}\|/S)^{1/2}+N^{-3/4}. \tag{2}
 \end{aligned}
\]

In particular every \(a_N=o(1)\) crossing against the whole near-one strip is negligible at weak-S scale, even in HS norm. This includes the **entire** raw low block \(m\le 2M\) used by the [Yilin Liu R counterexamples](https://hexagonmath.org/pdf/2611.00788v1), with bound \(O(L\sqrt{M/N})\) for polylogarithmic \(M\). This estimate covers arbitrary superpositions of their witnesses in this block, not merely their exhibited single entries. It is consistent with the much smaller R threshold. On fixed \(\rho\) the two individual hard-prefix discrepancies are necessary and sufficient for weak-S smallness of this **one** block. Neither the full operator nor uniform cancellation for either correlation is obtained.

## 1. Exact model and a uniform two-form mass cap

The [physical log representation](r25-arithmetic-minor-prefix.md) has kernel \(2\pi A_N(x,y)/(xy\sqrt{w_N(x)w_N(y)})\), with \(A_N\) the normalized signed cumulative weighted by \(\sqrt{uv}\) and \(w_N(x)=((Nx)^{-2/L}+(Nx)^{-1/4})^{-1}\). If \(x\le\rho,y\in J\), its cumulative sees exactly two possible alias lines: \(v=1+u\), sign plus, and \(v=1-u\), sign minus. Each has density \(S\,du\) in the continuous subtractand and atoms \(\Lambda(m)\Lambda(N\pm m)/N\) at \(u=m/N\) for \((m,N)=1\). No diagonal or other alias enters: \(0<u\le\rho\) and \(0<v\le y\le 6/5\), with \(u,v>0\), permit only the stated nonzero relations. The positive difference and negative sum models thus have the appropriate, shared singular series, but are not combined when probing a single line.

For an ordinary interval of raw length \(H\ge N^{1/4}\) in \([0,N/10]\), the positive Mangoldt pair mass on either line, even omitting units, is \(O(SH)\). Indeed use the two-form Selberg sieve to \(z=H^{1/20}\), with root counts \(\nu_p=1\) when \(p\mid N\) and \(2\) otherwise (including \(\nu_2=1\)). CRT gives remainder \(O(\nu(d))\) for squarefree moduli. The [Selberg upper bound](https://kskedlaya.org/ant/chap-selberg.html) with optimized weights at most one in absolute value is \(H/G(z)+O(z^4)\), where

\[
 G(z)=\sum_{d<z}\mu^2(d)\prod_{p\mid d}\frac{\nu_p}{p-\nu_p}.
\]

The error uses at most \(z^2\) weight pairs and \(\nu([d,e])\le[d,e]\le z^2\). To see the required singular factor, form all squarefree products of primes up to \(z^\eta\) for small fixed \(\eta>0\), with the displayed positive weights. Their average \(\log d\) after normalizing is \(\sum_{p\le z^\eta}(\nu_p/p)\log p\ll\eta\log z\), so at least half the mass lies at \(d<z\). The full mass \(\prod_{p\le z^\eta}(1-\nu_p/p)^{-1}\) is \(\gg(\log z)^2/S\): the squared Mertens product is divided by \(\prod_{p\le z^\eta}(1-\nu_p/p)/(1-1/p)^2\), which is \(O(S)\) directly by the Goldbach local factors and the nonzero convergent twin-prime product. If both prime bases exceed \(z\) their pair is in the sifted set and the total weight per pair is \(O(L^2)\). If either base is at most \(z\), the sum of its Mangoldt weights over powers is \(O(L)\) for each base and each power fixes the other form, giving \(O(zL^2)\) altogether; thus all prime powers are covered. Since \(\log z\asymp L\), all errors are absorbed in \(O(SH)\). Shorter edge strips can be enlarged for this positive bound.

For any raw prefix length \(H\ge1\) the simple alternative is \(O(LH)\), from \(\sum_{m\le H}\Lambda(m)\ll H\) and the bounded high leg \(\Lambda(N\pm m)\le O(L)\); below length 1 there are no atoms. The continuous part has mass at most \(S\) times its dimensionless length. It follows that \(|A_N(x,y)|\ll Lx^{3/2}\) always in the block, and \(|A_N(x,y)|\ll Sx^{3/2}\) if \(x\ge N^{-3/4}\). On \(y\in J\) the Hardy weights and log length are bounded. Squaring the kernel and using \(\int_0^d dx/w_N(x)\ll d+1/N\) (integrate the two explicit powers, splitting at \(1/N\)) handles the actual edge. The two bounds give (1), using the sharper cap only for \(x\ge N^{-3/4}\). The Riesz vectors of the external paper's compact probes lie in their physical support intervals, as also follows below.

## 2. Two directions without a hidden alias cancellation

On \(N^{-3/4}\le x\le\rho\), each line contributes an interval of its signed discrepancy measure in \(0<u\le x\), with mass bounded by \(2E_N^*\), using left limits as necessary for endpoint atoms. Abel summation with \(\sqrt{u(1\pm u)}\), of supremum and total variation \(O(\sqrt{x})\), gives \(|A_N(x,y)|\ll E_N^*\sqrt x\). Combine with the positive cap and \(w_N(x)\ge1/2\). The kernel is bounded by \(C\min(S\sqrt x,E_N^*/\sqrt x)\); its square integrates in \(d\log x\) to \(O(SE_N^*)\), splitting at \(x=E_N^*/S\) or using the appropriate single bound if that split is outside. The preceding exact edge estimate gives the first inequality of (2).

Conversely let \(N^{-3/4}\le\delta\le\rho/10\). For \(t<4\delta\), the mass cap on the enlarged prefix gives \(|E_N^\pm(t)|\ll S\delta\). Otherwise choose smooth \(0\le f\le1\) supported in \([\delta,t-\delta]\), equal to one on \([2\delta,t-2\delta]\) (with a zero-length middle interval harmless), derivative \(O(1/\delta)\) on two intervals of length \(O(\delta)\). Choose smooth \(g_+\) supported in \(J\cap(1,\infty)\) and one on \([1+\delta,1+\rho]\), cutting on with width comparable to \(\delta\) at the lower turn and fixed width at the upper turn. Choose the mirrored \(g_-\) below 1, equal to one on \([1-\rho,1-\delta]\). Thus one high weight is one on the intended alias for every point of the low support and zero on the other alias. All functions lie strictly inside the required projections; in particular the low weight vanishes near both zero and its upper edge even at \(t=\rho\).

For a real physical weight \(f\), the vector with log representative \(-u^2\sqrt{w_N(u)}(f(u)/\sqrt u)'/\sqrt{2\pi}\) has exact squared norm \((2\pi)^{-1}\int_0^\infty w_N(u)|f(u)/2-u f'(u)|^2du\), as in Li–Liu Proposition 7.4. Its support is within that of \(f\). Both low and high probes therefore have vector norm \(O(\delta^{-1/2})\), because \(w_N\) is bounded on their supports and steep derivatives lie on lengths \(O(\delta)\). The exact cumulative-kernel pairing integrates that representative against the primitive on each leg, yielding \(f(u)/\sqrt{2\pi u}\) and \(g(v)/\sqrt{2\pi v}\). The kernel's \(2\pi\sqrt{uv}\) cancels exactly. Hence the pairing \(\langle T_N v_{g_\pm},v_f\rangle\) is the single \(f\)-weighted centered discrepancy with its outer sign, for the arithmetic and continuous terms alike. In particular the continuous contribution is the one-line integral, not a cancellation improperly borrowed from the two-line test in the external paper. The bound on this pairing is \(O(\delta^{-1}\|B_{N,\rho}\|)\). Passing from smooth to hard incurs only the two edge strips of width \(O(\delta)\), in both arithmetic and model, of size \(O(S\delta)\) from the mass bound. Therefore

\[
 E_N^*\ll S\delta+\delta^{-1}\|B_{N,\rho}\|.
\]

Choose \(\delta=\max(N^{-3/4},\sqrt{\|B_{N,\rho}\|/S})\) if it is at most \(\rho/10\), otherwise use the crude bound \(E_N^*\ll_\rho S\) (positive mass at the full prefix). This proves the second inequality of (2).

## 3. The two actual minor coefficients left under global Dirichlet GRH

Set \(Y=4N\), \(P=Y^{2/5}\) and use the same arcs as the [localized R25 major estimate](r25-arithmetic-minor-prefix.md). Write \(U(\alpha)=\sum_{n\le Y}\Lambda(n)e(n\alpha)\), \(U_t(\alpha)=\sum_{m\le Nt}\Lambda(m)e(m\alpha)\). For \(t\ge P^2/N\), define

\[
 Z_N^-(t)=N^{-1}\int_{\mathfrak m} U_tUe(-N\alpha)\,d\alpha,\qquad
 Z_N^+(t)=N^{-1}\int_{\mathfrak m} U_t\overline Ue(N\alpha)\,d\alpha,
\]

and set both zero below that. These are the ordinary, unit-free arc coefficients, one from each line. The localized GRH major estimate with shorter support length \(Nt\) gives \(O_\epsilon(\sqrt{Nt}P N^\epsilon)\) raw error after subtracting the individual line model. In both cases its full continuous overlap is exactly \(Nt\), the partner lies in \([0,Y]\), and the coefficient is \(S\). The unit correction is \(O(L^3/N)\) normalized (sum over powers of primes dividing \(N\) on the low leg, their partner being uniquely fixed). For \(t<P^2/N\), prove \(|E_N^\pm(t)|\ll SP^2/N\) by bounding the positive part by the enlarged prefix; its raw length \(P^2\) is within the sieve bound. Thus

\[
 \max_{\pm}\sup_{0\le t\le\rho}|E_N^\pm(t)-Z_N^\pm(t)|\ll_\epsilon N^{-1/10+\epsilon}.
\]

At inverse-log accuracy the necessary and sufficient arithmetic inputs for this block are therefore two *separate*, pointwise hard-prefix minor bounds at exceptional even moduli. For a fixed positive \(t\) they are the first Goldbach sum discrepancy and the first shifted prime-pair difference discrepancy with macroscopic raw low interval \([0,Nt]\). Their short intervals around the spectral test endpoints are controlled only in upper mass by sieve; neither a GRH progression estimate for one prime leg nor the ordinary modulus-average minor moment evaluates the simultaneous prime pair for each fixed \(N\). No assertion is made about other blocks or the conjecture as a whole.
