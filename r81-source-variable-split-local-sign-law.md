# The local sign law with the actual variable rough split

Use the genuine two-leg carrier of the [growing-rough theorem](r75-source-dynamic-giant-growing-rough-residual.md) and the exact original long-label tests of the [finite orbit](r77-source-finite-short-orbit-product-boundary.md), now with the below-square-root floors of the [fixed-split local law](r80-source-local-mean-square-at-sign-transition.md). In particular write $L=\log X$, $\ell=\log L$, $T=L/\ell$, $\theta=1/20$, $\epsilon=1/64$, $\mathcal J=[X/2,(1+\Delta)X/2]$, and $\mathcal X=[X,(1+\Delta)X]$, with the same fixed $\rho,\Delta$ as there. Use the genuine common real split

$$
                    V_X^2\le Z\le X^{\delta_0},\qquad
                    \tau=\log Z/L,\qquad V_X=\exp(T\ell^\theta).
$$

The cutoff $Z$ may depend on $X$. It is common to the targets in one scale window; the theorem is not a maximal estimate over a different choice at each target. Keep $n=hF$, $m=kG$ in $\mathcal J$, $n+m=N$ even, both squarefree $N$-units, with $h=sWU$, $k=s'W'U'$ and genuine distinct prime alphabets. The original $s,s'$ are primes with normalized log in $[5/4,7/4]$. Each $W$ consists of the allowed primes in $[e^{4T},Z]$, with the actual gates $W\le X^{\epsilon/2}$ and $\omega(W)\le2\log\ell$; $U>1$ uses the allowed primes $>Z$ with no imposed arity cap. The same two excluded neighborhoods of the growing-rough theorem are removed, and the true typical exceptional count is on the whole squarefree product $WU$. The exclusions make this the count in the literal fixed tag interval $(2V_X,Y_{*,X}^{1/2})$ for every target, where $Y_{*,X}$ is as in that theorem. In particular **at the lower split, $U$ can supply the true tags**. Both parities are retained.

For fixed $0<a,b<20$ with $\delta=a+b-20>0$, the actual prime floors are $F\ge\sqrt N e^{-aT_N}$ and $G\ge\sqrt N e^{-bT_N}$, $T_N=\log N/\log\log N$. Write $R_{N,Z}$ for the actual signed selected sum with $d>D_N,e>D_N,de>Q_N$, $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$, $Q_N=\lfloor Ne^{-20T_N}\rfloor$, and the original exterior minus. There is no further parity, sign or residue selector. Set $B_{\mathcal J}(N)=|\mathcal J\cap(N-\mathcal J)|$ and let $\Sigma(N)$ be the binary singular series exactly as in the fixed-split local law.

For each allowed $W$, let $K(W)$ be the exact set of nonnegative upper tag counts that complete its tagged count to the required typical interval. In normalized log coordinates, let $g_{\rm t}(u)=\mathbf1_{I_{\rm t}}(u)/u$ and $g_{\rm f}(u)=\mathbf1_{I_{\rm f}}(u)/u$ be the true tagged and free upper prime kernels of the growing-rough theorem, with irrelevant top truncation at $.7$. Thus the reciprocal continuum measure for upper count $K$ is

$$
 A_{+,K}=\sum_{\substack{j\in K,\ k\ge0}}\frac{g_{\rm t}^{*j}*g_{\rm f}^{*k}}{j!\,k!}.
$$

Convolution powers of order zero mean the atom at zero; let $\varrho_{+,K}$ be its density on the compact range about $1/2$. An empty $K$ gives zero. Define the normalization

$$
 \mathcal C_{X,Z}=
    \frac{|\mathcal J|}{\ell}
      \sum_{\substack{s,W\\\text{true lower alphabets and gates}}}
       \frac{\varrho_{+,K(W)}(1/2-\log(sW)/L)}{sW}.
 \tag{1}
$$

Let $\Psi(\delta)$ be exactly the deterministic signed coefficient of the [short-prime Euler sign theorem](r79-source-short-prime-euler-sign-transition.md), not a new count-dependent short coefficient.

