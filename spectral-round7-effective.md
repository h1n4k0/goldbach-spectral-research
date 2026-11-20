# Round 7 supplement: explicit but conservative height constants

This supplement makes one arithmetic-cross tail bound fully numerical from elementary GRH consequences, without changing the sharper asymptotic bounds in [spectral-round7.md](spectral-round7.md). It does **not** evaluate a fixed-modulus upper bound for the whole operator. Its example quantifies why the conservative fully explicit estimate is not by itself a practical computational substitute for validated, sharply tuned tail bounds.

Use Round 7 notation and assume local GRH(N). Write $d=\|D_{\rm low}\|$ and
$$d_0=\sum_{n\in\mathcal I}\Lambda(n)^2 n^{-1-2\alpha}.$$
Both quantities concern a finite positive Gram on the low prefix; $d$ may be replaced throughout by any certified upper bound. For $H\ge1$ put
$$
 A=\log(4N(H+4)),\qquad c=6L^2,\qquad U=cA+\sqrt{d_0}.
$$
An explicit alternative to the implicit constant in Round 7 (3) is
$$
 0\le\|B_{\rm arith}\|^2-m_H
 \le E_{\rm elem}:=\frac{4d}{H}\bigl(U^2+2Uc+2c^2\bigr). \tag{E}
$$

**Derivation.** For every odd character, $L(z,\chi)$ is nonprincipal and its periodic character sums are bounded by $N$. For $\Re z>0$, Abel summation of its conditionally convergent Dirichlet series gives $|L(z,\chi)|\le N|z|/\Re z$. At $z_0=2+it$, its reciprocal Euler product gives $|L(z_0,\chi)|\ge1/\zeta(2)>1/2$. Take the disk $|z-z_0|<R=3/2-\alpha/4$. It stays in $\Re z>1/2$ and is zero-free under GRH(N), including for imprimitive characters. The analytic branch
$$
 f(u)=\log\bigl(L(z_0+u,\chi)/L(z_0,\chi)\bigr),\qquad f(0)=0,
$$
satisfies $\Re f(u)\le M_t:=\log(4N(|t|+4))$. Integrating the nonnegative real part of $M_t-f$ against the Fourier exponentials on each smaller circle gives Taylor coefficient bound $|f_j|\le2M_t/R^j$ for $j\ge1$. Thus $|f'(u)|\le 2M_tR/(R-|u|)^2$. For $u=-3/2+\sigma$ and $\sigma\in\{\alpha,\beta\}$ the radius margin is at least $3\alpha/4$, giving
$$
 \bigl|L'/L(1/2+\sigma+it,\chi)\bigr|\le6L^2M_t.
$$
This uses no uncomputed zero-count constant. It is deliberately weaker in $L$ than the averaged estimate of the main note.

Use this in Round 7 (1), Cauchy–Schwarz and odd-character orthogonality. The finite subtracted term contributes at most $\sqrt{d_0}\bigl(\sum|b_n|^2\bigr)^{1/2}$. Since $(N/2\pi)\sum|b_n|^2\le d$ for unit low vectors, the Gram tail is bounded by $4d\int_H^\infty(cM_t+\sqrt{d_0})^2dt/t^2$ (two height signs and two boundary lines). Substitute $t=Hv$, use $M_{Hv}\le A+\log v$, and use the values $1,1,2$ for $\int_1^\infty(\log v)^jv^{-2}dv$, $j=0,1,2$. This proves (E). When enclosing the integrals on a finite height rectangle by analytic quadrature, the same elementary proof on the disk of radius $3/2-\alpha/8$ gives $22L^2M_t$ for every displaced real part $\sigma\ge\alpha/2$ in the relevant strip. This makes a wider-panel envelope explicit as well, at the cost of larger constants.

**A bottleneck for this specific error budget.** Take $N=32768$, $a=4/N$. The sole unit prime power in the open low prefix is $3$, and the diagonal compression has rank one, with
$$
 d=6\pi(\log3)^2\int_3^4 v^{-3}(v^{-2\alpha}+v^{-1/4})\,dv>7/16.
$$
The lower inequality uses $\pi>3$, $\log3>1$, and each power factor $>1/2$. Here $L>10$, $c>600$, and $A>11$. Requiring the expression (E) to be at most $0.05^2$ first forces $H>3\cdot10^{10}$, using just $4d(cA)^2/H$. Then $A>30$ and the same inequality requires $H>2\cdot10^{11}$. This is a consequence of demanding that **the explicit majorant** prove absolute cross-norm uncertainty at most $0.05$ by taking its square root. It is not a lower bound on the true tail, an oracle or algorithmic complexity claim, or a determination that $0.05$ accuracy is necessary for a particular Schur decision. No height computation was run at this modulus. The example isolates the loss from a simple universal explicit envelope; effective averaged character bounds or a posteriori estimates could be far sharper.
