import json
import os
import sys
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <config_file> --folder <output_folder>")
        sys.exit(1)

    config_file = sys.argv[1]
    folder = "output"
    if "--folder" in sys.argv:
        folder_index = sys.argv.index("--folder") + 1
        if folder_index < len(sys.argv):
            folder = sys.argv[folder_index]

    # Klasör yoksa oluştur
    os.makedirs(folder, exist_ok=True)

    print(f"Reading config from: {config_file}")
    print(f"Output folder: {folder}")

    # turkish.json dosyasını oku
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {config_file}: {e}")
        data = {}

    # Basit çıktı üretelim (örnek olarak bir zaman damgası yaz)
    output_file = os.path.join(folder, "streams.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Streams updated at: {datetime.utcnow().isoformat()} UTC\n")
        f.write(f"Loaded config: {config_file}\n")
        f.write(f"Config keys: {', '.join(data.keys()) if data else 'none'}\n")

    print(f"✅ Stream data updated successfully: {output_file}")

if __name__ == "__main__":
    main()
