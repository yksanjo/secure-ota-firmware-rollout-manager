from datetime import datetime, timezone


def main() -> None:
    print("secure-ota-firmware-rollout-manager initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
