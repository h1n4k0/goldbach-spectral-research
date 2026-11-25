# The exact quadratic reference in the aligned Page formula

**Scope.** This evaluates the **uncapped quadratic reference** for the first color of the genuine aligned Page correction. The two long reciprocal-pole factors cancel against an exact second log-ratio moment of the actual finite short-label sum. It keeps the finite Ramanujan cutoff and its signs. This is not an estimate of the actual capped kernel, a bound for the complete exception, or a result on Hypothesis S.

Keep the notation and hypotheses of the [aligned two-pole formula](r92-spectral-aligned-exceptional-two-pole-formula.md): the possible primitive real Page character $\chi$ of conductor $r\mid N$, its real zero $\beta$, $Y\le N\le2Y$, $G=\log Y$, $Z=\sqrt G/\log G$, $Q_0=e^{16Z}$ and $H=Q_0/r$. Put $c_p=\chi(p)p^{-\beta}$ and $E_p=(1-c_p)^{-1}$ for $p\nmid r$. Use the exact factor $\mathcal L(uv;q,N)$ there, for squarefree $q$ prime to $r$. In the original first-color kernel $\mathcal G_0$, the numerator is $-\rho\min(T_x,\rho)/2$ with $\rho=|\log(u/v)|$. Here replace it by $-\rho^2/2$, and change no other arithmetic factor.

For a real short cutoff $U$, define the ordered true squarefree short sum

$$
 J_{q,U}=\!
 \sum_{\substack{u,v\le U,\ u,v\ {\rm sf}\\
                    (u,v)=1,\ (uv,r)=1}}
    \frac{\chi(uv)}{(uv)^\beta}\mathcal L(uv;q,N)
                                  (\log(u/v))^2 .
$$

The cutoff includes the original $U=Y^{1/10}$ and the smaller $U=Q_0^2/r$ from the [near-square-root confinement](r92-spectral-exceptional-balanced-square-root.md). Keeping $t\le H$ literally, put

$$
 C_{N,r}(H)=
   \sum_{\substack{t\le H,\ t\ {\rm sf}\\(t,r)=1}}
       \prod_{\substack{p\mid t\\p\mid N}}\frac1{p-1}
       \prod_{\substack{p\mid t\\p\nmid N}}\left(-\frac1{(p-1)^2}\right).
$$

**Theorem.** Uniformly for $Q_0^2/r\le U\le Y^{1/10}$,

$$
 \sum_{\substack{t\le H,\ t\ {\rm sf}\\(t,r)=1}}
       \frac{\mu(t)}{\varphi(t)}
       \sum_{q\mid t}q\,\mu(t/q)J_{q,U}
    =-2L'(\beta,\chi)^2 C_{N,r}(H)+O(G^C Q_0^{-1/40})
                                                                    \tag{1}
$$

with a fixed constant $C$. In particular the actual physical quadratic reference, defined by the substitution above in $\mathcal D_0$ of the aligned formula (3) with short cutoff $U$, equals

$$
 -\frac{r\chi(-1)}{\varphi(r)}C_{N,r}(H)
   \int_{N-x\in I}\frac{\omega(N-x)(N-x)^{\beta-1}x^{\beta-1}}{\log x}\,dx
            + O_A(Y^{2\beta-1}G^{-A})                              \tag{2}
$$

for every fixed $A>0$. One has an absolute $C_{N,r}(H)\gg1$ whenever $H\ge1$. Thus for nonnegative unit weight and a fixed-fraction physical interval, the reference has sign $-\chi(-1)$ and magnitude at least a constant times $Y^{2\beta-1}/G$ for all sufficiently large applicable scales. This sign is **only for the reference**; the difference between quadratic and capped log-ratio has not been bounded here.

## 1. Local algebra without dividing by any unoccupied factor

Use independent monomials $X,Y$ at a prime for its occupancy on the first and second short label, respectively. For every $p\nmid rq$ the exact local weights of no occupation and the two one-leg occupations in $J_{q,U}$, before the log-ratio moment, give

