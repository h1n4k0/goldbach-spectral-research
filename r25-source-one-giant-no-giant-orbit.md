# R25: a large one-giant/no-giant carrier, and its exact divisor-orbit compensation

Assume global Dirichlet GRH and use the original wide rough–rough kernel, with \(b_*=N^{3/40}\), \(D=D_*\asymp N^{43/120}\), \(Q=N^{7/8}\), and \(N\) tending through even moduli. We keep its original line signs, exact units modulo \(N\), deletion of the diagonal, and the condition of at most one distinct prime from \(W=\prod_{\ell\le\log N,\ \ell\nmid N}\ell\) on each raw integer. This note isolates the true central sum line of a **one-giant/no-giant** orientation. It is not a lower bound for the complete rough–rough kernel or \(T_N\).

Set
\[
 a=\tfrac1{10},\quad b=\tfrac3{25},\qquad u=\tfrac{37}{100},\quad v=\tfrac{39}{100}.
\]
Choose disjoint small closed physical intervals \(J_-\subset(0.46,0.49)\) and \(J_+=1-J_-\), and nonnegative smooth \(f,g\) supported in their interiors, with \(I_{f,g}:=\int f(x)g(1-x)\,dx>0\). On \(J_-\times J_+\) there is exactly one possible alias, \(n+m=N\), with **negative** outer sign. Select:
* the left raw integer \(n=pq\), with \(p,q\) prime and \(N^a\le q\le N^b\), keeping **all** its genuine long divisors;
* on the right, just the individual long-divisor term \(e\) prime, \(N^u\le e\le N^v\), \(e\mid m\), \(e^2\nmid m\).

Let \(C_{\rm iso}\) be this arithmetic kernel, summing each eligible \(e\) once. Write \(L=\log N\) and
\[
 B_N=\prod_{\ell\mid W}\left(1-\frac1{\ell-1}\right)
        \left(1+\sum_{\ell\mid W}\frac1{\ell-2}\right).
\]
There is a canonical pair of compact Hardy probes, defined below, on which the signed matrix element of \(C_{\rm iso}\) is
\[
 -2\pi\,B_N L\,(C_{f,g}+o(1)),\qquad
 C_{f,g}=I_{f,g}\log\frac{1-a}{1-b}\,[\log(v/u)-(v-u)]>0.             \tag{1}
\]
The \(o(1)\) is uniform over sufficiently large even \(N\). In particular the absolute probe is \(\gg \log N/\log\log N\) on **every** such modulus. The right raw integer has no admissible giant in the [R23 sense](r23-source-giant-cofactor.md), even before its other long divisors are considered.

For an exact compensation statement, select just the **least** eligible \(e\) for each right integer \(m\) (if there is any). The corresponding isolated term still has negative probe magnitude \(\asymp B_N L\). Complete this selected right divisor's orbit by including all true divisors \(e t\mid m\). The completed coefficient is exactly \(-\Lambda(m/e)\) on the right; the completed-orbit probe is \(O((\log\log(3N))^2)\). Thus the isolated carrier has a provable, explicit opposing contribution among its genuine multiples. What remains in this orbit is the two-prime input \(p\) and \(m/e\), plus a power-saving contribution from proper powers of \(m/e\); long right divisors **not** containing the selected \(e\) remain unestimated.

## 1. Exact admissibility and signs

For large \(N\), \(q\le N^{.12}<D\) and \(p\asymp N/q\gg N^{.88}\) on \(J_-\). Thus \(p>D,\ q\le D,\ pD>Q\), with unique \(p\). The genuine left long coefficient is \(-\Lambda(q)=-\log q\) by [R23](r23-source-giant-cofactor.md). This collapse is valid for every selected \(e\) and every divisor multiple added later, since each right divisor is \(>D\), so \(pD>Q\) ensures every left-long/right-long product passes the original cutoff. Both left factors exceed \(\log N\), so the first raw leg is fully rough.

On the right put \(s=m/e\). We have \(e>D\) since \(u>43/120\), and \(s\gg N^{1-v}>D\). For any prime factor \(p_0\) of \(m\), if \(p_0=e\) then the cofactor is \(s>D\); otherwise \(m/p_0\) is divisible by \(e>D\). Hence no prime factor of \(m\) has cofactor at most \(D\), and there is no admissible giant. This remains true separately from the exact condition \(m\) be rough-for-this-step. Since \(\mu(e)=-1\), the right individual coefficient is \(-\log s\). Consequently both original internal factors are negative, and the original sum sign makes the contribution of every isolated \(e\) nonpositive. The raw supports are disjoint, so the diagonal never enters. When necessary use \(q,e\nmid N\): if either divides \(N\) its raw integer is not a unit and must be excluded.

