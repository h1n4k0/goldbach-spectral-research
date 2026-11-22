# Opposite signs of the genuine odd midpoint remainder in every central cell for almost all moduli

**Scope.** This is an unconditional result about two explicit subfamilies of true prime positions in the [high-LCM remainder](spectral-midpoint-lcm-complement-frontier.md), not a synthetic transport or an assumption of GRH. On almost all even $N$ with arbitrary inverse-logarithmic exceptional savings, every original central cell has both a positive and a negative subfamily of that remainder, each of natural weight scale $SH/\log N$. Consequently the signed remainder cannot be estimated by proving that either entire sign class is negligible on almost all $N$. Cancellation of their actual sum, individual exceptional $N$, central Goldbach positivity, and Hypothesis S remain outside the result.

Fix $J\ge1$, $0<\beta<1/1000$, and an arbitrary exceptional-saving exponent $A_0>0$. Let $X$ tend to infinity and write $\ell=\log X$. For even $N\in[X,2X]$ write $L=\log N$, $S=\mathfrak S(N)$, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Partition $(N/2,9N/16]$ into $M=\lceil L^J\rceil$ equal real half-open cells $I$ of length $H=N/(16M)$. Write $m=N-n$ as before, and use the squarefree $N^\beta$-rough gate. The following assertions hold simultaneously for every such cell of every even $N$ outside a set of $O_{A_0,J}(X\ell^{-A_0})$ integers in the dyad.

There are two disjoint specific families of partners, $\mathcal G_3(X)$ and $\mathcal G_5(X)$, defined below. Both consist of squarefree products of an odd number of primes, all at least $N^\beta$, and with largest prime less than $\sqrt m$. Their genuine prime-position masses satisfy

$$
 \sum_{\substack{n\in I\\N-n\in\mathcal G_k(X)}}\lambda(n)
       \asymp_{J} \frac{S H}{L},\qquad k=3,5.                    \tag{1}
$$

The full high-LCM coefficient $\sum_{h\mid m,\,h>\sqrt m}C_m(h)$ is exactly $+2$ on $\mathcal G_3(X)$ and exactly $-6$ on $\mathcal G_5(X)$. The conclusion is about contributions of each whole subfamily to the genuine weighted sum. Their displayed signs concern the **full high block**, not its coefficient at each fixed modulus. By the truncation bound in the preceding note, their contributions to the actual $d,e\le D$ high block differ by $o(SH/L)$ for any fixed $D=\sqrt N L^{-B}$ with $B>0$.

## 1. Factor choices and exact signs

For $m\in[X/3,2X]$, define $\mathcal G_k(X)$ as follows. Choose one prime from each of the following $k-1$ disjoint power bands, multiply them into $c$, and require the final factor $p=m/c$ to be prime:

$$
\begin{array}{c|l}
 k & \text{exponent intervals for the bands }[X^a,X^b)\\\hline
 3 & [.310,.315),\ [.320,.325)\\
 5 & [.192,.193),\ [.194,.195),\ [.196,.197),\ [.198,.199).
\end{array}
$$

There is no additional cutoff on $p$; the bounds on $m$ and $c$ imply that $p$ exceeds all the chosen primes, uniformly for large $X$. For $k=3$ the exponents of $c$ are between $.630$ and $.640$, so every prime factor of $m$ is between $X^{.30}$ and $X^{.39}$ for large $X$. For $k=5$ the exponents of $c$ are between $.780$ and $.784$, and every prime factor of $m$ is between $X^{.19}$ and $X^{.23}$. In particular $m$ has exactly $k$ distinct prime factors, its representation by these bands and the final prime is unique, and it passes the roughness and largest-factor tests.

For $k=3$ the divisors below $\sqrt m$ have zero or one prime factor, because $\log m/\ell=1+O(1/\ell)$ and $2(.30)>.5$. For $k=5$ they have zero, one, or two factors, since $2(.23)<.5<3(.19)$. Thus the half-divisor Möbius sum $F_0(m)$ is $1-3=-2$ on the first family and $1-5+10=6$ on the second. The high block for such an odd-parity squarefree composite is $-F_0(m)$ by the [exact complement identity](spectral-midpoint-lcm-complement-frontier.md). This proves the asserted signs.

Let $\mathcal C_k(X)$ be the set of products $c$ of the chosen band primes, counted once. By Mertens,

$$
 b_k(X)=\sum_{c\in\mathcal C_k(X)}\frac1c
       =\prod_{\text{bands }[X^a,X^b)}
          \sum_{\substack{X^a\le r<X^b\\r\ {\rm prime}}}\frac1r
       \ \longrightarrow\ \prod_{\text{bands}}\log(b/a)>0.       \tag{2}
$$

## 2. An unconditional correlated lower bound with fixed physical windows

