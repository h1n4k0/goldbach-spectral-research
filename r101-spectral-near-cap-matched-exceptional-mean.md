# The matched exceptional mean near the original denominator cap

**Scope.** This extends the bounded matched signed mean of the **actual exceptional mixed-strip correction** to larger Page conductors, including combined sampling moduli above the original denominator cap. The finite arithmetic model is unchanged; an algebraic completion has an explicit tail, which is small under the stated logarithmic margin. The conclusion is conditional on an actual sufficiently close Page zero. It does not establish that such a zero exists, does not control individual targets, and says nothing about positivity of the full signed shell, the whole mixed-strip coefficient, a prime-pair count, or Weak S. Neither Dirichlet GRH nor an external zero-gap theorem is used.

Adopt the dyad and genuine sectors $\mathfrak E_\pm$ of [the matched Ramanujan mean](r100-spectral-matched-ramanujan-exceptional-mean.md), with $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $Y\le N\le2Y$ even, and the actual primitive real Page conductor $r\le Q_0$, character $\chi$, and simple real zero $\beta>1-4a_0/\sqrt G$. Suppose the zero exists, and impose $(1-\beta)G\le C_*\log G$ with $C_*$ fixed. Keep the original fixed admissible $B>B_0>0$, and the same common scaled half-open left interval $I_N=NJ$, $J\subset(1/2,9/16]$, with bounded-BV left and target weights $w,\eta$. Use the literal complete planting $K=K_z=\prod_{p\le z}p$, fixed on the dyad, with $2\le z\le Z$. Define

$$
 M=[r,K],\quad K'=\prod_{\substack{p\le z\\p\nmid r}}p,\quad
 R=Q_0/r,\quad \ell=\log z,\quad
 \theta=\frac{\log\log G}{2\ell},\quad
 \Xi=\mathbf1_{M>Q_0}\exp(-\theta\log R).
 \tag{1}
$$

Here $M=rK'$ exactly and $M=Y^{o(1)}$ throughout. There is no hypothesis $M\le e^{2Z}$ or $M\le Q_0$. As before write $r=2^e r_{\rm odd}$, with $e=0,2,3$ and $r_{\rm odd}$ squarefree; let $D=r_{\rm odd}/(r_{\rm odd},K)$, $P=M/K$, $\tau_0=\tau_2=1,\ \tau_3=1/2$ and $\gamma(N)=c_r(N)/\varphi(r)$. Let $\langle\cdot\rangle_K$ be the original normalized signed mean with the fixed $\eta$ on all multiples of $K$, and $\mathbb E_P$ the exact average over $m\bmod P$. For any function $\psi$ on those classes put $H_\psi=\mathbb E_P[\psi(m)\gamma(Km)]$ and $L_\psi=\mathbb E_P|\psi(m)|$.

Use $\widetilde P_i(M)$ for precisely the completed real integrals (without the exceptional sign or parity half) from [the aligned cap formula](r96-spectral-aligned-mean-euler-collapse.md) with its local coefficients at sampling modulus $M$:

$$
 \widetilde P_i(M)=\frac1Y\int_Y^{2Y}\eta(v/Y)
    \int_{v-x\in vJ}
     \frac{w((v-x)/v)(v-x)^{\beta-1}x^{\beta-1}}{\log x}\,
           \mathcal A_i(v,x)\,dx\,dv,\qquad i=0,1 .
 \tag{2}
$$

The two real caps in this definition retain the original $U_v=(B-B_0)\log\log v$, $T_{v,x}=2B\log\log v+\log(x/v)$ and the original hard geometry. Only the arithmetic denominator completion may now have a tail.

**Theorem.** With fixed $C$ one has

$$
 \begin{split}
 \left\langle \psi(N/K)\mathfrak E_\pm(N)\right\rangle_K
  ={}& -\tfrac12\chi(-1)H_\psi
                  \{\widetilde P_0(M)\pm\widetilde P_1(M)\}\\
    &+O\!\left(Y^\beta G^C r^{-1/2}L_\psi
             +Y^{2\beta-1}G^C\Xi\,|H_\psi|\right).
 \end{split} \tag{3}
$$

