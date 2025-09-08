# Docker Example

This is a simple example of how to use a custom container image with labgrid. It
is essentially a combination of the official labgrid repo's docker
[example](https://github.com/labgrid-project/labgrid/tree/master/examples/docker)
combined with the corresponding
[strategy](https://github.com/labgrid-project/labgrid/blob/master/labgrid/strategy/dockerstrategy.py),
but with some basic modifications in the env.yaml file. The image is based on
the one that the labgrid example used,
[ubuntu-sshd](https://github.com/rastasheep/ubuntu-sshd/blob/master/18.04/Dockerfile),
but it has been updated to use a more recent version.

## Prerequisites

To run the docker example one has to have docker-ce installed and
accessible via "unix:///var/run/docker.sock" (the default). The
default docker bridge network also needs to be accessible from the
pytest executor since the test tries to establish an ssh connection to
the container (again the default after a standard installation of
docker-ce).

## Setup

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install labgrid`
4. Build the container image with e.g. `docker build -t ubuntu-sshd:22.04 -f Dockerfile .`
5. `labgrid-client -p dockertest create`
6. `labgrid-client -p dockertest acquire`

From here, you can either run the example test with the same instruction as
specified in the labgrid example:

```
pytest -s --lg-env env.yaml test_shell.py 
```

or you can start and connect to the container with ssh:

```
labgrid-client -x ecogrid -c env.yaml -s accessible ssh
```

Note that it assumes you have a coordinator running on a resolvable host named
"ecogrid" (change as needed), hence the '-x' option.
