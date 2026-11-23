# The original signed sharp product without a squarefree or least-prime gate

**Scope.** This evaluates the **complete central sharp product**, including nonsquarefree partners, unconditionally on almost all even moduli and simultaneously in their original cells. No midpoint replacement or approximation to the arithmetic divisor coefficients is made. A positive modulus-dependent term comes from the sharp cutoff, not from prime representations. Since the transfer uses Bessel over the target modulus, it gives no bound for a prescribed exceptional modulus and neither proves Hypothesis S nor a new pointwise Goldbach theorem.

Fix $A_0>0$, $B>0$, and $J\ge1$. Let even $N\in[X,2X]$, $L=\log N$, $\ell=\log X$, $m=N-n$, $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$, and $\Sigma(N)$ be the binary singular series. Use every original half-open cell $I\subset(N/2,9N/16]$ of length $H=N/(16\lceil L^J\rceil)$ and the exact cut $D_N=\sqrt N L^{-B}$. Define

$$
 F_{0,D}(m)=\sum_{\substack{e\mid m\\e\le D}}\mu(e),\qquad
 F_{1,D}(m)=\sum_{\substack{f\mid m\\f\le D}}
               \mu(f)\left(1-\frac{2\log f}{\log m}\right),\qquad
 G_D=F_{0,D}F_{1,D}-F_{0,D}.
$$

Put $K_N=\varphi(N)/N$ and for an integer $w\ge1$ set $R_w(t)=\sum_{h\le e^t,\,(h,w)=1}\mu(h)/h$. Define the convergent quadratic coefficient

$$
 \mathcal Q_N^{\rm all}
   =\sum_{\substack{j\ge1\\(j,N)=1}}\frac{\mu(j)}{j^2}
                     \int_0^\infty R_{Nj}(t)^2dt,\qquad
 \mathcal D_N^{\rm all}=\frac{K_N}{\Sigma(N)}\mathcal Q_N^{\rm all}.
                                                                  \tag{1}
$$

Uniformly for even $N$, $c K_N^2\le \mathcal D_N^{\rm all}\le C$ for absolute constants $c,C>0$. Outside $O_{A_0,B,J}(X\ell^{-A_0})$ even moduli, in every original cell of each remaining modulus, **with no restriction on the partners**,

$$
 \begin{split}
 \sum_{n\in I}\lambda(n)F_{0,D_N}(m)
    &=O\!\left(\frac{\Sigma(N)H}{L^2}\right),\\
 \sum_{n\in I}\lambda(n)G_{D_N}(m)
    &=\Sigma(N)\int_I
       \frac{1+2\mathcal D_N^{\rm all}
                   \left(\frac12\log(N-u)-\log D_N\right)}
            {\log(N-u)}\,du
       +O\!\left(\frac{\Sigma(N)H}{L^2}\right).
 \end{split}                                                       \tag{2}
$$

Subtracting the [full squarefree estimate](r63-spectral-full-squarefree-crt-strip.md) evaluates the actual signed nonsquarefree contribution, with coefficient $\mathcal D_N^{\rm all}-\mathcal D_N$, whose sign is not asserted here. Both formulas have their exact original divisor endpoints. The proof below works directly with all integers and does not use the squarefree midpoint parity identity.

## 1. Exact four-factor model on the major arcs

On every $m>1$, squarefree or not, a nonzero term of the mixed product has $e=ab$, $f=ac$, $a=(e,f)$, and $m=abcd$. Here $a,b,c$ are squarefree and pairwise coprime, but **there is no coprimality or squarefree restriction on $d$**. The sign is $\mu(b)\mu(c)$. On $V=[X/3,2X]$ the cut $D$ frozen at $N_0$ from the [direct sharp-cut proof](spectral-midpoint-direct-sharp-subpower-cut.md) satisfies $D<\sqrt m$ for large $X$. Consequently the exact formula for the product $P_D=F_{0,D}F_{1,D}$ there is

