# Two higher sparse bands without a proper-divisor gap

Use the original signed central sum, hard interval $I\subseteq I_0=[\rho N,(1-\rho)N]$, strict tests $d>D$, $e>D$, $de>Q$, and true squarefree unit masks of the [two-higher-band theorem](r67-source-two-higher-bands-proper-divisor-gap.md). In particular, for even $N$ put $L=\log N$, $\ell=\log L$, $T=L/\ell$,

$$
     D=\lfloor\sqrt N e^{-20T}\rfloor,\qquad
     Q=\lfloor N e^{-20T}\rfloor.
$$

For fixed $0<\kappa<1/4$ and $0<c_i<d_i<\infty$, select integers $n=su,\ m=tv$, with both nonempty lower products $s,t$ made up of primes in the respective higher sparse bands $[\exp(c_iT),\exp(d_iT)]$. Both rough parts are nonempty, with every rough prime $\ge N^\kappa$. There is **no whole-product cap** on either lower product, no relation imposed between the two band constants beyond their individual ordering, and **no gap condition** on the proper divisors of either rough part.

**Theorem (unconditional, pointwise).** For every fixed $A>0$, all sufficiently large even $N$, and all admissible hard $I$,

$$
 \begin{split}
 R_N(I)&=-
 \sum_{\substack{n+m=N,\ n\in I,\ m\in I_0\\(nm,N)=1,\ n,m\ {\rm selected}}}
 \ \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
     \mu(d)\mu(e)\log(n/d)\log(m/e),\\
 |R_N(I)|&\ll_{\rho,\kappa,c_i,d_i,A}
              \mathfrak S(N)\left(\frac{|I|}{\log\log N}+NL^{-A}\right).
 \end{split}
 \tag{1}
$$

Additional integer masks independent of the interior divisor labels are allowed. For the exact least-prime double-switch expansion, the light–light and both heavy–light terms in fact contribute $O(\mathfrak S(N)(|I|/\ell^2+NL^{-A}))$. The second difference is controlled at the scale $|I|/\ell$ in (1). No exceptional moduli, first-moment extrapolation, or assumption on residue distribution of primes is used. This estimate requires the fixed polynomial rough cutoff, and does not assert the same saving at the growing rough threshold, for dense lower alphabets, for the full source operator, or for Hypothesis S.

## 1. Pointwise truncation with no original cap

Let $\varepsilon=1/32$. The sparse-band Rankin argument in the two-higher-band theorem applies before any gap condition: we can restrict $s,t\le N^\varepsilon$ with total error $O_A(NL^{-A})$, uniformly in the hard $I$ and the chosen masks. To detail the relevant arithmetic, there are at most $K=\lfloor1/\kappa\rfloor$ true rough primes on each side, so the absolute marked divisor weight is $O_\kappa(L\tau(w))$ on the lower product $w$ of either operand. The unrestricted squared reciprocal lower moment is bounded by

$$
  \sum_{\substack{w\ {\rm squarefree}\\
               p\mid w\Rightarrow \exp(c_iT)\le p\le\exp(d_iT)}}
            \frac{\tau(w)^2}{w}
       =\prod_{p\ {\rm in\ band}\ i}(1+4/p)=O_{c_i,d_i}(1)
$$

by Mertens, since the ratio of the endpoint logarithms is constant. For $w>N^\varepsilon$, Rankin at $\lambda/T$ with $\lambda>0$ fixed multiplies this upper profile by $L^{-\varepsilon\lambda}$, while replacing the product by at most $\prod(1+4e^{d_i\lambda}/p)=O_{c_i,d_i,\lambda}(1)$. Counting multiples of a fixed $w$ by $N/w$ and applying Cauchy on the actual equation $n+m=N$ loses only the square root of that Rankin saving and the factor $NL^2$. Taking $\lambda$ large in terms of $A$ permits the truncation on each side. Henceforth $s,t<D$ and $u,v\ge\rho N^{1-\varepsilon}>\sqrt N$.

## 2. Exact signed switches give a strip independent of the other rough label

