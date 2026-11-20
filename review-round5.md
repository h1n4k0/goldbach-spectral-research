# 第五轮候选：谱范数小于单零点主项，蕴含固定模数奇特征族的加权二点极限

**研究推导；不反推 S 或 R。** 设 $N\to\infty$ 沿满足局部 Dirichlet GRH 的偶数序列。额外假设甚至可以弱于 S：只须 $\|T_N\|=o(\log N)$。对任一固定高度的非负光滑谱权，选择如下可证的紧 Fourier 支撑子族，即可得到一般紧测试函数在平均零点间距尺度上的正弦核二点极限。本文的奇特征族是在**每一个**模数上取平均，零点来自各模 $N$ 奇特征所诱导的本原 $L$ 函数，不能换成跨很多原始导子的平均。

## 精确表述

使用 [review-round4.md](review-round4.md) 中的 $F,a,I,D_0,A$：$F=h_0*h_0$，$h_0$ 固定、实偶、非负、光滑、紧支撑且非零，$\mathrm{supp}(F)\subset(-w,w)$，$w<(\log2)/3$；$a(\gamma)=\int F(v)e^{i\gamma v}dv\ge0$，$I=\int F^2>0$，$L=\log N$。定义正局部有限测度
$$
 \nu_N=\frac1{LI}\mathbb E_{\chi\,{\rm odd}\bmod N}
 \sum_{\text{零点编号 }j,k}
 a(\gamma_{\chi,j})a(\gamma_{\chi,k})
 \,\delta_{L(\gamma_{\chi,j}-\gamma_{\chi,k})/(2\pi)} .
$$
重复零点的每个编号是真实的一个索引。则对每个 Schwartz 测试 $f$（亦可对连续紧支撑测试），
$$
 \int f\,d\nu_N\ \longrightarrow\ f(0)+
 \int_{\mathbb R}f(x)\left[1-\left(\frac{\sin \pi x}{\pi x}\right)^2\right]dx .
$$
若只对 $j\ne k$ 求和，则右边删掉 $f(0)$。这是**两点**相关的极限，既非全体阶数的随机矩阵定理，也非收敛速率、点态全谱定理或关于所有单个特征的断言。

## 证明

先验证固定紧频率区间上的分布收敛
$$
 \frac{A(Lu)}{LI}\,du\ \Longrightarrow\ \delta_0+\min(|u|,1)\,du. \tag{1}
$$
对 $|t|=|Lu|\le L+C$ 用第四轮的式 (2) 和同一小窗。导子尖峰部分的测度通过缩放在 $u=0$ 集中，质量为 $\mathbb E_\chi[\log(d_\chi/\pi)^2]/L^2\to1$。这里 $F$ 在原时间尺度的平方积分为 $I$；对应宽度在新的 $u$ 尺度为 $O(1/L)$。Gamma 项、替换导出特征的误差及所有交叉项的绝对积分为 $O_F(L)$，在 $du/(LI)=dt/(L^2I)$ 下消失。尖峰与素数项严格不重叠。

对 $0<|u|<1$，令 $t=L|u|$。最终 $t<L-\log2-w$。奇特征平均恰为导出特征对角
$$
\sum_{(n,N)=1}\frac{\Lambda(n)^2}{n}F(\log n-t)^2=I t+o_F(L).
$$
无单位限制的公式由素数定理分部求和得 $I t+O_F(1)+o_F(1)$。剔除 $p\mid N$ 的诸幂并不会产生点态主项：窗内 $n\asymp e^t$，每个 $p\mid N$ 在固定倍比窗内只有 $O_F(1)$ 个幂，总对角修正 $\ll_F e^{-t} L(t+1)=o(L)$。对全部中心区，单纯 Chebyshev 给出换后平方平均 $O_F(1+|t|)$（靠近末端用有界同余重数），故可支配收敛得到 $|u|\,du$ 的部分。两个端点 $|u|=1$ 附近宽度 $O(1/L)$ 的区段也不产生原子。

对每个固定 $A_0>1$，在 $L+C\le|t|\le A_0 L$，第四轮外区公式给
$$
|A(t)-D_0|\ll_F e^{2A_0}\|T_N\|+(\log L)^{C_F}+o(1)=o_F(L).
$$
这里 $D_0/(LI)\to1$。这给余下的常数函数 1，完成 (1)。原文现有 GRH 范数上界 $O(L^2)$ 不足以给这一点；S 所给 $\|T_N\|\ll\mathfrak S(N)/h\ll\log L$ 则绰绰有余。

设 $\widehat f(u)=\int f(x)e^{-2\pi iux}dx$。若 $\widehat f$ 光滑紧支撑，则 Fourier 反演与 (1) 给
$$
 \int f\,d\nu_N
 =\frac1{LI}\int \widehat f(u)A(Lu)du
 \to \widehat f(0)+\int\widehat f(u)\min(|u|,1)du.
$$
右边改写时，用 $\min(|u|,1)=1-(1-|u|)_+$ 和三角函数的逆 Fourier 变换；即得表述中的正弦核。将相同编号扣掉会减少 $f(0)D_0/(LI)\to f(0)$。

为去掉测试函数的 Fourier 支撑限制，选一个非负 Schwartz 函数 $g$，具有紧 Fourier 支撑且 $g\ge1$ 于 $[-1,1]$。例如把一个紧频率偶小窗的逆 Fourier 变换平方，伸缩、乘常数即可。由非负性和移位，所有实 $s$ 一致有
$$
 \nu_N([s-1,s+1])\le\int g(x-s)d\nu_N(x)
 \le (LI)^{-1}\int |\widehat g(u)|A(Lu)du\ll_g1.
$$
最后一步只用 (1) 在固定紧区间的质量有界。Schwartz 函数用 Fourier 截断在 Schwartz 拓扑中逼近；一致的单位区间质量使尾误差可控。连续紧支撑函数再由光滑一致逼近得到。证毕。

**能验证什么。** 一个沿无界模数列不符合上述二点统计的明确例子，将否定该列上 $\|T_N\|=o(L)$，从而否定其 S 预测。反向不成立：这个二点极限只听见归一于 $L$ 的族平均，漏掉 $o(L)$ 但仍远大于 S/R 阈值的误差。与 [Chandee–Lee–Liu–Radziwiłł 2014 年成果](https://arxiv.org/abs/1211.6725) 的比较仅作量词说明：其结果采用跨导子的平均与特定频率窗口，不能作为本条件推论的直接证明。这里不主张首次提出此类统计。
