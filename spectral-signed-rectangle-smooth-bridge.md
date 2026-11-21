# A smooth divisor bridge for pointwise central positivity

**Scope.** This improves the sufficient arithmetic hypothesis in the [signed rectangle criterion](spectral-signed-rectangle-central-positivity.md). The signed discrepancy remains unestimated. The implication here is arithmetic and does not assume GRH; it does not establish Hypothesis S.

Let $N$ be large and even, $S=\mathfrak S(N)$, $L=\log N$, $a=1/2$, $b=9/16$. Fix a real weight $W$ supported in $(a,b]$, with bounded variation on zero extension. Write $m=N-n$, and let
$$
 G_W=\frac1N\sum_{\substack{n+m=N\\(nm,N)=1}}\Lambda(n)\Lambda(m)W(n/N),
 \qquad
 P_W=\frac1N\sum_{\substack{n<N\\(n,N)=1}}\Lambda(n)\mu(N-n)W(n/N).
$$
Choose $D=\lfloor\sqrt N/L^C\rfloor$ with $C$ a sufficiently large fixed constant, and put $Q_0=N/D$, $Q=\lfloor Q_0\rfloor$. Define the actual unit central increment at a real pair of cutoffs by
$$
 B^+(t,y)=
 \sum_{\substack{q\le t\\(q,N)=1}}\mu(q)
 \sum_{\substack{N/2<n\le y\\(n,N)=1}}
    \Lambda(n)\mu(N-n)
       \left(\mathbf1_{n\equiv N\bmod q}-\frac1{\varphi(q)}\right),
 \quad aN\le y\le bN.
$$
Only squarefree $q$ contribute. Set $M(t)=\sup_{aN\le y\le bN}|B^+(t,y)|$ and $B_*^+=\sup_{1\le t\le Q}M(t)$. Define also the weighted auxiliary-modulus profile
$$
 \mathcal D_N=
 \int_1^{7Q_0/32}\frac{M(t)}{t}\,dt
   +\frac{L}{Q_0}\int_{7Q_0/32}^{Q_0/2}M(t)\,dt .
$$
This integrates an auxiliary rectangle endpoint at one fixed $N$, not an average over different $N$.

For every fixed $A>0$ (with $C$ chosen sufficiently large in terms of $A$), the transfer is
$$
 G_W=S\left(\int W-P_W\right)
       +O_{A,W}\left(L^{-A}+\frac{\mathcal D_N}{N}\right)
 =S\left(\int W-P_W\right)
       +O_{A,W}\left(L^{-A}+\frac{L B_*^+}{N}\right).
 \tag{1}
$$
In the second equality only the bound $\mathcal D_N\ll L B_*^+$ is used. In particular no partition into sharp moving-edge bins is necessary.

## 1. Smooth split, with the same arithmetic main terms

Choose a fixed smooth real function $\chi$ with $0\le\chi\le1$, equal to $1$ on $[0,1]$ and to $0$ on $[2,\infty)$, and put $R=1-\chi$. Insert $\mu^2(m)$ at normalized cost $O_W(N^{-1/2}L^2)$ for deleting proper prime powers in $m$. In the exact identity $\Lambda(m)=-\sum_{d\mid m}\mu(d)\log d$, split each term using the weights $\chi(d/D)$ and $R(d/D)$.

For the short part, the proof of the signed rectangle criterion applies with only the changes $d\le 2D$ and the extra bounded multiplier $\chi(d/D)$. In particular, expand the squarefree mask and cut the square divisor base $b'$ at a large fixed power of $L$. The tail bounds continue to count positive multiples, and the untwisted maximal Bombieri–Vinogradov estimate applies to all $[b'^2,d]\le 2D b'^2$ with the same polylogarithmic multiplicity and logarithmic coefficient. Increase $C$ by a fixed amount if necessary. The Euler coefficients for the main term are the same as in that criterion. Their hard cutoff sums with weight $-\log d$ equal the full value $S$ to every inverse log power uniformly for cutoffs in $[D,2D]$ (up to the factored squarefree product). Consequently summation by parts over the transition of $\chi$ gives the same normalized short main term $S\int W$ and an $O_{A,W}(L^{-A})$ error. This uses ordinary prime distribution and the classical zero-free-region Mertens estimate, not GRH.

For the long part, on squarefree $m$ put $q=m/d$, so the exact Möbius sign is $\mu(d)=\mu(m)\mu(q)$. The raw logarithm is $\log(m/q)$; the mask becomes $R(m/(Dq))$, vanishing for all $q\ge m/D$. For nonsquarefree $m$ both weighted sums vanish. The progression baseline after switching is, at each $m$ on the given support,
$$
 \sum_{\substack{q\le Q\\(q,N)=1}}
    \frac{\mu(q)}{\varphi(q)}R(m/(Dq))\log(m/q)
       =S+O_A(L^{-A}).
