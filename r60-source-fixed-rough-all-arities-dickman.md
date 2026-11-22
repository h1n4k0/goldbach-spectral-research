# All factor counts at fixed polynomial roughness: exact central cutoff and Dickman cancellation

Fix $0<\rho<1/2$ and a **fixed** $0<\kappa<1/4$. For sufficiently large even $N$ take $I_0=[\rho N,(1-\rho)N]$, any hard $I\subseteq I_0$, and the original retuned divisor thresholds

$$
 L_N=\log N,\qquad \theta_N=20/\log\log N,\qquad
 D=\lfloor\sqrt N e^{-\theta_N L_N}\rfloor,\qquad
 Q=\lfloor N e^{-\theta_N L_N}\rfloor.
$$

Let $\mathcal F_\kappa(N)$ be all squarefree central integers whose prime factors are at least $N^\kappa$, retaining exact units modulo $N$. Let $\mathcal B(N)$ be the [R58](r58-source-central-three-factor-first-order.md) central squarefree zero-small class with at most three prime factors, also with exact units. Finally set $\mathcal H_\kappa=\{n\in\mathcal F_\kappa:\Omega(n)\ge4\}$ and $\mathcal U_\kappa=\mathcal B\sqcup\mathcal H_\kappa$. The last union is disjoint. A mixed pairing of $\mathcal F_\kappa$ with $\mathcal B$ is defined in its two ordered slots, not by counting the union of overlapping sets.

For arbitrary named leg selections $\mathcal D,\mathcal E$ above write

$$
 \mathcal R_N(\mathcal D,\mathcal E;I)=
 -\!\sum_{\substack{n+m=N,\ n\in I\cap\mathcal D,\ m\in I_0\cap\mathcal E\\
                         (nm,N)=1}}
       \ \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
          \mu(d)\mu(e)\log(n/d)\log(m/e).
                                                               \tag{1}
$$

This keeps the actual curved cutoff and the actual negative central sum-alias sign. The difference aliases cannot occur on $I_0^2$, and equality of the two coordinates is excluded by units on this sum line.

For each integer $k\ge2$ let

$$
 \begin{split}
 A_k(x)&=\sum_{\substack{J\subseteq\{1,\ldots,k\}\\
                            s_J>1/2}}
       (-1)^{|J|}(1-s_J),\qquad s_J=\sum_{j\in J}x_j,\\
 c_{k,\kappa}
   &=\frac1{k!}
      \int_{\substack{x_1+\cdots+x_k=1\\x_i\ge\kappa}}
        \frac{A_k(x)}{\prod_{i=1}^k x_i}\,dx_1\cdots dx_{k-1},
       \qquad C_\kappa=\sum_{k\ge2} c_{k,\kappa}.
 \end{split}                                                    \tag{2}
$$

The sum is finite and a degenerate simplex has zero contribution. Set $\Delta=\pi^2/12-\log2$, and assign leg constants

$$
       \gamma_{\mathcal F_\kappa}=C_\kappa,\quad
       \gamma_{\mathcal B}=\Delta,\quad
       \gamma_{\mathcal H_\kappa}=C_\kappa-c_{2,\kappa}-c_{3,\kappa},
       \quad
       \gamma_{\mathcal U_\kappa}
          =\Delta+C_\kappa-c_{2,\kappa}-c_{3,\kappa}.
$$

**Theorem (unconditional at each fixed $\kappa$).** For any fixed $A,b>0$, with $L=\log X$, except on $O_{\rho,\kappa,A,b}(X L^{-b})$ even integers $N\in[X,2X]$, simultaneously for every hard $I$ and every ordered pair of the four named selections,

$$
 \mathcal R_N(\mathcal D,\mathcal E;I)
     =-\mathfrak S(N)|I|\,\gamma_{\mathcal D}\gamma_{\mathcal E}
       +O_{\rho,\kappa,A,b}\!\left(\mathfrak S(N)
                          (|I|\theta_N+NL^{-A})\right).
                                                               \tag{3}
$$

