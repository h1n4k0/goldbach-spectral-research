# The near-full conductor core after the signed principal

Use the [R43 exact box](weak-s-type-ii-doubly-untagged-signed-principal.md): $N=2^j$, $X=\sqrt N$, $L=\log N$, $L_2=\log L$, and

$$
 I=[.740X,.745X],\quad J=[.715X,.720X],\quad D=[.445X,.450X].
$$

Both variables lack broad tags $\mathcal P=[S,N^{.001}]\cap\mathbb P$, $S=\exp(C L/L_2)$ with $C$ sufficiently large and fixed. Define $\alpha_u=\mu(u){\bf1}_{u\in I,\ u\ {\rm odd,\ untagged}}$, $\beta_v=(w(v)/L){\bf1}_{v\in J,\ v\ {\rm odd,\ untagged}}$, where $w(v)=\sum_{N^{.024}<p\le N^{.2499},\,p\mid v}\log p$ over primes. The original statistic is $L\sum_{u,v,d:uv\equiv N\bmod d}\alpha_u\beta_v\mu(d)\mu^2(N-uv)$ with $d\in D$ odd.

**Unconditional reduction.** Truncate the true square completion at $c\le B=\exp(L_2^2)$; its tail and the total signed principal are already $O_A(NL^{-A})$ by R43 for every fixed $A$. For odd squarefree $c,d$ put $g=(d,c)$, $d=ge$, $q=[d,c^2]=c^2e$; split the conductor $f$ of $\chi\bmod q$ as $f=f_0f_1$, $f_0\mid c^2,\ f_1\mid e$, and put $h=e/f_1$. Uniformly in $T\ge1$ and arbitrary hard subintervals of $I,J,D$, the part with $h\ge Tc^2$ of the exact nonprincipal expansion is, in original weight units,

$$
       O\left(\frac{NL}{T L_2}+NL e^{-c_0\sqrt L}\right).
 \tag{1}
$$

In particular $T=L/\sqrt{L_2}$ gives $O(N/\sqrt{L_2})$, and $T=L^{A+1}/L_2$ gives $O_A(NL^{-A})$. The real sign $\mu(d)$ is used for very small $f_1$. This is an exact spectral subfamily bound, not a deletion by tuple density.

**Marginal norm obstruction in the surviving primitive shell.** Under global Dirichlet GRH, on the full box, after summing over a positive-density subset $D_0$ of actual odd squarefree $d$, each separate primitive-character second moment for $c=1$ is $\asymp N/L_2$ with the normalization above. Thus the product of square roots used by separated Cauchy, even on this primitive shell alone, costs $\asymp NL/L_2$ in original units, not $o(N)$. This is not a lower bound for the signed primitive covariance or any larger signed sum. It leaves both correlation within that shell and interaction with the other square terms unresolved.

## 1. Very small variable conductors: keep the modulus signs

Let $A_q(\chi)=\sum_u\alpha_u\chi(u)$, $B_q(\chi)=\sum_v\beta_v\chi(v)$. Orthogonality gives the exact nonprincipal sum after square completion, suppressing the factor $L$:

$$
 \sum_{c\le B,\ c\ {\rm odd}}\mu(c)\sum_{d\in D,\ d\ {\rm odd}}
 \frac{\mu(d)}{\varphi(q)}
 \sum_{\substack{\chi\bmod q\\\chi\ne\chi_0}}
        \overline{\chi(N)}A_q(\chi)B_q(\chi).
 \tag{2}
$$

Since $\mu(c)\mu(d)\ne0$, the $f_0,f_1$ split is unique, with $(c,e)=1$. The inducing primitive character factors as $\psi_0\psi_1$ by CRT (including a possible conductor 1). With $e=f_1h$, $(h,cf_1)=1$, $\mu(d)=\mu(g)\mu(f_1)\mu(h)$, $\varphi(q)=\varphi(c^2)\varphi(f_1)\varphi(h)$, and $\chi(N)=\psi_0(N)\psi_1(N)$.

