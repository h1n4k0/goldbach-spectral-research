# The four actual parity phases on the bounded moving floor plane

Use the genuine carrier, all the factor exclusions and count gates, and the exact external minus of the [capped long-floor theorem](r85-source-capped-long-floor-orbits.md). In particular let $L=\log X$, $\ell=\log L$, $T=L/\ell$, $T_N=\log N/\log\log N$, $\mathcal J=[X/2,(1+\Delta)X/2]$, and $\mathcal X=[X,(1+\Delta)X]$, with the same fixed parameters and $\theta=1/20$. For even $N\in\mathcal X$ keep $n=hF,m=kG\in\mathcal J$ with $n+m=N$, genuine squarefree $N$-units, the old prime, both excluded neighborhoods, and the actual typical tag count on the whole $WU$ on each arm. Use the true decomposition $h=sWU$ at any real $Z\in[Z_0,X^{\delta_0}]$, where $Z_0=V_X^2$ and $V_X=\exp(T\ell^\theta)$, and the same right-arm decomposition. The two literal prime floors are $F\ge\sqrt N e^{-aT_N}$ and $G\ge\sqrt N e^{-bT_N}$. The divisor tests are $d>D_N,e>D_N,de>Q_N$, where $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$ and $Q_N=\lfloor Ne^{-20T_N}\rfloor$.

Fix a finite $A_0>0$ and let $0\le a,b\le A_0$, including the individual long-floor seams. For $\varepsilon_1,\varepsilon_2\in\{-1,1\}$ denote by $R_{N,Z}^{a,b;[\varepsilon_1,\varepsilon_2]}$ the original sum restricted to $\mu(h)=\varepsilon_1$ and $\mu(k)=\varepsilon_2$. These are actual cofactor indicators, not the signs of the short labels. Let $\mathcal C_{X,Z}$ be the **unconditioned** positive normalization of the [variable split law](r81-source-variable-split-local-sign-law.md), $B_{\mathcal J}(N)=|\mathcal J\cap(N-\mathcal J)|$, and $\Sigma(N)$ the binary singular series.

Use the local signed short-label measure from the capped theorem:

$$
   \nu=(\delta_0-\pi)*\exp_*(-\lambda_A),\qquad
   \pi(dt)=\frac{\mathbf1_{[5/4,7/4]}(t)}{\log(7/5)}\frac{dt}{t},
   \qquad \lambda_A(dt)=\mathbf1_{[4,A]}(t)\frac{dt}{t}.
$$

Here $\delta_0$ in this formula is a unit atom, not the split exponent, and $\exp_*$ is the convolution exponential. Choose the truncation $A>24+2A_0$. All integrals below are independent of such $A$, as their kernels vanish when either short coordinate exceeds $A_0+20$. Let $\Phi$ be the capped coefficient of the unconditioned sum. Define the ordinary and mixed kernels by

$$
 \begin{split}
 P_{a,b}(t,u)
      &=\tfrac12\{(p+q-20)_+^2-(p-20)_+^2-(q-20)_+^2\},
       &p&=(a+20-t)_+,\quad q=(b+20-u)_+,\\
 Q_{a,b}(t,u)
      &=(a-20-t)_+(b+20-u)_+
              +\tfrac12\{c^2-(c+w_0-20)_+^2\},
       &c&=(\min(a-t,20))_+,\quad w_0=\min(20,(u-b)_+).
 \end{split}
 \tag{1}
$$

Write $P(a,b)=\iint P_{a,b}\,d\nu\,d\nu$ and $Q(a,b)=\iint Q_{a,b}\,d\nu\,d\nu$. The latter has the short **containing** label on the left and the ordinary label on the right. Set

$$
 \begin{split}
 \phi_{\varepsilon_1,\varepsilon_2}(a,b)
    &=\tfrac14\{\Phi(a,b)-\varepsilon_1\varepsilon_2P(a,b)
                    -\varepsilon_2 Q(a,b)-\varepsilon_1 Q(b,a)\},\\
 M_{N,Z}^{a,b;[\varepsilon_1,\varepsilon_2]}
    &=\Sigma(N)B_{\mathcal J}(N)
         \left(\frac{\mathcal C_{X,Z}}{|\mathcal J|}\right)^2
                                   \phi_{\varepsilon_1,\varepsilon_2}(a,b).
 \end{split}
 \tag{2}
