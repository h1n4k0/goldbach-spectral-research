# Keep the true tag and gain a log-log power on the moderate subpower splits

Use the [actual Walsh coefficients and intrinsic full-sign bits](r96-source-walsh-two-full-and-dominance-switch.md) of the seven genuine rows, with the same hard interval, exact prime-floor and divisor/product tests, squarefree unit masks and count conditions. As there, fix the carrier parameters and a finite floor range $0\le a,b\le A_0$. Write $L=\log X$, $\ell=\log L$, $T=L/\ell$, $H=\log\ell$, $J=\lfloor H/\log H\rfloor$, and use the original $Y_*=\exp(L/(64(J+1)))$, $V_X=\exp(T\ell^{1/20})$ and $Z_0=V_X^2$. Restrict the true split to

$$
              Z_0\le Z\le Z_{\max}:=\exp\!\left(\frac{L}{8(J+1)}\right).
                                                                    \tag{1}
$$

This lies in the original range for large $X$ and includes splits beyond $Y_*^2$. Define $m_j(\mathbf u)\in\{0,1,2\}$ as the number of surviving full-sign bits in $\mathbf b_j+\mathbf u$ modulo two. Only the channels with $m=m_j(\mathbf u)\in\{1,2\}$ are estimated below; they retain the exact zero comparator. In contrast to the [full polynomial-range estimate](r98-source-tag-full-sign-stretched-cancellation.md), the stronger bound here is obtained with the actual typical count kept intact.

**Theorem.** For either $m=1$ or $m=2$, uniformly at any fixed common $a,b,Z$ as above,

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
       \max_{\substack{j,\mathbf u\\m_j(\mathbf u)=m}}
           |W_j^{\mathbf u}(N;a,b,Z)|^2\ll X^3\ell^{-6m}.          \tag{2}
$$

Put $\sigma=2\log 2-1$. The common genuinely target-adaptive bound on the same restricted split range is

$$
 \sum_{\substack{N\in\mathcal X\\2\mid N}}
      \sup_{\substack{0\le a,b\le A_0,\ Z_0\le Z\le Z_{\max}\\
                                j,\mathbf u,\ m_j(\mathbf u)=m}}
           |W_j^{\mathbf u}(N;a,b,Z)|^2\ll X^3\ell^{-2\sigma}.       \tag{3}
$$

Constants are allowed to depend on the fixed carrier and $A_0$. There is no change to the matching-channel comparison, no claim of the new powers beyond (1), and no consequence at a specified exceptional modulus or for Hypothesis S.

## 1. Actual tagged factors and the free signed measure

Use the original signed reciprocal replacement from §2 of the [growing-residual theorem](r75-source-dynamic-giant-growing-rough-residual.md). For a fixed genuine $s,W$ and short label, this replaces the signed upper factors $\mu(U)/U$, with exactly the permitted integer tag-count set $K(W)$, by the real signed measure in (3) of that theorem; it works on hard intervals with bounded-variation marks and arbitrary inverse-logarithmic error. The replacement is uniform even for arbitrary subsets of allowable counts. We keep the original $K(W)$ throughout. The actual excluded neighborhoods of $V_X$ and $Y_*$ remain excluded, and every evaluated upper log argument lies in $[.4,.6]$ by the original cofactor window and lower size gate. Set

$$
  \tau=\frac{\log Z}{L},\qquad
  \alpha=\frac1{128(J+1)}=\frac{\log(Y_*^{1/2})}L,\qquad
  \tau_f=\frac1{32(J+1)}=\frac{\log(Y_*^2)}L .
$$

The exact stabilized tag band is $(2V_X,Y_*^{1/2})$; the lower excluded neighborhood is below $Z_0$. Hence if $\tau\le\tau_f$ the upper real tagged kernel is $g_t(u)=\mathbf1_{\tau<u<\alpha}/u$, understood as zero when the interval is empty, and the free kernel is supported on $\tau_f<u\le.7$. With $g_t^{*0}=\delta_0$, define

$$
 T_{-,K}=\sum_{\substack{k\ge0\\k\in K}}
                 \frac{(-1)^k}{k!} g_t^{*k}.
$$

When the tagged interval is empty, this formula is exactly the atom or zero as decided by $0\in K$. Because the restriction applies only to the tagged factors, the upper real measure at arguments $v\le.6$ is exactly

$$
              A_{-1,K}=T_{-,K}*A_{\tau_f},
 \qquad A_\xi=\exp_*(-\mathbf1_{u\ge\xi}\,du/u).                   \tag{4}
$$

All operations in (4) can be performed on the compact range; omitted upper shifts above $.7$ cannot contribute there. This is a factorization with the true count set, not a comparison to unrestricted total tag count. At $\tau=\tau_f$ the continuous formula is unchanged; literal integer cut endpoints were already accounted for by the reciprocal replacement.

As in §3 of the full polynomial-range estimate, $A_\xi$ consists of its unit atom at zero and its absolutely continuous density

