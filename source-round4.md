# 第四轮：不等尺度的协方差与模型衰减

**结果。** 对 $Y\ne Z$ 的不等尺度，连续模型的跨尺度基线可以精确移线求出。两个平滑窗的物理支撑一旦分离，基线以 $(\max(Y,Z)/\min(Y,Z))^{-3/2}$ 衰减，且首项可显式计算。相应的真实零点协方差仍缺统一消去。把基线与单零点统计对齐时，还出现一项位于尺度比附近的模 $N$ 素数进程差，新项不能在任意尺度比下省略。没有证明 S 或 R。

## 1. 精确模型及 Mellin 余项

沿用[原文](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf)及前轮记号。固定实值 $f,g\in C_c^\infty(0,\infty)$，分别取 $f_Y(u)=f(u/Y)$、$g_Z(u)=g(u/Z)$。不失一般性 $Y\ge Z\ge1$，记 $Q=Y/Z,\ d=\log Q,\ L=\log N$，以及导子亏损 $b_N=\sum_{p\mid N}\log p/(p-1)$。设
$$
F(\xi)=e^{\xi/2}f(e^\xi),\quad G(\xi)=e^{\xi/2}g(e^\xi),\quad
C(v)=\int F(\xi)G(\xi+v)d\xi .
$$
$C$ 紧支撑；其 Fourier 表达为 $C(v)=(2\pi)^{-1}\int\widetilde\Phi_f(it)\widetilde\Phi_g(-it)e^{itv}dt$。

将 $(f_Y,g_Z)$ 放入论文 (2.12)、§7.1 的模型矩阵元，令 $w=s+z$。由于窗的 Mellin 变换为 $Y^{1/2+s}\widetilde\Phi_f(s)$ 和 $Z^{1/2+z}\widetilde\Phi_g(z)$，连续模型除以 $\sqrt{YZ}$ 后是
$$
\frac1{(2\pi i)^2}
\int_{(r)}\int_{(0)}
Z^w Q^s\widetilde\Phi_f(s)\widetilde\Phi_g(w-s)X_1(s)X_1(w-s)
\pi^w\zeta(1-w)\zeta(1+w)A_N(w)\,ds,dw .
$$
取固定小 $r>0$，将 r 线相应的内积分先从合适的正 s 线移到 0 线。$A_N$ 为第三轮的 Euler 积，在 $0$ 有 $A_N(0)=1$、$A_N'(0)=b_N$。将 w 从 r 移到 $-\kappa$（$0<\kappa<1/2$），经过二阶极点
$$
\pi^w\zeta(1-w)\zeta(1+w)A_N(w)
=-w^{-2}-(\log\pi+b_N)w^{-1}+O_N(1).
$$
留数包括 $-(\log Z+\log\pi+b_N)C(d)$、对 $\widetilde\Phi_g(w-s)$ 的导数（带负号）与 $-X_1'(w-s)/X_1(w-s)$ 的贡献。导数项在物理坐标是 $-\sqrt Q\int f(t)g(Qt)\log(Qt)dt$。由素数定理，精确对角项除以 $\sqrt{YZ}$ 的主项为 $\sqrt Q\int f(t)g(Qt)\log(NYt)dt$，与前项及 $-\log Z\,C(d)$ 合并为 $\log N\,C(d)$。对角误差记为 $E_D$；有重叠时 Q 有固定上下界，可取 $E_D\ll_{f,g}e^{-c\sqrt{\log(NZ)}}+L\log(NZ)/(NZ)$；无重叠时精确为零。

在 $\Re w=-\kappa$ 的余项中把内 s 线左移到 $-(3/2+\kappa/2)$：$X_1(s)$ 在所经左半平面无极点（可能有零），且 $\Re(w-s)\le3/2-\kappa/2$ 始终在 $X_1$ 第一个极点的左侧。结合 Mellin 竖直快衰减、Stirling 与 $A_N$ 界，得
$$
E_K\ll_{f,g,\kappa} Q^{-3/2}(YZ)^{-\kappa/2}e^{C_\kappa L^\kappa}.
$$
固定 $\kappa$ 适合任一尺度至少为 $N$ 的正固定幂次，另外可沿用第三轮取 $\kappa=1/\log L$（把 gamma 靠近极点的逆距离损失和 ζ 损失计入 $(\log L)^C$）。因此最终基线为
$$
\frac{D(f_Y,g_Z)+K(f_Y,g_Z)}{\sqrt{YZ}}=\mathcal A_N(d)+O(E_D+E_K),\qquad
\mathcal A_N(d)=\frac1{2\pi}\int\widetilde\Phi_f(it)\widetilde\Phi_g(-it)e^{itd}
\left[\log(N/\pi)-b_N+\Re\psi(3/4+it/2)\right]dt .
$$
模型与对角公式本身不需 GRH。

## 2. 显式的尺度分离衰减

