# A two-sided rational profile for the actual centered critical-shell energy

Let $N$ be even, $X=\sqrt N$, $L=\log N$, and $R=\operatorname{rad}N$, and write $e(z)=e^{2\pi iz}$. Use the genuine hard complementary polynomial of [the coherent square-label estimate](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md):

$$
 D_m=\mathbf1_{N-y\le m<N/2}
         \sum_{\substack{dk=m,\ d\in I_d,\ k\in I_k\\
                    (dk,N)=1,\ (d,k)=1}}\mu(d)\mu^2(k),
 \qquad D(\alpha)=\sum_m D_m e(\alpha m).
$$

Here $N/2\le y\le9N/16$, $I_k$ is a hard interval including $k>t\ge N^{.49999}$, and $I_d$ is any hard interval in $[X,\infty)$, intersected with $[X,N/(2t))$ without changing any actual term. The endpoints may move with $N$. Let $\mathcal Q=[.8X,.9X]\cap\mathbb P$. Denote by $\mathcal E_N(D)$ the squared sample norm at $a/q+\beta$, $q\in\mathcal Q$, $1\le a<q$, integrated over $|\beta|\le1/(10N)$. Write $\mathcal E_N^0(D)$ for the squared norm after orthogonal projection off the constant in each $q,\beta$ group of nonzero numerators.

