# Exact sharp/low cancellation in the prime-free odd cofactor model

**Scope.** This is a prime-free calculation with **actual integer cofactors and exact Möbius parity**, not a bound for the genuine two-prime mixed strip. It explains a cancellation that must be preserved at the [remaining weighted odd count saddle](r72-spectral-moving-odd-weighted-saddle.md). We hold the real partner frequency $x$ fixed, use the exact sharp divisor formulas and their true two low-divisor geometries on $k$, but do not impose primality of $x/k$ or $N-x$, and do not impose $P^+(k)<x/k$. In particular neither a prime-pair bound nor the conditional genuine minor estimate follows from this calculation.

Let $0<\sigma<1/10$ and $B>B_0>0$ be fixed, with $N$ large and even, $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, $K=D N^\sigma$, and $x\in[7N/16,N/2]$ real. Put $h=\log(x/D^2)=2B\log L+O(1)$ and $U=\sqrt L$, $G=e^U$. The sum is over genuine integers $D<k\le K$ with $\mu(k)=+1$; thus $k$ is squarefree of even prime-factor count, the parity that would give odd $m=pk$ if $p$ were its new prime factor. Write

$$
 t=\log(k/D),\quad
 P_k=S_k(e^{t-})+S_k(e^{t-h}),\quad
 T_k=\int_{t-h}^{t} S_k(e^v)\,dv,\qquad
 X_k=\frac{hP_k^2-2P_kT_k}{\log x}.
 \tag{1}
$$

Here $S_k(y)=\sum_{r\mid k,r\le y}\mu(r)$ is zero for $y<1$ and $S_k(e^{t-})$ means a strict divisor cutoff at $e^t$. Formula (1) is precisely the sharp product from the odd-parity formulas at the formal complementary variable $p=x/k$.

Define the symbolic low term $Y_k=Y_k^{(1)}+Y_k^{(2)}$ by the following two exact divisor sums. In the first sum take positive integer $u\mid k$, $D<u\le H_0$, and coprime labels $a,b\mid u$ with $\max(a,b)<u/D$, and use weight

$$
 \mu(a)\mu(b)\{\log(x/u^2)+\log(ab)\}/\log x.
$$

In the second sum take positive integer $u\mid k$, $x/H_0\le u<x/D$, and coprime labels $a,b\mid k/u$ with $\max(a,b)<x/(uD)$, and use weight

$$
 \mu(a)\mu(b)\{\log(u^2/x)+\log(ab)\}/\log x.
$$

These are respectively the low LCM dividing $k$ and containing the distinguished factor: in the second case the low LCM is formally $x/u$. Since $x/k\gg N^{1/2-\sigma}L^B$ and the signed labels are polylogarithmic, none of these labels can contain that distinguished factor. The cutoff at $H_0$ and the strict short-label gates are the same as in the true mixed-strip formula.

Let $\mathcal S$ consist of these $k$ with

$$
 \left|\#\{p\le G:p\mid k,\ p\ {\rm prime}\}-2\log U\right|
           <12\sqrt{\log U\,\log L_2}.
 \tag{2}
$$

We prove that for an explicit constant $\mathcal C>0$ independent of $x,\sigma$,

$$
 \sum_{k\in\mathcal S}\frac{X_k}{k}
     =\sigma(h\mathcal C-1)+o(1),\qquad
 \sum_{k\in\mathcal S}\frac{Y_k}{k}
     =\sigma(h\mathcal C-1)+o(1).
 \tag{3}
$$

In particular the signed difference has reciprocal sum $o(1)$, although the two summands separately have positive main terms tending to infinity. The errors are uniform in the stated $x$ interval. All assertions in this note are unconditional.

## 1. Actual parity in the sharp reciprocal trace

