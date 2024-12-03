
# Algorithms in Structural Bioinformatics Assignments

This repository contains two assignments from the "Algorithms in Structural Bioinformatics" graduate course of the MSc Data Science & Information Technologies Master's programme (Bioinformatics - Biomedical Data Science Specialization) of the Department of Informatics and Telecommunications department of the National and Kapodistrian University of Athens (NKUA), under the supervision of professors Ioannis Emiris and Evangelia Chrysina, in the academic year 2022-2023. The assignments explore various computational techniques in structural bioinformatics, including RNA folding, molecular conformational analysis, and protein structure comparison. The implementation leverages Python and its bioinformatics libraries, with additional visualization tools for molecular structures.

## Assignment 1: RNA Folding and RMSD Analysis

**Key Tasks:**
1. **RNA Folding**:
    - Implemented a crude energy minimization algorithm to predict optimal secondary structures of an RNA sequence.
    - Visualized the energy matrix as a heatmap and manually backtracked to determine folding patterns.
    - Tools: Python, NumPy, Matplotlib, Seaborn.
2. **RMSD Analysis**:
    - Computed c-RMSD (coordinate root-mean-square deviation) and d-RMSD (distance root-mean-square deviation) for a set of molecular conformations.
    - Identified L1-centroid conformations and compared computation methods using different metrics and data subsets.
    - Visualized pairwise distance matrices as heatmaps.
    - Tools: Python, NumPy, Seaborn, Matplotlib.
3. **Matrix Rank and Perturbations**:
    - Analyzed the rank of Cayley-Menger matrices derived from SARS-CoV-2 protease structures and investigated changes under perturbations.

**Main Results:**
- Predicted RNA folding structures and validated them with a heatmap.
- Identified centroid conformations using c-RMSD and d-RMSD. Variations in results highlighted metric-specific centroid biases and computational trade-offs.
- Matrix perturbation increased rank, reflecting structural variability.

## Assignment 2: Structural Analysis of Serotonin Receptor

**Key Tasks:**
1. **Structural Information Extraction**:
    - Explored the PDBe entry (PDB ID: 7e2y) for the human serotonin receptor to analyze structural details, including:
        - Method of determination (cryo-EM, resolution 3.00 Å).
        - Chain composition and ligands.
2. **Molecular Visualization**:
    - Prepared figures using ChimeraX to visualize secondary structure elements (color-coded by chain) and distinct molecular components.
3. **Comparative Analysis**:
    - Computed RMSD values between the human serotonin receptor (PDB ID: 7e2y) and its chicken counterpart predicted by AlphaFold.
    - Conducted RMSD analyses over all atoms, Cα atoms, and secondary structure elements using PyMOL and Biopython.

**Main Results:**
- All-atom RMSD: 9.131 Å, indicating significant structural differences.
- Cα RMSD: 1.100 Å, suggesting a higher similarity in backbone structures.
- Secondary structure RMSD: 34.215 Å, reflecting major conformational differences in secondary elements.

## Cloning the Repository

```sh
git clone https://github.com/GiatrasKon/Algorithms-in-Structural-Bioinformatics-Assignments.git
```

## Repository Structure

### Assignment 1
- **data/**
    - `6LU7.pdb`: PDB file for SARS-CoV-2 protease.
    - `10_conformations.txt`: Molecular conformations data.
- **documents/**
    - `asg1.pdf`: Assignment 1 description.
    - `GiatrasKonstantinos - Assignment#1 - AiSB.pdf`: Completed report.
- **images/**
    - `CEM_heatmap.png`: Crude Energy Minimization heatmap.
    - `backtrack_path1.jpg`: Visual of RNA backtracking (Path 1).
    - `optimal_fold1.png`: Optimal RNA folding (Path 1).
    - `backtrack_path2.jpg`: Visual of RNA backtracking (Path 2).
    - `optimal_fold2.png`: Optimal RNA folding (Path 2).
    - `cRMSD_heatmap.png`: Pairwise c-RMSD heatmap.
    - `dRMSD_heatmap.png`: Pairwise d-RMSD heatmap.
    - `dRMSD2_heatmap.png`: Heatmap for subset d-RMSD.
- **notebooks/**
  - `AiSB_Assignment_1_Giatras_Konstantinos.ipynb`: Jupyter notebook for Assignment 1.

### Assignment 2
- **data/**
    - `7e2x.pdb`: Human serotonin receptor in the absence of serotonin (PDB: 7e2x).
    - `7e2y.pdb`: Human serotonin receptor in the presence of serotonin (PDB: 7e2y).
    - `7e2y.dssp`: Secondary structure elements for 7e2y.
    - `AF-D2K8P9-F1-model_v4.pdb`: AlphaFold-predicted chicken serotonin receptor.
    - `AF-D2K8P9-F1-model_v4.dssp`: Secondary structure elements for chicken serotonin receptor.
- **documents/**
    - `Assignment2_24May23.pdf`: Assignment 2 description.
    - `GiatrasKonstantinos - Assignment#2 - AiSB.pdf`: Completed report.
- **images/**
    - `figure1.png`: Visualization of secondary structure elements of the 7e2y protein coloured by chain.
    - `figure2.png`: Visualization of chemically distinct molecules in the 7e2y structure.
    - `ligands.png`: Highlighted ligands in the 7e2y structure.
- **scripts/**
    - `RMSD_secondary_structures.py`: Python script for secondary structure elements RMSD calculation.

## Package Dependencies

- **NumPy**: For numerical operations and matrix computations.
- **Matplotlib**: For plotting and visualizations.
- **Seaborn**: For creating heatmaps and enhanced data visualizations..
- **Biopython**: For handling PDB files and structural bioinformatics tasks.
- **PyMOL (open-source)**: For RMSD analysis and structural alignment.
- **[ChimeraX](https://www.cgl.ucsf.edu/chimerax/download.html)**: For molecular visualizations (installed separately; not a Python package).

You can install all the dependencies at once using the following command:

```sh
pip install numpy matplotlib seaborn biopython pymol-open-source
```

---