# Low alias conductors on the true larger-alias packet

The exact product-character condition forces conjugacy on the prime-to-denominator part of the auxiliary alias modulus. A low-conductor cut there therefore selects two low factors at once, with no mixed terms. Keeping that smaller character count in both the pointwise and conditional progression increment estimates allows deletion on **all** raw regions of the true larger-alias field, including the late–late region.

## 1. Actual selection and conclusion

Use the complete even modulus shell, transported parent profiles $h,f$, separated high-denominator packet $\mathcal C_+(B,R)$, normalization $J^{-1}\sum_m$ with $N=2m$, and common taper of [R85](r85-operator-skew-translation-all-short-aliases.md). Assume original local Dirichlet GRH at the shell targets and auxiliary Dirichlet GRH through $\lceil8MB\rceil+2$, including modulus $1$. Keep the original polynomial parameter ranges, the sharp $z,w>A$ domain and its high character and small common-divisor conditions from [R82](r82-operator-low-product-character-long-quotient.md). Write $R_*=1+R$. Let $Q\le A\le QH/100$ and $A/Q\le K\le4M$.

For each actual larger alias $k>K$ and denominator $b$, put $q=2k$, $q'=qb$, and factor

$$
q=d_b\,r_b,\qquad
 d_b=\prod_{p\mid b}p^{v_p(q)},\qquad
 (r_b,b)=1,\qquad q'=r_b(d_b b).
 \tag{1}
$$

Thus $r_b$ is the full prime-to-$b$ part of $q$, and the last factorization is coprime, even for $q,b$ not coprime. For a character $\xi\bmod q'$, let $\xi_{\perp}\bmod r_b$ be its component in this CRT. For real $D\ge1$, impose the new selection

$$
\operatorname{cond}(\xi_\perp)>D
 \tag{2}
$$

on both true progression vectors, in addition to every existing selection. This is not the R81 low individual conductor on the prime-to-$q$ part of $b$, nor the R82 conductor of the product modulo $b$.

Take either $Z=\mathcal Z_{>K}$, the exact R85 larger-alias field, or the exact [R87](r87-operator-adaptive-raw-minimum-even.md) field

$$
Z=\mathcal Z_{>K}-\mathcal E_{P,K}-\mathcal R^{\rm rem}_{P,K}
 \tag{3}
$$

with $K\ge2P$ and its admissible $H\le P\le M$. Denote by $Z_{>D,\perp}$ this same field with (2) applied. The two fields have the same raw masks, original signs $+,+,-$, exact detunings and outer phases. Then

$$
\left(\sum_{j\in\mathcal C_+(B,R)}
       \|Z(j)-Z_{>D,\perp}(j)\|_{\rm HS}^2\right)^{1/2}
 \ll_{\Gamma,\Theta,\epsilon} Q^\epsilon B^{3/2}D
       \left[\frac{R_*^{3/2}+R_*^{5/2}}Q+\frac{R_*^{1/2}}S\right].
 \tag{4}
$$

The same bound holds after fixed orthogonal spatial compression or restriction to any subset of the packet. When $r_b\le D$, the entire eligible larger alias at this denominator is deleted. This can happen even for large $q$ with small $(q,b)$, since $d_b$ contains **all** exponents in $q$ of primes dividing $b$, not just those in $(q,b)$.

Keep the R85–R87 example $H=Q^{2/5}, M=Q^{3/5}, A=Q^{6/5}, B=\lfloor Q^{39/100}\rfloor, R=\lfloor Q^{1/400}\rfloor,S=Q^{249/250}$, and the same $W_V,D_\times,G$. With $D=K=\lfloor Q^{81/200}\rfloor$, $P=K/2$ in (3), the rate in (4) is $O_\epsilon(Q^{-3/800+\epsilon})$. The sharp parent fields $\widehat T,\widehat P$ consequently have the same inherited packet comparison $O_\epsilon(Q^{-1/500+\epsilon})$, now to the new retained field from (3). The bound does not estimate high $r_b$-conductor covariance, all Fourier modes, a prescribed modulus, or weak S. It is separate from the structural Taylor rank of [R88](r88-operator-early-profile-taylor-rank.md): no spatial projection is needed in (4), and there is no early-profile restriction.

