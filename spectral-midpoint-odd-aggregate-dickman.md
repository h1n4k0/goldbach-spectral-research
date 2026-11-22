# The genuine odd high-LCM aggregate has a positive Dickman main term

**Scope.** This is an unconditional almost-all result for the **full signed** high-LCM block from the [midpoint analysis](spectral-midpoint-lcm-complement-frontier.md). For any fixed small polynomial roughness cutoff, the full block containing the opposing signs exhibited by the [two-sign subfamilies](spectral-midpoint-actual-opposite-sign-families.md) has a nonzero signed aggregate in each central cell. The leading constant is explicit and close to one. The result does not control any prescribed exceptional modulus, prove central Goldbach for all moduli, or imply Hypothesis S. No form of GRH is used.

Fix $J\ge1$, $0<\beta<1/1000$, and $A_0>0$. Let $X$ tend to infinity, $\ell=\log X$, and take even $N\in[X,2X]$. Write $L=\log N$, $m=N-n$, $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$, and partition $(N/2,9N/16]$ into $M=\lceil L^J\rceil$ equal half-open cells $I$ of length $H=N/(16M)$. Denote the usual binary singular series by

$$
 \Sigma(N)=2\prod_{p>2}\left(1-\frac1{(p-1)^2}\right)
                \prod_{\substack{p\mid N\\p>2}}\frac{p-1}{p-2}.
$$

It equals the binary Ramanujan-series normalization used below and is comparable to $S=\mathfrak S(N)$.

Let $G(m)=-F_0(m)$ if $m$ is squarefree with an odd number of distinct prime factors at least three, and $G(m)=0$ otherwise. Here $F_0(m)=\sum_{d\mid m,\ d<\sqrt m}\mu(d)$ as in the midpoint proof. By that proof, $G(m)$ agrees on squarefree integers with the **entire** high-LCM sum $\sum_{h\mid m,\ h>\sqrt m}C_m(h)$. In particular it vanishes if $m$ has a prime factor $>\sqrt m$; this also follows by summing over the divisors of the complementary cofactor. For all but $O_{\beta,J,A_0}(X\ell^{-A_0})$ even $N$ in the dyad, uniformly in **every** central cell, one has

$$
 \sum_{\substack{n\in I\\P^-(m)\ge N^\beta}}\lambda(n)G(m)
       =\frac{\Sigma(N)H}{L}\big(C_\beta+o_{\beta,J,A_0}(1)\big).       \tag{1}
$$

Here $P^-(m)$ is the least prime factor, and $G$ already includes the squarefree restriction. The cutoff high block with $d,e\le D=\sqrt N L^{-B}$, for any fixed $B>0$, has the same main term on this gate by the critical-band bound (2) of the midpoint LCM proof, with an error $O_{\beta,B,J}(SH(1+\log L)/L^2)$.

Let $K_\beta(dt)=\mathbf1_{t\ge\beta}\,dt/t$ on the nonnegative real line and define the positive, locally finite convolution exponential

$$
 \mathcal B_\beta=\sum_{j\ge0}\frac{K_\beta^{*j}}{j!},
 \qquad K_\beta^{*0}=\delta_0 .
$$

The constant in (1) is

$$
 \begin{split}
 C_\beta&=1-\int_{[0,1/2)}
              \frac{\rho((1-s)/\beta-1)}{1-s}\,\mathcal B_\beta(ds),\\
 0<1-\frac{1}{\beta\left\lfloor (2\beta)^{-1}-1\right\rfloor!}
           &\le C_\beta<1,
 \end{split}                                                       \tag{2}
$$

where the Dickman function is specified by $\rho(u)=1$ for $0\le u\le1$ and $u\rho'(u)=-\rho(u-1)$ for $u>1$. The proof of (2) below is independent of any theorem about counts of smooth integers.

## 1. Freeze the roughness threshold and define the genuine coefficient

In the analytic transfer use the fixed threshold $z=X^\beta$, and put $g_X(m)=G(m)\mathbf1_{P^-(m)\ge z}$ on $[X/3,2X]$. This is a function of the integer $m$ and $X$ only, not of $N$. It is bounded by a constant depending only on $\beta$, since a rough $m\le2X$ has at most $K=\lfloor2/\beta\rfloor$ prime factors for large $X$; hence the divisor sums have at most $2^K$ terms.

