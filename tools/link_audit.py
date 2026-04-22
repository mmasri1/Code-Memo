import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HTML_HREF_RE = re.compile(r'href\s*=\s*"([^"]+)"', re.IGNORECASE)


def _normalize_target(raw: str) -> str | None:
    raw = raw.strip()
    if re.match(r"^(mailto:|tel:|javascript:)", raw, re.IGNORECASE):
        return None

    # common markdown autolink style: (<...>)
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]

    # remove fragment/query for file existence checks
    if "#" in raw:
        raw = raw.split("#", 1)[0]
    if "?" in raw:
        raw = raw.split("?", 1)[0]

    return raw


def _is_external(target: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", target))


def _collect_files(root: Path) -> dict[str, Path]:
    return {
        str(p.relative_to(root)).replace("\\", "/"): p
        for p in root.rglob("*")
        if p.is_file()
    }


def _exists_repo_root_relative(all_files: dict[str, Path], target: str) -> bool:
    cand = target.lstrip("/")
    if cand in all_files:
        return True
    if (cand + ".md") in all_files:
        return True
    if cand.endswith("/") and (cand + "index.md") in all_files:
        return True
    return False


def _exists_file_relative_to(root: Path, all_files: dict[str, Path], base: Path, target: str) -> bool:
    candidate_path = (base / target).resolve()
    try:
        candidate_rel = str(candidate_path.relative_to(root)).replace("\\", "/")
    except ValueError:
        return False

    if candidate_rel in all_files:
        return True
    if (candidate_rel + ".md") in all_files:
        return True
    if candidate_path.is_dir() and (candidate_path / "index.md").exists():
        return True
    return False


def audit(root: Path) -> list[tuple[str, str, str]]:
    all_files = _collect_files(root)
    md_files = [p for p in root.rglob("*.md") if ".git" not in p.parts]
    broken: list[tuple[str, str, str]] = []

    for f in md_files:
        text = f.read_text(encoding="utf-8", errors="ignore")
        rel = str(f.relative_to(root)).replace("\\", "/")

        for m in MARKDOWN_LINK_RE.finditer(text):
            # skip images ![...](...)
            if m.start() > 0 and text[m.start() - 1] == "!":
                continue

            target_raw = m.group(2).strip()
            target = _normalize_target(target_raw)
            if target is None:
                continue

            if target == "" or target.startswith("#"):
                continue

            if _is_external(target):
                continue

            if target.startswith("/"):
                if not _exists_repo_root_relative(all_files, target):
                    broken.append((rel, m.group(0), f"missing internal target: {target}"))
                continue

            if not _exists_file_relative_to(root, all_files, f.parent, target):
                broken.append((rel, m.group(0), f"missing relative target: {target}"))

        for m in HTML_HREF_RE.finditer(text):
            target_raw = m.group(1).strip()
            target = _normalize_target(target_raw)
            if target is None:
                continue

            if target == "" or target.startswith("#") or _is_external(target):
                continue

            if target.startswith("/"):
                if not _exists_repo_root_relative(all_files, target):
                    broken.append((rel, f'href=\"{target_raw}\"', f"missing internal href: {target}"))
                continue

            if not _exists_file_relative_to(root, all_files, f.parent, target):
                broken.append((rel, f'href=\"{target_raw}\"', f"missing relative href: {target}"))

    return broken


def main() -> int:
    broken = audit(ROOT)
    md_count = len([p for p in ROOT.rglob("*.md") if ".git" not in p.parts])

    print(f"Scanned {md_count} markdown files")
    print(f"Broken internal links found: {len(broken)}")
    for rel, snippet, reason in broken[:200]:
        print(f"- {rel} :: {snippet} => {reason}")
    if len(broken) > 200:
        print(f"... ({len(broken) - 200} more)")

    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())

