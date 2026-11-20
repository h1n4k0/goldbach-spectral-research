# 第六轮：远块本原恢复项、精确相关输入和现有定理的边界

**结果。** 对真实远块，使用模数约化的奇正交性，把较大尺度的本原恢复误差压成 N 的负幂；同时给出全模式的远带恢复项界。主项仍是固定同一模数的带符号两尺度进程协方差，未获得 S/R 所需界。以下与共同窗零点间距工作无重叠。

## 1. 较大尺度的本原恢复交叉：无条件有限和估计

固定实或复值窗 $f,g\in C_c^\infty(0,\infty)$，令 $X\ge C_{f,g}Y\ge C_{f,g}$ 足够分离，使 $m\asymp_f X$ 和 $n\asymp_g Y$ 两个窗不相交。记
$$
P_X(\chi)=X^{-1/2}\sum_m\Lambda(m)\chi(m)f(m/X),\qquad
R_X(\chi)=X^{-1/2}\sum_m\Lambda(m)[\chi^*(m)-\chi(m)]f(m/X),
$$
其中 $\chi^*$ 是 $\chi\bmod N$ 的本原诱导对应，低侧 $P_Y$ 用窗 g。则
$$
\boxed{\ |\mathbb E_- R_X\overline{P_Y}|\ll_{f,g}
\frac{L\log(2Y)}{\phi(N)\sqrt{XY}}\,[Y+\min(X,N)]\ ,\qquad L=\log N.\ }
$$

证明：恢复项只出现于 $m=p^j$、$p^e\Vert N$，且仅在 $p$ 不整除本原导子时出现。令 $M=N/p^e$。由模 M 的奇正交，对低侧单位 n，平均 $\chi^*(p^j)\overline{\chi(n)}$ 连同上述导子条件，恰为
$$
\frac{\phi(M)}{\phi(N)}
\big[\mathbf1_{n\equiv p^j\ (M)}-\mathbf1_{n\equiv-p^j\ (M)}\big].
$$
没有 $n=p^j$ 项。若任何同余出现则 $M\ll_{f,g} X$；低侧候选 $O_g(1+Y/M)$ 个。乘 $\phi(M)\le M$ 后至多 $O_{f,g}(Y+\min(X,N))$；固定倍比窗内每个 p 至多 $O_f(1)$ 个 j。再用 $\Lambda(n)\ll_g\log(2Y)$、$\sum_{p\mid N}\log p\le L$，得到结论。对 $Y\le X$，方括号除以 $\sqrt{XY}$ 至多 $1+\sqrt N$，所以在本项目涉及的 $\log(2Y)\ll L^B$ 内，这是 $O_{f,g,B}(L^{B+1}\sqrt N/\phi(N))$，比任意逆对数小。没有假设零点或素数进程猜想。交换窗仅在恢复项处于高侧时给同样界；不能默默把两端都换为本原并沿用此论证。

## 2. 全模式的远带恢复项

用 [operator-round5.md](operator-round5.md) 的原始对数坐标 $x=\log n$、$f_{\chi,\alpha}$ 与 $W$。在绝对收敛线直接 Fourier 反演（再移至 $\alpha$），或对有限每个 Euler 恢复项逐项反演，得
$$
r_\chi(x)=f_{\chi^*,\alpha}(x)-f_{\chi,\alpha}(x)
=-\sqrt{2\pi}e^{-(1+\alpha)x}\!
\sum_{\substack{p\mid N,\ p\nmid d_\chi\\p^j\le e^x}}\log p\,\chi^*(p^j)p^{j/2}.
$$
对任意单 p，几何求和 $\sum_{p^j\le e^x} p^{j/2}\ll e^{x/2}$，故 $|r_\chi(x)|\ll L e^{-(1/2+\alpha)x}$。在 $x\ge y+B$、$y\ge0$，两侧真 Hardy 权 $\sqrt{W(x)W(y)}$ 有界。用纸面平均 $\mathbb E_-\|f_{\chi,\alpha}\|_2^2\ll L^2$（局部 GRH），有
$$
\left\|\mathbf1_{x\ge y+B,\ y\ge0}\sqrt{W(x)W(y)}\,
\mathbb E_- r_\chi(x)\overline{f_{\chi,\alpha}(y)}\right\|_{HS}
\ll L^2 e^{-B/2}.
$$
这是对整个远带高侧恢复项（含所有矩阵模式）的真实控制，而不是单个固定窗。配合远移线，只剩真实导出 odd-prime Gram 的主协方差；不能把这个很小的附加项误当成主协方差。

