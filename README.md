# Hardware-Efficient Quantum Optimization for Transportation Networks via Compressed Adiabatic Evolution

This repository contains code and experiment logs for the paper on **hardware-aware hybrid quantum optimization** using **Approximate Quantum Compilation (AQC)** and **QAOA** for transportation problems.

The repository includes experiments for three representative problem classes:

- **Vehicle Routing Problem (VRP)**
- **Traveling Salesman Problem (TSP)**
- **Facility Location Problem (FLP)**

The main idea is to compress early segments of digitized adiabatic evolution using **AQC-Tensor**, then use the resulting circuit directly or combine it with variational quantum layers.

---

## Repository Contents

### Jupyter notebooks
- `AQC_VRP.ipynb` — experiments for the Vehicle Routing Problem
- `AQC_TSP.ipynb` — experiments for the Traveling Salesman Problem
- `AQC_FLP.ipynb` — experiments for the Facility Location Problem

### Result spreadsheets
- `vrp_aqc.xlsx` — VRP experiment results
- `tsp_aqc.xlsx` — TSP experiment results
- `flp_aqc.xlsx` — FLP experiment results

---

## Requirements

Please install the following packages before running the notebooks:

- **Qiskit 2.3.0**
- **Qiskit Aer**
- **AQC-Tensor addon**

### Example installation

```bash
pip install qiskit==2.3.0
pip install qiskit-aer
pip install 'qiskit-addon-aqc-tensor[aer,quimb-jax]'
```


Each notebook contains the workflow for:

1. building the transportation optimization instance,
2. mapping it to a QUBO / Ising Hamiltonian,
3. constructing Trotterized annealing circuits,
4. compressing prefixes with AQC-Tensor,
5. evaluating annealing-only, AQC+QAOA, and related hybrid variants. (This only correctly works for VRP, the code may be adapted to the others)


---

## Notes

* The notebooks were developed for **Qiskit 2.3.0**. Later versions of Qiskit may introduce API incompatibilities.
* The experiments rely on **Qiskit Aer** for simulation and on **AQC-Tensor** for compressed circuit generation.
* The `.xlsx` files contain recorded results used for analysis, plotting, and paper figures.
* You will need to set up a Qiskit runtime service with IBM quantum API and instance credentials.


