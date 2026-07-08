# Researchmap vs publications.json 差分レポート

生成日時: 2026-07-07 09:08

## 概要

| 項目                          | 件数 |
| ----------------------------- | ---- |
| researchmap（業績系レコード） | 361  |
| publications.json             | 315  |
| マッチ（タイトル/DOI）        | 242  |
| マッチかつフィールド差分あり  | 127  |
| researchmap のみ              | 119  |
| publications.json のみ        | 73   |

## マッピング方針

- `published_papers.scientific_journal` → Journal Papers
- `published_papers.international_conference_proceedings` → International Conference Proceedings
- `published_papers.research_society` → Domestic Conference Proceedings
- `misc.summary_*` → Domestic / International Conference Proceedings
- `misc`（misc_type なし）→ Misc.
- `books_etc` → Books
- `presentations`（invited 等）→ Invited Talks and Tutorials
- マッチングキー: DOI 優先、なければ正規化タイトル

## researchmap のみ（119 件）

### Books (1)

- **OpenCV 3 プログラミングブック : OpenCV 3.0対応** (`rm:books_etc:43160545`)
  - category (guess): Books
  - authors: 藤本, 雄一郎 (工学), 青砥, 隆仁, 浦西, 友樹, 大倉, 史生, 小枝, 正直, 中島, 悠太, 山本, 豪志朗
  - date: 2015-09
  - publication_info: マイナビ
  - doi: —

### Domestic Conference Proceedings (7)

- **シミュレーションと自己符号化器を用いた光源変化に頑健なカメラ位置姿勢推定** (`rm:published_papers:21725784`)
  - category (guess): Domestic Conference Proceedings
  - authors: 正満 創太, 間下 以大, Photchara Ratsamee, 浦西 友樹, 清川 清, 竹村 治雄
  - date: 2017-08
  - publication_info: —
  - doi: —

- **Design of Archetype-based Clinical Concept Models: Towards Interoperable Antenatal Care EHR Systems** (`rm:misc:25165659`)
  - category (guess): Domestic Conference Proceedings
  - authors: Samar El Helou, Naoto Kume, Yuki Uranishi, Shinji Kobayashi, Eiji Kondo, Kazuya Okamoto, Hiroshi Tamura, Tomohiro Kuroda
  - date: 2015-11
  - publication_info: Proceedings of Joint Conference on Medical Informatics
  - doi: —

- **視覚障がい者のための誘導音を用いた線図形トレーシングシステム** (`rm:misc:18561731`)
  - category (guess): Domestic Conference Proceedings
  - authors: 瀧澤洸, 浦西友樹, 吉元俊輔, 井村誠孝, 大城理
  - date: 2014-05
  - publication_info: 第58回システム制御情報学会研究発表講演会 講演論文集
  - doi: —

- **リフォーカス画像におけるボケを用いた煙霧の空間濃度分布推定** (`rm:misc:18561708`)
  - category (guess): Domestic Conference Proceedings
  - authors: 井手口裕太, 浦西友樹, 黒田嘉宏, 井村誠孝, 大城理
  - date: 2014-01
  - publication_info: 電子情報通信学会 技術研究報告
  - doi: —

- **手の筋骨格モデルを導入した投球シミュレーション** (`rm:misc:18561739`)
  - category (guess): Domestic Conference Proceedings
  - authors: 横畑亮輔, 井村誠孝, 黒田嘉宏, 浦西友樹, 大城理
  - date: 2014
  - publication_info: 生体医工学シンポジウム 講演予稿集
  - doi: 10.11239/jsmbe.52.1

- **スマートフォン利用による視覚障がい者のための衣類の色および模様認識システム** (`rm:misc:18561738`)
  - category (guess): Domestic Conference Proceedings
  - authors: 三宅正夫, 眞鍋佳嗣, 浦西友樹, 井村誠孝, 黒田嘉宏, 大城理
  - date: 2013-09
  - publication_info: 生体医工学シンポジウム 講演予稿集
  - doi: 10.11239/jsmbe.51.342

- **ウェアラブルコンピュータにおけるリング型デバイス“Ubi-WA”の提案** (`rm:misc:18561766`)
  - category (guess): Domestic Conference Proceedings
  - authors: 藤木健史, 浦西友樹, 佐々木博史, 眞鍋佳嗣, 千原國宏
  - date: 2009-05
  - publication_info: 第53回 システム制御情報学会研究発表講演会 講演論文集
  - doi: 10.11509/sci.sci09.0.61.0

### International Conference Proceedings (16)

- **A Non-contact Translational and Rotational Force Feedback Device using Rotational Jet Propellers** (`rm:published_papers:47226653`)
  - category (guess): International Conference Proceedings
  - authors: Nishimura Ryo, Photchara Ratsamee, Yuki Uranishi, Haruo Takemura
  - date: 2024-03
  - publication_info: 2024 SICE International Symposium on Control Systems (SICE ISCS)
  - doi: 10.23919/siceiscs60954.2024.10505747

- **SmartVP: Viewpoint Optimization Based on Individual Preference for Watching 3D Boxing Punch Videos** (`rm:published_papers:43468934`)
  - category (guess): International Conference Proceedings
  - authors: Tao Tao, Photchara Ratsamee, Chang Liu, Yuki Uranishi, Haruo Takemura
  - date: 2023-03
  - publication_info: Proceedings of the 2023 5th International Conference on Image, Video and Signal Processing
  - doi: 10.1145/3591156.3591171

- **Panoptic-aware Image-to-Image Translation** (`rm:published_papers:43352268`)
  - category (guess): International Conference Proceedings
  - authors: Liyun Zhang, Photchara Ratsamee, Bowen Wang, Zhaojie Luo, Yuki Uranishi, Manabu Higashida, Haruo Takemura
  - date: 2023-01
  - publication_info: IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
  - doi: 10.1109/wacv56688.2023.00034

- **Exploring Three-Dimensional Locomotion Techniques in Virtual Reality** (`rm:published_papers:43468937`)
  - category (guess): International Conference Proceedings
  - authors: Donghae Lim, Shizuka Shirai, Jason Orlosky, Photchara Ratsamee, Yuki Uranishi, Haruo Takemura
  - date: 2022-10
  - publication_info: 2022 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct)
  - doi: 10.1109/ismar-adjunct57072.2022.00105

- **FrictionHaptics : Encountered-type haptic device fortangential friction emulation** (`rm:published_papers:47090286`)
  - category (guess): International Conference Proceedings
  - authors: Ryo Meguro, Photchara Ratsamee, Tomohiro Mashita, Yuki Uranishi, Haruo Takemura
  - date: 2019-10
  - publication_info: Adjunct Proceedings of the 2019 IEEE International Symposium on Mixed and Augmented Reality, ISMAR-Adjunct 2019
  - doi: 10.1109/ismar-adjunct.2019.000-6

- **3D Image Reconstruction from Multi-focus Microscopic Images.** (`rm:published_papers:26333096`)
  - category (guess): International Conference Proceedings
  - authors: Takahiro Yamaguchi, Hajime Nagahara, Ken'ichi Morooka, Yuta Nakashima, Yuki Uranishi, Shoko Miyauchi, Ryo Kurazume
  - date: 2019
  - publication_info: Image and Video Technology - PSIVT 2019 International Workshops
  - doi: 10.1007/978-3-030-39770-8_6

- **The 30th IEEE conference on computer vision and pattern recognition (CVPR 2017) report** (`rm:published_papers:47095850`)
  - category (guess): International Conference Proceedings
  - authors: Yuki Uranishi, Yuta Ideguchi
  - date: 2018
  - publication_info: Kyokai Joho Imeji Zasshi/Journal of the Institute of Image Information and Television Engineers
  - doi: 10.3169/itej.72.69

- **Graph databases for openEHR repositories** (`rm:misc:25165760`)
  - category (guess): International Conference Proceedings
  - authors: Samar El Helou, Naoto Kume, Shinji Kobayashi, Eiji Kondo, Yuki Uranishi, Kazuya Okamoto, Hiroshi Tamura, Tomohiro Kuroda
  - date: 2016-08
  - publication_info: European Journal of Epidemiology
  - doi: —

- **A Hybrid Flying and Walking Robot For Steel Bridge Inspection** (`rm:published_papers:27808265`)
  - category (guess): International Conference Proceedings
  - authors: Photchara Ratsamee, Pakpoom Kriengkomol, Tatsuo Arai, Kazuto Kamiyama, Yasushi Mae, Kiyoshi Kiyokawa, Tomohiro Mashita, Yuki Uranishi, Haruo Takemura
  - date: 2016
  - publication_info: 2016 IEEE INTERNATIONAL SYMPOSIUM ON SAFETY, SECURITY, AND RESCUE ROBOTICS (SSRR)
  - doi: —

- **Exploring Graph Databases with openEHR in Antenatal Care Settings** (`rm:misc:25165656`)
  - category (guess): International Conference Proceedings
  - authors: Samar El Helou, Naoto Kume, Shinji Kobayashi, Eiji Kondo, Yuki Uranishi, Kazuya Okamoto, Hiroshi Tamura, Tomohiro Kuroda
  - date: 2015-12
  - publication_info: Proceedings of Symposium on Big Data Analytics in Science and Engineering
  - doi: —

- **Large Deformation with Haptic Interaction by Stepwise Rotation Update of Finite Element Model** (`rm:misc:18561674`)
  - category (guess): International Conference Proceedings
  - authors: Yoshihiro Kuroda, Yuki Uranishi, Masataka Imura, Osamu Oshiro, Haruo Takemura
  - date: 2014-06
  - publication_info: Proceedings of International Congress, Exhibition Computer Assisted Radiology and Surgery (CARS2014)
  - doi: —

- **Pitching Simulation with Musculoskeletal Model of Hand** (`rm:published_papers:21725757`)
  - category (guess): International Conference Proceedings
  - authors: Ryosuke Yokohata, Masataka Imura, Yuki Uranishi, Shunsuke Yoshimoto, Yoshihiro Kuroda, Osamu Oshiro
  - date: 2014-05
  - publication_info: Proceedins of Digital Human Modeling Symposium
  - doi: —

- **Tactile Modulator: Roughness Modulation Using Electrotactile Augmentation** (`rm:published_papers:26275041`)
  - category (guess): International Conference Proceedings
  - authors: Shunsuke Yoshimoto, Yoshihiro Kuroda, Yuki Uranishi, Masataka Imura, Osamu Oshiro
  - date: 2014
  - publication_info: HAPTICS: NEUROSCIENCE, DEVICES, MODELING, AND APPLICATIONS, PT II
  - doi: —

- **HAPTIC GLOVE USING COMPRESSION-INDUCED FRICTION TORQUE** (`rm:published_papers:27535029`)
  - category (guess): International Conference Proceedings
  - authors: Yoshihiro Kuroda, Yu Shigeta, Masataka Imura, Yuki Uranishi, Osamu Oshiro
  - date: 2013
  - publication_info: ASME 2013 DYNAMIC SYSTEMS AND CONTROL CONFERENCE, VOL 2
  - doi: 10.1115/dscc2013-3866

- **Overlayable, Rotation-free Transmissive Circular Color Marker for Augmented Reality** (`rm:misc:18561684`)
  - category (guess): International Conference Proceedings
  - authors: Asahi Suzuki, Yoshitsugu Manabe, Noriko Yata, Yuki Uranishi
  - date: 2012-05
  - publication_info: IS&T's 6th European Conference on Colour in Graphics
  - doi: —

- **Whole shape measurement system using a single camera and a cylindrical mirror** (`rm:misc:18561694`)
  - category (guess): International Conference Proceedings
  - authors: Yuuki Uranishi, Mika Naganawa, Yoshihiro Yasumuro, Masataka Imura, Yoshitsugu Manabe, Kunihiro Chihara
  - date: 2006
  - publication_info: 18TH INTERNATIONAL CONFERENCE ON PATTERN RECOGNITION, VOL 4, PROCEEDINGS
  - doi: —

### Invited Talks and Tutorials (1)

- **タブレットPCと伸縮および振動可能な スタイラスを用いた力触覚提示** (`rm:presentations:16639258`)
  - category (guess): Invited Talks and Tutorials
  - authors: 長坂信吾, 浦西友樹, 吉元俊輔, 井村誠孝, 大城理
  - date: 2014-11
  - publication_info: 電気関係学会関西支部連合大会 予稿集
  - doi: —

### Journal Papers (18)

- **3DGesPolicy: Phoneme-Aware Holistic Co-Speech Gesture Generation Based on Action Control.** (`rm:published_papers:54004072`)
  - category (guess): Journal Papers
  - authors: Xuanmeng Sha, Liyun Zhang, Tomohiro Mashita, Naoya Chiba, Yuki Uranishi
  - date: 2026-01
  - publication_info: CoRR
  - doi: 10.48550/arxiv.2601.18451

- **3DFacePolicy: Speech-Driven 3D Facial Animation with Diffusion Policy.** (`rm:published_papers:48414184`)
  - category (guess): Journal Papers
  - authors: Xuanmeng Sha, Liyun Zhang, Tomohiro Mashita, Yuki Uranishi
  - date: 2024
  - publication_info: CoRR
  - doi: 10.48550/arxiv.2409.10848

- **Panoptic-based Object Style-Align for Image-to-Image Translation.** (`rm:published_papers:47318510`)
  - category (guess): Journal Papers
  - authors: Liyun Zhang, Photchara Ratsamee, Bowen Wang, Manabu Higashida, Yuki Uranishi, Haruo Takemura
  - date: 2021
  - publication_info: CoRR
  - doi: —

- **Reconstruction of Smoke based on Light Field Consistency** (`rm:published_papers:21725773`)
  - category (guess): Journal Papers
  - authors: Yuta Ideguchi, Yuki Uranishi, Shunsuke Yoshimoto, Yoshihiro Kuroda, Masataka Imura, Osamu Oshiro
  - date: 2016-12
  - publication_info: IEEJ Transactions on Sensors and Micromachines
  - doi: —

- **ライトフィールドからの煙の空間濃度分布推定** (`rm:published_papers:21725766`)
  - category (guess): Journal Papers
  - authors: 井手口裕太, 浦西友樹, 吉元俊輔, 黒田嘉宏, 井村誠孝, 大城 理
  - date: 2016-07
  - publication_info: 映像情報メディア学会誌
  - doi: 10.3169/itej.70.j146

- **Support system for clothes selection based on color information for visually impaired persons** (`rm:published_papers:29657893`)
  - category (guess): Journal Papers
  - authors: Masao Miyake, Yoshitsugu Manabe, Yuki Uranishi, Shunsuke Yoshimoto, Masataka Imura, Yoshihiro Kuroda, Osamu Oshiro
  - date: 2016-02
  - publication_info: Transactions of Japanese Society for Medical and Biological Engineering
  - doi: 10.11239/jsmbe.53.255

- **Reconstruction of smoke based on light field consistency** (`rm:published_papers:21725774`)
  - category (guess): Journal Papers
  - authors: Yuta Ideguchi, Yuki Uranishi, Shunsuke Yoshimoto, Yoshihiro Kuroda, Masataka Imura, Osamu Oshiro
  - date: 2016
  - publication_info: IEEJ Transactions on Sensors and Micromachines
  - doi: 10.1541/ieejsmas.136.522

- **Simulation of air flow bronchus caused by lung deformation** (`rm:published_papers:29638722`)
  - category (guess): Journal Papers
  - authors: Akihiro Wada, Masataka Imura, Yuki Uranishi, Shunsuke Yoshimoto, Yoshihiro Kuroda, Osamu Oshiro
  - date: 2014-08
  - publication_info: Transactions of Japanese Society for Medical and Biological Engineering
  - doi: 10.11239/jsmbe.52.o-436

- **Estimation of fingertip contact force direction based on change in nail color distribution** (`rm:published_papers:29638432`)
  - category (guess): Journal Papers
  - authors: Hironobu Mameno, Masataka Imura, Yuki Uranishi, Shunsuke Yoshimoto, Osamu Oshiro
  - date: 2014-08
  - publication_info: Transactions of Japanese Society for Medical and Biological Engineering
  - doi: 10.11239/jsmbe.52.o-155

- **Estimation of amount of swallowed water by analysis of swallowing sounds** (`rm:published_papers:29638368`)
  - category (guess): Journal Papers
  - authors: Hiroki Nakafuji, Masataka Imura, Yuki Uranishi, Shunsuke Yoshimoto, Osamu Oshiro
  - date: 2014-08
  - publication_info: Transactions of Japanese Society for Medical and Biological Engineering
  - doi: 10.11239/jsmbe.52.o-11

- **Pedestrian - traffic Logging Unit with Tailgating Detection using Range Image Sensor** (`rm:published_papers:21725754`)
  - category (guess): Journal Papers
  - authors: Yuki Uranishi, Yasufumi Moriie, Yoshitsugu Manabe, Osamu Oshiro, Kunihiro Chihara
  - date: 2013-09
  - publication_info: ACEEE International Journal on Information Technology
  - doi: —

- **Presentation system of color and pattern on clothes for visually impaired person using smartphone** (`rm:published_papers:37422663`)
  - category (guess): Journal Papers
  - authors: Masao Miyake, Yoshitsugu Manabe, Yuki Uranishi, Masataka Imura, Yoshihiro Kuroda, Osamu Oshiro
  - date: 2013
  - publication_info: Transactions of Japanese Society for Medical and Biological Engineering
  - doi: —

- **立体マーカを用いた拡張現実感環境における仮想物体の床平面に対する映り込みの実時間表現** (`rm:published_papers:13000998`)
  - category (guess): Journal Papers
  - authors: 浦西友樹, 眞鍋佳嗣, 千原國宏
  - date: 2012-12
  - publication_info: 日本バーチャルリアリティ学会論文誌
  - doi: 10.18974/tvrsj.17.4_477

- **視覚障がい者支援のための衣類の色および模様提示システム** (`rm:published_papers:13000999`)
  - category (guess): Journal Papers
  - authors: 三宅正夫, 眞鍋佳嗣, 浦西友樹, 池田聖, 千原國宏
  - date: 2012-03
  - publication_info: 日本色彩学会誌
  - doi: —

- **平城京ウォークスルー -多様な環境に対応したバーチャル空間散策システム-** (`rm:published_papers:13001002`)
  - category (guess): Journal Papers
  - authors: 井村誠孝, 浦西友樹, 池田聖, 眞鍋佳嗣, 大城理, 千原國宏
  - date: 2011-12
  - publication_info: 芸術科学会論文誌
  - doi: —

- **視覚障がい者のための化粧支援風圧ディスプレイ** (`rm:published_papers:13001004`)
  - category (guess): Journal Papers
  - authors: 木村有里, 眞鍋佳嗣, 浦西友樹, 千原國宏
  - date: 2010-12
  - publication_info: 映像情報メディア学会誌
  - doi: 10.3169/itej.64.1884