Use the original $\delta=L^{-2}$ physical and cofactor smoothing and arithmetic cutoff $T=L^{16}$ of [the genuine hard approximation, §1](weak-s-type-ii-critical-prime-full-polynomial-inverse-log-grh.md#1-actual-transfers-at-the-smaller-smoothing-width). Write $\Omega$ for the physical weight in $x=m/N$ and $w(k)$ for the common short weight. Both are inward cutoffs at the actual intervals. Define the analytic rational vector for $\rho\in\mathbb Q\setminus\{0\}$ by

$$
 \begin{split}
 \mathcal R_{q,\beta}(\rho)
   ={}&\sum_{\substack{l\le T,\ l\ \mathrm{squarefree},\ (l,N)=1,\ s\mid l\\
                h\mid R,\ su\in I_d,\ (u,lN)=1\\ j=\rho l^2hu\in\mathbb Z\setminus\{0\}}}
       \mu(l)\mu(s)\mu(h)\mu(u)\frac{N}{q l^2 h u}\\
     &{}\hspace{13mm}\times
       \int_{\mathbb R}\Omega(x)e(\beta Nx)w(Nx/(su))e(-\rho Nx/q)\,dx .
 \end{split}                                                        \tag{1}
$$

All $h\mid R$ are present in this analytic vector. Set

$$
   \mathscr D_N=
        \int_{-1/(10N)}^{1/(10N)}
           \sum_{q\in\mathcal Q}q(q-1)
                  \sum_{\rho\in\mathbb Q\setminus\{0\}}
                               |\mathcal R_{q,\beta}(\rho)|^2\,d\beta .
 \tag{2}
$$

**Theorem (global Dirichlet GRH).** Assume GRH for all primitive Dirichlet $L$-functions, including $\zeta$. Uniformly in all the original even targets and hard cuts,

$$
                    \mathcal E_N^0(D)
                     =\mathscr D_N+O\!\left(NL^{-3/2}\right).
 \tag{3}
$$

The main rational norm $\mathscr D_N$ is bounded by $O(N/L)$ unconditionally; the two-sided transport to the true centered samples in (3) is conditional. The error in (3) is absolute, not an assertion that the rational profile is bounded below at arbitrary cuts. Together with [the true additive constant profile](weak-s-type-ii-critical-prime-polynomial-width-true-constant-profile.md), this splits the actual full energy into a conditional rational centered part and an unconditional additive mean part. It asserts nothing about a signed prime pairing or Hypothesis S.

## 1. Subtract the two artificially completed squares

Let $D^\dagger$ be the original smoothed approximation with the square cutoff $l\le T$, exact long unit and short inclusion $h\le H_0=\exp(C_0(1+\log L)^2)$, $h\mid R$. All its other definitions are unchanged. Use the finite character transform of [the coherent completion, §1](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#1-complete-the-square-only-after-adding-the-square-labels). In particular $i$ is an original divisor dyad of scale $A_i=\lambda_i X$, $\lambda_i\le N^{.00001}$, $U_i=A_i/s$, and $\xi=x_{q,i}/h=Ns/(A_i ql^2h)$ is the short mesh. Its true finite cutoffs are $|\tau|\le L^4$ and $0<|j|\le\lambda_iN^{.001}$, so all $l,h,j$ are units modulo every shell $q$ for large $N$. The array $\mathcal S_q(v)$ is on the common residue $v=l^2hu/j\bmod q$, after integration against $\widehat G_\beta(\tau)$. For each $\chi\ne\chi_0$ the finite character expression equals $\sum_{v\ne0}\mathcal S_q(v)\chi(v)$ times a Gauss factor of modulus $\sqrt q$.

The exact sum of the squared nonprincipal character expressions from this finite array, at fixed $\beta$, is therefore

$$
 \begin{split}
 K_\beta
  &=\sum_q q\sum_{\chi\ne\chi_0}
                 \left|\sum_{v\ne0}\mathcal S_q(v)\chi(v)\right|^2\\
  &=\sum_q q(q-1)\sum_{v\bmod q}|\mathcal S_q(v)|^2
       -\sum_q q(q-1)|\mathcal S_q(0)|^2
       -\sum_q q\left|\sum_{v\ne0}\mathcal S_q(v)\right|^2 .
 \end{split}                                                       \tag{4}
$$

This is finite multiplicative Parseval, not an inequality. The two subtracted terms are artificial completions and neither equals the actual additive group mean.

We first bound the middle term even when some long labels are nonunits modulo $q$. At a fixed $(l,s,h,i,\tau)$ in this array, $v=0$ is exactly $q\mid u$. There are $O(1+U_i/q)\ll N^{.00001}+1$ possible $u$. With the common exact short Fourier envelope,

$$
          \xi\sum_{j\ne0}|\widehat f_{i,\tau}(j\xi)|\ll Y_\tau,
             \qquad Y_\tau=1+L+|\tau| .
$$

This follows by splitting at $Y_\tau/\xi$ and summing the squared-frequency tail. It controls the true finite $j$ sum, without inserting new modular labels. On the retained $\tau$, $Y_\tau=O(L^4)$ and $\|\widehat G_\beta\|_1=O(1+\log L)$. The $l,s,i$ counts are fixed-polylogarithmic, and there are at most $H_0=N^{o(1)}$ possible $h$. Consequently

$$
 |\mathcal S_q(0)|\ll N^{.00001+o(1)},\qquad
       \sum_q q(q-1)|\mathcal S_q(0)|^2\ll N^{1.50002+o(1)}.         \tag{5}
$$

These bounds are uniform in $q,\beta$ on the genuine cuts.

Summing instead over **all** residues $v$ factors the long and short sums at each fixed $(l,s,h,i,\tau)$. The original masked GRH additive Möbius bound in the coherent determinant argument gives

$$
  \left|\sum_u a_{i,\tau}(u)\right|\ll U_i^{4/5}.
$$

This is its uniform bound at zero additive frequency, on the true long unit mask and signed hard support. Together with the same short Fourier $\ell^1$ bound and the outer counts it gives $\left|\sum_v\mathcal S_q(v)\right|\ll N^{.400008+o(1)}$. Restrict to $v\ne0$ by (5). Thus the last artificial square in (4), before $\beta$ integration, is

$$
          \sum_q q\left|\sum_{v\ne0}\mathcal S_q(v)\right|^2
                  \ll N^{1.800016+o(1)},                           \tag{6}
$$

using $\sum_q q\ll X^2$. In particular (5)–(6) include all $q$, including shell primes that happen to divide $N$.

## 2. Restore only the rational diagonal and transfer to the hard samples

In the first term of (4), the coherent expansion imposes
$l_1^2 h_1 j' u-l_2^2 h_2 j u'=bq$. The [original nonzero-determinant estimate and actual rational restoration, §1](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#1-complete-the-square-only-after-adding-the-square-labels) apply to this unchanged finite completed expression. The contribution from $b\ne0$ is $O(N^{1.91}L^{O(1)})$, uniform in $\beta$, by the same masked additive-Möbius bound under global GRH and the fixed nonzero $bq$ Fourier frequencies. On $b=0$ the equality is equality of the rationals $\rho=j/(l^2 h u)$. Restore the $\tau,j$ tails and the full analytic $h\mid R$ **only** in this exact rational norm. The stated restoration gives negligible logarithmic error, with any prescribed fixed accuracy by the established tail estimates and a sufficiently large fixed $C_0$. Fourier inversion with the original short bump equal to one on the physical support reassembles the divisor dyads into the actual interval and gives exactly (1). Its squared norm (at fixed $\beta$) is $O(N^2/L)$ by [the signed paired-label rational bound, §2](weak-s-type-ii-critical-prime-coherent-square-label-inverse-log-grh.md#2-factor-the-common-rational-denominator-before-the-square-label-sum), which is unconditional.

The true centered additive samples on $a\ne0$ have the extra positive factor $q/(q-1)$ per nonprincipal character squared norm. This follows since the multiplicative Fourier transform on the numerator group has Gauss magnitude $\sqrt q$ at each nonprincipal character and Parseval divides by $q-1$. The factor equals $1+O(X^{-1})$ uniformly. After the exact subtraction in (4) the finite character norm at each $q$ is nonnegative. The difference caused by this factor is therefore at most $O(X^{-1})$ times the total finite norm; the comparison using (5)–(6) and the rational bound makes this negligible. The true finite $\tau,j$ cutoffs also have the negligible errors in the genuine sampled norm of the coherent construction. Taking the fixed logarithmic accuracy there, and in the rational restorations, sufficiently high, integrating over the $\beta$ interval of length $1/(5N)$ gives

$$
                        \mathcal E_N^0(D^\dagger)
                             =\mathscr D_N+O(NL^{-3}).               \tag{7}
$$

Finally the original inward transfers and arithmetic cutoffs give the ordinary squared error $\|D-D^\dagger\|_2^2=O(NL^{-2})$. The actual arcs are disjoint and the centering is an orthogonal projection, so its squared error on the centered shell is no larger. Equation (7) and the rational bound show $\mathcal E_N^0(D^\dagger)=O(N/L)$. The cross term in the hard transfer is at most $O((N/L)^{1/2}(NL^{-2})^{1/2})=O(NL^{-3/2})$. This proves (3) on the original literal polynomials. Adding the genuine full-minus-centered energy is an exact orthogonal decomposition; the unconditional result for that additive mean does not remove the conditional input for (3).