**Theorem (unconditional).** One has $\mathcal C_{X,Z}\asymp_{\rho,\delta_0}X$ uniformly over the stated splits and

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
 \left|
 R_{N,Z}-\Sigma(N)B_{\mathcal J}(N)
            \left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2\Psi(\delta)
 \right|^2 \ll_{\rho,\delta_0,a,b} X^3\ell^{-1/5}.
 \tag{2}
$$

The critical zero $\delta_*$ of the sign theorem therefore still gives $O(X^3\ell^{-1/5})$ for the actual sum of squares at $a=b=(20+\delta_*)/2$, including $Z=V_X^2$. For nonzero $\Psi(\delta)$ its strict sign has at most $O(X\ell^{-1/15})$ exceptions in the full window, and in any fixed interior subwindow its sign and magnitude $\gg X$ have at most $O(X\ell^{-1/5})$ exceptions. These are uniform bounds for each common split, not a common exceptional set for all splits, a fixed-modulus result, or an unrestricted central or Hypothesis S estimate.

## 1. Uniform positivity with the actual two-source count

The upper bound in (1) comes directly from the growing-rough theorem: the positive lower reciprocal profile is $O(\ell\tau)$, and $\|\varrho_{+,K}\|_\infty\ll\tau^{-1}$ on $[.4,.6]$ uniformly in $K$. We give a separate lower bound, because the density for a specified $W$ can be zero at the lower split.

For this lower bound only, choose a sufficiently small **fixed** $\delta_1<\delta_0$. Restrict $W$ to its true primes up to $\min(Z,X^{\delta_1})$. In the upper exponential measure, restrict preliminary coordinates to the allowed interval above $\tau$ and at most $\delta_1$, with its actual tag split. Write $u$ for their total normalized log. In addition, insert exactly one free coordinate in $[2/5,3/5]$. The latter interval is wholly above $\tau$ and all removed neighborhoods for large $X$, and is disjoint from the preliminary coordinates. No other upper coordinate is used for this lower bound. The unique large coordinate is free, so the tag set of the preliminary coordinates remains exactly $K(W)$. The factorial coefficients factor with the large coordinate of order one: this is the positive submeasure obtained by splitting the free kernel into its two disjoint used ranges and discarding the unused summands. There is no additional factorial cost or sign.

For a true size-gated $W$ and any allowed $s$, put $v=1/2-\log(sW)/L$. If $u\le1/32$, then $2/5<v-u<3/5$ for all sufficiently large $X$, with fixed margin. In this positive submeasure the marked-coordinate density at $v$ is $1/(v-u)\gg1$. Thus for each such $W,s$ the density at $v$ is bounded below by a fixed constant times the preliminary positive mass with $u\le1/32$ and upper tag count in $K(W)$. This density comparison may first be taken almost everywhere, then for the continuous representatives in this compact range: over the indicated $u$ interval the marked factor is uniformly smooth in $v$ and separated from its endpoints. The marked coordinate ensures $U>1$ also when the preliminary measure consists solely of its atom at zero.

Before applying the size and count events, normalize the discrete $W$ reciprocal product and the preliminary continuous exponential measure. The resulting choices of $W$ primes are independent with probabilities $1/(p+1)$, while the preliminary continuous choices have the law of a finite Poisson point process of intensity $\mathbf1_{\text{allowed},\,\tau<u\le\delta_1}\,du/u$. This last assertion follows directly by dividing the exponential measure of ordered tuples with factorial denominators by its total mass. The two choices are independent. Their joint mass before this normalization is

$$
 M_{X,Z}=
   \prod_{\substack{e^{4T}\le p\le \min(Z,X^{\delta_1})\\p\ {\rm allowed}}}(1+1/p)
   \exp\!\left(\int_{\substack{\tau<u\le\delta_1\\u\ {\rm allowed}}}
                                 \frac{du}{u}\right)\asymp_{\delta_1}\ell .
 \tag{3}
$$

Indeed reciprocal PNT on the discrete part followed by the continuous integral gives the full allowed reciprocal mass in log coordinates from $4/\ell$ to $\delta_1$, uniformly across $Z$ including a split inside either excluded neighborhood. The first neighborhood costs bounded mass, as does the second (its two logarithmic endpoints have ratio $4$); the unsubtracted mass is $\log\ell+O_{\delta_1}(1)$. Also replacing $\log(1+1/p)$ by $1/p$ costs $O(\sum_{p\ge e^{4T}}p^{-2})$. If the split is above $X^{\delta_1}$, all this mass is discrete and the preliminary upper mass is the unit atom.

