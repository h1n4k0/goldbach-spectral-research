# The full moving curved cut in a typical-count two-giant carrier

Use the same actual lower prime $s$ and squarefree rough product $W$ as in the [both-parities near-edge theorem](r73-source-both-parities-near-edge-mean-square.md), including its hard size, total count and typical exceptional-count masks. In particular both parities of $\omega(W)$ are allowed, each prime of $W$ is at least $\exp(4T)$, every $s\in[\exp(5T/4),\exp(7T/4)]$ is prime, $W\le X^{\epsilon/2}$ with $\epsilon=1/64$, and $\omega(W)\le2\log\ell$. The parameters and the two excluded prime neighborhoods of the [typical-count construction](r72-source-typical-count-masked-obstruction.md) are unchanged, including $\theta=1/20$. Write $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\mathcal J=[X/2,(1+\Delta)X/2]$, $\mathcal X=[X,(1+\Delta)X]$. The new **fixed integer carrier** is

$$
 n=hF,\qquad h=S f,\quad S=sW,\quad f,F\ {\rm prime},\qquad
 n\in\mathcal J,\qquad
 H_-=\tfrac12\sqrt X e^{-20T}\le h\le H_+=\tfrac14\sqrt X .
 \tag{1}
$$

Thus the short strip near $\sqrt{Q_X}$ is no longer imposed. For each even $N\in\mathcal X$ take $I=I_0$ and let $R^{\rm wide}_N$ denote the exact signed sum (1) of the [joint count theorem](r72-source-joint-middle-count-entropy.md) using (1) on both legs. The operands are actual squarefree $N$-units. Every internal divisor pair satisfying the original strict tests $d>D_N,e>D_N,de>Q_N$ is retained, with $D_N=\lfloor\sqrt N\exp(-20T_N)\rfloor$, $Q_N=\lfloor N\exp(-20T_N)\rfloor$ and $T_N=\log N/\log\log N$. These quantities are not fixed at $N=X$ in the original sum.

**Theorem (unconditional).** For all sufficiently large real $X$,

$$
       \sum_{\substack{N\in\mathcal X\\2\mid N}}
                   |R_N^{\rm wide}|^2\ll_\rho X^3\ell^{-2/5}.
 \tag{2}
$$

For example all but $O_\rho(X\ell^{-1/5})$ even targets in the window have $|R_N^{\rm wide}|\le X\ell^{-1/10}$. This retains the true curved test throughout the widened carrier, including terms with proper divisors of $h$ on either leg. It is a mean-square bound for this two-giant class, not arbitrary-mask cancellation, an all-target bound, a result for the whole middle count block, or Hypothesis S.

## 1. Eliminate the complete giant families with the true tests

For large $X$ the factor $f=h/S$ in (1) is above $X^{.4}$, while $S\le X^\epsilon$ and $F\ge X/(2H_+)>\sqrt N$. The two representations $h=Sf$ and $n=hF$ are unique by prime sizes, and $h$ is composite and squarefree. The same holds on the opposite leg, denoted $m=kG$ with $k=U g$. Thus every prime in either operand is at least $\exp(5T/4)$. Actual exceptional counts and old rough ranges are just as in the near-edge result: the primes $f,F$ and $g,G$ are beyond the upper ends of those subpower ranges and only $W$ and its counterpart supply the count. The two operands in the physical window are central for every target on their sum line.

For fixed opposite $e>D_N$, every label $Fz$, $z\mid h$, passes the individual and curved tests because $F>\sqrt N$ and $\sqrt N(D_N+1)>Q_N$. Their complete signed sum is $-\Lambda(h)=0$. Eliminate this whole family first and then the whole opposite family containing $G$. The genuine remainder on any coprime pair on the sum line is

$$
 -\sigma(h)\sigma(k)
 \sum_{\substack{b\mid h,\ c\mid k\\h/b>D_N,\ k/c>D_N\\(h/b)(k/c)>Q_N}}
       \mu(b)\mu(c)\log(Fb)\log(Gc),
 \qquad \sigma(h)=(-1)^{\omega(W)}=\mu(h),
 \tag{3}
$$

