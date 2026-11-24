# The actual mixed-strip main term for moving hard product tests in a much larger small-prime alphabet

**Scope.** This extends the genuine density-one mixed-strip law to adaptive hard intervals, and more generally bounded-variation tests, of the entire actual small-prime product for a substantially larger alphabet. The test can be chosen separately at every target. It does not control completely arbitrary weights on this larger alphabet, a prescribed even modulus, or weak S.

Use the actual above-BV squarefree mixed cutoff weights $M_\pm$ and the original moving polynomial major and minor arcs of the [whole mixed parity theorem](r80-spectral-whole-mixed-parity-density.md), with its physical $m\in[N/3,2N]$, hard half-open left interval $I\subset(N/2,9N/16]$ and uniformly bounded-BV left weight $\omega$. Thus $M_>$ is the true mixed sum with its sign $\mu(b)\mu(c)$ on pairwise coprime squarefree $abcd=m$, before its external subtraction, and $M_\pm=(1\pm\mu(m))M_>/2$. Write $L=\log N$, $\ell=\log Y$, $v=\log \ell$ on $Y\le N\le2Y$. Set

$$
        Z=\exp\!\left(\frac{v}{(1+\log v)^2}\right),
        \qquad s(m)=\prod_{\substack{p\mid m\\p\le Z}}p .
$$

The comparison $p\le Z$ is literal, including the upper endpoint when integral. For any fixed $C>0$ allow at each target an arbitrary complex function $F_N$ on the integers $1\le s\le\lceil5Y\rceil$ with

$$
   |F_N(s)|\le1,\qquad
   \sum_{s<\lceil5Y\rceil}|F_N(s+1)-F_N(s)|\le\ell^C.
$$

There is no regularity from one target to another. In particular an arbitrary hard interval in the **true whole product** $s(m)$, with either strict or weak endpoints and optionally using only $s(m)>1$, is allowed.

For each fixed $A>0$, outside one family of $O_{A,C}(Y\ell^{-A})$ even targets, simultaneously over all $F_N,I,\omega$, the actual full signed correlation with $F_N(s(m)) M_+(m)$ is

$$
 F_N(1)\Sigma(N)\int_I\frac{\omega(u)}{\log(N-u)}\,du
  +O_{A,C}\left(\frac{\Sigma(N)|I|}{L}\exp(-c(\log v)^2)
                          +Y\ell^{-A}\right),
 \tag{1}
$$

with just the error for $M_-$. The same formula holds on the actual original polynomial major arcs. The constant $c>0$ may depend on the fixed divisor-cut parameters. This assertion is unconditional. Neither the density-one error nor the main term is a prime-representation assertion.

## 1. Auxiliary major arithmetic on the expanded alphabet

Use the exact polynomial encoding in the [coefficient-norm bounded-pattern theorem](r83-spectral-adaptive-bounded-pattern-main.md). Namely let $\mathcal P=\{p:5\le p\le Z,\ p\ {\rm prime}\}$, $R=\prod_{p\in\mathcal P}p$, use ordinary absolutely summable power series in marks $X_p$ with the sum of absolute coefficients norm, and insert the monomial $X((m,R))$ into the true right coefficient. Retain separately the four actual exclusions $(m,r_0)=1$ for $r_0\mid6$, recovering the true pattern at $2,3$ by the same finite difference. Denote this algebra by $\mathscr B$. At the end contraction against the bounded values $F_N(s)$ costs no factor in the $\mathscr B$ major error, independent of any variation.

We check explicitly that the coefficientwise arithmetic in Section 1 of that theorem still applies. The only size requirements in its progression estimates are $R=\exp(o(\log Y))$, $3^{|\mathcal P|}=Y^{o(1)}$, and a fixed log-power bound for $\sum_{s\mid R}s^{-1}$. Indeed $\log R\ll Z=\ell^{o(1)}$ by Chebyshev, $3^{|\mathcal P|}\le 3^Z=Y^{o(1)}$, and $\sum_{s\mid R}s^{-1}=\prod_{p\in\mathcal P}(1+1/p)\ll(1+\log(2Z))^{O(1)}$ by prime harmonic summation. With the other three factors of product $h$ frozen in a large signed sector, the marked signed variable is $s d$ with $(d,h R r_0)=1$, in one class modulo $q/(q,s)$ when the true rational class is possible. Its polynomial length scale is $Y/(hs)$ and its exact hard interval is rescaled by $s$. The unconditionally uniform masked Möbius Siegel--Walfisz estimate of the [squarefree CRT theorem](r63-spectral-full-squarefree-crt-strip.md) therefore still gives each error $O_B(Y/(hs)\ell^{-B})$ with the same phase variation. Summing its coefficient norm loses the reciprocal sum just estimated, not the number of labels. In the bulk and untwisted low mixed term the two counted variables remain polynomial after fixing disjoint marked parts. Their squarefree progression and harmonic-convolution errors save a fixed power as before and can absorb $Y^{o(1)}$ allocation costs; all interval constraints are still evaluated at the actual rescaled variables. These checks use the exact identities before the above/below split on the same $m$, and the true total Möbius twist can still be applied before splitting one signed variable.

