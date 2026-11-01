SEVERITIES = frozenset({"LOW", "MEDIUM", "HIGH", "CRITICAL"})

# Задание 1
def validate_user_id(value: object) -> int:
    if type(value) is not int:
        raise ValueError
    if int(value) <=0 :
            raise ValueError
    return int(value)

# Задание 2
def normalize_severity(value: str) -> str:
    if type(value) is not str:
         raise ValueError
    normalized_severity = value.upper().strip()
    if normalized_severity not in SEVERITIES:
             raise ValueError
    return normalized_severity

# Задание 3
# три проблемы связанные с обработкой входных данных
# user_id и is_admin проверяются на широкие условия
# не равен 0, не пустая строка, не False
# из аргументов неясно соответствует ли роль admin переданному id
# автоматическое допущение что admin разрешено всё, вряд ли это применимо к клиенсткому счёту
def can_access(user_id, is_admin):
    if user_id and is_admin:
        return True
    
    return False

# Задание 3 исправленное
def can_access_fixed(user_id, is_admin):
    if type(user_id) is not int or user_id <= 0:
         return False
    if type(is_admin) is not bool:
         return False
    
    return is_admin

# Проверяем задание 1
print("=============== TASK 1 ==================")
for x in [1, "1", 2, None, "", 0, -1, 2.2]:
    try:
        print(validate_user_id(x))
    except ValueError as e:
        print(type(e).__name__)

# Проверяем задание 2
print("=============== TASK 2 ==================")
for x in [" high ", "CRITICAL", "unknown", None, 1]:
    try:
        print(normalize_severity(x))
    except ValueError as e:
        print(type(e).__name__)


# Проверяем задание 3
print("=============== TASK 3 ==================")
for x in [(1, True), (1, False), (1, 'False'), ("1", True)]:
    try:
        print(can_access_fixed(*x))
    except ValueError as e:
        print(type(e).__name__)