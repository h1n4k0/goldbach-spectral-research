# An Euler-tail dominance criterion for the competing odd-conductor mean

**Scope.** This gives a sufficient sign criterion in the competing case of the actual small-missing odd-conductor matched parity mean: the Page character is even, so the exceptional correction has the opposite sign from the positive ordinary term. A classical near-zero derivative comparison allows the finite positive shift mass already in the completed cap to absorb part of the derivative's Euler product. The remaining positive Euler tail determines a conditional negative sign of the genuine modulated mixed-strip mean. We do not infer a sign when this criterion fails, the existence of a Page zero, pointwise control, an unweighted sign for the full shell, a prime-pair result, or Weak S. No Dirichlet GRH or external zero-gap assertion is used.

Use all the assumptions of [the small-missing matched parity calculation](r105-spectral-small-missing-odd-conductor-parity-mean.md) and its positive-test conclusion except for the character parity. Thus $G=\log Y$, $g=\log G$, $Z=\sqrt G/\log G$, $Y\le N\le2Y$ even, and an actual primitive real Page character $\chi$ has **odd** squarefree conductor $r$ and a simple real zero $\beta>1-4a_0/\sqrt G$. Set $b=1-\beta$ and assume $bG\le C_*\log G$ with $C_*$ fixed. Take $\chi(-1)=1$, $K=K_z=\prod_{p\le z}p$, $D=r/(r,K)$, $M=KD\le e^{2Z}$, $H=1/\varphi(D)$, $\ell=\log z$, and $\gamma(N)=c_r(N)/\varphi(r)$. Retain the range $D\le G^{J_1}$, $\omega(D)\le m_0$, $A_0g\le z\le Z$, $\ell\le g/(\log g)^2$, and fixed admissible $B>B_0>0$ with $B>J_1+1$, as in R105. The constant $A_0$ is sufficiently large as in [the matched cap lower bound](r100-spectral-matched-ramanujan-exceptional-mean.md). The common bounded-BV tests $w,\eta$ are fixed and nonnegative with positive integrals, and $X_\pm$ denotes either the genuine full mixed strip $S_\pm$ or its genuine original moving polynomial-major integral $S_\pm^{\rm maj}$. Define $\langle\cdot\rangle_K$ and $\mathcal R,\mathcal R_*$ as in R105, retaining all targets, the literal central interval, and the actual signed parity difference.

Choose a sufficiently small fixed $c_y>0$ depending on $B-B_0$, put $y=G^{c_y}$, and define

$$
 \sigma=1+\frac1{2\log r},\qquad
 \mathcal F_\chi(y)=
  \prod_{\substack{p>y\\\chi(p)=1}}(1-p^{-\sigma})^{-2}
       \prod_{\substack{p>y\\p\mid r}}(1-p^{-\sigma})^{-1}.
 \tag{1}
$$

These are absolutely convergent positive products; $y>z$ for all sufficiently large $Y$ in this range.

**Theorem.** In this setting the exact exceptional color-one integral satisfies

$$
 P_1(M)\gg
  \left(\int_Jw\right)\left(\int_1^2\eta\right)
       \frac{Y^{2\beta-1}}G\,\frac M{\varphi(M)}
                        \frac1{\mathcal F_\chi(y)^2}.
 \tag{2}
$$

For a sufficiently large fixed constant $C_{\rm dom}$, the comparison

$$
                  D e^{-2bG}\ \ge\
                           C_{\rm dom}\mathcal F_\chi(y)^2
 \tag{3}
$$

therefore implies, for either genuine $X$, that

$$
  -\langle\gamma(X_+-X_-)\rangle_K
      \ \ge\ \tfrac12 H P_1(M)>0
 \tag{4}
$$

for all sufficiently large such dyads. The constants may depend on the fixed parameters and tests. The conclusion for sufficiently large dyads is ineffective as in R105. In particular the classical elementary bound on the tail here is
$\mathcal F_\chi(y)\ll (\log r/\log G)^2$; a uniform sufficient condition is
$D\ge C'_{\rm dom} e^{2bG}(\log r/\log G)^4$.
This improves the comparison made from the unrefined cap lower bound by the factor $(\log G)^4$ and leaves the exact Euler-tail version (3) available when it is stronger. These are sufficient conditions only, not a transition theorem at the stated thresholds.

## 1. Compare the derivative with an ordinary real Euler product

