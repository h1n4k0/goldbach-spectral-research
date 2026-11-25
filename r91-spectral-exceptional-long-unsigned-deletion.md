# Delete the long unsigned factors from the actual hard exceptional residue

**Scope.** The possible exceptional-character correction to the genuine mixed strip can be confined to two explicit sectors where **both** Möbius-weighted factors are polynomially long. The deletion is unconditional, uniform in actual even targets and hard left tests, and does not require the conductor to divide the target or any assumption on the real-zero gap. It is not a bound on the surviving two-signed-factor correlation, an uncorrected law for complete prescribed plantings, or a result on Hypothesis S.

Use the exact [hard exceptional transfer](r88-spectral-hard-exceptional-residue-transfer.md) of the [all-scale correction](r87-spectral-all-scale-exceptional-left-reduction.md). Here $Y\le N\le2Y$ is even, $G=\log Y$, $L=\log N$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$. The physical $m\in V=[N/3,2N]$, $n=N-m$, actual half-open $I\subset(N/2,9N/16]$ and uniformly bounded pointwise-BV $\omega$ are unchanged. Put $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ for the same admissible fixed $B>B_0>0$.

In the case when there is a Page character $\chi^*$, write $r\le Q_0$ for its primitive conductor, $\beta$ for its real zero, and $r_{\rm odd}$ for the odd part of $r$. With $c_t$ the usual Ramanujan sum, define the linear functional of an actual right coefficient $A(m)$ by

$$
 \mathcal H(A)=-\frac r{\varphi(r)}
 \sum_{n\in I\cap\mathbb Z}\omega(n)n^{\beta-1}\chi^*(n)
                    \mathcal C(n)A(N-n),\qquad
 \mathcal C(n)=\sum_{\substack{t\le Q_0/r\\(t,r)=1}}
                                  \frac{\mu(t)c_t(n)}{\varphi(t)} .
$$

Without such a character all these corrections are zero. In the notation of the [above-BV decomposition](r66-spectral-above-bv-strip-deletions.md) and the [genuine mixed parity law](r80-spectral-whole-mixed-parity-density.md), write $A_0=M_>$, $A_1=\mu(m)M_>$, with both zero off squarefree $m$ in $V$. These are the two four-factor arrays on squarefree pairwise coprime $a,b,c,d$ with product $m$, actual gates $D<\min(ab,ac)<\sqrt m$ and $abc>H_0$, and mark

$$
                    W(m,a,c)=1-\frac{2\log(ac)}{\log m}.
$$

The signs are respectively $\mu(b)\mu(c)$ and $\mu(a)\mu(d)$. In particular a variable called unsigned here still has its literal squarefree and coprimality tests. Put $T=Y^{1/10}$. Form $A_0^{\rm ss}$ by retaining precisely $a,d\le T$ in $A_0$, and $A_1^{\rm ss}$ by retaining precisely $b,c\le T$ in $A_1$. Those gates are on the individual actual tuple: they are not an independent restriction on the primes of $m$.

**Theorem.** For every $A>0$, uniformly in all the original hard tests, both genuine exceptional corrections of the all-scale formula satisfy

$$
 \mathfrak E_\pm=
      \tfrac12\bigl(\mathcal H(A_0^{\rm ss})
                          \ \pm\mathcal H(A_1^{\rm ss})\bigr)
                +O_A(YG^{-A}).                                  \tag{1}
$$

Specifically, for each of the two discarded genuine arrays one has, with a fixed $C$,

$$
  |\mathcal H(A_i-A_i^{\rm ss})|
       \ll Y^{\beta-1/40}+Y^\beta G^C r_{\rm odd}^{-1/2}
             \qquad(i=0,1)                                     \tag{2}
$$

for sufficiently large $Y$. In the first surviving array both signed factors $b,c$ are $\gg Y^{2/5}L^{-B}$; in the second, the signed factors $a,d$ are respectively $\gg Y^{2/5}L^{-B}$ and $\gg Y^{2/5}$. In particular all four possible surviving signed legs are at least $Y^{.39}$ for sufficiently large $Y$. All arithmetic exceptions in uses of the earlier all-scale formula stay as before; (1) itself is a pointwise comparison of the correction, not a new exception count for the full prime sum.

## 1. Keep the gates when fixing three factors