Here $\mathfrak S(N)$ is the ordinary even binary singular series. In particular the self block of $\mathcal F_\kappa$ has leading coefficient $-C_\kappa^2$, and its mixed coefficient with $\mathcal B$ is $-C_\kappa\Delta$ before multiplication by $\mathfrak S(N)|I|$. This is a density-one assertion on the stated central blocks only. The reduction of the original operator to these arithmetic components retains its separate assumptions.

There is an exact continuum cancellation across the factor counts in (2). Let $K_\kappa(dt)=\mathbf1_{t\ge\kappa}\,dt/t$ on the nonnegative line, set
$\mathcal B_\kappa=\sum_{j\ge0}K_\kappa^{*j}/j!$ (with atom one at zero), and let $\rho_{\rm D}$ be the Dickman function. Then

$$
 C_\kappa=-\int_{[0,1/2)}
                \frac{t}{1-t}\,
                  \rho_{\rm D}\!\left(\frac{1-t}{\kappa}-1\right)
                   \mathcal B_\kappa(dt),\qquad
 0<-C_\kappa\le
       \frac1{2\kappa\lfloor(2\kappa)^{-1}-1\rfloor!}.
                                                               \tag{4}
$$

Also $\gamma_{\mathcal U_\kappa}=\kappa+O(\kappa^2)$ as $\kappa\downarrow0$. These statements allow the **sequential** limits described below; nothing in (3) is uniform for a changing $\kappa=\kappa(N)$.

## 1. Genuine box counts at every fixed allowed arity

Put $K=\lfloor1/\kappa\rfloor$. Every member of $\mathcal F_\kappa$ has at most $K$ prime factors, and a one-prime leg has zero long mark. For a fixed $2\le k\le K$ use all ordered $k$ prime slots with common mark $L/k!$, initially allowing repeats. Each complete squarefree frequency then has mark $L$. Allow independent hard subintervals for all prime slots in addition to the exact physical and unit masks, as in [R59](r59-source-fixed-rough-four-prime-central.md). The other leg can be any rough arity of this fixed list, or one of the positive active old types from [R58](r58-source-central-three-factor-first-order.md) (including the heavy $L$ marker on $H_2$ when desired). We claim the same uniform exact **positive full sum-line** box comparator as [R59](r59-source-fixed-rough-four-prime-central.md), with arbitrary fixed error exponent $A'$ and the same $O_{\rho,\kappa,A',b}(XL^{-b})$ single exceptional bound for all boxes. The positive box count itself does not impose a two-leg product cutoff; it will only be used on a region where that cutoff passes exactly, or to bound positive boundary majorants.

Here are the changes needed to check this at every $k$, rather than only at four. Use the fixed physical envelope $[\rho X/2,2X]$, individual rough prime windows within $[X^\kappa,2X^{1-(k-1)\kappa}]$, and the classical arcs of denominator $d\le P=L^{6Z}$ and common half-width $P/X$, with $Z=2A'+2b+20K+200$. Exact target factor cuts are retained in the cell decomposition. For a primary prime of dyadic scale $U$, group the other $k-1$ primes into their product $m$ of scale $V=X/U$. Each $m$ has at most $(k-1)!$ ordered assignments across the other prime cells at fixed levels. Cauchy in $m$, with the bounded multiplicity and the constant $L/k!$ in its outer factor, gives a nonnegative sum of unmarked primary-prime squares. Sum these over the partner cells first. The ordered bound then permits a single enlargement to the full $m$ interval, before expanding the squares and summing over the physical cells. After expansion, the common-floor condition for $pm,(p+h)m$ is exactly the [R59](r59-source-fixed-rough-four-prime-central.md) one, with its strict test $hm<H$ at cell length $H$, including the integer edges.

For clarity, the numerical hypotheses of the grouped Fejér and geometric sums of [R59](r59-source-fixed-rough-four-prime-central.md) §1 hold unchanged. On the minor arcs choose $P<d\ll X/P$ by Dirichlet approximation, group $h$ into $O(1+U/d)$ blocks of length at most $d/2$, and use $Y_0=XL^{-Z}$. Now

