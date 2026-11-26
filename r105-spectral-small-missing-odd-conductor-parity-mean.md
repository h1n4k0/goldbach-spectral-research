# A positive ordinary term in the small-missing odd matched parity mean

**Scope.** For a hypothetical odd Page conductor with a bounded number of missing primes in the stated small-missing range, this evaluates the **ordinary** contribution to the matched parity-difference mean of the genuine mixed strip. It is a positive singular-series term on nonnegative tests. The exceptional cap is retained separately with its original sign. When the hypothetical character is odd, the two terms reinforce; when the character is even, they compete and we do not assert their combined sign. The conclusion is only about the modulated mean of the actual mixed-strip correlation (full or original moving major), not an individual target, the signed shell beyond the mixed strip, prime-pair positivity, Weak S, or existence of a Page zero. No Dirichlet GRH or external zero-gap assertion is used.

Use the exact setting of [the genuine odd-conductor matched means](r104-spectral-genuine-odd-conductor-large-missing-mean.md). In particular $G=\log Y$, $Z=\sqrt G/\log G$, $Y\le N\le2Y$ even, $K=K_z=\prod_{p\le z}p$, and an actual primitive real Page character $\chi$ has odd squarefree conductor $r$ and its simple zero $\beta>1-4a_0/\sqrt G$. Put $D=r/(r,K)$, $M=[K,r]=KD\le e^{2Z}$, $\gamma(N)=c_r(N)/\varphi(r)$ and $H=1/\varphi(D)$. Use the normalized signed mean $\langle F\rangle_K=(K/Y)\sum_{Y\le N\le2Y,\ K\mid N}\eta(N/Y)F(N)$ and the same common scaled half-open left test $I_N=NJ$, $J\subset(1/2,9/16]$, $\omega_N(u)=w(u/N)$; $w,\eta$ are bounded and of bounded variation. Take $X_\pm=S_\pm$ or $X_\pm=S_\pm^{\mathrm{maj}}$ as there, with both true squarefree factor-count parities and the original moving polynomial major, not the auxiliary common arcs.

Put $g=\log G$ and $\ell=\log z$. For fixed $J_1>0$, fixed integer $m_0\ge0$, and fixed admissible $B>B_0>0$, assume throughout that

$$
 \begin{gathered}
 D\le G^{J_1},\qquad \omega(D)\le m_0,\qquad
 \ell\le \frac{g}{(\log g)^2},\qquad
 z\ge A_0 g, \qquad 2\le z\le Z,\\
 B>J_1+1 .
 \end{gathered} \tag{1}
$$

Here $A_0$ is a sufficiently large fixed constant as in [the conditional cap bound](r100-spectral-matched-ramanujan-exceptional-mean.md); only $z\to\infty$ is used for the ordinary calculation. Define the physical integral and its ordinary response by

$$
 \mathcal W=\frac1Y\int_Y^{2Y}
       \eta(v/Y)v\int_J\frac{w(s)}{\log(v(1-s))}\,ds\,dv,
 \qquad
 \mathcal R=\frac K{\varphi(K)}\,H^2\,\mathcal W ,
 \qquad
 \mathcal R_*=\frac K{\varphi(K)}\,H^2\,\frac YG .
 \tag{2}
$$

Thus for fixed nonnegative tests with positive integrals, $\mathcal R\asymp\mathcal R_*>0$. Let $P_1(M)$ be the genuine completed color-one cap integral of R100, without the parity half or sign.

**Theorem.** For either actual $X_\pm$, uniformly for the declared bounded-BV tests and every fixed $A>0$,

$$
 \left\langle\gamma(X_+-X_-)\right\rangle_K
       =\mathcal R-\chi(-1)H P_1(M)
            + o(\mathcal R_*)+O_A(H\,YG^{-A}) .
 \tag{3}
$$

No further closeness hypothesis is needed for this formula. If moreover $(1-\beta)G\le C_*\log G$ with $C_*$ fixed, the tests are fixed nonnegative with positive integrals, and $\chi(-1)=-1$, then for all sufficiently large such dyads

