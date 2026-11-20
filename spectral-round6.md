# Round 6: eliminate the exact zero prefix in the top-eigenvalue problem

**Status.** Under the paper's local GRH(N) realization, this note improves the uniform left tail, gives an exact Schur criterion for the top spectral threshold, and reduces the low-to-high arithmetic coupling to a finite Gram matrix of signed progression profiles. It does not bound the remaining high-to-high block or signed progression profiles at the S scale. No fixed-modulus upper certificate is claimed or rerun.

Let $T_N$ be the [Li–Liu operator](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf) in the complete physical unitary coordinates of [source-round2.md](source-round2.md). Thus physical scales $x,y$ are normalized by $N$, $\alpha=1/\log N$, $\beta=1/8$, and $w(x)^{-1}=(Nx)^{-2\alpha}+(Nx)^{-2\beta}$. The kernel is the double cumulative signed arithmetic-minus-model measure with weight $\sqrt{uv}$, multiplied by $2\pi/[x^{3/2}y^{3/2}\sqrt{w(x)w(y)}]$. The two separate off-diagonal forms also have their own cumulative kernels; this follows from their compact smooth test identities, extended by the same density argument. Use $S=\mathfrak S(N)$.

## 1. A stronger actual low tail

Let $P_a$ project to $0<x<a$ and $Q_Y$ to $y>Y$, where $0<a\le1/2$ and $Y\ge1/2$. The continuous beta term (before its subtraction) satisfies
$$
 \|Q_Y\mathcal K_{N,\mathrm{model}}P_a\|_{HS}
 \ll \frac{S a\big(1+(Na)^{-\beta}\big)}{\sqrt Y}. \tag{1}
$$
All constants are absolute. This uses both the signs of the model and the thin support of its unmatched boundary terms, not just a contour tail. For $x\le a$, its unweighted cumulative mass against $y$ is
$$
 \sum_{k\ge1}S_k\int_0^x \sqrt u\,
 \left(\sqrt{k+u}\,\mathbf1_{k+u\le y}
       -\sqrt{k-u}\,\mathbf1_{k-u\le y}\right)du,
 \qquad S_k=\mathfrak S(kN).
$$
The other positive difference $y=u-k$ is impossible. When both partners have fully entered ($k+x\le y$), the two roots differ by $O(u/\sqrt k)$. The complete terms therefore have total size $O(Sx^{5/2}\sqrt y)$, using $\sum_{k\le y}S_k/\sqrt k\ll S\sqrt y$. The remaining terms occur only in $|y-k|<x$; there is at most one such $k$ almost everywhere because $x\le1/2$. Their total size is $O(S_k\sqrt k\, x^{3/2})$ on that interval. The model is identically zero for $y<1-x$, so on any nonzero part $y\ge1/2$ and $w(y)^{-1}\le2$.

For completeness, the divisor expansion $S_k/S=\sum_{d\mid k} a_d$, with $a_d$ multiplicative on square-free $d$, $a_p=(p-2)^{-1}$ for $p>2,p\nmid N$ and $a_p=0$ otherwise, gives $\sum_{k\le t}S_k\ll St$ and
$$
 \sum_{k\le t}S_k^2\le S^2t\sum_{d,e\ge1}\frac{a_da_e}{[d,e]}\ll S^2t.
$$
The latter Euler product has factors $1+2a_p/p+a_p^2/p$, so is bounded by an absolute convergent product. Partial summation gives the square-sum tail $\sum_{k\ge \max(1,Y-1/2)}S_k^2/k^2\ll S^2/Y$. After applying the physical kernel multipliers, the complete terms have squared integral in $y>Y$ at most $O(S^2 x^2/(Yw(x)))$. The unmatched terms have squared integral at most $O(S^2 x/(Yw(x)))$, because their intervals have lengths $2x$. Integrate in $x$ using
$$
 \int_0^a\frac{x}{w(x)}dx\ll a^2(1+(Na)^{-2\beta}).
$$
This proves (1).

At $a=1/N$ there is no actual arithmetic atom in the prefix: $n=1$ has $\Lambda(1)=0$, and all the arithmetic cumulative diagonal and off-diagonal row terms vanish there. Also $P_aT_NP_a=0$. Thus (1) gives the complete-operator bound
$$
 \|T_N-(I-P_{1/N})T_N(I-P_{1/N})\|\ll S/N. \tag{2}
$$
In fact, the discarded operator is purely off-diagonal, with norm exactly the norm of its one discarded cross block. For comparison, the negative-log-sector result of Round 2 gave $O(SN^{-3/4})$. Equation (2) is at a scale $o(\delta_N)$ but discards only raw additive sizes below 1.

The scale of (2) is sharp for that sector. On the rectangle $a/2<x<a$, $1-a/4<y<1-a/8$, only the negative sum model at $k=1$ contributes, and its integral over $a/4<u<a/2$ has magnitude $\gg S a^{3/2}$. For $1/N\le a\le1/2$, both $w(x),w(y)$ are bounded above, and hence the physical kernel has one sign and magnitude $\gg S$ on this rectangle. The pairing of its two $L^2$-normalized indicator boxes is $\gg Sa$. If $Na$ is at most the smallest prime $p_0$ not dividing $N$, there are no unit prime-power atoms in the open low prefix. In that case the actually discarded norm is $\asymp Sa$, not just an upper bound for the model. Taking $a=1/N$ proves sharpness of (2); taking $a=p_0/N$ when $p_0/N\le1/2$ extends the exact removable sector for moduli divisible by many small primes. These estimates do not give a comparable lower bound for the cross at $a>p_0/N$, where actual arithmetic may cancel the model.


## 2. Exact top-mode Schur complement and mass constraint

