# Full variance of the exterior difference matrix on shorter modulus windows

**Scope.** This bounds the full modulus-wise $L^2$ error, not just its low rational-frequency component, for the actual specified exterior mean differences and a quantitative shorter-window range. It uses auxiliary Dirichlet GRH. It does not bound individual moduli, other operator directions, or weak S.

Write $L=\log Q,\ \ell=\log L$. Fix $K>0,\ C>1$ and let $\mathcal I\subset[Q,2Q]$ be any interval of length

$$
 Q^{22/25}\le \Delta\le Q^{19/20}.
$$

Take the [common physical dyadic grid](r43-operator-signed-modulus-window.md) $V=2^jY$, $Y=e^H$, and its whole dyads in $[Y,M]$, where

$$
 H\ge 2(K+3)\ell^2/\log\ell,\qquad M=e^{CH}\le Q^{1/40}.
$$

Use the [normalized true mean differences](r40-operator-negative-difference-subspace.md) and their dyad-index isometries $E_N$ for even $N\in\mathcal I$. Put $B=P=\lfloor Q^{1/5}\rfloor$, $h=\lfloor Q^{3/4}\rfloor$. Assume the original local Dirichlet GRH at every even $N$ used and auxiliary Dirichlet GRH for moduli up to $8BM+2$; global Dirichlet GRH suffices. Then for every fixed $\epsilon>0$,

$$
 \left(\operatorname{Avg}_{N\in\mathcal I,\ 2\mid N}
   \|E_N^*T_NE_N\|_{\rm HS}^2\right)^{1/2}
 \ll_\epsilon Q^{-1/400+\epsilon}+L^{5/2}Y^{-1/5}
 =o(L^{-K})
 \tag{1}
$$

when $\epsilon$ is sufficiently small. The conclusion is for the entire Fourier spectrum in the modulus variable, but only on this spatial compression. The [exact spatial log-separation mask](r31-operator-zero-diagonal.md) equals one here, since the support diameter in log coordinates is at most $(\log Q)/40$. The estimate compares the true prime-power aliases with the exact original continuous model, not the long-divisor artificial integer diagonal.

## 1. Freeze the actual raw weights on the short interval

For even $N\in\mathcal I$, first take the R43 fixed physical subcell endpoints instead of whole R40 cells. The isometry error is $O(Y^{-1/5})$ and the two-sided operator error is $O(L^2Y^{-1/5})$, by R43. Let $N_0\in\mathcal I$ be any even midpoint representative (any even member within $O(\Delta)$ of all the others suffices). Write $e^\circ_{N,V}$ for the fixed-endpoint unit difference, and $r_N$ for the actual physical Hardy weight. For $a=N/N_0$ use the real profile

$$
 g_{N,V}(u)=a^2\frac{r_{N_0}(au)}{r_N(u)}e^\circ_{N_0,V}(au).
$$

These profiles need not be renormalized. They satisfy the exact identity

$$
 \frac{\sqrt{2\pi x}}N\int_{u\ge x/N} r_N(u)g_{N,V}(u)\,du
 = \frac{\sqrt{2\pi x}}{N_0}
       \int_{z\ge x/N_0}r_{N_0}(z)e^\circ_{N_0,V}(z)\,dz
 =:\rho_V(x).
 \tag{2}
$$

The ratio $a^2r_{N_0}(au)/r_N(u)=1+O(\Delta/Q)$ uniformly on these supports: in the numerator the raw argument $N_0au=Nu$ is unchanged, and $\log N-\log N_0=O(\Delta/Q)$. The base physical factors give $a^{1/2}=1+O(\Delta/Q)$. The fixed-endpoint profiles are smooth with uniformly bounded scaled derivatives on the interiors of their pieces; the two shifted support boundaries and the internal boundaries change by $O(V\Delta/Q)$, where profiles have size $O(V^{-1/2})$. Also the fixed-endpoint construction varies by $O(\Delta/Q)$ in $L^2$ on changing $N$ at fixed physical arguments, by differentiating its normalized weights as in R43. Hence

$$
 \|g_{N,V}-e^\circ_{N,V}\|_2\ll (\Delta/Q)^{1/2}.
$$

Both families separately have disjoint dyadic supports (the $g$-family uses the common dilation). Their *differences* have overlap bounded absolutely: each difference is supported in $I_V\cup a^{-1}I_V$, and each collection is disjoint. Thus the same bound holds in operator norm for the difference of the basis maps, by Cauchy–Schwarz at each point. The actual $T_N$ norm on the union of these exterior supports is $O(L^2)$ from the atom trace and stationary comparison, as in R43; the $O(\Delta/Q)$ change of the initial height is harmless under the stated threshold. Converting compression errors to HS costs at most $O(L^{1/2})$, since there are $O(L)$ dyads. The total test substitution error is therefore