First use any two fixed real intervals $U,V\subset[X/3,2X]$. Put $e(x)=e^{2\pi i x}$ and

$$
 P_U(\alpha)=\sum_{n\in U}\lambda(n)e(\alpha n),\qquad
 T_{k,V}(\alpha)=\sum_{\substack{m\in V\\m\in\mathcal G_k(X)}}
                   \log p_{\max}(m)\,e(\alpha m).
$$

By uniqueness the coefficient of $m$ in $T_{k,V}$ is bounded by $O(\ell)$, not by a number of different presentations. Parseval gives $\int_0^1|T_{k,V}|^2\ll X\ell^2$. The joint Fourier coefficient equals exactly

$$
 \int_0^1 P_U(\alpha)T_{k,V}(\alpha)e(-N\alpha)\,d\alpha
 =\sum_{\substack{n\in U,\ m=N-n\in V\\m\in\mathcal G_k(X)}}
             \lambda(n)\log p_{\max}(m).                       \tag{3}
$$

Choose large fixed $C$ and $Q=\ell^C$. Use major arcs $|\alpha-a/q|\le2Q/X$ around all reduced fractions of denominator $q\le Q$ on the circle. They are disjoint for large $X$. Given any fixed $E>0$, by choosing $C$ sufficiently large in terms of $E$, the minor arc bound

$$
 \sup_{\mathfrak m}|P_U|\ll_E X\ell^{-E}                         \tag{4}
$$

holds uniformly in the interval. Indeed Dirichlet approximation with denominator bound $\lfloor X/Q\rfloor$ supplies a reduced $a/q$ with $|\alpha-a/q|\le q^{-2}$, and off the major arcs $Q<q\le X/Q$. Apply the [Vaughan exponential-sum estimate, Theorem 17.1](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=77) to the two prefixes. The prime-power removal costs $O(\sqrt X\ell^2)$, which is negligible for fixed $E$. From (4) and Parseval, the sum of squares over all integers $N$ of the minor part of (3) is

$$
 \ll_E X^3\ell^{2-2E}.                                         \tag{5}
$$

No estimate for $T_{k,V}$ on the minor arcs beyond Parseval is used.

Write $\widehat U(\eta)=\int_U e(\eta x)\,dx$, with the same notation for $V$. On a major arc $\alpha=a/q+\eta$, for every prescribed $E_1$,

$$
 \begin{split}
 P_U(a/q+\eta)&=\frac{\mu(q)}{\varphi(q)}\widehat U(\eta)
                        +O_{C,E_1}(X\ell^{-E_1}),\\
 T_{k,V}(a/q+\eta)&=\frac{\mu(q)}{\varphi(q)}b_k(X)\widehat V(\eta)
                        +O_{C,E_1}(X\ell^{-E_1}).
 \end{split}                                                  \tag{6}
$$

For the first expansion apply [Siegel–Walfisz, Corollary 11.19](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287) to the prime-only weights in each reduced residue class and use partial summation. All the primes here exceed $q$. The residue sum is $c_q(a)=\mu(q)$. For the second expansion, fix $c$ and apply the same theorem to the final prime $p$ on the real interval $V/c$, using weight $\log p$ and additive phase $e(\eta cp)$. The scale $X/c$ is a fixed positive power of $X$, and $(c,q)=1$ because every prime factor of $c$ is polynomially large. The residue sum after multiplication by $c$ is again $\mu(q)$. The continuum integral for this $c$ is $\widehat V(\eta)/c$. The partial-summation factor is $O(1+|\eta|X)=O(Q)$, and summing over the reduced residues costs at most another factor $Q$. Increasing the requested saving in Siegel–Walfisz absorbs these factors uniformly; prime powers in each final-prime interval are power-small in $X/c$. Finally sum the errors using (2). This proves (6) with fixed $C$ and arbitrarily large $E_1$.

The major part of (3) is therefore

$$
 b_k(X)\,\Sigma_Q(N)
   \int_{-2Q/X}^{2Q/X}\widehat U(\eta)\widehat V(\eta)e(-N\eta)\,d\eta
   +O_{C,A_1}(X\ell^{-A_1}),                                  \tag{7}
$$

where $A_1$ is arbitrarily prescribed and

$$
 \Sigma_Q(N)=\sum_{q\le Q}\frac{\mu(q)^2c_q(N)}{\varphi(q)^2}.
$$

Indeed the total arc length is $O(Q^3/X)$, both original sums are $O(X\ell)$, and $E_1$ in (6) can be chosen after $C,A_1$. The complete integral in (7) equals $\operatorname{length}(U\cap(N-V))$ by Fourier inversion of the convolution of two interval indicators. The omitted tails have absolute integral $O(X/Q)$ from $|\widehat U|,|\widehat V|\ll |\eta|^{-1}$. These assertions are uniform in the endpoints and use interval lengths, not integer counts in a main term.

