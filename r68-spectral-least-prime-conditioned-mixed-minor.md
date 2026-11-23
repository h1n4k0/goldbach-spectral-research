# Least-prime-conditioned signed energy for the actual mixed minor

**Scope.** On genuine largest-prime slices of the above-BV central mixed strip, both squarefree Möbius parities now reach every fixed exponent $0<\gamma<1$ in the threshold $P_*=\sqrt N\exp(-(\log N)^\gamma)$. Previously the whole-parity bound reached $\gamma<3/4$, with $\gamma<1$ only for odd total parity. More generally, the bound below allows a moving $s=o(L/L_2^6)$ in $P_*=\sqrt N e^{-s}$, for example $s=L/L_2^7$. It treats the actual mixed coefficient and its actual minor-arc integral, not only the modeled coefficient. The full bound is unconditional; the minor bound uses historical Dirichlet GRH for the two prime progression sums as before. There is no estimate here on the remaining smaller-largest-prime mixed minor, in particular its fixed polynomial regimes.

Keep $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, fixed $B>B_0>0$, $Q=N^{1/1000}$, and $V=[N/3,2N]$. Take $L_2^4\le s$ with $sL_2^2=o(L)$. Let $A(m)$ denote the true squarefree mixed coefficient $M_>(m)$ supported on the LCM $h>H_0$, restricted to $m\in V$ and $P^+(m)>P_*$. One may additionally select either $\mu(m)=+1$ or $\mu(m)=-1$. Use the same central hard half-open interval $I$, left weight $\omega$ with bounded supremum and variation, genuine prime polynomial $P_{I,\omega}$, and minor arcs $\mathfrak m$ as in the [previous rough-shell estimate](r67-spectral-rough-short-shell-energy.md). With $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$, we prove

$$
\begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
  &\ll \Sigma(N)|I|\,sL_2^6/L^2 + N^{.76},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)
                         e(-N\theta)\,d\theta\right|
  &\ll \Sigma(N)|I|\,sL_2^6/L^2 + N^{1-10^{-4}} .
\end{split} \tag{1}
$$

In particular the Hardy normalization $L/N$ gives $o(\Sigma(N))$ for $s=o(L/L_2^6)$. Bounds involving $sL_2^2=o(L)$ are understood eventually along the specified sequence, with $B,B_0$ and the weight bounds fixed.

## 1. Exact gates and cofactor selection

Use the same largest-prime extraction $m=pk$, with $p>P^+(k)$ and $p>P_*$. The identity $M_>=-\Xi_D-M_\le$ is exact before applying any estimates. By the [subpower proof](r66-spectral-subpower-largest-prime.md), only $D<k\le2\sqrt N e^s$ need be retained. The prime $k$ case and the low mixed subtraction $M_\le$ have reciprocal majorant sums $O(s/L)$ and $O(sL_2^5/L)$, respectively, before multiplication by $k/\varphi(k)$, as in the [integrated proof](r66-spectral-integrated-short-cutoff.md). Its odd-total-parity bound still applies verbatim with this moving sublinear $s$: the required estimates are $\eta^2\log(2Z)\ll1$, $s\ge L_2^4$, $Z=N^{o(1)}$, and a polylogarithmic number of cells, where $\eta=s^{-1/2}$ and $Z=10e^{2s}$. We work on composite squarefree $k$ and **even total parity** $\mu(m)=+1$, so $\mu(k)=-1$.

For a real $x=kp\in V$, set $T_1=k/D$, $T_2=Dk/x$, and $S_k(T)=\sum_{r\mid k,\ r\le T}\mu(r)$, $J_k(T)=\int_1^T S_k(t)\,dt/t$ for $T\ge1$, both zero below 1. By the preceding exact sharp-divisor identities,

$$
\begin{split}
 F_{0,D}(pk)&=S_k(T_1^-)-S_k(T_2),\\
 F_{1,D}(pk;x)&=a(x) F_{0,D}(pk)
                   -\frac2{\log x}\bigl(J_k(T_1)+J_k(T_2)\bigr),\\
 a(x)&=\frac{\log(x/D^2)}{\log x}=O(L_2/L).