$$

**Theorem (unconditional).** With constants depending only on the fixed carrier and $A_0$, uniformly for one common choice of $(a,b,Z)$ and any parity pair,

$$
  \sum_{\substack{N\in\mathcal X\\2\mid N}}
    |R_{N,Z}^{a,b;[\varepsilon_1,\varepsilon_2]}
      -M_{N,Z}^{a,b;[\varepsilon_1,\varepsilon_2]}|^2
                      \ll X^3\ell^{-1/5}.
 \tag{3}
$$

The choices can also be independent at each target, in the strong form

$$
  \sum_{\substack{N\in\mathcal X\\2\mid N}}
       \sup_{\substack{0\le a,b\le A_0,\ Z_0\le Z\le X^{\delta_0}\\
                       \varepsilon_1,\varepsilon_2\in\{-1,1\}}}
    |R_{N,Z}^{a,b;[\varepsilon_1,\varepsilon_2]}
       -M_{N,Z}^{a,b;[\varepsilon_1,\varepsilon_2]}|^2
                      \ll X^3\ell^{-1/20}.
 \tag{4}
$$

The four phases add to $\Phi$. At $(a,b)=(0,0)$ they give the coefficient of the [literal giant parity theorem](r88-source-giant-parity-resolved-signs.md), whose separate one-axis maximal rate is sharper. Section 5 gives, in addition, a strict sign of a genuine one-parity contrast outside the common exceptional set. These results do not assert a sign at every target, an estimate for other carriers, or Hypothesis S.

## 1. The exact parity algebra

For a genuine pair use the ordinary labels $d=h/r$ with marks $u_h(r)=\mu(h)\mu(r)\log(Fr)$ and the right analogues. For the containing label $Fz$, with $z\mid h$, write $v_h(z)=\mu(z)\log(h/z)$, so its original mark is $-v_h(z)$. The complete containing sum is zero, since $h$ is squarefree composite; in particular its actual long sum is exactly $\sum_{Fz\le D_N}v_h(z)$, with the stated weak boundary. With the unchanged external minus, the original pairwise expansion thus consists of:
1. the negative ordinary-ordinary row on the three strict tests;
2. the negative mixed rows (one orientation each), each of an ordinary long arm against the sum of the containing nonlong residue and the containing retained-long forbidden product;
3. the positive double-containing forbidden product with both labels long and the negative double-nonlong product.

These are precisely formulas (4)–(5) and the preceding ordinary row in the capped theorem, pointwise on the actual integer pair. They remain identities after either genuine parity indicator is imposed. In particular one does not extend a completed long orbit to a forbidden product or cap it by a prime floor in place of $D_N$.

Squarefreeness gives the exact equalities

$$
 \mu(h)\mathbf1_{\mu(h)=\varepsilon_1}
                        =\frac{\mu(h)+\varepsilon_1}{2},
       \qquad
 \mathbf1_{\mu(h)=\varepsilon_1}
                        =\frac{1+\varepsilon_1\mu(h)}{2}.
 \tag{5}
$$

Use the first identity on an ordinary mark and the second on a containing mark, and similarly on the right. Call a bit with an explicit factor $\mu(h)$ or $\mu(k)$ a full-sign bit; $\mu(r)$ or $\mu(z)$ alone is just the short sign. We prove that all bits with at least one full sign contribute $O(X^{3/2}\ell^{-1/10})$ in target $\ell^2(N)$ norm. The other bits bear exactly the coefficients $-\varepsilon_1\varepsilon_2/4$ in the ordinary row, $-\varepsilon_2/4$ in the containing-left mixed rows, $-\varepsilon_1/4$ in the containing-right mixed rows, and $1/4$ times the original signs in the double rows.

On actual active rows the common fixed cofactor windows may be taken as

$$
    H_-=\tfrac12\sqrt X e^{-20T}\le h,k\le
    H_+=\tfrac12(1+\Delta)\sqrt X e^{A_0T}.
$$

An ordinary long arm forces $h>D_N$. In a containing forbidden product with a long mate one has $Fz\le Q_N/(D_N+1)<\sqrt N$, so that $h$ has the stronger lower bound implicit in $hF\ge X/2$. The same is true if $Fz\le D_N$. The upper bounds use the real prime floors. The cap $M=\exp((24+2A_0)T)$ covers every actual ordinary omission and short containing label, including after the fixed comparisons: $h/D_N\ll e^{(A_0+20)T}$ and $Q_N/(F(D_N+1))\ll e^{A_0T}$, with the single nonlong containing case smaller. All these labels divide the corresponding $sW$ and have bounded arity for fixed $A_0$. A common finite real log-support bound for them is sufficient for every bin below.

