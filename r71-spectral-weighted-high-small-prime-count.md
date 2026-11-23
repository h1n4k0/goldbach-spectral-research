# Weighted high small-prime counts in the genuine mixed strip

**Scope.** We control a complementary high-count region of the true squarefree above-BV mixed coefficient, with no least-prime restriction and no upper cap on the number of small primes. Keep $L=\log N$, $L_2=1+\log L$, $U=\sqrt L$, $G=\exp U$, and the actual count

$$
 j(m)=\#\{\ell\le G:\ell\ {\rm prime},\ \ell\mid m\}.
 \tag{1}
$$

Retain the true largest-prime gate $P^+(m)>N^\kappa$. The unconditional full assertion below holds for any fixed $0<\kappa<1/2$. At the unchanged $Q=N^{1/1000}$ the conditional assertion concerns the original genuine minor arcs and holds for fixed $1/250<\kappa<1/2$ under the historical Dirichlet GRH prime-character input. We treat the following count selectors:

$$
\begin{array}{c|c|c}
\text{total Möbius parity}&\text{condition on }j(m)&\mathcal B\\ \hline
\mu(m)=-1 & j(m)\ge\lceil(2+\varepsilon)\log U\rceil
        & L^{-d_\varepsilon}\\
\mu(m)=+1 & j(m)\ge\lceil(5/2)\log U\rceil
        & L^{-1/200}\\
\mu(m)=-1 & j(m)\le\lfloor(7/5)\log U\rfloor
        & L^{-1/200}
\end{array}
\qquad d_\varepsilon=\tfrac1{1000}\min(\varepsilon^2,1),
 \tag{2}
$$

where $\varepsilon>0$ is fixed. The first two rows are **upper tails of the actual weighted coefficient**, including all larger counts; they do not follow by bounding only the unweighted count of integers. The third is an optional low-count improvement. The intermediate count ranges, lower largest primes and weak S are not controlled.

More precisely, restrict the actual mixed $M_>(m)$ to $m\in V=[N/3,2N]$, (1)'s count as specified in a row of (2), and $P^+(m)>N^\kappa$, writing the result as $A(m)$. With $I,\omega,P_{I,\omega},\widehat A,\Sigma(N)$ and $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$ as in the [local floor and major transfer](r70-spectral-lowest-largest-prime-transfer.md), the estimates are

$$
\begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
  &\ll \Sigma(N)|I|\mathcal B/L+N^{1-c},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)e(-N\theta)
                                                     \,d\theta\right|
  &\ll \Sigma(N)|I|\mathcal B/L+N^{1-c}.
\end{split}
 \tag{3}
$$

The exponent $c>0$ can be taken as in that transfer, on the indicated range for each line. Each conclusion is $o(\Sigma(N))$ in the $L/N$ Hardy normalization. All estimates below for the reciprocal majorant itself are unconditional.

## 1. Keep the exact coefficients, including arbitrarily large true counts

Extract the true largest prime $p$ with $m=pk$, $p>\max(N^\kappa,P^+(k))$. Thus $p>G$ for large $N$ and $j(m)=j(k)$. Retain $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, fixed $B>B_0>0$. By the same true identities, only $D<k\le2N^{1-\kappa}$ contributes, $M_>=-\Xi_D-M_\le$, and at fixed $k$ the exact real weight has supremum and variation $O(\tau_4(k))$. This divisor bound is uniform, without a count cap: the sharp product has at most $\tau(k)^2\le\tau_4(k)$ terms on squarefree $k$, and the two possible low mixed divisor splits cost $O(\tau_4(k))$. Count and parity masks are constant at fixed $k$. In particular this bound can majorize the entire genuine coefficient for the extremely large counts

$$
 j(k)>J_*:=\lfloor32\log U\rfloor .
$$

Indeed the positive Rankin bound, including the local multiplier $k/\varphi(k)\ll L_2$, is