- **重ね合わせ可能な半透明二次元カラーマーカ** (`rm:published_papers:13001007`)
  - category (guess): Journal Papers
  - authors: 浦西友樹, 今村昂司, 眞鍋佳嗣, 佐々木博史, 千原國宏
  - date: 2010-06
  - publication_info: 日本バーチャルリアリティ学会論文誌
  - doi: 10.18974/tvrsj.15.2_125

- **円筒鏡を用いた三次元形状計測システム** (`rm:published_papers:13001010`)
  - category (guess): Journal Papers
  - authors: 浦西友樹, 長縄美香, 安室喜弘, 井村誠孝, 眞鍋佳嗣, 千原國宏
  - date: 2006-07
  - publication_info: 情報処理学会論文誌: コンピュータビジョンとイメージメディア
  - doi: —

### Misc. (40)

- **ニュージーランドと日本の高等学校における情報教育の比較のための予備調査-授業見学と教員インタビューを通じて-** (`rm:misc:52605474`)
  - category (guess): Misc.
  - authors: 北村祐稀, HENDERSON Tracy, 白井詩沙香, 長瀧寛之, 辰己丈夫, BELL Tim, 浦西友樹
  - date: 2024
  - publication_info: 情報処理学会研究報告(Web)
  - doi: —

- **ボルダリングにおける登攀上達を支援する投影情報の検討** (`rm:misc:37809284`)
  - category (guess): Misc.
  - authors: 浜本多聞, 浦西友樹, 浦西友樹, RATSAMEE Photchara, RATSAMEE Photchara, 東田学, 東田学, 劉暢, 山本豪志朗
  - date: 2022
  - publication_info: 情報処理学会研究報告(Web)
  - doi: —

- **ホールド形状を考慮したボルダリング課題の難度推定** (`rm:misc:37809281`)
  - category (guess): Misc.
  - authors: 大西和歩, 浦西友樹, 浦西友樹, RATSAMEE Photchara, RATSAMEE Photchara, 東田学, 東田学, 劉暢, 山本豪志朗
  - date: 2022
  - publication_info: 情報処理学会研究報告(Web)
  - doi: —

- **視線情報に基づくVR空間でのマンガ教材読書時の主観的難易度推定—Subjective Difficulty Estimation of VR-based Educational Comics Using Gaze Features—第185回 ヒューマンインタフェース学会研究会 人工現実感,エンタテインメント,メディアエクスペリエンスおよび一般** (`rm:misc:40806522`)
  - category (guess): Misc.
  - authors: 坂本 賢哉, 白井 詩沙香, 武村 紀子, Orlosky Jason, 長瀧 寛之, 上田 真由美, 浦西 友樹, 竹村 治雄
  - date: 2021
  - publication_info: ヒューマンインタフェース学会研究報告集
  - doi: —

- **多重焦点顕微鏡画像列からの細胞の3次元形状復元 (メディアエクスペリエンス・バーチャル環境基礎)** (`rm:misc:26333246`)
  - category (guess): Misc.
  - authors: 山口 貴大, 長原 一, 諸岡 健一, 中島 悠太, 浦西 友樹, 倉爪 亮, 大野 英治
  - date: 2019-01
  - publication_info: 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報
  - doi: —

- **私の研究開発ツール―第101回―コンピュータビジョンライブラリーOpenCV3.0** (`rm:misc:19346920`)
  - category (guess): Misc.
  - authors: 浦西友樹
  - date: 2018-09
  - publication_info: 映像情報メディア学会誌
  - doi: —

- **カメラ画像の大域的な輝度情報に基づく弾性体の変形推定 (医用画像)** (`rm:misc:37282813`)
  - category (guess): Misc.
  - authors: 齋藤 陽, 中尾 恵, 浦西 友樹, 松田 哲也
  - date: 2017-01
  - publication_info: 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報
  - doi: —

- **外来病棟における位置情報とオーダ情報を用いた患者待ち時間の分析—Analysis of waiting time of patients using position tracking data and clinical order data in an outpatient ward** (`rm:misc:39617912`)
  - category (guess): Misc.
  - authors: 福士 雄太, 岡本 和也, 岩尾 友秀, 浦西 友樹, 田村 寛, 齊藤 永, 加藤 源太, 黒田 知宏
  - date: 2016-05
  - publication_info: システム制御情報学会研究発表講演会講演論文集
  - doi: —

- **スーパーサイエンスハイスクール生徒研究発表会に参加して(学会活動)** (`rm:misc:37485861`)
  - category (guess): Misc.
  - authors: 浦西 友樹
  - date: 2016-03
  - publication_info: システム/制御/情報 : システム制御情報学会誌
  - doi: —

- **DT-1-1 OpenCV 3.0 : コンピュータビジョンを簡単化するライブラリ(DT-1.「パターン認識・メディア理解」必須ソフトウエアライブラリ 手とり足とりガイド,チュートリアルセッション,ソサイエティ企画)** (`rm:misc:37412688`)
  - category (guess): Misc.
  - authors: 浦西 友樹
  - date: 2016-03
  - publication_info: 電子情報通信学会総合大会講演論文集
  - doi: —

- **An attempt to connect medical instruments to hospital information system** (`rm:misc:25757203`)
  - category (guess): Misc.
  - authors: ESASHI Misa, NAKANO Tomohiro, IWAO Tomohide, URANISHI Yuki, URANISHI Yuki, OKAMAOTO Kazuya, OKAMAOTO Kazuya, KATO Genta, SAITO Hisashi, TAMURA Hiroshi, TAMURA Hiroshi, NOMA Haruo, KURODA Tomohiro, KURODA Tomohiro
  - date: 2016-01
  - publication_info: 日本生体医工学会大会プログラム・論文集(CD-ROM)
  - doi: —

- **Spatial Density Estimation of Smoke based on Light Field Consistency** (`rm:misc:37300432`)
  - category (guess): Misc.
  - authors: Ideguchi Yuta, Yoshimoto Shunsuke, Kuroda Yoshihiro, Oshiro Osamu, Uranishi Yuki, Imura Masataka
  - date: 2015-10
  - publication_info: 「センサ・マイクロマシンと応用システム」シンポジウム論文集 電気学会センサ・マイクロマシン部門 [編]
  - doi: —

- **視認性の高い投影のための色と形状に基づくシーンの評価 (マルチメディア・仮想環境基礎)** (`rm:misc:37412223`)
  - category (guess): Misc.
  - authors: 團原 佑壮, 浦西 友樹, 吉元 俊輔, 井村 誠孝, 大城 理
  - date: 2015-01
  - publication_info: 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報
  - doi: —

- **平行投影近似のためのライトフィードカメラへの補助レンズの追加** (`rm:misc:37658227`)
  - category (guess): Misc.
  - authors: 井手口裕太, 吉元俊輔, 井村誠孝, 大城理, 浦西友樹
  - date: 2015
  - publication_info: システム制御情報学会研究発表講演会講演論文集(CD-ROM)
  - doi: —

- **Deformation Estimation of Elastic Bodies Using Multiple Silhouette Images for Endoscopic Image Augmentation** (`rm:misc:27643079`)
  - category (guess): Misc.
  - authors: Akira Saito, Megumi Nakao, Yuki Uranishi, Tetsuya Matsuda
  - date: 2015
  - publication_info: 2015 IEEE International Symposium on Mixed and Augmented Reality
  - doi: 10.1109/ismar.2015.49

- **光計測を用いた爪装着型指先接触力センサ (MEとバイオサイバネティックス)** (`rm:misc:35359497`)
  - category (guess): Misc.
  - authors: 豆野 裕信, 井村 誠孝, 吉元 俊輔, 浦西 友樹, 大城 理
  - date: 2014-10
  - publication_info: 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報
  - doi: —

- **コンピュータビジョン-アルゴリズムと応用-, Richard Szeliski著, 玉木徹ほか訳, 出版社共立出版, 発行2013年3月, 全ページ836頁, 価格16,000円, ISBN978-4-320-12328-1** (`rm:misc:35397600`)
  - category (guess): Misc.
  - authors: 浦西 友樹
  - date: 2014-10
  - publication_info: システム/制御/情報 : システム制御情報学会誌
  - doi: —

- **リフォーカス画像におけるボケを用いた煙霧の空間濃度分布推定 (パターン認識・メディア理解)** (`rm:misc:19346900`)
  - category (guess): Misc.
  - authors: 井手口 裕太, 浦西 友樹, 黒田 嘉宏, 井村 誠孝, 大城 理
  - date: 2014-01
  - publication_info: 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報
  - doi: —

- **立体音響のための骨伝導の振動伝播解析 (MEとバイオサイバネティックス)** (`rm:misc:19346901`)
  - category (guess): Misc.
  - authors: 松崎 成敏, 黒田 嘉宏, 浦西 友樹, 井村 誠孝, 大城 理
  - date: 2013-10
  - publication_info: 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報
  - doi: —

- **力覚提示指向の大変形有限要素法** (`rm:misc:19346902`)
  - category (guess): Misc.
  - authors: 黒田 嘉宏, 浦西 友樹, 井村 誠孝
  - date: 2013-09
  - publication_info: 日本バーチャルリアリティ学会大会論文集 Proceedings of the Virtual Reality Society of Japan, Annual Conference
  - doi: —

- **バーチャル空間に挿入可能な三次元スケッチペン (マルチメディア・仮想環境基礎)** (`rm:misc:19346904`)
  - category (guess): Misc.
  - authors: 長坂 信吾, 浦西 友樹, 黒田 嘉宏, 井村 誠孝, 大城 理
  - date: 2013-05
  - publication_info: 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報
  - doi: —

- **聴覚フィードバックを用いた歌唱時の音程操作 (マルチメディア・仮想環境基礎)** (`rm:misc:19346903`)
  - category (guess): Misc.
  - authors: 井手口 裕太, 横畑 亮輔, 井村 誠孝, 浦西 友樹, 黒田 嘉宏, 大城 理
  - date: 2013-05
  - publication_info: 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報
  - doi: —

- **力覚提示指向の大変形有限要素法シミュレーション(<特集>医療・福祉・ヘルスケアとVR)** (`rm:misc:19346906`)
  - category (guess): Misc.
  - authors: 黒田 嘉宏, 浦西 友樹, 井村 誠孝, 大城 理
  - date: 2013
  - publication_info: 日本バーチャルリアリティ学会論文誌
  - doi: 10.18974/tvrsj.18.4_497

- **2-4 入力音声に応じた文字装飾が可能な電子黒板(第2部門ヒューマンインタフェース)** (`rm:misc:19346905`)
  - category (guess): Misc.
  - authors: 籏岡 亮, 井村 誠孝, 浦西 友樹, 黒田 嘉宏, 大城 理
  - date: 2013
  - publication_info: 映像情報メディア学会年次大会講演予稿集
  - doi: 10.11485/iteac.2013.0_2_1

- **カメラズームによる内部パラメータの変化を考慮した拡張現実感のためのカメラ位置・姿勢推定 (マルチメディア・仮想環境基礎)** (`rm:misc:19346907`)
  - category (guess): Misc.
  - authors: 岡田 和也, 武富 貴史, 山本 豪志朗, 浦西 友樹, 宮崎 純, 加藤 博一
  - date: 2012-09
  - publication_info: 電子情報通信学会技術研究報告 : 信学技報
  - doi: —

- **OpenCV : Open Computer Vision Library (特集 画像処理ライブラリ : 画像処理をより簡単に)** (`rm:misc:19346917`)
  - category (guess): Misc.
  - authors: 浦西 友樹
  - date: 2012-07
  - publication_info: 映像情報industrial
  - doi: —

- **認知症患者の在宅支援技術に関する検討 (第92回ヒューマンインタフェース学会研究会 インタラクションのデザインと評価および一般)** (`rm:misc:19346919`)
  - category (guess): Misc.
  - authors: Hyry Jaakko, 山本 豪志朗, 浦西 友樹
  - date: 2012
  - publication_info: ヒューマンインタフェース学会研究報告集
  - doi: —

- **データアクセスの改良による時系列パターンマイニングアルゴリズムの高速化** (`rm:misc:19346908`)
  - category (guess): Misc.
  - authors: 松原 裕貴, 宮崎 純, 山本 豪志朗, 浦西 友樹, 池田 聖, 加藤 博一
  - date: 2011-10
  - publication_info: 研究報告データベースシステム（DBS）
  - doi: —

- **透明物体に内包される不透明物体のシルエット形状補正 (コンピュータビジョンとイメージメディア(CVIM) Vol.2011-CVIM-175)** (`rm:misc:19346909`)
  - category (guess): Misc.
  - authors: 鈴本 悠輝, 浦西 友樹, 眞鍋 佳嗣
  - date: 2011-02
  - publication_info: 情報処理学会研究報告
  - doi: —

- **透明物体に内包される不透明物体のシルエット形状補正** (`rm:misc:19346911`)
  - category (guess): Misc.
  - authors: 鈴本 悠輝, 浦西 友樹, 眞鍋 佳嗣, 池田 聖, 千原 國宏
  - date: 2011-01
  - publication_info: 電子情報通信学会技術研究報告. MVE, マルチメディア・仮想環境基礎
  - doi: —

- **透明物体に内包される不透明物体のシルエット形状補正** (`rm:misc:19346910`)
  - category (guess): Misc.
  - authors: 鈴本 悠輝, 浦西 友樹, 眞鍋 佳嗣, 池田 聖, 千原 國宏
  - date: 2011-01
  - publication_info: 電子情報通信学会技術研究報告. PRMU, パターン認識・メディア理解
  - doi: —

- **8-12 拡張現実のための重ね合わせと自由回転可能な円形カラーマーカの提案(第8部門 メディア工学3)** (`rm:misc:19346913`)
  - category (guess): Misc.
  - authors: 鈴木 朝日, 眞鍋 佳嗣, 矢田 紀子, 浦西 友樹
  - date: 2011
  - publication_info: 映像情報メディア学会冬季大会講演予稿集
  - doi: 10.11485/itewac.2011.0_8_12

- **8-13 GPUを用いた複合現実感における映り込み表現の最適化(第8部門 メディア工学3)** (`rm:misc:19346912`)
  - category (guess): Misc.
  - authors: 小林 正英, 眞鍋 佳嗣, 矢田 紀子, 浦西 友樹
  - date: 2011
  - publication_info: 映像情報メディア学会冬季大会講演予稿集
  - doi: 10.11485/itewac.2011.0_8_13

- **H-023 不透明物体を内包する透明物体の形状計測のためのシルエット分離抽出(H分野:画像認識・メディア理解,一般論文)** (`rm:misc:19346914`)
  - category (guess): Misc.
  - authors: 鈴本 悠輝, 浦西 友樹, 眞鍋 佳嗣, 千原 國宏
  - date: 2010-08
  - publication_info: 情報科学技術フォーラム講演論文集
  - doi: —

- **A-15-9 指輪型マーカの三次元位置姿勢推定(A-15.ヒューマン情報処理,一般セッション)** (`rm:misc:19346915`)
  - category (guess): Misc.
  - authors: 藤木 健史, 浦西 友樹, 佐々木 博史, 眞鍋 佳嗣, 千原 國宏
  - date: 2010-03
  - publication_info: 電子情報通信学会総合大会講演論文集
  - doi: —

- **フィンガジェスチャインタフェース”Ubi-WA”の試作アプリケーションによる評価** (`rm:misc:34477179`)
  - category (guess): Misc.
  - authors: 藤木健史, 浦西友樹, 佐々木博史, 眞鍋佳嗣, 千原國宏
  - date: 2010
  - publication_info: システム制御情報学会研究発表講演会講演論文集(CD-ROM)
  - doi: —

- **重ね合わせ可能な半透明二次元カラーマーカ(<特集>テーブルトップ・インタラクション)** (`rm:misc:19346916`)
  - category (guess): Misc.
  - authors: 浦西 友樹, 今村 昂司, 眞鍋 佳嗣, 佐々木 博史, 千原 國宏
  - date: 2010
  - publication_info: 日本バーチャルリアリティ学会論文誌
  - doi: —

- **オープンソース画像処理ライブラリ「OpenCV」 (特集 マシンビジョンを活気づける画像処理ライブラリ)** (`rm:misc:19346918`)
  - category (guess): Misc.
  - authors: 浦西 友樹
  - date: 2009-03
  - publication_info: 映像情報industrial
  - doi: —

- **奈良ユニバーサロン ログ・イン 1000文字講座 物体の三次元形状を画像から知る(上・下)** (`rm:misc:18561780`)
  - category (guess): Misc.
  - authors: 浦西友樹
  - date: 2009-03
  - publication_info: 毎日新聞奈良版
  - doi: —

- **D-12-38 形状特徴を用いた非文字領域除去処理による文字列領域抽出の高精度化(D-12.パターン認識・メディア理解A)** (`rm:misc:19346899`)
  - category (guess): Misc.
  - authors: 浦西 友樹, 松尾 賢一, 上田 勝彦
  - date: 2004-03
  - publication_info: 電子情報通信学会総合大会講演論文集
  - doi: —

### Presentations (non-invited) (26)

- **SmartVP: Viewpoint Optimization Based on Individual Preference for Watching 3D Boxing Punch Videos** (`rm:presentations:42562567`)
  - category (guess): Presentations (non-invited)
  - authors: Tao Tao, Photchara Ratsamee, Chang Liu, Yuki Uranishi, Haruo Takemura
  - date: 2023-03
  - publication_info: Proceedings of the 2023 5th International Conference on Image, Video and Signal Processing
  - doi: 10.1145/3591156.3591171

- **Characteristics of Background Color Shifts Caused by Optical See-Through Head-Mounted Displays** (`rm:presentations:42216463`)
  - category (guess): Presentations (non-invited)
  - authors: Daichi Hirobe, Yuki Uranishi, Jason Orlosky, Shizuka Shirai, Photchara Ratsamee, Haruo Takemura
  - date: 2022-12
  - publication_info: ICAT-EGVE 2022 - International Conference on Artificial Reality and Telexistence and Eurographics Symposium on Virtual Environments
  - doi: 10.2312/egve.20221285

- **Thermal-to-Color Image Translation for Enhancing Visual Odometry of Thermal Vision** (`rm:presentations:42850046`)
  - category (guess): Presentations (non-invited)
  - authors: Liyun Zhang, Photchara Ratsamee, Yuki Uranishi, Manabu Higashida, Haruo Takemura
  - date: 2022-11
  - publication_info: 2022 IEEE International Symposium on Safety, Security, and Rescue Robotics (SSRR)
  - doi: 10.1109/ssrr56537.2022.10018810

