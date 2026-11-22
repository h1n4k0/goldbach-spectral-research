# A medium-prime parity test detects coherent transport

**Scope.** This is an unconditional estimate on the actual shifted-prime sequence in the [coherent transport construction](spectral-coherent-divisor-transport-barrier.md). Parity of the number of selected medium prime factors detects that construction at a fixed fraction of the removed prime-partner mass. It is not total Möbius parity, does not estimate the actual prime-pair mass, and can itself be preserved by a different transport. No assertion on Hypothesis S is made.

Fix $K\ge2$ and $J\ge1$, and keep the true prime weight $\lambda(n)=(\log n)\mathbf1_{n\ {\rm prime}}$ in each central cell $I$ of length $H=N/(16\lceil(\log N)^J\rceil)$ from the transport construction. Use $m=N-n$, $L=\log N$, $S=\mathfrak S(N)$, and $z=N^\beta$. Choose first an absolute sufficiently small fixed $0<\nu<1/100$, and define

$$
 \mathcal T_N=\{r\text{ prime}: N^{2/5}\le r<N^{2/5+\nu},\ r\nmid N\},\qquad
 h_N=\sum_{r\in\mathcal T_N}\frac1{r-1},\qquad
 \pi_T(m)=(-1)^{\omega_T(m)},\quad
 \omega_T(m)=\#\{r\in\mathcal T_N:r\mid m\}.
$$

Then $h_N\to h_\nu=\log((2/5+\nu)/(2/5))>0$, by Mertens, since at most two primes of the band can divide $N$. Choose the fixed $\beta>0$ in the transport construction sufficiently small depending on $K,\nu$; the required smallness is independent of $J$. Put

$$
 V_z=\prod_{\substack{p<z\\p\nmid N}}\left(1-\frac1{p-1}\right)
       \asymp S/(\beta L).
$$

All statements below are uniform over the cells and over sufficiently large even $N$; thresholds may depend on the fixed parameters.

Let $C_I^-$ and $C_I^+$ be the actual $\lambda$-masses on the transport reservoir $\mathcal C_I$ of squarefree $z$-rough $m$ with $\omega(m)>K$, further restricted to $\pi_T=-1$ or $+1$, respectively. Then

$$
 C_I^-\asymp H V_z h_N,\qquad C_I^+\asymp H V_z.                  \tag{1}
$$

The implied constants can be absolute after the choices below. In particular, with $C_I=C_I^-+C_I^+$ and $P_I$ the original true mass of primes $n$ with prime $m$, the specific uniform-reservoir transport of the earlier note satisfies

$$
 \sum_{n\in I}\big(\widetilde\lambda_N(n)-\lambda(n)\big)\pi_T(N-n)
       =-2P_I\,\frac{C_I^-}{C_I}.                                \tag{2}
$$

Its magnitude is $\asymp h_N P_I$ whenever $P_I>0$. In (2) the actual prime partners all satisfy $\pi_T=+1$; a prime $m\asymp N$ is above the tag band.

## 1. First tagged incidence by genuine coherent distribution

Since $3(2/5)>1$, one has $\omega_T(m)\le2$ in the central range. Let $M_1(I)$ be the actual $\lambda$-weighted first incidence of $\omega_T(m)$ on all $z$-rough $m$ in the cell, without a squarefree or total-factor restriction. For each $r\in\mathcal T_N$, sieve the positive true-prime weight with $r\mid m$ by the primes $p<z,\ p\nmid N$ on $m$. Write $\rho=1/2-(2/5+\nu)>0$ and take the sieve level $D=N^\rho L^{-B}$.

At a squarefree sieve modulus $d\le D$, the combined modulus is $rd$ and the residue is $N\bmod rd$, reduced. Because all prime factors of $d$ are $<z$ and $r>z$, the map $(r,d)\mapsto rd$ is injective. It lies below $\sqrt N L^{-B}$. Maximal [Bombieri–Vinogradov](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=206) therefore gives an aggregate $O_A(NL^{-A})$ bound across $r,d$ for replacing the prime progression weights by $H/(\varphi(r)\varphi(d))$. Each cell interval is a difference of two prefixes. Passage from Mangoldt to prime-only weights costs at most $O(\sqrt N L)$ per modulus, so enlarging $B$ absorbs it in the prescribed log saving. Every prime $N/2<n<N$ is a unit modulo $N$.

