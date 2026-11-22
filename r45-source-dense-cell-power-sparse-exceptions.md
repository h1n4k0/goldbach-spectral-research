# Power-sparse exceptions for the same dense four-prime rectangle

Work with the exact rectangle and notation of the [signed major evaluation](r43-source-dense-cell-positive-major-obstruction.md) and [density-one count](r44-source-dense-cell-density-one-signed.md): fixed $0<\rho<1/2$ and $0<\kappa\le1/2000$, even $N$, $N^{.38}\le q\le N^{.42}$, $N^{.08}\le s\le N^{.12}$, genuine prime giants $p,v$, original unit masks modulo $N$, and marker $(\log q)(\log s)$. Both orders of the summands $qp,sv$ are retained with the same moving hard $I\subseteq I_0(N)=[\rho N,(1-\rho)N]$ in the first position and the fixed $I_0(N)$ in the second. Let $C_I(N)$ denote the actual full-torus count and $\mathcal B_I(N)$ the exact R43 real comparator including the unit masks and $\lambda(q)\lambda(s)=(q-1)(s-1)/[(q-2)(s-2)]$.

**Theorem.** Assume global Dirichlet GRH. For $X$ sufficiently large there are at most $O_{\rho,\kappa}(X^{3/4})$ exceptional even $N\in[X,2X]$, simultaneously for all moving hard $I$, such that outside them

$$
 C_I(N)=\mathfrak S(N)\mathcal B_I(N)
               +O_{\rho,\kappa}\!\big(\mathfrak S(N)N^{99/100}\big).
                                                                    \tag{1}
$$

For the [exact Dirichlet complement](r35-source-square-root-dirichlet-arcs.md) $\mathfrak m(N)$, (1) and R43 give the genuine signed estimate

$$
 \left|\int_{\mathfrak m(N)}\mathcal P_I(\alpha)e(-N\alpha)\,d\alpha\right|
       \ll_{\rho,\kappa}\mathfrak S(N)N(\log N)^{-13}                 \tag{2}
$$

with the same power-sparse exceptional set. In particular, in any progression of admissible even integers of spacing $d\le X^{1/4-\epsilon}$, at most an $O_{\rho,\kappa}(X^{-\epsilon})$ proportion of the targets in $[X,2X]$ can be exceptional. This is not a claim for every term of a progression or for specially chosen thin sequences.

## 1. Power grids and a frozen minor estimate

Write $L=\log X$, $P=X^{2/5}$ and $e(t)=e^{2\pi it}$. As in R44, use frozen physical grids bracketing all four endpoints of the two ordered summand windows, now with step $O_\rho(X^{1-1/80})$. For each of the four moving cofactor endpoints $N^u$ use a separate grid bracketing its range for $N\in[X,2X]$, of step $O(X^{u-1/80})$. Every endpoint has $O_\rho(X^{1/80})$ choices, yielding $O_\rho(X^{1/10})$ configurations $(J,K,E,F)$, including either assignment of the two cofactor types to the first window. The physical grid lies in $[\rho X/2,2X]$ and contains all actual endpoints with room for an extra step to handle included or excluded atoms. Empty inner intervals are permitted.

The frozen actual prime transforms have no $N$-dependent unit masks:

$$
 A_{J,E}(\alpha)=\sum_{q\in E,\ q\ {\rm prime}}(\log q)
                   \sum_{p\ {\rm prime},\ qp\in J}e(\alpha qp).
$$

The ambient envelopes of the two cofactor sets, denoted $E_*,F_*$, have the same power endpoints $.38,.42$ and $.08,.12$ respectively, up to fixed multiplicative constants. For all frozen configurations the four constituent prime ranges are pairwise disjoint, since the giants are in power bands $[.58,.62]+O_\rho(1/L)$ and $[.88,.92]+O_\rho(1/L)$. Thus at the actual coefficient $qp+sv=N$ each prime is automatically a unit modulo $N$. True hard coefficients can be bracketed by the corresponding positive frozen coefficients, with no arithmetic error.

