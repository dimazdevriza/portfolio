import glob
import re

css_files = glob.glob(r'c:\laragon\www\portfolio\dist\_astro\*.css')
if not css_files:
    print('No CSS found!')
    exit(1)

with open(css_files[0], 'r', encoding='utf-8') as f:
    css_content = f.read()

with open(r'c:\laragon\www\portfolio\dist\slides\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

standalone = re.sub(r'<link rel="stylesheet" href="/_astro/[^"]+">', lambda m: f'<style>{css_content}</style>', html)

with open(r'c:\laragon\www\portfolio\dist\slides\standalone.html', 'w', encoding='utf-8') as f:
    f.write(standalone)

print('Standalone slides created! Length:', len(standalone))
