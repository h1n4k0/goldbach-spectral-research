# The leading constant for positive short-inclusion omission failures

Keep the nonnegative divisor statistic of [the critical exponential scale theorem](weak-s-type-ii-critical-prime-positive-inclusion-tail-critical-exponential.md):

$$
 \mathcal T_N(H)=\sum_{\substack{r\mid\operatorname{rad}N\\ r>H}}
                                   \frac{3^{\omega(r)}}r .
$$

Fix real constants $0<M<Q$. Put $\mathcal L=\log Y$, $v=\log\mathcal L$, $\lambda=Q/M>1$, and $Z=v^\lambda$. Let $E=E_{Q,M}(Y)$ count the even integers $Y\le N\le2Y$ for which

$$
                       \mathcal T_N(\mathcal L^Q)>\mathcal L^{-M}.
                                                                    \tag{1}
$$

**Theorem.** As $Y\to\infty$, for every such fixed $Q,M$,

$$
 \frac{\log(Y/E_{Q,M}(Y))}{(\log\log Y)^{Q/M}}
                  \longrightarrow
                     \left(\frac{M}{3\mathrm e}\right)^{Q/M},
                                                                    \tag{2}
$$

where $\mathrm e=\exp(1)$. This is an asymptotic for the failure of the specific **positive omission criterion**. It says nothing about a lower bound on the actual signed truncation error, centered-energy transport error, or Weak S.

## 1. Upper bound on the number of failures

Set $\sigma_0=1/\lambda$ and $a_0=1-\sigma_0$, so $0<a_0<1$. For fixed $u,c>0$ set

$$
 \sigma=\sigma_0+\frac{u}{\log v},\qquad a=1-\sigma,\qquad
 s=c v^{\lambda-1}\log v,\qquad
 W_N=\prod_{p\mid N}(1+3p^{-a}).
$$

For large $Y$, $a$ lies in a fixed compact subset of $(0,1)$ and $s\ge1$. Positive Rankin gives $\mathcal T_N(\mathcal L^Q)\le \mathcal L^{-Q\sigma}W_N$. Thus (1) implies $\log W_N>Quv/\log v$ and hence

$$
                           W_N^s>\exp(cQu Z).                      \tag{3}
$$

By expanding the positive squarefree divisor coefficients of $W_N^s$ and counting multiples up to $2Y$, as in the critical scale theorem, we have

$$
       \frac1Y\sum_{Y\le N\le2Y}W_N^s
           \le 2\exp\!\left(\sum_p f_v(p)\right),\qquad
      f_v(p)=\log\!\left(1+\frac{(1+3p^{-a})^s-1}{p}\right).
                                                                    \tag{4}
$$

This is an upper average over all integers and so also bounds the even targets. The product converges at each $Y$: as $p\to\infty$ its logarithmic factors are $O_{Y,Q,M,u,c}(p^{-1-a})$. No statistical independence of divisibility among integers has been assumed.

We evaluate the infinite sum in (4) asymptotically. Define

$$
       g(x)=(3ce^{\lambda u}x^{-a_0}-\lambda)_+\quad(x>0),
       \qquad D=(3ce^{\lambda u}/\lambda)^{1/a_0}.
$$

For $p=xZ$ with $\delta\le x\le R_0$, where $0<\delta<R_0$ are fixed, one has uniformly

$$
 \frac{s\log(1+3p^{-a})}{\log v}=3ce^{\lambda u}x^{-a_0}+o(1),
                \qquad  \frac{\log p}{\log v}=\lambda+o(1).
$$

Indeed $Z^{-a}=v^{1-\lambda}e^{\lambda u}$ and $p^{-a}$ tends uniformly to zero there. The first limit is bounded below by a positive constant on this compact range. Writing $(1+3p^{-a})^s-1$ as $(1+3p^{-a})^s$ times $1-(1+3p^{-a})^{-s}$, the latter factor has logarithm $o(1)$ uniformly. Applying $y_+\le\log(1+e^y)\le y_++\log 2$ gives $f_v(p)/\log v=g(x)+o(1)$ uniformly. The prime number theorem, by rescaled interval counts and then approximation of the continuous $g$ by step functions, gives

