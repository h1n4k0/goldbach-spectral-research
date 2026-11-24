# The genuine mixed-strip main term survives adaptive exclusion of small primes

**Scope.** This is an unconditional density-one result for the actual above-BV squarefree mixed coefficient. It shows that its even-parity signed leading term survives requiring its actual right integer to avoid any chosen subset of sufficiently small primes. The excluded part has no leading term in either parity. The subset may depend on the target, with one simultaneous exceptional set. This is a statement about signed cutoff weights, not a prime-counting, pointwise full/minor, or weak S theorem.

Keep the $M_\pm$, actual original polynomial major and minor arcs, genuine hard central intervals $I$, and uniformly bounded BV left weights $\omega$ of the [whole mixed parity theorem](r80-spectral-whole-mixed-parity-density.md). In particular $M_>(m)$ is the true signed sum before its external subtraction, with cutoffs $D=\sqrt N(\log N)^{-B}$, $H_0=\sqrt N(\log N)^{-B_0}$, fixed $B>B_0>0$, and right physical gate $m\in[N/3,2N]$. Subscripts $+$ and $-$ are true even and odd squarefree factor count. Write $L=\log N$, $v=\log\log Y$ for the scale $Y\le N\le2Y$, and set $z=v^2$. The precise small-prime endpoint is interpreted literally on integer primes.

For each target $N$, let $r$ be **any** squarefree divisor of $\prod_{p\le z}p$ and define the actual right coefficients

$$
 M_\pm^{(r)}(m)=\mathbf1_{(m,r)=1}M_\pm(m).
$$

For some fixed $c>0$, each fixed $A>0$, and outside $O_A(Y(\log Y)^{-A})$ even targets, simultaneously over all such $r$ and every usual $I,\omega$, the **full signed correlation** with $M_+^{(r)}$ is

$$
 \Sigma(N)\int_I\frac{\omega(u)}{\log(N-u)}\,du
   +O_A\!\left(\frac{\Sigma(N)|I|}{L}e^{-c\sqrt v}
                          +Y L^{-A}\right),
 \tag{1}
$$

and that with $M_-^{(r)}$ consists only of the stated error. The same holds for the genuine original moving polynomial-major integrals. In particular $r=\prod_{p\le z}p$ imposes the actual roughness condition $P^-(m)>z$. Subtracting from the case $r=1$ shows that the true complement $(m,r)>1$ has zero leading term in both parities, under the same simultaneous uniformity. No positivity is inferred for either summand.

## 1. The exact restricted arithmetic and its completion

Work on the fixed common auxiliary arcs with reduced $q\le Q_0=(\log Y)^K$ and slow radius $2Q_0/Y$, where $K$ may later be chosen large. The identity $M_>+M_\le=-\Xi_D$ of the [exact decomposition](r66-spectral-above-bv-strip-deletions.md) holds after multiplying every term by $\mathbf1_{(m,r)=1}$, and after any total Möbius twist. In its pairwise-coprime squarefree factorization $m=abcd$, the mask is exactly the exclusion of primes dividing $r$ in each of the four factors.

The arithmetic underpinning the genuine auxiliary major in §1 of the whole mixed parity theorem survives this exact additional coprimality. First, the masked Möbius and squarefree residue estimates of the [squarefree CRT calculation](r63-spectral-full-squarefree-crt-strip.md) with a coprimality parameter $w\le Y^{O(1)}$ remain uniform: in the signed large-variable interval apply the positive smoothing convolution on the primes dividing $w$, with total reciprocal mass $O(\log\log Y)$ and quarter-power Euler factor $O_\varepsilon(w^\varepsilon)$; on the squarefree count the floor error is $O(\tau(w)\sqrt{x})$ at length scale $x$. These are exactly the proofs of the cited estimates, with the same polynomial length requirement and with $\varepsilon$ chosen small enough. Our added $\prod_{p\le z}p$ is at most $\exp(O(z))=Y^{o(1)}$ by Chebyshev, and is simply included in each relevant coprimality parameter. Thus the pointwise auxiliary errors retain arbitrary inverse-log saving after the phase variation and residue sums. Prime Siegel--Walfisz for the left factor is unchanged.

In the untwisted $\Xi_D$ divide the signed $b,c$ into the two large signed regions and their common small bulk, as in the squarefree CRT calculation. For the twist use the signed $a,d$ regions and their small bulk, as in the [parity formula](r67-spectral-high-mixed-parity-major.md). In either bulk the two counted positive variables are at least $N^{.39}$. The squarefree CRT count for the first positive variable still preserves every hard interval. In the harmonic average of the second, each newly excluded prime has local factor $g(p^j)=0$ for $j\ge1$ and hence convolution with $1$ has only $k(p)=-1$ there, costing at most $O_\varepsilon(r^\varepsilon)$ in the same $3/4$ moment. No other local formula changes on primes outside $r$. The total positivity and real-interval errors therefore have the same power or arbitrary-log savings as before. No assumption about primes in growing moduli is used.

