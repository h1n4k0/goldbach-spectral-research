# 第八轮：保留 √N 以下素数数据的严格混合有限化

**新推导，不是谱小范数估计。** 对整个真实 Hardy 残差给出一个可配合矩阵验证的算术/解析混合近似：普通素数表只需到 $\sqrt N$；较大的真实字符数据用本原零点、一个显式单极点和坏 Euler 因子恢复；对角与 Beta 核由快速收敛的 Euler 修正和特殊函数求值。所有解析截断可低于 R 的阈值 $\delta_N$。现在缺的是完整的零点输入、数值验证以及最后的带符号矩阵小范数，不能把有限化当作抵消。

## 1. 字符 Gram：真正移到 s=−1 的左侧

沿用[原文](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf)及 [operator-round5.md](operator-round5.md) 的 $L=\log N$、$\alpha=1/L$、$x$ 原始对数坐标、$W(x)=1+e^{-2(\beta-\alpha)x}$。设
$$
f_{\chi,a}=\mathcal F^{-1}_{\mathrm{unitary}}\!left(\frac{g_\chi(a+it)}{1+a+it}\right),\qquad
g_\chi(s)=L'/L(1/2+s,\chi).
$$
记 $x_0=L/2$。在 $0\le x\le x_0$，
$$
f_{\chi,\alpha}(x)=-\sqrt{2\pi}e^{-(1+\alpha)x}\sum_{n\le e^x}\Lambda(n)\chi(n)\sqrt n ;
$$
只需预先筛到 $\sqrt N$，保留素数幂。等式由绝对收敛线逐项逆变换与无极点右半平面移线得到，格点处按几乎处处解释。

高侧先用本原诱导 $\chi^*$；固定 $0<\epsilon<1/2$、$a=-1-\epsilon$。在局部 GRH(N) 下，从 α 移到 a 会经过真正的零点 $s=i\gamma$ 及分母额外极点 $s=-1$；本原奇特征的首个平凡零点在 $s=-3/2$，不经过。横移可先对紧光滑 x 测试分布作，再应用第七轮的局部 $L^2$ 零点和控制。于是
$$
f_{\chi^*,\alpha}(x)=e^{(a-\alpha)x}f_{\chi^*,a}(x)
+\sqrt{2\pi}e^{-\alpha x}\sum_\gamma\frac{m_\chi(\gamma)e^{i\gamma x}}{1+i\gamma}
+\sqrt{2\pi}\,g_{\chi^*}(-1)e^{-(1+\alpha)x}.
$$
本原奇函数方程给
$$
g_{\chi^*}(s)+g_{\overline{\chi^*}}(-s)
=-\log(d_\chi/\pi)-\tfrac12[\psi((3/2+s)/2)+\psi((3/2-s)/2)] .
$$
所以 $\|f_{\chi^*,a}\|_2\ll_\epsilon L$，而 s=−1 的系数可以只保留
$c_\chi=-\log(d_\chi/\pi)-\tfrac12[\psi(1/4)+\psi(5/4)]$，误差 $|g_{\overline{\chi^*}}(1)|\ll1$（对应 L 函数实部 3/2 的绝对收敛）。**不能删除整个 s=−1 项**：其系数本身可达 $O(L)$。

最后从本原列恢复真正模 N 的列，即减去坏 Euler 恢复 $r_\chi=f_{\chi^*,\alpha}-f_{\chi,\alpha}$；它由 [source-round6.md](source-round6.md) 的显式几何前缀给定。保留所有 $p\mid N$、$p^j\le A_*=NL^2$ 的相应项；其他项仅支撑 $x\ge\log A_*$，其列误差 $\ll L A_*^{-1/2}\ll N^{-1/2}$。跳点之后每一列只是有限指数复合，可在整个正半轴使用，无须列出到 $\exp(L^2)$ 的普通素数。

用 $|\gamma|\le H$ 的认证完整零点列表构造高列。把 $\sqrt W$ 乘回各列。从 [source-round7.md](source-round7.md) 的单位区间 $L^2$ 界平方求和，加上三种附加误差，每一列（以及平均平方根）满足
$$
E\ll_\epsilon \frac{\sqrt L(L+\log(2H))}{\sqrt H}
+L N^{-(1+\epsilon)/2}+N^{-1/2}.
$$
原列平均平方范数 $O(L^2)$，因此字符 Gram 的全正半轴算子误差是 $O(LE+E^2)$。取 $H=NL^{2+\eta}$（固定 $\eta>0$），则 $O(LE+E^2)=o(\delta_N)$；取 $H=L^{2A+6}$ 则为 $o(L^{-A})$（任意预先给定固定 A）。这里取平方和得到 Gram 误差，未把单个谱窗外推到全空间。