Both sides of the tag interval lie below $X^{\delta_1}$ for large $X$. Under the product probability just described the **sum** of the true lower and upper preliminary tag counts has mean

$$
  \log\!\left(\frac{\log(Y_{*,X}^{1/2})}{\log(2V_X)}\right)+o(1)
     =(1-\theta)\log\ell+O(\log\log\ell),
$$

by reciprocal PNT on the discrete portion and the exact continuous intensity above the split. Its variance is $O(\log\ell)$, since it is a sum of independent Bernoulli indicators and an independent Poisson count. The literal typical interval of half-width $2(\log\ell)^{3/4}$ therefore holds with probability $1-o(1)$, uniformly. This event is exactly that the preliminary upper count is in $K(W)$; the marked large coordinate adds none. The discrete count $\omega(W)$ has mean at most $\log\ell+O(1)$ and variance $O(\log\ell)$, so its literal $2\log\ell$ gate also holds with probability $1-o(1)$.

Finally Chebyshev's prime bound by partial summation gives $\sum_{p\le y}(\log p)/p\ll 1+\log y$, whence $\mathbb E\,\log W/L\ll\delta_1+L^{-1}$. The mean preliminary coordinate sum is at most $\delta_1$. Choosing $\delta_1$ small enough that Markov bounds both failures of $\log W/L\le\epsilon/2$ and $u\le1/32$ by $1/8$ for large $X$, the two true count events and two size tests together retain a positive absolute portion of (3), uniformly in $Z$. This choice does not shrink the theorem's split range; it is used only for a positive lower submeasure. The old prime $s$ contributes its independent reciprocal mass $\asymp1$ and does not enter the tag count. Summing the density lower bound now gives $\sum_{s,W}\varrho_{+,K(W)}(v)/(sW)\gg\ell$, proving (1)'s lower bound. No separate typicality or independence of the tags of the **gated** $W$ and $U$ has been assumed.

## 2. Exact seams and the count-sensitive one-bin law

The exact four rows of the finite orbit identity hold for the whole range of the present fixed $a,b$. Indeed each distinguished prime exceeds $D_N$, and the unrestricted containing orbit sums to $-\Lambda(h)=0$ or $-\Lambda(k)=0$ since each cofactor is squarefree composite. For the first three rows, the proof of the finite-orbit bound uses only a fixed log-label cap $\exp((22+a+b)T)$, fixed cofactor log windows of width $O(T)$, and the untagged Euler band above this cap and below $V_X/4$. This band lies in $W$ for every allowed $Z$ and its removal does not change $K(W)$; its reciprocal mass is $\theta\log\ell+O(1)$. Thus the same endpoint and variation estimates are uniform in $Z$ by the counting-density input of the growing-rough theorem. More explicitly, partition the genuine three moving tests by hard log bins of width $T/\ell$. Per bin the ordinary signed fourth norm is $O(X^{3/4}\ell^{-1-1/10})$; the orbit and positive norms are $O(X^{3/4}\ell^{-1})$. The ordinary-ordinary row has two ordinary signs and each mixed row one. The cuts leave $O(\ell^2)$ accepted and $O(\ell)$ ambiguous bin pairs. Hölder and Parseval bound the accepted contributions by $O(X^{3/2}\ell^{-1/10})$ in target $\ell^2$ norm and the ambiguous terms by $O(X^{3/2}\ell^{-1})$ using positive bounds. Floor slivers and unit corrections have the still smaller bounds stated below. This applies only to the first three rows, without using $a+b\le20$ to suppress the fourth.

The remaining genuine containing-containing row is

$$
 H_{N,Z}=
 \sum_{\substack{hF+kG=N\\\text{true carrier and units}}}
  \ \sum_{\substack{z\mid h,\ w\mid k\\(Fz)(Gw)\le Q_N}}
                  \mu(z)\mu(w)\log(h/z)\log(k/w).
 \tag{4}
$$

