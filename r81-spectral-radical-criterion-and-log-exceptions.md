# A pointwise radical criterion and smaller exceptions for the true mixed strip

**Scope.** This strengthens the [whole mixed parity result](r80-spectral-whole-mixed-parity-density.md). Its unconditional full signed correlation and original polynomial-major conclusion now have arbitrary fixed inverse-logarithmic exceptional count. On an explicit growing-radical family we also obtain these densities at the **actual auxiliary polylogarithmic major arcs**, unconditionally and pointwise. The corresponding **original polynomial major** on that family still uses the historical prime and masked-Möbius Dirichlet GRH of the [pointwise parity calculation](r67-spectral-high-mixed-parity-major.md). There is no pointwise full or original-minor result, in particular none on all powers of two.

Use the notation, exact squarefree mixed coefficients $M_\pm$, hard central intervals and bounded-variation left weights of the whole mixed parity result. The plus sign is even total parity. In particular $L=\log N$, $L_2=1+\log L$, and $B>B_0>0$ are fixed cutoffs. Put

$$
 \mathcal A(N)=\prod_{\substack{p\mid N\\p>2}}
       (1-\alpha_p^\circ p^{1/4})^{-1},
 \qquad \alpha_p^\circ=(p-1)/(p^2-2) \quad(p>2).
$$

Write $\mathcal T(N;I,\omega)=\Sigma(N)\int_I\omega(u)/\log(N-u)\,du$ and

$$
 \mathcal R_A(N;I)=
        \frac{\Sigma(N)|I|}{L}e^{-c\sqrt{L_2}}+N L^{-A}.
$$

For some fixed $b,c>0$ depending on the cutoffs we have the following.

1. If the even target satisfies $\log\mathcal A(N)\le b\sqrt{L_2}$, then for each fixed $A>0$ choose $K$ sufficiently large. On the genuine auxiliary majors of reduced denominator at most $L^K$ and radius $2L^K/N$, the integral of $M_+$ is $\mathcal T+O_A(\mathcal R_A)$ and that of $M_-$ is $O_A(\mathcal R_A)$, unconditionally. The same holds on the common auxiliary arcs of denominator bound $(\log Y)^K$ and radius $2(\log Y)^K/Y$ for such $N\in[Y,2Y]$. Under the historical GRH inputs of the pointwise parity calculation the same formula holds on the actual moving original polynomial majors for each such $N$.
2. Unconditionally, the genuine full signed correlations and original moving polynomial-major integrals obey these formulas outside $O_A(Y(\log Y)^{-A})$ even targets in $[Y,2Y]$, simultaneously for all the usual hard and BV left tests.

The deterministic family includes every fixed even radical, and for any fixed $\epsilon>0$ every sufficiently large even target with at most $L_2^{2-\epsilon}$ distinct prime divisors. This is not a right small-prime selector: none of the genuine coefficients has changed.

## 1. Complete the auxiliary major at each such target

The exact parity calculation on auxiliary arcs in §1 of the whole mixed parity proof uses unconditional prime and masked-Möbius Siegel--Walfisz, positive squarefree CRT, and BV real amplitudes. These progression and real-integral steps do not average over targets. The version with moving auxiliary arcs uses $Y$ comparable to $N$ in its estimates, with slow radius $2L^K/N$ in place of $2(\log Y)^K/Y$; all length and log-error bounds are unchanged. Only the completion of the rational series there lost exceptional targets. We replace that completion pointwise.

For each squarefree denominator $q$ the formal right density has sup plus variation $O(L^C C_1^{\omega(q)}/q)$, from the genuine occupancy argument, also for formal coefficients past the cutoff. Its normalized absolute tail at $Q_0=L^K$ (or $Q_0=(\log Y)^K$ for $N\asymp Y$) is bounded by

$$
 L^C\sum_{\substack{q>Q_0\\q\ {\rm sf}}}
             \frac{C_1^{\omega(q)}|c_q(N)|}{q\varphi(q)}.
$$

Insert $(q/Q_0)^{1/4}$ and extend the positive sum. At $p\nmid N$ the Euler increment is $O(p^{-7/4})$, since $|c_p(N)|=1$, while at $p\mid N$ it is $O(p^{-3/4})$ since $|c_p(N)|=p-1$. At odd primes $\log\mathcal A(p)\asymp p^{-3/4}$ by the definition; the prime 2 costs a fixed factor. The normalized tail is therefore

$$
                 O\!\left(L^C Q_0^{-1/4}\mathcal A(N)^{C_2}\right)
 \tag{1}
