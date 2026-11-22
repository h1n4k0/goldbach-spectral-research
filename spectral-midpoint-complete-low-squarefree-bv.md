# The complete cut midpoint low block cancels on every modulus

**Scope.** The previous [moving-roughness result](spectral-midpoint-complementary-blocks-moving-roughness.md) controlled both terms on rough squarefree partners, outside an exceptional set. Here ordinary maximal Bombieri–Vinogradov and a square-divisor expansion determine the entire **cut** low term, with or without the squarefree restriction, on every large even modulus. Subtracting the rough piece determines the genuine less-rough low term on the previous good moduli. A separate, centered first-log marginal has a positive explicit main term, also individually for every modulus. This does not evaluate the mixed high-LCM block on less-rough partners or improve individual-modulus control of that high block.

Let $N$ be sufficiently large and even, $L=\log N$, $m=N-n$, and $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$. Use the [midpoint definitions](spectral-midpoint-parity-signed-transport.md)

$$
 F_{0,D}(m)=\sum_{\substack{d\mid m\\d\le D}}\mu(d),\qquad
 F_{1,D}(m)=\sum_{\substack{d\mid m\\d\le D}}
             \mu(d)\left(1-\frac{2\log d}{\log m}\right).
$$

Given any $A>0$ there is a fixed $B=B(A)>0$ such that with $D=\sqrt N L^{-B}$ the following holds for every real half-open interval $I\subset(N/2,9N/16]$, uniformly in both endpoints. Let

$$
 W_0(I)=\operatorname{length}(I),\qquad
 W_1(I)=\int_I\frac{du}{\log(N-u)},
$$

and let $\Sigma(N)$ be the usual binary singular series, as in the [Dickman proof](spectral-midpoint-odd-aggregate-dickman.md). Then for either $\sigma(m)=1$ or $\sigma(m)=\mu(m)^2$,

$$
 \begin{split}
 \sum_{n\in I}\lambda(n)\sigma(m)F_{0,D}(m)
      &=O_A(NL^{-A}),\\
 \sum_{n\in I}\lambda(n)\sigma(m)F_{1,D}(m)
      &=2\Sigma(N)W_1(I)+O_A(NL^{-A}).                         \tag{1}
 \end{split}
$$

The same bounds hold for any larger fixed $B$ (with a sufficiently large $N$ threshold). Consequently the **nonsquarefree** sector has $O_A(NL^{-A})$ contribution to each of these two linear sums separately. No averaging or Dirichlet GRH is used for (1).

For clarity about the cut, $F_{0,D}$ is the entire $\operatorname{lcm}(d,e)\le D$ block of $F_{0,D}F_{1,D}$, as in the [LCM proof](spectral-midpoint-lcm-complement-frontier.md). This remains true without a squarefree partner gate: every contributing $d,e$ and hence their lcm $h$ is squarefree, and for $h\le D$ the inner unrestricted lcm calculation still gives $\mu(h)$. The second line of (1) is a linear marginal, not the contribution of another mixed-product block.

## 1. A squarefree mask at polylogarithmic cost

For genuine prime positions $n\in I$, both $n$ and $m$ are units modulo $N$, as $N/2<n<N$. For $Y=L^C$ with fixed $C$ to be chosen, expand $\mu(m)^2=\sum_{a^2\mid m}\mu(a)$ and retain $a\le Y$. For both tests $|F_{j,D}(m)|\le\tau(m)$, since $D<\sqrt m$ throughout the central interval for large $N$ and the individual weights are in $[0,1]$. In the omitted sum each $m$ has at most $\tau(m)$ choices of $a$. The number of integers $m\le N$ with at least one $a>Y$ such that $a^2\mid m$ is at most

$$
 \sum_{Y<a\le\sqrt N}\left\lfloor\frac{N}{a^2}\right\rfloor\ll N/Y .
$$

By Cauchy–Schwarz the total cost is at most

$$
 \ll L(N/Y)^{1/2}\left(\sum_{m\le N}\tau(m)^4\right)^{1/2}
 \ll NL^{17/2}Y^{-1/2}.                                      \tag{2}
$$

For the last inequality one can use $\tau(m)^4\le d_{16}(m)$ and $\sum_{m\le N}d_{16}(m)\ll NL^{15}$. The former holds on each prime power: a tuple of four exponents in $[0,e]$ is recoverable from the 16 counts of membership patterns among the first $e$ exponent levels, which form a weak composition of $e$. The latter follows by summing the last variable of a 16-fold divisor tuple and bounding the remaining harmonic sums. Choose $C$ so large in terms of $A$ that (2) is $O(NL^{-A-2})$.

