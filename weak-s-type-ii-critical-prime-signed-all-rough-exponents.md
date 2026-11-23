# Signed critical-boundary energy at every fixed positive stretched-exponential exponent

Keep the original even $N$, $L=\log N$, $L_2=\log L$, $X=\sqrt N$, the true hard prime polynomial $P$ with any fixed $|E(u,v)|\le1$ and active gate $N/2<uv\le y\le9N/16$, and the [three exact least-prime boundary branches](weak-s-type-ii-critical-prime-least-prime-boundaries.md). Thus $d\in I_0=I_d\cap[X,\infty)$, $k>t\ge N^{.49999}$, $N-y\le m=dk<N/2$, $(m,N)=1$, and the genuine coefficient is $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$. For $p=P^-(m)$ the three branches are, respectively, $p\mid d$ and $d/p$ fails the lower endpoint; $p\mid k$ and $pd$ fails the upper endpoint; and $p\mid k$, $pd\in I_0$, $k/p\le t$. Every true hard endpoint is retained.

Fix $0<\gamma<1$, set $Z=\exp(L^\gamma)$, and write $\lambda=\log Z$. For a squarefree integer $s$, let $r_Z(s)$ be the product of its prime factors strictly below $Z$. With $1\le R<Z$ and $2\le W<Z$, let $D_{Z,R,W}$ be the true signed sum of all three boundary branches restricted by $r_Z(d)\le R$ and $p\le W$. There is no restriction on rough arity, no extra near-balance constraint on $d$ or $k$, and no assumption about the target's omitted small primes. Unconditionally and uniformly in the sharp cuts,

$$
\int_0^1 |D_{Z,R,W}(\alpha)|^2\,d\alpha
 \ll_{\gamma} \frac{N(1+\log R)^3(1+\log W)(1+L_2)}{\lambda}.
\tag{1}
$$

Consequently its full and double-centered signed pairings with $P$ on the whole critical-prime shell are bounded, in total, by

$$
O_\gamma\!\left(N\sqrt{\frac{(1+\log R)^3(1+\log W)(1+L_2)}{L^\gamma}}\right).
\tag{2}
$$

For all fixed polylogarithmic $R$ and $W$, this is $o(N)$ for every fixed $\gamma>0$, strengthening the [unsigned coefficient second moment](weak-s-type-ii-critical-prime-stretched-rough-boundary-second-moment.md) at $\gamma>1/3$. More generally it saves for $\log R=L^\theta$, $\log W=L^\omega$ with fixed $\theta,\omega>0$, $3\theta+\omega<\gamma$. The crucial distinction is to keep the true Möbius signs in the small-lcm main contribution.

## 1. Fix the whole small part of the complementary product

At a true squarefree $m$ write $m=bv$ where $b=r_Z(m)$, so $b$ is squarefree and supported on primes below $Z$, and $v$ is squarefree with all prime factors at least $Z$. The condition $p\le W<Z$ means $b>1$ and $p=P^-(b)$, unique for this $b$. For every retained divisor set $r=r_Z(d)$; then $r\mid b$, $r\le R$, and

$$
d=ra,\quad k=(b/r)c,\quad ac=v .
$$

The signed summand has weight $\mu(r)\mu(a)$ on true support. The original gcd and squarefree masks are automatic there from squarefreeness of $m$, and $(m,N)=1$ stays until after squaring. Define $T_R(b)=\sum_{r\le R,\ r\mid b}1$. Distinct $b$ have disjoint $m$ support. For each $b$, Cauchy across $r$ gives a factor $T_R(b)$ outside the sum of the signed squares for individual $r$; across the three branches there is a further factor at most three.

The part $b>N^{1/10}$ costs $O_{\gamma,J}(NL^{-J})$ for any fixed $J$. Indeed at each coefficient the absolute bound is $T_R(b)\tau(v)$, and $\sum_{v\le Y}\tau(v)^2\ll Y(1+\log Y)^3$ follows from $\tau(v)^2\le\tau_4(v)$ and the elementary divisor hyperbola estimate. With $\delta=1/\lambda$,

$$
\begin{split}
\sum_{\substack{b>N^{1/10}\\ b\ {\rm squarefree},\,P^+(b)<Z}}
 \frac{T_R(b)^2}{b}
