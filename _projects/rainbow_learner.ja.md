---
layout: page
title: Rainbow Learner
description: 構造色ARマーカを用いた光源方向・分光分布のリアルタイム推定
permalink: /ja/projects/rainbow_learner/
importance: 1
category: research
lang: ja
img: assets/img/projects/rainbow_learner/structual_marker.png
---

拡張現実 (Augmented Reality; AR) において実世界にバーチャルな物体を重畳表示する際は，幾何学的・光学的・時間的整合性を維持することが重要です．平面ARマーカを用いれば幾何学的な位置合わせは比較的容易ですが，そのマーカから周囲の照明環境，すなわち**光源方向**と**分光分布**の両方を推定することは依然として難しい課題です．

本プロジェクトでは，コンパクトディスク (CD) と平面ARマーカを組み合わせた構造色マーカ **Rainbow Learner** を提案しています．CD表面の微細構造が入射光を分散させ，視点や照明状態に応じて変化する**構造色パターン**を生じさせる現象を利用します．観測された構造色パターンから，(1) 光源方向と (2) 分光分布をそれぞれ推定する2つの畳み込みニューラルネットワーク (Convolutional Neural Network; CNN) を学習することで，AR描画における**リアルタイムな光学的整合性**を実現します．

### 提案手法の概要