$$
 \sum_{\substack{k\le2N^{1-\kappa}\\k\ {\rm sf},\ j(k)>J_*}}
       \frac{\tau_4(k)}k\,\frac{k}{\varphi(k)}
 \ll L_2\,2^{-J_*}
        \prod_{\ell\le2N,\ \ell\ {\rm prime}}
              \left(1+\frac{4\cdot 2^{\mathbf1_{\ell\le G}}}{\ell}\right)
 \ll L_2\,2^{-J_*}L^4U^4 \ll U^{-9}.
 \tag{4}
$$

The product estimate uses Mertens with the extra factor of 2 only at primes $\le G$. This treats every actual count above $J_*$ and imposes no artificial restriction on the corresponding small-factor product.

For $j=j(k)\le J_*$ write $k=bv$ exactly, where $b$ is the squarefree product of its primes $\le G$ and $v$ is strictly $G$-rough. Then $b\le G^{J_*}=N^{o(1)}$. On a physical cell in $x=pk$ and an arithmetic cell $K<k\le K'$ of log width $w$, take $T_1=k/D$, $T_2=Dk/x$. The parity formulas on composite squarefree $k$ are

$$
 F_0=-\mu(k)S_k(T_1^-)-S_k(T_2),\qquad
 F_1=\frac{\log(x/D^2)}{\log x}F_0
       +\frac2{\log x}\{\mu(k)J_k(T_1)-J_k(T_2)\}.
 \tag{5}
$$

Here $S_k$ is the signed divisor primitive, $J_k$ its integral in log coordinate, and the actual product for $-\Xi_D$ is $F_0F_1$. The first endpoint is strict and the second weak. Both cutoffs have log distance at most $W=C_B L_2$, and the same is true of the slightly widened envelopes below. Prime $k$ has $D<k<\sqrt x$ and reciprocal mass $O(L_2/L)$, as in the previous estimate.

The arithmetic border $k\le10 D L^{2B}$ needs a smaller majorant than $4^j$. Both short cutoffs there are at most $Y_1=20L^{2B}$ for large $N$, so only prime divisors of $k$ at most $Y_1$ can enter $S_k,J_k$. The integrated weights in (5) are $O(W/L)$ per divisor. Consequently the product's magnitude is $O((W/L)4^{j_1(k)})$, where $j_1(k)$ counts prime divisors $\le Y_1$. Expand $4^{j_1(k)}$ as $\sum_{d\mid k,\ P^+(d)\le Y_1}3^{\omega(d)}$ on squarefree $k$. For $j(k)\le J_*$ all its divisors $d$ have $\omega(d)\le J_*$ since $Y_1<G$ eventually, and $d\le Y_1^{J_*}=N^{o(1)}$. The reciprocal count of multiples of each on the border is $O(W/d+1/D)$. Their floor sum is $N^{-1/2+o(1)}$, including the weights. The reciprocal main sum is bounded by

$$
 W\prod_{\ell\le Y_1,\ \ell\ {\rm prime}}(1+3/\ell)
       \ll W L_2^3.
$$

Thus the border costs $O(W^2L_2^3/L)$ in the reciprocal product, even without any lower or upper count selector within $j\le J_*$. Counts above $J_*$ on the border were already included in (4).

## 2. Signed Fourier moments on the upper tail

Use the [signed Euler cutoff transform](r70-spectral-signed-shift-euler-slots.md). The exact operator $\mathcal D_b f(u)=\sum_{d\mid b}\mu(d)f(u-\log d)$ has multiplier $q_b(\xi)=\prod_{\ell\mid b}(1-e^{-i\xi\log\ell})$. For the masked reciprocal primitive $R_{G,e}$, where a rough gcd label $e$ also has its primes excluded, its Fourier transform is $\widehat R_G$ multiplied by $\prod_{\ell\mid e}(1-\ell^{-1-i\xi})^{-1}$. This factor is uniformly bounded on $e\le10N^{1/2-\kappa}L^B$ because the primes of $e$ exceed $G$. The frequency estimates and generating variable from the same proof are

$$
\begin{array}{ll}
 |\widehat R_G(\xi)|\ll U/(1+U|\xi|),\quad
 M(\xi)\le2\log(1+U|\xi|)+O(1)&(|\xi|\le1),\\
 M(\xi)\ll(U|\xi|)^2 &(U|\xi|\le1),\\
 |\widehat R_G(\xi)|\ll(1+\log(3+|\xi|))^4/|\xi|,\quad
 M(\xi)\le 2\log U+O(1+\log\log(3+|\xi|)) &( |\xi|\ge1),
