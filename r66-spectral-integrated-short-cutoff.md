# Integrated short-cutoff energy deepens the actual largest-prime deletion

**Scope.** We improve the [subpower largest-prime deletion](r66-spectral-subpower-largest-prime.md) for the genuine above-BV mixed term, after the exact global marginal removal. All parities now admit every fixed $0<\gamma<2/3$ in the threshold $\sqrt N\exp(-(\log N)^\gamma)$. Squarefree partners with an odd number of prime factors, equivalently $\mu(m)=-1$, admit every fixed $0<\gamma<1$. The full arithmetic upper bounds are unconditional; the pointwise minor bounds use the same historical Dirichlet GRH for the two prime progression sums at $q\le N^{1/1000}$. No GRH estimate for a Möbius progression is used. Neither an arbitrary masked prime marginal, the surviving smaller-largest-prime mixed term, nor any further part of Hypothesis S is estimated.

Use the preceding notation: $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ with fixed $B>B_0>0$, $V=[N/3,2N]$, and $s=L^\gamma$, $P_*=\sqrt N e^{-s}$. Restrict the squarefree right coefficient $M_>$ to $P^+(m)>P_*$, and set it to zero outside $V$. For the second assertion below also impose $\mu(m)=-1$. For any genuine left prime test over an exact central half-open interval $I$ with a weight of uniformly bounded supremum and variation, the actual full coefficient in absolute mass, and its genuine signed minor coefficient, are bounded respectively by $|I|$ times the corresponding row plus $O(N^{.76})$ and $O(N^{1-10^{-4}})$:

$$
 \begin{array}{c|c}
  \text{right selector} & \text{bound per unit interval length}\\ \hline
  P^+(m)>P_* &
        O\!\left(\Sigma(N)L^{-2}(s^{3/2}L_2+sL_2^6)\right)\\
  P^+(m)>P_*,\ \mu(m)=-1 &
        O\!\left(\Sigma(N)L^{-2}sL_2^6\right).
 \end{array}                                                       \tag{1}
$$

Thus the Hardy normalization $L/N$ gives $o(\Sigma(N))$ at the stated exponents. The preceding assumptions and exact endpoint convention are unchanged.

## 1. The new signed integrated energy

For $T\ge1$ define the signed primitive $S_k(T)=\sum_{r\mid k,\ r\le T}\mu(r)$ and its integrated version

$$
 J_k(T)=\int_1^T S_k(t)\frac{dt}{t}
       =\sum_{\substack{r\mid k\\r\le T}}\mu(r)\log(T/r).
$$

Take both as zero for $T<1$. The integrated analogue of the preceding signed LCM energy is

$$
 \sum_{r,t\le T}\frac{\mu(r)\mu(t)}{[r,t]}
                 \log(T/r)\log(T/t)\ll \log(2T).                 \tag{2}
$$

Indeed expand the gcd, obtaining
$\sum_{d\le T}\varphi(d)\mu^2(d)d^{-2}|\int_0^{\log(T/d)}R_d(u)\,du|^2$,
where $R_d(u)=\sum_{n\le e^u,\,(n,d)=1}\mu(n)/n$. The reciprocal Mertens primitive without masks is in $L^1(0,\infty)$, and excluding primes of $d$ convolves it with a positive forward log kernel of mass $d/\varphi(d)$, as in the previous proof. The integral inside the square is therefore at most a constant times $d/\varphi(d)$ in absolute value. Each term is at most a constant times $1/\varphi(d)$, whose sum is $O(\log(2T))$ by the ordinary Euler identity for $d/\varphi(d)$. This proves (2).

As before, write $K<k\le K'$ for a hard cell of relative width at most $\eta=s^{-1/2}$, $w=\log(K'/K)$, and take $Z=10e^{2s}$ as a uniform upper bound for all moving thresholds. The exact reciprocal count of multiples of a fixed lcm is $w/[r,t]+O(1/K)$ and the two logarithmic weights are $O(s)$. Consequently for a fixed $T\le Z$,