All formal local factors are the same marked polynomials as in the bounded-pattern theorem, with an absolute uniform constancy of their sup and variation bound $O(\ell^{C_0}C_1^{\omega(q)}/q)$ for squarefree $q$: an occupied signed label gains reciprocal $1/p$ at a prime of $q$, whereas if both signed labels are unoccupied, the uncompleted local norm gains $O(1/p)$ there. Outside $q$ the norms of the positive-factor local polynomials are no larger than their unmarked unphased positive masses. The left prime Siegel--Walfisz estimate and the averaging bound for the formal Ramanujan tail use no new masks. Therefore on auxiliary arcs of common cutoff $Q_0=\ell^K$ and slow radius $2Q_0/Y$, for a sufficiently large fixed $K$ the actual auxiliary major is given by the completed marked real density up to arbitrary inverse-log error and exceptional budget, uniformly in $I,\omega$ and $r_0$. This assertion uses only the coefficient-norm arithmetic, not the smaller-alphabet minor argument.

## 2. Moving exponential moment and the same exact constant

Let $\delta=(\log Z)^{-1}=(1+\log v)^2/v$, so $0<\delta<1/4$ for all sufficiently large $Y$. In the completed density use the same marked prime ratios and scalar values

$$
 d_p=
 \begin{cases}
 0,&p\mid N r_0,\\
 r_p X_p,&p\in\mathcal P,\ p\nmid N r_0,\\
 r_p,&p\notin\mathcal P,\ p\nmid N r_0,
 \end{cases}
 \quad
 \alpha_p=\frac{d_p}{p+2d_p},\qquad
 P=\prod_p(1-1/p)^2(1+2d_p/p),
$$

where $r_p=(p-1)/(p-2)$ for $p\nmid N$ (such $p$ are odd). In the marked region $p\ge5$ the geometric inverse remains valid and $\|\alpha_p\|\ll p^{-1}$ uniformly; $\|P\|\ll1$. Apart from the moment exponent the primitive calculation in Section 2 of the bounded-pattern theorem is unchanged. For completeness let $\alpha_p^\circ=(p-1)/(p^2-2)$ at odd primes and

$$
 \mathcal A_\delta(w)=\prod_{p\mid w,\ p>2}
                             (1-\alpha_p^\circ p^\delta)^{-1}.
$$

For the marked primitive $R_j(u)=\sum_{n\le e^u,\,(n,j)=1}\mu(n)\alpha(n)$, zero on $u<0$, factor the correcting log-convolution kernel against the ordinary reciprocal Möbius primitive. At a prime $p$, with $\alpha'_p=\alpha_p\mathbf1_{p\nmid j}$, its coefficient for $p^a$, $a\ge1$, is $(1/p-\alpha'_p)p^{-(a-1)}$. Consequently its total norm with weight $e^{\delta\,{\rm shift}}$ is bounded by

$$
 H_j\ll \mathcal A_\delta(N)\mathcal A_\delta(j)
            \exp\!\left(C_2\sum_{p\le Z}p^{-1+\delta}\right)
       \ll \mathcal A_\delta(N)\mathcal A_\delta(j)\,v^{C_3}.
 \tag{2}
$$

At unmarked primes the base factor incurs only $O(p^{-2+\delta})$ beyond one, and deletion at a prime dividing $Nj$ adds the local factor in $\mathcal A_\delta(N)\mathcal A_\delta(j)$, exactly by the scalar correction. The finitely many small-prime exclusion cases are harmless. At marked primes $\|\alpha'_p\|\ll1/p$, giving the indicated extra factors (also valid when the mark has been set to zero). The last estimate uses $p^\delta\le e$ for $p\le Z$ and $\sum_{p\le Z}1/p\ll1+\log\log(3Z)$. All constants can be taken uniform for $0<\delta\le1/4$. Also

$$
 \sum_{\substack{j\ {\rm sf}}}
         j^{1/4}\|\alpha(j)\|^2\mathcal A_\delta(j)^2\ll1
$$

by the same convergent Euler bound, using $\mathcal A_\delta(j)\le\mathcal A_{1/4}(j)$.

The typical size of the **moving** factor $\mathcal A_\delta(N)$ is small enough for the weaker exponential moment. For $m_0=\lfloor v^2\rfloor$, expand $\mathcal A_\delta(N)^{m_0}$ by nonnegative squarefree divisor coefficients. The number of multiples of $d$ in $[Y,2Y]$ is at most $2Y/d$, so its average is at most twice the Euler product with factors $1+(\mathcal A_\delta(p)^{m_0}-1)/p$. Since $\log\mathcal A_\delta(p)\ll p^{-1+\delta}$, when $p\le m_0^2$ we may bound the logarithm of a factor by $O(m_0/p)$, using $p^\delta\le2$ for large $Y$. When $p>m_0^2$, $m_0 p^{-1+\delta}=o(1)$ uniformly, so the summed logarithm of these factors is $O(m_0\sum_{n>m_0^2}n^{-2+\delta})=O(1)$. Thus the full logarithm is $O(m_0\log\log(3v))$. Markov with a sufficiently large fixed constant gives

