# A faster critical-prime bound and an actual density-one family

Fix a constant $C>1$. We use the original signed Type II critical-prime shell from the [proportional low-radical theorem](weak-s-type-ii-critical-prime-proportional-low-radical-closure.md), with even target $N$, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, and $I_d\subset[X,CX]$. Its two distinct prime boxes, arbitrary allowed bounded prime selector, actual hard cutoffs, and exact complementary coefficients are unchanged. In particular $J=[N-y,N/2)$ with $N/2\le y\le9N/16$, the cofactor $k$ has its genuine hard restrictions including $k>t\ge N^{.49999}$, and

$$
 D_m=\mathbf1_{m\in J}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\ {\rm in\ its\ true\ hard\ range}\\
                       (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k).
$$

Write $D(\alpha)=\sum_mD_m e(m\alpha)$ with $e(z)=\exp(2\pi iz)$, and let $\mathcal E_N(D)$ denote its squared norm on the actual arcs:

$$
 \mathcal E_N(D)=
 \int_{-1/(10N)}^{1/(10N)}
 \sum_{\substack{q\ {\rm prime}\\.8X\le q\le .9X}}
     \sum_{a=1}^{q-1}|D(a/q+\beta)|^2\,d\beta .
$$

**Pointwise theorem.** Fix $0<c<1/2$ and $\varepsilon>0$. Let $R\mid N$ be any even divisor with $2^{\omega(R)}\le L^c$, where $\omega(R)$ counts distinct prime divisors. Define the actual omitted-unit weight

$$
 \mathcal W(N,R)=\sum_{\substack{p\mid N\\p\nmid R}}\frac{1+\log p}{p}.
$$

Then, with all original hard cutoffs uniform,

$$
 \mathcal E_N(D)\ll_{C,c,\varepsilon}
   N\big(L^{-(1-2c)/4+\varepsilon}+\mathcal W(N,R)\big).
 \tag{1}
$$

The original full signed shell, the separately centered covariance, and its original parity-preserving signed even-lattice residual with $M=\lceil XL^2\rceil$ are bounded by

$$
 O_{C,c,\varepsilon}\left(
       N L^{-(1-2c)/8+\varepsilon}
               +N\sqrt{\mathcal W(N,R)}\right).
 \tag{2}
$$

Here a signed residual is the signed sum, not a bound for the squared individual compensated offsets. In particular, taking $R$ to have every prime of $N$ improves the rate on the low-radical family without changing its true unit gate.

**Density consequence.** For every fixed $A>0$ and every sufficiently large $Y$, all but $O_{C,A}(Y(\log Y)^{-A})$ even $N\in[Y,2Y]$ satisfy $\mathcal E_N(D)\ll_{C,A} N/\log(2+\log\log N)$ and the three signed bounds $O_{C,A}\big(N/\sqrt{\log(2+\log\log N)}\big)$, simultaneously in the original hard cutoffs and prime selector. Alternatively one gets the faster signed bound $O_C(N/\sqrt{1+\log\log N})$ on a density-one family with exceptional count $O_C(Y/\log(2+\log\log Y))$.

Every assertion is unconditional, for the fixed proportional divisor range and this critical-prime shell only. In particular none is a pointwise bound for unrestricted unit radicals, a theorem for polynomially wider divisor ranges, or an estimate of the other parts of the Goldbach kernel.

## 1. Signed ordinary squares on actual restricted multiples

For the proof let

$$
 F_m=\mathbf1_{m\in J}
       \sum_{\substack{dk=m,\ d\in I_d\\ k\ {\rm in\ its\ true\ hard\ range}}}\mu(d).
$$

Then $D_m=\mu^2(m)\mathbf1_{(m,N)=1}F_m$ exactly. Indeed the summands of $D_m$ require squarefree $m$, and on squarefree $m$ the single product mask makes both $\mu^2(k)$ and $(d,k)=1$ automatic. As in the previous theorem, $F$ outside the squarefree support is only a device for an ordinary squared-error estimate.

For every squarefree integer $\ell\ge1$ and $j=1$ or $2$, we claim

$$
 E_{\ell,j}:=\sum_{\ell^j\mid m}|F_m|^2
       \ll_C C_0^{\omega(\ell)}\frac{N(1+\log\ell)}{\ell^j}
 \tag{3}
$$

with an absolute $C_0>1$. This remains true with bounded-BV weights in the two divisor labels and a bounded product multiplier, with constants depending on their variation or supremum bounds.

