# Quantitative weak S targets and the smaller central sufficiency test

**Scope.** These are sufficient estimates to seek, not proofs of any new operator bound, of Hypothesis S, or of Goldbach. The arithmetic central sufficiency test below needs no GRH; its interpretation as a block of the original Hardy operator uses local Dirichlet GRH(N).

## 1. S relative to the original normalization

Write $S=\mathfrak S(N)$ and $L=\log N$. For the [original Li–Liu operator](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf), Theorem 6.1 and (1.7) make the zero-free S condition at modulus $N$ exactly
$$
 \|T_N\|\le\frac{S}{2h(N)\sqrt{1-\eta_N}},
 \qquad \eta_N=\frac{h(N)^2L^3}{NS}.
$$
Original S requires $h(N)\to\infty$ and eventually $\eta_N\le1/4$. The asymptotic norm target is thus $o(S)$. Fixed choices such as $h(N)=(\log\log N)^a$ or $h(N)=L^a$ with $a>0$ are admissible and not ruled out by the [Yilin Liu polylogarithmic lower bound under GRH](https://hexagonmath.org/pdf/2611.00788v1); they are not established. That preprint's lower bound, if applied for every fixed exponent, does rule out the aggressive admissible choice $h(N)=\sqrt N/L^a$ for any fixed $a>3/2$, under global Dirichlet GRH. It does not rule out $o(S)$. For mere existence or a positive fraction of the predicted representation count, one can ask for a weaker constant bound as follows.

## 2. Sharp threshold for the full-norm argument, with a safe simple constant

For a fixed nonzero, nonnegative smooth $\phi$, supported in $[1/3,2/3]$ and symmetric about $1/2$, write $c_\phi=\int\phi^2$ and $G_\phi(N)$ for the original weighted Goldbach sum:
$$
 G_\phi(N)=\frac1N\sum_{\substack{n+m=N\\(nm,N)=1}}
 \Lambda(n)\Lambda(m)\phi(n/N)\phi(m/N).
$$
The original Theorem 7.1 and Proposition 7.4 give
$$
 |G_\phi(N)-c_\phi S|\le Q_N(\phi)\|T_N\|,
 \qquad Q_N(\phi)\longrightarrow Q_\infty(\phi)
 =\frac{e^2}{2\pi}\int_{1/3}^{2/3}(\phi/2-u\phi')^2\,du .
$$
Here the companion test is $\Phi(u)=\sqrt u\,\phi(u)$, so that $\Phi-u\Phi'=\sqrt u(\phi/2-u\phi')$ in the exact formula with $du/u$. The limit follows by the uniform convergence of $(Nu)^{2/L}$ to $e^2$ and of $1+(Nu)^{-2(1/8-1/L)}$ to one on this fixed support. Integration by parts, and then symmetry for the kinetic term, give
$$
 \int (\phi/2-u\phi')^2
 =\int\left(\left[\tfrac14+(u-\tfrac12)^2\right](\phi')^2+\tfrac34\phi^2\right)du.
$$
The sharp strict coefficient for this **full norm and test argument** is therefore
$$
 \tau_* =\sup_\phi\frac{c_\phi}{Q_\infty(\phi)}
          =\frac{2\pi e^{-2}}{\lambda_1},
$$
where $\lambda_1$ is the ground Dirichlet eigenvalue of the last displayed quadratic form, divided by $\int\phi^2$. A one-dimensional ground state can be chosen positive inside the interval and is simple; reflection is a symmetry, so it is even about $1/2$. Multiplying this smooth ground state by symmetric nonnegative cutoffs approaching the endpoints yields smooth compactly supported tests converging in $H_0^1$ (the ground state vanishes linearly at the endpoints). One can rescale to $\phi\le1$ without changing the quotient. Thus the smoothness, symmetry and nonnegativity restrictions do not change the variational optimum.

An exact simple enclosure follows by the Liouville change of variables. Put $x=u-1/2$, $a(x)=1/4+x^2$, $x=\tfrac12\sinh t$, and $f(t)=a(x)^{1/4}\phi(u)$. The denominator is unitary in this change of variable. The kinetic part becomes $\int(f'-\tfrac12\tanh t\, f)^2dt$, and integrating the cross term by parts gives a Dirichlet Schrödinger operator with potential $1+\tfrac14\operatorname{sech}^2t$ on $[-T,T]$, $T=\operatorname{arsinh}(1/3)$. Hence
$$
 \frac{\pi^2}{4T^2}+\frac{49}{40}
 \le\lambda_1\le
 \frac{\pi^2}{4T^2}+\frac54.
$$
No decimal eigenvalue calculation is needed for a useful explicit margin. The elementary inequalities $T\ge53/162$ (integrate $(1+x^2)^{-1/2}\ge1-x^2/2$), $\pi^2<10$, $2\pi>157/25$, and $e^2<37/5$ give
$$
 \lambda_1 < \frac{276485}{11236}<\frac{4553}{185},
 \qquad \tau_* > \frac{157/185}{4553/185}=\frac1{29}.
$$
Thus one can fix a smooth $\phi$ with $c_\phi/Q_\infty(\phi)>1/29$. A zero-free width of the same form as S but with **constant $h=15$** would give
$$
 G_\phi(N)\ge(1/30-o(1))c_\phi S,
$$
since then $\eta_N\to0$. More generally $\limsup\|T_N\|/S<\tau_*$ suffices for a fixed positive fraction of $c_\phi S$ for a suitable test. This only establishes sufficiency of that margin; it does not give the asymptotic $G_\phi\sim c_\phi S$ and is not original S. Proper prime-power terms total $O(L^2/\sqrt N)$ after normalization (there are $O(\sqrt N)$ possible powers on either side), so the positive margin yields $\gg_\phi SN/L^2$ ordered prime-pair representations in the standard central window. The threshold is not asserted necessary for Goldbach, only optimal in the indicated norm argument.

## 3. A smaller target: one strict central half and a one-sided real probe

Set $a=1/2$, $b=9/16$, $I=[a,b]$, $w(u)=\sqrt{u(1-u)}$, and $M(x)=\int_a^x w(u)\,du$. With the exact strict lower endpoint of [the central block](r18-spectral.md), put
$$
 A_N(x)=\frac1N\sum_{\substack{N/2<n\le xN\\(n,N)=1}}
     \Lambda(n)\Lambda(N-n)w(n/N),\qquad F_N(x)=A_N(x)-SM(x).
$$
The unit restriction removes the midpoint atom. A central positivity threshold that does not ask to control the exterior is
$$
 \langle F_N,M\rangle_{L^2(I)}\ge-(1-\epsilon)S\|M\|_2^2
 \tag{1}
$$
for a guard $\epsilon>0$ independent of $N$. The more familiar condition $\|F_N\|_2\le(1-\epsilon)S\|M\|_2$ implies (1), but no bound on the modes orthogonal to $M$ is needed for (1). Since $0\le A_N(x)\le A_N(b)$ and $M\ge0$,
$$
 A_N(b)\ge\frac{\langle A_N,M\rangle}{\int_I M}
     \ge\epsilon S\frac{\|M\|_2^2}{\int_I M}.
$$
After removal of proper powers this gives $\gg_\epsilon SN/L^2$ prime-pair representations with one summand in $(N/2,9N/16]$ and the other in $[7N/16,N/2)$. This condition is arithmetic and independent of GRH. For comparison with the weighted Möbius transfer, it is a single nonnegative bounded-variation test on the strict upper half: $W(u)=\mathbf1_{(a,b]}(u)\,w(u)\int_u^b M(x)\,dx$. Fubini gives $G_W=\langle A_N,M\rangle$ and $\int W=\|M\|_2^2$, where $G_W$ denotes the one-variable weighted sum. Thus a pointwise bound $P_W\le(1-\epsilon)\int W$ and an $o(S)$ error in the weighted parity transfer suffice for this positivity. This is weaker than establishing all signed primitives, and neither of these two inputs follows just from the currently removed divisor sectors.

Under local GRH, there is also an operator version: reflect $F_N$ oddly to $[7/16,9/16]$. On the physical compression to this full symmetric interval there is no nonzero difference alias, and only the sum alias $1$ can occur. It is active exactly when $x+y\ge1$, where its cumulative interval is $[1-y,x]$. Hence the exact kernel is almost everywhere
$$
 -2\pi\,r_N(x)r_N(y)\mathbf1_{x+y\ge1}\{F_N(x)+F_N(y)\},
$$
with the same factor $r_N$ and measure convention as the upper-half block. Atom endpoints affect at most null lines of this kernel. Boundedness of $r_N$ on the fixed interval gives Hilbert–Schmidt norm $O(\|F_N\|_2)$, and the upper-half rank-two compression gives the reverse lower bound in operator norm. Therefore the mixed central half introduces no new full-norm smallness requirement, while the one-sided test (1) is an even smaller arithmetic target for prime-pair existence/count.
