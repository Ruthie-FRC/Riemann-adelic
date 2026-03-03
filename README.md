# Riemann-Adelic

A research repository exploring spectral operator approaches to the Riemann Hypothesis.

## Overview

This repository implements and tests a spectral framework for studying the Riemann Hypothesis, following the Hilbert–Pólya conjecture approach: that the non-trivial zeros of the Riemann zeta function correspond to eigenvalues of a self-adjoint operator.

The approach is built around an adelic operator `H_Ψ` constructed to satisfy:

```
Spec(H_Ψ) = { t ∈ ℝ | ζ(1/2 + it) = 0 }
```

The operator is constructed using adelic analysis — treating the integers through their representations at every prime simultaneously — combined with tools from spectral theory, functional analysis, and the Weil explicit formula.

**Status:** This is active mathematical research. The framework is numerically consistent with known Riemann zeros and has partial formal arguments in Lean 4, but does not yet constitute a complete proof accepted by the mathematical community.

## Repository Structure

```
├── core/                  # Core Python module (spectral oscillator, resonator)
├── lib/                   # Standalone library modules (operator implementations, etc.)
├── utils/                 # Mathematical utilities (adelic determinant, etc.)
├── src/                   # Additional source modules
├── operators/             # Operator implementations
├── operador/              # Adelic Hilbert space operator (H_Ψ)
├── spectral_RH/           # Spectral analysis components
├── formalization/         # Lean 4 formal proof attempts
│   └── lean/              # Lean source files and proof framework
├── tests/                 # Test suite (pytest)
├── scripts/               # Standalone scripts
│   ├── validation/        # Numerical validation scripts
│   ├── demos/             # Demonstration scripts
│   └── examples/          # Usage examples
├── zeros/                 # Riemann zero data (from Odlyzko's tables)
├── data/                  # Computed results and certificates
├── paper/                 # LaTeX manuscript source
├── notebooks/             # Jupyter notebooks
├── docs/                  # Documentation
├── validate_v5_coronacion.py  # Main validation entry point
└── requirements.txt       # Python dependencies
```

## Mathematical Approach

The framework has three components:

**1. Numerical validation** — The adelic canonical determinant `D(s)` is constructed as a Hadamard product over known Riemann zeros, then tested for the expected functional equation `D(s) = D(1-s)`, normalization `D(1/2) = 1`, and consistency with the Weil explicit formula.

**2. Operator theory** — The operator `H_Ψ` is built as a self-adjoint operator on an adelic Hilbert space `L²(𝔸_K / K×)`. Self-adjointness forces real eigenvalues, which under the spectral correspondence would place all zeros on `Re(s) = 1/2`.

**3. Lean 4 formalization** — Several key lemmas are formalized in Lean 4 using Mathlib, including the functional equation, Paley-Wiener uniqueness arguments, and the Selberg trace formula setup.

## Getting Started

### Requirements

- Python 3.11+
- See `requirements.txt` for Python dependencies

### Installation

```bash
git clone https://github.com/Ruthie-FRC/Riemann-adelic.git
cd Riemann-adelic
pip install -r requirements.txt
```

### Run the main validation

```bash
python validate_v5_coronacion.py
```

### Run the test suite

```bash
pytest tests/
```

### Options

```bash
python validate_v5_coronacion.py --precision 50 --verbose --save-certificate
```

## Key Files

| File | Purpose |
|------|---------|
| `validate_v5_coronacion.py` | Main validation script — runs all 5 coherence levels |
| `utils/adelic_determinant.py` | Adelic canonical determinant `D(s)` |
| `core/spectral_oscillator.py` | Spectral oscillator built from Riemann zeros |
| `formalization/lean/` | Lean 4 formal proof files |
| `zeros/zeros_t1e3.txt` | First ~1000 non-trivial Riemann zeros (Odlyzko) |

## What This Is Not

This repository does not contain a complete, peer-reviewed proof of the Riemann Hypothesis. The Lean 4 files contain `sorry` placeholders in several critical lemmas that remain unproved. The numerical evidence is consistent with RH but consistency is not a proof.

Several extended modules in this repository (biological analogies, QCD connections, consciousness models) represent speculative explorations and should not be taken as part of the core mathematical argument.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

- Mathematical content and manuscript: CC-BY 4.0
- Code: MIT License (see LICENSE-CODE)

## Author

José Manuel Mota Burruezo  
ORCID: [0009-0002-1923-0773](https://orcid.org/0009-0002-1923-0773)
