# Full growing physical-prefix variance of the genuine operator

**Scope.** The result concerns every spatial direction in the genuine physical prefix $(0,M]$, not just exterior mean differences, whole-cell means, or a finite-dimensional compression. It is an ordinary selected-modulus mean-square estimate and an exceptional-count bound, not a pointwise theorem for a specified $N$, a bound on the complement of the prefix, or a proof of weak S.

## Statement

Write $L=\log Q$. Let $\mathcal A$ be any set of $J\ge1$ distinct even integers in $[Q,2Q]$, $1\le M\le Q^\gamma$, $Y=Q^{-\sigma}$, and $P=\lfloor Q^\xi\rfloor$, for fixed exponents

$$
 0<\gamma<\sigma,\qquad \gamma+\sigma<\xi,\qquad
 \xi+\tfrac32\gamma<\tfrac12 .
 \tag{1}
$$

Assume the original local Dirichlet GRH for each $N\in\mathcal A$ to identify the true Hardy realization, and auxiliary Dirichlet GRH for all integers $q\le P$ for prime sums. These are separate assumptions; global Dirichlet GRH suffices. Let $P_M$ be the orthogonal projection onto $L^2((0,M],du)$ in the genuine physical coordinate of the paper. For every $\epsilon>0$,

$$
 \left(\operatorname{Avg}_{N\in\mathcal A}
       \|P_MT_NP_M\|_{\mathrm{HS}}^2\right)^{1/2}
 \ll_\epsilon Q^\epsilon\left[
 \frac{\sqrt M}{\sqrt J}\left(\sqrt{QM/P}+(QM)^{3/10}\right)
 +\frac{P M^{3/2}}{\sqrt Q}+\frac{M}{PY}
 +\frac{M}{\sqrt{QY}}+\sqrt{YM}\right].
 \tag{2}
$$

In particular, with $\sigma=3/20$ and $J\gg Q^d$, each of the three choices

$$
 (d,\gamma,\xi)
 =(129/200,1/40,11/25),\quad(77/100,3/40,77/200),\quad
 (93/100,3/25,127/400)
 \tag{3}
$$

gives $O_\epsilon(Q^{-1/400+\epsilon})$. This applies to all even moduli in each window of length at least a fixed positive multiple of $Q^d$, or any selection of that many from the full shell. No upper bound on the selection's diameter other than the shell is needed. R47's same explicit exponent choices controlled only the particular exterior mean-difference directions, had a lower spatial endpoint $e^H$, and required the modulus span at most $Q^{19/20}$.

## 1. Exact physical realization and common raw test spaces

Use the [exact physical cumulative kernel](source-round2.md). Write

$$
 w_N(u)^{-1/2}
  =\big((Nu)^{-2/\log N}+(Nu)^{-1/4}\big)^{1/2},\qquad
 r_N(u)=u^{-3/2}w_N(u)^{-1/2}.
$$

For an $L^2$ physical test $f$ supported in a compact interval away from zero its raw weight is

$$
 \rho_{N,f}(x)=\frac{\sqrt{2\pi x}}N\int_{u\ge x/N}r_N(u)f(u)\,du
 \qquad (x>0).
 \tag{4}
$$

The exact matrix of $T_N$ on two such tests is the signed arithmetic-minus-model sum over $m=x+kN,\ m=x-kN,\ m=kN-x$, for $k\ge1$, with signs $+,+,-$, respectively. The arithmetic weight on each admissible integer pair is $\Lambda(x)\Lambda(m)\rho_{N,f}(x)\rho_{N,g}(m)$, with $(xm,N)=1$. The model is $\mathfrak S(kN)\int\rho_{N,f}(x)\rho_{N,g}(m(x,N))\,dx$, with $\rho$ extended to zero at nonpositive arguments. The normalization follows directly from the source-round2.md kernel: the atom $N^{-1}\Lambda(x)\Lambda(m)$ or line measure $\mathfrak S(kN)d(x/N)$, together with the two physical Volterra weights evaluated at $x/N,m/N$, supplies exactly the product (4) in raw coordinates. There is no difference line $k=0$. Fubini on finite supports and density extend the formulas to the stated $L^2$ tests.

