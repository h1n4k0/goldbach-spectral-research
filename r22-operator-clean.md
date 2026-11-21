# R22 operator lane: the actual uncentered exterior direction

**Scope.** This treats one specific remaining R21 direction, not the whole coarse space. Let $N$ be even, $L=\log N,\ \alpha=1/L,\ \beta=1/8,\ S=S(N)$, and $\delta_N=\sqrt{S/N}L^{3/2}$ as in R20–R21. Fix $0<\gamma<1$, $Y=N^\gamma$, $1\le U\le\min(Y,N/4)$, and put $X=NY$. Here $x,y$ are dimensionless physical coordinates, not their logarithms, and $U$ is the raw integer scale. We use local GRH(N) for the Li–Liu physical identification and the zero formula; no arithmetic sieve estimate below requires averaging over moduli. The result neither proves S nor R. No remote writes.

With $r_N(y)^2=y^{-3}[(Ny)^{-2\alpha}+(Ny)^{-2\beta}]$, define

$$
W(Y)=\int_Y^\infty r_N(y)^2\,dy
     =\sum_{a\in\{\alpha,\beta\}}\frac{(NY)^{-2a}Y^{-2}}{2+2a},
\qquad
e_Y(y)=\frac{r_N(y){\bf1}_{[Y,\infty)}(y)}{\sqrt{W(Y)}}.
$$

The sum over $a$ labels the two traces, counted separately if equal. Because the R20–R21 cells partition $[Y,\infty)$, this is precisely the embedded $c/\|c\|$ from R21, not an arbitrary smoother. In particular $\|P_U T_N e_Y - R(c/\|c\|)\|_2=o(\delta_N)$ by R21 §1, where $R$ there is the sampled coarse map, not Hypothesis R. We prove the stronger direct bound

$$
\|P_U T_N e_Y\|_2
 \ll_\gamma S\sqrt{UY/N}
  +\log(2U)\frac{U}{NY}
  +S\log\log(5+Y)\sqrt{\frac{U}{NY}} .                         \tag{1}
$$

For example $U=Y=N^{3/40}$ gives $O(SN^{-17/40})$. Thus the genuinely uncentered direction is now negligible at any fixed inverse-log S scale in that setting. The same argument for $P_U T_N e_Y$ does **not** give $o(\delta_N)$ at that polynomial scale, and does not estimate the c-perpendicular separated covariance. The same inverse-power conclusion holds for the sampled $R(c/\|c\|)$ at $U=Y=N^{3/40}$ by the explicit R21 sampling error.

## 1. Exact smoothed opposite-progression moment

Let $\eta_a=(NY)^{-2a}Y^{-2}/[(2+2a)W(Y)]$, so $\sum_a\eta_a=1$. Set

$$
\Omega(v)=
\begin{cases}
\sqrt v, &0<v\le1,\\
\sum_a\eta_a v^{-3/2-2a}, &v>1.
\end{cases}
\quad
H_n(X)=\sum_{m\ge1}\Lambda(m)
     \bigl({\bf1}_{m\equiv n\ (N)}-{\bf1}_{m\equiv-n\ (N)}\bigr)\Omega(m/X).
\tag{2}
$$

Here $n$ ranges over units up to $U$, and all the $m$ admitted by the signs are units. The series is absolutely convergent. In notation $d(t)^2=t^{-2\alpha}+t^{-2\beta}$, define the raw low synthesis map

$$
(\mathcal V_U H)(t)=t^{-3/2}d(t)
    \sum_{\substack{n\le t\\(n,N)=1}}\Lambda(n)\sqrt n\,H_n,
      \qquad 0<t\le U.
$$

Let $\mathcal U_N f(t)=N^{-1/2}f(t/N)$, the unitary rescaling of the low space. The exact character covariance of R20, integrated against $e_Y$ on the right, gives

$$
\mathcal U_N P_U P_N e_Y
   = \frac{2\pi\sqrt{YW(Y)}}{\sqrt N}\,\mathcal V_U H.           \tag{3}