The same direct two-positive-variable calculation applies to the untwisted low mixed term, without invoking any major/minor assertion about the full visible coefficient. Indeed, fix its two signed $b,c$ and put $h=abc$. The gate becomes $D\max(b,c)<h\le H_0$, with $b,c<H_0/D$, and $d$ is in the positive polynomial range above $N/(3H_0)$. The positive variable $a$ is also at polynomial scale at least $N^{.49}$, so the same squarefree residue count in $d$ and harmonic average in $a$ apply, with polynomial-scale endpoints and their literal orientation. The upper strict midpoint gate is automatic as $h\le H_0<\sqrt m$. For the twisted low term the signed $d$ is in this same polynomial range and masked Möbius Siegel--Walfisz gives no leading term, uniformly.

At a prime $p\mid r$, both signed variables are unoccupied and both positive variables are units. In the uncompleted density the local factor is $(1-1/p)^2$ if $p\nmid q$, and $-(1-1/p)^2/(p-1)$ if $p\mid q$: the product of the two uniformly distributed nonzero residues is uniform on the nonzero residues, and its additive phase averages to $-1/(p-1)$. This count holds also for $p=2$. Multiplying by the left rational coefficient and summing $p$ absent or present in $q$ completes this factor to

$$
 (1-1/p)^2\left(1+\frac{c_p(N)}{(p-1)^2}\right)
                      =(1-1/p)^2\Sigma_p(N).
 \tag{2}
$$

Every other prime has the original occupancy and factor of the parity calculation. In particular at $p\mid N$ any right occupied prime has zero completed factor as before.

The right formal sup plus variation bound is still $O(L^C C_1^{\omega(q)}/q)$, uniformly in $r$, also beyond the auxiliary cutoff. Outside $q$ the forced unit local masses can only decrease the corresponding unoccupied masses. Inside $q$ a newly forced unit gives $O(1/p)$ by its exact local phase factor; on any nonexcluded prime, use the genuine reciprocal occupation gain of the original calculation. The same bound holds for the low mixed term just discussed. Therefore the BV slow-radius extension is valid with error $O_A(NL^{-A})$ for large $K$. The actual rational tail is pointwise bounded, after inserting $(q/Q_0)^{1/4}$, by

$$
 O\!\left(L^C Q_0^{-1/4}\mathcal A(N)^{C_2}\right)
$$

in normalized units, by the Euler calculation in the [radical criterion](r81-spectral-radical-criterion-and-log-exceptions.md), with no dependence on $r$. Thus for every target under its stated radical bound, the full rational coefficient may be completed at arbitrary log accuracy uniformly in all the present masks.

## 2. The same nonzero leading constant

For all these real integrations let $r_p$ denote the local ratio from the original parity formula, but set it to zero at $p\mid r$ as well as at $p\mid N$. Define

$$
 P_{N,r}=\prod_p(1-1/p)^2(1+2r_p/p),\qquad
 \alpha_{N,r}(p)=r_p/(p+2r_p).
$$

For squarefree integers extend $\alpha_{N,r}$ multiplicatively. By (2), the exact combined coefficient from the positive variables and the reciprocal weights of the two signed variables, when coprime, is precisely $\Sigma(N)P_{N,r}$ times their two $\alpha_{N,r}$ weights. This includes the low mixed density: its fixed-$b,c$, signed real integral has $u=\log(abc/D)$ from $\max(\log b,\log c)$ to $U=(B-B_0)\log L$, and its centered factor is $2(\Delta(x)-u+\log b)/\log x$ after the $b,c$ sum, where $\Delta(x)=\tfrac12\log(x/D^2)$. The upper untwisted integral and the twisted cap are unchanged as functions of the real variables, since the new exclusions entered only the exact CRT weights. Consequently the same finite signed gcd expansion and partial summation as in the parity formula give its exact completed density with $P_N,\alpha_p,R_{N,j}$ replaced by $P_{N,r},\alpha_{N,r}(p),R_{Nr,j}$. Here $R_{Nr,j}(u)$ is the signed reciprocal Möbius primitive of these $\alpha_{N,r}$ weights with the extra coprimality to $j$; it is zero for $u<0$. One can retain all intermediate finite moments of that formula, using the completely occupied mask $Nr$ in the underlying prime exclusions but **not** replacing $\Sigma(N)$ by $\Sigma(Nr)$. The additive numerator is still twisted by the actual target $N$.

For clarity, the unweighted first signed primitive now has positive smoothing kernel with quarter-power moment $O(\mathcal A(Nr)\mathcal A(j))$, by §2 of the whole mixed parity theorem. Here $\mathcal A$ is as in the radical criterion and $\mathcal A(Nr)\le\mathcal A(N)\mathcal A(r)$. Uniformly in the new mask,

$$
 \log \mathcal A(r)\ll \sum_{p\le v^2}p^{-3/4}
                  \ll \frac{\sqrt v}{\log(2v)}=o(\sqrt v)
$$