Fix $i$. Disjointly select the first unsigned variable $v$ of its two displayed unsigned variables which exceeds $T$, using their displayed order. With the other three squarefree and pairwise coprime variables fixed let $h$ be their product, so $m=hv$ and $h\le2Y^{9/10}$. All their values, signs, and any previous-variable length gate are now fixed. The two lower tests $ab,ac>D$, the high test $abc>H_0$, and the product and $n$ cutoffs are intervals in $v$. The upper test $\min(ab,ac)<\sqrt{hv}$ is the union of the two individual upper tests, each an interval after squaring; an individual divisor product either contains $v$ exactly once or is fixed. Consequently the genuine allowed set of $v$ is a union of at most two intervals. Partition it disjointly into intervals with the actual open or closed endpoints (merging overlaps when possible). No upper midpoint test was replaced by a pair of tests. The fixed earlier unsigned-variable gate is either empty or leaves the same intervals. The weight, including the real hard left representative, is

$$
                   \omega(N-hv)(N-hv)^{\beta-1}
                                            W(hv,a,c).
$$

It has norm (supremum plus pointwise variation) $O(Y^{\beta-1})$ across these intervals: the centered mark is the ratio of affine functions of $\log v$, of bounded magnitude and monotone, and the power of $n\asymp Y$ is monotone. The fixed other signs have magnitude at most one. Coefficient endpoints and left test values are therefore preserved by ordinary summation by parts, without any smoothing.

Use the exact subgroup expansion $c_t(n)=\sum_{d_0\mid(t,n)}d_0\mu(t/d_0)$. Only squarefree $t$ with $(t,r)=1$ survive. Fix $t,d_0$. The hard condition $d_0\mid N-hv$ either has no solutions or restricts $v$ to one class modulo $d_0/(d_0,h)$, prime to $r$. Expand

$$
               \mathbf1_{(v,h)=1}=\sum_{\substack{a_0\mid h\\a_0\mid v}}\mu(a_0),
              \qquad \mu^2(v)=\sum_{b_0^2\mid v}\mu(b_0).
$$

There is no extra target-unit restriction in the hard exceptional functional: its genuine right coefficient (1) in the hard transfer is the actual mixed coefficient just specified. In particular a prime dividing $N$ but not $r$ is not removed from that functional by hand.

Cut the $b_0$ sum at $Y^{1/30}$. Keeping the $a_0$ sum inside or restoring its original unit indicator, the absolute large-$b_0$ terms at this $h,t,d_0$ cost at most a constant times

$$
             Y^{\beta-1}\sum_{b_0>Y^{1/30}}
                              \left\lfloor\frac{2Y}{h b_0^2}\right\rfloor
                    \ll Y^{\beta-1}\frac Yh\,Y^{-1/30}.
$$

The floor upper bound holds with no extra unit-count error; the positive range is bounded by $2Y/h$. If the unit expansion is left open, its $Y^{o(1)}$ divisor factor is equally harmless. There are at most $\tau_3(h)$ fixed other triples. Summing their reciprocal harmonic volume costs a fixed log power by expanding $\tau_3$. The entire positive absolute weight sum over $t,d_0$ is $Q_0^{O(1)}=Y^{o(1)}$ even without the condition on $n$; for example use at most $Q_0^2$ pairs and $d_0/\varphi(t)\le Q_0$. The factor $r/\varphi(r)\ll G^C$ is also harmless. The square-label tail is thus $O(Y^{\beta-1/30+o(1)})$.

## 2. Complete character periods except on a thin true divisibility class

For $b_0\le Y^{1/30}$ let $s=[a_0,b_0^2]$. Write $v=sw$. The remaining linear congruence has no solutions or is one residue class for $w$ of modulus $e_0=d_0/(d_0,hs)$, prime to $r$. Thus on this progression $w=w_0+e_0 j$ the exceptional factor is the real character of

$$
                      N-hs w_0-hs e_0 j .
$$

The auxiliary progression variable $j$ is an integer on the actual intervals just proved. A primitive real character has squarefree odd conductor and its $2$-part is at most $8$: for odd $p$ the kernel reducing units modulo $p^k$ to modulo $p$ has odd order, so a real character is trivial there; for $p=2$ any quadratic character on units factors modulo $8$ because the group is generated by $-1$ and $5$ and its squares contain the kernel of reduction modulo $8$. The last assertion also follows directly from the standard unit group $C_2\times C_{2^{k-2}}$. By primitivity its local component at each odd $p\mid r$ is nonprincipal.

If some odd $p\mid r$ does not divide $hs$, this prime does not divide the coefficient of $j$. In a complete period modulo $r$, its local character sums to zero because its argument is a bijective affine map modulo $p$. The other local factors are independent of this variable by the Chinese remainder theorem, even if they sometimes vanish. Thus the complete period has zero sum irrespective of $N$. Every incomplete integer interval in $j$ costs at most $r$ by deleting complete periods, and with the exact BV weight this is $O(rY^{\beta-1})$. For fixed $h$ the choice count for $a_0,b_0$ is at most $\tau(h)Y^{1/30}$. Summing this estimate over the fixed triples, $h\le2Y^{9/10}$, and the absolute $t,d_0$ weights gives

