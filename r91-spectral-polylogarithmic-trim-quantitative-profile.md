# A polynomial-logarithmic conductor trim with a quantitative Dickman profile

**Scope.** At any fixed requested logarithmic accuracy, a selected divisor of the prescribed planting suffices on every sufficiently large dyad. The divisor differs by at most a fixed power of the ambient logarithm, and the true two mixed-strip parity sums have a quantitative Dickman profile error. No external real-zero-gap input or Dirichlet GRH is used. The estimates are for relative density one of the selected multiples, not for the complete original planting, an exact radical, a specified target, prime representations, or Hypothesis S.

Keep the [actual trim theorem](r90-spectral-all-scale-translates-conductor-trim.md) notation: $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $Y\le N\le2Y$, $L=\log N$, $G^\epsilon\le z\le Z$ with fixed $0<\epsilon<1/2$, $\ell=\log z$, $\theta_z=\ell/\log G$. The prescribed even squarefree integer $K_z=K_z(\mathcal P)$ is $2$ times the product of odd primes up to $z$ in a nonempty fixed union $\mathcal P$ of reduced classes, of density $d\in(0,1]$. Use the exact true coefficients $M_{\pm,N}$, real hard left interval $I\subset(N/2,9N/16]$, bounded-BV weight $\omega$, prime weights $\lambda(n)$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, and original polynomial arcs from that theorem. In particular $S_\pm$ is the genuine full signed correlation and $S_\pm^{\rm maj}$ its integral on the actual moving major of cap $N^{1/1000}$ and slow radius $2N^{1/1000}/N$. The sign $+$ denotes even squarefree factor count, not the parity of the integer. Positivity of the cutoffs $B>B_0>0$ is fixed, not taken to zero during the limit.

**Theorem.** There is a fixed $C_0$ such that for each fixed $A>0$ and every sufficiently large dyad one may select a single set of removed planting primes, the same at every threshold $z$. If $K'_z\mid K_z$ is the resulting even divisor, then

$$
             K_z/K'_z\le G^{C_0+3A+1/2}.
 \tag{1}
$$

