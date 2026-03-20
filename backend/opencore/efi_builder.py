import os

def build():

    folders = [
        "EFI/BOOT",
        "EFI/OC",
        "EFI/OC/Kexts",
        "EFI/OC/ACPI",
        "EFI/OC/Drivers",
        "EFI/OC/Tools"
    ]

    for f in folders:
        os.makedirs(f,exist_ok=True)

    return {"status":"EFI created"}
