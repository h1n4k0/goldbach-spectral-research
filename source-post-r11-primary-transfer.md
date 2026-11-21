# 固定光滑权次弧四次矩，如何真正转用到移动 Beta 矩形

**有条件改进，不是 S / R 的证明。** 使用全局 Dirichlet GRH 与 [Huixi Li–Zhixin Liu, arXiv:2610.26756v1, Theorem 1](https://arxiv.org/html/2610.26756v1#S1) 的固定权次弧四次矩。在本项目第十一轮的记号 $X=8R^2$、$N=2r^2$（$R<r\le2R$）、$J=[\log(1/2),\log(9/16)]$ 下，对某个绝对的固定小 $b>0$，有
$$
\#\{R<r\le2R:\|\mathbf1_J T_{2r^2,\log}\mathbf1_J\|_{HS}>\tau\}
\ll_\epsilon X^{1/4+\epsilon}\tau^{-2},
\qquad X^{-b/4}\le\tau\le1 .
$$
特别地，任一固定逆对数阈值的例外数 $O_{A,\epsilon}(X^{1/4+\epsilon})$。这是使用新一阶文献输入的**同一真实补偿块**改进；不是任何单一模数、整个算子或哥德巴赫猜想的证明。原始次弧论文的重证明不在这里；把其明确 Theorem 1 当作引用的条件性技术输入。

## 1. 真正适用的原文定理、不能直接套用的定理

[Althöfer–Chen–Perelli–Pintz, arXiv:2611.09386v1, Theorem 1](https://arxiv.org/html/2611.09386v1#S1) 给二次多项式值的**无表示**例外数 $O_\epsilon(R^{1/2+\epsilon})$。其 §4 使用固定全权表示数为零，而后主弧提供 $\gg Y$ 的正数量。我们的例外可能已有大量普通表示，也可能只在一个狭窄移动子窗里有任意符号的偏差；该结论本身完全不能给补偿 Hilbert–Schmidt 例外数。

真正可用的是更早一篇论文 [arXiv:2610.26756v1, Theorem 1 和权的 §2](https://arxiv.org/html/2610.26756v1#S2)。全局 GRH 蕴含其 $\Theta=1/2$ 的 $Q_\Theta$。存在固定 $\kappa\in(4/9,9/20)$，$P=Y^\kappa$，固定 Gevrey 权 $w\in C_c^\infty(0,1)$ 在 $[1/8,7/8]$ 等于 1，具有
$$
\|S_w\|_{4,\mathfrak m(P)}\ll Y^{5/8}(\log Y)^{25},\quad
S_w(\alpha)=\sum_p(\log p)w(p/Y)e(p\alpha).
$$
原文常数依赖固定 w，**不能**把该结论直接替换成随 s 和 $Y$ 变化的硬/平滑权。以下只在一个固定普通素数因子上使用这一定理；无须扩大或平移其次弧。

## 2. 只剩一个真正自适应的窗口

将 $s=2r^2\in(X/4,X]$ 分为常数个值域 $Y/2<s\le Y$（$Y=X$ 或 $X/2$）。在原始归一化前的 Beta 活动块所有有用硬矩形都满足 $n,m\le(9/16)s$；在 $n+m=s$ 后也有 $n,m\ge(7/16)s$。所以两个原始坐标都在 $[7Y/32,9Y/16]\subset [Y/8,7Y/8]$。不同 s 可以有任意选定的矩形，甚至由最大偏差自适应选择。将两窗并成唯一 n 区间 $I_s=I_s^{(1)}\cap(s-I_s^{(2)})$，m 端的原权 w 已准确为 1。

令 $\Delta=Y^{-b}$，以非负、质量 1、支撑 $[-\Delta,\Delta]$ 的平滑小窗卷积“缩进”和“扩张”的 $I_s/Y$，得 $v_{s,-}\le\mathbf1_{I_s/Y}\le v_{s,+}$，$0\le v_{s,\pm}\le1$。过窄内窗取零，空窗可直接处理；非空单点也由外窗覆盖。每项权支撑在一个固定的紧子区间，移动 m 端至多 $O(\Delta)$，仍在 w 的 1 平台。任意固定 j 阶导数 $O_j(\Delta^{-j})$，且连续主项 $Y\int v_{s,\pm}(u)w(s/Y-u)du$ 与 $|I_s|$ 只差 $O(Y\Delta)$。

选定 $E$（$M=|E|$）和任意 $|\sigma_s|\le1$。在任一共同的卷积平移参数处，n 权正是任意随 s 变化的一个硬区间（端点不需要冻结）。将每个 n 区间拆成整数网格上的标准 dyadic 区间，每一尺度至多两块。固定尺度对每个区间 B 写
$$
P_B(\alpha)=\sum_{p\in B}\log p\,e(p\alpha),\qquad
Q_B(\alpha)=\sum_{s=2r^2\in E:\ B\text{ 被选}}\sigma_s e(-s\alpha).
$$
若 $M_B$ 是这个子集的大小，平方差分解 $(r-u)(r+u)$ 与正交性给 $\|Q_B\|_4\ll_\epsilon \sqrt{M_B}Y^\epsilon$（与 [Round 11](arithmetic-post-round10-exceptions.md) 同一个适用于带符号子集的证明）。在给定尺度上 $\sum_B M_B\le2M$，且块 B 不交，$\sum_B\|P_B\|_2^2\ll Y\log Y$。应用 $(4,2,4)$ Hölder、再在 B 上 Cauchy，然后对 $O(\log Y)$ 尺度求和，给
$$
\left|\sum_{s\in E}\sigma_s\int_{\mathfrak m(P)}
S_{v_{s,\pm}}(\alpha)S_w(\alpha)e(-s\alpha)d\alpha\right|
\ll_\epsilon \sqrt M\,Y^{9/8+\epsilon}.
$$
卷积平移只是对上述一致的区间估计取正平均。这个步骤（[spectral-post-r11-adaptive.md](spectral-post-r11-adaptive.md) 的自适应区间分解）不向固定 w 的文献定理要求额外一致性。

## 3. 主弧：平滑窗口的一致性独立推出

说明用 $P=Y^\kappa$（超过第十一轮的 $Y^{1/3}$ 界）为什么合法。以下独立重做 [Li–Liu Proposition 4.1 的主弧误差步骤](https://arxiv.org/html/2610.26756v1#S4.SS2)，使用更强的全局 GRH。两权 v 均有上节的支撑与导数界。设 $\rho=(1-2\kappa)/8>0$，固定 $0<b<\min(\rho,\kappa)/100$。

在 $|\beta|\le P/(qY)$ 上，对每个模 q 特征的本原诱导对应，将相应 von Mangoldt 和经 Mellin 显式公式扣掉极点，误差记 $E_{\chi^*,v}(\beta)$。取 $H_q=Y^\rho P/q$。非平凡零点高于 $H_q$，不可能与 $Y\beta$ 形成驻相；在固定支撑反复积分分部，对任一固定 a 有 Mellin 衰减 $O_a(Y^{1/2}\Delta^{-a}(1+|\gamma|)^{-a})$。由于 $H_q\ge Y^\rho$ 且 $b<\rho$，选足够大的 a 后，高尾为 $O(Y^{-10})$。平凡零点至多给 $O(1)$（可能的零点在 0，其余由支撑 $u\asymp Y$ 几何衰减）。零点实部均为 1/2。有限零点和应用整个 β 实轴上的 Plancherel，其配对核为
$$
e^{i(\gamma-\gamma')\log Y}
\int|v(u)|^2u^{-1+i(\gamma-\gamma')}du
\ll \Delta^{-2}(1+|\gamma-\gamma'|)^{-2}
$$
（最后一项是模长界）。单位区间计数 $O(\log Y)$ 及总数 $O(H_q\log Y)$ 因而给
$$\int_{|\beta|\le P/(qY)} |E_{\chi^*,v}(\beta)|^2d\beta
\ll H_q\Delta^{-2}(\log Y)^C.$$
此处按 q 而非按本原导子统一取 $H_q$，避免不必要的诱导权重损失。

在固定 q 对既约分子做有限 Parseval。Gauss 系数为 $\tau_q(\bar\chi)/\phi(q)$，且 $\sum_\chi|\tau_q(\chi)|^2=\phi(q)^2$，故 q 的积分误差平方至多 $O(\phi(q)H_q\Delta^{-2}(\log Y)^C)$。模 q 去掉坏 Euler 与非单位项在固定倍比窗至多 $O(\log q)$；从 von Mangoldt 改到普通素数每个 α 至多 $O(Y^{1/2}(\log Y)^2)$，在弧的总测度 $O(P^2/Y)$ 下平方贡献 $O(P^2(\log Y)^4)$。于是总误差能量为 $O(Y^\rho P^2 \Delta^{-2}(\log Y)^C)$，指数 $\rho+2\kappa+2b<1$ 有足够余量。

两低频主项 $V_v(a/q+\beta)=\mu(q)Y\widehat v(-Y\beta)/\phi(q)$ 的 $L^2$ 质量 $O(Y\log Y)$（直接 Plancherel）。Cauchy 把乘积主弧的误差降为 $O(Y^{1-c})$，其中 c 可取 $>2b$；对每个 s 单独成立。完成 β 积分时，从各权二阶导数得到绝对尾 $O(Y\Delta^{-4}(q/P)^3)$；Ramanujan 的逐 s 加权截尾给 $O_\epsilon(Y^{1+\epsilon}\Delta^{-4}/P)$（见 R11，权 $(q/P)^3\le q/P$）。完成 q 级数的较大分母尾为 $O_\epsilon(Y^{1+\epsilon}/P)$。按 b 的选择，这些也在 $O(Y^{1-c})$ 内（若需要降低 c）。完整连续积分正是 $|I_s|+O(Y\Delta)$，且奇异级数逐个 s，而非平均。

## 4. 取真正的自适应块例外

主弧误差与次弧组合，正夹逼并对两个模型差取绝对值，得到任意所选 E 上的区间偏差（归一到 s 或可比的 Y）：
$$
\sum_{s=2r^2\in E}
\sup_{\text{该块硬矩形}}
\left|\frac{A_s-\mathfrak S(s)V_s}{s}\right|
\ll_\epsilon \sqrt M X^{1/8+\epsilon}+ M X^{-b} \log X.
$$
可先选每个 s 的近最坏区间再选符号，不存在对端点的 union bound。单位限制和真素数幂改回原算子至多 $O(X^{-1/2}(\log X)^2)$，已吸收。两倍平方值域之和 Cauchy 把 $\sum\sqrt{M_j}$ 吸收到 $O(\sqrt M)$。

在 J 内只有 $u+v=1$ 别名，D 已精确扣除。正 layer cake 及有界 Hardy 核乘子给**逐模数** $\|\mathbf1_JT_{s,\log}\mathbf1_J\|_{HS}\ll$ 上式中的矩形最大归一偏差（同 [spectral-post-r11-adaptive.md](spectral-post-r11-adaptive.md) §2，不需额外上筛平方损失）。选 E 为阈值例外，$MX^{-b}\log X=o(M\tau)$；于是 $M\tau\ll_\epsilon\sqrt M X^{1/8+\epsilon}$。平方并重标 ε 得首式。

**确切剩余。** 该估计连 $M=1$ 都没有在目标 τ 下排除，且只覆盖 Beta 活动第一和线的小型固定块。尤其不能把它换成充足的逐模数上界，或移除 full GRH 的辅助模数要求。若想推广到 R12 的增长前缀，必须另处理落在固定权平台外的原始尺度、差别名和随尺度增长的损失；本报告不声称已经完成。