- **Exploring Three-Dimensional Locomotion Techniques in Virtual Reality** (`rm:presentations:42850399`)
  - category (guess): Presentations (non-invited)
  - authors: Donghae Lim, Shizuka Shirai, Jason Orlosky, Photchara Ratsamee, Yuki Uranishi, Haruo Takemura
  - date: 2022-10
  - publication_info: 2022 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct)
  - doi: 10.1109/ismar-adjunct57072.2022.00105

- **Objective Measurements of Background Color Shifts Caused by Optical See-Through Head-Mounted Displays** (`rm:presentations:42850051`)
  - category (guess): Presentations (non-invited)
  - authors: Daichi Hirobe, Yuki Uranishi, Jason Orlosky, Shizuka Shirai, Photchara Ratsamee, Haruo Takemura
  - date: 2022-10
  - publication_info: 2022 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct)
  - doi: 10.1109/ismar-adjunct57072.2022.00084

- **A Japanese Character Flick-Input Interface for Entering Text in VR** (`rm:presentations:37545911`)
  - category (guess): Presentations (non-invited)
  - authors: Ryota Takahashi, Shizuka Shirai, Jason Orlosky, Yuki Uranishi, Haruo Takemura
  - date: 2021-10
  - publication_info: 2021 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct)
  - doi: 10.1109/ismar-adjunct54149.2021.00058

- **Evaluating Presence in VR with Self-Representing Auditory-Vibrotactile Input** (`rm:presentations:34861869`)
  - category (guess): Presentations (non-invited)
  - authors: Guanghan Zhao, Jason Orlosky, Yuki Uranishi
  - date: 2021-03
  - publication_info: 2021 IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops (VRW)
  - doi: 10.1109/vrw52623.2021.00171

- **Rainbow Learner: Lighting Environment Estimation from a Structural-color based AR Marker** (`rm:presentations:34861868`)
  - category (guess): Presentations (non-invited)
  - authors: Yuji Tsukagoshi, Yuki Uranishi, Jason Orlosky, Kiyomi Ito, Haruo Takemura
  - date: 2020-12
  - publication_info: 2020 IEEE International Conference on Artificial Intelligence and Virtual Reality (AIVR)
  - doi: 10.1109/aivr50618.2020.00074

- **Detecting Learner Drowsiness Based on Facial Expressions and Head Movements in Online Courses** (`rm:presentations:29489371`)
  - category (guess): Presentations (non-invited)
  - authors: Shogo Terai, Shizuka Shirai, Mehrasa Alizadeh, Ryosuke Kawamura, Noriko Takemura, Yuki Uranishi, Haruo Takemura, Hajime Nagahara
  - date: 2020-03
  - publication_info: Proceedings of the 25th International Conference on Intelligent User Interfaces Companion
  - doi: 10.1145/3379336.3381500

- **Real-to-Synthetic Feature Transform for Illumination Invariant Camera Localization** (`rm:presentations:34790122`)
  - category (guess): Presentations (non-invited)
  - authors: Sota Shoman, Tomohiro Mashita, Alexander Plopski, Photchara Ratsamee, Yuki Uranishi
  - date: 2020
  - publication_info: IEEE Computer Graphics and Applications
  - doi: 10.1109/mcg.2020.3041617

- **機械学習に基づくEpipolar Plane Imagesからの透明物体の屈折率推定** (`rm:presentations:16639246`)
  - category (guess): Presentations (non-invited)
  - authors: 浦西友樹, HOLDCROFT T, 間下以大, RATSAMEE P, 竹村治雄
  - date: 2019-05
  - publication_info: システム制御情報学会研究発表講演会講演論文集(CD-ROM)
  - doi: —

- **オープンソース画像処理ライブラリOpenCV:様々な環境での“Hello World“** (`rm:presentations:16639245`)
  - category (guess): Presentations (non-invited)
  - authors: 浦西友樹
  - date: 2019-05
  - publication_info: システム制御情報学会研究発表講演会講演論文集(CD-ROM)
  - doi: —

- **多重焦点顕微鏡画像列からの細胞の3次元形状復元** (`rm:presentations:16639247`)
  - category (guess): Presentations (non-invited)
  - authors: 山口貴大, 長原一, 諸岡健一, 中島悠太, 浦西友樹, 倉爪亮, 大野英治
  - date: 2019-01
  - publication_info: 電子情報通信学会技術研究報告
  - doi: —

- **構造色パターンから光源方向を推定可能なARマーカ** (`rm:presentations:16639249`)
  - category (guess): Presentations (non-invited)
  - authors: 伊藤澄美, 浦西友樹, RATSAMEE Photchara, 間下以大, 竹村治雄
  - date: 2018-10
  - publication_info: 電子情報通信学会技術研究報告
  - doi: —

- **透明感操作のためのcGANsによる集光模様の実時間生成** (`rm:presentations:16639248`)
  - category (guess): Presentations (non-invited)
  - authors: 岡本拓朗, 浦西友樹, 間下以大, RATSAMEE Photchara, 竹村治雄
  - date: 2018-10
  - publication_info: 電子情報通信学会技術研究報告
  - doi: —

- **Illumination invariant camera localization using synthetic images** (`rm:presentations:21725801`)
  - category (guess): Presentations (non-invited)
  - authors: Sota Shoman, Tomohiro Mashita, Alexander Plopski, Photchara Ratsamee, Yuki Uranishi, Haruo Takemura
  - date: 2018-10
  - publication_info: —
  - doi: —

- **映像監視空間の構築を支援するHMDを用いた3Dユーザインタフェース** (`rm:presentations:16639251`)
  - category (guess): Presentations (non-invited)
  - authors: 駒走友哉, 小池正英, RATSAMEE Photchara, RATSAMEE Photchara, 間下以大, 間下以大, 浦西友樹, 浦西友樹, 竹村治雄, 竹村治雄
  - date: 2018-09
  - publication_info: 日本バーチャルリアリティ学会大会論文集(CD-ROM)
  - doi: —

- **気流の可視化に伴い変化する温度感の評価** (`rm:presentations:16639250`)
  - category (guess): Presentations (non-invited)
  - authors: 金山哲也, 間下以大, 浦西友樹, RATSAMEE Photchara, 竹村治雄
  - date: 2018-09
  - publication_info: 日本バーチャルリアリティ学会大会論文集(CD-ROM)
  - doi: —

- **光源方向推定のための構造色パターンマッチング** (`rm:presentations:16639253`)
  - category (guess): Presentations (non-invited)
  - authors: 浦西友樹, 井村誠孝, 黒田知宏, 大城理
  - date: 2015-05
  - publication_info: 第59回システム制御情報学会研究発表講演会講演論文集
  - doi: —

- **視認性の高い投影のための色と形状に基づくシーンの評価 (マルチメディア・仮想環境基礎)** (`rm:presentations:16639256`)
  - category (guess): Presentations (non-invited)
  - authors: 團原 佑壮, 浦西 友樹, 吉元 俊輔, 井村 誠孝, 大城 理
  - date: 2015-01
  - publication_info: 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報
  - doi: —

- **視認性の高い投影のための色と形状に基づくシーンの評価** (`rm:presentations:16639254`)
  - category (guess): Presentations (non-invited)
  - authors: 團原佑壮, 浦西友樹, 吉元俊輔, 井村誠孝, 大城理
  - date: 2015-01
  - publication_info: 電子情報通信学会技術 研究報告
  - doi: —

- **Haptylus: Haptic Stylus for Interaction with Virtual Objects behind a Touch Screen** (`rm:presentations:16639257`)
  - category (guess): Presentations (non-invited)
  - authors: Shingo Nagasaka, Yuki Uranishi, Shunsuke Yoshimoto, Masataka Imura, Osamu Oshiro
  - date: 2014-12
  - publication_info: ACM SIGGRAPH Asia 2014 Emerging Technologies
  - doi: 10.1145/2669047.2669054

- **光計測を用いた爪装着型指先接触力センサ (MEとバイオサイバネティックス)** (`rm:presentations:16639259`)
  - category (guess): Presentations (non-invited)
  - authors: 豆野 裕信, 井村 誠孝, 吉元 俊輔, 浦西 友樹, 大城 理
  - date: 2014-10
  - publication_info: 電子情報通信学会技術研究報告 = IEICE technical report : 信学技報
  - doi: —

- **Tactile Roughness Modulation of Material Surfaces Using Electrical Stimulus** (`rm:presentations:16639264`)
  - category (guess): Presentations (non-invited)
  - authors: Shunsuke Yoshimoto, Yoshihiro Kuroda, Yuki Uranishi, Masataka Imura, Osamu Oshiro
  - date: 2014-07
  - publication_info: International Symposium Future of Shitsukan Research
  - doi: —

- **Roughness Modulation of Real Materials using Electrotactile Augmentation** (`rm:presentations:16639266`)
  - category (guess): Presentations (non-invited)
  - authors: Shunsuke Yoshimoto, Yoshihiro Kuroda, Yuki Uranishi, Masataka Imura, Osamu Oshiro
  - date: 2014-06
  - publication_info: Proceedings of Eurohaptics 2014
  - doi: —

- **投球シミュレーションのための野球ボールのリリースモデル** (`rm:presentations:16639265`)
  - category (guess): Presentations (non-invited)
  - authors: 井村誠孝, 横畑亮輔, 浦西友樹, 吉元俊輔, 黒田嘉宏, 大城理
  - date: 2014-05
  - publication_info: 第58回システム制御情報学会研究発表講演会 講演論文集
  - doi: —

### RM:published_papers (10)

- **3D Pointing Gestures as Target Selection Tools for Monocular UAVs** (`rm:published_papers:52667691`)
  - category (guess): RM:published_papers
  - authors: Anna C S Medeiros, Photchara Ratsamee, Jason Orlosky, Yuki Uranishi, Manabu Higashida, Haruo Takemura
  - date: 2020-10
  - publication_info: —
  - doi: 10.21203/rs.3.rs-90798/v1

- **軟組織変形追跡のための狭帯域画像を用いた多層テンプレートマッチング手法** (`rm:published_papers:35456566`)
  - category (guess): RM:published_papers
  - authors: 黒田 嘉宏, 田村 裕樹, 間下 以大, 浦西 友樹, 清川 清, 吉田 健志, 松田 公志, 大城 理, 竹村 治雄
  - date: 2017
  - publication_info: 生体医工学
  - doi: 10.11239/jsmbe.55annual.181

- **失敗を可視化する採血トレーナ** (`rm:published_papers:27809309`)
  - category (guess): RM:published_papers
  - authors: 浦西友樹, 丸山裕, 内藤知佐子, 岡本和也, 田村寛, 加藤源太, 黒田知宏
  - date: 2017
  - publication_info: 日本バーチャルリアリティ学会論文誌(Web)
  - doi: 10.18974/tvrsj.22.2_217

- **CCDR-PAID: More Efficient Cache-Conscious PAID Algorithm by Data Reconstruction** (`rm:published_papers:25883012`)
  - category (guess): RM:published_papers
  - authors: Yuki Matsubara, Jun Miyazaki, Goshiro Yamamoto, Yuki Uranishi, Sei Ikeda, Hirokazu Kato
  - date: 2012-03
  - publication_info: Proc. of the 27th ACM Symposium On Applied Computing
  - doi: 10.1145/2245276.2245313

- **コンピュータ画像処理コンピュータ画像処理, 2006** (`rm:published_papers:27100780`)
  - category (guess): RM:published_papers
  - authors: 三宅正夫, 眞鍋佳嗣, 浦西友樹, 池田聖, 千原國安
  - date: 2012
  - publication_info: 日本色彩学会誌
  - doi: —

- **糖尿病網膜症 働き盛りの約 300 万人が発症 毎年約 3000 人が失明糖尿病網膜症 働き盛りの約 300 万人が発症 毎年約 3000 人が失明, 2005** (`rm:published_papers:27100774`)
  - category (guess): RM:published_papers
  - authors: 三宅正夫, 眞鍋佳嗣, 浦西友樹, 池田聖, 千原國安
  - date: 2012
  - publication_info: 日本色彩学会誌
  - doi: —

- **新配色カード 199c 12cm$\times$ 17.5 cm 新配色カード 199c 12cm$\times$ 17.5 cm** (`rm:published_papers:27100772`)
  - category (guess): RM:published_papers
  - authors: 三宅正夫, 眞鍋佳嗣, 浦西友樹, 池田聖, 千原國安
  - date: 2012
  - publication_info: 日本色彩学会誌
  - doi: —

- **学校用色覚異常検査表学校用色覚異常検査表, 1985** (`rm:published_papers:27100770`)
  - category (guess): RM:published_papers
  - authors: 三宅正夫, 眞鍋佳嗣, 浦西友樹, 池田聖, 千原國安
  - date: 2012
  - publication_info: 日本色彩学会誌
  - doi: —

- **ソフト名: おしゃべりテキスト, プログラム名: OsyaberiText. exe ソフト名: おしゃべりテキスト, プログラム名: OsyaberiText. exe** (`rm:published_papers:27100768`)
  - category (guess): RM:published_papers
  - authors: 三宅正夫, 眞鍋佳嗣, 浦西友樹, 池田聖, 千原國安
  - date: 2012
  - publication_info: 日本色彩学会誌
  - doi: —

- **PROPOSAL OF TRACKING LAN ANTENNA USING IMAGE SENSOR** (`rm:published_papers:27100865`)
  - category (guess): RM:published_papers
  - authors: Uranishi Yuki, Ikeda Sei, Shimada Hideki, MANABE Yoshitsugu, CHIHARA Kunihiro
  - date: 2009-01
  - publication_info: 電子情報通信学会技術研究報告. IE, 画像工学
  - doi: —

## publications.json のみ（73 件）

### Books (2)

- **データ・AI利活用のための情報リテラシー入門** (`site:id=1`)
  - category: Books
  - authors: 白井詩沙香, 天野由貴, 浦西友樹, 小野淳, 小林聖人, 竹村治雄, 田中冬彦, 千葉直也, 長瀧寛之, 西田知博, 村上正行
  - date: 2025-04
  - publication_info: 培風館
  - doi: —
  - raw_text: 白井詩沙香 (編著), 天野由貴, 浦西友樹, 小野淳, 小林聖人, 竹村治雄, 田中冬彦, 千葉直也, 長瀧寛之, 西田知博, 村上正行 (著), "データ・AI利活用のための情報リテラシー入門", 培風館 (2025.4)

- **OpenCV 3 プログラミングブック** (`site:id=4`)
  - category: Books
  - authors: 藤本雄一郎, 青砥隆仁, 浦西友樹, 大倉史生, 小枝正直, 中島悠太, 山本豪志朗
  - date: 2015-09
  - publication_info: マイナビ
  - doi: —
  - raw_text: 藤本雄一郎, 青砥隆仁, 浦西友樹, 大倉史生, 小枝正直, 中島悠太, 山本豪志朗 (著), "OpenCV 3 プログラミングブック", マイナビ (2015.9)

### Domestic Conference Proceedings (33)

- **自然言語・画像情報を活用したロボットアームの階層型バイラテラル制御に基づく模倣学習** (`site:id=307`)
  - category: Domestic Conference Proceedings
  - authors: 小林聖人, Thanpimon Buamanee, 浦西友樹
  - date: 2026-03
  - publication_info: 言語処理学会 第32回年次大会 (NLP2026)
  - doi: —
  - raw_text: 小林聖人, Thanpimon Buamanee, 浦西友樹, "自然言語・画像情報を活用したロボットアームの階層型バイラテラル制御に基づく模倣学習", 言語処理学会 第32回年次大会 (NLP2026), March, 2026

- **VR環境を用いた和太鼓練習支援システムの提案とモチベーションへの影響評価** (`site:id=310`)
  - category: Domestic Conference Proceedings
  - authors: 平谷歩香, 中村拓人, 千葉直也, 浦西友樹
  - date: 2025-09
  - publication_info: 第30回日本バーチャルリアリティ学会大会
  - doi: —
  - raw_text: 平谷歩香, 中村拓人, 千葉直也, 浦西友樹, "VR環境を用いた和太鼓練習支援システムの提案とモチベーションへの影響評価", 第30回日本バーチャルリアリティ学会大会 (2025.9)

- **大阪大学における一般情報教育の改定に向けた取り組み：高等学校「情報I」への対応** (`site:id=312`)
  - category: Domestic Conference Proceedings
  - authors: 白井詩沙香, 中村拓人, 田中冬彦, 千葉直也, 東田学, 小林聖人, 長瀧寛之, 村上正行, 西田知博, 小野淳, 天野由貴, 竹村治雄, 浦西友樹
  - date: 2025-08
  - publication_info: 大学ICT推進協議会2025年度年次大会論文集
  - doi: —
  - raw_text: 白井詩沙香, 中村拓人, 田中冬彦, 千葉直也, 東田学, 小林聖人, 長瀧寛之, 村上正行, 西田知博, 小野淳, 天野由貴, 竹村治雄, 浦西友樹, "大阪大学における一般情報教育の改定に向けた取り組み：高等学校「情報I」への対応", 大学ICT推進協議会年次大会論文集, pp. 245-246 (2025)

- **大阪大学の2025年度新入生に対する高等学校情報科の学びに関するアンケート調査報告** (`site:id=313`)
  - category: Domestic Conference Proceedings
  - authors: 長瀧寛之, 白井詩沙香, 中村拓人, 浦西友樹
  - date: 2025-08
  - publication_info: 大学ICT推進協議会2025年度年次大会論文集
  - doi: —
  - raw_text: 長瀧寛之, 白井詩沙香, 中村拓人, 浦西友樹, "大阪大学の2025年度新入生に対する高等学校情報科の学びに関するアンケート調査報告", 大学ICT推進協議会年次大会論文集, pp. 247-248 (2025)

- **Robotics-inspired Control for Audio-driven 3D Facial Motion Synthesis** (`site:id=311`)
  - category: Domestic Conference Proceedings
  - authors: Xuanmeng Sha, Liyun Zhang, Tomohiro Mashita, Naoya Chiba, Yuki Uranishi
  - date: 2025-07
  - publication_info: 第28回画像の認識・理解シンポジウム (MIRU2025)
  - doi: —
  - raw_text: Xuanmeng Sha, Liyun Zhang, Tomohiro Mashita, Naoya Chiba, Yuki Uranishi, "Robotics-inspired Control for Audio-driven 3D Facial Motion Synthesis", 第28回画像の認識・理解シンポジウム (MIRU2025) (2025.7)

- **複合現実技術と言語指示に基づく自律移動ロボットインタフェース** (`site:id=163`)
  - category: Domestic Conference Proceedings
  - authors: Iglesius Eduardo, 小林聖人, 浦西友樹
  - date: 2025-06
  - publication_info: ロボティクス・メカトロニクス講演会
  - doi: —
  - raw_text: Iglesius Eduardo, 小林聖人, 浦西友樹, "複合現実技術と言語指示に基づく自律移動ロボットインタフェース", ロボティクス・メカトロニクス講演会, 山形 (2025.6)

