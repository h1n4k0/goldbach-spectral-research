# The actual additive constant-mode profile on the full polynomial-width critical shell

Let $N$ be even, $X=\sqrt N$, $L=\log N$, and $R=\operatorname{rad}N$. Use the actual complementary polynomial and shell of [the preceding unrestricted-radical profile](weak-s-type-ii-critical-prime-unrestricted-radical-constant-profile.md). In particular

$$
 D_m=\mathbf1_{N-y\le m<N/2}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                       (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_mD_m e(\alpha m),\qquad e(z)=e^{2\pi iz}.
$$

Here $N/2\le y\le9N/16$, $I_k$ is a hard interval with the genuine restriction $k>t\ge N^{.49999}$, and $I_d\subset[X,\infty)$ is any hard interval. We always intersect $I_d$ with $[X,N/(2t))$, without removing any actual contributions. This is the whole original polynomial-width range, not a logarithmic width assumption. The three hard cut parameters may move independently with $N$.

Set $\mathcal Q=[.8X,.9X]\cap\mathbb P$. The energies $\mathcal E_N(D)$ and $\mathcal E_N^0(D)$ are the squared sample sums at $a/q+\beta$, $q\in\mathcal Q$, $1\le a<q$, $|\beta|\le1/(10N)$, respectively without and with orthogonal projection off the constant in each group of nonzero numerators. The variable $\beta$ is integrated with Lebesgue measure. Define

$$
 \kappa_N=y/N,\qquad \mathcal D_N=I_d/X,\qquad \mathcal K_N=I_k/X,\qquad
 \mathfrak d(M)=\zeta(2)^{-1}\prod_{p\mid M}(1+1/p)^{-1},
 \qquad w(r)=\prod_{p\mid r}(1+1/p)^{-1}.
$$

For $\xi\in[.8,.9]$, $|\eta|\le.1$, keep the same normalized profile at these true cuts:

$$
 \Psi_N(\xi,\eta)=-
     \sum_{\substack{r\ge1,\ (r,N)=1\\r\xi\in\mathcal D_N}}\!
         \mu(r)w(r)
         \int_{\mathcal K_N\cap[(1-\kappa_N)/(r\xi),\,1/(2r\xi)]}
                        e(\eta r\xi z)\,dz .
 \tag{1}
$$

An empty integral is zero. The long cutoff keeps its literal endpoint convention; short endpoints do not change the real integral.

**Theorem.** Unconditionally and uniformly over all even $N$ and the true moving cut parameters, for every fixed $A>0$,

$$
 \frac{L}{N\mathfrak d(R)^2}\big(\mathcal E_N(D)-\mathcal E_N^0(D)\big)
  =
   \int_{.8}^{.9}\int_{-.1}^{.1}
        \frac{L}{\log(X\xi)}\,\xi\,|\Psi_N(\xi,\eta)|^2\,d\eta\,d\xi
   +O_A(L^{-A}).
 \tag{2}
$$

In particular $\mathcal E_N(D)-\mathcal E_N^0(D)\ll N/L$ uniformly, with no restriction on $R$. It is also possible to replace $L/\log(X\xi)$ by $2$ in (2) with error $O((1+\log L)^2/L)$ in the normalized formula. The order $N/L$ for the unnormalized difference is attained in the earlier fixed-radical witness. This result isolates exactly the genuine additive constant mode on this single shell; it does not bound the centered energy alone, a signed prime pairing, or Hypothesis S.

## 1. The original units and the uniform squarefree count

Put $Z_q(\beta)=\sum_{q\mid m}D_m e(\beta m)$. The true mean over the nonzero numerators is $(qZ_q(\beta)-D(\beta))/(q-1)$, by the elementary sum of $e(am/q)$ over $1\le a<q$. Hence the true energy difference is the integrated squared norm of this mean with weights $q-1$. The [hard-value proof, §1](weak-s-type-ii-critical-prime-unrestricted-radical-constant-profile.md#1-the-exact-mean-and-the-ordinary-hard-value) already proves $\sup_{\alpha}|D(\alpha)|\ll_H NL^{-H}$ for any fixed $H$ on the full original width, by applying masked Davenport at fixed $k$, real divisor scale $U=N/k$, and exact mask $kN$. It does not require a radical cap or any smoothing. The constants in this use of Davenport need not be effective. Thus the squared norm of the contribution $D(\beta)/(q-1)$ is $O_H(NL^{-1-2H})$, since $\sum_q(q-1)^{-1}\ll L^{-1}$ and the $\beta$ interval has length $1/(5N)$.

On actual support $k<X/2<q$, so $q\mid m$ means $d=rq$. The effective cutoff gives $r\ll N^{.00001}=X^{.00002}$. For $q\nmid N$ one has $q\nmid r$ for all large $N$, $\mu(rq)=-\mu(r)$, and the exact remaining unit conditions are $(r,N)=1$ and $(k,Rr)=1$. Accordingly

$$
 Z_q(\beta)=-\!\!\sum_{\substack{r\ge1,\ (r,N)=1\\rq\in I_d}}\!
      \mu(r)\!\!\sum_{\substack{k\in I_k,\ N-y\le rqk<N/2\\(k,Rr)=1}}\!
                      \mu^2(k)e(\beta rqk) .                         \tag{3}
$$

For a real hard prefix endpoint $V_0\in[0,X]$ and polynomial-size $M$, the squarefree-unit count in [the preceding uniform count, §2](weak-s-type-ii-critical-prime-unrestricted-radical-constant-profile.md#2-the-uniform-genuinely-nonunit-count) is

$$
 \sum_{\substack{k\le V_0\\(k,M)=1}}\mu^2(k)
      =\mathfrak d(M)V_0+
                  O\!\left(\tau(\operatorname{rad}M)(1+\sqrt{V_0})\right).
$$

Indeed expand over square divisors $b^2$ with $(b,M)=1$, use the exact finite inclusion count for the remaining units, and extend the absolutely convergent density at tail cost $O(1+\sqrt{V_0})$. Here $M=Rr\ll N^{1+.00001}$, so the divisor-function bound is $N^{o(1)}$ uniformly. In each term of (3) the phase has bounded variation on its actual short interval: $|\beta|N\le.1$ and $rqk<N/2$ throughout. Use two hard prefixes and Abel, including any isolated endpoint. Consequently the error after summing the $r$ labels is $O(X^{1/2+.00002+o(1)})$, which is $O(X^{3/5})$ for large $N$. On $(r,N)=1$ the density is exactly $\mathfrak d(Rr)=\mathfrak d(R)w(r)$, so with $\xi=q/X$ and $\eta=\beta N$ this proves

$$
       Z_q(\beta)=X\mathfrak d(R)\Psi_N(q/X,\beta N)+O(X^{3/5})
                    \qquad(q\nmid N).                                \tag{4}
$$

For $q\mid N$ the exact $Z_q$ is zero. Only $O(1)$ primes in the shell can divide $N$.

## 2. A signed reciprocal bound for the real profile

A crude absolute harmonic sum over polynomially many $r$ labels would not give a bounded unnormalized profile. To keep the actual sign, let $V(R)=\varphi(R)/R$ and $a_N(r)=\mu(r)w(r)\mathbf1_{(r,N)=1}$. There is an exact multiplicative convolution $a_N=\mu*g_N$, with

$$
 g_N(1)=1,\qquad
 g_N(p^j)=
 \begin{cases}
     1/(p+1),&p\nmid N,\\
     1,&p\mid N,
 \end{cases}\qquad j\ge1 .
$$

At an allowed prime this follows by dividing the Euler factor $1-\frac{p}{p+1}z$ by $1-z$; at an excluded prime the numerator is $1$. Thus $g_N$ is nonnegative and

$$
       \sum_{n\ge1}\frac{g_N(n)}n\ll V(R)^{-1}.
$$

The local factors outside $R$ are $1+1/(p^2-1)$ and their product converges; inside $R$ the factor is $(1-1/p)^{-1}$. Also $\sum_{n\le v}\mu(n)/n=O(1)$ for all real $v\ge1$, since $\sum_{n\le v}\mu(n)\lfloor v/n\rfloor=1$ and subtracting the fractional parts costs at most $v$. Applying the convolution therefore gives the uniform signed reciprocal prefix bound

$$
                         \sum_{r\le v}\frac{a_N(r)}r\ll V(R)^{-1}.
 \tag{5}
$$

For fixed $\xi,\eta$ change variable $x=r\xi z$ in each term of (1). The remaining multiplier after $1/(r\xi)$ is pulled outside is

$$
   f_{\xi,\eta}(r)=\mathbf1_{r\xi\in\mathcal D_N}
       \int_{[1-\kappa_N,1/2]\cap r\xi\mathcal K_N} e(\eta x)\,dx .
$$

As a function of positive real $r$ it has sup norm and total variation $O(1)$ uniformly in the true cuts. In detail, the two endpoints of the positive cofactor interval, multiplied by $r\xi$ and clipped to $[1-\kappa_N,1/2]$, are ordered nondecreasing functions of $r$, each of variation at most the length of that fixed physical interval. This representation gives zero also when the unclipped intersection is empty. The integral is a difference of primitive evaluations at these clipped endpoints, and the outer hard long gate adds at most two jumps. If the cofactor interval is empty the multiplier is zero. Strict endpoints cause no additional cost. Consequently Abel in (5) gives

$$
       \sup_{\xi,\eta}|\Psi_N(\xi,\eta)|\ll V(R)^{-1},
       \qquad
       \sup_{\xi,\eta}|\mathfrak d(R)\Psi_N(\xi,\eta)|\ll1,             \tag{6}
$$

because $\mathfrak d(R)/V(R)=\zeta(2)^{-1}\prod_{p\mid R}(1-p^{-2})^{-1}\le1$.

For clarity, the elementary uniform lower bound $\mathfrak d(R)\gg L^{-1}$ already suffices for all normalized error estimates. It follows by bounding the product for $p\le L$ below by the product over all integers from $2$ to $\lfloor L\rfloor$, and using $\sum_{p\mid R,\ p>L}1/p\ll1$. The sharper $V(R)\gg(1+\log L)^{-1}$ used only to replace the prime-density weight follows from the standard Mertens product up to $L^2$ and $\sum_{p\mid R,\ p>L^2}1/p\ll L^{-1}$.

## 3. Normalize the true mode and perform the ordinary prime sum

By (6), the unnormalized main term in (4) is $O(X)$. Its squared mean-mode norm is $O(N/L)$ using $\sum_{q\in\mathcal Q}q\ll X^2/L$ and the length $1/(5N)$. The $O(X^{3/5})$ pointwise error in (4), multiplied by $q/(q-1)$ for the group mean, contributes $O(X^{6/5}/L)$ in squared norm. After the normalization in (2) this is power-small, even in the cross term with the main profile, by $\mathfrak d(R)\gg L^{-1}$. Adding the $O(1)$ missing profile samples with $q\mid N$ costs at most $O(L^3/X)$ normalized because of (6). The ordinary hard-value squared error was $O_H(NL^{-1-2H})$; after normalization its own norm and its cross term with the main profile can be made as small as any fixed log power by choosing $H$. These norm comparisons use the actual group mean, not an auxiliary character term.

Change variables $d\beta=d\eta/N$, use $X^2=N$, and replace $q^2/(q-1)$ by $q$ at normalized power-small cost (there are $O(X/L)$ primes and $\sup|\Psi_N|\ll L$). The left side of (2) is now

$$
       \frac{L}{X}\sum_{q\in\mathcal Q}F_N(q/X)+O_A(L^{-A}),
       \qquad F_N(\xi)=\xi\int_{-.1}^{.1}|\Psi_N(\xi,\eta)|^2\,d\eta .
 \tag{7}
$$

For the moving profile, an individual $r$ term of (1) has sup and variation $O(1/r)$ as a function of $\xi$, uniformly in $\eta$. The physical cofactor interval has length $O(1/r)$, its endpoints move with Lipschitz norm $O(1/r)$, and the derivative of the phase on the common part is $O(1)$ because $rz\ll1$. The hard long gate adds only two possible jumps, and clipping to the actual cofactor interval cannot enlarge the Lipschitz loss. There are $r\ll X^{.00002}$, so the sup and variation of $\Psi_N$ are $O(L)$ even by absolute summation. The product variation inequality thus gives $\|F_N\|_\infty+\operatorname{Var}(F_N)\ll L^2$. Use the unconditional quantitative PNT in the form $\pi(v)=\operatorname{li}(v)+O_H(v(\log v)^{-H})$, for example [Johnston–Yang, Corollary 1.3](https://arxiv.org/pdf/2204.01980v2#page=2), and apply partial summation with this uniform variation bound:

$$
    \sum_{q\in\mathcal Q} F_N(q/X)
       =X\int_{.8}^{.9}\frac{F_N(\xi)}{\log(X\xi)}\,d\xi
                      +O_H(XL^{2-H}).
$$

This comparison is valid for any of the literal endpoint values. One may equivalently use hard prefix differences at jumps; the endpoint cost is bounded by the same discrepancy times the variation. Taking $H$ large in (7) proves (2).

For the asserted unnormalized bound apply (6) to (2). For the coarser normalized formula use $L/\log(X\xi)=2+O(1/L)$ and $\sup|\Psi_N|\ll1+\log L$ from (6) and Mertens. Finally, the fixed-radical example of [the true first odd transition](weak-s-type-ii-critical-prime-true-constant-transition.md) at $R=2$ and $I_d/X=[2.41,2.49]$ gives a strictly positive constant after normalizing by $L/N$, so the uniformly valid order $N/L$ for this specific mode cannot be improved. No conclusion about the remaining centered energy follows.
