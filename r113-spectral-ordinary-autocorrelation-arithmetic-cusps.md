# Exact arithmetic cusps in the ordinary autocorrelation

The ordinary autocorrelation used in the fixed-radical unsigned wall is not a smooth continuum correlation. Its symmetric small shift at every fixed lag is determined by exact coincidences of integer logarithms. The signed coprimality sum turns those coincidences into one explicit Euler weight. In particular the origin always has slope $-1/2$ from the right, and cusps of both symmetric signs occur densely. The result concerns this ordinary arithmetic profile, not a pointwise assertion about the full mixed correlation or the existence of an exceptional zero.

## 1. Statement

Fix an even squarefree integer $R$. Use the same ordinary $C_R$ as in the [true wall formula](r112-spectral-odd-disjoint-true-wall-correlation.md), defined in terms of the reciprocal primitives of the [shifted autocorrelation](r108-spectral-odd-disjoint-shifted-autocorrelation.md). For squarefree $j$ with $(j,R)=1$, put

$$
 \begin{split}
 a_j(n)&=\mu(n)\alpha^\circ(n)\mathbf1_{(n,Rj)=1}
               \quad(n\ {\rm squarefree}),\\
 R_j(u)&=\sum_{n\le e^u}a_j(n),\qquad
 C_j(t)=\int_{\mathbb R} R_j(u)R_j(u+t)\,du,\\
 C_R(t)&=\sum_{\substack{j\ {\rm sf},\;(j,R)=1}}
                       \mu(j)\alpha^\circ(j)^2 C_j(t).
 \end{split}                                                     \tag{1}
$$

Set $a_j(n)=0$ for nonsquarefree $n$ and $R_j(u)=0$ below $0$. The multiplicative $\alpha^\circ$ on the admissible squarefree integers has local factors $\alpha_p^\circ=(p-1)/(p^2-2)$ for odd $p$ and $\alpha^\circ(1)=1$. One can set $\alpha_2^\circ=0$ in positive majorants, since $2\mid R$. In particular $|a_j(n)|\le1/n$.

**Theorem.** At the origin one has

$$
        C_R(h)=C_R(0)-\frac{|h|}{2}
                  +O_R\!\left(h^2(1+\log^2(1/|h|))\right)
                    \qquad(0<|h|<1/8).                         \tag{2}
$$

At any fixed real $t$ the following symmetric limit exists:

$$
 \lim_{h\downarrow0}
       \frac{2C_R(t)-C_R(t+h)-C_R(t-h)}{h}
  =
 \begin{cases}
   \mu(ab)\alpha^\circ(ab),
      & e^t=a/b\ {\rm in\ lowest\ terms},\
                          ab\ {\rm sf},\ (ab,R)=1,\\
   0, & \text{otherwise}.
 \end{cases}                                                    \tag{3}
$$

Both the positive and negative nonzero coefficient sets in (3) are dense. In particular $C_R$ is not differentiable at each admissible log ratio and is neither convex nor concave on any open interval. A zero of the symmetric limit does not assert differentiability or identify a regular part of a second derivative.

## 2. Finite jump isolation and a uniform tail

The ordinary bounds (6)–(7) of the shifted proof give, with $A(j)$ its positive Euler moment, $A(j)\ge1$,

$$
 \|R_j\|_{2,[u,\infty)}
       \ll_R A(j)e^{-c_0\sqrt u}\quad (u\ge1),\qquad
 \sum_{\substack{j\ {\rm sf},\;(j,R)=1}}\alpha^\circ(j)^2 A(j)^2
                         \ll1 .                                 \tag{4}
$$

These estimates use the ordinary reciprocal Möbius primitive and a positive shift ratio for the deleted primes. They are independent of the real lag below.

Write $\Delta_h R_j(u)=R_j(u+h)-R_j(u)$ for $0<h<1/8$. Directly from the true jumps at $\log n$,

$$
      \Delta_h R_j(u)=\sum_{n\ge1}a_j(n)
                         \mathbf1_{[\log n-h,\,\log n)}(u).       \tag{5}
$$

At any finite $u$ this is a finite sum. Put $M_h=\lfloor 1/(4h)\rfloor$. The intervals for $n\le M_h$ are disjoint from each other and from all later jump intervals: the gap $\log(n+1)-\log n\ge1/(n+1)$ exceeds $h$ up to $n=M_h$. Their squared integral is therefore exactly $h\sum_{n\le M_h}|a_j(n)|^2$, regardless of which jumps are masked.

The remaining jump intervals have $u\ge\log(M_h+1)-h$. On that range their absolute sum at any $u$ is bounded by

$$
      \sum_{e^u<n\le e^{u+h}}\frac1n
          \ll h+e^{-u}\ll h.                                    \tag{6}
$$

The first inequality follows by multiplying the interval's integer count by $e^{-u}$, including a possible endpoint. The last follows from the lower bound on $u$. Integrate its square over $u\le U_h=C_0\log^2(1/h)$ for a sufficiently large fixed $C_0$. This costs $O(h^2\log^2(1/h))$. For $u>U_h$ the remaining increment is the full $\Delta_h R_j$ and its squared integral is $O_R(A(j)^2 h^3)$ by (4) with that choice of $C_0$. Thus the later jumps together cost at most $O_R(A(j)^2h^2(1+\log^2(1/h)))$ in squared norm. Replacing the finite diagonal sum by its infinite value costs at most $h\sum_{n>M_h}n^{-2}=O(h^2)$. We obtain

$$
 \|\Delta_h R_j\|_2^2
     =h\sum_{n\ge1}a_j(n)^2
             +O_R\!\left(A(j)^2h^2(1+\log^2(1/h))\right).        \tag{7}
$$

