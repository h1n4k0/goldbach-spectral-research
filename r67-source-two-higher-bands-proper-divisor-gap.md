# Two higher sparse bands with a genuine gap in the rough divisors

Use the exact squarefree central sum and sign of the [rough-complement theorem](r65-source-pointwise-rough-complements.md). Fix $0<\rho<1/2$, $0<\kappa<1/4$, $0<\delta<1/6$, and both pairs of band constants $0<c_i<d_i<\infty$. For every sufficiently large even $N$ put $L=\log N$, $\ell=\log L$, $T=L/\ell$, and

$$
 D=\lfloor\sqrt N e^{-20T}\rfloor,\qquad Q=\lfloor N e^{-20T}\rfloor,\qquad
 I_0=[\rho N,(1-\rho)N].
$$

Consider squarefree central units $n=su,\ m=tv$ with $s,t>1$, where all primes of $s,t$ are in their respective higher sparse bands $[\exp(c_i T),\exp(d_i T)]$, and all primes of the nonempty $u,v$ are $\ge N^\kappa$. There is **no whole-product cap** on $s,t$ in this selection. Require on the designated first side that

$$
    f\mid u,\quad 1<f<u
       \quad\Longrightarrow\quad
          f\notin [N^{1/2-\delta},N^{1/2+\delta}].
 \tag{1}
$$

The other side need not satisfy (1). This is an integer mask on the rough part, not a restriction on which divisor labels are summed. In particular it includes every first rough part which is a single prime, and also admits fixed multiple rough factors on either side.

**Theorem (unconditional, pointwise).** For each fixed $A>0$, all sufficiently large even $N$ and all hard $I\subseteq I_0$, the genuine signed block

$$
 R_N(I)=-
 \sum_{\substack{n+m=N,\ n\in I,\ m\in I_0\\(nm,N)=1,\ n,m\ {\rm selected}}}
 \ \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
          \mu(d)\mu(e)\log(n/d)\log(m/e)
$$

satisfies

$$
     |R_N(I)|\ll_{\rho,\kappa,\delta,c_i,d_i,A}
         \mathfrak S(N)\left(\frac{|I|}{(\log\log N)^2}
                                        +N L^{-A}\right).
 \tag{2}
$$

This holds under any additional masks on the outer integers that are independent of the interior divisor labels, and in the other orientation by reflecting $I$ to $N-I$. Both higher bands are present, with no small-prime anchor: the hypothesis replacing the lower-band advantage in the [unanchored sparse-band theorem](r66-source-unanchored-sparse-intermediate-bands.md) is (1) and fixed polynomial roughness. No unrestricted two-higher-band statement, fixed-target main term, or Hypothesis S assertion is made.

## 1. Sparse Rankin tail at each target

Let $\varepsilon=\delta/4$. We may temporarily assume $s,t\le N^\varepsilon$ at cost $O_A(NL^{-A})$ on the original signed sum. Each rough part has at most $\lfloor1/\kappa\rfloor$ actual prime factors, so the total absolute divisor mark on a side is $O_\kappa(L\tau(s))$ or $O_\kappa(L\tau(t))$. Cauchy on $n+m=N$, counting multiples of a fixed lower product by at most $N/s$, bounds the cost of one tail by $O_\kappa(NL^2)$ times the geometric mean of its squared reciprocal tail and the other side's total squared reciprocal moment. Mertens gives $\sum_{p\ \mathrm{in\ band}}1/p=O_{c_i,d_i}(1)$ because the log endpoint ratio is a fixed constant. The unrestricted moments are therefore bounded by $\prod_{p\ \mathrm{in\ band}}(1+4/p)=O(1)$. Rankin for the tail at exponent $K_0/T$ for any fixed $K_0>0$ gives

