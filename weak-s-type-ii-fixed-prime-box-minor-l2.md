# A separate-minor-$L^2$ obstruction in an actual fixed prime box

This is a method obstruction, not a signed lower bound. Use the definitions and stretched major arcs $\mathfrak M$ of the [signed seam major-arc estimate](weak-s-type-ii-signed-seam-major-arcs.md). Take $N=2^j$, $X=\sqrt N$, $L=\log N$, and the hard cuts

$$
 I_u=[.740X,.745X],\quad I_v=[.715X,.720X],\quad
 I_d=[X,.100N^{.50001}],\qquad y=9N/16,\quad t=N^{.49999}.
$$

Take $E(u,v)=1$ exactly when both $u,v$ are prime, and write $P=P_E$ and $D$ for the two exact circle polynomials there. All possible $u,v$ in the box satisfy $N/2<uv<9N/16$ and both prime factors are $N$-units. In particular they have no old tags, both small radicals are one, and their prime ratio is bounded, so lies below $N^{.000035}$. Thus this is a genuine fixed proportional, doubly prime subfamily of the previous no-exchange seam. The original weight at prime $v$ is $\log v$, not a prime model.

**Proposition.** Unconditionally $\|P\|_2^2\asymp N$ and $\|D\|_2^2\gg N$ over the full circle, for all sufficiently large such $N$. Under global Dirichlet GRH (including ordinary RH), the same two respective lower bounds hold with both norms restricted to $\mathfrak m=(\mathbb R/\mathbb Z)\setminus\mathfrak M$. In particular the ordinary separate Cauchy–Schwarz upper-bound quantity for the signed minor coefficient is at least $cN$ already in these fixed $u,v$ intervals. No conclusion about the signed value follows.

## 1. True signed coefficients of the complementary polynomial

The full-circle norm of $P$ follows from Parseval and the prime number theorem: the disjoint $I_u,I_v$ identify a unique ordered pair from its semiprime product, so the nonzero coefficients are exactly $-\log v$ and

$$
 \|P\|_2^2=\#\{u\in I_u:u\text{ prime}\}
                 \sum_{\substack{v\in I_v\\v\text{ prime}}}(\log v)^2
              \asymp N.
$$

To bound the actual signed $D$ norm, select primes $p$ in $[N^{.500002},N^{.500006}]$ and odd squarefree integers $k$ in

$$
   J_p=[.450N/p,.490N/p],\qquad K_p=N/p,\qquad
   B_p=\left\lfloor .100N^{.50001}/p\right\rfloor .
$$

We have $k<X<p$ and $N-y<pk<N/2$. The prime $p$ is uniquely determined by $pk$, because all its other prime factors are below $X$. Every divisor $d$ of $pk$ of at least $X$ is $p b$ with $b\mid k$. The hard $d$ cap is exactly $b\le B_p$, and $k/b\ge .450K_p/B_p\ge4.5N^{.49999}>t$. These are also all allowed choices for the $D$ coefficient at $pk$. The unit and squarefree masks hold in each instance because $p,k$ are odd, $k$ squarefree and $p>k$. Therefore the coefficient at $pk$ is exactly

$$
              -\theta_{B_p}(k),\qquad
            \theta_B(k)=\sum_{\substack{b\mid k\\b\le B}}\mu(b).
$$

This is the signed coefficient, with all its competing divisor representations present. In particular retaining one representation alone would *not* prove the claimed norm lower bound.

## 2. The squarefree variance of the truncated Möbius divisor sum

For squarefree odd $\ell$ and $J_p$ as above, elementary squarefree counting gives

$$
 \sum_{\substack{k\in J_p,\ k\ {\rm odd}\\\ell\mid k}}\mu^2(k)
 = c_{\mathrm{odd}}|J_p|\prod_{r\mid\ell}\frac1{r+1}
       +O\bigl(\sqrt{K_p/\ell}\,\tau(2\ell)\bigr),
 \qquad c_{\mathrm{odd}}=\tfrac12\prod_{r\ {\rm odd\ prime}}(1-r^{-2}),
$$

in the range $\ell\le B_p^2$. In fact, write $k=\ell h$ and retain odd squarefree $h$ with $(h,\ell)=1$. Expand $\mu^2(h)$ and the $2\ell$ unit mask; Möbius square bases up to $\sqrt{K_p/\ell}$ each give $O(\tau(2\ell))$ floor errors. Extending the model square-base sum costs $O(\sqrt{K_p/\ell}\,\tau(2\ell))$. The model contains $(1-1/r)/(1-1/r^2)=r/(r+1)$ for every $r\mid\ell$, in addition to the factor $1/\ell$.

Expand $\theta_{B_p}^2$ with $\ell=[b_1,b_2]$. Only odd squarefree $b_1,b_2$ remain. With $B=B_p$ and $K=K_p$, the aggregate error is $O_\epsilon(\sqrt K\, B^{2+2\epsilon})=o(K)$ uniformly, since $B\ll N^{.000008}$ and $K\ge N^{.499994}$. The model term divided by $c_{\mathrm{odd}}|J_p|$ is exactly the second moment of

