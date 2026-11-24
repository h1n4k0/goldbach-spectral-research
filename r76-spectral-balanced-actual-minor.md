# A genuine minor-arc bound for nearly balanced largest-prime partners

**Scope.** We bound real prime triples on the two-large-prime branch in absolute mass, then the actual minor integral at the original $Q$. In contrast to the [signed major estimate](r75-spectral-balanced-rejected-majors.md), this treats the **kept unique-largest** branch as well as the rejected one, and does not infer a full or minor bound by enlarging a signed major integral. The full absolute-mass statement is unconditional. Only the major comparison used for the minor statement needs the historical prime-character Dirichlet GRH. No conclusion is made about the more widely separated partners or about weak S.

Keep the central hard interval $I$, the bounded-variation left test $\omega$ and $P_{I,\omega}$, the genuine squarefree coefficient $M_>(m)$ after the prime marginal has been removed, and $L=\log N$, $L_2=1+\log L$, $D=\sqrt N L^{-B}$, $H_0=\sqrt N L^{-B_0}$, $V=[N/3,2N]$, $B>B_0>0$. For comparison with the actual ordered major, retain the fixed even radical hypothesis. Let $0<\sigma_1<\sigma_2<1/10$, $1\le E\le \sigma_1L/2$. At each squarefree $m\in V$ having at least two prime factors let $q>p$ be its largest two, and put $a=m/(pq)$. Use the true cutoff

$$
 0<\log(q/p)\le E .
 \tag{1}
$$

Take either the kept selector $D N^{\sigma_1}<ap\le D N^{\sigma_2}$ or the rejected selector $D N^{\sigma_1}<aq\le D N^{\sigma_2}$, separately. These mean eligibility of the mark $q$ or $p$, respectively. One may impose any further selector depending only on the integer $a$ and $N$, including its exact small-prime count. Work with a specified true parity, $\mu(m)=-1$ (odd total) or $\mu(m)=+1$ (even total). Define $A(m)$ to be the corresponding literal $M_>(m)$, zero on the complement, and $\widehat A(\theta)=\sum_m A(m)e(m\theta)$.

Put

$$
 \mathcal B_{\rm odd}(E)=\frac{(E+1)L_2^5}{L},\qquad
 \mathcal B_{\rm ev}(E)=\frac{(E+1)L_2^5}{L}
                           +\frac{(E+1)L_2}{\sqrt L}.
$$

Then, with the matching parity,

$$
\begin{split}
 \sum_{n\in I}\lambda(n)|\omega(n)|\,|A(N-n)|
   &\ll \frac{\Sigma(N)|I|}{L}\mathcal B_{\rm parity}(E)
                      +N^{.76},\\
 \left|\int_{\mathfrak m}P_{I,\omega}(\theta)\widehat A(\theta)
                               e(-N\theta)\,d\theta\right|
   &\ll \frac{\Sigma(N)|I|}{L}\mathcal B_{\rm parity}(E)
                      +N^{1-10^{-4}} .
\end{split} \tag{2}
$$

Here $\lambda(n)=\log n\,\mathbf1_{n\ {\rm prime}}$, and $\mathfrak m$ is unchanged, the complement of the arcs with reduced denominator at most $Q=N^{1/1000}$ and $|\nu|\le 2Q/N$. In particular the actual kept near-balance range $E=10L^{2/3}$ is negligible on odd total parity, and every fixed $E=L^{1/2-\epsilon}$, $0<\epsilon<1/2$, works on both. The same bounds apply to either positive-mass definition in the first line, or to their disjointly counted union at a factor of at most two.

## 1. Exact cutoff and a physical-cell envelope

At $x=pqa\in V$ write

$$
 t=\log(aq/D),\qquad s=\log(ap/D),\qquad h=\log(x/D^2),\qquad
 s+t=h+\log a .
$$

By the two eligible-band possibilities and (1), $s,t$ lie between $\sigma_1L/2$ and $(\sigma_2+\sigma_1/2)L$. Thus $ap,aq\le N^{.65+o(1)}$, $p,q>N^{1/3}$ for large $N$, and $a\le N^{.25+o(1)}$. In particular $p,q>a$, the two largest factors are genuinely the two formal tags, and $\mu(m)=\mu(a)$. There is no extra factor from possible nonunique assignments within either selector.

