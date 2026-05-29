from app.client import allowed_methods, build_pool, build_retry


def test_retry_total():
    assert build_retry().total == 3


def test_method_whitelist_configured():
    retry = build_retry()
    methods = allowed_methods(retry)
    assert "GET" in methods
    assert "HEAD" in methods


def test_pool_built():
    pool = build_pool()
    assert pool is not None
