# R24: one admissible giant with any proper prime-power cofactor

Keep the wide divisor cutoff \(D=D_*=\lfloor\lceil4N^{3/40}N\rceil^{1/3}\rfloor\asymp N^{43/120}\), \(Q=N^{7/8}\), and \(b_*=N^{3/40}\). In the exact rough–rough high-product component of R18–R20, select pairs for which **at least one** raw leg, say \(n\), has the form
\[
 n=pr,\qquad p>D\text{ prime},\qquad r=q^k\le D,\quad q\text{ prime},\ k\ge2,
 \qquad pD\ge Q .
\]
The other raw leg is any allowed rough leg, not necessarily another admissible giant. Keep the exact coprimality condition, roughness mask, nonzero signed aliases and diagonal deletion. Under global Dirichlet GRH, its actual arithmetic kernel on the physical compression \(0<x,y\le c\), for \(1\le c\le b_*\), satisfies
\[
 \|C_{\rm one\ giant,\ proper}\|_{\rm HS}
 \ll c\,\frac{(\log\log(3N))^2}{\log N}
       +O_\epsilon(cN^{-1/40+\epsilon}).                              \tag{1}
\]
This decays for \(c=o(\log N/(\log\log(3N))^2)\), in particular for every fixed \(c>0\) by compression and for \(c\le(\log N)^{1-\eta}\) with \(\eta>0\) fixed. It is not a decaying estimate at a polynomial prefix. The wider \(D\) and all original labels are unchanged. Prime cofactors and the part with no admissible giant remain uncontrolled here; neither S nor R follows.

The starting point is the [R23 exact giant identity](r23-source-giant-cofactor.md), frozen SHA-256 2c53750f688ad4c4d9979a20c7752327f776d46f424c42d15ee15ab8c098d548. At a pair with this first leg, the genuine coefficient before the outer line sign is
\[
 -\Lambda(r)\,R_D(m)=-\Lambda(r)\bigl(\Lambda(m)-\Lambda_D(m)\bigr),\qquad
 \Lambda_D(m)=\sum_{\substack{d\mid m\\d\le D}}\mu(d)\log(m/d).
\]
The giant prime \(p\) is unique and \(p\ge Q/D\gg N^{31/60}\); no other prime of \(n\) besides \(q\) can enter \(W=\prod_{\ell\le\log N,\ \ell\nmid N}\ell\). The right rough mask is retained and cannot be replaced by fully rough support.

## 1. Basic sparse pieces and the actual \(\Lambda(m)\) term

Work first with the oriented first-leg condition, put \(X=\lceil4cN\rceil\) (a raw support bound, not the definition of \(D\)), and fix a signed alias \(m=m(p)=h_0+\sigma rp\), \(h_0=\pm jN\ne0,\ \sigma=\pm1\). Write \(h=|h_0|\). For \(r\ge N^{1/10}\) proper, the [R23 sparse proof](r23-source-giant-cofactor.md), using the smaller actual support \(cN\) and \(O(c)\) aliases, bounds HS by \(O_\epsilon(cN^{-1/40+\epsilon})\). The selected region \(m\le N^{1/4}\) likewise has raw absolute weight \(O_\epsilon(N^{1/4+\epsilon})\) on each line: each \(m\) determines at most one \(n\), and the arithmetic coefficient is \(O_\epsilon(N^\epsilon)\). This gives an HS power error by the standard rectangle/layer-cake argument below. Henceforth \(r<N^{1/10},m>N^{1/4}\). The right \(\Lambda(m)\) term at proper prime powers \(m\) costs raw \(O_\epsilon(\sqrt X\,N^\epsilon)\), since each \(m\) fixes the raw pair and the giant representation is unique. The value at \(m=1\) is zero, and \(q^1\) on the first leg is not included in the hypothesis.

