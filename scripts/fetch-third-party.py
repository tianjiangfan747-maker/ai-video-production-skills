# -*- coding: utf-8 -*-
"""
fetch-third-party.py — 拉取第三方 prompt 知识库（lanshu-awesome-ai-video-kit, MIT License）

7 个模型工具技能（model-selector / prompt-translator / seedance-* / kling-prompter /
happyhorse-prompter）引用的 methodology / prompts / tools 资源不在本仓库内，
运行本脚本会从原开源仓库 https://github.com/cclank/lanshu-awesome-ai-video-kit
下载并填充到 skills/_shared/lanshu-kit/。

用法：python scripts/fetch-third-party.py
"""
import io
import os
import shutil
import sys
import tarfile
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET = os.path.join(REPO_ROOT, "skills", "_shared", "lanshu-kit")
TARBALL_URL = "https://codeload.github.com/cclank/lanshu-awesome-ai-video-kit/tar.gz/refs/heads/main"

NEEDED_DIRS = ["methodology", "prompts", "tools"]
NEEDED_FILES = ["RESOURCES.md", "CONTRIBUTING.md", "LICENSE", "README.md"]


def main():
    if os.path.exists(os.path.join(TARGET, "methodology")):
        print("已存在 skills/_shared/lanshu-kit/methodology，跳过下载。")
        print("如需强制刷新，请先删除 skills/_shared/lanshu-kit 目录再运行。")
        return

    print("正在下载 lanshu-awesome-ai-video-kit ...")
    try:
        with urllib.request.urlopen(TARBALL_URL, timeout=60) as r:
            data = r.read()
    except Exception as e:
        print(f"下载失败：{e}")
        print("可以手动 git clone https://github.com/cclank/lanshu-awesome-ai-video-kit")
        print("然后把 methodology/ prompts/ tools/ 和 RESOURCES.md CONTRIBUTING.md LICENSE README.md")
        print(f"复制到 {TARGET}")
        sys.exit(1)

    os.makedirs(TARGET, exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        top = tar.getnames()[0].split("/")[0]
        for member in tar.getmembers():
            rel = os.path.relpath(member.name, top)
            parts = rel.split(os.sep)
            if parts[0] in NEEDED_DIRS or (len(parts) == 1 and parts[0] in NEEDED_FILES):
                member.name = rel
                tar.extract(member, TARGET, filter="data")

    print(f"完成！资源已填充到 {TARGET}")
    print("现在 18 个技能全部可用。")


if __name__ == "__main__":
    main()