$$
 B_p(X,Y)= E_p^2(1-2c_p+c_pX+c_pY).
                                                                    \tag{3}
$$

Indeed the unoccupied weight is $1-p^{-2\beta}E_p^2=E_p^2(1-2c_p)$, using $c_p^2=p^{-2\beta}$; each occupied weight is $c_pE_p^2$. Mutual short coprimality is the reason there is no $XY$ in (3). For $p\mid q$, $p\nmid N$, the only term is the constant $B_p=E_p^2/(p-1)$. For $p\mid q$, $p\mid N$, it is the polynomial $B_p=c_pE_p^2(X+Y-2)$. At $p\mid r$ the local polynomial is identically one and $c_p$ can be set to zero.

Factor off the ordinary two character Euler factors by forming the correction polynomial

$$
 D_p(X,Y)=B_p(X,Y)(1-c_pX)(1-c_pY).
                                                                    \tag{4}
$$

This uses multiplication of polynomials only, in particular no inverse of $1-2c_p$ at $2$ or any other prime. At $X=Y=1$ the first type of $D_p$ is one; the two finite types are $1/(p-1)$ and zero respectively. Along $X=p^z,Y=p^{-z}$ the last type has a zero of order at least two at $z=0$, though only its value zero will be needed.

We make (4) an absolutely summable signed coefficient array, with norm $\|D\|_\delta=\sum_{a,b}|D(a,b)|(ab)^\delta$ in the integer variables corresponding to the monomials $X,Y$. It is a submultiplicative norm for the two-coordinate divisor convolution. Take the fixed $\delta=13/100$, and assume $\beta\ge .999$ (which holds on sufficiently large Page scales). For $p\nmid rq$, the constant deviation in $D_p-1$ is $-E_p^2c_p^2$; the linear and quadratic coefficients are $O(p^{-2\beta})$, and the cubic coefficients are $O(p^{-3\beta})$. This is an exact polynomial of total degree at most three. Its norm deviation is consequently

$$
      O(p^{-2\beta+2\delta}+p^{-3\beta+3\delta}).
$$

The sum over primes converges uniformly. At $p\mid q$, $p\nmid N$, the norm is at most $(p-1)^{-1}(1+O(p^{-\beta+\delta}))$; use $E_p^2$ in its absolute value and the two linear factors. At $p\mid q$, $p\mid N$, the norm is $O(p^{-\beta+\delta})$. Its ratio to $(p-1)^{-1}$ is $O(p^{1-\beta+\delta})$. Absorbing fixed constants per prime and the other factors into $O_\epsilon(q^\epsilon)$ (split primes at a sufficiently large constant) gives for the exact infinite coefficient array $D_q$

$$
   \|D_q\|_\delta\ll_\epsilon
                   \frac{q^{1-\beta+\delta+\epsilon}}{\varphi(q)}.
                                                                    \tag{5}
$$

The infinite product over primes outside $rq$ exists in this weighted convolution norm since the sum of norm deviations converges. All bounds are uniform in the real character. The finite $rq$ factors require no invertibility. In particular the exact original coefficient at $(u,v)$, including its global local-product constant and its squarefree mutual-coprimality test, is the divisor convolution

$$
 \sum_{\substack{a\mid u\\ b\mid v}}
       D_q(a,b)\frac{\chi(u/a)}{(u/a)^\beta}
                    \frac{\chi(v/b)}{(v/b)^\beta}.
                                                                    \tag{6}
$$

One can see this coefficientwise from (4): each coordinate of the ordinary character factors has the local geometric series, which cancels the corresponding linear factor. At every prime outside the support of $uvrq$ the constant of (4) keeps precisely the unoccupied factor. The absolute product control just proved permits passage from finitely many primes; (6) is not an assumption of absolute convergence of the two ordinary character series at $\beta$.

## 2. Replace the actual sharp rectangle and extract the moment

