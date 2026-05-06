import urllib.request
import os

def download_file(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(filename, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

os.makedirs('c:/Users/vivek/Documents/Marinegeo Website/img/recruiters', exist_ok=True)

logos = {
    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/ONGC_Logo.png/600px-ONGC_Logo.png': 'c:/Users/vivek/Documents/Marinegeo Website/img/recruiters/ongc.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/GSI_Logo_rgb.png/600px-GSI_Logo_rgb.png': 'c:/Users/vivek/Documents/Marinegeo Website/img/recruiters/gsi.png',
    'https://upload.wikimedia.org/wikipedia/en/b/ba/National_Institute_of_Oceanography_India_logo.png': 'c:/Users/vivek/Documents/Marinegeo Website/img/recruiters/nio.png',
    'https://ncpor.res.in/images/logo.png': 'c:/Users/vivek/Documents/Marinegeo Website/img/recruiters/ncpor.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Logo_of_Oil_India_Limited.png/600px-Logo_of_Oil_India_Limited.png': 'c:/Users/vivek/Documents/Marinegeo Website/img/recruiters/oil.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/National_Geophysical_Research_Institute_logo.png/600px-National_Geophysical_Research_Institute_logo.png': 'c:/Users/vivek/Documents/Marinegeo Website/img/recruiters/ngri.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/6/60/Central_Ground_Water_Board_logo.png/600px-Central_Ground_Water_Board_logo.png': 'c:/Users/vivek/Documents/Marinegeo Website/img/recruiters/cgwb.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/3/30/Naval_Physical_and_Oceanographic_Laboratory_logo.png/400px-Naval_Physical_and_Oceanographic_Laboratory_logo.png': 'c:/Users/vivek/Documents/Marinegeo Website/img/recruiters/npol.png',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/SLB_Logo_2022.png/600px-SLB_Logo_2022.png': 'c:/Users/vivek/Documents/Marinegeo Website/img/recruiters/slb.png',
    'https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Reliance_Industries_Logo.svg/512px-Reliance_Industries_Logo.svg.png': 'c:/Users/vivek/Documents/Marinegeo Website/img/recruiters/reliance.png'
}

for url, filename in logos.items():
    download_file(url, filename)
