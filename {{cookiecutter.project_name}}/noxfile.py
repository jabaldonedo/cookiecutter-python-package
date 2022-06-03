from nox import session


@session
def tests(session):
    session.install("pytest")
    session.run("pytest", "-v", "test")


@session
def black(session):
    session.install("black")
    session.run("black", "src")
