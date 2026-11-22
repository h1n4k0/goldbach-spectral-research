# Effective major-arc cancellation for the signed no-exchange seam

This isolates the actual minor-arc estimate needed in the [post-R56 seam](weak-s-type-ii-two-prime-exchange.md), including the genuine subfamily where both factors are prime at fixed proportions of $\sqrt N$. It does not bound the full signed coefficient.

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $V=N^{.2499}$, $N/2\le y\le 9N/16$, $t\ge N^{.49999}$. Let $I_u,I_v,I_d$ be arbitrary hard intervals. Restrict $u,v$ to at most $N^{.50002}$, $d\ge X$, and retain any selector $E(u,v)$ with values in $\{0,1\}$, independent of $d,k$; take for instance the exact R56 complement, with both small radicals below $N^{.000035}$, no old-band prime, and no qualifying opposite-side prime ratio. Write $e(x)=e^{2\pi i x}$ and set

$$
\begin{aligned}
 P_E(\alpha)&=\sum_{\substack{u\in I_u,\ v\in I_v,\ u,v\le N^{.50002}\\
                 N/2<uv\le y,\ (uv,N)=1}}
             E(u,v)\mu(u)b_{\rm II}(v)e(\alpha uv),\\
 D(\alpha)&=\sum_{\substack{d\in I_d,\ d\ge X\\(d,N)=1}}\mu(d)
         \sum_{\substack{k>t,\ N-y\le dk<N/2\\(k,dN)=1}}\mu^2(k)e(\alpha dk),
 \qquad b_{\rm II}(v)=\sum_{r\mid v,\ r>V}\Lambda(r).
\end{aligned}
$$

The full circle integral of $P_E(\alpha)D(\alpha)e(-N\alpha)$ is the genuine signed sum on $uv+dk=N$. This follows from $\mu(d)\mu^2(dk)=\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$ and the fact that $(uv,N)=1$ forces $(dk,N)=1$ on the exact coefficient. Thus both unit masks and the strict $k>t$ and $uv>N/2$ are preserved. The automatic ceiling $d<N^{.50001}/2$ is inside the support of $D$.

**Theorem.** Put $\Phi(L)=L^{3/5}(\log L)^{-1/5}$ and $Q_0=\exp(\eta\Phi(L))$ for a sufficiently small absolute effective $\eta>0$. Let $\mathfrak M$ be the union on $\mathbb R/\mathbb Z$ of $\alpha=a/q+\beta$, $(a,q)=1$, $q\le Q_0$, $|\beta|\le Q_0/N$. There is an absolute effective $c>0$ such that, uniformly in the hard intervals, $E,t,y$,

$$
    \sup_{\alpha\in\mathfrak M}|D(\alpha)|\ll N e^{-c\Phi(L)},\qquad
    \int_{\mathfrak M}|P_E(\alpha)D(\alpha)|\,d\alpha
                   \ll N e^{-c\Phi(L)} .
$$

The implied constants and the sufficiently-large threshold are effective, with no Dirichlet GRH, Siegel–Walfisz input, or assumption about a shifted Möbius correlation. Hence the required estimate in this sector is the **signed** minor coefficient on $(\mathbb R/\mathbb Z)\setminus \mathfrak M$; this theorem bounds neither its absolute integral nor its signed value.

## 1. The exact additive squarefree density

On a dyad $d\asymp D_0$ in the actual support, put $K_0=N/D_0$. For fixed $d$, let $J(d)$ be the real interval of $x>t$ with $N-y\le dx<N/2$, empty if these conflict. Its endpoints, including any possible integer equalities, specify precisely the original $k$ sum. Let

$$
 W_\beta(d)=\int_{J(d)} e(\beta dx)\,dx .
$$

