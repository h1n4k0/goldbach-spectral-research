# A common curved containing sign for actual target-selected floors

Use the [fixed-floor curved containing calculation](r107-source-curved-containing-fixed-box-sign.md), including its hard physical interval $\mathcal J$, even target interval $\mathcal X$, $L=\log X$, $\ell=\log L$, $T=L/\ell$, and $T_N=\log N/\log\log N$. Keep the same genuine carrier: $n=hF,m=kG\in\mathcal J$, $n+m=N$, actual squarefree $N$-units, $F=P^+(n),G=P^+(m)$, and each cofactor of the form $sV$ with $5T/4\le\log s\le7T/4$ and all primes of $V$ at least $e^{4T}$, permitting the wing $V=1$. Keep the genuine root floors $F\ge\sqrt N e^{-aT_N}$ and $G\ge\sqrt N e^{-bT_N}$, and all literal divisor tests using $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor$, $Q_N=\lfloor N e^{-20T_N}\rfloor$. Only the floor parameters may now be chosen independently at each target, in a fixed finite box $0\le a,b\le A_0$.

Keep the exact definitions of $V_f(N;a,b)$, the forbidden retained-long correction with exterior plus, and $U(N;a,b)$, the uncurved product of the two actual long containing traces with exterior minus. These are in the two-full Walsh channel $\mu(h)\mu(k)$. The exact curved containing-containing term is $V_{\rm curv}=U+V_f$, with the original strict product test; no ordinary divisor row is included. Let $I_N=\Sigma(N)B_{\mathcal J}(N)$, and use **the same** real functions $C_a(g),c_a,f(a,b)$ of (1) in the fixed-floor result. In particular the model depends on the actually selected $a,b$ and not on rounded floor values.

**Theorem (unconditional).** With a constant depending on the fixed box,

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
 \sup_{a,b\in[0,A_0]}
 \left(
  \left|V_f(N;a,b)-\frac{I_N}{\ell^2}f(a,b)\right|^2
  +\left|U(N;a,b)+\frac{I_N}{\ell^2}(1/2-c_a)(1/2-c_b)\right|^2
 \right)
 \ll_{A_0} X^3\ell^{-6}.                                      \tag{1}
$$

Hence there is **one** exceptional set of size $O_{A_0}(X/\ell^2)$ in any fixed interior subwindow, outside which $V_{\rm curv}(N;a,b)\le -c X/\ell^2$ for every pair in the box, with a fixed $c>0$ depending only on the interior subwindow and its physical normalization. This follows from the absolute strictly negative curved comparator of the fixed-floor calculation, with no loss in the exceptional count from choosing the floors. The squared norm is of order $X^3\ell^{-4}$ for any selection of floor pairs on the targets. Neither a moving box growing with $X$, a pointwise bound at a prescribed exceptional target, the remaining signed rows, the full original sum, nor Hypothesis S is estimated here.

## 1. Make disjoint joint cells of actual labels and actual roots

The [semiprime wing identities](r105-source-semiprime-wing-and-containing-contrast.md) apply before taking any model. If a composite arm has root $F$, its signed long containing trace is exactly $\sum_{Fz\le D_N}\mu(h)\mu(z)\log(h/z)$ by the zero full cofactor orbit. All its nonlong labels are retained. A wing has the lone nonzero long containing mark at $F$, whose Walsh-marked value is $+\log s$. In a wing $F>\sqrt N$ and $F(D_N+1)>Q_N$, regardless of $a$ or $b$, so it never enters $V_f$. This is also why the physical wing arm is independent of the selected floors.

On each composite arm let

$$
       u=\frac{L/2-\log F}{T},\qquad
       g=\frac{L/2-\log(Fz)}{T}=u-\frac{\log z}{T}.
                                                                    \tag{2}
$$

