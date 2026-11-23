# Polynomial largest primes with a near-polylogarithmic least-prime gate

**Scope.** This lowers the least-prime requirement in the [polynomial largest-prime deletion](r68-spectral-polynomial-largest-rough-mixed-minor.md), still on the genuine above-BV mixed coefficient and the genuine signed minor. For fixed $0<\delta<1/4$ and $\varepsilon>0$, both Möbius parities now allow

$$
 P^+(m)>N^{1/2-\delta},\qquad
 P^-(m)>\exp(U_0),\qquad
 U_0=L_2(1+\log L_2)^{3+\varepsilon},
 \quad L=\log N,\quad L_2=1+\log L .
 \tag{1}
$$

The least-prime threshold is much smaller than $\exp(L^\beta)$, but is still larger than any fixed power of $L$. No bound on the remaining small least primes is deduced. There is no estimate for the full Hardy profile or Hypothesis S.

Retain $\Sigma(N)$, the fixed $B>B_0>0$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, $V=[N/3,2N]$, major denominator $Q=N^{1/1000}$, and the genuine hard left interval $I$, weight $\omega$, and prime polynomial $P_{I,\omega}$ from the polynomial largest-prime result. Let $A(m)$ be the true squarefree $M_>(m)$ on $V$, restricted by (1), optionally also restricted to a single Möbius parity. Uniformly at each even $N$, the actual full coefficient in absolute mass and the genuine minor coefficient satisfy

$$
\begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
     &\ll \frac{\Sigma(N)|I|}{L}\,\mathcal B+N^{1-c_\delta},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)
                    e(-N\theta)\,d\theta\right|
     &\ll \frac{\Sigma(N)|I|}{L}\,\mathcal B+N^{1-c_\delta},
\end{split}
\qquad
 \mathcal B=(1+\log L_2)^{-\varepsilon/2},
 \quad c_\delta=\min(10^{-4},(1/4-\delta)/4).
 \tag{2}
$$

For the odd-total-parity selector alone one can take $\mathcal B=(1+\log L_2)^{-\varepsilon}$. The first bound is unconditional and the second uses the historical prime-progression Dirichlet GRH input at $q\le Q$ for the two primes, as before. No Möbius progression GRH is used. The normalized error after multiplying by $L/N$ is $o(\Sigma(N))$ on the stated selector.

## 1. Preserve the true cofactor gates

As in the preceding proof extract the unique largest prime $p$ on the squarefree support, $m=pk$, $p>P^+(k)$. It exceeds $G_0=\exp(U_0)$, so the roughness of $m$ is precisely the roughness of $k$. The exact decomposition $M_>=-\Xi_D-M_\le$ retains $D<k\le 2N^{1/2+\delta}$. Use $Z=10N^\delta L^B$, geometric hard $x$ and $k$ cells of log width $O(\eta)$ with $\eta=L^{-1/2}$, and the arithmetic border $k=10D L^{2B}$. The total log width of the $k$ cells is $O(L)$. Write $x=kp$, $T_1=k/D$, $T_2=Dk/x$; the cutoffs are at most $Z$, and above the border $T_2\ge5$.

The sharp product gives $-\Xi_D$ for composite squarefree $k$. Its exact factors are

$$
\begin{split}
 F_0&=-\mu(k)S_k(T_1^-)-S_k(T_2),\\
 F_1&=a(x)F_0+\frac2{\log x}\bigl(\mu(k)J_k(T_1)-J_k(T_2)\bigr),\\
 a(x)&=\log(x/D^2)/\log x=O(L_2/L),
\end{split}
 \tag{3}
$$

where $S,J$ are as in the [least-prime-conditioned proof](r68-spectral-least-prime-conditioned-mixed-minor.md), zero at subunit cutoffs. In the even total case $\mu(m)=+1$ we have $\mu(k)=-1$, and $F_0$ is the signed **open** shell $T_2<r<T_1$. In the odd total case $\mu(k)=+1$ the integrated term of $F_1$ is the integral between these cutoffs. Their log ratio is $2B\log L+O(1)$ on $V$. Fix $W=C_B L_2$ large enough to include the uncertainty of the moving endpoints in both cell variables. Endpoint conventions are those of (3).

