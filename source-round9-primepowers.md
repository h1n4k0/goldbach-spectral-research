# 有界的下一步：全高侧真素数幂可在 S 精度剔除

**实际取消估计，不是截断蛮例。** 在原论文的局部 GRH(N) 下，可把真实奇特征 Gram 的所有高侧真素数幂贡献（包括与任意尺度的混合项）削到任意预定逆对数精度。机制是 $\chi(p^k)=\chi^k(p)$：平方的主要异常只来自很小的二次特征子族，立方在奇族根本没有主特征异常。对角真素数幂可同时削掉。两个**普通素数**腿的跨尺度混合仍未得到 S 上界。

沿用 [Li–Liu](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf) 与 [source-round8.md](source-round8.md) 的 $L=\log N$、$\alpha=1/L$、$W(x)=1+e^{-2(\beta-\alpha)x}$、$x=\log$ 原始整数大小。以下只需正轴，$W\le2$。选 $x_0\ge1$，在每个原 Gram 列 $\Phi_\chi(x)=\sqrt W f_{\chi,\alpha}(x)$ 中，从 $x\ge x_0$ 删除所有 $k\ge2$ 的 $p^k$ 项，低侧一律仍精确。记差列为
$$
r_\chi(x)=-\sqrt{2\pi W(x)}\mathbf1_{x\ge x_0}e^{-(1+\alpha)x}
\sum_{k\ge2}\sum_{p^k\le e^x}\chi(p)^k(\log p)p^{k/2}.
$$
则
$$
\big(\mathbb E_-\|r_\chi\|_2^2\big)^{1/2}
\ll (L+x_0)^2 e^{-x_0/4}
+\sqrt{L\,2^{\omega(N)+1}/\phi(N)}\ e^{-x_0/L}.
$$
这里 $\omega$ 是不同素因子数，平均在同一个模 N 的奇族上做，不跨模数。

## 证明

对任何模 N 的非主特征 ξ，局部 GRH 适用于其本原诱导，故一致地
$$
\sum_{p\le U}\xi(p)\log p\ll\sqrt U\log^2(N(2+U)).
$$
可直接用 [Kandhil–Languasco–Moree, Lemma 2 (27)](https://link.springer.com/article/10.1007/s00208-026-03383-y#Sec2) 的显式公式取高度 $U$、单位纵坐标零点数界求和，再减除 $O(\sqrt U\log(2+U))$ 的真素数幂贡献。这里使用的是实际单特征 GRH 公式，不调用该文额外的两点猜想。乘因子 $p^{k/2}$ 后分部求和，给固定 k 在 $U=e^{x/k}$ 处至多 $O_k(U^{(k+1)/2}(L+x)^2)$。

* $k=2$：当 $\chi^2$ 非主，乘 $e^{-(1+\alpha)x}$ 后得到 $O((L+x)^2e^{-(1/4+\alpha)x})$。当 $\chi^2$ 主，Chebyshev 给 $O(e^{-\alpha x})$。二次特征至多 $2^{\omega(N)+1}$ 个，按 CRT（奇素数幂至多 2 个，2 的幂至多 4 个）；奇族恰有 $\phi(N)/2$ 个。常数 2 吸收到 $\ll$。
* $k=3$：$\chi^3(-1)=-1$，永远非主，相同论证给 $O((L+x)^2e^{-(1/3+\alpha)x})$。
* $k\ge4$：不需 GRH。Chebyshev 及 $p^{k/2}\le e^{x/2}$ 给绝对总和 $\ll e^{x/2}\sum_{4\le k\le x/\log2} e^{x/k}\ll e^{3x/4}$，因为第一项是 $e^{x/4}$，余项至多 $O(x e^{x/5})$. 列上得到 $O(e^{-(1/4+\alpha)x})$。

依次平方积分即可。原列 $\mathbb E_-\|\Phi_\chi\|_2^2\ll L^2$，所以用 $\Phi_\chi-r_\chi$ 形成的 Gram 与原 Gram 的全正轴算子误差至多 $2 O(L)E+E^2$，$E=(\mathbb E_-\|r_\chi\|_2^2)^{1/2}$。这一步同时覆盖所有 mixed near/far 和高高项，不是只对平滑窗。因 $2^{\omega(N)}/\phi(N)=N^{-1+o(1)}$，取 $x_0=L/2$ 给 $O(L^3N^{-1/8})$；任意固定 $A>0$，取 $x_0=(4A+16)\log L$ 则给 $o(L^{-A})$。

## 对角与最终剩余

对角的单个真素数幂 $n=p^k$ 列是 $u_n(x)=\sqrt{2\pi W(x)}e^{-(1+\alpha)x}\sqrt n\log p\,\mathbf1_{x\ge\log n}$。同样把它在 $x\ge x_0$ 切去。对 $n\le X_0=e^{x_0}$，每项的全列与截去部分范数之积 $\ll(\log p)^2 e^{-(1+\alpha)x_0} n^{-\alpha}$；对 $n>X_0$，全迹 $\ll \sum(\log p)^2 n^{-1-2\alpha}$。从 Chebyshev 和各 k 分层，$\sum_{p^k\le X,k\ge2}(\log p)^2\ll \sqrt X\log(2X)$，再分部求和，两个范围各为 $O((1+x_0)e^{-x_0/2})$。真素数幂对角及交叉可在同一尺度剔除，Beta 项保持原样。

因此在 S 的逆对数精度上，可以对整个正轴残差保留小于 $L^{4A+16}$ 原始尺度的所有系数，其余按普通素数输入来处理。本轮并未给剩余普通素数的跨尺度消去。检视的一阶 GRH 界、固定模单尺度方差和跨模数平均均不自动控制由另一个素数窗指定的带符号剩余类方向；其实际混合算子上界仍是缺口。不主张此轮能到 R 精度，也未改动早先报告。
