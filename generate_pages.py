import os
import json

root_dir = "./"
pages = []

def should_exclude_md(relative_path: str) -> bool:
    parts = relative_path.replace("\\", "/").split("/")
    if any(p.startswith("_") or p.startswith(".") for p in parts):
        return True

    abs_path = os.path.join(root_dir, relative_path)
    try:
        with open(abs_path, "r", encoding="utf-8") as f:
            first_line = f.readline()
            if first_line.strip() != "---":
                return False
            for line in f:
                s = line.strip()
                if s == "---":
                    break
                if s.lower() == "exclude_from_pages_json: true":
                    return True
    except Exception:
        return False

    return False

for root, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            relative_path = os.path.relpath(os.path.join(root, file), root_dir)
            if should_exclude_md(relative_path):
                continue
            pages.append(relative_path.replace("\\", "/"))

with open(os.path.join(root_dir, "pages.json"), "w") as f:
    json.dump({"pages": pages}, f, indent=2)

print("pages.json updated!")