For each arm use the fixed prime comparison $F_0(a)=\sqrt X e^{-aT}\le F\le\sqrt X e^{20T}$. The genuine lower floor dominates $F_0(a)$, and differs in log by $O_{A_0}(1)$, by monotonicity and bounded derivative of $y/2-ay/\log y$ for $y=\log N\in[L,L+O(1)]$. Any possible actual prime above the fixed upper endpoint lies in another log-width-$O(1)$ sliver, by $h\ge H_-$ and $hF\in\mathcal J$. Keep the physical interval hard. After these comparisons the cofactor window is automatic at every real physical $x\in\mathcal J$. The choice of distinguished prime is unique in the entire comparison: two primes as large as $F_0(A_0)$ would leave a factor product at most $O(e^{2A_0T})$, inconsistent with a required tagged prime greater than $2V_X$; both large primes are above the tag range. This also excludes repetitions of the distinguished factor in the comparison.

The [finite-orbit fourth-norm bounds](r77-source-finite-short-orbit-product-boundary.md), with the extended support as in the capped theorem, give $O(X^{3/4}\ell/L)$ for a positive all-label arm in a prime sliver and $O(X^{3/4})$ for a full arm. Thus the norm of both floor restoration errors is $O(X^{3/2}\ell/L)$, including after parity restriction. When taking a convolution the $N$-unit masks can temporarily be removed at cost $O_H(XL^{-H})$ per target for every fixed $H$: a bad common prime is at least $e^{5T/4}$, divides $N$ and splits off at most $O(X/p)$ first operands, and there are $O(\ell)$ candidates, with at most a fixed power of $L$ from labels and log marks. Unit and prime-window comparisons are made **after** the exact orbit identities and with positive all-label domination of their errors.

## 2. Full-sign bounds, including the containing arm

Use hard bins of width $1/\ell$ in the ordinary coordinate $(\log(h/r)-L/2)/T$ and the reversed containing coordinate $(L/2-\log(Fz))/T$. The no-full-sign short-signed and positive variants have fourth norm $\ll X^{3/4}\ell^{-1}$ in a bin by the real-density and Perron proof of the finite-orbit theorem. The ordinary full-sign variant has fourth norm $\ll X^{3/4}\ell^{-1-1/10}$ by the [growing-residual neutral band](r75-source-dynamic-giant-growing-rough-residual.md), as used in the capped theorem. We need the **same improvement with an additional $\mu(h)$ on the containing mark**; it is not a consequence merely of (5).

Fix a hard $Fz$ log bin $J$, and on each reduced auxiliary major arc apply Siegel–Walfisz only to the prime $F$ at fixed $h,z$, on the true intersection of $Fz\in\exp J$, the baseline prime interval and $hF\in\mathcal J$. All prime factors of $h$ exceed the polylogarithmic arc denominators. The real mark at $x=hF$ is $\log(h/z)/\log(x/h)$ divided by $h$, with the signs $\mu(h)\mu(z)$. The allowed interval in $\log h$ at fixed $x,z$ is the intersection of the fixed cofactor window, the translated real comparison prime interval, and $\log x+\log z-J$. Its width is at most $B=T/\ell$, and its domain depends on $x,z$ and $h$ as the integration variable, not on an allocation of the lower factors of $h$. The mark without $1/h$ and its scaled $x$ derivative are bounded in supremum and variation as functions of $\log h$ on that interval: the two logs in the quotient are $L/2+O_{A_0}(T)$, and all differentiations are of these real functions on a compact range with $\log(x/h)\gg L$.

At fixed $s,W,z$ replace the actual reciprocal $U$ sum, with full factor sign $\mu(U)$ and its exact upper tag set $K(W)$, by the real measure of the growing-residual theorem. Its signed density $\varrho_{-,K(W)}$ and its log-coordinate Lipschitz norm are $O(\tau^{-1})$, $\tau=\log Z/L$, on the required compact $[.4,.6]$. This replacement works at hard interval endpoints with the stated bounded-variation marks and arbitrary inverse log error. The positive lower labeled reciprocal mass is $O(\ell\tau)$; weighting each prime eligible for a short label twice costs only a constant, by the fixed log-ratio band below $M$. Thus the natural real density bound before a signed gain is $\ell B/L$.

