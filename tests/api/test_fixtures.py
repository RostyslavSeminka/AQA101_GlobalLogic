import pytest

@pytest.mark.check
def test_changes_second_name(user):
    assert user.name == 'Andrii'

@pytest.mark.check
def test_change_name(user):
    assert user.second_name == 'Ptashka'

