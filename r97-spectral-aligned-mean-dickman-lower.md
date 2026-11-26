# The aligned exceptional parity mean has a fixed sign at every fixed cutoff

**Scope.** This removes the low-cut restriction from Theorem 2 of [the complete aligned signed-mean formula](r96-spectral-aligned-mean-euler-collapse.md). The quantity is the **actual exceptional correction** in a signed dyadic mean over an entire, untrimmed full-primorial divisibility family. The statement is conditional on a sufficiently close, aligned Page zero. It proves neither the existence of such a zero nor a pointwise sign on aligned targets. It does not assert positivity of the whole mixed-strip coefficient, a prime-pair count, or Hypothesis S. No Dirichlet GRH or imported zero-gap assertion is used.

Use the setting of the complete aligned signed-mean formula. In particular, let $G=\log Y$, $Z=\sqrt G/\log G$, and let an actual primitive real Page character $\chi$ of conductor $r$ have its simple zero $\beta>1-4a_0/\sqrt G$. Take the fixed dyadic full primorial $K=K_z=\prod_{p\le z}p$ with $r\mid K_z$, $G^\epsilon\le z\le Z$, and $K_z\le e^{2Z}$, for fixed $0<\epsilon<1/2$. Write $\ell=\log z$ and assume the same quantitative closeness condition $(1-\beta)G\le C_*\log G$, with $C_*$ fixed. Fix any admissible $B>B_0>0$, as in the aligned formula. The original real cutoffs are $D_v=\sqrt v(\log v)^{-B}$ and $H_{0,v}=\sqrt v(\log v)^{-B_0}$ for $Y\le v\le2Y$, with $U_v=\log(H_{0,v}/D_v)$ and $T_{v,x}=\log(x/D_v^2)$ at $v-x\in vJ$. Here $J\subset(1/2,9/16]$ is the same fixed half-open interval. Retain the original common left test $w((v-x)/v)$ and dyadic test $\eta(v/Y)$, both fixed, nonnegative, bounded and of bounded variation, with positive integrals $\int_Jw$ and $\int_1^2\eta$. Angle brackets denote the same normalized signed mean $(K_z/Y)\sum_{Y\le N\le2Y,\ K_z\mid N}\eta(N/Y)(\cdot)$.

**Theorem.** For every such fixed cutoff pair $B>B_0>0$, without assuming $U_v\le\ell$, one still has on all sufficiently large dyads satisfying the stated hypotheses

$$
 -\chi(-1)\langle\mathfrak E_+-\mathfrak E_-\rangle_{K_z}
 \ \gg\
      \left(\int_J w\right)\left(\int_1^2\eta\right)
      \frac{Y^{2\beta-1}}{G}
      \frac{K_z}{\varphi(K_z)(\log r)^4}.
 \tag{1}
$$

The constants may depend on the fixed tests, $\epsilon,C_*,B,B_0$ and the fixed Page threshold. The indices $+$ and $-$ are the original even and odd squarefree factor-count sectors. The correction continues to be the one defined using the original finite Ramanujan range, not a newly uncapped object.

## 1. An all-minus rough comparator on every bounded log scale

Recall the completed signed coefficient $\alpha=\alpha^{K_z}$ of the aligned mean. It is squarefree multiplicative, vanishes on every prime $p\le z$, and on $p>z$ it is
$\alpha_p=c_p/(1-2c_p)$ with $c_p=\chi(p)p^{-\beta}$. All primes here are outside the conductor because $r\mid K_z$. Write $a_p=|\alpha_p|$, and put $b=1-\beta$. For each fixed $H>1$ one has $bH\ell=o(1)$ uniformly on the stated dyads. For large $Y$ and $p>z$, $a_p\ll p^{-\beta}$ and $a_p<1/2$. In the range $z<p\le z^H$,

$$
 \sum_{z<p\le z^H}|a_p-p^{-1}|
   \ll_H z^{1-2\beta}+b\ell e^{Hb\ell}
   =o(1).
 \tag{2}
$$

Indeed $|a_p-p^{-\beta}|\ll p^{-2\beta}$ uniformly for either sign, and $p^{-\beta}-p^{-1}\le b e^{Hb\ell}(\log p)/p$. The sum of $p^{-2\beta}$ is bounded by the corresponding integer tail, since $\beta\ge.99$ for large $Y$.

For completeness the required reciprocal-prime estimates follow from the elementary bound $\sum_{n\le x}\Lambda(n)\ll x$. Insert $\sum_{d\mid n}\Lambda(d)=\log n$ in $\sum_{n\le x}\log n$, replace $\lfloor x/d\rfloor$ by $x/d$, and use Stirling's estimate; this gives $\sum_{d\le x}\Lambda(d)/d=\log x+O(1)$. The proper prime powers contribute $O(1)$. Partial summation therefore gives, uniformly for $1\le t\le H$,
$\sum_{z<p\le z^t}p^{-1}=\log t+O_H(\ell^{-1})$.
In particular $\sum_{p\le z}p^{-1}=\log\log z+O(1)$. These estimates are elementary and do not use distribution of $\chi(p)$.

