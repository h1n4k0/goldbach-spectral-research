# A sharper central sum rule and microscopic pair-count obstruction

Keep the weighted odd-character family, fixed height cutoff $H$, $F,a,I,A,D_0$, and unweighted ordered excess-pair count $B_H(T)$ of [round 4](review-round4.md). In particular $F$ is the real even time autocorrelation narrowly supported in $(-w,w)$; $a$ is nonnegative and is bounded below on $[-H,H]$. Set $L=\log N$, $M=\|T_N\|$, and assume local Dirichlet GRH for the identification and the exterior estimate. For $T=L^2/8$, **R implies**
$$B_H(T)\ll_H (\log L)^{C_H}/L^2.$$
For $T=L\log L/8$, **S implies**
$$B_H(T)\ll_H L/(\log L)^3.$$
Constants are independent of the even modulus; these are upper bounds on a character-family average, not lower bounds, spacing asymptotics on shrinking windows, or simplicity for every character. Both are necessary conditions, not proofs of the norm conjectures.

## 1. The signed center has only polylogarithmic mass

Fix $t_0=L+C$ with the same fixed constant as in the round-4 exterior estimate. Write $b_\chi=\log(d_\chi/\pi)$, and let $G$ denote the fixed even real gamma correction in the narrow-window explicit formula there. Put $g=\int FG$. Applying the one-level formula to $a^2$ (whose inverse Fourier transform is $F*F$) gives **exactly**
$$D_0=I\,\mathbb E_- b_\chi+g.$$
Indeed the prime term has empty support at zero, and convolution with $F$ turns the gamma term at zero into $g$. The same cross term will appear below.

For $t\ge0$, first use the induced-character prime polynomial $P_\chi(t)=\sum \Lambda(n)\chi(n)F(\log n-t)/\sqrt n$. Up to $L-w-\log2$ odd orthogonality retains only its diagonal. On the remaining interval of bounded length up to $t_0$, the total extra contribution of the nondiagonal congruences is $O_F(\mathfrak S(N))$, not the diagonal-sized $O_F(L)$. In fact there $n,m\asymp_F N$; once the diagonal is removed there are only boundedly many positive shifts $kN$ for $m=n\pm kN$ or $m=kN-n$. Discard signs and unit restrictions. For each line the two-form upper sieve gives $\sum_{n\asymp_F N}\Lambda(n)\Lambda(kN\pm n)\ll_F N\mathfrak S(kN)$ on the part with both arguments positive and of size comparable to $N$. The variant $kN-n$ is identical. This is the dyadic argument of [arithmetic-round4.md, A](arithmetic-round4.md) on an interval of length $O_F(N)$, with both log weights $O_F(L)$ and all small-base prime powers included; $k$ is bounded and hence $\mathfrak S(kN)\ll_F\mathfrak S(N)$. The explicit weights $1/\sqrt{nm}$ supply the factor $O_F(1/N)$.

The integrated diagonal over both signs of $t$ is
$$2\int F(v)^2\sum_{n\le e^{t_0+v},\ (n,N)=1}\frac{\Lambda(n)^2}{n}\,dv
  = I t_0^2+O_F((\log L)^2).$$
The lower endpoint $t=0$ never cuts a prime-power window. The ordinary prime number theorem with classical remainder and partial summation give $\sum_{n\le e^s}\Lambda(n)^2/n=s^2/2+O(1)$; prime powers with exponent at least two contribute a convergent sum. The omitted local factors cost $\sum_{p\mid N}(\log p)^2/(p-1)\ll (\log L)^2$: for $p\le L$ use Chebyshev and partial summation; for $p>L$ bound $(\log p)/(p-1)\ll(\log L)/L$ and sum $\log p\le L$. Evenness kills the $t_0 v$ term.

