# structured-nut

Small forwarder that polls NUT (`upsc`) and emits JSON (GELF-like) lines to stdout.

## Files
- [Dockerfile](Dockerfile): builds a minimal image based on `python:3.12-slim` and installs `nut-client`.
- [app.py](app.py): Python forwarder; prints JSON events to stdout.

## Environment
- `UPS_NAME` (optional): UPS identifier for `upsc` (default: `myups@nut`).
- `INTERVAL` (optional): polling interval in seconds (default: `10`).

## Build (Docker)
Build the image:

```bash
docker build -t structured-nut:latest .
```

Run the container (example):

```bash
docker run --rm --name structured-nut structured-nut:latest
```

To set a custom UPS and interval:

```bash
docker run --rm -e UPS_NAME="upsname@host" -e INTERVAL=30 structured-nut:latest
```

## Run locally (for debugging)
Requires `upsc` available on the host (part of NUT client). Then run:

```bash
python app.py
```

## Validation performed
- `app.py`: Python syntax check (no syntax errors).
- `Dockerfile`: Basic structure looks valid; it installs `nut-client` via `apt-get` and runs `app.py`.

Notes:
- Confirm the package name `nut-client` exists on the base image's package repositories for your target platform. If not, adjust the `apt-get install` line to the correct package (e.g., `nut`, `nut-client`, or `nut-server` depending on distro).
- Consider adding `--no-install-recommends` and a non-root user for smaller, safer images.

## Next steps
- (Optional) Add a simple healthcheck or logging configuration.
- (Optional) Add CI checks to build the image and run the app.
