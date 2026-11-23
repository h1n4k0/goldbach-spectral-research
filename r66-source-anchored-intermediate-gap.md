# Pointwise control of anchored intermediate-prime bands

Keep the central hard window $I\subseteq I_0=[\rho N,(1-\rho)N]$, the exact $N$-units, and the original strict divisor tests of the [rough-complement theorem](r65-source-pointwise-rough-complements.md). For even $N$ use $L=\log N$, $\ell=\log L$, $T=L/\ell$, $D=\lfloor\sqrt N e^{-20T}\rfloor$, $Q=\lfloor N e^{-20T}\rfloor$. Fix $B_1,B_2>0$ with $B_1+B_2<20$, and $C>\max(B_1,B_2)$. In slot $i$ choose squarefree integers $n=a_1 b_1 u$, $m=a_2 b_2 v$ with the following factor ranges:

- The small part $a_i$ has all primes at most $\exp(L^{\alpha_i})$.
- The gap part $b_i$ has all primes in $[\exp(L^{\beta_i}),\exp(B_i T)]$, and its **whole product** satisfies $b_i\le\exp(B_iT)$.
- The nonempty rough parts $u,v$ have all primes at least $Y=\exp(CT)$ with unrestricted arity.

Here $0\le\alpha_i<\beta_i<1$ are fixed. Require at least one small part to be nonempty (greater than one); call such a slot anchored. A slot required to have $a_i=1$ is assigned $\alpha_i=0$. The gap parts may be empty or required to be nonempty. The product cap is an actual sector mask, not a claim that its complement is negligible. Further masks on the integers are allowed if independent of the interior divisor labels. The exact signed quantity is

$$
 {\cal R}_N(I)=-
 \sum_{\substack{n+m=N,\ n\in I,\ m\in I_0\\(nm,N)=1,\ n,m\ {\rm selected}}}
 \ \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
         \mu(d)\mu(e)\log(n/d)\log(m/e).
 \tag{1}
$$

**Theorem (unconditional, pointwise).** Set

$$
 \sigma=1-2\sum_{i=1}^2(\alpha_i+1-\beta_i),\qquad
 \nu=\frac{\log 2}{C},\qquad
 \delta=
 \begin{cases}
 \max(0,2\nu-1)&\text{both slots anchored},\\
 2\nu&\text{exactly one slot anchored}.
 \end{cases}
$$

For every fixed $A>0$, every sufficiently large even $N$, and every hard interval and admitted mask,

$$
 |{\cal R}_N(I)|\ll_{\rho,C,B_i,\alpha_i,\beta_i,A}
    \mathfrak S(N)\left(|I|\ell L^{-\sigma+\delta}+NL^{-A}\right).
 \tag{2}
$$

Thus $\sigma>\delta$ gives a log saving, with no exceptional targets. For example, both anchored with $\alpha_i=.05$, $\beta_i=.9$, $B_i=3$, $C=5$ gives $\sigma=.4$, $\delta=0$ and allows genuine gap primes in both slots. In the single-anchor case the other slot may still carry its gap product. No both-unanchored, unrestricted gap, pointwise main-term, or Hypothesis S assertion is made.

## 1. Lower profiles and product slack

Write $s=a_1b_1$, $t=a_2b_2$, and choose $\varepsilon=(20-B_1-B_2)/4$, $H=20-B_1-B_2-2\varepsilon>0$. Only the small parts may be truncated at $\exp(\varepsilon T)$, with error $O_A(N L^{-A})$. Indeed $n$ determines $m$ on the true sum line; the absolute total divisor weights per integer are at most $L^{1+\nu}\tau(a_i)\tau(b_i)$ because the true rough parts have at most $\ell/C$ prime factors. By Cauchy, using all multiples up to $N$ for a fixed lower product, the squared discarded side is bounded by $NL^{2+2\nu}$ times

$$
 \left(\sum_{\substack{a>\exp(\varepsilon T)\\ a\ \mathrm{squarefree},\ P^+(a)\le \exp(L^{\alpha_i})}}
                   \frac{\tau(a)^2}{a}\right)
 \left(\sum_{\substack{b\ \mathrm{squarefree}\\ p\mid b\Rightarrow
                           \exp(L^{\beta_i})\le p\le\exp(B_iT)}}
                   \frac{\tau(b)^2}{b}\right).
