# The exact shrinking divisor gap for two higher sparse bands

Use the same genuine central negative sum line, strict $D,Q$, hard interval $I$, squarefree unit selection, and two higher sparse lower alphabets $[\exp(c_i T),\exp(d_i T)]$ of the [proper-divisor-gap theorem](r67-source-two-higher-bands-proper-divisor-gap.md). Write $L=\log N$, $\ell=\log L$, $T=L/\ell$, $D=\lfloor\sqrt N e^{-20T}\rfloor$, $Q=\lfloor N e^{-20T}\rfloor$. On $n=su,m=tv$ the lower products $s,t$ are nonempty, without product caps, and the nonempty rough parts $u,v$ have all primes $\ge N^\kappa$, with $0<\kappa<1/4$ fixed. Replace the fixed-power proper-divisor gap on the designated first side by the exact integer condition

$$
  f\mid u,\quad 1<f<u\quad\Longrightarrow\quad
   f\notin (D_s,E_N],\qquad
  D_s=\left\lfloor D/s\right\rfloor,\quad
  E_N=\max\!\left(D,\left\lfloor Q/(D+1)\right\rfloor\right).
 \tag{1}
$$

The other side is unrestricted. Reflection allows either side to have (1), using the corresponding lower product in $D_s$. This is still a mask on the outer integer, not a change to the divisor labels.

**Theorem (unconditional, pointwise).** For every fixed $A>0$, all sufficiently large even $N$, all central hard intervals $I$ and all additional masks independent of the interior labels,

$$
  |R_N(I)|\ll_{\rho,\kappa,c_i,d_i,A}
    \mathfrak S(N)\left(\frac{|I|}{(\log\log N)^2}+NL^{-A}\right).
 \tag{2}
$$

Here $R_N(I)$ is exactly the original signed sum from that theorem, including $d>D$, $e>D$, $de>Q$. When the designated $s=e^{O(T)}$, the excluded log width in (1) is $20T+\log s+o(1)=O(T)$ instead of a fixed multiple of $L$. This geometric saving is not an assertion that all allowed products in the uncapped theorem have size $e^{O(T)}$. The two-sided near-half residual that still violates (1), as well as Hypothesis S, remains outside the bound.

## 1. Integer geometry and reuse of the polynomial sieve

The sparse Rankin argument in §1 of the proper-divisor-gap theorem applies without a fixed-gap hypothesis. Use its parameter $K_0/T$ for large fixed $K_0$ and now choose $\varepsilon=1/32$. It permits $s,t\le N^\varepsilon$ at true error $O_A(NL^{-A})$. Thus $s,t<D$ and $u,v\ge\rho N^{1-\varepsilon}>\sqrt N$. The empty rough label on the designated side is genuinely short. The full label is genuinely long against every admitted opposite divisor, since $E_N\le\sqrt N$.

For any proper rough label in that side, (1) gives one of two possibilities.

- If $f\le D_s$, then $a f\le s f\le D$ for **all** lower divisors $a\mid s$. All are excluded even at equality under the original strict cutoff.
- If $f>E_N$, then $f>D$ and $f(D+1)>Q$. Indeed for an integer $f$ the condition $f>\lfloor Q/(D+1)\rfloor$ is precisely the strict inequality $f>Q/(D+1)$. Every opposite admitted integer $e>D$ is at least $D+1$, so all $af$ pass both original tests against it.

Thus the chosen sufficient condition is exact even at a divisibility or rounding boundary. It need not be necessary if the particular target never has an opposite divisor near $D+1$. The complete first-side lower orbits now give $\mu(f)\Lambda(s)$ just as before, independently for each actual opposite $e$. The composite lower products cancel exactly; the retained ones are first-band primes $q$ with absolute marked weight $O_\kappa(\log q)$. The remaining right test is exactly $e>D$.

All subsequent estimates in §§2–3 of the proper-divisor-gap theorem then apply with $\varepsilon=1/32$: the opposite D-only least-prime switch has width $O(T)$ on a nonempty proper rough label $g$, and its cap $g\le D$ permits frozen $(h,k)=(q,tg)$ with $hk\le N^{1/2+2\varepsilon}$. In the unswitched light term freeze $(q,t)$. The two remaining rough complements are nonempty and have cutoff $N^\kappa$, the frozen coprimalities remain exact, and the polynomial sieve at $Z=N^{(1/2-2\varepsilon)/24}$ yields the same factor $L^{-2}$ and summable floor errors. Each band has bounded reciprocal mass; its log mark costs $O(T)$, with the heavy right log and its strip costing at most $L\cdot O(T/L)=O(T)$. Therefore the main bound is $O(\mathfrak S(N)|I|T^2/L^2)$ plus the stated errors, giving (2). To verify the logarithmic width, $\log D=\tfrac12 L-20T+o(1)$ and $Q/(D+1)=\sqrt N(1+o(1))$ by the exact floors. The log changes caused by the extra floors in (1) are $o(1)$ uniformly when $s\le N^\varepsilon$. Thus $\log E_N-\log D_s=20T+\log s+o(1)$ on the retained range.

## 2. A nonzero pairing excluded by both fixed-power gaps

Choose an external scale $X$ and distinct lower primes $s,t$ strictly inside the higher bands, using fixed interior logarithmic proportions at $T_X$. For each side choose a rough prime $F$ near $D_X/(2s)$ (respectively $D_X/(2t)$) in a narrow proportional window. Choose its other two distinct rough primes near $\sqrt{X/(2sF)}$ (respectively with $t,F$ on the other side), making all constituents globally distinct. Ordinary PNT supplies the primes. Both actual integers are then close to $X/2$, giving central units on their even target sum $N=X(1+O(\epsilon_0))$ for arbitrarily small fixed relative window parameter $\epsilon_0>0$. The discrete exponent $T_N$ differs from $T_X$ by $O(1/\log\log X)$ by the derivative of $L/\log L$. The ratio $D_N/D_X$ is $1+O(\epsilon_0)+o(1)$ by the same calculation and the original floor. Hence the first near-half prime on each side is $\le D_N/s$ or $\le D_N/t$ respectively, with room from the factor two. Its exponent is $1/2+o(1)$, so it violates every fixed positive power gap on each side.

The two remaining one-prime rough labels are of size $N^{1/4+o(1)}$ and short even after the entire lower product. Their pair has size $\asymp X/D_X$, and exceeds $E_N\le\sqrt N$ by a factor growing like $e^{20T_X}$. The two pairs containing the near-half prime each have size $N^{3/4+o(1)}$, hence are also above $E_N$. Thus on both actual operands the only proper labels are either short or uniformly long under (1). All rough factors exceed $N^\kappa$ for $\kappa<1/4$. On either side the summed long rough Möbius sign is $3-1=2$, because exactly the three pairs and the complete triple are long. The lower products are primes, so their full marked orbits are their logarithms, with the signs in the proper-divisor-gap theorem. The original pair therefore has actual summand $-4\log s\log t$. This shows the new geometry is not just the reflected fixed-gap sector, nor a class where the true signed term always vanishes. It asserts no lower bound on the combined sum.
