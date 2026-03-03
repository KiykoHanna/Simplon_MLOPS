"""tests.test_main.py."""

import pandas as pd

from app.main import main


def test_main(monkeypatch):
    """Test main."""
    def fake_read_csv(path):
        return pd.DataFrame({"a": [1, 2]})

    monkeypatch.setattr(pd, "read_csv", fake_read_csv)

    main()
