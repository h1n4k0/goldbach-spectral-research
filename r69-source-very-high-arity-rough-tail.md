# A pointwise very-high-arity tail at the true subpower rough floor

Keep the genuine negative central sum, squarefree unit selection, independent outer masks, hard interval $I\subseteq I_0=[\rho N,(1-\rho)N]$, and original strict $d>D,e>D,de>Q$ from the [retagged subpower-floor theorem](r68-source-retagged-subpower-rough-floor.md). Here $L=\log N$, $\ell=\log L$, $T=L/\ell$, $D=\lfloor\sqrt N e^{-20T}\rfloor$ and $Q=\lfloor N e^{-20T}\rfloor$. The operands are $n=su,m=tv$, with both nonempty lower products made of primes in the respective whole ranges

$$
         [\exp(c_iT/\ell^{a_i}),\exp(d_iT)],
              \qquad 0<c_i<d_i,\quad a_i\ge0
$$

for fixed parameters. The case $a_1=a_2=0$ is two actual uncapped higher sparse bands. The nonempty rough parts have all primes at least $Y=\exp(CT)$ with fixed $C>\max(d_1,d_2)$. There is no original product cap or proper-divisor gap, and no upper arity cap.

**Theorem (unconditional, pointwise).** Let $A,\beta>0$ be fixed and set

$$
        H_\beta=\lceil\max(128,\beta+12+2(a_1+a_2))\rceil,
        \qquad J_N=\lceil H_\beta\log\ell\rceil .
$$

On the actual block where **at least one** rough part has at least $3J_N$ prime factors, the signed central sum satisfies

$$
 \begin{split}
 R_N^{\mathrm{hi}}(I)
 &=-\!\!\sum_{\substack{n+m=N,\ n\in I,\ m\in I_0\\
             (nm,N)=1,\ n,m\ {\rm selected}\\
             \max(\omega(u),\omega(v))\ge3J_N}}
     \ \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
             \mu(d)\mu(e)\log(n/d)\log(m/e),\\
 |R_N^{\mathrm{hi}}(I)|&\ll
         \mathfrak S(N)\left(|I|\ell^{-\beta}+NL^{-A}\right).
 \end{split}                                                     \tag{1}
$$

This holds for every sufficiently large even $N$ and every admitted hard interval and outer mask, with constants depending on the fixed parameters. It independently controls a true higher-arity remainder with any prescribed power of $\log\log N$, without signed cancellation or a first-moment transfer. It does not remove the gap between the small growing arity in the retagged theorem and the large constant multiple of $\log\ell$ in (1). No bound for that middle-arity range or Hypothesis S is asserted.

## 1. A pointwise tail for the genuinely uncapped lower products

Let $\varepsilon=1/64$. Temporarily discard $s>N^\varepsilon$ or $t>N^\varepsilon$. Every rough part has at most $L/\log Y=\ell/C$ factors, so the absolute sum of marks on one side is $O(L\,2^{\ell/C}\tau(s))$ or the counterpart with $t$. Cauchy on the fixed equation $n+m=N$ and the upper bound $N/w$ for multiples of a fixed lower product reduce the discarded mass to the geometric mean of the two squared reciprocal profiles, multiplied by $O(NL^2 2^{2\ell/C})$. Those profiles have unrestricted Euler products $1+4/p$, bounded by a power of $\ell$ by Mertens on the stated alphabets. Rankin at $\lambda/T$ with fixed $\lambda>0$ gives $L^{-\varepsilon\lambda}$ in a squared tail, while its Euler product increases to at most $\prod(1+4e^{d_i\lambda}/p)$, again a power of $\ell$ with fixed exponent. Choosing $\lambda$ large makes this discarded part $O_A(NL^{-A})$, even with the displayed power $2^{2\ell/C}=L^{2\log2/C}$. This is an upper bound on the true absolute tail including all original divisor tests, not a restriction on the statement.

## 2. Freeze one third of the true rough primes of each operand

On the truncated range write $r=\omega(u)$, $r'=\omega(v)$ and put $j=\lfloor r/3\rfloor$, $j'=\lfloor r'/3\rfloor$. Let $F$ be the product of the $j$ smallest rough primes of $u$, and let $G$ be the analogous product in $v$. The empty product is one. These choices are unique on the true squarefree operands. The average logarithm of the first $j$ sorted prime factors is at most the full average, so

$$
         F\le u^{j/r}\le N^{1/3},\qquad
         G\le v^{j'/r'}\le N^{1/3}.
$$

The remaining $u/F,v/G$ are nonempty. Freeze $h=sF,k=tG$ so that $hk\le N^{2/3+2\varepsilon}=N^{1-\omega_0}$ where $\omega_0=1/3-2\varepsilon>0$. The genuine pair satisfies $(h,k)=1$ and $(hk,N)=1$ by the exact unit masks and the sum line. In particular the parity and affine determinant $N$ are unchanged. Its two remaining integer variables have no prime factor below $Y$.

Use the positive [affine rough-integer sieve](r65-source-pointwise-rough-complements.md) for $hP+kV=N$ on the genuine frozen pair, at $Z=N^{\omega_0/24}$ and $z=\exp(\eta T)$ for fixed $0<\eta<C$. Thus $z<Y$, and $\log z/\log Z\to0$ is small enough for the truncated Euler denominator as in that proof. The interval in the integer parameter has length $|I|/(hk)$. The upper bound is

