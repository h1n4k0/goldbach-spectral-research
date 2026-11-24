# Pointwise cancellation of the critical-prime shell on a low-radical family

**Scope.** This estimates the actual dense critical-prime Type II shell, in a fixed proportional complementary divisor range. The true squarefree, coprimality, unit, and moving hard gates are retained. The result is unconditional and pointwise on the stated low-radical family, including every sufficiently large power of two. It is not a bound for unrestricted radicals, polynomially wider divisor ranges, the other shells, or weak S.

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, and fix $C>1$. Use the true coefficients of the [critical-prime setup](weak-s-type-ii-critical-prime-least-prime-boundaries.md), with any of its original prime selectors $|E(u,v)|\le1$ and hard left cuts. In particular $P_{uv}=-E(u,v)\log v$ at the true prime products in the disjoint boxes, and $P(\alpha)=\sum_n P_ne(n\alpha)$, where $e(z)=\exp(2\pi i z)$. Write $J=[N-y,N/2)$, $N/2\le y\le9N/16$. The complete complementary coefficient is

$$
 D_m=\mathbf1_{m\in J}
        \sum_{\substack{dk=m,\ d\in I_d,\ k>t\\
                        (dk,N)=1,\ (d,k)=1}}
                    \mu(d)\mu^2(k),
 \qquad I_d\subset[X,CX],\quad t\ge N^{.49999}.
 \tag{1}
$$

Here $I_d$ is any actual hard interval and the $k$ gate may also include any independent hard interval. No auxiliary coefficient selector on $D_m$ is used.

Put $\mathcal Q=[.8X,.9X]\cap\mathbb P$, $\mathcal B=[-1/(10N),1/(10N)]$, and let $\omega(N)$ be the number of distinct prime divisors. Fix $0\le c<1/2$. Uniformly on the even targets satisfying $2^{\omega(N)}\le L^c$, the actual polynomial $D(\alpha)=\sum_m D_me(m\alpha)$ satisfies

$$
 \int_{\mathcal B}\sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}
                   |D(a/q+\beta)|^2\,d\beta
       \ll_{C,c} \frac{N}{L_2}.
 \tag{2}
$$

Consequently the original full signed shell, the shell with the two nonzero-numerator arrays centered separately at each $q,\beta$, and the zero-base even-lattice signed residual of the [endpoint theorem](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md) with averaging length $M=\lceil XL^2\rceil$ all have magnitude $O_{C,c}(N/\sqrt{L_2})$. The last assertion is about the signed sum of even-lattice hits, not a square bound on their individual compensated offsets. For each fixed $c>0$ the low-radical condition includes every fixed radical for all sufficiently large $N$; the stated case $c=0$ is vacuous for even $N$. No assumption about zeros of Dirichlet $L$-functions is made.

## 1. The signed ordinary square on multiples of one prime square

First remove the squarefree and $N$-unit indicators by introducing the auxiliary signed divisor sum

$$
 F_m=\mathbf1_{m\in J}\sum_{\substack{dk=m,\ d\in I_d\\ k\ {\rm in\ its\ true\ hard\ range}}}\mu(d).
 \tag{3}
$$

The $k$ range here includes the real strict condition $k>t$. The identity

$$
                 D_m=\mu^2(m)\mathbf1_{(m,N)=1}F_m
 \tag{4}
$$

is exact. Every term of (1) has squarefree $m$, and on that support both the squarefree $k$ condition and $(d,k)=1$ are automatic. The sequence $F_m$ is used on the nonsquarefree support only to bound the error of a finite approximation to (4).

For every prime $p$ we claim the uniform estimate

$$
                       \sum_{p^2\mid m}|F_m|^2
                  \ll_C \frac{N(1+\log p)}{p^2}.
 \tag{5}
$$

It also holds after inserting bounded weights of uniformly bounded variation in each divisor label and a bounded multiplier of the product $m$; constants may depend on the variation bounds.