Replacing $P^-(m)\ge z$ by $P^-(m)\ge N^\beta$ costs $o(SH/L)$ in every cell for every even $N$. Indeed a changed nonzero term has a prime factor $r\in[z,2^\beta z)$ and $m/r$ still $z$-rough. Use the [rough-cofactor bound (5)](spectral-midpoint-lcm-complement-frontier.md) with this $z\asymp N^\beta$: its proof depends on the exponent range and gives the same bound, with $V_z\asymp S/(\beta L)$, for this constant-factor change in threshold. Sum that bound over these $r$. The reciprocal sum $\sum 1/(r-1)$ is $O_\beta(1/L)$ by the prime upper bound in a dyadic interval, and the aggregate CRT error is $O_\beta(X^{(1+\beta)/2}L^2)$ by summing $r^{-1/2}$. Multiplication by the fixed bound for $G$ is harmless. This proves the stated comparison uniformly on the true prime sequence; it is not a distribution statement for roughness-conditioned progressions.

## 2. Transfer the exact coefficient by its largest prime

Let $V=[X/3,2X]$ and $U$ be any fixed real interval in that range. Write $e(u)=e^{2\pi i u}$. The exact discrete Fourier factors are

$$
 P_U(\alpha)=\sum_{n\in U}\lambda(n)e(\alpha n),\qquad
 T_X(\alpha)=\sum_{m\in V}g_X(m)e(\alpha m).
$$

In particular $\int_0^1|T_X|^2\ll_\beta X$. We compute its major arcs using the unique increasing prime factorization of each squarefree partner. For odd $3\le k\le K$, write $m=cp$, where $c=p_1\cdots p_{k-1}$ with $z\le p_1<\cdots<p_{k-1}$ prime, and the largest prime $p$ satisfies $p>p_{k-1}$. There is no multiplicity from factorization. We can restrict $c\le2X/z$ and the prime factors of $c$ to $[z,2X]$. The sum of $1/c$ over each such family is $O_\beta(1)$ by Mertens and the bound for the number of factors.

For fixed $c$ and a real variable $y$ with $y>p_{k-1}$, define the actual divisor sign weight extended to that real variable by

$$
 w_c(y)=-\sum_{a\mid c}\mu(a)
               \big(\mathbf1_{\,a^2<cy}-\mathbf1_{\,a^2y<c}\big).
$$

For a prime $y=p>p_{k-1}$ this is exactly $G(cp)$: the first term counts short divisors $a$ not containing $p$, and the second counts short divisors $ap$ with $\mu(ap)=-\mu(a)$. The product has an odd number $k\ge3$ of distinct primes. For real $y$ the formula is piecewise constant with $O_\beta(1)$ breakpoints $y=a^2/c$ or $y=c/a^2$. An explicit upper gate $y\le\sqrt{cy}$ is unnecessary, because the formula is zero for $y>\sqrt{cy}$ on these cofactor configurations. Endpoint choices are accounted for by treating each open interval and its endpoints separately.

Define the real major-arc density on $V$ by

$$
 a_X(x)=
 \sum_{\substack{3\le k\le K\\ k\ \rm odd}}
 \ \sum_{\substack{c=p_1\cdots p_{k-1}\le2X/z\\z\le p_1<\cdots<p_{k-1}\\
                        p_i\ \rm prime}}
     \frac{\mathbf1_{\,x/c\ge z,\ x/c>p_{k-1}}\,w_c(x/c)}
          {c\log(x/c)} .                                         \tag{3}
$$

An absent summand is set to zero without evaluating its denominator. On its support, the denominator is at least $c\beta\ell$. Each summand has total variation $O_\beta((c\ell)^{-1})$ on $V$, including its cutoff jumps and the monotone variation of the reciprocal logarithm. The same bound holds after extending it by zero off $V$. Thus $\|a_X\|_\infty$ and the total variation of $a_X\mathbf1_V$ are both $O_\beta(1/\ell)$. These bounds are uniform in $X$.

For the circle-method cutoff, choose $Q=\ell^C$ for a sufficiently large fixed $C$; use disjoint arcs $|\alpha-a/q|\le 2Q/X$ at reduced fractions $q\le Q$. For any prescribed $E_1>0$, [Siegel–Walfisz, Corollary 11.19](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF) and partial summation give on the major arcs, for $\eta=\alpha-a/q$,