$$
 P_D(m)=
 \sum_{\substack{abcd=m\\a,b,c\ {\rm squarefree,\ pairwise\ coprime}\\
                             a\max(b,c)\le D}}
      \mu(b)\mu(c)\left(1-\frac{2\log(ac)}{\log m}\right).
                                                                  \tag{3}
$$

The weight is in $[0,1]$ on this support. Both $P_D$ and $F_{0,D}$ are bounded by $\tau_4(m)$ and have squared torus norm $O(X\ell^{15})$, by $\tau_4^2\le\tau_{16}$.

Use the original target mesh of width at most $X\ell^{-J-12}$, also cutting at changes of $\lceil L^J\rceil$, and its $O_J(\ell^{2J+12})$ frozen first intervals $I_0$. Let $E=A_0+4J+40$, $C_0=10(E+1)$, and $Q=\ell^{C_0}$. On major arcs $h/q+\eta$ with $(h,q)=1$, $q\le Q$, $|\eta|\le2Q/X$, first remove the two disjoint true sectors $b>X^{1/10}$ and $c>X^{1/10}$ with $b\le X^{1/10}$. Fix the other variables and apply the [masked Möbius estimate in arbitrary residue classes](r63-spectral-full-squarefree-crt-strip.md#1-exact-arithmetic-strip-and-major-arc-one-variable-estimates) to the chosen signed variable with the exact coprimality to $a$ and the other signed variable. The physical cut and $a\max(b,c)\le D$ give an interval in that variable. Its weight is monotone and bounded on that interval, and the slow phase has variation $O(1+Q)$. Since the chosen variable exceeds $X^{1/10}$, partial summation and summing its residue classes give arbitrary log savings on its scale. Summing reciprocal weights of the fixed three factors costs $O(\ell^3)$, so the two true large-signed sectors together are $O_A(X\ell^{-A})$ for every fixed $A$ on the major arcs. The variable masks do **not** impose coprimality with $d$.

In the remaining bulk $b,c\le X^{1/10}$, each admissible $d$ has $d\ge X^{.39}$, since $a b c\le D\min(b,c)$ and $m\in V$. At fixed such $a,b,c$ the complete period average of $e(h\,abcd/q)$ in $d$ is exactly $\mathbf1_{q\mid abc}$. Partial summation for the bounded-variation $\eta$ phase and centered weight leaves an error $O(q(1+Q))$ for each triple, for all strict or weak integer endpoints. The number of candidate triples is $O(X^{1-.39}\ell^3)$ by summing $X/(abc)$ with the minimum scale $X^{.39}$, so these errors are superlogarithmically small on scale $X$. Writing $x=abcd$ for the real variable gives the right main Fourier density on $V$

$$
 A_{P,q}(x)=
 \sum_{\substack{b,c\le X^{1/10}\\a\le D/\max(b,c)\\
                 a,b,c\ {\rm squarefree,\ pairwise\ coprime}\\q\mid abc}}
     \frac{\mu(b)\mu(c)}{abc}\left(1-\frac{2\log(ac)}{\log x}\right).
                                                                  \tag{4}
$$

Similarly the exact low expansion $m=bd$, $b\le D$, $\mu(b)$ signed, $d$ unrestricted of scale at least $X^{.49}$ gives the density $A_{\rm lo,q}(x)=\sum_{b\le D,\ q\mid b}\mu(b)/b$ on $V$. All major errors are $O_A(X\ell^{-A})$ for every fixed $A$. There is no dependence on the reduced numerator in either right main term.

## 2. Complete the singular series before evaluating the density

On squarefree $q$, assign each prime of $q$ to its forced factor among $a,b,c$ in (4); at most $3^{\omega(q)}$ assignments occur and the reciprocal gain is $1/q$. Summing the other weights harmonically, and using bounded variation of the centered weight as a function of $x\in V$, gives supremum and variation $O(\ell^3 3^{\omega(q)}/q)$ for the density extended by zero off $V$. The bound includes the low density. The first polynomial has the standard major factor $\mu(q)/\varphi(q)$ times the Fourier transform of $\mathbf1_{I_0}$. Thus after summing numerators the multiplier is $\mu(q)c_q(N)/\varphi(q)$; nonsquarefree $q$ have zero main term. This is the same tail mechanism as in the squarefree CRT proof: for each fixed $N$ the complete main sum in (4) is finite because $q\mid abc$, and the mean absolute tail beyond $Q$, uniformly in all frozen cutoffs and $x\in V$, is $O(X\ell^3Q^{-1/2})$. Indeed $\sum_{N\le2X}|c_q(N)|\le2X\tau(q)$ and $\sum_{q\ {\rm sf}}3^{\omega(q)}\tau(q)q^{1/2}/(q\varphi(q))<\infty$. Markov at $\ell^{-2}$ costs $O(X\ell^5Q^{-1/2})$ exceptions. The Fourier tails on retained arcs are $O(XQ^{-1}\ell^3(\log(2Q))^{C_1})$ by the two variations and the reciprocal divisor sum; the major approximation errors are negligible upon choosing their exponent large enough.

On minor arcs the first polynomial has sup $O(X\ell^{-E})$ by Vaughan. With the right divisor moments in Section 1, Bessel on integer targets, threshold $X\ell^{-J-2}$ and the union over frozen intervals cost $O(X\ell^{31+4J-2E})$ exceptions. Both budgets are at most $O(X\ell^{-A_0})$. Thus for every good modulus and each cell the actual expressions are the real integrals of the combined full-$q$ densities at $x=N-u$, with additive $O(\Sigma(N)H/L^2)$. The original intervals, and $D_N$ in place of the frozen $D$, will be restored at the end.

The sum of $\mu(q)c_q(N)/\varphi(q)$ over $q\mid abc$ is the exact factor $\prod_{p\mid abc}V_p$, where

$$
 V_p=1-\frac{c_p(N)}{p-1}
       =\begin{cases}0,&p\mid N,\\ p/(p-1),&p\nmid N.\end{cases}
                                                                  \tag{5}
$$

Write $w_N(h)=\prod_{p\mid h}V_p$ on squarefree $h$. The combined low is $\sum_{b\le D}\mu(b)w_N(b)/b$. It is $O_A(\ell^{-A})$ by the signed cumulative estimate in Section 4, with prime coefficient $V_p/p=1/(p-1)=1/p+O(p^{-2})$ off $N$. The combined product density from (4) is **exactly**

$$
 A_P(x)=\sum_{\substack{b,c\le X^{1/10}\\(b,c)=1}}
    \frac{\mu(b)\mu(c)w_N(b)w_N(c)}{bc}
     \sum_{\substack{a\le D/\max(b,c)\\(a,bc)=1}}
     \frac{\mu^2(a)w_N(a)}a
         \left(1-\frac{2\log(ac)}{\log x}\right).
                                                                  \tag{6}
$$

Zeros of $w_N$ impose all required $N$-units in these signed factors, including exclusion of $p=2$ for even $N$.

## 3. The harmonic constants and signed polynomial

For $v=bc$, with $(bc,N)=1$ on nonzero outer weights, put $g_v(a)=\mu^2(a)w_N(a)\mathbf1_{(a,v)=1}$. For the log-shifted Dirichlet series let

$$
 \sum_a\frac{g_v(a)}{a^{1+s}}=\zeta(1+s)\,K_v(s),\qquad
 K_v(s)=K_\varnothing(s)\prod_{p\mid v}(1+V_p p^{-1-s})^{-1},
 \quad
 K_\varnothing(s)=\prod_p(1-p^{-1-s})(1+V_p p^{-1-s}).
                                                                  \tag{7}
$$

The product is analytic near $s=0$. If $g_v=1*k_v$, its Euler coefficients at $p\nmid Nv$ are $k_v(p)=O(1/p)$, $k_v(p^2)=O(1)$, with higher ones zero, and at $p\mid Nv$ only $k_v(p)=-1$ is nonzero. Thus $\sum |k_v(a)|a^{-3/4}\ll_\epsilon(Nv)^\epsilon$. This verifies convergence of (7) and its differentiated series locally, and the harmonic estimates below with power-saving errors. Importantly,

$$
 K_v(0)=K_N\prod_{p\mid v}(1+V_p/p)^{-1},\qquad
               \frac{V_p/p}{1+V_p/p}=\frac1p\quad(p\nmid N).
                                                                  \tag{8}
$$

The first formula uses the cancellation $(1-1/p)(1+V_p/p)=1$ for $p\nmid N$ and the factor $1-1/p$ otherwise.

Let $B_0(v),B_1(v)$ denote the constant and linear terms in the expansion of $\zeta(1+s)K_v(s)$ at zero after its pole $K_v(0)/s$. For $Y=D/\max(b,c)\ge X^{.39}$ the two real harmonic estimates are

$$
 \begin{split}
 \sum_{a\le Y}g_v(a)/a&=K_v(0)\log Y+B_0(v)+O(X^{-\epsilon_0}),\\
 \sum_{a\le Y}g_v(a)\log a/a&=\tfrac12K_v(0)(\log Y)^2-B_1(v)
                                   +O(X^{-\epsilon_0})
 \end{split}                                                       \tag{9}
$$

for an absolute $\epsilon_0>0$, uniformly here. To verify (9), convolve $g_v=1*k_v$ and insert $\sum_{r\le u}1/r=\log u+\gamma_{\!E}+O(1/u)$ and $\sum_{r\le u}(\log r)/r=\tfrac12\log^2 u+\gamma_1+O((1+\log u)/u)$, where $\zeta(1+s)=1/s+\gamma_{\!E}-\gamma_1s+O(s^2)$. These harmonic constants and their signs follow either from Abel summation or the expansion of $\zeta$. Extend the $k_v$ sums to infinity: each error is $O(Y^{-1/4}(1+\log Y)^2\sum |k_v(a)|a^{-3/4})$. Since $Nv\le2X^{1.2}$, a fixed sufficiently small $\epsilon$ in that moment gives the claimed power. This also shows the signs in (9), in particular the minus before $B_1$.

Define the one-variable additive prime weights
$A(h)=\sum_{p\mid h}(\log p)/p$ and $C(h)=\sum_{p\mid h}(1/p)(1-1/p)(\log p)^2$ on $N$-units. The log derivatives of $K_v$ give

$$
 \frac{B_0(bc)}{K_v(0)}=\gamma_{\!E}+k_1+A(b)+A(c),\qquad
 \frac{B_1(bc)}{K_v(0)}
   =-\gamma_1+\gamma_{\!E}M
       +\tfrac12\bigl(M^2+k_2-C(b)-C(c)\bigr),
 \quad M=k_1+A(b)+A(c),
                                                                  \tag{10}
$$

where $k_i$ is the $i$th log derivative of $K_\varnothing$ at zero, independent of $b,c$. This follows from (7): an excluded local prime has first log derivative $(\log p)/p$ and second log derivative $-(1/p)(1-1/p)(\log p)^2$. For $i=1,2$, $k_i=O(1+L^i)$ from absolutely convergent off-$N$ factors and summing the finite prime divisors of $N$. The errors in (9) remain power-saving after summing $b,c$ in (6), since $\sum_{h\le X^{1/10}}\mu^2(h)w_N(h)/h\ll\ell^2$ by Euler products. Formula (8) absorbs the outer weights exactly into $K_N\mu(b)\mu(c)/(bc)$ on $(bc,N)=1$.

With $t=\log x$, $d_0=\log D$, $y=\log b$, $v_0=\log c$, $r=\max(y,v_0)$, the leading harmonic polynomial from (9) is

$$
 (d_0-r)-\frac{2v_0(d_0-r)+(d_0-r)^2}{t}.
                                                                  \tag{11}
$$

The constants also contribute
$(1-2v_0/t)B_0(bc)/K_v(0)+2 B_1(bc)/(t K_v(0))$.
All these polynomials are summed on the symmetric rectangle $b,c\le X^{1/10}$ with symmetric signed weights and coprimality, so the quadratic piece $2v_0r-r^2$ in (11) can be replaced in its total sum by $yv_0$: the average of the two swapped expressions equals $yv_0$ identically. The linear coefficient of $r$ in (11) is $-1+2d_0/t=-2\Delta(x)/t$, where $\Delta(x)=\tfrac12\log x-\log D$. The remaining terms of (11) are constant or one-variable, apart from the symmetric quadratic $yv_0/t$.

## 4. Complete the signed block, with errors before its constants

We record the cumulative estimates used in this completion. For a prime array $\beta_p=0$ on $p\mid w$, $\beta_p=1/p+O(p^{-2})$ otherwise, as in the squarefree CRT proof, the additive log kernel $(1-\beta_p Z)/(1-Z/p)$ gives the uniform bound

$$
 \left|\sum_{h\le e^u}\mu(h)\beta(h)\right|
 \ll (w/\varphi(w))e^{-c\sqrt u}+O_\epsilon(w^\epsilon e^{-u/8})
                      \qquad(u\ge2),                            \tag{12}
$$

as well as $L^1,L^2$ norm bounds $O(w/\varphi(w))$ for the cumulative on $u\ge0$. Indeed the kernel has absolute mass $O(w/\varphi(w))$, quarter-power moment $O_\epsilon(w^\epsilon)$, and one applies the ordinary reciprocal Mertens estimate to the remaining $h$ sum for log kernel coordinate $\le u/2$, and Rankin otherwise. For $w\le X^{1.3}$ and $u\gg\ell$ this gives arbitrary inverse powers of $\ell$, including integrated tails, by choosing a sufficiently small fixed $\epsilon$; the same for polynomial weights in $u$. In particular it proves the combined low bound noted in Section 2.

For the unmodified reciprocal coefficients on units, the first moment at length $Y=e^U$ obeys

$$
 \sum_{\substack{h\le e^U\\(h,w)=1}}\frac{\mu(h)\log h}{h}
            =-\frac{w}{\varphi(w)}+O_A(\ell^{-A})
      \qquad(w\le X^{1.3},\ U\gg\ell).
                                                                  \tag{13}
$$

This follows by Abel summation: the left side is $U R_w(U)-\int_0^U R_w(u)\,du$. The signed log convolution kernel for the excluded primes has total mass $w/\varphi(w)$. The unmasked primitive has integral $1$, since its Laplace transform is $1/(s\zeta(1+s))\to1$ as $s\downarrow0$ and is integrable by (12). Replacing the finite integral by the entire integral is justified by (12). Equations (12) and (13) also give

$$
 \sum_{\substack{h\le e^U\\(h,w)=1}}\frac{\mu(h)A(h)}h
                                       =O_A(\ell^{-A})
      \qquad(w\le X^{1.1},\ U\ge \ell/20,\ U\le \ell/10).
                                                                  \tag{14}
$$

To see this, expand the prime in $A(h)$, then set $h=pr$ with $(r,pw)=1$. The sum is
$-\sum_{p\le e^U,\,p\nmid w}(\log p)p^{-2} R_{pw}(U-\log p)$.
For $p\le e^{U/2}$ the new cutoff is at least $\ell/40$ and $pw\le X^{1.3}$, so (12) suffices and $\sum (\log p)/p^2$ converges. For larger $p$ the reciprocal-square tail is exponentially small and the cumulative is trivially $O(1+U)$. Fixed constant factors in the stated bounds on $w$ are harmless.

Now expand $(b,c)=1$ by $\sum_{j\mid b,c}\mu(j)$. Only squarefree $(j,N)=1$ can contribute, and writing $b=jb',c=jc'$ gives the common coefficient $\mu(j)/j^2$ on two identical signed arrays $\mu(h)/h$ with $(h,Nj)=1$, each cut at $e^{T-\log j}$, $T=\ell/10$. Here $b',c'$ must be coprime to $j$, and their mutual coprimality has been removed by inclusion–exclusion. For $j>e^{T/2}$ the absolute contribution of all polynomial terms of Sections 3–4 is exponentially small by $j^{-2}$, trivial harmonic sums and $O(\ell^{C_2})$ bounds on those terms. For smaller $j$ the common cut $U=T-\log j$ lies in $[\ell/20,\ell/10]$, and $w=Nj\le 2X^{1.05}$, so the preceding estimates apply. The total signed mass in either leg is $O_A(\ell^{-A})$; therefore any constant or one-legged term, even depending on $j,N$, is negligible after the other leg and the outer $j$ sum. For this inference all remaining sums and coefficients are at most polynomial in $\ell$ by trivial harmonic and additive weight bounds.

The term from $\max(y,v_0)=\log j+\max(\log b',\log c')$ has signed sum $-\int_0^\infty R_{Nj}(u)^2du+O_A(\ell^{-A})$ for each retained $j$. The one-legged term in the maximum is negligible and the residual $(\log b'-\log c')_+$ is evaluated by integrating inside its finite rectangle: it equals $R_{Nj}(U)\int_0^U R_{Nj}-\int_0^U R_{Nj}^2$, completed by (12). On summing $j$, this is precisely $-\mathcal Q_N^{\rm all}$; the infinite $j$ tail is exponentially small by the $L^2$ estimate and $j/\varphi(j)\ll_\epsilon j^\epsilon$. Its multiplication by $-2\Delta(x)/t$ in (11) thus contributes the positive $2\Delta(x)\mathcal Q_N^{\rm all}/t$.

For the quadratic $yv_0/t$, after expanding out the $\log j$ shifts and dropping constant or one-legged terms, (13) yields $(Nj/\varphi(Nj))^2/t$ for each retained $j$. In the constant terms from (10), the only possible mixed products are $A(b)\log c$ and $A(b)A(c)$ (or their equivalent swapped forms); all other terms are constant or one-legged. Their shifted parts are likewise one-legged, while the remaining $A(b')$ factor vanishes to arbitrary log order by (14). Thus they do not change the quadratic baseline. This explicitly accounts for both harmonic constants in (9). Finally the quadratic scalar is

$$
 K_N\sum_{(j,N)=1}\frac{\mu(j)}{j^2}
                   \left(\frac{Nj}{\varphi(Nj)}\right)^2
   =\frac{N}{\varphi(N)}
       \prod_{p\nmid N}\left(1-\frac1{(p-1)^2}\right)
   =\Sigma(N).
                                                                  \tag{15}
$$

The first equality is an absolutely convergent Euler product; the second includes $p=2$ through $2\mid N$. Thus (6) equals
$(\Sigma(N)+2K_N\mathcal Q_N^{\rm all}\Delta(x))/\log x$
with superlogarithmically small uniform error.

For positivity and size in (1), excluding primes of $j$ convolves $R_N$ with a positive log kernel of mass $j/\varphi(j)$ when $(j,N)=1$. Therefore the absolute $j>1$ contribution in (1) is bounded by
$\|R_N\|_2^2[\prod_{p\ge3}(1+(p-1)^{-2})-1]$, strictly less than $\|R_N\|_2^2$ because $\zeta(2)-1<\log 2$. Hence $\mathcal Q_N^{\rm all}\asymp\|R_N\|_2^2$, with absolute constants. Here $\|R_N\|_2^2\ge\log3$ and $\|R_N\|_2\ll N/\varphi(N)$ by (12). As $\Sigma(N)\asymp N/\varphi(N)$ for even $N$, the asserted uniform bounds on $\mathcal D_N^{\rm all}$ follow.

Apply Section 2 to these two actual densities and subtract the low from the product. Finally restore the true cells and $D_N$ using the endpoint and divisor hyperbola bounds from the direct sharp-cut proof, Section 2, with no roughness change required. They bound the true weighted changes by $O(H/L^2)$; the continuum changes are smaller by the explicit formula and the uniform bound on $\mathcal D_N^{\rm all}$. This proves (2). Positive signed cutoff drift is not evidence of additional prime representations; the result pertains to the actual sharp polynomial after averaging moduli and leaves the exceptional set without a pointwise estimate.
