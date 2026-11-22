# Low-denominator rational component of the exterior alias variance

**Scope.** This bounds a genuine orthogonal component of the modulus-wise $L^2$ error of the actual exterior mean-difference matrices, simultaneously at all reduced rational frequencies of bounded denominator. It does not bound the complement, the full variance, or any individual modulus.

Put $L=\log Q,\ \ell=\log L$. Fix $K>0,\ C>1,\ 0<\delta<1/2$, and $\gamma,\xi\ge0$ satisfying $\xi+3\gamma/2<\delta$. Let $\mathcal I\subset[Q,2Q]$ be any interval of length $\Delta\ge Q^{1/2+\delta}$. Take the [common physical grid](r43-operator-signed-modulus-window.md) $V=2^jY$ and every whole dyad in $[Y,M]$, with

$$
 Y=e^H,\quad H\ge 2(K+3)\ell^2/\log\ell,\qquad M=e^{CH}\le Q^\gamma.
$$

Assume original local Dirichlet GRH at each even $N\in\mathcal I$, and auxiliary Dirichlet GRH for all moduli up to $8BM+2$, where $B$ is an integer $1\le B\le Q^\xi$. In particular global Dirichlet GRH suffices.

Let $E_N$ map the fixed dyad-index basis to the [true normalized weighted mean differences](r40-operator-negative-difference-subspace.md) at $N$. Put $\mathcal J=\{n\in\mathbb Z:2n\in\mathcal I\}$ with uniform probability, and $X(n)=E_{2n}^*T_{2n}E_{2n}$. In $L^2(\mathcal J)$ let $\mathcal R_B$ be the span of the distinct phases $e^{2\pi i an/r}$, $1\le r\le B,\ 0\le a<r,\ (a,r)=1$, including the constant for $r=1$. Denote by $\Pi_B$ its orthogonal projection, also applied to matrix-valued functions. Then for each sufficiently small fixed $\epsilon>0$,

$$
 \|\Pi_B X\|_{L^2(\mathcal J;\mathrm{HS})}
 \ll_\epsilon BQ^{1/2+\epsilon}M^{3/2}/\Delta
                  + L^{5/2}Y^{-1/5}
 =o(L^{-K}).
 \tag{1}
$$

For R43 fixed-endpoint tests the second error is absent. The projection of the centered error onto $\mathcal R_B\ominus\mathbb C$ is bounded by the same quantity. The [log-separation mask](r31-operator-zero-diagonal.md) is one on all supports since their log diameter is at most $\log M\le\gamma L$. On the [mean-difference benchmark strip](r41-operator-mean-difference-benchmark.md) the projected discrepancy is the signed prime-power alias matrix minus its actual benchmark, not the artificial long-divisor integer diagonal.

## 1. The arithmetic class-vector error

Use R43 fixed-endpoint tests and temporarily discard proper prime powers, incurring its uniform $O(Q^{-1/2}ML^3)$ error per entry; the model is unchanged. Write $\lambda=\log p$ at primes and zero otherwise. For one entry with dyads $V\le U$, and each signed orientation $y=x+kt,\ y=x-kt,\ y=kt-x$, the exact switched pair weight is the R43 weight

$$
 W_t(x,y)=\frac{b_{t,V}(x/(tV))b_{t,U}(y/(tU))}{t\sqrt{VU}}.
$$

After switching to $t=(y-x)/k,\ (x-y)/k$, or $(y+x)/k$, multiply this by ${\bf1}_{t\in\mathcal I}$ and call it $W(x,y)$. As proved in R43, each single-coordinate total variation and supremum is $O(1/(Q\sqrt{VU}))$, with supports $QV\le x\le4QV,\ QU\le y\le4QU$, and $k\le4U$. The weight is independent of the residue class chosen below. Transposing the legs merely interchanges difference orientations. Ordinary primes here are larger than $N$, so the original unit restriction is automatic.

Fix $r\le B$, $D=2r$, and even residues $\nu=2j,\ j=0,\ldots,r-1$. Summing over $N\equiv\nu\pmod D$ switches, for each orientation, to $y\equiv\pm x\pm k\nu\pmod q$, $q=kD$. For each $x$ these are $r$ distinct residues as $j$ varies. Both prime coordinates exceed $q$ for large $Q$, since $q\le 8BM$ and $\xi+\gamma<1$. Hence nonunit $y$-classes contribute exactly zero.