Use the exact swapped formulas (6)–(7) of the balanced major proof, with $S_a(u)=\sum_{d\mid a,\ \log d\le u}\mu(d)$ and $J_a(u)=\int_{-\infty}^u S_a(v)\,dv$. Their algebraic hypotheses still hold in the widened exponent ranges just stated: the two short arguments are $s^-$ and $s-h$, with labels $\ll N^{.15}$, and the complementary low terms use a cofactor divisor of size $N^{1/2+o(1)}$, hence one of the giant tags. In particular the first short cutoff is strict. On true pairs $M_>=X_a-Y_a$, and for odd total $X_a$ contains the short integrated difference, whereas for even total it contains the full integrated sum as in the stated formulas. Both are genuine squarefree calculations. The formulas are likewise valid for the real weights used after a fixed-tag prime comparison, by the same formal-tag symmetry.

Partition $V$ into real half-open geometric cells of log width at most $\eta=L^{-2}$. Take a reference point $x_0$ in the closure of a cell. At fixed $a,q$ write $s_0=\log(x_0/(qD))$, $h_0=\log(x_0/D^2)$. For a genuine $x$ in this cell,

$$
 |s-s_0|\le\eta,\quad |h-h_0|\le\eta,\quad s-h=s_0-h_0.
 \tag{3}
$$

In particular the second short cutoff does not move at all. For the envelope impose the widened common support

$$
 \sigma_1L/2-\eta\le s_0,t\le(\sigma_2+\sigma_1/2)L+\eta,
       \qquad -\eta\le t-s_0\le E+\eta ,
 \tag{4}
$$

which contains the true support of either selector on this cell. At fixed $a,x_0$ these are a bounded number of interval gates in $\log q$; at fixed $s_0,x_0$ the allowed $a$ has log width at most $E+2\eta$ since $t+s_0=h_0+\log a$. All ranges still have polynomial lower size for $a,p,q$ (in the reinterpreted sizes at $x_0$). This enlargement is only for positive envelopes, never for the actual polynomial or inner prime count.

Let

$$
 C_0(a,q)=|S_a(s_0^-)|+|S_a(s_0-h_0)|+
            \sum_{\substack{d\mid a\\ |\log d-s_0|\le 2\eta}}1 .
$$

The short primitive at any actual first cutoff, even when exactly at an integer, and the second short primitive are dominated. The endpoint movement of $J_a(s)$ is at most $O(\eta C_0)$, by integrating the corresponding primitive over the moving endpoint. Set $K_0=J_a(s_0)-J_a(s_0-h_0)$; the other integrated endpoint in (3) is unchanged. It follows from the exact sharp formulas that a nonnegative bound for $|X_a|$ throughout the cell, up to fixed absolute constants, is

$$
 \frac1L\left(L_2 C_0^2+C_0 C_1\right),\qquad
 C_1=
 \begin{cases}
    |K_0|+\eta C_0,&\text{odd total},\\
    |J_a(s_0)|+|J_a(s_0-h_0)|+\eta C_0,&\text{even total}.
 \end{cases}
 \tag{5}
$$

For $Y_a$ use its two genuine divisor folds but take absolute weights $O(L_2/L)$. In their formulas for $z=\log(l/D)$ at $x_0$, allow $-\eta\le z\le\log(H_0/D)+\eta$ and each signed-label bound $d_i\le e^{z+\eta}$. This covers the actual first fold, and the second fold has $h-s$ constant anyway. Keep the designated factor divisibilities and the coprimality of the two labels. Denote by $C(a,q)$ the resulting total positive envelope, zero outside (4). It can also be zero off the fixed integer selector on $a$. For each fixed $a,x_0$,

