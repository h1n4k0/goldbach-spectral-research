# R19: Pointwise dispersion in a balanced product-\(N\) long–long box

**Theorem.** Assume RH for \(\zeta(s)\). In the exact off-diagonal long–long kernel of [R17](https://github.com/h1n4k0/goldbach-spectral-research/blob/2f7c1e00c099b5f2332ca3bd8fa5856a58af862e/arithmetic-post-r16-mobius-longlong.md), take the physical prefix \(b=N^{1/100}\) and retain the actual terms with
\[
N^{1/2}<d,e\le N^{501/1000}.
\]
The signed cumulative operator of this component, with exact unit condition, no continuous model added, and no averaging over even \(N\), satisfies \(\|C_{\rm bal}\|_{\mathrm{HS}}\ll_\epsilon N^{-7/5000+\epsilon}\). One may independently shorten either divisor interval. This whole box lies in \(\{de>N\}\), beyond the regime of the R18 lattice-error bound. It does **not** cover the R17 larger prefix \(N^{3/40}\) or the full complement. Local GRH(N) is understood for identifying the paper's operator; R17's full replacement of original \(\Lambda\) by its long–long term still uses its auxiliary Dirichlet GRH.

## 1. Exact sawtooth on a chosen alias

Fix \(h=jN>0\), \(j\le 2b\), and any of \(m=n+h,m=n-h,m=h-n\). A hard rectangle specifies one raw interval \((A,B]\) for \(n\), with \(n,m\ge1\). Use dyadic boxes \(d\asymp U,e\asymp V\) with \(N^{1/2}\ll U,V\ll N^{501/1000}\) and possibly shorter supports. This band lies above the R17 cutoff \(D\asymp(bN)^{1/3}\).

First omit the logarithmic cofactors and allow separated weights \(\alpha_d,\beta_e\) bounded by fixed powers of \(\log N\), supported on those intervals and on \(d,e\) individually coprime to \(N\). The simultaneous unit condition is \((n,N)=1\), since \(m\equiv\pm n\pmod N\). Expand it as \(\sum_{r\mid N,r\mid n}\mu(r)\). Put \(g=(d,e)\), \(d=ga,e=gc\). Only \(g\mid h\) with \((g,N)=1\) occur, hence \(g\mid j\), and \(rg\mid h\) for each \(r\mid N\). In \(n=rga t\), the condition \(e\mid m\) becomes
\[
t\equiv t_0:=\vartheta\bar a\pmod c,\qquad
\vartheta=\pm h/(rg)\in\mathbb Z\setminus\{0\}.
\]
Here \((a,c)=1\), \((r,c)=1\), with sign depending on the line. The count is \((B-A)/(rgac)\) plus the difference at \(A,B\) of \(\psi(E/(rgac)-t_0/c)\), where \(\psi(x)=x-\lfloor x\rfloor-\tfrac12\). Use half-integer boundaries, preserving the integer count and avoiding jumps of the sawtooth. Returning to arbitrary endpoints changes the density by \(O_\epsilon(N^\epsilon)\), since the length changes by \(O(1)\) and \(\sum_{(d,e)\mid h}1/[d,e]\ll_\epsilon N^\epsilon\) on these boxes by summing \(1/(gac)\) first over \(a,c\). Summing the zero mode over \(r\) gives exactly the unit density \((\varphi(N)/N)/[d,e]\).

By [Vaaler, Theorem 18, Bull. AMS 12 (1985), 183–216](https://doi.org/10.1090/S0273-0979-1985-15349-2), \(\psi\) is approximated by a degree-\(H\) trigonometric polynomial with zero constant term and coefficients \(O(1/|\nu|)\), with pointwise error at most a nonnegative Fejér majorant all of whose coefficients are \(O(1/H)\). Bound the error with \(|\alpha_{ga}||\beta_{gc}|\) and that majorant. Its zero frequency costs \(O_\epsilon(N^\epsilon UV/(g^2 H))\). In either polynomial, on each signed frequency dyad \(|\nu|\asymp K\le H\) the coefficient norm is \(O(K^{-1/2})\): for the majorant use \(K^{1/2}/H\le K^{-1/2}\).

## 2. Applicable source and precise exponents

Apply [Bettin–Chandee, arXiv:1502.00769v1, Theorem 1 and Remark 1, equations (1.2)–(1.3)](https://arxiv.org/pdf/1502.00769#page=2). Their two dyadic variables are \(a,c\) with lengths \(M\asymp U/g,\ P\asymp V/g\); the third is \(|\nu|\asymp K\). Up to the frequency sign, the phase is
\[
e\!\left(\nu\vartheta\bar a/c-\nu E/(rgac)\right).
\]
The perturbation \(f_\nu(x,y)=-\nu E/(rgxy)\) has exactly the required derivative bounds \(O(X/(x^2 y))\), \(O(X/(xy^2))\), with \(X=O(1+KbN/(rg))\). The endpoints are fixed while estimating a sum; the perturbations can be smoothly extended off the positive dyadic domains. The sign of the frequency may be folded into \(\vartheta\) and \(f_\nu\). All coefficients are separated, and the endpoint is in the **joint phase**, not falsely separated as a weight. The large \(h\) is retained in \(\vartheta\), without averaging. The size multiplier in the actual theorem is
\[
\left(1+\frac{|\vartheta|K+X}{MP}\right)^{1/2}
\ll g^{1/2}b^{1/2}K^{1/2}
\]
because \(UV\gg N,\ r\ge1\). The product of divisor coefficient norms is \(O_\epsilon(N^\epsilon(UV)^{1/2}/g)\). Using the two trilinear terms of Theorem 1 and dropping beneficial \(g\) powers \(-29/20,-11/8\), then summing dyads and \(r\mid N,\ g\mid j\), gives raw discrepancy
\[
O_\epsilon\!\left(N^\epsilon\left[
 \frac{UV}{H}
 +b^{1/2}H^{7/20}(UV)^{17/20}(U+V)^{1/4}
 +b^{1/2}H^{1/2}(UV)^{7/8}(U+V)^{1/8}\right]\right).       \tag{1}
\]
There is **no truncation of the unit sieve**. With \(H=\lfloor N^{3/200}\rfloor\), the three exponents in (1) are at most \(0.987,0.9872,0.951875\). This uses the cited perturbed trilinear bound, not an extrapolation from an unperturbed fixed-numerator bilinear bound.

## 3. Exact signs, logarithms, and operator transfer

Expand \((\log n-\log d)(\log m-\log e)\) into four terms to restore the cofactors: \(\log d,\log e\) remain in separated weights, and each raw function of \(n\) has supremum and variation \(O((\log N)^2)\) because \(m=m(n)\) is monotone and both \(n,m\ge1\). Partial summation of (1), which applies to every subinterval of the hard interval, gives the exact weighted density integral plus (1) with absorbed logarithms.

For that density the signs are \(\mu(d)\mu(e)\), not their absolute values. At each real \(n,m\) group by \(g\mid j\), retaining \((g,N)=1\) and squarefree \(g\); the coefficient is then \(\mu(a)\mu(c)/(gac)\) on \((a,c)=1,(ac,gN)=1\). For fixed \(g,a\), the restricted RH Mertens tail for \(\sum_{(c,agN)=1}\mu(c)(\log c)^i/c\), \(i=0,1\), is \(O_\epsilon(N^\epsilon(V/g)^{-1/2+\epsilon})\) on the interval \(c\asymp V/g\). As in R18, the restriction follows by convolving Mertens' coefficients with the sequence supported on primes dividing \(agN\), whose absolute Dirichlet mass at \(1/2+\epsilon\) is \(O_\epsilon((agN)^\epsilon)\). Taking the tail difference cancels its constant. The remaining harmonic \(a\)-sum with log weights and \(\sum_{g\mid j}g^{-1/2}\) absorb into \(N^\epsilon\). Thus the integrated density is \(O_\epsilon(bN\,N^{-1/4+\epsilon})\), well below (1). Sum the dyadic boxes to obtain a raw bound \(O_\epsilon(N^{2468/2500+\epsilon})=O_\epsilon(N^{0.9872+\epsilon})\) on every line in every moving hard rectangle, with the full signs and coprimality retained.

Divide by \(N\) and sum the \(O(b)\) possible aliases after the exact \(n=m\) deletion. The selected arithmetic signed measure has uniform rectangle bound \(U_0=O_\epsilon(N^{-7/2500+\epsilon})\). Its cumulative \(A(x,y)\) with the \(\sqrt{uv}\) weight obeys \(|A(x,y)|\ll U_0\sqrt{xy}\) by positive layer cake. Complementarily, for \(x\le y\) any nonzero line needs \(y\ge1/2\), giving \(O(y)\) possible partners per integer \(n\le Nx\); each atom's divisor weight is \(O_\epsilon(N^\epsilon)\). Thus \(|A(x,y)|\ll_\epsilon N^\epsilon(xy)^{3/2}\) also by symmetry. The physical log kernel is \(2\pi A(x,y)/(xy\sqrt{w_N(x)w_N(y)})\); each \(w_N\ge1/2\) on \(x,y\ge1/N\). Multiply the complementary bounds, then integrate the squared kernel over log area \(O((\log N)^2)\). The remainder \(x<1/N\) or \(y<1/N\) has no atoms and exactly zero cumulative. This proves the claimed Hilbert–Schmidt bound for the full selected block.

**Remaining gap.** Using only (1) and absolute alias summation, for \(b=N^\rho,H=N^\lambda,\ U,V\le N^{1/2+\theta}\), two normalized error exponents are \(\rho+2\theta-\lambda\) and \(-1/40+(3/2)\rho+(39/20)\theta+(7/20)\lambda\). At the R17 \(\rho=3/40\) they cannot both be negative even with \(\theta=0\). This diagnoses a concrete loss in this transfer, not a lower bound for the actual kernel. It needs stronger signed aggregation over aliases or a different dispersion bound to reach that larger prefix. No conclusion follows about S or R.