It has the displayed plus sign from the subtraction of forbidden products before applying the external minus. Fix $A>\max(4,\delta)$ with $\delta=a+b-20$. For the fixed lower floor comparison $F\ge F_0=\sqrt X e^{-aT}$, $G\ge G_0=\sqrt X e^{-bT}$, every active short label is at most $e^{AT}$ and belongs to $sW$ or $s'W'$ because $e^{AT}<V_X^2\le Z$. The fixed floors are below the genuine floors by monotonicity, with genuine logs differing by $O(1)$. Also (4) gives $F\le Q_N/G_0<\sqrt X$ and $G\le Q_N/F_0<\sqrt X$ for large $X$, since $a,b<20$. Each distinguished prime is unique under the comparison: two factors at or above the near-square-root floor would leave a residual product $e^{O(T)}$, while both are above the tag interval and the true typical count supplies a distinct prime $>2V_X$. The comparison thus preserves genuine integer representatives on either arm. This remains true when the needed tag is in $U$.

As in the fixed-split local law, unit removal has pointwise error $O_C(XL^{-C})$ for any fixed $C$: an overlap prime divides $N$, is at least $e^{5T/4}$, and contributes at most $O(X/p)$ possibilities, with $O(\ell)$ overlap primes to check and polylogarithmic weights from bounded short-label arity. To restore the genuine floors after this comparison, one arm must lie in a fixed log-width-$O(1)$ prime sliver; the other lies in its full $O(T)$ log window. The all-label positive fourth bounds of the finite orbit yield norms $O(X^{3/4}\ell/L)$ and $O(X^{3/4})$ on these arms and error $O(X^{3/2}\ell/L)$ on the target norm. These comparisons preserve the actual total count, keeping the genuine alphabet and exact residual count $K(W)$ in every positive or signed polynomial.

For (4) use $\alpha=(L/2-\log F)/T\in[0,a]$ and the analogous $\alpha'$ for $G$ in $[0,b]$. Bin the actual coordinates $\gamma=\alpha-\log z/T$ and $\gamma'=\alpha'-\log w/T$ with fixed hard bins of width $\ell^{-1}$. The weak test is $\gamma+\gamma'\ge(L-\log Q_N)/T=20+O(T^{-1})$. Accept an entire bin rectangle when it passes for every target in $\mathcal X$ and reject when it fails everywhere; all undecided or endpoint cases fall in only $O(\ell)$ ambiguous pairs. Their exact contributions cost $O(X^{3/2}\ell^{-1})$ in $\ell^2(N)$ via the positive norms. The $O(\ell^2)$ accepted rectangles give precisely the Fourier coefficient of their products of actual signed bin polynomials, all before any real model replacement. Denote their first and second arm polynomials by $A_i$ and $B_j$ and their fixed acceptance set by $\mathcal A$.

Put $S=sW$. For bin $J_i$ write $I_{i,z}=(J_i+\log z/T)\cap[0,a]$. The scalar for its true signed major density is

$$
 c_i=\frac1\ell \sum_{\substack{s,W\\\text{true lower masks}}}
     \sum_{\substack{z\mid S\\z\le e^{AT}}}
       \frac{\mu(z)}S\,\varrho_{+,K(W)}(1/2-\log S/L)\,|I_{i,z}|.
 \tag{5}
$$

Define $d_j$ by the other exponent interval. The positive lower labeled reciprocal profile is $O(\ell\tau)$, also when a short divisor is selected: double the $1/p$ occupation weight only in the fixed log-ratio band $[e^{4T},e^{AT}]$ (bounded reciprocal mass) and allow two old-prime choices. The growing-rough theorem gives $\sup+\operatorname{Lip}\ll\tau^{-1}$ uniformly for every $\varrho_{+,K(W)}$ on $[.4,.6]$, and quantitatively replaces the actual upper reciprocal sum for hard intervals with bounded-variation marks, to arbitrary inverse log error uniformly in $K(W)$. Consequently $|c_i|,|d_j|\ll\ell^{-1}$, and $\sum_i|c_i|+\sum_j|d_j|\ll1$.

