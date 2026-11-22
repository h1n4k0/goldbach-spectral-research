# Polynomial rational denominators and wings in the signed seam

Retain $P_E$, $D$ and the exact hard cuts of [the signed-seam major-arc estimate](weak-s-type-ii-signed-seam-major-arcs.md), including every even $N$, $d\ge\sqrt N$, $t\ge N^{.49999}$, $N/2\le y\le9N/16$, and any selector $E(u,v)$ independent of $d,k$ with $|E|\le1$. Thus the true no-exchange remainder and its fixed proportional prime–prime restriction are included, with no replacement of $b_{\rm II}(v)$ or the squarefree and unit gates.

**Theorem.** Fix $\kappa>0$, $\lambda\ge0$ with $2\kappa+3\lambda<1/2-10^{-5}$. Put $Q=N^\kappa$, $W=N^\lambda\exp(\Phi(L))$, and $\Phi(L)=L^{3/5}(\log L)^{-1/5}$, $L=\log N$. Define

$$
 \mathfrak U=\bigcup_{\substack{q\le Q\\(a,q)=1}}
       \{a/q+\beta\bmod 1: |\beta|\le W/N\}.
$$

Then

$$
            \int_{\mathfrak U}|P_E(\alpha)D(\alpha)|\,d\alpha
                  \ll_{\kappa,\lambda} N \exp(-c\Phi(L))
$$

for some effective $c>0$. This is unconditional and uniform in the stated masks and cuts. For example it covers all reduced $q\le N^{.24}$ and $|\beta|\le N^{-.995}$. Both the denominators and the arc widths may now be polynomially larger than in the earlier result. It does not estimate the signed coefficient outside this region.

The proof does not upper-bound the full minor integral by separate global norms. It estimates the actual complementary polynomial in this rational region, using the averaged geometric remainder and the denominator decay of its signed main term. A simultaneous absolute oscillatory bound makes the signed main term square-integrable on the polynomially wide wings even when the $k>t$ boundary is active.

## 1. Averaging the geometric remainder and retaining the exact lengths

