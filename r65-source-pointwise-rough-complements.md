# Affine rough complements: pointwise medium-factor control at every rough arity

Keep the genuine signed central sum (1), strict thresholds $D,Q$, central window $I_0$, exact $N$-units and fixed parameters of the [two-rough-prime theorem](r65-source-pointwise-two-rough.md). As there, write $L=\log N$, $T=L/\log L$. The integers are still squarefree, $n=su$, $m=tv$, and the lower prime alphabets are bounded by $\exp(L^{\alpha_1})$ and $\exp(L^{\alpha_2})$. The extension is that $u,v$ now each have **any positive number of rough primes**, all $\ge N^\kappa$. At least one lower product is nonempty (greater than one); the other may be one. If a slot is specifically required to have empty lower product, set its $\alpha_i=0$ for the estimate only. As before the positive exponents and $0<\kappa<1/4$ are fixed, and additional integer masks may not distinguish the interior divisor labels.

**Theorem (unconditional, pointwise).** If $\sigma=1-2\alpha_1-2\alpha_2>0$, then for every fixed $A>0$, every sufficiently large even $N$, and every hard $I\subseteq I_0$,

$$
 |R_N(I)|\ll_{\rho,\kappa,\alpha_1,\alpha_2,A}
     \mathfrak S(N)\bigl(|I|(\log L)^2 L^{-\sigma}+NL^{-A}\bigr).
 \tag{1}
$$

For either slot, allowing both possibilities for its lower product is covered by splitting into its nonempty case and its empty case, provided both are not empty simultaneously. The latter case is not asserted. There is no exceptional set or main-term assertion. The higher sparse bands $\exp([c,C]L/\log L)$ of the first-moment papers, unrestricted intermediate factors, nonsquarefree inputs, and Hypothesis S remain outside the scope.

## 1. An upper sieve for affine rough integers

The preceding two-rough-prime theorem used an affine-prime bound for two remaining factors. Its unweighted square sieve only needs those factors to have **no prime divisors $\le z$**. Fix coprime frozen $h,k$ with $(hk,N)=1$ and count eligible integer pairs $P,V$ on $hP+kV=N$, $hP\in I$. For a remaining true nonempty rough product all its prime factors are $\ge N^\kappa$. Choosing the same $Z=e^T$ and $z=Z^\eta$ with fixed sufficiently small absolute $\eta>0$ gives $z<N^\kappa$ for large $N$. Hence the true remaining products are counted by the positive sieve even when composite. In detail the affine forms $P=P_0+k j$, $V=V_0-h j$ have determinant $N$ up to sign and interval length $|I|/(hk)$. Their product has a single root modulo $\ell$ if $\ell\mid hk$, or if $\ell\mid N$; otherwise it has two. At $2$ the single-root case always holds. These are the identical local factors for the same forms, not an assertion of any distribution of smooth or rough numbers in residues.

The squared Selberg weights in §1 of the two-rough-prime theorem give their upper pointwise divisor majorant equal to one on integers whose two forms have no prime factors $\le z$. Its main denominator is at least a constant times the full truncated Euler value, by the same $\log d$ expectation and small fixed $\eta$. The lattice error is $O(Z^6)$, by the bounds on the number of weights, their individual magnitudes and the root count on their least common multiple. Thus its bound (4) holds with $P,V$ any such rough integers:

$$
 O_\kappa\!\left(
     \frac{\mathfrak S(N)|I|}{hk T^2}\lambda^*(h)\lambda^*(k)
          +e^{6T}\right),\qquad
 \lambda^*(h)=\prod_{\substack{\ell\mid h\\ \ell>2}}
                 \frac{\ell-1}{\ell-2}.
 \tag{2}
$$

Nothing about composite $P,V$ other than this absence of small primes was inserted into the sieve. Hard endpoints enter through the same residue-floor errors. The true unit conditions imply the requisite frozen coprimalities, since a prime shared by $h,k$ would divide $N$.

At fixed $\kappa$ each whole rough part has at most $K=\lfloor1/\kappa\rfloor$ factors, from its size $\le N$, hence at most $2^K$ divisor labels. The large-lower-product tail of §1 of the two-rough-prime theorem, deleting $s>e^T$ or $t>e^T$, therefore still costs $O_A(NL^{-A})$: its pointwise Cauchy calculation used only a bounded number of rough labels and the genuine lower moments of $\tau(s)^2$ and $\tau(t)^2$. The constants now depend on $K$. With an empty lower side its squared divisor profile is simply one before the fixed rough multiplicity. Thus we can work with $s,t\le e^T$ below. In particular $s,t<D$ and $u,v\ge\rho N e^{-T}>\sqrt N$.

## 2. Both lower products nonempty

Keep exactly the algebraic double switch (5) of the two-rough-prime theorem: $a=P^-(s)$, $b=P^-(t)$, $x=cf$, $y=d'g$, with $c\mid s/a$, $d'\mid t/b$, $f\mid u$ and $g\mid v$. The four indicators $J_{\epsilon\eta}$ and the actual signed terms are unchanged. By the same argument empty and full rough labels cannot switch. Thus a switching label is proper and nonempty, but can now be a product of several rough primes. Its complementary rough part is therefore also nonempty, and (2) applies to that **whole** complement.

For the second difference $J_{00}-J_{10}-J_{01}+J_{11}$ there must be a switch in each direction. If either switch starts above its D boundary then the product condition gives $fg\le Q$; otherwise $f,g\le D$. Freeze $h=sf,k=tg$. As before $hk\le st\max(Q,D^2)\le N e^{-18T}$. The remaining $u/f,v/g$ are now used as the positive integers $P,V$ in (2). Fix one admissible first-side switch as in (6) of that theorem. For each choice of $s,t,c,d',g$ and opposite bit it gives one interval of width $\log a$ on $\log f$, with center independent of the remaining affine integers.