\end{split} \tag{2}
$$

The strict first cutoff and weak second cutoff in the first line mean an **open** shell $T_2<r<T_1$. The log ratio is $2B\log L+O(1)>0$. No endpoint term is lost in the integrated expression since its coefficient is zero at equality. On this composite support, $-\Xi_D$ is the sharp product $F_{0,D}F_{1,D}$.

As before, partition the physical $x$ range and the arithmetic $k$ range into hard geometric cells of relative width at most $\eta$, with clipped endpoints. Write $K<k\le K'$ and $w=\log(K'/K)$ for an arithmetic cell; the estimates also hold for the other hard endpoint conventions. Add a cut at $k=10D L^{2B}$. Below this cut the arithmetic log length is $O(L_2)$ and the preceding integrated bound $O(\sqrt s\,w/L)$ covers the sharp product, totaling $O(\sqrt s L_2/L)$ plus a power-small floor. Above it both cutoffs exceed 1 since $x\le2N$, and all possible cutoffs are below $Z$ with room for the cell brackets. In particular, if $P^-(k)>Z$ above this border, $F_{0,D}=1-1=0$ for every $p$ in the cell.

For the remaining $k$ choose its actual least prime $\ell=P^-(k)\le Z$, and write $k=\ell v$. On the retained squarefree support, $v$ is **strictly $\ell$-rough**, meaning that no prime $\le\ell$ divides it, including $\ell$ itself. Separating divisors according as they contain $\ell$ gives

$$
 S_k(T)=S_v(T)-S_v(T/\ell),\qquad
 J_k(T)=J_v(T)-J_v(T/\ell).
 \tag{3}
$$

The corresponding strict identity also holds. After (3), the first line of (2) is the difference of signed shell sums on $v$, one with its two cutoffs scaled by $1/\ell$. The other new factors are integrated differences on $v$ rather than separate integrals from 1.

If $\log\ell<L_2^2$, the previous rough-shell proof already bounds the product for this least-prime selector without any estimate on rough $v$. In a fixed arithmetic cell the reciprocal bound per $\ell$ is $O((L_2+\log\ell)(w+\ell Z^2/K)/(\ell L))$, using the signed primitive square on $v$ and the integral in (3). Summing over these primes and over the arithmetic cells gives $O(sL_2^2/L)$ since $\sum_{\ell\le e^{L_2^2}}\log\ell/\ell\ll L_2^2$, $\sum_{\ell\le Z}1/\ell\ll L_2$, and the floors cost only $N^{-1/2+o(1)}$ in total. This argument uses $sL_2^2=o(L)$ just to keep the factor ranges subpower; it needs no positive lower bound on $w$.

## 2. Complete rough reciprocal counts on a cell

Fix a larger least prime, and write $G=\ell$, $U=\log G\ge L_2^2$, $K_v=K/\ell$, $K_v'=K'/\ell$. Here $U\le\log Z=O(s)$ and $K_v\ge N^{1/2-o(1)}$. For every $G$-rough integer $j$ and any fixed $A_0>0$,

