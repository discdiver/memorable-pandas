def test():
    # Here we can either check objects created in the solution code, or the
    # string value of the solution, available as __solution__. A helper for
    # printing formatted messages is available as __msg__. See the testTemplate
    # in the meta.json for details.

    # If an assertion fails, the message will be displayed
    assert "print" in __solution__, "Did you make a print() function?"
    # assert some_var == len(DATA), "Are you getting the correct length?"
    assert (
        "__version__" in __solution__
    ), "Did you use __version__ with double underscores on each side?"

    __msg__.good("Well done!")
