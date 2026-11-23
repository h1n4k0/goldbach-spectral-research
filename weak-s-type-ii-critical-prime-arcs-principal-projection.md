# A signed principal projection at critical prime denominators

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $e(z)=e^{2\pi iz}$. Take actual prime inputs in the fixed proportional boxes $I_u=[.740X,.745X]$ and $I_v=[.715X,.720X]$, with any hard subintervals, $N/2<uv\le y\le9N/16$ and $(uv,N)=1$. Further selection by any $|E(u,v)|\le1$ is allowed. Write $P(\alpha)$ for their actual Fourier polynomial with weight $E(u,v)\mu(u)b_{\rm II}(v)$, where $\mu(u)=-1$ and the true $b_{\rm II}(v)=\log v$ on this subset. These primes lie in the actual no-exchange seam, as in [the fixed-box obstruction](weak-s-type-ii-fixed-prime-box-minor-l2.md).

Let $A>0$ be fixed, $P_0=\lceil A\rceil+10$, and $\mathcal D_A=X L^{2000P_0}$. Write $D_>(\alpha)$ for the actual complementary polynomial from [the signed-seam analysis](weak-s-type-ii-signed-seam-major-arcs.md), with original arbitrary hard $I_d$ and the extra lower cut $d\ge\mathcal D_A$:

$$
 D_>(\alpha)=\sum_{\substack{d\in I_d,\ d\ge\mathcal D_A\\(d,N)=1}}
     \ \sum_{\substack{k>t,\ N-y\le dk<N/2\\(k,dN)=1}}
       \mu(d)\mu^2(k)e(\alpha dk),
 \qquad t\ge N^{.49999}.
$$

This is the exact $\mu(d)\mu^2(dk)$ weight, since $\mu(d)$ already forces squarefree $d$. Cut $d<N^{.50001}/2$ before any partition, as it is automatic on the genuine support.

Let $\mathcal Q$ comprise the primes in $[.8X,.9X]$ and take all their reduced numerator arcs $a/q+\beta$, $|\beta|\le1/(10N)$. Distinct arcs are disjoint by the spacing at least $1/(.9X)^2$ of different reduced fractions. All primes on the $P$ leg are smaller than $q$, hence units modulo every $q\in\mathcal Q$. The **exact principal multiplicative-character projection** of $P$ on an arc is

$$
            P^{(0)}_q(a/q+\beta)=-\frac{P(\beta)}{q-1}.
$$

**Theorem.** Unconditionally and with effective constants, the complete-numerator signed contribution of $P^{(0)}_q D_>$ in these arcs obeys

$$
 \int_{|\beta|\le1/(10N)} \sum_{q\in\mathcal Q}
    \left|\sum_{a=1}^{q-1}
       P^{(0)}_q(a/q+\beta)D_>(a/q+\beta)e(-N(a/q+\beta))\right|\,d\beta
      \ll_A N L^{-A}.
$$

The absolute value is taken **after** the full numerator sum at each denominator. This identifies one genuinely signed term on the square-root scale, beyond every fixed-power denominator cutoff $N^\kappa$ with $\kappa<1/2$ in the [conditional near-square-root analysis](weak-s-type-ii-grh-near-square-root-arcs.md). It gives no estimate for $P-P^{(0)}_q$ paired with $D_>$, for the lower-$d$ part, or for other arcs. It does not give a bound on the full signed covariance.

## 1. The exact congruence produced by the numerator sign

For $q\in\mathcal Q$, define $A_q(\beta)$ to be the very same sum as $D_>(\beta)$ with $dk\equiv N\bmod q$ imposed. Finite geometric summation yields

$$
 \sum_{a=1}^{q-1} D_>(a/q+\beta)e(-Na/q)
                    =q A_q(\beta)-D_>(\beta).
$$

This remains true if $q\mid N$, in which case $A_q=0$ by the unit mask. The formula for $P^{(0)}_q$ follows because the mean of $e(a r/q)$ over the unit residue $r$ is $-1/(q-1)$. Thus it suffices to prove, uniformly for the stated $\beta$,

$$
              \sum_{q\in\mathcal Q}|A_q(\beta)|\ll_A NL^{-A}.
$$

The baseline $D_>(\beta)$ is $O(N e^{-c(\log N)^{3/5}(\log\log N)^{-1/5}})$ from the $q=1$ case of the signed-seam major-arc theorem, which permits any hard $I_d$. Also $\sum_{q\in\mathcal Q}(q-1)^{-1}\ll1$ by the trivial integer count. Finally $|P(\beta)|\ll N/L$ by the prime number theorem in the two fixed proportional intervals and the single prime weight $\log v$. Integrating their product over the stated width proves the theorem once the congruence estimate has been established.

## 2. Freeze only the product wall and truncate the common divisor

On each dyad of actual $d$ scale $D_0$ partition $d$ into cells of relative width at most $\eta=L^{-40P_0}$. Keep the hard $I_d$, $\mathcal D_A$ and $d<N^{.50001}/2$ cuts exact. For a cell with left endpoint $d_0$ replace $N-y\le dk<N/2$ by $N-y\le d_0k<N/2$ and keep the independent $k>t$ cut unchanged. This gives $O(L^{40P_0+1})$ rectangles, with $d\asymp D_0$, $k\asymp K_0=N/D_0$ and products $m=dk\asymp N$, $N-m\asymp N$ on the original or enlarged support. The phase remains $e(\beta dk)$, even on a frozen rectangle.