Use auxiliary disjoint reduced arcs $\mathfrak D_X^*$ with $r\le P$ and $|\beta|\le B_r=P/(rX)$; disjointness follows from $2P^2/X<1$. They are not the R35 arc family. On their complement Dirichlet approximation supplies $P<r\le\lceil X/P\rceil$ with $|\alpha-a/r|\le r^{-2}$; taking this ceiling ensures denominators at most $P$ would lie in $\mathfrak D_X^*$. For a cofactor dyad $U\le q<2U$ and $V=X/U$, the hard-intersection bilinear estimate of R44, obtained by Cauchy–Schwarz in the giant and spacing the $\alpha h$ in blocks of length $\lfloor r/2\rfloor$, gives

$$
 |A_{J,E}^{(U)}(\alpha)|^2
     \ll_\rho X^2L^3(U^{-1}+V^{-1}+r^{-1}+r/X).
$$

Always take the supremum on the larger-cofactor leg (the $E$ type), whatever its window position. Its dyads have $U\gg X^{.38}$, $V\gg X^{.58}$, so summing by the triangle inequality gives squared supremum $O_\rho(X^{2-.38}L^5)$. The other leg has full-circle squared energy $O_\rho(XL^2)$ by the unique small/large prime factorization. Hence Bessel bounds the sum of squared signed auxiliary minor coefficients in one frozen configuration by $O_\rho(X^{3-.38}L^7)$. At threshold $X^{.99}$ the number of bad integers is $O_\rho(X^{.64}L^7)$ per configuration. The simultaneous exceptional set for the entire grid has size $O_\rho(X^{.74}L^7)=O_\rho(X^{3/4})$. No positivity is used in the minor-coefficient estimate.

## 2. GRH prime approximation on the power-sized arcs

With $r_q=r/(r,q)$ the exact uncentered model on an arc is

$$
 M_{J,E,r}(\beta)=\sum_{q\in E,\ q\ {\rm prime}}
      \frac{\mu(r_q)}{\varphi(r_q)}
      \int_J\frac{\log q}{q\log(t/q)}\,e(\beta t)\,dt.
$$

We verify a squared error $O_\rho(X^{.96}L^{O(1)})$ on $\mathfrak D_X^*$ uniformly in the frozen bins, enough to replace each signed prime product at cost $O_\rho(X^{.98}L^{O(1)})$. This is the genuine prime-leg argument of R35 with an enlarged Mellin floor.

Smooth the hard $t/X$ edge at width $X^{-1/25}$ and denote its bump by $w_J$. For each cofactor dyad $U,V=X/U$, choose a fixed smooth cutoff of $p/V$ equal to one on the proportional range occurring under $w_J$. The real log-coordinate Fourier transform

$$
 \widehat A_\beta(\tau)=\int w_J(e^x)e(\beta Xe^x)e^{-i\tau x}\,dx
$$

separates the two twists $(q/U)^{i\tau}$ and $(p/V)^{i\tau}$. Set $T_r=100(P/r+X^{2/25})$. For $|\beta|\le B_r$ and $|\tau|\ge T_r$ the phase derivative is $\gg|\tau|$ on the support. Repeated integration by parts gives $|\widehat A_\beta(\tau)|\ll_{\rho,j}X^{j/25}|\tau|^{-j}$. Since $T_r\ge X^{2/25}$, trivial polynomial bounds for all separated sums and integrals make this tail negligible to any fixed power, uniformly on the arcs. For the low-height separated error $D(\tau)$, the R35 real Plancherel bound is

$$
 \int_{|\beta|\le B_r}\left|\int_{-T_r}^{T_r}\widehat A_\beta(\tau)D(\tau)\,d\tau\right|^2d\beta
       \ll_\rho X^{-1}\int_{-T_r}^{T_r}|D(\tau)|^2d\tau .
