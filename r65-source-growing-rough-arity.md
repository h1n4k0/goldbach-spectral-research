# Growing rough arity at a subpower cutoff: a pointwise extension

Use the exact squarefree central sum, strict cutoffs $D,Q$, unit conditions, hard interval $I$, and lower-prime alphabets of the [pointwise rough-complement theorem](r65-source-pointwise-rough-complements.md). Thus $n=su$, $m=tv$, with the primes of the nonempty lower products in their respective ranges up to $y_i=\exp(L^{\alpha_i})$, $L=\log N$. Each $u,v$ is nonempty. Either one or two lower products must be nonempty; an empty slot is assigned $\alpha_i=0$ in the bounds. Keep fixed $\alpha_i<1$ and $\sigma=1-2\alpha_1-2\alpha_2>0$. Write $\ell=\log L$, $T=L/\ell$, and fix any $C>0$. Replace the fixed polynomial roughness condition by

$$
       p\mid uv \ \Longrightarrow\ p\ge Y=\exp(CT),
       \qquad \nu=\frac{\log 2}{C}.
 \tag{1}
$$

The two ranges are disjoint for sufficiently large $N$. Rough arity is now allowed to grow with $N$. Integer masks independent of the interior divisor labels remain allowed.

**Theorem (unconditional, pointwise).** For every fixed $A>0$, every sufficiently large even $N$, and all the stated hard intervals and masks,

$$
  |R_N(I)|\ll_{\rho,C,\alpha_1,\alpha_2,A}
    \mathfrak S(N)\bigl(|I|\ell^5 L^{-\sigma+\delta}+NL^{-A}\bigr),
 \qquad
 \delta=
 \begin{cases}
      \max(0,2\nu-1), &s,t>1\text{ on the selected block},\\
      2\nu, &\text{exactly one lower product is nonempty}.
 \end{cases}
 \tag{2}
$$

Thus $C\ge 2\log 2$ gives the full exponent $\sigma$ when both lower products are nonempty; when one is empty any $C>2\log 2/\sigma$ gives a positive log saving. The constants and the sufficiently-large threshold may depend on $C$; no result for a varying $C$ is asserted. This extends the rough lower edge to a subpower prime scale, not the lower alphabet to arbitrary primes in the gap $(y_i,Y)$. Both-empty blocks and Hypothesis S are outside the statement.

## 1. Explicit reciprocal and multiplicity bounds

Define $K=\lfloor L/\log Y\rfloor=\lfloor\ell/C\rfloor$. Every true rough part has at most $K$ factors because it is an integer $\le N$. Therefore its number of divisor labels is at most $2^K\le L^\nu$. Use this loss only when a rough label is not frozen, and only on the true inputs before making any positive enlargement. A frozen rough product contributes a bounded factor to the local upper-sieve multiplier:

$$
   \prod_{p\mid f}\frac{p-1}{p-2}
      \le \exp(O(K/Y))=1+o_C(1)
 \tag{3}
$$

if $f$ is a rough part of a true integer. No factors on lower primes are dropped.

For all squarefree products of primes in $[Y,N]$, including $1$, the unrestricted reciprocal mass is bounded by

$$
    \prod_{Y\le p\le N}(1+1/p)\ll \frac{L}{\log Y}\ll_C \ell .
$$

For a **nonempty** such product constrained to an arbitrary interval of width $W$ in its logarithm, split off one prime and fix the remaining product. Overcounting all choices is harmless for this nonnegative upper bound. The prime then lies in a log interval of width $W$ in $[Y,N]$, with reciprocal prime mass $O((1+W)/\log Y)$ by Chebyshev on the enclosing unit-log intervals. Summing the frozen product reciprocals gives

$$
          O_C\!\left(\frac{(1+W)\ell^2}{L}\right).
 \tag{4}
$$

This avoids a number-of-slots loss in the strip. In particular, the free opposite frozen rough product costs only $O_C(\ell)$, not a separate harmonic sum for each of its at most $K$ positions.

## 2. The same exact switches and the same affine sieve

The tail bound defining $s,t\le e^T$ remains valid pointwise. In the original Cauchy upper bound replace the bounded rough multiplicities by $L^{2\nu}$ across the two factors; this is a fixed log power. Rankin for the nonempty lower side still gains $\exp(-T/\log y_i)=\exp(-L^{1-\alpha_i}/\ell)$, which absorbs that loss and every fixed inverse logarithm. The result is $O_{C,A,\alpha_1,\alpha_2}(NL^{-A})$ on the original sum line, including when the other lower product is empty.

