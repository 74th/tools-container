from invoke import task

@task
def do(c):
    c.run(f"docker pull ubuntu:rolling")
    c.run(f"docker-compose build")
    c.run(f"docker-compose push")