For every $a\le1/2$ the entire low-low block vanishes: $u,v$ in $0<u,v<a$ do not meet a nonzero difference or sum line. The kernel statement includes all physical interface vectors. Let $B=(I-P_a)T_NP_a$ and $C=(I-P_a)T_N(I-P_a)$, with $C$ considered on the high subspace. Exactly
$$
 T_N=\begin{pmatrix}0&B^*\\B&C\end{pmatrix}.
$$
For a threshold $t>0$,
$$
 \|T_N\|\le t
 \quad\Longleftrightarrow\quad
 tI+C-t^{-1}BB^*\succeq0\ \text{and}\ tI-C-t^{-1}BB^*\succeq0. \tag{3}
$$
This is obtained by completing the square in the low variable of each positive form $tI\pm T_N$. It handles the threshold coefficient exactly, unlike a norm comparison only up to constants. An eigenvector $(u,v)$ with nonzero eigenvalue $\mu$ has $u=B^*v/\mu$ and
$$
 (C+\mu^{-1}BB^*)v=\mu v.
$$
In particular any top-modulus eigenvector has at most half of its mass in the zero prefix, since $\|T_N\|\ge\|B\|$; quantitatively its low mass share is at most $\|B\|^2/(\mu^2+\|B\|^2)$. It cannot be a pure low-prefix mode. For coarse norm budgets, $b=\|B\|$ and $c=\|C\|$ give
$$
 \max(b,c)\le\|T_N\|\le\frac{c+\sqrt{c^2+4b^2}}{2}
$$
by the scalar $2\times2$ comparison on the norms of the components.

In particular one can spend a margin on the cross **quadratically**: if $\|C\|\le(1-\varepsilon)t$ and $\|B\|\le\sqrt{\varepsilon}\,t$, (3) certifies $\|T_N\|\le t$. A direct triangle split would ask for $\|B\|\le\varepsilon t$. If $t>\|C\|$, eliminating the high block instead gives the equivalent finite-rank-friendly tests $B^*(tI\pm C)^{-1}B\preceq tI$ on the low subspace.


## 3. Finite rank of the low-to-high arithmetic coupling

Fix $M=Na\ge1$ with $a\le1/2$. For each unit prime power $n<Na$ put
$$
 \ell_n(x)=\frac{\mathbf1_{n/N\le x<a}}{x^{3/2}\sqrt{w(x)}},\qquad
 r_n(y)=\frac{\mathbf1_{y>a}}{y^{3/2}\sqrt{w(y)}}F_n(y),
$$
where the signed weighted progression discrepancy is
$$
 F_n(y)=\sum_{k\ge1}\left[
 \Lambda(kN+n)\sqrt{k+n/N}\,\mathbf1_{k+n/N\le y}
 -\Lambda(kN-n)\sqrt{k-n/N}\,\mathbf1_{k-n/N\le y}
 \right].
$$
The arithmetic part of $B$ is exactly
$$
 B_{\mathrm{arith}}
 =\frac{2\pi}{N}\sum_{n<Na,(n,N)=1}\Lambda(n)\sqrt{n/N}\, r_n\otimes\ell_n. \tag{4}
$$
The exact diagonal is already subtracted, and all partners here are automatically units. The operator's rank is at most the number of unit prime powers below $M$, $O(M/\log(2M))$. The model part subtracted in $B$ has norm $O(Sa)$ by (1). Therefore whenever $a=o(1/h(N))$ with $Na\ge1$, controlling this cross at $o(S/h)$ is equivalent to controlling the **signed progression Gram** at that rate, not its absolute positive residue counts.

On any bounded high window $a<y<Y$, the Gram matrix of the right vectors in (4) is a finite sum of integrals of the weight $y^{-3}(1/w(y))$ times constant products, broken at the prime-power locations. The left Gram matrix is exactly given by the same weight integrated from $\max(n,m)/N$ to $a$. The antiderivatives are elementary sums of two powers, and numerical enclosures may use outward rounding. If $G_\ell$ is the left Gram and $G_r$ the right Gram (with the coefficients of (4) absorbed into the right vectors), then the square of the cross norm equals the largest eigenvalue of $G_\ell^{1/2}G_rG_\ell^{1/2}$. This includes interactions between all low directions, with no need to assume orthogonality of the nested $\ell_n$.

This is not yet a practical global certificate from raw prime-power enumeration. Local GRH gives, by odd-character orthogonality, the signed progression partial-sum bound $O_N(\sqrt s(1+\log s)^2)$ through raw size $s$; the principal terms cancel. Partial summation yields $|F_n(y)|=O_N(\sqrt N,y(1+\log(Ny))^2)$ for $y\ge1$, including the subtracted $m=n$ term. Thus the tails of the right-vector squared norms can be bounded by a constant times
$$
 N\int_Y^\infty (1+\log(Ny))^4 y^{-1-2\alpha}\,dy.
$$
This is effective at each fixed modulus and proves that the profiles are genuine $L^2$ vectors. But it only decays as $Y^{-2/\log N}$ times a polynomial in $\log Y$, unlike the continuous-model tail (1). For instance, at $Y=N^c$ with fixed $c$, even the bare norm damping $Y^{-1/\log N}=e^{-c}$ supplies no inverse-log accuracy. Direct evaluation of the sufficient cutoff entails a superpolynomial raw prime range for inverse-log damping, before constants and polynomial losses are counted. This is a bottleneck of this bound and literal enumeration, not a lower bound on the complexity of every algorithm.

**Remaining test.** Use (3) if the signed progression Gram and the high block admit sharper bounds. Neither the $O(S/N)$ tail, finite arithmetic rank in (4), nor the top-mode mass constraint controls the two outstanding forms in (3). No claim about the eventual S or R bound follows.
