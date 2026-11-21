# Removing the upper transition slab in the central L¹ criterion

**Scope.** An unconditional estimate for the original signed fixed-$N$ rectangles, above the square root by a fixed logarithmic power. This drops the GRH assumption of the [earlier supercritical calculation](spectral-critical-level-diagonal.md#3-the-genuine-signed-discrepancy-is-small-above-this-transition) and applies to the [single-profile criterion](spectral-signed-rectangle-l1-no-jump.md). The estimate is pointwise in the even modulus and removes an upper range of the auxiliary cutoff. The remaining lower range, including the first nontrivial character component at modulus three when three does not divide the even modulus, is still unestimated here. This does not prove a Goldbach lower bound on its own or establish Hypothesis S.

Let $N$ be even, $L=\log N$, $a=1/2,b=9/16$, and use the actual central unit $B^+(t,y)$ and $M_1(t)=\int_a^b |B^+(t,Nx)|\,dx$ from the [smooth bridge](spectral-signed-rectangle-smooth-bridge.md) and its addendum. For every fixed $A\ge1$ and $0<\epsilon<1/2$, put $J=2A+20$ and $C_A=A+3J+6$. Then
$$
 \sup_{aN\le y\le bN}|B^+(t,y)|\ll_{A,\epsilon}NL^{-A}
 \qquad\left(\sqrt N\,L^{C_A}\le t\le N^{1-\epsilon}\right).
 \tag{1}
$$
This is for **every fixed** even $N$ and both real endpoints, not for almost all $N$. The exponent $C_A$ is only a sufficient one.

## 1. Keep the exact strict complement and use untwisted maximal BV

Write $m=N-n$. Since $m>1$ on the central interval and $(m,N)=1$ at the unit points,
$$
 \mu(m)\sum_{\substack{q\mid m\\q\le t}}\mu(q)
  =-\mu^2(m)\sum_{\substack{d\mid m\\d<m/t}}\mu(d).
$$
For squarefree $m$ this uses the zero full Möbius sum and $d=m/q$ on the omitted tail $q>t$; for other $m$ both sides are zero. The progression part of $B^+(t,y)$ is therefore the **negative** of
$$
 \sum_{\substack{d\le N/(2t)\\(d,N)=1}}\mu(d)
    \sum_{\substack{aN<n\le y,\ n<N-td\\(n,N)=1,\ n\equiv N\bmod d}}
            \Lambda(n)\mu^2(N-n).
 \tag{2}
$$
Use $\mu^2(m)=\sum_{r^2\mid m}\mu(r)$, and cut that sum at $R=L^J$. The omitted terms are supported on $O(N/R)$ integers $m$: count all multiples of $r^2$ for $r>R$. At each such $m$ their absolute combined weight in (2) is at most $L\tau(m)^2$, including the $d$-choices. Cauchy and the fourth divisor moment therefore bound the raw error by $O(NL^{17/2}R^{-1/2})=O_A(NL^{-A})$.

For a retained pair $r,d$, only squarefree $r,d$ with $(rd,N)=1$ need be counted. Set $\ell=[r^2,d]$. The reduced residue is $N\bmod\ell$, and the interval is still the strict/weak intersection in (2), empty if necessary. For its Lebesgue length $\lambda_{t,y}(d)$, the unrestricted progression sum differs from $\lambda_{t,y}(d)/\varphi(\ell)$ by at most $2E^*(N,\ell)$, with
$$
 E^*(N,\ell)=\sup_{0\le z\le N}\max_{(c,\ell)=1}
       \left|\sum_{\substack{n\le z\\n\equiv c\bmod\ell}}\Lambda(n)
                       -z/\varphi(\ell)\right|.
$$
This also bounds differences involving a strict endpoint by taking a left limit. Imposing $(n,N)=1$ removes only powers of primes dividing $N$, of total weight $O(L^2)$ per pair. The sum of these errors over all $O(RN/t)$ pairs is $O_A(NL^{-A})$, since $t\ge\sqrt N L^{C_A}$.

For each $r$, on a fixed class of $g=(r,d)$ one has $\ell=r^2d/g$, injective in $d$. The total progression error is consequently at most
$$
 2\sum_{r\le R}\tau(r)\sum_{\ell\le R^2N/(2t)}E^*(N,\ell).
$$
Since $R^2N/(2t)\le\sqrt N L^{-(A+J+6)}$, the inner sum is
$O_A(NL^{-(A+J+3)})$ by maximal [Bombieri–Vinogradov, Montgomery–Vaughan Theorem 20.2](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=206). Apply the theorem at the upper cutoff $\sqrt N L^{-(A+J+6)}$ and use monotonicity if the actual upper cutoff is smaller. With $\sum_{r\le R}\tau(r)\ll R\log(2R)$, this proves the requisite inverse-log saving for (2)'s progression error.

## 2. The model also cancels, with no $\Lambda\mu$ estimate

Extend the model square divisors $r$ to infinity. Its absolute tail, after using $\lambda_{t,y}(d)\le N$, costs at most
$$
 \ll N\sum_{r>R}\frac{\tau(r)}{r^2}\sum_{e\le N}
                   \frac{\log(2r^2 e)}e
 \ll N L(L+\log(2R))\log(2R)/R .
$$
The first bound writes $d=(r,d)e$ for squarefree $d$, so that $\ell=r^2e$, and uses $1/\varphi(\ell)\ll\log(2\ell)/\ell$. Reversing the Lebesgue interval and $d$ sums gives the model for (2):
$$
 A_N\int_{aN}^{y}\!
       \sum_{\substack{d<(N-z)/t\\(d,N)=1}}\mu(d)g(d)\,dz,\qquad
 A_N=\prod_{p\nmid N}\left(1-\frac1{p(p-1)}\right),
 \quad g(p)=\frac{p-1}{p^2-p-1},
$$
with squarefree multiplicative $g$. Indeed a prime $p\mid d$ changes the local factor from $1-1/(p(p-1))$ to $1/(p-1)-1/(p(p-1))=1/p$, giving the stated ratio. The strict $d$ cutoff is exact and uniformly at least $(1-b)N^\epsilon$ in the given range of $t$.

Use the standard coprime zero-free-range Euler estimate, as detailed in the [structured-modulus calculation](spectral-maynard-structured-critical.md): for either $g(p)$ or $1/(p-1)$, the squarefree multiplicative signed sum up to any cutoff $Y\in[cN^\epsilon,N]$ is $O_{A,\epsilon,c}(L^{-A})$, also for a strict cutoff and after excluding the primes dividing $N$. Indeed factor off $1/\zeta(1+s)$; the correction has absolute coefficient weight on $\Re s=-1/4$ bounded by $\exp(O(L^{1/4}))$ from the finitely many primes dividing $N$ and the absolutely convergent good factors. Convolve with $\mu(j)/j$, split the correction index at $\sqrt Y$ and use the classical zero-free-region $O(\exp(-c'\sqrt{\log Y}))$ cancellation for the smaller indices and the weighted tail for the larger ones. Hence the model integral is $O_{A,\epsilon}(NL^{-A})$. The rectangle baseline is the true signed $\Lambda(n)\mu(N-n)$ central increment times $\sum_{q\le t,(q,N)=1}\mu(q)/\varphi(q)$. Request one extra logarithmic saving from the same Euler estimate and use the crude $NL$ bound for the increment. This proves (1).

## 3. The profile reduction and a literal low-end gap

Choose $A>4$ and the smooth bridge exponent $C>C_A+1$ large enough for its short bound. Then, with $T=\sqrt N L^{C_A}$ and $Q_0=N/\lfloor\sqrt N L^{-C}\rfloor$, one has $T<7Q_0/32<Q_0/2<N^{3/4}$ for sufficiently large $N$. Thus the **same** profile in the no-jump criterion satisfies
$$
 \mathcal L_N = \int_1^T M_1(t)\frac{dt}{t}
                      +O_A(NL^{1-A}).
$$
Apply (1) all the way through the smooth transition slab; its discounted weight has integral $O(L)$, as does any lower logarithmic interval. Hence it is enough to impose the original threshold on this shortened logarithmic integral only. This discards the entire smooth transition and the supercritical tail above the displayed logarithmic power, with a bound on the true arithmetic rather than a change of norm.

It does not discard the small auxiliary cutoffs. For example, if $3\nmid N$, on $3\le t<4$ only the $q=3$ summand survives: $q=1$ is identically zero and $2\mid N$. Writing $\chi_3$ for the nonprincipal character modulo 3, the factor $2\mathbf1_{n\equiv N\bmod3}-1$ equals $\chi_3(N)\chi_3(n)$ unless $3\mid n$. In this central interval the latter exception contributes only powers of 3, with total $O(L)$ weight. Thus for any fixed $W\in C_c^1((a,b))$, Stieltjes summation against $W$ gives
$$
 \left|\sum_{\substack{aN<n\le bN\\(n,N)=1}}
      \Lambda(n)\mu(N-n)\chi_3(n)W(n/N)\right|
   \le 2\|W'\|_\infty M_1(3)+O_W(L).
$$
Here $M_1(3)\log(4/3)\le\int_1^T M_1(t)\,dt/t$. In particular the shortened profile's desired $o(N/(L^2\log L))$ would already give that saving in a literal fixed-$N$ signed $\Lambda\mu$ correlation at the first nontrivial modulus on $3\nmid N$. This illustration is not a lower bound or an assertion of impossibility; the missing cancellation is not supplied by (1).