The original Page conductor growth says $r>G^A$ eventually for every fixed $A$, so $\log r/g\to\infty$ along the stipulated dyads. Also $b\log r=o(1)$ since $r\le e^{2Z}$ and $bG\le C_*g$. Thus the whole real segment $[\beta,\sigma]$ is inside the half-width classical zero-free region with the exceptional zero removed, and its length is less than $1/\log r$. The actual zero is the classical exceptional zero of $\chi$ in this region. By [Montgomery--Vaughan, Chapter 11, Theorem 11.4, (11.8)](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF),

$$
          \frac{L'}{L}(s,\chi)-\frac1{s-\beta}=O(\log r)
                   \qquad(\beta<s\le\sigma).
 \tag{5}
$$

Indeed the real-part restriction is satisfied since $b\log r=o(1)$, and $\sigma-\beta=1/(2\log r)+b<1/\log r$. The real function $L(s,\chi)$ is positive at $\sigma$ by the absolutely convergent Euler product and has no zero on $(\beta,\sigma]$. Its ratio to $s-\beta$ is positive and tends to the positive derivative at the left endpoint. Integrate (5) over this segment, using its $O(1/\log r)$ length. This gives

$$
          |L'(\beta,\chi)|\asymp
          \frac{L(\sigma,\chi)}{\sigma-\beta}
               \asymp (\log r)L(\sigma,\chi).
 \tag{6}
$$

Only the upper estimate in (6) will be used.

Put $A_\beta=\prod_{p\le z}(1-\chi(p)p^{-\beta})^{-1}$. The same product at $\sigma$ is $\asymp A_\beta$, since the difference between their logs is at most
$O((\sigma-\beta)e^{b\ell}\sum_{p\le z}\log p/p)=O(\ell/\log r)=o(1)$.
For $p>z$ there is the following local factorization of the Euler product at $\sigma$. Extract the ordinary factor $1-p^{-\sigma}$ at every prime. A prime with $\chi(p)=1$ then contributes the additional factor $(1-p^{-\sigma})^{-2}$. A conductor prime contributes the additional factor $(1-p^{-\sigma})^{-1}$. A prime with $\chi(p)=-1$ contributes only the additional factor $(1-p^{-2\sigma})^{-1}$, whose product is bounded by an absolute constant. There is no approximation in these local identities.

The extracted ordinary product over $p>z$ equals $\zeta(\sigma)^{-1}\prod_{p\le z}(1-p^{-\sigma})^{-1}\asymp \ell/\log r$. Here $\zeta(\sigma)\asymp(\sigma-1)^{-1}$, and the finite product at $\sigma$ is $\asymp\ell$ by the reciprocal prime estimates and $\ell/\log r=o(1)$. Thus from (6),

$$
 |L'(\beta,\chi)|\ll
  \ell A_\beta\,
  \mathcal F_\chi(y)\,
       \prod_{\substack{z<p\le y\\\chi(p)=1}}(1-p^{-\sigma})^{-2}
       \prod_{\substack{z<p\le y\\p\mid r}}(1-p^{-\sigma})^{-1}.
 \tag{7}
$$

For later use, the positive Euler tail in (1) is bounded by the square of the full reciprocal ordinary tail, namely
$\mathcal F_\chi(y)\le \zeta(\sigma)^2(\prod_{p\le y}(1-p^{-\sigma})^{-1})^{-2}\ll(\log r/\log y)^2$.
The finite Euler product up to $y$ has size $\asymp\log y$ by the same comparison, since $\log y=c_yg=o(\log r)$. This proves the asserted universal bound without imposing a prime-sign distribution assumption.

## 2. The finite positive shift factor absorbs all the small positive Euler factors

Write $U_v=(B-B_0)\log\log v$ and $T_{v,x}=2B\log\log v+\log(x/v)$ for the literal physical caps. Their original definitions are unchanged. In particular $U_v\ge\ell$ uniformly for large $Y$, since $\ell/g\to0$ and $B-B_0$ is fixed and positive. In the proof of R100 Section 2, the primitive is factored into a reciprocal all-minus base and a positive log-shift measure. Write $D_+(U)$ for the cumulative mass of that positive measure on $[0,U]$, in exactly the notation of R100. This is a **finite-cut** cumulative; we do not use the whole mass of an infinite positive Euler product.

Here is the required quantitative use of $D_+$. For a prime $p\nmid M$ with $\chi(p)=1$, let $a_p=p^{-\beta}/(1-2p^{-\beta})$. The positive shift factor is $(1+a_pX)/(1-a_pX)$, $X$ encoding shift $\log p$. Its unconstrained local mass is $(1+a_p)/(1-a_p)$, and its normalized mean log shift is $2a_p\log p/(1-a_p^2)$. At a prime $p\mid r$, $p>z$, the positive local factor is instead $(1-X/p)^{-1}$, with unconstrained mass $(1-1/p)^{-1}$ and normalized mean log shift $\log p/(p-1)$. All other primes $>z$ have unit positive factor. These are the exact R100 local measures, including the extra conductor primes.

Consider solely the product of those positive factors with $z<p\le y$. Since $y=G^{c_y}$ and $b\log y=o(1)$, each normalized mean is $O(\log p/p)$ with an absolute constant uniformly, and the combined mean is $O(\log y)$. For our sufficiently small fixed $c_y$ it is at most $U_v/2$ throughout the dyad. Markov for this normalized positive product retains at least half its mass on $[0,U_v]$. All other factors in the positive measure have their unit atom at zero and can be omitted for a lower bound there. Moreover $a_p\ge p^{-\sigma}$ at the positive primes, so by monotonicity
$(1+a_p)/(1-a_p)\ge(1-p^{-\sigma})^{-2}(1-p^{-2\sigma})$.
The product of the last correction factor is bounded away from zero by absolute convergence. At the conductor primes $(1-1/p)^{-1}\ge(1-p^{-\sigma})^{-1}$. We have proved uniformly in the genuine $U_v$ that

$$
     D_+(U_v)\gg
       \prod_{\substack{z<p\le y\\\chi(p)=1}}(1-p^{-\sigma})^{-2}
       \prod_{\substack{z<p\le y\\p\mid r}}(1-p^{-\sigma})^{-1}.
 \tag{8}
$$

This is a lower bound from a finite truncated positive product, not an assumed average of the prime signs. Together (7)--(8) give $|L'(\beta,\chi)|\ll\ell A_\beta D_+(U_v)\mathcal F_\chi(y)$.

## 3. Compare the two actual terms with the same small response

The proof of R100 Section 2, before discarding $D_+(U_v)\ge1$, gives the stronger cap bound
$\mathcal A_1(v,x)\gg M_M\,\ell^2D_+(U_v)^2$ for $U_v\ge\ell$ and $z\ge A_0g$. Here $M_M$ is the R96 prefactor at the sampling modulus $M$, not the modulus itself. Its exact product, as there, is

$$
 M_M
  =\frac{M}{\varphi(M)}
     \frac{A_\beta^2}{L'(\beta,\chi)^2}
       \{1+O(z^{1-2\beta})\}.
 \tag{9}
$$

Indeed the conductor factor restores the primes of $r$, the other primes of $M$ lie in $K$, and each exterior factor at $p\nmid M$ is $1+O(p^{-2\beta})$. The bracket in (9) stays positive and comparable to one. Combining (8) with (7) cancels the two powers of the true available $D_+(U_v)$, of $\ell$, and of the interior product $A_\beta$. In particular on the actual physical support,

$$
       \mathcal A_1(v,x)\gg
                \frac M{\varphi(M)}\,\mathcal F_\chi(y)^{-2}.
 \tag{10}
$$

The nonnegative physical integrals retain their original cutoffs and scale $Y^{2\beta-1}/G$ times the product of the two test integrals. Thus (10) proves (2). No pointwise arithmetic replacement has been made; this is a lower bound on the completed cap inside the already valid matched mean.

In the genuine R105 expansion (3), since $\chi(-1)=1$, the ordinary and exceptional terms are $\mathcal R$ and $-H P_1(M)$. For the fixed positive tests one has $\mathcal R\asymp \mathcal R_*$ and (2) gives the ratio lower

$$
    \frac{H P_1(M)}{\mathcal R}
           \gg e^{-2bG}\,D\,\mathcal F_\chi(y)^{-2}.
 \tag{11}
$$

The factor $D$ here is exact in the scaling: $M/\varphi(M)=(K/\varphi(K))(D/\varphi(D))$, while the ordinary response has $H^2$ and the exceptional has $H=1/\varphi(D)$. The physical test integrals cancel in this comparison up to absolute fixed factors. A sufficiently large fixed constant in (3) therefore gives $H P_1(M)\ge 4\mathcal R$. Choose $A>J_1+2$ in R105 so that its relative-to-$H$ inverse-log error is $o(\mathcal R_*)$, and its cap comparison error was already $o(\mathcal R_*)$. They are smaller than $\mathcal R$ for large $Y$ on these fixed tests. Substituting into that true parity difference yields (4) for each of the two genuine meanings of $X_\pm$. Without (3), this proof supplies a lower bound on the exceptional size, but does not show which of the two opposite terms dominates.
