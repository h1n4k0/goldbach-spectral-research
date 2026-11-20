# A quantitative high-zero cutoff on the entire genuine near band

**Result and limitation.** Let L=log N, 0≤B≤L/2, and H≥2. In the exact physical-log coordinates used in arithmetic-round6.md, replace the true odd-character Gram by the Gram of the explicit-formula features retaining only Dirichlet zeros |γ|≤H. Keep the exact diagonal D and Beta model K. On the *whole literal* band |p−q|≤B, with an exact zero mask at the lower no-alias corner, the resulting near residual differs in operator norm from the actual one by

    O((1+B)(Lη+η²)),     η=(L+log(2H))/√H + L² e^(B/2)/√N.       (1)

This is uniform in every sufficiently large even modulus under its local GRH(N). At fixed B>0, H=L^(2A+4) makes the error O_B(L^(-A)) for any fixed A>0. For arbitrary B≤L/2, H=L^(2A+6) suffices. The band itself does not shrink. This excludes higher zero ordinates as a necessary obstacle to inverse-log precision in the near band. It does *not* compare the retained low-zero Gram with D+K, prove an inverse-log bound for the retained residual, or say anything about S/R outside this approximation.

## 1. Genuine weighted prefix feature and its exact-zero cutoff

Use dimensionless x=e^p, physical prime prefix t=Nx, and

    w(x)=1/((Nx)^(-2/L)+(Nx)^(-1/4)).

The log-coordinate Gram P is the average over odd characters of feature products b_χ(p) conjugate(b_χ(q)), with weight 2/φ(N) and with the *same fixed* normalization as the physical Hardy transform. From the Volterra insertion in arithmetic-round6.md, up to that fixed square-root factor,

    b_χ(p)= [1/(t√w(e^p))] ∑_{n≤t} Λ(n)χ(n)√n.

Put p₀=−B−log 2. If |p−q|≤B and min(p,q)<p₀ then x,y≤1/2, the true residual kernel vanishes, and only the cancellation of the exact diagonal is involved (positive congruence only diagonal, negative no unit solutions, and Beta lines have no mass). Apply both near masks only on p,q≥p₀; the true masked near residual is unchanged. This cutoff is necessary because the *truncated* zero representation does not itself have this no-alias property. On the remaining region t≥N e^(−B)/2≥√N/2, and w≥1/2.

Write χ* for the inducing primitive character. For almost every t≥2, under its GRH,

    (1/t)∑_{n≤t} Λ(n)χ(n)√n
       = −∑_{ρ=1/2+iγ of χ*} t^(iγ)/(1+iγ) + O(L²/√t),       (2)

