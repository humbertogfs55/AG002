import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Read the CSV file into a DataFrame
df = pd.read_csv('palmerpenguins.csv')

# region (1)Replace mapping for species, island, and sex:
species_mapping = {
    'Adelie': 0,
    'Chinstrap': 1,
    'Gentoo': 2
}
island_mapping = {
    'Biscoe': 0,
    'Dream': 1,
    'Torgersen': 2
}
sex_mapping = {
    'FEMALE': 0,
    'MALE': 1
}

df['species'] = df['species'].replace(species_mapping)
df['island'] = df['island'].replace(island_mapping)
df['sex'] = df['sex'].replace(sex_mapping)

#endregion
# region (2)Reordering columns:

desired_order = ['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species']

df = df.reindex(columns=desired_order)

# endregion
# region (3)Separating data into training and testing:

X = df.drop(columns='species')  # Features, Independent variables contains all columns besides species
y = df['species']               # Target, dependent variable, contains the column species

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting data sets
#print("X_train shape:", X_train.shape)
#print("X_test shape:", X_test.shape)
#print("y_train shape:", y_train.shape)
#print("y_test shape:", y_test.shape)

# endregion
# region (4)Training decision tree classifier:

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)

# endregion
# region (5)using predict on the test sample

y_pred = dtc.predict(X_test)

# endregion
# region (6)Evaluating model:

accuracy = accuracy_score(y_test, y_pred)

report = classification_report(y_test, y_pred)

with open('evaluation_results.txt', 'w') as file:
    file.write(f"Accuracy: {accuracy:.2f}\n")
    file.write("Classification Report:\n")
    file.write(report)
print("Evaluation results saved to 'evaluation_results.txt' file.")
# endregion
# region (7)User input:

# Prompt user to input penguin data
culmen_length = float(input("Enter culmen length (in mm): "))
culmen_depth = float(input("Enter culmen depth (in mm): "))
flipper_length = float(input("Enter flipper length (in mm): "))
body_mass = float(input("Enter body mass (in grams): "))
island = input("Enter island (Biscoe, Dream, or Torgersen): ")
sex = input("Enter sex (Male or Female): ")

# Preprocess user input
# Convert island and sex to numeric values
island_mapping = {'Biscoe': 0, 'Dream': 1, 'Torgersen': 2}
sex_mapping = {'Male': 1, 'Female': 0}
island_numeric = island_mapping.get(island, -1)  # -1 if island not found
sex_numeric = sex_mapping.get(sex, -1)          # -1 if sex not found

# Check if island and sex are valid
if island_numeric == -1 or sex_numeric == -1:
    print("Invalid island or sex. Please enter 'Biscoe', 'Dream', 'Torgersen' for island and 'Male' or 'Female' for sex.")
else:
    # Make prediction
    penguin_data = [[island_numeric, sex_numeric, culmen_length, culmen_depth, flipper_length, body_mass]]
    # Provide feature names during prediction
    predicted_species = dtc.predict(penguin_data)

# Display predicted species
species_mapping = {0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo'}
predicted_species_name = species_mapping.get(predicted_species[0], 'Unknown')
print(f"The predicted species for the input penguin is: {predicted_species_name}")

# endregion