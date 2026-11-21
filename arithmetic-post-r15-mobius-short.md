# Pointwise removal of the short Möbius-divisor component

**Claim (global Dirichlet GRH).** For every sufficiently large even N and every 1≤b≤N, put Z=ceil(4bN) and D=floor(Z^{1/3}). In the physical coordinate x=n/N, let Π_b project to the full prefix 0<x≤b; projection in the log representation is 1_{p≤log b}. Define the genuine short Möbius-divisor weight

    Λ_D(m)=∑_{d|m,d≤D} μ(d) log(m/d).

Use the ordinary three signed line families of Li–Liu after exact diagonal subtraction, but on each line replace Λ(n)Λ(m) by [Λ(n)Λ_D(m)+Λ_D(n)Λ(m)]/2. Keep the exact singular series for each model line, and use the same physical Volterra/Hardy representation. The resulting real symmetric centered **prefix** operator C_{N,b,D} satisfies, uniformly in N,b,

    ∥C_{N,b,D}∥HS ≪_ε b^(11/12) N^(-1/12+ε).               (1)

For example b=N^{3/40} gives O_ε(N^(-7/480+ε)); there is no averaging, exceptional set, or restriction to doubled squares. This removes a component of the true prefix covariance using the actual Euler-product identity for Λ. It does **not** bound the full prefix operator: the complementary long sum Π_b T_N Π_b−C_{N,b,D} is specified in §4 and remains unestimated. In particular neither S nor R follows.

Global Dirichlet GRH is used for auxiliary progressions d≤D and RH for ζ; the original operator identification uses local GRH(N). The construction is a centered arithmetic decomposition on the prefix; the two pieces are not asserted to be covariance-positive, nor to be obtained by separately replacing the full (L)-functions.

## 1. The Möbius series already gives the correct local density

For even h≥2 let

    F_h(s)=∑_{(d,h)=1} μ(d)/(φ(d)d^s) = ζ(1+s)^(-1) H_h(s).

The Euler product converges absolutely for Re s>0. Its ratio factor at p∤h is [1−p^(-s)/(p−1)]/[1−p^(-1−s)]; at p|h it is [1−p^(-1−s)]^(-1). On evaluating at s=0, the ratio factor off h is p(p−2)/(p−1)^2, while on h it is p/(p−1). Their product is exactly S(h), with the factor 2 supplied by p=2. Thus analytic continuation near zero gives

    F_h(0)=0,       F_h′(0)=S(h).                             (2)

For explicit uniform tails put a_h(d)=d μ(d) 1_{(d,h)=1}/φ(d). Its Dirichlet series is ζ(w)^(-1)H_h(w−1). The Dirichlet coefficients c_h(v) of H_h(w−1) have c_h(1)=1 and for j≥1,

    c_h(p^j) = −1/(p−1) if p∤h,      c_h(p^j)=1 if p|h.

It follows by an absolute Euler product that for fixed σ>0 and each η>0,

    ∑_{v≥1}|c_h(v)|v^(−σ) ≪_{σ,η} h^η.

Off h the Euler factors converge absolutely by the extra 1/(p−1); on h the finite product is ∏_{p|h}(1−p^(-σ))^(-1), bounded by C_{σ,η} h^η since for all sufficiently large p each factor is ≤p^η. Now use [the RH Mertens bound, Titchmarsh Theorem 14.25(C)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf), ∑_{n≤U} μ(n)≪_η U^{1/2+η}, in the convolution a_h=μ*c_h. This gives ∑_{d≤U}a_h(d)≪_η h^η U^{1/2+η}. Partial summation proves convergence of the two series at s=0 and uniformly in even h

    ∑_{d≤D,(d,h)=1} μ(d)/φ(d) = O_η(h^η D^(-1/2+η)),
    ∑_{d≤D,(d,h)=1} μ(d)log d/φ(d)
        = −S(h)+O_η(h^η D^(-1/2+η)log(2D)).                (3)

One may identify these limits and the derivative with (2) termwise, since the same partial-summation bound gives locally uniform convergence and differentiability in a neighborhood of zero. In particular the density in (2) is not imported from an assumed prime-pair asymptotic.

## 2. Individual short-leg cancellation on every hard rectangle

Fix a shift h=jN with 1≤j≤2b and one of the actual relations n+m=h, n−m=h or m−n=h. Restrict both normalized positions u=n/N, v=m/N to any hard rectangle in [0,b]². Let V be the length in the first normalized coordinate of this line inside the rectangle, so V≤b; the continuous line measure is du with v determined by u. Then

    (1/N)∑_{line in rectangle,(nm,N)=1} Λ(n)Λ_D(m)
       = S(h)V + O_ε(Z^(5/6+ε)/N).                          (4)

To see this expand the short divisor leg and sum first over n with d|m. The first coordinate remains an interval, since the line determines m with slope ±1. If (d,N)>1 that term is empty. If (d,N)=1 but (d,h)>1, then all n on this progression are divisible by some fixed p|(d,h), so nonzero Λ(n) may occur only at powers of p. Their total Λ weight is O(log Z); their additional log(m/d) marker is at most O(log Z) in magnitude. The total error from these d is O(D (log Z)^2) before normalization. For the other d, n lies in a reduced residue ±h mod d. Removing the n that are not units modulo N costs at most the total Λ mass of powers of primes dividing N, O((log Z)^2) per d before inserting the log marker. Since h is a multiple of N, unit n and unit m are then equivalent.