$$
 \sum_{\substack{s>N^\varepsilon,\ s\ {\rm squarefree}\\
                                p\mid s\Rightarrow p\ {\rm in\ band}}}
      \frac{\tau(s)^2}{s}
 \le L^{-\varepsilon K_0}
           \prod_{p\ {\rm in\ band}}\left(1+\frac{4e^{d_iK_0}}p\right)
 \ll_{c_i,d_i,K_0} L^{-\varepsilon K_0}.
 \tag{3}
$$

Choose $K_0$ in terms of $A,\varepsilon$ to absorb the square-root loss and the $L^2$ mark factor, and repeat for the other tail. Thus the polynomial cap used in the proof is not a new sector restriction or an unproved cancellation.

## 2. Exact orbit cancellation on the side with the gap

After truncation, $s,t<D$ and $u,v\ge \rho N^{1-\varepsilon}>\sqrt N$. In the designated slot, the full rough label $u$ is above $N^{1/2+\delta}$ for large $N$; the empty label has largest possible lower divisor $s<D$. For a proper label $f\mid u$ below $N^{1/2-\delta}$ all divisors $a f$ with $a\mid s$ are at most $N^{1/2-\delta+\varepsilon}<D$ eventually, since $20T=o(L)$. If $f>N^{1/2+\delta}$ then all $a f>D$, and for each actual opposite $e>D$,

$$
        e\,a f\ \ge (D+1)f
                   > N^{1+\delta}e^{-20T}>Q.
$$

Thus the product cutoff is genuinely automatic for the selected first labels, not for untested two-higher bands. Since $s,u$ are coprime and $s>1$, the complete signed lower orbit of such an $f$ is exactly

$$
 \sum_{a\mid s}\mu(a f)\log(n/(a f))
       =\mu(f)\Lambda(s).
 \tag{4}
$$

Squarefreeness then leaves only $s=q$ a lower prime. Its first weight, including the bounded signed sum over high $f$, is at most $O_\kappa(\log q)$ in absolute value. All terms for composite $s$ have canceled against each actual opposite long divisor separately. The genuine opposite divisor test that remains is exactly $e>D$.

On the opposite side take the [exact single least-prime switch](r64-source-least-prime-toggle-first-moment.md) with $b=P^-(t)$. Fix a rough label $g\mid v$ and a lower divisor $a'\mid t/b$ and write $x=a'g$. The two possible divisors $x,bx$, including their signs, contribute

$$
 \mu(x)\left[-\log(m/x)\,\mathbf1_{\,x\le D<bx}
                       +(\log b)\mathbf1_{\,bx>D}\right].
 \tag{5}
$$

The heavy switch cannot have an empty or full rough label, by $t<D$ and $v>\sqrt N$. For fixed $a'$ it confines $\log g$ to an interval of length $\log b$ by $D/b<x\le D$. No restriction on the labels from the second leg was used to derive (5).

## 3. Polynomial-depth affine sieve and main bounds

For the light term of (5) freeze $h=q,k=t$, leaving both entire rough parts as the remaining two variables. For its heavy term freeze $h=q,k=tg$ and leave $u,v/g$. These are nonempty rough products in either case, and $hk\le N^{1/2+2\varepsilon}$ using $g\le D$ on the switch. The thin interval from (5) depends on the frozen lower label, not on the remaining two variables. On every true frozen pair, $(h,k)=1$ and $(hk,N)=1$ by the exact unit masks on $n+m=N$.

The positive affine sieve from the rough-complement theorem can now use **polynomial** depth. Put $\omega=1/2-2\varepsilon>0$, $Z=N^{\omega/24}$, $z=Z^\eta$ with fixed $0<\eta<\min(\eta_0,24\kappa/\omega)$ and $\eta_0$ the absolute small sieve constant. The remaining products have no primes at most $z$ since $z<N^\kappa$. The forms on $hP+kV=N$ have determinant $N$ up to sign and their interval has length $|I|/(hk)$. The nonzero frozen coprimalities give the same local roots: one at primes dividing $N$ or $hk$ (including 2), two otherwise. Thus the same quadratic Selberg weights give main upper term