$$
 T_B=\sum_{\substack{b\le B,\ b\ {\rm odd}\\b\ {\rm squarefree}}}
               \mu(b)\prod_{r\mid b}Z_r ,
$$

where the $Z_r$ for odd primes $r\le B$ are independent Bernoulli variables of means $1/(r+1)$. Center each variable and expand in the orthogonal products $\prod_{r\mid \ell}(Z_r-\mathbb E Z_r)$ for odd squarefree $\ell$. Orthogonality follows immediately from independence and a factor of mean zero whenever the subsets differ. For $B/2<\ell\le B$ the coefficient of this centered product is exactly $\mu(\ell)$, since no other multiple of $\ell$ occurs. Consequently

$$
 \mathbb E |T_B|^2\ge
  \sum_{\substack{B/2<\ell\le B\\\ell\ {\rm odd,\ squarefree}}}
           \frac1\ell\prod_{r\mid\ell}(1+1/r)^{-2}\gg1 .
$$

For the lower bound, a positive proportion of the integers in $(B/2,B]$ are odd squarefree by elementary squarefree counting. The sum of $\sum_{r\mid\ell}1/r$ over the interval is $O(B)$, by counting multiples and summing the reciprocal squares. Thus a positive proportion of odd squarefree $\ell$ have a uniformly bounded inner sum and then the product is bounded below. Here $B_p$ tends to infinity uniformly.

This gives $\sum_{k\in J_p,\ k\ {\rm odd}}\mu^2(k)|\theta_{B_p}(k)|^2\gg K_p$. Parseval and the disjoint supports indexed by $p$ now give $\|D\|_2^2\gg \sum_{p}N/p\gg N$, since the prime reciprocal sum in the stated fixed power band tends to $\log(.500006/.500002)>0$. This proves the unconditional part.

## 3. Remove the same stretched major arcs

For $D$ the unconditional major-arc bound and the choice of $\eta$ in §3 of the companion proof imply

$$
 \int_{\mathfrak M}|D(\alpha)|^2d\alpha
             \ll N Q_0^3 e^{-2c_2\Phi(L)}=o(N).
$$

For $P$ we use global Dirichlet GRH only here. Write $\alpha=a/q+\beta\in\mathfrak M$. Since $q\le Q_0=N^{o(1)}$, the two prime factors in the fixed box exceed $q$. For fixed prime $u$, partition the prime $v$ sum into reduced classes modulo $q$. The [prime counting bound under GRH, Lee, Corollary 1.1](https://arxiv.org/pdf/2301.13457v2#page=2) gives $O(X^{1/2}L^2)$ for the weighted prime count error in each prefix, uniformly in those classes and endpoint scales $\asymp X$. The cases $q=1,2$ follow from ordinary RH and removal of the prime $2$. Partial summation costs a factor $1+N|\beta|$; the exact sum of the unit phases is the Ramanujan sum $c_q(au)=\mu(q)$ since $(au,q)=1$. Thus

$$
 \sum_{\substack{v\in I_v\\v\text{ prime}}}\log v\, e(\alpha uv)
 =
 \frac{\mu(q)}{\varphi(q)}
         \int_{I_v}e(\beta u z)\,dz
      +O\bigl(q X^{1/2}L^2(1+N|\beta|)\bigr).
$$

We have $\big|\int_{I_v}e(\beta u z)dz\big|\ll X/(1+N|\beta|)$. Summing over the $O(X/L)$ available $u$ bounds the absolute $P$ main term by $O(N/(L\varphi(q)(1+N|\beta|)))$, with error $N^{3/4+o(1)}$ across the stretched major arcs. Squaring and integrating (the total arc measure is $O(Q_0^3/N)$), the main contributes at most

$$
       \ll \frac{N}{L^2}\sum_{q\le Q_0}\frac1{\varphi(q)}
           \ll \frac{N\log(2Q_0)}{L^2}=o(N)
$$

and the error at most $N^{1/2+o(1)}$. The reciprocal totient sum follows by expanding $q/\varphi(q)$ as $\sum_{r\mid q}\mu^2(r)/\varphi(r)$. The same proof using Siegel–Walfisz instead of GRH removes the classical smaller union $q,N|\beta|\le L^C$ unconditionally for each fixed $C$, with ineffective constants; the stretched-arc claim above uses GRH.

Both minor-arc norms are therefore at least a positive constant times $\sqrt N$ on the specified stretched arcs under GRH (and on the stated smaller union unconditionally). This obstruction is to estimating the signed minor coefficient just by their separate $L^2$ norms. Cancellation between the two Fourier functions or within a more structured partition is not ruled out, and nothing here proves or refutes weak S.
