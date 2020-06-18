from project import app
import sys

if __name__ == '__main__':
    if len(sys.argv) != 1:
        app.run(sys.argv[1])
    else:
        app.run('sne')