In the surviving sum the genuine progression is $n\equiv N\bmod[a^2,d]$ and only $(ad,N)=1$ can contribute. For each $(a,d)$ with $\mu(a)\mu(d)\ne0$ the modulus is at most $Q=Y^2D$. For fixed $a$ and modulus, the only choices in $d$ are the subset of primes of $a$ included in $d$; the cofactor outside $a$ is determined. Thus the multiplicity of a modulus among all $(a,d)$ is at most $Y^2$, since for each $a$ there are at most $2^{\omega(a)}\le a\le Y$ possibilities.

Use [maximal Bombieri–Vinogradov, Theorem 20.2](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=206) at $Q\le\sqrt N L^{-B_{\rm BV}}$, with saving $A'$ chosen larger than $A+2C+5$, and then $B>2C+B_{\rm BV}$. All the progression residues are reduced. The passage from von Mangoldt to prime-only weight costs at most $O(Q\sqrt N L^2)$ before the multiplicity factor, hence is also absorbed by taking $B$ larger. A real hard interval and each of its subprefixes is a difference of two prefixes. The weight for $F_1$ is monotone on the cell and takes values in $[0,1]$ for each $d\le D$, with total variation at most one, so partial summation costs only an absolute factor in the same maximal error bound. These observations give, for the squarefree mask,

$$
 \sum_{n\in I}\lambda(n)\mu(m)^2F_{0,D}(m)
     =W_0(I) M_0+O_A(NL^{-A}),\quad
 \sum_{n\in I}\lambda(n)\mu(m)^2F_{1,D}(m)
     =W_0(I) M_0-2W_1(I) M_1+O_A(NL^{-A}),                   \tag{3}
$$

where

$$
 M_j=\sum_{\substack{a\le Y,\,d\le D\\(ad,N)=1}}
                  \frac{\mu(a)\mu(d)(\log d)^j}{\varphi([a^2,d])},
 \qquad j=0,1.
$$

For the ungated version, ordinary maximal BV gives (3) with only the $a=1$ summand in $M_j$ and no square-mask error.

## 2. Uniform reciprocal Euler moments

For $M\le N L^C$ write $u(n)=\mu(n)/n$ and $v_M(n)=\mu(n)\mathbf1_{(n,M)=1}/\varphi(n)$. Dirichlet convolution gives $v_M=u*g_M$ with $g_M(1)=1$ and the multiplicative coefficients

$$
 g_M(p^r)=
 \begin{cases}
 p^{-r},&p\mid M,\\[2mm]
 -p^{-r}/(p-1),&p\nmid M
 \end{cases}
 \qquad (r\ge1).
$$

This follows by dividing the Euler factor $1-\mathbf1_{p\nmid M}(p-1)^{-1}p^{-s}$ by $1-p^{-(1+s)}$. Put $G_M=\sum_{n\ge1}g_M(n)$, an absolutely convergent product for each $M$. Uniformly for $N^{2/5}\le x\le N$ and $M\le NL^C$, for any prescribed $T>0$ we have

$$
 \sum_{n\le x}v_M(n)=O_{C,T}(L^{-T}),\qquad
 \sum_{n\le x}v_M(n)\log n=-G_M+O_{C,T}(L^{-T}).              \tag{4}
$$

Here is a uniform tail proof. Take the Rankin exponent $\delta=1/\log L$ for sufficiently large $N$. At primes outside $M$ the Euler product for $\sum |g_M(n)|n^\delta$ is bounded by an absolute constant, since the local increments for large primes are $O(p^{-2+\delta})$. At primes dividing $M$, the factors are $(1-p^{-1+\delta})^{-1}$. For $p\le L^2$, $p^\delta\le e^2$ and the sum of reciprocal primes there is $O(1+\log\log L)$. For $p>L^2$ there are $O_C(L/\log L)$ prime divisors of $M$, and each contributes at most $O(L^{-2})$ to the logarithm of the product. These estimates, with the bounded contributions of the smallest primes, give

$$
 \sum_{n\ge1}|g_M(n)|n^\delta\ll_C(\log L)^{C_1}
$$

for an absolute constant $C_1$ after $C$ is fixed. In particular the tail $n>\sqrt x$ in the unweighted absolute sum is exponentially small in $L/\log L$.

The classical unconditional reciprocal Möbius bound is $\sum_{n\le t}u(n)=O(\exp(-c\sqrt{\log t}))$, from [Montgomery–Vaughan, Chapter 6, (6.18)](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287). Partial summation gives a tail with arbitrary inverse-log decay for $\sum u(n)\log n$, whose total limit is $-1$: by Abel convergence it is the negative of the derivative at zero of $1/\zeta(1+s)=s+O(s^2)$. In the convolution sum over divisors $a\le\sqrt x$, apply these estimates at $t=x/a\ge\sqrt x$. When carrying a log weight, use $\log(an)=\log a+\log n$; the $\log a$ piece multiplies the vanishing zeroth moment, and the first moment gives $-1$. For larger $a$, the elementary absolute bounds for the two $u$ sums cost at most $O(L^2)$, absorbed by the Rankin tail. This proves (4). In particular

