# A cutoff-free hard rational profile for the actual centered critical-shell energy

Let $N$ be even, $X=\sqrt N$, $L=\log N$, $L_2=1+\log L$, $R=\operatorname{rad}N$, and $e(z)=e^{2\pi iz}$. Keep exactly the complementary coefficient and centered critical-prime energy of [the centered rational profile](weak-s-type-ii-critical-prime-centered-rational-profile-grh.md):

$$
 D_m=\mathbf1_{N-y\le m<N/2}
       \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                       (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_m D_m e(\alpha m).
$$

Here $N/2\le y\le9N/16$, $I_k$ is a hard interval including the strict condition $k>t\ge N^{.49999}$, and $I_d$ is any hard interval in $[X,\infty)$, clipped at $d<N/(2t)$. One may also clip $I_k$ at $k<X/2$. Both clippings are automatic for the actual product and for the real integrals below. Use the original shell $\mathcal Q=[.8X,.9X]\cap\mathbb P$, $1\le a<q$, $|\beta|\le1/(10N)$. The squared shell norm $\mathcal E_N^0(D)$ subtracts the average over $a=1,\dots,q-1$ separately at each $(q,\beta)$ before taking squares and integrating.

Put $\Omega_0(x)=\mathbf1_{[1-y/N,\,1/2)}(x)$ and $w_0(k)=\mathbf1_{I_k}(k)$. For $\rho\in\mathbb Q\setminus\{0\}$ define the hard real rational vector

$$
 \begin{split}
 \mathcal H_{q,\beta}(\rho)
  ={}& \sum_{\substack{l\ge1,\ l\ {\rm squarefree},\ (l,N)=1,\ s\mid l\\
                          h\mid R,\ su\in I_d,\ (u,lN)=1\\
                          \rho l^2hu\in\mathbb Z\setminus\{0\}}}
         \frac{N\mu(l)\mu(s)\mu(h)\mu(u)}{q l^2 h u}\\
     &{}\quad \times \int_{\mathbb R}\Omega_0(x)e(\beta Nx)
                      w_0(Nx/(su))e(-\rho Nx/q)\,dx.
 \end{split}                                                        \tag{1}
$$

There is no analytical square cutoff, unit inclusion cutoff, frequency cutoff or endpoint smoothing in (1). Discrete long endpoints $su\in I_d$ retain their original strictness. Real integrals are unchanged by altering the two real weights at isolated endpoints. Define

$$
 \mathscr H_N=
      \int_{-1/(10N)}^{1/(10N)}
           \sum_{q\in\mathcal Q}q(q-1)
                  \sum_{\rho\in\mathbb Q\setminus\{0\}}
                            |\mathcal H_{q,\beta}(\rho)|^2\,d\beta .
                                                                    \tag{2}
$$

**Theorem.** The series in (1) converges absolutely at each coordinate and in the indicated rational Hilbert space as the square cutoff tends to infinity; the resulting squared norm satisfies $\mathscr H_N\ll N/L$ unconditionally. Under global Dirichlet GRH (including the Riemann zeta function), for every fixed $A>0$,

$$
                        \mathcal E_N^0(D)
                      =\mathscr H_N+O_A(NL^{-A})                    \tag{3}
$$

uniformly in all even targets and all the permitted hard cuts above. The separately known [actual additive constant profile](weak-s-type-ii-critical-prime-polynomial-width-true-constant-profile.md) is unchanged. This is a centered **energy** formula; it neither estimates a signed pairing nor extends to other shells or proves Weak S.

## 1. Arbitrary fixed logarithmic accuracy in the genuine finite transport

Fix an intermediate accuracy $B>0$. We first compare the actual hard norm to the rational norm with genuine inward smoothing and finitely many square labels. Write $\Omega_\delta,w_\delta$ for the original inward physical and logarithmic cofactor cutoffs, with $\delta=L^{-K}$ for a sufficiently large fixed $K$. They take values in $[0,1]$, have bounded variation, and differ from the respective hard weights only within $O(\delta)$ of the two endpoints in their own coordinates. One construction is to shrink each interval by $\delta$ at both ends and convolve with a nonnegative unit-integral smooth mollifier supported in $(-\delta/2,\delta/2)$; if there is nothing left, take zero. In this case the entire hard interval lies in its endpoint strips. The derivative bounds are those of an interval convolved with a mollifier. Use the original auxiliary square cutoff $T=L^J$ for a sufficiently large fixed $J$, and $H_0=\exp(C_0L_2^2)$ for a sufficiently large fixed $C_0$, chosen after $K,J$. These parameters are used only in the proof.

The true physical transfer in [the smaller-width estimate, §1](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#1-actual-transfers-at-the-smaller-smoothing-width) is $O(N\delta+N^{.99}+NL^3e^{-c\Phi})$ in ordinary squared norm, where $\Phi=L^{3/5}(\log L)^{-1/5}$. It uses only the width in the continuous contribution and uniform polynomial-scale signed hard intervals for the floor correction, so it remains $O_K(N\delta)$. For each cofactor endpoint the physical support still meets only $O(1)$ divisor dyads. On dyad $i$ of scales $A_i=\lambda_i X$, $K_i=X/\lambda_i$, with $1\le\lambda_i\le N^{.00001}$, [the cofactor edge bounds, §1](weak-s-type-ii-critical-prime-polynomial-single-dyad-grh.md#1-literal-endpoint-and-arithmetic-transfers-on-the-polynomial-dyad) give the signed continuous cost

$$
 O_b\big(N(\delta+K_i^{-1}+\delta^2L_2^3+L^{-b})\big)
$$

and the actual/floor costs

$$
 O\!\left(N\delta^2(1+\log(2G))+\delta A_iG+\lambda_i^2G^2+K_i^2/G\right).
$$

Take fixed $b>K$ and $G=\lfloor L^{K+2}\rfloor$. All these costs are $O_K(N\delta)$, using the polynomial bounds for $K_i,A_i,\lambda_i$. The same bounded-BV prefix argument handles the actual cutoff differences; the physical and cofactor changes can be telescoped. There is no dyad count loss for either endpoint change.

After this transfer use exactly the approximant in [the joint completion, §2](weak-s-type-ii-critical-prime-cross-dyad-subpolynomial-grh.md#2-exact-auxiliary-truncations-and-joint-fourier-completion), with the new fixed $K,J,C_0$. The signed long unit remains true. Insert the square cutoff $l\le T$ with $(l,N)=1$ while the true full unit is still present; then truncate the short inclusion to $h\mid R,\ h\le H_0$. The exact split has $s=(l,d)\mid l$, $d=su$, $(u,lN)=1$, and $k$ a multiple of $l^2h/s$. Per dyad the squared ordinary errors for the two arithmetic truncations are

$$
 O(NLT^{-3/4}),\qquad
 O(NT^2L e^{-C_0 L_2}L_2^{O(1)}).
$$

These are the displayed bounds before substituting the former fixed value of $T$. They hold also before the common physical weight on the same compact normalized support, by the same bounded-BV proof. The factor from summing $O(L)$ dyads by norm triangle is at most $O(L^2)$ in the squared error. Thus the total ordinary squared error of the resulting $D^\dagger$ compared with $D$ is $O_B(NL^{-B})$ by the successive choices of $K,J,C_0$. The approximate pre-physical ordinary norm per dyad stays $O(\sqrt N)$.

Here are the finite versus analytical frequency cutoffs for this retuning. Write $G_\beta(v)=\Omega_\delta(e^v)e(\beta Ne^v)$; its transform satisfies

$$
 \big|\widehat G_\beta(\tau)\big|
     \ll\min(1,|\tau|^{-1},\delta^{-1}|\tau|^{-2}),\qquad
 \big|\widehat G_\beta(\tau)\big|\ll_r
                     \delta^{1-r}|\tau|^{-r}\quad(r\ge2).
$$

In particular its $L^1$ norm is $O_K(L_2)$. Choose a fixed $P>K+2$ and retain $|\tau|\le L^P$ in the actual finite completion. The omitted tail in genuine sampled norm at fixed $\beta$ is $O_C(NL^{-C})$ for any fixed $C$: before centering use the separated-center bound $O(LN)$ in sampled norm from [the integrated determinant construction, §2](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#2-integrate-in-the-complete-square-and-dispatch-its-off-diagonal), then integrate the high derivative bound. Centering is a contraction. The true short transform on each dyad is the transform of $f_{i,\tau}(z)=w_i(z)e(\tau\log z)$ with the original compact normalized bump. It has envelope $\ll\min(1,(Y_\tau/|\xi|)^2)$, where $Y_\tau=1+\delta^{-1/2}+|\tau|$, since its second derivative has $L^1$ norm $O(\delta^{-1}+(1+|\tau|)^2)$. Its higher derivative bounds cost only fixed log powers on retained $\tau$ for each fixed order. With $U_i=A_i/s$ and short mesh $\xi_i=K_i s/(q l^2 h)$, keep exactly $0<|j|\le J_i=\lambda_i N^{.001}$ in the modular array. The inequality $J_i\xi_i\gg N^{.001}/(T^2H_0)=N^{.001-o(1)}$ makes the actual omitted $\xi_i\widehat f_{i,\tau}(j\xi_i)$ tail power-small after taking a sufficiently high fixed derivative order, since its absolute sum is $O_r(\|f_{i,\tau}^{(r)}\|_1(J_i\xi_i)^{1-r})$. A fixed order can beat the polynomial label and norm factors. All retained $l,h,j$ are units modulo $q$.

Use the same coherent array on $v=l^2hu/j\bmod q$ of [the coherent completion, §1](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#1-complete-the-square-only-after-adding-the-square-labels). Its nonzero-determinant equation is unchanged:
$l_1^2h_1 j' u-l_2^2h_2j u'=bq,\ b\ne0$. For fixed labels including $b$, the long signed GRH additive bound $O(U_i^{4/5})$ and the elementary $L^2$ bounds $O(U_{i'}^{1/2})$, $O(X^2\sqrt{\#\mathcal Q})$ give at most $N^{1.9+.000013}$ before the label sums. The nonzero integral dilations cause no $L^2$ losses. The $j,j',b$ count is $\ll\lambda_{\max}^4 N^{.003+o(1)}$ for $\lambda_{\max}\le N^{.00001}$: in particular $|b|\ll T^2H_0\lambda_{\max}^2N^{.001}$, and each of the two $j$ ranges is unchanged. All $l,s$ counts and retained time scales cost fixed log powers at most, and the $h$ count is subpower. The product of the two time $L^1$ weights is $O_K(L_2^2)$. Thus the whole nonzero-determinant term is $O(N^{1.91})$, with room for any fixed log precision at scale $N^2$. The only conditional input here is the same global-GRH signed long bound, uniform after genuine unit convolution and Abel; it is unaffected by the fixed log enlargement of the time range.

For the exact centered norm also subtract the two artificial completions of [the centered calculation, §1](weak-s-type-ii-critical-prime-centered-rational-profile-grh.md#1-subtract-the-two-artificially-completed-squares). At fixed $(q,\beta)$ they are $q(q-1)|\mathcal S_q(0)|^2$ and $q|\sum_{v\ne0}\mathcal S_q(v)|^2$. Indeed the first completed squared norm is weighted by $q(q-1)$, and exact multiplicative Parseval restricts to unit residues and subtracts the constant character. These are not the actual additive constant. The short absolute sum remains $\ll Y_\tau$ by the envelope above. For the first completion there are $O(1+U_i/q)\ll N^{.00001}+1$ possible long labels per tuple because $v=0$ is exactly $q\mid u$. For the second completion first sum over all residues, so the two signed factors separate; the long sum is $O(U_i^{4/5})$ under the inherited bound at zero frequency, and then subtract the just bounded zero residue. Thus the two total subtractions are $O(N^{1.50002+o(1)})$ and $O(N^{1.800016+o(1)})$, including shell primes dividing $N$. The exact characterized nonprincipal norm is nonnegative separately at each $q$. Its transfer to actual nonzero numerators uses the same factor $q/(q-1)=1+O(X^{-1})$, without treating the subtracted squares as nonnegative summands of the actual group mean.

On exact determinant zero restore all time and dual labels only in the rational norm, not in the modular formula. At fixed $(l,s)$ the coherent coordinate $\rho=j/(l^2 h u)$ is a fixed rescaling of the coordinate in [the analytical restoration, §3](weak-s-type-ii-critical-prime-full-polynomial-physical-diagonal-grh.md#3-restore-the-exact-physical-integral-on-the-rational-diagonal-only). Its time tail proof bounds the squared instantaneous norm by

$$
 O\left(\frac{N^2Y_\tau L_2^3}{L l^2}
                          (L+\log(2+|\tau|))\right)
$$

per dyad and uses the above arbitrary fixed derivative bound for $G_\beta$. The lower bound on the mesh leaves the same omitted-sample threshold $N^{1/2000}$ in its squared dual tail estimate; the $Y_\tau^4$ cost on retained $\tau$ is only a fixed log power. Hence both norm restorations have any required fixed log accuracy also with $K,J,P$ chosen as above. Fourier inversion then gives the integral in (1) with $\Omega_\delta,w_\delta$ at $l\le T,h\le H_0$, on the unchanged $su\in I_d$. The normalized dyad bump is one on its actual physical interval. The genuine unit restrictions survive. Finally restore all $h\mid R$ in this rational vector: at each $(l,s)$ the squared tail is bounded, as in [the signed rational sampling bound, §3](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#3-keep-the-stronger-sparse-sampling-bound-and-integrate-the-actual-derivative), by

$$
 \frac{O(N^2)}{L l^2 V(lN)}
       \sum_{\substack{h_1,h_2\mid R\\ h_1,h_2>H_0}}
                    \frac1{[h_1,h_2]},\qquad V(M)=\varphi(M)/M.
$$

Its reciprocal Rankin factor is $\ll e^{-C_0 L_2}L_2^{O(1)}$. The hypotheses of that estimate are unchanged: $s\le L^J$, hence the long variable is at polynomial scale, the physical variation is bounded, and the actual logarithmic cofactor derivative has bounded integral separately at each edge. This last restoration can cost an arbitrary fixed log saving by increasing $C_0$ after $J$, even with triangle over $l,s$. No new $h$ is used in a modular inverse.

For clarity, write $\mathcal R_T[\Omega,w]$ for the vector (1) with $l\le T$ and the displayed weights replaced by $\Omega,w$, always with **all** rational $h\mid R$. Equip its fixed-$\beta$ coordinates with the squared norm $\|U\|_\beta^2=\sum_{q\in\mathcal Q}q(q-1)\sum_{\rho\ne0}|U_{q,\beta}(\rho)|^2$. The sharp paired-label rational upper bound is uniform for all these fixed-log choices of $\delta,T$:

$$
                    \|\mathcal R_T[\Omega_\delta,w_\delta]\|_\beta^2
                              \ll_{K,J} N^2/L .                     \tag{4}
$$

To check the parameter dependence, use [the paired denominator proof, §2](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#2-factor-the-common-rational-denominator-before-the-square-label-sum). After splitting $c=c_0m,\ c_i=m_i m$ there, $s_i m_i\le T^2$, so the actual interval $I_d/(s_i m_i)$ is in $[N^{.48},N^{.51}]$ for large $N$, and $l_i N m_i$ is a polynomial mask. Its signed reciprocal $1/m$ norm bound is uniform for the bounded-BV cofactor weight at each real $x$. For the physical derivative part apply it under $\|(\Omega_\delta e(\beta N\,\cdot))'\|_1\ll1$; for the other derivative, each true cofactor edge confines $v$ to a constant-ratio interval at $N/(s_i m_i m k_{\mathrm e})$ and integrates the actual log derivative to $O(1)$ per $m$. Thus the exact dense and sparse squared bounds of that proof give cost $O(1/(C_*V(l_i N m_i)))$ for the individual sampling, $C_*=N/(q c_0)$. No $\delta^{-1}$ cost enters. After the exact $h$ grouping, the $V(N)$ Euler factor cancels the two square-root mask costs and the convergent remaining paired-label Euler product gives (4). This argument, and all other purely rational estimates here, are unconditional.

Now the positive completed norm, with its nonzero-determinant error and the two artificial subtractions, differs from (4)'s squared rational norm by $O_C(N^2L^{-C})$ at any fixed accuracy $C$. In using norm restorations to compare the squares, (4), or the preliminary polynomial-in-$L$ rational bound, absorbs the cross term by choosing the norm errors sufficiently small. The group normalization $q/(q-1)$ also changes that norm by a negligible amount by positivity and (4). Integrating over $\beta$ therefore proves the same comparison at scale $N$ for $D^\dagger$. The original arcs are disjoint, and centering is orthogonal projection, so the actual ordinary squared error $O_B(NL^{-B})$ bounds the hard-to-$D^\dagger$ shell squared error. By (4) the difference of the two actual squared norms is $O(NL^{-B}+NL^{-(B+1)/2})$. We may choose $B$ and all subsequent interval/arithmetic accuracies sufficiently large for any fixed target power. This proves finite-label smooth transport to arbitrary fixed log accuracy, still under global Dirichlet GRH.

## 2. An all-square-label estimate independent of smoothing

In this section no GRH is used. Start with any finite set of square labels and keep all $h\mid R$. We will also allow either of the two difference vectors
$\mathcal R_T[\Omega_\delta-\Omega_0,w_\delta]$ and $\mathcal R_T[\Omega_0,w_\delta-w_0]$. The estimates hold for any finite label set, not just $l\le T$.

For a pair of labels $l_i,s_i,h_i$, $i=1,2$, write $b_i=l_i^2 h_i$. For a common reduced rational $\rho=a/c\ne0$ the membership condition is precisely $c\mid b_i u_i$. Set $c_i=c/(c,b_i)$, so $u_i=c_i v$. Factor $c=c_0m$ with $c_0$ supported on primes of $l_1l_2N$ and $(m,l_1l_2N)=1$. Since $u_i$ is squarefree on nonzero sign and a true $l_iN$ unit, the possibilities are exactly these:

- At primes of $N$, $c_N\mid g=(h_1,h_2)$, and its primes appear in neither $c_i$.
- At a prime common to $l_1,l_2$, the exponent in $c_0$ is $0,1,2$ and the prime is absent in both $c_i$.
- At a prime exclusive to one $l_i$, the exponent in $c_0$ is $0$ or $1$, appearing in the opposite $c_i$ alone in the latter case.
- Outside these primes the exponent is $0$ or $1$, common to both $c_i$.

Write $c_i=m_i m$, with $m_i$ determined by the exclusive primes of the other square label. For fixed $c_0$, put $C_*=N/(q c_0)$, and on each arm write

$$
 F_{i,m}(x)=\Omega(x)e(\beta Nx)
     \sum_{\substack{s_i m_i m v\in I_d\\(m_i m v,l_iN)=1}}
         \frac{\mu(m_i m v)}{v}\,w(Nx/(s_i m_i m v)).
                                                                    \tag{5}
$$

The remaining weighted frequency pairing at this $c_0$ is

$$
 \sum_{\substack{m\ge1\\(m,l_1l_2N)=1}}m^{-2}
      \sum_{\substack{a\ne0\\(a,c_0m)=1}}
       \widehat F_{1,m}(a C_*/m)
                     \overline{\widehat F_{2,m}(a C_*/m)}.
                                                                    \tag{6}
$$

The outer prefactor before the $h$ signs is
$q(q-1)N^2/(q^2 l_1^2l_2^2 h_1h_2 m_1m_2)$. In particular, (5)–(6) and their domains depend on $h_1,h_2$ only through $c_N\mid g$. The possibility $q\mid c_0$ does not affect any of this; these are rational coordinates not modular inverses.

We use a simple compact BV sampling bound. If $F$ is supported in $[7/16,1/2]$, then for $0<\Lambda\le1$, periodization without overlap followed by Parseval gives

$$
             \sum_{a\in\mathbb Z}|\widehat F(a\Lambda)|^2
                                 =\Lambda^{-1}\|F\|_2^2 .
$$

For $\Lambda>1$, compact-support BV integration by parts gives
$|\widehat F(a\Lambda)|\ll\min(\|F\|_1,\operatorname{Var}(F)/(|a|\Lambda))$ when $a\ne0$. Summing the squares, splitting at $\operatorname{Var}(F)/(\Lambda\|F\|_1)$ if this is at least one and using just the squared-frequency sum otherwise, gives

$$
         \sum_{a\ne0}|\widehat F(a\Lambda)|^2
                  \ll \frac{\|F\|_1\operatorname{Var}(F)}{\Lambda}.
                                                                    \tag{7}
$$

This includes discontinuous hard weights, using the distributional derivative with finite mass and ignoring isolated changes of representative in the real integral. The zero numerator is not inserted in (7).

For all the allowed weights, (5) has sup norm and total variation $O(L)$ by the elementary reciprocal sum over $v\le N$: each summand has $O(1)$ variation, since the cofactor composition is monotone on the compact physical interval and $|\beta|N\ll1$. If $\Omega,w$ are the hard or the smoothed weights, then $\|F_{i,m}\|_1\ll L$ and $\|F_{i,m}\|_2^2\ll L^2$. For either cutoff difference the stronger bounds are

$$
         \|F_{i,m}\|_1\ll\delta L,\qquad
         \|F_{i,m}\|_2^2\ll\delta L^2 .                              \tag{8}
$$

For the physical difference this follows from its support measure $O(\delta)$. For the cofactor difference, **each individual** $v$ term in (5) is supported, for $x$ in the fixed physical interval, inside the preimage of the two logarithmic cofactor endpoint strips. The function $\log(Nx/(s_i m_i m v))$ has derivative $1/x$ there. This preimage has measure $O(\delta)$ uniformly in every arithmetic label; its location need not be common to different $v$. Thus summing the $L^1$ bounds of the terms gives the first part of (8); multiply by the sup bound for the second. This requires neither an arithmetic short-interval estimate nor a polynomial bound on $s_i m_i$. If the original hard cofactor interval is shorter than the smoothing width, it is already contained in the same endpoint strips. Empty cuts cause no difficulty.

Apply dense Parseval or (7) to (6) at $\Lambda=C_*/m$, keep the extra masks until Cauchy in $(m,a)$, and drop them only in the individual positive squares. Put $\eta=1$ for original weights and $\eta=\delta$ for either difference vector. Each arm has

$$
 \sum_{m\ge1}\frac1{m^2}\sum_{a\ne0}
               |\widehat F_{i,m}(a C_*/m)|^2
                  \ll \frac{\eta L^3}{C_*},                          \tag{9}
$$

because its contribution at each $m$ is $O(\eta L^2/(C_*m))$, and $m\le u_i\le N$ on nonzero support. In particular (6) has the same bound. This crude estimate deliberately does not require the reciprocal Mertens norm at polynomial scale.

Keep the $h$ signs before bounding their paired sum. For fixed $g=(h_1,h_2)$ the exact coefficient from $\mu(h_1)\mu(h_2)/(h_1h_2)$ is

$$
 W(g)=\frac1{g^2}\prod_{\substack{p\mid N\\p\nmid g}}(1-2/p)\ge0 .
$$

This is zero if $2\nmid g$, and allows $q$ dividing $N$ just as before. From (9) the remaining factor in the $c_0$ sum is $c_0/(m_1m_2)$. The $c_N\mid g$ part supplies $\sigma(g)$ and hence
$\sum_{g\mid R}W(g)\sigma(g)=\prod_{p\mid N}(1-1/p+1/p^2)\le1$.
For the two square labels, primes in both give $1+p+p^2$ from $c_0/(m_1m_2)$, and primes exclusive to one label give $2$ because $m_i$ cancels the included $p$. Including the $s_i\mid l_i$ counts and $l_1^{-2}l_2^{-2}$, the resulting paired-label sum is bounded by

$$
                  \prod_p\left(1+\frac{8}{p^2}
                            +\frac{4(1+p+p^2)}{p^4}\right)<\infty.
                                                                    \tag{10}
$$

If one imposes $l_1>T$ or $l_2>T$, use Rankin with $l_i^\nu$ on that one arm for fixed $0<\nu<1$. It keeps (10) convergent, since exclusive and common factors involving that arm are now $O(p^{-2+\nu})$. The bound is then $O_\nu(T^{-\nu})$ by union of the two conditions; no need to put a moment on both arms of a common prime.

Combining (9)–(10) and $\sum_{q\in\mathcal Q}(q-1)\ll N/L$ now gives these uniform fixed-$\beta$ squared estimates:

$$
 \begin{array}{ll}
 \displaystyle O(N^2 L^3/L)
     &\text{for the vector of any finite subset of square labels},\\[2mm]
 \displaystyle O_\nu(T^{-\nu}N^2 L^3/L)
     &\text{if only square labels }l>T\text{ are retained},\\[2mm]
 \displaystyle O(\delta N^2 L^3/L)
     &\text{for either of the two cutoff difference vectors}.
 \end{array}                                                        \tag{11}
$$

To justify the expansions, for each finite square-label set all exterior $h$ labels are finite too, and (9) gives absolute summability of each scalar product by Cauchy. The tail bound independent of the finite upper cutoff proves Hilbert-space convergence as this cutoff tends to infinity, uniformly in $\beta$ for fixed $N$. At a fixed rational coordinate there is at most one integer $j$ per $(l,s,h,u)$; the absolute sum of amplitudes converges, using $\sum_l \tau(l)/l^2<\infty$ and finite $h,u$ ranges for fixed $N$. Thus the Hilbert-space limit is exactly (1) for the hard weights, rather than merely a choice of limiting norm. The same estimates allow the all-label smooth vector as well but do not ever introduce these labels into the finite modular construction.

## 3. Transfer to the literal hard limit

Use (11) with $\nu=1/2$. Compare $\mathcal H$ to $\mathcal R_T[\Omega_\delta,w_\delta]$ by first dropping the hard $l>T$ part and then telescoping the two real weights at $l\le T$. By triangle in the rational Hilbert space the squared difference is at most

$$
              O\!\left(\frac{N^2}{L}\,L^3(T^{-1/2}+\delta)\right),
                                                                    \tag{12}
$$

uniformly in $\beta$. Taking any sufficiently large fixed $J,K$ in (12) and using the unconditional (4) gives $\|\mathcal H\|_\beta^2\ll N^2/L$, and hence the claimed $\mathscr H_N\ll N/L$. For any fixed $A$, increase $J,K$ so that (12) and its squared-norm cross term with (4) are $O_A(N^2L^{-A})$. Integrate over the original $\beta$ interval. Combine this unconditional comparison with §1 and choose all finite transport accuracies accordingly. This proves (3) for the actual hard centered shell with the explicit cutoff-free model. Every use of any logarithmic or Fourier cutoff was in the comparison proof, and the two artificial completions were subtracted before the true centered transport.
