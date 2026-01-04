"""One-shot database reset for local development.

This script drops all tables and recreates them using the models in app.py.
It is intended for development environments when the SQLAlchemy models changed
but the SQLite schema wasn't migrated.

Usage (PowerShell):
  conda activate ai-backend
  python reset_db.py --yes

Notes:
- This will DELETE data. Use only when you explicitly want a rebuild.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urlparse

from app import app, db


def _resolve_sqlite_path(database_uri: str) -> Path | None:
    parsed = urlparse(database_uri)
    if parsed.scheme != "sqlite":
        return None

    # sqlite:///relative.db  -> parsed.path == '/relative.db'
    # sqlite:////abs/path.db -> parsed.path == '//abs/path.db'
    path = (parsed.path or "").lstrip("/")
    if not path or path == ":memory:":
        return None

    base_dir = Path(__file__).resolve().parent
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return (base_dir / candidate).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description="Drop and recreate all DB tables (development only).")
    parser.add_argument("--yes", action="store_true", help="Confirm deleting ALL data")
    parser.add_argument(
        "--delete-sqlite-file",
        action="store_true",
        help="Also delete the SQLite database file when using sqlite:///...",
    )
    args = parser.parse_args()

    if not args.yes:
        print("Refusing to reset without --yes (this deletes data).")
        return 2

    db_uri = app.config.get("SQLALCHEMY_DATABASE_URI", "")
    sqlite_path = _resolve_sqlite_path(db_uri) if args.delete_sqlite_file else None

    with app.app_context():
        print("Dropping all tables...")
        db.drop_all()
        db.session.commit()

        if sqlite_path is not None:
            try:
                if sqlite_path.exists():
                    print(f"Deleting SQLite file: {sqlite_path}")
                    sqlite_path.unlink()
            except Exception as exc:
                print(f"Warning: failed to delete sqlite file: {exc}")

        print("Creating all tables...")
        db.create_all()
        db.session.commit()

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
