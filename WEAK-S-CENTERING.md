# 弱 S 的两项中心化：双外侧零点与中央双素数腿

[研究状态](POST-R-STATUS.md) · [双外侧细方向与中央 Type I](WEAK-S-SECTOR-REDUCTIONS.md) · [中央 Type II](CENTRAL-TYPE-II.md)

沿用[李–刘 Hardy 算子](https://mrc.sdu.edu.cn/english/info/1018/1514.htm)。下述两项分别辨明一个可以抵消的确切分量与仍待估计的两侧相关；它们不是同一个算子上的可相加误差。

- **[双外侧：同一零点副本配自身的对角](r31-operator-zero-diagonal.md)。** 写 $L=\log N$，$x,z$ 为无量纲物理坐标的对数。对满足局部 Dirichlet GRH 的偶模数，在 $x,z\ge (K+3)(\log L)^2/\log\log L$、$|x-z|\le 2L-(2K+6)\log L$ 内，实际零点 Gram 的同副本对角抵消 $D_N+K_N$，误差在 Hilbert–Schmidt 范数中为 $o(L^{-K})$。可把该带内真实余项替换为多对数高度截断的**不同副本**项。重零点的不同副本仍在其中；该相关的大小及带外项都没有得到控制。
- **[中央：两条单侧波动项可消去](r31-source-double-giant-one-leg-centering.md)。** 在全局 Dirichlet GRH 下，对固定 $0<\rho<1/2$、$0<\kappa\le1/2000$，选实际 $qp+se=N$ 的中央半素数配对，短素数因子 $q,s$ 在 $[N^\kappa,N^{1/2-\kappa}]$，长素数因子 $p,e$ 位于原和别名。用明确的截断局部密度中心化后，两条单侧误差合计 $O_{\rho,\kappa}(N^{1-\kappa/4})$。真实选区减去局部比较项，等于两条中心化素性权重的同目标相关，外加归一化 Hilbert–Schmidt 误差 $O_{\rho,\kappa}(N^{-\kappa/4}+\mathfrak S(N)/(L\log L))$。没有估计该双侧相关，也没有把这项推广到截断端点或其余除数区。

因此，现有约化不能推出全块消失、全算子弱 S 或哥德巴赫渐近式。[原 R 的条件性反例](https://hexagonmath.org/2611.00788v1)的状态不变。
