# A pointwise middle-arity sector at the true subpower rough floor

Use the exact signed central sum, squarefree units, independent outer masks and original hard $I\subseteq I_0=[\rho N,(1-\rho)N]$ of the [retagged subpower-floor theorem](r68-source-retagged-subpower-rough-floor.md). Thus $L=\log N$, $\ell=\log L$, $T=L/\ell$, $D=\lfloor\sqrt N e^{-20T}\rfloor$, $Q=\lfloor N e^{-20T}\rfloor$, and $n=su,\ m=tv$ with nonempty lower products $s,t$ in the two respective genuine ranges

$$
     [\exp(c_iT/\ell^{a_i}),\exp(d_iT)],
            \qquad 0<c_i<d_i,\quad a_i\ge0
$$

for fixed constants. In particular $a_i=0$ gives the original higher sparse bands on **both** sides. The true nonempty rough parts have every prime $\ge Y=\exp(CT)$ with $C>\max(d_1,d_2)$ fixed. There is no original cap on the lower products, no proper-divisor gap, and **no total rough arity cap**.

Fix $0<\theta_i<1$ and $E_i>0$, and put

$$
 \varepsilon=1/64,\qquad
 J=\left\lfloor\frac{\log\ell}{\log\log\ell}\right\rfloor,\qquad
 V_i=\exp(E_i T\ell^{\theta_i}),\qquad
 Y_*=\exp(\varepsilon L/(J+1)).
$$

For large $N$ these satisfy $Y<V_i<Y_*$. The actual outer mask is that in slot $i$ there are at most $J$ rough prime factors in $(V_i,Y_*)$. There are no restrictions on the number of rough primes in the full band $[Y,V_i]$ or in $[Y_*,N]$. In particular the first of those two bands can itself supply a total arity comparable to $\log\ell$, beyond the smaller bound of the retagged theorem.

**Theorem (unconditional, pointwise).** Suppose

$$
       \sigma=1-2(a_1+a_2+\theta_1+\theta_2)>0 .
$$

For every fixed $A>0$ and $0<\xi<\sigma$, all sufficiently large even $N$, and all admitted hard intervals and integer masks, the true signed sum

$$
 R_N(I)=-
 \sum_{\substack{n+m=N,\ n\in I,\ m\in I_0\\
                   (nm,N)=1,\ n,m\ {\rm selected}}}
   \ \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
                   \mu(d)\mu(e)\log(n/d)\log(m/e)
$$

satisfies

$$
    |R_N(I)|\ll
          \mathfrak S(N)\bigl(|I|\ell^{-\sigma+\xi}+NL^{-A}\bigr).
 \tag{1}
$$

Constants may depend on the fixed parameters. The $J$ condition allows a slowly growing number of upper intermediate primes; its complement in the general middle-arity range is not controlled here. The claim is neither a first-moment lift nor Hypothesis S.

## 1. Remove the true very-high tail and regroup the factors

Use the [very-high-arity tail theorem](r69-source-very-high-arity-rough-tail.md) with $\beta=2$ on these same operands and outer masks. It removes those pairs for which either original rough arity reaches the explicit threshold $3\lceil H_2\log\ell\rceil$, with contribution $O(\mathfrak S(N)(|I|\ell^{-2}+NL^{-A}))$. This is not a new upper cap on the stated sector. On the remaining pairs both original rough arities are $O(\log\ell)$ with a fixed constant. The original lower products can be truncated at $s,t\le N^\varepsilon$ at $O_A(NL^{-A})$ as in §1 of that theorem: squarefree lower squared profiles have factors $1+4/p$, and Rankin at $\lambda/T$ for fixed sufficiently large $\lambda$ beats the absolute log and label weights by $L^{-\varepsilon\lambda}$ in the squared profile, followed by Cauchy on the genuine sum line. Alternatively one may make this lower truncation first; the original rough label bound is already $2^{\ell/C}$.

Write $u=w_1 w'_1 u_*$, where $w_1$ is the entire product of true rough primes in $[Y,V_1]$, $w'_1$ the true product of at most $J$ primes in $(V_1,Y_*)$, and $u_*$ the remaining product. Similarly split $v=w_2 w'_2 v_*$. After the very-high tail removal,

