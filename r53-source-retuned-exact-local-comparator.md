# Full retuned prime-cofactor comparator with exact local factors

Take the original retuned thresholds, exact true unit masks, genuine full sum-line count $C_N(I)$ and explicit comparator $M_N(I)$ from [R52](r52-source-retuned-full-count-comparator.md). Thus $I\subseteq I_0(N)=[\rho N,(1-\rho)N]$ is any hard interval, $0<\rho<1/2$ is fixed, and

$$
 \mathcal Q_N=\{q\text{ prime}:\log N<q\le D_N,\ (q,N)=1\},\qquad
 D_N=\left\lfloor\sqrt N\exp\!\left(-20\frac{\log N}{\log\log N}\right)\right\rfloor .
$$

For $t\in I_0(N)$ put $w_q(t)=(\log q)/(q\log(t/q))$, and let $\lambda_q=(q-1)/(q-2)$. The comparator is

$$
 M_N(I)=\mathfrak S(N)
       \sum_{\substack{q,s\in\mathcal Q_N\\q\ne s}}
            \lambda_q\lambda_s\int_I w_q(t)w_s(N-t)\,dt .
$$

Here $\mathfrak S(N)$ is the ordinary even binary singular series. The marked actual full count corresponds to $qp+sv=N$ with genuine primes $p,v$, exact $(qp\,sv,N)=1$, and $qp\in I$, $sv\in I_0(N)$. On this sum line the retuned long-divisor cutoff is automatic and the marker is $(\log q)(\log s)$, as in [R51](r51-source-retuned-endpoint-exact-minor.md).

**Theorem (unconditional).** For any fixed $A,b>0$, with $L=\log X$, outside at most $O_{\rho,A,b}(X L^{-b})$ even targets $N\in[X,2X]$, one has, simultaneously for every original hard $I$,

$$
       |C_N(I)-M_N(I)|\ll_{\rho,A,b}\mathfrak S(N)N L^{-A}.
                                                               \tag{1}
$$

This removes the low-endpoint deletion error of [R52](r52-source-retuned-full-count-comparator.md). It does not posit a local estimate at an exceptional target, transfer to different raw classes, or imply Hypothesis S. It concerns the full sum line, not the exact square-root Dirichlet complement of [R51](r51-source-retuned-endpoint-exact-minor.md). The same actual full count is automatically four-distinct, because a shared constituent prime would divide $N$ and be a unit modulo $N$.

## 1. Classical minor arcs: retain the actual low cofactors

Put

$$
 K_0=2A+2b+50,\qquad E=6K_0,\qquad P=L^E.
$$

Use the fixed classical reduced major arcs $\mathfrak G$ with denominators $r\le P$ and common half-width $P/X$. These are disjoint for large $X$, since $2P/X<P^{-2}$. Put $\mathfrak g=\mathbb T\setminus\mathfrak G$, and $Q'=\lceil X/P\rceil$. Use the fixed physical envelope $[\rho X/2,2X]$ and fixed cofactor envelope $[2,U_*]$, where $U_*=\sqrt X e^{-19L/\log L}$ contains all $D_N$ on the dyad, as in [R51](r51-source-retuned-endpoint-exact-minor.md). The primes $p$ on this envelope exceed $\sqrt{2X}$ and all cofactors for sufficiently large $X$. They have unique cofactor/partner factorization at every physical index. Initially ignore the target-dependent unit holes. At fixed aligned integer levels, let $J$ be a physical cell and $F$ a cofactor cell, and $A_{J,F}$ the genuine prime-marked polynomial on those cells.

For a fixed low cofactor $q\le L^{K_0}$ and physical cell $J$, write

$$
 A_{J,q}(\alpha)=(\log q)\sum_{\substack{p\ {\rm prime}\\qp\in J}}e(qp\alpha).
$$

On $\mathfrak g$ approximate $q\alpha$ by a reduced $a/d$, $d\le Q'$, with error $\le1/(dQ')\le d^{-2}$. Necessarily $qd>P$: otherwise reducing $a/(qd)$ gives a denominator at most $P$ for $\alpha$ and a lift of error at most $1/(qdQ')\le P/X$, contrary to membership in $\mathfrak g$. This also handles cancellation between $a$ and $q$. Hence $d>L^{E-K_0}$ and $d\ll X L^{-E}$. Apply [Vaughan's estimate, Montgomery–Vaughan II, Theorem 17.1](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=77) to the two prefixes of the hard interval for $p$, of scale $V=X/q$. Deleting the proper powers and partially summing $1/\log p$ on that scale convert the von Mangoldt weight to true unweighted partners. The resulting bound including $\log q$ is

