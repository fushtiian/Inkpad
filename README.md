# Inkpad

个人学习资源与笔记管理网站，记录理论与实践两类内容，涵盖数学、计算机及相关知识。

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | Vue 3 + JavaScript |
| 后端 | Python Flask |
| 数据库 | SQLite |

## 快速开始

### 后端

```bash
cd inkpad-api
pip install -r requirements.txt
python server.py
```

服务启动于 `http://127.0.0.1:5000`。

### 前端

```bash
cd inkpad-web
pnpm install
pnpm dev
```

服务启动于 `http://localhost:5173/`。

> **注意**：前端开发环境下通过 Vite 代理将 `/inkpad/*` 请求转发至后端，无需额外配置 CORS。

## 目录结构

```
inkpad-api/        # Flask 后端
└── app/
    ├── app_base/      # 应用初始化
    ├── app_index/     # 首页
    ├── app_login/     # 登录注册
    └── app_menu/      # 菜单管理

inkpad-web/        # Vue 3 前端
└── src/
    ├── components/    # 组件
    ├── router/        # 路由
    ├── utils/         # 工具函数
    └── views/         # 页面
```