The actual floor is $u\le a+O_{A_0}(1/T)$, uniformly in $a,N$. This follows directly by writing the exact upper threshold as $(L/2-(\log N)/2+aT_N)/T$. The actual forbidden pair is within distance $O(1/T)$ of the comparison triangle $0\le g,g'\le20,\ g+g'\ge20$ and has the same inequalities away from that boundary; each forbidden label is less than $\sqrt N$ by $Q_N/(D_N+1)<\sqrt N$. The nonlong composite trace is $g\ge20+O(1/T)$ with the true weak $Fz\le D_N$ boundary. Any such term has $g\le u\le A_0+O(1/T)$. Enclose all these composite descriptions in fixed bounded $g,u$ intervals, including their slivers and with endpoints independent of the target. All corresponding $h,F$ are $X^{1/2+o_{A_0}(1)}$, and $z\le e^{O_{A_0}(T)}$. In particular the fixed short-label block of the [split-free composite estimate](r104-source-split-free-composite-collision-law.md), §1, still suffices. Enlarging a fixed box if necessary, we may take $A_0\ge1$.

Put $\delta=\ell^{-3}$ and $\eta=\ell^{-6}$. Take a label grid with intervals of comparable width $\delta$, splitting at $0$ and $20$ and enclosing the above range. Take a root mesh $0=a_0<\cdots<a_M=A_0$ with gaps comparable to $\eta$. On the nonnegative part of the label grid use disjoint bins $B=(b_-,b_+]$ with $b_-\ge0$; bins touching $g=0$ will in any case be treated at the literal seam whenever needed. Take disjoint root intervals $J=(a_{j-1},a_j]$. For $g>0$ there is **no** omitted initial root interval: (2) gives $u\ge g>0$. The equality case $g=0$ is accounted for in the existing positive seam bins. With these endpoint conventions the nominal root test $u\le a_j$ on the modeled bins is precisely the first $j$ root intervals, including any root on the endpoint. The label and root coordinates are actual integer predicates, not separately sampled real cutoffs.

For a pair of bins $(B,J)$ let $A_{B,J}(\theta)$ be the canonical composite Fourier arm with hard $hF\in\mathcal J$, the two actual bin conditions of (2), and mark $\mu(h)\mu(z)\log(h/z)$. In this one-arm polynomial only the target-unit condition is suppressed; it will be restored uniformly. Use the common auxiliary arc model $H(\theta)$ of the [first curved collision calculation](r106-source-curved-containing-forbidden-collision.md): on the reduced arc $c/q+\beta$ it is $(\mu(q)/\varphi(q))\widehat J(\beta)$, with $\widehat J$ the window transform, and off the auxiliary majors it is zero. This same $H$ applies to every bin and to the wing, with $\|H\|_4\ll X^{3/4}$. Choose a sufficiently large fixed auxiliary exponent; it can depend on the box and precision.

## 2. Sum the one-arm error over both bin axes

If $J=(a_{j-1},a_j]$, put

$$
      m_{B,J}=-\frac1\ell\int_B
                     \bigl(C_{a_j}(g)-C_{a_{j-1}}(g)\bigr)\,dg .
                                                                    \tag{3}
$$

We prove the two summed budgets

$$
  \sum_{B,J}\|A_{B,J}-m_{B,J}H\|_4\ll_{A_0}X^{3/4}\ell^{-2},
  \qquad \sum_{B,J}|m_{B,J}|\ll_{A_0}\ell^{-1}.                    \tag{4}
$$

The second follows directly from the fixed-floor formula for $C_a(g)$: use its two nonnegative integrands separately before applying the two signs. At fixed old-prime log $t$, marked product log $\lambda$, and old-prime label choice $j_0\in\{0,1\}$, the disjoint $J$ test is on $u=g+\lambda+j_0t$; summing across both axes integrates $g$ over a single bounded interval. The positive $\mathcal P$ and old-prime log measures on this compact integration range have bounded mass. Thus the sum in (3) does not grow by the number of root endpoints.

For the first budget, separate the root and subtract strict rejection $F<P(h)$ and repeat $F\mid h$, exactly as in the first curved calculation. The separated rooted bin with both cuts is a **difference of two** separated fixed-floor bins (with upper cut $u\le a_j$ and $u\le a_{j-1}$ respectively). Both fourth norms are $O_{A_0,K}(X^{3/4}\delta\ell^{-K})$ for every fixed $K$, by the split-free signed estimate, uniformly in the hard endpoints. This difference suffices because its main term is zero, not because the full comparison errors at two nearby floors are small. These norms sum negligibly across $O_{A_0}(\delta^{-1}\eta^{-1})$ cells on choosing $K$ large. Repeats are also negligible after this sum: as in the fixed-floor proof, they have form $d_0 F^2$ with $\log d_0\le(2A_0+1)T$, support size $X^{1/2+o_{A_0}(1)}$, and polylogarithmic coefficient bound, giving fourth norm $X^{3/8+o_{A_0}(1)}$ per cell. The disjoint strict rejection has a unique $P=P(h)>F$ and $h=sW_1W_0P$, $z=s^{j_0}W_1$, with the precise sign $(-1)^{j_0}\mu(W_0)$.

