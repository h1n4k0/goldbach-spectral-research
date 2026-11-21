# R23: the giant-prime / prime-cofactor piece cannot be discarded on its own

Keep the original wide-prefix labels from [R22](r22-compressed-wide-d.md): \(b_*=N^{3/40}\), \(Z_*=\lceil4b_*N\rceil\), \(D_*=\lfloor Z_*^{1/3}\rfloor\), \(Q=N^{7/8}\), and \(W=\prod_{\ell\le\log N,\ \ell\nmid N}\ell\) (prime indices in this product). Take \(J=[9/20,11/20]\). Inside the genuine rough–rough high-product component (both integers have at most one distinct prime factor of \(W\)), let \(C_N^{pp}\) be its further restriction to \(n/N,m/N\in J\) and to factorizations

\[
 n=rp,\quad m=sq,\qquad r,s,p,q\text{ prime},\qquad N^{1/10}\le r,s\le N^{1/5}.
\]

This is a restriction on the two **integers**; in it keep all genuine terms \(d\mid n,e\mid m,d,e>D_*\), \(de>Q\), the exact unit condition and original signs, with no new Beta model. For some absolute \(c_0,c_1,M>0\), for every sufficiently large real \(X\) there are at least \(c_0 X\) even integers \(N\in[2X,11X/5]\) such that

\[
 F(N):=\prod_{\ell\mid N,\ \ell\ {\rm prime}}(1+2/\ell)\le M,
 \qquad \|P_1 C_N^{pp}P_1\|\ge c_1.
 \tag{1}
\]

Here \(P_1\) is the physical prefix \(0<x\le1\) with the original cumulative log-kernel normalization. In particular the same lower bound holds for its Hilbert–Schmidt norm, and \(\mathfrak S(N)\ll F(N)\) is bounded on the moduli in (1). The estimate is **unconditional as a statement about this arithmetic kernel**. Local GRH(N) concerns the identification with the Hardy representation; using the R22 replacement of the true operator by the rough–rough remainder also uses global Dirichlet GRH. There is **no** lower bound here for the entire rough–rough remainder or \(T_N\), and no conclusion on S or R. Contributions outside this sector may cancel it.

## 1. The genuine cutoff retains precisely a fixed sign

On \(J^2\) the positive difference aliases \(n-m=jN,m-n=jN\) with \(j\ge1\) are impossible. The only sum alias is \(n+m=N\), which has sign minus. For even \(N>2\), a diagonal point on this line has \(n=m=N/2\) and fails the unit condition; the removed zero difference line is not used. On the sum line \((nm,N)=1\) is equivalent to \((n,m)=1\). All counted factors in the selected sector are odd for large \(N\). Also \(p,q\ge(9/20)N^{4/5}\), so the small and large factors are distinct, the factorization is unique on either side, and all four primes exceed \(\log N\). In particular both integers have **zero** prime factors from \(W\).

We have \(r,s<D_*<p,q\) for sufficiently large \(N\), since \(D_*\asymp N^{43/120}\). The only long divisors of \(n\) are \(p,rp\), and the only long divisors of \(m\) are \(q,sq\). Every such pair passes the exact original \(de>Q\) cut because \(pq\ge (9/20)^2N^{8/5}>Q\). Terms with \(d=n\) or \(e=m\) vanish by the cofactor logarithm. Hence the full divisor coefficient here is

\[
 \mu(p)\mu(q)\log r\log s=\log r\log s.
\]

It retains its sign throughout this entire sector, regardless of how the other rough–rough terms are grouped. Write \(V(N)\) for the sum of these positive weights over the ordered pairs satisfying \(n+m=N\), the ratio and prime-factor cuts, and \((n,m)=1\).

## 2. First moment with the exact unit condition

Fix \(X\) large and use only the common box

\[
 X\le n=rp\le 11X/10,
 \qquad 2X^{1/10}\le r\le X^{1/5},
 \qquad r,p\text{ prime}.
\]

As \(r\) varies here the endpoint \(X/r\) is always at least \(X^{4/5}\). By the prime number theorem on the interval \([X/r,11X/(10r)]\), uniformly throughout this range the number of \(p\)'s is \(\asymp X/(r\log X)\). By partial summation from the prime number theorem, \(\sum_{2X^{1/10}\le r\le X^{1/5},\ r\text{ prime}} (\log r)/r\asymp\log X\). Thus the total weight \(A_X\), with weight \(\log r\) on \(rp\), satisfies \(A_X\asymp X\).