若列表纵坐标均有严格半径 $r\le1$ 的误差区间，且各重数/编号与完整性已验证，则列的额外误差为
$$
\ll r L^{3/2}(L+\log(2H))\log(2H).
$$
因为对单频率项 $e^{(-\alpha+i\gamma)x}/(1+i\gamma)$ 关于 γ 微分，$L^2(x\ge x_0)$ 范数 $\ll L^{3/2}/(1+|\gamma|)$；随后按单位高度箱求和。Gram 误差再乘 $O(L)$。R 可取 $r=N^{-1/2}L^{-4}$；逆对数精度可取 $r=L^{-A-5}$。边界不确定时采用 H 附近宽 1 的重叠列表，保证 $|\gamma|\le H-1$ 均收录即可，尾界用 H−1。以上是假设输入已严格认证后的误差传播，不是实际认证结果。

## 2. 对角与 Beta：无需在超长区间筛素数

沿 w=s+z 且 $\Re w=2\alpha$，对角的精确解析恒等式为
$$
D_N(w)= (\zeta'/\zeta)'(1+w)
-\sum_p\frac{(\log p)^2p^{-2(1+w)}}{(1-p^{-(1+w)})^2}
-\sum_{p\mid N}\frac{(\log p)^2p^{-(1+w)}}{1-p^{-(1+w)}}.
$$
检验：$\zeta'/\zeta$ 的导数在每个 $p^k$ 产生 $k(\log p)^2$，第一个修正扣掉 $k-1$，最后精确删掉坏 p。第一修正仅筛 p 到 $Q_*=\sqrt N$；Chebyshev 分部求和给尾 $O(\log Q_*/Q_*)=O(L/\sqrt N)$，在整个 w 线上一致。第二修正用因子分解的全部坏素数求值。两个高度分母使逐点误差转成同阶 HS 误差；正轴乘 $\sqrt{W(x)W(y)}$ 仅花常数。精度已低于 R。另见 [review-round8-diagonal.md](review-round8-diagonal.md) 的 RH 直接物理尾，提供独立方案但采用不同截断及求值对象。

Beta 用 (2.12) 的因式分解：
$$K_N(s,z)=(\pi/N)^w\zeta(1+w)\zeta(1-w)A_N(w)X_1(s)X_1(z),$$
其中 $A_N$ 是 [source-round3.md](source-round3.md) 的快速积。所有 $p\mid N$ 的因子保留；其余 p 因子在 $\Re w=2\alpha$ 是 $1+O(p^{-2})$，与高度无关。双素数常数中的剩余因子也有相同界。截到 $\sqrt N$ 后，$A_N$ 的绝对误差 $O((\log L)^C/(\sqrt N\log \sqrt N))$：坏素数积由 Mertens 和 $\sum_{p\mid N}\log p\le L$ 给 $O((\log L)^C)$，好素数尾由 Chebyshev 给 $\sum_{p>Q_*}p^{-2}\ll1/(Q_*\log Q_*)$。原文的 Euler–Maclaurin/Stirling 界使高度因子至多 $CL^2(2+|t-u|)^{2\alpha}$；再乘两个线性分母可平方积分。因此 Beta 的正轴全模式近似误差
$$O((\log L)^C L/\sqrt N)=o(\delta_N).$$
求值涉及 ζ 与 gamma（及对角的 ζ 对数导数的导数）；没有假设能免费或精确算出浮点结果。

## 3. 合并为一条可检验但尚未跑过的验证路线

1. 用 [operator-round4.md](operator-round4.md) 的真实算子矩阵投影，将正轴限制到 $[0,Y_0]$ 并用宽度 d 的单位归一格指标。R 精度可选固定 Sobolev 指数 $1/3$、$Y_0=L^2$、$d=N^{-2}$，给维数 $O(N^2 L^2)$ 及 $o(\delta_N)$ 的截断/投影误差；逆对数目标可选原报告的多对数维数。矩阵精度可另选更保守参数。
2. P 列的格积分利用逐段有限指数表达；$\sqrt W$ 因子光滑，可用严格区间求积。D、K 用原 α 双高度积分与格测试函数的 Fourier 变换。由已有的高度 Sobolev 界，可将双积分截止 $|t|,|u|\le N^2$，同样给 $O(L^2 N^{-2/3})$ 的 R 型上界；逆对数目标选多对数高度。保留 Euler 近似误差的三角不等式，不能把细网格误差自动算入零点误差。
3. 最终需要带明确误差和正余量的有限 Hermitian 范数证书；即使解析尾都低于 $\delta_N$，若近似矩阵范数不小或太接近门槛，也没有结论。

**数据规模。** 普通素数表到 $\sqrt N$，保留到该处的素数幂  $O(\sqrt N/\log N)$；坏素数幂到 $NL^2$，个数 $O(L^2)$；每个奇特征的零点编号上限 $O(H\log(N(2+H)))$，所有列的输入保守 $O(\phi(N)H\log(N(2+H)))$，共 $\phi(N)/2$ 列。比如 R 的 $H=NL^{2+\eta}$ 时，零点输入可能达到 $O(N^2L^{3+\eta})$，远非轻量计算。可共享共轭与本原诱导数据，但未证明相关压缩一定带来相同理论节省；也未给经过验证的 bit 复杂度或运行时间。这一架构避免枚举到原始 $\exp(L^2)$ 的素数，但不是 S、R 的证明。