The complete Ramanujan series is the usual binary singular series $\Sigma(N)$ (comparable to $S$); at each prime its factor is $1+(p-1)^{-1}$ when $p\mid N$ and $1-(p-1)^{-2}$ otherwise. It is bounded below by an absolute positive constant for even $N$. Absolute convergence for fixed $N$ follows from the product, since only finitely many primes divide $N$. The tails of the series are small for almost all $N$, to sufficient precision here. For squarefree $q$, the divisor formula gives

$$
 |c_q(N)|\le\sum_{d\mid(q,N)}d,\qquad
 \sum_{1\le N\le 2X}|c_q(N)|\le 2X\tau(q).
$$

It follows that

$$
 \sum_{N\le2X}\sum_{q>Q}
     \frac{\mu(q)^2|c_q(N)|}{\varphi(q)^2}\ll XQ^{-1/2}.        \tag{8}
$$

For the last step the Euler product of $\sum_q q^{1/2}\mu(q)^2\tau(q)/\varphi(q)^2$ converges, since its factors beyond finitely many primes are $1+O(p^{-3/2})$. By Markov the tail in (8) is at most $\ell^{-2}$ outside $O(X\ell^2Q^{-1/2})$ integers, a single exceptional set independent of $U,V$.

## 3. A polylogarithmic cover of all moving cells

Set $\delta=X/(1000\ell^J)$. Partition $[X,2X]$ into intervals of length at most $\delta$, further cutting wherever $M=\lceil(\log N)^J\rceil$ changes. Since $M$ is increasing and $O_J(\ell^J)$ on the dyad, there are $O_J(\ell^J)$ pieces in total. Endpoints at change points can be assigned to the plateau having their actual value of $M$, or treated as singleton pieces; this does not change the count.

For each piece with left reference point $N_0$ and fixed $M$, and each cell index $j=0,\ldots,M-1$, fix $U$ of length $\delta$ centered at $N_0/2+(j+1/2)N_0/(16M)$. For every $N$ in the piece $U$ is contained in the $j$-th actual cell: at fixed $M$ its two endpoints move by at most $(9/16)\delta$ between $N_0$ and $N$, and $N_0/(16M)\gg_J\delta$ with a factor larger than $10$ for all sufficiently large $X$. Fix $V$ of length $4\delta$ containing $N-U$ for every such $N$, for example by adding margins $\delta$ at each end of the interval from $N_0-\sup U$ to $N_0+\delta-\inf U$. Both $U,V$ lie in $[X/3,2X]$. The full integral in (7) has value $\delta$ for every such $N$. There are $O_J(\ell^{2J})$ interval pairs to consider.

For each pair and either $k$, by (5) the number of $N$ whose minor part exceeds $X\ell^{-J-2}$ in absolute value is $O_E(X\ell^{2J+6-2E})$. Take $E$ so large that multiplication by $O_J(\ell^{2J})$ still leaves $O(X\ell^{-A_0})$; then fix $C$ large enough for (4), (8), and $X/Q=o(\delta)$. Take $A_1>J+3$ in (7). For every remaining even $N$, the right side of (3) for each of its fixed pairs is

$$
 b_k(X)\Sigma(N)\delta+o(S\delta),
$$

uniformly over the whole cover, by (7), (8), and the uniform lower bound on $\Sigma(N)$. The inverse-log error terms may have constants depending on the chosen fixed parameters. Since the largest prime has $\log p_{\max}(m)\asymp\ell$ and the weights are nonnegative, (2) and containment of $U$ prove the lower bound in (1), simultaneously in every original cell.

For the upper bound in (1), valid for all sufficiently large even $N$, fix $c\in\mathcal C_k(X)$. If $(c,N)>1$ there are no contributions from genuine prime $n$ in the central interval. Otherwise apply the standard dimension-two upper sieve to $p$ and $N-cp$ over the interval of length $H/c$ determined by the actual cell. Here $c\le X^{.8}$, so that interval has polynomial length, and both true primes exceed its sifting threshold $(H/c)^{1/100}$. As in the [two-prime bound in the coherent transport proof](spectral-coherent-divisor-transport-barrier.md), there are two roots except for one root at each prime dividing $cN$, and in particular one at $2$. The extra local factors from $c$ are bounded because $c$ has at most four prime factors. Thus the raw $\lambda$-mass for fixed $c$ is

$$
 O\!\left(\frac{SH}{cL}+ L(H/c)^{1/2}\log(2H/c)\right).
$$

The main term sums by (2). Summing the remainder even over all integers $c\le X^{.8}$ gives $O(X^{.9}\ell^2)$, negligible relative to $SH/L$. This proves (1). The two opposing weighted contributions in (1) do not determine the signed sum over all genuine odd smooth-largest composites.
