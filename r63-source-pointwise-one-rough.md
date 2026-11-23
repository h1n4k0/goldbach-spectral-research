# Pointwise central cancellation when a squarefree leg has exactly one rough prime

Fix $0<\rho<1/2$ and a **fixed** $0<\kappa<1/4$. For every sufficiently large even $N$, put $L=\log N$, $B_L=1+\log L$, $I_0=[\rho N,(1-\rho)N]$, and take the unchanged original retuned thresholds

$$
 D=\left\lfloor \sqrt N\,e^{-20L/\log L}\right\rfloor,\qquad
 Q=\left\lfloor N\,e^{-20L/\log L}\right\rfloor .
$$

Let $\mathcal G_\kappa$ denote squarefree central units whose prime factors all lie in $[2,L]\cup[N^\kappa,N]$, with at least one prime in the second range. Let $\mathcal O_\kappa\subseteq\mathcal G_\kappa$ be the class with exactly one prime in the second range. No bound on the number of small primes is imposed, on either leg. In $\mathcal O_\kappa$ the optional prime case with no small factors has identically zero long mark. Let $\mathcal F_\kappa,\mathcal B,\mathcal H_\kappa,\mathcal U_\kappa$ and $\mathcal T_{\kappa,M}$ be the actual selections from [R60](r60-source-fixed-rough-all-arities-dickman.md) and [R62](r62-source-bounded-small-prime-slots.md), with the indicated $M$ fixed when used.

For hard $I\subseteq I_0$ let

$$
 R_N(\mathcal D,\mathcal E;I)=
 -\!\sum_{\substack{n+m=N,\ n\in I\cap\mathcal D,\ m\in I_0\cap\mathcal E\\(nm,N)=1}}
 \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
       \mu(d)\mu(e)\log(n/d)\log(m/e).
 \tag{1}
$$

This is the actual negative central sum alias, with both strict long tests and the strict curved product cutoff.

**Theorem (unconditional, pointwise).** For every such $N$, simultaneously for all hard $I$ and in both orders of the two legs, an $\mathcal O_\kappa$ leg against a partner $\mathcal E$ in the following table satisfies

$$
       |R_N|\ll_{\rho,\kappa,M}
       \mathfrak S(N)\bigl(|I|\,w_{\mathcal E}(N)+N^{1-\kappa/3}\bigr).
 \tag{2}
$$

- $\mathcal E=\mathcal F_\kappa,\mathcal B,\mathcal H_\kappa,\mathcal U_\kappa$: take $w_{\mathcal E}=B_L/L$.
- $\mathcal E=\mathcal T_{\kappa,M}$, for fixed $M$: take $w_{\mathcal E}=(B_L/L)(1+\log B_L)^M$.
- $\mathcal E=\mathcal G_\kappa$: take $w_{\mathcal E}=B_L^3/L$.
- $\mathcal E=\mathcal O_\kappa$: take $w_{\mathcal E}=(B_L/L)^2$.

In the last case, on the subblock where both small cofactors are $\le D$, both exact orbit sums can be carried out and the result is nonpositive, equal to the negative genuine count with the two small-prime logarithmic weights. The contribution where either small cofactor exceeds $D$ has absolute size $O_{\rho,\kappa}(N^{4/5})$. Constants involving $M$ are needed only in the fixed-$M$ row. There is no exceptional target set. This does not handle a pair of unrestricted hybrid legs with at least two rough primes each, intermediate prime factors, nonsquarefree legs, or Hypothesis S.

## 1. Exact signed complete orbits and a pointwise smooth tail

Write $n=ps$, where $p\ge N^\kappa$ is the only rough prime and $s$ is squarefree with all prime factors $\le L$. If $s=1$, the long mark is zero. For $1<s\le D$ we have $p\ge\rho N/D>\sqrt N$ for sufficiently large $N$. For each **actual** opposite $e>D$,

$$
      \max(D,Q/e)\le\sqrt N
$$

since $e\ge D+1>\sqrt N e^{-20L/\log L}$. Thus the only selected $n$-divisors are $pa$, $a\mid s$, and all are selected. Their signed sum is

$$
 \sum_{a\mid s}\mu(pa)\log(n/(pa))
       =-\sum_{a\mid s}\mu(a)\log(s/a)=-\Lambda(s).
 \tag{3}
$$

It vanishes for squarefree composite $s$ and equals $-\log s$ for prime $s$. This is exact for every $e$, without canceling separately inside a positive cutoff envelope.

