# Unrestricted lower small factors and an above-typical middle band

Keep the true central fixed-target prime polynomial $P$ with arbitrary fixed $|E(u,v)|\le1$, its original hard product gate, and the three exact signed least-prime boundaries of the [unrestricted typical-count result](weak-s-type-ii-critical-prime-unrestricted-typical-small-part.md). Thus $N$ is even, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, $d\in I_0=I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le m=dk<N/2$, $(m,N)=1$, and the signed weight is $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. The original branches with $p=P^-(m)$ are: $p\mid d$ and its exchanged divisor fails the lower endpoint; $p\mid k$ and the exchanged divisor fails the upper endpoint; and $p\mid k$, $pd\in I_0$, $k/p\le t$. All exact tests and signs remain.

Fix $0<\gamma<\delta<1$ and $0<c<1/\log2$. Put

$$
Z_0=\exp(L^\gamma),\qquad Z_1=\exp(L^\delta),\qquad
\lambda_i=\log Z_i,\qquad R=\lambda_1/\lambda_0.
$$

For the true squarefree $m$ let $b_0$ and $b_1$ be its products of primes below $Z_0$ and in $[Z_0,Z_1)$, respectively. Keep all three true branches at $p\le W$, $2\le W<Z_0$, with the **only additional restriction**

$$
\omega(b_1)\le K=\lfloor c\log R\rfloor .
$$

There is no constraint on $\omega(b_0)$, on the size of either small part, on which primes in the middle band may occur, or on the allocation of any of these primes to $d$ versus $k$. Denote the resulting polynomial by $D_{\rm mid}$. Unconditionally, for each fixed $J>0$,

$$
\int_0^1|D_{\rm mid}(\alpha)|^2\,d\alpha
 \ll_{\gamma,\delta,c,J}
 N(1+\log W)^2(1+L_2)
 \left(
  \frac{\lambda_0^3 R^{\,1+c\log2}}{\lambda_1^2}
  +\frac{\lambda_0^4 R^{\,\eta(c)}}{\lambda_1^3}
 \right)+NL^{-J},
\qquad
\eta(c)=c(1+\log(4/c)).
\tag{1}
$$

For example $\gamma=1/8$, $\delta=3/4$, $c=21/20$ make both powers of $L$ inside the parentheses negative. For any fixed polylogarithmic $W$ the true full and double-centered signed pairings on the entire critical-prime shell are then $o(N)$ on every sufficiently large even target. The middle allowance in this example is above its typical count $\log R$ in the ordinary reciprocal Euler measure, and its actual middle factors need not be absent. This is not a bound for the completely unrestricted middle range.

## 1. The actual fixed-product signed estimate and negligible size tails

