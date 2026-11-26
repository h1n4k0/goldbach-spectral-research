# A stretched-exponential gain for actual full-cofactor Walsh channels

Use the seven true signed rows, their intrinsic bits $\mathbf b_j$, and the unnormalized actual Walsh coefficients $W_j^{\mathbf u}$ of the [Walsh theorem](r96-source-walsh-two-full-and-dominance-switch.md). All its physical, split, squarefree, unit, prime-floor and long/product conditions are imposed here, including the original hard comparisons at every endpoint. In particular $0\le a,b\le A_0$ for fixed finite $A_0$, $Z_0\le Z\le X^{\delta_0}$, and the tag is the old typical count of the **entire** cofactor product $WU$, not of either split factor. Let $m_j(\mathbf u)$ be the number of ones in $\mathbf b_j+\mathbf u\pmod2$, so that $m_j(\mathbf u)$ is exactly the number of full-cofactor signs present after Walsh projection. The result below concerns $m=m_j(\mathbf u)\in\{1,2\}$, with its same zero comparator.

**Theorem.** There is a fixed $c>0$ such that with $\ell=\log\log X$ and $g_\ell=\ell^{-1/10}\exp(-c\sqrt{\log\ell})$, at fixed common $a,b,Z$,

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
       \max_{\substack{j,\mathbf u\\m_j(\mathbf u)=m}}
                  |W_j^{\mathbf u}(N;a,b,Z)|^2
                  \ll X^3 g_\ell^{2m}.                             \tag{1}
$$

With common fixed floors and a genuinely target-adaptive split the squared maximum is $O(X^3 g_\ell^m)$. With all three parameters independently target-adaptive, it is

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
       \sup_{\substack{a,b,Z,j,\mathbf u\\m_j(\mathbf u)=m}}
                  |W_j^{\mathbf u}(N;a,b,Z)|^2
                  \ll X^3 g_\ell^{m/2}.                            \tag{2}
$$

Constants can depend on the fixed carrier and $A_0$. The matching comparator and its [raw Euler bound](r97-source-matching-walsh-raw-euler-rate.md) are unchanged. As a separate consequence, the same simultaneous conditioned/parity-summed winner switch on the fixed high rectangle of the Walsh theorem holds off one even exceptional set of size $O(Xg_\ell^{1/2})$ in any fixed interior physical target subwindow, or $O(Xg_\ell^{1/6})$ on the full window. No statement applies to a prescribed exceptional modulus, an unbounded floor box or Hypothesis S.

## 1. Anatomy of the signed bin

Use the hard bins, major real densities and unchanged minor split of §2 of the [actual four-parity law](r89-source-four-actual-parity-phases.md), and the original carrier of the [growing-residual theorem](r75-source-dynamic-giant-growing-rough-residual.md). Write $L=\log X$, $T=L/\ell$, $\theta=1/20$, $V_X=\exp(T\ell^\theta)$, $H=\log\ell$, $J_X=\lfloor H/\log H\rfloor$, and $Y_*=\exp(L/(64(J_X+1)))$. The exact stabilized tag interval is $(2V_X,Y_*^{1/2})$; its true accepted count differs from $\mu_0=(1-\theta)H$ by at most $2H^{3/4}$, with the original endpoint convention. The excluded prime bands $[V_X/2,2V_X]$ and $[Y_*^{1/2},Y_*^2]$ remain excluded under every comparison below. The split begins at $Z_0=V_X^2$ and $\tau=(\log Z)/L$. All short labels lie below $M=\exp((24+2A_0)T)$ and use only the old prime $s$ and primes of $W$. In particular they use no tagged prime.

Consider a single ordinary or containing bin with a genuine full sign $\mu(h)$. Condition first on the actual $s,W$ and the short label, and replace the squarefree signed $U$ reciprocal sum by the exact count-restricted real measure $A_{-1,K(W)}$ of (3) of the growing-residual proof. This works uniformly with hard intervals or bounded-variation marks in the compact upper-coordinate range $[.4,.6]$, to arbitrary inverse-logarithmic error. These are the original upper weights $\mu(U)/U$, with any genuine selected tag-count set $K(W)$. The input interval for $v=\log h/L$ at fixed physical $x$ and label depends on that label and $x$, not on how the factors are assigned to the two levels. It has width at most $B/L$, $B=T/\ell$. The real prime marks are $\log(Fr)/\log F$ on an ordinary arm or $\log(h/z)/\log F$ on a containing arm, with $F=x/h$, and their scaled $x$-derivatives have uniformly bounded magnitude and variation on that interval. The labels and the signs in these marks do not change.