Let $\eta=1/200$ and take complex $|z|\le\eta$. For real $M\ge0$ let

$$
 S_\pm(M;z)=\sum_{1\le n\le M}\chi(n)n^{-\beta\pm z},
       \qquad L_\pm(z)=L(\beta\mp z,\chi).
$$

These partial sums tend to the indicated ordinary Dirichlet series (convergent in $\Re s>0$ by nonprincipal periodicity, and agreeing there with analytic continuation from $\Re s>1$). In particular no continuation argument replaces a divergent rectangle. The finite Fourier estimate of the near-square-root confinement, or the same additive Gauss argument for the entire primitive character modulo $r$, gives an incomplete prefix bound $O(\sqrt r\log(2r))$. To see the latter without an assumption on a local odd mode, apply that confinement's (4) with affine coefficient one and $r_{\rm odd}>1$; for bounded $2$-only modulus the asserted bound is immediate. Abel summation gives for $M\ge1$

$$
 |S_\pm(M;z)-L_\pm(z)|\ll G^C\sqrt r\,M^{-\beta+\eta}.
                                                                    \tag{7}
$$

Also all the partial sums, the limits and their tails have absolute bound $O(G^C r^\kappa)$ for $\kappa=1-\beta+\eta\le .006$. Indeed bound absolutely up to $r$ by $(1+\log r)r^\kappa$, then use (7) for a tail beyond $r$. This last estimate is an upper bound, not a claim of real character cancellation with a logarithmic loss alone. Interpolate these two bounds with power $\gamma=1/8$ on (7); writing $\nu=\gamma(\beta-\eta)$ gives

$$
 |S_\pm(M;z)-L_\pm(z)|
    \ll G^C r^{(1-\gamma)\kappa+\gamma/2}M^{-\nu}
                                                                    \tag{8}
$$

also for $0<M<1$, since there $S_\pm=0$, $M^{-\nu}>1$, and the exponent of $r$ is at least $\kappa$. In particular $\nu\ge .12425$ and $\eta+\nu\le .13=\delta$.

Let $F_{q,U}(z)$ be the actual short sum defining $J_{q,U}$ but with $u^zv^{-z}$ in place of $(\log(u/v))^2$. By (6) it is exactly

$$
       \sum_{a,b}D_q(a,b)a^z b^{-z}
                        S_+(U/a;z)S_-(U/b;z).
$$

Any term with $a>U$ or $b>U$ is zero, so the actual upper bounds are still sharp. Subtract the all-line expression

$$
       L_+(z)L_-(z)\sum_{a,b}D_q(a,b)a^z b^{-z}.
                                                                    \tag{9}
$$

Apply (8) on one arm and the uniform $G^Cr^\kappa$ bound on the other, then do the opposite arm. Since $\eta+\nu\le\delta$, the extra powers $a^\nu$ or $b^\nu$ are both paid by (5). The uniform error on the disk is

$$
 O_\epsilon\left(
             G^C r^{(2-\gamma)\kappa+\gamma/2} U^{-\nu}
                     \frac{q^{1-\beta+\delta+\epsilon}}{\varphi(q)}
           \right).                                               \tag{10}
$$

The two sides are holomorphic on a neighborhood of the disk: the finite sum is entire, the ordinary character functions are holomorphic there, and the continued correction sum converges in the absolute weighted norm with exponents strictly larger than $\eta$. Cauchy's formula on this fixed circle therefore gives (10) also for their second derivatives at zero, with the same fixed exponent costs.

At zero the two ordinary factors in (9) both vanish. Their product has second derivative $-2 L'(\beta,\chi)^2$ in $z$, since one uses $\beta-z$ and the other $\beta+z$. The correction has value $\varphi(q)^{-1}$ when $(q,N)=1$ and zero otherwise, by the local evaluations after (4). Thus

$$
  J_{q,U}=
           -2 L'(\beta,\chi)^2\frac{\mathbf1_{(q,N)=1}}{\varphi(q)}
                  +\text{the second-derivative error of (10)}.
                                                                    \tag{11}
