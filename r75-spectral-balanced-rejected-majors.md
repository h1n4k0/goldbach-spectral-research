# The near-balanced rejected tags have a smaller genuine major integral

**Scope.** This treats a genuine two-prime ordering correction left open by the [odd marked major](r73-spectral-marked-prime-weighted-major.md) and [even marked major](r74-spectral-even-marked-major.md). We remove the near-balanced part of the rejected tags for both Möbius parities on the **original major arcs**, under the same historical prime-character Dirichlet GRH (including the principal zeta case). This is not a full arithmetic or minor-arc bound. It does not estimate the more widely separated order correction or weak S.

Use the exact notation of the marked calculations: $0<\sigma_1<\sigma_2<1/10$, fixed $B>B_0>0$, even $N$ of fixed radical $\mathcal R$, $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ and $V=[N/3,2N]$. The right coefficient is the true $M_>(m)$ on squarefree partners, before its subtraction in the exact marginal decomposition. The original major arcs are $\mathfrak M$ with reduced denominators at most $Q=N^{1/1000}$ and widths $2Q/N$. The left polynomial is the genuine $P_{I,\omega}$ for the same exact central interval and bounded-variation left weight.

Define the rejected-tag right polynomial $A_{\rm bal}$ by taking the true marked terms $m=kp\in V$, $p$ prime, $p\nmid k$, $D N^{\sigma_1}<k\le D N^{\sigma_2}$, and retaining exactly

$$
 q=P^+(k)>p,\qquad 0<\log(q/p)\le E,\qquad 1\le E\le \sigma_1 L/2.
 \tag{1}
$$

One may impose either true total Möbius parity, or both. One may also impose any fixed-in-$N$-during-the-prime-transfer subset selector on the remaining integer $a=k/q$; in particular a condition on its number of prime factors at most $\exp(\sqrt L)$ is permitted and may depend on $N$. The branch is rejected by unique-largest selection; it does not count the accepted $q$ mark. For this genuinely restricted right polynomial we prove

$$
 \left|\int_{\mathfrak M}P_{I,\omega}(\theta)A_{\rm bal}(\theta)
                  e(-N\theta)\,d\theta\right|
 \ll \frac{\Sigma(N)|I|}{L}
          \left\{\frac{(E+1)L_2^5}{L}+\frac{L_2^2}{\sqrt L}\right\}
                  +N^{1-10^{-4}} .
 \tag{2}
$$

In particular $E=10 L^{2/3}$ leaves an $o(\Sigma(N))$ contribution in the $L/N$ normalization. The estimate does not assert that the actual positive mass in (1) is small.

## 1. Two actual primes and both reciprocal logarithms

Write $k=qa$, $x=pqa$, $k'=pa$. With $\Lambda_x=\log(x/D)$ and $h=\log(x/D^2)>0$, set