Detach the part $W_0$ of $W$ with primes in $[\exp((26+2A_0)T),V_X/4]$, writing $W=W_0W_1$. Every detached prime belongs to $W$ under every permitted split, is larger than $M$, and is below the tag range and outside the deleted neighborhoods. Therefore the exact count selector $K(W)$ is unchanged and $z\mid sW$ is exactly $z\mid sW_1$; the short sign does not use $W_0$. The interval in $\log h$ above remains literally the same as a real integration interval. The full sign now contributes $\mu(W_0)$.

For clarity, the two cap removals in the neutral-band argument are relative to the positive labeled mass. Replacing the original $2\log\ell$ total $W$ cap by a temporary $\omega(W_0)\le3\log\ell$ costs $O(\ell^{1-2\log2})$ there, from the $O(\ell)$ normalized $2^{\omega(W)}$ moment. On the temporary support put $\Delta_0=3(\log\ell)\log V_X$. Shifting the real density argument by $\log W_0/L$ costs $O(\Delta_0/L)$ relative to $\ell B/L$. The hard size gate on $W$ differs from the gate on $W_1$ only in the strip of width $\Delta_0$ below its original boundary $\epsilon L/2$ in $\log W_1$. Its weighted relative mass is $O((1+\Delta_0)/L)$: expand $\log W_1$ by marking one constituent prime with weight $\log p$ on the strip where $\log W_1\gg L$, fix the remaining factors, and use the Chebyshev bound for $\sum \nu_p\log p/p$ in the resulting log interval (here the label multiplicities are bounded by the same prime weights $1\le\nu_p\le2$). This keeps the real upper count set itself fixed in the shifting step. Releasing the temporary cap on $W_0$ costs the same moment bound. The remaining signed-to-positive Euler ratio is then

$$
          \prod_{\exp((26+2A_0)T)\le p\le V_X/4}
                     \frac{1-1/p}{1+1/p}\ll \ell^{-2\theta}=\ell^{-1/10}.
$$

Its reciprocal prime mass is $\theta\log\ell+O_{A_0}(1)$. Also $\Delta_0/L=O(\ell^{-1+\theta}\log\ell)$. The detached estimate therefore bounds the real containing-bin density by $O((\ell B/L)\ell^{-1/10})$. It also holds with the scaled $x$ derivative mark on any common fixed subinterval in $\log h$.

For variation between two physical points $x,y$, the symmetric difference of the clipped log intervals for each fixed label has length $O(|x-y|/X)$ and is bounded positively, costing $O(\ell|x-y|/(LX))$. On the common part use the preceding signed estimate for the difference of the two marks, by the same uniformly bounded derivative in supremum and variation. Thus the total variation on $\mathcal J$, including its two jumps, has the desired $\ell^{-1-1/10}$ scale for $B=T/\ell$, as $\ell/L$ is negligible. The real arc transform is bounded by this scale times $\min(X,|\beta|^{-1})$ at arc offset $\beta$. The real fourth moment uses $\int_{\mathbb R}\min(X,|\beta|^{-1})^4d\beta\ll X^3$ and $\sum_q\mu(q)^4/\varphi(q)^3<\infty$. The discrete errors are arbitrary inverse powers of $L$ on polylogarithmic arcs.

On the auxiliary minors the two hard half-integer Perron separations of the **integer** products $hF$ and $Fz$ from the finite-orbit proof stay valid. The $z$ twists and $\mu(h)$ are inside the same $h$ coefficient; its bound, the two-factor dyads, and the bounded-arity label multiplicity do not change. The minor supremum is therefore $O_H(XL^{-H})$ for any fixed $H$ after choosing the auxiliary arc exponent large enough, and coefficient energy is unchanged in its upper bound. This proves the improved containing-arm fourth norm on the whole circle. It has not used an equidistribution assumption for arithmetic parity.

