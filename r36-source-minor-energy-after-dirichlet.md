# Unsigned minor energy survives the logarithmic square-root cutoff

Assume global Dirichlet GRH. Use the exact $F_I$, $M=\operatorname{rad}(NW)$, $K=M/\varphi(M)$, eligible prime cofactor set $\mathcal Q$, $0<\kappa\le1/2000$, and interval $I\subseteq I_0=[\rho N,(1-\rho)N]$ of the [original covariance calculation](r32-source-double-giant-major-arcs.md) and the [full Dirichlet-width estimate](r35-source-square-root-dirichlet-arcs.md). In particular $L=\log N$, $0<\rho<1/2$ and $\kappa$ are fixed, and R35 uses $\mathfrak D$ with denominators $r\le R=\lfloor\lfloor\sqrt N\rfloor L^{-200}\rfloor$ and widths $1/(r\lfloor\sqrt N\rfloor)$. The complement only admits square-root Dirichlet approximants at distance at most $1/(r\lfloor\sqrt N\rfloor)$ with denominators $R<r\le\lfloor\sqrt N\rfloor$.

**Proposition.** For any fixed $\eta>0$, uniformly over the same hard intervals with $|I|\ge\eta N$ and all sufficiently large even $N$,

$$
 \int_{\mathbb T\setminus\mathfrak D}|F_I(\alpha)|^2\,d\alpha
 \ge 0.009\, |I|L . \tag{1}
$$

In particular, at $I=I_0$ the actual signed remainder $\int_{\mathbb T\setminus\mathfrak D}F_{I_0}(\alpha)^2e(-N\alpha)\,d\alpha$ cannot be bounded by $o(\mathfrak S(N)N)$ simply by taking absolute values of its integrand: that integral of the absolute value is the left side of (1), whereas $\mathfrak S(N)\ll\log L$. This is not a lower bound for the signed same-target coefficient and does not rule out signed cancellation.

Write

$$
 c=c_\kappa=\log\frac{1-\kappa}{1/2+\kappa},\qquad
 a=a_\kappa=1/2-2\kappa,\qquad d=d_\kappa=c-a .
$$

R32's full-circle Parseval calculation gives

$$
 \int_{\mathbb T}|F_I|^2=|I|L(d+o_{\rho,\kappa,\eta}(1)).
 \tag{2}
$$

Here the prime-supported semiprime representation is unique (the large prime $p$ is above $N^{1/2}$), its squared marker is $(\log q)^2$, and the usual RH prime count with both cutoffs yields $d=\int_\kappa^{1/2-\kappa}v/(1-v)\,dv$. The synthetic coefficients are $O_\kappa(K)$, with $K\ll(\log L)^2$, so their full energy and their cross with the prime portion are $o(NL)$. This is the same actual transform as in R35.

## 1. A first moment of the divisor corrections at the longer cutoff

For $t\in I_0$ let

$$
 g_q(t)=\frac{\log q}{q\log(t/q)},\qquad A(t)=\sum_{q\in\mathcal Q}g_q(t)=c+o_{\rho,\kappa}(1).
$$

The last evaluation follows from ordinary prime Mertens and partial summation; excluding the at most $1/\kappa$ prime factors of $N$ in the polynomial range changes it by $o(1)$. The exact R32 model density is

$$
 G_r(t)=\sum_{q\in\mathcal Q}g_q(t)
    \frac{\mu(r/(r,q))}{\varphi(r/(r,q))}
    {\bf1}_{r/(r,q)\nmid M}.
$$

On squarefree $r\nmid M$ this is $\mu(r)[A(t)-C_r(t)]/\varphi(r)$, with

$$
 C_r(t)=\sum_{\substack{q\in\mathcal Q\\q\mid r}}qg_q(t)
       -\sum_{\substack{q\in\mathcal Q\\q\mid r,\ r/q\mid M}}(q-1)g_q(t).
 \tag{3}
$$

Indeed each cofactor $q\mid r$ loses its usual common term and, unless $r/q\mid M$, adds its opposite Möbius sign with factor $q-1$. If $r\mid M$ all profiles vanish, and define $C_r=0$ there: no eligible $q$ divides $M$. For $r\le R$ and sufficiently large $N$ the correction is nonnegative and

