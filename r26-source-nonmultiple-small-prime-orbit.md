# R26: signed cancellation in an actual part of the R25 right nonmultiples

Keep the accepted [R25 one-giant/no-giant orbit](r25-source-one-giant-no-giant-orbit.md) (SHA-256 f9f60645c43c51df7caddda64bf7ca953989a83a5ee4381d60641eb8f4661c1b) on its fixed central raw ratio support \(J_-\times J_+\) and sum line \(n+m=N\), with even \(N\). Thus \(n=pq\), \(q\) prime in \([N^{1/10},N^{3/25}]\), \(p\) prime, and \(e\) is the least eligible prime divisor of \(m\) in \([N^{37/100},N^{39/100}]\) with \(e^2\nmid m\). Keep the original unit, sign, roughness and long-product conditions, the same \(D=D_*\asymp N^{43/120}\), and the original diagonal deletion. Write \(s=m/e\). In the actual left-over **nonmultiples of \(e\)** from R25, restrict to the pairs with
\[
 s=\ell^k s_0,\qquad
 \ell\le\log N\ \text{prime},\quad k\ge1,\quad (\ell,s_0)=1,\qquad
 P^-(s_0)>N^{1/6}.
\]
Here \(P^-(s_0)\) is the least prime factor, and by convention \(P^-(1)=+\infty\). The selected small prime is unique and is in the original \(W\): by units \(\ell\nmid N\). The power cutoffs and square deletions used in the proof are accounted for as errors rather than imposed silently on this sector.

**Claim.** The signed right-nonmultiple component on these pairs has on the physical prefix \(P_1\)
\[
 \|P_1 C_{\rm nonmult,\,one\ small}P_1\|_{\rm HS}
   \ll \frac{(\log\log(3N))^3}{\log N}+O_\epsilon(N^{-1/20+\epsilon}).   \tag{1}
\]
This is a genuine bound on the originally unestimated nonmultiple terms, not a reappraisal of the completed \(e\)-orbit. The arithmetic proof is unconditional. Local GRH(N) concerns its placement in the manuscript's Hardy realization, and using the earlier global-GRH decomposition of the original operator still requires those hypotheses. This removes neither the zero-small-prime sector nor the cases with other prime factors at or below \(N^{1/6}\), and supplies no conclusion on S or R.

## 1. Actual signed pairing, with its cutoff boundary kept

The remaining right coefficient at an eligible pair is
\(\sum_{t\mid s,\ t>D}\mu(t)\log(m/t)\), with left coefficient \(-\log q\), followed by the original negative sum-line sign. All right \(t>D\) are allowed by the product cutoff because the actual left giant \(p\) satisfies \(pD>Q\). A nonzero Möbius term uses the unique small prime \(\ell\) at most once, independent of its true exponent \(k\). Pair \(t=a\) and \(t=\ell a\) at fixed \(a\mid s_0\). Exactly,
\[
 \sum_{\substack{t\mid s\\t>D}}\mu(t)\log(m/t)
 =(\log\ell)\sum_{\substack{a\mid s_0\\a>D}}\mu(a)
  -\sum_{\substack{a\mid s_0\\D/\ell<a\le D}}\mu(a)\log(m/(\ell a)).       \tag{2}
\]
Both sides use the same least-\(e\) selection; that selection and all pair masks stay fixed throughout each divisor pair. At \(a=D/\ell\), \(\ell a=D\) is not long; at \(a=D\) only the \(\ell a\)-term is long. Equation (2) uses signed cancellation: away from the exact boundary the order-\(\log N\) marker becomes \(\log\ell\). The boundary is then estimated separately.

