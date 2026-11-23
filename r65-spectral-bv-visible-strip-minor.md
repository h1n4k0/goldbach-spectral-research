# The genuine low-LCM slice of the removed strip has a pointwise small signed minor coefficient

**Scope.** In the [pointwise central bridge](r64-spectral-pointwise-major-central-bridge.md), the true squarefree removed strip is one of the two remaining signed minor-arc terms. We remove its actual subrange above the original divisor cutoff and below the Bombieri–Vinogradov level. This is a bound on a signed minor coefficient for every modulus and every central prefix, not a density-one bound. The full arithmetic sum in this subrange is evaluated unconditionally; its separation into major and minor uses the historical Dirichlet GRH prime progression input for the same polynomial-size major arcs as before. The above-level strip, the separate sharp-profile minor term, the exterior, and Hypothesis S remain open.

Let even $N$ be large, $L=\log N$, $D=\sqrt N L^{-B}$, $m=N-n$, $V=[N/3,2N]$ and $e(t)=e^{2\pi it}$. Use $Q=N^{1/1000}$, $\mathfrak M=\bigcup_{q\le Q,\,(a,q)=1}\{\theta=a/q+\eta:|\eta|\le 2Q/N\}$ on the torus, and $\mathfrak m$ its complement. Let $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. For a half-open $I\subset(N/2,9N/16]$ and a left weight $\omega$ of bounded supremum and variation there write $P_{I,\omega}(\theta)=\sum_{n\in I}\lambda(n)\omega(n)e(n\theta)$.

The removed squarefree strip $\Xi_D$ uses $m=abcd$ with all four factors squarefree and pairwise coprime, $\max(ab,ac)>D$, $ab,ac<\sqrt m$, signed by $\mu(b)\mu(c)$ with weight $1-2\log(ac)/\log m$. This is the actual [midpoint product difference](r63-spectral-full-squarefree-crt-strip.md), not an approximate sieve weight. The exact associated LCM is $h=[ab,ac]=abc$. For a second cutoff $H_0=\sqrt N L^{-B_0}$, define $A_{\rm vis}(m)$ by retaining **only** the genuine terms of $\Xi_D(m)$ with $h\le H_0$, zero outside squarefree $m\in V$, retaining all their signs. Let $\widehat A_{\rm vis}(\theta)=\sum_m A_{\rm vis}(m)e(m\theta)$.

**Theorem.** Given any fixed $A>0$ choose $B_0$ sufficiently large (in terms of $A$); then for any fixed $B>B_0$, uniformly on every even $N$ and all exact intervals and weights above,

$$
 \int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A_{\rm vis}(\theta)
               e(-N\theta)\,d\theta=O_{A,B,B_0}(NL^{-A})
                                                                  \tag{1}
$$

using the prime GRH bound in Section 2. In the central Hardy normalization of the earlier bridge, with left weight $\omega_N(u)=w(u/N)\log(N-u)/L$ and multiplier $L/N$, (1) deletes this whole signed strip block to arbitrary fixed log precision (choose $A$ larger first). All its nonzero terms have $D<h\le H_0$, so it is not the low $h\le D$ block of the original sharp product.

## 1. Exact coefficient and unconditional arithmetic density

Because $H_0<\sqrt x$ for all $x\in V$, the strict upper midpoint inequalities are automatic in this slice. Since $\max(ab,ac)=h/\min(b,c)$, the lower strip gate becomes $\min(b,c)<h/D$. For squarefree $h$ set

$$
 W_h(x)=\sum_{\substack{abc=h\\ \min(b,c)<h/D}}
        \mu(b)\mu(c)\left(1-\frac{2\log(ac)}{\log x}\right).
                                                                  \tag{2}
$$

Then $A_{\rm vis}(m)=\mu^2(m)\sum_{h\mid m,\ h\le H_0,\ h\ {\rm sf}}W_h(m)$ on $V$. In particular $W_h=0$ for $h\le D$. Each centered weight has uniformly bounded size and variation on $V$, so $\|W_h\|_\infty+\operatorname{Var}_V W_h\ll\tau_3(h)$. Define the real density

