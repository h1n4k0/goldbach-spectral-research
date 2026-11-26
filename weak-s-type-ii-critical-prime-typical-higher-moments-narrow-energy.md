# Smaller exceptional sets for unconditional hard rational transport, with a narrow energy witness

Use the actual complementary coefficient, centered critical-prime shell, and cutoff-free hard rational model of [the hard profile theorem](weak-s-type-ii-critical-prime-cutoff-free-rational-profile-grh.md). Thus $N$ is even, $X=\sqrt N$, $L=\log N$, $R=\operatorname{rad}N$, $V=\varphi(N)/N$, and

$$
 D_m=\mathbf 1_{N-y\le m<N/2}
     \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                     (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k).
$$

The genuine hard cuts satisfy $N/2\le y\le9N/16$, $I_d\subset[X,CXL^\gamma]$ with fixed $C>1,\gamma\ge0$, and $I_k$ includes the strict condition $k>t\ge N^{.49999}$. One may intersect with the automatic bounds $d<N/(2t)$ and $k<X/2$. The shell uses primes $q\in[.8X,.9X]$, nonzero numerators $1\le a<q$, and $|\beta|\le1/(10N)$. Let $\mathcal E_N^0(D)$ be the squared norm after subtracting the additive mean over these numerators at each $(q,\beta)$, and let $\mathscr H_N$ be the cutoff-free hard rational squared norm for these same cuts.

**Theorem.** For every fixed $A>0$ and $B>0$, there is $c>0$ such that for all sufficiently large $Y$, outside a set of at most

$$
                   O_{A,B,C,\gamma}\!\left(
                         Y\exp[-c(\log\log Y)^B]\right)             \tag{1}
$$

even targets in $[Y,2Y]$, one has unconditionally

$$
                \mathcal E_N^0(D)=\mathscr H_N+
                                  O_{A,B,C,\gamma}(NL^{-A})         \tag{2}
$$

simultaneously for all permitted hard cuts, with no radical cap. One can take the exceptional set also to accommodate the fixed narrow cuts

$$
     I_d=[X,1.01X],\qquad
     I_k=(\max(N^{.49999},.42X),.50X),\qquad y=9N/16 .
                                                                    \tag{3}
$$

On these cuts, for the same good targets, the actual centered energy satisfies

$$
                             \mathcal E_N^0(D)\gg V^2N/L.           \tag{4}
$$

For the rational model alone, $\mathscr H_N\gg V^2N/L$ on (3) for every sufficiently large even $N$, with no exception set. Taking comparison precision at least $A=2$ is sufficient for (4) and gives the known $O(N/L)$ centered-energy upper bound on all the admitted cuts on these good targets. The ordinary full energy has the same upper bound there by the [true additive constant bound](weak-s-type-ii-critical-prime-polynomial-width-true-constant-profile.md). These are energy estimates, not signed lower bounds, uniform all-target transport, or Weak S.

## 1. A high moment of the actual short-inclusion tail

