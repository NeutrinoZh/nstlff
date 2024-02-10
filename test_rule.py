import rule

def test_checkEntry():
    assert rule.checkEntry("name.test", "./test/path/", False)
    assert not rule.checkEntry("Name.test", "./test/path/", False)
    assert not rule.checkEntry("name", "./test/path/", False)

    assert rule.checkEntry("Name", "./test/path/", True)
    assert not rule.checkEntry("name.test", "./test/path/", True)
    assert not rule.checkEntry("name", "./test/path/", True)