where squarefreeness gives $\mu(h/b)=\mu(h)\mu(b)$. The corresponding expression $\sigma(k)$ uses the other old rough product. In a retained term $bc<hk/Q_N\le \exp(21T)$ uniformly in the target window. This follows from $hk\le X/16$ and $Q_N\asymp X\exp(-20T)$ there. Write $M=\exp(21T)$. Thus we may enumerate only $b,c\le M$. Since $f,g>M$, the respective divisors $b,c$ then divide $S,U$. There is no additional replacement of the original label tests. Every such $b$ has at most a fixed number of prime factors since its primes are at least $\exp(5T/4)$.

The number of enumerated labels on one genuine operand is therefore at most $O((1+\log\ell)^{17})$ by the actual total count gate. In any of the pairings considered below, removing the unit condition on the full convolution gives an individually negligible error. Indeed any nonunit pair with $n+m=N$ has a common prime $p\mid N$, and each possible such prime is at least $\exp(5T/4)$. There are $O(\ell)$ of them and for each there are $O(X/p)$ choices of $n$ by the multiple count. The logarithms are $O(L)$; the label multiplicities above then give an error $O_A(XL^{-A})$ for any fixed $A$, uniformly in $N$. We retain the genuine units in (3) until that comparison.

## 2. Fixed bins and their signed and positive polynomials

Partition the possible values of $\log(h/b)$, with $h$ in (1) and $b\le M$, into fixed half-open bins $J_j$ of width $\Omega=T/\ell=L/\ell^2$. A complete finite cover of $[\log H_--21T,\log H_+]$ needs $O(\ell)$ bins. Any extreme endpoint can be included by one more bin. Introduce the two polynomials, both based on the actual carrier (1),

$$
 \begin{split}
 \mathcal B_j^-(\alpha)
  &=\sum_{h=Sf}\sum_{\substack{F\ {\rm prime}\\hF\in\mathcal J}}
       \ \sum_{\substack{b\mid S,\ b\le M\\\log(h/b)\in J_j}}
       \sigma(h)\mu(b)(\log F+\log b)\,e(\alpha hF),\\
 \mathcal B_j^+(\alpha)
  &=\sum_{h=Sf}\sum_{\substack{F\ {\rm prime}\\hF\in\mathcal J}}
       \ \sum_{\substack{b\mid S,\ b\le M\\\log(h/b)\in J_j}}
       (\log F+\log b)\,e(\alpha hF).
 \end{split}
 \tag{4}
$$

As usual $e(y)=e^{2\pi i y}$. The second sequence is coefficientwise nonnegative. We prove the uniform fourth-mean bounds

$$
       \int_0^1|\mathcal B_j^-(\alpha)|^4\,d\alpha
                         \ll_\rho X^3\ell^{-22/5},\qquad
       \int_0^1|\mathcal B_j^+(\alpha)|^4\,d\alpha
                         \ll_\rho X^3\ell^{-4}.
 \tag{5}
$$

The distinction between the two estimates is only a signed prime-product sum in the major density. The positive bounds will control ambiguity at the true moving boundaries.

For clarity, a simple positive reciprocal profile used repeatedly is

$$
       \sum_{s,W}\frac1{sW}\sum_{\substack{b\mid sW\\b\le M}}1
                                  \ll_\rho\ell .
 \tag{6}
$$

For $s$ its reciprocal mass is bounded and it can enter $b$ or not. On the $W$ alphabet assign $\nu_p=2$ when $p\le M$, $\nu_p=1$ otherwise. Dropping the hard size and count tests in this positive envelope makes the $W$ product $\prod_p(1+\nu_p/p)\ll_\rho\ell$, because doubling the weight only for primes in $[\exp(4T),M]$ costs a bounded factor by Mertens. This also provides an upper envelope for any errors when relaxing the masks in a density calculation. For fixed $S,b$, the admitted $f$ lie in a hard interval of log width at most $\Omega$. They are $\ge X^{.4}$, so their reciprocal mass is $O((1+\Omega)/L)$ by Chebyshev over unit log intervals. Hence

$$
     \sum_{h=Sf}\frac1h
              \sum_{\substack{b\mid S,\ b\le M\\\log(h/b)\in J_j}}1
                              \ll_\rho \ell\,\Omega/L=\ell^{-1}.
 \tag{7}
$$