$$
   U\ll X^{1-(k-1)\kappa},\quad
   V\ll X^{1-\kappa},\quad UV=X,\quad U/Y_0=o(1).
$$

In particular the grouped contribution $XU$ times a fixed log power is $o(X^2L^{4-Z})$, and the terms using $dV$ also have this bound because $d\ll XL^{-6Z}$. The discrete Fejér grid error costs $O(X^2L^{4-Z})$: after partner enlargement each $pm$ for a fixed difference has at most $O(L)$ possible prime divisors $p$, just as in [R59](r59-source-fixed-rough-four-prime-central.md), regardless of the number of original partner slots. The affine, diagonal and shifted near/far harmonic sums therefore give $O(X^2L^{4-Z})$ per ordinary dyad and joint cell energy $O(X^2L^{6-Z})$ after the dyadic Cauchy loss. The original multiplicity only changes constants depending on $\kappa$. These inequalities also apply at $k=2$. A class with $k\kappa=1$ is empty in the genuine central support and can be skipped.

Use the integrated cell energy $O_{\rho,\kappa}(XL^2)$ of the other leg by Parseval and bounded ordered multiplicity. Prime axes with optional hard cuts and target $N$-unit holes use $O(L^2)$ dyadic cells each; physical axes use $O(L)$, with the exact extra product axis in the $H_1$ case as in [R56](r56-source-high-factor-triprime-mixed-endpoints.md). There are at most $O(L^{4K+2})$ terms in the two-leg expansion and $O(L^{2K+2})$ choices of levels. By Cauchy and Bessel the genuine minor maximal squared sum is $O_{\rho,\kappa}(X^3L^{6K+12-Z})$. Markov at $XL^{-A'}$ gives the required exception exponent, uniformly over every hard prime-slot and physical window. The old type 2 last-prime units may alternatively use the old Cauchy restoration. There are only finitely many arity/old-marker choices depending on $\kappa$.

On the major arcs freeze $k-1$ primes with product $u$ and use the last genuine prime, at size at least $X^\kappa$, in the [Siegel–Walfisz estimate](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=129) at effective denominator $d/(d,u)$. Its hard interval is intersected with the physical window divided by $u$; partial summation, the arc phase and reciprocal outer sums work exactly as [R59](r59-source-fixed-rough-four-prime-central.md). The real profile per frozen ordered tuple has weight $L/(k!u\log(t/u))$ at $t/u$ in its selected last-prime interval. A last prime dividing $N$ costs at most $O_{\rho,\kappa}(X^{1-\kappa}L)$ in the genuine transform: finitely many such primes, each with $O(X/p)$ partner indices and bounded multiplicity. The older subpower-scale last primes use their existing Siegel–Walfisz inputs. After reduced numerator summation the complete signed Ramanujan coefficient for a pair of frozen products is zero for a common prime, and otherwise $\mathfrak S(N)$ times the product of the ordinary special factors $(\ell-1)/(\ell-2)$, as in [R56](r56-source-high-factor-triprime-mixed-endpoints.md)/[R59](r59-source-fixed-rough-four-prime-central.md). This remains true if repeated outer primes were temporarily admitted, because a nonsquarefree denominator is killed by Möbius or by the Ramanujan prime-power zero at a special $N$-unit prime.

The tails are uniformly controlled: with coarse positive profile weights $g_u=L/u$ per ordered outer tuple, $\sum_{m\mid u}g_u\ll_{\rho,\kappa} L^{K+1}/m$ for squarefree $m$ on every fixed envelope, using bounded slots for the prescribed primes and harmonic sums for the rest. The old types meet this same bound. At most $2K$ special primes occur in a box pair. Bounded variation gives the real tail $O(\mathfrak S(N)XL^{2K+2}/P)$. In the denominator tail the noncommon Rankin factors are bounded, while common factors are $\prod_{\ell\mid(u,v)}(1+\sqrt\ell)=\sum_{m\mid\operatorname{rad}((u,v))}\sqrt m$. Their weighted pair sum is $O_{\rho,\kappa}(L^{2K+2}\sum_m m^{-3/2})$. The rest is the ordinary convergent half-power Ramanujan series averaged with $\sum_{N\le2X}|c_h(N)|\le 2X\tau(h)$. Correct units fix the special Ramanujan factors before this averaging, so the bound $O(L^{2K+2}P^{-1/2})$ for the averaged normalized denominator tail is valid also for varying masks. Markov supplies the simultaneous bound; no exceptional set depends on a box choice.

Finally a repeated prime in a rough $k$-factor frequency forces a square divisor of base at least $X^\kappa$, and the possible such integer frequencies number $O(X^{1-\kappa})$. Their weight is $O_\kappa(L)$ and the opposite integer on the full sum line is determined, giving a power-saving difference. In the real model repeated frozen factors have small reciprocal-square mass, and last-prime equalities are a null set for each frozen tuple. Any older repeated classes are corrected as in their own proof. This proves the claimed positive box comparator for the true squarefree legs.

## 2. Exact product cutoff and the uniform real profile

For a fixed target partition the labelled prime logs of each rough arity into unit-length hard boxes. A box is stable if the log sum of every **nonempty proper subset** of its slots lies outside $[(1/2-2\theta_N)L_N,(1/2+2\theta_N)L_N]$ throughout the box. The full subset has mark zero and the empty subset is short. On a stable box each divisor is exactly long or short under the genuine threshold $D$ according to its sign relative to $L_N/2$. Each contributing long divisor is $\ge N^{1/2+2\theta_N}$, so $de>Q$ with **any** counterpart divisor $e>D$. Thus no curved decision is changed on the stable portion, including against the old endpoint legs. A prime leg is identically zero. A stable high giant with squarefree composite cofactor also gives exact zero when it is admissible; this follows either from the complete long orbit or from the same signed subset sum below. For $k=2$ the high giant with prime cofactor is not deleted.

Any nonstable box contributing a true integer lies within $2\theta_N+O_\kappa(L_N^{-1})$ of a proper-subset half hyperplane at its true prime logs. Use an outward cover by boxes meeting those strips, changing log sums by $O_\kappa(1)$ only. In the positive real model at a fixed physical $t$, after freezing $k-1$ primes put $x_k=\xi-\sum_{j<k}x_j$ with $\xi=\log t/L_N$. Every proper nonempty subset log sum has a free frozen coefficient $\pm1$: take a frozen slot inside the subset when the last slot is absent, and a frozen slot outside the subset when it is present. Conditional on the other frozen slots, the strip therefore gives a reciprocal prime interval of exponent width $O_\kappa(\theta_N+L_N^{-1})$, whose mass is $O_\kappa(\theta_N+L_N^{-1})$ by Chebyshev on polynomial scales. The remaining reciprocal masses and the last denominator are fixed-$\kappa$ bounded. Each true mark (1) is bounded on a boundary pairing by a constant times the two positive weights in §1: a rough side has $O_\kappa(L)$ absolute total divisor mark, and the old side uses its appropriate [R58](r58-source-central-three-factor-first-order.md) positive weight, including a heavy $H_2$ when necessary. All partner total profiles are bounded. Hence summing the positive box comparisons bounds the **actual** curved boundary contributions by

$$
 O_{\rho,\kappa,A,b}\!\left(\mathfrak S(N)
                   (|I|\theta_N+NL^{-A})\right).
                                                               \tag{5}
$$

This is an outward bound on the exact signed boundary, not a replacement of its product cutoff. Use $A'\ge A+2K+8$ to absorb the at most $O(L^{2K})$ relevant pairs of labelled boxes; the good set is uniform in all of them.

On the stable boxes put $x_i=\log p_i/\log n$. The exact long mark is $\log n\, A_k(x)$ in (2); indeed the subsets above half are precisely the genuine long ones, since $\log n=L_N+O_\rho(1)$ and the stable margin dominates. Within any unit-log box the actual mark changes by at most $O_\kappa(1)$: the signed subset list stays fixed and each complementary log sum is linear in the individual logs. Weight the positive box count by the representative mark divided by $L$, a bounded multiplier not required to be positive. Both the actual and real pointwise mark errors are $O_\kappa(1/L)$ times the positive model weight. Their total is $O_{\rho,\kappa,A,b}(\mathfrak S(N)(|I|/L+NL^{-A}))$ after the positive count input and the same summation. This preserves the real signed profile of the rough stable leg to the required accuracy.

In these comparisons the local special factors are all $1+O(1/L_N)$, and any common frozen prime when at least one leg is rough is $\ge X^\kappa$. The omitted common-cofactor weight is at most $O_{\rho,\kappa}(L^{2K+2}\sum_{\ell\ge X^\kappa}\ell^{-2})$, again by the prescribed divisor weight bounds of §1. The exact local model therefore factors as $\mathfrak S(N)$ times the product of the ordinary one-leg profiles up to negligible errors, for all pairings having a rough slot. For two old slots use [R58](r58-source-central-three-factor-first-order.md) directly. The old active profiles sum with their original signs to $\Delta+O_\rho(\theta_N)$, and an admissible-giant old triprime and a prime leg have their actual zero orbits as before. Against a stable rough slot the other leg's own cutoff is the only remaining divisor rule because $de>Q$ already passes.

For each rough $k$ the stable one-leg profile is $c_{k,\kappa}+O_{\rho,\kappa}(\theta_N)$ uniformly in real $t\in I_0$. The proof is the compact-exponent comparison of [R59](r59-source-fixed-rough-four-prime-central.md): the frozen coordinates have reciprocal prime measure, the last real exponent is $\xi-\sum_{j<k}x_j$, all contributing exponents are bounded away from zero by $\kappa$, and replacing $\xi=1+O(1/L_N)$ and the stable boundaries by the limiting half planes costs $O_\kappa(\theta_N+1/L_N)$ over finitely many proper-subset/lower-endpoint strips. (For a lower-endpoint strip use the same free-coordinate argument, including for the last slot.) The mark divided by the last logarithm becomes $A_k(x)/x_k$ at $\xi=1$. On the unclipped fixed domain, split frozen axes into a mesh of side $L_N^{-1/(10K)}$. Prime Mertens gives discrepancy $O_\kappa(L_N^{-1})$ per hard reciprocal interval; the finitely many boundary hyperplanes have total mass $O_\kappa(L_N^{-1/(10K)})$ by conditioning on a free coordinate. Elsewhere the mark and density are bounded and piecewise Lipschitz, varying by $O_\kappa(L_N^{-1/(10K)})$ on boxes. The tensor error summed over at most $O(L_N^{(k-1)/(10K)})$ elementary boxes is negligible. Unit deletions in frozen polynomial slots and repetitions lose a power of $X$. Thus the profile constant is the $(k!)^{-1}$-normalized integral in (2), without choosing a sort order or double-counting a slot.

These estimates give (3) for pure rough, for rough with old in both orders, and for the rough arities at least four with either partner. The remaining pairings follow by additive expansion of the disjoint $\mathcal U_\kappa$ union or by the old [R58](r58-source-central-three-factor-first-order.md) theorem. Products use the original external minus in (1). All exceptional sets can be joined over the finitely many analyses while preserving their stated size.

## 3. Summing the signed profiles by a convolution identity

The measures

$$
    \mathcal M_\kappa=\sum_{j\ge0}\frac{(-1)^j}{j!}K_\kappa^{*j},
     \qquad
    \mathcal B_\kappa=\sum_{l\ge0}\frac1{l!}K_\kappa^{*l}
$$

are locally finite, with finitely many nonzero indices on each bounded interval, since a single factor is supported at $t\ge\kappa$. Group the signed divisor subsets of (2) by their length $j$, and their complement by length $l$. Symmetric simplex integration turns $\binom{j+l}{j}/(j+l)!$ into $1/(j!l!)$. The long subset has sum $1-t>1/2$, and its complementary mark is $t$. The all-factor subset $t=0$ contributes zero; the empty long subset is never selected. By convolution over the two sums, integrating against the short complementary measure therefore gives exactly

$$
        C_\kappa=\int_{[0,1/2)} t f_-(1-t)\,\mathcal B_\kappa(dt),
                                                               \tag{6}
$$

where $f_-$ is the density of $\mathcal M_\kappa$ off zero. This uses the very same $\frac1{k!}$ simplex normalization as the ordered arithmetic counts; the sign $(-1)^j$ is on the **long** subset. There is no atom on the half boundary.

For completeness the Dickman density used in the companion midpoint calculation follows here from its defining convolution. Multiplication by the total variable distributes it across the convolution factors, so termwise
$t\mathcal M_\kappa(dt)=-((tK_\kappa)*\mathcal M_\kappa)(dt)$, with $tK_\kappa(dt)=\mathbf1_{t\ge\kappa}\,dt$. With $R(t)=\mathcal M_\kappa([0,t])$, this says $R(t)=1$ on $0\le t<\kappa$ and $tR'(t)=-R(t-\kappa)$ a.e. for $t>\kappa$. Continuity off zero and stepwise integration give $R(t)=\rho_{\rm D}(t/\kappa)$, hence $f_-(s)=-\rho_{\rm D}(s/\kappa-1)/s$ at $s>1/2$ (where it is continuous). Substituting in (6) gives (4). The Dickman function is strictly positive and nonincreasing: $u\rho_{\rm D}(u)=\int_{u-1}^u \rho_{\rm D}(v)\,dv$ for $u\ge1$ follows from its delay equation, and a first zero would contradict the positive preceding integral. The same identity gives $\rho_{\rm D}(u)\le\rho_{\rm D}(u-1)/u$, hence the factorial bound $\rho_{\rm D}(u)\le1/\lfloor u\rfloor!$. Finally $\mathcal B_\kappa([0,1/2])\le\exp(\int_\kappa^{1/2}dt/t)=1/(2\kappa)$ by dropping the total-sum restriction in each nonnegative convolution term. Since $t/(1-t)\le1$ on the integration range, this proves the upper bound; the positive mass on $(\kappa,1/2)$ gives strict negativity of $C_\kappa$.

The optional low-factor splice has a simple rate. In the two-prime limit $A_2(x)=-\min(x_1,x_2)$ off equality, so $c_{2,\kappa}=-\log(2(1-\kappa))$. For three primes the only contribution to the limiting integral is when all exponents are at most $1/2$, with mark $+1$; outside that set the giant composite-cofactor orbit cancels. The full integral at $\kappa=0$ is $\pi^2/12$ from [R55](r55-source-all-small-triprime-comparator.md). The removed corner $0<x_i<\kappa$ has its other two exponents in $[1/2-x_i,1/2]$, an interval of thickness $x_i$ in one free coordinate, and their reciprocal product is $4+O(x_i)$. The three corners are disjoint for $\kappa<1/4$, giving $c_{3,\kappa}=\pi^2/12-2\kappa+O(\kappa^2)$ after division by six. Therefore

$$
 \gamma_{\mathcal U_\kappa}
   =C_\kappa+\log(1-\kappa)+2\kappa+O(\kappa^2)
   =\kappa+O(\kappa^2)
$$

by the factorial bound. In particular the self and mixed coefficients involving $\mathcal F_\kappa$ tend to zero as $\kappa\downarrow0$, as does the self coefficient of $\mathcal U_\kappa$. More explicitly, first fix $\kappa$ and let $X\to\infty$ on the good moduli of (3), measuring uniformly in $I$ after division by $\mathfrak S(N)N$; then the resulting rough-self and rough--old upper bounds are at most $|C_\kappa|^2$ and $|C_\kappa|\Delta$, respectively, and may be sent to zero by taking $\kappa\downarrow0$. The exceptional sets and implied constants depend on $\kappa$. The fixed-power rough selectors are **not** the original $\log N$-rough selectors. No diagonal limit in $\kappa(N)$, all-modulus bound, other arithmetic sectors, or Hypothesis S follows.
