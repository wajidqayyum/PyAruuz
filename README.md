# 🖋️ PyAruuz - Advanced Urdu Poetry Scansion Engine

![UI Preview](https://via.placeholder.com/800x400.png?text=PyAruuz+Aesthetic+Web+UI)

**PyAruuz** is a state-of-the-art Urdu Poetry Scansion (تقطیع) engine. Originally developed in C#, this repository contains the complete, highly-optimized **Python Port** of the engine. It accurately predicts the poetic meter (بحر), feet (ارکان), and rhythm sequence (افاعیل) for Urdu Ghazals with mathematical precision using Dynamic Programming algorithms.

## ✨ Features

- **Perfect Accuracy:** Replicates the legacy C# engine with 100% parity, resolving complex Urdu poetic rules.
- **Dynamic Programming Engine:** Uses advanced sliding window DP matching to find the closest valid rhythmic path.
- **Urdu Morphological Heuristics:** Automatically handles complex poetic phenomena:
  - *Noon-Ghunna* (ن غنہ) reduction
  - *Wao-e-Ataf* (و عطف) integration
  - *Izafat* (کسرہِ اضافت) mapping
  - *Alif-Lam* (ال) rules
- **Ultra-Aesthetic Web UI:** A beautiful, responsive, glassmorphism frontend built using Flask, featuring exact structural mapping of words to their phonetic binary codes.
- **Terminal CLI:** Fully functional `ghazal_scanner.py` that outputs structured data cleanly into the terminal.

## 🚀 Tech Stack
- **Backend Core:** Python 3.10+
- **Database:** SQLite3 (`aruuz.db` mastertable and heuristics definitions)
- **Web Interface:** Flask, HTML5, CSS3 (Glassmorphism), Vanilla JS

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/PyAruuz.git
   cd PyAruuz/python_port
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Web Application:**
   ```bash
   python app.py
   ```
   *Open your browser and navigate to `http://localhost:5000` to access the aesthetic UI.*

4. **Run the CLI Version:**
   ```bash
   python ghazal_scanner.py
   ```
   *Paste your Ghazal into the terminal and type `END` to get a structured breakdown.*

## 📊 Example Output

```text
رمل مثمن مخبون محذوف مقطوع
فاعلاتن فَعِلاتن فَعِلاتن فِعْلن
یہ جہاں چیز ہے کیا لوح و قلم تیرے ہیں
x -= =- x x =-   -= =x x
Distance: 0
```

## 🤝 Contributing
Contributions are always welcome! Feel free to open an issue or submit a pull request if you want to improve the codebase, add more meters, or optimize the algorithms.

## 📝 License
This project is open-source and available under the MIT License.
