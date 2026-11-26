# Quantitative rarity and shrinking prime disagreement for the positive omission test

Let $0<M<Q$ be fixed, and retain the actual positive omission statistic and cutoff from [the leading-constant theorem](weak-s-type-ii-critical-prime-positive-inclusion-tail-leading-constant.md). Put

$$
 v=\log\log Y,\quad \ell=\log v,\quad \lambda=Q/M,\quad
 Z=v^\lambda,\quad D_*=(M/(3\mathrm e))^\lambda .
$$

Thus $\mathcal F_Y$ is the set of even $N\in[Y,2Y]$ with $\mathcal T_N((\log Y)^Q)>(\log Y)^{-M}$, where $\mathcal T_N(H)=\sum_{r\mid\operatorname{rad}N,\ r>H}3^{\omega(r)}/r$. Write $E=\#\mathcal F_Y$. For fixed $B\ge1$, use the same literal [prime disagreement statistic](weak-s-type-ii-critical-prime-positive-inclusion-conditional-prime-occupancy.md)

$$
   J_N(B)=\sum_{p\le Z^B}
        |\mathbf1_{p\mid N}-\mathbf1_{p\le D_*Z}|\log p .
$$

**Theorem.** For all sufficiently large $Y$,

$$
     \log(E/Y)=-D_*Z+O_{Q,M}(Z/\ell).                               \tag{1}
$$

For every fixed $B\ge1$ there exist $\tau_0,c,K>0$, depending only on $Q,M,B$, such that uniformly for $K/\sqrt\ell\le\tau\le\tau_0$ and all sufficiently large $Y$,