$$
To check it, first use the hard lower-cofactor model with $q<m/D$, whose zeroth and logarithmic Euler moments were established in the prior criterion. The difference of the weights is supported on $q\in[m/(2D),m/D]$ and has bounded-variation norm $O(L)$, including a possible jump of the hard model at its strict endpoint. Uniform inverse-log saving for the zeroth moment in this interval gives the error by summation by parts, after requesting one extra log power. Both of its endpoints have fixed positive-power size in $N$. Thus the baseline gives $-SP_W$, with an arbitrarily small inverse-log error (take an additional saving to absorb the harmless normalized bound on the absolute primitive).

## 2. A Lipschitz-scale transition and two successive Abel steps

For $x=n/N\in[a,b]$ and $1\le t\le Q$, put
$$
 K(x,t)=R\big((1-x)Q_0/t\big)\log\big(N(1-x)/t\big).
$$
Then $K(x,Q)=0$ for all sufficiently large $N$, since $Q>Q_0/2$. At each $n$, define $\Delta_q(n)$ to be the summand in $B^+(t,y)$ before summing over $n,q$. Exact integration of $\partial_tK$ gives the identity, including at integer endpoints,
$$
 \sum_{q\le Q}\Delta_q(n)K(x,q)
    =-\int_1^Q \partial_tK(x,t)\sum_{q\le t}\Delta_q(n)\,dt .
$$
Multiply by $W(x)$ and sum over the strict central $n$; the sums are finite. For fixed $t$, Abel summation in $n$ now weighs its signed prefix by the function $W(x)\partial_tK(x,t)$. Because the underlying discrete measure starts strictly above $aN$, left limits in the prefix definition handle any jump of $W$ or its endpoint, with no omitted atom. Thus the inner sum is bounded by
$$
 O\big(M(t)\|W(\cdot)\partial_tK(\cdot,t)\|_{\rm BV}\big).
$$

For $t\le 7Q_0/32$ the multiplier $R$ is identically one throughout $[a,b]$. Hence $\partial_tK=-1/t$ is independent of $x$; this pays $1/t$ in the preceding bound. For $t\ge Q_0/2$ the multiplier and all derivatives in use vanish. In the intervening interval $t\asymp Q_0$, put $\rho=(1-x)Q_0/t$. Then
$$
 \partial_tK=-\frac{R(\rho)+\rho R'(\rho)\log(N(1-x)/t)}{t}.
$$
Both $\partial_tK$ and $\partial_x\partial_tK$ are $O_\chi(L/Q_0)$ there: $\rho$ and $\partial_x\rho$ are bounded, the logarithm is $O(L)$, and its $x$ derivative is bounded. Hence the product variation in $x$ costs $O_{W,\chi}(L/Q_0)$. The two ranges give exactly $O_{W,\chi}(\mathcal D_N)$ for the **raw** long discrepancy. Divide by $N$ and combine with the two main terms to prove (1).

## 3. One-sided consequence with no separate primitive assumption

Let $p_0$ be the least prime not dividing $N$; $3\le p_0\ll L$ by the ordinary Chebyshev bound, and $p_0\le Q$ for large $N$. Put
$$
 J_{p_0} = \sup_{aN\le y\le bN}
          |B^+(p_0,y)-B^+(p_0-1,y)|.
$$
The sign in this jump is $\mu(p_0)=-1$, so it controls the actual individual central progression discrepancy at $p_0$. For fixed $W\ge0$, the least-missing-prime argument applied to these increments gives
$$
 |P_W|\le(1-1/p_0)\int W+O_{A,W}(L^{-A}+p_0 J_{p_0}/N).
$$
In detail, Abel against $W$ controls the difference from the $p_0$ progression normalized by $\varphi(p_0)$. Along that progression $|\mu(m)|=\mu^2(m)\le 1-\mathbf1_{p_0^2\mid m}$. The ordinary Siegel–Walfisz estimate at the reduced residues modulo $p_0,p_0^2$ gives the renormalized factor $1-1/p_0$. The necessary moduli are $O(L^2)$, and deleting nonunit prime powers is negligible. The fixed support above $a$ uses precisely the central increments, not the earlier part of the prefixes.

For any fixed such $W$ with $\int W>0$, the two conditions
$$
 \mathcal D_N=o(NS/p_0),\qquad J_{p_0}=o(N/p_0^2)
 \tag{2}
$$
therefore imply $G_W\gg_W S/p_0$ and $\gg_W SN/(p_0L^2)$ central prime pairs after removing proper powers. No boundedness of $S$ is assumed. A simpler sufficient condition is
$$
 B_*^+=o\!\left(N\min\{S/(Lp_0),\ p_0^{-2}\}\right).
$$
In particular $o(N/L^2)$ suffices uniformly, and if $p_0$ stays bounded then $o(N/L)$ suffices and gives predicted-order central count. Neither (2) nor its simpler sufficient condition is proved here; positivity is weaker than the asymptotic or the full weak-S operator bound.
