# What's planted in this repo (public on purpose)

This demo exists so anyone can verify that the Aoma Risk Scan actually finds
real problems. Every flaw below is deliberate. A scan report that misses one
is a scan that failed — check us.

| # | Flaw | Where | Should be caught by |
|---|------|-------|---------------------|
| 1 | Hardcoded Stripe-style live key | `app.py` | Secrets scan (Gitleaks) |
| 2 | Hardcoded database password | `app.py` | Secrets scan (Gitleaks) |
| 3 | AWS-style secret key in committed config | `config.py` | Secrets scan (Gitleaks) |
| 4 | SQL injection (string-formatted query) | `app.py` `get_user` | Pattern scan (Semgrep) |
| 5 | `eval()` on untrusted input | `app.py` `run_user_formula` | Pattern scan (Semgrep) |
| 6 | MD5 password hashing | `utils.py` `hash_password` | Pattern scan (Semgrep) |
| 7 | God function, extreme branching | `app.py` `legacy_discount_engine` | Graph analysis (CodeGraphContext complexity) |
| 8 | Dead code — 3 uncalled functions | `utils.py` | Graph analysis (CodeGraphContext dead-code) |
| 9 | Vulnerable pinned dependencies (requests 2.19.1, pyyaml 5.1, flask 2.0.1) | `requirements.txt` | Dependency scan (OSV-Scanner) |
| 10 | Debug mode enabled | `app.py`, `config.py` | Pattern scan (Semgrep) / report note |

The secrets above are **fake demo values** — they are not real credentials
for anything. Two of them are softened stand-ins (marked DEMO) because GitHub's push
protection refuses to publish *any* format-valid Stripe-style key — even
the well-known documentation example, even with DEMO in it (we tried both;
GH013 blocked both). Our local verification ran the original full-format
documentation example and the dedicated secrets rule caught it
(gitleaks: stripe-access-token). In this published copy, the Stripe-style
value is deliberately format-broken and is caught by the scan's pattern
layer (hardcoded-secret rule) in the same position.
