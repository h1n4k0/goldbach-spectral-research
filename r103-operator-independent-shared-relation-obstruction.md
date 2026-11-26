# A determinant obstruction to two small shared conductor relations

The original primitive-numerator incidence forces both shared character components to have their top local conductors. Consequently two nonparallel power relations cannot both place the pair on a small shared modulus. This is a support obstruction, not a norm estimate. It applies before detuning and is independent of Dirichlet GRH.

## 1. Live coefficients and the determinant restriction

Keep the actual alias $q=2k$, denominator $b$, progression modulus $q'=qb$, and genuine shared-factor convention of [R100 §1](r100-operator-three-factor-joint-powers.md#1-a-three-factor-sector-of-the-retained-field) and [R102 §1](r102-operator-shared-equal-gauss-conductor.md#1-exact-selection-and-packet-estimate):

$$
b=dm,\quad d=b_\parallel,\quad m=b_\perp,\qquad
 q=r_b h_q,\qquad s=dh_q,\qquad q'=r_b m s .
 \tag{1}
$$

Here $d$ is the full part of $b$ supported on primes dividing $q$; $h_q$ is the full part of $q$ on those primes. In particular $v_p(s)\ge2$ for every $p\mid s$. Let $\gamma,\gamma'$ be the two individual components on $s$, not their products or their restrictions to $d$. Call a pair live if its original character-pair incidence coefficient at a reduced rational numerator is nonzero in at least one of the original orientations. This definition concerns the coefficient of that individual pair. Subsequent analytic weights and sums can still annihilate it.

