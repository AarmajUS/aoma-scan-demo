"""Demo app for the Aoma Risk Scan — intentionally flawed. See PLANTED.md."""
import os
import sqlite3

import requests

# PLANTED: hardcoded secrets (should be caught by the secrets scanner)
STRIPE_API_KEY = "sk_live_DEMO-KEY-NOT-A-REAL-KEY"
DATABASE_PASSWORD = "hunter2-demo-password"

app_debug = True  # PLANTED: debug mode left on


def get_user(user_id):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    # PLANTED: SQL injection — user input formatted straight into the query
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cur.execute(query)
    return cur.fetchone()


def run_user_formula(formula):
    # PLANTED: eval() on untrusted input
    return eval(formula)


def notify(url):
    # Uses the pinned, outdated requests library (see requirements.txt)
    return requests.get(url, timeout=5)


def legacy_discount_engine(user, cart, coupon, region, tier, season,
                           promo, tax_table, shipping, loyalty):
    """PLANTED: god function — deeply branched, does everything at once."""
    total = 0
    for item in cart:
        price = item["price"]
        if tier == "gold":
            if season == "holiday":
                if promo:
                    price *= 0.7
                else:
                    price *= 0.8
            else:
                if coupon:
                    price *= 0.85
                else:
                    price *= 0.9
        elif tier == "silver":
            if region == "NJ":
                if loyalty:
                    price *= 0.88
                else:
                    price *= 0.95
            else:
                price *= 0.97
        else:
            if cart and len(cart) > 5:
                price *= 0.99
            elif user.get("new"):
                price *= 0.95
        if shipping == "express":
            total += price + 12
        elif shipping == "overnight":
            total += price + 24
        else:
            total += price
        if tax_table:
            total += price * tax_table.get(region, 0)
    if total > 1000:
        total *= 0.98
    elif total > 500:
        total *= 0.99
    elif total > 100:
        total *= 0.995
    return round(total, 2)