To prove (5) for hard gates, expand the square. The terms with nonzero $\mu(a)\mu(b)$ have squarefree signed divisors $a,b\asymp_C X$. For fixed $a,b$ the real $m$ satisfying the physical and two cofactor gates form an interval $U(a,b)\subset J$, with the original strict or inclusive endpoints. Counting $m$ with $[a,b,p^2]\mid m$ in this interval gives the continuous main term $|U(a,b)|/[a,b,p^2]$ and an $O(1)$ floor error. We use this floor error only for $(a,b)>G$, where $G=p^2$. Its absolute total is

$$
 \ll_C\sum_{G<g\ll_C X}(X/g)^2\ll_C N/G.
 \tag{6}
$$

In the full continuous main, at fixed real $x\in J$ the allowed signed divisors form a single interval $I(x)$: intersect $I_d$ with the reciprocal cofactor range at $x$. For any interval $I$, the corresponding continuous signed form is

$$
 \sum_{a,b\in I}\frac{\mu(a)\mu(b)}{[a,b,p^2]}
 =\frac1{p^2}
   \sum_{\substack{p\nmid a' b'\\a',b'\ge1}}
   \frac{\mu(a')\mu(b')}{[a',b']}
       \big(\mathbf1_{a'\in I}-\mathbf1_{pa'\in I}\big)
       \big(\mathbf1_{b'\in I}-\mathbf1_{pb'\in I}\big).
 \tag{7}
$$

