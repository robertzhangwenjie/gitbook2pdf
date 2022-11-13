import sys
from gitbook2pdf import Gitbook2PDF
if __name__ == '__main__':
    url = sys.argv[1]
    fname = sys.argv[2]
    Gitbook2PDF(url,fname).run()
