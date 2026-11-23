# Both parities cancel on average in the near-edge typical-count carrier

Use the exact fixed-scale carrier of the [typical-count masked obstruction](r72-source-typical-count-masked-obstruction.md), **deleting only its even-parity condition** on $\omega(W)$. Keep the true size and occupancy gates, prime alphabets, rigid near-edge carrier, strict original divisor cutoffs, and squarefree $N$-unit condition. In particular $\theta=1/20$, $a_i=0$, and the fixed $\rho,\Delta,\delta,\epsilon,\kappa$ and the prime exclusions are as in that obstruction. The two parities in each leg are included together. This does not remove the other restrictions defining the carrier.

For clarity, write $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\mathcal X=[X,(1+\Delta)X]$, $\mathcal J=[X/2,(1+\Delta)X/2]$ and

$$
 H_1=\sqrt{Q_X}\,e^{\kappa T},\qquad
 H_2=\sqrt{Q_X}\,e^{2\kappa T},\qquad
 Q_X=\lfloor X e^{-20T}\rfloor.
$$

The fixed mask, chosen before the target, now consists of all $n=S f F\in\mathcal J$ with $H_1\le Sf\le H_2$, $f,F$ prime, $S=sW$ with $s$ the one old lower prime, and the exact old $W$ selectors except parity. Thus $W\le X^{\epsilon/2}$, $\omega(W)\le 2\log\ell$, and the actual exceptional count is within $2(\log\ell)^{3/4}$ of $(1-\theta)\log\ell$. The exclusions at the moving cutoff boundaries, the ambient $I_0=[\rho N,(1-\rho)N]$, and the strict tests $d>D_N,e>D_N,de>Q_N$ are unchanged. All logarithms in those cutoffs use the actual target $N$. Let $R^{\mathrm{both}}_N$ be the original signed sum (1) of the [joint count theorem](r72-source-joint-middle-count-entropy.md) at $I=I_0$ with this same two-parity mask on both legs.

**Theorem (unconditional).** For all sufficiently large $X$,

$$
             \sum_{\substack{N\in\mathcal X\\2\mid N}}
                      |R^{\mathrm{both}}_N|^2
                    \ll_\rho X^3\ell^{-2/5}.
 \tag{1}
$$

For example $|R^{\mathrm{both}}_N|\le X\ell^{-1/10}$ for all but $O_\rho(X\ell^{-1/5})$ targets in this scale window. The factored convolution's major arc contribution is individually $O_\rho(\mathfrak S(N)X\ell^{-1/5})$ for every even $N$ in the window, with the actual unit correction individually negligible in the full convolution. The minor statement and the combined true sum estimate are in mean square; there is no all-target assertion. The earlier even-only lower bound concerns a different selection. Neither the general typical-count block, the unmasked central sum, nor Hypothesis S is settled.

## 1. Exact signed convolution and uniform unit exclusion

