# R23: giant-prime collapse and a genuine proper-prime-power sector in the rough–rough remainder

Keep the original wide prefix \(b_*=N^{3/40}\), \(X=\lceil4b_*N\rceil\), \(D_*=\lfloor X^{1/3}\rfloor\), \(Q=N^{7/8}\), with even \(N\). Start with the exact R18–R20 rough–rough arithmetic sector: the two long divisors \(d,e>D_*\) with \(de>Q\), both raw integers divisible by at most one distinct prime from \(W=\prod_{p\le\log N,\ p\nmid N}p\), original signed nonzero aliases \(n\pm m=\pm jN\) with the diagonal deleted, and \((nm,N)=1\). The individual arithmetic contribution on each line is normalized by \(1/N\). Under local GRH(N) this is in the manuscript's physical Hardy realization; relating it to the original wide-prefix decomposition additionally uses the GRH hypotheses in R17–R20. The arithmetic estimates below do not assume a prime-pair asymptotic.

Call a raw integer \(n\) **admissible on its giant-prime leg** if
\[
 n=p r,\qquad p \text{ prime},\qquad p>D_*,\quad r\le D_*,\quad pD_*\ge Q.     \tag{1}
\]
No roughness constraint is changed. Then the full genuine long-divisor coefficient on that leg in the actual high-product kernel collapses to \(-\Lambda(r)\), independently of the other long divisor \(e>D_*\). In particular, when \(r\) is not a prime power there is exact zero, including \(r=1\).

Let \(G_L(Y)\) be the part of the rough–rough kernel on which the first leg satisfies (1) and \(r=q^k\ge Y\) for a prime \(q\) and \(k\ge2\); \(G_R(Y)\) is its reflected counterpart. For \(2\le Y\le D_*\), either part and their set-theoretic union have
\[
 \|G(Y)\|_{\rm HS}\ll_\epsilon b_*\,Y^{-1/4}N^\epsilon .                    \tag{2}
\]
For \(Y=N^{1/3}\) the bound is \(O_\epsilon(N^{-1/120+\epsilon})\) on the full wide prefix. This is not a proper-power condition on the original integer \(n\): the integers \(p q^k\) have two distinct prime factors. It is a genuine nonempty part of the rough–rough survivor, as the witness below shows. Neither small proper cofactors, prime cofactors, nor the nonadmissible rough–rough complement are bounded by (2).

## Exact identity, thresholds, and masks

The \(p\) in (1) is unique: any other prime factor is a divisor of \(r\le D_*\). In particular \(p\nmid r\) and \(p^2>n\). Every divisor of \(n\) greater than \(D_*\) is therefore uniquely \(d=p a\), \(a\mid r\), and conversely each such \(p a\) is long. For any fixed \(e>D_*\), its product with \(p a\) is at least \(p e>pD_*\ge Q\). This remains **strict** even if \(pD_*=Q\). In the original region \(de>Q\) the sum over this leg may thus be taken over **all** \(a\mid r\), including \(a=r\), whose log weight is zero. Since \(\mu(pa)=-\mu(a)\) even when \(a\) is nonsquarefree,
\[
 \sum_{\substack{d\mid n\\d>D_*\\ de>Q}}\mu(d)\log(n/d)
      =-\sum_{a\mid r}\mu(a)\log(r/a)=-\Lambda(r).
\]
The masks for a hard rectangle, the chosen signed line and diagonal deletion, and whether one or both raw integers are rough depend only on \(n,m\), not on \(d,e\). The unit condition also does not cut the orbit: \((n,N)=1\) implies \((p r,N)=1\) and every \(d\mid n\) is a unit. Hence the other leg retains exactly \(R_{D_*}(m)=\sum_{e\mid m,e>D_*}\mu(e)\log(m/e)\) after this collapse. If both legs satisfy (1), its coefficient is exactly \(+\Lambda(r)\Lambda(s)\) before the outer line sign. This uses the *rough–rough* component as stated; it would not preserve an extra divisor-dependent good-leg mask from the mixed sector.

A sufficient global subregion for (1) is \(p>X/D_*\) and \(n\le X\). Indeed \(r<X/p<D_*\), \(p>D_*\) since \(X>D_*^2\), and \(pD_*>X>Q\). The inequality \(X>Q\) holds for every sufficiently large \(N\) with these parameters (in fact \(X\ge4N^{43/40}\)). The actual definition (1) is broader and is used in (2).

## Sparse proper powers and the full Hardy norm