Put $\mathcal L=\log Y$ and $v=\log\mathcal L$. The pointwise part of the [typical-target transport, §§1–4](weak-s-type-ii-critical-prime-typical-target-hard-rational-transport.md#1-average-the-actual-short-inclusion-tail-without-capping-the-retained-radical) requires the sole target statistic

$$
                  \mathcal T_N(H)=
                       \sum_{\substack{r\mid R\\r>H}}
                                      \frac{3^{\omega(r)}}r
                      \le \mathcal L^{-M},
       \qquad H=\mathcal L^Q .                                     \tag{5}
$$

Here $M$ is taken sufficiently large for the chosen ordinary smoothing, auxiliary square cutoff, and rational-restoration precision. The effect of $Q$ is only to set the fixed logarithmic ranges in the finite completion: the short mesh lower bound and modular label counts are then absorbed by choosing the dual cutoff and Davenport exponents later. In particular, after $M$ is fixed, any sufficiently large fixed $Q$ is allowed in that pointwise proof. Both uses of (5) are on the actual short inclusion and its analytical restoration, with the true long $N$-unit always present. No assumption on the radical is in the pointwise estimate.

Fix $0<\sigma<1$ and define the positive Euler product

$$
                W_N=\prod_{p\mid N}(1+3p^{-1+\sigma}).
$$

Since $R$ is squarefree, positive Rankin gives $\mathcal T_N(H)\le H^{-\sigma}W_N$. For real $s\ge1$ expand the positive divisibility product for $W_N^s$. Divisibility by each squarefree $d$ occurs at most $2Y/d$ times up to $2Y$, so

$$
  \frac1Y\sum_{Y\le N\le 2Y} W_N^s
       \le 2\prod_p
              \left(1+\frac{(1+3p^{-1+\sigma})^s-1}{p}\right).
                                                                    \tag{6}
$$

Allowing odd $N$ only increases the nonnegative sum. The product converges for every fixed $s$, and the bound needs no independence of divisibility events.

Write $P=s^{1/(1-\sigma)}$. At $p\le P$ the factor on the right of (6) is at most $(1+3p^{-1+\sigma})^s$. Its summed logarithm is at most $3s\sum_{n\le P} n^{-1+\sigma}\ll_\sigma s P^\sigma$. At $p>P$ one has $s p^{-1+\sigma}\le1$, so the logarithms sum to $O(s\sum_{n>P}n^{-2+\sigma})=O_\sigma(1)$. Thus there is a constant $C_\sigma$ such that

$$
 \log\left(\frac1Y\sum_{Y\le N\le2Y}W_N^s\right)
                         \le C_\sigma s^{1/(1-\sigma)}\qquad(s\ge1).
                                                                    \tag{7}
$$

Now take $Q\sigma>M+1$. Failure of (5) implies $W_N>\mathcal L^{Q\sigma-M}$. Put $b_0=Q\sigma-M>1$ and choose $s=(b_0 v/(2 C_\sigma))^{(1-\sigma)/\sigma}$, which is at least one for large $Y$. Markov's inequality and (7) give at most

$$
                     Y\exp\!\left[-(b_0/2) v s\right]
                       \le Y\exp[-c_{\sigma,Q,M}v^{1/\sigma}]        \tag{8}
$$

such targets. For any prescribed $B$ choose $\sigma$ with $1/\sigma>B$ and then take the corresponding fixed $Q$. This proves (1) and (2) by the pointwise transport at the desired precision. One may use $\max(A,2)$ for the precision and replace $C$ by $\max(C,1.01)$ as an internal upper bound, so that the resulting single exceptional set is independent of the cuts and covers (3) as well. Only the rarity estimate for the positive short-inclusion criterion changed relative to the preceding transport.

## 2. A lower bound for the literal hard rational model

Use the fixed cuts (3). Write $\Omega_0(x)=\mathbf 1_{[7/16,1/2)}(x)$, $w_0(k)=\mathbf 1_{I_k}(k)$, and $e(z)=e^{2\pi i z}$. First truncate the hard rational model only at $l\le T=L^{16}$, keeping all $h\mid R$. Its vector, denoted $\mathcal H_T$, is (1) of the hard profile with this finite set of square labels. For every $q,\beta$ we show

$$
       \sum_{\rho\in\mathbb Q\setminus\{0\}}
                     |\mathcal H_{T;q,\beta}(\rho)|^2\gg X V^2 .    \tag{9}
$$

We verify the [reduced-coordinate witness, §§2–3](weak-s-type-ii-critical-prime-all-even-centered-energy-witness-grh.md#2-reduced-rational-coordinates-with-the-exact-unit-weight) directly with the two literal hard weights. Let $B_1$ be a sufficiently large fixed constant to be chosen. Use squarefree $c\in I=[1.002X,1.008X]$ coprime to $R$ and free of primes at most $B_1$. For every $n\mid R$, take the reduced coordinates $\rho=a/(nc)$ with $1\le a\le n$ and $(a,nc)=1$. These fractions are distinct for all distinct triples $(n,c,a)$, since $n$ is recovered as the part of the reduced denominator supported on $R$. The integrality condition $\rho l^2 h u\in\mathbb Z\setminus\{0\}$ is exactly $n\mid h,\ c\mid l^2u$, because $l,u$ are $N$-units and $c$ is coprime to $R$. The $h$ signs in this analytic vector factor exactly:

$$
                  \sum_{\substack{h\mid R\\ n\mid h}}\frac{\mu(h)}h
                            =\frac{\mu(n)V}{\varphi(n)} .           \tag{10}
$$

No coprimality with the shell prime $q$ is needed in this rational equality.

When $l\le B_1$, necessarily $(l,c)=1$. Then $c\mid u$ and the true cut $su\in I_d$ force $u=c,s=1$. For all large $N$, $Nx/c$ stays strictly between the two endpoints of $I_k$ throughout $x\in[7/16,1/2)$: its ratio to $X$ is between $(7/16)/1.008$ and $(1/2)/1.002$. In particular $w_0(Nx/c)=1$. The contribution at such a coordinate from these low labels is therefore

$$
 \frac{\mu(n)\mu(c)V}{\varphi(n)}
    \frac{N}{qc}
     \left(\sum_{\substack{l\le B_1\\(l,N)=1}}\frac{\mu(l)}{l^2}\right)
     \int_{7/16}^{1/2} e\bigl((\beta N-aN/(qnc))x\bigr)\,dx .
                                                                    \tag{11}
$$

The squarefree condition in this low sum is automatic from $\mu$. The parenthesized sum is at least $1-\sum_{l\ge2}l^{-2}>0$. The real frequency has modulus at most $.1+1/(.8\cdot1.002)<1.35$, so rotation by the midpoint of the interval of length $1/16$ gives an absolute lower bound for the integral. Since $N/(qc)\asymp1$, (11) has modulus at least $c_0 V/\varphi(n)$ for some absolute $c_0>0$.

For $l>B_1$ set $r=(c,l)$. The exact condition $c\mid l^2u$, with $c$ squarefree, means $u=(c/r)z$ with positive integer $z$. The real interval $su\in I_d$ gives an interval of fixed ratio in $z$, with absolute reciprocal sum $O(1)$, including scales near one. With (10) already factored, the size of the remaining amplitude is at most

$$
     C_0\frac{V}{\varphi(n)}\,\mathcal U_{B_1}(c),\qquad
     \mathcal U_{B_1}(c)=
          \sum_{\substack{B_1<l\le T\\(l,N)=1}}
                       \frac{\tau(l)(c,l)}{l^2},
                                                                    \tag{12}
$$

where $\tau(l)$ counts positive divisors, $C_0$ is absolute, and the hard real integral was bounded absolutely. The exact signs and coprimalities may be relaxed only in this upper bound. A denominator is bad if $\mathcal U_{B_1}(c)>c_0/(2C_0)$.

Here are the uniform denominator and numerator counts. On $c\in I,\ (c,N)=1$, expand $(c,l)=\sum_{d\mid(c,l)}\varphi(d)$. For $(l,N)=1$ the number of these $c$ divisible by $d\mid l$ is $O(XV/d+\tau(R))$ by exact inclusion and a floor bound. This gives

$$
               \sum_{\substack{c\in I\\(c,N)=1}}(c,l)
                               \ll XV\tau(l)+l\tau(R).
$$

Summing in (12) and using $\tau(l)\ll l^{1/8}$, the number of bad $N$-unit $c$ is $O(XVB_1^{-3/4})+X^{o(1)}$. Indeed the main tail is $\sum_{l>B_1}\tau(l)^2/l^2\ll B_1^{-3/4}$, and the floor term, summed only to the **finite** $T=L^{16}$, is $X^{o(1)}$.

Put $P_1=\prod_{p\le B_1}p$ and $\omega_0(a)=\prod_{p\mid a}(1+1/p)^{-1}$. For each $a\le n$ with $(a,n)=1$, the number of squarefree $c\in I$ coprime to $RP_1a$ is

$$
 |I|\zeta(2)^{-1}\prod_{p\mid RP_1a}(1+1/p)^{-1}
                          +O_{B_1}(X^{1/2+o(1)}).
                                                                    \tag{13}
$$

This follows by the square-divisor expansion and the finite inclusion floor count for units; the mask is at most $P_1N^2$, so both the divisor-count floor and the omitted square-divisor tail are uniform. The listed density is $\gg V B_1^{-1/2}\omega_0(a)$ with an absolute constant: $\prod_{p\mid R}(1+1/p)^{-1}\asymp V$, and the reciprocal sum over all odd integers up to $B_1$ bounds $\sum_{p\le B_1}\log(1+1/p)\le \frac12\log B_1+O(1)$.

We have $\sum_{1\le a\le n,\,(a,n)=1}\omega_0(a)\gg\varphi(n)$ uniformly. Indeed the average of $\sum_{p\mid a}p^{-1}$ on these reduced units is $O(1)$: for $p\le n^{1/3}$ and $p\nmid n$, the count of those $a$ divisible by $p$ is $\varphi(n)/p+O(\tau(n))$ by inclusion. The errors after averaging total $O(\tau(n)\log(2n)/\varphi(n))=O(1)$ as $n$ is squarefree. Larger primes contribute at most $3n^{-1/3}$ per $a$, and $n=1$ is immediate. Apply Jensen to $\omega_0(a)\ge\exp(-\sum_{p\mid a}p^{-1})$. Thus by (13) the number of pairs before removing bad denominators is $\gg XV B_1^{-1/2}\varphi(n)$, with total floor error $O_{B_1}(X^{1/2+o(1)}\varphi(n))$. A bad denominator removes at most $\varphi(n)$ pairs. Choose $B_1$ large so the $B_1^{-3/4}$ loss is smaller than half the main factor at $B_1^{-1/2}$. All floor errors are negligible uniformly for large $N$, since $V\gg(1+\log L)^{-1}$ by the Mertens-product split at $L^2$. This gives $\gg_{B_1} XV\varphi(n)$ good pairs for each $n\mid R$.

For each good coordinate (11) dominates (12), giving modulus $\gg V/\varphi(n)$. These coordinates are disjoint over $n$. The resulting sum of squares is $\gg XV^3\sum_{n\mid R}\varphi(n)^{-1}=XV^2$ by the exact identity $\sum_{n\mid R}1/\varphi(n)=1/V$. This proves (9) for every $q,\beta$, with no GRH or exceptional-set hypothesis.

## 3. Remove the comparison label cutoff and return to actual energy

The rational norm at fixed $\beta$ uses weights $q(q-1)$ and the sum over nonzero rational coordinates. Summing (9) and using the prime number theorem in the fixed shell gives $\|\mathcal H_T\|_\beta^2\gg N^2V^2/L$. The unconditional [all-square-label hard tail, §2](weak-s-type-ii-critical-prime-cutoff-free-rational-profile-grh.md#2-an-all-square-label-estimate-independent-of-smoothing) gives

$$
                 \|\mathcal H-\mathcal H_T\|_\beta^2
                   \ll \frac{N^2}{L} L^3 T^{-1/2}
                    = O\!\left(\frac{N^2}{L}L^{-5}\right).
$$

Thus the norm triangle inequality transfers the lower bound to the all-label hard vector, uniformly in $\beta$; the tail is negligible compared with $V^2$ in these units. This use of the paired analytic estimate, not any sum of pointwise floor errors beyond $T$, removes the auxiliary square cutoff. Integration over the original length $1/(5N)$ yields $\mathscr H_N\gg V^2 N/L$ for every sufficiently large even $N$. Finally (2) at accuracy at least $A=2$ has smaller absolute error than this lower bound on the same good targets. This proves (4) for the genuine centered shell energy and only for that energy.
