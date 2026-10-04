# Aruuz Urdu Poetry Scansion Engine - Python Port Context

## Project Overview
This project is a direct Python port of the open-source **Aruuz C# Urdu Scansion Engine**. The goal is to accurately parse Urdu Ghazals, evaluate their rhythmic weight (Taqti), and match them against standard poetic meters locally using Python.

## Current State: ~95% Parity Achieved
The Python engine is currently fully functional and achieves identical results to the C# engine for the vast majority of lines. 

### Project Structure (in `python_port/`)
* **`aruuz.db`**: SQLite database ported from the original MySQL dump. Contains `exceptions`, `mastertable`, `plurals`, and `variations`.
* **`scansion.py`**: The core `Scansion` engine. Handles DB lookups, path generation, Vasl (Word Grafting), Izafat, and matching.
* **`heuristics.py`**: Complex phonetic parsing logic (`length_one_scan` to `length_five_scan`, and `noon_ghunna`) for words not found in the DB.
* **`meters.py`**: Contains the 129 standard Urdu meters and their symbol representations.
* **`araab.py`**: Constants for Arabic/Urdu diacritics (zabar, zer, pesh, jazm, etc.).
* **`ghazal_scanner.py`**: A CLI tool to batch-process a full Ghazal.

## Core Evaluation Workflow
When `scan_line(line)` is called:
1. **Word Splitting**: The line is split into words.
2. **Database Lookup (`get_word_codes`)**:
   * Queries the DB using the word with diacritics (retaining special letters like Noon Ghunna `ں` and Do Chashmi He `ھ`).
   * Searches in order: `exceptions` -> `mastertable` -> `plurals` -> `variations`.
   * If found in `mastertable`, splits the `Taqti` column by `+` and converts phonetic chunks to symbols (`=` for long, `-` for short, `x` for flexible).
3. **Heuristics Fallback**: If not in the DB, strips diacritics and runs `assign_code_heuristics` (which uses `heuristics.py`).
4. **Poetic Flexibilities**:
   * **Word End Flexibility**: Modifies the final symbol of a word based on vowels or origin language (e.g., `=` becomes `x` or `-x`).
   * **Izafat (`apply_izafat`)**: Modifies the rhythm if the word ends in a 'zer' (e.g., `کشِ`).
   * **Vasl / Word Grafting**: In `scan_line`, if a word ends in a consonant and the next starts with Alif `ا`, they merge rhythmically.
5. **Path Generation**: `itertools.product` generates all possible rhythmic combinations for the line.
6. **Matching**: Custom Levenshtein distance compares the generated paths against the `meters.py` database to find "Perfect" or "Closest" matches.

## Recent Fixes Implemented
* Implemented **Izafat (`ِ`)** logic to correctly add short syllables for trailing zers.
* Implemented **NoonGhunna** heuristics to correctly shorten `ہیں` and similar verbs to `-`.
* Fixed DB queries so they don't strip `ں` and `ھ` (preventing words like `نہیں` from failing).
* Implemented **Vasl (وصالِ الف)** across word boundaries.
* Fixed internal logic blocks in `length_three_scan` and `length_four_scan` for unvowelized fallback cases.

## Remaining Tasks (To-Do for Next Session)
To achieve 100% absolute parity with the C# engine for extreme edge cases, the following features from `Scansion.cs` need to be ported:

1. **Dynamic Plurals (`pluralForm*`)**:
   * Currently, we strictly search the `plurals` table. The C# code actively strips suffixes (like `وں`, `یں`, `ات`, `ے`) to find the singular root in the database (e.g., reducing `اُجڑے` to `اُجڑنا`), and then dynamically appends the suffix weight. 
2. **Compound Words (`compoundWord`)**:
   * A function to split long, unknown Persian/Urdu phrases into two known database words and combine their rhythms.
3. **Special Poetic Modifiers (`zamzamaFeet`, `hindiFeet`)**:
   * Some base meters (like `فَعِلن` `--=`) are dynamically stretched by Aruuz to allow for Urdu/Hindi liberties (like `فَعِلات` `--=-` when words end in trailing consonants, e.g., `میں فراز`). Porting these modifiers will fix the final 1-edit distance errors.
4. **Visual Output Formatting (`TaqtiObject` / `crunch`)**:
   * Implement the logic that physically aligns individual syllables under the metrical Arkan (e.g., aligning `ای ک دُش مَن` directly under `فاعلاتن`) to generate the HTML/Text visual tables.
5. **Long Word Heuristics**:
   * Port `length_six_scan` through `length_nine_scan` for extremely long unknown words.
