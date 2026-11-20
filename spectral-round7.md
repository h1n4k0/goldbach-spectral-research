# Round 7: a polynomial-height certificate for the low-to-high arithmetic Gram

**Status.** This is a quantitative finite-reduction result for the low-to-high arithmetic block separated in Round 6. Its height truncation is one-sided and controls all vectors in the low prefix. It is not a computed numerical upper bound for any particular modulus, and neither a fixed-modulus full-norm certificate nor a proof of S/R follows. The high-to-high block is still an independent obstacle.

Use the normalization and physical unitary coordinates of [Li–Liu](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf) and [spectral-round6.md](spectral-round6.md). Assume local GRH(N) throughout; $L=\log N$, $\alpha=1/L$, $\beta=1/8$, and $w(y)^{-1}=(Ny)^{-2\alpha}+(Ny)^{-2\beta}$. Fix the complete low prefix $0<x<a\le1/2$, with $M=Na\ge1$, and let $\mathcal I$ consist of unit prime powers $n<M$. Endpoint conventions do not affect the operator. Let $B_{\rm arith}$ denote the arithmetic part of the low-to-high block, after the exact diagonal subtraction. The beta model is separate.

## 1. Exact two-line transform for the right Gram

For $n\in\mathcal I$ put
$$
 a_n(m)=\Lambda(m)\bigl(\mathbf1_{m\equiv n\ (N)}
                   -\mathbf1_{m\equiv -n\ (N)}-\mathbf1_{m=n}\bigr),
 \qquad R_n(s)=\sum_m a_n(m)m^{-1/2-s}
 \quad(\Re s>1/2).
