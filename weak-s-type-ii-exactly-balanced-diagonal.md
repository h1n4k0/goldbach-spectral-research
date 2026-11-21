# A limitation of absolute-value and Cauchy bounds in one exactly balanced Type II box

**Scope.** For $N=2^j$, this proves that taking absolute values or applying the stated $(d,v)$-Cauchy step on the specified central box cannot give a saving, even after the principal subtraction described below. It is not a lower bound for the signed Type II sum or the Hardy operator, and it does not refute weak S.

For every sufficiently large $N=2^j$, put $X=\sqrt N$, $L=\log N$, and take the fixed physical boxes

$$
 I=[.740X,.745X],\qquad J=[.715X,.720X],\qquad D=[.445X,.450X].
$$

Restrict $d$ to the odd squarefree integers in $D$, $v$ to the odd integers in $J$, and keep

$$
 b_{\rm II}(v)=\sum_{r\mid v,\ r>N^{.2499}}\Lambda(r).
$$

The actual central Type II summand here is $\mu(d)b_{\rm II}(v)$ times

$$
 F(d,v)=\sum_{\substack{u\in I,\ u\ {\rm odd}\\ uv\equiv N\bmod d}}
              \mu(u)\mu^2(N-uv). \tag{1}
$$

Indeed $N/2<uv<9N/16$ on the entire box, $(uv,N)=1$ exactly means odd $u,v$, and $k=(N-uv)/d>X$ for any solution. Thus $t=X,\ y=9N/16$ are valid sharp cutoffs; $d>N^{.4975}$ and $u,v\asymp X$ put this exact box in the remaining central sector of the [preceding near-balanced deletion](weak-s-type-ii-wright-near-balanced.md). The exclusion of even or nonsquarefree $d$ discards only zero or inadmissible summands.

**Proposition.** The following estimates hold unconditionally:

$$
 \sum_{d,v} b_{\rm II}(v)|F(d,v)|\asymp NL,\qquad
 \sum_{d,v}\left(\frac{b_{\rm II}(v)}{L}\right)^2 |F(d,v)|^2\asymp N. \tag{2}
$$

The same orders hold with the twist $\omega_\tau(u)=(X/u)^{1+i\tau}$ inserted in (1), uniformly for every real $\tau$. Under **global Dirichlet GRH**, the second estimate still holds uniformly for $|\tau|\le N^4$ when the usual individual-modulus principal parts are subtracted after squarefree completion of $\mu^2(N-uv)$ at $B=N^{10^{-6}}$, in the precise formulation of §3 below.

This is a lower bound for the diagonal absolute-mass/variance quantities of a particular Cauchy reduction, not for the signed sum. It gives no lower bound on the operator or any obstruction to weak S itself.

## 1. Exact support and a squarefree counting lemma

For an admissible $(d,v)$, if $(d,v)>1$ there is no solution since $(d,N)=1$. Otherwise $u$ has at most one choice in $I$, because $|I|<d$. Hence the absolute value of (1) is precisely the indicator of an admissible incidence with squarefree $u$ and squarefree $N-uv$, and after inserting the twist it is that indicator times $|\omega_\tau(u)|\asymp1$. The trivial upper bounds in (2) follow from this and $0\le b_{\rm II}(v)\le L$.

For the lower bounds take the prime set

$$
 \mathcal P=\{p\text{ prime}: N^{.24993}\le p\le N^{.24997}\}.
$$

Every $v\in J$ is divisible by at most two distinct such primes. If there is at least one then $b_{\rm II}(v)\ge .24993L$. It therefore suffices to prove $\mathcal A\gg N$, where

$$
 \mathcal A=\sum_{p\in\mathcal P}\sum_{\substack{d\in D\\d\ {\rm odd},\ \mu^2(d)=1}}
 \sum_{\substack{u\in I,\ v\in J\\u,v\ {\rm odd},\ p\mid v\\uv\equiv N\bmod d}}
                \mu^2(u)\mu^2(N-uv).
 \tag{3}
$$

Expanding the squarefree indicators in $\mathcal A$, truncate both sums at $B=N^\sigma$, $\sigma=10^{-6}$. For $m=N-uv$, all omitted-square errors are supported where $u$ or $m$ is divisible by a square of an integer $>B$, and their pointwise absolute value is at most $2\tau(u)\tau(m)$. There are $O(X/B)$ such $u\le X$; summing over all $v\le X$, and using the at most $\tau(m)$ choices of $d$ and at most two of $p$, the $u$-error is $O_\epsilon(N^{1+\epsilon}/B)$. The $m$-error has the same bound since the support has $O(N/B)$ choices of $m$, at most $\tau(N-m)$ choices of $u,v$, at most $\tau(m)$ choices of $d$, and at most two of $p$. These are exact integer bounds using $\sum_{c>B}c^{-2}\ll B^{-1}$; no distribution assumption enters.

