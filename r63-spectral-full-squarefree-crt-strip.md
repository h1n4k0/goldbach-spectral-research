# The genuine sharp midpoint strip on all squarefree partners

**Scope.** This removes the least-prime cutoff on the squarefree branch of the actual sharp central high/low LCM moment. Its new term is an explicit positive, modulus-dependent quadratic expression obtained from the exact squarefree congruence factors. The claim is unconditional and almost-all, simultaneously over the original cells; it does not estimate nonsquarefree partners, a prescribed exceptional modulus, or Hypothesis S. Importantly, the new positive term is a signed **composite cutoff correction**, not an additional Goldbach representation count.

Fix $B>0$, $J\ge1$, and $A_0>0$. For even $N\in[X,2X]$ put $L=\log N$, $\ell=\log X$, $D_N=\sqrt N L^{-B}$, and $H=N/(16\lceil L^J\rceil)$. Use the original half-open cells $I\subset(N/2,9N/16]$ of length $H$, $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$, and $m=N-n$. Let $\Sigma(N)$ be the usual binary singular series. The coefficients are the actual

$$
 F_{0,D}(m)=\sum_{\substack{e\mid m\\e\le D}}\mu(e),\qquad
 F_{1,D}(m)=\sum_{\substack{f\mid m\\f\le D}}\mu(f)
              \left(1-\frac{2\log f}{\log m}\right),\qquad
 G_D=F_{0,D}F_{1,D}-F_{0,D}.
$$

For a prime $p$ set

$$
 U_p=1+\frac{c_p(N)}{(p-1)^2},\qquad V_p=1-\frac{c_p(N)}{p-1},
 \qquad r_p=\frac{V_p}{U_p},\qquad
 \alpha_p=\frac{r_p}{p+2r_p},\qquad
 P_N=\prod_p(1-1/p)^2(1+2r_p/p),
                                                                  \tag{1}
$$

where $c_p(N)=p-1$ if $p\mid N$ and $-1$ otherwise. Then $r_p=0=\alpha_p$ on $p\mid N$, and otherwise $p\ge3$, $r_p=(p-1)/(p-2)$ and $\alpha_p=(p-1)/(p^2-2)<1/p$. Define $\alpha(h)=\prod_{p\mid h}\alpha_p$ on squarefree $h$, with $\alpha(1)=1$; values off squarefree are immaterial. For each squarefree $j$ put

$$
 R_{N,j}(t)=\sum_{\substack{h\le e^t\\(h,j)=1}}\mu(h)\alpha(h),
 \qquad
 \mathcal Q_N=\sum_{j\ {\rm squarefree}}\mu(j)\alpha(j)^2
                       \int_0^\infty R_{N,j}(t)^2dt,
 \qquad \mathcal D_N=P_N\mathcal Q_N .
                                                                  \tag{2}
$$

All terms are absolutely summable in (2) after taking the absolute value of the outer coefficient, and uniformly for even $N$,

$$
        c(\varphi(N)/N)^2\le \mathcal D_N\le C.
                                                                  \tag{3}
$$

Outside $O_{A_0,B,J}(X\ell^{-A_0})$ even moduli, in **every** original cell of each remaining modulus,

$$
 \begin{split}
 \sum_{\substack{n\in I\\m\ {\rm squarefree}}}
       \lambda(n)F_{0,D_N}(m)
    &=O\!\left(\frac{\Sigma(N)H}{L^2}\right),\\
 \sum_{\substack{n\in I\\m\ {\rm squarefree}}}
       \lambda(n)G_{D_N}(m)
    &=\Sigma(N)\int_I
       \frac{1+2\mathcal D_N\left(\frac12\log(N-u)-\log D_N\right)}
            {\log(N-u)}\,du
        +O\!\left(\frac{\Sigma(N)H}{L^2}\right).
 \end{split}                                                       \tag{4}
$$