With the notation of §1 of the [major-arc proof](weak-s-type-ii-signed-seam-major-arcs.md#1-the-exact-additive-squarefree-density), for a fixed squarefree $d$ with $(d,N)=1$ expand $\mu^2(k)$ via $k=c^2\ell$ and the remaining unit mask via $\ell=h j$, $h\mid dN$. On a $d$ dyad $D_0\le d<2D_0$ put $K_0=N/D_0$, so that the original $k$ support is in $(0,K_0)$. Compare each square-base and unit-divisor term with its exact periodic mean, including all $c\ge1$ in the mean sum. In the $j$ variable the rational phase is $e(aM j/q)$, $M=d c^2h$, of reduced denominator $q'=q/(M,q)$.

First suppose $c^2h\le K_0$. On any hard prefix interval $J$ in the $j$ variable, there are $J_\#\ll K_0/(c^2h)$ integers to sum. If $q'>1$, the periodic mean is zero. Drop all full periods, leaving at most $\min(q',J_\#)$ distinct consecutive residues. Reduction of the unit $a$ modulo $q'$ has multiplicity $\varphi(q)/\varphi(q')\le q/q'$, and $M/(M,q)$ is a unit modulo $q'$. Additive Parseval over all residues modulo $q'$ therefore bounds the squared numerator norm by

$$
 \sum_{a\bmod q}^{*}\left|\sum_{j\in J}e(aMj/q)\right|^2
      \le (q/q')\,q'\min(q',J_\#)
      \ll q K_0/(c^2h).
$$

If $q'=1$, the phase is constant. The sum minus its real interval-length mean has magnitude at most two, so its norm is $O(\sqrt q)$, also within $O(\sqrt{qK_0}/(c\sqrt h))$. This bound holds for every hard prefix. Vector-valued Abel summation against $e(\beta d c^2hj)$ costs a factor $1+N|\beta|$ because $dk<N/2$ on the corresponding interval. Thus summing over $c^2h\le K_0$ for fixed $h$ costs $O((1+N|\beta|)\sqrt{qK_0/h}\,L)$ by the harmonic $c$ sum.

If $c^2h>K_0$, there is no positive integer $j$ in the support. In that case the only discrepancy is the continuous mean, if $q'=1$, of numerator norm at most $\sqrt q K_0/(c^2h)$. For fixed $h\le K_0$ the $c$-tail of $K_0/(c^2h)$ is $O(\sqrt{K_0/h})$; when $h>K_0$, summing all $c$ costs $O(K_0/h)\le O(\sqrt{K_0/h})$. This handles the infinite square-base extension in the main term without losing the short-length saving, and all other restrictions on $c$ only reduce these bounds.

Apply Minkowski over all $h\mid dN$ and sum over $d$ with its actual $\mu(d)$. The sum of $h^{-1/2}$ is at most $\tau(dN)$, and $D_0\sqrt{K_0}=\sqrt{ND_0}\ll N^{.750005}$ since $d<N^{.50001}/2$. Summing the $O(L)$ dyads, for every fixed $\epsilon>0$ we obtain the exact decomposition and averaged error

$$
 \begin{aligned}
 D(a/q+\beta)&=S_q(\beta)+R_{q,a}(\beta),\\
 S_q(\beta)&=\sum_{\substack{d\in I_d,\ d\ge\sqrt N\\(d,N)=1}}
             \mu(d) A_q(d;N)W_\beta(d),\\
 \left(\sum_{a\bmod q}^{*}|R_{q,a}(\beta)|^2\right)^{1/2}
          &\ll_\epsilon N^{.750005+\epsilon} \sqrt q(1+N|\beta|).
 \end{aligned}
$$

Here $A_q$ and $W_\beta$ are the same exact local density and clipped integral as in the cited proof; in particular $W_\beta(d)=d^{-1}\int_{\max(N-y,td)}^{N/2}e(\beta z)\,dz$ with the convention zero past the terminal point. Exactly at a sharp endpoint the discrepancy is included in the geometric remainder. This argument did not use a probability model for the rational numerators.

## 2. Extra denominator decay of the signed main term

For $g=(d,\operatorname{rad}q)$ on the support, recall

$$
 A_q(d;N)=C_{q,N,g}\prod_{\substack{p\mid d\\p\nmid qN}}\frac{p}{p+1}.
$$

Only $g$ coprime to $N$ occur. In addition to the bound $|C_{q,N,g}|\le1$, the local factors in the exact density give the stronger estimate

$$
 \sum_{\substack{g\mid\operatorname{rad}q\\(g,N)=1}}
                \frac{|C_{q,N,g}|}{g}\ \le\
       \frac{2^{\omega(q)}}q .
$$

In fact, at $p^e\Vert q$, for $p\nmid N$ sum the two possibilities $p\nmid g$ and $p\mid g$ with the latter weighted by $1/p$. For $e=1$ this yields $p^{-2}+p^{-1}(1-1/p)=1/p$. For $e=2$ it gives $p^{-2}+p^{-1}p^{-1}=2/p^2$. For $e\ge3$ it is zero. At $p\mid N$ only $p\nmid g$ is allowed and the local bound is $1/p$ for $e=1$, zero otherwise. The other local factors have modulus at most one. This calculation depends on summing the densities only after grouping the true signs, not on independence of $A_q$ and $\mu(d)$.

For fixed $g$ the actual $d=gn$ sum retains $(n,qN)=1$, with weight the signed multiplicative function $\mu(n)\prod_{p\mid n}p/(p+1)$. The effective masked weighted Mertens argument of [§2 of the major-arc proof](weak-s-type-ii-signed-seam-major-arcs.md#2-effective-cancellation-in-the-d-main-term) is unchanged with the minimum summatory scale $Y\ge N^{.24}$: its convolution split $h\le\sqrt Y$ has $\log(Y/h)\ge .12L$, and the $3/4$ moment handles the rest. In the present application $D_0/g\gg N^{1/2-\kappa}\ge N^{.24}$ for large $N$, and the mask satisfies $qN\le N^3$. For each dyad the supremum and variation of $W_\beta$ are $O(N/D_0)$, independent of $\beta$ (the lower endpoint is monotonically clipped). Consequently Abel summation on each dyad costs only this factor; summing all dyads and using the displayed denominator decay proves, with an absolute effective $c_1>0$,

$$
             |S_q(\beta)|\ll N e^{-c_1\Phi(L)}
                                      \frac{2^{\omega(q)}}q.
$$

No individual Dirichlet-character estimate, prime-distribution theorem, or GRH is used.

A second bound complements the signed one. For each $d\asymp D_0$, even when the lower endpoint is clipped by $td$, direct integration of the exponential gives

$$
  |W_\beta(d)|\ll \frac{N}{D_0(1+N|\beta|)} .
$$

For each $g\mid\operatorname{rad}q$, the total absolute density on the dyad with that $g$ is at most $O(D_0|C_{q,N,g}|/g)$: the multiplicative factor outside $qN$ is at most one, and the number of multiples of $g$ is $O(D_0/g)$ since $g\le q\ll D_0$. Sum over $g$ using the exact local denominator bound, then over dyads. Thus the two estimates together give

$$
 |S_q(\beta)|\ll NL\,\frac{2^{\omega(q)}}q
           \min\!\bigl(e^{-c_1\Phi(L)},(1+N|\beta|)^{-1}\bigr).
$$

The absolute estimate is used only at large $|\beta|$, not as a replacement for the signed main cancellation. Taking this minimum is what permits polynomial arc widths without any estimate for a twisted weighted Möbius sum at the moving endpoint.

## 3. Integrate the rational arcs

Two different centers of denominators at most $Q$ are separated by at least $1/Q^2$ on the circle, so the arcs are disjoint for large $N$ since $2\kappa+\lambda<1$. Write $S$ for $S_q(\beta)$ on each arc. For $0<\delta\le1$, the integral of $\min(\delta^2,(1+|x|)^{-2})$ over all real $x$ is $O(\delta)$, by splitting at $|x|=\delta^{-1}$. Apply this with $x=N\beta$, $\delta=e^{-c_1\Phi(L)}$. Then the squared main norm is

$$
 \int_{\mathfrak U}|S|^2\,d\alpha
   \ll NL^2 e^{-c_1\Phi(L)}
                 \sum_{q\le Q}\frac{4^{\omega(q)}\varphi(q)}{q^2}
   \ll NL^6 e^{-c_1\Phi(L)} .
$$

The last estimate follows from $4^{\omega(q)}\le \tau_4(q)$, where $\tau_4$ is the fourfold divisor function, and $\sum_{q\le Q}\tau_4(q)/q\ll(\log(2Q))^4$ by expansion. Write $R$ for the error on each arc, likewise patched together on the union. From §1,

$$
 \int_{\mathfrak U}|R|^2 d\alpha
    \ll_\epsilon N^{.50001+2\epsilon}Q^2(1+W)^3 .
$$

Indeed the square is summed over numerators *before* estimating the arc integral, leaving $\sum_{q\le Q}q$; also $\int_{-W/N}^{W/N}(1+N|\beta|)^2d\beta\ll (1+W)^3/N$. The exponent $.50001+2\kappa+3\lambda$ is strictly below one, so a sufficiently small fixed $\epsilon>0$ gives a power saving (the subpower factor in $W$ is harmless). It follows that $\|D\|_{L^2(\mathfrak U)}^2\ll_{\kappa,\lambda} N e^{-c_2\Phi(L)}$.

Finally each additive coefficient of $P_E$ has absolute value at most $L\tau(n)$ at product $n$. Hence $\|P_E\|_2^2\ll NL^5$ by Parseval, $\tau^2\le\tau_4$, and the ordinary divisor first moment for $\tau_4$. Cauchy using the **localized** norm of $D$ proves the theorem. In particular the original signed Type II coefficient is now the signed integral outside $\mathfrak U$ plus $O_{\kappa,\lambda}(N e^{-c\Phi(L)})$. The complement still contains general minor arcs, not just reduced rationals of large denominator; in particular no bound is claimed for points near small denominators but outside these narrow cores.