$$
 \sum_{\substack{K_v<v\le K_v'\\j\mid v,\ P^-(v)>G}}\frac1v
  =\frac{w}{j}\prod_{p\le G}(1-1/p)
      +O_{A_0}\bigl(wL^{-A_0}/j+N^{-1/2+o(1)}\bigr).
 \tag{4}
$$

Here and below 1 is allowed as a rough integer unless excluded explicitly. Indeed $j\mid v$ leaves the same roughness condition on $v/j$. Use upper and lower truncated Bonferroni, at adjacent even/odd depths within $O(1)$ of $\lceil L_2^2\rceil$. To see applicability with the reciprocal weight, apply the two pointwise inequalities for the product of the indicators of no prime divisibility to each positive term. A subset with product $d$ contributes the count of multiples of $jd$ with reciprocal main term $w/(jd)$ and floor $O(1/K_v)$ by partial summation. At depth $R\asymp L_2^2$ there are at most $(G+1)^{R+1}=N^{o(1)}$ retained terms because $sL_2^2=o(L)$. The two truncated main terms bracket the complete Euler product; their difference is at most $(\sum_{p\le G}1/p)^R/R!$, with a change of one in $R$ harmless. This is $O_{A_0}(L^{-A_0})$ for every fixed $A_0$, as $\sum_{p\le G}1/p=O(L_2)$ and $R\asymp L_2^2$. This proves (4) uniformly even on very short cells.

For coefficients $b_r$ supported on rough $r\le Z$, with $|b_r|\ll s$, the reciprocal square of $\sum_{r\mid v}b_r$ on the rough $v$ cell is therefore

$$
 w\prod_{p\le G}(1-1/p)\!
       \sum_{r,t}\frac{b_r\overline b_t}{[r,t]}
       +O_{A_0}\bigl(wL^{-A_0}+N^{-1/2+o(1)}\bigr).
 \tag{5}
$$

For the first error use $\sum_{r,t\le Z}1/[r,t]\ll(\log(2Z))^3$ by expanding the gcd, and initially choose the exponent in (4) larger. The floor is summed over at most $Z^2$ pairs, with all coefficient bounds subpower. We need only an upper bound for the square on the squarefree $v$ subset, so we may enlarge to all rough $v$ **after taking the nonnegative square**. In contrast, (5) itself keeps the signs in the lcm sum.

## 3. Two signed rough lcm energies

A direct positive harmonic estimate used below is that for a log interval $\mathcal J$ of width $H$,

$$
 \sum_{\substack{n>1,\ P^-(n)>G\\\log n\in\mathcal J}}\frac1n
 \ll H/U+(1+H)e^{-3U/4}.
 \tag{6}
$$

To see this, intersect with $\log n>U$ and cover by segments of width at most 1. On each segment use the dimension-one Selberg sieve of the [previous rough-shell proof](r67-spectral-rough-short-shell-energy.md), with level $\lfloor e^{U/10}\rfloor$, count $O(\text{ordinary length}/U+e^{U/4})$, and reciprocal at most the reciprocal of the segment's starting scale. This gives the stated estimate since that scale is at least $G$. Endpoint changes are included in the sieve error. If $n=1$ is allowed, add its possible single term.

For each squarefree rough $e\le Z$ let

$$
 R_{G,e}(u)=\sum_{\substack{d\le e^u,\ P^-(d)>G\\(d,e)=1}}\frac{\mu(d)}d ,
 \qquad R_{G,e}(u)=0\quad(u<0).
$$

The notation $e^u$ here is the real exponential. We use the ordinary reciprocal Mertens primitive $R(u)=\sum_{d\le e^u}\mu(d)/d$, zero below zero, with $R(u)\ll \exp(-c\sqrt u)$ for $u\ge0$, as in the [subpower proof](r66-spectral-subpower-largest-prime.md). Excluding the primes up to $G$ and those dividing the integer $e$ convolves $R$ with the positive measure giving weight $1/a$ at $\log a$ for integers $a$ supported on those excluded primes. The exponential moment of this measure at $1/U$ is

$$
 \prod_{\substack{p\le G\\\text{or }p\mid e}}
     (1-p^{-1+1/U})^{-1}\ll U.
 \tag{7}
$$

For the $p\le G$ part, divide by $\prod_{p\le G}(1-1/p)^{-1}\ll U$. The first powers in the log of the ratio are $O(U^{-1}\sum_{p\le G}\log p/p)=O(1)$, since $p^{1/U}\le \exp(1)$; higher powers contribute $O(1)$ by $1-1/U\ge3/4$. The remaining primes dividing $e$ exceed $G$, and each contributes $O(e^{1-U})$ to the log of the product, with at most $\log Z/U$ such primes. Thus (7) is uniform in $e$ and $G$. Splitting the positive convolution at log shift $u/2$ gives

$$
 |R_{G,e}(u)|\ll U\bigl(\exp(-c'\sqrt u)+\exp(-u/(2U))\bigr)\qquad (u\ge0).
 \tag{8}
$$

In particular, for any prescribed power $A_0$ it is $O_{A_0}(L^{-A_0})$ once $u>C_{A_0}U L_2$. We used $U\ge L_2^2$ and $U\ll L$. The same decay holds for the strict primitive, since the jump has magnitude at most $\exp(-u)$; at smaller $u\ge0$, (6) gives $|R_{G,e}(u)|\ll 1+u/U+(1+u)e^{-3U/4}$.

For real weights $f$ with support at $r\le Z$, set
$\mathcal E_G(f)=\sum_{r,t\ {\rm rough}}\mu(r)\mu(t)f(r)f(t)/[r,t]$. Expansion of $\gcd(r,t)$ gives the positive identity

$$
 \mathcal E_G(f)=
   \sum_{\substack{e\le Z\\e\ {\rm rough}}}
    \frac{\varphi(e)\mu(e)^2}{e^2}
    \left|\sum_{\substack{d\ {\rm rough}\\(d,e)=1}}
                 \frac{\mu(d)}d\,f(ed)\right|^2.
 \tag{9}
$$

We claim the following uniform estimates.

1. For $f(r)=\mathbf1_{\log r\in\mathcal J}$ with width $W=O_B(L_2)$, allowing all hard endpoint conventions and a shell containing 1, $\mathcal E_G(f)\ll 1$. Indeed the inner sum is the difference of appropriate strict or weak $R_{G,e}$ endpoints. Terms with $\sup\mathcal J-\log e>C_{A_0}U L_2+W$ have negligible total by (8) and $\sum_{e\le Z}1/e\ll s$. In the near range the rough $e$ harmonic sum is $O_{A_0}(L_2)$ by (6), and the nonunit $d$ harmonic sum is $O((1+W)/U)$ by the same estimate. The unit $d=1$ contributes only when $\log e\in\mathcal J$, where the rough $e$ harmonic sum is $O(1+(1+W)/U)$. Splitting the square into twice the unit and twice the nonunit squares gives $O(1+L_2(1+W)^2/U^2)\ll1$.

2. For $f(r)=(\log(T/r))_+-(\log(T/(Gr)))_+$, $0<T\le Z$, one has $\mathcal E_G(f)\ll U^2 L_2^3$. The inner sum in (9) is the integral of $R_{G,e}(u)$ from $\log(T/e)-U$ to $\log(T/e)$. If the upper endpoint is negative the contribution is zero. If the lower endpoint exceeds $C_{A_0}U L_2$, use (8) and the total harmonic bound as above. In the remaining log range of $e$ (width $O_{A_0}(U L_2)$), its rough harmonic sum is $O_{A_0}(L_2)$ by (6); the reciprocal primitive on the integration intervals is $O_{A_0}(L_2)$, so the squared integrals are $O_{A_0}(U^2 L_2^2)$. This proves the assertion. A fixed sufficiently large $A_0$ suffices in both estimates.

Finally the **unsigned** rough lcm energy in any boundary shell of log width $O(\eta)$ is $O(1)$. Write $r=ea,t=eb$, $e=(r,t)$, and retain roughness. Exactly one of $a,b$ being 1 is impossible since $\log G\gg\eta$. For both 1 the diagonal costs $O(1)$ by (6), including any unit. For both exceeding 1, each of their harmonic sums restricted by $e$ is $O(\eta/U)$ by (6), since $\eta\ge L^{-1/2}$ and $U\ge L_2^2$. The remaining rough $e$ harmonic sum is $O(1+s/U)$ by (6). Hence the off-diagonal contribution is at most $O((\eta/U)^2(1+s/U))=O(1)$ after dropping coprimality.

## 4. Retain actual moving cuts and transfer back to minors

Keep a fixed physical cell and one arithmetic cell. The four endpoints of the two signed shells in (2)–(3) vary in multiplicative brackets of log width $O(\eta)$, even after division by $\ell$, and each shell has width $O_B(L_2)$. For each shell choose fixed endpoints within the brackets, and majorize its moving absolute value by the absolute signed shell at those fixed endpoints plus the two unsigned boundary shell counts. This is an upper bound, not a replacement in the actual polynomial. Include all possible endpoint integers in the boundary counts. By (5), (9), and the boundary energy, on the rough $v$ cell its squared reciprocal sum is $O(w/U+N^{-1/2+o(1)})$, using $\prod_{p\le G}(1-1/p)\ll1/U$.

For the integrated difference $J_v(T)-J_v(T/G)$ with moving $T=T_1,T_2$, fix $T$ at one point of its bracket. The resulting squares on rough $v$ sum to $O(w U L_2^3+N^{-1/2+o(1)})$ by (5) and assertion 2. The change is bounded by the integrals of $|S_v(t)|$ on the two fixed endpoint brackets, of log width $O(\eta)$, with $S_v$ zero below 1. Cauchy there and the unconditional fixed-primitive square bound in the [subpower proof](r66-spectral-subpower-largest-prime.md) give $O(\eta^2(w+Z^2/K_v))$ for the squared reciprocal sum of this error, enlarged to all integer $v$ after taking squares. This is absorbed in the preceding bound. All these majorants are uniform in the physical variable on its cell.

Apply (2), $a(x)=O(L_2/L)$, and Cauchy on the rough $v$ cell. The reciprocal product sum for the sharp factors, now expressed in $k=\ell v$, is

$$
 \sum_{\substack{\text{cell }k\\P^-(k)=\ell}}\frac{\text{product majorant}(k)}k
 \ll \frac{wL_2^{3/2}}{\ell L}
        +\frac{N^{-1/4+o(1)}}{\ell}.
 \tag{10}
$$

Indeed the squared bounds on $v$ have main terms $w/U$ and $wU L_2^3/L^2$, respectively. The smaller $a(x)F_0$ term is absorbed as $U\ge L_2^2$. In using (5) take its arbitrary fixed savings sufficient to absorb all $wL^{-A_0}$ in these main bounds, since $U\ll L$; the Cauchy floor exponent in (10) is uniform even with tiny $w$. Sum over $\ell\le Z$ prime using $\sum1/\ell\ll L_2$, and then sum the arithmetic widths $O(s)$. The floor remains power-small, the number of cells being $O(1+s/\eta)$. For each fixed physical cell, the sharp-product reciprocal mean is thus $O(sL_2^{5/2}/L)$, including the small-prime, border, and prime-$k$ cases. Adding the old low mixed bound and multiplying by $k/\varphi(k)\ll L_2$ gives $O(sL_2^6/L)$.

For the first line of (1), use the same unconditional two-prime sieve as in the integrated proof with the actual $p,N-kp$ and hard intervals; its per-$k$ main term is $O(\Sigma(N)|I_{\rm cell}|(k/\varphi(k))/(kL^2))$ plus $O(N^{1/4}L)$. Multiply by $\lambda(n)\le L$ and the positive majorant and sum. The physical lengths sum to $|I|$. All coefficient majorants are subpower, the physical cells are polylogarithmically many, and $k\ll\sqrt N e^s=N^{1/2+o(1)}$, so the floors fit in $N^{.76}$. Any actual nonunit constraints are retained in the full sum and the same sieve is used on the unit cofactor classes.

For the second line, do not insert the majorants into the Fourier polynomial. The actual least-prime partition was only a device to bound the original real weight uniformly on physical cells. The right weight at fixed $k$, including the largest-prime condition and either parity selector, still has the earlier $O(\tau_4(k))$ supremum and variation bound. The original pointwise prime-progression evaluation thus gives the same $c_q(k)/\varphi(q)$ factors and $O_\epsilon(N^{3/4+\epsilon}Q^2)$ right polynomial error. The arithmetic occupation and Fourier/Ramanujan tails of the subpower proof apply unchanged since $e^s=N^{o(1)}$. The completed real density has local factor zero on $(k,N)>1$, otherwise $O(\Sigma(N)k/\varphi(k))$, and reciprocal prime cofactor $1/(k\log(x/k))$. Applying the just-proved reciprocal majorant bound here yields $O(\Sigma(N)|I|sL_2^6/L^2)$ for the major integral, with the same $O(N^{1-10^{-4}})$ power error. Subtract it from the actual full coefficient. Neither step estimates the minor integral on the complementary smaller-largest-prime sector.
