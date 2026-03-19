import datetime as dt
 
VALID_LEVELS = {"INFO", "WARNING", "ERROR", "DEBUG"}
file_path = "logs"

def write_log(message: str, 
              file_name: str ="log", 
              job: str | None = None, 
              level: str ='INFO'
              ) -> None:
    # Check level if valid
    level = level.upper()
    if level not in VALID_LEVELS:
        message = f"Invalid level: ({level}) {message}"
        level = "ERROR"

    timestamp = dt.datetime.now()
    current_date = timestamp.strftime("%Y-%m-%d")
    current_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

    # Message to write file and print terminal:
    if job:
        mes = f"{current_timestamp} | {job} | {level} | {message}"
    else:
        mes = f"{current_timestamp} | {level} | {message}"

    # Write to log file and terminal
    with open(f"{file_path}/{file_name}-{current_date}.log", "a", encoding="utf-8") as f:
        f.write(f"{mes}\n")

    print(mes)