Split $[Y,M]$ into dyads $I_V=[V,2V)\cap[Y,M]$, $V=2^jY$, with the top one possibly shortened. Use the fixed external spaces $\mathcal H_V=L^2([V,4V],dz)$, their direct sum $\mathcal H$, and the real anchor $r_Q$ given by the same formula. No GRH is assumed for the anchor, which is just a weight. For $a=N/Q\in[1,2]$ send $f|_{I_V}$ to the element

$$
 \Phi_{N,V}f(z)=a^{-2}\frac{r_N(z/a)}{r_Q(z)}f(z/a)
 \quad(z\in aI_V)
 \tag{5}
$$

in $\mathcal H_V$, with zero extension. These maps give $\|\Phi_N\|\ll1$ on the direct sum: the raw argument $Qz=N(z/a)$ is identical in both weights, $z\in[Y,4M]$, and their Hardy factors are comparable. For example, $Qz\ge QY=Q^{1-\sigma}\ge1$, and $\log(Qz)\ll L$ gives uniformly comparable powers $(Qz)^{-2/\log N},(Qz)^{-2/\log Q}$. The physical powers differ by the bounded factor $a^{3/2}$; the substitution $dz=a\,du$ controls the norm. Under (5) the raw weights are exactly preserved: $a^2/(aN)=1/Q$ after changing $z=au$ in (4).

Thus form an operator $\mathcal X_N$ on $\mathcal H$ by the same signed alias and continuous expressions with the fixed raw weights $\rho_{Q,\varphi}$, for arbitrary $\varphi\in\mathcal H_V$. No disjointness of the fixed external intervals is needed; this is a direct sum. Then

$$
 P_{[Y,M]}T_NP_{[Y,M]}=\Phi_N^*\mathcal X_N\Phi_N
 \quad\text{on }L^2([Y,M]),\qquad
 \|P_{[Y,M]}T_NP_{[Y,M]}\|_{\mathrm{HS}}\ll\|\mathcal X_N\|_{\mathrm{HS}} .
 \tag{6}
$$

We can bound the whole fixed raw operator and restrict by (6), so no mean-zero condition, approximation of the moving endpoints, or rank loss is involved.

## 2. Vector weights and proper-power and unit errors

Choose any fixed real orthonormal basis $(\varphi_i)$ of $\mathcal H_V$, put $Z=QV$, and let $h_V(x)=(\rho_{Q,\varphi_i}(x))_i$, extended by zero off $[0,4Z]$. Write $R(v)=V^{3/2}r_Q(Vv)$ and $\varphi_i^{(V)}(v)=\sqrt V\,\varphi_i(Vv)$ on $[1,4]$. Then $R$ is uniformly bounded by the true Hardy formula, and

$$
 \rho_{Q,\varphi_i}(x)=Z^{-1/2}\sqrt{2\pi s}\,C_i(s),\quad
 s=x/Z,\qquad
 C_i(s)=\int_1^4{\bf1}_{v\ge s}R(v)\varphi_i^{(V)}(v)\,dv .
 \tag{7}
$$

In particular $C_i(s)$ is constant for $0<s<1$; this part is retained, not set to zero. Bessel gives $\sum_i|C_i(s)|^2\ll1$ and $\|h_V(x)\|\ll\sqrt{x}/Z$, so $\int\|h_V(x)\|^2dx\ll1$. For any unit scalar test the corresponding $\rho$ is zero at $0,4Z$, with variation $O(Z^{-1/2})$ and $L^1$ norm $O(\sqrt Z)$: differentiate $\sqrt{s}C(s)$, use the integrable $s^{-1/2}$ factor and $C'(s)=-R(s)\varphi^{(V)}(s)$ on $[1,4]$, in $L^1$. Consequently the vector Fourier transform $B_V(\beta)=\int h_V(x)e(x\beta)\,dx$, $e(t)=e^{2\pi it}$, satisfies

$$
 \|B_V(\beta)\|\ll \sqrt Z\min(1,(Z|\beta|)^{-1}),\qquad
 \int_{\mathbb R}\|B_V(\beta)\|^2\,d\beta\ll1 .
 \tag{8}
$$

These statements follow by duality and Plancherel, respectively, and are independent of spatial dimension.