Use the [exact double-switch expansion](r65-source-pointwise-two-rough.md) on each retained actual pair. Put $a=P^-(s)$, $b=P^-(t)$; for rough divisor labels $f\mid u, g\mid v$ and lower divisors $c\mid s/a$, $d'\mid t/b$, let $x=cf$, $y=d'g$, $L_x=\log(n/x)$, $L_y=\log(m/y)$, and

$$
 J_{\epsilon\eta}
 =\mathbf1_{a^\epsilon x>D}\,
   \mathbf1_{b^\eta y>D}\,
   \mathbf1_{a^\epsilon b^\eta xy>Q},
          \qquad \epsilon,\eta\in\{0,1\}.
$$

After extracting the genuine factor $\mu(x)\mu(y)$, the four marked terms exactly sum to

$$
 L_xL_y(J_{00}-J_{10}-J_{01}+J_{11})
 +(\log a)L_y(J_{10}-J_{11})
 +L_x(\log b)(J_{01}-J_{11})
 +(\log a)(\log b)J_{11}.
 \tag{2}
$$

If the second difference is nonzero, there is a first-side switch for some fixed opposite bit $\eta$. Otherwise $J_{10}=J_{00}$ and $J_{11}=J_{01}$, making it zero. The mixed terms require a switch precisely on their heavy side. For any actual fixed opposite value $E>D$, a first-side switch is the strict cutoff condition

$$
       x\le \max(D,Q/E)<a x .
 \tag{3}
$$

Indeed both possible terms share the fixed opposite test, which must pass; since $a>1$ the first indicator can only change from zero to one. As $E\ge D+1$ and the floors are original,

$$
       D\le \max(D,Q/E)\le\sqrt N.
$$

It follows that **every** first-side switch, whether or not the product boundary is active, puts the genuine rough divisor $f$ into the interval

$$
                  \frac{D}{a c}< f\le \frac{\sqrt N}{c}.
 \tag{4}
$$

No placement of the other rough label is required for this necessary condition. Its log width is $\tfrac12 L-\log D+\log a=20T+\log a+o(1)=O_{d_1}(T)$. The empty and full first rough labels cannot switch: $a c\le s<D$ for the empty label, and $c u>\sqrt N$ for the full label. Thus a switching $f$ is nonempty and proper. The second-side version of (4) is identical with the roles exchanged.

The use of (4) is the essential change from the two-freeze estimates. Keep the exact signed difference until a genuine switch is established; only then enlarge its positive counting envelope to the whole strip (4). This lets one leave the other **entire** rough part unfrozen. In particular, no extra product cap is needed to keep the number of frozen pairs small.

## 3. The polynomial-depth affine upper bound

For a first-side switch freeze $h=sf,k=t$, leaving the two genuine rough integers $P=u/f,V=v$ on $hP+kV=N$. For a second-side switch freeze $h=s,k=tg$ in the other orientation. For the two-light term freeze just $h=s,k=t$. These choices retain the original interval $hP\in I$, and every remaining product is nonempty. From (4) in a switched term and from the truncation, all freezes satisfy

$$
                 hk\le N^{1/2+2\varepsilon}=N^{1-\omega},
              \qquad \omega=1/2-2\varepsilon>0.
 \tag{5}
$$

The switch can be chosen before taking the positive bound; the at most two opposite-bit choices in the second difference cost a fixed multiplicity, and the two-light term needs none.

Apply the [affine rough-integer sieve](r65-source-pointwise-rough-complements.md) with $Z=N^{\omega/24}$ and $z=Z^\eta$ for a fixed $0<\eta<\min(\eta_0,24\kappa/\omega)$, where $\eta_0$ is its small absolute sieve constant. Every true remaining rough integer has no prime divisor $\le z$. Each actual frozen pair has $(hk,N)=(h,k)=1$, since both are part of true units and any common prime would divide $N$. Thus the two forms on the $j$ lattice have determinant $N$ and one local product root at primes dividing $hk$ or $N$, including two, and two roots at the other primes. Their exact hard interval has length $|I|/(hk)$. The quadratic sieve, with $O(Z^6)$ total floor error per frozen pair, gives the positive upper bound

$$
     O_{\kappa}\!\left(
       \frac{\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)}{hk L^2}
                  +N^{\omega/4}\right),
       \qquad
       \lambda^*(w)=\prod_{\substack{p\mid w\\p>2}}\frac{p-1}{p-2}.
 \tag{6}
