# Unconditional power cancellation on the exact moving Dirichlet complement for almost all dense targets

Use the genuine dense rectangle of the [maximal cofactor estimate](r46-source-dense-cell-maximal-exception-improvement.md). Fix $0<\rho<1/2$, take $N$ even, and impose $N^{.38}\le q\le N^{.42}$, $N^{.08}\le s\le N^{.12}$ on the small prime cofactors of $qp,sv$, with genuine prime giants $p,v$. The original masks $(qp,N)=(sv,N)=1$ are retained. Use the marker $(\log q)(\log s)$ and both orders of the products, with a moving hard $I\subseteq I_0(N)=[\rho N,(1-\rho)N]$ in the first slot and $I_0(N)$ in the second. Denote the resulting actual product polynomial by $\mathcal P_I(N;\alpha)$; the four prime ranges are pairwise disjoint for large $N$.

Put $Q_N=\lfloor\sqrt N\rfloor$ and $R_N=\lfloor Q_N(\log N)^{-200}\rfloor$. The **[exact Dirichlet arc set](r35-source-square-root-dirichlet-arcs.md)** $\mathfrak D_N$ is the union of the complete reduced arcs $r\le R_N$, of widths $1/(rQ_N)$, and $\mathfrak m_N=\mathbb T\setminus\mathfrak D_N$. Let $e(t)=e^{2\pi it}$.

**Theorem (unconditional).** For fixed $0<\eta\le1/100$ and sufficiently large $X$, outside a set of

$$
 O_{\rho,\eta}\!\left(X^{31/50+6\eta}(\log X)^{23}\right)
                                                              \tag{1}
$$

even targets $N\in[X,2X]$, one has

$$
 \sup_{I\subseteq I_0(N)}
   \left|\int_{\mathfrak m_N}\mathcal P_I(N;\alpha)e(-N\alpha)\,d\alpha\right|
       \ll_{\rho,\eta} N^{1-\eta}.                             \tag{2}
$$

The supremum includes the original exact hard endpoint conventions. For instance $\eta=1/100$ gives $O(X^{17/25}(\log X)^{23})$ exceptions at a power saving $N^{99/100}$ in the actual signed integral, without a GRH input. The normalized squared mean, averaging over the even dyad and dividing the integral by $N$, is $O_{\rho,\eta}(X^{-2\eta})$. This does not give a bound at individual exceptional targets. R46 gives a smaller exceptional set at the same power accuracy for its distinct full-torus comparator problem under GRH; it is not used here to evaluate the moving exact minor integral.

## 1. Encode the moving exact arcs as two prefix coordinates

Let $L=\log X$, $P=X^{2/5}$. Use auxiliary rational arcs $\mathfrak D^*_X$ at reduced denominators $r\le P$ with widths $P/(rX)$ and put $\mathfrak m^*_X=\mathbb T\setminus\mathfrak D^*_X$. For all $N\in[X,2X]$ and sufficiently large $X$ one has $P\le R_N$ and $P/X\le1/Q_N$, so $\mathfrak D_X^*\subseteq\mathfrak D_N$.

Take $Q_*=\lfloor\sqrt X\rfloor$ and $R^*=\lceil \sqrt{2X}L^{-200}\rceil$. The ambient wide arcs $\mathfrak W_X$ include every reduced denominator $r\le R^*$ with width $1/(rQ_*)$. They are pairwise disjoint because the sum of two widths times the product of their denominators is at most $2R^*/Q_*<1$ for large $X$. They contain every $\mathfrak D_N$. On $\mathfrak W_X\cap\mathfrak m_X^*$ a point has a unique arc denominator $r(\alpha)$ and offset $\beta(\alpha)$ (with its unique small lift on the circle). Assign to it the coordinates $r(\alpha)$ and $v(\alpha)=r(\alpha)|\beta(\alpha)|$. Discretize the second coordinate into successive bands whose upper endpoints are the possible $1/Q_N$ in increasing order, starting at zero and ending at $1/Q_*$. A band endpoint can be assigned with the upper-closed convention; there are at most $O(\sqrt X)$ bands and rational centers themselves have measure zero.

