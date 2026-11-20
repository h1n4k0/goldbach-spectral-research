# 第七轮：全远块的高纵坐标切除

**新估计。** 在局部 GRH(N) 下，[第 5 轮算子笔记](operator-round5.md) 中真实零点–对数素数远块的 $|\gamma|>H$ 部分，有全模式 Hilbert–Schmidt 界
$$
\left\|\mathbf1_{x\ge y+B,\ y\ge0}\,\mathcal Z_N^{>H}(x,y)\right\|_{HS}
\ll e^{-B/L}\frac{L^{3/2}(L+\log(2H))}{\sqrt H},
\qquad L=\log N,\quad H\ge4.
$$
下半块由伴随得到同阶。它给出真正的高纵坐标尾截断，不控制低零点的跨尺度相位。与 arithmetic 组的近带切除互补：这里在整个无界远半块积分，利用另一侧的弱 Hardy 衰减把随 y 移动的下限保留下来。第六轮及之前文件未改动。

## 1. 对每个特征和每个单位时间区间的一致界

记本原诱导零点的真实纵坐标为 γ，重数 $m_\chi(\gamma)$。用第 5 轮归一化，在高纵坐标定义
$$
Z_\chi^{>H}(x)=\sum_{|\gamma|>H}\frac{m_\chi(\gamma)}{1+i\gamma}e^{i\gamma x}.
$$
先取有限纵坐标上限。给任意单位区间选平移的非负 $c(\sin(\epsilon t)/(\epsilon t))^2$ 作为 1 的上界，其中 $\epsilon$ 取固定小数。它有固定紧 Fourier 支撑，于是积分展开中，仅 $|\gamma-\gamma'|\le C$ 的项存留；平移只改变单位模相位。对各单位纵坐标区间 $[k,k+1)$ 记
$$
a_k=\sum_{\gamma\in[k,k+1),\ |\gamma|>H}\frac{m_\chi(\gamma)}{|1+i\gamma|}.
$$
则平方积分由 $C\sum_{|k-j|\le C'}a_ka_j\le C''\sum a_k^2$ 控制。从 Dirichlet L 函数局部计数（见 [Li–Liu](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf) §3, §6.4）得 $a_k\ll (L+\log(2+|k|))/(1+|k|)$。因此对所有实 v，
$$
\int_v^{v+1}|Z_\chi^{>H}(x)|^2dx
\ll \sum_{|k|\ge H-2}\frac{(L+\log(2+|k|))^2}{(1+|k|)^2}
\ll \frac{(L+\log(2H))^2}{H}.
$$
同样对截断之差，故极限在每个单位区间的 $L^2$ 中存在，且与原零点分布定义相容。不使用发散的绝对零点和；重数按通常零点计数已包括。

## 2. 整个非紧远块

原始对数坐标 $x=\log n$ 中，设 $\alpha=1/L$，$W(x)=1+e^{-2(\beta-\alpha)x}$。第 5 轮的远半核中，高零点贡献为
$$
\mathcal Z_N^{>H}(x,y)=\sqrt{2\pi W(x)W(y)}e^{-\alpha x}
\mathbb E_-\left[Z_\chi^{>H}(x)\overline{f_{\chi,\alpha}(y)}\right],\qquad x>y,
$$
其中 $f_{\chi,\alpha}$ 是 $g_\chi(\alpha+it)/(1+\alpha+it)$ 的单位 Fourier 逆变换。$W$ 在正轴有界。上一节沿 $x\ge y+B$ 求和：
$$
\int_{y+B}^\infty e^{-2\alpha x}|Z_\chi^{>H}(x)|^2dx
\ll Le^{-2(y+B)/L}\frac{(L+\log(2H))^2}{H}.
$$
不必交换无限非绝对级数与积分：可先用有限零点和，再靠一致的 $L^2$ 尾控制通过。对特征平均用 Jensen / Cauchy，随后在 y 求积并调用原论文 §6.4 的 $\mathbb E_-\|f_{\chi,\alpha}\|_2^2\ll L^2$，得到报告开头的界。

* 对任意固定 $A>0$，取 $H=L^{2A+6}$，高零点远块为 $O(L^{-A-1/2})$，低于 $o(\mathfrak S(N)L^{-A})$ 所需量级。
* 对 R 的目标 $\delta_N=\sqrt{\mathfrak S(N)/N}\,L^{3/2}$，取 $H=NL^{2+\epsilon}$、$\epsilon>0$ 固定，高纵坐标远块为 $o(\delta_N)$。这只处理高零点尾，不表示第 5 轮的另外各种误差自动也在 R 精度。

## 3. 低纵坐标需要检测的确切交叉量

对于两有限时间窗 $J,I\subset[0,\infty)$，若 $x-y\ge B$ 在 $I\times J$ 恒成立，则无需在该矩形再乘三角掩膜。把奇特征族的所有 $|\gamma|\le H$ 纵坐标取并集，不出现的重数记零。定义
$$
U_\gamma(x)=\mathbf1_I(x)\sqrt{W(x)}\,e^{(-\alpha+i\gamma)x}/(1+i\gamma),\quad
V_\gamma(y)=\mathbf1_J(y)\sqrt{W(y)}\,\mathbb E_-[m_\chi(\gamma)f_{\chi,\alpha}(y)] .
$$
低零点矩形算子恰为 $\sqrt{2\pi}\sum_\gamma U_\gamma\otimes V_\gamma$。令 $G_U,G_V$ 为列 Gram，则其范数平方恰为 $2\pi\|G_U^{1/2}G_VG_U^{1/2}\|$。同一固定 N 内的 $V_\gamma$ 可通过模 N 的素数幂前缀写出；唯一混合系数是
$$
c_{\gamma,N}(n)=\mathbb E_-[m_\chi(\gamma)\chi(n)],\qquad
V_\gamma(y)=-\sqrt{2\pi W(y)}\mathbf1_J(y)e^{-(1+\alpha)y}
\sum_{n\le e^y}\Lambda(n)\sqrt n\,c_{\gamma,N}(n).
$$
符号由 $L'/L$ 的 Dirichlet 展开给定。即使无需估计无限高零点，现在仍须在越来越长的两尺度窗上对这些**带符号的素数加权混合列**及不同 γ 的相关性得到统一小矩阵范数。零点计数、平均重数、单尺度方差或共同窗二点极限没有控制该矩阵。没有证明此矩阵满足 S/R 所需界。
