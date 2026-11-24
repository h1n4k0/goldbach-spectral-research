# Low conductor factors of the actual long quotient covariance are removable

**Scope.** On the actual long–long centered product from R80, primitive additive quotient modes annihilate every progression character missing certain local prime powers. Furthermore a genuine family of low-conductor factors has the desired quotient fourth bound, and every crossed term containing one such factor is small in Hilbert–Schmidt RMS on the entire R78 high packet. High–high conductor covariance is not estimated. The result uses actual Mangoldt progression errors and their character projections, not a model for their distribution.

## 1. Setup and statements

Use the complete even shell, true $h,f$ parent profiles, fixed transported parent index space, high-denominator collars $\mathcal C_+(B,R)$, and the definitions of $q=2k,\ q'=qb,\ A_{-a},\ F_{q',r}(z)$, and the common real taper $\omega_S$ in [R79](r79-operator-exceptional-centered-product.md). At a selected index $j$, its unique reduced center is $Ja/b$ and its circular detuning and common phase are the R79 ones. Retain original local Dirichlet GRH across the shell and auxiliary Dirichlet GRH for all $q'\le\lceil8MB\rceil+2$, including $1$. Let $R_*=1+R$. The early raw coordinates have been removed by [R80](r80-operator-early-quotient-resonance.md): write $\mathcal X_{\rm long}(j)$ for its exact product with $z,w>A$, for $1\le A\le QH/2$. Both orientations of the positive difference and the negative sum retain their signs.

For each $q,b$ split $b=b_\parallel m$, where $b_\parallel$ contains the full powers in $b$ of primes dividing $q$, and $(m,q)=1$. Put $q_0=q b_\parallel$, so $q'=q_0m$ and $(q_0,m)=1$. A character $\xi\bmod q'$ is called **retained at the local powers** if its primitive conductor has exponent $v_p(q')$ at every $p\mid b$ with $v_p(q')\ge2$. Write such a character uniquely as $\xi=\chi_0\nu$ by CRT, with $\chi_0\bmod q_0,\nu\bmod m$. In this retained set distinguish

$$
\nu\text{ low if }\operatorname{cond}(\nu)\le m b^{-1/3},
       \qquad\text{high otherwise}.
 \tag{1}
$$

When the threshold is below $1$ there is no low component. In particular when $(q,b)=1$ it is the conductor cutoff $b^{2/3}$ for the genuine factor modulo $b$. The other factor $\chi_0$ has no conductor restriction beyond the local powers just defined.

In the finite character decomposition of the actual progression vector $F(z)$, define $F_{\rm lo}(z)$ and $F_{\rm hi}(z)$ by retaining only the corresponding character components above, and $F_{\rm dead}(z)$ by retaining only the characters missing a local power. Thus the original vector equals their sum. Define $\mathcal X_{\rm hi,hi}(j)$ by replacing both occurrences of $F$ in the exact long product $\mathcal X_{\rm long}(j)$ with $F_{\rm hi}$, separately at its actual $q,b$ on each alias. This replacement does not change the raw threshold, taper, phase, unit test at $q'$, or any signed orientation.

For a vector $G$ on units modulo $q'$, write $E_a(G;r_0)$ for its normalized quotient transform as in R80 (1), and $A_a(G)=\sum_{r_0\bmod q}|E_a(G;r_0)|^2$. Then for every primitive additive numerator $a\bmod b$ and actual $z$ in the raw support,

$$
\begin{split}
 E_a(F_{\rm dead}(z);r_0)&=0,\\
 \sup_{(a,b)=1}A_a(F_{\rm lo}(z))&\ll_{\Gamma,\epsilon} Q^\epsilon z/b,
       \qquad
 \sum_{a\bmod b}^{*} A_a(F_{\rm lo}(z))^2
                           \ll_{\Gamma,\epsilon}Q^\epsilon z^2/b .
 \end{split}
 \tag{2}
$$

Moreover the whole high packet satisfies

$$
\begin{split}
 \left(\sum_{j\in\mathcal C_+(B,R)}
       \|\mathcal X_{\rm long}(j)-
                    \mathcal X_{\rm hi,hi}(j)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\Theta,\epsilon} Q^\epsilon B
     \left[\frac M Q R_*^{5/2}+\frac M S R_*^{1/2}\right].
 \end{split}
 \tag{3}
