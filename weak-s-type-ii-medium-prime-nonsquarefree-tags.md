# A nonsquarefree tagged slice of the balanced medium-prime remainder

Let $N=2^j$, $X=\sqrt N$, $L=\log N$, and keep the exact balanced box

$$
 I=[.740X,.745X],\qquad J=[.715X,.720X],\qquad D=[.445X,.450X].
$$

Use the same genuine weight $w(v)=\sum_{N^{.024}<p\le N^{.2499},\,p\mid v}\log p$, with $p$ prime, as in [the medium-prime remainder](weak-s-type-ii-medium-prime-character-shells.md). Put $S=N^{.002}$, and let $T(v)$ indicate that a prime $s\in[S,2S]$ divides $v$. Define the exact signed sum

$$
 Z=\sum_{\substack{u\in I,\ v\in J,\ d\in D\\
    u,v,d\ {\rm odd},\ uv\equiv N\bmod d}}
       \mu(u)\mu(d)\mu^2(N-uv)\,[1-\mu^2(v)]\,T(v)\,w(v).
$$

It has the same sharp physical cuts: $N/2<uv<9N/16$, $k=(N-uv)/d>\sqrt N$ when integral, and oddness is the exact unit condition. Then

$$
 |Z|\ll N L^{-5}\quad\text{under global Dirichlet GRH},
 \qquad
 \sum_{\text{same tuples}}|\text{summand of }Z|\asymp N
       \quad\text{unconditionally}. \tag{1}
$$

The signed estimate is uniform for arbitrary subintervals of the stated $I,J,D$; the unsigned lower bound is for the full boxes. This removes an occupied portion of the actual nonsquarefree $v$ remainder. It is disjoint from the earlier [tagged result for squarefree $v$](weak-s-type-ii-medium-prime-tagged-slice.md). It transfers prime factors in the opposite direction, placing the nonsquarefree test and the full medium-prime weight on the short leg. It does not control the untagged nonsquarefree portion, the entire balanced remainder, or weak S.

## 1. From a true union to finitely many signed transfer sums

For a fixed $d,u$ there is at most one admissible $v$, and for a fixed $d,v$ at most one $u$, as the other interval is shorter than $d$. If the fixed variable shares a factor with odd $d$, there are no solutions; otherwise the congruence imposes a unique residue on the other variable. Let $\omega(v)$ count the prime tags $s\in[S,2S]$ dividing $v$. The exact Bonferroni bound

$$
 \left|T(v)-\sum_{h=1}^{5}(-1)^{h+1}\binom{\omega(v)}h\right|
       \le \binom{\omega(v)}6
$$

costs $O(NL^{-5})$ in $Z$: for six distinct tags their common multiples $v\le X$ number at most $X/(s_1\cdots s_6)$, there are $O(X)$ choices for $d$, and $w(v)\le L$. The prime reciprocal sum over $[S,2S]$ is $O(L^{-1})$.

For each fixed $1\le h\le5$, write $r=s_1\cdots s_h$ with the tags pairwise distinct, count the tags as ordered with weight $1/h!$, and write $v=r m$. Drop the instances $(r,u)>1$. If $s_i\mid u$ then $u,v$ are both multiples of $s_i$; for each $s_i$ this gives $O(N/s_i^2)$ pairs $u,v$ and $\tau(N-uv)\ll_\epsilon N^\epsilon$ choices of $d$. The number of tag tuples attached to an eligible $v$ is bounded by a constant, as $v\asymp X$ and each tag is at least $N^{.002}$. Thus this error is $O_\epsilon(N^{1+\epsilon}/S)$. Since every tag is below the medium cut, $w(rm)=w(m)$ exactly. Replace $1-\mu^2(rm)$ by $1-\mu^2(m)$. These differ only if $(r,m)>1$, when $v$ is divisible by $s_i^2$ for a tag. For each such $v,d$ the possible $u$ is unique, so this costs $O(N L\sum_{s_i\ge S}s_i^{-2})=O(NL/S)$. In particular the short coefficient no longer has a coprimality condition involving $r$.

Partition each tag variable into relative blocks of ratio at most $1+\eta$, $\eta=L^{-20}$. If $r_0$ is the product of the $h$ left endpoints, replace the exact $m\in J/r$ by $m\in J/r_0$. For each such block tuple this can affect only $v=r m$ within $O(\eta X+1)$ integers of the two original endpoints of $J$, independently of the tuple. Since $v$ has $O(1)$ tag tuples and each $v,d$ determines at most one $u$, the total freezing error is $O(L X(\eta X+1))=o(NL^{-5})$. The enlarged supports have the same sharp physical gates for large $N$ by their fixed proportional margin.

