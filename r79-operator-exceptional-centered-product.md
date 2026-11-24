# Isolating the genuine twice-centered product on the exceptional Fourier packet

**Scope.** This is a quantitative reduction of the *whole* high-denominator packet of R78, including every exceptional mode. The actual signed matrix and actual prime Gram may be replaced there, with power-small total Hilbert–Schmidt error, by one explicit twice-centered switched product of two prime-progression errors. The key extra cancellation is in the sum over the positive alias index of the switched double principal: the three original signs cancel its average density. No smallness of the remaining centered product is claimed, and no exception from R78 is silently discarded.

## 1. Setup and statement

Use the genuine transported parent index basis, physical scales $4\le H<M\le Q^\Gamma$ with fixed $0<\Gamma<1$, and two actual families $u,v\in\{h,f\}$ of [R71](r71-operator-parent-terminal-layer.md). As in [R76](r76-operator-joint-rational-numerator-variance.md), write $T_N^{u,v}=P_N^{u,v}-D_N^{u,v}-K_N^{u,v}$, with $P_N^{u,v}$ the actual odd-character prime-power Gram, $D_N^{u,v}$ the exact equality atoms, and $K_N^{u,v}$ the exact signed continuous correction. Thus the literal off-diagonal prime-power line sum equals $P_N^{u,v}-D_N^{u,v}$, and the three orientations carry coefficients $+,+,-$. Suppress $u,v$ in matrix subscripts below. Use the complete even shell $N=2m\in[Q,2Q]$, $m_0\le m\le m_0+J-1$, $J\asymp Q$, and $\widehat T(j)=J^{-1}\sum_m e(-j(m-m_0)/J)T_{2m}$ with $e(z)=e^{2\pi i z}$.

Let $B\ge4$, $R\ge1$, and $\mathcal C_+(B,R)$ be the high-denominator collars of [R78](r78-operator-flat-numerator-most-modes.md), with $\lceil B/2\rceil\le b\le B$. Impose $BM\le Q/100$ and $B^2(1+R)\le J/100$, so each mode in the packet has one rational center $Ja/b$ and a circular detuning $\nu_j=j-Ja/b\bmod J$ of absolute value at most $R$. Use reduced representatives $0\le a<b$ and the real detuning of smallest absolute value. For the auxiliary comparison choose $2\le B_0<B/2$, $R_0\ge1$ with $BB_0(R+R_0+1)\le J/10$. This guarantees that $\mathcal C_+(B,R)$ is outside the $\mathcal C(B_0,R_0)$ collars of [R75](r75-operator-prime-divisor-fourier-signature.md), including its zero-frequency collar. Assume original local Dirichlet GRH across the even shell and auxiliary Dirichlet GRH for every $q'\le\lceil8MB\rceil+2$, including $1$. Write $R_*=1+R$, $L=\log(3Q)$, and choose $2\le S\le Q/100$. Let $\omega_S$ be a single smooth cutoff of [R77 (5)](r77-operator-common-shell-rational-packets.md#2-common-taper-and-the-exact-sharp-edge), with total edge length $O(S)$, independent of $j$.

We define the explicit matrix field $\mathcal X(j)$ on $\mathcal C_+(B,R)$. In a raw entry $I,I'$ on dyads $V,U$, use each orientation $\sigma=(\sigma_1,\sigma_2)\in\{(+,-),(-,+),(+,+)\}$, with respective sign $\eta_\sigma=+1,+1,-1$, and each positive integer $k$ with nonempty raw support. With raw coordinates $z,w$, put $t=(\sigma_1z+\sigma_2w)/k,\ q=2k,\ q'=qb$, $x(t)=(t/2-m_0)/J$, and