$$

This bound uses the full actual signed product, including crossings with one high and one low leg. It applies on the entire parent space and after any fixed compression or restriction to any subset of Fourier indices.

At the R80 parameters $H=Q^{2/5},M=Q^{3/5},W_V=Q^{23/175}V^{4/7},B=\lfloor Q^{39/100}\rfloor,R=\lfloor Q^{1/400}\rfloor,A=Q^{6/5}$, choose $S=Q^{249/250}$. Then (3) is $O_\epsilon(Q^{-3/800+\epsilon})$. Use R79 and R80 with this same $S$, and with $B_0=\lfloor Q^{1/5}\rfloor,\ R_0=\lfloor Q^{1/4}\rfloor,\ \kappa=3/10$ for the benchmark comparison. The true untapered $\widehat T$, and also the true $\widehat P$, differ from $\mathcal X_{\rm hi,hi}$ in full high-packet HS RMS by

$$
O_\epsilon(Q^{-1/500+\epsilon}).
 \tag{4}
$$

In particular this comparison holds on every exceptional mode excluded by [R78](r78-operator-flat-numerator-most-modes.md). The actual high–high field could still contain substantial energy.

## 2. Exact local-power vanishing and the low-conductor fourth moment

For $r_0\bmod q$ consider $r=r_0+qv,\ v\bmod b$, and extend every vector by zero at nonunit lifts. Suppose $p\mid b,\ v_p(q')\ge2$, and a character misses the last conductor power at $p$. Then its conductor divides $q'/p$. The shift $v\mapsto v+b/p$, equivalently $r\mapsto r+q'/p$, preserves the $q$-fiber and the unit set: every prime divisor of $q'$, including $p$, still divides $q'/p$. The inducing character also has unchanged values. The quotient phase $e(av/b)$ is multiplied by $e(a/p)\ne1$ for $(a,b)=1$. Summing over the invariant fiber proves exact vanishing for this character. Apply this to every discarded character to get the first part of (2). No cancellation of prime sums is assumed here.

For the remaining low estimate, write the exact full progression error in multiplicative characters:

$$
F_{q',r}(z)=\frac1{\phi(q')}
             \sum_{\xi\bmod q'}\overline{\xi(r)}\,W_\xi(z),\qquad
 W_\xi(z)=\psi(z,\xi)-z\,\mathbf1_{\xi=\xi_{\rm princ}} .
 \tag{5}
$$

Auxiliary GRH yields $|W_\xi(z)|\ll_{\Gamma,\epsilon}Q^\epsilon\sqrt z$ uniformly on the raw ranges here, including imprimitive characters and the principal with its centering; the unit-prime-power corrections are absorbed by the same bound. For $z<1$ the assertion follows directly as well. Orthogonality and finite character Parseval show $\|F(z)\|_2\ll Q^\epsilon\sqrt z$, and each of its indicated orthogonal projections obeys the same bound.

Let $D=m b^{-1/3}$. If $D<1$ there is nothing to bound. Otherwise fix a primitive additive $a\bmod b$. In $r=r_0+qv$, split $v$ into $v_\parallel\bmod b_\parallel$ and $v_\perp\bmod m$. The phase $e(av/b)$ splits into two phases with primitive additive frequencies on each factor by CRT. Put $a_\perp\equiv a\overline{b_\parallel}\bmod m$ for the $v_\perp$-frequency. The case of a unit factor uses the unique phase $1$ on that factor. In the sum defining $E_a(F_{\rm lo};r_0)$ first form, for each $r'=r_0+qv_\parallel\bmod q_0$,

$$
G_{r'}=m^{-1/2}\!\!
 \sum_{\substack{v_\perp\bmod m\\
                   r_0+qv_\perp\ {\rm unit}\bmod m}}
        e(a_\perp v_\perp/m)\,
             F_{\rm lo}(r_0+qv).
 \tag{6}
$$

Take only $r'$ unit modulo $q_0$; for a nonunit $r_0\bmod q$ all terms vanish. Because $q_0=q b_\parallel$, the map $(r_0,v_\parallel)\mapsto r'\bmod q_0$ is a bijection before imposing these units, and the units are exactly as stated. The normalized outer $v_\parallel$ sum is bounded by Cauchy:

$$
A_a(F_{\rm lo})\le
                                  \sum_{r'\bmod q_0}^{*}|G_{r'}|^2 .
 \tag{7}
$$

There is no loss of $b_\parallel$ in (7).

For a character $\nu\bmod m$ of conductor $d\mid m$ the normalized inner Fourier factor after $s=r_0+qv_\perp\bmod m$ has absolute value at most $\sqrt{d/m}$. Here is the imprimitive case explicitly. For a primitive additive $c\bmod m$, the unnormalized factor is, up to a phase of absolute value one,
$\sum_{s\bmod m}^{*}\bar\nu(s)e(cs/m)$.
Write $\nu^*$ for the primitive inducing character modulo $d$. Expanding the extra unit exclusions gives terms

$$
\mu(t)\overline{\nu^*(t)}
       \sum_{u\bmod m/t}\overline{\nu^*(u)}e(cu/(m/t)),
       \qquad t\mid m,\quad (t,d)=1 .
$$

The additive sum over lifts of one residue modulo $d$ vanishes unless $m/t=d$, because $c$ is coprime to $m$. In the possible surviving term, the primitive Gauss sum has magnitude $\sqrt d$, and the prefactor has magnitude at most one. This applies also to $d=1$. Thus the claimed normalized bound holds. In (6) the extra phase from the change $s=r_0+qv_\perp$ is common to all characters for the given $r'$ and can be removed before taking its squared norm.

Insert (5) in (6), restricted to the actual low and local-power-retained characters. Orthogonality in $\chi_0\bmod q_0$ gives a bound for (7):

$$
A_a(F_{\rm lo})\ \le\
 \frac1{\phi(q_0)\phi(m)^2}\sum_{\chi_0\bmod q_0}
 \left|\sum_{\substack{\nu\bmod m\\ \operatorname{cond}(\nu)\le D\\
                \chi_0\nu\ {\rm retained\ at\ the\ local\ powers}}}
       W_{\chi_0\nu}(z)\,c_{\nu,a}\right|^2 ,
 \quad |c_{\nu,a}|\le\sqrt{\operatorname{cond}(\nu)/m}.
 \tag{8}
$$

In fact the right side before the inequality in (7) is exact with the corresponding Gauss factors, with no assumption of independence across characters. Formula (8) remains valid if the local-power constraints make the inner sum depend on $\chi_0$. There are at most $\phi(d)$ characters induced from each particular conductor $d\mid m$. Hence

$$
\sum_{\substack{\nu\bmod m\\\operatorname{cond}(\nu)\le D}}
                  \sqrt{\operatorname{cond}(\nu)/m}
   \ll_\epsilon Q^\epsilon D^{3/2}/\sqrt m.
$$

Use (5) and $\phi(m)\gg_\epsilon m^{1-\epsilon}$, and note that $D^3/m^3=b^{-1}$, to obtain the second-line pointwise bound in (2). Parseval in the **complete** quotient frequencies gives $\sum_{a\bmod b}A_a(F_{\rm lo})=\|F_{\rm lo}\|_2^2\ll Q^\epsilon z$. Combine it with the pointwise primitive-frequency bound to obtain the fourth moment in (2). This is a genuine estimate for the stated part of the prime-progression error.

In cyclic shift coordinates, if $g_{r_0}(v)=F_{\rm lo}(r_0+qv)$ with zero at nonunits and $C(h)=\sum_{r_0,v}g_{r_0}(v+h)\overline{g_{r_0}(v)}$, then $A_a(F_{\rm lo})=b^{-1}\sum_h C(h)e(ah/b)$. Thus (2) also proves $\|P_{\rm prim}C\|_2^2\ll Q^\epsilon z^2$, where $P_{\rm prim}$ projects cyclic shift functions onto the reduced additive frequencies. It does not prove this shift variance for the full unconstrained prime vector.

## 3. Mixed terms in the actual centered product

Use the full residue-block identity from [R78 (7)–(8)](r78-operator-flat-numerator-most-modes.md#2-the-flat-weighted-quotient-incidence). For one orientation and any two actual projected or unprojected vectors $G,H$, its entry at primitive $a$ is a sum over $r_0\bmod q$ of products of the two normalized quotient transforms times $b$ and phases of absolute value one. The matched partner fiber is $s_0\equiv-\sigma_1\sigma_2r_0\bmod q$. Cauchy in these fibers gives

$$
\left|\sum_{r,s\bmod q'}^{*}A_{-a}(r,s)G(r)H(s)\right|
 \le b\,\big(A_{-\sigma_1 a}(G)A_{-\sigma_2 a}(H)\big)^{1/2}.
 \tag{9}
$$

If a dead component is present the expression vanishes exactly by (2). If one leg is low, for instance $G=F_{\rm lo}(z)$, and the other is $F(w)$ or any orthogonal restriction of it, use the primitive pointwise bound (2) on the first leg and quotient Parseval $\sum_a A_a(H)=\|H\|_2^2\ll Q^\epsilon w$ on the second. After summing the square of (9) over reduced numerators,

$$
\left(\sum_{a\bmod b}^{*}
       \left|\sum_{r,s\bmod q'}^{*}A_{-a}(r,s)G(r)H(s)\right|^2\right)^{1/2}
                 \ll_\epsilon Q^\epsilon\sqrt b\,\sqrt{zw}.
 \tag{10}
$$

The same holds with the low leg second. This is the square-root improvement compared with applying the pointwise GRH residue-energy bound to arbitrary full vectors on both legs. The algebraic difference between the full bilinear product and the high–high product is exactly the sum of (low, live) and (high, low), once the dead terms are removed; thus there are only these two crossed terms to bound. The selection is inside the true prime error vector, without introducing an extra signed continuum or diagonal term.

For clarity we detail the aggregation into the exact R80 field. With one common smooth test $\omega$ before the fractional numerator detuning, let $K_1=\|\omega\|_\infty+\|\omega'\|_1$ and $K_2=\|\omega''\|_1$. On dyads $V\le U$ and parent pair $I,I'$, the common mixed derivative estimate [R76 (5)](r76-operator-joint-rational-numerator-variance.md) has $L^1$ bound

$$
\ll b_Ib_{I'}[K_1+(QV/k)(K_2+K_1/Q)] .
$$

Restrict its integral to $z,w>A$ as in R80, *after* the derivative. No derivative of the indicator is taken. Its raw supports permit $\sqrt{zw}\ll Q\sqrt{VU}$. Minkowski in the common integral and (10) bounds the numerator norm on this one entry and alias by $Q^\epsilon\sqrt b Q\sqrt{VU} b_I b_{I'}$ times the bracket just displayed. In HS the parent envelopes have squared sums $O(1/(QV))$ and $O(1/(QU))$, so $Q\sqrt{VU}b_I b_{I'}$ costs $O(1)$. Sum $k\le4U$, using the harmonic bound for $1/k$, then sum dyads and all signed orientations. The resulting estimate before the shell normalization is

$$
\ll_\epsilon Q^\epsilon\sqrt b\,M(K_1+QK_2).
 \tag{11}
$$

The pointwise cuts and character sets may vary with $k,b$ as defined above, but not with the common test variable $t$; all bounds used in the integration and alias sum are uniform.

For each fixed denominator and integer shift $\ell$ use the fractional-rounding Taylor weights of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) on (11). This yields the effective $K_1\ll1+|\ell|$ and $K_2\ll S^{-1}+(1+|\ell|)^2/Q$ and keeps the exact modulus Fourier test up to the harmless absolute-value-one phases of R79. Dividing by $J\asymp Q$, the joint numerator error is therefore at most

$$
Q^\epsilon\sqrt b\left[
               \frac M Q(1+|\ell|)^2+\frac M S\right].
$$

Sum in squared norm over $b\in[\lceil B/2\rceil,B]$ and $|\ell|\le R+1$, using $\sum b\ll B^2$ and the corresponding shift moments $O(R_*^5)$, $O(R_*)$. Any redundant representations only overcount the square. This gives (3).

At the stated parameters the first and second terms of (3) have exponents $-3/800$ and $-19/4000$. In the same parameters R80 (4) with the larger $S=Q^{249/250}$ is still $O_\epsilon(Q^{-9/800+\epsilon})$. In R79 (3) the common edge is now $Q^{-1/500}$; the model, equality, principal, and single-error pieces are smaller, including the body mask error $O_\epsilon(Q^{-1/50+\epsilon})$. This proves (4) with the original sharp shell and both exact signed/Gram comparisons. It leaves the actual long–long high–high conductor covariance open.