若 $d$ 已越过 $C$ 的支撑并有固定正间隔，则两个窗不重叠，精确对角项和 $C(d)$ 都为零，只有 gamma 项。使用
$$
\Re\psi(a+it/2)=-\gamma_E+
\int_0^\infty\frac{e^{-u}-e^{-au}\cos(tu/2)}{1-e^{-u}}du
$$
并取 $a=3/4$。$C(d)=0$ 将常数项和 u 近零时的奇性去掉，故可换序得到
$$
\mathcal A_N(d)=-\int_{\mathbb R}C(v)\frac{e^{-3|d-v|/2}}{1-e^{-2|d-v|}}dv
=-Q^{-3/2}\int C(v)e^{3v/2}dv+O_{f,g}(Q^{-7/2}).
$$
对非零非负 f,g，首项系数严格非零。这个衰减的符号和指数可独立用 gamma 的第一极点检查，不能类推到真实算术协方差。

## 3. 不等尺度的一阶零点项与素数侧修正

以 $\mathbb E_-$ 表示奇特征平均，$\chi^*$ 为本原诱导对应，$a_N(n)=\mathbb E_-\chi^*(n)\in\mathbb R$。利用[Dirichlet Weil 显式公式](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.70360)（必要时对闭合共轭族先取 t 偶部），平移测试 $e^{itd}\widetilde\Phi_f(it)\widetilde\Phi_g(-it)$ 给
$$
\begin{split}
\mathbb E_-\sum_\gamma m_\chi(\gamma)\widetilde\Phi_f(i\gamma)\widetilde\Phi_g(-i\gamma)e^{i\gamma d}
&=\mathcal A_N(d)-\mathcal P_N(d)+O_{f,g}(|C(d)|L/\phi(N)),\\
\mathcal P_N(d)&=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}a_N(n)
[C(d-\log n)+C(d+\log n)] .
\end{split}
$$
支持集限定 $n\asymp_{f,g}Q$（第二项对 Q 足够大恒零）。若 $p\nmid N$，$a_N(p^r)=\mathbf1_{p^r\equiv1\ (N)}-\mathbf1_{p^r\equiv-1\ (N)}$。因此当 $Q<c_{f,g}N$ 时，这部分精准为零；一般地按两进程分别计数再取绝对值，得
$$
|\mathcal P_{N,p\nmid N}(d)|\ll_{f,g}
\log(2Q)(\sqrt Q/N+Q^{-1/2}).
$$
对 $p\mid N$，与第三轮相同，置 $M=N/p^{v_p(N)}$，可能非零的权重至多 $\phi(M)/\phi(N)$ 且必须 $M\le p^r+1\ll Q$。固定乘法窗每个 p 至多 $O_{f,g}(1)$ 个幂次，总对数 $O(L)$，故
$$
|\mathcal P_{N,p\mid N}(d)|\ll_{f,g}LQ^{-1/2}\min(1,Q/\phi(N))\ll_{f,g} L/\sqrt{\phi(N)}.
$$
所以只要 $Q\le N^{2-\epsilon}$，修正一律为 o(1)（低比值用精准消失）；比值再大时不能省略进程差。即便修正为 o(1)，也未必达到 R 的 $\delta_N$。

## 4. 待取消的双相位和，以及一个直接必要条件

GRH(N) 下，实际奇特征乘积除以 $\sqrt{YZ}$ 的零点展开为
$$
\mathbb E_-\sum_{\gamma,\gamma'}m_\chi(\gamma)m_\chi(\gamma')
\widetilde\Phi_f(i\gamma)\widetilde\Phi_g(-i\gamma')
e^{i[(\gamma-\gamma')\tau+(\gamma+\gamma')d/2]}+
O_{f,g}(L^2/\sqrt{NZ}),\qquad
\tau=(\log(NY)+\log(NZ))/2 .
$$
按第三轮证明分别对两个平滑素数和移线即可；此处误差取较小尺度 Z。若再扣掉 $D+K$，同纵坐标的系数由 $m^2$ 变为 $m(m-1)$，异纵坐标双相位保留，还须**减去** $\mathcal P_N(d)$。GRH(N) 只把相位移到单位圆，独自并不给其平均的衰减。

对具体几何尺度 $Y=N^\theta,Z=N^{\theta'}$，$\theta>\theta'\ge0$ 固定，模型和对角基线为 $O_{f,g}(N^{-3(\theta-\theta')/2})$。两个测试向量的范数乘积除以 $\sqrt{YZ}$ 为 $O_{f,g}(e^{2+\theta+\theta'})$，所以 S 推出实际奇特征协方差在除以 $\sqrt{YZ}$ 后为 $o(\mathfrak S(N))$；R 推出 $O_{f,g,\theta,\theta'}(\delta_N+N^{-3(\theta-\theta')/2})$。分离指数 $\theta-\theta'\ge1/3$ 时，基线已是 $o(\delta_N)$。这是可用纯算术和式及固定窗单独反验的**必要条件**，而非全算子充分条件。
