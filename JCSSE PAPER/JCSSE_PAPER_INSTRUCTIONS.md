# JCSSE Paper Implementation Instructions

These are the strict guidelines for editing and generating content for the JCSSE paper. You must read and follow these rules before implementing any changes to the LaTeX files.

## 1. Document Format & Syntax
- **Template:** The primary writing surface is `conference_101719.tex`.
- **Standards:** All LaTeX code, formatting, and syntax must strictly adhere to the guidelines provided in the IEEEtran HOWTO (`IEEEtran_HOWTO.pdf`).
- Do not use any unauthorized packages or alter the structural commands defined in the IEEEtran class unless explicitly necessary and compliant with IEEE guidelines. 
- Use standard IEEE styling for figures, tables, and citations (e.g., Fig. 1, Table I, [1]).

## 2. Document Outline
The layout of the paper must map exactly to the approved outline. When generating or editing content, make sure it falls within one of these specific sections and sub-sections, while adhering to the approximate page limitations:

**I. INTRODUCTION (~0.75 pages)**
- a. Background and Motivation
- b. Problem Statement
- c. Main Contributions

**II. RELATED WORK (~0.50 pages)**
- a. Existing Solutions
- b. AI Techniques in Video Analytics

**III. DATASET AND METHODOLOGY (~0.50 pages)**
- a. Data Source and Collection
- b. Data Preprocessing and Annotation
- c. Ethical Considerations

**IV. PROPOSED SYSTEM ARCHITECTURE (~2.0 pages)**
- a. System Overview
- b. AI/ML Module Design
- c. Backend and Video Processing Pipeline
- d. Frontend and Analytics Dashboard

**V. EXPERIMENTAL RESULTS AND DISCUSSIONS (~1.5 pages)**
- a. Experimental Setup and Evaluation Metrics
- b. AI Model Performance
- c. System Performance and Scalability
- d. Case Study

**VI. CONCLUSION AND FUTURE WORK (~0.50 pages)**
- a. Conclusion
- b. Future Work

## 3. Source Material (CRITICAL)
- **Primary Source:** Always use the Software Requirements Specification (SRS) documents located within this repository as the fundamental source of truth for all factual information, system details, architectural descriptions, and methodology.
- Do not hallucinate or invent features, performance metrics, or architectural components that do not exist within the project's codebase or SRS context. 
- Synthesize and map the relevant sections of the SRS into the academic outline structure seamlessly.

## 4. Writing Style & Best Practices for JCSSE
- **Tone:** Maintain a highly formal, objective, and academic tone consistent with IEEE and JCSSE (Joint Conference on Computer Science and Software Engineering) standards. 
- **Voice:** Avoid colloquialisms, jargon (unless strictly defined), and excessively marketing-driven language. Favor objective phrasing and focus purely on technical merit, scientific contribution, and objective evaluation.
- **Clarity & Conciseness:** Be direct and concise. Clearly state the problem, the methodology, and the results without unnecessary fluff.
- **Flow:** Ensure transitions between sections and paragraphs naturally follow a logical technical narrative. Connect the "Background" to the "Proposed System" and justify design choices objectively.
- **Terminology:** Use rigorous and precise technical terminology consistent with software engineering, computer vision, and artificial intelligence domains.
- **Formatting:** Ensure that the total content aligns with the page distributions provided in the outline, avoiding excessively long "wall-of-text" paragraphs. Ensure figures and tables are introduced properly in the text.