$$

The other side uses its unrestricted analogous squared moment. The gap Euler products are bounded by powers of $L$. Rankin at $L^{-\alpha_i}$ in the first sum gains $\exp(-\varepsilon L^{1-\alpha_i}/\ell)$ at cost $\prod_{p\le\exp(L^{\alpha_i})}(1+4e/p)\ll L^{O(1)}$. This absorbs all fixed logarithmic losses; if $a_i=1$ there is no discard. No supported $b_i$ is removed. Now $st\le\exp((20-H)T)$, $s,t<D$, and $u,v>\sqrt N$. For later lattice errors a squarefree $w\le\exp(MT)$ with fixed $M$ has $\tau(w)=\exp(o_M(T))$: split its primes at $\sqrt T$, giving at most $\sqrt T+2MT/\log T$ factors.

In the positive lower profile use weight $\tau(w)\lambda^*(w)/w$, where $\lambda^*(w)=\prod_{p\mid w,\ p>2}(p-1)/(p-2)$. When anchored, $P^-(w)$ is in $a_i$, so the optional mark $1+\log P^-(w)$ can be inserted into the small-part profile. The [least-prime weighted calculation](r65-source-pointwise-two-rough.md) bounds either such small-part profile by $O(L^{2\alpha_i})$. An unanchored small part has profile one. On multiplying by the gap Euler product, Mertens gives the additional factor

$$
 \prod_{\exp(L^{\beta_i})\le p\le\exp(B_iT)}
        (1+2\lambda^*(p)/p)
     \ll (B_iT/L^{\beta_i})^2\ll_{B_i} L^{2(1-\beta_i)}/\ell^2.
$$

The ratio inside the square tends to infinity, so the factor includes the empty gap product. The product cap can be discarded only in these positive profiles. Thus the two lower profiles together cost

$$
                  {\cal E}=O(L^{2\sum_i(\alpha_i+1-\beta_i)}/\ell^4).
 \tag{3}
$$

On the rough side use the [growing-arity reciprocal bounds](r65-source-growing-rough-arity.md): a free rough product costs $O_C(\ell)$, and a nonempty rough product in a log strip of width $W$ costs $O_C((1+W)\ell^2/L)$. These follow from the squarefree Euler product and fixing one prime in the log interval. The rough factors of $\lambda^*$ are $1+o_C(1)$ on the true support. Unfrozen rough labels cost at most $L^\nu$ per true operand; no such label cost is attached to a frozen rough factor itself.

## 2. Same affine sieve at a smaller fixed exponent

The freezes below give $hk\le st\max(Q,D^2)$, $hk\le stD$, or $hk=st$, all bounded by $Ne^{-HT}$ for large $N$. Use the same affine upper sieve of the rough-complement theorem on $hP+kV=N$, with the two remaining **entire rough parts**. Retune to $Z=\exp(HT/24)$, $z=Z^\eta$ with a fixed $0<\eta<\min(\eta_0,24C/H)$, where $\eta_0$ is the small constant of that sieve. Thus $z<Y$, so the true affine variables have no prime factor at most $z$. On the actual frozen masks $(hk,N)=(h,k)=1$, its determinant and local roots are unchanged. It gives main upper bound

$$
 O_{C,H}\!\left(\frac{\mathfrak S(N)|I|}{hkT^2}
              \lambda^*(h)\lambda^*(k)\right)
$$

and error $O(Z^6)=O(e^{HT/4})$ per pair including the hard-endpoint floors. The denominator is still $T^2$ because $\log z$ is a fixed multiple of $T$.

There are $O(Ne^{-HT}L)$ ordered frozen pairs. In either cofactor the small, gap, and rough primes split uniquely by the disjoint ranges. Lower multiplicity is $\exp(o(T))$ from §1, still-unfrozen rough labels are at most $L^{2\nu}$, and all weights are $O(L^2)$. Thus the total lattice error is at most $N\exp(-(3H/4-o(1))T)=O_A(NL^{-A})$. Coprimalities may be dropped only in the positive sums after applying the sieve to genuine frozen pairs.

## 3. The anchored switches

