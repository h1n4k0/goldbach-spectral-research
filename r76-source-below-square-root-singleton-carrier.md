# Below the square root: the true singleton correction on the near-giant carrier

Use the $s,W,U$ alphabets, squarefreeness, exact exceptional count of $WU$, exclusions around the exceptional endpoints, and dynamic upper rough split of the [growing-residual theorem](r75-source-dynamic-giant-growing-rough-residual.md). Thus $X$ is real and large, $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\theta=1/20$, $\mathcal J=[X/2,(1+\Delta)X/2]$, $\mathcal X=[X,(1+\Delta)X]$, and $V_X^2\le Z\le X^{\delta_0}$, uniformly, with fixed $\delta_0$ as there. Each $s$ is a single prime in $[\exp(5T/4),\exp(7T/4)]$, $W$ has the exact old size and count gates and uses allowed primes from $\exp(4T)$ to $Z$, and $U>1$ is squarefree with allowed primes strictly above $Z$, without an imposed arity cap. Both parities are used. The selected count of $WU$ is within $2(\log\ell)^{3/4}$ of $(1-\theta)\log\ell$; prime exclusions make it the same exact integer count in the actual exceptional band throughout $N\in\mathcal X$. The fixed $\rho,\Delta$ ensure that every pair in $\mathcal J^2$ with sum $N$ is central.

The difference is the **actual target-dependent carrier**: both operands have the form $n=hF\in\mathcal J$, $h=sWU$, $F$ prime, and

$$
                   F\ \ge\ \mathcal F_N:=\sqrt N\exp(-T_N),
          \qquad T_N=\log N/\log\log N,
 \tag{1}
$$

with the reflected condition on $m=kG$. In particular a selected prime may lie below $\sqrt N$. There is no additional cap on the largest prime of $U$ and no fixed $h$ window. The true moving integer cutoffs $D_N=\lfloor\sqrt N\exp(-20T_N)\rfloor$ and $Q_N=\lfloor N\exp(-20T_N)\rfloor$, all strict long and curved tests, the squarefree $N$-unit requirement, and the minus sign of the [joint-count central sum](r72-source-joint-middle-count-entropy.md) are unchanged. Write $R_{N,Z}^{\rm near}$ for this signed sum on $n+m=N$ at $I=I_0$.

**Theorem (unconditional).** Uniformly in the same range of $Z$,

$$
       \sum_{\substack{N\in\mathcal X\\2\mid N}}
                    |R_{N,Z}^{\rm near}|^2\ll_\rho X^3\ell^{-1/5}.
 \tag{2}
$$

For example all but $O_\rho(X\ell^{-1/10})$ even targets satisfy $|R_{N,Z}^{\rm near}|\le X\ell^{-1/20}$. This controls genuine below-square-root terms in the indicated class. It is a mean-square result on a specific carrier, not a pointwise estimate, an estimate for arbitrary no-giant pairs, or Hypothesis S.

## 1. Exact orbit algebra, including the singleton

Put $F_0=\sqrt X e^{-T}$. The function $\mathcal F_N$ increases on this scale for large $X$, and $\log(\mathcal F_N/F_0)=O(1)$. We can therefore examine the fixed wider comparison $F,G\ge F_0$ first. In this comparison $F$ is automatically the unique largest prime of $n$: if any prime of $h$ were at least $F$, it and $F$ would leave a remaining product $O(e^{2T})$. But the true typical count supplies at least one third prime above $2V_X$, distinct from these two since they are above the entire exceptional band, and $2V_X\gg e^{2T}$. This is impossible. The same size contradiction excludes a second copy of $F$ in the factorization. Consequently the fixed comparison is squarefree and factorization into $F,s,W,U$ is unique. No extra primality selector on the largest prime of $U$ is necessary.

All $F,G\ge F_0$ individually exceed $D_N$, and $FG>Q_N$. Every prime of $h,k$ is at least $\exp(5T/4)$. Thus if $z\mid h$, $z>1$, then $Fz>\sqrt N$ and $(Fz)e>Q_N$ against every opposite long integer $e>D_N$, using $\sqrt N(D_N+1)>Q_N$. The complete family containing $F$ has summed signed weight $-\Lambda(h)=0$, since $h$ is composite and squarefree. The only label in this family whose product test can fail is $F$ itself, with weight $-\log h$. It is excluded exactly when $Fe\le Q_N$, including equality. Hence for each fixed opposite long label,

