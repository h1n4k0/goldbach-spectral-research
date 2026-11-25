# The true critical prime shell with all units under only an imported real-zero gap

**Scope.** This replaces the global Dirichlet-GRH input in the [full-unit dual-determinant theorem](weak-s-type-ii-critical-prime-full-unit-dual-determinant-grh.md) by the weaker, separately [recorded external uniform real-zero gap](r88-spectral-external-zero-gap-implication.md). The arithmetic argument has this explicitly imported dependency; it does not give an independent proof of the gap, report a local formal rerun, or invoke RH or GRH. It also widens the genuine divisor range beyond every fixed power of $\log N$ while keeping the same critical shell. It is not a theorem for polynomial widening or Hypothesis S.

Assume **(UZG)**: there exist $c>0$ and $r_0\ge3$ such that every real zero $0<\beta<1$ of a primitive nonprincipal real Dirichlet $L$-function of conductor $r\ge r_0$ satisfies $(1-\beta)\log r\ge c$. The exact external statement, formal scope and separate external verification record are the ones in the dependency note. We use no hypothesis about zeros at height different from zero beyond the classical zero-free region.

Use the original genuine $P,D$, prime selectors, physical and cofactor cuts, rational points and hard arc endpoints of the full-unit theorem: $N$ even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, $\mathcal Q=[.8X,.9X]\cap\mathbb P$, $a=1,\ldots,q-1$ and $|\beta|\le1/(10N)$. In particular the actual $k$ has $k>t\ge N^{.49999}$ and the complementary coefficient imposes both $(dk,N)=1$ and squarefreeness on the physical interval $[N-y,N/2)$, $N/2\le y\le9N/16$. Fix $C>0$ and $F\ge1$ and permit any real hard divisor interval in

$$
                   X\le d\le X\Lambda,\qquad
                 \Lambda=\exp(C L_2^{\,F}).
$$

**Theorem (under imported UZG).** For every $\varepsilon>0$ and every sufficiently large even $N$, uniformly in all these actual gates,

$$
 \mathcal E_N(D)=\int_{-1/(10N)}^{1/(10N)}
        \sum_{q\in\mathcal Q}\sum_{a=1}^{q-1}|D(a/q+\beta)|^2\,d\beta
      \ll_{C,F,\varepsilon,{\rm UZG}} N L^{-1/2+\varepsilon}.
 \tag{1}
$$

The full signed shell, its separately centered numerator covariance, and the exact parity-preserving signed even-lattice residual with $M=\lceil XL^2\rceil$ are $O_{C,F,\varepsilon,{\rm UZG}}(NL^{-1/4+\varepsilon})$. There is no restriction on $\operatorname{rad}N$, no omitted reciprocal cost, and no exceptional family of even targets. If $F>1$, the stated divisor width is eventually larger than every fixed power of $\log N$, but still $N^{o(1)}$ times $X$.

## 1. Uniform additive Möbius cancellation from the real-zero gap only

The input available in place of Baker–Harman is the following stretched-exponential estimate: for an absolute-in-$x,\theta$ $c_1>0$ depending at most on the gap data,

$$
       \sup_{\theta\in\mathbb R}
             \left|\sum_{n\le x}\mu(n)e(n\theta)\right|
                    \ll x\exp(-c_1\sqrt{\log x}),\qquad x\ge3 .
 \tag{2}
$$

