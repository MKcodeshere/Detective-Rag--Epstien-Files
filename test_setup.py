#!/usr/bin/env python3
"""
Test script to verify installation and configuration
"""
import sys
from pathlib import Path

print("🔍 Epstein Files Research Assistant - Setup Test")
print("=" * 60)
print()

# Test 1: Python version
print("1️⃣  Checking Python version...")
version = sys.version_info
if version >= (3, 11):
    print(f"   ✅ Python {version.major}.{version.minor}.{version.micro}")
else:
    print(f"   ⚠️  Python {version.major}.{version.minor}.{version.micro} (3.11+ recommended)")
print()

# Test 2: Dependencies
print("2️⃣  Checking dependencies...")
dependencies = {
    'google.genai': 'google-genai',
    'streamlit': 'streamlit',
    'pandas': 'pandas',
    'dotenv': 'python-dotenv',
    'tqdm': 'tqdm'
}

missing = []
for module, package in dependencies.items():
    try:
        __import__(module)
        print(f"   ✅ {package}")
    except ImportError:
        print(f"   ❌ {package} - MISSING")
        missing.append(package)

if missing:
    print(f"\n   ⚠️  Install missing packages: pip install {' '.join(missing)}")
print()

# Test 3: Configuration
print("3️⃣  Checking configuration...")

env_file = Path('.env')
if env_file.exists():
    print("   ✅ .env file found")

    # Try to load config
    try:
        sys.path.insert(0, str(Path(__file__).parent / 'src'))
        from config import Config

        if Config.GEMINI_API_KEY and Config.GEMINI_API_KEY != 'your_api_key_here':
            print("   ✅ GEMINI_API_KEY configured")
        else:
            print("   ⚠️  GEMINI_API_KEY not set (edit .env file)")

        print(f"   ℹ️  Model: {Config.MODEL_NAME}")
        print(f"   ℹ️  Store: {Config.FILE_SEARCH_STORE_NAME}")

    except Exception as e:
        print(f"   ⚠️  Error loading config: {str(e)}")
else:
    print("   ❌ .env file not found")
    print("      Run: cp .env.example .env")
print()

# Test 4: Data directory
print("4️⃣  Checking data directory...")
data_dir = Path('data')
if data_dir.exists():
    print("   ✅ data/ directory exists")

    # Check for CSV
    csv_files = list(data_dir.glob('*.csv'))
    if csv_files:
        for csv in csv_files:
            size_mb = csv.stat().st_size / (1024 * 1024)
            print(f"   ✅ Found: {csv.name} ({size_mb:.1f} MB)")
    else:
        print("   ⚠️  No CSV files found in data/")
        print("      Download dataset from HuggingFace and place in data/")
else:
    print("   ❌ data/ directory not found")
    print("      Creating...")
    data_dir.mkdir(exist_ok=True)
    print("   ✅ Created data/ directory")
print()

# Test 5: Source files
print("5️⃣  Checking source files...")
src_dir = Path('src')
required_files = [
    'app.py',
    'config.py',
    'csv_processor.py',
    'file_search_manager.py',
    'query_engine.py',
    'utils.py'
]

all_present = True
for filename in required_files:
    filepath = src_dir / filename
    if filepath.exists():
        print(f"   ✅ {filename}")
    else:
        print(f"   ❌ {filename} - MISSING")
        all_present = False

print()

# Summary
print("=" * 60)
if not missing and all_present and env_file.exists():
    print("✅ Setup complete! Ready to run the application.")
    print()
    print("Next steps:")
    print("1. Ensure your GEMINI_API_KEY is set in .env")
    print("2. Download the dataset to data/epstein_dataset.csv")
    print("3. Run: streamlit run src/app.py")
else:
    print("⚠️  Some issues found. Please address them above.")
    print()
    print("Setup checklist:")
    print("□ Python 3.11+")
    print("□ Install dependencies: pip install -r requirements.txt")
    print("□ Create .env file: cp .env.example .env")
    print("□ Set GEMINI_API_KEY in .env")
    print("□ Download dataset to data/")

print("=" * 60)