- **言語情報を活用したバイラテラル制御に基づく模倣学習** (`site:id=162`)
  - category: Domestic Conference Proceedings
  - authors: 小林拓史, 小林聖人, Thanpimon Buamanee, 浦西友樹
  - date: 2025-06
  - publication_info: ロボティクス・メカトロニクス講演会
  - doi: —
  - raw_text: 小林拓史, 小林聖人, Thanpimon Buamanee, 浦西友樹, "言語情報を活用したバイラテラル制御に基づく模倣学習", ロボティクス・メカトロニクス講演会, 山形 (2025.6)

- **自律移動ロボットのための複合現実技術を用いた地図更新システム** (`site:id=161`)
  - category: Domestic Conference Proceedings
  - authors: 多喜匠, 小林聖人, Iglesius Eduardo, 千葉直也, 白井詩沙香, 浦西友樹
  - date: 2025-06
  - publication_info: ロボティクス・メカトロニクス講演会
  - doi: —
  - raw_text: 多喜匠, 小林聖人, Iglesius Eduardo, 千葉直也, 白井詩沙香, 浦西友樹, "自律移動ロボットのための複合現実技術を用いた地図更新システム", ロボティクス・メカトロニクス講演会, 山形 (2025.6)

- **教育・スポーツトレーニング・医療へのXR技術の応用** (`site:id=309`)
  - category: Domestic Conference Proceedings
  - authors: 浦西友樹, 小林聖人, 東田学, 中村拓人, 白井詩沙香, 千葉直也
  - date: 2025-06
  - publication_info: 第24回日本VR医学会学術大会
  - doi: —
  - raw_text: 浦西友樹, 小林聖人, 東田学, 中村拓人, 白井詩沙香, 千葉直也, "教育・スポーツトレーニング・医療への XR技術の応用", 第24回日本VR医学会学術大会 (2025)

- **Exploratory research on learning analytics adoption in Japanese higher educational institutions** (`site:id=164`)
  - category: Domestic Conference Proceedings
  - authors: David Soto, Shizuka Shirai, Mayumi Ueda, Manabu Higashida, Masayuki Murakami, Yuki Uranishi
  - date: 2025-03
  - publication_info: 情報処理学会第87回全国大会
  - doi: —
  - raw_text: Uranishi, " Exploratory research on learning analytics adoption in Japanese higher educational institutions ", 情報処理学会第87回全国大会, 大阪 (2025.3)

- **バイラテラル制御を用いた水中多自由度ロボットアームの遠隔操作システムに関する基礎的研究** (`site:id=166`)
  - category: Domestic Conference Proceedings
  - authors: 西滉平, 小林聖人, 浦西友樹
  - date: 2024-09
  - publication_info: 日本ロボット学会学術講演会
  - doi: —
  - raw_text: 西滉平, 小林聖人, 浦西友樹, "バイラテラル制御を用いた水中多自由度ロボットアームの遠隔操作システムに関する基礎的研究", 日本ロボット学会学術講演会, 大阪 (2024.9)

- **視覚・力触覚情報を活用したバイラテラル制御に基づく模倣学習によるロボットアームの行動生成手法に関する研究** (`site:id=165`)
  - category: Domestic Conference Proceedings
  - authors: 小林聖人, Thanpimon Buamanee, 浦西友樹
  - date: 2024-09
  - publication_info: 日本ロボット学会学術講演会
  - doi: —
  - raw_text: 小林聖人, Thanpimon Buamanee, 浦西友樹, "視覚・力触覚情報を活用したバイラテラル制御に基づく模倣学習によるロボットアームの行動生成手法に関する研究", 日本ロボット学会学術講演会, 大阪 (2024.9)

- **バイラテラル制御に基づく模倣学習におけるロボットアームの動作生成手法に関する研究** (`site:id=168`)
  - category: Domestic Conference Proceedings
  - authors: 小林聖人, Thanpimon Buamanee, Iglesius Eduardo, 西滉平, 浦西友樹, 竹村治雄
  - date: 2023-11
  - publication_info: 電気学会産業計測制御研究会
  - doi: —
  - raw_text: 小林聖人, Thanpimon Buamanee, Iglesius Eduardo, 西滉平 , 浦西友樹, 竹村治雄, "バイラテラル制御に基づく模倣学習におけるロボットアームの動作生成手法に関する研究", 電気学会産業計測制御研究会 , IIC-23-033, 東京 (2023.11)

- **水中におけるバイラテラル制御に基づく遠隔操作ロボットシステムの基礎検討** (`site:id=167`)
  - category: Domestic Conference Proceedings
  - authors: 西滉平, 小林聖人, 元井直樹, 浦西友樹, 竹村治雄
  - date: 2023-11
  - publication_info: 電気学会産業計測制御研究会
  - doi: —
  - raw_text: 西滉平, 小林聖人 , 元井直樹 , 浦西友樹, 竹村治雄, "水中におけるバイラテラル制御に基づく遠隔操作ロボットシステムの基礎検討", 電気学会産業計測制御研究会 , IIC-23-032, 東京 (2023.11)

- **微分可能レンダリングを用いた透明物体の自由視点画像生成** (`site:id=169`)
  - category: Domestic Conference Proceedings
  - authors: 城彰彦, 浦西友樹, 長原一
  - date: 2023-01
  - publication_info: 情報処理学会研究報告
  - doi: —
  - raw_text: 城彰彦, 浦西友樹, 長原一, “微分可能レンダリングを用いた透明物体の自由視点画像生成,” 情報処理学会研究報告, vol. 2023-CVIM-232, No. 23, 奈良 (2023.1)

- **マンガ教材読書時のリアルタイム難易度推定に向けた視線ヒートマップ分解能の検討** (`site:id=170`)
  - category: Domestic Conference Proceedings
  - authors: 坂本賢哉, 白井詩沙香, 武村紀子, Orlosky Jason, 長瀧寛之, 上田真由美, 浦西友樹, 竹村治雄
  - date: 2022-09
  - publication_info: 第27回日本バーチャルリアリティ学会大会論文集
  - doi: —
  - raw_text: 坂本賢哉, 白井詩沙香, 武村紀子, Orlosky Jason, 長瀧寛之, 上田真由美, 浦西友樹, 竹村治雄, “マンガ教材読書時のリアルタイム難易度推定に向けた視線ヒートマップ分解能の検討,” 第27回日本バーチャルリアリティ学会大会論文集, 北海道 (2022.9)

- **Rainbow Learner: 構造色パターンからの光源環境マップおよび分光分布推定** (`site:id=140`)
  - category: Domestic Conference Proceedings
  - authors: 浦西友樹*, 塚越優治*
  - date: 2022-07
  - publication_info: 第25回画像の認識・理解シンポジウム Extended Abstract [Poster]
  - doi: —
  - raw_text: 浦西友樹*, 塚越優治*, "Rainbow Learner: 構造色パターンからの光源環境マップおよび分光分布推定", 第25回画像の認識・理解シンポジウム Extended Abstract, IS2-5, 兵庫 (2022.7) [Poster] *equal contribution

- **プロジェクションマッピングを用いたボールのキックフォーム学習支援** (`site:id=171`)
  - category: Domestic Conference Proceedings
  - authors: 佐藤僚太, 浦西友樹, Photchara Ratsamee, 東田学, 竹村治雄
  - date: 2022-05
  - publication_info: 第66回システム制御情報学会研究発表講演会 論文集
  - doi: —
  - raw_text: 佐藤僚太, 浦西友樹, Photchara Ratsamee, 東田学, 竹村治雄, "プロジェクションマッピングを用いたボールのキックフォーム学習支援", 第66回システム制御情報学会研究発表講演会 論文集, 312-4, 京都 (2022.5)

- **視線情報に基づくVR空間でのマンガ教材読書時の主観的難易度推定** (`site:id=172`)
  - category: Domestic Conference Proceedings
  - authors: 坂本賢哉, 白井詩沙香, 武村紀子, Jason Orlosky, 長瀧寛之, 上田真由美, 浦西友樹, 竹村治雄
  - date: 2021-10
  - publication_info: 日本バーチャルリアリティ学会 複合現実感研究会
  - doi: —
  - raw_text: 坂本賢哉, 白井詩沙香, 武村紀子, Jason Orlosky, 長瀧寛之, 上田真由美, 浦西友樹, 竹村治雄, "視線情報に基づくVR空間でのマンガ教材読書時の主観的難易度推定", 日本バーチャルリアリティ学会 複合現実感研究会, オンライン (2021.10)

- **RGB画像と熱画像を併用した透明物体の三次元形状復元** (`site:id=174`)
  - category: Domestic Conference Proceedings
  - authors: 城彰彦, 浦西友樹, オーロスキ ジェーソン, 塚越優治
  - date: 2021-07
  - publication_info: 第24回画像の認識・理解シンポジウム Extended Abstract
  - doi: —
  - raw_text: 城彰彦, 浦西友樹, オーロスキ ジェーソン, 塚越優治, "RGB画像と熱画像を併用した透明物体の三次元形状復元", 第24回画像の認識・理解シンポジウム Extended Abstract , I11-33, オンライン (2021.7)

- **構造色パターンを利用した光源方向および分光分布推定に関する検討** (`site:id=173`)
  - category: Domestic Conference Proceedings
  - authors: 塚越優治, 浦西友樹, オーロスキ ジェーソン
  - date: 2021-07
  - publication_info: 第24回画像の認識・理解シンポジウム Extended Abstract
  - doi: —
  - raw_text: 塚越優治, 浦西友樹, オーロスキ ジェーソン, "構造色パターンを利用した光源方向および分光分布推定に関する検討" , 第24回画像の認識・理解シンポジウム Extended Abstract, I11- 25 , オンライン (2021.7)

- **SmartVP: An autonomous Viewpoint Selection for Watching a Boxing Game in Virtual Reality** (`site:id=175`)
  - category: Domestic Conference Proceedings
  - authors: 陶涛, ラサミー ポチャラ, 浦西友樹, オーロスキ ジェーソン, 東田学, 竹村治雄
  - date: 2021-05
  - publication_info: 第65回システム制御情報学会研究発表講演会 論文集
  - doi: —
  - raw_text: 竹村治雄, " SmartVP: An autonomous Viewpoint Selection for Watching a Boxing Game in Virtual Reality", 第65回システム制御情報学会研究発表講演会 論文集, TS12-02- 4 , オンライン (2021.5)

- **ClimbAR: クライミングにおける暗黙知の定量化と拡張現実による情報提示** (`site:id=300`)
  - category: Domestic Conference Proceedings
  - authors: 浦西友樹, 長濱愛珠咲, 大西和歩, 浜本多聞, オーロスキ ジェーソン, ラサミー ポチャラ, 竹村治雄
  - date: 2021-05
  - publication_info: 第65回システム制御情報学会研究発表講演会 論文集
  - doi: —
  - raw_text: 浦西友樹, 長濱愛珠咲, 大西和歩, 浜本多聞, オーロスキ ジェーソン, ラサミー ポチャラ, 竹村治雄, "ClimbAR: クライミングにおける暗黙知の定量化と拡張現実による情報提示", 第65回システム制御情報学会研究発表講演会 論文集, TS12-02-2, オンライン (2021.5)

- **GhostReplay: 人体モデルアニメーションを用いた3次元リプレイ提示によるスポーツにおける技能向上支援システム** (`site:id=301`)
  - category: Domestic Conference Proceedings
  - authors: 吉見光平, ラサミー ポチャラ, 浦西友樹, 東田学, オーロスキ ジェーソン, 竹村治雄
  - date: 2021-05
  - publication_info: 第65回システム制御情報学会研究発表講演会 論文集
  - doi: —
  - raw_text: 吉見光平, ラサミー ポチャラ, 浦西友樹, 東田学, オーロスキ ジェーソン, 竹村治雄, "GhostReplay: 人体モデルアニメーションを用いた3次元リプレイ提示によるスポーツにおける技能向上支援システム", 第65回システム制御情報学会研究発表講演会 論文集, TS12-02-3, オンライン (2021.5)

- **坂道の昇降感覚を提示する靴型デバイスの開発** (`site:id=179`)
  - category: Domestic Conference Proceedings
  - authors: 谷本識心, Photchara Ratsamee, Jason Orlosky, 浦西友樹, 竹村治雄
  - date: 2020-10
  - publication_info: 日本バーチャルリアリティ学会 複合現実感研究会
  - doi: —
  - raw_text: 谷本識心, Photchara Ratsamee, Jason Orlosky, 浦西友樹, 竹村治雄, "坂道の昇降感覚を提示する靴型デバイスの開発, 日本バーチャルリアリティ学会 複合現実感研究会, MR2020-18, 函館/オンライン (2020.10)

- **登攀動作に内在する練度の定量化** (`site:id=178`)
  - category: Domestic Conference Proceedings
  - authors: 長濱愛珠咲, 浦西友樹, Photchara Ratsamee, Jason Orlosky, 竹村治雄
  - date: 2020-10
  - publication_info: 日本バーチャルリアリティ学会 複合現実感研究会
  - doi: —
  - raw_text: 長濱愛珠咲, 浦西友樹, Photchara Ratsamee, Jason Orlosky, 竹村治雄, "登攀動作に内在する練度の定量化", 日本バーチャルリアリティ学会 複合現実感研究会, MR2020-14, 函館/オンライン (2020.10)

- **大阪大学におけるオンライン授業支援の取り組み** (`site:id=314`)
  - category: Domestic Conference Proceedings
  - authors: 白井詩沙香, 東田学, 小島一秀, 浦西友樹, 上田佑樹, 宮永勢次, 竹村治雄
  - date: 2020-10
  - publication_info: 大学ICT推進協議会2020年度年次大会論文集
  - doi: —
  - raw_text: 白井詩沙香, 東田学, 小島一秀, 浦西友樹, 上田佑樹, 宮永勢次, 竹村治雄, "大阪大学におけるオンライン授業支援の取り組み", AXIES2021年次大会論文集, pp. 385-390 (2020)

- **Rainbow Learner: 構造色パターンから光源環境を実時間推定可能なARマーカ** (`site:id=141`)
  - category: Domestic Conference Proceedings
  - authors: 塚越優治, 浦西友樹
  - date: 2020-08
  - publication_info: 第23回画像の認識・理解シンポジウム Extended Abstract [Short Oral]
  - doi: —
  - raw_text: 塚越優治, 浦西友樹, "Rainbow Learner: 構造色パターンから光源環境を実時間推定可能なARマーカ", 第23回画像の認識・理解シンポジウム Extended Abstract, OS1-2B-5, Online (2020.8) [Short Oral]

- **VRパラグライダー飛行トレーナーの開発** (`site:id=183`)
  - category: Domestic Conference Proceedings
  - authors: 長濱愛珠咲, 浜本多聞, 竹村治雄, Photchara Ratsamee, 浦西友樹
  - date: 2019-10
  - publication_info: 日本バーチャルリアリティ学会 複合現実感研究会
  - doi: —
  - raw_text: 長濱愛珠咲, 浜本多聞, 竹村治雄, Photchara Ratsamee, 浦西友樹, "VRパラグライダー飛行トレーナーの開発", 日本バーチャルリアリティ学会 複合現実感研究会, ウトロ (2019.10)

- **点群の位置合わせのためのローカルパッチ類似度推測** (`site:id=182`)
  - category: Domestic Conference Proceedings
  - authors: 田又健士朗, 間下以大, 浦西友樹, Photchara Ratsamee
  - date: 2019-10
  - publication_info: 日本バーチャルリアリティ学会 複合現実感研究会
  - doi: —
  - raw_text: 田又健士朗, 間下以大, 浦西友樹, Photchara Ratsamee, "点群の位置合わせのためのローカルパッチ類似度推測", 日本バーチャルリアリティ学会 複合現実感研究会, ウトロ (2019.10)

- **FrictionHaptics: 摩擦力提示のためのハプティックデバイス** (`site:id=181`)
  - category: Domestic Conference Proceedings
  - authors: 目黒僚, Photchara Ratsamee, 間下以大, 浦西友樹, 竹村治雄
  - date: 2019-10
  - publication_info: 日本バーチャルリアリティ学会 複合現実感研究会
  - doi: —
  - raw_text: 目黒僚, Photchara Ratsamee, 間下以大, 浦西友樹, 竹村治雄, "FrictionHaptics: 摩擦力提示のためのハプティックデバイス", 日本バーチャルリアリティ学会 複合現実感研究会, ウトロ (2019.10)

- **Light Field Consistency for Spatial Density Estimation of Smoke** (`site:id=147`)
  - category: Domestic Conference Proceedings
  - authors: Yuta Ideguchi, Yuki Uranishi, Shunsuke Yoshimoto, Masataka Imura, Osamu Oshiro
  - date: 2015-07
  - publication_info: 第18回画像の認識・理解シンポジウム Extended Abstract [Poster]
  - doi: —
  - raw_text: Yuta Ideguchi, Yuki Uranishi, Shunsuke Yoshimoto, Masataka Imura and Osamu Oshiro, “Light Field Consistency for Spatial Density Estimation of Smoke”, 第18回画像の認識・理解シンポジウム Extended Abstract, SS1-9, 大阪 (2015.7) [Poster]

- **ウェアラブルコンピュータにおけるリング型デバイス** (`site:id=269`)
  - category: Domestic Conference Proceedings
  - authors: 藤木健史, 浦西友樹, 佐々木博史, 眞鍋佳嗣, 千原國宏
  - date: 2009-05
  - publication_info: 第53回 システム制御情報学会研究発表講演会 講演論文集
  - doi: —
  - raw_text: 藤木健史, 浦西友樹, 佐々木博史, 眞鍋佳嗣, 千原國宏, “ウェアラブルコンピュータにおけるリング型デバイス“Ubi-WA”の提案”, 第53回 システム制御情報学会研究発表講演会 講演論文集, pp.157-158, 兵庫 (2009.5)

### International Conference Proceedings (15)

- **Bi-AQUA: Bilateral Control-Based Imitation Learning for Underwater Robot Arms via Lighting-Aware Action Chunking with Transformers** (`site:id=303`)
  - category: International Conference Proceedings
  - authors: Takeru Tsunoori*, Masato Kobayashi*, Yuki Uranishi
  - date: 2026-09
  - publication_info: IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS2026)
  - doi: —
  - raw_text: Takeru Tsunoori*, Masato Kobayashi*, Yuki Uranishi, "Bi-AQUA: Bilateral Control-Based Imitation Learning for Underwater Robot Arms via Lighting-Aware Action Chunking with Transformers", IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS2026), Pittsburgh, PA, USA (2026.9) accepted *equal contribution

