# Short-log kernels for the two-positive odd-disjoint exceptional mode

This gives exact real kernels in the [two-positive unsigned remainder](r106-spectral-odd-disjoint-two-positive-unsigned-mode.md). Integrating one real logarithmic coordinate and using the symmetry of the two genuine signed short labels leaves only two scalar kernels. If a stated target-local margin below the original denominator cap holds, the arithmetic at every prime outside the conductor is the ordinary binary reciprocal model. The extra conductor dependence is then one explicit finite signed shift operator. Neither formula assigns a sign or relative smallness to the resulting signed short sum. It does not give a pointwise parity sign or assert the existence of an exceptional zero.

Use exactly the odd-disjoint hypotheses of the two-positive unsigned theorem: genuine even $Y\le N\le2Y$, odd squarefree primitive Page conductor $r\le Q_0$ coprime to $N$, actual real simple zero $\beta$ in the original Page strip, $G=\log Y$, $L=\log N$, $Q_0=\exp(16\sqrt G/\log G)$, $S=Y^{1/10}$. The true $D=\sqrt N L^{-B}$ and $H_0=\sqrt N L^{-B_0}$ have the same fixed admissible $B>B_0>0$. The real hard half-open interval $I\subset(N/2,9N/16]$ and bounded pointwise-BV test $\omega$ are unchanged. Write $m\in N-I$ for the actual continuous product coordinate; this automatically lies in $[N/3,2N]$. Put

$$
    L_m=\log m,\qquad
    \Delta_m=\tfrac12\log m-\log D,\qquad
    U=\log(H_0/D),\qquad
    F(m)=\omega(N-m)(N-m)^{\beta-1}.
$$

We have $\Delta_m>U>0$ for all sufficiently large $Y$ and all these $m$, since $\Delta_m-U=B_0\log L+\tfrac12\log(m/N)$. For $x,y\ge0$ let $K=\Delta_m-(U-\max(x,y))_+$ and define the two symmetric kernels

$$
 \begin{split}
 k_{0,m}(x,y)&=\frac{K^2-|x-y|K}{L_m},\\
 k_{1,m}(x,y)&=-\frac{|x-y|\min(\Delta_m,|x-y|/2)}{L_m}.
 \end{split}                                                       \tag{1}
$$

**The literal finite formulas.** With $A_r^{[2]}$, $V_r^{[2]}$, $b_{p,h}^{[2]}$ from the two-positive theorem, its exact real remainders $\mathcal P_i$ satisfy

$$
 \mathcal P_i
  =\int_{N-I} F(m)
       \sum_{\substack{u,v\le S\\u,v\ {\rm sf},\ (u,v)=1}}
       \frac{\mu(u)\mu(v)}{uv} A_r^{[2]}(uv)V_r^{[2]}(uv)
          k_{i,m}(\log u,\log v)
       \sum_{\substack{t\le Q_0/r\\t\ {\rm sf},\ (t,r)=1}}
          \prod_{p\mid t}b^{[2]}_{p,uv}(N)\,dm .                   \tag{2}
$$

Here $(u,v)$ are $(b,c)$ in color 0 and $(a,d)$ in color 1. This equality involves no completion of the rational cap and no added $(uv,N)=1$ condition.

**A completed algebraic model.** Define

$$
 \mathcal A_{N,r}=\sum_{\substack{p\mid N\\p\nmid r}}p^{-3/4},
 \qquad
 \mathcal V_{N,r}=\prod_{\substack{p\nmid r\\p\mid N}}(1-1/p)
                    \prod_{p\nmid rN}(1-2/p^2).
                                                                    \tag{3}
$$

For a squarefree integer $u$ prime to $rN$ put
$\alpha^\circ(u)=\prod_{p\mid u}(p-1)/(p^2-2)$, with $\alpha^\circ(1)=1$. These are the ordinary reciprocal weights in the [ordinary mixed cap](r80-spectral-whole-mixed-parity-density.md). For two-variable functions define the positive-coordinate shift operators by $T_{1,h}f(x,y)=f(x+h,y)$ and $T_{2,h}f(x,y)=f(x,y+h)$. Set