Indeed each squarefree $a$ is either $a'$ or $pa'$, and the forced local exponent in the lcm is always exactly two. The kernel $1/[a',b']$ is positive semidefinite, as follows by expanding $\gcd(a',b')=\sum_{r\mid a',b'}\varphi(r)$. Its interval vector with the coefficients $\mu(a')$ has uniformly bounded squared norm by the Dress–Iwaniec–Tenenbaum prefix estimate, in the [sharp ordinary energy proof](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy).

The same uniform bound holds for the interval vector $\mu(a')\mathbf1_{p\nmid a'}$. To see this, use the exact identity

$$
 \mu(n)\mathbf1_{p\nmid n}
       =\sum_{j\ge0:\,p^j\mid n}\mu(n/p^j).
$$

For each $j$, changing both coordinates by the factor $p^j$ scales the squared lcm norm by $p^{-j}$, and leaves an ordinary interval vector in $n/p^j$. Minkowski and $\sum_{j\ge0}p^{-j/2}\ll1$ prove the uniform coprime version. Applying this to both intervals on the right of (7) shows that the full continuous contribution is $O_C(N/p^2)$ after integrating over $x\in J$.

It remains to bound the actual and continuous contributions at $g=(a,b)\le G$ in absolute value. Put $a=g u,b=g v$, with $(u,v)=1$. Before relaxing any conditions, $g,u,v$ are squarefree and pairwise coprime, by squarefreeness of the original $a,b$. One has $u,v\asymp_C X/g$ and any admissible integer is $m=g u v r$ with $r\asymp_C g$. In particular, the condition $p^2\mid m$ implies either $p^2\mid r$, or $p\mid r$ and $p\mid guv$. In the first case the absolute count for fixed $g$ is $O_C((X/g)^2g/p^2)=O_C(N/(gp^2))$. If $p$ divides $u$ or $v$ and $p\mid r$, the same bound follows by counting the two required multiples separately. These estimates use the positive upper bounds for the relevant coordinates, so a multiple of $p$ up to $V$ costs at most $V/p$ and does not create a new floor error. If $p\mid g$ and $p\mid r$, the upper bound at fixed $g$ is $O_C(N/(gp))$, and this must be summed over $p\mid g$. Since $\sum_{g\le G,p\mid g}1/g\le (1+\log G)/p$, all small-$g$ actual counts cost $O_C(N(1+\log G)/p^2)$.

For the small-$g$ continuous part, the denominator $[a,b,p^2]$ is $g u v p^2$ if $p\nmid guv$, and $g u v p$ otherwise. The reciprocal sums in $u,v$ on their proportional ranges are $O_C(1)$, or $O_C(1/p)$ if that coordinate is required to be divisible by $p$. As above the case $p\mid g$ costs an extra $1/p$ upon summing the restricted harmonic $g$ sum. The interval length is at most $N$, so the total is again $O_C(N(1+\log G)/p^2)$. We may now subtract this part from the full main (7) and insert the actual small-$g$ count. This, (6), and $G=p^2$ prove (5) without taking absolute values of the large-$g$ signed main.

For the variation extension of (5), represent each bounded-BV label weight by a bounded total variation superposition of prefix indicators on its actual hard interval (finite summation by parts is sufficient). Then use Minkowski in the restricted coefficient square norm on $p^2\mid m$. A product multiplier of supremum at most one only contracts that norm after the coefficient is formed.

## 2. Exact removal of the large prime-square tail

Fix a small constant $B>0$, to be chosen in terms of $c$, and put $\delta=L^{-B}$. Retain the hard $d$ cut. Smooth the physical gate and all $k$ endpoints by weights $W(m/N),w(k/X)\in[0,1]$ inside the actual allowed intervals, equal to one except on layers of relative width $O_C(\delta)$. Choose smooth weights with normalized $j$-th derivatives $O_{C,j}(\delta^{-j})$ for $j\le4$ and bounded variation. Their supports are in fixed compact subintervals of $(0,\infty)$, since $m\asymp N$ and $k\asymp_C X$ whenever the term is nonempty. In constructing $w$, an artificial enclosing interval can be placed strictly beyond the possible $k$ range, for example $7X/(32C)\le k\le 3X/4$. This does not change the hard input before smoothing. Intervals shorter than twice the edge width may be entirely charged to the corresponding endpoint estimate. These choices follow from convolution with a fixed compact smooth kernel after shrinking each allowed interval inward by the kernel radius. Strict endpoints are respected by the support and do not require moving the actual hard cuts.

Let $F_m^{\rm sm}$ denote (3) with these weights, and $D_m^{\rm sm}$ the corresponding actual squarefree unit coefficient (4). The [genuine endpoint bounds](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md#3-removing-all-actual-endpoint-layers-in-the-signed-compensated-shell) give

$$
          \|D-D^{\rm sm}\|_2^2\ll_{B,C}N L^{-B}L_2+N^{3/4}.
 \tag{8}
$$

Here and below the coefficient square norm equals the full circle norm by Parseval.

Take $Z=\max(3,\log L)$, $P_Z=\prod_{p\le Z}p$, and define

$$
 D_m^{(Z)}
     =\mathbf1_{(m,N)=1}F_m^{\rm sm}
          \prod_{p\le Z}\mathbf1_{p^2\nmid m}.
 \tag{9}
$$

The mismatch with $D_m^{\rm sm}$ is supported on integers divisible by a square $p^2$ with $p>Z$, and is bounded pointwise by $|F_m^{\rm sm}|$. Thus (5) and the elementary prime upper bound on dyads give

$$
 \|D^{(Z)}-D^{\rm sm}\|_2^2
 \ll_C N\sum_{p>Z}\frac{1+\log p}{p^2}
 \ll_C N/Z .
 \tag{10}
$$

For the last inequality sum dyads and use $\pi(2V)\ll V/\log(2V)$ on each. Also $\|D^{(Z)}\|_2^2\ll_C N$, by (8), (10), and the sharp ordinary norm of $D$. The actual additive arcs are disjoint. Hence (8) and (10) bound by $O_{B,C}(N/L_2)$ the integrated squared differences on the full union of those arcs. The cutoff (9) is an approximation only with this explicitly proved ordinary norm error; no coefficient of the true (1) is dropped without it.

## 3. The finite square sieve on all nonprincipal characters

At each $q\in\mathcal Q$ and $\beta\in\mathcal B$, and for a Dirichlet character modulo $q$ extended by zero on nonunits, put

$$
       D_\chi^{(Z)}(\beta)=\sum_m D_m^{(Z)}\chi(m)e(\beta m).
$$

Expand the product in (9) by $\sum_{\ell\mid P_Z,\,\ell^2\mid m}\mu(\ell)$. We may restrict to $(\ell,N)=1$ because of the actual product unit condition. For each $\ell$ and each squarefree signed divisor $d$, split exactly by $s=(\ell,d)$; write

$$
                   d=s u,\qquad k=(\ell^2/s)b,\qquad (u,\ell)=1.
 \tag{11}
$$

The condition on $u$ together with $\mu(u)$ keeps $d$ squarefree and $\mu(d)=\mu(s)\mu(u)$. Equality (11) is equivalent to $\ell^2\mid dk$ on this exact stratum. Keep $(u,N)=1$ in its coefficient, and expand the remaining unit condition on $b$ as $\mathbf1_{(b,N)=1}=\sum_{h\mid(b,N)}\mu(h)$. This is an exact sum over squarefree $h\mid N$, with $b=h v$. No actual unit prime is removed from the sieve.

Separate the smooth physical factor and the short arc modulation by normalized log Fourier inversion. Define the smooth compact function $G_\beta(z)=W(e^z)e(\beta N e^z)$; then

$$
 W(dk/N)e(\beta dk)=\int_{\mathbb R}\widehat G_\beta(\tau)
                e(\tau\log(d/X)) e(\tau\log(k/X))\,d\tau .
$$

Our Fourier transform convention is $\widehat G(\tau)=\int G(z)e(-\tau z)\,dz$. The derivative bounds and $|\beta|N\le1/10$ give uniformly

$$
             \int_{\mathbb R}|\widehat G_\beta(\tau)|
                         (1+|\tau|)^2\,d\tau\ll_C \delta^{-4}.
 \tag{12}
$$

For example integrate by parts four times for $|\tau|\ge1$ on its fixed compact support; the remaining $(1+|\tau|)^{-2}$ tail is integrable.

For each $\ell,s,h,\tau$, the $u$ sum is an arbitrary coefficient character sum at the actual hard $d=s u$ cut with
weights $\mu(u)\mathbf1_{(u,\ell N)=1}e(\tau\log(su/X))$. Its coefficients have modulus at most one, lie in a fixed length $O_C(X)$ range, and each residue modulo $q$ occurs $O_C(1)$ times. Complete multiplicative orthogonality and Cauchy within each residue therefore give

$$
 \left(\sum_{\chi\bmod q}|U_{\ell,s,\chi}(\tau)|^2\right)^{1/2}
                 \ll_C \sqrt{q X}.
 \tag{13}
$$

The remaining $v$ sum is, up to constants of modulus at most one,

$$
 \sum_{v\in\mathbb N}\chi(v) w(v/V)e(\tau\log(v/V)),
        \qquad V=\frac{Xs}{\ell^2h}>0.
$$

For every **nonprincipal** $\chi\bmod q$ its absolute value is

$$
                 \ll_C\sqrt q\,\delta^{-2}(1+|\tau|)^2.
 \tag{14}
$$

Here is a uniform verification, including short scales $V$. For $w_\tau(z)=w(z)e(\tau\log z)$ on its compact positive support, its Fourier transform is bounded by
$O_C(\delta^{-2}(1+|\tau|)^2(1+|\xi|)^{-2})$. Use two integrations by parts and the fixed support away from zero. By Poisson summation in the classes modulo $q$, the completed character sum is

$$
 \frac Vq\sum_{j\in\mathbb Z}\widehat w_\tau(jV/q)
                        \sum_{r\bmod q}\chi(r)e(jr/q).
$$

The inner Gauss sum vanishes when $q\mid j$, including $j=0$, and otherwise has modulus $\sqrt q$. For any $x>0$, $x\sum_{j\ne0}(1+|j|x)^{-2}\ll1$, so (14) holds for every $V>0$. This is not an application of an unproved sharp conditional character bound.

For each tuple of factors the constant character multipliers are $\chi(\ell^2 h)$ and the signs all have modulus at most one. Minkowski in $\ell^2$ over nonprincipal characters, (12), (13) and (14) show

$$
 \left(\sum_{\chi\ne\chi_0}|D_\chi^{(Z)}(\beta)|^2\right)^{1/2}
       \ll_C \delta^{-6}\,q\sqrt X\,
                      3^{\pi(Z)}2^{\omega(N)} .
 \tag{15}
$$

Indeed the number of pairs $(\ell,s)$ with $\ell\mid P_Z,s\mid\ell$ equals $3^{\pi(Z)}$ and the literal unit inclusion has at most $2^{\omega(N)}$ terms. All factors are controlled uniformly even when the original cutoffs move with $N$. The restriction on the radical is used only through this count.

Since $Z=\log L$ for large $N$, Chebyshev's bound gives $3^{\pi(Z)}=L^{o(1)}$. Integrating the square of (15) over $\mathcal B$ and summing over $\mathcal Q$ thus gives

$$
 \int_{\mathcal B}\sum_{q\in\mathcal Q}\sum_{\chi\ne\chi_0}
                  |D_\chi^{(Z)}(\beta)|^2\,d\beta
       \ll_C N L^{-1+12B+2c+o(1)}
 \tag{16}
$$

on the stated family, using $|\mathcal Q|\ll X/L$, $q\asymp X$ and $|\mathcal B|=1/(5N)$. Fix, for example, $B=(1-2c)/24>0$. Then (16) is $O_{C,c}(N/L_2)$.

## 4. Return to the exact additive shell and the even-lattice sum

At a fixed $q,\beta$, let $B_q(\beta)=\sum_{q\mid m} D_m^{(Z)}e(\beta m)$. On the nonzero additive numerators this is a constant in $a$. Since $k\le X/2<q$, a term in this sum must have $q\mid d$. There are $O_C(1)$ such $d$ in $I_d$, $O_C(X)$ possible $k$ for each, and the underlying coefficient magnitude before summation over $d$ is at most one by (9). Hence $|B_q(\beta)|\ll_C X$, unconditionally. On the remaining unit residues, the exact Gauss expansion on the $q-1$ nonzero additive numerators gives

$$
 \sum_{a=1}^{q-1}|D^{(Z)}(a/q+\beta)|^2
  =(q-1)\left| B_q(\beta)-\frac{D_{\chi_0}^{(Z)}(\beta)}{q-1}\right|^2
      +\frac q{q-1}\sum_{\chi\ne\chi_0}|D_\chi^{(Z)}(\beta)|^2 .
 \tag{17}
$$

In particular the second term is the **exact** energy after subtracting the mean on nonzero numerators. The first term is bounded by the sum of twice $(q-1)|B_q|^2$ and twice $|D_{\chi_0}^{(Z)}|^2/(q-1)$. The integrated sum of the first bound is $O_C(N/L)$. For the latter use $D_{\chi_0}^{(Z)}(\beta)=D^{(Z)}(\beta)-B_q(\beta)$, $\sum_q 1/(q-1)\ll1/L$, and the full circle norm $O_C(N)$ of $D^{(Z)}$; the $B_q$ contribution is smaller. The R82 zero-numerator base was a distinct signed expression and is not being declared small by this constant-mode estimate.

Combine (17), (16), and the disjoint-arc norm transfer from (8)–(10) to obtain (2) for the original **hard** $D$. Unique factorization of the two disjoint prime legs and the elementary prime-counting upper bound give $\|P\|_2^2\ll N$. Hence Cauchy on the actual arcs bounds the signed full pairing by $O_{C,c}(N/\sqrt{L_2})$. Centering either array by its mean in the nonzero numerator coordinate is an orthogonal contraction there; this proves the same bound for the original separately centered covariance and, by (17) or contraction, the corresponding true centered complementary energy.

Finally, the endpoint theorem's exact parity-preserving compensation applies directly to this original signed sum and hard $D$. At $M=\lceil XL^2\rceil$ its signed residual differs from the original full shell by $O_C(N/L+N(X/M)^2)$, including the repeated zero offset. Thus the weighted even-lattice hit sum after exact removal of the zero-numerator base has the asserted signed bound. This proof neither estimates individual compensated offsets via squared moments nor makes any assertion for the broader Type II range beyond fixed $d/X$, or for other parts of the Goldbach kernel.