In the original near-edge proof, the geometry and eliminations of the two complete giant-label families did not use the parity selection. For every true coprime pair from the restored mask the sole surviving internal labels are the two maxima $Sf,Ug$, and their signs are $(-1)^{\omega(W)}$ and $(-1)^{\omega(W')}$. This uses the actual moving integer $D_N,Q_N$ as before: $F,G>\sqrt N$ and each complete giant family passes every opposite long label and sums to zero, while any proper label without its giant loses a factor at least $\exp(5T/4)$ and fails the product test. Thus define

$$
 a(n)=(-1)^{\omega(W)}\log F\quad(n=S f F\ {\rm in\ the\ restored\ mask}),
          \qquad \mathcal B(\alpha)=\sum_n a(n)e(\alpha n)
$$

and zero elsewhere, with $e(x)=e^{2\pi i x}$. The representation is unique; in fact already the integer $h=Sf$ determines $S,f$ because $f\ge X^{.4}$ and $S\le X^\epsilon$. The original signed mark is exactly $-a(n)a(m)$ on each true unit pair.

Every prime dividing a mask integer is at least $\exp(5T/4)$. Any nonunit pair with $n+m=N$ has a common prime dividing $N$. The number of such relevant prime divisors of $N$ is $O(\ell)$, and for each one the number of possible $n$ is $O(X/p)$ by counting multiples in $\mathcal J$. Since the two marks are $O(L^2)$ in product, the contribution of all nonunit pairs is individually $O(X L^2\ell e^{-5T/4})$, uniformly in the exact moving $N$. Consequently

$$
              R_N^{\mathrm{both}}
       =-\int_{\mathbb R/\mathbb Z}\mathcal B(\alpha)^2e(-N\alpha)\,d\alpha
                 +O(X L^2\ell e^{-5T/4})
 \tag{2}
$$

for every $N$ of interest. Both operands on the fixed carrier are odd and central. The positive reciprocal bound $\sum_S1/S\ll_\rho\ell$ of the earlier proof, and its uniform PNT bounds for each $S$, did not require the even-parity mask and still give
$\#\{n:a(n)\ne0\}\ll_\rho X/L$. In particular $\|\mathcal B\|_2^2\ll_\rho XL$ and $\|\mathcal B\|_\infty\ll_\rho X$ by the ordinary coefficient bounds.

## 2. A uniform minor supremum for the collapsed bilinear form

Set $P=L^C$, $Q_0=\lfloor X/P\rfloor$ with fixed $C$ large, and take major arcs $a_0/q+\beta$ with $q\le P$, $(a_0,q)=1$, $|\beta|\le1/(qQ_0)$, on the torus. They are disjoint for large $X$, since the sum of any two radii is less than the spacing of their reduced centers; their total measure is $O(P^2/X)$. On the complement Dirichlet approximation gives a reduced $a_0/q$ with $P<q\le Q_0$ and $|\beta|\le1/(qQ_0)\le q^{-2}$.

Collapse $h=Sf$, with coefficient $\pm1$ on its mask and zero otherwise, and keep $F$ prime with weight $\log F$. Before the sharp $hF\in\mathcal J$ condition, break the $h$ interval into $O(L)$ dyadic intervals $U<h\le2U$. From each take only $O(1)$ dyadic $F$ intervals $V<F\le2V$ that can meet the product window for some $h$ in this interval. Then $UV\asymp X$ and $U,V\le X^{.6}$ because $h\in[H_1,H_2]$. The two hard product endpoints can be separated without smoothing: replace them by equivalent strict half-integer endpoints, and use truncated Perron on each at $\sigma=1/L$, height $X^4$. On each dyadic rectangle all $hF\asymp X$; the nearest integer to the half-integer bound has log distance $\gg X^{-1}$, so the usual truncated Perron error
$O((x/(hF))^\sigma\min(1,1/(X^4|\log(x/(hF))|)))$ is $O(X^{-3})$ per term. The integral inserts a factor $h^{-\sigma-it}F^{-\sigma-it}$ into the existing coefficients and has total absolute kernel cost $O(L)$, including $x^\sigma=O(1)$. Thus it suffices to bound ordinary bilinear rectangles uniformly in these bounded twists. An interval with closed lower or upper endpoint is preserved by the corresponding half-integer choice.

If the coefficients on $h,F$ have absolute bounds $1,O(L)$ respectively, Cauchy in $h$ and the geometric sum in the difference of two $F$ variables give the squared upper bound

$$
 \ll U V L^2\left(U+\sum_{1\le d\le 2V}\min(U,\|d\alpha\|^{-1})\right)
 \ll U V L^2(1+V/q)(U+q\log(2q)).
 \tag{3}
$$

For the last estimate, in consecutive blocks of length at most $q/2$ the points $d\alpha$ are at circular distance at least $1/(2q)$: a nonzero difference of the indices is below $q$, and its perturbation from the rational progression is at most $1/(2q)$. The closest points to zero cost $O(U)$ in each block and the others sum harmonically to $O(q\log(2q))$. On the minor arcs the last two factors of (3), excluding $UVL^2$, are
$O(X L^{1-C}+X^{.6}L)$ using $UV\asymp X$, $P<q\le Q_0$. Absorbing both the Perron and dyadic costs, for any desired fixed $K$ a sufficiently large $C$ gives

$$
          \sup_{\alpha\in\mathfrak m}|\mathcal B(\alpha)|\ll_{\rho,K} X L^{-K},
       \qquad
          \int_{\mathfrak m}|\mathcal B(\alpha)|^4\,d\alpha
                     \ll_{\rho,K} X^3L^{1-2K}.
 \tag{4}
$$

The second estimate uses the actual unmodified coefficient energy. No parity balance or regularity of the binary $h$ mask is assumed in (3).

## 3. The exact major density with one prime progression input

On a major arc evaluate the prime $F$ variable via the ordinary Siegel–Walfisz theorem for the logarithmically weighted primes; all its endpoints are at least $X^{.4}$, $q\le L^C$, and no prime there divides $q$. In a reduced class the main term has density $1/\varphi(q)$. Partial summation against $e(\beta h F)$ costs $O(1+|\beta|X)$. This is uniform in the hard interval $\mathcal J/h$; a change of endpoint convention costs at most one prime logarithm. The per-class error can therefore be taken to be $O_{C,M}((X/h)L^{-M})$ for any $M$, after increasing the exponent in Siegel–Walfisz. Sum over reduced classes before using any cancellations in $h$. Because all prime factors of every admitted $h$ exceed $P$, this rational sum is $c_q(a_0h)=\mu(q)$, where $c_q$ is the Ramanujan sum. The real integral is $h^{-1}\widehat{\mathbf1_{\mathcal J}}(\beta)$ with the convention $\widehat{\mathbf1_{\mathcal J}}(\beta)=\int_{\mathcal J}e(\beta x)\,dx$. Since $\sum_h1/h\ll1$, the major formula uniformly is

$$
 \mathcal B(a_0/q+\beta)
       =\frac{\mu(q)}{\varphi(q)}\,C_X\,
                  \widehat{\mathbf1_{\mathcal J}}(\beta)+O_{\rho,C,M}(XL^{-M}),
 \qquad
 C_X=\sum_{S=sW}\frac{(-1)^{\omega(W)}}{S}
           \sum_{\substack{H_1/S\le f\le H_2/S\\ f\ {\rm prime}}}\frac1f .
 \tag{5}
$$

The sum defining $C_X$ has the exact fixed hard endpoints and all original $W$ conditions except the removed parity restriction. The uniform error in (5) absorbs the sum over at most $P$ residue classes. No distribution in progressions is demanded of $f$ or $S$.

## 4. The parity factor despite the hard size and count gates

By the ordinary PNT with an arbitrary inverse logarithmic error and partial summation, applied at endpoints $\ge X^{.4}$, the inner sum in (5) equals
$\int_{H_1}^{H_2}dh/(h\log(h/S))+O_M(L^{-M})$ for each $S$. The error is still of arbitrary inverse logarithmic size on summing $\sum_S1/S\ll\ell$. We bound the signed real density inside this integral.

Let $u=\log\ell$ and separate $W=W_0 W_1$, with $W_0$ using all eligible primes in the entire lower untagged interval $[\exp(4T),V_X/4]$, and $W_1$ using all other eligible primes. This first interval is below both removed neighborhoods in the carrier and contains no exceptional primes; the actual typical exceptional-count test therefore depends only on $W_1$. Let $P_0,P_1$ be the unrestricted Euler products of $(1+1/p)$ in the two alphabets, so $P_0P_1\asymp_\rho\ell$. Under this positive reciprocal measure, each prime is occupied with probability $1/(p+1)$ and the total mean count is $u+O(1)$. The moment of $2^{\omega(W)}$ is at most $\exp(u+O(1))$, so $\omega(W)>2u$ has probability $O(\ell^{-(2\log2-1)})$. The same argument gives at least this saving for the event that either separate count exceeds $3u$. Hence in the *density estimate* we may first remove the original total-count test and temporarily impose each separate count at most $3u$, at an absolute positive error after log integration
$O(\ell^{-(2\log2-1)})$: wherever the hard size gate holds, $\log(h/S)\asymp L$ and the original log integration length is $\kappa T$, and $P_0P_1 T/L\asymp1$. No change to the actual Fourier carrier is made.

The bound $\omega(W_0)\le3u$ gives $\log W_0\le \Delta_0=3u\log V_X=3uT\ell^\theta=o(L)$. On the retained hard size region $W_0W_1\le X^{\epsilon/2}$, replace $\log(h/(sW_0W_1))$ in the denominator by $\log(h/(sW_1))$, with uniform error $O(\Delta_0/L^2)$ per reciprocal weight. On integrating, this costs $O(\Delta_0/L)$. The hard size test differs from $W_1\le X^{\epsilon/2}$ only for $\log W_1$ in a strip of width $\Delta_0$ immediately below $\epsilon L/2$. A product in this strip with $\omega(W_1)\le3u$ has some prime with $\log p\ge\epsilon L/(12u)$ for large $X$. Freeze the other factors and count all choices of such a prime. Its harmonic weight in this log strip is $O((1+\Delta_0)u/L)$, by Chebyshev over unit log intervals. Summing the other reciprocal factors costs at most $P_1$, and multiplying by the whole positive low profile $P_0$ proves that deleting this size-test ambiguity costs $O((1+\Delta_0)u/L)$ after the integral. This covers either hard endpoint of the strip.

Now the remaining gates and the real denominator are independent of $W_0$. Remove its temporary count cap with the same positive moment bound, while keeping the true $W_1$ count and size gates as used in this density calculation. The signed sum over $W_0$ contributes $\prod_p(1-1/p)$ in place of $P_0$. By Mertens, $\sum_{\exp(4T)\le p\le V_X/4}1/p=\theta u+O(1)$, so the ratio is $O(\ell^{-2\theta})$. The remaining absolute $W_1$ profile is at most $P_1$, and the $s$ profile is bounded. The density bound after integrating is therefore

$$
        C_X\ll_\rho
             \ell^{-2\theta}+\ell^{-(2\log2-1)}
                      +(1+\Delta_0)u/L
                \ll_\rho \ell^{-1/10}.
 \tag{6}
$$

The last step uses $\theta=1/20$; the size strip and real-denominator loss are smaller powers. This factor is a signed assay of the very same product family, not an assumption that either parity by itself is sparse.

## 5. Major energy and the paired estimate

The interval transform in (5) satisfies $|\widehat{\mathbf1_{\mathcal J}}(\beta)|\ll\min(X,|\beta|^{-1})$ and its real fourth integral is $O_\rho(X^3)$. Summing the fourth powers of the main terms over majors costs only $\sum_q\mu(q)^4/\varphi(q)^3<\infty$, using the convergent Euler product. The error in (5) is negligible in fourth mean by the arc measure bound and arbitrary $M$ following the fixed $C$. Thus (6) gives
$\int_{\mathfrak M}|\mathcal B|^4\ll_\rho X^3\ell^{-2/5}$.
Together with (4) and Parseval for $\mathcal B^2$, this proves (1), including the individually negligible error in (2).

For the asserted pointwise **major portion** of the factored convolution, unfold $\mathcal B^2e(-N\alpha)$ with (5) and group the equal-width arcs by denominator. The numerator sum of $e(-Na_0/q)$ is exactly $c_q(N)$ before any absolute values. Since
$\int_{\mathbb R}|\widehat{\mathbf1_{\mathcal J}}(\beta)|^2\,d\beta\ll X$ and

$$
       \sum_q\frac{\mu(q)^2|c_q(N)|}{\varphi(q)^2}
               \ll \mathfrak S(N)
              \qquad(2\mid N),
$$

the major integral is $O_\rho(\mathfrak S(N)X\ell^{-1/5})$. For the displayed arithmetic bound the local factors are $1+1/(p-1)$ for $p\mid N$ and $1+1/(p-1)^2$ otherwise; the latter converge away from two and the former are bounded by the ordinary binary singular factors up to an absolute factor. Summing the uniform squared-polynomial substitution error in (5) is negligible since the measure is $O(P^2/X)$ and $M$ is arbitrary. The minor integral at a fixed $N$ is not claimed small here; under restoration of both parities the actual full paired cancellation obtained is the mean-square statement (1).