$$
 O\big(L^{5/2}((\Delta/Q)^{1/2}+Y^{-1/5})\big).
 \tag{3}
$$

Let $X_V=N_0V$. Equation (2) is the genuine Volterra prefix weight, fixed as a function of the *raw integer* variable, of the form
$\rho_V(x)=X_V^{-1/2}b_{N_0,V}(x/X_V)$.
The function $b_{N_0,V}$ is bounded and Lipschitz, supported in $[1,2]$ with zero extension, as in R43. Original prime-power aliases on the $g$-tests can discard all proper powers with entry error $O(Q^{-1/2}ML^3)$: there are $O(\sqrt{Q\max(V,U)}L)$ powers on either leg, each with at most $O(\max(V,U))$ partners over the alias lines, and weight products at most $O(L^2/(Q\sqrt{VU}))$. Ordinary primes on the supports are larger than every $N$ and hence are units. The R43 physical line formula is still exact by (2): the true line $m=x\pm kN$ or $m=kN-x$ uses the product $\rho_V(x)\rho_U(m)$ times the ordinary prime log weights, and the continuous model uses $\mathfrak S(kN)\int \rho_V(x)\rho_U(m)\,dx$. Only $1\le k\le4M$ can occur for all large $Q$, since fixed raw supports end at $2N_0 M$ and $N_0/N=1+o(1)$; for the sum orientation more precisely $V,U\le M/2$ because their full physical dyads lie in $[Y,M]$. No integer equality line is included. Let $\widetilde X$ be this frozen ordinary-prime-only discrepancy matrix sequence; the continuous model stays exact on the frozen tests.

## 2. Actual arithmetic beyond the rational collars

Set $\mathcal J=\{n:2n\in\mathcal I\}$, $J=|\mathcal J|\asymp\Delta$. Let $\mathcal B=\mathcal B_{B,h}$ be the [orthogonal $J$-point Fourier collar space](r45-operator-fourier-collars.md) (radius $1/(8h)$ around each reduced rational of denominator $\le B$). For the original compression sequence $X(n)=E_{2n}^*T_{2n}E_{2n}$, R45 gives

$$
 \|P_{\mathcal B}X\|_{L^2(\mathrm{HS})}
 \ll_\epsilon BQ^{1/2+\epsilon}M^{3/2}/h+L^{5/2}Y^{-1/5}.
 \tag{4}
$$

Its parameter assumptions hold with $\delta=19/50,\ \delta'=1/4,\ \xi=1/5,\ \gamma=1/40$. We estimate the complementary projection on $\widetilde X$ independently.

For the ordinary primes write $A_V(\alpha)=\sum_x\lambda(x)\rho_V(x)e(x\alpha)$, where $\lambda(p)=\log p$ at primes and otherwise zero, and $e(s)=e^{2\pi i s}$. By Parseval and the elementary Chebyshev bound, $\|A_V\|_{L^2(\mathbb R/\mathbb Z)}\ll\sqrt L$. Each arithmetic alias contribution is a coefficient at $2kn$ of a product $A_V(\pm\alpha)A_U(\pm\alpha)$; signs depend on the orientation. This is exact Fourier inversion on integer $n$ with $N=2n$, with the existing raw coefficient normalization already in $\rho$.

Let $\mathfrak M$ be the torus union of intervals of radius $2P/(qQ)$ around reduced $a/q$ for $q\le P$, and $\mathfrak m$ its complement. By Dirichlet approximation using denominator up to $\lfloor Q/P\rfloor$, every point of $\mathfrak m$ has approximation $a/q$ with $P<q\le Q/P$ and error at most $q^{-2}$. The arcs and complement are symmetric. The [Vaughan bound (Koukoulopoulos, Theorem 23.8)](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=258) is

$$
 \left|\sum_{x\le t}\Lambda(x)e(\alpha x)\right|
 \ll (t/\sqrt q+t^{4/5}+\sqrt{tq})\log^{5/2}(2t).
$$

Apply it uniformly for $t\asymp X_V\ge Q$ to $\mathfrak m$. The prime power difference is $O(\sqrt{X_V}L^2)$, and Abel summation against the bounded-variation weight $\rho_V$ gives $\sup_{\mathfrak m}|A_V|\ll L^c\sqrt{QV/P}$ with a fixed $c$. Here $P\le Q^{1/5}$, so the $t^{4/5}$ term is absorbed. For one alias $k$, the sequence of minor-arc product Fourier coefficients at $2k n$ is a subsampling of the full integer Fourier coefficients with distinct indices. By torus Parseval and the sup bound on one factor, its normalized $L^2(\mathcal J)$ norm is at most $O(L^c\sqrt{QM/(P\Delta)})$, enlarging the fixed log power if needed. Sum over $O(M)$ aliases and the $O(L)$ matrix dimension, absorbing logs into $Q^\epsilon$; the whole minor-arc error is

