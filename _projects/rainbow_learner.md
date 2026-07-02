---
layout: page
title: Rainbow Learner
description: Real-time estimation of lighting direction and spectral distribution from a structural-color AR marker
importance: 1
category: research
lang: en
img: assets/img/projects/rainbow_learner/structual_marker.png
---

When superimposing virtual objects onto the real world in augmented reality (AR), it is critical to maintain geometric, photometric, and temporal consistency. Planar AR markers preserve geometric alignment readily, but estimating the surrounding illumination — both its **direction** and its **spectral distribution** — from such markers remains difficult.

This project introduces **Rainbow Learner**, a structural-color marker created by combining a compact disc (CD) with a planar AR marker. The marker exploits **structural coloration**: microstructures on the CD surface disperse incident light into viewpoint- and illumination-dependent color patterns. Two convolutional neural networks learn the mapping from an observed structural-color pattern to (1) the light source direction and (2) its spectral distribution, enabling **real-time photometric consistency** for AR rendering.

### Overview

<div class="row justify-content-sm-center">
  <div class="col-sm-10">
    {% include figure.liquid loading="eager" path="assets/img/projects/rainbow_learner/proc.png" title="Training and estimation pipeline" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

In the **training phase**, pairs of structural-color pattern images and corresponding illumination maps / spectral distributions are collected under multiple light sources. In the **estimation phase**, a camera observes the marker, the AR pattern is detected to crop and mask the structural-color region, and the trained models output the illumination direction and spectral distribution in real time.

### Structural-color marker

<div class="row justify-content-sm-center">
  <div class="col-sm-8">
    {% include figure.liquid loading="eager" path="assets/img/projects/rainbow_learner/structual_marker.png" title="Structural-color marker (CD + AR marker)" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

The marker uses a CD's concentric microstructure — originally cut for reading/writing data — together with an ArUco AR marker for pose estimation. The CD's concentric geometry approximately decouples the observed pattern from the marker's in-plane rotation, and a matte coating suppresses the specular reflection that would otherwise saturate the camera image.

### Key idea: illumination direction *and* spectral distribution both leave a signature

Structural-color appearance changes with both the **elevation/azimuth of the light source** and its **spectral distribution**, even when different light sources look similarly white to a conventional camera:

<div class="row justify-content-sm-center">
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/test_1_1.png" title="Elevation / azimuth variation" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/test_1_2.png" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/test_1_3.png" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Because the same underlying microstructure disperses light by wavelength, a white LED, a white LED with a color filter, and a halogen lamp placed in the *same* direction still produce visibly different structural-color patterns. In other words, the pattern encodes the light source's spectrum, not just its RGB appearance — which is what makes spectral estimation possible from a single low-cost marker.

Unlike prior pattern-matching approaches that require pre-recorded exemplars for every viewing condition, Rainbow Learner **models** the pattern-to-illumination relationship with machine learning, improving generalization within the training distribution.

### Network architecture

<div class="row justify-content-sm-center">
  <div class="col-sm-6">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/network_1.png" title="Direction-estimation network" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-6">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/network_2.png" title="Spectral-distribution-estimation network" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

The model consists of **two CNNs** that share the same structural-color marker image as input:

- **Direction network** — outputs a 16-dimensional vector of spherical-harmonic coefficients (orders 0–3), which reconstructs an illumination environment map representing the dominant light source's elevation and azimuth.
- **Spectral network** — outputs an 81-dimensional vector representing the relative spectral intensity from 380 nm to 780 nm in 5 nm steps.

Both networks stack convolutional layers with Leaky ReLU activations followed by fully connected layers with a Hyperbolic Tangent activation, trained with the Adam optimizer using Mean Absolute Error (MAE) loss.

### Dataset and light sources

<div class="row justify-content-sm-center align-items-end">
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/white_LED.png" title="White LED" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/blue_LED.png" title="White LED + blue filter" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/red_LED.png" title="White LED + red filter" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/halogen_lamp.png" title="Halogen lamp" class="img-fluid rounded z-depth-1" %}
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

Four light sources — a white LED panel, the same panel with blue and red color filters, and a halogen lamp — were used to vary the spectral distribution during data collection. In a dark room, an omnidirectional camera recorded the illumination environment while an RGB camera simultaneously captured the structural-color pattern; a spectroradiometer measured each light source's ground-truth spectral distribution in advance. From this setup, **6,914** paired samples (marker image, 16-D direction coefficients, 81-D spectral distribution) were collected. The direction network was trained for 10 epochs and the spectral network for 70 epochs (TensorFlow 2.7.0 / Python 3.7.8).

### Results: illumination direction

<div class="row justify-content-sm-center align-items-center">
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/input.png" title="Observed pattern" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/map_tar.png" title="Ground-truth illumination map" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/map_pred.png" title="Estimated illumination map" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Across 1,383 held-out test images, the mean absolute error of the estimated light-source direction (measured via the luminance centroid of the reconstructed map) was **3.08° (vertical)** and **11.80° (horizontal)**. Placing the marker in novel indoor and outdoor scenes not seen during training still yielded reasonable direction estimates — **(7.03°, 5.63°)** indoors and **(1.41°, 9.84°)** outdoors — though accuracy degrades outside the training distribution.

### Results: spectral distribution

<div class="row justify-content-sm-center align-items-center">
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/input.png" title="Observed pattern" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/estimation_spectrum_tar.png" title="Ground-truth spectral distribution" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/estimation_spectrum_pred.png" title="Estimated spectral distribution" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

The spectral network estimates the full 81-dimensional spectral curve from the same structural-color pattern, achieving a mean absolute error of **3.17 × 10⁻²** per wavelength band over the test set. To make the estimated spectra easier to interpret, they were converted to CIE 1931 XYZ tristimulus values and then to RGB swatches for a direct visual comparison against the ground truth:

<div class="row justify-content-sm-center align-items-center">
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/white.png" title="White LED (ground truth)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/white_error.png" title="White LED (estimated)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/blue.png" title="Blue LED (ground truth)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/blue_error.png" title="Blue LED (estimated)" class="img-fluid rounded z-depth-1" %}
  </div>
</div>
<div class="row justify-content-sm-center align-items-center mt-1">
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/red.png" title="Red LED (ground truth)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/red_error.png" title="Red LED (estimated)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/halogen.png" title="Halogen lamp (ground truth)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-3">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/halogen_error.png" title="Halogen lamp (estimated)" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Estimated and ground-truth colors match closely for all four light sources. The halogen lamp is the hardest case: because its structural-color pattern sometimes resembles the white LED's, the spectral network occasionally confuses the two. Generalization to novel scenes mirrors the direction results — an indoor scene lit by a light source similar to the training set is estimated accurately, whereas an **outdoor** scene lit by sunlight shows a large gap, since sunlight's spectral range lies outside the four light sources used for training. Domain adaptation or broader light-source sampling during data collection are natural next steps.

### Real-time performance

Running the full pipeline — marker detection, projective transformation, cropping, masking, and both network inferences — averaged **91.5 ms (≈10.9 fps)** on a desktop PC (Core i7-4771, GTX 780 Ti) and **136.0 ms (≈7.4 fps)** on a laptop (Core i7-1065G7, no dGPU), confirming real-time operation on commodity hardware.

### Limitations

<div class="row justify-content-sm-center align-items-center">
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/fail_1.png" title="Marker undetected (saturation)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/fail_2.png" title="Pattern not captured (saturation)" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4">
    {% include figure.liquid path="assets/img/projects/rainbow_learner/fail_3.png" title="Marker undetected (low light)" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

Because a CD's recording surface is designed to reflect laser light efficiently, certain camera–light–marker geometries cause specular saturation that prevents marker detection or corrupts the observed pattern. Insufficient illumination can likewise prevent marker detection. Both cases fall outside the training distribution and are directions for future robustness improvements (e.g., HDR capture, alternative marker materials).

### Contributions

- First method to estimate **both light direction and spectral distribution in real time** from a low-cost planar structural-color marker
- Combines geometric tracking (AR marker) with photometric estimation (structural color + two dedicated CNNs)
- Enables AR rendering that accounts for spectral illumination, not just RGB approximations, at ~10 fps on commodity hardware

### Related publications

- Yuji Tsukagoshi, Yuki Uranishi, Jason Orlosky, Kiyomi Ito, Haruo Takemura, [Rainbow Learner: Lighting Environment Estimation from a Structural-Color Based AR Marker](/publications/), AIVR 2020.
- Yuki Uranishi, Masataka Imura, Tomohiro Kuroda, [The Rainbow Marker: An AR Marker with Planar Light Probe based on Structural Color Pattern Matching](/publications/), IEEE VR 2016.

### Acknowledgments

This work was supported by JSPS KAKENHI Grant Number 21K11962.
