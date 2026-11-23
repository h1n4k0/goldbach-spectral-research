# Pointwise signed control with two rough primes on each leg

Fix $0<\rho<1/2$, $0<\kappa<1/4$, and fixed $\alpha_1,\alpha_2>0$ with $2\alpha_1+2\alpha_2<1$. For even $N$ put $L=\log N$, $T=L/\log L$, $D=\lfloor\sqrt N e^{-20T}\rfloor$, $Q=\lfloor N e^{-20T}\rfloor$, and $I_0=[\rho N,(1-\rho)N]$. The selected central integers are squarefree units $n=su$, $m=tv$, where $u,v$ each have **exactly two rough primes**, all $\ge N^\kappa$, and the nonempty lower products $s,t$ have all prime factors $\le y_i=\exp(L^{\alpha_i})$ in their respective slots. Lower arity is unrestricted and the two ranges are disjoint eventually. Allow additional integer masks independent of the interior divisor labels.

For hard $I\subseteq I_0$ use the genuine negative central alias

$$
 R_N(I)=-
 \sum_{\substack{n+m=N,\ n\in I,\ m\in I_0\\(nm,N)=1,\ n,m\ {\rm selected}}}
 \ \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
      \mu(d)\mu(e)\log(n/d)\log(m/e).
 \tag{1}
$$

**Theorem (unconditional, pointwise).** For every sufficiently large even $N$, put $\sigma=1-2\alpha_1-2\alpha_2>0$. Uniformly over the intervals and integer masks above,

$$
 |R_N(I)|\ll_{\rho,\kappa,\alpha_1,\alpha_2}
       \mathfrak S(N)\bigl(N+|I|(\log L)^2\bigr)L^{-\sigma},
 \tag{2}
$$

where $\mathfrak S(N)$ is the usual even binary singular series. In particular one may take equal $\alpha_1=\alpha_2<1/4$. There is no exceptional set. This does not concern a pointwise main term, three or more rough primes on a leg, a missing lower product, a higher sparse-band lower alphabet, nonsquarefree legs, or Hypothesis S.

## 1. The tails and the genuine affine-prime envelope

We may keep $s,t\le e^T$ with error $O_A(NL^{-A})$ for any fixed $A>0$. Indeed the absolute individual divisor-mark sums are bounded by $O(L\tau(s))$ and $O(L\tau(t))$, since there are only four rough labels on each side. For the tail $s>e^T$, Cauchy on the fixed target, where $n$ determines $m$, bounds the loss by

$$
 O\left(L^2N
 \left(\sum_{\substack{s>e^T,\ s\ {\rm squarefree}\\ P^+(s)\le y_1}}
                       \frac{\tau(s)^2}s\right)^{1/2}
 \left(\sum_{\substack{t\ {\rm squarefree}\\ P^+(t)\le y_2}}
                       \frac{\tau(t)^2}t\right)^{1/2}\right).
 \tag{3}
$$

For each lower product use all its multiples up to $N$ as a positive enlargement. The second sum is at most $\prod_{p\le y_2}(1+4/p)\ll L^{4\alpha_2}$. Rankin on the first, with exponent $1/\log y_1$, gains $\exp(-T/\log y_1)=\exp(-L^{1-\alpha_1}/\log L)$ at the cost of an Euler product bounded by $\prod_{p\le y_1}(1+4e/p)\ll L^{O(1)}$. This absorbs every log power. Exchange the sides for the other tail.

For fixed frozen cofactors $h,k$ with $(hk,N)=1$, $(h,k)=1$, the genuine primes $p,q\ge N^\kappa$ on $hp+kq=N$, $hp\in I$, have the upper bound

$$
 \ll_\kappa
 \frac{|I|\mathfrak S(N)}{hk T^2}\lambda^*(h)\lambda^*(k)+e^{6T},
 \qquad
 \lambda^*(h)=\prod_{\substack{\ell\mid h\\\ell>2}}
                                  \frac{\ell-1}{\ell-2}.
 \tag{4}