For clarity, the major transfer leading to (5) does not average $K(W)$. On an auxiliary reduced polylogarithmic arc $a_0/q+\beta$ of the fixed-split local law, fix $h,z$ and use Siegel–Walfisz in just the true prime $F$ on the hard intersection from $hF\in\mathcal J$ and $Fz$ in its bin, with the fixed prime interval. Both $F$ and $h$ are coprime to $q$ since all their prime factors exceed every fixed power of $L$. The numerator sum over its reduced residues gives $\mu(q)/\varphi(q)$, multiplying a continuous term independent of $a_0$. Change the physical variable to $x=hF$, then replace the actual upper reciprocal distribution by its exact count-restricted continuum using this $W$. All discrete replacement errors are $O_C(XL^{-C})$ on these arcs for every fixed $C$: the total reciprocal label weight including all upper products is $O(\ell\tau)\,O(\tau^{-1})=O(\ell)$, and the other costs are fixed powers of $L$. With $F(\alpha)=\sqrt X e^{-\alpha T}$ the continuous density on $\mathcal J$ becomes

$$
 \frac1\ell\sum_{S,z}\frac{\mu(z)}S\int_{I_{i,z}}
    \varrho_{+,K(W)}
       \!\left(\tfrac12+\tfrac{\alpha}{\ell}+
               \tfrac{\log x-L}{L}-\tfrac{\log S}{L}\right)
    \frac{\log x-\log F(\alpha)-\log z}{\log F(\alpha)}\,d\alpha .
 \tag{6}
$$

The interval $I_{i,z}$ is fixed independent of $x$, and the mark equals $1+O(\ell^{-1})$ on the actual short label range. Changing physical points $x,y$ changes this mark by $O(|x-y|/(XL))$ and the density factor by $O(\tau^{-1}|x-y|/(XL))$. The density arguments lie in $[.4,.6]$ under the inherited true size gate. In particular (6) differs from (5) in absolute supremum plus total variation on $\mathcal J$ by $O(\ell^{-2})$: the interval width $\ell^{-1}$ and the relative log shift $O(\ell^{-1})$ have the prefactor $\ell^{-1}O(\ell\tau)\,O(\tau^{-1})$. This does not assert a relative error to the signed and possibly zero $c_i$.

The minor bound of the fixed-split law also stays uniform: its two half-integer Perron separations are on the genuine products $hF$ and $Fz$ and leave the short-label twist in the $h$ coefficient. Only a pointwise upper bound on the number of short labels is needed there, independent of the unrestricted upper arity. Thus minor suprema are $O_C(XL^{-C})$ for any fixed precision with the sufficiently large fixed polylogarithmic arc choice, and their Fourier coefficient norms after multiplying the opposite bin polynomials and summing accepted pairs are negligible. The major density error just proved has transform $O(\ell^{-2}\min(X,|\beta|^{-1}))$. Grouping the reduced numerators **before** taking absolute values, the local arithmetic factor, complete real overlap and remainder are now exactly the calculation of §3 of the fixed-split local law: the numerator sum is $c_q(N)$ and $\|c_q(N)\|_{\ell^2(N)}/\varphi(q)^2\ll_\eta\sqrt X\,q^{-3/2+\eta}$ on squarefree $q$; the discrete errors and radius-extension tails are negligible. Hence the accepted actual coefficients have local term

$$
                   \Sigma(N)B_{\mathcal J}(N)D_{\mathcal A},
          \qquad D_{\mathcal A}=\sum_{(i,j)\in\mathcal A}c_id_j
$$

with error $O(X^{3/2}\ell^{-1})$ in target $\ell^2$ norm. The actual divisor floors, fixed physical windows and weak diagonal are restored with only the explicit errors above.

## 3. Peeling the short signed factors without changing the tag law

Allowing the continuous diagonal $\gamma+\gamma'\ge20$ instead of complete acceptance changes $D_{\mathcal A}$ by $O(\ell^{-1})$, from $O(\ell)$ boundary bins of absolute scalar size $O(\ell^{-2})$. After (5), this continuous scalar is the two-arm real area of the sign theorem, but with each lower reciprocal term weighted by its own $\varrho_{+,K(W)}(1/2-\log(sW)/L)$. For fixed short $z,w$ the normalized area is $\tfrac12(\delta-(\log z+\log w)/T)_+^2$, since the triangle is inside $[0,a]\times[0,b]$ by $\delta<\min(a,b)$. Thus no exposed label outside the fixed cap is needed.

