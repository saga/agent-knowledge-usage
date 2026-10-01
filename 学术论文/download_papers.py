#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""根据学术论文索引批量下载公开 PDF。"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import json, re, sys
from pathlib import Path
from urllib.request import Request, urlopen
ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "papers.json"
def safe_filename(text: str) -> str:
    text = re.sub(r"[^\\w\\u4e00-\\u9fff.-]+", "-", text.strip())
    return text[:140].strip("-")
def download(item: dict):
    target_dir = Path(item["directory"]) / "pdf"
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f'{item["order"]:02d}-{safe_filename(item["title"])}.pdf'
    if target.exists() and target.stat().st_size > 0:
        return item["arxiv_id"], "exists", target.stat().st_size
    request = Request(item["pdf_url"], headers={"User-Agent":"agent-knowledge-usage/academic-paper-downloader"})
    with urlopen(request, timeout=90) as response, target.open("wb") as fp:
        while True:
            chunk = response.read(1024 * 256)
            if not chunk: break
            fp.write(chunk)
    return item["arxiv_id"], "downloaded", target.stat().st_size
def main():
    items = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures=[]
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures={pool.submit(download,item):item for item in items}
        for f in as_completed(futures):
            item=futures[f]
            try:
                paper_id,status,size=f.result()
                print(f"{status:10} {paper_id:18} {size:>10} bytes  {item['title']}")
            except Exception as exc:
                failures.append((item["arxiv_id"],str(exc)))
                print(f"FAILED     {item['arxiv_id']:18} {exc}",file=sys.stderr)
    print(f"Total: {len(items)}; Failed: {len(failures)}")
    for paper_id,error in failures: print(f"- {paper_id}: {error}",file=sys.stderr)
    return 1 if failures else 0
if __name__=="__main__": raise SystemExit(main())