In particular the high term is its prime baseline plus the positive sharp-cut correction $2B\mathcal D_N(\log L)\Sigma(N)H/L$ with relative $O(1/\log L)$ error **in the correction**. The original fully squarefree residual below $L^K$ is consequently evaluated by subtracting the [unconditional polylogarithmic theorem](r62-spectral-unconditional-polylog-strip.md) for any fixed eligible $K$, on the common good moduli.

## 1. Exact arithmetic strip and major-arc one-variable estimates

On squarefree $m>1$ the [full strict midpoint parity identity](spectral-midpoint-parity-signed-transport.md) makes the product at the midpoint equal $\mathbf1_{m\ {\rm prime}}$. For $m\in V=[X/3,2X]$ and each cutoff $D=\sqrt{N_0}(\log N_0)^{-B}$ frozen as in the [direct-cut proof](spectral-midpoint-direct-sharp-subpower-cut.md), $D<\sqrt m$ for large $X$. As in the [polylogarithmic strip argument](r62-spectral-unconditional-polylog-strip.md), the removed strip on squarefree $m$ is exactly

$$
 \Xi_D(m)=
 \sum_{\substack{abcd=m\\ab<cd,\ ac<bd\\a\max(b,c)>D}}
       \mu(b)\mu(c)\left(1-\frac{2\log(ac)}{\log m}\right),
 \qquad
 G_D(m)=\mathbf1_{m\ {\rm prime}}-F_{0,D}(m)-\Xi_D(m).
                                                                  \tag{5}
$$

Indeed $a$ is the gcd of the two divisor labels and $b,c$ their exclusive parts. Here and throughout Sections 1–4 the right arithmetic sequences are zero on nonsquarefree partners. In (5) all four variables are therefore squarefree and pairwise coprime: no collision deletion is made. $\Xi_D,F_{0,D}$ are bounded in absolute value by $\tau_4(m)$, with $\sum_{m\le2X}\tau_4(m)^2\ll X\ell^{15}$, by the ordered-divisor moment from the polylogarithmic proof.

For any fixed $\delta>0$, $Y\ge X^\delta$, $q\le\ell^{C_0}$, and $w\le2X$ the following two facts apply, with arbitrary logarithmic saving for Möbius and a power saving for the squarefree count.

First, $\sum_{d\le Y,\ d\equiv u(q),\ (d,w)=1}\mu(d)\ll_{A,\delta,C_0}Y\ell^{-A}$ uniformly in all residues $u$. Use the exact convolution of $\mu$ with the indicator of integers supported on primes dividing $w$ to impose coprimality. In its convolution parameter $h\le\sqrt Y$, the linear congruence $hv\equiv u(q)$ is either empty or one class modulo $q/(h,q)$. Apply the ordinary [Möbius Siegel–Walfisz estimate in arbitrary residue classes](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/higher-uniformity-of-arithmetic-functions-in-short-intervals-i-all-intervals/6DF08E2A3EFABB2DD0DA6CDA38649B18), equation (1.13), at length $Y/h$. The total reciprocal factor for $h$ is at most $w/\varphi(w)\ll\log\log(4X)$. For $h>\sqrt Y$, a trivial count and Rankin with exponent $1/4$ give at most $Y^{1-1/8}\prod_{p\mid w}(1-p^{-3/4})^{-1}\ll_\epsilon Y^{1-1/8}w^\epsilon$, negligible after choosing $\epsilon$ small in terms of $\delta$. The Euler bound follows since each sufficiently large local factor is at most $p^\epsilon$.

Second, the count of squarefree $d\le Y$ with $(d,w)=1$ in any class $u\bmod q$ is $Y$ times the exact local density plus $O(\tau(w)\sqrt Y)$. Expand $\mu^2(d)$ by squared divisors $v^2\mid d$ and coprimality by $h\mid(d,w)$. Each compatible count has modulus $[q,h,v^2]$ and floor error $O(1)$. There are $O(\tau(w)\sqrt Y)$ retained pairs and the absolutely convergent main-term sum over omitted $v>\sqrt Y$ has the same error, since $[q,h,v^2]\ge v^2$. This proves the stated local density by CRT and Euler factorization. Both facts hold on all subintervals with endpoints comparable to $Y$, and with weights by partial summation. The second error is a power saving for $Y\ge X^\delta$ since $\tau(w)\ll_\epsilon X^\epsilon$.