For coprime $a,q$, fixed $d$ with $(d,N)=1$ and $\mu(d)\ne0$, use the exact squarefree expansion $\mu^2(k)=\sum_{c^2\mid k}\mu(c)$. Put $k=c^2\ell$. It forces $(c,dN)=1$, and expand $\mathbf1_{(\ell,dN)=1}$ by $h\mid dN$, $\ell=h j$. For fixed $c,h$, the function of the integer $j$ given by $e(a d c^2 h j/q)$ is periodic modulo $q$ with mean $\mathbf1_{q\mid d c^2 h}$. A hard prefix sum minus its mean times the interval length is $O(q)$, even at a strict endpoint, by splitting off complete periods. Partial summation against $e(\beta d c^2h j)$ costs a factor $1+N|\beta|$, since $d x\ll N$ throughout the original $k$ interval. Thus the inner sum over $j\in J(d)/(c^2h)$ equals

$$
       \frac{\mathbf1_{q\mid d c^2h}}{c^2 h} W_\beta(d)
             +O\bigl(q(1+N|\beta|)\bigr).
$$

Here and below a contribution from an empty interval is zero. There are $O(\sqrt{K_0})$ possible $c$ and at most $\tau(dN)$ possible $h$. Extend **only the main term** to all $c\ge1$; its absolute tail past $\lfloor\sqrt{N/(2d)}\rfloor$ is $O(\sqrt{K_0}\tau(dN))$ by the $1/c^2$ sum and $|W_\beta|\ll K_0$. Consequently

$$
\begin{aligned}
 \sum_{\substack{k\in J(d)\\(k,dN)=1}}\mu^2(k)e((a/q+\beta)dk)
 &= A_q(d;N) W_\beta(d)
       +O\bigl(q(1+N|\beta|)\sqrt{K_0}\tau(dN)\bigr),\\
 A_q(d;N)
 &=\sum_{\substack{c\ge1\\(c,dN)=1}}
       \frac{\mu(c)}{c^2}
          \sum_{h\mid dN}\frac{\mu(h)}h\mathbf1_{q\mid d c^2h}.
\end{aligned}
$$

The main density does not depend on the numerator $a$ or on a unit residue class of $d$. Its absolute Euler product converges. At $p\nmid q$, the factor is $1-1/p$ if $p\mid dN$, and $1-1/p^2$ otherwise. At $p^j\Vert q$, $j\ge1$, the factors are as follows:
- If $p\mid d$, hence $p\nmid N$, it is $1-1/p$ for $j=1$, $-1/p$ for $j=2$, and zero for $j\ge3$.
- If $p\nmid dN$, it is $-1/p^2$ for $j=1,2$, and zero for $j\ge3$.
- If $p\mid N$, hence $p\nmid d$, it is $-1/p$ for $j=1$, and zero for $j\ge2$.

These follow by allowing a prime of $dN$ only on the squarefree $h$ leg, or a prime outside $dN$ only on the squarefree $c$ leg. In particular, for $g=(d,\operatorname{rad}q)$ on the squarefree $d$ support,

$$
 A_q(d;N)=C_{q,N,g}\prod_{\substack{p\mid d\\p\nmid qN}}\frac{p}{p+1},
                  \qquad |C_{q,N,g}|\le1 .
$$

No positivity or interchange with an unsigned copy of $\mu(d)$ is required.

## 2. Effective cancellation in the $d$ main term

For $M\le N^3$ and $N^{.48}\le Y\le 2N$, the masked weighted summatory estimate

$$
  \sum_{\substack{n\le Y\\(n,M)=1}}\mu(n)
       \prod_{p\mid n}\frac{p}{p+1}
          \ll Y e^{-c_1\Phi(L)}
$$

has absolute effective constants. Here is a proof. The masked coefficient is $\mu*\rho_M$, where $\rho_M$ is multiplicative and $\rho_M(p^j)=1$ for $p\mid M$, $j\ge1$, and $\rho_M(p^j)=1/(p+1)$ otherwise. This follows by dividing its Euler factors by $1-p^{-s}$. At $\sigma=1$, $\sum \rho_M(h)h^{-1}\ll L^C$: the unrestricted factors at $p\nmid M$ are absolutely bounded, while the inverse factors from $p\mid M$ are bounded by splitting at $p=L$. The same splitting gives $\sum\rho_M(h)h^{-3/4}\le \exp(O(L^{1/4}))$; below $L$ compare to the sum over all integers, and above $L$ use $\#\{p:p\mid M\}=O(L)$.

