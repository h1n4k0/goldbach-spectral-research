# Removing three-small-factor integers from the actual central long sum

**Scope.** At the smaller subpower prime cutoff specified below, a weighted upper sieve reduces the complete-orbit deletion threshold to **three** small factors in the [broad smooth central split](spectral-broad-split-rare-support.md). The two cutoff statements do not assert inclusion of one deleted set in the other. The new estimate bounds weighted complete signed orbits on genuine integers at every fixed even $N$; it is not just a count of their support. The contributions with zero, one or two such primes are not estimated, so this does not prove central positivity or Hypothesis S.

Use the same $0<a<b<1/2$, $I=(1/2,9/16]$, and $F_N,D_N$, with $L=\log N$, $\ell=\log L$, $S=\mathfrak S(N)$. In this note take the smaller subpower cutoff

$$
 z=\exp(L/\ell^{12}),\qquad
 \omega=\omega_z(m)=\#\{p\le z : p\nmid N,\ p\mid m\},
 \qquad
 \omega_>(m)=\#\{p>z:p\mid m\},
$$

with $p$ always prime. Use $m=N-n$ and denote $\mathbb E_N[f]=N^{-1}\sum_{n/N\in I,\,(n,N)=1}\Lambda(n)W(n/N)f(N-n)$ for a fixed real central weight $W$ of bounded variation. The short main term is still $S\int W$, since the split itself has not changed. For every sufficiently large even $N$ we prove

$$
 \left|\mathbb E_N[D_N(m)\mathbf1_{\omega\ge3}]\right|
      \ll_{a,b}\|W\|_\infty\,\ell^{-2},
 \qquad
 G_W=S\int W-\mathbb E_N[D_N(m)\mathbf1_{\omega\le2}]
        +O_{a,b}(\|W\|_{\rm BV}\ell^{-2}).
 \tag{1}
$$

As before, the error bounds the sum of absolute values after taking each complete signed orbit, not the sum of its unsigned individual divisors.

## 1. A weighted moment with the true shifted primes

For clarity first assume $W\ge0$ and put $v=1/\ell$. The needed auxiliary bound is

$$
 \mathbb E_N\big[\mu^2(m)\, 2^{\omega_>(m)}v^{\omega_z(m)}\big]
       \ll \|W\|_\infty\,\frac{\ell^{25}}{L}.
 \tag{2}
$$

The analogous bound with both $\mu^2(m)$ and $2^{\omega_>(m)}$ omitted is $O(\|W\|_\infty\ell^{13}/L)$. All constants in these bounds are uniform in $N$.

For squarefree $m$, let $m_>$ be the product of its distinct primes $>z$. Pair $d\mid m_>$ with $m_>/d$; at least half of the resulting divisors satisfy $d\le\sqrt{m_>}\le\sqrt N$. Therefore

$$
 \mu^2(m)2^{\omega_>(m)}
       \le 2\!\sum_{\substack{d\mid m,\ d\le\sqrt N\\
                         d\ {\rm squarefree}\\p\mid d\ \Rightarrow\ p>z}}1 .
 \tag{3}
$$

The inequality also holds when the left side is zero. Keep the coprime $d$'s, the only ones on the unit support. Fix one such $d$ and write $m=d u$, where $u$ varies in the exact central interval of length $N/(16d)$, with the original half-open endpoints. Put $U=N/d$, so $U\ge\sqrt N$. Since $d$ has no small primes, $\omega_z(m)=\omega_z(u)$.

Use the upper-bound fundamental sieve for the integer variable $u$. For every prime $p<Y=U^{1/100}$ exclude $N-du\equiv0\bmod p$. Additionally, select each prime $p\le z$, $p\nmid N$, with probability $1-v$, independently, and exclude $u\equiv0\bmod p$ when it is selected. This finite randomization is only a way to average deterministic upper bounds: the probability to pass the extra exclusions at a given $u$ is exactly $v^{\omega_z(u)}$. For sufficiently large $N$, $z<Y$ uniformly in $d$. The central prime $n=N-du$ is $>N/2>Y$, so it always passes the primality-root exclusion.

If $p\mid d$, then $p\nmid N$, the primality root is absent and no extra root is selected. Otherwise the primality root is the single class $N\bar d\bmod p$; at every selected prime it is distinct from the extra root because $(p,Nd)=1$. In particular the two-root case never occurs at $2$, since $2\mid N$. Hence the local density $g(p)=\nu(p)/p$ has $0\le\nu(p)\le2$, $g(2)\le1/2$, and $g(p)\le2/3$ for $p>2$. The dimension-2 upper product condition holds with an absolute constant by Mertens, as in [the fundamental upper sieve, Tao Corollary 19 and condition (22)](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/). At level $D=U^{1/2}=Y^{50}$, the Chinese remainder theorem gives $O(2^{\omega(q)})$ remainder for each squarefree sieve modulus $q\le D$, by counting the corresponding residue classes in the interval (including all zero-root cases). Summing the remainders is $O(U^{1/2}\log(2U))$, using $2^{\omega(q)}\le\tau(q)$. This bound is uniform in the selected set.