On the units of $q$ let

$$
 I_a(s)=\sum_{\substack{y\le s\\y\equiv a\ (q)}}\lambda(y)-s/\phi(q)
$$

and extend by zero to nonunit classes. The GRH character PNT at $q$ gives, uniformly over all characters and $1\le s\le4QU$,
$\sum_{m\le s}\lambda(m)\chi(m)={\bf1}_{\chi=\chi_0}s+O(\sqrt{QU}L^2)$.
This follows from the usual $\Lambda$ version by discarding proper powers. Orthogonality, including the principal error, therefore gives

$$
 \sum_{a\bmod q}|I_a(s)|^2
 =\phi(q)^{-1}\sum_{\chi\bmod q}
  \left|\sum_{m\le s}\lambda(m)\chi(m)-{\bf1}_{\chi=\chi_0}s\right|^2
 \ll QU L^4 .
 \tag{2}
$$

For fixed prime $x$, select the injective subset of switched residues. Vector-valued Abel summation with the *same* weight $W(x,y)$ for all residues, and its variation bound, gives an $\ell^2$ replacement error $O(\sqrt{QU}L^2/(Q\sqrt{VU}))$ at this $x$. Minkowski and the prime mass $O(QV)$ on the short leg give $O(\sqrt{QV}L^2)$ for the fixed $k$ in class-vector norm. In particular there is no $\sqrt r$ penalty in this first replacement.

The main term left for class $\nu$ is

$$
 \frac1{\phi(q)}\sum_x\lambda(x){\bf1}_{(\pm x\pm k\nu,q)=1}
                                 \int W(x,y)\,dy.
$$

For each prime $p\mid q$ dividing $k\nu$, the $x$-unit condition already guarantees the displayed condition. At each other $p\mid q$, exclude one unit residue by inclusion–exclusion over squarefree $d\mid q,\ (d,k\nu)=1$. All those progressions are inside the auxiliary GRH range. The $x$-variation of the integrated weight is $O(\sqrt{U/V})$ by the one-coordinate bound integrated over $y$. The second prime replacement therefore incurs $O(\sqrt{QU}L^2\tau(q)/\phi(q))$ for each class and gives the density

$$
 u_{\nu,k}=\prod_{p\mid q,\ p\nmid k\nu}\left(1-\frac1{p-1}\right).
$$

Its cost over the whole class vector is $O_\epsilon(\sqrt{QU}Q^\epsilon)$, using $\sqrt r\,\tau(q)/\phi(q)\ll_\epsilon Q^\epsilon$, since $q\ge r$ and $q\le 8BM$. Sum both replacement costs over $k\le4U$ to obtain $O_\epsilon(Q^{1/2+\epsilon}M^{3/2})$. Changing $y$ to $t$ in the main integral gives an absolute Jacobian $k$ and the main term

$$
 \frac{k u_{\nu,k}}{\phi(q)}\int_{\mathcal I} I_k(t)\,dt,\qquad
 I_k(t)=\int W_t(x,y(x,t))\,dx .
 \tag{3}
$$

The $O(1)$ variation and supremum bounds of $I_k$ are those of R43.

## 2. The same class model has exactly the same density

For $N\equiv\nu\pmod D$, with $C_2=\prod_{p>2}(1-(p-1)^{-2})$, the singular series is

$$
 \mathfrak S(kN)
 =2C_2\prod_{\substack{p>2,\ p\mid q\\p\mid k\nu}}\frac{p-1}{p-2}
 \sum_{\substack{d\mid N,\ d\text{ odd squarefree}\\(d,q)=1}}
            a(d),\qquad a(d)=\prod_{p\mid d}(p-2)^{-1}.
$$

