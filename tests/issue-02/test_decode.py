from tests.code.morse import decode
import pytest


@pytest.mark.parametrize('morse_message, message', [
   ('... --- ...', 'SOS'),
   ('.... . .-.. .-.. ---', 'HELLO'),
   ('.- .- .-', 'AAA')
])
def test_decode(morse_message, message):
    assert decode(morse_message) == message


if __name__ == '__main__':
    pytest.main()