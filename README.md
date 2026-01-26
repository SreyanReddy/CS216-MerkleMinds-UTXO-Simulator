# CS216-MerkleMinds-UTXO-Simulator
This project simulates a simplified blockchain transaction system using the UTXO model, including transaction validation, mempool management, and block mining. It demonstrates key blockchain concepts such as double-spend prevention and ledger state transitions.

## Team Git Workflow (IMPORTANT)

### Branches
- `main` = stable/submission-ready only (protected)
- `dev` = integration branch (all work merges here first)
- `feature/*` = individual work branches (one task per branch)

### Rules
-  Never commit directly to `main`
-  Never merge your own PR without at least 1 review
-  All code changes must go through a Pull Request (PR)
-  Feature branches must be created from `dev` and merged back into `dev`
-  Only the organizer merges `dev` → `main` (release/submission)

### Standard workflow (for every team member)
1. Update local `dev`:
   git checkout dev
   git pull origin dev
2. Create a feature branch:
   git checkout -b feature/<task>-<initials>
3. Work + commit:
   git add .
   git commit -m "feat: <message>"
4. Push the feature branch:
   git push -u origin feature/<task>
5. Open a PR on GitHub:
   Base branch: dev
   Compare branch: your feature/<task>-<initials>
6. After approval + passing checks, merge PR into dev.
   