- **MRPoS: Mixed Reality-Based Robot Navigation Interface Using Spatial Pointing and Speech with Large Language Model** (`site:id=304`)
  - category: International Conference Proceedings
  - authors: Eduardo Iglesius*, Masato Kobayashi*, Yuki Uranishi
  - date: 2026-09
  - publication_info: IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS2026)
  - doi: —
  - raw_text: Eduardo Iglesius*, Masato Kobayashi*, Yuki Uranishi, "MRPoS: Mixed Reality-Based Robot Navigation Interface Using Spatial Pointing and Speech with Large Language Model", IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS2026), Pittsburgh, PA, USA (2026.9) accepted *equal contribution

- **Bi-HIL: Bilateral Control-Based Multimodal Hierarchical Imitation Learning via Subtask-Level Progress Rate and Keyframe Memory for Long-Horizon Contact-Rich Robotic Manipulation** (`site:id=305`)
  - category: International Conference Proceedings
  - authors: Thanpimon Buamanee*, Masato Kobayashi*, Yuki Uranishi
  - date: 2026-09
  - publication_info: IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS2026)
  - doi: —
  - raw_text: Thanpimon Buamanee*, Masato Kobayashi*, Yuki Uranishi, "Bi-HIL: Bilateral Control-Based Multimodal Hierarchical Imitation Learning via Subtask-Level Progress Rate and Keyframe Memory for Long-Horizon Contact-Rich Robotic Manipulation", IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS2026), Pittsburgh, PA, USA (2026.9) accepted *equal contribution

- **MRReP: Mixed Reality-based Hand-drawn Reference Path Editing Interface for Mobile Robot Navigation** (`site:id=306`)
  - category: International Conference Proceedings
  - authors: Takumi Taki*, Masato Kobayashi*, Yuki Uranishi
  - date: 2026-08
  - publication_info: Proceedings of the IEEE International Conference on Robot and Human Interactive Communication (RO-MAN2026)
  - doi: —
  - raw_text: Takumi Taki*, Masato Kobayashi*, Yuki Uranishi, "MRReP: Mixed Reality-based Hand-drawn Reference Path Editing Interface for Mobile Robot Navigation", Proceedings of the IEEE International Conference on Robot and Human Interactive Communication (RO-MAN2026), Kitakyushu, Fukuoka, Japan (2026.8) accepted *equal contribution

- **3DFacePolicy: Speech-Driven 3D Facial Animation Based on Diffusion Policy** (`site:id=298`)
  - category: International Conference Proceedings
  - authors: Xuanmeng Sha, Liyun Zhang, Tomohiro Mashita, Naoya Chiba and Yuki Uranishi
  - date: 2026-06
  - publication_info: the 2026 IEEE International Conference on Robotics & Automation (ICRA2026)
  - doi: —
  - raw_text: Xuanmeng Sha, Liyun Zhang, Tomohiro Mashita, Naoya Chiba and Yuki Uranishi, "3DFacePolicy: Speech-Driven 3D Facial Animation Based on Diffusion Policy", the 2026 IEEE International Conference on Robotics & Automation (ICRA2026), Vienna, Austria (2026.6) accepted

- **Viewpoint Suggestion of Feature-rich Photos Using Smartphone Photogrammetry and Keypoint Detection** (`site:id=299`)
  - category: International Conference Proceedings
  - authors: Haruka Ono, Koya Narumi and Yuki Uranishi
  - date: 2026-03
  - publication_info: Proceedings of the IEEE Conference on Virtual Reality and 3D User Interfaces (VR2026) Adjunct
  - doi: —
  - raw_text: Haruka Ono, Koya Narumi and Yuki Uranishi, "Viewpoint Suggestion of Feature-rich Photos Using Smartphone Photogrammetry and Keypoint Detection", Proceedings of the IEEE Conference on Virtual Reality and 3D User Interfaces (VR2026) Adjunct, Daegu, Korea (2026.3)

- **Detective Networks: Enhancing Disaster Recognition in Images Through Attention Shifting using Optimal Masking** (`site:id=64`)
  - category: International Conference Proceedings
  - authors: Narongthat Thanyawet, Photchara Ratsamee, Yuki Uranishi, Haruo Takemura
  - date: 2025-03
  - publication_info: Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision 2025 (WACV2025)
  - doi: —
  - raw_text: Narongthat Thanyawet, Photchara Ratsamee, Yuki Uranishi and Haruo Takemura, "Detective Networks: Enhancing Disaster Recognition in Images Through Attention Shifting using Optimal Masking", Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision 2025 (WACV2025), Tucson, AR, United States (2025.3)

- **GlanXR: A Hands-Free Fast Switching System for Virtual Screens** (`site:id=66`)
  - category: International Conference Proceedings
  - authors: Guanghan Zhao, Jason Orlosky, Kiyoshi Kiyokawa, Yuki Uranishi
  - date: 2024-10
  - publication_info: Proceedings of the 23rd International Symposium on Mixed and Augmented Reality (ISMAR2024)
  - doi: —
  - raw_text: Guanghan Zhao, Jason Orlosky, Kiyoshi Kiyokawa and Yuki Uranishi, "GlanXR: A Hands-Free Fast Switching System for Virtual Screens", Proceedings of the 23rd International Symposium on Mixed and Augmented Reality (ISMAR2024), Bellevue, WA, United States (2024.10)

- **Bi-ACT: Bilateral Control-Based Imitation Learning via Action Chunking with Transformer** (`site:id=68`)
  - category: International Conference Proceedings
  - authors: Thanpimon Buamanee*, Masato Kobayashi*, Yuki Uranishi, Haruo Takemura
  - date: 2024-08
  - publication_info: Proceedings of IEEE/ASME International Conference on Advanced Intelligent Mechatronics (AIM)
  - doi: —
  - raw_text: Thanpimon Buamanee*, Masato Kobayashi*, Yuki Uranishi and Haruo Takemura, "Bi-ACT: Bilateral Control-Based Imitation Learning via Action Chunking with Transformer", Proceedings of IEEE/ASME International Conference on Advanced Intelligent Mechatronics (AIM), pp. 385-390, Boston, MA, United States (2024.8) *equal contribution

- **Virtual Zoomorphic Accessories for Enhancing Perception of Vehicle Dynamics in Real-Time** (`site:id=70`)
  - category: International Conference Proceedings
  - authors: Koji Momota, Yuki Uranishi, Kiyoshi Kiyokawa, Jason Orlosky, Photchara Ratsamee, Masato Kobayashi
  - date: 2023-12
  - publication_info: Proceedings of the Joint 33rd International Conference on Artificial Reality and Telexistence & Eurographics Symposium on Virtual Environments (ICAT-EGVE 2023) Poster
  - doi: —
  - raw_text: Koji Momota, Yuki Uranishi, Kiyoshi Kiyokawa, Jason Orlosky, Photchara Ratsamee and Masato Kobayashi, "Virtual Zoomorphic Accessories for Enhancing Perception of Vehicle Dynamics in Real-Time", Proceedings of the Joint 33rd International Conference on Artificial Reality and Telexistence & Eurographics Symposium on Virtual Environments (ICAT-EGVE 2023) Po ster , Dublin, Ireland (2023.12)

- **Panoptic-based Object Style-Align for Thermal-to-Color Image Translation** (`site:id=72`)
  - category: International Conference Proceedings
  - authors: Liyun Zhang, Photchara Ratsamee, Bowen Wang, Manabu Higashida, Yuki Uranishi, Haruo Takemura
  - date: 2023-01
  - publication_info: IEEE/CVF Winter Conference on Applications of Computer Vision (WACV2023)
  - doi: —
  - raw_text: Liyun Zhang, Photchara Ratsamee, Bowen Wang, Manabu Higashida, Yuki Uranishi and Haruo Takemura, "Panoptic-based Object Style-Align for Thermal-to-Color Image Translation", IEEE/CVF Winter Conference on Applications of Computer Vision (WACV2023), Waikoloa, HW, United States (2023.1)

- **Surface Estimation of Transparent Object based on Local Photo Consistency** (`site:id=99`)
  - category: International Conference Proceedings
  - authors: Yuta Ideguchi, Yuki Uranishi, Shunsuke Yoshimoto, Yoshihiro Kuroda, Osamu Oshiro
  - date: 2016-01
  - publication_info: Proceedings of International Workshop on Advanced Image Technology (IWAIT2016)
  - doi: —
  - raw_text: Yuta Ideguchi, Yuki Uranishi, Shunsuke Yoshimoto, Yoshihiro Kuroda and Osamu Oshiro, "Surface Estimation of Transparent Object based on Local Photo Consistency", Proceedings of International Workshop on Advanced Image Technology (IWAIT2016), 1B-5, Busan, Korea (2016.1)

- **Oil Bubble Display: Oil Display for Flexible Interaction with Projected Images** (`site:id=135`)
  - category: International Conference Proceedings
  - authors: Junki Kawaguchi, Yuta Ideguchi, Yuki Uranishi, Shunsuke Yoshimoto, Yoshihiro Kuroda, Masataka Imura, Osamu Oshiro
  - date: 2015-10
  - publication_info: The 25th International Conference on Artificial Reality and Telexistence and the 20th Eurographics Symposium on Virtual Environments (ICAT-EGVE 2015) Demos
  - doi: —
  - raw_text: Junki Kawaguchi, Yuta Ideguchi, Yuki Uranishi, Shunsuke Yoshimoto, Yoshihiro Kuroda, Masataka Imura and Osamu Oshiro, “Oil Bubble Display: Oil Display for Flexible Interaction with Projected Images”, The 25th International Conference on Artificial Reality and Telexistence and the 20th Eurographics Symposium on Virtual Environments (ICAT-EGVE 2015) Demos, Kyoto, Japan (2015.10)

- **Deformation Estimation of Elastic Bodies Using Multiple Silhouette Images for Endoscopic Surgery** (`site:id=100`)
  - category: International Conference Proceedings
  - authors: Akira Saito, Megumi Nakao, Yuki Uranishi, Tetsuya Matsuda
  - date: 2015-09
  - publication_info: Proceedings of the 14th International Symposium on Mixed and Augmented Reality (ISMAR2015) Poster
  - doi: —
  - raw_text: Akira Saito, Megumi Nakao, Yuki Uranishi and Tetsuya Matsuda, “Deformation Estimation of Elastic Bodies Using Multiple Silhouette Images for Endoscopic Surgery”, Proceedings of the 14th International Symposium on Mixed and Augmented Reality, Poster, Fukuoka, Japan (2015.9)

- **Overlayable and Rotation-free Transmissive Circular Color Marker for Augmented Reality** (`site:id=114`)
  - category: International Conference Proceedings
  - authors: Asahi Suzuki, Yoshitsugu Manabe, Noriko Yata, Yuki Uranishi
  - date: 2012-05
  - publication_info: IS&T’s 6th European Conference on Colour in Graphics, Imaging (CGIV2012)
  - doi: —
  - raw_text: Asahi Suzuki, Yoshitsugu Manabe, Noriko Yata and Yuki Uranishi, “Overlayable and Rotation-free Transmissive Circular Color Marker for Augmented Reality”, IS&T’s 6th European Conference on Colour in Graphics, Imaging (CGIV 2012), pp.115-120, Amsterdam, the Netherlands (2012.5)

### Invited Talks and Tutorials (9)

- **明日から使える！研究効率化ツール入門** (`site:id=315`)
  - category: Invited Talks and Tutorials
  - authors: 浦西友樹, 松井勇佑, 米谷竜
  - date: 2026-03
  - publication_info: 第18回データ工学と情報マネジメントに関するフォーラム(DEIM2026) チュートリアル
  - doi: —
  - raw_text: 浦西友樹, 松井勇佑, 米谷竜, "明日から使える！研究効率化ツール入門", 第18回データ工学と情報マネジメントに関するフォーラム(DEIM2026) チュートリアル (2026.3)

- **大阪大学における教学DX** (`site:id=48`)
  - category: Invited Talks and Tutorials
  - authors: 浦西友樹
  - date: 2025-10
  - publication_info: 九州大学マス・フォア・インダストリ研究所「xR技術を活用した教育手法の確立と教育DX化」
  - doi: —
  - raw_text: 浦西友樹, "大阪大学における教学DX", 九州大学マス・フォア・インダストリ研究所「xR技術を活用した教育手法の確立と教育DX化」 (2025.10)

- **CursorとOverleafで卒論を英文論文化したり申請書を書いたりするのを楽にしよう** (`site:id=49`)
  - category: Invited Talks and Tutorials
  - authors: 浦西友樹
  - date: 2025-07
  - publication_info: MVA2025サテライト特別チュートリアル「大学・企業研究所PIのためのAI活用入門」
  - doi: —
  - raw_text: 浦西友樹, "CursorとOverleafで卒論を英文論文化したり申請書を書いたりするのを楽にしよう", MVA2025サテライト特別チュートリアル「大学・企業研究所PIのためのAI活用入門」 (2025.7)

- **大阪大学における教育へのICT活用 - 情報社会基礎・情報科学基礎の事例紹介** (`site:id=51`)
  - category: Invited Talks and Tutorials
  - authors: 浦西友樹, 白井詩沙香
  - date: 2024-09
  - publication_info: 神戸大学保健 FD研修『教育へのICT活用』
  - doi: —
  - raw_text: 浦西友樹, 白井詩沙香, "大阪大学における教育へのICT活用 - 情報社会基礎・情報科学基礎の事例紹介", 神戸大学保健 FD研修『教育へのICT活用』 (2024.9)

- **XRインタフェースと教育・スポーツへの応用** (`site:id=50`)
  - category: Invited Talks and Tutorials
  - authors: 浦西友樹
  - date: 2024-09
  - publication_info: 日本学術会議公開シンポジウム「農業デジタルツインの現状と展望」
  - doi: —
  - raw_text: 浦西友樹, "XRインタフェースと教育・スポーツへの応用", 日本学術会議公開シンポジウム「農業デジタルツインの現状と展望」 (2024.9)

- **大阪大学におけるブレンデッド教育の実例** (`site:id=52`)
  - category: Invited Talks and Tutorials
  - authors: 浦西友樹
  - date: 2022-03
  - publication_info: 龍谷大学先端理工学部FD報告会
  - doi: —
  - raw_text: 浦西友樹, "大阪大学におけるブレンデッド教育の実例", 龍谷大学先端理工学部FD報告会 (2022.3)

- **オープンソース画像処理ライブラリOpenCV：様々な環境での "Hello World"** (`site:id=53`)
  - category: Invited Talks and Tutorials
  - authors: 浦西友樹
  - date: 2019-05
  - publication_info: 第63回システム制御情報学会研究発表講演会 チュートリアル講演
  - doi: —
  - raw_text: 浦西友樹, "オープンソース画像処理ライブラリOpenCV：様々な環境での “Hello World”", 第63回システム制御情報学会研究発表講演会 チュートリアル講演 (2019.5)

- **VR/ARが医療にもたらす未来** (`site:id=54`)
  - category: Invited Talks and Tutorials
  - authors: 浦西友樹
  - date: 2017-09
  - publication_info: 第35回兵庫医療情報研究会
  - doi: —
  - raw_text: 浦西友樹, "VR/ARが医療にもたらす未来", 第35回兵庫医療情報研究会 (2017.9)

- **OpenCV 3.0 - コンピュータビジョンを簡単化するライブラリ** (`site:id=55`)
  - category: Invited Talks and Tutorials
  - authors: 浦西友樹
  - date: 2016-03
  - publication_info: 電子情報通信学会総合大会2016 企画セッション 「パターン認識・メディア理解」必須ソフトウェアライブラリ 手とり足とりガイド
  - doi: —
  - raw_text: 浦西友樹, "OpenCV 3.0 - コンピュータビジョンを簡単化するライブラリ", 電子情報通信学会総合大会2016 企画セッション 「パターン認識・メディア理解」必須ソフトウェアライブラリ 手とり足とりガイド, DT-1 (2016.3)

### Journal Papers (4)

- **TransPortal: A Portable Portal-Based Locomotion Technique** (`site:id=302`)
  - category: Journal Papers
  - authors: Daichi Hirobe, Shizuka Shirai, Jason Orlosky, Masato Kobayashi, Yuki Uranishi and Haruo Takemura
  - date: 2026-06
  - publication_info: IEEE Transactions on Visualization and Computer Graphics
  - doi: 10.1109/tvcg.2026.3702821
  - raw_text: Daichi Hirobe, Shizuka Shirai, Jason Orlosky, Masato Kobayashi, Yuki Uranishi and Haruo Takemura, "TransPortal: A Portable Portal-Based Locomotion Technique", IEEE Transactions on Visualization and Computer Graphics, pp.1-13 (2026.6) DOI: 10.1109/TVCG.2026.3702821

- **大阪大学における一般情報教育の変遷と今後の展望** (`site:id=9`)
  - category: Journal Papers
  - authors: 白井詩沙香, 松浦敏雄, 中西通雄, 竹村治雄, 清川清, 長瀧寛之, 浦西友樹
  - date: 2025-11
  - publication_info: 学術情報処理研究
  - doi: 10.24669/jacn.29.1_0043
  - raw_text: 白井詩沙香, 松浦敏雄, 中西通雄, 竹村治雄, 清川清, 長瀧寛之, 浦西友樹, "大阪大学における一般情報教育の変遷と今後の展望", 学術情報処理研究, Vol.25, No.1, pp.81-88 (2025.11) DOI: 10.24669/jacn.29.1_0043

- **A Modular Execution Architecture for Robust Multi-Robot Planning and Acting in Trans-Media Environments** (`site:id=10`)
  - category: Journal Papers
  - authors: Virgile De La Rochefoucauld, Photchara Ratsamee, Simon Lacroix, Félix Ingrand, Yuki Uranishi
  - date: 2025-10
  - publication_info: IEEE Access
  - doi: 10.1109/access.2025.3625646
  - raw_text: Virgile De La Rochefoucauld, Photchara Ratsamee, Simon Lacroix, Félix Ingrand and Yuki Uranishi, "A Modular Execution Architecture for Robust Multi-Robot Planning and Acting in Trans-Media Environments", IEEE Access, V ol.13, pp.186208-186230 (2025.10) DOI: 10.1109/ACCESS.2025.3625646

- **ホールド難度と配置を考慮したボルダリング課題の自動難度推定** (`site:id=21`)
  - category: Journal Papers
  - authors: 大西和歩, 浦西友樹, 劉暢, Photchara Ratsamee, 東田学, 山本豪志朗, 竹村治雄
  - date: 2022-12
  - publication_info: 日本バーチャルリアリティ学会論文誌
  - doi: 10.18974/tvrsj.27.4_331
  - raw_text: 大西和歩, 浦西友樹, 劉暢, Photchara Ratsamee, 東田学, 山本豪志朗, 竹村治雄, "ホールド難度と配置を考慮したボルダリング課題の自動難度推定", 日本バーチャルリアリティ学会論文誌, Vol.27, No.4, pp.331-340 (2022.12) DOI: 10.18974/tvrsj.27.4_331

