# Sparse Jacobi-product modes of the true critical prime covariance

Keep even $N$, $X=\sqrt N$, $L=\log N$, the fixed proportional boxes $I_u=[.740X,.745X]$, $I_v=[.715X,.720X]$, and the genuine complementary polynomial $D$ from the [double-centered critical-shell identity](weak-s-type-ii-critical-prime-double-centered.md). The shell is $q$ prime in $[.8X,.9X]$ and $|\beta|\le1/(10N)$. Both inputs keep the original unit masks modulo $N$. In $D$ retain all $d\ge X$ in its arbitrary hard $I_d$, strict $k>t\ge N^{.49999}$, $N-y\le dk<N/2$, $(dk,N)=1$, and weight $\mu(d)\mu^2(k)\mathbf 1_{(d,k)=1}$. Let $p_q^*(r),d_q^*(r)$ be the true unit-residue masses of $P,D$ with the unit means subtracted, extended by zero at $r=0$. In particular both have zero total sum, and the additive nonprincipal covariance for a single $q,\beta$ is

$$
C(q,\beta)=q\sum_{r\bmod q}p_q^*(r)d_q^*(N-r).
\tag{1}
$$

The masses include the phases $e(\beta uv)$ and $e(\beta dk)$; the additional outer phase $e(-N\beta)$ remains outside (1).

Unconditionally, the multiplicative principal-product class of (1) for $q\nmid N$ contributes $O(N/L)$ after summing over these primes and integrating over the shell, even with the previous arbitrary $|E(u,v)|\le1$, hard prime subintervals and product window $N/2<uv\le y\le9N/16$.

A separate GRH result applies to the actual unselected prime box $E=1$, with arbitrary individual hard subintervals of $I_u,I_v$ but with $y=9N/16$, so the prime-box product gate is automatic. Under global Dirichlet GRH, including ordinary RH, for each $q\nmid N$ select any at most $K$ nonprincipal product characters $\omega$ of $\mathbb F_q^\times$, measurably and independently for each $q$ and $\beta$. The shell integral of their joint contribution, even with the absolute value on the sum of selected product classes for each $q,\beta$, is

$$
\ll_\epsilon K N^{3/4+\epsilon}/L.
\tag{2}
$$

This retains **all** nonprincipal character pairs within each selected product class, not just a sparse marginal set of pairs. In the same GRH setting the full (1) on the prime denominators $q\mid N$ costs $O_\epsilon(N^{1/2+\epsilon})$ after shell integration. Thus $K\le N^{1/4-\delta}$, for fixed $0<\delta\le1/4$, permits signed elimination of all these selected classes with a power saving. The dense product-character complement is not estimated.

## Exact product-class formula

Fix $q,\beta$. For characters $\chi,\psi$ extended by zero at zero, use

$$
\widehat p(\chi)=\sum_r p_q^*(r)\chi(r),\qquad
\widehat d(\psi)=\sum_r d_q^*(r)\psi(r).
$$

The principal hats are zero. At nonprincipal characters, taking the hat of the original unit mass gives exactly the same value, since its subtracted constant has hat zero. Multiplicative inversion in (1), with $r=Nx$ on $q\nmid N$, gives

$$
C(q,\beta)=\sum_\omega C_\omega(q,\beta),\qquad
C_\omega=\frac{q\,\overline{\omega}(N)}{(q-1)^2}
  \sum_{\substack{\chi,\psi\ne1\\ \chi\psi=\omega}}
  \widehat p(\chi)\widehat d(\psi)J(\overline\chi,\overline\psi),
\quad
J(\xi,\eta)=\sum_{x\bmod q}\xi(x)\eta(1-x).
\tag{3}
$$

For $\xi,\eta,\xi\eta\ne1$, $|J(\xi,\eta)|=\sqrt q$: multiply the two Gauss sums and group by the sum of their input residues, using zero contribution at sum zero and the Gauss moduli $\sqrt q$. For $\xi\ne1$, the bijection $x/(1-x)$ from residues other than $0,1$ onto the units other than $-1$ gives $J(\xi,\overline\xi)=-\xi(-1)$. In particular,

$$
C_{1}(q,\beta)=-\frac{q}{q-1}\sum_{r\ne0}p_q^*(r)d_q^*(-r).
\tag{4}
$$

The residue argument $-r$ here is unrelated to the target $N$; the original phases in the masses have not changed.

For a nonzero residue $r$, the two-prime Selberg bound in the [double-centered analysis](weak-s-type-ii-critical-prime-double-centered.md) is uniform in this target $r$, by the uniform Kloosterman bound for the hyperbola with nonzero right side. Thus the number with $uv\equiv r$ is $O(X/L^2)$ and $|p_q^*(r)|\ll X/L$ after adding the weight $\log v$ and subtracting its mean. For the other side, the sum of the absolute values of the original unit masses is bounded by the number of admissible pairs, at most

