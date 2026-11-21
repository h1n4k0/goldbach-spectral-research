# 李–刘 Goldbach 谱假设：独立研究笔记

> **研究导航：** [转攻弱 S](POST-R-STATUS.md) · [第二十五轮 · 弱 S 的局部判据](ROUND25.md) · [中央正性的平滑截断判据](spectral-signed-rectangle-smooth-bridge.md) · [中央正性的单模数 L¹ 判据](spectral-signed-rectangle-l1-no-jump.md) · [中央 L¹ 判据的上端截去](spectral-l1-profile-upper-tail.md) · [双外侧与中央 Type I 约化](WEAK-S-SECTOR-REDUCTIONS.md) · [中央 Type II 的两块消去](CENTRAL-TYPE-II.md) · [近平衡 Type II 条带](weak-s-type-ii-wright-near-balanced.md) · [严格平衡区的绝对值障碍](weak-s-type-ii-exactly-balanced-diagonal.md) · [双外侧与双素数腿的中心化](WEAK-S-CENTERING.md) · [中央双侧相关的主弧](r32-source-double-giant-major-arcs.md) · [次弧内的窄有理数邻域](r33-source-signed-minor-rational-cores.md) · [谱路线临界区](SPECTRAL-CRITICAL.md) · [中央除数配对消去](CENTRAL-DIVISOR-ORBITS.md) · [第二十四轮 · 几乎所有偶数的前缀界](ROUND24.md) · [第二十三轮 · 巨大素因子与中央抵消](ROUND23.md) · [第二十二轮 · 保留宽截断的中央核](ROUND22.md) · [外侧算子补记](OPERATOR-EXTERIOR.md) · [外侧算子续记](OPERATOR-EXTERIOR-FOLLOWUP.md) · [第二十一轮 · 混合长除数区的消去](ROUND21.md) · [第二十轮 · 混合区筛减与平衡除数区](ROUND20.md) · [第十九轮 · 高乘积区的一类逐模数消去](ROUND19.md) · [第十八轮 · 真正的长–长区域与尾部界](ROUND18.md) · [第十七轮 · 长–长项与外侧模型](ROUND17.md) · [第十六轮 · 逐模数剥离短除数项](ROUND16.md) · [第十五轮 · 更大的完整前缀](ROUND15.md) · [第十四轮 · 非对称外侧交叉](ROUND14.md) · [第十三轮 · 固定块的更强均方界](ROUND13.md) · [第十二轮](ROUND12.md) · [第十一轮](ROUND11.md) · [第十轮](ROUND10.md) · [第九轮求积停机记录](spectral-round9.md) · [第八轮](ROUND8.md) · [第七轮](ROUND7.md) · [第六轮](ROUND6.md) · [第五轮](ROUND5.md) · [第四轮及数值复算](ROUND4.md) · [第三轮](ROUND3.md) · [第二轮](ROUND2.md) · [第一轮原始快照](https://github.com/h1n4k0/goldbach-spectral-research/blob/9cb40f4c80f0fa298dea3e02d82ae4f2a7ae9c06/README.md)
>
> **现状：** [Yilin Liu 的预印本给出 R 在全局 Dirichlet GRH 下的反证；较弱的 S 仍开放。](POST-R-STATUS.md) 下方保留原第一轮记录。

**第一轮快照 · 2026-11-20。S 和 R 均未证明，也未被否证。** 下列是对真实算子或其可明确定义的压缩、算术矩阵元所作的推导；“交叉核对”只指本笔记内部的独立重算，不是期刊同行评议，也不作优先权声明。

**起点。** 李嘉旻、刘建亚的[山东大学发布页](https://mrc.sdu.edu.cn/info/1018/2193.htm)与[作者的 63 页论文](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf)。设 $L=\log N$，$S_N=\mathfrak S(N)$ 为奇异级数，$\delta_N=\sqrt{S_N/N}\,L^{3/2}$，$\eta_N=h(N)^2L^3/(NS_N)$。固定原带宽 $\alpha_N=1/L,\beta=1/8$，在满足 $\mathrm{GRH}(N)$ 的每个充分大偶数上，必须控制的是同一真实自伴算子 $T_N$ 的**最大绝对特征值**：

- **S(h)**：$\|T_N\|\le S_N/[2h(N)\sqrt{1-\eta_N}]$，其中 $h\to\infty$ 事前指定且最终 $\eta_N\le1/4$；
- **R**：$\|T_N\|\le\delta_N$，常数必须是 1。R 推出每个合适的 S(h)。论文给出的 GRH 上界是 $O(L^2)$，仍不足。

## 从哪里读起

| 文件 | 本轮得到什么 | 边界与核查程度 |
|---|---|---|
| [source.md](source.md) | 一般窗口可拆成两种差卷积与一种和卷积；第一个半格的**整个压缩**为零。去掉这个零块后得到两个谱阈值的等价 Schur 判据。 | 支撑选择规则及 Schur 恒等式已交叉核对。零压缩并非零作用。 |
| [operator.md](operator.md) | 右–右核在 Hilbert–Schmidt 范数下为 $O(N^{-1/8}L)$。另有离左边界足够远的内线衰减和单个 Beta 分量估计。 | 固定右边界证明已交叉核对。带可变参数的完整不等式和单项精细界附推导，供进一步核查。它们不是全算子上界。 |
| [arithmetic.md](arithmetic.md) | 任意**固定**物理窗口的压缩范数有 $O_{a,b}(S_N)$ 界；更强地，在族 GRH 下，该压缩范数的**平方在偶模数的平均趋零**。其必要的固定测试矩阵元均方算术估计本身无条件。 | 已核对复杂度一四线性型、局部因子、混合矩与固定窗口有限网。用到 [Green–Tao 的线性素数型定理](https://annals.math.princeton.edu/2010/171-3/p08)。平均而非每个 $N$；无显式速率。 |
| [spectral.md](spectral.md) | $\sum_j|\mu_j|\ll L^2$（迹类）；固定 $N$ 的正负谱均为无穷，且有显式尾部下界。因此超出 R 阈值的谱因子数至多 $O(\sqrt{NL/S_N})$。 | Euler 求和迹类分解、$H^1_0$ 点值/min–max 下界已独立核对。例外个数上界不等于零。 |
| [review.md](review.md) | 澄清“存在 $h$／预定 $h$／所有 $h$”。另推导固定 Goldbach 窗的同余类有符号平均：在 Dirichlet GRH 下，即使 $q=o(X/\log^2X)$，仍得到相对主项趋零的总误差。 | 有完整 Parseval/CRT 推导；局部系数另作 4,095 组精确枚举。该平均定理待外部独立复核。它不隔离指定的 $N$。 |

## 明天可直接复核或继续的三件事

1. **查归一化。** 按原文 (2.1)、(2.12)、(2.17)、(2.37) 和定理 6.1 核对符号、双边正弧长与 $2\pi$，再用一对反射窗口验证矩阵元。若以 $N=30030$ 作例，原文附录 B 的有限计数校验不应被当成谱范数认证。
2. **针对最难的块。** 用 [source.md 第五节](source.md) 的精确分解 $T_N=\bigl(\begin{smallmatrix}0&B\\B^*&C\end{smallmatrix}\bigr)$。令 $M$ 取 S(h) 或 R 的阈值，所缺的具体引理是：对所有剩余单位向量 $y$，证明 $\|By\|^2/M+|\langle Cy,y\rangle|\le M$。首要待查是物理窗口逃逸、交叉作用及 $\alpha_N$ 左边界层，不能将已小的单块推广为全范数。
3. **区分可证伪与不可证实的数值结果。** 明确测试函数、误差区间和完整 Hardy 范数，才能用一个矩阵元给出**下界**。若它超过某一阈值，只能否定那个固定 $N$ 的局部版本；要否定最终成立的 S/R，须处理无界的 $N$ 序列。要从截断矩阵给出**上界**，须另证截断与真算子之差的算子范数上界。

另一个明确的研究问题是，能否对**每个**充分大偶数，控制 $X^{-1}\sum_r E_r(f)E_{a-r}(g)$ 的有符号抵消，而不是仅估计两个向量的长度（见 [review.md](review.md)）。这最多先解决特定窗口；全算子仍需对所有方向统一。以上笔记主要给出解析证明，无须私有数据或软件；原文只作链接，不在本包重发。