For every prescribed $z$, off $O_A((Y/K'_z)G^{-A})$ members of $\{N\in[Y,2Y]:K'_z\mid N\}$, simultaneously for both signs and all ordinary $I,\omega$, one has

$$
 \begin{split}
 S_\pm(N;I,\omega),\ S_\pm^{\rm maj}(N;I,\omega)
   ={}&\Sigma(N)\mathcal K_{\pm,d}
       \left(\frac{2B}{\theta_z},\frac{B-B_0}{\theta_z}\right)
                \int_I\frac{\omega(u)}{\log(N-u)}\,du\\
      &+O_A\!\left(\frac{\Sigma(N)|I|}{L}\,
                             \ell^{-d/(2d+1)}+YG^{-A}\right).
 \end{split}                                                       \tag{2}
$$

Here $\Sigma(N)$ is the genuine singular factor and the profile is the same [Dickman bracket](r83-spectral-ap-radical-major-law.md) with the prescribed density $d$, including $d\le1/2$. The relative exception, constants, and error are uniform across allowed $z$ for the fixed parameters; the exceptional sets are per selected $K'_z$. The original moving minor is still $O(Y^{1-1/40000})$ on the retained targets. The mask can depend on $A$; (1) is not simultaneous for every accuracy with one fixed polynomial exponent.

## 1. Spend only the remaining conductor budget

If no Page zero of the [all-scale reduction](r87-spectral-all-scale-exceptional-left-reduction.md) exists, set $K'_z=K_z$. Otherwise write $r$ for its primitive conductor, $\beta$ for its zero, $H=\log r$, and $g=(r,K_Z)$. Let $C_0$ be the exponent constant in the sufficient criterion of the [divisibility-sampled folded bound, (8)--(9)](r89-spectral-exceptional-conductor-folded-sampling.md#3-consequences-for-the-genuine-full-and-original-major-sums), enlarged if needed, and set

$$
 W_A=\bigl((C_0+3A)\log G-2(1-\beta)G-\log(r/g)\bigr)_+.
 \tag{3}
$$

If $W_A=0$ no deletion is needed. If $W_A>0$, the classical lower bound in the all-scale reduction gives $H/\log G\to\infty$ uniformly when this zero exists. Moreover $\log(r/g)\le(C_0+3A)\log G=o(H)$, so the squarefree $g$ has logarithm $H-o(H)$. By $\sum_{p\le x}\log p\ll x$, a sufficiently small fixed $\lambda>0$ makes the total logarithm of common primes $p\mid g$ with $p>\lambda H$ at least $H/2$ for all sufficiently large scales. In particular they are odd and supply more than $W_A$. Choose such primes in increasing order until their total log first reaches $W_A$. The final increment is at most $\log Z$, since all the common primes dividing $K_Z$ are at most $Z$. Denote this set by $\mathcal R$. Define $K'_z=K_z/\prod_{p\in\mathcal R,\,p\le z}p$. The chosen set is independent of $z$.

The gcd at $Z$ loses exactly the removed primes, since $K_Z$ is squarefree and the chosen primes divide $g$. Thus the new conductor quotient has gained at least $W_A$ in logarithm. At any smaller $z$ it only increases as $K'_z\mid K'_Z$, so (3) gives the folded sufficient criterion uniformly in $z$. By the same construction, including the case of an empty set,

$$
 \log(K_z/K'_z)\le W_A+\log Z,\qquad
 \sum_{p\in\mathcal R}\frac{\log p}{p}
      \ll_A\frac{\log G}{H}=o(1)
 \tag{4}
$$

when the zero exists, and the left sides are zero when it does not. The second inequality uses $p>\lambda H$ and the total log budget. In particular the number of removed primes is $O_A(\log G/\log\log G)$, though that count is not needed. With $\log Z\le(\log G)/2$, (4) implies (1). As in R90 the selection is ineffective only in the classical Siegel sense and need not be made on any zero-free-region hypothesis beyond that used in R87.

Since $K'_z\le K_Z\le e^{2Z}$, the folded theorem estimates both actual sums by the exact completed parity bracket $\mathcal B_\pm(N;I,\omega)$ with absolute error $O_A(YG^{-A})$, off the stated relative exception. It also gives the original minor conclusion. On the same selected family, discard also the exceptional set of [the actual extra-mask moment](r90-spectral-all-scale-translates-conductor-trim.md); it is smaller than every fixed inverse power of $G$, and then

$$
                X_N=\sum_{\substack{p\mid N\\p\nmid K'_z}}
                        \frac{\log p}{p}\ll\log(2\ell).
 \tag{5}
$$

No density limit has been used in this arithmetic step. The rest of the proof supplies the quantitative replacement of the exact finite bracket.

## 2. Quantitative convergence on the complete initial AP mask

Use the normalized profiles $f_{K,j}(v)=\ell R_{K,j}(\ell v)/M_{K,j}$ of R90 and [Section 1 of the AP profile proof](r83-spectral-ap-radical-major-law.md). The signed primitive masks the prime divisors of the even integer $K$ and of a squarefree $j$; $M_{K,j}=\int R_{K,j}>0$. The scale is always the original $\ell=\log z$. The universal bounds are $\|f_{K,j}\|_1\ll1$, $\|f_{K,j}\|_2\ll\sqrt\ell$, and $|v f_{K,j}(v)|\ll1$ for $v>0$. These apply even to the exact mask of $N$, not just the prescribed mask. Write $f=f_d$ for the probability density defined by the unconditional profile calculation in the AP proof and put $s_d=d/(2d+1)$. We prove for the complete original mask, uniformly for squarefree $j\le\ell^2$,

$$
 \|v(f_{K_z,j}-f)\|_2\ll\frac{1+\log j}{\sqrt\ell},\qquad
 \|f_{K_z,j}-f\|_1\ll (1+\log j)\ell^{-s_d}.
 \tag{6}
$$

These are estimates for the analytic Euler profiles, independent of the historical prime/Möbius-GRH inputs used for a prescribed exact-radical major in the AP proof.

Here are the Fourier details, with $\widehat f(\xi)=\int f(v)e^{-i\xi v}dv$. The complete-mask normalized profile is $\pi_{z,j}*a_\ell$, where $\pi_{z,j}$ is its normalized positive Euler measure and $a_\ell(v)=\ell R(\ell v)$ for the ordinary reciprocal Möbius primitive. Write $\Phi_{z,j}=\log\widehat\pi_{z,j}$ using its convergent Euler logarithm (8) in the AP proof, and $\Phi_d=d\int_0^1(e^{-i\xi v}-1)dv/v$. Both are zero at $\xi=0$, with nonpositive real parts. For $t=\xi/\ell$ the derivative of the Euler sum gives

$$
  \Phi'_{z,j}(\xi)
     =-\frac{i}{\ell}\sum_{\substack{p\le z\\p\in\mathcal P}}
                        \frac{\log p}{p}e^{-it\log p}
           +O\!\left((1+\log j)/\ell\right).
 \tag{7}
$$

The bound is uniform in the real phase: the terms of prime-power index at least two cost an absolutely summable $\sum_{p,k\ge2}(\log p)/p^k$ before division by $\ell$; the first-index replacement cost outside $K_z$ is $O(\sum_p(\log p)/p^2+\sum_{p\mid j}(\log p)/p)$, and the exceptional fixed prime $2$ costs $O(1)$. In particular this spells out the dependence on $j$ in (12) of the AP proof.

For $|\xi|\le\ell$, the fixed-AP prime number theorem used there for the weighted sum in (7) gives the integral $d\int_0^\ell e^{-itu}du$ with error $O_{q_*}(1)$. Explicitly use $\vartheta_{\mathcal P}(e^u)=de^u+O_{q_*}(e^u e^{-c\sqrt u})$, integrate by parts with the test $e^{-(1+it)u}$, and absorb the lower endpoint below $\log 2$. The error is bounded by $(1+|t|)$ times an integrable stretched exponential, plus end terms. The same argument, replacing $it$ by a real number between $0$ and $1$, applies to the analogous Laplace derivative for $0\le s\le\ell$. Thus in the low Fourier range

$$
 |\Phi'_{z,j}(\xi)-\Phi'_d(\xi)|\ll (1+\log j)/\ell,\qquad
 |\Phi_{z,j}(\xi)-\Phi_d(\xi)|\ll(1+\log j)|\xi|/\ell .
 \tag{8}
$$

For the second integrate from zero. Because the real parts are nonpositive, $|e^a-e^b|\le |a-b|$ on the connecting line segment for these exponents. Also $|\Phi'_d(\xi)|\ll(1+|\xi|)^{-1}$. Using $\widehat f_{K_z,j}=\widehat R(\xi/\ell)e^{\Phi_{z,j}}$, the finite first absolute moment of $R$ and $\int R=1$, we have $|\widehat R(\xi/\ell)-1|\ll|\xi|/\ell$ and $\ell^{-1}|\widehat R'(\xi/\ell)|\ll\ell^{-1}$. The product derivative and (8) now give

$$
  |\partial_\xi(\widehat f_{K_z,j}-\widehat f)(\xi)|
                            \ll (1+\log j)/\ell
                            \qquad(|\xi|\le\ell).
 \tag{9}
$$

For $|t|=|\xi|/\ell\ge1$, start the tail of the prime sum at raw log $a=C(1+\log(3+|t|))^2$ as in the AP proof. The shorter part costs $O(1+a)$ by Chebyshev; if $a<\ell$, the remaining oscillatory integral and its error are $O(1)$. Thus (7) is $O((1+\log j)(1+\log(3+|t|))^2/\ell)$. The ordinary bounds from that same proof, $|\widehat R(t)|+|\widehat R'(t)|\ll (1+\log(3+|t|))^4/|t|$, give

$$
 |\partial_\xi\widehat f_{K_z,j}(\xi)|
    \ll \frac{(1+\log j)(1+\log(3+|\xi|/\ell))^6}{|\xi|}
       \qquad(|\xi|\ge\ell).
 \tag{10}
$$

Since $|\widehat f'(\xi)|\ll(1+|\xi|)^{-1}$, the two derivative pieces (9)--(10) have squared integrals $\ll (1+\log j)^2/\ell$, using the substitution $\xi/\ell$ in the tail rather than a bound with $\log|\xi|$ there. Plancherel gives the first part of (6). The finite-profile weighted norms needed here follow from (5) of the AP proof and the finite first moments; the limit weighted norm also follows from the positive delay identity $v f(v)=d\int_{v-1}^v f(w)\,dw$, using zero extension on the negative half-line.

For the global $L^1$ estimate let $\delta=\ell^{-1/(2d+1)}$. The analogous Laplace derivative estimate from above, integrated up to $s=\delta^{-1}\le\ell$, gives an exponent difference $O((1+\log j)\delta^{-1}/\ell)=o(1)$ for $j\le\ell^2$ since $d>0$ is fixed. The limiting Laplace transform at $s=\delta^{-1}$ is $\ll_d\delta^d$, by splitting its defining integral at $\delta$. Therefore $\pi_{z,j}([0,\delta])\le e\int e^{-v/\delta}\pi_{z,j}(dv)\ll_d\delta^d$. Since $a_\ell$ is supported on the nonnegative half-line with bounded absolute norm, $\int_0^\delta|f_{K_z,j}|\ll\pi_{z,j}([0,\delta])$; the limiting density has the same upper bound there by its Laplace transform. On $[\delta,\infty)$ use Cauchy--Schwarz with $v^{-1}$, with norm $\delta^{-1/2}$, and the first part of (6). These two errors are $O((1+\log j)\ell^{-s_d})$, proving (6).

## 3. Quantitative propagation through both literal mask changes

The Dickman delay identity above gives a continuous locally absolutely continuous representative for $f$ on $(0,\infty)$. Differentiating away from zero gives $v f'(v)=(d-1)f(v)-d f(v-1)$ almost everywhere. As $0<d\le1$ and $f\ge0$, it is nonincreasing on $(0,\infty)$. Consequently for each $t\ge0$, writing $T_t$ for right translation,

$$
 \|T_t f-f\|_1=2\int_0^t f(v)\,dv\ll_d\min(1,t^d),\qquad
 \|T_t(vf)-vf\|_2\ll_d \min(1,\sqrt t).
 \tag{11}
$$

The cusp bound for the first estimate was just obtained by Laplace or follows from $f(v)=b_d v^{d-1}$ for $0<v<1$ in the AP proof. For the second use $vf=d\mathbf1_{(0,1)}*f$, then the $L^2$ norm of the translated difference of this interval indicator and $\|f\|_1=1$. This does not assume global square integrability of $f$.

For each actual $j$, first remove from $K_z$ the prescribed primes not already masked by $j$, then add the actual extra primes from (5) not already masked by $j$. These operations are the exact normalized convolutions of [Section 3 of R90](r90-spectral-all-scale-translates-conductor-trim.md#3-transfer-the-genuine-euler-primitives-through-the-omitted-primes): the removed-prime factor is the signed mass-one measure $(\delta_0-\alpha_p^\circ\delta_{\log p/\ell})/(1-\alpha_p^\circ)$, and the added-prime factor is the positive geometric probability $(1-\alpha_p^\circ)\sum_{k\ge0}(\alpha_p^\circ)^k\delta_{k\log p/\ell}$, where $\alpha_p^\circ=(p-1)/(p^2-2)$ on odd primes. This remains exact even if an actually added prime was earlier removed, because the factors are inverse; there is no distinctness assumption between the two lists. The mask at the prime $2$ is unchanged.

Their combined finite signed mass-one measure, say $\mu_{N,j}$, is supported on $[0,\infty)$. By (4) the total variation of the removal kernel is bounded and its first **absolute** moment is $O_A(\ell^{-1})$, by multiplying the variation masses and summing their normalized first moments as in R90 (12). This is valid even with the ineffective asymptotic conductor lower bound, because only a bounded numerator is needed. The addition kernel is a probability of mean $O(X_N/\ell)$. By total variation domination in convolution, $\|\mu_{N,j}\|_{\rm TV}\ll_A1$ and over the retained targets

$$
       m_1=\int t\,d|\mu_{N,j}|(t)\ll_A \log(2\ell)/\ell .
 \tag{12}
$$

The exact profile of $N$ is $\mu_{N,j}*f_{K_z,j}$. Since the measure has mass one, the difference against the limit $f$ is controlled by convolving the error in (6) and by the translated difference in (11) integrated against $|\mu_{N,j}|$. For the weighted estimate also use $v(\mu*h)=\mu*(vh)+(t\mu)*h$. The two errors are thus bounded by

$$
 \begin{split}
 \|f_{N,j}-f\|_1
  &\ll_A \|f_{K_z,j}-f\|_1+m_1^d
     \ll_A (1+\log j)\ell^{-s_d},\\
 \|v(f_{N,j}-f)\|_2
  &\ll_A \|v(f_{K_z,j}-f)\|_2+\sqrt{m_1}
                          +m_1\|f_{K_z,j}\|_2
     \ll_A \frac{1+\log j+\log(2\ell)}{\sqrt\ell}
                     \qquad(j\le\ell^2).
 \end{split}                                                       \tag{13}
$$

Here use Jensen or Hölder with total variation mass for the $t^d$ and $t^{1/2}$ moments, including $d=1$. This treats the near-zero cusp without an unquantified error of the form $\log G/H$ in the profile norm: inverse factors have mass one and small *position* moment, so (11) supplies an actual rate in $\ell$. The arithmetic choice of the mask and its sufficiently-large threshold may still be ineffective.

## 4. Transfer the rates through the genuine cuts and signed Euler sum

Use the exact bracket (15) of R90 for $x=N-u$, with $\tau_x=T(x)/\ell$, $\upsilon_j=(U-\log j)_+/\ell$, $T(x)=\log(x/D^2)$, $U=(B-B_0)\log L$. Expressed on the normalized profile $F=f_{N,j}$, the four terms in braces there are the terminal square $\tau_x\int_{\upsilon_j}^\infty F^2$, the square cumulative, the integrated autocorrelation, and $-\tau_x C_F(\tau_x)$ in the twisted part. The signed Euler factors $c_{N,j}$ have $\sum_jc_{N,j}=1$ and $\sum_j j^{1/2}|c_{N,j}|\ll1$ by the exact AP-profile identity, independently of the masks. For $j\le\ell^2$, both cutoffs are in fixed positive compact intervals, and their differences from $2B/\theta_z$, $(B-B_0)/\theta_z$ are respectively $O(\ell^{-1})$ and $O((1+\log j)/\ell)$ uniformly in $x$.

On a terminal half-line separated from zero, the weighted $L^2$ error in (13) controls the quadratic difference by Cauchy--Schwarz. The cumulative square and the integrated autocorrelation use the $L^1$ error in (13) and Young's inequality. For the point-shift term let $t$ vary in the positive compact shift interval. In
$C_F(t)-C_f(t)=\int(F-f)(v)F(v+t)dv+\int f(v)(F-f)(v+t)dv$,
the first term is bounded by the $L^1$ error and the universal $|vF(v)|$ bound. For the second split at $a=\ell^{-1}$: on $[0,a]$ both shifted factors are bounded and $\int_0^a f\ll a^d$. On $[a,\infty)$ use Cauchy--Schwarz and the shifted half-line weighted $L^2$ error. The cusp formula and the bounded tail give $\|f\mathbf1_{[a,\infty)}\|_2\ll_d a^{d-1/2}$ for $d<1/2$, $\ll (1+|\log a|)^{1/2}$ for $d=1/2$, and $\ll_d1$ for $d>1/2$. Thus the second term is $O_A(\ell^{-s_d})$ uniformly for $j\le\ell^2$, as $s_d<\min(d,1/2)$ and the extra logarithmic factors in (13) are harmless. No limit is asserted at zero shift.

The limiting profile's positive endpoint moves harmlessly: on any fixed positive half-line the delay formula and monotonicity bound $|f(y+h)-f(y)|\ll |h|^d$ for small $h$, by the masses of the two changed intervals of length $|h|$, each at most $\int_0^{|h|}f$, and the change in $1/y$. So $C_f(t+h)-C_f(t)\ll |h|^d$ for positive shifts bounded away from zero. The terminal square and cumulative endpoints move at bounded density, and the moving edges of the integrated autocorrelation use its boundedness at positive distance from zero. All these errors are $O_A(\ell^{-s_d})$ for $j\le\ell^2$. Consequently the per-$j$ difference of normalized brackets is $O_A((1+\log j)\ell^{-s_d})$.

For $\ell^2<j\le e^{U/2}$ the cutoffs still stay positive, and the actual brackets are uniformly bounded through the $L^1$ and $|v f_{N,j}|$ bounds. This range has total signed absolute weight $O(\ell^{-1})$. For $j>e^{U/2}$ the universal squared $L^2$ bound $O(\ell)$ gives total contribution $O((1+\ell)e^{-U/4})$, which is smaller than $\ell^{-s_d}$. Applying the uniform half moment also to $(1+\log j)$ in the first range, and the exact signed sum-one identity to the limiting bracket, gives total profile error $O_A(\ell^{-s_d})$ uniformly in $x$. Integration against the original test yields the first error in (2). Together with the genuine folded arithmetic and (5), this proves (2).

**What the index bound does not do.** If $P=K_z/K'_z$ in this construction, all its primes lie in the true conductor and $\gcd(r,K'_z)=\gcd(r,K_z)/P$. Reusing the folded exception bound on the smaller subgroup by plain intersection pays exactly the gain: $(Y/K'_z)\gcd(r,K'_z)/r=(Y/K_z)\gcd(r,K_z)/r$. Neither the shorter trim nor the quantitative profile grants the theorem on the complete originally prescribed family.