We need a stronger total error on this last strict part than would follow by taking differences of the earlier fixed-floor comparison errors. Apply Siegel–Walfisz on $F$ at fixed $h,z$, with both actual bins, hard physical interval and strict $F<P$, then reciprocal prime number theorem on $P$ at fixed physical $x=hF$ and low factors. These are exactly the two major-arc steps of the fixed-floor proof, except that a further fixed interval clips the prime $F$; each prime problem still has a hard interval and a bounded-variation mark. All factors in the cofactor are greater than a polylogarithmic denominator, so the reduced factor is still $\mu(q)/\varphi(q)$. The arbitrary inverse-log errors are uniform on the new exact endpoints. The hard minor proof likewise has the same three coupled tests $hF\in\mathcal J$, $Fz$ in its integer bin, and $F<P(h)$ separated at $P(h)-1/2$. The additional root bin is simply a fixed hard interval for the prime variable $F$, not another coupled test. The old half-integer Perron separations, near-square-root dyads, and reciprocal-distance bilinear bound therefore give arbitrary inverse-log fourth errors on the minors. All these errors remain negligible after summing the polynomial number of cells.

Here is the strengthened real variation estimate. Fix the actual low data $d=(s,W_1,W_0,j_0)$, put $t=\log s/T$, $\lambda=\log W_1/T$, $\zeta=\lambda+j_0t$, and give those data absolute reciprocal weight $w_d=1/(sW_1W_0)$. After $d\log P=T\,dg$, the real region in the cell is

$$
    g\in B\cap(J-\zeta),\qquad
    \log W_0/T<2g+\lambda+(2j_0-1)t+(\log x-L)/T .
                                                                    \tag{5}
$$

The scalar mark excluding $w_d$ is $R(g,x)=(T/\log P)(\log(h/z)/\log F)=2/\ell+O_{A_0}(\ell^{-2})$. All these ratios use the same log windows as before; at fixed $g$ their product has total variation $O_{A_0}(1/(\ell L))$ in the physical $x$-interval. Set $\lambda_{d,B,J}=|B\cap(J-\zeta)|$ for these fixed data. First freeze the last displacement in (5) at zero, then replace $R(g,x)$ by $2/\ell$. The change of the moving boundary has total length $O(1/T)$ across the physical window, by its monotonicity in $\log x$, so both the supremum and the total variation of the change of integral are $O_{A_0}(1/(T\ell))$ for these fixed data. This assertion follows by integrating the bounded mark on the changing slice of (5), together with the variation of the mark on a common region. It also holds if the unmarked input is the unit. On the now fixed integration region the corresponding error has supremum and total variation $O_{A_0}(\ell^{-2}\lambda_{d,B,J})$. Endpoint jumps from the fixed support in $x$ cost only these same supremum bounds. In particular, estimation of (5) does not take the variation of a discrete prime prefix.

Once this real error is separated, the fixed signed scalar is evaluated by the same reciprocal tuple replacement as in the fixed-floor proof, now with the literal bin $J$ in (5). Equivalently the fixed real scalar for strict rejection is $\ell^{-1}\int_B(C_{a_j}-C_{a_{j-1}})$. Indeed marking $W_1$ opens the positive reciprocal measure, the remaining exact $\mu(W_0)$ gives the signed Dickman cumulative at its affine cap, and $j_0=0,1$ give the two terms. Distinctness across the two prime groups still costs a reciprocal square tail. All low factors survive in the fixed log-ratio range $\log(sW_1W_0)\le(2A_0+1)T$ before the frozen replacement and at most $2A_0 T$ in the nonempty frozen clipped range. The positive bounded reciprocal weight sum $\sum_d w_d=O_{A_0}(1)$ on an enclosing fixed range also counts both $j_0$. Exact integer endpoints are used in the prime replacements, and any equality with the unit atom in the final real integral is a null set of $g$.