The algebraic second error is absent when $M\le Q_0$. Even when $M>Q_0$, this error is proportional to the **signed response** $|H_\psi|$, not to the mean modulus of the test.

For the conditional lower bound take the matched $\psi(m)=\gamma(Km)$, fixed nonnegative tests with $\int_Jw>0,\ \int_1^2\eta>0$, and $z\ge A_0\log G$ for a sufficiently large fixed $A_0$. Either require $M\le Q_0$, or assume for a sufficiently large fixed $A_1$ that

$$
           \log(Q_0/r)\ \ge\
                       A_1\frac{(\log G)\log z}{\log\log G}.
 \tag{4}
$$

Then for sufficiently large such dyads

$$
 -\chi(-1)\left\langle
       \gamma(N)\{\mathfrak E_+(N)-\mathfrak E_-(N)\}
                    \right\rangle_K
 \ \gg\ 
     \frac{\tau_e}{\varphi(D)}
     \left(\int_Jw\right)\left(\int_1^2\eta\right)
     \frac{Y^{2\beta-1}}{G}\,\frac{M}{\varphi(M)(\log r)^4}.
 \tag{5}
$$

The constants may depend on the fixed tests, cutoffs, threshold and $C_*$. The fixed-power comparison involving the classical conductor growth is ineffective. No lower bound on $\tau_e/\varphi(D)$ is required.

## 1. The actual finite model on each class is still the same

Start with the [all-target Ramanujan formula](r94-spectral-all-target-ramanujan-exception.md), which holds for every true even target with error $O(Y^\beta G^C r^{-1/2})$. On the $P$ genuine classes $N\equiv a\pmod M$, $a=Km\bmod M$, take the same normalized BV sample as in the matched mean. Since $\log M\le\log r+\sum_{p\le z}\log p=O(Z)$, each has $O(Y/M)$ points, and all arithmetic errors in the original R100 Section 1 sampling argument retain their original orders. In detail a finite constraint $d\mid N$, $d\mid q\mid t$, has squarefree $d$ and $(d,r)=1$. Every prime of $(d,M)$ divides $K$, so it is compatible with the class. The intersection is one translate modulo $[M,d]$ and its normalized BV continuum multiplier is $(M,d)/(dY)$, independent of $a$. The factor $\gamma(N)$ is exactly $\gamma(a)$ on this class. The physical profile and absolute coefficient bounds of [the complete signed-mean projection](r95-spectral-complete-planting-signed-mean.md) give the same error with factor $(M/Y)rQ_0^{O(1)}=Y^{-1+o(1)}$ multiplying $Y^\beta G^{O(1)}$, absorbed by the original $r^{-1/2}$ error. None of these sampling estimates required $M\le e^{2Z}$ once the pointwise arithmetic formula is restricted to its original denominators $rt\le Q_0$.

