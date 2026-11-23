# Actual complementary energy and shifted-character projections at critical prime denominators

Let $N$ be a large even integer, $X=\sqrt N$, $L=\log N$, and $e(z)=e^{2\pi iz}$. In the [critical-prime setup](weak-s-type-ii-critical-prime-double-centered.md), let

$$
D(\alpha)=\sum_{\substack{d\in I_d,\ d\ge X,\ k>t\\
                 N-y\le dk<N/2\\ (dk,N)=1,\ (d,k)=1}}
 \mu(d)\mu^2(k)e(\alpha dk),
\tag{1}
$$

where $I_d$ is any hard interval, $t\ge N^{.49999}$, and $N/2\le y\le9N/16$. We first prove the uniform unconditional bound

$$
\int_0^1|D(\alpha)|^2\,d\alpha\ll N.
\tag{2}
$$

In particular this has no divisor-moment logarithmic loss, and the hard product gate and endpoints need not be frozen.

We then take $y=9N/16$ and the actual unselected prime inputs $E=1$, with arbitrary independent hard subintervals of $[.740X,.745X]$, $[.715X,.720X]$ and the true weight $-\log v$ and mask $(uv,N)=1$. The prime product gate $N/2<uv\le y$ is automatic. On the shell $q$ prime in $[.8X,.9X]$, $|\beta|\le1/(10N)$, write $p_q^*,d_q^*$ for the true unit-centered residue masses of $P,D$, including their respective $\beta$ phases, and zero at residue zero. Define the orthogonal projection

$$
(\Pi z)(s)=
\begin{cases}
z(s)-(q-1)^{-1}\sum_{w\ne0}z(w),&s\ne0,\\
0,&s=0.
\end{cases}
$$

At each $q,\beta$ select arbitrarily and measurably at most $K$ distinct pairs $(b,\chi)$ with $b\in\mathbb F_q$, $b\not\equiv N\pmod q$, and $\chi$ nonprincipal modulo $q$. Write $W=W(q,\beta)$ for the span of the functions $\Pi[\chi(s-b)]$ for the selected pairs (characters extended by zero at zero). Let $d_{q,W}=\operatorname{proj}_W d_q^*$, the orthogonal projection of the actual centered complementary mass. For any integer $1\le K\le\frac1{10}\sqrt{.8X}$, the unconditional assertion is

$$
\int_{-1/(10N)}^{1/(10N)}
  \sum_{\substack{q\ {\rm prime}\\ .8X\le q\le .9X}}
 \left|q\sum_{s\bmod q}p_q^*(N-s,\beta)d_{q,W}(s,\beta)\right|\,d\beta
 \ll N\sqrt{\frac{K}{L}} .
\tag{3}
$$

Thus an adaptive family of $o(\log N)$ shifted directions can be removed from the actual signed covariance. All pairings carried by each such projection are retained; this is not a selection of Jacobi product characters. The complementary projection is not estimated. The shell condition $q\nmid N$ is unnecessary here; the shift condition $b\not\equiv N$ is essential to the argument.

## 1. The sharp moving complementary energy

Any nonzero term in (1) has squarefree $m=dk$: both $d,k$ are squarefree, and $(d,k)=1$. Conversely, for squarefree $m$ every divisor splitting is coprime. Therefore the exact coefficient of $e(\alpha m)$ in (1) is

$$
\mathbf1_{N-y\le m<N/2}\mathbf1_{(m,N)=1}
\mu^2(m)\mu(m)\sum_{\substack{k\mid m,\ k>t\\ m/k\in I_d\cap[X,\infty)}}\mu(k).
\tag{4}
$$

Indeed $\mu(d)=\mu(m)\mu(k)$ in every such splitting. The characteristic factors involving $N$ and squarefreeness can be dropped **after squaring** for an upper bound, not inside the signed coefficient identity. Trivial empty windows may be omitted. Write $[A,B]$ for the effective $d$ interval, with the original choices of open/closed endpoints; take $A\ge X$ and truncate $B$ at $N/(2t)$ without removing any terms. Every possible short $k$ is $<X/2$. For fixed $k,\ell$ the allowed $m$ form the intersection of three intervals:

