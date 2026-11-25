# Deleting small-power conductors from the actual larger-alias field

A large primitive conductor can collapse after taking a power of a character. This yields a further removal after the low-conductor cut: on the prime-to-denominator alias factor, all characters with a low-conductor power of polylogarithmic order can be deleted. The estimate is for the genuine selected Fourier packet, not a bound on the remaining covariance.

## 1. Exact selection and result

Keep the complete even target shell, genuine transported $h,f$ parent profiles, separated high packet $\mathcal C_+(B,R)$, original Fourier normalization $J^{-1}$, common taper, and polynomial parameter ranges of [R89](r89-operator-prime-to-denominator-alias-conductors.md). In particular assume the original local Dirichlet GRH for the even shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Keep $Q\le A\le QH/100$, $A/Q\le K\le4M$, and the larger aliases $k>K$. Write $R_*=1+R$. For each alias and denominator use

$$
q=2k=d_b r_b,\qquad
 d_b=\prod_{p\mid b}p^{v_p(q)},\qquad (r_b,b)=1,\qquad q'=r_b(d_b b).
 \tag{1}
$$

This last factorization is coprime. Denote the $r_b$ component of a character $\xi\bmod q'$ by $\xi_\perp$.

Let $Z$ be either actual input of R89: $\mathcal Z_{>K}$ or its exact post-[R86](r86-operator-long-alias-short-leg-even.md)/[R87](r87-operator-adaptive-raw-minimum-even.md) reduction with its compatible $K\ge2P$. Let $Z_{>D,\perp}$ be its true R89 reduction by the ordinary primitive conductor $>D$ on both $r_b$ legs. Fix $C>0$, put $U_Q=\lfloor(\log Q)^C\rfloor$, and let $D\ge1$. Define $Z_{\rm pow}$ by retaining instead, on each leg,

$$
\operatorname{cond}(\xi_\perp^m)>D
                    \quad\text{for every integer }1\le m\le U_Q.
 \tag{2}
$$

The powers are on the character group of units modulo $r_b$; the conductor is always the primitive inducing conductor. This includes the $m=1$ condition. The actual high selections on the other factors, true high product conductor, small common-divisor mask, $z,w>A$, orientations and their signs, parity restrictions where present, and exact Fourier detunings are unchanged.

For $\|X\|_{\rm pkt}=(\sum_{j\in\mathcal C_+(B,R)}\|X(j)\|_{\rm HS}^2)^{1/2}$, the estimate is

$$
\|Z-Z_{\rm pow}\|_{\rm pkt}+
       \|Z_{>D,\perp}-Z_{\rm pow}\|_{\rm pkt}
 \ll_{\Gamma,\Theta,C,\epsilon} Q^\epsilon B^{3/2}D
       \left[\frac{R_*^{3/2}+R_*^{5/2}}{Q}
                      +\frac{R_*^{1/2}}S\right].
 \tag{3}
$$

It is valid on the full parent space, including all raw early and late sectors together, and after any fixed orthogonal spatial compression or restriction to a subset of the packet. All conductor conditions are imposed on the actual characters before their original detunings.

At the R89 parameters, including $D=K=\lfloor Q^{81/200}\rfloor$, $B=\lfloor Q^{39/100}\rfloor$, $R=\lfloor Q^{1/400}\rfloor$, and $S=Q^{249/250}$, the bound is $O_{\epsilon,C}(Q^{-3/800+\epsilon})$. For the reduced input after R86/R87, the comparison of sharp $\widehat T,\widehat P$ to $Z_{\rm pow}$ retains the inherited $O_{\epsilon,C}(Q^{-1/500+\epsilon})$ rate. In particular one may remove all true $r_b$-characters of order at most $U_Q$, even when their primitive conductor is large. The estimate neither makes the retained all-powers-high field small nor extends to other Fourier modes, an individual modulus, or weak S.

As a check that the new arithmetic selection is not just the $m=1$ cut, consider an odd prime alias $k=r$ of size $Q^{11/20}$, and a prime denominator $b$ in the prescribed high band. They exist for large $Q$ by Bertrand's postulate, and $b<r$; this is within the larger-alias range of the concrete parameters. Then $r_b=2r$, and the nonprincipal quadratic character from $r$ has conductor $r>D$ and square of conductor $1$. If desired, choose the same character modulo $b$ of order $>2$ on both legs. Both are high in the R81 sense, and their product modulo $b$ is nonprincipal of conductor $b$, hence high in R82. The incidence is nonzero: on $2r$ the original relation pairs conjugate characters, and on $b$ the two nonzero primitive Gauss factors separate since $(2r,b)=1$. This demonstrates the strict enlargement of the eligible character sector; it is not a lower bound on its contribution.

## 2. A harmonic average of character power fibers

