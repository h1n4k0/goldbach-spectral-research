# Sharper moving-edge budget for signed central positivity

**Scope.** A refinement of the arithmetic hypothesis in the [signed rectangle criterion](spectral-signed-rectangle-central-positivity.md), not a proof of any signed discrepancy estimate or of S. It uses ordinary Brun–Titchmarsh and is independent of GRH as an implication.

Use the same $D=\lfloor\sqrt N/L^C\rfloor$, $Q=\lfloor N/D\rfloor$, $\mathcal B_*$, fixed nonnegative central bounded-variation $W$, and least prime $p_0\nmid N$ as in that criterion. With $L=\log N$ and $S=\mathfrak S(N)$, its conclusion $G_W\gg_W S/p_0$ already follows from the weaker asymptotic hypothesis
$$
 \mathcal B_* = o\left(\frac{N S^2}{L^2p_0^2}\right).
 \tag{1}
$$
For example $\mathcal B_*=o(N/L^4)$ suffices uniformly; when $p_0$ is bounded, $o(N/L^2)$ suffices, and the resulting representation count is of predicted order. In all cases the count conclusion is $\gg_W SN/(p_0L^2)$ on the stated strict upper central support.

Only the previously estimated moving-edge error changes. Partition the fixed support interval into $K$ bins with $1\ll K\ll L^3$, then freeze the moving $q$ cut as before. Let $H\asymp N/K$ be the raw length of a bin. Its changed $q$ lie in one interval of length $O(Q/K)$ with $q\asymp Q$. Uniformly for each such interval $J$,
$$
 \sum_{q\in J}\frac1{\varphi(q)}\ll\frac1K+\frac{L}{Q}.
 \tag{2}
$$
Indeed $q/\varphi(q)=\sum_{d\mid q}\eta(d)$ with $\eta(d)=\mu^2(d)/\varphi(d)$. Count multiples of $d$ in $J$ by $O(Q/(Kd)+1)$, use $q\asymp Q$, $\sum_d\eta(d)/d<\infty$, and $\sum_{d\le O(Q)}\eta(d)\ll L$. For the last estimate even $\sum_{d\le x}1/\varphi(d)\ll\log(2x)$ follows from the same divisor identity and the convergent weighted series.

For actual primes $n$ in the bin with $n\equiv N\pmod q$, the residue is reduced and $H/q\gg N^{1/2-o(1)}$. The interval [Brun–Titchmarsh theorem (Montgomery–Vaughan, Theorem 2)](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf), followed by the Mangoldt log weight, bounds the total prime weight by $O(H/\varphi(q))$; the logarithmic denominator $\log(H/q)\gg L$ cancels that weight. The corresponding baseline prime mass over the bin is $O(H)$ (the same interval theorem at modulus one), with the same multiplier $1/\varphi(q)$. The remaining $\log((N-n)/q)$ contributes at most $L$. Thus by (2) the total normalized edge error from primes is
$$
 O\left(\|W\|_\infty\frac{L}{N}KH
                 \left(\frac1K+\frac{L}{Q}\right)\right)
 =O\left(\|W\|_\infty [L/K+L^2/Q]\right).
$$
Proper prime powers cause a power-saving error independently of $K$: each actual power $n<N$ has at most $\tau(N-n)\ll_\epsilon N^\epsilon$ possible congruence moduli $q$, and the model pays at most $\sum_{q\le Q}1/\varphi(q)\ll L$. Each $n$ lies in just one bin; there are $O(\sqrt N)$ such powers, and the log weights are at most $L^2$. For example these power errors together are $O(\|W\|_\infty N^{-1/3})$ after normalization. Both real and baseline endpoints are treated by the same absolute bound, so strictness causes no additional issue.

The signed sum on each of the $K$ resulting fixed rectangles is unchanged and costs $O(L\|W\|_{\rm BV}\mathcal B_*)$ before normalization. Consequently the total changed edge plus the signed-rectangle error is
$$
 O\left(\|W\|_{\rm BV}
 \left[L/K+K L\mathcal B_*/N+L^2/Q+N^{-1/3}\right]\right).
 \tag{3}
$$
All other errors in the previous criterion remain $O_W(L^{-3})$ apart from the explicitly displayed $p_0$-jump error.

In (1) write $\beta_N=L^2p_0^2\mathcal B_* /(N S^2)\to0$, choose $k_N\to\infty$ with $k_N\le L$ and $k_N\beta_N\to0$, and take $K$ equal to the ceiling of $k_N Lp_0/S$. The elementary bounds $1\ll S\ll\log L$, $p_0\ll L$ ensure the permitted range of $K$. The first two terms of (3) are $o(S/p_0)$ by construction; the other terms are smaller as well. The prior jump argument gives error $O_W(S[L^{-3}+p_0\mathcal B_*/N])$. It too is $o(S/p_0)$ because $p_0^2\mathcal B_*/N=\beta_N(S/L)^2\to0$. The main lower term $S\int W/p_0$ therefore survives unchanged, and proper powers can be deleted as before. This proves the stated refinement, without resolving whether (1) holds.