$$
\sum_{X\le d<N^{.50001}/2}\frac{N}{2d}\ll NL.
$$

Centering at most doubles this bound. Therefore (4) is $O(X^3)$ for each $q,\beta$. Chebyshev gives $O(X/L)$ prime denominators, and the length $1/(5N)$ of the $\beta$ interval proves the unconditional $O(N/L)$ assertion.

## GRH estimates and the exceptional denominator

Uniformly for nonprincipal $\chi\bmod q$, [Montgomery–Vaughan, Theorem 13.7](https://ndl.ethernet.edu.et/bitstream/123456789/23715/1/Hugh%20L.%20Montgomery.pdf) gives both unweighted and $\log$-weighted prime sums on hard subintervals with error $O(\sqrt X L^2)$, including when the endpoints are below $q$. The primes dividing $N$ remove total weight $O(L^2)$ or less. For $E=1$ and $y=9N/16$, the two hard intervals are independent. Expand

$$
e(\beta uv)=\sum_{j\ge0}\frac{(2\pi i\beta N)^j}{j!}(u/X)^j(v/X)^j.
$$

The coefficient absolute sum is bounded uniformly and each power is bounded and monotone on its interval, with variation at most one. Abel summation on each prime side therefore gives

$$
|\widehat p(\chi)|\ll X L^4.
\tag{5}
$$

We do not use this bound for arbitrary nonseparable selectors $E$ or an active upper gate $uv\le y$.

For every $\psi\ne1\bmod q$, the actual nonprincipal complementary hat satisfies

$$
|\widehat d(\psi)|\ll_\epsilon X N^\epsilon.
\tag{6}
$$

Here are the precise ingredients from the [GRH hard-window Mellin bound, §§1–2](weak-s-type-ii-grh-mellin-critical-wings.md). The hat contains $\psi(dk)$, hence vanishes automatically on $q\mid dk$, and has no additional unit-mean term. On hard dyadic rectangles $d\asymp D_0$, $k\asymp K_0$ with $D_0 K_0\asymp N$, expand $\mathbf1_{(d,k)=1}=\sum_{h\mid(d,k)}\mu(h)$ and put $d=ha,k=hb$. The resulting coefficient is $\mu(a)\mu^2(b)$ times the constant $\mu^2(h)\psi(h)^2$ and the characters of $a,b$, with both still coprime to $hN$ and each twist zero on multiples of $q$. This is exact on the nonzero squarefree supports; nonunit $h$ gives zero. The separation of the hard integer product gate $N-y\le h^2ab<N/2$ and its phase $e(\beta h^2ab)$ has logarithmic Fourier norm $O(L)$ for $N|\beta|\le1/10$, at polynomial Mellin height with negligible uniform remainder. For each separated term the shifted hard Perron bounds are $O_\epsilon(\sqrt{D_0/h}N^\epsilon)$ for $\mu(a)\psi(a)$ and $O_\epsilon(\sqrt{K_0/h}N^\epsilon)$ for $\mu^2(b)\psi(b)$, preserving the additional coprimality masks. The bounds use respectively the reciprocal of $L(s,\psi)$ and the ratio $L(s,\psi)/L(2s,\psi^2)$ with finite unit factors. A principal $\psi^2$ in the denominator is allowed; the numerator in the squarefree sum is nonprincipal. Summing $1/h$ and the hard dyads and absorbing logarithms proves (6).

For fixed $\omega\ne1$, the number of pairs in (3) is at most $q-1$. By (5), (6) and $|J|=\sqrt q$,

$$
|C_\omega(q,\beta)|\ll_\epsilon N^{5/4+\epsilon}.
$$

The triangle inequality over any $K$ selected product classes, followed by Chebyshev's bound on the primes and the shell length, proves (2). These upper bounds also hold with the outer unit phase $e(-N\beta)$ included.

When $q\mid N$, do not use the substitution $r=Nx$ or (3). Equation (1) becomes $q\sum_r p_q^*(r)d_q^*(-r)$, and multiplicative orthogonality gives

$$
C(q,\beta)=\frac{q}{q-1}\sum_{\chi\ne1}
 \widehat p(\chi)\widehat d(\overline\chi)\chi(-1).
$$

By (5)–(6) this is $O_\epsilon(N^{3/2+\epsilon})$ per such prime. There are at most two such denominators for large $N$ since the product of three primes $\ge .8X$ exceeds $N$. Integrating proves the stated $O_\epsilon(N^{1/2+\epsilon})$ bound without imposing $q\nmid N$ on the full shell.

There are about $X$ product classes for each $q$. Applying (2) to all of them would only give an upper bound of order $N^{5/4+\epsilon}$ before the logarithm; this is not a lower bound or an impossibility theorem. A gain for the dense complement must control joint cancellation among the actual Jacobi-weighted products in (3), or exploit different arithmetic in the same centered covariance. No estimate of that dense contribution, the whole shell, or weak S follows here.