Perform the following operation in the real expression only: the signed typical-count part equals the signed unrestricted-count expression minus the signed atypical-count expression. The atypical set is the exact complement of the original count interval, each count still an integer; no atom at an endpoint is silently discarded. Neither of these two comparison expressions changes a prime exclusion, the original hard $W$ size or arity cap, or a bin test. This step is valid also after inserting the bounded real derivative mark.

We will bound the size of the real signed bin and of its derivative mark on a common fixed log interval by $O((\ell B/L)g_\ell)$. To track the relative errors, the positive lower labeled reciprocal mass is $O(\ell\tau)$, and the true upper bound and Lipschitz norm for any count set and either sign are $O(\tau^{-1})$ on $[.4,.6]$, by (4) of the growing-residual proof. Before any signed saving their product integrates to $O(\ell B/L)$.

## 2. Atypical counts: preserve the neutral saving, then tilt the true count

Choose the usual neutral band $\mathcal B_0=[\exp((26+2A_0)T),V_X/4]$, which lies inside $W$ at every split, uses no label prime and is strictly below the tag. Write $W=W_0W_1$ according to this band. The count selector of the atypical expression is exactly the selector on the total tagged count of $W_1U$, so it does not change with $W_0$. The short-label eligibility is also unchanged.

Apply the neutral detachment of the four-parity proof with this selector, which is allowed since its density and Lipschitz bounds are uniform for every count set. For completeness the absolute comparison permits each label-eligible lower prime weight at most two; this changes the reciprocal mass by a fixed factor. The normalized moment of $2^{\omega(W)}$ is $O(\ell)$. Replacing the total count cap $\omega(W)\le2\log\ell$ by $\omega(W_0)\le3\log\ell$, and releasing the latter at the end, costs a relative $O(\ell^{1-2\log2})$. In the temporary range the logarithm of $W_0$ is $O(T\ell^\theta\log\ell)$. Shifting the argument of the same upper density and removing $W_0$ from the hard size gate cost a relative $O(\ell^{-1+\theta}\log\ell)$. The bound for the size-gate strip follows by expanding $\log W_1$ and marking one prime on the strip where $\log W_1\gg L$; at fixed other factors its weighted reciprocal prime log sum over a log strip of length $\Delta$ is $O(1+\Delta)$. These are absolute errors before any signed saving. With the same true count of $W_1U$, the detached neutral product has signed-to-positive ratio

$$
 \prod_{p\in\mathcal B_0}\frac{1-1/p}{1+1/p}\ll\ell^{-2\theta}.
                                                                    \tag{3}
$$

After (3), bound the remaining atypical expression absolutely, still imposing atypicality jointly. Let $\lambda_W$ be the unweighted reciprocal prime mass in the true tag at the lower split, and $\lambda_U$ the integral of $du/u$ over its upper real part. These exclude the disallowed bands. No tag lies in the peeled neutral band or among the label primes. Reciprocal PNT uniformly up to the split, and integration above it, give

$$
 \lambda_W+\lambda_U
   =\log\!\left(\frac{\log(Y_*^{1/2})}{\log(2V_X)}\right)+O(1)
   =\mu_0-\log(J_X+1)+O(1).                                      \tag{4}
$$

The split may be inside or beyond the tag interval. Equation (4) applies in both cases.

Tilting each tagged lower prime by $e^t$ changes its positive labeled Euler bound to at most $O(\ell\tau)\exp((e^t-1)\lambda_W)$ for $|t|\le1$. Indeed at a tagged prime the label choice multiplier is one, and the log of the Euler quotient is $(e^t-1)/p+O(p^{-2})$, uniformly also for negative $t$. To bound the positive tilted upper density, mark one upper log coordinate as in (5) of the growing-residual proof. Its indicator has height at most $e^{|t|}$, and the remaining positive unrestricted upper measure has mass at most $O(\tau^{-1})\exp((e^t-1)\lambda_U)$. Dividing by the total coordinate on the same compact range gives this density bound. In both factors it is legitimate to enlarge to unrestricted positive profiles only after keeping the common compact range in the sums where the density is evaluated.

On either of the actual atypical events take $t=\pm H^{-1/4}$ with sign matching the event. The exponential bound for their relative weighted bin densities is

$$
 \exp\!\left\{(e^t-1)(\lambda_W+\lambda_U)
                   -t\mu_0-2|t|H^{3/4}\right\}
                 \ll \exp(-c_1\sqrt H) .                           \tag{5}
$$

