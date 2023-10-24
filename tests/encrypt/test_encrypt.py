from challenges.challenge_encrypt_message import encrypt_message
from pytest import raises


def test_encrypt_message():
    assert encrypt_message("teste", 2) == "ets_et"
    assert encrypt_message("teste", 3) == "set_et"
    assert encrypt_message("teste", -10) == "etset"
    assert encrypt_message("teste", 10) == "etset"

    with raises(TypeError):
        encrypt_message("teste", "10")
        encrypt_message(10, 10)
        encrypt_message(10, "10")