Positive integer proper prime powers have counting function at most \(O(\sqrt T\log(2T))\), by summing \(T^{1/k}\) over \(2\le k\le\log_2 T\). Dyadic summation therefore gives
\[
 \sum_{\substack{Y\le r\le X\\r=q^k,\ k\ge2}}\frac1r
          \ll Y^{-1/2}\log(2X).
\]
For each such \(r\), there are at most \(X/r\) possible positive \(p\) with \(p r\le X\); this does not even need their primality. The unique \(p\) makes the classification exact. Each line specifies at most one \(m\) for each \(n\). Its collapsed coefficient satisfies \(|\Lambda(r)R_{D_*}(m)|\ll_\epsilon N^\epsilon\) by the ordinary divisor bound and the log markers. Thus, for every hard rectangle on each actual signed line, the raw coefficient is \(O_\epsilon(XY^{-1/2}N^\epsilon)\). Arbitrary additional \(0/1\) masks depending only on the raw pair, such as the second admissibility condition or its complement, leave this estimate valid. In particular the union can be handled as the disjoint sum of the left condition and the right condition with the left excluded; equivalently subtract their intersection once. No double-counting of simultaneously admissible legs is used.

Normalize by \(1/N\) and sum \(O(b_*)\) aliases, obtaining rectangle bound \(U_0=O_\epsilon(b_*^2Y^{-1/2}N^\epsilon)\). For the actual weighted cumulative \(A(x,y)=\int_{(0,x]\times(0,y]}\sqrt{uv}\,d\mu(u,v)\), positive layer cake gives \(|A|\ll U_0\sqrt{xy}\). The independent bound \(|A|\ll_\epsilon N^\epsilon(xy)^{3/2}\) follows from the original divisor bound or its collapsed version: when \(x\le y\), a nonzero line requires \(y\ge1/2\), so each eligible \(n\le Nx\) has only \(O(y)\) possible \(m\)'s. Interchange coordinates for the other order. In log-physical coordinates the kernel is \(2\pi A/(xy\sqrt{w_N(x)w_N(y)})\), with \(w_N\ge1/2\) for \(x,y\ge1/N\). Multiply the two bounds on \(A\) and integrate on log area \(O((\log N)^2)\). The edge with either coordinate below \(1/N\) has exactly zero cumulative, since no atoms are present there. Taking square roots gives (2), including all internal directions of this actual component. At \(Y=N^{1/3}\), the exponent is \(3/40-1/12=-1/120\).

## Genuine nonempty moving-alias witness

The following supplies admissible signed atoms along infinitely many even \(N\) under the usual global Dirichlet GRH PNT in progressions (the PNT input is only for this example, not (2)). Let \(T\) grow, and choose a power of two \(j\) with \(T^{3/40}/8<j\le T^{3/40}/4\), changing the harmless endpoint convention if a power lies at equality. Choose distinct odd primes \(q,s\asymp T^{1/6}\), both at least \(2T^{1/6}\), from disjoint fixed-ratio intervals by Bertrand. Choose odd primes \(p,p'\) such that
\[
 jT/2\le n=p q^2\le 3jT/5,\qquad jT/2\le m=p' s^2\le 3jT/5,
 \qquad p'\equiv-pq^2(s^2)^{-1}\pmod{2j}.
\]
The first interval for \(p\) and the interval for \(p'\) each have length \(\asymp T^{89/120}\). The latter is a reduced class modulo \(2j\ll T^{3/40}\) since all these primes are odd and \(j\) is a power of two. The [GRH PNT in progressions](https://arxiv.org/abs/2301.13457) gives a main term of order at least \(T^{89/120-3/40}/\log T\) for the prime count in that interval, dominating the square-root error with logarithms. Thus choose distinct \(p,p'\), both much larger than \(q,s\). Put \(N=(n+m)/j\). The congruence makes \(N\) even, \(T\le N\le6T/5\), and \(n,m\le b_*N\) because \(j\le T^{3/40}/4\). Then \((n,m)=1\), since the four primes are distinct, so \(N\mid n+m\) implies \((nm,N)=1\). The raw integers are fully rough for the indicated logarithmic cutoff. Their cofactors satisfy \(N^{1/3}\le q^2,s^2\ll T^{1/3}\ll D_*\), and \(p,p'\asymp T^{89/120}\gg X/D_*\asymp T^{43/60}\). Hence both legs satisfy (1), and this is an actual moving sum alias \(n+m=jN\) in the intersection, with nonzero arithmetic coefficient \((\log q)(\log s)\) before the outer sum-line sign. No difference alias can coincide at this pair for \(N>2\), since that would force \(N\mid2n\) contradicting the unit condition. This is an atom witness, not a lower bound of a size relevant to S.

The estimates above remove just the exact zero or bounded proper-power sectors specified; the surviving prime-cofactor terms and other rough–rough sectors remain open, as do the exterior blocks. No conclusion about S or R follows.
