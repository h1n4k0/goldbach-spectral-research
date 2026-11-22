# Unconditional full sum-line comparator at the retuned prime-cofactor endpoints

Fix $0<\rho<1/2$. For even $N$ let $I_0(N)=[\rho N,(1-\rho)N]$, with $I\subseteq I_0(N)$ any hard interval, and retain the exact retuned zero-small double-giant subclass and genuine transforms $A_I(N;\alpha)$ of [R51](r51-source-retuned-endpoint-exact-minor.md). In particular

$$
 \mathcal Q_N=\{q\text{ prime}:\log N<q\le D_N,\ (q,N)=1\},
 \qquad D_N=\left\lfloor\sqrt N\exp\!\left(-20\frac{\log N}{\log\log N}\right)\right\rfloor.
$$

The actual full sum-line count is

$$
 C_N(I)=\sum_{\substack{q,s\in\mathcal Q_N,\ p,v\ {\rm prime}\\
                     qp+sv=N,\ qp\in I,\ sv\in I_0(N),\ (pv,N)=1}}
                     (\log q)(\log s).
$$

It uses the exact original long-divisor product cutoff, which is automatic in this subclass as verified in [R51](r51-source-retuned-endpoint-exact-minor.md). Define $w_q(t)=(\log q)/(q\log(t/q))$ on $I_0(N)$, $\lambda_q=(q-1)/(q-2)$, and the full explicit local-density comparator

$$
 M_N(I)=\mathfrak S(N)
       \sum_{\substack{q,s\in\mathcal Q_N\\q\ne s}}
          \lambda_q\lambda_s\int_I w_q(t)w_s(N-t)\,dt,\qquad
 \mathfrak S(N)=2\prod_{\ell>2}\left(1-\frac1{(\ell-1)^2}\right)
                \prod_{\substack{\ell\mid N\\\ell>2}}\frac{\ell-1}{\ell-2}.
                                                               \tag{1}
$$

This is the same local factor formula as [R31](r31-source-double-giant-one-leg-centering.md), here for the genuinely retuned cofactor set rather than a fixed-power subset.

**Theorem (unconditional).** For any fixed $A,b>0$, put $L=\log X$. Outside at most $O_{\rho,A,b}(X L^{-b})$ even targets $N\in[X,2X]$, one has simultaneously for every hard $I\subseteq I_0(N)$, with either endpoint convention,

$$
 C_N(I)-M_N(I)
   =O_{\rho,A,b}\!\left(\mathfrak S(N)\left(
                    |I|\frac{\log L}{L}+N L^{-A}\right)\right).
                                                               \tag{2}
$$

Here $|I|$ is the real length, so the second error also includes singleton endpoints. This is a full-torus statement for true prime products, independent of the exact signed partial-arc bound in [R51](r51-source-retuned-endpoint-exact-minor.md). No GRH or fixed-power centering theorem is used. In particular it does not estimate the exceptional targets, other rough–rough classes, or the weak-S operator.

## 1. The short cofactor endpoint on the actual sum line

Choose constants

$$
 E=2A+2b+40,\qquad B=2E+5,\qquad P=L^E.
$$

During the proof first keep only the high cofactors $q,s>L^B$ in $\mathcal Q_N$; use a superscript $>$ for that restriction. For any one low cofactor $q\le L^B$ and any other $s\in\mathcal Q_N$, there is no true solution when $q=s$, since then $q\mid N$. For distinct $q,s$, integral solutions of $qp+sv=N$ are parametrized by $p=p_0+s k$, $v=v_0-q k$. The hard interval for $k$ has length exactly $|I|/(qs)$ because $I_0(N)$ is symmetric about $N/2$. On this sum line both partners have size at least $\rho N/D_N\gg_\rho\sqrt N$.