$$
   \log w_i=O(T\ell^{\theta_i}\log\ell)=o(L),\qquad
   w'_i\le Y_*^J<N^\varepsilon .
$$

Thus both new lower products $S=s w_1 w'_1$, $U=t w_2 w'_2$ are at most $N^{3\varepsilon}$; their remaining rough parts $u_*,v_*$ are $>\sqrt N$ and have all primes $\ge Y_*$. These are exact reorganizations of the same squarefree integers, not replacements of any divisor or its sign. The original lower ranges are below $Y$, so the least prime of either new lower product is still in its **old** lower product and its logarithm is still $O(T)$. The new lower divisors are allowed to range over every divisor of the new larger factors in the exact rearrangement, including the moved primes. The count condition on exceptional upper intermediate primes is used as stated, not substituted by an entropy bound on the labels of the divisor sum.

## 2. Reciprocal profiles with the complete low rough bands

Use $\lambda^*(w)=\prod_{p\mid w,\ p>2}(p-1)/(p-2)$. The original lower profile of weight $\tau(s)\lambda^*(s)/s$ costs $O(\ell^{2a_i})$. The complete moved low band $[Y,V_i]$ contributes the additional product $\prod_{Y\le p\le V_i}(1+2\lambda^*(p)/p)=O(\ell^{2\theta_i})$ by Mertens, without an arity cut on that band in this positive upper profile. For the exceptional band $M_i=\sum_{V_i<p<Y_*}2\lambda^*(p)/p=O(\log\ell)$, so the profile of products with at most $J$ such primes is at most $\sum_{j\le J}M_i^j/j!$. This is $\ell^{o(1)}$: majorize $M_i$ by $C_0\log\ell$ with fixed $C_0>0$, which is above $J$ for large $N$, and use

$$
  \log\!\left(\sum_{j\le J}M_i^j/j!\right)
   \le \log(J+1)+J\log\!\left(\frac{e C_0\log\ell}J\right)
   =o(\log\ell).
$$

The factorial comes from ordered tuples of distinct primes. The two full lower profiles under exact retagging therefore cost jointly

$$
                 O\!\left(\ell^{2(a_1+a_2+\theta_1+\theta_2)+o(1)}\right).
 \tag{2}
$$

A least-prime mark on either costs at most an extra $O(T)$, from the original lower component. All profile relaxations here are positive upper bounds.

Each retained rough part has at most $(J+1)/\varepsilon$ prime factors by its true cutoff $Y_*$. Hence its divisor-label multiplicity is $\exp(O(J+1))=\ell^{o(1)}$. Its unrestricted rough reciprocal profile, counting all squarefree products of primes in $[Y_*,N]$, is $O(J+1)$ by Mertens. For a nonempty rough product in a log strip of width $W$, freeze all but one prime and overcount all choices: the last prime costs $O((1+W)/\log Y_*)$ by Chebyshev, and the frozen products cost $O(J+1)$ as just noted. This gives $O((J+1)^2(1+W)/L)$. The rough factors in $\lambda^*$ are bounded since their number is $O(J+1)$ and their primes are $\ge Y_*$.

## 3. Exact switches, one-sided freezing, and the polynomial error

Use the exact double least-prime switch of the [no-gap pointwise theorem](r68-source-two-higher-bands-no-divisor-gap.md), now on the actual lower products $S,U$ from §1. It is the same four terms of the original signed divisor sum because the retagged factors are disjoint and all are squarefree. Let $a=P^-(S)$ and $c\mid S/a$; for a first-side switched rough label $f$ and actual opposite $E>D$, its exact condition is

$$
       cf\le \max(D,Q/E)<a c f.
$$

As $D\le\max(D,Q/E)\le\sqrt N$ for integral $E>D$, the genuine support satisfies $D/(a c)<f\le\sqrt N/c$. Its log width is $20T+\log a+o(1)=O(T)$ irrespective of the opposite label, and $f$ is proper and nonempty since $S<D$ and $u_*>\sqrt N$. A nonzero second difference permits this first-side strip; a mixed term uses the strip on its heavy side. No product cutoff is replaced before the exact support is obtained.