\end{array}
$$

where $M(\xi)=\sum_{\ell\le G,\ \ell\ {\rm prime}}|1-e^{-i\xi\log\ell}|^2/\ell$. For any fixed $z>0$ the harmonic generator of the **exact signed squared multiplier** is

$$
 \sum_{\substack{b\ {\rm sf}\\P^+(b)\le G}}
      \frac{z^{\omega(b)}}b|q_b(\xi)|^2
       \le e^{zM(\xi)}.
 \tag{6}
$$

For positive counts use $e^{zM}-1$. With $z>1$ the total over $j\ge r$ therefore costs at most $z^{-r}$ times the weighted generator, including when the sum is later capped at $J_*$. This is the high-count direction of the generating inequality.

For clarity, the untruncated Plancherel integrals needed below have the following bounds, with constants allowed to depend on the fixed generating parameter. First, for $z>1/2$,

$$
 \int_{\mathbb R}|\widehat R_G(\xi)|^2 e^{zM(\xi)}\,d\xi
                  \ll_z U^{2z}.
 \tag{7}
$$

At $|\xi|\le1$ scale $y=U|\xi|$ and integrate
$U(1+y)^{-2+2z}$ over $[0,U]$; at $|\xi|\ge1$ the logarithmic powers integrate against $\xi^{-2}$ and cost $U^{2z}$. For $z<1/2$ the corresponding bound is $O_z(U)$, as previously. A sum or difference of two endpoint primitives of log distance $h$ costs at most a factor 4 in these squared bounds. Their intervening signed integral has multiplier at most $W$ times the unintegrated one for $0\le h\le W$, so its squared bound is at most $W^2$ times (7).

Second, for $0<z<3/2$, the full signed integrated cutoff of a positive count is bounded using

$$
 \int_{\mathbb R}|\widehat R_G(\xi)|^2
              \frac{e^{zM(\xi)}-1}{\xi^2}\,d\xi\ll_z U^3.
 \tag{8}
$$

Near zero $e^{zM}-1=O_z(y^2)$, so the scaled integral is finite; for $1\le y\le U$ its integrand after extracting $U^3$ is $O_z(y^{-4+2z})$. The large-$|\xi|$ contribution is $O_z(U^{2z})$ and is smaller. The multiplier $q_b(\xi)/(i\xi)$ here is the actual signed integrated primitive: extract one divisor prime of $b>1$, so integration becomes a finite log-interval convolution, followed by the other signed translates. A sum of two integrated cutoffs costs at most a factor 4 after squaring. Equations (7)–(8) hold also for each $R_{G,e}$ by its bounded extra factors. The same arguments of course apply to a lower count cap with $0<z<1$ and multiplier $z^{-r}$.

## 3. True rough traces and exact moving endpoints

We detail the changes required by allowing counts as large as $J_*$. Take arithmetic and physical log cells of width at most $\eta=L^{-100}$. For each fixed physical cell choose $x_0$ in it, putting $h=\log(x_0/D^2)\in(0,W]$. The two comparison cutoffs are $\exp u,\exp(u-h)$, with $u$ ranging over the arithmetic cutoff interval $\mathcal U$ of length $w$. They are within $O(\eta)$ in log of the original respective cutoffs throughout the cell pair. Work at fixed $b$ on $K/b<v\le K'/b$. Just as in the signed Euler proof, form uniform-in-$x$ nonnegative majorants $C_0(v),C_1(v)$ for the sharp factor and the **unscaled** braces in (5). Each one is the square root of the corresponding model-square mean over $u\in\mathcal U$, plus a positive endpoint envelope. Model signs are set to the selected parity, and other $v$ may be included only when upper-bounding the resulting nonnegative square. The actual parity weight and the Fourier polynomial are unmodified.