$$
           a_\xi(v)=-\frac1v\rho(v/\xi-1)\quad(v>0),
               \qquad \|A_\xi\|_{\mathrm{TV}}\le2,                 \tag{5}
$$

where $\rho=0$ on the negative half-line, is one on $[0,1]$, and is the positive nonincreasing Dickman function on the nonnegative half-line. In particular $x\rho(x)=\int_{x-1}^x\rho(y)\,dy$ for $x\ge1$ implies $\rho(x)\le\rho(x-1)/x$. Iteration yields $\rho(x)\le1/\lfloor x\rfloor!$ for $x\ge1$. Formula (5), including the atom, follows by marking one log coordinate in the convolution exponential; on compact ranges it is also the differential formula for the cumulative $\rho(v/\xi)$.

For $\tau\le\tau_f$, the total variation of $T_{-,K}$ is dominated by the positive tagged exponential $T_+=\exp_*(g_t)$. Its mass $\exp(\int g_t)\ll\tau^{-1}$. For a total argument $.4\le v\le.6$, restrict first to tagged shifts $u\le v/2$. The free density in (4) then has argument at least $.2$, so (5) and $J\log J=(1+o(1))H$ give, uniformly,

$$
 \sup_{w\ge.2}|a_{\tau_f}(w)|
   \ll \exp\bigl(-(6.4+o(1))H\bigr)\ll\ell^{-6}.                   \tag{6}
$$

This bound in (4) costs at most $O(\tau^{-1}\ell^{-6})$ after integrating all these tagged shifts, including the tag atom. Here and below the factorial bound can be read with a fixed strictly smaller exponent, so it is not an endpoint asymptotic.

For the other half of (4), we need a *density* bound for the large positive tag shifts, not just a mass bound. Take

$$
           s=\frac{\log J-2\log\log J}{\alpha}>0
$$

for large $X$. Its tilted tagged kernel is $e^{su}g_t(u)$. The tilted full measure is exactly $e^{su}dT_+(u)$; the convolution identity gives this before summing the arities. Its mass is at most

$$
 \tau^{-1}\exp\!\left(\int_0^\alpha\frac{e^{su}-1}{u}\,du+O(1)\right)
     \le \tau^{-1}\exp\bigl(O(s\alpha e^{s\alpha})+O(1)\bigr)
     =\tau^{-1}\exp(o(H)).                                       \tag{7}
$$

Indeed $s\alpha e^{s\alpha}=O(J/\log J)=o(H)$. If $q_s(w)$ is its density off zero, marking one tagged coordinate gives $wq_s(w)=(e^{su}\mathbf1_{\tau<u<\alpha}*T_{+,s})(w)$, so its supremum on $w\ge.2$ is bounded by (7) times $O(e^{s\alpha})$, still $\tau^{-1}\exp(o(H))$. Undoing the tilt, the unweighted density satisfies

$$
 q(w)\ll \tau^{-1}\exp(-.2s+o(H))
                  \ll\tau^{-1}\ell^{-24}\qquad(w\ge.2),           \tag{8}
$$

because $.2s=(25.6+o(1))H$. The same density domination in absolute value applies to $T_{-,K}$, uniformly in the true $K$. In the region $u>v/2$, multiply (8) by $\|A_{\tau_f}\|_{\rm TV}\le2$ including its atom, yielding a contribution $O(\tau^{-1}\ell^{-24})$. This proves that the density of (4) is $O(\tau^{-1}\ell^{-6})$ throughout the compact range, without cancellation in the tagged factor itself.

For $\tau_f<\tau\le1/(8(J+1))$, no possible upper factor is tagged and each allowed upper prime is past both excluded neighborhoods. The true upper count condition is then precisely $0\in K(W)$, or the whole term is zero. In the former case the upper density is exactly the free one in (5) with $\xi=\tau$ on the compact range. As $v/\tau\ge3.2(J+1)$ for $v\ge.4$, the factorial bound gives $O(\ell^{-3})$ there. In particular the following weaker unified estimate holds on the entire range (1):

$$
    |\varrho_{-1,K}(v)|\ll \tau^{-1}\ell^{-3}
                    \quad(.4\le v\le.6),                         \tag{9}
$$

uniformly in the genuine lower factors and their associated count sets. Unlike the full-range split bound, (9) neither peels a lower factor nor strips an arity, size or tag gate.

## 2. Refine the actual hard bins before multiplying the arm norms

Use the ordinary and containing integer log-label coordinates of the [four-parity proof](r89-source-four-actual-parity-phases.md). Take finer normalized bins of width $\delta=\ell^{-8}$ on the same bounded label-coordinate range. At a fixed physical $x=hF$ and a fixed short label, the corresponding interval of $\log h/L$ has length at most $\delta/\ell$. The particular clipping depends on the bin type, and the true log mark is left as in the four-parity proof. Its supremum and variation, and those of its scaled derivative in $x$ on a fixed common interval, are bounded uniformly. Neither this bound nor the actual hard reciprocal replacement depends on the larger bin length used there. The normalized lower positive mass with all possible short labels remains $O(\ell\tau)$; no reduction of the genuine lower $W$ masks is performed.