First impose hard gates alone. In the signed square expansion both signed divisors $a,b$ are squarefree and lie at scale $X$ with ratios controlled by $C$. For each pair, the possible real $m$ after the product and cofactor tests form an interval $U(a,b)\subset J$, including the prescribed strict or inclusive endpoints. The integer count with $[a,b,\ell^j]\mid m$ is its length divided by $[a,b,\ell^j]$, plus $O(1)$. For the pairs with $g=(a,b)>G=\ell^j$, the absolute floor error is

$$
           \sum_{G<g\ll_C X}O_C((X/g)^2)\ll_C N/G.
 \tag{4}
$$

To handle the full continuous signed contribution, at fixed real $m$ let $I$ be the allowed interval of its signed divisor. Write $a=s a', b=t b'$ with $s=(a,\ell)$ and $t=(b,\ell)$. Since $a,b$ are squarefree, $s,t\mid\ell$, $(a'b',\ell)=1$, and $[a,b,\ell^j]=\ell^j[a',b']$. The signed form on this interval is therefore $\ell^{-j}$ times the quadratic form with kernel $1/[a',b']$ on the vector

$$
 \mu(a')\mathbf1_{(a',\ell)=1}
                       \sum_{s\mid\ell}\mu(s)\mathbf1_{sa'\in I}.
$$

This kernel is positive semidefinite by $\gcd(a',b')=\sum_{v\mid(a',b')}\varphi(v)$. The Dress–Iwaniec–Tenenbaum signed interval bound used in the [sharp ordinary energy proof](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy) gives bounded lcm norm for the unmasked signed interval vector. The norm for an interval vector with $(a',\ell)=1$ is then at most

$$
 O(1)\sum_{\substack{u\ge1\\p\mid u\Rightarrow p\mid\ell}}u^{-1/2}
       =O(1)\prod_{p\mid\ell}(1-p^{-1/2})^{-1}.
$$

Indeed the exact convolution of $\mu$ with the indicator of integers supported on primes dividing $\ell$ imposes the coprimality. Scaling both coordinates in the quadratic kernel by $u$ scales its norm by $u^{-1/2}$, and the remaining rescaled interval is still an ordinary signed interval. Minkowski over $s\mid\ell$ and then squaring give an upper bound $O(C_0^{\omega(\ell)}/\ell^j)$ for the continuous form at each real $m$. Integrating gives $O(C_0^{\omega(\ell)}N/\ell^j)$.

It remains to compare the actual and continuous contributions at $g\le G$ by absolute counting. Set $a=gu,b=gv$, so that $g,u,v$ are pairwise coprime and squarefree before any relaxation. One has $u,v\asymp_C X/g$, and an actual multiple is $m=guvr$ with $r\asymp_C g$. At each $p\mid\ell$ there are four possibilities: no $p$ in $guv$, or $p$ in exactly one of $g,u,v$. In the first case $r$ must be divisible by $p^j$; in the other three it must be divisible by $p^{j-1}$. Accordingly, for each of at most $4^{\omega(\ell)}$ choices, write $A_g,A_u,A_v,A_r$ for the required divisibility moduli on the four coordinates, with

$$
 A_g A_u A_v A_r=\ell^j .
$$

For the actual count at fixed $g$, the positive upper bounds for $u,v,r$ give at most $O_C(N/(g A_u A_v A_r))$ triples: an integer multiple of $A$ up to $V$ has at most $V/A$ choices, with no extra $+1$. This upper bound is still valid after relaxing the requirements of nondivisibility and the other gates. Summing $g\le G$ over $A_g\mid g$ saves the remaining $A_g$, up to $1+\log G$. For the continuous count the exact denominator in the same local choice is $guv A_r$. The $u,v$ reciprocal sums on their proportional ranges, with the two required divisibilities, are $O_C(1/A_u)$ and $O_C(1/A_v)$. This gives the same bound after summing $g$. Thus each entire small-$g$ correction is $O_C(4^{\omega(\ell)}N(1+\log G)/\ell^j)$. Subtract the continuous small-$g$ part from the full signed main and insert the actual small-$g$ part. Together with (4) and $G=\ell^j$, this proves (3).

For bounded-BV label weights, use their finite summation-by-parts representations by prefix indicators of their true intervals. Minkowski applies in the restricted coefficient norm on $\ell^j\mid m$, and a bounded weight of the product contracts it up to its supremum. This proves the variation assertion without replacing the signed divisor sum by an unsigned one. The case $\ell=1$ gives the uniform ordinary full-circle squared norm $O_C(N)$ also for the auxiliary $F$ and its bounded-BV versions.

## 2. Two quantitative transfers to the actual coefficient

Replace the unit mask of $D$ temporarily by $\mathbf1_{(m,R)=1}$. The difference is supported where some genuine omitted prime $p\mid N,\ p\nmid R$ divides $m$, and is bounded by $|F_m|$. Thus (3) with $j=1,\ell=p$ yields

$$
 \|D-\mu^2(\cdot)\mathbf1_{(\cdot,R)=1}F\|_2^2
                         \ll_C N\mathcal W(N,R).
 \tag{5}
$$

Now put $\delta=L^{-B}$ for a fixed $B>0$. Smooth the physical and cofactor gates within the original intervals at relative width $\delta$, keeping $d$ sharp, as in the [actual endpoint theorem](weak-s-type-ii-critical-prime-zero-base-boundary-energy.md#3-removing-all-actual-endpoint-layers-in-the-signed-compensated-shell). Use $W(m/N),w(k/X)$, valued in $[0,1]$, compactly supported away from zero in their normalized coordinates, equal to one except on the thin endpoint layers. They may be arranged to have first derivative supported in layers of width $O_C(\delta)$ and derivative bounds $O_{C,j}(\delta^{-j})$: convolve a shrunk interval with a fixed compact mollifier of radius proportional to $\delta$. For intervals shorter than twice that radius, use zero. The physical gate and possible cofactor values stay within fixed positive proportional ranges, so inactive constraints may be ignored in this smoothing. Let $F^{\mathrm{sm}}$ be the resulting auxiliary signed coefficient. The ordinary squared smoothing cost on $\mu^2(m)\mathbf1_{(m,R)=1}F_m$ is

$$
 O_{C,B}(N L^{-B}L_2+N^{3/4}).
 \tag{6}
$$

Indeed the proof of the endpoint theorem bounds the physical and label edge norms by adding nonnegative squares after the common product unit indicator; it works for this smaller unit mask exactly as for the original one. Equations (5)–(6) refer to the actual coefficient difference, not errors only in one progression.

Instead of expanding over the product of all small primes, truncate the exact identity $\mu^2(m)=\sum_{l^2\mid m}\mu(l)$ at $l\le T=L^\eta$, with fixed $\eta>0$. Define

$$
 D^{[T,R]}_m
 =\mathbf1_{(m,R)=1}F_m^{\mathrm{sm}}
                     \sum_{\substack{l\le T\\l^2\mid m}}\mu(l).
$$

The square of the omitted coefficient sum is at most the count of pairs of squarefree $a,b>T$ with $a^2,b^2\mid m$. Each pair has squarefree $\ell=[a,b]>T$, $\ell^2\mid m$, and for each $\ell$ there are at most $3^{\omega(\ell)}$ pairs, since a prime may be in either or both. By (3), for every fixed $\rho>0$,

$$
 \|D^{[T,R]}-\mu^2(\cdot)\mathbf1_{(\cdot,R)=1}F^{\mathrm{sm}}\|_2^2
 \ll_C N\sum_{\ell>T}\frac{(3C_0)^{\omega(\ell)}(1+\log\ell)}{\ell^2}
 \ll_{C,\rho} N T^{-1+\rho}.
 \tag{7}
$$

The last inequality follows from $(3C_0)^{\omega(\ell)}(1+\log\ell)\ll_\rho \ell^{\rho/2}$, by splitting primes into the finitely many small ones and the remaining factors. This proves a uniform ordinary norm tail even though the cutoff coefficient need not be between zero and one. In particular $\|D^{[T,R]}\|_2^2\ll_C N$ (fix, for example, $\rho=1/2$). All transfers hold on the disjoint original arcs by Parseval.

## 3. Smooth completion at the literal rational points

Keep each $q\in[.8X,.9X]$ prime, $\beta\in[-1/(10N),1/(10N)]$ and each nonprincipal character $\chi\bmod q$. The exact retained sum is separated just as in the previous theorem: for each squarefree $l\le T$ with $(l,R)=1$, put $s=(l,d)$, then $d=su$ with $(u,l)=1$ and $k=(l^2/s)b$. These are the exact possibilities for $l^2\mid dk$ on the squarefree signed $d$ support. Keep the unit restriction on $u$; include the actual remaining $R$-unit test on $b$ by $\mathbf1_{(b,R)=1}=\sum_{h\mid(b,R)}\mu(h)$, and set $b=hv$. The character multipliers associated with this split are $\chi(l^2h)$; no modulus-dependent support selector is introduced.

For the normalized product weight put $G_\beta(z)=W(e^z)e(\beta N e^z)$. Its Fourier inversion separates the factors through $e(\tau\log(d/X))e(\tau\log(k/X))$. Since the derivatives of $W$ are localized at the physical layers, $\|G_\beta'\|_1=O_C(1)$ and $\|G_\beta''\|_1=O_C(\delta^{-1})$, uniformly in the actual $\beta$. Thus, for $\tau\ne0$,

$$
 |\widehat G_\beta(\tau)|
           \ll_C \min(1,|\tau|^{-1},\delta^{-1}|\tau|^{-2}).
 \tag{8}
$$

The ordinary Fourier transform here is $\widehat f(\xi)=\int_{\mathbb R}f(t)e(-t\xi)\,dt$.

At a fixed split, the $u$ character sum has coefficients of modulus at most one in a range of length $O_C(X)$; every modulo-$q$ residue occurs $O_C(1)$ times. Its $\ell^2$ norm in all characters is $O_C(\sqrt{qX})$ by multiplicative orthogonality. The $v$ sum has test $f_\tau(v/V)$, where

$$
 f_\tau(t)=w(t)e(\tau\log t),\qquad V=Xs/(l^2h)\le X.
$$

Put $x=V/q\le 5/4$. Poisson summation modulo $q$ and the nonprincipal Gauss sum give an upper bound $\sqrt q\, x\sum_{j\ne0}|\widehat f_\tau(jx)|$ for this $v$ sum. To bound the last quantity at every scale $x$, periodize $f_\tau$ with period $1/x$ and apply Parseval, also to its derivative. The support has bounded length, so these translates have uniformly bounded overlap for all $0<x\le5/4$. It follows that

$$
 x\sum_j|\widehat f_\tau(jx)|^2\ll_C\|f_\tau\|_2^2,\qquad
 x\sum_j(jx)^2|\widehat f_\tau(jx)|^2\ll_C\|f_\tau'\|_2^2 .
$$

Split the $\ell^1$ sum at $|jx|=H=\max(2,1+\|f_\tau'\|_2)$. Cauchy on the lower part costs $O_C(\sqrt H)$, since $\|f_\tau\|_2\ll_C1$. On the upper part, use the second bound and $x\sum_{|jx|>H}(jx)^{-2}\ll 1/H$, to obtain the same cost. The localized cofactor derivatives give $\|w'\|_2\ll_C\delta^{-1/2}$, so

$$
 x\sum_{j\ne0}|\widehat f_\tau(jx)|
                  \ll_C \delta^{-1/4}+\sqrt{1+|\tau|}.
$$

This does not use a sharp unsmoothed character estimate. By (8) and splitting the integral into $|\tau|\le1$, $1<|\tau|\le\delta^{-1}$, and $|\tau|>\delta^{-1}$, the integral of this last upper bound against $|\widehat G_\beta(\tau)|$ is $O_C(\delta^{-1/2})$.

Now apply Minkowski in $\ell^2(\chi\ne\chi_0)$ to the split factors and the $\tau$ integral. There are at most $\sum_{l\le T}\tau(l)\ll T(1+\log T)$ choices of $(l,s)$ and $2^{\omega(R)}\le L^c$ choices of $h$. We obtain at each $q,\beta$

$$
 \left(\sum_{\chi\ne\chi_0}
       \left|\sum_m D^{[T,R]}_m\chi(m)e(\beta m)\right|^2\right)^{1/2}
   \ll_C q\sqrt X\,\delta^{-1/2}T(1+\log T)L^c .
$$

After squaring, integrating over the original $\beta$ interval and summing over $q$, the nonprincipal energy is therefore

$$
 O_{C,\eta}\big(N L^{-1+B+2\eta+2c}L_2^2\big).
 \tag{9}
$$

This uses just the upper bound $O(X/L)$ for the number of critical primes.

## 4. Restore the original shell and bound the exceptional family

At the nonzero additive numerators, retain the nonunits modulo $q$ and the principal unit character as in the previous theorem's exact Gauss decomposition. The principal unit part contributes squared energy $O_C(N/L)$ by $\|D^{[T,R]}\|_2^2\ll_C N$ and $\sum_q1/(q-1)\ll 1/L$, after subtracting the nonunit product part from its numerator-zero value.

For clarity, the elementary nonunit estimate must account for the fact that the new truncated squarefree multiplier is not bounded by one. If $q\mid m=dk$, then $q\mid d$ because $k<X/2<q$, and there are $O_C(1)$ such $d$. At each such $d$,

$$
 \begin{split}
 \sum_{k\ll_C X}\left|\sum_{\substack{l\le T\\l^2\mid dk}}\mu(l)\right|
 &\le \sum_{\substack{l\le T\\l\ {\rm sf}}}
             \#\{1\le k\ll_C X:l^2\mid dk\}\\
 &\ll_C X\sum_{\substack{l\le T\\l\ {\rm sf}}}\frac{(l,d)}{l^2}
 \ll_C X\prod_{p\mid d}\left(1+\frac1p\right).
 \end{split}
$$

We used only the signed squarefree $d$ support, so $(l^2,d)=(l,d)$. Here $d=jq$ with $j=O_C(1)$, hence the displayed product is uniformly $O_C(1)$. The actual $q$-nonunit polynomial on each fixed $\beta$ is consequently still $O_C(X)$, uniformly in $T$ and the cutoffs. Its contribution at all nonzero numerators is $O_C(N/L)$ after integration. In the exact Gauss expansion the nonprincipal character energy enters with factor $q/(q-1)$, so (9) controls the remaining component.

Choose $B=\eta=(1-2c)/4$. Then the exponent in (9) is $-\eta$. Equations (5)–(7), the character bound, and the disjoint-arc norm give (1), absorbing the fixed logarithms and taking $\rho$ small in terms of $\varepsilon$. The prime polynomial has ordinary squared norm $O(N)$ from unique factorization of its two disjoint prime boxes and prime counting. Cauchy on the actual arcs gives the full signed bound in (2); the separate centering maps are contractions. The endpoint theorem's exact parity-preserving high-pass identity, including its $O_C(N/L+N(X/M)^2)$ error from the common average and repeated zero offset, gives the third signed bound in (2) for the original hard coefficient. The original additive target $N$ and both original prime-leg masks were never replaced.

For the density conclusions, fix for example $c=1/4$. Let $v=\log\log N$ and

$$
     z_N=\kappa v\log(2v),\qquad
     R_N=\prod_{\substack{p\mid N\\p\le z_N}}p .
$$

A sufficiently small fixed $\kappa>0$ ensures $2^{\omega(R_N)}\le 2^{\pi(z_N)}\le L^c$ by the elementary prime upper bound. Also $2\mid R_N\mid N$ for all large even $N$. For $N\in[Y,2Y]$ use $v_Y=\log\log Y$, $z_*=\kappa v_Y\log(2v_Y)$, and dominate $\mathcal W(N,R_N)$ by the common tail

$$
     A_N=\sum_{\substack{p>z_*\\p\mid N}} b_p,\qquad
                 b_p=(1+\log p)/p .
$$

Counting true multiples and using $\sum_{p>z_*}b_p/p\ll z_*^{-1}$ by prime dyads shows $\sum_{N\le2Y} A_N\ll Y/z_*$. Hence $A_N\le1/v_Y$ except on $O(Y/\log(2v_Y))$ targets, giving the faster density-one bound stated above.

For arbitrary fixed inverse-logarithmic exceptional count, take positive

$$
              s=\frac{z_*\,\log(2v_Y)}{8(1+\log z_*)}
                         \asymp_\kappa v_Y\log(2v_Y).
$$

Since $b_p$ decreases for $p>1$, one has $s b_p\le \log(2v_Y)/8$ for $p>z_*$. On expanding the exact positive divisor product and using $\#\{N\le2Y:d\mid N\}\le2Y/d$, we get

$$
 (2Y)^{-1}\sum_{N\le2Y}e^{s A_N}
 \le \prod_{p>z_*}\left(1+\frac{e^{s b_p}-1}{p}\right)
 \le \exp\!\left(O_\kappa(v_Y^{1/8})\right).
$$

Indeed the logarithm is at most $s(2v_Y)^{1/8}\sum_{p>z_*}b_p/p$, using $e^u-1\le u e^u$, and $s/z_*\ll_\kappa1$. The convergent positive Euler product does not assume independent prime divisibility of the targets. Markov with threshold $K_{A}/\log(2v_Y)$ now costs $O_A(Y\exp(-A v_Y))$ for sufficiently large fixed $K_A$. Insert this threshold in (1)–(2) to get the claimed arbitrary fixed log-power exceptional family. All exceptional sets depend only on the actual target integers and fixed parameters, so the conclusions are simultaneous over the original cutoffs and permitted prime selectors.
