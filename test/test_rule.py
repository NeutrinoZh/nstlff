import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import rule

def test_checkEntry():
    ruleset = rule.RuleSet([
        rule.Rule(r".*", r"[a-z]*.test", r"[A-Z][a-zA-Z]*"),
    ])

    assert ruleset.checkEntry("name.test", "./test/path/", False)
    assert not ruleset.checkEntry("Name.test", "./test/path/", False)
    assert not ruleset.checkEntry("name", "./test/path/", False)

    assert ruleset.checkEntry("Name", "./test/path/", True)
    assert not ruleset.checkEntry("name.test", "./test/path/", True)
    assert not ruleset.checkEntry("name", "./test/path/", True)