# A subpower largest-prime deletion for the genuine above-BV mixed strip

**Scope.** This strengthens the [largest-prime deletion at the original sharp cutoff](r66-spectral-largest-prime-mixed-strip.md). The remaining signed above-BV mixed minor is pointwise small on all squarefree partners whose largest prime exceeds $\sqrt N\exp(-(\log N)^\gamma)$, for every fixed $0<\gamma<1/2$. The new input is a uniform signed Möbius short-cutoff second moment plus a small multiplicative partition that keeps both varying sharp thresholds. The unconditional bound is for the full genuine arithmetic coefficient; the same prime-progression historical Dirichlet GRH input is used only to identify its major and minor portions. This does not estimate the residual with smaller largest prime, the separate sharp-profile minor, the exterior, or Hypothesis S.

Use the notation of the preceding deletion: even $N$, $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ with fixed $B>B_0>0$, $V=[N/3,2N]$, $Q=N^{1/1000}$, and $\mathfrak m$ the same minor arcs. Let $M_>$ be the actual above-$H_0$ mixed coefficient of the squarefree removed strip, signed before its subtraction. For $s=L^\gamma$ put $P_*=\sqrt N e^{-s}$ and $A_*(m)=M_>(m)\mathbf1_{P^+(m)>P_*}$, zero on nonsquarefree $m$ and outside $V$. Use every real half-open central interval $I\subset(N/2,9N/16]$, the genuine prime weight $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$, and any left weight $\omega$ of uniformly bounded supremum and variation, with the same polynomial $P_{I,\omega}$ as in the preceding proof. Then

$$
 \begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A_*(N-n)|
      &\ll_{B,B_0,\gamma}\Sigma(N)|I|\,L^{2\gamma-2}L_2^8+N^{.76},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)
              \widehat A_*(\theta)e(-N\theta)\,d\theta\right|
      &\ll_{B,B_0,\gamma}\Sigma(N)|I|\,L^{2\gamma-2}L_2^8
                              +N^{1-10^{-4}} .
 \end{split}                                                       \tag{1}
$$

The first bound is unconditional and the second uses prime GRH for $q\le Q$, as stated above. Thus the genuine signed remainder after the earlier deletions may be restricted to $P^+(m)\le P_*$ at $o(\Sigma(N))$ error in the original $L/N$ central normalization. No claim is made at $\gamma=1/2$.

## 1. A signed divisor energy, and its short moving endpoint

We give the new unconditional estimate in a form that can be used before any prime sieve. For $Y\ge1$,

$$
               \sum_{r,t\le Y}\frac{\mu(r)\mu(t)}{[r,t]}
                      \ll 1 .                                    \tag{2}
$$

In fact, by the gcd divisor identity, the left side equals the nonnegative sum over $d\le Y$ of
$\varphi(d)(\sum_{r\le Y,\ d\mid r}\mu(r)/r)^2$. Only squarefree $d$ survive, and the inner sum is $\mu(d)/d$ times the reciprocal Mertens sum to $Y/d$ with primes of $d$ excluded. The latter is the log convolution of the ordinary reciprocal Mertens primitive with the nonnegative reciprocal weights of integers whose prime factors all divide $d$. This follows directly by convolving $\mu$ with the indicator of integers all of whose prime factors divide $d$, which gives $\mu(n)\mathbf1_{(n,d)=1}$. Write these integers as $u,v$ in the squared sum and take absolute values. The [ordinary reciprocal Mertens bound](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287), Eq. 6.18, is $O(e^{-c\sqrt t})$ at log argument $t\ge0$, with small $t$ harmless. For $M=\max(u,v)$ and $R=\operatorname{rad}(uv)$ the remaining sum over $d$ is bounded by

$$
    \sum_{\substack{d\le Y/M\\R\mid d}}
         d^{-1}e^{-c\sqrt{\log(Y/(dM))}}\ll R^{-1}.
$$