&\le \exp(-L/(10\lambda))
 \sum_{\substack{b\ {\rm squarefree},\,P^+(b)<Z}}\frac{T_R(b)^2}{b^{1-\delta}}\\
&\ll \exp(-L/(10\lambda))\,\lambda(1+\log R)^3 .
\end{split}
\tag{3}
$$

To see the last estimate expand both divisors $r,r'$, write $j=[r,r']$, and impose $j\mid b$. One has $j^\delta\le R^{2/\lambda}\le e^2$. The remaining Euler product is at most $\prod_{\ell<Z}(1+\ell^{-1+\delta})\ll\lambda$ over primes: comparison to $\delta=0$ costs a bounded factor since $\sum_{\ell<Z}(\ell^\delta-1)/\ell\ll\delta\sum_{\ell<Z}(\log\ell)/\ell\ll1$. Also $\sum_{r,r'\le R}\mu^2(r)\mu^2(r')/[r,r']\le\prod_{\ell\le R}(1+3/\ell)\ll(1+\log R)^3$. The identical zero-shift estimate gives

$$
\sum_{\substack{b\ {\rm squarefree},\,P^+(b)<Z}}\frac{T_R(b)^2}{b}
 \ll \lambda(1+\log R)^3 .
\tag{4}
$$

For $b\le N^{1/10}$ put $Y=N/b\ge N^{9/10}$. The true $v$ lies in a fixed hard interval $\Omega\subset[7Y/16,Y/2)$. For each $r,p$ and branch the original conditions on $a,c$ are intervals in the two coordinates separately, inherited by the substitutions $d=ra$, $k=(b/r)c$. By the failed lower/upper tests, $d$ lies in a fixed interval of ratio at most $p$ for branches 1/2; in branch 3 the corresponding narrow fixed interval is $t<k\le pt$. Splitting the signed divisor sum at $a\le\sqrt v$ and exchanging $a,c$ on the other part preserves $\mu$ of the now short variable up to a common factor of modulus one, since $\mu(a)=\mu(v)\mu(c)$ on squarefree $v$. This split costs at most two upon squaring. In either orientation the short divisor is $>1$ and in fact at least $N^{.39}$ for sufficiently large $N$: one had $d/r\ge X/R$ and $k/(b/r)\ge t/b$, and $R<Z=N^{o(1)}$.

After squaring one such signed sum one may drop the common unit/squarefree restrictions from $v$ for an upper bound by adding nonnegative squares at all $Z$-rough $v$ in $\Omega$. The sum to be estimated is

$$
\sum_{\substack{v\in\Omega\\v\ {\rm integer},\ Z\text{-rough}}}
 \left|\sum_{a\mid v,\ a\in J(v)}\mu(a)\right|^2 .
\tag{5}
$$

Here each $J(v)$ is an exact interval inside $(1,\sqrt v]$ (strict at the complemented boundary), and for each fixed integer $a$ its test defines an interval in $v$. All $J(v)$ lie in a common fixed envelope $[H/(Cp),H]$, where $H\le\sqrt Y$ and on a nonempty piece $H\ge N^{.39}$. Indeed if the fixed narrow coordinate was exchanged, use $v\asymp Y$ and its reciprocal to obtain the new narrow envelope. Intersecting this envelope with the automatic short upper bound $\sqrt Y$ cannot increase its ratio. Nothing is rounded in the actual intervals.

## 2. Inputs for a fixed signed square

Write $V(Z)=\prod_{\ell<Z}(1-1/\ell)\asymp1/\lambda$ over primes and $U_p=1+\log p$. The [uniform rough-count proof](weak-s-type-ii-critical-prime-stretched-rough-boundary-second-moment.md#1-absolute-dyadic-rough-count-including-the-small-endpoint) gives $O(B/\lambda)$ $Z$-rough integers greater than one up to $B\ge Z$, by summing dyads. For their reciprocal sums a real interval of ratio $O(p)$ costs $O(U_p/\lambda)$ after excluding the atom $1$; including it costs $O(1+U_p/\lambda)=O(1)$. For ratio $O(pQ)$ the same bound is $O(1+(\log p+\log Q)/\lambda)$.

We use the [signed rough harmonic argument](weak-s-type-ii-critical-prime-signed-boundary-energy.md#2-rough-harmonic-control-and-an-elementary-rough-density) with the real fixed cutoff $Z$ (remove primes strictly below it). For any fixed $D$ one can choose $\Xi=Z^{C_{\gamma,D}(1+L_2)}=N^{o(1)}$ so that every prefix above $\Xi$ of $\sum_{a\ Z\text{-rough},\ (a,g)=1}\mu(a)/a$ is $O_{\gamma,D}(L^{-D})$, uniformly for $g\le N$ and the prefix endpoint at most $N$. Indeed the ordinary harmonic Mertens sum is convolved with reciprocals of $Z$-smooth numbers. In the half with smooth multiplier $\le\sqrt u$, the ordinary effective Mertens bound yields $O(L^{-D})$ at $u\ge\Xi$. In the other half, shift $1/\lambda$ and use the Euler product $O(\lambda)$ and $\exp(-\log u/(2\lambda))$. Excluding primes dividing $g$ that are at least $Z$ costs $O(L^2/(Z\lambda^2))$, because there are at most $L/\lambda$ such primes and the free rough reciprocal sum up to $N$ is $O(L/\lambda)$. Differences of prefixes apply to arbitrary endpoint conventions for intervals entirely above $2\Xi$.

For ordinary rough counts in any hard real interval $A$ of nonnegative values use the even/odd Bonferroni truncations at orders $j,j+1$ with $j\asymp_D (1+L_2)$ even and sufficiently large. This gives

$$
\#\{z\in A:z\text{ a positive }Z\text{-rough integer}\}
 =V(Z)|A|+O_D(|A| L^{-D}+Z^{j+1}).
\tag{6}
$$

The two truncated densities differ by at most $(\sum_{\ell<Z}1/\ell)^{j+1}/(j+1)!\ll_D L^{-D}$. The floor error is $O(Z^{j+1})$ since all retained squarefree divisors are at most $Z^{j+1}$. Take $Q=Z^{2(j+2)}=Y^{o(1)}$. For $[a,b]\le Y/Q$ the integer $v=[a,b]z$ in (5) requires $z$ in a real interval because the fixed-$a,b$ endpoint tests are intervals. The rough count gives the main term $V(Z)/[a,b]$ times the interval length in $v$, with error $O(Y L^{-D}/[a,b])$, since $Y/[a,b]\ge Q$. Summing its absolute error costs $O(Y L^{3-D})$ by $[a,b]=gxy$ with $a=gx$, $b=gy$, $g=(a,b)$.

## 3. Long-lcm correction: a nontrivial narrow rough gate

We bound the actual and continuous-model counts on $[a,b]>Y/Q$ separately, with weights made absolute only in this correction. Write $v=gxyz$ with $(x,y)=1$, so $[a,b]=gxy$. Then $1\le z<Q$, including the real continuous model, because $a,b\le\sqrt v$ gives $[a,b]\le ab\le v$. Moreover $x,y>1$ before relaxing any restriction: otherwise the lcm is one of the two short divisors and at most $\sqrt Y<Y/Q$. The retained two-sided gates are

$$
gx,gy\in[H/(Cp),H],\qquad
xz,yz\in[cY/H,C'pY/H]
\tag{7}
$$

for absolute constants. The last pair follows by dividing $v$ by the other short divisor. The largest variable is one of $g,x,y$ because $z<Q=Y^{o(1)}$ and $v\asymp Y$. For fixed other variables, its upper bound is $Y$ divided by their product; on any nonempty feasible tuple this upper bound is $\gg Y^{1/4}\gg Z$. Count that largest rough variable by $O(Y/\lambda)$ divided by the product of the other variables.

If $g$ is largest, keep $xz,yz$ and use both $x,y>1$. At fixed $z$ their two rough harmonic gates cost $O(U_p^2/\lambda^2)$. The free rough harmonic sum up to $Q$ in $z$ costs $O(1+\log Q/\lambda)=O(1+L_2)$. This gives $O(Y U_p^2(1+L_2)/\lambda^3)$.

If $x$ is largest, keep $gy,yz$. The shared variable $y$ lies in $[cY/(HQ),C'pY/H]$, so its free rough harmonic cost is $O(1+L_2)$. At fixed $y$, if at least one of $g,z$ exceeds one, that variable's narrow rough harmonic cost is $O(U_p/\lambda)$ and the other's cost including a possible $1$ is $O(1)$. In the actual discrete count $g=z=1$ cannot occur: then $v=xy$, both $x,y\le\sqrt v$ would force $x=y$, contrary to $(x,y)=1$ and $x,y>1$. Exclude this case before dropping coprimality. Hence the actual correction here costs $O(Y U_p(1+L_2)/\lambda^2)$. Largest $y$ is symmetric.

For the continuous model, change variables from $dv/[a,b]$ to $dz$ at fixed $g,x,y$; its density is $V(Z)$. Keeping the same gates and integrating over $z$ gives the same bounds: where $z$ is shared its harmonic integral with density is $O((\log Q)/\lambda)$; where it is gated its integral is $O(U_p/\lambda)$ whether or not $g=1$. Thus no use of discrete nonoccurrence of $g=z=1$ is needed here. Since $U_p\ll\lambda$, both entire corrections are $O(Y U_p(1+L_2)/\lambda^2)$.

## 4. The signed positive form, and summation

We can now use the full continuous signed lcm main term, charging the two corrections above. For each real $v\in\Omega$ its lcm form before multiplying by $V(Z)$ is exactly

$$
\sum_{\substack{g\le H\\g\ Z\text{-rough}}}
 \frac{\varphi(g)\mu^2(g)}{g^2}
 \left|\sum_{\substack{x\in J(v)/g\\x\ Z\text{-rough},\ (x,g)=1}}
                     \frac{\mu(x)}x\right|^2 .
\tag{8}
$$

This is $\gcd(a,b)=\sum_{g\mid a,b}\varphi(g)$ followed by completing the inner square, retaining the Möbius signs. If $g<H/(2Cp\Xi)$ all inner intervals lie above $2\Xi$; use the signed prefix estimate and the ordinary harmonic bound on $g$. For larger $g$ the allowed reciprocal sum in $g$ is $O(1+L_2)$ since the ratio is $O(p\Xi)$. The $x>1$ portion of each inner sum has absolute bound $O(U_p/\lambda)$, so its squared contribution is $O(U_p^2(1+L_2)/\lambda^2)$. Extract the atom $x=1$ using $|A+B|^2\le2|A|^2+2|B|^2$. It occurs only when $g\in J(v)$, where $g>1$ and its harmonic sum is $O(U_p/\lambda)$. Thus (8) is

$$
O\!\left(\frac{U_p}{\lambda}+\frac{U_p^2(1+L_2)}{\lambda^2}\right)
$$

up to a negligible power-log error. Integration over $\Omega$ with $V(Z)\asymp1/\lambda$, plus the two corrections and small-lcm error, yields a bound $O_\gamma(Y U_p(1+L_2)/\lambda^2)$ for (5).

Use $U_p\le1+\log W$ and the same bound for every small $b$ and allocation. Cauchy across the $T_R(b)$ allowed allocations therefore contributes at most $O_\gamma\big((N/b)T_R(b)^2(1+\log W)(1+L_2)/\lambda^2\big)$. Sum by (4), using disjoint $b$, and include (3). This proves (1) by Parseval. On disjoint arcs of radius $1/(10N)$ at all nonzero numerators of primes $q\in[.8X,.9X]$, restriction and separate numerator centering each contract $L^2$. The genuine prime-box energy is $O(N)$ by unique products and the prime upper bound (any fixed selector). Cauchy with the exact phase $e(-N\alpha)$ proves (2), with every alias and with no extra mod-$q$ filtering.

## 5. New genuine support and remaining gap

The growing-prime-count witness in the [preceding stretched-rough note](weak-s-type-ii-critical-prime-stretched-rough-boundary-second-moment.md#4-genuine-new-terms-absent-at-every-fixed-polynomial-rough-cutoff) works also for $0<\gamma<1/3$: its construction and quantitative prime number theorem need only $\gamma>0$. On $N=2^j$, it takes $d=3$ times $\asymp L^{1-\gamma}$ distinct primes near $\exp(2L^\gamma)$, $d\in[1.05X,1.061X)$, and a prime $k\in[.43X,.44X]$ with the stated unchanged sharp cuts. This is a true type-1 term with $p=r_Z(d)=3$, and it is absent for every fixed $\gamma'>1/3$ cutoff at polylogarithmic $R$. The witness is only support, not a lower bound for the signed covariance. The remaining $r_Z(d)>R$ sector at small $p$, the generic full critical covariance, and weak S remain open.
