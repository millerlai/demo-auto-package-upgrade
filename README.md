# demo-auto-package-upgrade

展示 [auto-package-migration](https://github.com/millerlai/auto-package-migration)
（即 `/package-upgrade` skill）偵測並修復「套件升級造成 breaking change」的能力。

每個 `{language}/{package-management-tool}/` 資料夾都是一個獨立情境：
使用**舊版套件**寫的主邏輯 + 單元測試，在舊版依賴下測試會綠燈；
一旦把套件升級到新版，主邏輯與 UT 就會 break，需要工具自動修正。

## 情境一覽

| 資料夾 | 套件管理 | 升級情境 | 主要 breaking 點 |
|---|---|---|---|
| `python/uv/` | uv | FastAPI 0.95 / Pydantic 1.10 / urllib3 1.26 → Pydantic 2 / urllib3 2 | `.dict()`、`@validator`、`orm_mode`、`Retry(method_whitelist=)` |
| `python/poetry/` | poetry | SQLAlchemy 1.4 → 2.0 | `declarative_base` 路徑、`engine.execute(str)`、`query.get()` |
| `python/pip/` | pip | pandas 1.5 → 2.0 | `DataFrame.append()`、`iteritems()` |
| `javascript/npm/` | npm | axios 0.27 → 1.x | `axios.all()` / `axios.spread()`、`paramsSerializer` |
| `typescript/pnpm/` | pnpm | chalk 4 → 5 (ESM-only) | CJS 預設匯入、`chalk.keyword()` |
| `go/go-modules/` | go modules | golang-jwt v4 → v5 | major path `/v4→/v5`、`StandardClaims`、`Token.Valid` |

## 跑各情境的測試

```bash
# python/uv
cd python/uv && uv sync --dev && uv run pytest

# python/poetry
cd python/poetry && poetry install && poetry run pytest

# python/pip
cd python/pip && pip install -r requirements-dev.txt && pytest

# javascript/npm
cd javascript/npm && npm install && npm test

# typescript/pnpm
cd typescript/pnpm && pnpm install && pnpm test

# go/go-modules
cd go/go-modules && go mod tidy && go test ./...
```

## demo 流程建議

1. 在舊版依賴下跑測試 → 全綠（baseline）。
2. 對某個資料夾執行 `/package-upgrade`，把套件升級到新版。
3. 升級後測試轉紅 → 工具分析 breaking change 並自動修正主邏輯與 UT → 回到綠燈。

> 註：每個資料夾原本附有一份 `BreakingInformation.md` 對照筆記，但已被 `.gitignore`
> 排除、不進 repo——刻意讓升級工具只看到 **code 與套件依賴檔**，沒有任何額外提示。