The literal log thresholds move by $O(1)$ over the target window. For each signed row there are $O(\ell^2)$ bin pairs, of which only $O(\ell)$ are ambiguous near its coordinate and product lines. Classify accepted and rejected bins using the true integer conditions for the entire window. Within ambiguities keep the original strict and weak tests and bound their coefficients positively. Their total target norm is $O(X^{3/2}\ell^{-1})$ by Hölder and Parseval. Each fully accepted pair is a separated convolution after the harmless unit comparison. A full sign on either side now gives per-pair norm $O(X^{3/2}\ell^{-2-1/10})$, uniformly also on the mixed and double rows with containing signs. Summing proves the asserted total $O(X^{3/2}\ell^{-1/10})$ norm for all full-sign bits of (5).

## 3. The surviving real bin scalars

It remains to evaluate the bits with two short signs and no full cofactor sign. For either type on a fixed bin $I$, let $j$ be the corresponding label $r$ or $z$, and put $t=\log j/T$. The scalar on an arm with floor $a$ is

$$
   c_{a,I}=\frac1\ell
       \sum_{\substack{s,W\\\text{actual lower masks}}}
       \sum_{\substack{j\mid sW\\ j\le M}}
           \frac{\mu(j)}{sW}\,
          \varrho_{+,K(W)}\left(\tfrac12-\frac{\log(sW)}L\right)
                |(I+t)\cap[-20,a]|.
 \tag{6}
$$

The same expression applies to two **different** real coordinates, as follows. Write $\alpha=(L/2-\log F)/T\in[-20,a]$ at physical $x=hF$. For an ordinary arm the actual coordinate is $\gamma=\alpha-t+(\log x-L)/T$. For a containing arm it is $\gamma=\alpha-t$ exactly. Thus the integration in $\alpha$ takes place in the clipped interval in (6), with the ordinary translate additionally shifted by $-(\log x-L)/T$. The Jacobian is $d\log h/L=d\alpha/\ell$. The exact real density argument is $\tfrac12+\alpha/\ell+(\log x-L)/L-\log(sW)/L$. The real prime marks divided by $\log F$ are $1+\log r/\log F$ in the ordinary case and $\log(h/z)/\log F$ in the containing case, both $1+O_{A_0}(\ell^{-1})$. This verifies the common limiting scalar (6) without exchanging ordinary and containing labels.

The real supremum error is $O(\ell^{-2})$ on a bin: combine its $\alpha$ width at most $\ell^{-1}$, the density Lipschitz bound $O(\tau^{-1})$, lower mass $O(\ell\tau)$, and the factor $1/\ell$. The ordinary shift costs only $O(1/T)$. For variation in $x$, the endpoints of the ordinary bin translate by $O(|x-y|/(XT))$ and the containing endpoints are fixed. On the common part, the density changes by $O(\tau^{-1}|x-y|/(XL))$, and the marks in the $\alpha$ variable have change zero (ordinary) or $O(|x-y|/(XL))$ (containing). Combined with the jumps at the physical window these give the same transform error $O(\ell^{-2}\min(X,|\beta|^{-1}))$. The count-restricted prime-product replacement and Siegel–Walfisz errors are arbitrarily inverse-logarithmic. The preceding exact minor separation applies with or without the full sign. In particular $|c_{a,I}|\ll\ell^{-1}$ and the sum of absolute scalar sizes over all bins is bounded.

Apply the rational completion of the [fixed local law](r80-source-local-mean-square-at-sign-transition.md) and the variable split law to the accepted pairs of scalars (6). The real transform at denominator $q$ carries $\mu(q)/\varphi(q)$, so reduced numerators must be summed before absolute values, giving $c_q(N)$. The bound $\|c_q(N)\|_2/\varphi(q)^2\ll_{\xi}\sqrt X q^{-3/2+\xi}$ on the squarefree polylogarithmic range, and its completing tails as in those proofs, give $\Sigma(N)B_{\mathcal J}(N)$ times the scalar product. For the total of all accepted pairs the real transform errors cost $O(X^{3/2}\ell^{-1})$ in norm: each product error has density scale $O(\ell^{-3})$. The scalar sum may now pass to the limiting real regions, since only $O(\ell)$ boundary bin pairs change and each two-bin mass is $O(\ell^{-2})$ even in the positive bound. This gives another $O(X^{3/2}\ell^{-1})$ error using $\|\Sigma\|_2\ll\sqrt X$ and $B_{\mathcal J}\ll X$. The real boundaries themselves have zero area; exact integer equality has already been handled before taking these integrals.

## 4. Areas, short Euler limit, and the joint maximum

