#!/usr/bin/env python
# -*- coding: utf-8 -*-

# subset of subprocess built-in module using posix_spawn rather than fork.



import os, sys
import signal
import shlex
import posix_spawn

PIPE = "42"

fsencoding = sys.getfilesystemencoding()

class Popen(object):
    def __init__(self, args, stdin=None, stdout=None, stderr=None):
        self.returncode = None
        self.stdout = None
        self.stderr = None
        self.stdin = None
        file_actions = posix_spawn.FileActions()
        if stdout is not None:
            # child's stdout, child 2 parent pipe
            c1pread, c1pwrite = os.pipe()
            # attach child's stdout to writing en of c1p pipe
            file_actions.add_dup2(c1pwrite, 1)
            # close other end
            file_actions.add_close(c1pread)
        if stderr is not None:
            # child's stderr, child 2 parent pipe
            c2pread, c2pwrite = os.pipe()
            # attach child's stderr to writing en of c2p pipe
            file_actions.add_dup2(c2pwrite, 2)
            # close other end
            file_actions.add_close(c2pread)
        if stdin is not None:
            # child's stdin, parent to child pipe
            p2cread, p2cwrite = os.pipe()
            # attach child's stdin to reading en of p2c pipe
            file_actions.add_dup2(p2cread, 0)
            # close other end
            file_actions.add_close(p2cwrite)
        args = [s.encode(fsencoding) for s in args if type(s)==str]
        self.pid = posix_spawn.posix_spawnp(args[0], args, file_actions=file_actions)
        if stdout is not None:
            self.stdout = os.fdopen(c1pread)
            os.close(c1pwrite)
        if stderr is not None:
            self.stderr = os.fdopen(c2pread)
            os.close(c2pwrite)
        if stdin is not None:
            self.stdin = os.fdopen(p2cwrite, 'w')
            os.close(p2cread)

    def _wait(self):
        if self.returncode is None:
            self.returncode = os.waitpid(self.pid, 0)[1]

    def communicate(self):
        if self.stdin is not None:
            self.stdin.close()
            self.stdin = None

        if self.stdout is not None:
            stdoutdata = self.stdout.read()
        else:
            stdoutdata = ""

        if self.stderr is not None:
            stderrdata = self.stderr.read()
        else:
            stderrdata = ""

        self._wait()

        if self.stdout is not None:
            self.stdout.close()
            self.stdout = None

        if self.stderr is not None:
            self.stderr.close()
            self.stderr = None

        return (stdoutdata, stderrdata)

    def wait(self):
        if self.stdin is not None:
            self.stdin.close()
            self.stdin = None

        self._wait()

        if self.stdout is not None:
            self.stdout.close()
            self.stdout = None

        if self.stderr is not None:
            self.stderr.close()
            self.stderr = None

        return self.returncode

    def poll(self):
        if self.returncode is None:
            pid, ret = os.waitpid(self.pid, os.WNOHANG)
            if (pid, ret) != (0, 0):
                self.returncode = ret

                if self.stdin is not None:
                    self.stdin.close()
                    self.stdin = None

                if self.stdout is not None:
                    self.stdout.close()
                    self.stdout = None

                if self.stderr is not None:
                    self.stderr.close()
                    self.stderr = None

        return self.returncode

    def kill(self):
        os.kill(self.pid, signal.SIGKILL)

        if self.stdin is not None:
            self.stdin.close()
            self.stdin = None

        if self.stdout is not None:
            self.stdout.close()
            self.stdout = None

        if self.stderr is not None:
            self.stderr.close()
            self.stderr = None


def call(*args):
    cmd = []
    if isinstance(args[0], str):
        if len(args) == 1:
            # splitting of arguments that cares about 
            # use of simple and double quotes
            cmd = shlex.split(args[0])
        else:
            cmd = args
    elif isinstance(args[0], list) and len(args) == 1:
        cmd = args[0]
    else:
        raise Exception("Wrong arguments passed to subprocess.call")
    pid = posix_spawn.posix_spawnp(cmd[0], cmd)
    return os.waitpid(pid, 0)


if __name__ == '__main__':
    # unit test

    p = Popen(["tr", "abc", "def"], stdin=PIPE, stdout=PIPE)
    p.stdin.write("blah")
    p.stdin.close()
    print(p.stdout.read())
    p.wait()

    p = Popen(["tr", "abc", "def"], stdin=PIPE, stdout=PIPE)
    p.stdin.write("blah")
    print(p.communicate())

    call("echo blah0")
    call(["echo", "blah1"])
    call("echo", "blah2")
