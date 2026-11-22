# Direct short-window variance for the exterior difference compression

**Scope.** A full, genuine Hilbert–Schmidt mean-square estimate on the [exterior mean-difference span](r40-operator-negative-difference-subspace.md). It permits substantially shorter modulus intervals than R46 and allows a larger physical range in two explicit choices, without using modulus-frequency collars. It controls averages on short even-modulus intervals and on sufficiently large subsets of them, not a bound at a specified modulus, a result on other spatial directions, or a proof of weak S.

## Statement

Write $L=\log Q$, $\ell=\log L$. Fix $K>0$ and $C>1$, and choose

$$
 H\ge 2(K+3)\ell^2/\log\ell,\qquad Y=e^H,\qquad M=e^{CH}\le Q^\gamma .
$$

Take all whole dyads in $[Y,M]$ on the common grid $V=2^jY$, and let $E_N$ be the genuine R40 normalized mean-difference isometry on that index set for each even $N$. Let $\mathcal I\subset[Q,2Q]$ be any interval of length $Q^d\le\Delta\le Q^{19/20}$, and let $\mathcal A$ be any set of $J\gg Q^d$ distinct even integers in it. Put $P=\lfloor Q^\xi\rfloor$. The fixed exponents satisfy

$$
 0<\gamma<\xi,\qquad \xi+\tfrac32\gamma<\tfrac12,\qquad
 \max\{1+2\gamma-\xi,\tfrac35+\tfrac85\gamma\}<d\le\tfrac{19}{20}.
 \tag{1}
$$

Assume the original local Dirichlet GRH at each $N\in\mathcal A$ and auxiliary Dirichlet GRH for moduli $q\le P$. These are separate assumptions; global Dirichlet GRH suffices. Then, uniformly in the position of $\mathcal I$,

$$
 \begin{split}
 \Big(\operatorname{Avg}_{N\in\mathcal A}
   \|E_N^*T_NE_N\|_{\mathrm{HS}}^2\Big)^{1/2}
 \ll_\epsilon {}&
 Q^\epsilon\left[
 \frac{\sqrt M}{\sqrt J}\left(\sqrt{\frac{QM}{P}}+(QM)^{3/10}\right)
 +P M^{3/2}Q^{-1/2}
 +\frac MP+\frac M{\sqrt Q}\right]\\
 &+L^{5/2}\big((\Delta/Q)^{1/2}+Y^{-1/5}\big).
 \end{split}
 \tag{2}
$$

In particular, each choice $(d,\gamma,\xi)=(129/200,\,1/40,\,11/25),\ (77/100,\,3/40,\,77/200),\ (93/100,\,3/25,\,127/400)$ gives $O_\epsilon(Q^{-1/400+\epsilon}+L^{5/2}Y^{-1/5})=o(L^{-K})$ for fixed sufficiently small $\epsilon>0$, including all even moduli in each indicated interval. For comparison R46 required $d=22/25$ and $\gamma\le 1/40$ in its explicit theorem. The last two choices here extend the spatial span by including all dyads through $Q^{3/40}$ and $Q^{3/25}$, respectively, not by adding arbitrary directions inside each dyad. The R31 spatial mask is identically one on these supports.

## 1. Exact raw tests and the signed alias formula