$$
 \sup_{\alpha\in\mathfrak g,\ J}|A_{J,q}(\alpha)|
   \ll_{\rho,K_0} X L^{-(E-K_0)/2+5}+X^{4/5}L^5.
                                                               \tag{2}
$$

Indeed the three Vaughan terms are $Vd^{-1/2}$, $V^{4/5}$ and $\sqrt{Vd}$ with fixed logarithms; use $V\ll_\rho X$ but the two opposite bounds on $d$. Ordinary partial summation does not require a minimum length for $J$.

At fixed physical level, $\sum_J |A_{J,q}|\ll_\rho(X/q)L$ by disjoint supports. Combine (2) with this inequality to bound the sum of the squares for fixed $q$, and use Cauchy over the at most $L^{K_0}$ low cofactors followed by summation over the disjoint cofactor cells. Since $\sum_{q\le L^{K_0}}1/q\ll_{K_0} L$, the joint energy of the actual low part is bounded by

$$
  O_{\rho,K_0}\!\left(
      X^2 L^{K_0+7-(E-K_0)/2}
           +X^{9/5}L^{K_0+7}\right)
   \ll_{\rho,K_0} X^2 L^{6-K_0}.                               \tag{3}
$$

For the high cofactors $q>L^{K_0}$ use the floor-cell and block argument of [R52](r52-source-retuned-full-count-comparator.md) §3 with the following distinct choices. On $\mathfrak g$ an undilated reduced approximant has $P<r\le Q'$ and error $\le r^{-2}$. In an ordinary cofactor dyad $U\le q<2U$, set $V=X/U$ and $G=1+U/r$. As in [R52](r52-source-retuned-full-count-comparator.md) partition differences $h=q'-q$ into $O(G)$ consecutive intervals of length at most $r/2$. Within each interval the phases $\alpha h$ are $1/(2r)$-separated. Use the Fejér scale $Y_0=X L^{-K_0}$, independent of the major radius. For $H<2Y_0$ the raw off-diagonal is $O(XH L^2)$; for $H\ge2Y_0$ the endpoint-inclusive Fejér error is $O(XY_0 L^4)$ with degree $K=\lfloor H/Y_0\rfloor$. Both statements use the exact same-cell test and at most $O(L)$ cofactor prime divisors per integer product, as in [R52](r52-source-retuned-full-count-comparator.md). For the remaining modes $kU/H\le U/Y_0=o(1)$ ensures the near/far calculation still applies. The oscillatory upper bound there is

$$
 O_\rho\!\left(VL^2
      \left\{G(VL+HL+rUVK/H+rU L^2)+UG(V+rL)L\right\}\right).
                                                               \tag{4}
$$

In (4), $G V^2=V^2+XV/r$, $G V H=VH+XH/r$, and

$$
 G r U V^2 K/H\le (r+U)V L^{K_0}
        \ll X^2L^{-E}+X L^{K_0}.
$$

The last inequality uses $r\ll X L^{-E}$, $UV=X$, and $V\ll X L^{-K_0}$. Also $G r U V=X(r+U)$ and $G(V+rL)\ll V+X/r+(r+U)L$. As $r>L^E$, $U\ll\sqrt X$, $H=O(X)$ and $E=6K_0$, every term costs $O_\rho(X^2 L^{4-K_0})$ per dyad, including the diagonal $O(UV^2L^2)$ and the affine $O(UV L^2G(V+rL))$. Taking Cauchy over ordinary dyads costs at most $L^2$. Combining with (3) proves

$$
 \sup_{\alpha\in\mathfrak g}\sum_{F,J}|A_{J,F}(\alpha)|^2
     \ll_{\rho,A,b} X^2 L^{6-K_0}
                                                               \tag{5}
$$

at fixed cofactor and physical levels, with both genuine low and high parts included.