## 2. Exact forcing of a pair and the smaller progression norms

The exact R82 identity kills every character pair $\xi,\xi'$ whose product does not factor through reduction to $b$. In the CRT (1), the reduction to $b$ is independent of the unit modulo $r_b$. Every surviving pair therefore obeys

$$
\xi_\perp'=\overline{\xi_\perp}.
 \tag{5}
$$

In particular the two conductors at issue are identical. The two existing high individual selections and the further even or odd projections, where used in (3), are diagonal on the same character basis. The R82 high product-conductor projector is on the reduced numerator family. Neither retaining that projector nor the common-divisor cut changes (5).

Let $F^{\rm lo}(z)$ be the true high residue vector projected further to $\operatorname{cond}(\xi_\perp)\le D$ at $q'$. By (5), the difference between a given field and its new selection is exactly the field with the **two** $F^{\rm lo}$ legs, with the inherited masks on them. Each mixed low/high pair has coefficient zero before the actual distinct fractional detunings. Thus no estimate of a mixed high/low term is being presumed. When $r_b=1$ use its unique conductor-one character in the same convention.

Put

$$
\lambda_{k,b}=\min(1,D/r_b).
$$

The number of characters of $r_b$ with conductor at most $D$ is at most $\sum_{d\mid r_b,\ d\le D}\phi(d)\le D\tau(r_b)$, and also at most $\phi(r_b)$. Allowing all characters of $d_b b$ only enlarges the count of low characters selected in $F^{\rm lo}$. Hence the resulting fraction among all characters of $q'$ is $O_\epsilon(Q^\epsilon\lambda_{k,b})$, using $\tau(r_b)\ll_\epsilon Q^\epsilon$ and $r_b/\phi(r_b)\ll_\epsilon Q^\epsilon$, and decreasing the intermediate $\epsilon$'s if needed.