For $s>D$ allow every divisor in the absolute bound. The first leg costs at most $2L\,\tau(s)$. Every partner in the theorem is either bounded-arity or has at most $\lfloor1/\kappa\rfloor$ rough slots and at most $\pi(L)$ distinct small primes. Its absolute mark is $O_\kappa(L\,2^{\pi(L)})$, hence $N^{o(1)}$, uniformly across its numerical values, by Chebyshev. For fixed $s$ there are at most $N/s$ possible $n$ and precisely one opposite integer for each. Rankin at exponent $1/2$ gives

$$
 \sum_{\substack{s>D,\ s\ {\rm squarefree}\\P^+(s)\le L}}\frac{\tau(s)}s
 \le D^{-1/2}\prod_{p\le L}(1+2/\sqrt p)
       \le D^{-1/2}\exp(O(\sqrt L))
       =N^{-1/4+o(1)} .
 \tag{4}
$$

Here $\tau$ is the divisor function; sum $p^{-1/2}$ over all integers if desired. Therefore this entire genuine tail is $O_{\rho,\kappa}(N^{4/5})$ for sufficiently large $N$, independently of $I$ and of the other leg's masks. If the partner is also $\mathcal O_\kappa$, apply (4) in both orientations and then use (3) in both slots. In general (3) reduces the retained marked first leg to $n=qp$ with two genuine primes, where $q=s\le L$ is the small prime and $p$ is the rough one. Its absolute surviving mark is $\log q$ and it is still an exact $N$-unit.

## 2. Two affine primes at a fixed target

On the opposite leg freeze its cofactor $h$ after removing its largest prime $v$, so that $m=hv$. Except when the entire leg has already canceled, $v\ge N^\kappa$ for every selection in the theorem: this is built in for the hybrid families, and for the old $\mathcal B$ family it follows from at most three prime factors and $m\ge\rho N$. Thus $h\le N^{1-\kappa}$. In a chosen partner family the factorization left in $h$ is uniquely sorted (and ordered definitions, if used, have only bounded rough multiplicity). Use a nonnegative bound $W(h)$ on the absolute partner long mark. It may incorporate the partner's original cofactor restrictions or any necessary projections of them. The choices and estimates are made below.

Keep the actual unit masks on frozen $q,h$. Necessarily $(q,h)=1$ on $qp+hv=N$, since a shared prime would divide $N$, and $(qh,N)=1$; pairs failing either test are omitted exactly. For fixed admissible $q,h$ take any integer solution $(p_0,v_0)$ and write the remaining lattice as

$$
        p=p_0+hk,\qquad v=v_0-qk .
 \tag{5}
$$

The exact physical condition $qp\in I$ restricts $k$ to an interval of length $H=|I|/(qh)$, with the same hard endpoint flags. The other physical condition and partner cuts can only decrease the number, but we keep the lower bounds $p,v\ge N^\kappa$ for sieve eligibility; $p\ge\rho N/L$ automatically on the first leg for large $N$.

Let $\nu(\ell)$ count the residues where the product of (5) vanishes modulo a prime $\ell$. If $\ell\mid qh$, just one form has unit slope and the other is a nonzero constant: this uses both coprimalities just imposed and $qp_0+hv_0=N$. Otherwise both slopes are units and their roots coincide precisely if $\ell\mid N$, since the determinant of the two rows of coefficients (slope, constant) is $h v_0+q p_0=N$. In particular $\nu(2)=1$ ($N$ even, $qh$ odd), and at no prime is $\nu(\ell)=\ell$. Write

$$
 \lambda^*(h)=\prod_{\ell\mid h,\ \ell>2}\frac{\ell-1}{\ell-2}.
$$

We prove the uniform upper bound on the genuine prime pairs for this frozen pair

$$
   \#\{(p,v)\}
      \ll_\kappa \frac{H\,\mathfrak S(N)}{L^2}
                  \lambda^*(q)\lambda^*(h)+N^{\kappa/2}.
 \tag{6}
$$

In particular this supplies an absolute endpoint error even when $H$ is very short.

