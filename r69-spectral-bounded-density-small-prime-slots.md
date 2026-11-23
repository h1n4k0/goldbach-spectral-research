# The genuine mixed minor with a growing count of small prime factors

**Scope.** This treats genuine partners that do not pass a least-prime gate: their least prime may be fixed. Retain the polynomial largest-prime condition $P^+(m)>N^{1/2-\delta}$, fixed $0<\delta<1/4$. Write $L=\log N$, $L_2=1+\log L$, and choose

$$
 U=L^{1/2},\qquad G=\exp U,\qquad r_*=\lfloor L_2/100\rfloor .
 \tag{1}
$$

Both squarefree Möbius parities can be deleted at $o(\Sigma(N))$ in the original Hardy normalization when $m$ has at most $r_*$ distinct prime factors $\le G$. The prime locations below $G$ are not individually restricted. In particular this includes every fixed finite small-prime count as $N$ grows, but not typical or arbitrary higher counts. No assertion is made on the remaining partners or on weak S.

Keep the genuine above-BV mixed coefficient $M_>(m)$, the earlier constants $B>B_0>0$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, $V=[N/3,2N]$, the genuine left interval $I$ and bounded-variation weight $\omega$, and the same major arcs with $Q=N^{1/1000}$, as in the [polynomial largest-prime model](r68-spectral-polynomial-largest-rough-mixed-minor.md). Let $A(m)$ be $M_>(m)$ on squarefree partners $m\in V$ satisfying (1)'s count and the largest-prime condition, optionally restricted to one parity. Put $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$, $c_\delta=\min(10^{-4},(1/4-\delta)/4)$ and

$$
 \mathcal B_{\rm all}=L^{-1/5},\qquad
 \mathcal B_{\rm odd}=L^{-2/5}.
 \tag{2}
$$

Then uniformly in every even $N$ and the hard left interval,

$$
\begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
  &\ll \Sigma(N)|I|\,\mathcal B/L + N^{1-c_\delta},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)
                         e(-N\theta)\,d\theta\right|
  &\ll \Sigma(N)|I|\,\mathcal B/L + N^{1-c_\delta}.
\end{split}
 \tag{3}
$$

Here $\mathcal B=\mathcal B_{\rm odd}$ on odd total parity and $\mathcal B_{\rm all}$ otherwise. The full upper bound is unconditional; the second line uses the same historical Dirichlet GRH estimates for the two prime progression sums at $q\le Q$, not a Möbius progression estimate. The factor $L/N$ in the original normalization then gives the stated deletion.

## 1. Exact small-factor extraction and harmonic bookkeeping

Write $m=pk$ with the true largest prime $p>\max(P^+(k),N^{1/2-\delta})$. Since $p>G$, the small primes of $m$ are exactly the small primes of $k$. On actual squarefree support there is a unique factorization

$$
 k=bv,\qquad b=\prod_{\substack{\ell\mid k\\\ell\le G,\ \ell\ {\rm prime}}}\ell,
     \qquad P^-(v)>G,\qquad t=\omega(b)\le r_* .
 \tag{4}
$$

Here $\omega(b)$ counts distinct primes and is distinct from the left weight $\omega(n)$. At a fixed $b$, the rough condition on $v$ is literal. An interval $K<k\le K'$ of log width $w$ becomes $K/b<v\le K'/b$ with the same width and $1/k=1/(bv)$. Since $b\le G^{r_*}=N^{o(1)}$, all such cells with $K\ge D$ have $K/b\ge N^{1/2-o(1)}$. The actual $t=0$ term, $b=1$, is already covered by the [common reciprocal kernel estimate](r69-spectral-rough-reciprocal-kernel-sampling.md) at $U_0=U$, with costs $O(\sqrt{L_2/U})$ and $O(L_2/U)$, respectively.

For $t\ge1$, put $\ell=P^-(b)$, $a=\log\ell$, and set

$$
 \mathcal H_t=\sum_{\substack{b\ {\rm sf}\\\omega(b)=t,\ P^+(b)\le G}}\frac1b,
 \qquad
 A_t=\sum_{\substack{b\ {\rm sf}\\\omega(b)=t,\ P^+(b)\le G}}\frac{\log P^-(b)}b.
$$

