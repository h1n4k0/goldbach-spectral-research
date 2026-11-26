# The actual constant-mode profile at arbitrary even targets

Let $N$ be even, $X=\sqrt N$, $L=\log N$, and $R=\operatorname{rad}N$. Write $e(z)=e^{2\pi iz}$, $\mathcal Q=[.8X,.9X]\cap\mathbb P$, and use the [genuine critical-shell polynomial](weak-s-type-ii-critical-prime-bounded-radical-davenport-transport.md). Thus

$$
 D_m=\mathbf1_{N-y\le m<N/2}
         \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                          (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_mD_m e(\alpha m).
$$

Fix $C>1,\gamma\ge0$. Let $I_d\subset[X,CXL^\gamma]$ and $I_k$ be arbitrary hard intervals, with $I_k$ including the original $k>t\ge N^{.49999}$, and let $N/2\le y\le9N/16$. All these endpoints may vary independently with $N$. Let $\mathcal E_N(D)$ and $\mathcal E_N^0(D)$ be the squared energies at $a/q+\beta$, $q\in\mathcal Q$, $1\le a<q$, $|\beta|\le1/(10N)$, respectively without and with projection off the constant in each group of nonzero numerators. This result concerns their difference only.

Put $\kappa_N=y/N$, $\mathcal D_N=I_d/X$, $\mathcal K_N=I_k/X$, and

$$
  \mathfrak d(M)=\frac1{\zeta(2)}\prod_{p\mid M}(1+1/p)^{-1},
        \qquad w(r)=\prod_{p\mid r}(1+1/p)^{-1}.
$$

For $\xi\in[.8,.9]$, $|\eta|\le.1$, define the real-coordinate profile

$$
 \Psi_N(\xi,\eta)=-\!\!\sum_{\substack{r\ge1,\ (r,N)=1\\r\xi\in\mathcal D_N}}
       \mu(r)w(r)
       \int_{\mathcal K_N\cap[(1-\kappa_N)/(r\xi),\,1/(2r\xi)]}
                    e(\eta r\xi z)\,dz .                             \tag{1}
$$

An empty integration interval contributes zero; the short-interval endpoint convention does not affect the integral. The displayed long endpoint convention is the original one.

**Theorem.** Uniformly in even $N$ and the actual moving cuts just stated, with no radical size condition,

$$
 \frac{L}{N\mathfrak d(R)^2}\big(\mathcal E_N(D)-\mathcal E_N^0(D)\big)
   =
   2\int_{.8}^{.9}\int_{-.1}^{.1}\xi|\Psi_N(\xi,\eta)|^2\,d\eta\,d\xi
      +O_{C,\gamma}\!\left(\frac{(1+\log L)^2}{L}\right).
 \tag{2}
$$

This is unconditional. It is not a bound on the centered energy or a signed covariance, nor does it refer to the artificially completed residue-zero term of a character calculation.

## 1. The exact mean and the ordinary hard value

For each $q,\beta$ put $Z_q(\beta)=\sum_{q\mid m}D_m e(\beta m)$. The sum of $e(am/q)$ over $1\le a<q$ is $q-1$ on $q\mid m$ and $-1$ otherwise. Thus the exact group mean is

$$
                     \frac{qZ_q(\beta)-D(\beta)}{q-1}.                 \tag{3}
$$

The difference of the two shell energies is precisely the squared norm of this mean, with weights $q-1$ and the stipulated $\beta$ integration.

The literal hard polynomial satisfies $\sup_\alpha |D(\alpha)|\ll_A NL^{-A}$ for every fixed $A>0$, uniformly even up to the original polynomial divisor width. Indeed fix $k$ on true support and put $U=N/k$. Then $2X<U\le N^{.50001}$, the true $d$ interval is the intersection of $I_d$ with $[(1-\kappa_N)U,U/2)$, and the actual sign is $\mu(d)$ with phase $e(\alpha kd)$ and mask $(d,kN)=1$. If $k$ fails its own unit test there is simply no contribution. Apply [the masked Davenport argument](weak-s-type-ii-critical-prime-bounded-radical-davenport-transport.md#2-davenport-cancellation-in-the-exact-completed-determinant) with the polynomial-size mask $M=kN\le N^{3/2}$. In its exact mask-smooth convolution, the labels $b\le\sqrt U$ divide hard prefix endpoints still at polynomial scale with logarithms comparable to $L$. Their reciprocal cost is $\ll L$, so arbitrary Davenport log savings persist. For $b>\sqrt U$, count without cancellation and use Rankin at $1/4$:

$$
 U\sum_{\substack{b>\sqrt U\\p\mid b\Rightarrow p\mid M}}b^{-1}
       \le U^{7/8}\prod_{p\mid M}(1-p^{-3/4})^{-1}
       =U^{7/8+o(1)} .
$$

For this uniform Euler estimate, count all integers up to $L^2$ in the small-prime logarithm, giving $O(L^{1/2})$, and use $O(L)$ prime factors for $p>L^2$, each costing $O(L^{-3/2})$. Consequently the hard $d$ sum is $O_A(UL^{-A})$ for every fixed exponent, and summing $U=N/k$ over the permitted $k$ costs at most $O(NL)$ before the adjustable log saving. This proves the assertion for the literal $D$, without smoothing.

We will use the simple uniform lower bound $\mathfrak d(R)\gg L^{-1}$. For primes at most $L$ one can bound their product by the product over all integers from $2$ to $\lfloor L\rfloor$. For larger prime divisors of $R$, their reciprocal sum is $O(1)$ since their number is $O(L)$ and each exceeds $L$. Thus the density normalization costs only a fixed power of $L$. The term $D(\beta)/(q-1)$ in (3) has squared norm $\ll_A NL^{-1-2A}$ by $\sum_q(q-1)^{-1}\ll L^{-1}$ and $|\beta|\le1/(10N)$, so it is negligible to arbitrary log accuracy after normalization.

## 2. The uniform genuinely nonunit count

For $q\nmid N$, on actual support $k<X/2<q$, and $q\mid m$ if and only if $d=rq$. We have $r\ll_C L^\gamma$, hence $q\nmid r$ for large $N$. The exact changes in the two masks are $(r,N)=1$ and $(k,Rr)=1$, and $\mu(rq)=-\mu(r)$. Thus

$$
 Z_q(\beta)=-
   \sum_{\substack{r\ge1,\ (r,N)=1\\rq\in I_d}}
    \mu(r)\!\!\sum_{\substack{k\in I_k,\ N-y\le rqk<N/2\\(k,Rr)=1}}
                          \mu^2(k)e(\beta rqk).                       \tag{4}
$$

For any real $V\in[0,X]$, the squarefree count in the mask $M=Rr$ is

$$
 \sum_{\substack{k\le V\\(k,M)=1}}\mu^2(k)
         =\mathfrak d(M)V+
            O\!\left(\tau(\operatorname{rad}M)(1+\sqrt V)\right).      \tag{5}
$$

This follows by expanding $\mu^2(k)$ over actual square divisors $b^2$ with $(b,M)=1$, and counting the remaining $M$-units by finite inclusion, at floor cost $O(\tau(\operatorname{rad}M))$ on each $b$. The convergent density's tail when $b>\sqrt V$ is $O(1+\sqrt V)$ after multiplication by $V$, and the local factor at each excluded prime is $(1-1/p)/(1-1/p^2)=(1+1/p)^{-1}$. The bound is uniform: $\tau(\operatorname{rad}M)=N^{o(1)}$ since $M\ll_C NL^\gamma$ and $\tau(n)\ll_\epsilon n^\epsilon$ for every $\epsilon>0$. The latter bound follows by multiplying $(j+1)/p^{\epsilon j}$ over prime powers $p^j\|n$, since for all but finitely many primes $j+1\le2^j\le p^{\epsilon j}$ and the quotient at each remaining prime is bounded for all $j$.

For each $r$ the short interval in (4) has endpoints at most $X/2$, and the phase has uniformly bounded variation on the **physical** interval of that term because $rqk\le N/2$ and $|\beta|N\le .1$. Abel summation in (5) thus gives error $X^{1/2+o(1)}$ per term, including hard endpoint choices. Since $r\ll_C L^\gamma$, summing the errors retains that size. On $(r,N)=1$ the density factors exactly as $\mathfrak d(Rr)=\mathfrak d(R)w(r)$. With $\xi=q/X,\ \eta=\beta N$, the rescaling $k=Xz$ therefore gives

$$
       Z_q(\beta)=X\mathfrak d(R)\Psi_N(\xi,\eta)+O(X^{1/2+o(1)})
                   \qquad(q\nmid N).                                 \tag{6}
$$

All implicit bounds here and below are uniform in the actual cuts.

For $q\mid N$, $Z_q(\beta)=0$ exactly by the unit condition, and only $O(1)$ primes of $\mathcal Q$ can divide $N$ since they are proportional to $X$. Each summand in (1) is $O(1/r)$, so $\sup|\Psi_N|\ll_C 1+\log(2+L^\gamma)\ll_{C,\gamma}1+\log L$. The main term in (6) has squared mean-mode norm $O((N/L)\mathfrak d(R)^2(1+\log L)^2)$. The error in (6) has squared norm $O(X^{1+o(1)}/L)$ by $\sum_q q\ll X^2/L$. After normalization it is power-small, also in the cross term with this main term, using $\mathfrak d(R)\gg L^{-1}$. Adding the absent $q\mid N$ samples to the profile expression costs normalized $O((L/X)(1+\log L)^2)$, by the bounded number of such primes. Combining (3), the ordinary hard-value estimate and (6), and using $d\beta=d\eta/N$ and $X^2=N$, the normalized energy difference becomes

$$
   \frac{L}{N}\sum_{q\in\mathcal Q}\frac{q^2}{q-1}
         \int_{-.1}^{.1}|\Psi_N(q/X,\eta)|^2\,d\eta
      + O_{C,\gamma}(L^{-2}).                                        \tag{7}
$$

For the ordinary hard-value loss choose the Davenport exponent large enough that its normalized norm and the cross term are $O(L^{-2})$. The other errors were power-small and can be included here.

## 3. Uniform ordinary prime averaging and the first odd multiple

Replacing $q^2/(q-1)$ by $q$ in (7) costs $O((1+\log L)^2/X)$. To take the prime sum with genuinely moving cut windows, each individual $r$ contribution in (1) as a function of $\xi$ has bounded variation and sup norm $O(1/r)$, uniformly in $|\eta|\le.1$. Indeed the underlying physical short interval has length $O(1/r)$, and its endpoints are $O(1/r)$-Lipschitz in $\xi$ after intersecting with the fixed-for-$N$ hard cofactor interval. The phase derivative on this support is $O(1)$ because $rz\ll1$. The outer long indicator $r\xi\in\mathcal D_N$ adds at most two jumps of size $O(1/r)$, regardless of endpoint convention. Thus the bounded variation norm of

$$
  F_N(\xi)=\xi\int_{-.1}^{.1}|\Psi_N(\xi,\eta)|^2\,d\eta
$$

on $[.8,.9]$ is $O_{C,\gamma}((1+\log L)^2)$ by summing $1/r$ and using the product variation inequality.

For ordinary prime counting use the unconditional quantitative prime number theorem, for example [Johnston–Yang, Corollary 1.3](https://arxiv.org/pdf/2204.01980v2#page=2), which gives $\pi(v)=\operatorname{li}(v)+O_A(v(\log v)^{-A})$ for every fixed $A>0$. Partial summation with the uniform total variation bound yields

$$
 \sum_{q\in\mathcal Q}F_N(q/X)=
      X\int_{.8}^{.9}\frac{F_N(\xi)}{\log(X\xi)}\,d\xi
             +O_{C,\gamma,A}\big(XL^{-A}(1+\log L)^2\big).
$$

This also holds at hard included or excluded jump values, by representing such values with prefix differences, each subject to the same discrepancy bound. Multiply by $L/X$ as required by (7). Since $L/\log(X\xi)=2+O(L^{-1})$ uniformly in $\xi$, this proves (2), including the uniform quantified remainder.

For a fixed example take $I_d=[2.41X,2.49X]$, $I_k=[.17X,.22X]\cap(N^{.49999},\infty)$ and $y=9N/16$. Exactly the possible $r=3$ term in (1) meets the shell: $r$ is odd and $r=1,5,7,\ldots$ fail the long gate. If $3\nmid N$ it contributes on $\xi\in(2.41/3,2.49/3)$. At $\eta=0$ its magnitude there is $w(3)/(16\cdot3\xi)>0$, since the entire physical cofactor interval lies inside the actual cofactor gate for sufficiently large $N$. Thus along these even targets the true difference is asymptotic to a fixed positive constant times $\mathfrak d(R)^2N/L$. If $3\mid N$, the genuine $q$-nonunit term is identically zero on the shell, by (4) and the true unit gate for $q\mid N$. The ordinary estimate in §1 then gives $\mathcal E_N(D)-\mathcal E_N^0(D)\ll_A NL^{-A}$ for every fixed $A$. This distinction is only for the actual additive constant mode.
