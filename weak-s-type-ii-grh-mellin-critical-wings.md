# A shifted-character Mellin bound for the actual rational wings

Assume global Dirichlet GRH, including RH for $\zeta$. Retain the exact $P_E,D$, even $N$, unit/squarefree masks, and hard cuts of the [conditional near-square-root analysis](weak-s-type-ii-grh-near-square-root-arcs.md). In particular $D$ contains $d\ge\sqrt N$, $k>t\ge N^{.49999}$, $N-y\le dk<N/2$, $\mu(d)\mu^2(k)\mathbf1_{(d,k)=1}$, and $(dk,N)=1$. The selector $|E(u,v)|\le1$ is arbitrary and independent of $d,k$. Write $L=\log N$ and $e(z)=e^{2\pi iz}$.

**Theorem.** Fix $C\ge1$. For a set $\mathcal Q$ of integers $1\le q\le N^C$ and real widths $0\le B_q\le N^C$ define

$$
  \mathfrak A=\bigcup_{\substack{q\in\mathcal Q\\(a,q)=1}}
       \{a/q+\beta\bmod 1:|\beta|\le B_q/N\}.
$$

Then for every fixed $\epsilon>0$,

$$
 \int_{\mathfrak A}|D(\alpha)|^2\,d\alpha
      \ll_{C,\epsilon} N^\epsilon
          \sum_{q\in\mathcal Q}(q+\sqrt N)(B_q+B_q^2).
$$

In particular, if the sum on the right without $N^\epsilon$ is $O(N^{1-\delta})$ for some fixed $\delta>0$, then $\int_{\mathfrak A}|P_ED|\ll N^{1-\delta/4}$ for sufficiently large $N$. For instance, one can take **all** $q\le N^{.4}$ and $|\beta|\le N^{-.951}$, among other choices outside the previous parameter region. More generally, all $q\le N^\kappa$ and $|\beta|\le N^{-1+\lambda}\exp((\log N)^{3/5}(\log\log N)^{-1/5})$ are allowed with a fixed power saving if $\kappa>0,\lambda\ge0,\ \kappa+2\lambda<1/2$. The theorem also covers arbitrary deterministic subfamilies of at most $N^{1/2-\delta}$ denominators $q\asymp\sqrt N$ with bounded $B_q$. It gives no estimate for the remaining signed covariance; in particular it does not control a full shell of critical denominators.

## 1. The hard cut is exact at every integer

On a $d$ dyad of scale $D_0\ge\sqrt N/2$, take a fixed hard $k$ interval of scale $K_0=N/D_0$ containing every $k$ allowed by $N-y\le dk<N/2$ on that dyad. Keep the independent strict cut $k>t$ exactly in this interval. No $d$-cell freezing is performed.

Let $m_-=\lceil N-y\rceil$, $m_+=N/2-1$. If $m_->m_+$ the polynomial is zero. Otherwise put

$$
  a_0=\log((m_--1/2)/N),\qquad b_0=\log((m_++1/2)/N).
$$

Convolve $\mathbf1_{[a_0,b_0]}$ in the real logarithmic variable $z$ with a nonnegative smooth mollifier of integral one, supported within a sufficiently small absolute constant times $1/N$ of zero. Call the result $w(z)$. The two endpoints lie in half-integer gaps in the physical product. On the compact proportional range of the walls, each nearest integer has logarithmic distance $\gg1/N$ from the corresponding endpoint. Hence for every positive integer $m$,

$$
 w(\log(m/N))=\mathbf1_{m_-\le m\le m_+}.
$$

The support of $w$ is in a fixed compact interval, $|w|\le1$, $\|w'\|_1\ll1$ and $\|w''\|_1\ll N$, all including an interval of just one allowed integer. Thus the smooth multiplier has **no change of the hard product gate at integer arguments**.

For $\beta$ real let $B=N|\beta|$ and $f_\beta(z)=w(z)e(\beta N e^z)$. Define its Fourier transform by $\widehat f_\beta(s)=(2\pi)^{-1}\int f_\beta(z)e^{-isz}\,dz$, so inversion uses $e^{isz}$. For any fixed polynomial height $T\ge2$, Plancherel on $|s|\le C_1(1+B)$ gives an $L^1$ bound $O(\sqrt{1+B})$ there. For $|s|>C_1(1+B)$ with a sufficiently large absolute $C_1$, the phase derivative $2\pi\beta N e^z-s$ has magnitude $\gg|s|$ throughout the support and its second derivative is $O(B)$. Integration by parts gives

$$
   |\widehat f_\beta(s)|
      \ll \|w'\|_1/|s|+B\|w\|_1/s^2\ll |s|^{-1}.
$$

Therefore $\int_{|s|\le T}|\widehat f_\beta(s)|\,ds\ll_C L+\sqrt{1+B}$ for $T=N^{2C+20}$. Also $\|f_\beta''\|_1\ll N+(1+B)^2$, so the $L^1$ tail past $T$ is $O_C(N^{-15})$ for $B\le N^C$. Uniform Fourier inversion now separates $w(\log(dk/N))e(\beta dk)$ into a weighted integral of $(dk/N)^{is}$ at polynomial heights, with the stated $L^1$ norm and a negligible pointwise tail. The arithmetic masks do not participate in the smoothing.

## 2. Shifted GRH transforms of the exact factors

