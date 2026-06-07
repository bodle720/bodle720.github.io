# Global Wheat Head Detection

[← Back to Portfolio](../index.md)

## End-to-End YOLO Object Detection for Dense Agricultural Imagery

This project builds a deployment-ready computer vision workflow for detecting individual wheat heads in field imagery using the Global Wheat Head Detection 2021 dataset.

The task is a dense small-object detection problem: each image can contain many small, visually similar wheat heads that are tightly packed, partially occluded, or difficult to separate from the surrounding crop. The project covers the full workflow from dataset preparation and YOLO training through MLflow model selection, held-out test evaluation, and Dockerized FastAPI inference.

**Prediction visualization legend**

- <strong style="color: #ef4444;">Red:</strong> ground-truth wheat heads
- <strong style="color: #22c55e;">Green:</strong> matched predictions / true positives
- <strong style="color: #3b82f6;">Blue:</strong> unmatched predictions / false positives
- **Missed detections:** red boxes without a corresponding green prediction
- **Match rule:** prediction is matched when IoU ≥ 0.5 with a ground-truth box

<p align="center">
  <img src="../assets/images/global-wheat/effective_example.jpg" alt="Successful wheat head detection example" width="850"><br>
  <em>Held-out test example with ground truth boxes, matched predictions, and unmatched predictions.</em>
</p>

## Project Snapshot

| Area        | Summary                                   |
| ----------- | ----------------------------------------- |
| Task        | Single-class wheat-head object detection  |
| Dataset     | Global Wheat Head Detection 2021          |
| Model       | YOLO11s                                   |
| Tracking    | MLflow + TensorBoard                      |
| Deployment  | FastAPI + Docker                          |
| Final model | MLflow `GlobalWheatHeadDetector@champion` |
| Main focus  | Train-to-deploy computer vision workflow  |

## Workflow

<div class="workflow">
  <div class="workflow-step">CVDMS dataset artifacts</div>
  <div class="workflow-arrow">↓</div>

  <div class="workflow-step">Local dataset cache and visual inspection</div>
  <div class="workflow-arrow">↓</div>

  <div class="workflow-step">YOLO-format conversion</div>
  <div class="workflow-arrow">↓</div>

  <div class="workflow-step">YOLO training experiments</div>
  <div class="workflow-arrow">↓</div>

  <div class="workflow-step">MLflow and TensorBoard tracking</div>
  <div class="workflow-arrow">↓</div>

  <div class="workflow-step">Validation-based model selection</div>
  <div class="workflow-arrow">↓</div>

  <div class="workflow-step">Held-out test evaluation</div>
  <div class="workflow-arrow">↓</div>

  <div class="workflow-step">MLflow champion registration</div>
  <div class="workflow-arrow">↓</div>

  <div class="workflow-step">FastAPI/Docker inference service</div>
</div>

The goal was not only to train a detector, but to build a reproducible, inspectable, deployment-oriented object detection workflow.

## Dataset and Challenge

The dataset was ingested through my Computer Vision Dataset Management System, then exported as a versioned object-detection dataset for training.

| Split      | Images | Avg. boxes / image |
| ---------- | -----: | -----------------: |
| Train      |  3,605 |               45.4 |
| Validation |  1,448 |               30.6 |
| Test       |  1,334 |               50.5 |
| Total      |  6,387 |                  — |

The official source splits were preserved instead of randomly recreated. Dataset profiling showed split-level differences in lighting, color richness, contrast, and object density. This makes the held-out test set more realistic and more challenging than a randomly shuffled split.

<p align="center">
  <img src="../assets/images/global-wheat/quality_lighting_buckets.png" alt="Lighting bucket distribution by split" width="850"><br>
  <em>CVDMS profiling revealed lighting differences across train, validation, and test splits.</em>
</p>

## Method

I trained and compared Ultralytics YOLO models on a local RTX 4060 Laptop GPU with 8 GB VRAM.

The training workflow included:

* CVDMS-to-YOLO dataset conversion
* dataset mosaics and visual inspection
* practical batch size / dataloader worker tuning
* YOLO11n and YOLO11s baseline comparisons
* MLflow and TensorBoard experiment tracking
* validation-only model selection
* one-time held-out test evaluation
* MLflow model registration for deployment

Selected experiment summary:

| Experiment              | Purpose                    | Outcome                                |
| ----------------------- | -------------------------- | -------------------------------------- |
| YOLO11n baseline        | Lightweight starting point | Fast, weaker test performance          |
| YOLO11s baseline        | Larger detector            | Better recall and mAP50-95             |
| YOLO11s, 50 epochs      | Longer training            | Final validation-selected model        |
| YOLO11s, 768 image size | Higher-resolution test     | Higher compute cost without clear gain |

The selected model was:

| Field        | Value                                    |
| ------------ | ---------------------------------------- |
| Model        | YOLO11s                                  |
| Training run | `baseline_003_yolo11s_e50_img640_b16_w4` |
| Epochs       | 50                                       |
| Image size   | 640                                      |
| Parameters   | ~9.43M                                   |
| Model size   | ~18.29 MB                                |
| MLflow model | `GlobalWheatHeadDetector`                |
| MLflow alias | `champion`                               |

## Results

The final model was selected using validation mAP50-95. The held-out test split was evaluated only after the model was chosen.

| Metric    | Validation | Held-out Test |
| --------- | ---------: | ------------: |
| Precision |      0.924 |         0.806 |
| Recall    |      0.837 |         0.594 |
| mAP50     |      0.920 |         0.684 |
| mAP75     |      0.555 |         0.225 |
| mAP50-95  |      0.528 |         0.309 |

The validation result shows the detector learned the task well. The lower held-out test result reflects the harder test distribution, higher object density, and difficulty of strict localization metrics in dense wheat-head scenes.

<p align="center">
  <img src="../assets/images/global-wheat/metrics_val_mAP50-95B.png" alt="Validation mAP50-95 training curve" width="850"><br>
  <em>Validation mAP50-95 during training for the selected YOLO11s run.</em>
</p>

## Visual Evaluation

Evaluation images use:

| Color | Meaning                 |
| ----- | ----------------------- |
| Red   | Ground-truth wheat head |
| Green | Matched prediction      |
| Blue  | Unmatched prediction    |

<p align="center">
  <img src="../assets/images/global-wheat/dense_example.jpg" alt="Dense wheat head detection example" width="850"><br>
  <em>Dense held-out test scene with many wheat heads.</em>
</p>

<p align="center">
  <img src="../assets/images/global-wheat/poor_example.jpg" alt="Difficult wheat head detection example" width="850"><br>
  <em>Harder case showing missed or merged wheat heads in a dense scene.</em>
</p>

The visual examples are important because dense small-object detection is not fully explained by a single metric. They show both useful detection behavior and remaining failure modes.

## Deployment and Latency

The selected model was registered in MLflow and served through a Dockerized FastAPI app.

At startup, the API loads:

<div class="tech-callout">
  <div class="tech-callout-label">Registered MLflow model URI</div>
  <code>models:/GlobalWheatHeadDetector@champion</code>
</div>

The `/predict` endpoint accepts an image upload and returns structured detections, bounding boxes, confidence scores, inference settings, and request-level latency metrics.

Local Docker CPU benchmark using 100 sequential prediction requests after warmup:

| Measurement                  |      Mean |    Median |        P95 |
| ---------------------------- | --------: | --------: | ---------: |
| Server total request         | 76.379 ms | 74.196 ms | 108.508 ms |
| Server model inference       | 68.656 ms | 66.368 ms |  97.993 ms |
| Client wall-clock round trip | 86.818 ms | 83.665 ms | 119.628 ms |

Offline YOLO evaluation on the local GPU averaged about 7.1 ms per image for preprocess, inference, and postprocess combined. The Docker benchmark is the better measurement for the deployed demo because it exercises the actual API path.

## Engineering Highlights

This project demonstrates:

* dense small-object detection with YOLO
* CVDMS dataset ingestion and versioned dataset artifacts
* image-quality and split-drift analysis before training
* CVDMS-to-YOLO conversion
* local GPU training and speed tuning
* MLflow and TensorBoard experiment tracking
* validation-only model selection
* held-out test evaluation
* visual prediction inspection
* MLflow champion model registration
* Dockerized FastAPI inference
* request-level latency reporting

## Limitations

This is a deployment-ready prototype, not a production-grade crop-counting system.

Current limitations include missed wheat heads in dense scenes, duplicate or unmatched predictions depending on post-processing settings, and lower held-out test performance than validation performance. Future production work could include threshold calibration, improved NMS/post-processing, larger model experiments, sliced/tiled inference, and deployment monitoring on production-like imagery.

## Links

* [Source code and full documentation](https://github.com/bodle720/MLProjects/tree/main/Training_Projects/projects/GlobalWheatHeadDetection)
* [Dataset exploration README](https://github.com/bodle720/MLProjects/tree/main/Training_Projects/projects/GlobalWheatHeadDetection/docs/README_initial_dataset.md)
* [Training experiments README](https://github.com/bodle720/MLProjects/tree/main/Training_Projects/projects/GlobalWheatHeadDetection/docs/README_training_experiments.md)
* [Final results README](https://github.com/bodle720/MLProjects/tree/main/Training_Projects/projects/GlobalWheatHeadDetection/docs/README_results.md)
* [Deployment README](https://github.com/bodle720/MLProjects/tree/main/Training_Projects/projects/GlobalWheatHeadDetection/deployment/README.md)
* [Evaluation README](https://github.com/bodle720/MLProjects/tree/main/Training_Projects/projects/GlobalWheatHeadDetection/evaluation/README.md)