## 2. Exact squarefree bulk densities with the additive phase

Freeze the target pieces and the first intervals as in the direct-cut proof, and let $q\le Q=\ell^{C_0}$, $(h,q)=1$, $|\eta|\le2Q/X$. On the right it is enough to compute the major density for squarefree $q$: for nonsquarefree $q$ the first prime polynomial has zero main term by Siegel–Walfisz, and the right polynomial has trivial bound $O(X\ell^3)$ from $\tau_4$.

Split (5) into $b>X^{1/10}$, $c>X^{1/10}$ with $b\le X^{1/10}$, and the bulk $b,c\le X^{1/10}$. In either of the first two regions keep the other three variables fixed, imposing their exact squarefree and cross-coprime conditions, and sum the signed large variable with coprimality to their product. Its admissible set is an interval: the two midpoint conditions are one lower and one upper bound in the variable, and $a\max(b,c)>D$ is automatic or one lower bound. The other physical and sector cuts are intervals too. The logarithmic factor is bounded by one and monotone there (the ratio $\log(ac)/\log(abcd)$ is nondecreasing in $c$ and nonincreasing in $b$). The phase $e(\eta abcd)$ contributes $O(1+Q)$ variation. The first estimate of Section 1, after summing its fixed residue classes for the rational phase and the other factors' reciprocals, gives $O_A(X\ell^{-A})$ for every fixed $A$ on these large signed sectors. For a nonempty admissible interval the chosen variable is $\ge X^{1/10}$ and comparable to $X$ divided by the fixed product; thus the preceding power cut hypotheses apply even when the interval itself is short.

In the bulk, retain $(b,c)=1$ and their actual signs. The geometry gives $a>D/\max(b,c)>X^{.39}$ and $d>\sqrt m/\min(b,c)>X^{.39}$ for large $X$. Keep $a,b,c$ fixed subject to their squarefree and pairwise coprime conditions and count $d$ by the second estimate of Section 1 with $w=abc$. At $p\nmid abc$, the unweighted local factor is $1-1/p^2$ when $p\nmid q$. When $p\mid q$, the additive phase averaged on the unit classes of $d$ is $-1/(p-1)$; it is one on the class divisible by $p$. The respective squarefree local masses are $1-1/p$ and $(1-1/p)/p$, giving the combined factor $-1/p^2$. At $p\mid abc$, $d$ must be a unit and the rational phase contribution is one when $p\mid q$. Thus the factor is $1-1/p$ for $p\mid abc$ independent of $q$. These local formulas result from additive CRT for squarefree $q$ and are independent of its reduced numerator.

After this count write $x=abcd$ as the real variable, remaining $a$ on $D/\max(b,c)<a<\sqrt x/\max(b,c)$ exactly. To justify averaging its multiplicative density, write the $d$ main coefficient as

$$
 D_q\!\prod_{p\mid abc}b_p(q),\qquad
 D_q=\prod_{p\nmid q}(1-p^{-2})\prod_{p\mid q}(-p^{-2}),\qquad
 b_p(q)=\frac{1-1/p}{(1-p^{-2})\mathbf1_{p\nmid q}-p^{-2}\mathbf1_{p\mid q}} .
                                                                  \tag{6}
$$

For fixed $b,c$, the function of $a$ to average is
$g(a)=\mu^2(a)\mathbf1_{(a,bc)=1}\prod_{p\mid a}b_p(q)$. Write $g=1*k$. Away from $qbc$, $k(p)=b_p(q)-1=O(1/p)$ and $k(p^2)=-b_p(q)=O(1)$ with no higher powers. At $p\mid bc$ only $k(p)=-1$ survives, and at remaining $p\mid q$ the nonzero terms are $O(p^2)$. Hence

