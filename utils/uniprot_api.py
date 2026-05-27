import requests

UNIPROT_URL = "https://rest.uniprot.org/uniprotkb/search"


def validate_uniprot_ids(ids):
    """
    Validate and enrich UniProt IDs using real UniProt API
    """

    valid = []

    for uid in ids:
        url = f"{UNIPROT_URL}?query={uid}&format=json"

        try:
            r = requests.get(url, timeout=10)

            if r.status_code == 200 and len(r.json().get("results", [])) > 0:
                valid.append(uid)

        except:
            continue

    return valid
