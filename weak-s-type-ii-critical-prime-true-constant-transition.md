# The actual constant-mode energy and the first odd shell multiple

Let $N$ tend to infinity through even integers with a fixed radical $R=\operatorname{rad}N$, and put $X=\sqrt N$, $L=\log N$, and $e(z)=e^{2\pi iz}$. Use the genuine complementary coefficient of [the critical-shell setup](weak-s-type-ii-critical-prime-bounded-radical-davenport-transport.md), now at fixed proportional cuts

$$
 \begin{gathered}
 y=\kappa N,\qquad \frac12\le\kappa\le\frac9{16},\qquad
 I_d=[D_-X,D_+X],\qquad 1\le D_-\le D_+<\infty,\\
 I_k=[K_-X,K_+X]\cap(N^{.49999},\infty),
                  \qquad 0<K_-<K_+<\infty,\\
 D_m=\mathbf1_{N-y\le m<N/2}
      \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                       (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_m D_m e(\alpha m).
 \end{gathered}
$$

The short restriction $k>N^{.49999}$ is inactive for sufficiently large $N$ at these fixed cuts. Define $\mathcal E_N(D)$ and $\mathcal E_N^0(D)$ on $q\in[.8X,.9X]\cap\mathbb P$, $1\le a<q$, $|\beta|\le1/(10N)$, respectively before and after projection off the constant in each nonzero-numerator group.

For $\xi\in[.8,.9]$, $\eta\in[-.1,.1]$, define the exact limiting profile

$$
 \begin{split}
 \mathfrak d(M)&=\frac{1}{\zeta(2)}\prod_{p\mid M}(1+1/p)^{-1},\\
 G(\xi,\eta)&=-\!\!\sum_{\substack{r\ge1,\ (r,R)=1\\D_-\le r\xi\le D_+}}\!
        \mu(r)\mathfrak d(Rr)
        \int_{[K_-,K_+]\cap[(1-\kappa)/(r\xi),\,1/(2r\xi)]}
                        e(\eta r\xi z)\,dz .
 \end{split}
 \tag{1}
$$

The sum over $r$ is finite; an empty interval contributes zero. Open versus closed endpoints have no effect on the integral. The full energy minus its separately centered energy satisfies, **unconditionally**,

$$
 \lim_{N\to\infty}\frac{L}{N}\big(\mathcal E_N(D)-\mathcal E_N^0(D)\big)
       =2\int_{.8}^{.9}\int_{-.1}^{.1}\xi\,|G(\xi,\eta)|^2\,d\eta\,d\xi .
 \tag{2}
$$

This is a formula for the **actual additive constant mode**. It neither asserts a limit for each energy taken separately at these general cuts nor concerns an artificially completed character square, a signed prime pairing, or Hypothesis S.

## 1. Suppress the ordinary Fourier value on the true hard coefficient

For each $q,\beta$, put $Z_q(\beta)=\sum_{q\mid m}D_m e(\beta m)$. The ordinary mean on the nonzero-numerator group at this $q$ is exactly

$$
                 M_q(\beta)=\frac{qZ_q(\beta)-D(\beta)}{q-1}.
 \tag{3}
$$

Indeed for $q$ prime the sum of $e(am/q)$ over $1\le a<q$ is $q-1$ when $q\mid m$ and $-1$ otherwise. Orthogonal projection off this mean gives the exact squared energy difference by integrating $\sum_q(q-1)|M_q(\beta)|^2$. We estimate $D(\beta)$ on the actual hard polynomial, rather than treating an artificial principal term as this mean.

In fact at the fixed divisor width,

$$
                 \sup_{\alpha\in\mathbb R}|D(\alpha)|\ll_A NL^{-A}
 \tag{4}
$$

for every fixed $A>0$ (with a constant permitted to depend on the fixed cuts). Fix $k$ on genuine support. Then $k<X/2$, and the remaining test in $d$ is a hard interval contained in $[D_-X,D_+X]$, obtained by intersecting $I_d$ with the exact physical cut divided by $k$. If $(k,N)\ne1$ there is no term. Otherwise the true mask on $d$ is $(d,kN)=1$, and the $d$ phase is $e(\alpha k d)$. Use [Davenport's unconditional estimate and the masked convolution, §2](weak-s-type-ii-critical-prime-bounded-radical-davenport-transport.md#2-davenport-cancellation-in-the-exact-completed-determinant), now with the polynomial-size mask $M=kN\le N^{3/2}$ rather than a logarithmic mask. The extension at this mask size follows directly: convolve $\mu$ with the indicator of integers supported on the primes of $M$, and for convolution labels $b\le\sqrt X$ use Davenport at the two divided integer-prefix endpoints and frequency $\alpha k b$. The endpoints are $\asymp X/b$ on a nonempty original hard interval, so their logarithms are $\asymp L$. The reciprocal label sum is at most $\sum_{b\le\sqrt X}b^{-1}\ll L$, which is harmless in an arbitrarily fixed log saving. For $b>\sqrt X$ count trivially to get at most a constant times

$$
  X\sum_{\substack{b>\sqrt X\\p\mid b\,\Rightarrow\, p\mid M}}\frac1b
       \le X^{7/8}\prod_{p\mid M}(1-p^{-3/4})^{-1}
       = X^{7/8+o(1)} .
$$

The uniform $o(1)$ follows by splitting the primes at $L^2$: the small-prime sum is $O(L^{1/2})$ even counting all integers up to $L^2$, and at most $O(L)$ remaining primes each cost $O(L^{-3/2})$ in the logarithm of the Euler product. The hard $d$ sum is therefore $O_A(XL^{-A})$, uniformly in $\alpha,k$ and either endpoint convention. Summing the $O(X)$ possible $k$ with the true $\mu^2(k)$ proves (4). This step needs neither smoothing nor a theorem on spherical or character-equivalent constants.

## 2. The true $q$-nonunits and the profile

Since $d\ge X$ and the physical upper endpoint is $m<N/2$, $k<X/2<q$. Thus $q\mid m$ is exactly $q\mid d$ on actual support, and then $d=rq$ for a positive integer $r\le D_+/.8$. For sufficiently large $N$, $q\nmid rR$, so $\mu(rq)=-\mu(r)$ even when $\mu(r)=0$. The remaining unit tests are $(r,R)=1$ and $(k,Rr)=1$. In particular no extra $q$-divisibility condition survives in the short factor. We have the exact formula

$$
 Z_q(\beta)=-
      \sum_{\substack{r\ge1,\ (r,R)=1\\rq\in I_d}}
       \mu(r)\!\!\sum_{\substack{k\in I_k,\ N-y\le rqk<N/2\\(k,Rr)=1}}\!
                     \mu^2(k)e(\beta rq k).
 \tag{5}
$$

For each fixed mask $Rr$, the number of squarefree units up to a real endpoint $V=O(X)$ is $\mathfrak d(Rr)V+O_{R,r}(\sqrt X+1)$. Indeed expand $\mu^2(k)=\sum_{b^2\mid k}\mu(b)$; the unit condition forces $(b,Rr)=1$, and the remaining unit count by finite inclusion has main density $\varphi(Rr)/(Rr)$ and bounded floor error. The tail past $b>\sqrt V$ in the absolutely convergent density costs $O(\sqrt V+1)$; its local factors give $\mathfrak d(Rr)$. Taking two prefixes and applying Abel to $e(\beta rq k)$ gives error $O_{R,r}(\sqrt X+1)$ uniformly here: its variation on the genuine support is $O(1)$ because $|\beta rq|X\ll_{D_+}1$. Put $\xi=q/X,\ \eta=\beta N$ and rescale $k=Xz$. Equation (5) becomes

$$
                  Z_q(\beta)=XG(\xi,\eta)+O_{R,D_+,K_+}(\sqrt X+1).
 \tag{6}
$$

In the energy of (3), the term $D(\beta)/(q-1)$ has squared norm $o(N/L)$ by (4), the $\beta$ length and $\sum_q1/(q-1)\ll1/L$. The error (6), in the term $qZ_q/(q-1)$, has squared norm $O(X/L)=o(N/L)$ since $\sum_q q\ll X^2/L$. The main term of (6) has squared norm $O(N/L)$ from boundedness of $G$, so norm triangle preserves its normalized energy. Its normalized squared value is exactly

$$
       \frac{L}{N}\sum_{q\in[.8X,.9X]\cap\mathbb P}
        \frac{q^2}{q-1}\int_{-.1}^{.1}|G(q/X,\eta)|^2\,d\eta ,
$$

using $X^2=N$ and $d\beta=d\eta/N$. Replacing $q^2/(q-1)$ by $q$ has negligible cost. The integrand in $q/X$ is bounded and continuous off the finite list of threshold endpoints $D_\pm/r$: the moving interval endpoints in (1) give continuous integrals on each piece. Ordinary prime-number asymptotics and a fixed Riemann partition therefore give (2), with the factor $L/\log X=2$.

When $R=2$, only odd $r$ are allowed; $r=1$ never occurs because $q<X\le d$. Thus there is no term before the first shell multiple $d=3q$, for example if $D_+<2.4$. There is a genuine positive constant at

$$
        [D_-,D_+]=[2.41,2.49],\qquad
        [K_-,K_+]=[.17,.22],\qquad \kappa=9/16 .
$$

For $\xi\in(2.41/3,2.49/3)\subset(.8,.9)$ only $r=3$ is admitted, and the entire physical cofactor interval $[(7/16)/(3\xi),1/(6\xi)]$ lies inside $[.17,.22]$. With $\mu(3)=-1$, at $\eta=0$ the profile is $\mathfrak d(6)/(16\cdot3\xi)>0$ there; joint continuity on the interior gives strict positivity of (2). The nonzero difference is an actual addition of order $N/L$ to the centered energy, not a lower bound for any signed statistic.
