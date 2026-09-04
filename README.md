# User Service — стартовый проект модуля pytest

Это учебный сервис, который ты будешь покрывать тестами на протяжении всего модуля 2 курса AQA. Код сервиса уже написан — **тесты ты пишешь сам**, это и есть содержание всех шести практик модуля.

## Что внутри

- **`validators.py`** — функции валидации email и пароля. Чистые функции (без побочных эффектов) — идеально для первых тестов с `assert` и параметризации.
- **`user_service.py`** — сервис работы с пользователями: регистрация, логин, поиск, удаление. Хранит данные в JSON-файле.
- **`users.json`** — стартовое хранилище (пустое).

## Структура классов и функций

### `validators.py`

```python
is_valid_email(email: str) -> bool
is_valid_password(password: str) -> bool
validate_registration_data(email: str, password: str) -> None  # бросает ValueError
```

### `user_service.py`

```python
class User:
    email: str
    password_hash: str
    User.create(email, password) -> User
    user.check_password(password) -> bool

class UserService:
    UserService(storage_path)                  # путь к JSON-файлу
    service.register(email, password) -> User  # ValueError, UserAlreadyExistsError
    service.login(email, password) -> User     # InvalidCredentialsError
    service.get_user(email) -> User | None
    service.delete_user(email) -> None         # UserNotFoundError
    service.count_users() -> int

# Исключения:
UserServiceError              # базовое
UserAlreadyExistsError
UserNotFoundError
InvalidCredentialsError
```

## Как развернуть проект

### 1. Создай свой репозиторий из шаблона

Нажми на этой странице кнопку **«Use this template» → «Create a new repository»**. GitHub создаст **твой собственный** репозиторий с этими файлами — без истории оригинала и без связи с ним. Дальше ты работаешь только в нём: ветки, коммиты, pull request'ы. В конце модуля этот репозиторий станет твоим портфолио.

Назови его как хочешь — например, `user-service-tests`.

Дальше склонируй его к себе:

```bash
git clone https://github.com/<твой-логин>/<имя-репозитория>.git
cd <имя-репозитория>
```

> ⚠️ **Не делай fork и не клонируй этот репозиторий напрямую.** Форк остаётся привязанным к оригиналу, и твои коммиты будут выглядеть как попытка изменить чужой проект. Нужен именно свой репозиторий через «Use this template».

### 2. Создай виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate          # macOS / Linux
# или
venv\Scripts\Activate.ps1         # Windows PowerShell
```

В начале строки должно появиться `(venv)`.

Нужен **Python 3.12 или новее** — в коде используется синтаксис, доступный начиная с 3.10.

### 3. Установи зависимости

```bash
pip install -r requirements.txt
```

### 4. Проверь, что код запускается

Создай файл `try_it.py` рядом с `user_service.py`:

```python
from user_service import UserService

service = UserService(storage_path="users.json")
service.register("alice@example.com", "Password123")
print(service.count_users())  # 1

user = service.login("alice@example.com", "Password123")
print(user.email)  # alice@example.com
```

Запусти:

```bash
python try_it.py
```

Если увидишь `1` и email — всё работает, можно писать тесты.

Удали потом `try_it.py` — он не понадобится. Это просто проверка, что код у тебя живой. Заодно верни `users.json` в исходное состояние (пустой объект `{}`), чтобы тестовые данные не попали в коммит.

## Как пользоваться сервисом — короткий пример

```python
from user_service import UserService, UserAlreadyExistsError

service = UserService(storage_path="users.json")

# Регистрация
service.register("bob@example.com", "MyPass123")

# Повторная регистрация того же email бросит исключение
try:
    service.register("bob@example.com", "OtherPass456")
except UserAlreadyExistsError as e:
    print(f"Не получилось: {e}")

# Логин
user = service.login("bob@example.com", "MyPass123")
print(user.email)

# Получить без бросания исключения
user = service.get_user("bob@example.com")
if user:
    print("Найден")

# Удалить
service.delete_user("bob@example.com")
print(service.count_users())  # 0
```

## Важно

- **Пароли хранятся в виде хеша** (sha256). Это видно в `users.json` — в открытом виде паролей нет. В реальных проектах используют bcrypt/argon2 с солью, но для учебного проекта sha256 достаточно.
- **`storage_path` — параметр конструктора.** Это сделано специально, чтобы в тестах ты мог передать **временный файл** вместо боевого `users.json`. Так тесты не мешают друг другу и не портят данные.
- **Сервис не делает retry, не логирует, не работает с многопоточностью.** Это намеренно — учебный проект должен быть простым и понятным. Все эти вещи добавляются по мере необходимости в реальных проектах.