For two anchors apply the exact double switch of the rough-complement theorem to the least prime on each side, both in their small parts. Let $f,g$ be the rough parts of the corresponding divisor labels. They cannot switch when empty or full, since $s,t<D$ and $u,v>\sqrt N$. A nonzero second difference has a switch each way. If either starts above its own D boundary then the original product boundary gives $fg\le Q$; otherwise $f,g\le D$. Freeze $h=sf,k=tg$ and retain one conditional strip on a switched rough label, of log width its least small-prime logarithm. For a mixed term switching at a product boundary the same freezes apply. At a D-type mixed switch, freeze only the switched rough part (at most $D$) and the other lower part; its shift gives the D strip independent of the other rough label. The light–light term freezes only $s,t$. This is the identical case decomposition with the original strict inequalities. In the order just given their main upper profiles, *before* the lower factors (3) and $\mathfrak S(N)|I|$, are bounded by

$$
     \ell^5 L^{-1},\qquad
     \ell^5 L^{-2},\qquad
     \ell^4 L^{-2+\nu},\qquad
     \ell^2 L^{-2+2\nu}.
$$

In fact the first cost is $L^2/T^2$ times the thin rough $\ell^2/L$ and the other frozen rough $\ell$; the strip's $1+W$ is included in (3) as the least-prime weight. The other terms replace one or both heavy $L$ by marked factors from (3), and pay the indicated $L^\nu$ only when a rough label is actually omitted. Multiplying by (3) gives (2) with $\delta=\max(0,2\nu-1)$.

Suppose only the first side has an anchor. Use the [exact single switch](r64-source-least-prime-toggle-first-moment.md) against each **actual** right divisor $e=d'g>D$ with $d'\mid t,g\mid v$. Set $p=P^-(s)$, $x=cf$ for the left base. The heavy term requires $x\le\max(D,Q/e)<p x$, so $f$ is nonempty and proper. When $x>D$, the product switch forces $xe\le Q$. The right $g$ is nonempty because $t<D$ and not full because then $e\ge v>\sqrt N$ makes this product condition impossible. Freeze $sf,tg$ with $hk\le stQ$, and use the true strip of width $\log p$ on $f$ given the opposite label. When $x\le D$, its switch forces $D/p<x\le D$. Freeze $sf,t$ with $hk\le stD$, and drop at most $L^\nu$ opposite rough labels. Finally the light term on the anchored side uses $\log p$ and the opposite log is bounded by $L$; freeze $s,t$ and allow $L^{2\nu}$ rough labels. The resulting profiles before (3) are $\ell^5/L$, $\ell^4L^{-1+\nu}$, and $\ell^2L^{-1+2\nu}$. The unanchored side used only its ordinary lower profile, even if it contains gap primes. This gives (2) with $\delta=2\nu$; if only the second slot is anchored, reflect the interval and exchange the slots. The true signs were retained up to the exact single or double difference before any positive upper bound.

The both-anchored gap sector need not have zero marked summands. For an external scale $X$, take $s=3p,t=5q$ with distinct gap primes $p,q$ near $\exp(2(\log X)^{\beta_i})$ on their respective sides, and distinct rough primes $f,g$ so that $sf,tg$ are each near $\sqrt{2Q_X}$. Choose rough complements $F,G$ with $(sf)F,(tg)G$ each near $X/2$. The PNT gives all these primes in sufficiently narrow fixed proportional windows, distinct across the two sides. The sum $N=(sf)F+(tg)G$ is even and the two integers are central units. The log derivative of the unrounded $Q$ is bounded, so the windows give $Q_N<(sf)(tg)<3Q_N$, with $sf,tg>D$. Also $F,G>\sqrt N$, and every divisor involving either of these in its rough label is a complete lower orbit against each opposite long divisor: that orbit vanishes for composite $s$ or $t$. For the remaining rough labels $f,g$ any omitted lower prime reduces the product by at least a factor three. Only the maximum pair of lower divisors passes Q, giving the actual summand $-\log F\log G$ in (1). This is an existence check, not a lower bound for an aggregate.

Without any anchor the weighted strip need not carry the small least-prime moment in (3). The product cap is also genuinely used for the affine error budget. Neither the unrestricted residual, the unanchored high bands of the first-moment theorem, nor the full operator has been bounded here.