The prime-$k$ contribution has reciprocal mass $O(L_2/L)$ because its actual condition $p>k$ gives $k<\sqrt x$. The cofactor border contributes $O(L_2^2/L)$ as in the previous polynomial deletion: all the cutoffs there are polylogarithmic and only 1 can enter the signed primitives on this rough support. The same proof gives a reciprocal majorant $O((L_2/L)(L_2/U_0)(1+L/U_0))$ for $M_\le$ independently of parity. Its two signed labels $b,c<H_0/D$ are now 1; write $h\mid k$ or $h=pr$, $r\mid k$, and use the short log range in $h$ or $k/r=x/h$ respectively. The long label complementary to either has harmonic rough cost $O(1+L/U_0)$. The centered factor supplies $L_2/L$. Also $k/\varphi(k)\ll1$ on this rough selector. It remains to bound $F_0F_1$ above the border.

## 2. Rough signed energies with an outer log-band estimate

For $U_0\le U\le L^{3/4}$ set $G=\exp U$. Allow real $G$ with the mask defined by all primes $\le G$. For any log interval of width $H$, the reciprocal sum on nonunit $G$-rough integers is $O(H/U+(1+H)e^{-3U/4})$, as proved in the earlier rough count. Allowing 1 adds at most one. In particular on any interval of log width $U$ the sum, with or without 1, is $O(1)$.

For a squarefree rough integer $e\le Z$, the reciprocal Möbius primitive $R_{G,e}(u)$ also excludes prime divisors of $e$ and is zero below zero. Uniformly in the present ranges the exponential moment at $1/U$ of its positive mask kernel is $O(U)$. Indeed the excluded primes up to $G$ have this moment by the Euler product comparison in the least-prime-conditioned proof. The extra primes of $e$ have logarithmic contribution $O((\log Z/U)e^{1-U})=o(1)$ since $U\ge U_0\gg L_2$ and $\log Z\ll L$. Splitting the shifted ordinary reciprocal Mertens primitive at $u/2$ therefore gives

$$
 |R_{G,e}(u)|\ll
 \min\left(1+u/U,\ U\left(e^{-c\sqrt u}+e^{-u/(2U)}\right)\right)
 \qquad(u\ge0).
 \tag{4}
$$

The first bound follows from the unsigned rough harmonic estimate, with its error absorbed in $1+u/U$; the second is the shifted mask bound. Strict primitives satisfy the same estimates, since a jump at $u$ is at most $e^{-u}$.

Consider the signed rough LCM energy

$$
 \mathcal E_G(f)=\sum_{r,t\ {\rm rough}}
             \frac{\mu(r)\mu(t)f(r)f(t)}{[r,t]}
 =\sum_{\substack{e\le Z\\e\ {\rm rough}}}
       \frac{\varphi(e)\mu(e)^2}{e^2}
       \left|\sum_{\substack{d\ {\rm rough}\\(d,e)=1}}
                   \frac{\mu(d)}d f(ed)\right|^2
 \tag{5}
$$

for real cutoff weights supported at $r\le Z$. This is the exact gcd expansion. For an upper cutoff with log height $t$, divide the outer variable by bands $jU\le t-\log e<(j+1)U$, $j\ge0$. Each band has rough reciprocal mass $O(1)$ by the log count above, rather than the unpartitioned total $O(1+L/U)$. It follows from (4) that the aggregate contribution from $j>C_A(1+\log U)$ is $O_A(U^{-A})$ for any fixed $A$, in each of the following three cases: a primitive at log height $t$, a difference with endpoints at log distance at most $W<U$, and an integral over the interval from $t-U$ to $t$. In the latter cases for $j\ge2$ use (4) on arguments at least $(j-1)U$. The largest possible outer tail is bounded by a constant times

$$
 U^4\sum_{j>C_A(1+\log U)}
          \left(e^{-2c\sqrt{(j-1)U}}+e^{-(j-1)}\right),
 \tag{6}
$$

using the length factor $U$ for the integral. This is $O_A(U^{-A})$ since the second sum is geometric and the first is bounded by its first term plus the integral under the substitution $y=\sqrt{(j-1)U}$. This supplies the uniform tail without taking a near window as large as $U L_2$.

Write $V_U=1+\log U$. The near bands have total rough harmonic mass $O_A(V_U)$. For a primitive at a fixed threshold $T\le Z$ the inner sum in (5) is $O_A(V_U)$ there. For a shifted integrated difference with $f(r)=(\log(T/r))_+-(\log(T/(Gr)))_+$, it is an integral of length $U$ and costs $O_A(UV_U)$. Consequently

