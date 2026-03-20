import platform

def detect_cpu():

    cpu = platform.processor()

    if "13" in cpu:
        gen = "Raptor Lake"

    elif "12" in cpu:
        gen = "Alder Lake"

    else:
        gen = "Unknown"

    return {
        "name": cpu,
        "generation": gen
    }
