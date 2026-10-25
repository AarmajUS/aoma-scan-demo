"""Helpers — some alive, some long dead."""
import hashlib


def hash_password(pw):
    # PLANTED: weak hash for passwords (MD5)
    return hashlib.md5(pw.encode()).hexdigest()


def format_money(cents):
    return f"${cents / 100:,.2f}"


# PLANTED: dead code — nothing in the repo calls these three functions.
def old_invoice_exporter_v1(rows):
    return "\n".join(str(r) for r in rows)


def old_invoice_exporter_v2(rows):
    return ",".join(str(r) for r in rows)


def deprecated_tax_lookup(zip_code):
    return {"08618": 0.06625}.get(zip_code, 0.07)
