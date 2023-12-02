TAX_CONSULTING_TEMPLATE_PATH = "data/sow_templates/tax_consulting_sow.txt"
TAX_COMPLIANCE_TEMPLATE_PATH = "data/sow_templates/tax_compliance_sow.txt"


def get_sow_temlpate(sowType) -> str:
    if sowType == "Tax Consulting SOW":
        f = open(TAX_CONSULTING_TEMPLATE_PATH, "r")
        return f.read()
    elif sowType == "Tax Compliance SOW":
        f = open(TAX_COMPLIANCE_TEMPLATE_PATH, "r")
        return f.read()
    else:
        return "No template found"