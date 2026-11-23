# A polynomial largest-prime threshold on true rough mixed partners

**Scope.** We enter a polynomial range below the square root for the actual above-BV mixed minor, on a genuine rough-partner selector. For any fixed $0<\delta<1/4$, the lower gate for the largest prime is now $P^+(m)>N^{1/2-\delta}$. Both squarefree Möbius parities are covered when the least prime exceeds $\exp((\log N)^\beta)$, $1/2<\beta<1$; odd total parity is covered for every fixed $0<\beta<1$. The full arithmetic bound is unconditional, and the signed minor bound uses only the former prime-progression Dirichlet GRH input. This does not control the complement of either prime-factor gate or the full central Hardy profile.

Use the central variables, hard left interval $I$, weight $\omega$, left prime polynomial $P_{I,\omega}$, squarefree mixed coefficient $M_>$ and major arcs with $Q=N^{1/1000}$ from the [least-prime-conditioned proof](r68-spectral-least-prime-conditioned-mixed-minor.md). In particular, $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ with fixed $B>B_0>0$, and $x\in V=[N/3,2N]$ is the real partner variable. Put $U=L^\beta$, $G=\exp U$. Let $A(m)$ be the actual $M_>(m)$ restricted to $m\in V$, $P^+(m)>N^{1/2-\delta}$ and $P^-(m)>G$, optionally on one of the two parities. Define

$$
 \mathcal B_{\rm odd}=\frac{L_2^4}{U}+\frac{L_2^2}{L},\qquad
 \mathcal B_{\rm all}=\mathcal B_{\rm odd}+\frac{\sqrt{L L_2}}U,
 \qquad
 c_\delta=\min\!\left(10^{-4},\,\frac{1/4-\delta}{4}\right).
 \tag{1}
$$

With $\mathcal B=\mathcal B_{\rm odd}$ for the odd selector and $\mathcal B=\mathcal B_{\rm all}$ otherwise, we establish

$$
\begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
     &\ll \frac{\Sigma(N)|I|}{L}\mathcal B+N^{1-c_\delta},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)
                     e(-N\theta)\,d\theta\right|
     &\ll \frac{\Sigma(N)|I|}{L}\mathcal B+N^{1-c_\delta}.
\end{split} \tag{2}
$$

Here $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$, and constants can depend on the fixed exponents, cutoff constants, and weight bounds. Thus the two asserted parameter ranges give $o(\Sigma(N))$ after the original $L/N$ normalization.

## 1. Geometry and surviving factors

Choose the actual largest prime $p$ and write $m=pk$ with $p>P^+(k)$ and $p>N^{1/2-\delta}$. Then $k$ is squarefree and $G$-rough, since $p$ already exceeds $G$. As before $M_>=-\Xi_D-M_\le$ exactly, and the proof that $k\le D$ does not contribute is unchanged: there $p=x/k>H_0$ and $p>D$, so low mixed divisors cannot occur and the exact prime-or-complete-product identities handle $\Xi_D$. The remaining cofactor range is

$$
 D<k\le 2N^{1/2+\delta},\qquad T_1=k/D,\quad T_2=Dk/x,\qquad
 Z=10N^\delta L^B.
 \tag{3}
$$

Both cutoffs are at most $Z$ with room for the cell brackets. For composite squarefree $k$, the exact formulas valid with either parity are

$$
\begin{split}
 F_{0,D}(pk)&=-\mu(k)S_k(T_1^-)-S_k(T_2),\\
 F_{1,D}(pk;x)&=a(x)F_{0,D}(pk)
                   +\frac{2}{\log x}\bigl(\mu(k)J_k(T_1)-J_k(T_2)\bigr),\\
 a(x)&=\log(x/D^2)/\log x=O(L_2/L).
\end{split} \tag{4}
$$

On this composite support $-\Xi_D=F_{0,D}F_{1,D}$. The two positive real cutoffs have log ratio $2B\log L+O(1)>0$, even when either one still lies below 1. Thus if $\mu(m)=+1$ ($\mu(k)=-1$) the first factor is the signed open shell $T_2<r<T_1$ on the divisors of $k$. If $\mu(m)=-1$ ($\mu(k)=+1$) the integrated term in the second factor is instead the integral between the two cutoffs.