$$

The proof is the [affine-prime sieve](r63-source-pointwise-one-rough.md) with the following parameters, equally valid for these two cofactors. Parametrize $p=p_0+k j$, $q=q_0-h j$; the determinant of the linear forms is $N$ up to sign. The $j$ interval has length $|I|/(hk)$. At a prime $\ell\mid hk$ exactly one form is a nonzero constant and the other has a unit slope, by both frozen coprimalities. Otherwise the slopes are units and the two roots coincide exactly if $\ell\mid N$. In particular $\nu(2)=1$ because $hk$ is odd and $N$ even, where $\nu$ counts roots of the product. These coprimalities hold in every actual frozen pair, since any prime shared by the cofactors would divide $N$.

For clarity take $Z=e^T$ and $z=Z^\eta$ with absolute sufficiently small fixed $\eta>0$; both genuine primes exceed $z$ eventually. In the quadratic upper sieve put $g(\ell)=\nu(\ell)/\ell$, $a(\ell)=g(\ell)/(1-g(\ell))$, multiplicatively on squarefree products, and $G=\sum_{d\le Z}a(d)$ on the divisor-closed support with primes $\le z$. The diagonalization $Y_l=\sum_{l\mid d}\lambda_dg(d)$ gives main quadratic form $\sum_lY_l^2/a(l)$; take $Y_l=\mu(l)a(l)/G$. Inversion gives $\lambda_1=1$, main form $1/G$, and $|\lambda_d|\le a(d)/g(d)\le d$. Each least-common-multiple residue count on the hard interval has absolute floor error $O(1)$, so the total lattice error is $O(Z^6)$ from at most $Z^2$ pairs of weights, each weight $\le Z$, and at most $Z^2$ roots at their least common multiple. In the full Euler product of $a(d)$ the mean of $\log d$ is $\sum_{\ell\le z}g(\ell)\log\ell=O(\log z)$; Markov with $\eta$ small leaves at least half the mass at $d\le Z$. Therefore $G^{-1}\ll\prod_{\ell\le z}(1-\nu(\ell)/\ell)\ll\mathfrak S(N)\lambda^*(h)\lambda^*(k)/T^2$ by Mertens and the stated local roots. The extra odd factors are exactly the ratios $(\ell-1)/(\ell-2)$ at primes dividing $hk$ (which are units modulo $N$); truncating the usual baseline prime product only costs an absolute constant. This proves (4), including arbitrarily short hard intervals. We use it only for freezes with $hk\le N e^{-18T}$, so that the summed lattice error is very small.

## 2. Exact double switch and the freezing geometry

For a retained pair put $a=P^-(s)$, $b=P^-(t)$, $A_1=\log a$, $A_2=\log b$. Fix rough labels $f\mid u$, $g\mid v$ and lower labels $c\mid s/a$, $d'\mid t/b$. Put $x=cf$, $y=d'g$, $L_x=\log(n/x)$, $L_y=\log(m/y)$ and

$$
 J_{\epsilon\eta}
   =\mathbf1_{a^\epsilon x>D}\mathbf1_{b^\eta y>D}
      \mathbf1_{a^\epsilon b^\eta xy>Q},\qquad \epsilon,\eta\in\{0,1\}.
$$

Factoring the actual sign $\mu(x)\mu(y)$, the four marked terms in (1) are exactly

$$
 L_xL_y(J_{00}-J_{10}-J_{01}+J_{11})
 + A_1 L_y(J_{10}-J_{11})
 + L_x A_2(J_{01}-J_{11})
 + A_1 A_2 J_{11}.
 \tag{5}
$$

The opposite-side masks are not frozen or replaced prior to this identity.

For an integer $z>D$, let $\mathcal T_z=\max(D,Q/z)$. Then $D\le\mathcal T_z\le\sqrt N$, since $z\ge D+1>\sqrt N e^{-20T}$ and $Q\le N e^{-20T}$. A first-side switch at fixed right value $z=b^\eta y>D$ is exactly

