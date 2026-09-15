"""Import Xcode's Codex skills, adapting references to this plugin's name."""

import json
from pathlib import Path
import subprocess


root = Path(__file__).resolve().parents[1]
plugin = Path(subprocess.check_output(
    ["xcrun", "agent", "plugin", "path", "--plugin-format", "codex"], text=True
).strip())
source_name = json.loads((plugin / ".codex-plugin/plugin.json").read_text())["name"]
target_name = json.loads((root / ".codex-plugin/plugin.json").read_text())["name"]
source = plugin / "skills"
assert list(source.glob("*/SKILL.md")), f"No skills found in {source}"
for path in sorted(source.rglob("*")):
    target = root / "skills" / path.relative_to(source)
    if path.is_dir():
        target.mkdir(parents=True, exist_ok=True)
        target.chmod(target.stat().st_mode | 0o700)
    elif path.is_file():
        if target.exists():
            target.chmod(target.stat().st_mode | 0o600)
        data = path.read_bytes()
        if path.suffix == ".md":
            data = data.replace(f"{source_name}:".encode(), f"{target_name}:".encode())
        target.write_bytes(data)
        target.chmod(path.stat().st_mode | 0o600)
print(f"Imported {len(list(source.glob('*/SKILL.md')))} skills from {plugin}")
retired = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")} - {
    p.parent.name for p in source.glob("*/SKILL.md")
}
if retired:
    print(f"Review skills absent from this Xcode build: {', '.join(sorted(retired))}")