$$
 G_N=\prod_{p\mid N}(1-1/p)^{-1}
          \prod_{p\nmid N}\left(1-\frac1{(p-1)^2}\right)
       =\Sigma(N)                                               \tag{5}
$$

when $N$ is even. The local factor at $2$ is then $2$.

## 3. The square-divisor model cancels

For each $a$ with $\mu(a)\ne0$ and $(a,N)=1$, write the squarefree $d=bc$ with $b\mid a$ and $(c,aN)=1$. Then $[a^2,d]=a^2c$ and $\mu(d)=\mu(b)\mu(c)$. The $d$ sum for that $a$ becomes, with the same log weight,

$$
 \frac1{\varphi(a^2)}
    \sum_{b\mid a}\mu(b)
         \sum_{\substack{c\le D/b\\(c,aN)=1}}
                        \frac{\mu(c)}{\varphi(c)}\big(\log b+\log c\big)^j .
                                                                    \tag{6}
$$

Here $D/b\ge N^{2/5}$ for all $b\mid a\le Y$, and $aN\le NL^C$. In (6) the zeroth moment vanishes to arbitrary inverse-log precision by (4). For $j=1$ the only nonnegligible term for that $a$ is

$$
            -\frac{G_{aN}}{\varphi(a^2)}\sum_{b\mid a}\mu(b).
$$

It vanishes for $a>1$; the surviving value at $a=1$ is $-\Sigma(N)$ by (5). All errors can be summed to arbitrary precision by asking for larger $T$ in (4): there are only $Y$ outer values and at most $Y$ inner divisors, and $\log b=O(L)$ suffices. Thus $M_0=O_A(L^{-A})$ and $M_1=-\Sigma(N)+O_A(L^{-A})$, and the same holds when $a$ is restricted to $1$. Substitution into (3) proves (1).

## 4. The actual less-rough low contribution

For an arbitrary threshold $z\ge2$, let $\mathcal L_{<z}(I)$ be the true squarefree contribution to the cut low block on $P^-(m)<z$. Let $\mathcal L_{\ge z}(I)$ denote its squarefree rough complement as in the [moving-roughness proof](spectral-midpoint-complementary-blocks-moving-roughness.md). The first line of (1) gives the uniform **pointwise** relation

$$
 \mathcal L_{<z}(I)=-\mathcal L_{\ge z}(I)+O_A(NL^{-A}),       \tag{7}
$$

simultaneously for all $z$. This is a signed comparison, not a bound for either summand individually.

For the original central cells of length $H=N/(16\lceil L^J\rceil)$, take $A>J+4$ in this proof and use the same fixed $B$ in the moving-roughness result. For fixed $0<\beta<1/1000$, its formula for the true rough low block and (7) give

$$
 \mathcal L_{<N^\beta}(I)
   =-\frac{\Sigma(N)H}{L}\big(\varepsilon_\beta+o(1)\big)
\quad \text{with } \varepsilon_\beta>0 ,
$$

on its common almost-all set. For $z_N=\exp(100L/\log L)$, they give

$$
       \mathcal L_{<z_N}(I)=O\!\left(\frac{\Sigma(N)H}{L^{9/5}}\right)
$$

on the corresponding common almost-all set. These are the **true** less-rough sums with the original sharp $D$ and the original squarefree restriction, not a change of weights or an approximation by an independent model. The preceding displays were derived with the squarefree restriction, but for both of these thresholds they also hold without it. There are $O(N/z)$ nonsquarefree $z$-rough partners: each has a prime square divisor with prime $\ge z$. By Cauchy--Schwarz, $|F_{j,D}|\le\tau(m)$ and the same divisor moment estimates as in (2), their true $\lambda$-weighted absolute contribution to either rough linear test is at most $O(NL^{17/2}/\sqrt z)$, smaller than any requested $NL^{-A}$ at the two indicated thresholds. The complete linear nonsquarefree sums already cancel by (1), so their less-rough linear sums do also. The same absolute rough nonsquarefree bound applies to $F_{0,D}F_{1,D}-F_{0,D}$ using its bound $O(\tau(m)^2)$; it does not estimate the nonsquarefree less-rough mixed sum.

The reason this does not finish the central mixed problem is specific: at LCM modulus $>D$ the mixed weight is no longer a single Möbius sum and cannot be estimated by the same single-progression inclusion–exclusion. The remaining less-rough high block and any uncut endpoint restoration outside the rough regime are left open. In particular neither (1) nor (7) gives a lower bound on prime-partner mass for a prescribed exceptional modulus or implies weak S.
