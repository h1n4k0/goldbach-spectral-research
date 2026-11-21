# Parseval on the auxiliary modulus and Plancherel on the major arcs

**Independent follow-on to the frozen [adaptive-rectangle result](spectral-post-r11-adaptive.md).** Assume global Dirichlet GRH. Use the same doubled squares $s=2r^2$, $R<r\le2R$, $X=8R^2$, $L=\log X$, and the exact fixed compensated block $\mathcal T_{s,J}$, $J=[\log(1/2),\log(9/16)]$. For any fixed $\eta\in(0,1/4)$, $\epsilon>0$, and $X^{-1/4+\eta}\le \tau\le1$,
$$
 \#\{r:\|\mathcal T_{2r^2,J}\|_{\rm HS}>\tau\}
 \ll_{\eta,\epsilon} X^\epsilon
       \bigl(X^{3/10}\tau^{-2}+X^{1/4}\tau^{-5/2}\bigr).
 \tag{1}
$$
In particular the block is $\le X^{-a}$ outside a power-saving fraction for every fixed $a<1/10$; and
$$
 \frac1{\#\{R<r\le2R\}}\sum_{R<r\le2R}\|\mathcal T_{2r^2,J}\|_{\rm HS}^2
 \ll_\epsilon X^{-1/5+\epsilon}. \tag{2}
$$
The refinement below changes the major estimate; (1)–(2) still use only the usual Vaughan bound on the minor arcs. These are density results for one block, not pointwise, full-operator, or a proof of S/R.

## 1. Uniform individual major estimate without a pointwise product loss

Let $I\subset[0,X]$ be any real interval, $e(\theta)=e^{2\pi i\theta}$, $P_I(\theta)=\sum_{n\in I}\Lambda(n)e(n\theta)$, $V_I(\beta)=\int_I e(\beta u)\,du$. Take disjoint major arcs $|\beta|\le P/(qX)$ at reduced $a/q$, $q\le P$, with $2P^2<X$. The main calculation will hold for every such $P$. Define
$$
 \Psi_\chi(u)=\sum_{n\le u}\Lambda(n)\chi(n)-\delta_\chi u,\qquad
 \mathcal E_{\chi,I}(\beta)=\int_I e(\beta u)\,d\Psi_\chi(u).
$$
Here $\delta_\chi=1$ only for the principal character modulo $q$. Endpoints in the Stieltjes integral follow the actual arithmetic interval convention, and its Lebesgue part uses the original real interval. On GRH one has $|\Psi_\chi(u)|\ll\sqrt X L^2$ for $0\le u\le X$ and $q\le P<\sqrt X$: apply the ordinary conditional prime number theorem for characters in its large-$u$ range, and the elementary Chebyshev bound for $u<q$ or bounded $u$. Use the inducing primitive estimate and remove the finite prime factors if needed. This is global GRH, not the GRH of the tested modulus alone.

Separate the unit and nonunit portions. For units define
$$
 E_{I,b}(\beta)=\sum_{\substack{n\in I\\n\equiv b\bmod q}}\Lambda(n)e(\beta n)
               -\frac{V_I(\beta)}{\varphi(q)} \quad ((b,q)=1),\qquad
 E_I^*(a,q,\beta)=\sum_{(b,q)=1} e(ab/q)E_{I,b}(\beta).
$$
Exact finite Parseval in $a$ and multiplicative orthogonality give
$$
 \sum_{a\bmod q}|E_I^*(a,q,\beta)|^2
   =q\sum_{(b,q)=1}|E_{I,b}(\beta)|^2
   =\frac q{\varphi(q)}\sum_{\chi\bmod q}|\mathcal E_{\chi,I}(\beta)|^2. \tag{3}
$$
The nonunit error is the unmodeled sum over powers of primes dividing $q$, bounded by $O(L^2)$ for every $a,\beta$. Let $E_I$ be the total error, so on reduced $a/q$, $P_I(a/q+\beta)=\mu(q)V_I(\beta)/\varphi(q)+E_I(a,q,\beta)$. Endpoint conventions in $E_I^*$ and in the nonunit piece are aligned to the same original $I$.

Abel summation bounds $\mathcal E_{\chi,I}(\beta)$ by $O(\sqrt X L^2(1+X|\beta|))$. This gives from (3)
$$
 \sum_{a\bmod q}|E_I(a,q,\beta)|^2\ll q X L^4(1+X|\beta|)^2. \tag{4}
$$
Now use Abel summation **before square integration in $\beta$**. If $B=P/(qX)$, the difference of endpoint terms in $\mathcal E_{\chi,I}$ has size $O(\sqrt X L^2)$, and the remaining term is $-2\pi i\beta$ times the Fourier transform of $\mathbf1_I\Psi_\chi$. Thus
$$
 \int_{-B}^B|\mathcal E_{\chi,I}(\beta)|^2\,d\beta
  \ll L^4\bigl(XB+X^2B^2\bigr)
  \ll L^4(P/q)^2. \tag{5}
$$
Indeed $\|\mathbf1_I\Psi_\chi\|_2^2\ll X^2L^4$ and real-line Plancherel bounds the entire squared Fourier integral. The last inequality uses $q\le P$. Apply (3) and include the nonunit contribution; the latter contributes at most $O(qBL^4)$, absorbed. Hence
$$
 \sum_{a\bmod q}\int_{-B}^B|E_I(a,q,\beta)|^2\,d\beta
   \ll P^2L^4/q. \tag{6}
$$

For two intervals $I_1,I_2$, the double-error product summed over reduced $a$ and integrated at fixed $q$ is bounded by (6) and Cauchy–Schwarz, so summing $q$ costs $O(P^2L^5)$. For a mixed term use (4) pointwise in $\beta$, Cauchy–Schwarz over the reduced $a$, and $|V_I(\beta)|\ll X/(1+X|\beta|)$. At fixed $q$ the bound is
$$
 \frac1{\varphi(q)}\int_{-B}^B |V_I(\beta)|
         \sum_{a\bmod q}^* |E_{I'}(a,q,\beta)|\,d\beta
 \ll \frac{\sqrt X P L^2}{\sqrt{q\varphi(q)}} .
$$
Summing produces $O(\sqrt X P L^3)$: use $(q/\varphi(q))^{1/2}\le q/\varphi(q)=\sum_{d\mid q}\mu^2(d)/\varphi(d)$ and $\sum_d\mu^2(d)/(d\varphi(d))<\infty$. These absolute error estimates hold after inserting $e(-s(a/q+\beta))$ separately for every $s$, or for the negative convolution sign with the corresponding complex conjugate. The Ramanujan series and continuous-integral tails remain $O_\epsilon(X^{1+\epsilon}/P)$ as in the frozen note. Thus the individual major error is
$$
 O_\epsilon\bigl(\sqrt X P L^3+P^2 L^5+X^{1+\epsilon}/P\bigr). \tag{7}
$$
A smooth fixed weight $w(n/X)$ on one factor is also permitted: replace $\Psi_\chi$ there by the corresponding cumulative signed weighted measure. Bounded $w$ and fixed variation preserve the $O_w(\sqrt X L^2)$ bound by Abel summation, which is all the derivation of (4)–(6) needs. The principal transform for that factor has the same $X/(1+X|\beta|)$ bound by ordinary integration by parts.

## 2. Adaptive selection and the exponent bookkeeping

Apply (7) individually to the collapsed adaptive interval and the one fixed uncut factor. The dyadic minor proof of the frozen note works unchanged for $P\le X^{2/5}$: for the uncut factor the $X^{4/5}$ Vaughan term is still at most $XP^{-1/2}$. Its norm yields the same selected minor bound $\sqrt M X^{5/4+\epsilon}P^{-1/4}$ before normalization by $X$. For an arbitrary selected set and each member's worst allowed interval, the weighted layer cake and exact kernel then give
$$
 \sum_{r\in E}\|\mathcal T_{2r^2,J}\|_{\rm HS}
 \ll_\epsilon
   \sqrt M X^{1/4+\epsilon}P^{-1/4}
   +M\bigl(X^{-1/2}PL^3+X^{-1}P^2L^5+X^\epsilon/P+X^{-1/2}L^2\bigr).
$$
The last summand is the unit/proper-power correction. There is no unproved exchange of a modulus supremum with an integral: the interval can be chosen for each $r$ first by the dyadic estimate.

Set $P=\lfloor\min(X^{2/5},\sqrt X\,\tau L^{-10})\rfloor$. The first two major errors are $O(\tau L^{-7}+\tau^2L^{-15})$. For the series tail, $X^\epsilon/(P\tau)$ is bounded by a constant times the larger of $X^{\epsilon-2/5}/\tau$ and $X^{\epsilon-1/2}\tau^{-2}L^{10}$, both $o(1)$ if $\tau\ge X^{-1/4+\eta}$ and the internal $\epsilon>0$ is small enough. The unit error is absorbed too. Take the actual exceptional set as $E$, divide away $\sqrt M$, and square:
$$
 M\ll_\epsilon X^{1/2+\epsilon}P^{-1/2}\tau^{-2}
   \ll_\epsilon X^\epsilon(X^{3/10}\tau^{-2}+X^{1/4}\tau^{-5/2}),
$$
after absorbing logarithms. For (2), take $\tau_0=X^{-1/10}$ in the layer-cake mean-square integral. Between $\tau_0$ and 1 the normalized first term integrates to $O_\epsilon(X^{-1/5+\epsilon}\log X)$ and the second to $O_\epsilon(X^{-1/4+\epsilon}\tau_0^{-1/2})=O_\epsilon(X^{-1/5+\epsilon})$. Below $\tau_0$ use the full-family count; above 1 use (1) at 1 and the elementary uniform $O(L)$ block bound from the frozen proof. This yields (2) after relabeling $\epsilon$.

**Separate implication using the stated fourth-moment preprint.** Formulae (1)–(2) use the usual Vaughan estimate only. If one invokes the stated fixed smooth fourth-moment theorem in [H. Li and Z. Liu, arXiv:2610.26756v1, Theorem 1](https://arxiv.org/html/2610.26756v1), it can be plugged into the same collapsed argument for this fixed block. Split the raw $s$ range into $[Z/2,Z]$ for $Z=X/2$ or $Z=X$. All contributing $n,m$ then lie in $[7s/16,9s/16]\subset[7Z/32,9Z/16]$, where the preprint's **own fixed log-Gevrey weight** at scale $Z$ equals one. Replace the uncut factor by the corresponding fixed smooth factor; no smooth approximation to the adaptive interval is necessary. The difference between the smooth Mangoldt factor and its prime-only version is $O(\sqrt Z\log Z)$ pointwise, so it is harmless in $L^4$. Its minor norm at $P=Z^{\kappa_0}$, $\kappa_0\in(4/9,9/20)$, is then $\ll Z^{5/8}(\log Z)^{25}$ by that theorem. The adaptive factor stays hard and is used only in interval Parseval. Bound (7) applies on the same arcs to the smoothed uncut factor, with the original continuous main term on allowed boxes. In either dyad the normalized minor bound is $\sqrt M Z^{1/8+\epsilon}$, and the individual major error after normalization is $O(Z^{-1/2+\kappa_0}(\log Z)^3+Z^{-1+2\kappa_0}(\log Z)^5+Z^{-\kappa_0+\epsilon})$. Thus this separate implication gives $O_{\epsilon,\delta}(X^{1/4+\epsilon}\tau^{-2})$ exceptions if $\tau\ge X^{-1/2+\kappa_0+\delta}$, for fixed $0<\delta<1/2-\kappa_0$. It relies on the stated preprint theorem and is not a reproof or audit of it. It does not change the pointwise gap: the bound at a singleton selected set remains too large to rule out an exceptional modulus.