Here and below the bounded $s$ profile is included.

## 3. Fourth mean of one fixed bin

Use the same Dirichlet arcs as in the proof of the near-edge theorem: $P=L^C$, $Q_0=\lfloor X/P\rfloor$ for fixed sufficiently large $C$, and $\alpha=a/q+\beta$ with $q\le P$, $(a,q)=1$, $|\beta|\le1/(qQ_0)$ on the major arcs. All other $\alpha$ have a reduced Dirichlet fraction with $P<q\le Q_0$ and $|\beta|\le q^{-2}$. The major arcs are disjoint and have total measure $O(P^2/X)$.

On the minors, split $\log F+\log b$ in (4) into two bilinear sums with separated coefficients in $h$ and $F$. Their coefficient-bound products are at most $O(L(1+\log\ell)^{17})$, since $\log b\ll T$ and $\log F\ll L$. The same dyadic splitting and exact half-integer Perron separation from the near-edge theorem apply: $h,F\le X^{.6}$ for large $X$, $hF\asymp X$ in the dyads that meet the true interval, and the integer product tests $hF\in\mathcal J$ remain hard. The bounded Perron twists preserve these coefficient bounds. More explicitly, on lengths $U,V$ with $UV\asymp X$, Cauchy and geometric sums give an upper bound for the square of a rectangle of

$$
 O\!\left(UV L^2 (1+\log\ell)^{34}(1+V/q)(U+q\log(2q))\right).
$$

The reciprocal-distance sum follows by spacing in blocks of length $q/2$, as in the near-edge proof. Here $(1+V/q)(U+q\log(2q))\ll XL^{1-C}+X^{.6}L$. The two dyad/Perron costs are $O(L^2)$ in absolute size, and the half-integer Perron error at height $X^4$ is negligible. By taking $C$ large enough we obtain $\sup_{\mathfrak m}|\mathcal B_j^\pm|\ll_{\rho,K}XL^{-K}$ for any chosen fixed $K$. The ordinary coefficient square norm is at most $O(X L^2(1+\log\ell)^{34})$, even by the trivial support count and the uniqueness of $n=hF$. Thus the minor fourth integral is smaller than $X^3\ell^{-A}$ for any fixed $A$ by choosing $K$ sufficiently large.

On the majors, use Siegel–Walfisz in the **prime $F$ only**, with both the weight $\log F$ and the unweighted prime count. The latter follows from the former by partial summation. The $F$ interval is $\mathcal J/h$, with endpoints $\ge X^{.4}$; the slow phase has total variation $O(1+|\beta|X)$. Summing the complete reduced classes gives $c_q(ah)=\mu(q)$ because every prime dividing $h$ exceeds $P$. All errors, including multiplication by $\log b$, are absorbed in an arbitrary inverse logarithmic bound by (7). Thus uniformly on these arcs,

$$
 \mathcal B_j^\pm(a/q+\beta)
  =\frac{\mu(q)}{\varphi(q)}
        \int_{\mathcal J} e(\beta x)D_j^\pm(x)\,dx
                      +O_{\rho,C,A}(XL^{-A}),
 \tag{8}
$$

where the exact finite real density $D_j^\pm(x)$ is the sum over $S,f,b$ in (7) of $K_x(h,b)/h$, with multiplier $\sigma(h)\mu(b)$ for the minus sign and multiplier $1$ for the plus sign, and

$$
                     K_x(h,b)=1+\frac{\log b}{\log(x/h)}.
$$

In particular the actual logarithm $\log(Fb)$ from (3) has not been shortened. The use of hard interval endpoints in Siegel–Walfisz is valid by counting the exact interval in each class, with a possible single endpoint term negligible at these prime sizes.

We claim uniformly for $x\in\mathcal J$ that

$$
 \begin{split}
 |D_j^+(x)|+X|\partial_xD_j^+(x)|&\ll_\rho \ell^{-1},\\
 |D_j^-(x)|+X|\partial_xD_j^-(x)|&\ll_\rho \ell^{-1-1/10}.
 \end{split}
 \tag{9}
$$