$$
 O_\epsilon\big(Q^\epsilon M^{3/2}\sqrt{Q/(P\Delta)}\big).
 \tag{5}
$$

This does not require cancellation between the signs.

For the major-arc part, an elementary finite-window leakage bound is useful. For a real frequency $\omega$ and a scalar sequence $w(n)$ on $\mathcal J$ with $\sup|w|+\mathrm{TV}(w)\le A$, Abel summation and the geometric sum give

$$
 \big|\operatorname{Avg}_{n\in\mathcal J} w(n)e((\omega-j/J)n)\big|
 \ll A/(J\|\omega-j/J\|_{\mathbb R/\mathbb Z})
$$

away from the frequency itself. The sum of squared coefficients over grid frequencies at distance at least $c/h$ is $O_c(A^2h/J)$, by comparison of the tail of $\sum_j j^{-2}$ with an integral. On a raw major arc with denominator $q\le P=B$, the frequency $\omega=\pm2k\alpha$ lies within $O(MP/Q)=o(1/h)$ of a rational with denominator at most $B$. Thus every $J$-grid frequency outside the collars is at distance at least $1/(16h)$ from $\omega$, for all large $Q$. By Minkowski and $\int |A_V A_U|\ll L$, the major-arc contribution for each alias outside $\mathcal B$ is $O(L\sqrt{h/\Delta})$. Summing aliases and entries yields

$$
 O_\epsilon\big(Q^\epsilon M\sqrt{h/\Delta}\big).
 \tag{6}
$$

No arithmetic major-arc expansion or main term has been assumed here.

## 3. The exact model also has small leakage

For each alias define $I_k(N)=\int \rho_V(x)\rho_U(m(x,N))\,dx$ with the appropriate orientation. By symmetry choose $V\le U$ in this integral. Its supremum is $O(\sqrt{V/U})$, and its total variation as $N$ runs over $\mathcal I$ is

$$
 O\!\left(\Delta\,k\,X_V^{1/2}/X_U^{3/2}\right)=O(1).
$$

This follows from the Lipschitz norm $O(X_U^{-3/2})$ of $\rho_U$, the $x$-range $O(X_V)$, the first weight size $O(X_V^{-1/2})$, and $k\ll U$. R43's exact model divisor expansion is

$$
 \mathfrak S(kN)=\mathfrak S(2k)
    \sum_{\substack{d\mid N,\ d\ {\rm odd\ squarefree}\\(d,k)=1}}a(d),
 \qquad a(d)=\prod_{p\mid d}(p-2)^{-1}.
$$

Uniformly for these $N,k$, the tail $d>B$ in one alias contributes $O_\epsilon(Q^\epsilon/B)$ pointwise: use $a(d)\ll_\eta d^{-1+\eta}$, $d\le 2Q$, and the divisor bound, taking $\eta$ sufficiently small relative to $\epsilon$. The factor $\mathfrak S(2k)$ is also $O_\eta(Q^\eta)$. In the part $d\le B$, expand ${\bf1}_{d\mid 2n}$ into additive phases, with total coefficient mass one for each $d$; each phase has denominator at most $d$. The sum of their coefficient masses after the $a(d)$ weights and $\mathfrak S(2k)$ factor is $O_\epsilon(Q^\epsilon)$. Apply the same finite-window leakage bound to the sequence $I_k(2n)$, whose supremum plus total variation is $O(1)$. The full continuous model outside $\mathcal B$ is thus bounded in $L^2(\mathrm{HS})$ by

$$
 O_\epsilon\big(Q^\epsilon M(\sqrt{h/\Delta}+B^{-1})\big).
 \tag{7}
$$

This retains both model signs, and bounds them separately.

## 4. Summing the actual variance components

Use (4) on the original $X$, and (5)–(7) plus (3) and the prime-power restoration on the complementary projection. All projections are orthogonal contractions on the matrix-valued $L^2$ space. The resulting bound is

$$
 O_\epsilon\!\left(
 Q^\epsilon\left[
 \frac{B\sqrt Q\,M^{3/2}}h
 + M^{3/2}\sqrt{\frac{Q}{P\Delta}}
 +M\sqrt{\frac h\Delta}+\frac MB
 +Q^{-1/2}M\right]
 + L^{5/2}\left[(\Delta/Q)^{1/2}+Y^{-1/5}\right]\right).
$$

For the displayed parameters the first five exponents of $Q$ before $\epsilon$ are at most $-1/80,-1/400,-1/25,-7/40,-19/40$, respectively. The freezing error is $O(L^{5/2}Q^{-1/40})$. Also $MPh/Q\ll Q^{-1/40}$, as used for separating the transmitted major arcs from the collar complement. This proves (1). Unlike the previous rational-frequency results, the modulus complement is estimated on this window range. It is still not a pointwise bound, a theorem for arbitrary spatial tests, or a proof of weak S.
