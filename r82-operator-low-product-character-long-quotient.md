# Removing low product characters from the genuine high–high quotient covariance

**Scope.** We delete a genuinely different sector of the actual high–high character product left by R81. In the exact switched incidence a pair can contribute only if its product character factors through the quotient denominator. All such products of small conductor, including the entire conjugate diagonal, have power-small total energy on the R78 high packet. We also remove every alias with a sufficiently large common divisor with the quotient denominator, without imposing a product-character cut on those aliases. The remaining high products are not estimated.

## 1. Exact setup and assertions

Use the original complete even shell, transported parent basis, actual $h,f$ profiles, and finite Fourier convention of [R79](r79-operator-exceptional-centered-product.md). The high-denominator packet $\mathcal C_+(B,R)$ has the same spacing and unique center $(a,b)$ with $\lceil B/2\rceil\le b\le B,\ (a,b)=1$, and the same exact circular detuning for each Fourier index. Assume the original local Dirichlet GRH at the even moduli and auxiliary Dirichlet GRH up to $\lceil8MB\rceil+2$, including $1$. Write $R_*=1+R$, and use the single common actual shell taper of edge length $O(S)$, $2\le S\le Q/100$. Retain the real integration domain $z,w>A$ from [R80](r80-operator-early-quotient-resonance.md), with $1\le A\le QH/2$. Let $\mathcal X_{\rm hi,hi}$ be the genuine long–long high–high field of [R81](r81-operator-low-conductor-long-quotient.md), with both of its actual high selections on the multiplicative characters modulo $q'=qb,\ q=2k$. The sign coefficients of its two positive difference and one negative sum orientations are unchanged.

Write $\pi_{q',b}$ for reduction on the unit groups modulo $q'$ and $b$. In the finite character expansion of its two-error integrand, let $\xi,\xi'\bmod q'$ be the two actual high characters. If $\xi\xi'$ does not factor through $\pi_{q',b}$, its primitive-numerator incidence is identically zero. Otherwise write $\xi\xi'=\nu\circ\pi_{q',b}$ for the unique product character $\nu\bmod b$. Thus $\nu$ is the character of a pair, not the individual CRT factor whose conductor was cut in R81.

For reals $D_\times\ge1,\ G\ge1$, define $\mathcal X_{\mathrm{res}}(j)$ by keeping in $\mathcal X_{\rm hi,hi}(j)$ only those terms for which

$$
(2k,b)<G,\qquad
             \xi\xi'=\nu\circ\pi_{q',b},\qquad
             \operatorname{cond}(\nu)>D_\times .
 \tag{1}
$$

The selections are made in the exact finite expansion inside each affine integral, before applying its original test for $j$. Then

$$
\begin{split}
 &\left(\sum_{j\in\mathcal C_+(B,R)}
  \|\mathcal X_{\rm hi,hi}(j)-\mathcal X_{\mathrm{res}}(j)\|_{\rm HS}^2
                                  \right)^{1/2}\\
 &\quad\ll_{\Gamma,\Theta,\epsilon} Q^\epsilon
       \left(BD_\times+\frac{B^{3/2}}{G}\right)
       \left[\frac M Q R_*^{5/2}+\frac M S R_*^{1/2}\right].
 \end{split}
 \tag{2}
$$

The bound holds on the whole common parent space and hence also after fixed orthogonal compression or restriction to arbitrary subsets of these Fourier indices.

For the actual R81 parameters

$$
\begin{gathered}
 H=Q^{2/5},\quad M=Q^{3/5},\quad W_V=Q^{23/175}V^{4/7},\quad
 A=Q^{6/5},\\
 B=\lfloor Q^{39/100}\rfloor,\quad
 R=\lfloor Q^{1/400}\rfloor,\quad S=Q^{249/250},
             \quad D_\times=Q^{1/1000},\quad G=Q^{1/5},
 \end{gathered}
 \tag{3}
$$

the low-product contribution is $O_\epsilon(Q^{-11/4000+\epsilon})$; the large-common-divisor contribution is $O_\epsilon(Q^{-7/800+\epsilon})$. Combining with R81 (4) at this same taper shows that the **true sharp-shell** $\widehat T$ and actual $\widehat P$, each on the full high packet, differ from the field $\mathcal X_{\mathrm{res}}$ by $O_\epsilon(Q^{-1/500+\epsilon})$ in HS RMS. The auxiliary cap remains $O(Q^{99/100})$. This includes every exceptional index of [R78](r78-operator-flat-numerator-most-modes.md), but asserts no smallness of the retained field on any such subset.

## 2. Exact dependence on the product of the two characters

Fix $q,b$ and an orientation $(\sigma_1,\sigma_2)$. For any two characters of $q'$, the full incidence coefficient, with the same negative rational twist as R79 (2), is