$$
                 x\le\mathcal T_z<a x,
 \tag{6}
$$

with the analogous right switch for fixed left value $a^\epsilon x>D$. The empty rough label on a side cannot switch, since its largest divisor is at most $e^T<D$. The full label cannot switch either: each $u,v\ge\rho N e^{-T}>\sqrt N$ so either all its terms pass when the opposite divisor passes D, or all fail. Thus every switching side has an individual rough prime as its label.

**Second difference.** A nonzero second difference in (5) requires one first-side switch for some $\eta$ and one right-side switch for some $\epsilon$; a zero difference in either direction at both values of the other bit would make it vanish. If either switch starts above its own D boundary, both base divisors at that switch passed their D tests, and their product was $\le Q$. In particular $fg\le Q$. Otherwise $x\le D$ and $y\le D$, so $f,g\le D$. Both labels are single rough primes by the preceding paragraph. Freeze $h=sf$, $k=tg$, leaving one genuine prime each. In the respective cases $hk\le stQ$ or $stD^2$, and therefore

$$
                        hk\le N e^{-18T}.
 \tag{7}
$$

Retain one of the two possible first-side switches. For fixed $s,t,c,d',g$ and $\eta$, (6) restricts $\log f$ to one interval of length $\log a$. Neither remaining prime enters its location.

