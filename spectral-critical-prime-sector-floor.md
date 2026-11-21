# A fixed-sign floor in the remaining actual critical sector

**Scope.** An unconditional lower bound for a specified sign component of the actual complementary-divisor sum. This is neither a lower bound on the full signed discrepancy nor a counterexample to S or R. It shows that estimating the remaining prime-divisor class in isolation by an inverse-log error below its natural scale cannot work.

Use the notation of the [critical-level reduction](spectral-critical-level-diagonal.md), and set $t=\sqrt N$. For even $N$ put
$$
 U_N=\sum_{\substack{d\ \mathrm{prime};\ \sqrt N/5\le d\le\sqrt N/3\\ (d,N)=1}}
       \sum_{\substack{N/2<n\le 9N/16;\ n<N-\sqrt N\, d\\
                          n\equiv N\bmod d;\ (n,N)=1}}
           \Lambda(n)\mu^2(N-n).
$$
All terms are nonnegative. Because $\mu(d)=-1$ for prime $d$, the contribution with this restriction in the complementary signed sum $C$ of the [structured-sector note](spectral-maynard-structured-critical.md), between the two indicated prefixes, is exactly $-U_N$. Every such $d$ is outside the structured sector.

For every sufficiently large $X$ there are $\gg X$ even integers $N$ in $[1.01X,1.065X]$ satisfying
$$
 U_N\gg \frac{N}{\log N}.
 \tag{1}
$$
One can additionally require $\mathfrak S(N)\le K$ for a fixed absolute $K$, still retaining $\gg X$ even $N$. Uniformly in all even $N$, the opposite upper bound $U_N\ll N/\log N$ holds.

To prove the lower bound, take actual primes $n\in[.53X,.54X]$ and $d\in[.24\sqrt X,.25\sqrt X]$, and take any odd squarefree integer $q\in[2\sqrt X,2.1\sqrt X]$ not divisible by $d$. Set $N=n+dq$. The product $dq$ lies in $[.48X,.525X]$, so $N\in[1.01X,1.065X]$ and is even. The interval bounds ensure
$$
 1/2<n/N\le 9/17<9/16,\qquad
 \sqrt N/5\le d\le\sqrt N/3,\qquad q>\sqrt N.
$$
Here the strict inequality $q>\sqrt N$ is exactly $n<N-\sqrt N\,d$. Also $(n,N)=1$ because $n$ is prime and larger than $d,q$, and $(d,N)=1$ because $d$ does not divide the different prime $n$. Finally $dq=N-n$ is squarefree. Thus each triple contributes $\log n$ to the appropriate $U_N$, with no multiplicity ambiguity because $(N,n,d)$ determines $q$.

For each such $d$ there are $\gg\sqrt X$ admissible $q$: the odd squarefree integers have positive density with elementary square-root error, by expanding the squarefree indicator; excluding multiples of $d$ removes only $O(1)$. By the prime number theorem there are $\gg\sqrt X/\log X$ choices for $d$ and $\sum_n\log n\gg X$. Thus the sum over these even $N$ of $U_N$ is $\gg X^2/\log X$.

For the uniform upper bound, remove the squarefree and moving-cut restrictions. The [Brun–Titchmarsh bound of Montgomery–Vaughan](https://doi.org/10.1112/S0025579300004708) for each reduced residue at prime modulus $d\asymp\sqrt N$ gives $O(N/(d\log(N/d)))$ primes below $N$ in that progression. Including the log weight this is $O(N/d)$. The sum of $1/d$ over the designated prime dyad is $O(1/\log N)$. The proper prime powers have total weight $O(\sqrt N(\log N)^2)$ before the $d$-count, and each fixed $n$ admits at most two of these prime moduli: three distinct primes at least $\sqrt N/5$ would have product larger than $N-n$. This proves $U_N\ll N/\log N$, so the first moment necessarily yields a fixed positive proportion of the stated even $N$ satisfying (1).

Finally the Goldbach singular series has bounded mean. Its factor for an odd prime dividing $N$ is $1+1/(p-2)$ times the fixed twin-prime product factor, and expanding the divisibility product gives
$$
 \sum_{N\le 2X\;;\ N\,\mathrm{even}}\mathfrak S(N)
 \ll X\prod_{p>2}\left(1+\frac1{p(p-2)}\right)\ll X.
$$
Choosing $K$ large in terms of the positive proportion removes at most half those $N$. Thus the floor occurs even when the singular series is bounded.

If one inserts $\log d$ as in the weighted long-divisor form and the nonnegative central factor $\sqrt{(n/N)(1-n/N)}$, the two weights are respectively comparable to $\log N$ and to one in this sector. After division by $N$ this sign component is then bounded below by an absolute positive constant on the same bounded-singular-series subsequence. Both sums are genuine actual-$\Lambda$, actual-$\mu$ subpieces. They can cancel against other divisor parities in the full expression; neither lower bound can be transferred to that full expression.