The first line is immediate from (7), since $K_x$ and $X\partial_x K_x$ are bounded. To prove the second, fix $s,W,b$. Apply the ordinary PNT and Abel summation to the reciprocal prime sum in $f$ on its exact interval. With $h=Sf$ the resulting real integral is over
$[H_-,H_+]\cap \exp(J_j)b$, with differential $dh/(h\log(h/S))$. Both $K_x(h,b)$ and $X\partial_x K_x(h,b)$ have uniformly bounded supremum and variation in $h$ over this interval, by their displayed formula and logarithms of size comparable to $L$. The PNT error per reciprocal $f$ interval in each case is $O_A(L^{-A})$, uniformly, since $f\ge X^{.4}$; summing with (6) leaves an arbitrary inverse logarithmic error. The main integral is accompanied by $1/S$ and $\sigma(h)\mu(b)$ as in (7).

Now split $W=W_0W_1$, putting into $W_0$ all its eligible primes in $[\exp(22T),V_X/4]$. This interval is entirely untagged in the true exceptional count and is above $M$. Thus $b\mid sW_1$ is exactly the same test as $b\mid S$, and both the $h$ interval and $K_x(h,b)$ are independent of $W_0$ for fixed $(s,W_1,b)$. The only obstructions to factoring the lower parity sum are the total and size caps, and the smooth denominator $\log(h/S)$.

For the total cap use the reciprocal majorant from (6), in which independent prime occupations have probabilities $(\nu_p/p)/(1+\nu_p/p)$ and total mean $\log\ell+O(1)$. The moment of $2^{\omega(W)}$ is at most $O(\ell)$. Replacing the true $\omega(W)\le2\log\ell$ by the temporary $\omega(W_0)\le3\log\ell$ therefore changes the normalized positive mass by $O(\ell^{-(2\log2-1)})$. The true exceptional count test still depends only on $W_1$. Each such mass error costs at most $O(\ell\Omega/L)$ times its normalized estimate in either of the two densities, from (6) and the log width $\Omega$ of each individual $(s,W,b)$ integral. The logarithmic denominator is comparable to $L$ on the true size gate.

On the temporary low-count support, $\log W_0\le\Delta_0=3(\log\ell)\log V_X=o(L)$. Replacing $\log(h/(sW_0W_1))$ by $\log(h/(sW_1))$ costs $O(\Delta_0/L^2)$ per positive weight. The hard product gate differs from $W_1\le X^{\epsilon/2}$ only if $\log W_1$ is in the interval of width $\Delta_0$ just below $\epsilon L/2$. Its positive weighted reciprocal mass is at most $O((1+\Delta_0)/L)$ times the full $W_1$ profile, even with the weight $\prod_{p\mid W_1}\nu_p$. Indeed on that strip $\log W_1\gg L$; mark the sum $\log W_1=\sum_{p\mid W_1}\log p$, freeze all factors but the marked prime, and note that $\sum \nu_p\log p/p\ll 1+\Delta_0$ in any log interval of this width by Chebyshev. The remaining factors have at most the full profile. Multiplying by the positive low profile and the per-label integral width yields a density error $O((\ell\Omega/L)(1+\Delta_0)/L)$, also for $X\partial_xD$ since the mark $X\partial_xK$ has the same uniform bound. This argument keeps the numerical cap $b\le M$ in the original density and merely overcounts the profile when bounding these positive errors.

After these replacements the weight and other gates are independent of $W_0$. Remove its temporary count bound by the same moment estimate. The signed $W_0$ reciprocal factor is now $\prod_p(1-1/p)$ instead of $\prod_p(1+1/p)$ over its allowed primes. The ratio is $O(\ell^{-2\theta})$ by Mertens, since these primes have reciprocal sum $\theta\log\ell+O(1)$. The remaining profiles, allowing $b$ to vary, are bounded from above by (6). Using $2\theta=1/10$, $\Delta_0/L\ll \ell^{-1+\theta}(1+\log\ell)$ and $\ell\Omega/L=\ell^{-1}$ proves the second line of (9). All enlargements just described occurred inside the real density estimate and not on the genuine Fourier coefficient.

By (9) and integration by parts on $\mathcal J$, the interval transform in (8) is bounded by $O_\rho(\ell^{-1-\gamma_\pm}\min(X,|\beta|^{-1}))$, where $\gamma_+=0,\gamma_-=1/10$ and at $\beta=0$ use $X$. Integrate its fourth power and sum over major arcs; $\sum_q\mu(q)^4/\varphi(q)^3<\infty$. The uniform approximation error has negligible fourth mean from the arc measure bound and arbitrary $A$. Combining with the minors proves (5).

