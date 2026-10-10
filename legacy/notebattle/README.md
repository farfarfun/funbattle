# notebattle

`notebattle` 已重命名为 `funbattle`。这是旧分发包的最终转发版本：安装它会安装
`funbattle`，但不再提供 `notebattle` 的实现。

请将依赖和 import 更新为新名称：

```bash
uv pip uninstall notebattle
uv pip install funbattle
```

```python
# 旧：import notebattle
import funbattle
```

项目说明和当前安装方式见 <https://github.com/farfarfun/funbattle#从-notebattle-迁移>。

## 发布

先发布 `funbattle` 0.0.8 或更高版本，再从本目录发布 `notebattle` 0.0.7。PyPI 项目说明和
对应 GitHub Release 应引用本 README 的迁移说明。