First ignore (2). Counts beyond $J_*=\lfloor32\log U\rfloor$ contribute $o(1)$ by the [old weighted Rankin tail](r71-spectral-weighted-high-small-prime-count.md), since $|X_k|+|Y_k|\ll\tau_4(k)$ on the entire squarefree range. For the remaining counts write the actual $k=bv$ with $b$ the squarefree product of its primes at most $G$, and $v$ strictly $G$-rough. Then $b\le G^{J_*}=N^{o(1)}$. Take geometric cells of log width at most $\eta=L^{-100}$ on $(D,K]$. Write $H<v\le H'$ on a fixed cell at fixed $b$, of log width $w$ and $H\asymp k/b$. Every divisor label in the model and in a moving boundary envelope is at most $Z_k\ll k/D$ on this cell.

For a rough squarefree LCM $d$ of two such labels, the exact parity trace is

$$
 \sum_{\substack{H<v\le H'\\d\mid v,\ P^-(v)>G\\\mu(v)=\mu(b)}}\frac1v
 =\frac{w V_G}{2d}
 +O_A\left(\frac{wL^{-A}+e^{-c\sqrt L}}d+H^{-1/2+o(1)}\right),
 \qquad V_G=\prod_{p\le G}(1-1/p).
 \tag{4}
$$

For the parity-independent rough count the usual Bonferroni truncation of depth $\asymp L_2^2$ gives $wV_G/d+O_A(wL^{-A}/d+H^{-1+o(1)})$, as in the [exact local rough trace](r70-spectral-lowest-largest-prime-transfer.md). To require squarefreeness, exclude $p^2\mid v$ at $p>G$. The reciprocal count for multiples of $[d,p^2]$ has floor $O(1/H)$ per possible $p\le\sqrt {H'}$. Its main term summed over these primes is at most
$(w/d)(\sum_{p>G}p^{-2}+\sum_{p\mid d}p^{-1})=O_A(wL^{-A}/d)$ because $d$ is rough and at most a fixed power of $N$. This proves the squarefree count error in (4).

For the parity difference, on multiples of squarefree $d$, $\mu(v)=\mu(d)\mu(v/d)\mathbf1_{(v/d,d)=1}$. The remaining signed variable $v/d$ is at least $N^{1/2-\sigma-o(1)}$ at the interval's lower endpoint, since $d\ll(k/D)^2$. Masking primes up to $G$ and the additional primes of $d$ is the exact positive convolution with integers supported on those excluded primes. The reciprocal mask has exponential moment at $1/U$ of size $O(U)$: the small-prime part is the standard Mertens comparison from the [rough signed energy proof](r68-spectral-least-prime-conditioned-mixed-minor.md), and the forced rough primes add $O((L/U)e^{1-U})$ to the log. The ordinary bound $\sum_{n\le z}\mu(n)\ll z e^{-c\sqrt{\log z}}$ follows also by partial summation of ordinary reciprocal Mertens. Split the mask at $\sqrt z$ and use this bound below it, the exponential mask moment above it. Uniformly for $z\ge N^{1/2-\sigma-o(1)}$ on the present ranges the masked sum is $O(z e^{-c'\sqrt L})$. Partial summation then bounds the signed reciprocal count by $O(e^{-c''\sqrt L}/d)$ on the hard cell, without a lower bound on its width. Taking $(\mu^2(v)+\mu(b)\mu(v))/2$ gives (4).

When expanded in a square or bilinear product, the $1/d$ errors in (4) sum against a reciprocal LCM sum $L^{O(1)}$. The worst floor summed over label pairs is

$$
 Z_k^2 H^{-1/2+o(1)}
 \ll N^{-1/4+3\sigma/2+o(1)}
$$

by $Z_k\ll k/D$, $k\le K$, $H\asymp k/b$. This saves a power because $\sigma<1/10$. The count cutoff keeps all tag factors polynomial in $L$, all cell counts polylogarithmic and $\sum_b1/b\ll U$.

Apply (4) to the bilinear sharp product with comparison log variable $t$ averaged on each cell, before applying the reciprocal trace. As in the [signed Euler cell proof](r70-spectral-signed-shift-euler-slots.md), the difference from the true point is bounded by the unsigned brackets of width $O(\eta)$ for each shifted primitive, or by the integrated primitive brackets for $T_k$. The rough-square bounds with all counts through $J_*$ give aggregate squared bracket cost $O(L^{-5})$ (after summing $1/b$): the two contributions for the sharp endpoints are bounded by $(4^{J_*}L\eta/U^2+8^{J_*}\eta/U)\sum_b1/b$, and that for the integrated endpoints by $4^{J_*}\eta^2L/U$ times this harmonic factor. Dropping the parity mask only in these positive error squares is legitimate. The corresponding unshifted model squares have size $O(U^2)$ for $P$, $O(h^2U^2)$ for $T$, by the signed generating bound at $z=1$ in the [weighted count estimate](r71-spectral-weighted-high-small-prime-count.md). The actual squares obey the same upper bounds by the endpoint envelopes. Cauchy therefore shows that the total change in the signed product, including the factor $1/\log x$, is $o(1)$. The division by the log cell width in the average cancels its main trace factor; the uniform floors above remain harmless.

Use the gcd expansion of the signed LCM form. Write $R_{G,e}$ for the reciprocal Möbius primitive omitting primes at most $G$ and additionally those of a rough $e$, zero below log argument 0. Write $A_{b,e}(u)=\sum_{d\mid b}\mu(d)R_{G,e}(u-\log e-\log d)$, and put $P_{b,e}(u)=A_{b,e}(u)+A_{b,e}(u-h)$ and $T_{b,e}(u)=\int_{u-h}^{u} A_{b,e}(v)\,dv$. Strict and weak comparison cutoffs agree almost everywhere in the log integral. By (4) the sharp test before count restriction is

$$
 \sum_{\substack{D<k\le K\\\mu(k)=+1}}\frac{X_k}{k}
 =\frac{V_G}{2\log x}
   \sum_{\substack{b\ {\rm sf},P^+(b)\le G\\\omega(b)\le J_*}}\frac1b
   \sum_{\substack{e\le N^\sigma\\e\ {\rm rough}}}
     \frac{\varphi(e)\mu(e)^2}{e^2}
      \int_{0}^{\sigma L}(hP_{b,e}^2-2P_{b,e}T_{b,e})(u)\,du+o(1).
 \tag{5}
$$

The divisor bounds at finite $t$ justify the indicated upper support of $e$; extending $R_{G,e}$ afterwards does not change the finite cutoff expression.

## 2. The sharp asymptotic, including its constant term

Retain $e\le\exp(\sigma L-L^{3/4})$ in (5), and extend its $u$ integral to the real line. All terms vanish for $u<0$. For $u\ge\sigma L$ their log arguments exceed $L^{3/4}-O(U\log U+h)\ge L^{3/4}/2$ even after the largest shift. The pointwise reciprocal Mertens convolution bound for $R_{G,e}$ is $O(U(e^{-c\sqrt v}+e^{-v/(2U)}))$ at $v\ge0$, uniformly in these rough $e$. This is the same positive moment used in (4). Integrating the two decays on the tail gives a negligible error even after the polynomial tag weights, the $h$ factors, and the harmonic sums. The discarded terminal range of $e$ has reciprocal weight $O(L^{3/4}/U)$ by the rough harmonic estimate. For each such $e$, the aggregate absolute integral is $O(hU^2)$ by Cauchy and the $z=1$ Plancherel bound (using $\|T\|_2\le h\|A\|_2$), so its contribution to (5) is $O(hL^{-1/4})=o(1)$.

The harmonic weight of the retained $e$ equals $\sigma L V_G+O(L^{4/5}V_G)+o(1)$. For clarity, first omit $e<\exp(L^{4/5})$, whose weight by the rough interval bound is $O(1+L^{4/5}/U)$. On the remaining interval apply the same rough Bonferroni trace of log length $\sigma L-L^{3/4}-L^{4/5}$, with power-small floor in the lower endpoint and arbitrary fixed log tail. Excluding rough prime squares costs a negligible error: split into dyadic intervals with lower endpoint at least $\exp(L^{4/5})$, use the $p^2$ counts as in (4), and sum the convergent reciprocal prime-square tail. Finally $\varphi(e)/e=1+O((L/U)e^{-U})$ uniformly on rough $e\le N^\sigma$. These estimates give the stated main harmonic weight.

Use Fourier convention $\widehat f(\xi)=\int f(u)e^{-i\xi u}\,du$. Plancherel makes the full integral at fixed $b,e$ equal to the integral of $|\widehat R_{G,e}(\xi)q_b(\xi)|^2/(2\pi)$ times

$$
 h|1+e^{-ih\xi}|^2-4\sin(h\xi)/\xi .
 \tag{6}
$$

Indeed the multiplier of $T$ is $(1-e^{-ih\xi})/(i\xi)$ and the real cross multiplier with the sum of endpoint primitives is $2\sin(h\xi)/\xi$. The rate at $\xi=0$ is interpreted by continuity. The extra rough primes of $e$ change the squared transform from that of $R_G$ relatively by $O((L/U)e^{-U})$, uniformly in $\xi$. Extend the $b$ sum over all squarefree products of primes $\le G$ in this spectral integral; its discarded $j>J_*$ weights give total primitive-square energy $O(U^4 2^{-J_*})$ by the signed Euler generator at $z=2$ and the bound $I_0(2)\ll U^4$ of the weighted count proof. Even the factor $O(h)$ in (6) leaves $o(1)$ after normalization. These estimates involve only the already positive harmonic product and do not extend the original cofactor mask.

Let $R(u)=\sum_{n\le e^u}\mu(n)/n$, zero for $u<0$, and put

$$
 F(\xi)=\prod_{p}
  \frac{(1-1/p)^2\{1+(2-2\cos(\xi\log p))/p\}}
       {|1-p^{-1-i\xi}|^2},\qquad
 J(\xi)=|\widehat R(\xi)|^2F(\xi),\qquad
 \mathcal C=\frac1{2\pi}\int_{\mathbb R}J(\xi)\,d\xi.
 \tag{7}
$$

The local factors are $1+O(p^{-2})$ and their derivatives are $O((\log p)/p^2)$, uniformly in $\xi$. Thus $F$ is positive, bounded, and has bounded derivative, and its finite product through $G$ differs by $O(1/G)$ uniformly. The finite product in (7) is exactly $V_G^2$ times the squared smooth-mask Euler factor times $\prod_{p\le G}(1+|1-e^{-i\xi\log p}|^2/p)$ from the $b$ sum. With the harmonic $e$ estimate, formula (5) becomes

$$
 \frac{\sigma}{2}\frac1{2\pi}
   \int_{\mathbb R}\left[h(2+2\cos(h\xi))-4\frac{\sin(h\xi)}{\xi}\right]
                    J(\xi)\,d\xi+o(1).
 \tag{8}
$$

Here $L/\log x=1+O(1/L)$ and all relative errors above beat $1/h$.

Ordinary reciprocal Mertens gives $R,uR\in L^1\cap L^2$. Consequently $J\in W^{1,1}(\mathbb R)$ by Plancherel and the bounded derivative of $F$, and it is Lipschitz near zero. Integration by parts and the Riemann–Lebesgue lemma give $h\int J(\xi)\cos(h\xi)d\xi=o(1)$. The sine integral tends to $\pi J(0)$: subtract $J(0)\mathbf1_{[-1,1]}$ before dividing by $\xi$, then use the Riemann–Lebesgue lemma and the Dirichlet integral. Here $F(0)=1$ exactly, and $\widehat R(0)=1$ by taking the positive real Laplace parameter to zero in $\int R(u)e^{-s u}du=1/(s\zeta(1+s))$. The formula for $s>0$ follows by absolute Dirichlet series and integration of each primitive. Thus $J(0)=1$ and $\mathcal C>0$. Formula (8) is $\sigma(h\mathcal C-1)+o(1)$.

## 3. The low asymptotic from the two true complementary factors

For squarefree $u v=k$ with coprime factors, the two complementary branches of $Y_k$ use the same local density for a forced squarefree label $d=ab$ in the designated factor. The two-factor constants are

$$
 K_2=\prod_p (1-1/p)^2(1+2/p),\qquad
 \alpha_p=\frac1{p+2},\qquad \alpha(d)=\prod_{p\mid d}\alpha_p
 \quad(d\ {\rm squarefree}).
 \tag{9}
$$

Indeed two independent residues at each prime have allowed occupations $(0,0),(1,0),(0,1)$ in their valuations, with probabilities $(1-1/p)^2$, $(1-1/p)^2/p$, $(1-1/p)^2/p$, respectively. Forcing occupancy in the specified factor multiplies the local total by $\alpha_p$. The actual parity $\mu(uv)=+1$ introduces $1/2$ up to negligible signed error, as detailed next. This is ordinary squarefree cofactor averaging; there is no prime-progressions input in (9).

Here is a uniform justification within our hard ranges. In either branch the large factor $u$ is $N^{1/2+o(1)}$ in a log interval of width $O(L_2)$ with endpoints depending on $a,b$, and the small factor lies below $K/u$. First discard $v\le v_0=\exp(L^{4/5})$. By the harmonic counts for multiples of $ab$ in the appropriate factor and the weight $O(h/L)$, its total contribution after summing $a,b\le H_0/D$ is $O(L^{-1/5}L_2^{O_B(1)})=o(1)$: the short-log factor has length $O(L_2)$, the other at most $1+\log v_0$, and the labels cost $\sum_{a,b\le H_0/D}1/(ab)\ll L_2^2$. Floors in the large factor are exponentially small.

For $v>v_0$, enforce the unsigned squarefree condition through primes $p\le L^{C_0}$, with $C_0$ a sufficiently large fixed constant depending on $B$. All forced label primes are here. At $p\mid ab$ impose the allowed prescribed occupation exactly modulo $p^2$. At other small primes the forbidden event is $p^2\mid u$, or $p^2\mid v$, or $p\mid u,v$. Its density is $O(p^{-2})$. Upper and lower Bonferroni of depth $\asymp L_2^2$ have an arbitrarily small inverse-log main difference because the sum of these densities is bounded. Each retained joint residue condition uses a modulus $\exp(O_{B,C_0}(L_2^3))$, and the number of retained subsets and residue pairs is also at most $\exp(O_{B,C_0}(L_2^3))$. For each such pair apply the reciprocal progression count in $v$ with the exact upper endpoint $K/u$ and lower endpoint $v_0$, then in $u$ with the resulting continuous log factor and the original bounded-variation weight on its own original interval. This gives the corresponding density times the real two-factor integral: the ordinary floor errors cost $\exp(O(L_2^3))L^{O(1)}/v_0$ or less even after all residue pairs. No enlargement of the moving hyperbola is needed in these main terms.

The forbidden events at $p>L^{C_0}$ can be bounded without the label masks in the absolute errors. Partition both variables into dyadic intervals, each of log width at most $\log 2$. On a pair of cells, the sums over $p$ of the reciprocal two-factor counts for $p^2\mid u$ or $p^2\mid v$ cost $O(L^{-C_0})$ plus $O(u_{\rm lo}^{-1/2}+v_{\rm lo}^{-1/2})$ by summing the reciprocal floors up to each cell's square-root endpoint. For $p\mid u,v$ the main cost is again $O(L^{-C_0})$ and the crossed floor terms are $O((1+\log L)(u_{\rm lo}^{-1}+v_{\rm lo}^{-1}))$; the double floor is bounded using $p\le\min(u_{\rm hi},v_{\rm hi})$. Summing the polylogarithmically many cells and the polynomially many short label choices gives $o(1)$ by taking $C_0$ large. The Euler product tail in (9) is bounded by the same reciprocal prime-square tail. This proves the unsigned model uniformly within the hard conditions.

For the signed part of $(\mu^2(uv)+\mu(uv))/2$, fix $u$ and sum over $v$ in its true interval. If the label divides $v$, write $v=(ab)w$ on its nonzero support; if it divides $u$, leave $v$ unchanged. A shared forced prime gives zero. The remaining Möbius variable has only the coprimality mask with $u$ and possibly $ab$, and its lower endpoint is at least $v_0/L^{O_B(1)}$. The positive mask moment at $1/U$ is $O(U)$ for every such mask: use the bound for all primes up to $G$, and the primes larger than $G$ contribute a negligible log as their number is $O(L/U)$. Ordinary Mertens and the same split at the square-root endpoint give signed partial sums $O(z e^{-cL^{3/10}})$ uniformly on these ranges, followed by the reciprocal weighted count of this size without the factor $z$. The large factor's reciprocal sum and all the polynomially many labels are harmless. This proves that the signed parity discrepancy is $o(1)$.

Apply this to the two real integrals. In the second change back from $u$ to the common low-LCM quantity $l=x/u$; in the first put $l=u$. In each case $D\max(a,b)<l\le H_0$, and the centered weight is $(\log(x/l^2)+\log(ab))/\log x$. The two small-factor log lengths add to the constant $\log(K^2/(x v_0^2))$ along this common interval, since one upper endpoint is $K/l$ and the other $Kl/x$. Both exceed $v_0$ on the entire low range. If $A=(B-B_0)\log L$, changing to $s=\log(l/D)$ gives

$$
 \sum_{\substack{D<k\le K\\\mu(k)=+1}}\frac{Y_k}{k}
 = \frac{K_2\log(K^2/(xv_0^2))}{2\log x}
       \int_0^A\{hH_\alpha(s)+D_\alpha(s)\}\,ds+o(1),
 \tag{10}
$$

where

$$
 H_\alpha(s)=\sum_{\substack{a,b<e^s\\(a,b)=1}}
                      \mu(a)\mu(b)\alpha(a)\alpha(b),\qquad
 D_\alpha(s)=\sum_{\substack{a,b<e^s\\(a,b)=1}}
            \mu(a)\mu(b)\alpha(a)\alpha(b)(\log(ab)-2s).
$$

Terms are supported on squarefree labels; the choice of values at a finite or countable endpoint set is immaterial inside these integrals.

## 4. The matching Euler identities and the actual count restriction

Define $R_{\alpha,j}(u)=\sum_{n\le e^u,(n,j)=1}\mu(n)\alpha(n)$ on squarefree $n$, zero for $u<0$, and $I_{\alpha,j}(u)=\int_0^u R_{\alpha,j}(v)\,dv$ for $u\ge0$, zero otherwise. The convolution multiplier relative to $R$ is

$$
 \prod_p\frac{1-\alpha_p e^{-i\xi\log p}}{1-p^{-1-i\xi}}
          \prod_{p\mid j}(1-\alpha_p e^{-i\xi\log p})^{-1}.
 \tag{11}
$$

Each local ratio has a positive power-series expansion in $e^{-i\xi\log p}$ because $\alpha_p\le1/p$. The first product has bounded total reciprocal mass and finite first log moment: $1/p-\alpha_p=O(p^{-2})$, and the higher local exponents are geometric. The second product has mass at most $j/\varphi(j)$ and first log moment at most its mass times $O(1+\log j)$. Therefore $\|R_{\alpha,j}\|_\infty+\|R_{\alpha,j}\|_1\ll j/\varphi(j)$ and its first absolute $L^1$ log moment is $O((j/\varphi(j))(1+\log j))$. This also justifies (11) as an ordinary Fourier transform.

Expand the coprimality of the two labels by their common divisors. For almost every $s$ this gives

$$
\begin{split}
 H_\alpha(s)&=\sum_{j\ {\rm sf}}\mu(j)\alpha(j)^2
                       R_{\alpha,j}(s-\log j)^2,\\
 D_\alpha(s)&=-2\sum_{j\ {\rm sf}}\mu(j)\alpha(j)^2
                   R_{\alpha,j}(s-\log j)I_{\alpha,j}(s-\log j).
\end{split} \tag{12}
$$

The stated moment bounds and $\sum_j\alpha(j)^2(j/\varphi(j))^2(1+\log j)<\infty$ give $\int_0^\infty (1+s)|H_\alpha(s)|ds<\infty$ and $\int_0^\infty |D_\alpha(s)|ds<\infty$. In (10) one may extend the integral to infinity at error $o(1)$ because $h=O(A)$ and the first moment of $H_\alpha$ is finite. The prefactor without $K_2$ differs from $\sigma$ by $O(L^{-1/5})$; this also costs $o(1)$.

Plancherel in the first line of (12) and the absolutely summable $j$ series yield

$$
 K_2\int_0^\infty H_\alpha(s)\,ds
    =\frac1{2\pi}\int_{\mathbb R}|\widehat R(\xi)|^2F(\xi)\,d\xi
    =\mathcal C.
$$

Explicitly the $p$ factor, with $u_p=\xi\log p$, is

$$
 (1-1/p)^2(1+2/p)
    \frac{|1-\alpha_p e^{-iu_p}|^2-\alpha_p^2}{|1-p^{-1}e^{-iu_p}|^2}
 =\frac{(1-1/p)^2\{1+(2-2\cos u_p)/p\}}{|1-p^{-1}e^{-iu_p}|^2},
$$

which is exactly (7). Likewise $\int 2R_{\alpha,j}I_{\alpha,j}=I_{\alpha,j}(\infty)^2$ and the zero frequency of (11) is $I_{\alpha,j}(\infty)$, since $\widehat R(0)=1$. Hence the second line of (12) gives

$$
 -K_2\int_0^\infty D_\alpha(s)\,ds
   =\prod_p (1+2/p)\{(1-\alpha_p)^2-\alpha_p^2\}=1.
$$

All Euler series here can first be taken over finitely many primes after the absolutely convergent $j$ expansion. We have proved that (10) is also $\sigma(h\mathcal C-1)+o(1)$.

Finally (2) can be reinstated without changing either asymptotic. The [moving odd count proof](r72-spectral-moving-odd-weighted-saddle.md) establishes, **before any application to primes**, a positive reciprocal envelope for the absolute sharp product and for the absolute low sum outside that count window. Its proof of that envelope uses only the integer cofactor range, real $x$ cells and the exact $F_0,F_1$ and $Y_k$ formulas; the subsequent two-root sieve and major-arc steps are not used here. In particular its local-label and hard-envelope bounds are also valid on the present smaller range $D<k\le K$, which lies in $k\le 2N^{1-\kappa}$ for any fixed $0<\kappa<1/2-\sigma$. The formal distinguished factor $x/k$ exceeds $G$ and the short labels; no cofactor estimate uses the largest-prime gate once these formulas and ranges are fixed. For the width in (2) the off-saddle reciprocal bound for either term is $O(L_2^{-6})+o(1)$, with the nonnegative multiplier $k/\varphi(k)\ge1$ allowed. Thus dropping the out-of-window cofactors changes both signed sums by $o(1)$, proving (3). The leading and constant-term cancellation is confined to this prime-free cofactor model; preserving it in the genuine prime-weighted signed minor is unresolved.