The number of roots of the product of these two affine forms at a prime $\ell$ is one for $\ell\mid qs$ (one form is then a nonzero constant, by $(qs,N)=1$); it is one for $\ell\mid N$ (the two roots coincide); otherwise it is two. Indeed for $\ell\nmid qs$ their determinant is $qp_0+sv_0=N$. In particular $\nu(2)=1$, and no $\nu(\ell)=\ell$. This is exactly the local condition in the elementary two-form sieve of [R41 §1](r41-source-unmasked-separated-cofactor-cells.md#1-full-torus-target-coefficient-unconditional-uniform-two-form-sieve) and does not require that the small cofactors lie in separated dyads. Use its explicit Selberg weight calculation with $Z=N^{1/100}$ and $z=Z^\varepsilon$ for the fixed small absolute $\varepsilon$ in that proof. Every genuine $p,v$ exceeds $z$. The lattice error is $O(Z^6)$ on any hard interval and the inverse sieve denominator is $O(\mathfrak S(N)L^{-2})$: factor out $\prod_{\ell\le z}(1-1/\ell)^2$, use the exact root counts above, and the two extra one-root factors at $q,s$ are bounded uniformly. Thus the true count for each low/high or low/low pair is at most

$$
 O_\rho\!\left(\frac{\mathfrak S(N)|I|}{qs L^2}+N^{.06}\right).
                                                               \tag{3}
$$

No short-interval prime distribution is assumed. The lattice upper bound is valid even when the real interval is very short. For the multiplicative scale of this application, $N/(qs)\gg_{\rho,B}N^{.49}$ whenever one cofactor is low; the proof keeps the additive error in (3), not a false relative estimate when $|I|$ is small.

Sum (3) with the actual positive weights, taking one low leg and then the other. The overlap where both are low is counted only in an upper bound for their union. Chebyshev and partial summation give
$\sum_{q\le L^B}\log q/q\ll_B\log L$, $\sum_{s\le D_N}\log s/s\ll L$.
There are at most $2L^B D_N$ pairs; the additive errors with both markers are $O_B(N^{.56}L^{B+2})=O_B(N^{.6})$. Therefore

$$
 0\le C_N(I)-C_N^>(I)
      \ll_{\rho,B}\mathfrak S(N)|I|\frac{\log L}{L}+N^{.6}.
                                                               \tag{4}
$$

For the analytic comparator, $\lambda_q$ is uniformly bounded and $w_q(t)\ll_\rho(\log q)/(qL)$ because $t/q$ is on the giant scale. The same reciprocal estimates prove
$0\le M_N(I)-M_N^>(I)\ll_{\rho,B}\mathfrak S(N)|I|\log L/L$. These deletions apply on the positive full sum-line count and its model, not to the signed integral on any other set of arcs.

## 2. Classical major arcs and restoration of the actual comparator

Use the fixed classical major arcs $\mathfrak G$ about each reduced $a/r$, $r\le P$, with common half-width $P/X$. For large $X$ they are disjoint: distinct centers have distance at least $P^{-2}$, and $2P/X<P^{-2}$. This family is used only for the full-torus proof; no identification with the [R51](r51-source-retuned-endpoint-exact-minor.md) arcs is needed. Write $\mathfrak g=\mathbb T\setminus\mathfrak G$. For each $N$ and $J\subseteq I_0(N)$ define the real density

$$
        a_{N,J}(t)=\mathbf1_J(t)\sum_{\substack{q\in\mathcal Q_N\\q>L^B}}w_q(t).
$$

With coefficients extended by zero off $J$, its supremum and total variation are $O_\rho(1)$ uniformly in every hard $J$. This follows from the two cutoff jumps, monotonicity of each $1/\log(t/q)$ on the central interval, and $\sum_q\log q/q\ll L$.

For $|\beta|\le P/X$, uniformly in all exact hard $J$,

$$
 A^>_J(N;a/r+\beta)=
       \frac{\mu(r)}{\varphi(r)}
            \widehat a_{N,J}(\beta)+O_{\rho,E,B,F}(X L^{-F}),
 \qquad
 \widehat a_{N,J}(\beta)=\int_{\mathbb R}a_{N,J}(t)e(\beta t)\,dt,
                                                               \tag{5}
$$

for any fixed $F>0$. To verify this, for fixed $q>L^B>P$ the cofactor and each partner prime are units modulo $r$. Apply [Siegel–Walfisz](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=129) on its reduced prime residue classes at scale $Y=N/q\gg_\rho\sqrt X$, so $\log Y\asymp L$ and $r\le P$ is a fixed log power in that theorem. The unweighted prime version follows from its von Mangoldt version by deleting the proper powers and partial summation. All endpoints in this step may be real: take the actual prefix difference and handle a singleton by $O(1)$ per residue, absorbed by the uniform $Y L^{-F'}$ error. Modulating by $e(\beta q p)$ adds a total-variation cost $O(P)$; summing over numerator residue classes adds at most $P$. Summing the main term over those classes gives $c_r(aq)=\mu(r)$ since $(aq,r)=1$. Changing variable $t=qp$ in the density $\int dp/\log p$ produces $w_q(t)$. Multiplying the uniform per-$q$ errors by $\log q$ and summing uses $\sum_q\log q/q\ll L$, so choosing the prime-theorem log accuracy $F'$ sufficiently large gives (5). The actual exclusion of a partner dividing $N$ costs at most $O(D_N L)$ uniformly, since every partner exceeds $\sqrt{2X}$ and at most one can divide $N$; this is within $X L^{-F}$ for fixed $F$. The cofactor unit restriction is already in the selection. Constants from Siegel–Walfisz may be ineffective.

Both the genuine factors and their approximants in (5) are bounded by $O_\rho(XL)$ by the unique factorization at these disjoint small and large scales, or by the density bound. The total arc length is $O(P^3/X)$, so multiplying (5) and integrating on $\mathfrak G$ costs $O_{\rho,A,b}(XL^{-A})$ after fixing sufficiently large $F$. The numerator sum gives the truncated Ramanujan series

$$
 \Sigma_P(N)=\sum_{r\le P}\frac{\mu(r)^2 c_r(N)}{\varphi(r)^2}
$$

multiplying the real integral of $\widehat a_{N,I}(\beta)\widehat a_{N,I_0(N)}(\beta)e(-N\beta)$ on $[-P/X,P/X]$. For clarity the absolute Ramanujan tail averaged in the dyad is $O(P^{-1/2})$. Indeed $\sum_{N\le2X}|c_r(N)|\le2X\tau(r)$ by the divisor formula, and $\sum_{r\ge1}r^{1/2}\mu(r)^2\tau(r)/\varphi(r)^2<\infty$ by its Euler product. The complete series is $\mathfrak S(N)$ by its squarefree Euler factors: the factor is $1+1/(\ell-1)$ for $\ell\mid N$ and $1-1/(\ell-1)^2$ otherwise, including the even factor $2$. This product is absolutely convergent for each fixed $N$. Thus except for $O(X L^{A+1}P^{-1/2})=O_{A,b}(X L^{-b})$ targets,

$$
  |\Sigma_P(N)-\mathfrak S(N)|\le L^{-A-1},\qquad
  |\Sigma_P(N)|\ll\mathfrak S(N).
                                                               \tag{6}
$$

This exceptional set is independent of $I$.

The bounded variations give $|\widehat a_{N,J}(\beta)|\ll_\rho|\beta|^{-1}$ for $\beta\ne0$, including the two interval edges. Hence the real integral tail when extending to the whole real line is $O_\rho(X/P)$ before multiplying by $\Sigma_P(N)$. Its full value is
$\int_I(\sum_{q>L^B} w_q(t))(\sum_{s>L^B}w_s(N-t))\,dt$
by Fourier inversion: convolution of these bounded compactly supported densities is continuous, and $N-I\subseteq I_0(N)$. Both cofactor sums here retain $\mathcal Q_N$. Its size is $O_\rho(|I|)$; this and (6) account for replacing the truncated singular factor. The result differs from $M_N^>(I)$ by $O_\rho(\mathfrak S(N)|I| L^{-B})$. Indeed $\lambda_q=1+O(L^{-B})$ for the high primes, and the model diagonal has size $O_\rho(|I|\sum_{q>L^B}q^{-2})=O_\rho(|I| L^{-B})$, since $(\log q)/\log(t/q)$ is bounded. Thus on these same good moduli the major contribution to $C_N^>(I)$ is $M_N^>(I)+O_{\rho,A,b}(\mathfrak S(N)N L^{-A})$ uniformly in $I$.

## 3. Signed control on the classical minor arcs, with four moving integer axes

This step uses the genuine prime polynomials, not their major model. Work on the fixed dyad-wide physical envelope $[\rho X/2,2X]$ and cofactor envelope $(L^B,U_*]$, $U_*=\sqrt X e^{-19L/\log L}$ as in [R51](r51-source-retuned-endpoint-exact-minor.md). Initially omit the target unit masks. If $\alpha\in\mathfrak g$, Dirichlet approximation with integer parameter $\lceil X/P\rceil$ gives a reduced $a/r$ with

$$
 P<r\le\lceil X/P\rceil,\qquad |\alpha-a/r|\le r^{-2};
$$

an approximant with $r\le P$ would be inside $\mathfrak G$. Thus $L^E<r\ll X L^{-E}$. For aligned dyadic cofactor and physical cells $E_0,J$, let $A_{J,E_0}$ be the genuine transform over those integer cells in the fixed envelopes. We prove the joint energy bound at every pair of levels:

$$
  \sup_{\alpha\in\mathfrak g}\sum_{E_0,J}|A_{J,E_0}(\alpha)|^2
           \ll_{\rho,A,b} X^2 L^{6-E}.
                                                               \tag{7}
$$

In one ordinary cofactor dyad $U\le q<2U$ put $V=X/U$, so $V\ll X L^{-B}$ and $U\ll\sqrt X$. Cauchy in the larger partner $p$, expansion and summation over the disjoint physical cells give exactly the [R50](r50-source-full-admissible-exact-dirichlet-mean.md) floor expression for same-cell membership, $1-hp/H+\psi((q+h)p/H)-\psi(qp/H)$ on the interval where $hp<H$, with $h=q'-q>0$, $p\asymp_\rho V$ and $H$ the physical dyadic cell length. The diagonal costs $O(UV^2L^2)$ with markers, and each $h$ has at most $O(U)$ eligible $q$ over all cofactor cells. The endpoint-inclusive discrete Fejér estimate from [R50](r50-source-full-admissible-exact-dirichlet-mean.md) is unchanged.

Here $r$ may be smaller than $2U$, so partition $1\le h\le U$ into $O(G)$ consecutive blocks of length at most $r/2$, where $G=1+U/r$. Within each block the phases $\alpha h$ are $1/(2r)$-separated. For any block the sum of truncated reciprocal distances from zero is $O_\rho(V+rL)$: the closest phase costs at most $O_\rho(V)$ and the remainder is a harmonic sum. Thus the affine part by Abel costs $O_\rho(UV L^2 G(V+rL))$.

Set $Y_0=X L^{-E}$. If $H<2Y_0$, the total off-diagonal by raw bounds is $O_\rho(UV H L^2)$: there are at most $O_\rho(H/V)$ positive $h$, $O(U)$ possible $q$ and $O_\rho(V)$ possible $p$ per pair, with the outer Cauchy factor $O_\rho(V)$ and two logarithmic marks. This is $O_\rho(X^2 L^{2-E})$. Otherwise put $K=\lfloor H/Y_0\rfloor\ge1$. The discrete approximation error costs $O_\rho(X H L^4/K)=O_\rho(X^2 L^{4-E})$: for one $h$ product multiplicity is $O(L)$ by the divisor-prime bound, one sums $O(X/H)$ full residue periods and the endpoint-inclusive [R50](r50-source-full-admissible-exact-dirichlet-mean.md) error, then at most $O(H/V)$ choices of $h$ and the outer $O(VL^2)$. No endpoint jump is thrown away.

For a frequency $1\le k\le K$, the two oscillatory phases are $\alpha h\pm kq/H$ and $\alpha h\pm k(q+h)/H$. The latter is treated using $q+h$ as variable. Since $kU/H\le U/Y_0=o(1)$, exactly as for [R50](r50-source-full-admissible-exact-dirichlet-mean.md) the near set $\|\alpha h\|\le4kU/H$ contains at most $O(G(1+rkU/H))$ possible $h$. For each near $h$, the shifted phases as $q$ varies have step $k/H$ and span $<1/4$, so cost $O_\rho(V+(H/k)L)$. Outside the near set the shifted distances are at least half their original distances; summing truncated reciprocals per block costs at most $O_\rho(V+rL)$, and $O(U)$ choices of $q$ multiply this. With coefficients $O(1/k)$ the resulting total is at most

$$
 O_\rho\!\left(VL^2
      \left\{G(VL+HL+rUVK/H+rU L^2)
                      + U G(V+rL)L \right\}\right).
                                                               \tag{8}
$$

In (8), $G V^2\ll V^2+X V/r$, $G V H\ll V H+X H/r$ and
$G r U V^2 K/H\ll (r+U)V L^E$. The last expression is
$O(X^2L^{-B}+XL^E)$ since $r\ll XL^{-E}$ and $UV=X$. Also
$G r U V=X(r+U)$ and $G(V+rL)\ll V+X/r+(r+U)L$.
With $B=2E+5$, $r>L^E$, $H=O(X)$ and $U=O(\sqrt X)$, all terms in (8), plus the affine and diagonal contributions, are $O_{\rho,A,b}(X^2 L^{4-E})$ for large $X$. Aggregating the $O(L)$ ordinary dyads by Cauchy costs at most $L^2$, proving (7).

The two cofactor intervals have at most $O(L)$ holes from primes dividing the target $N$, so each requires $O(L^2)$ aligned cells. The two hard physical windows each require $O(L)$ aligned cells. At most $O(L^6)$ fixed-cell terms appear in the product expansion on the fixed $\mathfrak g$, and the number of level choices is $O(L^4)$. As in [R50](r50-source-full-admissible-exact-dirichlet-mean.md), Cauchy followed by Bessel gives a maximal squared sum over all integer Fourier targets bounded by $O(L^{10})$ times the worst-level integral of the product of the two joint cell energies. Apply (7) to one and the $O(X L^2)$ integrated energy of the other by unique small/large factorization and Parseval. The squared sum is $O_{\rho,A,b}(X^3 L^{18-E})$. The omitted giant dividing $N$ changes each coefficient by $O_\rho(X^{3/4}L^2)$ using Cauchy and its squared norm $O(U_* L^2)$, so adds only $O(X^{5/2}L^4)$ to that squared sum. All physical endpoint cuts and cofactor units were exact in the expansion. Markov at $X L^{-A}$ now excludes at most $O_{\rho,A,b}(X L^{-b})$ even targets uniformly for every hard $I$.

Together with §2 this proves $C_N^>(I)=M_N^>(I)+O_{\rho,A,b}(\mathfrak S(N)N L^{-A})$ off the union of the two exceptional sets. The full-torus coefficient is exactly the true sum line by integer orthogonality, with no contribution from a shared constituent, since all four primes are units and the small and giant ranges are disjoint. Finally (4) and its model counterpart prove (2). The result does not bound the exceptional set pointwise or estimate any other arithmetic sector.

## 4. Size of the deterministic comparator

For interpretation, uniformly on the central range,

$$
   \sum_{q\in\mathcal Q_N} w_q(t)
      =\log\!\left(\frac{\log t-\log\log N}{\log t-\log D_N}\right)
                   +O_\rho(1/\log N)
      =\log 2+O_\rho(1/\log\log N).
$$

For the first estimate, partial summation with $\vartheta(x)=x+O(x/(\log x)^2)$ replaces the prime sum between $\log N$ and $D_N$ by $\int_{\log N}^{D_N}dx/(x\log(t/x))$: the weight has derivative $O_\rho(1/(x^2\log N))$, and the two endpoint errors and integrated PNT error are $O_\rho(1/\log N)$. Excluding $q\mid N$ costs at most $O_\rho(1/\log N)$, since $\sum_{q\mid N,\ q>\log N}(\log q)/q\le1$. The second estimate follows from the actual formula for $D_N$. In (1), the factors $\lambda_q$ change this bounded sum by $O_\rho(1/\log N)$, and deleting the diagonal costs $O_\rho(|I|/\log N)$ before the singular-series factor. Hence

$$
 M_N(I)=\mathfrak S(N)|I|
        \left((\log 2)^2+O_\rho(1/\log\log N)\right).
$$

For example, on all the good moduli of (2), any fixed polylogarithmic-length central intervals $|I|\ge N L^{-J}$ have the leading constant $(\log 2)^2$ by taking $A>J$. This concerns weighted products of genuine semiprimes in the specified raw sector, not representations of $N$ by two primes.
