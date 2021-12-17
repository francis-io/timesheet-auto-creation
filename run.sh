
docker build -t timesheet-creator:latest .
docker run --rm -it -v $(pwd):/output timesheet-creator:latest
