# Smaller full polynomial critical-shell energy with the actual derivative edges and unit signs

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, and $V=\varphi(N)/N$. Keep all the hypotheses and exact supports of the [full polynomial critical-shell theorem](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md). Thus $J=[N-y,N/2)$, $N/2\le y\le9N/16$, the hard cofactor test includes $k>t\ge N^{.49999}$, and the original coefficient is

$$
 D_m=\mathbf1_{m\in J}
  \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                         (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k).
$$

The hard interval $I_d\subset[X,\infty)$ is arbitrary; its intersection with $[X,N/(2t))$ on this physical support is exact, and there is no further width restriction. Keep the same genuine prime polynomial $P$ and permissible bounded prime selector, with its hard prime product and unit tests. The literal energy is

$$
 \mathcal E_N(D)=\int_{-1/(10N)}^{1/(10N)}
      \sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}
                  |D(a/q+\beta)|^2\,d\beta,\qquad
         \mathcal Q=[.8X,.9X]\cap\mathbb P.
$$

**Theorem (global Dirichlet GRH).** Assume GRH for every primitive Dirichlet $L$-function, including $\zeta(s)$. Uniformly over each even target and all original admissible hard cutoffs, with all original unit primes retained,

$$
                  \mathcal E_N(D)\ll N L^{-1/2} L_2^2 V^{1/2}.
 \tag{1}
$$

Consequently the actual signed full shell, its separately centered numerator covariance and the exact parity-preserving signed even-lattice residual with length $M=\lceil XL^2\rceil$ are each $O(NL^{-1/4}L_2V^{1/4})$. More precisely the proof gives

$$
 \mathcal E_N(D)\ll
 N\left(\delta+\frac{\delta^{-1}V L_2^4}{L}\right)
                  +O\left(\frac{N L_2^{12}}{L}+NL^{-2}\right),
                  \qquad L^{-1/2}\le\delta\le L_2^{-4}.
 \tag{2}
$$

This is an improvement within the same full polynomial shell, not a different selection of moduli or units. The two new improvements below concern only the **exact integer determinant diagonal**, and do not use GRH. The estimate for nonzero determinants still uses global Dirichlet GRH; neither an unconditional estimate (1), other shells, a bound on squares of individual compensated offsets, nor Hypothesis S is asserted.

## 1. The inherited physical rational diagonal and literal approximation

