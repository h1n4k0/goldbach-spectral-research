# A Dickman major-arc law on growing primorial radicals

**Scope.** The actual high-LCM mixed squarefree strip has an explicit pointwise limiting pair of major coefficients when all primes up to a growing threshold, and no others, divide the target. These coefficients need not be the fixed-radical pair $(1,0)$: for some admissible cuts the odd parity itself has a positive natural-scale major term. This is a conditional result on the genuine original polynomial major arcs, using the same historical prime and masked Möbius Dirichlet-GRH inputs as [the pointwise parity formula](r67-spectral-high-mixed-parity-major.md). It does not evaluate the full coefficient or the minor arcs on these sparse targets, prove any prime representation, or imply Hypothesis S.

Keep the exact $M_\pm=\tfrac12(1\pm\mu(m))M_>$, where $M_>$ is the true above-BV mixed strip before the overall minus in its decomposition. The $+$ selector means an even number of distinct prime factors of the squarefree partner $m$, not numerical evenness of $m$. Keep $L=\log N$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ with fixed admissible $B>B_0>0$, $V=[N/3,2N]$, and $Q=N^{1/1000}$. The arcs $\mathfrak M$ have $q\le Q$ and $|\eta|\le2Q/N$. The exact left prime sequence on a half-open $I\subset(N/2,9N/16\,N]$ is $\lambda(n)\omega(n)$ with $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$ and $\omega$ of uniformly bounded supremum and variation. Write $\mathfrak M_N$ for the original major integral and $\Sigma(N)$ for the singular factor of that formula. None of these arithmetic coefficients or cutoffs is replaced by a model on the Fourier legs.

Let $z\to\infty$ along a sequence of even $N$ satisfying

$$
 \operatorname{rad}(N)=K_z:=\prod_{p\le z}p,\qquad
 \frac{\log z}{\log L}\longrightarrow\vartheta,\qquad 0<\vartheta\le1 .
 \tag{1}
$$

Every such $\vartheta$ is possible. For instance take $z$ through primes and $N=K_z^{\lfloor z^{1/\vartheta-1}\rfloor}$; the prime number theorem gives $\log K_z\sim z$.

Let $f$ be the probability density on $[0,\infty)$, extended by zero to the negative half-line, with Fourier transform (convention $\widehat f(\xi)=\int_{\mathbb R}f(v)e^{-i\xi v}\,dv$)

$$
 \widehat f(\xi)=\exp\left(\int_0^1
                  \frac{e^{-i\xi v}-1}{v}\,dv\right).
 \tag{2}
$$

