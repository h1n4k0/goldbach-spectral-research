# The double-competitor correction below the cube-root floor

Keep the exact physical window, target dyad, and selected carrier of the [one-third floor result](r112-source-curved-containing-one-third-floor.md). Write $L=\log X$, $\ell=\log L$, $T=L/\ell$, $T_N=\log N/\log\log N$. The genuine operands $n=hF,m=kG\in\mathcal J$, $n+m=N$, are squarefree $N$-units, with largest prime roots $F,G$. Each cofactor has its one prescribed old prime $s$, $5T/4\le\log s\le7T/4$; every other prime in it is at least $e^{4T}$. Retain the semiprime wing, the true root floors $F\ge\sqrt N e^{-aT_N}, G\ge\sqrt N e^{-bT_N}$, and the integer cuts $D_N=\lfloor\sqrt N e^{-20T_N}\rfloor,\ Q_N=\lfloor Ne^{-20T_N}\rfloor$. Use exactly the same $U$ (uncurved two retained-long containing traces, exterior minus) and $V_f$ (their forbidden-product correction, exterior plus), with the two-full Walsh weight $\mu(h)\mu(k)$; $V_{\rm curv}=U+V_f$. No ordinary divisor arm is included.

The previously established refined single-competitor density is denoted by $K_a^{(1)}=K_a$ (the [paired-drift definition](r110-source-curved-containing-paired-drift.md)). Its formula can be continued to the slightly enlarged box below. Define the **new** double-competitor density as follows. Let $S(w)=\rho_+(w/4)$ be right-continuous and zero for $w<0$, where $\rho$ is the Dickman function, including $S(0)=1$. Write $\mathcal P=\exp_*(1_{v\ge4}\,dv/v)$, a positive locally finite convolution measure with unit atom at zero and density at most $1/4$ away from it, as in the [fixed-box argument](r107-source-curved-containing-fixed-box-sign.md). For $g,\lambda,w\ge0$, $5/4\le t\le7/4$, $j=0,1$, put

$$
 \begin{split}
 u_j&=g+\lambda+jt,\qquad D_{f,j}=\tfrac12-u_j/\ell,\\
 S_j^*(w)&=\tfrac12+[g+(j-1)t-w]/\ell,\\
 Z_j^{(2)}&=3g+2\lambda+(3j-1)t-\ell/2,\\
 R_j^{(2)}(w)&=
    \frac{1/2+g/\ell}{\ell D_{f,j}S_j^*(w)}
       \log\frac{S_j^*(w)-D_{f,j}}{D_{f,j}}
       \qquad (0\le w\le Z_j^{(2)}),\\
 K_a^{(2)}(g)&=
   \int_{5/4}^{7/4}\frac{dt}{t}\int_{[0,\infty)}d\mathcal P(\lambda)
    \sum_{j=0}^1(-1)^j 1_{u_j\le a}
     \int_{[0,Z_j^{(2)}]}R_j^{(2)}(w)\,dS(w).
 \end{split}                                                       \tag{1}
$$

An integral over a negative upper cap is zero. The formula is used only on active caps. The cap endpoint itself has mark zero. Set $J_a=K_a^{(1)}+K_a^{(2)}$, $D=\{0\le g,g'\le20,\ g+g'\ge20\}$, $I_N=\Sigma(N)B_{\mathcal J}(N)$, and