$$
 \|C(a,\cdot)\|_\infty+\operatorname{Var} C(a,\cdot)
                                 \ll L^{C'}\tau_8(a).
 \tag{6}
$$

To see this, view $\log q$ as the monotone variable: each short-label term makes at most a bounded number of hard jumps; $J_a$ is a sum of monotone clipped linear logs, each of variation $O(L)$ on the support. Absolute values and the products preserve this coarse variation bound. Each low fold has at most $\sum_{v\mid a}3^{\omega(v)}=\tau_4(a)$ possible divisor and label assignments on squarefree $a$ (in the first case swap $v$ and $a/v$ in this counting identity); each assignment has only a bounded number of interval tests. The same bound with $\tau_8$ therefore holds as stated. The supremum bound in (6) is $N^{o(1)}$ uniformly in the applicable $a$.

## 2. Actual reciprocal arithmetic energy on the widened cell

At fixed $x_0,s_0$, let the $a$ sum have support (4), with either true parity. The moving cutoff estimate (9) in the balanced major proof gives

$$
 \sum_a \frac{C_0^2}a\ll E+1,\qquad
 \sum_a \frac{C_1^2}a\ll
          \begin{cases}
               L_2^2(E+1),&\text{odd total},\\
               L(E+1),&\text{even total}.
          \end{cases}
 \tag{7}
$$

We detail the only extension, the unsigned shell in $C_0$. At any ordinary dyad $a\asymp A$, split its labels into $\log d\le\tfrac12\log a$ or $>\tfrac12\log a$. Reflect the latter by the actual divisor map $d\mapsto a/d$ on the true squarefree $a$. Both new shells then have log width at most $4\eta$, clipped if necessary at $\tfrac12\log a$, and upper size $O(\sqrt A)$. The gates for each label at fixed $s_0$ or at its reflected center $\log a-s_0$ are a bounded number of inequalities affine in $\log a$, so each pair of labels in a squared count has a bounded number of interval pieces. Sum over the relevant multiples of their LCM at those actual intervals. The ordinary $O(1/A)$ reciprocal floor is summed just once per pair, hence costs $O(1)$ on this dyad. In the real main term interchange the exact interval integrals and the label sum, and apply the unsigned short-shell reciprocal LCM bound (3) of the [subpower largest-prime proof](r66-spectral-subpower-largest-prime.md) at the moving shell. It gives $O(1+\eta^2L)=O(1)$ pointwise; clipping only decreases the positive main. Both reflected/ unreflected contributions therefore obey the same $O(1)$ reciprocal square on a dyad, expanding and dropping the squarefree subset only **after** these exact transformations. This proves the required shell estimate through $O(E+1)$ dyads.

For the signed terms of $C_0$ reflect by the exact strict/weak identity (10) of the balanced proof when their cutoff exceeds $\sqrt a$, then use that moving signed square estimate. For odd $K_0$, use Cauchy under its real interval of length $h_0=O(L_2)$ and apply the same primitive estimate at every intervening argument. For the even $J$ terms use the exact reflection of the composite squarefree $J_a$, then the moving integrated square estimate. In even parity $a$ is necessarily composite since $a$ is polynomially large and $\mu(a)=+1$. All reflected thresholds are affine in $\log a$ on a bounded number of pieces, and (4) still has log width $O(E+1)$. These facts prove (7), with no signed cancellation asserted across prime pairs.

For the absolute low bound in $C(a,q)$, use the same positive two-factor harmonic count as §4 of the balanced proof. In either widened fold write $a=uv$ with $\log v$ in an interval of width $O(L_2)$ within $O(L_2)$ of $s_0$, and with $u$ then in a log interval of width $O(E+1)$. The two labels $d_i\ll L^{B-B_0}$ are coprime and their product divides the designated factor. Both variables are polynomially large on this support, so their reciprocal counts (also in arbitrarily short intervals) are $O((w+1)/d)$ for a designated multiple of $d$ and $O(w+1)$ otherwise, where $w$ is its log width. The one-term floor fits even at the endpoint. The label harmonic cost is $O(L_2^2)$, and its coefficient is $O(L_2/L)$. Thus the absolute low sum contributes $O((E+1)L_2^4/L)$ to $\sum_a C(a,q(s_0,a))/a$, where $q(s_0,a)=x_0e^{-s_0}/D$ is simply the real second tag determined by $s_0$ and $x_0$ (the dependence on $a$ in the notation is only through the allowed support and coefficient). The sharp part using (5)–(7) contributes $O((E+1)L_2/L)$ in odd parity and $O((E+1)(L_2/L+1/\sqrt L))$ in even parity. In particular, if

$$
 \mathcal D_{\rm odd}(E)=\frac{(E+1)L_2^4}{L},\qquad
 \mathcal D_{\rm ev}(E)=\frac{(E+1)L_2^4}{L}
                                      +\frac{E+1}{\sqrt L},
$$

we have proved the uniform real-coordinate envelope

$$
             \sum_a \frac{C(a,q(s_0,a))}{a}
                              \ll \mathcal D_{\rm parity}(E).
 \tag{8}
$$

## 3. Absolute actual prime mass

Let $I_j$ be the part of the hard left interval for which $x=N-n$ lies in the physical cell. Fix the actual integer $k=aq$ with $q$ prime, and apply the [two-root upper sieve](r70-spectral-lowest-largest-prime-transfer.md) to the actual primes $p,N-kp$ on their true hard interval. All the original real gates (1) and the chosen kept/rejected band are intervals in $x$ at fixed $k,q$; the extra integer selector is fixed there. Since $p>N^{1/3}$, use sieving height $N^{1/300}$ and level $N^{1/12}$, exactly the permissible scale from that proof for $\kappa=1/3$. Both forms exceed the height. At such prime positions $(k,N)=1$, since otherwise the left prime $n$ would divide both $k$ and $N$ while $N/2<n<N$. The uniform sieve bound is

$$
 O\!\left(\frac{\Sigma(N)|I_j|}{kL^2}\frac{k}{\varphi(k)}
                                      +N^{1/12+o(1)}\right).
$$

Multiply by the positive coefficient envelope and the left log/weight bound. The total sieve floors cost $N^{.76}$: $k\le N^{.65+o(1)}$, there are only polylogarithmically many cells, each $k$ has at most one actual possible $q$ since $q>a$, and (6) is subpower. Even $O(L)$ possible divisors $q$ would be harmless. Thus it remains to bound, on each cell independently,

$$
 \sum_{a}\frac1a\sum_{q\ {\rm prime}}\frac{C(a,q)}q.
 \tag{9}
$$

We have used $k/\varphi(k)\ll L_2$ outside this sum, so no local-factor regularity in $q$ is required.

The genuine remaining prime $q$ in (9) can be summed against the positive bounded-variation weight (6) by the ordinary **unconditional** prime number theorem with error $O(y\exp(-c\sqrt{\log y}))$ for $\pi(y)-\mathrm{Li}(y)$ (e.g. [Montgomery–Vaughan, Ch. 6, Thm. 6.9 and partial summation](https://www.cambridge.org/core/books/abs/multiplicative-number-theory-i/prime-number-theorem/9373CF81784ED6539A5C77F8861E5287)). On each ordinary dyad $q\asymp Y\gg N^{1/3}$, the factor $1/q$ and its variation are $O(1/Y)$, so the error after summing dyads is $\tau_8(a)L^{O(1)}\exp(-c'\sqrt L)$. Summing with $1/a$ costs only a fixed log power. The real density is $dq/(q\log q)$, and $dq/q=-ds_0$ exactly. Since $\log q\gg L$, the main in (9) is bounded by $O(1/L)$ times the $s_0$ integral of (8) over a range of length $O(L)$. Hence (9) is $O(\mathcal D_{\rm parity}(E))$, uniformly in the physical cell and both literal eligibility choices. No one substitutes a model for the actual additive prime correlation in this step: the first two prime forms were upper-sieved and only the remaining positive outer majorant, with no additive phase, was summed by ordinary PNT.

Using $\sum_j|I_j|=|I|$ and the earlier $L_2$ local loss now proves the unconditional first line of (2). No mean over $N$ is involved.

## 4. The actual fixed-$Q$ minor integral

Use the same two-genuine-prime comparison and Ramanujan completion as §1 of the balanced major proof. For the kept eligibility gate at fixed $k=aq$, the cofactor log $s=\log(x/(qD))$ gives just an extra hard interval in $x$; $t$ is constant. Hence both literal selector choices give bounded variation $O(\tau_4(k))$ for the actual real right coefficient with all endpoints. The only larger upper range is $k\le N^{.65+o(1)}$, whose pointwise first-prime error summed in $k$ is $O_\epsilon(Q^2 N^{.825+\epsilon})$. This still meets the original integrated power error. The occupation estimates and Fourier/Ramanujan tails have the same fixed $Q$, since both tags exceed $Q$, $\log(x/k)\gg L$, and the support $k\le N$ and full variation bound are still valid. After completing the first prime with $r(k)$ as there, ordinary prime partial summation in the second tag gives exactly the real density with both prime logarithms (4) of that proof, on the chosen true support. The fixed left polynomial and the bounded family of hard intervals are unchanged. The historical Dirichlet GRH assumption supplies the same $O(N^{1-10^{-4}})$ integrated error.

The absolute completed density is also small: take the cell envelope with reference $x_0=x$ in (8), retain only the true support, and bound the two real prime logarithms below by a constant times $L$, the fixed local factor $r(a)$ above by $O(L_2)$, and the remaining $s$ interval by length $O(L)$. It is bounded by $\Sigma(N) \mathcal B_{\rm parity}(E)/L$ uniformly in $x\in V$. This uses a positive bound only after the exact genuine major comparison; it also covers the kept selector without using a signed cancellation special to rejected tags. Subtract the actual major integral from the exact full correlation (ordinary Fourier inversion). Apply the actual absolute-mass bound already proved to that full correlation. This gives the second line of (2), with the original arcs and actual prime polynomial untouched. The gap between the odd and even widths in this result is the long integrated primitive in the even **absolute-mass** step; the signed integration by parts on major arcs alone does not remove that gap for the genuine prime correlation.