We use the square-root prefix bounds of [the near-square-root proof, §2](weak-s-type-ii-grh-near-square-root-arcs.md#2-exact-character-strata-on-one-rectangle), now with the additional factor $n^{is}$ for $|s|\le T$. For $\mu(n)\chi(n)$ the Dirichlet series becomes $1/L(z-is,\chi)$ with the corresponding unit factors. For $\mu^2(n)\chi(n)$ the nonprincipal series becomes $L(z-is,\chi)/L(2z-2is,\chi^2)$, again with the exact unit factors. The fixed-line GRH bounds for $L$ and $1/L$ of nonprincipal characters at polynomial heights, and the absolute Euler bound for the denominator with $\Re(2z)>1$, give the same hard Perron proof on $\Re z=1/2+\eta$, fixed $\eta>0$. At a principal $\mu$ twist, use the ordinary [RH bound for the reciprocal zeta function, Titchmarsh (14.2.6)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=173), uniformly on a fixed right-hand substrip; $1/\zeta$ is zero at the removable point $1$, not singular there. All finite factors from imprimitive or extra unit masks of polynomial size are $N^{o(1)}$ on that line. With half-integer endpoints, take a larger polynomial Perron height, and choose $\eta$ and the subpower bound small relative to the fixed $\epsilon$. This proves the estimates $O_{C,\epsilon}(\sqrt Y N^\epsilon)$ uniformly for hard prefixes on either factor, including the principal Möbius character and the nonprincipal squarefree characters. The principal squarefree leg is still trivial $O(Y)$, since the Mellin twist has modulus one.

For clarity the exact algebra of the complementary sum is unchanged. Fix $q$ and group $g=(dk,q)$ on its squarefree support. Then $g$ is squarefree, $g=g_dg_k$ with its unique placement in $d$ or $k$, and after $d=g_d x,k=g_k z$ the rational phase is $e(a xz/l)$, $l=q/g$. The remaining masks are $(xz,qN)=1$ and $(x,z)=1$. Expand the latter by the common divisor $r$ and put $x=ri,z=rj$; surviving $r$ are squarefree and all inherited unit masks are retained. With a Mellin phase $(dk/N)^{is}$ the two factors now separate exactly at scales $D_0/(g_d r)$ and $K_0/(g_k r)$, and the residual constant $(g r^2/N)^{is}$ has modulus one. The character in the group modulo $l$ also separates, with scalar $\chi(r)^2$. Thus the product of the two shifted square-root bounds, summed over $r$, is $O_{C,\epsilon}(N^{1/2+\epsilon}/\sqrt g)$ for a nonprincipal character on this dyad. For a principal character use just the shifted Möbius bound and the trivial squarefree bound, giving $O_{C,\epsilon}(N^{3/4+\epsilon}/\sqrt g)$ since $D_0\gg\sqrt N$; the common-$r$ summation uses $r^{-3/2}$ rather than $r^{-1}$. These are on the whole uncut dyadic rectangle for each fixed Fourier frequency; integrating against $\widehat f_\beta$ supplies the exact hard product wall by §1.

## 3. Integrated bounds for arbitrary rational widths

Use multiplicative Parseval on the unit group modulo $l=q/g$ and lift numerators from $l$ to $q$, as in [the exact numerator analysis](weak-s-type-ii-grh-near-square-root-arcs.md#3-numerator-norms-and-the-near-square-root-range). In the nonprincipal part the numerator $\ell^2$ norm is bounded by $\sqrt{\varphi(q)}$ times the character-transform supremum after lifting; $\sum_\chi|\tau_l(\chi)|^2=\varphi(l)^2$. The principal Ramanujan coefficient is $\mu(l)/\varphi(l)$ and $\varphi(l)^{-1}\ll_\epsilon N^\epsilon g/q$, so summing the factors $g^{-1/2}$ there gives $q^{-1/2}N^{o(1)}$ before taking the numerator norm. The number of divisor strata and dyads costs only a subpower for $q\le N^C$. These statements apply directly also to $q$ not prime to $N$: only $g$ prime to $N$ occur, and no $\chi$ is presumed primitive.

Combining the two numerator norm bounds with the Mellin $L^1$ estimate and absorbing powers of $L$ gives, for fixed $\beta$ with $N|\beta|\le N^C$,

$$
 \left(\sum_{a\bmod q}^{*}|D(a/q+\beta)|^2\right)^{1/2}
     \ll_{C,\epsilon}
       N^\epsilon (N^{1/2}\sqrt q+N^{3/4})\sqrt{1+N|\beta|}.
$$

The truncated Fourier inversion tail contributes negligibly to this bound by the trivial count of $O(NL)$ pairs; squaring and summing is legitimate without additional normalization. Integrate the square over each $|\beta|\le B_q/N$ to obtain the theorem, by $\int_{-B_q/N}^{B_q/N}(1+N|\beta|)\,d\beta\ll(B_q+B_q^2)/N$. If arcs overlap, summing their integrals only increases the nonnegative bound.

For the power corollary use $\|P_E\|_2^2\ll NL^5$ from the actual coefficient bound $L\tau(m)$ and the ordinary divisor moment. Choose $\epsilon$ small relative to the fixed saving and absorb the logarithms. For uniform cutoffs the two power conditions before the subpower loss are $2\kappa+2\lambda<1$ and $\kappa+2\lambda<1/2$, the second implying the first. This is a larger conditional rational region, not a bound on the full signed integral.
