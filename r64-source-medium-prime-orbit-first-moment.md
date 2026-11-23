# A first moment for genuine medium-factor interactions with the original curved cutoff

Fix $0<\rho<1/2$ and fixed $0<\kappa<1/4$. Let $X$ be sufficiently large and write $L=\log X$. For even $N\in[X,2X]$ keep $I_0(N)=[\rho N,(1-\rho)N]$ and the original retuned thresholds

$$
 D_N=\left\lfloor \sqrt N\,e^{-20\log N/\log\log N}\right\rfloor,
 \qquad
 Q_N=\left\lfloor N\,e^{-20\log N/\log\log N}\right\rfloor .
$$

For this dyad let $\mathscr P_1,\mathscr P_2$ be arbitrary finite sets of primes below $X^\kappa$. In slot $i$ select squarefree central units $n_i=s_i u_i$, with all primes of $s_i$ in $\mathscr P_i$ and all primes of $u_i$ at least $N^\kappa$. Require $s_1>1$ and at least one rough prime on each side. There is no upper bound on the number of lower primes on either side. The second side can have $s_2=1$. In particular one can require **both** sides to have at least two rough primes, and genuine medium primes larger than $\log N$ on one or both sides. Any further subset masks on these integers may vary with $N$, provided they do not distinguish the interior divisor labels once the integers are fixed.

For hard $I\subseteq I_0(N)$ let the exact signed sum be

$$
 R_N(I)=-
 \sum_{\substack{n+m=N,\ n\in I,\ m\in I_0(N)\\
             n,m\ {\rm in\ their\ selected\ classes},\ (nm,N)=1}}
 \sum_{\substack{d\mid n,\ e\mid m\\d>D_N,\ e>D_N,\ de>Q_N}}
       \mu(d)\mu(e)\log(n/d)\log(m/e).
 \tag{1}
$$

All three inequalities are strict. Let $R_N^*$ be the supremum of $|R_N(I)|$ over these hard intervals and optional integer masks, for the fixed dyadic alphabets. Define their positive reciprocal moments

$$
 M_i=\prod_{p\in\mathscr P_i}(1+2/p),\qquad
 B_i=\sum_{p\in\mathscr P_i}\frac{\log p}{p},\qquad
 M_i(\zeta)=\prod_{p\in\mathscr P_i}(1+2p^{-1+\zeta}).
$$

**Theorem (unconditional first moment).** For every real $\zeta>0$,

$$
 \sum_{\substack{X\le N\le2X\\2\mid N}}R_N^*
 \ll_{\rho,\kappa} X^2 M_2
       \left(\frac{M_1(1+B_1)}L+X^{-\zeta/4}M_1(\zeta)\right).
 \tag{2}
$$

The constant does not depend on the alphabets or $\zeta$. The roles can be exchanged if the designated nonempty lower product is on the other side, reflecting the physical interval if necessary. If both products must be nonempty one can take the better directional bound. This does not solve the two-rough-leg problem when the lower prime factors range over arbitrary unseparated polynomial scales.

Two useful consequences concern actual new medium-prime regimes, not just bounded small slots:

1. If slot $i$ allows **all** primes below $y_i(N)=\exp((\log N)^{\alpha_i})$ in its lower component with fixed $0<\alpha_i<1$, the first moment is $O_{\rho,\kappa,\alpha_1,\alpha_2}(X^2L^{-1+3\alpha_1+2\alpha_2})$. For $b=1-3\alpha_1-2\alpha_2>0$ and fixed $0<\gamma<b$, all the stated hard-window quantities are $\ll NL^{-\gamma}$ off $O(XL^{-b+\gamma})$ even targets. Equal exponents can be any fixed $\alpha<1/5$.
2. Both slots may instead draw **all** their lower primes from
   $$
   \Big[\exp\!\left(\frac{c_i\log N}{\log\log N}\right),
        \exp\!\left(\frac{C_i\log N}{\log\log N}\right)\Big],
            \qquad 0<c_i<C_i<\infty\ {\rm fixed}.
   $$
   The first moment is $O(X^2/\log L)$, with constants depending also on these four endpoints. Thus for fixed $0<\gamma<1$, $R_N^*\ll N(\log L)^{-\gamma}$ except on $O(X(\log L)^{-1+\gamma})$ even targets. This band reaches far beyond the preceding complete low ranges while retaining bounded reciprocal prime mass.

These are density-one bounds with the stated saving/exception tradeoff, not bounds on each even $N$ or of order $|I|$ on short windows. They do not cover nonsquarefree legs, intervals outside the specified central region, or Hypothesis S. They use the full original signed sum line, not a model of it, and no assumption on the distribution of prime pairs at a fixed modulus.

## 1. Positive dyadic profiles

Use the common physical envelope $x\in[\rho X,2X]$. Each rough part contains $1\le r\le K$ primes, where $K=\lceil2/\kappa\rceil$ suffices since each is at least $X^\kappa$. One can sort these primes, then in estimates sum over all ordered choices. The overcount is bounded in terms of $\kappa$. Fix the lower product $s$ and $r-1$ rough primes with product $w$. The number of choices of the final rough prime is

