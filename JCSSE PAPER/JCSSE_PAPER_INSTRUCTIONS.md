# JCSSE / ICSEC Paper Writing Instructions

> **This is the authoritative style guide.** Before writing or editing ANY content in
> `conference_101719.tex`, read and internalize every rule below.
> These rules are derived from two reference papers that have been published at
> ICSEC 2024 and ICSEC 2025 — the companion conference to JCSSE within the same
> IEEE-format ecosystem. Every aspect — tone, structure, length, figure handling,
> data presentation — must match these references.

---

## 1. Global Constraints

| Parameter | Target |
|---|---|
| Total pages | **6** (hard limit, IEEE standard) |
| Column format | **Double-column**, IEEE `\documentclass[conference]{IEEEtran}` |
| Font | Times New Roman (default IEEEtran) |
| Abstract length | **150–220 words** |
| References | **20–35** entries, IEEE numeric `[1]` style |
| Figures | **4–6** total |
| Tables | **2–4** total |
| Template | `conference_101719.tex` with `IEEEtran.cls` |

---

## 2. Document Structure and Page Budget

The paper must follow this exact section layout. Roman-numeral numbered,
**ALL-CAPS** section headers. Subsections use bold-italic lettered headings (A, B, C).
Third-level headings use numbered italic (1), 2), 3)) or bold-italic lowercase (a., b., c.).

| # | Section | ≈ Pages | What Belongs Here |
|---|---|---|---|
| I | INTRODUCTION | 0.75–1.0 | Background → Problem statement → Proposed solution (1 sentence) → Contributions (numbered list) → Paper organization sentence |
| II | RELATED WORK(S) | 0.50–0.75 | Grouped by technical theme (bold-italic sub-headings). 2–3 sentences per cited work. Always say what they did AND how our work differs. |
| III | METHODOLOGY (or DATASET AND METHODOLOGY) | 1.5–2.0 | System overview diagram → each module as a subsection → equations, hyperparameters, design rationale |
| IV | EXPERIMENTAL RESULTS (AND DISCUSSION) | 1.5–2.0 | Setup (hardware, dataset, config) → Quantitative tables → Qualitative figures → Discussion paragraph → Limitations |
| V | CONCLUSION | 0.25–0.50 | 1 paragraph: restate contribution, key numerical results, future work. NO new information. |
| — | ACKNOWLEDGMENT | 2–3 lines | Thank institution(s) |
| — | REFERENCES | 0.5–0.75 | IEEE format |

> [!IMPORTANT]
> Always end the Introduction with a "paper organization" sentence:
> *"The rest of this paper is organized as follows: Section II reviews…"*

> [!IMPORTANT]
> The Conclusion must explicitly restate the most important numerical result (e.g.,
> "achieving 75.22% mAP and 78.83% Rank-1 accuracy").

---

## 3. Writing Style — Sentence Level

### 3.1 Tone
- **Formal, objective, and technically precise.** No marketing language.
- Never use "we believe", "we think", "our amazing system". Use "we propose",
  "we evaluate", "the system achieves".
- Avoid superlatives ("best-ever", "groundbreaking") unless backed by a table.

### 3.2 Voice
- **Methodology & setup → Passive voice:**
  "The model is trained for 100 epochs." / "Frames are resized to 480×480."
- **Contributions & results → Active voice:**
  "We propose…", "Our framework achieves…", "ConvNeXt achieved the highest mA."
- **Related work → Active voice for each cited author:**
  "Wojke et al. [5] proposed DeepSORT, which…"

### 3.3 Sentence Length
- Target **20–30 words per sentence** (medium length).
- Never exceed 40 words in a single sentence. If a sentence needs more, split it.
- Use semicolons sparingly; prefer two short sentences.

### 3.4 Paragraph Length
- **3–5 sentences per paragraph** is the sweet spot.
- Never write a single-sentence paragraph (except in a numbered contribution list).
- Never write a paragraph longer than 8 sentences; split it.

### 3.5 Transition Words (Use These)
Use these academic connectors between sentences/paragraphs where appropriate:
- Furthermore, Moreover, In addition,
- Specifically, In particular,
- However, In contrast, Unlike,
- Consequently, As a result,
- To address this, To achieve this,
- Evidently, Notably,

