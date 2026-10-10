# funbattle

数据竞赛代码骨架仓库：按「平台 / 赛事 ID」分目录，为个人参加的数据竞赛（如 DataFountain）
预留可导入的包结构。

**当前状态：只有目录骨架，尚无实现代码。** 已搭建的唯一赛题是 DataFountain 557，其
`model/`、`utils/`、`evalution/` 三个子包都只有空的 `__init__.py`，不提供任何函数、类或
CLI。赛事数据集和一次性脚本不随此包发布。

## 环境要求

- Python 3.10 或更高版本
- [uv](https://docs.astral.sh/uv/)（组织统一的虚拟环境与依赖管理工具）

## 安装

包尚未发布到 PyPI，需要克隆仓库后从本地安装：

```bash
git clone https://github.com/farfarfun/funbattle.git
cd funbattle
uv sync                 # 创建虚拟环境并安装运行时依赖与开发依赖
```

只想把本仓库装进已有环境时：

```bash
uv pip install .
```

开发时需要可编辑安装则使用：

```bash
uv pip install -e .
```

## 从 notebattle 迁移

`notebattle` 已弃用。请将依赖声明中的 `notebattle` 替换为 `funbattle`，并把
`import notebattle` 替换为 `import funbattle`：

```bash
uv pip uninstall notebattle
uv pip install funbattle
```

仓库中的 [`legacy/notebattle`](legacy/notebattle) 是旧分发包最后一个转发版本的发布
源码。发布 `funbattle` 后，维护者应从该目录发布 `notebattle` 0.0.7；它只依赖
`funbattle>=0.0.8`，不再包含项目实现。该版本的 PyPI 与 GitHub Release 说明应链接至
本节，告知使用者完成上述迁移。

## 示例

包内尚无实现代码，当前唯一能演示的就是目录骨架可被正常导入：

```python
from importlib import import_module

bt557 = import_module("funbattle.battles.datafountain.bt557")

print(bt557.__name__)  # funbattle.battles.datafountain.bt557
print(bt557.__doc__)  # 赛题数据集页面链接
```

新增赛事时，在 `src/funbattle/battles/<平台>/<赛事 ID>/` 下补充代码，并同步更新本节的
入口说明和可运行示例。

## 开发

开发依赖（`pytest`、`ruff`）定义在 `pyproject.toml` 的 `[dependency-groups].dev` 中，
由 `uv` 管理：

```bash
uv sync
```

运行测试与静态检查：

```bash
uv run pytest -q
uv run ruff check .
uv run ruff format --check .
```

## 许可证

本项目使用 [MIT License](LICENSE)。

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
