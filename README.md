# Redirect Service

A simple sphinx-based redirect service using `sphinx-reredirects`.

## Available Redirects

See `conf.py` for the list of available redirects.

## Adding Redirects

Edit `conf.py` and add entries to the `redirects` dictionary with a `/index` suffix.

```python
redirects = {
    "new-redirect/index": "https://example.com",
}
```

This will create a redirect from `https://go.pypsa.org/new-redirect` to `https://example.com` and the url can be used anywhere.