### 3.6 Numbers and Data in Prose
- Always use `%` with one or two decimal places: "94.03%", "75.22%".
- When comparing, state both numbers: "…improved from 34.4% to 58.4%."
- Introduce metrics before using them: "Multiple Object Tracking Accuracy (MOTA)."
- Hardware specs use exact model: "NVIDIA GeForce RTX 4060 (8 GB VRAM)."
- Use "respectively" for parallel lists: "Campus and factory achieved 60.2% and 63.3% IDF1, respectively."

### 3.7 Technical Terminology
- Define acronyms on first use: "person re-identification (Re-ID)."
- Use rigorous terms from the CV/AI domain.
- Avoid colloquialisms and informal abbreviations.
- Be consistent: if you call it "Re-ID" once, always call it "Re-ID" (not "re-id"
  or "ReID" or "re-identification" later).

---

## 4. Abstract Rules

The abstract must follow this exact 5-part structure in a **single paragraph**:

1. **Context** (1–2 sentences): State the broad application domain and why it matters.
2. **Problem** (1–2 sentences): Identify the specific challenge or gap.
3. **Proposed method** (2–3 sentences): Briefly describe what the system does and its key components. Name specific techniques.
4. **Results** (1–2 sentences): State the most important quantitative results with exact numbers.
5. **Implication/Future** (0–1 sentence): Optional brief mention of limitations or future direction.

> [!CAUTION]
> - **Never** include citations in the abstract.
> - **Never** use undefined acronyms in the abstract.
> - Keep it between **150–220 words**. Count carefully.
> - Do not include implementation details (framework versions, GPU models) in the abstract.

---

## 5. Introduction Rules

### Structure (4–5 paragraphs):
1. **Broad context** (3–4 sentences): What is the domain? Why is it important?
2. **Narrowing to the problem** (3–4 sentences): What specific challenge does this paper address? What are the limitations of existing approaches?
3. **Proposed solution** (3–4 sentences): What do we propose? How does it work at a high level?
4. **Contributions** (numbered list, 3 items max): Each contribution is 1 sentence. Use "(1)…; (2)…; and (3)…" inline style, or a LaTeX `\begin{enumerate}` block.
5. **Paper organization** (1 sentence): "The remainder of this paper is organized as follows…"

> [!WARNING]
> Do NOT include results in the Introduction unless it is a single headline number in the abstract.

---

## 6. Related Work Rules

- Group by **technical theme** using bold-italic sub-headings (e.g., *Attribute-assisted person ReID*, *Feature fusion*).
- For each cited work: **Who** [citation] + **what they did** + **how it differs from ours** (2–3 sentences max).
- Aim for **6–10 distinct works** discussed in this section.
- End with a transition paragraph (1–2 sentences) that positions our work relative to the literature.

---

## 7. Methodology Rules

- Start with a **System Overview** subsection that describes the full pipeline and references a system-architecture figure.
- Each subsequent subsection covers one module/component.
- Include **mathematical formulations** for any non-trivial computation (e.g., homography transformation, loss functions). Use `\begin{equation}` blocks.
- Specify **hyperparameters** in the text: learning rate, batch size, optimizer, epochs, thresholds.
- Reference figures inline: "As shown in Fig. 1, the pipeline consists of…"
- Use **hierarchical sub-subsections** when a module has sub-components:
  ```
  III. METHODOLOGY
     A. System Overview
     B. Module Name
        1) Sub-component 1
        2) Sub-component 2
           a. Detail
           b. Detail
  ```

---

## 8. Experimental Results Rules

### 8.1 Setup Subsection
- State the **dataset** (name, size, source, what it contains).
- State the **hardware** (exact GPU model, VRAM).
- State all **configuration parameters** (thresholds, frame skip, resolutions).
- This subsection replaces a standalone "Experimental Setup" section; keep it inside Results.

### 8.2 Tables
- Caption goes **above** the table (`\caption{...}` before `\begin{tabular}`).
- Use ALL-CAPS for table captions: `TABLE I: PERFORMANCE OF…`
- **Bold the best value** in each column.
- **Bold the Average/Summary rows.**
- Use `|` column separators and `\hline` row separators (IEEE standard).
- Use `\resizebox{\columnwidth}{!}{...}` if the table exceeds column width.
- Always introduce the table in the text before it appears: "Table I presents the…"

### 8.3 Discussion
- Compare environments/configurations and explain **why** one is better.
- Mention specific numbers: "The factory achieved 63.3% IDF1 vs. 60.2% for the campus."
- State **limitations** honestly in 1–2 sentences at the end.