$$
 \sum_{\substack{z\mid h\\Fz>D_N,\ (Fz)e>Q_N}}
         \mu(Fz)\log(h/z)
       =(\log h)\mathbf1_{\{Fe\le Q_N\}}.
 \tag{3}
$$

The family-containing-family interaction is zero because every product is at least $FG>Q_N$ and the two complete sums are zero. It follows that after the global minus sign the true pair consists exactly of the following three families:

$$
 \begin{split}
 -\mu(h)\mu(k)
    \sum_{\substack{b\mid h,\ c\mid k\\h/b>D_N,\ k/c>D_N\\(h/b)(k/c)>Q_N}}
        \mu(b)\mu(c)\log(Fb)\log(Gc),\\
 -(\log h)\mu(k)
    \sum_{\substack{c\mid k\\k/c>D_N,\ F(k/c)\le Q_N}}
        \mu(c)\log(Gc),\\
 -(\log k)\mu(h)
    \sum_{\substack{b\mid h\\h/b>D_N,\ G(h/b)\le Q_N}}
        \mu(b)\log(Fb).
 \end{split}
 \tag{4}
$$

Here $\mu(h/b)=\mu(h)\mu(b)$ on true squarefree support. In particular the singleton side in each mixed family has the **positive** weight $\log h$ or $\log k$ before the global minus, without a parity sign.

All contributing $h,k$ lie in the fixed window

$$
 \mathcal H=[H_-,H_+],\qquad
 H_-=\tfrac12\sqrt X e^{-20T},\qquad
 H_+=\frac{(1+\Delta)X}{2F_0}.
 \tag{5}
$$

Indeed ordinary long labels require the corresponding cofactor greater than $D_N>H_-$; a singleton interaction implies $F\le Q_N/(D_N+1)<\sqrt N$, so $h=n/F\gg\sqrt X$. The upper bound follows from the fixed prime floor. The ordinary label removals satisfy $bc<hk/Q_N\ll \exp(22T)$; a mixed removal satisfies $c<k/D_N\ll\exp(21T)$ or the reflection. We may therefore enumerate $b,c\le M=\exp(24T)$ in every family in (4). Since $Z\gg M$, the removals divide the corresponding $sW$. Each has at most a fixed number of prime factors, because its primes are at least $\exp(5T/4)$. There are $O((1+\log\ell)^{20})$ enumerated labels at a fixed operand by the actual $W$ count. Thus a nonunit correction on any of these comparisons is individually $O_A(XL^{-A})$ for all fixed $A$: any common prime divides $N$, there are $O(\ell)$ such possible primes $\ge\exp(5T/4)$, and there are $O(X/p)$ possible first operands per prime. Polynomial logarithmic weights and the label counts are harmless. The genuine pairs in (4) retain the unit requirement up to these comparisons.

## 2. A fixed prime-band estimate with moving real endpoints

We record the slight extension of the [wide curved bin estimate](r74-source-full-curved-two-giant-mean-square.md) and the count-restricted rough density of the growing-residual theorem that is needed here. All polynomials are on the true arithmetic carrier with $h\in\mathcal H$, $n=hF\in\mathcal J$, fixed $F\ge F_0$, and the exact old factor and count tests. The optional prime band $\mathcal F\subseteq[F_0,\infty)$ below is a fixed hard interval, not a target-dependent selector.

- A **label polynomial** has an optionally fixed hard bin $J$ for $\log(h/b)$, with $b\mid sW$, $b\le M$. Its mark is $\log F+\log b$, with sign $\mu(h)\mu(b)$ in the signed version and sign $+1$ in the positive version. It can also impose $F\in\mathcal F$.
- A **singleton polynomial** has a fixed hard prime band $F\in\mathcal F$ and the positive mark $\log h$; there is no $b$ label.

Let $\mathcal D$ bound the logarithmic width allowed for $h$ at each fixed real $x\in\mathcal J$, for each fixed $b$ when present. Thus a label bin of log width $\Omega$ allows $\mathcal D=\Omega$ even with an additional prime band; a prime band of log width $\Omega$ also allows $\mathcal D=\Omega$ with or without labels. If there is no bin or finite band, $\mathcal D=O(T)$ is sufficient. For our widths $\Omega=L/\ell^2$, $O(T)$, or $O(1)$, the fourth-mean bounds are

