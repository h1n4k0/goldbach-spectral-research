# 第十七轮：前缀长–长项与外侧确定性模型

**S 和 R 均未证明，也未否证。** 以下两项分别简化有限前缀和双外侧的一个模型项，不能拼成对 $T_N$ 的完整范数估计。

## 有限前缀：只剩真正的长–长项

沿用[第十六轮](ROUND16.md)的短除数权 $\Lambda_D$ 与切口 $D=\lfloor\lceil4bN\rceil^{1/3}\rfloor$，令 $R_D=\Lambda-\Lambda_D$。双短项用整数 CRT 和二元 Euler 积恢复同一精确奇异级数，只需 ζ 的 RH 来控截尾；再与第十六轮的单短项合用，则需要**全局 Dirichlet GRH**。对于每个充分大的偶数 $N$，可将完整物理前缀的真实算子换成有符号双权 $R_D(n)R_D(m)$，**不再扣除模型**，Hilbert–Schmidt 误差为 $O_\epsilon(b^{11/12}N^{-1/12+\epsilon})$。取 $b=N^{3/40}$ 得 $O_\epsilon(N^{-7/480+\epsilon})$。这未估计剩余的长–长关联。[推导](arithmetic-post-r16-mobius-longlong.md)

## 双外侧：对角加 Beta 模型的平稳近似

在物理坐标取对数后，令 $Q_h$ 投影到 $x\ge h$。仅假设原论文的**局部 GRH(N)**，对 $h=\gamma\log N$、固定 $\gamma>0$，$Q_h(D_N+K_N)Q_h$ 可用明确的卷积核与两侧 Hardy 权相乘来近似；Hilbert–Schmidt 误差具有幂衰减。这个确定性模型本身的算子范数仍为 $\asymp_\gamma\log N$，因此不能将它当成小尾丢弃。真正的奇特征协方差 $P_N$ 是否能抵消这一项、以及两条交叉项，仍未控制。[推导](operator-post-r15-stationary-tail.md)

[独立核对](review-round17.md)分别检查两个结论及其不同假设，不是期刊同行评议。