Here is the elementary quadratic sieve proof, as in the affine count of [R41 §1](r41-source-unmasked-separated-cofactor-cells.md#1-full-torus-target-coefficient-unconditional-uniform-two-form-sieve). Set $Z=N^{\kappa/12}$ and $z=Z^\eta$, where $\eta>0$ is a sufficiently small absolute constant. Both primes exceed $z$. On squarefree $d$ supported on primes $\ell\le z$ put $g(d)=\prod_{\ell\mid d}\nu(\ell)/\ell$, $a(d)=\prod_{\ell\mid d}g(\ell)/(1-g(\ell))$. Let $\mathcal D_z$ be such $d\le Z$, closed under divisors, and $G=\sum_{\mathcal D_z}a(d)$. With weights $\lambda_d$ supported there and $\lambda_1=1$, the square of the divisor sum over the product (5) majorizes prime-pair eligibility. Counting each least-common-multiple residue class in the hard interval gives main quadratic form $\sum_{d,e}\lambda_d\lambda_e g([d,e])$ times $H$, and error at most a constant times $\sum_{d,e}|\lambda_d\lambda_e|\nu([d,e])$.

Write $y_l=\sum_{l\mid d}\lambda_d g(d)$. Since $1/g((d,e))=\sum_{l\mid(d,e)}1/a(l)$, the quadratic form is $\sum_l y_l^2/a(l)$. Choose $y_l=\mu(l)a(l)/G$ on $\mathcal D_z$, so inversion gives $\lambda_1=1$, form $1/G$ and $|\lambda_d|\le a(d)/g(d)\le d$. For the inequality, the absolute inversion sum is at most $a(d)G/G$ and $\nu(\ell)\le \ell-1$. There are at most $Z^2$ pairs, and each $\nu([d,e])\le Z^2$, so the error is $O(Z^6)$. The interval residue count has $O(1)$ error per residue for either convention on a hard endpoint.

The Euler product of all $a(d)$ on the primes $\ell\le z$, normalized to probability, has mean of $\log d$ at most $\sum_{\ell\le z}(2/\ell)\log\ell=O(\log z)$, since inclusion at $\ell$ has probability $g(\ell)$. Markov with $\eta$ small leaves at least half the mass at $d\le Z$. Consequently $G^{-1}\ll\prod_{\ell\le z}(1-\nu(\ell)/\ell)$. Factor out $\prod_{\ell\le z}(1-1/\ell)^2\ll_\kappa L^{-2}$. At $\ell=2$ the remaining factor is $2$; at odd $\nu(\ell)=2$ it is $1-1/(\ell-1)^2$. For odd $\nu(\ell)=1$ the ratio relative to that latter factor is $(\ell-1)/(\ell-2)$. The primes where this occurs are those dividing $Nqh$. The product of the ordinary $\nu(\ell)=2$ base factors omitted past $z$ is bounded away from zero; all extra factors for $N,q,h$ are at least one. Since $(qh,N)=1$, the resulting upper bound is $O(\mathfrak S(N)\lambda^*(q)\lambda^*(h))$. This proves (6), uniformly even when $q,h$ vary and $h$ contains many small prime factors. There is no assertion about primality from a local comparison.

## 3. Summing the pointwise upper bound

The contribution from (6) with actual first weight $\log q$ and opposite weight $W(h)$ is at most a constant times

$$
 \frac{|I|\mathfrak S(N)}{L^2}
   \left(\sum_{q\le L}\frac{\lambda^*(q)\log q}{q}\right)
   \left(\sum_{h}\frac{\lambda^*(h)W(h)}h\right)
  +N^{\kappa/2}
   \left(\sum_{q\le L}\log q\right)
   \left(\sum_{h\le N^{1-\kappa}}W(h)\right).
 \tag{7}
$$

The sums are positive upper envelopes after (6) has been proved on the exact admissible frozen masks; the $q$ sums can be restricted to odd primes since 2 divides $N$. Its first reciprocal sum is $O(B_L)$ by $\lambda^*(q)\le2$ and Chebyshev.

For $\mathcal G_\kappa$, use $W(h)\ll_\kappa L\,\tau(s(h))$ where $s(h)$ is the small-prime part of the squarefree $h$. At most $\lfloor1/\kappa\rfloor$ additional rough primes contribute only a fixed factor to the divisor mark. Their weighted reciprocal mass is bounded by fixed-$\kappa$ prime Mertens, including their factors $\lambda^*(\ell)$. On the small side do **not** replace $\lambda^*(h)$ by a fixed constant when the number of slots is unbounded. Instead use

$$
 \sum_h\frac{\lambda^*(h)W(h)}h
       \ll_{\kappa} L\prod_{3\le p\le L}
                  \left(1+\frac{2\lambda^*(p)}p\right)
       \ll_\kappa L B_L^2 ,
 \tag{8}
$$

since $\lambda^*(p)=1+O(1/p)$. For $\mathcal T_{\kappa,M}$ the same sum is $\ll_{\kappa,M} L(1+\log B_L)^M$, summing only the first $M$ small slots with $\sum_{p\le L}1/p\ll 1+\log B_L$. For $\mathcal F_\kappa,\mathcal H_\kappa$ it is $O_\kappa(L)$ with no small slots. After both (3) and (4) are applied in the $\mathcal O_\kappa$ self pairing, $h$ is another small prime and $W(h)=\log h$, giving $O(B_L)$ for this reciprocal sum. On that retained pair block both giant primes pass the curved threshold with every admitted divisor of the other leg, so the external sign gives exactly the negative two-logarithm count as stated.

The $\mathcal B$ partner also gives $O_\rho(L)$ for this sum, but needs its geometric restrictions. Delete its prime and admissible-giant/composite cases by the exact cancellation (3), which requires only $s'\le D$ and not any small-slot assumption. For its other types, in the terminology of [R58](r58-source-central-three-factor-first-order.md), use $W(h)=\log h$ for old type 2 (a single cofactor prime $\le D$), and $W(h)=O(L)$ for types $3,H_1,H_2,B$. The reciprocal sum at type 2 is $O(L)$ by $\sum_{p\le D}(\log p)/p\ll L$, and at $B$ it is $O(L)$ since the frozen high prime is between $D$ and $\sqrt N$. For three-factor cases sort $a\le b\le v$, freezing $h=ab$. Any repeated labelling after sorting is bounded since there are at most three slots. We check bounded reciprocal mass of $a,b$ in the envelope of each class:

- Type 3 has $v\le D$, so $\rho N/(aD)\le b\le\sqrt{N/a}$. If $a\le N^{1/4}$ the $b$ scale is at least $\rho N^{1/4}$, and this interval has log-width at most $(\log a)/2+O_\rho(1)$. Partition into unit-log intervals, each of reciprocal prime mass $O_\rho(1/L)$ by Chebyshev on the enveloping fixed-ratio interval. Summing the resulting $(1+\log a)/(a L)$ over primes gives $O_\rho(1)$. If $a>N^{1/4}$ both axes have bounded polynomial-range reciprocal mass.
- Type $H_1$ has $v>D$ and $b\le D$ with $ab>D$ (otherwise the opposite orbit has already canceled). When $a\le N^{1/4}$, the resulting $D/a<b\le D$ has width at most $\log a$ and minimum at least $N^{1/5}$ for all sufficiently large $N$. Use the same bound. For $a>N^{1/4}$ again both reciprocal masses are bounded.
- Type $H_2$ has $b,v>D$, $a\le N/D^2$. The frozen $b$ lies in $(D,\sqrt N]$, with reciprocal prime mass $O(1/\log L)$ by the same fixed-ratio estimates or prime Mertens. The entire $a$ reciprocal prime mass is $O(1+\log L)$. Their product is bounded.

All frozen prime special factors are bounded on this fixed-arity $\mathcal B$ family. Thus use its $O_\rho(L)$ bound in (7). The $\mathcal U_\kappa$ union is covered by its disjoint $\mathcal B$ and $\mathcal H_\kappa$ selections.

Finally, the most general error sum in (7) satisfies

$$
 \sum_{h\le Y} W(h)
 \ll_\kappa L\sum_{h\le Y}
      \sum_{\substack{a\mid h,\ a\ {\rm squarefree}\\P^+(a)\le L}}1
 \ll_\kappa L Y\prod_{p\le L}(1+1/p)
 \ll_\kappa L Y B_L,\qquad Y=N^{1-\kappa}.
$$

The inner sum includes $a=1$. This holds after enlargement even for unbounded small arity and dominates the other families' error sums. The elementary bound $\sum_{q\le L}\log q=O(L)$ makes the full lattice error $O_\kappa(N^{1-\kappa/2}L^2 B_L)=O_\kappa(N^{1-\kappa/3})$. Combined with the power-small original tail (4), all the terms in (7) give (2); $\mathfrak S(N)$ is bounded below on even targets. The reflected order replaces $I$ by the hard $N-I$ and preserves its length by exact symmetry of (1). No analytic exceptional set has been introduced. The arithmetic-to-operator reduction, if used, retains its separate assumptions and does not gain an estimate for the unaddressed hybrid-by-hybrid block.
