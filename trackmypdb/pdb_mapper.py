import requests

def pdb_to_uniprot(pdb_id):

    url = f"https://data.rcsb.org/rest/v1/core/polymer_entity_instance/{pdb_id}/1"

    try:
        r = requests.get(url, timeout=10)

        data = r.json()

        uniprot_ids = []

        annotations = data.get("rcsb_polymer_entity_instance_container_identifiers", {})

        if "uniprot_ids" in annotations:
            uniprot_ids = annotations["uniprot_ids"]

        return uniprot_ids

    except:
        return []
