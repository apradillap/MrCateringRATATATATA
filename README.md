# MrCateringRATATATATA

This project aims to analyze basketball shots using the NBA shots dataset from 2001 to the present. It focuses on mentions of the player José Calderón and his 3-point shots.

## Links
- Kaggle: [NBA Shots Dataset](https://www.kaggle.com/datasets/techbaron13/nba-shots-dataset-2001-present)

## Installation

1. **Create a virtual environment**:
   ```bash
   python3 -m venv MrCateringRATATATATA
   ```

2. **Activate the virtual environment**:
   ```bash
   source MrCateringRATATATATA/bin/activate
   ```

3. **Install Dependencies**
Install the required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

4. **Update the requirements.txt file**
Freeze the current dependencies and update the `requirements.txt` file:
```bash
pip freeze > requirements.txt
```

5. **Prepare the data**
Run the script to search for mentions of 'José Calderón' and filter his 3-point shots:
```bash
python utils/prepare_data.py
```

The results will be saved in a new CSV file named `three_pointer_shots.csv` in the `data` directory.