Now restore the four moving integer axes exactly as in [R52](r52-source-retuned-full-count-comparator.md). Each cofactor interval $(\log N,D_N]$ minus $O(L)$ unit holes is a union of $O(L^2)$ aligned cells; the two physical intervals each use $O(L)$ cells. At most $O(L^6)$ fixed-cell terms occur in the expansion. Cauchy and the $O(L^4)$ level choices cost $O(L^{10})$ in the maximal squared sum. For fixed levels Bessel over integer targets gives the integral of the product of the two joint cell energies over $\mathfrak g$; use (5) for one and the $O(X L^2)$ integrated Parseval bound for the other by uniqueness. The total squared sum is $O(X^3 L^{18-K_0})$. An excluded partner prime dividing $N$ is unique if present, and its removed transform has squared energy $O(U_*L^2)$. Cauchy against the other leg yields at most $O_\rho(X^{3/4}L^2)$ per target, with squared sum $O(X^{5/2}L^4)$; the exact unit conditions are now restored on both sides. Thus the signed $\mathfrak g$ coefficient is $O_{\rho,A,b}(X L^{-A})$ uniformly over the simultaneous hard intervals outside $O_{\rho,A,b}(X L^{-b})$ targets by Markov. This part does not assume the small cofactors are units modulo the major denominator.

## 2. Classical major arcs: the effective denominator for each actual cofactor

For each reduced $a/r$ of denominator $r\le P$ let $r_q=r/(r,q)$. At the major arc $\alpha=a/r+\beta$, the reduced additive phase for $p$ has denominator exactly $r_q$, with numerator $a q/(r,q)$ coprime to $r_q$. Consequently the genuine prime cofactor polynomial there equals

$$
 A_J(N;a/r+\beta)=
       \sum_{q\in\mathcal Q_N}\frac{\mu(r_q)}{\varphi(r_q)}
                 W_{q,J}(\beta)+O_{\rho,A,b,F_1}(X L^{-F_1}),
 \qquad W_{q,J}(\beta)=\int_J w_q(t)e(\beta t)\,dt
                                                               \tag{6}
$$

for any fixed $F_1>0$, uniformly over hard $J$ and $|\beta|\le P/X$. For fixed $q$, all partner primes exceed $r$ and their interval is at polynomial scale $Y=N/q$. Apply [Siegel–Walfisz, Theorem 12.1](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=129) to each reduced residue modulo $r_q$ and use two real prefixes, unweighting by partial summation. The fixed number of possible endpoints costs $O(1)$ per class if necessary. The principal reduced-residue additive average is $\mu(r_q)/\varphi(r_q)$ independently of the numerator. The phase $e(\beta qp)$ over physical size $X$ adds $O(P)$ variation and summing residue classes adds at most $P$. Change variable $t=qp$ in the unweighted real density, giving the stated $w_q$. Uniform logarithmic accuracy follows by choosing sufficient accuracy in Siegel–Walfisz, multiplying each scale $X/q$ error by $\log q$ and summing $\sum_q\log q/q\ll L$. The unique excluded partner dividing $N$, if present, costs $O(D_N L)$, absorbed in (6). Cofactors dividing $N$ are not included in (6). The constants may be ineffective.

The actual transforms and the major approximants are $O_\rho(XL)$, and the total major length is $O(P^3/X)$. Thus inserting (6) into the signed product at frequency $N$ incurs $O_{\rho,A,b}(X L^{-A})$ on choosing $F_1$ sufficiently large. Summing the reduced numerators gives for each pair the signed coefficient

$$
   \Gamma_{q,s}(r;N)
      =c_r(N)\frac{\mu(r_q)\mu(r_s)}
                      {\varphi(r_q)\varphi(r_s)}
                                                               \tag{7}
$$

multiplying the real integral of $W_{q,I}W_{s,I_0(N)}e(-N\beta)$ over $[-P/X,P/X]$.

## 3. Pairwise signed Euler factors and both tails

Only squarefree $r$ can have a nonzero (7) on the true unit masks. If $\ell^2\mid r$ and $\ell\notin\{q,s\}$ it kills both Möbius factors; if $\ell=q$ or $s$ then $c_{\ell^j}(N)=0$ for $j\ge2$ because $\ell\nmid N$, and multiplicativity kills $c_r(N)$. This also handles the equal-cofactor case.