by Chebyshev and partial summation. Take a sufficiently small fixed threshold $b\sqrt v$ for $\log\mathcal A(N)$; §2 of the radical criterion allows any fixed $b>0$ with the same arbitrary inverse-log exceptional budget. All the primitive tails at the finite lengths $U$ and $T(x)=\log(x/D^2)$ therefore have the same exponentially small relative bound $O(e^{-c\sqrt v})$ after the integration and the $T(x)$ factors. More explicitly, the error before choosing this threshold is $O(\mathcal A(Nr)^2e^{-c_0\sqrt v})$ in the completed bracket times $P_{N,r}$, by the same $L^1,L^2$ positive kernel tail estimates and convergent $\alpha_{N,r}(j)^2\mathcal A(j)^2$ sum. The long cap truncations at fixed positive multiples of $L$ allow arbitrary inverse-log error.

Finally, the Euler factor of the infinite integrated signed quadratic moment is $(1-2\alpha_{N,r}(p))/(1-1/p)^2$, exactly as in the whole mixed parity theorem. Multiplication by the $p$ factor of $P_{N,r}$ gives one, since

$$
 (1-2\alpha_{N,r}(p))(1+2r_p/p)=1
$$

also where occupancy is forbidden. Accordingly the even bracket has coefficient one and the odd bracket has coefficient zero after the parity half, with the stated small error. This proves (1) on the actual auxiliary arcs, uniformly for all the new coprimality choices, for every target in the explicit good radical family. At $p\mid r$, the factor $(1-1/p)^2$ in (2) alone is not the final leading factor: the signed primitive compensates it exactly.

## 3. One simultaneous family for the two true circle transfers

It remains to estimate the complement of the fixed common auxiliary arcs with the actual, possibly target-dependent, exclusion. Write $R_z=\prod_{p\le z}p$. Use the exact identity

$$
              \mathbf1_{(m,r)=1}=\sum_{\substack{d\mid r\\ d\mid m}}\mu(d).
$$

For each fixed $d\mid R_z$, insert $d\mid m$ as a fixed test in the [arithmetic-label Bessel argument](r80-spectral-adaptive-divisor-label-minor.md). The actual upper midpoint gate and weights are fixed functions of the tuple; the intervals in $m,ab,ac,abc$ are the same true physical and numerical cuts. At fixed canonical levels, positive domination after assigning each tuple once gives the sum of the squared right norms over these cells at most $\sum_{m\le5Y,\ d\mid m,\ m\ {\rm sf}}\tau_{16}(m)$. The common auxiliary complement has the $O(YQ_0^{-1/2}(1+\log Y)^4)$ hard-interval prime supremum of the whole mixed parity proof. Combining its positive disjoint left bound with this right energy gives the corresponding maximal Fourier-coefficient square sum by the same dyadic cells and Parseval, keeping the left BV tests by partial summation. For this fixed arc set the $q,\beta$ axes are not needed.

For the actual divisor-lattice sum at a target, weighted Cauchy loses $\sum_{d\mid R_z}d^{-1/2}=(\log Y)^{o(1)}$ in the square, while its other factor sums the fixed $d$ Bessel squares with weight $d^{1/2}$. Indeed their weighted right energy is at most

$$
 \sum_{\substack{m\le5Y\\m\ {\rm sf}}}\tau_{16}(m)
         \sum_{d\mid(m,R_z)}d^{1/2}
 \ll Y(1+\log Y)^{15}\prod_{p\le z}(1+16p^{-1/2})
      =Y(\log Y)^{15+o(1)}.
$$

For prescribed $d$, the squarefree count $\tau_{16}$ factors at $m=d(m/d)$ and the elementary summatory bound on the second factor is $O((Y/d)(1+\log Y)^{15})$. Both Euler bounds use $\sum_{p\le v^2}p^{-1/2}\ll v/\log(2v)=o(v)$. Thus the summed maximal square over $N$, including the supremum over $r\mid R_z$, is $O(Y^3Q_0^{-1/2}(\log Y)^{O(1)})$. Choose $K$ large and apply Markov at $Y(\log Y)^{-A}$ with a sufficiently stronger log budget; the actual common-complement integral is that small outside $O_A(Y(\log Y)^{-A})$ even targets. This proves the genuine full formulas by ordinary Fourier inversion, not by a conditional pointwise estimate for a prime progression.

For the original moving polynomial arcs, use the [adaptive actual small-prime-pattern minor estimate](r81-spectral-adaptive-prime-pattern-minor.md). The squarefree small-prime product up to $z$ determines $\mathbf1_{(m,r)=1}$ for each of the permitted choices of $r$ at each $N$, and $z\le\log Y$ for large $Y$. Take the fixed common multiplier to be either true parity indicator; the true moving $D,H_0,V$ obey its genuine label intervals. The theorem thus bounds the original minor uniformly over all our choices with a power error outside a power-small exceptional set. Subtract just that moving original minor from the actual full correlation. This proves (1) on the original majors as well, with the one simultaneous exceptional family claimed. In particular no original arc was made smaller in the final statement.