Use the common inward physical mollification $\Omega(m/N)$ and common absolute cofactor cutoff $w(k)=W(\log k)$ at size $\delta$, as in [the full polynomial theorem, §§1–3](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#1-keep-the-genuine-common-smoothing-and-the-original-units). Both have bounded variation, with all true hard support preserved. The original approximate coefficients are unchanged: keep the exact long unit $(d,N)=1$, truncate the squarefree expansion at $l\le T=L^{16}$ with $(l,N)=1$, and truncate the short unit inclusion to $h\mid\operatorname{rad}N$, $h\le H_0=\exp(C_0L_2^2)$ for a sufficiently large fixed $C_0$. The global smoothing squared error is $O(N\delta)$ and the ordinary squarefree and short-unit truncation squared error is $O(NL^{-8})$ after the dyad sum. These transfers are uniform on the full original physical interval. As before $s=(l,d)\mid l$, $d=su$ and the exact long mask is $(u,lN)=1$.

The actual modular construction, its finite Fourier cutoffs, and the nonzero-determinant estimate are precisely the inherited ones, with this chosen fixed $C_0$. At each fixed $(l,s,\beta)$, global GRH bounds nonzero determinants by $O(N^{1.91})$ per pair of dyads before integration of the two independently truncated Fourier frequencies. Both integrations and all such pairs cost bounded powers of $L$, as do the finite $l,s$ label sums when applied to this error. The normalizing $\beta$ length is $1/(5N)$. Thus this error and the corresponding Fourier tails are negligible to every needed fixed inverse-logarithmic order in the shell. The actual principal and $q$-nonunit components are as in [the full polynomial theorem, §5](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#5-the-genuine-original-shell), contributing $O(NL_2^{12}/L)$, including $q\mid N$.

We recall the precise diagonal needed for the improvement. In the positive completed norm at fixed $(l,s,\beta)$, the integer determinant-zero condition is equality of the two nonzero **rational** coordinates $\rho=j/(hu)$, not just congruence. The inherited [rational tail restoration and physical inversion](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#3-restore-the-exact-physical-integral-on-the-rational-diagonal-only) applies before any new operation here. Restore both time and dual frequencies only in that exact rational space, changing its norm by $O_A(NL^{-A})$ for any fixed $A$. With $h\le H_0$ still in force, the physically inverted vector, at coordinate $(q,\rho)$, is

$$
 \mathcal V_{H_0}(q,\rho)=
   \sum_{\substack{h\mid\operatorname{rad}N,\ h\le H_0\\
                   su\in I_d,\ (u,lN)=1\\
                   j\ne0,\ j/(hu)=\rho}}
   \frac{N\mu(h)\mu(u)}{q l^2 h u}
     \int \Omega(x)e(\beta Nx)w(Nx/(su))
                           e\!\left(-\frac{jNx}{q l^2hu}\right)dx .
 \tag{3}
$$

The norm on this rational space has weights $q(q-1)$ in $(q,\rho)$. All artificial dyadic bumps equal one in the actual $\Omega$ support, so $I_d$ in (3) is the **single genuine full interval**. The change from the truncated diagonal of the modular positive norm to (3) occurs only after separating the nonzero-determinant estimate. The actual principal unit and nonunit terms are not replaced by this rational construction.

For a fixed pair $(h_1,h_2)$ with $g=(h_1,h_2)$, exact rational equality and $(u u',N)=1$ force $j=(h_1/g)i_1$, $j'=(h_2/g)i_2$, with $i_1/u=i_2/u'=a/c$ in reduced terms, $c\ge1$, $a\ne0$. Thus $u=cv$, $u'=cv'$ and the two physical frequency arguments agree, equal to $a\Lambda_c$ with $\Lambda_c=N/(q l^2 g c)$. Retain the same signed complete divisor functions as in that theorem:

$$
 R_c(x)=\sum_{\substack{scv\in I_d\\(cv,lN)=1}}\frac{\mu(cv)}v\,w(Nx/(scv)),
 \qquad F_c(x)=\Omega(x)e(\beta Nx)R_c(x).
 \tag{4}
$$

In the expansion of $\|\mathcal V_{H_0}\|_{\mathrm{rat}}^2$, the summand for this $q,h_1,h_2$ is exactly

$$
 \frac{q(q-1)N^2\,\mu(h_1)\mu(h_2)}{q^2 l^4 h_1h_2}
      \sum_{c\ge1}\frac1{c^2}
          \sum_{\substack{a\ne0\\(a,c)=1}}|\widehat F_c(a\Lambda_c)|^2 ,
 \tag{5}
$$

with $\widehat F(\xi)=\int F(x)e(-\xi x)\,dx$. These are the exact formulas of [the preceding physical sampling estimate](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#4-a-compact-physical-sampling-bound-for-the-masked-divisor-norm); in particular the same $F_c$ occurs for every $h_1,h_2$ at fixed $l,s,\beta$. Since its support has length less than one, compact periodization and integration by parts give the positive bound

$$
 \sum_{a\ne0}|\widehat F_c(a\Lambda)|^2
     \ll \Lambda^{-1}\big(\|F_c\|_2^2+\|F_c'\|_1^2\big)
                              \qquad(\Lambda>0).
 \tag{6}
$$

For $\Lambda\le1$ use Parseval at period $1/\Lambda$; for $\Lambda>1$ use the derivative and the sum over $a\ne0$ of $1/a^2$. The exclusion of $a=0$ in the rational coordinates is essential in the second range. When inserted into (5), the normalization in (6) gives $N(q-1)/(l^2[h_1,h_2])$ times the sum of $(\|F_c\|_2^2+\|F_c'\|_1^2)/c$. This is where the next two changes apply.

## 2. A sharper direct reciprocal norm on the true derivative edges

Let $B_0=lN$ as above. For a genuine hard interval $I$ at a positive proportional scale $U$ with $N^{.48}\le U\le N^{.51}$ and length $O(\delta U)$, we have

$$
 \sum_{c\ge1}\frac1c
   \left|\sum_{\substack{cv\in I\\(cv,B_0)=1}}\frac{\mu(cv)}v\right|^2
   \ll_A \delta+\delta^2 L_2^3+\frac{L}{U}+L^{-A}\ll\delta .
 \tag{7}
$$

The last inequality uses the stated range of $\delta$ and sufficiently large fixed $A$. Constants are uniform for fixed positive proportional and length constants. This is a direct estimate with weight $1/c$, not a comparison to $\varphi(c)/c^2$ in the narrow range.

For proof, set $Z=\exp(L_2^3)$. For $c\le U/Z$, terms with $(c,B_0)>1$ or $\mu(c)=0$ vanish. Otherwise write $\mu(cv)=\mu(c)\mu(v)\mathbf1_{(v,c)=1}$, so the inner reciprocal sum has mask $cB_0\le N^2$ for sufficiently large $N$. Its endpoints are $\gg Z$. The [signed reciprocal Mertens argument for a narrow interval](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md#a-signed-narrow-continuous-form-and-actual-label-edges) gives an arbitrary fixed inverse-logarithmic bound there, also with this mask: its coprime smooth-integer convolution uses exponents $1$ and $1-1/L_2$, whose Euler costs are $O(L_2)$ and $L_2^{O(1)}$ for any mask at most $N^2$, by the prime-factor split in the [masked signed lcm proof](weak-s-type-ii-critical-prime-unconditional-all-targets.md#1-the-signed-lcm-form-with-the-full-unit-mask). In detail, splitting at convolution factor the square root of the endpoint gives either the ordinary reciprocal Mertens saving at arguments $\gg\sqrt Z$, or the factor $Z^{-1/(2L_2)}$ up to a fixed constant. Both beat all powers of $L$, also after the reciprocal sum over $c$. Exact hard endpoints may be subtracted as prefixes; changing an isolated endpoint costs $O(1/Z)$ there.

For $U/Z<c\le C_1\delta U$, with $C_1$ a fixed constant larger than the relative length constant, the unsigned inner reciprocal sum is $O(\delta)$: there are at most $1+O(\delta U/c)$ terms of size $O(c/U)$. Summing $1/c$ in this middle range costs $O(L_2^3)$ (and is zero if empty). For $c>C_1\delta U$, at most one integer lies in $I/c$. Drop its mask in this positive upper bound and reverse the divisibility sum. The contribution is bounded by

$$
 \sum_{u\in I}\frac1{u^2}\sum_{c\mid u}c
       =\sum_{u\in I}\frac1u\sum_{b\mid u}\frac1b
 \ll \frac1U\sum_{b\ll U}\frac{1+O(\delta U/b)}b
 \ll \delta+\frac LU .
$$

The additive $1$ in the interval counts handles all conventions on strict endpoints. This proves (7).

At a fixed $x$ in the original physical support, the derivative of the cofactor weight $w(Nx/(su))$ in $x$ is

$$
                \frac1x\,W'\big(\log(Nx/(su))\big).
 \tag{8}
$$

For the actual inward log mollification, $W'$ is a difference of two translates of the smoothing kernel, each of sup norm plus total variation $O(\delta^{-1})$, each supported on a log interval of length $O(\delta)$. If the original interval is too short and the chosen smoothing is zero, so is (8). Each endpoint translate in (8) thus occupies one positive proportional interval in $u$ of length $O(\delta U)$ as in (7), intersected with the actual $I_d/s$. If nonempty its scale is in $[N^{.48},N^{.51}]$ for large $N$, since the effective true $d$ lies between $X$ and $N^{.50001}$ and $s\le L^{16}$. Composition with the monotone map $u\mapsto \log(Nx/(su))$ preserves the variation bound, and $1/x=O(1)$ here. Apply (7) to the hard prefixes **inside each such narrow interval** and do partial summation in the positive $\ell^2(1/c)$ norm. This yields the uniform derivative bound

$$
                  \|R_c'(x)\|_{\ell^2(1/c)}\ll\delta^{-1/2}.
 \tag{9}
$$

The two endpoint translates may be handled separately even if they overlap. No derivative weight is replaced by an unsigned coefficient on the complete polynomial interval.

For $R_c(x)$ itself on the full interval, retain the earlier bound $O(L_2^3)$ for the squared norm with weight $1/c$: use the masked DIT signed interval estimate with bounded-BV weight $w$ in (4), and $c/\varphi(c)\ll L_2$ for the actual $c\le N$, exactly as in the preceding proof. The full physical multiplier $\Omega(x)e(\beta Nx)$ has sup norm and derivative $L^1$ norm $O(1)$, as $|\beta|N\ll1$. For the derivative of its product with $R_c(x)$, take Minkowski in this weighted norm, using (9) and $\delta^{-1}\ge L_2^4$. We obtain the improvement of the sampling input:

$$
              \sum_c\frac1c
                         \bigl(\|F_c\|_2^2+\|F_c'\|_1^2\bigr)
                      \ll\delta^{-1}.
 \tag{10}
$$

This step is unconditional, uniform in the true hard intervals, and uses the direct narrow weight in (7) only for the actual cofactor derivative. The unrestricted term of the physical derivative is already dominated.

## 3. Exact exterior unit signs in the physically inverted norm

We now extend the set of $h$ to **all** squarefree divisors of $N$ in (3), only in the positive analytical rational space. Define $\mathcal V_{\mathrm{all}}$ by that extension of the *physically inverted* formula and $\mathcal V_{\mathrm{tail}}=\mathcal V_{\mathrm{all}}-\mathcal V_{H_0}$. All $h$ sets are finite and Fourier decay of the smooth compact physical test guarantees convergence in the dual indices for each fixed $N$. The exact pair formula (5) also holds for each of these sets: it uses integer equality of the rationals and the true $(u u',N)=1$, not that newly restored $h$ or dual integers are units modulo $q$. In particular this step does not extend the modular positive square, the nonzero determinant estimate, or the actual auxiliary coefficient entering the ordinary approximation. It does not alter the already restored $j,\tau$ tails.

For the tail vector $\mathcal V_{\mathrm{tail}}$ both $h$ labels in its squared norm exceed $H_0$. From (5), (6) and (10), taking absolute values of its $h$ signs, its squared norm is bounded by $O(N^2\delta^{-1}/(L l^2))$ times the corresponding pair sum of $1/[h_1,h_2]$. Rankin on $h_1$ with exponent $1/L_2$ and the four per-prime allocations give

$$
 \sum_{\substack{h_1,h_2\mid\operatorname{rad}N\\h_1,h_2>H_0}}
        \frac1{[h_1,h_2]}
 \le H_0^{-1/L_2}
       \prod_{p\mid N}\bigl(1+1/p+2p^{-1+1/L_2}\bigr)
 \ll e^{-C_0L_2}L_2^{O(1)}.
 \tag{11}
$$

Indeed for $p\le L^2$ use $p^{1/L_2}\le e^2$ and the prime harmonic sum; beyond $L^2$ there are at most $O(L)$ prime factors, each contributing $O(L^{-2+2/L_2})$. With a sufficiently large fixed $C_0$ the tail is negligible after all subsequent norm sums. The triangle bound
$\|\mathcal V_{H_0}\|_{\mathrm{rat}}\le\|\mathcal V_{\mathrm{all}}\|_{\mathrm{rat}}+\|\mathcal V_{\mathrm{tail}}\|_{\mathrm{rat}}$
will retain the upper bound for the originally truncated rational diagonal.

For the full $\mathcal V_{\mathrm{all}}$ keep its exterior $\mu(h_1)\mu(h_2)$ signs. At fixed $q,g=(h_1,h_2)$ the whole physical sampling expression in (5) is independent of $h_1,h_2$ apart from the two exterior denominators and signs. In particular its common sampling step depends on $g$ but not on the separate $h_i$. Write $h_i=g d_i$, where the $d_i$ are disjoint squarefree divisors of $\operatorname{rad}N/g$. Exactly

$$
 \sum_{\substack{h_1,h_2\mid\operatorname{rad}N\\(h_1,h_2)=g}}
          \frac{\mu(h_1)\mu(h_2)}{h_1h_2}
       =\frac1{g^2}\prod_{\substack{p\mid N\\p\nmid g}}
                                                   (1-2/p).
 \tag{12}
$$

At any prime not in $g$ there are the three cases neither, first only, and second only; both would change the gcd. The grouped coefficient is nonnegative, with a possible zero when $2\mid N$ and $2\nmid g$. Thus apply the positive sampling bound (6) **after** the signed grouping (12), and drop $(a,c)=1$ only in that positive bound. Then the factor $\Lambda_c^{-1}=q l^2 g c/N$ supplies one $g$. The remaining exterior $g$ mass is exactly

$$
 \sum_{g\mid\operatorname{rad}N}\frac1g
              \prod_{\substack{p\mid N\\p\nmid g}}(1-2/p)
       =\prod_{p\mid N}\left(\frac1p+1-\frac2p\right)
       =\frac{\varphi(N)}{N}=V .
 \tag{13}
$$

This calculation is valid for every actual radical, including $2$; no estimate has replaced the signed unit inclusion by absolute values in the full rational term.

Combining (10), (12)–(13) and $\sum_{q\in\mathcal Q}(q-1)\ll N/L$, the squared rational norm at fixed $(l,s,\beta)$, with the originally truncated $h$ restored back by (11), is at most

$$
                   O\left(\frac{N^2\delta^{-1}V}{L l^2}\right)
$$

plus negligible errors. This replaces both the previous squared derivative cost and the unsigned $h$ pair moment. Neither the arithmetic sign of the long divisor nor the interval has been factored independently of its true weight in (4).

## 4. Put the sharper diagonal into the literal shell

Use the exact original nonzero determinant bound, the already restored $\tau,j$ tails, and the last rational estimate. Minkowski over $(l,s)$ costs $\sum_{l\le T}\tau_{\mathrm d}(l)/l\ll L_2^2$ in norm, where $\tau_{\mathrm d}$ is the divisor function. The real $\beta$ interval has length $1/(5N)$ and the finite additive nonprincipal Gauss factor in squared norm is at most $q/(q-1)$. The resulting original nonprincipal energy is

$$
                   O\left(\frac{N\delta^{-1}V L_2^4}{L}\right)
                                 +O(NL^{-2}).
$$

Add the true principal and nonunit costs $O(NL_2^{12}/L)$ and the true ordinary transfer costs from §1. The original arcs are disjoint, so Parseval applies to those ordinary errors without enlarging their size. This proves (2). Since $V\gg1/L_2$, the choice $\delta=L^{-1/2}L_2^2\sqrt V$ lies in the allowed range for sufficiently large $N$. The $NL_2^{12}/L$ term is subordinate to the resulting main term uniformly in $N$, which proves (1).

The true $P,D$ have ordinary norm $O(\sqrt N)$ as in the full polynomial theorem. Apply Cauchy and contraction under separate numerator centering. For the exact parity-preserving residual, use the original identity and its error $O(N/L+N(X/M)^2)$ only after returning to the genuinely odd supports, as in that theorem. This proves the stated signed bounds, without any claim for the squares of individual compensated offsets.
