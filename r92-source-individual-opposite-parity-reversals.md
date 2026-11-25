# At least two sign reversals of the individual opposite-parity phases

Use the true moving floors and three strict divisor/product tests of the [four actual parity laws](r89-source-four-actual-parity-phases.md), with its actual cofactor parities and its unconditioned normalization. We evaluate the two **individual** opposite-parity phases at equal floors $a=b=d$. These are not the same-minus-opposite aggregate. The arithmetic conclusion uses only the inherited unconditional mean-square estimate and its common exceptional set on fixed bounded boxes; no pointwise assertion at specified targets or conclusion about Hypothesis S is made.

Let $x_*$ be the unique positive root of the uncapped phase $\Psi$ in the [Dickman phase theorem](r86-source-dickman-capped-phase-chart.md), and put $d_*=10+x_*/2$. In particular $85/8<d_*<20$. The two actual opposite-parity leading phases coincide along the diagonal:

$$
     \phi_{+,-}(d,d)=\phi_{-,+}(d,d)
       =\tfrac14\big(\Phi(d,d)+P(d,d)\big).
 \tag{1}
$$

Both are negative for $0\le d\le10$ and $d\ge d_*$, and both are at least $77/7560>0$ for $21/2\le d\le85/8$. Thus their common deterministic phase has sign reversals in the two disjoint intervals $(10,21/2)$ and $(85/8,d_*)$, in the sense that the signs at each pair of endpoints are opposite and at least one zero lies between. We do not assert that these are the only reversals or that their zeros are simple.

## 1. Diagonal reduction with the actual capped coefficient

For opposite cofactor parities $\varepsilon_1\varepsilon_2=-1$. At $a=b=d$ the two mixed terms in the four-parity formula are $-\varepsilon_2Q(d,d)-\varepsilon_1Q(d,d)=0$, while the ordinary contribution is $+P(d,d)$. This gives (1) for each individual parity slice; it is not an identity asserting that the two exact finite-target sums agree.

The [strict ordinary-phase sign](r91-source-monotone-parity-kink-positive-two-parity.md) gives $P(a,b)<0$ for all nonnegative floors. The [capped long-floor theorem](r85-source-capped-long-floor-orbits.md) gives $\Phi(d,d)=0$ for $d\le10$ and $\Phi(d,d)=\Psi(2d-20)$ for $10<d\le20$. For $d_*\le d\le20$ the latter is nonpositive. For $d\ge20$ the actual both-capped sign in the Dickman phase theorem gives $\Phi(d,d)<0$. These cases prove the stated negative regions. The root bounds $4\sqrt{\mathrm e}<x_*<51/5$ imply the claimed location of $d_*$.

It remains to get a strict positive region with the ordinary term still retained. Along the diagonal with $21/2\le d\le85/8$ we have $1\le 2d-20\le5/4$. The support of the local signed short measure has no positive point below $5/4$, and its atom at zero has mass one. Thus in the capped theorem's area integral only the pair of zero atoms can contribute a nonzero area in this range. If a coordinate equals $5/4$ at its upper endpoint the area is zero for that term. Consequently

$$
                   \Phi(d,d)=\tfrac12(2d-20)^2\ge\tfrac12 .
 \tag{2}
$$

## 2. An explicit Dickman tail leaves the positive sign

Let $A$ and $M$ be the signed cumulative and its primitive in the Dickman phase theorem. Extend them by zero to negative arguments. To bound the uncapped tail put $\rho_4=4e^{\gamma_{\rm E}} f$, where $f$ is its scale-four Dickman probability density. This normalization gives $0<\rho_4\le1$ on the positive half-line and a nonincreasing density there. Its real integral identity yields $\rho_4(t)\le4\rho_4(t-4)/t$ for $t>4$. For $t\ge18$, all four iterations are allowed and their factors have denominators $t/4-j\ge9/2-j$, $0\le j\le3$. Hence

