from subprocess import call
def execCommand(args=[]):
    retcode = call([r"C:\Python34\python.exe", r"C:\Users\burtbiel\documents\visual studio 2015\Projects\PythonApplication1\PythonApplication1\main.py"] + args)
    if (retcode != 0):
        raise Exception("Call failed: " + args)

execCommand()
execCommand(["foo", "bar"])