Thus (9) bounds the real density of a full-sign bin and its scaled derivative mark on common clipping intervals by $O(\delta\ell^{-3})$. Without a full sign, or with every mark taken positively, the same calculation using the original density upper gives $O(\delta)$. For variation in physical $x$, use the common clipped interval for the difference of marks, and bound its symmetric difference positively. The latter has normalized length $O(|x-y|/(XL))$, so its positive gauge is $O((\ell/L)|x-y|/X)$, smaller than $\delta\ell^{-3}$ at total-variation scale. This uses only the density bound and derivative of the bare mark, not a derivative of (9). The endpoint jumps of the true physical window have the same bounds as the density supremum.

Use the same reduced numerator Siegel–Walfisz completion and integer Perron separations of the four-parity proof. The weight, uniquely selected distinguished prime, bounded-arity label coefficient, and actual support are unchanged, and the narrow bins introduce only one hard interval in the existing bin coordinate; their separation requires no inverse factor in their width. On a fixed real auxiliary arc the transform factor is $\min(X,|\beta|^{-1})$, with the usual reduced-numerator factor; all arithmetic replacement and minor errors remain arbitrary inverse logarithmic. The major arc fourth means therefore give

$$
   \text{full-sign bin fourth norm }O(X^{3/4}\delta\ell^{-3}),
   \qquad
   \text{unsigned upper bin fourth norm }O(X^{3/4}\delta).        \tag{10}
$$

Here the no-full-sign signed short bin is bounded by the unsigned fourth norm using coefficientwise absolute domination of its squared convolution. All statements hold for either hard bin coordinate.

After the exact Walsh operation, for an accepted bin pair with $m$ actual full signs, Hölder and Parseval give a target norm $O(X^{3/2}\delta^2\ell^{-3m})$. There are $O(\delta^{-2})$ accepted bin pairs, so their total norm is $O(X^{3/2}\ell^{-3m})$. The literal integer thresholds move by $O(1)$ in the unnormalized log coordinates, giving normalized width $O(1/T)=o(\delta)$. For each of the seven rows the fixed number of exact long/product boundary lines therefore meets only $O(\delta^{-1})$ ambiguous bin pairs, as in the [separate-row argument](r95-source-off-axis-right-forbidden-dominance.md). In every such bin retain the true comparisons and dominate positively; by (10) their total norm is $O(X^{3/2}\delta)$. The exterior floor slivers and temporary unit deletion have the old $O(X^{3/2}\ell/L)$ and arbitrary inverse-logarithmic bounds, respectively. All these are smaller than the asserted signed norms, even for $m=2$; in particular the old coarse-bin $O(\ell^{-1})$ boundary total is not used. This proves (2) on the original discrete coefficients.

## 3. Common maximum on the actual short split interval

Use the coordinatewise positive envelopes of the [raw matching-channel theorem](r97-source-matching-walsh-raw-euler-rate.md), dropping no discrete mask in the coefficients being compared. A Walsh factor has modulus one on each actual operand pair and changes neither row eligibility nor absolute short-mark bounds. Hence each one-axis envelope remains a positive pointwise bound independent of the other two chosen coordinates, even for targetwise choices of the Walsh channel. Floor gap target norm is $O(X^{3/2}(d+\ell/L))$ for width $d$. Above the original $\tau_*=(\epsilon/16)(\log\log\ell)/\log\ell$, a split gap of width $d$ and endpoint ratio at most two costs $O_A(X^{3/2}(d+L^{-A}))$; it uses both the true gap prime and failure of an upper gate. The single initial split gap from $Z_0$ to $X^{\tau_*}$, intersected with (1), has the raw positive norm $O(X^{3/2}\ell^{-\sigma})$. This is a comparison of actual retained terms, and uses no matching-channel calibration since the comparator here is zero.

Take a mesh of spacing at most $\eta=\ell^{-2\sigma}$ on both floor axes and on the split exponent above $\tau_*$ within (1), including the initial split gap separately. Upper endpoint ratios are at most two since $\eta=o(\tau_*)$. The total squared cost of the upper gaps is $O(X^3\eta)$, because widths sum to a bounded number on each axis and the sum of their squares is $O(\eta)$. The initial squared cost is also $O(X^3\eta)$. There is no product-mesh factor multiplying the gaps. The total squared fixed-node cost from (2) is at most $O(X^3\eta^{-3}\ell^{-6m})$; as $8\sigma<6$, it is smaller than $X^3\eta$ already for $m=1$. The finite number of rows and bits changes only the constant. This proves (3), with a common estimate over all allowed truly adaptive parameters.
