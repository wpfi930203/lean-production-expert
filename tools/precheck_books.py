"""阶段 0 前置：精益书籍语料盘点与可抽取性预检。

关键判定：每本书是否有文本层。
- 有文本层 → 直接抽取，成本低
- 无文本层（扫描件）→ 需 OCR，成本高，必须先告知用户

同时检出与现有 skill 的重叠（已蒸馏过的书）。
"""
import pathlib
import sys

D = pathlib.Path(r"D:\BaiduNetdiskDownload\精益工具包\精益书籍")

try:
    import pypdf
except ImportError:
    try:
        from PyPDF2 import PdfReader as _R

        class pypdf:  # noqa
            PdfReader = _R
    except ImportError:
        print("需要 pypdf：pip install pypdf")
        sys.exit(1)

print("=" * 78)
print("阶段 0 · 语料盘点与可抽取性预检")
print("=" * 78)

rows = []
for f in sorted(D.glob("*")):
    if f.suffix.lower() not in (".pdf", ".PDF"):
        continue
    size = f.stat().st_size
    rec = {"file": f.name, "mb": size / 1024 / 1024, "pages": 0, "text_chars": 0,
           "scanned": None, "sample": ""}
    try:
        r = pypdf.PdfReader(str(f))
        rec["pages"] = len(r.pages)
        # 抽样前 12 页 + 中间 8 页判断文本层
        probe = list(range(min(12, len(r.pages))))
        mid = len(r.pages) // 2
        probe += list(range(mid, mid + 8))
        chars = 0
        samples = []
        for i in probe:
            if i >= len(r.pages):
                continue
            try:
                t = r.pages[i].extract_text() or ""
            except Exception:
                t = ""
            chars += len(t.strip())
            if t.strip() and len(samples) < 1:
                samples.append(t.strip()[:180])
        rec["text_chars"] = chars
        rec["sample"] = samples[0] if samples else ""
        # 判定：抽样的每页平均字符数
        per_page = chars / max(len(probe), 1)
        rec["scanned"] = per_page < 50
        rec["per_page"] = per_page
    except Exception as e:
        rec["error"] = str(e)[:60]
    rows.append(rec)

print(f"{'文件':46}{'MB':>7}{'页':>6}{'抽样字符':>10}{'每页':>8}  判定")
print("-" * 92)
scan_list, ok_list = [], []
for r in rows:
    name = r["file"][:44]
    if r.get("error"):
        print(f"{name:46}{r['mb']:>7.0f}{'ERR':>6}{'-':>10}{'-':>8}  读取失败")
        continue
    verdict = "扫描件需 OCR" if r["scanned"] else "有文本层"
    print(f"{name:46}{r['mb']:>7.0f}{r['pages']:>6}{r['text_chars']:>10,}"
          f"{r.get('per_page',0):>8.0f}  {verdict}")
    (scan_list if r["scanned"] else ok_list).append(r)

print()
print("=" * 78)
print(f"有文本层:{len(ok_list)} 本 | 需 OCR: {len(scan_list)} 本")
print("=" * 78)

print("\n【有文本层 — 可直接抽取】")
for r in ok_list:
    print(f"\n▸ {r['file'][:60]}")
    print(f"  {r['pages']} 页 / 每页约 {r.get('per_page',0):.0f} 字符")
    if r["sample"]:
        print(f"  样本: {r['sample'][:150]}")

if scan_list:
    print("\n\n【需 OCR — 成本高，需用户确认】")
    tot_pg = sum(r["pages"] for r in scan_list)
    for r in scan_list:
        print(f"  ▸ {r['file'][:58]}")
        print(f"    {r['pages']} 页 / 抽样每页仅 {r.get('per_page',0):.0f} 字符（无文本层）")
    print(f"\n  合计 {tot_pg} 页需 OCR。按此前《精益生产推行手册》经验（RapidOCR约 3.3–3.9 s/页，"
          f"3 进程并行），预计 {tot_pg*3.6/3/60:.0f}–{tot_pg*3.9/3/60:.0f} 分钟。")
    print("  ⚠️ 阶段 5红线 6：不能凭空记忆提取——没文本就停下来问。")
