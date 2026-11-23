# The unchanged minor arcs down to largest-prime exponent $1/500$

**Scope.** Keep the actual squarefree mixed coefficient $M_>$ and the precise parity and small-prime counts of the [signed Euler slot estimate](r70-spectral-signed-shift-euler-slots.md): $L=\log N$, $U=\sqrt L$, $G=e^U$, with at most $\lfloor\log U\rfloor$ actual primes $\le G$ in odd total parity or at most $\lfloor(2/5)\log U\rfloor$ in even total parity. Keep the exact central hard interval $I$, the bounded-variation left weight $\omega$, and the actual largest-prime gate $P^+(m)>N^\kappa$. No prime-count gate, cutoff, or endpoint changes. The [preceding lower-largest-prime transfer](r70-spectral-lowest-largest-prime-transfer.md) proves the unconditional full arithmetic bound for every fixed $0<\kappa<1/2$. For the **genuine minor integral on its unchanged arcs** we now get the same bound for every fixed

$$
 1/500<\kappa<1/2
$$

under the same historical prime-character Dirichlet GRH input, including the principal inducing zeta case for the relevant conductors. For example $\kappa=1/400$ now qualifies. The proof uses no Möbius progression hypothesis. It does not estimate the complementary largest-prime or slot-count selectors or the entire Hardy residual.

In the notation of that transfer let $A(m)$ be the actual restricted partner weight, $P_{I,\omega}(\theta)$ the actual left polynomial, and $\widehat A(\theta)$ the actual right polynomial. For $\mathcal B=L^{-1/20}$ on odd only and $L^{-1/100}$ otherwise, the new assertion is

$$
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)
               e(-N\theta)\,d\theta\right|
    \ll \Sigma(N)|I|\mathcal B/L+N^{1-c},\qquad
 c=\min(10^{-4},(\kappa-1/500)/10).
 \tag{1}
$$

Here $N$ is every sufficiently large even target, and $\mathfrak m$ is the complement of the original reduced arcs $q\le Q=N^{1/1000}$, $|\nu|\le2Q/N$. Uniformity in $I$ and the conventions for one selected parity or their union are unchanged. The unconditional full bound is inherited, not strengthened here.

## 1. Integrate against the left main term before estimating progressions

Let $\Omega(u)={\bf1}_I(u)\omega(u)$, extended by zero, with its two endpoint jumps included when taking total variation. Put $V_I(\nu)=\int\Omega(u)e(\nu u)\,du$. The left prime main term on the reduced arc $a/q+\nu$ is $\mu(q)V_I(\nu)/\varphi(q)$. For the right frequency $x$ define

$$
 W_Q(x)=\int_{-2Q/N}^{2Q/N} V_I(\nu)e((x-N)\nu)\,d\nu
       =\int\Omega(u)K_Q(u+x-N)\,du ,
 \qquad K_Q(t)=\frac{\sin(4\pi Qt/N)}{\pi t}.
 \tag{2}
$$

The value at $t=0$ is $4Q/N$. This is the exact band-limited test, not a smooth approximation to the original hard interval. The major arcs are disjoint for large $N$. The same $\nu$ range at every denominator makes (2) independent of $q,a$.

On the actual right frequency support $V=[N/3,2N]$, all arguments in (2) have $|t|\le4N$. The bounded kernel estimate $|K_Q(t)|\le\min(4Q/N,1/(\pi |t|))$ gives $\int_{-4N}^{4N}|K_Q(t)|\,dt\ll 1+\log(2Q)$. Integration by parts in $u$ in (2) shows $W_Q'(x)=-\int K_Q(u+x-N)\,d\Omega(u)$, with the distributional derivative of the zero-extended $\Omega$. Fubini, first for the value and then for the derivative, yields

$$
 \sup_{x\in V}|W_Q(x)|+\operatorname{Var}_{x\in V}W_Q(x)
 \ll (\|\Omega\|_\infty+\operatorname{Var}\Omega)(1+\log(2Q)).
 \tag{3}
$$

In particular extending the right test by zero across its original endpoints costs only this same bound; there is no estimate over the entire real line and no assumption that $I$ is long.

Write the true right sequence using its unique largest prime $p$, $m=kp$, with $D<k\le K_1=2N^{1-\kappa}$ and $p>\max(P^+(k),N^\kappa)$, exactly as in the preceding transfer. Its real weight $F_k(x)$ is supported in $V$ and has supremum and total variation $O(\tau_4(k))$. This includes the exact squarefree, largest-prime and slot gates as encoded there and the true step or log weights of the mixed coefficient. In particular $p>Q$ throughout the new conditional range, so the progression variable on this leg never needs a nonunit correction; the left prime also exceeds $Q$.

The right progression error integrated against $V_I(\nu)e(-N\nu)$ is exactly the AP error on the test $F_k(kp)W_Q(kp)$. This follows by interchanging a finite prime sum and two compact integrals, using the exact density $dp/\log p$ for its principal model. The test has size and variation $O(\tau_4(k)(1+\log(2Q)))$ uniformly in the two original hard supports by (3) and the product variation bound.