$$

It follows by integrating in real $\beta$ over the full line (writing $\widehat A_\beta$ as the transform in $e^x$), then using Fourier Plancherel in the log coordinate; the physical support is comparable to one.

For fixed $|\tau|\le T_r\le X^3$, global Dirichlet GRH gives the fixed smooth, log-twisted prime character discrepancy $O_\rho(\sqrt V L^2)$ of R35 §2 after extracting the principal integral with $1/\log t$. All occurring giant primes exceed $r$. For $q\nmid r$, character expansion of the additive modulation and reduced-numerator orthogonality bound the squared separated error summed over numerators by

$$
 \ll_\rho r V L^4\, U(1+U/r)L^2
       \ll_\rho X(r+U)L^8.
$$

This uses the complete Gauss coefficient bound $\sqrt r$ and the cofactor character mean square $O(U(1+U/r)L^2)$, from counting pairs in a residue class, with the twists of absolute value one. For $q\mid r$, work at $r/q$ and lift the reduced numerators; additive and character Parseval give $O_\rho(r V L^6)$ for each such $q$, with the factor $r/(r/q)$ bounding the lift multiplicity, including $q\mid r/q$. There are $O(1)$ such primes at a denominator since $q\gg X^{.08}$ and $r\le X^{.4}$. They are absorbed in the same displayed bound. The principal term is exactly $\mu(r_q)/\varphi(r_q)$ for each $q$. There is no exclusion on $q\mid N$ in the frozen transform or this estimate.

After real Plancherel and numerator summation, the low-height squared discrepancy per dyad is bounded by

$$
 L^{O(1)}\sum_{r\le P}(P/r+X^{2/25})(r+U)
 \ll_\rho L^{O(1)}
        \big(P^2+PU L+X^{2/25}(P^2+PU)\big)
 \ll_\rho X^{.90}L^{O(1)}
$$

because $U\ll X^{.42}$. The dyadic aggregation adds only logarithms. The original hard edges cost $O_\rho(X^{.96}L^2)$ in the squared torus norm by counting integer Fourier indices in the edge intervals. They cost the same in squared real model norm summed over arcs: use $|G_E(t;r)|\ll_\rho1/\varphi(r)$ for its physical density as in R35, and $\sum_{r\le P}1/\varphi(r)\ll L^2$. This proves the claimed hard squared approximation. Cauchy–Schwarz with true squared Fourier norms $O_\rho(XL^2)$ gives the signed product error $O_\rho(X^{.98}L^{O(1)})=o(X^{.99})$ uniformly in all configurations and even $N$.

## 3. The correct local zero for frozen cofactors dividing the target

Summing the target phase over reduced numerators gives

$$
 H_{q,s,N}(r)=c_r(N)\,
        \frac{\mu(r_q)\mu(r_s)}{\varphi(r_q)\varphi(r_s)}
$$

for each frozen cofactor pair. This coefficient is supported on squarefree $r$: for any prime square in $r$ at least one of the distinct $q,s$ legs retains that square. Its complete signed Euler product is

$$
 \sum_{r\ge1}H_{q,s,N}(r)
 =\mathfrak S(N)\lambda(q)\lambda(s)\mathbf1_{(qs,N)=1}.          \tag{3}
$$

Indeed the ordinary signed factor stays unchanged except at $q,s$; at $\ell=q$ the new factor is $1-c_q(N)/(q-1)$, equal to zero if $q\mid N$, and otherwise has ratio $\lambda(q)$ to the original factor. Likewise for $s$. In particular the frozen model exactly reinserts the target unit exclusions in the cofactor comparator; they must not be imposed on the initially fixed Fourier polynomials.

To justify real and denominator completion uniformly outside a small common exceptional set, put $w_q=(\log q)/(qL)$, and define

$$
 Z_X(N)=\sum_{\substack{q\in E_*,\,s\in F_*\\q,s\ {\rm prime}}}
   w_q w_s\sum_{r\ge1}\min(1,r/P)|H_{q,s,N}(r)|.