$$
 \mathcal E_G(\mathbf1_{r\le T})\ll V_U^3,\qquad
 \mathcal E_G\big((\log(T/r))_+-(\log(T/(Gr)))_+\big)
                  \ll U^2 V_U^3 .
 \tag{7}
$$

The first bound also applies to strict cutoffs. For a signed shell of log width at most $W$, the nonunit reciprocal terms of the inner sum in (5) cost $O(W/U)$, with rough $e$ in the near bands of mass $O_A(V_U)$. The unit term is supported on $e$ in the shell itself. Its rough reciprocal mass is $O(W/U)$ when the shell excludes 1, or $O(1+W/U)$ otherwise. Thus the signed shell energy is

$$
 O\!\left(W/U+V_U(W/U)^2\right)=O(W/U)
        \quad\text{if it excludes 1},
 \qquad O(1)\quad\text{otherwise}.
 \tag{8}
$$

Here $U\ge U_0$ makes $U/(W V_U)$ grow uniformly, and (6) with a fixed large $A$ covers the far terms.

For the unsigned boundary shells of width $O(\eta)$ use the same elementary split $r=ea,t=eb$, $e=(r,t)$. If exactly one of $a,b$ is 1 then the ratio contradicts $U\gg\eta$. Both units give a diagonal $O(\eta/U)$ if the shell excludes 1 and $O(1)$ otherwise. Both nonunits cost $O((\eta/U)^2(1+L/U))$ after summing over rough $e\le Z$. This is $O(W/U)$ in the first case and $O(1)$ in the second. We used $e^{-3U/4}\ll\eta/U$ from $U\ge U_0\gg L_2$. Exact cutoff endpoints are thereby included.

