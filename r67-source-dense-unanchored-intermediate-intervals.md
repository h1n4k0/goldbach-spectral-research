# Pointwise unanchored dense intermediate-prime intervals

Keep the exact negative central sum line, strict divisor tests, squarefree units and outer integer masks of the [unanchored sparse-band theorem](r66-source-unanchored-sparse-intermediate-bands.md). Thus $L=\log N$, $\ell=\log L$, $T=L/\ell$, $D=\lfloor\sqrt N e^{-20T}\rfloor$, $Q=\lfloor N e^{-20T}\rfloor$, $I\subseteq I_0=[\rho N,(1-\rho)N]$ is hard, and $n=su,m=tv$. Both lower products $s,t$ are nonempty and have **no small-prime anchor**. The nonempty rough parts contain only primes $\ge \exp(CT)$ with $C>0$ fixed. Their arity may grow.

The lower primes now lie in full intervals, not sparse bands:

- **Power-log endpoint:** fix $0<a_i<b_i<1$; the entire allowed prime interval is $[\exp(L^{a_i}),\exp(L^{b_i})]$, with no whole-product cap.
- **Higher endpoint:** fix $0<a_i<b_i=1$ and $0<B<\min(C,20)$; its entire allowed prime interval is $[\exp(L^{a_i}),\exp(BT)]$. On this slot require the original lower product to be $\le \exp(BT)$.

At most one slot uses a higher endpoint. All these ranges are disjoint from the true rough range for sufficiently large $N$. The statements allow arbitrary subsets of the selected integers independent of the interior divisor labels. Any smaller subalphabet can therefore be used as an integer mask.

**Theorem (unconditional, pointwise).** Let $j_H=0$ or $1$ be the number of higher endpoints, set $\nu=\log 2/C$, $a_*=\min(a_1,a_2)$ and $\Delta=(b_1-a_1)+(b_2-a_2)$. Suppose

$$
  \chi=\min(1-a_*-2\Delta,\ 2-a_1-a_2-2\Delta-2\nu)>0.
 \tag{1}
$$

For every fixed $A>0$, all sufficiently large even $N$, and all admitted hard intervals and masks, the actual sum

$$
 R_N(I)=-
 \sum_{\substack{n+m=N,\ n\in I,\ m\in I_0\\(nm,N)=1,\ n,m\ {\rm selected}}}
 \ \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
      \mu(d)\mu(e)\log(n/d)\log(m/e)
$$

satisfies

$$
   |R_N(I)|\ll
      \mathfrak S(N)\bigl(|I|\ell^{5-2j_H}L^{-\chi}+NL^{-A}\bigr).
 \tag{2}
$$

Constants depend on the fixed parameters. For example two power-log intervals with $a_i=.2,b_i=.39,C=5$ qualify, with $\chi=.04$. A power-log interval with $(a_1,b_1)=(.2,.25)$ also qualifies against a genuine capped higher endpoint with $a_2=.95,b_2=1,B=3,C=5$. Their reciprocal prime masses grow as a positive multiple of $\log L$, unlike the sparse alphabets. No bound for unrestricted dense endpoint widths, two higher endpoints, nonsquarefree inputs, a pointwise main term, or Hypothesis S is asserted.

## 1. Least-prime logarithms in a full moving interval

For an interval $[U,V]$ of lower primes write

$$
 M(U,V)=\prod_{U\le p\le V}(1+2\lambda^*(p)/p),
       \qquad \lambda^*(p)=\frac{p-1}{p-2}
$$

on the odd primes in this interval. All primes under consideration here exceed $2$ for large $N$. Since each local factor is $1+2/p+O(p^{-2})$, Mertens gives $M(U,V)\asymp(\log V/\log U)^2$, uniformly in $V\ge U\to\infty$. For the unmarked lower profile with weight $\tau(s)\lambda^*(s)/s$, the full unrestricted squarefree sum equals $M(U,V)$. For the least-prime mark a direct factorization, as in the [least-prime first moment](r64-source-least-prime-toggle-first-moment.md), gives

$$
 \frac1{M(U,V)}
 \sum_{\substack{s>1\ \mathrm{squarefree}\\p\mid s\Rightarrow U\le p\le V}}
          \frac{\tau(s)\lambda^*(s)}s\,\log P^-(s)
 =
 \sum_{U\le p\le V}
   \frac{2\lambda^*(p)\log p/p}{\prod_{U\le r\le p}(1+2\lambda^*(r)/r)}
 \ll (\log U)^2 \sum_{p\ge U}\frac1{p\log p}
 \ll \log U.
 \tag{3}
$$

In the denominator $r$ runs over primes. The partial Euler product through $p$ is $\gg(\log p/\log U)^2$, and the final tail bound follows from Chebyshev by partial summation or dyadic intervals. Thus the marked weight $1+\log P^-(s)$ costs **the lower log endpoint**, not the largest allowed prime logarithm. This is an upper moment, with the exact least prime of each positive integer. Dropping a product cap or a subalphabet in this estimate only enlarges positive sums and does not change any integer's least prime.

For slot $i$, the unmarked cost is $O(L^{2(b_i-a_i)})$ at a power-log endpoint, and $O_B(L^{2(1-a_i)}/\ell^2)$ at the higher endpoint. A least-prime weight multiplies its cost by $O(L^{a_i})$ in either case. Hence the product of the ordinary lower factors has size $O(L^{2\Delta}/\ell^{2j_H})$; marks on one or both slots add only the stated powers.

## 2. True tails and affine depth