This is the normalized Dickman density, equivalent to the density in [de Bruijn's original transform formula (1.9)](https://pure.tue.nl/ws/files/2416706/597496.pdf#page=4). The existence and the properties used here also follow below. Set
$F(v)=\int_0^v f(w)\,dw$ for $v\ge0$ and
$C_f(t)=\int_{\mathbb R} f(v)f(v+t)\,dv$. Put
$\tau=2B/\vartheta$ and $\upsilon=(B-B_0)/\vartheta$.

**Theorem.** Under the stated historical inputs, uniformly in the true $I,\omega$ above as $N\to\infty$ along (1), for each fixed $A>0$,

$$
 \mathfrak M_N(M_\pm;I,\omega)=
  \Sigma(N)\,\mathcal K_\pm(\tau,\upsilon)
          \int_I\frac{\omega(y)}{\log(N-y)}\,dy
  +o\!\left(\frac{\Sigma(N)|I|}{L}\right)
  +O_{A,B,B_0}\!\left(NL^{-A}\right),
 \tag{3}
$$

where

$$
 \mathcal K_\pm(\tau,\upsilon)=\frac12\left\{
       \tau\int_{\upsilon}^\infty f(v)^2\,dv+F(\upsilon)^2
       \ \pm\
       \left(\int_{-\tau}^{\tau}C_f(t)\,dt-\tau C_f(\tau)\right)
                                           \right\}.
 \tag{4}
$$

Here $|I|$ denotes real interval length; for very short $I$ the explicit additive remainder need not be smaller than the main scale. For example on intervals of length $\gg NL^{-J}$ with a fixed $J$ one may choose $A$ large enough in (3).

## 1. The single surviving normalized primitive

Set $\ell=\log z$. Use the arithmetic $\alpha_p,P_N,R_{N,j},Q_N$ of the [exact pointwise parity formula](r67-spectral-high-mixed-parity-major.md): $\alpha_p=0$ for $p\mid N$, otherwise $(p-1)/(p^2-2)$, and $\alpha(a)=\prod_{p\mid a}\alpha_p$ on squarefree $a$. The function
$R_{N,j}(u)=\sum_{a\le e^u,(a,j)=1}\mu(a)\alpha(a)$ is zero for $u<0$. All products and sums will use the actual mask (1). For the ordinary reciprocal primitive
$R(u)=\sum_{a\le e^u}\mu(a)/a$ (also zero for $u<0$), its [ordinary reciprocal Mertens bound and Fourier estimates](r70-spectral-signed-shift-euler-slots.md#1-fourier-weight-of-the-rough-reciprocal-primitive) give
$|R(u)|\ll e^{-c\sqrt u}$ on $u\ge0$, so $R\in L^1\cap L^2$. Its Laplace transform for $s>0$ is $1/(s\zeta(1+s))$, by integrating the absolutely convergent Dirichlet series; dominated convergence as $s\downarrow0$ gives $\int R=1$.

For a prime $p$, denote by $\delta_w$ the unit atom at log position $w$. Define the positive finite measures

$$
 \begin{split}
 \nu_z&=\mathop{*}_{p\le z}\left(\sum_{k\ge0}p^{-k}\delta_{k\log p}\right),\\
 \kappa_z&=\mathop{*}_{p>z}\left(\delta_0+
       (1/p-\alpha_p)\sum_{k\ge1}p^{-(k-1)}\delta_{k\log p}\right).
 \end{split}
 \tag{5}
$$

The factors at $p>z$ have nonnegative coefficients since $0<\alpha_p<1/p$ there. Their additional mass at each $p$ is $O(p^{-2})$, so the convolution product converges as a finite positive measure. The factor for $p\le z$ deletes $p$ from the ordinary primitive; the one for $p>z$ replaces its local weight by $\alpha_p$. For example its Laplace factor is
$(1-\alpha_p p^{-s})/(1-p^{-1-s})$. Comparing each Dirichlet coefficient, then taking the primitive, gives the exact log convolution $R_{N,1}=R*\nu_z*\kappa_z$. One can check it on each finite prefix, since only factors with $p\le e^u$ can shift its value at $u$. Young's inequality gives the same identity in $L^1\cap L^2$.

Write $M_z=\int_{\mathbb R}R_{N,1}$; since $\int R=1$, this is the positive mass of $\nu_z*\kappa_z$. The mass of $\kappa_z$ is $1+O(z^{-1})$, and ordinary Mertens gives $\|\nu_z\|= \prod_{p\le z}(1-1/p)^{-1}\sim e^\gamma\ell$. Thus $M_z\sim e^\gamma\ell$. The normalization in the original parity formula is

$$
 P_N M_z^2
  =\prod_{p>z}\frac{(1-\alpha_p)^2}{1-2\alpha_p}
  =1+O(z^{-1}).
 \tag{6}
$$

Indeed the original local $P_N$ factor is $(1-1/p)^2(1+2r_p/p)$, with $r_p=0$ on $p\mid N$ and $(p-1)/(p-2)$ otherwise; $\alpha_p=r_p/(p+2r_p)$. The primes $\le z$ cancel exactly against $M_z^2$, and each remaining factor differs from $1$ by $O(p^{-2})$.

For $j>1$ an $\alpha(j)\ne0$ term has all its prime factors $>z$, hence $j>z$. The bound from the [squarefree CRT primitive estimates](r63-spectral-full-squarefree-crt-strip.md), or the positive extra mask of mass $\prod_{p\mid j}(1-\alpha_p)^{-1}$ in (5), gives

$$
 \|R_{N,j}\|_1+\|R_{N,j}\|_2\ll \ell\,j/\varphi(j),\qquad
 \sum_{j>z\ {\rm sf}}\alpha(j)^2(j/\varphi(j))^2\ll z^{-1/2}.
 \tag{7}
$$

The last bound follows by inserting $(j/z)^{1/2}$, since the local increments of the resulting infinite sum are uniformly $O(p^{-3/2})$. For any such $j$, a terminal integrated square costs at most $\|R_{N,j}\|_2^2$, a squared primitive integral or the absolute integral over all shifts of its autocorrelation costs at most $\|R_{N,j}\|_1^2$, and a single value of its autocorrelation costs at most $\|R_{N,j}\|_2^2$. These also bound the differences involving a moving terminal endpoint. In the original formula $T(x)=\log(x/D^2)=O(\ell)$ uniformly on $V$, and $P_N\asymp\ell^{-2}$ by (6). The total normalized $j>1$ error is therefore $O(\ell z^{-1/2})=o(1)$, uniformly including all cutoff endpoints.

## 2. Global convergence to the Dickman density

Define the genuine signed density $f_z(v)=(\ell/M_z)R_{N,1}(\ell v)$. Its fixed-frequency Fourier transform is
$\widehat R(\xi/\ell)$ times the normalized multiplier of $\nu_z$ at $\xi/\ell$, times that of $\kappa_z$. The first tends to $1$ by integrability and $\int R=1$; the last tends to $1$ uniformly in real frequency by (5), since all the extra mass together is $O(z^{-1})$. For $\nu_z$ the exact logarithm of the normalized multiplier is

$$
 \sum_{p\le z}\sum_{k\ge1}
       \frac{e^{-ik\xi\log p/\ell}-1}{kp^k}.
 \tag{8}
$$

The $k\ge2$ part tends to zero at each fixed $\xi$ by absolute dominating sums and termwise convergence. For $k=1$, first restrict to $z^\varepsilon<p\le z$. The reciprocal prime measures $\sum_p p^{-1}\delta_{\log p/\ell}$ tend there to $dv/v$: on any fixed subinterval $(a,b]$ with $\varepsilon\le a<b\le1$, Mertens gives $\sum_{z^a<p\le z^b}1/p\to\log(b/a)$. Continuous testing on the compact interval follows by a partition, and a possible exact lower-bound prime has mass at most $z^{-\varepsilon}$. The omitted $p\le z^\varepsilon$ contribute at most $|\xi|\ell^{-1}\sum_{p\le z^\varepsilon}(\log p)/p\ll|\xi|\varepsilon+O(|\xi|/\ell)$ by ordinary partial summation. Taking $\varepsilon\downarrow0$ proves pointwise convergence to (2).

Pointwise convergence can be upgraded globally. Write $R_z=R*\nu_z$ for the reciprocal primitive with all primes $\le z$ excluded. The proof of the [rough Fourier bounds (5)](r70-spectral-signed-shift-euler-slots.md#1-fourier-weight-of-the-rough-reciprocal-primitive) applies with roughness parameter $G=z$: that proof uses $U=\log G$ in its prime integral, independently of later choices tying $G$ to the target $N$. It gives $|\widehat R_z(t)|\ll\ell/(1+\ell|t|)$ on $|t|\le1$ and $|\widehat R_z(t)|\ll (1+\log(3+|t|))^4/|t|$ on $|t|\ge1$. Combine with $\|\kappa_z\|=O(1)$ and $M_z\asymp\ell$ to obtain

$$
             |\widehat f_z(\xi)|
            \ll\frac{(1+\log(3+|\xi|))^4}{1+|\xi|}.
 \tag{9}
$$

The right side has integrable square. Dominated convergence and Plancherel show $f_z\to f$ in global $L^2$ for the inverse transform of (2).

The tails are also tight in absolute $L^1$. Let $\pi_z$ be the pushforward of $(\nu_z*\kappa_z)/M_z$ under division of the log coordinate by $\ell$; it is a positive probability measure supported on $[0,\infty)$. Uniformly for $z$ large, $\int e^v\pi_z(dv)\ll1$. For the $\nu_z$ component the log of this exponential moment is
$\sum_{p\le z,k\ge1}(p^{k/\ell}-1)/(kp^k)$. Its $k=1$ sum is $O(\ell^{-1}\sum_{p\le z}(\log p)/p)=O(1)$ since $p^{1/\ell}\le e$. For $k\ge2$ the sum is bounded by a uniform convergent Euler tail once $\ell\ge4$, using $p^{-k(1-1/\ell)}\le p^{-3k/4}$. For $\kappa_z$ the unnormalized exponential moment is bounded by the product of $1+O(p^{-2+1/\ell})$ for $p>z$, from (5). Its normalization is at least one, so the claimed bound follows.

The convolution representation is $f_z(v)\,dv=\pi_z*(\ell R(\ell v)\,dv)$. Since both arguments of this convolution are supported on the nonnegative half-line, splitting at $v/2$ in the two underlying variables yields, for any $b>0$,

$$
 \int_{v>b}|f_z(v)|\,dv
   \ll \|R\|_1 e^{-b/2}+\int_{w>b\ell/2}|R(w)|\,dw .
 \tag{10}
$$

The compact $L^1$ convergence from $L^2$, and these uniform tails, give global $L^1$ convergence: the limit tail is bounded by Fatou along a subsequence of almost-everywhere convergence. In particular $\int f=1$ and $f$ is supported on $[0,\infty)$. For any nonnegative compactly supported Lipschitz test $g$, the difference between testing $f_z$ and $\pi_z$ is at most $(\operatorname{Lip}g/\ell)\int w\,|R(w)|\,dw$, because $\int R=1$. Therefore $\int gf\ge0$, and $f\ge0$ almost everywhere. Finally repeating (8) with $e^{-sk\log p/\ell}$ for real $s\ge0$, using the same domination and the exact Laplace factor in (5), gives
$\int_0^\infty e^{-sv}f(v)\,dv=\exp\int_0^1(e^{-sv}-1)\,dv/v$.
No generalized prime-distribution hypothesis is used in this profile convergence.

## 3. Transfer on the original arcs and a nonzero odd example

The original formula (3) of the [pointwise parity calculation](r67-spectral-high-mixed-parity-major.md) has real bracket

$$
 P_N\left\{T(x)(Q_N-Q_{N,U})+J_{N,U}
  \ \pm\left(\int_{-T(x)}^{T(x)}C_N(t)\,dt-T(x)C_N(T(x))\right)\right\},
 \qquad U=\log(H_0/D),\quad x=N-y.
 \tag{11}
$$

It multiplies $\Sigma(N)\omega(y)/(2\log x)$ in the major evaluation. The original quantities have the following exact $j=1$ terms: $Q_N-Q_{N,U}$ contributes $\int_U^\infty R_{N,1}(u)^2du$; $J_{N,U}$ contributes $(\int_0^U R_{N,1}(u)\,du)^2$; and $C_N(t)$ contributes $\int R_{N,1}(u)R_{N,1}(u+t)du$. These are the hard terminal moments of that formula. The negligible error for passing to $j=1$ was verified in (7).

Now $T(x)/\ell\to\tau$ uniformly for $x\in V$, since $T(x)=2B\log L+\log(x/N)$, and $U/\ell\to\upsilon$ by (1). Rescaling the $j=1$ terms in (11) gives exactly $P_NM_z^2$ times the expression inside braces in (4) with $f,C_f,\tau,\upsilon$ replaced by $f_z,C_{f_z},T(x)/\ell,U/\ell$. For the squared tail, $\|f_z^2-f^2\|_1\to0$ by global $L^2$ convergence; the varying endpoint is valid by absolute continuity of the $f^2$ integral. The cumulative integrals follow by $L^1$ convergence. Uniformly over all real $t$,

$$
 |C_{f_z}(t)-C_f(t)|
       \le(\|f_z\|_2+\|f\|_2)\|f_z-f\|_2\longrightarrow0 .
 \tag{12}
$$

Continuity of $C_f$ from $L^2$ translation continuity handles the moving endpoint and integral. Thus the normalized coefficient converges uniformly on the actual physical domain and (6) gives (4). Integration against the exact bounded left weight, retaining the parent formula's additive error, proves (3).

For a concrete difference from fixed radical, let $0<\upsilon\le1/16$ and $\tau\ge32$. We claim $\mathcal K_-(\tau,\upsilon)\ge1/2$. To see this without any numerical evaluation, let $\mathcal L_f(s)$ denote the Laplace transform just established. Differentiating for $s>0$ and then using monotone convergence at $0$ shows the mean is $1$, since
$-\mathcal L_f'(s)=\mathcal L_f(s)(1-e^{-s})/s$. The same identity and Laplace uniqueness give for almost every $v>0$ the elementary relation
$v f(v)=\int_{\max(0,v-1)}^v f(t)\,dt$. On $(0,1)$ this says $F'=F/v$ and hence $f$ is constant there, at most $1$ because its total mass is $1$. Markov's inequality and Cauchy–Schwarz give $\int_0^2 f\ge1/2$ and $\int_0^2 f^2\ge1/8$. It follows that $\int_\upsilon^\infty f^2\ge1/16$. Also $C_f\ge0$ and $\int_{\mathbb R} C_f=1$ by Fubini, so the twisted bracket in (4) is at most $1$. Therefore the minus coefficient is at least $(\tau/16-1)/2\ge1/2$. In particular one may take $N=K_z$ itself and $B\ge16$ sufficiently large with $B_0=B-1/32$; then $\vartheta=1$ and these inequalities apply. There is no extrapolation from dense families to these sparse radials: this is the actual original major of the odd squarefree parity on the stated growing-radical sequence, conditional on the explicit inputs, with no inference about the complementary minor contribution.
