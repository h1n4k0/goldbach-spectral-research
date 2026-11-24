# Actual minor bounds in narrow offset polynomial-gap windows

**Scope.** This treats genuine largest-two-prime partners whose logarithmic gap lies in a narrow hard window, even when the window is centered at a fixed positive fraction of $\log N$. It refines the [wide even balance argument](r77-spectral-wide-even-balanced-minor.md): we retain the positive local sieve factor in the cutoff energies and use the actual coprime-label signs in the low folds before taking absolute values. The full absolute prime-mass estimate is unconditional. The actual original-$Q$ minor estimate uses the same historical prime-character Dirichlet GRH input as the earlier theorem. This is not a bound across a polynomial-gap interval of width comparable to $\log N$, nor a result on weak S.

Use the same cutoff constants, fixed even radical, original hard left interval $I$ and bounded-variation weight $\omega$, central partner interval $V=[N/3,2N]$, and genuine squarefree coefficient $M_>(m)$ of the [balanced minor proof](r76-spectral-balanced-actual-minor.md). Write $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$. Let $q>p$ be the actual largest two primes of a squarefree $m=pqa$ in $V$. Put $s=\log(ap/D)$, $t=\log(aq/D)$, $h=\log(m/D^2)$. Fix $0<\rho<\upsilon\le3/20$. For any real $H\ge2L^{1/3}$ and $1\le W\le L$, take the literal cutoff

$$
 \rho L\le s<t\le\upsilon L,\qquad H<t-s\le H+W .
 \tag{1}
$$

One may additionally impose the true kept or rejected band of the balanced minor proof, separately, and any integer selector on $a$ (in particular either true total Möbius parity $\mu(a)=\mu(m)$). Define $A(m)$ to be the genuine $M_>(m)$ on this support and zero elsewhere. Then, uniformly in these hard windows,

$$
 \begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
   &\ll \frac{\Sigma(N)|I|}{L}\!
         \left(\frac{(W+1)L_2^3}{L}+L_2^{-5/2}\right)+N^{1-10^{-4}},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)
                          e(-N\theta)\,d\theta\right|
   &\ll \frac{\Sigma(N)|I|}{L}\!
         \left(\frac{(W+1)L_2^3}{L}+L_2^{-5/2}\right)+N^{1-10^{-4}} .
 \end{split} \tag{2}
$$

Here $\mathfrak m$ is the original complement of reduced arcs of denominators at most $Q=N^{1/1000}$ and slow width $2Q/N$. Thus $W=o(L/L_2^3)$ is allowed even for $H\asymp L$, wherever the true polynomial cofactor ranges overlap. No sum over such windows is implicit.

## 1. Geometry, local weight and rough exception

The true conditions imply $p,q>N^{1/3}$, $ap,aq\le N^{.65+o(1)}$, and $a\le N^{.3+o(1)}$ since $a=(ap)(aq)/m$. In particular both primes exceed $a$, and their coprimality to $a$ is automatic for this two-prime representation. The swapped sharp and low formulas of the [two-tag calculation](r75-spectral-balanced-rejected-majors.md), §2, apply verbatim: the short labels are at most $N^{.15+o(1)}$, and a cofactor divisor of size $N^{1/2+o(1)}$ in a low fold contains the appropriate large tag. For the real comparison use the same exact formal divisor lattice with the two labels. At fixed $k=aq$, known $q=P^+(k)$, $t$ is constant and $s=\log(x/(qD))$ is affine in $\log x$, for $x=pqa$. All gates in (1) and any optional band are hard intervals in $x$, and the integer selector is constant. The same is true in the second prime comparison at fixed $a,x$, with $\log q$ as variable. In particular no filter introduces uncontrolled variation.

Use $w(n)=n/\varphi(n)$. The original first two-root upper sieve has local factor $k/\varphi(k)\ll w(a)$ at $k=aq$. The exact completed local factor is $\Sigma(N)r(k)$ as before, and $r(k)\ll w(a)$ as well: on units the factor ratio at any odd prime $\ell$ is

$$
 \frac{(\ell-1)/(\ell-2)}{\ell/(\ell-1)}
       = 1+O(\ell^{-2}),
$$

and the local factor vanishes on nonunits. Both comparisons now use $w(a)$ inside the reciprocal $a$ trace, not a blanket $L_2$.

