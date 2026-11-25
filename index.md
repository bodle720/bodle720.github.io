---
title: Brian Odle | Computer Vision & Machine Learning Portfolio
description: Applied computer vision, machine learning, remote sensing, model evaluation, and deployment-oriented portfolio projects.
image: /assets/images/social/portfolio-preview.jpg
---

<style>
/* Homepage only: distinguish section boundaries from item separators. */
section h2.home-major-heading {
  border-bottom: 2px solid var(--heading);
}
section hr.home-divider {
  height: 0;
  background: none;
  border: 0;
  margin: 2rem 0;
}
section hr.home-divider--major {
  border-top: 2px solid var(--heading);
}
section hr.home-divider--minor {
  border-top: 1px solid #64748b;
}
</style>

## Computer Vision & Machine Learning Engineer
{: .home-major-heading }

I build practical computer vision and machine learning systems across dataset infrastructure, model training, evaluation, deployment, and applied mathematical modeling.

This portfolio highlights selected projects with concise case studies, visuals, results, and links to the full source code.

<hr class="home-divider home-divider--major">

## Computer Vision & Machine Learning Projects
{: .home-major-heading }

### [Global Wheat Head Detection](projects/global-wheat-head-detection.md)

End-to-end YOLO object detection project for dense wheat-head detection in agricultural imagery. Includes CVDMS dataset artifacts, YOLO training experiments, MLflow model selection, held-out test evaluation, visual prediction inspection, and Dockerized FastAPI inference with latency reporting.

[View project →](projects/global-wheat-head-detection.md)

<hr class="home-divider home-divider--minor">

### [Computer Vision Dataset Management System](projects/cvdms.md)

AWS CDK-based computer vision data-management system for ingesting raw imagery and labels, validating and deduplicating assets, registering canonical images and labels, and creating reproducible train/validation/test dataset versions.

[View project →](projects/cvdms.md)

<hr class="home-divider home-divider--minor">

### [BigEarthNet Multi-Label Satellite Classification](projects/bigearthnet.md)

PyTorch ResNet-18 transfer-learning workflow for 17-class multi-label satellite image classification. Uses CVDMS dataset-version artifacts, multi-hot labels, `BCEWithLogitsLoss`, thresholded evaluation, per-class threshold tuning, and confusion diagnostics.

[View project →](projects/bigearthnet.md)

<hr class="home-divider home-divider--major">

## Personal Projects
{: .home-major-heading }

### [Anchorage Through the Seasons](/projects/anchorage-through-the-seasons/)

Cloud-native geospatial analysis of seasonal vegetation greenness, snow, and ice across Anchorage, Alaska, using eight Sentinel-2 acquisitions, fixed geographic study regions, and interactive regional statistics.

[View project →](/projects/anchorage-through-the-seasons/)

<hr class="home-divider home-divider--major">

## Applied Mathematics & Data Science
{: .home-major-heading }

Educational notebooks and technical explorations of mathematical and computational foundations.

### [Dynamic Mode Decomposition (DMD)](projects/dmd-pendulum.md)

<p style="color: var(--muted);">Identifies spatial modes and temporal dynamics in data, demonstrated through the reconstruction and forecasting of synthetic pendulum motion.</p>

<hr class="home-divider home-divider--minor">

### [Independent Component Analysis (ICA)](https://github.com/bodle720/DSTopics/blob/main/ICA/ica_on_imagery.ipynb)

<p style="color: var(--muted);">Separates mixed signals into statistically independent components, demonstrated using artificially mixed images.</p>

<hr class="home-divider home-divider--minor">

### [Linear PCA](https://github.com/bodle720/DSTopics/blob/main/PCA_linear/pca_linear_oscillation_system.ipynb) · [Kernel PCA](https://github.com/bodle720/DSTopics/blob/main/PCA_kernel/pca_kernel.ipynb) · [Robust PCA](https://github.com/bodle720/DSTopics/blob/main/PCA_robust/PCA_robust_handwritten_digits_noise.ipynb) · [Sparse PCA](https://github.com/bodle720/DSTopics/blob/main/PCA_sparse/PCA_sparse_handwritten_digits.ipynb)

<p style="color: var(--muted);">Explores dimensionality reduction, nonlinear structure, low-rank and sparse decomposition, and interpretability through four Principal Component Analysis notebooks.</p>

<hr class="home-divider home-divider--major">

## Technical Areas
{: .home-major-heading }

Computer Vision · Machine Learning · PyTorch · YOLO · MLflow · FastAPI · Docker · AWS CDK · Dataset Engineering · Remote Sensing · Object Detection · Multi-Label Classification · Linear Algebra · Dynamical Systems

---

## Links

* [GitHub](https://github.com/bodle720)
* [MLProjects Repository](https://github.com/bodle720/MLProjects)
* [DSTopics Repository](https://github.com/bodle720/DSTopics)
* [Image Credits](/image-credits/)