At primes of $q=kD$, membership in $kN$ is fixed by $k\nu$; the other odd primes are expanded as shown. Since $(d,D)=1$, the joint progression has density $1/(Dd)$ with $O(1)$ discrepancy against $I_k$ on any $\mathcal I$. As in R43, $a(d)\ll_\epsilon d^{-1+\epsilon}$, the fixed prime factor is $O_\epsilon(Q^\epsilon)$ after adjusting exponents, and truncating the main $a(d)/d$-sum at $2Q$ costs $O_\epsilon(Q^\epsilon)$ after integration. The total error per $k,\nu$ is $O_\epsilon(Q^\epsilon)$. Exactly, the main coefficient equals

$$
 \frac{2C_2}{D}
  \prod_{\substack{p>2,\ p\mid q\\p\mid k\nu}}\frac{p-1}{p-2}
  \prod_{\substack{p>2\\p\nmid q}}\left(1+\frac1{p(p-2)}\right)
 =\frac1D\prod_{p\mid q}\frac{p}{p-1}
   \prod_{\substack{p\mid q\\p\nmid k\nu}}\frac{p-2}{p-1}
 =\frac{k u_{\nu,k}}{\phi(q)} .
 \tag{4}
$$

At two use $2\mid k\nu$; at odd primes not dividing $q$ the expanded local factors cancel $C_2$. Thus each orientation separately cancels (3) before its sign is imposed. The model error for all aliases in class-vector norm is $O_\epsilon(M\sqrt r\,Q^\epsilon)$, absorbed in $O_\epsilon(Q^{1/2+\epsilon}M^{3/2})$ as $r\le B\le Q^\xi$, $\xi<1/2$.

## 3. Projection over all reduced phases

Let $\widetilde X$ be the fixed-endpoint, ordinary-prime-only matrix discrepancy. For each $r$, its raw class sums have $\ell^2$ norm $O_\epsilon(Q^{1/2+\epsilon}M^{3/2})$ per entry by §§1–2. Taking matrix HS costs at most the dimension $O(L)$, absorbed in $\epsilon$. Write $\Pi_r^{\rm per}$ for conditional expectation given $n\bmod r$, and $\mathcal J_j$ for these classes in $\mathcal J$. The counts are $|\mathcal J|/r+O(1)\asymp\Delta/r$, and the contribution of the squared class sum is divided by $|\mathcal J|\,|\mathcal J_j|$ in the normalized projected square norm. Hence

$$
 \|\Pi_r^{\rm per}\widetilde X\|_{L^2(\mathrm{HS})}
 \ll_\epsilon \sqrt r\,Q^{1/2+\epsilon}M^{3/2}/\Delta.
 \tag{5}
$$

Finite Parseval in the $r$ classes bounds the sum over $a=0,\ldots,r-1$ of squared HS correlations with $e^{2\pi i an/r}$ by
$\max_j(r|\mathcal J_j|/|\mathcal J|)\|\Pi_r^{\rm per}\widetilde X\|_{L^2(\mathrm{HS})}^2$;
the prefactor is $O(1)$.

The distinct reduced phases of denominator $\le B$ have spacing at least $B^{-2}$ on the circle. Their off-diagonal Gram entries on this consecutive interval are $O((\Delta\|a/r-a'/r'\|)^{-1})$ by geometric summation. By circle spacing, the total absolute off-diagonal row sum is $O(B^2\log(2B)/\Delta)=o(1)$, since $\xi<\delta<1/2$. Their Gram is therefore bounded below by $I/2$, and the inverse-Gram projection formula, applied entrywise, bounds the projected squared HS norm by twice the sum of the squared correlations. By (5) and $\sum_{r\le B}r=O(B^2)$ this gives the first term in (1).

Finally restore the proper powers and exact unions of R40 cells. Orthogonal projection is a contraction. The proper-power entry remainder gives $O(Q^{-1/2}ML^4)$ in full $L^2(\mathrm{HS})$, absorbed by the first term. The uniform R43 operator error of changing both test legs is $O(L^2Y^{-1/5})$, costing an additional $O(L^{1/2})$ in HS. This gives the second term in (1). The exponents make the first error polynomially small for fixed sufficiently small $\epsilon$; the second is smaller than any fixed inverse log on this $H$-range.

No estimate here applies to the orthogonal complement in the modulus, or supplies concentration, the unsmoothed variance, or weak S.
