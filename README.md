# funbattle

个人参加数据竞赛（如 DataFountain）时的代码归档仓库，按赛事 ID 分目录存放。

## 安装

```bash
pip install funbattle
```

## 示例

```python
from importlib import import_module

import funbattle

module = import_module("funbattle.battles.datafountain.bt557")
print(f"{funbattle.__name__}: {module.__name__}")
```

仓库目前发布的是赛事代码的可导入归档，不提供通用竞赛 API；示例只验证已归档
的 `bt557` 入口可以导入。赛事数据集和一次性脚本不随此包发布，新增赛事时应在
对应目录补充入口说明和可运行示例。

### 从 `notebattle` 迁移

包名和导入名已从 `notebattle` 改为 `funbattle`。旧 PyPI 包的最后版本是
`notebattle 0.0.6`；新项目使用 `pip install funbattle` 和 `import funbattle`。
旧包由原发布者维护，当前仓库不冒充或覆盖其发布权限。

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