For the remaining right-prime term, use the uniform two-affine Selberg sieve proved in the [R23 two-giant follow-up](r23-source-double-giant-proper.md), SHA-256 21f68a9dedb3043138c50bd9563204a7c0431d91da83f4b3d4a32691a1aafc60. Its checked quadratic proof applies to the forms \(t\) and \(h_0+\sigma rt\): their nonzero determinant has magnitude \(h\); use only sieve primes not dividing \(2rh\). For a cumulative rectangle \(n\le Nx,m\le Ny\) with atoms, \(t_0=N\min(x,y)\gg N^{1/4}\), and the allowed \(p\) interval has length at most \(t_0/r\). It is contained in an interval of length \(H\asymp t_0/r\), with \(N^{3/20}\ll H\ll N^{43/40}\). The sieve level \(H^{1/10}\) is below both candidate prime values, since \(m>N^{1/4}\) and \(p\gg N^{31/60}\). The exceptional product \(\prod_{\ell\mid2rh,\ \ell>2}(1-2/\ell)^{-1}\) is \(O((\log\log(3N))^2)\), uniformly for these polynomial \(r,h\). Thus the count for this \(r\) is
\[
 \ll (t_0/r)\,(\log\log(3N))^2/(\log N)^2 .
\]
Multiplying by \(\Lambda(r)\log m\) and summing uses \(\sum_{q,k\ge2}\log q/q^k<\infty\). Hence each alias contributes at most \(t_0 F_N\) in absolute raw prime weight, where \(F_N=(\log\log(3N))^2/\log N\). If \(q\mid h\), a right prime would have to equal \(q<N^{1/20}\), impossible in this high-\(m\) cut; the right powers of \(q\) were included among the sparse terms. This is consistent with the exact zero density below.

## 2. GRH PNT for the actual rough mask and truncated weight

For the right \(\Lambda_D(m)\) term, the indicator of at most one distinct prime from \(W\) is exactly
\[
 1+\sum_{\substack{P\mid W\\\omega(P)\ge2}}
     (-1)^{\omega(P)+1}(\omega(P)-1)\mathbf 1_{P\mid m}.
\]
In particular there are no singleton masks \(P=\ell\). The total absolute coefficient mass is \(N^{o(1)}\) by \(\pi(\log N)=O(\log N/\log\log N)\), and \(W\le N^{O(1)}\). Expand also the original \(d\le D\) divisor weight; \(\mu(d)\) makes \(d\) squarefree. Discard \(q\mid N\) or \((d,N)>1\), exactly as dictated by \((nm,N)=1\). The values \(m= h_0+\sigma rp\) satisfy \((m,N)=1\) precisely when \((rp,N)=1\). Thus for these \(q,d\) it suffices to exclude \(p\mid N\), which costs at most \(O(\log N)\) prime points per expansion term.

For a fixed \(d,P\), let \(K_0=[d,P]\) (squarefree). The relation \(K_0\mid m\) gives one reduced residue class for \(p\) modulo \(K_0\), unless restricted as follows.
* If \(q\mid K_0\), the associated condition is impossible for \(q\nmid h\) and automatic for \(q\mid h\). In the automatic case remove \(q\) from the progression modulus.
* If a prime \(\ell\ne q\) divides both \(K_0\) and \(h\), the class is nonreduced; any prime solution must equal such an \(\ell\). These contribute at most \(O(\log N)\) points per term and supply no continuous main term.

