# JCSSE Paper Revision Tasks

This document summarizes the feedback from the professor regarding the JCSSE paper revision, categorized by actionability.

## Part A: Able to fix right now by vibe writing
*Textual explanations, formatting, and text alignments we can implement directly in the LaTeX.*

*   [x] **Section III.D (Mapping Strategy) - CRITICAL**: Significantly expand to clarify the geometric identity solution. explicitly define `Xc`, `Ymax`, `pmap`, and `pimg`. Write a concrete walkthrough.
*   [x] **Experiment Setup (Baseline)**: Clearly define the baseline model and justify why it was chosen.
*   [x] **Dataset Description**: Include descriptions for specific camera IDs used in results (e.g., c09, c12, ..., c05).
*   [x] **Tables I, II, and III**: Remove the "Gain" column from all three tables.
*   [x] **References (Ordering)**: Re-order all references to reflect their exact order of appearance.
*   [x] **Results Reporting Justification (New)**: Explain why results are reported per-camera (c09, c12) instead of only global averages. *(Integrated in Section IV Introduction)*
*   [x] **Deployment Mention (New)**: Explicitly state that an app was created to connect all analytical processes and measure results. *(Integrated by Prof in Section III.A)*
*   [x] **Broader Introduction Scope (New)**: Rewrite the first two paragraphs of the introduction to discuss the importance of multi-camera tracking in general real-world applications (smart cities, retail) before diving into the specific factory/campus scenarios. *(Integrated in Section I)*

## Part B: Need manual input (Images/Diagrams from you)
*Tasks requiring new or modified graphics/diagrams to be created and provided by you.*

*   [x] **New System Overview Diagram (New Fig. 1)**: Create a new diagram for Section III.A (System Overview) with 4 main boxes. *(Implemented via custom left-to-right TikZ flowchart in `spoton_architecture.tex`)*
*   [ ] **Fix Figure 5 Y-Axis (New)**: Adjust the maximum y-axis value of Figure 5 (`ablation_figure_5.png`) to exactly 40. You will need to regenerate this plot from your script.
*   [x] **Modified Deployment Diagram (Old Fig. 1)**: Redesign the original deployment figure to represent workflow steps using boxes. Place the tool names/logos *outside/next to* the boxes. *(Integrated into Section 3.1)*

## Part C: Need to wait for the professor / action required
*Tasks the professor is handling, thinking about, or requiring external action.*

*   [x] **Introduction & Restructuring**: The professor rewritten the Introduction and structure. *(We have successfully integrated her provided LaTeX base)*
*   [x] **Deployment Status (Local vs. Actual)**: The professor noted the text might need to reflect local run. *(Resolved via the new Deployment Mention in III.A)*
*   [ ] **Conference Submission System Testing**: The professor requested you (เจ) try logging into the submission system and do a test submission to check for any automated format validation errors.
