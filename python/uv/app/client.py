"""HTTP client helper built on urllib3 1.26 API.

`Retry(method_whitelist=...)` was deprecated in 1.26 and *removed* in urllib3 2.x
(replaced by `allowed_methods`), so this breaks on upgrade.
"""
from urllib3 import PoolManager
from urllib3.util.retry import Retry


def build_retry() -> Retry:
    # urllib3 2.x: `method_whitelist` was removed -> `allowed_methods`.
    return Retry(
        total=3,
        backoff_factor=0.2,
        status_forcelist=[502, 503, 504],
        allowed_methods=["GET", "HEAD"],
    )


def build_pool() -> PoolManager:
    return PoolManager(retries=build_retry())


def allowed_methods(retry: Retry) -> frozenset:
    # urllib3 2.x exposes the configured methods via `.allowed_methods`.
    return retry.allowed_methods