Inside $\mathfrak W_X\cap\mathfrak m_X^*$ the subset $\mathfrak D_N\setminus\mathfrak D_X^*$ is exactly the rectangle of prefixes with $r(\alpha)\le R_N$ and $v(\alpha)\le1/Q_N$. Define $\mathcal R$ to be the family of such two-coordinate prefix rectangles with **arbitrary** separate cutoff ranks. For any $\mathcal U\in\mathcal R$ set $\Omega_{\mathcal U}=\mathfrak m_X^*\setminus\mathcal U$. Then the exact $\mathfrak m_N$ is one such $\Omega_{\mathcal U}$, up to a null set. Crucially all the fixed rank cells lie inside $\mathfrak m_X^*$, where a single bilinear saving is available.

## 2. A four-axis maximal Bessel bound

For fixed hard physical windows $J,K$ within $[\rho X/2,2X]$, consider the ordinary true-prime polynomials $A_{J,E}$ and $A_{K,F}$ from the [power-sparse exceptions argument](r45-source-dense-cell-power-sparse-exceptions.md) without any target-dependent unit exclusions. The cofactor domains $E,F$ may be subsets of the two fixed ambient envelopes, each a union of at most a fixed number $D_0$ of integer intervals. The large cofactor uses the $.38,.42$ envelope and the small cofactor the $.08,.12$ envelope; both orders of these in $J,K$ will be handled. At fixed levels of the standard integer dyadic partitions of the two cofactor axes, the cell estimates proven by the disjoint-pair Cauchy argument of R46 give

$$
 \sup_{\alpha\in\mathfrak m_X^*}\sum_{E'}|A_{J,E'}(\alpha)|^2
            \ll_\rho X^{2-.38}L^5,\qquad
 \int_{\mathbb T}\sum_{F'}|A_{K,F'}(\alpha)|^2\,d\alpha
            \ll_\rho XL^2,                                   \tag{3}
$$

when the large cofactor uses $J$. If it uses $K$ the two roles in (3) swap. For clarity, these statements require no GRH. In each ordinary multiplicative cofactor dyad $U$, Cauchy first in the giant and geometric summation over the intersection of two admissible $p$ intervals give the usual min-sum over the differences $h=q-q'$. Over disjoint cofactor cells at one partition level there are still at most $O(U)$ ordered pairs per fixed $h$. The outcomes are the dyad bound $X^2L^3(U^{-1}+V^{-1}+r^{-1}+r/X)$, $V=X/U$, from R44, and the extra $L^2$ for aggregation. The denominator $r$ of a Dirichlet approximant on the fixed $\mathfrak m_X^*$ lies between $P$ and $\lceil X/P\rceil$ and satisfies the spacing hypothesis. The small-leg energy sum follows by Parseval and the unique small/giant prime factorization of each frequency and the disjoint cofactor cells.

Put

$$
 b_{E,F,\mathcal U}(n)
 =\int_{\mathcal U} A_{J,E}(\alpha)A_{K,F}(\alpha)e(-n\alpha)\,d\alpha .
$$

Decompose each cofactor interval (or each of its $D_0$ components) into $O(L)$ disjoint aligned dyadic cells. Also decompose both prefix coordinates of $\mathcal U$ into $O(L)$ aligned dyadic rank cells. The resulting expansion of the coefficient has $O_{D_0}(L^4)$ terms. Cauchy bounds the square of its maximal value at a target by $O_{D_0}(L^4)$ times the sum of squares over all four level indices and all respective cells, independently of the chosen cofactor sets and arc prefixes.

At fixed four levels the corresponding arc cells $B$ partition $\mathfrak W_X\cap\mathfrak m_X^*$ up to endpoints. Thus Bessel and the disjointness yield

$$
 \sum_{n\in\mathbb Z}\sum_{E',F',B}|b_{E',F',B}(n)|^2
 \le\int_{\mathfrak m_X^*}
       \left(\sum_{E'}|A_{J,E'}|^2\right)
       \left(\sum_{F'}|A_{K,F'}|^2\right)d\alpha
 \ll_\rho X^{3-.38}L^7.                                        \tag{4}
$$