Here $e(t)=e^{2\pi i t}$. To prove it set $G=\log x$, $P_0=\exp(\kappa\sqrt G)$ and $Q_0=\lceil x/P_0\rceil$ for a fixed small $\kappa>0$ chosen below. The actual reduced Dirichlet approximant has $q\le Q_0$ and $|\theta-a/q|\le1/(qQ_0)\le P_0/(qx)$, which is also at most $q^{-2}$. When $q>P_0$, the [Basak–Robles–Zaharescu estimate, Theorem 1.4](https://arxiv.org/html/2312.17435v2) is

$$
  \left|\sum_{n\le x}\mu(n)e(n\theta)\right|
  \ll_\epsilon x^{4/5+\epsilon}
        +xq^{-1/2}(\log x)^3+\sqrt{xq}(\log x)^3 .
$$

Fix $\epsilon<1/10$ and use $q\le2x/P_0$; this gives (2) with any sufficiently small constant in terms of $\kappa$.

For clarity we check the reciprocal-$L$ major-arc bound at $q\le P_0$. Take height $T_*=e^{\sqrt G}$ and shift to $1-a_0/\sqrt G$ with a small absolute $a_0>0$. This is within the half-width classical zero-free regions for nonreal zeros when $\kappa\le1/2$. For a real exceptional candidate having conductor $r\le P_0$, (UZG) gives distance at least $c/(\kappa\sqrt G)$ from $1$ when $r\ge r_0$. The finitely many smaller primitive real nonprincipal characters have a fixed positive distance of real zeros from $1$ by $L(1,\chi)\ne0$, analyticity and finiteness. Thus for $\kappa$ sufficiently small no zero lies to the right of $1-4a_0/\sqrt G$ in the real region. The classical bounds for $1/L$ on the rectangle now hold with size $G^{O(1)}$. Precisely, use [Montgomery–Vaughan, Theorems 11.3–11.4](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF) (the near-real-zero bound, if needed, has distance $\gg G^{-1/2}$ on the contour), and [Theorems 6.6–6.7](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287) for the principal character. All choices are uniform as $\kappa$ decreases, once the inequality $c/\kappa>4a_0$ has been arranged. As in the [good-dyad reciprocal Perron argument](r85-spectral-unconditional-planted-ap-good-dyads.md#1-good-dyads-are-unconditional), an imprimitive character introduces only finite Euler factors, and the pole of $\zeta$ gives no pole for its reciprocal.

Account for nonunit residues exactly. For $b\bmod q$ put $d=(b,q)$, $b=d b'$, $q=dq'$. On $n\equiv b\bmod q$, write $n=d m$ with $m\equiv b'\bmod q'$ a unit residue. If $d$ is not squarefree the Möbius sum vanishes. Otherwise $\mu(dm)=\mu(d)\mu(m)\mathbf1_{(m,d)=1}$. After character orthogonality the reciprocal Dirichlet series is exactly

$$
   \frac1{L(s,\chi)}
        \prod_{\substack{p\mid d\\p\nmid q'}}(1-\chi(p)p^{-s})^{-1}
                \qquad(\chi\bmod q').
$$

The extra product on the rectangle is $G^{O(1)}$, because $p^{1-\Re s}\ll1$ there for $p\mid q$ and $\sum_{p\mid q}1/p\ll\log\log(3q)$, and each factor is uniformly bounded away from a pole. This proof includes $q'=1$ and $b=0$. The half-integer Perron endpoint at $u\asymp y/d$ preserves the hard prefix; for $x^{1/2}\le y\le x$ the new $u$ lies between $x^{1/3}$ and $2x$. Truncate on $1+1/\log u$ at $T_*$, shift in the zero-free rectangle, and sum the absolute error at distances from its half-integer endpoint as in that argument. The vertical cost is $u^{1-a_0/\sqrt G}G^{O(1)}$, and the truncation and two horizontal sides are $uG^{O(1)}/T_*$. Thus for each $b$ the prefix through $y$ is $O((y/d)e^{-c_2\sqrt G})$ with fixed $c_2>0$, which can be kept fixed for all further decreases of $\kappa$. The coefficient bound needed for the truncation is at most one, also after the extra $d$-unit mask.

Sum over the $q$ residues to bound the prefix with additive frequency $a/q$ by $O(xq e^{-c_2\sqrt G})$, uniformly over all $0\le y\le x$ (shorter $y<x^{1/2}$ is trivial). Abel summation of the residual frequency costs $1+x|\theta-a/q|\le1+P_0/q$, and hence the full bound is $O(x P_0 e^{-c_2\sqrt G})$ on these major arcs. Choose $\kappa<c_2/2$ in addition to the earlier restrictions. This proves (2) without assuming cancellation of any possible classical exceptional term.

## 2. The genuine no-condition transfers remain valid at this width

Use the actual divisor dyads $A_0=\lambda X\le d<2A_0$ with $1\le\lambda\ll\Lambda$ and $K=X/\lambda$, and leave the long $d$ cut sharp on each dyad. There are $O_{C,F}(1+L_2^F)$ dyads. The cofactor is still $k\asymp K$ on the actual physical interval, with $\log K\asymp L$. We record how the unconditional transfers of the [log-wide boundary estimates](weak-s-type-ii-critical-prime-logarithmic-range-and-reciprocal-unit-tail.md#2-uniform-exact-transfers-on-one-divisor-dyad) and the full-unit theorem behave, since the earlier statements only needed logarithmic $\lambda$.

For each squarefree forced-square label $\ell_0$, the same signed continuous lcm bound and actual small-gcd count give on one dyad

$$
 \sum_{\ell_0^{\,2}\mid m}|F_m|^2
 \ll C_3^{\omega(\ell_0)} N\ell_0^{-2}
                           (1+\log(2\lambda\ell_0)).
 \tag{3}
$$

Here $F_m$ is the signed raw auxiliary on the true dyad and cofactor gates. Use the large-gcd threshold $\lceil\lambda^2\ell_0^2\rceil$ to make its floor error $O(N/\ell_0^2)$. At small gcd $g$, writing the two long divisors as $g u,g v$ makes $u,v\asymp A_0/g$ and the shared quotient $m/[gu,gv]\ll g/\lambda^2$. The required prime-by-prime allocations of each $p^2\mid m$ use total modulus $\ell_0^2$ across these variables, exactly as there, and positive multiples counts cost $O(C_3^{\omega(\ell_0)}N/(g\ell_0^2))$ (an interval below one is empty). The continuous small-gcd subtraction uses the same harmonic lengths, while the whole signed lcm main is $O(C_3^{\omega(\ell_0)}N/\ell_0^2)$; neither step needs an upper bound of fixed log-power size on $\lambda$. These statements allow bounded-BV short weights by Minkowski. Squarefree truncation $l\le T_0=L^\eta$ then has squared cost $O_\rho(NT_0^{-1+\rho}(1+\log\Lambda)L_2)$ by grouping the two tail divisors by their lcm.

Smooth the physical gate and the short $k$ gate at relative width $\delta=L^{-B}$ as in the full-unit theorem, keeping the original unit mask and never smoothing $d$. On the true squarefree support, $\mu(d)=\mu(m)\mu(k)$ so the signed short-interval argument for the physical strips gives squared error $O(N\delta L_2+N^{3/4})$. In that argument the physical floor term is $K\sqrt{A_0}\le N^{3/4}$, with the same choice of small-gcd threshold since $\lambda=N^{o(1)}$. At a narrow $k$ endpoint the signed lcm bound uses only $\log K\asymp L$. Its small-gcd floor terms are $N\delta^2(1+\log(2G'))+\delta A_0G'+\lambda^2(G')^2$ with $G'=\lfloor L^{B+2}\rfloor$; the last two are $N^{1/2+o(1)}$ and $N^{o(1)}$, respectively, hence $O(N\delta)$ for fixed $B$. The large-gcd floor is $O(K^2/G')$. This gives the same smoothing error. Relative widths, sharp endpoints, and possible tiny empty intervals are treated by the same inside-supported smoothing. The combined ordinary squared cost in (2) of the full-unit theorem is thus valid here with a harmless extra fixed power of $L_2$.

Keep the exact long $(d,N)=1$ throughout. With the smoothed raw $F^{\rm sm}_{m,N}$ of the full-unit theorem, the forced first-divisibility estimate for squarefree $r\mid N$ is still

$$
  \sum_{r\mid m}|F^{\rm sm}_{m,N}|^2
              \ll \frac Nr\big(L_2^2+1+\log(2\lambda r)\big).
 \tag{4}
$$

Indeed its positive masked lcm norm uses an exact convolution with reciprocal $N$-smooth integers of total mass $N/\varphi(N)\ll L_2$. With both long divisors actual units the continuous main divides exactly by $r$. The large-gcd cutoff is $\lceil\lambda^2r\rceil$ as before, and the small-gcd multiple count is $O(N/(gr))$, since the common quotient must be an actual multiple of $r$. These are the proof of the full-unit estimate (4), with $\lambda=N^{o(1)}$, and $\log(2\lambda r)=O(L)$ for $r\mid N$. Therefore its short unit inclusion can still be truncated at $h\le H=\exp(C_0L_2^2)$ at ordinary squared cost $O_A(NL^{-A})$ with $C_0$ sufficiently large. Specifically use $|S_{T_0,N}|\le T_0$, group each omitted pair by lcm $r>H$, and apply Rankin at $1/L_2$ to $\sum_{r\mid\operatorname{rad}N,r>H}3^{\omega(r)}/r$ as there. No actual unit is omitted from the original theorem; these are only ordinary-norm transfers to its finite approximation. The true all-range ordinary square norm is $O(N)$ by the same signed short variable $k\le X/2$ on squarefree $m$, the actual moving short interval DIT bound and total $O(X^2)$ floors. The single-dyad truncated approximation likewise has ordinary squared norm $O(N)$ from these transfers. The genuine prime-side ordinary squared norm is unchanged.

## 3. Reinsert (2) in the exact joint determinant

In the finite approximation just obtained retain the exact splitting $s=(l,d)$ for $l\le T_0,(l,N)=1$, $d=su$, $k=l^2hv/s$, and the original short inclusion $h\le H,h\mid\operatorname{rad}N$. The normalized product Fourier transform and the character Poisson expansion are those of the [joint full-unit norm](weak-s-type-ii-critical-prime-full-unit-dual-determinant-grh.md#2-joint-poisson-norm-with-every-allowed-inclusion-label). At fixed real $\tau$, the common long coefficient is

$$
 a_u=\mu(u)\mathbf1_{su\in I_d\cap[A_0,2A_0)}
            \mathbf1_{(u,lN)=1}\,
                                e(\tau\log(su/A_0)),
 \qquad U=A_0/s.
$$

It is the same at every shell prime and all short inclusion labels. The smooth short Poisson mesh is $x_q/h$, where $x_q=Ks/(q l^2)$ and $x_0=Ks/(Xl^2)$. Put $\mathcal L=L_2^2+L_2^F$. One may truncate $|\tau|$ and $|j|$ at $\exp(C_1\mathcal L)$ and $\exp(C_2\mathcal L)$, with $C_2$ sufficiently larger (in particular larger than the constants from $H$ and $\Lambda$). The exact derivatives of the product cutoff give $\widehat G_\beta(\tau)\ll_r\delta^{1-r}|\tau|^{-r}$, while the short compact weight has $r$th derivative $L^1$ norm $\ll_r (1+\delta^{-1}+|\tau|)^r$. The mesh is at least $\exp(-C_4\mathcal L)$ uniformly, and periodization overlap is still bounded since the mesh is at most $5/4$. The elementary long norm through occupancy is $O(\lambda\sqrt{qX})$. Thus fixed large derivative orders as in the full-unit proof pay all the cut tails, even after multiplication by $H$ choices, the $\lambda$ occupancy bound and the $l,s$ tuple counts. Only $\exp(O_{C,F}(\mathcal L))$ labels are retained, all nonzero modulo every shell prime when required. There is no approximation to the original $\beta$ gate.

The exact congruence after the positive character expansion is $h j'u-h'j u'\equiv0\bmod q$. On its literal zero determinant use $(u u',N)=1$; after $g=(h,h')$, necessarily $h/g\mid j$ and $h'/g\mid j'$. The two meshes then both become $x_q/g$. Using the same positive gcd count and Fourier envelope as in [the zero determinant](weak-s-type-ii-critical-prime-full-unit-dual-determinant-grh.md#3-use-the-original-units-on-the-determinant-diagonal), the diagonal at $l,s,\tau$ is bounded by

$$
 \frac{N^2}{L\,l^2}\big(1+\delta^{-1/2}+|\tau|\big)
       O_{C,F}\!\big(\mathcal L\big)
       \sum_{h,h'\mid\operatorname{rad}N}\frac1{[h,h']}
 \ \ll\ \frac{N^2}{L\,l^2}
          \big(1+\delta^{-1/2}+|\tau|\big)O_{C,F}(\mathcal L L_2^3).
 \tag{5}
$$

The key cancellation of physical scales is exact $Ux_0=X/l^2$. The logarithm of the reciprocal mesh and the retained $\tau$ frequencies is now $O(\mathcal L)$ instead of $O(L_2^2)$; the Euler sum is still $\prod_{p\mid N}(1+3/p)\ll L_2^3$.

For nonzero determinant write $h j'u-h'j u'=bq$, $b\ne0$, as there. At fixed $h,h',j,j',b$ the integral has one polynomial $A(hj'\theta)=\sum_u a_u e(hj' u\theta)$, its conjugate at $h'j\theta$, and a $q$ polynomial with distinct frequencies $-bq$, each coefficient $O(X^2)$. To bound the first polynomial use (2) with the exact $(u,lN)=1$ mask. Convolve $\mu$ with the indicator of integers $b_0$ supported on the primes of $lN$. For $b_0\le\sqrt U$ the harmonic sum of $1/b_0$ is $O(L_2)$ by the full Euler product, and the rescaled hard prefixes have length of order $U/b_0\ge\sqrt U$. Uniform (2) gives $O(U L_2 e^{-c_5\sqrt L})$ there. For $b_0>\sqrt U$ the trivial tail is at most

$$
 U^{1-1/8}\prod_{p\mid lN}(1-p^{-3/4})^{-1}
                         \ll U^{1-1/8}\exp(O(L^{1/4})).
$$

For the last bound split primes at $L$ and use the sum over all integers up to $L$ and at most $O(L)$ prime divisors above $L$. Abel summation of the actual log weight costs $1+|\tau|$ and the sharp long interval entails just its two exact endpoints. Since $\mathcal L=o(\sqrt L)$, this proves $\|A\|_\infty\ll U e^{-c_6\sqrt L}$ uniformly on all retained $\tau$. The other long factor costs $O(\sqrt U)$ by Plancherel, and the distinct $q$ polynomial costs $O(X^2\sqrt{\#\mathcal Q})$. The $b$ values satisfy $|b|\ll \lambda H\exp(C_2\mathcal L)$, so the number of all these retained tuples is $\exp(O_{C,F}(\mathcal L))$. Moreover $U^{3/2} X^2\sqrt{\#\mathcal Q}\ll N^2\Lambda^{3/2}$. Thus the total absolute nonzero-determinant error is $O(N^2e^{-c_7\sqrt L})$. This is the only place the R88 GRH estimate needed replacement. It now uses the explicitly imported UZG via (2), and no power saving in $N$ is claimed.

Taking the square root of (5), the $\tau$ integral costs $O(\delta^{-1/2})$ as in the original joint norm, and the $l,s$ tuples cost $\sum_{l\le T_0}\tau_{\rm d}(l)/l\ll(1+\log T_0)^2$. Here $\tau_{\rm d}$ is the divisor-counting function. The actual $\beta$ integration is of length $1/(5N)$. This gives squared nonprincipal energy $O(N L^{-1+B+\varepsilon})$ on the dyad for every fixed $\varepsilon>0$, since all powers of $\mathcal L,L_2$ are absorbed.

Restore the exact nonunit and principal components as in the full-unit theorem, finally noting that the nonunit bound need not cost a power of the widened interval. If $q\mid N$, the exact long units and $k<X/2<q$ exclude every nonunit product. Otherwise $q\mid d$ leaves $O(\lambda)$ possible $d=j q$. For each, summing absolute truncated labels over $k\ll K$ costs at most $O(K(\sum_{h\mid\operatorname{rad}N}1/h)\prod_{p\mid d}(1+1/p))\ll K L_2^2$, since $(l,h)=1$ and the required square label modulus is $l^2/(l,d)$. Use Mertens with $\log d=O(L)$ to bound the prime product by $O(L_2)$, not an estimate by $\tau_{\rm d}(j)$. Thus the actual additive nonunit polynomial is $O(XL_2^2)$ and has squared shell energy $O(NL^{-1+\varepsilon})$. The principal unit polynomial follows from the true numerator-zero value and the ordinary square norm plus this nonunit error, with $\sum_q1/(q-1)\ll1/L$. Neither one is the algebraic principal or zero residue group added for an upper bound in the joint norm.

Set $B=\eta=1/2$, choose $\rho$ small in terms of the desired $\varepsilon$, use the ordinary transfers of §2 on the disjoint actual arcs by Parseval, and sum the $O(1+L_2^F)$ dyads in norm. This proves (1). The original Cauchy and centering steps are unchanged because the actual ordinary square norms remain $O(N)$. The parity-preserving even-lattice identity needs only the same exact oddness, physical support and ordinary norms, and keeps its error $O(N/L+N(X/M)^2)$ at the stated $M$. This yields the three signed consequences, without asserting bounds on individual compensated offset squares or on a different prime shell.