Complete $\mu^2(N-uv)$ by $\sum_{b^2\mid N-uv}\mu(b)$ up to $b\le B=L^{J_0}$ with $J_0$ a sufficiently large fixed constant. The omitted support consists of $O(N/B)$ values of $n'=N-uv$, and on each the weight is at most $C L\tau(N-n')\tau(n')^2$, including the bounded tag multiplicity and divisibility count for $d$. The ordinary divisor moments and Hölder with exponents $4,4,2$ give $O(NL^{C'}B^{-1/2})=o(NL^{-5})$. All preceding approximation errors were made before square completion.

## 2. The centered neighboring-tile range used here

The [centered dispersion argument of the previous tagged result, §2](weak-s-type-ii-medium-prime-tagged-slice.md#2-a-centered-neighboring-tile-estimate) works uniformly at the scales

$$
 U\asymp N^{.5+.002h},\quad M\asymp N^{.5-.002h},
 \quad 1\le h\le5,\qquad N^{.4999}\le Q\le N^{.5001}.
$$

For clarity the precise estimate is this. Let real $1$-bounded $\alpha_m,\beta_n$ be on dyadic supports at $M,U$, with odd squarefree support for $\beta$. Suppose $|\sum_n\beta_n\chi(n)|\ll_\epsilon N^\epsilon\sqrt U$ uniformly for nonprincipal $\chi\bmod q,\ q\asymp Q$. At fixed numerator $a=N$, the sum over $Q\le q<2Q,\ (q,N)=1$ of the absolute congruence discrepancy from the principal density is $O(N^{1-\kappa/3})$, $\kappa=10^{-5}$.

Here is the power budget, including the dependence on these new scales. Use the identical nonnegative centered variance extended to all $q$ before Poisson, $H=(Q/M)N^\kappa$, and small gcd cutoff $N^\kappa$. The all-$q$ center has zero-frequency bound $N^\epsilon MU$ by Parseval on the nonprincipal characters. Both large-gcd remainders cost $N^\epsilon(MU+MU^2/(Q N^\kappa))$; the proof uses $mn-N\ne0$ on odd $n>1$, odd squarefree $\beta$, and no cancellation in the coefficients. The neighboring-tile argument applies because $Q\ll U$, with $O(U^2/Q^2)$ tiles and residue-class combinations per gcd, as in the [previous pointwise estimate, §1](weak-s-type-ii-wright-near-balanced.md#1-the-needed-fixed-residue-dispersion-estimate). Apply its ordinary Bettin–Chandee fallback; no assumption of polynomial subdyadic savings is used. The nonzero square term is bounded by

$$
 N^{30\kappa+\epsilon}\left(Q^{-1}U^{23/8}
                          +M^{3/20}U^{59/20}Q^{-23/20}\right).
$$

In the cross term with the center, $Q\ll U$, $N H/(UQ)\ll N^\kappa$, and the odd $n_1$ condition implies $(N,n_1)=1$, so reciprocity, incomplete Weil, and $\sum_{1\le |h'|\le H}(h',n_1)^{1/2}\ll H\tau(n_1)$ give the same $N^{2\kappa+\epsilon}U^{5/2}/Q$ bound as in the tagged estimate. The center-square Ramanujan contribution similarly remains $N^{\kappa+\epsilon}U^2/Q$.

After multiplying the variance by $M Q$, the zero and first large-gcd term are at most $N^{1.9981+\epsilon+o(1)}$ (use $U\gg N^{.502},\ Q\le N^{.5001}$); the other large-gcd error is $N^{2-\kappa+\epsilon+o(1)}$. If $U=N^{p+o(1)}$, $Q=N^z$, the two trilinear exponents before $30\kappa+\epsilon+o(1)$ are

$$
 1+(15/8)p\le1.95625,\qquad
 23/20+(9/5)p-(3/20)z\le1.993015.
$$

Both center-dependent errors have exponent at most $1.765+2\kappa+\epsilon+o(1)$. Taking $\epsilon$ sufficiently small proves the stated discrepancy bound.

## 3. The transferred long coefficient and every principal density

Fix a tuple of ratio blocks at level $h$ and put $R=S^h$. Take $n=r u$ on the long side, and let

$$
 \beta_n=C_h^{-1}
   \sum_{\substack{\boldsymbol s\ {\rm distinct,\ in\ their\ blocks}\\
                     r=\prod_i s_i,\ r u=n,\ u\in I,\ u\ {\rm odd}\\(u,r)=1}}
        \mu(u),\qquad
 \alpha_m=L^{-1} w(m)(1-\mu^2(m))
                          {\bf1}_{m\in J/r_0,\ m\ {\rm odd}}.
$$

Here $C_h$ is a fixed sufficiently large constant: $n=O(XS^h)$ has at most 300 tag prime factors for large $N$, so the ordered tuple count is bounded by $300^h$. These coefficients are real and $1$-bounded. Nonzero $\beta_n$ is odd squarefree, since $(u,r)=1$ and $\mu(u)\ne0$. Each coefficient fits in a single suitable dyadic interval: the support ratio on the long side is at most $(.745/.740)(1+\eta)^h<2$, and on the short side at most $.720/.715<2$. The two scales are $U\asymp XR$, $M\asymp X/R$.

Under global GRH all nonprincipal characters satisfy

$$
 \left|\sum_n\beta_n\chi(n)\right|
     \ll_\epsilon N^\epsilon\sqrt{XR}.
$$

Indeed expand ${\bf1}_{(u,r)=1}=\sum_{a\mid(u,r)}\mu(a)$. Each divisor $a$ corresponds to a subset of the distinct tag positions, say of size $i$; write $r=a b_1$ and $u=a\ell$. Then $\mu(a)\mu(u)=\mu(\ell){\bf1}_{(\ell,a)=1}$, as $a$ is squarefree. Holding the $i$ tags of $a$ fixed, the remaining factors in the character sum separate into the $\ell$ sum with finite mask $(\ell,2a)=1$, the factor $\chi(a)^2$, and a product-prime sum with $\chi(b_1)$ whose tags are distinct and avoid the chosen $a$-tags. The $\ell$ sum on $I/a$ is $O_\epsilon(N^\epsilon\sqrt X\, S^{-i/2})$ by the [uniform coprime twisted Möbius bound](weak-s-type-ii-character-average.md#2-exact-perron-separation-and-an-all-character-mean-square), with a polynomial-size mask. For the product-prime sum impose distinctness by inclusion–exclusion among the finitely many pairs of remaining positions. In any collision group of size $k\ge2$ there is one prime in the intersection of its block intervals, and its sum (with $\chi^k$) has the trivial bound $O(S)\le O(S^{k/2})$. A singleton group has bound $O_\epsilon(N^\epsilon\sqrt S)$ by the global-GRH prime estimate for nonprincipal characters, on its exact interval; deleting at most five selected primes does not alter this. Hence the remaining-tag sum is $O_\epsilon(N^\epsilon S^{(h-i)/2})$. Sum over the $O(S^i)$ choices of $a$-tags and finitely many subsets, giving $N^\epsilon\sqrt{X S^h}$. This bound also covers imprimitive nonprincipal characters since the prime and masked Möbius estimates do. All intervals here are hard; no imaginary twist of a changing $n$-boundary is being used.

Fix squarefree odd $b\le B$ from the completion in §1. Among squarefree $d$ fix $g=(b,d)$, making $q=[d,b^2]=b^2d/g$ injective in $d$. Its odd moduli are good for numerator $N$, and all dyads have $Q=N^{.5+o(1)}$ as required. The exact congruence for both divisibilities is $mn\equiv N\bmod q$. The omitted $q$'s and $\mu(d)$ are harmless in the summed absolute discrepancy. For the principal density use

$$
 \left|\sum_{(n,q)=1}\beta_n\right|
    \ll_\epsilon R N^\epsilon\sqrt X
$$

by summing the uniform masked Möbius bound on $I$ over $O(R)$ tag tuples, with mask $2rq$ of polynomial size. No prime cancellation in the principal character is needed; $\sum_{(m,q)=1}|\alpha_m|\ll M$. Summing all principal densities in a $q$-dyad therefore costs $O_\epsilon(M R N^\epsilon\sqrt X)=O_\epsilon(N^{.75+\epsilon})$. The centered estimate saves a fixed power of $N$ as in §2. All factors $L,C_h,1/h!$, numbers of ratio blocks, values of $b,g$, and dyads together cost only a fixed power of $L$. After summation over $h\le5$ these errors are $o(NL^{-5})$. Together with §1 this proves the signed part of (1).

## 4. Unconditional occupied mass, with $9\mid v$

For the lower bound it suffices to retain $v$ divisible by $9s p$, with $s$ a tag prime, $p$ a prime in $[N^{.10},N^{.11}]$, and require squarefree $u,d,N-uv$ and the exact odd box and congruence. The nonsquarefree test is automatically true; if $p\mid v$ then $w(v)\ge .10L$. Both tag and $p$-multiplicities on each $v\le X$ are bounded by constants. It is enough to show the resulting incidence count (including $s,p$ labels) is $\gg N/L$.

Complete $\mu^2(u)\mu^2(N-uv)$ with $a^2\mid u,b^2\mid N-uv$ up to $B_0=N^{10^{-6}}$, with $d$ still squarefree. The elementary omitted-square incidence count as in [the occupied diagonal, §1](weak-s-type-ii-exactly-balanced-diagonal.md#1-exact-support-and-a-squarefree-counting-lemma) gives $O_\epsilon(N^{1+\epsilon}/B_0)$: for a bad $u$ choose among $O(X/B_0)$ integers, then $O(X)$ choices of $v$, and at most $\tau(N-uv)$ choices of $d$; for bad $m'=N-uv$ choose among $O(N/B_0)$ integers and at most $\tau(N-m')\tau(m')$ factorizations. Fixed divisor weights cost $N^\epsilon$, and prime labels have bounded multiplicity. Put $q=[d,b^2]$; if $(9sp a,q)>1$ there is no solution. Otherwise set $u=a^2u_1,v=9sp v_1$, with odd $u_1,v_1$, and apply the same parity-sensitive rectangular Weil count on $u_1v_1\equiv N\overline{9sp a^2}\bmod q$. The main term is

$$
 \frac{|I||J|}{36\,s p a^2}\frac{\varphi(q)}{q^2},
$$

and each error is $O_\epsilon(q^{1/2+\epsilon})$. Since $q\ll XB_0^2$, the total over $d,s,p,a,b$ is $O_\epsilon(N^{.862003+\epsilon})$.

In the main terms the constraint on $s,p$ is $(sp,d)=1$, since $b\le B_0<S$. Require $(3,db)=1$, and extend the $a,b$-model sums to infinity with their remaining coprimality. The absolute tail after factoring out $|I||J|/(36 sp)$ is $O_\epsilon(N^\epsilon/(d\sqrt{B_0}))$ by the same Rankin bound as before. The $a$-weight is $a^{-2}$, and for the $b$-weight the local multiplier of $1/[d,b^2]$ relative to $1/d$ is $1/\ell$ at primes $\ell\mid d$, and $1/\ell^2$ otherwise, for each $\ell\mid b$. This extension is only of the main-coefficient model. Its Euler factors give

$$
 \frac{\varphi(d)}{d^2}(1-3^{-2})
         \prod_{\ell\mid d}(1-1/\ell)
         \prod_{\substack{\ell\ge5\ {\rm prime}\\\ell\nmid d}}
                      (1-2\ell^{-2}+\ell^{-3})
       \gg d^{-1}(\varphi(d)/d)^2
$$

for odd squarefree $d$ coprime to 3. At prime 3 only the $a$-choice is possible; at a prime dividing $d$, the $a$-choice is forbidden and the $b$-choice has multiplier $1/\ell$; at the other primes the alternatives are neither, $a$ only, or $b$ only. All factors are positive.

There are $\gg X$ odd squarefree $d\in D$ coprime to 3 with $\varphi(d)/d$ bounded below: the squarefree sieve gives positive density in the odd interval after removing multiples of 3, and the average of the sum of reciprocal prime divisors is bounded. For each such $d$, the prime reciprocal sums over $s,p$ after deleting divisors of $d$ are $\asymp L^{-1}$, $\asymp1$, respectively, from the prime number theorem and bounded counts of such prime divisors of $d$. Thus the main term is $\gg N/L$ and the listed errors are all $o(N/L)$. Each distinct occupied tuple contributes at least $.10L$ to the unsigned sum in (1). Finally its upper bound $O(N)$ follows from $O(X\sum_s1/s)$ possible tagged $v$, $O(X)$ choices of $d$, uniqueness of $u$, and $w(v)\le L$. This validates the scale of the signed saving without using GRH for the mass.
