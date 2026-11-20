# The quadratic pair law persists on a shrinking window, conditional on S or R

Use the fixed height weight $a$, its squared time mass $I$, the full positive form factor $A$, and its single-index diagonal $D_0$ from [the round-4 definitions](review-round4.md). Set $L=\log N$ and assume local GRH(N) along the sequence of increasing even moduli. The following is a necessary consequence of either indicated norm hypothesis:

* **Under S:** take $T=L(\log L)^\kappa$ with any fixed $0<\kappa<1$.
* **Under R:** take $T=L^{2-\epsilon}$ with any fixed $0<\epsilon<1$.

The positive weighted off-index measures
$$
 \omega_{N,T}=\frac{T^3}{L^4}\,\mathbb E_{\chi\ \mathrm{odd}\bmod N}
 \sum_{j\ne k} a(\gamma_{\chi,j})a(\gamma_{\chi,k})\,
 \delta_{T(\gamma_{\chi,j}-\gamma_{\chi,k})}
$$
converge vaguely, and on Schwartz tests, to $I y^2\,dy/(24\pi)$. In particular, **for every fixed $b>0$** the unscaled weighted count with $|\gamma_j-\gamma_k|\le b/T$ is
$$
 \left(\frac{I b^3}{36\pi}+o(1)\right)\frac{L^4}{T^3}.
$$
Repeats with distinct labels are allowed, but their isolated mass at $y=0$ is $o(L^4/T^3)$ since the limit has no atom there. The test weight in absolute height is fixed, smooth and nonnegative, with compact Fourier support as specified in the definitions. The result is not an unweighted asymptotic for every compact interval of zero heights, nor a nearest-neighbor law. The spacing window is smaller than mean spacing by $L/T\to0$, so the statement does not follow by substituting a varying interval into [the fixed-test two-point law](review-round5.md). It uses a signed sum rule at finer precision. It proves neither S nor R.

## Proof

Take $t_0=L+C$ as in [the sharpened center estimate](review-refined-gaps.md). There are three central moment estimates:
$$
 \int_{-t_0}^{t_0}(A-D_0)\,dt=O_F((\log L)^2),\qquad
 \int_{-t_0}^{t_0}|A-D_0|\,dt=O_F(L^2),\qquad
 L^{-4}\int_{-t_0}^{t_0}t^2(A-D_0)\,dt\to-I/6.
$$
For the last one only the central, not exterior, part of the fixed-test proof is needed. The center measures $A(Lu)\mathbf1_{|Lu|\le t_0}du/(LI)$ converge on a fixed compact set to $\delta_0+|u|\mathbf1_{|u|\le1}du$. There are no endpoint atoms, since on the bounded seam in original time the induced prime sum has square mean $O_F(L)$ and the imprimitive error has negligible integrated mass. With $D_0/(LI)\to1$, the $u^2$ moment of the difference is $2I\int_0^1u^2(u-1)du=-I/6$ upon restoring the normalization. The spike at zero makes no contribution to this moment.

For a Schwartz gap test $f$ with smooth compactly supported frequency transform put $\psi(v)=(2\pi)^{-1}\int f(y)e^{-ivy}dy$, so $f(y)=\int\psi(v)e^{ivy}dv$. Both the true ordered measure and its limit are even; take the even part of the test. If $\psi$ is supported in $[-D,D]$, Fourier inversion gives
$$
 \int f\,d\omega_{N,T}=\frac{T^3}{L^4}\int_{-DT}^{DT}\frac{\psi(t/T)}{T}(A(t)-D_0)dt .
$$
On $|t|\le t_0$ expand $\psi(t/T)=\psi(0)+\psi''(0)t^2/(2T^2)+O_f(t^4/T^4)$. After normalization the constant term costs $O_f(T^2(\log L)^2/L^4)$, the fourth-order remainder is $O_f(L^2/T^2)$, and the quadratic term tends to $-I\psi''(0)/12$.

On the rest of this integral use the round-4 exterior estimate. Before normalization it costs, with fixed $D$,
$$
 O_{D,F,f}\left(M e^{2DT/L}+(\log L)^{C_F}/T+L/\varphi(N)+e^{-c\sqrt L}\right),\qquad M=\|T_N\|.
$$
For S, $M\ll\log L$ and $e^{2D(\log L)^\kappa}=L^{o(1)}$, whereas $L^4/T^3=L/(\log L)^{3\kappa}$. For R, $M\le e^{-L/2}L^{3/2}\sqrt{\mathfrak S(N)}$ and $DT/L=D L^{1-\epsilon}=o(L)$; further $(\log L)^{C_F}/T=o(L^4/T^3)$ since $T/L^2=L^{-\epsilon}$. The elementary $L/\varphi(N)$ and exponential errors are negligible in either regime. All remainders vanish in the normalized formula. Finally $-\psi''(0)=(2\pi)^{-1}\int y^2 f(y)dy$, giving the announced coefficient.

For extending the tests one must not bound by the full uncentered $A$ after multiplying by $T^3/L^4$: that would lose the needed cancellation. Instead let $g$ be an even nonnegative band-limited Schwartz function bounded below by 1 on $[-1,1]$. Translate the gap test to $g(y-s)$. Its even part corresponds to the compact frequency weight $\psi_g(v)\cos(sv)$, uniformly bounded in $s$, equal to $\psi_g(0)$ at the origin, and differing therefrom by $O_g((1+s^2)v^2)$ for $|v|\le t_0/T$. Use the signed zeroth moment, absolute $O_F(L^2)$ center bound, and uniform exterior bound as above. They give $\omega_{N,T}([s-1,s+1])\ll_g1+s^2$ uniformly. The weighted summation of this polynomial bound allows Fourier cutoff approximation in Schwartz topology; compact continuous tests follow by local uniform approximation. The interval limit follows by approximation since the boundary has zero limiting mass. The assertion about repeated labels at exactly zero follows by bounding their positive mass by that on $[-b,b]$ and taking $b\downarrow0$.
