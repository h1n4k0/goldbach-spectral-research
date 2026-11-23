# A positive signed boundary term at the sharp midpoint cutoff

**Scope.** This evaluates the first nonzero boundary term of the sharp mixed-product model and transfers it to the genuine cut. The sharpening at the previously proved subpower roughness is unconditional. The extension to a fixed polylogarithmic least-prime threshold uses only the ordinary Riemann hypothesis for the Riemann zeta function, and in fact only a fixed power-saving ordinary prime number theorem. No Dirichlet GRH is used. Every arithmetic asymptotic below is simultaneous over the original central cells on almost all even moduli. There is no claim about an individual exceptional modulus, the residual below the new threshold, an absolute mass bound, or Hypothesis S.

For even $N\in[X,2X]$ put $L=\log N$, $\ell=\log X$, $m=N-n$, and $\lambda(n)=(\log n)\mathbf1_{n\ \mathrm{prime}}$. Write $\Sigma(N)$ for the binary singular series and use the original half-open cells $I\subset (N/2,9N/16]$ of length $H=N/(16\lceil L^J\rceil)$, where $J\ge1$ is fixed. Fix $B>0$ and retain the actual divisor threshold $D_N=\sqrt N L^{-B}$ and coefficients

$$
 F_{0,D}(m)=\sum_{\substack{d\mid m\\d\le D}}\mu(d),\qquad
 F_{1,D}(m)=\sum_{\substack{d\mid m\\d\le D}}\mu(d)
                \left(1-\frac{2\log d}{\log m}\right),\qquad
 G_D(m)=F_{0,D}(m)F_{1,D}(m)-F_{0,D}(m).
$$

Here $F_{0,D}$ and $G_D$ are the [low and high LCM terms](spectral-midpoint-lcm-complement-frontier.md), respectively. With the squarefree-partner restriction initially understood, write $T_0(z;I,N)$ and $T_{\rm hi}(z;I,N)$ for their sums against $\lambda(n)$ on $n\in I$ with $P^-(N-n)\ge z$. Define

$$
 c_* = 2e^{-2\gamma_{\!E}}\int_0^\infty \rho(v)^2\,dv >0,
$$

where $\gamma_{\!E}$ is Euler's constant and $\rho$ is the Dickman function.

**Unconditional refinement.** For fixed $C>2$ and $z_C(N)=\exp((\log L)^C)$, for every fixed $A_0>0$ there are $O_{B,J,C,A_0}(X\ell^{-A_0})$ exceptional even moduli such that on every cell of each remaining modulus,

$$
 \begin{split}
 T_0(z_C;I,N)&=O\!\left(\frac{\Sigma(N)H}{L^2}\right),\\
 T_{\rm hi}(z_C;I,N)&=\frac{\Sigma(N)H}{L}
   \left(1+c_*B(\log L)^{1-C}+O((\log L)^{-C})\right).
 \end{split}                                                     \tag{1}
$$

In particular, for fixed $2<C_1<C_2$ the genuine intervening shell $z_{C_1}(N)\le P^-(m)<z_{C_2}(N)$ contributes **positively** to the signed high term: it is asymptotic to $c_*B(\log L)^{1-C_1}\Sigma(N)H/L$ on the common good set. The earlier proof gave an upper bound of that size, without an asymptotic or a sign.

**Conditional polylogarithmic extension.** Under ordinary RH, fix $A_0>0$, and choose a fixed $K$ sufficiently large in terms of $A_0,J,B$ as made explicit in Section 3. For $z=L^K$, on every cell outside $O_{B,J,A_0,K}(X\ell^{-A_0})$ exceptional even moduli,

$$
 \begin{split}
 T_0(L^K;I,N)&=O\!\left(\frac{\Sigma(N)H}{L^2}\right),\\
 T_{\rm hi}(L^K;I,N)&=\frac{\Sigma(N)H}{L}
   \left(1+c_*\frac{B}{K}+O\!\left(\frac{1}{\log L}\right)\right).
 \end{split}                                                     \tag{2}
$$

For any fixed $C>2$, the newly reached shell $L^K\le P^-(m)<z_C(N)$ therefore has genuine signed high sum asymptotic to $c_*(B/K)\Sigma(N)H/L$. Its low sum is $O(\Sigma(N)H/L^2)$. In both (1) and (2) and the associated shell statements, dropping the squarefree gate changes only the stated error terms.

