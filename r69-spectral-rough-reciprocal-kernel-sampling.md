# Sampling one masked Möbius kernel lowers the true rough-partner gate

**Scope.** In the [polynomial largest-prime mixed deletion](r68-spectral-polynomial-largest-near-polylog-roughness.md), the genuine least-prime gate can be moved arbitrarily close to fixed polylogarithmic size from above. Write $L=\log N$, $L_2=1+\log L$. Fix $0<\delta<1/4$ and the earlier cutoff constants $B>B_0>0$. For a sufficiently large constant $C_0=C_0(B,B_0)$, take any real

$$
 C_0L_2\le U_0\le L^{3/4}.
 \tag{1}
$$

On actual squarefree partners with $P^+(m)>N^{1/2-\delta}$ and $P^-(m)>\exp(U_0)$, both parities have relative upper bound $O(\sqrt{L_2/U_0})$ in the original Hardy normalization, and odd total parity has bound $O(L_2/U_0)$. Thus the normalized error is $o(\Sigma(N))$ whenever $U_0/L_2\to\infty$, arbitrarily slowly. A fixed sufficiently large gate $P^-(m)>L^C$ gives a quantitative bound $O(C^{-1/2})$ (odd: $O(C^{-1})$), not a little-oh claim at fixed $C$.

Let $A(m)$ be the actual above-BV mixed coefficient $M_>(m)$ with these gates, also restricted to $m\in V=[N/3,2N]$ and optionally to one parity. Keep $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, $Q=N^{1/1000}$, the genuine hard central $I$, bounded-variation weight $\omega$, and prime polynomial $P_{I,\omega}$. With $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$, put $c_\delta=\min(10^{-4},(1/4-\delta)/4)$ and $\mathcal B_{\rm all}=\sqrt{L_2/U_0}$, $\mathcal B_{\rm odd}=L_2/U_0$. Then

$$
 \begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
     &\ll \Sigma(N)|I|\mathcal B/L+N^{1-c_\delta},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)e(-N\theta)\,d\theta\right|
     &\ll \Sigma(N)|I|\mathcal B/L+N^{1-c_\delta}.
 \end{split}
 \tag{2}
$$

Here $\mathcal B=\mathcal B_{\rm odd}$ on odd total parity and $\mathcal B_{\rm all}$ otherwise; implicit constants are uniform in $U_0$ in (1). The first line is unconditional. The second uses the same historical prime-progression Dirichlet GRH inputs at $q\le Q$ as before, not a Möbius-progression estimate. Neither line controls complementary partners or the full Hardy profile.

## 1. Sample one reciprocal kernel, including the extra gcd masks

Let $C_0L_2\le U\le L^{9/10}$, $G=\exp U$, $Z=10N^\delta L^B$. Call an integer $G$-rough if it has no prime factor $\le G$; 1 is permitted unless otherwise stated. On any log interval of width $H$ the reciprocal mass of nonunit rough integers is

$$
 O\bigl(H/U+(1+H)e^{-3U/4}\bigr).
 \tag{3}
$$

This is the [previous rough sieve bound](r68-spectral-least-prime-conditioned-mixed-minor.md), by partitioning into segments of log width at most one after excluding the region below $G$. It includes endpoint changes. On log unit intervals the nonunit mass is $O(1/U)$, and the complete rough harmonic mass up to $Z$ is $O(1+L/U)$.

Write $R(u)=\sum_{d\le\exp(u)}\mu(d)/d$ for the ordinary reciprocal Möbius primitive, zero for $u<0$. Use the ordinary reciprocal Mertens estimate from the least-prime-conditioned proof, $|R(u)|\ll\exp(-c\sqrt u)$ for $u\ge0$. The weak and strict primitives both satisfy

$$
 \sum_{j\ge0}\sup_{j\le u\le j+1}|R(u)|\ll1 .
 \tag{4}
$$

Indeed changing an endpoint at $u$ costs at most $\exp(-u)$, including the harmless unit jump at zero.