## 2. Pointwise count with the exact Boolean roughness mask

Ignore \(e^2\nmid m\) temporarily. For fixed \(q,e\nmid N\) in the specified disjoint prime ranges, and any \(P\mid W\), the condition \(eP\mid m=N-qp\) gives a **reduced** residue class for \(p\bmod eP\). This is because \((q,eP)=(N,eP)=1\). The only remaining unit restriction is \(p\nmid N\); at most \(O(\log N)\) such prime points are deleted per term. All factors \(p,q,e\) are odd for large \(N\); \(N\) is even and \(m=N-qp\) is odd. Because \(2\mid N\), the prime \(2\) is not in \(W\), and hence causes no singular denominator in \(B_N\).

Expand the right mask of at most one prime from \(W\) as in [R24](r24-source-one-giant-proper.md), with constant coefficient \(1\) and higher terms \((-1)^{\omega(P)+1}(\omega(P)-1)\mathbf1_{P\mid m}\) for \(\omega(P)\ge2\). Its absolute expansion mass is \(N^{o(1)}\), and \(eP\le N^{O(1)}\). The [GRH progression PNT of Lee, Corollary 1.1 and §5](https://arxiv.org/pdf/2301.13457v2), with partial summation as checked in R24, replaces the prime count in each reduced class by \(dp/(\varphi(eP)\log p)\) at error \(O_\epsilon(\sqrt{N/q}\,N^\epsilon)\), absorbing logarithmic weights. If the modulus exceeds a counting endpoint, that portion has at most one point and model \(O((\log N)^C)\), so this theorem's range restriction introduces no loss. The marker \(\log((N-qp)/e)f(qp/N)g(1-qp/N)\) has bounded variation \(O(L)\) on its fixed ratio support, uniformly in \(q,e\). Thus the total raw error after summing \(q,e,P\) and their weights is
\[
 O_\epsilon\!\left(\sqrt N\,N^\epsilon
           \sum_{q\le N^b}q^{-1/2}\sum_{e\le N^v}1\right)
   = O_\epsilon(N^{1/2+b/2+v+\epsilon})=O_\epsilon(N^{.95+\epsilon}).
\]

The prime-density main factor \(\varphi(eP)^{-1}=(e-1)^{-1}\varphi(P)^{-1}\) realizes the exact Boolean polynomial at the independent probabilities \(1/(\ell-1)\), \(\ell\in W\). Its value is the probability \(B_N\) of at most one success, giving precisely the displayed formula. In particular \(B_N\le1\) and
\[
 B_N\ge \prod_{3\le\ell\le\log N,\ \ell\ {\rm prime}}
                   (1-1/(\ell-1))\gg 1/\log\log(3N)
\]
by Mertens' product, since deleting primes from that product only increases it and its ratio to \(\prod(1-1/\ell)\) has a bounded positive limit. This density calculation does not replace the actual mask by fully rough integers.

Change variables \(x=qp/N\) in the integral. The positive raw arithmetic weight, without the outer minus, is
\[
 N B_N\int f(x)g(1-x)\!
     \sum_{q,e}\frac{\log q}{q(e-1)}
       \frac{\log(N(1-x)/e)}{\log(Nx/q)}\,dx
       +O_\epsilon(N^{.95+\epsilon}),
\]
where \(q,e\nmid N\) are in the specified bands. Uniformly on the support the ratio of logarithms is
\((1-\log e/L)/(1-\log q/L)+O(1/L)\). The ordinary PNT and partial summation give
\[
 \frac1L\sum_q\frac{\log q}{q(1-\log q/L)}
          \longrightarrow\int_a^b\frac{d\alpha}{1-\alpha},\qquad
 \sum_e\frac{1-\log e/L}{e-1}
          \longrightarrow \int_u^v\frac{1-\beta}{\beta}\,d\beta .
\]
Only \(O(1)\) of the primes in either band can divide \(N\), by their size, so these exclusions do not affect the limits. This proves the raw main constant in (1). To restore \(e^2\nmid m\), note that \(m\) fixes \(n\), and there is at most one left factorization because the \(q\) and \(p\) ranges are disjoint by widely separated sizes (two different \(q\)'s would contradict the unique giant). The omitted pairs counted with multiplicity of \(e\) are at most
\(\sum_{e\ge N^u}\lfloor N/e^2\rfloor=O(N^{1-u})\).
Their weighted contribution is \(O_\epsilon(N^{.63+\epsilon})\). Both raw errors are \(o(NB_N L)\) uniformly over the even moduli. This gives (1) after normalization.

## 3. Least eligible prime, complete divisor orbit, and the remaining prime input

A given right integer \(m\le N\) has at most two distinct eligible primes, since \(3u>1\). The two possible weights \(\log(m/e)\) are comparable by absolute constants, as every \(s=m/e\asymp N/e\) satisfies \(\log s\asymp L\). Thus keeping only the least \(e\) among those with \(e^2\nmid m\) retains at least a fixed positive fraction of the total probe, which has one sign. No density approximation to this least-prime mask is needed. The choice is now unique and there is no overlap of orbit counts. For that chosen \(e\), \((e,s)=1\), including when \(s\) is not squarefree. Every divisor \(e t,\ t\mid s\), is a genuine right long divisor, survives the original product condition against every left long divisor, and has coefficient \(-\mu(t)\log(s/t)\). Summing this entire orbit gives \(-\Lambda(s)\) exactly, with \(t=s\) contributing zero. The added multiples \(t>1\) change the **signed** coefficient by \(+(\log q)(\log s-\Lambda(s))\) after incorporating the sum-line sign and left collapse; this is nonnegative. If \(s\) is not a prime power the orbit cancels to zero. If \(s\) is a prime, the support is two primes \(p,s\) in the equation \(q p + e s=N\) with the original unit condition; the other possible \(s\) are proper prime powers.

To bound the orbit after this cancellation, the upper estimate may ignore the least-prime, right roughness, and \(e^2\) masks. For each \(e\), the proper powers \(s\le N/e\) number \(O(\sqrt{N/e}\log N)\). Each fixes \(m,n\), hence at most one \(q,p\), and carries weight \(O(L^2)\). Summing \(e\le N^v\) gives \(O_\epsilon(N^{1/2+v/2+\epsilon})=O_\epsilon(N^{.695+\epsilon})\) in raw weight.

For \(s\) prime fix \(q,e\), which are distinct units modulo \(N\). The form \(q p+e s=N\) parametrizes \(p,s\) by affine forms of steps \(e,-q\), determinant \(N\), on an interval of length at most \(N/(qe)\). Enlarge to an interval of length \(H\asymp N/(qe)\gg N^{1-b-v}=N^{.49}\). Both prime values are \(\gg N^{1-v}\) and so exceed \(H^{1/10}\). The uniform two-form Selberg proof in [R23](r23-source-double-giant-proper.md) gives \(O(H(\log\log(3N))^2/L^2)\) on every such interval: the omitted primes divide \(2qeN\), and the nonzero determinant retains the same singular-factor bound. Coincident primes would force a shared raw factor and are impossible on genuine units; allowing them in the upper majorant does not change the form determinant. After weighting by \((\log q)(\log s)\), use \(\sum_q\log q/q\ll L,\ \sum_e1/e\ll1\) on these bands. This gives the total raw prime weight \(O(N(\log\log(3N))^2)\) as claimed. The omitted proper powers are smaller. The full right long coefficient on this chosen-pair region still includes
\[
 \sum_{\substack{t\mid s\\t>D}}\mu(t)\log(m/t)
\]
from right divisors not containing \(e\), which is not estimated here. In particular it would be wrong to substitute \(-\Lambda(s)\) for the *whole* opposite leg.

## 4. Exact compact Hardy probe and scope

In physical log coordinates with measure \(dx/x\), write
\[
 v_f(x)=\sqrt{xw_N(x)}\,\bigl(f(x)/2-xf'(x)\bigr),
 \qquad
 v_g(x)=\sqrt{xw_N(x)}\,\bigl(g(x)/2-xg'(x)\bigr).
\]
They are supported in the fixed \(J_-,J_+\subset(0,1)\), and have uniformly bounded norm since \(w_N\asymp1\) on the fixed supports. For the cumulative coefficient measure \(\mu_C\) of a selected component after the original \(1/N\) normalization and line signs, the physical log kernel is \(2\pi\int_{(0,x]\times(0,y]}\sqrt{uv}\,d\mu_C(u,v)/(xy\sqrt{w_N(x)w_N(y)})\). Then Fubini and
\[
 \int_u^\infty \frac{v_f(x)}{x^2\sqrt{w_N(x)}}\,dx=f(u)/\sqrt u
\]
(each integrand is minus the derivative of \(f(x)/\sqrt x\)) give
\[
 \langle C v_g,v_f\rangle=2\pi\int f(u)g(v)\,d\mu_C(u,v).
\]
This is a genuine compressed matrix element, not a hard-window-to-operator inference from cancellation of a scalar. If one wants a symmetric component, include the reflected pair support; it contributes zero to this same oriented matrix element because the two test supports are disjoint. Under local GRH(N) the representation is that of the manuscript; global Dirichlet GRH was additionally used for (1). The large isolated probe is *not* an obstruction to S: part of its own opposing divisor orbit is explicitly identified above, and the rest of the original signed kernel has not been bounded.
