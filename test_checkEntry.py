import nstlff

def test_checkEntry():
    assert nstlff.checkEntry("name.test", "./test/path/", False)
    assert not nstlff.checkEntry("Name.test", "./test/path/", False)
    assert not nstlff.checkEntry("name", "./test/path/", False)

    assert nstlff.checkEntry("Name", "./test/path/", True)
    assert not nstlff.checkEntry("name.test", "./test/path/", True)
    assert not nstlff.checkEntry("name", "./test/path/", True)