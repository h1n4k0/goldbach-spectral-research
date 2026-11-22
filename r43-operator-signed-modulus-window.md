# A signed modulus-window mean for the actual exterior difference matrix

**Scope.** This proves cancellation of the *signed first moment* of genuine prime-power aliases minus the exact continuous model, uniformly over ordinary even-modulus intervals. It does not bound the average norm, the mean square, or any individual modulus. The result uses auxiliary GRH beyond the original local GRH.

Put $L=\log Q$, $\ell=\log L$. Fix $K>0$, $0<\delta<1/2$, $0<\gamma<2\delta/3$, and a fixed $C>1$. Let $\mathcal I$ be any subinterval of $[Q,2Q]$ of length $\Delta\ge Q^{1/2+\delta}$, and average over the even integers $N\in\mathcal I$. Choose a common $H$ and physical grid with

$$
 2(K+3)\ell^2/\log\ell\le H,\qquad
 Y=e^H,\qquad M=e^{CH}\le Q^\gamma .
$$

Use every whole dyad $I_V=[V,2V)\subset [Y,M]$ on the grid $V=2^jY$, and let $E_N$ map the fixed dyad-index basis to the [real normalized weighted mean differences](r40-operator-negative-difference-subspace.md) $e_{N,V}$ in the actual physical Hardy realization at $N$. Use the exact parameters of the [fine-side grid](weak-s-exterior-fine.md), fixed independently of $N$. Assume the original local Dirichlet GRH for each even $N$ included, and also Dirichlet GRH for all moduli $2k\le 8M+2$. In particular global Dirichlet GRH suffices. Then

$$
 \left\| \operatorname{Avg}_{N\in\mathcal I,\ 2\mid N}
           E_N^* T_N E_N \right\|_{\rm op}
 \ll Q^{-\delta}M^{3/2}L^4 + L^2Y^{-1/5}
 =o(L^{-K}).
 \tag{1}
$$

The implied constants depend on the fixed exponents and grid, not on the interval position or its endpoints. With fixed physical subcell endpoints instead of full cells, the second error on the right is absent. For a full shell, the same proof permits any fixed $\gamma<1/3$, by using $\Delta\asymp Q$ directly. Since $\log M< L/3$, the [log-separation mask](r31-operator-zero-diagonal.md) is one on the complete matrix support. In the range of the [mean-difference benchmark](r41-operator-mean-difference-benchmark.md) this in particular gives the signed matrix mean of its actual diagonal and adjacent prime-power alias compensation, against the R41 deterministic target.

## 1. Genuine weights and continuity in the modulus

First use fixed physical subintervals $[V,5V/4)$ and $[7V/4,2V)$, not unions of whole fine-side cells. Keep the identical normalized weighted-mean difference construction. Denote it $\widetilde e_{t,V}$ when the modulus parameter is extended to real $t\in[Q,2Q]$, using

$$
 r_t(u)=u^{-3/2}\big((tu)^{-2/\log t}+(tu)^{-1/4}\big)^{1/2}.
$$

For $y\in [1,2]$, put $R_{t,V}(y)=V^{3/2}r_t(Vy)$ and $F_{t,V}(y)=V^{1/2}\widetilde e_{t,V}(Vy)$. They and their $t\partial_t$ derivatives are uniformly bounded there; on each first/last subinterval the normalizing $L^2(dy)$ factors are bounded above and below. This follows from the explicit weight and $\log V\le\gamma\log Q$, and differentiating the fixed-window integrals in the normalizers. The signs and $\int R_{t,V}F_{t,V}=0$ are exact. Define

$$
 b_{t,V}(s)=\sqrt{2\pi s}\int_{y\ge s}R_{t,V}(y)F_{t,V}(y)\,dy
$$

for $s>0$, zero elsewhere. This is supported on $[1,2]$, uniformly bounded and Lipschitz in $s$ there and on the whole line after zero extension. Also $t\partial_t b_{t,V}(s)$ is bounded uniformly, with the same support; the constant prefix vanishes for every $t$. The actual Volterra profile weight without $\Lambda(n)$ is exactly

$$
 \frac{\sqrt{2\pi n}}t\int_{u\ge n/t}r_t(u)\widetilde e_{t,V}(u)\,du
       =\frac{b_{t,V}(n/(tV))}{\sqrt{tV}} .
 \tag{2}