In the right mixed term with left weight $\log a$, a product switch again gives $fg\le Q$, both labels are proper and nonempty, and the same freeze $sf,tg$ applies, using the interval of width $\log b$ on $\log g$. If instead the right base $y=d'g$ is $\le D$, its switch forces $D/b<y\le D$. Freeze $k=tg$, but on the left now use $h=s$: the whole $u$ is an eligible rough integer. Then $hk\le stD\le N e^{-18T}$. The thin D interval on $\log g$ is independent of the left rough label, which can be dropped at the cost of at most $2^K$ choices. Exchange the sides for the other mixed term. All case bounds come from the exact switches, including strict shifted endpoints.

If a nonempty rough product $f$ is restricted to an interval of width $W$ in its logarithm, its total reciprocal mass is $O_\kappa((1+W)/L)$. To verify this, for each number of factors $1\le j\le K$ allow all ordered tuples in the upper bound, fix $j-1$ primes and apply the ordinary reciprocal-prime bound for a log interval of width $W$ to the last. The other rough reciprocals sum to $O_\kappa(1)$ per axis. The total unrestricted rough reciprocal mass including the empty product is also $O_\kappa(1)$. Thus every strip still gives the same reciprocal saving as with singleton rough labels. The factors in $\lambda^*(h)\lambda^*(k)$ contributed by rough primes now cost at most $2^{2K}$; the lower-prime factors are kept exactly in the positive profile. Formula (8) of the two-rough-prime theorem continues to bound the lower profiles with either a plain or a least-prime logarithmic weight by $O((\log(2y_i))^2)$.

For the two-light term, do not use a physical Cauchy bound. Freeze only $h=s,k=t$ and apply (2) to the two entire rough parts, dropping the residual $J_{11}$ only after taking its positive upper bound. The total original rough label multiplicity is at most $2^{2K}$, and the weights are $\tau(s)\log a$ and $\tau(t)\log b$. The same lower profiles yield a main bound $O(\mathfrak S(N)|I|L^{2\alpha_1+2\alpha_2}/T^2)$ with no loss from the length of $I$. This is smaller by a factor $1/L$ than the claimed scale. For switched terms the second-difference weight is $\le L^2$, while each mixed term has only one heavy $L$ and one least-prime log. The strips contribute $1/L$ and a single least-prime log on their own side. Thus all switched main sums are

$$
 O_\kappa\!\left(\mathfrak S(N)|I|
            \frac{L^2}{T^2}L^{-1+2\alpha_1+2\alpha_2}\right).
 \tag{3}
$$

In all these applications $hk\le Ne^{-18T}$ for large $N$, including the two-light case where $hk\le e^{2T}$. The number of ordered integer pairs $h,k$ in this envelope is $O(Ne^{-18T}L)$. Each frozen cofactor has a **unique** split into lower and rough primes because their ranges are disjoint, even when the rough part is empty or a product. For fixed cofactors the omitted rough products enter as the two affine variables; there is no factorization weight on either variable beyond the original bounded number of labels and the at most $\tau(s)\tau(t)\le e^{2T}$ lower choices. With weights at most $L^2$, the total lattice error is $O_\kappa(Ne^{-10T}L^3)=O_{\kappa,A}(NL^{-A})$. Together with (3) and the genuine tail this proves (1) for both lower products nonempty.

## 3. One lower product empty

Suppose $s>1$, $t=1$; a reflected hard interval handles the other order. Fix each actual long opposite label $e=g\mid v$, $g>D$. The one least-prime toggle on $s$ is exactly the [least-prime switch](r64-source-least-prime-toggle-first-moment.md). With $x=cf$, $a=P^-(s)$, it gives a heavy factor $\log(n/x)$ on the switch $x\le \mathcal T_g<ax$, $\mathcal T_g=\max(D,Q/g)$, and an unswitched light upper weight $\log a$; each still multiplies the actual signed opposite divisor weight. If $x\le D$, the switch entails $D/a<x\le D$. Freeze $h=sf$ and $k=1$, leaving all of $v$ on the right, and use the short D strip on $f$. The omitted opposite divisor labels number at most $2^K$. If $x>D$, the switch entails $fg\le Q$; the opposite label $g$ cannot be full, since then $g=v>\sqrt N$ and the product cutoff passes whenever $x>D$. So freeze $h=sf,k=g$, with both complements nonempty, and use the log strip of width $\log a$ on $f$ for fixed $g$. Both freezes satisfy $hk\le Ne^{-18T}$, the required coprimalities, and the same matrix residue proof.

In the light term leave both whole rough products by freezing $h=s,k=1$. The weight of the unfrozen opposite label is at most $L$, with at most $2^K$ choices, while the first label contributes $\tau(s)\log a$. The main bound is $O_\kappa(\mathfrak S(N)|I|\,L T^{-2}L^{2\alpha_1})$, which is exactly of the allowed order. The heavy term has a single short strip, both logs bounded by $L$, and the same order from (8) of the two-rough-prime theorem. For all freezes the lattice errors are bounded by the preceding integer-pair argument. This proves (1) with $\alpha_2=0$.

All bounds apply after the exact signed single or double switches, then enlarge only positive envelopes. The fixed polynomial lower bound for each rough prime, the subpower range of each lower alphabet, and the original retuned parameters are essential to the displayed quantitative estimates. No result about the complete operator or all arithmetic sectors is implied.
