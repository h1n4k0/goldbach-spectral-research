# Pointwise unanchored sparse-band pairings

Keep the original central interval $I_0=[\rho N,(1-\rho)N]$, a hard interval $I\subseteq I_0$, the squarefree unit masks and the genuine negative sum line of the [rough-complement theorem](r65-source-pointwise-rough-complements.md). In particular $L=\log N$, $\ell=\log L$, $T=L/\ell$, $D=\lfloor\sqrt N e^{-20T}\rfloor$, $Q=\lfloor N e^{-20T}\rfloor$. On the two slots put $n=su$, $m=tv$. The lower products $s,t$ are both nonempty; **all** their factors are in the indicated sparse bands, and neither slot has a small-prime anchor. The nonempty rough products have all primes at least $Y=\exp(CT)$, where $C>0$ is fixed. Allow any factor counts and further masks on the true integers that do not change the interior divisor labels.

For each slot choose fixed $0<c_i<d_i$ and one of the two types below.

- **Power-log band.** For fixed $0<\vartheta_i<1$, take all its lower primes in $[\exp(c_i L^{\vartheta_i}),\exp(d_i L^{\vartheta_i})]$. There is no product cap.
- **Higher band.** Set $\vartheta_i=1$ for exponent bookkeeping, take all lower primes in $[\exp(c_i T),\exp(d_i T)]$, and impose the genuine whole-product cap $\exp(BT)$ with fixed $c_i<B<20$. In this case choose $C>d_i$.

At **most one** slot is higher. Thus $\vartheta_*=\min(\vartheta_1,\vartheta_2)<1$. The lower and rough ranges in each slot are disjoint for sufficiently large $N$.

**Theorem (unconditional, pointwise).** Write $\nu=\log 2/C$ and require $2\nu<2-\vartheta_1-\vartheta_2$. Let

$$
   \chi=\min(1-\vartheta_*,\ 2-\vartheta_1-\vartheta_2-2\nu)>0.
$$

Then the genuine signed contribution

$$
 R_N(I)=-
 \sum_{\substack{n+m=N,\ n\in I,\ m\in I_0\\
                  (nm,N)=1,\ n,m\ {\rm selected}}}
    \ \sum_{\substack{d\mid n,\ e\mid m\\d>D,\ e>D,\ de>Q}}
                   \mu(d)\mu(e)\log(n/d)\log(m/e)
$$

satisfies, for every sufficiently large even $N$, every hard $I$, every admitted integer mask and each fixed $A>0$,

$$
       |R_N(I)|\ll \mathfrak S(N)
              \left(|I|\ell^5 L^{-\chi}+NL^{-A}\right).
 \tag{1}
$$

Constants may depend on the fixed parameters. Both slots can have gap primes arbitrarily closer to the endpoint $\vartheta_i=1$ in their respective fixed power-log bands, by choosing $C$ accordingly. A genuine capped higher band may interact with a strictly smaller power-log band; two higher bands are not covered. This is a **sparse-band** bound, not a union estimate for the continuous gap between the band scales, a fixed-target main term, or Hypothesis S.

## 1. Bounded reciprocal weight despite a large least prime

Each sparse lower band has $\sum_p 1/p=O(1)$ by Mertens: the ratio between its two endpoint logarithms is the fixed constant $d_i/c_i$. It follows that each unmarked lower profile

$$
     \sum_{\substack{w\ \mathrm{squarefree}\\p\mid w\ \Rightarrow p
                   \mathrm{\ in\ the\ band}}}
                 \frac{\tau(w)\lambda^*(w)}w
$$

is $O(1)$ by Euler products, where $\lambda^*(w)=\prod_{p\mid w,\ p>2}(p-1)/(p-2)$. Inserting $1+\log P^-(w)$ for $w>1$ costs at most $O(L^{\vartheta_i})$, since this is a bound even for the largest prime logarithm in that band. For the higher slot this overbounds its logarithm $O(T)$ by $O(L)$ and they are not set equal. The bounded reciprocal mass, unlike a small least prime, is the source of the improved exponent in (1).

If a slot is power-log, we may discard its product above $\exp(\varepsilon T)$ at a superlogarithmic cost at each target. Let $B=0$ if there is no higher slot, and choose $\varepsilon=(20-B)/4$. Each true rough part has at most $\ell/C$ prime factors and at most $L^\nu$ divisor labels. The absolute original weight is $O(L^{1+\nu}\tau(s))$ or $O(L^{1+\nu}\tau(t))$. Cauchy on $n+m=N$, with multiples counted at most $N/w$ for a fixed lower product $w$, reduces the discarded weight to the squared reciprocal tail of $\tau(w)$ on that side and its total moment on the other. The latter is $O(1)$ because the band is sparse, even if it is higher. On the power-log side Rankin with parameter $(d_i L^{\vartheta_i})^{-1}$ gives

$$
 \sum_{\substack{w>\exp(\varepsilon T)\\p\mid w\Rightarrow p\ \mathrm{in\ band}\\
                         w\ \mathrm{squarefree}}}\frac{\tau(w)^2}{w}
   \ll \exp(-\varepsilon T/(d_i L^{\vartheta_i}))
                     \prod_{p\ \mathrm{in\ band}}(1+4e/p)
   \ll \exp(-\varepsilon T/(d_i L^{\vartheta_i})).
$$

Its exponential absorbs the polynomial weights $L^{2+2\nu}$ and every fixed further log power. No tail on the higher side is asserted or taken: its cap is an original mask.