## 4. Reassemble the true moving curve

For a pair of bins declare it accepted if the original three strict tests hold for **every** pair of log labels in the two bins and every even $N$ in the scale window. Declare it rejected if the conjunction never holds there, and ambiguous otherwise. One can use closed bin enclosures in this classification, assigning boundary cases to ambiguity. The exact floors cause no issue: the ranges of $\log D_N,\log Q_N$ over $N\in\mathcal X$ each have width $O(1)$, whereas $\Omega\to\infty$. A bin pair can be ambiguous only if at least one coordinate bin meets the interval of possible $\log D_N$, or if the sum interval of its two bins meets the interval of possible $\log Q_N$. The first two tests each give $O(1)$ exceptional coordinate bins, with $O(\ell)$ possible other bins. For the sum test each fixed first bin has only $O(1)$ possible opposite bins. Thus there are $O(\ell)$ ambiguous pairs. There are at most $O(\ell^2)$ accepted pairs.

On accepted pairs the contribution with the unit comparison of §1 is exactly the negative sum of the corresponding coefficients $[\mathcal B_j^-\mathcal B_k^-]_N$. There is no contribution from rejected pairs. At each target the magnitude of the remaining true terms is bounded by the sum of coefficients $[\mathcal B_j^+\mathcal B_k^+]_N$ over ambiguous pairs, because all their actual terms are present in the corresponding positive convolutions irrespective of target. This bounds the curved moving seams in mean square with no fixed-target distribution claim. In the notation $[\mathcal B_j\mathcal B_k]_N=\int_0^1\mathcal B_j(\alpha)\mathcal B_k(\alpha)e(-N\alpha)\,d\alpha$, Parseval and Hölder give

$$
 \begin{split}
  \|[\mathcal B_j^-\mathcal B_k^-]_N\|_{\ell^2(N)}
                               &\ll_\rho X^{3/2}\ell^{-11/5},\\
  \|[\mathcal B_j^+\mathcal B_k^+]_N\|_{\ell^2(N)}
                               &\ll_\rho X^{3/2}\ell^{-2}.
 \end{split}
$$

Summing in these two groups gives $O_\rho(X^{3/2}\ell^{-1/5})$ and $O_\rho(X^{3/2}\ell^{-1})$, respectively. The nonunit correction is negligible in the same norm. Squaring proves (2). The signs and original logarithms on the moving seams were bounded from above, not replaced by a different asserted main term.

## 5. An occupied new piece where the curve matters

At a large external scale $X$, choose two distinct old lower primes $s,t$ near $\exp(3T/2)$, and on each leg choose the same number $\lfloor(1-\theta)\log\ell\rfloor$ of different old rough primes near $\exp(T\ell^{1/10})$. Take all these primes distinct. The rough factors are in the interior of the true exceptional bands, are above $M$, and give the true typical count, total count, and hard size gate. Their product has log size $O(T\ell^{1/10}\log\ell)=o(L)$. Denote the two lower products $sW,tW'$ by $S,U$. Use the PNT to choose $f,g$ so $h=Sf,k=Ug$ are each in a small fixed proportional window about $\sqrt{Q_X}\exp(6T/5)$; then choose $F,G$ so $hF,kG$ are in the interior of $\mathcal J$. The resulting distinct prime factors make the two operands squarefree and coprime. Their even sum has all the original moving properties. This is outside the near-edge carrier and inside (1).

On each side the only available omitted labels $b,c\le M$ are $1,s$ and $1,t$, respectively, since all other primes in $h,k$ exceed $M$. All four choices pass the individual long tests. The strict product test passes for $(1,1),(s,1),(1,t)$, and fails for $(s,t)$ because $hk/Q_N$ has log $(12/5+o(1))T$ while $\log s,\log t=(3/2+o(1))T$. The two parity factors agree, and the resulting original whole mark is $\log F\log G+\log s\log G+\log F\log t$, which is nonzero. This verifies genuinely new curved-cut coverage, not an aggregate lower bound.