$$
 \begin{split}
 P_U(a/q+\eta)&=\frac{\mu(q)}{\varphi(q)}\int_U e(\eta x)\,dx
                              +O_{C,E_1}(X\ell^{-E_1}),\\
 T_X(a/q+\eta)&=\frac{\mu(q)}{\varphi(q)}\int_V a_X(x)e(\eta x)\,dx
                              +O_{\beta,C,E_1}(X\ell^{-E_1}).
 \end{split}                                                       \tag{4}
$$

For the second expansion fix $c$. Its prime arguments range in $V/c$ and on the support have scale $X/c\gg z$; all factors of $c$ and all final primes exceed $q$. The admissible congruence classes for $p$ are all the reduced classes. Multiplication by $c$ permutes them, so their additive residue sum is $\mu(q)$, not a character correlation. In each reduced residue apply the unweighted prime form of Siegel–Walfisz, split into the bounded number of true sign intervals for $w_c$ and gates in (3), and partially sum against $e(\eta cp)$. The phase costs at most $O(Q)$, and the sum over residues costs at most another factor $Q$. The continuum substitution $x=cp$ supplies precisely $1/(c\log(x/c))$. The errors can be made $O_{\beta,C,E_1}((X/c)\ell^{-E_1})$ per $c$, including endpoints, since $X/c$ is polynomially large. Sum by the reciprocal bound for $c$. The usual log-weighted version and removal of proper powers give the first expansion. No estimate of a prime sum at a power-size modulus is used.

For any $E>0$, choosing $C$ sufficiently large yields $\sup_{\mathfrak m}|P_U|\ll_E X\ell^{-E}$ by the [Vaughan estimate, Theorem 17.1](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=77) on the two prefixes. Indeed Dirichlet approximation with denominator at most $\lfloor X/Q\rfloor$ gives a reduced approximant with error at most $1/(q\lfloor X/Q\rfloor)\le q^{-2}$; off the declared major arcs $q>Q$. The prime-only removal costs $O(\sqrt X\ell^2)$. Bessel and the genuine $L^2$ bound on $T_X$ give

$$
 \sum_{N\in\mathbb Z}
   \left|\int_{\mathfrak m}P_U(\alpha)T_X(\alpha)e(-N\alpha)\,d\alpha\right|^2
       \ll_{\beta,E} X^3\ell^{-2E}.                              \tag{5}
$$

## 3. Evaluate the continuum density uniformly

For $k\ge3$ odd put $t_k=1-\sum_{i<k}t_i$ and let

$$
 c_{\beta,k}=\frac1{k!}
 \int_{\substack{t_1,\ldots,t_k\ge\beta\\\sum_i t_i=1}}
 \frac{-\sum_{A\subseteq[k]}(-1)^{|A|}
                   \mathbf1_{\,\sum_{i\in A}t_i<1/2}}
      {t_1\cdots t_k}\,dt_1\cdots dt_{k-1}.                       \tag{6}
$$

All terms are zero beyond a fixed number of factors. Then uniformly for $x\in V$,

$$
 \ell a_X(x)=\sum_{\substack{k\ge3\\k\ \rm odd}}c_{\beta,k}+o_\beta(1).
                                                                    \tag{7}
$$

To verify the convergence, write $\xi=\log x/\ell=1+O(1/\ell)$ and $t_i=\log p_i/\ell$ for $i<k$, so that $\log(x/c)/\ell=\xi-\sum_{i<k}t_i$. In (3) this last quantity is at least $\beta$ and greater than $t_{k-1}$. The explicit sign formula $w_c$ becomes the signed subset sum in (6), with threshold $\xi/2$ and $t_k=\xi-\sum_{i<k}t_i$. The reciprocal-prime measures

$$
 \sum_{\substack{z\le p\le 2X\\p\ \rm prime}}
       \frac1p\,\delta_{\log p/\ell}
       \quad\Longrightarrow\quad
        \mathbf1_{\beta\le t\le1}\frac{dt}{t}
$$