$$
 \begin{split}
  \mathscr C_r&=\prod_{p\mid r}
       \left(\operatorname{Id}
         -\frac{p-1}{p-2}T_{1,\log p}
         -\frac{p-1}{p-2}T_{2,\log p}\right),\\
  f_{i,m}(x,y)&=\mathbf1_{x\le\log S,\ y\le\log S}\,k_{i,m}(x,y),\\
  \Theta_{i,m}
    &=\sum_{\substack{u,v\ {\rm sf},\ (u,v)=1\\(uv,rN)=1}}
       \mu(u)\mu(v)\alpha^\circ(u)\alpha^\circ(v)
                  (\mathscr C_r f_{i,m})(\log u,\log v),\\
  \widehat{\mathcal P}_i&=\mathcal V_{N,r}\int_{N-I} F(m)\Theta_{i,m}\,dm .
 \end{split}                                                       \tag{4}
$$

The displayed sum actually vanishes outside $u,v\le S$, since all shifts are nonnegative and the physical short-label conditions apply **after** the conductor shift.

There is a fixed $C$ for which

$$
 \bigl|\mathcal P_i-\widehat{\mathcal P}_i\bigr|
 \ll Y^\beta G^C
        \exp\bigl(C\{\omega(r)+\mathcal A_{N,r}\}\bigr)(Q_0/r)^{-1/4}.
                                                                    \tag{5}
$$

Here $\omega(r)$ counts distinct prime divisors, not the physical weight $\omega$. In particular, for each fixed $A>0$ one can replace the $\mathcal P_i$ of the true exceptional formula (5) of the two-positive result by $\widehat{\mathcal P}_i$ with additional error $O_A(|\gamma_N|Y^\beta G^{-A})$ if for a sufficiently large $C_A$,
$\log(Q_0/r)\ge C_A[\log G+\omega(r)+\mathcal A_{N,r}]$.
The existing raw error $O(Y^\beta G^C Q_0^{-1})$ and the two signed-pole colors are not altered. This does not make an arithmetic claim for denominators beyond the original $Q_0$.

## 1. Evaluate one real coordinate on the literal hard slices

For fixed genuine short labels of product $h$, write the two positive coordinates as $v>0$ and $w=m/(hv)$. The Jacobian is $(1/h)\,dm\,d\log v$. In color 0 the short labels are $u=b,v_{\rm s}=c$; in this paragraph the real logarithmic coordinate is $\log a$. Set $x=\log b,y=\log c$, $s=\log(a\min(b,c)/D)$. The actual lower tests give $s>0$ and $s>U-\max(x,y)$, since $abc=a\min(b,c)\max(b,c)$. The strict real upper test $\min(ab,ac)<\sqrt m$ gives $s<\Delta_m$. The mark becomes

$$
      1-\frac{2\log(ac)}{L_m}
        =\frac{2}{L_m}\bigl(\Delta_m-s-y+\min(x,y)\bigr).
$$

Thus its integral on this actual logarithmic interval is
$[K^2-2(y-\min(x,y))K]/L_m$. Interchanging the two actual short coordinates does not change any coefficient depending on $h$, the true hard short cut, the other gates, or the physical weight. Average the two orderings. The average mark integral is $k_{0,m}(x,y)$ since
$(x-\min)+(y-\min)=|x-y|$.

