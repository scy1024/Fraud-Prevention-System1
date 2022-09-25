# Contributing Guide

## Development Environment

推荐使用Pipenv, 在项目根目录下`pipenv install`.

若不适用Pipenv, 在项目根目录下以editable模式安装`pip install -e .`.

## Project structure

### File structure

```
emotionalqueue
├── __main__.py     # 模块主入口
├── lib             # native api library
├── queue.py        # 请求队列模型
├── service.py      # 请求处理服务
├── api.py          # api封装
├── ui              # ui实现
│   ├── repl.py     # repl ui
│   └── tk.py       # tkinter ui
└── utils.py        # 通用工具
```

### Module structure

```
+------------------------------------------------------+
|                  +---------------------+             |
|                  |      Front End      |             |
|         +------->+ +------+ +----+     |             |
|         | +------+ | REPL | | TK | ... |             |
|         | |      | +------+ +----+     |             |
|         | |      +---------------------+             |
|         | |                                          |
|         | v                                          |
| +-------+-+--------------+    +--------------------+ |
| | EmotionalQueueServices | -> |  Models(queue.py)  | |
| +----------+-------------+    +--------------------+ |
|            |                                         |
|            v                                         |
|         +--+-------------------------------+         |
|         |      API Clients                 |         |
|         | +----------+ +-----------------+ |         |
|         | | Emotion  | |     ASR         | |         |
|         | | Analysis | | +-------------+ | |         |   +-----------+
|         | +-----+----+ | | Unisound    | | |         |   | Unisound  |
|         |       |      | | Asr Adapter +-+-+---------+-> | C Library |
|         |       |      | +-------------+ | |         |   +-----------+
|         |       |      +-----------------+ |         |
|         +-------+--------------------------+         |
|                 |                                    |
+-----------------+------------------------------------+
                  |
                  v
         +--------+----------+
         | Custom Emotion    |
         | Analysis Provider |
         +-------------------+
```

## ToDo

* [ ] 原数据集缺失值情况，代码里面直接用第一个案件的对应值补上了-->优化，用随机值或者平均值
* [ ] 