For completeness the rough reciprocal count of a fixed LCM gives main weight $w\prod_{\ell\le G}(1-1/\ell)=O(w/U)$ times the reciprocal LCM, with the same Bonferroni log tail and local floor as in the lower-largest-prime proof. Every divisor label on a given cell is at most $10K/D$, even after a boundary expansion or division by a divisor of $b$. Thus the floor in a signed square, summed over all label pairs, is $N^{-\kappa+o(1)}$ per cell, since $(K/D)^2 b/K\le N^{-\kappa+o(1)}$. The factors $2^j$ are only polynomial in $L$ even up to $J_*$, the geometrically many cells in $L$ are polynomial in $L$, and $\sum_b1/b\ll U$. The floors therefore remain power-small after summing all cells and taking final Cauchy; the arbitrary fixed inverse-log main remainders can be made smaller than $L^{-5}$. Dividing by $w$ in the comparison mean cancels the exact trace main factor and leaves the uniform floor, and does not require any lower bound for a nonempty cell width.

The sharp endpoint envelope consists of unsigned brackets of log width $O(\eta)$ for the endpoint shifts by $d\mid b$. The rough divisor square of each bracket is $O(\eta/U)$ when it excludes 1 and $O(1)$ otherwise, by the diagonal plus the nonunit-pair bound $O((\eta/U)^2(1+L/U))$ for the reciprocal LCM and the negligible $e^{-3U/4}$ rough sieve error. For fixed $b$, a bracket containing 1 forces the arithmetic cutoff cell within $O(\eta)$ of $\log d$ or $\log d+h$, so the total marked log width is $O(2^j\eta)$. The corresponding aggregate squared envelope for fixed $b$, before the $1/b$ sum, is therefore

$$
 O(4^j L\eta/U^2+8^j\eta/U)
$$

apart from the reciprocal floors. The integrated envelope uses signed primitives inside the two log boundary integrals; its squared bound is $O(4^j\eta^2 L/U)$ by Cauchy and the uniform fixed signed primitive LCM energy $O(1)$ from the [common reciprocal kernel proof](r69-spectral-rough-reciprocal-kernel-sampling.md). These bounds include strict cutoffs and exact endpoint integers. Since $8^{J_*}\le U^{32\log8}$, $\sum_b1/b\ll U$, and $\eta=L^{-100}$, the two squared envelope totals are $O(L^{-5})$.

After this transfer the model energies are precisely those of Section 2. Expand the gcd, and for each rough outer $e\le Z=10N^{1/2-\kappa}L^B$ the inner signed sum is the translated cutoff function built from $R_{G,e}$, with weight $\varphi(e)\mu(e)^2/e^2$. Strict and weak model endpoints coincide almost everywhere in the cutoff integral. The disjoint cells integrate over a subset of the real cutoff line, so we may enlarge the nonnegative squares' integrals to the entire line. The rough harmonic sum on $e\le Z$ is $O(1+L/U)$, while the rough trace density contributes $O(1/U)$. Thus at $U=\sqrt L$ the overall multiplier of the Plancherel integral bounds is $O(L/U^2)=O(1)$, including the unit. This enlargement acts on the cutoff integrals only, not on the physical partner support.

## 4. Upper-tail savings and the true low mixed subtraction

For fixed physical cell the majorant for $|F_0F_1|$ is $O((W C_0^2+C_0C_1)/L)$. Apply Cauchy jointly over $b$, rough $v$, and the arithmetic cells, with reciprocal weight $1/(bv)$; include the centered $W C_0^2$ term separately.

For odd total parity $\mu(k)=+1$, the sharp model is a sum of two signed primitives and the braces in (5) give their intervening integral. At $\omega(b)\ge r=\lceil(2+\varepsilon)\log U\rceil$ and $\omega(b)\le J_*$, (6)–(7) bound their summed squares by $O_z(U^{2z}z^{-r})$ and $O_z(W^2 U^{2z}z^{-r})$ for any fixed $z>1$. Thus the reciprocal product is $O_z(W U^{2z-2}z^{-r})$. Set $z=1+\min(\varepsilon/8,1/8)$. The exponent
$2z-2-(2+\varepsilon)\log z$ is at most $-c_1\min(\varepsilon^2,1)$ for an absolute $c_1>1/100$, by $\log(1+s)\ge s-s^2/2$ for $0\le s\le1/8$. This has ample room for the claimed $d_\varepsilon$ after $U=\sqrt L$ and the factor $L_2$. For the optional low odd cap use $r=\lfloor(7/5)\log U\rfloor$, $z=499/1000<1/2$ and (7)'s $O(U)$ version. The product is $O(W U^{-1}z^{-r})$, with exponent $-1+(7/5)\log(1000/499)<-0.026$ in $U$.

