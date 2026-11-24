# Pointwise signed bounds on common short physical offsets

Fix a sufficiently large even $N$, and put $X=\sqrt N$, $L=\log N$. Use the actual prime boxes, unit masks and arbitrary bounded $E(u,v)$ of [the critical-prime setup](weak-s-type-ii-critical-prime-least-prime-boundaries.md). Thus the prime polynomial $P$ has exact coefficient $-E(u,v)\log v$ at $n=uv$, with the original true hard prime intervals and product gate. Write $D_m$ for the complete original signed complementary coefficient at $m=dk$ with the actual $d\ge X$, $I_d$, $k>t\ge N^{.49999}$, $N-y\le dk<N/2$, unit and squarefree requirements, and set $F_m=\rho_mD_m$ for any $|\rho_m|\le1$ chosen independently of the rational point at this target. The critical shell uses all primes $q$ in $\mathcal Q=[.8X,.9X]\cap\mathbb P$, all $a\ne0\bmod q$ and $\beta\in\mathcal B=[-1/(10N),1/(10N)]$.

Fix $\kappa>0$ and a real interval $I$ in the offset variable, of length $H$ with $N^{1/3+\kappa}\le H\le .01N$. Let $w:\mathbb Z\to\mathbb C$, $|w|\le1$, be supported in $I$. Define $\mathcal I_N[w]$ and $\mathcal C_N[w]$ by taking the exact signed full or double-centered shell pairing, expanding its two underlying integer coefficients at $n,m$, and inserting $w(n+m-N)$ in this pair expansion. The definition is after both numerator centerings for $\mathcal C_N[w]$; it does not re-center each alias or each slice separately. The signed sums over the entire shell are taken before the absolute values. With

$$
 G=\#\{h\in I\cap\mathbb Z:\ 0<|h|\le N/20,\ \exists q\in\mathcal Q,\ q\mid h\},
$$

we have unconditionally

$$
 |\mathcal I_N[w]|+|\mathcal C_N[w]|
 \ll_\kappa \mathcal V X
       \left(\frac{\sqrt{HG}}{L}+\frac{H}{L^2}\right)
   +\mathbf1_{0\in I}|w(0)|\,\frac{N\mathcal V}{L}.
 \tag{1}
$$

For a general product selector $\mathcal V=1$. If its support lies in any one actual count saddle of [the shifted saddle estimate](weak-s-type-ii-critical-prime-saddle-sparse-alias-gain.md), we may take $\mathcal V=R^{-(2\log 2-1)/2+\epsilon}$ for any fixed $\epsilon>0$, where $R=\log Z_1/\log Z_0$ in that theorem. In the saddle case the implied constant also depends on the fixed saddle parameters and $\epsilon$.

In particular $G\ll \min(H,(H+X)/L)$. Away from $h=0$, (1) is $O_\kappa(\mathcal V\sqrt N\,H/L)$, giving a pointwise power saving for any such $H\le N^{1/2-\delta}$ with fixed $\delta>0$. For $H\asymp\sqrt N\,L^b$ with $0\le b<3/2$ the nonzero part is $O_\kappa(N L^{b-3/2})=o(N)$; including zero costs an additional $O(N/L)$ and remains $o(N)$. With a true saddle and $R\asymp L^\Delta$ for fixed $\Delta>0$, the range extends to $b<3/2+\Delta(2\log 2-1)/2$ by taking $\epsilon$ small enough. These are bounds for a selected common physical offset region, not for the entire set of offsets and not a pointwise bound for the original full covariance.

## 1. Local square sum for the true shifted convolution

