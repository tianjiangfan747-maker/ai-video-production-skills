#!/usr/bin/env python3
"""Flag prompt-redundancy risks without rewriting creative instructions."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

NEGATIVE_PATTERNS = (
    re.compile(r"\b(?:no|without|avoid|exclude|do not|don't)\b(?:\s+[\w'-]+){0,5}", re.I),
    re.compile(r"(?:不要|无需|避免|禁止|不得|不出现|排除|去除)[^，。；;\n]{1,24}"),
)
CAMERA_PATTERNS = {
    "push/dolly in": re.compile(r"\b(?:dolly|push)(?:es|ing)?\s+in\b|推近|推轨", re.I),
    "pull/dolly out": re.compile(r"\b(?:dolly|pull)(?:s|ing)?\s+(?:out|back)\b|拉远", re.I),
    "pan": re.compile(r"\bpan(?:s|ning)?\b|摇镜|摇拍", re.I),
    "tilt": re.compile(r"\btilt(?:s|ing)?\b|俯仰", re.I),
    "orbit": re.compile(r"\borbit(?:s|ing)?\b|环绕", re.I),
    "tracking/follow": re.compile(r"\b(?:tracking shot|camera follows?|follow shot)\b|跟拍|跟随镜头", re.I),
    "lateral/truck": re.compile(r"\b(?:lateral move|truck(?:s|ing)?)\b|横移", re.I),
    "handheld": re.compile(r"\bhandheld\b|手持", re.I),
    "whip pan": re.compile(r"\bwhip[- ]pan\b|甩镜", re.I),
    "crane": re.compile(r"\bcrane(?:s|ing)?\s+(?:up|down)\b|升降镜头", re.I),
    "zoom": re.compile(r"\bzoom(?:s|ing)?\s+(?:in|out)\b|变焦", re.I),
}
QUALITY_PATTERNS = (
    r"\b[48]k\b", r"\bultra[ -]hd\b", r"\b(?:rich|high|ultra)[ -]detail(?:ed)?\b",
    r"\bsharp clarity\b", r"\bphotorealistic\b", r"\bmasterpiece\b",
    r"\bbest quality\b", r"\bcinematic (?:quality|textures)\b",
)
CLAUSE_SPLIT = re.compile(r"[.!?。！？；;\n]+")


def _clause_key(clause: str) -> str:
    return re.sub(r"[^\w\u4e00-\u9fff]+", "", clause.casefold())


def review_prompt(text: str, max_negatives: int = 3) -> dict:
    warnings = []
    negatives = []
    for pattern in NEGATIVE_PATTERNS:
        negatives.extend(match.group(0).strip() for match in pattern.finditer(text))
    if len(negatives) > max_negatives:
        warnings.append({
            "code": "negative-density",
            "message": f"发现 {len(negatives)} 处否定/排除表达。检查是否可由正面描述或参考图覆盖；保留用户明确约束。",
            "evidence": negatives,
        })

    keys = [_clause_key(c) for c in CLAUSE_SPLIT.split(text) if len(_clause_key(c)) >= 6]
    duplicates = sorted(key for key, count in Counter(keys).items() if count > 1)
    if duplicates:
        warnings.append({
            "code": "repeated-clause",
            "message": "发现重复语句。检查资产描述、风格锚点或限制词是否被逐镜/逐句重复。",
            "evidence": duplicates,
        })

    camera_hits = [name for name, pattern in CAMERA_PATTERNS.items() if pattern.search(text)]
    if len(camera_hits) > 1:
        warnings.append({
            "code": "camera-competition",
            "message": "发现多个可能的摄影机行为。若是连续路径，请确认有明确触发和结束态；否则只留主行为或拆镜。",
            "evidence": camera_hits,
        })

    quality_hits = sorted({m.group(0) for pattern in QUALITY_PATTERNS for m in re.finditer(pattern, text, re.I)})
    if len(quality_hits) >= 3:
        warnings.append({
            "code": "quality-tag-stack",
            "message": "发现多个质量标签。优先保留能具体改变画面的一项，删除同义后缀。",
            "evidence": quality_hits,
        })

    return {
        "stats": {
            "characters": len(text),
            "negative_expressions": len(negatives),
            "camera_behaviors": len(camera_hits),
            "quality_tags": len(quality_hits),
        },
        "warnings": warnings,
        "note": "机器检查只提示风险，不判断语义冗余，也不会自动改写。请人工确认必要性、参考图覆盖关系、用户明确排除项和镜头结束态。",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, help="UTF-8 prompt file; omit to read stdin")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--max-negatives", type=int, default=3, help="warning threshold, not an error limit")
    args = parser.parse_args()
    if args.max_negatives < 0:
        parser.error("--max-negatives must be >= 0")
    try:
        text = args.file.read_text(encoding="utf-8") if args.file else sys.stdin.read()
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Unable to read prompt: {exc}\n")
    if not text.strip():
        parser.exit(2, "Prompt is empty.\n")
    result = review_prompt(text, args.max_negatives)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