Mertens gives $\mathcal H_t\le (\sum_{\ell\le G,\ \ell\ {\rm prime}}1/\ell)^t/t!\le L_2^t/t!$ for large $N$. Importantly,

$$
 A_t\ll U
 \tag{5}
$$

with an absolute constant uniform in $t\ge1$: integrate the indicator that every prime of $b$ exceeds $e^z$ over $0<z<U$. The inner product sum is at most $(C+\log(U/z))^t/t!$ for an absolute $C\ge1$, by Mertens with bounded error at both endpoints; for $z<1$ the same upper bound follows by enlarging the full sum. Substituting $z=Ue^{-u}$, the integral is at most $U e^C \int_0^\infty v^t e^{-v}\,dv/t!=Ue^C$. This avoids multiplying the main bound by $\mathcal H_t$. We will also need the crude uniform estimate

$$
 \sum_{0\le t\le r_*}6^t \mathcal H_t\ll L^{1/10}
 \tag{6}
$$

where $\mathcal H_0=1$. Indeed $(6L_2)^t/t!$ increases up to $r_*$, and the sum is at most $(1+r_*)(6eL_2/r_*)^{r_*}$ for $r_*\ge1$. For large $N$, $L_2/200\le r_*\le L_2/100$, giving exponent $(\log(1200e))/100<.082$ before the factor $1+r_*$. These bounds are over positive auxiliary harmonic sums, not a change of the actual partner mask.

## 2. Sharp product and the genuine rough energy below its cutoffs

Use the exact decomposition $M_>=-\Xi_D-M_\le$. As in the preceding proofs only $D<k\le2N^{1/2+\delta}$ contributes. Set $Z=10N^\delta L^B$, $T_1=k/D$, $T_2=Dk/x$, $x=pk$, and use the same hard geometric physical and arithmetic cells with log width $O(\eta)$, $\eta=L^{-1/2}$. Let $W=C_B L_2$ bound the log distance of $T_1,T_2$ and their moving endpoint uncertainty. Both cutoffs lie below $Z$. For composite squarefree $k$ the true $-\Xi_D$ is the sharp product $F_0F_1$, with

$$
 F_0=-\mu(k)S_k(T_1^-)-S_k(T_2),\qquad
 F_1=a(x)F_0+\frac2{\log x}(\mu(k)J_k(T_1)-J_k(T_2)),
 \quad a(x)=O(W/L).
 \tag{7}
$$

Here $S_k(T)=\sum_{d\mid k,\ d\le T}\mu(d)$, $J_k(T)=\int_1^T S_k(z)\,dz/z$, both zero below 1. The threshold $T_1$ in the first term of $F_0$ is strict and $T_2$ weak. The arithmetic border $k\le10DL^{2B}$ has only polylogarithmic cutoffs; every divisor there is a divisor of $b$, since $v$ is rough. Thus there are at most $2^{r_*}$ terms in each divisor primitive or integrated sum, the integrated weights in (7) are $O(W/L)$, and the border contributes $O(4^{r_*}W^2/L)$ in reciprocal product using the total log width $O(W)$. Prime $k$ forces $D<k<\sqrt x$ and contributes $O(L_2/L)$; it is in the $t=0$ class eventually. Above the border $T_2\ge5$.

For all real $T$ the exact identities are

$$
 S_k(T)=\sum_{d\mid b}\mu(d)S_v(T/d),\qquad
 J_k(T)=\sum_{d\mid b}\mu(d)J_v(T/d).
 \tag{8}
$$

The corresponding strict primitive identity also holds. Splitting off the least prime $\ell$ of $b$ in one of these sums introduces the actual difference between arguments $T/d$ and $T/(d\ell)$ for $d\mid b/\ell$, of log length $a=\log\ell$. There is no enlargement of the coefficient by inserting a formal factor on non-squarefree integers.