It follows, using the common rational numerator factor and the transform bound from supremum plus variation, that the real replacement error in fourth norm on the cell is at most

$$
 X^{3/4}\, O_{A_0}\left(
       \ell^{-2}\sum_d w_d\,\lambda_{d,B,J}
                         +\frac1{T\ell}\right).                    \tag{6}
$$

For the factor $X^{3/4}$ use the integral of the fourth power of $\min(X,|\beta|^{-1})$ and the summable $\sum_q\mu(q)^4/\varphi(q)^3$ as in the first curved proof. Every $B$ and shifted $J-\zeta$ has fixed endpoints at these data. Their intersections are disjoint across the two indices, so $\sum_{B,J}\lambda_{d,B,J}=O_{A_0}(1)$ for each $d$, before its reciprocal weight is integrated. **This is the summable first term** in (6). The second term contributes only $O_{A_0}(\delta^{-1}\eta^{-1}/(T\ell))=o(\ell^{-2})$ after all cells. It absorbs the endpoint motion on every cell without requiring geometric disjointness of the moving boundaries. Subtraction of the strict rejected arm gives the minus in (3). Combined with the already negligible signed rooted, repeated, and discrete errors, this proves (4).

## 3. Arbitrary simultaneous node choices with the actual cuts

First allow any two root nodes chosen at a target, but put their root floors at the nominal thresholds $u\le a_i$ on the left and $u'\le a_j$ on the right. Leave the **actual** $D_N,Q_N$, long residues and units everywhere. Handle target-unit deletions as in the fixed-floor proof: for the fixed enclosing support of all choices, primes shared by the operands divide $N$ and are at least $e^{5T/4}$, so the $O(\ell)$ prime counts $O(X/p+1)$ and the bounded polylogarithmic weights yield $O_{A_0,K}(XL^{-K})$ pointwise. This upper bound is independent of all node choices, also when a wing appears.

For the forbidden term choose a fixed set of label-bin pairs contained in its real triangle and not touching its boundary collar of width $O(\delta)$; choose the collar constant so that all these accepted cells satisfy the actual moving predicates for every target. All remaining possibly contributing pairs are in $O_{A_0}(\delta^{-1})$ label-only cells meeting that collar, including the true outer slivers $g<0$ or $g>20$ and the actual product seam. Retain every one of the true strict and weak integer choices inside them. Their total absolute series at any target is bounded by a sum of positive g-bin pair convolutions, dropping **all** root choices and keeping the common enclosing support. Each g-bin arm has positive fourth norm $O_{A_0}(X^{3/4}\delta)$ by the split-free bin bound. The target norm of this common boundary error is $O_{A_0}(X^{3/2}\delta)$. For the uncurved product omit a collar at $g=20$ in each composite arm, keeping all exact true residue terms there for the corresponding positive error. This is a bounded number of g-bins, against a full positive mate of fourth norm $O_{A_0}(X^{3/4})$, including its possible wing. This again gives target norm $O_{A_0}(X^{3/2}\delta)$ simultaneously. These uses of positivity occur only at the enclosing collars, not in making the signed one-arm approximation.

On every accepted label cell, the two node root cutoffs are now two exact bin prefixes. Let $E_\alpha=A_\alpha-m_\alpha H$ with $\alpha=(B,J)$. For any subset of contributing off-boundary pairs chosen at any target, including the two prefixes, the absolute coefficient error is bounded by