### 8.4 Qualitative Results
- Include 1–2 figures showing visual outputs (tracking screenshots, t-SNE plots, confusion matrices, retrieval examples).
- Each qualitative figure needs a descriptive caption.

---

## 9. Conclusion Rules

- **One paragraph only** (8–15 sentences).
- Restate the contribution without introducing new information.
- Cite the key quantitative results.
- End with 1–2 sentences on future work.
- Do NOT repeat the abstract verbatim; rephrase.

---

## 10. Figure and Table Formatting

### Figures
- Use `\begin{figure}[htbp]` placement.
- Caption goes **below** the figure: `\caption{Description.}`
- Reference as **"Fig. 1"** in text (capital F, period after number).
- **Single-column** figures: `\begin{figure}` with `\includegraphics[width=\linewidth]`.
- **Double-column** figures (for system overviews, comparison panels): use `\begin{figure*}`.
- Use at most **1–2 double-column** figures per paper.
- Figures should be **high-resolution** and large enough to read at printed size.
- If a placeholder is needed, use `\framebox` with descriptive text.

### Tables
- Use `\begin{table}[htbp]`.
- Caption goes **above** the table.
- Reference as **"Table I"** (capital T, Roman numerals).
- All table captions use sentence case or title case consistently.

---

## 11. Citations and References

- Use `\cite{key}` inline with IEEE numeric style: "[1]", "[2, 3]", "[4]–[7]".
- In related work, use "Author et al. [N]" format on first mention.
- Reference list uses standard IEEE formatting:
  ```
  \bibitem{key} A. Author, B. Author, and C. Author, ``Title,'' \textit{Journal/Conference}, vol. X, no. Y, pp. Z--W, Year.
  ```
- Target **20–35 references**. Fewer than 15 looks weak; more than 40 is excessive.

---

## 12. LaTeX Conventions

- Do NOT add unauthorized packages.
- Use `\label{}` and `\ref{}` for all cross-references.
- Use `~` (non-breaking space) before `\cite`, `\ref`: `as shown in Fig.~\ref{fig:pipeline}`.
- Use `$...$` for inline math and `\begin{equation}` for display math.
- En-dash for ranges: `pp. 100--110`, not `pp. 100-110`.
- Use `\textit{...}` for journal/conference names in references.
- Use `''...''` (double backtick/single-quote pairs) for quoted titles in references.
- Balance the final page columns with `\vfill\null` or `\balance` if needed.

---

## 13. Self-Review Checklist

Before finalizing any edit, verify ALL of the following:

- [ ] Total page count is exactly **6 pages**
- [ ] Abstract is **150–220 words** with no citations
- [ ] Contribution list has **exactly 3 items**
- [ ] Every figure/table is referenced in the text **before** it appears
- [ ] All acronyms defined on first use
- [ ] No single-sentence paragraphs
- [ ] No paragraph exceeds 8 sentences
- [ ] No sentence exceeds ~40 words
- [ ] Best values in results tables are **bolded**
- [ ] Conclusion restates key metrics numerically
- [ ] Final page columns are balanced
- [ ] All `\ref{}` and `\cite{}` resolve (no "??")
- [ ] Writing tone is formal, objective — no marketing language
- [ ] IEEE formatting: Fig. X (period), Table I (Roman numeral)
- [ ] Consistent terminology throughout (e.g., "Re-ID" not mixed with "ReID")

---

## 14. Proactive Quality Improvement

Even when not explicitly asked, you MUST:

1. **Flag section length violations:** If any section exceeds or falls short of its page budget by more than 25%, report it immediately with a specific recommendation.
2. **Flag style inconsistencies:** If terminology, voice, or formatting deviates from these rules, correct it silently or flag it.
3. **Flag missing elements:** If a table lacks bolded best values, a figure is unreferenced, or the conclusion omits key metrics, fix it or flag it.
4. **Suggest improvements:** If a paragraph is verbose, a transition is missing, or an equation would clarify a concept, suggest the improvement.
5. **Cross-check numbers:** Verify that any metric cited in the abstract, introduction, results, and conclusion are **consistent** across all occurrences.
6. **Check figure quality:** Ensure all figures are high-enough resolution and appropriately sized for a printed IEEE paper.

---

## 15. Source Material

- **Primary source of truth:** The Software Requirements Specification (SRS) documents in this repository.
- **Never hallucinate** features, metrics, or architectural components not present in the codebase or SRS.
- Synthesize SRS content into the academic structure defined above.