$$
 \left\langle\gamma(X_+-X_-)\right\rangle_K
   \gg \mathcal R_*
      + H\left(\int_J w\right)\left(\int_1^2\eta\right)
          \frac{Y^{2\beta-1}}G\frac{M}{\varphi(M)(\log r)^4}.
 \tag{4}
$$

Constants can depend on the fixed bounds and tests. For $\chi(-1)=1$, (3) instead gives the two competing terms, with no sign implication. The case $D=1$ uses $\gamma=1$ on the family and is still only a result for the dyadic mean of this parity difference.

## 1. Start with the true regular parity cap, with $K$ already imposed

Let $\mathcal B_\pm$ be the exact ordinary completed bracket in [the mixed parity calculation](r80-spectral-whole-mixed-parity-density.md). At each even $N$ its parity difference is the physical integral of $\Sigma(N)P_N$ times
$\int_{-T}^T C_N(t)\,dt-T C_N(T)$, with measure $w(u/N)\,du/\log x$, $x=N-u$ and $T=2B\log\log N+\log(x/N)$. In this ordinary expression the absolutely summed full integral of $C_N$ is $J_{N,\infty}$ and $P_NJ_{N,\infty}=1$ exactly by R80 Section 2. If we replace only that finite combination by $\int_{\mathbb R}C_N$, the resulting ordinary coefficient is $\Sigma(N)\int_{I_N}w(u/N)\,du/\log(N-u)$. We will prove the replacement error small **in the matched mean**, not pointwise.

Use [the odd occupancy expansion](r102-spectral-genuine-two-adic-mixed-means.md), Sections 1--3, but first fix every prime of $K$ as occupied. The exact product is
$\Sigma(N)P_N=(\varphi(N)/N)\prod_{p\nmid N}(1-2/p^2)$ by its local factors. On multiples of $K$ its base scalar $B_K=\Sigma(K)P_K\asymp1/\ell$ has already incorporated all primes $p\le z$. The remaining scalar expansion uses only squarefree $k$ on $p>z$ and the same coefficient $\delta(k)$ with $|\delta(p)|\ll1/p$. This is an exact regrouping of that expansion, not an absolute bound over the planted primes.

Write $R(u)=\sum_{n\le e^u}\mu(n)/n$ for $u\ge0$ and zero below zero. Its ordinary positive base convolution kernel with the $K$ primes removed will be denoted by $\nu_K$. The local generating factor at $p\mid K$ is $(1-X/p)^{-1}$; at $p\nmid K$ it is $(1-\alpha_p^\circ X)/(1-X/p)$ with $\alpha_p^\circ=(p-1)/(p^2-2)$. As always $X$ shifts by $\log p$. These measures are nonnegative as $\alpha_p^\circ<1/p$ off $K$. Fix an odd squarefree $j$ coprime to $K$, as all other $j$ have zero actual weight. For a real pair of primitive slots, start with $\nu_{K,j}$ obtained by multiplying $\nu_K$ by $(1-\alpha_p^\circ X)^{-1}$ for $p\mid j$. The two slots then expand exactly into $F_i=R*\lambda_i$ where $\lambda_i=\nu_{K,j}*\rho_{d_i}$ and $\rho_{d_i}$ is the same product of nonconstant removals at the primes of $d_i$ as in R102. They have $d_i$ supported on $p>z$ and coprime to $j$. The outer weight is $\mu(j)\alpha^\circ(j)^2$ and the indicator $(N,j)=1$ still expands by $d_0\mid j$. Thus every tuple has precisely one remaining constraint $d=[k,d_0,d_1,d_2]\mid N$, where now $d$ is supported on $p>z$, coprime to $K$. The two primitive shifts are kept even if they share some prime. All weighted bounds below allow dropping the coprimality among labels only in **absolute** products.

With the right variable written $x=v(1-s)$ for real $v$, put $T=2B\log\log v+\log(1-s)$ as before. For each ordered tuple denote the cap replacement difference by

$$
 \mathcal T(F_1,F_2;T)
   =\int_{|t|>T} C_{F_1,F_2}(t)\,dt
                      +T C_{F_1,F_2}(T),\qquad
 C_{F_1,F_2}(t)=\int_\mathbb R F_1(u)F_2(u+t)\,du .
 \tag{5}
$$