$$
 \log\mathcal A_\delta(N)\ll \log\log(3v)
 \tag{3}
$$

outside $O_A(Y\ell^{-A})$ targets for every fixed $A$, since $v^2\log\log(3v)\gg Av$. No uniform bound at every $N$ is used.

For $\nu=1,2$ or for the pointwise primitive, splitting its correction shifts at $u_0/2$ yields

$$
 \big\|\,\|R_j(u)\|\mathbf1_{u\ge u_0}\big\|_{L^\nu(du)}
   \ll H_j\big(e^{-c_0\sqrt{u_0}}+e^{-\delta u_0/2}\big)
                   \qquad(u_0\ge1).
 \tag{4}
$$

Indeed the ordinary reciprocal Mertens primitive supplies the square-root exponential tail for short shifts and the $\delta$ moment gives the other tail. For the pointwise version evaluate at $u=u_0$. The whole $L^1,L^2$ norms have bound $O(H_j)$.

In the exact marked parity density, the terminal lengths are $U=(B-B_0)\log L$ and $T(x)=\log(x/D^2)$ with $x=N-u$; both are comparable to $v$. The finite signed cap's distant clipping at $L/10-\log j$ is also harmless: for $\log j\le L/20$ (4) gives errors smaller than all fixed inverse-log powers, while the other $j$ are bounded by the summable weighted Euler tail. At $U$ split $j$ at $e^{U/2}$ and apply (4) past $U-\log j$ for the small $j$, bounding the large $j$ by their weighted norm tail. In the autocorrelation outside $[-T,T]$ and at the endpoint $T$, at least one primitive coordinate is at least $T$, so use (4) there and a whole $L^1$ or $L^2$ bound for the other. On (3), (2) gives at most fixed powers of $v$ times the convergent $j$ factors. Since $\delta v=(1+\log v)^2$, all these replacements, including the explicit factors $T(x)$ in the exact density, have error $O(\exp(-c(\log v)^2))$ in the completed bracket's norm. The local integrated infinite constant is unchanged: the factor for the integrated signed quadratic is $(1-2\alpha_p)/(1-1/p)^2$, so multiplying by the corresponding factor in $P$ gives identically one in $\mathscr B$. This is precisely the convergent coefficientwise identity, not averaging the marker over any probabilistic model. The actual scalar parity density therefore retains only the empty pattern in its leading even term, with the stated coefficient-norm error. Finite differences restore the exact two possible low tags as before; the terms requiring either low prime present have zero leading coefficient.

## 3. One true product axis replaces summing all pattern labels on the auxiliary minor

For the auxiliary complement, use the fixed-arc maximal Bessel argument of the [true moving divisor-label minor theorem](r80-spectral-adaptive-divisor-label-minor.md) in the form used in the [whole mixed parity proof](r80-spectral-whole-mixed-parity-density.md). Add **one** further fixed integer coordinate to each actual four-factor tuple: its value is the true $s(m)$ above, computed once on the common scale $Y$. It divides the genuine $m\le5Y$ and is fixed independently of the target. A prefix condition $s(m)\le t$ therefore uses one extra dyadic interval axis in a fixed polynomial-size integer universe. The rest of the proof (true label constraints, exact signs and parity, hard left intervals, fixed auxiliary arc set and its actual left prime supremum) is unchanged.

At each fixed choice of canonical levels an original tuple contributes to exactly one cell, including on this new axis. Summing squared right cell norms still costs at most $\sum_{m\le5Y}\tau_{16}(m)$, up to fixed log powers for the numbers of levels and the left partial summations. No sum over a pattern catalogue enters this bound. The auxiliary prime supremum and disjoint-interval square bound therefore give a joint prefix-maximal squared estimate $O(Y^3\ell^{C_4}Q_0^{-1/2})$, simultaneously over the prefix endpoint and the original right and left hard cuts, by the same disjoint-cell Bessel proof; $C_4$ is fixed, independent of $K$. This is the fixed auxiliary complement, not a replacement of the final moving polynomial arcs.

Discrete partial summation writes each $F_N(s(m))$ as a linear combination of such prefixes with total absolute coefficients at most $1+\ell^C$. This use of variation is on the actual integer product coordinate, and applies even if the function and all its breakpoints are different at different $N$. Choosing $K$ larger and applying Markov against this fixed log loss makes the true auxiliary minor $O_{A,C}(Y\ell^{-A})$ outside $O_{A,C}(Y\ell^{-A})$ targets, simultaneously over these multipliers. Adding the auxiliary majors yields the actual full correlation (1) by ordinary Fourier inversion.

Finally the [adaptive whole-pattern minor estimate](r81-spectral-adaptive-prime-pattern-minor.md) applies directly on the original moving arcs, since $Z\le \log Y$ and the full true small-prime product (even without a variation assumption) is an allowed bounded selector there. Subtract this genuine original minor, power-small outside a power-small exceptional family, from the actual full result. This proves the original major assertion with the one simultaneous exceptional set. The variation condition is essential to the auxiliary-minor argument used here; the coefficient-norm major proof does not on its own justify the full theorem for arbitrary weights on the enlarged alphabet.
