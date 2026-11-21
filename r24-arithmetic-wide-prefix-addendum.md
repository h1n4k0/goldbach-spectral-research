# R24 addendum: full original wide prefix on an ordinary density-one set

Assume **global Dirichlet GRH**. For even \(N\in[2X,11X/5]\), now use the entire original wide projection \(P_{b_N}\) with \(b_N=N^{3/40}\). Then

\[
 \#\left\{N\in[2X,11X/5]: N\text{ even},\ \|P_{b_N}T_NP_{b_N}\|_{\rm HS}>X^{-1/400}\right\}
 \ll_\epsilon X^{571/600+\epsilon}.
 \tag{1}
\]

At the stronger threshold \(X^{-1/100}\) the bound is \(O_\epsilon(X^{589/600+\epsilon})\). Both counts are \(o(X)\) on taking \(\epsilon\) small, among **ordinary** even moduli. This does not rule out a designated sparse family consisting entirely of exceptional moduli, nor does it bound exterior crosses or establish S or R. It is not a change to the R15 estimates for a thin family.

To see the larger coverage, the proof of [R24](r24-arithmetic-growing-compensation.md), frozen SHA-256 `57e1e5e3ea396e178255b6f3fbd7901085aaecdfac73412b7bc40fdd4d0f7328`, actually gives for a common cutoff \(1\le B\le X^{1/4}\) and \(X^{-1/4}\le\tau\le1\)

\[
 \#\left\{N:\|P_BT_NP_B\|_{\rm HS}>\tau\right\}
 \ll_\epsilon \tau^{-4}B^{11/3}X^{2/3+\epsilon}.
 \tag{2}
\]

Indeed throughout its moving-rectangle estimate use \(Y=\lceil8BX\rceil\), \(P=Y^{1/3}\). All raw arguments, frequencies \(kN\), and line supports stay \(\le Y\). Disjoint major arcs, the individual GRH major estimate, Fourier Parseval with repetitions of \(kN\) bounded by the divisor function, and the arbitrary interval collapse do not require the smaller restriction \(B\le X^{1/40}\). The only \(Y^\epsilon\) and logarithmic factors are absorbed since \(Y\ll X^{5/4}\). In the transfer, the bulk log area is still \(O((\log X)^2)\), and the exact low-edge term \(B(\log X)^4/N\) in the squared HS estimate is \(O(X^{-3/4}(\log X)^4)=o(\tau^2)\) throughout this range. Thus the same threshold argument proves (2).

Choose the common \(B=(11X/5)^{3/40}\). Then \(P_{b_N}\) is a subprojection of \(P_B\) for every tested modulus, and compressing the same operator further cannot increase its Hilbert–Schmidt norm. There is no rescaling of the kernel. The factor \(B^{11/3}\) in (2) contributes \(X^{11/40}\) up to constants, so the two exponents are \(2/3+11/40+1/100=571/600\) and \(2/3+11/40+1/25=589/600\), respectively.

The R22 comparison with the **pure rough–rough** remainder is unchanged: it only controls that comparison for tested subprefixes \(b\le N^{1/40}\) while retaining the original wide divisor cutoff. Neither (1) nor (2) extends pure rough–rough compensation to \(b_N=N^{3/40}\); the noncentral mixed contribution is not estimated separately. Both claims above concern the full centered physical compression of \(T_N\), using auxiliary GRH for the major arcs and local GRH(N) for the operator identification.