$$
 \sum_{a\ge1}\frac{|k(a)|}{a^{3/4}}
           \ll_\epsilon q^{C}(bc)^\epsilon,\qquad
 \sum_{a\le Y}g(a)=Y\sum_{a\ge1}\frac{k(a)}a
                   +O_\epsilon(Y^{3/4}q^C(bc)^\epsilon).
                                                                  \tag{7}
$$

The first claim follows from the absolutely convergent Euler factors outside $qbc$, the bound $\prod_{p\mid bc}(1+p^{-3/4})\ll_\epsilon(bc)^\epsilon$, and harmless polynomial factors in $q$. The second follows by the floor error and the tail of the main series. Applying (7) by partial summation to $a^{-1}(1-2\log(ac)/\log x)$ on the stated interval, whose minimum is $>X^{.39}$, gives a power saving even including the prefactor $D_q\prod_{p\mid bc}b_p(q)$, which is $O(q^2)$. The derivative of that weight is $O(a^{-2})$ on its support. The $d$-count errors likewise sum to a power saving after choosing $\epsilon$ sufficiently small and summing the other factors' reciprocals. In detail, for each triple they are $O((X/(abc))^{1/2}X^\epsilon(1+Q))$ while $X/(abc)\gg X^{.39}$ when the interval is nonempty, so comparison with $X/(abc)$ gains a power prior to the $O(\ell^3)$ reciprocal sum.

Let $W_q(bc)$ denote the resulting product of local density factors of $a,d$, with $b,c$ fixed squarefree and coprime. It is
$(1-1/p)^2$ at $p\mid bc$, and otherwise the $p$-factor is

$$
 (1-1/p)^2
 \begin{cases}
  1+2/p,&p\nmid q,\\
  -1/(p-1)+2/p,&p\mid q.
 \end{cases}
                                                                  \tag{8}
$$

These formulas can be checked by the two valuations of $a$: for unit $a$ the above $d$ local factor applies; for $v_p(a)=1$ the $d$ factor is $1-1/p$, with rational phase one even if $p\mid q$. Both share the mass $(1-1/p)$ of a unit $a$, and its mass is $(1-1/p)/p$ when $v_p(a)=1$. Formula (8) includes $p=2$; the second case there is zero.

Consequently the right strip polynomial on the retained major arcs is $\int_V A_{\Xi,q}(x)e(\eta x)\,dx+O_A(X\ell^{-A})$ with no extra numerator factor, where

$$
 A_{\Xi,q}(x)=
 \sum_{\substack{b,c\le X^{1/10}\\(b,c)=1}}\frac{\mu(b)\mu(c)}{bc}
       W_q(bc)
       \int_{D/\max(b,c)}^{\sqrt x/\max(b,c)}
               \left(1-\frac{2\log(ac)}{\log x}\right)\frac{da}{a}.
                                                                  \tag{9}
$$

All local endpoint inequalities were used before the continuum integration; the real interval endpoints have zero measure. For the low $F_{0,D}$ use $m=bd$, $b\le D$ signed and $d\gg X^{.49}$ for large $X$, squarefree coprime to $b$. Its corresponding density $A_{\mathrm{lo},q}(x)$ is independent of $x$ in $V$, with local $d$ factors $1-1/p$ at $p\mid b$, and $1-1/p^2$ or $-1/p^2$ respectively at $p\nmid b$, depending on whether $p\nmid q$ or $p\mid q$. This is precisely the earlier $d$ calculation with (6) and no $a$ average.

## 3. Complete the actual arithmetic circle transfer

The first polynomial has major factor $\mu(q)/\varphi(q)$ multiplying the Fourier transform of $\mathbf1_{I_0}$, where $I_0$ is the frozen first interval. Hence summing the reduced numerators introduces $\mu(q)c_q(N)/\varphi(q)$ for (9) and its low counterpart. We justify taking the complete $q$ series before computing the local factors.