For integers $m\ge1$, let $T_m(r)=\#\{\chi\bmod r:\chi^m=1\}$, counting characters on units, with $T_m(1)=1$. We prove the unconditional uniform estimate

$$
\sum_{r\le8M}\frac{T_m(r)}r
                            \ll_{\Gamma,C,\epsilon} Q^\epsilon
                  \qquad(1\le m\le U_Q).
 \tag{4}
$$

The function is multiplicative in $r$ by CRT. At an odd prime $p$, the group of units modulo $p^a$ is cyclic, so

$$
T_m(p^a)=\gcd(m,p^{a-1}(p-1)),\qquad a\ge1.
$$

If $p\nmid m$, this is the same $\gcd(m,p-1)$ for every $a\ge1$, and the positive local harmonic factor equals $1+\gcd(m,p-1)/(p-1)$. If $p\mid m$, put $e=v_p(m)$. Each of the terms with $1\le a\le e+1$ is at most $1$ after multiplication by $p^{-a}$. On $a>e+1$, bound $T_m(p^a)$ by $p^e(p-1)$, giving a total tail at most $1/p$. The local harmonic factor is $O(1+e)$. At $p=2$ the unit groups for $a=1,2$ and the product of cyclic groups of orders $2,2^{a-2}$ for $a\ge3$ give the same $O(1+v_2(m))$ bound, since for $a>v_2(m)+2$ the remaining terms are geometric with numerator at most $2^{v_2(m)+1}$. Thus the combined factors of $p\mid m$ and $p=2$ are $m^{O(1)}$ up to an absolute constant.

By positivity $\sum_{r\le8M}T_m(r)/r$ is at most the product of those local factors over $p\le8M$, with the powers at each prime unrestricted in the upper bound. For the other factors the logarithm of the product is at most

$$
\sum_{p\le8M}\frac{\gcd(m,p-1)}{p-1}
      =\sum_{d\mid m}\varphi(d)
           \sum_{\substack{p\le8M\\p\equiv1\bmod d}}\frac1{p-1}
      \ll_\Gamma \tau(m)(1+\log\log(10Q)).
 \tag{5}
$$

For completeness, primes with $p\le3d+3$ in the inner sum contribute $O(1/d)$, as their $p-1$ are positive multiples of $d$ and there are only a bounded number of such multiples in that range. Above that point [Montgomery–Vaughan, Theorem 2, (1.10)](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf#page=3) gives $\pi(x;d,1)\ll x/(\varphi(d)\log(x/d))$. Partial summation from $3d+3$ bounds the weighted prime sum by $O((1+\log\log(10Q))/\varphi(d))$, uniformly in $d$, by integrating $dt/(t\log(t/d))$ up to $8M\le8Q^\Gamma$. For $d=1$ the same estimate follows directly as well, and if the lower limit is beyond $8M$ the tail is empty. The identity for the greatest common divisor in (5) is the usual totient divisor sum. Finally $\tau(m)\ll_\delta m^\delta$ for each fixed $\delta>0$; with $\delta=1/(4(C+1))$ the right side of (5) is $o(\log Q)$ uniformly in $m\le U_Q$. The exceptional prime factors have only $O_C(\log\log Q)$ logarithmic cost. This proves (4).

For every $r\ge1,m\ge1$ the map $\chi\mapsto\chi^m$ is a homomorphism on the finite group of characters modulo $r$; every attained image has exactly $T_m(r)$ preimages. There are at most $D\tau(r)$ characters modulo $r$ of primitive conductor $\le D$, by summing $\varphi(d)$ over $d\mid r,d\le D$. Hence, putting

$$
n_{D,U_Q}(r)=\#\{\chi\bmod r:\exists\,m\in[1,U_Q]\cap\mathbb Z,\
                              \operatorname{cond}(\chi^m)\le D\},
$$

we have the bound $n_{D,U_Q}(r)\le D\tau(r)\sum_{m\le U_Q}T_m(r)$. It follows from (4), $r/\varphi(r),\tau(r)\ll_\epsilon Q^\epsilon$ for $r\le8M$, and $U_Q=Q^{o(1)}$, that

$$
\sum_{r\le8M}\frac{n_{D,U_Q}(r)}{\varphi(r)}
                                  \ll_{\Gamma,C,\epsilon}Q^\epsilon D .
 \tag{6}
$$

In this use of (4) choose smaller intermediate $\epsilon$'s and absorb the finitely many resulting subpower factors. This is a harmonic **average**, not a claim that the torsion group is pointwise small uniformly for growing $m$.

## 3. The same fraction applies to both true progression factors

