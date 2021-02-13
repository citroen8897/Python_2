import hashlib


def generator_de_password(string_input):
    temp_int = int((len(string_input) / 2))
    user_password_hash_1 = hashlib.md5(string_input[:temp_int].
                                       encode('utf-8')).hexdigest()
    user_password_hash_2 = hashlib.sha1(string_input[temp_int:].
                                        encode('utf-8')).hexdigest()
    user_password = user_password_hash_1 + 'f2006i' + user_password_hash_2
    return user_password
