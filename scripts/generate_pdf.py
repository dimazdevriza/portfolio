import subprocess
import os

edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = r'c:\laragon\www\portfolio\dist\slides\standalone.html'
pdf_output = r'c:\laragon\www\portfolio\Portofolio_Dimaz_Devriza.pdf'

if os.path.exists(pdf_output):
    os.remove(pdf_output)

# Use URL http://localhost:4321/slides if server is up, or file URL
url = 'http://localhost:4321/slides'

cmd = [
    edge_path,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    '--run-all-compositor-stages-before-draw',
    '--virtual-time-budget=5000',
    f'--print-to-pdf={pdf_output}',
    url
]

print("Running command:", " ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
print("Exit code:", res.returncode)
if os.path.exists(pdf_output):
    size = os.path.getsize(pdf_output)
    print(f"SUCCESS! Created {pdf_output} ({size} bytes)")
else:
    print("FAILED! Stderr:", res.stderr)