$$
 \int_0^1|\mathcal B^-|^4\,d\alpha
     \ll_\rho X^3\bigl((\ell\mathcal D/L)\ell^{-1/10}+\ell/L\bigr)^4,
 \qquad
 \int_0^1|\mathcal B^+|^4\,d\alpha
     \ll_\rho X^3\bigl(\ell(\mathcal D+1)/L\bigr)^4 .
 \tag{6}
$$

The positive bound also applies to the singleton $\mathcal A$, and for a bounded or empty interval use an upper width bound with $\mathcal D+1\ge1$. The extra $\ell/L$ term accounts for moving real endpoints, not a hard-endpoint smoothing.

On the minors this follows by exactly the fixed log-bin argument: dyadically split $h,F$, separate the hard $hF\in\mathcal J$ by the half-integer Perron integrals, and apply bilinear Cauchy to the coefficients in the two variables. The fixed extra prime band is part of the coefficient in $F$. Splitting $\log F+\log b$ gives two separated terms, while $\log h$ is already an $h$ coefficient. Uniqueness and the label cap give a product coefficient bound $O(L(1+\log\ell)^{20})$. On relevant rectangles both variables are below $X^{.6}$ and their dyadic scales multiply to $\asymp X$. The same reciprocal-distance estimate on reduced $P<q\le X/P$, $P=L^C$, together with the two logarithmic losses from Perron and dyads, gives a supremum $O_K(XL^{-K})$ on the minor arcs for sufficiently large fixed $C$. The ordinary coefficient energy is at most $O(X L^2(1+\log\ell)^{40})$. This is more than enough for the minor fourth means in (6). All these comparisons use the actual hard interval in $hF$.

On a major arc of reduced denominator $q\le P$ use ordinary Siegel–Walfisz in the prime $F$ alone, including the hard band and both the weighted and ordinary prime counts. The rational factor is $\mu(q)/\varphi(q)$ because $h$ only has primes exceeding $P$. For a label the real mark is

$$
           K_b(x,h)=1+\frac{\log b}{\log(x/h)};
$$

for a singleton it is $K_*(x,h)=\log h/\log(x/h)$. Both are uniformly bounded with bounded variation in $h$ on their ranges, and their $x$ derivatives are $O(1/X)$ there. An exact finite real density is obtained by summing these marks with weight $1/h$, multiplying by the required sign, and imposing the label and prime bands with $F$ now the real value $x/h$. All existing support endpoints cost bounded jumps in the prime comparison; each sum over $h,b$ has total reciprocal weight $O(1)$ by the rough density estimate below, so the error is $O_A(XL^{-A})$ for every fixed $A$. In the singleton case there is no label sum.

For each fixed $s,W,b$ replace the reciprocal prime-product measure of $U$ by the count-restricted continuum density $\varrho_{\zeta,K}$ of the growing-residual theorem: $K$ is the **actual** allowed tag count after that of $W$ is subtracted, and $\zeta=-1$ in the signed case, $+1$ otherwise. That estimate holds uniformly on the hard $h$ interval at each $x$, with the bounded-variation marks here, and gives arbitrary inverse logarithmic error. Indeed the arguments $\log(h/(sW))/L$ are in $[.4,.6]$, all factors of $U$ are bounded by $h<X^{.6}$ so its old $.7$ cutoff is immaterial, and no additional upper endpoint enters the count-restricted renewal kernel. The same uniform $\|\varrho_{\zeta,K}\|_\infty+\operatorname{Lip}(\varrho_{\zeta,K})=O(\tau^{-1})$, $\tau=\log Z/L$, applies. The aggregated error from prime-product replacement is superlogarithmic by the labeled reciprocal profile $O(\ell\tau)$ over $s,W,b$. This profile is unchanged except that the doubling of prime weight on the small removal alphabet now ends at $e^{24T}$, still of bounded reciprocal mass.

Thus the real continuum density at a physical $x$ is a sum of integrals in $dv$, $v=\log h/L$, of the mark times $\varrho_{\zeta,K}(v-\log(sW)/L)$, with the lower weight $1/(sW)$ and the outside parity and label signs. For every fixed $b$, its integrated interval is the intersection of the fixed $h$ window, the label bin shifted by $\log b$ if present, and

