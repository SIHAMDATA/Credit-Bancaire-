import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_DIR = ROOT / "Python2026 6" / "Python2026"
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from acceuil_fastapi_new import app  # noqa: E402

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", "8002"))
    uvicorn.run(app, host="0.0.0.0", port=port)