Uniformly in $D$, the strip integral in (9) has supremum and variation on $V$ of order $O_B(1+\log\ell)$, by the length in $\log a$ and the explicit smooth expression obtained setting $\log a=\tfrac12\log x-\log\max(b,c)-s$. Its length is $\tfrac12\log x-\log D=O_B(1+\log\ell)$, and the derivative of the integral is $O_B((1+\log\ell)/X)$ uniformly. Each local factor outside $q$ has total product bounded above, by $(1-1/p)^2(1+2/p)=1+O(p^{-2})$ and the bounded changes at $p\mid bc$ (which only decrease this factor). At $p\mid q$ with $p\nmid bc$ its size is $O(1/p)$ relative to the outside-$q$ factor. When $p\mid bc$, the reciprocal sum with this prescribed occupation gains $2/p$: for any set of prescribed distinct primes, split each uniquely between the two factors because $(b,c)=1$, and sum remaining reciprocal weights at cost $O(\ell^2)$. Expanding the two choices gives the uniform bound

$$
 {\rm Var}(A_{\Xi,q})+\|A_{\Xi,q}\|_\infty
   +{\rm Var}(A_{\mathrm{lo},q})+\|A_{\mathrm{lo},q}\|_\infty
       \ll \ell^3\,C_2^{\omega(q)}/q\qquad(q\ {\rm squarefree}),
                                                                  \tag{10}
$$

with extension by zero off $V$. For the low term the same bound follows by prescribed occupation in just one factor and the stronger $p^{-2}$ at unoccupied $p\mid q$. The analogous prime baseline has right factor $\mu(q)/\varphi(q)$ and density $\mathbf1_V/\log x$ as usual.

By the exact divisor identity for Ramanujan sums, $\sum_{N\le2X}|c_q(N)|\le2X\tau(q)$. Uniformly across all pieces, the mean absolute tail of the combined densities past $Q$ is at most $O(X\ell^3Q^{-1/2})$, using (10) and convergence of
$\sum_{q\ {\rm squarefree}} C_2^{\omega(q)}\tau(q)q^{1/2}/(q\varphi(q))$. The same budget covers the prime series. Markov at $\ell^{-2}$ costs $O(X\ell^5 Q^{-1/2})$ exceptions. The Fourier tail from extending each retained major arc integral to the real line is at most $O(X Q^{-1}\ell^3(\log(2Q))^{C_3})$, by (10), the two variations, $|c_q(N)|\le\varphi(q)$, and $\sum_{q\le Q} C_2^{\omega(q)}/q\ll(\log(2Q))^{C_3}$ (bound by the Euler product over primes $\le Q$). All uniform individual major errors are superlogarithmically small after taking their arbitrary saving sufficiently large.

For completeness the minor arcs have genuine left sup $O(X\ell^{-E})$ by Vaughan, with $E=A_0+4J+40$, $Q=\ell^{C_0}$ and $C_0=10(E+1)$, as in the direct-cut proof. The right $L^2$ square is $O(X\ell^{15})$. Bessel, threshold $X\ell^{-J-2}$, and the $O_J(\ell^{2J+12})$ frozen first intervals give a union of $O(X\ell^{31+4J-2E})$ exceptions for the three tests. These bounds prove that the actual correlations on the common good set equal the integrals over $I_0$ of the combined densities at $x=N-u$, up to $O(\Sigma(N)H/L^2)$. The first and second variables stay inside their required central ranges as in the direct-cut proof. Absolute convergence of the complete series for fixed $N$ and fixed finite $b,c$ also holds (the potentially exceptional primes dividing $Nbc$ are finite; for all other primes the factor increment is $O(p^{-2})$). Thus it is legitimate both to form the combined density and to factor it below.

## 4. The local coefficients and the signed quadratic term