$$
 \sum_{\alpha,\alpha'}
     \left|[E_\alpha A_{\alpha'}+m_\alpha H E_{\alpha'}]_N\right| ,
                                                                    \tag{7}
$$

where $[\,\cdot\,]_N$ takes the $N$-th Fourier coefficient, and the upper sum can use **all** pairs. Its target norm is $O_{A_0}(X^{3/2}\ell^{-3})$ by Hölder, Parseval and (4): the sum of the fourth norms of $A_\alpha$ is at most the sum of the errors plus $\|H\|_4\sum_\alpha|m_\alpha|$. Thus (7) has no factor for the number of choices of two node prefixes. In the uncurved product one can add the genuine wing as a single always-present cell on each side, with scalar $1/(2\ell)$ and fourth error $O(X^{3/4}\ell^{-2})$ from its original asymptotic. This keeps both summed budgets and proves the same common error bound on $U$. The exterior plus of $V_f$ and minus of $U$ remain literal.

The summed node model in (7) compares, respectively, to $f(a_i,a_j)/\ell^2$ and $-(1/2-c_{a_i})(1/2-c_{a_j})/\ell^2$, multiplied by $[H^2]_N$. In fact the root intervals telescope **inside** (3), and passing from accepted label cells to the full triangle or trace domain loses only the label collar of width $O(\delta)$, at uniformly bounded real densities before the factor $\ell^{-2}$. Use the [common reduced-numerator completion](r80-source-local-mean-square-at-sign-transition.md), §3, to replace $[H^2]_N$ by $I_N$ in target norm with arbitrary inverse-log error. This completion is the same for every node pair, so its error is multiplied only by the maximum bounded scalar on the box. All the errors in this section are controlled by common nonnegative majorants in the target $\ell^2$ norm. We have therefore proved the analogue of (1) with a supremum over nominal root cutoffs at the nodes, while never flattening the true moving divisor and product tests.

## 4. Fill the whole box with the true root floors

Given an actual $a\in[0,A_0]$ at a target, take its lower mesh node $a_i$, with the endpoint $A_0$ itself treated as a node. The root predicate differs from its nominal lower node only in one of $O_{A_0}(\eta^{-1})$ fixed enlarged slabs in $u$, of width $O_{A_0}(\eta+1/T)=O_{A_0}(\eta)$, by the exact threshold following (2). Use slabs about the two ends also, to include equality and a displacement beyond a mesh endpoint. The same holds independently on the right. Wings are unaffected by these changes.

For the difference in $V_f$ on a fixed slab, ignore the pair constraints **for an upper bound** only, and dominate absolutely by a positive product of that composite slab arm with a global positive enclosing mate. For the difference in $U$ first use the exact composite nonlong identity and the exact wing mark, and then use the same domination; no uncontrolled full long-orbit sum is used in the positive arm. A slab of width $d=O(\eta)$ has positive fourth norm $O_{A_0}(X^{3/4}(d+1/T))$ with hard physical support and the enclosing short-label cap. This is the same positive prime-slab estimate of the split-free comparison: in the real cofactor argument the clipped root interval has width $O(Td)$ in log, giving $O(d)$ from the $O(\ell)$ positive density and $1/\ell$ normalized Jacobian. With the short labels fixed, translation with the physical variable has total log movement $O(1)$, giving the $O(1/T)$ variation allowance. The far-block atom is negligible even at this width and the same hard minor estimates apply. The polylogarithmic slab precision used here is therefore within that proof. The global positive mate (allowing its possible wing for $U$) has fourth norm $O_{A_0}(X^{3/4})$.

Each such slab product consequently has target norm $O_{A_0}(X^{3/2}\eta)$. The squared norm of the common maximum over the entire list of enclosing slab errors is at most the sum of their squared norms,

$$
                      O_{A_0}(X^3\eta).
                                                                    \tag{8}
$$

This is done for the two axes separately by telescoping the two root changes; the global mate is independent of the floor on the other axis. Hence the number of possible floors on that axis does not multiply (8). All divisor, product, and unit conditions on the original differences remain genuine, and are removed only in the common positive domination. This is a finite positive slab interpolation, not a claimed signed monotonicity in either floor. With $\eta=\ell^{-6}$ its squared cost is precisely the scale of (1).

Finally the model interpolates without any pointwise continuity assumption on the short Dickman factor. In the integral defining $C_a(g)$, for fixed $(t,\lambda,j_0)$ a change of $a$ only clips a $g$ interval of the same width. Using the bounded positive compact reciprocal masses gives $\int |C_a(g)-C_{a'}(g)|\,dg\ll_{A_0}|a-a'|$. Thus both $f$ and $c$ have Lipschitz variation in the fixed box, and the comparator changes by at most $O_{A_0}(\eta |I_N|/\ell^2)$ when choosing the lower nodes, with negligible target norm since $\|I_N\|_{\ell^2(N)}\ll X^{3/2}$. Combining this with (8) and the common node bounds proves (1) over the genuine continuum of floor choices. On a fixed interior even target subwindow $I_N\gg X$ and the fixed-floor deterministic margin is absolute over the box. Apply Chebyshev to the **one** supremum in (1) at scale $X/\ell^2$ to get the common exceptional set and the asserted signed bound.
