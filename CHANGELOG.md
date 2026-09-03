# CHANGELOG

## 0.0.7

### 变更

- **破坏性变更**：源码目录从仓库根目录的 `funbattle/` 迁移到标准的 `src/funbattle/`
  布局，import 路径不变（仍为 `import funbattle`），仅打包结构调整。
- 依赖 `tqdm` 补充版本下限（`>=4.60.0`）。
- 移除 `script/build.sh` 中基于 `setup.py`/`twine` 的手写发布流程，以及脚本内
  自动 `git pull`/`git commit`/`git push`，发布改走 `funbuild`。
- **破坏性变更**：import 名与 PyPI 包名从 `notebattle` 改为 `funbattle`，
  与仓库名保持一致。原 `import notebattle` / `pip install notebattle` 需切换为
  `import funbattle` / `pip install funbattle`。旧 `notebattle` 包将发布一个最终
  版本转发说明（由仓库所有者后续处理）。

### 修复

- 提交 `uv.lock` 以保证可复现构建。
- `.gitignore` 补充 `*.db`、`*.rar`、`.run/`、`logs/`、`.idea/`、`.vscode/`。