Thus there are two **common** normalized algebraic integrals $B_i(M;R)$, for colors $i=0,1$, before multiplication by $\gamma(a)$ and taking the parity half-sum. Define their convention as in (2): the sign $-\chi(-1)$ and half are outside, and the common prefactor inside is $r/(\varphi(r)L'(\beta,\chi)^2)$. Their denominator labels still satisfy $t\le R$, $(t,r)=1$ and short labels $u_1,u_2\le S=Y^{1/10}$ are mutually coprime and squarefree, exactly as in [the two-pole geometry and weights](r92-spectral-aligned-exceptional-two-pole-formula.md). The arithmetic factors are those of the local formula there with divisibility averaged as one for $p\mid M$ and $1/p$ elsewhere, exactly as in R95 (2). The BV discretization is the only step replacing sampled target profiles by real ones, so these common integrals include the literal moving hard geometries. No estimate for prime or Möbius progressions at denominator $rt>Q_0$ has been invoked.

## 2. The added tail costs a reciprocal denominator even on occupied primes

For $p\nmid r$ put $c_p=\chi(p)p^{-\beta}$, $E_p=(1-c_p)^{-1}$ and let $h=u_1u_2$. Sum over all $q\mid t$ for each original squarefree $t$, using the exact contraction $(l_{p,0}-p\,\overline l_{p,1})/(p-1)$ at $p\mid t$ from R96 Section 1. Here $l_{p,0}$ and $\overline l_{p,1}$ are the unoccupied and averaged occupied $q$ factors. The contraction is zero at every $p\nmid M$ regardless of whether it divides $h$, because $\overline l_{p,1}=l_{p,0}/p$. Thus only $t\mid K'$ can occur. At a surviving $p\mid t$, the divisibility factor is one and the two cases give exactly

$$
 \frac{l_{p,0}-p\,\overline l_{p,1}}{p-1}
    =
  \begin{cases}
     -E_p^2,&p\mid h,\\
     E_p^2\bigl((p-1)^{-1}+2c_p\bigr),&p\nmid h .
  \end{cases}
 \tag{6}
$$

There is no division by an unoccupied local factor, including at $2$. Since $p\le z$, $p^{1-\beta}\le e^{(1-\beta)\ell}=1+o(1)$. Consequently the absolute bound at $p\mid t$ is $O(1)$ on $p\mid h$ and $O(1/p)$ otherwise. The remaining local factors outside $t$ have absolute product $G^{O(1)}$ uniformly in $h$: away from $h,r$ they are $1+O(p^{-2\beta})$, and at $p\mid h$ they are $E_p^2$, for $h\le Y^{1/5}$. The latter product is $G^{O(1)}$ by splitting its primes at $G^2$ and using $1-\beta=O(G^{-1/2})$ and $\log h\le G/5$. This argument takes absolute products and allows zero factors.

Extend the common algebraic denominator sum to **all** $t\mid K'$, solely as a formal finite operation on the averaged two-pole weights. Its added part has $t>R$. For each such $t$, by (6), after including the two short weights and bounding the factors outside $t$, the absolute arithmetic sum is at most a fixed polylogarithmic factor times

$$
 \frac{C_1^{\omega(t)}}t
  \sum_{\substack{u_1,u_2\le S\\(u_1,u_2)=1}}
    (u_1u_2)^{-\beta}\!
     \prod_{p\mid t}\bigl(1+(p-1)\mathbf1_{p\mid u_1u_2}\bigr).
 \tag{7}
$$

The other short restrictions have been harmlessly dropped for this upper bound. Expand the product as a sum over $d\mid t$. Because $d$ is squarefree and $u_1,u_2$ are mutually coprime, the condition $d\mid u_1u_2$ splits into at most $2^{\omega(d)}$ assignments $d=d_1d_2$, $d_i\mid u_i$. For any assignment its absolute reciprocal cost is at most $d^{-\beta}(\sum_{n\le S}n^{-\beta})^2$, and $\sum_{n\le S}n^{-\beta}\ll G^{1+C_*/10}$ by the assumed closeness. Including the coefficient $\prod_{p\mid d}(p-1)\le d$ in this expansion costs at most $\prod_{p\mid t}(1+2p^{1-\beta})\ll C_2^{\omega(t)}$. Thus (7) is $\ll G^{C_3}C_4^{\omega(t)}/t$. The physical integrals divided by $Y$ contribute at most $Y^{2\beta-1}G^{O(1)}$, since $x,v-x\asymp Y$ and the true hard geometric kernels are polynomially bounded in $G$. The common prefactor $r/(\varphi(r)L'(\beta,\chi)^2)$ is $G^{O(1)}$ by the same reciprocal derivative bound as in R92 and elementary Euler estimates.

If $M\le Q_0$ then $K'\le R$ and there are no added terms. Otherwise, the positive Rankin bound for the tail at $\theta$ in (1) is

$$
 \sum_{\substack{t\mid K'\\ t>R}}\frac{C_4^{\omega(t)}}{t}
   \le R^{-\theta}\prod_{p\mid K'}(1+C_4p^{-1+\theta})
   \le R^{-\theta}\exp\!\bigl(O((\log G)^{1/2}\log\log G)\bigr).
 \tag{8}
$$

Indeed $p^\theta\le z^\theta=(\log G)^{1/2}$ and $\sum_{p\le z}p^{-1}\ll1+\log\log(2z)\ll\log\log G$. This Euler cost is $G^{o(1)}$. For each color the true finite-model error after algebraic completion is therefore $\ll Y^{2\beta-1}G^C\Xi$ and is the **same common quantity on every residue**, before multiplication by $\gamma(a)$.

## 3. Comparison with the completed cap and the matched bound

Summing all $t\mid K'$ puts back the exact local R96 products: at $p\mid M$ outside $r$ the sum of the two occupancies is $pE_p^2/(p-1)$ if $p\nmid h$, and zero if $p\mid h$. Outside $M$ the formal coefficients therefore remain $\alpha_p^M=c_p/(1-2c_p)$, and on $M$ they vanish, with the exact prefactor of R96 (2). This completion is finite even when $M>Q_0$; it is solely the estimator compared with the true finite common model in (8).

We record the only modulus checks for converting this completed estimator to (2). The R96 exponential shift moment with $\delta=1/8$ is at most $\exp(O(G^\delta))$ on the $M$ part, since $\log M=O(Z)$ just as before and splitting its prime factors at $G$ gives $\sum_{p\mid M}p^{-\beta+\delta}=O(G^\delta)$. The remaining squarefree $j$ moment with weight $j^{1/4}|\alpha^M(j)|^2$ is finite with the same bound. The ordinary twisted primitive has tail $O(r e^{-\beta u})$ and $r=Y^{o(1)}$ still. Thus the artificial short endpoint $S$ is removed with exactly the fixed power saving in R96 Section 3: keep $j\le S^{1/2}$, where the endpoint log is at least $G/20$ and the primitive tail is $Y^{-c}$, and control the rest by the same $S^{-1/8}$ moment. The cutoff-dependent terms of the true geometry retain the same finite endpoints $U_v$ and $T_{v,x}$, since this artificial short extension does not change either of those terms. The resulting estimator is (2) up to $O(Y^\beta Y^{-c'})$ with fixed $c'>0$, absorbed in the original arithmetic error. No bound on $M$ below $Q_0$ is needed at this analytic step.

On a translated class multiply the common colors by $\gamma(a)$ and the original exceptional factor $-\chi(-1)/2$. The literal mean with $\psi$ combines the $P$ normalized class means with factor $1/P$. As the cap-tail error from Section 2 was a common algebraic quantity, it multiplies $H_\psi$, whereas the uniform arithmetic error contributes at most its bound times $L_\psi$. This proves (3), with no unproved cancellation of class errors.

The completed color-one lower bound also persists with this $M$. Its proof is [R100 Section 2](r100-spectral-matched-ramanujan-exceptional-mean.md): all extra primes dividing $M$ outside $z$ are conductor primes and hence introduce positive reciprocal shifts $(1-X/p)^{-1}$ in the finite integrated rough primitive; all remaining local estimates and the inverse first moment depend on $z,\beta,U_v$ and $T_{v,x}$, not on an upper constant for $\log M/Z$. Since $\log M=O(Z)$, every analytic convergence and prefactor bound used in that proof is unchanged. The sole possible negative shifted-tail cost is absorbed as before by $z\ge A_0\log G$. Thus (6) of that proof gives
$\widetilde P_1(M)\gg (\int_Jw)(\int_1^2\eta)Y^{2\beta-1}M/(G\varphi(M)(\log r)^4)$
for the fixed nonnegative tests.

For the matched weight, the same exact R100 finite calculation gives $H_\psi=\tau_e/\varphi(D)>0$ and $L_\psi/H_\psi\le2^{\omega(D)}\ll r^{1/4}$. Dividing both errors in (3) by this response therefore leaves an arithmetic error $O(Y^\beta G^C r^{-1/4})$, smaller than any fixed inverse logarithmic power times $Y^\beta$ by the classical Page conductor growth. Since $Y^{2\beta-1}\ge YG^{-2C_*}$ and $\log r\le16Z$, that is negligible against the completed color-one lower bound. If $M>Q_0$, (4) makes $\Xi\le G^{-A_1/2}$, so a sufficiently large fixed $A_1$ makes the second error negligible on the same scale. If $M\le Q_0$ there is no second error. Subtract the parities in (3); only color one survives and the original half cancels. The resulting real sign is $-\chi(-1)$ and the lower bound is (5). The common algebraic error estimate alone does not justify a sign when $M>Q_0$ and the specified denominator margin fails.
