import random 
import json
from pathlib import Path

#define helper functions for lab values and conditions

def  generate_hba1c():   
     return round(random.uniform(6.5, 9.5), 1)

def generate_bmi():
    return round(random.uniform(25.0, 35.0), 1)

def generate_age():
     return random.randint(40, 65)

def generate_ethnicity():
     return random.choice(["White", "Black", "Hispanic", "Asian", "Other"])

def generate_conditions():
     base_conditions = ["Type 2 Diabetes"]
     optional_conditions = ["Hypertension", "Hyperlipidemia", "Obesity"]
     return base_conditions + random.sample(optional_conditions, random.randint(0, 2))

def generate_sex():
     return random.choice(["Male", "Female"])

def generate_medications():
     base_meds = ["Metformin"]
     optional_meds = ["Lisinopril", "Atorvastatin", "Lifestyle Therapy"]
     return base_meds + random.sample(optional_meds, random.randint(0, 2))

#generator function
def generate_patient(patient_id):
     patient = {
          "patient_id": patient_id,
          "age": generate_age(),
          "sex": generate_sex(),
          "ethnicity": generate_ethnicity(),
          "bmi": generate_bmi(),
          "hba1c": generate_hba1c(),
          "conditions": generate_conditions(),
          "medications": generate_medications(),
          "meets criteria": True   #logic assumes generation meets criteria
     }
     return patient

if __name__ == "main":
     out_dir = Path("../synthetic_data/")
     out_dir.mkdir(exist_ok=True)

     patients = []
     for i in range(100):
          pid = f"P{i:04d}"
          patient = generate_patient(pid)
          patients.append(patient)
    
     with open(out_dir / "patients_sample.json", "w") as f:
         json.dump(patients, f, indent = 2)