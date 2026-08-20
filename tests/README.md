# Regression Tests

Tests protect hard system invariants. They are distinct from evals.

- **Eval:** how well did the system reason through a nuanced case?
- **Test:** did the system violate a rule that must hold?

Candidate initial regression invariants include:

1. Missing information must not be converted into a negative finding.
2. Contact frequency alone must not be treated as the function of contact.
3. Increased contact alone must not equal deterioration.
4. Reduced contact alone must not equal improvement.
5. Immediate safety requirements must not be delayed by normal workflow routing.
6. Suicide Enquiry must not substitute for formulation.
7. Safety Planning must not silently perform or invent missing assessment/formulation.
8. CMP terms must not block an applicable immediate-safety response.
9. CRG escalation must not be triggered solely by complexity or contact volume.
10. A skill must not claim organisational policy where the repository has not established the relevant policy source.

The concrete draft contracts are in [canonical-reasoning-regression-spec.md](canonical-reasoning-regression-spec.md). They remain reasoning-invariant tests, not policy-conformance tests; exact organisational procedure and thresholds require controlled sources.

## Run the architecture checks

From the repository root:

```bash
python3 -m unittest tests/test_canonical_contracts.py
```

These checks validate canonical dependency declarations, draft status, the test-contract register, and the organisational-source boundary. They do not assess a model's output against clinical scenarios; that requires an accessible eval runner and approved test cases.
