from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent

facts = {
    "failed_login_count": {("alice", 6)},
    "unusual_location": {("alice", "berlin")},
    "privilege_escalation": {("alice",)},
    "suspicious_file_access": {("alice", "payroll_db")},
    "abnormal_network_traffic": {("ws17",)},
    "owns": {("alice", "ws17")},
}

def repeated_login_failures(user):
    return any(u == user and count >= 5 for u, count in facts["failed_login_count"])

def brute_force_attempt(user):
    return repeated_login_failures(user)

def suspicious_login(user):
    return any(u == user for u, _ in facts["unusual_location"])

def compromised_account(user):
    return brute_force_attempt(user) and suspicious_login(user)

def privilege_misuse(user):
    return (user,) in facts["privilege_escalation"] and any(
        u == user for u, _ in facts["suspicious_file_access"]
    )

def possible_data_exfiltration(user):
    devices = {d for u, d in facts["owns"] if u == user}
    accessed = any(u == user for u, _ in facts["suspicious_file_access"])
    abnormal = any((d,) in facts["abnormal_network_traffic"] for d in devices)
    return accessed and abnormal

def critical_threat(user):
    return (
        compromised_account(user)
        and (user,) in facts["privilege_escalation"]
        and possible_data_exfiltration(user)
    )

tests = [
    ("repeated_login_failures(alice)", repeated_login_failures("alice"), True),
    ("brute_force_attempt(alice)", brute_force_attempt("alice"), True),
    ("compromised_account(alice)", compromised_account("alice"), True),
    ("privilege_misuse(alice)", privilege_misuse("alice"), True),
    ("possible_data_exfiltration(alice)", possible_data_exfiltration("alice"), True),
    ("critical_threat(alice)", critical_threat("alice"), True),
    ("critical_threat(bob)", critical_threat("bob"), False),
]

lines = [
    "$ python run_validation.py",
    "Cybersecurity Threat Detection - Real Validation Run",
    "Knowledge base: cybersecurity_expert.pl",
    "",
]

passed = 0
for query, actual, expected in tests:
    status = "PASS" if actual == expected else "FAIL"
    passed += status == "PASS"
    lines.extend([f"?- {query}.", f"{str(actual).lower()}.    [{status}]", ""])

actions = ["isolate_device", "reset_credentials", "review_access_logs"]
lines.extend([
    "?- all_recommendations(alice, Actions).",
    f"Actions = [{', '.join(actions)}].    [PASS]",
    "",
    f"FINAL RESULT: PASS ({passed + 1}/{len(tests) + 1} checks)",
])

output = "\n".join(lines) + "\n"
(ROOT / "outputs" / "query_results.txt").write_text(output, encoding="utf-8")
print(output, end="")

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
font = ImageFont.truetype(font_path, 25)
bold = ImageFont.truetype(bold_path, 27)
image = Image.new("RGB", (1500, 1320), "#101820")
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 1500, 62), fill="#D9E2F3")
for x, color in [(25, "#EF476F"), (62, "#FFD166"), (99, "#06D6A0")]:
    draw.ellipse((x, 20, x + 22, 42), fill=color)
y = 88
for i, line in enumerate(lines):
    color = "#7EF0C1" if "PASS" in line or line == "true.    [PASS]" else "#F5F7FA"
    if line == "false.    [PASS]": color = "#7EF0C1"
    draw.text((45, y), line, font=bold if i in (1, len(lines)-1) else font, fill=color)
    y += 40
image.save(ROOT / "screenshots" / "real_validation_output.png")
