# Coherent square labels give an inverse-logarithmic upper bound on the genuine critical-shell energy

Work with the exact setup of the [inverse-logarithmic shell theorem](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md). Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, and $e(z)=e^{2\pi i z}$. The exact hard coefficient is

$$
 D_m=\mathbf 1_{m\in [N-y,N/2)}
 \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\(dk,N)=1,\ (d,k)=1}}
                 \mu(d)\mu^2(k),\qquad
 D(\alpha)=\sum_m D_m e(\alpha m),
$$

where $N/2\le y\le9N/16$, $I_d\subset[X,\infty)$ is an arbitrary hard interval, and the hard cofactor interval $I_k$ includes $k>t\ge N^{.49999}$. In particular $d<N/(2t)$ on actual support, with no extra restriction on its width. Define $\mathcal Q=[.8X,.9X]\cap\mathbb P$ and

$$
 \mathcal E_N(D)=\int_{-1/(10N)}^{1/(10N)}
    \sum_{q\in\mathcal Q}\sum_{1\le a<q}|D(a/q+\beta)|^2\,d\beta .
$$

**Theorem (global Dirichlet GRH).** Assume GRH for all primitive Dirichlet $L$-functions, including the Riemann zeta function. Uniformly on the actual full polynomial interval, original unit conditions and all the permitted cuts,

$$
                           \mathcal E_N(D)\ll \frac{N}{L}. \tag{1}
$$

For the same genuine prime polynomial $P$ and permitted selectors as in the preceding theorem, the actual signed shell, its separately centered numerator covariance, and the exact parity-preserving signed even-lattice residual with $M=\lceil XL^2\rceil$ are $O(N/\sqrt L)$. Only the inherited nonzero-determinant bound uses GRH. The result does not control other shells or the full operator, does not bound individual compensated offsets, and is not Hypothesis S.

## 1. Complete the square only after adding the square labels