## 2. Keep both exact numerator and residue savings

For each unit $v\bmod q$ write the integrated progression error explicitly as

$$
 \mathcal E_k(v;q)=
 \sum_{\substack{p\equiv v\bmod q\\ p\ {\rm prime}}}
                   F_k(kp)W_Q(kp)
 -\frac1{\varphi(q)}\int_2^\infty
                F_k(ky)W_Q(ky)\,\frac{dy}{\log y}.
 \tag{4}
$$

At all primitive conductors inducing a character mod $q$, including conductor $1$, use the usual GRH prime-progression estimate in character form (same [Montgomery–Vaughan, Theorem 13.7](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/conditional-estimates/98117860E24F0BB5605B4DF379A32190) as the preceding transfer). Removing prime powers and partial summation give a uniform unweighted prime-character discrepancy $\ll\sqrt{2N/k}L^{C}$ for endpoints up to $2N/k$. Here $q\le Q$ and $2N/k\ge N^\kappa$; the imprimitive deletion is already included in the character formulation. Applying the integrated BV test of §1 and then finite character Parseval, with the principal model in (4), gives

$$
 \sum_{v\bmod q}^*|\mathcal E_k(v;q)|^2
    \ll \tau_4(k)^2 (N/k)L^{C'}
 \tag{5}
$$

for an absolute fixed log exponent; the $1/\varphi(q)$ in the character expansion cancels the number of characters in this bound. Thus we retain the first Parseval saving without paying the old frequency variation $1+N|\nu|$.

Extend $\mathcal E_k$ by zero to nonunits and put $g=(k,q)$. The unchanged numerator map $a\mapsto ak\bmod q$ has $g$ preimages over every image point, so the full additive Parseval identity bounds the squared sum over $a$ by $qg\sum_v|\mathcal E_k(v;q)|^2$. Including the actual phase $e(-Na/q)$ does not change its norm. By Cauchy on the reduced numerators and summing $k$ the integrated error in these numerators has $\ell^1$ norm at most

$$
 \sum_{k\le K_1} q\sqrt{(k,q)}\tau_4(k)\sqrt{N/k}\,L^{O(1)}
     \ll_\epsilon q^{1+\epsilon}N^{1-\kappa/2+\epsilon}.
 \tag{6}
$$

For the last step use the divisor bound for $\tau_4$ and $\sum_{k\le K_1}\sqrt{(k,q)}/\sqrt k\ll\sqrt{K_1}\sum_{d\mid q}d^{-1/2}$, by summing the divisibility strata $d\mid k,\ d\mid q$. The remaining factor $\mu(q)/\varphi(q)$ from the left main term therefore bounds the right error across the full original major set by

$$
 O_\epsilon\bigl(Q^{1+\epsilon}N^{1-\kappa/2+\epsilon}\bigr),
 \tag{7}
$$

with the arbitrary epsilon enlarged as needed. No plus/minus numerator or modulus has been removed. In particular this is the signed major coefficient error after multiplication by the original left main term and $e(-N\theta)$; no claim of a smaller pointwise Fourier error for the right polynomial is required.

## 3. Restore the original model and subtract

Write the product difference as left error times actual right, plus left main times right error. The first term has the preceding transfer's bound $N^{1/2+o(1)}Q^5$: pointwise left error $O(q(1+N|\nu|)\sqrt N\,L^{O(1)})$, right supremum $N^{1+o(1)}$ and total arc measure $O(Q^3/N)$. There is no product of two approximation errors. The right main density, with its actual $c_q(k)/\varphi(q)$ factor, and left main are unchanged. Apply §3 of the [preceding transfer](r70-spectral-lowest-largest-prime-transfer.md#3-complete-the-real-major-density-and-subtract) verbatim to complete the real integral and the Ramanujan sum. Its inputs are support $k\le 2N^{1-\kappa}$, primes $p>Q$, $\log p\gg_\kappa L$, the same BV right weight and the arithmetic majorant of its §1. All hold here; the former $\kappa>1/250$ was used only for the right error exponent and to ensure $p>Q$. The completion gives the same genuine full local factor, zero for $(k,N)>1$ and $O(\Sigma(N)k/\varphi(k))$ otherwise; its tail errors $O(NQ^{-1}L^{O(1)}+N^{1+\epsilon}Q^{-1/4})$ are unchanged.

Thus the genuine major coefficient is bounded in absolute value by $\Sigma(N)|I|\mathcal B/L+O(N^{1-c})$, since $Q=N^{1/1000}$ in (7) and $\kappa>1/500$. The genuine full coefficient has the inherited unconditional bound of the same size. Subtract the major from the full coefficient to get (1). This only changes the tested fixed-power largest-prime range for the unchanged minor arcs; it does not assert cancellation on the unselected right weight.
