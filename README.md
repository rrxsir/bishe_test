# Causal Intelligence Hub

基于因果图的多智能体协同开源情报分析系统示例，实现了前后端分离架构。

## 系统功能

- **技术趋势监测**：整合多源数据，实时识别开源技术趋势。
- **开源项目追踪**：追踪重点项目的更新、活跃度与生态影响。
- **生态能力构建**：构建技术、组织、社区的因果网络并输出分析报告。

## 技术栈

- **后端**：FastAPI、NetworkX、Pydantic
- **前端**：Vue 3、Vite、Pinia、Axios

## 本地开发

### 后端

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认通过 Vite 代理访问本地 `http://localhost:8000` 的后端接口。

## API 概览

| 方法 | 路径 | 描述 |
| ---- | ---- | ---- |
| `GET` | `/health` | 健康检查 |
| `POST` | `/api/data/refresh` | 从选定数据源重新采集数据 |
| `GET` | `/api/data` | 获取缓存的情报数据 |
| `GET` | `/api/graph` | 基于缓存数据生成因果图结构 |
| `GET` | `/api/report` | 调用多智能体分析生成报告 |

## 数据源示例

- `config/web_sources.json`：模拟 Web 数据信号。
- `data/local_insights.json`：本地样例数据。
- `config/custom_sources.yaml`：自定义配置数据源。

运行 `POST /api/data/refresh` 即可自动聚合以上样例数据，后续接口均基于缓存内容进行分析。