$$
\mathcal I(k,\ell)=[N-y,N/2)\ \cap\ k[A,B]\ \cap\ \ell[A,B],
$$

with those endpoint conventions. Thus the count of $m$ divisible by $[k,\ell]$ is $|\mathcal I(k,\ell)|/[k,\ell]+O(1)$, uniform also for empty intervals or intervals consisting of one integer. Expanding the square of the sum in (4) and summing these errors over $t<k,\ell<X/2$ costs $O(X^2)=O(N)$, after taking absolute values of $\mu(k)\mu(\ell)$ for this error only.

For every real $z\in[N-y,N/2)$, the corresponding allowed short $k$ constitute a contiguous interval $J(z)$ of integers, since $t<k<X/2$ and $z/k\in[A,B]$. The main term of the expansion is exactly

$$
\int_{N-y}^{N/2}\sum_{k,\ell\in J(z)}
       \frac{\mu(k)\mu(\ell)}{[k,\ell]}\,dz.
\tag{5}
$$

The quadratic form with kernel $1/[k,\ell]$ is positive semidefinite, by its decomposition

$$
\sum_{k,\ell}\frac{a_k\overline{a_\ell}}{[k,\ell]}
=\sum_r\phi(r)\left|\sum_{r\mid k}a_k/k\right|^2.
$$