$$
 \mathcal V_N(x)=\sum_{\substack{h\le H_0\\h\ {\rm sf},\ (h,N)=1}}
          \frac{W_h(x)}h
           \prod_{p\nmid Nh}\left(1-\frac1{p(p-1)}\right)
              \qquad(x\in V).                                    \tag{3}
$$

We first prove, unconditionally,

$$
 \sum_{n\in I}\lambda(n)\omega(n)A_{\rm vis}(N-n)
     =\int_I\omega(u)\mathcal V_N(N-u)\,du+O_{A,B,B_0}(NL^{-A}).
                                                                  \tag{4}
$$

Every prime on the actual interval is $>N/2$, so both it and its partner are units modulo $N$. Expand the squarefree mask by $\sum_{s^2\mid m}\mu(s)$ and truncate $s\le S=L^C$. Some $s>S$ must have $s^2\mid m$ wherever the omitted terms can occur, a set of $O(N/S)$ integers; the omitted multiplicity is at most $\tau(m)$. The sum of absolute $h$-weights is at most $O(\sum_{h\mid m}\tau_3(h))=O(\tau_4(m))$. Hence by Cauchy–Schwarz, $\lambda\le L$, and $\tau_4\tau\le\tau_8$, $\tau_8^2\le\tau_{64}$, this error is $O(NL^{33}S^{-1/2})$. The divisor inequalities follow prime by prime from surjectivity of taking row and column sums of a nonnegative array, as for the moments in the squarefree strip proof.

For retained $h,s$ use modulus $\ell_h=[h,s^2]$ in the reduced residue $N$. Partial summation with $W_h(N-u)\omega(u)$ costs $O(\tau_3(h))$ times the maximal prime progression discrepancy $E_{\ell_h}$ up to $N$. Taking $\mathcal L=H_0 S^2$, the sum of errors is at most $S\sum_{\ell\le\mathcal L}\tau_4(\ell) E_\ell$: for fixed $\ell,s$, all candidate $h$ divide $\ell$ and their weights sum to at most $\tau_4(\ell)$. The trivial bound is $E_\ell\ll NL/\ell$ in this range, and hence $\sum_{\ell\le\mathcal L}\tau_4(\ell)^2 E_\ell\ll NL^{17}$ by $\tau_4^2\le\tau_{16}$. Cauchy–Schwarz and [maximal Bombieri–Vinogradov](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=206) then give $O(NL^{-A})$ by first choosing a large log-saving exponent and taking $B_0$ sufficiently large relative to $C$ and it. One can use prime-only $\lambda$: on summing over the moduli the difference from von Mangoldt is $O(\mathcal L\sqrt N L^2)$, absorbed by choosing $B_0$ larger.

Now extend the **model** $s$ sum to infinity. For squarefree $h$ the extra factors of $\varphi([h,s^2])/\varphi(h)$ are $p$ when $p\mid s$ and $p\mid h$, and $p(p-1)$ when $p\mid s$ but $p\nmid h$. Consequently the tail $\sum_{s>S}\mu^2(s)/\varphi([h,s^2])$ is at most

$$
 \frac{S^{-1/4}}{\varphi(h)}
          \prod_{p\mid h}(1+p^{-3/4})\,
          \prod_{p\nmid h}\left(1+\frac{p^{1/4}}{p(p-1)}\right).
$$

The last product converges. Summing $\tau_3(h)$ times the first factor over squarefree $h$ gives $O(L^3 S^{-1/4})$ by the Euler product with local coefficient $3(1+p^{-3/4})/(p-1)$. Choose $C$ sufficiently large for both square errors. On completing the signed $s$ series with $(hs,N)=1$, a prime $p\mid h$ contributes $(1-1/p)/(p-1)=1/p$, a prime $p\nmid Nh$ contributes $1-1/[p(p-1)]$, and a prime dividing $N$ imposes no square restriction on this already unit partner. This gives exactly (3)–(4), including all strict endpoints.

## 2. The same density on the genuine major arcs

Here assume the usual Dirichlet GRH progression bound for $\lambda$ at $q\le Q$, as in the pointwise bridge. No GRH estimate for Möbius is needed in the right leg of this slice. For squarefree $q$ the right major density is