Write the two square divisors as $a^2\mid u$ and $b^2\mid m$. Here $a,b$ are odd. Put $q=[d,b^2]$, odd, so $uv\equiv N\bmod q$. If $(ap,q)>1$, there is no solution, and in all other cases set $u=a^2w,\ v=pz$, with $w,z$ odd in $I/a^2,\ J/p$, and $wz\equiv N\overline{a^2p}\bmod q$.

For completeness the count on these two intervals is

$$
 \frac{\varphi(q)}{q^2}\,\frac{|I||J|}{4a^2p}
       +O_\epsilon(q^{1/2+\epsilon}). \tag{4}
$$

Both scaled interval lengths are $O(q)$. Fourier-expand their odd-integer indicators as multisets modulo $q$: since $q$ is odd, writing $w=2w_0+1,z=2z_0+1$ turns each Fourier coefficient into an interval progression sum with frequency scaled by $2\bmod q$. In the reduced inverse graph the complete Kloosterman coefficient has the bound

$$
 |S(h,kA;q)|\le \tau(q)\sqrt q\,(h,k,q)^{1/2},\qquad (A,q)=1,
$$

as in [Iwaniec–Kowalski, Corollary 11.12](https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf). The normalized Fourier coefficients are $O((1+|h'|)^{-1})$, with $h'$ the centered representative of $2h\bmod q$ (and similarly for $k'$); multiplication by 2 preserves divisibility by every divisor of odd $q$. Away from $(0,0)$, use $(h,k,q)^{1/2}\le\sum_{s\mid(h,k,q)}\sqrt s$. The coefficient sum over nonzero multiples of $s$ is $O(\log(2q)/s)$. Thus the sum over both nonzero frequencies is at most $O(\log^2(2q)\sum_{s\mid q}s^{-3/2})$ and over one zero frequency at most $O(\log(2q)\sum_{s\mid q}s^{-1/2})$. Both are $O_\epsilon(q^\epsilon)$. The zero-frequency counts are $|I|/(2a^2)+O(1), |J|/(2p)+O(1)$, whose rounding costs $O(1)$ in (4). This proves (4) including composite $q$, arbitrary interval offsets, and the parity constraint.

Here $q\ll XB^2$ and there are $O(X B^2 N^{.24997})$ quadruples $(d,a,b,p)$. Therefore the aggregate error in (4) is

$$
 O_\epsilon(N^{.99997+3\sigma+\epsilon})=o(N).
 \tag{5}
$$

The main term in $\mathcal A$ is consequently $(|I||J|/4)$ times the sum over $d,p$ of $p^{-1}$ times the truncated coefficients in the following display.

## 2. The positive local factors

We may extend the main square-completion variables $a,b$ to infinity:

$$
 D_{d,p}=
 \sum_{\substack{a,b\ {\rm odd}\\(ap,[d,b^2])=1}}
   \frac{\mu(a)\mu(b)}{a^2}\frac{\varphi([d,b^2])}{[d,b^2]^2}.
$$

The extension for each $d,p$ costs $O_\epsilon(N^\epsilon/(d\sqrt B))$. To verify it, bound $\varphi([d,b^2])/[d,b^2]^2\le 1/[d,b^2]$, and use the factors $a^{1/2}/\sqrt B$ or $b^{1/2}/\sqrt B$ for each tail. For squarefree $b,d$ the local multiplier of $1/[d,b^2]$ relative to $1/d$, when a prime $\ell\mid b$, is $1/\ell$ for $\ell\mid d$ and $1/\ell^2$ otherwise. The weighted local product for the $b$-tail is bounded by $O_\epsilon(N^\epsilon)$, because $\prod_{\ell\mid d}(1+\ell^{-1/2})\ll_\epsilon d^\epsilon$ and $\prod_\ell(1+\ell^{-3/2})<\infty$. The $a$-tail is no more costly. Summing this error against $p^{-1}$ and $d^{-1}$, then multiplying by $|I||J|/4$, gives $o(N)$, with a sufficiently small fixed $\epsilon>0$.

If $p\mid d$ there is no main term. Otherwise direct local enumeration gives

$$
 D_{d,p}=
 \frac{\varphi(d)}{d^2}\prod_{\ell\mid d}(1-\ell^{-1})\,
 (1-p^{-2})\prod_{\substack{\ell\ge3\ {\rm prime}\\\ell\nmid dp}}
           (1-2\ell^{-2}+\ell^{-3})
 \gg \frac1d\left(\frac{\varphi(d)}d\right)^2. \tag{6}
$$

For $\ell\mid d$, $a$ cannot contain $\ell$ and adding it to $b$ changes the local $\varphi(q)/q^2$ by a relative factor $1/\ell$. For $\ell=p$, adding it to $b$ is forbidden, so the $a$-factor is $1-p^{-2}$. Otherwise the choices are neither, $a$ only, or $b$ only with local contributions $1,\ -\ell^{-2},\ -(1-1/\ell)\ell^{-2}$ respectively, since $\ell\mid b$ forbids $\ell\mid a$. All factors are positive, and the infinite product is bounded below by a positive absolute constant.

The number of odd squarefree $d\in D$ is $c_0|D|+O(\sqrt X)$ with $c_0>0$, by the elementary squarefree sieve. A positive proportion have $\varphi(d)/d\ge c_1>0$: the sum over all $d\in D$ of $\sum_{\ell\mid d,\ \ell\ {\rm prime}}\ell^{-1}$ is $O(X)$, by first counting multiples of each prime and summing $\sum_{\ell}\ell^{-2}$. Restrict to the odd squarefree $d$ for which the inner sum is at most a sufficiently large absolute constant, using Markov and $-\log(1-1/\ell)\le 2/\ell$ for odd primes. The prime number theorem by partial summation gives

$$
 \sum_{p\in\mathcal P}\frac1p\longrightarrow\log(.24997/.24993)>0.
$$

Excluding $p\mid d$ decreases this by $o(1)$ uniformly: each such $d\ll X$ has at most two prime divisors in $\mathcal P$. Hence (6), summed over $p$ and a positive proportion of the $d$ in $D$, yields a sum bounded below by a positive constant. Since $|I||J|\asymp N$, this proves $\mathcal A\gg N$ after (5) and the two tail errors. With prime multiplicity at most two, this proves (2).

## 3. The principal parts do not remove this variance

Let $F_\tau$ denote (1) with $\omega_\tau(u)$ inserted, and $F_{\tau,B}$ the same with the squarefree completion in $m=N-uv$ truncated at $b\le B$. Equivalently, with $q_b=[d,b^2]$,

$$
 F_{\tau,B}(d,v)=
  \sum_{\substack{b\le B,\ b\ {\rm odd}\\(q_b,v)=1}}\mu(b)
  \sum_{\substack{u\in I,\ u\ {\rm odd}\\u\equiv N\bar v\bmod q_b}}
            \mu(u)\omega_\tau(u).
$$

The usual principal subtraction in each reduced progression is

$$
 P_{\tau,B}(d,v)=
 \sum_{\substack{b\le B,\ b\ {\rm odd}\\(q_b,v)=1}}\frac{\mu(b)}{\varphi(q_b)}
     \sum_{\substack{u\in I,\ u\ {\rm odd}\\(u,q_b)=1}}\mu(u)\omega_\tau(u).
$$

Under global Dirichlet GRH, the [height-uniform twisted Möbius estimate](weak-s-type-ii-character-average.md#2-exact-perron-separation-and-an-all-character-mean-square) bounds the inner signed sums by $O_\epsilon(N^{1/4+\epsilon})$, also with the oddness restriction (the Euler factor at 2) and for the imprimitive principal characters. This is uniform for $|\tau|\le N^4$ and $q_b\le O(XB^2)$. Since $q_b\ge d\asymp X$, it follows that $P_{\tau,B}(d,v)\ll_\epsilon B N^{-1/4+\epsilon}$.

In the weighted $\ell^2$ norm $\|G\|_w^2=\sum_{d,v}(b_{\rm II}(v)/L)^2|G(d,v)|^2$, this gives
$\|P_{\tau,B}\|_w^2\ll_\epsilon N^{1/2+\epsilon}B^2=o(N)$. Moreover

$$
 \|F_\tau-F_{\tau,B}\|_w^2\ll_\epsilon N^{1+\epsilon}/B=o(N)
$$

unconditionally: for each $d,v$ there is at most one original candidate $u$, so the squared absolute error is $O(\tau(m)^2)$ on the omitted-square support, and for each such $m$ there are at most $\tau(m)\tau(N-m)$ candidates for $d,u,v$. This is as in §1, now without prime weights and with a squared divisor bound. The triangle inequality and (2) yield, uniformly as asserted,

$$
 \|F_{\tau,B}-P_{\tau,B}\|_w^2\asymp N.
$$

A $(d,v)$-Cauchy estimate for the raw correlation, with $b_{\rm II}(v)$ normalized by $L$, has a prefactor of order $\sqrt N$ on the same boxes (there are $\asymp N$ indices, even if one retains only occupied indices), and the remaining weighted variance has norm of order $\sqrt N$ instead of $o(\sqrt N)$. Likewise direct absolute values on the actual signed summands have exact order $NL$. Even a principal subtraction followed by this full diagonal variance cannot yield a saving. This is strictly about that Cauchy step; estimates keeping signed cancellation across $v$ at fixed $d$, across $d$, or across neighboring physical pieces are not ruled out.