Write $b=b_0b_1=r_{Z_1}(m)$, $v=m/b$, and $Y=N/b$. At fixed $b\le N^{1/10}$ use the [signed fixed-$b$ short-divisor, lcm and atom estimates, §§2–4](weak-s-type-ii-critical-prime-unrestricted-typical-small-part.md#2-retain-the-signed-sum-of-all-allocations-at-fixed-small-part) with rough cutoff $Z_1$. These estimates precede its restriction on the total number of factors of $b$. For clarity, they fix one genuine branch and orientation, retain the signed sum across every $r=r_{Z_1}(d)\mid b$ before squaring, and approximate short lcms while retaining the signed $\mu$ factor on a large rough variable in the long correction. In the positive completed form they separate the common-divisor atom $x=1$. When two allocations share this atom, they satisfy $|\log(r/r')|\le\log(Cp)$, since the two true divisors are in the same branch interval at fixed $m$ (also in the complemented orientation). The remaining signed squared terms have the extra $1/\lambda_1$ from their nonunit rough gates. Thus with $U=1+\log W$, $B=\max(1,\log(CW))$, and

$$
A_b(B)=\#\{r,r'\mid b:|\log(r/r')|\le B\},
$$

the bound on the true squared coefficient sum at this $b$ is

$$
\ll_{\delta,D}
\frac{N}{b}\left(
  \frac{U A_b(B)}{\lambda_1^2}
 +\frac{U^2(1+L_2)4^{\omega(b)}}{\lambda_1^3}
 +L^{-D}4^{\omega(b)}
\right)
\tag{2}
$$

for any fixed $D>0$, with absolute $C$ enlarged if needed. All its rough size requirements persist: the genuine partners of $v$ satisfy $d/r\ge X/b$ and $k/(b/r)>t/b$, so both exceed $N^{.39}$. Restricting $b$ by the new count condition does not change any signed divisor sum at fixed $b$. The original squarefree and unit masks are retained until the nonnegative-square enlargement in the predecessor.

We can discard $b>N^{1/10}$ and, independently, the terms with

$$
\log b_0>T:=M\lambda_0(1+L_2)
\tag{3}
$$

for a sufficiently large fixed $M$, at squared cost $O_{\gamma,\delta,J}(NL^{-J})$. To see both assertions, use the absolute coefficient bound $\tau(b)\tau(v)$ and $\sum_{v\le x}\tau(v)^2\ll x(1+\log x)^3$. Distinct actual $b$ have disjoint integer support. A Rankin shift $1/\lambda_1$ in the reciprocal squarefree Euler sum for $4^{\omega(b)}$ handles the first tail, with factor $e^{-L/(10\lambda_1)}$ times $O(\lambda_1^4)$. For the second tail shift only the reciprocals of the below-$Z_0$ factors by $1/\lambda_0$, use $e^{-T/\lambda_0}$, and leave the middle Euler factors unshifted. This gives a bound

$$
\sum_{\substack{b_0,b_1\ {\rm squarefree\ in\ their\ bands}\\\log b_0>T}}
 \frac{4^{\omega(b_0)+\omega(b_1)}}{b_0b_1}
 \ll e^{-M(1+L_2)}\lambda_0^4 R^4 .
$$

The shifted product in each case differs from its zero-shift estimate by a bounded factor, since for $z=Z_i$, $\lambda_i=\log z$,
$\sum_{\ell<z}(\ell^{1/\lambda_i}-1)/\ell
 \ll\lambda_i^{-1}\sum_{\ell<z}\log\ell/\ell=O(1)$ by Chebyshev. The products here and below are over primes. The loose full fourth-weight Euler bound $O(\lambda_1^4)$ also absorbs all power-log errors from (2) by enlarging $D$.

## 2. Positive reciprocal count for the nonatom terms

Prime Mertens gives $\sum_{Z_0\le\ell<Z_1}1/\ell=\log R+O(1)$. The below-$Z_0$ factors receive no count tilt, so

$$
\sum_{\substack{b_0,b_1\ {\rm allowed}\\\omega(b_1)\le K}}
 \frac{4^{\omega(b_0)+\omega(b_1)}}{b_0b_1}
 \le
 \prod_{\ell<Z_0}(1+4/\ell)\,
 u^{-K}\prod_{Z_0\le\ell<Z_1}(1+4u/\ell)
 \ll_c\lambda_0^4 R^{\eta(c)},\qquad u=c/4 .
\tag{4}
$$

Here the size constraints may be dropped for a nonnegative upper bound. This is the second term in (1).

## 3. Close-allocation atom with a shifted middle log-bin estimate

Now keep the two size constraints for the atom. At fixed $b$ and $r,r'\mid b$, put each prime of $b$ in one of the four statuses: common, unused, only in $r$, only in $r'$. Denote the products in the last two statuses by $i=i_0i_1$ and $j=j_0j_1$, splitting at $Z_0$. Thus $r/r'=i/j$. Tilt by $2^{K-\omega(b_1)}$ on the true count range and drop coprimality between the status factors for an upper bound. The common and unused status products jointly cost

$$
\prod_{\ell<Z_0}(1+1/\ell)^2
 \prod_{Z_0\le\ell<Z_1}(1+1/(2\ell))^2
 \ll \lambda_0^2 R .
\tag{5}
$$

The factor from the middle tilt is $2^K\le R^{c\log2}$. The below-$Z_0$ differing factors $i_0,j_0$ have unweighted squarefree reciprocals, each with total at most $O(\lambda_0)$. Retain $i_0,j_0\le e^T$ from (3) and $i_1,j_1\le N$ from the true $b$ cap. The middle differing factors have reciprocal weights $f(n)/n$, where $f(n)=\mu^2(n)2^{-\omega(n)}$ on products of primes in $[Z_0,Z_1)$, zero elsewhere.

The elementary logarithmic divisor identity and Chebyshev, including the ordinary reciprocal bound for the supported primes, give for $x\ge Z_0$

$$
\sum_{n\le x} f(n)\log n
 \le \tfrac12\sum_{h\le x}f(h)\sum_{\ell\le x/h}\log\ell
 \ll x\prod_{Z_0\le\ell\le x}(1+1/(2\ell))
 \ll x\sqrt{\log x/\lambda_0}.
$$

Thus $\sum_{1<n\le x} f(n)\ll x/\sqrt{\lambda_0\log x}$ by treating $n\le\sqrt x$ trivially, and using the previous formula for the complementary part. There are no nonunit supported $n<Z_0$. On the log-axis, a unit-width bin at ordinate $s$ among nonunits therefore has harmonic weight $O(1/\sqrt{\lambda_0(1+s)})$ for $s\ge\lambda_0-1$. This bound also holds for the first possible partially occupied bin. As $B\ll U$ and $W<Z_0$, one has $B\le\lambda_0+O(1)$. For width-$B$ bins let $a_j$ be the reciprocal weight of the nonunits $n\le N$ in the $j$-th such bin. Summing the unit bins shows

$$
\sup_j a_j\ll B/\lambda_0,\qquad
\sum_j a_j^2\ll B(1+L_2)/\lambda_0 .
\tag{6}
$$

For the second bound one may use Cauchy within each width-$B$ bin, multiplying the sum of squared unit-bin weights by $O(B)$; a unit bin meets at most two of the width-$B$ bins, and the remaining harmonic sum in ordinates up to $\log N$ is $O(1+L_2)$.

Fix $i_0,j_0$. If both $i_1,j_1>1$, the near condition $|\log(i/j)|\le B$ only pairs bins with at most a fixed number of index offsets relative to the given real shift $\log(i_0/j_0)$. For each offset, Cauchy gives at most $\sum_j a_j^2$, uniformly even for large shifts. If exactly one of $i_1,j_1$ is $1$, the same condition selects only a bounded number of bins for the other, so use $\sup_j a_j$. Thus these cases cost $O(B(1+L_2)/\lambda_0)$ for each low pair. Summing the unrestricted low differing weights $O(\lambda_0^2)$ gives $O(B\lambda_0(1+L_2))$.

If $i_1=j_1=1$, it is the low differing factors alone that must be close in logarithm. For $i_0,j_0\le e^T$ their log bins of width $B$ each have ordinary reciprocal weight $O(B)$, even after dropping all prime masks. They have $O(1+T/B)$ bins and each bin has only boundedly many possible partners, giving $O(B(B+T))=O_M(B\lambda_0(1+L_2))$. This deals with the unit atoms without assuming a spurious $1/\lambda_0$ bound for them.

Combining the differing-factor sum with (5) and the count tilt proves

$$
\sum_{\substack{b\ {\rm retained\ in\ (2)-(3)}\\ \omega(b_1)\le K}}
 \frac{A_b(B)}b
 \ll_{\gamma,\delta,c,J} B(1+L_2)\lambda_0^3 R^{\,1+c\log 2}.
\tag{7}
$$

Inserting (4) and (7) into (2), using disjoint true small parts and Parseval, proves (1). Restriction to the disjoint critical arcs contracts the ordinary norm, and separate centering of each fixed-$q,\beta$ array over nonzero numerators contracts it again. The true prime box has squared norm $O(N)$ by unique oriented prime products in disjoint proportional boxes, even with the arbitrary fixed selector. Cauchy with the exact phase gives both true signed shell bounds, on every modulus, numerator and alias.

The two exponents in (1) are $3\gamma+(\delta-\gamma)(1+c\log2)-2\delta$ and $4\gamma+(\delta-\gamma)\eta(c)-3\delta$. At $\gamma=1/8,\delta=3/4,c=21/20$, they are less than $-.04$ and $-.21$, respectively. For the wide valid example no auxiliary target-specific restriction is required. In the normalized unweighted reciprocal Euler measure, $\omega(b_1)$ is a sum of independent Bernoulli variables with mean $\log R+O(1)$ and variance $O(\log R)$; this is the sense in which $c>1$ exceeds typical. None of this estimates the actual high-middle-count complement.

## 4. Actual high lower count with nonempty above-typical middle count

Here is a support witness on $N=2^j$, using the preceding explicit parameters and $W=3$. Set $K_0=\lfloor 3L_2\rfloor$ and choose two distinct primes per low cell on the exponent grid

$$
\theta_i=\gamma i/(K_0+1),\qquad [\exp(L^{\theta_i}),4\exp(L^{\theta_i})],
$$

starting at some sufficiently large fixed index and ending at $K_0$. The cells are disjoint and below $Z_0$ for all large $N$: the ratio of successive lower-endpoint logarithms tends to $e^{\gamma/3}>1$, skipping a fixed initial part makes adjacent lower endpoints differ by a factor exceeding $4$, and the last lower logarithm is asymptotic to $e^{-\gamma/3}L^\gamma$. Apply Bertrand twice in each cell. Allocate one prime of each low cell to each side and append $3$ to the $d$ side.

For the middle band take $K_1=\lfloor(26/25)(\delta-\gamma)L_2\rfloor$ primes, one in each factor-$4$ cell of the analogous exponent grid $\gamma+(\delta-\gamma)i/(K_1+1)$, $1\le i\le K_1$. These disjoint cells lie in $[Z_0,Z_1)$ by the same endpoint calculation (their successive lower logarithms have limiting ratio $e^{25/26}$). Allocate all these primes to $d$. Then $\omega(b_1)=K_1$ is strictly above $\log R$ by a positive proportion for large $N$, but is below $(21/20)\log R$.

Let $r,s$ be the resulting exact small products on $d,k$. Their logarithms are $O(L^\delta L_2)=o(L)$. Choose distinct primes $g,h>Z_1$ by the prime number theorem in proportional intervals so that $d=rg\in[1.05X,1.06X]$, $k=sh\in[.43X,.44X]$. With the actual cuts $I_0=[X,2X]$, $t=N^{.49999}$ and $y=9N/16$, this is a true squarefree unit product with $p=3$ and $d/3<X$, hence a genuine nonzero branch-1 summand.

For any fixed older one-scale exponent $\gamma'\le\gamma$, the low cells with exponents below $\gamma'/2$ already contribute $(24\gamma'+o(1))L_2$ prime factors on both sides jointly to the old exact small part. For $\gamma'>\gamma$ all the low cells contribute $(6+o(1))L_2$ joint factors. Both bounds exceed the earlier one-scale unrestricted total-count cap $\gamma' L_2/\log2$ for large $N$. Per side they also exceed the older slot caps. For the $d$ side, the two exponent grids together have a prime at an exponent in any fixed interior subinterval of $(\gamma'/3,\min(\gamma',\delta))$ not meeting $\gamma$, eventually. Thus the old magnitude bound $\log R_{\rm old}=O(L^{\gamma'/3})$ fails for every fixed $\gamma'\in(0,1)$. The middle primes are present, so this is not a true-gap construction. These are support statements only, not a signed lower bound. The general high-middle-count contribution, remaining dense critical covariance and weak S are not resolved.