Indeed split $d/R$ into log intervals of width one measured from $\log(Y/(RM))$; the reciprocal sum in each nonempty such interval is $O(1)$, and the displayed exponential bound is summable over those intervals. Finally $\sum_{u,v\ge1}1/(uv\,\operatorname{rad}(uv))<\infty$ by its Euler factors $1+O(p^{-2})$. This proves (2) uniformly, without assumptions on the distribution of primes in shifted sequences.

For a short multiplicative shell $Y<r,t\le(1+\eta)Y$ with $Y\ge1/2$ and $0<\eta\le1/2$, the unsigned bound is

$$
       \sum \frac1{[r,t]}
          \ll 1+\eta^2\log(2Y).                                 \tag{3}
$$

Indeed expand the gcd and for $d\le(1+\eta)Y$ bound the harmonic sum of scaled integers in the shell by $O(\eta+d/Y)$, giving $\sum_d d^{-1}(\eta+d/Y)^2$. Endpoint inclusions in (3), or $Y$ bounded below by a fixed positive constant less than one, change only the absolute constant.

Let $S_k(T)=\sum_{r\mid k,r\le T}\mu(r)$ and fix a real harmonic interval $K<k\le K'$ with $K\le K'\le(1+\eta)K$ and $w=\log(K'/K)$. The reciprocal count at any lcm $[r,t]$ on it equals $w/[r,t]+O(1/K)$ by partial summation of the integer floor count. Hence uniformly for $T\le Z$,

$$
 \sum_{K<k\le K'}\frac{|S_k(T)|^2}{k}\ll w+Z^2/K.                 \tag{4}
$$

The same bound holds with $S_k$ replaced by the **unsigned** count of divisors in a multiplicative shell of relative width $O(\eta)$ below $Z$, provided $\eta^2\log(2Z)=O(1)$, by (3). Nonnegative bounds proved over all integer $k$ can also be used on squarefree $k$. If a threshold varies within such a shell, its signed primitive is bounded by the absolute fixed left-end primitive plus the unsigned shell count. This includes strict as well as weak moving cutoffs. Finally (4) is uniform in $T$ even when used under a real integral of cutoff parameters.

## 2. The genuine factorization with two short moving cuts

On the squarefree $P^+(m)>P_*$ support choose the unique largest prime $p>P^+(k)$ with $m=pk$. As before $M_>=-\Xi_D-M_\le$ exactly. If $k\le D$ and $x=pk\in V$, then $p>H_0$ and $p>D$; for $k>1$ the product $F_{0,D}(k)F_{1,D}(k;x)$ is zero, and for $k=1$ the prime indicator cancels the full product. Also no low mixed term is possible since $h\le H_0$ avoids $p$ and would divide $k$. Thus only $D<k\le2\sqrt N e^s$ can contribute.

For $k>1$, $m$ is composite and the full squarefree strict midpoint product vanishes. Thus $-\Xi_D(m)$ equals the actual sharp product on $pk$. If $k$ is prime on the remaining support, $p>k>D$, so that product is one and its reciprocal $k$ sum is $O(s/L)$ by ordinary PNT on the interval $D<k\le2\sqrt N e^s$. For composite squarefree $k$, both complete Möbius sums on $k$ (constant and first logarithm) vanish. Separate divisors of $pk$ avoiding $p$ from those containing it, and replace the omitted divisors of $k$ by complements. The two sharp factors are exactly

$$
 \begin{split}
 F_{0,D}(pk)&=-\mu(k)\sum_{\substack{r\mid k\\r< k/D}}\mu(r)
                     -\sum_{\substack{r\mid k\\r\le D/p}}\mu(r),\\
 F_{1,D}(pk;x)&=-\mu(k)\sum_{\substack{r\mid k\\r< k/D}}\mu(r)
                    \left(1-\frac{2\log(k/r)}{\log x}\right)
             -\sum_{\substack{r\mid k\\r\le D/p}}\mu(r)
                    \left(1-\frac{2\log(pr)}{\log x}\right).
 \end{split}                                                       \tag{5}
$$

Thus $p$ is no longer required to exceed $D$. All cutoffs in (5) are at most $Z=10e^{2s}$ for large $N$, since $p>P_*$, $k\le2\sqrt N e^s$, and fixed powers of $L$ are smaller than $e^s$. On their actual support, the centered factors have size $O(s/L)$ and slopes in $\log r$ of size $O(1/L)$. For the omitted terms this uses $D<k/r\le2\sqrt N e^s$, and for included terms $P_*<pr\le D$. Empty subunit cutoffs are zero. These identities and estimates remain valid for the prescribed real model weight with $p=x/k$ and $x\in V$, on its exact interval support $p>\max(P_*,P^+(k))$.

Partition $V$ and the allowed $k$ range into hard geometric cells of relative width at most $\eta=s^{-1/2}$, cutting also at their true endpoints. In a fixed pair of cells the two cutoffs $k/D$ and $Dk/x$ each vary within a multiplicative shell of width $O(\eta)$. For each cutoff, dominate the signed primitive by its value at a fixed boundary plus the unsigned short-shell count, as in (4). After fixing the $k$ cell, the ensuing majorants depend on $k$ only, not the actual $p$ within the physical cell. Since $\eta^2\log(2Z)\ll1$, each majorant has reciprocal-square mean $O(w+Z^2/K)$ over this $k$ cell, with $w,K$ its log length and its lower endpoint. This applies also to a shell containing $1$ or an integer at equality.

For the weighted factor in (5), partial summation bounds each weighted term by $O(s/L)$ times its endpoint majorant plus
$O(L^{-1}\int_1^Z |S_k(t)|\,dt/t)$, by the affine logarithm slope. Cauchy and (4) bound the reciprocal-square mean of that integral by $O((\log(2Z))^2(w+Z^2/K))$. Thus the means of the squared majorants for $F_{0,D}$ and $F_{1,D}$ are respectively $O(w+Z^2/K)$ and $O((s/L)^2(w+Z^2/K))$, on composite squarefree $k$ (we may use nonnegative upper bounds from all $k$). Cauchy gives the product's reciprocal absolute mean on that cell $O((s/L)(w+Z^2/K))$. There are $O(1+s/\eta)$ $k$ cells, with $K\ge D$ and total $w=O(s)$. Since $Z=N^{o(1)}$, their endpoint errors are negligible. For each fixed physical cell, the sum over $k$ of its uniform-in-$p$ product majorant divided by $k$ is consequently $O(s^2/L)$, including the prime $k$'s.

The low mixed term $M_\le$ is easier. It has exactly the same two forms $h\mid k$ or $h=pr$, $r\mid k$, as in the preceding deletion. In the second case the signed factors cannot contain $p$, since both $b,c<h/D\le H_0/D$ are polylogarithmic while $p>P_*$. The exact extra interval $D\max(b,c)/r<p\le H_0/r$ is unchanged. In either form there are three divisor labels, one at most $Z$ (namely $k/h$ or $r$), and two at most $W=H_0/D=L^{B-B_0}$ (namely $b,c$). Their centered weight is $O(L_2/L)$. In the reciprocal sum over $k$ the lcm of the three labels gains its reciprocal, with factor $O(s)$ from the width of the $k$ range and negligible endpoint costs. At primes $p\le W$ there are at most seven lcm assignments; at $W<p\le Z$ only the first label can carry the prime. Therefore their joint reciprocal lcm sum is at most

$$
              \prod_{p\le W}(1+7/p)\prod_{W<p\le Z}(1+1/p)
                     \ll s L_2^6 .
$$

This follows from Mertens and $B>B_0$ fixed; the floor error can be bounded by $O(Z^3/D)$. The low mixed reciprocal sum is consequently $O(s^2 L_2^7/L)$, uniformly in the physical variable, even with each true $p$ interval enlarged for the purpose of this upper bound.

Combining both estimates and $k/\varphi(k)\ll L_2$ gives the following bound: on **each** fixed physical cell there is a uniform-in-$p$ nonnegative majorant $C(k)$ for the actual coefficient $M_>(pk)$ there such that

$$
           \sum_k\frac{C(k)}k\frac{k}{\varphi(k)}
                      \ll s^2L_2^8/L .                          \tag{6}
$$

The majorant can also be taken bounded by $N^\epsilon$ for any fixed $\epsilon>0$ and large $N$, by the ordinary divisor bound or by enlarging the harmless endpoint estimates. All weights in (5) and all steps for $M_\le$ have supremum plus variation $O(\tau_4(k))$ on the entire real support at each **fixed** $k$: each candidate term contributes at most two jumps and a monotone ratio in $\log p$, and the product obeys the variation product rule. This last variation statement, unlike (6), does not partition the actual Fourier coefficients.

## 3. All-modulus transfer

On genuine prime positions $(k,N)=1$. Split the physical partner range $x=N-n$ into the above cells, and within each use the [unchanged two-root upper sieve](r66-spectral-above-bv-strip-deletions.md#2-above-level-giant-partners-a-true-full-arithmetic-upper-bound) for the actual $p,N-kp$, $p>\max(P_*,P^+(k))$, in their true interval. Both forms exceed $N^{1/100}$ for large $N$. At subinterval length $H_i$ in the $n$ variable the bound per $k$ is $O(\Sigma(N)H_i/(kL^2)\cdot k/\varphi(k)+N^{1/4}L)$. Multiply by $LC(k)$ and use (6). Summing $H_i$ gives exactly $|I|$, so there is no loss from the number of physical cells in the main bound. The sieve floor errors sum to at most $N^{.76}$ because there are $O(\eta^{-1})$ physical cells and $N^{.5+o(1)}$ possible $k$. This proves the first line of (1).

For the genuine right polynomial on $\mathfrak M$, evaluate the prime $p$ with the exact real weight of (5) and $M_\le$, and the support $p>\max(P_*,P^+(k))$. Under the stated prime GRH bounds, each $q\le Q$ residue error for fixed $k$ is $O(\sqrt{N/k}L^2)$; the slow phase and the $O(\tau_4(k))$ full variation give total right error $O_\epsilon(Q^2N^{3/4+\epsilon})$ after summing $k\ll\sqrt N e^s$. Here $e^s=N^{o(1)}$ is absorbed into the arbitrary $\epsilon$. Since $p\gg P_*\gg Q$ on actual support, each arc's density carries precisely $c_q(k)/\varphi(q)$ from the reduced $p$ classes. The same occupation bound for the right sup and variation, $O(L^4 C^{\omega(q)}/q)$, follows as before by splitting $p\mid q$ according as its prime does or does not divide the squarefree $k$ label; here the primes of $q$ are not the summation variable $p$. This keeps the pointwise rational and Fourier tails of the previous proof with integrated $O(N^{1-10^{-4}})$ error. No partition of the actual arcs or of the true right weight is necessary for this calculation.

The completed density has the unchanged local factor $S(N,k)=\sum_q\mu(q)c_q(N)c_q(k)/\varphi(q)^2$, zero at $(k,N)>1$ and otherwise $\ll\Sigma(N)k/\varphi(k)$, and right continuous factor $1/[k\log(x/k)]$. All new constraints acted only on $x,k$, not on residues. For every real $x\in V$, use (6) in its physical cell and $\log(x/k)\gg L$; the density is $O(\Sigma(N)s^2L_2^8/L^2)$. Thus the actual major coefficient obeys this bound times $|I|$ plus its power error. Subtract from the true full coefficient to get the second line of (1). Upon multiplying by $L/N$, the main part is $O(\Sigma(N)L^{2\gamma-1}L_2^8)=o(\Sigma(N))$ for fixed $\gamma<1/2$; the power term is harmless. No signed estimate for the smaller-largest-prime residual is implied.