For a fixed selected subset $\mathcal J$, the sieve therefore majorizes its surviving $u$ count by

$$
 \ll
  \frac{U}{\log Y}\frac d{\varphi(d)}
          \prod_{p\in\mathcal J}\left(1-\frac1{p-1}\right)
       + U^{1/2}\log(2U).
$$

The first root product uses $\prod_{p<Y,\,p\nmid d}(1-1/p)\ll (d/\varphi(d))/\log Y$; a selected second root has the displayed ratio of local factors. Averaging the independent selections replaces the last product by

$$
 \prod_{\substack{p\le z\\p\nmid N}}
      \left(1-\frac{1-v}{p-1}\right)
   \le e^{-(1-v)h}\ll \frac{\ell^{13}}L,\qquad
 h=\sum_{\substack{p\le z\\p\nmid N}}\frac1{p-1}.
$$

Indeed $\log\log z=\ell-12\log\ell$, and $\sum_{p\mid N}1/(p-1)\le\log\ell+O(1)$: below $L$ use reciprocal-prime Mertens, and above $L$ count prime factors by their product. The difference between $1/(p-1)$ and $1/p$ has bounded total sum. Thus $h\ge\ell-13\log\ell-O(1)$, while $vh$ is bounded.

Include the normalized prime weight $\Lambda(n)W(n/N)/N\le L\|W\|_\infty/N$, and sum over the $d$'s in (3). Because $\log Y\asymp L$, the main contribution is at most

$$
 \ll \|W\|_\infty\,\frac{\ell^{13}}L
         \sum_{\substack{d\le\sqrt N,\ d\ {\rm squarefree}\\p\mid d\Rightarrow p>z}}
              \frac1{\varphi(d)}
 \ll \|W\|_\infty\,\frac{\ell^{25}}L.
$$

The last sum is bounded by $\prod_{z<p\le\sqrt N}(1+1/(p-1))\ll L/\log z=\ell^{12}$ by Mertens. Summing the sieve remainders costs $O(\|W\|_\infty L^2N^{-1/4})$, since $\sum_{d\le\sqrt N}(N/d)^{1/2}\ll N^{3/4}$. The proper prime powers in $n$ contribute $O_\epsilon(\|W\|_\infty N^{-1/2+\epsilon}L)$ directly, using $\mu^2(m)2^{\omega_>(m)}\le\tau(m)\ll_\epsilon N^\epsilon$ and $v^\omega\le1$. This proves (2). Taking just $d=1$ in the same sieve gives the stated unweighted variant; proper powers there also cost less. In particular the actual central Mangoldt mass with $\omega\le2$ is $O(\|W\|_\infty\ell^{15}/L)$ by $1_{\omega\le2}\le v^{-2}v^\omega$.

## 2. Use all the small factors before taking absolute values

Let $k=\lceil11\ell/\log\ell\rceil$. For $\omega\ge k$ use the old complete-$k$-orbit estimate with this smaller $z$: the bound only improves when the selected primes get smaller, and gives $O(\|W\|_\infty L^{-1})$ in the normalized sum. Thus it remains to handle $3\le j=\omega<k$. At squarefree $m$, split off **all** its $j$ distinct small factors. The orbit bases are now exactly the $d\mid m_>$, so there are $2^{\omega_>(m)}$ orbits. The Gevrey derivative estimate of the broad split gives

$$
 |D_N(m)|
   \ll_{a,b} L\,\mu^2(m)2^{\omega_>(m)}
            \left(\frac{C_{a,b}j^2}{\ell^{12}}\right)^j
   \le C'_{a,b} L\,\mu^2(m)2^{\omega_>(m)}\ell^{-27}v^j.
$$

The inequality uses $C_{a,b}k^2\le\ell^2$ for large $N$, and $\ell^{-10j}=\ell^{-9j}v^j\le\ell^{-27}v^j$ for $j\ge3$. The same bounds hold if the absolute value is taken per complete orbit before summing. Non-squarefree $m$ contribute zero.

Apply (2), with $|W|$ for a signed test. The normalized weighted sum over $3\le\omega<k$ is $O_{a,b}(\|W\|_\infty\ell^{-2})$. This proves the deletion in (1); applying the exact short-main term and bound for proper powers from the broad split proves the second assertion. The remaining coefficient, including $D_N(m)=-\log m$ for prime $m$, may still carry a nonnegligible signed weight despite the support bound. The method does not bound it or resolve Hypothesis S.
