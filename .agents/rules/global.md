# Global Rule: Auto-Commit Source Code Changes

- **Always Commit**: After making any meaningful changes to source code files (e.g., `.tex`, `.sty`, `.py`), you must immediately run `git add` and `git commit` to save the changes.
- **Ignore Build/Debug Files**: Do NOT stage or commit generated, compiled, or auxiliary files. Specifically ignore:
  - LaTeX build files: `.aux`, `.log`, `.out`, `.toc`, `.bbl`, `.blg`, `.fls`, `.fdb_latexmk`
  - Output documents: `.pdf` (unless explicitly requested to commit a final version)
  - System files: `.DS_Store`
  - Other debug, generic `etc`/log files.
- **Commit Messages**: Write a brief, descriptive commit message summarizing the changes made.
