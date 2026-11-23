# Least-prime toggling strengthens the genuine medium-factor first moment

Use exactly the central signed sum, strict original cutoffs, dyadic prime alphabets, integer masks and notation from the [medium-prime first-moment theorem](r64-source-medium-prime-orbit-first-moment.md). Thus the designated squarefree leg has lower product $s>1$, there is at least one rough prime on each side, and both **may** have multiple rough primes and an unrestricted number of medium primes. In the notation of that theorem, set

$$
 \Psi_1=1+
 \sum_{p\in\mathscr P_1}\frac{2\log p/p}
                {\displaystyle\prod_{\substack{\ell\in\mathscr P_1\\\ell\le p}}
                       (1+2/\ell)} .
 \tag{1}
$$

The product in the denominator includes $p$. This quantity uses only the fixed dyadic prime alphabet, not the target-dependent integer masks.

**Theorem (unconditional).** For every real $\zeta>0$ the same genuine maximal first moment satisfies

$$
 \sum_{\substack{X\le N\le2X\\2\mid N}}R_N^*
 \ll_{\rho,\kappa} X^2 M_2
       \left(\frac{M_1\Psi_1}{L}+X^{-\zeta/4}M_1(\zeta)\right).
 \tag{2}
$$

In particular, for complete lower ranges up to $y_i(N)=\exp((\log N)^{\alpha_i})$ with fixed $0<\alpha_i<1$, the bound is

$$
 \sum_N R_N^*
 \ll_{\rho,\kappa,\alpha_1,\alpha_2} X^2 L^{-1+2\alpha_1+2\alpha_2}.
 \tag{3}
$$

This raises the equal-exponent range with a logarithmic saving to every fixed $\alpha<1/4$. If instead the designated side has the complete lower range with $\alpha_1<1/2$ and its partner draws lower primes from the much higher band $\exp([c_2,C_2]\log N/\log\log N)$ of that theorem, the bound is $O(X^2L^{-1+2\alpha_1})$. In each case a bound $O(X^2L^{-b})$ with $b>0$ means uniformly $R_N^*\ll NL^{-\gamma}$ for each fixed $0<\gamma<b$ outside $O(XL^{-b+\gamma})$ even targets. If the designated side is originally second, reflect $I$ and exchange the ordered slots. These statements concern the same selected actual arithmetic block and do not give a uniform pointwise estimate, a bound linear in short-window length, or Hypothesis S.

## 1. An exact switch along a single lower prime

The discarded tail $s>X^{1/4}$ keeps exactly its Rankin bound from the medium-prime theorem. Work with retained $1<s\le X^{1/4}$. Fix an actual opposite divisor $e>D_N$, and write $T_e=\max(D_N,Q_N/e)$ as there. Fix a rough divisor $f\mid u$ on the designated side, and put $p=P^-(s)$, the least prime factor of $s$. Each lower divisor $a\mid s$ is uniquely either $c$ or $pc$, where $c\mid s/p$. For this pair put $W_c=\log(n/(cf))$, $J_0=\mathbf 1_{cf>T_e}$ and $J_1=\mathbf 1_{pcf>T_e}$. Its **actual signed** contribution is

$$
 \begin{split}
 &\mu(cf)J_0\log(n/(cf))+\mu(pcf)J_1\log(n/(pcf))\\
 &=\mu(cf)\bigl(-W_c\,\mathbf1_{cf\le T_e<pcf}
                         +(\log p)J_1\bigr).
 \end{split}
 \tag{4}
$$

Squarefreeness and separation of prime alphabets give $\mu(pcf)=-\mu(cf)$. This identity uses the strict original $D_N$ and $Q_N$ conditions through $T_e$, including exactly the stated switch endpoints. The heavy term in (4) is supported on

$$
 \log f\in(\log T_e-\log c-\log p,\ \log T_e-\log c].
 \tag{5}
$$

The width is $\log p$, not $\log s$. Both the $f=1$ and $f=u$ cases have no heavy term, since $s<D_N$ and $u>\sqrt N$. The statement and proof do not require assuming that the complementary light term vanishes. It will be bounded directly at weight $\log p$.

## 2. Dyadic counting and the least-prime moment

For fixed opposite $m,e$, fix $s,c$ and a proper nonempty rough label $f$. The bounded dyadic variation of $\log T_e$ proved in the medium-prime theorem widens (5) only by $O(1)$. Keep one rough prime free to count by the genuine-prime upper bound $O_\kappa(X/(s w L))$, where $w$ is the product of the other rough primes. As in its proper-subset argument, one different coordinate of $w$ has coefficient $+1$ in $\log f$ if the free prime is absent, or coefficient $-1$ after writing $\log f=\log n-\log s-\sum_{p_i\notin f}\log p_i$ if it is present. The physical envelope still gives $\log n=\log X+O_\rho(1)$. Since $c$ is fixed, the constrained rough coordinate has reciprocal prime mass $O_{\rho,\kappa}((1+\log p)/L)$. Sum the other rough reciprocals, use $W_c\le \log(2X)$, and then sum over the at most $\tau(s)/2$ distinct $c$ choices. The heavy total for this fixed $m,e$ is therefore

$$
 \ll_{\rho,\kappa} \frac{X}{L}
     \sum_{\substack{s>1\ {\rm squarefree}\\p'\mid s\Rightarrow p'\in\mathscr P_1}}
            \frac{\tau(s)(1+\log P^-(s))}{s}.
 \tag{6}
$$

For every light term of (4), enlarge positively by forgetting $J_1$ and count the last rough prime by the same genuine-prime bound. At weight $\log p$ this costs at most (6), without needing any short log strip. The number of choices of $f$ is bounded in terms of $\kappa$. When there is only one rough prime there is no heavy term, and the light argument still holds.

Factor the nonnegative sum with $\log P^-(s)$ by its least prime. Exactly

$$
 \sum_{s>1}\frac{\tau(s)\log P^-(s)}s
  =\sum_{p\in\mathscr P_1}\frac{2\log p}{p}
             \prod_{\substack{\ell\in\mathscr P_1\\\ell>p}}(1+2/\ell)
  =M_1(\Psi_1-1).
 \tag{7}
$$

The additional weight $1$ in (6) costs at most $M_1$. Thus (6) is $O_{\rho,\kappa}(XM_1\Psi_1/L)$. Multiply by the opposite total divisor weight $O_\kappa(XM_2)$ from the medium-prime theorem. Each genuine pair contributes to just $N=n+m$; the positive envelopes after (4) are uniform in all the permitted hard windows and integer-only masks. Add the unchanged tail to prove (2).

For a complete alphabet $\mathscr P_1=\{p\le y_1(2X)\}$, prime Mertens gives $\prod_{\ell\le p}(1+2/\ell)\gg(\log p)^2$, uniformly in $p$. Hence $\Psi_1\ll 1+\sum_p 1/(p\log p)\ll1$; the latter series converges by Chebyshev on the ordinary dyadic intervals. Use $M_i\ll L^{2\alpha_i}$ and the same superlogarithmically small Rankin tail as in the original theorem to get (3). The moving upper limit $y_1(N)$ may be smaller than the fixed envelope; the integer-mask uniformity permits this, and (7) is a positive moment of the envelope. If the partner is in the higher band, $M_2\ll1$ as previously proved, with no change in the designated tail. When the designated alphabet is itself a sparse medium band, the uniform inequality $\Psi_1\le1+2B_1$ recovers the original size; no bounded least-prime moment has been assumed for such a band. Markov gives the stated exception counts and leaves the unresolved pointwise and full-operator gaps unchanged.