converge weakly by Mertens on fixed exponent intervals, and the finite tensor products converge too. The factor $c\le2X/z$ is automatic on the support of (3). Outside strips of any fixed small thickness around the finitely many limiting hyperplanes of ordering, lower cutoffs, and nontrivial midpoint subset cuts, each indicator is unchanged for all $x\in V$ once $X$ is large. The empty and full subsets give constant indicators. On the complements of those strips, the reciprocal $1/t_k$ is bounded and changes uniformly by $O_\beta(1/\ell)$. The limiting measures of the strips tend to zero with their thickness, and the measures are finite; the same is then true for the limsup of their discrete masses. This proves uniform convergence to the ordered-region integral. Its integrand is symmetric in the $k$ coordinates on the simplex and the coordinate measure $dt_1\cdots dt_{k-1}$ is invariant under permutations, including swaps with $t_k$ (determinant of absolute value one). The ordering region is exactly $1/k!$ of the integral. This proves (7), including the possibility $k\beta=1$, which has zero limiting measure.

## 4. Scale of the main term in all cells on the same good moduli

From (4), the integral over the major arcs is, up to $O_{\beta,C,A_1}(X\ell^{-A_1})$ for arbitrary fixed $A_1$,

$$
 \Sigma_Q(N)\int_{-2Q/X}^{2Q/X}
         \widehat{1_U}(\eta)\widehat{a_X\mathbf1_V}(\eta)
                       e(-N\eta)\,d\eta,\qquad
 \Sigma_Q(N)=\sum_{q\le Q}\frac{\mu(q)^2c_q(N)}{\varphi(q)^2},
$$

where hats denote positive-sign Fourier integrals and $c_q$ is the Ramanujan sum. This uses total arc length $O(Q^3/X)$, and both original sums and approximants are bounded by $O_\beta(X\ell)$, absorbed by choosing $E_1$ after $C,A_1$. The bounded variation estimate after (3) gives $|\widehat{a_X\mathbf1_V}(\eta)|\ll_\beta(\ell|\eta|)^{-1}$ for $\eta\ne0$; also $|\widehat{1_U}(\eta)|\ll|\eta|^{-1}$. Hence restoring the full real-line integral costs $O_\beta(X/(Q\ell))$ before multiplication by $\Sigma_Q(N)$. By Fourier inversion the restored integral is $\int_U a_X(N-u)\mathbf1_V(N-u)\,du$.

The complete Ramanujan series is $\Sigma(N)$, which is bounded below on even $N$. For squarefree $q$, $\sum_{N\le2X}|c_q(N)|\le2X\tau(q)$ by the divisor formula; hence the absolute series tails summed over all $N\le2X$ are $O(XQ^{-1/2})$, since $\sum_q q^{1/2}\mu(q)^2\tau(q)/\varphi(q)^2$ converges by its Euler product. Thus the absolute tail is at most $\ell^{-2}$ except for $O(X\ell^2Q^{-1/2})$ moduli, independently of the intervals. In particular $\Sigma_Q(N)\asymp\Sigma(N)$ on the good even moduli.

To handle the moving cells, partition $[X,2X]$ into pieces of length at most $\delta=X\ell^{-J-4}$, also cutting at changes of $M$. This gives $O_J(\ell^{J+4})$ pieces, with singleton endpoints allowed. In each piece use a fixed reference $N_0$ in its closure with the piece's value of $M$ in the formulas, and take $U$ to be each of the $M$ fixed cells at that reference. For every $N$ in the piece, its corresponding true cell differs from $U$ by intervals of total length $O(\delta)$ since the endpoints at fixed $M$ are fixed linear functions of $N$. The genuine weighted sum over that difference is $O_\beta((\delta+1)L)=o(SH/L)$ using bounded $g_X$. Also $N-U\subset V$ for all such $N$ once $X$ is large, and $|U|=H(1+o(1))$. The number of fixed $U$ in the cover is $O_J(\ell^{2J+4})$.

For each $U$, (5) bounds the exceptional count at minor-arc error threshold $X\ell^{-J-2}$ by $O_{\beta,E}(X\ell^{2J+4-2E})$. Union over the cover, then choose $E$ so that $4J+8-2E<-A_0$. Choose $C$ sufficiently large both for this minor estimate and to make the Ramanujan exceptional count $O(X\ell^{-A_0})$ and $X/Q=o(H)$. Choose $A_1>J+2$. Equations (4)–(7), the restored integral, and the cell and roughness comparisons now prove (1) with $C_\beta=\sum_{k\ge3,\ k\ {\rm odd}}c_{\beta,k}$. Uniformity is on all cells of each remaining $N$; the proof does not pick one good cell separately for each $N$.