Set $U=L_2^6$, $G=e^U$, and let $b$ be the exact product of the primes in $a$ at most $G$. If $b=1$, the actual partner is $G$-rough, with largest $q>N^{.34}$ for large $N$. The [rough-kernel estimate](r69-spectral-rough-reciprocal-kernel-sampling.md) with $\delta=.16$ and $U_0=U$ gives relative $O(\sqrt{L_2/U})=O(L_2^{-5/2})$. For this exact subset use its positive reciprocal cofactor majorants and retain the extra cuts in the true full and major transfers: at fixed kept cofactor $ap$, $p$ is its actual largest prime, $a$ is fixed, and $t$ and $t-s$ are affine in $\log x$. Thus the extra hard intervals and fixed selector only reduce the positive majorant and preserve bounded variation. One obtains the minor by subtracting the genuinely restricted major, not by restricting an already estimated signed minor.

For $b>1$, use physical log cells of width $\eta=L^{-2}$ and let $x_0$ be the reference point, $s_0=\log(x_0/(qD))$, $h_0=\log(x_0/D^2)$. Then $s-h=s_0-h_0$ exactly, and $|s-s_0|,|h-h_0|\le\eta$. Widen only the positive envelope support by $\eta$ around the moving endpoints. At fixed $x_0,s_0$ the corresponding $a$ lies in a hard log interval of width at most $W+2\eta$ and above

$$
                  \exp(2s_0+H-h_0-\eta).
 \tag{3}
$$

The optional hard kept/rejected cut may shorten this interval. Both $s_0$ and $t$ remain between polynomial cofactor exponents bounded away from zero. We will prove that the positive reciprocal envelope at fixed $x_0,s_0$, now with weight $w(a)/a$, is $O((W+1)L_2^3/L)$ on this branch.

## 2. Weighted sharp cutoff energy

First remove extreme $j(a)=\omega(b)>J_*=\lceil C_*\log L\rceil$ from the positive envelope, with $C_*$ a sufficiently large fixed constant. The divisor bound for the envelope, including its variation, is at most $\tau_8(a)L^{O(1)}$; for the new low envelope this will be checked below. The factor $w(a)\ll L_2$ and the positive Rankin bound (3) of the wide even proof make this removed reciprocal weight smaller than any prescribed fixed inverse log, for a suitable $C_*$. This can be applied either at fixed $s_0$ or in the eventual prime transfer.

For the other terms write $a=bv$, with strictly $G$-rough $v$. Exactly $w(a)=w(b)w(v)$, and $w(v)=1+O((L/U)e^{-U})$ since $a$ is bounded by a fixed power of $N$. The latter factor can be replaced by 1 at negligible cost against the coarse positive divisor estimates. We use the weighted version of the fixed-cutoff proof in §§2–3 of the wide even theorem, both for a primitive and its indefinite integral. For $u$ between $s_0-h_0$ and $s_0$, including both endpoints and either strict/weak convention for the primitive, it gives

$$
 \sum_a\frac{w(a)}a|S_a(u)|^2\ll W+1,\qquad
 \sum_a\frac{w(a)}a|J_a(u)|^2\ll (W+1)U .
 \tag{4}
$$

Here $S_a(u)=\sum_{d\mid a,\log d\le u}\mu(d)$, and $J_a(u)=\int_{-\infty}^u S_a(v)\,dv$. Both sums keep the actual $b>1$ and the count cap. We give explicitly the effect of the change of weight and of using the unintegrated cutoff.

At fixed $b$ drop any extra subset or squarefree or parity restriction on the rough $v$ only from the nonnegative square, and then expand its signed pairs. On a dyad $v\asymp V_0$ the rough Bonferroni harmonic main for a pair-lcm $d$ is $w_0 V_G/d$, where $w_0$ is the actual dyad log width and $V_G=\prod_{\ell\le G}(1-1/\ell)$. Its errors are $O_A(w_0L^{-A}/d+\exp(O_A(U L_2^2))/V_0)$. The floor summed over labels is at most $e^{2s_0}\exp(O_A(U L_2^2))/V_0\ll \exp(-L^{1/3})$ for large $N$, by (3), $H\ge2L^{1/3}$, and $\log b=O(U\log L)$. Polynomial log signed coefficients and label reciprocals are harmless as in the earlier proof. In the remaining $b$ harmonic sum insert $w(b)/b$; it still has total $O(U)$, since $(w(\ell)-1)/\ell\ll\ell^{-2}$. The exact gcd expansion and the fixed-cutoff harmonic $e$ sampling then have the same error: for $b>1$ the shifted indefinite primitive uses a finite log interval; the shifted unintegrated primitive already decays at large positive argument. On the retained log window, the latter has polynomially bounded variation by the sum of the absolute reciprocal jumps, with strict/weak differences handled by the same endpoint trace. Thus both the $S^2$ and $J^2$ main terms are bounded by