Use the classical effective ordinary Mertens estimate at scale $Y/h$ for $h\le\sqrt Y$, e.g. [Lee and Leong, Theorem 2.2, (23)](https://arxiv.org/html/2208.06141v5#S2.SS2). Since $\log(Y/h)\ge .24 L$, its exponent is at least a constant times $\Phi(L)$; the logarithmic factors above are absorbed. For $h>\sqrt Y$, use the trivial inner bound $Y/h$ and the $3/4$ moment, costing at most $Y^{7/8}\exp(O(L^{1/4}))$. This proves the estimate. Only the ordinary zeta function is used.

For a $d$ prefix within a dyad, split by $g=(d,\operatorname{rad}q)$, write $d=gn$, and omit $g$ not prime to $N$. Because $\mu(d)$ requires squarefreeness, the exact mask on $n$ is $(n,qN)=1$. In that split the weight is the preceding masked Möbius coefficient times $\mu(g)C_{q,N,g}$, and all endpoint scales are $\asymp D_0/g\ge N^{.48}$ for sufficiently large $N$, since $q\le Q_0=N^{o(1)}$. Hence all such partial sums of $\mu(d)A_q(d;N)$ are

$$
 \ll D_0 e^{-c_1\Phi(L)}\sum_{g\mid\operatorname{rad}q}\frac1g
 \ll D_0(1+\log q)e^{-c_1\Phi(L)} .
$$

The smoothly-integrated weight needs no smoothing of the hard $t$ boundary. After changing variables $z=dx$,

$$
 W_\beta(d)=\frac1d\int_{\max(N-y,td)}^{N/2}e(\beta z)\,dz
$$

with value zero if the lower endpoint is past $N/2$. The lower endpoint increases monotonically with $d$ until the integral vanishes, giving total variation $O(N)$ of the undivided integral, independent of $\beta$ and $t$. Including $1/d$ gives both supremum and total variation $O(N/D_0)$ on the dyad. Abel summation now bounds the actual main $d$ sum by $O(N(1+\log q)e^{-c_1\Phi(L)})$. A hard $I_d$ only restricts the interval of Abel summation.

## 3. Major arcs and the exact remaining bound

Summing the error in §1 over $d\asymp D_0$ uses $D_0\sqrt{K_0}=\sqrt{ND_0}\ll N^{.750005}$ and the effective divisor bound $\tau(dN)\ll_\epsilon N^\epsilon$. Summing all dyads, the error for $q,N|\beta|\le Q_0$ is $O_\epsilon(N^{.750005+\epsilon} Q_0(1+Q_0)L)$, with a fixed power saving. The $O(L)$ main dyads and $1+\log q=O(1+\Phi(L))$ are absorbed in the exponential, so for an absolute effective $c_2>0$ one has $|D(\alpha)|\ll N e^{-c_2\Phi(L)}$ there. Choose $\eta$ small enough compared to $c_2$, e.g. $\eta<c_2/10$; for deriving $c_2$ one may first assume $\eta\le1$. The measure of the union is $O(Q_0^3/N)$ by counting reduced rationals and arc lengths, while $|P_E|\ll NL^2$ by $b_{\rm II}(v)\le\log v$ and the ordinary divisor first moment. This proves the integrated estimate with an absolute effective $c>0$.

In particular, for these exact supports the estimate still needed for an $o(N)$ conclusion is

$$
 \left|\int_{(\mathbb R/\mathbb Z)\setminus\mathfrak M}
           P_E(\alpha)D(\alpha)e(-N\alpha)\,d\alpha\right|=o(N)
$$

uniformly in $N,t,y$ and the desired hard intervals. It is genuinely a signed correlation: the major arcs have no surviving main term to subtract or estimate. Even for $u,v$ both prime and in fixed proportional windows about $\sqrt N$, the theorem supplies no bound on this minor integral. It applies to that case simply by retaining the true prime restriction inside $E$, not by substituting a prime model. No estimate for weak S is implied.
