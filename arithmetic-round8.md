# A genuine low-ordinate coherence identity and the failure of stationary phase deletion

**Result.** Actual distinct low Dirichlet-zero ordinates have a nonzero, explicitly fixed signed moment on two fixed-width arithmetic windows *above* the first physical onset. Under local GRH(N), this moment is determined up to any inverse power of log N, even if only heights H=O_A((log log N)^2) are retained for this particular smooth test. Separately, on another positive fixed-width near block in which the first Beta sum line is active, *every* stationary deweighted covariance stays an absolute distance from the true compensated target D+K along N=2^m. Thus deleting the distinct ordinates cannot establish the required o(S(N)) near error. This does not bound the true residual on the Beta-active block and does not disprove S/R.

## 1. Normalization and square-diagonal asymptotic

Work in the physical-log coordinates p=log x of arithmetic-round6/7. Remove the shared positive Hardy factors by defining the deweighted kernel ̄P= M_{√w}P_log M_{√w}/(2π) and similarly ̄D,̄K. On each of the fixed compact p intervals below these multipliers and their inverses have norms bounded by absolute constants. This is a normalization of the kernels, not a replacement of the exact D or K.

For an arithmetic test f in C_c^∞((0,∞)) let F(p)=e^(p/2)f(e^p) and ψ=F−F′. Indeed ψ(p)=e^(p/2)a_f(e^p), where a_f=f/2−u f′. The physical-log representative of v_f is √w ψ/√(2π), so pairing ̄P with ψ reproduces precisely the original character form. Likewise

    ⟨̄D ψ,ψ⟩ = (1/N)∑_{(n,N)=1} Λ(n)^2 |f(n/N)|².

For N=2^m and all large m, omitted nonunit prime powers are only powers of 2. Let L=log N. On fixed compact positive intervals, the PNT gives the ordinary square-diagonal asymptotics

    ∑_{(n,N)=1,n≤t} Λ(n)^2
       = t log t − t + O(t^(1/2)log³(2t)),
    ∑_{(n,N)=1,n≤t} nΛ(n)^2
       = (t²/2)log t − t²/4 + O(t^(3/2)log³(2t)).

For the displayed sharp error use RH for ζ, included in local GRH(N) through the conductor 1, or use an unconditional prime number theorem error of t times a super-inverse-log saving in the first line, and similarly for the second. To derive the displayed forms under RH, write the prime square sum by Abel summing log p against θ(t)=t+O(√t log²(2t)); multiply by n and Abel-sum once more for the second. Proper powers cost O(√t log²(2t)) before multiplication by n, and removing the powers of 2 is negligible. These prove, in particular,

    ⟨̄D ψ,ψ⟩ = ∫₀∞ |f(u)|²(L+log u)du + O_f(N^(-1/2)L³).

## 2. An actual signed distinct-zero moment on fixed positive windows

Choose a nonzero real f supported in I=(3/5,2/3). Put λ=9/8, d=log λ, and f_d(u)=λ^(-1/2)f(u/λ). Both I and λI=(27/40,3/4) have fixed positive width and lie above 1/2. Throughout each of I×I and λI×λI the sums lie strictly between 1 and 2, and the differences have modulus below 1. Thus there is no nontrivial arithmetic alias or Beta model line on the support of either test. The positive congruence gives exactly the diagonal. This is an exact genuine arithmetic relation, not an approximation for prime pairs. The log probes associated to f_d are F_d(p)=F(p−d) and ψ_d(p)=ψ(p−d). Since the scaling preserves ∫f² and adds d to its log-u moment, it follows that

    ⟨̄P ψ_d,ψ_d⟩−⟨̄P ψ,ψ⟩
       = d ∥F∥₂² + O_f(N^(-1/2)L³),       N=2^m.          (1)

The two test squares each lie in a fixed-width literal near band of any width B≥log(10/9). Their centers need not be the same.

The exact primitive odd-zero expansion from arithmetic-round7 gives the deweighted feature as −∑_γ e^(iγ(p+L))/(1+iγ) plus O(L²/√(Ne^p)). Let \hat F(ξ)=∫F(p)e^(−iξp)dp. The ψ integration is particularly simple:

    ∫ ψ(p)e^(iγp)dp = (1+iγ) \hat F(−γ).

Thus the common prefix denominator cancels *exactly* for this test. Using primitive ordinates of the character inducing each odd χ modulo N, with multiplicity, put

    Z_{N,H} = (2/φ(N))∑_{χ odd} ∑_{|γ|,|γ′|≤H, γ≠γ′}
         e^(iL(γ−γ′)) [e^(id(γ−γ′))−1]
                 · \hat F(−γ) overline(\hat F(−γ′)).

All same-ordinate terms cancel under translation independently of multiplicity. The expression is real by exchanging the two ordinates in the sum. Expanding the two *actual* truncated character forms and comparing with (1) gives

    Z_{N,H} = d ∥F∥₂² + O_{f,A}(L^(−A))                     (2)

