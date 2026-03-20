import plistlib

def generate_config():

    config = {
        "ACPI":{},
        "Booter":{},
        "DeviceProperties":{},
        "Kernel":{},
        "Misc":{},
        "NVRAM":{},
        "PlatformInfo":{},
        "UEFI":{}
    }

    return plistlib.dumps(config)
