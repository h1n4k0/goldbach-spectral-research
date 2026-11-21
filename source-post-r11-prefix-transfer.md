# 同一个固定权次弧定理，也可用于增长前缀

**延伸结论，引用一项预印本定理，不证明 S 或 R。** 在全局 Dirichlet GRH 和 [Huixi Li–Zhixin Liu，arXiv:2610.26756v1，Theorem 1](https://arxiv.org/html/2610.26756v1#S1) 的前提下，沿 [arithmetic-round12-prefix.md](arithmetic-round12-prefix.md) 的固定二次多项式偶数族，$N=2F(r)\asymp_F X$、$R<r\le2R$，有
$$
\#\{r:\|\Pi_b T_{2F(r),\log}\Pi_b\|_{HS}>\tau\}
\ll_{F,\epsilon} \tau^{-4}b^{17/4}X^{1/4+\epsilon},
\quad b\ge1,\quad 0<\tau\le1,\quad b^2\tau^{-2}\le X^{1/40}.
$$
原点包括在前缀内。例：$b=X^{1/100}$、$\tau=X^{-1/400}$ 满足最后条件，得 $O_\epsilon(X^{121/400+\epsilon})$ 个例外；不能换成逐模数或全空间。与 [固定首个 Beta 块](source-post-r11-primary-transfer.md) 不同，本式承担 $b^{17/4}\tau^{-4}$，处理的是许多和/差线的完整增长前缀。

## 1. 平台问题：始终选大的一侧

对固定 $k$ 和目标线 $n+m=kN$ 或 $|n-m|=kN$，按两个原始素数位置的大小分段，大的一侧称 m。和情形分成 $m\ge n$ 和换位后的 $m>n$，确保没有对角重复；现有单位限制也排除了真对角例外。差情形只需选择方向。无论哪种，在实际支持中 $m\ge kN/2$，另一变量不大于 m。

将 m 分别限制在 $[V,2V)$，V 取二进窗口，设置文献参数 $Y=4V$。则 $m/Y\in[1/4,1/2]$，始终在固定权 w 的平坦区 $[1/8,7/8]$ 内，并且目标 $s=kN\le Y$。实际两个移动硬区间、m 的二进窗及大小关系，沿单线相交后还是**一个 n 区间** $I_r\subset[0,Y]$。因此可把大的 m 因子完全换成原文固定 $S_w(\alpha)$，所有自适应性放进一侧 $P_{I_r}(\alpha)$；不移动或扩大文献的圆弧，不需要 w 对很小 n 也等于 1。每个出现的 Y 均在 $c_F X\le Y\le C_F bX$，且每条线二进区间数 $O(1+\log b)$。

固定二进窗，用 [spectral-post-r11-adaptive.md](spectral-post-r11-adaptive.md) 的单区间 dyadic 分解。对任意选中集合 E 的带符号二次和，$\|Q_I\|_4\ll_{F,\epsilon}\sqrt{|E_I|}X^\epsilon$：相邻值差 $k(F(r)-F(u))=k(r-u)(a_2(r+u)+a_1)$，固定 k 不改能量。应用 $(4,2,4)$ Hölder，依次是文献固定 $S_w$ 的次弧第四矩 $Y^{5/8}(\log Y)^{25}$、自适应一侧的分块 Parseval、任意选中子集的第四矩。在同尺度各块上 Cauchy 后给 $\sqrt{|E|}\,Y^{9/8+\epsilon}$，各尺度对数损失吸收入 $\epsilon$。差线若一端取共轭，所有使用的范数与能量保持不变。

## 2. 不平滑硬区间的较大主弧界

固定文献给的 $P=Y^\kappa$，$4/9<\kappa<9/20$。以下证明对自适应硬区间一致，不沿用传统的逐点 $1+Y|\beta|$ 平方误差。根据局部于每个辅助模 q 的 GRH，任一特征的原始前缀去掉主特征主项后，$E_\chi(t)\ll\sqrt Y(\log(2qY))^2$，$0\le t\le Y$，uniform in endpoints；见 [原始显式公式](https://link.springer.com/article/10.1007/s00208-026-03383-y#Sec2) Lemma 2、局部零点计数及 RH 的主特征版本。对任一硬区间 $I$，盘算 Abel 变换：
$$
E_{\chi,I}(\beta)=\text{两个端点误差}
-2\pi i\beta\int_I E_\chi(t)e(t\beta)dt .
$$
在 $|\beta|\le P/(qY)$，端点平方积分为 $O((P/q)L^4)$；其余项用 Plancherel 在全实轴上控制积分项，再取 $|\beta|^2\le(P/(qY))^2$，给 $O((P/q)^2L^4)$。加权固定侧 w 由有界全变差的硬前缀叠加，Minkowski 给同一界。对每个 q 的既约分子做 Gauss Parseval，$\sum_\chi|\tau_q(\chi)|^2=\phi(q)^2$，所以误差的平方总积分为 $O(P^2L^5)$。去掉非单位和真素数幂的简单修正亦在该界内。

主项由 $\mu(q)/\phi(q)$ 乘连续 Fourier 因子构成；其两侧的平方积分 $O(YL)$。Cauchy 因而给逐个 s 的系数误差
$$
O(\sqrt Y P L^3+P^2 L^5+Y^{1+\epsilon}/P).
$$
最后一项来自 Ramanujan 系数绝对尾和连续积分尾；对硬区间及 w 的变差积分都给 $\ll\min(Y,|\beta|^{-1})$，因此 [R11 §1](arithmetic-post-round10-exceptions.md) 的逐个 s 计算照用。完整的几何因子恰是 m 在固定 w 平台时的硬区间长度。由于 $\kappa<9/20$，取 $\nu=1/20<1/2-\kappa$，所示总误差为 $O(Y^{1-\nu})$。需要的是全局 GRH（这里用到 q≤P），不能只假设被测模数 N 的局部 GRH。

## 3. 将新的每线估计代入现有前缀证明

对固定线、任意每 r 的窗口，选最终残差符号，二进窗求和，再按 $N\asymp_F X$ 归一。上两节给出替换 [R12 前缀证明](arithmetic-round12-prefix.md) (2) 的
$$
\sum_{r\in E}|\Delta_r|
\ll_{F,\epsilon}\sqrt M\, b^{9/8}X^{1/8+\epsilon}+M b X^{-\nu}.
$$
二进窗的 $Y^{9/8+\epsilon}$ 与 $Y^{1-\nu}$ 均由最大相关尺度的阶支配（也可把对数损失吸收到 $\epsilon$ 和固定的指数余量中）。加回真素数幂和单位限制的逐线 $O(\sqrt{bX}\,L^2/X)$ 远小于 $bX^{-\nu}$。每条线的相交模型依旧居中于实际奇异级数 $\mathfrak S(kN)$；不只检测表示是否存在。

前缀上有 $O(b)$ 条别名。其余按 R12 的原证明：正层饼，较短边筛与有效的 $x=0$ 边缘估计。具体得到
$$
\sum_{r\in E}\|\Pi_bT_{2F(r),\log}\Pi_b\|_{HS}^2
\ll L^C(\sqrt M\,b^{17/8}X^{1/8+\epsilon}+M b^2 X^{-\nu}),
$$
因为层饼的选集 $L^1$ 界带 $1/\sqrt{xy}$，独立的短边筛给个体核上界 $\ll\mathfrak S(N)\sqrt{xy}$，两者相消；零边缘误差 $O_F(bX^{-1/4}L^4)$ 也吸收进第二项。让 E 为异常集，条件 $b^2\tau^{-2}\le X^{\nu/2}$ 保证第二项 $o(M\tau^2)$。平方余下 $M\tau^2\ll\sqrt M b^{17/8}X^{1/8+\epsilon}$，吸收对数即得结论。

仍缺充分大的每个 N 上的点态控制和前缀到外区的算子范数。任何一条选集估计在 $M=1$ 时仍允许远大于目标的误差。
