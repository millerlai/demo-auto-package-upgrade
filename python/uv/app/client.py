"""HTTP client helper built on urllib3 1.26 API.

`Retry(method_whitelist=...)` was deprecated in 1.26 and *removed* in urllib3 2.x
(replaced by `allowed_methods`), so this breaks on upgrade.
"""
from urllib3 import PoolManager
from urllib3.util.retry import Retry


def build_retry() -> Retry:
    # v1.26: `method_whitelist`. Removed in urllib3 2.x -> `allowed_methods`.
    return Retry(
        total=3,
        backoff_factor=0.2,
        status_forcelist=[502, 503, 504],
        method_whitelist=["GET", "HEAD"],
    )


def build_pool() -> PoolManager:
    return PoolManager(retries=build_retry())


def allowed_methods(retry: Retry) -> frozenset:
    # v1.26 exposes the configured methods via `.method_whitelist`.
    return retry.method_whitelist