Freeze $(h,k)=(Sf,U)$ on the first-side switch, $(S,Ug)$ on a second-side switch, or $(S,U)$ for the two-light term. The two remaining affine products are genuine nonempty rough products and have no prime factors below $Y_*$. For all these actual freezes,

$$
                    hk\le N^{1/2+6\varepsilon}=N^{1-\omega},
                    \qquad \omega=1/2-6\varepsilon>0.
$$

The [affine rough-integer sieve](r65-source-pointwise-rough-complements.md) is legal at $Z=N^{\omega/24}$ and $z=\exp(\eta\varepsilon L/(J+1))$ with fixed $0<\eta<\min(1,\eta_0\omega/(24\varepsilon))$, where $\eta_0$ is its small absolute constant. Thus $z<Y_*$ and $\log z/\log Z<\eta_0$. The true coprimalities $(h,k)=(hk,N)=1$ give its exact determinant and ordinary local root weights. The main upper count is

$$
 O\!\left(
      \frac{\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)}{hk}
              \frac{(J+1)^2}{L^2}\right)
$$

and the hard-floor error is $O(Z^6)=O(N^{\omega/4})$ per frozen pair. There are $O(N^{1-\omega}L)$ pairs, with unique factor splits at the disjoint prime ranges. The reclassified lower multiplicities are $N^{o(1)}$ (split the factors of $S,U\le N^{3\varepsilon}$ at $\sqrt L$); additional omitted rough labels cost $\ell^{o(1)}$ and absolute log weights at most $L^2$. Thus the summed floor error is $O(N^{1-3\omega/4+o(1)})=O_A(NL^{-A})$, irrespective of hard interval length.

For the two-heavy second difference, the weights are $O(L^2)$ and cancel the sieve denominator $L^{-2}$. The one true strip costs $O((J+1)^2T/L)$ in the rough reciprocal profile, and the single omitted rough label costs $\ell^{o(1)}$. Formula (2) and $(J+1)^4=\ell^{o(1)}$ give the main coefficient $\ell^{-\sigma+o(1)}$ times $\mathfrak S(N)|I|$. Each heavy–light term pays one less $L$ in exchange for $O(T)$, and the two-light term uses no strip but two $O(T)$ logs and at most $\ell^{o(1)}$ omitted-label multiplicity. Thus these terms cost at most $\ell^{-\sigma-1+o(1)}$ at the same scale. All coprimalities and masks were used at the actual frozen pair before the corresponding positive upper enlargements. Together with the true tails, this proves (1), absorbing subpowers of $\ell$ by the fixed $\xi$.

There is a nonzero actual example strictly in the prior middle-arity gap. Take $a_i=0$ and band constants $c_i=1,d_i=2,C=3$, with for example both $\theta_i=.1$. At external scale $X$ choose one original interior higher lower prime on each side and $\lfloor2\log\ell_X\rfloor$ distinct true rough primes per side in narrow relative windows near $\exp(4 T_X)$, with all factors distinct. These are in the complete low rough bands, with no exceptional factors needed. Denote their products with the two original lower primes by $S,U$. Take two further primes $f,F$ per side (or $g,G$) so $Sf,Ug$ are each near $\sqrt{2Q_X}$ and $SfF,UgG$ near $X/2$. Here $\log S,\log U=o(\log X)$, so the PNT supplies the primes in those narrow proportional windows. The resulting $N$ is even with genuine central units, the moving scales preserve all masks, and original rough arities are $\sim2\log\ell$ on both sides, beyond the admitted R68 retagged cap and below the R69 cutoff. Then $F,G>\sqrt N$ and the two maximum labels have product strictly between $Q_N$ and $3Q_N$, each above D. All complete lower orbits involving $F,G$ cancel because $S,U$ are composite; among the remaining $f,g$ labels, omitting any lower prime reduces the product by more than three. Only the two maximum proper labels contribute, with equal parity and actual summand $-\log F\log G$. This witnesses the genuine sector; it does not give an aggregate lower bound.
