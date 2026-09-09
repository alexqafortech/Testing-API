"""
Корневой conftest для всех тестов.

Добавляет директорию src/ в sys.path, чтобы тесты могли
импортировать модули как 'from user_service import ...'
без указания полного пути.
"""

import sys
from pathlib import Path

# Добавляем src/ в sys.path
SRC_DIR = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))