$$

Here $\log z$ is a fixed positive multiple of $L$; composite rough parts are allowed, because this sieve only tests the absence of small primes. No estimates for primes or rough integers in individual arithmetic progressions are imported.

The number of ordered integer pairs $(h,k)$ in (5) is $O(N^{1-\omega} L)$. Each such integer has a unique split into lower primes in its higher band and a rough frozen part, because those ranges are disjoint for large $N$. For fixed cofactors and actual operands, the omitted rough labels are bounded in terms of $K$, and the lower divisors contribute at most $\tau(s)\tau(t)=N^{o(1)}$ on the truncated support. The latter follows uniformly by splitting their prime factors at $\sqrt L$. All the absolute marks are $O(L^2)$. The summed lattice error is therefore $O(N^{1-3\omega/4+o(1)})=O_A(NL^{-A})$. This treats the exact original hard endpoints, without even asking that the particular hard interval have long lattice length.

## 4. Positive upper bounds after the exact expansion

The lower unmarked profiles

$$
   \sum_{\substack{w\ {\rm squarefree}\\
      p\mid w\Rightarrow p\ {\rm in\ band}\ i}}
       \frac{\tau(w)\lambda^*(w)}{w}
     =\prod_{p\ {\rm in\ band}\ i}(1+2\lambda^*(p)/p)
     =O_{c_i,d_i}(1)
$$

are bounded since the bands are sparse. Inserting any one least-prime logarithm on a nonempty $w$ costs $O(T)$. Frozen rough factors in $\lambda^*$ cost at most a constant in terms of $K$. For each fixed lower label and each possible rough arity, the reciprocal weight of a nonempty rough product in (4) is $O_\kappa(T/L)$: after fixing all but one constituent rough prime, the remaining prime is in a log interval of width $O(T)$ at polynomial size. Chebyshev over enclosing unit-log intervals gives $O_\kappa((1+T)/L)$ for it, while the other rough reciprocal sums on $[N^\kappa,N]$ are bounded. The uniformity in the center of the strip allows the bounded-label and lower-divisor sums after this upper bound; the strip has been used only on an actual switched branch.

For $L_xL_y$ times its second difference, use (4) on the first side, (6), and the two unmarked profiles. The two weights are at most $L^2$, canceled by the sieve $L^{-2}$; the remaining strip gives $T/L=1/\ell$. For either heavy–light term one log is at most $L$ and the actual least-prime log on the other side is $O(T)$. The corresponding heavy-side strip and the same sieve give $(L T)/L^2$ times $T/L$, namely $\ell^{-2}$. The two-light term has no strip; its two $O(T)$ logs and (6) give $T^2/L^2=\ell^{-2}$. Masks and exact coprimalities may be dropped only now in the positive reciprocal enlargements, never to create an opposite value for (3). Adding the true tails and floor errors proves (1), with the original external minus sign unchanged.

There are genuine nonzero pairings outside both orientations of the [shrinking-gap theorem](r67-source-two-higher-bands-shrinking-divisor-gap.md). For example use lower singleton primes $s,t$ strictly within the bands $[\exp(T),\exp(2T)]$. About an external scale $X$, choose two distinct rough primes on each side near $\sqrt{X/(2s)}$ or $\sqrt{X/(2t)}$, with all primes distinct. The PNT supplies them in fixed narrow proportional windows. The even target is comparable to $X$, both operands are central units, and the lower primes remain interior by the $O(1/\ell)$ change in $T$ from bounded changes of $\log N$. Each individual rough prime is larger than its side's $D/s$ or $D/t$, yet below the uniform long threshold $\max(D,\lfloor Q/(D+1)\rfloor)\sim\sqrt N$. Hence the prior exact proper-divisor mask fails on both sides. Nevertheless every nonempty rough label exceeds $D$ on its own, and every cross-product exceeds $Q$ in this particular example, with an exponential-in-$T$ margin from the choice of bands. The complete signed mark on each side is minus the lower prime logarithm, because the sum of the rough Möbius signs over nonempty subsets is $-1$. The original pair therefore has true summand $-\log s\log t$. This verifies nonvacuity, not an aggregate lower bound. The general proof did not assume this example's automatic product cutoff.
