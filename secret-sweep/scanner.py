import hashlib,math,re
from pathlib import Path
RULES=[("aws-access-key",re.compile(r"\bAKIA[0-9A-Z]{16}\b")),("github-token",re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b")),("private-key",re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),("generic-secret",re.compile(r"(?i)(?:api[_-]?key|secret|access[_-]?token)\s*[:=]\s*['\"]?([A-Za-z0-9_./+=-]{20,})"))]
SKIP_DIRS={".git","node_modules",".venv","venv","dist","build","__pycache__"}

def fingerprint(value):return hashlib.sha256(value.encode()).hexdigest()[:16]
def entropy(value):
    if not value:return 0.0
    return -sum((value.count(c)/len(value))*math.log2(value.count(c)/len(value)) for c in set(value))
def _match(rule,match):
    if rule=="generic-secret":return match.group(1) if match.lastindex else match.group(0)
    return match.group(0)
def scan_text(text,path="<memory>",allowlist=()):
    findings=[];allowed=set(allowlist)
    for line_no,line in enumerate(text.splitlines(),1):
        if "secret-sweep: ignore" in line:continue
        for rule,pattern in RULES:
            for match in pattern.finditer(line):
                secret=_match(rule,match);fp=fingerprint(secret)
                if fp in allowed:continue
                findings.append({"path":str(path),"line":line_no,"rule":rule,"fingerprint":fp,"redacted":"[REDACTED]"})
        for token in re.findall(r"(?<![A-Za-z0-9])[A-Za-z0-9_+/=-]{28,}(?![A-Za-z0-9])",line):
            if entropy(token)>=4.1:
                fp=fingerprint(token)
                if fp not in allowed and not any(f["line"]==line_no and f["fingerprint"]==fp for f in findings):
                    findings.append({"path":str(path),"line":line_no,"rule":"high-entropy-string","fingerprint":fp,"redacted":"[REDACTED]"})
    return findings

def scan_tree(root,allowlist=(),max_bytes=1_000_000):
    root=Path(root);findings=[]
    if not root.exists():raise FileNotFoundError(root)
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.relative_to(root).parts) or path.stat().st_size>max_bytes:continue
        try:text=path.read_text(encoding="utf-8")
        except (UnicodeDecodeError,OSError):continue
        findings.extend(scan_text(text,path.relative_to(root),allowlist))
    return findings
