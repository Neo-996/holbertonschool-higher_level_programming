import os

def generate_invitations(template, attendees):
    # Validate that the template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Validate that attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty template
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendee list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Loop through each attendee and generate their invitation
    for idx, attendee in enumerate(attendees, start=1):
        content = template  # Copy the original template

        # Replace each placeholder with actual values or "N/A" if missing
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            content = content.replace(f"{{{key}}}", value if value else "N/A")

        # Create a unique output filename for each attendee
        filename = f"output_{idx}.txt"

        # Write the filled template to the output file
        try:
            with open(filename, 'w') as output_file:
                output_file.write(content)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