At a prime $p$, if the product $m$ is a unit, the contribution from including $p$ in $q$ multiplies its local mass by $c_p(N)/(p-1)^2$. If $m$ is divisible by $p$, the contribution multiplies it by $-c_p(N)/(p-1)$. In each case add the term in which $p$ is absent from $q$, giving $U_p,V_p$ of (1). Equivalently these follow by multiplying the second case of (8) by $-c_p(N)/(p-1)$ and adding its first case. Thus at $p\nmid bc$ the combined $a,d$ factor is $(1-1/p)^2(U_p+2V_p/p)$, and for $p\mid bc$ it is $(1-1/p)^2 V_p$. The standard product $\prod_p U_p=\Sigma(N)$ includes $p=2$ because $N$ is even. After factoring $\Sigma(N)P_N$, the remaining product on occupied $b,c$ has factor $r_p/(1+2r_p/p)$ per occupied prime, which with the existing $1/(bc)$ is exactly the $\alpha$ weight of (1). The local $p\mid N$ gives no occupied contribution. For $p\nmid N$ the non-$\Sigma$ factor in $P_N$ is $1+O(p^{-2})$ and uniformly positive; for $p\mid N$ it is $(1-1/p)^2$. This proves $P_N\asymp(\varphi(N)/N)^2$.

For the low moment the corresponding combined constant outside occupied primes is $\Sigma(N)\prod_p (1-1/p)(1+r_p/p)$. The non-$\Sigma$ product is bounded by an absolute constant by the same Euler check. Each occupied prime in the signed $b$ gets $\widetilde\alpha_p=r_p/(p+r_p)$ including its reciprocal weight, zero if $p\mid N$ and $(p-1)/(p^2-p-1)=1/p+O(p^{-3})$ otherwise. The actual combined low density is therefore this outside constant times $\sum_{b\le D}\mu(b)\widetilde\alpha(b)$. It is $O_A(\Sigma(N)\ell^{-A})$ for every fixed $A$ by the convolution estimate below; that argument applies unchanged to these $\widetilde\alpha_p$.

For the strip let $T=\ell/10$, $\Delta(x)=\frac12\log x-\log D$. For $b,c\le e^T$ the integral in (9) is exactly

$$
 \frac{2}{\log x}
    \left(\Delta(x)(\log b-\log c)_++\tfrac12\Delta(x)^2\right).
                                                                  \tag{11}
$$

This follows by substituting $\log a=\tfrac12\log x-\log\max(b,c)-s$, $0\le s\le\Delta(x)$. The signed total mass in (11), with $(b,c)=1$, is $O_A(\ell^{-A})$, and its first signed moment is $-\mathcal Q_N+O_A(\ell^{-A})$, as we now prove.

Given a prime coefficient array $\beta_p$ with $\beta_p=0$ on primes dividing an integer $w$ and $\beta_p=1/p+O(p^{-2})$ otherwise, the sequence of weights $\mu(h)\beta(h)$ is the additive log convolution of $\mu(h)/h$ with the Euler kernel having local generating factor $(1-\beta_p Z)/(1-Z/p)$. For the arrays in this proof the absolute mass of that kernel is $O(w/\varphi(w))$, because outside $w$ the absolute nonconstant mass is $O(p^{-2})$. The kernel's absolute moment after multiplying by $h^{1/4}$ is $O_\epsilon(w^\epsilon)$, by the convergent product outside $w$ and $\prod_{p\mid w}(1-p^{-3/4})^{-1}\ll_\epsilon w^\epsilon$. The [ordinary Mertens reciprocal estimate](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287), Eq. 6.18, bounds the log cumulative of the original $\mu(h)/h$ by $O(e^{-c\sqrt t})$ for $t\ge1$. The convolved cumulative $R_\beta$ therefore has $L^1,L^2$ norms $O(w/\varphi(w))$ by the shift and triangle inequalities. Splitting the kernel at $\log h\le t/2$ gives, for $t\ge2$,

$$
 |R_\beta(t)|\ll (w/\varphi(w))e^{-c\sqrt t}
                    +O_\epsilon(w^\epsilon e^{-t/8}).
                                                                  \tag{12}
$$

This proves uniform superlogarithmic pointwise and integrated tails at $t\ge\ell/20$ for $w\le X^{1.1}$ with a fixed sufficiently small $\epsilon$ (a fixed factor in the bound on $w$ is harmless).