$$
 \mathfrak F_\ell(a,b)=\iint_D K_a^{(1)}(g)K_b^{(1)}(g')\,dg\,dg',
 \qquad
 \mathfrak U_\ell(a,b)=
 \left(\frac{1}{2\ell}-\int_{20}^\infty J_a(g)\,dg\right)
 \left(\frac{1}{2\ell}-\int_{20}^\infty J_b(g)\,dg\right).
                                                                    \tag{2}
$$

**Theorem (unconditional).** There is a fixed absolute $\epsilon_*>0$ such that, for $0<\epsilon\le\epsilon_*$, put $c=1/6+\epsilon$ and $A=c\ell+1/T$. On this larger box,

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
  \sup_{0\le a,b\le A}
   \left(
      |V_f(N;a,b)-I_N\mathfrak F_\ell(a,b)|^2
      +|U(N;a,b)+I_N\mathfrak U_\ell(a,b)|^2
   \right)\ll X^3\ell^{-6}.                                        \tag{3}
$$

Moreover $\mathfrak U_\ell-\mathfrak F_\ell\gg\ell^{-2}$ throughout the box. Thus on each fixed physical interior, one common exceptional set of $O(X/\ell^2)$ even targets suffices for $V_{\rm curv}(N;a,b)\le -c_0 X/\ell^2$ simultaneously for all independent choices of $a,b$ there, with a fixed $c_0>0$. The squared norm on the targets for any such selection has order $X^3\ell^{-4}$. The box includes the **exact** selectable root floor $N^{1/3-\epsilon}$ on either side, by $a=(1/6+\epsilon)\log\log N$ or likewise for $b$. There is no separate sign claim for $V_f$, no conclusion on another Walsh row, and no consequence asserted for the full pair sum or Hypothesis S.

## 1. Exact inclusion and exclusion for the first overlap

Use actual $u=(L/2-\log F)/T$, $g=(L/2-\log(Fz))/T$ where $z\mid h$ is the label in the containing trace. The physical floor normalized to $u$ moves by $O(1/T)$ on the entire box since $A=O(\ell)$; other walls from $D_N,Q_N$ also move by $O(1/T)$ in these coordinates. As in the one-third proof, complete the composite containing orbit to its exact signed nonlong complement $Fz\le D_N$. For $V_f$ keep the actual two long-divisor tests and product cap. The [genuine semiprime wing](r105-source-semiprime-wing-and-containing-contrast.md) contributes the same positive $+\log s$ long mark independent of these floors, with no $V_f$ term since $F(D_N+1)>Q_N$. Neither operation changes when $a$ or $b$ increases.

For the proof first allow $0<\epsilon\le 1/100$, using only absolute constants up to the final reduction of this upper bound. On a nominal cell $u\le A$, $F\ge e^{-1}X^{1/3-\epsilon}$. A padded positive enclosure with $g,u\ge-1$, $g\le\max(20,A)+2$ and $u\le A+2$ has $F\ge X^{1/3-\epsilon-o(1)}$. Four factors of that size counting multiplicity exceed the window. Consequently if $F\nmid h$ in the separated arm, there are $r\in\{0,1,2\}$ strictly larger prime competitors in $h$; its canonical largest-root indicator is **exactly** $1-r+\binom r2$. Compute the two subtraction arms with one selected $P>F$ or one unordered distinct pair $P,Q>F$, always genuine primes of the cofactor. In the first arm a second larger prime may be in the remaining unmarked group. It is not excluded.

One can apply separated-minus-single-plus-double on squarefree cofactors $h$ without first enforcing $F\nmid h$, and subtract the resulting spurious repeated-root terms as an error. Indeed $F|h$ forces the operand to have shape $dF^2$ with $d\ll X^{2c+o(1)}$, $F\ll X^{1/2+o(1)}$. Support $O(X^{1/2+2c+o(1)})=O(X^{5/6+2\epsilon+o(1)})$, and fixed polynomial-in-$L$ coefficients, give Fourier fourth norm $O(X^{5/8+3\epsilon/2+o(1)})$, even for each repeated-term part by supremum and Parseval interpolation. This is negligible after every cell is counted. All multiplicities, including ordered labels and the two competitor arms, are fixed powers of $L$, since the old prime is unique and each remaining prime has log at least $4T$. The positive enclosure counts at most three separated roots, and does not use a unique prime-orbit subtraction.

With $t=\log s/T,\lambda=\log W_1/T,w=\log W_0/T$, in the unsifted rooted arm $h=sW_1W_0$, $z=s^j W_1$, the Walsh sign is $-(-1)^j\mu(W_0)$. Each selected competitor has size strictly above $F$, so cannot divide $z\ll X^{c+o(1)}$; this also applies to both competitors. The single and double representations are necessarily $h=sW_1W_0P$ and $h=sW_1W_0PQ$ and have signs $+(-1)^j\mu(W_0)$ and $-(-1)^j\mu(W_0)$, respectively. They are subtracted and added, respectively. Hence the model from the two rejections together is $-K_a^{(1)}-K_a^{(2)}$, not their difference.

If an actual forbidden label is retained-long on both sides and the product cap holds, its $g$ is in $[0,20]$ up to $O(1/T)$. No such label can occur with two strict competitors in that arm: $hF\ge zFPQ>zF^3=(Fz)F^2$, of size at least $X^{1/2+2(1/3-\epsilon)-o(1)}>X$ by a fixed power. This uses the genuine distinctness of the selected primes and the label, and also applies on its thin geometric collar. The double model will independently be absent from the same strip.

## 2. Real double-competitor model on hard cells

Use the auxiliary arcs and $H=(\mu(q)/\varphi(q))\widehat J_{\mathcal J}(\beta)$ on their reduced major fraction $a_0/q+\beta$, zero elsewhere, with arbitrary fixed polylogarithmic denominator cap $P_{\rm arc}$ as in the one-third proof. In all occupied cells $\log F,\log h$, and any selected competitor logs, lie between $.30L$ and $.70L$ for sufficiently large $X$; here it is only $h$, not the remaining factor after all primes are removed, that must satisfy this bound. The cofactors are prime to all $q\le P_{\rm arc}$. For every fixed $h,z$ and fixed selection, Siegel–Walfisz in $F$ is on an interval (including optional $F<P$ and $F<Q$); thus the reduced numerator factor is identical for all arms. Across the physical variable $x=hF$ the resulting density has reciprocal cofactor factor $1/h$, and weight $\log(h/z)/\log(x/h)$. Abel handles the prime mark and the phase with only fixed $L$-powers; a fixed dyadic prime sum error relative to the interval ambient length, not relative to a possibly tiny interval, suffices. Summing errors over cofactors costs only $L^{O(1)}$ after the $1/h$ bound and polylogarithmic label multiplicity, so the absolute major comparison on each arc can be made $O_B(X L^{-B})$ for any fixed $B$.

On minors fix the selected competitor(s) as part of the cofactor/label coefficient. The threshold is a single literal $F<P$ or $F<\min(P,Q)$ (neither for the separated arm). The three half-integer Perron cuts for $hF,Fz$ and the latter threshold, with real line $1/L$ and height $X^4$, apply exactly as in the one-third proof. A root slice in $F$ itself is a hard interval; a factorization of the cofactor is not introduced in the oscillating $e(\alpha hF)$. The $h,F$ dyads satisfy $MK\asymp X$ and both lengths are in the above fixed polynomial range. Thus the same reciprocal-distance Cauchy bound $L^{O(1)}(q^{-1}+K^{-1}+\log(2q)/M+q\log(2q)/X)$ for the squared relative supremum, with $P_{\rm arc}<q\le\lfloor X/P_{\rm arc}\rfloor$, holds for these signed arms and the positive enclosure. Parseval uses $O(X L^{O(1)})$ energy with the valid multiplicity bound. This gives arbitrary fixed inverse-$L$ minor fourth norms relative to $X^{3/4}$.

In the double-major model choose the literal orientation $P>Q$. At fixed $x,Q,s,W_1,W_0$, write $d=sW_1W_0$. After the $F$-comparison, $F=x/(dPQ)$; the hard tests on $P$ intersect to one interval. In particular $P>F$ gives $P^2>x/(dQ)$, $Q>F$ gives $P>x/(dQ^2)$, and the label and root bins just bound $P$ from both sides. Use ordinary reciprocal PNT to replace $1/P$ by $dP/(P\log P)$. At fixed other data the mark has bounded variation in $\log P$ with $\log F,\log P\asymp L$; this bound is uniform for a clipped interval or an empty one. Change variables in this integral from $P$ to $g$, where $Fz=\exp(L/2-gT)$. At fixed $g$, set $y=\log Q/L$ and $\xi=(\log x-L)/L$. The other prime satisfies $\log P/L=S_j^*(w)+\xi-y$, and the remaining hard $Q$ interval is now $D_{f,j}<y<(S_j^*(w)+\xi)/2$: the first inequality is $Q>F$, and the second is $P>Q$ (so $P>F$ then follows). Use reciprocal PNT on this interval. The mark is BV on it with absolute denominators, and the $P$-Jacobian is $dg/(\ell(S_j^*(w)+\xi-y))$. It follows that the resulting positive mark before the signs is

$$
 \frac{1/2+g/\ell+\xi}{\ell D_{f,j}}
 \int_{D_{f,j}}^{(S_j^*(w)+\xi)/2}
       \frac{dy}{y(S_j^*(w)+\xi-y)}
 \quad\text{if }S_j^*(w)+\xi>2D_{f,j},
                                                                    \tag{4}
$$

and zero otherwise. This primitive at $\xi=0$ is exactly $R_j^{(2)}$ in (1). There is no factor of two: the ordered half interval is half of the symmetric two-prime fiber. The active inequality at $\xi=0$ is $w<Z_j^{(2)}$. The mark, extended by zero, is continuous at that wall, and piecewise differentiable in $\xi$ with derivative $O(\ell^{-1})$. This uses $D_{f,j}\ge1/3-\epsilon-O(1/L)$, $S_j^*(w)+\xi\ge 2D_{f,j}$ on the active side, and bounded upper denominators. Over the physical window the mark can thus be frozen at $x=X$ with supremum and total physical variation error $O(1/(\ell L))$ before the positive low-factor integrations. For (4), $x$ and $g$ are fixed during the second reciprocal PNT; the physical phase is not differentiated during either reciprocal PNT.

Here and for the other arms the replacement of low tuple groups is in their real model only. Expand the squarefree tuples symmetrically with factorial denominators in each group. Nonintersection within and across groups can be removed for this approximation at the cost of a reciprocal-square tail, since every prime is $\ge e^{5T/4}$. The same bound removes exclusions of $P$ or $Q$ equal to a fixed low factor, with the stronger lower bound on those primes. The true strict orientation $P>Q$ is kept in the two reciprocal comparisons and there is no arithmetic diagonal contribution. After (4), each low-factor variable at fixed remaining ones and $g$ has hard affine log conditions from the $u$ bin and log-product limits, and the integrated mark is uniformly piecewise smooth BV (including its zero extension); absolute denominator bounds apply wherever the mark is nonzero. Termwise reciprocal PNT and telescoping cost $L^{-B}$ to any fixed order up to polynomial factors: the total reciprocal mass per group before replacement is $O(\log\ell)$ and its tuple first moments are bounded by the two exponential generating sums and their derivatives. This also handles $s$ on its fixed interval using reciprocal PNT in $t$. The true $F|h$ coincidences were bounded in the arithmetic separately in Section 1. The sign and cut within the remaining real groups give exactly $dS(w)$, with its unit atom, and $d\mathcal P(\lambda)$. Their full real alphabets at cutoff $4$ need not be restricted further on an active cap: the low product and the selected primes automatically fit the physical cofactor. The $\xi$-freezing cost, even using both positive low measures through $O(\ell)$, is $O(\ell^{O(1)}/L)$ in physical supremum plus variation, sufficient after any fixed power grid in $\ell$. In the major fourth bound the smooth/step real density error uses the same physical BV estimate as the one-third proof; the arbitrary inverse-$L$ discrete errors use supremum on arcs of total size $L^{O(1)}/X$.

For the separated, positive and selected-single arms the corresponding real calculations survive this enlarged range. At fixed $x$ the separated unmarked log is $\log W_0/L=1/2+\xi+[g+(j-1)t]/\ell$, independently of the marked log. On all occupied slices it lies in a fixed compact subinterval of $(0,.70)$, and the full signed rough Dickman derivative $-\rho(v\ell/4-1)/v$ is smaller than every fixed inverse power of $\ell$. Positive unmarked density is $O(\ell)$, independently of $\lambda$. In the single-selected model $P>F$ still cuts the identical $w<2g+\lambda+(2j-1)t+(\log x-L)/T$. It yields the identical rational mark $R_j=(1/2+g/\ell)/(\ell D_{p,j}D_{f,j})$, now with $D_{p,j}=S_j^*(w)$ on the single cap, and all denominators still bounded above and below. Thus no extra sign or single-cap endpoint is discarded. The positive fourth bounds and separated negligible bound on inverse-$\ell$ cell widths are

$$
 \|A^+_{\rm slab}\|_4\ll X^{3/4}(A+1)(d+1/T),\qquad
 \|A^+_{\rm full}\|_4\ll X^{3/4}(A+1)^2,\qquad
 \|A^{\rm root}_{B,J}\|_4\ll_{B_0} X^{3/4}\ell^{-B_0},
                                                                    \tag{5}
$$

where a slab limits either coordinate to width $d$ and in the last display the implied constant may depend on the requested decay exponent (not the label cell). To see the first from the positive model, fix the marked data and the old placement and clip the unmarked log interval to width $O(d/\ell)$ (total physical endpoint variation $O(1/L)$); then integrate marked mass $O(A+1)$. On the full interval take $d=O(A+1)$. The phase enjoys the usual physical BV fourth integral, and the uniform errors above apply.

## 3. The double profile is small, with a favorable uniform margin

Use $Z_j^{(2)}=3u_j-\lambda-t-\ell/2$. A nonempty fitted cap implies $\lambda\le3\epsilon\ell+O(1)$ and $\ell/6-2\epsilon\ell-O(1)\le g\le A$. Thus $K_a^{(2)}$ vanishes for $0\le g\le20$ for large $X$, with a uniform gap. Let $M=1+\epsilon\ell$; its support in $(g,\lambda)$, using $dg\,d\mathcal P(\lambda)$, has area $O(M^2)$, including the atom. By integration by parts including the atom in the Stieltjes measure, each fitted double inner integral is exactly

$$
 \int_{[0,Z_j^{(2)}]}R_j^{(2)}\,dS
   =-\int_0^{Z_j^{(2)}} S(w)\,\partial_w R_j^{(2)}(w)\,dw .
                                                                    \tag{6}
$$

There is no cap term, since $S(Z_j^{(2)})R_j^{(2)}(Z_j^{(2)})=0$; the formula also covers cap zero. The derivative formula on the active side satisfies $\partial_w R_j^{(2)}=O(\ell^{-2})$. Where both placements fit and $w\le Z_0^{(2)}$, interpolate $j=q\in[0,1]$. Then $D_f$ and $S^*$ vary at rate $O(1/\ell)$, the cap increases at rate $3t$, and the first and second partial derivatives of the rational-log shape are absolutely bounded on the common active positive denominator set. Thus $\partial_w R_1^{(2)}-\partial_w R_0^{(2)}=O(\ell^{-3})$.

Use $\int_0^\infty S(w)\,dw<\infty$. The common interval in (6) costs $O(M^2/\ell^3)$ after pairing. At fixed $(\lambda,t)$, only placement zero can fit singly, on a $g$-strip of length at most $t$, costing $O(M/\ell^2)$. On the extra cap interval $Z_0^{(2)}< w\le Z_1^{(2)}$ of length at most $3t$ inside $w\ge0$, the integrand is bounded by $O(\ell^{-2})S(\max(0,Z_0^{(2)}))$. At fixed $(\lambda,t)$ its integral in $g$ is bounded since $Z_0^{(2)}$ has slope 3, and a negative $Z_0^{(2)}$ where $Z_1^{(2)}\ge0$ costs a bounded strip. This costs $O(M/\ell^2)$ too. In supremum at fixed $g$, use (6) and the mark derivative directly and count marked mass $O(M)$. Consequently

$$
 \|K_a^{(2)}\|_1\ll\epsilon/\ell+\ell^{-2},
       \qquad \|K_a^{(2)}\|_\infty\ll\ell^{-1}.
                                                                    \tag{7}
$$

The **unpaired** cell scalar budget is $O(M^2/\ell^2)=O(1)$, using (6) per placement and summing over the disjoint $(g,u_j)$ cells. This budget is used before pairing model terms against Fourier errors and is distinct from (7).

For $K_a^{(1)}$ use the exact Stieltjes endpoint/decomposition of the one-third proof. On its common cap write $q$ for the interpolated old placement. The derivative identity from that proof has
$D_{p,q}-2D_{f,q}\le-\tfrac12+3a/\ell\le3\epsilon+3/L$.
Thus the **positive** part of the common difference $\partial_w R_1-\partial_w R_0$ is $O((\epsilon+1/L)\ell^{-3})$; its absolute value is still $O(\ell^{-3})$. The endpoint and extra-cap envelopes are unchanged with costs $O(\ell^{-2})$ after integration; the singly fitting derivative contribution, with only placement zero, is still nonpositive. These yield uniformly

$$
 \begin{split}
 \|K_a^{(1)}\|_1+\|K_a^{(1)}\|_\infty &\ll \ell^{-1},\\
 \|K_a^{(1)}-C_a/\ell\|_{L^1([0,20])}&\ll\ell^{-2},\\
 \int_{20}^\infty K_a^{(1)}(g)\,dg
      &\le c_a/\ell+O(\epsilon/\ell+\ell^{-2}).
 \end{split}                                                       \tag{8}
$$

Here the first two estimates use the same absolute derivative accounting: total common area $O(\ell^2)$, fixed-strip common area $O(\ell)$, and the singly fitting strip has width at most $t$ in $g$ at fixed $\lambda,t$ or $\mathcal P$-mass at most $1+t/4$ at fixed $g,t$. The fixed-strip bound applies including the atom at $\lambda=0$. The unpaired single scalar budget is unchanged: its endpoint costs $O(\ell^{-1})$ by the integrable $S(2g+\lambda+(2j-1)t)$ envelope, and its derivative costs $O(\ell^{-2})$ before integrating area $O(\ell^2)$.

The constants on the right of (7) and (8) are absolute for $0<\epsilon\le1/100$. From the [fixed-box estimates](r107-source-curved-containing-fixed-box-sign.md), $\mathfrak F_\ell=f(a,b)/\ell^2+O(\ell^{-3})$ with $|f|<1/20$, and $|c_a|\le17/2041200$. By (7) and (8), each uncurved factor is at least $[1/2-17/2041200-O(\epsilon)-O(1/\ell)]/\ell$. Choose a fixed $\epsilon_*\le1/100$ so small that the absolute combined $O(\epsilon)$ in this bracket is $<1/10$; for all sufficiently large $X$ this yields a uniform positive gap of fixed size times $\ell^{-2}$ after subtracting $\mathfrak F_\ell$. For fixed positive $\epsilon$ the double contribution and the refined single drift are parts of the retained model, not arithmetic errors at scale $\ell^{-3}$.

## 4. Transfer to the exact adaptive row

Use the [adaptive cell argument](r108-source-curved-containing-adaptive-floors.md) as implemented in the one-third theorem: split the $g$ mesh $\delta=\ell^{-6}$ at $0,20$ and the right-closed $u$ mesh $\eta=\ell^{-14}$ at $0,A$. Safe nominal cells number $O(\ell^{22})$. If $\mathcal B$ is a label bin and $\mathcal I=(a_-,a_+]$ a root bin, the canonical signed cell scalar for the composite arm is $m_{\mathcal B,\mathcal I}=-\int_\mathcal B(J_{a_+}-J_{a_-})\,dg$. Section 2 and the repeat norm show that the sum over cells of the fourth errors against $m_{\mathcal B,\mathcal I}H$ is $O(X^{3/4}\ell^{-20})$; Sections 2–3 give $\sum |m_{\mathcal B,\mathcal I}|=O(1)$. Take absolute coefficient errors only after forming each cell product, use Hölder and Parseval, and sum the cell bounds for a target majorant applying to every simultaneously accepted safe cell set. There is no union over floor choices. In $V_f$, the double component vanishes on the forbidden strip on both real and true supports as already proved. For $U$, telescope the whole nonlong composite prefix scalar before multiplying any wing error: the resulting scalar is $O(1/\ell)$ by (7)–(8), whereas the sum of the absolute cell scalar bounds alone would only give $O(1)$. The static wing's Fourier fourth error to $H/(2\ell)$ is $O(X^{3/4}\ell^{-2})$, so all wing cross errors cost $O(X^{3/2}\ell^{-3})$ in target norm. The remaining common rational factor $[H^2]_N$ is replaced by $I_N$ using the [rational completion](r80-source-local-mean-square-at-sign-transition.md), Section 3, at arbitrarily small inverse-log norm.

For exact cuts, collar cells where literal $D_N,Q_N$ differ from the reference labels have $O(\delta)$ thickness. All arithmetic on these cells is kept by positive majorization only: there are $O(\delta^{-1})$ forbidden pair cells and $O(1)$ nonlong seam bins against a positive full mate. By (5) their target norms are $O(X^{3/2}(A+1)^2\delta)$ and $O(X^{3/2}(A+1)^3\delta)$ respectively. Real collars are smaller by the absolute $L^1$ and $L^\infty$ bounds on $J_a$. True $N$-unit masks are restored uniformly before taking the maximum: a shared prime divides $N$, is at least $e^{5T/4}$, and bounds first operands by $O(X/p+1)$. There are $O(\ell)$ candidate primes among the actual operands (or among divisors of $N$ above the threshold) and polylogarithmic label weight. This costs $O_B(X L^{-B})$ pointwise and includes the wing.

For an arbitrary selected floor use its closest lower mesh node in the nominal coordinates. The difference with the actual integer floor is contained in one fixed enlarged root slab of width $O(\eta)$, with the $O(1/T)$ displacement and end slabs included. For each such slab the signed row difference, with all other actual tests kept, is bounded by the positive slab against a positive full mate, completing the composite nonlong identity first in $U$. The wing has no floor difference. The $\ell^2$ maximum bound over $O((A+1)/\eta)$ slabs costs $O(X^{3/2}(A+1)^{7/2}\eta^{1/2})=O(X^{3/2}\ell^{-7/2})$ in target norm for each side. The model floor difference satisfies $\|J_a-J_{a'}\|_1\ll (A+1)|a-a'|/\ell$: at fixed $\lambda,t,j$ the root restriction clips $g$ by exactly this width, the inner marks in both models are $O(1/\ell)$, and the full $dS$ variation is $\le2$. The model interpolation therefore has negligible norm. These comparisons establish (3) with actual floor, divisor and product predicates. In particular the arithmetic compares to the refined model on the whole box, not to fixed-floor approximations.

Finally $I_N\gg X$ on each fixed physical interior for even $N$, and $\|I_N\|_2\ll X^{3/2}$ by the same completion. Chebyshev on the common maximum at a fixed fraction of the deterministic gap gives the claimed single exceptional set and the squared norm scale. Since $\log\log N-\ell=O(1/L)$, the exact below-cube selectable endpoint is inside the allowed mesh box. The correction accounts only for the first distinct-competitor overlap in this prescribed containing-containing block.