$$
  O(W+1)V_G^2\sum_{\substack{b>1,\ b\ {\rm sf}\\P^+(b)\le G}}
          \frac{w(b)}{b}\|\mathcal D_b R_G\|_2^2,\qquad
  O(W+1)V_G^2\sum_{\substack{b>1,\ b\ {\rm sf}\\P^+(b)\le G}}
          \frac{w(b)}{b}\|J_b\|_2^2,
 \tag{5}
$$

respectively, with negligible errors. Here $\mathcal D_b$, $R_G$ and $J_b$ are exactly as in the wide even proof. Large finite positive sums have been completed only after the signed square has become a nonnegative energy.

The weighted Euler generator now has factor $1+w(\ell)|1-e^{-i\xi\log\ell}|^2/\ell$. Away from zero its log differs from the unweighted generator by $O(\sum_\ell(w(\ell)-1)/\ell)=O(1)$. At $U|\xi|\le1$, after subtracting its unit term, it is $O((U|\xi|)^2)$ by $w(\ell)\le2$ and the same moment $\sum_{\ell\le G}(\log\ell)^2/\ell\ll U^2$. The ordinary PNT frequency bounds of the [signed Euler proof](r70-spectral-signed-shift-euler-slots.md), §1, therefore give $O(U^2)$ for the unintegrated Fourier energy: up to frequency 1 the integrand is $O(U^2)$, and at higher frequencies the fixed powers of the logarithm over $\xi^2$ are integrable with the same factor $U^2$. For the integrated energy the extra $\xi^{-2}$ just as in the wide even proof gives $O(U^3)$, with the unit term absent. Division by $V_G^{-2}\asymp U^2$ proves (4).

The unsigned first endpoint movement in the sharp envelope at $s_0$ has an even smaller squared reciprocal mean with the weight $w(a)$. For a log shell of width $O(\eta)$ around $Z\asymp e^{s_0}$,

$$
 \sum_{d,e\text{ in shell}}[d,e]^{-1}
           \ll \eta+Z^{-1}+\eta^2\log(2Z).
 \tag{6}
$$

The diagonal is $O(\eta+Z^{-1})$. Off the diagonal the gcd is at most $|d-e|\ll\eta Z$; at fixed gcd $g$ the two scaled harmonic weights are each $O(\eta+g/Z)=O(\eta)$, then sum $1/g$. The exact ordinary reciprocal trace over the hard $a$ interval has summed floors $O(Z^2/a_{\min})$, negligible by (3); the crude pointwise $w(a)\ll L_2$ suffices on this one shell. With $\eta=L^{-2}$ this gives weighted reciprocal square $O(W+1)$. The other sharp endpoint does not move. Consequently the sharp positive envelope (5) of the balanced theorem keeps the weighted $C_0^2$ bound $O(W+1)$ and now has $C_1^2$ bound $O((W+1)U)$, allowing either parity. For odd total, the short difference is bounded also by the sum of the absolute two primitives $J$; this weaker bound still suffices. Cauchy gives a weighted reciprocal sharp bound $O((W+1)(L_2+\sqrt U)/L)$.

## 3. Keep the coprime-label signs in the low folds

We first state a small-cutoff consequence of the signed LCM energy (8) in the two-tag balanced major proof. On any hard interval at scale at least $N^c$ of log width $w_0$ (where $c>0$ is fixed), a primitive $S_n(u(n))$ with cutoff at most $L^C$, and the corresponding $J_n(u(n))$, have squared reciprocal bounds with weight $w(n)$ of

$$
 O(w_0+1),\qquad O((w_0+1)L_2),
 \tag{7}