$$
 D_q(x)=\sum_{\substack{h\le H_0\\h\ {\rm sf}}}\frac{W_h(x)}h
       \prod_{p\mid h}(1-1/p)
       \prod_{\substack{p\nmid h\\p\nmid q}}(1-1/p^2)
       \prod_{\substack{p\nmid h\\p\mid q}}(-1/p^2).
                                                                  \tag{5}
$$

Indeed $m=hd$, where $d$ is positive squarefree and $(d,h)=1$. Its progression counts at any residue have their exact CRT density with error $O(\tau(h)\sqrt Y)$ on prefixes of length $Y$, by the $s^2\mid d$ and coprimality expansion in [the squarefree proof](r63-spectral-full-squarefree-crt-strip.md#1-exact-arithmetic-strip-and-major-arc-one-variable-estimates). If $p\mid h$ then $d$ is a unit at $p$ and the rational phase at $p\mid q$ is one, giving $1-1/p$ in either case. If $p\nmid h$ and $p\mid q$, the squarefree unit mass $1-1/p$ is multiplied by $-1/(p-1)$ as the mean phase on units, and the valuation-one mass $(1-1/p)/p$ has phase one, giving $-1/p^2$. If $p\nmid hq$ its squarefree mass is $1-1/p^2$. These products are independent of the reduced numerator. Crucially, the actual right coefficient has **not** been changed to impose $(h,N)=1$ on the Fourier leg.

With $d\asymp N/h\gg\sqrt N$ and $q\le Q$, sum the residue errors and partially sum the true centered coefficient and slow phase. The total error in $\widehat A_{\rm vis}(a/q+\eta)$ is at most

$$
  O_\epsilon\!\left(Q^2N^\epsilon
                    \sum_{h\le H_0}\sqrt{N/h}\right)
                =O_\epsilon(Q^2N^{3/4+\epsilon}).
$$

Here $\tau(h)\tau_3(h)\ll_\epsilon N^\epsilon$, and $O(Q)$ bounds the slow variation. Thus this genuine major polynomial equals $\int_V D_q(x)e(\eta x)\,dx$ to a power error. For nonsquarefree $q$ it is enough to use the trivial right bound, since the left prime main factor is zero. The genuine left major approximation has the factor $\mu(q)/\varphi(q)$ times the transform of $\mathbf1_I\omega$, with error $O_\epsilon(N^{1/2+\epsilon}Q^2)$ by GRH, partial summation and the residue sum.

The completed major evaluation has power error uniformly in $N$. To see this directly, (5) has supremum and variation $O(L^3 C_1^{\omega(q)}/q)$ extended by zero off $V$: for each $p\mid q$ either $p\nmid h$ and its factor saves $O(p^{-2})$ relative to its unconstrained factor, or $p\mid h$ which saves $3/p$ in the reciprocal sum with $\tau_3(h)$. Expanding these choices leaves the ordinary squarefree $\tau_3$ harmonic bound $O(L^3)$. Thus the two variations extend the Fourier integrals with error $O(N Q^{-1}L^3(\log(2Q))^{C_2})$. The local polynomial errors above multiplied on arcs of total length $O(Q^3/N)$ also save a fixed power. For the rational tail the same pointwise estimate as in the central bridge gives
$\sum_{q>Q}C_1^{\omega(q)}|c_q(N)|/(q\varphi(q))\ll_\epsilon Q^{-1/4}N^\epsilon$ on squarefree $q$. This follows from $|c_q(N)|\le(q,N)$ and absolutely convergent Euler factors except for the finite $N$-prime product, bounded by $N^\epsilon$. Together these give error $O(N^{1-10^{-4}})$ in the completed major integral.

To complete its density, multiply (5) by $\mu(q)c_q(N)/\varphi(q)$ and sum squarefree $q$. At $p\mid h$ the resulting local factor is $(1-1/p)(1-c_p(N)/(p-1))$, zero for $p\mid N$ and one otherwise. At $p\nmid h$ it is $(1-1/p^2)+c_p(N)/(p^2(p-1))$, equal to one on $p\mid N$ and $1-1/[p(p-1)]$ otherwise. The $1/h$ in (5) is unchanged. This is **exactly** (3), pointwise for every $N$; the finite set of nonunit $h$'s vanish in the model rather than being removed from the Fourier leg. Subtract the actual major evaluation just proved from the full genuine convolution (4). The result is (1).

## 3. A nontrivial signed response of the same arithmetic slice

The visible block is not identically negligible as the cutoffs vary. The completed density gives a definite cutoff response on every modulus. Define
$\mathcal A_N=\prod_{p\nmid N}(1-1/[p(p-1)])$,
$\beta_p=(1-1/[p(p-1)])^{-1}/p$ for $p\nmid N$ and zero otherwise, and $R_\beta(u)=\sum_{k\le e^u}\mu(k)\beta(k)$ with multiplicative squarefree weights. Put $H_0=DL^R$ for a fixed $R=B-B_0>0$ and $T=R\log L$. Keep the $\alpha$, $P_N$, $R_{N,j}$ of the [squarefree strip formula](r63-spectral-full-squarefree-crt-strip.md). Define finite signed moments

$$
 Q_{N,T}=\sum_{\substack{j\le e^T\\j\ {\rm sf}}}
       \mu(j)\alpha(j)^2\int_0^{T-\log j}R_{N,j}(u)^2du,\qquad
 J_{N,T}=\sum_{\substack{j\le e^T\\j\ {\rm sf}}}
       \mu(j)\alpha(j)^2\left(\int_0^{T-\log j}R_{N,j}(u)\,du\right)^2 .
$$

Then (3) has the explicit formula uniformly on $V$, with arbitrary fixed log saving,

$$
 \mathcal V_N(x)=
     -\frac{2}{\log x}
       \left[
        \mathcal A_N\int_0^T R_\beta(u)\,du+
        \Sigma(N)P_N\left(\Delta(x) Q_{N,T}-\frac12J_{N,T}\right)
        \right]+O_{A,B,B_0}(L^{-A}).
                                                                  \tag{6}
$$

Here is a derivation which uses only bounded positive-factor counts at scale $\sqrt N$ and retains the finite signed moments at their true scale. In (2) write the condition $\min(b,c)<h/D$ as the union of $b<h/D$ and $c<h/D$. Since $D>1$, the sum with $b<h/D$, $c$ unrestricted is zero by summing $\mu(c)$ over divisors of $h/b$. In the other one-sided sum its constant centered part is likewise zero, and $\sum_{b\mid h/c}\mu(b)\log b$ vanishes unless $h/c$ is prime, when it equals $-\log(h/c)$. Inclusion–exclusion therefore gives the exact expression

$$
 W_h(x)=
  -\frac{2}{\log x}\sum_{\substack{p\mid h\\p>D}}\mu(h/p)\log p
  -\!\!\sum_{\substack{bc\mid h,\ (b,c)=1\\b,c<h/D}}
       \mu(b)\mu(c)\left(1-\frac{2\log h-2\log b}{\log x}\right).
                                                                  \tag{7}
$$

First use the prime marginal with $h=kp$, $k\le e^T$ and $D<p\le H_0/k$. The upper and lower limits are of polynomial size in $N$, while $k$ is polylogarithmic. Ordinary PNT by partial summation gives
$\sum_{D<p\le H_0/k,\ p\nmid Nk}\beta_p\log p
=\log(H_0/(kD))+O_A(L^{-A})$ uniformly in $k$. The Euler factor in $\beta_p$ can be removed there with a power error, and the finitely many $p\mid N$ in this range are also negligible. The first contribution to (6) follows since the remaining sum $\sum_{k\le e^T}\mu(k)\beta(k)(T-\log k)$ is $\int_0^T R_\beta$. No unproved estimate on that **finite** cumulative is used.

For the second term of (7), fix the two factors $b,c\le e^T$ and sum over $a=h/(bc)$ on $D\max(b,c)<abc\le H_0$, with $(a,bcN)=1$ and $a$ squarefree. Its lowest endpoint is at least $N^{.49}$ for large $N$. Put $U_p=(1-1/[p(p-1)])^{-1}$ on $p\nmid N$. The summatory density of $\mu^2(a)\mathbf1_{(a,bcN)=1}\prod_{p\mid a}U_p$ is $\prod_p(1-1/p)\prod_{p\nmid bcN}(1+U_p/p)$, interpreted jointly at each prime. The power error follows by convolution with $1$: outside $bcN$ the local kernel has $k(p)=O(p^{-2})$, $k(p^2)=O(1)$, higher entries zero, and on occupied primes only $k(p)=-1$. Its moment $\sum |k(a)|a^{-3/4}\ll_\epsilon(Nbc)^\epsilon$ permits the real integral by partial summation, with a uniform power error also after summing $b,c$ in their reciprocal weights. Including $\mathcal A_N$ and the occupied reciprocals, the constant is exactly $\Sigma(N)P_N$ times $\alpha(b)\alpha(c)$: for $p\nmid N$, multiplying the local factor of $\mathcal A_N$ and $(1-1/p)(1+U_p/p)$ gives $1-2/p^2$, while the occupied relative reciprocal is $U_p/(p+U_p)=\alpha_p$. For $p\mid N$ the factor is $1-1/p$, agreeing with $\Sigma(N)P_N=(\varphi(N)/N)\prod_{p\nmid N}(1-2/p^2)$.

Under $u=\log(abc/D)$ the range is $\max(\log b,\log c)<u\le T$, and the centered weight is $2(\Delta(x)-u+\log b)/\log x$. Expand $(b,c)=1$ by the common divisor $j$, writing $b=jb'$, $c=jc'$; the outer coefficient is $\mu(j)\alpha(j)^2$ and the remaining arrays are both cut at $t=u-\log j$ and prime to $j$. Partial summation gives the signed log-$b$ moment as $uR_{N,j}(t)-\int_0^tR_{N,j}$, including the $\log j$ shift. Thus the two integrands after the product are
$\Delta(x)R_{N,j}(t)^2-R_{N,j}(t)\int_0^tR_{N,j}$.
Integration over $0\le t\le T-\log j$ gives the two terms $Q_{N,T}$ and $-J_{N,T}/2$ in (6). Endpoints of the real integral are insensitive to individual jump values, while the discrete endpoints were kept in (7).

Finally $Q_{N,T}\gg1$ uniformly for $T\ge\log3$. As in the squarefree positivity proof, excluding $j$ convolves the primitive with a positive forward log kernel of mass $\prod_{p\mid j}(1-\alpha_p)^{-1}$. On the truncated half-line norm, each forward shift is contractive, so the total absolute contribution of $j>1$ to $Q_{N,T}$ is at most
$\|R_{N,1}\|_{L^2(0,T)}^2[\prod_{p\ge3}(1+(p-1)^{-2})-1]$, strictly less than its $j=1$ term. Also $R_{N,1}=1$ on $[0,\log3)$. In particular, choose two fixed exponents $B_2>B_1$, with the same $R>0$ and each $B_i-R$ large enough for the BV argument, and define $D_i,H_i$ accordingly. All finite moments in (6) are unchanged, while $\Delta_2-\Delta_1=(B_2-B_1)\log L$. Therefore the visible arithmetic sum for $(D_2,H_2)$ minus that for $(D_1,H_1)$ is

$$
 -2(B_2-B_1)(\log L)\,\Sigma(N)P_N Q_{N,T}
                    \int_I\frac{\omega(u)}{\log(N-u)}\,du
       +O_A(NL^{-A}).
$$

On any original cell of length $N/(16\lceil L^J\rceil)$ with $J$ fixed, at weight $1$ and with $A>J+1$ chosen first, this is strictly negative for large $N$ and of magnitude at least a constant times $|I|/L$, by $\Sigma(N)P_N\asymp\varphi(N)/N\gg1/\log L$. This cutoff comparison changes both cutoffs at fixed ratio $L^R$; it is not an assertion about varying $D$ at a fixed $H_0$, nor about the sign of the full untruncated strip. It confirms that (1) deletes a genuine signed arithmetic component whose full size need not be small.
