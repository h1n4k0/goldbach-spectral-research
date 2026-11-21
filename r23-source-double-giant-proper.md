# R23 follow-up: proper prime-power cofactors on two admissible giant legs

Keep the original wide \(b_*=N^{3/40},D_*=\lfloor\lceil4b_*N\rceil^{1/3}\rfloor,Q=N^{7/8}\) and the exact rough–rough mask. Use the admissibility from [the giant-cofactor note](r23-source-giant-cofactor.md), frozen SHA-256 2c53750f688ad4c4d9979a20c7752327f776d46f424c42d15ee15ab8c098d548: \(n=p r\), \(p\) prime, \(p>D_*,r\le D_*,pD_*\ge Q\), and the same for \(m=p's\). Retain the pairs on which **both** giant legs are admissible and **at least one** of \(r,s\) is a proper prime power (exponent at least two); require the original exact unit, roughness, and alias masks. On the physical compression \(0<x,y\le c\) for \(1\le c\le b_*\), the actual selected arithmetic kernel satisfies
\[
 \|C_{\rm two\ giants,\ proper}\|_{\rm HS}
    \ll c\,\frac{(\log\log(3N))^2}{\log N}
          +O_\epsilon(c\,N^{-1/40+\epsilon}).
\]
In particular this is inverse-logarithmically small at fixed \(c\). The quoted bound tends to zero for \(c=o(\log N/(\log\log(3N))^2)\), including \(c\le(\log N)^{1-\eta}\) for every fixed \(\eta>0\); no decay for polynomial \(c\) is claimed. It does not estimate two prime cofactors, a lone admissible giant with a small proper cofactor, or the other rough–rough sectors. The arithmetic estimate itself is unconditional; local GRH(N) identifies the Hardy realization, and the preceding wider reductions use their own GRH hypotheses.

## 1. A uniform two-form upper bound on the actual windows

By the exact giant identity, the coefficient on such a pair is \(\Lambda(r)\Lambda(s)\) before the outer sign. When either cofactor is a proper prime power at least \(N^{1/10}\), use the sparse counting proof in the giant-cofactor note with raw support \(cN\) and \(O(c)\) aliases. Its proof is unchanged by keeping \(D_*\) fixed; it gives \(O_\epsilon(cN^{-1/40+\epsilon})\). Count the union of such conditions by partitioning it into left and right-minus-left, or bound it by both absolute weights. We henceforth take, up to reflection, \(r=q^k<N^{1/10}\), \(k\ge2\), with \(s\le D_*\) any prime power. Counting both permitted choices of this proper leg is safe for an absolute majorant.

Fix cumulative \(x,y\le c\) with at least one atom, and one alias of shift \(h=jN\ne0\). Put \(t_0=N\min(x,y)\). Both raw integers are at least \(Q/D_*\gg N^{31/60}\) by giant admissibility, so \(t_0\gg N^{31/60}\). At fixed \(r,s\), the line is \(rp\pm sp'=h\) or its reflection; if \(g=(r,s)\nmid h\) it is empty. Otherwise integer candidates \(p,p'\) are two affine forms in an integer parameter of steps \(s/g\) and \(\pm r/g\); the determinant of the forms is \(\pm h/g\). The \(n,m\) restrictions place this parameter in an interval of length at most \(t_0/[r,s]\). Enlarge it if necessary to a real interval of length \(H\asymp t_0/[r,s]\). Our cuts guarantee
\[
 H\gg N^{31/60-1/10-43/120}=N^{7/120},\qquad H\ll N^{43/40}.
\]
Thus sparsity of one raw coordinate does not force this sieve into a subpolynomial interval. On the genuine prime pairs both primes are at least \(Q/D_*\), much larger than \(z=\lfloor H^{1/10}\rfloor\). Moreover, coincident giant primes do not occur in the genuine kernel: \(p=p'\) would force \(p\mid h=jN\), but \(p>2b_*\ge j\) and \((nm,N)=1\). Even including them in an upper majorant cannot change the form determinant, which is nonzero independently of whether two values happen to coincide. The prime 2 and all primes dividing either slope or the determinant are excluded from the sifting set below; good small primes are less than both giant values.

Here is a uniform Selberg sieve justification with coefficient and discriminant sizes kept. Let \(B=2rs|h|\), polynomial in \(N\); use only primes \(\ell\le z\) not dividing \(B\). Both forms together have exactly two distinct forbidden residue classes there; discard all other primes from the sifting conditions for an upper bound. On the original admissible solutions no value is divisible by a prime used, since the values are primes greater than \(z\). The Selberg quadratic with level-\(z\) divisor weights and local densities \(\gamma_\ell=2/\ell\) gives
\[
 S\ \le\ H/G(z)+O_\epsilon(z^{2+\epsilon}),\qquad
 G(z)=\sum_{\substack{d\le z,\ \mu^2(d)=1\\ (d,B)=1}}\prod_{\ell\mid d}\frac{2}{\ell-2}.
\]
In fact the standard normalizing inverse-\(G(z)\) quadratic and the explicit weights are given by [Green–Tao, *Restriction theory of the Selberg sieve*, §7 and equation (7.16)](https://www.numdam.org/article/JTNB_2006__18_1_147_0.pdf), applied with zero local obstruction at the deliberately omitted primes. The optimal coefficient magnitudes are at most \(\prod_{\ell\mid d}(1-2/\ell)^{-1}\ll_\epsilon d^\epsilon\); counting each allowed squarefree modulus by CRT gives exactly its interval density plus \(O(2^{\omega([d,e])})\) in each \(d,e\) term of the quadratic, giving the displayed remainder. This argument uses no fixed-form \(o_F(1)\) error.

For completeness, truncate the good-prime Euler product at \(z^\kappa\) for a small absolute \(\kappa>0\). Its probability weight on divisors has independent marginals \(2/\ell\); the expectation of \(\log d\) is \(2\sum_{\ell\le z^\kappa}\log\ell/\ell\ll\kappa\log z\), at most \(\tfrac12\log z\) by choosing \(\kappa\) small. Markov's inequality shows at least half its mass has \(d\le z\). Hence the denominator \(G(z)\) is at least a constant times \((\log z)^2/F(B)\), with \(F(B)=\prod_{\ell\mid B,\ell>2}(1-2/\ell)^{-1}\). Mertens' product and \(\log B=O(\log N)\) give \(F(B)\ll(\log\log(3N))^2\): primes up to \((\log(3N))^2\) give that bound on their whole product, and all larger divisors of \(B\) give a bounded multiplier since their summed reciprocals are \(O(1/\log(3N))\). Here \(\log H\asymp\log N\); \(z^{2+\epsilon}\) is negligible compared with \(H/(\log N)^2\). We obtain the uniform bound
\[
 \#\{p,p'\text{ eligible at these }r,s\}
   \ll \frac{t_0}{[r,s]}\,\frac{(\log\log(3N))^2}{(\log N)^2}.
\]
Dropping unit, roughness or endpoint requirements in constructing this majorant does not change the actual coefficient: those are only enlargements for this upper estimate.

## 2. Weights and the log-physical norm

The weighted reciprocal sum over \(r=q^k,\ k\ge2\) and \(s\) any prime power \(\le D_*\) satisfies
\[
 \sum_{r,s}\frac{\Lambda(r)\Lambda(s)}{[r,s]}\ll \log N.
\]
For distinct prime bases use \([r,s]=rs\), the absolutely convergent \(\sum_{q,k\ge2}\log q/q^k\), and \(\sum_{s\le D_*}\Lambda(s)/s\ll\log N\). For the same prime base, the double exponent sum is \(\sum_{k\ge2,l\ge1}q^{-\max(k,l)}\ll q^{-2}\), and \(\sum_q(\log q)^2/q^2\) converges. Extending the ranges this way is valid for a positive bound. After summing the two-form bound, one alias contributes at most \(t_0 F_N\) in raw weight, where \(F_N=(\log\log(3N))^2/\log N\).

Assume \(x\le y\). If any alias is active then \(y\ge1/2\), and there are \(O(y)\) possible shifts including all three orientations. Normalizing the raw weights by \(1/N\) and multiplying by the supremum \(\sqrt{xy}\) of the cumulative marker, we bound \(|A(x,y)|\ll xy\sqrt{xy}F_N\). The same holds for \(y<x\). The actual log-physical kernel is therefore bounded by \(O(\sqrt{xy}F_N)\); there is no atom below the raw lower bound \(Q/D_*>1\), and \(w_N(x),w_N(y)\ge1/2\) whenever the cumulative is nonzero. Integrating its square in \(dx\,dy/(xy)\) directly yields HS \(O(cF_N)\), without an additional full log-area loss. Add the earlier sparse component. This is a bound on a selected signed operator obtained by absolute upper estimates, not cancellation in the remaining prime-cofactor sector or a result on S/R.
