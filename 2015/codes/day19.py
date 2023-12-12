with open('../inputs/day19') as f:
    lines=f.read().strip().split('\n')

lines.pop(-2)
replacements = [line.split(' => ') for line in lines][:-2]
molecule = lines[-1]

def apply_replacement(molecule, replacement):
    result = []
    for i in range(len(molecule)):
        if molecule[i:i+len(replacement[0])] == replacement[0]:
            result.append(molecule[:i] + replacement[1] + molecule[i+len(replacement[0]):])
    return result

def count_distinct_molecules(replacements, molecule):
    distinct_molecules = set()

    for replacement in replacements:
        result_molecules = apply_replacement(molecule, replacement)
        distinct_molecules.update(result_molecules)

    return len(distinct_molecules)

count_distinct_molecules(replacements, molecule)