Partition $V$ in $x$ and the cofactor range in $k$ into hard geometric cells with log width $O(\eta)$ for $\eta=L^{-1/2}$. Include a cut at $k=10D L^{2B}$, and write $K<k\le K'$ with $w=\log(K'/K)$ for one arithmetic cell. The widths sum to $O(L)$ and the number of cells in either variable is polylogarithmic. Above the added cut $T_2\ge5$ since $x\le2N$. Below it the only possible divisor in the two sharp primitives is 1, since the cutoffs are at most a fixed power of $L$ and $k$ is $G$-rough. There $J_k(T_j)=(\log T_j)_+$, so the product is $O(L_2/L)$ and its reciprocal total over the border interval is $O(L_2^2/L)$. If $k$ is prime, the genuine largest-prime condition forces $D<k<\sqrt x\le\sqrt{2N}$. Therefore its reciprocal mass is $O(L_2/L)$ by ordinary PNT, and the actual sharp product in this range is one. The larger interval in (3) is not used for that prime term.

## 2. True rough reciprocal squares in the polynomial range

For rough labels $r,t\le Z$, the Bonferroni reciprocal count from the [least-prime-conditioned proof](r68-spectral-least-prime-conditioned-mixed-minor.md) now uses the fixed roughness threshold $G$ on $k$ itself. The proof works because $G^{O(L_2^2)}=N^{o(1)}$ for $\beta<1$, and $K\ge D=N^{1/2-o(1)}$. It gives a main term $w V_G/[r,t]$ with $V_G=\prod_{p\le G}(1-1/p)\ll1/U$, and error

$$
 O_{A_0}\bigl(wL^{-A_0}/[r,t]+N^{-1/2+o(1)}\bigr)
 \tag{5}
$$

uniformly for arbitrary short cells. For clarity one applies the even/odd truncated exclusion inequalities to positive reciprocals of multiples of $[r,t]$, using depth $\asymp L_2^2$ and the tail $(\sum_{q\le G,\ q\ {\rm prime}}1/q)^R/R!$; the resulting errors in a **signed** square are bounded only after the main term is formed. Summing (5) in a divisor square whose coefficients are $O(L)$ costs at most $O_{A_0}(wL^{-A_0}+N^{-1/2+2\delta+o(1)})$, since the reciprocal lcm sum is $O(L^3)$ and $Z^2=N^{2\delta+o(1)}$. One first takes a larger $A_0$ in (5). The floor saves a fixed power because $\delta<1/4$. We may maximize bound estimates by removing the squarefree or parity masks after taking a nonnegative square, while retaining the actual rough mask needed for the main term.

The logarithmic harmonic bound and masked reciprocal Mertens argument of that proof also apply with $Z$ in (3). Specifically, the rough nonunit reciprocal sum on a log interval of width $H$ is $O(H/U+(1+H)e^{-3U/4})$. If $e$ is a squarefree rough integer up to $Z$, the masked primitive $R_{G,e}$ omits primes $\le G$ and those dividing $e$. It is the convolution of the ordinary reciprocal Mertens primitive with a positive reciprocal Euler measure. Its total mass and its exponential moment at $1/U$ are $O(U)$: the extra primes dividing $e$ contribute $O((\log Z/U)e^{1-U})$ to the logarithm of the product. Consequently

$$
 \|R_{G,e}\|_1\ll U,\qquad
 R_{G,e}(u)\ll_{A_0} L^{-A_0}\quad (u>C_{A_0} U L_2).
 \tag{6}
$$

This uses only $\log Z\ll L$ for the new polynomial ranges. At smaller nonnegative $u$ the unsigned rough harmonic bound gives $O(1+u/U)$, and $R_{G,e}(u)=0$ below zero. Strict endpoints obey the same estimates. These are ordinary reciprocal Möbius estimates, not estimates in prime progressions.

Let $\mathcal E_G(f)$ be the rough signed lcm square with weights $\mu(r)f(r)$. Expand the gcd, so for each rough $e\le Z$ its contribution is $\varphi(e)\mu(e)^2/e^2$ times the squared masked reciprocal primitive with the cutoff weight $f(ed)$. Three bounds follow:

- A signed shell of log width $W=O_B(L_2)$ **excluding** 1 has energy $O(L_2/U)$. The outer $e$ with a scaled endpoint in the range $O_{A_0}(U L_2)$ have rough reciprocal sum $O_{A_0}(L_2)$, and the inner nonunit contributions are $O((1+W)/U)$. The unit part only occurs where $e$ itself is in the original shell, and now $e=1$ is excluded, so its reciprocal sum is $O((1+W)/U)$. The far outer $e$ contribute a negligible power of $L^{-1}$ by (6). The total bound is $O((1+W)/U+L_2(1+W)^2/U^2)=O(L_2/U)$.
- An ordinary signed cutoff has rough energy $O(L_2^3)$. The same near outer $e$ count $O_{A_0}(L_2)$ combines with the pointwise bound $O_{A_0}(L_2)$ on its inner primitive. The far range is negligible by (6).
- For the integrated cutoff $f(r)=(\log(T/r))_+$, $T\le Z$, the inner integral is at most $\|R_{G,e}\|_1\ll U$. Summing over all rough $e\le Z$ costs $O(1+L/U)$. Thus the integrated energy is $O(L U)$.

All bounds are uniform in the actual cutoff values and endpoint choices. For moving unsigned boundary shells of width $O(\eta)$, write $r=ea$, $t=eb$, $e=(r,t)$. The one-unit case for $a,b$ is impossible by $U\gg\eta$. If both are 1 the reciprocal contribution is $O(1)$, or $O(\eta/U)$ when the original shell excludes 1. The nonunit-pair contribution is $O((\eta/U)^2(1+L/U))$ by the rough harmonic estimate; this is $O(1)$ always and $O(\eta/U)$ if $\beta>1/2$. This also bounds boundary shells containing the exact cutoff integer.

## 3. Distinct parity savings

Work on fixed physical and arithmetic cells above the border. For even total parity, freeze the narrow shell endpoints in (4) and use the two unsigned boundary shells as an envelope for the difference. All three shells exclude 1. Applying (5) and the shell bounds shows that the squared reciprocal mean of a uniform majorant for $F_{0,D}$ on rough $k$ is

$$
 O\bigl(wL_2/U^2+N^{-1/2+2\delta+o(1)}\bigr)
 \qquad(\beta>1/2).
 \tag{7}
$$

For either individual integrated cutoff $J_k(T_j)$, the fixed-cutoff reciprocal square is $O(wL+N^{-1/2+2\delta+o(1)})$ by (5) and the integrated energy. When its endpoint moves, the change is at most the integral of $|S_k(t)|$ in a fixed log bracket of width $O(\eta)$. Cauchy in that bracket and the signed fixed primitive bound give squared reciprocal error $O(\eta^2(w L_2^3/U+N^{-1/2+2\delta+o(1)}))$, absorbed in the same bound. The $F_{1,D}$ square therefore has main bound $O(w/L)$ by (4), (7), and $a(x)=O(L_2/L)$. This gives an even-parity reciprocal product bound $O(w\sqrt{L L_2}/(LU))$ by Cauchy, apart from a power-small floor.

For odd total parity, the fixed primitive and unsigned moving-boundary estimates give a uniform majorant for $F_{0,D}$ with reciprocal square $O(w L_2^3/U+N^{-1/2+2\delta+o(1)})$. The signed integral in (4) now lies in a common fixed interval in log coordinate of width $O(L_2)$ for the cell pair. Integrate the absolute primitive there and use Cauchy in the interval and the fixed primitive energy; no triangle sum of separate full integrals from 1 is needed. The main square bound for $F_{1,D}$ is $O(w L_2^5/(L^2U))$ plus the power floor. The odd reciprocal product main term is therefore $O(w L_2^4/(LU))$. This part only needs $\beta>0$.

After summing arithmetic cell widths $O(L)$, these are bounded by the corresponding rows of (1), including the border and genuine prime-$k$ case. The power-small Cauchy terms stay at most $N^{-(1/4-\delta)+o(1)}$ after all arithmetic cells. The $wL^{-A_0}$ errors in (5) have been absorbed in the main terms, since an arbitrarily large fixed $A_0$ is available.

