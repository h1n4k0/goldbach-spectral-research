# Local divisors and numerator Parseval permit much smaller largest primes

**Scope.** Keep the genuine parity and small-prime-count selectors of the [signed Euler slot estimate](r70-spectral-signed-shift-euler-slots.md): $U=\sqrt L$, $G=\exp U$, true squarefree $m$, odd total parity with at most $\lfloor\log U\rfloor$ primes $\le G$, or even total parity with at most $\lfloor(2/5)\log U\rfloor$. The fixed-power largest-prime condition can be weakened from $P^+(m)>N^{1/2-\delta}$, $\delta<1/4$, to

$$
 P^+(m)>N^\kappa.
 \tag{1}
$$

For the true full arithmetic bound this works for any fixed $0<\kappa<1/2$. For the genuine minor, at the unchanged major denominator $Q=N^{1/1000}$, it works for every fixed $1/250<\kappa<1/2$ under the same historical Dirichlet GRH assumption for the prime progression calculation. For example $\kappa=1/200$ is allowed. No larger small-prime count, partner with $P^+(m)\le N^\kappa$, or unrestricted spectral norm is estimated.

Keep the notation of the signed Euler estimate, including $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, $V=[N/3,2N]$ and the actual mixed $M_>$ on squarefree partners. Let $A(m)$ be $M_>(m)$ restricted to $V$, (1), and one of the two stated parity-and-count masks or their union. With the same actual $I$, $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$, bounded variation weight $\omega$, and polynomials $P_{I,\omega}$ and $\widehat A$, we prove

$$
\begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
       &\ll \Sigma(N)|I|\mathcal B/L+N^{1-c},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)
                                  e(-N\theta)\,d\theta\right|
       &\ll \Sigma(N)|I|\mathcal B/L+N^{1-c}.
\end{split}
 \tag{2}
$$

Here $\mathcal B=L^{-1/20}$ for odd only and $L^{-1/100}$ otherwise, as in the signed Euler estimate. In the first line one may take $c=\min(10^{-4},\kappa/10)$; in the conditional second line take $c=\min(10^{-4},(\kappa-1/250)/10)$ (we can also take that exponent in the first). Constants may depend on the fixed $\kappa,B,B_0$ and left weight bounds. The original Hardy normalization is $L/N$.

## 1. Each divisor floor uses its own cutoff scale

Extract the true largest prime $p$ from squarefree $m=pk$, as before, with $p>\max(P^+(k),N^\kappa)$. The proof that $k\le D$ contributes zero is unchanged: then $p=x/k\ge N/(3D)>D,H_0$ and the exact product and low mixed gates eliminate it. On all remaining support,

$$
 D<k\le 2N^{1-\kappa},\qquad T_1=k/D,\quad T_2=Dk/x,\quad x=kp.
 \tag{3}
$$

Both true small-prime count selectors are constant at fixed $k$ because $p>G$ eventually. Write $k=bv$ with the product $b$ of its actual small primes and strictly $G$-rough $v$; $b\le G^{\log U}=N^{o(1)}$. The parity identities for $F_0,F_1$, the two factors of the sharp product for $-\Xi_D$, as well as $M_>=-\Xi_D-M_\le$, are unchanged. The prime-$k$ case still forces $k<\sqrt x$ and the near-unit arithmetic border still has polylogarithmic cutoffs. The real weight $F_k(x)$ in the unique-largest-prime expansion of $A$ retains supremum and variation $O(\tau_4(k))$: the original sharp product has at most $\tau(k)^2\le\tau_4(k)$ step-monotone terms on squarefree $k$, and the low mixed sums with or without $p$ in the LCM have at most $O(\tau_4(k))$ such terms. In the latter case the low signed labels are polylogarithmic, so they cannot contain $p$. All variation includes the support jumps and the actual prime-count and parity selectors, constant at fixed $k$.

The cutoff model and its hard endpoint envelopes in the signed Euler proof use arithmetic cells $K<k\le K'$ of log width $w\le\eta=L^{-10}$ and fixed physical cells of width at most $\eta$. On each such cell, every short divisor label on $v$ before a rough square is formed is at most

$$
 Z_K=10K/D.
 \tag{4}
$$