Fubini, positivity of the shift measures, and the bounds from R102 imply that after testing with $w,\eta$ each of the finite and infinite geometric profiles is locally BV in $v$ with sup plus variation at most $YG^C$ times its two shift masses. For the finite part this is precisely R102 (6)--(7); the complete integral is instead a constant of the two fixed functions multiplied by the same physical test, and is bounded by their $L^1$ norms. Their difference therefore has the same BV bound. Fix $d\le2Y$ on the actual targets. Apply [R104 (4)](r104-spectral-genuine-odd-conductor-large-missing-mean.md) to each profile. Only $D\mid d$ contributes to the continuum, and that term now has normalized density $K/[K,d]=1/d$. The total normalized discretization error is $O(KG^C2^{\omega(D)})=Y^{o(1)}$ by the same absolute summability as R102 (8); imposing $K$ early costs at most a fixed power of $G$, since $\|\nu_K\|\ll 1+\ell$. These operations do not use pointwise closeness of the finite cap to the complete integral.

## 2. Bound the continuum tail after retaining its sampling density

For $\theta=0$ or $\theta=1/\ell$ let $\|\lambda\|_\theta=\int e^{\theta u}\,d|\lambda|(u)$ for a finite log-shift measure. For sufficiently large $Y$ we have $\theta\le1/8$. For both choices,

$$
    \|\nu_K\|_\theta\ll \ell,\qquad
    b_{p,\theta}=\|\rho_p\|_\theta
       =\frac{\alpha_p^\circ p^\theta}{1-\alpha_p^\circ p^\theta}
       \ll p^{-1+\theta}\quad(p>z).
 \tag{6}
$$

For the first estimate the product at $p\nmid K$ has nonconstant local mass $O(p^{-2+\theta})$ and is bounded absolutely. At $p\mid K$ the factor is $(1-p^{-1+\theta})^{-1}$ and its value at zero moment has product $O(\ell)$. The log of its ratio to the zero moment is $O(\sum_{p\le z}(p^\theta-1)/p)=O(1)$, since $p^\theta\le e$ and $\theta\sum_{p\le z}\log p/p=O(1)$. The denominators here are bounded away from zero since $\theta\le1/8$. All these constants are uniform.

Now sum the absolute scalar weights of the fixed tuples times their two shift moments and the continuum density $1/d$, retaining $D\mid d$. After factoring out the two base masses and $B_K$, one may drop coprimality restrictions and extend the nonnegative Euler sums to all primes $p>z$. For a prime $p>z$, set $A_{p,\theta}=(\alpha_p^\circ)^2/(1-\alpha_p^\circ p^\theta)^2\ll p^{-2}$, the cost for including it in $j$, accounting for both slots. Before applying density, the unrestricted local sum is
$(1+|\delta(p)|)(1+b_{p,\theta})^2(1+2A_{p,\theta})$,
while its part with $p$ absent from $d$ is exactly $1+A_{p,\theta}$. Their difference is nonnegative and $O(p^{-1+\theta})$. The part with $p$ present in $d$ has the single density factor $1/p$ exactly, even if two or more of $k,d_0,d_1,d_2$ contain $p$. Hence at unforced primes the increment is $O(p^{-2+\theta})$, summable uniformly, and at each forced $p\mid D$ the entire factor is $O(p^{-2+\theta})$. In particular the weighted sum of both slot moments including $B_K$ is at most

$$
             C_2^{\omega(D)}\,\ell\,D^{-2+\theta}.
 \tag{7}
$$

No factor $G^C$ is needed in this **continuum** estimate. The separate discretization error was bounded before inserting the density.

