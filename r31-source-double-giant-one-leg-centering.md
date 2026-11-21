# Pointwise centering of the one-sided terms in the double-admissible interior

**Scope.** Assume global Dirichlet GRH. Fix $0<\rho<1/2$ and $0<\kappa\le1/2000$, let $L=\log N$, and take sufficiently large even $N$. The raw interval $I$ is any hard interval in $[\rho N,(1-\rho)N]$, with either endpoint convention. Let

$$
 {\cal P}_N=\{q\text{ prime}:N^\kappa\le q\le N^{1/2-\kappa},\ (q,N)=1\}.
$$

The selected arithmetic sum consists of the quadruples $qp+se=N$, $qp\in I$, $(qp\,se,N)=1$, with $q,s\in{\cal P}_N$ and $p,e$ prime. To identify this exact sector of the long-divisor sum, set

$$
 D=\lfloor\sqrt N\,e^{-20L/\log L}\rfloor,\qquad
 Q=\lfloor N\,e^{-20L/\log L}\rfloor.
$$

For fixed $\rho,\kappa$ and large $N$, both $q,s\le D$, while $p,e\ge\rho N^{1/2+\kappa}>D$ and $pD,eD>Q$. All four prime bases exceed $\log N$, so the raw roughness restrictions are automatic. On $n=qp$ the only long divisors are $p,qp$; the latter contributes zero to $\sum_{d\mid n,d>D}\mu(d)\log(n/d)$, and the former contributes $-\log q$. Likewise the other leg contributes $-\log s$. The cutoff $de>Q$ is automatic for all the two-leg products in this sector. Thus the coefficient here is $\log q\log s$ before the negative sum-alias sign. No assertion about all sectors at these cutoffs or about their endpoints is needed.

Let $z=\kappa L/1000$ and set

$$
 W=\prod_{\substack{\ell\le z,\ \ell\ {\rm prime}\\\ell\nmid N}}\ell,\qquad
 K_N=N/\varphi(N),\qquad K_W=W/\varphi(W),\qquad
 b(t)=\frac{K_NK_W}{\log t}{\bf1}_{(t,W)=1}.
$$

Here $b(p),b(e)$ are used only on integers $p,e\ge\rho N^{1/2+\kappa}$. Denote $a(t)={\bf1}_{t\ {\rm prime}}$, $\xi=a-b$. Write $\mathcal L(I)$ for the exact quadruples above with $p,e$ positive **integers** and $q,s\in{\cal P}_N$ distinct, so all their unit constraints are still imposed. For weights $f,g$ write

$$
 [f,g]_I=\sum_{(q,s,p,e)\in\mathcal L(I)}(\log q)(\log s) f(p)g(e).
$$

Thus $A_\kappa(I;N)=[a,a]_I$ is the genuine original prime-cofactor sum, not its majorant. Define the local-density comparator $M_\kappa(I;N)$ by the following formula, with $S=\mathfrak S(N)$:

$$
 S\sum_{\substack{q,s\in{\cal P}_N\\q\ne s}}
 \frac{q-1}{q-2}\frac{s-1}{s-2}
 \frac{\log q\log s}{q s}
 \int_I \frac{dt}{\log(t/q)\log((N-t)/s)} .
$$

**Theorem.** Uniformly in $I$, the two true single-error terms satisfy

$$
 |[\xi,b]_I|+|[b,\xi]_I|\ll_{\rho,\kappa} N^{1-\kappa/4}, \tag{1}
$$

and the genuine centered interior has the quantitative identity

$$
 A_\kappa(I;N)-M_\kappa(I;N)
 =[\xi,\xi]_I+O_{\rho,\kappa}\!\left(N^{1-\kappa/4}+\frac{SN}{L\log L}\right). \tag{2}
$$

Only the last, genuinely two-sided arithmetic correlation remains unbounded at the desired scale. In particular (2) is not a pointwise asymptotic for $A_\kappa$, and neither the full original operator nor S is bounded here.