A pair drawn from this same box has even sum \(N\in[2X,11X/5]\), has \(N^{1/10}\le r,s\le N^{1/5}\), and has \(n/N,m/N\in[10/21,11/21]\subset J\). Thus it lies in \(V(N)\) whenever it is coprime. To account for the exact unit condition, for any fixed prime factor \(\ell\) either in the small or large range, bound the total box weight of multiples of \(\ell\) by \(O(X\log X/\ell)\), simply counting the other factor as an integer in the box interval. The additive counting error is absorbed because every such \(\ell\ll X^{9/10}\). The small and large ranges are disjoint. Summing the squares of these bounds for \(\ell\ge2X^{1/10}\) gives

\[
 \sum_{\substack{n,m\ \text{in box}\\(n,m)>1}}(\log r)(\log s)
 \ll X^2(\log X)^2 \sum_{k\ge2X^{1/10}} k^{-2}
 \ll X^{19/10}(\log X)^2=o(X^2).
\]

Here and below all pairs are ordered, which agrees with the signed line measure. It follows that

\[
 \sum_{\substack{2X\le N\le 11X/5\\N\text{ even}}} V(N)\gg X^2.
 \tag{2}
\]

## 3. A uniform weighted second-moment majorant

Fix an even \(N\in[2X,11X/5]\) and eligible primes \(r,s\). Only \(r,s\nmid N\) and \(r\ne s\) can contribute to a unit pair. Solve \(rp+sq=N\) with

\[
 p=p_0+s t,\qquad q=q_0-r t,
 \qquad t\in\mathbb Z.
\]

The cuts in \(n,m\) reduce \(t\) to one interval of length \(H\ll X/(rs)\), possibly empty. Prime values satisfy \(p,q\gg X^{4/5}\). Sift their product up to \(z=X^{1/20}\). For a prime \(\ell\), let \(\nu(\ell)\) count the roots of the product in \(t\bmod\ell\). Away from \(rs\) both slopes are invertible, and their roots coincide precisely when \(\ell\mid N\). At \(\ell=r\) or \(s\), the constant form is nonzero (as \((rs,N)=1\)) and the varying form has one root. Thus \(\nu(\ell)=2\) for \(\ell\nmid Nrs\) and \(1\) otherwise; in particular \(\nu(2)=1\). For an eligible squarefree modulus \(d\), CRT gives \(H\nu(d)/d+O(\nu(d))\) points with product divisible by \(d\), where \(\nu\) is extended multiplicatively.