For the ordinary fixed correlation $C_R(t)=\int R(u)R(u+t)du$ one has
$|C_R(t)|+\int_{|x|>|t|}|C_R(x)|\,dx\ll e^{-c\sqrt{|t|}}$ for $|t|\ge1$. This follows from the ordinary reciprocal Möbius tail in R80 Section 2 by the $L^1,L^2$ bounds with $R=0$ below zero. Also its supremum and $L^1$ norm are bounded. As in R102, $C_{F_1,F_2}$ is the average of translates $C_R(t+s_1-s_2)$ against the two positive shift measures in $s_1,s_2$. For $s_1+s_2\le T/2$, the translated arguments at $\pm T$ and outside $[-T,T]$ retain distance at least $T/2$ from zero. Their contribution to the absolute kernel in (5) is $\ll (1+T)e^{-c'\sqrt T}$ times the corresponding shift mass. For the other pairs, use the bound $\ll (1+T)$ and exponential Markov, which costs at most $e^{-\theta T/2}\|\lambda_1\|_\theta\|\lambda_2\|_\theta$. Therefore, on using (7) at both moments and the physical prefactor $v/\log(v(1-s))\ll Y/G$, the absolute continuum error in the matched mean is at most a constant times

$$
 \frac YG\,\ell\,D^{-2} C_2^{\omega(D)}(1+g)
             \left\{e^{-c_3\sqrt g}
                       +\exp\!\left(-\frac{(B-J_1)g-O(1)}{\ell}\right)
             \right\}.
 \tag{8}
$$

Here $T=2Bg+O(1)$ uniformly on the real support and $\log D\le J_1 g$. Under (1), both bracketed errors, even with the factor $1+g$, tend to zero; for the second use $g/\ell\ge(\log g)^2$. The bounded count of missing primes makes $C_2^{\omega(D)}$ a harmless constant. Since $K/\varphi(K)\asymp\ell$ and $H^2\ge D^{-2}$, (8) is $o(\mathcal R_*)$. The $Y^{o(1)}$ discretization error from Section 1 is also $o(\mathcal R_*)$ by $D\le G^{J_1}$. We have proved the precise matched replacement by $\Sigma(N)\int_{I_N}w(u/N)\,du/\log(N-u)$.

## 3. Compute the resulting singular-series response

On multiples of $K$, the standard exact Euler expansion using the local factors of R80 is
$\Sigma(N)=\Sigma(K)\sum_{d\mid N,\ (d,K)=1}\sigma(d)$, where $d$ is squarefree and $\sigma(p)=1/(p-2)$ for $p>z$. These coefficients are positive. Apply R104 (4) with the common BV profile from (2), including $\eta$, and again $d\le2Y$ on actual targets. The discretization error is $O(KG^C2^{\omega(D)})$ because $\sum_{d\le2Y}\sigma(d)\ll G^C$. For the main sum extend the continuum $d$ beyond $2Y$, with a negligible error: Rankin at $1/4$ gives for the tail of $\sum_{D\mid d}\sigma(d)/d$ an upper bound
$O(Y^{-1/4}D^{1/4}\prod_{p\mid D}\sigma(p)/p)$, using the convergent product of the unforced increments. This is $o(1)$ relative to the full continuum scalar, uniformly in (1).

For $p>z$ the base factor in $\Sigma(K)$ is $1-1/(p-1)^2$. At $p\nmid D$, multiplying by $1+\sigma(p)/p$ makes it exactly one; at $p\mid D$, multiplying by the forced factor $\sigma(p)/p$ leaves $1/(p-1)^2$. At $p\le z$ the factor is $p/(p-1)$, including $p=2$. Therefore the continuum result is exactly $\mathcal W(K/\varphi(K))/\varphi(D)^2=\mathcal R$. Together with (8) this yields
$\langle\gamma(\mathcal B_+-\mathcal B_-)\rangle_K=\mathcal R+o(\mathcal R_*)$.

Finally keep the ordinary mean as a separate term in [R104 Section 3](r104-spectral-genuine-odd-conductor-large-missing-mean.md). That comparison between the auxiliary decomposition and each genuine $X_\pm$, and the raw exceptional formula of R100, have all other errors $O_A(H\,YG^{-A})$ after the exact $\gamma$ moments. On taking the parity difference the exceptional term is $-\chi(-1)H P_1(M)$, with no parity half. This proves (3). Since $D\le G^{J_1}$, the relative inverse-log error is $o(\mathcal R_*)$ for any sufficiently large fixed $A$ (for example $A>J_1+2$). On fixed nonnegative tests $\mathcal W\asymp (\int_Jw)(\int_1^2\eta)Y/G>0$. When $\chi(-1)=-1$ the exceptional lower bound of R100 has the same sign as the now-controlled ordinary term, proving (4). The competing case in (3) does not require either term to dominate the other.