$$
 \frac1Z\sum_{\delta Z\le p\le R_0 Z}f_v(p)
                         \longrightarrow \frac1\lambda
                                      \int_\delta^{R_0}g(x)\,dx .  \tag{5}
$$

Here $\log Z=\lambda\log v$, which accounts for the factor $1/\lambda$.

For the lower end, use $0\le f_v(p)\le3s p^{-a}$ and $\sum_{p\le x}p^{-a}\ll x^{1-a}/\log x$ uniformly in a compact subinterval of $(0,1)$, by the prime upper bound and partial summation. For any fixed $0<\delta<1$, this yields

$$
 \sum_{p<\delta Z}f_v(p)\ll_{Q,M,u,c} Z\delta^{\sigma_0/2}
$$

for all sufficiently large $Y$ depending on $\delta$. The implied constant is independent of $\delta$: indeed $s Z^{1-a}/\log v=ce^{\lambda u}Z$, $\log(\delta Z)\ge \frac12\log Z$ eventually for fixed $\delta$, and $1-a\ge\sigma_0/2$. For the upper end, take $R_0>D$ so large that $3s p^{-a}\le\frac12\log Z$ when $p>R_0Z$ for all large $Y$. Such a fixed $R_0$ exists by the same critical scaling and monotonicity in $p$. Then

$$
 \sum_{p>R_0 Z} f_v(p)
       \ll s Z^{1/2}\sum_{n>R_0Z}n^{-1-a}
       \ll_{Q,M,u,c,R_0} Z^{1/2}\log v=o(Z).
$$

This uses $\log(1+w)\le w$ and $e^t-1\le t e^t$ for $w,t\ge0$. Let $\delta\downarrow0$ in (5). Since $g$ vanishes for $x\ge D$ and $a_0<1$, these bounds prove

$$
 \frac1Z\sum_p f_v(p)
              \longrightarrow \frac1\lambda\int_0^D
                   (3c e^{\lambda u}x^{-a_0}-\lambda)\,dx
                         =(\lambda-1)D.                            \tag{6}
$$

The last equality uses $3c e^{\lambda u}D^{-a_0}=\lambda$ and $(1-a_0)^{-1}=\lambda$.

Write $D_*=(M/(3\mathrm e))^\lambda$, and choose $u=1/\lambda$, $c=(\lambda/(3\mathrm e))D_*^{a_0}$. Then $D=D_*$ in (6) and $cQu=cM=\lambda D_*$ since $D_*^{\sigma_0}=M/(3\mathrm e)$. Markov's inequality by (3)–(4) gives

$$
                          E/Y\le\exp(-(D_*+o(1))Z).                \tag{7}
$$

All parameters in this choice other than the prescribed $v$-dependence of $\sigma,a,s$ are fixed.

## 2. Lower bound from tilted divisors of a primorial

Fix any $D>D_*$ and put $z=DZ$, $P_z=\prod_{p\le z}p$. For large $Y$, each multiple of $P_z$ is even, and the prime number theorem in the form $\sum_{p\le z}\log p\sim z$ shows that their number in $[Y,2Y]$ is

$$
                      Y\exp(-(D+o(1))Z),                          \tag{8}
$$

since $\log Y=e^v$ and $Z=o(\log Y)$. We prove that every such multiple satisfies (1) for large $Y$.

On the **finite divisor space** $r\mid P_z$, give $r$ probability $3^{\omega(r)}r^{-(1-\sigma)}/W_z(\sigma)$ with

$$
                    W_z(\sigma)=\prod_{p\le z}
                                       (1+3p^{-(1-\sigma)}).
$$

The prime choices are independent in this constructed divisor space, not on random target integers. For $a=1-\sigma$ each chosen-prime probability is $t_p=3p^{-a}/(1+3p^{-a})$. Let $m_z(\sigma)$ be the mean of $\log r$:

$$
                 m_z(\sigma)=\sum_{p\le z}t_p\log p .
$$

Uniformly on any fixed compact subset of $0<\sigma<1$, the prime number theorem and partial summation give