$$
 O_{\kappa,\delta}\!\left(
   \frac{\mathfrak S(N)|I|}{hk L^2}\lambda^*(h)\lambda^*(k)\right),
       \qquad \lambda^*(w)=\prod_{p\mid w,\ p>2}\frac{p-1}{p-2},
$$

and lattice error $O(Z^6)=O(N^{\omega/4})$ per pair, including hard endpoint floors. The denominator is $L^2$ rather than $T^2$ because $\log z$ is a fixed positive multiple of $L$. The total count of frozen pairs $hk\le N^{1-\omega}$ is $O(N^{1-\omega}L)$. Their lower/rough splits are unique since the prime ranges are disjoint. Each $t\le N^\varepsilon$ has $\tau(t)=N^{o(1)}$ uniformly (split its distinct primes at $\sqrt L$); the free rough-label choices are bounded in terms of $\kappa$. With all logs at most $L$, the summed lattice error is $O(N^{1-3\omega/4+o(1)})$, hence $O_A(NL^{-A})$. Only the positive reciprocal profiles may now drop the frozen masks.

Since the lower bands are sparse,

$$
 \sum_{q\ \mathrm{in\ first\ band}}\frac{\lambda^*(q)\log q}{q}\ll T,\qquad
 \sum_{\substack{t\ {\rm squarefree}\\p\mid t\Rightarrow p\ {\rm in\ second\ band}}}
     \frac{\tau(t)\lambda^*(t)}{t}\ll1 .
 \tag{6}
$$

The second is the Euler product $1+2\lambda^*(p)/p=1+O(1/p)$ over the sparse band. Its log-marked version with $\log P^-(t)$ inserted is $O(T)$. The light term of (5) uses those two log-marked profiles and the sieve factor $L^{-2}$, giving $O(\mathfrak S(N)|I|T^2/L^2)$. In the heavy term, for fixed lower labels the nonempty rough product $g$ lies in one log interval of width $W=\log b=O(T)$. Its reciprocal mass is $O_\kappa((1+W)/L)$: fix all but one of its bounded number of rough prime factors, and use Chebyshev on unit log intervals for the remaining polynomial-sized prime. The other rough reciprocals, and the local multiplier from $g$, are bounded by constants depending on $\kappa$. The heavy mark is at most $L$; use the $O(T)$ first profile and the ordinary second profile (6). This gives the same main bound $O(\mathfrak S(N)|I|T^2/L^2)$. Equations (3) and (5), and $T/L=1/\ell$, prove (2). Both orientations preserve the exact sign because the transformation $n\leftrightarrow m$, $I\leftrightarrow N-I$ is on the original sum.

For a genuine multi-rough example, fix an external scale $X$, choose distinct lower primes $s,t$ at interior exponents of their respective higher bands, and then three distinct rough primes on each side near $(X/(2s))^{1/3}$ or $(X/(2t))^{1/3}$, with all constituents distinct. The ordinary PNT supplies them in narrow proportional windows. The resulting $N=su+tv$ is even, both integers are central units, and $\log N=\log X+O(1)$. The change of $L/\log L$ under this shift is $O(1/\log L)$ by its derivative, so the moving narrow proportional windows preserve the interior lower band membership. Every proper rough label has exponent $1/3+o(1)$ or $2/3+o(1)$, hence lies outside (1)'s interval for $\delta<1/6$. The long rough labels on either side are the three two-prime labels and the three-prime label, with total Möbius sign $3-1=2$. All product tests on them are automatic, and both marked lower orbits have $\Lambda(s)=\log s$, $\Lambda(t)=\log t$. The pair therefore contributes the actual summand $-4\log s\log t$. This only witnesses a nonzero sector. The near-half case in which both rough parts admit a proper divisor within the forbidden interval remains outside (2).