The price of restoring the primitive character in the prime sum is also small. For $p^e\Vert N$, the probability in the odd family that $p\nmid d_\chi$ is at most $2/\varphi(p^e)$. Only on this event can the missing $p^j$ term survive. For its difference polynomial $R_\chi(t)$, triangle inequality in $L^2(dt\,d\chi)$ bounds its norm by
$$
 C_F\sum_{p\mid N}\frac{\log p}{\sqrt{\varphi(p^e)}}\sum_{j\ge1}p^{-j/2}\ll_F\log(2L).
$$
Here and below $p=2$ is harmless; $\sum_{p\mid N}(\log p)/p\ll\log(2L)$ follows by splitting at $L$. For the cross with $P_\chi$, its pointwise character RMS is $O_F(\sqrt{1+t})$ throughout the center by the bounded number of representatives in each unit class and Chebyshev. Apply Cauchy in the character variable to each restored prime-power term and then integrate on its $O_F(1)$ support. This costs at most
$$C_F\sum_{p\mid N}\frac{\log p}{\sqrt{\varphi(p^e)}}\sum_{j\ge1}p^{-j/2}\sqrt{1+j\log p}
 \ll_F (\log(2L))^{3/2}.$$
Again split the resulting sum $\sum_{p\mid N}(\log p)\sqrt{1+\log p}/p$ at $L$. All spike/prime crosses vanish by narrow support. The pure gamma square and gamma cross with $P_\chi$ are $O_F(1)$ by rapid decay; the restored/gamma cross is $O_F(\log(2L))$ by Cauchy. Thus the integrated prime and gamma contributions other than the spike, its gamma cross, and the full diagonal above change the total by at most $O_F((\log L)^2)$.

Finally $\mathbb E_- (b_\chi-t_0)^2\ll_C(\log L)^2$. To see this, the all-character family has independent conductor drops $D_p=(e-v_p(d_\chi))\log p$ by CRT. Their tails are $\mathbb P(D_p\ge j\log p)=\varphi(p^{e-j})/\varphi(p^e)\ll p^{-j}$, $1\le j\le e$. Hence the square of the sum has expectation $O((\sum_{p\mid N}\log p/p)^2+\sum_{p\mid N}(\log p)^2/p)=O((\log L)^2)$. Restricting to odd characters costs at most 2 for this nonnegative variable. Combining the spike-square, spike/gamma cross, prime diagonal and subtraction $2t_0 D_0$ now gives the signed sum rule
$$
 \int_{-t_0}^{t_0}(A(t)-D_0)\,dt
  =I\,\mathbb E_-(b_\chi-t_0)^2+2g(\mathbb E_- b_\chi-t_0)
   + O_F((\log L)^2)=O_F((\log L)^2).
$$
This cancellation is not an absolute-value bound. The absolute integral remains $O_F(L^2)$.

## 2. A smooth positive-definite replacement for the triangle

Choose a real, even, nonnegative $C_c^\infty$ bump $q$, supported in $(-1/2,1/2)$ and with positive integral. Its autocorrelation $\Psi=q*q$ is supported in $(-1,1)$, satisfies $\Psi(x)-\Psi(0)=O(x^2)$, and has nonnegative Fourier transform $|\widehat q|^2$ bounded below for $|\xi|\le1$ (use the radian transform $e^{i\xi x}$). In the positive counting inequality of round 4 use $\Psi(t/T)/T$. The center costs
$$O_F((\log L)^2/T+L^4/T^3),$$
using the signed sum rule for the constant term and the absolute $O_F(L^2)$ for the quadratic distortion. The outer estimate of round 4 is unchanged, since $\Psi$ is bounded and compactly supported. This yields for $T>t_0$
$$B_H(T)\ll_H (\log L)^2/T+L^4/T^3+M e^{2T/L}
 +(\log L)^{C_H}/T+L/\varphi(N)+O_H(e^{-c\sqrt L}).$$
The two stated bounds follow on inserting $M\le\sqrt{\mathfrak S(N)/N}\,L^{3/2}$ or $M\ll\mathfrak S(N)/h\ll\log L$, respectively. The cubic term agrees in its scale with the small-gap power predicted by the quadratic zero of the sine-kernel pair density; the proof gives no matching lower bound.
