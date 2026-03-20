def analyze(log):

    if "Still waiting for root device" in log:
        return "Storage controller issue"

    if "IOConsoleUsers" in log:
        return "GPU framebuffer issue"

    if "Unsupported CPU" in log:
        return "CPU spoof required"

    return "Unknown panic"
