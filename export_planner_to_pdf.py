import os
import subprocess
import sys

def export_pdf():
    chrome_paths = [
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    
    browser = None
    for p in chrome_paths:
        if os.path.exists(p):
            browser = p
            break
            
    if not browser:
        print("Error: Neither Chrome nor Edge executable was found.")
        sys.exit(1)
        
    workspace = r"c:\Users\Asus\Downloads\ebook"
    html_file = os.path.join(workspace, "dear_2027_master_planner_52pages.html")
    pdf_file = os.path.join(workspace, "dear_2027_master_planner_52pages.pdf")
    
    print(f"Using browser: {browser}")
    print(f"Source HTML: {html_file}")
    print(f"Target PDF: {pdf_file}")
    print("Compiling 52 pages to A4 PDF...")
    
    cmd = [
        browser,
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=15000",
        f"--print-to-pdf={pdf_file}",
        html_file
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(pdf_file) and os.path.getsize(pdf_file) > 0:
        size_kb = os.path.getsize(pdf_file) / 1024
        print(f"SUCCESS: Exported {pdf_file} ({size_kb:.1f} KB)")
    else:
        print("Failed to export PDF.")
        print("stdout:", res.stdout)
        print("stderr:", res.stderr)
        sys.exit(1)

if __name__ == "__main__":
    export_pdf()
