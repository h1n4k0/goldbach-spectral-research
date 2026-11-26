# An unconditional inverse-logarithmic critical-shell bound with logarithmic radical and divisor width

Let $N$ be even, $X=\sqrt N$, $L=\log N$, and $e(z)=e^{2\pi iz}$. Use the actual complementary polynomial of the [bounded-radical argument](weak-s-type-ii-critical-prime-bounded-radical-davenport-transport.md): $N/2\le y\le9N/16$, the hard cofactor interval $I_k$ includes the restriction $k>t\ge N^{.49999}$, and

$$
 D_m=\mathbf1_{N-y\le m<N/2}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                     (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_m D_m e(\alpha m).
$$

Let $\mathcal Q=[.8X,.9X]\cap\mathbb P$ and

$$
 \mathcal E_N(D)=\int_{-1/(10N)}^{1/(10N)}
            \sum_{q\in\mathcal Q}\sum_{1\le a<q}|D(a/q+\beta)|^2\,d\beta .
$$

**Theorem.** For every fixed $B,\gamma\ge0$ and $C>1$, assume only

$$
           \operatorname{rad}N\le L^B,\qquad I_d\subset[X,CXL^\gamma].
 \tag{1}
$$

Then unconditionally, uniformly in the actual hard intervals and other cuts above,

$$
                    \mathcal E_N(D)\ll_{B,\gamma,C}\frac{N}{L}.
 \tag{2}
$$

This enlarges both bounded axes of the earlier unconditional inverse-logarithmic bound. It asserts neither an energy limit for varying cuts nor a bound for a signed prime pairing, any other shell, or the full operator. The absence of GRH here relies on holding $B,\gamma$ fixed; this does not prove the result with unrestricted radical or polynomial divisor width.

## 1. The same arithmetic and smoothing, with the wider logarithmic cutoff

Use $\delta=L^{-2}$ for the true physical and cofactor inward smoothing, and $T=L^{16}$ for the squarefree inclusion cutoff, as in [the original unconditional approximation estimates](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#1-actual-transfers-at-the-smaller-smoothing-width). These estimates apply here: for fixed $B,\gamma,C$ and all large $N$, the logarithmic width is inside the admitted polynomial width, and we can still intersect $I_d$ with $[X,N/(2t))$ without removing any original terms. The ordinary squared approximation error to $D^\dagger$ is $O(NL^{-2})$ and $\|D^\dagger\|_2^2\ll N$. Every $h\mid R=\operatorname{rad}N$ is retained in the original short inclusion, since $h\le L^B<\exp(C_0(1+\log L)^2)$ for sufficiently large $N$. In particular this is not a truncated-prime mask or an omitted-radical estimate.

The actual split is $l\le T$ squarefree, $(l,N)=1$, $s=(l,d)\mid l$, $d=su$ with $(u,lN)=1$, and $k=(l^2h/s)v$ with $v>0$. The signs are $\mu(l)\mu(s)\mu(h)\mu(u)$. Decompose the true $d$ interval into $O_\gamma(1+\log L)$ dyads (with constants also depending on $C$), with scales $A_i=\lambda_i X$ and $1\le\lambda_i\ll_C L^\gamma$. As before put $K_i=N/A_i$, $U_i=A_i/s$, and let

$$
             \xi=\xi_{q,i,h}=\frac{K_i s}{q l^2h},\qquad
             \Lambda=32+B+\gamma .
$$

Then

$$
           L^{-\Lambda}\ll_C\xi\ll_C1,\qquad
           U_i\le CXL^\gamma,\qquad
           U_i\xi=\frac{N}{q l^2h}\ll X .
 \tag{3}
$$

All $l,h$ are units at each shell prime for large $N$. There are at most $O_{B,\gamma,C}(L^{33+B})$ choices of $(l,s,h,i)$, using $s\mid l$, $h\mid R\le L^B$, and the dyad count; this intentionally crude logarithmic bound is sufficient.

Let $G_\beta$, $a_{i,\tau}(u)$ and $f_{i,\tau}$ be the time weight, exact long label and short weight of [the bounded-radical cutoff, §1](weak-s-type-ii-critical-prime-bounded-radical-davenport-transport.md#1-genuine-approximation-and-a-logarithmic-dual-cutoff), still with the same inward smoothing, common actual cofactor cutoff and fixed normalized dyad bump. In particular the short estimates are uniform here because the normalized support remains fixed independently of $i$. With $Y_\tau=1+L+|\tau|$ they give

$$
 \begin{split}
 |\widehat f_{i,\tau}(z)|&\ll \min(1,(Y_\tau/|z|)^2),&
 \|f_{i,\tau}^{(r)}\|_1&\ll_r(1+L^2+|\tau|)^r,\\
 \|\widehat G_\beta\|_1&\ll 1+\log L,&
 |\widehat G_\beta(\tau)|&\ll_r L^{2r-2}|\tau|^{-r}\quad(r\ge2).
 \end{split}
 \tag{4}
$$

At fixed $l,s,h,i,\tau$ the long character sum $U_\chi=\sum_u a_{i,\tau}(u)\chi(u)$ now satisfies

$$
       \sum_{\chi\bmod q}|U_\chi|^2
          \ll q (1+U_i/q) U_i \ll_{C,\gamma} qXL^{2\gamma}.
 \tag{5}
$$

Indeed its hard long support is inside $[U_i,2U_i)$, with at most $O(1+U_i/q)$ hits in a residue. For any uniform bound $S$ on the short Poisson factor after extracting the Gauss factor of magnitude $\sqrt q$, (5) gives modular squared norm $O_{C,\gamma}(N^2L^{2\gamma}S^2)$ over $q,\chi\ne\chi_0$. This uses $\sum_q q^2\ll X^3$ and allows the true long factor to vanish at residue zero without adding a term.

For a prescribed fixed log-error exponent, take $|\tau|\le L^4$ and $0<|j|\le J_*=L^P$, with $P$ a sufficiently large fixed exponent in terms of $B,\gamma$ and that accuracy. First for the full short sum use $\xi\sum_{j\ne0}|\widehat f_{i,\tau}(j\xi)|\ll Y_\tau$ as in the preceding argument. With the high-order $\widehat G_\beta$ bound in (4) this removes $|\tau|>L^4$ at arbitrarily fixed logarithmic accuracy, after multiplication by $NL^\gamma$ from (5) and the logarithmic exterior count. On retained $\tau$, the omitted dual tail satisfies

$$
     \xi\sum_{|j|>J_*}|\widehat f_{i,\tau}(j\xi)|
        \ll_r L^{4r}(J_*\xi)^{1-r},
        \qquad J_*\xi\gg_C L^{P-\Lambda}.
 \tag{6}
$$

For instance any $P>\Lambda+6$ admits an $r$ large enough to beat all fixed log losses in this modular cutoff. We will take $P$ larger still for the rational tail below. The actual sampled nonprincipal norm error, uniform in $\beta$, is $O_A(NL^{-A})$ for each prescribed $A$, by (5), (6), the finite exterior label count, and integration against $\widehat G_\beta$. This accounts for the nontrivial long residue occupancy before discarding the modular dual tail. All retained nonzero $j$ are units modulo $q$.

## 2. Complete coherently and remove the nonzero modular determinants

Insert the actual $\chi(l^2)$ multiplier into the residue $l^2hu/j\bmod q$ within the joint array, preserving the $l,s,h$ signs and the independent frequency integrals in its square. This is the [coherent positive completion](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#1-complete-the-square-only-after-adding-the-square-labels), so the completed norm has weights $q(q-1)$ and exactly

$$
                    l_1^2h_1j'u-l_2^2h_2ju'=bq .
 \tag{7}
$$

For the upper bound it is harmless to add the artificial principal and residue-zero squares in the completion. They are not replacements for the true additive constant modes.

Write $B_0=lR\le L^{16+B}$. The unconditional masked Davenport estimate of [the preceding determinant argument, §2](weak-s-type-ii-critical-prime-bounded-radical-davenport-transport.md#2-davenport-cancellation-in-the-exact-completed-determinant) is uniform at this mask size. Explicitly, convolve $\mu$ with the indicator of integers whose prime factors divide $B_0$ to impose the exact coprimality. For convolution labels $r\le\sqrt{U_i}$ use the original Davenport bound at the rescaled hard endpoints, whose logarithms are comparable to $L$ since $X/L^{16}\ll U_i\ll XL^\gamma$. The reciprocal factor costs at most $L^{O_B(1)}$. For $r>\sqrt{U_i}$ the trivial count is at most

$$
      U_i^{7/8}\prod_{p\mid B_0}(1-p^{-3/4})^{-1}
                         \ll_B U_i^{7/8}L^{O_B(1)}
$$

by the same Rankin exponent $1/4$. This is power-small relative to $U_i$, uniformly over the mask. Abel for the actual twist $e(\tau\log(su/A_i))$ costs $O(1+|\tau|)$. Thus the signed long additive transform has sup norm $O_D(U_iL^{-D})$ for each fixed $D$, on retained $\tau$ and the true cut, without GRH.

For fixed labels and $b\ne0$, two long Fourier factors at the nonzero integral dilations in (7) pair with the sum over distinct $bq$; the latter has $L^2$ norm $\ll X^2\sqrt{\#\mathcal Q}$ because its weights, including both short transforms and meshes and the completion factor, are $O(X^2)$. Use the masked sup norm for the first long factor and the ordinary $L^2$ norm $O(\sqrt{U_{i'}})$ for the second. This is $O_D(N^2L^{3\gamma/2-D})$ using (3) and $\#\mathcal Q\ll X$. The determinant range has $|b|\ll_C L^{32+B+\gamma+P}$. With $j,j'$ of size at most $L^P$, both exterior label counts from §1, and the absolute time integrals in (4), every remaining cost is a fixed power of $L$. Choosing $D$ sufficiently large gives $O_A(N^2L^{-A})$ for all nonzero determinants at any prescribed log accuracy, uniformly in $\beta$. In particular no power-size index range is being paid for by Davenport cancellation.

## 3. The rational restoration and the genuine full energy

For zero determinant the coordinate is literally $\rho=j/(l^2hu)\ne0$. We justify the smaller cutoff also in this rational space, where the norm is weighted by $q(q-1)$. At fixed $l,s,h,i,\tau$, two colliding coordinates have $u=r z,\ u'=r'z$ and $j=d r,\ j'=d r'$ with $(r,r')=1$ and $d\ne0$. In a range $r\asymp V$, also $r'\asymp V$ by the true dyad, so $O(V^2)$ pairs and $O(U_i/V)$ positive $z$ occur. The elementary fourth-power sum with the envelopes in (4) is $O(Y_\tau/(V\xi))$, after summing $d$, or $O(Y_\tau^4/(V\xi F^3))$ if the two arguments have magnitude at least $F$. Each estimate remains an upper bound when the resulting lower bound on $|d|$ is below one. There are $O(L)$ dyads in $V$. Including $\xi^2$ and (3) and summing the $q(q-1)$ weights, the full squared norm for these fixed labels is therefore at most $O(N^2L Y_\tau)$.

For the omitted-$j$ vector, on retained $|\tau|\le L^4$ both arms of its own squared norm have $|j|,|j'|>J_*$. By (3) we may take $F=L^{P-\Lambda-1}$ in the second envelope sum just described. The resulting squared norm is $O(N^2L Y_\tau^4/F^3)$. Increasing the fixed $P$ gives arbitrary fixed log-accuracy even after the polylogarithmic exterior count. The first envelope sum and (4) do the same for the $|\tau|>L^4$ rational tail. The triangle inequality across $l,s,h,i$ is used only for these negligible tails. The full crude rational norm is polynomial in $L$ in units of $N$, so the resulting change in the squared norm at fixed $\beta$ is $O_A(N^2L^{-A})$ at the chosen accuracy.

Fourier inversion with the dyad-normalized bump equal to one on the fixed physical weight gives the exact rational term with sign $\mu(l)\mu(s)\mu(h)\mu(u)$ and coefficient

$$
       \frac{N}{q l^2 h u}\int\Omega(x)e(\beta Nx)
                 w(Nx/(su))e(-\rho Nx/q)\,dx .
$$

Only the rational diagonal has been extended; no new indices are inserted in (7). All physical dyads reassemble to the original single hard $I_d$, and every $h\mid R$ was already included. The [exact paired-label rational bound](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#2-factor-the-common-rational-denominator-before-the-square-label-sum) is uniform in the original larger polynomial width and full unit mask. It bounds this squared norm by $O(N^2/L)$ before the $\beta$ integral, with the $h$ signs grouped before estimating the common and exclusive square-label prime factors. It is unconditional, and no factor depending on $R$ or the number of true dyads is incurred in the main rational norm.

Multiplicative Parseval gives the genuine nonconstant additive part with a bounded extra $q/(q-1)$ factor per positive character norm. By (7), the new off-diagonal bound and the rational comparison, its $\beta$ integral is $O(N/L)$. The [actual constant-mode estimates](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#4-a-signed-real-sumintegral-for-the-actual-q-nonunits) give $O(N/L)$ for the original principal and real $q$-nonunit modes of $D^\dagger$ too. Their proof was unconditional and uniform on the original width, and deleting the short-inclusion tail here is unnecessary because all $h\mid R$ are retained. Finally the true arcs are disjoint, so ordinary Parseval controls the approximation error $O(NL^{-2})$ in the squared shell norm when returning to the literal $D$. This proves (2).
