# Rational-slope slices of the genuine four-prime minor integral

Retain the exact setup of the [full Dirichlet arcs](r35-source-square-root-dirichlet-arcs.md), the [four-distinct-prime reduction](r38-source-four-distinct-prime-minor-reduction.md), and the [small giant-gap slice](r39-source-four-prime-small-giant-gap.md). Fix $0<\rho<1/2$ and $0<\kappa\le1/2000$, let $N$ be sufficiently large and even, and put $L=\log N$, $I_0=[\rho N,(1-\rho)N]$. The first window is an arbitrary hard interval $I\subseteq I_0$ with either endpoint convention; the second stays $I_0$. Let $\mathcal Q$ be the primes $N^\kappa\le q\le N^{1/2-\kappa}$ that are coprime to $N$, $Q_*=\lfloor\sqrt N\rfloor$, $R=\lfloor Q_*L^{-200}\rfloor$, and

$$
 \mathfrak D=\bigcup_{\substack{1\le r\le R\\ a\bmod r,\ (a,r)=1}}
          \{\alpha\in\mathbb T:\|\alpha-a/r\|\le 1/(rQ_*)\},
 \qquad \mathfrak m=\mathbb T\setminus\mathfrak D .
$$

In the actual four-distinct-prime expansion of the genuine product $A_I A_{I_0}$, orient by the small primes for purposes of the mask only: $q>s$ are in $\mathcal Q$, and $p,v$ are the respective genuine large primes attached to $q,s$, both coprime to $N$. The two physical products are $qp,sv$, in their original ordered windows. In particular each large prime exceeds $\rho N^{1/2+\kappa}$ apart from possible equality at the stated lower endpoint, and the small and large prime ranges are disjoint for large $N$. Both original orderings are kept when allowed. The marker is always $(\log q)(\log s)$.

Fix $C_\rho=1+(1-\rho)/\rho$. For each $q\in\mathcal Q$ and integer $1\le b\le Q_*$, prescribe a finite set $\mathcal H_{q,b}\subset\mathbb Z\setminus\{0\}$. Keep a four-distinct tuple if *some* positive coprime pair $a,b$ with $1\le b\le Q_*$ and $a\le C_\rho b$ satisfies

$$
 h=bp-av\in\mathcal H_{q,b}.
$$

This is a union mask, not a sum with multiplicity over witnesses. The sets may depend on $N$ but are fixed as $I$ varies. Apply any further fixed tuple exclusion if desired. Write $\mathcal P_I(\alpha)$ for this exact masked product expansion and

$$
 B_*=\sum_{q\in\mathcal Q}\sum_{1\le b\le Q_*}(q,b)|\mathcal H_{q,b}|.
$$

**Theorem (unconditional).** Uniformly over the exact moving hard $I$, with $e(x)=e^{2\pi ix}$,

$$
 \left|\int_{\mathfrak m}\mathcal P_I(\alpha)e(-N\alpha)\,d\alpha\right|
    \ll_\rho B_* R L^4 .                                          \tag{1}
$$

In particular, for $1\le H\le\sqrt N$, keep genuine tuples for which some positive reduced slope $a/b$ satisfies $0<q b |bp-av|\le H$. Their signed integral on the exact complement is

$$
 O_{\rho,\kappa}(H\sqrt N\,L^{-195}).                              \tag{2}
$$

One may also require $s|p-v|>\sqrt N$, making this slice disjoint from the entire geometric R39 slice. The theorem does not estimate the four-prime term outside the named mask, or a centered masked product containing a synthetic term.

## Output multiplicity and numerator compression

Write $\mathcal P_I(\alpha)=\sum_M u_I(M)e(M\alpha)$. For each fixed output $M$, oriented cofactor $q$, denominator $b$, and prescribed $h$, any actual tuple satisfies

$$
 bM-qh=v(aq+bs).
$$

This positive integer is $O_\rho(N^{2-2\kappa})$: $a\le C_\rho b$, $b\le\sqrt N$, $sv\le N$ and $qv\le (q/s)N\le N^{3/2-2\kappa}$. It can have at most three distinct eligible prime divisors $v$ for large $N$, since each is at least $\rho N^{1/2+\kappa}$ and the product of four such primes exceeds that upper bound. For each candidate $v$, let $m=(bM-qh)/v$. Then $q a\equiv m\bmod b$. With $g=(q,b)$ this congruence either has no solution or pins $a$ to a single class modulo $b/g$. Thus $1\le a\le C_\rho b$ admits $O_\rho(g)$ possible $a$, even when $q\mid b$. Each fixes $s=(m-qa)/b$ and $p=(av+h)/b$. All integrality, primality, prescribed coprimality and moving endpoint conditions can only reduce the count. One recovers at most two original orderings per oriented tuple. Summing witnesses bounds the count of the union irrespective of duplicates, giving

