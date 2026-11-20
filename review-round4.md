# 第四轮：正 Fourier 测试把 S/R 变成零点重数与微小间距的必要条件

**条件性推论，不是 S 或 R 的证明。** 令 $L=\log N$。固定任意高度界 $H>0$，考察模 $N$ 的奇特征，每个特征用它所诱导的本原 $L$ 函数。设非平凡零点写成 $1/2+i\gamma$、不同纵坐标的重数为 $m_\chi(\gamma)$；下列论断假设论文的 $\mathrm{GRH}(N)$。以 $\mathbb E_\chi$ 表示均匀奇特征平均。

定义 $B_H(T)$ 为下列两种**有序**超近配对的平均数：（i）$|\gamma|\le H$ 上同一纵坐标的 $m(m-1)$ 个异编号对；（ii）$|\gamma|,|\gamma'|\le H$、$0<|\gamma-\gamma'|\le1/T$ 的不同纵坐标对，计 $m(\gamma)m(\gamma')$。则对每个充分大、满足相应谱假设的偶模数，
$$
\begin{array}{c|c|c}
\text{范数假设}& T & B_H(T) \\ \hline
\mathrm{R} & L^2/8 & O_H(\log L/L) \\
\mathrm{S}(h) & L\log L/8 & O_H(L/(\log L)^2).
\end{array}
$$
第一行意味着，在每个这样的模数上，有异常重数或如此小间距的奇特征所占的比例趋零。它不是说所有单个 $L$ 函数的零点都简单，也不作无条件判断。第二行的数量是 $o(L)$ 而非 $o(1)$，与第一行不同。

## 一、选谱权并从正性取下界

取一个实偶非负光滑小窗 $h_0$，支撑充分窄，使其 Fourier 变换在 $[-H,H]$ 内有正下界（余弦在支撑上为正即够）。令 $F=h_0*h_0$, $\mathrm{supp}(F)\subset(-w,w)$，其中 $0<w<(\log2)/3$。采用 $a(\xi)=\int F(v)e^{i\xi v}dv$；于是 $a=|\widehat h_0|^2$ 处处实非负、快速衰减，在目标高度段有下界。设 $I=\int F(v)^2dv$，
$$
 Z_\chi(t)=\sum_{\gamma} m_\chi(\gamma)a(\gamma)e^{i\gamma t},\quad
 A(t)=\mathbb E_\chi|Z_\chi(t)|^2,\quad D_0=\mathbb E_\chi\sum_\gamma m_\chi(\gamma)a(\gamma)^2 .
$$
由单位高度零点数界，级数绝对收敛。$a$ 实值故 $|Z_\chi|^2$ 为偶函数，不要求单个非实特征自身的纵坐标对称。

归一 Fejér 时间核 $K_T(t)=T^{-1}(1-|t|/T)_+$ 的 Fourier 变换是 $\operatorname{sinc}^2(Tu/2)$，处处非负且在 $|u|\le1/T$ 有绝对正下界。逐项展开得
$$
 c_H B_H(T)\le \int_{-T}^T K_T(t)(A(t)-D_0)\,dt. \tag{1}
$$
关键点：$D_0$ 只扣除同一个**编号**的零点；同纵坐标的其余 $m(m-1)$ 对仍保留。不同纵坐标的全部贡献非负，因为 $a\ge0$。

## 二、不可忽略的导子尖峰与中心区相消

对本原诱导奇特征应用 [Dirichlet 型 Weil 显式公式](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.70360)，或用正负两侧 Mellin 移线。对 $t\ge0$ 得
$$
 Z_\chi(t)=\log(d_\chi/\pi)F(t)+G(t)-
 \sum_{n\ge1}\frac{\Lambda(n)\chi^*(n)}{\sqrt n}F(\log n-t).
 \tag{2}
$$
傅里叶符号的另一选择将 $\chi^*$ 换成其共轭，不改变族平均。$G(t)$ 是固定函数：$a(\xi)\Re\psi(3/4+i\xi/2)$ 的逆 Fourier 变换，快速衰减；$\psi=\Gamma'/\Gamma$。通常还有支撑 $F(\log n+t)$ 的素数侧，在这里因 $n\ge2,\ w<\log2,\ t\ge0$ 恒为零。导子项与剩下的素数项也无重叠，因为 $2w<\log2$。同一公式在 $t=0$ 用 $a^2$：其逆变换 $F*F$ 在 0 的值为 $I$，支撑不碰任何 $\log n$，故
$$
 D_0= I L+O_H(\log L).
$$
这里 $\mathbb E_\chi(L-\log d_\chi)\ll\log L$：奇特征至多花费全族平均的两倍；全族亏损为 $\sum_{p\mid N}\log p/(p-1)$，按 $p\le L,p>L$ 拆开用 Chebyshev 及 $\sum_{p\mid N}\log p\le L$ 即证。于是 $\mathbb E_\chi(\log(d_\chi/\pi))^2 = L^2+O(L\log L)$。

取 $t_0=L+C$，$C>\log 2+1$ 固定。下证
$$
 \int_{-t_0}^{t_0}[A(t)-D_0]dt=O_H(L\log L). \tag{3}
$$
为此在 (2) 中先把本原特征换为模 $N$ 的导出特征。素数项的修正逐特征至多
$$
 b(t)\ll_H\min(e^{t/2},L e^{-t/2}).
$$
第一界由 Chebyshev；第二界因每个 $p\mid N$ 的幂在固定比率窗内只有 $O_H(1)$ 个。两界切在 $t=\log L$，故 $\int_0^\infty b(t)^2dt\ll L$，且 $\int_0^\infty\sqrt{1+t}\, b(t)dt\ll\sqrt{L\log(2L)}$。

对换后的素数项，在 $0\le t<L-\log2-w$ 用奇特征正交性，平方的平均**恰为** $\sum_{(n,N)=1}\Lambda(n)^2 F(\log n-t)^2/n$，因为窗口内所有 $n<N/2$。在直至 $t_0$ 的剩余有界长度区间，模 $N$ 每个剩余类只有有界多个窗口候选，舍去奇筛用全特征正交性及 Cauchy 即得平方平均 $O_H(1+t)$；同一上界在前一段由 Chebyshev 成立。这证明由 $b$ 和固定 $G$ 产生的平方误差与交叉误差合计积分 $O_H(L)$（与导子尖峰的 $G$ 交叉项也是 $O(L)$；素数项在尖峰支撑为零）。

将精确对角式在正半段积分，其值为 $I L^2/2+O_H(L)$。具体地，对不在上下窗移动边缘的每个 $n$，$t$ 积分正是 $I$；上端固定倍比区间的 $\Lambda^2/n$ 总量为 $O(L)$。普通素数定理分部求和给 $\sum_{n\le N}\Lambda(n)^2/n=L^2/2+O(L)$；剔除 $p\mid N$ 的诸幂至多 $\sum_{p\mid N}(\log p)^2/(p-1)\ll L$。加上负半段，素数斜坡总面积为 $I L^2+O_H(L)$。导子尖峰在整个中心区的面积又是 $I L^2+O_H(L\log L)$，而 $2t_0D_0=2 I L^2+O_H(L\log L)$。这给 (3)。若删除中心尖峰，反而会得出伪矛盾。

非负性及 (3) 还给 $\int_{-t_0}^{t_0}|A(t)-D_0|dt\ll_H L^2$。对 $T>t_0$ 插入 Fejér 权后，中心区对 (1) 的贡献至多
$$
 O_H(L\log L/T+ L^3/T^2). \tag{4}
$$

## 三、外区：在恰当时间尺度使用目标谱假设

设 $f(u)=u^{-1/2}F(\log u)$，共同伸缩量 $Y=e^t/N$。这样 [source-round3.md](source-round3.md) 中的零点权正是 $a$。由该笔记给出的模型基线及有界 Riesz 向量缩放（$M_N=\|T_N\|$），对 $t_0\le t\le T$，
$$
 |A(t)-D_0|\ll_H M_N e^{2t/L}
 +(\log L)^{C_H}e^{-(t-L)/\log L}
 +e^{-c\sqrt t}+L^2 e^{-t/2}+L/\varphi(N).
$$
固定的 $F$ 及其 $H$ 相关常数不随 $N,T$ 变化。该行是上界、并非未经误差的单零点匹配。负 $t$ 由偶性处理。将外区积分除以 $T$，模型移线误差至多 $O_H((\log L)^{C_H+1}/T)$，其余指数尾部可忽略。结合 (1)、(4)，得到可独立检查的通用门槛
$$
 B_H(T)\ll_H L\log L/T+L^3/T^2+ M_N e^{2T/L}
 +(\log L)^{C_H+1}/T+L/\varphi(N). \tag{5}
$$

若有 R，则 $M_N\le\sqrt{\mathfrak S(N)/N}\,L^{3/2}$。取 $T=L^2/8$，放大仅为 $e^{L/4}$；所有外区项低于 $O_H(\log L/L)$。若有 S(h)，$M_N\ll\mathfrak S(N)/h\ll\log L$；取 $T=L\log L/8$，则放大为 $L^{1/4}$，总量由中心权残差 $L/(\log L)^2$ 控制。两行即证。

**如何尝试反证。** 若能在无界的合法模数列上证明每个模数的奇特征族在固定高度段平均有**正比例常数个**上述重数过量或 $O(L^{-2})$ 间距对，则与 R 不相容。这里没有找到这样的算术下界。单个特征的一个近重零，或平均于许多导子的简零百分数，都不足以给出所需矛盾。反过来，没有这些近重零也不证明 R。
