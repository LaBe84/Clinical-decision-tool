# Tests and evals

## Four distinct assurance layers

- **Architecture tests:** repository state, provenance and dependency contracts.
- **Reasoning regression tests:** forbidden reasoning moves in controlled case prompts.
- **Policy-conformance tests:** exact organisational procedure/threshold checks once controlled sources are verified.
- **Evals:** quality of nuanced clinical reasoning.

The concrete draft contracts are in [canonical-reasoning-regression-spec.md](canonical-reasoning-regression-spec.md). A passing test suite is necessary but not sufficient for live use: all mandatory contracts must pass, and any exception must be documented, clinically reviewed and approved.

## Run the architecture checks

From the repository root:

```bash
python3 -m unittest tests/test_canonical_contracts.py
```

These checks verify repository-level architectural contracts: dependency declarations, draft status, contract registration and organisational-source boundaries. They do not assess a model’s clinical reasoning against scenarios.
