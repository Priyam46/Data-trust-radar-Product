from freshness_score import calculate_freshness_score
from volume_score import calculate_volume_score
from schema_score import calculate_schema_score
from impact_score import calculate_impact_score
from final_score import calculate_final_score
from datetime import datetime
import csv

def run_scoring(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ["trust_score"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in reader:
            freshness = calculate_freshness_score(
                datetime.fromisoformat(row["last_updated"]),
                int(row["expected_frequency_hours"])
            )

            volume = calculate_volume_score(
                int(row["current_row_count"]),
                int(row["historical_avg_row_count"])
            )

            schema = calculate_schema_score(int(row["schema_changes"]))
            impact = calculate_impact_score(int(row["downstream_dashboards"]), row["business_criticality"])

            final_score = calculate_final_score(freshness, volume, schema, impact)

            row["trust_score"] = final_score
            writer.writerow(row)

if __name__ == "__main__":
    run_scoring("../sample-data/dataset_metadata.csv", "../sample-data/trust_score_output.csv")