Expand $\mathbf1_{(b,c)=1}=\sum_{j\mid b,c}\mu(j)$. Writing $b=j b'$, $c=j c'$, $\mu(b)\mu(c)\alpha(b)\alpha(c)$ becomes $\alpha(j)^2\mu(b')\mu(c')\alpha(b')\alpha(c')$ with each remaining variable coprime to $j$; their logarithmic difference is unchanged. For $j\le e^{T/2}$ apply (12) with $w=Nj$, and cutoff $T-\log j\ge\ell/20$. The signed total for this $j$, before its outer $\mu(j)\alpha(j)^2$, is $R_{N,j}(T-\log j)^2$ and negligible. The signed first moment at this cutoff is

$$
 R_{N,j}(T-\log j)\int_0^{T-\log j}R_{N,j}(t)\,dt
          -\int_0^{T-\log j} R_{N,j}(t)^2\,dt.
                                                                  \tag{13}
$$

Use signed Fubini on the finite rectangle via $\log c'\le t<\log b'$. The first term in (13) is negligible and the second may extend to infinity by (12). The discarded $j>e^{T/2}$ contribution to the original truncated sums is exponentially small by $\alpha(j)^2\le j^{-2}$ and the trivial remaining harmonic sums $O((1+T)^2)$ with the extra weight $O(T)$ if needed. For the infinite moment, the $L^2$ bound in terms of $Nj/\varphi(Nj)$ shows its same discarded tail is negligible, since $j/\varphi(j)\ll_\epsilon j^\epsilon$. These checks prove the claimed signed first moment and total and the absolute convergence of (2). The argument with $w=N$ and $\beta_p=\widetilde\alpha_p$ also proves the asserted low estimate because $\log D\gg\ell$.

Finally excluding the primes of $j$ from $R_{N,1}$ is convolving its primitive with the positive log kernel $\prod_{p\mid j}(1-\alpha_p Z)^{-1}$. Its absolute mass is $\prod_{p\mid j}(1-\alpha_p)^{-1}$. Thus the absolute contribution of $j>1$ to $\mathcal Q_N$ is at most $\|R_{N,1}\|_2^2$ times

$$
 \prod_{p\ge3}\left(1+\left(\frac{\alpha_p}{1-\alpha_p}\right)^2\right)-1
       \ \le\ \exp\!\left(\sum_{n\ge3}(n-1)^{-2}\right)-1\ <\ 1.
                                                                  \tag{14}
$$

Here $\alpha_p<1/p$ on the active primes and $p=2$ is excluded because $N$ is even. The last strict inequality is $\zeta(2)-1<\log 2$. Therefore $\mathcal Q_N$ is bounded below by an absolute positive multiple of $\|R_{N,1}\|_2^2$, which in turn is at least $\log 3$ since $R_{N,1}=1$ on $0\le t<\log3$. The same estimates bound it above by an absolute multiple of the norm square, and (12) gives $\|R_{N,1}\|_2\ll N/\varphi(N)$. This proves (3).

The combined strip density is now $-2\Sigma(N)\mathcal D_N\Delta(x)/\log x+O_A(\Sigma(N)\ell^{-A})$ by (11)–(13), with a minus sign. The prime baseline is $\Sigma(N)/\log x$ and the low density negligible. Subtracting the strip in (5) proves the frozen form of (4). Restore the true $D_N$ and interval endpoints with the hyperbola and divisor moment bounds of the direct-cut proof, Section 2, unchanged by keeping squarefree partners and no roughness cutoff. The errors are $O(H/L^2)$; (3) also bounds the small continuum endpoint/cut changes. This proves (4). On the actual cell, $\Delta(N-u)=B\log L+O(1)$, while $\mathcal D_N\gg(\varphi(N)/N)^2\gg(\log L)^{-2}$. Thus the $O(\Sigma(N)H/L^2)$ error is smaller than the asserted signed correction by the stated relative margin. No claim here concerns the nonsquarefree branch or individual moduli.