## 3. 精确还缺什么

对窗分离的 $X,Y$，导出特征的真正主协方差是
$$
\mathcal C_N(X,Y;f,g)=\mathbb E_-P_X\overline{P_Y}
=\frac1{\sqrt{XY}}\sum_{n\approx Y}\Lambda(n)\overline{g(n/Y)}\mathbf1_{(n,N)=1}
\left[\sum_{m\equiv n\ (N)}\Lambda(m)f(m/X)-\sum_{m\equiv -n\ (N)}\Lambda(m)f(m/X)\right].
$$
特别地，扣掉相同的主项是精确的；缺的不是主项识别，而是检测由短侧 Λ 选择并加权的剩余类方向时，高侧两进程误差的带符号抵消。这与仅证明 $\sum_a|E_X(a)|^2$ 的单尺度 Hooley 方差不等价。全模式输入应控制同一 mod N 的两尺度反射反对称进程向量内积，作为二维有符号核（或其有限远块矩阵）而非仅某一窗的数值。

一个定量对照：若额外具有点态 Montgomery 型的 $\sqrt{X/N}X^\varepsilon$ 进程误差，且适用于固定倍比平滑窗口和该模数范围，则逐个 n 代入上式给 $|\mathcal C_N|\ll_{f,g,\varepsilon}\sqrt{Y/N}X^\varepsilon$。所以在 $X\le N^A$、$Y\le N^{1-\tau}$ 且 $N\le X^{1-\varepsilon}$ 的有界幂次范围，取 $\varepsilon<\tau/(4A)$ 会给真实的负幂解耦。这个计算恰说明该输入的局限：两侧都超过 N 时没有这样的收益，在超多项式范围固定的 $X^\varepsilon$ 也不可用。因此即使添加此强一阶输入，仍不等于解决全远块。

## 4. 文献核对

* [Kandhil–Languasco–Moree（2026）Theorem 3 与公式 (9)、(17)](https://link.springer.com/article/10.1007/s00208-026-03383-y)：其确有 GRH 下的成对结果，但对固定剩余类含 $\chi_1,\chi_2$ 混合和，且需零点高度 $T\ge X/\phi(q)$ 与 $q\le\sqrt X/(\log X)^{2+\varepsilon}$。这里关键窗的绝对零点高度固定或有光滑衰减，且只在同一奇特征内取协方差，两者不是同一个对象。文中的 Theorem 4 确给上述点态 Montgomery 误差，但额外使用尚未证明的 Conjecture 2，不能作为 GRH 单独推论。
* [Travor Z. H. Liu（2026-11-16），§§6–8](https://hexagonmath.org/pdf/2611.00509v1)：固定素模、所有本原特征的单尺度平滑 Hooley 方差与形式因子平台之间的归约。不是偶合数 N 的奇特征两尺度交叉定理，也未提供所需平台的无条件/仅 GRH 证明。
* [Chandee–Lee–Liu–Radziwiłł §1](https://arxiv.org/html/1211.6725v2#S1) 的渐近大筛结论有跨模数平均，不能消除这里的逐 N 要求。不能把相似名称或更低维的一阶/方差统计当作远块范数。

综上：有条件与无条件的几块误差已明确清掉，但尚没有匹配的固定模两尺度交叉定理。不能据此宣布 S/R 已证明或被反证。
