from string import ascii_letters, digits
characters = ascii_letters

def is_in_chars(c: str) -> bool:
    return c in characters

def is_alpha_num_or_underscore(c: str) -> bool:
    return c.isalnum() or c == "_"

def validar_user_name(uname: str) -> bool:
    # for c in uname:
    #     if not c.isalnum() or c != '_':
    #         return False
    #     return False
    # return True
    return all(map(is_alpha_num_or_underscore, uname))

def validar_dominio(domain: str) -> bool:
    if "." not in domain:
        return False
    parts = domain.split(".")
    if not (2 < len(parts) < 3):
        return False
    return all(map(lambda x: map(is_in_chars, x) or x in "", parts))

def validar_email(email: str) -> bool:
    if "@" not in email:
        return False
    user, domain = email.split("@")
    return validar_user_name(user) and validar_dominio(domain)

def validar_cpf(cpf: str) -> bool:
    return any(
        re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf),
        re.match(r"\d{11}", cpf),
    )

def validar_rg(cpf: str) -> bool:
    return any(
        re.match(r"\d{3}\.\d{3}\.\d{3}-\d{2}", r),
        re.match(r"\d{11}", rg),
    )

def count_chars_in_pattern(s: str, pattern: list[str]) -> int:
    return len([c for c in s if c])

def validar_senha(senha: str) -> bool:
    if len(senha) < 15:
        return False

    return all(
        map (
            lambda pattern: count_chars_n_pattern(senha, pattern) >= 3,
            (
                digits,
                ascii_uppercase,
                ascii_lowercase,
                r"!@#$%¨*()[]{};,.:/\|",
            )
        )
    )