$$

respectively, on squarefree $n$. The same former bound holds for the unsigned endpoint shell of width $O(\eta)$ there, allowing the unit, and for the weighted harmonic count without the primitive. The log cutoff is allowed to be affine in $\log n$ on a bounded number of pieces; strict/weak endpoints are allowed. Only these cases are used below.

For verification, expand the positive weight

$$
                 w(n)=\sum_{r\mid n}\frac{\mu^2(r)}{\varphi(r)} .
$$

On a clipped ordinary dyad $n\asymp K$ of log width $w_1$, first take $r\le\sqrt K$ and write $n=ry$. Squarefreeness supplies $(r,y)=1$, so split the signed divisor primitive into shifts over the divisors of $r$ (and similarly for the integral). Use Cauchy in these shifts, drop the remaining $y$ restrictions on the resulting positive squares, and apply the unweighted moving signed LCM trace of that proof. Its main is $O(w_1)$ for $S$, $O(w_1L_2)$ for $J$, and its floor is at most a power of $L$ times $\sqrt K^{-1}$, since labels are polylogarithmic and $y\gg\sqrt K$. For the unsigned shell the same argument uses the unsigned shell LCM bound of the [subpower proof](r66-spectral-subpower-largest-prime.md), with main $O(w_1)$ and same floors; it also applies to a shell containing 1. The total shift factor sums because

$$
            \sum_{r\ge1}\frac{\mu^2(r)\tau(r)^2}{r\varphi(r)}<\infty .
$$

For $r>\sqrt K$ use the crude polylogarithmic primitive bounds and the reciprocal count $w_1/r+O(1/K)$. The tail of $\sum_r\mu^2(r)/(r\varphi(r))$ is $O(K^{-1/4})$ by its half moment, and $\sum_{r\le2K}\mu^2(r)/\varphi(r)\ll\log(2K)$, directly from the finite Euler product. Thus the large-$r$ contribution and all floors are negligible, even summed over $O(L)$ dyads. The weighted harmonic bound follows from the same positive expansion without shifts. This proves (7).

For each low fold at real $x$, write $a=uv$, $z=\log(l/D)$ with the exact low gate $0<z\le\log(H_0/D)$. In the first fold $z=s-\log v$ and the two signed labels divide $u$; in the second $z=h-s+\log v$ and both divide $v$. Let $n$ denote the designated factor $u$ or $v$. Expand their true coprimality by the sum of $\mu(g)$ over common divisors. Since the actual $n$ is squarefree, the exact signed label expression before division by $\log x$ is

$$
 \sum_{\substack{g\mid n\\\log g<z}}\mu(g)
       \left\{h\,S_{n/g}((z-\log g)^-)^2
              -2 S_{n/g}((z-\log g)^-)J_{n/g}(z-\log g)\right\}.
 \tag{8}
$$

Indeed the two labels become $g d_1,g d_2$ with $d_i\mid n/g$, so their two Möbius factors contribute $\mu(g)^2=1$. The logarithmic factor becomes $h-2(z-\log g)+\log(d_1d_2)$, and summing this gives (8). This exact step is before taking absolute values. In particular we have not replaced the signed label sum by its unsigned count.

To form its positive cell envelope, enlarge the $z$ gates by $O(\eta)$ about $x_0$, and similarly allow $g\le (H_0/D)e^{O(\eta)}$ and $\log g\le z_0+O(\eta)$, where $z_0$ is the appropriate expression at $x_0$. At the first moving endpoint dominate $S$ by its reference absolute value plus the unsigned label shell of width $O(\eta)$, and $|J|$ by the reference $|J|$ plus $O(\eta)$ times that same extended absolute $S$ envelope. In the second fold $z$ does not move at all on the physical cell. Apply absolute values only to the outer sum over $g$ and the displayed product in (8). This gives a positive bounded-variation majorant in $\log q$ at fixed $a,x_0$: each original label threshold is a bounded set of interval gates, and each integrated weight is a finite sum of clipped affine functions. The number of resulting divisor and label combinations on squarefree $a$ is at most $6^{\omega(a)}$ up to an absolute factor, since $\sum_{g\mid n}4^{\omega(n/g)}=5^{\omega(n)}$ and one then sums $n$ over the factors of $a$. Hence the asserted $\tau_8(a)L^{O(1)}$ bound in supremum plus variation holds. These are the weights used for the genuine positive second-prime transfer.

