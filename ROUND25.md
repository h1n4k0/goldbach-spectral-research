# 第二十五轮：次弧比较与弱 S 的局部判据

[研究状态](POST-R-STATUS.md) · [第二十四轮](ROUND24.md) · [中央谱块补记](SPECTRAL-CRITICAL.md)

沿用[李–刘原论文](https://mrc.sdu.edu.cn/english/info/1018/1514.htm)定理 6.1 的 Hardy 算子 $T_N$。记 $S_N=\mathfrak S(N)$、$L=\log N$。[Yilin Liu 的 Hexagon v1](https://hexagonmath.org/2611.00788v1) 在全局 Dirichlet GRH 下否定原假设 R；本轮没有证明或否定质性弱 S，即 $\|T_N\|=o(S_N)$。质性目标只相当于存在某个足够慢的发散率，不能代替对原 S 中预先给定的 $h(N)$ 的检验。

## 已证明的局部界

- [完整前缀的次弧比较](r25-arithmetic-minor-prefix.md)：在**全局 Dirichlet GRH** 下，对每个普通偶模数 $N\in[2X,11X/5]$，整个物理前缀 $b_N=N^{3/40}$ 的真实压缩与显式次弧算子之差，在 Hilbert–Schmidt 范数中为 $O_\epsilon(X^{-13/400+\epsilon})$。次弧均方界给出：压缩范数 $\|\cdot\|_{\rm HS}$ 超过 $X^{-1/400}$ 的模数数目为 $O_\epsilon(X^{29/40+\epsilon})$；超过 $X^{-1/100}$ 的为 $O_\epsilon(X^{37/50+\epsilon})$。这是普通偶模数上的计数，不给出任意指定稀疏子族的相对例外率，也不估计前缀外侧或全算子。
- [靠近零与靠近一的交叉](weak-s-first-alias.md)：局部 GRH(N) 用于识别真实算子。从 $0<x\le a$ 到 $4/5<y<6/5$ 的交叉范数有上界 $\ll S_N\sqrt a+L N^{-3/8}$，所以 $a=o(1)$ 时，包括 R 反例所处的整个多对数低端块，在弱 S 尺度上可忽略。固定小前缀时，该块的弱 S 小性等价于**分别**控制 $N-m$ 和 $N+m$ 两条首别名的中心化硬前缀误差。可在全局 GRH 下把它们各自化为次弧比较，但没有得到逐模数抵消。

## 尚待满足的中央判据

- [全范数充分常数与单侧正性测试](spectral-weak-s-central-threshold.md)：用原论文的归一化，常数 $h=15$ 对应的范数界若成立，就足以给出预测数量中一个固定正比例的中央素数对；常数 $h$ 不满足原 S 的发散要求。只为推出中央正性时，也可改检验严格上半中央区间上的一个正权测试，而不必先控制全范数。
- [带符号矩形判据](spectral-signed-rectangle-central-positivity.md)及[较宽的移动边缘误差预算](spectral-signed-rectangle-sharper-edge.md)：令 $p_0$ 为不整除 $N$ 的最小素数。在指定平方根乘对数幂的区间内，若实际带符号 Möbius 矩形误差 $\mathcal B_*$ 有界于 $O(N/L^{10})$，甚至只满足 $\mathcal B_*=o(NS_N^2/(L^2p_0^2))$，则在固定严格上半中央区间得到 $\gg_W S_NN/(p_0 L^2)$ 个素数对。这两个算术蕴含本身不需 GRH；**矩形误差假设没有证明**。判据给出下界，不给出渐近式，也不建立弱 S。

下一步需要对真实中央带符号误差取得逐模数控制。对前缀的密度一估计不能代替这一点，也不能代替外侧和交叉的全算子控制。
