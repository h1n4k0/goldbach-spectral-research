# 第十三轮：主弧改进与单列的文献推论

**没有证明或否证 S、R。** 不需额外次弧定理的主结果处理倍平方族 $N=2r^2$、$R<r\le2R$ 在固定窗口 $J=[\log(1/2),\log(9/16)]$ 上的真实补偿压缩。设 $X=8R^2$、$L=\log X$；辅助主弧模数需要**全局 Dirichlet GRH**，原算子识别使用局部 GRH(N)。

### 主结果：只使用常规 Vaughan 次弧估计

[定理与推导](spectral-post-r12-major-plancherel.md)先对辅助模数的所有分子用有限 Parseval，再对主弧的连续高度变量用 Plancherel，改善逐模数主弧误差；[第十二轮](ROUND12.md)的自适应区间分解不变。对任意固定 $\eta>0$、$\epsilon>0$，在 $X^{-1/4+\eta}\le\tau\le1$ 时，
$$
\#\{r:\|\mathbf1_JT_{2r^2,\log}\mathbf1_J\|_{HS}>\tau\}
\ll_{\eta,\epsilon}X^\epsilon
      \bigl(X^{3/10}\tau^{-2}+X^{1/4}\tau^{-5/2}\bigr).
$$
同一块的 Hilbert–Schmidt 范数平方平均改善至 $O_\epsilon(X^{-1/5+\epsilon})$。因此每个固定 $a<1/10$ 的阈值 $X^{-a}$ 仍有幂次节省的例外比例。

### 单列推论：额外调用一篇预印本的第四矩定理

若采用 [Huixi Li–Zhixin Liu 的 arXiv:2610.26756v1，Theorem 1](https://arxiv.org/html/2610.26756v1#S1) 给定的固定光滑权次弧四次矩，同一固定块的例外数进一步是 $O_{\epsilon,\delta}(X^{1/4+\epsilon}\tau^{-2})$，但只在 $\tau\ge X^{-1/2+\kappa_0+\delta}$ 的注明范围内，$\kappa_0\in(4/9,9/20)$ 由该定理给出。这是额外输入，不参与上一节的均方证明。我们核对了固定权平台、原次弧范围和向真实补偿块的传递，未重证外部定理。

同样引用该预印本，[增长前缀推论](source-post-r11-prefix-transfer.md)适用于 $N=2F(r)$ 的固定正首项二次多项式族。取每条和／差线中较大的素数作固定权因子，按二进尺度把它放在原定理的权平台内。若 $b^2\tau^{-2}\le X^{1/40}$，完整物理前缀 $0<x\le b$ 的例外数是 $O_{F,\epsilon}(\tau^{-4}b^{17/4}X^{1/4+\epsilon})$。例如 $b=X^{1/100}$、$\tau=X^{-1/400}$ 给 $O_{F,\epsilon}(X^{121/400+\epsilon})$。这里同样没有重证外部四次矩定理；[固定块的平滑夹逼版本](source-post-r11-primary-transfer.md)仅作传递的交叉检验，不重复计为另一个结论。

[独立复核](review-round13.md)区分了两种输入及其阈值范围。以上不控制前缀外的交叉作用、剩下的例外或真实算子的最大谱值，也不主张改进一般哥德巴赫表示的纪录。
