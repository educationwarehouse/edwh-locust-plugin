from invoke import task


@task()
def foo(c):
    print("Hello, world!")