Use the [raw-weight freezing construction](r46-operator-short-window-full-variance.md#1-freeze-the-actual-raw-weights-on-the-short-interval), which is independent of the R45 Fourier collar theorem. In brief, replace the whole-cell differences by the [fixed physical endpoint tests](r43-operator-signed-modulus-window.md#1-genuine-weights-and-continuity-in-the-modulus) $e^\circ_{N,V}$. Anchor an $N_0\in\mathcal A$, put $a=N/N_0$, and define $g_{N,V}(u)=a^2r_{N_0}(au)e^\circ_{N_0,V}(au)/r_N(u)$ with the actual physical Hardy weight $r_N$. In the Volterra prefix, $du=dz/a$ and $a/N=1/N_0$ give

$$
 \frac{\sqrt{2\pi x}}N\int_{u\ge x/N}r_N(u)g_{N,V}(u)\,du
 =\rho_V(x)
 =X_V^{-1/2}b_{N_0,V}(x/X_V),\qquad X_V=N_0V.
 \tag{3}
$$

The functions $b_{N_0,V}$ are uniformly bounded Lipschitz, supported on $[1,2]$ with zero extension. The fixed-degree weight bounds in R43 and the support change estimates in R46 are uniform for $\log V=O(\log Q)$, including the present range. In particular the fixed test replacement and freezing contribute $O(L^{5/2}((\Delta/Q)^{1/2}+Y^{-1/5}))$ in HS as in R46: the two families of tests have disjoint dyadic supports separately, so their differences have overlap at most two and basis-map norm $O((\Delta/Q)^{1/2})$; the $L^2$ exterior operator bound is $O(L^2)$, and there are only $O(L)$ dyads. The support dilation is $1+O(\Delta/Q)$, which keeps the fine-side starting threshold and R31 mask intact. This uses only the original local GRH. Since $\gamma<1/5$ by (1), the fixed polynomial-scale assumptions in that application of R43–R46 hold.

For an entry $(V,U)$, sum the three signed aliased lines $m=x+kN,\ m=x-kN,\ m=kN-x$ for $1\le k\le4M$, with signs $+,+,-$, respectively. There is no $m=x$ term. On each line the arithmetic term is $\Lambda(x)\Lambda(m)\rho_V(x)\rho_U(m)$ with the original unit conditions; the exact continuous term is

$$
 \mathfrak S(kN)\int_{\mathbb R}\rho_V(x)\rho_U(m(x,N))\,dx .
 \tag{4}
$$

Removing the proper powers gives an error $O(Q^{-1/2}ML^3)$ per entry as in R43–R46. Indeed each such power on either leg has at most $O(\max(V,U))$ alias partners, the raw leg contains $O(\sqrt{Q\max(V,U)}L)$ powers, and each pair has size $O(L^2/(Q\sqrt{VU}))$. The remaining primes exceed $N$, so the original unit conditions are automatic. The continuous model is not changed.

Put $\lambda(p)=\log p$ at primes and zero otherwise, $e(z)=e^{2\pi iz}$, and

$$
 A_V(\alpha)=\sum_x\lambda(x)\rho_V(x)e(x\alpha),\qquad
 B_V(\beta)=\int_{\mathbb R}\rho_V(x)e(x\beta)\,dx .
$$

By Chebyshev and Parseval, $\|A_V\|_{L^2(\mathbb R/\mathbb Z)}\ll\sqrt L$; $\|\rho_V\|_2\ll1$, $\|\rho'_V\|_\infty\ll X_V^{-3/2}$ a.e., and $|B_V(\beta)|\ll\sqrt{X_V}\min(1,(X_V|\beta|)^{-1})$. The ordinary-prime alias for $N=2n$ is the Fourier coefficient at $s=2kn$ of $A_V(\varepsilon_1\alpha)A_U(\varepsilon_2\alpha)$, where $(\varepsilon_1,\varepsilon_2)=(-,+),(+,-),(+,+)$ for the three lines above. All sign choices are kept in what follows.

## 2. Minor arcs: use multiplicities before summing alias coefficients

Take disjoint raw major arcs $\mathfrak M=\bigcup_{q\le P,\ (a,q)=1}\{a/q+\beta:|\beta|\le\delta_q\}$ on the torus, where $\delta_q=2P/(qQ)$. Two distinct rational centers are at distance at least $1/(qq')$, and $\delta_q+\delta_{q'}\le 4P^2/(qq'Q)<1/(qq')$. The remaining set $\mathfrak m$ is symmetric. Dirichlet approximation with denominator bound $\lfloor Q/P\rfloor$ gives for each $\alpha\in\mathfrak m$ an approximation $a/q$ with $P<q\le Q/P$ and $|\alpha-a/q|\le q^{-2}$. The classical Vaughan bound for $\sum_{x\le t}\Lambda(x)e(\alpha x)$ has terms $t/\sqrt q+t^{4/5}+\sqrt{tq}$, times $\log^{5/2}(2t)$ ([Koukoulopoulos, Theorem 23.8](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=258)). Abel summation with $\rho_V$ at $t\asymp X_V$, and proper-power removal in this one-variable estimate, give

$$
 \sup_{\mathfrak m}|A_V|\ll L^{O(1)}
       \left(\sqrt{QM/P}+(QM)^{3/10}\right).
 \tag{5}
$$

Here $\sqrt{Q/P}$ from the upper endpoint for $q$ is bounded by the first displayed term. This proof does not assume $P\le Q^{1/5}$.

For one entry and one orientation put $c_s=\int_{\mathfrak m}A_V(\varepsilon_1\alpha)A_U(\varepsilon_2\alpha)e(-s\alpha)\,d\alpha$. Orthogonality is on the whole torus after inserting ${\bf1}_{\mathfrak m}$. Write $\mathcal J=\{n:2n\in\mathcal A\}$, so $J=|\mathcal J|$. No consecutive-interval property of $\mathcal J$ is used. Cauchy before summing $n$, followed by the divisor bound for $s\le 8QM$, gives

$$
 \sum_{n\in\mathcal J}\left|\sum_{1\le k\le4M}c_{2kn}\right|^2
 \ll M\sum_{n\in\mathcal J}\sum_{1\le k\le4M}|c_{2kn}|^2
 \ll_\epsilon M Q^\epsilon\sum_{s\in\mathbb Z}|c_s|^2 .
 \tag{6}
$$

Indeed for a given positive $s=2kn$ there are at most $\tau(s)$ possible pairs $(k,n)$. In the last square sum use (5) on one factor and $\|A_U\|_2\ll\sqrt L$ on the other. After dividing by $J$, taking roots and summing the three orientations and the $O(L)$ matrix dimension, the result is in fact

$$
 O_\epsilon\left(Q^\epsilon\frac{\sqrt M}{\sqrt J}
       \left(\sqrt{QM/P}+(QM)^{3/10}\right)\right).
 \tag{7}
$$

This estimate does not require cancellation between the orientations, and it does not presume that the coefficients at $2kn$ are all distinct.

## 3. Integrated actual major-arc error from auxiliary GRH

For each unit residue $r\bmod q$, set

$$
 F_r(t)=\sum_{\substack{x\le t\\x\equiv r\ (q)}}\lambda(x)-t/\phi(q).
$$

Set $F_r=0$ for nonunits. Auxiliary GRH, character Parseval and the elementary prime-power bound give

$$
 \sum_{r\bmod q}|F_r(t)|^2\ll t L^4,\qquad
 q\le P,\quad t\asymp X_V.
 \tag{8}
$$

Specifically, by [Koukoulopoulos, Exercise 11.2(a)](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=126), the character sums of $\Lambda$ differ from ${\bf1}_{\chi=\chi_0}t$ by $O(\sqrt t\log^2(2qt))$ under Dirichlet GRH, also for imprimitive characters after removing missing Euler factors. Replacing $\Lambda$ by $\lambda$ costs $O(\sqrt t L^2)$. Divide the squared character sum by $\phi(q)$. All ordinary primes on the supports exceed $q$, so nonunits have no arithmetic mass there.

For fixed $V,q$, let $f_r=\rho'_V F_r$ and $g_r=\rho_V F_r$, extended by zero outside the support of $\rho_V$. Abel gives

$$
 A_V(a/q+\beta)=\frac{\mu(q)}{\phi(q)}B_V(\beta)
     -\sum_{r\bmod q}e(ar/q)
                    \big(\widehat f_r(\beta)+2\pi i\beta\widehat g_r(\beta)\big)
 \quad ((a,q)=1),
 \tag{9}
$$

with positive-sign Fourier transforms and the usual identity
$\sum_{(r,q)=1}e(ar/q)=\mu(q)$. There are no endpoint terms because the zero-extended Lipschitz weights vanish at endpoints. Denote the error in (9) by $R_V(a/q+\beta)$. Apply finite Fourier Parseval by majorizing the unit $a$-sum by the full $a\bmod q$ sum for the error. For the $f$-part, use $\sup_\beta\sum_r|\widehat f_r(\beta)|^2\le O(1)L^4$, which follows by Cauchy on the $t$-range $O(X_V)$ and (8). For the $g$-part, use real-line Plancherel: $\sum_r\|\widehat g_r\|_2^2=\sum_r\|g_r\|_2^2\ll X_VL^4$ by (8). This yields

$$
 \begin{split}
 \sum_{q\le P}\sum_{a\bmod q}^{*}
        \int_{-\delta_q}^{\delta_q}|R_V(a/q+\beta)|^2\,d\beta
 &\ll L^4\sum_{q\le P}q\big(\delta_q+\delta_q^2X_V\big)\\
 &\ll L^5P^2V/Q .
 \end{split}
 \tag{10}
$$

The $\beta$ derivative is squared inside the integral, not estimated by the square of a pointwise endpoint bound.

The major main function in (9) has $L^2(\mathfrak M)$ norm $O_\epsilon(Q^\epsilon)$: the squared norm is at most $\|\rho_V\|_2^2\sum_{q\le P}\mu^2(q)/\phi(q)$, by Plancherel. By Cauchy the coefficient error from replacing the product of both actual major functions by both main functions is at most $O_\epsilon(Q^\epsilon P\sqrt{M/Q})$ for each alias, uniformly in $N$. This controls the two cross terms and the double-error term, since $P\sqrt{M/Q}\le1$. The same proof applies to $A_V(-\alpha)$ by symmetry. Summing aliases and entries costs $O_\epsilon(Q^\epsilon P M^{3/2}Q^{-1/2})$.

## 4. Major main equals the exact continuous model up to a small uniform error

For the coefficient $s=2kn>0$, the two main functions in (9) contribute

$$
 \sum_{q\le P}\frac{\mu^2(q)c_q(s)}{\phi(q)^2}
       \int_{-\delta_q}^{\delta_q}
            B_V(\varepsilon_1\beta)B_U(\varepsilon_2\beta)e(-s\beta)\,d\beta ,
 \tag{11}
$$

where $c_q(s)=\sum_{a\bmod q}^{*}e(as/q)$ is the Ramanujan sum. Product decay of $B_V,B_U$ gives integral tails bounded by $O((\sqrt{X_VX_U}\,\delta_q)^{-1})\ll q/P$. The inequality $|c_q(s)|\le\sum_{d\mid(q,s)}d$ gives, uniformly for $1\le s\le 8QM$,

$$
 \sum_{q\le P}\frac{q|c_q(s)|}{\phi(q)^2}\ll_\epsilon Q^\epsilon,\qquad
 \sum_{q>P}\frac{\mu^2(q)|c_q(s)|}{\phi(q)^2}\ll_\epsilon Q^\epsilon/P.
 \tag{12}
$$

For the first bound, use $\phi(q)^{-2}\ll_\eta q^{-2+2\eta}$ and $\sum_{q\le P}\sum_{d\mid(q,s)}d/q\ll\tau(s)\log(2P)$. For the second, write $q=de$ with $d\mid s$ and sum $d^{-1+2\eta}\sum_{e>P/d}e^{-2+2\eta}$. Each $d$ contributes $O_\eta(P^{-1+2\eta})$, also when $d>P$; choose $\eta$ small relative to $\epsilon$. Thus extending the integrals in (11) to $\mathbb R$ and the arithmetic series to $q\ge1$ costs $O_\epsilon(Q^\epsilon/P)$ per alias; the full integral is bounded by $\|\rho_V\|_2\|\rho_U\|_2$.

The absolutely convergent series is exactly $\mathfrak S(s)$ by the Euler factors $1+c_p(s)/(p-1)^2$, including the factor 2 at $p=2$ since $s$ is even. The real-line integral, by convolution/Fourier inversion with the signs shown, is
$\int \rho_V(x)\rho_U(\varepsilon_2(s-\varepsilon_1 x))\,dx$.
This is precisely (4), with no averaging or change of the benchmark. Summing the $O(Q^\epsilon/P)$ entrywise alias errors contributes $O_\epsilon(Q^\epsilon M/P)$ in HS.

## 5. Endpoints, exponents and scope

Combine the genuine weight substitution, the proper-power restoration, (7), the integrated major error and (12). This proves (2). The two minor exponents are $(1+2\gamma-\xi-d)/2$ and $3/10+4\gamma/5-d/2$. The other exponents are $\xi+3\gamma/2-1/2,\ \gamma-\xi,\ \gamma-1/2$, and for the freezing error at most $-1/40$. At the three parameter choices every exponent is at most $-1/400$; $L^{5/2}Y^{-1/5}=o(L^{-K})$. Only the major error in §3 needs auxiliary Dirichlet GRH up to $P$; the weight/operator construction requires the separate original local Dirichlet GRH.

For each parameter choice, the number of selected moduli with this compression HS norm above $L^{-K}$ is at most

$$
 O_\epsilon\big(Q^\epsilon L^{2K} M[QM/P+(QM)^{3/5}]\big).
 \tag{13}
$$

Indeed all the non-minor terms are bounded pointwise by $o(L^{-K})$; then use the unnormalized square sum (6) and the Chebyshev bound. This exceptional-count estimate does not itself require $J\gg Q^d$, only $\Delta\le Q^{19/20}$ and the same physical-radius and auxiliary hypotheses. For the three printed choices its $Q$-exponents before $\epsilon$ are at most $0.640,\ 0.765,\ 0.9225$, respectively. Thus the conclusion also applies to large modulus subsets within each window, such as an arithmetic progression of $n=N/2$ that retains $\gg Q^d$ moduli, with no local GRH required at discarded moduli. Since operator norm is bounded by HS, the same conclusion holds for the compression's operator norm. It says nothing about any named individual modulus or the full $T_N$.