For squarefree $r$ the signed sum in (7) has an absolutely convergent Euler product. At $\ell\notin\{q,s\}$ the local factor is the ordinary binary one $1+c_\ell(N)/(\ell-1)^2$. At $\ell=q$ with $q\ne s$, exactly one leg loses its denominator factor and the other contributes $\mu(q)=-1$. Since $c_q(N)=-1$, the local factor is $1+1/(q-1)$, with ratio to the ordinary one equal to $\lambda_q$; likewise at $s$. At $\ell=q=s$, both effective denominators lose $q$, so the local factor is $1+c_q(N)=0$. Thus

$$
    \sum_{r\ge1}\Gamma_{q,s}(r;N)
       =
       \begin{cases}
        \mathfrak S(N)\lambda_q\lambda_s,& q\ne s,\\
        0,&q=s.
       \end{cases}                                             \tag{8}
$$

The absolute series is $O(\mathfrak S(N))$ uniformly even at equality: the ordinary absolute product has only constant multiples relative to $\mathfrak S(N)$ by comparison at primes not dividing even $N$, and the special absolute factors are bounded by two each. This gives absolute convergence for fixed $N$ as well as the uniform statement.

Write $g_q=(\log q)/(qL)$ for the fixed dyad weight. The sup norm and bounded variation of $w_q\mathbf1_J$ are $O_\rho(g_q)$, so $|W_{q,J}(\beta)|\ll_\rho g_q\min(X,|\beta|^{-1})$. Consequently the real integral tail $|\beta|>P/X$ before its coefficient in (7) is $O_\rho(g_qg_s X/P)$. Summing over all pairs and $r\le P$ costs $O_\rho(\mathfrak S(N)X/P)$ pointwise, by the absolute Euler bound and $\sum_{q\le U_*} g_q\ll1$. With the real integral restored, Fourier inversion gives exactly $\int_I w_q(t)w_s(N-t)\,dt$, since $N-I\subseteq I_0(N)$; this integral is $O_\rho(Xg_qg_s)$. There is no Mellin or Perron cutoff here.

For the separate tail $r>P$ define

$$
 \mathcal E_N=\sum_{q,s\in\mathcal Q_N}g_qg_s
                    \sum_{r>P}|\Gamma_{q,s}(r;N)|.
$$

We show $\sum_{X\le N\le2X,\ N\ {\rm even}}\mathcal E_N\ll XP^{-1/2}$. Multiply each term with $r>P$ by $r^{1/2}/P^{1/2}\ge1$, and separate off the squarefree primes in $\{q,s\}$ from $r$. In the remaining integer $u$ coprime to $qs$, the factor is $\mu(u)^2 |c_u(N)|/\varphi(u)^2$ and its average is bounded by $2X\tau(u)\mu(u)^2/\varphi(u)^2$, using $\sum_{N\le2X}|c_u(N)|\le2X\tau(u)$ from the divisor formula. At the special primes, the true unit masks already fix $|c_q(N)|=|c_s(N)|=1$. Thus after taking their explicit factors, the remaining upper bound can drop those masks and use the whole dyad in the $u$ average. For $q\ne s$ the Rankin factors from the special primes are
$(1+q^{1/2}/(q-1))(1+s^{1/2}/(s-1))=O(1)$. For $q=s$ its factor is $1+q^{1/2}$. This latter factor is summable against $g_q^2\le q^{-2}$ on the fixed cofactor envelope, so no uniform diagonal bound is silently assumed. The distinct pair weights sum to $O(1)$ as well. The remaining series

$$
   \sum_{u\ge1}\frac{\mu(u)^2 u^{1/2}\tau(u)}{\varphi(u)^2}
$$

converges by its Euler product. These checks prove the claimed absolute averaged bound for $\mathcal E_N$, even though the true selections $q,s\in\mathcal Q_N$ vary with $N$. Markov now gives $\mathcal E_N\le L^{-A}$ outside $O(X L^{A-E/2})=O_{A,b}(X L^{-b})$ even targets, independently of $I$. On these moduli completing (7) costs at most $O_\rho(X L^{-A})$ after real inversion. By (8) the completed main integral is exactly $M_N(I)$, not just its diagonal-free high-cofactor approximation.

The full-circle coefficient is $C_N(I)$ by integer orthogonality. Combine the exact pairwise major evaluation and §1 on the union of their good moduli, and use $\mathfrak S(N)\gg1$ for even $N$ to absorb unweighted errors. This proves (1) with both endpoint choices and all genuine cofactors simultaneously.