Apply the [Selberg upper-bound sieve, Theorem 13.1](https://kskedlaya.org/ant/chap-selberg.html#theorem-13-1) in the finite interval, with supported squarefree weights \(d<z\) and \(g(\ell)=\nu(\ell)/\ell\). The main term is at most \(H/G(z)\), where

\[
 G(z)=\sum_{d<z}\mu^2(d)\prod_{\ell\mid d}\frac{g(\ell)}{1-g(\ell)}.
\]

One may use the optimized weights \(|\rho(d)|\le1\) from that theorem: writing \(h(\ell)=g(\ell)/(1-g(\ell))\), their factor \(h(d)/g(d)=\prod_{\ell\mid d}(1+h(\ell))\) times \(\sum_{v<z/d,(v,d)=1}\mu^2(v)h(v)\) is at most \(G(z)\), by including all \(uv\) with \(u\mid d\). The counting errors are \(O(z^4)\) directly from \(\sum_{d,e<z}\nu([d,e])\le z^4\). All actual prime values are above \(z\), so this is an upper bound for the actual prime-pair count, even if we omit its additional unit restriction on \(p,q\) at this stage.

For the main term let \(a(k)=\mu^2(k)2^{\omega(k)}/k\). At primes not dividing \(Nrs\), \(h(\ell)=2/(\ell-2)\ge2/\ell\). Splitting each \(k\) into its prime factors dividing \(Nrs\) and those not dividing it gives

\[
 G(z)\ge \sum_{\substack{k<z\\(k,Nrs)=1}} a(k)
 \ge \frac{\sum_{k<z}a(k)}{\prod_{\ell\mid Nrs}(1+2/\ell)}
 \gg \frac{(\log z)^2}{F(Nrs)}.
\]

For completeness, the last unrestricted lower bound follows by taking squarefree products of primes at most \(z^\eta\), for a fixed small \(\eta>0\). Their full mass is \(\prod_{\ell\le z^\eta}(1+2/\ell)\gg(\log z)^2\), by comparison with the square of the Euler product \(\prod (1-1/\ell)^{-1}\); that product dominates \(\sum_{m\le z^\eta}1/m\). Under the resulting normalized mass law the average \(\log k\) is \(\sum_{\ell\le z^\eta}(2/(\ell+2))\log\ell=O(\eta\log z)\) by partial summation. Taking \(\eta\) sufficiently small ensures at least half the mass has \(k<z\).

Since \(X/(rs)\gg X^{3/5}\), the \(O(z^4)\) error is absorbed by \(X/(rs(\log X)^2)\). This upper bound is uniform even if the actual chosen \(t\)-interval is very small. Hence the prime pair count for each \(r,s\) is

\[
 \ll \frac{XF(Nrs)}{rs(\log X)^2}\ll\frac{XF(N)}{rs(\log X)^2}.
\]

Multiplying back by \(\log r\log s\) and summing, with \(\sum_{r\le(11X/5)^{1/5},\ r\text{ prime}}(\log r)/r\ll\log X\), gives

\[
 V(N)\ll XF(N).
 \tag{3}
\]

Finally, write \(u(\ell)=(1+2/\ell)^2-1\) on primes and extend \(u\) multiplicatively to squarefree integers (zero elsewhere). Since all coefficients are nonnegative,

\[
 \sum_{N\le 11X/5}F(N)^2
 \le (11X/5)\prod_\ell(1+u(\ell)/\ell)\ll X.
 \tag{4}
\]

This product converges because \(u(\ell)=O(1/\ell)\). Equations (3) and (4) give the weighted second-moment bound \(\sum_N V(N)^2\ll X^3\). More specifically, the contribution to (2) from \(F(N)>M\) is at most \(O(X^2/M)\). Fix \(M\) large enough that at least half of the lower bound (2) survives; then remove the terms \(V(N)<cX\) for a sufficiently small absolute \(c>0\). Each remaining term is \(O(MX)\) by (3), so there are \(\gg X\) remaining even \(N\). For these moduli \(V(N)\gg N\) and \(\mathfrak S(N)\ll F(N)\le M\), since for every prime \(\ell\ge5\) the standard Goldbach local inflation \((\ell-1)/(\ell-2)\) is at most \(1+2/\ell\), and the factor at \(3\) costs only an absolute constant.

## 4. Bounded physical test and scope of the obstruction

For the pure arithmetic component, the exact physical log kernel is \(2\pi\) times the cumulative of its atomic measure (with a factor \(\sqrt{uv}\) at \((u,v)=(n/N,m/N)\)) divided by \(xy\sqrt{w_N(x)w_N(y)}\), where

\[
 w_N(x)=\left((Nx)^{-2/\log N}+(Nx)^{-1/4}\right)^{-1}.
\]

Every atom above has measure \(-\log r\log s/N\) before the \(\sqrt{uv}\) factor. Choose a fixed nonnegative \(f\in C_c^\infty((2/5,3/5))\) equal to one on \(J\), and on the log Hilbert space use the real test \(g_N(\log x)=-x^2\sqrt{w_N(x)}f'(x)\). It lies in the physical prefix \(P_1\) and has \(\|g_N\|_2^2=\int x^3 w_N(x)|f'(x)|^2\,dx\ll_f1\), uniformly in \(N\). For any atom at \(u\), integration against the cumulative primitive on that leg is exact:

\[
 \int_{x\ge u}\frac{g_N(\log x)}{x\sqrt{w_N(x)}}\,d\log x=f(u).
\]

It follows that \(\langle C_N^{pp}g_N,g_N\rangle=-(2\pi/N)\sum\sqrt{uv}(\log r)(\log s)\le-(9\pi/10)V(N)/N\), where the sum is the same set of pairs as in \(V(N)\). This proves (1) and records the sign of the test rather than only the norm.

Thus bounding all independent factorization sectors by \(o(1)\) is not a viable way to remove the central rough–rough remainder. On the moduli from (1), this particular pure sector has natural-scale mass in a signed central form. Under the R22 global-GRH comparison, proving a small full central form would require compensating contributions from the complementary rough–rough factorizations on that same test. The proposition neither supplies nor rules out that compensation. No pointwise asymptotic for \(V(N)\) is used, and no claim about signed combinations outside this test or beyond the central prefix follows.