$$
 \ll_\kappa \frac{X}{s w L}.
 \tag{3}
$$

Indeed it is zero unless $2X/(sw)\ge X^\kappa$, and otherwise the Chebyshev upper bound at $2X/(sw)$ gives (3). The unrestricted reciprocal sum over any one rough prime in $[X^\kappa,2X]$ is $O_\kappa(1)$ by prime Mertens. Consequently, on either slot, the total weight $L\tau(s)$ over the enlarged integer envelope is $O_\kappa(X M_i)$. Here $\tau(s)=2^{\omega(s)}$, and

$$
 \sum_{\substack{s\ {\rm squarefree}\\p\mid s\Rightarrow p\in\mathscr P_i}}\frac{\tau(s)}s=M_i,
 \qquad
 \sum_s\frac{\tau(s)\log s}s
   =M_i\sum_{p\in\mathscr P_i}\frac{2\log p}{p+2}
   \le 2M_i B_i.
 \tag{4}
$$

Both sums allow $s=1$. The total weight $\log q$ on the subfamily with lower product a single prime $q$ is instead $O_\kappa(X B_i/L)$ by (3). The pointwise sum of absolute divisor marks without any cutoff is $O_\kappa(L\tau(s))$ since there are at most $2^K$ rough divisor labels. Thus on the opposite slot the unrestricted sum, over $m$ and its possible divisor labels $e$, of $|\mu(e)|\log(m/e)$ is $O_\kappa(X M_2)$.

For the designated side delete $s>X^{1/4}$ by an absolute upper bound. The same genuine prime count (3), but with Rankin over the lower product, gives that tail's total integer weight at most

$$
 O_\kappa\!\left(X\sum_{s>X^{1/4}}\frac{\tau(s)}s\right)
       \ll_\kappa X^{1-\zeta/4} M_1(\zeta).
 \tag{5}
$$

All target pairs $(n,m)$ determine at most one $N=n+m$, so multiplying (5) by the opposite total weight already bounds the sum over $N$ of the supremum of the excluded contribution. This applies to the original signed cutoff because taking absolute values and enlarging the set of its labels is legitimate for this discarded tail. There is no restriction on the size of the opposite lower product in this proof.

## 2. Exact orbits and uniformity of the thin support

On the retained designated leg $n=su$ with $1<s\le X^{1/4}$, fix an actual opposite $e>D_N$. Set $T_e(N)=\max(D_N,Q_N/e)$. The exact test on $d$ is $d>T_e(N)$, and $D_N\le T_e(N)\le\sqrt N$ since $e\ge D_N+1$ and $Q_N\le N e^{-20\log N/\log\log N}$. The orbit with rough part $f\mid u$ consists of $d=af$ for $a\mid s$. Its empty rough subset $f=1$ is wholly out because $s<D_N$; the full rough subset $f=u$ is wholly in because $u\ge\rho X^{3/4}>\sqrt{2X}$. Every full orbit has the exact signed mark

$$
 \sum_{a\mid s}\mu(af)\log(n/(af))=\mu(f)\Lambda(s),
 \tag{6}
$$

by $\sum_{a\mid s}\mu(a)=0$ and $\sum_{a\mid s}\mu(a)\log(s/a)=\Lambda(s)$. The lower product is squarefree, so (6) vanishes unless $s$ is a prime $q$, when its size is $\log q$. This cancellation is performed against each actual opposite divisor, before taking absolute values. Summing these full orbits by the singleton profile of §1 and the opposite total bounds their first moment by $O_\kappa(X^2 M_2 B_1/L)$.

A partially included orbit must have nonempty proper rough subset $f$, and its exact support forces

$$
      f\le T_e(N)<sf,\qquad
      \log f\in(\log T_e(N)-\log s,\log T_e(N)].
 \tag{7}
$$

Its absolute weight after (7) is known is at most $O(L\tau(s))$. This follows by bounding all its original signed terms once partial inclusion is established; one has not replaced complete orbits by unsigned ones.

There is a fixed outward envelope for (7) at each opposite divisor $e$ throughout the dyad. More precisely,

$$
      \log T_e(N)=\log T_e(X)+O(1)
      \quad(X\le N\le2X),
 \tag{8}
$$

with an absolute constant independent of $e$. Define $D_X,Q_X$ by the same formulas even if $X$ is not an integer. In log coordinates, the two unrounded log thresholds are $t/2-20t/\log t$ and $t-20t/\log t$, with $t=\log N$. Their derivatives are bounded for large $t$ and the log change from a floor is $o(1)$. The max of these two rounded log functions, with $-\log e$ added to the second, changes by at most the larger change in the two functions. This proves (8) even for divisors that are admissible only at some targets of the dyad. Only the **outward** enclosure is used on the partially included orbit. It does not replace the curved cutoff on the original sum.

## 3. A dyadic count of the genuine partial orbits