<div class="row justify-content-sm-center">
  <div class="col-sm-10">
    {% include figure.liquid loading="eager" path="assets/img/projects/rainbow_learner/proc.png" title="学習フェーズと推定フェーズの処理概要" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

**学習フェーズ**では，複数の光源環境下で撮影した構造色パターン画像と，対応する照明環境マップ・分光分布のペアを収集します．**推定フェーズ**では，カメラで観測した画像からARマーカを検出して構造色パターン領域を切り出し・マスク処理した後，学習済みモデルに入力することで光源方向と分光分布をリアルタイムに出力します．

### 構造色マーカ

<div class="row justify-content-sm-center">
  <div class="col-sm-8">
    {% include figure.liquid loading="eager" path="assets/img/projects/rainbow_learner/structual_marker.png" title="構造色マーカ（CD + ARマーカ）" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

このマーカは，データの読み書きのために刻まれたCDの同心円状の微細構造と，姿勢推定用のArUco ARマーカを組み合わせたものです．CDの同心円構造により，観測パターンとマーカの面内回転との依存性を概ね排除できます．また，マット塗装によりカメラ画像を飽和させる正反射を抑制しています．

### 着眼点: 構造色パターン

構造色パターンの見え方は，**光源の高度・方位角**と**その分光分布**の両方によって変化します．これは，見た目上は似たような白色に見える光源同士でも同様です．

<div class="row justify-content-sm-center">
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/test_1_1.png" title="高度・方位角の違いによる変化" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/test_1_2.png" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/test_1_3.png" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

CDの微細構造は波長ごとに光を分散させるため，白色LED，色フィルタ付き白色LED，ハロゲンランプを同じ方向から当てた場合でも，観測される構造色パターンは明確に異なります．つまり，このパターンは光源の単なるRGB外観ではなく，その**分光特性**を反映しているということを意味します．

観測条件ごとに事前収集した見本パターンとの照合を必要とする従来のパターンマッチング手法とは異なり，Rainbow Learnerは機械学習によってパターンと照明環境の関係を**モデル化**することで，学習分布内での汎化性能を向上させています．

### ネットワーク構成

<div class="row justify-content-sm-center">
  <div class="col-sm-6">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/network_1.png" title="光源方向推定ネットワーク" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-6">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/network_2.png" title="分光分布推定ネットワーク" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

本手法のモデルは，同じ構造色マーカ画像を入力とする**2つのCNN**から構成されます．

- **方向推定ネットワーク** — 球面調和関数（0〜3次）の係数を表す16次元ベクトルを出力し，主要な光源の高度・方位角を表す照明環境マップを再構成します．
- **分光推定ネットワーク** — 380nmから780nmまで5nm間隔でサンプリングした，81次元の相対分光強度ベクトルを出力します．

両ネットワークとも，Leaky ReLUを活性化関数とする畳み込み層を重ねた後，双曲線正接（tanh）を用いる全結合層で出力します．学習にはAdam Optimizerを使用し，損失関数には平均絶対誤差(MAE)を採用しています．

### データセットと光源

<div class="row justify-content-sm-center align-items-end">
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/white_LED.png" title="白色LED" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/blue_LED.png" title="白色LED + 青色フィルタ" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/red_LED.png" title="白色LED + 赤色フィルタ" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/halogen_lamp.png" title="ハロゲンランプ" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="row justify-content-sm-center align-items-end mt-1">
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/spectrum_white.png" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/spectrum_blue.png" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/spectrum_red.png" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/spectrum_halogen.png" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

データ収集では，白色LEDパネル，同パネルに青・赤の色フィルタを付けたもの，ハロゲンランプの計4種類の光源を用いて分光分布を変化させました．暗室内で全天球カメラが照明環境を，RGBカメラが構造色パターンを同時に撮影し，あらかじめ分光放射計で各光源の正解分光分布を測定しています．この手順により，**6,914組**のペアデータ（マーカ画像・16次元方向係数・81次元分光分布）を収集しました．方向推定ネットワークは10エポック，分光推定ネットワークは70エポック学習しています（TensorFlow 2.7.0 / Python 3.7.8）．

### 結果: 光源方向の推定

<div class="row justify-content-sm-center align-items-center">
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/input.png" title="観測された構造色パターン" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/map_tar.png" title="正解の照明環境マップ" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/map_pred.png" title="推定された照明環境マップ" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

テストデータ1,383枚に対する光源方向の平均絶対誤差（再構成マップの輝度重心により算出）は，垂直方向**3.08°**，水平方向**11.80°**でした．学習データに含まれない屋内・屋外シーンにマーカを設置した場合でも，屋内で **(7.03°, 5.63°)**，屋外で **(1.41°, 9.84°)** と，おおむね妥当な方向推定ができています．ただし学習データの分布から離れるほど精度は低下します．

### 結果: 分光分布の推定

<div class="row justify-content-sm-center align-items-center">
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/input.png" title="観測された構造色パターン" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/estimation_spectrum_tar.png" title="正解の分光分布" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/estimation_spectrum_pred.png" title="推定された分光分布" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

分光推定ネットワークは，同じ構造色パターンから81次元の分光分布曲線全体を推定し，テストデータにおいて波長帯あたりの平均絶対誤差**3.17 × 10⁻²**を達成しています．推定結果を視覚的に比較しやすくするため，CIE 1931 XYZ三刺激値を経由してRGBに変換しました．

<div class="row justify-content-sm-center align-items-center">
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/white.png" title="白色LED（正解）" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/white_error.png" title="白色LED（推定）" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/blue.png" title="青色LED（正解）" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/blue_error.png" title="青色LED（推定）" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="row justify-content-sm-center align-items-center mt-1">
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/red.png" title="赤色LED（正解）" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/red_error.png" title="赤色LED（推定）" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/halogen.png" title="ハロゲンランプ（正解）" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/halogen_error.png" title="ハロゲンランプ（推定）" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

4種類の光源すべてで，推定値と正解値の色はよく一致しています．最も難しいのはハロゲンランプのケースで，その構造色パターンが白色LEDのものと似ることがあるため，分光推定ネットワークが両者を混同する場合があります．未知シーンへの汎化性能は光源方向の結果と同様の傾向を示し，学習データに近い光源で照らされた屋内シーンでは精度良く推定できますが，太陽光が主光源となる**屋外**シーンでは大きな誤差が生じます．これは，太陽光の分光特性が学習に用いた4種類の光源の範囲外にあるためです．ドメイン適応や，学習時に用いる光源の種類を増やすことが今後の課題です．

### 処理時間

マーカ検出・射影変換・切り出し・マスク処理・両ネットワークの推論を含む全処理のパイプラインは，デスクトップPC（Core i7-4771, GTX 780 Ti）で平均**91.5 ms（約10.9 fps）**，ラップトップPC（Core i7-1065G7, dGPUなし）で平均**136.0 ms（約7.4 fps）**を達成し，一般的なPC上でのリアルタイム動作を確認しました．

### 今後の課題

<div class="row justify-content-sm-center align-items-center">
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/fail_1.png" title="飽和によりマーカ未検出" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/fail_2.png" title="飽和によりパターンを正しく観測できない" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/fail_3.png" title="照度不足によりマーカ未検出" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

CDの記録面はレーザ光を効率的に反射するよう設計されているため，光源・マーカ・カメラの位置関係によっては正反射によって画像が飽和し，マーカが検出できなかったり構造色パターンが正しく観測できなかったりする場合があります．また，光源からの照度が不足している場合も同様にマーカ検出に失敗します．いずれも学習データの分布外の状況であり，HDR撮影や別のマーカ素材の検討など，今後のロバスト性向上に向けた課題です．

### 貢献

- 低コストな平面構造色マーカから，**光源方向と分光分布の両方をリアルタイムに推定**する初めての手法
- 幾何学的な位置合わせ（ARマーカ）と光学的推定（構造色 + 専用CNN2系統）を統合
- 一般的なPC上で約10fps動作し，RGB近似ではなく分光分布を考慮したAR描画を実現

### 関連論文

- Yuji Tsukagoshi, Yuki Uranishi, Jason Orlosky, Kiyomi Ito, Haruo Takemura, [Rainbow Learner: Lighting Environment Estimation from a Structural-Color Based AR Marker](/ja/publications/), AIVR 2020.
- Yuki Uranishi, Masataka Imura, Tomohiro Kuroda, [The Rainbow Marker: An AR Marker with Planar Light Probe based on Structural Color Pattern Matching](/ja/publications/), IEEE VR 2016.

### 謝辞

本研究は科学研究費補助金 基盤研究 (C) 21K11962の助成を受けたものです．