$$
\mathcal H_{I,I',k,j}(z,w)
    =\omega_S(t)e(-\nu_jx(t))u_{I,t}(z)v_{I',t}(w).
 \tag{1}
$$

Here and below the test is zero outside the support of $\omega_S$ in $t$; the exact physical profiles have the same support and derivatives as in R76. On unit residues modulo $q'$, put

$$
\begin{split}
 A_{-a}(r,s)&=\mathbf1_{q\mid\sigma_1r+\sigma_2s}
                   e(-a(\sigma_1r+\sigma_2s)/q'),\\
 F_{q',r}(z)&=\psi(z;q',r)-z/\phi(q')\qquad(z\ge0),
 \end{split}
$$

extending $F$ by zero for $z<0$. The entry of the centered-product field is

$$
\mathcal X_{I,I'}(j)=\frac{e(a m_0/b)}{J}
   \sum_\sigma\sum_{k\ge1}\eta_\sigma
     \sum_{r,s\bmod q'}^{*}
          A_{-a}(r,s)
         \iint F_{q',r}(z)F_{q',s}(w)
                      \partial_{zw}^2\mathcal H_{I,I',k,j}(z,w)\,dz\,dw .
 \tag{2}
$$

The $k$-sum is finite by the actual raw support, and the derivatives are integrable as in R76 (5). The outer phase in (2) exactly converts the complete shell normalization to the displayed rational twist. When the detuning uses a wrap modulo $J$, the same phase identity holds at every actual integer $m$; the fixed representative $|\nu_j|\le R$ is used to make the corresponding real extension (1).

Let $E_\kappa$ and $\mathcal B_{\rm HS}$ be as in [R74 (2)](r74-operator-fixed-macro-mean-all-modes.md#statement), for fixed $0<\kappa<1/3$, with $\iota=0$ for $h,h$ and $\iota=1$ if a body profile $f$ is present. On the entire fixed parent index space,

$$
\begin{split}
 &\left(\sum_{j\in\mathcal C_+(B,R)}
       \|\widehat T(j)-\mathcal X(j)\|_{\rm HS}^2\right)^{1/2}\\[-2pt]
 &\qquad\ll_{\Gamma,\kappa,\Theta,\epsilon} Q^\epsilon
   \left[E_\kappa+\iota\mathcal B_{\rm HS}
      +B_0^{-1}+(1+R_0)^{-1/2}
      +\sqrt{S/Q}+\sqrt{B/Q}
      +\sqrt{M/Q}\,R_*^{3/2}
      +\frac{B\sqrt{R_*}}{Q}\sqrt{\frac MH}
      +\frac{\sqrt{R_*}}{B}\right].
 \end{split}
 \tag{3}
$$

The same bound holds with $\widehat P$ in place of $\widehat T$. For any fixed orthogonal projection $\Pi$ on the parent index space and any subset $\mathcal E\subset\mathcal C_+(B,R)$, even chosen by the actual size of the sharp coefficients, (3) bounds the difference between the Fourier Hilbert–Schmidt RMS on $\mathcal E$ for $\Pi\widehat T\Pi$ (or $\Pi\widehat P\Pi$) and the RMS there for $\Pi\mathcal X\Pi$. Here RMS means square root of summed squared Fourier coefficients in the displayed normalized Fourier convention, with no additional division by the number of modes in $\mathcal E$.

For the R78 spatial sizes $H=Q^{2/5},M=Q^{3/5},W_V=Q^{23/175}V^{4/7}$, and the R78 high packet $B=\lfloor Q^{39/100}\rfloor,\ R=\lfloor Q^{1/400}\rfloor$, take

$$
S=Q^{3/4},\qquad B_0=\lfloor Q^{1/5}\rfloor,\qquad
 R_0=\lfloor Q^{1/4}\rfloor,\qquad \kappa=3/10 .
 \tag{4}
$$

Then the right side of (3) is $O_\epsilon(Q^{-3/25+\epsilon})$ for $h,h$ and $O_\epsilon(Q^{-1/50+\epsilon})$ with a body leg. The auxiliary modulus cap is $O(Q^{99/100})$, exactly the R78 example cap. In particular the reduction applies on every actual exceptional mode in R78 (3) after its fixed macro projection, or on any other subset of its high packet. It does not estimate the RMS of $\mathcal X$ there.

## 2. The switched double principal cancels its alias density

We show why the switched principal term is small on this whole high packet without first matching its coefficient to a separate lattice error in the benchmark. For each frequency use the exact twist and real weight (1) in the R76 switch. By the R73 row and column computation [R73 (8), (12)](r73-operator-rational-modulus-collars.md), the double principal term for an orientation has coefficient

$$
\frac{k}{\phi(2k)\phi(b)^2}\int
        \omega_S(t)e(-\nu_jx(t))I_{k,\sigma}(t)\,dt
 \tag{5}
$$

if $b$ is squarefree and $(b,2k)=1$, and zero otherwise, before the factor $e(a m_0/b)/J$. The line profile in (5) is the exact

$$
I_{k,\sigma}(t)=\int_{z>0}
                      u_{I,t}(z)v_{I',t}\big(\sigma_2(kt-\sigma_1z)\big)\,dz ,
$$

with the second leg zero at nonpositive coordinates. Here $k$ in (5) is the positive Jacobian $dw=k\,dt$ at fixed $z$, not an asymptotic replacement.

Suppose $b$ is odd and squarefree, the only case with a nonzero term in (5). The exact divisor identity

$$
\frac{k}{\phi(2k)}
        =\sum_{\substack{d\mid k\\d\ {\rm odd}}}\frac{\mu^2(d)}{\phi(d)}
$$

and inclusion-exclusion yield, for $0\le X\le 4M+1$,

$$
\sum_{\substack{1\le k\le X\\(k,b)=1}}\frac{k}{\phi(2k)}
       =c_b X+O_{\Gamma,\epsilon}(Q^\epsilon),\quad
 c_b=\frac{\phi(b)}b
        \sum_{\substack{d\ {\rm odd}\\(d,b)=1}}
                      \frac{\mu^2(d)}{d\phi(d)} .
 \tag{6}
$$

Indeed write $k=d l$. On $(d,b)=1$, the count of $l\le X/d$ with $(l,b)=1$ is $(\phi(b)/b)(X/d)+O(\tau(b))$. The accumulated floors in (6) are $O_\epsilon(Q^\epsilon)$ since $\sum_{d\le X}1/\phi(d)\ll_\epsilon(1+X)^\epsilon$ and $\tau(b)\ll_\epsilon Q^\epsilon$, with arbitrarily small exponents before combination. The extended coefficient tail times $X$ has the same bound from $\sum_{d>X}1/(d\phi(d))\ll_\epsilon X^{-1+\epsilon}$ for $X\ge1$. For $0\le X<1$ use the bounded constant $c_b$. The coefficient $c_b$ is common to the three orientations and does not depend on $t$.

Fix $t\in[Q,2Q]$. Let $I_{k,\sigma}(t)$ extend to real $k=z_0\ge0$ by the same formula. In the raw dyads with $V\le U$, its supremum and variation on $z_0\ge0$ are $O_{\Gamma,\Theta}(QV b_Ib_{I'})$, where $b_I=\sqrt{|I|}/(\sqrt Q V)$, $b_{I'}=\sqrt{|I'|}/(\sqrt Q U)$. Use the shorter first leg in $L^1$ and the other leg in supremum plus variation, and the monotone affine map in $z_0$. It vanishes for $z_0>4U$. The literal affine identities give

$$
\int_0^\infty\sum_\sigma\eta_\sigma I_{z_0,\sigma}(t)\,dz_0=0 .
 \tag{7}
$$

In fact $dz_0$ on each line gives absolute Jacobian $1/t$ in the second raw coordinate. The two difference orientations divide the positive raw quadrant into its two open halves, while the sum orientation covers it completely; the equal line is Lebesgue null. Thus the integrals cancel for these exact moving profiles at every fixed $t$, not just after a shell average. This is the same signed geometry as [R68 (8)–(10)](r68-operator-residue-orbit-and-alias-slope-covariance.md#exact-continuous-benchmark), applied to the different coefficient (6).

Partial summation in the positive integer aliases using (6) and (7) now bounds the signed sum in (5), before its $t$-integration, by $O_\epsilon(Q^\epsilon QV b_Ib_{I'}/\phi(b)^2)$. The $t$-integration with the harmless cutoff and phase, divided by $J$, costs a constant. After HS aggregation, $QVb_Ib_{I'}$ costs $O(\sqrt{V/U})$ by the square sum of the parent envelopes. Sum the dyad pairs, transpose for $U<V$, and absorb logarithms to obtain $O_\epsilon(Q^\epsilon b^{-2})$ per Fourier coefficient. For even or nonsquarefree $b$ the whole double principal is zero as already noted. There are $O(b R_*)$ modes per denominator. Summing squared bounds for $\lceil B/2\rceil\le b\le B$ gives $O_\epsilon(Q^\epsilon\sqrt{R_*}/B)$ in HS RMS. This is the last term of (3); without using the signs and the density in (6), direct estimation of (5) over $k$ need not be small on this packet.

## 3. Joint estimates for the other expanded arithmetic terms

For one frequency $j$, apply the switch of R76 to the actual off-diagonal prime-power sums multiplied by $\omega_S$, restoring the two temporarily removed kinds of nonunits in the error. Then expand the two residue measures using $z/\phi(q')+F_{q',r}$. The four terms are exactly the double principal of (5), two single errors, and the double error (2). The last is written after two partial integrations, with no endpoint terms by the common profile bounds. No term with $k=0$ is ever added. The original continuous correction contributes $-\widehat{\omega_S K}(j)$, and is not expanded into a separate lattice main in this comparison.

For the single errors use the joint numerator bound R76 (9) before the sum over $k$. This yields the $b^{-1/2}\sqrt{QM}K_1$ part of R76 (4) alone; it holds for a common arbitrary smooth test. For the different nearest-center detunings at fixed integer shift $\ell$, use the common Taylor weights in R77 (7), as there, but only the $K_1$ sum. After dividing by $J$, the reduced-numerator $\ell^2$ bound for the single-error fields is $O_\epsilon(Q^\epsilon b^{-1/2}\sqrt{M/Q}(1+|\ell|))$. Summing squares over $b\in[\lceil B/2\rceil,B]$ and $|\ell|\le R+1$ gives $O_\epsilon(Q^\epsilon\sqrt{M/Q}R_*^{3/2})$. There is no $S^{-1}$ from these first partial integrations.

For the unit restorations the R76 scalar bound per entry, summed over aliases and actual moduli before dividing by $J$, is $O_\epsilon(Q^\epsilon QU b_Ib_{I'})$ with $V\le U$; it uses only a supremum bound on the test. To recall why, at each original $N$ a unit failure occurs on a prime-power carrier of total raw Mangoldt mass $O(L^2)$, with $O(U)$ possible partners across aliases. After switching, for each $k$ a $q'$-nonunit carrier has the same mass bound and at most $O(QU/(2k)+1)$ partners by the congruence modulo $2k$. Either raw leg can fail; sum the estimates for both, and then sum over $k\le4U$. The finite raw range and $q'\le \lceil8MB\rceil+2$ give uniform logarithms. After normalizing and HS aggregation the cost per frequency is $O_\epsilon(Q^\epsilon Q^{-1}\sqrt{M/H})$. There are $O(B^2R_*)$ modes, so the full cost is the eighth term in (3). The signs do not need to cancel in these bounds. Every occurrence of the actual prime powers and unit tests is thus either exactly in (2) or accounted for by the displayed small remainders.

## 4. Keep the original continuous benchmark and restore the true shell

The pointwise bounds of [R72 §1](r72-operator-principal-modulus-low-modes.md#1-exact-fixed-supports-and-parameter-envelopes) give $O_\epsilon(Q^\epsilon)$ in HS for $T_N$ and for its exact $K_N$ separately. Therefore replacing each by its $\omega_S$-weighted field costs only $O_\epsilon(Q^\epsilon\sqrt{S/Q})$ in the RMS over *all* Fourier modes, from the actual edge length and full normalized Parseval, as in R77 (6). This applies also to any subset of the high packet, without accumulating a separate error per denominator.

By the disjointness from $\mathcal C(B_0,R_0)$, R75 (2) bounds $\widehat{D+K}$ on the high packet by the first four terms in (3). For the separate removal of $\widehat K$ we also need a bound for $D$, not the smallness of $D+K$ alone. Remove the unit test in the raw equality term and extend the resulting sum to real $t\in[Q,2Q]$:

$$
D^0_{t;I,I'}=\sum_{n\ge1}\Lambda(n)^2u_{I,t}(n)v_{I',t}(n).
$$

On dyads $V\le U$ the fixed raw support limits this to $O(QV)$ integers. With raw weights and $t$-derivatives as in R72 (4), both $\sup_t|D^0_{t;I,I'}|$ and $Q\sup_t|\partial_tD^0_{t;I,I'}|$ are $O(L^2 QV b_Ib_{I'})$. Thus in HS the slow field has supremum plus total variation $O(L^{O(1)})$. The unit correction satisfies $\|D_N-D^0_N\|_{\rm HS}\ll Q^\epsilon/(QH)$ pointwise: the sum of $\Lambda(n)^2$ on prime powers with base dividing $N$ in the raw range is $O(L\sum_{p\mid N}\log p)=O(L^2)$. Insert the envelope factors and aggregate the dyads. This argument is valid for the true $h,f$ profiles and their moving normalizations.

Discrete Abel summation as in R75 (11) gives $\|\widehat{D^0}(j)\|_{\rm HS}\ll_\epsilon Q^\epsilon(1+\operatorname{dist}(j,J\mathbb Z))^{-1}$. Every selected high center has $b\ge2$; a reduced $a/b$ there is at circular distance at least $1/B$ from zero. Hence $\operatorname{dist}(j,J\mathbb Z)\gg Q/B$ throughout the high packet, under the spacing assumptions in §1. Summing this squared tail and using Parseval for the unit correction gives $O_\epsilon(Q^\epsilon\sqrt{B/Q})$ for $\widehat D$ there. Since $K=(D+K)-D$, the same benchmark comparison plus this last estimate bounds $\widehat K$, and the edge estimate above bounds its $\omega_S$-weighted version.

Combine the switched decomposition of §3, the signed principal estimate of §2, and these benchmark and edge bounds to prove (3) for the original unweighted $\widehat T$. Adding $\widehat{D+K}$ proves it for $\widehat P$ as well. Compression by a fixed projection is an HS contraction, and the triangle inequality on any subset of modes gives the asserted comparison of RMS norms, regardless of how the subset was selected.

At (4) all disjointness and spacing conditions hold by strict exponent differences. The stationary error in R74 is $Q^{-3/25+\epsilon}$ at $\kappa=3/10$, and the body benchmark loss is $O_\epsilon(Q^{-1/50+\epsilon})$. The common edge and the $R_0$ tail are both $O_\epsilon(Q^{-1/8+\epsilon})$; the equality and restored-unit errors and the principal term are smaller. The single-error exponent is $-1/5+3/800=-157/800$. This proves the stated rates. No false conclusion about the energy of the actual exceptions follows from this reduction: it is now exactly the shifted product (2), up to these errors, that must be bounded.
