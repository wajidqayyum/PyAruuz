# Urdu Scansion Engine: Architectural Guide & Future Roadmap

This document provides a deep technical breakdown of the current rule-based Scansion Engine and outlines how to transition toward a high-efficiency production system or a Machine Learning (ML) model.

---

## 1. How the Current Engine Works

The engine is a **multi-layered rule-based system** that simulates the phonetic and rhythmic parsing of Urdu poetry. It operates in several distinct phases:

### Phase A: Lexical Analysis & Decomposition
1.  **Tashdid Rewriting**: The engine first "unrolls" words with Shadda (e.g., `مُدّت` becomes `مُد + دَت`). This ensures the double consonant is correctly accounted for in the syllable count.
2.  **Compound Word Splitting**: Words are split by the `+` delimiter (retrieved from the `Taqti` column in the database). This allows for recursive scanning of complex Persian-style compounds.
3.  **Suffix Resolution**: If a word isn't in the database, the engine attempts to strip known suffixes (`وں`, `یں`, `ات`, `نا`, etc.) and queries the database for the root word, mutating the resulting code based on the suffix type.

### Phase B: The Heuristic Scan (`length_XXX_scan`)
When a word is unknown, the engine applies hardcoded heuristics based on the presence of **Araab** (Zer, Zabar, Pesh, Jazm):
-   **Vowel Rules**: Characters like `ا`, `و`, `ی`, and `ے` are treated as long syllables (`=`) unless they act as consonants.
-   **Consonant Clusters**: Two consecutive consonants without a vowel usually result in a heavy syllable (`=`).
-   **Noon Ghunna**: Nasalized sounds (`ں`) are weighted as transparent or weight-reducing depending on their position.

### Phase C: Line-Level Poetic License
Scansion isn't just about individual words; it's about how they interact:
-   **Alif-Lam Grafting**: Handling the "L" sound in `عبدُالکریم` by shifting weights from the preceding word.
-   **Izafat (Ezafe)**: The short "e" sound at the end of words (like `غمِ عشق`) adds a short syllable (`-`) but can be stretched to long (`x`) based on the meter.
-   **Ataf (Waw)**: The conjunctive "o" (e.g., `دل و جان`) is processed similarly to Izafat.

### Phase D: Fuzzy DP Matching
The engine uses a **Dynamic Programming (DP)** approach to align the line's possible codes against a registry of ~300 meters.
-   **Zi-aaf (Flexibility)**: It accounts for syllables that can be either short or long (`x`).
-   **Tilde Rule (`~`)**: Supports Persian-style flexible syllables where a short syllable can be suppressed or a long one shortened.

---

## 2. Building an Efficient Production System

The current engine is robust but can be optimized for large-scale analysis:

### 1. Finite State Automata (FSA)
Instead of suffix stripping via logic branches, use a **Trie** or **FSA** to represent the entire Urdu dictionary.
-   Each node in the Trie stores the scansion code for that prefix.
-   Suffixes can be handled as state transitions within the automaton, allowing O(L) lookup for any word.

### 2. Pre-computed Scansion Cache
-   **Bloom Filters**: Check if a word is "known" before hitting the DB.
-   **In-Memory KV Store**: Use Redis to keep the scans of the top 100,000 most common Urdu words ready.

### 3. Parallel DP Aligners
Matching a line against 300+ meters can be parallelized using SIMD or GPU kernels, running the DP matching across all meters simultaneously.

---

## 3. Transitioning to Machine Learning (ML)

An ML model can "learn" the rhythm of Urdu poetry without needing explicit Araab.

### Recommended Model Architecture
1.  **Transformer (Encoder-Only)**: Use a model like `urdu-bert` to extract embeddings.
2.  **CRF (Conditional Random Field) Head**: A CRF layer on top of the Transformer ensures that the output follows valid rhythmic transitions.
3.  **Cross-Lingual Transfer**: Leverage Persian and Arabic datasets for high-literary vocabulary.

### Data Strategy
-   **Source**: Use the `aruuz.db` as a supervised training set.
-   **Augmentation**: Randomly remove Araab from input text to force the model to learn scansion from characters alone.

### Implementation Roadmap
1.  **Tokenizer**: Character-level tokenizer to handle Urdu morphology.
2.  **Loss Function**: Cross-Entropy loss for each syllable position.
3.  **Hybrid Inference**: Use the ML model to predict Araab for unknown words, then pass that through the rule-based engine for a deterministic proof.

---

## Summary Comparison
| Feature | Rule-Based (Current) | ML Model (Future) |
| :--- | :--- | :--- |
| **Accuracy** | High (with Araab) | High (from context) |
| **Speed** | Medium | Fast (Forward pass) |
| **Robustness** | Brittle on rare words | Generalizes well |
| **Requirements** | Database + Heuristics | Training Data + GPU |