## 1. Signed boundary calculation in the continuum

Use the [Dickman convolution measures](spectral-midpoint-odd-aggregate-dickman.md) $K_b(dt)=\mathbf1_{t\ge b}dt/t$, $\mathcal B_b=\exp_*(K_b)$, and $\mathcal M_b=\exp_*(-K_b)$, as in the [direct sharp-cut transfer](spectral-midpoint-direct-sharp-subpower-cut.md). Write $f_{+,b}$ for the non-atomic density of $\mathcal B_b$ and set it to zero on nonpositive arguments. The original low and product models at normalized threshold $\nu$ are

$$
 \begin{split}
 \mathcal L_b(\nu)&=\int_{[0,\nu]}\mathcal M_b(du)\,f_{+,b}(1-u),\\
 \mathcal P_b(\nu)&=\int_{x+y\le\nu,\,x+v\le\nu}
       \mathcal B_b(dx)\mathcal M_b(dy)\mathcal M_b(dv)\,
       \bigl(1-2(x+v)\bigr)f_{+,b}(1-x-y-v).
 \end{split}                                                     \tag{3}
$$

The high model is $\mathcal P_b-\mathcal L_b$. The full midpoint simplex identity gives $\mathcal P_b(1/2)=1$. Also $\mathcal L_b(1/2)$ and $\mathcal L_b(1/2-ab)$ are smaller than every power of $b$ as $b\downarrow0$, uniformly for bounded $a\ge0$. Indeed the full-midpoint low in the [complementary-block evaluation](spectral-midpoint-complementary-blocks-moving-roughness.md) has a Dickman factorial bound, and the extra strip meets $u\ge2/5$ for small $b$. There the negative density of $\mathcal M_b$ is $-\rho(u/b-1)/u$ and $f_{+,b}\le1/b$, so removing the strip costs less than every power of $b$. In fact both low estimates are exponentially small in $1/b$ by the same factorial bounds.

Let $\omega=f_{+,1}$. The recurrence $t\omega(t)=\mathcal B_1([0,t-1])$ implies $0\le\omega\le1$, and $\omega(t)=1/t$ on $1<t<2$. Where $t>2$ is not an integer, $t\omega'(t)=\omega(t-1)-\omega(t)$. The function is locally absolutely continuous above $1$. If $D_j$ is the essential supremum of $|\omega'|$ on $[j,j+1]$, the last identity gives $D_j\le j^{-1}\max(D_{j-1},D_j)$ for $j\ge3$, since $[t-1,t]$ is in the union of those two intervals. Hence $D_j\le D_{j-1}/j$ and $\omega$ converges to a limit $c_\infty$ with exponentially small error. To identify it, the Laplace transform gives

$$
 s\int_0^\infty e^{-su}\omega(u)\,du
       =s\left(\exp\!\left(\int_1^\infty e^{-su}\frac{du}{u}\right)-1\right)
       \longrightarrow e^{-\gamma_{\!E}}
       \quad(s\downarrow0).
$$

