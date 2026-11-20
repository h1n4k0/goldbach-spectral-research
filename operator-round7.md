# Round 7: the actual cross out of a thin first-period row

This note addresses a genuine crossing sector of the [Li–Liu operator](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf) under its local GRH(N). The operator is put in the exact physical L²(dx) coordinates of source-round2.md §1, not a selected Mellin probe. Unlike the onset square of Round 6, the input is permitted anywhere, or in any specified larger physical prefix. The one remaining coarse output row is separated and not claimed small at the R scale.

Let L=log N, S=the Goldbach singular series, α=1/L, β=1/8, w(x)=(Nx)^(2α)/(1+(Nx)^(−2(β−α))), and r(x)=x^(−3/2)w(x)^(−1/2). Fix 0<a<b<1. Take any interval J⊂[a,b] of length ε and left endpoint x₀; suppose H=Nε≥1. Let P_J be multiplication by its indicator; set e_J=r1_J/||r1_J||₂ and F_J=P_J−e_J⊗e_J. Both are true orthogonal projections, and F_J has removed exactly one mode on J. Write T for the conjugate of the actual T_N and P,D,K for its separate conjugated character, diagonal and model components as in T=P−D−K.

**Full-line cross:** uniformly in such J,

    ||P_J T||_HS ≪_{a,b} L^(3/2) sqrt(ε),
    ||F_J T||_HS ≪_{a,b} ε L² / sqrt(log(2+H)) + S ε^(3/2).          (1)

**Cross into a possibly larger prefix:** for any A≥1, with P_{≤A} denoting its true physical projection,

    ||F_J T P_{≤A}||_HS ≪_{a,b} S ε^(3/2) sqrt(A) · L log(2NA)/log²(2+H).   (2)

Adjoints give the reverse crossings. For fixed A, ε=N^(−1/3) makes (2) o(δ_N). For the full line, choosing ε=N^(−1/2)L^(−c) with any fixed c>0 makes the second bound of (1) o(δ_N). Here δ_N=sqrt(S/N)L^(3/2). The strips can be centered at 1/2, or anywhere in the first physical period separated from 0 and 1. These maps can include actual Goldbach and difference aliases in their input; the discarded one-dimensional coarse mode is not small by these conclusions.

## 1. Local character and diagonal row mass

The actual Hardy atom for d_n(s)=n^(−s)/(1+s) is, in physical coordinates,

    d_n(x)=sqrt(2π) r(x)(n/N) 1_{n≤Nx}.

This follows by the inverse-height Fourier transform of 1/(1+s), a causal exponential on the full log-coordinate line, followed by multiplication by the Hardy weight sqrt(1+exp(−2(β−α)log(Nx))) and by x^(−1/2) for the change of measure. Likewise the atom for gχ(s)/(1+s) has the exact representative

    pχ(x)=−sqrt(2π) r(x) N^(−1) Σ_{n≤Nx} Λ(n)χ(n) sqrt(n).

The latter is first proved on the absolute-convergence line and moved to α by testing against compact Mellin weights and local GRH, or directly by spectral-round2.md (2). Thus P is the average of pχ⊗pχ over odd χ and D=Σ_{(n,N)=1}(Λ(n)²/n)d_n⊗d_n. The source gives ||P||+||D||≪L².

For x≤b<1, any family of nonnegative coefficients c_n supported on n≤Nx satisfies

    Av_odd χ |Σ c_n χ(n)|² ≤ Σ c_n².

Indeed the equality congruence forces n=m on this range, and the opposite congruence contributions have negative sign and are nonnegative before multiplication by that sign. Nonunits are zero. This applies equally to the full prefix and to the incremental interval Nx₀<n≤Nx; its weights Λ(n)sqrt(n) are nonnegative. The character atoms and the diagonal formula therefore imply

    tr(P_J P P_J) + tr(P_J D P_J) ≪_{a,b} (ε/N) Σ_{n≤bN} Λ(n)² ≪ ε L.

The constant prefix n≤Nx₀ in pχ on J is a scalar multiple of r1_J and is eliminated by F_J, while the same holds termwise for d_n if n≤Nx₀. Using that F_J is a contraction on the remaining part gives

    tr(F_J P F_J) + tr(F_J D F_J) ≪_{a,b} (ε/N) Σ_{n/N∈J} Λ(n)².