Discard the extremely sparse raw pairs with \(\ell^k\ge N^{1/20}\) or with any repeated remote prime \(r>N^{1/6}\) dividing \(s_0\) at least twice. To verify the raw errors, \(m\) fixes \(n=N-m\), and the left factorization is unique by the widely separated ranges for \(q\) and \(p\). For an upper bound we can sum over all eligible \(e\), ignoring the least choice (at most two anyway). Since \(e^2\nmid m\), if \(r^2\mid s_0\) then \(r\ne e\). A fixed \(e,\ell^k\) or \(e,r^2\) therefore gives at most \(N/(e\ell^k)\) or \(N/(er^2)\) raw integers. We use
\[
 \sum_{e\text{ in its band}}\frac1e\ll1,\qquad
 \sum_{\ell\le\log N}\sum_{\ell^k\ge N^{1/20}}\ell^{-k}
   \ll N^{-1/20}\log N,\qquad
 \sum_{r>N^{1/6}}r^{-2}\ll N^{-1/6}.
\]
The divisor bound and log markers give \(O_\epsilon(N^\epsilon)\) per actual pair's summed original coefficient, so these exclusions cost at most \(O_\epsilon(N^{1-1/20+\epsilon})\) raw absolute mass. All remaining \(s_0\) are squarefree, with at most three prime factors since \(s_0\le N/e\ll N^{.63}\) and their primes are \(>N^{1/6}\).

## 2. Sieve on a polynomial-length parameter, for both pieces of (2)