**Right switch with a left light factor.** In $A_1 L_y(J_{10}-J_{11})$, the right switches at fixed $z=a x>D$. If $y>D$, the product boundary was active before the switch, so $fg\le Q$. The left f is neither empty (since $z>D$) nor full (then $z>\sqrt N$ and $zy>Q$ automatically when $y>D$). Thus freeze $h=sf,k=tg$ with (7) and use the right version of (6), for fixed $f$, as an interval of log width $\log b$ on $g$. If $y\le D$, the right switch forces $D/b<y\le D$, even when $Q/z$ contributes to the actual threshold. Freeze $g$ and on the left freeze the smaller rough prime $f_0\le\sqrt N$ of $u$; $h=sf_0,k=tg$ then satisfy $hk\le st\sqrt N D\le N e^{-18T}$. The D strip on $\log g$ still has width $\log b$ (subtract $\log d'$). For this upper bound the original left rough label may be enlarged away; it has only four choices and the left light weight depends only on $s$. The term $L_x A_2(J_{01}-J_{11})$ has the exchanged argument. These switches include equality at the base edge and exclude equality at the shifted edge; the original threshold was strict.

## 3. Summation of the switched terms

A log interval of width $W$ in the polynomial prime range has reciprocal mass $O_\kappa((1+W)/L)$ by Chebyshev over unit-log intervals. The unrestricted reciprocal mass of $[N^\kappa,N]$ is $O_\kappa(1)$. Hence for each $s,t,c,d'$ the frozen rough reciprocal pairs cost $O_\kappa((1+\log a)/L)$ in the second difference and $O_\kappa((1+\log b)/L)$ in the right mixed term, by first fixing the prime not constrained by its strip. The exchanged mixed term uses $\log a$. The two rough factors of $\lambda^*(h)\lambda^*(k)$ are bounded constants, but keep the complete lower factor $\lambda^*(s)\lambda^*(t)$, since the lower arity is unrestricted. After applying (4) to genuine frozen pairs, the positive reciprocal upper sums may drop coprimalities.

The lower profiles obey

$$
 \sum_{\substack{w\ {\rm squarefree}\\P^+(w)\le y}}
       \frac{\tau(w)\lambda^*(w)}w
  +\sum_{\substack{w>1\ {\rm squarefree}\\P^+(w)\le y}}
       \frac{\tau(w)\lambda^*(w)(1+\log P^-(w))}w
       \ll (\log(2y))^2 .
 \tag{8}
$$

The unmarked product has local factors $1+2\lambda^*(p)/p=1+2/p+O(p^{-2})$ (use $\lambda^*(2)=1$ for this positive enlargement). Factoring the log-marked sum by its least prime as in the [least-prime first-moment refinement](r64-source-least-prime-toggle-first-moment.md), the normalized weight has an extra denominator containing the local factors through that prime, $\gg(\log p)^2$. The normalized least-prime logarithm thus costs at most a constant times $\sum_p1/(p\log p)$, convergent by Chebyshev. This proves (8). The numerical restriction on the actual lower alphabet cannot increase these bounds.

For the second difference use $L_xL_y\ll L^2$, at most $\tau(s)\tau(t)$ choices of $c,d'$, the strip just established, and (8). The main part of (4) gives the total bound

$$
 O_\kappa\!\left(\mathfrak S(N)|I|\,\frac{L^2}{T^2}
                     L^{-1+2\alpha_1+2\alpha_2}\right).
 \tag{9}
$$

Either mixed term needs one short log strip and the unshifted least-prime log on the nonswitching side; both are covered by (8). Its remaining heavy log is at most $L$, giving the same bound, with an additional $1/L$ if retained.

To bound lattice errors, the number of ordered integer pairs of frozen cofactors with (7) is $O(Ne^{-18T}L)$ by harmonic summation. Each $h$ and $k$ has a unique split into lower product and singleton rough prime. The lower labels contribute at most $\tau(s)\tau(t)\le e^{2T}$, the original rough label choices and the roles of the switches only a bounded multiplicity, and the absolute marks are $\ll L^2$. The summed $e^{6T}$ error of (4) is $O(Ne^{-10T}L^3)=O_A(NL^{-A})$. No lower bound on the length of the *hard* interval was used.

## 4. The two light factors

At weight $A_1 A_2$ the final term of (5) is bounded by Cauchy on the genuine sum line after taking absolute values and summing the at most $O(\tau(s)\tau(t))$ labels. For either side freeze its lower product $w$ and one rough prime $r$. The remaining genuine prime has at most $O_\kappa(N/(w r L))$ choices by Chebyshev whenever $N/(wr)\ge N^\kappa$, and otherwise no choices. Sum the rough reciprocals, then the squared integer weights. They are at most

$$
 \ll_\kappa \frac{N}{L}
   \sum_{\substack{w>1\ {\rm squarefree}\\P^+(w)\le y_i}}
           \frac{\tau(w)^2(\log P^-(w))^2}{w}
       \ll_\kappa \frac{N}{L}(\log(2y_i))^4 .
 \tag{10}
$$

Indeed the Euler product now has local factors $1+4/p$, and its product through the least prime is $\gg(\log p)^4$. The square of the least-prime logarithm costs a convergent series dominated by $\sum_p1/(p(\log p)^2)$. Taking the geometric mean of the two squared masses gives $O_\kappa(NL^{-1+2\alpha_1+2\alpha_2})$. Hard cuts may be dropped at this positive bound, but both omitted variables were genuine primes in the count.

Combining (3), (9) and (10) proves (2) because $L^2/T^2=(\log L)^2$ and the even singular series is bounded below. The external minus and every divisor cutoff were unchanged in the inputs. The block is nonempty and can carry genuine signed summands: use one lower prime on each side with logs of order $L^{\alpha_i}$, and two distinct rough primes each near the corresponding central square-root scale divided by the square root of its lower prime. The PNT supplies all six distinct primes at narrow proportional widths. The sum is even with units and central; all rough primes exceed $D$ and cross-products exceed $Q$ since $L^{\alpha_i}=o(T)$. Each leg then has full mark minus its lower prime logarithm, yielding the negative product of those logs in (1), not a lower bound on the aggregate. The displayed freezing argument does not extend to a general longer rough label: a proper label may be a product or leave more than one rough prime outside, and (7) for a two-prime lattice no longer follows. The arithmetic-to-operator implication, if relevant, retains its separate estimates and assumptions.