The retained products have $st\le \exp((B+2\varepsilon)T)$, both $<D$, and $u,v>\sqrt N$. Write $H=20-B-2\varepsilon>0$. The true rough reciprocal profile and thin-strip profile are $O_C(\ell)$ and $O_C((1+W)\ell^2/L)$ for log width $W$ by the [growing-arity theorem](r65-source-growing-rough-arity.md). True frozen rough factors in $\lambda^*$ remain bounded: there are at most $\ell/C$ of them, each $\ge Y$. Unfrozen rough labels cost $L^\nu$ per operand only when omitted in an upper bound.

## 2. Retain the double switch and the precise masks

Use the actual signed double least-prime switch of the rough-complement theorem; both least primes are now in their sparse bands. For a genuine second difference, each side has a transition with the opposite bit fixed. When either switching base is above D the original product condition forces $fg\le Q$ for the two proper rough labels $f,g$; otherwise both $f,g\le D$. Freeze $h=sf,k=tg$, leaving two nonempty rough complements. **Either** side's transition gives the true log strip, at one of two possible positions fixed by its opposite label. Choose the side with $\vartheta_*$ so the width is $O(L^{\vartheta_*})$. This choice uses simultaneous support of both switches, not a gain claimed when only one side switches.

A mixed term at a product edge also freezes both proper rough labels and uses a strip on the switching side. At a D-type mixed edge the switching base is $\le D$ and within a factor of its own least prime of D; it freezes only that rough label along with the lower products, omitting at most $L^\nu$ rough labels on the other side. The light–light term freezes only $s,t$ and omits at most $L^{2\nu}$ rough labels. These are the same exact switch identities, so the initial signs and strict shifted endpoints are unchanged.

The four types of freezes satisfy $hk\le st\max(Q,D^2)$, $hk\le stD$, or $hk=st$, hence always $hk\le Ne^{-HT}$ for large $N$. The affine rough-integer upper sieve is legal with $Z=e^{HT/24}$, $z=Z^\eta$ for fixed $0<\eta<\min(\eta_0,24C/H)$, where $\eta_0$ is its small absolute sieve constant. Thus $z<Y$ and it applies to the actual rough complements. On exactly the true frozen coprimalities $h,k$ are coprime to one another and to $N$ by the unit masks, and the determinant is $N$. The main upper bound is $O(\mathfrak S(N)|I|\lambda^*(h)\lambda^*(k)/(hk T^2))$; the error per frozen pair is $O(Z^6)=O(e^{HT/4})$ including the hard endpoints. The $O(Ne^{-HT}L)$ frozen pairs split uniquely into their lower and rough parts. Since any squarefree lower product at most $\exp(O(T))$ has at most $\sqrt T+O(T/\log T)$ prime factors (split at $\sqrt T$), lower labels contribute $e^{o(T)}$ to the error. Unfrozen rough labels are at most $L^{2\nu}$, marks at most $L^2$, and the summed error is $O_A(NL^{-A})$. Drop other masks only in positive enlargements after the exact switch and the genuine frozen local conditions.

## 3. The four positive main bounds after switching

After division by $\mathfrak S(N)|I|$ in the sense of main coefficients, the bounds are

$$
 \begin{array}{rll}
 \text{second difference:} && \ell^5L^{-1+\vartheta_*},\\
 \text{mixed product type:} && \ell^5L^{-2+\vartheta_1+\vartheta_2},\\
 \text{mixed D type:} && \ell^4 L^{-2+\vartheta_1+\vartheta_2+\nu},\\
 \text{light--light:} && \ell^2L^{-2+\vartheta_1+\vartheta_2+2\nu}.
 \end{array}
$$

For the first, use heavy logs $L^2$, sieve $T^{-2}$, the smaller side's strip $\ell^2 L^{-1+\vartheta_*}$ and the other rough reciprocal cost $\ell$. In a mixed term the switching width pays its own exponent $\vartheta_i$ and the actual light least-prime log pays the other, replacing one heavy $L$. The D-type term has no free opposite rough reciprocal factor $\ell$ but pays its $L^\nu$ unfrozen-label cost. The light–light term has no strip and no frozen rough reciprocals, but pays two least-prime logs and the two unfrozen-label costs. Both unmarked lower profiles are bounded, as proved above. These rows, the tail and lattice error prove (1). In the mixed higher/power-log case positivity of $\chi$ comes from the strictly smaller exponent on one side; it is not a claim of cancellation for two higher bands.

For a nonzero genuine witness, choose one lower prime in each band at an interior point of its exponent range (and below the cap when higher). About an external scale $X$, on each side choose two distinct rough primes near $\sqrt{X/(2s)}$ or $\sqrt{X/(2t)}$ respectively, using all distinct prime factors. The ordinary PNT supplies the choices in fixed sufficiently narrow proportional windows; the resulting even $N$ has the two integers central and coprime to $N$. The moving endpoint conditions hold by keeping the lower prime exponents in the interior of their bands. The rough primes all exceed $D$ and any cross-product of one from each side exceeds $Q$: the sum of the two lower logarithms is $\le B T+o(T)$ if one band is higher and $o(T)$ otherwise. This leaves a strict margin since $B<20$. Each nonempty rough subset then has a complete lower orbit against every admitted opposite divisor, of mark $\mu(f)\log s$ or $\mu(g)\log t$. The sum over nonempty rough subsets has total Möbius weight $-1$ on either side. Thus the genuine pair contributes $-\log s\log t$. The witness establishes nonvacuity only, not an aggregate lower bound.

If both bands are at the higher scale, the smaller-side strip does not supply the required polynomial log saving. If one replaces a sparse band by the complete interval between two separated log exponents, its lower reciprocal Euler products need not be bounded. Neither extrapolation is made in (1).