We also need a fixed cutoff $M$ for a limit at nonzero lag. Let $D_{j,M,h}$ be the first $M$ terms in (5), and $E_{j,M,h}=\Delta_h R_j-D_{j,M,h}$. For sufficiently small $h$ at fixed $M$, the terms with $M<n\le M_h$ still have disjoint intervals and their squared integral is at most $h\sum_{n>M}n^{-2}$. The later contribution is the one already bounded, with disjoint support. Thus

$$
   \|E_{j,M,h}\|_2^2
      \ll h/M+O_R\!\left(A(j)^2h^2(1+\log^2(1/h))\right).        \tag{8}
$$

No finiteness of the total absolute jump mass is used in these statements.

## 3. Pair the jumps at every fixed lag

The real correlation identity is exact for any $t$:

$$
  2 C_j(t)-C_j(t+h)-C_j(t-h)
       =\int_{\mathbb R}\Delta_h R_j(u)\Delta_h R_j(u+t)\,du .    \tag{9}
$$

For fixed $M$, apply (9) first with the increments on the right replaced by $D_{j,M,h}$. In the product, the two jump intervals at $\log n$ and $\log m-t$ either coincide or are disjoint for all sufficiently small $h$ (depending on $M,t$ only). The normalized limit of this finite correlation is exactly $\sum_{m,n\le M,\ \log(m/n)=t}a_j(n)a_j(m)$. To pass to all jumps, (7) bounds the normalized squared norm of the full increment by $O_R(A(j)^2)$ uniformly as $h\downarrow0$, and the finite increment is bounded the same way. Equation (8) and Cauchy--Schwarz, also after translation, bound the limsup error after division by $h$ by $O_R(A(j)^2/\sqrt M)$. Sending $M\to\infty$ gives

$$
  \lim_{h\downarrow0}\frac{2 C_j(t)-C_j(t+h)-C_j(t-h)}h
             =\sum_{\log(m/n)=t}a_j(n)a_j(m).                   \tag{10}
$$

The diagonal sum converges absolutely: with $t$ fixed, each $n$ has at most one matching $m$, and the two square sums converge. There is no uniform Diophantine estimate of gaps between nonmatching logarithms; the argument takes the finite cutoff first. By (7)–(9) the same uniform bound $O_R(A(j)^2)$ dominates the normalized expressions for all $t$. The moment (4) now justifies both the $j$ limit exchange in (10) and an absolute bound $O_R(h)$ on the symmetric numerator for $C_R$, uniformly in $t$.

If $e^t$ is irrational the right of (10) is empty. Otherwise write $e^t=a/b$ with positive coprime integers $a,b$, so that $m=da,n=db$ for a positive integer $d$. If $ab$ is not squarefree or is not prime to $R$ then there is no nonzero product. In the remaining case the product vanishes unless $(ab,j)=1$, $d$ is squarefree and $(d,abRj)=1$. When it does not vanish, it equals $\mu(ab)\alpha^\circ(ab)(\alpha^\circ(d))^2$. Multiply by the signed $j$ weight from (1) and sum. All terms are absolutely dominated by the convergent Euler product with local factor $1+2(\alpha_p^\circ)^2$. Outside $abR$ each prime either stays absent, occupies only $d$ with $+(\alpha_p^\circ)^2$, or occupies only $j$ with $-(\alpha_p^\circ)^2$; simultaneous occupancy is excluded. The resulting product is exactly $1$. This proves (3), including its sign and the origin value $1$.

For the quantitative claim at the origin use (9) there and evenness; its right side becomes $\|\Delta_hR_j\|_2^2$. Insert (7) before summing $j$. The same local cancellation for $(a,b)=(1,1)$ gives coefficient $1$, and (4) controls the errors. This proves the full remainder in (2), not merely the origin limit.

Nonzero values of (3) preclude a two-sided derivative at that lag, because a derivative would give a symmetric numerator $o(h)$. In a given open lag interval choose reduced ratios $p/q$ of distinct primes outside $R$. They are dense by the prime number theorem on any fixed positive relative interval for $p$ at a chosen sufficiently large prime $q$; for instance use [Johnston--Yang, Corollary 1.3](https://arxiv.org/pdf/2204.01980#page=2). These ratios have positive coefficients in (3). For negative coefficients fix another odd prime $p_0\nmid R$ and instead use ratios $p_0p/q$ of three distinct primes outside $R$. They are dense by the same argument, making the chosen interval avoid $p_0$ if necessary to ensure $p\ne q$. Their coefficients are negative. On an interval where a function is convex its symmetric numerator is nonpositive at interior points; for a concave function it is nonnegative. The two dense sets therefore exclude both possibilities for $C_R$.

## 4. Consequence for the true unsigned wall profile

In the notation of the true wall proof, its exact ordinary integrand before the fixed normalization is

$$
                  B_R(T,d)=T C_R(d)-2\int_0^d C_R(t)\,dt .
$$

The directed integral here is the original cumulative term, including on the negative side. For $T>0$ the origin expansion gives

$$
 B_R(T,d)=T C_R(0)-\frac{T}{2}|d|-2C_R(0)d
       +O_R\!\left(Td^2(1+\log^2(1/|d|))+d^2\right)              \tag{11}
$$

for $0<|d|<1/8$, with the identity at zero. In particular $B_R(T,v/T)-T C_R(0)\to-|v|/2$ uniformly on each fixed bounded real $v$ interval when $T\to\infty$. In the true wall formula one must use the actual $T=T_m$ and $d=T_m-\log p$ in this expression, not substitute a continuum Dickman kernel or move the physical wall. A fine test selecting $|d|=O(1/T)$ need not carry macroscopic mass. This local profile conclusion preserves every scope bound of the true wall result: no claim on the distinct signed pole, the full exceptional difference, or a full mixed correlation.