The exact product-character forcing of [R82](r82-operator-low-product-character-long-quotient.md) and R89 gives $\xi_\perp'=\overline{\xi_\perp}$ for every surviving pair. The condition counted in $n_{D,U_Q}$ is invariant under conjugation. Thus mixed retained/deleted pairs have zero incidence, as do mixed pairs if one restricts to those counted characters with original conductor $>D$ to estimate the incremental difference from $Z_{>D,\perp}$. In either case the deleted field contains both genuine progression vectors projected to the **same** class of $r_b$-characters. This projection is fixed once $k,b$ are fixed and commutes with the original parity projections on either leg; no collection of characters selected from a raw coordinate or a Fourier mode is being averaged.

At $(k,b)$ write $f_{k,b}=n_{D,U_Q}(r_b)/\varphi(r_b)$. Allowing every character on the other CRT factor gives at most that fraction of the total number of characters. Auxiliary GRH and the per-character argument of [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference) therefore imply, after normalized residue Parseval, for the actual projected vector $F^{\rm del}$

$$
\begin{split}
  \|F^{\rm del}(z)\|_2^2
       &\ll_\epsilon Q^\epsilon f_{k,b}\,z,\\
  \int_X^{2X}\|F^{\rm del}(z+h)-F^{\rm del}(z)\|_2^2\,dz
       &\ll_\epsilon Q^\epsilon f_{k,b}\,X|h|,
        \qquad 1\le|h|\le X/4 .
 \end{split}
 \tag{7}
$$

Here $X$ is any of the polynomial raw scales in that argument, and the same bounds hold for the even or odd projected legs. The estimates use the actual centered character coefficients at modulus $q'=2kb$, with the original high individual selections. In the incremental deletion one can use the same upper fraction because additionally requiring $\operatorname{cond}(\chi_\perp)>D$ only lowers that count.

At each fixed denominator $b$, group its possible aliases $2k=d_b r_b$ by $d_b$. The $d_b$ are supported on primes dividing $b$ and are at most $8M$; the argument of [R89 §4](r89-operator-prime-to-denominator-alias-conductors.md#4-count-the-actual-aliases-then-restore-the-fourier-packet) bounds their number by $O_\epsilon(Q^\epsilon)$ uniformly. Using (6) for each group, and relaxing parity, coprimality, and the original cut $(2k,b)<G$ only in this positive upper sum, gives

$$
\sum_{K<k\le4M}f_{k,b}\ll_{\Gamma,C,\epsilon}Q^\epsilon D,\qquad
 \sum_{K<k\le4M}\frac{f_{k,b}}{k}
                       \ll_{\Gamma,C,\epsilon}Q^\epsilon D/K .
 \tag{8}
$$

Neither estimate uses independence of actual aliases.

## 4. Transfer with both raw signs and exact detuning

The hypotheses used in the fixed-alias estimates of [R89 §3](r89-operator-prime-to-denominator-alias-conductors.md#3-per-alias-weighted-estimates-and-the-exact-masks) are precisely the common two-leg selection, the pointwise and increment bounds (7), and the actual profile envelopes. In its notation $f_{k,b}$ now replaces $\lambda_{k,b}$: each pointwise leg contributes $\sqrt{f_{k,b}}$; the symmetric increment square for the cosine difference and the interval-restricted raw Fourier estimate for the sine difference both use (7) linearly in $f_{k,b}$. The exact sum orientation uses the two pointwise factors. Thus for a common shell test $\omega$ the genuine per-alias bound for the unmodified larger-alias input is $O_\epsilon(Q^\epsilon b f_{k,b}[K_1+QK'_2])$, with $K_1=\|\omega\|_\infty+\|\omega'\|_1,\ K'_2=\|\omega''\|_1+K_1/Q$. This uses the same sharp-to-smooth raw comparison for differences before the marginal and sine estimates, not a marginal identity with a sharp mask still in place.

If the input is the post-R86/R87 residual, subtract the two projected even-removal fields exactly as in R89 (8). Their estimates follow from reflection and pointwise GRH only and are $O_\epsilon(Q^\epsilon b f_{k,b}(QP/k)(E_\infty+E_1))$ for the two removal pieces together, with the same derivative seminorms $E_\infty,E_1$ as there. The raw-branch masks are kept exact, and none is used to modify an unmasked marginal cancellation. By (8), all larger aliases sum with $D$ in place of the unrestricted alias count, and the latter pieces use $P\le K/2$.

Finally apply the original common Taylor tests for the distinct fractional detunings, keep the outer unit phase, divide by $J\asymp Q$, and aggregate $b,\ell$ exactly as in R89 §4. These common tests give effective $K_1=O(1+|\ell|)$, and $K'_2,E_\infty,E_1=O(S^{-1}+(1+|\ell|)^2/Q)$. The denominator and offset square sums produce $B^{3/2}$, $R_*^{3/2}$, $R_*^{5/2}$ and $R_*^{1/2}$ at their respective terms. This proves (3) both for the union and for the incremental removal. The three exponent costs in (3) at the stated parameters are $-1/160,-3/800,-19/4000$. No part of this argument controls the retained covariance across high-order characters whose powers all keep large conductor.