Use the uniform two-form Selberg upper bound exactly as proved in [R23](r23-source-double-giant-proper.md), based on [Green–Tao's explicit Selberg quadratic, §7](https://www.numdam.org/article/JTNB_2006__18_1_147_0.pdf). Its argument applies as well when the second form need not be prime but has no prime factor up to the sieve level, which is all that its majorant uses. Here is the concrete application throughout. In the equation
\[
 q p + K b=N
\]
with fixed \(q,K\) and \((q,K)=1\), all candidates are two integer affine forms for \(p,b\), of steps \(K,-q\), determinant of magnitude \(N\). The good sieve primes are those not dividing \(2qKN\); they have two distinct roots, and the omitted-prime product is \(O((\log\log(3N))^2)\) because the parameters are polynomial in \(N\). On every nonempty selection the integer parameter range can be enclosed in an interval of length \(H\asymp N/(qK)\). When \(H\gg N^\delta\) for fixed \(\delta>0\) and both forms are free of primes up to \(H^{1/10}\), the bound is \(O_\delta(H(\log\log(3N))^2/(\log N)^2)\). This is the same finite CRT and Selberg estimate, not a fixed-coefficient asymptotic. Exact endpoint, least-prime, and remaining raw divisibility conditions can be dropped **only** in these absolute upper bounds. The condition \((q,K)=1\) is valid wherever an original unit pair exists: \(q\nmid N\), and \(q\mid K\mid m\) would force \(q\mid n+m=N\).

For the complete-pair term in (2), fix \(q,e,\ell^k\) and take \(K=e\ell^k,\ b=s_0\). Since \(\ell^k<N^{1/20}\), the length is \(H\gg N^{1-3/25-39/100-1/20}=N^{.44}\). We have \(H\ll N\), and its sieve level is below \(N^{1/6}\) and below \(p\). Thus \(s_0\) satisfies the second sifting condition. Using at most \(2^3\) squarefree divisors \(a\mid s_0\), the complete-pair raw absolute mass, *after* the signed pairing (2), is at most a constant times
\[
 \frac{N(\log\log(3N))^2}{(\log N)^2}
  \sum_q\frac{\log q}{q}
  \sum_e\frac1e\sum_{\ell\le\log N,\ k\ge1}\frac{\log\ell}{\ell^k}
  \ll \frac{N(\log\log(3N))^3}{\log N}.
\]

For the boundary term in (2), \(a\in(D/\ell,D]\) with \(a\mid s_0\). Its quotient \(s_0/a>1\), because \(s_0\gg N^{1-39/100-1/20}=N^{.56}\) on the original \(m\)-support, whereas \(a\le D\). Choose a prime \(b\mid(s_0/a)\) (e.g. its least) and put \(b'=s_0/(ab)\). Fix \(q,e,\ell^k,a,b'\) and let \(K=e\ell^k a b'\). Then \(p,b\) are both prime. Whenever this choice has an eligible original pair, \(K b=m\asymp N\) with \(b>N^{1/6}\), so \(H\asymp N/(qK)\gg N^{1/6-3/25}=N^{7/150}\). Again \(H^{1/10}\) is below both primes. The positive upper estimate may now sum over all \(b'\) having at most two factors from the remote prime ranges. Their harmonic mass is \(O(1)\), since each prime is in \((N^{1/6},N^{.63}]\). There is no sign argument in this boundary upper estimate.

The essential extra saving here comes from the original short multiplicative boundary. For each \(\ell\le\log N\),
\[
 \sum_{\substack{D/\ell<a\le D\\\mu(a)^2=1,\ P^-(a)>N^{1/6}}}
      \frac1a\ \ll\ \frac{1+\log\ell}{\log N}.                         \tag{3}
\]
Indeed \(a\le D\) has at most two remote primes, and \(D/\ell>1\) for large \(N\). If \(a\) has one prime it is constrained to a multiplicative interval of factor \(\ell\); if two, fix one (whose harmonic sum over the full remote range is bounded), and the other lies in a moving interval of the same factor \(\ell\). Intersecting either interval with primes \(>N^{1/6}\), cover by \(O(1+\log\ell)\) dyadic intervals; Chebyshev's prime bound gives \(O(1/\log N)\) on each. This proves (3) uniformly without assuming cancellation in that boundary.

The marker in the boundary is \(O(\log N)\). Combining (3) with the two-form bound and the \(b'\) harmonic bound gives raw absolute mass at most
\[
 \frac{N(\log\log(3N))^2}{(\log N)^2}\, O(\log N)
  \sum_q\frac{\log q}{q}\sum_e\frac1e
  \sum_{\ell\le\log N,\ k\ge1}
          \frac{1+\log\ell}{\ell^k\log N}
 \ll \frac{N(\log\log(3N))^3}{\log N}.
\]
The elementary prime harmonic bounds used in both estimates are
\(\sum_{N^{1/10}\le q\le N^{3/25}}(\log q)/q\ll\log N\),
\(\sum_{N^{.37}\le e\le N^{.39}}1/e\ll1\), and
\(\sum_{\ell\le\log N,\ k\ge1}(1+\log\ell)/\ell^k\ll\log\log(3N)\).
The short multiplicative estimate (3), not the unsquared factor count alone, is needed to pay for the boundary marker.

## 3. Original compressed operator and a genuine nonempty witness

All bounds are on absolute raw mass only after performing the exact signed pair cancellation in (2), uniform in any further raw subrectangle of the given support. Normalize by \(1/N\), retain the original negative sign, and form the actual weighted cumulative. Its support in the log-coordinate kernel of \(P_1\) has \(x\ge\inf J_->0,\ y\ge\inf J_+>0\). On this fixed box the weight \(\sqrt{uv}\) is bounded, \(1/(xy\sqrt{w_N(x)w_N(y)})=O(1)\) and the log-area is bounded. Thus the normalized absolute bound gives the full HS estimate (1) by the original kernel formula, not just a selected probe. A reflected copy, if included, satisfies the same estimate.

The signed part is nonempty along infinitely many even \(N\) without a prime-pair asymptotic. For large \(T\), choose distinct odd primes \(q\asymp T^{.11},e\asymp T^{.38},v_0\asymp T^{.62}\) in fixed proportional intervals and put \(m=3ev_0\). Choose a prime \(p\asymp T/q\) with \(n=pq\) and \(n/(n+m)\) in the interior of \(J_-\) (or where the fixed probe product is positive). The permissible \(p\)-interval has a fixed positive relative length, so the ordinary PNT suffices. Then \(N=n+m\asymp T\) is even, all five prime bases \(p,q,3,e,v_0\) are distinct, and \((nm,N)=1\) because \((n,m)=1\). In particular \(3\nmid N\). The prime \(e\) is the unique eligible right prime, \(e^2\nmid m\), and \(s=3v_0\) has the required factorization. Its only right-long nonmultiples are \(t=v_0,3v_0\), whose coefficients sum to \(-\log(3e)+\log e=-\log3\), not zero. This witnesses a real compensation inside the remaining nonmultiples, not a change to the earlier \(e\)-orbit. It is not a lower bound of a size relevant to S.

The unestimated R25 complement still contains in particular zero-small-prime \(s\) with remote semiprime parity variation. No estimate for it is inferred from (1).