$$

This calculation retains the actual two short cutoffs via (10); replacing either by a formal infinite quadratic integral without this comparison would not give (11).

## 3. Keep the original finite Ramanujan denominator

For squarefree $t$ the total positive weight $\varphi(t)^{-1}\sum_{q\mid t}q/\varphi(q)$ is at most $6^{\omega(t)}/t$, by multiplying its prime factors. Thus

$$
        \sum_{\substack{t\le H\\t\ {\rm sf}}}
               \varphi(t)^{-1}\sum_{q\mid t}q/\varphi(q)
               \ll (\log(2H))^C .
$$

This is the elementary positive Euler upper product and Mertens' bound for the sum of reciprocal primes. For the error of (11), take $\epsilon=1/200$ in (5). Then $1-\beta+\delta+\epsilon\le .136$ and $(2-\gamma)\kappa+\gamma/2\le .07375$. With the actual $q\le H$ and $U\ge Q_0^2/r=Q_0H$ the sum of (10) is bounded by a fixed power of $G$ times

$$
     r^{.07375} Q_0^{-\nu} H^{.136-\nu}
            \ \le\ Q_0^{\, .07375-.12425+.01175}
            \ =\ Q_0^{-.03875}.
$$

Here $\nu<.136$ and $r,H\le Q_0$; the displayed conservative bound suffices for $Q_0^{-1/40}$. Thus no polynomial-in-$Q_0$ error was taken against a merely inverse-logarithmic gain.

For the main term in (11), the exact finite divisor sum $\sum_{q\mid t}q\mu(t/q)\mathbf1_{(q,N)=1}/\varphi(q)$ has local factor $-1$ when $p\mid N$ and $-1+p/(p-1)=1/(p-1)$ when $p\nmid N$. Multiplying by the outer $\mu(t)/\varphi(t)$ gives exactly $C_{N,r}(H)$, with both signs shown above. This proves (1), without passing $H$ to infinity.

To prove its absolute positivity, group $t=de$ with $d$ composed only of primes dividing $N$ and $e$ coprime to $N$. For each fixed squarefree $(d,r)=1$ with $d\le H$, the inner sum over squarefree $e\le H/d$, $(e,Nr)=1$ has term $1$ and all remaining terms of total absolute weight at most

$$
   \prod_{p\ge3}\left(1+\frac1{(p-1)^2}\right)-1
     \ \le\ \exp\!\left(\sum_{k\ge1}\frac1{(2k)^2}\right)-1
     \ =\ e^{\pi^2/24}-1<1 .
$$

The prime $2$ cannot lie in $e$ because $N$ is even. The inner sum is at least $2-e^{\pi^2/24}>0$, and every $d$ weight is positive, including $d=1$. This proves the assertion for the actual finite $H$, even if it is close to one.

Finally insert (1) in the reference substitution of the aligned physical formula; its original negative prefactor and the reference negative geometric weight first give a positive factor $r\chi(-1)/(2\varphi(r)L'(\beta,\chi)^2)$. The negative moment in (1) then gives the sign of (2). The bound $|1/L'(\beta,\chi)|\ll1$ is precisely the near-exception reciprocal bound used and cited in that formula, not a new estimate on the Page gap. With $r/\varphi(r)\ll G^C$, the actual physical integral is $O(Y^{2\beta-1}/G)$ for the original bounded test, so $Q_0^{-1/40}$ gives all the claimed log savings in (2). The lower bound there for unit weight on an interval of fixed positive fractional length follows from $N-x,x\asymp Y$, $\beta\to1$ and the finite positivity just proved.

For the genuine first color it remains to evaluate the signed sum with $\rho(\rho-T_x)_+$, which is exactly the additive difference $\rho^2-\rho\min(T_x,\rho)$. Formula (2) does not estimate that term or preclude its cancellation of the reference. The original second color and unaligned targets are not modified.