$$
                 \log h\in \log x-\log\mathcal F .
 \tag{7}
$$

For a singleton use the same interval without a label bin. It is independent of $W$ once the label is specified. The positive continuum supremum is therefore $O_\rho(\ell\mathcal D/L)$ from the marked rough density and the reciprocal profile. For the signed continuum take the independent untagged low factors of $W$ from $[\exp(25T),V_X/4]$, wholly above $M$. The same calculation as in the growing-residual theorem works for every such integrated interval: the numerical label cap, tag-count selector and interval (7) are all independent of these factors after the split. The weighted positive total-count tail costs a relative $O(\ell^{-(2\log2-1)})$. On the temporary low-count support shifting the Lipschitz argument costs $O(\Delta_0/L)$ with $\Delta_0=3(\log\ell)\log V_X$, and the hard $W$ size ambiguity costs $O((1+\Delta_0)/L)$ by tagging one large accumulated prime with weight $\log p$. Factoring the full low signed reciprocal Euler product then gives $\ell^{-2\theta}=\ell^{-1/10}$ relative to the positive profile. Thus the continuum supremum is $O_\rho((\ell\mathcal D/L)\ell^{-1/10})$ in the signed case, with the same bound for the scaled derivative of the mark on a fixed $h$ interval. These are density estimates only: the actual integer polynomials keep every count and size condition.

For clarity about the extra real endpoint, use the continuum density just constructed **before** taking its variation in $x$. Between two physical values $x,y\in\mathcal J$, the symmetric difference of the two intervals in (7) for each label has normalized length at most $2|\log x-\log y|/L$, even after clipping by the fixed intervals. Charge this difference to the positive density bound, giving $O_\rho(\ell|\log x-\log y|/L)$. On the common part apply the previous signed or positive calculation to the difference of the two marks, which is $O(|x-y|/X)$ with the same uniform bounds after dividing by $|x-y|/X$. The continuation of the count-restricted density itself is independent of $x$. The total variation in $x$ is consequently bounded by the corresponding supremum estimate plus $O_\rho(\ell/L)$. This handles the discontinuities of the original hard prime-band comparisons without differentiating a discrete prime trace. The superlogarithmic pointwise replacement error is integrated directly in the major approximation.

The real transform is now bounded by the indicated density size plus variation times $\min(X,|\beta|^{-1})$ on each major arc. Summing the fourth powers uses $\sum_q\mu(q)^4/\varphi(q)^3<\infty$, the real integral $O(X^3)$ of $\min(X,|\beta|^{-1})^4$, and the superlogarithmically small errors on a major set of measure $O(P^2/X)$. This completes (6).

## 3. True moving tests, prime-floor sliver and mean square

First use the fixed comparison $F,G\ge F_0$. Put $\Omega=L/\ell^2$ and divide the possible values $\log(h/b)$ into $O(\ell)$ bins of width $\Omega$ covering their hard range from (5) and $b\le M$. Along $\mathcal X$, both $\log D_N$ and $\log Q_N$ have ranges of width $O(1)$ after the true integer floors. The usual grid classification uses the original moving tests: a bin pair is accepted only if its entire rectangle passes for every target, rejected if no point passes, and ambiguous otherwise. Closed enclosures may be used to flag boundary cases as ambiguous. For the ordinary row of (4), each individual cut meets only $O(1)$ coordinate bins and the sum cut meets $O(1)$ opposite bins per first bin. Thus there are $O(\ell^2)$ potentially accepted pairs and only $O(\ell)$ ambiguous ones. For each accepted pair the true signed coefficient is exactly the convolution of the two signed label polynomials, with the external minus. The ambiguous coefficients are dominated by the corresponding positive convolutions. From (6) the accepted pairs contribute $\ell^2(N)$ norm $O_\rho(X^{3/2}\ell^{-1/5})$, and the ambiguities contribute $O_\rho(X^{3/2}\ell^{-1})$, by Parseval, Hölder and summation.