Let $\mathcal A$ be a finite family of pairs $(a,c)\in\mathbb Z^2$. For $v=(a,c)$ put $P_v=\gamma^a(\gamma')^c$, and let

$$
L=\operatorname{lcm}_{v\in\mathcal A}\operatorname{cond}(P_v).
 \tag{2}
$$

Conductors mean primitive inducing conductors, so $L\mid s$. Suppose $\mathcal A$ has rank two over $\mathbb Q$, and let $I$ be the positive greatest common divisor of the nonzero determinants of all pairs of its vectors. For a live pair,

$$
\operatorname{cond}(\gamma^I)\mid L,\qquad
    \operatorname{cond}((\gamma')^I)\mid L,\qquad
                          L\ge \frac{s}{2I^2}.
 \tag{3}
$$

These assertions allow signed integer exponents. When $(I,s)=1$, one has the stronger exact conclusion $L=s$.

There is also a local congruence restriction. For $p^A\parallel s$ set $E_p=v_p(L)$, and put $b_p=1$ at odd primes and at $p=2,A=2$, and $b_2=2$ at $p=2,A\ge3$. Define

$$
M_s(L)=\prod_{p^A\parallel s}
                        p^{A-\max(E_p,b_p)} .
 \tag{4}
$$

For this fixed pair and $L$, all relations with conductor dividing $L$ lie in a congruence lattice $c\equiv\vartheta_L a\pmod {M_s(L)}$, for one unit $\vartheta_L$ there. In particular $M_s(L)\mid I$ when the clipped exponent family has rank two. A relation satisfying this congruence need not have conductor dividing $L$, since the congruence alone does not test all tame or sign conditions. The modulus-one convention gives no restriction.

## 2. Proof using the literal unit fibers

Fix $p\mid d$, so $p\mid b$ and $v_p(q')\ge2$. In an original orientation $(\sigma_1,\sigma_2)$ the incidence on two unit coordinates $x,y\bmod q'$ has the congruence $q\mid \sigma_1x+\sigma_2y$ and phase $e(-A_0(\sigma_1x+\sigma_2y)/q')$, with $(A_0,b)=1$ and $e(t)=e^{2\pi it}$. If the first leg misses the top $p$-power conductor, its conductor divides $q'/p$. Shifting $x$ by $q'/p$ preserves its unit status and the genuine congruence because every prime of $q'$ remains a divisor of $q'/p$ and $q\mid q'/p$. The character factor is unchanged, while the numerator phase is multiplied by $e(-A_0\sigma_1/p)\ne1$. The sum on the original unit domain is therefore exactly zero. The same holds for the second leg. This is the local fiber argument of [R81 §2](r81-operator-low-conductor-long-quotient.md#2-exact-local-power-vanishing-and-the-low-conductor-fourth-moment) before any divisor truncation. Thus on a live pair both $\gamma$ and $\gamma'$ are primitive on the entire $s$. No bound on any Mangoldt progression error is involved.

For $v=(a,c),w=(a',c')$ with $\Delta=ac'-a'c\ne0$, compute

$$
P_v^{c'} P_w^{-c}=\gamma^\Delta,\qquad
        P_v^{-a'}P_w^a=(\gamma')^\Delta .
 \tag{5}
$$

The character group of modulus $s$ induced from any divisor modulus $L$ is a subgroup, via the unit reduction. All $P_v$ lie in it by (2), so the two powers in (5) also do. Bézout's identity in the exponents gives the same property for both powers with exponent $I$. This proves the first two claims of (3).

For clarity, the power loss is much smaller here than the generic primitive-conductor loss bound that includes the full radical of $s$: every initial local factor has a top exponent $A\ge2$. At an odd $p^A\parallel s$, a primitive local factor has wild order $p^{A-1}$. For $v=v_p(I)$, it retains the original conductor if $v=0$; if $0<v<A-1$ its new conductor exponent is $A-v$. If $v\ge A-1$, the ratio of original to new conductor is at most $p^A\le p^{2v}$, whether or not a tame part remains. At $2^A\parallel s$, an odd power retains full conductor. If $A=2$ and $v=v_2(I)\ge1$, the ratio is at most $2^2$. For $A\ge3$, the cyclic wild component generated by $5$ has exact order $2^{A-2}$ under a primitive character. If $0<v<A-2$, the new exponent is $A-v$. Otherwise the ratio is at most $2^A\le 2^{2v+1}$. Multiply these losses over the shared primes; the extra factor $2$ occurs at most once. This gives

$$
\operatorname{cond}(\gamma^I)\ge s/(2 I^2).
 \tag{6}
$$

If $(I,s)=1$, no local losses occur, so $\operatorname{cond}(\gamma^I)=s$ and $L=s$. This includes the trivial shared factor.

For (4), at odd $p$ use the two unit exponents $\lambda_p,\lambda'_p$ describing $\gamma,\gamma'$ on a generator of the cyclic wild subgroup of order $p^{A-1}$. They are units modulo $p$. A character factoring through $p^{E_p}$ must have wild exponent divisible by $p^{A-\max(E_p,1)}$, including $E_p=0$. Thus $a\lambda_p+c\lambda'_p\equiv0$ modulo the corresponding factor of (4). For $2^A$ with $A\ge3$ the same argument on $5$ uses the modulus $2^{A-\max(E_p,2)}$, and for $A=2$ it uses the sign generator $-1$ and $2^{A-\max(E_p,1)}$. The primitive $\lambda'_p$ are invertible at all these moduli. The Chinese remainder theorem gives one $\vartheta_L$ reducing to $-\lambda_p/\lambda'_p$ on them. Cross-multiplying the congruences for any two vectors shows $M_s(L)\mid\Delta$; hence it divides $I$. This yields the stated local restriction without claiming a converse.

## 3. Consequences on the actual retained selections

If each coordinate of each exponent pair is at most $V$ in absolute value, any two independent vectors have $0<|\Delta|\le2V^2$. Hence for a live pair two such shared power relations of conductors $A_1,A_2$ satisfy

$$
\operatorname{lcm}(A_1,A_2)\ \ge\ s/(8V^4).
 \tag{7}
$$

For instance, the exponent pairs with $\operatorname{cond}(P_v)\le L_0$ in this box span at most one rational line at a live pair whenever $L_0^2<s/(8V^4)$. This follows pairwise from $ \operatorname{lcm}(A_1,A_2)\le A_1 A_2$. If $s$ is a prime power, the sufficient condition improves to $L_0<s/(8V^4)$, since the lcm is then the larger of the two conductors. A common inducing modulus $L_0$ for all the considered relations admits the same stronger condition for arbitrary $s$. These conclusions describe a line that can depend on the genuine pair. They do not give one shared line, or cancellation, across all coefficients.

In particular, consider two prospective joint tests on the same coefficient after the preceding [R96 selection](r96-operator-equal-and-signed-joint-powers.md#1-exact-enlargement-and-packet-bound), requiring in each case the product of the alias, coprime-denominator, and shared mixed conductors to be at most $D_i$, $i=1,2$. Require that both tests' alias/coprime exponent triples are wholly in the actual R96 range, whose threshold is $D_J$. Retention by R96 forces the product of the first two conductors for either witnessing triple to exceed $D_J$. Consequently $A_i\le D_i/D_J$ for the two shared conductors; if a test's exponents are outside that earlier range, this step is not valid. With this exact range condition, (7) forbids two independent shared directions whenever

$$
\frac{D_1D_2}{D_J^2}<\frac{s}{8V^4}.
 \tag{8}
$$

The same conclusion holds if the left side is replaced by any true upper bound on their shared inducing lcm.

At the actual R100 and R102 numerical choices, consider their two arithmetic selectors together **before** the later deletions, keeping the old R96 gate and restricting R100 to its R96-covered exponent triples. The R100 shared pair has unequal positive exponents, whereas the R102 shared pair is $(a,a)$ with $a\ne0$, so they are independent. At $D_1=Q^{7/10}$, $D_2=Q^{133/200}$, $D_J=Q^{3/5}$, and $d\ge Q^{1/5}$, the left side of (8) equals $Q^{33/200}$. The right side is at least $Q^{1/5}/(8V^4)$, larger for sufficiently large $Q$ and any fixed polylogarithmic $V$. Thus no live pair belongs to both of those **arithmetic tests** on that preceding field. This is not the tautological disjointness of consecutive deletions, whose later inputs already omit the first. It asserts geometric incompatibility at a single original coefficient even if both tests are applied to the same earlier field. It neither compares the integrated fields nor gives orthogonality of their norms.

More generally a method that first demands two independent polylogarithmic shared relations with inducing lcm $L\ll dQ^{-\delta}$ for fixed $\delta>0$ has no live original incidence coefficient for sufficiently large $Q$, because $s\ge d$ and (7) contradict that cap. In particular such a cap cannot provide a nontrivial extension of the shared-product Gauss saving. The obstruction concerns two independent relations on one pair; one low relation, proportional relations, and sums of distinct pairs are not ruled out.

## 4. The quadratic determinant loss can occur on a retained coefficient

For the concrete packet scales of R102 choose an odd prime $p$ with $V/4<p<V/2$, for a fixed power $V=\lfloor(\log Q)^C\rfloor$ and sufficiently large $Q$, by Bertrand's postulate applied to $\lfloor V/4\rfloor$. Let $d=p2^e$ be obtained by taking the least $2$-power for which $d\ge Q^{1/5}$; choose an odd prime $m\in(B/(2d),B/d)$ and an odd prime $r\asymp Q^{9/20}$, distinct from $p,m$. Take $b=dm,\ k=pr,\ q=2pr$. Then $r_b=r,\ h_q=2p,\ s=2^{e+1}p^2$, and the true arithmetic gates $k>K,\ k\le4M,\ (2k,b)=2p<G,\ d\ge Q^{1/5}$ hold. The high band follows by construction. On $r$ use a generator and its conjugate. On $m$ take $\eta'=\eta^{2V^*}$ with $\eta$ a generator and $V^*$ bounding all the preceding fixed log-power ranges, as in [R102 §4](r102-operator-shared-equal-gauss-conductor.md#4-a-live-coefficient-beyond-the-r101-cutoff).

On $2^{e+1}$ take both shared factors to be the same sign-trivial primitive generator of the $5$-component. On $p^2$ take a primitive factor of order $p$ and its inverse, both trivial on the tame component. These two local products lift from the primitive conductor $2^e$ and from conductor one respectively, so the full shared product is induced from $d$ as required by the exact pairing. The $2$-part of every previously tested positive shared power, equal or unequal, has conductor $Q^{1/5-o(1)}$: its exponent is $a+c$ and loses at most a fixed log power. The same holds for any of the shared product's previous small powers. On $m$ all prior tested individual, product and signed mixed powers remain nonprincipal, including the powers in R102; the alias and $m$ conductors in the joint tests multiply to $rm\asymp Q^{.64}$. The alias conductor $r$ alone exceeds the earlier alias and alias/shared thresholds. Thus the earlier R98/R99 shared thresholds and R100/R101/R102 three-factor thresholds all fail to remove the pair, with the latter products at least $Q^{.84-o(1)}$. The full product stays high on $m$.

The coefficient is live in the unmodified input: at $2^{e+1}$ the congruence modulo $2$ is automatic on odd units and the two primitive Gauss sums at unit frequencies are nonzero. At $p^2$, fix an orientation and use the exact local parameterization of [R93 §2](r93-operator-unequal-mixed-denominator-powers.md#2-a-shared-prime-restriction-of-the-exact-gauss-factor), with local exponents $v_p(q)=v_p(b)=1$. The $x\bmod p$ transform is the Fourier transform of a nontrivial additive character $x\mapsto\overline{\gamma'_p(1+px)}$. It is exactly $p$ at one nonzero frequency and zero elsewhere. The outer local unit $r_0\bmod p$ permutes the nonzero frequencies, so just one term remains and is nonzero (here the local product is principal). The alias conjugacy factor on $r$ and primitive coprime Gauss factors on $m$ are nonzero too. This shows incidence, not a lower bound for an integrated or parity-reduced field.

Now take vectors $(1,1)$ and $(1,p+1)$, both within the indicated box for sufficiently large $Q$. Their determinant is $p$. Both mixed powers are principal on $p^2$, while on $2^{e+1}$ the exponents respectively are $2$ and $p+2$, the latter odd. Hence their inducing lcm is precisely $2^{e+1}=s/p^2$. This attains quadratic loss in the determinant even on an actual retained coefficient. These two conductors are not small in the sense of (8), and the example does not assert a large contribution to the operator.