Fix $m$ and its divisor $e$, and fix one nonempty proper rough subset label in the designated tuple. Keep a rough prime $p_r$ free for (3). If the label omits $p_r$, then after freezing all other slots except one selected $p_i$, the coefficient of $\log p_i$ in $\log f$ is $+1$. If the label uses $p_r$, write

$$
      \log f=\log n-\log s-\sum_{p_i\notin f}\log p_i.
$$

Some $p_i\notin f$ is a frozen slot and has coefficient $-1$. On the whole physical envelope $\log n=\log X+O_\rho(1)$. In either case, for fixed $s$ and all other frozen slots, the chosen $p_i$ is confined to **one** log interval of length $\log s+O_\rho(1)$ by (7) and (8). The chosen $p_i$ is distinct from the final rough prime that will be counted in (3). The argument uses that $f$ is proper and nonempty; when there is just one rough prime no partial orbit remains.

A log interval of length $W$ on the polynomial scale $[X^\kappa,2X]$ has prime reciprocal mass $O_\kappa((1+W)/L)$: cover it by at most $O(1+W)$ unit log intervals and apply Chebyshev on each enclosing fixed-ratio interval. Thus after summing the constrained frozen coordinate, the other rough reciprocals and then the last prime (3), the total partial weight over this designated dyadic integer family, for the fixed $m,e$, is

$$
 \ll_{\rho,\kappa} \frac{X}{L}
      \sum_s\frac{\tau(s)(1+\log s)}s
    \ll_{\rho,\kappa} \frac{XM_1(1+B_1)}L.
 \tag{9}
$$

The factors in (9) are as follows: the last prime contributes $X/(swL)$, the absolute orbit weight contributes $O(L\tau(s))$, and the constrained frozen prime gives one more $1/L$ with the factor $1+\log s$. The rough arity and choice of rough subset cost only a bounded factor. Physically there is no relaxation of the true target in deriving (7); in bounding (9) we may enlarge the set using the outward envelope. In particular the full integer-level boxes and all possible positions of hard endpoints are bounded by this one argument.

Multiply (9) by the opposite total $O_\kappa(XM_2)$ from §1. The map $(n,m)\mapsto N=n+m$ ensures this bounds the sum of the per-target nonnegative envelopes, rather than summing a fixed-target estimate over a further independent $N$. The envelopes bound every hard window and every integer-only mask simultaneously: cancellation (6) holds unchanged for each retained integer pair, and all post-cancellation upper bounds drop such masks only in positive sums. Adding the full-orbit estimate and (5) proves (2), with both original signs and unit conditions on its input. Reflection for the other order takes $I$ to $N-I$; indeed the central region is invariant under this reflection. No uniform bound for a fixed target can be read off (9) alone.

## 4. Verifying the two medium regimes

For the complete lower ranges choose dyad envelopes $\mathscr P_i=\{p\le y_i(2X)\}$. Mertens and Chebyshev give $M_i\ll (\log y_i(2X))^2\ll L^{2\alpha_i}$ and $B_i\ll L^{\alpha_i}$. Use $\zeta=1/\log y_1(2X)$ in (5). Now $p^\zeta\le e$, so $M_1(\zeta)\ll L^{O(1)}$, while $X^{-\zeta/4}\le \exp(-c L^{1-\alpha_1})$. The tail is smaller than every logarithmic power and the main factor is $L^{-1+3\alpha_1+2\alpha_2}$. For the higher bands, the moving ranges sit inside dyadic bands with slightly enlarged fixed constants, so $\sum_{p\in\mathscr P_i}1/p=O_{c_i,C_i}(1)$ by prime Mertens, $M_i=O(1)$ and $B_i=O(L/\log L)$. Choose $\zeta=A\log L/L$ with any fixed large $A$. Then $p^\zeta\le e^{O_{C_1}(A)}$ on the designated alphabet and $M_1(\zeta)\ll_{A,c_1,C_1}1$, so the tail can be made $O(L^{-A/4})$. Markov applied to (2) gives exactly the two stated exception tradeoffs. If the two bands overlap or a prime on one leg would divide the other, the actual unit and sum tests have already handled it; no independence at a prescribed target was invoked.

The higher-band regime contains actual central tuples with a genuine signed weight. For instance use the same medium band with $c_i=1/2,C_i=1$ and take one distinct lower prime on each side with log near $0.75\log X/\log\log X$. On each leg take two further distinct primes near $\sqrt{X/q}$ for its chosen lower prime $q$, with all six primes distinct over the two legs. The ordinary PNT supplies these at arbitrary fixed narrow relative widths, and the resulting integers are each near $X$; their sum is even and both are central units for sufficiently narrow widths (and lies in a comparable dyad). At these sizes both rough primes on each leg exceed $D_N$ and any product of one from each side exceeds $Q_N$ with room to spare. All nonempty rough subsets therefore carry full orbits against the opposite long terms, giving the actual weight $-(\log q)(\log q')$ before adding any other pairs. This only certifies that the asserted arithmetic class is present and can have a nonzero marked summand. It is not a lower bound on the combined signed sum. The original conversion from these arithmetic components to an operator bound still requires its own assumptions and estimates of the other components.