$$

This dominates all frozen subselections. For fixed $r$, $\sum_{X\le n\le2X}|c_r(n)|\le 2X\tau(r)$ by the divisor identity. With $\sigma=3/4$, the associated Euler series

$$
 \sum_{r\ge1}\frac{\mu^2(r)\tau(r)\,r^\sigma}
                  {\varphi(r_q)\varphi(r_s)}\ll 1
$$

is uniform in the distinct large cofactors: the ordinary local terms are $1+2\ell^\sigma/(\ell-1)^2$, and each of the two special terms $1+2q^\sigma/(q-1)$ or $1+2s^\sigma/(s-1)$ is bounded. Since $\min(1,r/P)\le(r/P)^\sigma$ and the ambient sums of $w$ are $O(1)$, one has $X^{-1}\sum_{n\in[X,2X]}Z_X(n)\ll P^{-3/4}=X^{-.30}$. Thus $Z_X(N)>X^{-.01}$ fails at most $O(X^{.71})$ integers after Markov.

The real hard profile for fixed $q$ has size $O_\rho(w_q\min(X,|\beta|^{-1}))$ by integration by parts. Filling $|\beta|>B_r$ for $r\le P$ therefore costs $O_\rho(Xw_qw_s\,r/P)$ per pair times $|H|$, and filling $r>P$ costs $O_\rho(Xw_qw_s)$ times its absolute tail. This gives total completion error $O_\rho(XZ_X(N))$ for every selected box, both orders. The whole real integral is exact convolution at $N$ of the two hard physical profiles. By (3) its model is precisely the signed R43 density with the frozen cofactor and physical windows, including $\lambda(q)\lambda(s)$ and the original cofactor exclusions. There is no use of averaging over different cutoff definitions here.

## 4. Power bracketing and scope

The frozen signed full count therefore has the stated model with error $O_\rho(X^{.99})$ simultaneously on all configurations for all but $O_\rho(X^{3/4})$ even $N$. To restore exact hard endpoints, bracket by inner and outer boxes. The real model profiles are bounded uniformly because $\sum_q(\log q)/(qL)\ll1$ in the ambient ranges, and the factors $\lambda(q)$ are bounded. Varying a physical endpoint by one grid step costs $O_\rho(X^{1-1/80})$ in the convolution. Moving a cofactor endpoint of size $X^u$ by one step changes the corresponding profile by $O_\rho(X^{-1/80}+X^{-u})$, directly from counting integers in the edge and bounding their weights by $O_\rho(X^{-u})$. These estimates hold with any subset of cofactor units, hence also with the exact masks. Multiply by $\mathfrak S(N)$; the bracketing error is $o(\mathfrak S(N)X^{.99})$. The positive exact counts between the frozen bounds then give (1) for all original $I$, with no smoothing of the final coefficient.

To obtain (2), subtract the genuine signed major evaluation of R43 on the exact R35 arcs, not the auxiliary $\mathfrak D_X^*$ used for the proof of (1). The power error is smaller than $N(\log N)^{-13}$. An admissible progression of even integers of spacing $d\le X^{1/4-\epsilon}$ has $\gg X/d$ targets in $[X,2X]$; the absolute exceptional count gives the claimed relative proportion. Also the [unconditional two-form sieve upper bound](r41-source-unmasked-separated-cofactor-cells.md) $C_I(N)\ll_{\rho,\kappa}\mathfrak S(N)N$ and the same model bound imply that the average squared supremum of $(C_I(N)-\mathfrak S(N)\mathcal B_I(N))/(\mathfrak S(N)N)$ over even $N\in[X,2X]$ is $O_{\rho,\kappa}(X^{-1/50})$. None of these estimates supplies a pointwise signed bound for the remaining exceptional moduli or a bound outside the exact four-prime rectangle.