$$
 0\le C_r(t)\le\sum_{q\mid r}\frac{\log q}{\log(t/q)}
              \le \frac{\log r}{\log(\rho N)-\log r}\le1.
 \tag{4}
$$

We evaluate its first moment uniformly on $I_0$:

$$
 \sum_{r\le R}\frac{\mu^2(r)}{\varphi(r)}C_r(t)
   = L\bigl(\ell_\kappa+o_{\rho,\kappa}(1)\bigr),
 \qquad
 \ell_\kappa=\int_\kappa^{1/2-\kappa}\frac{1/2-v}{1-v}\,dv=a-c/2.
 \tag{5}
$$

For the first sum on the right of (3), write $r=qd$ and switch the sums. Its contribution is

$$
 \sum_{q\in\mathcal Q}\frac{q\,g_q(t)}{q-1}
       \sum_{\substack{d\le R/q\\(d,q)=1}}\frac{\mu^2(d)}{\varphi(d)} .
$$

Every eligible $q\le R$ eventually. The inner sum is $\log(R/q)+O(1+L/q)$: the unrestricted harmonic sum is $\log x+O(1)$ by the elementary convolution in R32 §4, and the multiples of the prime $q$ remove at most $(q-1)^{-1}\sum_{d\le x/q}\mu^2(d)/\varphi(d)$. The difference of $q/(q-1)$ from one is negligible after multiplication by $\log(R/q)$. Also the second subtraction in (3) costs at most

$$
 \sum_q g_q(t)\sum_{d\mid M}1/\varphi(d)=K A(t)=O_\rho((\log L)^2)=o(L),
$$

since $q\nmid M$ and $\varphi(qd)=(q-1)\varphi(d)$ for those pairs. Thus the left side of (5) is $\sum_q g_q(t)(\log R-\log q)+o(L)$. Replacing $\log R$ by $L/2$ costs $O(\log L)$, and replacing $\log(t/q)$ by $L-\log q$ costs $O_\rho(1)$ in this expression. Prime Mertens in $\sum_q (\log q)/q$ yields (5), including the endpoints.

## 2. The major energy is strictly below the total

On squarefree $r\nmid M$, use $(A-C_r)^2\le A^2-(2A-1)C_r$ from (4) and bound the $\beta$ energy of each real profile by full real Plancherel. The disjoint arcs have $\varphi(r)$ numerators and $\sum_{r\le R}\mu^2(r)/\varphi(r)=\log R+O(1)$. Equations (4) and (5) bound the squared major **signal** energy from squarefree denominators by

$$
 |I|L\left[\frac{c^2}{2}-(2c-1)\ell_\kappa+o_{\rho,\kappa}(1)\right].
$$

The use of the nonnegative squarefree harmonic sum for the first term is an upper bound; the omitted $r\mid M$ carry zero $C_r$ and so do not change the correction term. For nonsquarefree $r$ a signal is possible only at $r=q^2 h$ with squarefree $h$ coprime to an eligible $q$. The weighted mass of these denominators is

$$
 \sum_{\substack{r\le R\\r=q^2h}}\frac1{\varphi(r)}
 \ll L\sum_{q\ge N^\kappa}q^{-2}=O(LN^{-\kappa}) .
$$

Using $|G_r(t)|\ll_\rho1/\varphi(r)$ and Plancherel, these signals cost $o(|I|L)$. The squared discrepancy $O_{\rho,\kappa}(NL^{-32})$ from R35, and its cross term by Cauchy–Schwarz, also cost $o(|I|L)$ because $|I|\ge\eta N$. Therefore the last displayed squarefree bound, with $o_{\rho,\kappa,\eta}(1)$, bounds the actual major energy.

Subtract from (2). The gap is

$$
 d-\frac{c^2}{2}+(2c-1)\ell_\kappa
 = (1-c)\left(\frac{3c}{2}-2a\right)>0.0105
$$

throughout the stated range, since $0.69<c<0.70$ and $a\le 1/2$. This proves (1) with room for the uniform little-oh terms. The proposition uses the wider all-denominator R35 family exactly; it is not an assertion about the union with R34's nonnested constant-width arcs.
