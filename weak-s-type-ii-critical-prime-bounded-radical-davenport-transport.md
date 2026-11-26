# Unconditional transport to the coherent critical-shell energy at bounded radical

Let $N$ be even, $X=\sqrt N$, $L=\log N$, and $e(z)=e^{2\pi i z}$. Use the actual complementary polynomial and critical-prime shell of the [coherent inverse-logarithmic upper bound](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md): $N/2\le y\le9N/16$, $I_k$ is a hard interval with $k>t\ge N^{.49999}$, and

$$
 D_m=\mathbf1_{N-y\le m<N/2}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                       (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad
 D(\alpha)=\sum_m D_m e(\alpha m).
$$

Here assume that $I_d\subset[X,CX]$ for fixed $C>1$ and $R=\operatorname{rad}N\le R_0$ for fixed $R_0$. Write $\mathcal Q=[.8X,.9X]\cap\mathbb P$ and let $\mathcal E_N(D)$ and $\mathcal E_N^0(D)$ be the squared energy over $a/q+\beta$, $q\in\mathcal Q$, $1\le a<q$, $|\beta|\le1/(10N)$, respectively before and after orthogonal projection off the constant in each nonzero-numerator group.

**Theorem.** Unconditionally, uniformly in these hard cuts,

$$
                           \mathcal E_N(D)\ll_{C,R_0} N/L.
 \tag{1}
$$

In particular, on the exact powers-of-two cuts of [the limiting-energy example](weak-s-type-ii-critical-prime-limiting-complementary-energy-grh.md), both actual energies satisfy

$$
               \mathcal E_N(D)\sim C_{\rm ex}N/L,\qquad
               \mathcal E_N^0(D)\sim C_{\rm ex}N/L
 \tag{2}
$$

**without GRH**, with the same finite positive integral constant as there. This is only the stated shell and bounded-radical transport, with the limit asserted at the indicated fixed witness. No signed lower bound, other shells, or Hypothesis S result follows.

## 1. Genuine approximation and a logarithmic dual cutoff

Use the inward smoothing $\delta=L^{-2}$, the physical weight $\Omega(m/N)$, the log-cofactor weight $w(k)$, and the square truncation $T=L^{16}$ of [the preceding unconditional transfer estimates](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#1-actual-transfers-at-the-smaller-smoothing-width). Their squared ordinary error is $O(NL^{-2})$ and the approximant $D^\dagger$ has squared ordinary norm $O(N)$. Since $R$ is bounded, every short inclusion label $h\mid R$ is already included for sufficiently large $N$ in the permitted cutoff, and the unit condition on $d$ is exact. Split the approximate coefficient with $l\le T$ squarefree, $(l,N)=1$, $s=(l,d)\mid l$, $d=su$, $(u,lN)=1$, and $k=(l^2h/s)v$, $v>0$. Its scalar signs are $\mu(l)\mu(s)\mu(h)\mu(u)$. Partition the genuine $d$ interval into its $O_C(1)$ dyadic pieces $I_i$ with scale $A_i\asymp_C X$, and put

$$
 K_i=N/A_i,\qquad U_i=A_i/s,\qquad x_{q,i}=K_i s/(ql^2),\qquad
 \xi_{q,i,h}=x_{q,i}/h .
$$

For retained labels, $\xi_{q,i,h}\gg_{C,R_0}L^{-32}$, $\xi_{q,i,h}\ll_C1$ and $U_i\xi_{q,i,h}\asymp X/(l^2h)$. As in [the exact product-frequency construction](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#2-integrate-in-the-complete-square-and-dispatch-its-off-diagonal), take

$$
 \begin{split}
 G_\beta(z)&=\Omega(e^z)e(\beta Ne^z),\\
 a_{i,\tau}(u)&=\mu(u)\mathbf1_{su\in I_i}\mathbf1_{(u,lN)=1}e(\tau\log(su/A_i)),\\
 f_{i,\tau}(z)&=w_i(z)e(\tau\log z).
 \end{split}
$$

Here $w_i$ is the normalized short weight with its fixed dyad bump, equal to the genuine normalized cofactor weight on the physical support. The established Fourier envelopes at this smoothing width are

$$
 \begin{split}
 |\widehat G_\beta(\tau)|
   &\ll\min(1,|\tau|^{-1},L^2|\tau|^{-2}),
   &|\widehat G_\beta(\tau)|&\ll_r L^{2r-2}|\tau|^{-r}\quad(r\ge2),\\
 |\widehat f_{i,\tau}(z)|
   &\ll\min(1,(Y_\tau/|z|)^2),\qquad Y_\tau=1+L+|\tau|,
   &\|f_{i,\tau}^{(r)}\|_1&\ll_r(1+L^2+|\tau|)^r .
 \end{split}
 \tag{3}
$$

In particular $\|\widehat G_\beta\|_1\ll 1+\log L$, the bounds are uniform in the actual $\beta$ range, and

$$
        \xi\sum_{j\ne0}|\widehat f_{i,\tau}(j\xi)|\ll Y_\tau
 \tag{4}
$$

for every $\xi>0$, by splitting at $|j|\asymp Y_\tau/\xi$. We retain $|\tau|\le L^4$ and now **take $0<|j|\le J_*=L^P$** with a sufficiently large fixed exponent $P$. Its size can be chosen for any specified fixed logarithmic accuracy in the steps below. This is the change that allows the unconditional nonzero-determinant argument: a fixed power cutoff in $N$ would not be paid for by Davenport's estimate.

To justify this cutoff in the **actual modular vector**, use progression Poisson for each nonprincipal character $\chi\bmod q$. At fixed $l,s,h,i,\tau$, the two factors, in modulus after extracting the common Gauss factor of magnitude $\sqrt q$, are the long transform $U_\chi=\sum_u a_{i,\tau}(u)\chi(u)$ and a short sum bounded by the left hand side of (4) (or its discarded tail). A nonzero residue has $O_C(1)$ possible long labels since $u\ll_C X$ and $q\asymp X$. The multiplicative Parseval bound is

$$
                     \sum_{\chi\bmod q}|U_\chi|^2\ll_C qU_i .
 \tag{5}
$$

It follows by Cauchy within each residue and does not require estimating the added principal by Poisson. Zero long residues have character value zero. Thus a uniform short bound $S$ gives squared norm over $(q,\chi\ne\chi_0)$ at most $O_C(N^2 S^2)$, since $U_i\ll_C X$ and $\sum_q q^2\ll X^3$. Now use (4) for all $j$ and the high-order bound on $\widehat G_\beta$ to delete the part $|\tau|>L^4$ at cost $O_B(NL^{-B})$ in norm for any fixed $B$, even after the logarithmic number of outer labels. On retained $\tau$, integration by parts in $f$ to order $r\ge2$ gives

$$
 \xi\sum_{|j|>J_*}|\widehat f_{i,\tau}(j\xi)|
       \ll_r L^{4r}(J_*\xi)^{1-r},
       \qquad \xi=\xi_{q,i,h}.
 \tag{6}
$$

Here $J_*\xi\gg L^{P-32}$. Taking $P$ and the fixed derivative order large enough makes (6) as small a fixed inverse log as needed. Apply (5) again, then integrate in $\tau$ and sum the outer labels in norm. This preserves an $O_B(NL^{-B})$ norm error. In particular this logarithmic cutoff was justified using actual residue occupancy and Parseval, not by replacing a polynomial-size trivial bound in the earlier power cutoff argument. All retained $l,h,j$ are units modulo $q$ for sufficiently large $N$.

## 2. Davenport cancellation in the exact completed determinant

The uniform unconditional estimate we use is [Davenport's additive Möbius bound](https://academic.oup.com/qjmath/article-abstract/os-8/1/313/1564796), in the form of [He–Huang (1.2), p. 1](https://www.impan.pl/shop/en/publication/transaction/download/product/91740?download.pdf=#page=1):

$$
      \sup_{\theta\in\mathbb R}\left|\sum_{n\le V}\mu(n)e(n\theta)\right|
                          \ll_B V(\log V)^{-B}
 \tag{7}
$$

for each fixed $B>0$ and $V\ge2$. The needed consequences may have ineffective constants. We explain the exact mask and twist reduction as both appear inside the determinant. Write $B_0=lR$; the multiplicative identity

$$
     \mu(n)\mathbf1_{(n,B_0)=1}
          =(\mu*1_{\{r:\,p\mid r\Rightarrow p\mid B_0\}})(n)
 \tag{8}
$$

is checked at each prime. For prefixes ending on the original hard interval at scale $U_i$, split the smooth label $r$ in (8) at $\sqrt{U_i}$. On the small side apply (7) to the rescaled endpoints (their logarithms are $\asymp L$), at reciprocal cost $\prod_{p\mid B_0}(1-1/p)^{-1}=L^{O(1)}$. Endpoint differences give the same bound on hard subintervals within $[U_i,2U_i)$, with strict endpoints represented by the appropriate integer prefixes. On the large side, direct counting and Rankin at exponent $1/4$ give

$$
 U_i\sum_{\substack{r>\sqrt{U_i}\\p\mid r\Rightarrow p\mid B_0}}\frac1r
        \le U_i^{7/8}\prod_{p\mid B_0}(1-p^{-3/4})^{-1}
        \le U_i^{7/8} L^{O(1)},
$$

since $B_0\le R_0 T$. Abel summation against $e(\tau\log(su/A_i))$ costs $O(1+|\tau|)$ on the dyad. Consequently for each fixed $D>0$, uniformly over all the actual retained labels and $|\tau|\le L^4$,

$$
            \|A_{i,\tau}\|_\infty\ll_{C,R_0,D} U_i L^{-D},
       \qquad A_{i,\tau}(\theta)=\sum_u a_{i,\tau}(u)e(u\theta).
 \tag{9}
$$

Exactly as in [the coherent construction, §1](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#1-complete-the-square-only-after-adding-the-square-labels), insert the $\chi(l^2)$ factor into the common residue $v=l^2 h u/j\bmod q$ before squaring, keeping the true signs $\mu(l)\mu(s)\mu(h)$ and the time integral. Denote the resulting finite array by $\mathcal S_q(v)$, with mesh factor $\xi_{q,i,h}$. When its positively completed norm $\sum_q q(q-1)\sum_{v\bmod q}|\mathcal S_q(v)|^2$ is expanded, its literal relation is

$$
                    l_1^2h_1 j'u-l_2^2h_2 j u'=bq .
 \tag{10}
$$

Fix the two outer label sets, $j,j',b$ and the independent $\tau,\tau'$. If $b\ne0$, the integral imposing (10) is the product of $A_{i,\tau}$ and the conjugate $A_{i',\tau'}$ at the corresponding nonzero integer dilations, and the Fourier polynomial with frequencies $bq$ and weights $\omega_q=O(X^2)$. These weights include the Fourier short factors and $q(q-1)$; they have the required bound by (3) and $\xi\ll1$. The $bq$ frequencies are distinct for fixed $b\ne0$, so the latter polynomial has norm $O(X^2\sqrt{\#\mathcal Q})$. One other factor has $L^2$ norm $O(\sqrt{U_{i'}})$ by integer dilation and Parseval. Apply (9) to the remaining factor. Since $U_i,U_{i'}\ll_C X$ and $\#\mathcal Q\ll X$, the product is $O_{C,R_0,D}(N^2 L^{-D})$. The number of pairs and determinant labels, including $|b|\ll_{C,R_0} T^2 L^P$, is bounded by a fixed power of $L$, because of the logarithmic dual cutoff and bounded $h$ labels. The two $\widehat G_\beta$ integrals cost another fixed logarithmic power. Choosing $D$ sufficiently large therefore gives a contribution

$$
                             O_{C,R_0,B}(N^2 L^{-B})
 \tag{11}
$$

for every prescribed fixed $B>0$, before integration in $\beta$. This sums the signed off-diagonal terms with the original coefficients; (9) is not applied to a sum of unsigned long labels.

The positive completion also has two additions, which must be subtracted to recover the positive centered norm precisely. At finite cutoffs $\mathcal S_q(0)=L^{O(1)}$: only $O_C(1)$ long labels in each dyad are zero modulo $q$ at fixed $l,s$, and (4) and the exterior log counts suffice. Its completed squared norm sums to $O(X^3 L^{O(1)})$. The sum over all residues factors the long and short transforms at each fixed $(l,s,h,i,\tau)$ with no further restrictions. By (9) at $\theta=0$, (4), and the bounded logarithmic losses it is $O_D(XL^{-D})$ for each fixed $D$. Restricting this sum to $v\ne0$ costs at most $|\mathcal S_q(0)|=L^{O(1)}$. Hence the algebraic principal contribution $\sum_q q|\sum_{v\ne0}\mathcal S_q(v)|^2$ is again $O_{C,R_0,B}(N^2L^{-B})$ for any fixed $B$. These two bounds contain no estimate for the true additive mean of $D^\dagger$.

## 3. Restore the exact rational diagonal and the literal shell

On $b=0$ the completed condition is literal equality of the rationals $\rho=j/(l^2hu)$, so this part is the squared norm of the integrated rational vector with weights $q(q-1)$. Its tails are estimated in this analytical space only. Here are bounds at the new cutoff, given explicitly to ensure that no global GRH input or remaining power cutoff is inherited.

Fix one $l,s,h,i,\tau$. In the square at $q$, write $u=r z,\ u'=r'z$ with $(r,r')=1$ and $j=d r,\ j'=d r'$ for an integer $d\ne0$, as follows from exact equality at this fixed $l,h$. Within the same dyad $u,u'\asymp U_i$, so $r,r'$ are comparable. On a dyadic range $r\asymp V$ there are $O(V^2)$ pairs of $(r,r')$ and $O(U_i/V)$ choices for $z$, with $V\ll U_i$ and $O(L)$ ranges. The product of the envelopes in (3), summed over $d$, is $O(Y_\tau/(V\xi))$ at $\xi=\xi_{q,i,h}$. Indeed the two arguments have comparable magnitude $|d|V\xi$, and the elementary fourth-power tail bound gives this estimate even when $Y_\tau/(V\xi)<1$. Including $\xi^2$ and summing the ranges bounds the squared norm per $q$ before $q(q-1)$ by $O(U_i\xi L Y_\tau)$. Since $U_i\xi\ll X$, the squared norm after the $q$ sum is $O(N^2 L Y_\tau)$. Apply the higher-order bound of (3) to the norm integral of $|\tau|>L^4$ and sum the outer labels by triangle. The resulting error is $O_B(NL^{-B})$ for any fixed $B$.

On retained $|\tau|\le L^4$, to bound the omitted-$j$ rational vector both arms in this squared norm have $|j|,|j'|>J_*$. Thus both short arguments have magnitude at least $F=L^{P-33}$ for all large $N$; comparability also holds from $r\asymp r'$. In place of the preceding envelope sum use

$$
       O\left(\frac{Y_\tau^4}{V\xi F^3}\right),
$$

obtained by summing $(Y_\tau/(|d|V\xi))^4$ over $|d|\gg F/(V\xi)$. The formula remains an upper bound if the indicated lower threshold is below one. Thus the squared norm of this omitted vector for the fixed exterior labels is $O(N^2 L Y_\tau^4/F^3)$. Taking $P$ large enough beats all requested fixed log powers, including the actual label counts and the $L^1$ time integral. These are norm estimates for fixed $l,s,h,i$ and then triangle for the negligible errors; they make no triangle estimate on the main coherent vector. The crude full-norm estimate just given and (3) imply that the extension changes the integrated squared rational norm at fixed $\beta$ by $O_B(N^2L^{-B})$ for each prescribed fixed $B$ after suitable cutoff choices.

We can now use the exact physical inversion termwise, as in [the rational-only inversion, §3](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#3-restore-the-exact-physical-integral-on-the-rational-diagonal-only). The signs remain $\mu(l)\mu(s)\mu(h)\mu(u)$; the contribution of a term with $su\in I_d$, $(u,lN)=1$ and $\rho l^2 h u\in\mathbb Z\setminus\{0\}$ is

$$
 \frac{\mu(l)\mu(s)\mu(h)\mu(u)N}{q l^2 h u}
       \int\Omega(x)e(\beta Nx)w(Nx/(su))e(-\rho Nx/q)\,dx.
 \tag{12}
$$

Let $\mathscr D_N$ be the $q(q-1)$-weighted squared norm of this common vector integrated over $\beta$. Its bound $O(N/L)$ comes solely from [the signed paired-label rational estimate, §2](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#2-factor-the-common-rational-denominator-before-the-square-label-sum): the actual $h$ signs are grouped, then the common and exclusive square-label prime factors are absolutely summable. This estimate is unconditional, and its pre-$\beta$ bound is $O(N^2/L)$ uniformly.

Subtract the finite artificial residue-zero and principal terms of §2 from the completed squared norm and use the true multiplicative-character Parseval identity for the mean-zero additive numerator groups. Its factor is $q/(q-1)$ per nonprincipal character norm, since the Gauss squared magnitude is $q$ and Parseval divides by $q-1$. The finite norms are nonnegative, so this differs from their total without the factor by relative $O(X^{-1})$. The uniform $O(N^2/L)$ rational bound, (11), the cutoff estimates, and the $\beta$ length $1/(5N)$ give

$$
                \mathcal E_N^0(D^\dagger)=\mathscr D_N+o(N/L).
 \tag{13}
$$

Adding the actual constant modes costs $O(N/L)$ for the upper bound by [the genuine constant-mode proof, §4](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#4-a-signed-real-sumintegral-for-the-actual-q-nonunits), which uses unconditional signed harmonic sums and ordinary bounds rather than either artificial term. Finally $\|D-D^\dagger\|_2^2=O(NL^{-2})$ transfers to the actual shell by disjoint arcs, also after projection. In squared norm its cross-term cost is $O(NL^{-3/2})$ since $\mathscr D_N=O(N/L)$. This proves (1) and gives (13) with the literal $D$.

## 4. The positive limit on the original fixed cuts

Now take $N=2^J$, $I_d=[X,1.01X]$, $I_k=(\max(N^{.49999},.42X),.50X)$, and $y=9N/16$. Here $h=1,2$, and $q\nmid d,k$ exactly on the true or approximate supports since $q<X<d$ up to the possible endpoint, $2q>1.01X$ and $k<X/2$. The actual mean of the additive numerator group of $D^\dagger$ is $-D^\dagger(\beta)/(q-1)$. Estimate this ordinary value at fixed $l,s,h,k$ by summing $u$ first. Its multiplier in $u$ is $\Omega(suk/N)e(\beta s u k)$, of bounded variation on its fixed physical support because $|\beta|N\le.1$. Equation (9) at zero additive frequency and $\tau=0$, with one more bounded-variation partial summation, bounds the signed $u$ sum by $O_B(U_iL^{-B})$. Summing the $O(X)$ short labels and the fixed-logarithmic number of exterior labels gives $|D^\dagger(\beta)|\ll_B NL^{-B}$ for any fixed $B>0$. The actual constant energy is therefore $o(N/L)$ after summing $(q-1)^{-1}$ and integrating in $\beta$. The genuine hard transfer preserves this negligibility in norm. Thus both energies are $\mathscr D_N+o(N/L)$ unconditionally on these cuts.

The vector (12) and $\mathscr D_N$ are literally the ones in (1)–(2) of [the limiting-energy proof](weak-s-type-ii-critical-prime-limiting-complementary-energy-grh.md). Its [rational truncation, §2](weak-s-type-ii-critical-prime-limiting-complementary-energy-grh.md#2-uniform-truncations-that-leave-a-finite-dimensional-limit) and [finite integral limit, §3](weak-s-type-ii-critical-prime-limiting-complementary-energy-grh.md#3-the-finite-integrals-and-their-limit) use no GRH: after truncating the paired square label with an absolutely summable Euler majorant, small denominators by the sparse derivative bound, and large numerators by integration by parts, only fixed-mask squarefree counts and ordinary prime-number asymptotics remain. They give the identical limiting constant from (7) there. For strict positivity use the [rational witness, §2 of the lower example](weak-s-type-ii-critical-prime-sharp-complementary-energy-example-grh.md#2-a-positive-proportion-of-denominators-with-a-nonzero-coherent-coordinate) directly, not its previously conditional conclusion for the true energy. That rational witness needs just positive-density squarefree denominators avoiding a fixed small-prime mask, an elementary $l$-tail first moment, and the prime number theorem. It gives $\mathscr D_N\gg N/L$ unconditionally. Equation (13) and the new actual constant estimate thus prove (2), with no quadratic or signed prime-pairing inference beyond the stated energy limits.