A standard one-residue upper-bound sieve on an interval of length H gives Σ_{n/N∈J}Λ(n)²≪(H+1)L²/log(2+H). Use a cutoff z=H^c for a sufficiently small fixed c, and an upper sieve level H^d for a fixed d>c. Powers with base >z pass this sieve; each is weighted at most L². For bases ≤z, the contribution per prime to the sum of Λ² up to N is at most L log p≤L², so their total is O(z L²), absorbed by the same bound, including bounded H. The proof is the one-dimensional version of the short-interval sieve used in operator-round6.md. For a positive trace-class operator V and orthogonal E, ||EV||_HS²=tr(E V² E)≤||V||tr(EVE). Applying this to P and D, with H+1≤2H, proves their contributions to (1).

## 2. Signed model row, with no finite-prefix truncation

For u∈[0,b], u<1 means that the two possible families in the second coordinate are k+u (positive difference) and k−u (negative sum), k≥1; a positive difference with u larger than the second coordinate by an integer is impossible. The model cumulative function in the exact physical representation is therefore

    M_K(x,y)=∫_0^x sqrt(u) Σ_{k≥1} S(kN)
         [sqrt(k+u)1_{k+u≤y}−sqrt(k−u)1_{k−u≤y}] du.

There is no contribution for y<1−b. For y≥2, where both indicators hold, the square-root difference is O_b(u/sqrt(k)); sum using Σ_{k≤Y} S(kN)≪SY (positive divisor expansion, with Σ a_{N,d}/d bounded) and partial summation. When one indicator is missing, there are at most two endpoint integers k∈(y−u,y+u], and their contribution is O_b(S sqrt(y) loglog(5+y)) by S(kN)≪S loglog(5+k). The latter bound follows by splitting prime divisors of k at log(3+k), applying Mertens to the small primes and ∑_{p|k}log p≤log k to the remainder. Bounded y≥1−b is immediate. Thus, for all x,x₀∈[a,b],

    |r(y) M_K(x,y)| ≪_{a,b} S h(y),
    |r(y)[M_K(x,y)−M_K(x₀,y)]| ≪_{a,b} S |x−x₀| h(y),
    h(y)=1_{y≥1−b} loglog(5+y)/(1+y) ∈ L²(0,∞).

The model kernel is 2π r(x)r(y)M_K(x,y). The first envelope gives ||P_J K||_HS≪S sqrt(ε); the second gives ||F_J K||_HS≪S ε^(3/2), since the row built by replacing M_K(x,y) by M_K(x₀,y) has output exactly in span(e_J). This step uses real cancellation of the two continuous alias families; summing both absolute masses would leave a nonintegrable bound as y→∞. With S≪loglog N this completes (1).

## 3. A sharper asymmetric bound into a finite physical prefix

Use the exact full discrepancy kernel 2π r(x)r(y)M_N(x,y), not the separate terms. Subtract in the kernel on J×(0,A] the rank-one row 2π r(x)1_J(x)r(y)M_N(x₀,y). It is well-defined on that prefix and killed by F_J. What remains has cumulative x variable restricted to x₀<u≤x. Again it vanishes for y<1−b. For a single alias m=kN±n, with n in this window of length at most H, the short-interval two-form upper sieve from operator-round6.md gives

    Σ Λ(n)Λ(kN±n) ≪ S(kN) (H+1)L log(2NA)/log²(2+H),

uniformly for all positive participating coordinates and 1≤k≤A+1. The proof and small-base corrections are identical, with the second coordinate weight now bounded by log(2NA) instead of L. Within that alias sqrt(uv)≪_b sqrt(k). The positive divisor expansion gives Σ_{k≤y+b} S(kN)sqrt(k)≪S(1+y)^(3/2). The same continuous model contribution is bounded by S ε(1+y)^(3/2) and absorbed by the displayed sieve factor. On y≥1−b, r(y)(1+y)^(3/2) is bounded, and r(x) is bounded on J. Combining these facts shows that the kernel of the remainder is bounded in absolute value by O_{a,b}(S ε L log(2NA)/log²(2+H)). Its square support has area at most ε A, giving (2). No sign cancellation between individual prime pairs is hypothesized in this prefix estimate.

## 4. What is still uncontrolled

The full row has the exact decomposition P_J T= e_J⊗ω_J + F_J T, where ω_J=T e_J (the operator is self-adjoint). Its actual kernel row in real coordinates is

    ω_J(y) = 2π r(y) ||r 1_J||₂^(−1) ∫_J r(x)² M_N(x,y) dx.

In particular the moment-free gain is a genuine operator block estimate, not a claim that replacing the full row is costless: the remaining mode involves the whole cumulative signed arithmetic discrepancy. In the special first-alias onset square its row can be tiny because no full alias lines contribute from the prefix. Outside that square the same geometric argument provides neither a small coarse row nor uniform control over the entire near band from Round 5. No bound on the largest full-space eigenvalue follows.