Indeed $t(\lambda_W+\lambda_U-\mu_0)=O(H^{-1/4}\log H)$, while the quadratic term is $(\tfrac12+o(1))t^2(1-\theta)H$, strictly smaller than $2\sqrt H$. If a convention includes the equality case in one bound, the same tilt bounds that event. Multiplying (5) by the neutral factor (3), and adding the count and strip errors already accounted for, proves the claimed normalized bin gain for the atypical expression. In particular (5) was not used for a fixed atypical lower count with no upper tilt, which would lose (4).

## 3. The unrestricted signed term at large and small splits

Put $Z_*=\exp(T\ell^{1/4})$. At $Z\ge Z_*$, detach from $W$ all allowed primes between $\exp((26+2A_0)T)$ and $Z_*$. The sole crossed exclusion is the low $V_X$ neighborhood; $Z_*<Y_*^{1/2}$ for large $X$. There is no tag test in this comparison term, and all label primes lie below the detached band. The same count and strip argument costs relative $O(\ell^{1-2\log2}+\ell^{-3/4}\log\ell)$. The signed-to-positive ratio is now $O(\ell^{-1/2})$, since the reciprocal prime mass of the detached band is $\tfrac14\log\ell+O(1)$. The compact density evaluation and mark support are otherwise the same. Both this ratio and the stripping errors are smaller than $g_\ell$.

Suppose now $Z\le Z_*$, so $\tau\le\ell^{-3/4}$. Keep the entire actual lower sum. On the needed upper real arguments $v\le.6$ the unrestricted signed upper measure has the exact convolution

$$
 A_{\mathrm{unrestricted},-}
     =A_\tau*B_{\mathcal E},\qquad
 A_\tau=\exp_*(-\mathbf1_{[\tau,\infty)}(u)\,du/u),\qquad
 B_{\mathcal E}=\exp_*(\mathbf1_{\mathcal E}(u)\,du/u).             \tag{6}
$$

Here $\mathcal E$ is the excluded upper log neighborhood $[\log(Y_*^{1/2})/L,\log(Y_*^2)/L]$ clipped to $u\ge\tau$. The lower $V_X$ band is below $Z_0$. Convolution uses only nonnegative shifts, so the outer true upper comparison bound $.7$ is immaterial on $v\le.6$. Equation (6) follows by multiplying convolution exponentials first on a compact range; it does not assign any positive weights to an excluded prime in the original sum.

For clarity the cumulative of $A_\tau$ is $\rho(v/\tau)$, with $\rho(x)=0$ for $x<0$ and $\rho=1$ on $[0,1]$. By expanding the finite integrals on compact intervals and marking one log coordinate, the absolutely continuous part has density $-\rho(v/\tau-1)/v$ for $v>0$ (zero for $v<\tau$). That is, $x\rho'(x)=-\rho(x-1)$. Then $x\rho(x)=\int_{x-1}^x\rho(y)\,dy$ for $x\ge1$, by differentiation and agreement at one. A first zero would contradict this identity, so $\rho$ is positive, decreasing beyond one, and $\rho(x)\le\rho(x-1)/x$. Iteration gives factorial decay and hence $\|A_\tau\|_{\rm TV}\le2$ including its atom at zero. Its density is smaller than any negative power of $\ell$ for $v\ge.2$ when $\tau\le\ell^{-3/4}$, by the same decay.

The positive $B_{\mathcal E}$ has total mass at most four, and the largest possible step is $\xi=1/(32(J_X+1))$. Its density $b(v)$ satisfies $v b(v)=(\mathbf1_{\mathcal E}*B_{\mathcal E})(v)$. For $v\ge.2$, the right side is bounded by the mass of shifts at least $v-\xi$; these need at least $6J_X$ steps for large $X$. Thus

$$
 b(v)\ll \sum_{j\ge6J_X}\frac{(\log4)^j}{j!}
                     \ll\ell^{-5}\qquad(v\ge.2),                 \tag{7}
$$

because $J_X\log J_X=(1+o(1))\log\ell$. In (6), for a total argument $v\in[.4,.6]$, split convolution at the excluded-measure shift $v/2$. At shifts at most $v/2$, use the rapidly small Dickman density and bounded mass of $B_{\mathcal E}$. At shifts greater than $v/2$, use (7) and the total variation of $A_\tau$, including its atom. The atom of $B_{\mathcal E}$ is included in the first part. The resulting unrestricted signed upper density is $O(\ell^{-5})$ on the compact range. Multiplying by the lower profile and hard bin width gives more than the required saving, without any approximation to the hard lower $W$ gates in this small-split case.