$$
 0\le u_I(M)\ll_\rho B_* L^2.
$$

The coefficients are supported in $2\rho N\le M\le2(1-\rho)N$, hence $|M-N|\le N$. For large $N$ all four primes are odd, so $M$ is automatically even; no strengthening of that parity condition is used.

## Exact cutoff and unrestricted reduced slopes in the geometric mask

The finite Fourier mass bound of R39 is

$$
 \sum_{|k|\le N}\left|\int_{\mathfrak D}e(k\alpha)\,d\alpha\right|
   \ll R L^2 .
$$

It uses disjointness of the exact R35 arcs: for $k\ne0$ their complete-numerator integral is $\sum_{r\le R}c_r(k)\sin(2\pi k/(rQ_*))/(\pi k)$, and $\sum_{k=1}^N|c_r(k)|/k\le(1+L)\tau(r)$ by the divisor formula for $c_r$. The zero term is at most $2R/Q_*$. The coefficient bound above therefore costs $O_\rho(B_*RL^4)$ on $\mathfrak D$, while the exact full-torus coefficient is $u_I(N)=O_\rho(B_*L^2)$. Their difference proves (1) on $\mathfrak m$.

For the geometric condition set $\mathcal H_{q,b}=\{h:0<|h|\le H/(qb)\}$. Any valid slope with nonzero integer $h$ has $b\le H/q\le Q_*$, and

$$
 \frac{a}{b}\le \frac p v+\frac{H}{q b^2v}
     \le \frac{1-\rho}{\rho}+\frac{H}{\rho N}
     \le C_\rho .
$$

Here $p/v=(qp)/(sv)\cdot s/q$ and $qv\ge sv\ge\rho N$. Thus the denominator and numerator cutoffs in (1) discard none of these geometric tuples. Since $q$ is prime, splitting into $q\nmid b$ and $q\mid b$ gives

$$
 \sum_{b\le Q_*}\frac{(q,b)}b\le
     \sum_{b\le Q_*}\frac1b+\sum_{j\le Q_*/q}\frac1j\ll L.
$$

Consequently $B_*\ll H L\sum_{q\in\mathcal Q}1/q\ll_\kappa H L$, using prime harmonic mass over the fixed polynomial range. This proves (2). The mask is independent of $I$, so the same ordered first-leg additivity needed for bounded-variation physical weights is retained. None of these bounds uses GRH.

## A genuine macroscopic giant gap in the new slice

To see why the restriction $s|p-v|>\sqrt N$ need not empty the slice, let $X$ grow, write $U=X^{1/4}$ and $P=X^{3/4}$, and choose $s\in[U,(1+\epsilon)U]$, $q\in[2U,2(1+\epsilon)U]$ prime, with $0<\epsilon$ sufficiently small in terms of $\rho$. Existence follows from the ordinary PNT. We also require a prime $p\in[P,(1+\epsilon)P]$ and a prime $v$ in $(2p-J,2p]$, with integer $J=\lfloor(2P)^{1/4}\rfloor$.

For this last existence claim, apply the primary theorem of [Zaccagnini, *Primes in almost all short intervals*, Acta Arith. 84 (1998), p. 225](https://doi.org/10.4064/aa-84-3-225-244) with $x=2P$, $h=J$ and its allowed auxiliary function $\varepsilon(x)=0$. For this range the theorem bounds the Selberg integral for $\pi(t)-\pi(t-J)-J/\log t$ by $O(xJ^2(\log x)^{-2}(\log\log x/\log x)^2)$. Hence the bad set of $t\in[x,2x]$ with $\pi(t)-\pi(t-J)=0$ has measure $O(x(\log\log x/\log x)^2)=o(x/\log x)$. Since $J$ is an integer, if an integer $t_0$ is bad then every $t\in[t_0,t_0+1)$ is bad, apart from measure-zero endpoints. There are $\gg_\epsilon x/\log x$ distinct integer centers $2p$ of the required type by the PNT, and their unit intervals lie in $[x,2x]$ for large $X$. One such center is good, providing $v$. Since $2p$ is composite, $0<2p-v\le J$.

Set $N=qp+sv\asymp X$. It is even, all four primes are distinct, and each is coprime to $N$ because it does not divide the other corresponding product. The original two products are central for the chosen $\epsilon$, and both cofactors are in $\mathcal Q$ for sufficiently large $X$. With slope $a/b=1/2$ one has $0<2q|2p-v|\ll X^{7/16}<\sqrt N$, whereas $s|p-v|\asymp X\asymp N$. This invokes the short-interval theorem only for a witness outside R39, not in the signed upper bound. It does not provide a lower bound for the signed integral.