In an ordinary-ordinary pair write the two coordinates as $\gamma=\alpha-t,\gamma'=\alpha'-u$ after the controlled physical shifts. The long tests are $\gamma,\gamma'\ge-20$ and the product region is $\gamma+\gamma'\ge-20$. The lower prime comparison $\alpha\ge-20$ imposes only $\gamma\ge-20-t$, already automatic, and likewise on the right. After shifting both coordinates by $20$, the available rectangle has side lengths $p,q$ of (1) and the sum must be at least $20$. Its area is the corner-triangle formula $P_{a,b}(t,u)$ in (1), including if either side length vanishes.

For the containing-left nonlong row the left coordinate $g=\alpha-t$ is at least $20$ and the ordinary right coordinate at least $-20$, giving exactly the rectangle term of $Q_{a,b}$. In the retained-long forbidden row let $g$ denote the containing coordinate and $y=-\gamma'$ the reflected ordinary coordinate. The two long tests are $g\le20,y\le20$ and the forbidden product is $g+y\ge20$. These imply $g,y\ge0$, so the lower endpoints from $\alpha,\alpha'\ge-20$ cannot further restrict the area. The upper endpoint on $g$ is $c$, and the lower one on $y$ is $w_0$, unless the interval is empty (the capped $w_0=20$ gives zero area in that case). For fixed $g\in[0,c]$ its available $y$ length is $\min(g,20-w_0)$, whose integral is the remaining term of $Q_{a,b}$. The containing-right area is the reflection. For the double rows only the coordinates $\gamma,\gamma'\ge0$ appear (indeed both at least $20$ for the nonlong product), and their signed difference is $H_{a,b}$ of the capped theorem. This proves all four area contributions and their actual orientations.

Every area in this proof is uniformly bounded and Lipschitz in the four variables on the fixed supported domain and vanishes when either short coordinate exceeds $A_0+20$. For $P$ this follows from the side-length formula with a zero side, and for $Q$ from either $c=0$ or $w_0=20$ along with the displayed nonlong term. Thus the signed short-prime peeling of the capped theorem applies to each of these new two-variable tests, not just to the double kernel. More explicitly, peel the $W$ primes up to $\exp(AT)$ after (6); they belong to $W$ at every split, lie below the tags and the deleted neighborhoods, and leave $K(W)$ unchanged. The positive moment and hard size strip removal with temporary arity $3\log\ell$ cost $O(\ell^{1-2\log2}+\log\ell/\ell)$ after normalization per arm. The lower labeled reciprocal mass is still $O(\ell\tau)$, with a bounded extra factor for short-label choices. At fixed remaining factors the signed label choice on an occupied low prime contributes the atom at its log position with coefficient $-1/(p+1)$ under the detached positive normalization; the old prime contributes its two signs at zero and $\log s/T$. The difference from the convolution exponential is negligible by $\sum_{p\ge e^{4T}}p^{-2}$ and reciprocal PNT on the fixed log bands, with bounded-variation tests. The cap $j\le M$ cannot remove any surviving area because $\log M/T>A_0+20$. The same positive-factor comparison, without the label test, gives the **same** $\mathcal C_{X,Z}/|\mathcal J|$ per arm as in the capped theorem, with the preceding uniform error. Hence the ordinary and mixed scalars are that common normalization squared times $P(a,b)$ and $Q(a,b)$, respectively, up to $O(\ell^{-1/10})$; the corresponding statement for the double difference is the known $\Phi(a,b)$. Combining with the exact coefficients in §1 gives (2)–(3).