Fix $c,g,f_0,f_1,\psi_0,\psi_1$ with $f_1\le F_0=\exp(\kappa\sqrt L)$, where $\kappa>0$ is sufficiently small and fixed. Reverse the two coefficient sums; unless $(uv,cf_1)=1$ there is no contribution, and then the exact remaining mask is $(h,2cf_1uv)=1$. All restrictions on $d$ and $h\ge Tc^2$ give a single hard interval for $h$ at scale $X/(gf_1)=N^{1/2-o(1)}$. The [signed harmonic Mertens bound of R43, §1](weak-s-type-ii-doubly-untagged-signed-principal.md#1-signed-summation-of-the-principal-density) is $O(e^{-c_1\sqrt L})$ for $\sum\mu(h)/\varphi(h)$ on this masked interval uniformly. The bound for a single inducing character is $O(X^2e^{-c_1\sqrt L}/(\varphi(c^2)\varphi(f_1)))$. There are at most $\varphi(f_0)\varphi(f_1)$ primitive pairs, $\sum_{f_0\mid c^2}\varphi(f_0)=c^2$, and summing $c,g$ costs only $e^{O(L_2^2)}$. For $\kappa<c_1/4$ this gives $O(N e^{-c_2\sqrt L})$ in the normalized sum. No assumption on character cancellation is used in this step.

## 2. Large sieve over the remaining variable part

For $f_1>F_0$, Möbius de-mask the extension units exactly:

$$
 A_q(\chi)=\sum_{r\mid h}\mu(r) A_{r,c}(\psi_0\psi_1),
 \qquad
 A_{r,c}(\psi)=\sum_{\substack{r\mid u\\(u,c)=1}}\alpha_u\psi(u)
$$

and likewise for $B_{s,c}$. The $(u,f_1)=1$ restriction is already in $\psi$. At fixed $c,g$, let $Y=X/g$ and split $f_1\asymp F$ into dyads; $h\ge Tc^2$ implies $F\ll Y/(Tc^2)$. For fixed $f_1$, $\ell=[r,s]$, the sum over extensions in absolute value is bounded by

$$
 \sum_{\substack{h\asymp Y/f_1\\ \ell\mid h}}\frac1{\varphi(h)}
 \ll \frac1{\varphi(\ell)}.
 \tag{3}
$$

Indeed $\varphi(\ell k)\ge\varphi(\ell)\varphi(k)$ and $\sum_{k\asymp Z}\varphi(k)^{-1}\ll1$ uniformly (including small positive $Z$). The latter follows from $k/\varphi(k)=\sum_{a\mid k}\mu^2(a)/\varphi(a)$, a harmonic sum over multiples of $a$ in the dyad, and $\sum_a1/(a\varphi(a))<\infty$. Extra interval cuts and masks can be dropped in (3).

At fixed $f_0,\psi_0,r,s$, apply the [primitive multiplicative large sieve, Theorem 25.15](https://dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=281) over $\psi_1$ at $f_1\asymp F$ coprime to $c$, then Cauchy on $f_1,\psi_1$. For the first factor write $u=rk$; $|\psi_1(r)|\le1$ and the coefficient of $\psi_1(k)$ is $\alpha_{rk}\psi_0(rk){\bf1}_{(rk,c)=1}$, independent of $f_1$, supported in $[1,X/r]$. Dividing the large sieve weight $f_1/\varphi(f_1)$ by $F$ bounds the first squared norm by

$$
     O\bigl((F+X/F)\sum_{k\le X/r}|\alpha_{rk}|^2\bigr),
$$

and analogously for $\beta_{sk}$. The original phase $\overline{\psi_0(N)\psi_1(N)}$ has modulus 1. If $r\le N^{.1}$, the coefficient norm squared is $O_C(X/(r L_2))$: it is zero if $r$ has a broad tag, otherwise $k$ must be untagged, and the [R41 upper sieve](weak-s-type-ii-medium-prime-first-cell.md#3-a-small-elementary-sieve-sandwich) gives $O_C(X/(rL_2)+N^{.03}\log(2L_2))$ on that interval. The same holds for $s$. For large $r,s$ use the trivial $X/r,X/s$. The joint mask sum from (3) converges:

$$
   \sum_{r,s\ {\rm squarefree}}
        \frac1{\sqrt{rs}\,\varphi([r,s])}
      =\prod_p\left(1+\frac2{\sqrt p(p-1)}+\frac1{p(p-1)}\right)<\infty.
$$

The part $\max(r,s)>N^{.1}$ is $O(N^{-.025})$ by Rankin with $r^{1/4}$ or $s^{1/4}$ (both modified products converge). Hence the dyad bound before the fixed $c$-denominator is $O_C(X(F+X/F)/L_2)$ per fixed $\psi_0$. This unsigned estimate works also for a squared coefficient norm and arbitrary subfamilies and multipliers of modulus at most 1 in the modulus sum.

Summing the $\psi_0$ count over $f_0\mid c^2$ gives $c^2$, and summing $F\gg F_0,\ F\ll Y/(Tc^2)$ geometrically gives at fixed $c,g$

$$
 \ll_C \frac{c^2}{\varphi(c^2)}\frac{X}{L_2}
                         \left(\frac{Y}{Tc^2}+\frac{X}{F_0}\right).
$$

The $Y$-term is summable over $c,g$, since $\sum_c\varphi(c^2)^{-1}\sum_{g\mid c}g^{-1}<\infty$. The $F_0^{-1}$ term absorbs all $e^{O(L_2^2)}$ external completion counts. Combining with §1 and restoring $L$ proves (1). The exact square tail is bounded in R43 by $O(NL^{O(1)}B^{-1/2})$; the total principal was removed without GRH there.

## 3. Primitive second moments on genuine moduli

For large fixed $P_0$, let $D_0\subset D$ consist of squarefree $d$ with no prime factor $\le P_0$, and $\varphi(d)/d\ge1/2$. Then $\#D_0\gg X/\log P_0$, with a constant independent of fixed $P_0$ for large $N$. Indeed squarefree counting coprime to $\prod_{p\le P_0}p$ gives density $\gg1/\log P_0$; the absolute sum $\sum_{d\le X}\sum_{p\mid d,p>P_0}1/p\ll X/P_0$ bounds the number lost from the $\varphi(d)/d$ restriction.

Write $a_n$ for either $\alpha_n$ or $\beta_n$ on its full interval. For each $d\in D_0$,

$$
             \sum_{(n,d)=1}|a_n|^2\asymp_C X/L_2 .       \tag{4}
$$

The upper bound is the one-variable tag sieve. For the lower bound for $\alpha$, count squarefree $n\in I$ coprime to $2d$, untagged. Apply the R41 lower sieve in the tag divisors $r\le N^{.03}$, the exact inclusion-exclusion over divisors of $2d$, and complete the square condition at $B_0=S^{1/10}$. Floor errors are $O(N^{.03+o(1)})$ from the number of tag/square/mask divisors and the sieve coefficient bound. The omitted square tail is $O(X B_0^{-1}\exp(O(L/L_2)))$ by counting integers with a missing square and using the sieve multiplicity $\tau(n)$. For fixed $r$, extension only of the model square sum costs $O((X/r)B_0^{-1/2}\exp(O(\sqrt L)))$ by half-power Rankin: at $p\mid r$ the optional square divisor density is $1/p$ rather than $1/p^2$ after conditioning on $p\mid n$. These errors are $o(X/L_2)$, uniformly in $d$, for large fixed $C$, using $\sum_{r\le N^{.03}}1/r\ll L$. The main density before tag sifting is $\frac{\varphi(2d)}{2d}\prod_{p\nmid 2d}(1-p^{-2})\gg1$; the multiplicative tag factor is zero at $s\mid d$ and $(1/s-1/s^2)/(1-1/s^2)=1/(s+1)$ otherwise. Its sifted density is $\asymp_C1/L_2$ by the prime product, since $s\ge S$, at most $O(L_2)$ tag primes divide $d$, and $1/(s+1)-1/s=O(s^{-2})$.

For $\beta$, force $n=pm$ with a labeled $p\in[N^{.10},N^{.11}]$, omitting $p\mid 2d$. Use the same exact coprime mask and lower sieve on $m$ (no square gate), giving a main count $\gg_C X/(pL_2)$ with total floor errors over $p$ of $O(N^{.14+o(1)})$. The remaining reciprocal label sum is $\asymp1$ even after omitting the prime divisors of $d$, whose reciprocal sum in the band is $O(N^{-.10})$; label multiplicity is bounded, and each label gives $\beta_n\ge.10$. This proves (4).

All-character Parseval divided by $\varphi(d)$ is exactly $\sum_{(n,d)=1}|a_n|^2$, since the support interval has length less than $d$. Thus the total all-character energy on $D_0$ is $\gg_C N/(L_2\log P_0)$ and $O_C(N/L_2)$. The principal energy is $O_C(N/L_2^2)$ by $\#\mathrm{supp}(a)\ll_C X/L_2$ and the lower bound for $\varphi(d)$.

For the imprimitive energies, put $T_1=L^3$ and $f=\operatorname{cond}(\chi)$. Those with $h=d/f\ge T_1$ and $f>F_0$ have energy $O_C(N/(T_1L_2)+Ne^{-c_3\sqrt L})$ by the unsigned part in §2 for $c=1$ and coefficients $a,\bar a$. For the nonprincipal $f\le F_0$ use global Dirichlet GRH only here: the true transforms satisfy $|\sum a_n\chi(n)|\ll_C\sqrt X\exp(O(L/L_2))$. To verify the exact masks, let $E=\mathcal P\cup\{2\}$. The Dirichlet series for the unsliced $\alpha$ is $L(s,\chi)^{-1}\prod_{p\in E}(1-\chi(p)p^{-s})^{-1}$. That for the unnormalized $w$ sequence underlying $\beta$ is $L(s,\chi)\prod_{p\in E}(1-\chi(p)p^{-s})\sum_{p\ {\rm medium}}(\log p)\chi(p)p^{-s}$, since the marked primes are outside $E$. This identity requires no squarefree restriction on $v$. All these extra factors, including the finite inverse factors, are bounded on $1/2+1/L_2\le\Re s\le2,\ |\Im s|\le N^4$ by the shifted prime bound in [R42, §1](weak-s-type-ii-medium-prime-opposite-tags.md#1-the-long-transform-with-the-exact-wide-euler-exclusion), with prime 2 harmless; the $L^{\pm1}$ estimates and hard Perron bound used there yield the claimed transform. Induced characters are allowed since the cited proof accounts for their finite Euler corrections. Counting at most $\varphi(f)$ primitive characters for each $f$ and summing $h\asymp X/f$ with $1/\varphi(h)$ as in (3) bounds their total energy by $O(X F_0\exp(O(L/L_2)))=N^{1/2+o(1)}$. This nonnegative energy step does not use signed $h$-averaging.

For the remaining imprimitive characters $1<h<T_1$, any $p\mid h$ has $P_0<p<T_1$, and the character is induced from $d/p$. Summing over possible $p$ and applying Parseval modulo $d/p$ bounds their energy by the sum over $p,d$ with $p\mid d$ of

$$
 \frac1{p-1}\sum_{\substack{n,n'\ {\rm in\ interval}\\(nn',d)=1,\ 
                    n\equiv n'\bmod d/p}} |a_n a_{n'}|.
$$

The diagonal part totals $O_C((N/L_2)\sum_{p>P_0}(p(p-1))^{-1})=O_C(N/(P_0L_2))$ by (4) and $O(X/p)$ admissible $d$. For the off-diagonal put $e=d/p,\ n'=n+ke,\ 0<|k|\ll p$. Drop all conditions except the rectangular $n,e$ ranges and untagged $n,n+ke$. For fixed sieve divisors $r_1,r_2\le N^{.03}$, the condition $r_1\mid n,\ r_2\mid n+ke$ gives one residue of $e\bmod r_2$ per multiple of $r_1$ in the $n$-interval, since $|k|\ll L^3<S$. Even intersecting $r_1,r_2$ cause no extra condition. The rectangular count is area divided by $r_1r_2$, with error $O(X/r_1+(X/p)/r_2+1)$. Applying the product of two R41 upper sieves therefore bounds this count by $O_C(N/(pL_2^2)+N^{.56+o(1)})$ for each $p,k$, using the two prime products and at most $N^{.06}$ divisor pairs in the error. There are $O(p)$ choices of $k$ and a $1/(p-1)$ prefactor. Summing over $p<T_1$ gives off-diagonal $O_C(N\log\log(3T_1)/L_2^2+N^{.56+o(1)})=o(N/L_2)$.

Choose $P_0$ once such that $O_C(N/(P_0L_2))$ is smaller than half the all-character lower bound; its constant and the lower-bound constant are independent of fixed $P_0$. All other subtractions are $o(N/L_2)$. This proves

$$
 \sum_{d\in D_0}\frac1{\varphi(d)}
        \sum_{\chi\bmod d}^*
          \left|\sum_n a_n\chi(n)\right|^2
          \asymp_C N/L_2 \qquad (a=\alpha,\beta),
$$

as claimed. In the actual primitive covariance the factors also carry $\overline{\chi(N)}\mu(d)$; the lower bound is for the separated norm product, not for that signed expression. Neither this obstruction nor (1) proves weak S.