For the second row of (4), the singleton coordinate only needs $F\le Q_N/(D_N+1)<\sqrt N$. Cover its fixed possible range $[F_0,\sqrt{(1+\Delta)X}]$ by $O(\ell)$ hard log bins of width $\Omega$. Grid those bins against the old log-label bins for $e=k/c$. Classify by the actual tests $e>D_N$, $Fe\le Q_N$. The weak product test stays weak, exactly as in (3). The singleton pair count is again $O(\ell^2)$ clear and $O(\ell)$ ambiguous by the single-coordinate and diagonal seams, using the same integer threshold ranges. An accepted pair is precisely a singleton positive polynomial times the opposite signed label polynomial at coefficient $N$, with the minus sign of (4); the ambiguous set is dominated by positive singleton times positive label convolutions. From (6), for each accepted bin pair the product of the fourth norms is $O_\rho(X^{3/2}\ell^{-2-1/10})$, and for each ambiguous pair it is $O_\rho(X^{3/2}\ell^{-2})$. Summing all such pairs gives $O_\rho(X^{3/2}\ell^{-1/10})$ in $\ell^2(N)$, also for the reflected third row. No cancellation on the singleton leg is used or claimed.

To restore the actual prime floor (1), a difference in the count of an actual pair requires one selected prime in the fixed band $[F_0,\max_{\mathcal X}\mathcal F_N]$, of logarithmic width $O(1)$. Formula (4) is valid on both comparisons, and all its terms are bounded in magnitude by constant multiples of products of the positive all-label marks. Here $\log h\ll\log F$ on (5) and the label list includes $b=1$, so this also covers the singleton terms. Take the corresponding positive all-label polynomial with the fixed prime sliver and compare it against the full opposite all-label polynomial. The two positive fourth means in (6) have $\mathcal D=O(1)$ and $O(T)$ respectively, giving a mixed $\ell^2(N)$ norm $O_\rho(X^{3/2}\ell/L)$. This bounds the error of the actual target-specific prime condition, without modifying its true threshold. Together with the individual unit comparison, all errors are smaller than the claimed total $\ell^2(N)$ norm $O_\rho(X^{3/2}\ell^{-1/10})$. Squaring proves (2).

## 4. Occupied below-square-root support

Here is an example with exactly one of the two new mixed terms genuinely nonzero. Set $Z=V_X^2$ and choose distinct $F,G$ near $\sqrt X e^{-T/2}$. On each side choose the same number $\lfloor(1-\theta)\log\ell\rfloor$ of distinct upper tagged primes near $\exp(3T\ell^\theta)$, all in the interior of the actual exceptional interval. Choose distinct lower $s,t$ near $\exp(3T/2)$. On the first side use $W=1$, on the second let $W$ be one untagged prime $p$ near $\exp(81T/4)$; it belongs to $W$ for large $X$. Complete $U$ on each side with two free prime factors of size $X^{1/4+o(1)}$, adjusting the second to put $hF,kG$ strictly inside $\mathcal J$. The ordinary PNT supplies these in narrow fixed proportional intervals because the tagged products have log size $o(L)$. All primes can be chosen distinct, so the actual even target has genuine squarefree units and $F,G<\sqrt N$ but $F,G>\mathcal F_N$.

For these operands the available $b\le M$ are $1,s$ and the second removals are $1,t,p,tp$. Relative to $\sqrt X$, $k/p$ is near $\exp(-79T/4)$ up to bounded factors. Hence $D_N<k/p<Q_N/F$, while $k/(tp)<D_N$ and $k,k/t>Q_N/F$. The reflected singleton has no qualifying mate. The ordinary row includes all four pairs $b\in\{1,s\}$, $c\in\{1,t\}$ and one additional pair $(1,p)$: its mate $(s,p)$ fails the curved product test and $tp$ fails the individual test. All margins are exponential in $T$, hence stable under the actual $N/X$ and the floor changes. Since $\mu(h)\mu(k)=-1$, the total original mark is

$$
             \log s\log t+
                      \bigl(\mu(k)\log h-\log F\bigr)\log(Gp).
$$

It is nonzero: if $\mu(k)=+1$, then $\log h-\log F=T+O(1)>0$ up to the fixed proportional choices; if $\mu(k)=-1$, the negative quadratic-in-$L$ term dominates $\log s\log t=O(T^2)$. The newly accounted singleton term is therefore an actual part of the strict curved sum below the square root. This is a support witness, not a lower bound on a summed correlation.