For the joint maximum use the [three-axis positive envelopes of the capped theorem](r85-source-capped-long-floor-orbits.md). Their bounds survive the parity restrictions: on any physical pair the cofactor does not change under varying its floor or split, since the distinguished prime is unique and only the permitted split decomposition changes. The parity and all seven mark formulas are therefore fixed on a pair whenever selected. The same global cofactor window and label cap work for all four masks, and on any affected row absolute domination uses the positive all-label mark, independent of the other mesh axes. For clarity choose mesh spacing at most $\eta=\ell^{-1/20}$ on the two floor axes and on the split exponent above $\eta$, with the initial subpower split gap treated separately. A floor gap of length $d$ has one-axis norm envelope $O(X^{3/2}(d+\ell/L))$ uniformly in the other coordinates; the [marked split gap](r83-source-full-polynomial-adaptive-split.md) gives $O_H(X^{3/2}(d+L^{-H}))$ for exponent length $d$ there, and the [initial subpower comparison](r82-source-target-adaptive-subpower-split.md) gives $O(X^{3/2}\ell^{-1/10})$. These are the same positive envelope bounds, without changing any parity-conditioned main term. The gaps contribute $O(X^3\eta)$ to the square of the joint maximum by summing squared envelopes per axis. The normalization calibration at split gaps is unchanged because $\mathcal C_{X,Z}$ is unconditioned. The Lipschitz kernels in (1) and the capped kernel imply comparator changes $O(X\eta|\Sigma(N)|)$ from a bracket node. Finally there are $O(\eta^{-3})$ nodes and only four parity pairs, so their squared-error budget by (3) is $O(X^3\eta^{-3}\ell^{-1/5})=O(X^3\eta)$. This proves (4) without any regularity of the choices in $N$.

## 5. A strict parity contrast and checks of the normalization

Write $A(x)=\nu([0,x])$ for $x\ge0$ and $A(x)=0$ for $x<0$; in the following deterministic formulas use the local, indefinitely extendible measure (or sufficiently large cutoffs for the displayed arguments). Put $M_1(x)=\int_0^{x_+}A(s)\,ds$. The [Dickman phase theorem](r86-source-dickman-capped-phase-chart.md) gives $A(x)=1$ for $0\le x<5/4$ and $A(x)<0$ for $x>4$. With $C=a+b+20$ the two new scalars can equivalently be written

$$
 \begin{split}
 P(a,b)&=\Psi(C)-\int_0^a A(C-v)M_1(v)\,dv
                   -\int_0^b A(C-v)M_1(v)\,dv,\\
 Q(a,b)&=M_1(a)M_1(b+20)
                 -\int_0^{20}A(a-g)M_1(b+20-g)\,dg.
 \end{split}
 \tag{7}
$$

For the first formula start from the uncapped triangle with coordinates $s=a-\gamma,t'=b-\gamma'$, weighted by $A(s)A(t')$. Its two omitted tails $s>a+20$ and $t'>b+20$ are disjoint on $s+t'\le C$. Each integrates to the stated one-dimensional term. For the second formula the retained-long forbidden triangle has integral $\int_0^{20}\int_{20-g}^{20} A(a-g)A(b+y)\,dy\,dg$; adding the exact nonlong rectangle $M_1(a-20)M_1(b+20)$ cancels its lower primitive term. These Fubini calculations use bounded support in the integration variables.

In particular $P(0,0)=\Psi(20)$, $Q(0,0)=\Phi(0,0)=0$, and each phase at the origin has the sign stated in the literal giant theorem. Uniform continuity gives the same parity sign pattern in a sufficiently small fixed square near the origin. There is also a separate strict **one-parity** signal. For any $0<a\le5/4$ and any $b\ge0$ in the fixed box one has $Q(a,b)<0$: the nonlong rectangle vanishes, the retained-long integral above has $A(a-g)=1$ for $0<g<a$, and there $b+y\ge b+20-g>4$ so the second factor is strictly negative on positive area. The exact right-parity contrast is $\sum_{\varepsilon_1,\varepsilon_2}\varepsilon_2 R_{N,Z}^{a,b;[\varepsilon_1,\varepsilon_2]}$, and its comparator is $-Q(a,b)$ times $\Sigma(N)B_{\mathcal J}(N)(\mathcal C_{X,Z}/|\mathcal J|)^2$. This follows by summing the four exact phase coefficients; it is not a positivity assertion for the mixed mark before its arithmetic averaging. The reflected left-parity contrast uses $-Q(b,a)$.

On any allowed set with phase (or a stated contrast phase) of absolute size at least a fixed $\kappa>0$, (4) supplies its own strict sign and magnitude $\gg_\kappa X$ on each fixed interior subwindow outside a common $O_\kappa(X\ell^{-1/20})$ even exceptional set. Over the whole window the strict signs hold outside $O_\kappa(X\ell^{-1/60})$ even targets by deleting overlap strips of width $X\ell^{-1/60}$ and applying the squared estimate there. These use the actual positive normalization and the positive lower bound for the even singular series. At exact zero phase the statement is cancellation in mean square. The identities for parity sums and contrasts leave the unconditioned conclusion as before.