We use the [signed rough LCM energies](r69-spectral-rough-reciprocal-kernel-sampling.md) on the true rough $v$ cell: energy $O(1)$ for a signed primitive, $O(a^2)$ for a signed integrated difference of length $a$, and $O(H/U)$ for a signed shell of log width at most $H$, excluding 1, for $1\le H\le U$. If a shell contains 1 the cost is $O(1)$. In particular the length-$a$ shell may use $H=\max(1,a)\ll a$ since $\ell\ge2$. The corresponding actual rough reciprocal square has main bound $O(w/U)$ times the energy. The Bonferroni floor with divisor labels at most $Z$ is $O_A(wL^{-A}+N^{-1/2+2\delta+o(1)})$ after summing label pairs, uniformly on $K/b<v\le K'/b$ by $b=N^{o(1)}$ and $G^{O(L_2^2)}=N^{o(1)}$. For moving sharp shell endpoints add the old unsigned boundary counts of width $O(\eta)$, with energy $O(H/U)$ excluding 1 and $O(1)$ otherwise. Any exact endpoint integer lies in these boundary envelopes. For a moving integrated difference, freezing its two endpoints costs two bracket integrals of $|S_v|$ of log width $O(\eta)$, so by the primitive energy the square of its error has main bound $O(\eta^2w/U)$ by Cauchy. These envelopes are uniform in $x$ on its physical cell.

In using these bounds for multiple translates in (8), the triangle inequality in the weighted arithmetic $L^2$ norm gives a factor at most $2^t$ in a square root. In the square itself it is at most $4^t$. Positive squares can be enlarged from the true squarefree and parity selected $v$ to all rough $v$, but the original coefficient and its Fourier polynomial are not changed. In the estimates below we only display the main reciprocal terms: the fixed-$A$ log errors can be absorbed, the post-Cauchy power floor per cell and $b$ being $N^{-1/4+\delta+o(1)}/b$. The number of cells is polylogarithmic, $4^t$ is polylogarithmic, and the full $1/b$ sum is at most $\prod_{\ell\le G,\ \ell\ {\rm prime}}(1+1/\ell)\ll U$. Thus all aggregated floors retain the same power saving.

## 3. Where an actual unit can enter a shifted shell

Fix a physical cell $[x_-,x_+]$ and a small-factor product $b$ with $t\ge1$. For even total parity $\mu(m)=+1$ one has $\mu(k)=-1$, so $F_0$ is the signed open shell between $T_2,T_1$. Under the divisor switch in (8) it is a sum of translates divided by $d\mid b$. Mark an arithmetic cell if the full hull of any translated endpoints can contain 1. For a particular $d$ this forces $K\le d x_+/D$, $K'\ge dD$, so the cell intersects $[dD,d x_+/D]$ of log width $O(W)$. Over all $d$ the marked cells have total log width $O(2^t W)$, including the endpoint cells. Off this union every translated shell and its two moving boundary brackets exclude 1.

Use (8) with the least-prime switch for each $J_k(T_j)$ in (7). The squared reciprocal bound for its integrated terms on $v$ is $O(4^t w a^2/U)$ because the shift length is $a$ and $\eta\ll a$. The $F_0$ square is $O(4^t wW/U^2)$ off marked cells and $O(4^t w/U)$ on them. Treat $a(x)F_0^2$ separately. Off the marked cells the resulting main reciprocal bound for the product in each cell is

$$
 \ll \frac{4^t w}{bL}
        \left(\frac{a\sqrt W}{U^{3/2}}+\frac{W^2}{U^2}\right).
 \tag{9}
$$

On the marked cells it is $O(4^t w(a+W)/(bL U))$. Summing log widths $O(L)$ off and $O(2^t W)$ on, and then over the $b$ of count $t$ by (5), gives at most

$$
 O\!\left(4^t\sqrt{W/U}+4^t W^2 \mathcal H_t/U^2
             +8^t W/L+8^t W^2 \mathcal H_t/(LU)\right)
 \tag{10}
$$

for this parity.

For odd total parity $\mu(k)=+1$, and use the least-prime switch in every $S_k$ of (7) and in the intermediate integrand of $J_k(T_1)-J_k(T_2)$. For each $d\mid b/\ell$ mark an arithmetic cell if 1 can enter a shell with endpoints $z/(d\ell),z/d$, where $z$ ranges over the full common hull from the minimum $T_2$ to the maximum $T_1$ in the cell pair. This forces the cell to intersect $[dD,d\ell x_+/D]$, hence the total marked log width is $O(2^t(W+a))$ across these $d$. Off the marked cells, the one-sided primitives of $F_0$ after switching are signed shells of log width $a$, each excluding 1, and the same is true for every intermediate integrand just described. The squared reciprocal main term of $F_0$ is $O(4^t w a/U^2)$. Cauchy over the common intermediate log hull of width $O(W)$ gives squared main term $O(4^t w a W^2/(L^2 U^2))$ for $F_1$, including its centered $F_0$ term. On marked cells use the corresponding energy bounds allowing the unit, so these two squared main terms become $O(4^t w/U)$ and $O(4^t wW^2/(L^2U))$. Moving endpoint boundaries are included just as before. The product sums are therefore at most $O(4^t w a W/(bL U^2))$ off marked cells and $O(4^t wW/(bLU))$ on them. Sum widths and then $b$ using (5), obtaining the odd analogue of (10),