$$

Indeed the cumulative signed $A_n(y)$ of R21 is paired with $r_N(y)^2/\sqrt{W(Y)}$. When $m$ is fixed the remaining high weight is $W(\max(Y,m/N))/\sqrt{W(Y)}$; multiplying by $\sqrt{m/N}$ gives exactly $\sqrt{YW(Y)}\Omega(m/X)$. The low $N$-factors then give (3). This checks the whole normalization before any approximation. In particular $W(Y)\asymp_\gamma Y^{-2}$, since $(NY)^{-2\alpha}=e^{-2(1+\gamma)}$.

For a uniform scalar bound use R21 (4), or the same [Montgomery–Vaughan Brun–Titchmarsh bound](https://doi.org/10.1112/S0025579300004708) for first weights plus R21's proper-power count, to obtain

$$
\sum_{m\le NV,\ m\equiv b\ (N)}\Lambda(m)\ll_\gamma S V,\qquad V\ge Y
\tag{4}
$$

for a unit residue $b$. Explicitly the primes are $\ll (N/\phi(N))V/\log(2V)$; multiply by $\log(2NV)$ and use $V\ge N^\gamma$. The proper powers in the proof of R21 (4) are $O_\gamma(V^{3/4}+V^{1/2}\log(2NV))$ before weighting, hence absorbed. Apply (4) at $V=Y$ to $m\le X$ and at $V=2^{k+1}Y$ to the dyads above $X$, using $\Omega(v)\le v^{-3/2}$ above 1. The sum of the dyadic upper bounds is $O_\gamma(SY)$, so $\sup_n|H_n(X)|\ll_\gamma SY$. The elementary inequality

$$
\|\mathcal V_U H\|_2\ll \sqrt U\,\sup_n|H_n|
\tag{5}
$$

follows by $\sum_{n\le t}\Lambda(n)\sqrt n\ll t^{3/2}$, $d(t)^2\le2$ where the sum is nonzero. Substituting into (3), and using R20 §2 for the entire diagonal and Beta cross, proves (1). Crucially this integrates the actual high weight before applying the arithmetic bound; it does not assert an $S\sqrt{UY/N}$ Hilbert–Schmidt bound over the complete high exterior.

## 2. Rigorous deletions at the R scale

Even at $U=Y=N^{3/40}$, we can replace the $H_n$ in (3) by sums over the shorter alias range

$$
                    N Y^{1/3}<m\le N Y^3
\tag{6}
$$

with error $o(\delta_N)$ in the direction norm. This also holds for every fixed $\gamma$ and the stated $U\le Y$. To see the low deletion, take $B=Y^{1/3}$. There are $O(B+1)$ integers in either residue below $NB$, each $\Lambda(m)\le O_\gamma(L)$ and $\Omega(m/X)\le\sqrt{B/Y}$. The removed $H_n$ is $O_\gamma(LB^{3/2}/\sqrt Y)$; (3)–(5) give the error

$$
O_\gamma\!\left(L\sqrt{U/N}\,B^{3/2}/Y\right)
  =O_\gamma(L/\sqrt N)=o(\delta_N).
$$

For the high deletion take $Z=Y^3$. Apply (4) to dyads above $NZ$, with $\Omega(m/X)\le(m/X)^{-3/2}$. The removed $H_n$ is $O_\gamma(SY^{3/2}/\sqrt Z)$; the error is

$$
O_\gamma\!\left(S\sqrt{U/N}\,Y/\sqrt Z\right)
  =O_\gamma(S/\sqrt N)=o(\delta_N).
$$

We used $S\ll\log\log(3N)$ and $S$ bounded below by a positive absolute constant for even $N$. This is a cutoff of the underlying arithmetic partners in this single high direction, not a theorem for an operator block cut at those physical heights.

One can also delete all high-side proper powers from (2) at $o(\delta_N)$ if $U\le Y N^{-\eta}$ for fixed $0<\eta<\gamma$, or for all $U\le Y$ on moduli with $\omega(N)$ bounded. Here $\omega(N)$ is the number of distinct prime factors. For the first assertion, fix any $\epsilon>0$. Through $V\ge Y$, the count in each unit progression of powers of each fixed degree $2\le j\le J$ is $O_{J,\epsilon}(N^{\epsilon/2}[1+\sqrt{V/N}])$, from the CRT root count of R21. The weights are at most $\log(2NV)$; summing against $\Omega$ on dyads with $V=2^kY$, and treating the initial $m\le X$ with weight at most 1, makes their contribution $O_{\gamma,J,\epsilon}(N^\epsilon)$, since $Y<N$. For degrees $j>J$ the unrestricted count through $NV$ is $O((NV)^{1/(J+1)}\log(2NV))$; the same dyadic sum, with the additional Mangoldt log, is $O_\gamma(X^{1/(J+1)}L^2)$. Choose $J$ large enough that this is $O_\gamma(N^\epsilon)$, then (3)–(5) give $O_\gamma(N^{-1/2+\epsilon}\sqrt{U/Y})=o(\delta_N)$ for $\epsilon<\eta/2$. If $\omega(N)$ is bounded, the fixed-degree root counts are bounded in terms of $J,\omega(N)$, so the fixed-degree contribution is $O_{\gamma,J,\omega(N)}(L)$ per $n$, already sufficient for $U\le Y$. For the degrees $j>J$, their total $\ell^1$ mass over $n$ is at most the unrestricted weighted count $O_\gamma(X^{1/(J+1)}L^2)$, because the disjoint residues $\pm n$ can use each $m$ only once. The $\ell^2$ bound below thus gives $o(\delta_N)$ if $(1+\gamma)/(J+1)<\gamma/2$. We do not obtain this full proper-power deletion at $U=Y$ for every modulus.

## 3. Actual zero filter and its R-scale uniform tail

The Mellin filter in (2) is exact:

$$
\widehat\Omega(s)=\sum_a\frac{\eta_a(2+2a)}
             {(s+1/2)(3/2+2a-s)},\qquad -1/2<\Re s<3/2+2\min(a).
$$

Equivalently, pair the R20 genuine zero realization on the high line against $e_Y$. For each $\chi$, the high atom paired with $e_Y$ has main term

$$
\sqrt{2\pi}\,Y\sqrt{W(Y)}
  \sum_{\rho_\chi=1/2+i\tau}
     m_\chi(\tau) X^{i\tau}\widehat\Omega(1/2+i\tau),
\tag{7}
$$

with error $O_\kappa(L X^{-\kappa})$ for $0<\kappa<1/2$ from R20 §3. The $m_\chi$ are the multiplicities of primitive nontrivial zeros; summation is over distinct ordinates before counting multiplicity. The sign in (7) is positive for the high atom $p_\chi=-\sqrt{2\pi}r_N N^{-1}\sum\Lambda\chi\sqrt n$. Indeed integrating $y r_N(y)^2 (Ny)^{i\tau}/(1+i\tau)$ gives exactly

$$
Y W(Y)\,X^{i\tau}\sum_a
      \frac{\eta_a(2+2a)}{(1+i\tau)(1+2a-i\tau)} .
$$

To justify the pairing with a nonsmooth cutoff, the absolutely convergent quadratic denominator sum may also be obtained directly by Mellin inversion of the continuous $\Omega$ in (2). On $1<\Re s<3/2+2\min(a)$, $\sum_m\Lambda(m)\chi(m)\Omega(m/X)$ is the integral of $(-L'/L)(s,\chi) X^s\widehat\Omega(s)$ divided by $2\pi i$. Shift to $\Re s=1/2-\kappa>0$, crossing precisely the nontrivial zeros under local GRH(N). The sign on that prime sum is negative, canceled by that of $p_\chi$; the missing Euler factors have poles at $\Re s=0$ only. The usual local logarithmic derivative bound used in R20 and its shifted contour (away from zeros) makes the vertical integral $O_\kappa(L X^{1/2-\kappa})$, prior to dividing by $\sqrt X$. One may choose a sequence of horizontal sides at distance $\gg1/\log(N(2+|T|))$ from all ordinates of the fixed $\chi$, by the unit-bin zero count; the squared-denominator filter then makes the horizontal integrals vanish. Formula (7) introduces no zero-spacing conjecture.

For the conversion to an operator error we use

$$
\|\mathcal V_U\|_{\ell^2\to L^2}\ll \sqrt{\log(2U)}.            \tag{8}
$$

The column Gram has entries $\ll\Lambda(n)\Lambda(m)\sqrt{nm}/\max(n,m)^2$. For nonzero columns use Schur weights $h_m=\Lambda(m)/\sqrt m$; the weighted row sums divided by $h_n$ are
$\ll n^{-1}\sum_{m\le n}\Lambda(m)^2+n\sum_{m>n}\Lambda(m)^2/m^2\ll\log(2n)$, using Chebyshev. The normalized odd-character vectors $\chi\mapsto\chi(n)$ for distinct units $n\le U<N/4$ are orthonormal, so the synthesis operator from the probability-weighted odd-character space to the low physical space using $P_U p_\chi$ has norm $O(\sqrt{\log(2U)})$ by (8), absorbing $\sqrt{2\pi}$. This applies equally with complex conjugation in the high inner product.

The unit-bin zero count and the quadratic denominators show absolute convergence in (7) and yield

$$
\sum_{|\tau|>T} m_\chi(\tau)\,
      |\widehat\Omega(1/2+i\tau)|\ll (L+\log(2+T))/T
       \qquad(T\ge2).
$$

Since $Y\sqrt{W(Y)}\asymp_\gamma 1$, the low norm error when replacing the high atoms by (7) truncated at $|\tau|\le T$ is

$$
O_{\gamma,\kappa}\!\left(\sqrt{\log(2U)}
      \left[L X^{-\kappa}+\frac{L+\log(2+T)}{T}\right]\right).
$$

Taking $1/[2(1+\gamma)]<\kappa<1/2$, and $T=\sqrt N L^\epsilon$ for any fixed $\epsilon>0$, this is $o(\delta_N)$. The real sign-sensitive arithmetic coefficients after averaging are those of (2); no random phases or unconditional low-frequency decorrelation have been substituted. A low-ordinate nonvanishing moment as in R19 does not bound the translated expression $\sum_\tau X^{i\tau}m_\chi(\tau)\widehat\Omega(1/2+i\tau)$.

## 4. Remaining R obstruction on the actual direction

At $o(\delta_N)$ accuracy the diagonal and Beta terms vanish, and (3) shows that $o(\delta_N)$ on this direction is exactly the assertion

$$
\|\mathcal V_U H\|_2=o\bigl(\sqrt{SY}\,L^{3/2}\bigr).
$$

For $3\nmid N$ and $U\ge4$, the fixed output interval $3\le t<4$ contains only the one unit Mangoldt atom $n=3$ (since $N$ is even). Thus this little-o bound implies the concrete single signed moment

$$
\left|\sum_m \Lambda(m)
      ({\bf1}_{m\equiv3\ (N)}-{\bf1}_{m\equiv-3\ (N)})\Omega(m/X)\right|
     =o\bigl(\sqrt{SY}\,L^{3/2}\bigr).
$$

It is enough here to keep only ordinary primes, by the proper-power deletion for fixed $U=4$, or directly at this one coordinate by its per-residue bound above. This implication is a necessary obstruction to the stated little-o target, not a counterexample or a claim that the published non-strict R hypothesis itself implies little-o. Under a norm upper bound of size $\delta_N$, the same test yields the corresponding big-O moment bound. The local GRH individual contour estimate for this smoothed moment is $O(\sqrt X L)$ from (7), and (4) instead gives $O_\gamma(SY)$; neither provides the requisite signed cancellation at fixed polynomial $Y$. Sections 2–3 do narrow the actual remaining arithmetic and spectral contributions at the R scale. They do not resolve either of them or the R21 separated covariance.