$$
 \sum_{p\le z} p^{-(1-\sigma)}\log p
                  \sim\frac{z^\sigma}{\sigma},\qquad
 \sum_{p\le z} p^{-(1-\sigma)}
                  \sim\frac{z^\sigma}{\sigma\log z}.                \tag{9}
$$

For the first relation use the ordinary estimate for the sum of $\log p$, with the small endpoints uniformly negligible since $\sigma$ is bounded below. For the second one may discard $p\le z^{1-\epsilon}$ for fixed $\epsilon>0$ by the ordinary integer power sum, then use the logarithmic weights in the first relation with $1\le\log z/\log p\le(1-\epsilon)^{-1}$, and let $\epsilon\downarrow0$. The replacements of $t_p$ by $3p^{-a}$ and of $\log(1+3p^{-a})$ by $3p^{-a}$ cost only $O(p^{-2a})$ per prime, with an extra $\log p$ for the mean. These errors are smaller than their respective mains in (9), uniformly: at $p>\sqrt z$ factor out $z^{-a/2}$ times the corresponding linear sum, and at $p\le\sqrt z$ use an integer power sum. Consequently

$$
               m_z(\sigma)\sim \frac{3z^\sigma}{\sigma},\qquad
               \log W_z(\sigma)\sim\frac{3z^\sigma}{\sigma\log z}.
                                                                    \tag{10}
$$

In particular, uniformly for bounded real $w$ at $\sigma=\sigma_0+w/\log v$,

$$
          m_z(\sigma)=\bigl(3\lambda D^{\sigma_0}e^{\lambda w}
                                                      +o(1)\bigr)v.
                                                                    \tag{11}
$$

Put $\Delta=v/(\log v)^2$ and $u_D=\lambda^{-1}\log(M/(3D^{\sigma_0}))$. The expression $3\lambda D^{\sigma_0}e^{\lambda w}$ equals $Q$ at $w=u_D$ and is strictly increasing. The exact mean is itself continuous strictly increasing as a function of $\sigma$, since each of its positive Bernoulli terms is. For any fixed $\epsilon>0$, (11) brackets $Qv+\Delta/2$ between the means at $w=u_D-\epsilon$ and $w=u_D+\epsilon$ for large $Y$. Choose the unique $\sigma=\sigma(v)$ in this neighborhood with exact mean $Qv+\Delta/2$. Taking arbitrary fixed $\epsilon$ proves $(\sigma(v)-\sigma_0)\log v=u_D+o(1)$. Since $D>D_*$, we have $u_D<1/\lambda$. By (10) and $\log z=\lambda\log v+O_D(1)$, this choice has

$$
                         \log W_z(\sigma(v))
                          =(M+o(1))\,v/\log v .                    \tag{12}
$$

The variance of $\log r$ in the divisor space is

$$
 \sum_{p\le z} t_p(1-t_p)(\log p)^2
                   \le (\log z)m_z(\sigma(v))=O_{Q,M,D}(v\log v).
$$

Chebyshev therefore gives probability $1-o(1)$ to $Qv<\log r\le Qv+\Delta$, because $v\log v/\Delta^2=(\log v)^5/v=o(1)$. This band enforces the strict original threshold $r>\mathcal L^Q$. For any multiple of $P_z$, all these divisors are in the original positive sum. Undo the tilt on the band: $r^{-\sigma(v)}\ge e^{-\sigma(v)(Qv+\Delta)}$ there for large $Y$, since $\sigma(v)>0$. Thus

$$
 \begin{split}
  \log\mathcal T_N(\mathcal L^Q)
       &\ge \log W_z(\sigma(v))-\sigma(v)(Qv+\Delta)+\log(1-o(1))\\
       &= -Mv+\bigl(M-Q u_D+o(1)\bigr)\frac v{\log v}.
 \end{split}                                                       \tag{13}
$$

We used $\Delta=o(v/\log v)$ and $Q\sigma_0=M$. As $M-Q u_D>0$, (13) proves (1) for all the genuine multiples counted in (8).

Equations (7) and (8) prove a limit inferior at least $D_*$ and a limit superior at most $D$ for the ratio in (2). Since $D>D_*$ was arbitrary, (2) follows. This identifies the leading constant in the rate for the exact positive divisor test, without any implication of actual error on its exceptional targets.
