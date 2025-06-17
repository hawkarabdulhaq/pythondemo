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
# Progress constants  ← week 5 changed to 4
# ───────────────────────────────────────────────────────────────
_REQUIRED_TABS = {1: 10, 2: 12, 3: 12, 4: 7, 5: 4}
_TOTAL_REQUIRED = sum(_REQUIRED_TABS.values()) or 1
_WEEK_COLORS = {1: "#27c93f", 2: "#0ff", 3: "#b19cd9", 4: "#ffbd2e", 5: "#f44"}

# ───────────────────────────────────────────────────────────────
# Fetch participants
# ───────────────────────────────────────────────────────────────
def _fetch_participants():
    query = (
        "SELECT u.fullname, u.username, u.date_of_joining, "
        "p.week1track, p.week2track, p.week3track, p.week4track, p.week5track "
        "FROM users u JOIN progress p ON u.username = p.username"
    )
    rows = []
    try:
        with _get_conn() as conn:
            cur = conn.cursor()
            cur.execute(query)
            for full, user, doj, w1, w2, w3, w4, w5 in cur.fetchall():
                weeks = {1: w1 or 0, 2: w2 or 0, 3: w3 or 0, 4: w4 or 0, 5: w5 or 0}
                percent = min(100, round(sum(weeks.values()) / _TOTAL_REQUIRED * 100))
                rows.append({
                    "fullname": full or user,
                    "doj": doj.strftime("%Y-%m-%d") if doj else "N/A",
                    "percent": percent,
                    "weeks": weeks,
                })
    except Error as e:
        st.error(f"Database error: {getattr(e,'msg',e)}")
    return sorted(rows, key=lambda r: (-r["percent"], r["fullname"]))

# ───────────────────────────────────────────────────────────────
# HTML template pieces
# ───────────────────────────────────────────────────────────────
_HTML_TEMPLATE = """
<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
<title>Participants Dashboard</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&display=swap');
:root{--bg1:#0d1117;--bg2:#161b22;--bg3:#21262d;--green:#00ff41;--cyan:#00d4ff;--yellow:#ffcc02;--border:#30363d;
--text:#f0f6fc;--text2:#8b949e;}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#0a0e13;font-family:'JetBrains Mono',monospace;color:var(--text);}
.terminal{width:95%;max-width:1000px;margin:30px auto;background:var(--bg1);border:2px solid var(--green);
border-radius:12px;padding:26px;overflow:visible;}  /* changed here */
.header{display:flex;align-items:center;margin-bottom:22px;padding-bottom:14px;border-bottom:1px solid var(--border);}
.title{color:var(--cyan);font-size:1.6rem;font-weight:700;margin-right:auto;}
.stats{color:var(--text2);font-size:.9rem;}
.divider{border-top:1px solid var(--border);margin:10px 0;}
.participant{padding:10px 0;}
.p-head{display:flex;align-items:center;margin-bottom:8px;}
.p-name{font-size:1rem;font-weight:600;color:var(--yellow);}
.p-doj{font-size:.75rem;color:var(--text2);margin-left:8px;}
.badge{display:flex;align-items:center;background:var(--bg3);padding:4px 10px;border-radius:18px;border:1px solid var(--border);margin-left:auto;}
.pct{font-weight:700;color:var(--green);margin-right:6px;}
.o-bar{width:90px;height:6px;background:var(--bg3);border-radius:3px;overflow:hidden;}
.o-prog{height:100%;background:linear-gradient(90deg,var(--green),var(--cyan));}
.weeks{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:6px;}
.w-item{display:flex;align-items:center;background:var(--bg2);padding:4px 8px;border-radius:5px;border-left:3px solid;}
.w-lbl{font-size:.75rem;margin-right:4px;}
.w-prog{flex:1;height:5px;background:var(--bg1);border-radius:2px;overflow:hidden;margin-right:4px;}
.w-bar{height:100%;border-radius:2px;}
.w-count{font-size:.7rem;color:var(--text2);}
.no-data{text-align:center;color:var(--text2);margin:40px 0;font-style:italic;}
</style></head><body><div class=\"terminal\"><div class=\"header\">
<div class=\"title\">⚡ Participants</div><div class=\"stats\">{{STATS}}</div></div>{{ROWS}}</div></body></html>"""

def _week_row(num, done):
    req = _REQUIRED_TABS[num] or 1
    pct = min(100, round(done / req * 100))
    color = _WEEK_COLORS.get(num, "#00d4ff")
    return (
        f'<div class="w-item" style="border-left-color:{color};">'
        f'<span class="w-lbl" style="color:{color};">W{num}</span>'
        f'<div class="w-prog"><div class="w-bar" style="background:{color};width:{pct}%;"></div></div>'
        f'<span class="w-count">{done}/{req}</span></div>'
    )

def _rows_html(data):
    if not data:
        return "<p class='no-data'>No participants found.</p>"
    rows = []
    for p in data:
        weeks = "".join(_week_row(k, v) for k, v in p["weeks"].items() if _REQUIRED_TABS[k])
        rows.append(
            f'<div class="participant">'
            f'<div class="p-head"><span class="p-name">{p["fullname"]}</span>'
            f'<span class="p-doj">{p["doj"]}</span>'
            f'<div class="badge"><span class="pct">{p["percent"]}%</span>'
            f'<div class="o-bar"><div class="o-prog" style="width:{p["percent"]}%"></div></div></div></div>'
            f'<div class="weeks">{weeks}</div></div><div class="divider"></div>'
        )
    return "\n".join(rows)

# ───────────────────────────────────────────────────────────────
# Main display
# ───────────────────────────────────────────────────────────────
def show():
    participants = _fetch_participants()
    avg = sum(p["percent"] for p in participants) / len(participants) if participants else 0
    stats = f"👥 {len(participants)} | Avg {avg:.1f}%"
    html_out = _HTML_TEMPLATE.replace("{{STATS}}", stats).replace("{{ROWS}}", _rows_html(participants))
    
    total_height = 300 + len(participants) * 70
    html(html_out, height=total_height, scrolling=False)

if __name__ == "__main__":
    show()