## 4. Fourier norms, common maximum and actual row comparison

The preceding estimates are uniform for the real density and the scaled derivative mark on any common clipped log interval. At two physical points $x,y$, the symmetric difference in these intervals costs at most $O((\ell/L)|x-y|/X)$ by the old positive bound and the log shift of their endpoints. This is negligible at bin density scale $\ell^{-1}g_\ell$; on the common part apply the proved estimate to the difference of marks. With the endpoint jumps of the physical hard window this gives a transform bounded by $O(\ell^{-1}g_\ell\min(X,|\beta|^{-1}))$ at real auxiliary arc offset $\beta$, multiplied by the usual $\mu(q)/\varphi(q)$. The discrete errors and the actual minor arc bound are unchanged: the analytic decomposition in §§2–3 was only in the real comparison, so the hard $hF$ and $Fz$ Perron separations, label coefficients and literal discrete tag are the old ones. Integrating the real fourth powers with $\sum_q\mu(q)^4/\varphi(q)^3<\infty$ proves the signed fourth norm $O(X^{3/4}\ell^{-1}g_\ell)$ on each bin, for either type of arm.

Return to the section-by-section reduction in the Walsh and [seven-row proofs](r95-source-off-axis-right-forbidden-dominance.md). Each accepted hard bin pair is a genuine separated convolution after the harmless unit and window comparisons. With $m$ full signs its target norm is bounded by the product of the two bin fourth norms, $O(X^{3/2}\ell^{-2}g_\ell^m)$. There are $O(\ell^2)$ accepted pairs. The positively bounded actual ambiguous pairs retain every strict or weak integer test, with total norm $O(X^{3/2}\ell^{-1})$, and the floored and unit restoration errors are smaller. Since $\ell^{-1}=o(g_\ell^m)$ for both $m=1,2$, this proves (1).

Use the independent positive upper-axis gap envelopes from the seven-row and matching proofs, with the same original marked threshold $\tau_*=(\epsilon/16)\log\log\ell/\log\ell$. A floor gap of width $d$ costs $O(X^{3/2}(d+\ell/L))$ in target norm. A split gap above $\tau_*$ uses the actual gap prime and upper $W$-failure and has norm $O_A(X^{3/2}(d+L^{-A}))$ for bounded endpoint ratio at most two. On the single initial gap the raw positive bound of the matching proof is $O(X^{3/2}\ell^{-(2\log2-1)})$. All these are pointwise positive envelopes independent of the other axes, and a Walsh factor of modulus one does not affect them. No comparator calibration is needed for a zero-comparator channel.

For a three-axis grid at spacing $\eta=g_\ell^{m/2}=o(\tau_*)$, the squared sum of independent envelopes is $O(X^3\eta)$ because $\sum d^2=O(\eta)$ per axis and the initial gap is smaller. Its $O(\eta^{-3})$ nodes cost $O(X^3\eta^{-3}g_\ell^{2m})=O(X^3\eta)$, proving (2). With fixed floors, use spacing $\eta=g_\ell^m$ instead, so the one-axis node cost is $O(X^3\eta^{-1}g_\ell^{2m})=O(X^3\eta)$ and the actual gaps remain cheaper. The same initial positive envelope handles the stronger two-sign one-axis rate.

Finally, inverse Walsh summation expresses each true parity-resolved row as one fourth of the signed sum of its four actual channels. The matching maximal squared error from the raw Euler theorem is $O(X^3\ell^{-(2\log2-1)/2})$, smaller than $X^3g_\ell^{1/2}$. Equations (1)–(2) therefore bound the squared maximum of the actual conditioned rows' individual comparator errors by $O(X^3g_\ell^{1/2})$; the parity-summed rows are the actual $\mathbf u=(0,0)$ channels, with no extra averaging. On the fixed high rectangle the conditioned $R_f$ gap and the negative parity-summed $D_f$ gap are fixed positive constants times the same $\mathcal N_{N,Z}$, by the seven-row and Walsh theorems. There are only finitely many comparisons and all phase gaps are uniform on that rectangle. On an interior subwindow $\mathcal N_{N,Z}\gg X$ for every split, so Markov bounds the common exception count by $O(Xg_\ell^{1/2})$. For the whole window trim endpoint strips of width $Xg_\ell^{1/6}$, leaving $\mathcal N_{N,Z}\gg Xg_\ell^{1/6}$; the error-square bound then excludes at most $O(Xg_\ell^{1/6})$ further targets. This proves the claimed simultaneous strict comparisons of the actual subrows, not just their model phases, without a conclusion for the rest of the carrier.