### Misc. (10)

- **書評: OpenCVとPythonによる機械学習プログラミング** (`site:id=283`)
  - category: Misc.
  - authors: 浦西友樹
  - date: 2022-03
  - publication_info: 日本バーチャルリアリティ学会誌
  - doi: —
  - raw_text: 浦西友樹, "書評: OpenCVとPythonによる機械学習プログラミング", 日本バーチャルリアリティ学会誌, Vol.27, No.1, pp.41-42 (2022.3)

- **研究室運営に関するアンケート「我々は如何にこの難局を乗り越えようとしているのか」** (`site:id=284`)
  - category: Misc.
  - authors: 浦西友樹
  - date: 2021-03
  - publication_info: 日本バーチャルリアリティ学会誌
  - doi: —
  - raw_text: 浦西友樹, "研究室運営に関するアンケート「我々は如何にこの難局を乗り越えようとしているのか", 日本バーチャルリアリティ学会誌, Vol.26, No.1, pp. 6-9 (2021.3)

- **令和元年は今度こそHMD元年となるか?** (`site:id=285`)
  - category: Misc.
  - authors: 浦西友樹
  - date: 2019-09
  - publication_info: 日本バーチャルリアリティ学会誌
  - doi: —
  - raw_text: 浦西友樹, "令和元年は今度こそHMD元年となるか?", 日本バーチャルリアリティ学会誌, Vol.24, No.3, p.6 (2019.9)

- **コンピュータビジョンライブラリーOpenCV3.0** (`site:id=286`)
  - category: Misc.
  - authors: 浦西友樹
  - date: 2018-09
  - publication_info: 映像情報メディア学会誌
  - doi: —
  - raw_text: 浦西友樹, "コンピュータビジョンライブラリーOpenCV3.0", 映像情報メディア学会誌, Vol.72, No.5, pp.736-739 (2018.9)

- **MIRU2017若手プログラム実施報告** (`site:id=287`)
  - category: Misc.
  - authors: 浦西友樹, 五十川麻理子, 井下智加, 牛久祥孝, 大倉史生, 川西康友, 上瀧剛
  - date: 2018-05
  - publication_info: 情報処理学会研究報告: コンピュータビジョンとイメージメディア
  - doi: —
  - raw_text: 浦西友樹, 五十川麻理子, 井下智加, 牛久祥孝, 大倉史生, 川西康友, 上瀧剛, "MIRU2017若手プログラム実施報告", 情報処理学会研究報告: コンピュータビジョンとイメージメディア, Vol.2018-CVIM-212, No.40, pp.1-7, 兵庫 (2018.5)

- **CVPR2017見聞記** (`site:id=288`)
  - category: Misc.
  - authors: 浦西友樹, 井手口裕太
  - date: 2018-01
  - publication_info: 映像情報メディア学会誌
  - doi: —
  - raw_text: 浦西友樹, 井手口裕太, "CVPR2017見聞記", 映像情報メディア学会誌, Vol.72, No.1, pp.69-73 (2018.1)

- **CVPR2016参加報告** (`site:id=290`)
  - category: Misc.
  - authors: 浦西友樹
  - date: 2017-01
  - publication_info: 映像情報メディア学会誌
  - doi: —
  - raw_text: 浦西友樹, "CVPR2016参加報告", 映像情報メディア学会誌, Vol.71, No.1, pp.46-48 (2017.1)

- **MIRU2016若手プログラム実施概要と次回の企画紹介** (`site:id=289`)
  - category: Misc.
  - authors: 舩冨卓哉, 石井雅人, 井上中順, 金崎朝子, 高橋康輔, 道満恵介, 吉岡隆宏, 浦西友樹
  - date: 2017-01
  - publication_info: 電子情報通信学会 情報・システムソサイエティ誌
  - doi: —
  - raw_text: 舩冨卓哉, 石井雅人, 井上中順, 金崎朝子, 高橋康輔, 道満恵介, 吉岡隆宏, 浦西友樹, "MIRU2016若手プログラム実施概要と次回の企画紹介", 電子情報通信学会 情報・システムソサイエティ誌, Vol.21, No.4, pp.16-22 (2017)

- **スーパーサイエンスハイスクール生徒研究発表会に参加して** (`site:id=293`)
  - category: Misc.
  - authors: 浦西友樹
  - date: 2016-03
  - publication_info: システム/制御/情報
  - doi: —
  - raw_text: 浦西友樹, "スーパーサイエンスハイスクール生徒研究発表会に参加して", システム/制御/情報, Vol.60, No.3, p.128 (2016.3)

- **MIRU2014若手プログラム実施報告と次回の企画紹介** (`site:id=292`)
  - category: Misc.
  - authors: 島田敬士, 浦西友樹, 上瀧剛, 柴田剛志, 道満恵介, 豊浦正広, 柳川由紀子
  - date: 2016-01
  - publication_info: 電子情報通信学会 情報・システムソサイエティ誌
  - doi: —
  - raw_text: 島田敬士, 浦西友樹, 上瀧剛, 柴田剛志, 道満恵介, 豊浦正広, 柳川由紀子, "MIRU2014若手プログラム実施報告と次回の企画紹介", 電子情報通信学会 情報・システムソサイエティ誌, Vol.20, No.4, pp.21-24 (2016)

## マッチしたが差分あり（127 件）

### MR-UBi: Mixed Reality-Based Underwater Robot Arm Teleoperation System with Reaction Torque Indicator via Bilateral Control

- site `id=296` / researchmap `published_papers:54067962`

- authors: RM `Kohei Nishi, Masato Kobayashi, Yuki Uranishi` vs site `Kohei Nishi, Masato Kobayashi and Yuki Uranishi`
- date: RM `2026` vs site `2026-03`
- publication_info: RM `IEEE Access` vs site `IEEE Access (Early Access)`

### HybridSphere: Enhancing Hybrid Meetings with Avatar-Based VR Environments

- site `id=297` / researchmap `published_papers:54067961`

- authors: RM `Koji Momota, Shizuka Shirai, Masato Kobayashi, Naoya Chiba, Photchara Ratsamee, Kiyoshi Kiyokawa, Yuki Uranishi` vs site `Koji Momota, Shizuka Shirai, Masato Kobayashi, Naoya Chiba, Photchara Ratsamee, Kiyoshi Kiyokawa and Yuki Uranishi`
- date: RM `2026` vs site `2026-03`
- publication_info: RM `IEEE Transactions on Visualization and Computer Graphics` vs site `IEEE Transactions on Visualization and Computer Graphics: Special Issue on IEEE Virtual Reality and 3D User Interfaces 2026`

### Real-Time Feedback System for Body Tilt in Archery Shooting

- site `id=59` / researchmap `published_papers:52773386`

- publication_info: RM `2025 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct)` vs site `Proceedings of the 24th International Symposium on Mixed and Augmented Reality (ISMAR2025)`

### Which Tile Should I Discard?: Supporting Beginners in Mahjong by Presenting Recommended Discards in Mixed Reality

- site `id=60` / researchmap `published_papers:52773383`

- publication_info: RM `2025 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct)` vs site `Proceedings of the 24th International Symposium on Mixed and Augmented Reality (ISMAR2025)`

### Exploring Visual Augmentation for Soccer Kicking Posture Instruction

- site `id=11` / researchmap `published_papers:52654182`

- date: RM `2025` vs site `2025-10`

### Bi-LAT: Bilateral Control-Based Imitation Learning Via Natural Language and Action Chunking with Transformers

- site `id=61` / researchmap `published_papers:52798410`

- authors: RM `Takumi Kobayashi, Masato Kobayashi, Thanpimon Buamanee, Yuki Uranishi` vs site `Takumi Kobayashi, Masato Kobayashi, Thampimon Buamanee, Yuki Uranishi`
- publication_info: RM `2025 34th IEEE International Conference on Robot and Human Interactive Communication (RO-MAN)` vs site `Proceedings of the IEEE International Conference on Robot & Human Interactive Communication (RO-MAN2025)`

### MRHaD: Mixed Reality-based Hand-Drawn Map Editing Interface for Mobile Robot Navigation

- site `id=62` / researchmap `published_papers:52626164`

- category: RM `Journal Papers` vs site `International Conference Proceedings`
- date: RM `2025-04` vs site `2025-08`
- publication_info: RM `CoRR` vs site `Proceedings of the IEEE International Conference on Robot & Human Interactive Communication (RO-MAN2025)`

### User-Centric Locomotion Techniques for Virtual Reality Games: A Survey of User Needs and Issues

- site `id=13` / researchmap `published_papers:48468045`

- date: RM `2024` vs site `2025-06`

### 複合現実技術を用いた推奨打牌情報の提示による麻雀支援システムの提案

- site `id=160` / researchmap `misc:52626246`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- date: RM `2025` vs site `2025-06`
- publication_info: RM `情報処理学会研究報告(Web)` vs site `情報処理学会第213回ヒューマンコンピュータインタラクション研究会`

### アーチェリー行射における身体傾斜情報の即時提示システムの提案

- site `id=159` / researchmap `misc:52626244`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- date: RM `2025` vs site `2025-06`
- publication_info: RM `情報処理学会研究報告(Web)` vs site `情報処理学会第213回ヒューマンコンピュータインタラクション研究会`

### DABI: Evaluation of Data Augmentation Methods Using Downsampling in Bilateral Control-Based Imitation Learning with Images

- site `id=308` / researchmap `published_papers:52596251`

- authors: RM `Masato Kobayashi, Thanpimon Buamanee, Yuki Uranishi` vs site `Masato Kobayashi*, Thanpimon Buamanee*, Yuki Uranishi`
- publication_info: RM `2025 IEEE International Conference on Robotics and Automation (ICRA)` vs site `IEEE International Conference on Robotics and Automation (ICRA2025)`

### Climbing Motion Generation for Humanoid Agents through Deep Reinforcement Learning with Optimization Constraints

- site `id=63` / researchmap `published_papers:52404377`

- authors: RM `Kazuho Onishi, Yuki Uranishi, Masato Kobayashi, Chang Liu, Goshiro Yamamoto, Ratsamee Photchara` vs site `Kazuho Onishi, Yuki Uranishi, Masato Kobayashi, Chang Liu, Goshiro Yamamoto, Photchara Ratsamee`
- date: RM `2025-02` vs site `2025-03`
- publication_info: RM `2025 IEEE International Conference on Mechatronics (ICM)` vs site `Proceedings of the 2025 IEEE International Conference on Mechatronics (ICM’25)`

### ILBiT: Imitation Learning for Robot Using Position and Torque Information based on Bilateral Control with Transformer

- site `id=14` / researchmap `published_papers:48468035`

- date: RM `2024` vs site `2025-02`

### Generating Double Dyno Motion for Humanoid Agents in Simulated Bouldering Environment through Deep Reinforcement Learning

- site `id=65` / researchmap `published_papers:49296265`

- authors: RM `Kazuho Onishi, Yuki Uranishi, Masato Kobayashi, Chang Liu, Goshiro Yamamoto, Ratsamee Photchara` vs site `Kazuho Onishi, Yuki Uranishi, Masato Kobayashi, Chang Liu, Goshiro Yamamoto, Photchara Ratsamee`
- publication_info: RM `2025 IEEE International Conference on Artificial Intelligence and eXtended and Virtual Reality (AIxVR)` vs site `Proceedings of the IEEE the 7th IEEE International Conference on Artificial Intelligence & eXtended and Virtual Reality (AIxVR) Workshop on AI and AR/VR for Exergaming (AIVR4Exergame)`

### Cloud Computing Challenges and Needs in Higher Education Institutions in Post-COVID-19 Times: A Case of a Japanese Survey

- site `id=15` / researchmap `published_papers:48512897`

- date: RM `2024` vs site `2024-11`
- publication_info: RM `IEEE Access` vs site `IEEE Access (Early Access)`

### Enhancing Learning Dynamics: Integrating Interactive Learning Environments and ChatGPT for Computer Networking Lessons

- site `id=67` / researchmap `published_papers:52667696`

- date: RM `2024` vs site `2024-09`
- publication_info: RM `KES` vs site `Proceedings of the 28th International Conference on Knowledge-Based and Intelligent Information & Engineering Systems (KES’24)`

### Identifying Disaster Regions in Images Through Attention Shifting with a Retarget Network

- site `id=16` / researchmap `published_papers:47462109`

- date: RM `2024` vs site `2024-08`
- publication_info: RM `IEEE Access` vs site `IEEE Access (Early Access)`

### Bi-ACT: Bilateral Control-Based Imitation Learning via Action Chunking with Transformer

- site `id=69` / researchmap `published_papers:47559720`

- authors: RM `Thanpimon Buamanee, Masato Kobayashi, Yuki Uranishi, Haruo Takemura` vs site `Thanpimon Buamanee*, Masato Kobayashi*, Yuki Uranishi, Haruo Takemura`
- date: RM `2024-07` vs site `2024-05`
- publication_info: RM `2024 IEEE International Conference on Advanced Intelligent Mechatronics (AIM)` vs site `ICRA Workshop: A Future Roadmap for Sensorimotor Skill Learning for Robot Manipulation`

### Real-time Alert of Excessive Force Based on Forearm Muscle Activity for Wall Climbing

- site `id=71` / researchmap `published_papers:46220383`

- authors: RM `Toru Kowada, Photchara Ratsamee, Goshiro Yamamoto, Chang Liu, Yuki Uranishi` vs site `Toru Kowada, Yuki Uranishi, Chang Liu, Goshiro Yamamoto, Photchara Ratsamee`
- publication_info: RM `2023 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct)` vs site `Proceedings of the 22nd IEEE International Symposium on Mixed and Augmented Reality (ISMAR2023) Poster`

### Mitigation of VR Sickness during Locomotion with a Motion-Based Dynamic Vision Modulator

- site `id=17` / researchmap `published_papers:49662155`

- authors: RM `Zhao, G., Orlosky, J., Feiner, S., Ratsamee, P., Uranishi, Y.` vs site `Guanghan Zhao, Jason Orlosky, Steven Feiner, Photchara Ratsamee, Yuki Uranishi`
- date: RM `2022` vs site `2023-10`

### Panoptic-Level Image-to-Image Translation for Object Recognition and Visual Odometry Enhancement

- site `id=19` / researchmap `published_papers:42924456`

- date: RM `2023` vs site `2023-06`
- publication_info: RM `IEEE Transactions on Circuits and Systems for Video Technology` vs site `IEEE Transactions on Circuits and Systems for Video Technology (Early Access)`

### Difficulty Estimation of Educational Comics Using Gaze Features

- site `id=20` / researchmap `published_papers:42193347`

- publication_info: RM `IEICE Transactions on Information and Systems` vs site `The IEICE Transactions on Information and Systems`

### Characteristics of Background Color Shifts Caused by Optical See-Through Head-Mounted Displays

- site `id=74` / researchmap `published_papers:43332046`

- publication_info: RM `ICAT-EGVE 2022 - International Conference on Artificial Reality and Telexistence and Eurographics Symposium on Virtual Environments` vs site `The 32nd International Conference on Artificial Reality and Telexistence and Eurographics Symposium on Virtual Environments (ICAT-EGVE2022)`

### Evaluation of User Interfaces for Three-Dimensional Locomotion in Virtual Reality

- site `id=73` / researchmap `presentations:40863384`

- publication_info: RM `Symposium on Spatial User Interaction` vs site `ACM Spatial User Interaction 2022 (SUI2022)`

### Thermal-to-Color Image Translation for Enhancing Visual Odometry of Thermal Vision

- site `id=75` / researchmap `published_papers:43468935`

- publication_info: RM `2022 IEEE International Symposium on Safety, Security, and Rescue Robotics (SSRR)` vs site `The 2022 IEEE International Symposium on Safety, Security, and Rescue Robotics (SSRR2022)`

### Evaluation of User Interfaces for Three-Dimensional Locomotion in Virtual Reality

- site `id=77` / researchmap `published_papers:43332045`

- date: RM `2022-12` vs site `2022-10`
- publication_info: RM `Symposium on Spatial User Interaction` vs site `Proceedings of the 21st IEEE International Symposium on Mixed and Augmented Reality (ISMAR2021) Poster`

### Objective Measurements of Background Color Shifts Caused by Optical See-Through Head-Mounted Displays

- site `id=76` / researchmap `published_papers:43468936`

- publication_info: RM `2022 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct)` vs site `Proceedings of the 21st IEEE International Symposium on Mixed and Augmented Reality (ISMAR2021) Poster`

### Real-to-Synthetic Feature Transform for Illumination Invariant Camera Localization

- site `id=22` / researchmap `published_papers:49662152`

- authors: RM `Shoman, S., Mashita, T., Plopski, A., Ratsamee, P., Uranishi, Y.` vs site `Sota Shoman, Tomohiro Mashita, Alexander Plopski, Photchara Ratsamee, Yuki Uranishi`
- date: RM `2022` vs site `2022-01`

### A Japanese Character Flick-Input Interface for Entering Text in VR

- site `id=78` / researchmap `published_papers:43332044`

- publication_info: RM `2021 IEEE International Symposium on Mixed and Augmented Reality Adjunct (ISMAR-Adjunct)` vs site `Proceedings of the 20th IEEE International Symposium on Mixed and Augmented Reality (ISMAR2021)`

### UAV Target-Selection: 3D Pointing Interface System for Large-Scale Environment

- site `id=79` / researchmap `published_papers:52667695`

- category: RM `RM:published_papers` vs site `International Conference Proceedings`
- authors: RM `Haruo Takemura, Manabu Higashida, Yuki Uranishi, Anna C. S. Medeiros, Photchara Ratsamee, Jason Orlosky` vs site `Anna C. S. Medeiros, Photchara Ratsamee, Jason Orlosky, Yuki Uranishi, Manabu Higashida, Haruo Takemura`
- date: RM `2021-05` vs site `2021-06`
- publication_info: RM `2021 IEEE International Conference on Robotics and Automation (ICRA)` vs site `Proceedings of the 2021 International Conference on Robotics and Automation (ICRA2021)`

### Spherical Magnetic Joint for Inverted Locomotion of Multi-Legged Robot

- site `id=80` / researchmap `published_papers:52667687`

- category: RM `RM:published_papers` vs site `International Conference Proceedings`
- authors: RM `Yuki Uranishi, Haruo Takemura, Harn Sison, Manabu Higashida, Tomohiro Mashita, Photchara Ratsamee` vs site `Harn Sison, Photchara Ratsamee, Manabu Higashida, Tomohiro Mashita, Yuki Uranishi, Haruo Takemura`
- date: RM `2021-05` vs site `2021-06`
- publication_info: RM `2021 IEEE International Conference on Robotics and Automation (ICRA)` vs site `Proceedings of the 2021 International Conference on Robotics and Automation (ICRA2021)`

