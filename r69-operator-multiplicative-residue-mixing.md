# Multiplicative mixing of genuine exterior residue-orbit covariance

**Scope.** This is an all-alias, pointwise result for actual centered residue-orbit terms left after the bounded-degree deletion. It uses Fourier mixing of a specified arithmetic set of orbit ratios, not an absolute covariance bound or an alias band. A second result controls the signed difference of two positive-density sets of orbit pairs. The full unweighted covariance remains open.

## 1. Actual variance and the ratio mixing identity

Use the literal mesowindow means and the exact all-alias signed raw rectangle of [R68 §1](r68-operator-residue-orbit-and-alias-slope-covariance.md#1-antipodal-residue-orbit-covariance-with-exact-centering). Thus $Q\le N\le2Q$ is even and $N>2$, $1\le D\le H<M\le Q^\Gamma$ with $0<\Gamma<1$ fixed, and $V,U$ are two physical dyad starts. The same raw rectangle is imposed on all three original orientations; a bounded combination of such rectangles is allowed. This includes the true high–high complement of the low-raw cuts of [R65](r65-operator-dense-low-raw-alias-deletion.md). There is no truncation in the positive alias index $k$.

Let $G_N=(\mathbb Z/N\mathbb Z)^\times/\{\pm1\}$, $m_N=\phi(N)/2$. Write $C(r)=C_{N,r}$ for the exact real matrix of R68 (2): the integer tensor on the antipodal unit orbit $r$, with its equality atoms removed as in R68 (5), minus its canonical share $B_N/m_N$ of the exact signed continuous benchmark. In particular,

$$
\mathcal V_N=\left\|\sum_{r\in G_N}C(r)\right\|_{\rm HS}^2
   =\sum_{r,r'\in G_N}\langle C(r),C(r')\rangle_{\rm HS}
 \tag{1}
$$

is the genuine squared norm of the retained all-alias matrix of this dyad pair. By R68 (3), local odd Dirichlet GRH gives

$$
\sum_{r\in G_N}\|C(r)\|_{\rm HS}^2
      \ll_{\Gamma,\epsilon} Q^\epsilon\frac{\min(V,U)}{Q}.
 \tag{2}
$$

Here $V,U\ge1$, so the $+1$ in R68 can be absorbed. We also have the crude bound $\mathcal V_N\ll_{\Gamma,\epsilon}Q^\epsilon$. To see this without any conjecture on the dense covariance, use R68 (6) and partial summation to give $\sum_r\|d_V(r)\|_2^2,\sum_r\|d_U(r)\|_2^2\ll_\Gamma(\log(3Q))^4$, in its notation. The tensor sum of the $d_V(r)\otimes d_U(r)$ is bounded by the geometric mean of these two sums. The removed equality matrices sum in HS norm to $O_\Gamma((\log(3Q))^2)$ by the pointwise per-orbit bound in R68 §1, and the signed continuous benchmark is $O_{\Gamma,\epsilon}(Q^\epsilon)$ by R68 (10). Applying these bounds first with a smaller $\epsilon$ yields the asserted squared estimate.

For $S\subset G_N$, define the true signed graph contribution

$$
\mathcal V_N(S)=\sum_{\substack{r,r'\in G_N\\r'r^{-1}\in S}}
                            \langle C(r),C(r')\rangle_{\rm HS}.
 \tag{3}
$$

The original correlation is used on every retained ordered pair and includes all prime powers and the exact benchmark. This is not the sum of absolute values. One may exclude the identity from $S$ so that every pair is distinct.

For a character $\xi$ of $G_N$ put $\widehat C(\xi)=m_N^{-1/2}\sum_{r\in G_N}\overline{\xi(r)}C(r)$, and let $\lambda_S(\xi)=\sum_{a\in S}\xi(a)$. Finite-group Parseval on the complexified matrix space gives

$$
\mathcal V_N(S)
    = \frac{|S|}{m_N}\mathcal V_N
           +\sum_{\xi\ne1}\lambda_S(\xi)\|\widehat C(\xi)\|_{\rm HS}^2 .
 \tag{4}
$$

Indeed, $\sum_r\langle C(ar),C(r)\rangle_{\rm HS}$ is the contribution at ratio $a$, with the complex inner product taken linear in its first argument. Its Fourier multiplier is $\xi(a)$; summation yields (4). The original matrices are real, so the displayed sum is real even for a directed graph. It follows that

$$
\left|\mathcal V_N(S)-\frac{|S|}{m_N}\mathcal V_N\right|
       \ll_{\Gamma,\epsilon} Q^\epsilon \frac{\min(V,U)}{Q}
                    \max_{\xi\ne1}|\lambda_S(\xi)|.
 \tag{5}
$$

The same formula applies to a difference of two sets using their signed indicators. All expressions in (3)–(5) concern the exact finite matrix, with no random model for the residues.

## 2. A natural large-degree graph under local even GRH

For $2\le B<N/2$, take $S_B$ to be the set of ratios represented by the integers $2\le a\le B$ with $(a,N)=1$. These give distinct nonidentity orbits, because no two of these representatives are congruent or antipodal. In addition to the local odd GRH used above, assume local Dirichlet GRH for the **nonprincipal even** characters modulo $N$. Then uniformly in $B$,

$$
\begin{split}
 \left|\mathcal V_N(S_B)-\frac{|S_B|}{m_N}\mathcal V_N\right|
       &\ll_{\Gamma,\epsilon}Q^\epsilon\frac{\sqrt B\,\min(V,U)}{Q},\\
 |\mathcal V_N(S_B)|
       &\ll_{\Gamma,\epsilon}Q^\epsilon\left[
              \frac BQ+\frac{\sqrt B\,\min(V,U)}{Q}\right].
 \end{split}
 \tag{6}
$$

The same estimate holds for a multiplicative translate of $S_B$, if desired with the identity removed. Translation only multiplies the nonprincipal eigenvalues by unit phases; deleting one term adds at most one to their absolute bound. All estimates are pointwise, not averages over $N$.

In fact a character of $G_N$ is an even character of the unit group, extended by zero on the nonunits. Its nonprincipal prefix sum obeys

$$
\left|\sum_{a\le B}\xi(a)\right|\ll_\epsilon Q^\epsilon\sqrt B
     \qquad (2\le B\le N),
 \tag{7}
$$

by the standard even-GRH implication of generalized Lindelöf and truncated Perron. For precision, use $x=\lfloor B\rfloor+1/2$, $c=1+1/\log(2x)$, $T=(2Q)^4$. The truncated Perron error is $O(x\log(2x)/T)$ because the coefficients are bounded by 1: the terms $n\in[x/2,2x]$ contribute at most $O(x/T)\sum_{n\in[x/2,2x]}|x-n|^{-1}$, and the rest cost $O(x^c\zeta(c)/T)$. Shift the integral of $L(s,\xi)x^s/s$ to $\Re s=1/2+\delta$, crossing no pole for a nonprincipal character. For its inducing primitive character the usual GRH Lindelöf bound is uniform on this strip, in analytic conductor $N(2+|\Im s|)$; see, for example, the discussion opening [Lagarias–Soundararajan, §5](https://arxiv.org/pdf/1102.4911#page=19). The finitely many omitted Euler factors for an imprimitive character give $O_\eta(N^\eta)$ for each $\eta>0$, by $1+p^{-1/2}\le p^\eta$ for the large primes and a constant for the remaining primes. On the new vertical line use $x^{1/2+\delta}\log(2T)$ times the conductor bound, and on the horizontal edges use $x^c/T$ times that bound. Taking $\delta$ and the conductor exponent sufficiently small in terms of $\epsilon$, and using $x\ll Q$, proves (7). Removing $a=1$ has no effect on this bound. Now apply (5) and $|S_B|/m_N\ll_\epsilon Q^\epsilon B/Q$ to prove (6).

At $M=Q^{3/5}$, $B=\lfloor Q^{79/100}\rfloor$, this is $O_{\Gamma,\epsilon}(Q^{-1/200+\epsilon})$ **in the squared covariance expansion**, on every dyad pair, including the top comparable dyads. The density of this set of pairs tends to zero, but there are $Q^{179/100-o(1)}$ retained ordered pairs per dyad pair, since $|S_B|=B\phi(N)/N+O(\tau(N)+1)$. The degree is $Q^{79/100-o(1)}$; applying merely the absolute degree-limited R68 estimate would give no power saving at these parameters. Summing over the logarithmically many physical dyad pairs preserves the stated bound with $Q^\epsilon$. No auxiliary moduli are used, but the even-GRH assumption in this section is essential to the given proof.

## 3. Signed balancing of two positive-density ratio sets using local odd GRH alone

Let $L_0=\lfloor N/8\rfloor$. Let $S_1,S_2$ be represented by the units in $(L_0,2L_0]$ and $(2L_0,3L_0]$ respectively. For sufficiently large $N$ these intervals contain no identity representative, lie below $N/2$, and give disjoint sets of distinct orbits. Each graph covers $1/4+O_\epsilon(Q^{-1+\epsilon})$ of all ordered pairs, and

$$
\big|\mathcal V_N(S_1)-\mathcal V_N(S_2)\big|
     \ll_{\Gamma,\epsilon}Q^\epsilon
             \left[\frac1Q+\frac{\min(V,U)}{\sqrt Q}\right].
 \tag{8}
$$

This uses local odd GRH for the true prime matrices, and no GRH for the even mixing characters. The exact even character sums in the two intervals have the unconditional Pólya–Vinogradov estimate $O_\epsilon(Q^{1/2+\epsilon})$. For a primitive character of conductor $f\mid N$, completion by its Gauss sum of modulus $\sqrt f$, and the geometric progression sums bounded by $O(f/\min(b,f-b))$ for $b\bmod f$, give $O(\sqrt f\log(2f))$. For an imprimitive nonprincipal character, remove the primes dividing $N$ but not $f$ by inclusion–exclusion, reducing to primitive character sums on intervals at a cost $O(\tau(N))$. Finally the two equal-length intervals have unit counts differing by $O(\tau(N))$, again by divisor inclusion–exclusion. Thus their principal contributions in (4) differ by $O_\epsilon(Q^{-1+\epsilon}\mathcal V_N)$. Combining this with (5) gives (8).

In particular, any dyad pair with $\min(V,U)\le Q^{1/2-\eta}$ for a fixed $\eta>0$ has pointwise power-saving cancellation **between** the two genuinely dense signed covariance sums in (8). For example, an $H$-scale dyad with $H=Q^{2/5}$ and an $M$-scale dyad with $M=Q^{3/5}$ has error $O_\epsilon(Q^{-1/10+\epsilon})$, even with the true high–high raw cut. This does not say that either positive-density graph contribution separately is small. For two top dyads of scale $Q^{3/5}$, (8) supplies no power saving.

## 4. What the argument leaves

The full ordered-pair weight $1$ has only a principal Fourier eigenvalue, so (4) leaves exactly $\mathcal V_N$ for that weight. Even a perfect bound for every nonprincipal mixer eigenvalue cannot estimate that term. In §2 the principal contribution is small only because $|S_B|/m_N$ is small; in §3 it cancels between the two deliberately balanced sets. Neither observation proves the total dense variance or weak S. Nor is either estimate a statement about independent $\Lambda$ phases or about absolute covariance; they use signed sums of the actual centered matrix, with its exact continuum benchmark.
