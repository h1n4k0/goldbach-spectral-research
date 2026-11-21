# Adaptive rectangles on doubled squares: selected exceptional sets without ratio slicing

**Proved under global Dirichlet GRH.** Write $X=8R^2$, $L=\log X$, $N=2r^2$ for $R<r\le2R$, and $J=[\log(1/2),\log(9/16)]$ in the normalized physical log coordinate. Let $\mathcal T_{N,J}=\mathbf1_J T_{N,\log}\mathbf1_J$ for the actual Li–Liu operator. For any fixed $0<\kappa<1/5$, $\epsilon>0$, and $X^{-1/5+\kappa}\le\tau\le1$,
$$
 \#\{R<r\le2R:\|\mathcal T_{2r^2,J}\|_{\rm HS}>\tau\}
 \ll_{\kappa,\epsilon}X^{1/3+\epsilon}\tau^{-7/3}. \tag{1}
$$
In particular for each $a<1/14$ the norm of this block is $\le X^{-a}$ outside a power-saving fraction of the doubled-square moduli. Moreover
$$
 \frac1{\#\{R<r\le2R\}}\sum_{R<r\le2R}\|\mathcal T_{2r^2,J}\|_{\rm HS}^2
 \ll_\epsilon X^{-1/7+\epsilon}. \tag{2}
$$
This is a single fixed compensated block and a sparse family. It is not an estimate for every doubled square, every even modulus, or the full residual. Global GRH is used for auxiliary major-arc conductors, and local GRH for the operator identification. There is no proof or disproof of S/R.

## 1. A selected $\ell^1$ estimate allowing completely adaptive boxes

For each $s=2r^2$, let $I_s^{(1)},I_s^{(2)}\subset[0,s]$ be arbitrary real intervals: these may depend on $s$ and on the arithmetic data. Set
$$
 A_s=\sum_{n+m=s}\Lambda(n)\Lambda(m)
          \mathbf1_{I_s^{(1)}}(n)\mathbf1_{I_s^{(2)}}(m),\quad
 V_s=\int_{\mathbb R}\mathbf1_{I_s^{(1)}}(u)\mathbf1_{I_s^{(2)}}(s-u)\,du .
$$
For any selected set $E$ of $M$ values of $r$, and real signs $|\sigma_r|\le1$, the normalized selected error obeys
$$
 \frac1X\left|\sum_{r\in E}\sigma_r\left(A_s-\mathfrak S(s)V_s\right)\right|
 \ll_\epsilon
 \sqrt M\,X^{1/4+\epsilon}P^{-1/4}
 +M\left(X^{-1/2}P^{3/2}L^2+X^{-1}P^3 L^5+X^{\epsilon}/P\right),
 \qquad 2\le P\le X^{1/3}.                                  \tag{3}
$$
There is no subdivision of the $r$-interval by ratios.

**Collapse first.** The condition $n+m=s$ expresses both windows as a single interval $I_s=I_s^{(1)}\cap(s-I_s^{(2)})$ in $n$; the $m$-sum is then uncut on $[0,X]$. Thus $V_s=|I_s|$ and with $e(u)=e^{2\pi i u}$,
$$
 A_s=\int_0^1 P_{I_s}(\theta)P_{\rm all}(\theta)e(-s\theta)\,d\theta,\quad
 P_I(\theta)=\sum_{n\in I}\Lambda(n)e(n\theta),\quad P_{\rm all}=P_{[0,X]}.
$$
As usual only positive integer indices contribute. Empty or singleton windows cause no issue.

**Individual major arcs.** Use the disjoint arcs $|\theta-a/q|\le P/(qX)$, $q\le P$, with reduced $a/q$. For each $s$ separately, apply the character-Parseval and summation-by-parts calculation of [Round 11 §1](arithmetic-post-round10-exceptions.md) to its two fixed intervals $I_s,[0,X]$. On each arc $|P_I(a/q+\gamma)-\mu(q)V_I(\gamma)/\varphi(q)|\ll\sqrt{Xq}L^2(1+X|\gamma|)$, while $|V_I(\gamma)|\ll X/(1+X|\gamma|)$. These bounds are uniform in the endpoints. In the product, the two mixed terms summed over $a,q$ and integrated cost $O(\sqrt X P^{3/2}L^2)$ and the two-error term costs $O(P^3L^5)$. Extending the Hardy–Littlewood integral and Ramanujan series costs $O_\epsilon(X^{1+\epsilon}/P)$ individually, using the same square-free divisor split of Round 11 for each $s\le X$. The full principal integral is $\mathfrak S(s)|I_s|$. This estimate is prior to summation over $E$ and sees no moving-window cost.

**Adaptive minor arcs.** An integer interval $I_s\cap\mathbf Z$ is a disjoint union of aligned dyadic intervals contained in it, with at most two at any given scale. This follows by selecting maximal dyadic subintervals in the usual partition of a single dyadic universe containing $[1,X]$. At a fixed scale the dyadic blocks $I$ are disjoint. Let $E_I$ consist of $r\in E$ for which that particular block was selected in $I_s$, and set $Q_I(\theta)=\sum_{r\in E_I}\sigma_r e(-2r^2\theta)$. In particular $\sum_I|E_I|\le2M$ at this scale. Summing over the dyadic scales rewrites the actual signed minor integrand exactly as $P_{\rm all}\sum_I P_I Q_I$.

For each $I$, the same selected fourth moment as Round 11 gives $\|Q_I\|_4^2\ll_\epsilon |E_I|X^\epsilon$, after relabeling $\epsilon$. Indeed the zero difference $r^2-u^2=0$ has $|E_I|$ representations, each nonzero difference has at most a divisor bound through $(r-u)(r+u)$, and the total multiplicity is $|E_I|^2$. Hölder with exponents $4,2,4$ on the minor arcs, then Cauchy in the block index, gives at each dyadic scale
$$
 \sum_I\int_{\mathfrak m}|P_{\rm all}P_IQ_I|
 \le \|P_{\rm all}\|_{4,\mathfrak m}
        \left(\sum_I\|P_I\|_2^2\right)^{1/2}
        \left(\sum_I\|Q_I\|_4^2\right)^{1/2}.
$$
Disjointness and Parseval bound the middle factor by $O((XL)^{1/2})$. For the first factor, only the uncut $P_{\rm all}$ needs a minor-arc sup estimate. Dirichlet approximation and the [Vinogradov–Vaughan estimate](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf) give $\sup_{\mathfrak m}|P_{\rm all}|\ll XP^{-1/2}L^4$; the $X^{4/5}$ term is smaller for $P\le X^{1/3}$. Interpolation with its full $L^2$ norm yields
$$
 \|P_{\rm all}\|_{4,\mathfrak m}\ll X^{3/4} P^{-1/4} L^{9/4}.
$$
The last factor is $\ll_\epsilon \sqrt M X^\epsilon$ at this scale. Sum at most $O(L)$ levels, absorb logarithms into the arbitrary $X^\epsilon$, and combine with the individual main-arc errors to prove (3). Neither uniform pointwise control of each adaptive prime sum nor a union bound over interval choices is used.

## 2. Supremum inside the selected average and the exact block

Take $\sigma_r$ to be the sign of each discrepancy. Since (3) allows arbitrary intervals per $r$, choose intervals with discrepancies at least half the individual supremum, and obtain (3), up to a factor 2, for
$$
 \sum_{r\in E}\sup_{I_1,I_2\subset[0,s]}
       \frac{|A_s(I_1,I_2)-\mathfrak S(s)V_s(I_1,I_2)|}{X}.
$$
The supremum is inside the selected sum, not an averaged estimate for a single fixed test. Reimposing unit summands costs $O(X^{-1/2}L^2)$ per normalized count: distinct prime summands are both units; any proper prime-power summand has $O(\sqrt X)$ possibilities and determines its partner.

For $x=e^p,y=e^q$ with $p,q\in J$, the physical cumulative $(0,x]\times(0,y]$ of the true operator contains no difference aliases, only the first sum alias, and the diagonal is already subtracted. The model likewise contains only $u+v=1$. By the exact cumulative kernel identity in the [pinned Round 10 source](https://github.com/h1n4k0/goldbach-spectral-research/blob/df49c707d35986232009cff619b9b23cdaa4dad3/arithmetic-round10.md), the only extra arithmetic weight within this box is $\sqrt{uv}$, and the multiplicative kernel normalizations are uniformly bounded on $J^2$. Positive layer cake writes the weighted discrepancy as the integral of unweighted rectangle discrepancies on $[h,x]\times[k,y]$ against $dh\,dk/(4\sqrt{hk})$, whose total mass is $\sqrt{xy}=O(1)$. It follows, *for each modulus*, that the HS norm is bounded linearly by the supremum of its unit arithmetic-minus-model discrepancy with normalization $1/s$; normalization by $1/X$ differs only by an absolute factor. In particular no multiplication by an upper-sieve bound to estimate the square of the kernel is needed. This gives from (3)
$$
 \sum_{r\in E}\|\mathcal T_{2r^2,J}\|_{\rm HS}
 \ll_\epsilon \sqrt M\,X^{1/4+\epsilon}P^{-1/4}
 +M\left(X^{-1/2}P^{3/2}L^2+X^{-1}P^3L^5
             +X^\epsilon/P+X^{-1/2}L^2\right). \tag{4}
$$

For a prescribed $\tau$ set $P=\lfloor X^{1/3}\tau^{2/3}L^{-10}\rfloor$. For $\tau\ge X^{-1/5+\kappa}$ this is between 2 and $X^{1/3}$ for sufficiently large $X$. The first two major errors in parentheses are $O(\tau L^{-13}+\tau^2L^{-25})$; the third divided by $\tau$ is $O(X^{\epsilon-1/3}\tau^{-5/3}L^{10})=o(1)$ when the internal $\epsilon<5\kappa/3$. The unit error is also $o(\tau)$. Choose $E$ to be the exceptional set in (1) and absorb these terms into $M\tau$. Squaring the resulting $\sqrt M$ bound gives $M\ll_{\kappa,\epsilon}X^{1/3+\epsilon}\tau^{-7/3}$.

For the mean, put $\tau_0=X^{-1/14}$ and choose a fixed $\kappa$ with $1/14<1/5-\kappa$. Norms $\le\tau_0$ contribute at most $\tau_0^2$ to the normalized layer-cake integral. On $[\tau_0,1]$ insert (1), divide by the $\asymp X^{1/2}$ family size, and integrate $2\tau$ times the distribution bound to obtain $O_\epsilon(X^{-1/6+\epsilon}\tau_0^{-1/3})=O_\epsilon(X^{-1/7+\epsilon})$. Finally the uniform bound $\|\mathcal T_{s,J}\|_{\rm HS}\ll L$ follows already by Cauchy on the arithmetic $n+m=s$ sum, $\sum_{n\le X}\Lambda(n)^2\ll XL$, and $\mathfrak S(s)\ll L$. Thus the range above 1 contributes $O_\epsilon(L^2 X^{-1/6+\epsilon})$ via the exception count at 1. This proves (2).

**What still fails pointwise.** Even for $M=1$, after optimizing the major cutoff the minor term in (4) is much larger than the tested scale. The improvement is that we can select both the bad support and each modulus's worst rectangle, not that we can now eliminate any remaining individual exceptions. No claim about all cross blocks or the top spectrum follows.