$$

This follows by substituting $u=Vy$, and retains the true Hardy weight.

For an entry with dyads $V,U$, the [exact physical cumulative discrepancy](source-round2.md) and Volterra pairing give a signed sum of three types of lines: $m=n+kN$ and $m=n-kN$ with plus signs, and $m=kN-n$ with minus sign, $k\ge1$. No $n=m$ line occurs. On a line the prime-power weight is $\Lambda(n)\Lambda(m)$ times

$$
 W_t(n,m)=\frac{b_{t,V}(n/(tV))b_{t,U}(m/(tU))}{t\sqrt{VU}},
 \tag{3}
$$

with the original unit restrictions. Its counterpart in the model is $\mathfrak S(kt)\int W_t(n,m(n,t))\,dn$ for $t=N$. Indeed the physical line measure is $\mathfrak S(kN)\,d(n/N)$, and integration of the two physical Volterra factors in (2) converts it to this ordinary $dn$ normalization. Only $k\le 4\max(V,U)$ can occur.

The effect of removing all proper prime powers from the arithmetic terms of this entry, for each $N$, is $O(Q^{-1/2}ML^3)$. To see it, at most $O(\sqrt{Q\max(V,U)}L)$ proper powers occur on either raw leg; each has at most $O(\max(V,U))$ partners over the alias lines, and each product is at most $O(L^2/(Q\sqrt{VU}))$. Both remaining prime coordinates exceed $N$, hence automatically satisfy the unit restrictions. This removal is only an error bound; the exact model is unchanged.

## 2. Divisor switching on an arbitrary modulus interval

Fix $k$ and one line orientation. On the arithmetic side sum over the even $N\in\mathcal I$ without normalizing yet. With $\lambda(n)=\log n$ on primes and zero otherwise, switch the line equation to

$$
 t=(m-n)/k,\quad (n-m)/k,\quad\text{or }(m+n)/k,
$$

respectively. The condition that $t$ is an even integer becomes $m\equiv n\pmod{2k}$ or $m\equiv -n\pmod{2k}$ as appropriate. Write $W(n,m)={\bf1}_{t\in\mathcal I}W_t(n,m)$ after this substitution. By symmetry between the two legs take $V\le U$ and fix the short raw leg $n$ for the first replacement; transposition only exchanges the two difference orientations. The support is in $QV\le n\le4QV$ and $QU\le m\le4QU$.

For fixed one coordinate, the other-coordinate function $W$ has sup norm and total variation $O(1/(Q\sqrt{VU}))$. In fact $t$ varies monotonically linearly where positive, and each ratio appearing in (3), as a function along that line, is of the form $(a/t+b)/V$ or $(a/t+b)/U$ with constant real $a,b$. It is monotone, and its travel through $[1,2]$ is at most one. Lipschitz continuity in the ratio and the $t\partial_t$ bounds handle the two profile factors. The extra sharp interval restriction costs at most two endpoint jumps of the same size. The prefactor $1/t$ is monotone with variation $O(1/Q)$. This proves the claimed bound uniformly in $k,n,m,V,U$.

For a fixed prime $n$ in its support, $n>2k$ for large $Q$, so its residue class modulo $2k$ is a unit. The [standard GRH prime number theorem in arithmetic progressions](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=126) gives the uniform error $O(\sqrt{QU}L^2)$ for partial sums of $\lambda(m)$ in the class after subtracting Lebesgue density $1/\phi(2k)$. The ordinary $\Lambda$ version gives the same bound for $\lambda$ after discarding proper powers. Abel summation against $W(n,m)$, followed by the elementary total bound $\sum_{n\le4QV}\lambda(n)\ll QV$, gives error $O(\sqrt{QV}L^2)$ at this $k$. Next replace $\lambda(n)$ in the main term by Lebesgue measure. The $n$-variation of $\int W(n,m)\,dm$ is at most the integral of the $n$-variations and hence $O(\sqrt{U/V})$. The ordinary RH prime number theorem and Abel therefore give error $O(\sqrt{QU}L^2/\phi(2k))$. Summing both bounds over $k\le4U$ costs at most $O(Q^{1/2}M^{3/2}L^2)$ in this unnormalized modulus sum.