This uses the [exponential-integral expansion at zero](https://dlmf.nist.gov/6.6.E2); bounded convergence applied after the change of variable $w=su$ identifies the same limit with $c_\infty$. For the signed measure $M=\mathcal M_1$, the cumulative mass is $M([0,u])=\rho(u)$, the whole mass is zero, and $|M|$ has bounded first moment and factorial tails. These facts follow directly from the Dickman density in the cited convolution proof.

Here is the new boundary estimate, uniformly for $0\le a\le A$ with $A$ fixed:

$$
 \mathcal P_b(1/2-ab)=1+c_*a+O_A(ae^{-c/b}) \qquad (b\downarrow0). \tag{4}
$$

Set $t=1/b$ and rescale all three variables in (3) by $b$, writing them again as $x,y,v$. Convolution measures become $\mathcal B_1,M,M$, and the remaining density contributes the factor $t$. Set $r=\max(y,v)$ and $s_0=\min(y,v)$. The set removed in $\mathcal P_b(1/2)-\mathcal P_b(1/2-ab)$ is exactly the strip $t/2-r-a<x\le t/2-r$ in the integration over $x\ge0$, understood with the actual weak cutoff; an equality at a nonzero boundary has zero measure here. At $x=t/2-r-u$ with $0\le u\le a$, the remaining exponent is $t/2-s_0+u$. The weight multiplied by $t$ is exactly $2(r-v+u)$.

For the density part of $\mathcal B_1$, restrict first to $r\le t/8$. Both $\omega$ factors are then at arguments at least $3t/8-A$. They equal $e^{-\gamma_{\!E}}+O_A(e^{-ct})$, uniformly, and the entire width $a$ is present. On the discarded tail $r>t/8$, the integral, even with clipped width, has absolute value $O_A(ae^{-ct})$: use $\omega\le1$, strip width at most $a$, weight at most $2(y+v+A)$, and the factorial tails of $|M|\otimes|M|$. The atom $x=0$ requires $r\in(t/2-a,t/2]$. At least one of $y,v$ is in this tail interval, whose absolute $M$-mass is at most $a$ times the supremum of its factorially small density there; the other coordinate has absolute mass at most two. With weight bounded by $O_A(t)$ here, the atom likewise costs $O_A(ae^{-ct})$. These estimates include $a$ tending to zero; at $a=0$ the difference is exactly zero.

Extending the truncated $y,v$ integral to all nonnegative coordinates costs another $O_A(ae^{-ct})$. Thus the removed contribution is

$$
 2e^{-2\gamma_{\!E}}\iint M(dy)M(dv)\int_0^a (r-v+u)\,du
       +O_A(ae^{-ct}).
$$

The term in $u$ is zero because $M$ has total mass zero. The signed first moment has the opposite sign from its unsigned integrand:

$$
 \iint (y-v)_+\,M(dy)M(dv)
   =\int_0^\infty M((w,\infty))\,M([0,w])\,dw
   =-\int_0^\infty \rho(w)^2\,dw.
$$

Both uses of signed Fubini are justified by the finite first moment of $|M|$ and its finite mass. The removed term is therefore $-c_*a+O_A(ae^{-ct})$. Subtracting it from the full value $1$ proves (4), with the indicated positive sign at the **smaller** divisor cutoff.

## 2. Unconditional application at the subpower gate

The [direct sharp-cut transfer](spectral-midpoint-direct-sharp-subpower-cut.md), Sections 2–3, evaluates the exact arithmetic terms by $\Sigma(N)\int_I a(N-u)\,du+O(\Sigma(N)H/L^2)$, with local densities $\mathcal L_b(\nu)/\log x$ and $(\mathcal P_b(\nu)-\mathcal L_b(\nu))/\log x$. Its one-coordinate product comparison, removal of the small-largest region, and arithmetic restoration have the displayed $O(\Sigma(N)H/L^2)$ accuracy for fixed $C>2$. Here each frozen piece uses $b=\log z_C(N_0)/\log x$ and $\nu=\log D_{N_0}/\log x$, and $x$ lies in the real second interval $V=[X/3,2X]$. With the mesh and parameters of that proof,

$$
 a=\frac{1/2-\nu}{b}
    =\frac{B\log\log N_0+\tfrac12\log(x/N_0)}{(\log\log N_0)^C}
    =B(\log L)^{1-C}+O((\log L)^{-C})
$$

uniformly. This is positive for large $X$. Since $\log x=L+O(1)$ and the low model is negligible, (4) gives (1). Subtraction on the intersection of the two good sets proves the asserted shell sign; all exceptions remain $O(X\ell^{-A_0})$.

## 3. Polylogarithmic extension and the exact extra input

Assume the ordinary RH through [von Koch's prime number theorem error](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5070-11511_2006_Article_BF02403071.pdf#page=24), $\pi(u)-\mathrm{Li}(u)\ll\sqrt u\log u$. The following checks give the direct transfer at $z=L^K$ without changing the definition of the sharp arithmetic coefficient.

* First choose $E=A_0+4J+40$, and $C_0=10(E+1)$ for the major-arc cutoff $Q=\ell^{C_0}$. Then any fixed $K>2C_0+2J+100$ suffices. The $O(\ell^{2J+12})$ frozen tests, minor sup $O(X\ell^{-E})$ from Vaughan with denominator $Q\le q\le X/Q$, and $O(X\ell^{15})$ squared second torus norm give at most $O(X\ell^{31+4J-2E})$ minor exceptions at threshold $X\ell^{-J-2}$, as in the earlier direct proof. The absolute Ramanujan-tail mean $O(XQ^{-1/2})$, at threshold $\ell^{-6}$, gives $O(X\ell^{6-C_0/2})$ exceptions. Both are smaller than the required exception bound. In the Fourier tail on the retained arcs, the factor $b_0^{-5}/\ell$ is $O(\ell^4)$, where $b_0=\log z/\ell$ for a frozen $z$. The tail $O(X\ell^4/Q)$ times the sum of absolute truncated coefficients stays negligible: that sum is at most $\sum_{q\le Q}\varphi(q)^{-1}\ll\log(2Q)$. Thus the circle transfers have the same error tolerance as in the unconditional proof.
* On a frozen piece the least prime exceeds $Q$ because $K>C_0$, and the temporary largest prime $p$ exceeds $y=\exp(\ell/(\log\ell)^2)\gg Q$. All prefixes and the final prime are therefore units on the small major moduli. Ordinary Siegel–Walfisz for the final prime, with the original cofactor variation bounds and $\log p\gg\ell/(\log\ell)^2$, still gives arbitrarily many log savings on those arcs. The major Fourier density, small-largest deletion by Rankin and fourth divisor moments, and continuum small-largest deletion are unchanged. The prefix Euler and Fourier variation bounds need only $b_0^{-1}\ll\ell$, which holds. In particular, no Dirichlet GRH is inserted in the major-arc step.
* The new use of RH is solely for the interval discrepancy of the reciprocal-prime measure above the frozen $z$. Partial summation against $u^{-1}$ gives, uniformly for intervals in the range $p\ge z$,

$$
 \left|\sum_{p\in[u,v]}p^{-1}-\int_u^v\frac{dw}{w\log w}\right|
       \ll z^{-1/2}(\log z)^2\qquad(v\ge u\ge z).
$$

The same holds for all endpoint conventions since an endpoint atom costs at most $z^{-1}$. The two measures in the ordered-prefix Stieltjes comparison have common mass upper bound $M_0\le\log(1/b_0)+O(1)$. From the earlier one-coordinate bound $O(4^k/b_0)$, factorial summation makes the full loss at most $O(b_0^{-1}e^{4M_0})=O(b_0^{-5})$; the repeated-prime cost is $O(b_0^{-5}/z)$ by the two-coordinate collision sum. Consequently the entire discrepancy in the **normalized** $\ell a(x)$ is $O(b_0^{-5}z^{-1/2}(\log z)^2)=o(\ell^{-1})$ for the chosen $K$. The cutoff in this comparison is still the exact affine inequality corresponding to $d\le D$. Any fixed-power error $\pi(u)-\mathrm{Li}(u)\ll u^{1-\delta}(\log u)^C$ in place of RH would work with $K$ enlarged in terms of $\delta$.
* Moving $z=(\log N)^K$ on a piece of mesh width $\delta_0=X\ell^{-J-12}$ changes it by relative size $O_K(\delta_0/X)$; the true weighted error $O_K(X\ell^4(\delta_0/X+1/z))$ is $O(H/L^2)$ at the chosen $K$. Moving $D$ and the cell endpoints is covered by the earlier hyperbola bounds independently of this change. After dropping the squarefree gate, the true partners that can be added to either test have some squared prime at least $z^2$ dividing $m$. Counting them by $O(N/z)$ and using the fourth divisor moment gives the same $O(NL^{17/2}/\sqrt z)$ weighted error as in the earlier proof. Since $K>2J+21$, this is $O(H/L^2)$. The unconditional assertion about dropping the gate follows from the identical bound at $z_C$.

Thus the actual low and high correlations are again given by the two densities in Section 2 with an additive $O(\Sigma(N)H/L^2)$, uniformly in every central cell of the common good set. Now on a frozen piece

$$
 \frac{1/2-\nu}{b}
       =\frac{B\log\log N_0+\tfrac12\log(x/N_0)}{K\log\log N_0}
       =\frac{B}{K}+O_K((\log L)^{-1}).
$$

Here $b\asymp_K(\log L)/L$, so the exponentially small remainders of Section 1 stay negligible. Formula (4), $\log x=L+O(1)$, and the circle transfer give (2). Subtracting (1) on the common good moduli proves the stated conditional shell asymptotic. In particular the new shell does not have negligible signed high mass relative to $\Sigma(N)H/L$ for fixed $B,K$: its main term is the genuine additive boundary term of the sharp cutoff rather than an error bound.
