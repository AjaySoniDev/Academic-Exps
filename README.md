<h1 align="center">Academic-Exps</h1>

<p align="center">
  <strong>Compact Python coursework repository for foundational programming experiments.</strong><br>
  The current repository contains two implemented console-based experiments: student result processing and a guarded arithmetic calculator.
</p>

<p align="center">
  <img alt="Status" src="https://img.shields.io/badge/status-academic%20coursework-blue">
  <img alt="Language" src="https://img.shields.io/badge/language-Python-3776AB">
  <img alt="Experiments" src="https://img.shields.io/badge/implemented%20experiments-2-purple">
</p>

<p align="center">
  <a href="#overview">Overview</a> ·
  <a href="#what-this-repo-contains">Contents</a> ·
  <a href="#implemented-experiments">Experiments</a> ·
  <a href="#run-locally">Run Locally</a> ·
  <a href="#current-scope">Current Scope</a>
</p>

---

## Overview

**Academic-Exps** is a small repository for college programming practicals implemented in Python.

The current <code>main</code> branch contains exactly **two** executable experiments. Each experiment lives in its own folder and can be run directly with Python without third-party dependencies.

~~~text
User input
   ↓
Basic validation / branching
   ↓
Computation
   ↓
Console result
~~~

---

## What This Repo Contains

| Path | Purpose |
|---|---|
| <code>Experiment-1/experiment_1.py</code> | Student result processing system. |
| <code>Experiment-2/experiment_2.py</code> | Menu-driven arithmetic calculator. |
| <code>README.md</code> | Repository documentation. |

---

## Implemented Experiments

### Experiment 1 — Student Result Processing

The program collects student name, roll number, and marks in Python, Mathematics, and English. It calculates total marks out of 300, percentage, and a pass/fail result using a 40% threshold.

This experiment demonstrates console input, variables, numeric conversion, arithmetic, conditionals, and formatted output.

### Experiment 2 — Arithmetic Calculator

The calculator accepts two numbers and one operator.

| Operator | Operation |
|---|---|
| <code>+</code> | Addition |
| <code>-</code> | Subtraction |
| <code>*</code> | Multiplication |
| <code>/</code> | Division |
| <code>//</code> | Floor division |
| <code>%</code> | Modulus |
| <code>**</code> | Exponentiation |

Division, floor division, and modulus explicitly guard against a zero divisor. Unsupported operators return an invalid-operator message.

---

## User Flow

~~~text
Choose an experiment
   ↓
Run the Python file
   ↓
Enter requested console values
   ↓
Program evaluates the input
   ↓
Read the calculated result
~~~

---

## Repository Structure

~~~text
Academic-Exps/
├── Experiment-1/
│   └── experiment_1.py
├── Experiment-2/
│   └── experiment_2.py
└── README.md
~~~

---

## Run Locally

Python 3 is sufficient.

~~~bash
python Experiment-1/experiment_1.py
~~~

or:

~~~bash
python Experiment-2/experiment_2.py
~~~

No external packages are required by the current source.

---

## Current Scope

This repository should be treated as **foundational academic coursework**, not as a reusable software package.

The current branch does **not** contain ten completed experiments, automated tests, package metadata, dependency files, CI configuration, or a deployment target.

Earlier documentation referred to ten practical experiments, but the live repository contains only the two files documented above. This README follows the actual <code>main</code> branch.

---

## License

No repository-level license file is currently committed. Reuse rights should therefore not be inferred from this README.
