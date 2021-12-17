
docker build -t timesheet-creator:latest .
docker run --rm -it -p 5000:5000 -v $(pwd):/output timesheet-creator:latest