Set $B=0$ if there is no higher endpoint, $\varepsilon=(20-B)/4$, and $H=20-B-2\varepsilon>0$. In each power-log slot we may remove lower products $>\exp(\varepsilon T)$ with error $O_A(NL^{-A})$ at every target. The true absolute divisor marks cost at most $L^{1+\nu}\tau(s)$ per side, since the rough part has at most $\ell/C$ prime factors. Cauchy on the genuine sum line and counting multiples by $N/s$ reduce the tail to squared reciprocal sums. Their full Euler factors $1+4/p$ cost at most a power of $L$. In the discarded power-log slot Rankin at $L^{-b_i}$ gives a factor $\exp(-\varepsilon L^{1-b_i}/\ell)$, and its Euler product $1+4e/p$ still costs only a power of $L$. This absorbs every fixed log power. A higher endpoint retains its actual original cap without discarding any additional product on that side.

After truncation $st\le e^{(20-H)T}$, $s,t<D$, and $u,v>\sqrt N$. The exact double-switch branches of the sparse-band theorem depend only on these size conditions and the original signed identities. For the second difference and product mixed type freeze both proper rough labels $f,g$, with $h=sf,k=tg$. If a switch starts above D, its base product gives $fg\le Q$; otherwise in the second difference both $f,g\le D$. For the D-type mixed term freeze only the switched proper rough part and both lower products; its switched rough part is $\le D$. The light–light term freezes only $s,t$. Thus all the same true freezes satisfy $hk\le Ne^{-HT}$ for large $N$. Every remaining product is nonempty and has no prime factors below $Y=\exp(CT)$.

Use the affine rough sieve of the [rough-complement theorem](r65-source-pointwise-rough-complements.md) at $Z=e^{HT/24}$, $z=Z^\eta$ for fixed $0<\eta<\min(\eta_0,24C/H)$, so $z<Y$ and $\log z\asymp T$. Here $\eta_0$ is its absolute small constant. On each genuine frozen pair its coprimality, determinant $N$, and hard interval $|I|/(hk)$ are unchanged. Its upper bound is a main term $O(\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)/(hkT^2))$ and an error $O(Z^6)$. There are $O(Ne^{-HT}L)$ ordered frozen integer pairs, uniquely split into lower and rough factors by the disjoint ranges. On the retained lower products $\tau(s)\tau(t)=e^{o(T)}$ by splitting their prime factors at $\sqrt T$; any omitted true rough labels cost at most $L^{2\nu}$. With $O(L^2)$ mark size, the total error is $N\exp(-(3H/4-o(1))T)=O_A(NL^{-A})$. This does not require a long hard interval.

## 3. Pointwise summation with the two marked moments

As in the [growing rough arity bound](r65-source-growing-rough-arity.md), unrestricted rough reciprocal mass is $O_C(\ell)$, a log strip of width $W$ costs $O_C((1+W)\ell^2/L)$, and frozen rough factors of $\lambda^*$ are bounded. In taking positive upper bounds retain the true signed second or first differences before reading off these supports. The second difference requires switches in both directions. We can therefore read its conditional strip on the side with the smaller exponent $a_*$, retaining one of its at most two opposite-bit choices. The width is exactly the logarithm of that side's actual least prime (with a harmless endpoint unit in its reciprocal bound). In the mixed terms the switch pays such a strip on its own side, with a separate actual light least-prime log on the other. In the two-light term both least-prime logs remain but there is no strip.

Consequently, after factoring out $\mathfrak S(N)|I|$ and $L^{2\Delta}/\ell^{2j_H}$, the respective positive main bounds are

$$
 \begin{array}{ll}
 \text{second difference:}& O_C(\ell^5L^{-1+a_*}),\\
 \text{mixed product type:}& O_C(\ell^5L^{-2+a_1+a_2}),\\
 \text{mixed D type:}& O_C(\ell^4L^{-2+a_1+a_2+\nu}),\\
 \text{light--light:}& O_C(\ell^2L^{-2+a_1+a_2+2\nu}).
 \end{array}
$$

Indeed the first uses $L^2/T^2$, the thin strip $\ell^2/L$, an opposite unrestricted rough reciprocal $\ell$, and its marked factor $L^{a_*}$ from (3). The next two trade one heavy $L$ for a marked lower factor; only the D type omits an opposite rough label and so pays $L^\nu$ instead of its rough reciprocal. The last has two light marks, no strip, and at most $L^{2\nu}$ unfrozen rough labels. Summing these bounds with the lattice errors and true tails gives (2). No conditioning on the least prime has been transferred to a distribution statement about the actual affine rough variables.

There are genuine nonzero witnesses: choose one lower prime per side strictly inside each moving log interval at an external scale $X$, using a fixed proportional exponent $<B$ times $T_X$ if higher. Choose two distinct rough primes on each side near the square root of its required rough product $X/(2s)$ or $X/(2t)$, and make all primes distinct. The PNT supplies them in narrow proportional windows. Their central even sum is comparable to $X$ and preserves the interior lower bounds. All these rough primes exceed D and any cross-product exceeds Q, since the lower logarithms total at most $BT+o(T)$, with $B<20$. Both signed lower orbits thus have mark minus their lower prime logarithm summed over the nonempty rough labels, and the actual summand is $-\log s\log t$. This is not a lower bound for the signed sum.

The positive moment argument does not turn (1) into an estimate for arbitrary dense widths: the factors $L^{2\Delta}$ are genuinely present in the reciprocal upper profiles, and $\chi$ can become nonpositive. Nor does it treat two higher endpoints or the full source operator. Those exclusions are not replaced by a claim about main terms or Goldbach.