Define $T_{\mathrm{abs}}(M)=\sum_n|P_n F_{M-n}|$. The prime boxes are disjoint, so a product $uv$ has exactly one possible orientation and carries just one coefficient. Ordinary estimates give $\sum_n|P_n|^2\ll N$ by the two prime counts and $\sum_m|F_m|^2\ll N$ by [the signed sharp complementary energy](weak-s-type-ii-critical-prime-true-shifted-projection.md#1-the-sharp-moving-complementary-energy).

More precisely, uniformly in the integer $M$,

$$
 \sum_{\substack{n=uv\\M-n\in\operatorname{supp} F}}|P_n|^2\ll N\mathcal V^2.
 \tag{2}
$$

For the saddle case this is the true joint support estimate of the cited shifted saddle proof: there are $O((N/L^2)R^{1-2\log2+2\epsilon})$ prime pairs for which $M-uv$ is a possible saddle product, obtained by forcing actual small-prime divisors of that shifted number. We only multiply by $|P_n|^2\le L^2$. In the general case (2) is the ordinary prime energy.

After Cauchy--Schwarz at each $M$, sum the resulting squared estimate over $M\in N+I$ and interchange the remaining nonnegative sums over $m=M-n$ and the prime products. For each fixed $m$, only $uv\in N+I-m$ occur. The [short hyperbolic prime-pair sieve](weak-s-type-ii-critical-prime-short-target-logarithmic-gain.md#1-a-short-hyperbolic-strip-prime-pair-bound-in-a-residue) with modulus $1$ bounds their number by $O_\kappa(H/L^2)$, uniformly in the translation. Enlarge the interval by at most two if needed for the exact endpoints. Consequently

$$
 \sum_{M\in N+I} T_{\mathrm{abs}}(M)^2
 \ll_\kappa N\mathcal V^2 \sum_m |F_m|^2 \frac{H}{L^2}
 \ll_\kappa \frac{N^2H\mathcal V^2}{L^2}.
 \tag{3}
$$

The same individual Cauchy inequality, with no translation sum, also gives $T_{\mathrm{abs}}(N)\ll N\mathcal V$.

## 2. Exact unit and nonunit pair kernels

Let $h=n+m-N$. Before the factor $e(\beta h)$, the full per-$q$ pair kernel is $q\mathbf 1_{q\mid h}-1$. The centered kernel is zero if $q\mid m$, because the transform of this one $m$ is a constant on nonzero additive numerators and is removed. The $n$ factor always has $q\nmid n$ as its prime factors are smaller than $q$. For $q\nmid m$ and $q\nmid N$, the centered kernel is

$$
 q\mathbf 1_{q\mid h}
 -\frac{q^2}{(q-1)^2}
 +\frac{q}{q-1}
       \big(\mathbf1_{n\equiv N\pmod q}+\mathbf1_{m\equiv N\pmod q}\big).
 \tag{4}
$$

For $q\nmid m$ and $q\mid N$, it is $q\mathbf1_{q\mid h}-q/(q-1)$. To see both formulas, the centered residue vector attached to a single unit $n$ is $\mathbf1_{r=n}-(q-1)^{-1}$ on $r\ne0$ and zero at $r=0$. Pair this with the corresponding centered vector of $m$ at $N-r$ and multiply by $q$ by finite additive orthogonality. Both centered vectors have zero total mass, so their additive transforms at $a=0$ vanish and one can sum over all additive numerators for this calculation. If $q\nmid N$, the two excluded rows $0,N$ are distinct, giving $q-2$ rows for the constant-constant contribution. If $q\mid N$, all $q-1$ unit rows survive together. This derivation is valid for the actual double-centering on nonzero numerators and also retains the external phase $e(-N\beta)$.

The products fit $n\in[.5291N,.5364N]$ and $m\in[7N/16,N/2)$, so all actual $|h|<N/20$. A nonzero such $h$ is divisible by at most one critical prime, because distinct critical primes have product at least $.64N$. Each non-hit part of (4) and of the other pair kernels is $O(1)$. Summing over $q$ and integrating in $\beta$ using $|\mathcal B|=1/(5N)$ therefore bounds the two pairings on nonzero offsets by a constant times

$$
 \frac XN\sum_{\substack{h\in I,\ h\ne0\\ h\text{ has a critical prime divisor}}}
                T_{\mathrm{abs}}(N+h)
 +\frac{|\mathcal Q|}N\sum_{\substack{h\in I\\h\ne0}}T_{\mathrm{abs}}(N+h),
 \tag{5}
$$

where all actual coefficients vanish outside the preceding physical support. The hit count satisfies $G\le H+1$ and

$$
 G\le \sum_{q\in\mathcal Q}(H/q+1)\ll (H+X)/L
$$

by the prime count. Cauchy--Schwarz in (5) and (3) give the first term of (1). At $h=0$, the sum of the kernel magnitudes is $O(\sum_q q)=O(N/L)$, and the individual bound for $T_{\mathrm{abs}}(N)$ gives the final term in (1). All unit deletions and pointwise bounds here concern genuine physical pair offsets; no primality or sign assumption beyond the stated original inputs was imposed on the factors.