### 3D Pointing Gestures as Target Selection Tools: Guiding Monocular UAVs during Window Selection in an Outdoor Environment

- site `id=23` / researchmap `published_papers:34790033`

- date: RM `2021-12` vs site `2021-04`

### VR技術を用いたパラグライダ操縦技能獲得システムの設計と評価

- site `id=177` / researchmap `misc:34790130`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- date: RM `2021` vs site `2021-01`
- publication_info: RM `情報処理学会研究報告(Web)` vs site `日本バーチャルリアリティ学会 複合現実感研究会`

### スポーツクライミングにおけるOST-HMDの利用と効果の検証

- site `id=176` / researchmap `misc:34790128`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- date: RM `2021` vs site `2021-01`
- publication_info: RM `情報処理学会研究報告(Web)` vs site `日本バーチャルリアリティ学会 複合現実感研究会`

### Rainbow Learner: Lighting Environment Estimation from a Structural-Color Based AR Marker

- site `id=81` / researchmap `published_papers:43332043`

- publication_info: RM `2020 IEEE International Conference on Artificial Intelligence and Virtual Reality (AIVR)` vs site `Proceedings of the IEEE 3rd International Conference on Artificial Intelligence & Virtual Reality (AIVR2020)`

### 大阪大学におけるメディア授業実施に関する全学的な支援体制の整備と新入生支援の取り組み

- site `id=24` / researchmap `published_papers:34384334`

- category: RM `RM:published_papers` vs site `Journal Papers`
- date: RM `2020` vs site `2020-10`

### Human-Drone Interaction: Using Pointing Gesture to Define a Target Object

- site `id=82` / researchmap `published_papers:47101418`

- date: RM `2020` vs site `2020-07`
- publication_info: RM `Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)` vs site `Proceedings of HCI International 2020, Part 2`

### MomentViz: An Interactive 3D Vision Augmentation Framework for Rapid Motion

- site `id=25` / researchmap `published_papers:29750379`

- authors: RM `Tao Tao, Ratsamee Photchara, Orlosky Jason, Uranishi Yuki, Takemura Haruo` vs site `Tao Tao, Photchara Ratsamee, Jason Orlosky, Yuki Uranishi, Haruo Takemura`
- date: RM `2020` vs site `2020-06`
- publication_info: RM `日本バーチャルリアリティ学会論文誌` vs site `Transactions of the Virtual Reality Society of Japan`

### Detecting Learner Drowsiness Based on Facial Expressions and Head Movements in Online Courses

- site `id=84` / researchmap `published_papers:43307509`

- publication_info: RM `Proceedings of the 25th International Conference on Intelligent User Interfaces Companion` vs site `Proceedings of the International Conference on Intelligent User Interfaces Companion (IUI2020)`

### Optimal Arrangement of Surveillance Cameras Using Space Division and a Genetic Algorithm

- site `id=83` / researchmap `published_papers:27921830`

- authors: RM `Yuya Komabashiri, Tomohiro Mashita, Ratsamee Photchara, Yuki Uranishi, Masahide Koike, Kiyoyasu Maruyama` vs site `Yuya Komabashiri, Tomohiro Mashita, Photchara Ratsamee, Yuki Uranishi, Masahide Koike, Kiyoyasu Maruyama`
- publication_info: RM `International Conference on Intelligent User Interfaces Companion(IUI2020)` vs site `Proceedings of the International Conference on Intelligent User Interfaces Companion (IUI2020)`

### The Effect of the Presence of an Embodied Agent in an AR Guiding System

- site `id=27` / researchmap `published_papers:27921821`

- authors: RM `Techasarntikul Nattaon, Ratsamee Photchara, Orlosky Jason, Mashita Tomohiro, Uranishi Yuki, Kiyokawa Kiyoshi, Takemura Haruo` vs site `Nattaon Techasarntikul, Photchara Ratsamee, Jason Orlosky, Tomohiro Mashita, Yuki Uranishi, Kiyoshi Kiyokawa, Haruo Takemura`
- date: RM `2020` vs site `2020-03`
- publication_info: RM `日本バーチャルリアリティ学会論文誌` vs site `Transactions of the Virtual Reality Society of Japan`

### Real-time Guidance and Visualization of Optimized Packing Solutions

- site `id=26` / researchmap `published_papers:27921817`

- date: RM `2020` vs site `2020-03`

### 顔表情および頭部動作に基づくeラーニング時の覚醒度推定

- site `id=180` / researchmap `misc:37841135`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- date: RM `2020-02` vs site `2020-03`

### 3D Gesture Interface: Japan-Brazil Perceptions

- site `id=85` / researchmap `published_papers:27921828`

- publication_info: RM `1st International Conference on Human-computer Interaction` vs site `Proceedings of the 21st International Conference on Human-computer Interaction (HCII 2019): Cross-Cultural Design. Methods, Tools and User Experience`

### 写実的拡張現実環境に向けた構造色パターンからの学習ベース光源分布推定

- site `id=142` / researchmap `presentations:40461088`

- authors: RM `浦西 友樹, 伊藤 澄美, 間下 以大, ラサミー ポチャラ, 竹村 治雄` vs site `浦西友樹*, 伊藤澄美*, 間下以大, ラサミーポチャラ, 竹村治雄`
- publication_info: RM `第22回画像の認識・理解シンポジウム Extended Abstract` vs site `第22回画像の認識・理解シンポジウム Extended Abstract [Short Oral]`

### 機械学習に基づくEpipolar Plane Imagesからの透明物体の屈折率推定

- site `id=186` / researchmap `published_papers:21725804`

- authors: RM `浦西 友樹, ホールドクロフト トレバー, 間下 以大, ラサミー ポチャラ, 竹村 治雄` vs site `浦西友樹, Holdcroft Trevor, 間下以大, ラサミー ポチャラ, 竹村治雄`

### 拡張現実感におけるRGBカメラ画像に整合した陰影付け

- site `id=185` / researchmap `presentations:16639240`

- authors: RM `小川敬也, 間下以大, 浦西友樹, RATSAMEE Photchara, 竹村治雄` vs site `小川敬也, 間下以大, 浦西友樹, ラサミー ポチャラ, 竹村治雄`
- publication_info: RM `情報処理学会研究報告(Web)` vs site `情報処理学会研究報告`

### 天井裏における偏光情報を用いた特徴点対応の評価

- site `id=184` / researchmap `presentations:16639239`

- authors: RM `小川和樹, 間下以大, 浦西友樹, PHOTCHARA Ratsamee, 竹村治雄` vs site `小川和樹, 間下以大, 浦西友樹, ラサミー ポチャラ, 竹村治雄`
- publication_info: RM `情報処理学会研究報告(Web)` vs site `情報処理学会研究報告`

### A Comparison of Adaptive View Techniques for Exploratory 3D Drone Teleoperation

- site `id=28` / researchmap `published_papers:5419339`

- authors: RM `John Thomason, Photchara Ratsamee, Jason Orlosky, Kiyoshi Kiyokawa, Tomohiro Mashita, Yuki Uranishi, Haruo Takemura` vs site `John Thomason, Photchara Ratsamee, Kiyoshi Kiyokawa, Jason Orlosky, Tomohiro Mashita, Yuki Uranishi, Haruo Takemura`
- publication_info: RM `ACM Transactions on Interactive Intelligent Systems` vs site `ACM Transactions on Interactive Intelligent Systems (TiiS)`

### Evaluation of Pointing Interfaces with an AR Agent for Multi-section Information Guidance

- site `id=86` / researchmap `published_papers:27921825`

- date: RM `2019` vs site `2019-03`
- publication_info: RM `IEEE VR` vs site `Proceedings of the IEEE Virtual Reality 2019 (VR2019)`

### Illumination Invariant Camera Localization Using Synthetic Images

- site `id=87` / researchmap `published_papers:47074391`

- date: RM `2018-07` vs site `2018-10`
- publication_info: RM `Adjunct Proceedings - 2018 IEEE International Symposium on Mixed and Augmented Reality, ISMAR-Adjunct 2018` vs site `Proceedings of the 17th IEEE International Symposium on Mixed and Augmented Reality (ISMAR2018)`

### OpenCVとPythonによる機械学習プログラミング

- site `id=2` / researchmap `books_etc:43160544`

- authors: RM `Beyeler, Michael, 池田, 聖, 浦西, 友樹, 中島, 悠太, 森, 尚平, 山添, 大丈, 山本, 豪志朗` vs site `Michael Beyeler, 池田聖, 浦西友樹, 中島悠太, 森尚平, 山添大丈, 山本豪志朗`

### 携帯端末による屋内構造の計測と直方体モデルのフィッティング

- site `id=192` / researchmap `presentations:21725798`

- authors: RM `土田 知実, 間下 以大, 浦西 友樹, Ratsamee Photchara, 竹村 治雄` vs site `土田知実, 間下以大, 浦西友樹, Photchara Ratsamee, 竹村治雄`

### VisMerge: Light Adaptive Vision Augmentation via Spectral and Temporal Fusion of Non-visible Light

- site `id=91` / researchmap `published_papers:21725790`

- publication_info: RM `2017 IEEE International Symposium on Mixed and Augmented Reality (ISMAR)` vs site `Proceedings of the 16th IEEE International Symposium on Mixed and Augmented Reality (ISMAR2017)`

### シミュレーションと自己符号化器を用いた光源変化に頑健なカメラ位置姿勢推定

- site `id=143` / researchmap `published_papers:21725786`

- date: RM `2017-09` vs site `2017-08`

### 深層学習による集光模様の実時間生成

- site `id=197` / researchmap `published_papers:21725777`

- date: RM `2017-05` vs site `2017-08`
- publication_info: RM `情報処理学会研究報告, Vol. 2017` vs site `第20回画像の認識・理解シンポジウム Extended Abstract`

### Light Field Convergency: Implicit Photometric Consistency on Transparent Surface

- site `id=93` / researchmap `published_papers:21725783`

- publication_info: RM `2017 IEEE Conference on Computer Vision and Pattern Recognition Workshops` vs site `Proceedings of the 2nd Workshop on Light Fields for Computer Vision (LF4CV): IEEE Conference on Computer Vision and Pattern Recognition Workshop`

### Image Matching between Cameras for Vision Augmentation HMDs

- site `id=134` / researchmap `published_papers:21725782`

- category: RM `RM:published_papers` vs site `International Conference Proceedings`

### 対面協調作業に適した相互モーションキャプチャシステムの開発

- site `id=198` / researchmap `published_papers:21725780`

- publication_info: RM `映像情報メディア学会技術報告 = ITE technical report` vs site `第143回ヒューマンインタフェース学会研究会「人工現実感，エンタテイメント，メディアエクスペリエンスおよび一般」`

### 失敗を可視化する採血トレーナ

- site `id=30` / researchmap `published_papers:5370163`

- date: RM `2017` vs site `2017-06`

### 画像処理・機械学習プログラミング OpenCV3対応

- site `id=3` / researchmap `books_etc:43160546`

- authors: RM `浦西, 友樹, 青砥, 隆仁, 井村, 誠孝, 大倉, 史生, 金谷, 一朗, 小枝, 正直, 中島, 悠太, 藤本, 雄一郎 (工学), 山口, 明彦, 山本, 豪志朗` vs site `浦西友樹, 青砥隆仁, 井村誠孝, 大倉史生, 金谷一朗, 小枝正直, 中島悠太, 藤本雄一郎, 山口明彦, 山本豪志朗`
- publication_info: RM `マイナビ出版` vs site `マイナビ`

### 深層学習による集光模様の実時間生成

- site `id=199` / researchmap `published_papers:21725785`

- date: RM `2017-08` vs site `2017-05`
- publication_info: RM `情報処理学会研究報告(Web)` vs site `情報処理学会研究報告`

### 大域照明の内挿による光源操作可能なARシステム

- site `id=201` / researchmap `published_papers:21725779`

- publication_info: RM `情報処理学会研究報告, Vol. 2017` vs site `情報処理学会研究報告`

### 光源変化シミュレーションと深層学習による特徴量変換を用いたカメラ位置姿勢推定

- site `id=200` / researchmap `published_papers:21725778`

- publication_info: RM `情報処理学会研究報告, Vol. 2017` vs site `情報処理学会研究報告`

### Adaptive View Management for Drone Teleoperation in Complex 3D Structures

- site `id=94` / researchmap `published_papers:21725776`

- publication_info: RM `International Conference on Intelligent User Interfaces, Proceedings IUI` vs site `Proceedings of the 22nd International Conference on Intelligent User Interfaces (IUI2017)`

### Virtual Reality Forest: Real Measured Trees and Enhanced Experience

- site `id=95` / researchmap `published_papers:21725772`

- category: RM `Journal Papers` vs site `International Conference Proceedings`
- publication_info: RM `Proceedings of the EuroVR Conference 2016, Technical Session III, Athens, Greece` vs site `Proceedings of the EuroVR Conference 2016, Technical Session III`

### 光線収束性を用いた透明物体表面の五次元推定の高精度化

- site `id=203` / researchmap `misc:37658200`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- date: RM `2016` vs site `2016-11`
- publication_info: RM `情報処理学会研究報告(Web)` vs site `情報処理学会研究報告: コンピュータビジョンとイメージメディア`

### MRの未来を語る若手放談会（20周年記念特集 これからのVR）

- site `id=291` / researchmap `misc:37278444`

- publication_info: RM `日本バーチャルリアリティ学会誌 = Journal of the Virtual Reality Society of Japan` vs site `日本バーチャルリアリティ学会誌`

### Deformation Estimation of Elastic Bodies Using Multiple Silhouette Images for Supporting Endoscopic Surgery

- site `id=96` / researchmap `published_papers:21725767`

- category: RM `Journal Papers` vs site `International Conference Proceedings`
- publication_info: RM `Proceedings of 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC2016) Late Breaking Research Posters Paper, Orlando, FL, United States` vs site `Proceedings of 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC2016) Late Breaking Research Posters Paper`

### 3D Reconstruction of Cochlea Using Optical Coherence Tomography

- site `id=97` / researchmap `published_papers:21725768`

- authors: RM `Tuukka Karvonen, Yuki Uranishi, Tatsunori Sakamoto, Yosuke Tona, Kazuya Okamoto, Hiroshi Tamura, Tomohiro Kuroda` vs site `Tuukka Matias Karvonen, Yuki Uranishi, Tatsunori Sakamoto, Yosuke Tona, Kazuya Okamoto, Hiroshi Tamura, Tomohiro Kuroda`
- date: RM `2016` vs site `2016-08`
- publication_info: RM `2016 38TH ANNUAL INTERNATIONAL CONFERENCE OF THE IEEE ENGINEERING IN MEDICINE AND BIOLOGY SOCIETY (EMBC)` vs site `Proceedings of 38th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC2016)`

### 勤務表から抽出した制約条件を用いたナース・スケジューリングシステム

- site `id=207` / researchmap `published_papers:21725765`

- authors: RM `今中 健, 岡本 和也, 疋田 智子, 岩尾 友秀, 浦西 友樹, 田村 寛, 齋藤 永, 加藤 源太, 黒田 知宏` vs site `今中健, 岡本和也, 疋田智子, 岩尾友秀, 浦西友樹, 田村寛, 齊藤永, 加藤源太, 黒田知宏`
- publication_info: RM `システム制御情報学会研究発表講演会講演論文集` vs site `第60回システム制御情報学会研究発表講演会 論文集`

### 外来病棟における位置情報とオーダ情報を用いた患者待ち時間の分析

- site `id=206` / researchmap `published_papers:21725764`

- publication_info: RM `第60回システム制御情報学会研究発表講演会 論文集, 143-3, 京都` vs site `第60回システム制御情報学会研究発表講演会 論文集`

### Estimation of the Degree of Endolymphatic Hydrops Using Optical Coherence Tomography

- site `id=33` / researchmap `published_papers:5419298`

- authors: RM `Karvonen Tuukka, Uranishi Yuki, Sakamoto Tatsunori, Tona Yosuke, Okamoto Kazuya, Tamura Hiroshi, Kuroda Tomohiro` vs site `Tuukka Karvonen, Yuki Uranishi, Tatsunori Sakamoto, Yosuke Tona, Kazuya Okamoto, Hiroshi Tamura, Tomohiro Kuroda`
- date: RM `2016` vs site `2016-03`

### The Rainbow Marker: An AR Marker with Planar Light Probe based on Structural Color Pattern Matching

- site `id=98` / researchmap `misc:25757305`

- category: RM `Misc.` vs site `International Conference Proceedings`
- date: RM `2016` vs site `2016-03`
- publication_info: RM `2016 IEEE Virtual Reality, VR 2016, Greenville, SC, USA, March 19-23, 2016` vs site `Proceedings of the IEEE Virtual Reality 2016 (VR2016)`

### リスク想定学習のためのフィードバック情報を投影する採血シミュレータ

- site `id=209` / researchmap `misc:25165662`

- publication_info: RM `計測自動制御学会関西支部・システム制御情報学会 若手研究発表会予稿集` vs site `計測自動制御学会関西支部・システム制御情報学会若手研究発表会 講演論文集`

### 辺縁での光学的部分恒常性に基づく透明物体の表面形状推定

- site `id=210` / researchmap `misc:37658217`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- date: RM `2015` vs site `2015-11`
- publication_info: RM `情報処理学会研究報告(Web)` vs site `情報処理学会研究報告: コンピュータビジョンとイメージメディア`

### Haptic Interface with a Stylus for a Mobile Touch Panel

- site `id=35` / researchmap `published_papers:5419336`

- date: RM `2015` vs site `2015-10`

### Estimation of the Degree of Endolymphatic Hydrops Using Optical Coherence Tomography

- site `id=145` / researchmap `published_papers:21725762`

- category: RM `Journal Papers` vs site `Domestic Conference Proceedings`
- date: RM `2016-03` vs site `2015-09`
- publication_info: RM `Advanced Biomedical Engineering` vs site `生体医工学シンポジウム2015 講演予稿集`

### 視覚障がい者のための色にもとづく服飾選択支援システム

- site `id=146` / researchmap `published_papers:5419319`

- category: RM `Journal Papers` vs site `Domestic Conference Proceedings`
- authors: RM `三宅正夫, 眞鍋佳嗣, 浦西友樹, 井村誠孝, 黒田嘉宏, 大城理` vs site `三宅正夫, 眞鍋佳嗣, 浦西友樹, 吉元俊輔, 井村誠孝, 黒田嘉宏, 大城理`
- date: RM `2015-10` vs site `2015-09`
- publication_info: RM `生体医工学` vs site `生体医工学シンポジウム2015 講演予稿集`

