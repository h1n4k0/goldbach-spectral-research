# A growing prime-parity family detects coherent transport

**Scope.** The finite tagged tests in the [joint-parity construction](spectral-joint-parity-transport.md) can all be preserved by an artificial one-sided transport onto its zero-tag reservoir. A polynomially growing family of genuine individual prime-divisibility parity signs cannot: its aggregate signed defect is at least twice the erased mass. This family is within the unconditional Bombieri–Vinogradov level for the true sequence. If the receivers are allowed to be arbitrary genuine squarefree composite partners, a pointwise cap gives the same detection up to a smaller, explicitly bounded balanced-semiprime loss. The results concern parity marginals, not the parity of the total factor count, and do not give a lower bound for prime-pair mass.

Let $N$ be a sufficiently large even integer, $L=\log N$, $S=\mathfrak S(N)$, $m=N-n$, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. As in the [coherent transport](spectral-coherent-divisor-transport-barrier.md), fix $J\ge1$ and use its half-open central cells $I\subset(N/2,9N/16]$ of length $H=N/(16\lceil L^J\rceil)$. Thus $m\asymp N$, $m<N$, and every prime $n$ in the cell is a unit modulo $N$. Fix a sufficiently small constant $\beta>0$, put $z=N^\beta$, and let $\mathcal T$ be the union of the old R43 prime bands (only their upper exponent bound $.41$ is needed below). For a fixed $B>0$ define

$$
 D=\sqrt{N}\,L^{-B},\qquad
 \mathcal R=\{r\text{ prime}:z\le r\le D,\ r\nmid N,\ r\notin\mathcal T\}.
$$

For all large $N$, every old tagged prime is below $D$. The old primes are primes $p<z$ and the primes in $\mathcal T$. A partner prime $m$ is above $D$ and does not meet any old prime or any $r\in\mathcal R$.

## 1. True parity marginals are available at full precision

For $r\in\mathcal R$, define $\pi_r(m)=(-1)^{\mathbf1_{r\mid m}}$ and $A_r(\lambda)=\sum_{n\in I}\lambda(n)\mathbf1_{r\mid N-n}$. The progression for $A_r$ is exactly $n\equiv N\bmod r$, a reduced residue. Given $A>0$, [maximal Bombieri–Vinogradov for primes in progressions](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=206), for $B=B(A)$ sufficiently large, gives uniformly for the cells

$$
 \sum_{r\in\mathcal R}\left|A_r(\lambda)-\frac{H}{r-1}\right|
       \ll_A NL^{-A}.                                      \tag{1}
$$

Indeed a cell is a difference of two actual prefixes. The use of prime-only $\lambda$ instead of von Mangoldt costs at most $O(D\sqrt N L^2)$ in the aggregate, absorbed by enlarging $B$. The restriction to the particular prime set $\mathcal R$ only drops nonnegative errors. These are equivalent to centered parity marginal data: if $M_I(\lambda)=\sum_{n\in I}\lambda(n)$, then the $\pi_r$-mass of the cell is $M_I(\lambda)-2A_r(\lambda)$. Centering at the actual cell total avoids multiplying its error by the number of primes. Thus both signed observables and their $\ell^1$ precision are exact at the stated unconditional level.

## 2. Detection with a strict one-sided transport

Let $\widetilde\lambda$ be obtained by removing nonnegative weight of total mass $P$ from prime-partner positions in this cell, then depositing mass $P$ nonnegatively on genuine prime positions with squarefree composite partners. The symbol $P$ can be the entire actual prime-partner mass, as in the earlier transports, but it need not be. Suppose the deposit preserves every old divisibility marginal. Then it is supported on $z$-rough partners with no tagged prime: for each old prime, none of the removals was divisible by it, so every nonnegative deposit at a position divisible by it would change its marginal. Primes dividing $N$ cannot divide any actual partner. This is the only use of the preservation requirement; it holds directly for the R43 all-zero receiver.

Let $\eta(n)\ge0$ be the deposited weight, $\Delta_r=A_r(\widetilde\lambda)-A_r(\lambda)$, and let $b_D(m)=\#\{r\in\mathcal R:r\mid m\}$. Then

$$
 \Delta_r=\sum_{n\in I}\eta(n)\mathbf1_{r\mid m}\ge0,\qquad
 \sum_{r\in\mathcal R}\Delta_r=\sum_{n\in I}\eta(n)b_D(m).     \tag{2}
$$

The absolute change of the $\pi_r$-mass is $2\Delta_r$, since the cell total is unchanged. Also $b_D(m)\le M=\lfloor1/\beta\rfloor$ whenever $m<N$, by multiplying the distinct factors at least $z$. If each receiver has at least three prime factors, its least prime is at most $m^{1/3}<D$ and hence belongs to $\mathcal R$. Thus $b_D(m)\ge1$ on the entire receiver. In particular the R43 all-zero receiver (more than $K\ge2$ factors) satisfies

$$
 2P\le
 \sum_{r\in\mathcal R}\left|
   \sum_{n\in I}(\widetilde\lambda-\lambda)(n)\pi_r(N-n)\right|
 \le 2MP.                                                   \tag{3}
$$

Every contributing least prime is below $N^{1/3}$. Thus, for this high-factor conclusion alone one can restrict $\mathcal R$ further to $r\le N^{1/3}$, still use (1), and get the same (3). The centered aggregate can also be read from a single bounded real test $\beta b_D\in[0,1]$, which changes by at least $\beta P$.