$$
       \sum_{K<k\le K'}\frac{|J_k(T)|^2}{k}
                       \ll s w+s^2Z^2/K.                        \tag{3}
$$

If $T$ varies within a fixed multiplicative shell of width $O(\eta)$, freeze it at one endpoint $T_0$. The error is bounded in absolute value by $O(\eta)$ times the sum of the absolute signed primitive at $T_0$ and the unsigned count in the shell. Both have reciprocal-square mean $O(w+Z^2/K)$ by the fixed primitive and raw shell estimates of the preceding proof, since $\eta^2\log(2Z)=O(1)$. This remains valid for a shell crossing $1$, extending primitives by zero below $1$. Therefore the same bound (3) holds with a majorant uniform in the moving $T$. The case of a strict endpoint in the primitive $S_k$ is still controlled by including the endpoint in the unsigned shell. The coefficients of $J_k$ at equality are zero.

## 2. Apply the signed integral to the exact sharp factors

Extract the largest prime $p>P^+(k)$ as before, $m=pk$, $p>P_*$. The genuine mixed coefficient is $M_>=-\Xi_D-M_\le$, and only $D<k\le 2\sqrt N e^s$ contributes. For prime $k>D$ one has $p>k>D$ and the sharp product equals one. Its reciprocal mass in $k$ is $O(s/L)$ by ordinary PNT. On composite squarefree $k$ use the exact compensated divisor sums of the preceding proof, with strict $T_1=k/D$ and weak $T_2=D/p$. Centering the two affine functions at $D$ gives the more precise identity

$$
 F_{1,D}(pk;x)
   =\left(1-\frac{2\log D}{\log x}\right)F_{0,D}(pk)
      +\frac2{\log x}\bigl(\mu(k)J_k(T_1)-J_k(T_2)\bigr),
                          \qquad x=kp.                           \tag{4}
$$

For the omitted divisors of $k$, the centered factor of $e=k/r$ equals its value at $D$ minus $2\log(T_1/r)/\log x$; their sign outside the sum is $-\mu(k)$. For included $pr$ the factor equals that value plus $2\log(T_2/r)/\log x$ and the sign is minus. These are the signs in (4). In particular the exact sharp gates have not been changed.

Partition into the same hard geometric physical $x$ and arithmetic $k$ cells. In a fixed cell pair, the $F_{0,D}$ squared reciprocal mean is $O(w+Z^2/K)$ by the previous moving primitive bound. Also $1-2\log D/\log x=O(L_2/L)$ uniformly. From (3)–(4) the squared reciprocal mean of a uniform-in-$p$ majorant for $F_{1,D}$ is
$O(L^{-2} (s w+s^2Z^2/K))$, since $s$ exceeds every fixed power of $L_2$. Cauchy therefore bounds the product's reciprocal mean on a $k$ cell by $O(\sqrt{s}\,w/L)$ plus power-small endpoint errors. For example those errors are bounded by $O(sZ^2/(KL)+s Z\sqrt{w/K}/L)$, and remain power-small after the $O(1+s/\eta)$ cells. Summing $w=O(s)$ gives $O(s^{3/2}/L)$ for each physical cell, including its prime-$k$ term.

On the odd total parity selector $\mu(m)=-1$ we have $\mu(k)=+1$, so $k$ has an even number of distinct prime factors: $m=pk$ is squarefree and $\mu(p)=-1$. The case $k=1$ has no contribution, as in the preceding deletion. The difference in (4) is then the signed integral between the two cutoffs, whose log distance is exactly

$$
        \log(T_1/T_2)=\log(x/D^2)=2B\log L+O(1)>0 .
$$

Clipping the lower end to $1$ if necessary can only shorten it. Over a fixed cell pair the possible integration intervals all lie in one deterministic interval of log length $O(L_2)$, because the two cutoffs vary by relative $O(\eta)$. Cauchy in this interval and the fixed primitive estimate (4) of the subpower proof give a squared reciprocal mean $O(L_2^2(w+Z^2/K))$ for its absolute-integral majorant. Thus the $F_{1,D}$ squared mean has factor $O(L_2^2/L^2)$ instead of $O(s/L^2)$. The product's full reciprocal mean becomes $O(sL_2/L)$ in a fixed physical cell. The parity mask is constant in $p$ at fixed $k$.

## 3. Sharper elementary bound for the low mixed subtraction

The low mixed $M_\le$ is supported on $D<h\le H_0$, and its two signed divisors $b,c<h/D\le W:=H_0/D$ are polylogarithmic. We need only their absolute incidence at weight $1$, with an additional centered factor $O(L_2/L)$. When $h\mid k$ and $p$ is not in $h$, write $k=h u$ and sum over $h$ first. The $u$ harmonic sum in the allowable range is $O(s)$; for fixed $b,c$ the reciprocal $h$ count on $(D,H_0]$ is $O(L_2/[b,c]+1/D)$. Summing $b,c\le W$ costs $O(L_2^3)$ in $1/[b,c]$ by the three occupied-prime states for two squarefree divisors, and the endpoint remainder is negligible. Thus the total reciprocal incidence is $O(sL_2^4)$.

When $h=pr$ contains $p$, the signed $b,c$ divide $r$ as before. Put $k=rv$ so that $h=x/v$. In a fixed physical $x$ cell with endpoints $x_-,x_+$, the condition $D<h\le H_0$ puts $v\in[x_-/H_0,x_+/D)$, up to endpoint conventions, of log length $O(L_2)$. Its reciprocal sum is $O(L_2)$. The remaining $r\le Z$ harmonic count of multiples of $[b,c]$ is $O(s/[b,c])$. The same sum over the two short signed divisors gives again $O(sL_2^4)$. Both estimates majorize the actual coefficient uniformly in $p$ within the fixed physical cell; relaxing these support intervals is done only in this upper bound.

The extra centered factor yields a low mixed reciprocal mean $O(sL_2^5/L)$ on every physical cell. Multiplying this and the two sharp-product means of Section 2 by $k/\varphi(k)\ll L_2$ produces majorant sums $O((s^{3/2}L_2+sL_2^6)/L)$ and $O(sL_2^6/L)$ respectively.

## 4. Same individual-modulus transfer

The true two-prime upper sieve, exact largest-prime representation, and prime progression major calculation are unchanged from the [subpower proof](r66-spectral-subpower-largest-prime.md). For clarity the unconditional sieve in each physical cell uses the actual interval in $p$ with $p>\max(P_*,P^+(k))$ and $n=N-kp\in I$, of length at most that cell's first-variable length divided by $k$. On $(k,N)=1$ it counts at most
$O(\Sigma(N)|I_{\rm cell}|(k/\varphi(k))/(kL^2)+N^{1/4}L)$
pairs. Multiply by $L$ for $\lambda$ and sum the majorants just proved. The main lengths sum to $|I|$, and the floor errors remain $O(N^{.76})$ because the number of cells is polynomial in $L$ and $k$ and all coefficient majorants are $N^{.5+o(1)}$ and $N^{o(1)}$ in size respectively.

For the major calculation the actual weight still has variation $O(\tau_4(k))$ as a function of $p$, because equation (4) was only used to bound the same sharp product, not to replace it. The parity selector, if present, depends only on $k$. The $p$ sums in reduced classes thus give $c_q(k)/\varphi(q)$ with total right polynomial error $O_\epsilon(N^{3/4+\epsilon}Q^2)$. Prime sizes, occupation bounds, Fourier and Ramanujan tails are identical: $e^s=N^{o(1)}$ for all fixed $\gamma<1$. The completed density vanishes on $(k,N)>1$, otherwise has the same local factor at most $O(\Sigma(N)k/\varphi(k))$, and the real cofactor $1/[k\log(x/k)]$ supplies another $O(1/L)$. The new majorant sums give exactly the two rows of (1); the integrated power error remains $O(N^{1-10^{-4}})$. Subtracting the major from the genuine full sum proves the minor bounds with their stated log exponents. No unestimated signed term outside these selectors is replaced by its major density.
