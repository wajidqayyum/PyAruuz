# Machine Learning Implementation Guide: Urdu Scansion

Transitioning from a rule-based engine to a Machine Learning (ML) model allows the system to handle unvoweled text and rare vocabulary by learning the underlying rhythmic patterns of the Urdu language. This guide provides a step-by-step technical roadmap for that implementation.

---

## 1. Data Engineering: The Foundation
The most valuable asset for this project is the existing `aruuz.db`.

### A. Dataset Generation
1.  **Source Extraction**: Extract all words and their associated `Taqti` and `Code` from `mastertable` and `exceptions`.
2.  **Line Synthesis**: Urdu scansion is context-dependent (due to Izafat and Word Grafting). Generate synthetic poetic lines by sampling words from the database and concatenating them into valid meters using your current scansion engine.
3.  **Feature Sets**:
    *   **Input**: Urdu sentences (raw, no Araab).
    *   **Target**: Syllable sequences (e.g., `=-== -=-= --=`).
    *   **Auxiliary Target**: Voweled (Muarrab) text. Predicting the Araab as an intermediate step significantly improves rhythmic accuracy.

### B. Preprocessing
*   **Normalization**: Standardize Unicode characters (e.g., ensure all `ی` are the same codepoint).
*   **Noon Ghunna Handling**: Explicitly mark nasalized sounds as they are rhythmic markers.

---

## 2. Model Architecture: Seq2Seq with CRF

A standard Transformer or Bi-LSTM is insufficient because poetic meter has strict structural constraints.

### A. The Core: Transformer Encoder
Use a pre-trained Urdu model like **BERT-base-Urdu** or **RoBERTa-Urdu**.
*   **Fine-tuning**: Fine-tune the model to output a vector for each character or syllable.

### B. The Sequence Head: Conditional Random Field (CRF)
Place a **CRF Layer** on top of the Transformer.
*   **Role**: The CRF learns transition probabilities, preventing the model from outputting rhythmically "illegal" sequences.

### C. Multitask Learning (MTL)
Train the model on two tasks:
1.  **Syllable Classification**: Predicting `-`, `=`, or `x`.
2.  **Diacritic Prediction**: Predicting the missing Zabar, Zer, and Pesh.

---

## 3. Training Strategy

### A. Tokenization
Use **Character-Level** or **Subword-Level (BPE)** tokenization. Scansion happens at the character level, so word-level models are less effective.

### B. Training Objective
*   **Loss**: Masked Cross-Entropy Loss + CRF Log-Likelihood.
*   **Curriculum Learning**: Start on short phrases and increase to full poetic lines.

---

## 4. The "Hybrid Inference" Pipeline (Recommended)

Combine the ML model's intuition with the rule-based engine's precision.

1.  **ML Predictor**: Predicts missing Zabar, Zer, and Pesh.
2.  **Deterministic Engine**: Restored text is passed to your current `length_XXX_scan` heuristics.
3.  **Result**: High speed with 100% rhythmic accuracy.

---

## 5. Deployment Roadmap

### Phase 1: Data Collection (1 Week)
Export `aruuz.db` to JSONL and generate synthetic lines.

### Phase 2: Model Benchmarking (2 Weeks)
Compare Bi-LSTM + CRF vs. Fine-tuned Urdu-BERT.

### Phase 3: Integration (1 Week)
Export to **ONNX** for high-speed inference and wrap in a FastAPI service.