Let $F_z(u)$ be zero for $u<0$ and be the primitive formed by giving **every** prime $p>z$ the squarefree coefficient $-a_p$:

$$
 F_z(u)=
 \sum_{\substack{n\le e^u,\ n\ {\rm sf}\\p\mid n\ \Rightarrow\ p>z}}
                      \prod_{p\mid n}(-a_p)
 \qquad (u\ge0).
 \tag{3}
$$

The term at $n=1$ is one. On $0\le u\le H\ell$ only primes $p\le z^H$ and at most $\lfloor H\rfloor$ distinct prime factors can enter. For $t\in[0,H]$ put $I_0(t)=1$ and
$I_k(t)=\int_{v_i\ge1,\ \sum_{i=1}^k v_i\le t}\prod_i(dv_i/v_i)$ for $k\ge1$. The cumulative masses of $\sum_{z<p\le z^H}a_p\delta_{\log p/\ell}$ differ uniformly from those of $\mathbf1_{[1,H]}(v)\,dv/v$ by $O_H(d_z)$, where $d_z=\ell^{-1}+z^{1-2\beta}+b\ell e^{Hb\ell}=o(1)$. The same discrepancy bound holds on all real endpoints, extending the two cumulative functions by zero and their total masses at the respective ends.

The total masses of these positive measures are $O_H(1)$. At any fixed $k\ge1$, telescoping the $k$ convolution factors gives a cumulative discrepancy $O_H(d_z)$: the cumulative of a signed difference integrated against any of the remaining positive convolutions is bounded by its uniform discrepancy times the positive total masses. Deleting repeated primes from the discrete $k$-fold convolution costs at most $\binom{k}{2}(\sum a_p^2)(\sum a_p)^{k-2}=O_H(z^{1-2\beta})$ for $k\ge2$, by prescribing two positions with the same prime. Dividing the remaining ordered tuples by $k!$ is exact. Hence

$$
 F_z(t\ell)=\rho(t)+O_H(d_z)
 \quad(0\le t\le H),
 \qquad
 \rho(t)=\sum_{k\ge0}\frac{(-1)^k}{k!}I_k(t).
 \tag{4}
$$

Here the series for $\rho$ is finite locally in $t$. The estimates cover discrete endpoints as stated; no continuity of $F_z$ is needed.

This is the ordinary Dickman function in its cumulative normalization. To verify the only property needed, take $I_k(t)=0$ for $t<k$ when $k\ge1$. For $t>1$ off the integer breakpoints, differentiation at the simplex boundary and its symmetry give $t I_k'(t)=k I_{k-1}(t-1)$. For $k\ge2$, on the sum boundary replace the factor $t$ by the sum of the $k$ variables. They contribute equally under the boundary integration written in the first $k-1$ coordinates; the last variable cancels its reciprocal factor, leaving $I_{k-1}(t-1)$. The $k=1$ formula is direct. Thus $\rho=1$ on $[0,1]$, is continuous, and $t\rho'(t)=-\rho(t-1)$ off the breakpoints. Integrating this identity from $1$ gives $t\rho(t)=\int_{t-1}^t\rho(s)\,ds$ for $t\ge1$. A first zero would have a strictly positive right hand side, so $\min_{[0,H]}\rho>0$. This proof supplies positivity without a prime-sign distribution hypothesis.

For the actual primitive $R_1(u)=\sum_{n\le e^u}\alpha(n)$, use the exact coefficient identity at each of the finitely many primes $z<p\le z^H$:

$$
 1+\alpha_p X=(1-a_p X)\frac{1+\alpha_p X}{1-a_p X}.
 \tag{5}
$$

The quotient is one when $\alpha_p=-a_p$, and otherwise is $1+2\sum_{k\ge1}a_p^kX^k$. With $X$ encoding a shift by $\log p$, these quotient factors have nonnegative masses, including mass one at zero. Up to $H\ell$ they convolve $F_z$ into $R_1$ exactly, as can also be checked by finite coefficient multiplication at each reachable integer. This is only a finite-prime identity on the stated interval, not an assertion of global positive convergence of the quotient. For any shift reaching $[0,H\ell]$, the remaining argument of $F_z$ is either negative, where it is zero, or lies in the same interval, where (4) gives a positive lower bound. The zero shift alone guarantees the lower bound. The upper bound follows from $\prod_{z<p\le z^H}(1+a_p)\ll_H1$. For constants $c_H,C_H>0$ and large $Y$ we obtain

$$
                   c_H\le R_1(u)\le C_H
                         \qquad(0\le u\le H\ell).
 \tag{6}
$$

No corresponding sign outside a fixed bounded multiple of $\ell$ is used.

## 2. The genuine finite cap remains positive

Write $C_K,Q_K,J_K,M_K$ for exactly the aligned mean definitions (2)--(3), and $R_j$ for their primitive with $(n,j)=1$. For squarefree $j$ of nonzero weight, removing its local factors gives $R_j=R_1*\nu_j$, where $\nu_j$ is a signed measure supported on nonnegative shifts, of total variation at most $V_j=\prod_{p\mid j}(1-a_p)^{-1}$. This follows by multiplying the inverse factors $(1+\alpha_p X)^{-1}$ and including the same finite set of primes $p\mid j$. The aggregated nonunit common-divisor weight satisfies