Changed integer products are within $O(\eta N)$ of one of the two original product boundaries, hence number $O(1+\eta N)$. For each such $m$, the $d,k$ multiplicity is at most $\tau(m)$, and the number of congruence moduli in the actual shell is at most $\tau(N-m)$. Each pair has exactly one $d$ cell. Its weight is bounded by one. Consequently the total error over all moduli, including sharp endpoint changes, is

$$
  \ll (1+\eta N)^{1/2}
       \left(\sum_{m\asymp N,\ N-m\asymp N}\tau(m)^2\tau(N-m)^2\right)^{1/2}
  \ll (\eta N+1)^{1/2}\sqrt N L^8 .
$$

The divisor-moment estimate is Cauchy with the ordinary fourth moments. In particular this error does not acquire the number of cells as a factor.

On the frozen support expand $\mathbf1_{(d,k)=1}=\sum_{r\mid(d,k)}\mu(r)$ and truncate to $r\le B=L^{500P_0}$. An omitted term requires $r^2\mid m$ for some $r>B$; the corresponding products number $O(N/B)$ by summing $N/r^2$. The representation, common-divisor and congruence-modulus multiplicities are together bounded by $\tau(m)^2\tau(N-m)$. Cauchy and then the eighth and fourth divisor moments give a total error

$$
 \ll (N/B)^{1/2}
       \left(\sum_{m\asymp N,\ N-m\asymp N}\tau(m)^4\tau(N-m)^2\right)^{1/2}
       \ll NL^{68}B^{-1/2}.
$$

Both comparison errors are below $NL^{-A}$; they are evaluated on the exact signed summands before dispersing them.

## 3. Rebalance on the true long signed leg

On each retained squarefree $r$, necessarily $(r,N)=1$, put $d=rn,\ k=r\ell$. On the nonzero squarefree weights we keep $(n\ell,rN)=1$; the product of the three signs/weights is exactly

$$
           \mu(r)\mu(rn)\mu^2(r\ell)=\mu(n)\mu^2(\ell).
$$

The pivotal point is to put the common square into the **short** variable:

$$
      m=r^2\ell,\qquad n=d/r,\qquad mn=dk .
$$

Then the actual numerator remains $N$ in $mn\equiv N\bmod q$ and $M\asymp r K_0,\ U\asymp D_0/r$ satisfy $MU\asymp N$. The long coefficient is squarefree, odd, bigger than one, and a unit modulo $N$. It is not necessary for the short coefficient to be squarefree. All the masks and intervals on the two legs are independent of $q$.

For the true slow phase choose upper scales $M_*,U_*$ with $M_*U_*\ll N$ and $0<m/M_*,n/U_*\le1$ on these supports. Taylor separation is the exact absolutely convergent identity

$$
 e(\beta mn)=\sum_{j=0}^{\infty}
        \frac{(2\pi i\beta M_* U_*)^j}{j!}
          (m/M_*)^j(n/U_*)^j .
$$

Its coefficient $\ell^1$ norm is bounded absolutely since $N|\beta|\le1/10$. Each separated leg stays $1$-bounded; the long extra real power is monotone with variation at most one on its hard interval, uniformly in $j$.

With $Q\asymp X$ and $d\ge X L^{2000P_0}$ we have $Q/U\ll B L^{-2000P_0}=L^{-1500P_0}$, also $U\ll N^{.50001}$. Thus the input conditions of the [effective high-only centered dispersion estimate, §2](weak-s-type-ii-effective-fixed-power-seam-tags.md#2-a-high-only-centered-variance) hold for each $1$-bounded separated pair of coefficients, with $F_0=L^{10000P_0}$. The prime shell lies in one comparable modulus dyad and is allowed as a subfamily of the absolute high-projection discrepancy. For the actual prime $q\asymp X>F_0$, its entire low-conductor projection consists only of the principal character. The contribution from $q\mid N$ is zero and need not be included in the dispersion sum. The high estimate on the remaining actual moduli is

$$
 \ll N L^6 \sqrt{Q/U}+N F_0^{-1/2}+N^{1-\delta_0}
$$

for a fixed $\delta_0>0$, before the bounded Taylor coefficient norm and counting cells and $r$.

For the one low character, the effective ordinary masked Möbius bound on the long variable with mask $q r N$, as in [the masked Mertens argument](weak-s-type-ii-medium-prime-growing-tags.md#1-quantitative-reciprocal-l-bound-and-interval-m%C3%B6bius-sums), gives $O(U e^{-c\sqrt L})$ for all relevant prefixes, since $U\ge N^{.49}$ eventually. This is the unconditional principal bound there, not its nonprincipal GRH estimate. Abel summation with the monotone normalized powers preserves it uniformly in $j$. The short transform is $O(M)$, so summing the principal term with weights $1/(q-1)$ on the actual shell costs $O(N e^{-c\sqrt L})$ for each rectangle and $r$.

There are at most $O(L^{540P_0+1})$ external rectangle and $r$ choices. Summing all errors proves $\sum_{q\in\mathcal Q}|A_q(\beta)|\ll_A NL^{-A}$: the displayed $Q/U$ contributes $L^{-750P_0}$ after square root, the low-projection cutoff contributes $L^{-5000P_0}$, and fixed-power and exponential savings absorb all logarithms. This proves the claimed complete-numerator signed bound with no changed coefficient or cutoff inside the retained sum.