On the good reduced classes, [the GRH PNT in progressions](https://arxiv.org/abs/2301.13457) gives the prefix main term t/φ(d) with O(√Z (log Z)^2) error uniformly up to Z, also under restriction (n,N)=1 by the preceding observation. For d≥3 use Lee, Corollary 1.1, for t≥max(e^10,d); the shorter endpoints t<d≤D≪√Z and bounded t are harmless by Chebyshev. For d=1 use the ordinary RH prime number theorem; d=2 is excluded on the good classes since h is even. The raw weight log(m/d), with m affine of slope ±1, has supremum and total variation O(log Z) on m≥1. Partial summation on that interval costs O(√Z (log Z)^3) per good d. Extending any main-term endpoint from n,m≥1 to n,m>0 changes its integral by O(log Z) per d: only raw segments of total length O(1) are added and the logarithmic singularity at m=0 is integrable. Endpoints of hard intervals cost at most the same error. Consequently after summation the normalized expression is

    (1/N) ∫_{raw first-coordinate overlap}
       [ (log m) ∑_{d≤D,(d,h)=1} μ(d)/φ(d)
                      −∑_{d≤D,(d,h)=1} μ(d)log d/φ(d)] dn
      +O(D√Z (log Z)^3/N).

Each raw integral of log m has absolute size O(Z log Z) (also near m=0). Apply (3), with h≤Z and D≈Z^{1/3}; its error and the progression error are O_ε(Z^{5/6+ε}/N) after choosing the auxiliary η sufficiently small. The main term is S(h)V with the correct sign. By exchanging coordinates (4) holds also for Λ_D(n)Λ(m). The same calculation works for the sums and both orientations of differences; the signed line signs enter only in the next step.

## 3. From hard rectangles to the actual cumulative Hardy kernel

Let μ^{short} be the signed arithmetic-minus-model measure on [0,b]² built from the symmetrized short weights and the exact line densities. The two difference lines have positive signs and the sum line has negative sign before subtracting the model. The line n=m does not occur: it was removed exactly before the split. There are O(b) nonzero shifts. By (4), every hard rectangle satisfies

    |μ^{short}(I×J)| ≪_ε U,     U=b^{11/6} N^(-1/6+ε).

Write A(x,y)=∫_{0<u≤x,0<v≤y}√(uv)dμ^{short}(u,v). The positive layer cake for √u√v gives |A(x,y)|≪_ε √(xy)U. A complementary absolute bound for all positive x,y≤b is

    |A(x,y)|≪_ε Z^ε (log Z)^2 (xy)^{3/2}.                 (5)

For (5) suppose x≤y. Nonzero terms require x+y≥1, hence y≥1/2. For each n≤Nx there are O(y) possible partners from the shift lines. The pointwise weights satisfy |Λ_D(m)|≤d(m)log Z≪_ε Z^ε log Z (and likewise with n and m interchanged). Multiply by √(xy) and divide by N. For the continuous model there are O(y) lines, each with normalized length at most x and singular series O(log Z), giving the same bound; if x+y<1 all lines are absent exactly. No bound from the upper sieve is applied to the signed surrogate Λ_D.

The log kernel is 2πA(x,y)/(xy√(w_N(x)w_N(y))), with w_N(x)=[(Nx)^(-2/log N)+(Nx)^(-1/4)]^(-1). On x,y≥1/N, w_N≥1/2; combine the hard-rectangle weighted estimate and (5) multiplicatively to bound the squared log kernel by O_ε(U Z^ε (log Z)^2). Its log area is O((log N)^2) since b≤N. On x<1/N, y≥1−x≥3/4 whenever nonzero, and (5) bounds the squared log kernel by O_ε(Z^{2ε} (log Z)^4 xy/[w_N(x)w_N(y)]). Integrating in dp dq=dxdy/(xy) there costs O_ε(Z^{2ε}b N^-1 (log Z)^4): ∫₀^{1/N}dx/w_N(x)≪1/N by the two explicit integrable exponents, and ∫_{3/4}^b dy/w_N(y)≪b. The other edge is symmetric. These bounds give (1) after taking a square root and relabeling ε.

## 4. The precise remaining arithmetic

The identity Λ(m)=(μ*log)(m) gives exactly

    Λ(m)−Λ_D(m)=∑_{d|m,d>D} μ(d) log(m/d).

On each orientation, with h=jN, write m=kd. The complementary measures in Π_b T_N Π_b−C_{N,b,D} contain only the genuine weighted tails of the form

    (1/N) ∑_{2≤k≤Z/D} (log k)
      ∑_{d>D, (kd,N)=1, 0<n=h±kd≤Z}
         μ(d) Λ(n) · 1_{(n/N,kd/N) in the specified rectangle},

and the reflected orientation n=kd−h, with one half from each symmetrized leg and the original outer signs. The k=1 coefficient is zero, and the unit condition removes non-coprime k automatically. These are the kernels before the same √uv cumulative and Hardy weighting, not separately bounded absolute values. The true operator's exact model has already been compensated in (1); no new conjectural main term is assigned to these tails. Obtaining sufficient cancellation in this remaining **signed long-divisor Möbius–prime family**, controlling the relevant exterior crosses, and removing full-uniformity gaps remain necessary to reach S. GRH individual progression estimates here controlled the short congruence, not this residual two-variable correlation.