We bound this envelope at fixed $x_0,s_0$ including the arithmetic weight $w(a)/a$. In the first fold $v$ is within a log interval of width $O(L_2)$ about $e^{s_0}$, and at fixed $v$ the other factor $u$ lies in the literal $a/v$ interval of width $O(W+1)$ in log. For fixed $g$ use $u=g u'$; on the true squarefree terms $w(a)=w(v)w(g)w(u')$. Divide the reciprocal weight by $g$ and apply (7) in $u'$ to the fixed log cutoff $z_0-\log g$ and its envelope. By Cauchy the $S J$ sum costs $O((W+1)\sqrt{L_2})$, and the $h S^2$ sum costs $O((W+1)L_2)$. The integrated uncertainty from the moving endpoint is smaller. In the second fold write instead $v=g v'$. The shifted cutoff is now exactly

$$
                       z_0-\log g=h_0-s_0+\log v',
$$

a moving cutoff of the allowed type in (7) as $v'$ varies over a log interval of width $O(L_2)$. The other-factor harmonic sum is uniformly $O(W+1)$ for each $v'$, again by (7). The centered-square and product bounds in $v'$ now cost $O(L_2^2)$, using the same $h=O(L_2)$ and Cauchy. In both folds the variables other than $g$ are polynomially large: $\log v=s_0+O(L_2)$ and $\log(a/v)=t+O(L_2)$ on these widened supports, with $\rho>0$. Thus all uses of (7) and its moving endpoints apply. In the first fold the weighted reciprocal $v$ sum is $O(L_2)$; in both folds the outer $g$ sum with $w(g)/g$ is $O(L_2)$ by the same harmonic estimate (the positive Euler expansion gives this upper bound down to 1). Dividing by $\log x\asymp L$ therefore gives

$$
                 O\!\left(\frac{(W+1)L_2^3}{L}\right)
 \tag{9}
$$

for the whole positive low envelope. All enlargements were of nonnegative terms after (8); no subset of a signed low-fold estimate has been inferred.

## 4. Actual full and original minor

Combine (9) with the sharp estimate after (6), using $\sqrt U=L_2^3$. This gives the stated fixed-$s_0$ positive reciprocal envelope with the precise weight $w(a)/a$. For each physical cell keep the real interval of the two inner primes $p,N-aqp$, at fixed actual prime $q$ and $k=aq$, and use the same unconditional two-root upper sieve as the balanced minor theorem. The gated parameters are still hard intervals at fixed $k$, the primes exceed the sieving height, and $k\le N^{.65+o(1)}$ gives the same sieve floor. Its local loss is bounded by $O(w(a))$ and has already been inserted. Sum the genuine outer prime $q$ by ordinary unconditional PNT against its positive $O(\tau_8(a)L^{O(1)})$-variation envelope, with $w(a)/a$ fixed. This is precisely §3 of the balanced minor argument, with the new weighted envelope in place of the old one. The exponents give $q>N^{1/3}$, $dq/q=-ds_0$, and $\log q\gg L$ as before. The relative errors from PNT are negligible against the polynomial size of $q$ and the positive divisor harmonic sum, and the left subinterval lengths add to $|I|$. No actual prime condition on $p$ or $N-aqp$ has been replaced by PNT. This proves the unconditional full bound with the separate rough case of §1.

For the genuine major use again the exact two-prime completion of the balanced theorem, §4. All actual gates in (1), including the offset and the optional original band, preserve the fixed-$k$ real bounded variation $O(\tau_4(k))$ of the signed coefficient. The size $k\le N^{.65+o(1)}$, $p,q>N^{1/3}$ and the fixed original $Q$ preserve its integrated power error under the same historical prime progression hypothesis. The completed real density has both reciprocal prime logarithms, each $\asymp L$, and local factor $r(k)\ll w(a)$. It is bounded by the same positive reciprocal envelope with $x_0=x$, integrating $s$ over length $O(L)$. Subtract this actual major from the literal full coefficient by Fourier inversion. After including the independently treated rough subset this proves the minor line of (2). The argument neither covers a window of macroscopic logarithmic width nor turns this upper bound into cancellation between such windows.
