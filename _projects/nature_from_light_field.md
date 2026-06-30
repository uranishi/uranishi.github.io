---
layout: page
title: Nature from Light Field
description: ライトフィールドからの物体の特性計測 — smoke tomography and transparent surface estimation.
importance: 4
category: research
---

## Nature from Light Field（ライトフィールドからの物体の特性計測）

我々の研究グループではライトフィールドにかかわる様々な性質を利用し、従来手法では形状や空間密度分布の計測が困難であった対象の特性を計測することを目指しています。

### 煙の空間濃度分布推定

Photo-consistent な性質を利用して物体の表面形状を計測する Space Carving [Kutulakos & Seitz, 2000] のように、light field-consistent な性質を利用して煙や霧の空間濃度分布のトモグラフィを試みています。

### 透明物体の受動的形状計測

透明物体の boundary contour 周辺にて観測される Local Photo Consistency という性質を利用し、透明物体の受動的形状計測を試みます。ライトフィールドカメラにより撮影される光線空間は、超短ベースラインであるカメラアレイにより撮影された画像群と等価であるとみなせ、これらの画像群から Local Photo Consistency を有する点を探索し、透明物体の形状を計測します。

**提案手法の特徴:**

- パッシブ計測
- 屈折率未知でも計測可能
- 背景パターン未知でも計測可能

### Related publications

- Yuta Ideguchi, Yuki Uranishi, et al., "Reconstruction of Smoke based on Light Field Consistency", IEEJ Trans. Sensors and Micromachines, 2016.
- Yuta Ideguchi, Yuki Uranishi, et al., "Surface Estimation of Transparent Object based on Local Photo Consistency", IWAIT2016.