for any fixed A>0 provided H=L^ε for any fixed ε>0 (the cutoff constant may depend on A,f,ε). Indeed the unit-bin zero count of arithmetic-round7 and rapid Fourier decay give per character ∑|F̂(−γ)|≪_f L and ∑_{|γ|>H}|F̂(−γ)|≪_{f,M}(L+log(2H))H^(−M) for arbitrary M. Both prefixes lie at t≍N, so integrating the explicit-formula error costs O_f(L²/√N) per feature and O_f(L³/√N) in the covariance. These estimates prove (2) without estimating any pair correlation or assuming simple zeros. Pairs with 0<|γ−γ′|≤L^(−3) contribute only O_f(L^(−1)) by |e^(id(γ−γ′))−1|≪|γ−γ′| and the same absolute mass bound, so the forced coherence is not confined to exact or extremely close coincidences.

One can choose a single fixed F improving the height in (2) to H=C_{F,A}(log L)^2. Take the centered distribution of a sum of independent uniform random variables on intervals of half-width c/j², with c small enough that the support fits inside log I after translation. Its Fourier transform is the product of the sinc factors. If |ξ| is large, the first ≍√|ξ| factors have |ξ|c/j²≥2 and therefore modulus ≤1/2. The product has |F̂(ξ)|≪exp(−c′√|ξ|), and the distribution has a compact smooth density by Fourier inversion with all derivative moments finite. Take this nonzero density for F and f(e^p)=e^(−p/2)F(p). The tail error in the covariance is then ≪L²e^(−c″√H) by the same bin estimate, giving the claimed cutoff. This lower height concerns this fixed smooth witness, not arbitrary unit vectors or the whole near operator.

In particular a phase calculation giving zero expectation to every distinct-ordinate covariance cannot describe the true low-ordinate object to o(1) even on these positive, fixed-scale tests. The result is a genuine nonstationary translation moment of order one; it is not a claim about how individual zero pairs contribute.

## 3. The exact Beta-active benchmark is also nonstationary

To test the method directly in a sector containing a genuine sum-family support, take the fixed interval

    J=[log(1/2),log(9/16)]

and n→∞ along N=2^m. For x=e^p,y=e^q with p,q∈J, the prefixes 0<u≤x and 0<v≤y contain no difference line (x,y<1), and only the negative Beta line u+v=1. Thus in the *deweighted* exact benchmark C=̄D+̄K,

    C(p,q)=e^(−|p−q|)[L/2+min(p,q)/2−1/4]
           − S(N)/(xy) ∫_{1−y}^x √(u(1−u)) du
           + O(N^(-1/2)L³).                                (3)

The error is solely from the square diagonal; the Beta expression is exact. The line integral is zero when x=y=1/2 but positive in the interior. Here S(N)=2 C₂≥1, since the product defining C₂ is over n=p−1⊂{2,3,…} and ∏_{n≥2}(1−1/n²)=1/2. It is also bounded above by 2.

Write I(x,y) for the integral in (3). The derivative of I(x,y)/(xy) under simultaneous log translation (x,y)→(e^s x,e^s y), evaluated at points of the displayed square, is

    [x√(x(1−x))+y√(y(1−y))−2 I(x,y)]/(xy) ≥ 88/81 >1.

Indeed on the relevant range √(u(1−u))≥15/32 for the two endpoint factors, x+y≥1, 2I≤x+y−1≤1/8, and xy≤81/256. The simultaneous derivative of the deterministic D expression in (3) is +(1/2)e^(−|p−q|), at most 1/2, and its leading L term is translation invariant. Thus for a fixed small positive shift d₀ inside J, the deterministic part of C(p+d₀,q+d₀)−C(p,q)≤−d₀/2 on any translated sub-square contained in J, with the same uniform o(1) error.

For any stationary deweighted kernel A_N(p−q), tested on this square, take one fixed nonnegative unit bump supported inside the lower part of J and its translate by d₀, also inside J. Their quadratic forms for A_N are identical, whereas those for C differ by at least a fixed positive constant for all large N. Consequently

    inf_A_N ∥1_J(A_N−̄D−̄K)1_J∥op ≥ c>0               (4)

for every large modulus in the dyadic-power family. Only stationarity is used, not positivity, the Fourier law, numerical values of the zeros, or absence of multiplicities. Restoring the actual Hardy weights loses only a constant. In particular the covariance obtained by retaining only equal-ordinate terms of the true expansion is in this class, as is a covariance that assigns independent centered phases to unequal ordinates. Such a replacement cannot be centered by the exact D+K to o(S(N)) on this Beta-active fixed near sector. If the genuine S-scale centered bound holds, it must supply nonstationary distinct-ordinate contributions of at least this size on this sector. Formula (4) itself does not assert that genuine bound, and does not decide the residual's size on J when the actual unequal-ordinate terms are retained.