$$
             \rho_4(t)\le
             \frac{1}{(9/2)(7/2)(5/2)(3/2)}=\frac{16}{945}.
 \tag{3}
$$

Here the last shifted factor is at most one. In the same formulas $A=\rho_4-\pi*\rho_4$ and $M=\rho_4*\kappa$, with $\pi$ the old-prime probability on $[5/4,v]$, $v=7/4$, and $\kappa$ its survival function on $[0,v]$. If $x\ge20$, the two nonnegative terms in $A$ are each at most $\rho_4(x-v)$ by monotonicity; their absolute difference is at most that same bound, without a factor of two. Since $x-v\ge18$ and $\int\kappa\le v$, (3) proves

$$
               |A(x)|\le16/945,\qquad M(x)\le16v/945
                          \quad(x\ge20).
 \tag{4}
$$

The sign of $A=M'$ is positive up to $v$, zero from $v$ to $4$, and negative after $4$; moreover $M$ tends to zero at infinity. Thus $\int |A|=2M(v)\le 2v$, the inequality following also from $0\le\rho_4\le1$ and the mass of $\kappa$. Positivity of that convolution and $\int f=1$ give $\int M=4e^{\gamma_{\rm E}}\int\kappa\le12v$, using $\gamma_{\rm E}\le1$ and $\mathrm e<3$.

For $C\ge40$, split the exact formula $\Psi(C)=\int_0^C A(s)M(C-s)\,ds$ at $C/2$. On the first half use (4) for $M(C-s)$ and on the second use it for $|A(s)|$. The resulting bound is

$$
       |\Psi(C)|\le \frac{16}{945}\left(v\int |A|+\int M\right)
                 \le \frac{434}{945}<\frac12 .
 \tag{5}
$$

We now compare the **capped ordinary** phase, rather than dropping that cap. The exact ordinary-tail expression in (7) of the four-parity law at $a=b=d$ is

$$
   P(d,d)=\Psi(C)-2\int_0^d A(C-r)M(r)\,dr,\qquad C=2d+20 .
 \tag{6}
$$

It subtracts the two disjoint missing tails of the ordinary triangle. Here $C-r\ge d+20>4$ and $M(r)>0$ for $r>0$, so (6) gives $P(d,d)\ge\Psi(C)$ (strictly if $d>0$). In the range of (2), $C\ge40$ and thus

$$
        \tfrac14(\Phi(d,d)+P(d,d))
               \ge \tfrac14(1/2-434/945)=77/7560 .
$$

Together with the already proved negative regions and continuity of the exact phase, this proves both disjoint sign reversals.

## 3. Simultaneous arithmetic sign tests, not pointwise zeros

On any fixed bounded box of floors, the two phases are continuous jointly in $a,b$. Thus the diagonal signs also hold on two-dimensional relative neighborhoods of compact portions of the three strict regions. On any such compact sign-separated sets the absolute phase has a positive lower bound, uniform for both parity choices. This assertion uses the complete phase off the diagonal, including both mixed terms there.

Apply the common maximal estimate of the four-parity theorem at these fixed boxes. The local multiplier $\Sigma(N)B_{\mathcal J}(N)(\mathcal C_{X,Z}/|\mathcal J|)^2$ is positive with size bounded below by a constant times $X$ on a fixed interior target subwindow. Hence, outside one $O(X\ell^{-1/20})$ even exceptional set, both true opposite-parity sums have their stated signs and magnitude $\gg X$ there for every one of the permitted floor pairs and every true split $Z$. On the whole target window the sign version holds outside $O(X\ell^{-1/60})$ targets by the same overlap-strip estimate, with constants allowed to depend on the fixed compact sets and carrier.

In particular one may test low, middle and high diagonal floor values at the **same** even target, with the same true split or adaptive splits, outside the one common set. The two finite-target parity slices then each exhibit the negative, positive, negative pattern as the floor parameter increases. This does not force an exact zero of either arithmetic step function, or uniform arithmetic statements as the floor box grows. The zeros above are zeros of the deterministic leading phases.