For each $r$ the positive sieve uses $X=H/\varphi(r)$ and local density $1/(p-1)$ at the sifted unit primes, giving dimension one and the common product $V_z$. Apply the [fundamental lemma, Corollary 19](https://terrytao.wordpress.com/2015/01/21/254a-notes-4-some-sieve-theory/) with $\log D/\log z\to\rho/\beta$, taking $\beta$ so small that the relative sieve error is at most $1/2$. This does not take relative errors separately in the actual prime sequences: the arithmetic remainders have just been summed over the distinct moduli. With $A>J+5$ we obtain, for all sufficiently large $N$,

$$
 \tfrac13 H V_z h_N\ \le M_1(I)\ \le 2 H V_z h_N.                \tag{3}
$$

The rough mass with no tag condition on $I$ likewise lies between $\frac13 H V_z$ and $2H V_z$ by the same dimension-one sieve, as in the transport proof.

## 2. Double tags cost a second harmonic factor

Let $M_2(I)$ be the actual $\lambda$-weighted $\binom{\omega_T(m)}{2}$ incidence on $z$-rough $m$. For distinct $r,s\in\mathcal T_N$ put $C=rs$ and write $m=C u$. The $u$-interval induced by $n\in I$ has length $U=H/C\ge N^{.2-2\nu-o(1)}$, so $\log U$ is at least an absolute positive multiple of $L$ for large $N$. Impose primality of $n=N-Cu$ by its forbidden roots at primes $p<Y=U^{1/100}$. Also impose $u\not\equiv0\bmod p$ for primes $p<z,\ p\nmid N$. Choose $\beta<1/1000$, so $z<Y$ uniformly. All original points pass these exclusions: $n$ prime is $>Y$ and $C$ has no factor $<z$.

The first root is absent at $p\mid C$; at $p\nmid C$ it is $N\bar C\bmod p$. The second root is distinct whenever it occurs because $p\nmid CN$; there is no second root at $2$. Thus the uniform dimension-two upper sieve with level $U^{1/2}$ and $Y=U^{1/100}$ applies. Each squarefree sieve modulus has CRT remainder $O(2^{\omega(d)})$; their total is $O(U^{1/2}\log(2U))$. Its local main product is at most

$$
 \ll \frac{C}{\varphi(C)\log Y}V_z .
$$

Indeed the first-root product is $\prod_{p<Y,\ p\nmid C}(1-1/p)$, and the ratio for each extra root is $(p-2)/(p-1)$. Multiplying the sifted count by $L$ for the prime logarithm, and summing over unordered tag pairs, gives

$$
 M_2(I)\le B_0 H V_z h_N^2+O(N^{.9+\nu}L^2)                   \tag{4}
$$

with an absolute $B_0$, independent of the small $\beta,\nu$. The main term uses $\sum_{r<s}1/\varphi(rs)\le h_N^2/2$. For the errors, $H^{1/2}\sum_{r<s}(rs)^{-1/2}\ll N^{.9+\nu}$ by the elementary sum of inverse square roots up to $N^{2/5+\nu}$. The error in (4) is negligible relative to $H V_z h_N$.

Since $\omega_T$ is at most two, the mass of exactly one tag is $M_1(I)-2M_2(I)$. Choose the fixed $\nu$ so small that $h_\nu<\min(1/(100 B_0),1/1000)$. The dimension-two constant in (4) is uniform throughout $0<\nu<1/100$, so this choice is not circular. For sufficiently large $N$, (3)–(4) make the mass of exactly one tag $\gg H V_z h_N$; its upper bound follows already from (3).

Delete the nonsquarefree $z$-rough $m$ at raw cost $O(NL/z)$, using a square of a prime at least $z$. Delete also the squarefree rough $m$ with at most $K$ prime factors. Their raw mass was bounded in the transport proof by

$$
 O_K\big(SH L^{-1}(1+\log(1/\beta))^{K-1}
            +N^{1-1/(4K)}L^2\big).
$$

After fixing $\nu,K$, the choice of a sufficiently small fixed $\beta$ makes this smaller than half of the preceding lower bound $c H V_z h_N$, since $\beta(1+\log(1/\beta))^{K-1}\to0$. This proves the estimate for $C_I^-$ in (1). For $C_I^+$, start from the full rough mass lower bound $\frac13 H V_z$, then subtract the same low-factor and squareful masses and all tagged mass, the latter at most $M_1(I)$. The smallness of $h_N$ and $\beta$ leaves $\gg H V_z$ in the **zero**-tag subset of the reservoir. The full rough upper bound gives the corresponding upper bound. This proves (1).

## 3. What the additional test does and does not force

In the earlier uniform transport, the removed prime mass $P_I$ contributes $-P_I$ to the test in (2). The increase on the whole reservoir contributes $(P_I/C_I)(C_I^+-C_I^-)$. This proves (2) exactly, and summing over cells causes no cancellation of the defect. Thus a genuine signed factor-count statistic beyond the coherent small-divisor data is measured at the scale needed to detect this particular transport, if there is prime-partner mass to remove.

One can nevertheless modify the construction by transporting solely onto the **zero**-tag reservoir, whose mass was just proved to be $\gg H V_z$. The same $1+O(\beta)$ weight cap, exact cell totals, coherence and squarefree preservation, and zero composite coefficient at receiving sites still hold. This new transport preserves the tag moment in every complete cell because both the removed and receiving points now have $\pi_T=+1$. Consequently this single parity bit does not distinguish primes from the whole high-factor reservoir. In particular (1) does not estimate the genuine sign $\mu(m)$, and cannot certify a central prime-pair lower bound.