The number of four level choices is $O(L^4)$. Consequently the maximal two-cofactor/two-arc coefficient has summed square $O_{\rho,D_0}(X^{3-.38}L^{15})$. For the coefficient on the whole $\mathfrak m_X^*$ the same two-cofactor argument has only $L^{11}$ instead, as in R46. Taking the difference and using the square triangle bound gives

$$
 \sum_{n\in\mathbb Z}
    \sup_{E,F,\mathcal U\in\mathcal R}
       \left|\int_{\Omega_{\mathcal U}}
          A_{J,E}(\alpha)A_{K,F}(\alpha)e(-n\alpha)\,d\alpha\right|^2
      \ll_{\rho,D_0}X^{3-.38}L^{15}.                            \tag{5}
$$

This controls the signed coefficients at the moving *exact* masks because $\mathfrak m_N$ is in that family, not because it is interchangeable with the fixed auxiliary mask.

## 3. Restore target-dependent prime units and both hard windows

Use a grid spacing $\Delta=X^{1-2\eta}L^{-4}$ for a single first physical prefix endpoint. The prefix starts at $\rho X/2$ and its endpoint covers the actual endpoint range, with room for an extra step inside the ambient interval. It suffices to use prefixes because the same $\mathfrak m_N$, cofactor ranges and second window apply to both endpoints of $I$, and the signed first-slot expression is additive. An open or closed hard prefix is within $O(\Delta+1)$ integer indices of a strict or non-strict grid prefix in the corresponding physical region. Also freeze the second window using a grid on $[X,2X]$ of spacing $\Delta$: at grid point $N_j$ use $K_j=I_0(N_j)$, whose two endpoints differ from the true $I_0(N)$ by $O_\rho(\Delta)$. There are $O_\rho(X^{4\eta}L^8)$ combinations of these first-prefix and second-window choices, including both orders.

At threshold $X^{1-\eta}$, (5) leaves $O_{\rho,D_0}(X^{.62+2\eta}L^{15})$ bad targets per frozen window pair. The union bound over just the physical grids gives (1). For a good target $N$, select $E,F$ to be the exact cofactor bands excluding the primes dividing $N$. At most $O(1)$ primes in the fixed bands can divide $N$, since they are all at least a fixed multiple of $X^{.08}$. Hence these cofactor masks are representable by a union of at most a fixed absolute $D_0$ integer intervals on each side, with the excluded prime points removed exactly. They are among the choices in (5).

It remains to exclude $p$ or $v$ when it divides $N$, which is not automatic on a partial circle. Every giant prime exceeds $\sqrt{2X}$ for all the allowed physical windows and sufficiently large $X$, and is $\gg_\rho X^{.58}$. At most one such prime can divide $N\le2X$. Fixing it as the giant allows at most $O_\rho(X^{.42})$ cofactor indices; by Parseval the removed transform has squared norm $O_\rho(X^{.42}L^2)$. Its contribution against the other actual factor in any arc integral is $O_\rho(X^{.71}L^2)$ by Cauchy and the unrestricted squared norm $O_\rho(XL^2)$. This argument also applies after imposing the cofactor masks and when changing the windows.

For restoration of a physical window from its grid value, the Fourier coefficient differences are supported on $O_\rho(\Delta+1)$ integer indices, with marker $O(L)$ and unique factorization. Thus by full-torus Parseval and Cauchy on the exact $\mathfrak m_N$, each product edge contributes at most $O_\rho(\sqrt{X(\Delta+1)}L^2)=O_\rho(X^{1-\eta})$. This works for either hard endpoint convention and for the second interval just as for the first. After both restorations take the difference of two exact prefixes to obtain any $I$ (including a possible included singleton) and sum the two orientations. All errors are $O_{\rho,\eta}(X^{1-\eta})$ on the good target, proving (2). No positivity or full-torus second-window substitution is used to restore this partial-circle result.

At exceptional targets the unconditional trivial bound for each actual signed integral is $O_\rho(NL^2)$ by the two torus norms. Therefore (1) and (2) give the normalized squared mean $O_{\rho,\eta}(X^{-2\eta}+X^{-.38+6\eta}L^{27})=O_{\rho,\eta}(X^{-2\eta})$. The argument is only about the specified dense genuine four-prime product, not the full weak-S operator, and no pointwise estimate is claimed for all even $N$.