$$
\mathcal I_{\xi,\xi'}(a)
   =\sum_{r,s\bmod q'}^*
      \overline{\xi(r)}\,\overline{\xi'(s)}
       \mathbf1_{q\mid\sigma_1r+\sigma_2s}
             e\!\left(-\frac{a(\sigma_1r+\sigma_2s)}{qb}\right).
 \tag{4}
$$

Since $r,s$ are units, set $s=t_0 r\bmod q'$ with $t_0$ a unit. The congruence in (4) is then $t_0\equiv-\sigma_1\sigma_2\bmod q$. On those $q$-lifts put $c(t_0)=(\sigma_1+\sigma_2t_0)/q\bmod b$, with any consistent integer representative. Hence (4) is exactly

$$
\sum_{\substack{t_0\bmod q'\ {\rm unit}\\
                   t_0\equiv-\sigma_1\sigma_2\bmod q}}
       \overline{\xi'(t_0)}
        \sum_{r\bmod q'}^*
            \overline{(\xi\xi')(r)}e(-a c(t_0)r/b).
 \tag{5}
$$

The $b$ lifts before the unit cut have distinct values of $c(t_0)\bmod b$. The unit reduction from $q'$ onto $b$ is surjective, including when $(q,b)>1$, with fibers of size $\phi(q')/\phi(b)$. In (5) the additive phase is constant on each fiber. Orthogonality on the kernel kills it unless $\xi\xi'$ factors through $b$ as $\nu$, proving the support assertion. In the surviving case its inner sum is

$$
\frac{\phi(q')}{\phi(b)}
                    \nu(a)\,\tau_b(\bar\nu;-c(t_0)),\qquad
 \tau_b(\bar\nu;c)=\sum_{u\bmod b}^{*}\overline{\nu(u)}e(cu/b).
 \tag{6}
$$

Indeed $a$ is a unit, and substituting $u\mapsto au\bmod b$ in the fiber-reduced sum gives $\nu(a)$ from the barred multiplicative character. Thus the $a$-dependence is exactly one multiplicative character for every eligible pair, at each orientation and each alias. This calculation applies also to imprimitive $\xi,\xi'$ and did not enlarge the actual unit set.

Let $d=\operatorname{cond}(\nu)$. The following bound applies to all additive frequencies $c$, not just primitive ones:

$$
\sum_{c\bmod b}|\tau_b(\bar\nu;c)|
                            \le \tau(b)b\sqrt d .
 \tag{7}
$$

To prove it let $\nu^*$ be the primitive inducing character modulo $d$. Inclusion–exclusion of unit exclusions at primes not dividing $d$ expresses the sum defining $\tau_b$ as the sum of terms

$$
\mu(u)\overline{\nu^*(u)}
       \sum_{x\bmod b/u}\overline{\nu^*(x)} e(cx/(b/u)),
              \qquad u\mid b,\quad (u,d)=1 .
$$

Writing $H_u=b/(ud)$, the additive sum over lifts of each class of $x\bmod d$ vanishes unless $H_u\mid c$. When $H_u\mid c$, its absolute value is $H_u$ times that of a primitive Gauss sum at modulus $d$, hence at most $H_u\sqrt d$. There are $b/H_u$ such $c\bmod b$. The argument includes the trivial conductor $d=1$. This proves (7) after summing the divisors $u$. By (5)–(7) and $b/\phi(b)\ll_\epsilon Q^\epsilon$, the coefficient of $\nu(a)$ in an individual incidence is

$$
O_\epsilon(Q^\epsilon\phi(q')\sqrt d).
 \tag{8}
$$


## 3. Remove the genuine low product conductors

At fixed raw coordinates $z,w$, the $\xi$- and $\xi'$-coefficients in the two actual high progression vectors are $W_\xi(z)/\phi(q')$, $W_{\xi'}(w)/\phi(q')$ after the character basis factors as in R81 (5). In particular auxiliary GRH gives $W_\xi(z)\ll_\epsilon Q^\epsilon\sqrt z$ and the analogous bound for $w$, including imprimitive characters. For a fixed product $\nu$, after $\xi$ is chosen there is just one possible $\xi'=(\nu\circ\pi_{q',b})\bar\xi$; the high restrictions can only remove choices. Hence there are at most $\phi(q')$ eligible pairs. After the two normalizing factors $\phi(q')^{-1}$, (8) bounds the exact coefficient of $\nu(a)$ in their centered product by $O_\epsilon(Q^\epsilon\sqrt{dzw})$. The restrictions are on the actual character expansion of the genuine progression error on both legs.

Now keep product conductors $d\le D_\times$, including $d=1$. By multiplicative character orthogonality on the **complete reduced numerator set**, its joint numerator $\ell^2$ norm is at most

$$
\begin{split}
  &O_\epsilon\!\left(Q^\epsilon \sqrt{\phi(b)}
      \left(\sum_{\substack{d\mid b\\d\le D_\times}}d\phi(d)\right)^{1/2}
               \sqrt{zw}\right)
    \ll_\epsilon Q^\epsilon \sqrt b\,D_\times\sqrt{zw}.
 \end{split}
 \tag{9}
$$

Here a conductor $d$ supplies at most $\phi(d)$ characters, and the number of divisors of $b$ is $Q^{o(1)}$. The $\nu=1$ part is exactly the conjugate diagonal $\xi'=\bar\xi$ in this true finite character expansion. Even nonprincipal product characters of small conductor are accounted for; no relation between the values of the two distinct prime-character errors was assumed.

To pass (9) to the signed field, initially use a common smooth test $\omega$ before choosing the individual numerator detuning, with $K_1=\|\omega\|_\infty+\|\omega'\|_1,\ K_2=\|\omega''\|_1$. With dyads $V\le U$, the common derivative of the true raw profiles on an $I,I'$ entry has $L^1$ bound $\ll b_I b_{I'}[K_1+(QV/k)(K_2+K_1/Q)]$ by [R76 (5)](r76-operator-joint-rational-numerator-variance.md). Restrict the integration to $z,w>A$ **after** the derivative as in R80. The raw supports give $\sqrt{zw}\ll Q\sqrt{VU}$. Minkowski under this common integral and then HS aggregation, with $\sum_I b_I^2\ll1/(QV)$, $\sum_{I'}b_{I'}^2\ll1/(QU)$, give a joint numerator estimate per $k$ of

$$
Q^\epsilon\sqrt b\,D_\times
       \big[K_1+(QV/k)(K_2+K_1/Q)\big].
$$

Summing $k\le4U$ and the finitely signed orientations and dyad pairs gives $Q^\epsilon\sqrt b D_\times M(K_1+QK_2)$ before division by $J$. The same bound holds when only $(2k,b)<G$ is used, because the selection does not depend on the numerator or the common test.

For each $b$ and fixed integer shift $\ell$ about nearest rational centers, apply the shared Taylor weights of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field) to this estimate. The $a$-dependent factors are at most $2^{-n}$ on Taylor term $n$, so they multiply the joint $\ell^2$ estimates of (9) without loss. The phases of absolute value one in the sharp-shell convention can be kept. This does **not** assert that the final field with differing detunings is a multiplicative projection of the already detuned field. Rather, the selected products are assembled with their exact original detunings, using a common test within each Taylor term. The effective $K_1$ is $O(1+|\ell|)$, and $K_2$ is $O(S^{-1}+(1+|\ell|)^2/Q)$. After normalization by $J\asymp Q$, the bound is

$$
Q^\epsilon\sqrt b D_\times
                    \left[\frac M Q(1+|\ell|)^2+\frac M S\right].
 \tag{10}
$$

Squaring and summing over denominator and shift, $\sum_{b\le B}b\ll B^2$, $\sum_{|\ell|\le R+1}(1+|\ell|)^4\ll R_*^5$, yields the $BD_\times$ term of (2). Extra representations of shell indices can only increase the sum of nonnegative squares.

## 4. Remove large common divisors without a product cut

For aliases with $(2k,b)\ge G$, we may bound the **whole** high–high product without expanding into product characters. At each fixed $z,w$, the original joint incidence bound R76 (7) is $b$ times the residue Euclidean norms of the two tested vectors. The actual high projections are orthogonal restrictions of $F(z)$ and $F(w)$, so these norms satisfy the GRH residue bound $O_\epsilon(Q^\epsilon\sqrt z)$ and $O_\epsilon(Q^\epsilon\sqrt w)$. Use the same common derivative, raw support and HS aggregation as in §3. Now the admissible $k$'s are contained in the union of the multiples of $g/(g,2)$ over all $g\mid b,\ g\ge G$. Indeed any such $k$ supplies $g=(2k,b)$. Hence, on $1\le k\le4U$,

$$
\#\{k:(2k,b)\ge G\}\ll_\epsilon Q^\epsilon U/G,
 \qquad
 \sum_{\substack{1\le k\le4U\\(2k,b)\ge G}}\frac1k
                              \ll_\epsilon Q^\epsilon/G .
 \tag{11}
$$

For each divisor $g$ these bounds follow from the count and harmonic sum of multiples, respectively, with at most a factor $2$ from $(g,2)$. The factor $\tau(b)$ and the harmonic logarithm are absorbed by $Q^\epsilon$. The bounds also hold if there are no such aliases.

Thus the estimate before shell normalization is $O_\epsilon(Q^\epsilon bM G^{-1}(K_1+QK_2))$, now for the complete heavy-alias part of the high–high product. Apply the same detuning Taylor argument and normalize. Summing squares over $b,\ell$, with $\sum b^2\ll B^3$, gives the $B^{3/2}/G$ term in (2). This controls all product conductors on the heavy-alias sector, and in particular does not follow from (9).

Together the exact vanished terms, the heavy aliases, and the low products on the other aliases are exactly the part removed by (1). At (3) the first and second terms from $BD_\times$ have powers $-11/4000$, $-15/4000$; the ones from $B^{3/2}/G$ have powers $-7/800$, $-39/4000$. Both errors are smaller than the $Q^{-1/500}$ edge comparison of R81 (4). This proves the stated comparison on the entire packet with the true unweighted normalized Fourier convention and the exact benchmark. It provides no estimate of the residual correlations of high product characters at the remaining aliases.
