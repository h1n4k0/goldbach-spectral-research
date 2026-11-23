# Prime-weighted odd saddle cancellation on an actual marked major branch

**Scope.** We turn the prime-free cofactor cancellation into a bound for a **genuine prime-weighted major integral** on a marked branch. This branch does not require the marked prime $p$ to be the largest prime of $m=kp$. It counts each eligible $p$ as a tag, so a partner with two eligible marks can occur twice. The result is conditional on the historical prime-character Dirichlet GRH input on the original major arcs. It is **not** a bound for the genuine minor, the full prime correlation, the largest-prime ordered branch, or weak S.

Fix $B>B_0>0$, $0<\sigma_1<\sigma_2<1/10$, and a fixed squarefree even integer $\mathcal R$. Let $N\to\infty$ through even integers with $\operatorname{rad}(N)=\mathcal R$; for example $N=2^v$ is permitted. Put $L=\log N$, $L_2=1+\log L$, $U=\sqrt L$, $G=e^U$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, and $V=[N/3,2N]$. For $k$ integer write $j(k)=\#\{p\mid k:p\ {\rm prime},\ p\le G\}$, and set

$$
 \mathcal S_N=\left\{k:\ \mu(k)=+1,\ 
       |j(k)-2\log U|<12\sqrt{\log U\,\log L_2}\right\}.
$$

Use the genuine above-BV mixed coefficient $M_>(m)$ on the squarefree partner $m$. Define the actual marked right polynomial

$$
 A_{\rm tag}(\theta)=
  \sum_{\substack{D N^{\sigma_1}<k\le D N^{\sigma_2}\\ k\in\mathcal S_N}}
   \ \sum_{\substack{p\ {\rm prime},\ p\nmid k\\kp\in V}}
           M_>(kp)e(kp\theta).
 \tag{1}
$$

In this range each $p$ exceeds $G$ for large $N$, so the tagged product has odd total Möbius parity and the same small-prime count as $k$. At most two different $p$'s can be eligible for any $m$, since $p\gg N^{1/2-\sigma_2} L^B$. The summation does not impose any ordering between $p$ and the prime factors of $k$.

Let $P_{I,\omega}$ be the actual left prime polynomial on the hard central interval $I$ with the bounded-variation weight $\omega$ of the [pointwise major bridge](r64-spectral-pointwise-major-central-bridge.md). Let $\mathfrak M$ be the original major arcs, $q\le Q=N^{1/1000}$, $|\nu|\le2Q/N$. Then

$$
 \left|\int_{\mathfrak M} P_{I,\omega}(\theta) A_{\rm tag}(\theta)
                   e(-N\theta)\,d\theta\right|
       \le o(1)\,\frac{\Sigma(N)|I|}{L}
                         + O(N^{1-10^{-4}}).
 \tag{2}
$$

The $o(1)$ is uniform in $I$ and in the bounded family of weights as before. The result is $o(\Sigma(N))$ in the $L/N$ normalization. In particular the actual prime-weighted tag branch has no large completed major term at the odd saddle; its actual full or minor integral is not estimated here.

## 1. The weighted cofactor calculation at fixed real $x$

For a prime $\ell$ define

$$
 r_\ell=\begin{cases}0,&\ell\mid\mathcal R,\\
                  (\ell-1)/(\ell-2),&\ell\nmid\mathcal R,\end{cases}
 \qquad r(k)=\prod_{\ell\mid k}r_\ell\quad(k\ {\rm squarefree}).
 \tag{3}
$$