Write $W=W_{\rm l}W_{\rm h}$ at $e^{AT}$. The lower part is below every tag and both deleted neighborhoods for large $X$, and is available in $W$ throughout the split range. In particular $K(W)=K(W_{\rm h})$ **exactly**, also when a genuine upper tag count is required. The signed area labels are divisors of $sW_{\rm l}$, since any higher prime would give zero area. In this real scalar only, peel the low factors using the positive labeled law. Its total lower mass is $O(\ell\tau)$ and the density bound is $O(\tau^{-1})$. Normalize the lower positive measure by its full product, doubling occupation on the low log-ratio band as before. The moment of $2^{\omega(W)}$ is $O(\ell)$ uniformly: its normalized product is bounded by $\exp(\sum \nu_p/p)$ with $\nu_p$ the doubled weights there and one elsewhere. Exchanging the actual $2\log\ell$ total count for a temporary $3\log\ell$ low-part cap, and later releasing that cap, therefore incurs relative mass $O(\ell^{1-2\log 2})$. This upper comparison keeps all active labels and uses only positive bounds on the errors.

During this temporary restriction $\log W_{\rm l}=O(T\log\ell)$. The difference of the true size gate and the size gate on $W_{\rm h}$ alone is confined to a log strip of this width. Mark one high factor in $\log W_{\rm h}=\sum_{p\mid W_{\rm h}}\log p$ on that strip, where $\log W_{\rm h}\gg L$, and use $\sum \nu_p\log p/p=O(1+T\log\ell)$ in the permitted log interval at fixed other factors. This bounds the normalized mass error by $O(\log\ell/\ell)$, by the same positive product estimate (even without the high tag restriction in the upper error). The Lipschitz bound for the **same** $K(W_{\rm h})$ allows removal of $\log(sW_{\rm l})/L$ from its density argument with error $O(\tau^{-1}\log\ell/\ell)$ before multiplying the lower profile and $\ell^{-1}$. All density arguments used up to this point stay in $[.4,.6]$, including on the temporary comparison where $W_{\rm h}\le X^{\epsilon/2}$ and the added lower logarithm is $o(L)$. Thus the total error is $O(\log\ell/\ell)$ at the normalized scalar scale. This proof of peeling neither modifies the tag gates in the surviving high density nor assumes that an upper rough distribution is unaffected by different high $W$ counts. The same bounds apply without label multiplicities to (1).

After peeling, both arms share the same positive high normalization, including $\varrho_{+,K(W_{\rm h})}(1/2-\log W_{\rm h}/L)$ and the true high size gate. That normalization, including the unmarked low Euler product and $|\mathcal J|/\ell$, times the old $s$ reciprocal mass equals $\mathcal C_{X,Z}$ with error $O(X(\ell^{1-2\log2}+\log\ell/\ell))$. For each low divisor prime, presence with its genuine minus sign costs $-1/(p+1)$ under the exact reciprocal occupation law. Thus the detached signed measure in each arm is the same as in the sign theorem, namely the convolution of the old two-point signed measure at $0,\log s/T$ with the elementary factors $\delta_0^{\rm atom}-(p+1)^{-1}\delta_{\log p/T}^{\rm atom}$ for $e^{4T}\le p\le e^{AT}$. In the pair, convolution exponential replaces the elementary factors with coefficient $-2$ and exponentially small total variation error, and reciprocal PNT in the normalized fixed log bands gives arbitrary inverse log error against the bounded-variation area and its translates, with only finitely many nonzero convolution orders. The old $s$ variables have exactly the same limiting law $du/[u\log(7/5)]$. These replacements give precisely $\Psi(\delta)$, uniformly in the allowed variable split because none of the low Euler factors or old primes depends on that split. Consequently

$$
       D_{\mathcal A}
          =\left(\mathcal C_{X,Z}/|\mathcal J|\right)^2
                   \Psi(\delta)+O(\ell^{-1/10}).
$$

The rational local factor has $\ell^2(N)$ norm $O(\sqrt X)$ and the overlap is $O(X)$, so the scalar error, all seam errors, and the first three signed rows give (2) on squaring. At the exact fixed zero this removes the entire comparator. Away from its zeros, the uniform positivity of (1) and the even singular-series lower bound give the respective sign consequences exactly as in the fixed-split law: use the order-$X$ overlap in the interior, or remove endpoint strips of width $X\ell^{-1/15}$ and apply the square estimate to the remaining wrong signs. In particular no pointwise statement is obtained at an exceptional target.