Indeed $T_1\le K'/D$, $T_2/T_1=D^2/x<1$ for large $N$, the comparisons move by $O(\eta)$ in log, and translating by a divisor of $b$ can only lower the cutoff. The integrated endpoint brackets have the same property. In contrast, the size of the rough cell variable is $K/b$.

In the reciprocal rough-square transfer, each reciprocal count for an LCM of a pair of such labels has floor cost $N^{o(1)}b/K$, by the same Bonferroni inclusion/exclusion at depth $\asymp L_2^2$, since $G^{O(L_2^2)}=N^{o(1)}$. To spell out that floor, a squarefree exclusion modulus $d$ multiplies the fixed LCM, and the reciprocal count of its multiples on $K/b<v\le K'/b$ is $w/(d\,[r,t])+O(b/K)$; the number of admitted exclusion subsets is subpower. Use (4) to sum the endpoints before taking the final Cauchy. Including all polynomial-in-$L$ short weights, the total floor per square and cell is

$$
 O\!\left(Z_K^2(b/K)N^{o(1)}\right)
       \ll bK D^{-2}N^{o(1)}
       \ll N^{-\kappa+o(1)} .
 \tag{5}
$$

The multiplicative main factor is still $w\prod_{\ell\le G}(1-1/\ell)\mathcal E_G$, with the exact signed divisor LCM square from the preceding proof; the arbitrary fixed inverse-log Bonferroni remainder is also unchanged, since all global labels are at most $Z=10N^{1/2-\kappa}L^B$ and their reciprocal LCM sum is $L^{O(1)}$. Thus (5) replaces the earlier use of the global maximum label together with the minimum cell scale. A continuous arithmetic-cutoff average retains this floor after division by $w$, as that floor is uniform pointwise inside the averaged cell. The number of cells is still polylogarithmic and $\sum_b1/b\ll U$. Thus (5) remains a power saving even after all such sums and the final Cauchy, where it contributes $N^{-\kappa/2+o(1)}$ to the reciprocal product upper bound.