$$
 \delta_z=\sum_{\substack{j>1\\j\ {\rm sf}}}|\alpha(j)|^2 V_j^2
        =\prod_{p>z}\left(1+\frac{a_p^2}{(1-a_p)^2}\right)-1
        \ll z^{1-2\beta}=o(1).
 \tag{7}
$$

Terms where $\alpha(j)=0$ are omitted here and below. The primitive $R_1$ is in $L^2$ by the aligned formula. Globally $\|R_j\|_2\le V_j\|R_1\|_2$, and for $0\le u\le H\ell$ the same convolution and (6) give $|R_j(u)|\le V_j C_H$. These estimates use support on nonnegative shifts, with $R_1=0$ on negative arguments.

Since $U_v=(B-B_0)\log\log v$ and $\ell\ge\epsilon\log G$, choose a fixed $H>2+2(B-B_0)/\epsilon$. Then $0\le U_v\le (H-1)\ell$ for large $Y$, throughout the dyad. For every $U$ in this interval put $E_{>}(U)=\int_U^\infty R_1(u)^2\,du$ and $E_{<}(U)=\int_0^U R_1(u)^2\,du$. Inequality (6) gives $E_{>}(U)\ge c_H^2\ell$ from $[U,U+\ell]$, and $E_{<}(U)\le C_H^2 H\ell$. For each $j$, the difference between its full squared norm in $C_K(0)$ and the portion in $Q_K(U)$ is nonnegative before multiplication by its signed coefficient. When $j>e^U$ the latter portion is zero, as in the exact formula. Its absolute contribution is at most $|\alpha(j)|^2 V_j^2\|R_1\|_2^2$. The $j=1$ term is precisely $E_{>}(U)$. Consequently

$$
 \frac{C_K(0)-Q_K(U)}{M_K}
     \ge (1-\delta_z)E_{>}(U)-\delta_z E_{<}(U)
     \gg_H \ell.
 \tag{8}
$$

The calculation does not replace the total global norm by a fixed-window model; a large global tail only strengthens this bound.

Similarly the $j=1$ term of $J_K(U)/M_K$ is at least $c_H^2U^2$. Every $j>1$ in its actual finite range has $0\le U-\log j\le U$, and $|\int_0^{U-\log j}R_j|\le V_j C_H U$. The full absolute bound on their contribution gives

$$
                \frac{J_K(U)}{M_K}
                 \ge (c_H^2-C_H^2\delta_z)U^2\ge0 .
 \tag{9}
$$

These formulas also cover a coincident endpoint $U=\log j$, whose corresponding integral is zero. On the original real support $v-x\in vJ$ one has $x\asymp Y$ and $T_{v,x}=2B\log\log v+O(1)\asymp\ell$. With (8)--(9), the true color-one coefficient (4) of the aligned mean therefore obeys

$$
 \mathcal A_1(v,x)
   =T_{v,x}\{C_K(0)-Q_K(U_v)\}+J_K(U_v)
   \gg M_K\ell^2.
 \tag{10}
$$

In particular neither of the actual cutoff-dependent finite terms has been replaced by an infinite one.

## 3. Quantitative size of the actual signed parity difference

The normalization estimate in Section 4 of the aligned mean proof does not use $U_v\le\ell$. Explicitly the $p>z$ factor in $P_K$ is $1+O(z^{1-2\beta})$, and at the primes of $K_z$ the factors $p/(p-1)$ together with $r/\varphi(r)$ give exactly $K_z/\varphi(K_z)$. The remaining Euler factors obey $\prod_{p\mid K_z,\ p\nmid r}(1-c_p)^{-2}\ge\exp(-2\sum_{p\le z}p^{-\beta})\gg\ell^{-2}$, using the reciprocal estimates above and $b\ell=o(1)$. The same primary near-exception bound used in the aligned formula, [Montgomery--Vaughan, Chapter 11, (11.10)](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF), gives $|L'(\beta,\chi)|\ll(\log r)^2$. Altogether $M_K\ell^2\gg K_z/(\varphi(K_z)(\log r)^4)$.

Subtract the two exact mean formulas (5) of the aligned mean proof. The other color cancels, and the remaining signed factor is $-\chi(-1)$, not $-\chi(-1)/2$. The correction is real for these inputs as in that proof. On the support $x,v-x\asymp Y$, $\log x\asymp G$; substituting $s=(v-x)/v$ and $v/Y$ in the nonnegative test integrals gives the product of integrals in (1), at physical scale $Y^{2\beta-1}/G$. Apply (10) and the lower bound for $M_K\ell^2$. The original error $O_A(Y^\beta G^{-A})$ is negligible by choosing a sufficiently large fixed $A$: $Y^{2\beta-1}\ge YG^{-2C_*}$, $\log r\le 2Z$, and $K_z/\varphi(K_z)\ge1$. This proves (1) for the original correction, with the original tests and moving finite caps. In particular the statement is a signed-mean result only; it does not bound either the magnitude or sign of that correction at individual $N$.