## 5. The signed simplex constant

Define $\mathcal M_\beta=\sum_{j\ge0}(-1)^j K_\beta^{*j}/j!$, also locally finite with atom one at zero. The series are finite on bounded supports in their convolution indices, so $\mathcal M_\beta*\mathcal B_\beta=\delta_0$ by the binomial identity. For $t>0$ write $f_-(t)$ and $f_+(t)$ for their densities. They are continuous near $t=1$: the only step from the single convolution is at $\beta$, and higher convolutions of the locally bounded densities are continuous for $t>0$.

Let

$$
 A_-=\int_{[0,1/2)}f_+(1-s)\,\mathcal M_\beta(ds),\qquad
 A_+=\int_{[0,1/2)}f_-(1-s)\,\mathcal B_\beta(ds).
$$

Splitting the density of $\mathcal M_\beta*\mathcal B_\beta$ at total $1$ at the midpoint gives $A_-+A_+=0$. The right-half contribution is $A_+$ after swapping the variables. There is no boundary atom at $1/2$; the two terms with an atom at zero are separately included.

Expand $A_-$ and $A_+$ by the number $j$ of factors on the subset side with sum $s<1/2$, and the number $l$ on the complementary side with sum $1-s$. A term has coefficient $1/(j!l!)$, multiplied respectively by $(-1)^j$ and $(-1)^l$. The difference divided by two selects odd $k=j+l$ with sign $(-1)^j$. On the symmetric simplex, the $1/(j!l!)$ coefficient is exactly the subset multiplicity $\binom{k}{j}/k!$ in (6). Thus the signed constant from (6), **including** the one-prime term, is $-(A_--A_+)/2=A_+$. The one-prime term has value $-1$, from the empty subset and $K_\beta(1)=1$ in density notation. Excluding this term gives $C_\beta=1+A_+$.

For completeness the density $f_-$ follows directly from the convolution series. Multiplying $K_\beta^{*j}$ by its variable distributes that variable across its $j$ factors. Hence

$$
 t\,\mathcal M_\beta(dt)=
      -\big((tK_\beta)*\mathcal M_\beta\big)(dt),\qquad
 tK_\beta(dt)=\mathbf1_{t\ge\beta}\,dt .
$$

Writing $R(t)=\mathcal M_\beta([0,t])$, one has $R(t)=1$ for $0\le t<\beta$ and $t R'(t)=-R(t-\beta)$ for almost all $t>\beta$. Continuity on $t>0$ and stepwise integration give the unique solution $R(t)=\rho(t/\beta)$. In particular for $t>\beta$,

$$
 f_-(t)=-\frac{\rho(t/\beta-1)}{t}.
$$

Substituting in $C_\beta=1+A_+$ proves its integral formula in (2).

The delay equation gives the equivalent identity $u\rho(u)=\int_{u-1}^u\rho(v)\,dv$ for $u\ge1$: the two sides have the same derivative for $u>1$ and agree at $1$. A first zero would contradict the positive integral over preceding values, so $\rho$ is positive; the delay equation then makes it nonincreasing. Consequently $\rho(u)\le\rho(u-1)/u$ for $u\ge1$, and iteration gives $\rho(u)\le 1/\lfloor u\rfloor!$. Also

$$
 \mathcal B_\beta([0,1/2])\le
      \exp\!\left(\int_\beta^{1/2}\frac{dt}{t}\right)=\frac1{2\beta},
$$

by dropping the restriction on the total of the nonnegative factor variables in each term. The integral in (2) is strictly positive (already its atom at zero contributes) and at most $\beta^{-1}\rho((2\beta)^{-1}-1)$. The factorial bound is $<1$ for the stated small $\beta$: writing $x=(2\beta)^{-1}>500$ and $r=\lfloor x-1\rfloor\ge499$, one has $\beta^{-1}=2x<2(r+2)<r!$. This proves (2).

Thus the **net** high-LCM term on the genuine rough sequence is not $o(SH/L)$ on these good moduli. This statement is compatible with a large signed contribution of either sign on subfamilies and makes no estimate on the exceptional moduli.
