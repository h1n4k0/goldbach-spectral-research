# A uniform lower bound for the true centered energy at the fixed critical-shell witness

Let $N$ be any even integer, $X=\sqrt N$, $L=\log N$, $R=\operatorname{rad}N$, $V=\varphi(N)/N$, and $e(z)=e^{2\pi iz}$. Use the genuine hard coefficient of [the fixed-cut complementary-energy example](weak-s-type-ii-critical-prime-sharp-complementary-energy-example-grh.md), now at every even $N$, with exactly

$$
 y=9N/16,\qquad I_d=[X,1.01X],\qquad
 I_k=(\max(N^{.49999},.42X),.50X).
$$

Thus

$$
 D_m=\mathbf1_{7N/16\le m<N/2}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                       (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_mD_m e(\alpha m).
$$

As usual $\mathcal Q=[.8X,.9X]\cap\mathbb P$. Let $\mathcal E_N^0(D)$ be the squared energy at $a/q+\beta$, $q\in\mathcal Q$, $1\le a<q$, integrated on $|\beta|\le1/(10N)$, after projection off the constant in each nonzero-numerator group.

**Theorem (global Dirichlet GRH).** Assume GRH for all primitive Dirichlet $L$-functions, including $\zeta$. Then for all sufficiently large even $N$,

$$
                   \mathcal E_N^0(D)\gg V^2\frac{N}{L}.               \tag{1}
$$

No radical cap is imposed and the entire original unit condition is retained. This is a lower bound for one actual centered **energy** at the indicated hard cuts, not for a signed pairing, a compensated offset, or Hypothesis S. No optimality in the dependence on $V$ is asserted.

## 1. The conditional transfer on these fixed cuts

Use the exact inward smoothing $\delta=L^{-2}$ and arithmetic approximation of [the hard transfer, §1](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#1-actual-transfers-at-the-smaller-smoothing-width). Write $\Omega$ for its physical weight in $x=m/N$, and $w(k)$ for its true short weight. The coherent finite character completion is that of [the square-label proof, §1](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#1-complete-the-square-only-after-adding-the-square-labels), with square cutoff $T=L^{16}$ and finite $h\le H_0=\exp(C_0(1+\log L)^2)$ dividing $R$. Its rational-only cutoffs restore all $h\mid R$. A term of the resulting physical rational vector at reduced nonzero rational $\rho$ is

$$
 \frac{N\mu(l)\mu(s)\mu(h)\mu(u)}{q l^2hu}
       \int_{\mathbb R}\Omega(x)e(\beta Nx)w(Nx/(su))e(-\rho Nx/q)\,dx ,
                                                                        \tag{2}
$$

where $l\le T$ is squarefree, $(l,N)=1$, $s\mid l$, $su\in I_d$, $(u,lN)=1$, $h\mid R$, and $\rho l^2 h u$ is a nonzero integer. Sum all such terms to define $\mathcal R_{q,\beta}(\rho)$. Let $\mathscr D_N$ be its squared norm summed over $\rho\ne0$, weighted by $q(q-1)$, summed over $q$ and integrated in $\beta$.

We record the conditional comparison on these cuts, to make the argument independent of any new assertion about wider intervals. In the finite character array of the coherent completion, the common residue is $v=l^2hu/j\bmod q$ with all $l,h,j$ units at $q$. There are no $q$-divisible long $d$ on $I_d$: $q<X$ and $2q\ge1.6X>1.01X$. Thus $q\nmid u$ and the artificially added residue-zero term is zero. The artificially added principal square is $\sum_q q|\sum_{v\ne0}\mathcal S_q(v)|^2$, with $\mathcal S_q$ the finite array. Sum over $v$ to factor the long and short transforms. The masked GRH Möbius bound $O((X/s)^{4/5})$ for the long sum applies at additive frequency zero; the short absolute mesh sum is $O(1+L+|\tau|)$, with $|\tau|\le L^4$. All $l,s$ counts and the time-weight norm are fixed-polylogarithmic, and the $h$ count is at most $H_0=N^{o(1)}$. Hence the artificial principal is $O(N^{9/5+o(1)})$ before beta integration. Subtract it by finite multiplicative Parseval, just as in [the lower-bound transfer on the same cuts, §3](weak-s-type-ii-critical-prime-sharp-complementary-energy-example-grh.md#3-subtract-the-artificial-term-and-return-to-actual-numerator-energy). The new $h$ count is why the loss here is written $N^{o(1)}$, rather than a fixed logarithmic power.

The nonzero determinant is $O(N^{1.91}L^{O(1)})$ by the same coherent GRH estimate, uniformly in $\beta$. The true squared nonprincipal character sum changes by the factor $q/(q-1)=1+O(X^{-1})$ for additive energy; it acts on positive norms after the subtraction. The coherent rational norm is $O(N^2/L)$ before $\beta$ integration by [the paired-label bound, §2](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#2-factor-the-common-rational-denominator-before-the-square-label-sum). The established rational-only $\tau,j,h$ restoration and ordinary sampled truncations have negligible log errors with a sufficiently large fixed $C_0$. Thus the centered energy of the smoothed approximate coefficient is $\mathscr D_N+O(NL^{-3})$ after integration. Disjoint arcs and centering contract the true hard-approximation squared error $O(NL^{-2})$; its cross term with energy $O(N/L)$ is $O(NL^{-3/2})$. We conclude on these exact cuts that

$$
                   \mathcal E_N^0(D)=\mathscr D_N+O(NL^{-3/2}).       \tag{3}
$$

The rational lower bound below is independent of GRH; its transfer (3) is conditional.

## 2. Reduced rational coordinates with the exact unit weight

Fix a sufficiently large constant $B$ to be chosen, and write $I=[1.002X,1.008X]$. Use integers $c\in I$ that are squarefree, coprime to $R$ and free of primes at most $B$. For every $n\mid R$ take the coordinates

$$
 \rho=\frac{a}{nc},\qquad 1\le a\le n,\qquad (a,nc)=1.
$$

These fractions are reduced and distinct for distinct triples $(n,c,a)$: $n$ is the exact part of the reduced denominator supported on $R$. In (2), since $l,u$ are true $N$-units and $(c,R)=1$, the integrality condition is precisely $n\mid h$ and $c\mid l^2u$. In this full analytic rational sum the $h$ weights therefore factor as

$$
       \sum_{\substack{h\mid R\\n\mid h}}\frac{\mu(h)}h
               =\frac{\mu(n)V}{\varphi(n)} .                         \tag{4}
$$

There is no change to the finite modular labels in §1.

For $l\le B$, prime avoidance by $c$ forces $c\mid u$. Then $su\in I_d$ forces $u=c$ and $s=1$, since $c>X$ and twice $c$ exceeds the upper endpoint. The low-$l$ part of this rational coordinate is thus

$$
 \frac{\mu(c)\mu(n)V}{\varphi(n)}\,
      \frac{N}{qc}
      \sum_{\substack{l\le B\\(l,N)=1}}\frac{\mu(l)}{l^2}
      \int\Omega(x)e\!\left((\beta N-aN/(qnc))x\right)\,dx .          \tag{5}
$$

Here $w(Nx/c)=1$ on the support of $\Omega$ for all large $N$, because $Nx/c$ stays a fixed proportional distance inside $(.42X,.50X)$. The finite sum is at least $1-\sum_{j\ge2}j^{-2}>0$. The real frequency in the last exponential has absolute value less than $1.35$ since $a\le n$; on a support interval of length $1/16$, rotating by the midpoint bounds the absolute integral below by a fixed multiple of $\int\Omega\gg1$. Also $N/(qc)\asymp1$ and the signs outside have modulus one. Consequently (5) has modulus at least $c_0 V/\varphi(n)$ for an absolute $c_0>0$, uniform in all labels and in $q,\beta$.

For $l>B$ put $r=(c,l)$. Because $c$ is squarefree, the exact condition $c\mid l^2u$ means $(c/r)\mid u$. Set $u=(c/r)v$. For each $s\mid l$, $su\in I_d$ restricts $v$ to an interval of ratio $1.01$ and scale $\asymp r/s$, so its absolute reciprocal sum is $O(1)$, even for intervals near or below one. From $1/u=r/(cv)$ and the absolute integral bound in (2), the modulus of the full higher-$l$ part is at most

$$
       C_1\frac{V}{\varphi(n)}\mathcal T_B(c),\qquad
       \mathcal T_B(c)=
           \sum_{\substack{B<l\le T\\(l,N)=1}}
                        \frac{\tau(l)(c,l)}{l^2},                    \tag{6}
$$

for an absolute $C_1$. Crucially (4) was taken out before measuring this tail. Let a denominator be bad if $\mathcal T_B(c)>c_0/(2C_1)$. This definition has no dependence on $q,\beta,n,a$.

## 3. The uniform count of good numerator-denominator pairs

First average (6) over all $N$-units in $I$. For each $l$ in (6), expand the gcd as $\sum_{d\mid(c,l)}\varphi(d)$. Since $(l,N)=1$, the number of such $c$ divisible by a fixed $d\mid l$ is at most $O(XV/d+\tau(R))$, by finite unit inclusion after writing $c=db$. Therefore

$$
 \sum_{\substack{c\in I\\(c,N)=1}}(c,l)
                  \ll XV\tau(l)+l\tau(R)
$$

using $\sum_{d\mid l}\varphi(d)=l$. Summing this in (6), the number of bad $N$-units is at most

$$
                    O(XV B^{-3/4})+X^{o(1)}.                       \tag{7}
$$

Indeed $\sum_{l>B}\tau(l)^2/l^2\ll B^{-3/4}$ by a fixed divisor-function exponent $1/8$, and the sum of the floor term costs only a fixed power of $L$ times $\tau(R)=X^{o(1)}$.

Next fix $n\mid R$ and count initially without removing the bad $c$. Write $Q_B=\prod_{p\le B}p$, and define

$$
 \mathfrak d(M)=\zeta(2)^{-1}\prod_{p\mid M}(1+1/p)^{-1},
             \qquad \omega_0(a)=\prod_{p\mid a}(1+1/p)^{-1}.
$$

For each reduced unit $1\le a\le n$, $(a,n)=1$, the number of squarefree $c\in I$ coprime to $RQ_Ba$ is $|I|\mathfrak d(RQ_Ba)+O_B(X^{1/2+o(1)})$. This is the elementary square-divisor expansion and finite unit count: on a mask $M$, the floor error over square divisors is $O(\tau(\operatorname{rad}M)\sqrt X)$ and the density tail costs $O(\sqrt X)$. Here $RQ_Ba\le Q_BN^2$, so the error is uniform in $n,a$. The local factors yield

$$
       \mathfrak d(RQ_Ba)\ge \mathfrak d(R)\omega_0(Q_B)\omega_0(a)
                          \gg V B^{-1/2}\omega_0(a).                 \tag{8}
$$

Indeed $\mathfrak d(R)\asymp V$ by the absolutely bounded product of $(1-p^{-2})^{-1}$, and $\sum_{p\le B}\log(1+1/p)\le\frac12\log B+O(1)$ by bounding the sum over odd primes by that over all odd integers.

We need the absolute uniform elementary bound

$$
       \sum_{\substack{1\le a\le n\\(a,n)=1}}\omega_0(a)
                                       \gg\varphi(n)                 \tag{9}
$$

for every $n\mid R$. To see it, average $\sum_{p\mid a}1/p$ over these reduced units. For $p\le n^{1/3}$, $p\nmid n$, the number of such $a$ with $p\mid a$ is $\varphi(n)/p+O(\tau(n))$ by finite inclusion on $a/p\le n/p$. The small-prime contribution to the average is $O(1)+O(\tau(n)\log(2n)/\varphi(n))=O(1)$, because $n$ is squarefree, $\varphi(n)\gg\sqrt n$, and $\tau(n)\ll n^{1/4}$. Larger primes contribute at most $3n^{-1/3}$ on each $a\le n$. The case $n=1$ is immediate. Since $\omega_0(a)\ge\exp(-\sum_{p\mid a}1/p)$, Jensen's inequality yields (9).

By (8)–(9), before discarding bad denominators the number of pairs for each $n$ is $\gg XV B^{-1/2}\varphi(n)$, apart from $O_B(X^{1/2+o(1)}\varphi(n))$. Each bad denominator costs at most $\varphi(n)$ such pairs. Choose $B$ fixed so large that the $B^{-3/4}$ term of (7) is less than half the absolute leading lower bound at $B^{-1/2}$, then take $N$ sufficiently large to absorb all floor errors uniformly using $V\gg(1+\log L)^{-1}$. The latter bound follows from the ordinary Mertens product up to $L^2$ and the $O(L)$ possible remaining prime factors. Thus for every $n\mid R$ there are $\gg_B XV\varphi(n)$ good pairs.

For each resulting reduced coordinate (5) dominates the tail (6) by the definition of good $c$, so $|\mathcal R_{q,\beta}(a/(nc))|\gg V/\varphi(n)$ uniformly. The coordinates for different triples are distinct. The positive rational sum is therefore

$$
 \sum_{\rho\ne0}|\mathcal R_{q,\beta}(\rho)|^2
       \gg XV^3\sum_{n\mid R}\varphi(n)^{-1}
       =XV^2 ,
$$

using the exact product $\prod_{p\mid R}(1+1/(p-1))=V^{-1}$. After the $q(q-1)$ weights, the ordinary count of shell primes $\gg X/L$, and the $\beta$ integration, this is $\mathscr D_N\gg V^2N/L$. The error in (3) is smaller since $V\gg(1+\log L)^{-1}$. This proves (1) without a conclusion about signed pairings.