Use the actual inward smoothing $\delta=L^{-2}$, physical weight $\Omega(x)$ and cofactor weight $w(k)=W(\log k)$ of [the preceding theorem, §1](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#1-actual-transfers-at-the-smaller-smoothing-width). The true squared ordinary approximation error is $O(NL^{-2})$. We keep all of its literal arithmetic approximations: signed squarefree $l\le T=L^{16}$ with $(l,N)=1$, short inclusion $h\mid\operatorname{rad}N$ with $h\le H_0=\exp(C_0L_2^2)$, and $s=(l,d)\mid l$, with $d=su$, $(u,lN)=1$ and $k$ a positive multiple of $l^2h/s$. The sign from the two first divisor variables is $\mu(l)\mu(s)\mu(u)$, in addition to the unit sign $\mu(h)$. In particular these are not independent unsmoothed changes of the original arithmetic.

Use the dyad quantities $A_i=\lambda_i X,\ K_i=X/\lambda_i,\ U_i=A_i/s,\ x_{q,i}=K_i s/(ql^2)$ with $\lambda_i\le N^{1/100000}$, where $i$ runs over the disjoint divisor dyads. Let $a_{i,\tau},f_{i,\tau}$ and $G_\beta$ denote the phases and cutoffs of [the integrated determinant construction, §2](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#2-integrate-in-the-complete-square-and-dispatch-its-off-diagonal). Here $a_{i,\tau}(u)=\mu(u)\mathbf1_{su\in I_i}\mathbf1_{(u,lN)=1}e(\tau\log(su/A_i))$, and $G_\beta(z)=\Omega(e^z)e(\beta Ne^z)$. In the finite modular vector keep $|\tau|\le L^4$ and $0<|j|\le J_i=\lambda_i N^{1/1000}$. Every retained $l,h,j$ is a unit modulo every $q\in\mathcal Q$. Previously the common Gauss factor for $\chi\ne\chi_0$ was followed by $\mu(l)\mu(s)\chi(l^2)$. Instead insert $\chi(l^2)$ into the argument of $\chi$, and form the combined array

$$
 \begin{split}
 \mathcal S_q(v)=
 \int_{|\tau|\le L^4}\widehat G_\beta(\tau)
 \sum_{\substack{l\le T,\ (l,N)=1\\s\mid l}}\mu(l)\mu(s)
 \sum_i \sum_{\substack{h\mid\operatorname{rad}N,\ h\le H_0\\
                        0<|j|\le J_i\\l^2hu/j\equiv v\bmod q}}
 \frac{\mu(h)x_{q,i}}h\,a_{i,\tau}(u)
                \widehat f_{i,\tau}(jx_{q,i}/h)\,d\tau .
 \end{split} \tag{2}
$$

The sum in the last line includes the $u$ labels on the indicated actual support. Squarefree $l$ can be required, since the others have zero sign. For nonprincipal $\chi$ its Fourier transform on the unit residues is followed by the same Gauss factor $\tau_q(\chi)$ of modulus $\sqrt q$, independent of $l,s,i$. In particular (2) is obtained before completing squares; it is not the sum of already completed norms. Add the principal and zero terms by positivity. The actual nonprincipal character norm after the original finite truncations is then bounded by

$$
                      \sum_q q(q-1)\sum_{v\bmod q}|\mathcal S_q(v)|^2 . \tag{3}
$$

As in the original expansion, the additive numerator energy has at most a bounded extra factor $q/(q-1)$. The constant additive modes are kept independently and restored in §3 below, not identified with the algebraic terms in (3).

Expanding (3) with independent frequencies $\tau,\tau'$ gives

$$
                l_1^2 h_1 j' u_1-l_2^2h_2 j u_2=bq. \tag{4}
$$

For $b\ne0$, fix $l_1,s_1,l_2,s_2,i,i'$ in addition to $h_1,h_2,j,j',b$. The two integral dilations in the Fourier proof are now $l_1^2h_1j'$ and $l_2^2h_2j$. They are nonzero integers, so the original $L^2$ bounds are unchanged. The $bq$ frequencies are distinct for fixed nonzero $b$, and the actual short Fourier weights including $q(q-1)$ are $O(X^2)$, since $x_{q,i}\ll1$. The first signed factor still has its uniform $U_i^{4/5}$ bound under GRH, the second has norm $O(U_{i'}^{1/2})$, and the $q$ factor has norm $O(X^2\sqrt{\#\mathcal Q})$. The new $l_i^2$ can enlarge the $b$ range only by $T^2$. Thus the total tuple count at fixed $l,s,i$ pair is $O(\lambda_{\max}^4N^{3/1000+o(1)})$, with $\lambda_{\max}\le N^{1/100000}$, as in the integrated determinant proof. In particular the same $O(N^{1.91})$ bound per pair applies before the integrations, since the power without labels is at most $N^{1.9+0.000013}$. Both frequency $L^1$ weights, all dyads and all square labels cost only fixed logarithmic factors. The whole nonzero-determinant contribution to (3) is power smaller than $N^2/L$, uniformly in $\beta$. No nonunit $j$ enters this argument.

For $b=0$ the completed vector has literal rational coordinates
$\rho=j/(l^2hu)\in\mathbb Q\setminus\{0\}$ for each $q$, with positive norm weights $q(q-1)$. On each fixed $l,s$, the change of coordinates from the previous rational vector $\rho_0=j/(hu)$ to $\rho=\rho_0/l^2$ is a bijective relabeling of the rational norm. The [exact-rational $j,\tau$ tail bounds, §3](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#3-restore-the-exact-physical-integral-on-the-rational-diagonal-only), at the smaller width as justified in the preceding theorem, therefore allow extension to all $j\ne0$ and all $\tau$ on each $l,s$ with $\mathrm{rat}$-norm error $O_A(NL^{-A})$. Combining these negligible errors by triangle costs only a fixed logarithmic power since $l\le T$. The extended vector also has a polynomial-in-$L$ bound in units of $N$ before the improvement below, so the change in the square can be taken as small as any fixed inverse log. The same reasoning applies to the original modular $j,\tau$ truncation errors, for which the cited proof controls actual separated centers. None of these extensions is made in (2) or in the nonzero equation of (4).

After Fourier inversion each term of the rational vector has its exact amplitude

$$
 \mu(l)\mu(s)\mu(h)\mu(u)\frac{N}{q l^2h u}
   \int \Omega(x)e(\beta Nx)w(Nx/(su))e(-\rho Nx/q)\,dx. \tag{5}
$$

The normalized dyad bump was one on this actual physical support, so the $u$ cut can be taken on the single full hard interval $su\in I_d$. In the analytical rational vector only, we may now restore **all** $h\mid\operatorname{rad}N$. Indeed, the norm of the tail at fixed $l,s$ is invariant under the same relabeling. The absolute lcm-weighted tail bound in [the preceding theorem, §3](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#3-keep-the-stronger-sparse-sampling-bound-and-integrate-the-actual-derivative) is

$$
 \ll \frac{N^2}{L l^2 V(lN)}
       \sum_{\substack{h_1,h_2\mid\operatorname{rad}N\\h_1,h_2>H_0}}
              \frac1{[h_1,h_2]},\qquad V(B)=\frac{\varphi(B)}B,
$$

for the squared tail. Its pair Rankin estimate is $e^{-C_0L_2}L_2^{O(1)}$ in the last sum. Take $C_0$ sufficiently large and combine the negligible tails over the square labels by triangle. This remains harmless at the $N^2/L$ scale. All signs and terms in (5) can thus be used jointly, including $h$ divisible by $q$, without introducing a new modular inverse or altering (4).

## 2. Factor the common rational denominator before the square-label sum

Fix the two exterior $l,s,h$ labels and $q,\beta$. Write $b_i=l_i^2h_i$ for $i=1,2$, and $\rho=a/c$ in reduced terms with $c\ge1,\ a\ne0$. For each arm (5) occurs exactly when $c\mid b_i u_i$; the corresponding integer $j_i=a b_i u_i/c$ is unique. Put $c_i=c/(c,b_i)$, so $u_i=c_i v_i$. The two transforms have the same frequency $aN/(qc)$, and the two exterior denominators are $b_i c_i$. Define the actual arm transform by

$$
 F_{i,c_i}(x)=\Omega(x)e(\beta Nx)
       \sum_{\substack{s_i c_i v\in I_d\\(c_i v,l_iN)=1}}
                       \frac{\mu(c_i v)}v\,w(Nx/(s_i c_i v)).
 \tag{6}
$$

Separate $c=c_0m$, where $c_0$ is supported on the primes of $l_1l_2N$ and $(m,l_1l_2N)=1$. On the actual support each $u_i$ is squarefree and $(u_i,l_iN)=1$, and $(l_i,N)=1$. Thus the exact possibilities at each prime are:

- If $p\mid N$, its exponent in $c$ is zero or one. The exponent one is possible only when $p\mid g=(h_1,h_2)$, and then it does not appear in either $c_i$. Denote this part by $c_N\mid g$.
- If $p\mid(l_1,l_2)$, its exponent in $c$ is $0,1$ or $2$, and it is absent in both $c_i$.
- If $p\mid l_j,\ p\nmid l_i$ for $i\ne j$, its exponent is zero or one. In the latter case it goes into $c_i$ alone.
- Outside $l_1l_2N$, the exponent is zero or one, with the prime occurring identically in both $c_i$.

These give $c_i=m_i m$, where $m_i$ is squarefree, $m_i\mid l_{3-i}$ and $(m_i,l_iN)=1$. Each $m_i$ is determined by the chosen $c_0$ primes exclusive to the opposite label. For any permitted $c_0$ the remaining dependence on the arithmetic support is enforced by (6), including the squarefree sign. In particular the two $F_{i,c_i}$, the admissible $m,a$ conditions and the common frequency depend on the $h$ pair only through the admissible set $c_N\mid g$.

Retain the exact $h$ signs before any inequality in each fixed $l,s$ pair. At fixed $g$, the signed coefficient apart from $l,s$ and the common quantities in (6) is

$$
 \sum_{\substack{h_1,h_2\mid\operatorname{rad}N\\(h_1,h_2)=g}}
        \frac{\mu(h_1)\mu(h_2)}{h_1h_2}
   =\frac1{g^2}\prod_{\substack{p\mid N\\p\nmid g}}(1-2/p)\ \ge0 . \tag{7}
$$

Indeed a prime in $g$ is on both arms, and a prime outside $g$ can occur on neither or exactly one. In particular (7) vanishes when $2\nmid g$.

Fix $c_0$ for the moment. Its mixed sampled sum, after taking $1/(m_1m_2)$ outside, is

$$
 \sum_{\substack{m\ge1\\(m,l_1l_2N)=1}}\frac1{m^2}
    \sum_{\substack{a\ne0\\(a,c_0m)=1}}
       \widehat F_{1,m_1m}(aN/(qc_0m))
                 \overline{\widehat F_{2,m_2m}(aN/(qc_0m))}.
 \tag{8}
$$

The squarefree condition on $m$ is automatic where the signs are nonzero. Bound (8) by Cauchy in the indicated $(m,a)$ coordinates. For each individual square the sparse/dense bound [§3, (8) of the preceding theorem](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#3-keep-the-stronger-sparse-sampling-bound-and-integrate-the-actual-derivative) applies with $C_*=N/(q c_0)$, label variable $m$, interval $I_d/(s_i m_i)$, and mask $B_i=l_iNm_i$. More explicitly, factoring $\mu(m_i m v)$ supplies the constant $\mu(m_i)$ and the exact extra coprimality $(mv,m_i)=1$ wherever the sign is nonzero. The remaining sign is $\mu(mv)$, and the weight is $w(Nx/(s_i m_i m v))$. The new hard interval is still at polynomial scale, since $s_i m_i\le T^2$; the mask is polynomially bounded. Hence the direct $1/m$ reciprocal norm from that theorem is $O(1/V(B_i))$. The physical derivative estimate for the cofactor part is still $O(1)$ per $m$: the actual integrated log bumps constrain $v$ to at most two constant-ratio intervals of scale $N/(s_im_im k_{\rm e})$, for the actual endpoints $k_{\rm e}$, and integrate in $d x/x$. No derivative supremum cost or numerator zero is introduced. Any extra restrictions on $m,a$ are dropped only in these positive squares. It follows that (8) is at most

$$
                 O\left(\frac{q c_0}{N\sqrt{V(B_1)V(B_2)}}\right) \tag{9}
$$

in absolute value. Including the two $N/q$ factors, the weight $q(q-1)$, the square-label denominators and $1/(m_1m_2)$, the remaining bound at this $c_0$, before multiplication by (7), is

$$
 O\left(\frac{N(q-1)c_0}
   {l_1^2 l_2^2\,m_1m_2\sqrt{V(l_1Nm_1)V(l_2Nm_2)}}\right). \tag{10}
$$

The transform expansions are legitimate as positive-norm scalar products. For fixed $N$ the exterior labels are finite, and the square bounds (9) give absolute summability of the mixed transform products by Cauchy.

Now sum $c_N\mid g$ in (10), supplying $\sigma(g)$, and then $g$ in (7). The exact $N$-prime factor is

$$
 \prod_{p\mid N}\left(1-\frac2p+\frac{1+p}{p^2}\right)
     =\prod_{p\mid N}\left(1-\frac1p+\frac1{p^2}\right)
     \ll V(N). \tag{11}
$$

The last comparison follows since the ratio at $p$ is $1+1/(p(p-1))$. This cancels $V(N)^{-1}$ from the two square-root masks in (10). The remaining $c_0$ factors are independent of the primes of $N$: each common $p\mid(l_1,l_2)$ gives $1+p+p^2$, and each exclusive $p$ gives $1+(1-1/p)^{-1/2}$, because its factor $p$ in $c_0$ is canceled by $m_i$. The remaining outside denominator is $l_1^2l_2^2\sqrt{V(l_1)V(l_2)}$. There are at most $\tau_{\rm d}(l_1)\tau_{\rm d}(l_2)$ choices of $s_1,s_2$, where $\tau_{\rm d}$ is the divisor function. Taking absolute values of the exterior $l,s$ signs **now**, the total arithmetic factor over the two squarefree $l$ labels is bounded independently of $T$: it is at most

$$
 \prod_p\left(
 1+\frac{4(1+(1-1/p)^{-1/2})}{p^2\sqrt{1-1/p}}
   +\frac{4(1+p+p^2)}{p^4(1-1/p)}
 \right)<\infty. \tag{12}
$$

The terms describe a prime exclusive to either label or present on both, including the respective divisor counts. Both are $O(p^{-2})$. This convergent paired-label cost replaces the factor $L_2^4$ in the separately estimated completed norms.

It follows from (10)–(12) that the whole rational squared norm is $O(N\sum_q(q-1))=O(N^2/L)$ uniformly in $\beta$. In particular no norm triangle over the main square-label contributions has been used.

## 3. Restore the actual modes and original signed statistic

The length of the $\beta$ interval is $1/(5N)$. The original nonprincipal additive energy is $O(N/L)$ by (2)–(12), with the approximation errors bounded in the ordinary or sampled norm as stated. The actual additive constants are unchanged from [the preceding theorem, §4](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#4-a-signed-real-sumintegral-for-the-actual-q-nonunits): the genuine $q$-nonunit value is $O(X)$ by its reciprocal sum–integral and exact $h$ sign, including the zero when $q\mid N$; the actual principal unit coefficient has energy $O(N/L)$. These bounds concern the original truncated smoothed polynomial and do not rely on the algebraically completed principal and residue-zero terms. The actual arcs are disjoint, so ordinary Parseval controls the $O(NL^{-2})$ squared genuine coefficient error and the smaller arithmetic truncation errors on the shell. This proves (1) for the literal hard coefficient.

The actual prime polynomial has ordinary squared norm $O(N)$. Cauchy on the shell and contraction for centering therefore give $O(N/\sqrt L)$ for the first two signed quantities. The [original parity-preserving reduction](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md) for the genuine odd supports has error $O(N/L+N(X/M)^2)$, which at the stated $M$ is smaller. This gives the same bound for the exact signed even-lattice residual, without a claim on any other shell or on global weak S.
