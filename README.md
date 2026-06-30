# 📊 C-Engine Student Dashboard - Sample Project

A hybrid, lightweight analytical dashboard that bridges a low-level native **C Processing Core** with an interactive **Streamlit (Python) Web Frontend**. The application demonstrates Inter-Process Communication (IPC) by dynamically compiling and running a C program on the hosting server, intercepting its standard output (`stdout`), and parsing it directly into data visualizations.

---

## 🏛️ Project Architecture Layout

```text
├── packages.txt       # System dependency manager (Auto-installs GCC compiler)
├── requirements.txt   # Python package manager (Auto-installs Streamlit & Pandas)
├── app.py             # Streamlit frontend layout and subprocess execution controller
└── project.c          # Native C data structure processing engine
```

## ⚡ Technical Workflow

1. **On-Demand Compilation:** When a user interacts with the web interface, Python triggers the Linux `gcc` compiler to bundle `project.c` into an optimized machine binary (`backend`).
2. **Data Streaming:** The binary executes natively on the host server instance. It computes mathematical averages using static structures and streams out a standardized CSV formatting table to the system shell console.
3. **Reactive UI Interception:** Python catches the live text output stream via a secure `subprocess` data pipeline, deserializes it into memory as a Pandas Dataframe, and displays interactive analytical metric blocks.

---

## 🛠️ Deployment Instructions

### Cloud Deployment (Streamlit Community Cloud)
1. Commit all four project files directly into a public **GitHub Repository**.
2. Log into [Streamlit Community Cloud](https://streamlit.io) using your GitHub workspace profile credentials.
3. Click **New app**, select your repository name, configure your deployment branch to `main`, and explicitly assign the main file path to `app.py`.
4. Click **Deploy!** The server container will automatically identify `packages.txt` to install the C development environment before loading your web interface link.

### Local Machine Execution
Ensure you have a local C compiler (`gcc`) and Python 3.8+ properly configured on your operating system environment path variables.

```bash
# 1. Clone your project workspace down locally
git clone https://github.com
cd your-repository-name

# 2. Build the python packages stack
pip install -r requirements.txt

# 3. Spin up the Streamlit engine instance
streamlit run app.py
```

---

## 📋 Source Elements Configuration Manifest

To ensure clean execution profiles on deployment, verify that your configuration infrastructure matching files are created precisely as written below:

*   **`packages.txt`**
    ```text
    gcc
    ```
*   **`requirements.txt`**
    ```text
    streamlit
    pandas
    ```
