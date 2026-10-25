# Aoma Scan Demo — a codebase with planted flaws

A tiny Python app that is **deliberately broken** in ten documented ways:
hardcoded secrets, a SQL injection, an `eval()`, MD5 password hashing, a god
function, dead code, vulnerable pinned dependencies, debug mode left on.

It exists so anyone can verify the **Aoma Risk Scan** actually finds real
problems: run the scan on this repo and compare against
[PLANTED.md](./PLANTED.md) — every planted flaw should show up in the report.
A scan that misses one is a scan that failed. Check us.

Companion repos:
- The scanner: https://github.com/AarmajUS/aoma-risk-scan
- A sample report generated from this repo lives in that repo under `examples/`.

The planted secrets are fake demo values, not real credentials.
