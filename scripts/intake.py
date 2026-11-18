"""Create and check a local catalogue issue draft."""
import argparse
import json
from pathlib import Path

common = {"title": ""}
templates = {
    "bug": dict(common, location="", expected="", observed="", model_id=None, revision=None),
    "improvement": dict(common, location="", proposal="", model_id=None),
    "model": dict(common, subject="", description="", tags=[], sources=[], material=None,
                  standards=None, previews=[], rights_evidence=None),
    "subject": dict(common, parent="", aliases=[], examples=[]),
}
required = {
    "bug": ("title", "location", "expected", "observed"),
    "improvement": ("title", "location", "proposal"),
    "model": ("title", "subject", "description"),
    "subject": ("title", "parent"),
}
parser = argparse.ArgumentParser()
parser.add_argument("command", choices=["new", "check"])
parser.add_argument("value")
args = parser.parse_args()
if args.command == "new":
    if args.value not in templates:
        parser.error("choose bug, improvement, model, or subject")
    print(json.dumps(dict(type=args.value, **templates[args.value]), indent=2))
else:
    draft = json.loads(Path(args.value).read_text())
    kind = draft.get("type")
    if kind not in templates:
        parser.error("type must be bug, improvement, model, or subject")
    absent = [key for key in required[kind] if not isinstance(draft.get(key), str) or not draft[key].strip()]
    if absent:
        parser.error("fill in: " + ", ".join(absent))
    print("Draft structure valid. Submit to the catalogue maintainer for triage.")
