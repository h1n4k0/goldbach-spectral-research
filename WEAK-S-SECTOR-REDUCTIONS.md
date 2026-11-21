# 弱 S 的两项局部约化：双外侧与中央 Type I

[研究状态](POST-R-STATUS.md) · [前缀与首别名](ROUND25.md) · [中央正性的平滑判据](spectral-signed-rectangle-smooth-bridge.md)

两项约化针对不同对象，不能合并成原算子的全局范数界。

- [双外侧的细方向可忽略](weak-s-exterior-fine.md)。对满足局部 Dirichlet GRH 的每个大偶模数，物理两坐标均在 $Y$ 以上时，只要其中一侧与指定的加权单元均值方向正交，真实压缩的 Hilbert–Schmidt 范数便是 $o((\log N)^{-K})$。$Y$ 可从 $\exp((K+3)(\log\log N)^2/\log\log\log N)$ 开始；所有更远的区间一起估计，没有上端截断。证明结合实际奇特征协方差及[平稳对角与 Beta 模型](operator-post-r15-stationary-tail.md)的统一余项。两侧都取均值方向的块，以及与中央区的交叉，没有得到上界。
- [真实中央增量的两个 Vaughan Type I 项可移除](spectral-vaughan-central-type-i.md)。用固定中央上半区 $N/2<n\le y\le9N/16$。在任意固定幂区间 $N^{\theta_0}\le t\le N^{\theta_1}$、$UV\le N^{\theta_0-\varepsilon}$ 的条件下，两个 Type I 项分别为 $O_A(N(\log N)^{-A})$，不需 GRH，也不跨模数平均。保留了原始严格边界 $k>t$、单位条件和符号；留下的是明确的 Type II 和式而不是已证抵消。它不是从零开始的前缀估计，也没有解决中央正性的带符号判据。

两项结果都不证明弱 S 或哥德巴赫猜想，也不改变[精确 R 的条件性反例](https://hexagonmath.org/2611.00788v1)。