$$
 t=\log(k/D),\quad s=\log(k'/D),\quad c_a=h+\log a,\quad
 t+s=c_a,\quad q=(x/D)e^{-s},\quad p=(x/D)e^{-t}.
 \tag{3}
$$

The two primes exceed $cN^{1/2-\sigma_2}L^B$ because the rejected prime $p=x/k$ already has that bound. Also $a=k/q\ll N^{2\sigma_2}L^{-2B}$, so $p,q>a$ for large $N$. Thus the larger prime is unique and automatically coprime to $a$; $a$ is squarefree. Both primes exceed the small-prime threshold and any short label below. The count selector agrees with the corresponding selector on $k$, $k'$ or $m$. The total parity is $\mu(a)$, not its negative, since there are two giant primes.

At fixed eligible integer $k=qa$ with its actual larger prime $q$, the added gates are exactly $x<kq$ and $x\ge kq e^{-E}$. The selector on $a$ and its parity are constant at fixed $k$. These support restrictions preserve the $O(\tau_4(k))$ supremum and variation of the real coefficient, including the jumps. Thus the prime-progression comparison and original Fourier/Ramanujan completion of §2 of the odd marked calculation give the genuine major integral as the integral over the left test of the completed right density, with the same $O(N^{1-10^{-4}})$ error. Its right term at fixed $k$ is $\Sigma(N)r(k)/(k\log(x/k))$ times the real coefficient on its exact gated support. Here $r(k)$ denotes the fixed-radical local factor of that calculation. The same right polynomial error uses $Q^2\sum_{k\ll N^{1/2+\sigma_2}}\sqrt{N/k}\,\tau_4(k)L^{O(1)}$; the original occupation bound has not changed. A prime dividing $k$ cannot be the restored tag on this support: it is either $q$, excluded by the strict gate, or at most $a$, below the support. There is at most one rejected tag per $m$ on this range, so the genuine left-error pairing is also unchanged.

After that completion, evaluate the second **actual prime** $q$ by ordinary prime partial summation at fixed $a,x$. The completed $r(k)=r(a)r_q$ has $r_q=1+O(1/q)$ since the radical is fixed, so dropping $r_q$ costs only a power. The real coefficient in $q$ through its gated interval has supremum plus variation $O(\tau_8(a))$: the two short sharp cutoff sums involve only divisors of $a$, and in either low fold the large divisor uses exactly one giant tag; the signed labels then belong to an $a$-divisor. The exact expressions in §2 below verify this directly also when $q$ becomes continuous. At worst each divisor choice has a bounded number of monotone ratio pieces and support jumps, and their total on a squarefree $a$ is $O(\tau_8(a))$. Using the principal zeta prime estimate $\pi(y)=\mathrm{Li}(y)+O(\sqrt y\log^2(2y))$ included in the historical assumption, on each ordinary dyad $q\asymp Y\gg N^{.4}$ the reciprocal $1/(q\log(x/(aq)))$ supplies $O(1/(YL))$ in supremum plus variation. The error at fixed $a$ is consequently $O(N^{-.19}\tau_8(a)/a)$ after dyadic summation. Summing it over $a$ costs just a fixed power of $L$, using the divisor harmonic bound. The same argument bounds the discarded $r_q-1$ term. In particular no new progression hypothesis for the second prime is used after the completed rational factor.

With $dq/q=-ds$, the completed density at real $x$ is consequently

$$
 \Sigma(N)
 \sum_{\substack{a\ {\rm sf}\\\text{selected}}}\frac{r(a)}a
   \int_{\mathcal J_a} W_a(s)\{X_a(s,x)-Y_a(s,x)\}\,ds
       +O(\Sigma(N)N^{-.18}),
 \qquad
 W_a(s)=\frac1{(\Lambda_x-s)(\Lambda_x-c_a+s)},
 \tag{4}
$$

where the exact interval is

$$
 \mathcal J_a=[c_a-\sigma_2L,\ c_a-\sigma_1L)
                    \cap[(c_a-E)/2,\ c_a/2).
 \tag{5}
$$

The forward/completed cofactor sum has no parity restriction other than the one specified in the theorem. Both denominators in (4) are comparable to $L$ on (5). In particular $\|W_a\|_\infty\ll L^{-2}$ and $\|W_a'\|_\infty\ll L^{-3}$ there, including their finite endpoint limits. Strict inequality at $q=p$ remains in the actual polynomial; no diagonal correction is hidden in the continuous integral.

## 2. Exact swapped short formulas

Let $S_a(u)=\sum_{d\mid a,\ \log d\le u}\mu(d)$, with the strict version $S_a(u^-)$, and put $J_a(u)=\int_{-\infty}^u S_a(v)\,dv$. Both vanish below log argument $0$. In (4) use the swapped tag $q$ with cofactor $k'=pa$. Its cutoff arguments are $s$ and $s-h$. The formal $p$ cannot enter either short divisor sum, since $p\gg N^{.4}$ and all labels are $\ll N^{\sigma_2}$. For almost every $s$ the sharp coefficient is, using $A(s)=S_a(s)$ and $A_h(s)=S_a(s-h)$,

$$
 X_a(s,x)=
 \begin{cases}
 \bigl[h(A+A_h)^2-2(A+A_h)(J_a(s)-J_a(s-h))\bigr]/\log x,
                                      &\mu(a)=-1,\\
 \bigl[h(A-A_h)^2-2(A-A_h)(J_a(s)+J_a(s-h))\bigr]/\log x,
                                      &\mu(a)=+1 .
 \end{cases}
 \tag{6}
$$

The original first cutoff is strict; replacing it by a weak one in (6) is only an almost-everywhere statement for the real integral at fixed $a$. Indeed $\mu(k')=-\mu(a)$ and the formulas are those of the preceding sharp decompositions.

For the low coefficient the two-fold exact formula uses a common low variable $l$, with $D<l\le H_0$. Write $z=\log(l/D)$ and $v\mid a$. The large divisor of $k'$ in either fold is necessarily $k'/v$: it contains the tag $p$ since $a\ll N^{.2}$ and the large divisor is $N^{1/2+o(1)}$. Thus in the first fold $l=k'/v$ and $z=s-\log v$; the two signed coprime short labels $d_1,d_2$ divide $a/v$. In the second fold $l=x/(k'/v)=qv$ and $z=h-s+\log v$; the labels divide $v$. In both cases impose $d_i<e^z$ strictly and apply weight

$$
 \mu(d_1)\mu(d_2)\frac{h-2z+\log(d_1d_2)}{\log x}.
 \tag{7}
$$

These give $Y_a(s,x)$, with the exact low cutoff as in the marked proof. On the region (5) the composite squarefree identity is $M_>=X_a-Y_a$.

For clarity, this swap is valid in the real completed coefficient, not only at prime pairs. The original divisor formulas can be evaluated on the squarefree divisor lattice with two formal independent tags of sizes $p$ and $q$ and with actual remaining factors of $a$. A label consists of a divisor of $a$ and a subset of the two tags, with its usual sign; its real size is the product. Divisibility, coprimality and LCM refer to that lattice. The complementary identities and original low folds are finite algebra on this lattice with the same real size inequalities. Interchanging which tag is used first changes neither the collection of signed divisors nor any size gate. The continuous coefficient originally inserted at fixed integer $k=qa$ agrees with this evaluation even if $p=x/k$ is real. On the actual prime pairs the formal lattice is the usual one. This justifies using (6)–(7) throughout the second prime comparison, without an extrapolation from equality at integers.

## 3. A moving cutoff at the actual square-root floor

Use the signed reciprocal LCM bounds of the [sharp energy](r66-spectral-subpower-largest-prime.md) and [integrated energy](r66-spectral-integrated-short-cutoff.md), namely

$$
 \sum_{d,e\le T}\frac{\mu(d)\mu(e)}{[d,e]}\ll1,\qquad
 \sum_{d,e\le T}\frac{\mu(d)\mu(e)}{[d,e]}
                      \log(T/d)\log(T/e)\ll\log(2T).
 \tag{8}
$$

They are nonnegative quadratic forms and hold for arbitrary real sharp endpoints (also the strict version by taking the left limit). We need the following moving version without a grid loss. On any hard interval $\mathcal H\subset[A,2A]$, let $T(a)$ be positive monotone with supremum $O(\sqrt A)$, and with a fixed choice of strict or weak version. Put $Q_0(a)=S_a(\log T(a))$ and $Q_1(a)=J_a(\log T(a))$ on this interval. Then

$$
 \sum_{a\in\mathcal H}\frac{|Q_0(a)|^2}a\ll1,\qquad
 \sum_{a\in\mathcal H}\frac{|Q_1(a)|^2}a\ll1+\log(2A).
 \tag{9}
$$

No squarefree restriction is needed in (9), and any subset mask after the square can be dropped.

To prove it, expand into a square and sum over multiples of $[d,e]$. For each pair the step/log product of its two coefficient weights has supremum plus variation at most a constant times its product of upper sizes. This is by monotonicity, and includes the endpoints of the hard interval. The reciprocal progression floor is $O(1/A)$ times that product; the main term is $1/[d,e]$ times the corresponding real reciprocal integral. Summing floors over all $d,e$ costs $O(T_{\max}^2/A)=O(1)$, since $\sum_{d\le T_{\max}}1\ll T_{\max}$ and $\sum_{d\le T_{\max}}\log(T_{\max}/d)\le T_{\max}$, respectively. In the real main term interchange the finite label sum and the integral, then apply (8) at the actual real $T(a)$. This proves (9). The same bounds apply to a bounded number of monotone pieces; in particular the endpoints and their shifted versions below have this property. This avoids freezing with a different floor for each point or each fine cell.

At squarefree $a>1$, complementation gives

$$
 S_a(u^-)=-\mu(a) S_a(\log a-u),\qquad
 S_a(u)=-\mu(a) S_a((\log a-u)^-).
 \tag{10}
$$

For composite squarefree $a$ it also gives $J_a(u)=\mu(a)J_a(\log a-u)$. Indeed $\sum_{d\mid a}\mu(d)=\sum_{d\mid a}\mu(d)\log d=0$ in the composite case, and replace $\log d$ by $\log a-\log d$ in the negative part of $u-\log d$. In the only case where we use reflection for $J_a$, namely $\mu(a)=+1$ on (5), $a$ is composite since $a\ge N^c$ for a fixed $c>0$. For a general moving primitive intersect the dyad with the pieces $u\le \frac12\log a$ and $u>\frac12\log a$, applying (10) on the latter. Each log argument we use is affine in $\log a$ or fixed, up to a bounded number of pieces; after reflection its cutoff remains monotone on each piece, with upper size at most $\sqrt{2A}$. Thus (9) applies also to these reflected expressions on the true squarefree parity set. We first use the exact reflection only on that set, then drop restrictions in the positive square of each new primitive. Because $r(a)\ll L_2$, inserting the local weight costs only $O(L_2)$.

For fixed $s$ the nonempty allowed $a$ interval in (5) has log length at most $E$. Hence the sum of either primitive square over it is bounded by $O((E+1)L_2)$ for $S$, and by $O((E+1)LL_2)$ for the full $J$ on even total parity, using (9) on $O(E+1)$ ordinary dyads. These same $S$ bounds are uniform for arguments $u=s-v$, $0\le v\le h$, as their reflected versions still meet the previous conditions. For an endpoint of $\mathcal J_a$ at fixed $a$, its possible values are the four affine boundary functions appearing in (5). Apply the same estimates with the endpoint as a function of $\log a$, on the region where it is active. This requires only $O(L)$ ordinary dyads for all relevant $a$, since $a\le N^{2\sigma_2+o(1)}$. For these endpoint sums the corresponding bounds are $O(LL_2)$ for $S$ and $O(L^2L_2)$ for the even full $J$. The estimates also hold at all endpoint values with strict or weak convention, and when any of the allowed integer selectors are imposed.

## 4. Signed integration through the balanced strip

Write $K_a(s)=J_a(s)-J_a(s-h)=\int_{s-h}^s S_a(v)\,dv$ and $J_+(s)=J_a(s)+J_a(s-h)$. By the squared primitive estimates and Cauchy inside the interval of length $h$, for fixed $s$ the reciprocal sum of $|K_a|^2$ is $O(h^2(E+1)L_2)$. At the finitely typed endpoints the same bound is $O(h^2 LL_2)$. These bounds use the intervening real arguments of §3 and include the weight $r(a)/a$.

The odd formula in (6), and the centered square term for even, are immediately bounded in (4) by the bulk estimates and Cauchy. Before the factor $\Sigma(N)$ their absolute bulk bound is $O(h(E+1)L_2/L^2)$: the $s$ range has length $O(L)$ and there are the $O(L^{-2})$ weight and $O(L^{-1})$ sharp prefactor. For the even cross term, it is essential to take its **signed** integral first. Since $K_a'=A-A_h$ and $J_+'=A+A_h$ almost everywhere, the exact integration by parts on (5) gives

$$
 \int_{\mathcal J_a} W_a(A-A_h)J_+\,ds
   =[W_a K_a J_+]_{\partial\mathcal J_a}
      -\int_{\mathcal J_a} W_a K_a(A+A_h)\,ds
      -\int_{\mathcal J_a} W_a' K_a J_+\,ds.
 \tag{11}
$$

Both integrated primitives are absolutely continuous; their endpoint values do not depend on the representative of a sharp step. If (5) is empty we use zero. Its open/closed conventions have no effect on the integration formula.

The middle integral in (11) is another bulk term using only the short primitive and is bounded just as in the odd case. For the endpoint sum, Cauchy and the endpoint bounds give

$$
 \sum \frac{r(a)}a |K_a J_+|_{\partial\mathcal J_a}
                             \ll h L^{3/2} L_2 .
$$

Here the same integer selector is kept in (11); only after integration by parts do we take absolute values of the three resulting quantities and use positive bounds. The first term, including $W_a$ and the sharp prefactor, costs $O(h L_2/L^{3/2})$ in the right density before $\Sigma(N)$. For the last term the fixed-$s$ product sum is $O(h\sqrt L(E+1)L_2)$ by Cauchy. Its additional $L^{-1}$ in $W_a'$ bounds it, after integrating $O(L)$ and using the sharp prefactor, by $O(h(E+1)L_2/L^{5/2})$, no larger than the endpoint bound. This controls the entire sharp part without bounding the long even integrated primitive in absolute mass on the full strip.

For the low part in (7) ordinary positive harmonic counts suffice. Fix $s$ in the balanced region, a fold and $d_1,d_2$. Their product $d$ divides the designated factor of $a=uv$, where the other factor is free except for the original product interval and the log gate on $v$. Here $v$ ranges over a log interval of width $O(L_2)$, with $v\ge N^c$, and $u=a/v$ is also polynomially large because $t,s\ge \sigma_1L/2$ on (5). For every fixed $v$ the allowable interval for $u$ has log length at most $E$. For a designated multiple use the standard reciprocal count $O((w+1)/d)$ on an interval of log width $w$ whose lower endpoint is polynomially larger than $d$; for the other factor use the case $d=1$. This bound includes its one-point floor. If the labels are in $v$ use the multiple count in $v$, and otherwise in $u$. Summing reciprocal product weights over the selected factors costs $O(L_2(E+1)/d)$; dropping coprimality, squarefreeness and parity in this positive estimate only enlarges it. Sum $1/d=1/(d_1d_2)$ over the coprime labels up to $H_0/D$, with total $O(L_2^2)$; the centered coefficient costs $O(L_2/L)$ and $r(a)$ another $O(L_2)$. Thus for fixed $s$ the reciprocal absolute low sum is $O((E+1)L_2^5/L)$. After the $s$ integral of length $O(L)$ and the weight $O(L^{-2})$, its bound in (4) is $O((E+1)L_2^5/L^2)$ before $\Sigma(N)$.

Combine the low and sharp estimates in (4), with $h=O(L_2)$ and all constants uniform for $x\in V$. Integrating against the original left weight on $I$ proves (2); the small power error in (4) is absorbed in the existing fixed-$Q$ error. The gain at $E=10 L^{2/3}$ is for the actual signed major correction only. It uses neither a prime-free substitution for the original right polynomial nor a claim that a short logarithmic strip by itself forces small absolute arithmetic mass.