The rough trace transfer for these energies is unchanged. On $K<k\le K'$ or $K/\ell<v\le K'/\ell$, where $\ell\le\exp(L^{3/4})$ and the log width is $w=\log(K'/K)$, the reciprocal count of multiples of a fixed rough LCM has main coefficient $w\prod_{q\le G,\ q\ {\rm prime}}(1-1/q)/[r,t]$. Use Bonferroni depth $\asymp L_2^2$, so $G^{O(L_2^2)}=N^{o(1)}$, and the individual reciprocal floors cost $N^{-1/2+o(1)}$ uniformly. The product coefficient is $O(w/U)$. For coefficients $O(L)$ and labels at most $Z$ the errors after taking a square are $O_A(wL^{-A}+N^{-1/2+2\delta+o(1)})$, on taking deeper fixed log savings in the single count. As before, the approximate count transfers the **signed** main energy first and only the errors are summed absolutely. This is the only use of a signed-square comparison on the rough cell.

## 3. Use the sector where the shifted shell can meet 1

For odd total parity we can apply (7) directly with $G=G_0$ and no least-prime extraction. For a moving $F_0$ use the fixed signed primitives and the unsigned boundary counts, with the reciprocal square main bound $O(w V_{U_0}^3/U_0)$. The difference of integrals in (3) is supported on a common log bracket of width $O(W)$ over a cell pair. Cauchy in the bracket and the fixed primitive bound give $O(w W^2 V_{U_0}^3/(L^2 U_0))$ for the reciprocal square of a majorant for $F_1$, including the $a(x)F_0$ term. After Cauchy in the arithmetic cell and summing widths $O(L)$, the reciprocal product main bound is $O(W V_{U_0}^3/U_0)$. For this direct use $U=U_0$ is in the permitted range.

For even total parity the already proved polynomial largest-prime deletion covers $P^-(k)>\exp(L^{3/4})$ with the power-log saving there. On the remaining actual least primes $\ell=P^-(k)$, $\exp(U_0)<\ell\le\exp(L^{3/4})$, write $k=\ell v$. Then $v$ is strictly $\ell$-rough (including exclusion of $\ell$ itself), since $k$ is squarefree. Use $G=\ell$, $U=\log\ell$ in the preceding energies. The exact identities $S_k(T)=S_v(T)-S_v(T/\ell)$ and $J_k(T)=J_v(T)-J_v(T/\ell)$ also hold with the strict endpoints where applicable. Thus $F_0$ is the difference of two signed shells on $v$, with the second shell's endpoints divided by $\ell$. The new integrated components in $F_1$ are shifted differences of the type (7).

Fix a physical cell $x_-\le x\le x_+$ and a least prime $\ell$. Mark an arithmetic cell exceptional for the unit if the common hull of all possible **shifted** endpoints includes 1. Since the unshifted endpoints satisfy $T_2\ge5$ above the border, their hull avoids 1. For a marked arithmetic cell, $K\le\ell x_+/D$ and $K'\ge\ell D$, so it intersects $[\ell D,\ell x_+/D]$ and the total log width of all marked cells is $O(W)$, including the endpoint cells. This count does not depend on the size of $\ell$. In the unmarked arithmetic cells both shell envelopes (the fixed signed shell plus its two unsigned boundary brackets) exclude 1. This includes a shell lying entirely below 1, where there is no divisor contribution.

On the rough $v$ cell, (8) and the boundary estimates give main squared reciprocal bounds $O(w W/U^2)$ on the unmarked and $O(w/U)$ on the marked cells for $F_0$. The shifted integrated differences have squared reciprocal main bound $O(w U V_U^3)$ by (7). To allow moving endpoints, freeze $T=T_j$ in its bracket and bound the change in $J_v(T)-J_v(T/\ell)$ by the integrals of $|S_v|$ on the two fixed endpoint brackets of width $O(\eta)$. The primitive bound in (7) and Cauchy on the brackets give main squared reciprocal error $O(\eta^2 w V_U^3/U)$, which is absorbed. Consequently the $F_1$ squared reciprocal main bound is $O(w U V_U^3/L^2)$ in both cases by (3), including the term $a(x)F_0$. Using these positive majorants in Cauchy on the arithmetic cell, and $1/k=1/(\ell v)$, gives main reciprocal products

$$
 \frac{w}{\ell L}\,\sqrt{W/U}\,V_U^{3/2}
        \quad\hbox{unmarked};\qquad
 \frac{w}{\ell L}\,V_U^{3/2}
        \quad\hbox{marked}.
 \tag{9}
$$

The square floor terms from the rough transfer, including the two moving brackets, yield $N^{-1/4+\delta+o(1)}/\ell$ per cell after Cauchy. Their sum is still power-small; the number of cells is polylogarithmic and the reciprocal sum over the selected primes is $O(L_2)$. We used the $wL^{-A}$ terms with fixed $A$ large enough to be absorbed by the displayed main bounds, including arbitrary short cells.

On the marked cells, summing widths $O(W)$ per least prime gives $O(W L_2^{5/2}/L)$ after summing primes, using $V_U\ll L_2$. On the unmarked cells, summing widths $O(L)$ and then primes gives

$$
 \sqrt W\sum_{\ell>\exp(U_0)}
       \frac{(1+\log\log\ell)^{3/2}}{\ell\sqrt{\log\ell}}
     \ll \sqrt{W/U_0}\,(1+\log U_0)^{3/2}.
 \tag{10}
$$

For the last step use dyadic bins in $\log\ell$, on each of which the prime reciprocal mass is $O(1)$ by Mertens, and sum the geometric factor $(\log\ell)^{-1/2}$. This is why a unit present in the shifted shell is not allowed to recur at full log width for each least prime.

By (1), $W=O_B(L_2)$ and $V_{U_0}\asymp1+\log L_2$, so (10) is $O((1+\log L_2)^{-\varepsilon/2})$. The direct odd bound is $O((1+\log L_2)^{-\varepsilon})$. The marked bound, the previously treated larger least primes, and all border, prime-$k$ and low mixed terms are smaller. The inequalities bound the original coefficients, not a new right polynomial.

Finally, the genuine full two-prime sieve and conditional major transfer apply exactly as in the polynomial largest-prime proof: the cofactor and prime ranges are unchanged, and the present least-prime splitting affects upper estimates only. At fixed $k$ all rough and parity masks depend only on $k$; the actual $p$ interval and weight retain their original variation $O(\tau_4(k))$. Thus the right prime AP error stays $O_\epsilon(Q^2N^{3/4+\delta/2+\epsilon})$ pointwise on the arcs, and the same completed local factors, tails, and sieve floors apply. These are within $N^{1-c_\delta}$ as there. Multiply the reciprocal majorant by the left log and the two-prime count for the full coefficient; for the actual major density use its $1/[k\log(x/k)]$ factor and $O(\Sigma(N)k/\varphi(k))$ local factor. Subtract the actual major from the full coefficient to obtain (2). No arcs or coefficients outside the specified selector were estimated.
