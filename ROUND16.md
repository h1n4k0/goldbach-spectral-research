# 第十六轮：逐模数剥离短 Möbius 除数项

**S 和 R 均未证明，也未否证。** 本轮改用逐模数分解，不是再缩小二倍平方族的例外集。它只估计真实算子的一个中心化分量，未估计全前缀。

在**全局 Dirichlet GRH** 下，对每个充分大的偶数 $N$、$1\le b\le N$，取 $Z=\lceil 4bN\rceil$、$D=\lfloor Z^{1/3}\rfloor$，定义真正的短除数权

$$\Lambda_D(m)=\sum_{d\mid m,\ d\le D}\mu(d)\log(m/d).$$

在已扣除对角的三条有符号和／差线族上，用 $[\Lambda(n)\Lambda_D(m)+\Lambda_D(n)\Lambda(m)]/2$ 取代原双权，保留每条线的精确奇异级数模型。由此得到真实物理前缀 $0<x\le b$ 上的中心化分量 $C_{N,b,D}$。[完整推导](arithmetic-post-r15-mobius-short.md)给出

$$\|C_{N,b,D}\|_{\mathrm{HS}}\ll_\epsilon b^{11/12}N^{-1/12+\epsilon}.$$

特别地，$b=N^{3/40}$ 时误差为 $O_\epsilon(N^{-7/480+\epsilon})$，小于[第十五轮](ROUND15.md)示例阈值 $N^{-1/400}$，但不够小到 Hypothesis R 所要求的尺度。证明使用每条线的短模数 GRH 素数定理，以及 $\sum_{(d,h)=1}\mu(d)/(\varphi(d)d^s)$ 在 $s=0$ 的导数恰为 $\mathfrak S(h)$；再将硬矩形误差传到包含零端的真实累计核。[独立核对](review-post-r15-mobius-short.md)不是期刊同行评议。

从原前缀算子减去该分量后，精确剩下带符号的长除数 $d>D$ 的 Möbius–素数移位和。该和仍未得到逐模数上界；前缀之外的交叉项也不在本轮范围内。
