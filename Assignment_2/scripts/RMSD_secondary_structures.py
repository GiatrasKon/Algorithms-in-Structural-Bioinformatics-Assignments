from Bio.PDB import PDBParser, Superimposer

# PDB file paths
pdb1_path = "7e2y.pdb"
pdb2_path = "AF-D2K8P9-F1-model_v4.pdb"

# DSSP file paths
dssp1_path = "7e2y.dssp"
dssp2_path = "AF-D2K8P9-F1-model_v4.dssp"

# Parse the PDB files to get the structures
pdb_parser = PDBParser()
structure1 = pdb_parser.get_structure("7e2y", pdb1_path)
structure2 = pdb_parser.get_structure("AF-D2K8P9-F1-model_v4", pdb2_path)

# Parse the DSSP files to get the secondary structure elements
def parse_dssp(dssp_path):
    with open(dssp_path) as f:
        lines = f.readlines()[28:]  # DSSP secondary structure starts from line 29
        return [line[16] for line in lines if len(line) > 16 and line[16] in 'EHBIGST']

dssp1 = parse_dssp(dssp1_path)
dssp2 = parse_dssp(dssp2_path)

# Get the atom coordinates for secondary structure elements
def get_secondary_structure_atoms(structure, dssp):
    atoms = []
    for model in structure:
        for chain in model:
            for i, residue in enumerate(chain):
                # Get the residue number
                res_num = residue.get_id()[1]

                # If we have a secondary structure element for this residue
                if res_num < len(dssp) and dssp[res_num] != '-':
                    try:
                        atoms.append(residue["CA"])
                    except:
                        continue
    return atoms

atoms1 = get_secondary_structure_atoms(structure1, dssp1)
atoms2 = get_secondary_structure_atoms(structure2, dssp2)

# Modify this section to use the smaller number of atoms from atoms1 and atoms2
min_length = min(len(atoms1), len(atoms2))
super_imposer = Superimposer()
super_imposer.set_atoms(atoms1[:min_length], atoms2[:min_length])

print("secondary structure elements RMSD:", super_imposer.rms, "Angstrom")