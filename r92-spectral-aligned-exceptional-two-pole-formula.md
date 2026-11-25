# The aligned-conductor exceptional term has a two-pole formula

**Scope.** Suppose the possible Page conductor $r$ divides the actual even target $N$. The genuine remaining hard exceptional correction of the mixed strip then has an explicit two-pole formula, before any positivity or smallness estimate. Both true squarefree parities are covered. The coefficient has finite Ramanujan weights, explicit local factors, and genuine geometric kernels at the original hard cuts. No Dirichlet GRH or external real-zero-gap input is used. The result neither treats targets with $r\nmid N$ nor bounds the displayed colored remainder by a small quantity. It proves no uncorrected planted law, prime-pair representation, or Hypothesis S.

Use the parameters of [the all-scale correction](r87-spectral-all-scale-exceptional-left-reduction.md): $Y\le N\le2Y$, $G=\log Y$, $L=\log N$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$ for fixed admissible $B>B_0>0$. The hard central real half-open interval $I\subset(N/2,9N/16]$ and its uniformly bounded pointwise-BV weight $\omega$ are unchanged. Let $\chi=\chi^*$ denote the actual primitive real Page character, when it exists, with conductor $r\le Q_0$ and simple zero $\beta>1-4a_0/\sqrt G$. Do not change the exceptional threshold. Take the two colors $A_0=M_>$, $A_1=\mu(m)M_>$ on squarefree $m\in[N/3,2N]$, with exact four labels $m=abcd$, pairwise coprime and squarefree, gates $D<\min(ab,ac)<\sqrt m$ and $abc>H_0$, and centered weight $1-2\log(ac)/\log m$. Thus the signed legs are $b,c$ for $A_0$ and $a,d$ for $A_1$. These are the actual coefficients **before** the overall subtraction defining the mixed correction.

Put $S=Y^{1/10}$. The [long unsigned deletion](r91-spectral-exceptional-long-unsigned-deletion.md) restricts the unsigned labels to $a,d\le S$ or $b,c\le S$, respectively, in the genuine hard exceptional term. Denote these retained arrays by $A_i^{\rm ss}$. Use their true signed signs and actual interval tests, not an artificial fixed band for the two large factors.

## Formula

Retain the finite $t\le Q_0/r$ sum of the [hard exceptional transfer](r88-spectral-hard-exceptional-residue-transfer.md). In the following local factors $q\mid t$ and $\mu(t)\ne0$, so $q$ is squarefree and $(q,r)=1$. For $p\nmid r$ put $c_p=\chi(p)p^{-\beta}$ and $E_p=(1-c_p)^{-1}$. For $(h,r)=1$, with $h$ squarefree, define

$$
 \begin{split}
 \mathcal L(h;q,N)={}&
  \prod_{\substack{p\nmid r\\p\nmid qh}}(1-p^{-2\beta}E_p^2)
  \prod_{\substack{p\mid h\\p\nmid q}}E_p^2
  \prod_{p\mid(h,q)}E_p^2\mathbf1_{p\mid N}\\
 &{}\times
  \prod_{\substack{p\mid q\\p\nmid h}}
      E_p^2\left(\frac{\mathbf1_{p\nmid N}}{p-1}
                            -2c_p\mathbf1_{p\mid N}\right).
 \end{split}
 \tag{1}
$$

The infinite part converges absolutely since $\beta$ is close to one. Primes of $r$ contribute one and are not included in (1). There is no division by the possibly small local factor $1-p^{-2\beta}E_p^2$, at $p=2$ or elsewhere. In particular (1) uses actual $p\mid N$ on the finite Ramanujan denominator and does not replace it by $p\mid r$.

At a real physical $x=N-n$ with $n\in I$ let $T_x=\log(x/D^2)>0$. For short labels $u,v\le S$ put $\rho=|\log(u/v)|$ and

$$
 \begin{split}
 \mathcal G_0(x;u,v)&=-\frac{\rho\min(T_x,\rho)}{2\log x},\\
 W_x(u,v)&=\left[\min\left(\frac{T_x}{2},
              \frac12\log x-\log H_0+\log\max(u,v)\right)\right]_+,\\
 \mathcal G_1(x;u,v)&=\frac{W_x(u,v)^2-W_x(u,v)\rho}{\log x}.
 \end{split}
 \tag{2}
$$