## 3. Allowing arbitrary composite receivers: the balanced exception

Suppose instead that the arbitrary squarefree composite deposits are subject to the pointwise cap $0\le\eta(n)\le C_{\rm cap}\lambda(n)$ for a fixed $C_{\rm cap}$. Since old factors and primes dividing $N$ are excluded on receivers, $b_D(m)=0$ requires that every prime factor of $m$ exceed $D$. For large $N$, $D^3>N$; such a squarefree composite must be $m=rq$ with primes $D<r<q$ and $r\le\sqrt N$.

Let $E_I$ be the true $\lambda$-mass of all these balanced semiprime positions, whether or not they have any old factors. Fix a least prime $r$ in this range. It is coprime to $N$, or there is no genuine prime $n$ in the cell on that progression. The cofactor $q$ runs in an interval of length $U=H/r$. To majorize the number of primes $q$ with $N-rq$ also prime, apply the dimension-two upper sieve to $q$ and $N-rq$ at $Y=U^{1/100}$ with level $U^{1/2}$. Here $\log U\asymp L$, and both primes and the coefficient $r$ exceed $Y$ for all sufficiently large $N$. For primes below $Y$, there are two excluded roots unless the prime divides $N$, when there is one. In particular $2$ has one root. The local product is

$$
 \prod_{\ell<Y}\left(1-\frac{\rho(\ell)}{\ell}\right)
 \ll \frac{S}{(\log Y)^2},
 \qquad
 \rho(\ell)=
 \begin{cases}
  1,&\ell\mid N,\\
  2,&\ell\nmid N.
 \end{cases}
$$

This follows by factoring out $\prod_{\ell<Y}(1-1/\ell)^2$ and using Mertens, with the product of the correcting factors $(\ell-1)/(\ell-2)$ for odd $\ell\mid N$ bounded by the corresponding full singular-series factor. The dimension inequality is uniform since $\rho(\ell)\le2$ at odd primes and the root count at $2$ is one. By the [fundamental upper sieve](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/), the count is $O(SU/L^2+U^{1/2}\log(2U))$: the error per squarefree modulus $d$ is $O(2^{\omega(d)})$ by the CRT, and their sum up to $U^{1/2}$ gives the indicated remainder. Restrictions such as $q>r$ may be dropped for this upper bound, by counting the passing positions in the full cofactor interval.

Multiply by $\lambda(n)\le L$ and sum over $D<r\le\sqrt N$. The power remainder is $O(N^{3/4}L^2)$, using $\sqrt H\sum_{r\le\sqrt N}r^{-1/2}\ll N^{3/4}$. The reciprocal sum of primes in this range is $O_B((1+\log L)/L)$: cover the range by $O_B(1+\log L)$ intervals with ratio at most two, and use the elementary upper prime count in each to get $O(1/L)$ per interval. Since the power error is negligible uniformly in the cells, the result is

$$
 E_I\ll_{B,J} \frac{S H(1+\log L)}{L^2}.                     \tag{4}
$$

The deposited weight on the invisible part is at most $C_{\rm cap}E_I$. For the remaining receivers, $b_D(m)\ge1$. Consequently the lower bound in (3) becomes $2\max\{0,P-C_{\rm cap}E_I\}$, with the same upper bound.

It follows from (1)–(4) that if the transported weights themselves satisfy an estimate of the form (1) for this enlarged set of coherent prime moduli, then

$$
 P\ll_A NL^{-A}\quad\text{for high-factor receivers},\qquad
 P\ll_{A,B,J,C_{\rm cap}}
  NL^{-A}+\frac{SH(1+\log L)}{L^2}
  \quad\text{for arbitrary squarefree composite receivers}. \tag{5}
$$

Here $B$ is chosen for the prescribed $A$, not a single $B$ for all $A$. For $A>J+3$, the second bound is strictly smaller than the conjectural raw prime-partner scale $SH/L$. This is a restriction on the artificial transport if required to match more data; it does not establish that the true erased mass has the conjectural size.

## 4. What signed reallocation would have to add

The one-sided support and sign assumptions are real. For example, allow a signed change $\eta$ on genuine old-zero, $z$-rough squarefree composite positions, still with net deposit $P$ and with $\eta^+\le C_{\rm cap}\lambda$. Write $P_-=\sum_n\eta^-(n)$. The donor removal contributes zero to every new marginal, and by the same support test,

$$
 \sum_{r\in\mathcal R}\Delta_r
   =\sum_n\eta(n)b_D(N-n)
   \ge P-(M-1)P_--C_{\rm cap}E_I.                           \tag{6}
$$

In fact the visible positive mass is at least $P+P_--C_{\rm cap}E_I$, and the negative part can subtract at most $MP_-$. In the high-factor class, set $E_I=0$ in this inequality. So preserving both true and transported BV precision requires additional negative composite mass at least $\max\{0,P-C_{\rm cap}E_I-O_A(NL^{-A})\}/(M-1)$ for $M>1$. This is only a necessary condition, not a construction or an impossibility result for two-sided transport.

The growing family sees a least prime that the finite old bands may miss. Neither its true marginal evaluations nor its transport defect estimates $\mu(m)$ or $(-1)^{\omega(m)}$ on the genuine sequence. There is no implication here for Hypothesis S or central Goldbach positivity.
