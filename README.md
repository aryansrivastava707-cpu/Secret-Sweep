# Portfolio Projects — Remaining Set

Ten independent repositories to fill the remaining portfolio slots. The live portfolio had 2 Web Development, 1 AI & ML, 1 Cybersecurity, and 1 IoT & Hardware project. After counting the five earlier projects already delivered (Git Archaeologist, Typing Fingerprint, TinyRAG, Gene Timetable, and Log Sentinel), this set adds the remaining 2 Web, 2 AI/ML, 2 Cybersecurity, and 4 IoT projects to reach five per category.

## Projects by portfolio category

### Web Development
- [Campus Resource Booker](campus-resource-booker/) — React and TypeScript interface with a Python and SQLite booking API.
- [Markdown Studio](markdown-studio/) — Node.js static publisher for Markdown notes.

### AI & ML
- [Explainable Risk Lab](explainable-risk-lab/) — small logistic regression model with feature contribution explanations.
- [Topic Cluster Lab](topic-cluster-lab/) — TF-IDF and k-means document grouping.

### Cybersecurity
- [Secret Sweep](secret-sweep/) — local scanner for common credential patterns with redacted findings.
- [Security Header Auditor](security-header-auditor/) — explainable HTTP security header review.

### IoT & Hardware
- [Irrigation Guardian](irrigation-guardian/) — moisture threshold controller with fail-safe behavior.
- [Coldchain Beacon](coldchain-beacon/) — temperature/humidity alarm logic and MicroPython firmware.
- [BinWatch Edge](binwatch-edge/) — ultrasonic fill-level estimation with outlier resistance.
- [Solar Pulse Meter](solar-pulse-meter/) — pulse-based power and energy estimation.

## Repository setup

Each project folder is a standalone repository. Open a terminal inside one folder, create a GitHub repository with the same project name, then initialize, commit, add the remote URL GitHub shows, and push. Each project README contains its own stack, setup, usage, tests, and limitations.

## Notes

- Python projects use local or synthetic test data. Markdown Studio uses Node.js; Campus Resource Booker includes a React/TypeScript frontend.
- Hardware projects include host-side simulators and logic tests. Physical sensor behavior has not been verified.
- Keep `.gitignore` in each GitHub repository; it prevents caches, generated output, local databases, and dependencies from being committed. Documentation and example data are part of the repository when included in the project folder.
- No `node_modules`, `.git`, Python cache folders, generated site output, local databases, or test reports are included in the ZIP.