$$
 O_{C,\eta}\!\left(
       \frac{\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)}{hkT^2}
                                   +N^{\omega_0/4}\right),
      \qquad \lambda^*(w)=\prod_{\substack{p\mid w\\p>2}}\frac{p-1}{p-2}.
 \tag{2}
$$

Here the denominator is $T^2$, not $L^2$: the actual rough floor is used for the sieve, and no polynomial primality of the remaining products is assumed. The $N^{\omega_0/4}=Z^6$ floor error is uniform in the hard endpoint convention. The conditions defining the smallest $j,j'$ primes, the genuine squarefreeness, and the original masks on the remaining variables may be dropped only for this positive upper count.

At fixed true $r,r'$, the sum of absolute original divisor marks at a pair of operands is at most

$$
                   L^2\tau(s)\tau(t)2^{r+r'}.
 \tag{3}
$$

This upper bound is taken **after** the actual sum and therefore needs no claim that the cutoff or the signs can be relaxed in an exact identity. For a given $h,k$ the lower and rough parts split uniquely by their disjoint ranges. The frozen arities $j,j'$ determine $r,r'$ up to the three choices $3j,3j+1,3j+2$ and their analogues. There are $O(N^{1-\omega_0}L)$ ordered frozen pairs in the product envelope. On the truncation $\tau(s)\tau(t)=N^{o(1)}$ uniformly by splitting their prime factors at $\sqrt L$; also $2^{r+r'}\le L^{2\log2/C}$. The summed floor error after (3) is $O(N^{1-3\omega_0/4+o(1)})=O_A(NL^{-A})$.

## 3. A factorial rough-arity tail

The unmarked lower reciprocal profiles $\sum_w\tau(w)\lambda^*(w)/w$ are $O(\ell^{2a_i})$ by the log endpoint ratios. Put

$$
         B_N=\sum_{Y\le p\le N}\frac{\lambda^*(p)}p.
$$

Since $\lambda^*(p)=1+O(1/p)$ and $\log Y=CT$, Mertens gives $B_N\le\log\ell+O_C(1)$. In particular $e^{8B_N}\ll_C\ell^8$ and $B_N\le2\log\ell$ for all sufficiently large $N$. For fixed $j$, the sum of $\lambda^*(F)/F$ over all squarefree products of $j$ allowable rough primes is at most $B_N^j/j!$ by counting ordered tuples. We may drop the additional size constraint on $F$ in this positive reciprocal profile. Since $2^r\le4\cdot8^j$ and at most three $r$ map to a fixed $j$, the full rough profile on the opposite slot is $O(e^{8B_N})$.

If $r\ge3J_N$ then $j\ge J_N$. The profile on this high-arity side is at most a fixed multiple of

$$
      \sum_{j\ge J_N}\frac{(8 B_N)^j}{j!}
        \ll \left(\frac{16e}{H_\beta}\right)^{J_N}
        \le \ell^{-H_\beta}.
 \tag{4}
$$

Indeed the ratio of successive terms is at most $16/H_\beta$ past $J_N$, and $J_N!\ge(J_N/e)^{J_N}$ handles the first. The final inequality follows from $H_\beta\ge128>16e^2$. The same bound applies if the second side has high arity; a two-way upper bound may count their intersection twice. Combining (2)–(4), $L^2/T^2=\ell^2$ and the lower profiles, the main positive coefficient divided by $\mathfrak S(N)|I|$ is

$$
             O\!\left(\ell^{\,2(a_1+a_2)+10-H_\beta}\right)
                                   =O(\ell^{-\beta}).
$$

The lower and rough reciprocal sums only discard conditions after their use in the genuine frozen local sieve. The true lower-product tails and floor errors already obtained complete (1).

The high-arity block can contain nonzero genuine summands. For example choose fixed band constants $c_i=1,d_i=2,a_i=0$ and $C=3$. About an external scale $X$ take one interior lower prime on each side, and the same number $4\lceil H_\beta\log\ell_X\rceil$ of distinct true rough primes per side near $\exp(4T_X)$. Denote their products with the lower primes by $S,U$. On each side choose two further rough primes $f,F$ or $g,G$ with $Sf,Ug$ near $\sqrt{2Q_X}$ and $SfF,UgG$ near $X/2$. All these primes exist in fixed narrow proportional windows by the PNT, since $\log S,\log U=O(T_X\log\ell_X)=o(\log X)$. Take all primes distinct, so the resulting even sum has two central units. The moving scales differ negligibly for $\log N=\log X+O(1)$, and the true rough arities exceed $3J_N$. Here $F,G>\sqrt N$ and $Q<(Sf)(Ug)<3Q$, with both maximum proper labels above D. Group the true divisors into the complete lower orbits for $S,U$ and the remaining two-prime labels on each side. All complete lower orbits involving $F,G$ cancel because $S,U$ are composite and these labels pass against every opposite long divisor. Among the remaining $f,g$ lists only the two maximum lower multipliers pass the product test, since omitting any prime reduces the product by more than three. With equal arities on the two sides their original signs give $-\log F\log G$. This is a nonvacuity witness for (1), not a lower bound for its aggregate.