On $s,t\le e^T$, the exact switching identities, the estimate $\max(D,Q/e)\le\sqrt N$ for actual $e>D$, and the exclusion of empty and full switching rough labels remain literally the same. They use the sizes of the complete lower and rough products, not fixed arity. The affine upper bound (2) of the rough-complement theorem is likewise unchanged: take $Z=e^T$, $z=e^{\eta T}$ with $0<\eta<\min(C,\eta_0)$ fixed and $\eta_0$ the small absolute sieve constant. A nonempty remaining rough product is then free of primes $\le z$ by (1). The determinant is still $N$ and the same coprime frozen cofactors give the ordinary binary singular series times their two extra local factors. Since $\log z=\eta T$, the real density bound is $O_C(\mathfrak S(N)\lambda^*(h)\lambda^*(k)/T^2)$, and the hard-interval count has the same $e^{6T}$ error. In particular, the sieve is never being applied to true products having rough primes below its level.

The genuine freezes from the rough-complement theorem give $hk\le Ne^{-18T}$ in all terms, and the pure light terms have the much smaller $hk\le e^{2T}$. For each frozen pair the lower and rough factors are uniquely determined because of the gap between the alphabets. There are at most $e^{2T}$ lower divisor-label choices (from $\tau(s)\tau(t)$), and at most $L^{2\nu}$ choices of any still-unfrozen rough labels on true pairs. The number of frozen pairs is $O(Ne^{-18T}L)$. Thus the uniformly summed $e^{6T}$ errors, even with all allowed absolute logarithmic weights $\ll L^2$, are

$$
              O_C(Ne^{-10T}L^{3+2\nu})=O_{C,A}(NL^{-A}).
 \tag{5}
$$

This includes either convention for a hard interval endpoint and does not require that a specific hard window have long lattice length.

## 3. Main upper bounds, with every arity loss accounted for

Use exactly the signed double switch or single switch already proved. After identifying its genuine switch support, a positive affine upper bound may be taken as in the rough-complement theorem. The lower reciprocal factors, including each retained local $\lambda^*(s)$, have the same $O((\log(2y_i))^2)$ profiles from the [two-rough-prime theorem](r65-source-pointwise-two-rough.md), both with no least-prime mark and with a factor $1+\log P^-(s)$. The separate profiles in the two slots therefore cost $O(L^{2\alpha_1+2\alpha_2})$; an empty side costs one. A short strip uses (4), with $1+W$ at most a constant times $1+\log P^-$ in the corresponding side. Use (3) for all genuine frozen rough factors.

For clarity each bound below is its main upper contribution **after** division by $\mathfrak S(N)|I|$. The designation D-type means the switching base was $\le D$ in the original proof, irrespective of whether the actual maximum threshold also involved Q.
 
| Original term and freeze | Still-unfrozen rough labels in the upper bound | Main bound |
| --- | --- | --- |
| Both lower products nonempty, second difference; freeze both switched rough products | None, because each proper label $f,g$ is in its frozen cofactor | $O_C(\ell^5 L^{-\sigma})$ |
| Both nonempty, mixed product-edge switch; freeze both proper rough labels | None | $O_C(\ell^5 L^{-\sigma-1})$ |
| Both nonempty, mixed D-type switch; freeze only the switched rough label | One side, costing at most $L^\nu$ | $O_C(\ell^4 L^{-\sigma-1+\nu})$ |
| Both nonempty, light–light term; freeze only $s,t$ | Both sides, at most $L^{2\nu}$ | $O_C(\ell^2 L^{-\sigma-1+2\nu})$ |
| Exactly one nonempty, heavy product-edge switch; both proper labels are frozen | None | $O_C(\ell^5 L^{-\sigma})$ |
| Exactly one nonempty, heavy D-type switch; freeze only its switched rough label | One side, at most $L^\nu$ | $O_C(\ell^4 L^{-\sigma+\nu})$ |
| Exactly one nonempty, light term; freeze only $s,t$ | Both sides, at most $L^{2\nu}$ | $O_C(\ell^2 L^{-\sigma+2\nu})$ |

Indeed in the first row the heavy marks give $L^2$, the sieve gives $T^{-2}$, the log strip gives $\ell^2/L$ and the other frozen rough product gives $\ell$, producing $\ell^5/L$ before the lower profiles. The mixed product row replaces one $L$ by a least-prime log already covered by the lower profile. The D-type rows omit the reciprocal cost $\ell$ of the entirely unfrozen rough part and use its stated multiplicity instead. The two-light row has no strip, both least-prime weights are covered in the lower profiles, and only $T^{-2}$ and the indicated rough multiplicity remain. With one empty side the analogous light term has one remaining heavy weight $L$, as in the exact single-switch proof. These computations keep the signs until the support conditions and the indicated labels have actually been identified; there is no signed estimate replaced by an unrestricted absolute divisor sum.

The bound for the nonempty–nonempty case follows because $\max(0,2\nu-1)\ge\nu-1$, and the one-empty row maximum is $2\nu$. Summing (5), the pointwise tail, and these main estimates proves (2), which remains valid on reflected hard intervals and for every admitted integer mask. In the both-nonempty case, for every fixed $C\ge2\log2$ the new threshold permits rough arity growing as a constant multiple of $\log\log N$, while the original fixed-$\kappa$ theorem allowed only bounded arity. Neither result treats arbitrary intermediate-factor interactions or supplies estimates for the full operator.