All signed Euler integrals and estimates for narrow unsigned boundary counts are unchanged, because the proof only needs $\log Z=O(L)$ in its outer rough harmonic sum and in the harmless extra gcd Euler factors, and the total log cofactor width is $O(L)$. The low mixed subtraction still has the true two alternatives $h\mid k$ and $h=pr$: the bounded rough factor is now at most this global $Z$, while its complementary log interval has width $O(L_2)$ as before. The split $2^{\omega(b)}3^{\#\{\ell\mid b:\ell\le H_0/D\}}$ is identical. Thus on each physical cell there is a reciprocal majorant for the actual coefficient, including the multiplier $k/\varphi(k)$, of total size $O(\mathcal B+N^{-\kappa/2+o(1)})$. The individual majorants are of subpower size by the divisor bound. For the even $t=0$ contribution, the [rough-kernel estimate](r69-spectral-rough-reciprocal-kernel-sampling.md) used its auxiliary true least-prime split rather than a full integrated cutoff at $b=1$. That arithmetic proof also transfers with (4)–(5). On least primes $\ell\in(\exp U,\exp(L^{9/10})]$ its cell variable is $k/\ell$, so the same floor uses the subpower factor $\ell$ in place of $b$; the Bonferroni exclusion count remains subpower up to $\log\ell=L^{9/10}$. The marked cell widths and the reciprocal least-prime sum are unchanged and give $O(\sqrt{L_2/U})$. For the higher least-prime tail use the arithmetic cofactor calculation of the [polynomial rough deletion](r68-spectral-polynomial-largest-rough-mixed-minor.md) at roughness $\exp(L^{9/10})$: the same local labels (4) and floors (5) apply without a least-prime split, and its rough primitive, narrow shell and integrated estimates need only $\log Z=O(L)$ and total cofactor log width $O(L)$. Its reciprocal bound $O(L^{-2/5}\sqrt{L_2}+L_2^4/L^{9/10}+L_2^2/L)$ is smaller. Only those arithmetic cofactor bounds are invoked here, not their larger-$P^+$ prime comparison. This argument retains the true $p$ support in using the majorant; only the nonnegative cutoff energies were enlarged.

For the true arithmetic upper bound, use the [same two-root fundamental upper sieve](r66-spectral-above-bv-strip-deletions.md#2-above-level-giant-partners-a-true-full-arithmetic-upper-bound) on the actual $p,N-kp$. Set the sieving height to $N^{\kappa/100}$ and the level to $N^{\kappa/4}$, retaining the ratio of their logarithms equal to 25. Both forms exceed the sieving height for sufficiently large $N$. On genuine prime pairs $(k,N)=1$, since $n=N-kp$ is prime strictly between $N/2$ and $N$. The CRT two-root count for this exact interval is unchanged and the positive sieve main term at fixed $k$ is
$O(\Sigma(N)|I_{\rm cell}|(k/\varphi(k))/(kL^2))$, with the constant allowed to depend on $\kappa$. The absolute remainder is $N^{\kappa/4+o(1)}$ by the same divisor sum up to the sieve level. The number of candidate cofactors is $O(N^{1-\kappa})$, and summing the subpower coefficient bounds, physical cells and left log costs a total floor $N^{1-3\kappa/4+o(1)}$. The physical interval lengths add exactly to $|I|$. This proves the unconditional first line of (2).

## 2. Character and numerator Parseval on the unchanged arcs

Write $\theta=a/q+\nu$, with $q\le Q$, $(a,q)=1$ and $|\nu|\le2Q/N$. We estimate the integrated major error using the left **main term**, not the product of two suprema on the whole arc set.

For fixed $k$ and $v\in(\mathbb Z/q\mathbb Z)^\times$, let $E_k(v;\nu)$ be the error in replacing the actual prime progression sum weighted by $F_k(kp)e(\nu kp)$ in class $v$ by $1/\varphi(q)$ times its real integral with prime density $1/\log p$. The exact $F_k(x)$ still includes $p>\max(P^+(k),N^\kappa)$ and all other true gates. Because $\kappa>1/250$, every $p$ on the right is $>Q$, so no prime dividing $q$ enters. On the left the prime position is also $>Q$.

The underlying character form of the historical prime GRH estimate is
$\psi(Y,\chi)-\mathbf1_{\chi=\chi_0}Y\ll \sqrt Y(\log Y)(\log(qY))$ for $Y\ge2$ and $\chi\bmod q$ (see [Montgomery–Vaughan, Theorem 13.7](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/conditional-estimates/98117860E24F0BB5605B4DF379A32190)). This uses Dirichlet GRH at conductors dividing $q$, including the zeta case for the principal character. Removing prime powers and partial summation for unweighted primes preserve a bound $O(\sqrt Y L^{O(1)})$ on the relevant polynomial ranges. Weighted by the true $F_k$ and the slow phase, the error for each character is at most
$O((1+N|\nu|)\tau_4(k)\sqrt{N/k}L^{O(1)})$, because the prime variable is $\le 2N/k$ and the phase has variation $O(N|\nu|)$. Character orthogonality followed by Parseval therefore gives

$$
 \sum_{v\bmod q}^* |E_k(v;\nu)|^2
       \ll (1+N|\nu|)^2\tau_4(k)^2 (N/k)L^{O(1)}.
 \tag{6}
$$

Indeed $E_k(v;\nu)$ is $1/\varphi(q)$ times the character expansion of the character errors, so the squared sum is $1/\varphi(q)$ times the character squared sum. This has no extra factor $q$.

Now let $g=(k,q)$ and extend $E_k(v;\nu)$ by zero on the nonunits. In the numerator $a$, the map $a\mapsto ak\bmod q$ has exact multiplicity $g$ on its image. The full residue Fourier Parseval identity and positivity give

$$
 \sum_{a\bmod q}\left|\sum_{v\bmod q}E_k(v;\nu)e(akv/q)\right|^2
       \le qg\sum_{v\bmod q}|E_k(v;\nu)|^2 .
 \tag{7}
$$

Taking the $\ell^1$ norm in numerators by Cauchy and then summing $k$ gives the genuine right polynomial error $E_R(a,q,\nu)$ with

$$
 \sum_{a\bmod q}^* |E_R(a,q,\nu)|
    \ll_\epsilon q^{1+\epsilon}(1+N|\nu|)
                                  N^{1-\kappa/2+\epsilon}.
 \tag{8}
$$

Explicitly, for each $k$ the $\ell^1$ norm is at most $q\sqrt{g}$ times the square root in (6), and

$$
 \sum_{k\le K_1}\frac{\sqrt{(k,q)}}{\sqrt k}
 \le \sum_{d\mid q}\sqrt d\sum_{\substack{k\le K_1\\d\mid k}} k^{-1/2}
 \ll \sqrt{K_1}\sum_{d\mid q}d^{-1/2}
 \ll_\epsilon \sqrt{K_1}q^\epsilon,\qquad K_1=2N^{1-\kappa}.
 \tag{9}
$$

The divisor factor $\tau_4(k)$ and log powers are absorbed in the arbitrary $N^\epsilon$.

The exact left prime main term is $\mu(q)V_I(\nu)/\varphi(q)$ with $V_I(\nu)=\int_I\omega(u)e(\nu u)\,du$. By bounded variation, $|V_I(\nu)|\ll\min(N,1/|\nu|)$, hence

$$
 \int_{|\nu|\le2Q/N}|V_I(\nu)|(1+N|\nu|)\,d\nu\ll Q.
 \tag{10}
$$

Pairing (8) only with that left main term and summing $q$ therefore costs

$$
 O_\epsilon\bigl(Q^{2+\epsilon}N^{1-\kappa/2+\epsilon}\bigr),
 \tag{11}
$$

after enlarging the arbitrary epsilon in $q$ if necessary and using $q/\varphi(q)\ll_\epsilon q^\epsilon$. For the other error write the product difference as left error times actual right plus left main times right error. The left pointwise error is $O(q(1+N|\nu|)\sqrt N L^{O(1)})$ by the old prime AP bound; the actual right is $N^{1+o(1)}$ in supremum by the divisor bound. The total arc measure $O(Q^3/N)$ bounds this first integrated error by $N^{1/2+o(1)}Q^5$. No product of two new error bounds is needed. With $Q=N^{1/1000}$ the exponent in (11) is below 1 when $\kappa>1/250$ and $\epsilon$ is chosen small in terms of the difference. These estimates use the original arcs and actual hard weights without shrinking the major set.

## 3. Complete the real major density and subtract

The right main on a reduced numerator is still the real Fourier density obtained by summing, at fixed $k$,

$$
 \frac{c_q(k)}{\varphi(q)}
       \frac{F_k(x)}{k\log(x/k)} .
 \tag{12}
$$

This is the exact sum of its additive factors over unit $p$ classes. The bound $\log(x/k)\gg_\kappa L$ and the $O(\tau_4(k))$ variation give the unchanged major occupation estimate $O_\kappa(L^4 C^{\omega(q)}/q)$ for its supremum and variation, since $k\le2N^{1-\kappa}\le N$ eventually. For squarefree $q$, each prime dividing $q$ is either unoccupied in $k$, gaining $O(1/p)$ from $|c_q(k)|/\varphi(q)$, or occupied and gains $O(1/p)$ by the reciprocal $\tau_4(k)/k$ sum. This is exactly the occupation calculation of the [completed giant major](r66-spectral-above-bv-strip-deletions.md#3-the-same-upper-scale-for-the-actual-giant-major-arcs), now with its larger but still at most $N$ cofactor range.

It follows that extending the retained real Fourier convolutions beyond $|\nu|\le2Q/N$ costs $O(NQ^{-1} L^{O(1)})$, by the bounded variations on both legs, as in the [pointwise completion argument](r64-spectral-pointwise-major-central-bridge.md). The omitted Ramanujan terms are likewise $O_\epsilon(N^{1+\epsilon}Q^{-1/4})$: the left main restricts to squarefree $q$, and its $c_q(N)$ numerator is bounded by $(q,N)$, permitting the same $Q^{-1/4}$ Euler product with a factor $N^\epsilon$. For example $\epsilon=1/20000$ absorbs the logarithms and leaves both errors within $N^{1-10^{-4}}$.

The fully completed local factor is zero for $(k,N)>1$, otherwise $O(\Sigma(N)k/\varphi(k))$, as before. Section 1's true reciprocal majorant and $\log(x/k)\gg_\kappa L$ thus bound the completed major coefficient by the right side of (2), including the reciprocal power floor, uniformly on the exact central $I$. All major errors above fit the stated $c>0$. Subtract this genuine major integral from the actual full coefficient in (2) to obtain the minor estimate. The smaller largest-prime sector in (1) has been genuinely enlarged, but its complementary count and largest-prime ranges remain unresolved.
