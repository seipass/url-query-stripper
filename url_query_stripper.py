import argparse,csv,json,sys
def transform(url):
    from urllib.parse import urlsplit,urlunsplit
    p=urlsplit(url); return urlunsplit((p.scheme,p.netloc,p.path,"",""))

def main():
    parser=argparse.ArgumentParser(description='URL query and fragment stripper')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    data=source
    result=transform(data)
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