### Segmentation of Cochlear Structure in Optical Coherence Tomography Images

- site `id=212` / researchmap `misc:25165741`

- authors: RM `Tuukka Karvonen, 浦西友樹, 坂本達則, 十名洋介, 岡本和也, 田村 寛, 黒田知宏` vs site `Tuukka Karvonen, Yuki Uranishi, Tatsunori Sakamoto, Yosuke Tona, Kazuya Okamoto, Hiroshi Tamura, Tomohiro Kuroda`
- publication_info: RM `日本VR医学会学術大会抄録集` vs site `第15回日本VR医学会学術大会 抄録集`

### 採血トレーニングのための穿刺位置に対する注射針の角度および深度推定

- site `id=211` / researchmap `misc:25165738`

- publication_info: RM `日本VR医学会学術大会抄録集` vs site `第15回日本VR医学会学術大会 抄録集`

### 光源方向推定のための構造色パターンマッチング

- site `id=213` / researchmap `misc:25756974`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- authors: RM `浦西 友樹, 井村 誠孝, 黒田 知宏` vs site `浦西友樹, 井村誠孝, 黒田知宏, 大城理`
- publication_info: RM `システム制御情報学会研究発表講演会講演論文集` vs site `第59回システム制御情報学会研究発表講演会 論文集`

### 注射トレーニングのための腕型シミュレータへの解剖学的構造の投影

- site `id=214` / researchmap `misc:25165651`

- publication_info: RM `第59回システム制御情報学会研究発表講演会講演論文集` vs site `第59回システム制御情報学会研究発表講演会 論文集`

### 視認性の高い投影のための色と形状に基づくシーンの評価

- site `id=216` / researchmap `misc:35290508`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- publication_info: RM `研究報告コンピュータビジョンとイメージメディア（CVIM）` vs site `電子情報通信学会技術 研究報告`

### Haptylus: Haptic Stylus for Interaction with Virtual Objects behind a Touch Screen

- site `id=101` / researchmap `published_papers:25241082`

- date: RM `2014` vs site `2014-12`
- publication_info: RM `SIGGRAPH Asia 2014 Emerging Technologies, Shenzhen, China, December 3-6, 2014` vs site `ACM SIGGRAPH Asia 2014 Emerging Technologies`

### タブレットPCと伸縮および振動可能なスタイラスを用いた力触覚提示

- site `id=217` / researchmap `misc:37658230`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- date: RM `2014` vs site `2014-11`
- publication_info: RM `電気関係学会関西連合大会講演論文集(CD-ROM)` vs site `電気関係学会関西支部連合大会 予稿集`

### Grid-pattern Indicating Interface for Ambient Assisted Living

- site `id=102` / researchmap `misc:25757307`

- category: RM `Misc.` vs site `International Conference Proceedings`
- authors: RM `Zeeshan Asghar, Goshiro Yamamoto, Yuki Uranishi, Christian Sandor, Tomohiro Kuroda, Petri Pulli, Hirokazu Kato` vs site `Goshiro Yamamoto, Zeeshan Asghar, Yuki Uranishi, Takafumi Taketomi, Christian Sandor, Tomohiro Kuroda, Petri Pulli, Hirokazu Kato`
- date: RM `2015-01` vs site `2014-09`
- publication_info: RM `Recent Advances on Using Virtual Reality Technologies for Rehabilitation` vs site `Proceedings of International Conference on Disability, Virtual Reality and Associated Technologies (ICDVRAT2014)`

### Reconstruction of Spatial Density of Smoke based on Light Field Consistency

- site `id=149` / researchmap `presentations:16639262`

- publication_info: RM `第17回画像の認識・理解シンポジウム Extended Abstract` vs site `第17回画像の認識・理解シンポジウム Extended Abstract [Poster]`

### Large Deformation with Haptic Interaction by Stepwise Rotation Update of Finite Element Model

- site `id=103` / researchmap `published_papers:21725758`

- authors: RM `Y. Kuroda, Y. Uranishi, M. Imura, O. Oshiro, H. Takemura` vs site `Yoshihiro Kuroda, Yuki Uranishi, Masataka Imura, Osamu Oshiro, Haruo Takemura`
- publication_info: RM `Proceedings of International Congress and Exhibition Computer Assisted Radiology and Surgery` vs site `Proceedings of International Congress and Exhibition Computer Assisted Radiology and Surgery (CARS2014)`

### Roughness Modulation of Real Materials using Electrotactile Augmentation

- site `id=104` / researchmap `published_papers:25241081`

- date: RM `2014` vs site `2014-06`
- publication_info: RM `Haptics: Neuroscience, Devices, Modeling, and Applications - 9th International Conference, EuroHaptics 2014, Versailles, France, June 24-26, 2014, Proceedings, Part I` vs site `Proceedings of Eurohaptics 2014`

### 視覚障がい者のための誘導音を用いた線図形トレーシングシステム

- site `id=223` / researchmap `published_papers:21725759`

- category: RM `Journal Papers` vs site `Domestic Conference Proceedings`
- authors: RM `浦西友樹, 瀧澤洸, 吉元俊輔, 井村誠孝, 大城理` vs site `瀧澤洸, 浦西友樹, 吉元俊輔, 井村誠孝, 大城理`
- date: RM `2015-05` vs site `2014-05`
- publication_info: RM `システム制御情報学会論文誌` vs site `第58回システム制御情報学会研究発表講演会 講演論文集`

### 投球シミュレーションのための野球ボールのリリースモデル

- site `id=224` / researchmap `misc:35562831`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- authors: RM `井村 誠孝, 横畑 亮輔, 浦西 友樹` vs site `井村誠孝, 横畑亮輔, 浦西友樹, 吉元俊輔, 黒田嘉宏, 大城理`
- publication_info: RM `システム制御情報学会研究発表講演会講演論文集` vs site `第58回システム制御情報学会研究発表講演会 講演論文集`

### ボクセル空間における煙霧のボケ除去のGPUを用いた高速化

- site `id=222` / researchmap `misc:18561730`

- publication_info: RM `第58回システム制御情報学会研究発表講演会 講演論文集` vs site `第58回システム制御情報学会研究発表講演会 講演論文集, 335-3`

### 手の筋骨格モデルを導入した投球シミュレーション

- site `id=38` / researchmap `published_papers:13000992`

- date: RM `2014` vs site `2014-02`

### リフォーカス画像におけるボケを用いた煙霧の空間濃度分布推定

- site `id=227` / researchmap `misc:37372466`

- category: RM `Misc.` vs site `Domestic Conference Proceedings`
- publication_info: RM `研究報告コンピュータビジョンとイメージメディア（CVIM）` vs site `電子情報通信学会 技術研究報告`

### 手の筋骨格モデルを導入した投球シミュレーション

- site `id=151` / researchmap `published_papers:21725756`

- category: RM `Journal Papers` vs site `Domestic Conference Proceedings`
- date: RM `2014-02` vs site `2013-09`
- publication_info: RM `生体医工学` vs site `生体医工学シンポジウム 講演予稿集`

### スマートフォン利用による視覚障がい者のための衣類の色および模様認識システム

- site `id=150` / researchmap `published_papers:21725755`

- category: RM `Journal Papers` vs site `Domestic Conference Proceedings`
- date: RM `2013-12` vs site `2013-09`
- publication_info: RM `生体医工学` vs site `生体医工学シンポジウム 講演予稿集`

### Connected Component Labeling on GPU based on Raster Segment Pair Approach

- site `id=152` / researchmap `misc:18561711`

- publication_info: RM `第16回画像の認識・理解シンポジウム 論文集` vs site `第16回画像の認識・理解シンポジウム 論文集 [Poster]`

### 視体積とリフォーカス画像群を併用した煙霧の空間濃度分布推定

- site `id=153` / researchmap `misc:18561712`

- publication_info: RM `第16回画像の認識・理解シンポジウム 論文集` vs site `第16回画像の認識・理解シンポジウム 論文集 [Poster]`

### Estimation of Bone Conduction Frequency Characteristics with Variation in Ear Canal

- site `id=136` / researchmap `misc:18561704`

- publication_info: RM `Proceedings of 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC2013)` vs site `Proceedings of 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC2013), Short Papers`

### Novel Algorithm for Real-Time Onset Detection of Surface Electromyography in Step-Tracking Wrist Movements

- site `id=109` / researchmap `misc:18561679`

- authors: RM `Yoshihiro Kuroda, Ilana Nisky, Yuki Uranishi, Masataka Imura, Allison M. Okamura, Osamu Oshiro` vs site `Yoshihiro Kuroda, Ilana Nisky, Yuki Uranishi, Masataka Imura, Allison Okamura, Osamu Oshiro`
- date: RM `2013` vs site `2013-07`
- publication_info: RM `2013 35TH ANNUAL INTERNATIONAL CONFERENCE OF THE IEEE ENGINEERING IN MEDICINE AND BIOLOGY SOCIETY (EMBC)` vs site `Proceedings of 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC2013)`

### 3D Simulation of Platelet Aggregation in Cryosurgery

- site `id=108` / researchmap `misc:18561678`

- date: RM `2013` vs site `2013-07`
- publication_info: RM `Proceedings of the Annual International Conference of the IEEE Engineering in Medicine and Biology Society, EMBS` vs site `Proceedings of 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC2013)`

### Automatic Cropping Method of Chest Radiographs Based on Adaptive Binarization

- site `id=107` / researchmap `misc:18561677`

- date: RM `2013` vs site `2013-07`
- publication_info: RM `2013 35TH ANNUAL INTERNATIONAL CONFERENCE OF THE IEEE ENGINEERING IN MEDICINE AND BIOLOGY SOCIETY (EMBC)` vs site `Proceedings of 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC2013)`

### Voice Response System of Color and Pattern on Clothes for Visually Handicapped Person

- site `id=106` / researchmap `misc:18561676`

- date: RM `2013` vs site `2013-07`
- publication_info: RM `Proceedings of the Annual International Conference of the IEEE Engineering in Medicine and Biology Society, EMBS` vs site `Proceedings of 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC2013)`

### Work Step Indication with Grid-Pattern Projection for Demented Senior People

- site `id=105` / researchmap `misc:18561675`

- date: RM `2013` vs site `2013-07`
- publication_info: RM `2013 35TH ANNUAL INTERNATIONAL CONFERENCE OF THE IEEE ENGINEERING IN MEDICINE AND BIOLOGY SOCIETY (EMBC)` vs site `Proceedings of 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC2013)`

### A Laser Projection-based Tele-Guidance System Embedded on a Mobility Aid

- site `id=110` / researchmap `misc:18561680`

- date: RM `2013` vs site `2013-03`
- publication_info: RM `2013 7TH INTERNATIONAL SYMPOSIUM ON MEDICAL INFORMATION AND COMMUNICATION TECHNOLOGY (ISMICT)` vs site `Proceedings of International Symposium on Medical Information and Communication Technology (ISMICT2013)`

### Interactive Photomosaic System Using GPU

- site `id=111` / researchmap `misc:18561681`

- date: RM `2012` vs site `2012-11`
- publication_info: RM `MM 2012 - Proceedings of the 20th ACM International Conference on Multimedia` vs site `ACM Multimedia 2012 (ACMMM2012) Technical Demos`

### Representation of Texture using Integrating Shading, Inter-reflection and Highlight in Mixed Reality

- site `id=113` / researchmap `misc:18561683`

- publication_info: RM `Proceedings of the 2012 Asian Symposium on Printing Technology (2012ASPT)` vs site `Proceedings of the 2012 Asian Symposium on Printing Technology (ASPT2012)`

### OpenCV: Open Computer Vision Library

- site `id=294` / researchmap `misc:18561779`

- date: RM `2012-07` vs site `2012-03`

### OpenCV 2 プログラミングブック

- site `id=5` / researchmap `books_etc:10430996`

- authors: RM `OpenCV, プログラミングブック制作チーム` vs site `OpenCV 2 プログラミングブック制作チーム`

### OpenCV2.2 ～画像処理プログラミングを簡単に～

- site `id=56` / researchmap `presentations:11803978`

- publication_info: RM `ロボット学会セミナー 第62回シンポジウム 「ロボットに使える画像処理技術の最前線」` vs site `ロボット学会セミナー 第62回シンポジウム 「ロボットに仕える画像処理技術の最前線」`

### FireVolleyball: Multi-player Interactive Game Providing a Sense of Touching Fire

- site `id=118` / researchmap `misc:18561688`

- date: RM `2010` vs site `2010-10`
- publication_info: RM `MM'10 - Proceedings of the ACM Multimedia 2010 International Conference` vs site `Proceedings of the ACM Multimedia 2010`

### 可視光画像と距離画像の併用による共連れ対応入退室情報記録システム

- site `id=260` / researchmap `misc:18561721`

- publication_info: RM `画像の認識・理解シンポジウム 2010 論文集` vs site `画像の認識・理解シンポジウム 論文集`

### Glanular Materials Rendering based on Radiance Caching

- site `id=120` / researchmap `misc:18561690`

- date: RM `2009` vs site `2009-12`
- publication_info: RM `ACM SIGGRAPH ASIA 2009 Posters, SIGGRAPH ASIA '09` vs site `Poster Presentation at SIGGRAPH ASIA 2009`

### Real-time Representation of Inter-reflection for Cubic Marker

- site `id=121` / researchmap `misc:18561691`

- date: RM `2009` vs site `2009-10`
- publication_info: RM `2009 8TH IEEE INTERNATIONAL SYMPOSIUM ON MIXED AND AUGMENTED REALITY - SCIENCE AND TECHNOLOGY` vs site `Proceedings of the 8th International Symposium on Mixed and Augmented Reality (ISMAR2009), Florida`

### OpenCV プログラミングブック 第2版

- site `id=6` / researchmap `books_etc:10447369`

- authors: RM `OpenCVプログラミングブック制作チーム` vs site `奈良先端科学技術大学院大学 OpenCVプログラミングブック制作チーム`

### Design and Implementation of Wireless LAN System for Airship

- site `id=122` / researchmap `misc:18561692`

- date: RM `2009` vs site `2009-06`
- publication_info: RM `DISTRIBUTED COMPUTING, ARTIFICIAL INTELLIGENCE, BIOINFORMATICS, SOFT COMPUTING, AND AMBIENT ASSISTED LIVING, PT II, PROCEEDINGS` vs site `Proceedings of the International Symposium on Distributed Computing and Artificial Intelligence (DCAI2009)`

### Implementation of Whole Shape Measurement System Using a Cylindrical Mirror

- site `id=124` / researchmap `misc:37620582`

- category: RM `Misc.` vs site `International Conference Proceedings`
- authors: RM `Uranishi Yuki, Manabe Yoshitsugu, Sasaki Hiroshi, CHIHARA Kunihiro` vs site `Yuki Uranishi, Yoshitsugu Manabe, Hiroshi Sasaki, Kunihiro Chihara`
- publication_info: RM `電子情報通信学会技術研究報告. IE, 画像工学` vs site `Proceedings of International Workshop on Advanced Image Technology (IWAIT2009)`

### 円筒鏡を用いた全周形状計測システムの実装

- site `id=156` / researchmap `misc:18561725`

- publication_info: RM `画像の認識・理解シンポジウム2008 論文集` vs site `画像の認識・理解シンポジウム2008 論文集, 長野  [Poster]`

### OpenCV プログラミングブック

- site `id=7` / researchmap `books_etc:10430998`

- authors: RM `OpenCVプログラミングブック制作チーム` vs site `奈良先端科学技術大学院大学 OpenCVプログラミングブック制作チーム`

### Whole Shape Measurement System Using a Single Camera and a Cylindrical Mirror

- site `id=131` / researchmap `misc:18561701`

- date: RM `2006` vs site `2006-08`
- publication_info: RM `18TH INTERNATIONAL CONFERENCE ON PATTERN RECOGNITION, VOL 4, PROCEEDINGS` vs site `Proceedings of the 18th International Conference on Pattern Recognition (ICPR2006)`

### 円筒鏡を用いた単眼全周形状計測システム

- site `id=157` / researchmap `misc:18561726`

- publication_info: RM `画像の認識・理解シンポジウム2006 論文集` vs site `画像の認識・理解シンポジウム2006 論文集, 宮城  [Poster]`

### 円筒鏡を用いた全周形状計測システムのための対応点探索手法の検討

- site `id=279` / researchmap `misc:18561775`

- publication_info: RM `第50回 システム制御情報学会研究発表講演会 講演論文集` vs site `第50回 システム制御情報学会研究発表講演会 講演論文集, 6W3-2`

### 円筒鏡を用いた3次元形状計測システム

- site `id=158` / researchmap `misc:18561727`

- publication_info: RM `画像の認識・理解シンポジウム2005 論文集` vs site `画像の認識・理解シンポジウム2005 論文集, 兵庫  [Poster]`

### Three-Dimensional Measurement System Using A Cylindrical Mirror

- site `id=132` / researchmap `misc:18561702`

- authors: RM `Y Uranishi, M Naganawa, Y Yasumuro, M Imura, Y Manabe, K Chihara` vs site `Yuuki Uranishi, Mika Naganawa, Yoshihiro Yasumuro, Masataka Imura, Yoshitsugu Manabe, Kunihiro Chihara`
- date: RM `2005` vs site `2005-06`
- publication_info: RM `IMAGE ANALYSIS, PROCEEDINGS` vs site `Proceedings of the 14th Scandinavian Conference on Image Analysis (SCIA2005)`

### Three-Dimensional Measurement for Small Moving Object

- site `id=133` / researchmap `misc:18561703`

- authors: RM `Y Manabe, Y Uranishi, Y Yasumuro, M Imura, KU Chihara` vs site `Yoshitsugu Manabe, Yuuki Uranishi, Yoshihiro Yasumuro, Masataka Imura, Kunihiro Chihara`
- date: RM `2005` vs site `2005-01`
- publication_info: RM `Videometrics VIII` vs site `Proceedings of SPIE-IS&T Electronic Imaging (SPIE2005)`

### 形状特徴を用いた非文字領域除去処理による文字列領域抽出の高精度化

- site `id=281` / researchmap `misc:18561777`

- authors: RM `松尾 賢一, 浦西 友樹, 上田 勝彦, 梅田 三千雄` vs site `浦西友樹, 松尾賢一, 上田勝彦`
- date: RM `2004` vs site `2004-03`
- publication_info: RM `奈良工業高等専門学校研究紀要` vs site `2004年電子情報通信学会総合大会 講演論文集`

## 補足

- 一致とみなしたがフィールド差分なし: 115 件（本レポートでは省略）
- `presentations` の非招待発表はサイト側カテゴリと1対1で対応しない場合があります
- researchmap の `misc`（misc_type なし）は雑誌寄稿・学会活動報告などが混在します
