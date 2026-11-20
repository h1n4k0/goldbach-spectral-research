# 独立复核：中心有符号矩与缩小窗二点极限

逐式复核 [review-refined-gaps.md](review-refined-gaps.md) 和 [review-shrinking-gaps.md](review-shrinking-gaps.md)。两篇的条件性推导成立。没有发现 S、R 的证明或反例。原四/五轮材料未改动。

## 中心矩与尺度归一

* $D_0=I\mathbb E_- b_\chi+\int FG$ 恰由 Parseval / Weil 得到，其中 $a^2$ 的逆变换是 $F*F$。$2w<\log2$ 保证这一公式在原点的素数项为空，且导子尖峰不与任意素数项重叠。
* 对角积分换元后为 $2\int F(v)^2\sum_{n\le e^{t_0+v},(n,N)=1}\Lambda(n)^2/n\,dv$。$F$ 为偶，积分中的线性项消去；$\sum_{n\le e^s}\Lambda(n)^2/n=s^2/2+O(1)$，减去坏素数幂的代价 $O((\log L)^2)$。原点不会截断任何素数幂窗口。在 $t=L+O(1)$ 的边缘区，非对角别名由有限条线及二元上筛给 $O(\mathfrak S(N))$。
* 全特征族的导子亏损沿 $p$ 独立，二阶矩可由 $e-v_p(d)\ge j$ 的概率 $\phi(p^{e-j})/\phi(p^e)\ll p^{-j}$ 得到。奇族对此非负二阶矩最多放大 2 倍。于是受控的主代数项恰是 $I\mathbb E_-(b_\chi-t_0)^2+2(\int FG)(\mathbb E_-b_\chi-t_0)$，得到 $O((\log L)^2)$ 的有符号总积分。
* $t^2$ 矩的极限是 $2I\int_0^1 u^2(u-1)du=-I/6$；导子原子不贡献。将 $\psi(t/T)$ 作偶次 Taylor，乘 $T^3/L^4$、保留输入 Fourier 的 $dt/T$，得到二阶系数 $-I\psi''(0)/12$。以 $\psi(v)=(2\pi)^{-1}\int f(y)e^{-ivy}dy$ 展开，极限密度恰为 $I y^2/(24\pi)$，在 $[-b,b]$ 的质量 $I b^3/(36\pi)$。
* S 的 $T=L(\log L)^\kappa$（$0<\kappa<1$）与 R 的 $T=L^{2-\epsilon}$（$0<\epsilon<1$）都满足：常数项误差 $T^2(\log L)^2/L^4\to0$；四阶余项 $L^2/T^2\to0$；固定紧频率外区上界经归一化后趋零。翻译测试时用 $\cos(sv)$ 可保留常数项消去，得到多项式局部质量 $O(1+s^2)$；不能直接用未中心化的 $A$ 来界。

量词澄清：归一的 $\omega_{N,T}(\{0\})=o(1)$；未归一的异编号重零点加权计数是 $o(L^4/T^3)$。结论针对指定固定高度窗下的平均配对，不是单特征最近邻分布，也不是把固定窗弱极限直接用于随 N 收缩的区间。

## 额外的无条件交叉项估计

这里的平均是模 $N$ 奇特征平均，$R_p(t)$ 表示从模 $N$ 导出特征恢复到本原诱导特征时，坏素数 $p\mid N$ 的增补素数幂和；$R=\sum_{p\mid N}R_p$，$P$ 是模 $N$ 导出特征素数多项式。固定 $t_0=L+C$，有
$$
 \int_0^{t_0}\left|\mathbb E_- P\overline R\right|dt\ll_F L^3/\phi(N),
 \qquad
 \int_0^{t_0}\mathbb E_-|R|^2dt\ll_F1.
$$

第一式：设 $p^e\Vert N$、$M=N/p^e$。$R_p$ 只来自导子与 p 互素、即通过模 M 诱导的奇特征。对 $(n,N)=1$，对应精确有限族相关系数是
$$
 \mathbb E_-\left[\chi(n)\overline{\chi^*(p^j)}\mathbf1_{p\nmid d_\chi}\right]
 =\frac{\phi(M)}{\phi(N)}
 [\mathbf1_{n\equiv p^j\bmod M}-\mathbf1_{n\equiv -p^j\bmod M}].
$$
当 $M\le2$ 时右边也恰为零。两个时间窗重合只在 $n\asymp_F p^j$。若 $p^j<c_F M$，差的同余仅能是整数相等（但 $p\mid n$ 被排除），和的同余不可能。其余候选每个 j 数目 $O_F(1+p^j/M)$，乘每项绝对权重 $O_F((\log p)(1+j\log p)/p^j)$ 与有界的时间积分长度；求和至 $p^j\ll_F N$ 得 $O_F(L^2/M)$。再乘精确系数的比例 $\phi(M)/\phi(N)$，对至多 $O(L)$ 个 p 求和。

第二式：同一个 p 的不同幂时间窗不相交，因为 $\log p\ge\log 2>2w$，而 $\mathbb P_-(p\nmid d_\chi)\le2/\phi(p^e)$，故同底 p 的平方贡献不超过 $C_F(\log p)^2/[(p-1)\phi(p^e)]$，对 p 甚至可用全素数收敛级数求和。对 $p\ne q$，共同条件是导子与 pq 互素，即由 $M=N/(p^{v_p(N)}q^{v_q(N)})$ 诱导。模 M 奇正交要求 $p^j\equiv\pm q^k\pmod M$。因两者为不同底的素数幂，且时间窗重合只在二者成固定倍比时，$p^j<c_F M$ 的候选全部消失。对每个 j，至多有 $O_F(1)$ 个 k；对剩余 j 用几何级数求和得 $\sum 1/p^j\ll_F1/M$。连同比例因子，交叉贡献 $O_F(\log p\log q/\phi(N))$，总计 $O_F(L^2/\phi(N))$。由 Cauchy，$R$ 与固定 gamma 项的总积分交叉也改进为 $O_F(1)$。

此处无条件是指从有限特征正交得到的素数和估计，不是对原算子或零点声明无条件结论。它将本原恢复误差从中心主瓶颈中剥离；尚未给出大尺度双零点协方差或 S/R 范数的上界。
