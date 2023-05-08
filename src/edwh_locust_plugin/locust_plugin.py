import csv
import glob
import json
from pathlib import Path
from statistics import median

from invoke import task


@task()
def output(c, bestand):
    """is ervoor gemaakt om de locust output (csv) naar een Excel bestand over te zetten
    bestand: naam van het bestand"""
    with open(bestand, "r") as file:
        lines = [json.loads(_) for _ in file.read().replace("}{", "}\n{").split("\n")]

    with open(bestand, "w", newline="") as csvfile:
        csv_writer = csv.DictWriter(
            csvfile, dialect="excel", fieldnames=lines[0].keys()
        )
        csv_writer.writeheader()
        for line in lines:
            csv_writer.writerow(line)


@task()
def median_of_output(c):
    """Verander het path naar de goede path: bestanden & bestand.replace
    de /**/ betekent dat die in die directory gaat kijken en uiteindelijk naar iets kijkt wat eindigt op een ".cvs\" """
    list_50 = []
    list_95 = []
    list_rps = []
    results = {}

    locust_output_path = Path.home() / "locust_output"

    csv_files = glob.glob(f"{locust_output_path}/**/**/*.csv")
    for csv_file in csv_files:
        with open(csv_file, "r") as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                median_50 = row["median respone time 50"]
                # if len(row['median respone time 50']) == 1:
                #     median_50 = row['median respone time 50'].replace('0', '10000')
                list_50.append(float(median_50))
                median_95 = row["median respone time 95"]
                # if len(row['median respone time 95']) == 1:
                #     median_95 = row['median respone time 95'].replace('0', '10000')
                list_95.append(float(median_95))
                rps = row["total rps"]
                list_rps.append(float(rps))

        results["which one"] = csv_file.replace(f"{locust_output_path}/", "")
        results["median of median response time 50"] = median(sorted(list_50))
        results["average of median response time 50"] = sum(list_50) / len(
            list_50
        )
        results["median of median response time 95"] = median(sorted(list_95))
        results["average of median response time 95"] = sum(list_95) / len(
            list_95
        )
        results["average rps"] = sum(list_rps) / len(list_rps)
        print(results)