$$

with fixed $C_2$. Under the deterministic criterion its last factor is $\exp(O(\sqrt{L_2}))=L^{o(1)}$. Thus $K$ sufficiently large gives integrated error $O_A(NL^{-A})$. The usual BV Fourier tail at the auxiliary slow radius costs $O(NQ_0^{-1}L^C(1+\log Q_0)^{O(1)})$, as in the original common auxiliary calculation. Hence the exact completed density (2) of the whole mixed proof holds pointwise on this family at either stated auxiliary arc set.

By (4) of the whole mixed proof, its actual bracket times $P_N$ equals $(1\pm1)$ with uniform error $O(\mathcal A(N)^2e^{-c_3\sqrt{L_2}})$. The Euler constant $P_NJ_{N,\infty}=1$ holds for each even $N$, not a mean over radicals. Choose $b<c_3/4$ and a smaller $c>0$ for the error. This gives the pointwise auxiliary formulas. Under the historical GRH inputs the original polynomial-major formula is already exact for every even modulus by the pointwise parity proof; the same deterministic radical bound on its bracket gives the claimed conditional extension. If $r$ is the number of distinct primes dividing $N$, then $\log\mathcal A(N)\ll\sum_{j\le r}(j+1)^{-3/4}\ll(r+1)^{1/4}$ by ordering the primes. This verifies the example growing family.

## 2. A growing moment and the genuine even-target exception count

For real $m\ge2$, expand the positive Euler power over squarefree divisors and use $\#\{N\le2Y:d\mid N\}\le2Y/d$. This gives

$$
 \frac1{2Y}\sum_{N\le2Y}\mathcal A(N)^m
    \le \prod_{p>2}\left(1+\frac{\mathcal A(p)^m-1}{p}\right).
 \tag{2}
$$

Split at $P=m^{4/3}$. For smaller primes the log factor is at most $m\log\mathcal A(p)\ll mp^{-3/4}$, with total $O(mP^{1/4})=O(m^{4/3})$, even summing over all integers up to $P$. For larger primes $m\log\mathcal A(p)\ll1$, so the log factor is $O(mp^{-7/4})$ and their total is $O(mP^{-3/4})=O(1)$. The log of (2)'s right side is therefore $O(m^{4/3})$, with an absolute constant independent of $Y$ and $m$.

Write $v=\log\log Y$. Failure of the deterministic criterion for $N\in[Y,2Y]$ entails $\log\mathcal A(N)>b\sqrt v$. Take $m=\lfloor\epsilon v^{3/2}\rfloor$ for a sufficiently small fixed $\epsilon>0$ depending on $b$. By Markov the number of failures is at most

$$
       2Y\exp(Cm^{4/3}-bm\sqrt v)
                   \ll Y\exp(-c_4v^2),
 \tag{3}
$$

since $C\epsilon^{4/3}<b\epsilon/4$ can be arranged. This is smaller than $Y(\log Y)^{-A}$ for each fixed $A$. The condition and count are for actual targets, not a substitute random radical.

On all remaining targets apply the deterministic formula at the **common** auxiliary major arcs. The complementary signed integral on the actual common complement has the unconditional maximal Bessel estimate of §3 of the whole mixed proof. That estimate preserves the true cutoff arithmetic by its divisor-bound squared norm error and keeps the exact moving physical intervals. For each desired $A$, choose its mesh and then $K$ large enough to give signed complementary integral $O_A(YL^{-A})$ outside $O_A(Y(\log Y)^{-A})$ targets, uniformly in the left BV and hard gates. This is independent of the new radical estimate. Adding by Fourier inversion proves the full formulas. Finally the [actual moving original-minor bound](r79-spectral-original-minor-power-exception.md) applies to each fixed common parity mask, giving genuine power saving outside a power-small exceptional set. Subtract that actual minor from the full correlation. The original polynomial major formula then follows unconditionally on the same good family, with the stated adjustment to its exceptional count. No polynomial-modulus GRH is used in this density conclusion.

For instance, for any fixed $C>0$ this unconditional conclusion holds with arbitrary fixed inverse-logarithmic **relative** exceptional proportion among the even targets in any compatible residue class of modulus at most $(\log Y)^C$: use the global estimate with a larger log exponent before counting that class. This does not reach a family specified by an exact fixed radical, which may be much smaller. In particular the pointwise auxiliary-major calculation is not an unconditional evaluation of the full correlation on all powers of two.