All remaining classes are reduced and have modulus \(N^{O(1)}\). Use [Lee, arXiv:2301.13457v2, Corollary 1.1 and §5](https://arxiv.org/pdf/2301.13457v2) for the standard GRH \(\theta\) estimate when \(t\) exceeds the modulus, then partial summation to obtain the prime density \(dt/(\varphi(k)\log t)\) with error \(O(\sqrt t\,(\log N)^C)\) for every reduced modulus \(k=N^{O(1)}\) needed here. Below the modulus there is at most one integer in the residue class and the proposed integrated main term is \(O((\log N)^C)\); this handles that range before partial summation as well. For moduli \(1,2\) the ordinary RH PNT suffices. This verifies applicability even when \(P\) is larger than \(X/r\). In the hard \(p\) interval, the original log marker \(\log(m(p)/d)\) is bounded with total variation \(O(\log N)\), since \(m(p)>N^{1/4}\) is monotone. Abel summation and exact endpoint handling cost \(O_\epsilon(\sqrt{X/r}\,N^\epsilon)\) per \(d,P\), including the exceptional individual primes above. Summed over signed \(d\), Boolean \(P\), and \(r=q^k\) weighted by \(\Lambda(r)\), the raw error is \(O_\epsilon(D\sqrt X\,N^\epsilon)\); here \(\sum_{r\le D,\ k\ge2}\Lambda(r)/\sqrt r\ll\log N\) (the square exponents give the harmonic prime sum, and the rest converge).

We next evaluate the weighted density and its finite-cutoff error. Let \(W'=[W,q]\) be squarefree, and put \(d=u a\) with \(u\mid W'\), \((a,W')=1\). The admissible residues require \((a,hW')=1\). Local compatibility of \(u,P\) is just the set of rules for primes in \(K_0\) above. Let \(K\) be \([u,P]\) with the factor \(q\) omitted when it divides \([u,P]\) and \(q\mid h\). The modulus attached to the reduced class is then \(Ka\), and its PNT multiplier at real \(p\) is
\[
 \sum_{\substack{u\mid W'\\u,P\ {\rm compatible}}}
       \frac{\mu(u)}{\varphi(K)}
       \sum_{\substack{a\le D/u\\(a,hW')=1}}
          \frac{\mu(a)}{\varphi(a)}
          \bigl(\log m(p)-\log u-\log a\bigr).                         \tag{2}
\]
This does not replace the signed cutoff by a nonnegative sieve. By [R16](arithmetic-post-r15-mobius-short.md), equation (3), on RH
\[
 \sum_{\substack{a\ge1\\(a,B)=1}}\frac{\mu(a)}{\varphi(a)}=0,\qquad
 -\sum_{\substack{a\ge1\\(a,B)=1}}
       \frac{\mu(a)\log a}{\varphi(a)}=\mathfrak S(B)
       \quad(B\ {\rm even}),
\]
with tails \(O_\epsilon(B^\epsilon Y^{-1/2+\epsilon}(\log(2Y))^i)\) above \(a=Y\), \(i=0,1\). The input has exactly \(B=hW'\), even because \(N\) is even. Also \(q\) is odd by the unit condition, so the prime 2 is never a forced singleton requiring a separate local convention. This project has no odd \(h=jN\) to which this evaluation must be extrapolated; both signs of \(h_0\) use the same \(|h_0|\).

Replace the inner cutoff in (2) by these two series. The uniform error for fixed \(r,P\) on the actual real interval is
\[
 O_\epsilon\left(N^\epsilon D^{-1/2}
       \sum_{u\mid W'}\frac{\sqrt u}{\varphi(K)}\right)
 \ll_\epsilon N^\epsilon D^{-1/2}(1+\sqrt q).
\]
For \(D/u<1\) the inner sum was empty; the same bound holds since \(\sqrt{u/D}>1\) and the full limits are \(O_\epsilon(N^\epsilon)\). For the last estimate, \(\varphi(K)\ge\varphi(u/(u,q))\); the factor \(1+\sqrt q\) covers the possibly denominator-free \(q\), and \(\prod_{\ell\mid W,\ell\ne q}(1+\sqrt{\ell}/(\ell-1))=N^{o(1)}\). Integrating \(dp/\log p\), summing \(P\), then \(r\) with \(\Lambda(r)\) costs raw \(O_\epsilon(XD^{-1/2}N^\epsilon)\), since \(\sum_{q,k\ge2}(1+\sqrt q)\log q/q^k\) converges. This tail estimate is uniform even when \(q>\log N\).

The complete density shows why the exact \(P\) mask did not create a spurious large main term.
* If \(q\mid h\), pair the two \(u\)'s with and without \(q\). The factor \(q\) is automatic and omitted from \(K\), so the pair has identical denominator and opposite Möbius signs, for every compatible \(P\), including \(P=1\). The complete density is zero.
* If \(q\nmid h\), \(u,P\) cannot contain \(q\), nor any prime of \(h\). For any compatible nonempty \(P\), choose \(\ell\mid P\); toggling \(\ell\) in \(u\) leaves \([u,P]\) unchanged and cancels the density. Incompatible \(P\)'s had no reduced-class main. Thus only the coefficient \(+1\) at \(P=1\) remains. Summing its local \(u\) signs in (2) gives precisely
\[
 \mathfrak S(hW')\prod_{\substack{\ell\mid W\\\ell\nmid hq}}
        \left(1-\frac{1}{\ell-1}\right)=\mathfrak S(hq),
\]
since the factor \(\ell/(\ell-1)\) in \(\mathfrak S(hW')\) becomes the ordinary factor \(\ell(\ell-2)/(\ell-1)^2\) when \(\ell\nmid hq\). The \(q\) factor already occurs in \(hW'\) whether or not \(q\in W\), as required. Primes dividing \(N\) are included through \(h\), not counted again by the mask.

In particular, the raw model for the oriented right-truncated term on each exact line is the positive measure
\[
 \sum_{\substack{r=q^k<N^{1/10},\, k\ge2\\ q\nmid h}}
       \Lambda(r)\mathfrak S(hq)\frac{dp}{\log p},
       \qquad n=rp,\quad m=h_0+\sigma rp ,
\]
on the actual real support of the giant and \(m>N^{1/4}\) cuts. Here \(q\nmid h\) includes the unit condition \(q\nmid N\). The removal of \(p\mid N\) affected only the atomic PNT errors, not this continuous density. Its raw mass in any cumulative rectangle is \(O(t_0 F_N)\): \(\log p\gg\log N\), the \(p\) interval has length at most \(t_0/r\), \(\mathfrak S(hq)\ll(\log\log(3N))^2\) uniformly, and \(\sum\Lambda(r)/r<\infty\) for proper powers. This density is an intermediate device to bound the actual truncated weight, not an additional model subtracted from the original rough–rough kernel.

## 3. Hardy transfer and the exact union

For a component whose absolute cumulative line mass is \(O(t_0 F_N)\), when \(x\le y\) there are \(O(y)\) active aliases if any, with \(y\ge1/2\). After normalization by \(1/N\) and the marker \(\sqrt{uv}\), its cumulative bound is \(O(xy\sqrt{xy}F_N)\), and the same after reflection. Its log-physical kernel is \(O(\sqrt{xy}F_N)\) because
\(K=2\pi A/(xy\sqrt{w_N(x)w_N(y)})\) and both physical coordinates are at least \(1/N\) on the prime/model support just used. Integrating in \(dx\,dy/(xy)\) gives HS \(O(cF_N)\), without a log-area loss.

For the signed discrepancy between the atomic truncated term and its intermediate density, every hard rectangle on one line has raw discrepancy \(O_\epsilon((D\sqrt X+XD^{-1/2})N^\epsilon)\); the sparse terms removed earlier have raw weights \(O_\epsilon((N^{1/4}+\sqrt X)N^\epsilon)\) except for the separately bounded \(r\ge N^{1/10}\) sector. Normalize by \(1/N\) and sum \(O(c)\) aliases. The density in the raw \(n\) coordinate is at most \(O_\epsilon(N^\epsilon)\), since it is a sum weighted by \(\Lambda(r)/(r\log(n/r))\) with converging proper-power reciprocal sum. The atomic per-point bound is also \(O_\epsilon(N^\epsilon)\). Hence the trivial cumulative bound \(O_\epsilon(N^\epsilon(xy)^{3/2})\) holds for all these errors, and layer cake from the hard rectangle bound \(U_0\) gives the complementary \(O(U_0\sqrt{xy})\). Multiply them in the squared log kernel and integrate on log area \(O((\log N)^2)\); there is no atom or model below \(1/N\) in either coordinate. The resulting HS error is at most
\[
 O_\epsilon\bigl(
 c^{3/4}N^{-17/240+\epsilon}
 +cN^{-43/480+\epsilon}
 +c^{1/2}N^{-3/8+\epsilon}
 +c^{3/4}N^{-1/4+\epsilon}\bigr),
\]
using \(D\asymp N^{43/120}\). For \(c\ge1\) all four terms are at most \(O_\epsilon(cN^{-1/40+\epsilon})\). This proves (1) for the oriented first-leg selection and for its reflection.

The union of the two orientations is exactly their sum minus the intersection. The intersection requires both giant legs and proper cofactors, hence is bounded by the [R23 two-giant proper-cofactor bound](r23-source-double-giant-proper.md): its proof is an absolute majorant and does not require both selections to be disjoint. One must not simply remove the intersection from the PNT calculation in (2), since the extra moving mask would change its density. The resulting union bound is (1) with the original signs and every pair included exactly once. All limits and norm estimates concern this stated sector only.