The [Dress–Iwaniec–Tenenbaum theorem, §2](https://tenenb.perso.math.cnrs.fr/PPP/Somme-Moebius.pdf#page=2) proves convergence as $U\to\infty$ of the prefix form $\sum_{k,\ell\le U}\mu(k)\mu(\ell)/[k,\ell]$, hence its uniform boundedness for all real $U\ge0$. The exact form and boundedness are also recorded in [de la Bretèche–Dress–Tenenbaum, §1, (1.1)–(1.4)](https://tenenb.perso.math.cnrs.fr/PPP/Sxz.pdf#page=1). A contiguous interval vector is the difference of two prefix vectors, so its form is bounded by twice the sum of their forms. This bounds (5) by $O(N)$, proving (2) by Parseval. There is no dependence on the choice of sharp endpoints.

The critical arcs are disjoint modulo one: two distinct reduced centers have distance at least $1/(qq')\ge1/(.81N)$ (also on the torus), whereas their combined radii are $1/(5N)$. For fixed $q,\beta$, $D^*(a)=D(a/q+\beta)$ minus its mean over $a\ne0$, so subtracting this constant is an orthogonal projection on those numerator coordinates. Moreover $D^*(a)$ is the additive transform of $d_q^*(s,\beta)$ and its extension has value zero at $a=0$. Additive Parseval, disjointness, and (2) give

$$
\int_{-1/(10N)}^{1/(10N)}\sum_q q\|d_q^*(\cdot,\beta)\|_2^2\,d\beta
=\int_{-1/(10N)}^{1/(10N)}\sum_q\sum_{a\ne0}|D^*(a)|^2\,d\beta
\ll N.
\tag{6}
$$

No model or GRH is used.

## 2. The genuine prime shift test

If $\xi$ is any nonprincipal character and $h\in\mathbb F_q^\times$, let $T_{U,v}=\xi(Uv-h)$ with $U\in\mathbb F_q$, $v\ne0$. Its column Gram is

$$
(T^*T)_{v,w}=q\mathbf1_{v=w}-\overline{\xi(v)}\xi(w).
\tag{7}
$$

The diagonal is $q-1$. For $v\ne w$, away from its single pole the fractional linear map $(U-h/w)/(U-h/v)$ bijects to $\mathbb F_q\setminus\{1\}$, since the two roots are distinct. Its $\xi$ sum is $-1$, which gives the off-diagonal after restoring the prefactors. The pole makes zero contribution to the original Gram. In particular $\|T\|_{2\to2}\le\sqrt q$.

The actual prime factors below $q$ occur injectively as residues. Their coefficient norms on the two sides are $O(\sqrt{q/L})$ and $O(\sqrt{qL})$, respectively, by the upper bound for prime counting and the coefficient $\log v$ on the second side. All $N$-unit masks are kept, factoring as separate masks on $u,v$. The absolutely summable Taylor expansion in $(u/X)^j(v/X)^j$ of $e(\beta uv)$ has uniformly bounded coefficient absolute sum because $|\beta|N\le1/10$; each monomial is bounded by one on either interval. Equation (7) then gives

$$
\left|\sum_{r\ne0}p_q^*(r,\beta)\xi(r-h)\right|\ll q^{3/2}.
\tag{8}
$$

Here the passage from the original to the unit-centered prime mass introduces an error $O(q/L)$, since the original total weight is $O(q^2/L)$ and the sum of $\xi(r-h)$ over units has modulus at most one. This argument uses the unselected prime product and the absence of an active product endpoint on that leg; it does not assert (8) for arbitrary selectors.

For a selected pair $(b,\chi)$ the function $F_{b,\chi}(s)=\chi(s-b)$ has full-field sum zero. Then $\Pi F=F-F(0)v_0$, with $v_0(s)=(q\mathbf1_{s=0}-1)/(q-1)$. Pairing $p_q^*(N-s)$ against $F$ gives (8), times $\chi(-1)$, with $h=N-b\ne0$. The correction is bounded by

$$
\left|\sum_s p_q^*(N-s)v_0(s)\right|
=\frac{q}{q-1}|p_q^*(N)|\ll q/L.
$$

This uses the uniform nonzero-residue prime cap from the [critical-prime analysis, proof of its prime-box bound](weak-s-type-ii-critical-prime-double-centered.md); when $q\mid N$ the expression is zero. So (8) also bounds each reflected unit-centered basis direction in (3).

## 3. Adaptive orthogonal projections and summation

The full-field vectors $F_{b,\chi}$ have norm squared $q-1$. At the same shift different characters are orthogonal. At distinct shifts their scalar product is a unit multiple of $J(\chi,\bar\psi)$ or its conjugate, by substituting $s=b+(c-b)x$ for shifts $b\ne c$. Its modulus is at most $\sqrt q$ by the Gauss product formula (including the principal-product case of modulus one). Since $\|v_0\|_2^2=q/(q-1)$, unit projection subtracts an inner product of magnitude at most $q/(q-1)$ in each Gram entry. Hence the Gram of any selected list of at most $K$ vectors $\Pi F_{b,\chi}$ has diagonal at least $q-1-q/(q-1)$ and off-diagonal magnitude at most $\sqrt q+q/(q-1)$. The stated upper bound on $K$ makes its smallest eigenvalue at least $q/2$ for sufficiently large $N$, by the row-sum bound. This accommodates independently chosen shifts, not just a single common shift.

Consequently, in the unique selected expansion $d_{q,W}=\sum_{(b,\chi)} c_{b,\chi}\Pi F_{b,\chi}$,

$$
\sum_{(b,\chi)}|c_{b,\chi}|^2
 \le (2/q)\|d_{q,W}\|_2^2\le(2/q)\|d_q^*\|_2^2.
$$

Using (8) on each direction and Cauchy–Schwarz on the at most $K$ coefficients bounds the integrand per $q$ in (3) by $O(q^2\sqrt K\,\|d_q^*\|_2)$. Finally apply Cauchy–Schwarz over $q,\beta$, using (6) and

$$
\int_{-1/(10N)}^{1/(10N)}\sum_{q\ {\rm prime},\, .8X\le q\le .9X}q^3\,d\beta
 \ll N/L
$$

from the upper bound for prime counting. This proves (3), including the original outer scalar phase $e(-N\beta)$ if desired.

This estimates a genuine signed projection of the true complementary mass using its ordinary total energy and exact prime-factor arithmetic. It is not an estimate for all residue directions. Even combining all shifted directions by a triangle inequality does not control the dense complementary projection, the full critical shell, or weak S.