$$
                O(Y^{\beta-1/10+1/30+o(1)}).
$$

Here $r,Q_0$ and the fixed-order divisor bounds have subpower size. This is periodic cancellation in the raw positive leg, not an assertion on $\mu\chi^*$.

On the remaining expansion terms every odd prime of the conductor divides $hs$. Since $v$ is a multiple of $s$, **the actual product integer satisfies $r_{\rm odd}\mid m$ on every such term**, even though the truncated expansion did not require $v$ itself squarefree. Bound these terms absolutely at fixed true $n=N-m$ instead of counting all $t,d_0$ independently. Dropping restrictions only on the absolute coefficients gives

$$
 \sum_{\substack{t\le Q_0/r\\ t\ {\rm sf},\,(t,r)=1}}
       \frac1{\varphi(t)}\sum_{d_0\mid(t,n)}d_0
   \ \le\ \prod_{p\le Q_0}
      \left(1+\frac{1+p\mathbf1_{p\mid n}}{p-1}\right)
   \ll (\log(2Q_0))\,\tau(n)^2.                              \tag{3}
$$

Indeed the ordinary product of $1+1/(p-1)$ is $O(\log(2Q_0))$ by Mertens' product, and each extra local factor is at most $4$ in ratio (even its unnormalized factor is at most $4$). Thus only a fixed-order divisor weight occurs. At this integer $m$ the count of raw quadruples is at most $\tau_4(m)$, and the possible $a_0,b_0$ on any of them cost at most $\tau(v)^2\le\tau(m)^2$: each is a divisor of $v$. The physical hard tests and signs do not increase the bound. Since $\tau_4(m)\le\tau(m)^3$, the total bad absolute contribution is bounded by

$$
        \ll Y^{\beta-1}G^C
             \sum_{\substack{n\in I\cap\mathbb Z\\r_{\rm odd}\mid N-n}}
                   \tau(n)^2\tau(N-n)^5
         \ll Y^\beta G^C r_{\rm odd}^{-1/2}.                  \tag{4}
$$

For the second inequality the progression has at most $O(Y/r_{\rm odd})$ points as $r_{\rm odd}\le Q_0=Y^{o(1)}$. Cauchy separates its count from the full-interval squared weight; another Cauchy separates the two arguments, leaving fixed moments $\sum_{m\le2Y}\tau(m)^k\ll_k YG^{O_k(1)}$. These elementary moment bounds follow from $\tau(m)^k\le\tau_{2^k}(m)$ and counting ordered factors by reciprocal harmonic sums. Thus no subpower loss from the modulus enumeration was silently used against a merely inverse-logarithmic conductor gain. Formula (4) also pays for the factor $r/\varphi(r)$.

Gathering the tail, the zero-mean terms, and (4) proves (2). Classical Siegel in [the all-scale proof, §1](r87-spectral-all-scale-exceptional-left-reduction.md#1-remove-only-multiples-of-the-exceptional-conductor-in-the-auxiliary-calculation) gives $r>G^J$ eventually for every fixed $J$ for this Page choice, since $1-\beta<4a_0/\sqrt G$. As $r_{\rm odd}\ge r/8$, the last term of (2) has every fixed log saving, without using a *lower* bound on $(1-\beta)G$. Intersecting the two parity projectors exactly gives $M_\pm=(A_0\pm A_1)/2$. Apply the old hard transfer (2) with its unchanged additive error to the full $M_\pm$, then subtract the just-bounded actual discarded terms. This proves (1); it does not need a hard-transfer theorem for arbitrary new tuple sectors.

## 3. What truly survives

In $A_0^{\rm ss}$ we have $a,d\le T$. Both lower gates give $b,c>D/a\ge D/T$, which proves the claimed bound. In $A_1^{\rm ss}$ we have $b,c\le T$, so $a>D/T$. Also $a\min(b,c)<\sqrt m$ gives
$abc<\sqrt m\,\max(b,c)\le\sqrt m\,T$, hence $d=m/(abc)>\sqrt m/T$. In particular the literal *minimum* midpoint gate suffices; replacing it by two upper gates would not be justified.

On a target with $r\mid N$, the surviving character can be written exactly as $\chi^*(N-m)=\chi^*(-1)\chi^*(m)$, so each of these two long signed legs carries $\mu(v)\chi^*(v)$. For such a character its reciprocal Dirichlet series can have the possible real pole at $\beta$; the positive-variable periodic argument above supplies no cancellation on those two signed arrays. For general $N$ even that factorization is not asserted. The theorem changes only the explicit exceptional correction and leaves the genuine base and all nonexceptional arithmetic unchanged.
