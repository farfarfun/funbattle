# CHANGELOG

## 0.0.8

### 变更

- README 只描述当前状态，移除历史改名说明章节；安装入口保持为本地
  `pip install .`，待包正式发布到 PyPI 后再改为 `pip install funbattle`。
- 仓库 homepage 清空，不再指向非本组织的 PyPI 包。

## 0.0.7

### 变更

- **破坏性变更**：源码目录从仓库根目录的 `funbattle/` 迁移到标准的 `src/funbattle/`
  布局，import 路径不变（仍为 `import funbattle`），仅打包结构调整。
- 依赖 `tqdm` 补充版本下限（`>=4.60.0`）。
- 移除 `script/build.sh` 中基于 `setup.py`/`twine` 的手写发布流程，以及脚本内
  自动 `git pull`/`git commit`/`git push`，发布改走 `funbuild`。
- **破坏性变更**：import 名与 PyPI 包名从 `notebattle` 改为 `funbattle`，
  与仓库名保持一致。原 `import notebattle` / `pip install notebattle` 需切换为
  `import funbattle` / `pip install funbattle`。PyPI 上可查到的旧包最终版本为
  `notebattle 0.0.6`；该包属于原发布者账号，本仓库没有权限发布其转发版本。
  迁移完成后请使用新包名，不要继续依赖旧包。

### 修复

- 提交 `uv.lock` 以保证可复现构建。
- `.gitignore` 补充 `*.db`、`*.rar`、`.run/`、`logs/`、`.idea/`、`.vscode/`。