Consider a fixed pair of dyads $V,U$. Only $k\le 8M$ can occur since both raw axes are at most $4QM$ and $N\ge Q$. Each pair-weight matrix $h_V(x)\otimes h_U(m)$ has HS norm $\ll (Q\sqrt{VU})^{-1}$, by (7). Remove all proper powers and then allow all ordinary primes, including $p\mid N$, in the arithmetic expressions. For each proper power on either leg there are at most $O(M)$ partners; the number of powers is $O(\sqrt{Q\max(V,U)}L)$. The weight product includes $O(L^2)$ von Mangoldt factors. For prime divisors of $N$ the analogous count on either leg is $O(L)$ instead. Thus the HS error costs $O(L^3 M/\sqrt{QY})$ per dyad pair. This error also accounts for any reflected equal-prime term introduced by dropping the unit restriction: an arithmetic prime on $2p=kN$ divides $N$ whenever $N$ is even. Only $O(L)$ dyads are used, so their HS matrix errors are absorbed into $Q^\epsilon M/\sqrt{QY}$. The continuous model is unchanged.

Put $A_V(\alpha)=\sum_p(\log p)h_V(p)e(p\alpha)$. By vector Parseval and Chebyshev,

$$
 \int_{\mathbb R/\mathbb Z}\|A_V(\alpha)\|^2\,d\alpha
 \ll Z^{-1}\sum_{p\le4Z}(\log p)^2\ll L .
 \tag{9}
$$

The ordinary-prime alias on $N=2n$ is the tensor Fourier coefficient of $A_V(\varepsilon_1\alpha)\otimes A_U(\varepsilon_2\alpha)$ at $s=2kn$, with $(\varepsilon_1,\varepsilon_2)=(-,+),(+,-),(+,+)$ in the displayed order of the physical lines. Tensor norm is HS norm. All formulas can first be applied to finite basis truncations, with constants independent of the truncations; equivalently the vector or tensor integrals exist by the stated bounds.

## 3. Minor arcs: vector Bessel and divisor multiplicity

Use the same torus major arcs as [R47](r47-operator-direct-short-window-variance.md), centered at reduced $a/q$, $q\le P$, radius $\delta_q=2P/(qQ)$; they are disjoint for large $Q$ because $P^2/Q=o(1)$. The symmetric minor set admits approximants with $P<q\le Q/P$, $|\alpha-a/q|\le q^{-2}$. The standard Vaughan bound for $\sum_{x\le t}\Lambda(x)e(x\alpha)$ has terms $t/\sqrt q,t^{4/5},\sqrt{tq}$, times $\log^{5/2}(2t)$ ([Koukoulopoulos, Theorem 23.8](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=258)). Remove proper powers and apply Abel summation with $\sqrt x$ to bound all prime sums $\sum_{p\le Zv}\sqrt p(\log p)e(p\alpha)$, $1\le v\le4$, by $L^{O(1)}\sqrt Z(Z/\sqrt q+Z^{4/5}+\sqrt{Zq})$. From (7) the coefficient $A_{V,i}$ is the pairing of $\varphi_i^{(V)}(v)$ with this weighted cumulative sum times $\sqrt{2\pi}R(v)/Z$. Bessel therefore gives

$$
 \sup_{\mathfrak m}\|A_V(\alpha)\|\ll L^{O(1)}
 \big(\sqrt{QM/P}+(QM)^{3/10}\big).
 \tag{10}
$$

Indeed the normalizing factor is $1/Z$, the third term is at most $\sqrt{Q/P}$, and $M\ge1$. The case $t<2$ contributes no prime sum.

Fix a dyad pair and orientation, and let $c_s$ be the HS-valued tensor Fourier coefficients on the minor set. For the selected $n=N/2$, Cauchy first in $k$, followed by the divisor bound ($1\le 2kn\le16QM$) gives

$$
 \sum_{2n\in\mathcal A}\Big\|\sum_{1\le k\le8M}c_{2kn}\Big\|_{\mathrm{HS}}^2
 \ll_\epsilon M Q^\epsilon \sum_{s\in\mathbb Z}\|c_s\|_{\mathrm{HS}}^2 .
 \tag{11}
$$

For a fixed integer $s$, at most $\tau(s)$ pairs $(k,n)$ occur; no interval structure is used. Vector Parseval, (9), and (10) bound the right hand side. After dividing by $J$ and taking roots, the resulting contribution is the first term of (2), including the $Q^\epsilon$ loss for summing $O(L^2)$ dyad pairs and three signs.