Let $R_G(u)$ be the same primitive restricted to rough $d$, and let $R_{G,e}$ additionally omit prime divisors of a rough integer $e$. [Tao's Theorem 1.1](https://arxiv.org/pdf/0908.4323#page=3), also written in coprimality form as equation (9), gives $|R_G|,|R_{G,e}|\le1$ for every allowed prime set and threshold. Strict versions follow by limits. This uses the uniform finite partial-sum bound, not a nonuniform convergence assertion.

The exact positive convolution for the excluded primes $p\le G$ is

$$
 R_G(u)=\sum_{\substack{a\ge1\\P^+(a)\le G}}\frac{R(u-\log a)}a
 \tag{5}
$$

including $a=1$, with the same endpoint convention on both sides. The full mass of the convolution is $\prod_{p\le G}(1-1/p)^{-1}\ll U$. For any real shift $t$ and fixed $a$, use (3) on unit log bins in $u=t-\log a-\log j$ for nonunit rough $j$, and then (4). This gives
$\sum_{j>1,\ j\ {\rm rough}} |R(t-\log a-\log j)|/j\ll1/U$ independently of both $t$ and $a$. Summing the positive weights in (5) costs $O(U)$, while the term $j=1$ has $|R_G(t)|\le1$. Consequently

$$
 \sup_{t\in\mathbb R}\sum_{j\ {\rm rough}}\frac{|R_G(t-\log j)|}{j}\ll1.
 \tag{6}
$$

The same estimate holds for the strict version, uniformly.

For the extra gcd mask, the exact second positive convolution is
$R_{G,e}(u)=\sum_{\operatorname{rad}(a)\mid e}R_G(u-\log a)/a$,
where $\operatorname{rad}(a)$ is the product of the distinct primes of $a$. If $e$ is rough then the $a$ in this convolution are also rough. After taking absolute values and interchanging the positive sums, put $e=\operatorname{rad}(a)j$ and enlarge to all rough $j$. By (6) the inner $e$-sum is $O(1/\operatorname{rad}(a))$, uniformly in the translated argument. Since
$\sum_{a\ge1}1/(a\,\operatorname{rad}(a))=\prod_p(1+1/(p(p-1)))<\infty$, this proves the exact masked sampling estimate

$$
 \sup_{t\in\mathbb R}
  \sum_{e\ {\rm rough}}\frac{|R_{G,e}(t-\log e)|}{e}\ll1.
 \tag{7}
$$

No truncation depending on $e$ or uniform decay in the additional mask is required. One may restrict $e$ to squarefree integers at any point on this positive side.

## 2. Three signed LCM energies

For real cutoff weights $f$ supported on $r\le Z$, the signed LCM energy has the exact nonnegative gcd expansion

$$
 \mathcal E_G(f)=\sum_{r,t\ {\rm rough}}
         \frac{\mu(r)\mu(t)f(r)f(t)}{[r,t]}
 =\sum_{\substack{e\le Z\\e\ {\rm rough}}}
      \frac{\varphi(e)\mu(e)^2}{e^2}
      \left|\sum_{\substack{d\ {\rm rough}\\(d,e)=1}}
                 \frac{\mu(d)}d f(ed)\right|^2 .
 \tag{8}
$$

Here $\varphi(e)/e^2\le1/e$.

**Primitive.** For a cutoff at $T\le Z$ the inner sum in (8) is $R_{G,e}(\log T-\log e)$, weak or strict. Use the pointwise bound 1 for one factor of the square and (7) for the other. This proves

$$
 \mathcal E_G(\mathbf1_{r\le T})\ll 1 ,
 \tag{9}
$$

also with $<$ and with the primitive set to zero below 1.

**Integrated difference.** For $f(r)=(\log(T/r))_+-(\log(T/(\exp(h)r)))_+$, the inner sum is an integral of $R_{G,e}(u)$ from $\log(T/e)-h$ to $\log(T/e)$. This holds for any $h\ge0$, since equality at a cutoff has zero log coefficient when the corresponding log is integrated. Each integral has modulus at most $h$ by Tao's bound. By (7) and Fubini the $1/e$ weighted sum of their moduli is $O(h)$: integrate in the common shift $t$ from $\log T-h$ to $\log T$. Thus

$$
 \mathcal E_G\big((\log(T/r))_+-(\log(T/(\exp(h)r)))_+\big)
                   \ll h^2 .
 \tag{10}
$$

**Narrow shell.** Let $W\ge1$ bound the log width, with $W\le U$. On a shell with upper log height $t$ and width $a\le W$, the inner value in (8) is the difference of two masked primitives at $t-\log e$ and $t-a-\log e$, with the appropriate one-sided values. Its $1/e$ weighted sum in absolute value is $O(1)$ by (7). In the portion where the inner interval does not contain the divisor 1, its absolute value is $O(W/U)$ by (3), since all terms there are rough nonunits, even when keeping an endpoint. In the other portion the inner value is bounded by 2 and $\log e$ must be in the original shell. If the latter excludes 1, the reciprocal mass of such outer $e$ is $O(W/U)$ by (3). Otherwise it is $O(1+W/U)$. Consequently

$$
 \mathcal E_G(\mathbf1_{\log r\in J})
     \ll W/U\quad\text{if }1\text{ is excluded},\qquad
     \ll1\quad\text{otherwise},\qquad |J|\le W\le U.
 \tag{11}
$$

At equal endpoints a possible singleton is handled by the same reciprocal count for the nonunit or unit. Taking $W\ge1$ covers arbitrarily small widths without any floor assumption.

For moving endpoints of log width $O(\eta)$, $\eta=L^{-1/2}$, the [previous unsigned boundary-shell estimate](r68-spectral-polynomial-largest-near-polylog-roughness.md) still applies. In its decomposition $r=ea,t=eb$, $e=(r,t)$, the nonunit-pair term is $O((\eta/U)^2(1+L/U))$, as $e^{-3U/4}\ll\eta/U$ for $C_0$ large. The diagonal is $O(\eta/U)$ if the shell excludes 1, and $O(1)$ otherwise. This is $O(W/U)$ and $O(1)$, respectively, and includes possible exact endpoint integers.

## 3. True reciprocal cell trace and the original parity factors

Use the cells and exact factors of the near-polylog proof. Thus $m=pk$ with actual largest $p>\max(P^+(k),N^{1/2-\delta})$, $D<k\le 2N^{1/2+\delta}$, $T_1=k/D$, $T_2=Dk/x$, $x=kp$, and $W=C_B L_2$ bounds their log separation plus endpoint uncertainty on the cells. The lower gate in (1) makes $U\ge W$ in (11). On the arithmetic border $k\le10DL^{2B}$ only the unit can enter the cutoffs; its total product reciprocal cost is $O(L_2^2/L)$. The genuine prime $k$ has $D<k<\sqrt x$, hence cost $O(L_2/L)$. Above the border $T_2\ge5$. The remaining $-\Xi_D$ on composite squarefree partners is the sharp product $F_0F_1$, with

$$
 F_0=-\mu(k)S_k(T_1^-)-S_k(T_2),\qquad
 F_1=a(x)F_0+\frac{2}{\log x}\{\mu(k)J_k(T_1)-J_k(T_2)\},
 \quad a(x)=O(W/L).
 \tag{12}
$$

The original identity $M_>=-\Xi_D-M_\le$ is unchanged.

For a hard arithmetic cell $K<k\le K'$, log width $w$, reciprocal rough counts on $k$ or on $v=k/\ell$ have the same signed-square transfer as before. In the latter case $\ell\le\exp(L^{9/10})$ so $K/\ell=N^{1/2-o(1)}$ or larger. Bonferroni depth $\asymp L_2^2$ still has $G^{O(L_2^2)}=N^{o(1)}$ throughout $U\le L^{9/10}$. For divisor labels $\le Z$ and coefficients $O(L)$ the reciprocal square is bounded by $O(w/U)$ times its nonnegative signed energy plus

$$
 O_A(wL^{-A}+N^{-1/2+2\delta+o(1)})
 \tag{13}
$$

for each fixed $A$. This follows by first taking the exact completed signed main term $w\prod_{q\le G,\ q\ {\rm prime}}(1-1/q)\mathcal E_G$, then bounding the floor from at most $Z^2$ label pairs and the Bonferroni tail as in the near-polylog proof. The same applies to the unsigned boundary energy. Thus (9)–(11) do not assert anything about a synthetic sequence of cofactors. Error terms $wL^{-A}$ will be absorbed in the main squares with a fixed sufficiently large $A$, and the power floors stay $N^{-1/4+\delta+o(1)}$ after Cauchy and all cells (with $1/\ell$ for a least-prime class).

**Odd total parity.** Here $\mu(k)=+1$. Use the rough mask directly with $U=U_0$. Equation (9) and the unsigned boundary envelopes give a moving $F_0$ squared reciprocal mean $O(w/U_0)$ plus floors. The integrated difference in (12) is supported inside a common width $O(W)$ in the log variable for the cell pair. Bound its absolute value by the integral of $|S_k|$ there and use Cauchy in the bracket and (9). Thus the $F_1$ square has main bound $O(w W^2/(L^2U_0))$, including the $a(x)$ term. Their product reciprocal bound is $O(w W/(L U_0))$. Summing arithmetic widths $O(L)$ gives $O(W/U_0)$.

**Even total parity.** Here $\mu(k)=-1$. For $P^-(k)>\exp(L^{9/10})$ retain the absolute majorant of the [polynomial rough deletion](r68-spectral-polynomial-largest-rough-mixed-minor.md) with $\beta=9/10$, on the unchanged polynomial largest-prime gate. Its relative cost $O(L^{-2/5}\sqrt{L_2}+L_2^4/L^{9/10}+L_2^2/L)$ is $O(\sqrt{L_2/U_0})$ uniformly for (1). For the remaining true least prime $\ell\in(\exp(U_0),\exp(L^{9/10})]$ write $k=\ell v$ with strictly $\ell$-rough $v$. Put $G=\ell$ and $U=\log\ell$. The exact primitive switch $S_k(T)=S_v(T)-S_v(T/\ell)$ is valid with either joint endpoint convention, and the analogous integrated switch holds. Thus $F_0$ is the difference of signed open shells $T_2<r<T_1$ and $T_2/\ell<r<T_1/\ell$ on $v$. The unshifted shell cannot contain 1. For a fixed physical cell $[x_-,x_+]$ and fixed $\ell$, the shifted hull can meet 1 only on arithmetic cells intersecting $[\ell D,\ell x_+/D]$, of total log width $O(W)$ including endpoint cells. Call only these cells marked.

Freeze the shell endpoints and dominate the change by their unsigned boundary brackets. By (11) and (13) the $F_0$ squared reciprocal means on $v$ are $O(wW/U^2)$ unmarked and $O(w/U)$ marked. By (10) and (13) each fixed integrated difference $J_v(T_j)-J_v(T_j/\ell)$ has squared mean $O(wU)$. Its moving change is bounded by two integrals of $|S_v|$ on log brackets of width $O(\eta)$, whose squared mean is $O(\eta^2w/U)$ by (9) and Cauchy inside each bracket, apart from floors. It follows from (12) that the $F_1$ square is $O(wU/L^2)$, including the $a(x)F_0$ term. Cauchy on the arithmetic cell and $1/k=1/(\ell v)$ give product reciprocal bounds $O(w\sqrt{W/U}/(\ell L))$ off marked cells and $O(w/(\ell L))$ on marked cells. Their total, using widths $O(L)$ off and $O(W)$ on per $\ell$, is

$$
 \ll \sqrt W\sum_{\ell>\exp(U_0)}
             \frac1{\ell\sqrt{\log\ell}}
        +\frac{W}{L}\sum_{\ell\le\exp(L^{9/10})}\frac1\ell
 \ll \sqrt{W/U_0}+W L_2/L .
 \tag{14}
$$

All $\ell$ sums here are over primes. For the first, dyadic bins in $\log\ell$ have prime reciprocal mass $O(1)$ by Mertens, and the geometric bound for $(\log\ell)^{-1/2}$ is summable. The power floors in (13) are summed with $1/\ell$, so no large additive loss occurs.

The true low mixed $M_\le$ has $b=c=1$ because its signed labels are below $H_0/D<\exp(U_0)$. Exactly as in the preceding deletion its reciprocal majorant is $O((W/L)(W/U_0)(1+L/U_0))$, by a rough harmonic sum on the short log shell in $h$, or in $k/r=x/h$ if $h=pr$. This, the border, and the prime-$k$ cost all fit the displayed relative rates uniformly in (1). Also $k/\varphi(k)\ll1$ on the retained rough support.

Finally apply the genuine two-prime upper sieve and conditional major transfer of the polynomial rough deletion. For fixed $k$, no arithmetic upper envelope replaces the actual weight or changes its variation $O(\tau_4(k))$. All selectors are fixed in $k$ apart from the original hard $p,x$ gates. The arithmetic floor $N^{3/4+\delta+o(1)}$ and the prime AP pointwise major polynomial error $O_\epsilon(Q^2N^{3/4+\delta/2+\epsilon})$ are unchanged. The rough reciprocal product bounds control both the full two-prime count and the completed major density with its $1/[k\log(x/k)]$ denominator and its actual local factor $O(\Sigma(N)k/\varphi(k))$ on unit cofactors. The left hard intervals in the physical cells sum to $|I|$; all previous completion errors and the new tuple floors fit $N^{1-c_\delta}$. Subtract the genuine major integral from the full sum for the second line of (2). For the final fixed-polylogarithmic interpretation take $U_0=C\log L$ for fixed sufficiently large $C$, using (1) eventually. No smallness at fixed $C$ beyond the stated quantitative dependence is implied.
