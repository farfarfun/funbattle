# CHANGELOG

> `funbattle` 尚未发布到 PyPI（`https://pypi.org/pypi/funbattle/json` 返回 404），
> 下列各段落记录的都是仓库内的改动，均未对应任何已发布的分发包。

## 未发布

### 变更

- README 改为如实描述当前状态：本仓库只有目录骨架、没有实现代码，并补充 uv
  前置要求、`uv sync` / `uv pip install .` 安装方式与「开发」章节的测试、静态检查命令。
- `pyproject.toml` 的 `description` 同步改为「代码骨架」口径，与 GitHub 仓库描述一致。
- 补充 `[project.urls]`、`keywords`、`classifiers` 打包元信息。
- 开发依赖组补充 `ruff`，新增 `[tool.ruff] target-version = "py310"` 与
  `[tool.pytest.ini_options] testpaths`。

### 修复

- 为已发布的 `notebattle` 0.0.6 提供最终转发版本的发布源码：该版本依赖
  `funbattle>=0.0.8`，并在 README 中说明从旧分发名和 import 名迁移的路径。发布顺序为先
  发布 `funbattle`，再从 `legacy/notebattle` 发布 `notebattle` 0.0.7。
- 移除运行时依赖 `tqdm`：仓库内没有任何代码引用它，声明它会让安装者白装一个用不到的包。
  后续真正用到时再按「依赖要写版本下限」的规范加回。
- 不再跟踪 `uv.lock`（`.gitignore` 已忽略），与规范「不提交 `uv.lock`」一致；
  此前 0.0.7 段落记录的「提交 `uv.lock`」已作废。

## 0.0.8（未发布）

### 变更

- README 只描述当前状态，移除历史改名说明章节。
- 仓库 homepage 清空，不再指向非本组织的 PyPI 包。

## 0.0.7（未发布）

### 变更

- **破坏性变更**：源码目录从仓库根目录的 `funbattle/` 迁移到标准的 `src/funbattle/`
  布局，import 路径不变（仍为 `import funbattle`），仅打包结构调整。
- 依赖 `tqdm` 补充版本下限（`>=4.60.0`）。
- 移除 `script/build.sh` 中基于 `setup.py`/`twine` 的手写发布流程，以及脚本内
  自动 `git pull`/`git commit`/`git push`，发布改走 `funbuild`。
- **破坏性变更**：import 名与分发包名从 `notebattle` 改为 `funbattle`，与仓库名保持一致。
  原 `import notebattle` / `pip install notebattle` 需切换为 `import funbattle`。
  PyPI 上旧包 `notebattle` 停在 0.0.6，不再接收更新，也不会发布转发版本。

### 修复

- `.gitignore` 补充 `*.db`、`*.rar`、`.run/`、`logs/`、`.idea/`、`.vscode/`。