There is no denominator at 2 since $2\mid\mathcal R$. This is exactly the non-singular-series part of the completed $S(N,k)$ in [the genuine prime major formula](r66-spectral-above-bv-strip-deletions.md#3-the-same-upper-scale-for-the-actual-giant-major-arcs). We prove the following weighted extension of the [prime-free cofactor calculation](r72-spectral-cofactor-saddle-cancellation.md). Neither the outer $p$ nor $N-x$ is being counted in this intermediate claim.

Uniformly for $x\in V$ and $\sigma_1\le s\le\sigma_2$, with $h=\log(x/D^2)$ and the exact $X_k(x),Y_k(x)$ of the cofactor calculation, one has

$$
 \sum_{\substack{D<k\le D N^s\\ k\in\mathcal S_N}}
       \frac{r(k)}k X_k(x)
  =s(h\mathcal C_r-1)+o(1),\qquad
 \sum_{\substack{D<k\le D N^s\\ k\in\mathcal S_N}}
       \frac{r(k)}k Y_k(x)
  =s(h\mathcal C_r-1)+o(1).
 \tag{4}
$$

The two potentially large terms therefore cancel before the prime weights are compared. We give all changes to that calculation caused by (3).

**Sharp trace and transform.** The preceding parity trace writes an integer $k=bv$ with $b$ the exact squarefree product of its primes at most $G$ and $v$ strictly $G$-rough. For counts at most $32\log U$ one has $b=N^{o(1)}$. Since the primes of $\mathcal R$ are fixed, all are eventually $\le G$, and $r(v)=1+O((L/U)e^{-U})$ uniformly on these rough cofactors. Thus the reciprocal parity trace on $v$, including the squarefree floors and signed masked Mertens correction, does not change. Insert $r(b)/b$ in the external $b$ sum. In bounding the tiny error from $r(v)-1$, the crude $|X_k|\ll\tau_4(k)$ and the usual positive harmonic product cost only powers of $L$. The weighted harmonic sum over the $b$ labels remains $O_{\mathcal R}(U)$, since $r_\ell=1+O(1/\ell)$ away from the fixed excluded primes. The ordinary extreme count bound still applies with $r(k)\ll k/\varphi(k)$.

For the harmonic Euler transform this only replaces the factor $1+|1-e^{-i\xi\log\ell}|^2/\ell$ of the signed $b$-generator by $1+r_\ell |1-e^{-i\xi\log\ell}|^2/\ell$. Uniformly in $\xi$ the exponent difference in its positive generating bound is $O_{\mathcal R}(1)$, by the convergent $\sum_{\ell\nmid\mathcal R}|r_\ell-1|/\ell$ and the finitely many omitted primes. Hence the hard endpoint error and both the $z=1$ and $z=2$ signed square estimates are unchanged up to constants. Removing $j>32\log U$ before applying the parity trace and reinstating it only in the positive Fourier generator costs $o(1)$, as previously. The external rough harmonic factor is still $s L V_G(1+O(L^{-1/5}))$, $V_G=\prod_{\ell\le G}(1-1/\ell)$, because the rough variable is not weighted in the limit.

The resulting product for the whole signed Euler integral is thus

$$
 F_r(\xi)=\prod_{\ell}
      \frac{(1-1/\ell)^2
           \{1+r_\ell(2-2\cos(\xi\log\ell))/\ell\}}
           {|1-\ell^{-1-i\xi}|^2}.
 \tag{5}
$$

Away from $\mathcal R$ the factors and their derivatives have the same uniform $1+O(\ell^{-2})$ and $O((\log\ell)/\ell^2)$ bounds as in the unweighted case, and the finitely many other factors are fixed smooth positive functions. Consequently the function $J_r(\xi)=|\widehat R(\xi)|^2F_r(\xi)$, for ordinary reciprocal Mertens primitive $R$, is in $W^{1,1}$ and is Lipschitz near zero. The same sharp multiplier is $h|1+e^{-ih\xi}|^2-4\sin(h\xi)/\xi$. Its cosine correction is $o(1)$ after multiplication by $h$ by integration by parts, and its sine kernel tends to $\pi J_r(0)$. Since $F_r(0)=1=\widehat R(0)$, the latter gives $-s$ after the parity and transform factors. Thus the sharp asymptotic in (4) before the count restriction holds with

$$
 \mathcal C_r=(2\pi)^{-1}\int_{\mathbb R}|\widehat R(\xi)|^2 F_r(\xi)\,d\xi.
 \tag{6}
$$

All endpoint and rough-factor truncations in that proof were uniform in its upper cofactor exponent in a compact subinterval of $(0,1/10)$: the rough $e$-cutoff still has terminal buffer $L^{3/4}$, the comparison range starts at $k=D$, and the worst squarefree-pair floor $N^{-1/4+3\sigma_2/2+o(1)}$ still saves a power. Enlarging the fixed real $x$ interval to $V$ does not change the inequalities $h=2B\log L+O(1)$, $x/k\gg N^{1/2-\sigma_2}L^B$, or the geometric error bounds.

**The actual low two-factor average with weight $r(uv)$.** In each branch of $Y_k$ write $k=uv$ in its true two complementary cofactor factors, with $u=N^{1/2+o(1)}$ the large factor and $v\le D N^s/u$. As in the prior proof, the short labels $a,b$ force the squarefree product $ab$ to divide the designated factor, and the parity $\mu(uv)=+1$ is exact. The small range $v\le v_0=\exp(L^{4/5})$ is negligible even after multiplication by $r(k)\ll L_2$. For the rest, the local squarefree factor probabilities at each prime remain those for the three allowed occupations $(0,0),(1,0),(0,1)$, but the latter two now receive $r_\ell$. Thus the unsigned density and ratio for a forced label are

$$
 K_r=\prod_\ell (1-1/\ell)^2(1+2r_\ell/\ell),
 \qquad \alpha_\ell=\frac{r_\ell}{\ell+2r_\ell}.
 \tag{7}
$$

Here $K_r>0$ for fixed $\mathcal R$ and $\alpha_\ell=0$ on its primes. The weighted signed parity term is negligible.

For rigor in this last comparison, the positive cofactor weight can be truncated to its primes $\ell\le L^{C_0}$ in the low two-factor count. Uniformly for $k\le N$ the omitted product differs from 1 by $O(L^{1-C_0})$. Take $C_0$ sufficiently large in terms of $B$ and the desired power-log saving. The fixed excluded primes are imposed as unit conditions in both factors. At other small primes expand the weight into products of $(r_\ell-1)\mathbf1_{\ell\mid uv}$. Truncate this positive expansion at degree $\lceil L_2^2\rceil$: since $\sum_{\ell\le L^{C_0},\,\ell\nmid\mathcal R}(r_\ell-1)=O(\log L_2)$, its tail is $O_A(L^{-A})$, even uniformly on all small-prime residue pairs. This uniform statement holds because the expansion uses nonnegative coefficients and can be bounded by the one with all occupancies present. In the unsigned squarefree count combine the retained expansion with the same upper and lower Bonferroni on forbidden square/collision events at these primes, and impose the forced label conditions. The number of joint terms, their moduli and residue counts remain $\exp(O(L_2^3))$. The same reciprocal count on a residue class in $v$ keeps its exact endpoint $D N^s/u$; then partial summation in $u$ keeps the hard label limits. Large-prime square/collision tails may be bounded without constraints as in the preceding proof, paying only an additional $O(L_2)$ from the positive truncated weight. These steps give (7) in the main term, including overlaps between a weighted occupation and a forced label, because the conditions are imposed on the same local residue-pair set.

For the parity difference expand the same truncated occupation weights before summing $\mu(uv)$. Fix $u$; any imposed occupancy $\ell\mid uv$ not already in $u$ forces $\ell\mid v$, while those already in $u$ cause no additional restriction beyond coprimality. Together with any label forced in $v$ the prescribed product is at most $\exp(O(L_2^3))$. Factor it from $v$ on the nonzero Möbius support and include its primes, and those of $u$, in the ordinary coprimality mask. The lower endpoint remains $\ge\exp(\tfrac12 L^{4/5})$, so the same masked ordinary Mertens argument and its $\exp(-cL^{3/10})$ saving dominate all retained terms. This proves the weighted parity factor $1/2$ and all the required uniform errors without a Möbius progression hypothesis.

To finish the low main, the complementary branches still add the two real log lengths to the same constant $\log((DN^s)^2/(xv_0^2))$ after changing $u$ to the common low-LCM variable. The short signed-label integrals are the same $H_\alpha,D_\alpha$ as in the preceding calculation, now using (7). The positive convolution argument for their absolute first moment and their constant integral applies: $0\le\alpha_\ell\le1/\ell$, $1/\ell-\alpha_\ell=O(\ell^{-2})$ away from the finite $\mathcal R$, and the finitely omitted primes add only fixed positive mask factors. All tails at $(B-B_0)\log L$ and the prefactor error $O(L^{-1/5})$ still cost $o(1)$ after the factor $h$.

Finally their Euler identities match the same (5) and its same zero-frequency constant. For $t=\xi\log\ell$, the local numerator is

$$
 (1-1/\ell)^2(1+2r_\ell/\ell)
                 \bigl(|1-\alpha_\ell e^{-it}|^2-\alpha_\ell^2\bigr)
   =(1-1/\ell)^2\{1+r_\ell(2-2\cos t)/\ell\}.
$$

At zero, $(1+2r_\ell/\ell)(1-2\alpha_\ell)=1$. The first identity gives the $\mathcal C_r$ term for $K_r\int H_\alpha$, and the second gives $K_r\int D_\alpha=-1$ by the same exact integrated primitive relation. This proves the low asymptotic in (4) without the moving count restriction.

For both asymptotics the moving count can now be imposed, as before. The [moving odd reciprocal bound](r72-spectral-moving-odd-weighted-saddle.md) before any prime comparison gives a total $o(1)$ positive reciprocal envelope outside $\mathcal S_N$ for either the sharp or the low expression, with weight $k/\varphi(k)$. Here $r(k)\ll k/\varphi(k)$ and the cofactor range is smaller than the range used for the local floors. The envelopes use the exact real cutoffs in $X_k,Y_k$, not primality or order of the formal distinguished factor. This proves (4) on the masked range.

## 2. From the weighted cofactor cancellation to the marked major integral

For each real $x\in V$, the needed actual completed density is

$$
 \Sigma(N)
 \sum_{\substack{D N^{\sigma_1}<k\le D N^{\sigma_2}\\ k\in\mathcal S_N}}
          \frac{r(k)\{X_k(x)-Y_k(x)\}}{k\log(x/k)}.
 \tag{8}
$$

Indeed by (4) the partial sums of the numerator divided by $k$, with upper endpoint $D N^s$ and $\sigma_1\le s\le\sigma_2$, are uniformly $o(1)$. The reciprocal logarithm $1/\log(x/k)$ has sup plus variation $O(1/L)$ as a function of $k$ on this interval. Ordinary partial summation over $k$, with the two true cofactor endpoints retained, therefore bounds (8) by $o(\Sigma(N)/L)$ uniformly in $x$. This step does not replace the varying reciprocal prime density by a fixed value.

We justify that (8) is the completed density of the original arcs for (1). For every fixed $k$, the real coefficient $X_k(x)-Y_k(x)$, extended by zero outside $V$, has sup plus variation $O(\tau_4(k))$: each sharp term comes from the original divisor gates and centered log weight, or the two low folds, with their actual log inequalities, as in the [lower-largest-prime transfer](r70-spectral-lowest-largest-prime-transfer.md). Its use here does not need $p>P^+(k)$, only that the distinguished prime $p$ exceeds $G$ and all short labels, and does not divide $k$. For each excluded prime $p\mid k$, restoring the formal term for this progression comparison costs $O(\tau_4(k))$; their total across $k$ is $O_\epsilon(N^{1/2+\sigma_2+\epsilon})$, a power-small error in the major integral. For the genuine remaining tags the identity $M_>(kp)=X_k(kp)-Y_k(kp)$ holds by the actual composite squarefree odd formulas, with its exact endpoints.

At $q\le Q$ every tagged prime exceeds $Q$. Applying the ordinary historical prime-progression GRH estimate at fixed $k$ with the bounded-variation coefficient and the slow phase gives the same principal real density contribution

$$
 \frac{c_q(k)}{\varphi(q)}\,
       \frac{X_k(x)-Y_k(x)}{k\log(x/k)} .
$$

The right pointwise error is $O_\epsilon(Q^2N^{3/4+\sigma_2/2+\epsilon})$ after summing $\sqrt{N/k}$ over the exact range and absorbing the divisor bound. It is power-small after multiplying by the left polynomial and the original total arc length, since $\sigma_2<1/10$; the left error times the actual right is likewise power-small (tag multiplicity at most two). The right occupation bound $O(L^4 C^{\omega(q)}/q)$ in sup and variation is unchanged: the proof sums over $k\le N$ with $O(\tau_4(k))$ variation and $\log(x/k)\gg L$, irrespective of the tag's largest-prime ordering. The same original-$Q$ Fourier and Ramanujan completion bounds therefore give $O(N^{1-10^{-4}})$ error, as in the lower-largest-prime transfer, and the completed local factor is exactly $\Sigma(N)r(k)$. This is (8). Integrate it against the original hard left test on $I$ to obtain (2). All prime input in this section concerns only the genuine major comparison; no estimates on the actual minor or on the unordered-tag multiplicity difference are implicit.