The remaining switched integral is $\phi(2k)^{-1}\iint W(n,m)\,dn\,dm$. With $n$ fixed, substitute $m=m(n,t)$; its absolute Jacobian is $k$ on each orientation. Thus the main term for this line is exactly

$$
 \frac{k}{\phi(2k)}\int_{\mathcal I} I_k(t)\,dt,\qquad
 I_k(t)=\int W_t(n,m(n,t))\,dn .
 \tag{4}
$$

The substitution $n=ty$ in $I_k$ shows $\|I_k\|_\infty+\mathrm{TV}_{[Q,2Q]}(I_k)\ll1$. The factors then have fixed ratio arguments $y/V$ and $(\pm y\pm k)/U$. Their product is supported in an interval of length $O(\min(V,U))$; the prefactor is $1/\sqrt{VU}$, and the $t$-derivatives are $O(1/t)$. In particular (4) is valid uniformly on every $\mathcal I$, with no smoothing of its endpoints.

## 3. The exact averaged singular coefficient

For the original model on even $N$,

$$
 \mathfrak S(kN)=\mathfrak S(2k)
 \sum_{\substack{d\mid N\\ d\text{ odd squarefree}\\(d,k)=1}}
       a(d),\qquad a(d)=\prod_{p\mid d}\frac1{p-2}.
$$

On $\mathcal I$, the progression $N\equiv0\pmod{2d}$ sums $I_k(N)$ to $(2d)^{-1}\int_{\mathcal I}I_k(t)\,dt+O(1)$, by its bounded variation and the uniform floor discrepancy. For every fixed $\epsilon>0$, $a(d)\ll_\epsilon d^{-1+\epsilon}$ and $\mathfrak S(2k)\ll_\epsilon k^\epsilon$, by bounding each large-prime factor by $p^\epsilon$ after removing its $1/p$ where appropriate. Summing errors for $d\le2Q$, and extending the main sum over $a(d)/d$ past $2Q$, therefore gives $O_\epsilon(Q^\epsilon)$ per $k$ after adjusting $\epsilon$ (as $k\ll M\le Q^\gamma$). Exactly,

$$
 \frac{\mathfrak S(2k)}2
 \prod_{\substack{p>2\\p\nmid k}}
       \left(1+\frac1{p(p-2)}\right)
 = \prod_{\substack{p>2\\p\mid k}}\frac p{p-1}
 =\frac k{\phi(2k)}.
$$

The first equality cancels the good-prime factors of the twin-prime singular-series product; the even-prime factor is the initial $2$. Thus the model main term is precisely (4), on each line before summing its sign.

Divide by the number $\asymp\Delta$ of even moduli in $\mathcal I$ and sum the three signs. The signed entry residual is $O(Q^{1/2}M^{3/2}L^3/\Delta)$, absorbing the proper-power error since $\Delta\le Q$, and absorbing the $O_\epsilon(MQ^\epsilon/\Delta)$ singular-series error. There are $O(L)$ dyads, so the elementary matrix bound by dimension times the uniform entry estimate gives $O(Q^{1/2}M^{3/2}L^4/\Delta)$.

Finally, on each dyad the original R40 difference built from whole cells differs from the fixed-endpoint difference in norm by $O((d(V)/V)^{1/2})\ll V^{-1/5}$, since lost endpoint lengths are $O(d(V))$, the relative physical weights are bounded, and the normalizers are comparable. Disjoint dyad supports give the same $O(Y^{-1/5})$ for the difference of the two basis isometries, without an extra dimension. The original local-GRH trace of $P_N$ and the [stationary benchmark bound](weak-s-exterior-fine.md#diagonal-and-beta-benchmark) give $\|T_N\|\ll L^2$ on this exterior strip. Hence changing both test legs costs $O(L^2Y^{-1/5})$ uniformly in each $N$. This proves (1).

No sum of absolute signed errors over $N$ is controlled. The divisor switch uses the full ordinary even-modulus interval, not a selected exceptional set. Both signs and the exact original continuous model, rather than the inflated long-divisor integer diagonal, enter the conclusion. Individual-modulus covariance and weak S remain open.
