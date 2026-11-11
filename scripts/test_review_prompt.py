#!/usr/bin/env python3
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from review_prompt import review_prompt


class ReviewPromptTests(unittest.TestCase):
    def test_clean_prompt_has_no_warning(self):
        result = review_prompt("人物走向窗边，镜头贴近右肩跟随；门框短暂遮挡后露出高塔，人物停步，镜头停在越肩中景。")
        self.assertEqual(result["warnings"], [])

    def test_explicit_necessary_constraints_remain_untouched(self):
        text = "镜头缓慢推近，人物停下。不要字幕，不要BGM，不要乱码。"
        result = review_prompt(text)
        self.assertEqual(result["stats"]["negative_expressions"], 3)
        self.assertNotIn("negative-density", {w["code"] for w in result["warnings"]})
        self.assertIn("不要字幕", text)

    def test_excess_negatives_warn_without_deleting(self):
        text = "No subtitles. No BGM. No watermark. No logo. Avoid clutter."
        result = review_prompt(text)
        self.assertEqual(result["stats"]["negative_expressions"], 5)
        self.assertIn("negative-density", {w["code"] for w in result["warnings"]})

    def test_competing_camera_moves_warn(self):
        result = review_prompt("The camera pushes in, orbits the subject, then pulls back.")
        self.assertIn("camera-competition", {w["code"] for w in result["warnings"]})

    def test_repeated_clause_warns(self):
        result = review_prompt("保持角色身份。镜头缓慢推近。保持角色身份。")
        self.assertIn("repeated-clause", {w["code"] for w in result["warnings"]})

    def test_quality_stack_warns(self):
        result = review_prompt("4K, ultra HD, rich detail, sharp clarity, cinematic textures.")
        self.assertIn("quality-tag-stack", {w["code"] for w in result["warnings"]})

    def test_cli_reads_utf8_file_and_returns_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "prompt.txt"
            path.write_text("镜头固定，人物停步。不要字幕。", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("review_prompt.py")), str(path), "--json"],
                check=True, capture_output=True, text=True, encoding="utf-8",
            )
        result = json.loads(completed.stdout)
        self.assertEqual(result["stats"]["negative_expressions"], 1)
        self.assertEqual(completed.returncode, 0)


if __name__ == "__main__":
    unittest.main()