## 1. Synthetic main term with exact units

Because $N$ is even and $(W,N)=1$, for each prime $\ell\mid W$ the two forbidden residues of $n=qp$ are $0,N$, distinct. Put

$$
 {\cal U}=\{u\bmod W:(u(N-u),W)=1\},\qquad |{\cal U}|=\prod_{\ell\mid W}(\ell-2),\qquad
 S_z=K_N K_W^2 |{\cal U}|/W .
$$

When $W=1$ the usual empty product convention applies. The correct full singular series is $S=K_N\prod_{\ell\nmid N}(1-(\ell-1)^{-2})$, so

$$
 S_z=K_N\prod_{\substack{\ell\le z\\\ell\nmid N}}\left(1-\frac{1}{(\ell-1)^2}\right)
     =S\left(1+O_\kappa((L\log L)^{-1})\right). \tag{3}
$$

Only convergent good-prime factors are truncated. Chebyshev on dyadic shells gives $\sum_{\ell>z,\ \ell\ {\rm prime}}\ell^{-2}\ll(z\log z)^{-1}$. One cannot omit the $K_N$ factor if $N$ has many prime factors outside $W$.

For fixed distinct $q,s$ and $u\in{\cal U}$ the constraints $q\mid n,\ s\mid N-n,\ n\equiv u\bmod W$ specify one residue modulo $qsW$; the moduli are coprime. The actual units $(n,N)=1$ are $\sum_{r\mid N,\ r\mid n}\mu(r)$, with every such $r$ coprime to $q s W$, so the density is $\varphi(N)/(NqsW)$, with error $O(2^{\omega(N)})$ on every real subinterval. Abel summation applies to $\big(\log(t/q)\log((N-t)/s)\big)^{-1}$, whose supremum plus variation on the central interval is $O_\rho(L^{-2})$. Thus

$$
 [b,b]_I
 = S_z\sum_{\substack{q,s\in{\cal P}_N\\q\ne s}}\frac{\log q\log s}{qs}
    \int_I \frac{dt}{\log(t/q)\log((N-t)/s)}
    +O_{\rho,\kappa}(N^{1-3\kappa/2}). \tag{4}
$$

For this error use at most $N^{1-2\kappa}$ pairs, $W\le N^{\kappa/100}$ by Chebyshev at $z=\kappa L/1000$, $2^{\omega(N)}=N^{o(1)}$, and $(K_NK_W)^2\ll L^4$ by Mertens; the log markers are offset by $L^{-2}$. The constants in this power bound can depend on fixed $\kappa$. The unweighted-in-$S_z$ main sum is $O_\rho(N)$, by the two Chebyshev bounds $\sum_q(\log q)/q\ll L$. The factors $(q-1)/(q-2),(s-1)/(s-2)$ in $M_\kappa$ differ from one by $O(N^{-\kappa})$, uniformly. In combination with (3) and (4) this proves

$$
 [b,b]_I=M_\kappa(I;N)+O_{\rho,\kappa}\!\left(N^{1-3\kappa/2}+\frac{SN}{L\log L}\right). \tag{5}
$$

## 2. A maximal one-prime progression bound for the convolved outer leg

For $s\in{\cal P}_N$ and each reduced residue $v\bmod sW$, put

$$
 T_{s,v}(I)=\sum_{\substack{q\in{\cal P}_N,\ q\ne s;\ p\text{ prime}\\ (p,N)=1,\ qp\in I,\ qp\equiv v\bmod sW}}\log q,\qquad
 D_s(I)=\sum_{\substack{q\in{\cal P}_N\\q\ne s}}\frac{\log q}{q}\int_I\frac{dt}{\log(t/q)} .
$$

The needed uniform estimate is

$$
 \sum_{s\in{\cal P}_N}\max_{(v,sW)=1}\sup_I
 \left|T_{s,v}(I)-\frac{D_s(I)}{\varphi(sW)}\right|
 \ll_{\rho,\kappa}N^{1-\kappa/3}. \tag{6}