For completeness, the low mixed $M_\le$ is especially small on this true rough selector. Its two signed divisor labels $b,c$ are below $H_0/D=L^{B-B_0}<G$, hence $b=c=1$ exactly. The remaining divisor $h$ is in $(D,H_0]$ and its centered weight is $O(L_2/L)$. Either $h\mid k$, or $h=pr$ with $r\mid k$. In the first case sum over $h$ and $k/h\le Z$: the former is rough in a log interval of width $O(L_2)$ and the latter is rough up to $Z$. In the second case sum over $v=k/r=x/h$ and $r\le Z$: for fixed physical cell $v$ lies in a single log interval of width $O(L_2)$, away from 1, and $r$ is rough up to $Z$. Both give a reciprocal majorant $O((L_2/L)(L_2/U)(1+L/U))$, absorbed in $\mathcal B_{\rm odd}$. In both cases the enlargements occur only in the positive majorant. Also $k/\varphi(k)\ll1$ on the retained rough support: $\sum_{q\mid k,\ q\ {\rm prime}}1/q\ll (L/U)e^{-U}$.

## 4. Actual full and minor transfer

Use the same two-prime upper sieve from the [genuine mixed deletion](r66-spectral-largest-prime-mixed-strip.md) on $p$ and $N-kp$ in the exact hard prime interval for each $k$ and physical cell. Both forms exceed $N^{1/100}$, as $\delta<1/4$. The per-cofactor sieve bound is $O(\Sigma(N)|I_{\rm cell}|(k/\varphi(k))/(kL^2)+N^{1/4}L)$ on genuine unit pairs. Each coefficient majorant has size $N^{o(1)}$ by the divisor bound and at most logarithmic endpoint factors. The floor cost is $N^{3/4+\delta+o(1)}$ including all cells and the left log. The reciprocal power-small floors from Section 3 are also absorbed in the error stated in (2), since $\Sigma(N)\ll L_2$ and the lengths sum to $|I|$. This proves the unconditional first line.

In the major calculation the true weight at each fixed $k$ still has supremum and variation $O(\tau_4(k))$, including the interval $p>\max(P^+(k),N^{1/2-\delta})$, as in the preceding deletion. The rough and parity selectors only mask fixed $k$. No upper envelope has been substituted into the genuine right Fourier polynomial. Under the prime AP input, the resulting right model on a reduced arc with $q\le Q$ has real coefficient $c_q(k)/[k\varphi(q)\log(x/k)]$ times that weight, since $p>Q$. Its total approximation error is

$$
 O_\epsilon\bigl(Q^2 N^{3/4+\delta/2+\epsilon}\bigr),
 \tag{8}
$$

by summing $\sqrt{N/k}$ up to $2N^{1/2+\delta}$, using the old per-cofactor progression and phase-variation error. The larger $k$ range still has $\log(x/k)\gg L$, and the occupation bound $O(L^4 C^{\omega(q)}/q)$ for the right real density's supremum and variation is unchanged: the unrestricted $\tau_4(k)/k$ harmonic sum up to $N$ bounds it with the same local occupancy factors. Thus the Fourier and pointwise Ramanujan completions in the [giant-prime major calculation](r66-spectral-above-bv-strip-deletions.md#3-the-same-upper-scale-for-the-actual-giant-major-arcs) continue to apply. The integrated error in (8) after the left factor and the $O(Q^3/N)$ total arc measure is still a fixed power below $N^{1-10^{-4}}$, for instance by taking $\epsilon=1/100$; the left approximation and completion tails are unchanged.

The completed real density has the same local factor, zero for $(k,N)>1$, otherwise $O(\Sigma(N)k/\varphi(k))$. Its reciprocal prime denominator $k\log(x/k)$ and the bounds of Section 3 show that the major coefficient is bounded by the same right side of (2), including the floor. Subtract this actual major from the true full coefficient to get the claimed minor bound. This proves a deletion only on the stipulated rough-partner selector and does not estimate the signed minor left in the complementary regimes.