For color 1 the short labels are $a,d$ and the positive coordinates are $b,c$. The high gate is automatic: $abc=m/d\gg Y^{9/10}>H_0$ on the actual range. Let $x=\log a,y=\log d$ and $q=(x-y)/2$. Put $\ell_m=\tfrac12\log(m/(ad))$ and $t'=\log b-\ell_m$ (distinct from the rational label $t$). Then $\log c=\ell_m-t'$. The true two lower tests become $|t'|<\Delta_m+q$, and the true upper test on the minimum becomes $|t'|>q$. If $q<0$ the latter is automatic, and if $q=0$ it only removes an isolated point. The retained length is therefore $2(\Delta_m+q-\max(0,q))_+$, with symmetry under $t'\mapsto-t'$. The genuine mark is $2(t'-q)/L_m$. Its integral is

$$
       -\frac{4q}{L_m}(\Delta_m+q-\max(0,q))_+.
$$

For the swapped short pair $q$ is replaced by $-q$, and all arithmetic factors and test weights are unchanged. Averaging these two values gives $-2|q|\min(\Delta_m,|q|)/L_m=k_{1,m}(x,y)$. These continuous endpoints may be dropped only as null sets of the integral, not from the actual discrete tuple definition. The original envelope $v,w>S$ is automatic in this signed-short domain, by the earlier exact two-positive reduction. Restoring $1/h$ and the original physical test proves (2).

## 2. Complete the contracted arithmetic sum only under a controlled error

Set $\vartheta=1/4$. At fixed true $h=uv$ the absolute $\vartheta$-moment of the $t$ coefficients in (2) is bounded by
$\prod_{p\nmid r}(1+p^\vartheta|b_{p,h}^{[2]}(N)|)$.
This is on the already contracted $q\mid t$ coefficient, not on the two separate numerator choices. Use the unoccupied factors for all primes first. Outside $N$ they cost $1+O(p^{\vartheta-2})$, and at $p\mid N,p\nmid r$ they cost $1+O(p^{\vartheta-1})$. Their combined product is $O(\exp(C\mathcal A_{N,r}))$. To accommodate occupancy $p\mid h$, insert positive extra factors $1+w_p$ on $p\nmid r$ with $w_p=O(p^{\vartheta-1})$ outside $N$ and $w_p=O(p^\vartheta)$ inside $N$. The estimates include $p=2$ by enlarging the fixed constants.

On the physical support $\Delta_m=O(\log G)$, $L_m\asymp G$, and $|x-y|\le\log S=O(G)$ for the true short pair. Thus each kernel has absolute bound $G^C$, and the physical integral costs $O(Y^\beta G^C)$ before its reciprocal $1/(uv)$. For an absolute upper bound only, discard the finite output restrictions except the prime range $p\le S$ and the fact that a prime cannot occupy both short slots. Since $V_r^{[2]}(h)\le1$, the remaining reciprocal short sum with the occupancy extras is at most

$$
 \prod_{\substack{p\le S\\p\nmid r}}\left(1+\frac{2(1+w_p)}p\right)
       \prod_{p\mid r}\left(1+2\frac{p-1}{p-2}\right)
    \ll G^C\exp\bigl(C\{\omega(r)+\mathcal A_{N,r}\}\bigr).
                                                                    \tag{6}
$$

The ordinary reciprocal product costs a power of $G$ by the prime harmonic bound; after its removal the extra outside-$N$ increments are summable, and the inside-$N$ increments give the declared moment. The factor $A_r^{[2]}(p)/p=(p-1)/(p-2)\le2$ at each odd conductor prime is not replaced by a decaying reciprocal. Equations (2) and (6), with the Rankin factor $(Q_0/r)^{-1/4}$ on the omitted $t$, prove (5) for extending that sum to all squarefree $t$ coprime to $r$. No extension of a discrete arithmetic progression is used.

## 3. Identify the exact completed local arithmetic

For each fixed $h$ the completed $t$ sum is the absolutely convergent product $\prod_{p\nmid r}(1+b^{[2]}_{p,h}(N))$; the unoccupied factors outside $Nr$ differ from one by $O(p^{-2})$ and all other unusual primes are finite. No division by this product is needed at a zero. At a nonconductor prime write $U_p=1-1/p$. The local default in $V_r^{[2]}$ is $U_p^2(1+2/p)$ when unoccupied and $U_p^2$ when occupied by $h$. Multiplication by $1+b^{[2]}_{p,h}$ gives exactly

$$
 \begin{array}{c|cc}
             & p\nmid h &p\mid h\\ \hline
   p\mid N   & U_p      &0\\
   p\nmid N &1-2/p^2   &U_p .
 \end{array}                                                       \tag{7}
$$

For example the unoccupied denominator is $(p-1)^2(p+2)$, and adding its $p-2$ numerator for $p\nmid N$ produces $p^3-2p$, hence $1-2/p^2$. In the other unoccupied case multiplication by the $p\mid N$ factor gives $U_p$, including at the actual even prime $2$. The occupied dead factors at $p\mid N$ therefore impose the short-unit restriction only in the **completed** model. For $p\nmid rN$ dividing exactly one short label, its ratio of occupied to unoccupied weights, times the signed reciprocal factor $-1/p$, is $-(p-1)/(p^2-2)$. The entire unoccupied product is $\mathcal V_{N,r}$.

At $p\mid r$ assigning the prime to one short slot, as opposed to leaving it absent, has exactly the signed reciprocal factor $-A_r^{[2]}(p)/p=-(p-1)/(p-2)$. The actual coprimality forbids assigning that prime to both slots. Thus the finite product of translations in (4) is exact, with the cutoff evaluated on the actual shifted short logs. This proves (4) for the completed (2), so (5) compares their literal sizes. In the true exceptional formula the factor multiplying these errors has modulus $C_r^{[2]}/(2\varphi(r))\le|\gamma_N|/2$ on the odd-disjoint targets. This proves the claimed conditional error strength. The exact weighted kernels and signed conductor shifts leave a signed finite sum; none of these algebraic identities estimates its sign relative to the other color or its two-pole counterpart.