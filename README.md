# The Last Stand — 2D RTS / Lane Defense Game

**The Last Stand** is a real-time strategy and lane-defense game developed in Python using **Pygame-CE**. The project demonstrates modular software design, state-machine entity logic, custom sub-pixel vector movement, and dynamic asset management tailored for game development portfolios.

---

## Technical Highlights & Architecture

* **State-Driven Entity System:** Implemented a state machine for game units, cleanly managing animations and behavior transitions (`standing`, `walking`, `shooting`).
* **Sub-Pixel Vector Movement:** Utilized floating-point positional vectors to eliminate truncation errors and pixel jitter during distance calculations.
* **Directional Sprite Orientations:** Dynamic horizontal flipping and velocity-aware direction locking to maintain smooth unit rotation during path arrival.
* **Robust Asset Loader:** Cross-platform path resolution using absolute OS-level directory mapping (`os.path.abspath`) with fallback surface rendering for error recovery.
* **OOP & Clean Code Standards:** Designed with strict Object-Oriented Programming principles, event-driven architecture, and modular structure for high maintainability.

---

## Tech Stack

* **Language:** Python 3.11+
* **Framework:** Pygame-CE (Community Edition)
* **Tools:** VS Code, Git

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MKelzUA/The-Last-Stand.git(https://github.com/MKelzUA/The-Last-Stand.git)
   cd The-Last-Stand
   python -m venv .venv
.venv\Scripts\activate
pip install pygame-ce
python main.py