$$
 O\!\left(4^t W/U+8^t W/L+8^t W^2 \mathcal H_t/(LU)\right).
 \tag{11}
$$

## 4. Low mixed intervals and transfer to the actual prime minor

In $M_\le$ the LCM $h$ lies in $(D,H_0]$ and both signed divisor labels are strictly below $H_0/D<G$. They must therefore be coprime divisors of $b$; each small prime has at most three assignments to the two labels (absent or in either one), at most $3^t$ signed label pairs. The centered weight is $O(W/L)$. For each $b$ there are two cases. If $h\mid k$, factor $h$ and $k/h$ into their small and rough parts, assigning the $t$ small primes to the two factors in at most $2^t$ ways. The rough part of $h$ is in a log interval of width $O(W)$, away from 1 because $D/b=N^{1/2-o(1)}$ or larger. The other rough part is bounded by $Z$. If $h=pr$ with $r\mid k$, do the same with $k/r=x/h$ and $r$. On a fixed physical cell the former runs in a log interval of width $O(W)$ and its rough part is again away from 1; the rough part of $r$ is at most $Z$. In either case the reciprocal product gives at most

$$
 O\left(\frac{6^t}{b}\frac{W}{L}\frac{W}{U}(1+L/U)\right)
 \tag{12}
$$

on that cell, by the rough harmonic estimates. All enlargements in this step concern the absolute upper weights, not the actual signs. Sum with (6). In these upper estimates the local multiplier $k/\varphi(k)$ is no longer bounded by an absolute constant because of the actual small factors, but the uniform elementary bound $k/\varphi(k)\ll L_2$ suffices.

To collect rates, $W=O(L_2)$, $U=L^{1/2}$, $4^{r_*}\le L^{(\log 4)/100+o(1)}$, and $8^{r_*}\le L^{(\log 8)/100+o(1)}$. For the terms weighted by $\mathcal H_t$ use $\sum_{t\le r_*}4^t\mathcal H_t\ll L^{1/10}$ and $\sum_{t\le r_*}8^t\mathcal H_t\le (4/3)^{r_*}\sum_{t\le r_*}6^t\mathcal H_t\ll L^{.104}$ by (6). Thus the sums of (10), the border, and (12), after multiplication by $k/\varphi(k)\ll L_2$, are $O(L^{-1/5})$. For (11) they are $O(L^{-2/5})$ with the same costs. For example the leading unmarked terms have power exponents $-1/4+(\log4)/100$ and $-1/2+(\log4)/100$, respectively, leaving room for the factor $L_2$ and the number $r_*$ of counts. The $t=0$ term already satisfied both rates.

Finally use the true two-prime upper sieve and conditional prime-AP major transfer of the preceding polynomial argument. For each fixed $k$ the new count mask and parity are constant; all hard $p,x$ support conditions and the actual weight, of variation $O(\tau_4(k))$, are unchanged. The two linear forms on a physical cell are $p,N-kp$, with interval length at most $|I_{\rm cell}|/k$ and the same upper sieve local factor as before. Multiply the reciprocal majorants by $\lambda(n)\le L$ and use the summed arithmetic lengths, which are exactly $|I|$ in the physical variable. The floor $N^{3/4+\delta+o(1)}$ and the power errors from reciprocal floors fit $N^{1-c_\delta}$. For the conditional major, the exact right progression approximation still has error $O_\epsilon(Q^2N^{3/4+\delta/2+\epsilon})$, and the completed density uses the unchanged $1/[k\log(x/k)]$ factor and local bound $O(\Sigma(N)k/\varphi(k))$ on unit cofactors; the old Fourier and Ramanujan completion estimates apply. The upper estimates for the coefficient therefore give the two desired bounds, by subtracting the actual major integral from the genuine full coefficient for the second one. No comparison outside the stated count or largest-prime gates follows.