$$

The modulus here is $sW$, not $N$. We prove this with the [primitive-character large sieve, Montgomery–Vaughan, Theorem 19.16](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=186), and with the standard individual GRH character PNT (for example [E. S. Lee, Theorem 4.3 and the $\theta(x,\chi)$ estimate](https://arxiv.org/html/2301.13457v2#S4)), only for the small-conductor terms. Neither a fixed-residue theorem with constants depending on the numerator nor simultaneous primality is an input.

Split $q$ and $s$ into dyads of scales $U$ and $R$ with $U,R\in[\tfrac12N^\kappa,N^{1/2-\kappa}]$, intersecting the original endpoints. Set $P=N/U$. For the chosen $q$ dyad every centrally contributing $p$ is in the fixed interval $[\rho P/2,(1-\rho)P]$, so it is harmless to restrict the prime $p$ sequence to that interval. Primes on both sequences are units modulo $W$; also every such $p$ exceeds every $s$ for all large $N$ at fixed $\kappa,\rho$. Remove $p\mid N$ from its sequence and $q\mid N$ from the other as stated. Dependence on $s$ is only through characters mod $sW$ and exclusion $q=s$, which is built into those characters. A principal character term sums ordinary primes $p$ in $I/q$, excluding at most $\omega(N)$ primes and with $q\ne s$, giving $D_s(I)+O_\rho(U\sqrt P\,L^C)$ in the numerator by the RH PNT and Abel summation. For a nonprincipal character induced from conductor $d\mid W$, its restriction to $p$ is independent of $s$; the removed primes only cause $O(L)$. The uniform GRH estimate $\sum_{p\in\mathcal J}\chi^*(p)\ll\sqrt P\,L^C$ on intervals $\mathcal J$ in that range follows by partial summation from the standard weighted estimate with a $\log p$ marker. Summing over $q\ne s$ costs $U L$. At most $\varphi(W)$ characters mod $sW$ are of either small-conductor kind altogether. After multiplying by $1/\varphi(sW)$ and summing over the $s$ dyad, their $\varphi(W)$ factor cancels and $\sum_{s\sim R}(s-1)^{-1}\ll1$. Thus the aggregate small-conductor and principal discrepancy is $O_\rho(U\sqrt P\,L^C)$ on the pair of dyads, uniform in its intervals.

All other characters have conductor $s d$ for some $d\mid W$; an induced character agrees with its primitive character on these $p,q$ supports, including when $q=s$, where both vanish. Orthogonality gives coefficient $1/\varphi(sW)\ll1/R$, and the residue phase is of modulus one. For each fixed $d$ the conductors $s d$ are distinct as $s$ varies, bounded by $2dR$. To separate the product interval use the truncated Perron formula at real part $1$ and height $N^4$, with half-integer endpoints chosen to give exactly the selected integer products. Because $qp\asymp_\rho N$, each Perron error is $O_\rho(N^{-3})$, using $|\log(Y/(qp))|\gg_\rho N^{-1}$, with $Y$ the half-integer endpoint. Changes at the real endpoints are not needed in the continuous principal model, which was estimated directly. The integral has $O(L)$ weight even after taking the supremum over $Y$; pull all phases of $Y$ out in absolute value. At fixed imaginary part $\tau$ the two coefficients on the dyads are twisted by $q^{-1-i\tau}$, $p^{-1-i\tau}$, with product of their $\ell^2$ norms times $Y$ bounded by $O_\rho(\sqrt N L)$. Taking absolute values and applying Cauchy–Schwarz and the primitive-character large sieve once to each separated factor therefore gives the bound

$$
 \ll_\rho L^C\frac{W\sqrt N}{R}
       \sqrt{(U+(WR)^2)(P+(WR)^2)}
 \ll_\rho L^C W^3 N^{1-\kappa/2}.
$$

Here at most $W$ divisors $d\mid W$ were used, and the four elementary terms after expanding the square-root product are bounded using $N/R,\sqrt{NU},\sqrt{NP},\sqrt N R$, each $O(N^{1-\kappa/2})$. The Perron remainders summed over characters contribute negligibly, since each dyad has at most $O(N)$ raw tuples with log marker at most $L$ and $\sum_\chi1/\varphi(sW)=1$. This estimate permits the maximum over residues and supremum over intervals separately for each $s$: the same nonnegative integral majorant applies before summation. The extra $O(L^2)$ dyad count and all fixed log losses, together with $W\le N^{\kappa/100}$, fit in the target $N^{1-\kappa/3}$. This proves (6).

## 3. The single-error terms genuinely disappear

In $[a,b]_I$ the factor $b(e)$ is supported on $n\equiv u\bmod W$ with $N-u$ a unit; $a(p)$ forces $u$ to be a unit as well. For each $u\in{\cal U}$ and $s\in{\cal P}_N$, write $v(u,s)$ for the CRT combination $u\bmod W,\ N\bmod s$, a reduced residue. Since $q,s$ are units modulo $N$, actual prime $p$ is counted subject to $(p,N)=1$, as in $T_{s,v}$; $e=(N-n)/s$ then automatically satisfies $(e,N)=1$. Consequently the exact sum is

$$
 [a,b]_I
 =K_NK_W\sum_{s\in{\cal P}_N}\log s
       \sum_{u\in{\cal U}}\int_I\frac{dT_{s,v(u,s)}(t)}{\log((N-t)/s)},
$$

where $dT$ is the atomic progression counting measure. Apply (6) by Abel summation, against a weight whose supremum plus variation is $O_\rho(L^{-1})$. The error is $O_{\rho,\kappa}(N^{1-\kappa/4})$, since the $\log s$ marker cancels $L^{-1}$, $K_NK_W\ll L^2$, $|{\cal U}|\le W\le N^{\kappa/100}$, and (6) has exponent $1-\kappa/3$.

The resulting main term is exactly

$$
 S_z\sum_{\substack{q,s\in{\cal P}_N\\q\ne s}}\frac{\log q\log s}{q(s-1)}
 \int_I\frac{dt}{\log(t/q)\log((N-t)/s)},
$$

since $K_NK_W|{\cal U}|/\varphi(sW)=S_z/(s-1)$. Its only difference from the main term of (4) is the factor $s/(s-1)=1+O(N^{-\kappa})$, costing $O_\rho(S_zN^{1-\kappa})$. Thus $[a,b]_I-[b,b]_I=[\xi,b]_I$ satisfies (1); reflection $n\leftrightarrow m$ gives the other term. Expanding $[a,a]_I$ exactly and using (5) proves (2).

In the [physical log kernel](r24-arithmetic-growing-compensation.md), these signed errors also transfer to the selected central subkernel after normalization by $N$, with the original sum-alias sign: each cumulative rectangle is one hard raw interval on the sum line; its extra $\sqrt{(n/N)(m/N)}$ weight has bounded variation there. Abel summation transfers the uniform signed interval errors. The resulting kernel is supported at cumulative endpoints in $[\rho,1]^2$, where the physical Hardy factors and log area are bounded in terms of $\rho$. Thus the normalized error in Hilbert–Schmidt norm is $O_{\rho,\kappa}(N^{-\kappa/4}+S/(L\log L))$.

The uncanceled term $[\xi,\xi]_I$ is a sum of products of **two** residual primality weights at $p,e$ satisfying the same fixed-target linear relation. The large sieve in (6) only controls an unweighted-in-$p,e$ progression total on one leg, or a smooth weight from the other surrogate. It does not control the varying residual $\xi((N-qp)/s)$. No estimate for that covariance, or compensation against other genuine rough sectors, is claimed.