with the zero series understood in local L² in log t. To verify the normalization and convergence, one may start from the integrated explicit formula in [E. S. Lee, arXiv:2301.13457, p. 15](https://arxiv.org/pdf/2301.13457#page=15). For an odd primitive character its analytic remainder has derivative −L'/L(0,χ*)+O(1) on t≥2. The functional equation and the standard GRH Ψ bound give |L'/L(0,χ*)|≪L²: at 1 the bound follows by Abel-summing the convergent nonprincipal Mangoldt series, and Γ derivatives at the odd parity arguments are bounded constants. Differentiating the integrated zero formula in weak sense gives −∑ρ t^ρ/ρ for Ψ(t,χ*); its derivative series converges in local L² by the bin estimate in §2 (coefficient 1/ρ has the same size there). Abel-summing with √n from t=2 transforms the zero coefficient into −1/(ρ+1/2): in each truncation the boundary term has coefficient −1/ρ and the integrated contribution is +1/[2ρ(ρ+1/2)], yielding exactly −1/(ρ+1/2). The lower endpoint's zero constants converge absolutely, since they carry 1/[ρ(ρ+1/2)]. The remaining nonzero part of Ψ is O(L²), contributing O(L²√t) before division by t. The imprimitive correction adds at most O(L√t) before division, since each removed prime contributes through a geometric sum of √(p^j) of size O(√t) times log p and ∑_{p|N}log p≤L. Differences at exact prime-power endpoints have measure zero in the kernels. All conductors divide N; no global GRH is needed.

Define b_{χ,H}(p) by using only |γ|≤H in (2) and dividing by √w with the original fixed normalization. The approximate Gram P_H keeps the true odd family/normalization, goes over all characters modulo N, and retains multiplicities of the actual primitive zeros. Define the approximate near residual as the kernel P_H−D−K on p,q≥p₀ and |p−q|≤B, zero elsewhere.

## 2. High ordinates in a fixed-width log window

Let I be any real interval of length at most 1. For finite coefficients a_j at frequencies γ_j let m_k=∑_{γ_j∈[k,k+1)}|a_j|. Then

    ∫_I |∑_j a_j e^(iγ_j p)|²dp ≪ ∑_{k∈Z} m_k².            (3)

Use a positive translated squared-sinc envelope, bounded below on I, whose Fourier transform is compactly supported in a fixed frequency interval. Only O(1) neighboring integer bins interact after expanding the square. The cross-bin terms are bounded by Cauchy–Schwarz via ∑_k m_k m_{k+ell}≤∑_k m_k². All constants are independent of the location of I or of any intervening short zero gaps.

The standard unit-bin count #{γ∈[k,k+1)}≪log(N(2+|k|)) follows from the zero counting formula, for example [Lee, Lemma 2.2](https://arxiv.org/pdf/2301.13457#page=5). It counts multiplicities; ordinates near zero and both signs are included. For a_j=e^(iγ L)/(1+iγ), or for the derivative-series coefficients 1/(1/2+iγ), this gives

    m_k ≪ log(N(2+|k|))/(1+|k|).

Summing squares over all k gives O(L²). Restricting to |γ|>H gives O((L+log(2H))²/H), by an integral comparison (a boundary bin changes at most the same order). The tail bounds for finite subseries imply convergence in L² on every compact log interval and justify the derivative step and Abel passage in (2).

Since p≥p₀ and w≥1/2 there, every such unit interval in the truncated region satisfies

    ∫_I (2/φ(N))∑_{χ odd}|b_{χ,H}(p)|²dp ≪ L²,
    ∫_I (2/φ(N))∑_{χ odd}|b_χ(p)−b_{χ,H}(p)|²dp ≪ η².

The first estimate follows directly from (3), independent of H. The second adds the error in (2), with t≥N e^(−B)/2. No averaging in N or smoothing of the final near-band mask occurs here.

## 3. Literal-band operator comparison

Split the physical log line p≥p₀ into unit cells. On any cell pair I×J the covariance difference P−P_H consists of two cross terms with one error feature and one retained feature, and one term with two error features. By Cauchy–Schwarz over characters pointwise, the Hilbert–Schmidt norm on that cell pair is bounded by C(Lη+η²) using §2. Multiplying the kernel by the band indicator can only decrease that Hilbert–Schmidt bound; there is no assumption that arbitrary kernel masks contract operator norm.

Each unit cell has O(1+B) neighbors intersecting |p−q|≤B, both as an input and an output. The scalar Schur test on the matrix of these block operator bounds gives (1). The common D and K cancel exactly in the difference. For the power cutoffs stated above log H=O_A(log L) and the N-dependent error is exponentially smaller than any inverse log throughout B≤L/2. The retained Gram before masking has finite rank; the literal masked kernel is not asserted to have finite rank, since band multiplication does not preserve it.

**Remaining bottleneck.** In each modulus the low-ordinate covariance, retaining both same-ordinate and distinct-ordinate terms, must still be centered by the exact D+K to additive inverse-log operator precision on a fixed-width near band. The calculation controls the *tail* without solving that signed covariance. One-level zero counts are used solely for the tail; they determine no cancellation of the retained Gram.