$$
      \frac{\#\{N\in\mathcal F_Y:J_N(B)\ge\tau Z\}}{E}
                            \le \exp(-c\tau^2Z).                   \tag{2}
$$

The range in (2) includes a shrinking disagreement threshold. These are statements about the positive omission criterion alone. They do not bound actual signed truncation error, centered-energy transport error, or Weak S, and do not assert all-or-none occupancy at individual primes.

## 1. Quantitative upper bound for the failure count

We use the classical quantitative prime number theorem in the form

$$
       \vartheta(x)=\sum_{p\le x}\log p
                      =x+O(xe^{-b\sqrt{\log x}})
                                                                    \tag{3}
$$

for some absolute $b>0$ and large $x$; for example, this follows from [Johnston–Yang, Corollary 1.2, p. 2](https://arxiv.org/pdf/2204.01980#page=2) by absorbing the fixed log power into the exponential. In particular $\pi(x)\ll x/\log x$.

In the upper moment let $\sigma_0=1/\lambda$, $a_0=1-\sigma_0$, $u=1/\lambda$, and put

$$
 \sigma=\sigma_0+u/\ell,\qquad a=1-\sigma,\qquad
 s=c_*v^{\lambda-1}\ell,\quad c_*=\frac{\lambda}{3\mathrm e}D_*^{a_0},
 \qquad t_p=(1+3p^{-a})^s .
$$

Write $X_N=\prod_{p\mid N}t_p$. The exact Rankin implication is unchanged: $N\in\mathcal F_Y$ implies $X_N>\exp(\lambda D_*Z)$. The squarefree positive divisor expansion and floor count give

$$
 \frac1Y\sum_{Y\le N\le2Y}X_N\le 2\exp\!\left(\sum_p f_v(p)\right),
       \qquad f_v(p)=\log(1-1/p+t_p/p).                            \tag{4}
$$

We now prove the quantitative form of the limiting Euler integral:

$$
                  \sum_p f_v(p)=(\lambda-1)D_*Z+O_{Q,M}(Z/\ell).
                                                                    \tag{5}
$$

Take $\delta=\ell^{-K_0}$ with fixed $K_0>4/\sigma_0$. Since $f_v(p)\le3s p^{-a}$ and $\sum_{p\le x}p^{-a}\ll x^{1-a}/\log x$ uniformly for $a$ in a compact subinterval of $(0,1)$, the contribution from $p<\delta Z$ is $O(Z\delta^{\sigma_0/2})=o(Z/\ell)$. Here $\log(\delta Z)\asymp\ell$ and $sZ^{1-a}/\ell=c_*e^{\lambda u}Z$. At the upper end take a sufficiently large fixed $R>D_*+1$. The local formula for $t_p$ at $p=RZ$ and monotonicity give $3s p^{-a}\le\frac14\log Z$ for $p>RZ$. Then the upper tail in (5) is at most

$$
       O\left(s Z^{1/4}\sum_{n>RZ}n^{-1-a}\right)
                          =O_{Q,M,R}(Z^{1/4}\ell)=o(Z/\ell),
$$

by $(1+3p^{-a})^s-1\le e^{3s p^{-a}}-1\le3s p^{-a}e^{3s p^{-a}}$.

Write $x=p/Z$ and $g(x)=[\lambda(D_*/x)^{a_0}-\lambda]_+$. On the middle range $\delta\le x\le R$, we have

$$
  f_v(p)=\ell g(x)+
             O_{Q,M,K_0,R}\!\left((1+x^{-a_0})(1+|\log x|)\right).
                                                                    \tag{6}
$$

Indeed $3s p^{-a}=\lambda\ell(D_*/x)^{a_0}x^{u/\ell}$ and
$x^{u/\ell}-1=O(|\log x|/\ell)$ there. The quadratic Taylor error in $\log t_p$ is $O(s p^{-2a})=o(1)$ uniformly, since $\delta$ is a fixed negative power of $\ell$ and $v^{1-\lambda}$ decays faster than any such power. Also $\log p=\lambda\ell+\log x$, and replacing $\log(1-1/p+t_p/p)$ by $\log(1+t_p/p)$ costs $O(1/p)$; now apply $\log(1+e^y)=y_++O(1)$. These estimates give (6) with its weight, rather than taking the supremum of $|\log x|$ across the middle range.

The sum of that weight over middle-range primes is $O_{Q,M,R}(Z/\ell)$. For $x\le1$ use the dyads $2^{-j-1}<x\le2^{-j}$: their prime counts are $O(Z2^{-j}/\ell)$, since $\log(\delta Z)\asymp\ell$, and the weighted sum converges by $\sum_{j\ge0}(1+j)2^{-j\sigma_0}<\infty$. For $1\le x\le R$ use the same prime upper bound on a single range. On the leading sum in (6), passing from $\ell g(p/Z)$ to $g(p/Z)\log p/\lambda$ costs at most $\lambda^{-1}\sum_p g(p/Z)|\log(p/Z)|=O(Z/\ell)$ by the same weight. Then apply (3) in partial summation to the latter sum. The total variation and sup norm of $g$ on $[\delta,R]$ are $O(\delta^{-a_0})$; hence replacing the $\vartheta$ integration by ordinary integration costs $O(Z\delta^{-a_0}e^{-b'\sqrt{\ell}})=o(Z/\ell)$, including the possible endpoint terms. Thus the middle leading sum equals

$$
     \frac{Z}{\lambda}\int_\delta^R g(x)\,dx+O(Z/\ell).
$$

Fill the interval $(0,\delta)$ at cost $O(Z\delta^{\sigma_0})=o(Z/\ell)$; the integral vanishes past $D_*$. Its whole value divided by $\lambda$ is $(\lambda-1)D_*$, by direct integration. This proves (5), and (4) with the failure threshold now proves the upper half of (1).

## 2. Quantitative lower bound with the strict divisor test

Use the primorial construction of the leading-constant theorem. Choose

$$
       D=D_*+\frac A\ell,\qquad z=DZ,\qquad
       P_z=\prod_{p\le z}p,\qquad \Delta=\frac v{\ell^3} ,
$$

where the fixed positive constant $A$ will be chosen large. As before all multiples of $P_z$ are even for large $Y$. On the finite divisor set of $P_z$, use probability proportional to $3^{\omega(r)}r^{-(1-\sigma)}$, with normalization $W_z(\sigma)=\prod_{p\le z}(1+3p^{-a})$, $a=1-\sigma$. Its Bernoulli mean for $\log r$ is

$$
          m_z(\sigma)=\sum_{p\le z}\frac{3p^{-a}}{1+3p^{-a}}\log p.
$$

On compact subsets of $0<\sigma<1$, (3) yields uniformly

$$
 m_z(\sigma)=\frac{3z^\sigma}{\sigma}
                    (1+O(e^{-b'\sqrt{\log z}})),\qquad
 \log W_z(\sigma)=\frac{3z^\sigma}{\sigma\log z}
                    (1+O(1/\log z)).                               \tag{7}
$$

For the first bound use partial summation of $\sum p^{-a}\log p$ with (3). For the second the Stieltjes weight for $\sum p^{-a}$ is $t^{-a}/\log t$, and the resulting integral is $z^\sigma/(\sigma\log z)(1+O(1/\log z))$ by integration by parts. In both arguments the portion below $\sqrt z$ is power smaller by the integer power sum, and above it the exponential prime error in (3) is uniform. Replacing $3p^{-a}$ by the exact Bernoulli weight or by $\log(1+3p^{-a})$ costs $O(p^{-2a})$ per prime (including $\log p$ for the mean); split again at $\sqrt z$ and factor out $z^{-a/2}$ above it. This proves (7) with constants uniform in the stated compact range.

Put $u_D=\lambda^{-1}\log(M/(3D^{\sigma_0}))$. For bounded real $w$, at $\sigma=\sigma_0+w/\ell$ the first expression in (7), divided by $v$, is

$$
         3\lambda D^{\sigma_0}e^{\lambda w}(1+O(1/\ell)).
$$

The error here is uniform for bounded $w$ and $D$ in a fixed compact neighborhood of $D_*$. In particular the values at $w=u_D-1$ and $w=u_D+1$ bracket the desired mean $Qv+\Delta/2$ for large $Y$. Since $m_z$ is continuous strictly increasing in $\sigma$, choose the exact tilt with $m_z=Qv+\Delta/2$. On writing $\sigma=\sigma_0+w/\ell$ for that tilt, the displayed equation gives $w=u_D+O(1/\ell)$. Also
$\log W_z=(m_z/\log z)(1+O(1/\ell))=Mv/\ell+O(v/\ell^2)$ by (7). Both error constants may be taken independent of the eventual choice of fixed $A$, using the fixed compact neighborhood of $D_*$.

The variance of $\log r$ is at most $(\log z)m_z=O(v\ell)$ as in the leading-constant construction. Thus the exact tilted divisor probability of $Qv<\log r\le Qv+\Delta$ is $1-O(\ell^7/v)$ by Chebyshev. Every divisor in this band lies strictly above the original threshold. For any multiple $N$ of $P_z$, undoing the tilt on the band gives

$$
 \begin{split}
 \log\mathcal T_N((\log Y)^Q)
    &\ge \log W_z-\sigma(Qv+\Delta)+\log(1-O(\ell^7/v))\\
    &\ge -Mv+(M-Qu_D)\frac v\ell-O_{Q,M}(v/\ell^2).
 \end{split}                                                       \tag{8}
$$

Here $M-Qu_D=(M/\lambda)\log(D/D_*)$, which is at least a fixed positive multiple of $A/\ell$ for all sufficiently large $Y$. Choose $A$ large enough that (8) is strictly greater than $-Mv$. Therefore every such multiple of $P_z$ really fails the test. Lastly $\log P_z=\vartheta(z)=D_*Z+O_{Q,M}(Z/\ell)$ by (3), and there are $Y/P_z+O(1)$ multiples in the dyad with $P_z=\exp(O(Z))=Y^{o(1)}$. This proves the lower half of (1).

## 3. Uniform marking at a shrinking disagreement threshold

Use the same unmarked moment parameters and (5). We make the exact marking of the occupancy theorem with variable scales $\delta=\tau/16$ and $\kappa=k_0\tau$, with $k_0>0$ fixed sufficiently small. Take $\tau_0$ small enough that $\delta\le D_*/4$, and consider $\ell^{-1/2}\le\tau\le\tau_0$ for the moment. Ignore the primes below $\delta Z$ and within $\delta Z$ of $D_*Z$. By (3), their possible log mass is at most $3\delta Z+o(\tau Z)$, uniformly in this range: at the endpoints around $D_*Z$ the error in (3) is $O(Ze^{-b'\sqrt\ell})$, and at $\delta Z$ the same bound suffices since $\log(\delta Z)\asymp\ell$. Thus $J_N(B)\ge\tau Z$ implies its retained part $J'_N\ge\tau Z/2$ for all large $Y$.

On a fixed neighborhood of $p/Z=D_*$, the expansion used in (6) before taking positive parts yields

$$
 \log(t_p/p)=\lambda\ell[(D_* /(p/Z))^{a_0}-1]+O_{Q,M}(1).
$$

At $p/Z=D_*\pm\delta$ its leading signed gap has magnitude at least a fixed positive multiple of $\tau\ell$. The error is negligible uniformly since $\tau\ell\ge\sqrt\ell$. The function $t_p/p$ decreases with the real variable $p>1$. Hence for some $d>0$ depending only on $Q,M$, $t_p/p\ge Z^{d\tau}$ below the lower boundary and $t_p/p\le Z^{-d\tau}$ above the upper boundary. At marked primes $p\le RZ$ we have $p^\kappa\le Z^{2k_0\tau}$ for large $Y$. Choose $k_0$ small enough that $2k_0<d/2$ and $B k_0\tau_0\le1/2$.

At each retained low prime (also with $p\le Z^B$), the multiplier $p^\kappa$ marks the missing case, exactly as in the occupancy theorem: its expansion is $p^\kappa[1+(t_p p^{-\kappa}-1)\mathbf1_{p\mid N}]$. The internal coefficient is nonnegative by the just established gap. At a retained high prime $p\le Z^B$ the multiplier marks the occupied case, and its coefficient is plainly nonnegative. Positive divisor expansion and the ordinary floor count therefore give the same exact upper moment factors for $X_N e^{\kappa J'_N}$: $p^\kappa(1-1/p)+t_p/p$ at marked lows and $1-1/p+t_pp^\kappa/p$ at marked highs. Unmarked factors do not change. There is no independence assumption over integers.

By the gap estimates each log increment at marked $p\le RZ$ is at most $Z^{-d\tau/2}$, uniformly. This contributes $O(Z e^{-b''\tau\ell})=o(Z/\ell)$. At marked $RZ<p\le Z^B$ use $t_p\le Z^{1/4}$ as in Section 1; the total log increment is at most

$$
 Z^{1/4}\sum_{n\le Z^B}n^{\kappa-1}
       \le Z^{1/4+B\kappa}(1+B\log Z)
                         =O_B(Z^{3/4}\log Z)=o(Z/\ell).
$$

This avoids a constant growing as $1/\kappa$ when $\tau$ shrinks. The log of the marked upper moment is consequently at most $(\lambda-1)D_*Z+O_{Q,M,B}(Z/\ell)$, using (5).

A failing target with $J_N(B)\ge\tau Z$ contributes more than $\exp((\lambda D_*+k_0\tau^2/2)Z)$ to this moment. Markov and the lower count in (1) now give the conditional fraction

$$
                       \le \exp(-k_0\tau^2 Z/2+C_1Z/\ell)
$$

with $C_1$ independent of $\tau$ in the displayed range. Choose $K\ge1$ with $C_1/K^2\le k_0/4$. This proves (2) with $c=k_0/4$ uniformly for $K/\sqrt\ell\le\tau\le\tau_0$. Only the scalar positive omission test was used as the failure condition throughout.