For the individual centered character sums $W_\xi(z)=\psi(z,\xi)-z\mathbf1_{\xi=\xi_{\rm princ}}$, pointwise auxiliary GRH gives $|W_\xi(z)|\ll_\epsilon Q^\epsilon\sqrt z$ uniformly in the actual raw ranges. Also the proof of [R83 (7)](r83-operator-small-alias-progression-increments.md#3-a-conditional-short-progression-increment-on-the-actual-affine-difference) bounds **each** character before residue Parseval. In its raw polynomial ranges it gives $\int_X^{2X}|W_\xi(z+h)-W_\xi(z)|^2 dz\ll_\epsilon Q^\epsilon X|h|$ for $1\le |h|\le X/4$. Indeed the zero-bin argument uses the primitive inducing character's local upper zero count uniformly, and its lower-order imprimitive prime-power corrections and principal centering are already included. The negative shift is covered by translating the real interval, as there.

Now use the exact normalization $F_r(z)=\phi(q')^{-1}\sum_\xi\overline{\xi(r)}W_\xi(z)$ on the unit set. Finite character Parseval on the reduced class set, counting only the selected characters, yields

$$
\begin{split}
 \|F^{\rm lo}(z)\|_2^2 &\ll_\epsilon Q^\epsilon\lambda_{k,b}\,z,\\
 \int_X^{2X}\|F^{\rm lo}(z+h)-F^{\rm lo}(z)\|_2^2\,dz
       &\ll_\epsilon Q^\epsilon\lambda_{k,b}\,X|h|
                         \qquad(1\le |h|\le X/4).
 \end{split}
 \tag{6}
$$

The same estimates hold for the parity projections of this vector. In particular the saving in the integrated bound is obtained from the individual explicit formula estimates, not inferred by projecting a bound already summed over all characters.

## 3. Per-alias weighted estimates and the exact masks

Use a common scalar test $\omega\in C_c^2((Q,2Q))$ before any primitive-numerator-specific rounding. Write

$$
K_1=\|\omega\|_\infty+\|\omega'\|_1,\qquad
 K'_2=\|\omega''\|_1+K_1/Q.
$$

We first estimate the low part of the unmodified $\mathcal Z_{>K}$. At each $k>K$, after all spatial dyad pairs, its common-test cost in joint numerator HS norm is

$$
O_\epsilon\!\left(
                Q^\epsilon b\lambda_{k,b}[K_1+QK'_2]\right).
 \tag{7}
$$

Here are the separate checks that the fixed-alias estimates of R84–R85 apply with this factor. All have $k>K\ge A/Q$, so the exceptional bookkeeping for $k<A/Q$ is not needed.

* For the two differences take the R84 cutoff $\rho_k=A+8kQ$ and at a pair $V\le U$ write $X=QV,\ Y=QU$. On the good pairs $4\rho_k\le X$, the actual sharp-to-smooth cutoff change costs the right side of [R84 (6)](r84-operator-short-cosine-and-sum-aliases.md#2-common-test-and-an-adaptive-raw-cutoff) times $\lambda_{k,b}$: the two pointwise vector bounds on the unchanged arithmetic each contribute $\sqrt{\lambda_{k,b}}$ by (6). Since $\rho_k\le9kQ$, the bracket is $O(K_1+QK'_2)$. On other pairs $X<4\rho_k\le36kQ$, use the R84 unmodified derivative bound; $X/k\le36Q$ gives the same cost, again with both pointwise savings. These estimates use only joint incidence and genuine derivative envelopes.
* On a good smoothly cut pair, for the symmetric difference the two exact marginal cancellations from [R84 §3](r84-operator-short-cosine-and-sum-aliases.md#3-two-exact-marginal-cancellations-on-the-symmetric-difference) still use the **same** $F^{\rm lo}$ at both coordinates, fixed at $q',b,k$. For the fourth derivative term, at fixed $t$ the shift is $h=\pm kt$ and has $|h|\le\rho_k/4$. The raw squared increment norm is bounded by $O_\epsilon(Q^\epsilon\lambda_{k,b} X |h|)$ by (6) on its raw dyads, exactly as in R84 (9). After the $w\mapsto t$ change one factor $1/k$ remains, so $|h|/k\le2Q$; the parent square sums cost $X/\sqrt{XY}\le1$. The first three terms use the pointwise bounds and $w\asymp z$, giving the $K_1$ part with the same $\lambda_{k,b}$.
* For the skew part on a good pair, keep the same raw dyad interval restriction of $F^{\rm lo}$ on both legs in the proof of [R85 (3)–(6)](r85-operator-skew-translation-all-short-aliases.md#3-a-weighted-raw-translation-estimate-for-the-skew-incidence). The interval endpoints are paid with the pointwise square bound in (6), and the interior translations use its second bound. Thus both estimates (3) of R85 have the common factor $\lambda_{k,b}$. The Fourier first moment with the actual odd translation multiplier, the loss from undoing one endpoint, and the fixed-$t$ BV weighting are all linear in these squared estimates. The raw pairing bound (6) of R85 therefore has the same extra factor. The fourth derivative then costs $O_\epsilon(Q^\epsilon b\lambda_{k,b}Q K'_2)$ after HS just as there, and the first three cost $O_\epsilon(Q^\epsilon b\lambda_{k,b}K_1)$. No covariance between different aliases is used.
* For the sum orientation, the proof of [R84 (12)](r84-operator-short-cosine-and-sum-aliases.md#4-single-increments-and-the-sum-orientation) gives per alias $O_\epsilon(Q^\epsilon b\min(1,k/V)[K_1+QK'_2])$ on each pair. The two raw vector bounds used there each bring $\sqrt{\lambda_{k,b}}$; its early strips use just pointwise bounds, while on other pairs the shorter-support $QV/k$ is $O(Q)$. The original negative sign and the exact raw restrictions remain in the field.

The $b$ joint numerator factor in all of these is [R76 (7)](r76-operator-joint-rational-numerator-variance.md#2-additive-parseval-in-the-exact-incidence-and-the-continuous-term). The triangle over only logarithmically many physical dyad pairs proves (7), with the usual $Q^\epsilon$ allowance for logarithms. This is a fixed-alias argument before Taylor detuning, independent of how many eligible larger aliases there are.

For the reduced input (3), decompose its low part by linearity as the low part just estimated minus the low parts of $\mathcal E_{P,K}$ and $\mathcal R^{\rm rem}_{P,K}$. The estimates [R86 (5)–(6)](r86-operator-long-alias-short-leg-even.md#3-bound-the-integrated-difference-at-a-fixed-alias) and [R87 (7)–(8)](r87-operator-adaptive-raw-minimum-even.md#3-weighted-derivative-bounds) apply to those two latter pieces with $F^{\rm lo}$ replacing $F$; their exact reflection and parity identities still hold, and their vector estimates are pointwise. At each $k$ their combined cost after spatial pairs is

$$
O_\epsilon\!\left(Q^\epsilon b\lambda_{k,b}
                 \frac{QP}{k}(E_\infty+E_1)\right),
 \quad E_\infty=\|\omega'\|_\infty+\|\omega\|_\infty/Q,\quad
 E_1=\|\omega''\|_1+\|\omega'\|_1/Q+\|\omega\|_1/Q^2 .
 \tag{8}
$$

This step avoids applying an unmasked marginal identity to the raw masks of R87. No overlap is subtracted twice, since $\mathcal R^{\rm rem}_{P,K}$ is already the exact R86-complement deletion. The reordering of projections is legitimate by (5) and commutation on each affected leg.

## 4. Count the actual aliases, then restore the Fourier packet

At a fixed $b$, the number of integers $d\le8M$ supported on primes dividing $b$ is $O_\epsilon(Q^\epsilon)$. Indeed for fixed small $\delta>0$ it is at most $(8M)^\delta\prod_{p\mid b}(1-p^{-\delta})^{-1}$. For any fixed $\eta>0$ the product is $O_{\delta,\eta}(b^\eta)$: for all sufficiently large primes each factor is at most $p^\eta$, and finitely many small primes contribute a fixed constant. Choose the two exponents small in the original polynomial ranges. Grouping $q=2k\le8M$ by such $d_b$ gives

$$
\sum_{K<k\le4M}\lambda_{k,b}
 \le \sum_{\substack{d\le8M\\p\mid d\Rightarrow p\mid b}}
        \sum_{r\le8M/d}\min(1,D/r)
 \ll_\epsilon Q^\epsilon D .
 \tag{9}
$$

The innermost sum is $O(D(1+\log(8M)))$; the omitted parity, coprimality and common-divisor restrictions can only lower it. Also $\sum_{K<k\le4M}\lambda_{k,b}/k\ll_\epsilon Q^\epsilon D/K$. This is a count over true alias possibilities, not orthogonality of sums indexed by $k$.

From (7) and (9) the common-test cost is $O_\epsilon(Q^\epsilon bD[K_1+QK'_2])$. For (3), the extra (8) sums to at most $O_\epsilon(Q^\epsilon bQD(E_\infty+E_1))$, since $P\le K/2$. Restore the original common Taylor tests of [R77 (7)](r77-operator-common-shell-rational-packets.md#3-the-true-central-tapered-field). The effective $K_1$ is $O(1+|\ell|)$ for integer offset $\ell$; the effective $K'_2,E_\infty,E_1$ are all $O(S^{-1}+(1+|\ell|)^2/Q)$, including the taper derivative bound of R86 for $E_\infty$. The true fractional coefficients and exterior phase are applied exactly after each common test. Divide by $J\asymp Q$ and square-sum over $b$ and $|\ell|\le R+1$ as in R85. The denominator square sum is $O(B^3)$, and the three offset factors are $O(R_*^{3/2}),O(R_*^{5/2}),O(R_*^{1/2})$ respectively after taking square roots. This proves (4) on the genuine packet, for either input. The example exponents are $-1/160,-3/800,-19/4000$. All preexisting comparisons to the sharp field and its benchmark are unchanged.
