import streamlit as st
import mysql.connector
from mysql.connector import Error
from streamlit.components.v1 import html

# ───────────────────────────────────────────────────────────────
# Database helper
# ───────────────────────────────────────────────────────────────

def _get_conn():
    cfg = st.secrets["mysql"]
    return mysql.connector.connect(
        host=cfg["host"],
        port=int(cfg.get("port", 3306)),
        user=cfg["user"],
        password=cfg["password"],
        database=cfg["database"],
        autocommit=False,
    )

# ───────────────────────────────────────────────────────────────
# Progress constants
# ───────────────────────────────────────────────────────────────

_REQUIRED_TABS = {1: 10, 2: 12, 3: 12, 4: 7, 5: 0}
_TOTAL_REQUIRED = sum(_REQUIRED_TABS.values()) or 1
_WEEK_COLORS = {1: "#27c93f", 2: "#0ff", 3: "#b19cd9", 4: "#ffbd2e", 5: "#f44"}

# ───────────────────────────────────────────────────────────────
# Fetch participants & progress
# ───────────────────────────────────────────────────────────────

def _fetch_participants():
    query = (
        "SELECT u.fullname, u.username, u.date_of_joining, "
        "       p.week1track, p.week2track, p.week3track, p.week4track, p.week5track "
        "FROM users u JOIN progress p ON u.username = p.username"
    )
    rows = []
    try:
        with _get_conn() as conn:
            cur = conn.cursor()
            cur.execute(query)
            for fullname, username, doj, w1, w2, w3, w4, w5 in cur.fetchall():
                weeks = {1: w1 or 0, 2: w2 or 0, 3: w3 or 0, 4: w4 or 0, 5: w5 or 0}
                percent = round(sum(weeks.values()) / _TOTAL_REQUIRED * 100)
                rows.append({
                    "fullname": fullname or username,
                    "username": username,
                    "doj": doj.strftime("%Y-%m-%d") if doj else "N/A",
                    "percent": percent,
                    "weeks": weeks,
                })
    except Error as e:
        st.error(f"Database error: {getattr(e,'msg',e)}")
    return sorted(rows, key=lambda r: (-r["percent"], r["fullname"]))

# ───────────────────────────────────────────────────────────────
# HTML helpers
# ───────────────────────────────────────────────────────────────

_HTML_TEMPLATE = """<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width,initial-scale=1.0'><style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&display=swap');:root{--bg1:#0d1117;--bg2:#161b22;--bg3:#21262d;--green:#00ff41;--cyan:#00d4ff;--yellow:#ffcc02;--text:#f0f6fc;--text2:#8b949e;--border:#30363d;}*{margin:0;padding:0;box-sizing:border-box;}body{background:#0d1117;font-family:'JetBrains Mono',monospace;color:var(--text);padding:0 10px;} .terminal{width:100%;background:var(--bg1);border:2px solid var(--green);border-radius:12px;padding:30px;overflow:auto;} .header{display:flex;align-items:center;margin-bottom:20px;border-bottom:1px solid var(--border);padding-bottom:10px;} .title{color:var(--cyan);font-size:1.6rem;font-weight:700;} .stats{margin-left:auto;color:var(--text2);font-size:.9rem;} .divider{border-top:1px solid var(--border);margin:12px 0;} .participant{margin:12px 0;} .p-head{display:flex;align-items:center;justify-content:space-between;} .p-name{color:var(--yellow);font-weight:600;} .p-doj{color:var(--text2);font-size:.8rem;margin-left:8px;} .badge{display:flex;align-items:center;background:var(--bg3);padding:4px 10px;border-radius:16px;border:1px solid var(--border);} .pct{color:var(--green);font-weight:700;margin-right:6px;} .o-bar{width:90px;height:6px;background:var(--bg2);border-radius:3px;overflow:hidden;} .o-prog{height:100%;background:linear-gradient(90deg,var(--green),var(--cyan));} .weeks{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:6px;margin-top:6px;} .w-item{display:flex;align-items:center;background:var(--bg2);padding:4px;border-radius:4px;border-left:3px solid;} .w-lbl{font-size:.75rem;margin-right:4px;} .w-barbox{flex:1;height:4px;background:var(--bg3);margin-right:4px;border-radius:2px;overflow:hidden;} .w-bar{height:100%;} .w-count{font-size:.7rem;color:var(--text2);} .no-data{text-align:center;color:var(--text2);} </style></head><body><div class='terminal'><div class='header'><div class='title'>⚡ Participants</div><div class='stats'>{{STATS}}</div></div>{{ROWS}}</div></body></html>"""


def _week_html(week, done):
    req = _REQUIRED_TABS.get(week, 1)
    pct = int(done / req * 100) if req else 0
    color = _WEEK_COLORS.get(week, "#00d4ff")
    return (
        f"<div class='w-item' style='border-left-color:{color};'>"
        f"<span class='w-lbl' style='color:{color};'>W{week}</span>"
        f"<div class='w-barbox'><div class='w-bar' style='background:{color};width:{pct}%;'></div></div>"
        f"<span class='w-count'>{done}/{req}</span></div>"
    )


def _build_rows(parts):
    if not parts:
        return "<p class='no-data'>No participants found.</p>", "0"
    stats = f"👥 {len(parts)} | 📊 {sum(p['percent'] for p in parts)/len(parts):.1f}% avg"
    rows = []
    for p in parts:
        weeks_html = "".join(_week_html(w, c) for w, c in p["weeks"].items() if _REQUIRED_TABS[w])
        rows.append(
            f"<div class='participant'>"
            f"<div class='p-head'><span class='p-name'>{p['fullname']}</span><span class='p-doj'>({p['doj']})</span>"
            f"<div class='badge'><span class='pct'>{p['percent']}%</span>"
            f"<div class='o-bar'><div class='o-prog' style='width:{p['percent']}%;'></div></div></div></div>"
            f"<div class='weeks'>{weeks_html}</div></div><div class='divider'></div>"
        )
    return "\n".join(rows), stats

# ───────────────────────────────────────────────────────────────
# Streamlit entrypoint
# ───────────────────────────────────────────────────────────────

def show():
    parts = _fetch_participants()
    rows_html, stats = _build_rows(parts)
    html_doc = _HTML_TEMPLATE.replace("{{ROWS}}", rows_html).replace("{{STATS}}", stats)
    # Full‑width component; height scales with participants - removed scrolling
    html(html_doc, height=min(1000, 260 + len(parts) * 60), width=1400)


if __name__ == "__main__":
    show()