## 4. Major arcs: vector GRH error and exact signed benchmark

For $q\le P$ and unit residues $r\bmod q$, set $F_r(t)=\sum_{p\le t,\ p\equiv r\ (q)}\log p-t/\phi(q)$, and $F_r=0$ on nonunits. For all $0<t\le4Z$, the auxiliary GRH prime number theorem for characters ([Koukoulopoulos, Exercise 11.2(a)](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=126)), removal of proper powers, and finite character Parseval imply

$$
 \sum_r |F_r(t)|^2\ll t L^4 .
 \tag{12}
$$

For $t<2$ this follows directly from $F_r=-t/\phi(q)$. The maximum $qt$ for the other values is polynomial in $Q$. At the major point $a/q+\beta$, Abel summation over unit residues gives the main vector $(\mu(q)/\phi(q))B_V(\beta)$, with component errors of the form

$$
 -\sum_{r\bmod q}e(ar/q)
 \left(\int F_r(x)\rho_{Q,\varphi_i}'(x)e(x\beta)\,dx
   +2\pi i\beta\int F_r(x)\rho_{Q,\varphi_i}(x)e(x\beta)\,dx\right).
 \tag{13}
$$

The nonunit primes $p\mid q$ must be added separately. Their vector norm is uniformly $O(L/\sqrt Z)$, by (7) and $\sum_{p\mid q}\log p\le\log q$. It has squared arc integral $O(L^2/Z)$, since the major arcs are disjoint.

For the derivative term in (13) the sum of squared integrals over $r,i$ is $O(L^4)$, uniformly in $\beta$. To see this, differentiate (7). The $\sqrt{s}$-derivative term has $Z^{-3/2} C_i(x/Z)/\sqrt{x/Z}$ up to a constant. The $(r,i)$-vector under the integral before the $Z^{-3/2}$ factor has norm $O(\sqrt Z L^2)$ by (12), also near $x=0$; integrate over length $4Z$. The cumulative-derivative term is supported at $1\le s\le4$; substituting $x=Zs$ gives an integral pairing with $\varphi_i^{(V)}(s)$ times $Z^{-1/2}\sqrt{s}R(s)F_r(Zs)e(Zs\beta)$. Sum its squares over $i$ by Bessel and then $r$ by (12), giving $O(L^4)$. For the term multiplied by $\beta$, use real-line Plancherel:

$$
 \sum_{r,i}\|F_r\,\rho_{Q,\varphi_i}\|_2^2
 \ll L^4\int_0^{4Z} x\|h_V(x)\|^2dx\ll Z L^4 .
$$

Applying finite Parseval over $a\bmod q$ to (13), and adding the nonunit error, bounds the squared $L^2(\mathfrak M)$ vector error by

$$
 O\!\left(L^4\sum_{q\le P}q(\delta_q+\delta_q^2 Z)+L^2/Z\right)
 \ll L^5P^2(1+V)/Q+L^2/Z .
 \tag{14}
$$

The $L^2(\mathfrak M)$ main vector norm is $O_\epsilon(Q^\epsilon)$, by (8) and $\sum_{q\le P}\mu^2(q)/\phi(q)\ll_\epsilon Q^\epsilon$. It follows by Cauchy that the product replacement, in each coefficient and each dyad pair, is $O_\epsilon(Q^\epsilon(P\sqrt{M/Q}+(QY)^{-1/2}))$ in tensor norm. This absorbs the double-error term as both parameters tend to zero under (1). By symmetry the negative arguments are covered too. Summing $O(M)$ aliases and $O(L^2)$ dyad pairs gives the second and fourth terms in (2).

The resulting exact coefficient is

$$
 \sum_{q\le P}\frac{\mu^2(q)c_q(s)}{\phi(q)^2}
     \int_{-\delta_q}^{\delta_q}
       B_V(\varepsilon_1\beta)\otimes B_U(\varepsilon_2\beta)e(-s\beta)\,d\beta .
 \tag{15}
$$

The bound (8) gives integral tails $O(q/(P\sqrt{VU}))$ in tensor norm. For $1\le s\le16QM$, the same divisor estimates as R47 follow from $|c_q(s)|\le\sum_{d\mid(q,s)}d$:

$$
 \sum_{q\le P}\frac{q|c_q(s)|}{\phi(q)^2}\ll_\epsilon Q^\epsilon,\qquad
 \sum_{q>P}\frac{\mu^2(q)|c_q(s)|}{\phi(q)^2}
       \ll_\epsilon Q^\epsilon/P.
 \tag{16}
$$

For the first, write $q=de$, use $\phi(q)^{-2}\ll_\eta q^{-2+2\eta}$, and sum $\sum_{e\le P/d}e^{-1}$ with $P^{2\eta}\tau(s)$. For the second, $\sum_{e>P/d}e^{-2+2\eta}d^{-1+2\eta}\ll_\eta P^{-1+2\eta}$ uniformly, including $d>P$. Choose $\eta$ sufficiently small. The full $\beta$-integral has bounded tensor norm by Cauchy and (8). Thus extending both the integral and the series costs $O_\epsilon(Q^\epsilon/(PY))$ per dyad pair and alias. The absolutely convergent Ramanujan series is exactly $\mathfrak S(s)$: at a prime $p$ its factor is $1+c_p(s)/(p-1)^2$, giving 2 at $p=2$ since $s$ is even. The full Fourier integral equals
$\int h_V(x)\otimes h_U(\varepsilon_2(s-\varepsilon_1x))\,dx$
by Fourier inversion (componentwise, or by Bochner integration). This is precisely the continuous model from (4). The three signs are unmodified. The model errors give the third term of (2).

## 5. The origin row and conclusion

It remains to pass from $[Y,M]$ to the full prefix $(0,M]$. The exact cumulative kernel has the form $2\pi(xy)^{-3/2}w_N(x)^{-1/2}w_N(y)^{-1/2}$ times the signed cumulative atom-minus-line mass weighted by $\sqrt{uv}$ on $(0,x]\times(0,y]$. For $x\le Y<1/4$ there is no alias unless $y\ge3/4$. In that case there are $O(y)$ possible lines. On each line there are at most $Nx$ actual points, the atom scale is $1/N$, $\Lambda(n)\Lambda(m)\ll L^2$, and the weighted factor is at most $\sqrt{xy}$. The continuous line has length $O(x)$ in the first-coordinate parameter and $\mathfrak S(kN)\ll_\epsilon Q^\epsilon$. Thus the absolute cumulative mass is $O_\epsilon(Q^\epsilon x^{3/2}y^{3/2})$, using zero atomic mass if $x<1/N$. The displayed factors from $w_N$ are bounded when the raw coordinate is at least one; at $x<1/N$ the factor is $O((Nx)^{-1/8})$ for large $Q$, which has squared integral $O(1/N)$ there. Since $Y>1/N$, the edge HS norm is $O_\epsilon(Q^\epsilon\sqrt{YM})$, uniformly in $N$; symmetry handles the other edge. This gives the final term in (2).

The first term in (2) gives $Q$-powers $(1+2\gamma-\xi-d)/2$ and $3/10+4\gamma/5-d/2$ if $J\gg Q^d$; the other powers are $\xi+3\gamma/2-1/2,\ \gamma+\sigma-\xi,\ \gamma-(1-\sigma)/2,\ (\gamma-\sigma)/2$. All are at most $-1/400$ in (3) with $\sigma=3/20$. Independently, by (11) without normalizing by $J$, for the examples in (3) the number of selected $N$ where the HS norm exceeds $Q^{-1/800}$ is

$$
 \ll_\epsilon Q^{1/400+\epsilon}M\big(QM/P+(QM)^{3/5}\big).
 \tag{17}
$$

Indeed all other contributions are bounded pointwise by $O_\epsilon(Q^{-1/400+\epsilon})=o(Q^{-1/800})$ for sufficiently small $\epsilon$. Formula (17) does not require a lower bound on $J$, and for the three sample radii the exceptional-count exponents are respectively $0.6425,\ 0.7675,\ 0.925$ before $\epsilon$. It also bounds the exceptions for the compression's operator norm, by HS domination, but does not select individual successful moduli. In particular it does not ensure control on, for example, every member or most members of an arbitrary family of size $Q^{1/2}$. The exterior square complement and the two full cross blocks with $u>M$ remain outside this theorem.