$$
Odd-character orthogonality gives its continuation to the Hardy strip as
$$
 R_n(s)=-\frac{2}{\varphi(N)}\sum_{\chi\ {\rm odd}}
     \overline{\chi(n)}\,\frac{L'}{L}(1/2+s,\chi)
       -\Lambda(n)n^{-1/2-s}. \tag{1}
$$
The extra diagonal subtraction in (1) is important: with it, the first possible nonzero $a_n(m)$ has $m\ge N-n>N/2$. Consequently the Round 6 right profile has no support in $y\le a$, and no physical hard cutoff has to be inserted when taking its transform.

In the log variable $u=\log(Ny)$, write $F_n^\flat(u)=e^{-u}\sum_{m\le e^u}a_n(m)\sqrt m$. The raw diagnostic right profile in Round 6 becomes
$$
 r_n(y)=\sqrt N\,y^{-1/2}w(y)^{-1/2}F_n^\flat(\log(Ny)).
$$
The ordinary GRH estimate for the signed character/progression prefix has no principal main term. Partial summation shows $F_n^\flat(u)\ll_N(1+u)^2$ for $u\ge0$; it vanishes for $u<0$. The elementary Laplace integral valid initially at $\Re s>1/2$,
$$
 \int_{\mathbb R}F_n^\flat(u)e^{-su}\,du = \frac{R_n(s)}{1+s},
$$
thus extends by analytic continuation to $\Re s>0$. In particular Plancherel on both boundary lines gives the exact right Gram
$$
 \langle r_i,r_j\rangle
 =\frac{N}{2\pi}\sum_{\sigma\in\{\alpha,\beta\}}\!
       \int_{\mathbb R}
       \frac{R_i(\sigma+it)\overline{R_j(\sigma+it)}}
            {|1+\sigma+it|^2}\,dt, \tag{2}
$$
with transposition if the opposite inner-product matrix convention is used. The factor $N$ follows from $dy/y=du$; the two boundary norms are summed, not averaged. This replaces the raw prime range with only finitely many $L'/L$ combinations once a height error is specified.

## 2. A uniform, positive omitted-tail bound

Truncate (2) at $|t|\le H$ on each boundary. This yields a positive Gram $G_r(H)$ increasing in Loewner order to the true Gram. Absorb the coefficients $c_n=(2\pi/N)\Lambda(n)\sqrt{n/N}$ of the Round 6 rank factorization in the right Gram, and call the resulting finite matrix $G_c(H)$. Let $G_\ell$ be the left Gram. Define
$$
 m_H=\lambda_{\max}(G_\ell^{1/2}G_c(H)G_\ell^{1/2}).
$$
Then for $H\ge1$,
$$
 m_H\ \le\ \|B_{\rm arith}\|^2
 \ \le\ m_H+C\log(2M)\,\frac{\log^2(N(2+H))}{H}. \tag{3}
$$
The constant is absolute. There is no factor equal to the number of low residues. Here is the proof.

For a unit low vector $\xi$, put $b_n=c_n\langle\xi,\ell_n\rangle$. Every $n$ is below $N/2$ and no two active residues are equal or opposite. Odd orthogonality gives
$$
 \mathbb E_{\chi\ {\rm odd}}\left|\sum_{n\in\mathcal I}
                  b_n\overline{\chi(n)}\right|^2=\sum_n|b_n|^2.
$$
By [operator-round4.md §1](operator-round4.md), the average of the squared logarithmic derivatives is $O(\log^2(N(2+|t|)))$ on $\sigma=\alpha$. The same bound on the fixed line $\sigma=\beta$ follows even pointwise in $\chi$ from GRH, comparison with a fixed absolutely convergent line in the completed logarithmic derivative, and the standard local zero count. The finite removed-Euler terms each cost $O(\log N)$ in total by $\sum_{p\mid N}\log p\le L$. Cauchy–Schwarz in the odd-character average of (1) therefore bounds the squared norm of the combined character term by $O(\log^2(N(2+|t|))\sum|b_n|^2)$. For the subtracted diagonal term, apply Cauchy–Schwarz in $n$ and $\sum\Lambda(n)^2n^{-1-2\sigma}\ll L^2$. Thus
$$
 \left|\sum_{n\in\mathcal I} b_n R_n(\sigma+it)\right|^2
 \ll \log^2(N(2+|t|))\sum|b_n|^2.
$$

There is an exact normalization linking the last sum to a positive operator. Let $D_{\rm low}$ be the compression of the paper's exact diagonal to $x<a$. Its atom expansion in physical coordinates is
$$
 D_{\rm low}=\frac{2\pi}{N}\sum_{n\in\mathcal I}
          \Lambda(n)^2(n/N)\,\ell_n\otimes\ell_n,
 \qquad
 \sum_n|b_n|^2=\frac{2\pi}{N}\langle D_{\rm low}\xi,\xi\rangle .
$$
In particular $\|D_{\rm low}\|\ll\log(2M)$. To see the sharper cutoff dependence, it is enough to bound the full diagonal operator with integers $n<M$ only (all other atoms vanish after compression). On either Hardy boundary the raw diagonal vectors $n^{-s}/(1+s)$ have Gram entries
$$
 \frac{\pi(mn)^{-\sigma}}{1+\sigma}
     e^{-(1+\sigma)|\log(m/n)|},
$$
as follows by the Fourier transform of $((1+\sigma)^2+t^2)^{-1}$. Their weights in the diagonal expansion are $\Lambda(n)^2/n$. Applying the weighted Schur test with weights $\Lambda(n)/\sqrt n$ on active indices, the weighted quotient of each row is bounded by $C\sum_{m<M} (\Lambda(m)^2/m)e^{-|\log(m/n)|}$. In each block $j\le\log m<j+1$, Chebyshev gives mass $O(1+j)$, and the exponential factors sum uniformly, yielding $O(\log(2M))$. This proof retains both boundary pieces without integrating a separate unweighted trace.

Inserting the resulting bound $\sum|b_n|^2\ll\log(2M)/N$ into the omitted part of (2) cancels its factor $N$. The tail integral is at most $C\log^2(N(2+H))/H$: for $t=Hz$ use $\log(N(2+Hz))\le\log(N(2+H))+\log z$ and $\int_1^\infty(1+\log^2 z)z^{-2}dz<\infty$. Taking the supremum over all unit low vectors proves (3), including its one-sided sign.

## 3. A sample-count bound for certified quadrature

Height truncation need not be followed by an unquantified point grid. For either boundary, partition $[-H,H]$ into panels of length at most $\alpha/4$. On each panel use a positive-weight Gauss rule exact for degree $P$ (for instance, $\lceil(P+1)/2\rceil$ nodes). The operator-norm error in the low Gram due to such quadrature, using exact node values, is
$$
 O\bigl(2^{-P}\log(2M)L^2\bigr). \tag{4}
$$
Thus for error $\epsilon$ in the squared-norm matrix, the number of required function-sample locations is
$$
 O\left(H L\log\bigl(2+L^2\log(2M)/\epsilon\bigr)\right), \tag{5}
$$
separate from the cost of validated evaluation at these locations. Increasing the quadrature degree reduces (4), not the omitted-height error (3).

To prove (4), fix a unit low vector $\xi$ and use its coefficients $b_n$ from §2. If $t_0$ is a real panel center, consider the holomorphic continuation in $t$ of
$$
  \frac{(\sum_n b_n R_n(\sigma+it))(\sum_n \overline{b_n}R_n(\sigma-it))}
       {(1+\sigma)^2+t^2} .
$$
It equals the quadratic-form integrand on real $t$, since the continued $R_n$ have real Dirichlet coefficients. On $|t-t_0|\le\alpha/2$, the two displaced $\alpha$ real parts both stay between $\alpha/2$ and $3\alpha/2$. The argument of [operator-round4.md §1](operator-round4.md) works uniformly in that interval: comparing an ordinate term at such real part $\rho$ with the term at $2\alpha$ costs at most a constant multiple of $2\alpha/((2\alpha)^2+(t-\gamma)^2)$ at the new **real** height. The beta line stays a fixed distance from the pole line for sufficiently large $N$. The same weighted odd mean square and diagonal comparison therefore apply throughout the disk, with constants uniform in $t_0$. The denominator has magnitude $\gg 1+t_0^2$ there. By §2, the analytic integrand is bounded on the disk by
$$
 C\frac{\log(2M)}{N}\frac{\log^2(N(2+|t_0|))}{1+t_0^2}.
$$
The degree-$P$ Taylor error on the inner panel is at most $O(2^{-P})$ times that envelope by Cauchy's estimates. Exactness on the polynomial, positivity of the weights and their sum equal to the panel length show that the error for its integral is at most twice the length times the maximum Taylor error. Summing panels gives $O(2^{-P}\log(2M)L^2/N)$ before multiplication by $N/(2\pi)$, because the displayed height majorant is integrable with integral $O(L^2)$. The estimate was uniform in $\xi$, so gives (4) as a Hermitian operator-norm bound. Standard validated finite precision must also be included in an implementation; sample count alone supplies neither those enclosures nor the exact constants.

## 4. What this would cost and what it certifies

With a target cross-norm error $L^{-A}$ at fixed $A>0$, the cost in (3) can be made $o(L^{-2A})$ in the **squared** norm by taking $H=L^{2A+3+\varepsilon}$ with fixed $\varepsilon>0$, for arbitrary $M\le N/2$. More precisely the factor $\log(2M)\le L+O(1)$ may be retained. This is polynomial-logarithmic height, whereas obtaining even $L^{-A}$ damping from the direct physical truncation bound in Round 6 wanted $Y\ge \exp(A L\log L)$ before its coefficients were counted. This compares two proved *bounds*, not lower bounds on the real error or on computational complexity. For an R-scale squared-error budget, $\delta_N^2=S(N)L^3/N$, choosing $H$ a sufficiently large multiple of $N\log(2M)/(S(N)L)$ is sufficient up to the constant and a fixed margin, as long as $H$ has at most polynomial size in $N$. With $M$ a power of $N$, this criterion is at height of order $N/S(N)$. Proving the inequality using this conservative tail bound, rather than a sharper a posteriori estimate, entails this much height at R accuracy. A direct evaluator still needs a family average over as many as $\varphi(N)/2$ odd characters and simultaneous accuracy in the finite Gram. Polynomial-logarithmic height does not by itself mean polynomial-logarithmic running time.

On a finite height rectangle, (1) may be evaluated with interval arithmetic via nonprincipal periodic Dirichlet series, independently of a long enumeration of prime powers. For example at $z=1/2+s$ with real part $\sigma'>0$, truncate $L(z,\chi)$ at a multiple $X$ of $N$, so the character partial sum is zero there. Its future partial sums have magnitude at most $N$. The tails have explicit bounds
$$
 |L-L_X|\le N|z|\,X^{-\sigma'}/\sigma',\qquad
 |L'-L_X'|\le NX^{-\sigma'}\Big[\sigma'^{-1}
       +|z|(\sigma'^{-1}\log X+\sigma'^{-2})\Big].
$$
These follow from Abel summation and differentiating its absolutely convergent tail integral. Under local GRH both lines are zero-free. On any fixed compact integration rectangle with positive $s$ real part, subdivision and refinement ultimately separate every required interval for an $L$ denominator from zero, permitting rigorous enclosure of the log derivatives and finite integrals. This elementary series is a baseline, not a fast implementation; faster validated special-function evaluation or Fourier transforms over residues can reduce costs. The constant in (3) would also have to be made numerical for an implemented upper certificate; here it is derived as a uniform mathematical bound and was not tuned or evaluated.

For the whole cross, add the Round 6 beta bound $O(S(N)a)$ when $Na\ge1$; one can make it negligible at a prescribed S scale by taking $a=o(1/h(N))$. Use the exact Schur criterion of [spectral-round6.md §2](spectral-round6.md): a verified $\|C\|\le(1-\eta)t$ together with $\|B\|\le\sqrt\eta\,t$ would certify $\|T_N\|\le t$. Formula (3) makes a comparatively practical route for the low-to-high arithmetic input to that criterion, but supplies neither the high-to-high upper bound on $C$ nor the signed cancellation in the finite matrix $G_\ell^{1/2}G_c(H)G_\ell^{1/2}$ as $N$ grows. There is no asymptotic assertion of S/R.