The pair $(u,v)$ denotes $(a,d)$ for $i=0$ and $(b,c)$ for $i=1$. Define the following quantity (the integral is over the real $x$ with $N-x\in I$, which automatically lies in the physical support):

$$
 \begin{split}
 \mathcal D_i={}&-\frac{r\chi(-1)}
        {\varphi(r)L'(\beta,\chi)^2}
 \sum_{\substack{t\le Q_0/r,\ t\ {\rm sf}\\(t,r)=1}}\frac{\mu(t)}{\varphi(t)}
       \sum_{q\mid t}q\,\mu(t/q)
 \sum_{\substack{u,v\le S,\ u,v\ {\rm sf}\\
                   (u,v)=1,\ (uv,r)=1}}
       \frac{\chi(uv)}{(uv)^\beta}\mathcal L(uv;q,N)\\
 &{}\hspace{19mm}\times
  \int_{N-x\in I}\omega(N-x)(N-x)^{\beta-1}x^{\beta-1}
                                \mathcal G_i(x;u,v)\,dx .
 \end{split}
 \tag{3}
$$

**Theorem.** If the Page zero exists and $r\mid N$, uniformly in the genuine $N,I,\omega$ and for each fixed $A>0$,

$$
              \mathfrak E_\pm
                   =\tfrac12(\mathcal D_0\pm\mathcal D_1)
                                +O_A(Y^\beta G^{-A}).
 \tag{4}
$$

When the Page zero is absent the original correction is zero as usual. The statement in the presence of the zero is a pointwise replacement of that correction, which can be inserted in the earlier full and original-major formulas only with their own qualifications. In particular there is no additional statement about their target exceptional sets. The sign in (3) comes from the hard left correction, while the two signs in (4) are the true squarefree total prime-factor parities.

## 1. Exact single-pole progression, including nonunits

For the proof let $q$ be any squarefree integer with $rq\le Q_0$ and $(q,r)=1$, let $b\bmod q$ be any residue, and let $w\le Y^C$ be a coprimality mask for fixed $C$. Put $g=(b,q)$ and define

$$
 B(w;q,b)=\mathbf1_{(g,w)=1}
       \frac{\mu(g)\chi(g)g^{-\beta}}{\varphi(q/g)}
                 \prod_{p\mid wq}(1-\chi(p)p^{-\beta})^{-1}.
 \tag{5}
$$

Then for some fixed $c>0$ and $Y^{1/4}\le X\le4Y$,

$$
 \sum_{\substack{n\le X,\ n\equiv b\ (q)\\(n,w)=1}}\mu(n)\chi(n)
     =\frac{B(w;q,b)}{L'(\beta,\chi)}\,\frac{X^\beta}{\beta}
                         +O(Xe^{-c\sqrt G}).
 \tag{6}
$$

For $q=1$ use its single residue and take $g=1$. Formula (6) uses the simple pole of the actual reciprocal Dirichlet function, not the pole residue of its logarithmic derivative.

To verify it, if $(g,w)>1$ the progression sum is zero. Otherwise write $n=g\ell$. The new class $b/g\bmod q/g$ is reduced, and the true identity
$\mu(g\ell)\chi(g\ell)=\mu(g)\chi(g)\mu(\ell)\chi(\ell)\mathbf1_{(\ell,g)=1}$ holds since $q$ is squarefree. Apply character orthogonality modulo $q/g$ with the mask $wg$. If a character $\psi$ there has primitive part of conductor $f$, the product of $\chi$ with that primitive part is primitive of conductor $rf$ by the coprime CRT. For a nonprincipal $\psi$, $f>1$ and this product is not the Page character. For the principal $\psi$ the primitive is exactly $\chi$. Its reciprocal Dirichlet function with all the masks and omitted local factors is $L(s,\chi)^{-1}\prod_{p\mid wq}(1-\chi(p)p^{-s})^{-1}$: $q/g$ contributes its unit restriction, and the additional $g$ from $\mu(g\ell)$ restores the remaining primes of $q$. Repeated restricted primes enter only once. This proves the factor in (5) on taking its residue and replacing $X$ by $X/g$. All other characters have no pole in the rectangle.

Here are the uniform contour checks. Use the same narrow real strip and height $T_*=e^{\sqrt G}$ as in [R87, Section 2](r87-spectral-all-scale-exceptional-left-reduction.md#2-treat-only-the-left-arithmetic-on-the-excluded-arcs), now shifting $1/L$ rather than $-L'/L$ to $1-5a_0/\sqrt G$. The zero-free bounds and Page uniqueness of [Montgomery--Vaughan, Chapter 11, Theorems 11.3--11.4 and Corollary 11.10](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/primes-in-arithmetic-progressions-ii/E570686BE17580FCF058DE38AF6F3CAF) apply since all primitive conductors are at most $Q_0$ and $\log Q_0=o(\sqrt G)$. The one real zero is at least $a_0/\sqrt G$ from the new vertical line. Theorem 11.4, including its near-exception bound (11.10), bounds all reciprocal functions by $G^{O(1)}$ on the three shifted sides, and also gives $|1/L'(\beta,\chi)|\ll1$ by taking the derivative at the simple zero in that bound. Finite Euler corrections do not change the contour bound: for any $v\le Y^{C'}$ and $\sigma\ge1-5a_0/\sqrt G$, one has $\sum_{p\mid v}p^{-\sigma}=O(\log G)$, by summing over all integers $2\le p\le G^2$ and using at most $O(G)$ prime factors for $p>G^2$. Thus their reciprocal products are $G^{O(1)}$. The same checks apply to all imprimitive products after deleting their finite Euler factors.

The truncated Perron estimate for coefficients of magnitude at most one is the [half-integer argument in R85](r85-spectral-unconditional-planted-ap-good-dyads.md#1-good-dyads-are-unconditional), also the unmasked reciprocal contour of Montgomery--Vaughan, Chapter 11, Exercise 11.3.7. After reduction, $X/g\ge Y^{1/5}$ for large $Y$ because $g\le Q_0$. The two horizontal errors and truncation are at most a polynomial in $G$ times $(X/g)e^{-\sqrt G}$, and the vertical bound gives a fixed stretched exponential. Returning the half-integer endpoint to the real endpoint changes the pole term by at most $G^{O(1)}(X/g)^{\beta-1}$, harmless here. The reduced-class orthogonality averages bounded errors, and $|\mu(g)\chi(g)|\le1$. This proves (6) with the stated absolute prefactor, including arbitrary sharp differences of such prefixes. Its real density is $B(w;q,b)x^{\beta-1}/L'(\beta,\chi)$, with no remaining factor of $\beta$.

## 2. Apply it to both genuine long labels

By the [hard transfer](r88-spectral-hard-exceptional-residue-transfer.md) and the long unsigned deletion, $\mathfrak E_\pm$ is the half signed combination of the two genuine hard functionals $\mathcal H(A_i^{\rm ss})$, with error $O_A(Y^\beta G^{-A})$ here. Indeed the error of the hard transfer has that stronger normalization, and the two terms in (2) of the deletion proof also do, by $r_{\rm odd}\ge r/8$ and classical Siegel's $r>G^J$ for each fixed $J$ at this Page choice.

Under $r\mid N$, $\chi(N-m)=\chi(-1)\chi(m)$ exactly; nonunits satisfy the same identity with zero values. Fix the two genuine short labels $(u,v)$, let $h=uv$, and take $(h,r)=1$ since all other terms vanish. Denote the two signed variables by $(b_1,b_2)$, in the order $(b,c)$ or $(a,d)$ in the respective color. The exact identity $c_t(n)=\sum_{q\mid(t,n)}q\mu(t/q)$ gives the summed congruence $h b_1b_2\equiv N\bmod q$ for each pair $t,q$. Expand their mutual coprimality by $\sum_{k\mid(b_1,b_2)}\mu(k)$ and put $b_1=kz_1,\ b_2=kz_2$. Because each long leg already carries $\mu\chi$, we discard $(k,hr)>1$ and restrict to squarefree $k$. The product of the two original signs and characters then becomes

$$
     \mu(z_1)\chi(z_1)\mu(z_2)\chi(z_2)
                   \mathbf1_{(z_1z_2,kh)=1},
 \tag{7}
$$

since $\mu(k)^2\chi(k)^2=1$. Do not impose an extra $(z_1,z_2)=1$ after the expansion: the outer factor $\mu(k)$ imposes the original coprimality. The $q^2$ pairs of residues $b'_1,b'_2\bmod q$ are now tested exactly by $h k^2 b'_1 b'_2\equiv N\bmod q$, before using (6). This works even if a residue or $hk$ is nonunit modulo $q$.

The contribution of $k>Y^{1/100}$ before any analytic replacement is $O(Y^{\beta-1/100+o(1)})$. For each $h,k$ the absolute number of pairs is at most $(4Y/(hk^2))(1+\log(4Y))$, since $z_1z_2\le4Y/(hk^2)$. This bound uses floors without a spurious extra interval error. Sum $k^{-2}$ in the tail, sum the short labels reciprocally, and use $O(Y^{\beta-1})$ for the weight. The sum over the absolute Ramanujan weights costs only $Q_0^{O(1)}$; this power saving can afford that subpower loss.

For $k\le Y^{1/100}$ both $z_i$ on the actual support are at least $Y^{.37}$ for large $Y$, by the genuine lower bounds of the long unsigned deletion. The same is true for the real admissible interiors by the same lower gate inequalities. With one variable fixed, the other lies in at most two intervals at size comparable to $Y/(hk^2 z_{\rm fixed})$, since $x=h k^2 z_1z_2$ is in the true physical interval $N-I$. The assertions about the interval union and bounded variation are those verified in the deletion proof, now on the genuinely signed legs after dividing by $k$. For clarity, each basic product test is affine in the remaining variable or constant after fixing the other; each branch of the one minimum upper gate becomes one interval after squaring. The hard half-open condition on $n=N-x$ gives an interval with its literal endpoints. The centered logarithmic weight is bounded and monotone in the single variable, and composition of $\omega$ with the affine $n$ preserves its pointwise-BV norm. Thus partial summation of (6) costs $O(Y^{\beta-1})$ on each branch. It applies to arbitrary endpoints, including the degenerate one-point changes by the same error bound.

Use (6) in $z_2$ first on the actual fixed $z_1$ slices. Its error at this first step, summed in $z_1$, is at most
$Y^\beta G^{O(1)}e^{-c\sqrt G}/(hk^2)$ per residue pair, by a reciprocal harmonic sum. For the second step **interchange the finite first sum and the real $z_2$ integral**, then use (6) in $z_1$ at each fixed real $z_2$. The literal remaining slices have the same interval and variation properties. In this error the other pole density is $O(G^{O(1)}z_2^{\beta-1})$ by (5), so the remaining real integral costs at most $\int_1^{4Y}z_2^{\beta-2}dz_2\ll G$. No variation of an integrated moving boundary needs to be assumed. This gives the same second-step error. Summing $h,k,t,q$ and the $q^2$ residue choices multiplies the common stretched-exponential bound by at most $G^{O(1)}Q_0^{O(1)}$ beyond the displayed reciprocals, so the total is $O_A(Y^\beta G^{-A})$.

To read the model, its local factor is

$$
 \mathcal C(h,k;q,N)=
    \sum_{\substack{b'_1,b'_2\bmod q\\
                         hk^2 b'_1 b'_2\equiv N\ (q)}}
                         B(kh;q,b'_1)B(kh;q,b'_2).
 \tag{8}
$$

The real density of the two independent variables is
$L'(\beta,\chi)^{-2}(z_1z_2)^{\beta-1}dz_1dz_2$ times (8). Restoring the original variables $b_1,b_2$ gives the factor $k^{-2\beta}$. Making $x=h b_1b_2$ the physical variable gives
$(b_1b_2)^{\beta-1}db_1db_2=h^{-\beta}x^{\beta-1}dx\,d\log b_1$.
The hard left factor $(N-x)^{\beta-1}\omega(N-x)$ remains literal. Thus the real log integral of the centered weight in (2) is what remains from the physical geometry; the analytic normalization has two poles, with denominator $L'(\beta,\chi)^2$.

## 3. Evaluate the local completion without completing the Ramanujan sum

We may extend the model $k$ sum to all squarefree $k$ with $(k,hr)=1$. Its new tail is negligible: the factors from primes of $hq$ in (5) are $G^{O(1)}$ by the previous finite-product bound at $\beta$, while extra factors from $k$ are $O_\eta(k^\eta)$ for any fixed $\eta>0$, since $\beta\ge .99$ for large $Y$. This last inequality follows by absorbing finitely many primes into a constant and bounding each large Euler factor by $p^\eta$. The $q^2$ choices in (8) and outer Ramanujan weights cost only $Q_0^{O(1)}$. Consequently $\sum_{k>Y^{1/100}}k^{-2\beta+2\eta}\ll Y^{-c_1}$ for some fixed $c_1>0$ and small fixed $\eta$. The real integrals before summing the short labels are $O(Y^{2\beta-1}G^{O(1)})$, since both $x$ and $N-x$ are comparable to $Y$ and the log volumes and centered factor are bounded by fixed powers of $G$. The short reciprocal sum is at most $O(G^2Y^{(1-\beta)/5})$ because both short labels are at most $Y^{1/10}$. In particular $Y^{2\beta-1+(1-\beta)/5}\le Y^\beta$. This proves the needed tail estimate with the same $Y^\beta$ normalization.

The absolutely convergent local product of
$\sum_{(k,hr)=1}\mu(k)k^{-2\beta}\mathcal C(h,k;q,N)$
is exactly (1). To check the factors at $p\mid q$, the local mass in (5) at a nonzero residue is $E_p/(p-1)$, whether $p$ is in the mask $kh$ or not. At zero the mass is $-c_pE_p$ if $p\nmid kh$, and is zero if $p\mid kh$. Thus for $p\mid kh$ only units are present and the congruence either keeps all of them, if $p\mid N$, or none. For $p\nmid kh$, the nonzero-product congruence gives $E_p^2/(p-1)$ when $p\nmid N$. When $p\mid N$, the condition is that at least one residue is zero and its mass is $E_p^2(c_p^2-2c_p)$. If $p\nmid h$ the term from occupying $k$ at this prime subtracts $p^{-2\beta}E_p^2\mathbf1_{p\mid N}$; as $(p,r)=1$, it cancels the $c_p^2$ part exactly. At a prime outside $q$, its only effect when occupied by $h$ or $k$ is $E_p^2$; summing the two $k$ choices gives the first factor of (1). These checks give all the stated cases, without using any approximation of the $t$ cutoff or replacing the original Ramanujan factor by an infinite singular series.

## 4. Evaluate the two real geometries and preserve the signs

All the local and short prefactors other than the real mark depend on the two short labels only through their product $h$. Thus their ordered sum may be symmetrized in those labels. The local formula is also symmetric in the two long residues and the two long pole measures, allowing a long-leg swap whenever its literal domain is symmetric.

For $i=0$ the short labels are $(a,d)$. The condition $abc>H_0$ is automatic on this domain, since $abc=x/d\gg Y^{9/10}$. Put $s=\log(a/d)$. At fixed $x,a,d$ the interval in $\log b$ where both $b,c>D/a$ has length $(T_x+s)_+$. Removing the domain where both $b,c\ge\sqrt x/a$ subtracts $s_+$, wholly contained in the first interval as $D<\sqrt x$. This implements the **one minimum** upper gate, not two upper restrictions. The remaining length is $J_x(s)=(T_x+s)_+-s_+$. Averaging the centered mark over the two symmetric long variables $b,c$ makes it $-\log(a/d)/\log x=-s/\log x$ by $abcd=x$. Averaging next under swapping the short labels $a,d$ gives $-\frac{s}{2\log x}(J_x(s)-J_x(-s))=-\rho\min(T_x,\rho)/(2\log x)$. This proves $\mathcal G_0$, with its minus sign.

For $i=1$ the short labels are $(b,c)$. The two signed long labels are $a,d$. At fixed $x,b,c$ the true gates give the interval

$$
   \max(D/\min(b,c),\,H_0/(bc))<a<\sqrt x/\min(b,c).
 \tag{9}
$$

Its logarithmic width is exactly $W_x(b,c)$ in (2). Put $s=\frac12\log x-\log\min(b,c)-\log a$ so that $0<s<W_x$. The centered mark is $2(s+\log\min(b,c)-\log c)/\log x$. Its integral is
$(W_x^2+2W_x(\log\min(b,c)-\log c))/\log x$.
Averaging under swapping $b,c$ gives $\mathcal G_1$, since
$2\log\min(b,c)-\log b-\log c=-|\log(b/c)|$.
Only the continuum measure loses individual equality points; the original discrete inequalities were used at the progression step.

Finally the two exact single-pole replacements, the absolute $k$ completion and the real kernels prove $\mathcal H(A_i^{\rm ss})=\mathcal D_i+O_A(Y^\beta G^{-A})$. The character factor $\chi(-1)$ and the negative prefactor in (3) both come from the hard left functional, before the distinct parity half-sum in (4). This proves the assertion. The remaining colored short sums with (1)--(2) may have cancellation, but neither the pole replacement nor the displayed local cancellation proves that they are small.