For even total parity $\mu(k)=-1$, the sharp model is a difference, bounded by (7), and the braces in (5) are the sum of two full signed integrated cutoffs, bounded by (8). On the high cap $r=\lceil(5/2)\log U\rceil\le j\le J_*$, take $z_0=6/5$ for the former, $z_1=149/100$ for the latter. Their summed squares are $O(U^{2z_0}z_0^{-r})$ and $O(U^3 z_1^{-r})$. This gives the reciprocal product bound

$$
 O\!\left(W U^{2z_0-2}z_0^{-r}
                + U^{z_0-1/2}(z_0 z_1)^{-r/2}\right).
 \tag{9}
$$

The two $U$ exponents are at most
$2z_0-2-\tfrac52\log z_0<-0.055$ and
$z_0-\tfrac12-\tfrac54\log(z_0z_1)<-0.026$. This is a genuine high-count improvement from the signed transform; replacing (6) by an unsigned number of translates would lose these savings.

For the true $M_\le$ on $j\le J_*$ retain the low-divisor split of the signed Euler proof. The h-gate is $D<h\le H_0$ and the two signed coprime labels are below $Y_0=H_0/D=L^{B-B_0}$. Let $j_0$ count primes of $b$ at most $Y_0$. In the two cases $h\mid k$ and $h=pr$, the actual two complementary positive factors split the small tags at cost $2^j$, and the two signed labels incur at most $3^{j_0}$. One complementary rough factor is in a short log interval of width $O(W)$ away from 1 (as $b=N^{o(1)}$), and the other is at most $Z$. Including the $O(W/L)$ centered weight the reciprocal bound before summing $b$ is

$$
 \frac{2^j 3^{j_0}}b\,O\!\left(\frac WL\frac WU(1+L/U)\right).
$$

An auxiliary count parameter $z>0$ weights its harmonic tag product by at most

$$
 \exp\left(2z\sum_{\ell\le G}\frac1\ell+
               4z\sum_{\ell\le Y_0}\frac1\ell\right)
                 \ll_z U^{2z}L_2^{O_z(1)} .
$$

The sums are over primes. For the first two rows of (2) use the same respective $z>1$ and factor $z^{-r}$, obtaining exactly the smaller exponent $2z-2-(r/\log U)\log z$ up to powers of $L_2$. For the low odd row use $z=7/10$ and $r=\lfloor(7/5)\log U\rfloor$, giving exponent $2(7/10)-2+(7/5)\log(10/7)<-0.10$. Counts beyond $J_*$ in $M_\le$ were covered by (4) for the full actual coefficient. The border, prime-$k$, and moving-square floors fit the same rates. Multiplication by the local factor $k/\varphi(k)\ll L_2$ is harmless. This proves the stated reciprocal majorant bounds on every physical cell for exactly the actual masks.

Finally use the original two-root upper sieve and the genuine local-floor/numerator-Parseval major transfer in the lower-largest-prime proof. The positive majorants apply to the true hard $p,N-kp$ pairs and to the completed density with denominator $k\log(x/k)$ and its actual local factor. All selectors remain constant at fixed $k$ and the true right variation is still $O(\tau_4(k))$ even on the extreme tail. The adapted full sieve cutoff and character estimates at the fixed $Q$ are therefore unchanged; the reciprocal floors above supply the same powers in (3). No averaging over moduli, replacement prime sequence or shrinking of the major arcs occurs. Subtract the actual major integral from the actual full coefficient for the second line of (3). None of these bounds estimates the stated gaps between low and high counts.
