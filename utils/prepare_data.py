import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get base directory and output file from environment variables
base_dir = os.getenv('BASE_DIR', 'data/nba')
output_file = os.getenv('OUTPUT_FILE', 'data/nba/three_pointer_shots.csv')

def find_calde_mentions(base_dir=base_dir):
    """
    Searches for mentions of 'Calde' in CSV files within the specified directory.
    
    Args:
        base_dir (str): Base directory to search for CSV files
        
    Returns:
        dict: Dictionary with file names and the rows where 'Calde' was found
    """
    results = {}
    
    # Create a DataFrame to store 3-point shots
    three_pointer_shots = pd.DataFrame()

    # Traverse all files in the directory
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                try:
                    # Read the CSV file
                    df = pd.read_csv(file_path)
                    
                    # Search for 'Calde' in all columns
                    mask = df.astype(str).apply(lambda x: x.str.contains('José Calderón', case=False, na=False))
                    
                    # If any matches are found
                    if mask.any().any():
                        # Get the rows that contain 'Calde'
                        matches = df[mask.any(axis=1)]
                        results[file_path] = matches
                        
                        print(f"\nFound 'José Calderón' in {file_path}")
                        print(f"Number of matches: {len(matches)}")
                        
                        # Filter 3-point shots
                        three_pointer = matches[matches['shot_type'] == '3-pointer']
                        three_pointer_shots = pd.concat([three_pointer_shots, three_pointer])
                
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")
    
    # Save the 3-point shots to a new CSV file
    if not three_pointer_shots.empty:
        three_pointer_shots.to_csv(output_file, index=False)
        print(f"\n3-point shots saved to '{output_file}'.")

    return results

if __name__ == "__main__":
    results = find_calde_mentions()
    
    # Show detailed results
    for file_path, matches in results.items():
        print(f"\nFile: {file_path}")
        print(matches)
